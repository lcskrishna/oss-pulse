# sgl-project/sglang — Weekly Change Report
**Period:** 2026-10-05 → 2026-10-12  |  **Total commits:** 537

## ✨ New Features This Week

- **2026-10-12** [#37426](https://github.com/sgl-project/sglang/pull/37426) — [CI][Diffusion] Add caching for npu GT images in CI (#37426)
- **2026-10-12** [#40323](https://github.com/sgl-project/sglang/pull/40323) — [DSV4.1][PD][1/N] Support prefill node use cp parallel strategy (#40323)
- **2026-10-12** [#38603](https://github.com/sgl-project/sglang/pull/38603) — [BCG][DSV4-Flash][CP] Support DeepSeek V4 prefill with interleave CP and breakable CUDA graphs (#38603)
- **2026-10-12** [#34355](https://github.com/sgl-project/sglang/pull/34355) — [XPU] Support decode context parallelism (DCP) on Intel XPU (#34355)
- **2026-10-12** [#36345](https://github.com/sgl-project/sglang/pull/36345) — [HiCache] Support Mamba in buffer-only host memory mode (#36345)
- **2026-10-12** [#41940](https://github.com/sgl-project/sglang/pull/41940) — [diffusion][xpu] FLUX.2: enable the bit-exact Triton SwiGLU on XPU (#41940)
- **2026-10-12** [#40666](https://github.com/sgl-project/sglang/pull/40666) — [AMD][MORI] Add MORI EP V2 support (#40666)
- **2026-10-12** [#40925](https://github.com/sgl-project/sglang/pull/40925) — Support kv cache sharding for DSA indexer (#40925)
- **2026-10-12** [#43722](https://github.com/sgl-project/sglang/pull/43722) — [MemCache] Add shared component size and path APIs to the tree core interface (#43722)
- **2026-10-11** [#43670](https://github.com/sgl-project/sglang/pull/43670) — [DSpark] Add `SGLANG_DSPARK_USE_GREEDY_DRAFT`, an argmax draft accepted as one-hot (#43670)
- _…and 88 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-12** [`0d0be8fc98`](https://github.com/sgl-project/sglang/commit/0d0be8fc98) [#40666](https://github.com/sgl-project/sglang/pull/40666) — [AMD][MORI] Add MORI EP V2 support (#40666)
- **2026-10-12** [`37d2e5c34f`](https://github.com/sgl-project/sglang/commit/37d2e5c34f) [#43077](https://github.com/sgl-project/sglang/pull/43077) — [AMD][V4.1][*/N] Fix DP attention + TP MoE decode NaN and support bounded replay (#43077)
- **2026-10-11** [`22d63f5e43`](https://github.com/sgl-project/sglang/commit/22d63f5e43) [#43383](https://github.com/sgl-project/sglang/pull/43383) — [AMD]Qwen add Sparse attention to capturing hip graphs (#43383)
- **2026-10-10** [`a916d91cd3`](https://github.com/sgl-project/sglang/commit/a916d91cd3) [#43547](https://github.com/sgl-project/sglang/pull/43547) — [AMD][CI] Cap pyarrow below 26 for lmms-eval (#43547)
- **2026-10-10** [`ff19159e16`](https://github.com/sgl-project/sglang/commit/ff19159e16) [#41071](https://github.com/sgl-project/sglang/pull/41071) — [AMD] Add an opt-in AITER CK blockscale GEMM for gfx942 block-FP8 linears (#41071)
- **2026-10-10** [`e35f60b9bc`](https://github.com/sgl-project/sglang/commit/e35f60b9bc) [#43318](https://github.com/sgl-project/sglang/pull/43318) — [AMD][CI] Drop removed tp_rank/tp_size kwargs from small-M FP8 proj test (#43318)
- **2026-10-10** [`d7d22e8a30`](https://github.com/sgl-project/sglang/commit/d7d22e8a30) [#39840](https://github.com/sgl-project/sglang/pull/39840) — [AMD] Resolving bug in per batch size graph capture due to multiple capture runs per batch size (#39840)
- **2026-10-10** [`8b2aaf7060`](https://github.com/sgl-project/sglang/commit/8b2aaf7060) [#42287](https://github.com/sgl-project/sglang/pull/42287) — [Refactor][TCPCG] Retire backend selection and configuration (3/9) (#42287)
- **2026-10-10** [`37114afe20`](https://github.com/sgl-project/sglang/commit/37114afe20) [#42982](https://github.com/sgl-project/sglang/pull/42982) — [AMD][Fix] Saturate FP8 KV commits instead of reproducing e4m3fnuz NaN overflow (#42982)
- **2026-10-09** [`6d8ddaf1d7`](https://github.com/sgl-project/sglang/commit/6d8ddaf1d7) [#42614](https://github.com/sgl-project/sglang/pull/42614) — [AMD] MiniMax-M3 indexer CP: packed scoring for EAGLE verify rows (#42614)
- **2026-10-09** [`70e82f7b73`](https://github.com/sgl-project/sglang/commit/70e82f7b73) [#43259](https://github.com/sgl-project/sglang/pull/43259) — [AMD] Run the MiniMax indexer CP test on MI35X, not MI300 (#43259)
- **2026-10-09** [`db32673b78`](https://github.com/sgl-project/sglang/commit/db32673b78) [#41258](https://github.com/sgl-project/sglang/pull/41258) — [AMD] Let the GLM DSA NextN draft declare its own shared-expert fusion architecture (#41258)
- **2026-10-09** [`d5c3ae9752`](https://github.com/sgl-project/sglang/commit/d5c3ae9752) [#41030](https://github.com/sgl-project/sglang/pull/41030) — [AMD] Eliminate remaining gfx95 FP8 scale relayout copies (#41030)
- **2026-10-09** [`348689da40`](https://github.com/sgl-project/sglang/commit/348689da40) [#38959](https://github.com/sgl-project/sglang/pull/38959) — [PP+PD] Fix #38206 Reduce bootstrap consensus latency (#38959)
- **2026-10-09** [`5eca4d8caf`](https://github.com/sgl-project/sglang/commit/5eca4d8caf) [#42570](https://github.com/sgl-project/sglang/pull/42570) — [AMD] Set maxseq length limit for DSV4.1 BCG metadata buffers (#42570)
- **2026-10-09** [`23f890613e`](https://github.com/sgl-project/sglang/commit/23f890613e) [#43319](https://github.com/sgl-project/sglang/pull/43319) — [AMD] Patch aiter's group32 MXFP8 GEMM masked-scale fix (#43319)
- **2026-10-09** [`51f7ea84c7`](https://github.com/sgl-project/sglang/commit/51f7ea84c7) [#42772](https://github.com/sgl-project/sglang/pull/42772) — [AMD] Keep MiniMax decode-score tile at 128 tokens off gfx950 (#42772)
- **2026-10-09** [`08fc290f48`](https://github.com/sgl-project/sglang/commit/08fc290f48) [#41982](https://github.com/sgl-project/sglang/pull/41982) — [AMD] gfx950 small-batch MoE: expert-count gate for the small sort and FP8 block-scale small-M kernel (#41982)
- **2026-10-09** [`3c1703d2ff`](https://github.com/sgl-project/sglang/commit/3c1703d2ff) [#31054](https://github.com/sgl-project/sglang/pull/31054) — [AMD] Support Quark DeepSeek-V4-MXFP4 checkpoints on the DSV4 stack, enabling shared-expert fusion and MTP (#31054)
- **2026-10-08** [`baee5f3b62`](https://github.com/sgl-project/sglang/commit/baee5f3b62) [#43234](https://github.com/sgl-project/sglang/pull/43234) — [CI] Drop the `labeled` trigger from the extra CI workflows (#43234)
- **2026-10-08** [`4ab4d90d78`](https://github.com/sgl-project/sglang/commit/4ab4d90d78) [#34537](https://github.com/sgl-project/sglang/pull/34537) — [AMD][DCP 3/N] add aiter asm for kimi k3 target verify (#34537)
- **2026-10-08** [`2d26823f94`](https://github.com/sgl-project/sglang/commit/2d26823f94) [#42152](https://github.com/sgl-project/sglang/pull/42152) — [AMD] Drop static input_scale on aiter per-token FP8 path (use dynamic per-token) (#42152)
- **2026-10-08** [`b3e6c87be3`](https://github.com/sgl-project/sglang/commit/b3e6c87be3) [#42753](https://github.com/sgl-project/sglang/pull/42753) — [Refactor] Translate each KV loc once per iteration (#42753)
- **2026-10-08** [`5afe4d6334`](https://github.com/sgl-project/sglang/commit/5afe4d6334) [#42230](https://github.com/sgl-project/sglang/pull/42230) — [AMD] Fix DSpark draft bucket tests for the raw in-graph metadata default (#42230)
- **2026-10-08** [`8b80808366`](https://github.com/sgl-project/sglang/commit/8b80808366) [#37628](https://github.com/sgl-project/sglang/pull/37628) — [unified-memory] Fuse the draft model's KV into the target's page envelope (mechanism) (#37628)
- **2026-10-08** [`08d30f2300`](https://github.com/sgl-project/sglang/commit/08d30f2300) [#37627](https://github.com/sgl-project/sglang/pull/37627) — [unified-memory] Speculative decoding on the unified memory pool: translate every read and write path (#37627)
- **2026-10-08** [`33883a5fa3`](https://github.com/sgl-project/sglang/commit/33883a5fa3) [#41134](https://github.com/sgl-project/sglang/pull/41134) — [AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950 (#41134)
- **2026-10-08** [`b2cd65b8b0`](https://github.com/sgl-project/sglang/commit/b2cd65b8b0) [#41133](https://github.com/sgl-project/sglang/pull/41133) — [AMD] One-launch small-M MoE router for Qwen3.5 on gfx950 (#41133)
- **2026-10-08** [`b72da1b817`](https://github.com/sgl-project/sglang/commit/b72da1b817) [#43033](https://github.com/sgl-project/sglang/pull/43033) — [AMD] Update v4 amd cookbook 1008 (#43033)
- **2026-10-08** [`c892301ff7`](https://github.com/sgl-project/sglang/commit/c892301ff7) [#35594](https://github.com/sgl-project/sglang/pull/35594) — [Platform] Thread vendor KV pool classes through the in-tree builders; add PlatformCapabilities (#35594)
- **2026-10-07** [`79ef49cb6b`](https://github.com/sgl-project/sglang/commit/79ef49cb6b) [#43015](https://github.com/sgl-project/sglang/pull/43015) — [Docs] GLM-5.3-Flash: measured MI355X MXFP4 agentic recipe (#43015)
- **2026-10-07** [`c389cbaf99`](https://github.com/sgl-project/sglang/commit/c389cbaf99) [#42859](https://github.com/sgl-project/sglang/pull/42859) — [AMD][diffusion] Route bf16 fuse_scale_shift to the native fallback on gfx1250 (#42859)
- **2026-10-07** [`49d7d60dfa`](https://github.com/sgl-project/sglang/commit/49d7d60dfa) [#42858](https://github.com/sgl-project/sglang/pull/42858) — [AMD][diffusion] VAE attention to the math SDPA backend on gfx1250 (#42858)
- **2026-10-07** [`11972e5207`](https://github.com/sgl-project/sglang/commit/11972e5207) [#42784](https://github.com/sgl-project/sglang/pull/42784) — [deps] bump transformers to 5.19.0 (#42784)
- **2026-10-07** [`1c42ad3679`](https://github.com/sgl-project/sglang/commit/1c42ad3679) [#42747](https://github.com/sgl-project/sglang/pull/42747) — [ROCm] Skip the tilelang act_quant in the DSA indexer on gfx1250 (#42747)
- **2026-10-07** [`9ddbba50dd`](https://github.com/sgl-project/sglang/commit/9ddbba50dd) [#39923](https://github.com/sgl-project/sglang/pull/39923) — [AMD][DSV4] feat: enable PCP with fp8 unified_kv on gfx950 (#39923)
- **2026-10-07** [`168458fd90`](https://github.com/sgl-project/sglang/commit/168458fd90) [#42796](https://github.com/sgl-project/sglang/pull/42796) — [AMD][V4.1] Fix wo_b input flatten for packed fp8 activations on gfx950 (#42796)
- **2026-10-07** [`9e26600f3a`](https://github.com/sgl-project/sglang/commit/9e26600f3a) [#42671](https://github.com/sgl-project/sglang/pull/42671) — [DSA] Clarify pooled-page naming and ownership (#42671)
- **2026-10-07** [`c0df52be2d`](https://github.com/sgl-project/sglang/commit/c0df52be2d) [#34540](https://github.com/sgl-project/sglang/pull/34540) — [AMD] Fix Quark W4A4 MXFP4 MoE clamped-SwiGLU on the AITER path (#34540)
- **2026-10-07** [`9a21d82958`](https://github.com/sgl-project/sglang/commit/9a21d82958) [#42847](https://github.com/sgl-project/sglang/pull/42847) — [AMD] Update v4.1 amd cookbook 1006 (#42847)
- **2026-10-07** [`660b17e8dc`](https://github.com/sgl-project/sglang/commit/660b17e8dc) [#42635](https://github.com/sgl-project/sglang/pull/42635) — [AMD] Let AITER unified verify run without host seq_lens (#42635)
- **2026-10-07** [`e13933c4fd`](https://github.com/sgl-project/sglang/commit/e13933c4fd) [#41670](https://github.com/sgl-project/sglang/pull/41670) — [diffusion] docs: add gfx1151 Strix Halo serving guidance (#41670)
- **2026-10-07** [`3e914e69d5`](https://github.com/sgl-project/sglang/commit/3e914e69d5) [#42771](https://github.com/sgl-project/sglang/pull/42771) — [AMD] ci: nightly-test the miles ROCm 10 MI30X image on MI300 (#42771)
- **2026-10-06** [`66dd4e15b9`](https://github.com/sgl-project/sglang/commit/66dd4e15b9) [#42757](https://github.com/sgl-project/sglang/pull/42757) — [AMD][Docs] Add MI355X DeepSeek-V4 Pro PD recipes (#42757)
- **2026-10-06** [`209e190ee5`](https://github.com/sgl-project/sglang/commit/209e190ee5) [#41605](https://github.com/sgl-project/sglang/pull/41605) — [AMD] ci: build the miles ROCm 10 MI30X image nightly (#41605)
- **2026-10-06** [`730f1f3e5b`](https://github.com/sgl-project/sglang/commit/730f1f3e5b) [#42245](https://github.com/sgl-project/sglang/pull/42245) — [DeepSeek-V4.1] Unify mHC into one state machine and drop medium-batch fusion variants (#42245)
- **2026-10-06** [`ba94488b42`](https://github.com/sgl-project/sglang/commit/ba94488b42) [#41655](https://github.com/sgl-project/sglang/pull/41655) — [diffusion] feat: default Qwen-Image 2.1 to VAE tiling on gfx1151 (#41655)
- **2026-10-06** [`f3b5a28f43`](https://github.com/sgl-project/sglang/commit/f3b5a28f43) [#42605](https://github.com/sgl-project/sglang/pull/42605) — [AMD] M3-mxfp8 Nightly Test Update (#42605)
- **2026-10-06** [`542addad32`](https://github.com/sgl-project/sglang/commit/542addad32) [#42602](https://github.com/sgl-project/sglang/pull/42602) — [AMD] M3-MXFP4 Nightly Test (#42602)
- **2026-10-06** [`c76faa1ff2`](https://github.com/sgl-project/sglang/commit/c76faa1ff2) [#42613](https://github.com/sgl-project/sglang/pull/42613) — docs(cookbook): enable Top-K v2 for GLM-5.2 MI355X MTP (#42613)
- **2026-10-06** [`1abd356595`](https://github.com/sgl-project/sglang/commit/1abd356595) [#42552](https://github.com/sgl-project/sglang/pull/42552) — [AMD] Add engram host/device address mapping (#42552)
- **2026-10-05** [`b3f967e809`](https://github.com/sgl-project/sglang/commit/b3f967e809) [#41282](https://github.com/sgl-project/sglang/pull/41282) — Revert "Revert "[AMD][ROCm] Keep cos_sin_cache fp32 on HIP for fused QSA indexer kernel (#41282)"" (#42558)
- **2026-10-05** [`c41b2d26e5`](https://github.com/sgl-project/sglang/commit/c41b2d26e5) [#28650](https://github.com/sgl-project/sglang/pull/28650) — [diffusion][ROCm][Perf]: Set gfx942 AITER FMHA rounding mode to rtz instead of rtna (#28650)
- **2026-10-05** [`456d533e61`](https://github.com/sgl-project/sglang/commit/456d533e61) [#41282](https://github.com/sgl-project/sglang/pull/41282) — Revert "[AMD][ROCm] Keep cos_sin_cache fp32 on HIP for fused QSA indexer kernel (#41282)" (#42541)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#43098](https://github.com/sgl-project/sglang/issues/43098) | Agentic Cache Scheduling System Roadmap (Q4) | — | 2026-10-12 |
| [#43878](https://github.com/sgl-project/sglang/issues/43878) | [Feature] [diffusion] ComfyUI integrated mode: support FLUX.2 and FLUX | — | 2026-10-12 |
| [#42907](https://github.com/sgl-project/sglang/issues/42907) | [Bug] trigger_cuda_user_coredump misses the default pipe: driver creat | — | 2026-10-12 |
| [#43864](https://github.com/sgl-project/sglang/issues/43864) | [Bug] Audio request to a multimodal model without an audio tower crash | — | 2026-10-12 |
| [#43313](https://github.com/sgl-project/sglang/issues/43313) | SGLang-Diffusion Roadmap (2026 Q4) | diffusion, roadmap | 2026-10-12 |
| [#43862](https://github.com/sgl-project/sglang/issues/43862) | [Bug] PD disagg: bootstrap_room normalization diverges between the Rus | — | 2026-10-12 |
| [#43857](https://github.com/sgl-project/sglang/issues/43857) | [Bug] sglang-mm: token-layout offsets wrap at u32 for prompts expandin | — | 2026-10-12 |
| [#43699](https://github.com/sgl-project/sglang/issues/43699) | [Roadmap] Prefill-Decode Disaggregation Roadmap (2026 Q4) | PD Disaggregation | 2026-10-12 |
| [#43526](https://github.com/sgl-project/sglang/issues/43526) | [AMD][Bug] Accuracy issue with gfx942 block-FP8 linear AITER CK blocks | — | 2026-10-12 |
| [#43412](https://github.com/sgl-project/sglang/issues/43412) | Speculative decoding crashes server on first non-greedy request: flash | — | 2026-10-12 |
| [#40843](https://github.com/sgl-project/sglang/issues/40843) | [Bug] Severe repetition and degenerate loops in reasoning/output when  | — | 2026-10-12 |
| [#43765](https://github.com/sgl-project/sglang/issues/43765) | [Bug][AMD] DSV4 compact_attention_hip imports aiter's pa_decode_sparse | — | 2026-10-12 |
| [#16565](https://github.com/sgl-project/sglang/issues/16565) | [Roadmap][Feature] Support Moore Threads (MUSA) GPU | mthreads | 2026-10-12 |
| [#43731](https://github.com/sgl-project/sglang/issues/43731) | [Bug] [Diffusion] Concurrent instances: scheduler silently rebinds to  | — | 2026-10-11 |
| [#43730](https://github.com/sgl-project/sglang/issues/43730) | [Bug][ROCm] NGRAM speculative decoding on a DSA model (GLM-5.3, gfx942 | — | 2026-10-11 |
| [#38709](https://github.com/sgl-project/sglang/issues/38709) | [Bug][ROCm] --dcp-size > 1 crashes every rank on the first forward: fo | — | 2026-10-11 |
| [#38710](https://github.com/sgl-project/sglang/issues/38710) | [Bug] enable_aiter_allreduce_fusion auto-enable is commented out while | — | 2026-10-11 |
| [#40877](https://github.com/sgl-project/sglang/issues/40877) | [SM120] Field report: DeepSeek-V4.1-Flash in production on 8x RTX PRO  | — | 2026-10-11 |
| [#39499](https://github.com/sgl-project/sglang/issues/39499) | [Roadmap] SGLang dLLM Serving | — | 2026-10-11 |
| [#42473](https://github.com/sgl-project/sglang/issues/42473) | Development Roadmap (2026 Q4) | — | 2026-10-11 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 125 |
| Multimodal | 121 |
| KV Cache / Memory | 55 |
| Prefill / Decode Disaggregation | 41 |
| MoE / Expert Parallel | 37 |
| Quantization | 23 |
| Other | 20 |
| Tensor / Data Parallel | 18 |
| Triton / Kernels | 17 |
| CI / Build | 16 |
| Scheduler / Batching | 15 |
| Docs / Examples | 14 |
| Speculative Decoding | 12 |
| ROCm / AMD | 10 |
| Models | 8 |
| Serving / API | 4 |
| LoRA | 1 |

## Attention / FlashInfer  (125 commits)

- **2026-10-12** [`d88d5c325a`](https://github.com/sgl-project/sglang/commit/d88d5c325a) [#37525](https://github.com/sgl-project/sglang/pull/37525)
  Prebuild fixup_zero_kv JIT module at TRTLLM-MLA backend init (#37525)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-10-12** [`23a1f53fc3`](https://github.com/sgl-project/sglang/commit/23a1f53fc3) [#43463](https://github.com/sgl-project/sglang/pull/43463)
  [QSA] Bound the decode indexer's work by the context length (#43463)
  _Files: `python/sglang/srt/layers/attention/qsa/fused_kv.py`, `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` _+2 more__
- **2026-10-12** [`f006fb49ec`](https://github.com/sgl-project/sglang/commit/f006fb49ec) [#43308](https://github.com/sgl-project/sglang/pull/43308)
  [NPU] Stabilize HiCache and registered CI tests (#43308)
  _Files: `scripts/ci/npu/npu_ci_install_dependency.sh`, `test/manual/ascend/test_npu_piecewise_graph_prefill.py`, `test/registered/npu/basic_function/HiCache/test_npu_hicache_mla.py`, `test/registered/npu/basic_function/dp_attn/test_npu_dp_attention.py` _+4 more__
- **2026-10-12** [`b0c84d4518`](https://github.com/sgl-project/sglang/commit/b0c84d4518) [#43799](https://github.com/sgl-project/sglang/pull/43799)
  [Docs] Cookbook: refresh SemiAnalysis AgentX launches (GLM-5.2 B300, DeepSeek-V4.1 GB300) (#43799)
  _Files: `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+2 more__
- **2026-10-12** [`450837e770`](https://github.com/sgl-project/sglang/commit/450837e770) [#43802](https://github.com/sgl-project/sglang/pull/43802)
  [Docs] Update GLM-5.3-Flash playground: B300 default, CP8, EP and PD (#43802)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-10-12** [`54409c2fa0`](https://github.com/sgl-project/sglang/commit/54409c2fa0) [#38603](https://github.com/sgl-project/sglang/pull/38603)
  [BCG][DSV4-Flash][CP] Support DeepSeek V4 prefill with interleave CP and breakable CUDA graphs (#38603)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/cp/bcg.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/unit/layers/cp/test_dsv4_prefill_cp_bcg.py`_
- **2026-10-12** [`8d491fbc3e`](https://github.com/sgl-project/sglang/commit/8d491fbc3e) [#34355](https://github.com/sgl-project/sglang/pull/34355)
  [XPU] Support decode context parallelism (DCP) on Intel XPU (#34355)
  _Files: `docs/docs/advanced_features/dcp.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/hardware-platforms/xpu.mdx`, `python/sglang/srt/arg_groups/attention_hook.py` _+9 more__
- **2026-10-12** [`b6ba148384`](https://github.com/sgl-project/sglang/commit/b6ba148384) [#43711](https://github.com/sgl-project/sglang/pull/43711)
  Capture KV host transfer buffers (#43711)
  _Files: `python/sglang/srt/mem_cache/pool_host/mha.py`, `python/sglang/srt/mem_cache/pool_host/mla.py`, `test/registered/unit/mem_cache/pool_host/test_kvcacheio_asymmetric.py`, `test/registered/unit/mem_cache/test_asymmetric_mha_pool_host_unit.py` _+6 more__
- **2026-10-12** [`da4bf1ef8e`](https://github.com/sgl-project/sglang/commit/da4bf1ef8e) [#43238](https://github.com/sgl-project/sglang/pull/43238)
  [Perf] Route BF16 mixed-batch decode tails through decode attention (#43238)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-10-12** [`130e11d50e`](https://github.com/sgl-project/sglang/commit/130e11d50e) [#43494](https://github.com/sgl-project/sglang/pull/43494)
  [Deps] Bump FlashInfer to 0.7.1 (#43494)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`, `python/pyproject.toml`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/README.md` _+2 more__
- **2026-10-12** [`bf703013f2`](https://github.com/sgl-project/sglang/commit/bf703013f2) [#43762](https://github.com/sgl-project/sglang/pull/43762)
  [Test] Re-anchor the VLM flashinfer throughput floor (#43762)
  _Files: `test/registered/basic_perf/test_vlm_serving_flashinfer.py`_
- **2026-10-11** [`b0a75c8196`](https://github.com/sgl-project/sglang/commit/b0a75c8196) [#43595](https://github.com/sgl-project/sglang/pull/43595)
  Share MLA host capacity initialization (#43595)
  _Files: `python/sglang/srt/mem_cache/pool_host/base.py`, `python/sglang/srt/mem_cache/pool_host/mha.py`, `python/sglang/srt/mem_cache/pool_host/mla.py`, `test/registered/kernels/ops/kvcache/test_mxfp8_host_allocation.py` _+1 more__
- **2026-10-11** [`047405f534`](https://github.com/sgl-project/sglang/commit/047405f534) [#41933](https://github.com/sgl-project/sglang/pull/41933)
  [qwen 3.8 next] Fuse QSA prefill KV gathering and dtype conversion (#41933)
  _Files: `python/sglang/srt/layers/attention/qsa/sparse_attn.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `test/registered/kernels/ops/attention/qsa/test_qsa.py`_
- **2026-10-11** [`22d63f5e43`](https://github.com/sgl-project/sglang/commit/22d63f5e43) [#43383](https://github.com/sgl-project/sglang/pull/43383)
  [AMD]Qwen add Sparse attention to capturing hip graphs (#43383)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-10-11** [`260551ebe9`](https://github.com/sgl-project/sglang/commit/260551ebe9) [#42857](https://github.com/sgl-project/sglang/pull/42857)
  [KDA] Support Helion MTP verification and harden prefill, decode (#42857)
  _Files: `python/sglang/kernels/ops/attention/helion/kda_verify.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_helion.py`, `test/registered/kernels/ops/attention/test_kda_helion.py` _+1 more__
- **2026-10-11** [`65e6bb6be7`](https://github.com/sgl-project/sglang/commit/65e6bb6be7) [#43332](https://github.com/sgl-project/sglang/pull/43332)
  [GDN] Fix CuTe DSL decode to read the [N, HV, V, K] state layout (#43332)
  _Files: `python/sglang/kernels/ops/attention/cutedsl_gdn.py`, `test/registered/kernels/ops/attention/test_cutedsl_gdn.py`_
- **2026-10-11** [`b931b2c8bd`](https://github.com/sgl-project/sglang/commit/b931b2c8bd) [#43634](https://github.com/sgl-project/sglang/pull/43634)
  [diffusion] perf: run the attention section eager under torch.compile for MiniMax-H3 (#43634)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_dit_contract.py`_
- **2026-10-11** [`d45ef0f2d2`](https://github.com/sgl-project/sglang/commit/d45ef0f2d2) [#43586](https://github.com/sgl-project/sglang/pull/43586)
  [diffusion] perf: keep Qwen-Image-2.1 and Ulysses graphs whole (#43586)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image21.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py` _+1 more__
- **2026-10-11** [`d60e0c8570`](https://github.com/sgl-project/sglang/commit/d60e0c8570) [#37907](https://github.com/sgl-project/sglang/pull/37907)
  [diffusion] Support LLaDA-Image BF16 generation and editing (#37907)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/__init__.py`, `python/sglang/multimodal_gen/configs/models/dits/llada_image.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/__init__.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/llada_image.py` _+24 more__
- **2026-10-11** [`156d54e56c`](https://github.com/sgl-project/sglang/commit/156d54e56c) [#38217](https://github.com/sgl-project/sglang/pull/38217)
  fix: wait for HiCache load-back before hybrid MLA KV reads (#38217)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/mem_cache/test_full_loc_fast_path.py`_
- **2026-10-11** [`9336681310`](https://github.com/sgl-project/sglang/commit/9336681310) [#42957](https://github.com/sgl-project/sglang/pull/42957)
  [DSA] Support TileLang FP8 KV cache on CUDA (#42957)
  _Files: `python/sglang/kernels/ops/attention/dsa/tilelang_kernel.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` _+2 more__
- **2026-10-10** [`3b16eeedce`](https://github.com/sgl-project/sglang/commit/3b16eeedce) [#43459](https://github.com/sgl-project/sglang/pull/43459)
  [Refactor] Declare pipeline neighbours from a shared declaration function (#43459)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/layer_boundary/__init__.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py` _+10 more__
- **2026-10-10** [`3b717c0f13`](https://github.com/sgl-project/sglang/commit/3b717c0f13) [#43458](https://github.com/sgl-project/sglang/pull/43458)
  [Refactor] Decide an exit's fixed facts when the stage is built (#43458)
  _Files: `python/sglang/srt/arg_groups/layernorm_sp_hook.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py`, `python/sglang/srt/layers/layer_boundary/exit.py` _+12 more__
- **2026-10-10** [`d2c597c8db`](https://github.com/sgl-project/sglang/commit/d2c597c8db) [#43456](https://github.com/sgl-project/sglang/pull/43456)
  [Refactor] Decide input-scattered eligibility and stage rejections in one place (#43456)
  _Files: `python/sglang/srt/layers/layer_boundary/adapters/attention.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/factories.py`, `python/sglang/srt/layers/layer_boundary/layout.py` _+1 more__
- **2026-10-10** [`8bd7f2d178`](https://github.com/sgl-project/sglang/commit/8bd7f2d178) [#43453](https://github.com/sgl-project/sglang/pull/43453)
  [Refactor] Record what a bound stage path does instead of reading it back (#43453)
  _Files: `python/sglang/srt/layers/layer_boundary/adapters/attention.py`, `python/sglang/srt/layers/layer_boundary/boundary.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py` _+7 more__
- **2026-10-10** [`f61163b4b0`](https://github.com/sgl-project/sglang/commit/f61163b4b0) [#43554](https://github.com/sgl-project/sglang/pull/43554)
  [Docs] Let the Qwen3 B300 recipe use the default attention backend (#43554)
  _Files: `docs/src/snippets/autoregressive/qwen3-deployment.jsx`_
- **2026-10-10** [`72657f7ca5`](https://github.com/sgl-project/sglang/commit/72657f7ca5) [#43521](https://github.com/sgl-project/sglang/pull/43521)
  [diffusion] perf: pipeline every USPAttention Ulysses path's exchange over the copy engine (#43521)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/environment_variables.mdx`, `docs/docs/sglang-diffusion/parallelism.mdx`, `python/sglang/multimodal_gen/envs.py` _+6 more__
- **2026-10-10** [`16be9df25f`](https://github.com/sgl-project/sglang/commit/16be9df25f) [#43470](https://github.com/sgl-project/sglang/pull/43470)
  [CI] Remove the GLM-5.3-Flash PTX KDA prefill nightly test (#43470)
  _Files: `test/registered/e2e/models/test_glm53_flash_kda_ptx_prefill_blackwell.py`_
- **2026-10-10** [`0aa580f904`](https://github.com/sgl-project/sglang/commit/0aa580f904) [#43478](https://github.com/sgl-project/sglang/pull/43478)
  [Dsv4.1] Add DeepSeek V4.1 DSPARK TP and DP EP accuracy coverage (#43478)
  _Files: `test/registered/e2e/models/test_deepseek_v41_flash_gb300.py`_
- **2026-10-10** [`37678784c6`](https://github.com/sgl-project/sglang/commit/37678784c6) [#42019](https://github.com/sgl-project/sglang/pull/42019)
  [Gemma4][Attention] Enable Gemma4 FA4 on SM90 with head-dim 512 support (#42019)
  _Files: `python/sglang/kernels/ops/attention/flash_attention.py`, `python/sglang/kernels/ops/attention/flash_attention_v4.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/flash_fwd_sm90.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py` _+7 more__
- **2026-10-10** [`465253ef52`](https://github.com/sgl-project/sglang/commit/465253ef52) [#43444](https://github.com/sgl-project/sglang/pull/43444)
  [Scheduler] Fix the deterministic-inference hang when a prefill chunk is shorter than its alignment (#43444)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/kernels/ops/attention/extend_attention.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/triton_backend.py` _+3 more__
- **2026-10-10** [`78218194ad`](https://github.com/sgl-project/sglang/commit/78218194ad) [#42683](https://github.com/sgl-project/sglang/pull/42683)
  perf(kda): rebalance MTP verify precompute and state synchronization (#42683)
  _Files: `python/sglang/kernels/ops/attention/kda_decode_mtp.py`, `test/registered/kernels/ops/attention/test_kda_decode_mtp.py`_
- **2026-10-10** [`16423cb6d2`](https://github.com/sgl-project/sglang/commit/16423cb6d2) [#43000](https://github.com/sgl-project/sglang/pull/43000)
  [sgl-router] Serve DeepSeek-V4.1 Flash through sglang-processor (#43000)
  _Files: `.agents/skills/processor-model-parity/SKILL.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/server/metrics.rs`, `experimental/sgl-router/src/tokenizer/chat_formatter.rs` _+24 more__
- **2026-10-09** [`6d8ddaf1d7`](https://github.com/sgl-project/sglang/commit/6d8ddaf1d7) [#42614](https://github.com/sgl-project/sglang/pull/42614)
  [AMD] MiniMax-M3 indexer CP: packed scoring for EAGLE verify rows (#42614)
  _Files: `python/sglang/kernels/ops/attention/minimax_sparse/decode/indexer_cp.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` _+1 more__
- **2026-10-09** [`fbf8d730fd`](https://github.com/sgl-project/sglang/commit/fbf8d730fd) [#41845](https://github.com/sgl-project/sglang/pull/41845)
  [Fix] MiniMax-M3: default to the breakable prefill CUDA graph (#41845)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/radix_attention.py`, `test/registered/unit/layers/test_radix_attention.py`_
- **2026-10-09** [`72eab59bf6`](https://github.com/sgl-project/sglang/commit/72eab59bf6) [#42845](https://github.com/sgl-project/sglang/pull/42845)
  [GLM-5.3-Flash] Enable breakable prefill CUDA graph by default (#42845)
  _Files: `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/arg_groups/resolution_hooks.py`, `test/registered/e2e/models/test_glm53_flash_b200.py`_
- **2026-10-09** [`1203eb9181`](https://github.com/sgl-project/sglang/commit/1203eb9181) [#43164](https://github.com/sgl-project/sglang/pull/43164)
  [diffusion] perf: pipeline MiniMax-H3's Ulysses exchange against attention over the copy engine (#43164)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a_multi.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py` _+5 more__
- **2026-10-09** [`d5c3ae9752`](https://github.com/sgl-project/sglang/commit/d5c3ae9752) [#41030](https://github.com/sgl-project/sglang/pull/41030)
  [AMD] Eliminate remaining gfx95 FP8 scale relayout copies (#41030)
  _Files: `python/sglang/srt/layers/layer_boundary/residual/add_norm.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha_rocm.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` _+1 more__
- **2026-10-09** [`d511e6bd1d`](https://github.com/sgl-project/sglang/commit/d511e6bd1d) [#42999](https://github.com/sgl-project/sglang/pull/42999)
  [sgl-router] Parse tool calls when serving chat through /generate (#42999)
  _Files: `.agents/skills/processor-model-parity/SKILL.md`, `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/server/routes/chat/preparation.rs` _+21 more__
- **2026-10-09** [`67d063f63b`](https://github.com/sgl-project/sglang/commit/67d063f63b) [#35310](https://github.com/sgl-project/sglang/pull/35310)
  [diffusion] feat: allow per-role attention backend override (#35310)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/configs/attention_roles.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py` _+13 more__
- **2026-10-09** [`3805d78796`](https://github.com/sgl-project/sglang/commit/3805d78796) [#42998](https://github.com/sgl-project/sglang/pull/42998)
  [sgl-router] Serve /v1/chat/completions through /generate, with reasoning parsing (#42998)
  _Files: `.agents/skills/processor-model-parity/SKILL.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/server/routes/chat/preparation.rs`, `experimental/sgl-router/src/tokenizer/mod.rs` _+23 more__
- **2026-10-09** [`5eca4d8caf`](https://github.com/sgl-project/sglang/commit/5eca4d8caf) [#42570](https://github.com/sgl-project/sglang/pull/42570)
  [AMD] Set maxseq length limit for DSV4.1 BCG metadata buffers (#42570)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-10-09** [`14e3414513`](https://github.com/sgl-project/sglang/commit/14e3414513) [#43235](https://github.com/sgl-project/sglang/pull/43235)
  [Docs] Add Clef cookbook with selectable Clef Flash variant (#43235)
  _Files: `docs/cards/logos/cloudflare.png`, `docs/cookbook/autoregressive/Cloudflare/clef.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-10-09** [`dc0b394471`](https://github.com/sgl-project/sglang/commit/dc0b394471) [#42936](https://github.com/sgl-project/sglang/pull/42936)
  [Refactor] Remove Kimi K3's own layer communication and let the consumer set an FFN's exit (#42936)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py`, `python/sglang/srt/layers/layer_boundary/factories.py` _+12 more__
- **2026-10-09** [`305ad5503d`](https://github.com/sgl-project/sglang/commit/305ad5503d) [#42898](https://github.com/sgl-project/sglang/pull/42898)
  [Refactor] Run Kimi K3's fused collectives through stage boundaries (#42898)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/attn_residual.py`, `python/sglang/srt/layers/layer_boundary/__init__.py`, `python/sglang/srt/layers/layer_boundary/adapters/attention.py` _+12 more__
- **2026-10-09** [`2b469040d2`](https://github.com/sgl-project/sglang/commit/2b469040d2) [#42897](https://github.com/sgl-project/sglang/pull/42897)
  [Refactor] Support attention-TP dense FFNs and unpadded batches on stage boundaries (#42897)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/layer_boundary/adapters/attention.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py` _+10 more__
- **2026-10-09** [`b9ae3d1a65`](https://github.com/sgl-project/sglang/commit/b9ae3d1a65) [#42896](https://github.com/sgl-project/sglang/pull/42896)
  [Fix] Run attention on a padded extend batch's real rows (#42896)
  _Files: `python/sglang/kernels/ops/attention/flash_attention_v4.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/layers/communication/k3_sp_collective.py`, `python/sglang/srt/layers/radix_attention.py` _+5 more__
- **2026-10-09** [`48a6c0a5d0`](https://github.com/sgl-project/sglang/commit/48a6c0a5d0) [#42892](https://github.com/sgl-project/sglang/pull/42892)
  [Fix] Return an FFN's output to the attention rows at a pipeline handoff (#42892)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py`, `python/sglang/srt/layers/layer_boundary/exit.py` _+4 more__
- **2026-10-09** [`b2402ccad6`](https://github.com/sgl-project/sglang/commit/b2402ccad6) [#42891](https://github.com/sgl-project/sglang/pull/42891)
  [Fix] Merge DeepSeek-V4 two-batch-overlap microbatches without a residual (#42891)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/e2e/models/test_deepseek_v4_flash_fp4_b200_tbo.py`_
- **2026-10-09** [`b130f8af02`](https://github.com/sgl-project/sglang/commit/b130f8af02) [#42997](https://github.com/sgl-project/sglang/pull/42997)
  [sgl-router] Serve /v1/completions through /generate, with the shared OpenAI layer (#42997)
  _Files: `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/policies/dp_rank.rs`, `experimental/sgl-router/src/server/app.rs` _+27 more__
- **2026-10-09** [`217980566a`](https://github.com/sgl-project/sglang/commit/217980566a) [#33000](https://github.com/sgl-project/sglang/pull/33000)
  fix(fa4): isolate sheared-bias workspaces by CUDA stream (#33000)
  _Files: `python/sglang/kernels/ops/attention/flash_attn/cute/__init__.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py`, `test/registered/kernels/ops/attention/test_flash_attention_4.py`_
- **2026-10-09** [`bd2d73daa5`](https://github.com/sgl-project/sglang/commit/bd2d73daa5) [#42721](https://github.com/sgl-project/sglang/pull/42721)
  [model] support Clef and Clef-Flash decision models on /v1/systemone (#42721)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/serving_decisions.py` _+16 more__
- **2026-10-09** [`51f7ea84c7`](https://github.com/sgl-project/sglang/commit/51f7ea84c7) [#42772](https://github.com/sgl-project/sglang/pull/42772)
  [AMD] Keep MiniMax decode-score tile at 128 tokens off gfx950 (#42772)
  _Files: `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`_
- **2026-10-09** [`1fc6b8962c`](https://github.com/sgl-project/sglang/commit/1fc6b8962c) [#43083](https://github.com/sgl-project/sglang/pull/43083)
  [Docs] Cookbook: AgentX launches for Qwen3.5 / Qwen3.8-Flash-Next; refresh GLM-5.2, DeepSeek-V4, DeepSeek-V4.1 (#43083)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`, `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx` _+5 more__
- **2026-10-09** [`e46aaaa789`](https://github.com/sgl-project/sglang/commit/e46aaaa789) [#40588](https://github.com/sgl-project/sglang/pull/40588)
  [diffusion] feat: accept strided row views in the packed QKV all-to-all (#40588)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/test/unit/test_usp_attention_replicated_prefix.py`, `python/sglang/multimodal_gen/test/unit/test_usp_packed_qkv_a2a.py`_
- **2026-10-09** [`9a1aeacc3b`](https://github.com/sgl-project/sglang/commit/9a1aeacc3b) [#41105](https://github.com/sgl-project/sglang/pull/41105)
  [GLM-5.3-Flash] Capture the KDA extend in breakable prefill CUDA graphs (#41105)
  _Files: `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/kda.py`, `python/sglang/kernels/ops/attention/fla/kda_prefill_graph_track.py`, `python/sglang/kernels/ops/attention/helion/kda_prefill.py` _+11 more__
- **2026-10-09** [`3ba90f1b52`](https://github.com/sgl-project/sglang/commit/3ba90f1b52) [#42666](https://github.com/sgl-project/sglang/pull/42666)
  [rust] Update Dynamo frontend crates to latest compatible releases (#42666)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/src/tokenizer/deepseek.rs`, `experimental/sgl-router/tests/component/tokenizer/kimi.rs` _+15 more__
- **2026-10-09** [`33bffcd490`](https://github.com/sgl-project/sglang/commit/33bffcd490) [#42044](https://github.com/sgl-project/sglang/pull/42044)
  [CP] GLM-5.3-Flash Prefill CP implemented on layer boundaries (#42044)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `python/sglang/srt/arg_groups/cp_tp_group_sharing_hook.py`, `python/sglang/srt/configs/glm5_next.py`, `python/sglang/srt/layers/attention/dsa/dsa_backend_kpool.py` _+16 more__
- **2026-10-09** [`8e19db19b0`](https://github.com/sgl-project/sglang/commit/8e19db19b0) [#43246](https://github.com/sgl-project/sglang/pull/43246)
  [KDA] Default safe-gate Blackwell prefill to FlashInfer (#43246)
  _Files: `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/utils.py`, `test/registered/attention/unittests/kda/README.md` _+1 more__
- **2026-10-09** [`fedab5537b`](https://github.com/sgl-project/sglang/commit/fedab5537b) [#41406](https://github.com/sgl-project/sglang/pull/41406)
  [XPU] Enable ring attention on XPUAttentionBackend (#41406)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/xpu_backend.py`_
- **2026-10-09** [`51686cf8e7`](https://github.com/sgl-project/sglang/commit/51686cf8e7) [#41857](https://github.com/sgl-project/sglang/pull/41857)
  [XPU] split Intel nightly into kernel-main and kernel-wheel jobs (#41857)
  _Files: `.github/workflows/nightly-test-intel.yml`, `.github/workflows/xpu-ci-job-monitor.yml`, `test/registered/debug_utils/test_dumper.py`, `test/registered/e2e/xpu/test_dflash_intel_xpu.py` _+23 more__
- **2026-10-09** [`265efe5e01`](https://github.com/sgl-project/sglang/commit/265efe5e01) [#43199](https://github.com/sgl-project/sglang/pull/43199)
  [MemCache] Serve disabled full-attention models with `UnifiedRadixCache` (#43199)
  _Files: `python/sglang/srt/mem_cache/registry.py`, `test/registered/unit/mem_cache/test_registry.py`_
- **2026-10-09** [`fc3385d530`](https://github.com/sgl-project/sglang/commit/fc3385d530) [#41400](https://github.com/sgl-project/sglang/pull/41400)
  feat(kda): integrate FlashInfer prefill checkpoints (#41400)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_kda_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashinfer.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashinfer_prefill.py` _+10 more__
- **2026-10-09** [`1e77db3215`](https://github.com/sgl-project/sglang/commit/1e77db3215) [#43227](https://github.com/sgl-project/sglang/pull/43227)
  [Perf] Avoid gate copies in gated RMSNorm (#43227)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_norm_gate.py`, `test/registered/kernels/ops/attention/test_fused_norm_gate_strided.py`_
- **2026-10-08** [`2b94cb4eb5`](https://github.com/sgl-project/sglang/commit/2b94cb4eb5) [#43159](https://github.com/sgl-project/sglang/pull/43159)
  docs(cookbook): add Qwen3.8 GB300 long-context recipe (#43159)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-flash-next.jsx`_
- **2026-10-08** [`2abb761639`](https://github.com/sgl-project/sglang/commit/2abb761639) [#43180](https://github.com/sgl-project/sglang/pull/43180)
  [metrics] Count per-rank DP attention pairs and their imbalance (#43180)
  _Files: `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/observability/metrics_collector.py`, `test/registered/observability/test_metrics.py` _+2 more__
- **2026-10-08** [`e902207a4e`](https://github.com/sgl-project/sglang/commit/e902207a4e) [#43012](https://github.com/sgl-project/sglang/pull/43012)
  [Speculative] Support block verification for the DFlash family (#43012)
  _Files: `docs/docs/advanced_features/speculative_decoding.mdx`, `python/sglang/kernels/ops/speculative/dspark/dspark_accept.py`, `python/sglang/srt/arg_groups/fields/spec.py`, `python/sglang/srt/arg_groups/speculative_hook.py` _+5 more__
- **2026-10-08** [`d1ba943016`](https://github.com/sgl-project/sglang/commit/d1ba943016) [#42782](https://github.com/sgl-project/sglang/pull/42782)
  [Model] Add support for EmbeddingGemma 2 (#42782)
  _Files: `docs/cookbook/autoregressive/Google/EmbeddingGemma2.mdx`, `docs/docs.json`, `python/sglang/kernels/ops/attention/extend_attention.py`, `python/sglang/srt/arg_groups/model_hook.py` _+11 more__
- **2026-10-08** [`b193ef382a`](https://github.com/sgl-project/sglang/commit/b193ef382a) [#43195](https://github.com/sgl-project/sglang/pull/43195)
  [CI] Clean some unnecessary DSV4 tests (#43195)
  _Files: `test/registered/cp/test_deepseek_v4_flash_fp4_b200_cp.py`, `test/registered/e2e/models/test_deepseek_v4_flash_fp4_b200.py`, `test/registered/e2e/models/test_deepseek_v4_flash_fp4_b200_trtllm.py`, `test/registered/e2e/models/test_deepseek_v4_flash_fp4_h200.py` _+4 more__
- **2026-10-08** [`93f2acf614`](https://github.com/sgl-project/sglang/commit/93f2acf614) [#43187](https://github.com/sgl-project/sglang/pull/43187)
  [Metrics] Use widely supported bucket boundaries for the DP attention imbalance ratio (#43187)
  _Files: `python/sglang/srt/observability/metrics_collector.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`_
- **2026-10-08** [`075fd8fa0b`](https://github.com/sgl-project/sglang/commit/075fd8fa0b) [#43192](https://github.com/sgl-project/sglang/pull/43192)
  [Mamba] Describe the track snapshot dtype by its kernel instead of fp32 (#43192)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`_
- **2026-10-08** [`e3c5719713`](https://github.com/sgl-project/sglang/commit/e3c5719713) [#43179](https://github.com/sgl-project/sglang/pull/43179)
  [DFlash] Build the attention QKV projection through an overridable hook (#43179)
  _Files: `python/sglang/srt/models/dflash.py`_
- **2026-10-08** [`344b8a863b`](https://github.com/sgl-project/sglang/commit/344b8a863b) [#43013](https://github.com/sgl-project/sglang/pull/43013)
  [Perf] Fuse short-convolution checkpoint tracking metadata (#43013)
  _Files: `python/sglang/kernels/ops/mamba/__init__.py`, `python/sglang/kernels/ops/mamba/sconv_tracking.py`, `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `test/registered/kernels/ops/mamba/test_sconv_tracking.py`_
- **2026-10-08** [`46ad9eb439`](https://github.com/sgl-project/sglang/commit/46ad9eb439) [#43101](https://github.com/sgl-project/sglang/pull/43101)
  Fix K-only host buffer cleanup (#43101)
  _Files: `python/sglang/srt/mem_cache/pool_host/mha.py`, `test/registered/hicache/test_k_only_host_release.py`_
- **2026-10-08** [`4ab4d90d78`](https://github.com/sgl-project/sglang/commit/4ab4d90d78) [#34537](https://github.com/sgl-project/sglang/pull/34537)
  [AMD][DCP 3/N] add aiter asm for kimi k3 target verify (#34537)
  _Files: `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/attention/test_aiter_gluon_h12_fp8.py`_
- **2026-10-08** [`11b1fb21de`](https://github.com/sgl-project/sglang/commit/11b1fb21de) [#38841](https://github.com/sgl-project/sglang/pull/38841)
  [MiniMax-M3] Decode: paged K/V tile loads and a tiny GEMM for the router projection (#38841)
  _Files: `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/models/minimax_m3.py`, `test/registered/kernels/ops/attention/test_minimax_sparse_decode_paged_tile.py`_
- **2026-10-08** [`6e6ccb26f2`](https://github.com/sgl-project/sglang/commit/6e6ccb26f2) [#38615](https://github.com/sgl-project/sglang/pull/38615)
  [MiniMax-M3] Instantiate the decode block top-k in register buckets (#38615)
  _Files: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `python/sglang/kernels/ops/attention/minimax_decode_topk.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py` _+1 more__
- **2026-10-08** [`45abea0269`](https://github.com/sgl-project/sglang/commit/45abea0269) [#42664](https://github.com/sgl-project/sglang/pull/42664)
  [rust-processor] DeepSeek-V4 parity with SGLang, plus a reusable parity harness and skill (#42664)
  _Files: `.agents/skills/processor-model-parity/SKILL.md`, `.claude/rules/modify-component-must-read.md`, `docker/renderer.Dockerfile`, `rust/Cargo.lock` _+16 more__
- **2026-10-08** [`7b9c42cf49`](https://github.com/sgl-project/sglang/commit/7b9c42cf49) [#43081](https://github.com/sgl-project/sglang/pull/43081)
  [CI] Remove the unregistered chunked-prefill tests under test/manual (#43081)
  _Files: `python/sglang/test/scripted_runtime_chunked_helpers.py`, `test/manual/chunked_prefill/__init__.py`, `test/manual/chunked_prefill/test_e2e_disagg.py`, `test/manual/chunked_prefill/test_e2e_dp_attention.py` _+30 more__
- **2026-10-08** [`b3e6c87be3`](https://github.com/sgl-project/sglang/commit/b3e6c87be3) [#42753](https://github.com/sgl-project/sglang/pull/42753)
  [Refactor] Translate each KV loc once per iteration (#42753)
  _Files: `python/sglang/kernels/ops/kvcache/kv_read_table.py`, `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py` _+93 more__
- **2026-10-08** [`508ddc859a`](https://github.com/sgl-project/sglang/commit/508ddc859a) [#40492](https://github.com/sgl-project/sglang/pull/40492)
  [unified-memory] Admit DFLASH and DSPARK with fused draft KV (#40492)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/layout/fused_draft.py`, `python/sglang/srt/model_executor/model_runner_components/spec_aux_hidden_state.py` _+11 more__
- **2026-10-08** [`c2d491e38b`](https://github.com/sgl-project/sglang/commit/c2d491e38b) [#40491](https://github.com/sgl-project/sglang/pull/40491)
  [unified-memory] Admit EAGLE/EAGLE3 onto fused draft KV, on mamba-MHA and MLA hosts (#40491)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/layout/fused_draft.py` _+14 more__
- **2026-10-08** [`8b80808366`](https://github.com/sgl-project/sglang/commit/8b80808366) [#37628](https://github.com/sgl-project/sglang/pull/37628)
  [unified-memory] Fuse the draft model's KV into the target's page envelope (mechanism) (#37628)
  _Files: `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py` _+24 more__
- **2026-10-08** [`08d30f2300`](https://github.com/sgl-project/sglang/commit/08d30f2300) [#37627](https://github.com/sgl-project/sglang/pull/37627)
  [unified-memory] Speculative decoding on the unified memory pool: translate every read and write path (#37627)
  _Files: `python/sglang/kernels/ops/kvcache/kv_read_table.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` _+13 more__
- **2026-10-08** [`4f320fb85a`](https://github.com/sgl-project/sglang/commit/4f320fb85a) [#37662](https://github.com/sgl-project/sglang/pull/37662)
  [diffusion] perf: FastH3 8-Step V2 native support, native Blackwell VSA and batched H3 VAE decode (#37662)
  _Files: `.pre-commit-config.yaml`, `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `docs/docs/sglang-diffusion/fused_kernels.mdx` _+39 more__
- **2026-10-08** [`b7b2975b57`](https://github.com/sgl-project/sglang/commit/b7b2975b57) [#42793](https://github.com/sgl-project/sglang/pull/42793)
  fix(dsa): align FA3 metadata with unpadded queries (#42793)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`_
- **2026-10-08** [`7327fb225f`](https://github.com/sgl-project/sglang/commit/7327fb225f) [#42114](https://github.com/sgl-project/sglang/pull/42114)
  [DSV4] Guard V4.1 indexer SM100 check on non-CUDA devices (#42114)
  _Files: `python/sglang/srt/layers/attention/dsv4/v41_indexer/__init__.py`_
- **2026-10-08** [`99463390f8`](https://github.com/sgl-project/sglang/commit/99463390f8) [#40978](https://github.com/sgl-project/sglang/pull/40978)
  [Fix] MiMo-V2: accept checkpoints with the split attention layout (#40978)
  _Files: `python/sglang/srt/configs/model_config.py`_
- **2026-10-08** [`c892301ff7`](https://github.com/sgl-project/sglang/commit/c892301ff7) [#35594](https://github.com/sgl-project/sglang/pull/35594)
  [Platform] Thread vendor KV pool classes through the in-tree builders; add PlatformCapabilities (#35594)
  _Files: `docs/docs/hardware-platforms/plugin.mdx`, `python/sglang/kernels/ops/kvcache/mla_buffer.py`, `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/compilation/backend.py` _+42 more__
- **2026-10-08** [`21fa2251a0`](https://github.com/sgl-project/sglang/commit/21fa2251a0) [#42848](https://github.com/sgl-project/sglang/pull/42848)
  [diffusion] refactor: share sigma schedules and causal cross-attention (#42848)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/causal_wanvideo.py`, `python/sglang/multimodal_gen/runtime/models/dits/lingbot_world.py`, `python/sglang/multimodal_gen/runtime/models/dits/longlive2.py`, `python/sglang/multimodal_gen/runtime/models/schedulers/scheduling_flow_match_euler_discrete.py` _+6 more__
- **2026-10-08** [`5cb7fb886c`](https://github.com/sgl-project/sglang/commit/5cb7fb886c) [#42645](https://github.com/sgl-project/sglang/pull/42645)
  [Feature] support pplx-decider-v1.1 and update the pplx-decider cookbooks (#42645)
  _Files: `docs/cookbook/autoregressive/Perplexity/PPLX-Decider-v1-27B.mdx`, `docs/cookbook/autoregressive/Perplexity/PPLX-Decider-v1.1-27B.mdx`, `docs/cookbook/autoregressive/Perplexity/pplx-decider-v1-27b.mdx`, `docs/cookbook/autoregressive/intro.mdx` _+11 more__
- **2026-10-07** [`7760d5264a`](https://github.com/sgl-project/sglang/commit/7760d5264a) [#42590](https://github.com/sgl-project/sglang/pull/42590)
  [Refactor] Use destination layouts for model checkpoint mappings (#42590)
  _Files: `python/sglang/srt/layers/vocab_parallel_embedding.py`, `python/sglang/srt/models/apertus.py`, `python/sglang/srt/models/arcee.py`, `python/sglang/srt/models/dots3_common/modeling.py` _+21 more__
- **2026-10-07** [`dec5d9d6fc`](https://github.com/sgl-project/sglang/commit/dec5d9d6fc) [#42586](https://github.com/sgl-project/sglang/pull/42586)
  [Refactor] Let vision encoders select their parallel group (#42586)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/qwen2_5vl.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen3vl_vision.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen_vl_vision.py`, `python/sglang/multimodal_gen/test/unit/test_qwen2_5vl_generation.py` _+14 more__
- **2026-10-07** [`79ef49cb6b`](https://github.com/sgl-project/sglang/commit/79ef49cb6b) [#43015](https://github.com/sgl-project/sglang/pull/43015)
  [Docs] GLM-5.3-Flash: measured MI355X MXFP4 agentic recipe (#43015)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-10-07** [`44d10eab5e`](https://github.com/sgl-project/sglang/commit/44d10eab5e) [#42931](https://github.com/sgl-project/sglang/pull/42931)
  [GLM-V] Shard the vision tower over the attention-TP group under DP attention (#42931)
  _Files: `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/models/glm_ocr.py`_
- **2026-10-07** [`49d7d60dfa`](https://github.com/sgl-project/sglang/commit/49d7d60dfa) [#42858](https://github.com/sgl-project/sglang/pull/42858)
  [AMD][diffusion] VAE attention to the math SDPA backend on gfx1250 (#42858)
  _Files: `python/sglang/multimodal_gen/runtime/platforms/rocm.py`_
- **2026-10-07** [`ba77d30256`](https://github.com/sgl-project/sglang/commit/ba77d30256) [#42926](https://github.com/sgl-project/sglang/pull/42926)
  [FA4] Keep stream last in the SM100 MLA kernel so disk-cached objects load (#42926)
  _Files: `python/sglang/kernels/ops/attention/flash_attn/cute/flash_fwd_mla_sm100.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py`_
- **2026-10-07** [`1c42ad3679`](https://github.com/sgl-project/sglang/commit/1c42ad3679) [#42747](https://github.com/sgl-project/sglang/pull/42747)
  [ROCm] Skip the tilelang act_quant in the DSA indexer on gfx1250 (#42747)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-10-07** [`43b4abd857`](https://github.com/sgl-project/sglang/commit/43b4abd857) [#41529](https://github.com/sgl-project/sglang/pull/41529)
  [diffusion] fix: validate SageAttention 2 head sizes without overriding component policy (#41529)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/sage_attn.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py`, `python/sglang/multimodal_gen/test/unit/test_cuda_attention_backend.py`_
- **2026-10-07** [`9e26600f3a`](https://github.com/sgl-project/sglang/commit/9e26600f3a) [#42671](https://github.com/sgl-project/sglang/pull/42671)
  [DSA] Clarify pooled-page naming and ownership (#42671)
  _Files: `python/sglang/kernels/ops/attention/dsa/index_buf_accessor.py`, `python/sglang/kernels/ops/attention/dsa/kpool_topk_transform.py`, `python/sglang/kernels/ops/attention/dsa_kpool_metadata/decode.py`, `python/sglang/kernels/ops/attention/dsa_kpool_metadata/draft_extend.py` _+26 more__
- **2026-10-07** [`012cd3858b`](https://github.com/sgl-project/sglang/commit/012cd3858b) [#42611](https://github.com/sgl-project/sglang/pull/42611)
  [Fix] Make the fused KDA beta sigmoid bit-identical to torch.sigmoid (#42611)
  _Files: `python/sglang/kernels/ops/attention/fla/kda.py`, `test/registered/kernels/ops/attention/test_kda_gate_beta_cumsum.py`_
- **2026-10-07** [`660b17e8dc`](https://github.com/sgl-project/sglang/commit/660b17e8dc) [#42635](https://github.com/sgl-project/sglang/pull/42635)
  [AMD] Let AITER unified verify run without host seq_lens (#42635)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/unit/layers/attention/test_aiter_verify_metadata.py`_
- **2026-10-07** [`e13933c4fd`](https://github.com/sgl-project/sglang/commit/e13933c4fd) [#41670](https://github.com/sgl-project/sglang/pull/41670)
  [diffusion] docs: add gfx1151 Strix Halo serving guidance (#41670)
  _Files: `docs/docs/hardware-platforms/amd_gpu.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `docs/docs/sglang-diffusion/installation.mdx`_
- **2026-10-06** [`264d1c2015`](https://github.com/sgl-project/sglang/commit/264d1c2015) [#42651](https://github.com/sgl-project/sglang/pull/42651)
  Back the DFlash-family draft KV pool to the post-capture token count (#42651)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/kv_pool_runtime.py`, `python/sglang/srt/model_executor/model_runner_components/spec_aux_hidden_state.py`, `test/registered/unit/model_executor/test_kv_canary_headroom.py`_
- **2026-10-06** [`4506927635`](https://github.com/sgl-project/sglang/commit/4506927635) [#42755](https://github.com/sgl-project/sglang/pull/42755)
  [Metrics] Add per-rank DP attention imbalance metrics (#42755)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py` _+5 more__
- **2026-10-06** [`49bafb58cd`](https://github.com/sgl-project/sglang/commit/49bafb58cd) [#42659](https://github.com/sgl-project/sglang/pull/42659)
  perf(mla): use native SATFINITE FP8 conversion in MLA KV/Q preparation (#42659)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/set_mla_kv_concat_q.cuh`_
- **2026-10-06** [`45db430530`](https://github.com/sgl-project/sglang/commit/45db430530) [#42750](https://github.com/sgl-project/sglang/pull/42750)
  [DSA] Fix pooled page table refresh for target verify CUDA graph replay (#42750)
  _Files: `python/sglang/srt/layers/attention/dsa/kpool_plan.py`_
- **2026-10-06** [`33ce0943e9`](https://github.com/sgl-project/sglang/commit/33ce0943e9) [#42682](https://github.com/sgl-project/sglang/pull/42682)
  [Bugfix] Guard merge_state sgl_kernel import on non-CUDA platforms (#42682)
  _Files: `python/sglang/srt/layers/attention/merge_state.py`_
- **2026-10-06** [`e446698cdd`](https://github.com/sgl-project/sglang/commit/e446698cdd) [#32779](https://github.com/sgl-project/sglang/pull/32779)
  [SM120&90] Add CUDA fused Triton sparse-MLA prefill backend for DSA (#32779)
  _Files: `docs/docs/advanced_features/attention_backend.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/kernels/ops/attention/dsa/triton_sparse_mla_prefill.py`, `python/sglang/kernels/ops/attention/flash_mla_sm120.py` _+7 more__
- **2026-10-06** [`1e1bdeedbb`](https://github.com/sgl-project/sglang/commit/1e1bdeedbb) [#42489](https://github.com/sgl-project/sglang/pull/42489)
  [Perf] Improve GLM-5.3-Flash DFlash decoding on B300 (#42489)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_norm_gate.py`, `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/dsa/dsa_backend_kpool.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_kpool.py` _+4 more__
- **2026-10-06** [`620c76f25d`](https://github.com/sgl-project/sglang/commit/620c76f25d) [#41603](https://github.com/sgl-project/sglang/pull/41603)
  [DSV4.1] Add opt-in TRT-LLM sparse attention support (#41603)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c1.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/c2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/kv_layout.cuh`, `python/sglang/kernels/ops/attention/dsv4/elementwise.py` _+12 more__
- **2026-10-06** [`62af5f56a5`](https://github.com/sgl-project/sglang/commit/62af5f56a5) [#42571](https://github.com/sgl-project/sglang/pull/42571)
  [CI] Drop the redundant and broken tc_piecewise tests (#42571)
  _Files: `test/registered/cuda_graph/breakable/test_bcg_with_speculative_decoding_extra.py`, `test/registered/cuda_graph/piecewise/test_pcg_with_speculative_decoding.py`, `test/registered/cuda_graph/piecewise/test_pcg_with_speculative_decoding_dflash.py`, `test/registered/cuda_graph/piecewise/test_pcg_with_speculative_decoding_extra.py` _+1 more__
- **2026-10-06** [`18ec2ecce3`](https://github.com/sgl-project/sglang/commit/18ec2ecce3) [#42285](https://github.com/sgl-project/sglang/pull/42285)
  [Refactor][TCPCG] Relocate shared graph tensor and DSA head-gate helpers (1/9) (#42285)
  _Files: `python/sglang/srt/compilation/cuda_piecewise_backend.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/dsa_prefill_cuda_graph.py`, `python/sglang/srt/layers/attention/dsa/head_gate.py` _+3 more__
- **2026-10-05** [`61ba98443d`](https://github.com/sgl-project/sglang/commit/61ba98443d) [#42178](https://github.com/sgl-project/sglang/pull/42178)
  [DSA] k-pool: 256-token logical page so index page id = logical page id (#42178)
  _Files: `python/sglang/kernels/ops/attention/dsa/index_buf_accessor.py`, `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py`, `python/sglang/srt/layers/attention/dsa/dsa_backend_kpool.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_kpool.py` _+13 more__
- **2026-10-05** [`c765f8818a`](https://github.com/sgl-project/sglang/commit/c765f8818a) [#41737](https://github.com/sgl-project/sglang/pull/41737)
  [DFlash2] Keep the greedy selector walk in range for all-NaN score rows (#41737)
  _Files: `python/sglang/kernels/ops/speculative/dflash.py`, `test/registered/kernels/ops/speculative/test_lilicorr_cuda.py`_
- **2026-10-05** [`26a1377c50`](https://github.com/sgl-project/sglang/commit/26a1377c50) [#42057](https://github.com/sgl-project/sglang/pull/42057)
  [Spec] LiLiCorr: named head MLPs and quantized head linears (#42057)
  _Files: `python/sglang/srt/models/dflash.py`, `python/sglang/srt/models/lilicorr.py`, `python/sglang/srt/speculative/lilicorr_utils.py`_
- **2026-10-05** [`284cda01fb`](https://github.com/sgl-project/sglang/commit/284cda01fb) [#41906](https://github.com/sgl-project/sglang/pull/41906)
  [diffusion] optimization: fuse the video VAE decoder's RMSNorm and QK RoPE for MiniMax-H3 (#41906)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/h3_vae_fused_norm.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/attention.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/vae_vit.py` _+3 more__
- **2026-10-05** [`55dcf3254f`](https://github.com/sgl-project/sglang/commit/55dcf3254f) [#41656](https://github.com/sgl-project/sglang/pull/41656)
  Fix XQA draft extend with FP8 KV cache in trtllm_mha (#41656)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `test/registered/attention/test_trtllm_mha_graph_metadata.py`_
- **2026-10-05** [`abd6c374c7`](https://github.com/sgl-project/sglang/commit/abd6c374c7) [#42101](https://github.com/sgl-project/sglang/pull/42101)
  [Perf] Optimize MiMo local audio attention on Hopper (#42101)
  _Files: `python/sglang/kernels/ops/attention/mimo_local_attention.py`, `python/sglang/srt/models/mimo_audio.py`_
- **2026-10-05** [`9f7d38ffd3`](https://github.com/sgl-project/sglang/commit/9f7d38ffd3) [#33855](https://github.com/sgl-project/sglang/pull/33855)
  [diffusion] attention: Allow disabling sequence masking in SP (#33855)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`_
- **2026-10-05** [`c41b2d26e5`](https://github.com/sgl-project/sglang/commit/c41b2d26e5) [#28650](https://github.com/sgl-project/sglang/pull/28650)
  [diffusion][ROCm][Perf]: Set gfx942 AITER FMHA rounding mode to rtz instead of rtna (#28650)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py`_
- **2026-10-05** [`cafb37a10d`](https://github.com/sgl-project/sglang/commit/cafb37a10d) [#40785](https://github.com/sgl-project/sglang/pull/40785)
  [JIT] Fuse FP8 KV-cache quantization into the prefix-valid commit kernel (#40785)
  _Files: `python/sglang/kernels/ops/kvcache/cache_move.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/test/kernels/prefix_valid.py` _+2 more__
- **2026-10-05** [`520d6d0229`](https://github.com/sgl-project/sglang/commit/520d6d0229) [#41659](https://github.com/sgl-project/sglang/pull/41659)
  [DSv4.1] Prefill indexer: raw selection, row-pair schedule ids, no host syncs (#41659)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/__init__.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/dense_blocks.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/full_topk.py` _+10 more__
- **2026-10-05** [`f385390be5`](https://github.com/sgl-project/sglang/commit/f385390be5) [#42506](https://github.com/sgl-project/sglang/pull/42506)
  [Refactor] Simplify GDN, vision RoPE and MLA kernel dispatch (#42506)
  _Files: `python/sglang/kernels/ops/attention/set_mla_kv_concat_q.py`, `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/kernels/ops/attention/vision_rope.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py` _+2 more__
- **2026-10-05** [`f70e8c68fc`](https://github.com/sgl-project/sglang/commit/f70e8c68fc) [#42273](https://github.com/sgl-project/sglang/pull/42273)
  [Dsv4.1] Bounded replay with sparse mla path (#42273)
  _Files: `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `test/registered/kernels/ops/attention/test_flashmla_sched_meta.py` _+1 more__

## Multimodal  (121 commits)

- **2026-10-12** [`1a553927b0`](https://github.com/sgl-project/sglang/commit/1a553927b0) [#37426](https://github.com/sgl-project/sglang/pull/37426)
  [CI][Diffusion] Add caching for npu GT images in CI (#37426)
  _Files: `.github/workflows/pr-test-npu.yml`, `scripts/ci/utils/diffusion/prefetch_consistency_gt.py`_
- **2026-10-12** [`279f1fad90`](https://github.com/sgl-project/sglang/commit/279f1fad90) [#43756](https://github.com/sgl-project/sglang/pull/43756)
  [diffusion] chore: bind worker CPUs to the GPU's NUMA node when memory policy is not permitted (#43756)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/test/unit/test_gpu_worker_cpu_threads.py`, `python/sglang/srt/utils/numa_utils.py`, `test/registered/utils/test_numa_utils.py`_
- **2026-10-12** [`d1357bf87b`](https://github.com/sgl-project/sglang/commit/d1357bf87b) [#43210](https://github.com/sgl-project/sglang/pull/43210)
  [NPU] Diffusion CI fixes (#43210)
  _Files: `.github/workflows/_npu-analyze-failure.yml`, `.github/workflows/pr-test-npu.yml`, `proto/sglang/api/v1/generate.proto`, `python/sglang/api/v1/api_types.py` _+11 more__
- **2026-10-12** [`208df292e5`](https://github.com/sgl-project/sglang/commit/208df292e5) [#41940](https://github.com/sgl-project/sglang/pull/41940)
  [diffusion][xpu] FLUX.2: enable the bit-exact Triton SwiGLU on XPU (#41940)
  _Files: `python/sglang/kernels/ops/diffusion/activation/silu_mul_bitexact.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py`_
- **2026-10-12** [`6ac8602e8d`](https://github.com/sgl-project/sglang/commit/6ac8602e8d) [#43747](https://github.com/sgl-project/sglang/pull/43747)
  [CI] Fix TestQwenImageModulationCache after Qwen-Image modulation sharding (#43747)
  _Files: `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-10-12** [`d0a098b2e0`](https://github.com/sgl-project/sglang/commit/d0a098b2e0) [#43684](https://github.com/sgl-project/sglang/pull/43684)
  [diffusion] perf: split and batch LTX-2.3 one-stage guidance passes under CFG parallel (#43684)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/encode_while_decoding.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/joy_echo/setup.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/decoding_av.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py` _+2 more__
- **2026-10-12** [`a954b395e6`](https://github.com/sgl-project/sglang/commit/a954b395e6) [#43683](https://github.com/sgl-project/sglang/pull/43683)
  [diffusion] perf: layerwise offload for the LTX-2.5 Gemma-4 text encoder (#43683)
  _Files: `docs/cookbook/diffusion/LTX/LTX2.5.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/models/encoders/gemma_4_unified.py`, `python/sglang/multimodal_gen/test/unit/test_gemma4_unified_layerwise_offload.py`_
- **2026-10-12** [`a67228aa43`](https://github.com/sgl-project/sglang/commit/a67228aa43) [#43691](https://github.com/sgl-project/sglang/pull/43691)
  [diffusion] fix: shard Qwen-Image adaLN modulation and text FFN under TP (#43691)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image.mdx`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image_joint_qkv.py`_
- **2026-10-11** [`97bfa5cc53`](https://github.com/sgl-project/sglang/commit/97bfa5cc53) [#43690](https://github.com/sgl-project/sglang/pull/43690)
  [diffusion] fix: select VSA-H3 for FastH3 when no transformer backend is given (#43690)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py` _+1 more__
- **2026-10-11** [`11bfd868ac`](https://github.com/sgl-project/sglang/commit/11bfd868ac) [#43656](https://github.com/sgl-project/sglang/pull/43656)
  [diffusion] perf: encode LTX video/audio through the shared bounded MP4 path (#43656)
  _Files: `docs/docs/sglang-diffusion/performance-optimization.mdx`, `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/runtime/models/vaes/ltx_2_vae.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/decoding.py` _+4 more__
- **2026-10-11** [`a1500b10e3`](https://github.com/sgl-project/sglang/commit/a1500b10e3) [#43084](https://github.com/sgl-project/sglang/pull/43084)
  [diffusion] Don't report video jobs completed after their outputs are deleted (#43084)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/test/unit/test_video_job_lifecycle.py`_
- **2026-10-11** [`3458c94fad`](https://github.com/sgl-project/sglang/commit/3458c94fad) [#43492](https://github.com/sgl-project/sglang/pull/43492)
  [diffusion] comfyui: consolidate executor conditioning-cache fixes (#43492)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/adapter.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/base.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/comfyui_mode.py` _+2 more__
- **2026-10-11** [`638330d975`](https://github.com/sgl-project/sglang/commit/638330d975) [#43490](https://github.com/sgl-project/sglang/pull/43490)
  [diffusion] comfyui: consolidate FluxAdapter correctness fixes (#43490)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/flux.py`, `python/sglang/multimodal_gen/runtime/loader/comfyui_checkpoints/flux.py`, `python/sglang/multimodal_gen/test/unit/test_comfyui_adapters.py`, `python/sglang/multimodal_gen/test/unit/test_comfyui_profile.py`_
- **2026-10-11** [`b21826e609`](https://github.com/sgl-project/sglang/commit/b21826e609) [#43633](https://github.com/sgl-project/sglang/pull/43633)
  [diffusion] fix: replay Qwen-Image-2.1 BCG graphs across prompt lengths (#43633)
  _Files: `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/model_padders/qwen_image21.py`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/prompt_padding.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image21.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/qwen_image21.py` _+2 more__
- **2026-10-11** [`b237afa547`](https://github.com/sgl-project/sglang/commit/b237afa547) [#43632](https://github.com/sgl-project/sglang/pull/43632)
  [diffusion] fix: Qwen-Image BCG prompt padding misses every graph and attends the pad (#43632)
  _Files: `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/model_padders/qwen_image.py`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/prompt_padding.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_bcg_padding.py`_
- **2026-10-11** [`b3a65efe7e`](https://github.com/sgl-project/sglang/commit/b3a65efe7e) [#43577](https://github.com/sgl-project/sglang/pull/43577)
  [diffusion] perf: keep Cosmos3's fused kernels in the graph (#43577)
  _Files: `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/test/unit/test_regional_torch_compile.py`_
- **2026-10-11** [`e4b423256e`](https://github.com/sgl-project/sglang/commit/e4b423256e) [#43631](https://github.com/sgl-project/sglang/pull/43631)
  [diffusion] fix: serve whole graphs after offload-during-compile (#43631)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_offload_during_compile.py`_
- **2026-10-11** [`d7ed5b56f5`](https://github.com/sgl-project/sglang/commit/d7ed5b56f5) [#43590](https://github.com/sgl-project/sglang/pull/43590)
  [diffusion] fix: keep the overlay probe from stalling cached startup (#43590)
  _Files: `python/sglang/multimodal_gen/runtime/utils/hf_diffusers_utils.py`, `python/sglang/multimodal_gen/test/unit/test_hf_diffusers_utils.py`_
- **2026-10-11** [`5730345717`](https://github.com/sgl-project/sglang/commit/5730345717) [#43495](https://github.com/sgl-project/sglang/pull/43495)
  [diffusion] comfyui: fail early instead of silently dropping features in SGLD integrated mode (#43495)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/model_patcher.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/preflight.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/adapter.py` _+9 more__
- **2026-10-11** [`d1313dd5fe`](https://github.com/sgl-project/sglang/commit/d1313dd5fe) [#43601](https://github.com/sgl-project/sglang/pull/43601)
  [diffusion] fix: skip inductor's saved multi-kernel pick for torch.compile (Z-Image warm starts crash or hang) (#43601)
  _Files: `python/sglang/multimodal_gen/runtime/utils/torch_compile.py`, `python/sglang/multimodal_gen/test/unit/test_torch_compile_inductor_config.py`_
- **2026-10-11** [`3022989bad`](https://github.com/sgl-project/sglang/commit/3022989bad) [#43574](https://github.com/sgl-project/sglang/pull/43574)
  [diffusion] CI: skip the LTX-2 RMSNorm-modulation guard test off the CUDA platform (#43574)
  _Files: `python/sglang/multimodal_gen/test/unit/test_ltx2_rmsnorm_modulate_fallback.py`_
- **2026-10-11** [`65386cb95a`](https://github.com/sgl-project/sglang/commit/65386cb95a) [#43501](https://github.com/sgl-project/sglang/pull/43501)
  [diffusion] perf: add the dynamic LoRA delta inside the second GEMM (#43501)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/test/unit/test_lora_dynamic_delta_in_gemm.py`_
- **2026-10-11** [`e328c7ecbd`](https://github.com/sgl-project/sglang/commit/e328c7ecbd) [#43576](https://github.com/sgl-project/sglang/pull/43576)
  [diffusion] fix: skip QKV packing while layers are offloaded (#43576)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/qwen_image21.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py`_
- **2026-10-11** [`7373665085`](https://github.com/sgl-project/sglang/commit/7373665085) [#43584](https://github.com/sgl-project/sglang/pull/43584)
  [diffusion] fix: keep exported buffers out of expandable segments for IPC all-to-all(#43584)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a_multi.py`, `python/sglang/multimodal_gen/test/unit/test_ipc_a2a_lifecycle.py`_
- **2026-10-11** [`5e872557cb`](https://github.com/sgl-project/sglang/commit/5e872557cb) [#43602](https://github.com/sgl-project/sglang/pull/43602)
  [diffusion] feat: keep the TP all-reduce inside the graph (#43602)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/group_coordinator.py`, `python/sglang/multimodal_gen/test/unit/test_group_coordinator_compiled_all_reduce.py`_
- **2026-10-11** [`664e4c6499`](https://github.com/sgl-project/sglang/commit/664e4c6499) [#43568](https://github.com/sgl-project/sglang/pull/43568)
  [diffusion] feat: warn instead of disabling on unvalidated models for BCG(#43568)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/runner.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py` _+3 more__
- **2026-10-11** [`23764b1242`](https://github.com/sgl-project/sglang/commit/23764b1242) [#43565](https://github.com/sgl-project/sglang/pull/43565)
  [diffusion] feat: bind each GPU worker to its GPU's NUMA node (#43565)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_gpu_worker_cpu_threads.py` _+1 more__
- **2026-10-11** [`9933cf5437`](https://github.com/sgl-project/sglang/commit/9933cf5437) [#43575](https://github.com/sgl-project/sglang/pull/43575)
  [diffusion] feat: declare regional compile regions for flux (#43575)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/flux.py`, `python/sglang/multimodal_gen/test/unit/test_regional_torch_compile.py`_
- **2026-10-11** [`68e1a3dbb1`](https://github.com/sgl-project/sglang/commit/68e1a3dbb1) [#43573](https://github.com/sgl-project/sglang/pull/43573)
  [diffusion] fix: accept request-level profiling on the image API (#43573)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/test/unit/test_openai_image_api.py`_
- **2026-10-10** [`616178a596`](https://github.com/sgl-project/sglang/commit/616178a596) [#35524](https://github.com/sgl-project/sglang/pull/35524)
  [Responses] Fix max_output_tokens overestimate on multimodal requests (#35524)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py`, `test/registered/unit/entrypoints/openai/test_responses_protocol.py`_
- **2026-10-10** [`a510340aeb`](https://github.com/sgl-project/sglang/commit/a510340aeb) [#43508](https://github.com/sgl-project/sglang/pull/43508)
  [diffusion] perf: run head_dim-128 QK-norm + RoPE two rows per warp for every RoPE layout (#43508)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_rope.cuh`, `test/registered/kernels/ops/diffusion/test_qknorm_rope_out_of_place.py`_
- **2026-10-10** [`d8c5eca3ac`](https://github.com/sgl-project/sglang/commit/d8c5eca3ac) [#43385](https://github.com/sgl-project/sglang/pull/43385)
  [diffusion] fix: keep a LoRA unmerged under merge_mode auto when merging would round its update away (#43385)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py` _+1 more__
- **2026-10-10** [`3831e7e091`](https://github.com/sgl-project/sglang/commit/3831e7e091) [#35755](https://github.com/sgl-project/sglang/pull/35755)
  [diffusion] Z-Image: autotune the shared transformer block at both token scales (#35755)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/base.py`, `python/sglang/multimodal_gen/configs/models/dits/zimage.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/runtime/utils/torch_compile.py`_
- **2026-10-10** [`aa79087017`](https://github.com/sgl-project/sglang/commit/aa79087017) [#34978](https://github.com/sgl-project/sglang/pull/34978)
  [diffusion] fix: fail MiniMax-H3 quality="high" closed on substituted DiT weights (#34978)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_admission.py`_
- **2026-10-10** [`ccae3b3639`](https://github.com/sgl-project/sglang/commit/ccae3b3639) [#43373](https://github.com/sgl-project/sglang/pull/43373)
  [diffusion] perf: pipeline MiniMax-H3's Ulysses exchange against cuDNN SDPA on Blackwell (#43373)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`_
- **2026-10-10** [`436d73ddda`](https://github.com/sgl-project/sglang/commit/436d73ddda) [#36311](https://github.com/sgl-project/sglang/pull/36311)
  [diffusion] model: support HunyuanImage-3.0-Instruct (#36311)
  _Files: `docs/cookbook/diffusion/Tencent/HunyuanImage3.mdx`, `docs/cookbook/diffusion/intro.mdx`, `docs/docs.json`, `docs/src/snippets/configs/tencent/hunyuan-image3.jsx` _+31 more__
- **2026-10-10** [`77ba54f7df`](https://github.com/sgl-project/sglang/commit/77ba54f7df) [#43380](https://github.com/sgl-project/sglang/pull/43380)
  [diffusion] docs: add Wan-Animate-2 cookbook command picker (#43380)
  _Files: `docs/cookbook/diffusion/LTX/LTX2.5.mdx`, `docs/cookbook/diffusion/Wan/Wan-Animate-2.mdx`, `docs/docs.json`, `docs/scripts/tests/wan-animate-2-config.test.mjs` _+1 more__
- **2026-10-10** [`cde16aa64d`](https://github.com/sgl-project/sglang/commit/cde16aa64d) [#43391](https://github.com/sgl-project/sglang/pull/43391)
  [diffusion] model: support Qwen-Image 2.1 Turbo and checkpoint sampling grids (#43391)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/configs/Qwen/qwen-image-2.1.jsx`, `docs/src/snippets/diffusion/model-catalog.jsx` _+5 more__
- **2026-10-10** [`66e6b68d82`](https://github.com/sgl-project/sglang/commit/66e6b68d82) [#43178](https://github.com/sgl-project/sglang/pull/43178)
  [diffusion] comfyui: report the real runtime import error (#43178)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/base.py`, `python/sglang/multimodal_gen/test/unit/test_comfyui_generator.py`_
- **2026-10-10** [`ff3aa58f11`](https://github.com/sgl-project/sglang/commit/ff3aa58f11) [#43337](https://github.com/sgl-project/sglang/pull/43337)
  [diffusion] perf: run MiniMax-H3's QK-norm + RoPE two rows per war while bit-identical (#43337)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_rope.cuh`, `python/sglang/kernels/ops/diffusion/rope/qknorm_rope_jit.py`, `test/registered/kernels/benchmark/diffusion/bench_qknorm_rope.py`, `test/registered/kernels/ops/diffusion/test_qknorm_rope_out_of_place.py`_
- **2026-10-10** [`32f34e898b`](https://github.com/sgl-project/sglang/commit/32f34e898b) [#38671](https://github.com/sgl-project/sglang/pull/38671)
  [diffusion] fix: honor requested inference step count for MiniMax H3(#38671)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/configs/sample/minimax_h3.py`, `python/sglang/multimodal_gen/configs/sample/minimax_h3_vdn.py`, `python/sglang/multimodal_gen/envs.py` _+18 more__
- **2026-10-10** [`bd7c7971ba`](https://github.com/sgl-project/sglang/commit/bd7c7971ba) [#43361](https://github.com/sgl-project/sglang/pull/43361)
  [diffusion] perf: move MiniMax-H3's pipelined Ulysses copies off the SMs (#43361)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a_multi.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/single_test_file/test_ipc_a2a_multi_gpu.py`_
- **2026-10-09** [`f6e3444b2e`](https://github.com/sgl-project/sglang/commit/f6e3444b2e) [#41620](https://github.com/sgl-project/sglang/pull/41620)
  ci: diffusion-only option for the runner utilization report (#41620)
  _Files: `.github/workflows/runner-utilization.yml`, `scripts/ci/utils/runner_utilization_report.py`_
- **2026-10-09** [`76ccf0850c`](https://github.com/sgl-project/sglang/commit/76ccf0850c) [#42422](https://github.com/sgl-project/sglang/pull/42422)
  [diffusion] fix: fix TeaCache CFG state lifecycle and skip boundaries (#42422)
  _Files: `python/sglang/multimodal_gen/configs/sample/teacache.py`, `python/sglang/multimodal_gen/runtime/cache/teacache.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`, `python/sglang/multimodal_gen/test/test_utils.py` _+2 more__
- **2026-10-09** [`121aa8dcc7`](https://github.com/sgl-project/sglang/commit/121aa8dcc7) [#43327](https://github.com/sgl-project/sglang/pull/43327)
  [diffusion] perf: fuse MiniMax-H3's RMSNorm and indexed AdaLN under quality lossless (#43327)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/rmsnorm_scale_shift_triton.py`, `python/sglang/kernels/ops/diffusion/sites/minimax_h3_norm_modulate_site.py` _+3 more__
- **2026-10-09** [`f1e0472fcc`](https://github.com/sgl-project/sglang/commit/f1e0472fcc) [#42941](https://github.com/sgl-project/sglang/pull/42941)
  [diffusion] model: support Wan-Animate-2 (#42941)
  _Files: `docs/cookbook/diffusion/Wan/Wan-Animate-2.mdx`, `docs/docs.json`, `docs/docs/sglang-diffusion/api/openai_api.mdx`, `docs/src/snippets/diffusion/model-catalog.jsx` _+28 more__
- **2026-10-09** [`59eb71a831`](https://github.com/sgl-project/sglang/commit/59eb71a831) [#23772](https://github.com/sgl-project/sglang/pull/23772)
  [diffusion] fix: align SGLD CFG combine formula with diffusers Z-Image (#23772)
  _Files: `docs/cookbook/diffusion/Z-Image/Z-Image-Turbo.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/zimage.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/configs/sample/zimage.py` _+3 more__
- **2026-10-09** [`516fd1c1b5`](https://github.com/sgl-project/sglang/commit/516fd1c1b5) [#43267](https://github.com/sgl-project/sglang/pull/43267)
  [diffusion] perf: tile MiniMax-H3's indexed modulation kernels by 2048 columns (#43267)
  _Files: `python/sglang/kernels/ops/diffusion/modulate/indexed_modulation_triton.py`, `test/registered/kernels/ops/diffusion/test_indexed_modulation.py`_
- **2026-10-09** [`7cfecbef56`](https://github.com/sgl-project/sglang/commit/7cfecbef56) [#41492](https://github.com/sgl-project/sglang/pull/41492)
  [diffusion][model] Add native SANA-Video 2.0 support (#41492)
  _Files: `docs/cookbook/diffusion/SANA-Video/SANA-Video.mdx`, `docs/src/snippets/diffusion/model-catalog.jsx`, `python/sglang/multimodal_gen/configs/models/dits/sana_video2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/sana_video2.py` _+8 more__
- **2026-10-09** [`d677848968`](https://github.com/sgl-project/sglang/commit/d677848968) [#41706](https://github.com/sgl-project/sglang/pull/41706)
  [diffusion] fix: fix CFG normalization to use per-sample norm instead of batch-flattened norm (#41706)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/cfg_policy.py`, `python/sglang/multimodal_gen/test/unit/test_cfg_policy.py`_
- **2026-10-09** [`3ab142adc4`](https://github.com/sgl-project/sglang/commit/3ab142adc4) [#36470](https://github.com/sgl-project/sglang/pull/36470)
  [diffusion] feat: enable breakable CUDA graphs for FLUX.2 Klein (#36470)
  _Files: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`_
- **2026-10-09** [`b922f5ca20`](https://github.com/sgl-project/sglang/commit/b922f5ca20) [#43269](https://github.com/sgl-project/sglang/pull/43269)
  [diffusion] fix: share the IPC all-to-all transport between AllToAll4D and USP (#43269)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a.py`, `python/sglang/multimodal_gen/test/single_test_file/test_ipc_a2a_2_gpu.py`, `python/sglang/multimodal_gen/test/unit/test_ipc_a2a_lifecycle.py`_
- **2026-10-09** [`17b2f35ae7`](https://github.com/sgl-project/sglang/commit/17b2f35ae7) [#43064](https://github.com/sgl-project/sglang/pull/43064)
  [diffusion] refactor: remove unused helpers and write-only state (#43064)
- **2026-10-09** [`ee4e2f7818`](https://github.com/sgl-project/sglang/commit/ee4e2f7818) [#28021](https://github.com/sgl-project/sglang/pull/28021)
  [diffusion] optimization: enable channels_last_3d for Cosmos3 VAE (#28021)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/test/test_utils.py`, `python/sglang/multimodal_gen/test/unit/test_vae_loader.py`_
- **2026-10-09** [`45ad463c87`](https://github.com/sgl-project/sglang/commit/45ad463c87) [#42899](https://github.com/sgl-project/sglang/pull/42899)
  [diffusion] refactor: deduplicate UniPC solvers and Gemma3 shard loading (#42899)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/gemma_3.py`, `python/sglang/multimodal_gen/runtime/models/schedulers/scheduling_flow_unipc_multistep.py`, `python/sglang/multimodal_gen/runtime/models/schedulers/scheduling_helios.py`, `python/sglang/multimodal_gen/runtime/models/schedulers/scheduling_unipc_multistep.py` _+3 more__
- **2026-10-09** [`37ae292e6f`](https://github.com/sgl-project/sglang/commit/37ae292e6f) [#43134](https://github.com/sgl-project/sglang/pull/43134)
  [diffusion] fix: skip LTX-2 SP masks only for globally unpadded sequences (#43134)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/ltx_2.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/schedule_batch.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/joy_echo/denoising.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py` _+1 more__
- **2026-10-09** [`33e7b4cc4b`](https://github.com/sgl-project/sglang/commit/33e7b4cc4b) [#43117](https://github.com/sgl-project/sglang/pull/43117)
  [diffusion] perf: decode plain base64 MiniMax-H3 materials without a per-character loop (#43117)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/material_io.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_media.py`_
- **2026-10-09** [`5d8e98b7fd`](https://github.com/sgl-project/sglang/commit/5d8e98b7fd) [#41885](https://github.com/sgl-project/sglang/pull/41885)
  [XPU][Diffusion] Plain-torch scale-shift for inductor (#41885)
  _Files: `python/sglang/multimodal_gen/runtime/layers/elementwise.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`_
- **2026-10-09** [`6e7beace14`](https://github.com/sgl-project/sglang/commit/6e7beace14) [#43140](https://github.com/sgl-project/sglang/pull/43140)
  [diffusion] fix: fix int32 offset overflow in the Ulysses packed-QKV pack kernel (#43140)
  _Files: `python/sglang/kernels/ops/diffusion/layout/ulysses_qkv_triton.py`, `test/registered/kernels/ops/diffusion/test_layout.py`_
- **2026-10-09** [`df1e4f3f2b`](https://github.com/sgl-project/sglang/commit/df1e4f3f2b) [#42980](https://github.com/sgl-project/sglang/pull/42980)
  [diffusion] refactor: share SANA-WM refiner block computation (#42980)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/sana_wm/refiner.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/sana_wm/streaming_refiner.py`_
- **2026-10-09** [`86624f14eb`](https://github.com/sgl-project/sglang/commit/86624f14eb) [#43143](https://github.com/sgl-project/sglang/pull/43143)
  [Rust] Pass the media item fps hint to multimodal processors (#43143)
  _Files: `rust/sglang-server/src/lib.rs`, `rust/sglang-server/src/message/multimodal.rs`, `rust/sglang-server/src/message/request.rs`, `rust/sglang-server/src/message/wire.rs` _+1 more__
- **2026-10-08** [`3030e31ff8`](https://github.com/sgl-project/sglang/commit/3030e31ff8) [#42903](https://github.com/sgl-project/sglang/pull/42903)
  [diffusion] refactor: deduplicate request extraction and ComfyUI test helpers (#42903)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/test/passthrough.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/test/test_flux_pipeline.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/test/test_qwen_image_edit_pipeline.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/test/test_qwen_image_pipeline.py` _+10 more__
- **2026-10-08** [`7dd512b0e8`](https://github.com/sgl-project/sglang/commit/7dd512b0e8) [#43002](https://github.com/sgl-project/sglang/pull/43002)
  [diffusion] refactor: deduplicate FLUX positions and RoPE application (#43002)
  _Files: `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/base.py`, `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/mrope.py`, `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/utils.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux.py` _+1 more__
- **2026-10-08** [`5c5f593110`](https://github.com/sgl-project/sglang/commit/5c5f593110) [#42841](https://github.com/sgl-project/sglang/pull/42841)
  [diffusion] refactor: share KL VAE encode/decode and tiling operations (#42841)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/autoencoder.py`, `python/sglang/multimodal_gen/runtime/models/vaes/autoencoder_kl.py`, `python/sglang/multimodal_gen/runtime/models/vaes/autoencoder_kl_flux2.py`, `python/sglang/multimodal_gen/test/unit/test_autoencoder_kl_shared.py`_
- **2026-10-08** [`74308cf1d6`](https://github.com/sgl-project/sglang/commit/74308cf1d6) [#40765](https://github.com/sgl-project/sglang/pull/40765)
  [diffusion] fix: wait for multimodal process teardown (#40765)
  _Files: `python/sglang/multimodal_gen/runtime/utils/process.py`, `python/sglang/multimodal_gen/test/unit/test_process.py`_
- **2026-10-08** [`57e9ff5403`](https://github.com/sgl-project/sglang/commit/57e9ff5403) [#42967](https://github.com/sgl-project/sglang/pull/42967)
  [diffusion] refactor: share timestep retrieval across pipeline stages (#42967)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/diffusion_scheduler_utils.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/hunyuan3d/shape.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/qwen_image_layered.py`, `python/sglang/multimodal_gen/test/unit/test_pi05_runtime_helpers.py`_
- **2026-10-08** [`e7530a3a26`](https://github.com/sgl-project/sglang/commit/e7530a3a26) [#34494](https://github.com/sgl-project/sglang/pull/34494)
  [diffusion] fix: fix forward multimodal token type IDs in image encoding (#34494)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/image_encoding.py`, `python/sglang/multimodal_gen/test/unit/test_image_encoding_stage.py`_
- **2026-10-08** [`b0d7254fbc`](https://github.com/sgl-project/sglang/commit/b0d7254fbc) [#42986](https://github.com/sgl-project/sglang/pull/42986)
  [diffusion] CI: rebase LTX H100 timing references on recent CI runs (#42986)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`_
- **2026-10-08** [`28c08b02c3`](https://github.com/sgl-project/sglang/commit/28c08b02c3) [#42983](https://github.com/sgl-project/sglang/pull/42983)
  [diffusion] refactor: deduplicate MOVA initialization (#42983)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/mova_audio_dit.py`, `python/sglang/multimodal_gen/runtime/models/dits/mova_video_dit.py`_
- **2026-10-08** [`243f3dc35f`](https://github.com/sgl-project/sglang/commit/243f3dc35f) [#42860](https://github.com/sgl-project/sglang/pull/42860)
  [diffusion] refactor: deduplicate Qwen-VL inputs and component accuracy suites (#42860)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/qwen2_5vl.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen3vl.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen_vl.py`, `python/sglang/multimodal_gen/test/single_test_file/component_accuracy/suite.py` _+3 more__
- **2026-10-08** [`b91919ffe2`](https://github.com/sgl-project/sglang/commit/b91919ffe2) [#42794](https://github.com/sgl-project/sglang/pull/42794)
  [XPU][diffusion] Re-baseline Wan2.1-T2V-1.3B TextEncodingStage on B60 (#42794)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines/xpu_b60.json`_
- **2026-10-08** [`287b8b793f`](https://github.com/sgl-project/sglang/commit/287b8b793f) [#42866](https://github.com/sgl-project/sglang/pull/42866)
  [diffusion] refactor: deduplicate VAE resampling and LTX tiling (#42866)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/autoencoder_kl_qwenimage21.py`, `python/sglang/multimodal_gen/runtime/models/vaes/ltx_2_vae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/resample.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py` _+2 more__
- **2026-10-08** [`1e2f524726`](https://github.com/sgl-project/sglang/commit/1e2f524726) [#42988](https://github.com/sgl-project/sglang/pull/42988)
  [diffusion] refactor: share stacked encoder weight loading (#42988)
  _Files: `python/sglang/multimodal_gen/runtime/loader/weight_utils.py`, `python/sglang/multimodal_gen/runtime/models/encoders/llama.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen3.py`, `python/sglang/multimodal_gen/runtime/models/encoders/t5.py` _+1 more__
- **2026-10-08** [`d52ea5ee90`](https://github.com/sgl-project/sglang/commit/d52ea5ee90) [#42990](https://github.com/sgl-project/sglang/pull/42990)
  [diffusion] refactor: deduplicate realtime transport and LingBot tests (#42990)
  _Files: `python/sglang/multimodal_gen/test/unit/realtime/test_lingbot_causal_denoising.py`, `python/sglang/multimodal_gen/test/unit/realtime/test_realtime_output_transport.py`_
- **2026-10-08** [`9101e895ea`](https://github.com/sgl-project/sglang/commit/9101e895ea) [#41819](https://github.com/sgl-project/sglang/pull/41819)
  [diffusion] feat: encode the MP4 while the VAE decodes (MiniMax-H3, Wan) (#41819)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/runtime/models/vaes/common.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py` _+8 more__
- **2026-10-07** [`0b635266d4`](https://github.com/sgl-project/sglang/commit/0b635266d4) [#42958](https://github.com/sgl-project/sglang/pull/42958)
  [diffusion] CI: warm up CI cases at the request's quality level (#42958)
  _Files: `python/sglang/multimodal_gen/test/server/testcase_configs.py`, `python/sglang/multimodal_gen/test/unit/test_cfg_parallel_warmup.py`_
- **2026-10-07** [`d9a0f1cb34`](https://github.com/sgl-project/sglang/commit/d9a0f1cb34) [#41917](https://github.com/sgl-project/sglang/pull/41917)
  [diffusion] fix: fix hybrid SP+TP for I2V models   (#41917)
  _Files: `.github/workflows/pr-test-multimodal-gen.yml`, `python/sglang/multimodal_gen/runtime/layers/parallel_conv.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py`, `python/sglang/multimodal_gen/test/single_test_file/test_wan_vae_parallel_groups_4_gpu.py`_
- **2026-10-07** [`492dbd0807`](https://github.com/sgl-project/sglang/commit/492dbd0807) [#42706](https://github.com/sgl-project/sglang/pull/42706)
  [CI] keep diffusion-only kernels and tests out of the srt stages (#42706)
  _Files: `.github/workflows/_pr-test-check-changes.yml`_
- **2026-10-07** [`c389cbaf99`](https://github.com/sgl-project/sglang/commit/c389cbaf99) [#42859](https://github.com/sgl-project/sglang/pull/42859)
  [AMD][diffusion] Route bf16 fuse_scale_shift to the native fallback on gfx1250 (#42859)
  _Files: `python/sglang/kernels/ops/diffusion/modulate/scale_shift_triton.py`_
- **2026-10-07** [`11972e5207`](https://github.com/sgl-project/sglang/commit/11972e5207) [#42784](https://github.com/sgl-project/sglang/pull/42784)
  [deps] bump transformers to 5.19.0 (#42784)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `docker/rocm.Dockerfile`, `python/pyproject.toml`, `python/pyproject_cpu.toml` _+5 more__
- **2026-10-07** [`c52dcc5a01`](https://github.com/sgl-project/sglang/commit/c52dcc5a01) [#41585](https://github.com/sgl-project/sglang/pull/41585)
  The sgalng api specs (#41585)
  _Files: `.codespellrc`, `.pre-commit-config.yaml`, `docker/Dockerfile`, `docker/Dockerfile.cu134` _+91 more__
- **2026-10-07** [`1d019ce1c8`](https://github.com/sgl-project/sglang/commit/1d019ce1c8) [#15215](https://github.com/sgl-project/sglang/pull/15215)
  [diffusion] fix: honor the lazy transformer loader contract (#15215)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/component_loading.py`, `python/sglang/multimodal_gen/test/unit/test_component_loader_identity.py`, `python/sglang/multimodal_gen/test/unit/test_kandinsky6_bf16_dtype.py`_
- **2026-10-07** [`b0dff4009f`](https://github.com/sgl-project/sglang/commit/b0dff4009f) [#34903](https://github.com/sgl-project/sglang/pull/34903)
  [diffusion] cli: restore gated Diffusers model detection (#34903)
  _Files: `python/sglang/cli/utils.py`, `test/registered/unit/cli/test_utils.py`_
- **2026-10-07** [`bde01f8dc8`](https://github.com/sgl-project/sglang/commit/bde01f8dc8) [#42608](https://github.com/sgl-project/sglang/pull/42608)
  [Diffusion] Fuse Anima AdaLN modulation and cache the FFI callable (#42608)
  _Files: `python/sglang/kernels/ops/diffusion/modulate/modulate_scale_shift_jit.py`, `python/sglang/multimodal_gen/runtime/models/dits/anima.py`_
- **2026-10-07** [`35f18848db`](https://github.com/sgl-project/sglang/commit/35f18848db) [#19530](https://github.com/sgl-project/sglang/pull/19530)
  [diffusion] fix: validate output_quality and fix return type annotation (#19530)
  _Files: `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/utils.py`_
- **2026-10-07** [`3e914e69d5`](https://github.com/sgl-project/sglang/commit/3e914e69d5) [#42771](https://github.com/sgl-project/sglang/pull/42771)
  [AMD] ci: nightly-test the miles ROCm 10 MI30X image on MI300 (#42771)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm10-mi30x.yml`_
- **2026-10-07** [`6da08fd7cf`](https://github.com/sgl-project/sglang/commit/6da08fd7cf) [#42495](https://github.com/sgl-project/sglang/pull/42495)
  [diffusion] CI: fix qwen cache-dit step 10/49 perf baselines (#42495)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`_
- **2026-10-07** [`1351f32bb4`](https://github.com/sgl-project/sglang/commit/1351f32bb4) [#42768](https://github.com/sgl-project/sglang/pull/42768)
  [diffusion] refactor: simplify Kandinsky 6 models, SR sampling and tests (#42768)
  _Files: `docs/cookbook/diffusion/Kandinsky/Kandinsky6-SR.mdx`, `python/sglang/multimodal_gen/configs/models/dits/kandinsky6_sr.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/kandinsky6.py`, `python/sglang/multimodal_gen/runtime/models/dits/kandinsky6.py` _+43 more__
- **2026-10-06** [`38bdf25f8d`](https://github.com/sgl-project/sglang/commit/38bdf25f8d) [#42612](https://github.com/sgl-project/sglang/pull/42612)
  [Docker] Use uv-managed Python 3.12 and uv for all installs in the CUDA image (#42612)
  _Files: `docker/Dockerfile`_
- **2026-10-06** [`209e190ee5`](https://github.com/sgl-project/sglang/commit/209e190ee5) [#41605](https://github.com/sgl-project/sglang/pull/41605)
  [AMD] ci: build the miles ROCm 10 MI30X image nightly (#41605)
  _Files: `.github/workflows/release-docker-amd-miles-rocm10-nightly.yml`_
- **2026-10-06** [`e17935820a`](https://github.com/sgl-project/sglang/commit/e17935820a) [#35108](https://github.com/sgl-project/sglang/pull/35108)
  [diffusion] fix: fix width/height silently dropped on multipart /v1/videos requests (#35108)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`_
- **2026-10-06** [`679d2851ba`](https://github.com/sgl-project/sglang/commit/679d2851ba) [#40888](https://github.com/sgl-project/sglang/pull/40888)
  fix(mimo-vl): keep multimodal features when capturing aux hidden states and correct vision preprocessing (#40888)
  _Files: `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_vl.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`_
- **2026-10-06** [`16a23a672b`](https://github.com/sgl-project/sglang/commit/16a23a672b) [#42743](https://github.com/sgl-project/sglang/pull/42743)
  [diffusion] model: support Kandinsky 6 (#42743)
- **2026-10-06** [`2a5f45d3d4`](https://github.com/sgl-project/sglang/commit/2a5f45d3d4) [#42748](https://github.com/sgl-project/sglang/pull/42748)
  [diffusion] fix: skip zero blocks when hashing large conditioning inputs (#42748)
  _Files: `python/sglang/multimodal_gen/runtime/cache/conditioning.py`, `python/sglang/multimodal_gen/test/unit/test_conditioning_cache.py`_
- **2026-10-06** [`ba94488b42`](https://github.com/sgl-project/sglang/commit/ba94488b42) [#41655](https://github.com/sgl-project/sglang/pull/41655)
  [diffusion] feat: default Qwen-Image 2.1 to VAE tiling on gfx1151 (#41655)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image21.py`, `python/sglang/multimodal_gen/runtime/platforms/interface.py`, `python/sglang/multimodal_gen/runtime/platforms/rocm.py` _+1 more__
- **2026-10-06** [`1be3013118`](https://github.com/sgl-project/sglang/commit/1be3013118) [#30487](https://github.com/sgl-project/sglang/pull/30487)
  [diffusion] feat: support Ideogram TurboTime LoRA (#30487)
  _Files: `python/sglang/multimodal_gen/configs/sample/ideogram.py`, `python/sglang/multimodal_gen/runtime/cache/cache_dit_integration.py`, `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/runtime/models/dits/base.py` _+7 more__
- **2026-10-06** [`01345197af`](https://github.com/sgl-project/sglang/commit/01345197af) [#17270](https://github.com/sgl-project/sglang/pull/17270)
  [diffusion] chore: harden OpenAI upload filename handling (#17270)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/mesh_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/realtime_adapter.py` _+5 more__
- **2026-10-06** [`d0494af08b`](https://github.com/sgl-project/sglang/commit/d0494af08b) [#36854](https://github.com/sgl-project/sglang/pull/36854)
  [diffusion] security: pin multimodal-gen ZMQ scheduler ingress to loopback on wildcard --host (#36854)
  _Files: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-10-06** [`b524de2de6`](https://github.com/sgl-project/sglang/commit/b524de2de6) [#41718](https://github.com/sgl-project/sglang/pull/41718)
  [diffusion] optimization: release the allocator cache when the server idles not per request (#41718)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_metrics.py`, `python/sglang/multimodal_gen/test/unit/test_idle_cache_release.py` _+1 more__
- **2026-10-06** [`67959f80ab`](https://github.com/sgl-project/sglang/commit/67959f80ab) [#42609](https://github.com/sgl-project/sglang/pull/42609)
  [diffusion] optimization: fuse Anima FP32 split-half Q/K RoPE (#42609)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/rope_rotate_half_fp32.py`, `python/sglang/multimodal_gen/runtime/models/dits/anima.py`, `test/registered/kernels/ops/diffusion/test_model_fast_paths.py` _+1 more__
- **2026-10-06** [`21c9bbdf2c`](https://github.com/sgl-project/sglang/commit/21c9bbdf2c) [#41541](https://github.com/sgl-project/sglang/pull/41541)
  [diffusion] fix: fix concurrent server perf dump writes across ranks (#41541)
  _Files: `python/sglang/multimodal_gen/test/unit/test_performance_metrics.py`_
- **2026-10-06** [`36b216e2ee`](https://github.com/sgl-project/sglang/commit/36b216e2ee) [#42130](https://github.com/sgl-project/sglang/pull/42130)
  [Docs] Refresh K2 Horizon checkpoint revisions (#42130)
  _Files: `docs/cookbook/autoregressive/IFM/K2-Horizon.mdx`, `docs/src/snippets/configs/IFM/k2-horizon.jsx`_
- **2026-10-06** [`5d385007b3`](https://github.com/sgl-project/sglang/commit/5d385007b3) [#41830](https://github.com/sgl-project/sglang/pull/41830)
  [diffusion] kernels: take the Wan VAE decoder's remaining first-decode work off the request path (#41830)
  _Files: `python/sglang/kernels/ops/diffusion/layout/wan_causal_cache_triton.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wan_vae_cuda_opt.py`, `test/registered/kernels/ops/diffusion/test_layout.py`, `test/registered/kernels/ops/diffusion/test_shape_specialization.py` _+1 more__
- **2026-10-06** [`3120bb87a2`](https://github.com/sgl-project/sglang/commit/3120bb87a2) [#41723](https://github.com/sgl-project/sglang/pull/41723)
  [diffusion] fix: fix the OOM hint's placement advice and add a 24 GB Wan2.1 recipe (#41723)
  _Files: `docs/cookbook/diffusion/Wan/Wan2.1.mdx`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`_
- **2026-10-05** [`efb62ce269`](https://github.com/sgl-project/sglang/commit/efb62ce269) [#40158](https://github.com/sgl-project/sglang/pull/40158)
  [diffusion] fix: resolve QKV layout inference for MiniMax-H3 checkpoints (#40158)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_comfyui_h3.py`_
- **2026-10-05** [`150f568900`](https://github.com/sgl-project/sglang/commit/150f568900) [#41710](https://github.com/sgl-project/sglang/pull/41710)
  [diffusion] kernels: stop specializing on per-request sequence lengths (#41710)
  _Files: `python/sglang/kernels/kda_kernels/layernorm_modulate_triton.py`, `python/sglang/kernels/ops/diffusion/layout/ulysses_qkv_triton.py`, `python/sglang/kernels/ops/diffusion/layout/wan_causal_cache_triton.py`, `python/sglang/kernels/ops/diffusion/modulate/scale_shift_triton.py` _+2 more__
- **2026-10-05** [`a977e3b9d5`](https://github.com/sgl-project/sglang/commit/a977e3b9d5) [#41721](https://github.com/sgl-project/sglang/pull/41721)
  [diffusion] optimization: stream an oversized DiT in auto mode instead of OOMing (#41721)
  _Files: `python/sglang/multimodal_gen/runtime/loader/utils.py`, `python/sglang/multimodal_gen/runtime/server_args/auto_tune.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`, `python/sglang/multimodal_gen/test/unit/test_weight_utils.py`_
- **2026-10-05** [`ad3e80d4de`](https://github.com/sgl-project/sglang/commit/ad3e80d4de) [#41833](https://github.com/sgl-project/sglang/pull/41833)
  [diffusion] chore: warm the image writer and the HTTP route models at startup (#41833)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/test/unit/test_health_warmup_gate.py` _+1 more__
- **2026-10-05** [`c83c84b422`](https://github.com/sgl-project/sglang/commit/c83c84b422) [#41722](https://github.com/sgl-project/sglang/pull/41722)
  [diffusion] chore: keep the DiT off component offload under explicit multi-GPU fsdp (#41722)
  _Files: `docs/cookbook/diffusion/Wan/Wan2.1.mdx`, `docs/cookbook/diffusion/Wan/Wan2.2.mdx`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-10-05** [`23bf107469`](https://github.com/sgl-project/sglang/commit/23bf107469) [#22441](https://github.com/sgl-project/sglang/pull/22441)
  [diffusion] optimization: cache LTX-2 RoPE coords to avoid per-step recompute (#22441)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_bcg_coords.py`_
- **2026-10-05** [`91f9bf8d17`](https://github.com/sgl-project/sglang/commit/91f9bf8d17) [#22813](https://github.com/sgl-project/sglang/pull/22813)
  [diffusion] fix: fix scheduler host not working when ipv6 in multi modal gen (#22813)
  _Files: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-10-05** [`f20f8e120d`](https://github.com/sgl-project/sglang/commit/f20f8e120d) [#39523](https://github.com/sgl-project/sglang/pull/39523)
  [diffusion] model: restore folded H3 GGUF patch embedding (#39523)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/minimax_h3_qwen3vl.py`, `python/sglang/multimodal_gen/test/unit/test_gguf_diffusion.py`_
- **2026-10-05** [`83a6e1d39b`](https://github.com/sgl-project/sglang/commit/83a6e1d39b) [#42227](https://github.com/sgl-project/sglang/pull/42227)
  [diffusion] docs: keep model compatibility details in cookbook recipes (#42227)
  _Files: `docs/cookbook/diffusion/inclusionAI/Ming-Image.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`_
- **2026-10-05** [`860ebe720e`](https://github.com/sgl-project/sglang/commit/860ebe720e) [#40761](https://github.com/sgl-project/sglang/pull/40761)
  [diffusion] fix: skip warmup preferred preload when it would OOM (#40761)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_residency_strategies.py`, `python/sglang/multimodal_gen/test/unit/test_component_residency.py`_
- **2026-10-05** [`8663e3b670`](https://github.com/sgl-project/sglang/commit/8663e3b670) [#40095](https://github.com/sgl-project/sglang/pull/40095)
  [diffusion] optimization: avoid full-video clone in VAE post-processing for MiniMax-H3 (#40095)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_vae_processor.py`_
- **2026-10-05** [`d349e672bc`](https://github.com/sgl-project/sglang/commit/d349e672bc) [#41832](https://github.com/sgl-project/sglang/pull/41832)
  [diffusion] feat: recycle warmup-only entries of conditioning-cache at the first served store (#41832)
  _Files: `python/sglang/multimodal_gen/runtime/cache/conditioning.py`, `python/sglang/multimodal_gen/test/unit/test_conditioning_cache.py`_
- **2026-10-05** [`7352073ec6`](https://github.com/sgl-project/sglang/commit/7352073ec6) [#37549](https://github.com/sgl-project/sglang/pull/37549)
  [diffusion] feat: support --async-output-save to overlap output saving with the next request (#37549)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/performance-optimization.mdx`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py` _+4 more__
- **2026-10-05** [`f048d5aa4b`](https://github.com/sgl-project/sglang/commit/f048d5aa4b) [#35857](https://github.com/sgl-project/sglang/pull/35857)
  [diffusion] feat: add community LoRA recipes and Kohya mapping (#35857)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/format_adapter.py`_
- **2026-10-05** [`0263fdacb2`](https://github.com/sgl-project/sglang/commit/0263fdacb2) [#41641](https://github.com/sgl-project/sglang/pull/41641)
  [diffusion] fix: keep generic warmup valid for step-floored models and stop reporting a failed warmup as warm (#41641)
  _Files: `python/sglang/multimodal_gen/configs/sample/minimax_h3.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/runtime/entrypoints/diffusion_generator.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py` _+5 more__
- **2026-10-05** [`dd2ffdb680`](https://github.com/sgl-project/sglang/commit/dd2ffdb680) [#42226](https://github.com/sgl-project/sglang/pull/42226)
  [diffusion] nightly: keep nightly regression baselines on a comparable methodology (#42226)
  _Files: `python/sglang/multimodal_gen/test/unit/test_diffusion_nightly_comparison.py`, `scripts/ci/utils/diffusion/generate_diffusion_dashboard.py`_
- **2026-10-05** [`f218798006`](https://github.com/sgl-project/sglang/commit/f218798006) [#42505](https://github.com/sgl-project/sglang/pull/42505)
  [diffusion] CI: relax the load latency check and extend the 2-GPU retry deadline (#42505)
  _Files: `.github/workflows/pr-test-multimodal-gen.yml`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/server/test_server_utils.py`, `python/sglang/multimodal_gen/test/server/testcase_configs.py` _+2 more__

## KV Cache / Memory  (55 commits)

- **2026-10-12** [`a70a83bcd2`](https://github.com/sgl-project/sglang/commit/a70a83bcd2) [#43594](https://github.com/sgl-project/sglang/pull/43594)
  Keep NIXL Mamba checkpoint keys separate by TP rank (#43594)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/hicache_nixl.py`, `test/registered/unit/mem_cache/test_hicache_nixl_storage.py`_
- **2026-10-12** [`5ca0695aa6`](https://github.com/sgl-project/sglang/commit/5ca0695aa6) [#40223](https://github.com/sgl-project/sglang/pull/40223)
  [HiCache] Preserve all MTP KV and recurrent state (#40223)
  _Files: `python/sglang/srt/configs/inkling.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/mem_cache/base_swa_memory_pool.py`, `python/sglang/srt/mem_cache/cache_init_params.py` _+12 more__
- **2026-10-12** [`f5f5003323`](https://github.com/sgl-project/sglang/commit/f5f5003323) [#36345](https://github.com/sgl-project/sglang/pull/36345)
  [HiCache] Support Mamba in buffer-only host memory mode (#36345)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/storage_prefetch.py`, `python/sglang/srt/mem_cache/unified_cache/components/base.py` _+7 more__
- **2026-10-12** [`20c49f12c9`](https://github.com/sgl-project/sglang/commit/20c49f12c9) [#40925](https://github.com/sgl-project/sglang/pull/40925)
  Support kv cache sharding for DSA indexer (#40925)
  _Files: `python/sglang/srt/mem_cache/page_interleave_pool.py`, `test/registered/unit/mem_cache/test_page_interleave_shard.py`_
- **2026-10-12** [`77a15cf4e2`](https://github.com/sgl-project/sglang/commit/77a15cf4e2) [#43722](https://github.com/sgl-project/sglang/pull/43722)
  [MemCache] Add shared component size and path APIs to the tree core interface (#43722)
  _Files: `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/components/base.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py` _+6 more__
- **2026-10-12** [`e4cfc0c42a`](https://github.com/sgl-project/sglang/commit/e4cfc0c42a) [#43721](https://github.com/sgl-project/sglang/pull/43721)
  [MemCache] Split the SWA mapping move out of locked-full recovery as `RecoverEvictedSWA` (#43721)
  _Files: `python/sglang/srt/mem_cache/unified_cache/cache_action.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa.py`, `test/registered/unit/mem_cache/test_swa_locked_full_recover_unified.py`_
- **2026-10-11** [`46a97e5540`](https://github.com/sgl-project/sglang/commit/46a97e5540) [#43593](https://github.com/sgl-project/sglang/pull/43593)
  Preserve serialized page dtype in NIXL copy fallback (#43593)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/hicache_nixl.py`, `test/registered/unit/mem_cache/test_hicache_nixl_storage.py`_
- **2026-10-11** [`c938b6e454`](https://github.com/sgl-project/sglang/commit/c938b6e454) [#43596](https://github.com/sgl-project/sglang/pull/43596)
  Build Mamba host pools from device buffer infos (#43596)
  _Files: `python/sglang/srt/mem_cache/device_pool_info.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/pool_host/mamba.py` _+8 more__
- **2026-10-11** [`ef3e5c83c5`](https://github.com/sgl-project/sglang/commit/ef3e5c83c5) [#43550](https://github.com/sgl-project/sglang/pull/43550)
  [HiCache] Keep storage workers alive on backend exceptions (#43550)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`_
- **2026-10-11** [`0923bcd258`](https://github.com/sgl-project/sglang/commit/0923bcd258) [#43567](https://github.com/sgl-project/sglang/pull/43567)
  [Unified Radix] Invalidate lazy Mamba checkpoints before in-place tracking (#43567)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/radix_cache/test_mamba_cache_kl.py`_
- **2026-10-11** [`04f740580c`](https://github.com/sgl-project/sglang/commit/04f740580c) [#43475](https://github.com/sgl-project/sglang/pull/43475)
  [VLM] fix: repair multimodal VMM lease cleanup and source-stream ordering (#43475)
  _Files: `python/sglang/srt/managers/mm_schedule.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/models/deepseek_v4.py` _+15 more__
- **2026-10-11** [`dab108b9f3`](https://github.com/sgl-project/sglang/commit/dab108b9f3) [#43290](https://github.com/sgl-project/sglang/pull/43290)
  [Scheduler] Hold back decode rows on a mixed step when they do not fit the KV pool (#43290)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/chunked_prefill/test_scripted_swa_1gpu.py`_
- **2026-10-11** [`aa5c969dc3`](https://github.com/sgl-project/sglang/commit/aa5c969dc3) [#43237](https://github.com/sgl-project/sglang/pull/43237)
  [Perf] Fuse BF16 writes to native HND KV cache storage (#43237)
  _Files: `python/sglang/kernels/ops/kvcache/cache_ops.py`, `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-10-11** [`58cb1a2be6`](https://github.com/sgl-project/sglang/commit/58cb1a2be6) [#43479](https://github.com/sgl-project/sglang/pull/43479)
  [Scheduler] Keep waiting-prefix LRU refresh consistent across TP ranks (#43479)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `test/registered/unit/mem_cache/test_fcfs_waiting_prefix_refresh.py`_
- **2026-10-11** [`33d2ef1756`](https://github.com/sgl-project/sglang/commit/33d2ef1756) [#43564](https://github.com/sgl-project/sglang/pull/43564)
  [Fix] Reserve remaining tokens for ignore_eos requests during prefill admission (#43564)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `test/registered/unit/managers/test_prefill_adder.py`, `test/registered/unit/mem_cache/test_prefill_memory_budget.py`_
- **2026-10-10** [`0acd93c35c`](https://github.com/sgl-project/sglang/commit/0acd93c35c) [#43029](https://github.com/sgl-project/sglang/pull/43029)
  [Scheduler] Use committed length in spec mamba track boundary check (#43029)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/e2e/radix_cache/test_mamba_extra_buffer_spec_grammar.py`_
- **2026-10-10** [`f9cee8d2b2`](https://github.com/sgl-project/sglang/commit/f9cee8d2b2) [#42788](https://github.com/sgl-project/sglang/pull/42788)
  [HiCache] Keep protected cgroup page cache charged in host budgets (#42788)
  _Files: `python/sglang/srt/mem_cache/host_memory.py`, `test/registered/unit/mem_cache/test_host_memory.py`_
- **2026-10-10** [`587b6d622d`](https://github.com/sgl-project/sglang/commit/587b6d622d) [#43551](https://github.com/sgl-project/sglang/pull/43551)
  [Docs] Document Qwen3-4B/8B H200 mixed-chunk latency tradeoffs (#43551)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`_
- **2026-10-10** [`406540ab5f`](https://github.com/sgl-project/sglang/commit/406540ab5f) [#39606](https://github.com/sgl-project/sglang/pull/39606)
  [HiCache] Add staged write-back for the page-unified KV cache layout (#39606)
  _Files: `python/sglang/kernels/jit/csrc/kvcacheio/relayout.cuh`, `python/sglang/kernels/jit/csrc/kvcacheio/staged_write_back.cuh`, `python/sglang/kernels/ops/kvcache/hicache.py`, `test/registered/kernels/ops/kvcache/test_hicache_page_first_write_back.py`_
- **2026-10-10** [`99d6f4e158`](https://github.com/sgl-project/sglang/commit/99d6f4e158) [#41452](https://github.com/sgl-project/sglang/pull/41452)
  [MemCache] refactor: require an anchored lock receipt for non-root releases (#41452)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `rust/sglang-radix-tree/src/tests/components/full.rs`, `rust/sglang-radix-tree/src/tests/components/swa.rs` _+4 more__
- **2026-10-10** [`416ebe6090`](https://github.com/sgl-project/sglang/commit/416ebe6090) [#43538](https://github.com/sgl-project/sglang/pull/43538)
  [CI] Fix EAGLE3 CUDA parity prefill chunk alignment (#43538)
  _Files: `test/registered/spec/eagle/test_spec_eagle_parity.py`_
- **2026-10-10** [`49e629d239`](https://github.com/sgl-project/sglang/commit/49e629d239) [#42807](https://github.com/sgl-project/sglang/pull/42807)
  [Rust] Upgrade sglang-radix-tree to PyO3 0.29 (#42807)
  _Files: `rust/Cargo.toml`, `rust/sglang-radix-tree/Cargo.lock`, `rust/sglang-radix-tree/Cargo.toml`, `rust/sglang-radix-tree/src/python_bindings.rs`_
- **2026-10-10** [`17852cdfe8`](https://github.com/sgl-project/sglang/commit/17852cdfe8) [#43165](https://github.com/sgl-project/sglang/pull/43165)
  [DSv4.1] Initialize the full-to-SWA mapping for request-window pools (#43165)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `test/registered/unit/mem_cache/test_dsv4_compressed_pools.py`_
- **2026-10-10** [`f2e9a2bed1`](https://github.com/sgl-project/sglang/commit/f2e9a2bed1) [#43206](https://github.com/sgl-project/sglang/pull/43206)
  [unified memory pool] Allocate without transfer waits, pin floating SWA reservations, drop the HiCache startup asserts (#43206)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py`, `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py` _+19 more__
- **2026-10-10** [`55a8dffc87`](https://github.com/sgl-project/sglang/commit/55a8dffc87) [#43435](https://github.com/sgl-project/sglang/pull/43435)
  Skip the eager activation reserve in KV sizing on a capped Full prefill role (#43435)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/model_runner_components/kv_pool_runtime.py`_
- **2026-10-10** [`37114afe20`](https://github.com/sgl-project/sglang/commit/37114afe20) [#42982](https://github.com/sgl-project/sglang/pull/42982)
  [AMD][Fix] Saturate FP8 KV commits instead of reproducing e4m3fnuz NaN overflow (#42982)
  _Files: `python/sglang/kernels/ops/kvcache/cache_move.py`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/test/kernels/prefix_valid.py` _+1 more__
- **2026-10-10** [`5f94a45896`](https://github.com/sgl-project/sglang/commit/5f94a45896) [#43461](https://github.com/sgl-project/sglang/pull/43461)
  [srt] Allow mixed chunk prefill on the Full prefill CUDA graph backend (#43461)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/unit/model_executor/test_prefill_cuda_graph_runner.py`_
- **2026-10-10** [`8cf4d73c84`](https://github.com/sgl-project/sglang/commit/8cf4d73c84) [#43334](https://github.com/sgl-project/sglang/pull/43334)
  [XPU] Fix XPU CI breaks from #41105 (KDA chunk_offsets) and #42588 (int4 test tp_group) (#43334)
  _Files: `python/sglang/srt/hardware_backend/xpu/kernels/fla/chunk_delta_h.py`, `test/registered/xpu/test_xpu_int4_dense.py`_
- **2026-10-09** [`114cb44920`](https://github.com/sgl-project/sglang/commit/114cb44920) [#43291](https://github.com/sgl-project/sglang/pull/43291)
  [MLX] Read radix prefix slots from the model runner's `req_to_token` pool (#43291)
  _Files: `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `test/registered/unit/hardware_backend/mlx/test_tp_worker_routing.py`_
- **2026-10-09** [`87845cda2b`](https://github.com/sgl-project/sglang/commit/87845cda2b) [#43301](https://github.com/sgl-project/sglang/pull/43301)
  [Multimodal] Chunk and cache audio items whose offsets span several placeholder runs (#43301)
  _Files: `python/sglang/srt/managers/mm_schedule.py`, `test/registered/chunked_prefill/test_mm_chunked_embedding_unit.py`_
- **2026-10-09** [`0955169ed2`](https://github.com/sgl-project/sglang/commit/0955169ed2) [#35694](https://github.com/sgl-project/sglang/pull/35694)
  [mem_cache] Bound FlexKV checkpoint stores and restore DSPARK cache checks (#35694)
  _Files: `python/sglang/srt/mem_cache/storage/flexkv/flexkv_radix_cache.py`, `test/registered/e2e/models/test_inkling_small_nvfp4.py`_
- **2026-10-09** [`f48ed2127e`](https://github.com/sgl-project/sglang/commit/f48ed2127e) [#42523](https://github.com/sgl-project/sglang/pull/42523)
  test: allow bounded checkpoint lag in Mamba HiCache tests (#42523)
  _Files: `python/sglang/test/kl_multiturn_utils.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mamba.py`_
- **2026-10-09** [`125f88cb75`](https://github.com/sgl-project/sglang/commit/125f88cb75) [#42894](https://github.com/sgl-project/sglang/pull/42894)
  [Refactor] Run Kimi K3 through stage boundaries (#42894)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/arg_groups/boundary_reduction.py`, `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/layers/layer_boundary/factories.py` _+13 more__
- **2026-10-09** [`4ee3f0f370`](https://github.com/sgl-project/sglang/commit/4ee3f0f370) [#43183](https://github.com/sgl-project/sglang/pull/43183)
  [Session] Skip the KV free when page alignment empties a streaming-session rewind (#43183)
  _Files: `python/sglang/srt/session/streaming_session.py`, `test/registered/unit/mem_cache/test_streaming_session_unit.py`_
- **2026-10-09** [`4e3eaba619`](https://github.com/sgl-project/sglang/commit/4e3eaba619) [#43174](https://github.com/sgl-project/sglang/pull/43174)
  [HiCache] Re-admit a split node's queued buffer-mode write instead of dropping it (#43174)
  _Files: `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-10-09** [`f6569bce4d`](https://github.com/sgl-project/sglang/commit/f6569bce4d) [#43253](https://github.com/sgl-project/sglang/pull/43253)
  [MemCache] Skip KV events and eviction config on a disabled radix cache (#43253)
  _Files: `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_radix_cache_unit.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-10-09** [`e0ab91e3ca`](https://github.com/sgl-project/sglang/commit/e0ab91e3ca) [#43202](https://github.com/sgl-project/sglang/pull/43202)
  [MemCache] Rename `SWAChunkCapPoolConfigurator` to `SWARequestCapPoolConfigurator` (#43202)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-10-09** [`b2786a670e`](https://github.com/sgl-project/sglang/commit/b2786a670e) [#43185](https://github.com/sgl-project/sglang/pull/43185)
  [MemCache] Count reclaimable tokens in the unified tree ledgers (#43185)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/base.py`, `python/sglang/srt/mem_cache/unified_cache/components/full.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-10-09** [`508ba79688`](https://github.com/sgl-project/sglang/commit/508ba79688) [#43200](https://github.com/sgl-project/sglang/pull/43200)
  [MemCache] Serve disabled hybrid-SWA models with `UnifiedRadixCache` (#43200)
  _Files: `python/sglang/srt/mem_cache/registry.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa.py`, `test/registered/unit/mem_cache/test_registry.py`_
- **2026-10-09** [`977e2719c7`](https://github.com/sgl-project/sglang/commit/977e2719c7) [#43198](https://github.com/sgl-project/sglang/pull/43198)
  [MemCache] Serve disabled pure-SWA models with `PureSWARadixCache` (#43198)
  _Files: `python/sglang/srt/mem_cache/pure_swa_radix_cache.py`, `python/sglang/srt/mem_cache/registry.py`, `test/registered/unit/mem_cache/test_pure_swa_radix_cache.py`, `test/registered/unit/mem_cache/test_registry.py`_
- **2026-10-09** [`57ce47862d`](https://github.com/sgl-project/sglang/commit/57ce47862d) [#43197](https://github.com/sgl-project/sglang/pull/43197)
  [MemCache] Report no prefix sharing from a disabled `RadixCache` (#43197)
  _Files: `python/sglang/srt/mem_cache/radix_cache.py`, `test/registered/unit/mem_cache/test_radix_cache_unit.py`, `test/registered/unit/mem_cache/test_swa_eviction_interval.py`_
- **2026-10-09** [`20d1f3f56a`](https://github.com/sgl-project/sglang/commit/20d1f3f56a) [#41593](https://github.com/sgl-project/sglang/pull/41593)
  [Scheduler] Refresh waiting requests' cached prefixes under FCFS-like policies with LRU eviction (#41593)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/common.py` _+4 more__
- **2026-10-08** [`ae4da8cd78`](https://github.com/sgl-project/sglang/commit/ae4da8cd78) [#43203](https://github.com/sgl-project/sglang/pull/43203)
  [MemCache] Skip SWA request-cap pool sizing when chunked prefill is off (#43203)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-10-08** [`e2fbc6a550`](https://github.com/sgl-project/sglang/commit/e2fbc6a550) [#42643](https://github.com/sgl-project/sglang/pull/42643)
  Stream a chunk once stream_interval tokens are unsent (#42643)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `test/registered/unit/managers/test_output_streamer_customized_info.py`_
- **2026-10-08** [`642e81fbb8`](https://github.com/sgl-project/sglang/commit/642e81fbb8) [#43100](https://github.com/sgl-project/sglang/pull/43100)
  Fix DSA index host buffer cleanup (#43100)
  _Files: `python/sglang/srt/mem_cache/pool_host/dsa.py`, `test/registered/hicache/test_dsa_host_release.py`_
- **2026-10-07** [`b1ffe5c16a`](https://github.com/sgl-project/sglang/commit/b1ffe5c16a) [#42846](https://github.com/sgl-project/sglang/pull/42846)
  [dLLM] Keep the request row across FDFO blocks (#42846)
  _Files: `python/sglang/srt/dllm/mixin/scheduler.py`, `test/registered/unit/mem_cache/test_dllm_fdfo_kv_reuse.py`_
- **2026-10-07** [`685d4d453d`](https://github.com/sgl-project/sglang/commit/685d4d453d) [#42399](https://github.com/sgl-project/sglang/pull/42399)
  [HiCache] Add SeaweedFS L3 storage backend (#42399)
  _Files: `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/storage/backend_factory.py`, `python/sglang/srt/mem_cache/storage/seaweedfs/README.md` _+3 more__
- **2026-10-07** [`e23093077e`](https://github.com/sgl-project/sglang/commit/e23093077e) [#42832](https://github.com/sgl-project/sglang/pull/42832)
  [DSv4] Fix shared index cache accessor page size (#42832)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`_
- **2026-10-07** [`2889158792`](https://github.com/sgl-project/sglang/commit/2889158792) [#42518](https://github.com/sgl-project/sglang/pull/42518)
  [MemCache] test: require every ComponentData field to be classified by each split hook (#42518)
  _Files: `test/registered/unit/mem_cache/test_component_split_contract.py`_
- **2026-10-06** [`08aad0c196`](https://github.com/sgl-project/sglang/commit/08aad0c196) [#42633](https://github.com/sgl-project/sglang/pull/42633)
  [HiCache] Manage buffer-mode backups per storage pool (#42633)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/buffer_mode/storage_existence_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py` _+7 more__
- **2026-10-06** [`e49e971131`](https://github.com/sgl-project/sglang/commit/e49e971131) [#42467](https://github.com/sgl-project/sglang/pull/42467)
  [mem_cache] Keep prefix_indices current for chunked requests kept out of the tree (#42467)
  _Files: `python/sglang/srt/mem_cache/common.py`_
- **2026-10-06** [`ed75fe67f1`](https://github.com/sgl-project/sglang/commit/ed75fe67f1) [#40915](https://github.com/sgl-project/sglang/pull/40915)
  Declare hybrid Mamba indexer host pool (#40915)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`_
- **2026-10-06** [`f3fe753475`](https://github.com/sgl-project/sglang/commit/f3fe753475) [#42657](https://github.com/sgl-project/sglang/pull/42657)
  [misc] Rename `SGLANG_OPT_SWA_RELEASE_LEAF_LOCK_AFTER_WINDOW` to `SGLANG_OPT_RELEASE_PREFILL_SWA` (#42657)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `test/manual/dsv4/test_dsv4_swa_radix_retract.py`, `test/registered/unit/mem_cache/test_swa_eviction_interval.py`_
- **2026-10-05** [`968726f3ce`](https://github.com/sgl-project/sglang/commit/968726f3ce) [#33883](https://github.com/sgl-project/sglang/pull/33883)
  [HiCache] Route --file-storage-path to the file storage backend (#33883)
  _Files: `python/sglang/srt/arg_groups/fields/serving.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_hicache_file_storage_path_unit.py`_
- **2026-10-05** [`503b898540`](https://github.com/sgl-project/sglang/commit/503b898540) [#42539](https://github.com/sgl-project/sglang/pull/42539)
  [Session] Count streaming session KV by owner in pool accounting (#42539)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/managers/scheduler_components/pool_stats_observer.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` _+7 more__

## Prefill / Decode Disaggregation  (41 commits)

- **2026-10-12** [`f92199b569`](https://github.com/sgl-project/sglang/commit/f92199b569) [#40896](https://github.com/sgl-project/sglang/pull/40896)
  [Unified Cache] Abort requests whose external linker load fails instead of crashing the scheduler (#40896)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py` _+15 more__
- **2026-10-12** [`7953751bfa`](https://github.com/sgl-project/sglang/commit/7953751bfa) [#41783](https://github.com/sgl-project/sglang/pull/41783)
  [PD][Spec] Give a PD decode's first EAGLE draft step a proposal distribution (#41783)
  _Files: `python/sglang/srt/speculative/eagle_disaggregation.py`, `test/registered/unit/speculative/test_pd_eagle_draft_proposal.py`_
- **2026-10-12** [`62ff466ac0`](https://github.com/sgl-project/sglang/commit/62ff466ac0) [#40323](https://github.com/sgl-project/sglang/pull/40323)
  [DSV4.1][PD][1/N] Support prefill node use cp parallel strategy (#40323)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` _+5 more__
- **2026-10-12** [`4195980f5a`](https://github.com/sgl-project/sglang/commit/4195980f5a) [#43719](https://github.com/sgl-project/sglang/pull/43719)
  [PD] Poison the deferred abort ack when a Mooncake send fails (#43719)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `test/registered/unit/disaggregation/test_deferred_decode_kv_release.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py` _+1 more__
- **2026-10-12** [`9e0b001db4`](https://github.com/sgl-project/sglang/commit/9e0b001db4) [#43769](https://github.com/sgl-project/sglang/pull/43769)
  [CI] Skip eval retries in the PD transfer-failure test (#43769)
  _Files: `test/registered/disaggregation/test_disaggregation_basic.py`_
- **2026-10-12** [`a1001bcf3a`](https://github.com/sgl-project/sglang/commit/a1001bcf3a) [#43757](https://github.com/sgl-project/sglang/pull/43757)
  [PD] Retract transferred decode requests on a retract pause (#43757)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_flush_cache_after_retract.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_
- **2026-10-11** [`d62b9c2480`](https://github.com/sgl-project/sglang/commit/d62b9c2480) [#42455](https://github.com/sgl-project/sglang/pull/42455)
  [KV Events] Publish LoRA adapter names and namespaced block hashes (#42455)
  _Files: `python/sglang/srt/disaggregation/kv_events.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/events.py` _+11 more__
- **2026-10-11** [`53295c6972`](https://github.com/sgl-project/sglang/commit/53295c6972) [#43386](https://github.com/sgl-project/sglang/pull/43386)
  [kvevents] fix missing topics in replayed kv events (#43386)
  _Files: `experimental/sgl-router/src/state/kv_events/subscriber.rs`, `python/sglang/srt/disaggregation/kv_events.py`, `test/registered/unit/disaggregation/test_kv_events.py`_
- **2026-10-11** [`e1f43c9a61`](https://github.com/sgl-project/sglang/commit/e1f43c9a61) [#43562](https://github.com/sgl-project/sglang/pull/43562)
  [PD][HiCache] Fold the decode restore outcome into the MIN-reduced KV poll (#43562)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/disaggregation/utils.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-10-10** [`c640dc97ce`](https://github.com/sgl-project/sglang/commit/c640dc97ce) [#43598](https://github.com/sgl-project/sglang/pull/43598)
  [CI] Fix Kimi-Linear DCP PD test startup (#43598)
  _Files: `test/registered/disaggregation/test_disaggregation_kimi_linear.py`_
- **2026-10-10** [`de487f8039`](https://github.com/sgl-project/sglang/commit/de487f8039) [#40102](https://github.com/sgl-project/sglang/pull/40102)
  [kv-shard 3/4] Enable Control Plane C (#40102)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/parallel.py`, `python/sglang/srt/arg_groups/kv_shard_hook.py` _+13 more__
- **2026-10-10** [`6fc8d9da32`](https://github.com/sgl-project/sglang/commit/6fc8d9da32) [#42989](https://github.com/sgl-project/sglang/pull/42989)
  [rust-server] preserve PD routing in chat and completions (#42989)
  _Files: `rust/sglang-server/src/api_server/http/openai.rs`, `rust/sglang-server/src/api_server/http/openai/chat.rs`, `rust/sglang-server/src/api_server/http/openai/completions.rs`, `rust/sglang-server/src/api_server/http/openai/pd_routing.rs` _+2 more__
- **2026-10-10** [`441de659f4`](https://github.com/sgl-project/sglang/commit/441de659f4) [#43505](https://github.com/sgl-project/sglang/pull/43505)
  [CI] Fix Python 3.10 failure in prefill complete integration test (#43505)
  _Files: `test/registered/unit/disaggregation/test_prefill_complete_integration.py`_
- **2026-10-10** [`8b2aaf7060`](https://github.com/sgl-project/sglang/commit/8b2aaf7060) [#42287](https://github.com/sgl-project/sglang/pull/42287)
  [Refactor][TCPCG] Retire backend selection and configuration (3/9) (#42287)
  _Files: `docs/docs.json`, `docs/docs/advanced_features/breakable_cuda_graph.mdx`, `docs/docs/advanced_features/cuda_graph_for_multi_modal_encoder.mdx`, `docs/docs/advanced_features/piecewise_cuda_graph.mdx` _+26 more__
- **2026-10-10** [`1814ece57f`](https://github.com/sgl-project/sglang/commit/1814ece57f) [#43329](https://github.com/sgl-project/sglang/pull/43329)
  [PP+PD] Harden PPConsensusStore: msgspec wire format, drop malformed messages (#43329)
  _Files: `python/sglang/srt/disaggregation/pp_consensus_store.py`, `test/registered/unit/disaggregation/test_pp_consensus_store.py`_
- **2026-10-10** [`20948cdcc6`](https://github.com/sgl-project/sglang/commit/20948cdcc6) [#43442](https://github.com/sgl-project/sglang/pull/43442)
  [PD] Reclaim parked optimistic prefills when request slots are exhausted (#43442)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `test/registered/unit/disaggregation/test_prefill_complete_integration.py`_
- **2026-10-10** [`a338b9858a`](https://github.com/sgl-project/sglang/commit/a338b9858a) [#43410](https://github.com/sgl-project/sglang/pull/43410)
  [PD] Receive decode KV into separate paged SWA host pools; let host-capable receivers own abort drain tracking (#43410)
  _Files: `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/pool_host/group.py` _+2 more__
- **2026-10-10** [`e8fb52c526`](https://github.com/sgl-project/sglang/commit/e8fb52c526) [#43439](https://github.com/sgl-project/sglang/pull/43439)
  [Fix] Keep request-pool row generations monotonic across clear() (#43439)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/disaggregation/test_decode_req_to_token_pool.py`_
- **2026-10-09** [`f7e601b936`](https://github.com/sgl-project/sglang/commit/f7e601b936) [#43282](https://github.com/sgl-project/sglang/pull/43282)
  [MLX] Drain in-flight jobs before a retract-mode `pause_generation` (#43282)
  _Files: `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/disaggregation/test_prefill_result_polling.py`, `test/registered/unit/hardware_backend/mlx/test_scheduler_mixin.py` _+1 more__
- **2026-10-09** [`f6c848c882`](https://github.com/sgl-project/sglang/commit/f6c848c882) [#43407](https://github.com/sgl-project/sglang/pull/43407)
  [PD] Use 1 to disable decode host receive and 0 for always-on (#43407)
  _Files: `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/decode.py` _+8 more__
- **2026-10-09** [`78996e3f02`](https://github.com/sgl-project/sglang/commit/78996e3f02) [#39696](https://github.com/sgl-project/sglang/pull/39696)
  [Performance] Batch Mooncake hybrid-pool metadata and puts (#39696)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `test/registered/unit/mem_cache/test_mooncake_group_semantics.py`_
- **2026-10-09** [`348689da40`](https://github.com/sgl-project/sglang/commit/348689da40) [#38959](https://github.com/sgl-project/sglang/pull/38959)
  [PP+PD] Fix #38206 Reduce bootstrap consensus latency (#38959)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/fake/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py` _+9 more__
- **2026-10-09** [`e14ef4b658`](https://github.com/sgl-project/sglang/commit/e14ef4b658) [#42720](https://github.com/sgl-project/sglang/pull/42720)
  [Scheduler] Skip the decode for a request whose last token is already in flight (#42720)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/test/kits/streaming_session_kit.py` _+6 more__
- **2026-10-09** [`b4fe282836`](https://github.com/sgl-project/sglang/commit/b4fe282836) [#43201](https://github.com/sgl-project/sglang/pull/43201)
  [MemCache] Delete `ChunkCache` (#43201)
  _Files: `.github/labeler.yml`, `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/docs/advanced_features/dcp.mdx`, `docs/src/snippets/_kimi_k3_mamba_ratio_calculator.jsx` _+19 more__
- **2026-10-08** [`bb43927404`](https://github.com/sgl-project/sglang/commit/bb43927404) [#43173](https://github.com/sgl-project/sglang/pull/43173)
  [PD] Charge decode admission the page-rounded allocation when the radix cache is disabled (#43173)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`, `test/registered/unit/managers/test_priority_scheduling_disaggregation.py`_
- **2026-10-08** [`b0e06359ac`](https://github.com/sgl-project/sglang/commit/b0e06359ac) [#40177](https://github.com/sgl-project/sglang/pull/40177)
  [DSV4.1][PD][5/N] Decode node support DP attention (#40177)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/disaggregation/common/conn.py`_
- **2026-10-08** [`3fef129ff8`](https://github.com/sgl-project/sglang/commit/3fef129ff8) [#42904](https://github.com/sgl-project/sglang/pull/42904)
  [PD] Allow state-only KV checksum inputs (#42904)
  _Files: `python/sglang/srt/disaggregation/checksum.py`, `test/registered/unit/disaggregation/test_kv_checksum.py`_
- **2026-10-08** [`89b5935793`](https://github.com/sgl-project/sglang/commit/89b5935793) [#43023](https://github.com/sgl-project/sglang/pull/43023)
  [MemCache] Return only the loaded length from `init_load_back`; drop `empty_device_indices` (#43023)
  _Files: `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py` _+12 more__
- **2026-10-08** [`5a4d01a3ae`](https://github.com/sgl-project/sglang/commit/5a4d01a3ae) [#42923](https://github.com/sgl-project/sglang/pull/42923)
  [MemCache] Return only the matched length from `match_prefix`; read KV indices off the node path (#42923)
  _Files: `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/hardware_backend/npu/dsv4/c128_sidecar_component.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` _+39 more__
- **2026-10-07** [`1066decce6`](https://github.com/sgl-project/sglang/commit/1066decce6) [#42822](https://github.com/sgl-project/sglang/pull/42822)
  [Scheduler] Replace `extend_range` with `extend_end` derived from `prefix_len` (#42822)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/prefill.py` _+38 more__
- **2026-10-07** [`5349d3e9d2`](https://github.com/sgl-project/sglang/commit/5349d3e9d2) [#42825](https://github.com/sgl-project/sglang/pull/42825)
  [Scheduler] Derive prefix KV indices from `last_node` at allocation; drop `Req.prefix_indices` (#42825)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/managers/schedule_batch.py` _+36 more__
- **2026-10-07** [`e9240b3243`](https://github.com/sgl-project/sglang/commit/e9240b3243) [#42824](https://github.com/sgl-project/sglang/pull/42824)
  [Scheduler] Track prefill progress as `prefix_len` (#42824)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py` _+41 more__
- **2026-10-07** [`4bf8f28d15`](https://github.com/sgl-project/sglang/commit/4bf8f28d15) [#42823](https://github.com/sgl-project/sglang/pull/42823)
  [Scheduler] Fold match write-back into `match_kv_cache` (#42823)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py` _+2 more__
- **2026-10-07** [`f1065423d3`](https://github.com/sgl-project/sglang/commit/f1065423d3) [#42649](https://github.com/sgl-project/sglang/pull/42649)
  [PD] Stop reserving unallocated mamba spec-verify scratch in prefill KV sizing (#42649)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `test/registered/unit/mem_cache/test_mamba_donated_alloc_ratio.py`_
- **2026-10-06** [`fd62ee84f7`](https://github.com/sgl-project/sglang/commit/fd62ee84f7) [#39659](https://github.com/sgl-project/sglang/pull/39659)
  feat(grpc): expose follower metadata and node-local KV sources (#39659)
  _Files: `proto/build.rs`, `python/sglang/srt/arg_groups/fields/serving.py`, `python/sglang/srt/disaggregation/kv_events.py`, `python/sglang/srt/entrypoints/engine.py` _+13 more__
- **2026-10-06** [`abed685de1`](https://github.com/sgl-project/sglang/commit/abed685de1) [#41927](https://github.com/sgl-project/sglang/pull/41927)
  [PD] Fix crash for allocation when mamba + pd + decode radix cache (#41927)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/allocation.py`, `python/sglang/srt/mem_cache/allocation_sizing.py` _+4 more__
- **2026-10-06** [`c7f3ae1dd5`](https://github.com/sgl-project/sglang/commit/c7f3ae1dd5) [#42686](https://github.com/sgl-project/sglang/pull/42686)
  [mem_cache] Hold a request's tree lock as one `TreeLock` (#42686)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/schedule_batch.py` _+26 more__
- **2026-10-06** [`c683190b40`](https://github.com/sgl-project/sglang/commit/c683190b40) [#41395](https://github.com/sgl-project/sglang/pull/41395)
  [PD] Wait for prefill completion before Mooncake early KV transfer (#41395)
  _Files: `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `test/registered/unit/disaggregation/test_mooncake_transfer_batching.py`, `test/registered/unit/disaggregation/test_prefill_complete_integration.py`_
- **2026-10-06** [`ad7a9b53cc`](https://github.com/sgl-project/sglang/commit/ad7a9b53cc) [#42270](https://github.com/sgl-project/sglang/pull/42270)
  [mem_cache] Make `release_kv_cache`'s final checkpoint an explicit `checkpoint` flag (#42270)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/schedule_batch.py` _+22 more__
- **2026-10-06** [`c01d59eb90`](https://github.com/sgl-project/sglang/commit/c01d59eb90) [#42537](https://github.com/sgl-project/sglang/pull/42537)
  [Session] Let a streaming session own its KV record and tree lock from the first turn (#42537)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/allocation.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` _+7 more__
- **2026-10-05** [`734cf3cf3b`](https://github.com/sgl-project/sglang/commit/734cf3cf3b) [#41691](https://github.com/sgl-project/sglang/pull/41691)
  [PD] Reload NIXL peer metadata after the peer is invalidated (#41691)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_

## MoE / Expert Parallel  (37 commits)

- **2026-10-12** [`06887827c7`](https://github.com/sgl-project/sglang/commit/06887827c7) [#43784](https://github.com/sgl-project/sglang/pull/43784)
  [CI] Move tests that do not need GB300 off the per-PR GB300 suite (#43784)
  _Files: `test/registered/e2e/models/test_deepseek_v41_flash_gb300.py`, `test/registered/e2e/models_large/test_deepseek_v3_cutedsl_4gpu.py`, `test/registered/ep/test_flashinfer_a2a.py`, `test/registered/kernels/ops/attention/test_flash_attention_4_sm103.py` _+2 more__
- **2026-10-12** [`166b4ae7fc`](https://github.com/sgl-project/sglang/commit/166b4ae7fc) [#43688](https://github.com/sgl-project/sglang/pull/43688)
  [Fix] Adapt to transformers 5.18 / 5.19 changes (#43688)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `python/sglang/multimodal_gen/runtime/models/encoders/hunyuan3d.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/configs/granitemoehybrid.py` _+5 more__
- **2026-10-12** [`0d0be8fc98`](https://github.com/sgl-project/sglang/commit/0d0be8fc98) [#40666](https://github.com/sgl-project/sglang/pull/40666)
  [AMD][MORI] Add MORI EP V2 support (#40666)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/moe_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/eplb/expert_distribution.py` _+13 more__
- **2026-10-12** [`37d2e5c34f`](https://github.com/sgl-project/sglang/commit/37d2e5c34f) [#43077](https://github.com/sgl-project/sglang/pull/43077)
  [AMD][V4.1][*/N] Fix DP attention + TP MoE decode NaN and support bounded replay (#43077)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+3 more__
- **2026-10-12** [`0c52cb1519`](https://github.com/sgl-project/sglang/commit/0c52cb1519) [#42212](https://github.com/sgl-project/sglang/pull/42212)
  [MoE] Skip block-padding rows in the TMA down activation and quant (#42212)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/activation.cuh`, `python/sglang/kernels/jit/csrc/gemm/per_token_group_quant.cuh`, `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/kernels/ops/quantization/per_token_group_quant.py` _+4 more__
- **2026-10-11** [`6576e50cd5`](https://github.com/sgl-project/sglang/commit/6576e50cd5) [#43228](https://github.com/sgl-project/sglang/pull/43228)
  [1/N][DSv41] Enable DP attention with MegaMoE (#43228)
  _Files: `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_dspark.py`, `python/sglang/srt/multimodal/dsv41/vl_routing.py` _+3 more__
- **2026-10-10** [`234ccba7f6`](https://github.com/sgl-project/sglang/commit/234ccba7f6) [#43460](https://github.com/sgl-project/sglang/pull/43460)
  [Refactor] Declare every model's stages from a shared function and drop the meta-device neighbour build (#43460)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/layer_boundary/factories.py`, `python/sglang/srt/layers/layer_boundary/facts.py`, `python/sglang/srt/layers/layer_boundary/residual/attn_bank.py` _+61 more__
- **2026-10-10** [`a65f4ffba5`](https://github.com/sgl-project/sglang/commit/a65f4ffba5) [#43472](https://github.com/sgl-project/sglang/pull/43472)
  [diffusion] docs: standardize diffusion cookbook command builders (#43472)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `docs/cookbook/diffusion/Ernie-Image/Ernie-Image.mdx`, `docs/cookbook/diffusion/FLUX/FLUX.mdx`, `docs/cookbook/diffusion/Ideogram/Ideogram4.mdx` _+52 more__
- **2026-10-09** [`961bcf481d`](https://github.com/sgl-project/sglang/commit/961bcf481d) [#43432](https://github.com/sgl-project/sglang/pull/43432)
  support DeepEP v2 on GLM-5.3 (#43432)
  _Files: `python/sglang/srt/configs/moe_model_registry.py`_
- **2026-10-09** [`2f1acef3d8`](https://github.com/sgl-project/sglang/commit/2f1acef3d8) [#31768](https://github.com/sgl-project/sglang/pull/31768)
  [Model] Add LLaDA2.2 Block Routing MoE support (#31768)
  _Files: `python/sglang/srt/dllm/config.py`, `python/sglang/srt/models/llada2.py`, `test/registered/kernels/ops/moe/test_block_topk_triton.py`, `test/registered/unit/models/test_llada2.py`_
- **2026-10-09** [`3bffe69b74`](https://github.com/sgl-project/sglang/commit/3bffe69b74) [#43245](https://github.com/sgl-project/sglang/pull/43245)
  [moe] Fill num_token_non_padded for the customized A2A backend at EP 1 (#43245)
  _Files: `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/model_executor/test_num_token_non_padded_localization.py`_
- **2026-10-09** [`db32673b78`](https://github.com/sgl-project/sglang/commit/db32673b78) [#41258](https://github.com/sgl-project/sglang/pull/41258)
  [AMD] Let the GLM DSA NextN draft declare its own shared-expert fusion architecture (#41258)
  _Files: `python/sglang/srt/models/glm4_moe.py`, `test/registered/unit/models/test_glm_nextn_moe_ptpc.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`_
- **2026-10-09** [`0eb24e7d5b`](https://github.com/sgl-project/sglang/commit/0eb24e7d5b) [#42175](https://github.com/sgl-project/sglang/pull/42175)
  [Performance] Optimize Qwen3.8-Flash-Next BF16 decode on Blackwell (#42175)
  _Files: `python/sglang/kernels/jit/csrc/distributed/all_reduce_fusion.cuh`, `python/sglang/kernels/jit/csrc/elementwise/hc_combine_decode.cuh`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/kernels/ops/communication/__init__.py` _+17 more__
- **2026-10-09** [`08fc290f48`](https://github.com/sgl-project/sglang/commit/08fc290f48) [#41982](https://github.com/sgl-project/sglang/pull/41982)
  [AMD] gfx950 small-batch MoE: expert-count gate for the small sort and FP8 block-scale small-M kernel (#41982)
  _Files: `python/sglang/kernels/ops/moe/moe_sorting_small.py`, `python/sglang/kernels/ops/moe/smallm_moe_gfx950/__init__.py`, `python/sglang/kernels/ops/moe/smallm_moe_gfx950/smallm_moe.hip`, `python/sglang/srt/layers/moe/moe_runner/aiter.py` _+2 more__
- **2026-10-09** [`3c1703d2ff`](https://github.com/sgl-project/sglang/commit/3c1703d2ff) [#31054](https://github.com/sgl-project/sglang/pull/31054)
  [AMD] Support Quark DeepSeek-V4-MXFP4 checkpoints on the DSV4 stack, enabling shared-expert fusion and MTP (#31054)
  _Files: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_nextn.py` _+1 more__
- **2026-10-08** [`71584b62c0`](https://github.com/sgl-project/sglang/commit/71584b62c0) [#43226](https://github.com/sgl-project/sglang/pull/43226)
  [CI] Fix stale fakes in the NVFP4 MoE dispatch and CP strategy unit tests (#43226)
  _Files: `test/registered/cp/test_cp_strategy_unit.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4_moe_dispatch.py`_
- **2026-10-08** [`0b658c12ff`](https://github.com/sgl-project/sglang/commit/0b658c12ff) [#43188](https://github.com/sgl-project/sglang/pull/43188)
  [Bench][MoE] Deal the simulated round-robin experts evenly across EP ranks (#43188)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/runtime_context.py`, `test/manual/layers/moe/test_simulate_balanced_routing.py`, `test/registered/kernels/ops/moe/test_round_robin_ep_balance.py`_
- **2026-10-08** [`d20bdc1443`](https://github.com/sgl-project/sglang/commit/d20bdc1443) [#39199](https://github.com/sgl-project/sglang/pull/39199)
  Add per-token NVFP4 MoE support for ReLU2 activation (#39199)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`, `test/registered/e2e/models_large/test_nvidia_nemotron_3_super_nvfp4.py` _+1 more__
- **2026-10-08** [`214347891a`](https://github.com/sgl-project/sglang/commit/214347891a) [#41072](https://github.com/sgl-project/sglang/pull/41072)
  [Bugfix] Skip post-experts EP all-reduce on the FlashInfer cutlass FP4 all-gather MoE path (#41072)
  _Files: `python/sglang/srt/layers/moe/utils.py`, `test/registered/kernels/ops/moe/test_fp4_allgather_moe_reduction.py`, `test/registered/unit/layer_boundary/test_moe_output_reduction.py`, `test/registered/unit/layer_boundary/test_reduction_fusion.py`_
- **2026-10-08** [`33883a5fa3`](https://github.com/sgl-project/sglang/commit/33883a5fa3) [#41134](https://github.com/sgl-project/sglang/pull/41134)
  [AMD] Small-M W8A8 FP8 projection GEMM for Qwen3.5 AttnFP8 on gfx950 (#41134)
  _Files: `python/sglang/kernels/ops/attention/fla/layernorm_gated.py`, `python/sglang/kernels/ops/elementwise/elementwise.py`, `python/sglang/kernels/ops/gemm/smallm_fp8_gfx950/__init__.py`, `python/sglang/kernels/ops/gemm/smallm_fp8_gfx950/smallm_fp8_gemm.hip` _+5 more__
- **2026-10-08** [`b2cd65b8b0`](https://github.com/sgl-project/sglang/commit/b2cd65b8b0) [#41133](https://github.com/sgl-project/sglang/pull/41133)
  [AMD] One-launch small-M MoE router for Qwen3.5 on gfx950 (#41133)
  _Files: `python/sglang/kernels/ops/moe/smallm_router_gfx950/__init__.py`, `python/sglang/kernels/ops/moe/smallm_router_gfx950/smallm_router.hip`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/qwen2_moe.py` _+1 more__
- **2026-10-08** [`d1b751d958`](https://github.com/sgl-project/sglang/commit/d1b751d958) [#42963](https://github.com/sgl-project/sglang/pull/42963)
  [diffusion] refactor: inherit existing defaults instead of repeating overrides (#42963)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/diffusers_generic.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/lingbot_video_moe.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/pi05.py`, `python/sglang/multimodal_gen/runtime/layers/lora/linear.py` _+15 more__
- **2026-10-08** [`0c00bffc6f`](https://github.com/sgl-project/sglang/commit/0c00bffc6f) [#42843](https://github.com/sgl-project/sglang/pull/42843)
  [diffusion] refactor: deduplicate Qwen Image RoPE and SenseNova backbones (#42843)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`, `python/sglang/multimodal_gen/runtime/models/sensenova_u1/neo_unify/modeling_neo_chat.py`, `python/sglang/multimodal_gen/runtime/models/sensenova_u1/neo_unify/modeling_qwen3.py`, `python/sglang/multimodal_gen/runtime/models/sensenova_u1/neo_unify/modeling_qwen3_moe.py` _+2 more__
- **2026-10-07** [`5e12831cec`](https://github.com/sgl-project/sglang/commit/5e12831cec) [#42589](https://github.com/sgl-project/sglang/pull/42589)
  [Refactor] Load auxiliary and expert checkpoints using owner partitions (#42589)
  _Files: `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/quark/weights.py`, `python/sglang/srt/models/bailing_moe_linear.py` _+13 more__
- **2026-10-07** [`64c7f65eac`](https://github.com/sgl-project/sglang/commit/64c7f65eac) [#42588](https://github.com/sgl-project/sglang/pull/42588)
  [Refactor] Retain process groups in parallel linear layers (#42588)
  _Files: `python/sglang/multimodal_gen/test/single_test_file/test_encoder_fold_srt_2_gpu.py`, `python/sglang/multimodal_gen/test/single_test_file/test_encoder_fold_srt_linear_2_gpu.py`, `python/sglang/multimodal_gen/test/unit/test_qwen2_5vl_generation.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_vision_parallel_groups.py` _+51 more__
- **2026-10-07** [`267e34516c`](https://github.com/sgl-project/sglang/commit/267e34516c) [#42587](https://github.com/sgl-project/sglang/pull/42587)
  [Refactor] Select parallel groups for remaining model projections (#42587)
  _Files: `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/mova.py`, `python/sglang/srt/models/bailing_moe_v3.py` _+31 more__
- **2026-10-07** [`59740a728f`](https://github.com/sgl-project/sglang/commit/59740a728f) [#42484](https://github.com/sgl-project/sglang/pull/42484)
  [Refactor] Let MLA projections select their parallel group (#42484)
  _Files: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/dots3_common/modeling.py`, `python/sglang/srt/models/sarvam_moe.py` _+1 more__
- **2026-10-07** [`961d7290fe`](https://github.com/sgl-project/sglang/commit/961d7290fe) [#42468](https://github.com/sgl-project/sglang/pull/42468)
  [Refactor] Let model MLPs select their parallel group (#42468)
  _Files: `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_v3.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/dots3_common/modeling.py` _+11 more__
- **2026-10-07** [`4c5130ac5a`](https://github.com/sgl-project/sglang/commit/4c5130ac5a) [#42426](https://github.com/sgl-project/sglang/pull/42426)
  [Refactor] Let linear layers select their parallel group (#42426)
  _Files: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/clip.py` _+24 more__
- **2026-10-07** [`c0df52be2d`](https://github.com/sgl-project/sglang/commit/c0df52be2d) [#34540](https://github.com/sgl-project/sglang/pull/34540)
  [AMD] Fix Quark W4A4 MXFP4 MoE clamped-SwiGLU on the AITER path (#34540)
  _Files: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`_
- **2026-10-07** [`d7190b0122`](https://github.com/sgl-project/sglang/commit/d7190b0122) [#42239](https://github.com/sgl-project/sglang/pull/42239)
  [Perf] Accelerate DiffusionGemma with FA4 and CUDA graphs on Blackwell (#42239)
  _Files: `python/sglang/kernels/ops/activation/__init__.py`, `python/sglang/kernels/ops/activation/softcap.py`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dllm_kv_pack.py` _+39 more__
- **2026-10-07** [`7a4d6dfd2f`](https://github.com/sgl-project/sglang/commit/7a4d6dfd2f) [#42370](https://github.com/sgl-project/sglang/pull/42370)
  [diffusion] feat: name the quality tiers after what they guarantee (#42370)
  _Files: `docs/cookbook/diffusion/FLUX/FLUX.mdx`, `docs/cookbook/diffusion/JoyEcho/JoyEcho.mdx`, `docs/cookbook/diffusion/LingBot-World/LingBot-World-2.0.mdx`, `docs/cookbook/diffusion/LingBot-World/LingBot-World.mdx` _+61 more__
- **2026-10-06** [`3eec178e48`](https://github.com/sgl-project/sglang/commit/3eec178e48) [#42022](https://github.com/sgl-project/sglang/pull/42022)
  [Spec][MegaMoE] Let the speculative draft choose its own W4A4 MXFP4 MegaMoE MMA type (#42022)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/spec.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` _+6 more__
- **2026-10-06** [`730f1f3e5b`](https://github.com/sgl-project/sglang/commit/730f1f3e5b) [#42245](https://github.com/sgl-project/sglang/pull/42245)
  [DeepSeek-V4.1] Unify mHC into one state machine and drop medium-batch fusion variants (#42245)
  _Files: `python/sglang/kernels/jit/csrc/distributed/all_reduce_fusion.cuh`, `python/sglang/kernels/ops/communication/all_reduce_mhc.py`, `python/sglang/kernels/ops/communication/all_reduce_mhc_combine.py`, `python/sglang/kernels/ops/layernorm/hc_combine_norm.py` _+15 more__
- **2026-10-06** [`b563bbd597`](https://github.com/sgl-project/sglang/commit/b563bbd597) [#40671](https://github.com/sgl-project/sglang/pull/40671)
  [Fix] Don't let a failed deep_ep import-time check kill servers that never use DeepEP (#40671)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep_v2.py`, `test/registered/unit/layers/moe/test_deepep_import_guard.py`_
- **2026-10-06** [`fcbbefa82a`](https://github.com/sgl-project/sglang/commit/fcbbefa82a) [#42693](https://github.com/sgl-project/sglang/pull/42693)
  [GLM-5.3-Flash] Autotune MoE kernels at prefill sizes (#42693)
  _Files: `python/sglang/srt/models/glm5_next.py`_
- **2026-10-05** [`438d9d2074`](https://github.com/sgl-project/sglang/commit/438d9d2074) [#37261](https://github.com/sgl-project/sglang/pull/37261)
  [Feature] DeepEP v2: expanded (do_expand=True) prefill dispatch (#37261)
  _Files: `docs/src/snippets/configs/Qwen/qwen3.8.jsx`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`, `python/sglang/srt/arg_groups/moe_hook.py` _+13 more__

## Quantization  (23 commits)

- **2026-10-12** [`d434ea444d`](https://github.com/sgl-project/sglang/commit/d434ea444d) [#42159](https://github.com/sgl-project/sglang/pull/42159)
  [DSV4.1] Reduce eager Engram extend preparation (#42159)
  _Files: `python/sglang/kernels/ops/embeddings/engram_hash.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/engram.py`, `test/manual/quantization/test_engram_extend_hash.py`_
- **2026-10-11** [`586d98cc15`](https://github.com/sgl-project/sglang/commit/586d98cc15) [#43062](https://github.com/sgl-project/sglang/pull/43062)
  [Diffusion] Add ModelOpt FP8 checkpoint quantization for Pi0.5 (#43062)
  _Files: `python/sglang/multimodal_gen/runtime/models/vlas/pi05_core.py`, `python/sglang/multimodal_gen/runtime/models/vlas/pi05_policy.py`, `python/sglang/multimodal_gen/runtime/vla/pi05_quantization.py`, `python/sglang/multimodal_gen/test/unit/test_pi05_modelopt_fp8.py` _+2 more__
- **2026-10-10** [`ff19159e16`](https://github.com/sgl-project/sglang/commit/ff19159e16) [#41071](https://github.com/sgl-project/sglang/pull/41071)
  [AMD] Add an opt-in AITER CK blockscale GEMM for gfx942 block-FP8 linears (#41071)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-10-10** [`e35f60b9bc`](https://github.com/sgl-project/sglang/commit/e35f60b9bc) [#43318](https://github.com/sgl-project/sglang/pull/43318)
  [AMD][CI] Drop removed tp_rank/tp_size kwargs from small-M FP8 proj test (#43318)
  _Files: `test/registered/amd/test_smallm_fp8_proj_gfx950.py`_
- **2026-10-10** [`2ff3e6dce1`](https://github.com/sgl-project/sglang/commit/2ff3e6dce1) [#42604](https://github.com/sgl-project/sglang/pull/42604)
  [SM90] Use native block32 DeepGEMM for DeepSeek-V4.1 (#42604)
  _Files: `python/pyproject.toml`, `python/sglang/kernels/ops/gemm/fp8_kernel.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py` _+5 more__
- **2026-10-10** [`6acaf3374a`](https://github.com/sgl-project/sglang/commit/6acaf3374a) [#42810](https://github.com/sgl-project/sglang/pull/42810)
  [kernel] SwiGLU-OAI MXFP8 producer; move swizzled MXFP8 producers to ops/quantization (#42810)
  _Files: `python/sglang/kernels/kda_kernels/layernorm_modulate_triton.py`, `python/sglang/kernels/numerics.py`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py` _+15 more__
- **2026-10-09** [`2d38934493`](https://github.com/sgl-project/sglang/commit/2d38934493) [#42156](https://github.com/sgl-project/sglang/pull/42156)
  [DSv4.1] mxfp8 dispatch cache (#42156)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/mxfp8_dispatch_cache.py`, `test/manual/quantization/test_mxfp8_dispatch_cache.py`_
- **2026-10-09** [`4debae7534`](https://github.com/sgl-project/sglang/commit/4debae7534) [#41887](https://github.com/sgl-project/sglang/pull/41887)
  Add blackwell dual gemm fusion support for MLP (#41887)
  _Files: `python/sglang/kernels/ops/gemm/__init__.py`, `python/sglang/kernels/ops/gemm/cutedsl_dual_gemm.py`, `python/sglang/srt/layers/dual_gemm.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` _+5 more__
- **2026-10-09** [`23f890613e`](https://github.com/sgl-project/sglang/commit/23f890613e) [#43319](https://github.com/sgl-project/sglang/pull/43319)
  [AMD] Patch aiter's group32 MXFP8 GEMM masked-scale fix (#43319)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-09** [`e54f08c860`](https://github.com/sgl-project/sglang/commit/e54f08c860) [#39817](https://github.com/sgl-project/sglang/pull/39817)
  [XPU] Misc changes to support XPU (#39817)
  _Files: `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/hunyuan_v3_nextn.py` _+1 more__
- **2026-10-08** [`8ad24fb560`](https://github.com/sgl-project/sglang/commit/8ad24fb560) [#42927](https://github.com/sgl-project/sglang/pull/42927)
  [Perf] Cache compiled ModelOpt exclusion patterns (#42927)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`_
- **2026-10-08** [`2d26823f94`](https://github.com/sgl-project/sglang/commit/2d26823f94) [#42152](https://github.com/sgl-project/sglang/pull/42152)
  [AMD] Drop static input_scale on aiter per-token FP8 path (use dynamic per-token) (#42152)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `test/registered/amd/test_fp8_per_channel_detection.py`_
- **2026-10-08** [`2489bd1d2e`](https://github.com/sgl-project/sglang/commit/2489bd1d2e) [#42856](https://github.com/sgl-project/sglang/pull/42856)
  [diffusion] refactor: share ModelOpt checkpoint conversion I/O (#42856)
  _Files: `python/sglang/multimodal_gen/test/unit/test_modelopt_checkpoint_tools.py`, `python/sglang/multimodal_gen/tools/build_modelopt_fp8_transformer.py`, `python/sglang/multimodal_gen/tools/build_modelopt_nvfp4_transformer.py`, `python/sglang/multimodal_gen/tools/modelopt_checkpoint.py`_
- **2026-10-08** [`35608e48d1`](https://github.com/sgl-project/sglang/commit/35608e48d1) [#42964](https://github.com/sgl-project/sglang/pull/42964)
  [diffusion] refactor: reuse the single-process parallel test fixture (#42964)
  _Files: `python/sglang/multimodal_gen/test/unit/test_flux3_action.py`, `python/sglang/multimodal_gen/test/unit/test_mxfp8_online_gemm.py`_
- **2026-10-07** [`b83827ea02`](https://github.com/sgl-project/sglang/commit/b83827ea02) [#42585](https://github.com/sgl-project/sglang/pull/42585)
  [Fix] Quantize reloaded FP8 weights after native sharding (#42585)
  _Files: `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/model_loader/weight_utils.py` _+4 more__
- **2026-10-07** [`00b21d6415`](https://github.com/sgl-project/sglang/commit/00b21d6415) [#42437](https://github.com/sgl-project/sglang/pull/42437)
  [diffusion] fix: reset DiT cache state at the start of each request (#42437)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_denoising_cache_reset.py`, `python/sglang/multimodal_gen/test/unit/test_flux2_fp8_norm_quant_gate.py`, `python/sglang/multimodal_gen/test/unit/test_kandinsky6_pipeline_contract.py` _+2 more__
- **2026-10-07** [`aa5551d9b6`](https://github.com/sgl-project/sglang/commit/aa5551d9b6) [#38028](https://github.com/sgl-project/sglang/pull/38028)
  [diffusion] fix: do not interleave comfy-kitchen MXFP8 scales twice (#38028)
  _Files: `python/sglang/multimodal_gen/runtime/layers/quantization/mxfp8.py`, `python/sglang/multimodal_gen/test/unit/test_transformer_quant.py`_
- **2026-10-07** [`9ddbba50dd`](https://github.com/sgl-project/sglang/commit/9ddbba50dd) [#39923](https://github.com/sgl-project/sglang/pull/39923)
  [AMD][DSV4] feat: enable PCP with fp8 unified_kv on gfx950 (#39923)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/models/test_deepseek_v4_cp_kv_store.py`, `test/registered/unit/models/test_deepseek_v4_unified_fp8_q_pair.py` _+1 more__
- **2026-10-07** [`168458fd90`](https://github.com/sgl-project/sglang/commit/168458fd90) [#42796](https://github.com/sgl-project/sglang/pull/42796)
  [AMD][V4.1] Fix wo_b input flatten for packed fp8 activations on gfx950 (#42796)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-06** [`0a0fe001f1`](https://github.com/sgl-project/sglang/commit/0a0fe001f1) [#41765](https://github.com/sgl-project/sglang/pull/41765)
  fix: route Thor SM110 FP8 and ModelOpt NVFP4 auto backends (#41765)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/utils/common.py`_
- **2026-10-06** [`2579875b5d`](https://github.com/sgl-project/sglang/commit/2579875b5d) [#42556](https://github.com/sgl-project/sglang/pull/42556)
  [diffusion] feat: support loading community ComfyUI-GGUF Qwen-Image-2.1 transformers (#42556)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image21.py` _+1 more__
- **2026-10-06** [`f3b5a28f43`](https://github.com/sgl-project/sglang/commit/f3b5a28f43) [#42605](https://github.com/sgl-project/sglang/pull/42605)
  [AMD] M3-mxfp8 Nightly Test Update (#42605)
  _Files: `test/registered/amd/accuracy/mi35x/test_minimax_m3_tp4_eval_mi35x.py`_
- **2026-10-06** [`542addad32`](https://github.com/sgl-project/sglang/commit/542addad32) [#42602](https://github.com/sgl-project/sglang/pull/42602)
  [AMD] M3-MXFP4 Nightly Test (#42602)
  _Files: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_minimax_m3_mxfp4_tp4_eval_mi35x.py`_

## Other  (20 commits)

- **2026-10-12** [`296774da37`](https://github.com/sgl-project/sglang/commit/296774da37) [#43104](https://github.com/sgl-project/sglang/pull/43104)
  [Tokenizer] Require fastokens>=0.3.2 and include it in the all extra (#43104)
  _Files: `python/pyproject.toml`_
- **2026-10-12** [`cd8ed1bb55`](https://github.com/sgl-project/sglang/commit/cd8ed1bb55) [#43398](https://github.com/sgl-project/sglang/pull/43398)
  [Bugfix] Preserve available host memory for integrated MUSA devices (#43398)
  _Files: `python/sglang/srt/utils/common.py`, `test/registered/unit/platforms/test_platform_interface.py`_
- **2026-10-12** [`95ce9caaf2`](https://github.com/sgl-project/sglang/commit/95ce9caaf2) [#43724](https://github.com/sgl-project/sglang/pull/43724)
  [Rust] Lock hyper 1.12.0 and want 0.3.2 in the rust workspace (#43724)
  _Files: `rust/Cargo.lock`_
- **2026-10-12** [`3c74f68a9c`](https://github.com/sgl-project/sglang/commit/3c74f68a9c) [#43702](https://github.com/sgl-project/sglang/pull/43702)
  [Fix] Initialize BF16 GEMM dispatch in the one-batch benchmark (#43702)
  _Files: `python/sglang/benchmark/one_batch.py`_
- **2026-10-11** [`d26b6a5a9c`](https://github.com/sgl-project/sglang/commit/d26b6a5a9c) [#35292](https://github.com/sgl-project/sglang/pull/35292)
  fix: default Inkling to fa4 on Hopper (#35292)
  _Files: `python/sglang/srt/arg_groups/model_overrides/inkling.py`_
- **2026-10-11** [`41652225d0`](https://github.com/sgl-project/sglang/commit/41652225d0) [#43346](https://github.com/sgl-project/sglang/pull/43346)
  [Sampler] Sort only the max(top_k) leading columns in the torch sampler (#43346)
  _Files: `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/sampling/sampling_batch_info.py`, `test/registered/sampling/test_sampling_mask.py`, `test/registered/unit/sampling/test_sampling_batch_info.py` _+1 more__
- **2026-10-11** [`89e24e7a20`](https://github.com/sgl-project/sglang/commit/89e24e7a20) [#43286](https://github.com/sgl-project/sglang/pull/43286)
  [KV canary] Expect sweep counters on the target runner only (#43286)
  _Files: `python/sglang/srt/kv_canary/runner/canary_manager.py`, `python/sglang/srt/kv_canary/runner/health_checker.py`, `python/sglang/test/kv_canary/runner_test_base.py`, `test/registered/kv_canary/test_self_unit_runner_health.py`_
- **2026-10-10** [`a956aa192a`](https://github.com/sgl-project/sglang/commit/a956aa192a) [#43457](https://github.com/sgl-project/sglang/pull/43457)
  [Refactor] Bind a layer stack in one pass over each stage's data flow (#43457)
  _Files: `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/factories.py`, `test/registered/unit/layer_boundary/test_independent_stage_construction.py`, `test/registered/unit/layer_boundary/test_nemotron_h_stages.py`_
- **2026-10-09** [`888de24cc8`](https://github.com/sgl-project/sglang/commit/888de24cc8) [#43321](https://github.com/sgl-project/sglang/pull/43321)
  Add BJWang-ant to CI_Permission (#43321)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-10-09** [`9172a73725`](https://github.com/sgl-project/sglang/commit/9172a73725) [#43232](https://github.com/sgl-project/sglang/pull/43232)
  [sgl-router] Keep charset=utf-8 on streamed responses (#43232)
  _Files: `experimental/sgl-router/src/proxy/mod.rs`, `experimental/sgl-router/tests/proxy/chat_routing.rs`, `experimental/sgl-router/tests/proxy/generate_routing.rs`_
- **2026-10-08** [`00b3a48753`](https://github.com/sgl-project/sglang/commit/00b3a48753) [#31773](https://github.com/sgl-project/sglang/pull/31773)
  [dLLM] Add JointThresholdInDel algorithm for insertion & deletion decoding (#31773)
  _Files: `python/sglang/srt/dllm/algorithm/joint_threshold_indel.py`, `python/sglang/srt/dllm/config.py`, `test/registered/unit/dllm/algorithm/test_joint_threshold_indel.py`_
- **2026-10-08** [`b2cb24995d`](https://github.com/sgl-project/sglang/commit/b2cb24995d) [#42690](https://github.com/sgl-project/sglang/pull/42690)
  [Debug] Add opt-in NaN detection before sampling (#42690)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/utils/async_probe.py`, `python/sglang/srt/utils/invariants.py`_
- **2026-10-07** [`c721602ad2`](https://github.com/sgl-project/sglang/commit/c721602ad2) [#39839](https://github.com/sgl-project/sglang/pull/39839)
  Cover SWA admission after declined HiCache restores (#39839)
  _Files: `test/registered/unit/managers/test_prefill_adder.py`_
- **2026-10-07** [`8f1790f595`](https://github.com/sgl-project/sglang/commit/8f1790f595) [#42826](https://github.com/sgl-project/sglang/pull/42826)
  Add Rust code owners and grant shodoco CI permissions (#42826)
  _Files: `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS`_
- **2026-10-06** [`a34cba3c62`](https://github.com/sgl-project/sglang/commit/a34cba3c62) [#42754](https://github.com/sgl-project/sglang/pull/42754)
  [HiCache] Resolve write_back to write_through under buffer_only host memory (#42754)
  _Files: `python/sglang/srt/arg_groups/hicache_hook.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-10-06** [`05340e9ecb`](https://github.com/sgl-project/sglang/commit/05340e9ecb) [#42629](https://github.com/sgl-project/sglang/pull/42629)
  [sgl-router] Make one request dispatchable more than once (retry 2/5) (#42629)
  _Files: `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/src/server/routes/chat/forward.rs`, `experimental/sgl-router/src/server/routes/chat/preparation.rs`_
- **2026-10-06** [`8c273d6813`](https://github.com/sgl-project/sglang/commit/8c273d6813) [#42628](https://github.com/sgl-project/sglang/pull/42628)
  [sgl-router] Let selection skip workers a request already failed on (retry 1/5) (#42628)
  _Files: `experimental/sgl-router/src/buckets_reorg.rs`, `experimental/sgl-router/src/policies/registry.rs`, `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/src/server/routes/chat/reorg.rs` _+1 more__
- **2026-10-06** [`40fb5935c0`](https://github.com/sgl-project/sglang/commit/40fb5935c0) [#36410](https://github.com/sgl-project/sglang/pull/36410)
  Allow platforms to declare Mamba extra-buffer support (#36410)
  _Files: `python/sglang/srt/arg_groups/mamba_hook.py`, `python/sglang/srt/platforms/interface.py`, `test/registered/unit/platforms/test_platform_interface.py`, `test/registered/unit/server_args/test_mamba_extra_buffer_platform.py`_
- **2026-10-06** [`9a09b48da7`](https://github.com/sgl-project/sglang/commit/9a09b48da7) [#42723](https://github.com/sgl-project/sglang/pull/42723)
  [Fix] Add `maybe_hand_to_session` to the one-batch benchmark `TreeCacheNamespace` (#42723)
  _Files: `python/sglang/benchmark/one_batch.py`_
- **2026-10-05** [`ab4f8a44f4`](https://github.com/sgl-project/sglang/commit/ab4f8a44f4) [#42572](https://github.com/sgl-project/sglang/pull/42572)
  [sgl-router] Point the design doc at the shared engine ranking (#42572)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`_

## Tensor / Data Parallel  (18 commits)

- **2026-10-11** [`ad8b1e1f85`](https://github.com/sgl-project/sglang/commit/ad8b1e1f85) [#43285](https://github.com/sgl-project/sglang/pull/43285)
  [Test] Do not hang scripted-runtime teardown when the server died (#43285)
  _Files: `python/sglang/test/scripted_runtime/http_server.py`_
- **2026-10-10** [`b0dde87de2`](https://github.com/sgl-project/sglang/commit/b0dde87de2) [#43455](https://github.com/sgl-project/sglang/pull/43455)
  [Refactor] Make residual read and update capabilities explicit and checked (#43455)
  _Files: `python/sglang/srt/layers/layer_boundary/boundary.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/exit.py`, `python/sglang/srt/layers/layer_boundary/factories.py` _+15 more__
- **2026-10-10** [`514feb1afc`](https://github.com/sgl-project/sglang/commit/514feb1afc) [#43454](https://github.com/sgl-project/sglang/pull/43454)
  [Fix] Keep residual rows and sums consistent across appends and pipeline handoffs (#43454)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/layer_boundary/boundary.py`, `python/sglang/srt/layers/layer_boundary/factories.py`, `python/sglang/srt/layers/layer_boundary/residual/batch.py` _+9 more__
- **2026-10-09** [`8020ea2ee9`](https://github.com/sgl-project/sglang/commit/8020ea2ee9) [#43284](https://github.com/sgl-project/sglang/pull/43284)
  [MLX] Drop a retracted request's runner state at its re-prefill (#43284)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `test/registered/unit/hardware_backend/mlx/test_tp_worker_routing.py`_
- **2026-10-09** [`66d840a8ef`](https://github.com/sgl-project/sglang/commit/66d840a8ef) [#43303](https://github.com/sgl-project/sglang/pull/43303)
  [cuda_graph] Size dp-local decode graphs by the runner's own gather requirement (#43303)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/model_executor/runner/base_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/base_runner.py` _+4 more__
- **2026-10-09** [`7203747cc8`](https://github.com/sgl-project/sglang/commit/7203747cc8) [#42895](https://github.com/sgl-project/sglang/pull/42895)
  [Fix] Shard Kimi K3's shared experts over the TP group they sum over (#42895)
  _Files: `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/layers/test_kimi_mlp_parallel_groups.py`_
- **2026-10-09** [`f620d733d2`](https://github.com/sgl-project/sglang/commit/f620d733d2) [#42996](https://github.com/sgl-project/sglang/pull/42996)
  [rust-processor] Share the reasoning splitter and tool constraint across hosts (#42996)
  _Files: `rust/sglang-processor/README.md`, `rust/sglang-processor/src/lib.rs`, `rust/sglang-processor/src/parser/aliases.rs`, `rust/sglang-processor/src/parser/mod.rs` _+7 more__
- **2026-10-09** [`e0608d890e`](https://github.com/sgl-project/sglang/commit/e0608d890e) [#43041](https://github.com/sgl-project/sglang/pull/43041)
  fix: use dp_size instead of attn_dp_size for msprobe rank id (#43041)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-10-09** [`cba1d07a94`](https://github.com/sgl-project/sglang/commit/cba1d07a94) [#43176](https://github.com/sgl-project/sglang/pull/43176)
  [Memory] Share one full prefill graph output buffer across shapes for tuple and list outputs (#43176)
  _Files: `python/sglang/srt/model_executor/runner_backend/full_cuda_graph_backend.py`, `test/registered/unit/model_executor/runner_backend/test_full_cuda_graph_backend.py`_
- **2026-10-09** [`3e13f1b2c7`](https://github.com/sgl-project/sglang/commit/3e13f1b2c7) [#42889](https://github.com/sgl-project/sglang/pull/42889)
  [Perf] Serialize OpenAI chat/completion responses in one pass (#42889)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/utils/json_response.py`, `test/registered/unit/utils/test_json_response.py`_
- **2026-10-08** [`20bf93b6bf`](https://github.com/sgl-project/sglang/commit/20bf93b6bf) [#43218](https://github.com/sgl-project/sglang/pull/43218)
  [metrics] Call DPBalanceStats.create by keyword in the ratio ladder test (#43218)
  _Files: `test/registered/unit/observability/test_forward_pass_metrics.py`_
- **2026-10-08** [`3d8d44a4a9`](https://github.com/sgl-project/sglang/commit/3d8d44a4a9) [#39723](https://github.com/sgl-project/sglang/pull/39723)
  [Qwen3.8 CP 3/4] Collocated prefill CP integration (#39723)
  _Files: `python/sglang/srt/arg_groups/cp_tp_group_sharing_hook.py`, `python/sglang/srt/arg_groups/fields/parallel.py`, `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/configs/qwen3_next.py` _+5 more__
- **2026-10-08** [`5a5ea81036`](https://github.com/sgl-project/sglang/commit/5a5ea81036) [#43004](https://github.com/sgl-project/sglang/pull/43004)
  [rust-server] warm up each rust listener in-process (#43004)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `rust/sglang-server/src/api_server/core/handle.rs`, `rust/sglang-server/src/api_server/http/app.rs`, `rust/sglang-server/src/utils/runtime.rs`_
- **2026-10-08** [`1638c5d699`](https://github.com/sgl-project/sglang/commit/1638c5d699) [#43114](https://github.com/sgl-project/sglang/pull/43114)
  [http_server] Let custom /generate routes skip the second contract check (#43114)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `test/registered/unit/entrypoints/test_generate_api_contract.py`_
- **2026-10-06** [`6b737fd4c6`](https://github.com/sgl-project/sglang/commit/6b737fd4c6) [#42695](https://github.com/sgl-project/sglang/pull/42695)
  Bind the MessageQueue remote socket atomically (#42695)
  _Files: `python/sglang/srt/distributed/device_communicators/shm_broadcast.py`_
- **2026-10-06** [`c76faa1ff2`](https://github.com/sgl-project/sglang/commit/c76faa1ff2) [#42613](https://github.com/sgl-project/sglang/pull/42613)
  docs(cookbook): enable Top-K v2 for GLM-5.2 MI355X MTP (#42613)
  _Files: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-10-05** [`08fa37e48d`](https://github.com/sgl-project/sglang/commit/08fa37e48d) [#42429](https://github.com/sgl-project/sglang/pull/42429)
  [sgl-router] Add reorg bucket config with per-group admission (#42429)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/buckets_reorg.rs`, `experimental/sgl-router/src/config/cli.rs` _+36 more__
- **2026-10-05** [`a96b146491`](https://github.com/sgl-project/sglang/commit/a96b146491) [#42428](https://github.com/sgl-project/sglang/pull/42428)
  [sgl-router] Move pressure and prefix signals out of legacy policies (#42428)
  _Files: `experimental/sgl-router/src/main.rs`, `experimental/sgl-router/src/policies/admission.rs`, `experimental/sgl-router/src/policies/cache_aware.rs`, `experimental/sgl-router/src/policies/decode.rs` _+19 more__

## Triton / Kernels  (17 commits)

- **2026-10-12** [`a0e6effe50`](https://github.com/sgl-project/sglang/commit/a0e6effe50) [#43764](https://github.com/sgl-project/sglang/pull/43764)
  [Fix] Link cuda_ipc JIT against CUDA driver stubs dir (#43764)
  _Files: `python/sglang/kernels/ops/communication/all_reduce.py`_
- **2026-10-11** [`efd14cfb66`](https://github.com/sgl-project/sglang/commit/efd14cfb66) [#43070](https://github.com/sgl-project/sglang/pull/43070)
  [DeepSeek-V4.1] Use num_stages=1 for the hc_mix stats partial kernel (#43070)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`_
- **2026-10-11** [`d32d8fa0d1`](https://github.com/sgl-project/sglang/commit/d32d8fa0d1) [#42808](https://github.com/sgl-project/sglang/pull/42808)
  [Dsv4.1] Mega-mhc integration (#42808)
  _Files: `python/sglang/kernels/ops/layernorm/mhc_mega.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_mhc.py`_
- **2026-10-10** [`33f6b00f32`](https://github.com/sgl-project/sglang/commit/33f6b00f32) [#43172](https://github.com/sgl-project/sglang/pull/43172)
  Clamp default decode CUDA graph max_bs to max_running_requests (#43172)
  _Files: `python/sglang/srt/arg_groups/memory_hook.py`_
- **2026-10-09** [`58f6976ce7`](https://github.com/sgl-project/sglang/commit/58f6976ce7) [#43211](https://github.com/sgl-project/sglang/pull/43211)
  [Fix] Unblock CUDA graph startup for hybrid parallelism (#43211)
  _Files: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/unit/layers/deep_gemm_wrapper/test_warmup_memory.py`, `test/registered/unit/model_executor/test_prefill_cuda_graph_runner_helpers.py`_
- **2026-10-09** [`5cbf949839`](https://github.com/sgl-project/sglang/commit/5cbf949839) [#43384](https://github.com/sgl-project/sglang/pull/43384)
  Fix torch.compile crash in fused gate-sigmoid-mul launcher (#43384)
  _Files: `python/sglang/kernels/ops/elementwise/elementwise.py`_
- **2026-10-09** [`e1c6ddca1d`](https://github.com/sgl-project/sglang/commit/e1c6ddca1d) [#43340](https://github.com/sgl-project/sglang/pull/43340)
  [NPU] Bump SGLANG_KERNEL_NPU_TAG to 2026.9.0.post9 (#43340)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `docker/npu.Dockerfile`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-10-09** [`666da4f56b`](https://github.com/sgl-project/sglang/commit/666da4f56b) [#42893](https://github.com/sgl-project/sglang/pull/42893)
  [Fix] Kimi K3 KDA value head size and SiTU input alignment (#42893)
  _Files: `python/sglang/kernels/ops/activation/_jit_situ_and_mul.py`, `python/sglang/srt/models/kimi_k3.py`_
- **2026-10-09** [`438df9a2a4`](https://github.com/sgl-project/sglang/commit/438df9a2a4) [#42709](https://github.com/sgl-project/sglang/pull/42709)
  [Spec] Fix wrong tokens from compact-verify CUDA graphs when a token tier is captured more than once (#42709)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `test/registered/unit/model_executor/runner/test_decode_cuda_graph_runner.py`_
- **2026-10-08** [`2e64740442`](https://github.com/sgl-project/sglang/commit/2e64740442) [#43229](https://github.com/sgl-project/sglang/pull/43229)
  [CI] Avoid Hugging Face Hub API calls when the local model cache is complete (#43229)
  _Files: `python/sglang/srt/model_loader/ci_weight_validation.py`, `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/utils/common.py`, `python/sglang/test/test_utils.py` _+2 more__
- **2026-10-08** [`9f5d871251`](https://github.com/sgl-project/sglang/commit/9f5d871251) [#43035](https://github.com/sgl-project/sglang/pull/43035)
  [NPU] Quote the arm64 Triton-ascend wheel URL in npu.Dockerfile (#43035)
  _Files: `docker/npu.Dockerfile`_
- **2026-10-08** [`54b551df8e`](https://github.com/sgl-project/sglang/commit/54b551df8e) [#42286](https://github.com/sgl-project/sglang/pull/42286)
  [Refactor][TCPCG] Bind live forward batches in BCG eager calls (2/9) (#42286)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_backend/breakable_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_backend_utils/breakable_cuda_graph/breakable_cuda_graph.py`, `python/sglang/srt/model_executor/runner_utils/forward_batch.py` _+1 more__
- **2026-10-08** [`0f5bc4af4b`](https://github.com/sgl-project/sglang/commit/0f5bc4af4b) [#43056](https://github.com/sgl-project/sglang/pull/43056)
  [CI] Fix stale fakes in the NPU CUDA-graph backend unit test (#43056)
  _Files: `test/registered/unit/npu/graph_runner/test_npu_cudagraph_backend.py`_
- **2026-10-08** [`89bea053ac`](https://github.com/sgl-project/sglang/commit/89bea053ac) [#40404](https://github.com/sgl-project/sglang/pull/40404)
  [NPU] Add NPU cudagraph runner unit tests (#40404)
  _Files: `test/registered/unit/npu/graph_runner/test_npu_cudagraph_backend.py`, `test/registered/unit/npu/graph_runner/test_npu_graph_capture.py`, `test/registered/unit/npu/graph_runner/test_npu_graph_runner.py`_
- **2026-10-08** [`0427ea8032`](https://github.com/sgl-project/sglang/commit/0427ea8032) [#43024](https://github.com/sgl-project/sglang/pull/43024)
  [CI] Split the shared Cargo target dir per glibc (#43024)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-10-07** [`f47d89564d`](https://github.com/sgl-project/sglang/commit/f47d89564d) [#42905](https://github.com/sgl-project/sglang/pull/42905)
  [KDA] Default GLM-5-Next spec verify to the CuTe DSL KDA kernel (#42905)
  _Files: `python/sglang/srt/arg_groups/glm5_next_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`_
- **2026-10-07** [`2f6e0ec45d`](https://github.com/sgl-project/sglang/commit/2f6e0ec45d) [#41704](https://github.com/sgl-project/sglang/pull/41704)
  [DSv4.1] Trim prefill model-entry overhead (#41704)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`, `python/sglang/srt/layers/engram.py`, `python/sglang/srt/models/deepseek_v4.py`_

## CI / Build  (16 commits)

- **2026-10-12** [`8afe107c24`](https://github.com/sgl-project/sglang/commit/8afe107c24) [#42003](https://github.com/sgl-project/sglang/pull/42003)
  [XPU] Upgrade XPU backend to PyTorch 2.14 (#42003)
  _Files: `docker/xpu.Dockerfile`, `docs/docs/hardware-platforms/xpu.mdx`, `python/pyproject_xpu.toml`_
- **2026-10-12** [`8ce76b88df`](https://github.com/sgl-project/sglang/commit/8ce76b88df) [#42048](https://github.com/sgl-project/sglang/pull/42048)
  [XPU CI] Optimize PR CI per-file timeouts and fail hanging tests fast (#42048)
  _Files: `.github/workflows/pr-test-xpu.yml`, `python/sglang/test/ci/ci_utils.py`, `test/run_suite.py`_
- **2026-10-10** [`c55790d38b`](https://github.com/sgl-project/sglang/commit/c55790d38b) [#43503](https://github.com/sgl-project/sglang/pull/43503)
  [CI] Drop CPU tests with no bug-catching signal and run Rust workspace tests in their own workflow (#43503)
- **2026-10-08** [`d8448d2e62`](https://github.com/sgl-project/sglang/commit/d8448d2e62) [#43058](https://github.com/sgl-project/sglang/pull/43058)
  [CI] Re-enable GB300 (#43058)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/release-whl-deepgemm.yml`, `.github/workflows/rerun-test.yml` _+1 more__
- **2026-10-08** [`cbf49695c3`](https://github.com/sgl-project/sglang/commit/cbf49695c3) [#43022](https://github.com/sgl-project/sglang/pull/43022)
  [CI] Add dedicated sglang-processor workflow (#43022)
  _Files: `.github/workflows/pr-test-sgl-processor.yml`_
- **2026-10-08** [`9578cb1c63`](https://github.com/sgl-project/sglang/commit/9578cb1c63) [#43025](https://github.com/sgl-project/sglang/pull/43025)
  [CI] Don't run the full GPU suite for renderer-only Cargo.lock changes (#43025)
  _Files: `.github/workflows/_pr-test-check-changes.yml`_
- **2026-10-08** [`4b384df0c9`](https://github.com/sgl-project/sglang/commit/4b384df0c9) [#43068](https://github.com/sgl-project/sglang/pull/43068)
  [CI] Keep the KL tests' LongBench cache outside the checkout and bound its download (#43068)
  _Files: `python/sglang/test/kl_test_utils.py`_
- **2026-10-08** [`f795fe352d`](https://github.com/sgl-project/sglang/commit/f795fe352d) [#38520](https://github.com/sgl-project/sglang/pull/38520)
  [Test] Add a docs drift check for server_arguments.mdx (#38520)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/_pr-test-stage-cpu.yml`, `docs/.mintignore`, `docs/docs/advanced_features/server_arguments.mdx` _+2 more__
- **2026-10-08** [`ac656ee79a`](https://github.com/sgl-project/sglang/commit/ac656ee79a) [#42959](https://github.com/sgl-project/sglang/pull/42959)
  [CI] Re-enable B300 (#42959)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/rerun-test.yml`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-10-07** [`f497b626b6`](https://github.com/sgl-project/sglang/commit/f497b626b6) [#42827](https://github.com/sgl-project/sglang/pull/42827)
  build: use one DeepEP ref for implementation and packaging (#42827)
  _Files: `.github/workflows/release-whl-deepep.yml`, `docker/Dockerfile.cu134`, `docs/docs/developer_guide/contribution_guide.mdx`, `scripts/build_sgl_deepep.sh`_
- **2026-10-06** [`44a2558d40`](https://github.com/sgl-project/sglang/commit/44a2558d40) [#42661](https://github.com/sgl-project/sglang/pull/42661)
  [NVIDIA] Fix nightly-cu134 build and update (#42661)
  _Files: `docker/Dockerfile.cu134`_
- **2026-10-06** [`0f57a39152`](https://github.com/sgl-project/sglang/commit/0f57a39152) [#42663](https://github.com/sgl-project/sglang/pull/42663)
  [rust-processor] Gate render, tokenizer and parser behind cargo features (#42663)
  _Files: `docker/renderer.Dockerfile`, `rust/sglang-processor/Cargo.toml`, `rust/sglang-processor/README.md`, `rust/sglang-processor/src/lib.rs` _+1 more__
- **2026-10-06** [`60878c3fba`](https://github.com/sgl-project/sglang/commit/60878c3fba) [#42704](https://github.com/sgl-project/sglang/pull/42704)
  [CI] Temporarily disable B300 (#42704)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/rerun-test.yml`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-10-06** [`4409d2fd22`](https://github.com/sgl-project/sglang/commit/4409d2fd22) [#40923](https://github.com/sgl-project/sglang/pull/40923)
  [ci] add renderer automatic labeler (#40923)
  _Files: `.github/labeler.yml`_
- **2026-10-05** [`1818db4e54`](https://github.com/sgl-project/sglang/commit/1818db4e54) [#42543](https://github.com/sgl-project/sglang/pull/42543)
  [CI] Drop the echoed command from /rerun-test result replies (#42543)
  _Files: `.agents/skills/ci-workflow-guide/SKILL.md`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-10-05** [`b1bbd74f28`](https://github.com/sgl-project/sglang/commit/b1bbd74f28) [#41634](https://github.com/sgl-project/sglang/pull/41634)
  [XPU][CI] Disable test_xpu_graph until tc_piecewise is removed (#41634) (#42524)
  _Files: `test/registered/xpu/test_xpu_graph.py`_

## Scheduler / Batching  (15 commits)

- **2026-10-12** [`28621739fc`](https://github.com/sgl-project/sglang/commit/28621739fc) [#41911](https://github.com/sgl-project/sglang/pull/41911)
  [Fix] Make tokenizer request-state initialization atomic (#41911)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
- **2026-10-12** [`2240049194`](https://github.com/sgl-project/sglang/commit/2240049194) [#43758](https://github.com/sgl-project/sglang/pull/43758)
  [RL] Return a failed weight update when the cache flush is refused (#43758)
  _Files: `python/sglang/srt/managers/scheduler_components/weight_updater.py`_
- **2026-10-12** [`a297cd3da1`](https://github.com/sgl-project/sglang/commit/a297cd3da1) [#41872](https://github.com/sgl-project/sglang/pull/41872)
  [Fix] scheduler: stop latching batch_is_full when nothing can run (#41872)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_batch_is_full_latch.py`_
- **2026-10-11** [`cf88ed4352`](https://github.com/sgl-project/sglang/commit/cf88ed4352) [#35721](https://github.com/sgl-project/sglang/pull/35721)
  [BugFix][DP] Prevent health checks from perturbing user request routing (#35721)
  _Files: `python/sglang/srt/managers/data_parallel_controller.py`, `test/registered/unit/managers/test_data_parallel_controller.py`_
- **2026-10-11** [`0a21a3b798`](https://github.com/sgl-project/sglang/commit/0a21a3b798) [#43283](https://github.com/sgl-project/sglang/pull/43283)
  [Scheduler] Keep a DP-converted decode batch as the running batch (#43283)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_dp_converted_batch_full.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_
- **2026-10-11** [`448759b235`](https://github.com/sgl-project/sglang/commit/448759b235) [#43298](https://github.com/sgl-project/sglang/pull/43298)
  [Scheduler] Requeue preempted requests when admission admits nothing (#43298)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/scheduler/test_priority_scheduling.py`_
- **2026-10-10** [`44bc478863`](https://github.com/sgl-project/sglang/commit/44bc478863) [#41446](https://github.com/sgl-project/sglang/pull/41446)
  [HiSparse] Avoid host synchronization in eager backup (#41446)
  _Files: `python/sglang/srt/managers/hisparse_coordinator.py`_
- **2026-10-10** [`7d44269907`](https://github.com/sgl-project/sglang/commit/7d44269907) [#43474](https://github.com/sgl-project/sglang/pull/43474)
  [MemCache] Fix the strict busy check on prefill-aware SWA and tidy small leftovers (#43474)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/managers/scheduler_components/pool_stats_observer.py`, `test/registered/scheduler/test_retract_decode.py` _+1 more__
- **2026-10-09** [`46498bc8c5`](https://github.com/sgl-project/sglang/commit/46498bc8c5) [#43292](https://github.com/sgl-project/sglang/pull/43292)
  [MLX] Sync decode KV to the pool once at release, clamped to the owned prefix (#43292)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/hardware_backend/mlx/test_decode_kv_release.py` _+2 more__
- **2026-10-09** [`cb9bd1d4d4`](https://github.com/sgl-project/sglang/commit/cb9bd1d4d4) [#42238](https://github.com/sgl-project/sglang/pull/42238)
  [Perf] Reduce multi-detokenizer router IPC sends (#42238)
  _Files: `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `test/registered/unit/managers/test_multi_tokenizer_mixin.py`_
- **2026-10-09** [`3c612132fd`](https://github.com/sgl-project/sglang/commit/3c612132fd) [#43177](https://github.com/sgl-project/sglang/pull/43177)
  Overlap scheduler startup with the data parallel controller (#43177)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `test/registered/unit/managers/test_data_parallel_controller.py`_
- **2026-10-09** [`7859eff6ca`](https://github.com/sgl-project/sglang/commit/7859eff6ca) [#43181](https://github.com/sgl-project/sglang/pull/43181)
  [srt] Inject "__req__" into custom_params only for custom logit processors (#43181)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/sampling/sampling_params.py`, `test/registered/unit/managers/test_req_custom_params_ref.py`_
- **2026-10-08** [`393eaed509`](https://github.com/sgl-project/sglang/commit/393eaed509) [#34076](https://github.com/sgl-project/sglang/pull/34076)
  [Fix] overlap scheduler: record_stream mix_running_indices for the forward-stream relay gather (#34076)
  _Files: `python/sglang/srt/managers/overlap_utils.py`_
- **2026-10-06** [`90aa1cb0fb`](https://github.com/sgl-project/sglang/commit/90aa1cb0fb) [#42625](https://github.com/sgl-project/sglang/pull/42625)
  [Scheduler] Gather prefill-delayer queue timeout across ranks (#42625)
  _Files: `python/sglang/srt/managers/prefill_delayer.py`, `test/registered/unit/managers/test_prefill_delayer_gather.py`, `test/registered/unit/managers/test_prefill_delayer_high_watermark.py`_
- **2026-10-06** [`12004043b8`](https://github.com/sgl-project/sglang/commit/12004043b8) [#42797](https://github.com/sgl-project/sglang/pull/42797)
  [Metrics] Read scheduled prefill KV tokens from batch `prefix_lens` (#42797)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`_

## Docs / Examples  (14 commits)

- **2026-10-12** [`180933518e`](https://github.com/sgl-project/sglang/commit/180933518e) [#42316](https://github.com/sgl-project/sglang/pull/42316)
  [sgl-router] Serve the Anthropic Messages API on /v1/messages (#42316)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/lib.rs`, `experimental/sgl-router/src/protocol/anthropic/mod.rs`, `experimental/sgl-router/src/protocol/anthropic/request.rs` _+10 more__
- **2026-10-12** [`62c853b654`](https://github.com/sgl-project/sglang/commit/62c853b654) [#43787](https://github.com/sgl-project/sglang/pull/43787)
  docs: clarify prefill CP terminology and simplify wording (#43787)
  _Files: `docs/docs/advanced_features/prefill_cp.mdx`_
- **2026-10-12** [`f9bd83e7a9`](https://github.com/sgl-project/sglang/commit/f9bd83e7a9) [#43462](https://github.com/sgl-project/sglang/pull/43462)
  docs: sync LMSYS SGLang blog cards (#43462)
  _Files: `docs/index.mdx`_
- **2026-10-09** [`408f5d057a`](https://github.com/sgl-project/sglang/commit/408f5d057a) [#43349](https://github.com/sgl-project/sglang/pull/43349)
  docs: add Clef accuracy results to the deployment wizard (#43349)
  _Files: `docs/cookbook/autoregressive/Cloudflare/clef.mdx`, `docs/src/snippets/configs/Cloudflare/clef-benchmarks.jsx`, `docs/src/snippets/configs/Cloudflare/clef.jsx`_
- **2026-10-09** [`91b3692a4c`](https://github.com/sgl-project/sglang/commit/91b3692a4c) [#41601](https://github.com/sgl-project/sglang/pull/41601)
  docs: add thinking budget guide (#41601)
  _Files: `docs/docs.json`, `docs/docs/advanced_features/separate_reasoning.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/advanced_features/thinking_budget.mdx`_
- **2026-10-09** [`ff146fa20c`](https://github.com/sgl-project/sglang/commit/ff146fa20c) [#43336](https://github.com/sgl-project/sglang/pull/43336)
  [NPU] [DOC] remove --enable-torch-compile from Ascend support matrix (#43336)
  _Files: `docs/docs/hardware-platforms/ascend-npus/optimization/parameter_tuning.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`_
- **2026-10-09** [`c44a42e6d3`](https://github.com/sgl-project/sglang/commit/c44a42e6d3) [#43307](https://github.com/sgl-project/sglang/pull/43307)
  docs: reorder README workloads, hardware, and ecosystem (#43307)
  _Files: `README.md`_
- **2026-10-06** [`1291f3175d`](https://github.com/sgl-project/sglang/commit/1291f3175d) [#42756](https://github.com/sgl-project/sglang/pull/42756)
  [rust-processor] Fix chat-template precedence wording in the processor README (#42756)
  _Files: `rust/sglang-processor/README.md`_
- **2026-10-06** [`28525b43c4`](https://github.com/sgl-project/sglang/commit/28525b43c4) [#42751](https://github.com/sgl-project/sglang/pull/42751)
  [sgl-router] Document and reject a zero request timeout (#42751)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs` _+1 more__
- **2026-10-06** [`2167cf90c3`](https://github.com/sgl-project/sglang/commit/2167cf90c3) [#42632](https://github.com/sgl-project/sglang/pull/42632)
  [sgl-router] Bound streaming time-to-headers by --request-timeout-secs (retry 5/5) (#42632)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/proxy/mod.rs` _+1 more__
- **2026-10-06** [`662879e495`](https://github.com/sgl-project/sglang/commit/662879e495) [#42631](https://github.com/sgl-project/sglang/pull/42631)
  [sgl-router] Back off between retry attempts (retry 4/5) (#42631)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs` _+2 more__
- **2026-10-06** [`bb4d0a13c1`](https://github.com/sgl-project/sglang/commit/bb4d0a13c1) [#42630](https://github.com/sgl-project/sglang/pull/42630)
  [sgl-router] Retry failed dispatches on another worker (retry 3/5) (#42630)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs` _+8 more__
- **2026-10-06** [`f2f0be731c`](https://github.com/sgl-project/sglang/commit/f2f0be731c) [#42167](https://github.com/sgl-project/sglang/pull/42167)
  [Docs] GLM-5.2: move GB300 AgentX recipe to the agentic HiCache section and drop no-op settings (#42167)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-10-05** [`70f0b7351e`](https://github.com/sgl-project/sglang/commit/70f0b7351e) [#42545](https://github.com/sgl-project/sglang/pull/42545)
  [sgl-router] Improved policy balanced mode (#42545)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/buckets_reorg.rs`, `experimental/sgl-router/src/config/cli.rs` _+10 more__

## Speculative Decoding  (12 commits)

- **2026-10-11** [`e6072935bf`](https://github.com/sgl-project/sglang/commit/e6072935bf) [#43623](https://github.com/sgl-project/sglang/pull/43623)
  [DSpark] Apply `SGLANG_SIMULATE_ACC_LEN` inside the accept instead of switching paths (#43623)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_verify.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-10-11** [`a65b776963`](https://github.com/sgl-project/sglang/commit/a65b776963) [#43670](https://github.com/sgl-project/sglang/pull/43670)
  [DSpark] Add `SGLANG_DSPARK_USE_GREEDY_DRAFT`, an argmax draft accepted as one-hot (#43670)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_draft_model.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dspark_components/dspark_block_accept_estimator.py` _+8 more__
- **2026-10-11** [`3cc23b3b86`](https://github.com/sgl-project/sglang/commit/3cc23b3b86) [#43669](https://github.com/sgl-project/sglang/pull/43669)
  [DSpark] Merge the draft TP sync sites into `dspark-draft` (#43669)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py`, `python/sglang/srt/speculative/spec_tp_sync.py` _+2 more__
- **2026-10-11** [`00ba90fd1a`](https://github.com/sgl-project/sglang/commit/00ba90fd1a) [#43668](https://github.com/sgl-project/sglang/pull/43668)
  [DSpark] Run the same markov block in the draft graph tail; drop `SGLANG_DSPARK_FOLDED_SAMPLING` (#43668)
  _Files: `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`, `python/sglang/kernels/ops/speculative/dspark/dspark_draft_model.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4_dspark.py` _+9 more__
- **2026-10-11** [`48abbdb845`](https://github.com/sgl-project/sglang/commit/48abbdb845) [#43622](https://github.com/sgl-project/sglang/pull/43622)
  [DSpark] Draft the eager markov block through `MarkovSampleStep` (#43622)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4_dspark.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py` _+2 more__
- **2026-10-11** [`467209e838`](https://github.com/sgl-project/sglang/commit/467209e838) [#43621](https://github.com/sgl-project/sglang/pull/43621)
  [DSpark] Add `MarkovSampleStep`, one op for a markov draft step's add and token pick (#43621)
  _Files: `python/sglang/kernels/ops/speculative/dspark/markov_sample.py`, `python/sglang/kernels/ops/speculative/dspark/sharded_greedy.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4_dspark.py` _+1 more__
- **2026-10-11** [`9943cf8eef`](https://github.com/sgl-project/sglang/commit/9943cf8eef) [#43620](https://github.com/sgl-project/sglang/pull/43620)
  [DSpark] Run every markov head through one step interface (#43620)
  _Files: `python/sglang/srt/models/deepseek_v4_dspark.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py`_
- **2026-10-10** [`6e8f3e09dd`](https://github.com/sgl-project/sglang/commit/6e8f3e09dd) [#40453](https://github.com/sgl-project/sglang/pull/40453)
  [Model Loader] Add InstantTensor loader support (#40453)
  _Files: `docs/docs/advanced_features/model_loading.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/pyproject.toml`, `python/sglang/srt/arg_groups/choices.py` _+17 more__
- **2026-10-09** [`46c2585faa`](https://github.com/sgl-project/sglang/commit/46c2585faa) [#42987](https://github.com/sgl-project/sglang/pull/42987)
  [DSpark] Fold draft sampling for DeepSeek-V4.1 heads under AUTO (#42987)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py`, `test/registered/spec/dspark/test_dspark_draft_path_default.py`_
- **2026-10-08** [`5afe4d6334`](https://github.com/sgl-project/sglang/commit/5afe4d6334) [#42230](https://github.com/sgl-project/sglang/pull/42230)
  [AMD] Fix DSpark draft bucket tests for the raw in-graph metadata default (#42230)
  _Files: `test/registered/amd/test_dsv4_hip_bcg_metadata.py`_
- **2026-10-08** [`785005d21b`](https://github.com/sgl-project/sglang/commit/785005d21b) [#42624](https://github.com/sgl-project/sglang/pull/42624)
  [DSpark] Mask uncommitted slots before commit-inject cache lookups (#42624)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py`, `test/registered/spec/dspark/test_dspark_kernel_parity.py`_
- **2026-10-05** [`57826a62ea`](https://github.com/sgl-project/sglang/commit/57826a62ea) [#42297](https://github.com/sgl-project/sglang/pull/42297)
  [Speculative] Add opt-in block verification (#42297)
  _Files: `benchmark/kernels/bench_block_verification.py`, `docs/docs/advanced_features/speculative_decoding.mdx`, `python/sglang/kernels/ops/speculative/reject_sampling.py`, `python/sglang/srt/arg_groups/fields/spec.py` _+5 more__

## ROCm / AMD  (10 commits)

- **2026-10-10** [`a916d91cd3`](https://github.com/sgl-project/sglang/commit/a916d91cd3) [#43547](https://github.com/sgl-project/sglang/pull/43547)
  [AMD][CI] Cap pyarrow below 26 for lmms-eval (#43547)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-10-10** [`d7d22e8a30`](https://github.com/sgl-project/sglang/commit/d7d22e8a30) [#39840](https://github.com/sgl-project/sglang/pull/39840)
  [AMD] Resolving bug in per batch size graph capture due to multiple capture runs per batch size (#39840)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_backend/full_cuda_graph_backend.py`, `test/registered/unit/model_executor/runner/test_decode_cuda_graph_runner.py`_
- **2026-10-09** [`70e82f7b73`](https://github.com/sgl-project/sglang/commit/70e82f7b73) [#43259](https://github.com/sgl-project/sglang/pull/43259)
  [AMD] Run the MiniMax indexer CP test on MI35X, not MI300 (#43259)
  _Files: `test/registered/amd/test_minimax_indexer_cp.py`_
- **2026-10-08** [`baee5f3b62`](https://github.com/sgl-project/sglang/commit/baee5f3b62) [#43234](https://github.com/sgl-project/sglang/pull/43234)
  [CI] Drop the `labeled` trigger from the extra CI workflows (#43234)
  _Files: `.github/workflows/pr-states.yml`, `.github/workflows/pr-test-amd-extra.yml`, `.github/workflows/pr-test-extra.yml`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-10-08** [`b72da1b817`](https://github.com/sgl-project/sglang/commit/b72da1b817) [#43033](https://github.com/sgl-project/sglang/pull/43033)
  [AMD] Update v4 amd cookbook 1008 (#43033)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-10-07** [`9a21d82958`](https://github.com/sgl-project/sglang/commit/9a21d82958) [#42847](https://github.com/sgl-project/sglang/pull/42847)
  [AMD] Update v4.1 amd cookbook 1006 (#42847)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-10-06** [`66dd4e15b9`](https://github.com/sgl-project/sglang/commit/66dd4e15b9) [#42757](https://github.com/sgl-project/sglang/pull/42757)
  [AMD][Docs] Add MI355X DeepSeek-V4 Pro PD recipes (#42757)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/scripts/check_cookbook_configs.mjs`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/_playground.jsx` _+1 more__
- **2026-10-06** [`1abd356595`](https://github.com/sgl-project/sglang/commit/1abd356595) [#42552](https://github.com/sgl-project/sglang/pull/42552)
  [AMD] Add engram host/device address mapping (#42552)
  _Files: `python/sglang/srt/layers/engram.py`_
- **2026-10-05** [`b3f967e809`](https://github.com/sgl-project/sglang/commit/b3f967e809) [#41282](https://github.com/sgl-project/sglang/pull/41282)
  Revert "Revert "[AMD][ROCm] Keep cos_sin_cache fp32 on HIP for fused QSA indexer kernel (#41282)"" (#42558)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/layers/rotary_embedding/mrope.py`_
- **2026-10-05** [`456d533e61`](https://github.com/sgl-project/sglang/commit/456d533e61) [#41282](https://github.com/sgl-project/sglang/pull/41282)
  Revert "[AMD][ROCm] Keep cos_sin_cache fp32 on HIP for fused QSA indexer kernel (#41282)" (#42541)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/layers/rotary_embedding/mrope.py`_

## Models  (8 commits)

- **2026-10-12** [`c6e822c29b`](https://github.com/sgl-project/sglang/commit/c6e822c29b) [#43309](https://github.com/sgl-project/sglang/pull/43309)
  [Fix] Adapt NPU Qwen-VL processor patch to transformers 5.19 resize() signature change (#43309)
  _Files: `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`_
- **2026-10-12** [`1a7af3290d`](https://github.com/sgl-project/sglang/commit/1a7af3290d) [#43446](https://github.com/sgl-project/sglang/pull/43446)
  Fix Mistral-native format detection when the Hub is unreachable (#43446)
  _Files: `python/sglang/srt/arg_groups/model_path_hook.py`_
- **2026-10-11** [`5678b71b6c`](https://github.com/sgl-project/sglang/commit/5678b71b6c) [#43037](https://github.com/sgl-project/sglang/pull/43037)
  [Spec] Allow Qwen3.5 backends to opt into packed target verification (#43037)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-10-11** [`7187bb593e`](https://github.com/sgl-project/sglang/commit/7187bb593e) [#43624](https://github.com/sgl-project/sglang/pull/43624)
  [Model] Keep gpt-oss router logits batch-invariant under deterministic inference (#43624)
  _Files: `python/sglang/srt/models/gpt_oss.py`_
- **2026-10-10** [`9b37e28b83`](https://github.com/sgl-project/sglang/commit/9b37e28b83) [#43447](https://github.com/sgl-project/sglang/pull/43447)
  Disable DualGemm fusion for Inkling dense MLP (#43447)
  _Files: `python/sglang/srt/models/inkling_common/dense_mlp.py`_
- **2026-10-08** [`943621c336`](https://github.com/sgl-project/sglang/commit/943621c336) [#42665](https://github.com/sgl-project/sglang/pull/42665)
  [sgl-router] Render DeepSeek-V4 through sglang-processor (#42665)
  _Files: `.github/workflows/pr-test-sgl-router.yml`, `docker/sgl-router.Dockerfile`, `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml` _+8 more__
- **2026-10-08** [`7b6b6ee25e`](https://github.com/sgl-project/sglang/commit/7b6b6ee25e) [#42726](https://github.com/sgl-project/sglang/pull/42726)
  [Docs] Cookbook: interactive SemiAnalysis InferenceX AgentX launches for GLM-5.2, DeepSeek-V4 and DeepSeek-V4.1 (#42726)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/_agentx.jsx` _+4 more__
- **2026-10-06** [`cf19ae6d04`](https://github.com/sgl-project/sglang/commit/cf19ae6d04) [#42662](https://github.com/sgl-project/sglang/pull/42662)
  [rust-processor] Split sglang-processor into tokenizer, render and parser (#42662)
  _Files: `rust/sglang-processor/README.md`, `rust/sglang-processor/src/lib.rs`, `rust/sglang-processor/src/parser/aliases.rs`, `rust/sglang-processor/src/parser/mod.rs` _+12 more__

## Serving / API  (4 commits)

- **2026-10-10** [`506f140166`](https://github.com/sgl-project/sglang/commit/506f140166) [#43233](https://github.com/sgl-project/sglang/pull/43233)
  [sgl-router] Read finished /generate streams to the end; expose reorg admission caps as flags (#43233)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/server/routes/chat/openai.rs`, `experimental/sgl-router/tests/proxy/openai_generate.rs`_
- **2026-10-09** [`fba3ad4b1f`](https://github.com/sgl-project/sglang/commit/fba3ad4b1f) [#41259](https://github.com/sgl-project/sglang/pull/41259)
  [Frontend] Parallelize long chat prompt encoding (#41259)
  _Files: `python/sglang/srt/entrypoints/openai/parallel_prompt_encode.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/environ.py`, `test/registered/unit/entrypoints/openai/test_parallel_prompt_encode.py`_
- **2026-10-07** [`1e86143bf0`](https://github.com/sgl-project/sglang/commit/1e86143bf0) [#42962](https://github.com/sgl-project/sglang/pull/42962)
  [Bugfix] Return None for empty reasoning_content outside K2 Horizon (#42962)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-10-07** [`9c8fc6a8e4`](https://github.com/sgl-project/sglang/commit/9c8fc6a8e4) [#42623](https://github.com/sgl-project/sglang/pull/42623)
  [Bugfix] Preserve empty K2 Horizon reasoning in chat responses (#42623)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_

## LoRA  (1 commits)

- **2026-10-09** [`7578432c21`](https://github.com/sgl-project/sglang/commit/7578432c21) [#43297](https://github.com/sgl-project/sglang/pull/43297)
  [LoRA][Test] Use the 0.9 ROUGE-L tolerance for the CUDA multi-LoRA batch test (#43297)
  _Files: `test/registered/lora/test_multi_lora_backend.py`_

---
_Generated 2026-10-12 17:43 UTC_