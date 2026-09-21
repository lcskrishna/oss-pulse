---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-09-21 15:12 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-09-14 → 2026-09-21](reports/ROCm_aiter/ROCm_aiter_2026-09-14_to_2026-09-21.md) — **127 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 43 |
| GEMM | 27 |
| Quantization | 12 |
| Triton Kernels | 9 |
| MHA / Attention | 9 |
| MLA | 9 |
| Other | 6 |
| RMSNorm / LayerNorm | 5 |
| CI / Build | 4 |
| Paged Attention | 3 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-09-14 → 2026-09-21](reports/ROCm_mori/ROCm_mori_2026-09-14_to_2026-09-21.md) — **23 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 12 |
| MORI-UMBP (Memory Pool) | 3 |
| SDMA / Shared Memory | 2 |
| MORI-CCL (Collectives) | 2 |
| CI / Build | 1 |
| RDMA / Transport | 1 |
| Env / Config | 1 |
| Memory / VA Management | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-09-14 → 2026-09-21](reports/sgl-project_sglang/sgl-project_sglang_2026-09-14_to_2026-09-21.md) — **406 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 85 |
| Prefill / Decode Disaggregation | 59 |
| Other | 50 |
| MoE / Expert Parallel | 37 |
| Multimodal | 32 |
| KV Cache / Memory | 27 |
| Scheduler / Batching | 17 |
| Quantization | 15 |
| CI / Build | 13 |
| Triton / Kernels | 13 |
| Tensor / Data Parallel | 11 |
| Docs / Examples | 10 |
| Models | 10 |
| Speculative Decoding | 7 |
| ROCm / AMD | 6 |
| Structured Output | 6 |
| Serving / API | 5 |
| LoRA | 3 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-09-14 → 2026-09-21](reports/vllm-project_vllm/vllm-project_vllm_2026-09-14_to_2026-09-21.md) — **446 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 83 |
| MoE / Expert Parallel | 48 |
| Attention | 43 |
| Other | 40 |
| Multimodal | 34 |
| Scheduler / Engine | 29 |
| CI / Build | 28 |
| Serving / API | 23 |
| Disaggregation / PD | 23 |
| Models | 22 |
| KV Cache / Offload | 16 |
| Speculative Decoding | 15 |
| Quantization | 13 |
| Perf / Benchmark | 9 |
| Docs | 8 |
| LoRA | 8 |
| Compilation / CUDA Graph | 4 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-09-14 → 2026-09-21](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-09-14_to_2026-09-21.md) — **260 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 56 |
| Attention | 54 |
| MoE | 34 |
| Executor / Runtime | 27 |
| Torch Path (_torch) | 19 |
| Disaggregation / KV | 19 |
| Speculative Decoding | 11 |
| Other | 10 |
| Quantization | 9 |
| ROCm / AMD | 8 |
| Models | 5 |
| Docs / Examples | 4 |
| AutoDeploy | 2 |
| Compilation / Graph | 1 |
| Perf | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

