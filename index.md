---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-09-28 16:48 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-09-21 → 2026-09-28](reports/ROCm_aiter/ROCm_aiter_2026-09-21_to_2026-09-28.md) — **110 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 25 |
| GEMM | 22 |
| Quantization | 13 |
| MLA | 11 |
| Triton Kernels | 11 |
| MHA / Attention | 7 |
| Other | 7 |
| CI / Build | 5 |
| Paged Attention | 5 |
| RMSNorm / LayerNorm | 3 |
| OPUS / ASM | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-09-21 → 2026-09-28](reports/ROCm_mori/ROCm_mori_2026-09-21_to_2026-09-28.md) — **14 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 7 |
| SDMA / Shared Memory | 2 |
| MORI-UMBP (Memory Pool) | 1 |
| Other | 1 |
| CI / Build | 1 |
| RDMA / Transport | 1 |
| MORI-CCL (Collectives) | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-09-21 → 2026-09-28](reports/sgl-project_sglang/sgl-project_sglang_2026-09-21_to_2026-09-28.md) — **459 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 105 |
| MoE / Expert Parallel | 71 |
| Multimodal | 51 |
| Prefill / Decode Disaggregation | 48 |
| Other | 37 |
| KV Cache / Memory | 29 |
| Quantization | 16 |
| Scheduler / Batching | 14 |
| Triton / Kernels | 13 |
| ROCm / AMD | 13 |
| Models | 11 |
| CI / Build | 11 |
| Docs / Examples | 10 |
| Speculative Decoding | 9 |
| Tensor / Data Parallel | 9 |
| Serving / API | 5 |
| Structured Output | 5 |
| LoRA | 2 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-09-21 → 2026-09-28](reports/vllm-project_vllm/vllm-project_vllm_2026-09-21_to_2026-09-28.md) — **409 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 97 |
| Other | 47 |
| Attention | 42 |
| Multimodal | 37 |
| MoE / Expert Parallel | 28 |
| Serving / API | 24 |
| Models | 22 |
| CI / Build | 22 |
| Scheduler / Engine | 20 |
| Quantization | 18 |
| Speculative Decoding | 15 |
| Disaggregation / PD | 13 |
| KV Cache / Offload | 8 |
| LoRA | 6 |
| Perf / Benchmark | 4 |
| Compilation / CUDA Graph | 4 |
| Docs | 2 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-09-21 → 2026-09-28](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-09-21_to_2026-09-28.md) — **144 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 26 |
| Attention | 21 |
| MoE | 20 |
| Disaggregation / KV | 14 |
| Executor / Runtime | 13 |
| Other | 9 |
| Torch Path (_torch) | 9 |
| Quantization | 8 |
| Speculative Decoding | 7 |
| Models | 7 |
| Docs / Examples | 4 |
| ROCm / AMD | 2 |
| AutoDeploy | 2 |
| LoRA | 1 |
| Compilation / Graph | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

**Latest report:** [2026-09-21 → 2026-09-28](reports/NVIDIA_TensorRT/NVIDIA_TensorRT_2026-09-21_to_2026-09-28.md) — **1 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT/)

| Component | Commits |
|-----------|:-------:|
| Release / Docs | 1 |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

