# oss-pulse

> Weekly digest of changes across tracked OSS repositories.

---

## Tracked Repositories

| Repository | Description | Last Report | Commit Activity |
|------------|-------------|:-----------:|:---------------:|
| [ROCm/aiter](https://github.com/ROCm/aiter) | AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention) | [2026-05-13 → 2026-05-20](reports/ROCm_aiter/ROCm_aiter_2026-05-13_to_2026-05-20.md) | ![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square) |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step for it in `.github/workflows/weekly-tracker.yml`
3. Push — the next Monday run will pick it up automatically

## Run Manually

```bash
# Track the last 7 days (default)
python scripts/track_repo_changes.py --repo ROCm/aiter

# Custom date range
python scripts/track_repo_changes.py --repo ROCm/aiter --since 2026-05-01 --until 2026-05-20

# Faster run (skip per-commit file fetching)
python scripts/track_repo_changes.py --repo ROCm/aiter --no-files
```

---

_Dashboard last updated: 2026-05-20 02:12 UTC_
