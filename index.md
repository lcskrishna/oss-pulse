---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-05-20 02:29 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-05-13 → 2026-05-20](reports/ROCm_aiter/ROCm_aiter_2026-05-13_to_2026-05-20.md) — **58 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| Other | 18 |
| Triton Kernels | 8 |
| GEMM | 7 |
| MoE | 7 |
| Quantization | 6 |
| CI / Build | 5 |
| MLA | 2 |
| MHA / Attention | 2 |
| OPUS / ASM | 1 |
| CK / CK_TILE | 1 |
| RMSNorm / LayerNorm | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-05-13 → 2026-05-20](reports/ROCm_mori/ROCm_mori_2026-05-13_to_2026-05-20.md) — **10 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| CI / Build | 3 |
| MORI-IO (KVCache / P2P) | 2 |
| Env / Config | 1 |
| MORI-CCL (Collectives) | 1 |
| CLI / Tools | 1 |
| JIT / IR / FlyDSL | 1 |
| MORI-EP (Expert Parallel) | 1 |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

