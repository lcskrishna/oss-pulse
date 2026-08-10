# sgl-project/sglang — Weekly Change Report
**Period:** 2026-08-03 → 2026-08-10  |  **Total commits:** 399

## ✨ New Features This Week

- **2026-08-10** [#33639](https://github.com/sgl-project/sglang/pull/33639) — [Hicache][2/2]Support Mamba branching in Unified Radix Cache with HiCache (#33639)
- **2026-08-10** [#30023](https://github.com/sgl-project/sglang/pull/30023) — [tracing] sglang tracing v2: support exporting tracing data asynchronously (#30023)
- **2026-08-10** [#33661](https://github.com/sgl-project/sglang/pull/33661) — [BCG][5/N] MLA Fully Support (#33661)
- **2026-08-10** [#34222](https://github.com/sgl-project/sglang/pull/34222) — [Feature] Support NVFP4 token embedding in ModelOpt mixed-precision checkpoints (#34222)
- **2026-08-10** [#33962](https://github.com/sgl-project/sglang/pull/33962) — enable TRT-LLM for MiniMax M3 by preserving SwiGLU params (#33962)
- **2026-08-10** [#33808](https://github.com/sgl-project/sglang/pull/33808) — [Intel GPU] DeepSeek V4 15/N: Add silu_and_mul_clamp support to triton fused_moe for XPU (#33808)
- **2026-08-10** [#30050](https://github.com/sgl-project/sglang/pull/30050) — [MLX] Support gpt-oss: sliding-window attention, attention sinks, sm_scale (#30050)
- **2026-08-10** [#33630](https://github.com/sgl-project/sglang/pull/33630) — Add kda replayssm tests (#33630)
- **2026-08-09** [#22867](https://github.com/sgl-project/sglang/pull/22867) — [feat] Add language_model_only parameter support for Qwen35 (#22867)
- **2026-08-09** [#34169](https://github.com/sgl-project/sglang/pull/34169) — Add skill for the logprob consistency tests (#34169)
- _…and 72 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-10** [`f2a4c4c847`](https://github.com/sgl-project/sglang/commit/f2a4c4c847) [#31843](https://github.com/sgl-project/sglang/pull/31843) — [AMD] [CI] Enable 3 nested unit tests needing harness stub fixes (#31843)
- **2026-08-09** [`967cac801c`](https://github.com/sgl-project/sglang/commit/967cac801c) [#34147](https://github.com/sgl-project/sglang/pull/34147) — [AMD] [CI] Register the DeepSeek-V4-Pro-DSpark MI35x nightly job so its suite actually runs (#34147)
- **2026-08-08** [`cea16bf229`](https://github.com/sgl-project/sglang/commit/cea16bf229) [#34006](https://github.com/sgl-project/sglang/pull/34006) — Fix Qwen3-MoE producing garbage with the mori a2a backend (#34006)
- **2026-08-08** [`ba7abd4f92`](https://github.com/sgl-project/sglang/commit/ba7abd4f92) [#30964](https://github.com/sgl-project/sglang/pull/30964) — [AMD] Support DeepSeek V4 DSpark on AMD HIP platform (#30964)
- **2026-08-08** [`c4f018ba1d`](https://github.com/sgl-project/sglang/commit/c4f018ba1d) [#31531](https://github.com/sgl-project/sglang/pull/31531) — [Refactor] Separate ROCm-specific DeepSeek MHA and MLA forward paths (#31531)
- **2026-08-08** [`6679d9b60c`](https://github.com/sgl-project/sglang/commit/6679d9b60c) [#33981](https://github.com/sgl-project/sglang/pull/33981) — [AMD] Add K3 verified mla kernel for DSpark on triton backend (#33981)
- **2026-08-07** [`62a28197c0`](https://github.com/sgl-project/sglang/commit/62a28197c0) [#32556](https://github.com/sgl-project/sglang/pull/32556) — Autotune flashinfer extend buckets at warmup (#32556)
- **2026-08-07** [`fc9479243e`](https://github.com/sgl-project/sglang/commit/fc9479243e) [#32120](https://github.com/sgl-project/sglang/pull/32120) — [AMD][DI][CI] 8/N Add GLM-5.2 MXFP4 1P1D DI/CI recipes (base + MTP + DP8/EP8) (#32120)
- **2026-08-06** [`b38caebf09`](https://github.com/sgl-project/sglang/commit/b38caebf09) [#32466](https://github.com/sgl-project/sglang/pull/32466) — [AMD] Enable gfx1250 sgl-kernel builds (#32466)
- **2026-08-06** [`18e6c61c21`](https://github.com/sgl-project/sglang/commit/18e6c61c21) [#29677](https://github.com/sgl-project/sglang/pull/29677) — [AMD] perf: compact Triton extend-attention for ragged prefill (AMD/HIP-only) (#29677)
- **2026-08-06** [`dfe53232d7`](https://github.com/sgl-project/sglang/commit/dfe53232d7) [#33809](https://github.com/sgl-project/sglang/pull/33809) — [AMD] Move test_load_weights_from_remote_instance.py to extra CI (#33809)
- **2026-08-06** [`4cdab7b4f4`](https://github.com/sgl-project/sglang/commit/4cdab7b4f4) [#31899](https://github.com/sgl-project/sglang/pull/31899) — [AMD] Add msgpack to ROCm diffusion deps (fix multimodal-gen unit test ModuleNotFoundError) (#31899)
- **2026-08-06** [`0e584529f5`](https://github.com/sgl-project/sglang/commit/0e584529f5) [#33832](https://github.com/sgl-project/sglang/pull/33832) — [CI] Remove profiling from nightly tests (#33832)
- **2026-08-06** [`c11ce7c514`](https://github.com/sgl-project/sglang/commit/c11ce7c514) [#33842](https://github.com/sgl-project/sglang/pull/33842) — chore: bump sgl-kernel version to 0.4.6.post1 (#33842)
- **2026-08-06** [`cf7923615c`](https://github.com/sgl-project/sglang/commit/cf7923615c) [#33694](https://github.com/sgl-project/sglang/pull/33694) — [AMD] Gate DFLASH non-greedy verify on the target-only kernel being registered (#33694)
- **2026-08-06** [`dea07b348b`](https://github.com/sgl-project/sglang/commit/dea07b348b) [#33825](https://github.com/sgl-project/sglang/pull/33825) — [AMD] Update amd k3 cookbook for fp8 kv cache (#33825)
- **2026-08-06** [`407a65d3cb`](https://github.com/sgl-project/sglang/commit/407a65d3cb) [#33753](https://github.com/sgl-project/sglang/pull/33753) — [AMD] [CI] Track the MI355X disagg nightly in the AMD CI job monitor (#33753)
- **2026-08-06** [`d90ef69802`](https://github.com/sgl-project/sglang/commit/d90ef69802) [#31483](https://github.com/sgl-project/sglang/pull/31483) — [AMD] ci: run vetted nested multimodal_gen unit tests on AMD (#31483)
- **2026-08-06** [`e675c7226a`](https://github.com/sgl-project/sglang/commit/e675c7226a) [#33774](https://github.com/sgl-project/sglang/pull/33774) — [AMD]Stage MI355X nightly by node count (#33774)
- **2026-08-06** [`c952ee5ac1`](https://github.com/sgl-project/sglang/commit/c952ee5ac1) [#33678](https://github.com/sgl-project/sglang/pull/33678) — chore: bump sgl-kernel version to 0.4.6 (#33678)
- **2026-08-05** [`8279702e0b`](https://github.com/sgl-project/sglang/commit/8279702e0b) [#33689](https://github.com/sgl-project/sglang/pull/33689) — [AMD] Stop publishing the K3 MI35X nightly image (#33689)
- **2026-08-05** [`1478cdec9f`](https://github.com/sgl-project/sglang/commit/1478cdec9f) [#33599](https://github.com/sgl-project/sglang/pull/33599) — [AMD] Fuse Kimi-K3 attn-residual aggregation (#33599)
- **2026-08-04** [`b327d76682`](https://github.com/sgl-project/sglang/commit/b327d76682) [#33462](https://github.com/sgl-project/sglang/pull/33462) — [AMD] Bump mori to latest in sglang (#33462)
- **2026-08-04** [`723c277640`](https://github.com/sgl-project/sglang/commit/723c277640) [#33399](https://github.com/sgl-project/sglang/pull/33399) — [AMD] [Fix] Enable aiter hd256 FP8 prefill FMHA on gfx950 (#33399)
- **2026-08-04** [`eaf5c29cc5`](https://github.com/sgl-project/sglang/commit/eaf5c29cc5) [#33402](https://github.com/sgl-project/sglang/pull/33402) — [AMD] Enable block-fp8 + quick INT4 all-reduce in MiniMax-M3 MI35x nightly Test (#33402)
- **2026-08-04** [`48dcadc770`](https://github.com/sgl-project/sglang/commit/48dcadc770) [#31500](https://github.com/sgl-project/sglang/pull/31500) — [AMD][DI][CI] 5/N Add DSV4 wide-EP16 4-node 2P1D nightly recipes (#31500)
- **2026-08-04** [`a84e70eb1e`](https://github.com/sgl-project/sglang/commit/a84e70eb1e) [#33333](https://github.com/sgl-project/sglang/pull/33333) — [AMD][DI][CI] 6/N Add Kimi-K2.6 MXFP4 wide-EP16 2P1D nightly recipes (#33333)
- **2026-08-04** [`03f44c978a`](https://github.com/sgl-project/sglang/commit/03f44c978a) [#33374](https://github.com/sgl-project/sglang/pull/33374) — [AMD][DI][CI] Auto-mount  latest host ionic/ibverbs userspace in the MI355X nightly launcher (fix ABI mismatch) (#33374)
- **2026-08-03** [`92999d84f4`](https://github.com/sgl-project/sglang/commit/92999d84f4) [#32046](https://github.com/sgl-project/sglang/pull/32046) — [AMD]Qwen3.5 integration gfx950 fmha fp8 hd256 (#32046)
- **2026-08-03** [`21d930aae3`](https://github.com/sgl-project/sglang/commit/21d930aae3) [#33195](https://github.com/sgl-project/sglang/pull/33195) — [AMD] Fix JIT compile failure in sgl_kernel/warp.cuh (#33195)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-08-10 |
| [#32432](https://github.com/sgl-project/sglang/issues/32432) | [RFC] Define Metadata, Workspace, and Stream-Ownership Contracts for D | — | 2026-08-10 |
| [#33356](https://github.com/sgl-project/sglang/issues/33356) | [Bug] DSpark large decode CUDA-Graph capture can hit non-deterministic | — | 2026-08-10 |
| [#31023](https://github.com/sgl-project/sglang/issues/31023) | [Bug] DSpark compact target-verify CUDA Graph transition can hit timin | — | 2026-08-10 |
| [#34211](https://github.com/sgl-project/sglang/issues/34211) | [Bug] [NPU] (v0.5.17)Eco-Tech/Qwen3.6-35B-A3B-w8a8 Model Served with f | — | 2026-08-10 |
| [#34227](https://github.com/sgl-project/sglang/issues/34227) | [diffusion] MiniMax-H3 with --use-fsdp-inference produces silently cor | — | 2026-08-10 |
| [#23206](https://github.com/sgl-project/sglang/issues/23206) | [RFC] Sglang non-GPU process rust migration | — | 2026-08-10 |
| [#34120](https://github.com/sgl-project/sglang/issues/34120) | Wide EP for GLM5-2 and kimi-k3 | — | 2026-08-10 |
| [#34205](https://github.com/sgl-project/sglang/issues/34205) | [Bug] Aborted LoRA requests retain a LoRARegistry reference | — | 2026-08-10 |
| [#33642](https://github.com/sgl-project/sglang/issues/33642) | [Bug] All schedulers hang in cuModuleLoadData on first EAGLE verify (D | — | 2026-08-10 |
| [#34149](https://github.com/sgl-project/sglang/issues/34149) | [Bug] Abort can commit a delayed final chunked-prefill token on latest | — | 2026-08-09 |
| [#33636](https://github.com/sgl-project/sglang/issues/33636) | [NVIDIA] DeepSeek V4 Perf Tracking | nvidia | 2026-08-09 |
| [#33522](https://github.com/sgl-project/sglang/issues/33522) | [Roadmap]Fast Engine Recovery: Weight Cache Daemon | — | 2026-08-09 |
| [#32321](https://github.com/sgl-project/sglang/issues/32321) | [RFC] Replace the MLX runner-stub split with one Torch-owned SRT path  | — | 2026-08-09 |
| [#16255](https://github.com/sgl-project/sglang/issues/16255) | [Feature] deepseek_v2.py Refactor | inactive, deepseek, Good Pro Issue | 2026-08-08 |
| [#30781](https://github.com/sgl-project/sglang/issues/30781) | [Bug] sgl-model-gateway router rejects /v1/responses requests with too | — | 2026-08-08 |
| [#29736](https://github.com/sgl-project/sglang/issues/29736) | [Roadmap][DCP] Decode Context Parallelism & Helix Parallelism (2026 Q3 | — | 2026-08-07 |
| [#27252](https://github.com/sgl-project/sglang/issues/27252) | [Roadmap]Prefill Context Parallel Refactor | — | 2026-08-07 |
| [#34003](https://github.com/sgl-project/sglang/issues/34003) | [Bug] [NPU] Qwen3.5 model does not work in dynamic CPP scenario with r | — | 2026-08-07 |
| [#33978](https://github.com/sgl-project/sglang/issues/33978) | [Bug] | — | 2026-08-07 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 103 |
| Multimodal | 77 |
| Prefill / Decode Disaggregation | 27 |
| MoE / Expert Parallel | 26 |
| Other | 24 |
| Scheduler / Batching | 23 |
| Triton / Kernels | 21 |
| KV Cache / Memory | 19 |
| CI / Build | 17 |
| Quantization | 15 |
| Speculative Decoding | 11 |
| ROCm / AMD | 11 |
| Tensor / Data Parallel | 7 |
| Serving / API | 7 |
| Docs / Examples | 6 |
| Models | 3 |
| Structured Output | 2 |

## Attention / FlashInfer  (103 commits)

- **2026-08-10** [`b51bf9ec9e`](https://github.com/sgl-project/sglang/commit/b51bf9ec9e) [#34234](https://github.com/sgl-project/sglang/pull/34234)
  [Spec] Budget the DFLASH draft KV pool from its own attention geometry (#34234)
  _Files: `python/sglang/srt/mem_cache/kv_cache_dtype.py`, `python/sglang/srt/model_executor/model_runner_components/spec_aux_hidden_state.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `python/sglang/srt/speculative/dflash_utils.py` _+1 more__
- **2026-08-10** [`06f32bab6b`](https://github.com/sgl-project/sglang/commit/06f32bab6b) [#33661](https://github.com/sgl-project/sglang/pull/33661)
  [BCG][5/N] MLA Fully Support (#33661)
  _Files: `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+3 more__
- **2026-08-10** [`aea78d1e73`](https://github.com/sgl-project/sglang/commit/aea78d1e73) [#34217](https://github.com/sgl-project/sglang/pull/34217)
  [misc] Pass FP8 scales in FlashInfer SWA prefill, autotune fp8 on SM120, and tighten `is_image_understandable_model` (#34217)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/constrained/xgrammar_backend.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/attention_kv_cache.py` _+8 more__
- **2026-08-10** [`2969ab3d41`](https://github.com/sgl-project/sglang/commit/2969ab3d41) [#34166](https://github.com/sgl-project/sglang/pull/34166)
  [MLX] Window-bounded SWA KV storage and in-graph sampling (#34166)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/constrained/xgrammar_backend.py`, `python/sglang/srt/hardware_backend/mlx/aot.py` _+23 more__
- **2026-08-10** [`accc51c6db`](https://github.com/sgl-project/sglang/commit/accc51c6db) [#34167](https://github.com/sgl-project/sglang/pull/34167)
  [DSA] Fix top-k v2 dropping non-primary ranks' output on CUDA 13.1+ (root cause for #33835) (#34167)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/kernels/ops/attention/dsv4/topk.py`_
- **2026-08-10** [`ee3ee8393c`](https://github.com/sgl-project/sglang/commit/ee3ee8393c) [#34161](https://github.com/sgl-project/sglang/pull/34161)
  fix: preserve GQA head mapping in Triton DCP prefill (#34161)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `test/registered/dcp/test_dcp_layout_unit.py`_
- **2026-08-10** [`553dc0f936`](https://github.com/sgl-project/sglang/commit/553dc0f936) [#30050](https://github.com/sgl-project/sglang/pull/30050)
  [MLX] Support gpt-oss: sliding-window attention, attention sinks, sm_scale (#30050)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/hardware_backend/mlx/aot.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/__init__.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/attention_contract.py` _+8 more__
- **2026-08-09** [`4a5d7d3c67`](https://github.com/sgl-project/sglang/commit/4a5d7d3c67) [#34189](https://github.com/sgl-project/sglang/pull/34189)
  [DSV4] Fix silent KV corruption when speculative draft tokens > 4 (#34189)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsv4_attention.py` _+2 more__
- **2026-08-09** [`110bf7e6a8`](https://github.com/sgl-project/sglang/commit/110bf7e6a8) [#34080](https://github.com/sgl-project/sglang/pull/34080)
  config: retire the hidden global fallbacks and the mamba-extra-buffer instance reads (#34080)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/mem_cache/allocation_sizing.py` _+8 more__
- **2026-08-09** [`168eba3257`](https://github.com/sgl-project/sglang/commit/168eba3257) [#33892](https://github.com/sgl-project/sglang/pull/33892)
  [Fix] Speculative decoding crashes with DP-Attention (#33892)
  _Files: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-08-09** [`2ab96d0fe0`](https://github.com/sgl-project/sglang/commit/2ab96d0fe0) [#34181](https://github.com/sgl-project/sglang/pull/34181)
  Fix mlx unit test batch mock (#34181)
  _Files: `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`_
- **2026-08-09** [`fc40684b32`](https://github.com/sgl-project/sglang/commit/fc40684b32) [#34043](https://github.com/sgl-project/sglang/pull/34043)
  [srt] Fix sconv state memory corruption on specdec (#34043)
  _Files: `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_utils/buffers.py`_
- **2026-08-09** [`11d03eaeef`](https://github.com/sgl-project/sglang/commit/11d03eaeef) [#33471](https://github.com/sgl-project/sglang/pull/33471)
  runtime: Add flashinfer rmsnorm + quant fusion support SM90, SM100, SM120- #32994 (#33471)
  _Files: `benchmark/kernels/bench_fused_rmsnorm_fp8_quant.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/fp8.py` _+7 more__
- **2026-08-09** [`7120f3ee13`](https://github.com/sgl-project/sglang/commit/7120f3ee13) [#33436](https://github.com/sgl-project/sglang/pull/33436)
  fix: support FA4 backend for GLM4.7-flash (#33436)
  _Files: `python/sglang/kernels/ops/attention/flash_attention_v4.py`, `test/registered/kernels/ops/attention/test_flash_attention_4.py`_
- **2026-08-09** [`51470b376f`](https://github.com/sgl-project/sglang/commit/51470b376f) [#33702](https://github.com/sgl-project/sglang/pull/33702)
  [diffusion] feat: support sol-attn sparse attention backend for h3 (#33702)
  _Files: `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/sol_attn.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py` _+2 more__
- **2026-08-08** [`ba7abd4f92`](https://github.com/sgl-project/sglang/commit/ba7abd4f92) [#30964](https://github.com/sgl-project/sglang/pull/30964)
  [AMD] Support DeepSeek V4 DSpark on AMD HIP platform (#30964)
  _Files: `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/runtime.py`, `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` _+5 more__
- **2026-08-08** [`a59bb931c6`](https://github.com/sgl-project/sglang/commit/a59bb931c6) [#32858](https://github.com/sgl-project/sglang/pull/32858)
  Fix DCP KV head mapping for GQA models (#32858)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/linear.py` _+13 more__
- **2026-08-08** [`c4f018ba1d`](https://github.com/sgl-project/sglang/commit/c4f018ba1d) [#31531](https://github.com/sgl-project/sglang/pull/31531)
  [Refactor] Separate ROCm-specific DeepSeek MHA and MLA forward paths (#31531)
  _Files: `python/sglang/srt/batch_overlap/operations.py`, `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/__init__.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py` _+8 more__
- **2026-08-08** [`dc9624deb2`](https://github.com/sgl-project/sglang/commit/dc9624deb2) [#34085](https://github.com/sgl-project/sglang/pull/34085)
  [diffusion] Clean up kernels and shared fast paths (#34085)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/modulate_scale_shift.cuh`, `python/sglang/kernels/jit/csrc/diffusion/qknorm_rope.cuh`, `python/sglang/kernels/jit/csrc/diffusion/residual_gate_add.cuh`, `python/sglang/kernels/jit/csrc/diffusion/usp_relayout.cuh` _+46 more__
- **2026-08-08** [`548ff545c5`](https://github.com/sgl-project/sglang/commit/548ff545c5) [#34107](https://github.com/sgl-project/sglang/pull/34107)
  [diffusion] fix: guard sage attention sm90 bindings (#34107)
  _Files: `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py`, `python/sglang/multimodal_gen/test/unit/test_cuda_attention_backend.py`_
- **2026-08-08** [`a1ca76b24b`](https://github.com/sgl-project/sglang/commit/a1ca76b24b) [#34052](https://github.com/sgl-project/sglang/pull/34052)
  [Scheduler] Unify WAR read-done gating behind shared-read boundary declarations (#34052)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+7 more__
- **2026-08-08** [`e732c0a9dc`](https://github.com/sgl-project/sglang/commit/e732c0a9dc) [#32505](https://github.com/sgl-project/sglang/pull/32505)
  [UT][NPU] add unit tests for ascend_torch_native_backend and mla_preprocess (#32505)
  _Files: `test/registered/unit/npu/attention/test_npu_ascend_torch_native_backend.py`, `test/registered/unit/npu/attention/test_npu_mla_preprocess.py`_
- **2026-08-08** [`db3898fec1`](https://github.com/sgl-project/sglang/commit/db3898fec1) [#32785](https://github.com/sgl-project/sglang/pull/32785)
  fix: avoid piecewise prefill graph for trtllm_mla (#32785)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/configs/test_multimodal_piecewise_cuda_graph.py`_
- **2026-08-08** [`6185ed8011`](https://github.com/sgl-project/sglang/commit/6185ed8011) [#34045](https://github.com/sgl-project/sglang/pull/34045)
  Add registered short-conv tests and backend extensions (#34045)
  _Files: `python/sglang/srt/configs/linear_attn_model_registry.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `python/sglang/srt/models/inkling_common/sconv.py` _+1 more__
- **2026-08-08** [`6679d9b60c`](https://github.com/sgl-project/sglang/commit/6679d9b60c) [#33981](https://github.com/sgl-project/sglang/pull/33981)
  [AMD] Add K3 verified mla kernel for DSpark on triton backend (#33981)
  _Files: `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/layers/attention/triton_backend.py`_
- **2026-08-08** [`f64328c7f6`](https://github.com/sgl-project/sglang/commit/f64328c7f6) [#32581](https://github.com/sgl-project/sglang/pull/32581)
  [diffusion] feat: support quant-videogen prq kv-cache quantization (memory-saving) for causal-dit (#32581)
  _Files: `docs/cookbook/diffusion/LingBot-World/LingBot-World-2.0.mdx`, `docs/cookbook/diffusion/LingBot-World/LingBot-World.mdx`, `docs/docs.json`, `docs/docs/sglang-diffusion/api/cli.mdx` _+12 more__
- **2026-08-08** [`a25c330eb1`](https://github.com/sgl-project/sglang/commit/a25c330eb1) [#33327](https://github.com/sgl-project/sglang/pull/33327)
  [diffusion] feat: cross-node sequence parallelism (Ulysses x Ring) (#33327)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/ring_sp_performance.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py` _+16 more__
- **2026-08-07** [`ce84df0fa1`](https://github.com/sgl-project/sglang/commit/ce84df0fa1) [#33417](https://github.com/sgl-project/sglang/pull/33417)
  Fix deterministic inference for Inkling (#33417)
  _Files: `python/sglang/kernels/ops/attention/flash_attn/cute/batch_invariance.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/block_info.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/flash_fwd_sm100.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py` _+7 more__
- **2026-08-07** [`86f373daff`](https://github.com/sgl-project/sglang/commit/86f373daff) [#34044](https://github.com/sgl-project/sglang/pull/34044)
  docs(cookbook): DeepSeek-V4-Flash-0731 — drop chunked-prefill/autotune flags on B300 low-latency (#34044)
  _Files: `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-08-07** [`0da25ee6f7`](https://github.com/sgl-project/sglang/commit/0da25ee6f7) [#33882](https://github.com/sgl-project/sglang/pull/33882)
  Docs: Ling-3.0-flash cookbook — serve native 256K, drop YaRN override (#33882)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash.mdx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash.jsx`_
- **2026-08-07** [`8600457731`](https://github.com/sgl-project/sglang/commit/8600457731) [#34026](https://github.com/sgl-project/sglang/pull/34026)
  [Spec] Propagate state capture outputs in DFlash (#34026)
  _Files: `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-08-07** [`b3ee679467`](https://github.com/sgl-project/sglang/commit/b3ee679467) [#33208](https://github.com/sgl-project/sglang/pull/33208)
  [MXFP8] Use FlashInfer CUTLASS for dense GEMM on SM120, delete Triton path (#33208)
  _Files: `python/sglang/kernels/ops/quantization/__init__.py`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` _+2 more__
- **2026-08-07** [`699fcdc936`](https://github.com/sgl-project/sglang/commit/699fcdc936) [#33379](https://github.com/sgl-project/sglang/pull/33379)
  Fix _pa_swa_prefill_lens off-by-one in FlashAttentionBackend (#33379)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/unit/layers/attention/test_flashattention_pa_swa_prefill_lens_size.py`_
- **2026-08-07** [`62a28197c0`](https://github.com/sgl-project/sglang/commit/62a28197c0) [#32556](https://github.com/sgl-project/sglang/pull/32556)
  Autotune flashinfer extend buckets at warmup (#32556)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py` _+12 more__
- **2026-08-07** [`1480687cff`](https://github.com/sgl-project/sglang/commit/1480687cff) [#33532](https://github.com/sgl-project/sglang/pull/33532)
  [CP]: Support CP V2 Strategy for dsv4 (#33532)
  _Files: `python/sglang/kernels/ops/attention/dsv4/metadata_kernel.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsa/utils.py` _+6 more__
- **2026-08-07** [`fe52b49827`](https://github.com/sgl-project/sglang/commit/fe52b49827) [#30340](https://github.com/sgl-project/sglang/pull/30340)
  Fix IndexError in Triton backend with pipeline parallelism (#30340)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-08-07** [`13938fed3f`](https://github.com/sgl-project/sglang/commit/13938fed3f) [#33928](https://github.com/sgl-project/sglang/pull/33928)
  [diffusion] feat: make ring admission a backend capability (#33928)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/attention_backend.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/sage_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py` _+3 more__
- **2026-08-07** [`28b43bf693`](https://github.com/sgl-project/sglang/commit/28b43bf693) [#33954](https://github.com/sgl-project/sglang/pull/33954)
  [diffusion] perf: build qwen's masked varlen metadata host-side (#33954)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`, `python/sglang/multimodal_gen/test/unit/test_varlen_meta_host_build.py`_
- **2026-08-07** [`470807ef74`](https://github.com/sgl-project/sglang/commit/470807ef74) [#33976](https://github.com/sgl-project/sglang/pull/33976)
  [NPU] [DOC] Upgrade recommendeded sglang version on Ascend NPU (#33976)
  _Files: `docs/docs/hardware-platforms/ascend-npus/evaluation/accuracy_evaluation.mdx`, `docs/docs/hardware-platforms/ascend-npus/faq.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/quick_start.mdx` _+19 more__
- **2026-08-07** [`7395ee833e`](https://github.com/sgl-project/sglang/commit/7395ee833e) [#33944](https://github.com/sgl-project/sglang/pull/33944)
  [CI] Share VLM engines and prune launch matrices on the per-commit H100/H200 suites (#33944)
  _Files: `python/sglang/test/server_fixtures/streaming_session_fixture.py`, `test/registered/cuda_graph/breakable/test_breakable_cuda_graph.py`, `test/registered/lora/test_lora_overlap_loading.py`, `test/registered/mem_cache/test_post_capture_kv_sizing.py` _+15 more__
- **2026-08-07** [`3ed2a0adf3`](https://github.com/sgl-project/sglang/commit/3ed2a0adf3) [#33616](https://github.com/sgl-project/sglang/pull/33616)
  feat: Add flashinfer mHC fusion for DSV4 (#33616)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-08-07** [`85d611a055`](https://github.com/sgl-project/sglang/commit/85d611a055) [#33953](https://github.com/sgl-project/sglang/pull/33953)
  [diffusion] fix: scope the masked-path replicated guard to sp runs (#33953)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/test/unit/test_usp_attention_replicated_prefix.py`_
- **2026-08-07** [`5e58af1503`](https://github.com/sgl-project/sglang/commit/5e58af1503) [#33463](https://github.com/sgl-project/sglang/pull/33463)
  Fix fractional simulated acceptance in DSpark (#33463)
  _Files: `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py`, `python/sglang/srt/speculative/spec_utils.py`_
- **2026-08-07** [`6dc77e490d`](https://github.com/sgl-project/sglang/commit/6dc77e490d) [#33923](https://github.com/sgl-project/sglang/pull/33923)
  [diffusion] chore: route zimage and hunyuanvideo attention through USPAttention (#33923)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/hunyuanvideo.py`, `python/sglang/multimodal_gen/runtime/models/dits/zimage.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py` _+2 more__
- **2026-08-07** [`698f019a5a`](https://github.com/sgl-project/sglang/commit/698f019a5a) [#33707](https://github.com/sgl-project/sglang/pull/33707)
  [diffusion] chore: derive h3 attention admission from backend capabilities (#33707)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/attention_backend.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py` _+4 more__
- **2026-08-07** [`db8f3cdd11`](https://github.com/sgl-project/sglang/commit/db8f3cdd11) [#33810](https://github.com/sgl-project/sglang/pull/33810)
  fix(gdn): skip the -1 padding sentinel in the chunked extend kernel (#33810)
  _Files: `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `test/registered/8-gpu-models/test_qwen35.py`_
- **2026-08-07** [`1e08b865f9`](https://github.com/sgl-project/sglang/commit/1e08b865f9) [#32667](https://github.com/sgl-project/sglang/pull/32667)
  [diffusion] feat: support K/V-gather style sequence parallel (CP-like) attention (#32667)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/ring_sp_performance.mdx`, `python/sglang/multimodal_gen/runtime/distributed/sp_shard_utils.py`, `python/sglang/multimodal_gen/runtime/entrypoints/vla/protocol.py` _+9 more__
- **2026-08-06** [`bae29f716a`](https://github.com/sgl-project/sglang/commit/bae29f716a) [#33788](https://github.com/sgl-project/sglang/pull/33788)
  Fix inference mode mismatch in FlashInfer warmup (#33788)
  _Files: `python/sglang/srt/model_executor/runner/base_runner.py`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`_
- **2026-08-06** [`18e6c61c21`](https://github.com/sgl-project/sglang/commit/18e6c61c21) [#29677](https://github.com/sgl-project/sglang/pull/29677)
  [AMD] perf: compact Triton extend-attention for ragged prefill (AMD/HIP-only) (#29677)
  _Files: `python/sglang/kernels/ops/attention/extend_attention.py`, `python/sglang/kernels/ops/attention/verify_splitkv.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/triton_backend.py` _+5 more__
- **2026-08-06** [`971932d661`](https://github.com/sgl-project/sglang/commit/971932d661) [#33650](https://github.com/sgl-project/sglang/pull/33650)
  [Kimi-K3] Allow DSPARK verify on cutedsl_mla (fold_sq) (#33650)
  _Files: `python/sglang/srt/arg_groups/overrides.py`_
- **2026-08-06** [`7195b8e4c7`](https://github.com/sgl-project/sglang/commit/7195b8e4c7) [#33851](https://github.com/sgl-project/sglang/pull/33851)
  [diffusion] refactor: validate and document spectrum controls (#33851)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs.json`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx` _+6 more__
- **2026-08-06** [`0e584529f5`](https://github.com/sgl-project/sglang/commit/0e584529f5) [#33832](https://github.com/sgl-project/sglang/pull/33832)
  [CI] Remove profiling from nightly tests (#33832)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/nightly_bench_utils.py`, `python/sglang/test/nightly_utils.py`, `python/sglang/test/performance_test_runner.py` _+61 more__
- **2026-08-06** [`04374ba5e0`](https://github.com/sgl-project/sglang/commit/04374ba5e0) [#33841](https://github.com/sgl-project/sglang/pull/33841)
  Update AOT kernels for Torch 2.13 (#33841)
  _Files: `python/sglang/kernels/aot/CMakeLists.txt`, `python/sglang/kernels/aot/Dockerfile`, `python/sglang/kernels/aot/README.md`, `python/sglang/kernels/aot/rename_wheels.sh` _+1 more__
- **2026-08-06** [`b8140f36ea`](https://github.com/sgl-project/sglang/commit/b8140f36ea) [#33830](https://github.com/sgl-project/sglang/pull/33830)
  Fix lint error (#33830)
  _Files: `python/sglang/srt/speculative/dflash_utils.py`_
- **2026-08-06** [`31c1e5943f`](https://github.com/sgl-project/sglang/commit/31c1e5943f) [#28609](https://github.com/sgl-project/sglang/pull/28609)
  Facade DSA index-cache: MTP topk-reuse state + index-K storage (#28609)
  _Files: `python/sglang/srt/layers/attention/index_topk_share.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/index_key_cache.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+5 more__
- **2026-08-06** [`cf7923615c`](https://github.com/sgl-project/sglang/commit/cf7923615c) [#33694](https://github.com/sgl-project/sglang/pull/33694)
  [AMD] Gate DFLASH non-greedy verify on the target-only kernel being registered (#33694)
  _Files: `python/sglang/srt/speculative/dflash_utils.py`_
- **2026-08-06** [`f33f6a522f`](https://github.com/sgl-project/sglang/commit/f33f6a522f) [#33780](https://github.com/sgl-project/sglang/pull/33780)
  Relax GDN ReplaySSM fold test for Triton 3.7 (#33780)
  _Files: `test/registered/attention/unittests/gdn/test_gdn_replayssm_spec_fold.py`_
- **2026-08-06** [`4ea227fa91`](https://github.com/sgl-project/sglang/commit/4ea227fa91)
  config: the draft runner carries its own attention backend
  _Files: `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/forward_batch_info.py` _+18 more__
- **2026-08-06** [`bebebb8f6c`](https://github.com/sgl-project/sglang/commit/bebebb8f6c)
  config: retire the alias-form process-global config reads
  _Files: `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/k3_sp_collective.py`, `python/sglang/srt/mem_cache/mamba_checkpoint_pool.py`, `python/sglang/srt/models/inkling_common/attn.py` _+3 more__
- **2026-08-06** [`28848bfe7c`](https://github.com/sgl-project/sglang/commit/28848bfe7c) [#33564](https://github.com/sgl-project/sglang/pull/33564)
  Fix Nightly NV CI (#33564)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/n_gram_embedding.py`, `test/registered/8-gpu-models/test_glm52_fp8.py`, `test/registered/8-gpu-models/test_longcat_flash_lite_fp8.py`_
- **2026-08-06** [`c9506d023f`](https://github.com/sgl-project/sglang/commit/c9506d023f) [#33148](https://github.com/sgl-project/sglang/pull/33148)
  [Quantization] Route per-tensor FP8 checkpoints to FlashInfer on SM90 (#33148)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`_
- **2026-08-06** [`ba12a16a62`](https://github.com/sgl-project/sglang/commit/ba12a16a62) [#33655](https://github.com/sgl-project/sglang/pull/33655)
  [diffusion] Prefer cuDNN SDPA over FA4 for dense attention on sm_100 (B200) (#33655)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py` _+2 more__
- **2026-08-05** [`070fde72bf`](https://github.com/sgl-project/sglang/commit/070fde72bf) [#33763](https://github.com/sgl-project/sglang/pull/33763)
  [CI] Remove some unneeded CP tests (#33763)
  _Files: `test/registered/cp/test_glm52_cp_index_share.py`, `test/registered/cp/test_gqa_prefill_cp_legacy.py`, `test/registered/cp/test_mimo_cp.py`_
- **2026-08-05** [`a1cc286062`](https://github.com/sgl-project/sglang/commit/a1cc286062) [#27790](https://github.com/sgl-project/sglang/pull/27790)
  [Intel GPU] DeepSeek V4 4/N: use sgl-kernel implementation of fused_q_norm_rope on XPU (#27790)
  _Files: `python/sglang/kernels/ops/attention/dsv4/elementwise.py`_
- **2026-08-05** [`c0ef548eef`](https://github.com/sgl-project/sglang/commit/c0ef548eef) [#33363](https://github.com/sgl-project/sglang/pull/33363)
  [misc] Unify MLA `scaling` init and remove dead buffer / scaling code (#33363)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/cutlass_mla_backend.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py` _+3 more__
- **2026-08-05** [`990a446773`](https://github.com/sgl-project/sglang/commit/990a446773) [#33253](https://github.com/sgl-project/sglang/pull/33253)
  Fix padded positions in breakable CUDA Graph attention (#33253)
  _Files: `python/sglang/srt/layers/radix_attention.py`, `test/registered/cuda_graph/breakable/test_breakable_cuda_graph.py`, `test/registered/unit/layers/test_radix_attention.py`_
- **2026-08-05** [`717a559f02`](https://github.com/sgl-project/sglang/commit/717a559f02) [#33587](https://github.com/sgl-project/sglang/pull/33587)
  [Scheduler] Align WAR fences with CUDA graph metadata reads (#33587)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/model_executor/model_runner.py` _+9 more__
- **2026-08-05** [`36853b8ffc`](https://github.com/sgl-project/sglang/commit/36853b8ffc) [#33459](https://github.com/sgl-project/sglang/pull/33459)
  [Spec] Support logprobs with DFlash (#33459)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `test/registered/spec/dflash/test_dflash.py`_
- **2026-08-05** [`1a045669e4`](https://github.com/sgl-project/sglang/commit/1a045669e4) [#33641](https://github.com/sgl-project/sglang/pull/33641)
  [CI] Merge tokenizer worker tests and drop redundant triton attention e2e (#33641)
  _Files: `test/registered/attention/test_triton_attention_backend.py`, `test/registered/mla/test_flashmla.py`, `test/registered/mla/test_mla_flashinfer.py`, `test/registered/mla/test_mla_int8_deepseek_v3.py` _+4 more__
- **2026-08-05** [`acaab22d09`](https://github.com/sgl-project/sglang/commit/acaab22d09) [#33703](https://github.com/sgl-project/sglang/pull/33703)
  [diffusion] feat: add SageAttention packed varlen path for minimax-h3 (#33703)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/sage_attn.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/release_metadata.py` _+1 more__
- **2026-08-05** [`b3cdd016ba`](https://github.com/sgl-project/sglang/commit/b3cdd016ba) [#33556](https://github.com/sgl-project/sglang/pull/33556)
  Add Ling-3.0-flash cookbook (#33556)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash.mdx`, `docs/cookbook/autoregressive/InclusionAI/Ring-2.6-1T.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+4 more__
- **2026-08-05** [`4e7209caa8`](https://github.com/sgl-project/sglang/commit/4e7209caa8) [#28267](https://github.com/sgl-project/sglang/pull/28267)
  [NPU] Add causal conv1d (#28267)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`_
- **2026-08-05** [`3b4fac5b99`](https://github.com/sgl-project/sglang/commit/3b4fac5b99) [#31865](https://github.com/sgl-project/sglang/pull/31865)
  [XPU] DeepSeek V4: use sgl-kernel-xpu implemetation of flash_mla_sparse_fwd for prefill (#31865)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-08-05** [`a5888c956f`](https://github.com/sgl-project/sglang/commit/a5888c956f) [#33667](https://github.com/sgl-project/sglang/pull/33667)
  [diffusion] Pack Ulysses Q/K/V input all-to-all into one collective + reusable a2a staging buffers (#33667)
  _Files: `python/sglang/kernels/ops/diffusion/triton/ulysses_qkv.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_dit_contract.py` _+1 more__
- **2026-08-05** [`2f22ed58ea`](https://github.com/sgl-project/sglang/commit/2f22ed58ea) [#29027](https://github.com/sgl-project/sglang/pull/29027)
  [NPU] Adding a fast layernorm for diffusion models and fix BSA (#29027)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/block_sparse_attn.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`_
- **2026-08-05** [`6c05aaae7e`](https://github.com/sgl-project/sglang/commit/6c05aaae7e) [#33063](https://github.com/sgl-project/sglang/pull/33063)
  [trtllm_mha] perf: Stop allocating per-layer scratch inside the decode CUDA graph (#33063)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dense_attention.py`_
- **2026-08-05** [`d2c405f19d`](https://github.com/sgl-project/sglang/commit/d2c405f19d) [#28040](https://github.com/sgl-project/sglang/pull/28040)
  [Intel GPU] DeepSeek V4 8/N: use sgl-kernel implementation of fused_k_norm_rope_flashmla on XPU (#28040)
  _Files: `python/sglang/kernels/ops/attention/dsv4/elementwise.py`_
- **2026-08-05** [`9303e26f03`](https://github.com/sgl-project/sglang/commit/9303e26f03) [#33607](https://github.com/sgl-project/sglang/pull/33607)
  [ci] add qwen 3.5 mtp + replayssm + flashinfer gdn test (#33607)
  _Files: `test/registered/models_e2e/test_qwen35_fp4_mtp.py`_
- **2026-08-04** [`b0fd31ba07`](https://github.com/sgl-project/sglang/commit/b0fd31ba07) [#33537](https://github.com/sgl-project/sglang/pull/33537)
  Multiple flexibility fixes for DP attention (#33537)
  _Files: `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `test/registered/unit/model_executor/test_mlp_sync_pad_unpad.py`_
- **2026-08-04** [`19d3f86895`](https://github.com/sgl-project/sglang/commit/19d3f86895) [#30298](https://github.com/sgl-project/sglang/pull/30298)
  [LoRA] Laguna: per-layer LoRA hidden-dim resolution for packed attention (#30298)
  _Files: `python/sglang/srt/lora/utils.py`, `python/sglang/srt/models/laguna.py`, `test/registered/unit/lora/test_laguna_hidden_dim_unit.py`_
- **2026-08-04** [`0753663b8e`](https://github.com/sgl-project/sglang/commit/0753663b8e) [#33586](https://github.com/sgl-project/sglang/pull/33586)
  [CI] Trim redundant B200 test registrations (#33586)
  _Files: `test/registered/attention/unittests/dense/test_fa3.py`, `test/registered/backends/test_flashinfer_trtllm_gen_attn_backend.py`, `test/registered/lora/test_lora_qwen3_5_35b_a3b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_vl_30b_a3b_instruct_logprob_diff.py` _+5 more__
- **2026-08-04** [`aa06433709`](https://github.com/sgl-project/sglang/commit/aa06433709) [#33306](https://github.com/sgl-project/sglang/pull/33306)
  Avoid TRTLLM prefill output copy (#33306)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/attention/unittests/dense/test_trtllm_mha.py`_
- **2026-08-04** [`4794b401d5`](https://github.com/sgl-project/sglang/commit/4794b401d5) [#33375](https://github.com/sgl-project/sglang/pull/33375)
  [Observability] Add startup, memory, and hybrid SWA diagnostics (#33375)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py` _+32 more__
- **2026-08-04** [`8f2a3ad6d7`](https://github.com/sgl-project/sglang/commit/8f2a3ad6d7) [#33445](https://github.com/sgl-project/sglang/pull/33445)
  [mem_cache] Label HiCache host pools and clarify post-capture KV sizing logs (#33445)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/pool_host/base.py`, `python/sglang/srt/mem_cache/pool_host/mha.py` _+3 more__
- **2026-08-04** [`723c277640`](https://github.com/sgl-project/sglang/commit/723c277640) [#33399](https://github.com/sgl-project/sglang/pull/33399)
  [AMD] [Fix] Enable aiter hd256 FP8 prefill FMHA on gfx950 (#33399)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-08-04** [`b57721ccf7`](https://github.com/sgl-project/sglang/commit/b57721ccf7) [#33427](https://github.com/sgl-project/sglang/pull/33427)
  Enable post-capture KV sizing with DP attention (#33427)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-08-04** [`b6d548afd7`](https://github.com/sgl-project/sglang/commit/b6d548afd7) [#33509](https://github.com/sgl-project/sglang/pull/33509)
  [Fix] Resolve VLM test image placeholders from the model's own chat template (#33509)
  _Files: `python/sglang/test/test_utils.py`, `test/manual/distributed/test_dp_attention_large.py`, `test/manual/quant/test_torchao.py`, `test/registered/cuda_graph/piecewise/test_piecewise_cuda_graph_support_1_gpu.py` _+3 more__
- **2026-08-04** [`bfa4e4a57b`](https://github.com/sgl-project/sglang/commit/bfa4e4a57b) [#32589](https://github.com/sgl-project/sglang/pull/32589)
  [Nemotron] Hoist mamba track-mask host syncs out of the per-layer prefill path (#32589)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/layers/attention/mamba/mamba2_metadata.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`_
- **2026-08-04** [`48dcadc770`](https://github.com/sgl-project/sglang/commit/48dcadc770) [#31500](https://github.com/sgl-project/sglang/pull/31500)
  [AMD][DI][CI] 5/N Add DSV4 wide-EP16 4-node 2P1D nightly recipes (#31500)
  _Files: `scripts/ci/slurm/nightly-configs.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/dsv4flash/1k1k/2p1d-ep16-mtp.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/dsv4flash/1k1k/2p1d-ep16.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/dsv4pro/1k1k/2p1d-ep16-mtp.yaml` _+5 more__
- **2026-08-04** [`afc868517b`](https://github.com/sgl-project/sglang/commit/afc868517b) [#33349](https://github.com/sgl-project/sglang/pull/33349)
  [Perf] Speed up the Kimi-K2.5 vision path and match PIL bicubic in the GPU resize (#33349)
  _Files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/kimi_k25.py`, `python/sglang/srt/models/kimi_vl_moonvit.py`, `python/sglang/srt/multimodal/mm_utils.py` _+7 more__
- **2026-08-04** [`b058dc9106`](https://github.com/sgl-project/sglang/commit/b058dc9106) [#33353](https://github.com/sgl-project/sglang/pull/33353)
  [diffusion] fix: reject ring parallelism where it would silently miscompute (#33353)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`_
- **2026-08-04** [`1e64fc1563`](https://github.com/sgl-project/sglang/commit/1e64fc1563) [#33065](https://github.com/sgl-project/sglang/pull/33065)
  [Fix] Honor FlashMLA natural-log LSE in DCP reduction (#33065)
  _Files: `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/srt/layers/dcp/comm.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `test/registered/kernels/test_dcp_lse_combine.py`_
- **2026-08-04** [`92087ef4d2`](https://github.com/sgl-project/sglang/commit/92087ef4d2) [#33432](https://github.com/sgl-project/sglang/pull/33432)
  fix(mem_cache): state the MLA KV bound in the DCP index space (#33432)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-08-04** [`eb31a53338`](https://github.com/sgl-project/sglang/commit/eb31a53338) [#33455](https://github.com/sgl-project/sglang/pull/33455)
  Revert "Add flashinfer rmsnorm + quant fusion support SM90, SM100, SM120" (#33455)
  _Files: `benchmark/kernels/bench_fused_rmsnorm_fp8_quant.py`, `python/sglang/kernels/aot/benchmark/bench_fp8_gemm.py`, `python/sglang/kernels/aot/csrc/gemm/fp8_gemm_kernel.cu`, `python/sglang/kernels/aot/tests/test_fp8_gemm.py` _+10 more__
- **2026-08-04** [`7f6a2e2b50`](https://github.com/sgl-project/sglang/commit/7f6a2e2b50) [#33443](https://github.com/sgl-project/sglang/pull/33443)
  [Refactor] Clean up and split DSA indexer (#33443)
  _Files: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_metadata.py` _+5 more__
- **2026-08-04** [`3960983753`](https://github.com/sgl-project/sglang/commit/3960983753) [#32994](https://github.com/sgl-project/sglang/pull/32994)
  Add flashinfer rmsnorm + quant fusion support SM90, SM100, SM120 (#32994)
  _Files: `benchmark/kernels/bench_fused_rmsnorm_fp8_quant.py`, `python/sglang/kernels/aot/benchmark/bench_fp8_gemm.py`, `python/sglang/kernels/aot/csrc/gemm/fp8_gemm_kernel.cu`, `python/sglang/kernels/aot/tests/test_fp8_gemm.py` _+10 more__
- **2026-08-04** [`1307968605`](https://github.com/sgl-project/sglang/commit/1307968605) [#32952](https://github.com/sgl-project/sglang/pull/32952)
  [JIT] Drop redundant per-kernel arch overrides (#32952)
  _Files: `python/sglang/kernels/jit/__main__.py`, `python/sglang/kernels/jit/utils/arch.py`, `python/sglang/kernels/ops/attention/qprep_bf16_fp8_sm90.py`, `python/sglang/kernels/ops/attention/sparse_mla_q8kv8_prefill_sm90.py` _+1 more__
- **2026-08-03** [`92999d84f4`](https://github.com/sgl-project/sglang/commit/92999d84f4) [#32046](https://github.com/sgl-project/sglang/pull/32046)
  [AMD]Qwen3.5 integration gfx950 fmha fp8 hd256 (#32046)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-08-03** [`204e0fbac0`](https://github.com/sgl-project/sglang/commit/204e0fbac0) [#32320](https://github.com/sgl-project/sglang/pull/32320)
  [SM120] Only split touched SWA pages in FlashMLA page-split kernel (#32320)
  _Files: `python/sglang/kernels/ops/attention/flash_mla_sm120.py`, `test/registered/kernels/ops/attention/test_flash_mla_backends.py`_
- **2026-08-03** [`b1754a8f3b`](https://github.com/sgl-project/sglang/commit/b1754a8f3b) [#33102](https://github.com/sgl-project/sglang/pull/33102)
  [gdn] fused replayssm ring write into flashinfer gdn mtp verify kernel (#33102)
  _Files: `python/sglang/kernels/ops/attention/cutedsl_gdn_mtp_ring.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `test/registered/attention/unittests/gdn/test_gdn_cutedsl_ring_verify.py`, `test/registered/attention/unittests/gdn/test_gdn_replayssm_spec_fold.py`_
- **2026-08-03** [`b8109b5d63`](https://github.com/sgl-project/sglang/commit/b8109b5d63) [#33338](https://github.com/sgl-project/sglang/pull/33338)
  config: retire the last process-global config field reads (#33338)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/kernels/ops/layernorm/mhc.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/attention_registry.py` _+9 more__
- **2026-08-03** [`ebb1c88d23`](https://github.com/sgl-project/sglang/commit/ebb1c88d23) [#33334](https://github.com/sgl-project/sglang/pull/33334)
  config: stop writing config onto the published ServerArgs at three sites (#33334)
  _Files: `python/sglang/srt/constrained/base_grammar_backend.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/utils.py` _+6 more__
- **2026-08-03** [`e824b24250`](https://github.com/sgl-project/sglang/commit/e824b24250) [#33137](https://github.com/sgl-project/sglang/pull/33137)
  [CP] Fuse zigzag attention into a single call (#33137)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/layers/cp/zigzag.py`, `test/registered/cp/test_cp_strategy_unit.py`_

## Multimodal  (77 commits)

- **2026-08-10** [`f2a4c4c847`](https://github.com/sgl-project/sglang/commit/f2a4c4c847) [#31843](https://github.com/sgl-project/sglang/pull/31843)
  [AMD] [CI] Enable 3 nested unit tests needing harness stub fixes (#31843)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/unit/progressive_resolution/test_progressive.py`, `python/sglang/multimodal_gen/test/unit/sana_wm/test_streaming_realtime_path.py`, `scripts/ci/utils/ci_coverage_report.py`_
- **2026-08-10** [`169783d42f`](https://github.com/sgl-project/sglang/commit/169783d42f) [#34173](https://github.com/sgl-project/sglang/pull/34173)
  [diffusion] chore: make torch.compile opt-in for speed mode (#34173)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/model_deployment_config.py`, `python/sglang/multimodal_gen/runtime/server_args/auto_tune.py` _+1 more__
- **2026-08-10** [`441910f926`](https://github.com/sgl-project/sglang/commit/441910f926) [#34172](https://github.com/sgl-project/sglang/pull/34172)
  [diffusion] LTX-2 quality=high fused RMSNorm+modulate + FFN GELU epilogue (H200 ltx23-one-stage denoise 45.85->43.24 s, ~matches torch.compile) (#34172)
  _Files: `python/sglang/kernels/ops/diffusion/ltx2_rmsnorm_modulate.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `test/registered/kernels/ops/diffusion/test_ltx2_rms_norm_modulate.py`_
- **2026-08-10** [`56ef810cad`](https://github.com/sgl-project/sglang/commit/56ef810cad) [#34174](https://github.com/sgl-project/sglang/pull/34174)
  [diffusion] BCG: auto-capture the default warmup resolution instead of hard-requiring --warmup-resolutions (H200 SANA denoise 0.73->0.457 s with a single flag) (#34174)
  _Files: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-08-09** [`71043b9dbb`](https://github.com/sgl-project/sglang/commit/71043b9dbb) [#34160](https://github.com/sgl-project/sglang/pull/34160)
  Revert parallel request lifecycle tracking from #32588 (#34160)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_io_struct.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py` _+1 more__
- **2026-08-09** [`22e003580b`](https://github.com/sgl-project/sglang/commit/22e003580b) [#33921](https://github.com/sgl-project/sglang/pull/33921)
  [Kimi K3] optimize: preprocess cpu-transport images on the vision owner (#33921)
  _Files: `python/sglang/srt/managers/mm_schedule.py`, `python/sglang/srt/models/kimi_k3.py`, `python/sglang/srt/multimodal/kimi_k3_image_processing.py`, `python/sglang/srt/multimodal/processors/kimi_k3.py` _+2 more__
- **2026-08-09** [`d0aa37b49b`](https://github.com/sgl-project/sglang/commit/d0aa37b49b) [#32685](https://github.com/sgl-project/sglang/pull/32685)
  [diffusion] fix: update weight from tensor detects device by uuid (#32685)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/post_training/io_struct.py`, `python/sglang/multimodal_gen/runtime/entrypoints/post_training/weights_api.py`, `python/sglang/multimodal_gen/runtime/post_training/gpu_worker_post_training_mixin.py`_
- **2026-08-09** [`38c007dfe5`](https://github.com/sgl-project/sglang/commit/38c007dfe5) [#34126](https://github.com/sgl-project/sglang/pull/34126)
  [diffusion] FLUX.1: route the adaLN LN+modulate sites through the bit-exact fused LayerNorm+modulate kernel (H200 1024^2 lossless denoise -1.2%, e2e wall -2.9%) (#34126)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/flux.py`, `test/registered/kernels/ops/diffusion/test_flux_ln_modulate.py`_
- **2026-08-09** [`6424fec326`](https://github.com/sgl-project/sglang/commit/6424fec326) [#34125](https://github.com/sgl-project/sglang/pull/34125)
  [diffusion] Bit-exact data-movement elimination for the Wan causal VAE decoder (H200 LongLive2 704x1280x61f: decode 2.80->2.32 s lossless / 2.12->1.67 s quality=high, e2e -10.7%) (#34125)
  _Files: `python/sglang/kernels/ops/diffusion/triton/wan_causal_cache.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py`, `test/registered/kernels/ops/diffusion/test_wan_causal_cache.py`_
- **2026-08-09** [`33ed5d4413`](https://github.com/sgl-project/sglang/commit/33ed5d4413) [#34124](https://github.com/sgl-project/sglang/pull/34124)
  [diffusion] perf_logger: SYNC_STAGE_PROFILING must drain the GPU queue for stage records too (fixes 2-3x inflated DecodingStage readings) (#34124)
  _Files: `python/sglang/multimodal_gen/runtime/utils/perf_logger.py`, `test/registered/kernels/ops/diffusion/test_stage_profiler_sync.py`_
- **2026-08-08** [`cf2d4fd679`](https://github.com/sgl-project/sglang/commit/cf2d4fd679) [#34099](https://github.com/sgl-project/sglang/pull/34099)
  docs: clarify K3 VLM feature transport (#34099)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-08-08** [`2c0188cc78`](https://github.com/sgl-project/sglang/commit/2c0188cc78) [#34100](https://github.com/sgl-project/sglang/pull/34100)
  [Fix] Give the piecewise CUDA graph test stub an `hf_config` (#34100)
  _Files: `test/registered/unit/configs/test_multimodal_piecewise_cuda_graph.py`_
- **2026-08-08** [`891445676c`](https://github.com/sgl-project/sglang/commit/891445676c) [#34015](https://github.com/sgl-project/sglang/pull/34015)
  [diffusion] Sana: bit-exact fused aten LayerNorm+modulate under BCG (H200 denoise -4.8%) (#34015)
  _Files: `python/sglang/kernels/ops/diffusion/triton/layernorm_modulate.py`, `python/sglang/multimodal_gen/runtime/models/dits/sana.py`, `test/registered/kernels/ops/diffusion/test_sana_ln_modulate.py`_
- **2026-08-08** [`d747bd052e`](https://github.com/sgl-project/sglang/commit/d747bd052e) [#33936](https://github.com/sgl-project/sglang/pull/33936)
  feat(vlm): auto-select cuda vmm on multi-node mnnvl (#33936)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/model_loader/utils.py`, `python/sglang/srt/models/kimi_k25.py` _+7 more__
- **2026-08-08** [`5dffa06fe1`](https://github.com/sgl-project/sglang/commit/5dffa06fe1) [#34008](https://github.com/sgl-project/sglang/pull/34008)
  [diffusion] GLM-Image bit-exact fused aten LayerNorm+modulate / qk-LN (H200 30-step denoise -8.1%) (#34008)
  _Files: `python/sglang/kernels/ops/diffusion/triton/layernorm_modulate.py`, `python/sglang/multimodal_gen/runtime/models/dits/glm_image.py`, `test/registered/kernels/ops/diffusion/test_glm_image_ln_modulate.py`_
- **2026-08-08** [`148f15b0af`](https://github.com/sgl-project/sglang/commit/148f15b0af) [#34004](https://github.com/sgl-project/sglang/pull/34004)
  [diffusion] FLUX.1 fused adaLN modulate (bit-exact) + RoPE cache hoist, LN-affine folding behind quality=high (H200 e2e -3.5% lossless / -6.9% high) (#34004)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/modulate_scale_shift.cuh`, `python/sglang/kernels/ops/diffusion/fused_ln_modulate.py`, `python/sglang/kernels/ops/diffusion/modulate_scale_shift.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux.py` _+3 more__
- **2026-08-08** [`24c84dfa68`](https://github.com/sgl-project/sglang/commit/24c84dfa68) [#33704](https://github.com/sgl-project/sglang/pull/33704)
  [diffusion] doc: add parallelism overview (#33704)
  _Files: `docs/docs.json`, `docs/docs/sglang-diffusion/parallelism.mdx`_
- **2026-08-08** [`55f02e6887`](https://github.com/sgl-project/sglang/commit/55f02e6887) [#33691](https://github.com/sgl-project/sglang/pull/33691)
  Support Intern-S2-Mobius (#33691)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/interns2_mobius.py`, `python/sglang/srt/configs/model_config.py` _+6 more__
- **2026-08-08** [`52afe87a08`](https://github.com/sgl-project/sglang/commit/52afe87a08) [#33969](https://github.com/sgl-project/sglang/pull/33969)
  [diffusion] fix: stop runai-model-streamer's rank-discovery collective from firing on independent per-rank loads (#33969)
  _Files: `python/sglang/multimodal_gen/runtime/loader/weight_utils.py`, `python/sglang/multimodal_gen/test/unit/test_weight_utils.py`_
- **2026-08-07** [`c59d2b4329`](https://github.com/sgl-project/sglang/commit/c59d2b4329) [#34017](https://github.com/sgl-project/sglang/pull/34017)
  [Fix] Judge the phase-checker device-assert test by its FAIL line, not the exit code (#34017)
  _Files: `test/registered/models_e2e/test_qwen3_next_models.py`, `test/registered/utils/test_phase_checker.py`, `test/registered/vlm/test_vision_openai_server_a.py`_
- **2026-08-07** [`8fc66d1a62`](https://github.com/sgl-project/sglang/commit/8fc66d1a62) [#34030](https://github.com/sgl-project/sglang/pull/34030)
  docker: pin Kimi images to SGLang commit (#34030)
  _Files: `docker/kimi_k3/kimi_k3_cu12.Dockerfile`, `docker/kimi_k3/kimi_k3_cu13.Dockerfile`_
- **2026-08-07** [`7f6b4cb94b`](https://github.com/sgl-project/sglang/commit/7f6b4cb94b) [#33899](https://github.com/sgl-project/sglang/pull/33899)
  Add CUDA VMM multimodal feature transport (#33899)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/multimodal/processors/base_processor.py` _+6 more__
- **2026-08-07** [`6c7498113f`](https://github.com/sgl-project/sglang/commit/6c7498113f) [#33989](https://github.com/sgl-project/sglang/pull/33989)
  [diffusion] Enable breakable CUDA graph for SANA (H200 1024px e2e -26%, bit-exact) (#33989)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising_dmd.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`_
- **2026-08-07** [`d4be483efb`](https://github.com/sgl-project/sglang/commit/d4be483efb) [#33885](https://github.com/sgl-project/sglang/pull/33885)
  [diffusion] Enable breakable CUDA graph for LTX-2 (H200 two-stage e2e 10.75 s -> 6.90 s, 1.56x) (#33885)
  _Files: `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/runner.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/runtime/warmup_request_builder.py`_
- **2026-08-07** [`bc148dfdc8`](https://github.com/sgl-project/sglang/commit/bc148dfdc8) [#33965](https://github.com/sgl-project/sglang/pull/33965)
  [diffusion] feat: make scheduler rpc deadlines explicit (#33965)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/runtime/scheduler_client.py` _+5 more__
- **2026-08-07** [`bc8c037041`](https://github.com/sgl-project/sglang/commit/bc8c037041) [#33983](https://github.com/sgl-project/sglang/pull/33983)
  Fix vae fast path test after the gate refactor (#33983)
  _Files: `test/registered/kernels/ops/diffusion/test_autoencoder_kl_fastpath.py`_
- **2026-08-07** [`5ca734fc3d`](https://github.com/sgl-project/sglang/commit/5ca734fc3d) [#33960](https://github.com/sgl-project/sglang/pull/33960)
  [diffusion] UX: speed up tp and fsdp checkpoint loading (#33960)
  _Files: `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/runtime/loader/rank_local_checkpoint.py`, `python/sglang/multimodal_gen/runtime/loader/weight_utils.py`, `python/sglang/multimodal_gen/test/unit/test_fsdp_load.py`_
- **2026-08-07** [`1034977318`](https://github.com/sgl-project/sglang/commit/1034977318) [#33054](https://github.com/sgl-project/sglang/pull/33054)
  [diffusion] fix: bind each rank to accelerator before distributed init (#33054)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/platforms/interface.py`, `python/sglang/multimodal_gen/runtime/platforms/mps.py`_
- **2026-08-07** [`acb64db9e2`](https://github.com/sgl-project/sglang/commit/acb64db9e2) [#33421](https://github.com/sgl-project/sglang/pull/33421)
  [diffusion] fix: enable bcg with tp (#33421)
  _Files: `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/runner.py`, `python/sglang/multimodal_gen/runtime/distributed/group_coordinator.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/single_test_file/test_diffusion_bcg_tp2_zimage_turbo.py` _+1 more__
- **2026-08-07** [`7af3d000f2`](https://github.com/sgl-project/sglang/commit/7af3d000f2) [#33787](https://github.com/sgl-project/sglang/pull/33787)
  [diffusion] feat: gate /health and /health_generate on warmup completion and add liveness endpoint (#33787)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/test/unit/test_health_warmup_gate.py`_
- **2026-08-07** [`572434e2f6`](https://github.com/sgl-project/sglang/commit/572434e2f6) [#33886](https://github.com/sgl-project/sglang/pull/33886)
  [diffusion] Z-Image bit-exact fused qk-norm (H200 Turbo 1024px e2e -6.4%) (#33886)
  _Files: `python/sglang/kernels/ops/diffusion/triton/zimage_native_norm.py`, `python/sglang/multimodal_gen/runtime/models/dits/zimage.py`, `python/sglang/multimodal_gen/test/unit/test_zimage_qknorm_fusion.py`_
- **2026-08-07** [`9aadacfc53`](https://github.com/sgl-project/sglang/commit/9aadacfc53) [#33931](https://github.com/sgl-project/sglang/pull/33931)
  [diffusion] CI: exercise the default sp selection in CI (#33931)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`_
- **2026-08-07** [`a79340dedd`](https://github.com/sgl-project/sglang/commit/a79340dedd) [#33864](https://github.com/sgl-project/sglang/pull/33864)
  [diffusion] fix: minimax-h3 text encoder device mismatch under --text-encoder-cpu-offload (#33864)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/minimax_h3_qwen3vl.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_encoder_device.py`_
- **2026-08-07** [`c2657cc4bf`](https://github.com/sgl-project/sglang/commit/c2657cc4bf) [#33849](https://github.com/sgl-project/sglang/pull/33849)
  [diffusion] refactor: gate fast vae paths by quality (#33849)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/runtime/models/vaes/fast_path_gate.py` _+6 more__
- **2026-08-07** [`453ea21dd3`](https://github.com/sgl-project/sglang/commit/453ea21dd3) [#22634](https://github.com/sgl-project/sglang/pull/22634)
  fix(qwen2_5vl): replace in-place += with out-of-place + on expand view in decode path (#22634)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/qwen2_5vl.py`_
- **2026-08-07** [`c54dc4582f`](https://github.com/sgl-project/sglang/commit/c54dc4582f) [#33688](https://github.com/sgl-project/sglang/pull/33688)
  [Diffusion]Skipping tensor copying for non-BCG GLM-Image workflows (#33688)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/glm_image.py`, `python/sglang/multimodal_gen/test/scripts/gen_perf_baselines.py`, `python/sglang/multimodal_gen/test/server/ascend/perf_baselines_npu.json`_
- **2026-08-07** [`9ee658d4f6`](https://github.com/sgl-project/sglang/commit/9ee658d4f6) [#33878](https://github.com/sgl-project/sglang/pull/33878)
  [diffusion] CI: fix output-rank test fixture (#33878)
  _Files: `python/sglang/multimodal_gen/test/unit/realtime/test_output_materialization.py`_
- **2026-08-06** [`44bde3911a`](https://github.com/sgl-project/sglang/commit/44bde3911a) [#33848](https://github.com/sgl-project/sglang/pull/33848)
  [diffusion] fix: resolve IPC A2A peers from process groups (#33848)
  _Files: `docs/docs/sglang-diffusion/environment_variables.mdx`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a.py`, `python/sglang/multimodal_gen/test/unit/test_ipc_a2a_lifecycle.py`_
- **2026-08-06** [`591cfb0881`](https://github.com/sgl-project/sglang/commit/591cfb0881) [#33823](https://github.com/sgl-project/sglang/pull/33823)
  [diffusion] FLUX.2 bit-exact residual-gate fast path (H200 klein-4B 50-step denoise -1.2%) (#33823)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py`, `test/registered/kernels/ops/diffusion/test_residual_gate_add.py`_
- **2026-08-06** [`dd98c9572a`](https://github.com/sgl-project/sglang/commit/dd98c9572a) [#33818](https://github.com/sgl-project/sglang/pull/33818)
  [diffusion] Generalize the FLUX.2 VAE decoder fast path to AutoencoderKL (Z-Image / FLUX.1) behind quality=high (#33818)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/flux2_vae_cuda_opt.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py`, `test/registered/kernels/ops/diffusion/test_autoencoder_kl_fastpath.py`_
- **2026-08-06** [`183bd80add`](https://github.com/sgl-project/sglang/commit/183bd80add) [#33845](https://github.com/sgl-project/sglang/pull/33845)
  [diffusion] chore: centralize entrypoint API hygiene (#33845)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/__init__.py`, `python/sglang/multimodal_gen/runtime/entrypoints/diffusion_generator.py`, `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/common_api.py` _+4 more__
- **2026-08-06** [`2132cdef16`](https://github.com/sgl-project/sglang/commit/2132cdef16) [#33843](https://github.com/sgl-project/sglang/pull/33843)
  [diffusion] chore: consolidate pipeline core hygiene (#33843)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/zimage.py`, `python/sglang/multimodal_gen/runtime/pipelines/flux.py`, `python/sglang/multimodal_gen/runtime/pipelines/flux_2.py`, `python/sglang/multimodal_gen/runtime/pipelines/glm_image.py` _+17 more__
- **2026-08-06** [`1a15cf1536`](https://github.com/sgl-project/sglang/commit/1a15cf1536) [#33653](https://github.com/sgl-project/sglang/pull/33653)
  Gate multimodal feature transport by model capability (#33653)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-08-06** [`e8d0fe92e9`](https://github.com/sgl-project/sglang/commit/e8d0fe92e9) [#32999](https://github.com/sgl-project/sglang/pull/32999)
  [diffusion] Fix GLM-Image resolution alignment (#32999)
  _Files: `python/sglang/multimodal_gen/configs/sample/glmimage.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/glm_image.py` _+4 more__
- **2026-08-06** [`3654740347`](https://github.com/sgl-project/sglang/commit/3654740347) [#33854](https://github.com/sgl-project/sglang/pull/33854)
  [diffusion] ERNIE-Image bit-exact fused RMSNorm+scale/shift (H200 1024^2 e2e 15.63 -> 15.00 s, denoise -3.3%) (#33854)
  _Files: `python/sglang/kernels/ops/diffusion/triton/rmsnorm_scale_shift_bitexact.py`, `python/sglang/multimodal_gen/runtime/models/dits/ernie_image.py`, `test/registered/kernels/ops/diffusion/test_ernie_norm_scale_shift.py`_
- **2026-08-06** [`295784723a`](https://github.com/sgl-project/sglang/commit/295784723a) [#33822](https://github.com/sgl-project/sglang/pull/33822)
  [diffusion] Ideogram 4: fuse RMSNorm modulate/gate chains via the Z-Image Triton suite behind quality=high (H200 e2e -2.9%/-3.4%) (#33822)
  _Files: `python/sglang/kernels/ops/diffusion/fused_gate_rmsnorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/ideogram.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `test/registered/kernels/ops/diffusion/test_fused_gate_rmsnorm.py`_
- **2026-08-06** [`eff6a11350`](https://github.com/sgl-project/sglang/commit/eff6a11350) [#33819](https://github.com/sgl-project/sglang/pull/33819)
  [diffusion] FLUX.1 bit-exact residual-gate fast path + tanh-GELU epilogue behind quality=high (H200 e2e -1.1% lossless / -4.3% high) (#33819)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/flux.py`, `test/registered/kernels/ops/diffusion/test_fused_linear_gelu.py`, `test/registered/kernels/ops/diffusion/test_residual_gate_add.py`_
- **2026-08-06** [`4cdab7b4f4`](https://github.com/sgl-project/sglang/commit/4cdab7b4f4) [#31899](https://github.com/sgl-project/sglang/pull/31899)
  [AMD] Add msgpack to ROCm diffusion deps (fix multimodal-gen unit test ModuleNotFoundError) (#31899)
  _Files: `python/pyproject_other.toml`_
- **2026-08-06** [`bfce378e5f`](https://github.com/sgl-project/sglang/commit/bfce378e5f) [#33775](https://github.com/sgl-project/sglang/pull/33775)
  [diffusion] feat: capture-safe pynccl all-to-all (#33775)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/device_communicators/pynccl.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/pynccl_wrapper.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/single_test_file/test_pynccl_a2a_capture_2_gpu.py`_
- **2026-08-06** [`32e5d788bd`](https://github.com/sgl-project/sglang/commit/32e5d788bd) [#32365](https://github.com/sgl-project/sglang/pull/32365)
  [mm] rust-server: native multimodal processing for Qwen VL (integrate sglang-mm, e2e) (#32365)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/multimodal_processor.py`, `python/sglang/srt/managers/rust_server.py` _+31 more__
- **2026-08-06** [`c84ddc0e76`](https://github.com/sgl-project/sglang/commit/c84ddc0e76) [#33738](https://github.com/sgl-project/sglang/pull/33738)
  docker: pin nightly image source to workflow commit (#33738)
  _Files: `.github/workflows/release-docker-dev.yml`_
- **2026-08-06** [`b6876fc652`](https://github.com/sgl-project/sglang/commit/b6876fc652) [#33734](https://github.com/sgl-project/sglang/pull/33734)
  [diffusion] ERNIE-Image bit-exact residual-gate fast path (H200 1024^2 e2e 16.17 -> 15.75 s) (#33734)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/ernie_image.py`, `test/registered/kernels/ops/diffusion/test_ernie_residual_gate_add.py`_
- **2026-08-06** [`604d3561b0`](https://github.com/sgl-project/sglang/commit/604d3561b0) [#33725](https://github.com/sgl-project/sglang/pull/33725)
  [diffusion] feat: data-parallel serving (--dp-size) (#33725)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/runtime/scheduler_client.py` _+4 more__
- **2026-08-06** [`d90ef69802`](https://github.com/sgl-project/sglang/commit/d90ef69802) [#31483](https://github.com/sgl-project/sglang/pull/31483)
  [AMD] ci: run vetted nested multimodal_gen unit tests on AMD (#31483)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `scripts/ci/utils/ci_coverage_report.py`_
- **2026-08-05** [`5424d2039c`](https://github.com/sgl-project/sglang/commit/5424d2039c) [#33731](https://github.com/sgl-project/sglang/pull/33731)
  [CI] Fix GLM-Image usage unit tests (#33731)
  _Files: `python/sglang/multimodal_gen/test/unit/test_glm_image_ar.py`, `python/sglang/multimodal_gen/test/unit/test_glm_image_multi_output.py`_
- **2026-08-05** [`55b1c09e73`](https://github.com/sgl-project/sglang/commit/55b1c09e73) [#32434](https://github.com/sgl-project/sglang/pull/32434)
  [core] Consolidate compiled-kernel caches under SGLANG_CACHE_DIR (#32434)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/__init__.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/srt/entrypoints/engine.py` _+5 more__
- **2026-08-05** [`ea65f8ddc9`](https://github.com/sgl-project/sglang/commit/ea65f8ddc9) [#31491](https://github.com/sgl-project/sglang/pull/31491)
  Feat/spectrum (#31491)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/stablediffusion3.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/configs/sample/spectrum.py`, `python/sglang/multimodal_gen/runtime/cache/__init__.py` _+8 more__
- **2026-08-05** [`3425c93666`](https://github.com/sgl-project/sglang/commit/3425c93666) [#33546](https://github.com/sgl-project/sglang/pull/33546)
  [diffusion] Wan VAE RMSNorm+SiLU fusion behind quality=high (H200 FastWan2.2 e2e 9.611 -> 9.125 s) (#33546)
  _Files: `python/sglang/kernels/ops/diffusion/triton/wan_rmsnorm_silu.py`, `python/sglang/multimodal_gen/runtime/models/vaes/flux2_vae_cuda_opt.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wan_vae_cuda_opt.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py` _+1 more__
- **2026-08-05** [`22d558b103`](https://github.com/sgl-project/sglang/commit/22d558b103) [#33378](https://github.com/sgl-project/sglang/pull/33378)
  [Feature] Add GLM Image usage report (#33378)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/utils.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py` _+5 more__
- **2026-08-05** [`8279702e0b`](https://github.com/sgl-project/sglang/commit/8279702e0b) [#33689](https://github.com/sgl-project/sglang/pull/33689)
  [AMD] Stop publishing the K3 MI35X nightly image (#33689)
  _Files: `.github/workflows/release-docker-amd-rocm720-nightly.yml`_
- **2026-08-05** [`d96df7bed5`](https://github.com/sgl-project/sglang/commit/d96df7bed5) [#30683](https://github.com/sgl-project/sglang/pull/30683)
  [Diffusion] Batch GLM-Image AR requests (#30683)
  _Files: `docs/docs/sglang-diffusion/dynamic_batching.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/glm_image.py`, `python/sglang/multimodal_gen/runtime/managers/dynamic_batch_admission.py` _+10 more__
- **2026-08-05** [`4949b5fccf`](https://github.com/sgl-project/sglang/commit/4949b5fccf) [#30883](https://github.com/sgl-project/sglang/pull/30883)
  [XPU] Add qknorm_rope support for Flux (#30883)
  _Files: `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py`_
- **2026-08-04** [`58da9859c4`](https://github.com/sgl-project/sglang/commit/58da9859c4) [#33597](https://github.com/sgl-project/sglang/pull/33597)
  [CI] Extract `download-rust-ext` and give every install step a cache fallback (#33597)
  _Files: `.github/actions/download-rust-ext/action.yml`, `.github/workflows/_pr-test-rust-ext-build.yml`, `.github/workflows/_pr-test-stage-cpu.yml`, `.github/workflows/_pr-test-stage.yml` _+6 more__
- **2026-08-04** [`95d0e57e83`](https://github.com/sgl-project/sglang/commit/95d0e57e83) [#33536](https://github.com/sgl-project/sglang/pull/33536)
  [diffusion] Fuse DiT FFN tanh-GELU into up-proj GEMM (cublasLt epilogue) behind quality=high (Qwen-Image 1024^2 denoise 12.36 -> 12.05 s on H200) (#33536)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/fused_linear_gelu.py`, `python/sglang/multimodal_gen/runtime/models/dits/glm_image.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py` _+2 more__
- **2026-08-04** [`0d0c7d853f`](https://github.com/sgl-project/sglang/commit/0d0c7d853f) [#33451](https://github.com/sgl-project/sglang/pull/33451)
  [diffusion] FLUX.2 VAE decoder fast path behind quality=high (H200: 1024^2 97.6->29.2 ms, 2048^2 437.2->168.5 ms) (#33451)
  _Files: `python/sglang/kernels/ops/diffusion/triton/group_norm_silu_twopass.py`, `python/sglang/multimodal_gen/runtime/models/vaes/flux2_vae_cuda_opt.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/decoding.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py` _+1 more__
- **2026-08-04** [`17d19081d9`](https://github.com/sgl-project/sglang/commit/17d19081d9) [#32364](https://github.com/sgl-project/sglang/pull/32364)
  [mm] sglang-mm: server vision pipeline core (fetch/driver/pipeline) + Qwen VL (#32364)
  _Files: `.github/workflows/pr-test-rust-exts.yml`, `.pre-commit-config.yaml`, `python/setup.py`, `rust/Cargo.lock` _+27 more__
- **2026-08-04** [`101bb2327c`](https://github.com/sgl-project/sglang/commit/101bb2327c) [#33365](https://github.com/sgl-project/sglang/pull/33365)
  [diffusion] fix: fix local-path detection for MiniMax-H3 and other non-diffusers models (#33365)
  _Files: `python/sglang/cli/utils.py`, `python/sglang/multimodal_gen/registry.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`, `python/sglang/utils.py`_
- **2026-08-04** [`c6f2a9c1d4`](https://github.com/sgl-project/sglang/commit/c6f2a9c1d4) [#33453](https://github.com/sgl-project/sglang/pull/33453)
  [diffusion] Restrict request-level quality to two validated tiers: lossless (default) and high (#33453)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py` _+6 more__
- **2026-08-04** [`614825fd38`](https://github.com/sgl-project/sglang/commit/614825fd38) [#33367](https://github.com/sgl-project/sglang/pull/33367)
  [vla] fix: pi05 models does not apply scale factor for language embeddings (#33367)
  _Files: `docs/cookbook/vla/OpenPI/Pi0.5.mdx`, `python/sglang/multimodal_gen/benchmarks/bench_pi05_openpi.py`, `python/sglang/multimodal_gen/runtime/models/vlas/pi05_core.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/pi05_preprocess.py` _+4 more__
- **2026-08-04** [`cdff33d738`](https://github.com/sgl-project/sglang/commit/cdff33d738) [#33384](https://github.com/sgl-project/sglang/pull/33384)
  [CI] Build the Rust extension modules once per run instead of in every CUDA job (#33384)
  _Files: `.github/workflows/_pr-test-rust-ext-build.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test-jit-kernel.yml` _+5 more__
- **2026-08-04** [`f829fb3ff7`](https://github.com/sgl-project/sglang/commit/f829fb3ff7) [#33317](https://github.com/sgl-project/sglang/pull/33317)
  [diffusion] Fix component accuracy topology reuse (#33317)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/test/single_test_file/component_accuracy/config.py`, `python/sglang/multimodal_gen/test/single_test_file/component_accuracy/hooks.py` _+4 more__
- **2026-08-03** [`b8f6181bff`](https://github.com/sgl-project/sglang/commit/b8f6181bff) [#33437](https://github.com/sgl-project/sglang/pull/33437)
  [CI] Build the Rust extensions with the pinned toolchain instead of the image default (#33437)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`, `scripts/ci/utils/install_rustup.sh`_
- **2026-08-03** [`4ef1660cd8`](https://github.com/sgl-project/sglang/commit/4ef1660cd8) [#33398](https://github.com/sgl-project/sglang/pull/33398)
  [Docs] MiniMax-H3: add measured H200 Ulysses4 vs TP2+Ulysses2 topology data (#33398)
  _Files: `docs_new/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`_
- **2026-08-03** [`0ba46c88e5`](https://github.com/sgl-project/sglang/commit/0ba46c88e5) [#33281](https://github.com/sgl-project/sglang/pull/33281)
  [diffusion] CI: add minimax-h3 2-gpu consistency coverage (#33281)
  _Files: `.github/workflows/diffusion-ci-gt-gen.yml`, `.github/workflows/pr-test-multimodal-gen.yml`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json` _+3 more__
- **2026-08-03** [`c2dbdfd218`](https://github.com/sgl-project/sglang/commit/c2dbdfd218) [#33345](https://github.com/sgl-project/sglang/pull/33345)
  [Docs] Fix overlapping quality-profile table headers on MiniMax-H3 page (#33345)
  _Files: `docs_new/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`_
- **2026-08-03** [`dd6ddc053b`](https://github.com/sgl-project/sglang/commit/dd6ddc053b) [#33308](https://github.com/sgl-project/sglang/pull/33308)
  [Fix] Drop deprecated multimodal processor residency state (#33308)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` _+4 more__
- **2026-08-03** [`4bc593fdc8`](https://github.com/sgl-project/sglang/commit/4bc593fdc8) [#33307](https://github.com/sgl-project/sglang/pull/33307)
  [Perf] Broadcast single-image DP vision embedding instead of pad-to-max all-gather (#33307)
  _Files: `python/sglang/srt/multimodal/mm_utils.py`, `test/manual/vlm/verify_single_image_gather.py`, `test/registered/unit/models/test_kimi_k25.py`_

## Prefill / Decode Disaggregation  (27 commits)

- **2026-08-10** [`a76a167812`](https://github.com/sgl-project/sglang/commit/a76a167812) [#28753](https://github.com/sgl-project/sglang/pull/28753)
  Fix/hisparse host backed max request length (#28753)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/model_executor/model_runner.py`, `test/registered/unit/mem_cache/test_hisparse_max_token_pool_size.py`_
- **2026-08-10** [`5a8e360e70`](https://github.com/sgl-project/sglang/commit/5a8e360e70) [#34191](https://github.com/sgl-project/sglang/pull/34191)
  [PD] Skip speculative verify scratch on prefill servers (saves num_draft_tokens x mamba pool per rank) (#34191)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/model_executor/runner/base_runner.py`_
- **2026-08-10** [`c20e99bd22`](https://github.com/sgl-project/sglang/commit/c20e99bd22) [#34163](https://github.com/sgl-project/sglang/pull/34163)
  fix(vlm): preserve Kimi-K3 GPU JPEG accuracy (#34163)
  _Files: `docker/kimi_k3/kimi_k3_cu12.Dockerfile`, `docker/kimi_k3/kimi_k3_cu13.Dockerfile`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/multimodal/processors/kimi_k3.py` _+4 more__
- **2026-08-09** [`7c90840bad`](https://github.com/sgl-project/sglang/commit/7c90840bad) [#34186](https://github.com/sgl-project/sglang/pull/34186)
  [CI] Key scheduled CUDA suites by runner_config instead of hand-written jobs (#34186)
  _Files: `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/nightly-test-nvidia.yml` _+90 more__
- **2026-08-09** [`e216c2bc59`](https://github.com/sgl-project/sglang/commit/e216c2bc59) [#34095](https://github.com/sgl-project/sglang/pull/34095)
  config: the runner and scheduler read resolved config from the bags (#34095)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/request_receiver.py`, `python/sglang/srt/model_executor/model_runner.py` _+6 more__
- **2026-08-08** [`f6a6f5bf1e`](https://github.com/sgl-project/sglang/commit/f6a6f5bf1e) [#34070](https://github.com/sgl-project/sglang/pull/34070)
  [CI] Trim redundant nightly test registrations (#34070)
  _Files: `test/registered/backends/test_deepseek_r1_fp8_trtllm_backend.py`, `test/registered/backends/test_qwen3_fp4_trtllm_gen_moe.py`, `test/registered/bench_fn/test_bench_serving_functionality.py`, `test/registered/cuda_graph/piecewise/test_pcg_glm52_fp4.py` _+20 more__
- **2026-08-08** [`dd5d82bead`](https://github.com/sgl-project/sglang/commit/dd5d82bead) [#33724](https://github.com/sgl-project/sglang/pull/33724)
  [NPU] Improve the execution efficiency and maintainability of pr‑test‑npu (#33724)
  _Files: `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/pr-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py` _+56 more__
- **2026-08-08** [`a5af27f49e`](https://github.com/sgl-project/sglang/commit/a5af27f49e) [#33887](https://github.com/sgl-project/sglang/pull/33887)
  config: retire ServerArgs.derive; per-runner values are constructor arguments (#33887)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/server_args.py` _+8 more__
- **2026-08-07** [`eb3cc879e0`](https://github.com/sgl-project/sglang/commit/eb3cc879e0) [#33932](https://github.com/sgl-project/sglang/pull/33932)
  Install DeepEP from release wheels (#33932)
  _Files: `.github/workflows/_pr-test-sgl-kernel-build.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test-extra.yml` _+27 more__
- **2026-08-07** [`07297049e9`](https://github.com/sgl-project/sglang/commit/07297049e9) [#33925](https://github.com/sgl-project/sglang/pull/33925)
  config: route DCP topology reads through get_parallel() (#33925)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/managers/scheduler.py` _+10 more__
- **2026-08-06** [`af7c62e337`](https://github.com/sgl-project/sglang/commit/af7c62e337) [#33794](https://github.com/sgl-project/sglang/pull/33794)
  Fix paged SWA retraction resume accounting (#33794)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-08-06** [`434e646282`](https://github.com/sgl-project/sglang/commit/434e646282) [#28836](https://github.com/sgl-project/sglang/pull/28836)
  [Deps] Upgrade CUDA PyTorch stack to 2.13 (#28836)
  _Files: `.github/workflows/_docker-build-and-publish.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/nightly-72-gpu-gb200.yml`, `.github/workflows/pr-test-jit-kernel.yml` _+30 more__
- **2026-08-06** [`05c7ebf64c`](https://github.com/sgl-project/sglang/commit/05c7ebf64c) [#30545](https://github.com/sgl-project/sglang/pull/30545)
  [Disagg][StagingBuffer][2/2] Support radix cache (#30545)
  _Files: `python/sglang/srt/disaggregation/common/staging_buffer.py`, `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+6 more__
- **2026-08-06** [`c212a6938c`](https://github.com/sgl-project/sglang/commit/c212a6938c) [#33850](https://github.com/sgl-project/sglang/pull/33850)
  [diffusion] chore: retire released warmup and decoder flags (#33850)
  _Files: `docs/cookbook/diffusion/SANA-WM/SANA-WM.mdx`, `docs/docs/sglang-diffusion/cache_dit.mdx`, `docs/docs/sglang-diffusion/disaggregation.mdx`, `docs/docs/sglang-diffusion/models_with_ar.mdx` _+15 more__
- **2026-08-06** [`45dfd80674`](https://github.com/sgl-project/sglang/commit/45dfd80674) [#33844](https://github.com/sgl-project/sglang/pull/33844)
  [diffusion] refactor: simplify disaggregation transport hygiene (#33844)
  _Files: `python/sglang/multimodal_gen/runtime/disaggregation/scheduler_mixin.py`, `python/sglang/multimodal_gen/runtime/disaggregation/transport/allocator.py`, `python/sglang/multimodal_gen/runtime/disaggregation/transport/buffer.py`, `python/sglang/multimodal_gen/runtime/disaggregation/transport/manager.py` _+1 more__
- **2026-08-06** [`48f1b14fc7`](https://github.com/sgl-project/sglang/commit/48f1b14fc7) [#32638](https://github.com/sgl-project/sglang/pull/32638)
  test: fix NIXL EP Mooncake FT test (#32638)
  _Files: `test/manual/ep/test_nixl_ep.py`_
- **2026-08-06** [`8e11feb68e`](https://github.com/sgl-project/sglang/commit/8e11feb68e) [#30393](https://github.com/sgl-project/sglang/pull/30393)
  [HiCache] Support packed and sidecar draft caches for MTP/EAGLE/DSpark (#30393)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/cache_init_params.py` _+15 more__
- **2026-08-06** [`99cfc90658`](https://github.com/sgl-project/sglang/commit/99cfc90658)
  config: retire ServerArgs.override in favour of derive()
  _Files: `.claude/rules/general-code-style.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/compile_deep_gemm.py`, `python/sglang/lang/backend/runtime_endpoint.py` _+18 more__
- **2026-08-05** [`9436de717f`](https://github.com/sgl-project/sglang/commit/9436de717f) [#31477](https://github.com/sgl-project/sglang/pull/31477)
  [Spec][PD] Enable fused TopK for GLM-5.2 MTP IndexShare (#31477)
  _Files: `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/speculative/eagle_disaggregation.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-08-05** [`c0d5ebd6c4`](https://github.com/sgl-project/sglang/commit/c0d5ebd6c4) [#33654](https://github.com/sgl-project/sglang/pull/33654)
  [CI] Move CPU-only unit tests to the CPU suite and trim dead 5090 registrations (#33654)
  _Files: `test/registered/perf/test_vlm_perf_5090.py`, `test/registered/unit/disaggregation/test_specv2_kvcache_offloading.py`, `test/registered/unit/distributed/test_cuda_wrapper.py`, `test/registered/unit/distributed/test_parallel_state.py` _+26 more__
- **2026-08-05** [`5dc4102960`](https://github.com/sgl-project/sglang/commit/5dc4102960) [#33523](https://github.com/sgl-project/sglang/pull/33523)
  [npu] [bugfix] Fix PD‑disaggregation error (#33523)
  _Files: `python/sglang/srt/disaggregation/ascend/conn.py`_
- **2026-08-04** [`e76d0acdc9`](https://github.com/sgl-project/sglang/commit/e76d0acdc9) [#33346](https://github.com/sgl-project/sglang/pull/33346)
  migrate NPU PR/nightly test cases to a3-560T (#33346)
  _Files: `.github/workflows/pr-test-npu.yml`, `docs/docs/hardware-platforms/ascend-npus/development/contribution_guide.mdx`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/npu_eval_accuracy_kit.py` _+29 more__
- **2026-08-03** [`db0fe370b7`](https://github.com/sgl-project/sglang/commit/db0fe370b7) [#33118](https://github.com/sgl-project/sglang/pull/33118)
  [PD] Fix false health-503 during decode retraction re-admission (#33118)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-08-03** [`6cf661117d`](https://github.com/sgl-project/sglang/commit/6cf661117d) [#33133](https://github.com/sgl-project/sglang/pull/33133)
  [PD] Add a queues.prealloc_ready counter to the load snapshot (#33133)
  _Files: `python/sglang/srt/managers/load_snapshot.py`, `python/sglang/srt/managers/scheduler_components/load_inquirer.py`, `test/registered/unit/entrypoints/test_v1_loads_aggregate.py`_
- **2026-08-03** [`3953788596`](https://github.com/sgl-project/sglang/commit/3953788596) [#31901](https://github.com/sgl-project/sglang/pull/31901)
  [HiSparse]Fix DeepSeek V4 HiSparse PD Transfers with Separate Host and Device KV Indices (#31901)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `test/registered/unit/mem_cache/test_hisparse_allocator.py`_
- **2026-08-03** [`a2d1003b18`](https://github.com/sgl-project/sglang/commit/a2d1003b18) [#32403](https://github.com/sgl-project/sglang/pull/32403)
  [Mooncake] Fix ProcessGroup API imports (#32403)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/elastic_ep/elastic_ep.py`_
- **2026-08-03** [`5d2dbb35a6`](https://github.com/sgl-project/sglang/commit/5d2dbb35a6) [#33125](https://github.com/sgl-project/sglang/pull/33125)
  [rust-server] PD disaggregation support (#33125)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/disagg_service.py`, `python/sglang/srt/managers/scheduler.py` _+11 more__

## MoE / Expert Parallel  (26 commits)

- **2026-08-10** [`e226bb711c`](https://github.com/sgl-project/sglang/commit/e226bb711c) [#33962](https://github.com/sgl-project/sglang/pull/33962)
  enable TRT-LLM for MiniMax M3 by preserving SwiGLU params (#33962)
  _Files: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py` _+4 more__
- **2026-08-10** [`449f0da78f`](https://github.com/sgl-project/sglang/commit/449f0da78f) [#33808](https://github.com/sgl-project/sglang/pull/33808)
  [Intel GPU] DeepSeek V4 15/N: Add silu_and_mul_clamp support to triton fused_moe for XPU (#33808)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`_
- **2026-08-10** [`5d85f25f75`](https://github.com/sgl-project/sglang/commit/5d85f25f75) [#32229](https://github.com/sgl-project/sglang/pull/32229)
  fix(minimax): use routed TRT-LLM for NVFP4 MoE auto on SM100 (#32229)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-08-09** [`63833f8034`](https://github.com/sgl-project/sglang/commit/63833f8034) [#34081](https://github.com/sgl-project/sglang/pull/34081)
  config: business code no longer reads the published ServerArgs (#34081)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` _+31 more__
- **2026-08-08** [`cea16bf229`](https://github.com/sgl-project/sglang/commit/cea16bf229) [#34006](https://github.com/sgl-project/sglang/pull/34006)
  Fix Qwen3-MoE producing garbage with the mori a2a backend (#34006)
  _Files: `python/sglang/srt/models/qwen3_moe.py`_
- **2026-08-08** [`3fbb5330c7`](https://github.com/sgl-project/sglang/commit/3fbb5330c7) [#33764](https://github.com/sgl-project/sglang/pull/33764)
  Fix the router GEMM inaccuracy when using _front_w in Kimi-K3 (#33764)
  _Files: `python/sglang/kernels/jit/csrc/gemm/per_token_group_quant.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/situ_and_mul.cuh`, `python/sglang/kernels/jit/csrc/moe/route_quant_fused.cuh`, `python/sglang/kernels/ops/gemm/cutedsl_bf16_gemm.py` _+4 more__
- **2026-08-08** [`ec5199b906`](https://github.com/sgl-project/sglang/commit/ec5199b906) [#34106](https://github.com/sgl-project/sglang/pull/34106)
  [jit_kernel] Fix missing JIT kernel namespaces (#34106)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/modulate_scale_shift.cuh`, `python/sglang/kernels/jit/csrc/moe/align_single_token.cuh`_
- **2026-08-08** [`5fdf6cd18f`](https://github.com/sgl-project/sglang/commit/5fdf6cd18f) [#32395](https://github.com/sgl-project/sglang/pull/32395)
  [MoE] Single-launch moe_align for tiny batches with many experts (#32395)
  _Files: `python/sglang/kernels/ops/moe/__init__.py`, `python/sglang/kernels/ops/moe/moe_align_small_numel.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/moe_align_block_size.py`, `test/registered/kernels/ops/moe/test_moe_align_small_numel.py`_
- **2026-08-08** [`afb4f37ca5`](https://github.com/sgl-project/sglang/commit/afb4f37ca5) [#33903](https://github.com/sgl-project/sglang/pull/33903)
  [Inkling] silu_and_mul: replace helion kernels with plain Triton (#33903)
  _Files: `python/pyproject.toml`, `python/pyproject_other.toml`, `python/sglang/kernels/ops/moe/inkling_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/silu_and_mul_interleaved_sm_100.json` _+9 more__
- **2026-08-08** [`b61a06921e`](https://github.com/sgl-project/sglang/commit/b61a06921e) [#33889](https://github.com/sgl-project/sglang/pull/33889)
  moe: the shared-experts-fusion decision is a per-runner value the loader installs (#33889)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/model_executor/model_runner.py` _+36 more__
- **2026-08-08** [`eda0ddc260`](https://github.com/sgl-project/sglang/commit/eda0ddc260) [#33888](https://github.com/sgl-project/sglang/pull/33888)
  config: delete the dead get_server_args() bindings across the repo (#33888)
  _Files: `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` _+10 more__
- **2026-08-07** [`4020bc95a7`](https://github.com/sgl-project/sglang/commit/4020bc95a7) [#33543](https://github.com/sgl-project/sglang/pull/33543)
  Fix Nemotron W4A16 NVFP4 MoE backend (#33543)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/quantization/marlin_utils_fp4.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-08-07** [`a42683eb62`](https://github.com/sgl-project/sglang/commit/a42683eb62) [#32341](https://github.com/sgl-project/sglang/pull/32341)
  [diffusion] model: support lingbot-video moe 30b t2v (#32341)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/__init__.py`, `python/sglang/multimodal_gen/configs/models/dits/lingbot_video_moe.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/__init__.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/lingbot_video_moe.py` _+16 more__
- **2026-08-06** [`4ad990ba7d`](https://github.com/sgl-project/sglang/commit/4ad990ba7d) [#33115](https://github.com/sgl-project/sglang/pull/33115)
  [ModelOpt FP4] Support online MoE weight quantization (#33115)
  _Files: `docs/docs/advanced_features/quantization.mdx`, `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` _+10 more__
- **2026-08-06** [`beabc5949b`](https://github.com/sgl-project/sglang/commit/beabc5949b) [#33618](https://github.com/sgl-project/sglang/pull/33618)
  Enable MoE deferred finalize by default and drop its expert_weights dtype workaround (#33618)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/kernels/jit/csrc/moe/moe_finalize_fuse_shared.cu`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`_
- **2026-08-06** [`4c0a8940fa`](https://github.com/sgl-project/sglang/commit/4c0a8940fa) [#33205](https://github.com/sgl-project/sglang/pull/33205)
  [Kernel] Unify BaseFusedOp and MultiPlatformOp dispatch (#33205)
  _Files: `docs/docs/hardware-platforms/plugin.mdx`, `python/sglang/kernels/README.md`, `python/sglang/kernels/fused_op.py`, `python/sglang/kernels/ops/layernorm/__init__.py` _+19 more__
- **2026-08-05** [`3869fe556f`](https://github.com/sgl-project/sglang/commit/3869fe556f) [#33756](https://github.com/sgl-project/sglang/pull/33756)
  [CI] Collapse the EAGLE launch matrix and the scoring engine boots on the per-commit runners (#33756)
  _Files: `python/sglang/multimodal_gen/runtime/layers/quantization/mxfp4.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py` _+18 more__
- **2026-08-05** [`7bc90ab394`](https://github.com/sgl-project/sglang/commit/7bc90ab394) [#33474](https://github.com/sgl-project/sglang/pull/33474)
  Select DeepGEMM standard layouts by memory budget (#33474)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py` _+1 more__
- **2026-08-05** [`02cd44c59a`](https://github.com/sgl-project/sglang/commit/02cd44c59a) [#33108](https://github.com/sgl-project/sglang/pull/33108)
  feat(dgx-spark): add inkling-small MoE support for sm_121 (#33108)
  _Files: `python/sglang/kernels/ops/moe/inkling_moe.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/silu_and_mul_interleaved_sm_121.json`, `python/sglang/srt/utils/common.py`_
- **2026-08-05** [`b9d572ee02`](https://github.com/sgl-project/sglang/commit/b9d572ee02) [#33752](https://github.com/sgl-project/sglang/pull/33752)
  [test] Re-enable a pruned Inkling LoRA unit-test set (68 -> 9 cases) (#33752)
  _Files: `test/registered/unit/lora/test_experimental_sgl_marlin_alignment.py`, `test/registered/unit/lora/test_experimental_sgl_marlin_direct_decode.py`, `test/registered/unit/lora/test_experimental_sgl_marlin_multi_prefill.py`, `test/registered/unit/lora/test_experimental_sgl_marlin_policy.py` _+5 more__
- **2026-08-05** [`a14c870886`](https://github.com/sgl-project/sglang/commit/a14c870886) [#33123](https://github.com/sgl-project/sglang/pull/33123)
  Fix broken Nemotron DP attention (#33123)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/mamba/mamba2_metadata.py`, `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`, `python/sglang/srt/model_executor/model_runner_components/layer_setup.py` _+3 more__
- **2026-08-05** [`81c7a54ecd`](https://github.com/sgl-project/sglang/commit/81c7a54ecd) [#33433](https://github.com/sgl-project/sglang/pull/33433)
  [NVIDIA] Use sm_100f instead of sm_100a for sgl-kernel and FlashMLA (#33433)
  _Files: `python/sglang/kernels/aot/CMakeLists.txt`, `python/sglang/kernels/aot/cmake/flashmla.cmake`, `python/sglang/kernels/aot/csrc/moe/fp8_blockwise_moe_kernel.cu`_
- **2026-08-05** [`198a3bc29b`](https://github.com/sgl-project/sglang/commit/198a3bc29b) [#33615](https://github.com/sgl-project/sglang/pull/33615)
  [Test] Route GEMM backend UTs through real layer modules and weight loaders (#33615)
  _Files: `python/sglang/test/layer_ut_utils.py`, `python/sglang/test/quant_ref_utils.py`, `test/registered/debug_utils/test_tensor_dump_forward_hook.py`, `test/registered/kernels/ops/moe/test_fp4_moe.py` _+7 more__
- **2026-08-04** [`76dc89f5aa`](https://github.com/sgl-project/sglang/commit/76dc89f5aa) [#33611](https://github.com/sgl-project/sglang/pull/33611)
  [Test] Replace NVFP4 MoE runner backend e2e matrix with a layer-level unit test (#33611)
  _Files: `test/registered/backends/test_deepseek_v3_fp4_cutedsl_moe.py`, `test/registered/backends/test_deepseek_v3_fp4_cutlass_moe.py`, `test/registered/quant/test_deepseek_v3_fp4_4gpu_extra.py`, `test/registered/unit/layers/quantization/test_nvfp4_moe_backends.py`_
- **2026-08-04** [`16d3b118a2`](https://github.com/sgl-project/sglang/commit/16d3b118a2) [#33428](https://github.com/sgl-project/sglang/pull/33428)
  Reduce startup log noise and fix Dynamo / CUDA-graph edge cases (#33428)
  _Files: `python/sglang/kernels/jit/utils/compile.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` _+4 more__
- **2026-08-03** [`5fe97637df`](https://github.com/sgl-project/sglang/commit/5fe97637df) [#33128](https://github.com/sgl-project/sglang/pull/33128)
  Support DeepGEMM for standard MoE dispatch (#33128)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/srt/layers/quantization/fp8.py`, `test/registered/kernels/ops/moe/test_minimax_quant_scatter.py` _+1 more__

## Other  (24 commits)

- **2026-08-09** [`a2199c1dee`](https://github.com/sgl-project/sglang/commit/a2199c1dee) [#34094](https://github.com/sgl-project/sglang/pull/34094)
  config: pin that resolution is reproducible from the raw input (#34094)
  _Files: `test/registered/unit/server_args/test_resolution_is_reproducible.py`_
- **2026-08-09** [`c2fbe2f6d8`](https://github.com/sgl-project/sglang/commit/c2fbe2f6d8) [#34169](https://github.com/sgl-project/sglang/pull/34169)
  Add skill for the logprob consistency tests (#34169)
  _Files: `.claude/skills/kl-consistency-test/SKILL.md`_
- **2026-08-09** [`fb72a37fde`](https://github.com/sgl-project/sglang/commit/fb72a37fde) [#34168](https://github.com/sgl-project/sglang/pull/34168)
  Add deterministic logprob-consistency test for inkling-small nvfp4 (#34168)
  _Files: `test/registered/models_e2e/test_inkling_small_nvfp4.py`_
- **2026-08-09** [`3fe65e0654`](https://github.com/sgl-project/sglang/commit/3fe65e0654) [#33423](https://github.com/sgl-project/sglang/pull/33423)
  Deterministic gumbel sampling: clamp u=1 so masked tokens can't be sampled (#33423)
  _Files: `python/sglang/srt/layers/sampler.py`, `test/registered/sampling/test_deterministic_gumbel_u1.py`_
- **2026-08-09** [`c500674124`](https://github.com/sgl-project/sglang/commit/c500674124) [#32402](https://github.com/sgl-project/sglang/pull/32402)
  Switch inkling per-commit test to nvfp4 (#32402)
  _Files: `test/registered/models_e2e/test_inkling_small_nvfp4.py`_
- **2026-08-09** [`bc285b2064`](https://github.com/sgl-project/sglang/commit/bc285b2064) [#34158](https://github.com/sgl-project/sglang/pull/34158)
  refactor: clean up logits processor helpers (#34158)
  _Files: `python/sglang/srt/layers/logits_processor.py`_
- **2026-08-08** [`c69d59395b`](https://github.com/sgl-project/sglang/commit/c69d59395b) [#33898](https://github.com/sgl-project/sglang/pull/33898)
  [inkling] Render tool-result media instead of coercing content to str (#33898)
  _Files: `python/sglang/srt/parser/inkling_renderer.py`, `test/registered/unit/parser/test_inkling_renderer.py`_
- **2026-08-07** [`1d812865dc`](https://github.com/sgl-project/sglang/commit/1d812865dc) [#33558](https://github.com/sgl-project/sglang/pull/33558)
  [Laguna] fix YaRN mscale double-application in rope config (#33558)
  _Files: `python/sglang/srt/configs/laguna.py`, `test/registered/unit/configs/test_laguna_config.py`_
- **2026-08-07** [`8e7d361def`](https://github.com/sgl-project/sglang/commit/8e7d361def) [#31958](https://github.com/sgl-project/sglang/pull/31958)
  [perf] Compute input logprobs without materializing the full-vocab log-softmax (#31958)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/logprob_processor.py`, `python/sglang/srt/layers/logsumexp.py`, `test/registered/unit/layers/test_logprob_fast_input.py`_
- **2026-08-06** [`8a1637a479`](https://github.com/sgl-project/sglang/commit/8a1637a479) [#33663](https://github.com/sgl-project/sglang/pull/33663)
  Fix serving benchmark post-warmup cache flush race (#33663)
  _Files: `python/sglang/benchmark/serving.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`_
- **2026-08-06** [`735995e7bd`](https://github.com/sgl-project/sglang/commit/735995e7bd) [#33138](https://github.com/sgl-project/sglang/pull/33138)
  Implement random tie breadking for cache_aware sglang router policy (#33138)
  _Files: `sgl-model-gateway/src/policies/cache_aware.rs`_
- **2026-08-06** [`f01f706960`](https://github.com/sgl-project/sglang/commit/f01f706960) [#27692](https://github.com/sgl-project/sglang/pull/27692)
  [RL] Skip rotary cache tensors in weight checker (#27692)
  _Files: `python/sglang/srt/utils/weight_checker.py`_
- **2026-08-05** [`593777c046`](https://github.com/sgl-project/sglang/commit/593777c046) [#33527](https://github.com/sgl-project/sglang/pull/33527)
  [FIX] [benchmark] Fix flush_cache failure after warmup by waiting for server idle (#33527)
  _Files: `python/sglang/benchmark/serving.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`_
- **2026-08-05** [`211ee64249`](https://github.com/sgl-project/sglang/commit/211ee64249) [#33575](https://github.com/sgl-project/sglang/pull/33575)
  [rotary] Rebuild the shared RoPE cache entry when its buffers are dead (#33575)
  _Files: `python/sglang/srt/layers/rotary_embedding/factory.py`, `test/registered/rotary/test_rope_cache_invalidation.py`_
- **2026-08-04** [`6808c6d571`](https://github.com/sgl-project/sglang/commit/6808c6d571) [#33609](https://github.com/sgl-project/sglang/pull/33609)
  [Tiny] Little enhancement of Kimi-K3 test (#33609)
  _Files: `test/registered/models_e2e/test_kimi_k3_b300.py`_
- **2026-08-04** [`a9c3b55435`](https://github.com/sgl-project/sglang/commit/a9c3b55435) [#33392](https://github.com/sgl-project/sglang/pull/33392)
  [Refactor] Keep chat template validation out of ServerArgs dispatcher (#33392)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-08-04** [`e510dc58ba`](https://github.com/sgl-project/sglang/commit/e510dc58ba) [#33472](https://github.com/sgl-project/sglang/pull/33472)
  Add @Jiminator as codeowner for Laguna model and config (#33472)
  _Files: `.github/CODEOWNERS`_
- **2026-08-04** [`34af3ff386`](https://github.com/sgl-project/sglang/commit/34af3ff386) [#33545](https://github.com/sgl-project/sglang/pull/33545)
  Allow optimistic prefill with L2 hierarchical cache and write-back policy (#33545)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-08-04** [`abddb1c7e9`](https://github.com/sgl-project/sglang/commit/abddb1c7e9) [#32541](https://github.com/sgl-project/sglang/pull/32541)
  [Kimi] Support kimi-k3 (#32541)
- **2026-08-04** [`4494fb96b2`](https://github.com/sgl-project/sglang/commit/4494fb96b2) [#33420](https://github.com/sgl-project/sglang/pull/33420)
  refactor the tcp listener binding logic (#33420)
  _Files: `rust/sglang-server/src/api_server.rs`, `rust/sglang-server/src/runtime.rs`, `rust/sglang-server/src/utils.rs`, `rust/sglang-server/src/utils/sock.rs`_
- **2026-08-04** [`c113ead98a`](https://github.com/sgl-project/sglang/commit/c113ead98a) [#32562](https://github.com/sgl-project/sglang/pull/32562)
  Bump helion version to 1.4 (#32562)
  _Files: `python/pyproject.toml`, `python/pyproject_other.toml`_
- **2026-08-03** [`d48ab2d386`](https://github.com/sgl-project/sglang/commit/d48ab2d386) [#33371](https://github.com/sgl-project/sglang/pull/33371)
  Fix BCG circular import during server startup (#33371)
  _Files: `python/sglang/srt/layers/cp/bcg.py`_
- **2026-08-03** [`8186eeb939`](https://github.com/sgl-project/sglang/commit/8186eeb939) [#33026](https://github.com/sgl-project/sglang/pull/33026)
  [rust-server] Reland: fix TCP-layer TTFT stalls (#33026) (#33269)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/sglang-server/Cargo.toml`, `rust/sglang-server/src/api_server.rs` _+1 more__
- **2026-08-03** [`741e33db81`](https://github.com/sgl-project/sglang/commit/741e33db81) [#32525](https://github.com/sgl-project/sglang/pull/32525)
  fix(sampling): reject conflicting structural tag constraints (#32525)
  _Files: `python/sglang/srt/sampling/sampling_params.py`, `test/registered/unit/sampling/test_sampling_params.py`_

## Scheduler / Batching  (23 commits)

- **2026-08-10** [`fb3d1419fd`](https://github.com/sgl-project/sglang/commit/fb3d1419fd) [#30023](https://github.com/sgl-project/sglang/pull/30023)
  [tracing] sglang tracing v2: support exporting tracing data asynchronously (#30023)
  _Files: `docs/docs/references/environment_variables.mdx`, `docs/docs/references/production_request_trace.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py` _+4 more__
- **2026-08-09** [`78cd60b4e3`](https://github.com/sgl-project/sglang/commit/78cd60b4e3) [#33477](https://github.com/sgl-project/sglang/pull/33477)
  [srt] Reuse batched Mamba boundary mask (#33477)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/managers/test_batch_result_processor_mamba_boundary.py`_
- **2026-08-09** [`ce1b9f88b6`](https://github.com/sgl-project/sglang/commit/ce1b9f88b6) [#34133](https://github.com/sgl-project/sglang/pull/34133)
  config: derive the runner's DCP topology from its ParallelState (#34133)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/parallel_state_wrapper.py`, `python/sglang/srt/managers/scheduler.py` _+4 more__
- **2026-08-08** [`d238e36b24`](https://github.com/sgl-project/sglang/commit/d238e36b24) [#33565](https://github.com/sgl-project/sglang/pull/33565)
  [Fix] Restore data_parallel_rank alias on native /generate (dp-aware gateway routing is silently dropped) (#33565)
  _Files: `python/sglang/srt/managers/io_struct.py`, `test/registered/unit/managers/test_io_struct.py`_
- **2026-08-08** [`209857334e`](https://github.com/sgl-project/sglang/commit/209857334e) [#33404](https://github.com/sgl-project/sglang/pull/33404)
  [Scheduler] Gate SWA eviction on accumulated tokens (#33404)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-08-07** [`df3aa20d89`](https://github.com/sgl-project/sglang/commit/df3aa20d89) [#33908](https://github.com/sgl-project/sglang/pull/33908)
  Reland serving-time Triton load diagnostics (#33908)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/utils/triton_load_watch.py`_
- **2026-08-07** [`b53a39c5e4`](https://github.com/sgl-project/sglang/commit/b53a39c5e4) [#34020](https://github.com/sgl-project/sglang/pull/34020)
  Limit prefill delayer debug logs to rank zero (#34020)
  _Files: `python/sglang/srt/managers/prefill_delayer.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-08-07** [`fe6a05a8e8`](https://github.com/sgl-project/sglang/commit/fe6a05a8e8) [#32977](https://github.com/sgl-project/sglang/pull/32977)
  fix: preserve priority for batched embedding requests (#32977)
  _Files: `python/sglang/srt/managers/io_struct.py`, `test/registered/unit/managers/test_io_struct.py`_
- **2026-08-06** [`5d1a0c7129`](https://github.com/sgl-project/sglang/commit/5d1a0c7129) [#33826](https://github.com/sgl-project/sglang/pull/33826)
  Revert "Warn on risky serving-time Triton work" (#33826)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/utils/triton_load_watch.py`, `test/registered/unit/utils/test_triton_load_watch.py`_
- **2026-08-06** [`d9b1cba255`](https://github.com/sgl-project/sglang/commit/d9b1cba255) [#33214](https://github.com/sgl-project/sglang/pull/33214)
  Fix DeepSeek-OCR batching crash on variable local-crop counts (#33214)
  _Files: `python/sglang/srt/models/deepseek_ocr.py`, `test/registered/xpu/test_deepseek_ocr.py`_
- **2026-08-05** [`a3a1ebc7b7`](https://github.com/sgl-project/sglang/commit/a3a1ebc7b7) [#33120](https://github.com/sgl-project/sglang/pull/33120)
  Warn on risky serving-time Triton work (#33120)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/utils/triton_load_watch.py`, `test/registered/unit/utils/test_triton_load_watch.py`_
- **2026-08-05** [`5c4f72f92a`](https://github.com/sgl-project/sglang/commit/5c4f72f92a) [#31300](https://github.com/sgl-project/sglang/pull/31300)
  [Build] Add srt_empty extra group for device-agnostic install (#31300)
  _Files: `python/pyproject_other.toml`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/server_args.py`, `test/registered/core/test_srt_empty_deps.py`_
- **2026-08-05** [`96c89863a3`](https://github.com/sgl-project/sglang/commit/96c89863a3) [#33595](https://github.com/sgl-project/sglang/pull/33595)
  Measure prefill busy time between launches (#33595)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-08-05** [`a6e5fa7081`](https://github.com/sgl-project/sglang/commit/a6e5fa7081) [#33403](https://github.com/sgl-project/sglang/pull/33403)
  [Scheduler] Honor explicit min-free-slots thresholds (#33403)
  _Files: `python/sglang/srt/managers/min_free_slots_delayer.py`, `python/sglang/srt/server_args.py`, `test/registered/scheduler/test_min_free_slots_delayer.py`_
- **2026-08-05** [`a0b04dbe4c`](https://github.com/sgl-project/sglang/commit/a0b04dbe4c) [#32588](https://github.com/sgl-project/sglang/pull/32588)
  feat(grpc): add generation request semantics (#32588)
  _Files: `proto/sglang/runtime/v1/sglang.proto`, `python/sglang/srt/entrypoints/grpc_bridge.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/io_struct.py` _+6 more__
- **2026-08-04** [`38dc2d6cf8`](https://github.com/sgl-project/sglang/commit/38dc2d6cf8) [#32734](https://github.com/sgl-project/sglang/pull/32734)
  [metrics] Split tokenizer request metrics by stream (#32734)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/observability/metrics_collector.py`_
- **2026-08-04** [`5081c063c0`](https://github.com/sgl-project/sglang/commit/5081c063c0) [#33562](https://github.com/sgl-project/sglang/pull/33562)
  fix(metrics): clear forward occupancy on idle (#33562)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`_
- **2026-08-04** [`7dd8a3d5ea`](https://github.com/sgl-project/sglang/commit/7dd8a3d5ea) [#33467](https://github.com/sgl-project/sglang/pull/33467)
  [CI] Fix scheduler max new tokens test fixture (#33467)
  _Files: `test/registered/unit/managers/test_scheduler_init_req_max_new_tokens.py`_
- **2026-08-04** [`91fae8a72c`](https://github.com/sgl-project/sglang/commit/91fae8a72c) [#33448](https://github.com/sgl-project/sglang/pull/33448)
  [DCP] Bound a request by the aggregate KV pool, not one rank's share (#33448)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`_
- **2026-08-03** [`bc7e1a07c3`](https://github.com/sgl-project/sglang/commit/bc7e1a07c3) [#32880](https://github.com/sgl-project/sglang/pull/32880)
  Bound prefill delayer all-branch delay and decay the max_prefill_bs high-watermark (#32880)
  _Files: `python/sglang/srt/managers/prefill_delayer.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/scheduler/test_prefill_delayer.py`_
- **2026-08-03** [`aa3bbbc6e8`](https://github.com/sgl-project/sglang/commit/aa3bbbc6e8) [#33337](https://github.com/sgl-project/sglang/pull/33337)
  observability: publish the generated forward-pass-metrics endpoint to the bags (#33337)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`, `test/registered/unit/test_server_args_writer_ratchet.py`_
- **2026-08-03** [`0b3e8bedd1`](https://github.com/sgl-project/sglang/commit/0b3e8bedd1) [#33336](https://github.com/sgl-project/sglang/pull/33336)
  config: keep runtime hicache and weight-version updates off ServerArgs (#33336)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/grpc_bridge.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/realtime/session.py` _+12 more__
- **2026-08-03** [`c844244da5`](https://github.com/sgl-project/sglang/commit/c844244da5) [#33105](https://github.com/sgl-project/sglang/pull/33105)
  support dp attn with client lb (#33105)
  _Files: `python/sglang/srt/managers/rust_server.py`, `python/sglang/srt/server_args.py`_

## Triton / Kernels  (21 commits)

- **2026-08-10** [`3bb72bc72a`](https://github.com/sgl-project/sglang/commit/3bb72bc72a) [#34231](https://github.com/sgl-project/sglang/pull/34231)
  [CI] Keep the torch compilation cache instead of wiping it on install (#34231)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-08-10** [`7331287c1c`](https://github.com/sgl-project/sglang/commit/7331287c1c) [#26671](https://github.com/sgl-project/sglang/pull/26671)
  [JIT Kernel][DSv4] Optimize epilogue of c128 (#26671)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c128_v2.cuh`_
- **2026-08-10** [`25b7015064`](https://github.com/sgl-project/sglang/commit/25b7015064) [#34184](https://github.com/sgl-project/sglang/pull/34184)
  Fix stale track rows corrupting conv checkpoints under the prefill graph (#34184)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/models_e2e/test_inkling_small_nvfp4.py`_
- **2026-08-08** [`db75dfe10f`](https://github.com/sgl-project/sglang/commit/db75dfe10f) [#33352](https://github.com/sgl-project/sglang/pull/33352)
  fix: always capture default prefill CUDA graph (#33352)
  _Files: `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `test/registered/unit/model_executor/model_runner_components/test_cuda_graph_setup.py`, `test/registered/unit/model_executor/test_prefill_cuda_graph_runner.py`_
- **2026-08-08** [`4ad5bb5d9a`](https://github.com/sgl-project/sglang/commit/4ad5bb5d9a) [#33400](https://github.com/sgl-project/sglang/pull/33400)
  [jit_kernel] Move JIT kernels into namespace sglang (#33400)
- **2026-08-07** [`9e3f6b746b`](https://github.com/sgl-project/sglang/commit/9e3f6b746b) [#33665](https://github.com/sgl-project/sglang/pull/33665)
  fix(mamba): widen causal_conv1d token offsets to int64 (#33665)
  _Files: `python/sglang/kernels/ops/mamba/causal_conv1d_triton.py`_
- **2026-08-07** [`5e60363960`](https://github.com/sgl-project/sglang/commit/5e60363960) [#33906](https://github.com/sgl-project/sglang/pull/33906)
  Fix prefill CP graph overflow with larger bucket search (#33906)
  _Files: `python/sglang/srt/layers/cp/bcg.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/cp/test_cp_strategy_unit.py`_
- **2026-08-07** [`afa79330b8`](https://github.com/sgl-project/sglang/commit/afa79330b8) [#33929](https://github.com/sgl-project/sglang/pull/33929)
  [misc] Remove break-graph debug log; reclaim pid-less /dev/shm leaks in CI (#33929)
  _Files: `python/sglang/srt/model_executor/runner_backend_utils/breakable_cuda_graph/breakable_cuda_graph.py`, `python/sglang/srt/utils/stale_shm_cleanup.py`, `test/registered/utils/test_stale_shm_cleanup.py`_
- **2026-08-06** [`f8f2870a84`](https://github.com/sgl-project/sglang/commit/f8f2870a84) [#24370](https://github.com/sgl-project/sglang/pull/24370)
  Profiling Enhancements [1/3]: cuda graph profile traces (#24370)
  _Files: `docs/docs/developer_guide/benchmark_and_profiling.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_backend/full_cuda_graph_backend.py` _+3 more__
- **2026-08-06** [`efc99a86ff`](https://github.com/sgl-project/sglang/commit/efc99a86ff) [#33847](https://github.com/sgl-project/sglang/pull/33847)
  [CI] Restore the full prefill CUDA graph capture range in test launches (#33847)
  _Files: `python/sglang/test/test_utils.py`_
- **2026-08-06** [`f9b954ddb1`](https://github.com/sgl-project/sglang/commit/f9b954ddb1) [#33772](https://github.com/sgl-project/sglang/pull/33772)
  [CI] Temporarily disable prefill cuda graph for qwen3.5 nightly test (#33772)
  _Files: `test/registered/8-gpu-models/test_qwen35.py`_
- **2026-08-05** [`2d27133fcf`](https://github.com/sgl-project/sglang/commit/2d27133fcf) [#33757](https://github.com/sgl-project/sglang/pull/33757)
  [CI] Skip `apt-get` when the required packages are already installed (#33757)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-08-05** [`4a3d6ca88c`](https://github.com/sgl-project/sglang/commit/4a3d6ca88c) [#33637](https://github.com/sgl-project/sglang/pull/33637)
  [CI] Skip sglang-kernel and sgl-deep-gemm reinstall on version match (#33637)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-08-05** [`1033cae8d5`](https://github.com/sgl-project/sglang/commit/1033cae8d5) [#33619](https://github.com/sgl-project/sglang/pull/33619)
  [CI] Speed up dependency install: dual-ABI Rust ext cache and prevalidation pruning (#33619)
  _Files: `.github/actions/download-rust-ext/action.yml`, `.github/workflows/_pr-test-rust-ext-build.yml`, `.github/workflows/seed-rust-ext-cache.yml`, `.pre-commit-config.yaml` _+7 more__
- **2026-08-04** [`dea2be5ae3`](https://github.com/sgl-project/sglang/commit/dea2be5ae3) [#33553](https://github.com/sgl-project/sglang/pull/33553)
  [CUDA Graph] Allow custom decode graph runners (#33553)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `test/registered/unit/model_executor/model_runner_components/test_cuda_graph_setup.py`_
- **2026-08-04** [`23ea7b6481`](https://github.com/sgl-project/sglang/commit/23ea7b6481) [#30741](https://github.com/sgl-project/sglang/pull/30741)
  Prewarm DSV4 MHC post kernel at model load (#30741)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-08-04** [`157401f050`](https://github.com/sgl-project/sglang/commit/157401f050) [#33460](https://github.com/sgl-project/sglang/pull/33460)
  [CI] Build the Rust extensions on the 5090 pool and seed the cache from main (#33460)
  _Files: `.github/workflows/_pr-test-rust-ext-build.yml`, `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/seed-rust-ext-cache.yml` _+3 more__
- **2026-08-03** [`7eb27372b3`](https://github.com/sgl-project/sglang/commit/7eb27372b3) [#30206](https://github.com/sgl-project/sglang/pull/30206)
  fix(server): capture legal multi-request prefill CUDA graph batches (#30206)
  _Files: `python/sglang/srt/model_executor/cuda_graph_config.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/server_args.py`_
- **2026-08-03** [`c949e91f18`](https://github.com/sgl-project/sglang/commit/c949e91f18) [#33441](https://github.com/sgl-project/sglang/pull/33441)
  [CI] Remove the orphaned site-packages sglang skeleton that shadows the checkout (#33441)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-08-03** [`22c2e2bcad`](https://github.com/sgl-project/sglang/commit/22c2e2bcad) [#33361](https://github.com/sgl-project/sglang/pull/33361)
  [CI] Persist the cargo build cache across CUDA CI jobs (#33361)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-08-03** [`28a2472f95`](https://github.com/sgl-project/sglang/commit/28a2472f95) [#32910](https://github.com/sgl-project/sglang/pull/32910)
  [DeepSeek-V4] Fix nvcc 13 crash building the topk_v2 kernel (#32910)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`_

## KV Cache / Memory  (19 commits)

- **2026-08-10** [`3c533acec6`](https://github.com/sgl-project/sglang/commit/3c533acec6) [#33639](https://github.com/sgl-project/sglang/pull/33639)
  [Hicache][2/2]Support Mamba branching in Unified Radix Cache with HiCache (#33639)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/unified_cache/components/mamba_component.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py`, `python/sglang/srt/mem_cache/unified_cache/components/tree_component.py` _+3 more__
- **2026-08-09** [`b4284f3eb7`](https://github.com/sgl-project/sglang/commit/b4284f3eb7) [#34096](https://github.com/sgl-project/sglang/pull/34096)
  config: the KV-cache configurator reads the bags (#34096)
  _Files: `python/sglang/srt/mem_cache/allocation_sizing.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/runtime_context.py`, `test/registered/dcp/test_dcp_layout_unit.py` _+2 more__
- **2026-08-08** [`cfb354bcfc`](https://github.com/sgl-project/sglang/commit/cfb354bcfc) [#34067](https://github.com/sgl-project/sglang/pull/34067)
  [Bugfix] Fix batched KV free aliasing (#34067)
  _Files: `python/sglang/srt/hardware_backend/npu/allocator_npu.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/hisparse.py`, `python/sglang/srt/mem_cache/allocator/paged.py` _+7 more__
- **2026-08-07** [`3dc91366ac`](https://github.com/sgl-project/sglang/commit/3dc91366ac) [#33777](https://github.com/sgl-project/sglang/pull/33777)
  [HiCache] write_back: reclaim duplicated host copy first under host pressure (#33777)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-08-07** [`12de7fb1f6`](https://github.com/sgl-project/sglang/commit/12de7fb1f6) [#33468](https://github.com/sgl-project/sglang/pull/33468)
  Remove the HiMambaRadixTree that is no longer in use (#33468)
  _Files: `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/mamba_checkpoint_pool.py`, `python/sglang/srt/mem_cache/storage/nixl/README.md` _+2 more__
- **2026-08-07** [`0756a1d2b0`](https://github.com/sgl-project/sglang/commit/0756a1d2b0) [#33975](https://github.com/sgl-project/sglang/pull/33975)
  Move SWA chunk-cap hatch tests into the registered suite (#33975)
  _Files: `test/manual/test_schedule_policy.py`, `test/registered/unit/managers/test_prefill_adder.py`_
- **2026-08-07** [`4d4f8023c4`](https://github.com/sgl-project/sglang/commit/4d4f8023c4) [#33475](https://github.com/sgl-project/sglang/pull/33475)
  [srt] Batch scheduler cache frees (#33475)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/mem_cache/allocator/swa.py`, `python/sglang/srt/mem_cache/radix_cache.py` _+2 more__
- **2026-08-06** [`2fc557254b`](https://github.com/sgl-project/sglang/commit/2fc557254b) [#33666](https://github.com/sgl-project/sglang/pull/33666)
  fix(PP): size the mamba pool per pipeline stage, not per whole model (#33666)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `test/registered/unit/mem_cache/test_mamba_donated_alloc_ratio.py`_
- **2026-08-06** [`21225aba3d`](https://github.com/sgl-project/sglang/commit/21225aba3d) [#32700](https://github.com/sgl-project/sglang/pull/32700)
  [Scheduler] Fix to restrict the SWA chunk-cap escape hatch to true head-of-line livelock (#32700)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `test/manual/test_schedule_policy.py`, `test/registered/unit/managers/test_prefill_adder.py`_
- **2026-08-06** [`f6de147b8d`](https://github.com/sgl-project/sglang/commit/f6de147b8d) [#33613](https://github.com/sgl-project/sglang/pull/33613)
  Remove revoke queue after hit-then-alloc refactoring (#33613)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-08-06** [`dea07b348b`](https://github.com/sgl-project/sglang/commit/dea07b348b) [#33825](https://github.com/sgl-project/sglang/pull/33825)
  [AMD] Update amd k3 cookbook for fp8 kv cache (#33825)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-08-06** [`64eeb153df`](https://github.com/sgl-project/sglang/commit/64eeb153df)
  config: resolve the draft worker's config per runner, not on a copy
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+12 more__
- **2026-08-05** [`106bcc1293`](https://github.com/sgl-project/sglang/commit/106bcc1293) [#32388](https://github.com/sgl-project/sglang/pull/32388)
  Observability enhancement for HiCache (#32388)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py` _+8 more__
- **2026-08-05** [`5f79cf3511`](https://github.com/sgl-project/sglang/commit/5f79cf3511) [#33348](https://github.com/sgl-project/sglang/pull/33348)
  [DCP] Match the replicated draft KV pool's page granularity to its allocator (#33348)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`_
- **2026-08-05** [`b1bd871df5`](https://github.com/sgl-project/sglang/commit/b1bd871df5) [#33580](https://github.com/sgl-project/sglang/pull/33580)
  [Unified Radix Cache] Complete the tree-core interface boundary (#33580)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/README.md`, `python/sglang/srt/mem_cache/unified_cache/components/mamba_component.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py` _+1 more__
- **2026-08-05** [`99709f734d`](https://github.com/sgl-project/sglang/commit/99709f734d) [#32415](https://github.com/sgl-project/sglang/pull/32415)
  [VLM] split multimodal scheduling from mm_utils (#32415)
  _Files: `python/sglang/srt/managers/mm_schedule.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `test/registered/chunked_prefill/test_mm_chunked_embedding_unit.py`_
- **2026-08-05** [`29831d58ef`](https://github.com/sgl-project/sglang/commit/29831d58ef) [#32895](https://github.com/sgl-project/sglang/pull/32895)
  fix mm-chunk-embedding test suite (#32895)
  _Files: `test/registered/chunked_prefill/test_mm_chunked_embedding_unit.py`_
- **2026-08-04** [`c8822fd990`](https://github.com/sgl-project/sglang/commit/c8822fd990) [#33598](https://github.com/sgl-project/sglang/pull/33598)
  Clarify post-capture KV reservation logs (#33598)
  _Files: `python/sglang/srt/mem_cache/kv_vmm_backing.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/swa_memory_pool.py`_
- **2026-08-04** [`572924634b`](https://github.com/sgl-project/sglang/commit/572924634b) [#32575](https://github.com/sgl-project/sglang/pull/32575)
  [mem_cache] Build empty-prefix last_loc sentinel on-device to avoid per-call H2D sync (#32575)
  _Files: `python/sglang/srt/mem_cache/allocation.py`_

## CI / Build  (17 commits)

- **2026-08-10** [`410088c91e`](https://github.com/sgl-project/sglang/commit/410088c91e) [#34103](https://github.com/sgl-project/sglang/pull/34103)
  [NPU] Increase the retry count to 3 for the GSM8K. (#34103)
  _Files: `.github/workflows/_npu-single-node-test-stage.yml`, `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`_
- **2026-08-09** [`1ebd6fab6c`](https://github.com/sgl-project/sglang/commit/1ebd6fab6c) [#34145](https://github.com/sgl-project/sglang/pull/34145)
  [CI] Gate Kimi-K3 acceptance length on the GSM8K average (#34145)
  _Files: `test/registered/models_e2e/test_kimi_k3_b300.py`_
- **2026-08-08** [`c2d90db1e3`](https://github.com/sgl-project/sglang/commit/c2d90db1e3) [#34089](https://github.com/sgl-project/sglang/pull/34089)
  [CI] Add Kimi-K3 low-latency performance check (#34089)
  _Files: `test/registered/models_e2e/test_kimi_k3_b300.py`_
- **2026-08-08** [`c9444deef4`](https://github.com/sgl-project/sglang/commit/c9444deef4) [#34041](https://github.com/sgl-project/sglang/pull/34041)
  Docker: install DeepEP from release wheels (#34041)
  _Files: `.github/workflows/_docker-build-and-publish.yml`, `.github/workflows/nightly-72-gpu-gb200.yml`, `.github/workflows/release-docker-dev.yml`, `docker/Dockerfile`_
- **2026-08-08** [`633838b0ec`](https://github.com/sgl-project/sglang/commit/633838b0ec) [#34009](https://github.com/sgl-project/sglang/pull/34009)
  Add the 8-gpu Inkling consistency test (#34009)
  _Files: `test/registered/8-gpu-models/test_inkling_nvfp4_nightly.py`_
- **2026-08-07** [`8a22b8305d`](https://github.com/sgl-project/sglang/commit/8a22b8305d) [#33956](https://github.com/sgl-project/sglang/pull/33956)
  docker: add Kimi K3 artifacts and build hpc-ops with C++20 (#33956)
  _Files: `docker/Dockerfile`_
- **2026-08-07** [`163b739b34`](https://github.com/sgl-project/sglang/commit/163b739b34) [#33904](https://github.com/sgl-project/sglang/pull/33904)
  [CI] Refresh the CPU HF cache base only on main-ref runs (#33904)
  _Files: `.github/workflows/_pr-test-stage-cpu.yml`_
- **2026-08-06** [`e0af47b03e`](https://github.com/sgl-project/sglang/commit/e0af47b03e) [#33866](https://github.com/sgl-project/sglang/pull/33866)
  Fix sgl-deep-ep builder dependencies (#33866)
  _Files: `.github/workflows/release-whl-deepep.yml`, `docker/sgl-deep-ep.Dockerfile`, `scripts/build_sgl_deepep.sh`_
- **2026-08-06** [`ba9074035a`](https://github.com/sgl-project/sglang/commit/ba9074035a) [#33498](https://github.com/sgl-project/sglang/pull/33498)
  Build and release sgl-deep-ep wheels (#33498)
  _Files: `.github/workflows/release-whl-deepep.yml`, `docker/sgl-deep-ep.Dockerfile`, `scripts/build_sgl_deepep.sh`, `scripts/update_deepep_whl_index.py`_
- **2026-08-06** [`ae5f8c94b7`](https://github.com/sgl-project/sglang/commit/ae5f8c94b7) [#32390](https://github.com/sgl-project/sglang/pull/32390)
  ci(xpu): harden nightly + PR XPU CI (HF login / tag fetch / docker push retries) (#32390)
  _Files: `.github/workflows/nightly-test-intel.yml`, `.github/workflows/pr-test-xpu.yml`, `.github/workflows/release-docker-intel-xpu-nightly.yml`_
- **2026-08-05** [`25035bff8d`](https://github.com/sgl-project/sglang/commit/25035bff8d) [#33760](https://github.com/sgl-project/sglang/pull/33760)
  Use main branch in Kimi Dockerfiles (#33760)
  _Files: `docker/kimi_k3/kimi_k3_cu12.Dockerfile`, `docker/kimi_k3/kimi_k3_cu13.Dockerfile`_
- **2026-08-05** [`98ed5554bb`](https://github.com/sgl-project/sglang/commit/98ed5554bb) [#33675](https://github.com/sgl-project/sglang/pull/33675)
  Stop testing cu129 DeepGEMM wheels (#33675)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-08-05** [`eac1f78568`](https://github.com/sgl-project/sglang/commit/eac1f78568) [#33644](https://github.com/sgl-project/sglang/pull/33644)
  [CI] Free hosted-runner disk space only when it is low (#33644)
  _Files: `.github/workflows/_pr-test-stage-cpu.yml`, `.github/workflows/rerun-test.yml`_
- **2026-08-04** [`26a542722f`](https://github.com/sgl-project/sglang/commit/26a542722f) [#33512](https://github.com/sgl-project/sglang/pull/33512)
  [CI] Replace the rust-ext-build venv instead of failing when it exists (#33512)
  _Files: `.github/workflows/_pr-test-rust-ext-build.yml`_
- **2026-08-04** [`7ba393dd15`](https://github.com/sgl-project/sglang/commit/7ba393dd15) [#33461](https://github.com/sgl-project/sglang/pull/33461)
  [CI] Dispatch base-a-test-cpu through its own reusable stage workflow (#33461)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/_pr-test-stage-cpu.yml`, `.github/workflows/pr-test.yml`, `scripts/ci/utils/compute_partitions.py`_
- **2026-08-03** [`7cd79fda56`](https://github.com/sgl-project/sglang/commit/7cd79fda56) [#33410](https://github.com/sgl-project/sglang/pull/33410)
  [CI] Skip absent inline suites when loading timeouts (#33410)
  _Files: `scripts/ci/utils/compute_partitions.py`_
- **2026-08-03** [`fcc4de9e5f`](https://github.com/sgl-project/sglang/commit/fcc4de9e5f) [#33329](https://github.com/sgl-project/sglang/pull/33329)
  [CI] Size the CPU stage from the live partition model (#33329)
  _Files: `.github/workflows/pr-test.yml`, `scripts/ci/utils/compute_partitions.py`_

## Quantization  (15 commits)

- **2026-08-10** [`d6a066131c`](https://github.com/sgl-project/sglang/commit/d6a066131c) [#34222](https://github.com/sgl-project/sglang/pull/34222)
  [Feature] Support NVFP4 token embedding in ModelOpt mixed-precision checkpoints (#34222)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/quant/test_nvfp4_embedding.py`_
- **2026-08-09** [`f6cbdc1dd1`](https://github.com/sgl-project/sglang/commit/f6cbdc1dd1) [#34143](https://github.com/sgl-project/sglang/pull/34143)
  docs(diffusion): refresh skills for latest runtime (#34143)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md` _+3 more__
- **2026-08-07** [`fc9479243e`](https://github.com/sgl-project/sglang/commit/fc9479243e) [#32120](https://github.com/sgl-project/sglang/pull/32120)
  [AMD][DI][CI] 8/N Add GLM-5.2 MXFP4 1P1D DI/CI recipes (base + MTP + DP8/EP8) (#32120)
  _Files: `scripts/ci/slurm/nightly-configs.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/glm52/1k1k/1p1d-dp8ep8-mtp.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/glm52/1k1k/1p1d-dp8ep8.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/glm52/1k1k/1p1d-mtp.yaml` _+1 more__
- **2026-08-07** [`914644e81c`](https://github.com/sgl-project/sglang/commit/914644e81c) [#33875](https://github.com/sgl-project/sglang/pull/33875)
  [diffusion] fix: fix 4/8-step distilled minimax-h3 turbo lora merge (#33875)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/lora/linear.py` _+1 more__
- **2026-08-06** [`8b29c90218`](https://github.com/sgl-project/sglang/commit/8b29c90218) [#33617](https://github.com/sgl-project/sglang/pull/33617)
  [NVIDIA] Enable CuTe DSL BF16 GEMM on SM107 (#33617)
  _Files: `python/sglang/kernels/ops/gemm/cutedsl_bf16_gemm.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/server_args.py`, `test/registered/kernels/ops/gemm/test_cutedsl_bf16_gemm.py`_
- **2026-08-06** [`fe55d78b7d`](https://github.com/sgl-project/sglang/commit/fe55d78b7d) [#33500](https://github.com/sgl-project/sglang/pull/33500)
  Fix MXFP4 scale placeholder initialization (#33500)
  _Files: `python/sglang/srt/layers/quantization/mxfp4.py`_
- **2026-08-06** [`fc74c35546`](https://github.com/sgl-project/sglang/commit/fc74c35546) [#33469](https://github.com/sgl-project/sglang/pull/33469)
  kernels: scalar scale A support for fp8_gemm (#33469)
  _Files: `python/sglang/kernels/aot/benchmark/bench_fp8_gemm.py`, `python/sglang/kernels/aot/csrc/gemm/fp8_gemm_kernel.cu`, `python/sglang/kernels/aot/tests/test_fp8_gemm.py`_
- **2026-08-06** [`269d51ed4b`](https://github.com/sgl-project/sglang/commit/269d51ed4b) [#33750](https://github.com/sgl-project/sglang/pull/33750)
  [Fix] Inkling works with gs:// runai_streamer paths (#33750)
  _Files: `python/sglang/srt/models/inkling_common/quantization/config.py`_
- **2026-08-06** [`65d5a0ec25`](https://github.com/sgl-project/sglang/commit/65d5a0ec25) [#32538](https://github.com/sgl-project/sglang/pull/32538)
  Support ModelOpt MXFP8 checkpoints (#32538)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/quantization/base_config.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py` _+2 more__
- **2026-08-05** [`988c6e6aeb`](https://github.com/sgl-project/sglang/commit/988c6e6aeb) [#33621](https://github.com/sgl-project/sglang/pull/33621)
  Pin online NVFP4 4over6 quantization settings (#33621)
  _Files: `python/sglang/srt/model_loader/loader.py`_
- **2026-08-04** [`a0b3f1dde6`](https://github.com/sgl-project/sglang/commit/a0b3f1dde6) [#33596](https://github.com/sgl-project/sglang/pull/33596)
  [Test] Replace GEMM backend e2e matrices with layer-level unit tests (#33596)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `test/registered/quant/test_fp8_blockwise_gemm.py`, `test/registered/quant/test_fp8_gemm_sm120.py`, `test/registered/quant/test_nvfp4_gemm.py` _+2 more__
- **2026-08-04** [`eaf5c29cc5`](https://github.com/sgl-project/sglang/commit/eaf5c29cc5) [#33402](https://github.com/sgl-project/sglang/pull/33402)
  [AMD] Enable block-fp8 + quick INT4 all-reduce in MiniMax-M3 MI35x nightly Test (#33402)
  _Files: `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`_
- **2026-08-04** [`a84e70eb1e`](https://github.com/sgl-project/sglang/commit/a84e70eb1e) [#33333](https://github.com/sgl-project/sglang/pull/33333)
  [AMD][DI][CI] 6/N Add Kimi-K2.6 MXFP4 wide-EP16 2P1D nightly recipes (#33333)
  _Files: `scripts/ci/slurm/launch_mi355x.sh`, `scripts/ci/slurm/nightly-configs.yaml`, `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/2p1d-ep16-mtp-mxfp4.yaml`, `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/2p1d-ep16-mxfp4.yaml`_
- **2026-08-03** [`0bf0640b9d`](https://github.com/sgl-project/sglang/commit/0bf0640b9d) [#33136](https://github.com/sgl-project/sglang/pull/33136)
  [CP] Support breakable CUDA graphs for zigzag strategy (#33136)
  _Files: `python/sglang/srt/layers/cp/bcg.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-08-03** [`b64fd800d4`](https://github.com/sgl-project/sglang/commit/b64fd800d4) [#33282](https://github.com/sgl-project/sglang/pull/33282)
  docs(diffusion): update skills for MiniMax-H3 (#33282)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/references/testing-and-accuracy.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md` _+4 more__

## Speculative Decoding  (11 commits)

- **2026-08-10** [`430f38ea25`](https://github.com/sgl-project/sglang/commit/430f38ea25) [#34250](https://github.com/sgl-project/sglang/pull/34250)
  Update dspark draft path in Inkling small cookbook (#34250)
  _Files: `docs/cookbook/autoregressive/ThinkingMachines/Inkling-Small.mdx`, `docs/src/snippets/configs/thinkingmachines/inkling-small.jsx`_
- **2026-08-07** [`b2f9603f93`](https://github.com/sgl-project/sglang/commit/b2f9603f93) [#33758](https://github.com/sgl-project/sglang/pull/33758)
  [bugfix] Stop/EOS inside a spec accept run beats the max_new_tokens finish (#33758)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_finish_length_speculative.py`_
- **2026-08-06** [`dd7e4c91e2`](https://github.com/sgl-project/sglang/commit/dd7e4c91e2) [#33785](https://github.com/sgl-project/sglang/pull/33785)
  Fix Mistral-Large-3 EAGLE draft skipping DeepseekV2Model.__init__ (#33785)
  _Files: `python/sglang/srt/models/mistral_large_3_eagle.py`, `test/registered/8-gpu-models/test_mistral_large3.py`_
- **2026-08-06** [`9bd1461757`](https://github.com/sgl-project/sglang/commit/9bd1461757) [#33776](https://github.com/sgl-project/sglang/pull/33776)
  [CI] Bound the CUDA graph capture range in test launches and lift the spec fixture's admission cap (#33776)
  _Files: `python/sglang/test/server_fixtures/spec_eagle_fixture.py`, `python/sglang/test/test_utils.py`, `test/registered/cpu/test_spec_eagle_cpu.py`, `test/registered/cpu/test_spec_eagle_parity_cpu.py` _+5 more__
- **2026-08-06** [`ceaeca0b9e`](https://github.com/sgl-project/sglang/commit/ceaeca0b9e) [#33748](https://github.com/sgl-project/sglang/pull/33748)
  [Fix] Vocab out of bounds in DSpark for Inkling-Small (#33748)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-08-05** [`de34dd11e9`](https://github.com/sgl-project/sglang/commit/de34dd11e9) [#33745](https://github.com/sgl-project/sglang/pull/33745)
  [CI] Fold duplicate-server suites and prune the retract matrix on 1-gpu-5090 (#33745)
  _Files: `python/sglang/test/kits/anthropic_messages_kit.py`, `python/sglang/test/kits/json_mode_kit.py`, `test/registered/constrained_decoding/test_constrained_decoding.py`, `test/registered/model_loading/test_weight_cache_daemon.py` _+7 more__
- **2026-08-04** [`0d99d91e49`](https://github.com/sgl-project/sglang/commit/0d99d91e49) [#33605](https://github.com/sgl-project/sglang/pull/33605)
  [CI] Make B200 base-b suites single-GPU as prep for 1-gpu B200 runners (#33605)
  _Files: `test/registered/kernels/ops/kimi_k3/test_collectives.py`, `test/registered/spec/eagle/test_deepseek_v3_fp4_mtp_small.py`_
- **2026-08-04** [`53804d609c`](https://github.com/sgl-project/sglang/commit/53804d609c) [#32438](https://github.com/sgl-project/sglang/pull/32438)
  [CI][XPU] Stabilize XPU CI: pin UMD/IGC, retry infra flakes, right-size EAGLE3 (#32438)
  _Files: `.github/workflows/pr-test-xpu.yml`, `docker/xpu.Dockerfile`, `python/sglang/test/ci/ci_utils.py`, `python/sglang/test/test_utils.py` _+2 more__
- **2026-08-04** [`154f0ac662`](https://github.com/sgl-project/sglang/commit/154f0ac662) [#33098](https://github.com/sgl-project/sglang/pull/33098)
  Fix DSpark and DP/EP (#33098)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_draft.py`, `test/registered/spec/dspark/test_dspark_dp_tier.py`_
- **2026-08-03** [`9bc8848fcf`](https://github.com/sgl-project/sglang/commit/9bc8848fcf) [#33335](https://github.com/sgl-project/sglang/pull/33335)
  spec: build every draft worker from a draft ServerArgs copy (#33335)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/draft_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` _+6 more__
- **2026-08-03** [`2a7a299c27`](https://github.com/sgl-project/sglang/commit/2a7a299c27) [#33298](https://github.com/sgl-project/sglang/pull/33298)
  [Spec] Support sampling in the DSPARK graph-folded draft proposal (#33298)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_

## ROCm / AMD  (11 commits)

- **2026-08-09** [`967cac801c`](https://github.com/sgl-project/sglang/commit/967cac801c) [#34147](https://github.com/sgl-project/sglang/pull/34147)
  [AMD] [CI] Register the DeepSeek-V4-Pro-DSpark MI35x nightly job so its suite actually runs (#34147)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`_
- **2026-08-06** [`b38caebf09`](https://github.com/sgl-project/sglang/commit/b38caebf09) [#32466](https://github.com/sgl-project/sglang/pull/32466)
  [AMD] Enable gfx1250 sgl-kernel builds (#32466)
  _Files: `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce_base.h`, `python/sglang/kernels/aot/setup_rocm.py`_
- **2026-08-06** [`dfe53232d7`](https://github.com/sgl-project/sglang/commit/dfe53232d7) [#33809](https://github.com/sgl-project/sglang/pull/33809)
  [AMD] Move test_load_weights_from_remote_instance.py to extra CI (#33809)
  _Files: `test/registered/model_loading/test_load_weights_from_remote_instance.py`_
- **2026-08-06** [`c11ce7c514`](https://github.com/sgl-project/sglang/commit/c11ce7c514) [#33842](https://github.com/sgl-project/sglang/pull/33842)
  chore: bump sgl-kernel version to 0.4.6.post1 (#33842)
  _Files: `python/sglang/kernels/aot/pyproject.toml`, `python/sglang/kernels/aot/pyproject_cpu.toml`, `python/sglang/kernels/aot/pyproject_musa.toml`, `python/sglang/kernels/aot/pyproject_rocm.toml` _+1 more__
- **2026-08-06** [`407a65d3cb`](https://github.com/sgl-project/sglang/commit/407a65d3cb) [#33753](https://github.com/sgl-project/sglang/pull/33753)
  [AMD] [CI] Track the MI355X disagg nightly in the AMD CI job monitor (#33753)
  _Files: `.github/workflows/amd-ci-job-monitor.yml`_
- **2026-08-06** [`e675c7226a`](https://github.com/sgl-project/sglang/commit/e675c7226a) [#33774](https://github.com/sgl-project/sglang/pull/33774)
  [AMD]Stage MI355X nightly by node count (#33774)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-08-06** [`c952ee5ac1`](https://github.com/sgl-project/sglang/commit/c952ee5ac1) [#33678](https://github.com/sgl-project/sglang/pull/33678)
  chore: bump sgl-kernel version to 0.4.6 (#33678)
  _Files: `python/sglang/kernels/aot/pyproject.toml`, `python/sglang/kernels/aot/pyproject_cpu.toml`, `python/sglang/kernels/aot/pyproject_musa.toml`, `python/sglang/kernels/aot/pyproject_rocm.toml` _+1 more__
- **2026-08-05** [`1478cdec9f`](https://github.com/sgl-project/sglang/commit/1478cdec9f) [#33599](https://github.com/sgl-project/sglang/pull/33599)
  [AMD] Fuse Kimi-K3 attn-residual aggregation (#33599)
  _Files: `python/sglang/kernels/ops/kimi_k3/attn_res_hip.py`, `python/sglang/srt/layers/attn_residual.py`_
- **2026-08-04** [`b327d76682`](https://github.com/sgl-project/sglang/commit/b327d76682) [#33462](https://github.com/sgl-project/sglang/pull/33462)
  [AMD] Bump mori to latest in sglang (#33462)
  _Files: `docker/rocm.Dockerfile`_
- **2026-08-04** [`03f44c978a`](https://github.com/sgl-project/sglang/commit/03f44c978a) [#33374](https://github.com/sgl-project/sglang/pull/33374)
  [AMD][DI][CI] Auto-mount  latest host ionic/ibverbs userspace in the MI355X nightly launcher (fix ABI mismatch) (#33374)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`, `scripts/ci/slurm/launch_mi355x.sh`_
- **2026-08-03** [`21d930aae3`](https://github.com/sgl-project/sglang/commit/21d930aae3) [#33195](https://github.com/sgl-project/sglang/pull/33195)
  [AMD] Fix JIT compile failure in sgl_kernel/warp.cuh (#33195)
  _Files: `python/sglang/kernels/jit/include/sgl_kernel/warp.cuh`_

## Tensor / Data Parallel  (7 commits)

- **2026-08-10** [`68b961e9fb`](https://github.com/sgl-project/sglang/commit/68b961e9fb) [#33630](https://github.com/sgl-project/sglang/pull/33630)
  Add kda replayssm tests (#33630)
  _Files: `test/registered/kernels/test_kda_mtp_cutedsl_replayssm_ring.py`, `test/registered/kernels/test_kda_replayssm_fold.py`, `test/registered/kernels/test_kda_replayssm_fold_batched.py`, `test/registered/kernels/test_kda_replayssm_ring_fused.py` _+1 more__
- **2026-08-09** [`fcc5468cce`](https://github.com/sgl-project/sglang/commit/fcc5468cce) [#34159](https://github.com/sgl-project/sglang/pull/34159)
  Fix deterministic inference all-reduce for tp>1 (#34159)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/server_args.py`_
- **2026-08-07** [`f9e6888b5a`](https://github.com/sgl-project/sglang/commit/f9e6888b5a) [#32900](https://github.com/sgl-project/sglang/pull/32900)
  [Distributed] Propagate semantic group names to PyTorch process groups (#32900)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `test/registered/unit/distributed/test_parallel_state.py`_
- **2026-08-07** [`2c3ecf32f1`](https://github.com/sgl-project/sglang/commit/2c3ecf32f1) [#33446](https://github.com/sgl-project/sglang/pull/33446)
  [Fix] Reformat /vertex_generate successful predictions (#33446)
  _Files: `python/sglang/srt/entrypoints/http_server.py`_
- **2026-08-06** [`1d47952c7c`](https://github.com/sgl-project/sglang/commit/1d47952c7c)
  config: pass the Ray placement group as a launch argument
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/ray/data_parallel_controller.py`, `python/sglang/srt/ray/engine.py`, `python/sglang/srt/ray/http_server.py` _+1 more__
- **2026-08-04** [`5e6c37f2b4`](https://github.com/sgl-project/sglang/commit/5e6c37f2b4) [#32678](https://github.com/sgl-project/sglang/pull/32678)
  [cuda_graph] Gate breakable-CG capture_inputs retention to DP-gather paths (#32678)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`_
- **2026-08-03** [`45c00daa1b`](https://github.com/sgl-project/sglang/commit/45c00daa1b) [#33351](https://github.com/sgl-project/sglang/pull/33351)
  [misc] Deep-merge nested config overrides and parse request bodies with orjson (#33351)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/utils/hf_transformers/config.py`_

## Serving / API  (7 commits)

- **2026-08-09** [`4792ab1e90`](https://github.com/sgl-project/sglang/commit/4792ab1e90) [#34146](https://github.com/sgl-project/sglang/pull/34146)
  [CI] Pin the rust frontend parity test to eager prefill (#34146)
  _Files: `test/registered/openai_server/basic/test_openai_completion_rust.py`_
- **2026-08-08** [`f3ed82b3a8`](https://github.com/sgl-project/sglang/commit/f3ed82b3a8) [#33913](https://github.com/sgl-project/sglang/pull/33913)
  [inkling] Let Anthropic thinking=disabled map to reasoning effort "none" (#33913)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-08-07** [`3c51e29deb`](https://github.com/sgl-project/sglang/commit/3c51e29deb) [#32689](https://github.com/sgl-project/sglang/pull/32689)
  Responses support (#32689)
  _Files: `python/sglang/srt/entrypoints/context.py`, `python/sglang/srt/entrypoints/harmony_utils.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py` _+5 more__
- **2026-08-06** [`d33ab39ebc`](https://github.com/sgl-project/sglang/commit/d33ab39ebc)
  config: template-detected parsers go to the engine's control-plane overlay
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py` _+1 more__
- **2026-08-05** [`059269594c`](https://github.com/sgl-project/sglang/commit/059269594c) [#33140](https://github.com/sgl-project/sglang/pull/33140)
  [DSV4] Add official DSV4 reasoning effort support (#33140)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/entrypoints/openai/chat_encoding.py`, `python/sglang/srt/entrypoints/openai/encoding_dsv4.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py` _+2 more__
- **2026-08-04** [`7adf2f4a9a`](https://github.com/sgl-project/sglang/commit/7adf2f4a9a) [#33538](https://github.com/sgl-project/sglang/pull/33538)
  Inline _set_gc into _set_envs_and_config (#33538)
  _Files: `python/sglang/srt/entrypoints/engine.py`_
- **2026-08-04** [`d257b58e67`](https://github.com/sgl-project/sglang/commit/d257b58e67) [#33548](https://github.com/sgl-project/sglang/pull/33548)
  [Router] Report accelerator count in /v1/loads (#33548)
  _Files: `python/sglang/srt/entrypoints/v1_loads.py`, `test/registered/unit/entrypoints/test_v1_loads_aggregate.py`_

## Docs / Examples  (6 commits)

- **2026-08-09** [`57f2105118`](https://github.com/sgl-project/sglang/commit/57f2105118) [#34097](https://github.com/sgl-project/sglang/pull/34097)
  docs(skill): record where config is read now that the seed is off limits (#34097)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`_
- **2026-08-07** [`0c3a76fa0a`](https://github.com/sgl-project/sglang/commit/0c3a76fa0a) [#33935](https://github.com/sgl-project/sglang/pull/33935)
  Clean GLM-5.2 NVFP4 cookbook (#33935)
  _Files: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-08-04** [`87ed82ff7e`](https://github.com/sgl-project/sglang/commit/87ed82ff7e) [#33612](https://github.com/sgl-project/sglang/pull/33612)
  Remove custom all-reduce disable from Kimi-K3 B300 recipe (#33612)
  _Files: `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-08-03** [`b819d2fb5b`](https://github.com/sgl-project/sglang/commit/b819d2fb5b) [#32123](https://github.com/sgl-project/sglang/pull/32123)
  [Docs] Rename docs_new/ to docs/ (#32123)
- **2026-08-03** [`e9366d7f79`](https://github.com/sgl-project/sglang/commit/e9366d7f79) [#33038](https://github.com/sgl-project/sglang/pull/33038)
  Updated b200 kimi-k3 cookbook (#33038)
  _Files: `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs_new/src/snippets/_deployment.jsx`, `docs_new/src/snippets/_playground.jsx`, `docs_new/src/snippets/configs/moonshotai/kimi-k3-benchmarks.jsx` _+1 more__
- **2026-08-03** [`85484c457d`](https://github.com/sgl-project/sglang/commit/85484c457d) [#33347](https://github.com/sgl-project/sglang/pull/33347)
  docs: refresh README news highlights (#33347)
  _Files: `README.md`_

## Models  (3 commits)

- **2026-08-09** [`bfeb9a8af2`](https://github.com/sgl-project/sglang/commit/bfeb9a8af2) [#22867](https://github.com/sgl-project/sglang/pull/22867)
  [feat] Add language_model_only parameter support for Qwen35 (#22867)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/utils/hf_transformers/processor.py`_
- **2026-08-07** [`115cd7bde1`](https://github.com/sgl-project/sglang/commit/115cd7bde1) [#32945](https://github.com/sgl-project/sglang/pull/32945)
  docs: update checkpoint to Qwen3.5 NVFP4 V2 for InfX (#32945)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-08-05** [`6fa3f9df11`](https://github.com/sgl-project/sglang/commit/6fa3f9df11) [#33671](https://github.com/sgl-project/sglang/pull/33671)
  [Bugfix] Treat unsharded model.safetensors as HF weights in Mistral-native format detection (#33671)
  _Files: `python/sglang/srt/server_args.py`_

## Structured Output  (2 commits)

- **2026-08-03** [`e00f32ed4f`](https://github.com/sgl-project/sglang/commit/e00f32ed4f) [#33103](https://github.com/sgl-project/sglang/pull/33103)
  feat: rust sglang server openai apis (#33103)
  _Files: `python/sglang/srt/managers/rust_server.py`, `rust/Cargo.lock`, `rust/rust-toolchain.toml`, `rust/sglang-server/Cargo.toml` _+24 more__
- **2026-08-03** [`f5f021672a`](https://github.com/sgl-project/sglang/commit/f5f021672a) [#33328](https://github.com/sgl-project/sglang/pull/33328)
  [Fix] Treat an empty grammar constraint as unset in SamplingParams (#33328)
  _Files: `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/sampling/sampling_params.py`, `test/registered/unit/constrained/test_grammar_manager.py`, `test/registered/unit/sampling/test_sampling_params.py`_

---
_Generated 2026-08-10 09:42 UTC_