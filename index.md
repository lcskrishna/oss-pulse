---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-08-17 08:57 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-08-10 → 2026-08-17](reports/ROCm_aiter/ROCm_aiter_2026-08-10_to_2026-08-17.md) — **93 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 27 |
| Triton Kernels | 15 |
| MLA | 12 |
| GEMM | 12 |
| CI / Build | 5 |
| Quantization | 5 |
| MHA / Attention | 4 |
| Paged Attention | 4 |
| Other | 3 |
| RoPE / Embedding | 2 |
| OPUS / ASM | 2 |
| Docs | 1 |
| CK / CK_TILE | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-08-10 → 2026-08-17](reports/ROCm_mori/ROCm_mori_2026-08-10_to_2026-08-17.md) — **17 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 11 |
| MORI-IO (KVCache / P2P) | 3 |
| RDMA / Transport | 1 |
| CI / Build | 1 |
| Other | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-08-10 → 2026-08-17](reports/sgl-project_sglang/sgl-project_sglang_2026-08-10_to_2026-08-17.md) — **394 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Multimodal | 81 |
| Attention / FlashInfer | 76 |
| MoE / Expert Parallel | 41 |
| KV Cache / Memory | 29 |
| Prefill / Decode Disaggregation | 27 |
| Other | 27 |
| Quantization | 20 |
| Docs / Examples | 18 |
| Models | 13 |
| Triton / Kernels | 13 |
| Tensor / Data Parallel | 10 |
| Speculative Decoding | 9 |
| CI / Build | 9 |
| ROCm / AMD | 8 |
| Scheduler / Batching | 7 |
| Serving / API | 4 |
| Structured Output | 2 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-08-10 → 2026-08-17](reports/vllm-project_vllm/vllm-project_vllm_2026-08-10_to_2026-08-17.md) — **312 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 56 |
| Other | 40 |
| Attention | 40 |
| MoE / Expert Parallel | 29 |
| CI / Build | 25 |
| Multimodal | 22 |
| Models | 17 |
| Serving / API | 16 |
| Scheduler / Engine | 15 |
| Quantization | 12 |
| Speculative Decoding | 11 |
| KV Cache / Offload | 8 |
| Disaggregation / PD | 7 |
| Perf / Benchmark | 5 |
| Docs | 4 |
| LoRA | 3 |
| Compilation / CUDA Graph | 2 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-08-10 → 2026-08-17](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-08-10_to_2026-08-17.md) — **226 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 72 |
| Executor / Runtime | 27 |
| Attention | 24 |
| MoE | 20 |
| Quantization | 17 |
| Disaggregation / KV | 15 |
| Speculative Decoding | 14 |
| Models | 11 |
| Torch Path (_torch) | 10 |
| Other | 9 |
| AutoDeploy | 2 |
| Docs / Examples | 2 |
| Perf | 1 |
| LoRA | 1 |
| ROCm / AMD | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

