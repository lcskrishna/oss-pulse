#!/usr/bin/env python3
"""
Regenerate README.md (GitHub repo homepage) and index.md (GitHub Pages homepage)
from all per-repo report files. Run automatically in CI after track_repo_changes.py.
"""

import re
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


def extract_component_table(report_path: Path) -> list[tuple[str, int]]:
    """Parse the Summary by Component table from a report markdown file."""
    if report_path is None:
        return []
    text = report_path.read_text(encoding="utf-8")
    # Find the summary table block
    in_table = False
    rows = []
    for line in text.splitlines():
        if "## Summary by Component" in line:
            in_table = True
            continue
        if in_table:
            if line.startswith("| Component"):
                continue
            if line.startswith("|---"):
                continue
            if line.startswith("| ") and " | " in line:
                parts = [p.strip() for p in line.strip().strip("|").split("|")]
                if len(parts) == 2:
                    try:
                        rows.append((parts[0], int(parts[1])))
                    except ValueError:
                        pass
            elif line.startswith("##") and rows:
                break   # hit the next section
    return rows


def extract_commit_count(report_path: Path) -> int:
    """Read total commit count from report header line."""
    if report_path is None:
        return 0
    for line in report_path.read_text(encoding="utf-8").splitlines():
        m = re.search(r"Total commits:\*\*\s*(\d+)", line)
        if m:
            return int(m.group(1))
    return 0


# ---------------------------------------------------------------------------
# Build README.md  (plain, shown on GitHub repo homepage)
# ---------------------------------------------------------------------------

def build_readme() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# oss-pulse",
        "",
        "> Weekly digest of changes across tracked ROCm OSS repositories.",
        "> View the live site: **[lcskrishna.github.io/oss-pulse](https://lcskrishna.github.io/oss-pulse)**",
        "",
        "---",
        "",
        "## Tracked Repositories",
        "",
        "| Repository | Description | Last Report | Commit Activity |",
        "|------------|-------------|:-----------:|:---------------:|",
    ]
    for t in TRACKED:
        period, path = latest_report(t["slug"])
        rel = f"reports/{t['slug']}/{path.name}" if path else ""
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
        "2. Add a run step in `.github/workflows/weekly-tracker.yml`",
        "3. Push — the next Monday run picks it up automatically",
        "",
        "## Run Manually",
        "",
        "```bash",
        "python scripts/track_repo_changes.py --repo ROCm/aiter",
        "python scripts/track_repo_changes.py --repo ROCm/mori",
        "python scripts/update_dashboard.py",
        "```",
        "",
        "---",
        f"_Last updated: {now}_",
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Build index.md  (rendered by Jekyll → GitHub Pages single-page dashboard)
# ---------------------------------------------------------------------------

def build_index() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "---",
        "layout: default",
        f'title: "oss-pulse — Weekly OSS Digest"',
        "---",
        "",
        "# oss-pulse",
        "",
        "> Weekly digest of changes across tracked ROCm OSS repositories.",
        "",
        f"_Last updated: **{now}**_",
        "",
        "---",
        "",
    ]

    for t in TRACKED:
        period, path = latest_report(t["slug"])
        total = extract_commit_count(path)
        components = extract_component_table(path)

        rel_report = f"reports/{t['slug']}/{path.name}" if path else ""
        rel_index  = f"reports/{t['slug']}/"

        lines += [
            f"## [{t['repo']}]({t['link']})",
            "",
            f"{t['desc']}",
            "",
            f"![last-commit]({t['badge']}?style=flat-square)",
            "",
        ]

        if period != "—" and total:
            lines += [
                f"**Latest report:** [{period}]({rel_report}) — "
                f"**{total} commits** &nbsp;·&nbsp; [all reports]({rel_index})",
                "",
            ]

        if components:
            lines += [
                "| Component | Commits |",
                "|-----------|:-------:|",
            ]
            for comp, count in components:
                lines.append(f"| {comp} | {count} |")
            lines.append("")

        lines += ["---", ""]

    lines += [
        "## How to Add a Repository",
        "",
        "1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`",
        "2. Add a run step in `.github/workflows/weekly-tracker.yml`",
        "3. Push — GitHub Actions picks it up every Monday",
        "",
    ]

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    readme = REPO_ROOT / "README.md"
    readme.write_text(build_readme(), encoding="utf-8")
    print(f"README    → {readme}")

    index = REPO_ROOT / "index.md"
    index.write_text(build_index(), encoding="utf-8")
    print(f"index.md  → {index}")
