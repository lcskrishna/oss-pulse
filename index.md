---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-06-29 12:45 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-06-22 → 2026-06-29](reports/ROCm_aiter/ROCm_aiter_2026-06-22_to_2026-06-29.md) — **80 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| GEMM | 20 |
| MoE | 16 |
| MLA | 10 |
| Quantization | 9 |
| Other | 8 |
| Triton Kernels | 7 |
| CI / Build | 5 |
| Paged Attention | 2 |
| MHA / Attention | 1 |
| Sampling | 1 |
| RoPE / Embedding | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-06-22 → 2026-06-29](reports/ROCm_mori/ROCm_mori_2026-06-22_to_2026-06-29.md) — **12 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-IO (KVCache / P2P) | 5 |
| MORI-EP (Expert Parallel) | 2 |
| MORI-UMBP (Memory Pool) | 2 |
| Docs | 1 |
| CI / Build | 1 |
| Bootstrap / Topology | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-06-22 → 2026-06-29](reports/sgl-project_sglang/sgl-project_sglang_2026-06-22_to_2026-06-29.md) — **316 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 71 |
| Multimodal | 38 |
| MoE / Expert Parallel | 31 |
| Other | 23 |
| Prefill / Decode Disaggregation | 23 |
| KV Cache / Memory | 21 |
| Quantization | 16 |
| Scheduler / Batching | 15 |
| Triton / Kernels | 14 |
| Models | 13 |
| Speculative Decoding | 13 |
| Docs / Examples | 10 |
| Tensor / Data Parallel | 9 |
| ROCm / AMD | 7 |
| CI / Build | 5 |
| Serving / API | 5 |
| Structured Output | 2 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-06-22 → 2026-06-29](reports/vllm-project_vllm/vllm-project_vllm_2026-06-22_to_2026-06-29.md) — **323 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 74 |
| MoE / Expert Parallel | 51 |
| Other | 33 |
| Attention | 29 |
| Scheduler / Engine | 19 |
| Multimodal | 18 |
| Models | 14 |
| Serving / API | 14 |
| Quantization | 14 |
| CI / Build | 14 |
| KV Cache / Offload | 12 |
| Disaggregation / PD | 9 |
| Speculative Decoding | 8 |
| LoRA | 6 |
| Docs | 5 |
| Compilation / CUDA Graph | 1 |
| Distributed | 1 |
| Perf / Benchmark | 1 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-06-22 → 2026-06-29](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-06-22_to_2026-06-29.md) — **151 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 37 |
| MoE | 18 |
| Attention | 17 |
| Torch Path (_torch) | 15 |
| Executor / Runtime | 14 |
| Models | 14 |
| Quantization | 12 |
| Other | 7 |
| Disaggregation / KV | 7 |
| Speculative Decoding | 4 |
| Docs / Examples | 3 |
| LoRA | 1 |
| Perf | 1 |
| AutoDeploy | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

**Latest report:** [2026-06-22 → 2026-06-29](reports/NVIDIA_TensorRT/NVIDIA_TensorRT_2026-06-22_to_2026-06-29.md) — **1 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT/)

| Component | Commits |
|-----------|:-------:|
| Release / Docs | 1 |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

