---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-07-06 12:15 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-06-29 → 2026-07-06](reports/ROCm_aiter/ROCm_aiter_2026-06-29_to_2026-07-06.md) — **73 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 16 |
| GEMM | 14 |
| Quantization | 10 |
| MHA / Attention | 7 |
| CI / Build | 6 |
| Other | 6 |
| MLA | 5 |
| Paged Attention | 5 |
| Triton Kernels | 3 |
| OPUS / ASM | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-06-29 → 2026-07-06](reports/ROCm_mori/ROCm_mori_2026-06-29_to_2026-07-06.md) — **14 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-IO (KVCache / P2P) | 4 |
| RDMA / Transport | 4 |
| MORI-UMBP (Memory Pool) | 2 |
| CI / Build | 1 |
| MORI-CCL (Collectives) | 1 |
| SDMA / Shared Memory | 1 |
| MORI-EP (Expert Parallel) | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-06-29 → 2026-07-06](reports/sgl-project_sglang/sgl-project_sglang_2026-06-29_to_2026-07-06.md) — **267 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 54 |
| Multimodal | 34 |
| Other | 27 |
| MoE / Expert Parallel | 25 |
| KV Cache / Memory | 17 |
| Quantization | 14 |
| Prefill / Decode Disaggregation | 14 |
| Tensor / Data Parallel | 12 |
| Docs / Examples | 11 |
| Triton / Kernels | 11 |
| Models | 11 |
| ROCm / AMD | 10 |
| Scheduler / Batching | 9 |
| Speculative Decoding | 8 |
| CI / Build | 7 |
| Structured Output | 1 |
| LoRA | 1 |
| Serving / API | 1 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-06-29 → 2026-07-06](reports/vllm-project_vllm/vllm-project_vllm_2026-06-29_to_2026-07-06.md) — **273 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 45 |
| Other | 38 |
| Attention | 34 |
| MoE / Expert Parallel | 25 |
| Models | 22 |
| Serving / API | 20 |
| Multimodal | 19 |
| CI / Build | 17 |
| Scheduler / Engine | 14 |
| Quantization | 11 |
| LoRA | 10 |
| Speculative Decoding | 7 |
| Disaggregation / PD | 6 |
| KV Cache / Offload | 3 |
| Docs | 1 |
| Compilation / CUDA Graph | 1 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-06-29 → 2026-07-06](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-06-29_to_2026-07-06.md) — **183 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 57 |
| MoE | 25 |
| Attention | 21 |
| Executor / Runtime | 19 |
| Quantization | 11 |
| Models | 11 |
| Torch Path (_torch) | 10 |
| Disaggregation / KV | 8 |
| Other | 7 |
| Speculative Decoding | 6 |
| Docs / Examples | 3 |
| AutoDeploy | 3 |
| Perf | 1 |
| LoRA | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

