# sgl-project/sglang — Weekly Change Report
**Period:** 2026-07-27 → 2026-08-03  |  **Total commits:** 297

## ✨ New Features This Week

- **2026-08-03** [#33103](https://github.com/sgl-project/sglang/pull/33103) — feat: rust sglang server openai apis (#33103)
- **2026-08-03** [#33136](https://github.com/sgl-project/sglang/pull/33136) — [CP] Support breakable CUDA graphs for zigzag strategy (#33136)
- **2026-08-03** [#33128](https://github.com/sgl-project/sglang/pull/33128) — Support DeepGEMM for standard MoE dispatch (#33128)
- **2026-08-03** [#33298](https://github.com/sgl-project/sglang/pull/33298) — [Spec] Support sampling in the DSPARK graph-folded draft proposal (#33298)
- **2026-08-03** [#33125](https://github.com/sgl-project/sglang/pull/33125) — [rust-server] PD disaggregation support (#33125)
- **2026-08-03** [#33105](https://github.com/sgl-project/sglang/pull/33105) — support dp attn with client lb (#33105)
- **2026-08-02** [#33150](https://github.com/sgl-project/sglang/pull/33150) — [BCG][4/N] Enable bcg on megamoe & flashinfer a2a backend (#33150)
- **2026-08-02** [#33112](https://github.com/sgl-project/sglang/pull/33112) — [Feat] DCP + HiCache L2 Support (ported from kimi-k3) (#33112)
- **2026-08-02** [#32392](https://github.com/sgl-project/sglang/pull/32392) — [NPU] Add PR test cases (#32392)
- **2026-08-02** [#33275](https://github.com/sgl-project/sglang/pull/33275) — [diffusion] model: support minimax-h3 (#33275)
- _…and 75 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-03** [`92999d84f4`](https://github.com/sgl-project/sglang/commit/92999d84f4) [#32046](https://github.com/sgl-project/sglang/pull/32046) — [AMD]Qwen3.5 integration gfx950 fmha fp8 hd256 (#32046)
- **2026-08-03** [`21d930aae3`](https://github.com/sgl-project/sglang/commit/21d930aae3) [#33195](https://github.com/sgl-project/sglang/pull/33195) — [AMD] Fix JIT compile failure in sgl_kernel/warp.cuh (#33195)
- **2026-08-02** [`12eadf86f1`](https://github.com/sgl-project/sglang/commit/12eadf86f1) [#31741](https://github.com/sgl-project/sglang/pull/31741) — [AMD] Enable mamba JIT transfer kernel on ROCm (fix transfer_kv_mamba NameError) (#31741)
- **2026-08-02** [`1685d29f21`](https://github.com/sgl-project/sglang/commit/1685d29f21) [#31727](https://github.com/sgl-project/sglang/pull/31727) — [AMD] Fix DeepSeek-V4 fused-RMS FP8 scale metadata on gfx950 (#31727)
- **2026-08-02** [`37be4e9247`](https://github.com/sgl-project/sglang/commit/37be4e9247) [#32315](https://github.com/sgl-project/sglang/pull/32315) — [AMD] Speed up DSV4 MoE weight loading from mmap views (#32315)
- **2026-08-02** [`7e509f690e`](https://github.com/sgl-project/sglang/commit/7e509f690e) [#31450](https://github.com/sgl-project/sglang/pull/31450) — [AMD] Fix DeepSeek-V4 FP4 MoE expert memory bloat (#31450)
- **2026-08-01** [`47d8b5b749`](https://github.com/sgl-project/sglang/commit/47d8b5b749) [#33170](https://github.com/sgl-project/sglang/pull/33170) — config: route parallel config-leaf reads through get_parallel() (#33170)
- **2026-08-01** [`2fd78ec2d7`](https://github.com/sgl-project/sglang/commit/2fd78ec2d7) [#31221](https://github.com/sgl-project/sglang/pull/31221) — [AMD] Derive AITER verify tokens-per-req from input shape (#31221)
- **2026-08-01** [`0d186f49be`](https://github.com/sgl-project/sglang/commit/0d186f49be) [#33090](https://github.com/sgl-project/sglang/pull/33090) — [AMD][Fix] Restore aiter-padded MoE weight dims for serialized checkpoints (#33090)
- **2026-07-31** [`70cec31378`](https://github.com/sgl-project/sglang/commit/70cec31378) [#32862](https://github.com/sgl-project/sglang/pull/32862) — [AMD] Pin mem_fraction_static for the piecewise CUDA graph 1-GPU test on MI300 (#32862)
- **2026-07-31** [`2573190b93`](https://github.com/sgl-project/sglang/commit/2573190b93) [#32837](https://github.com/sgl-project/sglang/pull/32837) — feat: support Kimi Linear PD disaggregation with DCP (#32837)
- **2026-07-30** [`48c1b37a33`](https://github.com/sgl-project/sglang/commit/48c1b37a33) [#32939](https://github.com/sgl-project/sglang/pull/32939) — [AMD] Update ROCm AITER pin to d9e5ef7 (#32939)
- **2026-07-30** [`fd86795107`](https://github.com/sgl-project/sglang/commit/fd86795107) [#32230](https://github.com/sgl-project/sglang/pull/32230) — [AMD] MiniMax-M3: opt-in custom/quick all-reduce on ROCm (#32230)
- **2026-07-30** [`04d6fb4d6c`](https://github.com/sgl-project/sglang/commit/04d6fb4d6c) [#32036](https://github.com/sgl-project/sglang/pull/32036) — [AMD] Minimax-M3 : unblock mxfp8 block convert on gfx950 (#32036)
- **2026-07-30** [`4b52758c76`](https://github.com/sgl-project/sglang/commit/4b52758c76) [#31924](https://github.com/sgl-project/sglang/pull/31924) — [AMD] Skip test_update_weights_from_disk on ROCm pending reload fix (#31924) (#31925)
- **2026-07-30** [`3d6e1e6f81`](https://github.com/sgl-project/sglang/commit/3d6e1e6f81) [#32879](https://github.com/sgl-project/sglang/pull/32879) — [AMD] Revert ROCm AITER pin to 9127c94 (#32879)
- **2026-07-29** [`bfc450248e`](https://github.com/sgl-project/sglang/commit/bfc450248e) [#31409](https://github.com/sgl-project/sglang/pull/31409) — [AMD] Replace MI325 with MI300 CI Runners (#31409)
- **2026-07-29** [`d12ea3e9ba`](https://github.com/sgl-project/sglang/commit/d12ea3e9ba) [#32760](https://github.com/sgl-project/sglang/pull/32760) — docker: add Kimi K3 images (#32760)
- **2026-07-29** [`f5bcd00e16`](https://github.com/sgl-project/sglang/commit/f5bcd00e16) [#31747](https://github.com/sgl-project/sglang/pull/31747) — [AMD] DSv4: bring HIP compress-state pool into the memory_saver KV_CACHE region (#31747)
- **2026-07-29** [`68673fe6c5`](https://github.com/sgl-project/sglang/commit/68673fe6c5) [#32613](https://github.com/sgl-project/sglang/pull/32613) — [AMD] add Gemma3RMSNorm.forward_hip to unbreak ROCm (#32613)
- **2026-07-28** [`4fe8f5218d`](https://github.com/sgl-project/sglang/commit/4fe8f5218d) [#32643](https://github.com/sgl-project/sglang/pull/32643) — [AMD] Add Kimi K3 ROCm 7.2 nightly image (#32643)
- **2026-07-28** [`9cffc2ba52`](https://github.com/sgl-project/sglang/commit/9cffc2ba52) [#32636](https://github.com/sgl-project/sglang/pull/32636) — [Kernel] Remove unused implementations and stale registry entries (#32636)
- **2026-07-28** [`2b6e01c673`](https://github.com/sgl-project/sglang/commit/2b6e01c673) [#32632](https://github.com/sgl-project/sglang/pull/32632) — [AMD] Run AITER Scout on Saturdays (#32632)
- **2026-07-27** [`7cae831e41`](https://github.com/sgl-project/sglang/commit/7cae831e41) [#32559](https://github.com/sgl-project/sglang/pull/32559) — Update mi35x ROCm image to k3-20260727 (#32559)
- **2026-07-27** [`c6a6200a1a`](https://github.com/sgl-project/sglang/commit/c6a6200a1a) [#32469](https://github.com/sgl-project/sglang/pull/32469) — [AMD] Fix pip setup in AMD Miles nightly builds (#32469)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#33383](https://github.com/sgl-project/sglang/issues/33383) | [AMD] EAGLE3 spec-decode unsupported for MiniMax-M3: minimax_sparse_ba | — | 2026-08-03 |
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-08-03 |
| [#26751](https://github.com/sgl-project/sglang/issues/26751) | [Bug] Gemma-4 mm: single non-RGB image crashes vision tower and kills  | — | 2026-08-03 |
| [#33356](https://github.com/sgl-project/sglang/issues/33356) | [Bug] DSpark large decode CUDA-Graph capture can hit non-deterministic | — | 2026-08-03 |
| [#27310](https://github.com/sgl-project/sglang/issues/27310) | [RFC] GPU Memory Service (GMS) integration for out-of-process GPU memo | — | 2026-08-03 |
| [#33185](https://github.com/sgl-project/sglang/issues/33185) | [Bug] DeepSeek-V4-Flash-0731: reasoning_effort mapped one level off —  | — | 2026-08-03 |
| [#32432](https://github.com/sgl-project/sglang/issues/32432) | [RFC] Define Metadata, Workspace, and Stream-Ownership Contracts for D | — | 2026-08-03 |
| [#31023](https://github.com/sgl-project/sglang/issues/31023) | [Bug] DSpark compact target-verify CUDA Graph transition can hit timin | — | 2026-08-03 |
| [#33355](https://github.com/sgl-project/sglang/issues/33355) | [Feature][DCP] symm_a2a backend: peer-direct A2A for MLA decode on sin | — | 2026-08-03 |
| [#33322](https://github.com/sgl-project/sglang/issues/33322) | [Feature]  Make diffusion LLM serving usable for RL rollout and high-t | — | 2026-08-03 |
| [#32925](https://github.com/sgl-project/sglang/issues/32925) | [RFC] Push-based Engine Load Reporting and Router Load Monitoring | — | 2026-08-03 |
| [#27937](https://github.com/sgl-project/sglang/issues/27937) | [Failure Tracker] PR Test (AMD) | — | 2026-08-03 |
| [#33292](https://github.com/sgl-project/sglang/issues/33292) | [Bug] [multimodal_gen] CustomOp.dispatch_forward() XPU breaking model  | — | 2026-08-02 |
| [#32607](https://github.com/sgl-project/sglang/issues/32607) | [Feature] Kimi K3 Roadmap | — | 2026-08-02 |
| [#33181](https://github.com/sgl-project/sglang/issues/33181) | [Bug] Inkling reasoning parser leaks the tool name into visible conten | — | 2026-08-01 |
| [#29630](https://github.com/sgl-project/sglang/issues/29630) | [RFC] Introduce a unified sglang.kernels namespace for kernel organiza | RFC, jit-kernel, kernel | 2026-08-01 |
| [#29738](https://github.com/sgl-project/sglang/issues/29738) | [Bug] NameError: name 'deep_gemm' is not defined in tf32_hc_prenorm_ge | — | 2026-08-01 |
| [#32968](https://github.com/sgl-project/sglang/issues/32968) | [Bug][kimi-k3] Long-context [PAD] (id 163839) storms + DSPARK inf/nan  | kimi | 2026-08-01 |
| [#32960](https://github.com/sgl-project/sglang/issues/32960) | [Bug] Kimi-K3: a literal <|kimi_image_placeholder|> in message text re | kimi | 2026-08-01 |
| [#33142](https://github.com/sgl-project/sglang/issues/33142) | [Bug] ROCm diffusion fused-norm kernels depend on non-public FlyDSL AP | — | 2026-07-31 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 62 |
| Other | 33 |
| MoE / Expert Parallel | 33 |
| Multimodal | 32 |
| Prefill / Decode Disaggregation | 26 |
| KV Cache / Memory | 19 |
| Docs / Examples | 18 |
| Quantization | 13 |
| Speculative Decoding | 10 |
| ROCm / AMD | 9 |
| Scheduler / Batching | 9 |
| Models | 8 |
| Triton / Kernels | 7 |
| Tensor / Data Parallel | 4 |
| Structured Output | 4 |
| CI / Build | 4 |
| Serving / API | 4 |
| LoRA | 2 |

## Attention / FlashInfer  (62 commits)

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
- **2026-08-02** [`1a3bea77f2`](https://github.com/sgl-project/sglang/commit/1a3bea77f2) [#33112](https://github.com/sgl-project/sglang/pull/33112)
  [Feat] DCP + HiCache L2 Support (ported from kimi-k3) (#33112)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool_host.py` _+5 more__
- **2026-08-02** [`0877a0e2f1`](https://github.com/sgl-project/sglang/commit/0877a0e2f1) [#33254](https://github.com/sgl-project/sglang/pull/33254)
  [CI] Add speculative_draft_attention_backend to the page-constraint test view (#33254)
  _Files: `test/registered/unit/test_model_overrides.py`_
- **2026-08-02** [`8d106c3d79`](https://github.com/sgl-project/sglang/commit/8d106c3d79) [#31948](https://github.com/sgl-project/sglang/pull/31948)
  [NPU] Enable automatic ascend_attn selection for vision attention and graph runners (#31948)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/multimodal/internvl_vit_cuda_graph_runner.py`, `python/sglang/srt/multimodal/vit_cuda_graph_runner.py` _+2 more__
- **2026-08-01** [`131bd51b01`](https://github.com/sgl-project/sglang/commit/131bd51b01) [#25545](https://github.com/sgl-project/sglang/pull/25545)
  [Spec] Add `trtllm_mha` support for Gemma 4 MTP draft attention backend (#25545)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/speculative/frozen_kv_mtp_cuda_graph_runner.py`, `python/sglang/srt/speculative/frozen_kv_mtp_worker_v2.py`, `test/registered/attention/unittests/dense/test_trtllm_mha.py`_
- **2026-08-01** [`f1b41a5b3d`](https://github.com/sgl-project/sglang/commit/f1b41a5b3d) [#33100](https://github.com/sgl-project/sglang/pull/33100)
  [CP]: FIx some issue for glm5.2 cp v2 (#33100)
  _Files: `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/server_args.py`_
- **2026-08-01** [`00a219f6c9`](https://github.com/sgl-project/sglang/commit/00a219f6c9) [#32843](https://github.com/sgl-project/sglang/pull/32843)
  [Quant] Keep the flashinfer_deepgemm FP8 GEMM to 1 <= M < 32 (#32843)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-08-01** [`ae84811666`](https://github.com/sgl-project/sglang/commit/ae84811666) [#33109](https://github.com/sgl-project/sglang/pull/33109)
  [Docs] Add verified H200 and B200 DeepSeek-V4 Flash Official results (#33109)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-08-01** [`2fd78ec2d7`](https://github.com/sgl-project/sglang/commit/2fd78ec2d7) [#31221](https://github.com/sgl-project/sglang/pull/31221)
  [AMD] Derive AITER verify tokens-per-req from input shape (#31221)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-08-01** [`fd96a35fb0`](https://github.com/sgl-project/sglang/commit/fd96a35fb0) [#32649](https://github.com/sgl-project/sglang/pull/32649)
  add NPU GSM8K accuracy tests for 7 models (#32649)
  _Files: `.github/workflows/pr-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/ascend/accuracy/glm4_7_flash/test_npu_glm4_7_flash_1p_gsm8k.py`, `test/registered/ascend/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py` _+4 more__
- **2026-08-01** [`bae8eb8d6c`](https://github.com/sgl-project/sglang/commit/bae8eb8d6c) [#30971](https://github.com/sgl-project/sglang/pull/30971)
  [minimax-m3] fp8 attention GEMMs on SM100 (fp8_e4m3 KV + trtllm_mha) (#30971)
  _Files: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `python/sglang/kernels/ops/attention/minimax_decode_topk.py`, `python/sglang/kernels/ops/attention/minimax_sparse/common/utils.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py` _+19 more__
- **2026-08-01** [`934a13ce3e`](https://github.com/sgl-project/sglang/commit/934a13ce3e) [#33116](https://github.com/sgl-project/sglang/pull/33116)
  [Inkling] Hold the short-conv per-step state on one metadata struct (#33116)
  _Files: `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/models/inkling_common/sconv.py`, `test/registered/unit/models/test_inkling_sconv_metadata_once.py`_
- **2026-08-01** [`ca07917c58`](https://github.com/sgl-project/sglang/commit/ca07917c58) [#33127](https://github.com/sgl-project/sglang/pull/33127)
  [Fix] Bound FULL_MASK verify-mask reuse by the captured max_bs (#33127)
  _Files: `python/sglang/srt/layers/attention/verify_mask.py`, `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/unit/layers/attention/test_verify_mask.py`_
- **2026-08-01** [`1496bfee93`](https://github.com/sgl-project/sglang/commit/1496bfee93) [#32828](https://github.com/sgl-project/sglang/pull/32828)
  [Kimi] Support DCP + DSpark (ported from kimi-k3 branch) (#32828)
  _Files: `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/pool_configurator.py` _+4 more__
- **2026-07-31** [`3c5f115741`](https://github.com/sgl-project/sglang/commit/3c5f115741) [#32708](https://github.com/sgl-project/sglang/pull/32708)
  Split #32584 into 2/2: [LoRA] Shard attention LoRA by attn-TP and allow dynamic LoRA with dp attention (#32708)
  _Files: `python/sglang/srt/lora/layers.py`, `python/sglang/srt/lora/lora_manager.py`, `python/sglang/srt/lora/mem_pool.py`, `python/sglang/srt/lora/utils.py` _+3 more__
- **2026-07-31** [`4480e2a051`](https://github.com/sgl-project/sglang/commit/4480e2a051) [#33087](https://github.com/sgl-project/sglang/pull/33087)
  [Fix] Repair verify mask test fixture (#33087)
  _Files: `python/sglang/srt/layers/attention/verify_mask.py`, `test/registered/unit/layers/attention/test_verify_mask.py`_
- **2026-07-31** [`7e996a5d0d`](https://github.com/sgl-project/sglang/commit/7e996a5d0d) [#32707](https://github.com/sgl-project/sglang/pull/32707)
  Split #32584 into 1/2: [LoRA] Guard DP-attention idle forwards against stale LoRA batch state (#32707)
  _Files: `python/sglang/srt/lora/backend/base_backend.py`, `python/sglang/srt/lora/backend/triton_backend.py`, `python/sglang/srt/lora/deepseek_mla_correction.py`, `python/sglang/srt/lora/layers.py` _+4 more__
- **2026-07-31** [`94743f934c`](https://github.com/sgl-project/sglang/commit/94743f934c) [#33083](https://github.com/sgl-project/sglang/pull/33083)
  [Docs] Add DeepSeek-V4 Flash Official (0731) recipe (#33083)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/_playground.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-07-31** [`77c77a3da8`](https://github.com/sgl-project/sglang/commit/77c77a3da8) [#33023](https://github.com/sgl-project/sglang/pull/33023)
  feat(inkling): migrate short convs onto the ShortConv attention backend (#33023)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py` _+12 more__
- **2026-07-31** [`d3222bcc3a`](https://github.com/sgl-project/sglang/commit/d3222bcc3a) [#33046](https://github.com/sgl-project/sglang/pull/33046)
  [unified-memory] Support fa3, the default MLA backend on pre-Blackwell hosts (#33046)
  _Files: `python/sglang/kernels/ops/attention/metadata.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py` _+5 more__
- **2026-07-31** [`e3d4f48e55`](https://github.com/sgl-project/sglang/commit/e3d4f48e55) [#32690](https://github.com/sgl-project/sglang/pull/32690)
  [Fix] missing max_context_len on HybridAttnBackend (#32690)
  _Files: `python/sglang/srt/layers/attention/hybrid_attn_backend.py`, `test/registered/attention/test_trtllm_mha_graph_metadata.py`, `test/registered/unit/model_executor/model_runner_components/test_attention_backend_setup.py`, `test/registered/unit/spec/test_dflash_overlap_hostsync.py`_
- **2026-07-31** [`754b692afc`](https://github.com/sgl-project/sglang/commit/754b692afc) [#31854](https://github.com/sgl-project/sglang/pull/31854)
  [diffusion] optimization: support cuda-ipc zero-staging all-to-all for 2-rank Ulysses (#31854)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/base_device_communicator.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py` _+5 more__
- **2026-07-31** [`33c27d8e7f`](https://github.com/sgl-project/sglang/commit/33c27d8e7f) [#32972](https://github.com/sgl-project/sglang/pull/32972)
  [unified-memory] Let Kimi-Linear use the paged MLA attention backends (#32972)
  _Files: `python/sglang/kernels/ops/kvcache/kv_indices.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+5 more__
- **2026-07-31** [`5c6635d8f3`](https://github.com/sgl-project/sglang/commit/5c6635d8f3) [#32920](https://github.com/sgl-project/sglang/pull/32920)
  [Spec] Compact the target-verify mask when nothing reads it (#32920)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` _+13 more__
- **2026-07-31** [`e23ccb15f0`](https://github.com/sgl-project/sglang/commit/e23ccb15f0) [#32971](https://github.com/sgl-project/sglang/pull/32971)
  [unified-memory] Support MLA-hybrid-Mamba (Kimi-Linear) on the Triton backend (#32971)
  _Files: `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/layout/page_major.py` _+6 more__
- **2026-07-31** [`425349b799`](https://github.com/sgl-project/sglang/commit/425349b799) [#31128](https://github.com/sgl-project/sglang/pull/31128)
  [Perf][DSA] Pass topk_length to flash_mla_sparse_fwd in the sparse attention path (#31128)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`_
- **2026-07-31** [`0aefba7283`](https://github.com/sgl-project/sglang/commit/0aefba7283) [#32490](https://github.com/sgl-project/sglang/pull/32490)
  fix(dsa): correct packed FlashInfer top-k and backend selection semantics (#32490)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/kernels/ops/attention/test_dsa_indexer.py`_
- **2026-07-31** [`55c1963df4`](https://github.com/sgl-project/sglang/commit/55c1963df4) [#31430](https://github.com/sgl-project/sglang/pull/31430)
  Remove unused draft-extend CUDA graph top-k (#31430)
  _Files: `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_draft_extend_runner.py`_
- **2026-07-30** [`5339450ed4`](https://github.com/sgl-project/sglang/commit/5339450ed4) [#32595](https://github.com/sgl-project/sglang/pull/32595)
  Support SGLANG_SIMULATE_ACC_LEN for DFLASH (#32595)
  _Files: `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-07-30** [`b78d3999b5`](https://github.com/sgl-project/sglang/commit/b78d3999b5) [#32791](https://github.com/sgl-project/sglang/pull/32791)
  【NPU】fix decode MTP + eagle shape error (#32791)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-07-30** [`6ab3231b97`](https://github.com/sgl-project/sglang/commit/6ab3231b97) [#32886](https://github.com/sgl-project/sglang/pull/32886)
  [Perf] Skip the target-verify tree mask fill when the backend never reads it (#32886)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/hybrid_attn_backend.py` _+4 more__
- **2026-07-30** [`f46d5f25b4`](https://github.com/sgl-project/sglang/commit/f46d5f25b4) [#30482](https://github.com/sgl-project/sglang/pull/30482)
  [4/N][CP] Support interleave strategy for cp v2 (#30482)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/cp/base.py` _+11 more__
- **2026-07-30** [`c192145830`](https://github.com/sgl-project/sglang/commit/c192145830) [#32813](https://github.com/sgl-project/sglang/pull/32813)
  [Kernel] Fuse KV-cache writes for asymmetric K/V (head_dim != v_head_dim) (#32813)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/kvcache.cuh`, `python/sglang/kernels/ops/kvcache/kvcache.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/kernels/benchmark/kvcache/bench_store_cache.py` _+2 more__
- **2026-07-30** [`ed361ae7f0`](https://github.com/sgl-project/sglang/commit/ed361ae7f0) [#32625](https://github.com/sgl-project/sglang/pull/32625)
  Fix attention backends for models with per-layer head counts (num_attention_heads_per_layer) (#32625)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dense_attention.py` _+8 more__
- **2026-07-30** [`62dfaaa0e0`](https://github.com/sgl-project/sglang/commit/62dfaaa0e0) [#32555](https://github.com/sgl-project/sglang/pull/32555)
  [Nemotron] Fix decode track-save reading the stale tail of the CUDA-graph track buffer (#32555)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `test/registered/radix_cache/test_mamba2_extra_buffer_kl.py`_
- **2026-07-30** [`8fbf960980`](https://github.com/sgl-project/sglang/commit/8fbf960980) [#32115](https://github.com/sgl-project/sglang/pull/32115)
  [MLX] Size request capacity by attention DP (#32115)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `test/registered/unit/hardware_backend/mlx/test_attn_dp_request_capacity.py`_
- **2026-07-30** [`1d9c292547`](https://github.com/sgl-project/sglang/commit/1d9c292547) [#32788](https://github.com/sgl-project/sglang/pull/32788)
  [Kernel] Add inventory guards and clean benchmark layout (#32788)
  _Files: `benchmark/kernels/attention/bench_flash_attention_fp8.py`, `benchmark/kernels/attention/bench_gdn_replayssm_decode.py`, `benchmark/kernels/attention/fa4_benchmark_utils.py`, `benchmark/kernels/attention/sm90_config_search.py` _+10 more__
- **2026-07-30** [`a55e1764a2`](https://github.com/sgl-project/sglang/commit/a55e1764a2) [#32668](https://github.com/sgl-project/sglang/pull/32668)
  Enable GPT-OSS FlashInfer MXFP4 on SM120 (#32668)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `test/registered/unit/layers/quantization/test_mxfp4_sm120_cutlass.py`_
- **2026-07-29** [`fddfc1fb5e`](https://github.com/sgl-project/sglang/commit/fddfc1fb5e) [#29735](https://github.com/sgl-project/sglang/pull/29735)
  [GDN] Support FlashInfer GDN prefill with extra-buffer radix cache (#29735)
  _Files: `docs_new/docs/advanced_features/attention_backend.mdx`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py` _+5 more__
- **2026-07-29** [`1c6a0e91e1`](https://github.com/sgl-project/sglang/commit/1c6a0e91e1) [#31563](https://github.com/sgl-project/sglang/pull/31563)
  fix mqa preshuffle layout issue for deepseek v4 (#31563)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/kernels/ops/attention/dsa/index_buf_accessor.py`, `python/sglang/kernels/ops/attention/dsv4/compress.py`, `python/sglang/kernels/ops/kvcache/triton_store_cache.py` _+2 more__
- **2026-07-29** [`0ebbe43dbb`](https://github.com/sgl-project/sglang/commit/0ebbe43dbb) [#32695](https://github.com/sgl-project/sglang/pull/32695)
  fix(diffusion): size VSA top-k from padded blocks (#32695)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/video_sparse_attn.py`, `python/sglang/multimodal_gen/test/unit/test_video_sparse_attention.py`_
- **2026-07-29** [`d004a15a3e`](https://github.com/sgl-project/sglang/commit/d004a15a3e) [#32371](https://github.com/sgl-project/sglang/pull/32371)
  Fix GLM4-7B-Flash accuracy test configuration, tune Qwen3.6-27B/35B performance test parameters, and harden Ascend NPU multi-node E2E test utilities against pod name format errors. (#32371)
  _Files: `python/sglang/test/ascend/e2e/run_npu_e2e_test.py`, `python/sglang/test/ascend/e2e/test_npu_multi_node_utils.py`, `test/registered/ascend/accuracy/glm4_7_flash/test_npu_glm4_7_flash_1p_aime25.py`, `test/registered/ascend/accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_1p_gpqa.py` _+2 more__
- **2026-07-29** [`d12ea3e9ba`](https://github.com/sgl-project/sglang/commit/d12ea3e9ba) [#32760](https://github.com/sgl-project/sglang/pull/32760)
  docker: add Kimi K3 images (#32760)
  _Files: `docker/kimi_k3/apply_deepep_k3_patch.sh`, `docker/kimi_k3/apply_deepgemm_situ_patch.py`, `docker/kimi_k3/flashinfer-perkz-dcp-0.6.15.txt`, `docker/kimi_k3/kimi_k3_cu12.Dockerfile` _+2 more__
- **2026-07-29** [`1b9dfa14e6`](https://github.com/sgl-project/sglang/commit/1b9dfa14e6) [#32318](https://github.com/sgl-project/sglang/pull/32318)
  Fix FlashInfer MNNVL workspace size check (#32318)
  _Files: `python/sglang/srt/layers/flashinfer_comm_fusion.py`_
- **2026-07-29** [`7dcebca255`](https://github.com/sgl-project/sglang/commit/7dcebca255) [#32118](https://github.com/sgl-project/sglang/pull/32118)
  Fix nightly CI: NVFP4 cuda-graph crash, NVILA batching, CuTe paged-KV zero-size, Kimi-VL OOM (#32118)
  _Files: `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py`, `python/sglang/srt/models/kimi_vl.py`, `python/sglang/srt/models/kimi_vl_moonvit.py`, `python/sglang/srt/models/nvila.py` _+1 more__
- **2026-07-29** [`ef6c07008b`](https://github.com/sgl-project/sglang/commit/ef6c07008b) [#32612](https://github.com/sgl-project/sglang/pull/32612)
  Support DCP for Kimi Linear model (#32612)
  _Files: `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/cutedsl_mla_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py` _+13 more__
- **2026-07-29** [`339bef7fad`](https://github.com/sgl-project/sglang/commit/339bef7fad) [#32447](https://github.com/sgl-project/sglang/pull/32447)
  [MLX] Fix overlap-loop request bookkeeping and graceful shutdown (#32447)
  _Files: `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`, `test/registered/unit/hardware_backend/mlx/test_scheduler_mixin.py`_
- **2026-07-29** [`d86492fea0`](https://github.com/sgl-project/sglang/commit/d86492fea0) [#31739](https://github.com/sgl-project/sglang/pull/31739)
  [NPU] adapt dflash v2 on npu (#31739)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-07-28** [`7f438a6031`](https://github.com/sgl-project/sglang/commit/7f438a6031) [#26928](https://github.com/sgl-project/sglang/pull/26928)
  feat: SM120 (Blackwell Desktop) support for GLM-5.1 inference (#26928)
  _Files: `python/sglang/kernels/ops/attention/flash_mla_sm120.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/server_args.py` _+5 more__
- **2026-07-28** [`4e5a05148a`](https://github.com/sgl-project/sglang/commit/4e5a05148a) [#30825](https://github.com/sgl-project/sglang/pull/30825)
  [FullCG] Support chunked cached-prefix prefill (#30825)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/hybrid_attn_backend.py`, `python/sglang/srt/model_executor/cuda_graph_config.py` _+6 more__
- **2026-07-28** [`a24906a091`](https://github.com/sgl-project/sglang/commit/a24906a091) [#30090](https://github.com/sgl-project/sglang/pull/30090)
  [diffusion] feat: add dynamic cuDNN SDPA attention backend (#30090)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py` _+2 more__
- **2026-07-28** [`d9cf7b0a8b`](https://github.com/sgl-project/sglang/commit/d9cf7b0a8b) [#32219](https://github.com/sgl-project/sglang/pull/32219)
  [MTP] Cut spec-v2 host-seam overhead in hybrid-linear MTP decode (#32219)
  _Files: `python/sglang/kernels/ops/mamba/mamba_state_indices_triton.py`, `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py` _+3 more__
- **2026-07-27** [`5a46e16f01`](https://github.com/sgl-project/sglang/commit/5a46e16f01) [#31629](https://github.com/sgl-project/sglang/pull/31629)
  [Fix] Enable graph capture and MSCCL++ for attention TP groups (#31629)
  _Files: `python/sglang/srt/distributed/parallel_state.py`_
- **2026-07-27** [`1da062f018`](https://github.com/sgl-project/sglang/commit/1da062f018) [#31840](https://github.com/sgl-project/sglang/pull/31840)
  [Inkling] Add minimal DFLASH support (#31840)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/srt/models/inkling.py` _+2 more__
- **2026-07-27** [`db9143ee08`](https://github.com/sgl-project/sglang/commit/db9143ee08) [#32210](https://github.com/sgl-project/sglang/pull/32210)
  [NPU] Fix MTP IndexShare warm-up for attention DP and prefill CP (#32210)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-07-27** [`08af5aea57`](https://github.com/sgl-project/sglang/commit/08af5aea57) [#32383](https://github.com/sgl-project/sglang/pull/32383)
  optimize: optimize EmbeddingGemma prefill performance (#32383)
  _Files: `docs_new/cookbook/autoregressive/Google/EmbeddingGemma.mdx`, `docs_new/docs.json`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/layernorm.py` _+3 more__
- **2026-07-27** [`abb8f4b5e3`](https://github.com/sgl-project/sglang/commit/abb8f4b5e3) [#32375](https://github.com/sgl-project/sglang/pull/32375)
  model: support EmbeddingGemma (#32375)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/pooler.py`, `python/sglang/srt/managers/scheduler.py` _+8 more__

## Other  (33 commits)

- **2026-08-03** [`d48ab2d386`](https://github.com/sgl-project/sglang/commit/d48ab2d386) [#33371](https://github.com/sgl-project/sglang/pull/33371)
  Fix BCG circular import during server startup (#33371)
  _Files: `python/sglang/srt/layers/cp/bcg.py`_
- **2026-08-03** [`8186eeb939`](https://github.com/sgl-project/sglang/commit/8186eeb939) [#33026](https://github.com/sgl-project/sglang/pull/33026)
  [rust-server] Reland: fix TCP-layer TTFT stalls (#33026) (#33269)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/sglang-server/Cargo.toml`, `rust/sglang-server/src/api_server.rs` _+1 more__
- **2026-08-03** [`741e33db81`](https://github.com/sgl-project/sglang/commit/741e33db81) [#32525](https://github.com/sgl-project/sglang/pull/32525)
  fix(sampling): reject conflicting structural tag constraints (#32525)
  _Files: `python/sglang/srt/sampling/sampling_params.py`, `test/registered/unit/sampling/test_sampling_params.py`_
- **2026-08-02** [`ec741e4161`](https://github.com/sgl-project/sglang/commit/ec741e4161) [#33276](https://github.com/sgl-project/sglang/pull/33276)
  Fix DSpark loading for hybrid DSV4 NVFP4 (#33276)
  _Files: `python/sglang/srt/model_loader/loader.py`_
- **2026-08-02** [`06554515f4`](https://github.com/sgl-project/sglang/commit/06554515f4) [#33257](https://github.com/sgl-project/sglang/pull/33257)
  Revert "[rust-server] fix TCP-layer TTFT stalls" (#33257)
  _Files: `rust/sglang-server/src/api_server.rs`, `rust/sglang-server/src/runtime.rs`_
- **2026-08-01** [`574ead753a`](https://github.com/sgl-project/sglang/commit/574ead753a) [#33026](https://github.com/sgl-project/sglang/pull/33026)
  [rust-server] fix TCP-layer TTFT stalls (#33026)
  _Files: `rust/sglang-server/src/api_server.rs`, `rust/sglang-server/src/runtime.rs`_
- **2026-08-01** [`7071cfb873`](https://github.com/sgl-project/sglang/commit/7071cfb873) [#33172](https://github.com/sgl-project/sglang/pull/33172)
  runtime_context: per-role namespace enforcement behind SGLANG_ROLE_NAMESPACES (#33172)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/runtime_context.py`, `test/registered/unit/test_runtime_context_config_bags.py`_
- **2026-08-01** [`33ecf4bcd8`](https://github.com/sgl-project/sglang/commit/33ecf4bcd8) [#31952](https://github.com/sgl-project/sglang/pull/31952)
  Add pr tests (#31952)
- **2026-07-31** [`55b6769b0e`](https://github.com/sgl-project/sglang/commit/55b6769b0e) [#33013](https://github.com/sgl-project/sglang/pull/33013)
  config: read resolved config via namespace accessors (#33013)
- **2026-07-31** [`1d640aaea2`](https://github.com/sgl-project/sglang/commit/1d640aaea2) [#32981](https://github.com/sgl-project/sglang/pull/32981)
  bump dynamo-tokenizers to 1.7.0 (#32981)
  _Files: `rust/Cargo.lock`, `rust/sglang-server/Cargo.toml`, `rust/sglang-server/src/api_server/frame.rs`, `rust/sglang-server/src/message/finish_reason.rs`_
- **2026-07-31** [`5f9b0db18c`](https://github.com/sgl-project/sglang/commit/5f9b0db18c) [#32896](https://github.com/sgl-project/sglang/pull/32896)
  Fix async loading of RunAI-streamed tensors (#32896)
  _Files: `python/sglang/srt/model_loader/utils.py`, `test/registered/unit/model_loader/test_runai_model_streamer_loader.py`_
- **2026-07-31** [`68d442945f`](https://github.com/sgl-project/sglang/commit/68d442945f) [#32225](https://github.com/sgl-project/sglang/pull/32225)
  Flush dropped reasoning at stream end when stream_reasoning=False (#32225)
  _Files: `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/parser/test_reasoning_parser.py`_
- **2026-07-30** [`3312645a30`](https://github.com/sgl-project/sglang/commit/3312645a30) [#32877](https://github.com/sgl-project/sglang/pull/32877)
  wire the rust server modules into lib, runtime, and tokenizer manager (#32877)
  _Files: `rust/sglang-server/src/environ.rs`, `rust/sglang-server/src/error.rs`, `rust/sglang-server/src/lib.rs`, `rust/sglang-server/src/message.rs` _+2 more__
- **2026-07-30** [`047635ee35`](https://github.com/sgl-project/sglang/commit/047635ee35) [#32876](https://github.com/sgl-project/sglang/pull/32876)
  add the rust server native api handlers and runtime threads (#32876)
  _Files: `rust/sglang-server/src/api_server/native_api.rs`, `rust/sglang-server/src/runtime/threads.rs`_
- **2026-07-30** [`4facc0e18a`](https://github.com/sgl-project/sglang/commit/4facc0e18a) [#32874](https://github.com/sgl-project/sglang/pull/32874)
  add the rust server ingress tests, guard, and submit modules (#32874)
  _Files: `rust/sglang-server/src/api_server/guard.rs`, `rust/sglang-server/src/api_server/submit.rs`, `rust/sglang-server/src/tokenizer_manager/ingress.rs`_
- **2026-07-30** [`922d6e5542`](https://github.com/sgl-project/sglang/commit/922d6e5542) [#32872](https://github.com/sgl-project/sglang/pull/32872)
  add the rust server tokenizer, detokenizer, and egress modules (#32872)
  _Files: `rust/sglang-server/src/detokenizer.rs`, `rust/sglang-server/src/tokenizer.rs`, `rust/sglang-server/src/tokenizer_manager/egress.rs`_
- **2026-07-30** [`35f2e6ab58`](https://github.com/sgl-project/sglang/commit/35f2e6ab58) [#32871](https://github.com/sgl-project/sglang/pull/32871)
  update Cargo.lock for the rust sglang-server dependencies (#32871)
  _Files: `rust/sglang-server/Cargo.lock`_
- **2026-07-30** [`4f51dad1da`](https://github.com/sgl-project/sglang/commit/4f51dad1da) [#31339](https://github.com/sgl-project/sglang/pull/31339)
  fix: prevent ReqTimeStats from being dropped during IPC serialization (#31339)
  _Files: `python/sglang/srt/observability/req_time_stats.py`_
- **2026-07-30** [`36afd442c7`](https://github.com/sgl-project/sglang/commit/36afd442c7) [#21094](https://github.com/sgl-project/sglang/pull/21094)
  [DLLM]  vectorized joint/low-confidence decoding and skip redundant attn init (#21094)
  _Files: `python/sglang/srt/dllm/algorithm/base.py`, `python/sglang/srt/dllm/algorithm/joint_threshold.py`, `test/registered/ascend/basic_function/dllm/test_npu_llada2_mini.py`_
- **2026-07-30** [`d7a4c830e5`](https://github.com/sgl-project/sglang/commit/d7a4c830e5) [#32358](https://github.com/sgl-project/sglang/pull/32358)
  sglang rust server tokenizer manager, ring and runtime (#32358)
  _Files: `rust/sglang-server/src/fsm.rs`, `rust/sglang-server/src/lib.rs`, `rust/sglang-server/src/message.rs`, `rust/sglang-server/src/message/request.rs` _+5 more__
- **2026-07-30** [`6e48c13497`](https://github.com/sgl-project/sglang/commit/6e48c13497) [#32342](https://github.com/sgl-project/sglang/pull/32342)
  sglang rust server egress message (#32342)
  _Files: `rust/sglang-server/src/message.rs`, `rust/sglang-server/src/message/egress.rs`, `rust/sglang-server/src/message/finish_reason.rs`_
- **2026-07-29** [`d24de56995`](https://github.com/sgl-project/sglang/commit/d24de56995) [#32343](https://github.com/sgl-project/sglang/pull/32343)
  sglang rust server sampling message (#32343)
  _Files: `rust/sglang-server/src/message/sampling.rs`, `rust/sglang-server/src/utils/regex.rs`_
- **2026-07-29** [`ffd4705baa`](https://github.com/sgl-project/sglang/commit/ffd4705baa) [#32540](https://github.com/sgl-project/sglang/pull/32540)
  fix(reasoning): honor Poolside template thinking defaults (#32540)
  _Files: `python/sglang/srt/parser/template_detection.py`, `test/registered/unit/parser/test_template_manager.py`_
- **2026-07-29** [`2ca2ca753a`](https://github.com/sgl-project/sglang/commit/2ca2ca753a) [#32242](https://github.com/sgl-project/sglang/pull/32242)
  sglang rust server request message (#32242)
  _Files: `rust/sglang-server/src/ids.rs`, `rust/sglang-server/src/lib.rs`, `rust/sglang-server/src/message.rs`, `rust/sglang-server/src/message/io_struct.rs` _+3 more__
- **2026-07-29** [`3763d3fa8c`](https://github.com/sgl-project/sglang/commit/3763d3fa8c) [#32789](https://github.com/sgl-project/sglang/pull/32789)
  Add decode-lock skip to compute-mamba-ratio (#32789)
  _Files: `.claude/skills/compute-mamba-ratio/SKILL.md`_
- **2026-07-29** [`c151080d28`](https://github.com/sgl-project/sglang/commit/c151080d28) [#32763](https://github.com/sgl-project/sglang/pull/32763)
  Add compute-mamba-ratio skill (#32763)
  _Files: `.claude/skills/compute-mamba-ratio/SKILL.md`_
- **2026-07-29** [`b21cc8eb9b`](https://github.com/sgl-project/sglang/commit/b21cc8eb9b) [#32717](https://github.com/sgl-project/sglang/pull/32717)
  [misc] Update CodeOwner (#32717)
  _Files: `.github/CODEOWNERS`_
- **2026-07-28** [`16a52bff23`](https://github.com/sgl-project/sglang/commit/16a52bff23) [#32694](https://github.com/sgl-project/sglang/pull/32694)
  [Refactor] Move sampling tokenizer validation helper (#32694)
  _Files: `python/sglang/srt/sampling/sampling_params.py`_
- **2026-07-28** [`d943636a48`](https://github.com/sgl-project/sglang/commit/d943636a48) [#32676](https://github.com/sgl-project/sglang/pull/32676)
  support regex that compatible with python re lib however apply more l… (#32676)
  _Files: `rust/sglang-server/Cargo.toml`, `rust/sglang-server/src/lib.rs`, `rust/sglang-server/src/utils.rs`, `rust/sglang-server/src/utils/regex.rs`_
- **2026-07-28** [`b8b9f3c8f5`](https://github.com/sgl-project/sglang/commit/b8b9f3c8f5) [#32679](https://github.com/sgl-project/sglang/pull/32679)
  [misc] update CI_PERMISSIONS.json (#32679)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-07-28** [`ec4a7fa2b7`](https://github.com/sgl-project/sglang/commit/ec4a7fa2b7) [#32608](https://github.com/sgl-project/sglang/pull/32608)
  codeowners update (#32608)
  _Files: `.github/CODEOWNERS`_
- **2026-07-27** [`34454c06b8`](https://github.com/sgl-project/sglang/commit/34454c06b8) [#32496](https://github.com/sgl-project/sglang/pull/32496)
  [Refactor] Tidy server_args.py section grouping and drop unused alias (#32496)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-27** [`2abb1d2c37`](https://github.com/sgl-project/sglang/commit/2abb1d2c37) [#31992](https://github.com/sgl-project/sglang/pull/31992)
  fix(hisparse): correct DSA KV memory budget (#31992)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_hisparse_pool_configurator.py`_

## MoE / Expert Parallel  (33 commits)

- **2026-08-03** [`5fe97637df`](https://github.com/sgl-project/sglang/commit/5fe97637df) [#33128](https://github.com/sgl-project/sglang/pull/33128)
  Support DeepGEMM for standard MoE dispatch (#33128)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/srt/layers/quantization/fp8.py`, `test/registered/kernels/ops/moe/test_minimax_quant_scatter.py` _+1 more__
- **2026-08-02** [`8cc941a672`](https://github.com/sgl-project/sglang/commit/8cc941a672) [#33150](https://github.com/sgl-project/sglang/pull/33150)
  [BCG][4/N] Enable bcg on megamoe & flashinfer a2a backend (#33150)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-08-02** [`37be4e9247`](https://github.com/sgl-project/sglang/commit/37be4e9247) [#32315](https://github.com/sgl-project/sglang/pull/32315)
  [AMD] Speed up DSV4 MoE weight loading from mmap views (#32315)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `python/sglang/srt/environ.py` _+2 more__
- **2026-08-02** [`7e509f690e`](https://github.com/sgl-project/sglang/commit/7e509f690e) [#31450](https://github.com/sgl-project/sglang/pull/31450)
  [AMD] Fix DeepSeek-V4 FP4 MoE expert memory bloat (#31450)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`_
- **2026-08-01** [`e2cf21b9e5`](https://github.com/sgl-project/sglang/commit/e2cf21b9e5) [#33025](https://github.com/sgl-project/sglang/pull/33025)
  [Kimi K3] Add reasoning, tool-call, and OpenAI serving support (#33025)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/constrained/base_grammar_backend.py`, `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/constrained/reasoner_grammar_backend.py` _+30 more__
- **2026-08-01** [`fb207b72b0`](https://github.com/sgl-project/sglang/commit/fb207b72b0) [#32890](https://github.com/sgl-project/sglang/pull/32890)
  feat(kernels): port standalone Kimi K3 kernels (#32890)
  _Files: `python/sglang/kernels/jit/csrc/attention/fixup_zero_kv.cuh`, `python/sglang/kernels/jit/csrc/attention/kda_fused_decode.cuh`, `python/sglang/kernels/jit/csrc/attention/kda_packed_decode.cuh`, `python/sglang/kernels/jit/csrc/attention/kda_prefill.cu` _+80 more__
- **2026-08-01** [`0d186f49be`](https://github.com/sgl-project/sglang/commit/0d186f49be) [#33090](https://github.com/sgl-project/sglang/pull/33090)
  [AMD][Fix] Restore aiter-padded MoE weight dims for serialized checkpoints (#33090)
  _Files: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`_
- **2026-07-31** [`3e0f7c3f30`](https://github.com/sgl-project/sglang/commit/3e0f7c3f30) [#31987](https://github.com/sgl-project/sglang/pull/31987)
  [BCG][3/N] Enable bcg on dsa & deepep a2a backend (#31987)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py` _+9 more__
- **2026-07-31** [`937c77cf50`](https://github.com/sgl-project/sglang/commit/937c77cf50) [#33016](https://github.com/sgl-project/sglang/pull/33016)
  [Fix] Clear stale FlashInfer BF16 MoE index cache (#33016)
  _Files: `python/sglang/srt/layers/quantization/unquant.py`_
- **2026-07-31** [`06ccaef24a`](https://github.com/sgl-project/sglang/commit/06ccaef24a) [#32962](https://github.com/sgl-project/sglang/pull/32962)
  Fix silently wrong EPLB output with --moe-a2a-backend none (rank-invariant dispatch) (#32962)
  _Files: `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/eplb/expert_location_dispatch.py`, `python/sglang/srt/server_args.py`, `test/registered/ep/test_eplb_no_a2a.py` _+1 more__
- **2026-07-31** [`48dbc24cbf`](https://github.com/sgl-project/sglang/commit/48dbc24cbf) [#31382](https://github.com/sgl-project/sglang/pull/31382)
  [Qwen3.5][MTP] Support FlashInfer CuTe DSL for online NVFP4 draft MoE (#31382)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/layers/quantization/nvfp4_online.py` _+1 more__
- **2026-07-30** [`a1c30701aa`](https://github.com/sgl-project/sglang/commit/a1c30701aa) [#30756](https://github.com/sgl-project/sglang/pull/30756)
  Integrate pplx a2a backend (#30756)
  _Files: `docs_new/docs/advanced_features/expert_parallelism.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/overrides.py` _+12 more__
- **2026-07-30** [`3a53c26c27`](https://github.com/sgl-project/sglang/commit/3a53c26c27) [#32937](https://github.com/sgl-project/sglang/pull/32937)
  [CI] Fix MoE compile and DSA indexer regressions (#32937)
  _Files: `python/sglang/srt/layers/moe/fused_moe_native.py`, `test/registered/kernels/ops/attention/test_dsa_indexer.py`_
- **2026-07-30** [`a6221d776f`](https://github.com/sgl-project/sglang/commit/a6221d776f) [#31989](https://github.com/sgl-project/sglang/pull/31989)
  feat: Support nvidia/MiniMax-M3-NVFP4 (#31989)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/models/minimax_m3.py` _+2 more__
- **2026-07-30** [`c4af6cf263`](https://github.com/sgl-project/sglang/commit/c4af6cf263) [#31220](https://github.com/sgl-project/sglang/pull/31220)
  Qwen3.5-MoE: support modelopt_fp4 checkpoints that quantize attention (+ load baked FP8 KV scales) (#31220)
  _Files: `python/sglang/srt/models/qwen3_5.py`, `test/registered/unit/models/test_qwen3_5_modelopt_fp4.py`_
- **2026-07-30** [`fc007e1f00`](https://github.com/sgl-project/sglang/commit/fc007e1f00) [#29016](https://github.com/sgl-project/sglang/pull/29016)
  Add SM90 FP8 MegaMoE support for DeepSeek-V4 (#29016)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/mega_moe_sm90.py`, `python/sglang/srt/layers/quantization/fp8.py` _+1 more__
- **2026-07-30** [`92b3a51ba6`](https://github.com/sgl-project/sglang/commit/92b3a51ba6) [#32884](https://github.com/sgl-project/sglang/pull/32884)
  [LoRA] Fix Marlin MoE kernel import (#32884)
  _Files: `python/sglang/srt/lora/marlin_lora_temp/moe_runner.py`_
- **2026-07-30** [`e4a40a71f8`](https://github.com/sgl-project/sglang/commit/e4a40a71f8) [#31888](https://github.com/sgl-project/sglang/pull/31888)
  [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.2 & DeepSeek-V3.2: Q8-Path & Shared-Path Optimizations (#31888)
  _Files: `benchmark/kernels/deepseek/benchmark_q8kv8_kv_gather.py`, `benchmark/kernels/deepseek/benchmark_q8kv8_q_prep.py`, `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `python/sglang/kernels/jit/csrc/qprep_bf16_fp8_sm90/entry.cuh` _+26 more__
- **2026-07-29** [`e5c46ff07d`](https://github.com/sgl-project/sglang/commit/e5c46ff07d) [#32818](https://github.com/sgl-project/sglang/pull/32818)
  [Fix] Route asymmetric-KV models to fa4 on SM100 and pin MiMoV2 FP8 MoE to flashinfer_trtllm (#32818)
  _Files: `docs_new/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx`, `docs_new/src/snippets/autoregressive/mimo-v25-deployment.jsx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/model_config.py` _+2 more__
- **2026-07-29** [`8fc54d46ef`](https://github.com/sgl-project/sglang/commit/8fc54d46ef) [#32663](https://github.com/sgl-project/sglang/pull/32663)
  Fix MoE reduce-scatterv eligibility check (#32663)
  _Files: `python/sglang/srt/layers/moe/utils.py`, `test/registered/unit/test_runtime_context.py`_
- **2026-07-29** [`e4f7f7b380`](https://github.com/sgl-project/sglang/commit/e4f7f7b380) [#32022](https://github.com/sgl-project/sglang/pull/32022)
  fix(qwen3.5): restrict MoE weights to local PP layers (#32022)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-07-29** [`62d0f81f16`](https://github.com/sgl-project/sglang/commit/62d0f81f16) [#30553](https://github.com/sgl-project/sglang/pull/30553)
  [2/N] elastic-ep: Enable EPLB after scale-up (#30553)
  _Files: `python/sglang/srt/eplb/eplb_manager.py`, `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/eplb/expert_location_updater.py`, `python/sglang/srt/managers/scheduler.py` _+2 more__
- **2026-07-29** [`d19999b755`](https://github.com/sgl-project/sglang/commit/d19999b755) [#30780](https://github.com/sgl-project/sglang/pull/30780)
  [LFM2] Wire Lfm2MoeForCausalLM into the LFM2 serving override tables (#30780)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/server_args.py`_
- **2026-07-29** [`f05c92fb6d`](https://github.com/sgl-project/sglang/commit/f05c92fb6d) [#30768](https://github.com/sgl-project/sglang/pull/30768)
  :sparkles: [llm][npu][quant] Add W8A8 MXFP8 quantization for Qwen3 MoE on Ascend NPU (#30768)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quantization.mdx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/hardware_backend/npu/moe/init_routing.py` _+14 more__
- **2026-07-29** [`f01a0c7f97`](https://github.com/sgl-project/sglang/commit/f01a0c7f97) [#31510](https://github.com/sgl-project/sglang/pull/31510)
  Fixing MXFP8 online quantization pipeline (#31510)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/mxfp4.py` _+3 more__
- **2026-07-29** [`580b1acbe6`](https://github.com/sgl-project/sglang/commit/580b1acbe6) [#32448](https://github.com/sgl-project/sglang/pull/32448)
  [MLX] Move fused swiglu tests to test/registered so CI collects them (#32448)
  _Files: `python/sglang/srt/hardware_backend/mlx/moe/tests/__init__.py`, `test/registered/unit/hardware_backend/mlx/test_fused_swiglu.py`_
- **2026-07-28** [`ee236086db`](https://github.com/sgl-project/sglang/commit/ee236086db) [#28370](https://github.com/sgl-project/sglang/pull/28370)
  Fix invalid escape warnings in tool parsers (#28370)
  _Files: `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/function_call/lfm2_detector.py`, `python/sglang/srt/function_call/llama32_detector.py` _+8 more__
- **2026-07-28** [`9cffc2ba52`](https://github.com/sgl-project/sglang/commit/9cffc2ba52) [#32636](https://github.com/sgl-project/sglang/pull/32636)
  [Kernel] Remove unused implementations and stale registry entries (#32636)
  _Files: `python/sglang/kernels/jit/csrc/dsa/kpool_topk_transform.cuh`, `python/sglang/kernels/jit/csrc/elementwise/resolve_future_token_ids.cuh`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dsv4/compress_c128_hip.py` _+23 more__
- **2026-07-27** [`3005af0941`](https://github.com/sgl-project/sglang/commit/3005af0941) [#32430](https://github.com/sgl-project/sglang/pull/32430)
  Fix compressed-tensors NVFP4 MoE W13 layout (#32430)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4_moe.py`_
- **2026-07-27** [`8d6549bc40`](https://github.com/sgl-project/sglang/commit/8d6549bc40) [#32304](https://github.com/sgl-project/sglang/pull/32304)
  [Attention Backend] Extend hpc_ops dynamic-scheduled decode to bf16 (#32304)
  _Files: `docker/Dockerfile`, `docs_new/docs/advanced_features/attention_backend.mdx`, `python/sglang/srt/layers/attention/hpc_ops_backend.py`, `python/sglang/srt/layers/moe/moe_runner/hpc_ops.py` _+3 more__
- **2026-07-27** [`169fc1e20c`](https://github.com/sgl-project/sglang/commit/169fc1e20c) [#31280](https://github.com/sgl-project/sglang/pull/31280)
  [NPU] Acc fix for afmoe model introduced by topk refactor. (#31280)
  _Files: `python/sglang/srt/models/afmoe.py`_
- **2026-07-27** [`c0f47a06fc`](https://github.com/sgl-project/sglang/commit/c0f47a06fc) [#31393](https://github.com/sgl-project/sglang/pull/31393)
  [NPU] Determine the topk norm_type through scoring_func (#31393)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/models/glm4_moe_lite.py`_
- **2026-07-27** [`a358374ae9`](https://github.com/sgl-project/sglang/commit/a358374ae9) [#32001](https://github.com/sgl-project/sglang/pull/32001)
  [NPU][Fix Issue]: Send expert weights contiguous tensor across cards during EPLB rebalance (#32001)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py`_

## Multimodal  (32 commits)

- **2026-08-03** [`c2dbdfd218`](https://github.com/sgl-project/sglang/commit/c2dbdfd218) [#33345](https://github.com/sgl-project/sglang/pull/33345)
  [Docs] Fix overlapping quality-profile table headers on MiniMax-H3 page (#33345)
  _Files: `docs_new/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`_
- **2026-08-03** [`dd6ddc053b`](https://github.com/sgl-project/sglang/commit/dd6ddc053b) [#33308](https://github.com/sgl-project/sglang/pull/33308)
  [Fix] Drop deprecated multimodal processor residency state (#33308)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py` _+4 more__
- **2026-08-03** [`4bc593fdc8`](https://github.com/sgl-project/sglang/commit/4bc593fdc8) [#33307](https://github.com/sgl-project/sglang/pull/33307)
  [Perf] Broadcast single-image DP vision embedding instead of pad-to-max all-gather (#33307)
  _Files: `python/sglang/srt/multimodal/mm_utils.py`, `test/manual/vlm/verify_single_image_gather.py`, `test/registered/unit/models/test_kimi_k25.py`_
- **2026-08-02** [`70fe2e0dd5`](https://github.com/sgl-project/sglang/commit/70fe2e0dd5) [#33275](https://github.com/sgl-project/sglang/pull/33275)
  [diffusion] model: support minimax-h3 (#33275)
- **2026-08-02** [`558c9bdcc2`](https://github.com/sgl-project/sglang/commit/558c9bdcc2) [#33255](https://github.com/sgl-project/sglang/pull/33255)
  [misc] Improve benchmark determinism and dataset API coverage (#33255)
  _Files: `benchmark/gsm8k/bench_sglang.py`, `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/image.py`, `python/sglang/benchmark/one_batch_server.py` _+2 more__
- **2026-07-31** [`585a7d05e3`](https://github.com/sgl-project/sglang/commit/585a7d05e3) [#32683](https://github.com/sgl-project/sglang/pull/32683)
  [Diffusion] Return scheduler sigmas snapshot in rollout dit_trajectory (#32683)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/post_training/rollout_api.py`, `python/sglang/multimodal_gen/runtime/post_training/rl_dataclasses.py`, `python/sglang/multimodal_gen/runtime/post_training/rollout_denoising_mixin.py`, `python/sglang/multimodal_gen/test/unit/test_rollout_api.py`_
- **2026-07-31** [`a149717308`](https://github.com/sgl-project/sglang/commit/a149717308) [#30903](https://github.com/sgl-project/sglang/pull/30903)
  feat: log multimodal encoder DP tradeoffs (#30903)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-07-30** [`c5bd3d7dce`](https://github.com/sgl-project/sglang/commit/c5bd3d7dce) [#32917](https://github.com/sgl-project/sglang/pull/32917)
  [diffusion][benchmark] Add reproducible request-manifest offline benchmark (#32917)
  _Files: `python/sglang/multimodal_gen/benchmarks/bench_offline_throughput.py`, `python/sglang/multimodal_gen/benchmarks/request_manifest.py`, `python/sglang/multimodal_gen/test/unit/test_request_manifest.py`_
- **2026-07-30** [`7784ac8f91`](https://github.com/sgl-project/sglang/commit/7784ac8f91) [#32916](https://github.com/sgl-project/sglang/pull/32916)
  [diffusion][docs] Fix Cosmos3 model sizes (#32916)
  _Files: `docs_new/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `docs_new/docs/sglang-diffusion/compatibility_matrix.mdx`, `python/sglang/multimodal_gen/registry.py`_
- **2026-07-30** [`b129e8a299`](https://github.com/sgl-project/sglang/commit/b129e8a299) [#32932](https://github.com/sgl-project/sglang/pull/32932)
  [diffusion] docs: surface diffusion AR and PE guides (#32932)
  _Files: `docs_new/docs.json`, `docs_new/docs/sglang-diffusion/api/cli.mdx`, `docs_new/docs/sglang-diffusion/index.mdx`, `docs_new/docs/sglang-diffusion/models_with_ar.mdx` _+1 more__
- **2026-07-30** [`db3da62333`](https://github.com/sgl-project/sglang/commit/db3da62333) [#30211](https://github.com/sgl-project/sglang/pull/30211)
  [diffusion] feat: unify encoder folding and batch data-parallel encoding (#30211)
  _Files: `docs_new/docs.json`, `docs_new/docs/sglang-diffusion/api/cli.mdx`, `docs_new/docs/sglang-diffusion/encoder_parallel.mdx`, `docs_new/docs/sglang-diffusion/index.mdx` _+10 more__
- **2026-07-30** [`4b52758c76`](https://github.com/sgl-project/sglang/commit/4b52758c76) [#31924](https://github.com/sgl-project/sglang/pull/31924)
  [AMD] Skip test_update_weights_from_disk on ROCm pending reload fix (#31924) (#31925)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`_
- **2026-07-30** [`22faf9fef8`](https://github.com/sgl-project/sglang/commit/22faf9fef8) [#32481](https://github.com/sgl-project/sglang/pull/32481)
  embedding: centralize capabilities and complete OpenAI compatibility (#32481)
  _Files: `docs_new/docs/basic_usage/native_api.mdx`, `docs_new/docs/basic_usage/openai_api_embeddings.mdx`, `docs_new/docs/developer_guide/bench_serving.mdx`, `docs_new/docs/supported-models/embedding_models.mdx` _+12 more__
- **2026-07-30** [`2aa86e9130`](https://github.com/sgl-project/sglang/commit/2aa86e9130) [#32836](https://github.com/sgl-project/sglang/pull/32836)
  [diffusion] docs: add diffusion cookbook model tags (#32836)
  _Files: `docs_new/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `docs_new/cookbook/diffusion/Ernie-Image/Ernie-Image.mdx`, `docs_new/cookbook/diffusion/FLUX/FLUX.mdx`, `docs_new/cookbook/diffusion/Ideogram/Ideogram4.mdx` _+16 more__
- **2026-07-29** [`22151edca1`](https://github.com/sgl-project/sglang/commit/22151edca1) [#32784](https://github.com/sgl-project/sglang/pull/32784)
  [diffusion] optimization: accelerate CUDA video output finalization (#32784)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/test/unit/test_output_saving.py`_
- **2026-07-29** [`4f5b50c576`](https://github.com/sgl-project/sglang/commit/4f5b50c576) [#32697](https://github.com/sgl-project/sglang/pull/32697)
  perf(diffusion): decode Wan VAE in BF16 (#32697)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/longlive2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py`, `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py` _+6 more__
- **2026-07-29** [`917e900d4d`](https://github.com/sgl-project/sglang/commit/917e900d4d) [#32696](https://github.com/sgl-project/sglang/pull/32696)
  feat(diffusion): add regional torch compile (#32696)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/runtime/utils/torch_compile.py`, `python/sglang/multimodal_gen/test/unit/test_regional_torch_compile.py`_
- **2026-07-29** [`67c2258906`](https://github.com/sgl-project/sglang/commit/67c2258906) [#32743](https://github.com/sgl-project/sglang/pull/32743)
  [diffusion] fix: fix dual-DiT models crash with (1,)-placeholder weights after compile-time offload (#32743)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-07-29** [`227dadd79a`](https://github.com/sgl-project/sglang/commit/227dadd79a) [#31538](https://github.com/sgl-project/sglang/pull/31538)
  [diffusion] feat: support resident layers for DiT (#31538)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-07-29** [`0caf0fc01d`](https://github.com/sgl-project/sglang/commit/0caf0fc01d) [#30614](https://github.com/sgl-project/sglang/pull/30614)
  [Diffusion][Docs] Ascend A2, A3 add basic usage and benchmark results in diffusion cookbook (#30614)
  _Files: `docs_new/cookbook/diffusion/FLUX/FLUX.mdx`, `docs_new/cookbook/diffusion/Qwen-Image/Qwen-Image.mdx`, `docs_new/cookbook/diffusion/Wan/Wan2.1.mdx`, `docs_new/cookbook/diffusion/Wan/Wan2.2.mdx` _+6 more__
- **2026-07-29** [`da5528db30`](https://github.com/sgl-project/sglang/commit/da5528db30) [#31596](https://github.com/sgl-project/sglang/pull/31596)
  fix(vlm): materialize Qwen3-VL features on the vision device (#31596)
  _Files: `python/sglang/srt/models/qwen3_vl.py`, `test/registered/unit/models/test_qwen3_vl_feature_materialization.py`_
- **2026-07-29** [`7c248dde7f`](https://github.com/sgl-project/sglang/commit/7c248dde7f) [#31361](https://github.com/sgl-project/sglang/pull/31361)
  [diffusion] fix: don't self-kill diffusion worker when PID 1 is the real parent (#31361)
  _Files: `python/sglang/multimodal_gen/test/unit/test_utils_parent_death.py`, `python/sglang/multimodal_gen/utils.py`_
- **2026-07-29** [`9a03bebf13`](https://github.com/sgl-project/sglang/commit/9a03bebf13) [#32661](https://github.com/sgl-project/sglang/pull/32661)
  docs(kimi-k3): clarify VLM compatibility (#32661)
  _Files: `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`_
- **2026-07-28** [`70ea37e7e0`](https://github.com/sgl-project/sglang/commit/70ea37e7e0) [#31957](https://github.com/sgl-project/sglang/pull/31957)
  vlm: reject moss vision metadata mismatches (#31957)
  _Files: `python/sglang/srt/multimodal/processors/moss_vl.py`, `test/registered/unit/models/test_moss_vl_processor.py`_
- **2026-07-28** [`c9947b087b`](https://github.com/sgl-project/sglang/commit/c9947b087b) [#30872](https://github.com/sgl-project/sglang/pull/30872)
  Enable multimodal prefill BCG for VL and audio models (#30872)
  _Files: `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/unit/model_executor/test_prefill_cuda_graph_runner_helpers.py`_
- **2026-07-28** [`84cdfde5b2`](https://github.com/sgl-project/sglang/commit/84cdfde5b2) [#30017](https://github.com/sgl-project/sglang/pull/30017)
  [diffusion] fix: fix diffusion output stability on mps (#30017)
  _Files: `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/layers/linear.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py`, `python/sglang/multimodal_gen/runtime/models/dits/sana.py` _+15 more__
- **2026-07-28** [`161fffedfc`](https://github.com/sgl-project/sglang/commit/161fffedfc) [#32639](https://github.com/sgl-project/sglang/pull/32639)
  docs: clarify diffusion stage reuse guidance (#32639)
  _Files: `docs_new/docs/sglang-diffusion/support_new_models.mdx`_
- **2026-07-28** [`75017c3fa0`](https://github.com/sgl-project/sglang/commit/75017c3fa0) [#31849](https://github.com/sgl-project/sglang/pull/31849)
  [diffusion] fix: keep fused qk-norm-rope out of dynamo tracing (#31849)
  _Files: `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`_
- **2026-07-28** [`4fe8f5218d`](https://github.com/sgl-project/sglang/commit/4fe8f5218d) [#32643](https://github.com/sgl-project/sglang/pull/32643)
  [AMD] Add Kimi K3 ROCm 7.2 nightly image (#32643)
  _Files: `.github/workflows/release-docker-amd-rocm720-nightly.yml`_
- **2026-07-28** [`356c11d5d9`](https://github.com/sgl-project/sglang/commit/356c11d5d9) [#30260](https://github.com/sgl-project/sglang/pull/30260)
  [Fix] --mm-process-config crash when video config contains (#30260)
  _Files: `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`, `test/registered/unit/managers/test_mm_process_config.py`_
- **2026-07-27** [`8a311d1c88`](https://github.com/sgl-project/sglang/commit/8a311d1c88) [#32420](https://github.com/sgl-project/sglang/pull/32420)
  [diffusion] fix: preserve tensor stride when offloading rollout weights to pinned host memory (#32420)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/memory_occupation_controller.py`_
- **2026-07-27** [`7cae831e41`](https://github.com/sgl-project/sglang/commit/7cae831e41) [#32559](https://github.com/sgl-project/sglang/pull/32559)
  Update mi35x ROCm image to k3-20260727 (#32559)
  _Files: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `docs_new/src/snippets/configs/moonshotai/kimi-k3.jsx`_

## Prefill / Decode Disaggregation  (26 commits)

- **2026-08-03** [`a2d1003b18`](https://github.com/sgl-project/sglang/commit/a2d1003b18) [#32403](https://github.com/sgl-project/sglang/pull/32403)
  [Mooncake] Fix ProcessGroup API imports (#32403)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/elastic_ep/elastic_ep.py`_
- **2026-08-03** [`5d2dbb35a6`](https://github.com/sgl-project/sglang/commit/5d2dbb35a6) [#33125](https://github.com/sgl-project/sglang/pull/33125)
  [rust-server] PD disaggregation support (#33125)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/disagg_service.py`, `python/sglang/srt/managers/scheduler.py` _+11 more__
- **2026-08-02** [`f8e62a9224`](https://github.com/sgl-project/sglang/commit/f8e62a9224) [#32392](https://github.com/sgl-project/sglang/pull/32392)
  [NPU] Add PR test cases (#32392)
  _Files: `.github/workflows/pr-test-npu.yml`, `python/sglang/test/ascend/npu_eval_accuracy_kit.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/npu/accuracy/glm4_7_flash/test_npu_glm4_7_flash_1p_gsm8k.py` _+20 more__
- **2026-08-02** [`056474cdb0`](https://github.com/sgl-project/sglang/commit/056474cdb0) [#29173](https://github.com/sgl-project/sglang/pull/29173)
  feat: Session-reference-aware Unified Radix Cache for agentic multi-turn workloads (#29173)
  _Files: `docs_new/docs.json`, `docs_new/docs/advanced_features/overview.mdx`, `docs_new/docs/advanced_features/session_radix_cache.mdx`, `python/sglang/srt/disaggregation/prefill.py` _+19 more__
- **2026-08-01** [`9b44695713`](https://github.com/sgl-project/sglang/commit/9b44695713) [#33171](https://github.com/sgl-project/sglang/pull/33171)
  test: recover the config-namespace-migration deferrals (#33171)
  _Files: `test/registered/rl/test_fp32_lm_head.py`, `test/registered/unit/batch_overlap/test_tbo_cuda_graph_num_token_device.py`, `test/registered/unit/batch_overlap/test_tbo_filter_batch_marker.py`, `test/registered/unit/constrained/test_grammar_manager.py` _+12 more__
- **2026-08-01** [`47d8b5b749`](https://github.com/sgl-project/sglang/commit/47d8b5b749) [#33170](https://github.com/sgl-project/sglang/pull/33170)
  config: route parallel config-leaf reads through get_parallel() (#33170)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py` _+77 more__
- **2026-07-31** [`4862edc85f`](https://github.com/sgl-project/sglang/commit/4862edc85f) [#33012](https://github.com/sgl-project/sglang/pull/33012)
  runtime_context: record the publishing process role (#33012)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/elastic_ep/expert_backup_manager.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/scheduler.py` _+8 more__
- **2026-07-31** [`fd28242b68`](https://github.com/sgl-project/sglang/commit/fd28242b68) [#33044](https://github.com/sgl-project/sglang/pull/33044)
  [CI] Pin NCCL ports for GB300 PR tests (#33044)
  _Files: `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`, `test/registered/disaggregation/test_disaggregation_aarch64.py`, `test/registered/ep/test_flashinfer_a2a.py`_
- **2026-07-31** [`2573190b93`](https://github.com/sgl-project/sglang/commit/2573190b93) [#32837](https://github.com/sgl-project/sglang/pull/32837)
  feat: support Kimi Linear PD disaggregation with DCP (#32837)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/utils.py` _+9 more__
- **2026-07-31** [`f3fd869494`](https://github.com/sgl-project/sglang/commit/f3fd869494) [#32692](https://github.com/sgl-project/sglang/pull/32692)
  [gdn] support replayssm with extra buffer (#32692)
  _Files: `python/sglang/kernels/ops/attention/fla/bench_gdn_replayssm_fold.py`, `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/kernels/ops/attention/fla/gdn_replayssm_spec_fold.py`, `python/sglang/srt/configs/mamba_utils.py` _+10 more__
- **2026-07-31** [`c039e1a7ee`](https://github.com/sgl-project/sglang/commit/c039e1a7ee) [#32857](https://github.com/sgl-project/sglang/pull/32857)
  [NPU][DOC] Restructure ascend-npus docs into layered navigation (#32857)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`, `docs_new/docs.json`, `docs_new/docs/advanced_features/quantization.mdx`, `docs_new/docs/get-started/install.mdx` _+52 more__
- **2026-07-30** [`4ba7d5ad93`](https://github.com/sgl-project/sglang/commit/4ba7d5ad93) [#31591](https://github.com/sgl-project/sglang/pull/31591)
  [BugFix][EPD] Early-release mooncake GPU embeddings; fix gpu_id via scheduler.ps (#31591)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`_
- **2026-07-30** [`f6ff5e8bb0`](https://github.com/sgl-project/sglang/commit/f6ff5e8bb0) [#32797](https://github.com/sgl-project/sglang/pull/32797)
  [PD] Handle abort requests in PP mode (#32797)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`_
- **2026-07-29** [`eefb434d17`](https://github.com/sgl-project/sglang/commit/eefb434d17) [#31869](https://github.com/sgl-project/sglang/pull/31869)
  [PD+PP] Honor PP consensus for bootstrap and prealloc (#31869)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` _+3 more__
- **2026-07-29** [`977f04aafe`](https://github.com/sgl-project/sglang/commit/977f04aafe) [#32025](https://github.com/sgl-project/sglang/pull/32025)
  [PD] NIXL connector: shard by destination (#32025)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-07-29** [`4c82bb3252`](https://github.com/sgl-project/sglang/commit/4c82bb3252) [#30256](https://github.com/sgl-project/sglang/pull/30256)
  Add Mooncake tenant id support (#30256)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/README.md`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_embedding_store.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py` _+1 more__
- **2026-07-29** [`983e4aa18d`](https://github.com/sgl-project/sglang/commit/983e4aa18d) [#32620](https://github.com/sgl-project/sglang/pull/32620)
  Eliminate redundant DSA state transfers (Mooncake) (#32620)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`_
- **2026-07-29** [`9bdbb180b1`](https://github.com/sgl-project/sglang/commit/9bdbb180b1) [#31968](https://github.com/sgl-project/sglang/pull/31968)
  [Disagg][NIXL] Fix heterogeneous attn-TP KV transfer for replicated GQA heads (NIXL_ERR_NOT_FOUND) (#31968)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-07-29** [`bf6e80718a`](https://github.com/sgl-project/sglang/commit/bf6e80718a) [#31706](https://github.com/sgl-project/sglang/pull/31706)
  [Elastic EP] fix previously flaky test of test_mooncake_ep_small.py (#31706)
  _Files: `test/registered/ep/test_mooncake_ep_small.py`_
- **2026-07-29** [`1af0167493`](https://github.com/sgl-project/sglang/commit/1af0167493) [#32104](https://github.com/sgl-project/sglang/pull/32104)
  [EPD][VLM] Fix Kimi-VL 2D encoder grids (#32104)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `test/registered/disaggregation/test_epd_disaggregation.py`, `test/registered/unit/disaggregation/test_encode_server.py`_
- **2026-07-28** [`9ca4023b13`](https://github.com/sgl-project/sglang/commit/9ca4023b13) [#32688](https://github.com/sgl-project/sglang/pull/32688)
  [Core] Clean up array-like msgspec structs (#32688)
  _Files: `experimental/sgl-router/src/policies/kv_events/wire.rs`, `python/sglang/srt/disaggregation/kv_events.py`, `python/sglang/srt/sampling/sampling_params.py`, `test/registered/unit/sampling/test_sampling_params.py`_
- **2026-07-28** [`1eee8fbdcc`](https://github.com/sgl-project/sglang/commit/1eee8fbdcc) [#32267](https://github.com/sgl-project/sglang/pull/32267)
  [PD] Drain NIXL completion notifications before enforcing the WaitingForInput timeout (#32267)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-07-28** [`32c30c0f96`](https://github.com/sgl-project/sglang/commit/32c30c0f96) [#31417](https://github.com/sgl-project/sglang/pull/31417)
  Return 400 instead of 500 for unfetchable or unparseable multimodal inputs (#31417)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/utils/common.py`, `test/registered/unit/multimodal/test_base_processor_bad_input.py`_
- **2026-07-28** [`5558dbad00`](https://github.com/sgl-project/sglang/commit/5558dbad00) [#31931](https://github.com/sgl-project/sglang/pull/31931)
  [NPU] Optimize DeepSeek-V4 performance (#31931)
  _Files: `python/sglang/kernels/ops/attention/deepseek_v4_rope.py`, `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+17 more__
- **2026-07-27** [`5656de2d9a`](https://github.com/sgl-project/sglang/commit/5656de2d9a) [#31543](https://github.com/sgl-project/sglang/pull/31543)
  [PD] pool decode bootstrap HTTP sessions (#31543)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`_
- **2026-07-27** [`3d3ba4f746`](https://github.com/sgl-project/sglang/commit/3d3ba4f746) [#32071](https://github.com/sgl-project/sglang/pull/32071)
  [BugFix][EPD] Fix Mooncake source-MR lifecycle for multi-TP /send (#32071)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`_

## KV Cache / Memory  (19 commits)

- **2026-08-02** [`12eadf86f1`](https://github.com/sgl-project/sglang/commit/12eadf86f1) [#31741](https://github.com/sgl-project/sglang/pull/31741)
  [AMD] Enable mamba JIT transfer kernel on ROCm (fix transfer_kv_mamba NameError) (#31741)
  _Files: `python/sglang/kernels/jit/csrc/kvcacheio/transfer_mamba.cuh`, `python/sglang/srt/mem_cache/memory_pool_host.py`_
- **2026-08-02** [`88e5a0f635`](https://github.com/sgl-project/sglang/commit/88e5a0f635) [#33294](https://github.com/sgl-project/sglang/pull/33294)
  test: stand up the config tiers two unit tests read from (#33294)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `test/registered/chunked_prefill/test_mm_chunked_embedding_unit.py`, `test/registered/unit/hardware_backend/mlx/test_attn_dp_request_capacity.py`_
- **2026-08-02** [`43be25b2b7`](https://github.com/sgl-project/sglang/commit/43be25b2b7) [#32829](https://github.com/sgl-project/sglang/pull/32829)
  [CI] Graceful teardown for kv_canary and EAGLE spec fixtures (#32829)
  _Files: `python/sglang/test/chunked_prefill_test_utils.py`, `python/sglang/test/kv_canary/e2e_base.py`, `python/sglang/test/server_fixtures/default_fixture.py`, `python/sglang/test/server_fixtures/dsa_mtp_fixture.py` _+14 more__
- **2026-08-01** [`df55e911d6`](https://github.com/sgl-project/sglang/commit/df55e911d6) [#33168](https://github.com/sgl-project/sglang/pull/33168)
  Fix the chunked-prefix-cache gate writing config the backends never read (#33168)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/misc_utils.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/speculative/draft_worker_common.py` _+2 more__
- **2026-08-01** [`e6a4cefc69`](https://github.com/sgl-project/sglang/commit/e6a4cefc69) [#33126](https://github.com/sgl-project/sglang/pull/33126)
  perf(startup): skip unused PyTorch headers for KV VMM allocator stub (#33126)
  _Files: `python/sglang/srt/mem_cache/kv_vmm_backing.py`_
- **2026-07-31** [`26486a957d`](https://github.com/sgl-project/sglang/commit/26486a957d) [#32915](https://github.com/sgl-project/sglang/pull/32915)
  Fix --hicache-size allocating ~2x host memory on hybrid Mamba (#32915)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`_
- **2026-07-31** [`afeaeccfa2`](https://github.com/sgl-project/sglang/commit/afeaeccfa2) [#32483](https://github.com/sgl-project/sglang/pull/32483)
  perf(hisparse): eliminate redundant swap output fill (#32483)
  _Files: `python/sglang/kernels/jit/csrc/hisparse.cuh`, `python/sglang/srt/managers/hisparse_coordinator.py`, `test/registered/kernels/benchmark/kvcache/bench_hisparse.py`, `test/registered/kernels/ops/kvcache/test_hisparse.py`_
- **2026-07-29** [`3c1717d9b6`](https://github.com/sgl-project/sglang/commit/3c1717d9b6) [#32672](https://github.com/sgl-project/sglang/pull/32672)
  Follow up on #30157 post-merge review (#32672)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_components/kv_pool_runtime.py`, `python/sglang/srt/server_args.py`_
- **2026-07-29** [`50029f05a3`](https://github.com/sgl-project/sglang/commit/50029f05a3) [#30511](https://github.com/sgl-project/sglang/pull/30511)
  [HiCache] Merge HiCache event checks to reduce decode overhead (#30511)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` _+4 more__
- **2026-07-29** [`50b029257f`](https://github.com/sgl-project/sglang/commit/50b029257f) [#32228](https://github.com/sgl-project/sglang/pull/32228)
  Skip mamba lock during decoding (#32228)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` _+7 more__
- **2026-07-29** [`f5bcd00e16`](https://github.com/sgl-project/sglang/commit/f5bcd00e16) [#31747](https://github.com/sgl-project/sglang/pull/31747)
  [AMD] DSv4: bring HIP compress-state pool into the memory_saver KV_CACHE region (#31747)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_compress_state.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`_
- **2026-07-29** [`cce5873513`](https://github.com/sgl-project/sglang/commit/cce5873513) [#32735](https://github.com/sgl-project/sglang/pull/32735)
  [CI] Fail lint when a registered file's TestCase classes never run (#32735)
  _Files: `scripts/ci/check_registered_tests.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_bench.py`_
- **2026-07-29** [`c4fc241fd3`](https://github.com/sgl-project/sglang/commit/c4fc241fd3) [#32701](https://github.com/sgl-project/sglang/pull/32701)
  [Perf] Free KV pages by segment in the paged allocator without a device sync (#32701)
  _Files: `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/paged.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py` _+6 more__
- **2026-07-29** [`14bd315d6e`](https://github.com/sgl-project/sglang/commit/14bd315d6e) [#32709](https://github.com/sgl-project/sglang/pull/32709)
  [Refactor] Remove dead allocator `backup_state` / `restore_state` (#32709)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_allocator.py`, `python/sglang/srt/mem_cache/allocation.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/swa.py` _+1 more__
- **2026-07-29** [`ee678910f7`](https://github.com/sgl-project/sglang/commit/ee678910f7) [#32477](https://github.com/sgl-project/sglang/pull/32477)
  [Kernel] Skip KV writes to reserved padding slots (#32477)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/kvcache.cuh`, `python/sglang/kernels/ops/kvcache/kvcache.py`, `test/registered/kernels/ops/kvcache/test_store_cache.py`_
- **2026-07-28** [`dd67452b4f`](https://github.com/sgl-project/sglang/commit/dd67452b4f) [#32502](https://github.com/sgl-project/sglang/pull/32502)
  [Cleanup] Move mamba-max-states-per-path validation into _handle_mamba_backend (#32502)
  _Files: `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `python/sglang/srt/server_args.py`, `test/registered/unit/mem_cache/test_mamba_path_state_cap.py`_
- **2026-07-28** [`60d6914f17`](https://github.com/sgl-project/sglang/commit/60d6914f17) [#32484](https://github.com/sgl-project/sglang/pull/32484)
  [UnifiedTree]: move /mem_cache/unifed_cache_component dir to /mem_cache/unified_cache (#32484)
  _Files: `python/sglang/srt/hardware_backend/mlx/kv_cache/auxiliary_state.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` _+19 more__
- **2026-07-27** [`4ea17169b0`](https://github.com/sgl-project/sglang/commit/4ea17169b0) [#31902](https://github.com/sgl-project/sglang/pull/31902)
  [UnifiedTree] fix: drop prefetched host refill under an un-backed-up parent (#31902)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-07-27** [`ee1736f39a`](https://github.com/sgl-project/sglang/commit/ee1736f39a) [#30988](https://github.com/sgl-project/sglang/pull/30988)
  [LoRA] Support LoRA under the breakable/full prefill CUDA graph (#30988)
  _Files: `python/sglang/srt/lora/backend/ascend_backend.py`, `python/sglang/srt/lora/backend/base_backend.py`, `python/sglang/srt/lora/backend/chunked_backend.py`, `python/sglang/srt/lora/backend/torch_backend.py` _+9 more__

## Docs / Examples  (18 commits)

- **2026-08-03** [`e9366d7f79`](https://github.com/sgl-project/sglang/commit/e9366d7f79) [#33038](https://github.com/sgl-project/sglang/pull/33038)
  Updated b200 kimi-k3 cookbook (#33038)
  _Files: `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs_new/src/snippets/_deployment.jsx`, `docs_new/src/snippets/_playground.jsx`, `docs_new/src/snippets/configs/moonshotai/kimi-k3-benchmarks.jsx` _+1 more__
- **2026-08-03** [`85484c457d`](https://github.com/sgl-project/sglang/commit/85484c457d) [#33347](https://github.com/sgl-project/sglang/pull/33347)
  docs: refresh README news highlights (#33347)
  _Files: `README.md`_
- **2026-08-01** [`729081e14f`](https://github.com/sgl-project/sglang/commit/729081e14f) [#33173](https://github.com/sgl-project/sglang/pull/33173)
  docs: rewrite the runtime-context skill for the namespace-bag config model (#33173)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`_
- **2026-08-01** [`e4c4faf8a2`](https://github.com/sgl-project/sglang/commit/e4c4faf8a2) [#33131](https://github.com/sgl-project/sglang/pull/33131)
  feat(cookbook): add DGX Spark support for Inkling-Small (#33131)
  _Files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`, `.claude/skills/cookbook-review-pr/SKILL.md` _+5 more__
- **2026-07-31** [`89f4a80c1f`](https://github.com/sgl-project/sglang/commit/89f4a80c1f) [#31859](https://github.com/sgl-project/sglang/pull/31859)
  Support fastsafetensors no-GDS loading and page-cache release (#31859)
  _Files: `docs_new/docs/advanced_features/model_loading.mdx`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/model_loader/weight_utils.py`, `test/registered/unit/model_loader/test_prefetch_checkpoints.py`_
- **2026-07-30** [`85f9998524`](https://github.com/sgl-project/sglang/commit/85f9998524) [#32838](https://github.com/sgl-project/sglang/pull/32838)
  docs: sync LMSYS SGLang blog cards (#32838)
  _Files: `docs_new/index.mdx`_
- **2026-07-30** [`04edadb34d`](https://github.com/sgl-project/sglang/commit/04edadb34d) [#32951](https://github.com/sgl-project/sglang/pull/32951)
  Add Inkling-Small cookbook (#32951)
  _Files: `docs_new/cookbook/autoregressive/ThinkingMachines/Inkling-Small.mdx`, `docs_new/cookbook/autoregressive/ThinkingMachines/Inkling.mdx`, `docs_new/docs.json`, `docs_new/src/snippets/_deployment.jsx` _+3 more__
- **2026-07-30** [`20d5b91e5b`](https://github.com/sgl-project/sglang/commit/20d5b91e5b) [#32749](https://github.com/sgl-project/sglang/pull/32749)
  [NPU] [DOC] update feature name to follow the code changement (#32749)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-07-30** [`5efbb18a6f`](https://github.com/sgl-project/sglang/commit/5efbb18a6f) [#32835](https://github.com/sgl-project/sglang/pull/32835)
  [docs] Rotate popular models on the landing pages, lead the Cookbook nav with Kimi (#32835)
  _Files: `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/cookbook/intro.mdx`, `docs_new/docs.json`, `docs_new/index.mdx` _+2 more__
- **2026-07-29** [`f73d6f2789`](https://github.com/sgl-project/sglang/commit/f73d6f2789) [#32799](https://github.com/sgl-project/sglang/pull/32799)
  Update Inkling cookbook install command (#32799)
  _Files: `docs_new/cookbook/autoregressive/ThinkingMachines/Inkling.mdx`_
- **2026-07-29** [`cb12a1547b`](https://github.com/sgl-project/sglang/commit/cb12a1547b) [#32647](https://github.com/sgl-project/sglang/pull/32647)
  [NPU] [DOC] update supported features on ascend npu (#32647)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-07-28** [`86ee545388`](https://github.com/sgl-project/sglang/commit/86ee545388) [#32592](https://github.com/sgl-project/sglang/pull/32592)
  docs(cookbook): update Kimi-K3 GB200 recipes from measured 4x4 runs (#32592)
  _Files: `docs_new/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-07-28** [`85618cc798`](https://github.com/sgl-project/sglang/commit/85618cc798) [#32654](https://github.com/sgl-project/sglang/pull/32654)
  docs: update sglang cookbook (#32654)
  _Files: `docs_new/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-07-28** [`9c0dbf508f`](https://github.com/sgl-project/sglang/commit/9c0dbf508f) [#32465](https://github.com/sgl-project/sglang/pull/32465)
  [cookbook] add inkling dspark command (#32465)
  _Files: `docs_new/cookbook/autoregressive/ThinkingMachines/Inkling.mdx`, `docs_new/src/snippets/_deployment.jsx`, `docs_new/src/snippets/_playground.jsx`, `docs_new/src/snippets/configs/thinkingmachines/inkling-benchmarks.jsx` _+1 more__
- **2026-07-28** [`b79388f338`](https://github.com/sgl-project/sglang/commit/b79388f338) [#32586](https://github.com/sgl-project/sglang/pull/32586)
  docs(cookbook): mark every Kimi-K3 cell in-progress; land Playground "Switch base" on the configurator (#32586)
  _Files: `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs_new/src/snippets/_deployment.jsx`, `docs_new/src/snippets/_playground.jsx`, `docs_new/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-07-28** [`edc0e5489f`](https://github.com/sgl-project/sglang/commit/edc0e5489f) [#32590](https://github.com/sgl-project/sglang/pull/32590)
  docs: sync LMSYS SGLang blog cards (#32590)
  _Files: `docs_new/index.mdx`_
- **2026-07-27** [`3ebb7c2d07`](https://github.com/sgl-project/sglang/commit/3ebb7c2d07) [#32547](https://github.com/sgl-project/sglang/pull/32547)
  docs: point Kimi-K3 references to public branch (#32547)
  _Files: `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs_new/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-07-27** [`082b2a10b6`](https://github.com/sgl-project/sglang/commit/082b2a10b6) [#32489](https://github.com/sgl-project/sglang/pull/32489)
  Add local ZIP uploader for whl releases (#32489)
  _Files: `scripts/release/README.md`, `scripts/release/update_others_whl_index.py`, `scripts/release/upload_zip_to_whl.sh`_

## Quantization  (13 commits)

- **2026-08-03** [`0bf0640b9d`](https://github.com/sgl-project/sglang/commit/0bf0640b9d) [#33136](https://github.com/sgl-project/sglang/pull/33136)
  [CP] Support breakable CUDA graphs for zigzag strategy (#33136)
  _Files: `python/sglang/srt/layers/cp/bcg.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-08-03** [`b64fd800d4`](https://github.com/sgl-project/sglang/commit/b64fd800d4) [#33282](https://github.com/sgl-project/sglang/pull/33282)
  docs(diffusion): update skills for MiniMax-H3 (#33282)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/references/testing-and-accuracy.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md` _+4 more__
- **2026-08-02** [`1685d29f21`](https://github.com/sgl-project/sglang/commit/1685d29f21) [#31727](https://github.com/sgl-project/sglang/pull/31727)
  [AMD] Fix DeepSeek-V4 fused-RMS FP8 scale metadata on gfx950 (#31727)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/quant/test_fused_rms_fp8_group_quant.py`, `test/registered/unit/layers/test_fp8_bpreshuffle_scale.py`_
- **2026-07-31** [`4af8ddb576`](https://github.com/sgl-project/sglang/commit/4af8ddb576) [#29799](https://github.com/sgl-project/sglang/pull/29799)
  support rust sglang server (#29799)
  _Files: `python/sglang/benchmark/serving.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/environ.py` _+19 more__
- **2026-07-31** [`f94d2c5663`](https://github.com/sgl-project/sglang/commit/f94d2c5663) [#32953](https://github.com/sgl-project/sglang/pull/32953)
  [Fix] Restore online MXFP8 quantization for linear layers (#32953)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/models/nemotron_h.py`_
- **2026-07-30** [`2e9c82b359`](https://github.com/sgl-project/sglang/commit/2e9c82b359) [#32842](https://github.com/sgl-project/sglang/pull/32842)
  [Kernel] Remove unreachable AOT headers (#32842)
  _Files: `python/sglang/kernels/aot/csrc/cutlass_extensions/gemm/dispatch_policy.hpp`, `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cuh`, `python/sglang/kernels/aot/csrc/gemm/marlin/dequant.h`, `python/sglang/kernels/aot/csrc/gemm/marlin/kernel.h` _+3 more__
- **2026-07-30** [`04d6fb4d6c`](https://github.com/sgl-project/sglang/commit/04d6fb4d6c) [#32036](https://github.com/sgl-project/sglang/pull/32036)
  [AMD] Minimax-M3 : unblock mxfp8 block convert on gfx950 (#32036)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`_
- **2026-07-29** [`f69af7b7ad`](https://github.com/sgl-project/sglang/commit/f69af7b7ad) [#32736](https://github.com/sgl-project/sglang/pull/32736)
  [Bugfix] compressed-tensors: mixed-precision checkpoints silently load unquantized (#32736)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`, `test/registered/unit/layers/quantization/test_compressed_tensors_mixed_precision.py`_
- **2026-07-29** [`9ab88380c1`](https://github.com/sgl-project/sglang/commit/9ab88380c1) [#31917](https://github.com/sgl-project/sglang/pull/31917)
  :busts_in_silhouette: chore(codeowners): Update codeowners for NPU quantization (#31917)
  _Files: `.github/CODEOWNERS`_
- **2026-07-29** [`d6fcfe02d6`](https://github.com/sgl-project/sglang/commit/d6fcfe02d6) [#32013](https://github.com/sgl-project/sglang/pull/32013)
  :bug: [llm][npu][quant] Fix ModelSlim MXFP4 packed weight loading (#32013)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`, `python/sglang/srt/layers/quantization/modelslim/schemes/modelslim_mxfp4.py`_
- **2026-07-29** [`9ea964a535`](https://github.com/sgl-project/sglang/commit/9ea964a535) [#32157](https://github.com/sgl-project/sglang/pull/32157)
  [diffusion] fix: per-shard FP8 scale shape for single-GPU fused linears (#32157)
  _Files: `python/sglang/multimodal_gen/runtime/layers/linear.py`_
- **2026-07-28** [`7778dd23ea`](https://github.com/sgl-project/sglang/commit/7778dd23ea) [#32651](https://github.com/sgl-project/sglang/pull/32651)
  [diffusion] refactor: remove stale kernels and dead code (#32651)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/cutedsl/norm_tanh_mul_add_norm_scale.py`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/references/testing-and-accuracy.md` _+25 more__
- **2026-07-28** [`dde03d7c4a`](https://github.com/sgl-project/sglang/commit/dde03d7c4a) [#32616](https://github.com/sgl-project/sglang/pull/32616)
  [JIT] Restore the previous division behavior in per-token group quantization (#32616)
  _Files: `python/sglang/kernels/jit/csrc/gemm/per_token_group_quant.cuh`_

## Speculative Decoding  (10 commits)

- **2026-08-03** [`9bc8848fcf`](https://github.com/sgl-project/sglang/commit/9bc8848fcf) [#33335](https://github.com/sgl-project/sglang/pull/33335)
  spec: build every draft worker from a draft ServerArgs copy (#33335)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/draft_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` _+6 more__
- **2026-08-03** [`2a7a299c27`](https://github.com/sgl-project/sglang/commit/2a7a299c27) [#33298](https://github.com/sgl-project/sglang/pull/33298)
  [Spec] Support sampling in the DSPARK graph-folded draft proposal (#33298)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-07-31** [`ab2553284a`](https://github.com/sgl-project/sglang/commit/ab2553284a) [#33011](https://github.com/sgl-project/sglang/pull/33011)
  config: preserve resolved config across nested publishes + mutation ratchets (#33011)
  _Files: `python/sglang/srt/runtime_context.py`, `python/sglang/srt/speculative/draft_worker_common.py`, `test/registered/unit/test_migration_deferral_ratchet.py`, `test/registered/unit/test_runtime_context_override.py` _+1 more__
- **2026-07-31** [`5df193b4ac`](https://github.com/sgl-project/sglang/commit/5df193b4ac) [#32334](https://github.com/sgl-project/sglang/pull/32334)
  [Speculative Decoding] Fix GPT-OSS EAGLE3 hidden states (#32334)
  _Files: `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/models/llama_eagle3.py`_
- **2026-07-30** [`9f56553408`](https://github.com/sgl-project/sglang/commit/9f56553408) [#32887](https://github.com/sgl-project/sglang/pull/32887)
  [Perf] Fast-path chain-style draft token organization in multi-layer EAGLE (#32887)
  _Files: `python/sglang/srt/speculative/base_spec_worker.py`, `python/sglang/srt/speculative/eagle_utils.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` _+1 more__
- **2026-07-30** [`2625fdfe6b`](https://github.com/sgl-project/sglang/commit/2625fdfe6b) [#32867](https://github.com/sgl-project/sglang/pull/32867)
  [Fix] Count multi-layer draft-extend replays in the fwd-occupancy device timer (#32867)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`, `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py` _+4 more__
- **2026-07-30** [`f4e0ac382e`](https://github.com/sgl-project/sglang/commit/f4e0ac382e) [#32881](https://github.com/sgl-project/sglang/pull/32881)
  [misc] Remove unused multi_layer_draft_forward_cg module (#32881)
  _Files: `python/sglang/srt/speculative/multi_layer_draft_forward_cg.py`_
- **2026-07-30** [`313a518bee`](https://github.com/sgl-project/sglang/commit/313a518bee) [#32850](https://github.com/sgl-project/sglang/pull/32850)
  [Spec] Emit step trace span for multi-layer draft-extend graph replays (#32850)
  _Files: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-07-29** [`ca6e0ff2c8`](https://github.com/sgl-project/sglang/commit/ca6e0ff2c8) [#32711](https://github.com/sgl-project/sglang/pull/32711)
  [NPU] fix dsv4 mtp condition on NPU graph (#32711)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`_
- **2026-07-29** [`bd47ec97ff`](https://github.com/sgl-project/sglang/commit/bd47ec97ff) [#32396](https://github.com/sgl-project/sglang/pull/32396)
  [EAGLE] Handle NaNs in fused top-k=1 (#32396)
  _Files: `python/sglang/kernels/ops/speculative/topk1.py`_

## ROCm / AMD  (9 commits)

- **2026-08-03** [`21d930aae3`](https://github.com/sgl-project/sglang/commit/21d930aae3) [#33195](https://github.com/sgl-project/sglang/pull/33195)
  [AMD] Fix JIT compile failure in sgl_kernel/warp.cuh (#33195)
  _Files: `python/sglang/kernels/jit/include/sgl_kernel/warp.cuh`_
- **2026-07-31** [`70cec31378`](https://github.com/sgl-project/sglang/commit/70cec31378) [#32862](https://github.com/sgl-project/sglang/pull/32862)
  [AMD] Pin mem_fraction_static for the piecewise CUDA graph 1-GPU test on MI300 (#32862)
  _Files: `test/registered/cuda_graph/piecewise/test_piecewise_cuda_graph_support_1_gpu.py`_
- **2026-07-30** [`48c1b37a33`](https://github.com/sgl-project/sglang/commit/48c1b37a33) [#32939](https://github.com/sgl-project/sglang/pull/32939)
  [AMD] Update ROCm AITER pin to d9e5ef7 (#32939)
  _Files: `docker/rocm.Dockerfile`_
- **2026-07-30** [`fd86795107`](https://github.com/sgl-project/sglang/commit/fd86795107) [#32230](https://github.com/sgl-project/sglang/pull/32230)
  [AMD] MiniMax-M3: opt-in custom/quick all-reduce on ROCm (#32230)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/environ.py`_
- **2026-07-30** [`3d6e1e6f81`](https://github.com/sgl-project/sglang/commit/3d6e1e6f81) [#32879](https://github.com/sgl-project/sglang/pull/32879)
  [AMD] Revert ROCm AITER pin to 9127c94 (#32879)
  _Files: `docker/rocm.Dockerfile`_
- **2026-07-29** [`bfc450248e`](https://github.com/sgl-project/sglang/commit/bfc450248e) [#31409](https://github.com/sgl-project/sglang/pull/31409)
  [AMD] Replace MI325 with MI300 CI Runners (#31409)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd-extra.yml`, `.github/workflows/pr-test-amd-rocm720.yml` _+5 more__
- **2026-07-29** [`68673fe6c5`](https://github.com/sgl-project/sglang/commit/68673fe6c5) [#32613](https://github.com/sgl-project/sglang/pull/32613)
  [AMD] add Gemma3RMSNorm.forward_hip to unbreak ROCm (#32613)
  _Files: `python/sglang/srt/layers/layernorm.py`_
- **2026-07-28** [`2b6e01c673`](https://github.com/sgl-project/sglang/commit/2b6e01c673) [#32632](https://github.com/sgl-project/sglang/pull/32632)
  [AMD] Run AITER Scout on Saturdays (#32632)
  _Files: `.github/workflows/amd-aiter-scout.yml`_
- **2026-07-27** [`c6a6200a1a`](https://github.com/sgl-project/sglang/commit/c6a6200a1a) [#32469](https://github.com/sgl-project/sglang/pull/32469)
  [AMD] Fix pip setup in AMD Miles nightly builds (#32469)
  _Files: `.github/workflows/release-docker-amd-miles-rocm700-nightly.yml`, `.github/workflows/release-docker-amd-miles-rocm720-nightly.yml`_

## Scheduler / Batching  (9 commits)

- **2026-08-03** [`aa3bbbc6e8`](https://github.com/sgl-project/sglang/commit/aa3bbbc6e8) [#33337](https://github.com/sgl-project/sglang/pull/33337)
  observability: publish the generated forward-pass-metrics endpoint to the bags (#33337)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`, `test/registered/unit/test_server_args_writer_ratchet.py`_
- **2026-08-03** [`0b3e8bedd1`](https://github.com/sgl-project/sglang/commit/0b3e8bedd1) [#33336](https://github.com/sgl-project/sglang/pull/33336)
  config: keep runtime hicache and weight-version updates off ServerArgs (#33336)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/grpc_bridge.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/realtime/session.py` _+12 more__
- **2026-08-03** [`c844244da5`](https://github.com/sgl-project/sglang/commit/c844244da5) [#33105](https://github.com/sgl-project/sglang/pull/33105)
  support dp attn with client lb (#33105)
  _Files: `python/sglang/srt/managers/rust_server.py`, `python/sglang/srt/server_args.py`_
- **2026-08-02** [`a0b7bcf592`](https://github.com/sgl-project/sglang/commit/a0b7bcf592) [#30177](https://github.com/sgl-project/sglang/pull/30177)
  [Feature] Support return_hidden_states="last" (#30177)
  _Files: `examples/runtime/hidden_states/hidden_states_engine.py`, `examples/runtime/hidden_states/hidden_states_server.py`, `python/sglang/srt/entrypoints/EngineBase.py`, `python/sglang/srt/entrypoints/engine.py` _+26 more__
- **2026-08-01** [`c0d06a6547`](https://github.com/sgl-project/sglang/commit/c0d06a6547) [#33179](https://github.com/sgl-project/sglang/pull/33179)
  [CI] Fix runtime context setup in flat logprob tests (#33179)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/logprob_result_processor.py`, `test/registered/unit/managers/test_flat_raw_top_logprobs.py`_
- **2026-08-01** [`58974ca16c`](https://github.com/sgl-project/sglang/commit/58974ca16c) [#32223](https://github.com/sgl-project/sglang/pull/32223)
  [perf] Assemble flat prompt top logprobs scheduler-side as numpy arrays (#32223)
  _Files: `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/schedule_batch.py` _+5 more__
- **2026-07-29** [`d0e69d3881`](https://github.com/sgl-project/sglang/commit/d0e69d3881) [#31960](https://github.com/sgl-project/sglang/pull/31960)
  [feat] Optional base64 encoding for the flat prompt top logprob arrays (#31960)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_flat_raw_top_logprobs.py`_
- **2026-07-28** [`c19a333944`](https://github.com/sgl-project/sglang/commit/c19a333944) [#32498](https://github.com/sgl-project/sglang/pull/32498)
  [mm] Handle per-item embeddings in cache misses (#32498)
  _Files: `python/sglang/srt/managers/mm_utils.py`_
- **2026-07-27** [`5cc273a780`](https://github.com/sgl-project/sglang/commit/5cc273a780) [#32078](https://github.com/sgl-project/sglang/pull/32078)
  [feat] Opt-in flat response format for prompt top logprobs (#32078)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_flat_raw_top_logprobs.py`_

## Models  (8 commits)

- **2026-08-01** [`e1964da451`](https://github.com/sgl-project/sglang/commit/e1964da451) [#33157](https://github.com/sgl-project/sglang/pull/33157)
  [Docs] Add RTX 5090 DeepSeek-V4 recipe (#33157)
  _Files: `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-07-30** [`b61cb5f9de`](https://github.com/sgl-project/sglang/commit/b61cb5f9de) [#30240](https://github.com/sgl-project/sglang/pull/30240)
  Fix DeepSeek V4 loading with RunAI Model Streamer. (#30240)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_dspark.py`, `test/registered/unit/model_loader/test_runai_model_streamer_loader.py`_
- **2026-07-29** [`d254ec9ff8`](https://github.com/sgl-project/sglang/commit/d254ec9ff8) [#28691](https://github.com/sgl-project/sglang/pull/28691)
  Add LFM2.5 embedding model support (#28691)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/lfm2.py`_
- **2026-07-28** [`51397af885`](https://github.com/sgl-project/sglang/commit/51397af885) [#28956](https://github.com/sgl-project/sglang/pull/28956)
  Pack aux hidden states into a preallocated buffer (#28956)
  _Files: `python/sglang/srt/layers/aux_hidden_states.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/models/deepseek_v2.py`_
- **2026-07-28** [`fc8b328f5c`](https://github.com/sgl-project/sglang/commit/fc8b328f5c) [#32401](https://github.com/sgl-project/sglang/pull/32401)
  [Model] Support standalone text-only Qwen3.5 checkpoints (#32401)
  _Files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/qwen3_5_text.py`, `python/sglang/srt/utils/hf_transformers/common.py`_
- **2026-07-27** [`7dafacca49`](https://github.com/sgl-project/sglang/commit/7dafacca49) [#32542](https://github.com/sgl-project/sglang/pull/32542)
  docs(cookbook): add the Kimi-K3 serving cookbook (#32542)
  _Files: `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K2.7-Code.mdx`, `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs_new/cookbook/autoregressive/intro.mdx` _+10 more__
- **2026-07-27** [`1d350aaad3`](https://github.com/sgl-project/sglang/commit/1d350aaad3) [#32400](https://github.com/sgl-project/sglang/pull/32400)
  fix(reasoning):  let --enable-strict-thinking works for DeepSeek-V4 (#32400)
  _Files: `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/parser/test_reasoning_parser.py`_
- **2026-07-27** [`9a0bd24bed`](https://github.com/sgl-project/sglang/commit/9a0bd24bed) [#32457](https://github.com/sgl-project/sglang/pull/32457)
  model: serve bare Qwen3Model backbone natively as an embedding model (#32457)
  _Files: `docs_new/docs/supported-models/embedding_models.mdx`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/qwen3_embedding.py`, `test/registered/unit/models/test_qwen3_embedding_registration.py`_

## Triton / Kernels  (7 commits)

- **2026-08-03** [`28a2472f95`](https://github.com/sgl-project/sglang/commit/28a2472f95) [#32910](https://github.com/sgl-project/sglang/pull/32910)
  [DeepSeek-V4] Fix nvcc 13 crash building the topk_v2 kernel (#32910)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`_
- **2026-08-01** [`e0ba311026`](https://github.com/sgl-project/sglang/commit/e0ba311026) [#33130](https://github.com/sgl-project/sglang/pull/33130)
  Disable breakable CUDA graph for NemotronH (#33130)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/server_args.py`_
- **2026-07-31** [`0d6bef6b6d`](https://github.com/sgl-project/sglang/commit/0d6bef6b6d) [#32986](https://github.com/sgl-project/sglang/pull/32986)
  [NPU] [DOC] renew triton-ascend installation guide location (#32986)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`_
- **2026-07-31** [`3abbc565e4`](https://github.com/sgl-project/sglang/commit/3abbc565e4) [#32956](https://github.com/sgl-project/sglang/pull/32956)
  [Docs] Add a Conventions section to the add-jit-kernel skill (#32956)
  _Files: `.claude/skills/add-jit-kernel/SKILL.md`_
- **2026-07-29** [`8742a1a0f8`](https://github.com/sgl-project/sglang/commit/8742a1a0f8) [#32642](https://github.com/sgl-project/sglang/pull/32642)
  Add a benchmark script for the HPC-Ops bf16xfp32 router GEMM (#32642)
  _Files: `test/registered/kernels/benchmark/gemm/bench_bf16xfp32_router_gemm.py`_
- **2026-07-29** [`c32c4ef79c`](https://github.com/sgl-project/sglang/commit/c32c4ef79c) [#32648](https://github.com/sgl-project/sglang/pull/32648)
  [Kernel] Move sgl-kernel under sglang.kernels.aot (#32648)
- **2026-07-29** [`dac4325c0e`](https://github.com/sgl-project/sglang/commit/dac4325c0e) [#32596](https://github.com/sgl-project/sglang/pull/32596)
  sgl-kernel-npu tag update to 2026.7.27 (#32596)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `scripts/ci/npu/npu_ci_install_dependency.sh`_

## Tensor / Data Parallel  (4 commits)

- **2026-08-03** [`45c00daa1b`](https://github.com/sgl-project/sglang/commit/45c00daa1b) [#33351](https://github.com/sgl-project/sglang/pull/33351)
  [misc] Deep-merge nested config overrides and parse request bodies with orjson (#33351)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/utils/hf_transformers/config.py`_
- **2026-07-30** [`30643f88bc`](https://github.com/sgl-project/sglang/commit/30643f88bc) [#32875](https://github.com/sgl-project/sglang/pull/32875)
  add the rust server api frame codec and http server entry (#32875)
  _Files: `rust/sglang-server/src/api_server.rs`, `rust/sglang-server/src/api_server/frame.rs`_
- **2026-07-30** [`3c9efaf3e1`](https://github.com/sgl-project/sglang/commit/3c9efaf3e1) [#32834](https://github.com/sgl-project/sglang/pull/32834)
  [docs] Kimi-K3: widen the H200 High-Throughput recipe to 4x8 TP32/EP32 (#32834)
  _Files: `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs_new/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-07-29** [`e1f2f9d1fa`](https://github.com/sgl-project/sglang/commit/e1f2f9d1fa) [#27089](https://github.com/sgl-project/sglang/pull/27089)
  Disable extra NCCL CUDA event synchronization with symm mem (#27089)
  _Files: `python/sglang/srt/distributed/device_communicators/pynccl.py`, `python/sglang/srt/distributed/device_communicators/pynccl_wrapper.py`, `python/sglang/srt/distributed/parallel_state.py`_

## Structured Output  (4 commits)

- **2026-08-03** [`e00f32ed4f`](https://github.com/sgl-project/sglang/commit/e00f32ed4f) [#33103](https://github.com/sgl-project/sglang/pull/33103)
  feat: rust sglang server openai apis (#33103)
  _Files: `python/sglang/srt/managers/rust_server.py`, `rust/Cargo.lock`, `rust/rust-toolchain.toml`, `rust/sglang-server/Cargo.toml` _+24 more__
- **2026-08-03** [`f5f021672a`](https://github.com/sgl-project/sglang/commit/f5f021672a) [#33328](https://github.com/sgl-project/sglang/pull/33328)
  [Fix] Treat an empty grammar constraint as unset in SamplingParams (#33328)
  _Files: `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/sampling/sampling_params.py`, `test/registered/unit/constrained/test_grammar_manager.py`, `test/registered/unit/sampling/test_sampling_params.py`_
- **2026-07-30** [`1f04eaab6a`](https://github.com/sgl-project/sglang/commit/1f04eaab6a) [#27614](https://github.com/sgl-project/sglang/pull/27614)
  Fix LFM 2 tool parser. (#27614)
  _Files: `python/sglang/srt/function_call/lfm2_detector.py`_
- **2026-07-30** [`07a087bf45`](https://github.com/sgl-project/sglang/commit/07a087bf45) [#32861](https://github.com/sgl-project/sglang/pull/32861)
  Fix Inkling tool-call parsing recovery, content handling, and streaming (#32861)
  _Files: `python/sglang/srt/function_call/inkling_detector.py`, `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/function_call/test_function_call_parser.py`, `test/registered/unit/parser/test_reasoning_parser.py`_

## CI / Build  (4 commits)

- **2026-08-03** [`fcc4de9e5f`](https://github.com/sgl-project/sglang/commit/fcc4de9e5f) [#33329](https://github.com/sgl-project/sglang/pull/33329)
  [CI] Size the CPU stage from the live partition model (#33329)
  _Files: `.github/workflows/pr-test.yml`, `scripts/ci/utils/compute_partitions.py`_
- **2026-08-02** [`27b15349e5`](https://github.com/sgl-project/sglang/commit/27b15349e5) [#33277](https://github.com/sgl-project/sglang/pull/33277)
  [CI] Fix stale CPU test fixtures (#33277)
- **2026-08-01** [`a1344fad4e`](https://github.com/sgl-project/sglang/commit/a1344fad4e) [#33143](https://github.com/sgl-project/sglang/pull/33143)
  Replace Kimi K3 DeepGEMM patch with 0.1.5.post1 (#33143)
  _Files: `docker/kimi_k3/apply_deepgemm_situ_patch.py`, `docker/kimi_k3/kimi_k3_cu12.Dockerfile`, `docker/kimi_k3/kimi_k3_cu13.Dockerfile`_
- **2026-07-31** [`301ea43f35`](https://github.com/sgl-project/sglang/commit/301ea43f35) [#32719](https://github.com/sgl-project/sglang/pull/32719)
  [CI] Re-enable GB300 CI jobs (#32719)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/release-whl-deepgemm.yml`_

## Serving / API  (4 commits)

- **2026-07-31** [`9dcaf6bfdf`](https://github.com/sgl-project/sglang/commit/9dcaf6bfdf) [#33096](https://github.com/sgl-project/sglang/pull/33096)
  rust server build release artifacts (#33096)
  _Files: `rust/sglang-grpc/Cargo.toml`, `rust/sglang-server/Cargo.toml`_
- **2026-07-31** [`690de097c4`](https://github.com/sgl-project/sglang/commit/690de097c4) [#32914](https://github.com/sgl-project/sglang/pull/32914)
  [fix]reject media input for text-only models (#32914)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_responses.py`_
- **2026-07-31** [`09193bf36f`](https://github.com/sgl-project/sglang/commit/09193bf36f) [#32522](https://github.com/sgl-project/sglang/pull/32522)
  [Fix]: render tool_reference schema regardless of tool_result part order (#32522)
  _Files: `python/sglang/srt/entrypoints/anthropic/serving.py`, `test/registered/unit/entrypoints/anthropic/test_serving.py`_
- **2026-07-30** [`e2c65af229`](https://github.com/sgl-project/sglang/commit/e2c65af229) [#32873](https://github.com/sgl-project/sglang/pull/32873)
  add the rust server ingress request validation and api server common types (#32873)
  _Files: `rust/sglang-server/src/api_server/common.rs`, `rust/sglang-server/src/api_server/log.rs`, `rust/sglang-server/src/api_server/openai.rs`, `rust/sglang-server/src/tokenizer_manager/ingress.rs`_

## LoRA  (2 commits)

- **2026-08-02** [`21d932069b`](https://github.com/sgl-project/sglang/commit/21d932069b) [#33251](https://github.com/sgl-project/sglang/pull/33251)
  docs: drop unreachable inkling LoRA benchmark entry (#33251)
  _Files: `docs_new/src/snippets/configs/thinkingmachines/inkling-benchmarks.jsx`_
- **2026-07-28** [`0a49226d19`](https://github.com/sgl-project/sglang/commit/0a49226d19) [#32580](https://github.com/sgl-project/sglang/pull/32580)
  [LoRA] 1/n Per-rank tensor serialization for load_lora_adapter_from_tensors under dp_size > 1 (#32580)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_control_mixin.py`, `python/sglang/srt/managers/tp_worker.py` _+2 more__

---
_Generated 2026-08-03 11:36 UTC_