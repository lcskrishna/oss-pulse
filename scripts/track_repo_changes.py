#!/usr/bin/env python3
"""
Track weekly changes in a GitHub repository and produce a structured report.

Supports ROCm/aiter, ROCm/mori, sgl-project/sglang, vllm-project/vllm,
NVIDIA/TensorRT-LLM, and NVIDIA/TensorRT with repo-specific classifiers.
Also surfaces ROCm-related commits/issues in each report.
Easily extensible via REPO_CLASSIFIERS below.

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
        ("Docs",                        ["readme", "docs/", "changelog"]),
        ("Benchmarks / Tests",          ["benchmark/", "tests/", "perf test", "latency", "bandwidth"]),
    ],

    "sgl-project/sglang": [
        # Core inference features
        ("Prefill / Decode Disaggregation", ["[pd]", "disaggregat", "srt/disaggregation",
                                              "prefill_decode", "pd_disagg", "mooncake"]),
        ("MoE / Expert Parallel",       ["moe", "expert parallel", "eplb", "elastic_ep",
                                          "srt/elastic_ep", "srt/eplb", "fused_moe"]),
        ("Attention / FlashInfer",      ["attention", "flash", "flashinfer", "mla", "mha",
                                          "batch_prefill", "varlen", "nsa", "gqa"]),
        ("KV Cache / Memory",           ["kv cache", "kvcache", "mem_cache", "srt/mem_cache",
                                          "radix", "chunk", "memory pool", "paged"]),
        ("Quantization",                ["quant", "fp8", "int4", "int8", "mxfp4", "awq", "gptq",
                                          "bnb", "blockscale"]),
        ("Multimodal",                  ["multimodal", "vlm", "vision", "image", "video",
                                          "audio", "srt/multimodal", "[vlm]", "diffusion"]),
        ("LoRA",                        ["lora", "srt/lora", "adapter"]),
        ("Speculative Decoding",        ["speculative", "draft", "eagle", "medusa"]),
        ("Structured Output",           ["constrained", "structured", "json schema", "grammar",
                                          "xgrammar", "srt/constrained", "function_call"]),
        ("Scheduler / Batching",        ["scheduler", "batching", "continuous batch",
                                          "srt/managers", "srt/batch"]),
        ("Tensor / Data Parallel",      ["tensor parallel", "data parallel", "tp", "dp",
                                          "srt/distributed", "pipeline"]),
        ("ROCm / AMD",                  ["rocm", "amd", "aiter", "hip", "gfx", "mi3",
                                          "amd-ci", "nightly-test-amd"]),
        ("Triton / Kernels",            ["triton", "sgl-kernel", "kernel", "cuda", "hip kernel"]),
        ("Models",                      ["srt/models", "[model]", "deepseek", "llama", "qwen",
                                          "mistral", "gemma", "phi", "falcon"]),
        ("Serving / API",               ["openai", "api server", "grpc", "http", "srt/entrypoints",
                                          "srt/grpc", "openai compatible"]),
        ("CI / Build",                  ["ci:", "[ci]", "workflow", "docker", "nightly", "cmake"]),
        ("Docs / Examples",             ["readme", "docs", "example", "tutorial"]),
    ],

    "vllm-project/vllm": [
        # ROCm/AMD — highest priority so it's always surfaced
        ("ROCm / AMD",                  ["rocm", "amd", "aiter", "hip", "gfx9", "mi3",
                                          "csrc/rocm", "test-amd", "rocm-base",
                                          "[rocm]", "[amd]", "vllm/_aiter"]),
        # Core inference
        ("MoE / Expert Parallel",       ["moe", "expert parallel", "fused_moe", "topk",
                                          "vllm/model_executor/layers/fused_moe",
                                          "enable-expert-parallel", "ep_size"]),
        ("Attention",                   ["attention", "flash", "flashinfer", "mla", "mha",
                                          "paged_attn", "vllm/attention", "flashattn"]),
        ("KV Cache / Offload",          ["kv cache", "kv offload", "kvcache", "prefix caching",
                                          "vllm/core/block", "radix", "chunk prefill"]),
        ("Quantization",                ["quant", "fp8", "int4", "int8", "mxfp4", "nvfp4",
                                          "awq", "gptq", "blockscale", "csrc/quantization"]),
        ("Speculative Decoding",        ["speculative", "draft", "eagle", "medusa", "ngram"]),
        ("Multimodal",                  ["multimodal", "vlm", "vision", "image", "video",
                                          "audio", "vllm/multimodal", "[vlm]"]),
        ("LoRA",                        ["lora", "vllm/lora", "adapter", "[lora]"]),
        ("Disaggregation / PD",         ["disaggregat", "prefill_decode", "pd_disagg",
                                          "vllm/distributed", "mooncake", "[pd]"]),
        ("Scheduler / Engine",          ["scheduler", "engine", "vllm/engine", "vllm/core",
                                          "continuous batch", "async engine"]),
        ("Compilation / CUDA Graph",    ["cuda graph", "torch.compile", "vllm/compilation",
                                          "piecewise", "graph capture"]),
        ("Models",                      ["vllm/model_executor/models", "[model]", "deepseek",
                                          "llama", "qwen", "mistral", "gemma", "cohere"]),
        ("Serving / API",               ["openai", "api server", "vllm/entrypoints", "grpc",
                                          "vllm serve", "openai compatible"]),
        ("Distributed",                 ["tensor parallel", "pipeline parallel", "vllm/distributed",
                                          "tp_size", "pp_size", "all_reduce"]),
        ("CI / Build",                  ["[ci]", "ci:", "buildkite", "cmake", "docker",
                                          "nightly", "requirements"]),
        ("Perf / Benchmark",            ["[perf]", "benchmark", "throughput", "latency",
                                          "vllm/benchmarks"]),
        ("Docs",                        ["readme", "docs/", "[doc]", "changelog"]),
    ],

    "NVIDIA/TensorRT-LLM": [
        # ROCm/AMD — surface first
        ("ROCm / AMD",                  ["rocm", "amd", "hip", "mi3", "opt_flags_amd",
                                          "triton_kernels/matmul_ogs_details/opt_flags_amd"]),
        # Core features
        ("MoE",                         ["moe", "expert", "mixtral", "topk", "gating",
                                          "cutlass moe", "fused_moe", "moe_backend"]),
        ("Attention",                   ["attention", "flash", "mla", "mha", "fmha",
                                          "flashinfer", "paged kv", "attention_backend"]),
        ("Quantization",                ["quant", "fp8", "int4", "int8", "nvfp4", "mxfp4",
                                          "awq", "gptq", "blockscale", "calibr"]),
        ("Speculative Decoding",        ["speculative", "eagle", "draft", "medusa", "ngram"]),
        ("Disaggregation / KV",         ["disaggregat", "kv transfer", "kv cache",
                                          "_torch/disaggregation", "pd_disagg"]),
        ("LoRA",                        ["lora", "adapter", "lora_manager"]),
        ("Executor / Runtime",          ["executor", "runtime", "trtllm/executor",
                                          "llmapi", "_torch/llm", "overlap scheduling",
                                          "early emission"]),
        ("AutoDeploy",                  ["autodeploy", "auto_deploy", "auto-deploy",
                                          "_torch/auto_deploy"]),
        ("Models",                      ["deepseek", "llama", "qwen", "gemma", "phi",
                                          "falcon", "mistral", "kimi", "gpt"]),
        ("Torch Path (_torch)",         ["_torch/", "torch path", "pytorch"]),
        ("Compilation / Graph",         ["compilation", "cuda graph", "graph rewrite",
                                          "_torch/compilation", "trtllm/compilation"]),
        ("Perf",                        ["[perf]", "perf]", "throughput", "latency", "scheduling"]),
        ("CI / Infra",                  ["[infra]", "[none][infra]", "ci", "nightly", "lock file",
                                          "waive", "blossom", "jenkins"]),
        ("Docs / Examples",             ["readme", "docs/", "example", "changelog"]),
    ],

    "NVIDIA/TensorRT": [
        # TensorRT is lower-velocity; classify by area
        ("Plugins",                     ["plugin/", "custom plugin", "qkv", "nms", "bert",
                                          "fused multihead"]),
        ("ONNX / Parser",               ["onnx", "parser", "graphsurgeon", "onnx_graphsurgeon"]),
        ("Python API",                  ["python/", "pyproject", "pybind"]),
        ("Samples / Demo",              ["sample", "demo/", "quickstart"]),
        ("Build / CMake",               ["cmake", "build", "docker", "toolchain"]),
        ("Quantization",                ["quant", "fp8", "int8", "int4", "calibr", "ptq", "qat"]),
        ("Safety / Embedded",           ["safety", "cudla", "qnx", "aarch64", "jetson"]),
        ("Release / Docs",              ["release", "readme", "docs", "roadmap", "changelog",
                                          "10.", "11."]),
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


# ROCm keywords used to spotlight relevant commits and issues
ROCM_KEYWORDS = ["rocm", "amd", "aiter", "hip", "gfx9", "mi3", "mi300", "mi325", "mi355",
                  "cdna", "mori", "rdma", "ibgda"]


def is_rocm_related(text: str) -> bool:
    t = text.lower()
    return any(kw in t for kw in ROCM_KEYWORDS)


def fetch_rocm_issues(repo: str, since: str) -> list:
    """Fetch open issues updated since `since` that mention ROCm/AMD."""
    try:
        path = f"repos/{repo}/issues?state=open&per_page=100&sort=updated&direction=desc"
        issues = gh_get(path)
        rocm_issues = []
        for i in issues:
            if i.get("pull_request"):   # skip PRs
                continue
            text = (i.get("title", "") + " " + (i.get("body") or "")).lower()
            labels = " ".join(l["name"] for l in i.get("labels", [])).lower()
            if is_rocm_related(text) or is_rocm_related(labels):
                rocm_issues.append({
                    "number":  i["number"],
                    "title":   i["title"],
                    "state":   i["state"],
                    "labels":  ", ".join(l["name"] for l in i.get("labels", [])),
                    "updated": i["updated_at"][:10],
                    "url":     i["html_url"],
                })
        return rocm_issues[:20]   # cap at 20
    except Exception:
        return []


# ---------------------------------------------------------------------------
# New-feature detector — commits that look like additions rather than fixes
# ---------------------------------------------------------------------------

NEW_FEATURE_SIGNALS = ["feat", "add ", "new ", "support", "implement", "introduce",
                        "enable", "[feature]", "✨"]
FIX_SIGNALS         = ["fix", "bugfix", "hotfix", "revert", "workaround", "[fix]"]


def is_new_feature(msg: str) -> bool:
    m = msg.lower()
    if any(s in m for s in FIX_SIGNALS):
        return False
    return any(s in m for s in NEW_FEATURE_SIGNALS)


# ---------------------------------------------------------------------------
# Report builders
# ---------------------------------------------------------------------------

def build_markdown(commits: list, repo: str, since: str, until: str,
                   by_component: dict, rocm_issues: list) -> str:
    total = len(commits)
    lines = []
    lines.append(f"# {repo} — Weekly Change Report")
    lines.append(f"**Period:** {since} → {until}  |  **Total commits:** {total}\n")

    # ── New features spotlight ──────────────────────────────────────────────
    new_features = [c for c in commits if is_new_feature(c["message"])]
    if new_features:
        lines.append("## ✨ New Features This Week\n")
        for c in new_features[:10]:
            pr_link = (f" [#{c['pr']}](https://github.com/{repo}/pull/{c['pr']})"
                       if c["pr"] else "")
            lines.append(f"- **{c['date']}**{pr_link} — {c['message']}")
        if len(new_features) > 10:
            lines.append(f"- _…and {len(new_features)-10} more_")
        lines.append("")

    # ── ROCm spotlight ─────────────────────────────────────────────────────
    rocm_commits = [c for c in commits
                    if is_rocm_related(c["message"]) or
                       any(is_rocm_related(f) for f in c.get("files", []))]
    if rocm_commits or rocm_issues:
        lines.append("## 🔴 ROCm / AMD Spotlight\n")
        if rocm_commits:
            lines.append("### Commits touching ROCm\n")
            for c in rocm_commits:
                pr_link = (f" [#{c['pr']}](https://github.com/{repo}/pull/{c['pr']})"
                           if c["pr"] else "")
                sha_link = f"[`{c['sha']}`](https://github.com/{repo}/commit/{c['sha']})"
                lines.append(f"- **{c['date']}** {sha_link}{pr_link} — {c['message']}")
            lines.append("")
        if rocm_issues:
            lines.append("### Open Issues mentioning ROCm / AMD\n")
            lines.append("| # | Title | Labels | Updated |")
            lines.append("|---|-------|--------|---------|")
            for i in rocm_issues:
                lines.append(
                    f"| [#{i['number']}]({i['url']}) | {i['title'][:70]} "
                    f"| {i['labels'] or '—'} | {i['updated']} |"
                )
            lines.append("")

    # ── Summary table ───────────────────────────────────────────────────────
    lines.append("## Summary by Component\n")
    lines.append("| Component | Commits |")
    lines.append("|-----------|:-------:|")
    for comp, items in sorted(by_component.items(), key=lambda x: -len(x[1])):
        lines.append(f"| {comp} | {len(items)} |")
    lines.append("")

    # ── Per-component detail ────────────────────────────────────────────────
    for comp, items in sorted(by_component.items(), key=lambda x: -len(x[1])):
        lines.append(f"## {comp}  ({len(items)} commits)\n")
        for c in items:
            pr_link = (f" [#{c['pr']}](https://github.com/{repo}/pull/{c['pr']})"
                       if c["pr"] else "")
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
            "date":        c["date"],
            "sha":         c["sha"],
            "pr":          c["pr"],
            "component":   c["component"],
            "new_feature": "yes" if is_new_feature(c["message"]) else "",
            "rocm":        "yes" if (is_rocm_related(c["message"]) or
                                     any(is_rocm_related(f) for f in c.get("files", []))) else "",
            "message":     c["message"],
            "author":      c["author"],
            "files":       "; ".join(c["files"][:6]),
            "url":         f"https://github.com/{repo}/commit/{c['sha']}",
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

    print(f"  Fetching open ROCm/AMD issues …")
    rocm_issues = fetch_rocm_issues(repo, since)
    print(f"  Found {len(rocm_issues)} ROCm-related open issues")

    rocm_commits = [c for c in commits
                    if is_rocm_related(c["message"]) or
                       any(is_rocm_related(f) for f in c.get("files", []))]
    new_feat_count = sum(1 for c in commits if is_new_feature(c["message"]))
    print(f"  New features: {new_feat_count}  |  ROCm commits: {len(rocm_commits)}")

    date_tag = f"{since}_to_{until}"

    if args.format in ("md", "both"):
        md_path = output_dir / f"{repo_slug}_{date_tag}.md"
        md_path.write_text(
            build_markdown(commits, repo, since, until, by_component, rocm_issues),
            encoding="utf-8",
        )
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
