---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-06-15 14:36 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-06-08 → 2026-06-15](reports/ROCm_aiter/ROCm_aiter_2026-06-08_to_2026-06-15.md) — **77 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| GEMM | 17 |
| MoE | 13 |
| Other | 10 |
| MHA / Attention | 8 |
| CI / Build | 7 |
| Quantization | 6 |
| Paged Attention | 6 |
| Triton Kernels | 5 |
| MLA | 4 |
| RoPE / Embedding | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-06-08 → 2026-06-15](reports/ROCm_mori/ROCm_mori_2026-06-08_to_2026-06-15.md) — **15 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-UMBP (Memory Pool) | 6 |
| MORI-IO (KVCache / P2P) | 4 |
| MORI-EP (Expert Parallel) | 3 |
| Bootstrap / Topology | 2 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-06-08 → 2026-06-15](reports/sgl-project_sglang/sgl-project_sglang_2026-06-08_to_2026-06-15.md) — **373 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 78 |
| Multimodal | 40 |
| KV Cache / Memory | 32 |
| Prefill / Decode Disaggregation | 29 |
| Docs / Examples | 26 |
| MoE / Expert Parallel | 26 |
| Speculative Decoding | 23 |
| Other | 22 |
| Tensor / Data Parallel | 15 |
| Triton / Kernels | 14 |
| ROCm / AMD | 14 |
| CI / Build | 14 |
| Models | 12 |
| Quantization | 12 |
| Scheduler / Batching | 10 |
| Structured Output | 3 |
| LoRA | 2 |
| Serving / API | 1 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-06-08 → 2026-06-15](reports/vllm-project_vllm/vllm-project_vllm_2026-06-08_to_2026-06-15.md) — **281 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 34 |
| Other | 33 |
| Multimodal | 29 |
| MoE / Expert Parallel | 28 |
| Serving / API | 26 |
| Attention | 25 |
| Models | 21 |
| Quantization | 16 |
| CI / Build | 14 |
| Disaggregation / PD | 14 |
| Scheduler / Engine | 13 |
| Perf / Benchmark | 6 |
| Docs | 6 |
| Speculative Decoding | 5 |
| KV Cache / Offload | 5 |
| LoRA | 3 |
| Compilation / CUDA Graph | 3 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-06-08 → 2026-06-15](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-06-08_to_2026-06-15.md) — **171 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 38 |
| MoE | 27 |
| Attention | 25 |
| Quantization | 14 |
| Models | 12 |
| Executor / Runtime | 12 |
| Disaggregation / KV | 11 |
| Torch Path (_torch) | 8 |
| Other | 8 |
| Docs / Examples | 7 |
| AutoDeploy | 7 |
| Speculative Decoding | 2 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

