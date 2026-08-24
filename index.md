---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-08-24 09:01 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-08-17 → 2026-08-24](reports/ROCm_aiter/ROCm_aiter_2026-08-17_to_2026-08-24.md) — **79 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 28 |
| GEMM | 11 |
| Triton Kernels | 8 |
| CI / Build | 7 |
| MLA | 6 |
| MHA / Attention | 5 |
| Paged Attention | 4 |
| Quantization | 3 |
| Other | 3 |
| Sampling | 2 |
| CK / CK_TILE | 1 |
| RoPE / Embedding | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-08-17 → 2026-08-24](reports/ROCm_mori/ROCm_mori_2026-08-17_to_2026-08-24.md) — **8 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 4 |
| Env / Config | 1 |
| MORI-IO (KVCache / P2P) | 1 |
| CI / Build | 1 |
| MORI-CCL (Collectives) | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-08-17 → 2026-08-24](reports/sgl-project_sglang/sgl-project_sglang_2026-08-17_to_2026-08-24.md) — **417 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Multimodal | 96 |
| Attention / FlashInfer | 64 |
| Quantization | 44 |
| Prefill / Decode Disaggregation | 44 |
| MoE / Expert Parallel | 34 |
| KV Cache / Memory | 28 |
| ROCm / AMD | 18 |
| Other | 17 |
| Tensor / Data Parallel | 16 |
| Scheduler / Batching | 11 |
| Triton / Kernels | 8 |
| Models | 8 |
| Docs / Examples | 7 |
| Serving / API | 7 |
| Speculative Decoding | 6 |
| CI / Build | 5 |
| Structured Output | 4 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-08-17 → 2026-08-24](reports/vllm-project_vllm/vllm-project_vllm_2026-08-17_to_2026-08-24.md) — **308 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 61 |
| Attention | 41 |
| MoE / Expert Parallel | 39 |
| Multimodal | 27 |
| Other | 24 |
| CI / Build | 20 |
| Models | 16 |
| Serving / API | 15 |
| Scheduler / Engine | 13 |
| Disaggregation / PD | 10 |
| Speculative Decoding | 9 |
| LoRA | 8 |
| Perf / Benchmark | 7 |
| Quantization | 6 |
| Docs | 5 |
| Compilation / CUDA Graph | 4 |
| KV Cache / Offload | 2 |
| Distributed | 1 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-08-17 → 2026-08-24](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-08-17_to_2026-08-24.md) — **232 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 68 |
| Executor / Runtime | 27 |
| MoE | 24 |
| Attention | 23 |
| Disaggregation / KV | 19 |
| Quantization | 17 |
| Torch Path (_torch) | 14 |
| Models | 10 |
| Speculative Decoding | 7 |
| Other | 6 |
| Docs / Examples | 6 |
| LoRA | 5 |
| Perf | 2 |
| ROCm / AMD | 2 |
| AutoDeploy | 1 |
| Compilation / Graph | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

**Latest report:** [2026-08-17 → 2026-08-24](reports/NVIDIA_TensorRT/NVIDIA_TensorRT_2026-08-17_to_2026-08-24.md) — **1 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT/)

| Component | Commits |
|-----------|:-------:|
| Samples / Demo | 1 |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

