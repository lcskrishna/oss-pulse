---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-07-20 11:12 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-07-13 → 2026-07-20](reports/ROCm_aiter/ROCm_aiter_2026-07-13_to_2026-07-20.md) — **55 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 14 |
| MLA | 12 |
| Quantization | 8 |
| CI / Build | 4 |
| Other | 4 |
| GEMM | 4 |
| Triton Kernels | 3 |
| MHA / Attention | 3 |
| Paged Attention | 3 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-07-13 → 2026-07-20](reports/ROCm_mori/ROCm_mori_2026-07-13_to_2026-07-20.md) — **23 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 9 |
| MORI-IO (KVCache / P2P) | 5 |
| Env / Config | 2 |
| MORI-UMBP (Memory Pool) | 2 |
| CI / Build | 2 |
| JIT / IR / FlyDSL | 1 |
| RDMA / Transport | 1 |
| Other | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-07-13 → 2026-07-20](reports/sgl-project_sglang/sgl-project_sglang_2026-07-13_to_2026-07-20.md) — **344 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 72 |
| MoE / Expert Parallel | 46 |
| Prefill / Decode Disaggregation | 29 |
| Multimodal | 27 |
| KV Cache / Memory | 20 |
| Scheduler / Batching | 19 |
| Speculative Decoding | 19 |
| Triton / Kernels | 18 |
| Other | 17 |
| Quantization | 17 |
| ROCm / AMD | 15 |
| CI / Build | 12 |
| Tensor / Data Parallel | 12 |
| Models | 8 |
| Docs / Examples | 6 |
| LoRA | 4 |
| Serving / API | 2 |
| Structured Output | 1 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-07-13 → 2026-07-20](reports/vllm-project_vllm/vllm-project_vllm_2026-07-13_to_2026-07-20.md) — **242 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 47 |
| Attention | 28 |
| MoE / Expert Parallel | 26 |
| Other | 22 |
| Disaggregation / PD | 15 |
| Serving / API | 14 |
| Quantization | 12 |
| Multimodal | 11 |
| Scheduler / Engine | 11 |
| KV Cache / Offload | 10 |
| Models | 10 |
| CI / Build | 9 |
| Speculative Decoding | 9 |
| Docs | 8 |
| Compilation / CUDA Graph | 4 |
| LoRA | 4 |
| Perf / Benchmark | 2 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-07-13 → 2026-07-20](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-07-13_to_2026-07-20.md) — **208 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 67 |
| Attention | 26 |
| Executor / Runtime | 24 |
| Disaggregation / KV | 19 |
| MoE | 15 |
| Other | 12 |
| Models | 11 |
| Quantization | 8 |
| Torch Path (_torch) | 7 |
| AutoDeploy | 7 |
| Speculative Decoding | 6 |
| Perf | 3 |
| ROCm / AMD | 3 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

