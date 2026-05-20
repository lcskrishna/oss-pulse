#!/usr/bin/env python3
"""
Track weekly changes in a GitHub repository and produce a structured report.

Supports ROCm/aiter and ROCm/mori with repo-specific component classifiers.
Easily extensible to any other repo via REPO_CLASSIFIERS below.

Usage:
    python3 track_repo_changes.py [--repo OWNER/REPO] [--since YYYY-MM-DD]
                                  [--until YYYY-MM-DD] [--output-dir PATH]
                                  [--format {md,csv,both}] [--no-files]

Defaults:
    --repo    ROCm/aiter
    --since   7 days ago
    --format  both

Requires: gh CLI authenticated
"""

import argparse
import csv
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# Per-repo component classifiers
# Each entry: (display_label, [keywords matched against lowercased
#              commit message + changed file paths])
# Order matters — first match wins.
# ---------------------------------------------------------------------------

REPO_CLASSIFIERS: dict[str, list] = {

    "ROCm/aiter": [
        ("MoE",                 ["moe", "fused_moe", "expert", "topk", "gating", "moe_sorting"]),
        ("MLA",                 ["mla", "multi_latent", "concat_cache_mla"]),
        ("MHA / Attention",     ["mha", "fmha", "flash_attn", "batch_prefill", "varlen"]),
        ("Paged Attention",     ["paged_attn", "pa_", "/pa.", "kvcache"]),
        ("GEMM",                ["gemm", "tuned_gemm", "deepgemm", "batched_gemm", "scaled_mm"]),
        ("Quantization",        ["quant", "mxfp4", "fp8", "int4", "int8", "smoothquant", "blockscale"]),
        ("RMSNorm / LayerNorm", ["rmsnorm", "layernorm", "groupnorm", "fused_qk_norm"]),
        ("RoPE / Embedding",    ["rope", "rotary", "embedding"]),
        ("Sampling",            ["sampling", "sample"]),
        ("Triton Kernels",      ["triton", "gluon"]),
        ("CK / CK_TILE",        ["ck_tile", "cktile", "[ck]", "composable_kernel"]),
        ("OPUS / ASM",          ["opus", "hsa/", "asm", "gfx942", "gfx950", "gfx1201"]),
        ("CI / Build",          ["ci:", "[ci]", "cmake", "setup.py", "pyproject", "requirements",
                                  "auto-update", "split test", "githooks"]),
        ("Docs",                ["readme", "docs/", "changelog", "contribute"]),
    ],

    "ROCm/mori": [
        # Applications — highest priority, most specific
        ("MORI-EP (Expert Parallel)",   ["src/ops", "dispatch_combine", "ep_local", "internode",
                                          "(ep)", "feat(ep)", "fix(ep)", "perf(ep)",
                                          "mori-ep", "dispatch", "combine"]),
        ("MORI-IO (KVCache / P2P)",     ["src/io", "python/mori/io", "scatter_gather",
                                          "(io)", "feat(io)", "fix(io)",
                                          "mori-io", "kvcache", "p2p", "xgmi fallback"]),
        ("MORI-CCL (Collectives)",      ["src/collective", "python/mori/ccl", "allgather",
                                          "allreduce", "all2all", "collective",
                                          "(ccl)", "feat(ccl)", "fix(ccl)"]),
        ("MORI-UMBP (Memory Pool)",     ["src/umbp", "umbp", "memory pool", "tiered"]),
        # Framework building blocks
        ("RDMA / Transport",            ["rdma", "ibgda", "transport", "qp ", "pollcq",
                                          "connectx", "bnxt", "thor2", "ainic", "pensando",
                                          "ibverbs", "providers/", "mlx5", "mtu"]),
        ("SDMA / Shared Memory",        ["sdma", "shmem", "symmmem", "symmetric_memory",
                                          "src/shmem", "smem"]),
        ("Bootstrap / Topology",        ["bootstrap", "topology", "socket_bootstrap",
                                          "torch_bootstrap", "mpi_bootstrap"]),
        ("Memory / VA Management",      ["memory_region", "va_manager", "allocator",
                                          "memory region", "va manager"]),
        ("JIT / IR / FlyDSL",           ["jit", "flydsl", "fly_dsl", "python/mori/ir",
                                          "bitcode", "(jit)", "feat(jit)", "fix(jit)"]),
        ("Quantization",                ["fp8", "blockwise", "quant", "int8"]),
        ("CI / Build",                  ["ci:", "[ci]", "cmake", "workflow", "nightly",
                                          "wheel", "pypi", "gh-pages", "docker"]),
        ("Env / Config",                ["env_setup", "env_check", "(env)", "feat(env)",
                                          "fix(env)", "dscp", "mori_enable", "mori_disable"]),
        ("CLI / Tools",                 ["(cli)", "feat(cli)", "console entry", "tools/"]),
        ("Docs",                        ["readme", "docs/", "changelog", "changelog"]),
        ("Benchmarks / Tests",          ["benchmark/", "tests/", "perf test", "latency", "bandwidth"]),
    ],
}

# Fallback generic classifier used when a repo isn't in REPO_CLASSIFIERS
GENERIC_RULES = [
    ("Fix",         ["fix", "bugfix", "bug fix", "hotfix"]),
    ("Feature",     ["feat", "feature", "add", "implement"]),
    ("Performance", ["perf", "optim", "speed", "throughput", "latency"]),
    ("CI / Build",  ["ci", "cmake", "build", "workflow", "docker"]),
    ("Docs",        ["readme", "docs", "changelog"]),
    ("Refactor",    ["refactor", "cleanup", "reorg", "restructure"]),
    ("Test",        ["test", "bench"]),
]


def get_rules(repo: str) -> list:
    return REPO_CLASSIFIERS.get(repo, GENERIC_RULES)


def classify(commit: dict, rules: list) -> str:
    msg = commit["message"].lower()
    files = [f.lower() for f in commit.get("files", [])]
    combined = msg + " " + " ".join(files)
    for label, keywords in rules:
        if any(kw in combined for kw in keywords):
            return label
    return "Other"


# ---------------------------------------------------------------------------
# GitHub helpers
# ---------------------------------------------------------------------------

def gh_get(path: str):
    result = subprocess.run(
        ["gh", "api", "--paginate", path],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        sys.exit(f"gh API error for {path}:\n{result.stderr.strip()}")
    text = result.stdout.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        arrays = re.findall(r"\[.*?\]", text, re.DOTALL)
        merged = []
        for a in arrays:
            try:
                merged.extend(json.loads(a))
            except Exception:
                pass
        return merged


def fetch_commits(repo: str, since: str, until: str) -> list:
    path = (
        f"repos/{repo}/commits"
        f"?since={since}T00:00:00Z&until={until}T23:59:59Z&per_page=100"
    )
    raw = gh_get(path)
    commits = []
    for c in raw:
        msg = c["commit"]["message"]
        pr_num = _extract_pr(msg)
        commits.append({
            "sha":          c["sha"][:10],
            "date":         c["commit"]["author"]["date"][:10],
            "author":       c["commit"]["author"]["name"],
            "message":      msg.split("\n")[0].strip(),
            "pr":           pr_num,
            "files":        [],
            "component":    "",
        })
    return commits


def _extract_pr(msg: str) -> str:
    m = re.search(r"\(#(\d+)\)", msg)
    return m.group(1) if m else ""


def fetch_commit_files(repo: str, sha: str) -> list:
    try:
        data = gh_get(f"repos/{repo}/commits/{sha}")
        return [f["filename"] for f in data.get("files", [])]
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Report builders
# ---------------------------------------------------------------------------

def build_markdown(commits: list, repo: str, since: str, until: str, by_component: dict) -> str:
    total = len(commits)
    lines = []
    lines.append(f"# {repo} — Weekly Change Report")
    lines.append(f"**Period:** {since} → {until}  |  **Total commits:** {total}\n")

    lines.append("## Summary by Component\n")
    lines.append("| Component | Commits |")
    lines.append("|-----------|:-------:|")
    for comp, items in sorted(by_component.items(), key=lambda x: -len(x[1])):
        lines.append(f"| {comp} | {len(items)} |")
    lines.append("")

    for comp, items in sorted(by_component.items(), key=lambda x: -len(x[1])):
        lines.append(f"## {comp}  ({len(items)} commits)\n")
        for c in items:
            pr_link = (
                f" [#{c['pr']}](https://github.com/{repo}/pull/{c['pr']})"
                if c["pr"] else ""
            )
            sha_link = f"[`{c['sha']}`](https://github.com/{repo}/commit/{c['sha']})"
            lines.append(f"- **{c['date']}** {sha_link}{pr_link}")
            lines.append(f"  {c['message']}")
            if c["files"]:
                shown = c["files"][:4]
                suffix = f" _+{len(c['files'])-4} more_" if len(c["files"]) > 4 else ""
                lines.append(f"  _Files: `{'`, `'.join(shown)}`{suffix}_")
        lines.append("")

    lines.append("---")
    lines.append(f"_Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_")
    return "\n".join(lines)


def build_csv(commits: list, repo: str) -> list:
    return [
        {
            "date":      c["date"],
            "sha":       c["sha"],
            "pr":        c["pr"],
            "component": c["component"],
            "message":   c["message"],
            "author":    c["author"],
            "files":     "; ".join(c["files"][:6]),
            "url":       f"https://github.com/{repo}/commit/{c['sha']}",
        }
        for c in commits
    ]


# ---------------------------------------------------------------------------
# Dashboard updater  (updates reports/ROCm_aiter/README.md)
# ---------------------------------------------------------------------------

def update_dashboard_index(output_dir: Path, repo: str, since: str, until: str,
                           by_component: dict, total: int):
    index_path = output_dir / "README.md"
    repo_slug = repo.replace("/", "_")

    # Collect existing report links
    existing = []
    if index_path.exists():
        for line in index_path.read_text().splitlines():
            if line.startswith("| [") and "→" in line:
                existing.append(line)

    # New entry for this run
    md_name = f"{repo_slug}_{since}_to_{until}.md"
    top_comp = max(by_component.items(), key=lambda x: len(x[1]), default=("—", []))
    new_entry = (
        f"| [{since} → {until}](./{md_name})"
        f" | {total}"
        f" | {top_comp[0]} ({len(top_comp[1])})"
        f" | {', '.join(sorted(by_component.keys())[:4])} |"
    )
    # Avoid duplicate for same date range
    existing = [l for l in existing if f"{since} → {until}" not in l]
    existing.insert(0, new_entry)

    lines = [
        f"# {repo} — Change Reports\n",
        f"Weekly commit digests for [`{repo}`](https://github.com/{repo}).\n",
        "| Period | Commits | Top Area | Areas Changed |",
        "|--------|:-------:|----------|---------------|",
    ]
    lines += existing[:12]   # keep last 12 weeks
    lines += [
        "",
        "---",
        f"_Last updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_",
    ]
    index_path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    today = datetime.now(timezone.utc).date()
    week_ago = today - timedelta(days=7)

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo",       default="ROCm/aiter")
    parser.add_argument("--since",      default=str(week_ago), help="Start date YYYY-MM-DD")
    parser.add_argument("--until",      default=str(today),    help="End date YYYY-MM-DD")
    parser.add_argument("--output-dir", default=None,
                        help="Directory for output files (default: reports/<repo_slug>/)")
    parser.add_argument("--format",     default="both", choices=["md", "csv", "both"])
    parser.add_argument("--no-files",   action="store_true",
                        help="Skip per-commit file fetching (faster, less detail)")
    args = parser.parse_args()

    repo = args.repo
    since, until = args.since, args.until
    repo_slug = repo.replace("/", "_")

    script_dir = Path(__file__).parent
    output_dir = Path(args.output_dir) if args.output_dir else script_dir.parent / "reports" / repo_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching commits: {repo}  {since} → {until} …")
    commits = fetch_commits(repo, since, until)
    print(f"  Found {len(commits)} commits")

    if not args.no_files and commits:
        print(f"  Fetching changed files …", end="", flush=True)
        for i, c in enumerate(commits):
            c["files"] = fetch_commit_files(repo, c["sha"])
            if (i + 1) % 10 == 0:
                print(f" {i+1}", end="", flush=True)
        print()

    rules = get_rules(repo)
    for c in commits:
        c["component"] = classify(c, rules)

    by_component: dict = defaultdict(list)
    for c in commits:
        by_component[c["component"]].append(c)

    print(f"\nComponent breakdown:")
    for comp, items in sorted(by_component.items(), key=lambda x: -len(x[1])):
        print(f"  {len(items):3d}  {comp}")

    date_tag = f"{since}_to_{until}"

    if args.format in ("md", "both"):
        md_path = output_dir / f"{repo_slug}_{date_tag}.md"
        md_path.write_text(build_markdown(commits, repo, since, until, by_component),
                           encoding="utf-8")
        print(f"\n  Markdown → {md_path}")

    if args.format in ("csv", "both"):
        rows = build_csv(commits, repo)
        csv_path = output_dir / f"{repo_slug}_{date_tag}.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys() if rows else [])
            writer.writeheader()
            writer.writerows(rows)
        print(f"  CSV     → {csv_path}")

    update_dashboard_index(output_dir, repo, since, until, by_component, len(commits))
    print(f"  Index   → {output_dir / 'README.md'}")


if __name__ == "__main__":
    main()
