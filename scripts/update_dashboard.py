#!/usr/bin/env python3
"""
Regenerate the root README.md dashboard from all per-repo index files.
Run automatically after track_repo_changes.py in CI, or manually.
"""

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
    # Add more repos here as you onboard them
]


def latest_report_link(slug: str) -> tuple[str, str]:
    """Return (period_str, relative_md_path) of the most recent report, or ('—', '')."""
    report_dir = REPO_ROOT / "reports" / slug
    if not report_dir.exists():
        return "—", ""
    reports = sorted(report_dir.glob(f"{slug}_*.md"), reverse=True)
    # Exclude index README
    reports = [r for r in reports if r.name != "README.md"]
    if not reports:
        return "—", ""
    latest = reports[0]
    # Extract period from filename: SLUG_YYYY-MM-DD_to_YYYY-MM-DD.md
    parts = latest.stem.replace(f"{slug}_", "")   # YYYY-MM-DD_to_YYYY-MM-DD
    period = parts.replace("_to_", " → ")
    rel = f"reports/{slug}/{latest.name}"
    return period, rel


def build_dashboard() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# oss-pulse",
        "",
        "> Weekly digest of changes across tracked OSS repositories.",
        "",
        "---",
        "",
        "## Tracked Repositories",
        "",
        "| Repository | Description | Last Report | Commit Activity |",
        "|------------|-------------|:-----------:|:---------------:|",
    ]

    for t in TRACKED:
        period, rel = latest_report_link(t["slug"])
        report_cell = f"[{period}]({rel})" if rel else "—"
        badge = f"![last-commit]({t['badge']}?style=flat-square)"
        lines.append(
            f"| [{t['repo']}]({t['link']}) | {t['desc']} | {report_cell} | {badge} |"
        )

    lines += [
        "",
        "---",
        "",
        "## How to Add a Repository",
        "",
        "1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`",
        "2. Add a run step for it in `.github/workflows/weekly-tracker.yml`",
        "3. Push — the next Monday run will pick it up automatically",
        "",
        "## Run Manually",
        "",
        "```bash",
        "# Track the last 7 days (default)",
        "python scripts/track_repo_changes.py --repo ROCm/aiter",
        "",
        "# Custom date range",
        "python scripts/track_repo_changes.py --repo ROCm/aiter --since 2026-05-01 --until 2026-05-20",
        "",
        "# Faster run (skip per-commit file fetching)",
        "python scripts/track_repo_changes.py --repo ROCm/aiter --no-files",
        "```",
        "",
        "---",
        "",
        f"_Dashboard last updated: {now}_",
    ]

    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    readme = REPO_ROOT / "README.md"
    readme.write_text(build_dashboard(), encoding="utf-8")
    print(f"Dashboard written → {readme}")
