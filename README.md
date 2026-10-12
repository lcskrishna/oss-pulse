# oss-pulse

> Weekly digest of new features landing across the LLM inference stacks.

### → **[Open the dashboard](https://lcskrishna.github.io/oss-pulse)**

Browse features week by week, filter to ROCm/AMD only, or search across all six repos.

---

## Tracked Repositories

| Repository | Description | Last Report | Features | Commit Activity |
|------------|-------------|:-----------:|:--------:|:---------------:|
| [ROCm/aiter](https://github.com/ROCm/aiter) | AI Tensor Engine for ROCm — optimized GPU kernels (MoE, MLA, GEMM, Attention) | [2026-10-05 → 2026-10-12](reports/ROCm_aiter/ROCm_aiter_2026-10-05_to_2026-10-12.md) | **34** / 115 | ![last-commit](https://img.shields.io/github/last-commit/ROCm/aiter?style=flat-square) |
| [ROCm/mori](https://github.com/ROCm/mori) | Modular RDMA Interface — MORI-EP (Expert Parallel), MORI-IO (KVCache P2P), MORI-CCL | [2026-10-05 → 2026-10-12](reports/ROCm_mori/ROCm_mori_2026-10-05_to_2026-10-12.md) | **4** / 20 | ![last-commit](https://img.shields.io/github/last-commit/ROCm/mori?style=flat-square) |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | SGLang inference engine — PD Disaggregation, MoE/EP, Multimodal, LoRA, ROCm | [2026-10-05 → 2026-10-12](reports/sgl-project_sglang/sgl-project_sglang_2026-10-05_to_2026-10-12.md) | **98** / 537 | ![last-commit](https://img.shields.io/github/last-commit/sgl-project/sglang?style=flat-square) |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | vLLM inference engine — Attention, MoE, Quantization, Disaggregation, ROCm | [2026-10-05 → 2026-10-12](reports/vllm-project_vllm/vllm-project_vllm_2026-10-05_to_2026-10-12.md) | **75** / 455 | ![last-commit](https://img.shields.io/github/last-commit/vllm-project/vllm?style=flat-square) |
| [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | TensorRT-LLM — MoE, Attention, Quantization, AutoDeploy, Disaggregation | [2026-10-05 → 2026-10-12](reports/NVIDIA_TensorRT-LLM/NVIDIA_TensorRT-LLM_2026-10-05_to_2026-10-12.md) | **33** / 138 | ![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT-LLM?style=flat-square) |
| [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT) | TensorRT OSS — Plugins, ONNX parser, Python API, Quantization | [2026-10-05 → 2026-10-12](reports/NVIDIA_TensorRT/NVIDIA_TensorRT_2026-10-05_to_2026-10-12.md) | **0** / 1 | ![last-commit](https://img.shields.io/github/last-commit/NVIDIA/TensorRT?style=flat-square) |

---

## How to Add a Repository

1. Add an entry to `TRACKED` in `scripts/update_dashboard.py`
2. Add a run step in `.github/workflows/weekly-tracker.yml`
3. Push — the next Monday run picks it up automatically

## Run Manually

```bash
python scripts/track_repo_changes.py --repo ROCm/aiter   # fetch one repo's week
python scripts/update_dashboard.py                       # regenerate this README
python scripts/build_dashboard.py                        # regenerate index.html
```

---
_Last updated: 2026-10-12 17:48 UTC_
