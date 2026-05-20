---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-05-20 04:15 UTC**_

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

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-05-13 → 2026-05-20](reports/sgl-project_sglang/sgl-project_sglang_2026-05-13_to_2026-05-20.md) — **359 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Scheduler / Batching | 57 |
| Prefill / Decode Disaggregation | 48 |
| Attention / FlashInfer | 42 |
| MoE / Expert Parallel | 41 |
| Multimodal | 27 |
| Other | 21 |
| KV Cache / Memory | 21 |
| CI / Build | 18 |
| Quantization | 15 |
| Triton / Kernels | 12 |
| Tensor / Data Parallel | 12 |
| Speculative Decoding | 11 |
| Docs / Examples | 11 |
| Models | 10 |
| ROCm / AMD | 8 |
| Serving / API | 3 |
| LoRA | 1 |
| Structured Output | 1 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-05-13 → 2026-05-20](reports/vllm-project_vllm/vllm-project_vllm_2026-05-13_to_2026-05-20.md) — **225 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 34 |
| MoE / Expert Parallel | 32 |
| Attention | 31 |
| Other | 28 |
| Disaggregation / PD | 16 |
| Multimodal | 16 |
| Models | 11 |
| CI / Build | 11 |
| Quantization | 10 |
| Serving / API | 8 |
| Speculative Decoding | 8 |
| Scheduler / Engine | 6 |
| KV Cache / Offload | 4 |
| Perf / Benchmark | 4 |
| Compilation / CUDA Graph | 3 |
| Docs | 2 |
| LoRA | 1 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-05-13 → 2026-05-20](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-05-13_to_2026-05-20.md) — **161 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 43 |
| Executor / Runtime | 22 |
| MoE | 22 |
| Attention | 17 |
| Quantization | 12 |
| Torch Path (_torch) | 9 |
| Disaggregation / KV | 9 |
| Other | 7 |
| AutoDeploy | 7 |
| Models | 4 |
| Docs / Examples | 4 |
| Speculative Decoding | 3 |
| Perf | 2 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

