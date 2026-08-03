---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-08-03 11:41 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-07-27 → 2026-08-03](reports/ROCm_aiter/ROCm_aiter_2026-07-27_to_2026-08-03.md) — **50 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 20 |
| Quantization | 7 |
| MLA | 6 |
| Other | 5 |
| CI / Build | 4 |
| GEMM | 4 |
| Paged Attention | 2 |
| RMSNorm / LayerNorm | 1 |
| Docs | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-07-27 → 2026-08-03](reports/ROCm_mori/ROCm_mori_2026-07-27_to_2026-08-03.md) — **8 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| RDMA / Transport | 3 |
| MORI-EP (Expert Parallel) | 3 |
| CI / Build | 1 |
| MORI-IO (KVCache / P2P) | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-07-27 → 2026-08-03](reports/sgl-project_sglang/sgl-project_sglang_2026-07-27_to_2026-08-03.md) — **297 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 62 |
| Other | 33 |
| MoE / Expert Parallel | 33 |
| Multimodal | 32 |
| Prefill / Decode Disaggregation | 26 |
| KV Cache / Memory | 19 |
| Docs / Examples | 18 |
| Quantization | 13 |
| Speculative Decoding | 10 |
| ROCm / AMD | 9 |
| Scheduler / Batching | 9 |
| Models | 8 |
| Triton / Kernels | 7 |
| Tensor / Data Parallel | 4 |
| Structured Output | 4 |
| CI / Build | 4 |
| Serving / API | 4 |
| LoRA | 2 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-07-27 → 2026-08-03](reports/vllm-project_vllm/vllm-project_vllm_2026-07-27_to_2026-08-03.md) — **329 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 73 |
| Other | 32 |
| MoE / Expert Parallel | 32 |
| Attention | 30 |
| CI / Build | 25 |
| Multimodal | 23 |
| Disaggregation / PD | 21 |
| Quantization | 20 |
| Models | 16 |
| Serving / API | 14 |
| Scheduler / Engine | 13 |
| KV Cache / Offload | 8 |
| Perf / Benchmark | 6 |
| Speculative Decoding | 6 |
| Docs | 6 |
| Compilation / CUDA Graph | 2 |
| LoRA | 2 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-07-27 → 2026-08-03](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-07-27_to_2026-08-03.md) — **192 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 50 |
| Attention | 24 |
| Executor / Runtime | 24 |
| MoE | 22 |
| Torch Path (_torch) | 17 |
| Other | 12 |
| Speculative Decoding | 12 |
| Disaggregation / KV | 11 |
| Quantization | 10 |
| Models | 7 |
| Docs / Examples | 1 |
| ROCm / AMD | 1 |
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

