# sgl-project/sglang — Weekly Change Report
**Period:** 2026-07-20 → 2026-07-27  |  **Total commits:** 277

## ✨ New Features This Week

- **2026-07-27** [#32489](https://github.com/sgl-project/sglang/pull/32489) — Add local ZIP uploader for whl releases (#32489)
- **2026-07-27** [#32078](https://github.com/sgl-project/sglang/pull/32078) — [feat] Opt-in flat response format for prompt top logprobs (#32078)
- **2026-07-27** [#30988](https://github.com/sgl-project/sglang/pull/30988) — [LoRA] Support LoRA under the breakable/full prefill CUDA graph (#30988)
- **2026-07-27** [#32375](https://github.com/sgl-project/sglang/pull/32375) — model: support EmbeddingGemma (#32375)
- **2026-07-26** [#32453](https://github.com/sgl-project/sglang/pull/32453) — Add oulgen to CI_PERMISSIONS.json (#32453)
- **2026-07-26** [#31189](https://github.com/sgl-project/sglang/pull/31189) — [NPU]Add Ascend transfer version compatibility. (#31189)
- **2026-07-26** [#32427](https://github.com/sgl-project/sglang/pull/32427) — add fill_draft_extend_prepare_buffers_native for NPU (#32427)
- **2026-07-26** [#32294](https://github.com/sgl-project/sglang/pull/32294) — [UT][NPU] add NPU attention unit tests for ascend_backend and ascend_dsv4_backend (#32294)
- **2026-07-26** [#32339](https://github.com/sgl-project/sglang/pull/32339) — [comm] Enable multi-node custom-AR v2 on a single NVLink clique (#32339)
- **2026-07-25** [#24256](https://github.com/sgl-project/sglang/pull/24256) — [core/loader] Add presharded load format (#24256)
- _…and 59 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-27** [`c6a6200a1a`](https://github.com/sgl-project/sglang/commit/c6a6200a1a) [#32469](https://github.com/sgl-project/sglang/pull/32469) — [AMD] Fix pip setup in AMD Miles nightly builds (#32469)
- **2026-07-26** [`833e1bc601`](https://github.com/sgl-project/sglang/commit/833e1bc601) [#31793](https://github.com/sgl-project/sglang/pull/31793) — [Fix][AMD] Qwen3.5 MoE: disable global-slot shared-expert fusion under per-rank EP backends (MoRI + dp-attention init crash) (#31793)
- **2026-07-26** [`1d0cd2e473`](https://github.com/sgl-project/sglang/commit/1d0cd2e473) [#30613](https://github.com/sgl-project/sglang/pull/30613) — [AMD] Nightly Test Coverage - Minimax-M3-MXFP8 Accuracy Test (#30613)
- **2026-07-25** [`6a046fad09`](https://github.com/sgl-project/sglang/commit/6a046fad09) [#31144](https://github.com/sgl-project/sglang/pull/31144) — [PD] Prevent decode scheduler from blocking on ZMQ sends to a stalled prefill peer (#31144)
- **2026-07-25** [`1ef2b85ef7`](https://github.com/sgl-project/sglang/commit/1ef2b85ef7) [#32347](https://github.com/sgl-project/sglang/pull/32347) — chore: bump docs install version to 0.5.16 (#32347)
- **2026-07-23** [`8ce68370b5`](https://github.com/sgl-project/sglang/commit/8ce68370b5) [#31757](https://github.com/sgl-project/sglang/pull/31757) — [AMD] Build Miles nightly ROCm images with docker/build.py and test ROCm 7.2 (#31757)
- **2026-07-22** [`40b2119b23`](https://github.com/sgl-project/sglang/commit/40b2119b23) [#31889](https://github.com/sgl-project/sglang/pull/31889) — [AMD] Cache AITER expert mask across decode (#31889)
- **2026-07-22** [`e8e765b9d6`](https://github.com/sgl-project/sglang/commit/e8e765b9d6) [#24651](https://github.com/sgl-project/sglang/pull/24651) — [AMD] Add fused all-reduce RMSNorm per-group quant for Qwen3.5 FP8 (#24651)
- **2026-07-22** [`71fe649d68`](https://github.com/sgl-project/sglang/commit/71fe649d68) [#32069](https://github.com/sgl-project/sglang/pull/32069) — [AMD] Register the Helios release workflow on main (#32069)
- **2026-07-21** [`2f4f2362fb`](https://github.com/sgl-project/sglang/commit/2f4f2362fb) [#31202](https://github.com/sgl-project/sglang/pull/31202) — Delete sgl-kernel AOT `bmm_fp8`, use `flashinfer.bmm_fp8` (#31202)
- **2026-07-21** [`dcd9014f15`](https://github.com/sgl-project/sglang/commit/dcd9014f15) [#28291](https://github.com/sgl-project/sglang/pull/28291) — [AMD][MXFP4] Reland "Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs" (#28291)
- **2026-07-21** [`c4c405a46b`](https://github.com/sgl-project/sglang/commit/c4c405a46b) [#31615](https://github.com/sgl-project/sglang/pull/31615) — [AMD] batch 3: register newly-added JIT kernel benchmarks for jit-kernel-benchmark-test-amd (#31615)
- **2026-07-20** [`8905cbd42f`](https://github.com/sgl-project/sglang/commit/8905cbd42f) [#31837](https://github.com/sgl-project/sglang/pull/31837) — Fix MiniMax-M3 crash on ROCm by making its override fields resolvable (#31837)
- **2026-07-20** [`54aaedd76d`](https://github.com/sgl-project/sglang/commit/54aaedd76d) [#31654](https://github.com/sgl-project/sglang/pull/31654) — Clean up prefill CUDA graph runner (#31654)
- **2026-07-20** [`b6be150798`](https://github.com/sgl-project/sglang/commit/b6be150798) [#31792](https://github.com/sgl-project/sglang/pull/31792) — [AMD] Split ROCm 7.2 Stage-B large 1-GPU tests into three partitions (#31792)
- **2026-07-20** [`17fdd8487f`](https://github.com/sgl-project/sglang/commit/17fdd8487f) [#31737](https://github.com/sgl-project/sglang/pull/31737) — [AMD] Update qwen3.5 cookbook (#31737)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#32521](https://github.com/sgl-project/sglang/issues/32521) | [Bug] [MLX] Hunyuan cannot be served: auto_map fails in kv_cache_build | — | 2026-07-27 |
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-07-27 |
| [#31783](https://github.com/sgl-project/sglang/issues/31783) | [Roadmap] Quantization 2026 H2 | — | 2026-07-27 |
| [#32507](https://github.com/sgl-project/sglang/issues/32507) | [Bug]  CPU OffloaderV2 with DeepEP fails when local expert count is no | — | 2026-07-27 |
| [#32432](https://github.com/sgl-project/sglang/issues/32432) | [RFC] Define Metadata, Workspace, and Stream-Ownership Contracts for D | — | 2026-07-27 |
| [#31023](https://github.com/sgl-project/sglang/issues/31023) | [Bug] DSpark compact target-verify CUDA Graph transition can hit timin | — | 2026-07-27 |
| [#32321](https://github.com/sgl-project/sglang/issues/32321) | [RFC] Make BaseTpWorker the explicit framework-to-backend boundary - M | — | 2026-07-27 |
| [#30599](https://github.com/sgl-project/sglang/issues/30599) | [Feature][AMD] Officially support consumer Radeon RDNA3/RDNA4 (gfx1100 | — | 2026-07-27 |
| [#32441](https://github.com/sgl-project/sglang/issues/32441) | [Bug] [MLX] test_batched_decode_matches_solo asserts bitwise solo/batc | — | 2026-07-26 |
| [#32331](https://github.com/sgl-project/sglang/issues/32331) | [Bug] UnifiedRadixCache prefill crash: TypeError: object of type 'None | — | 2026-07-26 |
| [#32377](https://github.com/sgl-project/sglang/issues/32377) | [GLM-5.2 FP4 Bug] tvm.error.InternalError in trtllm_bf16_moe on Blackw | — | 2026-07-26 |
| [#31600](https://github.com/sgl-project/sglang/issues/31600) | [Bug] glm-5.2-w4afp8 +l2(hicache)+l3(mooncake) kvcache dram cluster ,c | — | 2026-07-26 |
| [#30734](https://github.com/sgl-project/sglang/issues/30734) | [Roadmap] GLM-5.2 + AMD/ROCm DSpark support | — | 2026-07-25 |
| [#32378](https://github.com/sgl-project/sglang/issues/32378) | [Bug] mooncake with sglang:dev with glm-5.2-w4afp8 with pd error | — | 2026-07-25 |
| [#31359](https://github.com/sgl-project/sglang/issues/31359) | [Tracking] Inkling Day-0 Support | high priority, new-model | 2026-07-25 |
| [#32335](https://github.com/sgl-project/sglang/issues/32335) | [RFC]: Native Heterogeneous Weight Conversion in SGLang | — | 2026-07-24 |
| [#30928](https://github.com/sgl-project/sglang/issues/30928) | [RFC] Position-Independent KV Cache Reuse for Agentic/RAG Workloads | — | 2026-07-24 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-07-24 |
| [#27252](https://github.com/sgl-project/sglang/issues/27252) | [Roadmap]Prefill Context Parallel Refactor | — | 2026-07-24 |
| [#32101](https://github.com/sgl-project/sglang/issues/32101) | [Feature][MLX] Gemma 4 text generation on Apple Silicon | — | 2026-07-23 |

## Summary by Component

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

## Attention / FlashInfer  (45 commits)

- **2026-07-27** [`db9143ee08`](https://github.com/sgl-project/sglang/commit/db9143ee08) [#32210](https://github.com/sgl-project/sglang/pull/32210)
  [NPU] Fix MTP IndexShare warm-up for attention DP and prefill CP (#32210)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-07-27** [`08af5aea57`](https://github.com/sgl-project/sglang/commit/08af5aea57) [#32383](https://github.com/sgl-project/sglang/pull/32383)
  optimize: optimize EmbeddingGemma prefill performance (#32383)
  _Files: `docs_new/cookbook/autoregressive/Google/EmbeddingGemma.mdx`, `docs_new/docs.json`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/layernorm.py` _+3 more__
- **2026-07-27** [`abb8f4b5e3`](https://github.com/sgl-project/sglang/commit/abb8f4b5e3) [#32375](https://github.com/sgl-project/sglang/pull/32375)
  model: support EmbeddingGemma (#32375)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/pooler.py`, `python/sglang/srt/managers/scheduler.py` _+8 more__
- **2026-07-26** [`78d7928296`](https://github.com/sgl-project/sglang/commit/78d7928296) [#32294](https://github.com/sgl-project/sglang/pull/32294)
  [UT][NPU] add NPU attention unit tests for ascend_backend and ascend_dsv4_backend (#32294)
  _Files: `.github/workflows/pr-test-npu.yml`, `test/registered/unit/npu/attention/test_npu_ascend_backend.py`, `test/registered/unit/npu/attention/test_npu_ascend_dsv4_backend.py`, `test/run_suite.py`_
- **2026-07-25** [`fae84ac0f9`](https://github.com/sgl-project/sglang/commit/fae84ac0f9) [#32411](https://github.com/sgl-project/sglang/pull/32411)
  Fix token count localization for replicated attention-TP forwards (#32411)
  _Files: `python/sglang/srt/model_executor/forward_batch_info.py`_
- **2026-07-25** [`3da1071d56`](https://github.com/sgl-project/sglang/commit/3da1071d56) [#32409](https://github.com/sgl-project/sglang/pull/32409)
  [Spec] Hold the grammar bitmask in one `GrammarMask` type across all decode paths (#32409)
  _Files: `python/sglang/srt/constrained/base_grammar_backend.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/sampling/sampling_batch_info.py`, `python/sglang/srt/speculative/dflash_info.py` _+12 more__
- **2026-07-25** [`9791fc7090`](https://github.com/sgl-project/sglang/commit/9791fc7090) [#31389](https://github.com/sgl-project/sglang/pull/31389)
  Add configurable FlashInfer autotune skips (#31389)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`, `python/sglang/srt/server_args.py`_
- **2026-07-25** [`e943e609dc`](https://github.com/sgl-project/sglang/commit/e943e609dc) [#31753](https://github.com/sgl-project/sglang/pull/31753)
  [DSPARK] Grammar-constrained decoding, incl. tool_choice=auto (#31753)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/dflash_info_v2.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py` _+2 more__
- **2026-07-25** [`a678a42033`](https://github.com/sgl-project/sglang/commit/a678a42033) [#26888](https://github.com/sgl-project/sglang/pull/26888)
  [KDA] Add target_verify support for speculative decoding (#26888)
  _Files: `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/models/kimi_linear.py`, `test/manual/test_kda_spec_integration.py` _+2 more__
- **2026-07-25** [`d021990bf5`](https://github.com/sgl-project/sglang/commit/d021990bf5) [#30096](https://github.com/sgl-project/sglang/pull/30096)
  [DFLASH] Support grammar-constrained decoding in speculative verify (#30096)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/dflash_info.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dflash_worker_v2.py` _+4 more__
- **2026-07-24** [`9c483cccfe`](https://github.com/sgl-project/sglang/commit/9c483cccfe) [#31834](https://github.com/sgl-project/sglang/pull/31834)
  Support a same-size mixed q dtype in the fused RoPE kernels (#31834)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/rope.cuh`, `python/sglang/kernels/ops/attention/rope.py`, `python/sglang/srt/layers/radix_attention.py`, `test/registered/kernels/ops/attention/test_rope.py`_
- **2026-07-24** [`f7986c8603`](https://github.com/sgl-project/sglang/commit/f7986c8603) [#31087](https://github.com/sgl-project/sglang/pull/31087)
  [RL] DSV4: dispatch indexer topk_transform_512 through DSATopKBackend (#31087)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`_
- **2026-07-24** [`82fe0f041a`](https://github.com/sgl-project/sglang/commit/82fe0f041a) [#32288](https://github.com/sgl-project/sglang/pull/32288)
  Fix stale flashinfer-MLA fallback poisoning spec verify capture (trtllm_mla + tc_piecewise) (#32288)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/server_args.py`_
- **2026-07-24** [`1e69765bae`](https://github.com/sgl-project/sglang/commit/1e69765bae) [#27059](https://github.com/sgl-project/sglang/pull/27059)
  Add FP4 Indexer for DeepSeek V4 on SM120 (#27059)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py`, `python/sglang/srt/server_args.py`, `test/registered/kernels/benchmark/attention/bench_dsv4_fp4_indexer.py` _+1 more__
- **2026-07-24** [`8389d79e43`](https://github.com/sgl-project/sglang/commit/8389d79e43) [#32125](https://github.com/sgl-project/sglang/pull/32125)
  ci: add LongCat-Flash-Lite-FP8 8-GPU nightly test + fix NextN rope_theta (#32125)
  _Files: `python/sglang/srt/models/longcat_flash_nextn.py`, `test/registered/8-gpu-models/test_longcat_flash_lite_fp8.py`_
- **2026-07-24** [`841fa293b5`](https://github.com/sgl-project/sglang/commit/841fa293b5) [#31943](https://github.com/sgl-project/sglang/pull/31943)
  [Fix] Reject online weight updates while the HPC-Ops router GEMM split cache is active (#31943)
  _Files: `python/sglang/kernels/ops/attention/dsv4/gemm.py`, `python/sglang/srt/model_executor/model_runner_components/weight_updater.py`, `python/sglang/srt/models/longcat_flash.py`, `test/registered/gemm/test_linear_bf16_fp32_hpc.py`_
- **2026-07-24** [`35e25f5356`](https://github.com/sgl-project/sglang/commit/35e25f5356) [#21637](https://github.com/sgl-project/sglang/pull/21637)
  [Feature] DCP: A2A + FlashInfer-MNNVL comm backends and q-replicate (Helix) (#21637)
  _Files: `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/srt/distributed/device_communicators/pynccl.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/activation.py` _+9 more__
- **2026-07-24** [`99b29bf188`](https://github.com/sgl-project/sglang/commit/99b29bf188) [#32178](https://github.com/sgl-project/sglang/pull/32178)
  [Fix] Support ENCODER_ONLY target-verify in the trtllm_mha backend (#32178)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dense_attention.py`, `test/registered/attention/test_trtllm_mha_encoder_only.py`, `test/registered/attention/test_trtllm_mha_graph_metadata.py`_
- **2026-07-24** [`eac7c7d7cd`](https://github.com/sgl-project/sglang/commit/eac7c7d7cd) [#32251](https://github.com/sgl-project/sglang/pull/32251)
  fix(attention): read per-runner kv cache dtype off model_runner (#32251)
  _Files: `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/linear/lightning_backend.py`, `python/sglang/srt/layers/attention/xpu_backend.py` _+11 more__
- **2026-07-23** [`3d0c6bf57f`](https://github.com/sgl-project/sglang/commit/3d0c6bf57f) [#32181](https://github.com/sgl-project/sglang/pull/32181)
  [Fix] Fix trtllm_mla backend + fp8 kv cache without rope (#32181)
  _Files: `python/sglang/kernels/ops/attention/utils.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`_
- **2026-07-23** [`ebe3ab29e4`](https://github.com/sgl-project/sglang/commit/ebe3ab29e4) [#27657](https://github.com/sgl-project/sglang/pull/27657)
  [DeepSeek V4] CP decode opt: slice repeat attention weights to local TP partition (#27657)
  _Files: `python/sglang/srt/layers/cp/cp_decode_attn_tp.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_v4.py` _+2 more__
- **2026-07-23** [`9b853e6832`](https://github.com/sgl-project/sglang/commit/9b853e6832) [#32023](https://github.com/sgl-project/sglang/pull/32023)
  [Scheduler] Enable decode retraction ordering under speculative decoding (#32023)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/speculative/dflash_info_v2.py` _+4 more__
- **2026-07-23** [`09071be105`](https://github.com/sgl-project/sglang/commit/09071be105) [#32130](https://github.com/sgl-project/sglang/pull/32130)
  [NPU] [FIX] Fix performance degradation of Qwen3.5-397B-A17B (#32130)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`_
- **2026-07-23** [`1b63155efe`](https://github.com/sgl-project/sglang/commit/1b63155efe) [#32109](https://github.com/sgl-project/sglang/pull/32109)
  [Perf] Skip blocks past per-request live length in full-width Triton kernels (#32109)
  _Files: `python/sglang/kernels/ops/attention/dsa/index_buf_accessor.py`, `python/sglang/kernels/ops/attention/dsa/transform_index.py`, `python/sglang/kernels/ops/attention/dsa_metadata.py`, `python/sglang/kernels/ops/attention/extend_attention.py` _+5 more__
- **2026-07-23** [`eb242b6c03`](https://github.com/sgl-project/sglang/commit/eb242b6c03) [#32126](https://github.com/sgl-project/sglang/pull/32126)
  Seed the GDN CuteDSL correctness test inputs to fix flakiness (#32126)
  _Files: `test/registered/attention/test_gdn_prefill_cutedsl.py`_
- **2026-07-23** [`a2935ce329`](https://github.com/sgl-project/sglang/commit/a2935ce329) [#31250](https://github.com/sgl-project/sglang/pull/31250)
  [XPU][GDN] add XPU path for causal_conv1d_fn and causal_conv1d_update (#31250)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`_
- **2026-07-23** [`926530b0cf`](https://github.com/sgl-project/sglang/commit/926530b0cf) [#31863](https://github.com/sgl-project/sglang/pull/31863)
  [NPU]remove duplicate code (#31863)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`_
- **2026-07-23** [`9a7ac3ecef`](https://github.com/sgl-project/sglang/commit/9a7ac3ecef) [#31754](https://github.com/sgl-project/sglang/pull/31754)
  Fix unnecessary gather/scatter on CPU for non-contiguous Mamba statepool (#31754)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`_
- **2026-07-22** [`0a6d1930c3`](https://github.com/sgl-project/sglang/commit/0a6d1930c3) [#30540](https://github.com/sgl-project/sglang/pull/30540)
  [Attention Backend] Add HPC-Ops attention backend (#30540)
  _Files: `docs_new/docs/advanced_features/attention_backend.mdx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/hpc_ops_backend.py` _+2 more__
- **2026-07-22** [`004df6b520`](https://github.com/sgl-project/sglang/commit/004df6b520) [#29973](https://github.com/sgl-project/sglang/pull/29973)
  [FIX] Prevent Lightning Attention extra-buffer mamba state corruption (#29973)
  _Files: `python/sglang/kernels/ops/attention/linear/seg_la.py`, `python/sglang/srt/layers/attention/linear/lightning_backend.py`, `test/registered/attention/unittests/lightning/test_triton.py`_
- **2026-07-22** [`ae2bc3321e`](https://github.com/sgl-project/sglang/commit/ae2bc3321e) [#31904](https://github.com/sgl-project/sglang/pull/31904)
  [KDA] Fix mixed exponent bases in Triton chunk prefill (#31904)
  _Files: `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/kda.py`, `python/sglang/kernels/ops/attention/linear/kda_blackwell/__init__.py` _+2 more__
- **2026-07-22** [`394b0dd13a`](https://github.com/sgl-project/sglang/commit/394b0dd13a) [#31867](https://github.com/sgl-project/sglang/pull/31867)
  [NPU] Update non-vit vision part for cumulative seqlen (#31867)
  _Files: `python/sglang/srt/layers/attention/vision.py`_
- **2026-07-22** [`3217b7e3ce`](https://github.com/sgl-project/sglang/commit/3217b7e3ce) [#30981](https://github.com/sgl-project/sglang/pull/30981)
  fix(hicache): support staged write-back for asymmetric MHA (#30981)
  _Files: `python/sglang/srt/mem_cache/pool_host/mha.py`, `python/sglang/test/kl_test_utils.py`, `test/registered/jit/test_kvcacheio_asymmetric.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mimo.py` _+1 more__
- **2026-07-22** [`8ae0eb83fc`](https://github.com/sgl-project/sglang/commit/8ae0eb83fc) [#31985](https://github.com/sgl-project/sglang/pull/31985)
  [Perf] Fold dspark dense draft embedding into the draft graph via forward_embed (#31985)
  _Files: `python/sglang/srt/models/dflash.py`, `python/sglang/srt/models/dspark.py`_
- **2026-07-21** [`08cb081ed0`](https://github.com/sgl-project/sglang/commit/08cb081ed0) [#31981](https://github.com/sgl-project/sglang/pull/31981)
  [Perf] Skip page-table columns past kv length in DSA draft-extend metadata kernel (#31981)
  _Files: `python/sglang/kernels/ops/attention/dsa_metadata.py`, `test/registered/kernels/test_dsa_metadata.py`_
- **2026-07-21** [`e4eea7ce2f`](https://github.com/sgl-project/sglang/commit/e4eea7ce2f) [#30247](https://github.com/sgl-project/sglang/pull/30247)
  Optimize LongCat-Flash router GEMM with the HPC-Ops bf16xfp32 kernel (#30247)
  _Files: `python/sglang/jit_kernel/dsv4/gemm.py`, `python/sglang/srt/models/longcat_flash.py`, `test/registered/gemm/test_linear_bf16_fp32_hpc.py`, `test/registered/unit/models/test_longcat_flash_router_hpc_gemm.py`_
- **2026-07-21** [`429f6b6d15`](https://github.com/sgl-project/sglang/commit/429f6b6d15) [#31682](https://github.com/sgl-project/sglang/pull/31682)
  Turn on breakable prefill cuda graph for dp attention by default (#31682)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py`, `python/sglang/srt/hardware_backend/xpu/graph_runner/xpu_full_graph_backend.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+11 more__
- **2026-07-21** [`d093c6a4bb`](https://github.com/sgl-project/sglang/commit/d093c6a4bb) [#31050](https://github.com/sgl-project/sglang/pull/31050)
  [FullCG] Preserve attention LSE through the custom-op boundary (#31050)
  _Files: `python/sglang/srt/layers/radix_attention.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `test/registered/unit/layers/test_radix_attention.py`_
- **2026-07-20** [`a82ead53bd`](https://github.com/sgl-project/sglang/commit/a82ead53bd) [#31667](https://github.com/sgl-project/sglang/pull/31667)
  Make Q contiguous before TRT-LLM MHA decode (#31667)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `test/registered/quant/test_llama8b_nvfp4_kv_cache_sm120.py`_
- **2026-07-20** [`7fe9ad25ac`](https://github.com/sgl-project/sglang/commit/7fe9ad25ac) [#31677](https://github.com/sgl-project/sglang/pull/31677)
  [Spec] Extract DFlash compact draft-cache rebuild helpers (#31677)
  _Files: `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-07-20** [`c41c573ce9`](https://github.com/sgl-project/sglang/commit/c41c573ce9) [#28695](https://github.com/sgl-project/sglang/pull/28695)
  [GDN] Support ReplaySSM Ring Spec-Verify (#28695)
  _Files: `python/sglang/kernels/ops/attention/fla/gdn_replayssm_spec_decode.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` _+3 more__
- **2026-07-20** [`3d82dacd58`](https://github.com/sgl-project/sglang/commit/3d82dacd58) [#31714](https://github.com/sgl-project/sglang/pull/31714)
  Bump CuTe DSL to 4.6.0 (#31714)
  _Files: `python/pyproject.toml`, `python/sglang/kernels/ops/attention/cute_utils/_tcgen05.py`, `python/sglang/multimodal_gen/test/test_utils.py`, `python/sglang/srt/utils/common.py` _+1 more__
- **2026-07-20** [`97e0647bdc`](https://github.com/sgl-project/sglang/commit/97e0647bdc) [#31302](https://github.com/sgl-project/sglang/pull/31302)
  [NPU] [DOC] Fix issues about npu docs found by aidd (#31302)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_operator_development.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_optimization.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_profiling.mdx` _+25 more__
- **2026-07-20** [`fafa302e41`](https://github.com/sgl-project/sglang/commit/fafa302e41) [#30246](https://github.com/sgl-project/sglang/pull/30246)
  [XPU][NIGHTLY] Add 8 XPU nightly tests, enable 1-gpu suite (#30246)
  _Files: `.github/workflows/nightly-test-intel.yml`, `python/sglang/test/xpu/simple_eval_gsm8k_xpu_mixin.py`, `scripts/ci/xpu/xpu_ci_start_container.sh`, `test/registered/xpu/llm_models/test_xpu_gemma_4_26b_a4b.py` _+9 more__
- **2026-07-20** [`9668d9ea72`](https://github.com/sgl-project/sglang/commit/9668d9ea72) [#31732](https://github.com/sgl-project/sglang/pull/31732)
  Support GPT-OSS zigzag CP with TRTLLM-MHA (#31732)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/layers/cp/base.py`, `python/sglang/srt/layers/cp/utils.py`, `python/sglang/srt/layers/cp/zigzag.py` _+1 more__

## MoE / Expert Parallel  (39 commits)

- **2026-07-27** [`169fc1e20c`](https://github.com/sgl-project/sglang/commit/169fc1e20c) [#31280](https://github.com/sgl-project/sglang/pull/31280)
  [NPU] Acc fix for afmoe model introduced by topk refactor. (#31280)
  _Files: `python/sglang/srt/models/afmoe.py`_
- **2026-07-27** [`c0f47a06fc`](https://github.com/sgl-project/sglang/commit/c0f47a06fc) [#31393](https://github.com/sgl-project/sglang/pull/31393)
  [NPU] Determine the topk norm_type through scoring_func (#31393)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/models/glm4_moe_lite.py`_
- **2026-07-27** [`a358374ae9`](https://github.com/sgl-project/sglang/commit/a358374ae9) [#32001](https://github.com/sgl-project/sglang/pull/32001)
  [NPU][Fix Issue]: Send expert weights contiguous tensor across cards during EPLB rebalance (#32001)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py`_
- **2026-07-26** [`e8a635a412`](https://github.com/sgl-project/sglang/commit/e8a635a412) [#32435](https://github.com/sgl-project/sglang/pull/32435)
  Load initial expert location metadata on CPU (#32435)
  _Files: `python/sglang/srt/eplb/expert_location.py`_
- **2026-07-26** [`833e1bc601`](https://github.com/sgl-project/sglang/commit/833e1bc601) [#31793](https://github.com/sgl-project/sglang/pull/31793)
  [Fix][AMD] Qwen3.5 MoE: disable global-slot shared-expert fusion under per-rank EP backends (MoRI + dp-attention init crash) (#31793)
  _Files: `python/sglang/srt/models/qwen2_moe.py`_
- **2026-07-25** [`1054060ef1`](https://github.com/sgl-project/sglang/commit/1054060ef1) [#31552](https://github.com/sgl-project/sglang/pull/31552)
  perf: speed up marlin moe with occupancy-aware launch specialization (#31552)
  _Files: `python/sglang/kernels/jit/csrc/gemm/marlin_moe/kernel.h`, `python/sglang/kernels/jit/csrc/gemm/marlin_moe/marlin_template.h`, `python/sglang/kernels/jit/csrc/gemm/marlin_moe/moe_wna16_marlin.cuh`, `python/sglang/kernels/ops/moe/moe_wna16_marlin.py` _+1 more__
- **2026-07-25** [`9eb2dccbb7`](https://github.com/sgl-project/sglang/commit/9eb2dccbb7) [#31744](https://github.com/sgl-project/sglang/pull/31744)
  [Elastic EP] Fix recovery lifecycle and add manual coverage (#31744)
  _Files: `python/sglang/srt/elastic_ep/elastic_ep.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/model_runner.py` _+3 more__
- **2026-07-25** [`b83041c3cc`](https://github.com/sgl-project/sglang/commit/b83041c3cc) [#32248](https://github.com/sgl-project/sglang/pull/32248)
  Migrate CompressedTensorsW4A4Nvfp4MoE TRT-LLM path onto MoeRunner (#32248)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4_moe.py`_
- **2026-07-24** [`14d6e1d3b1`](https://github.com/sgl-project/sglang/commit/14d6e1d3b1) [#31085](https://github.com/sgl-project/sglang/pull/31085)
  [RL] Support FlashInfer TRT-LLM NVFP4 MoE in the RL weight checker (#31085)
  _Files: `python/sglang/srt/utils/weight_checker_comparator.py`_
- **2026-07-24** [`3d91a569ce`](https://github.com/sgl-project/sglang/commit/3d91a569ce) [#30541](https://github.com/sgl-project/sglang/pull/30541)
  [MoE Backend] Add HPC-Ops FP8 MoE runner backend (#30541)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/hpc_ops.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/moe/token_dispatcher/standard.py` _+7 more__
- **2026-07-24** [`4d5917e744`](https://github.com/sgl-project/sglang/commit/4d5917e744) [#31017](https://github.com/sgl-project/sglang/pull/31017)
  Add DeepSeek-reference 1e-20 epsilon to top-k renormalization to prevent 0/0 NaN (#31017)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/moe/test_topk_renormalize_degenerate.py`_
- **2026-07-24** [`b954e9cf3d`](https://github.com/sgl-project/sglang/commit/b954e9cf3d) [#30822](https://github.com/sgl-project/sglang/pull/30822)
  [6/6][kimi-deterministic] Use deterministic seeded coins for EAGLE rejection sampling (#30822)
  _Files: `python/sglang/kernels/ops/attention/flash_attention.py`, `python/sglang/kernels/ops/attention/flash_attention_v4.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` _+15 more__
- **2026-07-24** [`b8bb1b4e5a`](https://github.com/sgl-project/sglang/commit/b8bb1b4e5a) [#31870](https://github.com/sgl-project/sglang/pull/31870)
  [lora] Fix WAR race: never write MoE runner output into hidden_states in place (#31870)
  _Files: `python/sglang/srt/lora/layers.py`, `test/registered/unit/lora/test_lora_moe_inplace_unit.py`_
- **2026-07-24** [`39955d5314`](https://github.com/sgl-project/sglang/commit/39955d5314) [#29523](https://github.com/sgl-project/sglang/pull/29523)
  [MoE] Make DeepEP auto serve flashinfer_cutedsl FP4 (coerce to low_latency) + guard (#29523)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-23** [`71fe41b6b3`](https://github.com/sgl-project/sglang/commit/71fe41b6b3) [#29569](https://github.com/sgl-project/sglang/pull/29569)
  [DSV4] Support megamoe for CP (#29569)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-07-23** [`378aea1385`](https://github.com/sgl-project/sglang/commit/378aea1385) [#32246](https://github.com/sgl-project/sglang/pull/32246)
  Fix nvfp4 online scale with pcg (#32246)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`_
- **2026-07-23** [`62aa85d9aa`](https://github.com/sgl-project/sglang/commit/62aa85d9aa) [#32160](https://github.com/sgl-project/sglang/pull/32160)
  [Kernel] Sweep missed dedicated kernels into kernels.ops (moe/quant siblings + dspark) (RFC #29630) (#32160)
  _Files: `python/sglang/kernels/ops/moe/gate_topk.py`, `python/sglang/kernels/ops/moe/inkling_moe.py`, `python/sglang/kernels/ops/moe/sigmoid_gate_topk_renorm.py`, `python/sglang/kernels/ops/quantization/mxfp8_interleave_sf.py` _+21 more__
- **2026-07-23** [`235a488c87`](https://github.com/sgl-project/sglang/commit/235a488c87) [#32040](https://github.com/sgl-project/sglang/pull/32040)
  [NPU] ascend fuseep use moe ep group (#32040)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/fuseep.py`_
- **2026-07-23** [`108182cb81`](https://github.com/sgl-project/sglang/commit/108182cb81) [#32113](https://github.com/sgl-project/sglang/pull/32113)
  [Bugfix] [NPU] Fix w4a8 MoE performance degradation (#32113)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py`_
- **2026-07-22** [`0c29c8fece`](https://github.com/sgl-project/sglang/commit/0c29c8fece) [#31927](https://github.com/sgl-project/sglang/pull/31927)
  Bump FlashInfer to 0.6.15.post1 (#31927)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/attention/dsa_backend.py` _+7 more__
- **2026-07-22** [`40b2119b23`](https://github.com/sgl-project/sglang/commit/40b2119b23) [#31889](https://github.com/sgl-project/sglang/pull/31889)
  [AMD] Cache AITER expert mask across decode (#31889)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/standard.py`_
- **2026-07-22** [`d6690de961`](https://github.com/sgl-project/sglang/commit/d6690de961) [#32049](https://github.com/sgl-project/sglang/pull/32049)
  [CI] Fix Marlin MoE test ServerArgs initialization (#32049)
  _Files: `test/registered/quant/test_marlin_moe.py`_
- **2026-07-22** [`977ea336cd`](https://github.com/sgl-project/sglang/commit/977ea336cd) [#32015](https://github.com/sgl-project/sglang/pull/32015)
  [Kernel] Phase 4 batch-2: migrate JIT operator groups into kernels.ops (no shims) (RFC #29630) (#32015)
  _Files: `python/sglang/jit_kernel/benchmark/utils.py`, `python/sglang/jit_kernel/dsv4/attn.py`, `python/sglang/jit_kernel/tests/utils.py`, `python/sglang/kernels/ops/communication/all_reduce.py` _+91 more__
- **2026-07-22** [`9456cef279`](https://github.com/sgl-project/sglang/commit/9456cef279) [#31796](https://github.com/sgl-project/sglang/pull/31796)
  [NPU]fix rl update weights 'Parameter' object has no attribute 'weight_LOADER' (#31796)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py`_
- **2026-07-22** [`d708969f68`](https://github.com/sgl-project/sglang/commit/d708969f68) [#31782](https://github.com/sgl-project/sglang/pull/31782)
  [bugfix][NPU] Fix startup bug in olmoe 1b 7b (#31782)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/ascend_tp.py`_
- **2026-07-22** [`14c0a31829`](https://github.com/sgl-project/sglang/commit/14c0a31829) [#31769](https://github.com/sgl-project/sglang/pull/31769)
  [Bugfix] Fix Cohere2MoeConfig import crash from huggingface_hub @strict (#31769)
  _Files: `python/sglang/srt/configs/cohere2_moe.py`, `test/registered/unit/configs/test_cohere2_moe_config.py`_
- **2026-07-22** [`8bb0d8d005`](https://github.com/sgl-project/sglang/commit/8bb0d8d005) [#30924](https://github.com/sgl-project/sglang/pull/30924)
  [JIT] Trait-driven per_token_group_quant: unify the quant kernel family (flat + masked) (#30924)
  _Files: `python/sglang/jit_kernel/csrc/gemm/per_token_group_quant.cuh`, `python/sglang/jit_kernel/csrc/gemm/per_token_group_quant_8bit.cuh`, `python/sglang/jit_kernel/per_token_group_quant.py`, `python/sglang/jit_kernel/per_token_group_quant_8bit.py` _+13 more__
- **2026-07-22** [`a2c38175a4`](https://github.com/sgl-project/sglang/commit/a2c38175a4) [#31762](https://github.com/sgl-project/sglang/pull/31762)
  fix(marlin_nvfp4): only apply routed_scaling_factor in moe_sum_reduce (#31762)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`_
- **2026-07-21** [`2f4f2362fb`](https://github.com/sgl-project/sglang/commit/2f4f2362fb) [#31202](https://github.com/sgl-project/sglang/pull/31202)
  Delete sgl-kernel AOT `bmm_fp8`, use `flashinfer.bmm_fp8` (#31202)
  _Files: `python/sglang/kernels/ops/gemm/__init__.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_fused_rope_rocm.py` _+11 more__
- **2026-07-21** [`927979e127`](https://github.com/sgl-project/sglang/commit/927979e127) [#31838](https://github.com/sgl-project/sglang/pull/31838)
  Fix pad-row top-k masking with custom_routing_function under DP attention (#31838)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+2 more__
- **2026-07-21** [`57e5846b90`](https://github.com/sgl-project/sglang/commit/57e5846b90) [#31608](https://github.com/sgl-project/sglang/pull/31608)
  [LoRA] Guard TMA down path for LoRA hooks (#31608)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`_
- **2026-07-21** [`dcd9014f15`](https://github.com/sgl-project/sglang/commit/dcd9014f15) [#28291](https://github.com/sgl-project/sglang/pull/28291)
  [AMD][MXFP4] Reland "Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs" (#28291)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/dequantization.py` _+10 more__
- **2026-07-21** [`c0ed009f5b`](https://github.com/sgl-project/sglang/commit/c0ed009f5b) [#31772](https://github.com/sgl-project/sglang/pull/31772)
  [NPU] Fix LLaDA2 MoE OOM after the FRACTAL_NZ cast, re-enabling the NZ speedup (#31772)
  _Files: `python/sglang/srt/models/llada2.py`, `test/registered/ascend/basic_function/dllm/test_npu_llada2_mini.py`_
- **2026-07-21** [`01f558d905`](https://github.com/sgl-project/sglang/commit/01f558d905) [#31669](https://github.com/sgl-project/sglang/pull/31669)
  Sm120 scatter fallback (#31669)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`_
- **2026-07-20** [`91b210f7b0`](https://github.com/sgl-project/sglang/commit/91b210f7b0) [#28416](https://github.com/sgl-project/sglang/pull/28416)
  [GLM5][MoE] perf: Write FlashInfer TRT-LLM MoE output directly (#28416)
  _Files: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`_
- **2026-07-20** [`ff6c755952`](https://github.com/sgl-project/sglang/commit/ff6c755952) [#31733](https://github.com/sgl-project/sglang/pull/31733)
  [Refactor] Unify logprob results into a single `LogprobResult` and rename chunk env vars (#31733)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/logprob_processor.py`, `python/sglang/srt/layers/sampler.py` _+7 more__
- **2026-07-20** [`1843384c7a`](https://github.com/sgl-project/sglang/commit/1843384c7a) [#31311](https://github.com/sgl-project/sglang/pull/31311)
  Fix LongCat-2.0 real EP (deepep): double all-reduce + ScMoE RoPE crash (#31311)
  _Files: `python/sglang/srt/models/longcat_flash.py`_
- **2026-07-20** [`1f637a65b9`](https://github.com/sgl-project/sglang/commit/1f637a65b9) [#31707](https://github.com/sgl-project/sglang/pull/31707)
  [NPU] bugfix for W4A8MoE bias 3D dimension mismatch problem (#31707)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py`_
- **2026-07-20** [`bab1dd0d12`](https://github.com/sgl-project/sglang/commit/bab1dd0d12) [#31126](https://github.com/sgl-project/sglang/pull/31126)
  [Intel XPU] Enable (biased) grouped topk for xpu (#31126)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/xpu/test_topk.py`_

## Other  (26 commits)

- **2026-07-27** [`34454c06b8`](https://github.com/sgl-project/sglang/commit/34454c06b8) [#32496](https://github.com/sgl-project/sglang/pull/32496)
  [Refactor] Tidy server_args.py section grouping and drop unused alias (#32496)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-27** [`2abb1d2c37`](https://github.com/sgl-project/sglang/commit/2abb1d2c37) [#31992](https://github.com/sgl-project/sglang/pull/31992)
  fix(hisparse): correct DSA KV memory budget (#31992)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_hisparse_pool_configurator.py`_
- **2026-07-26** [`3863612023`](https://github.com/sgl-project/sglang/commit/3863612023) [#32453](https://github.com/sgl-project/sglang/pull/32453)
  Add oulgen to CI_PERMISSIONS.json (#32453)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-07-25** [`5f330004bd`](https://github.com/sgl-project/sglang/commit/5f330004bd) [#32410](https://github.com/sgl-project/sglang/pull/32410)
  Fix flaky test_sampling_mask: mask length can legitimately be top_k + 1 (#32410)
  _Files: `test/registered/sampling/test_sampling_mask.py`_
- **2026-07-25** [`659d349b61`](https://github.com/sgl-project/sglang/commit/659d349b61) [#24256](https://github.com/sgl-project/sglang/pull/24256)
  [core/loader] Add presharded load format (#24256)
  _Files: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml` _+5 more__
- **2026-07-24** [`be7cc17307`](https://github.com/sgl-project/sglang/commit/be7cc17307) [#32240](https://github.com/sgl-project/sglang/pull/32240)
  sglang rust server environ fsm error id gen (#32240)
  _Files: `rust/sglang-server/src/environ.rs`, `rust/sglang-server/src/error.rs`, `rust/sglang-server/src/fsm.rs`, `rust/sglang-server/src/ids.rs` _+1 more__
- **2026-07-24** [`34d02bae47`](https://github.com/sgl-project/sglang/commit/34d02bae47) [#32306](https://github.com/sgl-project/sglang/pull/32306)
  Add CI permissions for Elastic EP contributor UNIDY2002 (#32306)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-07-24** [`f4f15162bc`](https://github.com/sgl-project/sglang/commit/f4f15162bc) [#32279](https://github.com/sgl-project/sglang/pull/32279)
  [Fix] Fail fast when a safetensors index references missing shard files (#32279)
  _Files: `python/sglang/srt/model_loader/weight_utils.py`, `test/registered/unit/model_loader/test_weight_utils.py`_
- **2026-07-23** [`20eb37a2a1`](https://github.com/sgl-project/sglang/commit/20eb37a2a1) [#32256](https://github.com/sgl-project/sglang/pull/32256)
  init sglang rust server project (#32256)
  _Files: `rust/Cargo.toml`, `rust/sglang-server/Cargo.toml`, `rust/sglang-server/pyproject.toml`, `rust/sglang-server/src/lib.rs`_
- **2026-07-23** [`1f9d778d1b`](https://github.com/sgl-project/sglang/commit/1f9d778d1b) [#31410](https://github.com/sgl-project/sglang/pull/31410)
  Skip dist_init/nccl port prechecks when the dist init method is overridden (#31410)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-22** [`f5dcbe8f14`](https://github.com/sgl-project/sglang/commit/f5dcbe8f14) [#32100](https://github.com/sgl-project/sglang/pull/32100)
  Revert RuntimeContext config-namespace reads/roles (#31813–#31817) (#32100)
- **2026-07-22** [`e81b326e72`](https://github.com/sgl-project/sglang/commit/e81b326e72) [#32095](https://github.com/sgl-project/sglang/pull/32095)
  Add Inkling per-commit server test (#32095)
  _Files: `test/registered/models/test_inkling.py`_
- **2026-07-22** [`a9497e8d73`](https://github.com/sgl-project/sglang/commit/a9497e8d73) [#31973](https://github.com/sgl-project/sglang/pull/31973)
  Guard min_new_tokens penalizer against None eos_token_id (#31973)
  _Files: `python/sglang/srt/sampling/penaltylib/min_new_tokens.py`_
- **2026-07-22** [`b13abfdedf`](https://github.com/sgl-project/sglang/commit/b13abfdedf) [#31312](https://github.com/sgl-project/sglang/pull/31312)
  Fix LongCat n-gram token-table crashes on padded batches (#31312)
  _Files: `python/sglang/srt/layers/n_gram_embedding.py`, `python/sglang/srt/model_executor/model_runner_components/ngram_embedding_manager.py`_
- **2026-07-22** [`2e43b4de52`](https://github.com/sgl-project/sglang/commit/2e43b4de52) [#31817](https://github.com/sgl-project/sglang/pull/31817)
  test: publish resolved config in unit fixtures for the namespace API (#31817)
  _Files: `test/registered/unit/test_legacy_global_ratchet.py`, `test/registered/unit/test_runtime_context.py`_
- **2026-07-22** [`602b546a4e`](https://github.com/sgl-project/sglang/commit/602b546a4e) [#31815](https://github.com/sgl-project/sglang/pull/31815)
  config: load-time declarations write the config bags (#31815)
  _Files: `python/sglang/srt/arg_groups/overrides.py`_
- **2026-07-22** [`11a4c2d057`](https://github.com/sgl-project/sglang/commit/11a4c2d057) [#31814](https://github.com/sgl-project/sglang/pull/31814)
  config: read resolved config via namespace accessors (#31814)
- **2026-07-22** [`09688d58bc`](https://github.com/sgl-project/sglang/commit/09688d58bc) [#31810](https://github.com/sgl-project/sglang/pull/31810)
  runtime_context: add resolved-config namespace bags and accessors (#31810)
  _Files: `python/sglang/srt/runtime_context.py`, `test/registered/unit/test_runtime_context_config_bags.py`_
- **2026-07-22** [`1a19f2b50f`](https://github.com/sgl-project/sglang/commit/1a19f2b50f) [#31809](https://github.com/sgl-project/sglang/pull/31809)
  config: annotate ServerArgs fields with their runtime-config namespace (#31809)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/test_server_args_namespaces.py`_
- **2026-07-22** [`88836eb38e`](https://github.com/sgl-project/sglang/commit/88836eb38e) [#31950](https://github.com/sgl-project/sglang/pull/31950)
  Add OrangeRedeng and Alisehen to CI_PERMISSIONS.json (#31950)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-07-21** [`cb324cc958`](https://github.com/sgl-project/sglang/commit/cb324cc958) [#31980](https://github.com/sgl-project/sglang/pull/31980)
  Add wangfakang to CI_PERMISSIONS.json (#31980)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-07-21** [`075bd97952`](https://github.com/sgl-project/sglang/commit/075bd97952) [#31941](https://github.com/sgl-project/sglang/pull/31941)
  [Benchmark] Remove obsolete auto-benchmark remnants (#31941)
  _Files: `python/sglang/auto_benchmark.py`, `python/sglang/auto_benchmark_lib.py`, `python/sglang/benchmark/datasets/__init__.py`, `python/sglang/benchmark/datasets/autobench.py` _+5 more__
- **2026-07-21** [`0a06cc5317`](https://github.com/sgl-project/sglang/commit/0a06cc5317) [#31942](https://github.com/sgl-project/sglang/pull/31942)
  Fix extra_buffer_lazy guard bypass (#31942)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-21** [`66ea79dc2e`](https://github.com/sgl-project/sglang/commit/66ea79dc2e) [#31916](https://github.com/sgl-project/sglang/pull/31916)
  Update FLA directory in CODEOWNERS (#31916)
  _Files: `.github/CODEOWNERS`_
- **2026-07-20** [`5ab3d90b81`](https://github.com/sgl-project/sglang/commit/5ab3d90b81) [#31787](https://github.com/sgl-project/sglang/pull/31787)
  Fix dropped Inkling reasoning at stream end (#31787)
  _Files: `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/parser/test_reasoning_parser.py`_
- **2026-07-20** [`02236fa38c`](https://github.com/sgl-project/sglang/commit/02236fa38c) [#31681](https://github.com/sgl-project/sglang/pull/31681)
  Add Inkling model support (#31681)

## Prefill / Decode Disaggregation  (25 commits)

- **2026-07-27** [`3d3ba4f746`](https://github.com/sgl-project/sglang/commit/3d3ba4f746) [#32071](https://github.com/sgl-project/sglang/pull/32071)
  [BugFix][EPD] Fix Mooncake source-MR lifecycle for multi-TP /send (#32071)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`_
- **2026-07-26** [`e14068d161`](https://github.com/sgl-project/sglang/commit/e14068d161) [#31189](https://github.com/sgl-project/sglang/pull/31189)
  [NPU]Add Ascend transfer version compatibility. (#31189)
  _Files: `python/sglang/srt/disaggregation/ascend/transfer_engine.py`_
- **2026-07-26** [`a76b74cbe0`](https://github.com/sgl-project/sglang/commit/a76b74cbe0) [#32427](https://github.com/sgl-project/sglang/pull/32427)
  add fill_draft_extend_prepare_buffers_native for NPU (#32427)
  _Files: `python/sglang/kernels/ops/speculative/multi_layer_eagle.py`, `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_utils.py`_
- **2026-07-25** [`cd145f840f`](https://github.com/sgl-project/sglang/commit/cd145f840f) [#29901](https://github.com/sgl-project/sglang/pull/29901)
  Radix Cache Split: Spin off TreeCore (#29901)
  _Files: `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/kv_canary/radix_cache_walker.py`, `python/sglang/srt/managers/schedule_batch.py` _+21 more__
- **2026-07-25** [`91f386a5b2`](https://github.com/sgl-project/sglang/commit/91f386a5b2) [#32270](https://github.com/sgl-project/sglang/pull/32270)
  fix(disagg): support pipeline-parallel hybrid-linear transfer (#32270)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py` _+8 more__
- **2026-07-25** [`f5155d9602`](https://github.com/sgl-project/sglang/commit/f5155d9602) [#31275](https://github.com/sgl-project/sglang/pull/31275)
  [EPD] Fix HTTP dispatch lock blocking cross-request encoder batching (#31275)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`_
- **2026-07-25** [`bdd0698541`](https://github.com/sgl-project/sglang/commit/bdd0698541) [#32302](https://github.com/sgl-project/sglang/pull/32302)
  chore: bump mooncake version to 0.3.12.post1 (#32302)
  _Files: `docker/Dockerfile`, `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-07-25** [`6a046fad09`](https://github.com/sgl-project/sglang/commit/6a046fad09) [#31144](https://github.com/sgl-project/sglang/pull/31144)
  [PD] Prevent decode scheduler from blocking on ZMQ sends to a stalled prefill peer (#31144)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py` _+2 more__
- **2026-07-25** [`ebcb74abd4`](https://github.com/sgl-project/sglang/commit/ebcb74abd4) [#29326](https://github.com/sgl-project/sglang/pull/29326)
  feat(hicache): Add shared memory allocator for host KV cache (#29326)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/pool_host/base.py` _+10 more__
- **2026-07-24** [`2428f56145`](https://github.com/sgl-project/sglang/commit/2428f56145) [#32262](https://github.com/sgl-project/sglang/pull/32262)
  [Bugfix] Fix Kimi-Linear state transfer across heterogeneous TP (#32262)
  _Files: `python/sglang/srt/configs/mamba_utils.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py` _+6 more__
- **2026-07-24** [`fa243fee40`](https://github.com/sgl-project/sglang/commit/fa243fee40) [#32324](https://github.com/sgl-project/sglang/pull/32324)
  [CI] Skip flaky test in CI for disaggregation group (#32324)
  _Files: `test/registered/disaggregation/test_disaggregation_dwdp_mimo.py`_
- **2026-07-24** [`de816e1eb5`](https://github.com/sgl-project/sglang/commit/de816e1eb5) [#31217](https://github.com/sgl-project/sglang/pull/31217)
  [Disagg][StagingBuffer][1/2] Robustness and failure handling (#31217)
  _Files: `docs_new/docs/advanced_features/pd_disaggregation.mdx`, `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/disaggregation/common/staging_buffer.py`, `python/sglang/srt/disaggregation/common/staging_handler.py` _+7 more__
- **2026-07-24** [`364b5f23e6`](https://github.com/sgl-project/sglang/commit/364b5f23e6) [#31592](https://github.com/sgl-project/sglang/pull/31592)
  [BugFix][EPD] Harden zmq_to_scheduler receiver failures; sync error info across TP (#31592)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/managers/scheduler_components/request_receiver.py`_
- **2026-07-24** [`58f417049d`](https://github.com/sgl-project/sglang/commit/58f417049d) [#30412](https://github.com/sgl-project/sglang/pull/30412)
  [PD] Fix multi-tokenizer disaggregation metrics labels (#30412)
  _Files: `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-07-23** [`86e1bb584d`](https://github.com/sgl-project/sglang/commit/86e1bb584d) [#31920](https://github.com/sgl-project/sglang/pull/31920)
  [HiCache] Add model-aware key isolation to Mooncake Store (#31920)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `test/registered/unit/mem_cache/test_mooncake_group_semantics.py`_
- **2026-07-22** [`5c6a29b3c3`](https://github.com/sgl-project/sglang/commit/5c6a29b3c3) [#32029](https://github.com/sgl-project/sglang/pull/32029)
  [Fix] Unify pinned host pool release on graceful shutdown (#32029)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py` _+3 more__
- **2026-07-22** [`745b2ca45c`](https://github.com/sgl-project/sglang/commit/745b2ca45c) [#31816](https://github.com/sgl-project/sglang/pull/31816)
  config: read parallel config leaves via get_parallel() (#31816)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py` _+57 more__
- **2026-07-22** [`1d0a6ee178`](https://github.com/sgl-project/sglang/commit/1d0a6ee178) [#31813](https://github.com/sgl-project/sglang/pull/31813)
  runtime_context: record the publishing process role (#31813)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/elastic_ep/expert_backup_manager.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/scheduler.py` _+4 more__
- **2026-07-22** [`e1479cc966`](https://github.com/sgl-project/sglang/commit/e1479cc966) [#31812](https://github.com/sgl-project/sglang/pull/31812)
  config: route runtime config adjustments through the namespace bags (#31812)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/linear/lightning_backend.py` _+27 more__
- **2026-07-22** [`97e2c0c4ee`](https://github.com/sgl-project/sglang/commit/97e2c0c4ee) [#31811](https://github.com/sgl-project/sglang/pull/31811)
  config: make ServerArgs read-only with a single audited mutation entry (#31811)
  _Files: `examples/runtime/token_in_token_out/token_in_token_out_vlm_engine.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/runtime_context.py` _+3 more__
- **2026-07-22** [`ddaf430e6c`](https://github.com/sgl-project/sglang/commit/ddaf430e6c) [#31708](https://github.com/sgl-project/sglang/pull/31708)
  [Elastic EP] Centralize Mooncake PG configuration (#31708)
  _Files: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/device_communicators/mooncake_transfer_engine.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-07-21** [`6f55de0468`](https://github.com/sgl-project/sglang/commit/6f55de0468) [#31576](https://github.com/sgl-project/sglang/pull/31576)
  [EPD] Make encoder register/unregister health-check robust (#31576)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/environ.py`_
- **2026-07-21** [`df39a7b0b6`](https://github.com/sgl-project/sglang/commit/df39a7b0b6) [#27894](https://github.com/sgl-project/sglang/pull/27894)
  [CI][PD] Add NIXL disaggregation functional tests (#27894)
  _Files: `python/sglang/test/server_fixtures/disaggregation_fixture.py`, `test/registered/disaggregation/test_disaggregation_nixl.py`_
- **2026-07-21** [`37a830b667`](https://github.com/sgl-project/sglang/commit/37a830b667) [#29778](https://github.com/sgl-project/sglang/pull/29778)
  [Feature] Add DWDP (Distributed Weight Data Parallelism) for MoE prefill (#29778)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/dwdp/__init__.py`, `python/sglang/srt/layers/moe/dwdp/dwdp_manager.py` _+16 more__
- **2026-07-20** [`50c118704a`](https://github.com/sgl-project/sglang/commit/50c118704a) [#31325](https://github.com/sgl-project/sglang/pull/31325)
  [diffusion] disagg: handle numpy arrays in cross-role transfer field extraction (#31325)
  _Files: `python/sglang/multimodal_gen/runtime/disaggregation/scheduler_mixin.py`_

## Multimodal  (19 commits)

- **2026-07-25** [`d3cf4dfbaa`](https://github.com/sgl-project/sglang/commit/d3cf4dfbaa) [#32408](https://github.com/sgl-project/sglang/pull/32408)
  Update audio container test time estimate (#32408)
  _Files: `test/registered/unit/multimodal/test_audio_container_decode.py`_
- **2026-07-25** [`a23f6ea090`](https://github.com/sgl-project/sglang/commit/a23f6ea090) [#32032](https://github.com/sgl-project/sglang/pull/32032)
  [Diffusion] offload rollout weights to pinned host memory (#32032)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/memory_occupation_controller.py`_
- **2026-07-25** [`95865de24f`](https://github.com/sgl-project/sglang/commit/95865de24f) [#32297](https://github.com/sgl-project/sglang/pull/32297)
  [diffusion] CI: read consistency GT from ci-data-diffusion at per-platform commit (#32297)
  _Files: `python/sglang/multimodal_gen/test/test_utils.py`, `python/sglang/multimodal_gen/test/unit/test_consistency_metrics.py`_
- **2026-07-25** [`ebf5330f71`](https://github.com/sgl-project/sglang/commit/ebf5330f71) [#32282](https://github.com/sgl-project/sglang/pull/32282)
  [diffusion] CI: enhance diffusion GT publishing with per-platform directory resolution (#32282)
  _Files: `.github/workflows/diffusion-ci-gt-gen.yml`, `scripts/ci/utils/diffusion/publish_diffusion_gt.py`_
- **2026-07-24** [`962c076934`](https://github.com/sgl-project/sglang/commit/962c076934) [#31832](https://github.com/sgl-project/sglang/pull/31832)
  Decode input_audio media containers with PyAV & Update memory profiler (#31832)
  _Files: `python/pyproject.toml`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler_components/profiler_manager.py`, `python/sglang/srt/multimodal/audio_from_video.py` _+4 more__
- **2026-07-24** [`2f823a2eee`](https://github.com/sgl-project/sglang/commit/2f823a2eee) [#32044](https://github.com/sgl-project/sglang/pull/32044)
  [Intel GPU] calculate free memory based on allocated memory for XPU (#32044)
  _Files: `python/sglang/multimodal_gen/runtime/platforms/xpu.py`, `python/sglang/srt/utils/common.py`_
- **2026-07-24** [`433429b16a`](https://github.com/sgl-project/sglang/commit/433429b16a) [#32117](https://github.com/sgl-project/sglang/pull/32117)
  diffusion: skip `_save_gt_output` for 3d/mesh (#32117)
  _Files: `python/sglang/multimodal_gen/test/server/test_server_common.py`_
- **2026-07-23** [`ed26a111b2`](https://github.com/sgl-project/sglang/commit/ed26a111b2) [#32257](https://github.com/sgl-project/sglang/pull/32257)
  Revert "docker: install dynamo nightly in the dev image for rapid iteration/testing" (#32257)
  _Files: `.github/workflows/release-docker-dev.yml`, `docker/Dockerfile`_
- **2026-07-23** [`a25164bda3`](https://github.com/sgl-project/sglang/commit/a25164bda3) [#32011](https://github.com/sgl-project/sglang/pull/32011)
  Shift nightly image build & pipeline schedule ahead by 2 hours (#32011)
  _Files: `.github/workflows/nightly-test-npu.yml`, `.github/workflows/release-docker-npu-nightly.yml`_
- **2026-07-23** [`8ce68370b5`](https://github.com/sgl-project/sglang/commit/8ce68370b5) [#31757](https://github.com/sgl-project/sglang/pull/31757)
  [AMD] Build Miles nightly ROCm images with docker/build.py and test ROCm 7.2 (#31757)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm720.yml`, `.github/workflows/release-docker-amd-miles-rocm700-nightly.yml`, `.github/workflows/release-docker-amd-miles-rocm720-nightly.yml`_
- **2026-07-22** [`93cb9a5482`](https://github.com/sgl-project/sglang/commit/93cb9a5482) [#31983](https://github.com/sgl-project/sglang/pull/31983)
  [CI] Point diffusion CI writes to sgl-project/ci-data-diffusion (#31983)
  _Files: `.github/workflows/diffusion-ci-gt-gen-npu.yml`, `.github/workflows/diffusion-ci-gt-gen.yml`, `python/sglang/multimodal_gen/test/server/test_server_common.py`, `python/sglang/multimodal_gen/test/server/test_server_utils.py` _+4 more__
- **2026-07-21** [`1b4cb6b8c1`](https://github.com/sgl-project/sglang/commit/1b4cb6b8c1) [#31928](https://github.com/sgl-project/sglang/pull/31928)
  Route /rerun-test for b200 multimodal tests to the b200 pool (#31928)
  _Files: `scripts/ci/utils/slash_command_handler.py`_
- **2026-07-21** [`303896a475`](https://github.com/sgl-project/sglang/commit/303896a475) [#31663](https://github.com/sgl-project/sglang/pull/31663)
  [Bugfix] Place empty Qwen encoder-DP embeddings on the communication device (#31663)
  _Files: `python/sglang/srt/multimodal/mm_utils.py`_
- **2026-07-21** [`4682ded472`](https://github.com/sgl-project/sglang/commit/4682ded472) [#31438](https://github.com/sgl-project/sglang/pull/31438)
  vlm: parallelize multimodal preprocessing with customized worker num (#31438)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/executor.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-07-20** [`e149cdb337`](https://github.com/sgl-project/sglang/commit/e149cdb337) [#31819](https://github.com/sgl-project/sglang/pull/31819)
  docs(cookbook): revert MiniMax-M3 to dev image (model not yet in a release) (#31819)
  _Files: `docs_new/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`_
- **2026-07-20** [`4e8eb1457b`](https://github.com/sgl-project/sglang/commit/4e8eb1457b) [#31565](https://github.com/sgl-project/sglang/pull/31565)
  [Diffusion] msgpack raw-bytes transport (drop base64/JSON) (#31565)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/post_training/rollout_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/post_training/utils.py`, `python/sglang/multimodal_gen/test/unit/test_rollout_api.py`_
- **2026-07-20** [`2eed35d738`](https://github.com/sgl-project/sglang/commit/2eed35d738) [#31301](https://github.com/sgl-project/sglang/pull/31301)
  perf: avoid temporary VLM encoder gather padding (#31301)
  _Files: `python/sglang/srt/multimodal/mm_utils.py`, `test/registered/unit/multimodal/test_mrope_encoder_utils.py`_
- **2026-07-20** [`9f8e916131`](https://github.com/sgl-project/sglang/commit/9f8e916131) [#31263](https://github.com/sgl-project/sglang/pull/31263)
  [diffusion] post_training: run weight update under torch.inference_mode() (#31263)
  _Files: `python/sglang/multimodal_gen/runtime/post_training/weights_updater.py`_
- **2026-07-20** [`6a25dd7b5f`](https://github.com/sgl-project/sglang/commit/6a25dd7b5f) [#31298](https://github.com/sgl-project/sglang/pull/31298)
  fix: warm up Kimi VLM vision encoder at startup (#31298)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `test/registered/unit/entrypoints/test_server_warmup.py`_

## KV Cache / Memory  (18 commits)

- **2026-07-27** [`4ea17169b0`](https://github.com/sgl-project/sglang/commit/4ea17169b0) [#31902](https://github.com/sgl-project/sglang/pull/31902)
  [UnifiedTree] fix: drop prefetched host refill under an un-backed-up parent (#31902)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-07-27** [`ee1736f39a`](https://github.com/sgl-project/sglang/commit/ee1736f39a) [#30988](https://github.com/sgl-project/sglang/pull/30988)
  [LoRA] Support LoRA under the breakable/full prefill CUDA graph (#30988)
  _Files: `python/sglang/srt/lora/backend/ascend_backend.py`, `python/sglang/srt/lora/backend/base_backend.py`, `python/sglang/srt/lora/backend/chunked_backend.py`, `python/sglang/srt/lora/backend/torch_backend.py` _+9 more__
- **2026-07-26** [`2c63a2f12b`](https://github.com/sgl-project/sglang/commit/2c63a2f12b) [#32373](https://github.com/sgl-project/sglang/pull/32373)
  Fix --hicache-size allocating ~2x host memory on hybrid SWA (#32373)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`_
- **2026-07-25** [`7c4b22fae5`](https://github.com/sgl-project/sglang/commit/7c4b22fae5) [#31181](https://github.com/sgl-project/sglang/pull/31181)
  [Hicache][1/2]Support Mamba branching in Unified Radix Cache with HiCache (#31181)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/unified_cache_components/mamba_component.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-07-24** [`0a212c6119`](https://github.com/sgl-project/sglang/commit/0a212c6119) [#31086](https://github.com/sgl-project/sglang/pull/31086)
  [RL] DSV4: add env to quantize SWA KV cache from bf16-rounded values (#31086)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-07-24** [`5da0b6ec39`](https://github.com/sgl-project/sglang/commit/5da0b6ec39) [#31845](https://github.com/sgl-project/sglang/pull/31845)
  Write-back policy fix for unified tree (#31845)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/full_component.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-07-24** [`448662e85e`](https://github.com/sgl-project/sglang/commit/448662e85e) [#31826](https://github.com/sgl-project/sglang/pull/31826)
  [mm] Accept per-item embedding lists from DataEmbeddingFunc (#31826)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `test/registered/chunked_prefill/test_mm_chunked_embedding_unit.py`_
- **2026-07-24** [`1e10ec93b3`](https://github.com/sgl-project/sglang/commit/1e10ec93b3) [#23534](https://github.com/sgl-project/sglang/pull/23534)
  [XPU] Add XPU device support for LMCache radix cache integration (#23534)
  _Files: `.github/workflows/pr-test-xpu.yml`, `python/sglang/srt/mem_cache/storage/lmcache/lmc_radix_cache.py`, `python/sglang/srt/utils/common.py`, `test/registered/xpu/test_lmcache_connector.py` _+2 more__
- **2026-07-23** [`59ef3b15cc`](https://github.com/sgl-project/sglang/commit/59ef3b15cc) [#32184](https://github.com/sgl-project/sglang/pull/32184)
  [Fix] Reserve the mamba pool's +1 padding slot in the memory budget solve (#32184)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`_
- **2026-07-23** [`70ac0c4b0e`](https://github.com/sgl-project/sglang/commit/70ac0c4b0e) [#30986](https://github.com/sgl-project/sglang/pull/30986)
  [UnifiedRadixCache][mamba] Fix mamba state corruption and slot leak when load_back aborts (#30986)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/__init__.py`, `python/sglang/srt/mem_cache/unified_cache_components/mamba_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/tree_component.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+1 more__
- **2026-07-23** [`c18919f8f3`](https://github.com/sgl-project/sglang/commit/c18919f8f3) [#31230](https://github.com/sgl-project/sglang/pull/31230)
  [Mamba] Add a per-path cap for cached states (#31230)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/mamba_component.py`, `python/sglang/srt/server_args.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mamba.py`, `test/registered/unit/mem_cache/test_mamba_path_state_cap.py`_
- **2026-07-22** [`24da0e51b6`](https://github.com/sgl-project/sglang/commit/24da0e51b6) [#30938](https://github.com/sgl-project/sglang/pull/30938)
  Warn on small Mamba chunked prefill size (#30938)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-22** [`98cc8d91cf`](https://github.com/sgl-project/sglang/commit/98cc8d91cf) [#32016](https://github.com/sgl-project/sglang/pull/32016)
  [Fix] Evict only the KV shortfall in evict_from_tree_cache (#32016)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`_
- **2026-07-21** [`9057db9417`](https://github.com/sgl-project/sglang/commit/9057db9417) [#31982](https://github.com/sgl-project/sglang/pull/31982)
  Gate Mamba slot-donation debug asserts behind SGLANG_MAMBA_DEBUG_ASSERTS (#31982)
  _Files: `python/sglang/srt/mem_cache/mamba_radix_cache.py`, `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-07-21** [`1a53f231d6`](https://github.com/sgl-project/sglang/commit/1a53f231d6) [#31443](https://github.com/sgl-project/sglang/pull/31443)
  [HiCache]: Optimize hybrid/DSA L3 prefetch result sync and usable-prefix clamping (#31443)
  _Files: `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-07-21** [`f369a820d4`](https://github.com/sgl-project/sglang/commit/f369a820d4) [#31308](https://github.com/sgl-project/sglang/pull/31308)
  [HiCache] Remove redundant parameters of build_xxx_stack and others (#31308)
  _Files: `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-07-21** [`696e8f80d1`](https://github.com/sgl-project/sglang/commit/696e8f80d1) [#31871](https://github.com/sgl-project/sglang/pull/31871)
  [CI] Graceful teardown in kl_mamba hicache tests to release pinned host pool (#31871)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mamba.py`_
- **2026-07-20** [`49b9c46f41`](https://github.com/sgl-project/sglang/commit/49b9c46f41) [#27877](https://github.com/sgl-project/sglang/pull/27877)
  [dLLM] Reuse block KV/req slots in place across FDFO rounds (#27877)
  _Files: `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/allocation.py` _+1 more__

## Quantization  (17 commits)

- **2026-07-26** [`1d0cd2e473`](https://github.com/sgl-project/sglang/commit/1d0cd2e473) [#30613](https://github.com/sgl-project/sglang/pull/30613)
  [AMD] Nightly Test Coverage - Minimax-M3-MXFP8 Accuracy Test (#30613)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`_
- **2026-07-25** [`9402012f0f`](https://github.com/sgl-project/sglang/commit/9402012f0f) [#32296](https://github.com/sgl-project/sglang/pull/32296)
  [Perf] Halve the non-finite sanitization overhead in per_token_group_quant (#32296)
  _Files: `python/sglang/kernels/jit/csrc/gemm/per_token_group_quant.cuh`, `test/registered/kernels/benchmark/quantization/bench_per_token_group_quant.py`_
- **2026-07-25** [`7de8792758`](https://github.com/sgl-project/sglang/commit/7de8792758) [#31340](https://github.com/sgl-project/sglang/pull/31340)
  Fix FP8 Triton dtype selection on A100 (#31340)
  _Files: `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/kernels/ops/quantization/fp8_quantize.py`, `python/sglang/kernels/ops/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`_
- **2026-07-24** [`71015f3fea`](https://github.com/sgl-project/sglang/commit/71015f3fea) [#31346](https://github.com/sgl-project/sglang/pull/31346)
  fix(dsa): fail fast on fp8_e4m3 KV with tilelang DSA backend on CUDA (#31346)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `test/registered/unit/test_dsa_tilelang_fp8_validation.py`_
- **2026-07-24** [`15d73f1e03`](https://github.com/sgl-project/sglang/commit/15d73f1e03) [#32239](https://github.com/sgl-project/sglang/pull/32239)
  Fix dynamo recompile limit in allreduce and bf16 gemm (#32239)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/server_args.py`_
- **2026-07-23** [`d4a0dfbc31`](https://github.com/sgl-project/sglang/commit/d4a0dfbc31) [#32188](https://github.com/sgl-project/sglang/pull/32188)
  [Fix] Two root causes of the H100 deepep TBO CI break: scale-tensor use-after-free + missing non-finite quant sanitization (#32188)
  _Files: `python/sglang/kernels/jit/csrc/gemm/per_token_group_quant.cuh`, `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `test/registered/kernels/ops/quantization/test_per_token_group_quant.py`_
- **2026-07-23** [`845f6ad954`](https://github.com/sgl-project/sglang/commit/845f6ad954) [#31460](https://github.com/sgl-project/sglang/pull/31460)
  [MLX] Handle configs without quant_method in Humming (#31460)
- **2026-07-22** [`e7511141ea`](https://github.com/sgl-project/sglang/commit/e7511141ea) [#30567](https://github.com/sgl-project/sglang/pull/30567)
  Support CuteDSL GEMM BF16 on SM100 on by default when allowed by heuristic (#30567)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/server_args.py`_
- **2026-07-22** [`e8e765b9d6`](https://github.com/sgl-project/sglang/commit/e8e765b9d6) [#24651](https://github.com/sgl-project/sglang/pull/24651)
  [AMD] Add fused all-reduce RMSNorm per-group quant for Qwen3.5 FP8 (#24651)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `benchmark/kernels/all_reduce/benchmark_fused_ar_rms_quant_amd.py`, `python/sglang/srt/distributed/communication_op.py` _+5 more__
- **2026-07-22** [`4f88206393`](https://github.com/sgl-project/sglang/commit/4f88206393) [#32047](https://github.com/sgl-project/sglang/pull/32047)
  [CI] Fix stale per-token group quant callers (#32047)
  _Files: `sgl-kernel/benchmark/bench_per_token_group_quant_8bit.py`, `sgl-kernel/tests/test_per_token_group_quant_8bit.py`_
- **2026-07-22** [`7dcf3f7cbf`](https://github.com/sgl-project/sglang/commit/7dcf3f7cbf) [#31998](https://github.com/sgl-project/sglang/pull/31998)
  [Doc] Rename A5 product name (#31998)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quantization.mdx`_
- **2026-07-22** [`b54adced46`](https://github.com/sgl-project/sglang/commit/b54adced46) [#31825](https://github.com/sgl-project/sglang/pull/31825)
  [Quant] Support NVFP4_AWQ checkpoints in ModelOpt FP4 path (#31825)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/unit/model_loader/test_modelopt_loader.py`_
- **2026-07-21** [`0eae9423d8`](https://github.com/sgl-project/sglang/commit/0eae9423d8) [#31961](https://github.com/sgl-project/sglang/pull/31961)
  Change the FP8 per-tensor GEMM backend on SM120 to cuBLAS (#31961)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`_
- **2026-07-21** [`d6ef68881e`](https://github.com/sgl-project/sglang/commit/d6ef68881e) [#29131](https://github.com/sgl-project/sglang/pull/29131)
  [NPU] Adapt MiMo-V2.5-W8A8 (#29131)
  _Files: `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/manual/ascend/llm_models/test_npu_mimo_v2_5_w8a8.py`_
- **2026-07-21** [`bfefdc52d7`](https://github.com/sgl-project/sglang/commit/bfefdc52d7) [#31334](https://github.com/sgl-project/sglang/pull/31334)
  [CPU] Fix mxfp4 padding size (#31334)
  _Files: `python/sglang/srt/configs/update_config.py`, `python/sglang/srt/layers/quantization/mxfp4.py`_
- **2026-07-20** [`370f454e3d`](https://github.com/sgl-project/sglang/commit/370f454e3d) [#31456](https://github.com/sgl-project/sglang/pull/31456)
  [NPU] fix modelslim quant tensor name (#31456)
  _Files: `python/sglang/srt/layers/quantization/modelslim/modelslim.py`_
- **2026-07-20** [`829e9ce9d5`](https://github.com/sgl-project/sglang/commit/829e9ce9d5) [#31748](https://github.com/sgl-project/sglang/pull/31748)
  Lower AutoRound quantization MMLU threshold (#31748)
  _Files: `test/registered/quant/test_autoround_quantization.py`_

## Triton / Kernels  (17 commits)

- **2026-07-25** [`3079157175`](https://github.com/sgl-project/sglang/commit/3079157175) [#32354](https://github.com/sgl-project/sglang/pull/32354)
  Fix PyPI release: drop the git-only sgl-eval dep from packaged metadata (#32354)
  _Files: `python/pyproject.toml`, `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-07-24** [`dfaf75b1a6`](https://github.com/sgl-project/sglang/commit/dfaf75b1a6) [#30112](https://github.com/sgl-project/sglang/pull/30112)
  [NPU] bugfix for extra device memory on Ascend (#30112)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py`_
- **2026-07-24** [`3849beb7e3`](https://github.com/sgl-project/sglang/commit/3849beb7e3) [#32298](https://github.com/sgl-project/sglang/pull/32298)
  [CI] Fix XPU platform test on machines without the XPU sgl-kernel op (#32298)
  _Files: `test/registered/unit/platforms/test_platform_interface.py`_
- **2026-07-23** [`11b0e5c5ad`](https://github.com/sgl-project/sglang/commit/11b0e5c5ad) [#32148](https://github.com/sgl-project/sglang/pull/32148)
  [Kernel] Classification cleanup: unify _jit_ naming, drop empty/model groups, add elementwise (RFC #29630) (#32148)
- **2026-07-23** [`2d1a7be8c4`](https://github.com/sgl-project/sglang/commit/2d1a7be8c4) [#32128](https://github.com/sgl-project/sglang/pull/32128)
  [Kernel] Reclassify kernel tests by ops group + move helpers out of the package (RFC #29630) (#32128)
- **2026-07-23** [`60dea26077`](https://github.com/sgl-project/sglang/commit/60dea26077) [#13397](https://github.com/sgl-project/sglang/pull/13397)
  [sgl-kernel][CPU] add kernel for shm_allgather_into_tensor and shm_reduce_scatter_tensor (#13397)
  _Files: `sgl-kernel/csrc/cpu/interface.cpp`, `sgl-kernel/csrc/cpu/shm.cpp`, `sgl-kernel/csrc/cpu/shm.h`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp` _+1 more__
- **2026-07-23** [`99f636a86f`](https://github.com/sgl-project/sglang/commit/99f636a86f) [#32072](https://github.com/sgl-project/sglang/pull/32072)
  [Kernel] RFC #29630 finale: retire sglang.jit_kernel into sglang.kernels (#32072)
- **2026-07-22** [`b855efd9e6`](https://github.com/sgl-project/sglang/commit/b855efd9e6) [#32076](https://github.com/sgl-project/sglang/pull/32076)
  Fix Inkling kernel imports after migration (#32076)
  _Files: `python/sglang/srt/models/inkling_common/attn.py`, `python/sglang/srt/models/inkling_common/kernels/comm.py`_
- **2026-07-22** [`74338e94f1`](https://github.com/sgl-project/sglang/commit/74338e94f1) [#32045](https://github.com/sgl-project/sglang/pull/32045)
  [Kernel] Phase 4 batch-3: migrate tangled JIT subsystems + new groups into kernels.ops (RFC #29630) (#32045)
- **2026-07-22** [`246b3c3eaf`](https://github.com/sgl-project/sglang/commit/246b3c3eaf) [#31666](https://github.com/sgl-project/sglang/pull/31666)
  [Kernel] Phase 3+4: move JIT infra + operator groups into sglang.kernels (RFC #29630) (#31666)
- **2026-07-22** [`878d77929d`](https://github.com/sgl-project/sglang/commit/878d77929d) [#31897](https://github.com/sgl-project/sglang/pull/31897)
  [CPU] refactor rope kernels (#31897)
  _Files: `sgl-kernel/csrc/cpu/rope.cpp`, `sgl-kernel/csrc/cpu/vec.h`, `test/registered/cpu/test_rope.py`_
- **2026-07-22** [`03342e7732`](https://github.com/sgl-project/sglang/commit/03342e7732) [#30280](https://github.com/sgl-project/sglang/pull/30280)
  Delete sgl-kernel AOT router GEMM and fused A GEMM (#30280)
  _Files: `benchmark/kernels/deepseek/benchmark_deepgemm_dsv3_router_gemm_blackwell.py`, `python/sglang/jit_kernel/dsv3_fused_a_gemm.py`, `python/sglang/jit_kernel/dsv3_router_gemm.py`, `python/sglang/jit_kernel/fused_a_gemm.py` _+15 more__
- **2026-07-21** [`8260ade61b`](https://github.com/sgl-project/sglang/commit/8260ade61b) [#31919](https://github.com/sgl-project/sglang/pull/31919)
  [Bugfix] Fix CUDA import on non-CUDA platforms (#31919)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-07-21** [`fa0ced195e`](https://github.com/sgl-project/sglang/commit/fa0ced195e) [#30273](https://github.com/sgl-project/sglang/pull/30273)
  [XPU] Enable breakable prefill CUDA graph on XPU (#30273)
  _Files: `docs_new/docs/hardware-platforms/xpu.mdx`, `python/sglang/srt/model_executor/runner_backend_utils/breakable_cuda_graph/breakable_cuda_graph.py`, `python/sglang/srt/server_args.py`, `test/registered/xpu/test_breakable_cuda_graph.py`_
- **2026-07-20** [`e856eae921`](https://github.com/sgl-project/sglang/commit/e856eae921) [#27127](https://github.com/sgl-project/sglang/pull/27127)
  use sgl_kernel_npu rmsrope accelerate llada2 (#27127)
  _Files: `python/sglang/srt/models/llada2.py`_
- **2026-07-20** [`8bf2ab9be9`](https://github.com/sgl-project/sglang/commit/8bf2ab9be9) [#31649](https://github.com/sgl-project/sglang/pull/31649)
  Enable GPT-OSS TinyGEMM on CUDA 13 (#31649)
  _Files: `python/sglang/srt/models/gpt_oss.py`_
- **2026-07-20** [`5325cee7ea`](https://github.com/sgl-project/sglang/commit/5325cee7ea) [#31541](https://github.com/sgl-project/sglang/pull/31541)
  Bug fix in compress to support XPU (#31541)
  _Files: `python/sglang/jit_kernel/dsv4/compress.py`_

## Speculative Decoding  (13 commits)

- **2026-07-25** [`17afd8421f`](https://github.com/sgl-project/sglang/commit/17afd8421f) [#32393](https://github.com/sgl-project/sglang/pull/32393)
  [Spec] Share the grammar mask build and verify-tree staging across spec workers (#32393)
  _Files: `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/ngram_worker.py`, `python/sglang/srt/speculative/spec_utils.py`_
- **2026-07-25** [`3c5bf1f6d2`](https://github.com/sgl-project/sglang/commit/3c5bf1f6d2) [#32380](https://github.com/sgl-project/sglang/pull/32380)
  [Spec] Derive NGRAM grammar tree links on the host instead of reading back `retrive_next_token` (#32380)
  _Files: `python/sglang/srt/speculative/ngram_worker.py`, `test/registered/spec/test_spec_ngram.py`_
- **2026-07-25** [`cff20a2fbb`](https://github.com/sgl-project/sglang/commit/cff20a2fbb) [#32353](https://github.com/sgl-project/sglang/pull/32353)
  [Spec] Consolidate the grammar sync decision into ScheduleBatch.grammar_needs_sync (#32353)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/ngram_worker.py`, `python/sglang/srt/speculative/spec_info.py`_
- **2026-07-24** [`a31542ebd9`](https://github.com/sgl-project/sglang/commit/a31542ebd9) [#32308](https://github.com/sgl-project/sglang/pull/32308)
  [Feature] Add leveled invariant-check primitive for nan/inf/oob validity checks (#32308)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4_dspark.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py`, `python/sglang/srt/speculative/dspark_components/dspark_planner.py` _+3 more__
- **2026-07-24** [`d059b0f56e`](https://github.com/sgl-project/sglang/commit/d059b0f56e) [#32277](https://github.com/sgl-project/sglang/pull/32277)
  [Fix] Clamp degenerate all-sentinel draft rows to token 0 in dspark `_online_combine_kernel` (#32277)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_draft_model.py`, `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py`, `python/sglang/kernels/ops/speculative/reject_sampling.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py` _+1 more__
- **2026-07-24** [`f0f78a6c93`](https://github.com/sgl-project/sglang/commit/f0f78a6c93) [#30026](https://github.com/sgl-project/sglang/pull/30026)
  Add deterministic inference for eagle parity test (#30026)
  _Files: `python/sglang/test/kits/spec_server_kits.py`, `python/sglang/test/server_fixtures/spec_eagle_fixture.py`, `test/registered/spec/eagle/test_spec_eagle_parity.py`_
- **2026-07-23** [`a0728ea502`](https://github.com/sgl-project/sglang/commit/a0728ea502) [#32254](https://github.com/sgl-project/sglang/pull/32254)
  [spec decoding] fix inkling multi layer mtp draft extend cuda graph (#32254)
  _Files: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-07-23** [`f35411ee81`](https://github.com/sgl-project/sglang/commit/f35411ee81) [#32110](https://github.com/sgl-project/sglang/pull/32110)
  [Spec] Enable grammar overlap scheduling for STANDALONE speculative decoding (#32110)
  _Files: `python/sglang/srt/speculative/spec_info.py`, `test/registered/spec/test_spec_standalone.py`_
- **2026-07-22** [`024639a372`](https://github.com/sgl-project/sglang/commit/024639a372) [#31986](https://github.com/sgl-project/sglang/pull/31986)
  [Perf] Stack dspark dense draft per-layer ctx KV projection into one GEMM (#31986)
  _Files: `python/sglang/srt/models/dspark.py`, `test/registered/spec/dspark/test_dspark_stacked_ctx_kv_parity.py`_
- **2026-07-21** [`7c9257529f`](https://github.com/sgl-project/sglang/commit/7c9257529f) [#30437](https://github.com/sgl-project/sglang/pull/30437)
  [Mamba] Support speculative decoding with extra_buffer_lazy (#30437)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/spec_utils.py` _+1 more__
- **2026-07-21** [`9462c303a5`](https://github.com/sgl-project/sglang/commit/9462c303a5) [#31738](https://github.com/sgl-project/sglang/pull/31738)
  Fix stop boundaries for grammar-constrained speculative decoding (#31738)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_grammar_stop_speculative.py`_
- **2026-07-21** [`e7e8aaa73c`](https://github.com/sgl-project/sglang/commit/e7e8aaa73c) [#31488](https://github.com/sgl-project/sglang/pull/31488)
  Overlap grammar (constrained decoding) with speculative decode verify (#31488)
  _Files: `python/sglang/srt/constrained/xgrammar_backend.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py` _+8 more__
- **2026-07-20** [`35f2d4f761`](https://github.com/sgl-project/sglang/commit/35f2d4f761) [#31273](https://github.com/sgl-project/sglang/pull/31273)
  Fix no-padding CUDA graph admission (#31273)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`_

## Models  (11 commits)

- **2026-07-27** [`1d350aaad3`](https://github.com/sgl-project/sglang/commit/1d350aaad3) [#32400](https://github.com/sgl-project/sglang/pull/32400)
  fix(reasoning):  let --enable-strict-thinking works for DeepSeek-V4 (#32400)
  _Files: `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/parser/test_reasoning_parser.py`_
- **2026-07-27** [`9a0bd24bed`](https://github.com/sgl-project/sglang/commit/9a0bd24bed) [#32457](https://github.com/sgl-project/sglang/pull/32457)
  model: serve bare Qwen3Model backbone natively as an embedding model (#32457)
  _Files: `docs_new/docs/supported-models/embedding_models.mdx`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/qwen3_embedding.py`, `test/registered/unit/models/test_qwen3_embedding_registration.py`_
- **2026-07-26** [`2cbddb842d`](https://github.com/sgl-project/sglang/commit/2cbddb842d) [#30954](https://github.com/sgl-project/sglang/pull/30954)
  [DSV4/SM120] Allow fused MHC opt-in with standalone TileLang pre disabled (#30954)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/models/test_deepseek_v4_fused_mhc_policy.py`_
- **2026-07-25** [`953c587adf`](https://github.com/sgl-project/sglang/commit/953c587adf) [#31413](https://github.com/sgl-project/sglang/pull/31413)
  [Docs] Add Qwen3.6 35B NVFP4 to cookbook (#31413)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs_new/src/snippets/autoregressive/qwen36-deployment.jsx`_
- **2026-07-24** [`be7c13af07`](https://github.com/sgl-project/sglang/commit/be7c13af07) [#31752](https://github.com/sgl-project/sglang/pull/31752)
  [BugFix] Fix DS/Kimi crash on non-first PP ranks when resolving input length (#31752)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-07-23** [`b98a577fbe`](https://github.com/sgl-project/sglang/commit/b98a577fbe) [#32205](https://github.com/sgl-project/sglang/pull/32205)
  Doc/update ascend quickstart (#32205)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quick_start.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/qwen3_6_35b_a3b.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/model-tutorials/qwen3_6_35b_a3b.mdx`_
- **2026-07-22** [`40ac197fb2`](https://github.com/sgl-project/sglang/commit/40ac197fb2) [#32096](https://github.com/sgl-project/sglang/pull/32096)
  Fix get_server_args import lint error (#32096)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-07-22** [`297f9336c8`](https://github.com/sgl-project/sglang/commit/297f9336c8) [#31991](https://github.com/sgl-project/sglang/pull/31991)
  [Test] Enable mamba lazy extra buffer alloc edge case kl test in CI (#31991)
  _Files: `test/registered/models_e2e/test_qwen3_next_models.py`_
- **2026-07-22** [`4597dd4d88`](https://github.com/sgl-project/sglang/commit/4597dd4d88) [#28671](https://github.com/sgl-project/sglang/pull/28671)
  Fix reward/classification models broken by `load_weights` v2 dispatch (#28671) (#31988)
  _Files: `python/sglang/srt/models/llama_classification.py`, `python/sglang/srt/models/llama_reward.py`, `python/sglang/srt/models/qwen2_classification.py`, `python/sglang/srt/models/qwen2_rm.py`_
- **2026-07-21** [`4a55fdba0b`](https://github.com/sgl-project/sglang/commit/4a55fdba0b) [#31363](https://github.com/sgl-project/sglang/pull/31363)
  docs(cookbook): re-benchmark DeepSeek-V4 on sglang 0.5.15 (#31363)
  _Files: `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/benchmarks.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-migrate-model/SKILL.md` _+4 more__
- **2026-07-21** [`becf252e6c`](https://github.com/sgl-project/sglang/commit/becf252e6c) [#28671](https://github.com/sgl-project/sglang/pull/28671)
  AutoWeightLoader support Sglang native models 1: demo  (#28671)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/model_loader/auto_loader.py`, `python/sglang/srt/models/llama.py`, `python/sglang/srt/models/qwen2.py` _+2 more__

## Scheduler / Batching  (11 commits)

- **2026-07-27** [`5cc273a780`](https://github.com/sgl-project/sglang/commit/5cc273a780) [#32078](https://github.com/sgl-project/sglang/pull/32078)
  [feat] Opt-in flat response format for prompt top logprobs (#32078)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_flat_raw_top_logprobs.py`_
- **2026-07-26** [`61057bda6c`](https://github.com/sgl-project/sglang/commit/61057bda6c) [#32180](https://github.com/sgl-project/sglang/pull/32180)
  [BugFix] Prevent TBO crash when return_logprob is enabled (#32180)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`_
- **2026-07-26** [`72e415dfc8`](https://github.com/sgl-project/sglang/commit/72e415dfc8) [#32389](https://github.com/sgl-project/sglang/pull/32389)
  [Bugfix] Fix prefill suspension caused by delayed negotiate_should_allow_prefill invocation (#32389)
  _Files: `python/sglang/srt/managers/schedule_policy.py`_
- **2026-07-25** [`69a3c54c70`](https://github.com/sgl-project/sglang/commit/69a3c54c70) [#32379](https://github.com/sgl-project/sglang/pull/32379)
  Fix SWA admission livelock on cached-prefix resumes (#32379)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `test/registered/unit/managers/test_prefill_adder.py`_
- **2026-07-25** [`f9c14e6bd4`](https://github.com/sgl-project/sglang/commit/f9c14e6bd4) [#27139](https://github.com/sgl-project/sglang/pull/27139)
  [FEAT] Support fast engine recovery through weight cache (#27139)
  _Files: `.github/CODEOWNERS`, `python/sglang/srt/configs/load_config.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py` _+14 more__
- **2026-07-25** [`a690e5e0b3`](https://github.com/sgl-project/sglang/commit/a690e5e0b3) [#32363](https://github.com/sgl-project/sglang/pull/32363)
  Add stream label to TTFT metrics (#32363)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/observability/metrics_collector.py`_
- **2026-07-24** [`8727d105db`](https://github.com/sgl-project/sglang/commit/8727d105db) [#32245](https://github.com/sgl-project/sglang/pull/32245)
  Add prefill and decode load counters to LoadSnapshot (#32245)
  _Files: `python/sglang/srt/managers/load_snapshot.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/load_inquirer.py` _+1 more__
- **2026-07-23** [`d0b9689805`](https://github.com/sgl-project/sglang/commit/d0b9689805) [#32122](https://github.com/sgl-project/sglang/pull/32122)
  [Fix] Include disagg prefill waiting queue in FPM (#32122)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`_
- **2026-07-21** [`d03c8cee80`](https://github.com/sgl-project/sglang/commit/d03c8cee80) [#31835](https://github.com/sgl-project/sglang/pull/31835)
  Negotiate PrefillDelayer only after KV-budget admission checks (#31835)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `test/registered/unit/managers/test_prefill_adder.py`_
- **2026-07-20** [`fce5c75a30`](https://github.com/sgl-project/sglang/commit/fce5c75a30) [#31701](https://github.com/sgl-project/sglang/pull/31701)
  [NPU] Fix vit graph tnd cu seqlens (#31701)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`, `python/sglang/srt/managers/mm_utils.py`_
- **2026-07-20** [`b15a83983c`](https://github.com/sgl-project/sglang/commit/b15a83983c) [#31746](https://github.com/sgl-project/sglang/pull/31746)
  [Fix] Release hierarchical cache host pool on graceful shutdown (#31746)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/hicache/test_hicache_storage.py`_

## CI / Build  (11 commits)

- **2026-07-24** [`4ececf2b1d`](https://github.com/sgl-project/sglang/commit/4ececf2b1d) [#32349](https://github.com/sgl-project/sglang/pull/32349)
  [chore] Add verbose flag to twine upload command (#32349)
  _Files: `.github/workflows/release-pypi.yml`_
- **2026-07-24** [`f15b43242b`](https://github.com/sgl-project/sglang/commit/f15b43242b) [#32345](https://github.com/sgl-project/sglang/pull/32345)
  Bump sgl-deep-gemm to 0.1.5 (#32345)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`_
- **2026-07-24** [`bd3f6a7935`](https://github.com/sgl-project/sglang/commit/bd3f6a7935) [#32243](https://github.com/sgl-project/sglang/pull/32243)
  [CI] Remove redundant Rust cache save-if settings (#32243)
  _Files: `.github/workflows/pr-benchmark-rust.yml`, `.github/workflows/pr-test-rust.yml`_
- **2026-07-23** [`a2ddf92e61`](https://github.com/sgl-project/sglang/commit/a2ddf92e61) [#32211](https://github.com/sgl-project/sglang/pull/32211)
  [CI] Fix Mamba ServerArgs namespace (#32211)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-23** [`20f6a416e7`](https://github.com/sgl-project/sglang/commit/20f6a416e7) [#32193](https://github.com/sgl-project/sglang/pull/32193)
  [Tiny] Skip sm120 deepgemm test temporarily (#32193)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-07-23** [`5387e23ecd`](https://github.com/sgl-project/sglang/commit/5387e23ecd) [#32174](https://github.com/sgl-project/sglang/pull/32174)
  [Tiny]Correct runner for testing deepgemm (#32174)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-07-22** [`0bdd4730af`](https://github.com/sgl-project/sglang/commit/0bdd4730af) [#32091](https://github.com/sgl-project/sglang/pull/32091)
  [CI] Fix failures on main (#32091)
  _Files: `test/registered/unit/model_executor/model_runner_components/test_ngram_embedding_manager.py`_
- **2026-07-21** [`604b1507d2`](https://github.com/sgl-project/sglang/commit/604b1507d2) [#31939](https://github.com/sgl-project/sglang/pull/31939)
  Add Inkling to nightly test (#31939)
  _Files: `test/registered/8-gpu-models/test_inkling_nvfp4_nightly.py`_
- **2026-07-20** [`d1c2a1de08`](https://github.com/sgl-project/sglang/commit/d1c2a1de08) [#31777](https://github.com/sgl-project/sglang/pull/31777)
  [NPU] memfabric-zbal update (#31777)
  _Files: `docker/npu.Dockerfile`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-07-20** [`3f48245080`](https://github.com/sgl-project/sglang/commit/3f48245080) [#31764](https://github.com/sgl-project/sglang/pull/31764)
  [CI] Temporarily disable GB300 jobs (runner availability) (#31764)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/release-whl-deepgemm.yml`_
- **2026-07-20** [`2f14d6c6f2`](https://github.com/sgl-project/sglang/commit/2f14d6c6f2) [#31749](https://github.com/sgl-project/sglang/pull/31749)
  ci: run nvidia nightly every 2 days at 14:00 UTC (7am PT) (#31749)
  _Files: `.github/workflows/nightly-test-nvidia.yml`_

## ROCm / AMD  (8 commits)

- **2026-07-27** [`c6a6200a1a`](https://github.com/sgl-project/sglang/commit/c6a6200a1a) [#32469](https://github.com/sgl-project/sglang/pull/32469)
  [AMD] Fix pip setup in AMD Miles nightly builds (#32469)
  _Files: `.github/workflows/release-docker-amd-miles-rocm700-nightly.yml`, `.github/workflows/release-docker-amd-miles-rocm720-nightly.yml`_
- **2026-07-25** [`1ef2b85ef7`](https://github.com/sgl-project/sglang/commit/1ef2b85ef7) [#32347](https://github.com/sgl-project/sglang/pull/32347)
  chore: bump docs install version to 0.5.16 (#32347)
  _Files: `docs_new/docs/get-started/install.mdx`, `docs_new/docs/hardware-platforms/amd_gpu.mdx`_
- **2026-07-22** [`71fe649d68`](https://github.com/sgl-project/sglang/commit/71fe649d68) [#32069](https://github.com/sgl-project/sglang/pull/32069)
  [AMD] Register the Helios release workflow on main (#32069)
  _Files: `.github/workflows/release-docker-amd-rocm7_15-nightly.yml`_
- **2026-07-21** [`c4c405a46b`](https://github.com/sgl-project/sglang/commit/c4c405a46b) [#31615](https://github.com/sgl-project/sglang/pull/31615)
  [AMD] batch 3: register newly-added JIT kernel benchmarks for jit-kernel-benchmark-test-amd (#31615)
  _Files: `test/registered/jit/benchmark/bench_spec_topk1.py`, `test/registered/jit/benchmark/bench_vocab_parallel_embedding.py`_
- **2026-07-20** [`8905cbd42f`](https://github.com/sgl-project/sglang/commit/8905cbd42f) [#31837](https://github.com/sgl-project/sglang/pull/31837)
  Fix MiniMax-M3 crash on ROCm by making its override fields resolvable (#31837)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-07-20** [`54aaedd76d`](https://github.com/sgl-project/sglang/commit/54aaedd76d) [#31654](https://github.com/sgl-project/sglang/pull/31654)
  Clean up prefill CUDA graph runner (#31654)
  _Files: `python/sglang/srt/model_executor/runner/base_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_backend/tc_piecewise_cuda_graph_backend.py`, `python/sglang/srt/utils/aiter.py`_
- **2026-07-20** [`b6be150798`](https://github.com/sgl-project/sglang/commit/b6be150798) [#31792](https://github.com/sgl-project/sglang/pull/31792)
  [AMD] Split ROCm 7.2 Stage-B large 1-GPU tests into three partitions (#31792)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`_
- **2026-07-20** [`17fdd8487f`](https://github.com/sgl-project/sglang/commit/17fdd8487f) [#31737](https://github.com/sgl-project/sglang/pull/31737)
  [AMD] Update qwen3.5 cookbook (#31737)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs_new/src/snippets/autoregressive/qwen35-deployment.jsx`_

## Docs / Examples  (5 commits)

- **2026-07-27** [`082b2a10b6`](https://github.com/sgl-project/sglang/commit/082b2a10b6) [#32489](https://github.com/sgl-project/sglang/pull/32489)
  Add local ZIP uploader for whl releases (#32489)
  _Files: `scripts/release/README.md`, `scripts/release/update_others_whl_index.py`, `scripts/release/upload_zip_to_whl.sh`_
- **2026-07-24** [`319055c191`](https://github.com/sgl-project/sglang/commit/319055c191) [#31949](https://github.com/sgl-project/sglang/pull/31949)
  [Intel GPU] Add XPU Platform support (#31949)
  _Files: `docs_new/docs/hardware-platforms/plugin.mdx`, `python/sglang/srt/platforms/__init__.py`, `python/sglang/srt/platforms/xpu.py`, `test/registered/unit/platforms/test_platform_interface.py`_
- **2026-07-23** [`9bda6fdb9a`](https://github.com/sgl-project/sglang/commit/9bda6fdb9a) [#32127](https://github.com/sgl-project/sglang/pull/32127)
  docs: sync LMSYS SGLang blog cards (#32127)
  _Files: `docs_new/index.mdx`_
- **2026-07-21** [`9a6c96083f`](https://github.com/sgl-project/sglang/commit/9a6c96083f) [#31918](https://github.com/sgl-project/sglang/pull/31918)
  [Cookbook] Add Laguna-S-2.1 (#31918)
  _Files: `docs_new/cookbook/autoregressive/Poolside/Laguna-M.1.mdx`, `docs_new/cookbook/autoregressive/Poolside/Laguna-S-2.1.mdx`, `docs_new/cookbook/autoregressive/Poolside/Laguna-XS-2.1.mdx`, `docs_new/cookbook/autoregressive/intro.mdx` _+3 more__
- **2026-07-20** [`0a2d3ca071`](https://github.com/sgl-project/sglang/commit/0a2d3ca071) [#31823](https://github.com/sgl-project/sglang/pull/31823)
  [cookbook] Inkling: add measured accuracy numbers to benchmark cards (#31823)
  _Files: `docs_new/src/snippets/configs/thinkingmachines/inkling-benchmarks.jsx`, `docs_new/src/snippets/configs/thinkingmachines/inkling.jsx`_

## Structured Output  (4 commits)

- **2026-07-25** [`9989077f24`](https://github.com/sgl-project/sglang/commit/9989077f24) [#32412](https://github.com/sgl-project/sglang/pull/32412)
  Use native batched llguidance mask generation (#32412)
  _Files: `python/sglang/srt/constrained/base_grammar_backend.py`, `python/sglang/srt/constrained/llguidance_backend.py`, `python/sglang/srt/sampling/sampling_batch_info.py`, `test/registered/unit/constrained/test_llguidance_batched_mask.py` _+1 more__
- **2026-07-22** [`c20c48b8fd`](https://github.com/sgl-project/sglang/commit/c20c48b8fd) [#30832](https://github.com/sgl-project/sglang/pull/30832)
  Add 'anyOf' schema support for qwen3_coder tool call parser (#30832)
  _Files: `python/sglang/srt/function_call/qwen3_coder_detector.py`, `python/sglang/srt/function_call/utils.py`, `test/registered/unit/function_call/test_function_call_parser.py`_
- **2026-07-22** [`4eaa5ca651`](https://github.com/sgl-project/sglang/commit/4eaa5ca651) [#31975](https://github.com/sgl-project/sglang/pull/31975)
  Treat partial_json_parser AssertionError as incomplete JSON (#31975)
  _Files: `python/sglang/srt/function_call/utils.py`_
- **2026-07-21** [`2cf2e7377f`](https://github.com/sgl-project/sglang/commit/2cf2e7377f) [#31860](https://github.com/sgl-project/sglang/pull/31860)
  Fix dropped tool calls when a stream delta carries several (#31860)
  _Files: `python/sglang/srt/function_call/inkling_detector.py`, `test/registered/unit/function_call/test_function_call_parser.py`_

## Serving / API  (4 commits)

- **2026-07-25** [`ce705bb6dc`](https://github.com/sgl-project/sglang/commit/ce705bb6dc) [#32348](https://github.com/sgl-project/sglang/pull/32348)
  Report accelerator type in /v1/loads (#32348)
  _Files: `python/sglang/srt/entrypoints/v1_loads.py`, `test/registered/unit/entrypoints/test_v1_loads_aggregate.py`_
- **2026-07-23** [`410ab4fde5`](https://github.com/sgl-project/sglang/commit/410ab4fde5) [#30917](https://github.com/sgl-project/sglang/pull/30917)
  Add return_token_ids support to completions and chat completions APIs (#30917)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_completions.py`, `test/registered/unit/entrypoints/openai/test_protocol.py` _+2 more__
- **2026-07-23** [`7fe82dd02e`](https://github.com/sgl-project/sglang/commit/7fe82dd02e) [#32014](https://github.com/sgl-project/sglang/pull/32014)
  create rust workspace (#32014)
  _Files: `.github/workflows/lint.yml`, `.github/workflows/pr-test.yml`, `.pre-commit-config.yaml`, `python/pyproject.toml` _+21 more__
- **2026-07-20** [`7fc545b649`](https://github.com/sgl-project/sglang/commit/7fc545b649) [#31784](https://github.com/sgl-project/sglang/pull/31784)
  Align reasoning_effort schema across chat, tokenize, and responses (#31784)
  _Files: `docs_new/cookbook/autoregressive/ThinkingMachines/Inkling.mdx`, `python/sglang/srt/entrypoints/openai/protocol.py`_

## Tensor / Data Parallel  (3 commits)

- **2026-07-26** [`55c4853487`](https://github.com/sgl-project/sglang/commit/55c4853487) [#32339](https://github.com/sgl-project/sglang/pull/32339)
  [comm] Enable multi-node custom-AR v2 on a single NVLink clique (#32339)
  _Files: `python/sglang/kernels/jit/csrc/distributed/custom_all_reduce.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/distributed/communicator.cuh`, `python/sglang/srt/distributed/device_communicators/configs/custom_all_reduce_v2.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py` _+5 more__
- **2026-07-22** [`21065bc862`](https://github.com/sgl-project/sglang/commit/21065bc862) [#31076](https://github.com/sgl-project/sglang/pull/31076)
  feat: add native gRPC sidecar module launcher (#31076)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/sidecar.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-07-22** [`fc0cbb795d`](https://github.com/sgl-project/sglang/commit/fc0cbb795d) [#31841](https://github.com/sgl-project/sglang/pull/31841)
  [Misc] Add sm120 tests to DeepGemm release pipeline (#31841)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_

## LoRA  (1 commits)

- **2026-07-22** [`0a3cd26b28`](https://github.com/sgl-project/sglang/commit/0a3cd26b28) [#15912](https://github.com/sgl-project/sglang/pull/15912)
  LoRA: Ascend: Update ascend LoRA backend to support new kernels (#15912)
  _Files: `python/sglang/srt/lora/backend/ascend_backend.py`_

---
_Generated 2026-07-27 11:33 UTC_