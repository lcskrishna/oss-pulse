---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-09-14 15:07 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-09-07 → 2026-09-14](reports/ROCm_aiter/ROCm_aiter_2026-09-07_to_2026-09-14.md) — **103 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 33 |
| GEMM | 21 |
| MHA / Attention | 13 |
| Triton Kernels | 10 |
| Quantization | 8 |
| Other | 8 |
| MLA | 7 |
| CI / Build | 2 |
| RMSNorm / LayerNorm | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-09-07 → 2026-09-14](reports/ROCm_mori/ROCm_mori_2026-09-07_to_2026-09-14.md) — **21 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 10 |
| MORI-UMBP (Memory Pool) | 3 |
| Other | 2 |
| Memory / VA Management | 1 |
| RDMA / Transport | 1 |
| CI / Build | 1 |
| Benchmarks / Tests | 1 |
| Bootstrap / Topology | 1 |
| Env / Config | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-09-07 → 2026-09-14](reports/sgl-project_sglang/sgl-project_sglang_2026-09-07_to_2026-09-14.md) — **379 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 91 |
| Multimodal | 50 |
| KV Cache / Memory | 37 |
| Prefill / Decode Disaggregation | 35 |
| Other | 30 |
| MoE / Expert Parallel | 30 |
| CI / Build | 18 |
| Quantization | 16 |
| Triton / Kernels | 15 |
| Tensor / Data Parallel | 13 |
| Models | 12 |
| ROCm / AMD | 9 |
| Scheduler / Batching | 6 |
| LoRA | 5 |
| Docs / Examples | 4 |
| Serving / API | 3 |
| Speculative Decoding | 3 |
| Structured Output | 2 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-09-07 → 2026-09-14](reports/vllm-project_vllm/vllm-project_vllm_2026-09-07_to_2026-09-14.md) — **389 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 76 |
| Attention | 53 |
| Multimodal | 34 |
| Other | 31 |
| MoE / Expert Parallel | 27 |
| Disaggregation / PD | 26 |
| CI / Build | 25 |
| Serving / API | 22 |
| Quantization | 20 |
| Models | 19 |
| Speculative Decoding | 12 |
| Scheduler / Engine | 12 |
| Docs | 9 |
| LoRA | 7 |
| Perf / Benchmark | 7 |
| KV Cache / Offload | 5 |
| Compilation / CUDA Graph | 4 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-09-07 → 2026-09-14](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-09-07_to_2026-09-14.md) — **227 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 45 |
| Attention | 39 |
| Executor / Runtime | 28 |
| MoE | 26 |
| Other | 19 |
| Disaggregation / KV | 16 |
| Quantization | 12 |
| Docs / Examples | 10 |
| Torch Path (_torch) | 8 |
| ROCm / AMD | 7 |
| Speculative Decoding | 6 |
| Models | 6 |
| LoRA | 3 |
| AutoDeploy | 2 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

