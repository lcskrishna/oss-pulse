---
layout: default
title: "oss-pulse — Weekly OSS Digest"
---

# oss-pulse

> Weekly digest of changes across tracked ROCm OSS repositories.

_Last updated: **2026-06-01 13:49 UTC**_

---

## [ROCm/aiter](https://github.com/ROCm/aiter)

AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention)

![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square)

**Latest report:** [2026-05-25 → 2026-06-01](reports/ROCm_aiter/ROCm_aiter_2026-05-25_to_2026-06-01.md) — **77 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_aiter/)

| Component | Commits |
|-----------|:-------:|
| MoE | 22 |
| GEMM | 15 |
| Other | 9 |
| Quantization | 6 |
| MHA / Attention | 5 |
| Triton Kernels | 5 |
| CI / Build | 5 |
| OPUS / ASM | 4 |
| MLA | 3 |
| Paged Attention | 1 |
| RMSNorm / LayerNorm | 1 |
| CK / CK_TILE | 1 |

---

## [ROCm/mori](https://github.com/ROCm/mori)

Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL

![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square)

**Latest report:** [2026-05-25 → 2026-06-01](reports/ROCm_mori/ROCm_mori_2026-05-25_to_2026-06-01.md) — **5 commits** &nbsp;·&nbsp; [all reports](reports/ROCm_mori/)

| Component | Commits |
|-----------|:-------:|
| RDMA / Transport | 3 |
| JIT / IR / FlyDSL | 1 |
| MORI-IO (KVCache / P2P) | 1 |

---

## [sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm

![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square)

**Latest report:** [2026-05-25 → 2026-06-01](reports/sgl-project_sglang/sgl-project_sglang_2026-05-25_to_2026-06-01.md) — **303 commits** &nbsp;·&nbsp; [all reports](reports/sgl-project_sglang/)

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 60 |
| Prefill / Decode Disaggregation | 35 |
| MoE / Expert Parallel | 31 |
| Multimodal | 22 |
| KV Cache / Memory | 19 |
| Speculative Decoding | 18 |
| Scheduler / Batching | 18 |
| Other | 17 |
| Triton / Kernels | 16 |
| Models | 13 |
| CI / Build | 12 |
| Tensor / Data Parallel | 11 |
| ROCm / AMD | 10 |
| Quantization | 7 |
| Docs / Examples | 6 |
| Structured Output | 5 |
| LoRA | 3 |

---

## [vllm-project/vllm](https://github.com/vllm-project/vllm)

vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm

![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square)

**Latest report:** [2026-05-25 → 2026-06-01](reports/vllm-project_vllm/vllm-project_vllm_2026-05-25_to_2026-06-01.md) — **211 commits** &nbsp;·&nbsp; [all reports](reports/vllm-project_vllm/)

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 44 |
| MoE / Expert Parallel | 26 |
| Other | 26 |
| Models | 19 |
| Multimodal | 15 |
| Attention | 11 |
| Serving / API | 10 |
| Docs | 10 |
| Scheduler / Engine | 10 |
| Disaggregation / PD | 10 |
| Quantization | 9 |
| CI / Build | 9 |
| Speculative Decoding | 5 |
| KV Cache / Offload | 4 |
| Perf / Benchmark | 3 |

---

## [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation

![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square)

**Latest report:** [2026-05-25 → 2026-06-01](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-05-25_to_2026-06-01.md) — **170 commits** &nbsp;·&nbsp; [all reports](reports/NVIDIA_TensorRT-LLM/)

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 41 |
| Attention | 27 |
| MoE | 21 |
| Executor / Runtime | 21 |
| Disaggregation / KV | 11 |
| Torch Path (_torch) | 9 |
| Quantization | 9 |
| Models | 9 |
| Other | 7 |
| AutoDeploy | 7 |
| Docs / Examples | 5 |
| Speculative Decoding | 2 |
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

