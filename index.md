---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-07-13 11:27 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-07-06 → 2026-07-13](reports/ROCm_aiter/ROCm_aiter_2026-07-06_to_2026-07-13.md) — **83 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 20 |
| GEMM | 15 |
| Quantization | 10 |
| MLA | 9 |
| Other | 9 |
| Triton Kernels | 6 |
| Paged Attention | 5 |
| CI / Build | 5 |
| MHA / Attention | 3 |
| RMSNorm / LayerNorm | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-07-06 → 2026-07-13](reports/ROCm_mori/ROCm_mori_2026-07-06_to_2026-07-13.md) — **10 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 2 |
| CI / Build | 2 |
| RDMA / Transport | 2 |
| MORI-IO (KVCache / P2P) | 2 |
| MORI-CCL (Collectives) | 1 |
| MORI-UMBP (Memory Pool) | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-07-06 → 2026-07-13](reports/sgl-project_sglang/sgl-project_sglang_2026-07-06_to_2026-07-13.md) — **274 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 62 |
| MoE / Expert Parallel | 33 |
| Multimodal | 28 |
| Prefill / Decode Disaggregation | 26 |
| Other | 21 |
| KV Cache / Memory | 19 |
| Docs / Examples | 18 |
| Triton / Kernels | 16 |
| Quantization | 11 |
| Scheduler / Batching | 11 |
| Tensor / Data Parallel | 9 |
| ROCm / AMD | 6 |
| Speculative Decoding | 4 |
| CI / Build | 4 |
| Serving / API | 3 |
| Models | 2 |
| LoRA | 1 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-07-06 → 2026-07-13](reports/vllm-project_vllm/vllm-project_vllm_2026-07-06_to_2026-07-13.md) — **274 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 44 |
| Other | 36 |
| Attention | 31 |
| MoE / Expert Parallel | 26 |
| Multimodal | 25 |
| Models | 19 |
| CI / Build | 15 |
| Scheduler / Engine | 13 |
| Serving / API | 13 |
| Quantization | 12 |
| Disaggregation / PD | 9 |
| Speculative Decoding | 8 |
| KV Cache / Offload | 7 |
| LoRA | 6 |
| Docs | 5 |
| Compilation / CUDA Graph | 3 |
| Perf / Benchmark | 2 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-07-06 → 2026-07-13](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-07-06_to_2026-07-13.md) — **203 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 57 |
| Executor / Runtime | 28 |
| Attention | 27 |
| MoE | 22 |
| Other | 15 |
| Disaggregation / KV | 13 |
| Quantization | 12 |
| Torch Path (_torch) | 8 |
| Speculative Decoding | 7 |
| AutoDeploy | 5 |
| Models | 4 |
| Perf | 2 |
| ROCm / AMD | 1 |
| Docs / Examples | 1 |
| LoRA | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

**Latest report:** [2026-07-06 → 2026-07-13](reports/NVIDIA_TensorRT/NVIDIA_TensorRT_2026-07-06_to_2026-07-13.md) — **1 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT/)

| Component | Commits |
|-----------|:-------:|
| Samples / Demo | 1 |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

