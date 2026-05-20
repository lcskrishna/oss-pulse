#!/usr/bin/env python3
"""
Delete the oldest report files (both .md and .csv) when a repo's report
directory exceeds MAX_REPORTS entries. README.md index files are never removed.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
MAX_REPORTS = 10


def cleanup_slug(report_dir: Path) -> list[str]:
    """Return list of deleted file names."""
    reports = sorted(
        [p for p in report_dir.glob("*.md") if p.name != "README.md"]
    )
    excess = len(reports) - MAX_REPORTS
    if excess <= 0:
        return []

    deleted = []
    for md in reports[:excess]:
        csv = md.with_suffix(".csv")
        md.unlink()
        deleted.append(md.name)
        if csv.exists():
            csv.unlink()
            deleted.append(csv.name)
    return deleted


def main() -> None:
    reports_root = REPO_ROOT / "reports"
    if not reports_root.exists():
        print("No reports/ directory found — nothing to clean.")
        return

    total_deleted = 0
    for slug_dir in sorted(reports_root.iterdir()):
        if not slug_dir.is_dir():
            continue
        deleted = cleanup_slug(slug_dir)
        if deleted:
            print(f"{slug_dir.name}: removed {len(deleted) // 2} report(s)")
            for f in deleted:
                print(f"  - {f}")
            total_deleted += len(deleted) // 2

    if total_deleted == 0:
        print("All report directories are within the 10-report limit.")
    else:
        print(f"\nTotal: {total_deleted} report(s) removed.")


if __name__ == "__main__":
    sys.exit(main())
