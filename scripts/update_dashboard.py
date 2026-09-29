#!/usr/bin/env python3
"""
Regenerate README.md (the GitHub repo homepage) from all per-repo report files.
Run automatically in CI after track_repo_changes.py.

The GitHub Pages dashboard is a separate artifact — see scripts/build_dashboard.py,
which imports TRACKED from this module so repo metadata stays defined in one place.
"""

import csv
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

TRACKED = [
    {
        "repo":  "ROCm/aiter",
        "desc":  "AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)",
        "slug":  "ROCm_aiter",
        "badge": "https://img.shields.io/github/last-commit/ROCm/aiter",
        "link":  "https://github.com/ROCm/aiter",
    },
    {
        "repo":  "ROCm/mori",
        "desc":  "Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL",
        "slug":  "ROCm_mori",
        "badge": "https://img.shields.io/github/last-commit/ROCm/mori",
        "link":  "https://github.com/ROCm/mori",
    },
    {
        "repo":  "sgl-project/sglang",
        "desc":  "SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm",
        "slug":  "sgl-project_sglang",
        "badge": "https://img.shields.io/github/last-commit/sgl-project/sglang",
        "link":  "https://github.com/sgl-project/sglang",
    },
    {
        "repo":  "vllm-project/vllm",
        "desc":  "vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm",
        "slug":  "vllm-project_vllm",
        "badge": "https://img.shields.io/github/last-commit/vllm-project/vllm",
        "link":  "https://github.com/vllm-project/vllm",
    },
    {
        "repo":  "NVIDIA/TensorRT-LLM",
        "desc":  "TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation",
        "slug":  "NVIDIA_TensorRT-LLM",
        "badge": "https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM",
        "link":  "https://github.com/NVIDIA/TensorRT-LLM",
    },
    {
        "repo":  "NVIDIA/TensorRT",
        "desc":  "TensorRT OSS — Plugins, ONNX parser, Python API, Quantization",
        "slug":  "NVIDIA_TensorRT",
        "badge": "https://img.shields.io/github/last-commit/NVIDIA/TensorRT",
        "link":  "https://github.com/NVIDIA/TensorRT",
    },
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def latest_report(slug: str) -> tuple[str, Path | None]:
    """Return (period_str, Path) of the most recent report file, or ('—', None)."""
    report_dir = REPO_ROOT / "reports" / slug
    if not report_dir.exists():
        return "—", None
    reports = sorted(
        [r for r in report_dir.glob(f"{slug}_*.md") if r.name != "README.md"],
        reverse=True,
    )
    if not reports:
        return "—", None
    latest = reports[0]
    period = latest.stem.replace(f"{slug}_", "").replace("_to_", " → ")
    return period, latest


# ---------------------------------------------------------------------------
# Build README.md  (plain, shown on GitHub repo homepage)
# ---------------------------------------------------------------------------

def latest_feature_count(slug: str) -> tuple[int, int]:
    """Return (new features, total commits) from the most recent report CSV."""
    csvs = sorted((REPO_ROOT / "reports" / slug).glob(f"{slug}_*.csv"), reverse=True)
    if not csvs:
        return 0, 0
    with csvs[0].open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    return sum(1 for r in rows if (r.get("new_feature") or "").strip() == "yes"), len(rows)


def build_readme() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# oss-pulse",
        "",
        "> Weekly digest of new features landing across the LLM inference stacks.",
        "",
        "### → **[Open the dashboard](https://lcskrishna.github.io/oss-pulse)**",
        "",
        "Browse features week by week, filter to ROCm/AMD only, or search across all six repos.",
        "",
        "---",
        "",
        "## Tracked Repositories",
        "",
        "| Repository | Description | Last Report | Features | Commit Activity |",
        "|------------|-------------|:-----------:|:--------:|:---------------:|",
    ]
    for t in TRACKED:
        period, path = latest_report(t["slug"])
        rel = f"reports/{t['slug']}/{path.name}" if path else ""
        report_cell = f"[{period}]({rel})" if rel else "—"
        badge = f"![last-commit]({t['badge']}?style=flat-square)"
        feats, commits = latest_feature_count(t["slug"])
        feat_cell = f"**{feats}** / {commits}" if commits else "—"
        lines.append(
            f"| [{t['repo']}]({t['link']}) | {t['desc']} | {report_cell} "
            f"| {feat_cell} | {badge} |"
        )
    lines += [
        "",
        "---",
        "",
        "## How to Add a Repository",
        "",
        "1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`",
        "2. Add a run step in `.github/workflows/weekly-tracker.yml`",
        "3. Push — the next Monday run picks it up automatically",
        "",
        "## Run Manually",
        "",
        "```bash",
        "python scripts/track_repo_changes.py --repo ROCm/aiter   # fetch one repo's week",
        "python scripts/update_dashboard.py                       # regenerate this README",
        "python scripts/build_dashboard.py                        # regenerate index.html",
        "```",
        "",
        "---",
        f"_Last updated: {now}_",
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    readme = REPO_ROOT / "README.md"
    readme.write_text(build_readme(), encoding="utf-8")
    print(f"README    → {readme}")
