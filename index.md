---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-06-22 13:47 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-06-15 → 2026-06-22](reports/ROCm_aiter/ROCm_aiter_2026-06-15_to_2026-06-22.md) — **65 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 11 |
| GEMM | 10 |
| Other | 10 |
| CI / Build | 8 |
| Triton Kernels | 8 |
| MLA | 6 |
| Quantization | 6 |
| MHA / Attention | 2 |
| Sampling | 1 |
| RoPE / Embedding | 1 |
| OPUS / ASM | 1 |
| Docs | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-06-15 → 2026-06-22](reports/ROCm_mori/ROCm_mori_2026-06-15_to_2026-06-22.md) — **12 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-IO (KVCache / P2P) | 3 |
| RDMA / Transport | 3 |
| MORI-UMBP (Memory Pool) | 3 |
| MORI-EP (Expert Parallel) | 2 |
| JIT / IR / FlyDSL | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-06-15 → 2026-06-22](reports/sgl-project_sglang/sgl-project_sglang_2026-06-15_to_2026-06-22.md) — **314 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 59 |
| Other | 36 |
| Multimodal | 34 |
| MoE / Expert Parallel | 28 |
| Prefill / Decode Disaggregation | 20 |
| Docs / Examples | 18 |
| Triton / Kernels | 17 |
| Quantization | 17 |
| Speculative Decoding | 16 |
| ROCm / AMD | 16 |
| Scheduler / Batching | 14 |
| Tensor / Data Parallel | 13 |
| KV Cache / Memory | 13 |
| Models | 5 |
| CI / Build | 4 |
| Serving / API | 3 |
| Structured Output | 1 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-06-15 → 2026-06-22](reports/vllm-project_vllm/vllm-project_vllm_2026-06-15_to_2026-06-22.md) — **270 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 41 |
| Other | 36 |
| Attention | 26 |
| Scheduler / Engine | 26 |
| Models | 20 |
| MoE / Expert Parallel | 19 |
| Quantization | 16 |
| Serving / API | 15 |
| CI / Build | 14 |
| Disaggregation / PD | 14 |
| Multimodal | 13 |
| KV Cache / Offload | 10 |
| LoRA | 7 |
| Compilation / CUDA Graph | 4 |
| Docs | 3 |
| Speculative Decoding | 3 |
| Perf / Benchmark | 3 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-06-15 → 2026-06-22](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-06-15_to_2026-06-22.md) — **80 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 29 |
| Attention | 15 |
| Executor / Runtime | 6 |
| Disaggregation / KV | 6 |
| MoE | 6 |
| Quantization | 5 |
| Models | 4 |
| Other | 3 |
| Torch Path (_torch) | 3 |
| Docs / Examples | 2 |
| AutoDeploy | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

