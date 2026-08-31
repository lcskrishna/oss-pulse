---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-08-31 16:10 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-08-24 → 2026-08-31](reports/ROCm_aiter/ROCm_aiter_2026-08-24_to_2026-08-31.md) — **106 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| GEMM | 38 |
| MoE | 25 |
| Triton Kernels | 9 |
| MLA | 9 |
| CI / Build | 8 |
| MHA / Attention | 6 |
| Other | 5 |
| Quantization | 5 |
| RMSNorm / LayerNorm | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-08-24 → 2026-08-31](reports/ROCm_mori/ROCm_mori_2026-08-24_to_2026-08-31.md) — **19 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 8 |
| MORI-IO (KVCache / P2P) | 3 |
| MORI-CCL (Collectives) | 2 |
| Bootstrap / Topology | 2 |
| Quantization | 1 |
| CI / Build | 1 |
| Other | 1 |
| Env / Config | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-08-24 → 2026-08-31](reports/sgl-project_sglang/sgl-project_sglang_2026-08-24_to_2026-08-31.md) — **453 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 92 |
| Multimodal | 66 |
| MoE / Expert Parallel | 49 |
| Quantization | 47 |
| Prefill / Decode Disaggregation | 45 |
| KV Cache / Memory | 36 |
| Other | 21 |
| CI / Build | 18 |
| ROCm / AMD | 14 |
| Triton / Kernels | 13 |
| Scheduler / Batching | 13 |
| Models | 10 |
| Docs / Examples | 10 |
| Tensor / Data Parallel | 9 |
| Speculative Decoding | 4 |
| Structured Output | 3 |
| Serving / API | 2 |
| LoRA | 1 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-08-24 → 2026-08-31](reports/vllm-project_vllm/vllm-project_vllm_2026-08-24_to_2026-08-31.md) — **300 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| Attention | 38 |
| Other | 38 |
| ROCm / AMD | 31 |
| Multimodal | 29 |
| MoE / Expert Parallel | 29 |
| Serving / API | 20 |
| CI / Build | 18 |
| Models | 17 |
| Scheduler / Engine | 16 |
| KV Cache / Offload | 12 |
| Disaggregation / PD | 11 |
| Quantization | 9 |
| Perf / Benchmark | 9 |
| Docs | 8 |
| LoRA | 7 |
| Speculative Decoding | 4 |
| Compilation / CUDA Graph | 3 |
| Distributed | 1 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-08-24 → 2026-08-31](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-08-24_to_2026-08-31.md) — **270 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 78 |
| Attention | 35 |
| Executor / Runtime | 31 |
| MoE | 28 |
| Disaggregation / KV | 19 |
| Quantization | 18 |
| Models | 14 |
| Torch Path (_torch) | 13 |
| LoRA | 8 |
| Other | 8 |
| Docs / Examples | 7 |
| Speculative Decoding | 7 |
| AutoDeploy | 4 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

**Latest report:** [2026-08-24 → 2026-08-31](reports/NVIDIA_TensorRT/NVIDIA_TensorRT_2026-08-24_to_2026-08-31.md) — **2 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT/)

| Component | Commits |
|-----------|:-------:|
| Release / Docs | 2 |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

