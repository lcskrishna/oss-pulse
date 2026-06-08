---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-06-08 12:48 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-06-01 → 2026-06-08](reports/ROCm_aiter/ROCm_aiter_2026-06-01_to_2026-06-08.md) — **79 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 19 |
| Triton Kernels | 10 |
| GEMM | 9 |
| Other | 8 |
| MLA | 7 |
| MHA / Attention | 7 |
| CI / Build | 6 |
| Quantization | 6 |
| Paged Attention | 3 |
| OPUS / ASM | 2 |
| RMSNorm / LayerNorm | 2 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-06-01 → 2026-06-08](reports/ROCm_mori/ROCm_mori_2026-06-01_to_2026-06-08.md) — **14 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 4 |
| RDMA / Transport | 3 |
| MORI-UMBP (Memory Pool) | 2 |
| MORI-IO (KVCache / P2P) | 2 |
| CI / Build | 2 |
| JIT / IR / FlyDSL | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-06-01 → 2026-06-08](reports/sgl-project_sglang/sgl-project_sglang_2026-06-01_to_2026-06-08.md) — **355 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 61 |
| Multimodal | 56 |
| KV Cache / Memory | 42 |
| MoE / Expert Parallel | 30 |
| Prefill / Decode Disaggregation | 29 |
| Scheduler / Batching | 23 |
| Speculative Decoding | 17 |
| Models | 16 |
| Other | 15 |
| CI / Build | 13 |
| Tensor / Data Parallel | 10 |
| Triton / Kernels | 10 |
| Docs / Examples | 10 |
| ROCm / AMD | 9 |
| Quantization | 9 |
| LoRA | 2 |
| Serving / API | 2 |
| Structured Output | 1 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-06-01 → 2026-06-08](reports/vllm-project_vllm/vllm-project_vllm_2026-06-01_to_2026-06-08.md) — **248 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 38 |
| Other | 36 |
| MoE / Expert Parallel | 33 |
| Multimodal | 21 |
| Models | 17 |
| Disaggregation / PD | 14 |
| Attention | 14 |
| Scheduler / Engine | 12 |
| Quantization | 12 |
| KV Cache / Offload | 11 |
| CI / Build | 10 |
| Serving / API | 10 |
| Speculative Decoding | 5 |
| Perf / Benchmark | 4 |
| Compilation / CUDA Graph | 4 |
| LoRA | 4 |
| Docs | 3 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-06-01 → 2026-06-08](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-06-01_to_2026-06-08.md) — **155 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 37 |
| Executor / Runtime | 19 |
| MoE | 19 |
| Attention | 18 |
| Other | 11 |
| Quantization | 10 |
| Models | 9 |
| Disaggregation / KV | 8 |
| Torch Path (_torch) | 8 |
| Docs / Examples | 6 |
| AutoDeploy | 5 |
| Speculative Decoding | 3 |
| Perf | 1 |
| LoRA | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

**Latest report:** [2026-06-01 → 2026-06-08](reports/NVIDIA_TensorRT/NVIDIA_TensorRT_2026-06-01_to_2026-06-08.md) — **2 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT/)

| Component | Commits |
|-----------|:-------:|
| Samples / Demo | 1 |
| Release / Docs | 1 |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

