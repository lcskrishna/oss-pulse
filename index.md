---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-07-27 11:37 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-07-20 → 2026-07-27](reports/ROCm_aiter/ROCm_aiter_2026-07-20_to_2026-07-27.md) — **52 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 17 |
| GEMM | 10 |
| MLA | 5 |
| Other | 5 |
| CI / Build | 4 |
| MHA / Attention | 4 |
| Quantization | 3 |
| Triton Kernels | 2 |
| RMSNorm / LayerNorm | 1 |
| Docs | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-07-20 → 2026-07-27](reports/ROCm_mori/ROCm_mori_2026-07-20_to_2026-07-27.md) — **18 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-UMBP (Memory Pool) | 5 |
| MORI-IO (KVCache / P2P) | 4 |
| MORI-EP (Expert Parallel) | 3 |
| Env / Config | 2 |
| RDMA / Transport | 1 |
| CI / Build | 1 |
| Docs | 1 |
| Bootstrap / Topology | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-07-20 → 2026-07-27](reports/sgl-project_sglang/sgl-project_sglang_2026-07-20_to_2026-07-27.md) — **277 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 45 |
| MoE / Expert Parallel | 39 |
| Other | 26 |
| Prefill / Decode Disaggregation | 25 |
| Multimodal | 19 |
| KV Cache / Memory | 18 |
| Quantization | 17 |
| Triton / Kernels | 17 |
| Speculative Decoding | 13 |
| Models | 11 |
| Scheduler / Batching | 11 |
| CI / Build | 11 |
| ROCm / AMD | 8 |
| Docs / Examples | 5 |
| Structured Output | 4 |
| Serving / API | 4 |
| Tensor / Data Parallel | 3 |
| LoRA | 1 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-07-20 → 2026-07-27](reports/vllm-project_vllm/vllm-project_vllm_2026-07-20_to_2026-07-27.md) — **278 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 37 |
| Other | 37 |
| Attention | 35 |
| MoE / Expert Parallel | 23 |
| CI / Build | 23 |
| KV Cache / Offload | 17 |
| Multimodal | 17 |
| Scheduler / Engine | 16 |
| Quantization | 15 |
| Models | 14 |
| Disaggregation / PD | 11 |
| Serving / API | 11 |
| Docs | 6 |
| Perf / Benchmark | 5 |
| Compilation / CUDA Graph | 4 |
| LoRA | 4 |
| Speculative Decoding | 3 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-07-20 → 2026-07-27](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-07-20_to_2026-07-27.md) — **180 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 53 |
| Attention | 32 |
| Executor / Runtime | 20 |
| MoE | 16 |
| Disaggregation / KV | 16 |
| Models | 13 |
| Quantization | 12 |
| Torch Path (_torch) | 6 |
| Speculative Decoding | 4 |
| Other | 3 |
| Perf | 3 |
| Compilation / Graph | 1 |
| Docs / Examples | 1 |

---

## [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)

TensorRT OSS — Plugins, ONNX parser, Python API, Quantization

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square)

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — GitHub Actions picks it up every Monday

