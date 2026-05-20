# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.
> View the live site: **[lcskrishna.github.io/oss-pulse](https://lcskrishna.github.io/oss-pulse)**

---

## Tracked Repositories

| Repository | Description | Last Report | Commit Activity |
|------------|-------------|:-----------:|:---------------:|
| [ROCm/aiter](https://github.com/ROCm/aiter) | AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention) | [2026-05-13 → 2026-05-20](reports/ROCm_aiter/ROCm_aiter_2026-05-13_to_2026-05-20.md) | ![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square) |
| [ROCm/mori](https://github.com/ROCm/mori) | Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL | [2026-05-13 → 2026-05-20](reports/ROCm_mori/ROCm_mori_2026-05-13_to_2026-05-20.md) | ![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square) |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — the next Monday run picks it up automatically

## Run Manually

```bash
python scripts/track_repo_changes.py --repo ROCm/aiter
python scripts/track_repo_changes.py --repo ROCm/mori
python scripts/update_dashboard.py
```

---
_Last updated: 2026-05-20 02:29 UTC_
