---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-09-07 14:16 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-08-31 → 2026-09-07](reports/ROCm_aiter/ROCm_aiter_2026-08-31_to_2026-09-07.md) — **77 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 25 |
| GEMM | 10 |
| CI / Build | 9 |
| Triton Kernels | 7 |
| Quantization | 6 |
| Other | 6 |
| Paged Attention | 4 |
| MHA / Attention | 3 |
| RMSNorm / LayerNorm | 3 |
| MLA | 3 |
| Docs | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-08-31 → 2026-09-07](reports/ROCm_mori/ROCm_mori_2026-08-31_to_2026-09-07.md) — **12 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| MORI-EP (Expert Parallel) | 5 |
| RDMA / Transport | 3 |
| Other | 1 |
| Env / Config | 1 |
| MORI-UMBP (Memory Pool) | 1 |
| MORI-CCL (Collectives) | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-08-31 → 2026-09-07](reports/sgl-project_sglang/sgl-project_sglang_2026-08-31_to_2026-09-07.md) — **421 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 98 |
| Multimodal | 53 |
| Prefill / Decode Disaggregation | 41 |
| MoE / Expert Parallel | 40 |
| KV Cache / Memory | 38 |
| Quantization | 24 |
| Other | 23 |
| Triton / Kernels | 22 |
| CI / Build | 18 |
| ROCm / AMD | 15 |
| Tensor / Data Parallel | 11 |
| Scheduler / Batching | 10 |
| Docs / Examples | 9 |
| Models | 9 |
| Speculative Decoding | 4 |
| LoRA | 2 |
| Structured Output | 2 |
| Serving / API | 2 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-08-31 → 2026-09-07](reports/vllm-project_vllm/vllm-project_vllm_2026-08-31_to_2026-09-07.md) — **370 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 53 |
| Attention | 52 |
| MoE / Expert Parallel | 32 |
| Multimodal | 32 |
| Other | 28 |
| CI / Build | 27 |
| Models | 22 |
| Disaggregation / PD | 22 |
| Quantization | 20 |
| Scheduler / Engine | 19 |
| Serving / API | 16 |
| KV Cache / Offload | 15 |
| Perf / Benchmark | 10 |
| Speculative Decoding | 8 |
| LoRA | 5 |
| Compilation / CUDA Graph | 5 |
| Docs | 4 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-08-31 → 2026-09-07](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-08-31_to_2026-09-07.md) — **259 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 63 |
| Attention | 44 |
| Executor / Runtime | 24 |
| Disaggregation / KV | 22 |
| MoE | 22 |
| Quantization | 19 |
| Torch Path (_torch) | 15 |
| Other | 14 |
| Models | 12 |
| Docs / Examples | 10 |
| Speculative Decoding | 8 |
| ROCm / AMD | 2 |
| LoRA | 2 |
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

