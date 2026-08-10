---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-08-10 09:46 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-08-03 → 2026-08-10](reports/ROCm_aiter/ROCm_aiter_2026-08-03_to_2026-08-10.md) — **69 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 18 |
| GEMM | 10 |
| MLA | 9 |
| Other | 6 |
| Quantization | 6 |
| Triton Kernels | 5 |
| Paged Attention | 5 |
| MHA / Attention | 4 |
| CI / Build | 3 |
| OPUS / ASM | 1 |
| Sampling | 1 |
| RMSNorm / LayerNorm | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-08-03 → 2026-08-10](reports/ROCm_mori/ROCm_mori_2026-08-03_to_2026-08-10.md) — **18 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 11 |
| RDMA / Transport | 3 |
| Other | 2 |
| MORI-IO (KVCache / P2P) | 1 |
| SDMA / Shared Memory | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-08-03 → 2026-08-10](reports/sgl-project_sglang/sgl-project_sglang_2026-08-03_to_2026-08-10.md) — **399 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 103 |
| Multimodal | 77 |
| Prefill / Decode Disaggregation | 27 |
| MoE / Expert Parallel | 26 |
| Other | 24 |
| Scheduler / Batching | 23 |
| Triton / Kernels | 21 |
| KV Cache / Memory | 19 |
| CI / Build | 17 |
| Quantization | 15 |
| Speculative Decoding | 11 |
| ROCm / AMD | 11 |
| Tensor / Data Parallel | 7 |
| Serving / API | 7 |
| Docs / Examples | 6 |
| Models | 3 |
| Structured Output | 2 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-08-03 → 2026-08-10](reports/vllm-project_vllm/vllm-project_vllm_2026-08-03_to_2026-08-10.md) — **302 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 46 |
| MoE / Expert Parallel | 45 |
| Other | 36 |
| Multimodal | 23 |
| Quantization | 22 |
| CI / Build | 19 |
| Scheduler / Engine | 18 |
| Attention | 18 |
| Disaggregation / PD | 17 |
| Models | 16 |
| KV Cache / Offload | 14 |
| Speculative Decoding | 7 |
| Serving / API | 6 |
| Perf / Benchmark | 5 |
| Compilation / CUDA Graph | 4 |
| Docs | 3 |
| LoRA | 3 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-08-03 → 2026-08-10](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-08-03_to_2026-08-10.md) — **197 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 65 |
| Attention | 24 |
| MoE | 22 |
| Executor / Runtime | 21 |
| Models | 17 |
| Disaggregation / KV | 15 |
| Torch Path (_torch) | 10 |
| Other | 7 |
| Quantization | 6 |
| Speculative Decoding | 3 |
| Docs / Examples | 3 |
| AutoDeploy | 2 |
| Compilation / Graph | 1 |
| LoRA | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

**Latest report:** [2026-08-03 → 2026-08-10](reports/NVIDIA_TensorRT/NVIDIA_TensorRT_2026-08-03_to_2026-08-10.md) — **1 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT/)

| Component | Commits |
|-----------|:-------:|
| Release / Docs | 1 |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

