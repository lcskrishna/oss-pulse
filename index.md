---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-05-25 12:03 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-05-18 → 2026-05-25](reports/ROCm_aiter/ROCm_aiter_2026-05-18_to_2026-05-25.md) — **55 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| GEMM | 13 |
| MoE | 10 |
| Triton Kernels | 8 |
| CI / Build | 6 |
| Quantization | 5 |
| MLA | 5 |
| MHA / Attention | 3 |
| Other | 3 |
| Paged Attention | 1 |
| OPUS / ASM | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-05-18 → 2026-05-25](reports/ROCm_mori/ROCm_mori_2026-05-18_to_2026-05-25.md) — **10 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| CI / Build | 7 |
| RDMA / Transport | 1 |
| Docs | 1 |
| MORI-EP (Expert Parallel) | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-05-18 → 2026-05-25](reports/sgl-project_sglang/sgl-project_sglang_2026-05-18_to_2026-05-25.md) — **353 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Scheduler / Batching | 52 |
| Attention / FlashInfer | 47 |
| Prefill / Decode Disaggregation | 45 |
| Multimodal | 42 |
| MoE / Expert Parallel | 38 |
| CI / Build | 18 |
| Speculative Decoding | 17 |
| Other | 17 |
| KV Cache / Memory | 15 |
| Quantization | 14 |
| Triton / Kernels | 11 |
| Models | 10 |
| Tensor / Data Parallel | 9 |
| Docs / Examples | 6 |
| ROCm / AMD | 5 |
| Serving / API | 3 |
| LoRA | 2 |
| Structured Output | 2 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-05-18 → 2026-05-25](reports/vllm-project_vllm/vllm-project_vllm_2026-05-18_to_2026-05-25.md) — **236 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 30 |
| Other | 29 |
| MoE / Expert Parallel | 29 |
| Attention | 27 |
| Disaggregation / PD | 18 |
| Multimodal | 16 |
| Quantization | 16 |
| CI / Build | 16 |
| Models | 14 |
| Docs | 8 |
| Scheduler / Engine | 8 |
| Serving / API | 8 |
| KV Cache / Offload | 5 |
| Perf / Benchmark | 4 |
| Speculative Decoding | 4 |
| LoRA | 3 |
| Compilation / CUDA Graph | 1 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-05-18 → 2026-05-25](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-05-18_to_2026-05-25.md) — **186 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 44 |
| MoE | 25 |
| Executor / Runtime | 21 |
| Attention | 20 |
| Models | 16 |
| Other | 14 |
| Disaggregation / KV | 11 |
| Quantization | 9 |
| AutoDeploy | 8 |
| Torch Path (_torch) | 8 |
| Speculative Decoding | 6 |
| Docs / Examples | 2 |
| LoRA | 1 |
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

