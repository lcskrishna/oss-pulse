# vllm-project/vllm — Weekly Change Report
**Period:** 2026-05-18 → 2026-05-25  |  **Total commits:** 236

## ✨ New Features This Week

- **2026-05-25** [#43568](https://github.com/vllm-project/vllm/pull/43568) — [Doc] Add section on escalating stalled contributions (#43568)
- **2026-05-25** [#42296](https://github.com/vllm-project/vllm/pull/42296) — [Feat][KVConnector] Support DSV4 in SimpleCPUOffloadBackend (#42296)
- **2026-05-25** [#40275](https://github.com/vllm-project/vllm/pull/40275) — [Docker] Non-root support for vllm-openai; add opt-in vllm-openai-nonroot target (#40275)
- **2026-05-25** [#43474](https://github.com/vllm-project/vllm/pull/43474) — [Kernel] Add mhc_pre_big_fuse_with_norm_tilelang  (#43474)
- **2026-05-24** [#41735](https://github.com/vllm-project/vllm/pull/41735) — File system secondary tier implemented in python (#41735)
- **2026-05-24** [#43385](https://github.com/vllm-project/vllm/pull/43385) — [ROCm] [DSv4] [Perf] Support DeepSeek v4 MTP (#43385)
- **2026-05-24** [#43142](https://github.com/vllm-project/vllm/pull/43142) — [kv_offload]: Add DSv4 support (#43142)
- **2026-05-23** [#43392](https://github.com/vllm-project/vllm/pull/43392) — [Mooncake] Add metrics for MooncakeStoreConnector operations (#43392)
- **2026-05-23** [#42787](https://github.com/vllm-project/vllm/pull/42787) — [MM] Enable FlashInfer metadata support for Qwen2.5-VL vision attention (#42787)
- **2026-05-23** [#42952](https://github.com/vllm-project/vllm/pull/42952) — [XPU]feat: enable FP8 block-scaled quantization on XPU (#42952)
- _…and 51 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-05-25** [`d4004455d2`](https://github.com/vllm-project/vllm/commit/d4004455d2) [#43554](https://github.com/vllm-project/vllm/pull/43554) — [Kernel] Remove NormGateLinear (#43554)
- **2026-05-25** [`6cbe448eed`](https://github.com/vllm-project/vllm/commit/6cbe448eed) [#42373](https://github.com/vllm-project/vllm/pull/42373) — fix: MoE model using shared routed experts crashes on AMD GPUs (#42373)
- **2026-05-24** [`1806d1adfc`](https://github.com/vllm-project/vllm/commit/1806d1adfc) [#43385](https://github.com/vllm-project/vllm/pull/43385) — [ROCm] [DSv4] [Perf] Support DeepSeek v4 MTP (#43385)
- **2026-05-24** [`5940590855`](https://github.com/vllm-project/vllm/commit/5940590855) [#43016](https://github.com/vllm-project/vllm/pull/43016) — [ROCm][CI] Stabilize 400 error return code for invalid schema inputs (#43016)
- **2026-05-23** [`46f95b2ec2`](https://github.com/vllm-project/vllm/commit/46f95b2ec2) [#43486](https://github.com/vllm-project/vllm/pull/43486) — [ROCm][Critical] Fix the GDN import bug (#43486)
- **2026-05-23** [`2a7d5b7324`](https://github.com/vllm-project/vllm/commit/2a7d5b7324) [#41669](https://github.com/vllm-project/vllm/pull/41669) — [ROCm][CI] Remove benchmarks test group and shard long test groups (#41669)
- **2026-05-23** [`d28bdf9344`](https://github.com/vllm-project/vllm/commit/d28bdf9344) [#41577](https://github.com/vllm-project/vllm/pull/41577) — [ROCm][CI] Fix ROCm LoRA Transformers fallback with full CUDA graphs (#41577)
- **2026-05-23** [`76ea1d5d2f`](https://github.com/vllm-project/vllm/commit/76ea1d5d2f) [#43017](https://github.com/vllm-project/vllm/pull/43017) — [ROCm][CI] Stabilize Granite tool-use and test URL construction (#43017)
- **2026-05-23** [`6a4723a2e0`](https://github.com/vllm-project/vllm/commit/6a4723a2e0) [#43023](https://github.com/vllm-project/vllm/pull/43023) — [ROCm][CI] Stabilize runner teardown between sampler tests (#43023)
- **2026-05-22** [`8de5cabeb7`](https://github.com/vllm-project/vllm/commit/8de5cabeb7) [#42950](https://github.com/vllm-project/vllm/pull/42950) — [XPU]fix: add XPU platform guards to DeepSeek-V4 ops (#42950)
- **2026-05-22** [`843715739b`](https://github.com/vllm-project/vllm/commit/843715739b) [#43149](https://github.com/vllm-project/vllm/pull/43149) — [Refactor] Extract DeepSeek V4 sparse MLA impl into model folder (#43149)
- **2026-05-22** [`a377631d21`](https://github.com/vllm-project/vllm/commit/a377631d21) [#43329](https://github.com/vllm-project/vllm/pull/43329) — [CI] Fix AMD docker build tests (#43329)
- **2026-05-22** [`694d9a81bb`](https://github.com/vllm-project/vllm/commit/694d9a81bb) [#43377](https://github.com/vllm-project/vllm/pull/43377) — [BugFix] Fix setuptools-rust dep in requirements files (#43377)
- **2026-05-22** [`35d0141a0b`](https://github.com/vllm-project/vllm/commit/35d0141a0b) [#43236](https://github.com/vllm-project/vllm/pull/43236) — [ROCm][CI] add warmup to mem_util test before measurement (#43236)
- **2026-05-22** [`86ccef7d44`](https://github.com/vllm-project/vllm/commit/86ccef7d44) [#41753](https://github.com/vllm-project/vllm/pull/41753) — [ROCm] Add XGMI backend for MoRI Connector (#41753)
- **2026-05-21** [`caf69823d6`](https://github.com/vllm-project/vllm/commit/caf69823d6) [#43292](https://github.com/vllm-project/vllm/pull/43292) — [CI] Pin protoc binary in rust-build stages (#43292)
- **2026-05-21** [`f2ace1d57d`](https://github.com/vllm-project/vllm/commit/f2ace1d57d) [#40848](https://github.com/vllm-project/vllm/pull/40848) — [Frontend][RFC] Rust front-end integration (#40848)
- **2026-05-20** [`bde560ed6e`](https://github.com/vllm-project/vllm/commit/bde560ed6e) [#41675](https://github.com/vllm-project/vllm/pull/41675) — [ROCm] Add QuickReduce min-size override and codec threshold (#41675)
- **2026-05-20** [`452baa860b`](https://github.com/vllm-project/vllm/commit/452baa860b) [#42772](https://github.com/vllm-project/vllm/pull/42772) — Add dllehr-amd to CODEOWNERS and committers list (#42772)
- **2026-05-20** [`07aeaf9d4d`](https://github.com/vllm-project/vllm/commit/07aeaf9d4d) [#42663](https://github.com/vllm-project/vllm/pull/42663) — [6/n] Migrate activation kernels, gptq, gguf, non cutlass w8a8 to libtorch stable ABI (continued) (#42663)
- **2026-05-20** [`cd0ff26e7a`](https://github.com/vllm-project/vllm/commit/cd0ff26e7a) [#42111](https://github.com/vllm-project/vllm/pull/42111) — [CI] Add DSV4-Flash to gsm8k moe-refactor/config-b200.txt (#42111)
- **2026-05-19** [`07beaed842`](https://github.com/vllm-project/vllm/commit/07beaed842) [#43077](https://github.com/vllm-project/vllm/pull/43077) — [Model Refactoring] Rename deepseek_v4.py to model.py [4/N] (#43077)
- **2026-05-19** [`b14be81c1f`](https://github.com/vllm-project/vllm/commit/b14be81c1f) [#43073](https://github.com/vllm-project/vllm/pull/43073) — [Model Refactoring] Move deepseek_v4_ops to models/deepseek_v4 [3/N] (#43073)
- **2026-05-19** [`301d986473`](https://github.com/vllm-project/vllm/commit/301d986473) [#42946](https://github.com/vllm-project/vllm/pull/42946) — [Frontend] Consolidate beam search by BeamSearchMixin. (#42946)
- **2026-05-19** [`87b08c5f64`](https://github.com/vllm-project/vllm/commit/87b08c5f64) [#43039](https://github.com/vllm-project/vllm/pull/43039) — [Model Refactoring] Move DeepSeek V4 layers to `models/deepseek_v4/` [2/N] (#43039)
- **2026-05-19** [`287471b994`](https://github.com/vllm-project/vllm/commit/287471b994) [#43004](https://github.com/vllm-project/vllm/pull/43004) — [Model Refactoring] Migrate DeepSeek V4 to vllm/models/ [1/N]  (#43004)
- **2026-05-18** [`8fc1c284b9`](https://github.com/vllm-project/vllm/commit/8fc1c284b9) [#42880](https://github.com/vllm-project/vllm/pull/42880) — [ROCm] Guard AITER GDN decode fast path by layout (#42880)
- **2026-05-18** [`a2c8fc6657`](https://github.com/vllm-project/vllm/commit/a2c8fc6657) [#41436](https://github.com/vllm-project/vllm/pull/41436) — [ROCm][Quantization][3/N] Refactor quark_moe w4a4 w/ oracle (#41436)
- **2026-05-18** [`67f58ce23f`](https://github.com/vllm-project/vllm/commit/67f58ce23f) [#42930](https://github.com/vllm-project/vllm/pull/42930) — [Bugfix] Fix DSV4 MTP after ROCm mHC integration (#42930)
- **2026-05-18** [`b50646e5ef`](https://github.com/vllm-project/vllm/commit/b50646e5ef) [#42909](https://github.com/vllm-project/vllm/pull/42909) — [ROCm][CI] Stabilize ROCm pooling and multimodal CI (#42909)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#43593](https://github.com/vllm-project/vllm/issues/43593) | [Bug]: AssertFail | bug | 2026-05-25 |
| [#43009](https://github.com/vllm-project/vllm/issues/43009) | [Bug]: Triton kernel JIT compilation during inference | bug | 2026-05-25 |
| [#43559](https://github.com/vllm-project/vllm/issues/43559) | [Bug]: Accuracy drops ~20% when `--enable-prefix-caching` is used toge | bug | 2026-05-25 |
| [#42363](https://github.com/vllm-project/vllm/issues/42363) | [Bug]: EngineDeadError with Kimi-K2.6 model using vLLM 0.20.2 | bug | 2026-05-25 |
| [#38656](https://github.com/vllm-project/vllm/issues/38656) | [Bug]: qwen 3.5 model launch get stuck for quite a long time | bug | 2026-05-25 |
| [#34090](https://github.com/vllm-project/vllm/issues/34090) | what am I doing wrong ? libmpi_cxx.so.40: cannot open shared object fi | usage | 2026-05-25 |
| [#43564](https://github.com/vllm-project/vllm/issues/43564) | [Bug] FP8 block-quant loader rejects artifacts using 'weight_scale' ra | — | 2026-05-25 |
| [#43224](https://github.com/vllm-project/vllm/issues/43224) | [RFC]: Porting compiler fusions to manual fusion | RFC | 2026-05-25 |
| [#43563](https://github.com/vllm-project/vllm/issues/43563) | [Usage]: Intel Xeon Prefill Decode Disaggregation | usage | 2026-05-25 |
| [#43561](https://github.com/vllm-project/vllm/issues/43561) | [Usage]: How to run Qwen3.5 models on V100 given the conflicting requi | usage | 2026-05-25 |
| [#43507](https://github.com/vllm-project/vllm/issues/43507) | [Bug] CUTLASS MoE backend unavailable on SM_120/SM_121 (consumer Black | — | 2026-05-25 |
| [#34545](https://github.com/vllm-project/vllm/issues/34545) | [Installation]: unrecognized arguments: --omni | installation, stale | 2026-05-25 |
| [#34859](https://github.com/vllm-project/vllm/issues/34859) | [Bug]: missing shards from quantized checkpoint fails silently | bug, stale | 2026-05-25 |
| [#35084](https://github.com/vllm-project/vllm/issues/35084) | [Bug]: VLLM tries to load "inductor" instead of custom compiler | bug, torch.compile, stale | 2026-05-25 |
| [#35165](https://github.com/vllm-project/vllm/issues/35165) | [Feature]: Add TCP support to MORI KV connector | feature request, stale | 2026-05-25 |
| [#43549](https://github.com/vllm-project/vllm/issues/43549) | [Doc]: Mention Ascend NPU in the main quickstart | — | 2026-05-25 |
| [#43545](https://github.com/vllm-project/vllm/issues/43545) | [RFC]: Add Gumiho speculative decoding to vLLM | RFC | 2026-05-24 |
| [#40554](https://github.com/vllm-project/vllm/issues/40554) | [AMD][CI Failure][Tracker] Static dashboard tracker for current CI fai | rocm, ci-failure | 2026-05-24 |
| [#41820](https://github.com/vllm-project/vllm/issues/41820) | [Performance]: Deepseek-V4 Support and Optimization on ROCm Backend | performance, rocm, DSv4 | 2026-05-24 |
| [#38967](https://github.com/vllm-project/vllm/issues/38967) | [Bug] vLLM >= 0.18.0 NCCL segfault (cuMemCreate) with TP>1 on RTX 4090 | — | 2026-05-24 |

## Summary by Component

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

## ROCm / AMD  (30 commits)

- **2026-05-25** [`d4004455d2`](https://github.com/vllm-project/vllm/commit/d4004455d2) [#43554](https://github.com/vllm-project/vllm/pull/43554)
  [Kernel] Remove NormGateLinear (#43554)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_norm_router_gemm.py`, `csrc/moe/dsv3_router_gemm_bf16_out.cu`, `csrc/moe/dsv3_router_gemm_float_out.cu` _+12 more__
- **2026-05-25** [`6cbe448eed`](https://github.com/vllm-project/vllm/commit/6cbe448eed) [#42373](https://github.com/vllm-project/vllm/pull/42373)
  fix: MoE model using shared routed experts crashes on AMD GPUs (#42373)
  _Files: `vllm/model_executor/layers/fused_moe/router/aiter_shared_routed_fused_moe_router.py`_
- **2026-05-24** [`1806d1adfc`](https://github.com/vllm-project/vllm/commit/1806d1adfc) [#43385](https://github.com/vllm-project/vllm/pull/43385)
  [ROCm] [DSv4] [Perf] Support DeepSeek v4 MTP (#43385)
  _Files: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mtp.py` _+4 more__
- **2026-05-24** [`5940590855`](https://github.com/vllm-project/vllm/commit/5940590855) [#43016](https://github.com/vllm-project/vllm/pull/43016)
  [ROCm][CI] Stabilize 400 error return code for invalid schema inputs (#43016)
  _Files: `tests/entrypoints/openai/completion/test_shutdown.py`, `tests/entrypoints/openai/test_openai_schema.py`, `tests/entrypoints/serve/disagg/test_generate_stream.py`, `tests/entrypoints/weight_transfer/test_weight_transfer_llm.py` _+7 more__
- **2026-05-23** [`46f95b2ec2`](https://github.com/vllm-project/vllm/commit/46f95b2ec2) [#43486](https://github.com/vllm-project/vllm/pull/43486)
  [ROCm][Critical] Fix the GDN import bug (#43486)
  _Files: `tests/compile/passes/test_fusion.py`, `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`_
- **2026-05-23** [`2a7d5b7324`](https://github.com/vllm-project/vllm/commit/2a7d5b7324) [#41669](https://github.com/vllm-project/vllm/pull/41669)
  [ROCm][CI] Remove benchmarks test group and shard long test groups (#41669)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-05-23** [`d28bdf9344`](https://github.com/vllm-project/vllm/commit/d28bdf9344) [#41577](https://github.com/vllm-project/vllm/pull/41577)
  [ROCm][CI] Fix ROCm LoRA Transformers fallback with full CUDA graphs (#41577)
  _Files: `tests/kernels/ir/test_layernorm.py`, `vllm/kernels/vllm_c.py`, `vllm/model_executor/layers/utils.py`, `vllm/model_executor/models/transformers/base.py`_
- **2026-05-23** [`76ea1d5d2f`](https://github.com/vllm-project/vllm/commit/76ea1d5d2f) [#43017](https://github.com/vllm-project/vllm/pull/43017)
  [ROCm][CI] Stabilize Granite tool-use and test URL construction (#43017)
  _Files: `examples/tool_chat_template_granite.jinja`, `tests/tool_use/test_parallel_tool_calls.py`, `tests/tool_use/test_tool_calls.py`, `tests/tool_use/utils.py` _+1 more__
- **2026-05-23** [`6a4723a2e0`](https://github.com/vllm-project/vllm/commit/6a4723a2e0) [#43023](https://github.com/vllm-project/vllm/pull/43023)
  [ROCm][CI] Stabilize runner teardown between sampler tests (#43023)
  _Files: `tests/conftest.py`, `vllm/v1/engine/core.py`_
- **2026-05-22** [`8de5cabeb7`](https://github.com/vllm-project/vllm/commit/8de5cabeb7) [#42950](https://github.com/vllm-project/vllm/pull/42950)
  [XPU]fix: add XPU platform guards to DeepSeek-V4 ops (#42950)
  _Files: `vllm/model_executor/layers/activation.py`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`, `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/nvidia/model.py` _+2 more__
- **2026-05-22** [`843715739b`](https://github.com/vllm-project/vllm/commit/843715739b) [#43149](https://github.com/vllm-project/vllm/pull/43149)
  [Refactor] Extract DeepSeek V4 sparse MLA impl into model folder (#43149)
  _Files: `docs/design/attention_backends.md`, `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/kernels/test_fused_inv_rope_fp8_quant.py`, `vllm/models/deepseek_v4/amd/rocm.py` _+5 more__
- **2026-05-22** [`a377631d21`](https://github.com/vllm-project/vllm/commit/a377631d21) [#43329](https://github.com/vllm-project/vllm/pull/43329)
  [CI] Fix AMD docker build tests (#43329)
  _Files: `CMakeLists.txt`, `cmake/utils.cmake`_
- **2026-05-22** [`694d9a81bb`](https://github.com/vllm-project/vllm/commit/694d9a81bb) [#43377](https://github.com/vllm-project/vllm/pull/43377)
  [BugFix] Fix setuptools-rust dep in requirements files (#43377)
  _Files: `requirements/build/rocm.txt`, `requirements/build/tpu.txt`, `requirements/xpu.txt`_
- **2026-05-22** [`35d0141a0b`](https://github.com/vllm-project/vllm/commit/35d0141a0b) [#43236](https://github.com/vllm-project/vllm/pull/43236)
  [ROCm][CI] add warmup to mem_util test before measurement (#43236)
  _Files: `tests/utils_/test_mem_utils.py`_
- **2026-05-22** [`86ccef7d44`](https://github.com/vllm-project/vllm/commit/86ccef7d44) [#41753](https://github.com/vllm-project/vllm/pull/41753)
  [ROCm] Add XGMI backend for MoRI Connector (#41753)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`_
- **2026-05-21** [`caf69823d6`](https://github.com/vllm-project/vllm/commit/caf69823d6) [#43292](https://github.com/vllm-project/vllm/pull/43292)
  [CI] Pin protoc binary in rust-build stages (#43292)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cpu`, `docker/Dockerfile.nightly_torch`, `docker/Dockerfile.rocm` _+2 more__
- **2026-05-21** [`f2ace1d57d`](https://github.com/vllm-project/vllm/commit/f2ace1d57d) [#40848](https://github.com/vllm-project/vllm/pull/40848)
  [Frontend][RFC] Rust front-end integration (#40848)
  _Files: `.buildkite/image_build/image_build.sh`, `.buildkite/image_build/image_build_cpu.sh`, `.buildkite/image_build/image_build_cpu_arm64.sh`, `.buildkite/image_build/image_build_hpu.sh` _+31 more__
- **2026-05-20** [`bde560ed6e`](https://github.com/vllm-project/vllm/commit/bde560ed6e) [#41675](https://github.com/vllm-project/vllm/pull/41675)
  [ROCm] Add QuickReduce min-size override and codec threshold (#41675)
  _Files: `tests/distributed/test_quick_all_reduce.py`, `vllm/distributed/device_communicators/quick_all_reduce.py`, `vllm/envs.py`_
- **2026-05-20** [`452baa860b`](https://github.com/vllm-project/vllm/commit/452baa860b) [#42772](https://github.com/vllm-project/vllm/pull/42772)
  Add dllehr-amd to CODEOWNERS and committers list (#42772)
  _Files: `.github/CODEOWNERS`, `docs/governance/committers.md`_
- **2026-05-20** [`07aeaf9d4d`](https://github.com/vllm-project/vllm/commit/07aeaf9d4d) [#42663](https://github.com/vllm-project/vllm/pull/42663)
  [6/n] Migrate activation kernels, gptq, gguf, non cutlass w8a8 to libtorch stable ABI (continued) (#42663)
  _Files: `CMakeLists.txt`, `csrc/attention/dtype_fp8.cuh`, `csrc/cuda_vec_utils.cuh`, `csrc/cutlass_extensions/torch_utils.hpp` _+24 more__
- **2026-05-20** [`cd0ff26e7a`](https://github.com/vllm-project/vllm/commit/cd0ff26e7a) [#42111](https://github.com/vllm-project/vllm/pull/42111)
  [CI] Add DSV4-Flash to gsm8k moe-refactor/config-b200.txt (#42111)
  _Files: `requirements/common.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt`, `requirements/test/xpu.txt` _+2 more__
- **2026-05-19** [`07beaed842`](https://github.com/vllm-project/vllm/commit/07beaed842) [#43077](https://github.com/vllm-project/vllm/pull/43077)
  [Model Refactoring] Rename deepseek_v4.py to model.py [4/N] (#43077)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/__init__.py`, `vllm/models/deepseek_v4/amd/deepseek_v4.py`, `vllm/models/deepseek_v4/amd/deepseek_v4_mtp.py` _+4 more__
- **2026-05-19** [`b14be81c1f`](https://github.com/vllm-project/vllm/commit/b14be81c1f) [#43073](https://github.com/vllm-project/vllm/pull/43073)
  [Model Refactoring] Move deepseek_v4_ops to models/deepseek_v4 [3/N] (#43073)
  _Files: `.github/CODEOWNERS`, `tests/kernels/core/test_fused_q_kv_rmsnorm.py`, `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` _+16 more__
- **2026-05-19** [`301d986473`](https://github.com/vllm-project/vllm/commit/301d986473) [#42946](https://github.com/vllm-project/vllm/pull/42946)
  [Frontend] Consolidate beam search by BeamSearchMixin. (#42946)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/samplers.yaml`, `vllm/entrypoints/generate/__init__.py`, `vllm/entrypoints/generate/beam_search/__init__.py` _+5 more__
- **2026-05-19** [`87b08c5f64`](https://github.com/vllm-project/vllm/commit/87b08c5f64) [#43039](https://github.com/vllm-project/vllm/pull/43039)
  [Model Refactoring] Move DeepSeek V4 layers to `models/deepseek_v4/` [2/N] (#43039)
  _Files: `.github/CODEOWNERS`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/nvidia/deepseek_v4.py` _+1 more__
- **2026-05-19** [`287471b994`](https://github.com/vllm-project/vllm/commit/287471b994) [#43004](https://github.com/vllm-project/vllm/pull/43004)
  [Model Refactoring] Migrate DeepSeek V4 to vllm/models/ [1/N]  (#43004)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/model_executor/layers/quantization/__init__.py`, `vllm/model_executor/models/registry.py`, `vllm/models/__init__.py` _+8 more__
- **2026-05-18** [`8fc1c284b9`](https://github.com/vllm-project/vllm/commit/8fc1c284b9) [#42880](https://github.com/vllm-project/vllm/pull/42880)
  [ROCm] Guard AITER GDN decode fast path by layout (#42880)
  _Files: `vllm/model_executor/layers/mamba/gdn_linear_attn.py`_
- **2026-05-18** [`a2c8fc6657`](https://github.com/vllm-project/vllm/commit/a2c8fc6657) [#41436](https://github.com/vllm-project/vllm/pull/41436)
  [ROCm][Quantization][3/N] Refactor quark_moe w4a4 w/ oracle (#41436)
  _Files: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-EMU-TP2.yaml`, `tests/evals/gsm8k/configs/models-mi3xx.txt`, `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` _+4 more__
- **2026-05-18** [`67f58ce23f`](https://github.com/vllm-project/vllm/commit/67f58ce23f) [#42930](https://github.com/vllm-project/vllm/pull/42930)
  [Bugfix] Fix DSV4 MTP after ROCm mHC integration (#42930)
  _Files: `vllm/model_executor/models/deepseek_v4.py`, `vllm/model_executor/models/deepseek_v4_mtp.py`_
- **2026-05-18** [`b50646e5ef`](https://github.com/vllm-project/vllm/commit/b50646e5ef) [#42909](https://github.com/vllm-project/vllm/pull/42909)
  [ROCm][CI] Stabilize ROCm pooling and multimodal CI (#42909)
  _Files: `tests/models/language/pooling/test_gritlm.py`, `tests/models/language/pooling/test_max_tokens_per_doc.py`, `tests/models/multimodal/generation/test_qwen2_5_vl.py`, `vllm/model_executor/models/transformers/base.py`_

## Other  (29 commits)

- **2026-05-25** [`716d5294e6`](https://github.com/vllm-project/vllm/commit/716d5294e6) [#43583](https://github.com/vllm-project/vllm/pull/43583)
  [Misc] Print accuracy value for PD tests even on success  (#43583)
  _Files: `tests/v1/kv_connector/nixl_integration/test_accuracy.py`_
- **2026-05-24** [`d0a100c87a`](https://github.com/vllm-project/vllm/commit/d0a100c87a) [#41735](https://github.com/vllm-project/vllm/pull/41735)
  File system secondary tier implemented in python (#41735)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`, `tests/v1/kv_offload/test_file_mapper.py`, `tests/v1/kv_offload/test_fs_tier.py`, `vllm/v1/kv_offload/file_mapper.py` _+5 more__
- **2026-05-23** [`b32fe416ea`](https://github.com/vllm-project/vllm/commit/b32fe416ea) [#42691](https://github.com/vllm-project/vllm/pull/42691)
  [Bugfix] Fix reasoning dropped on streaming boundary deltas (#42691)
  _Files: `tests/parser/test_streaming.py`, `vllm/parser/abstract_parser.py`_
- **2026-05-23** [`3a1c062151`](https://github.com/vllm-project/vllm/commit/3a1c062151) [#43383](https://github.com/vllm-project/vllm/pull/43383)
  [Misc] Added missing return type annotations to improve mypy and IDE tooling (#43383)
  _Files: `vllm/model_executor/layers/pooler/activations.py`, `vllm/model_executor/layers/pooler/seqwise/methods.py`, `vllm/model_executor/layers/pooler/special.py`, `vllm/v1/pool/metadata.py`_
- **2026-05-22** [`08cb46789d`](https://github.com/vllm-project/vllm/commit/08cb46789d) [#43437](https://github.com/vllm-project/vllm/pull/43437)
  mhc_post - remove sts & add vectorized copies (#43437)
  _Files: `vllm/_tilelang_ops.py`_
- **2026-05-22** [`b3c7ffcab8`](https://github.com/vllm-project/vllm/commit/b3c7ffcab8) [#43286](https://github.com/vllm-project/vllm/pull/43286)
  [Misc] Replace assert with proper exceptions for security and validation in pooling (#43286)
  _Files: `tests/model_executor/layers/test_pooler_activations.py`, `vllm/model_executor/layers/pooler/activations.py`, `vllm/pooling_params.py`, `vllm/v1/pool/metadata.py`_
- **2026-05-22** [`6bb8753db1`](https://github.com/vllm-project/vllm/commit/6bb8753db1) [#43321](https://github.com/vllm-project/vllm/pull/43321)
  Correcting the mock classes for MM GC tests (#43321)
  _Files: `tests/v1/cudagraph/test_encoder_cudagraph.py`_
- **2026-05-22** [`18a27cc9a3`](https://github.com/vllm-project/vllm/commit/18a27cc9a3) [#43020](https://github.com/vllm-project/vllm/pull/43020)
  [Bugfix] Make CuMemAllocator free callback stream-aware (#43020)
  _Files: `vllm/device_allocator/cumem.py`_
- **2026-05-22** [`39910f2b25`](https://github.com/vllm-project/vllm/commit/39910f2b25) [#43283](https://github.com/vllm-project/vllm/pull/43283)
  [Rust Frontend] Move code from `vllm-frontend-rs` (#43283)
- **2026-05-21** [`565b745ec5`](https://github.com/vllm-project/vllm/commit/565b745ec5) [#43125](https://github.com/vllm-project/vllm/pull/43125)
  [BugFix] Use correct logprobs for `logprob_token_ids` (#43125)
  _Files: `vllm/v1/sample/sampler.py`_
- **2026-05-21** [`17b69828a0`](https://github.com/vllm-project/vllm/commit/17b69828a0) [#43105](https://github.com/vllm-project/vllm/pull/43105)
  [Core] Add native ModelExpress load format (#43105)
  _Files: `tests/model_executor/model_loader/test_modelexpress_loader.py`, `vllm/config/load.py`, `vllm/config/vllm.py`, `vllm/model_executor/model_loader/__init__.py` _+1 more__
- **2026-05-21** [`1c78f76c29`](https://github.com/vllm-project/vllm/commit/1c78f76c29) [#43079](https://github.com/vllm-project/vllm/pull/43079)
  [Bugfix] Add early validation to reject incompatible runner types for embedding models (#43079)
  _Files: `vllm/config/model.py`_
- **2026-05-21** [`ebbfb34e3e`](https://github.com/vllm-project/vllm/commit/ebbfb34e3e) [#43085](https://github.com/vllm-project/vllm/pull/43085)
  [Test] Replace zephyr-7b-beta (7B) with SmolLM2-135M in tokenization test (#43085)
  _Files: `tests/entrypoints/serve/tokenize/test_tokenization.py`_
- **2026-05-21** [`6441cf4a44`](https://github.com/vllm-project/vllm/commit/6441cf4a44) [#43140](https://github.com/vllm-project/vllm/pull/43140)
  [Refactor] Use shared coerce_to_schema_type in Seed-OSS tool parser (#43140)
  _Files: `vllm/tool_parsers/seed_oss_tool_parser.py`_
- **2026-05-20** [`ded871201a`](https://github.com/vllm-project/vllm/commit/ded871201a) [#42452](https://github.com/vllm-project/vllm/pull/42452)
  [Bug][Structured Outputs] Fix bug that leads to unconstrained generations with structural tags (#42452)
  _Files: `tests/v1/structured_output/test_reasoning_structured_output.py`, `vllm/v1/structured_output/__init__.py`_
- **2026-05-20** [`1cb224430b`](https://github.com/vllm-project/vllm/commit/1cb224430b) [#40717](https://github.com/vllm-project/vllm/pull/40717)
  [GDN] Enable FI Blackwell GDN prefill kernel (#40717)
  _Files: `vllm/model_executor/layers/mamba/gdn_linear_attn.py`, `vllm/platforms/cuda.py`_
- **2026-05-20** [`9b343dd4f5`](https://github.com/vllm-project/vllm/commit/9b343dd4f5) [#43192](https://github.com/vllm-project/vllm/pull/43192)
  Enable mermaid diagrams in the docs (#43192)
  _Files: `mkdocs.yaml`_
- **2026-05-20** [`73dd2f33b7`](https://github.com/vllm-project/vllm/commit/73dd2f33b7) [#43121](https://github.com/vllm-project/vllm/pull/43121)
  [bug] fix WeightTransferConfig.backend to allow for all strings (#43121)
  _Files: `tests/distributed/test_weight_transfer.py`, `vllm/config/weight_transfer.py`_
- **2026-05-19** [`42b4f1fdf7`](https://github.com/vllm-project/vllm/commit/42b4f1fdf7) [#43025](https://github.com/vllm-project/vllm/pull/43025)
  [Refactor] Extract extract_types_from_schema utility from Minimax M2 tool parser (#43025)
  _Files: `tests/tool_parsers/test_utils.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`, `vllm/tool_parsers/utils.py`_
- **2026-05-19** [`4a4fdabe28`](https://github.com/vllm-project/vllm/commit/4a4fdabe28) [#43041](https://github.com/vllm-project/vllm/pull/43041)
  [Misc] Aligning tokwise pooler heads for consistency (#43041)
  _Files: `vllm/model_executor/layers/pooler/seqwise/poolers.py`, `vllm/model_executor/layers/pooler/tokwise/__init__.py`, `vllm/model_executor/layers/pooler/tokwise/heads.py`, `vllm/model_executor/layers/pooler/tokwise/poolers.py`_
- **2026-05-19** [`f1e3f0e6d6`](https://github.com/vllm-project/vllm/commit/f1e3f0e6d6) [#41354](https://github.com/vllm-project/vllm/pull/41354)
  [XPU] Use custom op collective behavior  (#41354)
  _Files: `vllm/platforms/xpu.py`_
- **2026-05-19** [`27f4ba9481`](https://github.com/vllm-project/vllm/commit/27f4ba9481) [#42671](https://github.com/vllm-project/vllm/pull/42671)
  fix: use keyword arguments for shard_id and expert_id in weight_loade… (#42671)
- **2026-05-18** [`57fef4e0bf`](https://github.com/vllm-project/vllm/commit/57fef4e0bf) [#43006](https://github.com/vllm-project/vllm/pull/43006)
  [Refactor] Extract shared coerce_to_schema_type utility from Minimax M2 tool parser (#43006)
  _Files: `tests/tool_parsers/test_utils.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`, `vllm/tool_parsers/utils.py`_
- **2026-05-18** [`84747489de`](https://github.com/vllm-project/vllm/commit/84747489de) [#42529](https://github.com/vllm-project/vllm/pull/42529)
  Tier offload followup (#42529)
  _Files: `tests/v1/kv_offload/test_tiering_offloading.py`, `vllm/v1/kv_offload/cpu/spec.py`, `vllm/v1/kv_offload/tiering/base.py`, `vllm/v1/kv_offload/tiering/example/__init__.py` _+4 more__
- **2026-05-18** [`b12745e4f3`](https://github.com/vllm-project/vllm/commit/b12745e4f3) [#42935](https://github.com/vllm-project/vllm/pull/42935)
  Fix `--convert` passed without `--runner` on causal models (#42935)
  _Files: `vllm/config/model.py`_
- **2026-05-18** [`e26736973a`](https://github.com/vllm-project/vllm/commit/e26736973a) [#42778](https://github.com/vllm-project/vllm/pull/42778)
  [Model Runner V2] Fix prompt logprobs calculation `Sizes of tensors must match` error (#42778)
  _Files: `vllm/v1/worker/gpu/sample/prompt_logprob.py`_
- **2026-05-18** [`f5d3dc7115`](https://github.com/vllm-project/vllm/commit/f5d3dc7115) [#42783](https://github.com/vllm-project/vllm/pull/42783)
  [Model Runner v2] Support update_config (#42783)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-05-18** [`69c91d010a`](https://github.com/vllm-project/vllm/commit/69c91d010a) [#42955](https://github.com/vllm-project/vllm/pull/42955)
  [MRv2] Default to MRv1 when a connector is present (#42955)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-05-18** [`cac81b6eda`](https://github.com/vllm-project/vllm/commit/cac81b6eda) [#42666](https://github.com/vllm-project/vllm/pull/42666)
  [CPU Backend] Improve cpu thread utilization (#42666)
  _Files: `csrc/cpu/cpu_attn_impl.hpp`, `vllm/utils/ompmultiprocessing.py`_

## MoE / Expert Parallel  (29 commits)

- **2026-05-23** [`4438b6e7dc`](https://github.com/vllm-project/vllm/commit/4438b6e7dc) [#42680](https://github.com/vllm-project/vllm/pull/42680)
  [MoE] Migrate W4A8 CT to oracle kernel setup (#42680)
  _Files: `vllm/model_executor/layers/fused_moe/__init__.py`, `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/w4a8.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a8_fp8.py`_
- **2026-05-23** [`d19db10974`](https://github.com/vllm-project/vllm/commit/d19db10974) [#42739](https://github.com/vllm-project/vllm/pull/42739)
  [Bugfix] Fix native Triton top-k/top-p kernel assumes contiguous logi… (#42739)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_triton.py`_
- **2026-05-23** [`54d153637b`](https://github.com/vllm-project/vllm/commit/54d153637b) [#42915](https://github.com/vllm-project/vllm/pull/42915)
  [XPU] reudce host overhead of XPU MOE (#42915)
  _Files: `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`_
- **2026-05-22** [`6d30655b13`](https://github.com/vllm-project/vllm/commit/6d30655b13) [#40881](https://github.com/vllm-project/vllm/pull/40881)
  elastic_ep: stage/commit MoE quant method on reconfigure (#40881)
  _Files: `vllm/distributed/device_communicators/all2all.py`, `vllm/distributed/elastic_ep/elastic_execute.py`, `vllm/model_executor/layers/fused_moe/all2all_utils.py`, `vllm/model_executor/layers/fused_moe/eep_reconfigure.py` _+3 more__
- **2026-05-22** [`e203006a8b`](https://github.com/vllm-project/vllm/commit/e203006a8b) [#42566](https://github.com/vllm-project/vllm/pull/42566)
  [Quantization][ModelOpt] W4A16 NVFP4 fused MoE + mixed-precision dispatch (#42566)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-05-22** [`fb21d8b4f9`](https://github.com/vllm-project/vllm/commit/fb21d8b4f9) [#42209](https://github.com/vllm-project/vllm/pull/42209)
  Add NVFP4 MOE support for Deepseek V4. (#42209)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/moe/test_trtllm_nvfp4_moe.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py` _+5 more__
- **2026-05-22** [`15f7cd33dc`](https://github.com/vllm-project/vllm/commit/15f7cd33dc) [#42737](https://github.com/vllm-project/vllm/pull/42737)
  [LoRA] Reduce memory of 2D weights when EP is set (#42737)
  _Files: `tests/lora/test_moe_lora_ep_load.py`, `vllm/lora/lora_model.py`, `vllm/lora/model_manager.py`, `vllm/lora/worker_manager.py`_
- **2026-05-22** [`d3d1cf6972`](https://github.com/vllm-project/vllm/commit/d3d1cf6972) [#42951](https://github.com/vllm-project/vllm/pull/42951)
  [XPU]feat: add XPU fallback for MoE topk routing and MXFP4 backend (#42951)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`_
- **2026-05-22** [`025d4f5cd2`](https://github.com/vllm-project/vllm/commit/025d4f5cd2) [#43296](https://github.com/vllm-project/vllm/pull/43296)
  [CI] Fix "test_awq_load[gemma4-moe-*]" failure (#43296)
  _Files: `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-05-22** [`2998a047aa`](https://github.com/vllm-project/vllm/commit/2998a047aa) [#42855](https://github.com/vllm-project/vllm/pull/42855)
  [Bugfix] Fix DSV4 Base model swiglu limit issue in FP8 path  (#42855)
  _Files: `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutlass_moe.py`, `vllm/model_executor/layers/fused_moe/experts/fused_batched_moe.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`_
- **2026-05-21** [`9b54e50e2c`](https://github.com/vllm-project/vllm/commit/9b54e50e2c) [#43148](https://github.com/vllm-project/vllm/pull/43148)
  [Deprecation] Mark env vars covered by --moe-backend / --linear-backend (#43148)
  _Files: `vllm/envs.py`, `vllm/model_executor/kernels/linear/__init__.py`_
- **2026-05-21** [`edafea3555`](https://github.com/vllm-project/vllm/commit/edafea3555) [#43223](https://github.com/vllm-project/vllm/pull/43223)
  Fix FlashInfer TRTLLM NvFP4 monolithic MoE routing (#43223)
  _Files: `vllm/model_executor/layers/fused_moe/config.py`_
- **2026-05-21** [`050611a3dd`](https://github.com/vllm-project/vllm/commit/050611a3dd) [#39601](https://github.com/vllm-project/vllm/pull/39601)
  [Bugfix] Fix glm4_moe_tool_parser._is_string_type for /v1/responses FunctionTool format (#39601)
  _Files: `tests/tool_parsers/test_glm4_moe_tool_parser.py`, `vllm/tool_parsers/glm4_moe_tool_parser.py`_
- **2026-05-20** [`5774aad9c5`](https://github.com/vllm-project/vllm/commit/5774aad9c5) [#43135](https://github.com/vllm-project/vllm/pull/43135)
  [Perf][gpt-oss] Downgrade triton_kernels to v3.5.1 (#43135)
  _Files: `cmake/external_projects/triton_kernels.cmake`, `tests/kernels/quantization/test_mxfp4_triton_ep.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`_
- **2026-05-20** [`363fc84407`](https://github.com/vllm-project/vllm/commit/363fc84407) [#40082](https://github.com/vllm-project/vllm/pull/40082)
  Integrate flashinfer b12x MoE and FP4 GEMM kernels for SM120/121 (#40082)
  _Files: `tests/kernels/moe/test_flashinfer_b12x_moe.py`, `tests/kernels/quantization/test_flashinfer_nvfp4_scaled_mm.py`, `vllm/config/kernel.py`, `vllm/envs.py` _+6 more__
- **2026-05-20** [`5774aaed0c`](https://github.com/vllm-project/vllm/commit/5774aaed0c) [#43143](https://github.com/vllm-project/vllm/pull/43143)
  [Cohere] Enable Cohere MoE (#43143)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`_
- **2026-05-19** [`f54721bcc3`](https://github.com/vllm-project/vllm/commit/f54721bcc3) [#42976](https://github.com/vllm-project/vllm/pull/42976)
  [Bugfix][MoE] FlashInfer one-sided: workspace union across heterogeneous layers (#42976)
  _Files: `tests/distributed/test_mnnvl_alltoall.py`, `vllm/distributed/device_communicators/all2all.py`_
- **2026-05-19** [`b82e908b4c`](https://github.com/vllm-project/vllm/commit/b82e908b4c) [#42347](https://github.com/vllm-project/vllm/pull/42347)
  [Perf][4/n] Eliminate various GPU<->CPU syncs (#42347)
  _Files: `tests/v1/logits_processors/test_correctness.py`, `vllm/lora/ops/triton_ops/utils.py`, `vllm/lora/punica_wrapper/utils.py`, `vllm/model_executor/models/bert.py` _+19 more__
- **2026-05-19** [`8f16c4a5c0`](https://github.com/vllm-project/vllm/commit/8f16c4a5c0) [#42468](https://github.com/vllm-project/vllm/pull/42468)
  [BugFix][CPU][Spec Decode] Fix Eagle implementation on CPU backend (#42468)
  _Files: `vllm/v1/sample/ops/topk_topp_sampler.py`, `vllm/v1/worker/cpu_model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-05-18** [`00e20e76f7`](https://github.com/vllm-project/vllm/commit/00e20e76f7) [#42767](https://github.com/vllm-project/vllm/pull/42767)
  [Refactor] Remove dead cuda kernels (#42767)
  _Files: `CMakeLists.txt`, `csrc/attention/vertical_slash_index.cu`, `csrc/moe/torch_bindings.cpp`, `csrc/ops.h` _+2 more__
- **2026-05-18** [`6859ca7615`](https://github.com/vllm-project/vllm/commit/6859ca7615) [#42541](https://github.com/vllm-project/vllm/pull/42541)
  [Bugfix] fix swiglu limit issue for humming backend + deepseek v4 (#42541)
  _Files: `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/utils/humming_utils.py`_
- **2026-05-18** [`8c296de63b`](https://github.com/vllm-project/vllm/commit/8c296de63b) [#42857](https://github.com/vllm-project/vllm/pull/42857)
  [Perf] Re-enable flashinfer autotune by default and cleanup (#42857)
  _Files: `vllm/config/vllm.py`, `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py`, `vllm/model_executor/warmup/kernel_warmup.py` _+1 more__
- **2026-05-18** [`78e7a7b9b0`](https://github.com/vllm-project/vllm/commit/78e7a7b9b0) [#42483](https://github.com/vllm-project/vllm/pull/42483)
  Refactor AWQ Marlin MoE onto modular WNA16 oracle (#42483)
  _Files: `tests/kernels/moe/test_moe.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py` _+2 more__
- **2026-05-18** [`2e40faf08b`](https://github.com/vllm-project/vllm/commit/2e40faf08b) [#42954](https://github.com/vllm-project/vllm/pull/42954)
  [XPU][CI] Temporarily skip test_moe_lora_align_block_size_mixed_base_and_lora[1] in Intel GPU CI (#42954)
  _Files: `.buildkite/intel_jobs/lora_intel.yaml`_
- **2026-05-18** [`88a860d754`](https://github.com/vllm-project/vllm/commit/88a860d754) [#41922](https://github.com/vllm-project/vllm/pull/41922)
  [CPU] Add MXFP4 W4A16 MoE support (#41922)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `csrc/cpu/sgl-kernels/common.h`, `csrc/cpu/sgl-kernels/gemm.h`, `csrc/cpu/sgl-kernels/gemm_fp8.cpp` _+12 more__
- **2026-05-18** [`2267f70070`](https://github.com/vllm-project/vllm/commit/2267f70070) [#42527](https://github.com/vllm-project/vllm/pull/42527)
  [Kernel] Pack topk id/weights triton kernel (#42527)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py`, `vllm/model_executor/layers/fused_moe/utils.py`_
- **2026-05-18** [`7d5b033782`](https://github.com/vllm-project/vllm/commit/7d5b033782) [#42242](https://github.com/vllm-project/vllm/pull/42242)
  [LoRA] Support 2D and 3D MoE LoRA adapter  at the same time (#42242)
  _Files: `docs/features/lora.md`, `tests/lora/conftest.py`, `tests/lora/test_qwen36_moe_lora.py`, `tests/lora/test_qwen3moe_tp.py` _+12 more__
- **2026-05-18** [`e3aeee5ff8`](https://github.com/vllm-project/vllm/commit/e3aeee5ff8) [#40131](https://github.com/vllm-project/vllm/pull/40131)
  [Bugfix] moe lora align kernel grid (#40131)
  _Files: `csrc/moe/moe_align_sum_kernels.cu`, `tests/lora/test_moe_lora_align_sum.py`_
- **2026-05-18** [`03ddc1c9bc`](https://github.com/vllm-project/vllm/commit/03ddc1c9bc) [#42497](https://github.com/vllm-project/vllm/pull/42497)
  [Perf] Wire silu_and_mul_per_block_quant into TritonFP8MoE (MiniMax-M2)  (#42497)
  _Files: `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`_

## Attention  (27 commits)

- **2026-05-23** [`a0be71ee47`](https://github.com/vllm-project/vllm/commit/a0be71ee47) [#42787](https://github.com/vllm-project/vllm/pull/42787)
  [MM] Enable FlashInfer metadata support for Qwen2.5-VL vision attention (#42787)
  _Files: `vllm/model_executor/models/qwen2_5_vl.py`_
- **2026-05-23** [`367cb81966`](https://github.com/vllm-project/vllm/commit/367cb81966) [#42925](https://github.com/vllm-project/vllm/pull/42925)
  [DSV4] More multi-stream enablement for c4a (#42925)
  _Files: `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/ops/attention.py`_
- **2026-05-23** [`552bbe6f4e`](https://github.com/vllm-project/vllm/commit/552bbe6f4e) [#38822](https://github.com/vllm-project/vllm/pull/38822)
  [Attention] Add head_dim=512 support for FlashInfer trtllm attention backend (#38822)
  _Files: `docs/design/attention_backends.md`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-05-22** [`23f7b11bf4`](https://github.com/vllm-project/vllm/commit/23f7b11bf4) [#43427](https://github.com/vllm-project/vllm/pull/43427)
  [Bugfix] Detect wrong libcute_dsl_runtime.so variant in FlashInfer GDN (#43427)
  _Files: `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-05-22** [`c7624bea5e`](https://github.com/vllm-project/vllm/commit/c7624bea5e) [#42650](https://github.com/vllm-project/vllm/pull/42650)
  [Bugfix] Source num_qo_heads from Attention layers in Flashinfer/Triton metadata builders (#42650)
  _Files: `vllm/v1/attention/backends/flashinfer.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/backends/utils.py`_
- **2026-05-22** [`7e1b45a092`](https://github.com/vllm-project/vllm/commit/7e1b45a092) [#41126](https://github.com/vllm-project/vllm/pull/41126)
  [Attention] Mamba attention module refactor (#41126)
  _Files: `vllm/config/compilation.py`, `vllm/model_executor/layers/mamba/gdn/__init__.py`, `vllm/model_executor/layers/mamba/gdn/base.py`, `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` _+6 more__
- **2026-05-22** [`8c8b1825eb`](https://github.com/vllm-project/vllm/commit/8c8b1825eb) [#37888](https://github.com/vllm-project/vllm/pull/37888)
  [XPU] Enable multiple key kernels for sparse attention (#37888)
  _Files: `vllm/_custom_ops.py`, `vllm/_xpu_ops.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-05-21** [`39d5fa96a7`](https://github.com/vllm-project/vllm/commit/39d5fa96a7) [#41873](https://github.com/vllm-project/vllm/pull/41873)
  [Bugfix] Zero stale is_prefilling in padded CUDA graph rows for Mamba (#41873)
  _Files: `tests/v1/attention/test_attention_splitting.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-05-21** [`b29cbf0652`](https://github.com/vllm-project/vllm/commit/b29cbf0652) [#42988](https://github.com/vllm-project/vllm/pull/42988)
  [Perf] `zeros` -> `empty` to remove additional fill (#42988)
  _Files: `vllm/_custom_ops.py`, `vllm/model_executor/layers/mamba/gdn_linear_attn.py`, `vllm/model_executor/layers/quantization/utils/fp8_utils.py`, `vllm/v1/attention/backends/turboquant_attn.py`_
- **2026-05-21** [`c68c55d43e`](https://github.com/vllm-project/vllm/commit/c68c55d43e) [#42943](https://github.com/vllm-project/vllm/pull/42943)
  [CPU][RISC-V] Add VLEN=256 support to RVV attention kernels (#42943)
  _Files: `csrc/cpu/cpu_attn_rvv.hpp`, `csrc/cpu/cpu_types_riscv_defs.hpp`, `csrc/cpu/generate_cpu_attn_dispatch.py`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-05-21** [`ee05e8137e`](https://github.com/vllm-project/vllm/commit/ee05e8137e) [#43103](https://github.com/vllm-project/vllm/pull/43103)
  [Minor]  Bigger overlap for FI AR (#43103)
  _Files: `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-05-20** [`2a43b407c5`](https://github.com/vllm-project/vllm/commit/2a43b407c5) [#43237](https://github.com/vllm-project/vllm/pull/43237)
  [Bugfix][CI] Add missing import of pad_nvfp4_activation_for_cutlass in flashinfer (#43237)
  _Files: `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`_
- **2026-05-20** [`c628a93a64`](https://github.com/vllm-project/vllm/commit/c628a93a64) [#40727](https://github.com/vllm-project/vllm/pull/40727)
  [Perf][Bugfix] Update dflash aux layer indexing (#40727)
  _Files: `tests/v1/e2e/spec_decode/test_spec_decode.py`, `vllm/transformers_utils/configs/speculators/algos.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-05-19** [`9aaf83ef50`](https://github.com/vllm-project/vllm/commit/9aaf83ef50) [#43119](https://github.com/vllm-project/vllm/pull/43119)
  [CI failure] Temporarily disable using persistent cache for flashinfer autotune (#43119)
  _Files: `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-05-19** [`d247a931cc`](https://github.com/vllm-project/vllm/commit/d247a931cc) [#42080](https://github.com/vllm-project/vllm/pull/42080)
  [feat] Add FP8 per-tensor Q scale support to Triton attention backend (#42080)
  _Files: `tests/kernels/attention/test_triton_unified_attention.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/ops/triton_unified_attention.py`_
- **2026-05-19** [`d740e2c029`](https://github.com/vllm-project/vllm/commit/d740e2c029) [#43043](https://github.com/vllm-project/vllm/pull/43043)
  [XPU] update xpu graph usage (#43043)
  _Files: `vllm/distributed/device_communicators/xpu_communicator.py`, `vllm/distributed/parallel_state.py`, `vllm/platforms/xpu.py`, `vllm/v1/attention/backends/flash_attn.py`_
- **2026-05-19** [`ef54a4d604`](https://github.com/vllm-project/vllm/commit/ef54a4d604) [#43046](https://github.com/vllm-project/vllm/pull/43046)
  [Misc][MM] Remove redundant code in CLIPAttention (#43046)
  _Files: `vllm/model_executor/models/clip.py`_
- **2026-05-19** [`3ca8db2ef8`](https://github.com/vllm-project/vllm/commit/3ca8db2ef8) [#42899](https://github.com/vllm-project/vllm/pull/42899)
  add cutedsl dsv4 indexer fp8 kernel (#42899)
  _Files: `tests/kernels/test_fused_indexer_q_rope_quant.py`, `vllm/v1/attention/ops/deepseek_v4_ops/cutedsl_utils.py`, `vllm/v1/attention/ops/deepseek_v4_ops/fused_indexer_q.py`, `vllm/v1/attention/ops/deepseek_v4_ops/fused_indexer_q_cutedsl.py`_
- **2026-05-19** [`da03e549b3`](https://github.com/vllm-project/vllm/commit/da03e549b3) [#42537](https://github.com/vllm-project/vllm/pull/42537)
  [UX] Add a persistent cache for FlashInfer autotuning (#42537)
  _Files: `docs/usage/security.md`, `tests/model_executor/test_flashinfer_autotune_cache.py`, `vllm/envs.py`, `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-05-18** [`37ece593c1`](https://github.com/vllm-project/vllm/commit/37ece593c1) [#42774](https://github.com/vllm-project/vllm/pull/42774)
  [Perf] Padded nvfp4 quant kernel to remove additional copy, 2.4%~5.7% e2e performance improvement (#42774)
  _Files: `csrc/libtorch_stable/quantization/fp4/nvfp4_quant_kernels.cu`, `tests/kernels/quantization/test_nvfp4_quant.py`, `vllm/_custom_ops.py`, `vllm/model_executor/kernels/linear/nvfp4/cutlass.py` _+1 more__
- **2026-05-18** [`0191354827`](https://github.com/vllm-project/vllm/commit/0191354827) [#42885](https://github.com/vllm-project/vllm/pull/42885)
  [Perf][MLA] Enable FULL cudagraph capture for TRITON_MLA decode (#42885)
  _Files: `vllm/v1/attention/backends/mla/triton_mla.py`_
- **2026-05-18** [`47829b1159`](https://github.com/vllm-project/vllm/commit/47829b1159) [#42430](https://github.com/vllm-project/vllm/pull/42430)
  [Bugfix] mamba: run single-token extends as decodes (#42430)
  _Files: `tests/v1/attention/test_mamba_update_block_table.py`, `tests/v1/attention/utils.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/v1/attention/backends/mamba_attn.py`_
- **2026-05-18** [`737bfa3a43`](https://github.com/vllm-project/vllm/commit/737bfa3a43) [#41233](https://github.com/vllm-project/vllm/pull/41233)
  [Bugfix][Hybrid][NemotronH] Fix mamba_cache_mode=all + speculative decoding crash (#41233)
  _Files: `tests/v1/attention/test_mamba_update_block_table.py`, `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/model_executor/models/config.py` _+6 more__
- **2026-05-18** [`df852ed503`](https://github.com/vllm-project/vllm/commit/df852ed503) [#41710](https://github.com/vllm-project/vllm/pull/41710)
  fix: remove unused norm for dpskv4 (#41710)
  _Files: `vllm/model_executor/layers/deepseek_v4_attention.py`_
- **2026-05-18** [`b4601ad43f`](https://github.com/vllm-project/vllm/commit/b4601ad43f) [#42707](https://github.com/vllm-project/vllm/pull/42707)
  [CPU] Add fused GDN support for AMX CPU platform (#42707)
  _Files: `csrc/cpu/sgl-kernels/conv.cpp`, `csrc/cpu/sgl-kernels/fla.cpp`, `csrc/cpu/torch_bindings.cpp`, `vllm/_custom_ops.py` _+4 more__
- **2026-05-18** [`965d076148`](https://github.com/vllm-project/vllm/commit/965d076148) [#42740](https://github.com/vllm-project/vllm/pull/42740)
  [CPU] Specify required KV cache layout for CPU attention backend (#42740)
  _Files: `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-05-18** [`998714b21b`](https://github.com/vllm-project/vllm/commit/998714b21b) [#42849](https://github.com/vllm-project/vllm/pull/42849)
  [Perf] Add do_not_specialize in fused FP8 RoPE kernel (#42849)
  _Files: `vllm/v1/attention/ops/deepseek_v4_ops/fused_inv_rope_fp8_quant.py`_

## Disaggregation / PD  (18 commits)

- **2026-05-25** [`873758c13a`](https://github.com/vllm-project/vllm/commit/873758c13a) [#43281](https://github.com/vllm-project/vllm/pull/43281)
  [KV Connector] Handle Mooncake finish after preemption (#43281)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/scheduler.py`_
- **2026-05-25** [`81252d4e24`](https://github.com/vllm-project/vllm/commit/81252d4e24) [#42296](https://github.com/vllm-project/vllm/pull/42296)
  [Feat][KVConnector] Support DSV4 in SimpleCPUOffloadBackend (#42296)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/simple_cpu_offload_connector.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-05-24** [`357fddf614`](https://github.com/vllm-project/vllm/commit/357fddf614) [#43142](https://github.com/vllm-project/vllm/pull/43142)
  [kv_offload]: Add DSv4 support (#43142)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py`, `vllm/v1/kv_offload/base.py`_
- **2026-05-24** [`0902d8e62f`](https://github.com/vllm-project/vllm/commit/0902d8e62f) [#43494](https://github.com/vllm-project/vllm/pull/43494)
  [KV Connector] Keep MooncakeStore full hits block-aligned (#43494)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-05-23** [`819c610f9b`](https://github.com/vllm-project/vllm/commit/819c610f9b) [#43392](https://github.com/vllm-project/vllm/pull/43392)
  [Mooncake] Add metrics for MooncakeStoreConnector operations (#43392)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/metrics.py` _+1 more__
- **2026-05-23** [`3cb83c9592`](https://github.com/vllm-project/vllm/commit/3cb83c9592) [#42922](https://github.com/vllm-project/vllm/pull/42922)
  Add `model` to `WeightTransferEngine.__init__` (#42922)
  _Files: `tests/distributed/test_weight_transfer.py`, `vllm/distributed/weight_transfer/__init__.py`, `vllm/distributed/weight_transfer/base.py`, `vllm/distributed/weight_transfer/factory.py` _+3 more__
- **2026-05-22** [`977703aa94`](https://github.com/vllm-project/vllm/commit/977703aa94) [#40733](https://github.com/vllm-project/vllm/pull/40733)
  [RFC][EPLB][#32028] Remove dead torch.accelerator.synchronize() from sync path (#40733)
  _Files: `vllm/distributed/eplb/rebalance_execute.py`_
- **2026-05-22** [`b21f3d56d4`](https://github.com/vllm-project/vllm/commit/b21f3d56d4) [#43371](https://github.com/vllm-project/vllm/pull/43371)
  [KV Connector] MooncakeStore: don't co-queue save with load to avoid double delayed-free (#43371)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`_
- **2026-05-22** [`d3a563501b`](https://github.com/vllm-project/vllm/commit/d3a563501b) [#43110](https://github.com/vllm-project/vllm/pull/43110)
  [EPLB] Change default EPLB communicator (#43110)
  _Files: `vllm/config/parallel.py`, `vllm/distributed/nixl_utils.py`_
- **2026-05-21** [`e26e1f0928`](https://github.com/vllm-project/vllm/commit/e26e1f0928) [#42968](https://github.com/vllm-project/vllm/pull/42968)
  [Feature] Add `--cpu-distributed-timeout-seconds` CLI Option for CPU Process Group Timeout (#42968)
  _Files: `vllm/config/parallel.py`, `vllm/distributed/parallel_state.py`, `vllm/distributed/utils.py`, `vllm/engine/arg_utils.py`_
- **2026-05-20** [`9c78c99995`](https://github.com/vllm-project/vllm/commit/9c78c99995) [#42993](https://github.com/vllm-project/vllm/pull/42993)
  [MISC] Fix symm_mem cap-equal gate; log AR backend selection (#42993)
  _Files: `vllm/distributed/device_communicators/cuda_communicator.py`, `vllm/distributed/device_communicators/symm_mem.py`_
- **2026-05-20** [`40651c0207`](https://github.com/vllm-project/vllm/commit/40651c0207) [#43097](https://github.com/vllm-project/vllm/pull/43097)
  [Docs][PD][NIXL] Bidirectional kv-cache transfer (#43097)
  _Files: `docs/features/nixl_connector_usage.md`_
- **2026-05-20** [`7e4bc2cecb`](https://github.com/vllm-project/vllm/commit/7e4bc2cecb) [#43099](https://github.com/vllm-project/vllm/pull/43099)
  [Docs][PD][NIXL] Lease extension mechanism for blocks on P (#43099)
  _Files: `docs/design/nixl_kv_cache_lease.md`_
- **2026-05-19** [`aed2eb355a`](https://github.com/vllm-project/vllm/commit/aed2eb355a) [#42994](https://github.com/vllm-project/vllm/pull/42994)
  [Docs] Fix MooncakeStoreConnector role in disaggregated example (#42994)
  _Files: `docs/features/mooncake_store_connector_usage.md`_
- **2026-05-19** [`129019f334`](https://github.com/vllm-project/vllm/commit/129019f334) [#42677](https://github.com/vllm-project/vllm/pull/42677)
  [CI] Add MTP + PD disagg test for Qwen3.5 (#42677)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/kv_connector/nixl_integration/config_sweep_spec_decode_test.sh`, `tests/v1/kv_connector/nixl_integration/spec_decode_acceptance_test.sh`, `tests/v1/kv_connector/nixl_integration/test_spec_decode_acceptance.py`_
- **2026-05-19** [`056bc2e166`](https://github.com/vllm-project/vllm/commit/056bc2e166) [#42828](https://github.com/vllm-project/vllm/pull/42828)
  [KVConnector][DSV4] HMA support for Mooncake store connector (#42828)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py` _+6 more__
- **2026-05-19** [`afd7b1dce9`](https://github.com/vllm-project/vllm/commit/afd7b1dce9) [#42926](https://github.com/vllm-project/vllm/pull/42926)
  [Bugfix] Use platform-agnostic device in example_connector load (#42926)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`_
- **2026-05-18** [`e5417657e5`](https://github.com/vllm-project/vllm/commit/e5417657e5) [#42611](https://github.com/vllm-project/vllm/pull/42611)
  [KV Connector][Offloading] Flush all pending jobs on last step (#42611)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_

## Multimodal  (16 commits)

- **2026-05-25** [`3df1c7c43e`](https://github.com/vllm-project/vllm/commit/3df1c7c43e) [#40275](https://github.com/vllm-project/vllm/pull/40275)
  [Docker] Non-root support for vllm-openai; add opt-in vllm-openai-nonroot target (#40275)
  _Files: `.buildkite/image_build/image_build.yaml`, `.pre-commit-config.yaml`, `docker/Dockerfile`, `docker/entrypoints/test_vllm_nonroot_entrypoint.sh` _+3 more__
- **2026-05-23** [`d8b385b7ea`](https://github.com/vllm-project/vllm/commit/d8b385b7ea) [#43414](https://github.com/vllm-project/vllm/pull/43414)
  [Bugfix][Frontend] Fix input_audio parsing when uuid is present  (#43414)
  _Files: `vllm/entrypoints/chat_utils.py`_
- **2026-05-23** [`84e351555a`](https://github.com/vllm-project/vllm/commit/84e351555a) [#43051](https://github.com/vllm-project/vllm/pull/43051)
  [Bugfix] Auto-raise max_num_batched_tokens for prefix-LM multimodal models (#43051)
  _Files: `tests/v1/engine/test_engine_args.py`, `vllm/engine/arg_utils.py`_
- **2026-05-22** [`f0feb15e7f`](https://github.com/vllm-project/vllm/commit/f0feb15e7f) [#41234](https://github.com/vllm-project/vllm/pull/41234)
  [Multimodal] Simplify ViT CUDA graph interfaces (#41234)
  _Files: `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/qwen2_5_vl.py` _+5 more__
- **2026-05-22** [`79ff0ffa98`](https://github.com/vllm-project/vllm/commit/79ff0ffa98) [#43118](https://github.com/vllm-project/vllm/pull/43118)
  [BugFix] wire make_empty_intermediate_tensors on AyaVision and Voxtral (#43118)
  _Files: `vllm/model_executor/models/aya_vision.py`, `vllm/model_executor/models/voxtral.py`_
- **2026-05-22** [`4658bf882b`](https://github.com/vllm-project/vllm/commit/4658bf882b) [#43001](https://github.com/vllm-project/vllm/pull/43001)
  [Bugfix] Clear P0 mm sender cache on sleep/pause to fix mm_hash desync (#43001)
  _Files: `tests/multimodal/test_cache.py`, `vllm/v1/engine/async_llm.py`, `vllm/v1/engine/llm_engine.py`_
- **2026-05-22** [`2380bfc210`](https://github.com/vllm-project/vllm/commit/2380bfc210) [#43393](https://github.com/vllm-project/vllm/pull/43393)
  [Docs] Note image preprocessing difference between qwen_vl_utils and vllm. (#43393)
  _Files: `docs/models/pooling_models/embed.md`, `docs/models/pooling_models/scoring.md`, `docs/models/supported_models.md`_
- **2026-05-22** [`1fe3303983`](https://github.com/vllm-project/vllm/commit/1fe3303983) [#43064](https://github.com/vllm-project/vllm/pull/43064)
  [CI] De-flake renderers/test_hf.py::test_resolve_content_format_fallbacks[Qwen/Qwen-VL-string] (#43064)
  _Files: `tests/models/multimodal/conftest.py`, `tests/models/multimodal/processing/test_common.py`, `tests/renderers/conftest.py`, `tests/tokenizers_/conftest.py` _+1 more__
- **2026-05-21** [`5ecd8e9c70`](https://github.com/vllm-project/vllm/commit/5ecd8e9c70) [#43266](https://github.com/vllm-project/vllm/pull/43266)
  [XPU][CI]Fix Docker image pull-to-run race in Intel GPU CI (#43266)
  _Files: `.buildkite/scripts/hardware_ci/run-intel-test.sh`_
- **2026-05-21** [`7e5070934e`](https://github.com/vllm-project/vllm/commit/7e5070934e) [#43082](https://github.com/vllm-project/vllm/pull/43082)
  [CI] Fix "test_vit_cudagraph_[image|video][step3_vl]" failure (#43082)
  _Files: `tests/models/multimodal/generation/test_vit_cudagraph.py`_
- **2026-05-21** [`2b75a73b8e`](https://github.com/vllm-project/vllm/commit/2b75a73b8e) [#43169](https://github.com/vllm-project/vllm/pull/43169)
  [Perf][Gemma4] Batch vision encoder calls for image and video processing (#43169)
  _Files: `vllm/model_executor/models/gemma4_mm.py`_
- **2026-05-19** [`1c6158083a`](https://github.com/vllm-project/vllm/commit/1c6158083a) [#42654](https://github.com/vllm-project/vllm/pull/42654)
  [Model] Openvla support (#42654)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_openvla.py`, `tests/models/registry.py` _+7 more__
- **2026-05-19** [`9fd8487d2f`](https://github.com/vllm-project/vllm/commit/9fd8487d2f) [#42626](https://github.com/vllm-project/vllm/pull/42626)
  [Docs] Add SVG images for pooling models. (#42626)
  _Files: `docs/assets/models/pooling_models/cheat_sheet.svg`, `docs/assets/models/pooling_models/pooling_types.svg`, `docs/assets/models/pooling_models/score_types.svg`, `docs/models/pooling_models/README.md` _+1 more__
- **2026-05-19** [`6e889b582b`](https://github.com/vllm-project/vllm/commit/6e889b582b) [#43030](https://github.com/vllm-project/vllm/pull/43030)
  [ci] Route 28 gpu_1_queue tests to h200_35gb queue (#43030)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/lora.yaml` _+8 more__
- **2026-05-18** [`9758a6e5c5`](https://github.com/vllm-project/vllm/commit/9758a6e5c5) [#42819](https://github.com/vllm-project/vllm/pull/42819)
  [BugFix] support PP for Cohere vision model (#42819)
  _Files: `vllm/model_executor/models/cohere2_vision.py`_
- **2026-05-18** [`990f49bdcb`](https://github.com/vllm-project/vllm/commit/990f49bdcb) [#42224](https://github.com/vllm-project/vllm/pull/42224)
  [MM][CG] Enable encoder Cudagraph for Step3VL (#42224)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/interfaces.py` _+4 more__

## Quantization  (16 commits)

- **2026-05-23** [`33d7cbe02c`](https://github.com/vllm-project/vllm/commit/33d7cbe02c) [#43233](https://github.com/vllm-project/vllm/pull/43233)
  [Model Runner v2] Force v1 runner for tests (#43233)
  _Files: `tests/compile/correctness_e2e/test_async_tp.py`, `tests/compile/correctness_e2e/test_sequence_parallel.py`, `tests/compile/fullgraph/test_basic_correctness.py`, `tests/distributed/test_pipeline_parallel.py` _+2 more__
- **2026-05-23** [`10d264a2b9`](https://github.com/vllm-project/vllm/commit/10d264a2b9) [#43492](https://github.com/vllm-project/vllm/pull/43492)
  Revert "[Misc] add humming to dependencies" (#43492)
  _Files: `requirements/cuda.txt`, `setup.py`, `vllm/model_executor/layers/quantization/humming.py`_
- **2026-05-23** [`5bb8d2767a`](https://github.com/vllm-project/vllm/commit/5bb8d2767a) [#39912](https://github.com/vllm-project/vllm/pull/39912)
  [Kernel] Batch invariant NVFP4 linear using cutlass (#39912)
  _Files: `.buildkite/test_areas/misc.yaml`, `csrc/libtorch_stable/quantization/fp4/nvfp4_scaled_mm_kernels.cu`, `csrc/libtorch_stable/quantization/fp4/nvfp4_scaled_mm_sm120_kernels.cu`, `tests/v1/determinism/test_nvfp4_batch_invariant_scaled_mm.py` _+1 more__
- **2026-05-23** [`09a219c075`](https://github.com/vllm-project/vllm/commit/09a219c075) [#42546](https://github.com/vllm-project/vllm/pull/42546)
  [ModelOpt] Support Qwen3.5/3.6 VLM quantized prefix mapping (#42546)
  _Files: `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-05-23** [`a7be0f342d`](https://github.com/vllm-project/vllm/commit/a7be0f342d) [#43209](https://github.com/vllm-project/vllm/pull/43209)
  [7/n] Migrate pos_encoding and norm kernels to libtorch stable ABI (continued) (#43209)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/dispatch_utils.h`, `csrc/libtorch_stable/fused_qknorm_rope_kernel.cu`, `csrc/libtorch_stable/layernorm_kernels.cu` _+11 more__
- **2026-05-23** [`a5bbd81e2e`](https://github.com/vllm-project/vllm/commit/a5bbd81e2e) [#42952](https://github.com/vllm-project/vllm/pull/42952)
  [XPU]feat: enable FP8 block-scaled quantization on XPU (#42952)
  _Files: `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/triton.py`, `vllm/model_executor/layers/quantization/input_quant_fp8.py`, `vllm/model_executor/layers/quantization/utils/fp8_utils.py`_
- **2026-05-22** [`4e597b7491`](https://github.com/vllm-project/vllm/commit/4e597b7491) [#36854](https://github.com/vllm-project/vllm/pull/36854)
  [Bugfix] Clear error message for FP8 torchao quantization on unsupported GPUs (#36854)
  _Files: `vllm/model_executor/layers/quantization/torchao.py`_
- **2026-05-21** [`68e07d5916`](https://github.com/vllm-project/vllm/commit/68e07d5916) [#43261](https://github.com/vllm-project/vllm/pull/43261)
  [Bug] Fix ci issue `assert output_size is not None` AssertionError (#43261)
  _Files: `tests/kernels/quantization/test_cutlass_scaled_mm.py`, `tests/quantization/test_fp8.py`, `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`, `vllm/model_executor/layers/quantization/fp8.py` _+1 more__
- **2026-05-20** [`53ff50fcd3`](https://github.com/vllm-project/vllm/commit/53ff50fcd3) [#42651](https://github.com/vllm-project/vllm/pull/42651)
  [Perf] Optimize `CutlassFP8ScaledMMLinearKernel` when padding needed by pre-weight processing, 13.5% TTFT improvement (#42651)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`_
- **2026-05-20** [`644b2a28e7`](https://github.com/vllm-project/vllm/commit/644b2a28e7) [#41215](https://github.com/vllm-project/vllm/pull/41215)
  [Bugfix] Use enable_sm120_family for per-tensor FP8 CUTLASS kernels on SM12.1 (#41215)
- **2026-05-20** [`df84fb07a6`](https://github.com/vllm-project/vllm/commit/df84fb07a6) [#43144](https://github.com/vllm-project/vllm/pull/43144)
  Remove additional dead code as a follow-up to #42889 (#43144)
  _Files: `tests/quantization/test_compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`_
- **2026-05-19** [`8200fbe1ac`](https://github.com/vllm-project/vllm/commit/8200fbe1ac) [#42540](https://github.com/vllm-project/vllm/pull/42540)
  [Misc] add humming to dependencies (#42540)
  _Files: `requirements/cuda.txt`, `setup.py`, `vllm/model_executor/layers/quantization/humming.py`_
- **2026-05-19** [`36dcaf25d8`](https://github.com/vllm-project/vllm/commit/36dcaf25d8) [#37844](https://github.com/vllm-project/vllm/pull/37844)
  [XPU] add gptq(int4) support (#37844)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `vllm/model_executor/kernels/linear/mixed_precision/MPLinearKernel.py`, `vllm/model_executor/kernels/linear/mixed_precision/xpu.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils.py`_
- **2026-05-18** [`cd49a05d5a`](https://github.com/vllm-project/vllm/commit/cd49a05d5a) [#42889](https://github.com/vllm-project/vllm/pull/42889)
  [Refactor] Remove dead code (#42889)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/__init__.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_24.py`, `vllm/model_executor/layers/quantization/schema.py` _+1 more__
- **2026-05-18** [`ce88f01c9a`](https://github.com/vllm-project/vllm/commit/ce88f01c9a) [#41666](https://github.com/vllm-project/vllm/pull/41666)
  [Docs] update attribution to reflect EDEN foundation (#41666)
  _Files: `vllm/model_executor/layers/quantization/turboquant/__init__.py`, `vllm/model_executor/layers/quantization/turboquant/config.py`_
- **2026-05-18** [`23c15acd77`](https://github.com/vllm-project/vllm/commit/23c15acd77) [#42869](https://github.com/vllm-project/vllm/pull/42869)
  [BugFix] Kimi-K2.5: skip vision tower dtype conversion when using quantization (#42869)
  _Files: `vllm/model_executor/models/kimi_k25.py`_

## CI / Build  (16 commits)

- **2026-05-22** [`65b7a812a2`](https://github.com/vllm-project/vllm/commit/65b7a812a2) [#43225](https://github.com/vllm-project/vllm/pull/43225)
  [CPU] Experimentally enable Triton and MRV2 (#43225)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `docker/Dockerfile.cpu`, `setup.py`, `vllm/platforms/cpu.py` _+7 more__
- **2026-05-22** [`a761697717`](https://github.com/vllm-project/vllm/commit/a761697717) [#43360](https://github.com/vllm-project/vllm/pull/43360)
  Fix the docker build failure in tpu-inference (#43360)
  _Files: `requirements/tpu.txt`_
- **2026-05-22** [`ba369b7eb5`](https://github.com/vllm-project/vllm/commit/ba369b7eb5) [#43378](https://github.com/vllm-project/vllm/pull/43378)
  [CI] Fix dockerfile dependency graph failure for pre-commit (#43378)
  _Files: `docs/assets/contributing/dockerfile-stages-dependency.png`_
- **2026-05-21** [`0b59fc45dd`](https://github.com/vllm-project/vllm/commit/0b59fc45dd) [#43038](https://github.com/vllm-project/vllm/pull/43038)
  Disable build isolation to bypass CUDA related deps for vllm-tpu (#43038)
  _Files: `requirements/build/tpu.txt`, `tools/vllm-tpu/build.sh`_
- **2026-05-21** [`9b9d5dbaab`](https://github.com/vllm-project/vllm/commit/9b9d5dbaab) [#43311](https://github.com/vllm-project/vllm/pull/43311)
  [CI] Fix CPU tests failing on `tl.exp2` import (#43311)
  _Files: `vllm/triton_utils/importing.py`_
- **2026-05-21** [`0a54df2847`](https://github.com/vllm-project/vllm/commit/0a54df2847) [#43287](https://github.com/vllm-project/vllm/pull/43287)
  [XPU] add setuptools-rust for xpu dependency (#43287)
  _Files: `requirements/xpu.txt`_
- **2026-05-21** [`a950e9447e`](https://github.com/vllm-project/vllm/commit/a950e9447e) [#43197](https://github.com/vllm-project/vllm/pull/43197)
  [CI] De-flake test_models for bigscience/bloom-560m (#43197)
  _Files: `vllm/transformers_utils/config.py`_
- **2026-05-21** [`5d041cc1fe`](https://github.com/vllm-project/vllm/commit/5d041cc1fe) [#43262](https://github.com/vllm-project/vllm/pull/43262)
  update GPU json file based on h200 recipes (#43262)
  _Files: `.buildkite/performance-benchmarks/tests/serving-tests.json`_
- **2026-05-20** [`6dc0a71843`](https://github.com/vllm-project/vllm/commit/6dc0a71843) [#43230](https://github.com/vllm-project/vllm/pull/43230)
  [Misc] downgrade nvidia-cutlass-dsl to 4.5.0 (#43230)
  _Files: `requirements/cuda.txt`_
- **2026-05-20** [`f2d5e3d3ae`](https://github.com/vllm-project/vllm/commit/f2d5e3d3ae) [#43186](https://github.com/vllm-project/vllm/pull/43186)
  [CI] Lower granite-4.0-h-tiny gsm8k threshold for Hybrid SSM NixlConnector PD accuracy tests (4 GPUs) (#43186)
  _Files: `tests/v1/kv_connector/nixl_integration/test_accuracy.py`_
- **2026-05-20** [`6f21558da1`](https://github.com/vllm-project/vllm/commit/6f21558da1) [#42499](https://github.com/vllm-project/vllm/pull/42499)
  [XPU][CI] Add 2 server model test files in Intel GPU CI (#42499)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`_
- **2026-05-20** [`85959567c3`](https://github.com/vllm-project/vllm/commit/85959567c3) [#43188](https://github.com/vllm-project/vllm/pull/43188)
  [ci] Revert model executor test back to L4 (#43188)
  _Files: `.buildkite/test_areas/model_executor.yaml`_
- **2026-05-19** [`a65093c1a3`](https://github.com/vllm-project/vllm/commit/a65093c1a3) [#43129](https://github.com/vllm-project/vllm/pull/43129)
  [ci] Move language models tests (hybrid) back to L4 (#43129)
  _Files: `.buildkite/test_areas/models_language.yaml`_
- **2026-05-18** [`f85c76d701`](https://github.com/vllm-project/vllm/commit/f85c76d701) [#42991](https://github.com/vllm-project/vllm/pull/42991)
  [CI/Build] Bump nvidia-cutlass-dsl to 4.5.1 (#42991)
  _Files: `requirements/cuda.txt`_
- **2026-05-18** [`c38bed4248`](https://github.com/vllm-project/vllm/commit/c38bed4248) [#42582](https://github.com/vllm-project/vllm/pull/42582)
  delete xpu ci (#42582)
  _Files: `.buildkite/hardware_tests/intel.yaml`, `.buildkite/scripts/hardware_ci/run-xpu-test.sh`_
- **2026-05-18** [`107210442d`](https://github.com/vllm-project/vllm/commit/107210442d) [#42567](https://github.com/vllm-project/vllm/pull/42567)
  [CI] Add NIXL EP import canary (#42567)
  _Files: `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/test_nixl_imports.py`_

## Models  (14 commits)

- **2026-05-25** [`5c1aec3dc0`](https://github.com/vllm-project/vllm/commit/5c1aec3dc0) [#42933](https://github.com/vllm-project/vllm/pull/42933)
  Reduce memory usage for granite_speech. (#42933)
  _Files: `vllm/model_executor/models/granite_speech.py`_
- **2026-05-25** [`b06813e872`](https://github.com/vllm-project/vllm/commit/b06813e872) [#43474](https://github.com/vllm-project/vllm/pull/43474)
  [Kernel] Add mhc_pre_big_fuse_with_norm_tilelang  (#43474)
  _Files: `vllm/_tilelang_ops.py`, `vllm/model_executor/kernels/mhc/tilelang.py`, `vllm/model_executor/layers/mhc.py`, `vllm/models/deepseek_v4/nvidia/model.py` _+1 more__
- **2026-05-22** [`f743254143`](https://github.com/vllm-project/vllm/commit/f743254143) [#42353](https://github.com/vllm-project/vllm/pull/42353)
  DSv4 fused Q-norm kernel grid refactor (#42353)
  _Files: `csrc/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`_
- **2026-05-22** [`fa1ff88b31`](https://github.com/vllm-project/vllm/commit/fa1ff88b31) [#43213](https://github.com/vllm-project/vllm/pull/43213)
  [Model] Fix MiniCPM-V 4.6 vit_merger qkv weight loading (#43213)
  _Files: `vllm/model_executor/models/minicpmv4_6.py`_
- **2026-05-22** [`e746a2eebf`](https://github.com/vllm-project/vllm/commit/e746a2eebf) [#42972](https://github.com/vllm-project/vllm/pull/42972)
  [Model] Use `AutoWeightsLoader` for Voyage (#42972)
  _Files: `vllm/model_executor/models/voyage.py`_
- **2026-05-21** [`d97ba29fdc`](https://github.com/vllm-project/vllm/commit/d97ba29fdc) [#37831](https://github.com/vllm-project/vllm/pull/37831)
  [ToolParser][Bugfix] Re-land: Fix anyOf/oneOf/$ref type resolution in Qwen3CoderToolParser (#37831) (#38973)
  _Files: `tests/tool_parsers/test_qwen3coder_tool_parser.py`, `vllm/tool_parsers/qwen3coder_tool_parser.py`_
- **2026-05-21** [`e45df8c3f7`](https://github.com/vllm-project/vllm/commit/e45df8c3f7) [#36329](https://github.com/vllm-project/vllm/pull/36329)
  [Bugfix] Fix Qwen3.5 GatedDeltaNet in_proj_ba Marlin failure at TP>=2 (#36329)
  _Files: `vllm/model_executor/layers/mamba/gdn_linear_attn.py`_
- **2026-05-21** [`63ea11709b`](https://github.com/vllm-project/vllm/commit/63ea11709b) [#43255](https://github.com/vllm-project/vllm/pull/43255)
  [CI] Add composed-schema regression tests for DeepSeek V3.2/V4 parsers (#43255)
  _Files: `tests/tool_parsers/test_deepseekv32_tool_parser.py`, `tests/tool_parsers/test_deepseekv4_tool_parser.py`_
- **2026-05-20** [`a10d69116c`](https://github.com/vllm-project/vllm/commit/a10d69116c) [#43019](https://github.com/vllm-project/vllm/pull/43019)
  [Bugfix] Use shared coerce_to_schema_type in DeepSeekV32 tool parser (#43019)
  _Files: `tests/tool_parsers/test_deepseekv32_tool_parser.py`, `vllm/tool_parsers/deepseekv32_tool_parser.py`_
- **2026-05-20** [`0a508743d4`](https://github.com/vllm-project/vllm/commit/0a508743d4) [#43130](https://github.com/vllm-project/vllm/pull/43130)
  [Spec Decode] Support non-MTP speculation for NemotronH (#43130)
  _Files: `vllm/model_executor/models/nemotron_h.py`_
- **2026-05-19** [`117afeea46`](https://github.com/vllm-project/vllm/commit/117afeea46) [#41277](https://github.com/vllm-project/vllm/pull/41277)
  Fix error in Dynamic NTK scaling (#41277)
  _Files: `tests/models/language/pooling/test_nomic_max_model_len.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/dynamic_ntk_scaling_rope.py`, `vllm/model_executor/models/config.py`_
- **2026-05-18** [`4a39b4f553`](https://github.com/vllm-project/vllm/commit/4a39b4f553) [#41154](https://github.com/vllm-project/vllm/pull/41154)
  [Model] Add Apertus Tool Parser (#41154)
  _Files: `docs/features/tool_calling.md`, `examples/tool_chat_template_apertus.jinja`, `tests/tool_parsers/test_apertus_tool_parser.py`, `vllm/tool_parsers/__init__.py` _+1 more__
- **2026-05-18** [`9537542537`](https://github.com/vllm-project/vllm/commit/9537542537) [#42923](https://github.com/vllm-project/vllm/pull/42923)
  Revert checkpoint specific workaround in Transformers modelling backend (#42923)
  _Files: `vllm/model_executor/models/transformers/base.py`_
- **2026-05-18** [`5ab6d1b3fd`](https://github.com/vllm-project/vllm/commit/5ab6d1b3fd) [#42311](https://github.com/vllm-project/vllm/pull/42311)
  [Model] [Perf] Use flatten for Qwen3.5's GDN output projection (#42311)
  _Files: `vllm/model_executor/layers/mamba/gdn_linear_attn.py`_

## Docs  (8 commits)

- **2026-05-25** [`0c942c69d6`](https://github.com/vllm-project/vllm/commit/0c942c69d6) [#43568](https://github.com/vllm-project/vllm/pull/43568)
  [Doc] Add section on escalating stalled contributions (#43568)
  _Files: `docs/contributing/README.md`_
- **2026-05-25** [`1b26fa361e`](https://github.com/vllm-project/vllm/commit/1b26fa361e) [#43552](https://github.com/vllm-project/vllm/pull/43552)
  [Docs] Reorganize offline inference docs.  (#43552)
  _Files: `docs/serving/offline_inference.md`_
- **2026-05-23** [`8737e4a857`](https://github.com/vllm-project/vllm/commit/8737e4a857) [#43489](https://github.com/vllm-project/vllm/pull/43489)
  [Docs] Fix stale version number in token_classify.md (#43489)
  _Files: `docs/models/pooling_models/token_classify.md`_
- **2026-05-23** [`7c2ff1f819`](https://github.com/vllm-project/vllm/commit/7c2ff1f819) [#43488](https://github.com/vllm-project/vllm/pull/43488)
  [Docs] Fix stale version number in token_embed.md (#43488)
  _Files: `docs/models/pooling_models/token_embed.md`_
- **2026-05-21** [`0f66623b0d`](https://github.com/vllm-project/vllm/commit/0f66623b0d) [#43168](https://github.com/vllm-project/vllm/pull/43168)
  [Frontend] Rework fastokens integration (#43168)
  _Files: `docs/configuration/optimization.md`, `docs/design/huggingface_integration.md`, `vllm/config/model.py`, `vllm/envs.py` _+3 more__
- **2026-05-20** [`87e31455b0`](https://github.com/vllm-project/vllm/commit/87e31455b0) [#40326](https://github.com/vllm-project/vllm/pull/40326)
  [Doc] Sync CLI guide with actual help modes and launch subcommand (#40326)
  _Files: `docs/cli/.nav.yml`, `docs/cli/README.md`, `docs/cli/launch/render.md`, `docs/mkdocs/hooks/generate_argparse.py`_
- **2026-05-19** [`be16785998`](https://github.com/vllm-project/vllm/commit/be16785998) [#43115](https://github.com/vllm-project/vllm/pull/43115)
  [CPU][DOC] Fix installation commands for Arm CPUs (#43115)
  _Files: `docs/getting_started/installation/cpu.arm.inc.md`_
- **2026-05-18** [`c1f7854342`](https://github.com/vllm-project/vllm/commit/c1f7854342) [#42929](https://github.com/vllm-project/vllm/pull/42929)
  Improve logging when docs build is skipped (#42929)
  _Files: `.readthedocs.yaml`, `docs/pre_run_check.sh`_

## Scheduler / Engine  (8 commits)

- **2026-05-23** [`82536acc54`](https://github.com/vllm-project/vllm/commit/82536acc54) [#43433](https://github.com/vllm-project/vllm/pull/43433)
  Keep scheduler alive for delayed KV connector frees (#43433)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/engine/core.py`_
- **2026-05-22** [`91f5b92438`](https://github.com/vllm-project/vllm/commit/91f5b92438) [#43405](https://github.com/vllm-project/vllm/pull/43405)
  [Rust Frontend] [Refactor] Extract a newtype for utility call ID (#43405)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/client/state.rs`, `rust/src/engine-core-client/src/error.rs` _+5 more__
- **2026-05-22** [`0ddd7dd656`](https://github.com/vllm-project/vllm/commit/0ddd7dd656) [#40841](https://github.com/vllm-project/vllm/pull/40841)
  [Frontend] DP Supervisor (#40841)
  _Files: `tests/entrypoints/openai/test_dp_supervisor.py`, `vllm/engine/arg_utils.py`, `vllm/entrypoints/cli/serve.py`, `vllm/entrypoints/openai/api_server.py` _+3 more__
- **2026-05-20** [`19cf334207`](https://github.com/vllm-project/vllm/commit/19cf334207) [#33648](https://github.com/vllm-project/vllm/pull/33648)
  [Feature] Support manually enabling the cumem allocator (#33648)
  _Files: `docs/features/nixl_connector_usage.md`, `tests/v1/kv_connector/unit/test_config.py`, `vllm/config/model.py`, `vllm/config/vllm.py` _+2 more__
- **2026-05-19** [`f34623bf3c`](https://github.com/vllm-project/vllm/commit/f34623bf3c) [#42117](https://github.com/vllm-project/vllm/pull/42117)
  [bug] AsyncScheduler drops first post-resume token after pause_generation + clear_cache (#42117)
  _Files: `examples/rl/rlhf_async_new_apis.py`, `vllm/v1/core/sched/async_scheduler.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/request.py`_
- **2026-05-19** [`257af77bc2`](https://github.com/vllm-project/vllm/commit/257af77bc2) [#41907](https://github.com/vllm-project/vllm/pull/41907)
  [Docs] Reorganize online serving docs. (#41907)
  _Files: `docs/.nav.yml`, `docs/assets/models/pooling_models/cheat_sheet.svg`, `docs/configuration/README.md`, `docs/configuration/engine_args.md` _+20 more__
- **2026-05-19** [`fab07e4d0f`](https://github.com/vllm-project/vllm/commit/fab07e4d0f) [#42289](https://github.com/vllm-project/vllm/pull/42289)
  [Bugfix][KV Connector] Fix SimpleCPUOffloadScheduler TOCTOU between Phase A and Phase B (#42289)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-05-19** [`239b5ff30c`](https://github.com/vllm-project/vllm/commit/239b5ff30c) [#42476](https://github.com/vllm-project/vllm/pull/42476)
  [Frontend] Add --spec-method/--spec-model/--spec-tokens CLI aliases (#42476)
  _Files: `vllm/engine/arg_utils.py`, `vllm/entrypoints/llm.py`_

## Serving / API  (8 commits)

- **2026-05-22** [`2b94d1c0ca`](https://github.com/vllm-project/vllm/commit/2b94d1c0ca) [#43426](https://github.com/vllm-project/vllm/pull/43426)
  [Frontend] Simplify AuthenticationMiddleware path extraction (#43426)
  _Files: `vllm/entrypoints/openai/server_utils.py`_
- **2026-05-22** [`60af5c16ee`](https://github.com/vllm-project/vllm/commit/60af5c16ee) [#43260](https://github.com/vllm-project/vllm/pull/43260)
  [Frontend] Add truncation side to OpenAI endpoints (#43260)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/completion/test_completion.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py` _+1 more__
- **2026-05-21** [`a6682d1d25`](https://github.com/vllm-project/vllm/commit/a6682d1d25) [#42905](https://github.com/vllm-project/vllm/pull/42905)
  [Bugfix] Warn when renderer_num_workers has no effect on offline LLM (#42905)
  _Files: `vllm/config/model.py`, `vllm/entrypoints/llm.py`_
- **2026-05-21** [`346cf163a1`](https://github.com/vllm-project/vllm/commit/346cf163a1) [#42664](https://github.com/vllm-project/vllm/pull/42664)
  [Frontend] Normalize reasoning_content to reasoning for client compatibility (#42664)
  _Files: `tests/tool_use/test_chat_completion_request_validations.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`_
- **2026-05-20** [`2d6b3489b9`](https://github.com/vllm-project/vllm/commit/2d6b3489b9) [#38939](https://github.com/vllm-project/vllm/pull/38939)
  [R3] Add routed experts to openai entrypoint  (#38939)
  _Files: `tests/entrypoints/openai/test_return_routed_experts.py`, `tests/entrypoints/serve/disagg/test_return_routed_experts.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/chat_completion/serving.py` _+2 more__
- **2026-05-20** [`cb600d1cdb`](https://github.com/vllm-project/vllm/commit/cb600d1cdb) [#42330](https://github.com/vllm-project/vllm/pull/42330)
  [Frontend] Forward X-data-parallel-rank header on /inference/v1/generate (#42330)
  _Files: `vllm/entrypoints/serve/disagg/serving.py`_
- **2026-05-20** [`fadf5d332c`](https://github.com/vllm-project/vllm/commit/fadf5d332c) [#42975](https://github.com/vllm-project/vllm/pull/42975)
  add enqueue all option to throughput benchmark (#42975)
  _Files: `tests/entrypoints/llm/test_mm_processor_kwargs.py`, `vllm/benchmarks/throughput.py`, `vllm/entrypoints/llm.py`_
- **2026-05-19** [`a78b842d0e`](https://github.com/vllm-project/vllm/commit/a78b842d0e) [#42887](https://github.com/vllm-project/vllm/pull/42887)
  [Bugfix] Fix top logprobs token placeholders in `/inference/v1/generate` (#42887)
  _Files: `tests/entrypoints/serve/disagg/test_tokens_logprobs.py`, `vllm/entrypoints/serve/disagg/serving.py`_

## KV Cache / Offload  (5 commits)

- **2026-05-22** [`47d4407d7c`](https://github.com/vllm-project/vllm/commit/47d4407d7c) [#35045](https://github.com/vllm-project/vllm/pull/35045)
  [Model Runner V2] Support sharing kv cache layers (#35045)
  _Files: `vllm/config/vllm.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/utils.py`_
- **2026-05-21** [`b719b1635b`](https://github.com/vllm-project/vllm/commit/b719b1635b) [#43195](https://github.com/vllm-project/vllm/pull/43195)
  Update KDA chunk prefill decay to use exp2 semantics (#43195)
  _Files: `vllm/model_executor/layers/fla/ops/chunk_delta_h.py`, `vllm/model_executor/layers/fla/ops/kda.py`, `vllm/model_executor/layers/fla/ops/op.py`_
- **2026-05-20** [`4f940896a3`](https://github.com/vllm-project/vllm/commit/4f940896a3) [#43076](https://github.com/vllm-project/vllm/pull/43076)
  [KV Offload] Pass `OffloadingSpec` instead of `VllmConfig` to secondary tiers (#43076)
  _Files: `tests/v1/kv_offload/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/base.py`, `vllm/v1/kv_offload/tiering/example/manager.py`, `vllm/v1/kv_offload/tiering/factory.py` _+1 more__
- **2026-05-19** [`fba010dd74`](https://github.com/vllm-project/vllm/commit/fba010dd74) [#42766](https://github.com/vllm-project/vllm/pull/42766)
  [Bugfix][MRV2] Fix KVCache tensor explicit `kernel_block_size` dim (#42766)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/block_table.py` _+2 more__
- **2026-05-18** [`e414e1f1c0`](https://github.com/vllm-project/vllm/commit/e414e1f1c0) [#42945](https://github.com/vllm-project/vllm/pull/42945)
  [Bugfix][KV Offload] count appended GPU blocks in store group_sizes (#42945)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_

## Perf / Benchmark  (4 commits)

- **2026-05-24** [`d56285c747`](https://github.com/vllm-project/vllm/commit/d56285c747) [#43083](https://github.com/vllm-project/vllm/pull/43083)
  Tuning script and configs for Triton Mamba SSU kernel (#43083)
  _Files: `benchmarks/kernels/benchmark_selective_state_update.py`, `tests/kernels/mamba/__init__.py`, `tests/kernels/mamba/test_mamba_ssm.py`, `tests/kernels/mamba/test_mamba_ssm_configs.py` _+9 more__
- **2026-05-21** [`b730c46352`](https://github.com/vllm-project/vllm/commit/b730c46352) [#40172](https://github.com/vllm-project/vllm/pull/40172)
  [Perf] [Hybrid] Fused Triton kernel for GPU-side Mamba state postprocessing (#40172)
  _Files: `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `tests/v1/worker/test_mamba_utils.py`, `vllm/v1/worker/gpu_model_runner.py`, `vllm/v1/worker/mamba_utils.py`_
- **2026-05-21** [`905b97adfa`](https://github.com/vllm-project/vllm/commit/905b97adfa) [#43245](https://github.com/vllm-project/vllm/pull/43245)
  [Benchmark] Add num-warmup to vllm bench throughput (#43245)
  _Files: `vllm/benchmarks/throughput.py`_
- **2026-05-20** [`2ae910ed88`](https://github.com/vllm-project/vllm/commit/2ae910ed88) [#42938](https://github.com/vllm-project/vllm/pull/42938)
  [Perf] Avoid forward scan for async output placeholders (#42938)
  _Files: `vllm/v1/worker/gpu_input_batch.py`_

## Speculative Decoding  (4 commits)

- **2026-05-23** [`3f3e862681`](https://github.com/vllm-project/vllm/commit/3f3e862681) [#42143](https://github.com/vllm-project/vllm/pull/42143)
  fix(eagle3): read norm_before_fc from eagle_config for NVIDIA checkpoint (#42143)
  _Files: `vllm/model_executor/models/llama_eagle3.py`_
- **2026-05-22** [`4e2eba28be`](https://github.com/vllm-project/vllm/commit/4e2eba28be) [#37374](https://github.com/vllm-project/vllm/pull/37374)
  [Perf] Optimize hidden state extraction logic (#37374)
  _Files: `benchmarks/benchmark_hidden_state_extraction.py`, `docs/features/speculative_decoding/README.md`, `docs/features/speculative_decoding/extract_hidden_states.md`, `examples/features/speculative_decoding/extract_hidden_states_offline.py` _+5 more__
- **2026-05-19** [`1242196295`](https://github.com/vllm-project/vllm/commit/1242196295) [#42764](https://github.com/vllm-project/vllm/pull/42764)
  [Model] Support post-norm architecture for EAGLE-3 supeculators (#42764)
  _Files: `vllm/model_executor/models/deepseek_eagle3.py`, `vllm/model_executor/models/llama_eagle3.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-05-18** [`a171e6b52d`](https://github.com/vllm-project/vllm/commit/a171e6b52d) [#43010](https://github.com/vllm-project/vllm/pull/43010)
  Add parallel drafting to v2 model runner unsupported features (#43010)
  _Files: `vllm/config/vllm.py`_

## LoRA  (3 commits)

- **2026-05-22** [`5ea76fa89a`](https://github.com/vllm-project/vllm/commit/5ea76fa89a) [#43314](https://github.com/vllm-project/vllm/pull/43314)
  [CI] Fix test_lora_with_spec_decode on V2 model runner (#43314)
  _Files: `tests/v1/e2e/spec_decode/test_lora_with_spec_decode.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-05-21** [`9640970de2`](https://github.com/vllm-project/vllm/commit/9640970de2) [#43139](https://github.com/vllm-project/vllm/pull/43139)
  [Model Runner V2] Fix lora `Triton Error [CUDA]: device-side assert triggered` (#43139)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-05-20** [`39bba710be`](https://github.com/vllm-project/vllm/commit/39bba710be) [#43160](https://github.com/vllm-project/vllm/pull/43160)
  [MRV2][BugFix] Fix default-stream CG capture in P/W LoRA case (#43160)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`_

## Compilation / CUDA Graph  (1 commits)

- **2026-05-18** [`1ac10f159a`](https://github.com/vllm-project/vllm/commit/1ac10f159a) [#42686](https://github.com/vllm-project/vllm/pull/42686)
  Revert "[torch.compile] Add patch for fullgraph compilation" (#42686) (#42913)
  _Files: `vllm/env_override.py`_

---
_Generated 2026-05-25 12:02 UTC_