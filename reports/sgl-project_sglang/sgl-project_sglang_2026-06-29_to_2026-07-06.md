# sgl-project/sglang — Weekly Change Report
**Period:** 2026-06-29 → 2026-07-06  |  **Total commits:** 267

## ✨ New Features This Week

- **2026-07-06** [#25364](https://github.com/sgl-project/sglang/pull/25364) — Add Accuracy Benchmark for OCR models (#25364)
- **2026-07-06** [#30201](https://github.com/sgl-project/sglang/pull/30201) — cookbook: add Hunyuan 3 (Hy3) Day-0 page (#30201)
- **2026-07-06** [#27906](https://github.com/sgl-project/sglang/pull/27906) — [Model] Support Qwen3.6 ModelOpt mixed NVFP4 (#27906)
- **2026-07-06** [#30048](https://github.com/sgl-project/sglang/pull/30048) — [XPU] Unbreak stage-b: re-add --disable-decode-cuda-graph, quarantine EAGLE3 parity (#30048)
- **2026-07-06** [#29362](https://github.com/sgl-project/sglang/pull/29362) — [AMD ]Feat/dsv4 ep tbo prefill (#29362)
- **2026-07-05** [#23049](https://github.com/sgl-project/sglang/pull/23049) — [Diffusion] Diffusion model support log-requests (#23049)
- **2026-07-05** [#29855](https://github.com/sgl-project/sglang/pull/29855) — [AMD][DI][CI] 3/N Add Kimi K2.6 FP8 MI355X 1P1D nightly recipes (#29855)
- **2026-07-05** [#30040](https://github.com/sgl-project/sglang/pull/30040) — [diffusion] feat: add LingBot realtime prompt, KV window, and lazy VAE controls (#30040)
- **2026-07-04** [#30107](https://github.com/sgl-project/sglang/pull/30107) — [diffusion] perf: add unified SP shard helpers and zero-copy tail-pad attention (#30107)
- **2026-07-04** [#30072](https://github.com/sgl-project/sglang/pull/30072) — [refactor] Add the post-process resolution stage; migrate sampling_backend (stack 10/15) (#30072)
- _…and 69 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-06** [`80decc78ec`](https://github.com/sgl-project/sglang/commit/80decc78ec) [#30237](https://github.com/sgl-project/sglang/pull/30237) — [AMD][DeepSeek V4] Set SGLANG_OPT_FLASHMLA_SPARSE_PREFILL to false on hip code path (#30237)
- **2026-07-06** [`81735ecf80`](https://github.com/sgl-project/sglang/commit/81735ecf80) [#29362](https://github.com/sgl-project/sglang/pull/29362) — [AMD ]Feat/dsv4 ep tbo prefill (#29362)
- **2026-07-06** [`c9ceab34cf`](https://github.com/sgl-project/sglang/commit/c9ceab34cf) [#29394](https://github.com/sgl-project/sglang/pull/29394) — [AMD] [Docker] Update MoRI to v1.2.1 (#29394)
- **2026-07-05** [`8fb99bbaf8`](https://github.com/sgl-project/sglang/commit/8fb99bbaf8) [#30137](https://github.com/sgl-project/sglang/pull/30137) — [refactor] Config resolution pipeline: full-stack review (10-PR series, review only) (#30137)
- **2026-07-05** [`ce733f106b`](https://github.com/sgl-project/sglang/commit/ce733f106b) [#28787](https://github.com/sgl-project/sglang/pull/28787) — [AMD] Fix RMSNorm batch-invariance on ROCm under deterministic inference (#28787)
- **2026-07-05** [`67361ff91b`](https://github.com/sgl-project/sglang/commit/67361ff91b) [#29855](https://github.com/sgl-project/sglang/pull/29855) — [AMD][DI][CI] 3/N Add Kimi K2.6 FP8 MI355X 1P1D nightly recipes (#29855)
- **2026-07-04** [`def20782cf`](https://github.com/sgl-project/sglang/commit/def20782cf) [#30064](https://github.com/sgl-project/sglang/pull/30064) — [refactor] Move ServerArgs ownership into the runtime context (stack 2/15) (#30064)
- **2026-07-03** [`486bcb48e7`](https://github.com/sgl-project/sglang/commit/486bcb48e7) [#30039](https://github.com/sgl-project/sglang/pull/30039) — [diffusion] CI: fix AMD diffusion CI import (#30039)
- **2026-07-03** [`0ab095eb3f`](https://github.com/sgl-project/sglang/commit/0ab095eb3f) [#29986](https://github.com/sgl-project/sglang/pull/29986) — [AMD]: hot-patch transformers dynamic_module_utils symlink bug (#29986)
- **2026-07-03** [`67697fb891`](https://github.com/sgl-project/sglang/commit/67697fb891) [#30014](https://github.com/sgl-project/sglang/pull/30014) — [AMD] Temporarily disabled: every-6-hours rocm 7.2 test (#30014)
- **2026-07-03** [`bee0f34e68`](https://github.com/sgl-project/sglang/commit/bee0f34e68) [#29822](https://github.com/sgl-project/sglang/pull/29822) — [AMD] Accept ROCm tensors in JIT kernel TensorMatcher + register 4 kernel tests (#29822)
- **2026-07-03** [`05bc3f2aa7`](https://github.com/sgl-project/sglang/commit/05bc3f2aa7) [#29918](https://github.com/sgl-project/sglang/pull/29918) — [AMD] Gate broken CK block-FP8 GEMM shapes to aiter-triton-GEMM to fix ROCm 7.0 Qwen3.5 accuracy (#29918)
- **2026-07-02** [`8519be82e8`](https://github.com/sgl-project/sglang/commit/8519be82e8) [#29982](https://github.com/sgl-project/sglang/pull/29982) — [AMD][DeepSeek V4] Fix default FlashMLA sparse prefill off on ROCm/HIP (#29982)
- **2026-07-02** [`f3904f0293`](https://github.com/sgl-project/sglang/commit/f3904f0293) [#27835](https://github.com/sgl-project/sglang/pull/27835) — [bugfix][AMD] Disable aiter allreduce+RMSNorm fusion under DP attention / EP (#27835)
- **2026-07-02** [`caf2e5da2d`](https://github.com/sgl-project/sglang/commit/caf2e5da2d) [#29756](https://github.com/sgl-project/sglang/pull/29756) — [AMD] Fix MiniMax M3 state transfer in Mori PD (#29756)
- **2026-07-02** [`b276a9acee`](https://github.com/sgl-project/sglang/commit/b276a9acee) [#29770](https://github.com/sgl-project/sglang/pull/29770) — chore: cleanup garbage code (#29770)
- **2026-07-02** [`0ae76117ef`](https://github.com/sgl-project/sglang/commit/0ae76117ef) [#29680](https://github.com/sgl-project/sglang/pull/29680) — [AMD] Register 2 CPU/ROCm-safe tests for AMD 1-GPU PR CI (#29680)
- **2026-07-02** [`e88645d65f`](https://github.com/sgl-project/sglang/commit/e88645d65f) [#29672](https://github.com/sgl-project/sglang/pull/29672) — [amd][diffusion] fix: fix causal Conv3D cat/pad fusion crashes for wan2.2 t2v (#29672)
- **2026-07-02** [`a3f6680874`](https://github.com/sgl-project/sglang/commit/a3f6680874) [#27730](https://github.com/sgl-project/sglang/pull/27730) — [AMD]: docker(rocm) bump Mooncake to latest main + enable multi-protocol (#27730)
- **2026-07-01** [`3adfd0f34b`](https://github.com/sgl-project/sglang/commit/3adfd0f34b) [#29782](https://github.com/sgl-project/sglang/pull/29782) — [AMD] Register 3 unit mem_cache + utils tests for stage-b-test-1-gpu-small-amd (#29782)
- **2026-07-01** [`8361561c24`](https://github.com/sgl-project/sglang/commit/8361561c24) [#29694](https://github.com/sgl-project/sglang/pull/29694) — [AMD] Fix int8 per-token quant Triton portability + register test for AMD nightly CI (#29694)
- **2026-07-01** [`9bb7de9258`](https://github.com/sgl-project/sglang/commit/9bb7de9258) [#29784](https://github.com/sgl-project/sglang/pull/29784) — [AMD][DI][CI] 2/N Add DSV4 DP8/EP8 and MTP MI355X 1P1D nightly recipes (#29784)
- **2026-07-01** [`2a6e5c60fe`](https://github.com/sgl-project/sglang/commit/2a6e5c60fe) [#29726](https://github.com/sgl-project/sglang/pull/29726) — [AMD] Rebalance stage-c-large-8-gpu-mi35x partitions to fix 60-min timeout (#29726)
- **2026-07-01** [`13dc5f2dc7`](https://github.com/sgl-project/sglang/commit/13dc5f2dc7) [#25377](https://github.com/sgl-project/sglang/pull/25377) — [HiCache][AMD] Add UMBP tiered DRAM + SSD L3 storage backend with hugepage host allocator   (#25377)
- **2026-07-01** [`548f505cc5`](https://github.com/sgl-project/sglang/commit/548f505cc5) [#29290](https://github.com/sgl-project/sglang/pull/29290) — [AMD] Cover DeepSeek-R1 MXFP4 TP4 MTP nightly CI (#29290)
- **2026-07-01** [`69ce72020a`](https://github.com/sgl-project/sglang/commit/69ce72020a) [#29693](https://github.com/sgl-project/sglang/pull/29693) — [AMD] Register ltx2_ada_values JIT kernel test for AMD nightly CI (#29693)
- **2026-07-01** [`81a472efcc`](https://github.com/sgl-project/sglang/commit/81a472efcc) [#29816](https://github.com/sgl-project/sglang/pull/29816) — [AMD] Update ROCm AITER pin to 9127c94 (#29816)
- **2026-07-01** [`308d89e042`](https://github.com/sgl-project/sglang/commit/308d89e042) [#29409](https://github.com/sgl-project/sglang/pull/29409) — [AMD] Split qwen3.5 triton DCP test into its own nightly job (#29409)
- **2026-07-01** [`56f22cd520`](https://github.com/sgl-project/sglang/commit/56f22cd520) [#28612](https://github.com/sgl-project/sglang/pull/28612) — Optimize C128 state pool allocation using request state pool (#28612)
- **2026-06-30** [`bb98629157`](https://github.com/sgl-project/sglang/commit/bb98629157) [#28471](https://github.com/sgl-project/sglang/pull/28471) — docs(cookbook): add AMD MI300X/MI325X/MI355X support for GLM-5.2 (#28471)
- **2026-06-30** [`c70cc96905`](https://github.com/sgl-project/sglang/commit/c70cc96905) [#29768](https://github.com/sgl-project/sglang/pull/29768) — [AMD] Stop rocm720 pr auto-runs (#29768)
- **2026-06-30** [`f2756f53f3`](https://github.com/sgl-project/sglang/commit/f2756f53f3) [#29765](https://github.com/sgl-project/sglang/pull/29765) — [AMD] Update AMD local registry address (#29765)
- **2026-06-30** [`a5e6dd3767`](https://github.com/sgl-project/sglang/commit/a5e6dd3767) [#27204](https://github.com/sgl-project/sglang/pull/27204) — [AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8 (#27204)
- **2026-06-30** [`bae78a44da`](https://github.com/sgl-project/sglang/commit/bae78a44da) [#29393](https://github.com/sgl-project/sglang/pull/29393) — [Deps] Bump transformers to 5.12.1 (#29393)
- **2026-06-30** [`f920a37da4`](https://github.com/sgl-project/sglang/commit/f920a37da4) [#29642](https://github.com/sgl-project/sglang/pull/29642) — [AMD] Copy decode result on forward_stream instead of copy_stream (#29642)
- **2026-06-30** [`54e71506b3`](https://github.com/sgl-project/sglang/commit/54e71506b3) [#29420](https://github.com/sgl-project/sglang/pull/29420) — [AMD][DSV4] Remove per-batch D2H syncs in MTP to avoid bubbles between 2 batches (#29420)
- **2026-06-30** [`7da4e30d9b`](https://github.com/sgl-project/sglang/commit/7da4e30d9b) [#29671](https://github.com/sgl-project/sglang/pull/29671) — [AMD] Register fused_metadata_copy JIT kernel test for AMD nightly CI (#29671)
- **2026-06-30** [`6bf15aa2b9`](https://github.com/sgl-project/sglang/commit/6bf15aa2b9) [#28348](https://github.com/sgl-project/sglang/pull/28348) — [AMD]: Enable NIXL PD disaggregation for ROCm(1/n)  (#28348)
- **2026-06-29** [`5169df70f6`](https://github.com/sgl-project/sglang/commit/5169df70f6) [#29661](https://github.com/sgl-project/sglang/pull/29661) — [AMD] Sgl-data mount opt-in (#29661)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-07-06 |
| [#30245](https://github.com/sgl-project/sglang/issues/30245) | ROCm consumer GPU (gfx1100/RDNA3): fused-MoE blocked by upstream trito | — | 2026-07-06 |
| [#30233](https://github.com/sgl-project/sglang/issues/30233) | [Bug] PD disaggregation: aborted prefill requests (input too long) cau | — | 2026-07-06 |
| [#28618](https://github.com/sgl-project/sglang/issues/28618) | [RFC] Add SM89/L20 support for DeepSeek-V4-Flash-FP8 | — | 2026-07-06 |
| [#30209](https://github.com/sgl-project/sglang/issues/30209) | [Bug] GlmMoeDsa (GLM-5.2) FP4 + EAGLE: illegal memory access in flashi | — | 2026-07-06 |
| [#29736](https://github.com/sgl-project/sglang/issues/29736) | [Roadmap][DCP] Decode Context Parallel & Helix Parallelism — next step | — | 2026-07-06 |
| [#30190](https://github.com/sgl-project/sglang/issues/30190) | PD disaggregation over Mooncake multi-protocol (rdma+hip) is unstable  | — | 2026-07-06 |
| [#30099](https://github.com/sgl-project/sglang/issues/30099) | [AMD][DI][CI] NIXL Cross-Node KV Transfer Blocked on MI355X Due to Ion | — | 2026-07-05 |
| [#30082](https://github.com/sgl-project/sglang/issues/30082) | [Bug] The performance of deepseekv4 failed to pass the test on the mai | — | 2026-07-04 |
| [#21774](https://github.com/sgl-project/sglang/issues/21774) | [Bug] ROCm release & nightly images doesn't work with Thor-2 NIC | inactive | 2026-07-04 |
| [#30033](https://github.com/sgl-project/sglang/issues/30033) | [Bug] PD disaggregation + DP-attention decode: no admission control ag | — | 2026-07-03 |
| [#29875](https://github.com/sgl-project/sglang/issues/29875) | [Bug] MI355X nightly: Kimi-K2.6 (trust_remote_code) fails at server st | — | 2026-07-03 |
| [#27937](https://github.com/sgl-project/sglang/issues/27937) | [Failure Tracker] PR Test (AMD) | — | 2026-07-02 |
| [#27310](https://github.com/sgl-project/sglang/issues/27310) | [RFC] GPU Memory Service (GMS) integration for out-of-process GPU memo | — | 2026-07-02 |
| [#23206](https://github.com/sgl-project/sglang/issues/23206) | [RFC] Sglang non-GPU process rust migration | — | 2026-07-02 |
| [#27462](https://github.com/sgl-project/sglang/issues/27462) | [Roadmap] Parallel Speculative Decoding Roadmap | — | 2026-07-02 |
| [#23363](https://github.com/sgl-project/sglang/issues/23363) | [Bug] KimiK2Detector streaming parser silently drops / hangs on multi- | — | 2026-07-02 |
| [#29687](https://github.com/sgl-project/sglang/issues/29687) | [Bug][ROCm] Multimodal CUDA-IPC non-pooled fallback crashes (hipErrorI | — | 2026-07-02 |
| [#29709](https://github.com/sgl-project/sglang/issues/29709) | [RFC]: KV Cache Events for HiCache L3 Storage Backends | RFC | 2026-07-02 |
| [#29864](https://github.com/sgl-project/sglang/issues/29864) | [AMD/ROCm] store_cache_4d Triton kernel fails to compile on ROCm 7.2.0 | — | 2026-07-01 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 54 |
| Multimodal | 34 |
| Other | 27 |
| MoE / Expert Parallel | 25 |
| KV Cache / Memory | 17 |
| Quantization | 14 |
| Prefill / Decode Disaggregation | 14 |
| Tensor / Data Parallel | 12 |
| Docs / Examples | 11 |
| Triton / Kernels | 11 |
| Models | 11 |
| ROCm / AMD | 10 |
| Scheduler / Batching | 9 |
| Speculative Decoding | 8 |
| CI / Build | 7 |
| Structured Output | 1 |
| LoRA | 1 |
| Serving / API | 1 |

## Attention / FlashInfer  (54 commits)

- **2026-07-06** [`80decc78ec`](https://github.com/sgl-project/sglang/commit/80decc78ec) [#30237](https://github.com/sgl-project/sglang/pull/30237)
  [AMD][DeepSeek V4] Set SGLANG_OPT_FLASHMLA_SPARSE_PREFILL to false on hip code path (#30237)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`_
- **2026-07-06** [`6bb2918938`](https://github.com/sgl-project/sglang/commit/6bb2918938) [#30047](https://github.com/sgl-project/sglang/pull/30047)
  Bugfix qwen prefix cache circumstances (#30047)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`_
- **2026-07-06** [`5eb1b6a7ba`](https://github.com/sgl-project/sglang/commit/5eb1b6a7ba) [#29912](https://github.com/sgl-project/sglang/pull/29912)
  Remove retired DSA env paths (#29912)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py`, `python/sglang/srt/layers/attention/dsa/dsa_mtp_verification.py` _+3 more__
- **2026-07-06** [`81735ecf80`](https://github.com/sgl-project/sglang/commit/81735ecf80) [#29362](https://github.com/sgl-project/sglang/pull/29362)
  [AMD ]Feat/dsv4 ep tbo prefill (#29362)
  _Files: `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/tbo_backend.py` _+7 more__
- **2026-07-05** [`5e6f49c986`](https://github.com/sgl-project/sglang/commit/5e6f49c986) [#30040](https://github.com/sgl-project/sglang/pull/30040)
  [diffusion] feat: add LingBot realtime prompt, KV window, and lazy VAE controls (#30040)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/lingbot_world.py`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/adapters/lingbot_world_realtime_adapter.py`, `python/sglang/multimodal_gen/runtime/layers/kvcache/causal_attention_cache.py` _+9 more__
- **2026-07-04** [`763c6bf372`](https://github.com/sgl-project/sglang/commit/763c6bf372) [#30107](https://github.com/sgl-project/sglang/pull/30107)
  [diffusion] perf: add unified SP shard helpers and zero-copy tail-pad attention (#30107)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/runtime/distributed/sp_shard_utils.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/ernie_image.py` _+8 more__
- **2026-07-04** [`e552f6ed75`](https://github.com/sgl-project/sglang/commit/e552f6ed75) [#30111](https://github.com/sgl-project/sglang/pull/30111)
  [Fix] Fix DSA indexer fusion for NeoX RoPE (#30111)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `test/registered/8-gpu-models/test_deepseek_v32_indexcache.py`_
- **2026-07-04** [`92b800c531`](https://github.com/sgl-project/sglang/commit/92b800c531) [#29959](https://github.com/sgl-project/sglang/pull/29959)
  [DSA][GLM5.2] Index Share for MHA (#29959)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`_
- **2026-07-04** [`abbb41a214`](https://github.com/sgl-project/sglang/commit/abbb41a214) [#30073](https://github.com/sgl-project/sglang/pull/30073)
  [refactor] Migrate the attention_backend resolution chain (stack 11/15) (#30073)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-07-04** [`ad744c6c6b`](https://github.com/sgl-project/sglang/commit/ad744c6c6b) [#29843](https://github.com/sgl-project/sglang/pull/29843)
  [trtllm_mha] Fuse cuda-graph metadata rebuild into one triton kernel (#29843)
  _Files: `python/sglang/srt/layers/attention/hybrid_attn_backend.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/triton_ops/trtllm_mha_graph_metadata.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py` _+5 more__
- **2026-07-04** [`5f623ad24e`](https://github.com/sgl-project/sglang/commit/5f623ad24e) [#30083](https://github.com/sgl-project/sglang/pull/30083)
  Revert "Fix wrong RMSNorm fallback to old Flashinfer CUDA kernel when in PCG" (#30083)
  _Files: `python/sglang/srt/layers/layernorm.py`, `sgl-kernel/python/sgl_kernel/elementwise.py`_
- **2026-07-03** [`6ce02b95ad`](https://github.com/sgl-project/sglang/commit/6ce02b95ad) [#30025](https://github.com/sgl-project/sglang/pull/30025)
  fix: reorder DSA indexer dual-stream ops to avoid CUDA graph stream explosion (#30025)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-07-03** [`0203c60fdf`](https://github.com/sgl-project/sglang/commit/0203c60fdf) [#29365](https://github.com/sgl-project/sglang/pull/29365)
  [CP] Consolidate decode-context-parallel (DCP) helpers into layers/dcp/ (#29365)
  _Files: `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/attention/utils.py` _+16 more__
- **2026-07-03** [`4dddb04325`](https://github.com/sgl-project/sglang/commit/4dddb04325) [#27914](https://github.com/sgl-project/sglang/pull/27914)
  [Intel GPU] DeepSeek V4 6/N: use sgl-kernel implemetation of flash_mla_with_kvcache on XPU (#27914)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-07-03** [`9df16b5ba9`](https://github.com/sgl-project/sglang/commit/9df16b5ba9) [#29911](https://github.com/sgl-project/sglang/pull/29911)
  [XPU] Remove redundant xpu graph backend and make xpu graph opt-in by default (#29911)
  _Files: `docs_new/docs/hardware-platforms/xpu.mdx`, `python/sglang/multimodal_gen/runtime/platforms/xpu.py`, `python/sglang/srt/hardware_backend/xpu/graph_runner/xpu_graph_runner.py`, `python/sglang/srt/hardware_backend/xpu/xpu_cudagraph_backend.py` _+13 more__
- **2026-07-03** [`76f7f7c006`](https://github.com/sgl-project/sglang/commit/76f7f7c006) [#29995](https://github.com/sgl-project/sglang/pull/29995)
  [Spec] Remove the ServerArgs clone + global save/restore hack from DFlashWorkerV2 (#29995)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/model_runner.py` _+2 more__
- **2026-07-03** [`a6ee64d237`](https://github.com/sgl-project/sglang/commit/a6ee64d237) [#29619](https://github.com/sgl-project/sglang/pull/29619)
  [DeepSeek-V4] Add an opt-in non-paged indexer for long-context prefill (#29619)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py` _+2 more__
- **2026-07-03** [`70b6c06793`](https://github.com/sgl-project/sglang/commit/70b6c06793) [#29798](https://github.com/sgl-project/sglang/pull/29798)
  fix: avoid DSA indexer CPU seq lens fallback (#29798)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py`_
- **2026-07-03** [`372a893744`](https://github.com/sgl-project/sglang/commit/372a893744) [#29945](https://github.com/sgl-project/sglang/pull/29945)
  Move deferred mamba cow and clear (#29945)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-07-03** [`d8a4f7a7aa`](https://github.com/sgl-project/sglang/commit/d8a4f7a7aa) [#29932](https://github.com/sgl-project/sglang/pull/29932)
  add mimo-v2-flash model tutorial (#29932)
  _Files: `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/model-tutorials/mimo_v2_flash.mdx`_
- **2026-07-02** [`8519be82e8`](https://github.com/sgl-project/sglang/commit/8519be82e8) [#29982](https://github.com/sgl-project/sglang/pull/29982)
  [AMD][DeepSeek V4] Fix default FlashMLA sparse prefill off on ROCm/HIP (#29982)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`_
- **2026-07-02** [`f3904f0293`](https://github.com/sgl-project/sglang/commit/f3904f0293) [#27835](https://github.com/sgl-project/sglang/pull/27835)
  [bugfix][AMD] Disable aiter allreduce+RMSNorm fusion under DP attention / EP (#27835)
  _Files: `python/sglang/srt/layers/communicator.py`, `test/registered/ops/test_aiter_allreduce_fusion_amd.py`_
- **2026-07-02** [`bc25abb786`](https://github.com/sgl-project/sglang/commit/bc25abb786) [#29921](https://github.com/sgl-project/sglang/pull/29921)
  perf(triton): avoid per-step D2H .item() sync in cuda-graph loc translate (#29921)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`_
- **2026-07-02** [`1b6d1e9752`](https://github.com/sgl-project/sglang/commit/1b6d1e9752) [#29702](https://github.com/sgl-project/sglang/pull/29702)
  Fix wrong RMSNorm fallback to old Flashinfer CUDA kernel when in PCG (#29702)
  _Files: `python/sglang/srt/layers/layernorm.py`, `sgl-kernel/python/sgl_kernel/elementwise.py`_
- **2026-07-02** [`3c1adddff9`](https://github.com/sgl-project/sglang/commit/3c1adddff9) [#29852](https://github.com/sgl-project/sglang/pull/29852)
  [diffusion] refactor: refactor cuda attention backend resolver (#29852)
  _Files: `python/sglang/multimodal_gen/runtime/platforms/cuda.py`, `python/sglang/multimodal_gen/test/unit/test_cuda_attention_backend.py`_
- **2026-07-02** [`476c946543`](https://github.com/sgl-project/sglang/commit/476c946543) [#29884](https://github.com/sgl-project/sglang/pull/29884)
  [Doc] Cookbook: Laguna-XS-2.1 (DFlash low-latency + high-throughput) (#29884)
  _Files: `docs_new/cookbook/autoregressive/Poolside/Laguna-XS-2.1.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json`, `docs_new/src/snippets/configs/poolside/laguna-xs21-benchmarks.jsx` _+1 more__
- **2026-07-02** [`697b400d70`](https://github.com/sgl-project/sglang/commit/697b400d70) [#29779](https://github.com/sgl-project/sglang/pull/29779)
  Share one logits output buffer across prefill/decode/draft cuda-graph runners (#29779)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/model_executor/graph_shared_output.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+5 more__
- **2026-07-02** [`926140d789`](https://github.com/sgl-project/sglang/commit/926140d789) [#29053](https://github.com/sgl-project/sglang/pull/29053)
  [XPU] Enable XPU graph support (decode full-graph + prefill tc_piecewise) (#29053)
  _Files: `docs_new/docs/hardware-platforms/xpu.mdx`, `python/sglang/srt/compilation/backend.py`, `python/sglang/srt/compilation/weak_ref_tensor.py`, `python/sglang/srt/compilation/xpu_piecewise_backend.py` _+21 more__
- **2026-07-02** [`307094dc7d`](https://github.com/sgl-project/sglang/commit/307094dc7d) [#29885](https://github.com/sgl-project/sglang/pull/29885)
  [DeepSeek V4] Cover both dense and sparse prefill paths in the compress attention unittest (#29885)
  _Files: `python/sglang/test/kits/attention_unittest/attention_methods/dsv4_attention.py`, `test/registered/attention/unittests/dsv4/test_deepseek_v4.py`_
- **2026-07-02** [`9ba4b8f8ba`](https://github.com/sgl-project/sglang/commit/9ba4b8f8ba) [#29551](https://github.com/sgl-project/sglang/pull/29551)
  sgl-kernel: bump sgl-attn for varlen num_splits OOM fix (#29551)
  _Files: `sgl-kernel/CMakeLists.txt`, `sgl-kernel/tests/test_flash_attention.py`_
- **2026-07-02** [`eb23f9a86b`](https://github.com/sgl-project/sglang/commit/eb23f9a86b) [#29472](https://github.com/sgl-project/sglang/pull/29472)
  [KDA] Add FlashKDA prefill backend for safe-gate KDA linear attention (#29472)
  _Files: `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashkda.py`, `python/sglang/srt/layers/attention/linear/utils.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-07-02** [`6eeb9871e5`](https://github.com/sgl-project/sglang/commit/6eeb9871e5) [#29446](https://github.com/sgl-project/sglang/pull/29446)
  Add Laguna XS.2.1 DFlash support to SGLang (#29446)
  _Files: `python/sglang/srt/configs/laguna.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/srt/models/laguna.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-07-02** [`bac351d617`](https://github.com/sgl-project/sglang/commit/bac351d617) [#29829](https://github.com/sgl-project/sglang/pull/29829)
  [NPU] Fix block_table batch size mismatch in GLM-4.7-Flash DeepEP + MTP without CUDA Graphs (#29829)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-07-02** [`cf7c6ac234`](https://github.com/sgl-project/sglang/commit/cf7c6ac234) [#28925](https://github.com/sgl-project/sglang/pull/28925)
  fix(nightly-precision): pin flashinfer allreduce-fusion backend for TP-partial capture contract (#28925)
  _Files: `test/registered/debug_utils/test_nightly_precision_regression.py`_
- **2026-07-01** [`c865347b98`](https://github.com/sgl-project/sglang/commit/c865347b98) [#29775](https://github.com/sgl-project/sglang/pull/29775)
  [DeepSeek V4] Enable FlashMLA sparse prefill by default (#29775)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py` _+1 more__
- **2026-07-01** [`8f0d320d31`](https://github.com/sgl-project/sglang/commit/8f0d320d31) [#29595](https://github.com/sgl-project/sglang/pull/29595)
  [Spec] Enable FlashInfer autotune for spec draft (#29595)
  _Files: `python/sglang/srt/model_executor/runner/base_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`, `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py` _+12 more__
- **2026-07-01** [`4a8e76805c`](https://github.com/sgl-project/sglang/commit/4a8e76805c) [#29678](https://github.com/sgl-project/sglang/pull/29678)
  feat(mem_cache): unified memory pool for hybrid Mamba / SWA models (#29678)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` _+24 more__
- **2026-07-01** [`9bb7de9258`](https://github.com/sgl-project/sglang/commit/9bb7de9258) [#29784](https://github.com/sgl-project/sglang/pull/29784)
  [AMD][DI][CI] 2/N Add DSV4 DP8/EP8 and MTP MI355X 1P1D nightly recipes (#29784)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`, `scripts/ci/slurm/launch_mi355x.sh`, `scripts/ci/slurm/nightly-configs.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/dsv4flash/1k1k/1p1d-dp8ep8-mtp.yaml` _+11 more__
- **2026-07-01** [`81a472efcc`](https://github.com/sgl-project/sglang/commit/81a472efcc) [#29816](https://github.com/sgl-project/sglang/pull/29816)
  [AMD] Update ROCm AITER pin to 9127c94 (#29816)
  _Files: `docker/rocm.Dockerfile`, `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-07-01** [`00e12cebb4`](https://github.com/sgl-project/sglang/commit/00e12cebb4) [#29161](https://github.com/sgl-project/sglang/pull/29161)
  [Fix]: Defer DSA MLA CP KV gather for fp8 trtllm prefill in PD mode (#29161)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`_
- **2026-07-01** [`41779d56fd`](https://github.com/sgl-project/sglang/commit/41779d56fd) [#29271](https://github.com/sgl-project/sglang/pull/29271)
  fix: make write_token dynamic (#29271)
  _Files: `python/sglang/srt/hardware_backend/mlx/kv_cache/attention_kv_cache.py`, `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`_
- **2026-06-30** [`b6fceaa789`](https://github.com/sgl-project/sglang/commit/b6fceaa789) [#29613](https://github.com/sgl-project/sglang/pull/29613)
  [DSA] Use cos_sin_cache for DSA indexer fusion (#29613)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v32/indexer_k.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/jit_kernel/dsv32/elementwise.py`, `python/sglang/jit_kernel/dsv4/elementwise.py` _+2 more__
- **2026-06-30** [`dbb51c46ac`](https://github.com/sgl-project/sglang/commit/dbb51c46ac) [#29715](https://github.com/sgl-project/sglang/pull/29715)
  [CI] Migrate JIT tests missed by #29066 to runner_config registration (#29715)
  _Files: `scripts/ci/check_registered_tests.py`, `test/registered/dcp/test_reduce_scatter_along_dim.py`, `test/registered/jit/benchmark/bench_dsv3_fused_a_gemm.py`, `test/registered/jit/benchmark/bench_dsv3_router_gemm.py` _+14 more__
- **2026-06-30** [`54e71506b3`](https://github.com/sgl-project/sglang/commit/54e71506b3) [#29420](https://github.com/sgl-project/sglang/pull/29420)
  [AMD][DSV4] Remove per-batch D2H syncs in MTP to avoid bubbles between 2 batches (#29420)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-06-30** [`3a72d02415`](https://github.com/sgl-project/sglang/commit/3a72d02415) [#29499](https://github.com/sgl-project/sglang/pull/29499)
  [DSA] Optimize DSA CUDA graph replay metadata generation (#29499)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/attention/triton_ops/dsa_metadata.py` _+1 more__
- **2026-06-30** [`bc8b3ab1f5`](https://github.com/sgl-project/sglang/commit/bc8b3ab1f5) [#25751](https://github.com/sgl-project/sglang/pull/25751)
  [Kernel] Add SM90 Q8KV8 FP8 Sparse MLA Prefill JIT Kernel with Tests and Benchmark (#25751)
  _Files: `python/sglang/jit_kernel/csrc/sparse_mla_q8kv8_prefill_sm90/config.h`, `python/sglang/jit_kernel/csrc/sparse_mla_q8kv8_prefill_sm90/defines.h`, `python/sglang/jit_kernel/csrc/sparse_mla_q8kv8_prefill_sm90/dense_fp8_transpose_v.h`, `python/sglang/jit_kernel/csrc/sparse_mla_q8kv8_prefill_sm90/dense_fp8_utils.h` _+7 more__
- **2026-06-29** [`f0bf96390b`](https://github.com/sgl-project/sglang/commit/f0bf96390b) [#27455](https://github.com/sgl-project/sglang/pull/27455)
  [SM120] Add FlashInfer sparse MLA decode for DSv4-Flash (#27455)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flash_mla_sm120.py`, `test/registered/kernels/test_flash_mla_backends.py`_
- **2026-06-29** [`fc96edd297`](https://github.com/sgl-project/sglang/commit/fc96edd297) [#29533](https://github.com/sgl-project/sglang/pull/29533)
  feat(mem_cache): page-major (layer-major within a page) KV/state layout (#29533)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py`, `python/sglang/srt/layers/attention/triton_backend.py` _+21 more__
- **2026-06-29** [`a2b5ce2ed1`](https://github.com/sgl-project/sglang/commit/a2b5ce2ed1) [#26929](https://github.com/sgl-project/sglang/pull/26929)
  Add stochastic rounding for FP16 Mamba SSM cache (#26929)
  _Files: `docs_new/cookbook/autoregressive/NVIDIA/Nemotron3-Ultra.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `docs_new/src/snippets/autoregressive/nemotron3-ultra-deployment.jsx`, `python/sglang/srt/layers/attention/mamba/ops/mamba_ssm.py` _+4 more__
- **2026-06-29** [`c0d45cda29`](https://github.com/sgl-project/sglang/commit/c0d45cda29) [#29338](https://github.com/sgl-project/sglang/pull/29338)
  [Spec] Add DFLASH basic sanity CI test (#29338)
  _Files: `python/sglang/test/kits/fwd_occupancy_kit.py`, `test/registered/core/test_basic_sanity_dflash.py`_
- **2026-06-29** [`62d7929b3a`](https://github.com/sgl-project/sglang/commit/62d7929b3a) [#29598](https://github.com/sgl-project/sglang/pull/29598)
  [NPU][Bugfix] Accept in_capture in Ascend replay metadata (#29598)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`_
- **2026-06-29** [`2260e612f6`](https://github.com/sgl-project/sglang/commit/2260e612f6) [#29492](https://github.com/sgl-project/sglang/pull/29492)
  [NPU] update best practicce docs from testcase (#29492)
  _Files: `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_r1.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_v3_2.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/glm5_1.mdx` _+11 more__
- **2026-06-29** [`be17475a1b`](https://github.com/sgl-project/sglang/commit/be17475a1b) [#29541](https://github.com/sgl-project/sglang/pull/29541)
  [Spec] Publish DFLASH verify read-done event for fine-grained WAR barrier (#29541)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`_
- **2026-06-29** [`abaee4664e`](https://github.com/sgl-project/sglang/commit/abaee4664e) [#29343](https://github.com/sgl-project/sglang/pull/29343)
  [dflash] fa3/fa4: device-side page table; drop seq_lens_cpu D2H sync (#29343)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/attention/test_trtllm_mha_page_table.py`_

## Multimodal  (34 commits)

- **2026-07-06** [`5f98f62a8a`](https://github.com/sgl-project/sglang/commit/5f98f62a8a) [#30086](https://github.com/sgl-project/sglang/pull/30086)
  [diffusion] perf: tp-shard every text/image encoder across the full DiT replica (any parallelism) (#30086)
  _Files: `python/sglang/multimodal_gen/configs/models/encoders/base.py`, `python/sglang/multimodal_gen/configs/models/encoders/t5.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/image_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py` _+8 more__
- **2026-07-06** [`de00b838c4`](https://github.com/sgl-project/sglang/commit/de00b838c4) [#30148](https://github.com/sgl-project/sglang/pull/30148)
  [diffusion] fix: pass progressive params through image API (#30148)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`_
- **2026-07-06** [`9d00385b63`](https://github.com/sgl-project/sglang/commit/9d00385b63) [#30180](https://github.com/sgl-project/sglang/pull/30180)
  Cleanup: relocate temp_set_env and consolidate multi-device/CUDA helpers in common.py (#30180)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/utils/common.py` _+3 more__
- **2026-07-05** [`931b00f1b0`](https://github.com/sgl-project/sglang/commit/931b00f1b0) [#30159](https://github.com/sgl-project/sglang/pull/30159)
  [diffusion] Clean up duplicate helper definitions (#30159)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/joy_echo/memory.py`, `python/sglang/multimodal_gen/test/scripts/gen_diffusion_ci_outputs.py`_
- **2026-07-05** [`addffd7489`](https://github.com/sgl-project/sglang/commit/addffd7489) [#23049](https://github.com/sgl-project/sglang/pull/23049)
  [Diffusion] Diffusion model support log-requests (#23049)
  _Files: `docs_new/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/scheduler_client.py`, `python/sglang/multimodal_gen/runtime/server_args.py`, `python/sglang/multimodal_gen/runtime/utils/request_logger.py` _+1 more__
- **2026-07-05** [`b070cb2ae0`](https://github.com/sgl-project/sglang/commit/b070cb2ae0) [#29926](https://github.com/sgl-project/sglang/pull/29926)
  Fix Diffusion GT generation pipelines (#29926)
  _Files: `python/sglang/multimodal_gen/test/scripts/gen_diffusion_ci_outputs.py`_
- **2026-07-04** [`00f088f6be`](https://github.com/sgl-project/sglang/commit/00f088f6be) [#30138](https://github.com/sgl-project/sglang/pull/30138)
  [fix] Wrap the sp_shard test entry point in sys.exit so failures propagate (#30138)
  _Files: `python/sglang/multimodal_gen/test/unit/test_sp_shard.py`_
- **2026-07-04** [`6dd0cefb2a`](https://github.com/sgl-project/sglang/commit/6dd0cefb2a) [#29844](https://github.com/sgl-project/sglang/pull/29844)
  [CI] Revert ModelOpt NVFP4 threshold relax (#29844)
  _Files: `.github/workflows/pr-test-multimodal-gen.yml`, `python/sglang/multimodal_gen/test/server/consistency_thresholds/h100.json`, `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-07-04** [`36fc0093d6`](https://github.com/sgl-project/sglang/commit/36fc0093d6) [#30110](https://github.com/sgl-project/sglang/pull/30110)
  [diffusion] fix: shut down diffusion workers on serve exit (#30110)
  _Files: `python/sglang/multimodal_gen/runtime/launch_server.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/test/unit/test_launch_server_shutdown.py`, `python/sglang/multimodal_gen/utils.py`_
- **2026-07-04** [`def20782cf`](https://github.com/sgl-project/sglang/commit/def20782cf) [#30064](https://github.com/sgl-project/sglang/pull/30064)
  [refactor] Move ServerArgs ownership into the runtime context (stack 2/15) (#30064)
  _Files: `python/sglang/multimodal_gen/test/unit/test_disagg_trace.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/test_runtime_context.py`_
- **2026-07-04** [`03962d4238`](https://github.com/sgl-project/sglang/commit/03962d4238) [#29306](https://github.com/sgl-project/sglang/pull/29306)
  [diffusion] feat: enable compile warmup for vae decode (#29306)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/zimage.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/runtime/models/dits/zimage.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/decoding.py` _+9 more__
- **2026-07-04** [`5af1f949ca`](https://github.com/sgl-project/sglang/commit/5af1f949ca) [#29831](https://github.com/sgl-project/sglang/pull/29831)
  [diffusion] CI: prefer official diffusion consistency GT (#29831)
  _Files: `python/sglang/multimodal_gen/runtime/server_warmup.py`, `python/sglang/multimodal_gen/test/scripts/gen_diffusion_ci_outputs.py`, `python/sglang/multimodal_gen/test/server/consistency_thresholds/h100.json`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json` _+2 more__
- **2026-07-04** [`b28bc1060f`](https://github.com/sgl-project/sglang/commit/b28bc1060f) [#29994](https://github.com/sgl-project/sglang/pull/29994)
  fix(mimo-vl): pass padded_context_dim to Qwen2_5_VisionPatchMerger (#29994)
  _Files: `python/sglang/srt/models/mimo_vl.py`_
- **2026-07-03** [`486bcb48e7`](https://github.com/sgl-project/sglang/commit/486bcb48e7) [#30039](https://github.com/sgl-project/sglang/pull/30039)
  [diffusion] CI: fix AMD diffusion CI import (#30039)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`_
- **2026-07-03** [`1058d00fe0`](https://github.com/sgl-project/sglang/commit/1058d00fe0) [#29631](https://github.com/sgl-project/sglang/pull/29631)
  [diffusion] feat: support cache-dit for Ideogram 4 (#29631)
  _Files: `python/sglang/multimodal_gen/runtime/cache/cache_dit_integration.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ideogram.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/progressive_resolution/ideogram.py`_
- **2026-07-03** [`42acfd1550`](https://github.com/sgl-project/sglang/commit/42acfd1550) [#30016](https://github.com/sgl-project/sglang/pull/30016)
  [diffusion] feat: performance_mode=speed enables torch.compile by default (#30016)
  _Files: `python/sglang/multimodal_gen/runtime/server_args_auto_tune.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-07-03** [`fe60764f54`](https://github.com/sgl-project/sglang/commit/fe60764f54) [#27704](https://github.com/sgl-project/sglang/pull/27704)
  [diffusion] fix: add profiling support and fix VBench dataset handling in bench_offline_throughput (#27704)
  _Files: `python/sglang/multimodal_gen/benchmarks/bench_offline_throughput.py`, `python/sglang/multimodal_gen/benchmarks/datasets.py`_
- **2026-07-03** [`e878c6ebdd`](https://github.com/sgl-project/sglang/commit/e878c6ebdd) [#29774](https://github.com/sgl-project/sglang/pull/29774)
  [diffusion] feat: shard qwen-image dit across tp ranks (#29774)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`_
- **2026-07-03** [`bee0f34e68`](https://github.com/sgl-project/sglang/commit/bee0f34e68) [#29822](https://github.com/sgl-project/sglang/pull/29822)
  [AMD] Accept ROCm tensors in JIT kernel TensorMatcher + register 4 kernel tests (#29822)
  _Files: `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/csrc/diffusion/causal_conv3d_cat_pad.cuh`, `python/sglang/jit_kernel/csrc/ngram_embedding.cuh`, `test/registered/jit/diffusion/test_causal_conv3d_cat_pad.py` _+2 more__
- **2026-07-02** [`119b76567d`](https://github.com/sgl-project/sglang/commit/119b76567d) [#29862](https://github.com/sgl-project/sglang/pull/29862)
  [diffusion] feat: add --offload-during-compile to fit max-autotune on tight-memory GPUs (#29862)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/hunyuan3d/shape.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ideogram.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/progressive_resolution/ideogram.py` _+3 more__
- **2026-07-02** [`e88645d65f`](https://github.com/sgl-project/sglang/commit/e88645d65f) [#29672](https://github.com/sgl-project/sglang/pull/29672)
  [amd][diffusion] fix: fix causal Conv3D cat/pad fusion crashes for wan2.2 t2v (#29672)
  _Files: `python/sglang/multimodal_gen/runtime/layers/parallel_conv.py`_
- **2026-07-01** [`03b9278da0`](https://github.com/sgl-project/sglang/commit/03b9278da0) [#29824](https://github.com/sgl-project/sglang/pull/29824)
  [diffusion] CI: tighten multimodal-gen consistency thresholds (#29824)
  _Files: `python/sglang/multimodal_gen/test/server/consistency_thresholds/h100.json`_
- **2026-07-01** [`79f334b1aa`](https://github.com/sgl-project/sglang/commit/79f334b1aa) [#29791](https://github.com/sgl-project/sglang/pull/29791)
  [diffusion] CI: add 5090 job (#29791)
  _Files: `.github/workflows/pr-test-multimodal-gen.yml`, `python/sglang/multimodal_gen/test/scripts/gen_perf_baselines.py`, `python/sglang/multimodal_gen/test/server/consistency_thresholds/5090.json`, `python/sglang/multimodal_gen/test/server/consistency_thresholds/b200.json` _+12 more__
- **2026-07-01** [`69ce72020a`](https://github.com/sgl-project/sglang/commit/69ce72020a) [#29693](https://github.com/sgl-project/sglang/pull/29693)
  [AMD] Register ltx2_ada_values JIT kernel test for AMD nightly CI (#29693)
  _Files: `test/registered/jit/diffusion/test_ltx2_ada_values.py`_
- **2026-07-01** [`47ae1241d3`](https://github.com/sgl-project/sglang/commit/47ae1241d3) [#29767](https://github.com/sgl-project/sglang/pull/29767)
  [CI] Relax ModelOpt NVFP4 diffusion consistency thresholds (#29767)
  _Files: `python/sglang/multimodal_gen/test/server/consistency_threshold.json`_
- **2026-07-01** [`fcb9f229b3`](https://github.com/sgl-project/sglang/commit/fcb9f229b3) [#29708](https://github.com/sgl-project/sglang/pull/29708)
  [KDA-Pilot] Add LTX2 QKNorm split-RoPE CUDA fast path (#29708)
  _Files: `python/sglang/jit_kernel/csrc/diffusion/ltx2_qknorm_split_rope.cuh`, `python/sglang/jit_kernel/diffusion/ltx2_qknorm_split_rope.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `test/registered/jit/benchmark/diffusion/bench_ltx2_qknorm_split_rope.py` _+1 more__
- **2026-06-30** [`a531d81c19`](https://github.com/sgl-project/sglang/commit/a531d81c19) [#29688](https://github.com/sgl-project/sglang/pull/29688)
  [diffusion][cache-dit] support Krea-2 + run-driven `has_separate_cfg` (#29688)
  _Files: `docs_new/cookbook/diffusion/Krea/Krea-2.mdx`, `python/sglang/multimodal_gen/runtime/cache/cache_dit_integration.py`, `python/sglang/multimodal_gen/runtime/models/dits/krea2.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py` _+1 more__
- **2026-06-30** [`bae78a44da`](https://github.com/sgl-project/sglang/commit/bae78a44da) [#29393](https://github.com/sgl-project/sglang/pull/29393)
  [Deps] Bump transformers to 5.12.1 (#29393)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` _+13 more__
- **2026-06-30** [`b6907d9664`](https://github.com/sgl-project/sglang/commit/b6907d9664) [#29634](https://github.com/sgl-project/sglang/pull/29634)
  docker: install dynamo nightly in the dev image for rapid iteration/testing (#29634)
  _Files: `.github/workflows/release-docker-dev.yml`, `docker/Dockerfile`_
- **2026-06-30** [`2068ae7eec`](https://github.com/sgl-project/sglang/commit/2068ae7eec) [#29364](https://github.com/sgl-project/sglang/pull/29364)
  [diffusion] chore: document VAE decode parallel group axes (#29364)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/test/unit/test_vae_spatial_parallel_decode.py`_
- **2026-06-30** [`3add35e26d`](https://github.com/sgl-project/sglang/commit/3add35e26d) [#29664](https://github.com/sgl-project/sglang/pull/29664)
  [Diffusion] Reuse shared AlignedVector and tidy jit_kernel/diffusion (#29664)
  _Files: `python/sglang/jit_kernel/csrc/diffusion/causal_conv3d_cat_pad.cuh`, `python/sglang/jit_kernel/csrc/diffusion/residual_gate_add.cuh`, `python/sglang/jit_kernel/csrc/diffusion/timestep_embedding.cuh`, `python/sglang/jit_kernel/diffusion/cutedsl/norm_tanh_mul_add_norm_scale.py` _+6 more__
- **2026-06-30** [`25b6051c70`](https://github.com/sgl-project/sglang/commit/25b6051c70) [#29519](https://github.com/sgl-project/sglang/pull/29519)
  [diffusion] warmup: default to model sampling resolution (declare Z-Image default) (#29519)
  _Files: `python/sglang/multimodal_gen/configs/sample/zimage.py`, `python/sglang/multimodal_gen/runtime/warmup_request_builder.py`, `python/sglang/multimodal_gen/test/server/perf_baselines.json`, `python/sglang/multimodal_gen/test/unit/test_cfg_parallel_warmup.py`_
- **2026-06-29** [`b0be644133`](https://github.com/sgl-project/sglang/commit/b0be644133) [#29649](https://github.com/sgl-project/sglang/pull/29649)
  [diffusion] feat: keep image-model auxiliary components resident under auto memory policy (#29649)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/ltx_2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/model_deployment_config.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/sana_wm.py` _+3 more__
- **2026-06-29** [`473a278dd1`](https://github.com/sgl-project/sglang/commit/473a278dd1) [#28958](https://github.com/sgl-project/sglang/pull/28958)
  model: support nvidia/LocateAnything-3B (#28958)
  _Files: `docs_new/docs/supported-models/multimodal_language_models.mdx`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/locate_anything.py`, `python/sglang/srt/configs/model_config.py` _+7 more__

## Other  (27 commits)

- **2026-07-06** [`e2b55bdbab`](https://github.com/sgl-project/sglang/commit/e2b55bdbab) [#28401](https://github.com/sgl-project/sglang/pull/28401)
  NUMA: probe numactl binding and fall back when --membind is rejected (#28401)
  _Files: `python/sglang/srt/utils/numa_utils.py`, `test/registered/utils/test_numa_utils.py`_
- **2026-07-06** [`24c42c90be`](https://github.com/sgl-project/sglang/commit/24c42c90be) [#30186](https://github.com/sgl-project/sglang/pull/30186)
  Clean up ServerArgs post-init dispatch (#30186)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/managers/test_mm_process_config.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-07-05** [`8673e85e6c`](https://github.com/sgl-project/sglang/commit/8673e85e6c) [#30153](https://github.com/sgl-project/sglang/pull/30153)
  Remove `# fmt: off` from environ.py Envs class (#30153)
  _Files: `python/sglang/srt/environ.py`_
- **2026-07-05** [`602c8615a1`](https://github.com/sgl-project/sglang/commit/602c8615a1) [#30154](https://github.com/sgl-project/sglang/pull/30154)
  [fix] Reconcile the legacy-getter ratchet baseline after racing merges (#30154)
  _Files: `test/registered/unit/test_legacy_global_ratchet.py`_
- **2026-07-05** [`3ea875fef4`](https://github.com/sgl-project/sglang/commit/3ea875fef4) [#30149](https://github.com/sgl-project/sglang/pull/30149)
  [chore] Remove the stack-review placeholder file (#30149)
  _Files: `STACK_REVIEW_PLACEHOLDER.md`_
- **2026-07-04** [`b941e337a4`](https://github.com/sgl-project/sglang/commit/b941e337a4) [#30077](https://github.com/sgl-project/sglang/pull/30077)
  [refactor] Rename Arg.model_overridable to Arg.resolvable (stack 15/15) (#30077)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-07-04** [`276fbfe880`](https://github.com/sgl-project/sglang/commit/276fbfe880) [#30074](https://github.com/sgl-project/sglang/pull/30074)
  [refactor] Migrate the page_size resolution chain (stack 12/15) (#30074)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py` _+1 more__
- **2026-07-04** [`5c95bf15c8`](https://github.com/sgl-project/sglang/commit/5c95bf15c8) [#30072](https://github.com/sgl-project/sglang/pull/30072)
  [refactor] Add the post-process resolution stage; migrate sampling_backend (stack 10/15) (#30072)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-07-04** [`ae29c5a1dc`](https://github.com/sgl-project/sglang/commit/ae29c5a1dc) [#30071](https://github.com/sgl-project/sglang/pull/30071)
  [refactor] Sweep disable_hybrid_swa_memory writers; close the dtype family (stack 9/15) (#30071)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-07-04** [`4bf4db09f6`](https://github.com/sgl-project/sglang/commit/4bf4db09f6) [#30070](https://github.com/sgl-project/sglang/pull/30070)
  [refactor] Add predicate-keyed registration; migrate the Step3p family (stack 8/15) (#30070)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-07-04** [`c3d751b231`](https://github.com/sgl-project/sglang/commit/c3d751b231) [#30067](https://github.com/sgl-project/sglang/pull/30067)
  [refactor] Add the declarative model-override registry and resolution gate (stack 5/15) (#30067)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-07-04** [`10f258257f`](https://github.com/sgl-project/sglang/commit/10f258257f) [#30066](https://github.com/sgl-project/sglang/pull/30066)
  [refactor] Add the resolved-flags tier + resolvable-field metadata (stack 4/15) (#30066)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/runtime_context.py`, `test/registered/unit/test_model_overrides.py`, `test/registered/unit/test_runtime_context.py`_
- **2026-07-04** [`ff57171f98`](https://github.com/sgl-project/sglang/commit/ff57171f98) [#30065](https://github.com/sgl-project/sglang/pull/30065)
  [refactor] Soft-deprecate the legacy global ServerArgs accessors + ratchet (stack 3/15) (#30065)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/test_legacy_global_ratchet.py`_
- **2026-07-04** [`6d662c9245`](https://github.com/sgl-project/sglang/commit/6d662c9245) [#30063](https://github.com/sgl-project/sglang/pull/30063)
  [refactor] Add a read-through server_args accessor to RuntimeContext (stack 1/15) (#30063)
  _Files: `python/sglang/srt/runtime_context.py`, `test/registered/unit/test_runtime_context.py`_
- **2026-07-03** [`e3258d3b54`](https://github.com/sgl-project/sglang/commit/e3258d3b54) [#30018](https://github.com/sgl-project/sglang/pull/30018)
  [Fix] Turn off dsa indexer fusion by default (#30018)
  _Files: `python/sglang/srt/environ.py`_
- **2026-07-02** [`c05c48b35e`](https://github.com/sgl-project/sglang/commit/c05c48b35e) [#29853](https://github.com/sgl-project/sglang/pull/29853)
  bugfix for npu Grok2 model --detokenizer without all special ids (#29853)
  _Files: `python/sglang/srt/utils/patch_tokenizer.py`_
- **2026-07-02** [`0c1a0be3b2`](https://github.com/sgl-project/sglang/commit/0c1a0be3b2) [#28190](https://github.com/sgl-project/sglang/pull/28190)
  fix(precision): do not promote failed runs to the comparison baseline (#28190)
  _Files: `python/sglang/test/precision_baseline_store.py`, `test/registered/unit/test_precision_baseline_store.py`_
- **2026-07-01** [`1a5977d41b`](https://github.com/sgl-project/sglang/commit/1a5977d41b) [#29871](https://github.com/sgl-project/sglang/pull/29871)
  [chore] Add no-getattr rule; refine no-dataclasses rule (#29871)
  _Files: `.claude/rules/no-dataclasses.md`, `.claude/rules/no-getattr-defensive.md`_
- **2026-07-01** [`76d828a4e8`](https://github.com/sgl-project/sglang/commit/76d828a4e8) [#29870](https://github.com/sgl-project/sglang/pull/29870)
  Add pranjalssh to CI_PERMISSIONS.json (#29870)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-07-01** [`721350656d`](https://github.com/sgl-project/sglang/commit/721350656d) [#29381](https://github.com/sgl-project/sglang/pull/29381)
  [NPU] Fix glm 4.6v (#29381)
  _Files: `python/sglang/srt/hardware_backend/npu/modules/glm46v_processor.py`_
- **2026-07-01** [`546d6e23ad`](https://github.com/sgl-project/sglang/commit/546d6e23ad) [#29681](https://github.com/sgl-project/sglang/pull/29681)
  fix(mlx): default prefill_aware_swa=False on MlxModelRunnerStub (#29681)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`_
- **2026-06-30** [`7d9116d9d7`](https://github.com/sgl-project/sglang/commit/7d9116d9d7) [#29376](https://github.com/sgl-project/sglang/pull/29376)
  Fix test_type_based_dispatcher after TokenizedGenerateReqInput field changes (#29376)
  _Files: `test/registered/utils/test_type_based_dispatcher.py`_
- **2026-06-30** [`8dbf04fc56`](https://github.com/sgl-project/sglang/commit/8dbf04fc56) [#29700](https://github.com/sgl-project/sglang/pull/29700)
  Add new Intel SGLang members into CI_permission list (#29700)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-06-29** [`6c018eb4d1`](https://github.com/sgl-project/sglang/commit/6c018eb4d1) [#29156](https://github.com/sgl-project/sglang/pull/29156)
  Fix bounded checkpoint prefetching and buffered drop-cache handling (#29156)
  _Files: `python/sglang/srt/model_loader/weight_utils.py`, `test/registered/unit/model_loader/test_prefetch_checkpoints.py`_
- **2026-06-29** [`bb7d3440b5`](https://github.com/sgl-project/sglang/commit/bb7d3440b5) [#29146](https://github.com/sgl-project/sglang/pull/29146)
  bugfix revise interface get cpu copy for npu mem pool to align with gpu (#29146)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-06-29** [`cd91dd0757`](https://github.com/sgl-project/sglang/commit/cd91dd0757) [#29623](https://github.com/sgl-project/sglang/pull/29623)
  fix test_weight_checker_comparator assertion and ue8m0 scale unpack (#29623)
  _Files: `python/sglang/srt/utils/weight_checker_comparator.py`, `test/registered/unit/utils/test_weight_checker_comparator.py`_
- **2026-06-29** [`d5abafcc1c`](https://github.com/sgl-project/sglang/commit/d5abafcc1c) [#28308](https://github.com/sgl-project/sglang/pull/28308)
  [Intel GPU] add pytorch profiling support for XPU in bench offline throughput and enhance num steps (#28308)
  _Files: `python/sglang/benchmark/offline_throughput.py`_

## MoE / Expert Parallel  (25 commits)

- **2026-07-05** [`8fb99bbaf8`](https://github.com/sgl-project/sglang/commit/8fb99bbaf8) [#30137](https://github.com/sgl-project/sglang/pull/30137)
  [refactor] Config resolution pipeline: full-stack review (10-PR series, review only) (#30137)
  _Files: `STACK_REVIEW_PLACEHOLDER.md`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/hisparse_hook.py`, `python/sglang/srt/arg_groups/nemotron_h_hook.py` _+70 more__
- **2026-07-04** [`3836cba9ee`](https://github.com/sgl-project/sglang/commit/3836cba9ee) [#30075](https://github.com/sgl-project/sglang/pull/30075)
  [refactor] Migrate the moe_runner_backend / quantization resolution chains (stack 13/15) (#30075)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-07-04** [`c21f6f19cf`](https://github.com/sgl-project/sglang/commit/c21f6f19cf) [#30079](https://github.com/sgl-project/sglang/pull/30079)
  [MoE] Fix moe_fused_gate out-of-range expert id on all-NaN rows (fixes eagle_dp_attention crash) (#30079)
  _Files: `python/sglang/jit_kernel/moe_fused_gate.py`_
- **2026-07-03** [`e90fec4868`](https://github.com/sgl-project/sglang/commit/e90fec4868) [#28048](https://github.com/sgl-project/sglang/pull/28048)
  [Intel GPU] DeepSeek V4 10/N : Add sqrtsoftplus support to fused_topk_torch_native (#28048)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-07-03** [`8416544ab0`](https://github.com/sgl-project/sglang/commit/8416544ab0) [#29999](https://github.com/sgl-project/sglang/pull/29999)
  [NPU] bugfix for Base class add mamba_track_indices parameter (#29999)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`, `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`_
- **2026-07-03** [`d364cd8ead`](https://github.com/sgl-project/sglang/commit/d364cd8ead) [#27349](https://github.com/sgl-project/sglang/pull/27349)
  Support DSV4 shared expert fusion for DeepEP and MegaMOE (#27349)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/moe/utils.py` _+9 more__
- **2026-07-03** [`a2d7eb303e`](https://github.com/sgl-project/sglang/commit/a2d7eb303e) [#26771](https://github.com/sgl-project/sglang/pull/26771)
  [MoE] Consolidate ungrouped + grouped gate/topk onto one Triton router (#26771) — faster than AOT on B200/H100/H200, at parity with flashinfer (#29771)
  _Files: `python/sglang/jit_kernel/csrc/moe/grouped_topk.cuh`, `python/sglang/jit_kernel/grouped_topk.py`, `python/sglang/jit_kernel/moe_fused_gate.py`, `python/sglang/srt/environ.py` _+3 more__
- **2026-07-02** [`bdd3515389`](https://github.com/sgl-project/sglang/commit/bdd3515389) [#29503](https://github.com/sgl-project/sglang/pull/29503)
  NPU case rl update weights for tensor load_format == None and flatten bucket (#29503)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/unquant.py`_
- **2026-07-02** [`26b15a0825`](https://github.com/sgl-project/sglang/commit/26b15a0825) [#29659](https://github.com/sgl-project/sglang/pull/29659)
  [LFM2-MoE] Support Transformers v5 packed MoE expert weights (#29659)
  _Files: `python/sglang/srt/models/lfm2_moe.py`_
- **2026-07-02** [`b558cc1abb`](https://github.com/sgl-project/sglang/commit/b558cc1abb) [#29867](https://github.com/sgl-project/sglang/pull/29867)
  feat(short-conv): shared ShortConvAttnBackend for ZAYA1 CCA + LFM2 short conv (#29867)
  _Files: `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/short_conv_backend.py`, `python/sglang/srt/layers/attention/mamba/causal_conv1d.py` _+4 more__
- **2026-07-01** [`c312cdd3a7`](https://github.com/sgl-project/sglang/commit/c312cdd3a7) [#29554](https://github.com/sgl-project/sglang/pull/29554)
  Upgrading tvm-ffi/sgl-deep-gemm/tilelang (#29554)
  _Files: `python/pyproject.toml`, `python/sglang/srt/layers/attention/dsa/tilelang_kernel.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/mhc.py` _+1 more__
- **2026-07-01** [`779ea4a9b5`](https://github.com/sgl-project/sglang/commit/779ea4a9b5) [#28676](https://github.com/sgl-project/sglang/pull/28676)
  [RL] fix deepseek v4 MXFP8 flashinfer_trtllm_routed MoE weight update (#28676)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `test/registered/rl/test_update_weights_from_disk_blackwell.py`_
- **2026-07-01** [`eb75d990f7`](https://github.com/sgl-project/sglang/commit/eb75d990f7) [#29761](https://github.com/sgl-project/sglang/pull/29761)
  [Bugfix] compressed-tensors WNA16 MoE: don't assume a "Linear" config group (#29761)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`, `test/registered/unit/layers/quantization/test_compressed_tensors_wna16_moe_no_linear.py`_
- **2026-07-01** [`8ee200972e`](https://github.com/sgl-project/sglang/commit/8ee200972e) [#26255](https://github.com/sgl-project/sglang/pull/26255)
  [fix] Add support for flashinfer MOE A2A to Qwen3 BF16 model path (#26255)
  _Files: `python/sglang/srt/layers/moe/utils.py`, `sgl-kernel/csrc/moe/moe_topk_softmax_kernels.cu`, `test/registered/moe/test_flashinfer_a2a_cutlass.py`_
- **2026-07-01** [`df0dfbaa45`](https://github.com/sgl-project/sglang/commit/df0dfbaa45) [#29636](https://github.com/sgl-project/sglang/pull/29636)
  [Kernel] Strengthen kernel shape coverage (#29636)
  _Files: `sgl-kernel/tests/test_dsv3_fused_a_gemm.py`, `sgl-kernel/tests/test_fp8_gemm.py`, `sgl-kernel/tests/test_norm.py`, `sgl-kernel/tests/test_per_token_quant_fp8.py` _+11 more__
- **2026-07-01** [`a7390b17f8`](https://github.com/sgl-project/sglang/commit/a7390b17f8) [#29793](https://github.com/sgl-project/sglang/pull/29793)
  [NPU]Modify --lora-backend & --moe-runner-backend description. (#29793)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-06-30** [`cf36dca6d4`](https://github.com/sgl-project/sglang/commit/cf36dca6d4) [#25835](https://github.com/sgl-project/sglang/pull/25835)
  [JIT Kernel] Triton moe fused gate (#25835)
  _Files: `python/sglang/jit_kernel/csrc/moe/moe_fused_gate.cuh`, `python/sglang/jit_kernel/moe_fused_gate.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/jit/benchmark/bench_moe_fused_gate.py` _+1 more__
- **2026-06-30** [`c6a7c98ae4`](https://github.com/sgl-project/sglang/commit/c6a7c98ae4) [#29509](https://github.com/sgl-project/sglang/pull/29509)
  [NPU]GLM-4.7-Flash optimize with fused kernels (#29509)
  _Files: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/hardware_backend/npu/moe/topk.py`_
- **2026-06-30** [`a5e6dd3767`](https://github.com/sgl-project/sglang/commit/a5e6dd3767) [#27204](https://github.com/sgl-project/sglang/pull/27204)
  [AMD] Implement QuarkW4A8MXFp4MoE to support amd/gpt-oss-120b-w-mxfp4-a-fp8 (#27204)
  _Files: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/__init__.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`, `python/sglang/srt/layers/quantization/quark/weights.py` _+2 more__
- **2026-06-30** [`89620b9169`](https://github.com/sgl-project/sglang/commit/89620b9169) [#28980](https://github.com/sgl-project/sglang/pull/28980)
  [NPU] Support DeepSeek V4 Flash MTP on Ascend (#28980)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_allocator.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_common_hooks.py` _+9 more__
- **2026-06-29** [`a6bc432fd8`](https://github.com/sgl-project/sglang/commit/a6bc432fd8) [#18612](https://github.com/sgl-project/sglang/pull/18612)
  [Perf][Kernel] Fuse SiLU+Mul into NVFP4 Expert Quantization for CUTLASS MoE (#18612)
  _Files: `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_expert_quant.cuh`, `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_quant_entry.cuh`, `python/sglang/jit_kernel/nvfp4.py`, `python/sglang/srt/layers/moe/cutlass_moe.py` _+3 more__
- **2026-06-29** [`b8c25bfaa7`](https://github.com/sgl-project/sglang/commit/b8c25bfaa7) [#22394](https://github.com/sgl-project/sglang/pull/22394)
  [NVIDIA] Support flashinfer a2a with flashinfer_trtllm_routed moe (#22394)
  _Files: `docs_new/docs/advanced_features/expert_parallelism.mdx`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-06-29** [`6bdecb8206`](https://github.com/sgl-project/sglang/commit/6bdecb8206) [#29463](https://github.com/sgl-project/sglang/pull/29463)
  [DeepSeek V3] Reland: run routed experts on main stream in dual-stream MoE (#29463)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-06-29** [`93926b9a95`](https://github.com/sgl-project/sglang/commit/93926b9a95) [#29640](https://github.com/sgl-project/sglang/pull/29640)
  Add Qwen3 MoE tests for PP compatibility with CP and DP (#29640)
  _Files: `test/registered/pp/test_pp_parallel_compat.py`_
- **2026-06-29** [`f85cc94d82`](https://github.com/sgl-project/sglang/commit/f85cc94d82) [#29505](https://github.com/sgl-project/sglang/pull/29505)
  [NPU] Qwen3-VL-30B use split_qkv_rmsnorm_rope for extend (#29505)
  _Files: `python/sglang/srt/models/qwen3_moe.py`_

## KV Cache / Memory  (17 commits)

- **2026-07-03** [`430418e218`](https://github.com/sgl-project/sglang/commit/430418e218) [#30001](https://github.com/sgl-project/sglang/pull/30001)
  [NPU] bugfix for dsv4 memory pool (#30001)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_memory_pool.py`_
- **2026-07-02** [`f19246e59a`](https://github.com/sgl-project/sglang/commit/f19246e59a) [#29817](https://github.com/sgl-project/sglang/pull/29817)
  [HiCache] write_back policy refinement (#29817)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`_
- **2026-07-02** [`a375e9f3da`](https://github.com/sgl-project/sglang/commit/a375e9f3da) [#29860](https://github.com/sgl-project/sglang/pull/29860)
  Fix SWA eviction tombstoning the last leaf (#29860)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `test/registered/unit/mem_cache/test_swa_eviction_boundary.py` _+1 more__
- **2026-07-02** [`0ae76117ef`](https://github.com/sgl-project/sglang/commit/0ae76117ef) [#29680](https://github.com/sgl-project/sglang/pull/29680)
  [AMD] Register 2 CPU/ROCm-safe tests for AMD 1-GPU PR CI (#29680)
  _Files: `test/registered/models/test_vit_pos_embed_interpolate.py`, `test/registered/unit/mem_cache/test_minimax_sparse_pool_host_unit.py`_
- **2026-07-02** [`70df09b833`](https://github.com/sgl-project/sglang/commit/70df09b833) [#27923](https://github.com/sgl-project/sglang/pull/27923)
  Fix MambaPool.clear_slots OOM by replacing expand-based tensor allocation with scalar zeroing (#27923)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-07-01** [`3adfd0f34b`](https://github.com/sgl-project/sglang/commit/3adfd0f34b) [#29782](https://github.com/sgl-project/sglang/pull/29782)
  [AMD] Register 3 unit mem_cache + utils tests for stage-b-test-1-gpu-small-amd (#29782)
  _Files: `test/registered/unit/mem_cache/test_hiradix_cache_unit.py`, `test/registered/unit/mem_cache/test_triton_kernel_layout.py`, `test/registered/unit/utils/test_common.py`_
- **2026-07-01** [`13dc5f2dc7`](https://github.com/sgl-project/sglang/commit/13dc5f2dc7) [#25377](https://github.com/sgl-project/sglang/pull/25377)
  [HiCache][AMD] Add UMBP tiered DRAM + SSD L3 storage backend with hugepage host allocator   (#25377)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/pool_host/common.py`, `python/sglang/srt/mem_cache/storage/backend_factory.py`, `python/sglang/srt/mem_cache/storage/umbp/__init__.py` _+5 more__
- **2026-07-01** [`1e80d938ff`](https://github.com/sgl-project/sglang/commit/1e80d938ff) [#29823](https://github.com/sgl-project/sglang/pull/29823)
  [HiCache]fix draft host pool allocator type (#29823)
  _Files: `python/sglang/srt/mem_cache/kv_cache_builder.py`_
- **2026-07-01** [`7d9de81cda`](https://github.com/sgl-project/sglang/commit/7d9de81cda) [#27060](https://github.com/sgl-project/sglang/pull/27060)
  feat(hicache): Use NIXL path-mode (#27060)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/nixl_registry.py`, `python/sglang/srt/mem_cache/storage/nixl/nixl_utils.py`, `test/registered/unit/mem_cache/test_hicache_nixl_storage.py`_
- **2026-07-01** [`5e1ccd9320`](https://github.com/sgl-project/sglang/commit/5e1ccd9320) [#28287](https://github.com/sgl-project/sglang/pull/28287)
  [HiCache] Optimize HiCache hash generation with bulk token byte conversion (#28287)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/cpp_utils/hash_binding.cpp`, `python/sglang/srt/mem_cache/cpp_utils/native_hash.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py` _+3 more__
- **2026-06-30** [`53c61bd5e6`](https://github.com/sgl-project/sglang/commit/53c61bd5e6) [#29352](https://github.com/sgl-project/sglang/pull/29352)
  [bug2] skip swa recovery on locked full kv (#29352)
  _Files: `python/sglang/srt/mem_cache/allocator/swa.py`, `python/sglang/srt/mem_cache/swa_radix_cache.py`, `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-06-30** [`1c2523b719`](https://github.com/sgl-project/sglang/commit/1c2523b719) [#29351](https://github.com/sgl-project/sglang/pull/29351)
  [bug1] keep full kv when swa skips leaf data (#29351)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/README.md`, `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/tree_component.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+1 more__
- **2026-06-30** [`cc238270b1`](https://github.com/sgl-project/sglang/commit/cc238270b1) [#29686](https://github.com/sgl-project/sglang/pull/29686)
  Update GLM tests to 5.2 and delete redundant tests (#29686)
  _Files: `test/registered/8-gpu-models/test_deepseek_v32.py`, `test/registered/8-gpu-models/test_glm52_fp8.py`, `test/registered/cuda_graph/piecewise/test_pcg_glm52_fp4.py`, `test/registered/cuda_graph/piecewise/test_pcg_glm52_fp8_tp8.py` _+12 more__
- **2026-06-29** [`e6c15f76f3`](https://github.com/sgl-project/sglang/commit/e6c15f76f3) [#29350](https://github.com/sgl-project/sglang/pull/29350)
  [optimize] fix swa eviction boundary for unfinished inserts (#29350)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-06-29** [`f76e707f59`](https://github.com/sgl-project/sglang/commit/f76e707f59) [#29546](https://github.com/sgl-project/sglang/pull/29546)
  Clean up follow-ups for eagle hidden dim clean up (#29546)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`_
- **2026-06-29** [`e1ca92a7fd`](https://github.com/sgl-project/sglang/commit/e1ca92a7fd) [#28974](https://github.com/sgl-project/sglang/pull/28974)
  [weight checker] refactor: add precision branch; allow ULP quant err; used chunked compare (#28974)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler_components/weight_updater.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/utils/weight_checker.py` _+3 more__
- **2026-06-29** [`bd2a5db987`](https://github.com/sgl-project/sglang/commit/bd2a5db987) [#29310](https://github.com/sgl-project/sglang/pull/29310)
  [HiCache] Detect for double-free in HostKVCache (#29310)
  _Files: `python/sglang/srt/mem_cache/pool_host/base.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py`_

## Quantization  (14 commits)

- **2026-07-06** [`b1942fc3ea`](https://github.com/sgl-project/sglang/commit/b1942fc3ea) [#27906](https://github.com/sgl-project/sglang/pull/27906)
  [Model] Support Qwen3.6 ModelOpt mixed NVFP4 (#27906)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/layers/vocab_parallel_embedding.py` _+4 more__
- **2026-07-05** [`67361ff91b`](https://github.com/sgl-project/sglang/commit/67361ff91b) [#29855](https://github.com/sgl-project/sglang/pull/29855)
  [AMD][DI][CI] 3/N Add Kimi K2.6 FP8 MI355X 1P1D nightly recipes (#29855)
  _Files: `scripts/ci/slurm/launch_mi355x.sh`, `scripts/ci/slurm/nightly-configs.yaml`, `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/1p1d-mtp.yaml`, `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/1p1d.yaml`_
- **2026-07-05** [`a37bc2456d`](https://github.com/sgl-project/sglang/commit/a37bc2456d) [#30118](https://github.com/sgl-project/sglang/pull/30118)
  [diffusion] refactor: consolidate diffusion weight load planning (#30118)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/bridge_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py` _+3 more__
- **2026-07-04** [`b7c3709f33`](https://github.com/sgl-project/sglang/commit/b7c3709f33) [#29903](https://github.com/sgl-project/sglang/pull/29903)
  [diffusion] fix: fix z-Image online fp8 quantization crash with dit_cpu_offload (#29903)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/zimage.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py` _+2 more__
- **2026-07-03** [`70a813493f`](https://github.com/sgl-project/sglang/commit/70a813493f) [#29937](https://github.com/sgl-project/sglang/pull/29937)
  [NPU] [DOC] add missing DEEP_NORMAL_MODE_USE_INT8_QUANT for w8a8+deepep scenarios (#29937)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_environment_variables.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_glm5.2_examples.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_optimization.mdx` _+2 more__
- **2026-07-03** [`05bc3f2aa7`](https://github.com/sgl-project/sglang/commit/05bc3f2aa7) [#29918](https://github.com/sgl-project/sglang/pull/29918)
  [AMD] Gate broken CK block-FP8 GEMM shapes to aiter-triton-GEMM to fix ROCm 7.0 Qwen3.5 accuracy (#29918)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-07-02** [`cfb9c574d3`](https://github.com/sgl-project/sglang/commit/cfb9c574d3) [#29956](https://github.com/sgl-project/sglang/pull/29956)
  Fix UE8M0 scale rounding for DeepGEMM (#29956)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/manual/quant/test_block_fp8_deep_gemm_blackwell.py`_
- **2026-07-02** [`cb06c4e6ce`](https://github.com/sgl-project/sglang/commit/cb06c4e6ce) [#29497](https://github.com/sgl-project/sglang/pull/29497)
  [CPU] Fix model failures on Xeon (#29497)
  _Files: `docker/xeon.Dockerfile`, `docs_new/docs/hardware-platforms/cpu_server.mdx`, `python/pyproject_cpu.toml`, `python/sglang/srt/layers/quantization/mxfp4.py` _+2 more__
- **2026-07-02** [`0543246184`](https://github.com/sgl-project/sglang/commit/0543246184) [#29458](https://github.com/sgl-project/sglang/pull/29458)
  Enable Breakable Cuda Graph as Default (#29458)
  _Files: `python/sglang/srt/model_executor/cuda_graph_config.py`, `python/sglang/srt/model_executor/runner/__init__.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_backend_utils/__init__.py` _+6 more__
- **2026-07-01** [`8361561c24`](https://github.com/sgl-project/sglang/commit/8361561c24) [#29694](https://github.com/sgl-project/sglang/pull/29694)
  [AMD] Fix int8 per-token quant Triton portability + register test for AMD nightly CI (#29694)
  _Files: `python/sglang/srt/layers/quantization/int8_kernel.py`, `test/registered/quant/test_int8_kernel.py`_
- **2026-07-01** [`2a6e5c60fe`](https://github.com/sgl-project/sglang/commit/2a6e5c60fe) [#29726](https://github.com/sgl-project/sglang/pull/29726)
  [AMD] Rebalance stage-c-large-8-gpu-mi35x partitions to fix 60-min timeout (#29726)
  _Files: `test/registered/amd/test_deepseek_r1_mxfp4_8gpu.py`, `test/registered/amd/test_kimi_k25_mxfp4.py`, `test/registered/amd/test_kimi_k25_mxfp4_bcg_mi35x.py`, `test/registered/amd/test_qwen3_coder_next_8gpu.py` _+1 more__
- **2026-07-01** [`548f505cc5`](https://github.com/sgl-project/sglang/commit/548f505cc5) [#29290](https://github.com/sgl-project/sglang/pull/29290)
  [AMD] Cover DeepSeek-R1 MXFP4 TP4 MTP nightly CI (#29290)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mtp_mi35x.py`_
- **2026-07-01** [`8205aa3603`](https://github.com/sgl-project/sglang/commit/8205aa3603) [#29789](https://github.com/sgl-project/sglang/pull/29789)
  chore: clean diffusion dead code (#29789)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/qwen_image.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/nodes.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/test/test_flux_pipeline.py` _+37 more__
- **2026-06-29** [`06fd2efedd`](https://github.com/sgl-project/sglang/commit/06fd2efedd) [#29029](https://github.com/sgl-project/sglang/pull/29029)
  [NPU][Bugfix] Fix a ModelSlim loading failure (#29029)
  _Files: `python/sglang/srt/layers/quantization/modelslim/modelslim.py`_

## Prefill / Decode Disaggregation  (14 commits)

- **2026-07-05** [`fbe3110866`](https://github.com/sgl-project/sglang/commit/fbe3110866) [#29615](https://github.com/sgl-project/sglang/pull/29615)
  Make mem_fraction_static reserve disaggregation-mode aware (#29615)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-04** [`754524d8de`](https://github.com/sgl-project/sglang/commit/754524d8de) [#30139](https://github.com/sgl-project/sglang/pull/30139)
  [Fix] Skip cross-node probe in MultimemAllGatherer on single-node runs (fixes mooncake EP segfault) (#30139)
  _Files: `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py`_
- **2026-07-02** [`caf2e5da2d`](https://github.com/sgl-project/sglang/commit/caf2e5da2d) [#29756](https://github.com/sgl-project/sglang/pull/29756)
  [AMD] Fix MiniMax M3 state transfer in Mori PD (#29756)
  _Files: `python/sglang/srt/disaggregation/mori/conn.py`_
- **2026-07-02** [`cba3801f52`](https://github.com/sgl-project/sglang/commit/cba3801f52) [#29544](https://github.com/sgl-project/sglang/pull/29544)
  docs: add PD disaggregation to GLM-5.2 cookbook playground (#29544)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs_new/src/snippets/_playground.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-07-02** [`b276a9acee`](https://github.com/sgl-project/sglang/commit/b276a9acee) [#29770](https://github.com/sgl-project/sglang/pull/29770)
  chore: cleanup garbage code (#29770)
  _Files: `benchmark/bench_linear_attention/bench_gdn_decode.py`, `benchmark/mmmu/bench_hf.py`, `experimental/sgl-router/BENCHMARKS.md`, `experimental/sgl-router/src/workers/manager.rs` _+51 more__
- **2026-07-02** [`a3f6680874`](https://github.com/sgl-project/sglang/commit/a3f6680874) [#27730](https://github.com/sgl-project/sglang/pull/27730)
  [AMD]: docker(rocm) bump Mooncake to latest main + enable multi-protocol (#27730)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `docker/rocm.Dockerfile`_
- **2026-07-01** [`30c9801b39`](https://github.com/sgl-project/sglang/commit/30c9801b39) [#29211](https://github.com/sgl-project/sglang/pull/29211)
  [disagg] Fix KV-event publisher port collision under pure data parallelism (#29211)
  _Files: `python/sglang/srt/disaggregation/kv_events.py`, `python/sglang/srt/managers/scheduler_components/kv_events_publisher.py`, `test/registered/unit/disaggregation/test_kv_events.py`_
- **2026-07-01** [`5de66d7fbc`](https://github.com/sgl-project/sglang/commit/5de66d7fbc) [#29296](https://github.com/sgl-project/sglang/pull/29296)
  [EPD][BugFix] Fix encoder health check with global cache TP (#29296)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`_
- **2026-07-01** [`56f22cd520`](https://github.com/sgl-project/sglang/commit/56f22cd520) [#28612](https://github.com/sgl-project/sglang/pull/28612)
  Optimize C128 state pool allocation using request state pool (#28612)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/c128_online_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/online_c128_mtp.cuh`, `python/sglang/jit_kernel/dsv4/__init__.py` _+28 more__
- **2026-06-30** [`e721259079`](https://github.com/sgl-project/sglang/commit/e721259079) [#25153](https://github.com/sgl-project/sglang/pull/25153)
  typo-fix: correct mooncake package name to "mooncake-transfer-engine" (#25153)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-06-30** [`97fc4dfd73`](https://github.com/sgl-project/sglang/commit/97fc4dfd73) [#28586](https://github.com/sgl-project/sglang/pull/28586)
  [Doc]Checking and modifying Markdown formatting issues and link validity (#28586)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_contribution_guide.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx` _+10 more__
- **2026-06-30** [`dad0120c57`](https://github.com/sgl-project/sglang/commit/dad0120c57) [#29710](https://github.com/sgl-project/sglang/pull/29710)
  [HiSparse]: Skip flaky hisparse-nixl ci (#29710)
  _Files: `test/registered/disaggregation/test_disaggregation_hisparse.py`_
- **2026-06-30** [`6bf15aa2b9`](https://github.com/sgl-project/sglang/commit/6bf15aa2b9) [#28348](https://github.com/sgl-project/sglang/pull/28348)
  [AMD]: Enable NIXL PD disaggregation for ROCm(1/n)  (#28348)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/release-docker-amd-nightly.yml`, `.github/workflows/release-docker-amd-rocm720-nightly.yml` _+2 more__
- **2026-06-29** [`3b1b512a9a`](https://github.com/sgl-project/sglang/commit/3b1b512a9a) [#29570](https://github.com/sgl-project/sglang/pull/29570)
  Fix disaggregation receiver ZMQ cleanup (#29570)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`_

## Tensor / Data Parallel  (12 commits)

- **2026-07-06** [`7c9bb316cf`](https://github.com/sgl-project/sglang/commit/7c9bb316cf) [#30214](https://github.com/sgl-project/sglang/pull/30214)
  docs(cookbook): total (input+output) throughput per GPU + percentile latency labels (#30214)
  _Files: `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/benchmarks.jsx.tmpl`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-review-pr/SKILL.md` _+9 more__
- **2026-07-04** [`df6491d80c`](https://github.com/sgl-project/sglang/commit/df6491d80c) [#30068](https://github.com/sgl-project/sglang/pull/30068)
  [refactor] Wire the config resolution pipeline (dispatch, stash, dual-apply, publish) (stack 6/15) (#30068)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-07-04** [`576dc31e33`](https://github.com/sgl-project/sglang/commit/576dc31e33) [#29881](https://github.com/sgl-project/sglang/pull/29881)
  Avoid logits multimem all-gather on cross-node TP groups (#29881)
  _Files: `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py`_
- **2026-07-03** [`1f0f353d92`](https://github.com/sgl-project/sglang/commit/1f0f353d92) [#30021](https://github.com/sgl-project/sglang/pull/30021)
  [CI] Add GLM52 NVFP4 MTP B200 tests (#30021)
  _Files: `python/sglang/test/server_fixtures/dsa_mtp_fixture.py`, `test/registered/models_e2e/test_dsa_glm52_nvfp4_dp_mtp.py`, `test/registered/models_e2e/test_dsa_glm52_nvfp4_tp_mtp.py`_
- **2026-07-03** [`2b3223a953`](https://github.com/sgl-project/sglang/commit/2b3223a953) [#29017](https://github.com/sgl-project/sglang/pull/29017)
  [model-gateway] PD router: cancel paired decode when prefill fails (#29017)
  _Files: `sgl-model-gateway/src/routers/http/pd_router.rs`_
- **2026-07-02** [`aff44d748d`](https://github.com/sgl-project/sglang/commit/aff44d748d) [#20072](https://github.com/sgl-project/sglang/pull/20072)
  [CPU] Padding for dim divisibility in TP3/6 cases (#20072)
  _Files: `python/sglang/srt/configs/update_config.py`, `python/sglang/srt/models/gpt_oss.py`, `python/sglang/srt/models/mllama.py`, `python/sglang/srt/models/mllama4.py` _+2 more__
- **2026-07-01** [`5ae214f18b`](https://github.com/sgl-project/sglang/commit/5ae214f18b) [#29621](https://github.com/sgl-project/sglang/pull/29621)
  Extract reusable VMM shareable-handle helpers from register_graph_inputs (#29621)
  _Files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `python/sglang/srt/distributed/device_communicators/vmm_utils.py`, `test/registered/unit/distributed/test_vmm_utils.py`_
- **2026-07-01** [`5134dcdcab`](https://github.com/sgl-project/sglang/commit/5134dcdcab) [#28908](https://github.com/sgl-project/sglang/pull/28908)
  [Intel XPU] Initially add nightly GSM8K accuracy tests for Llama-3.1-8B (TP=2) and Qwen3-32B (TP=4) (#28908)
  _Files: `.codespellrc`, `.github/workflows/nightly-test-intel.yml`, `python/sglang/test/xpu/__init__.py`, `python/sglang/test/xpu/simple_eval_gsm8k_xpu_mixin.py` _+4 more__
- **2026-07-01** [`40594bd381`](https://github.com/sgl-project/sglang/commit/40594bd381) [#29684](https://github.com/sgl-project/sglang/pull/29684)
  [passthrough] engine: zstd request-body decompression + header overrides (#29684)
  _Files: `python/pyproject.toml`, `python/sglang/srt/entrypoints/http_request_decompression.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/request_headers.py` _+3 more__
- **2026-06-30** [`99b8f36cb1`](https://github.com/sgl-project/sglang/commit/99b8f36cb1) [#27948](https://github.com/sgl-project/sglang/pull/27948)
  Skip custom all-reduce v2 CUDA graph capture with torch memory saver. (#27948)
  _Files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`_
- **2026-06-29** [`5106b42cbd`](https://github.com/sgl-project/sglang/commit/5106b42cbd) [#29557](https://github.com/sgl-project/sglang/pull/29557)
  [cookbook] GLM-5.2 NVFP4 B300: TP8 recipe + 3 strategies (#29557)
  _Files: `docs_new/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-06-29** [`c7b9b92d9a`](https://github.com/sgl-project/sglang/commit/c7b9b92d9a) [#29596](https://github.com/sgl-project/sglang/pull/29596)
  Fix CI caused by https://github.com/sgl-project/sglang/pull/29576 (#29596)
  _Files: `test/registered/kernels/test_dsa_indexer.py`_

## Docs / Examples  (11 commits)

- **2026-07-06** [`b3ab56545b`](https://github.com/sgl-project/sglang/commit/b3ab56545b) [#25364](https://github.com/sgl-project/sglang/pull/25364)
  Add Accuracy Benchmark for OCR models (#25364)
  _Files: `benchmark/ocr/README.md`, `benchmark/ocr/bench_sglang.py`, `benchmark/ocr/eval_utils.py`, `benchmark/ocr/generate_report.py` _+5 more__
- **2026-07-06** [`6f22790943`](https://github.com/sgl-project/sglang/commit/6f22790943) [#30201](https://github.com/sgl-project/sglang/pull/30201)
  cookbook: add Hunyuan 3 (Hy3) Day-0 page (#30201)
  _Files: `docs_new/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`, `docs_new/cookbook/autoregressive/Tencent/Hy3.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json` _+2 more__
- **2026-07-03** [`2fe7182e75`](https://github.com/sgl-project/sglang/commit/2fe7182e75) [#30011](https://github.com/sgl-project/sglang/pull/30011)
  [DOC] [NPU] update supported features on ascend npu (#30011)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/model-tutorials/glm_5_2.mdx`_
- **2026-07-03** [`a6bc7fef90`](https://github.com/sgl-project/sglang/commit/a6bc7fef90) [#29828](https://github.com/sgl-project/sglang/pull/29828)
  glm5.2 on ascend doc (new version) (#29828)
  _Files: `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/model-tutorials/glm_5_2.mdx`_
- **2026-07-03** [`91d7645aca`](https://github.com/sgl-project/sglang/commit/91d7645aca) [#29990](https://github.com/sgl-project/sglang/pull/29990)
  docs: sync LMSYS SGLang blog cards (#29990)
  _Files: `docs_new/index.mdx`_
- **2026-07-02** [`85e71b7e13`](https://github.com/sgl-project/sglang/commit/85e71b7e13) [#29974](https://github.com/sgl-project/sglang/pull/29974)
  [Doc] Cookbook Laguna-XS-2.1: add AIME25 accuracy (B300 + GB300) (#29974)
  _Files: `docs_new/src/snippets/configs/poolside/laguna-xs21-benchmarks.jsx`, `docs_new/src/snippets/configs/poolside/laguna-xs21.jsx`_
- **2026-06-30** [`081a01c37d`](https://github.com/sgl-project/sglang/commit/081a01c37d) [#29307](https://github.com/sgl-project/sglang/pull/29307)
  docs: sync LMSYS SGLang blog cards (#29307)
  _Files: `docs_new/index.mdx`_
- **2026-06-29** [`11b7ed7c9e`](https://github.com/sgl-project/sglang/commit/11b7ed7c9e) [#29676](https://github.com/sgl-project/sglang/pull/29676)
  [Docs] Add --prerelease=allow so uv installs the latest sglang (#29676)
  _Files: `docs_new/docs/get-started/install.mdx`, `docs_new/docs/get-started/quickstart.mdx`_
- **2026-06-29** [`74a197af9d`](https://github.com/sgl-project/sglang/commit/74a197af9d) [#29674](https://github.com/sgl-project/sglang/pull/29674)
  docs: add B200 NVFP4 recipes + benchmarks to GLM-5.2 cookbook (#29674)
  _Files: `docs_new/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-06-29** [`489017b3d6`](https://github.com/sgl-project/sglang/commit/489017b3d6) [#29632](https://github.com/sgl-project/sglang/pull/29632)
  [NPU] [DOC] Update deterministic inference feature support status to A2, A3 (#29632)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-06-29** [`38d4ffcd86`](https://github.com/sgl-project/sglang/commit/38d4ffcd86) [#28731](https://github.com/sgl-project/sglang/pull/28731)
  [cookbook] drop redundant serve flags (GLM-5.2) + fix M3 page-size note (#28731)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs_new/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx` _+1 more__

## Triton / Kernels  (11 commits)

- **2026-07-06** [`c016c6f355`](https://github.com/sgl-project/sglang/commit/c016c6f355) [#26788](https://github.com/sgl-project/sglang/pull/26788)
  [JIT Kernel] DeepSeek-V4 DSA indexer: faster top-k + page-table transform (runtime k <= 2048) (#26788)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/jit_kernel/dsv4/topk.py`, `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/topk/cluster.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/topk/common.cuh` _+7 more__
- **2026-07-03** [`e81f05cf4f`](https://github.com/sgl-project/sglang/commit/e81f05cf4f) [#29988](https://github.com/sgl-project/sglang/pull/29988)
  [dsv4] Trigger MHC prenorm prewarm at weight-load time with rank sync (#29988)
  _Files: `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/kernels/test_mhc_kernels.py`_
- **2026-07-02** [`790156c98f`](https://github.com/sgl-project/sglang/commit/790156c98f) [#27915](https://github.com/sgl-project/sglang/pull/27915)
  [Intel GPU] DeepSeek V4 7/N: Support fused_rope_inplace on XPU using triton (#27915)
  _Files: `python/sglang/jit_kernel/dsv4/elementwise.py`_
- **2026-07-02** [`80ac11eda3`](https://github.com/sgl-project/sglang/commit/80ac11eda3) [#29866](https://github.com/sgl-project/sglang/pull/29866)
  Fix capture-mode detection during breakable CUDA graph capture (#29866)
  _Files: `python/sglang/srt/model_executor/runner_utils/capture_mode.py`_
- **2026-07-01** [`07ca24372b`](https://github.com/sgl-project/sglang/commit/07ca24372b) [#29667](https://github.com/sgl-project/sglang/pull/29667)
  Add fused EH norm for DeepSeek NextN (#29667)
  _Files: `python/sglang/jit_kernel/csrc/elementwise/fused_eh_norm.cuh`, `python/sglang/jit_kernel/fused_eh_norm.py`, `python/sglang/srt/models/deepseek_nextn.py`, `test/registered/jit/benchmark/bench_fused_eh_norm.py` _+1 more__
- **2026-07-01** [`5b76f55d90`](https://github.com/sgl-project/sglang/commit/5b76f55d90) [#29166](https://github.com/sgl-project/sglang/pull/29166)
  [Fix]: Inline H2D during CUDA graph capture to avoid stream isolation in Offloader (#29166)
  _Files: `python/sglang/srt/utils/offloader.py`_
- **2026-06-30** [`2f730e299f`](https://github.com/sgl-project/sglang/commit/2f730e299f) [#28053](https://github.com/sgl-project/sglang/pull/28053)
  Disable dsr1 prefill cudagraphs by default (#28053)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-29** [`a5c45a12bb`](https://github.com/sgl-project/sglang/commit/a5c45a12bb) [#29625](https://github.com/sgl-project/sglang/pull/29625)
  CUDA graph executable dedup via cudaGraphExecUpdate (#29625)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/runner_backend/breakable_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_backend/cuda_graph_dedup_mixin.py`, `python/sglang/srt/model_executor/runner_backend_utils/breakable_cuda_graph/breakable_cuda_graph.py`_
- **2026-06-29** [`bd3b252e0a`](https://github.com/sgl-project/sglang/commit/bd3b252e0a) [#29382](https://github.com/sgl-project/sglang/pull/29382)
  [CPU] use faster exp in silu_and_mul (#29382)
  _Files: `sgl-kernel/csrc/cpu/activation.cpp`_
- **2026-06-29** [`909123ddb8`](https://github.com/sgl-project/sglang/commit/909123ddb8) [#29591](https://github.com/sgl-project/sglang/pull/29591)
  [misc] Use --cuda-graph-max-bs-decode in tests, examples, and docs (#29591)
- **2026-06-29** [`3217410cf6`](https://github.com/sgl-project/sglang/commit/3217410cf6) [#29378](https://github.com/sgl-project/sglang/pull/29378)
  [CPU] enable fused_sigmoid_mul on CPU device (#29378)
  _Files: `python/sglang/srt/models/qwen3_5.py`, `sgl-kernel/csrc/cpu/activation.cpp`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`, `test/registered/cpu/test_activation.py`_

## Models  (11 commits)

- **2026-07-05** [`92a1f6e06c`](https://github.com/sgl-project/sglang/commit/92a1f6e06c) [#30151](https://github.com/sgl-project/sglang/pull/30151)
  [refactor] Reorder ServerArgs sections common-first; inline LLAMA4/MIMO_V2 arch tuples (#30151)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-04** [`7ea2284551`](https://github.com/sgl-project/sglang/commit/7ea2284551) [#30076](https://github.com/sgl-project/sglang/pull/30076)
  [refactor] Migrate the DeepSeek family and the parallel-request chains (stack 14/15) (#30076)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-07-04** [`8d8f17e28c`](https://github.com/sgl-project/sglang/commit/8d8f17e28c) [#30069](https://github.com/sgl-project/sglang/pull/30069)
  [refactor] Migrate the first override families: Mistral/Pixtral dtype, MiniMaxM2, MiMoV2 (stack 7/15) (#30069)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-07-04** [`4028304579`](https://github.com/sgl-project/sglang/commit/4028304579) [#30088](https://github.com/sgl-project/sglang/pull/30088)
  [DSA] Disable indexer fusion by default to restore DeepSeek-V3.2 accuracy (#30088)
  _Files: `python/sglang/srt/environ.py`_
- **2026-07-02** [`9588cacaa1`](https://github.com/sgl-project/sglang/commit/9588cacaa1) [#29758](https://github.com/sgl-project/sglang/pull/29758)
  Remove transformers 5.12.1 dead-code workarounds (#29758)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/kimi_k25.py`_
- **2026-07-02** [`1c75243f5e`](https://github.com/sgl-project/sglang/commit/1c75243f5e) [#29905](https://github.com/sgl-project/sglang/pull/29905)
  docs: add Qwen3.6-27B-NVFP4 variant to cookbook (#29905)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs_new/src/snippets/autoregressive/qwen36-deployment.jsx`_
- **2026-07-01** [`677a11bfa9`](https://github.com/sgl-project/sglang/commit/677a11bfa9) [#29827](https://github.com/sgl-project/sglang/pull/29827)
  [Doc] Tiny update dsv4 doc (#29827)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`_
- **2026-06-30** [`ff51acd67b`](https://github.com/sgl-project/sglang/commit/ff51acd67b) [#29627](https://github.com/sgl-project/sglang/pull/29627)
  [NPU] Qwen3-VL-8B use split_qkv_rmsnorm_rope for extend (#29627)
  _Files: `python/sglang/srt/models/qwen3.py`_
- **2026-06-30** [`f41d455f37`](https://github.com/sgl-project/sglang/commit/f41d455f37) [#27887](https://github.com/sgl-project/sglang/pull/27887)
  [Model] Add HrmTextForCausalLM (Hierarchical Reasoning Model - Text) (#27887)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/hrm_text.py`_
- **2026-06-29** [`98d0e702c3`](https://github.com/sgl-project/sglang/commit/98d0e702c3) [#29470](https://github.com/sgl-project/sglang/pull/29470)
  [GLM-5] Tune the threshold of router GEMM (#29470)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-06-29** [`d5133e925b`](https://github.com/sgl-project/sglang/commit/d5133e925b) [#29493](https://github.com/sgl-project/sglang/pull/29493)
  [NPU][Bugfix] Add scoring_func for mimo_v2 (#29493)
  _Files: `python/sglang/srt/models/mimo_v2.py`_

## ROCm / AMD  (10 commits)

- **2026-07-06** [`c9ceab34cf`](https://github.com/sgl-project/sglang/commit/c9ceab34cf) [#29394](https://github.com/sgl-project/sglang/pull/29394)
  [AMD] [Docker] Update MoRI to v1.2.1 (#29394)
  _Files: `docker/rocm.Dockerfile`_
- **2026-07-05** [`ce733f106b`](https://github.com/sgl-project/sglang/commit/ce733f106b) [#28787](https://github.com/sgl-project/sglang/pull/28787)
  [AMD] Fix RMSNorm batch-invariance on ROCm under deterministic inference (#28787)
  _Files: `python/sglang/srt/layers/layernorm.py`_
- **2026-07-03** [`0ab095eb3f`](https://github.com/sgl-project/sglang/commit/0ab095eb3f) [#29986](https://github.com/sgl-project/sglang/pull/29986)
  [AMD]: hot-patch transformers dynamic_module_utils symlink bug (#29986)
  _Files: `docker/rocm.Dockerfile`_
- **2026-07-03** [`67697fb891`](https://github.com/sgl-project/sglang/commit/67697fb891) [#30014](https://github.com/sgl-project/sglang/pull/30014)
  [AMD] Temporarily disabled: every-6-hours rocm 7.2 test (#30014)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`_
- **2026-07-01** [`308d89e042`](https://github.com/sgl-project/sglang/commit/308d89e042) [#29409](https://github.com/sgl-project/sglang/pull/29409)
  [AMD] Split qwen3.5 triton DCP test into its own nightly job (#29409)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/test_qwen3p5_triton_dcp.py`_
- **2026-06-30** [`bb98629157`](https://github.com/sgl-project/sglang/commit/bb98629157) [#28471](https://github.com/sgl-project/sglang/pull/28471)
  docs(cookbook): add AMD MI300X/MI325X/MI355X support for GLM-5.2 (#28471)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs_new/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-06-30** [`c70cc96905`](https://github.com/sgl-project/sglang/commit/c70cc96905) [#29768](https://github.com/sgl-project/sglang/pull/29768)
  [AMD] Stop rocm720 pr auto-runs (#29768)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`_
- **2026-06-30** [`f2756f53f3`](https://github.com/sgl-project/sglang/commit/f2756f53f3) [#29765](https://github.com/sgl-project/sglang/pull/29765)
  [AMD] Update AMD local registry address (#29765)
  _Files: `.github/workflows/release-docker-amd-miles-rocm700-nightly.yml`, `.github/workflows/release-docker-amd-miles-rocm720-nightly.yml`, `.github/workflows/release-docker-amd-nightly.yml`, `.github/workflows/release-docker-amd-rocm720-nightly.yml` _+2 more__
- **2026-06-30** [`7da4e30d9b`](https://github.com/sgl-project/sglang/commit/7da4e30d9b) [#29671](https://github.com/sgl-project/sglang/pull/29671)
  [AMD] Register fused_metadata_copy JIT kernel test for AMD nightly CI (#29671)
  _Files: `test/registered/jit/test_fused_metadata_copy.py`_
- **2026-06-29** [`5169df70f6`](https://github.com/sgl-project/sglang/commit/5169df70f6) [#29661](https://github.com/sgl-project/sglang/pull/29661)
  [AMD] Sgl-data mount opt-in (#29661)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `scripts/ci/amd/amd_ci_start_container.sh`_

## Scheduler / Batching  (9 commits)

- **2026-07-05** [`48ba79c11e`](https://github.com/sgl-project/sglang/commit/48ba79c11e) [#30053](https://github.com/sgl-project/sglang/pull/30053)
  [BugFix] Release HiCache prefetch resources on disagg-prefill bootstrap-queue abort (#30053)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-07-04** [`63c4996fef`](https://github.com/sgl-project/sglang/commit/63c4996fef) [#29882](https://github.com/sgl-project/sglang/pull/29882)
  fix: populate batch req rids and per-request http_worker_ipc for mult… (#29882)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/tokenizer/test_multi_tokenizer.py`_
- **2026-07-02** [`ae1f0c6d07`](https://github.com/sgl-project/sglang/commit/ae1f0c6d07) [#29977](https://github.com/sgl-project/sglang/pull/29977)
  `session_id` dataclass field should not put in msgpack struct (#29977)
  _Files: `python/sglang/srt/managers/io_struct.py`_
- **2026-07-02** [`d15b79e96e`](https://github.com/sgl-project/sglang/commit/d15b79e96e) [#29354](https://github.com/sgl-project/sglang/pull/29354)
  [bug6] clear stale mamba cow source on rematch (#29354)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-07-02** [`e6f6a353bf`](https://github.com/sgl-project/sglang/commit/e6f6a353bf) [#29842](https://github.com/sgl-project/sglang/pull/29842)
  pad customized_info for mixed output batches (#29842)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `test/registered/unit/managers/test_output_streamer_customized_info.py`_
- **2026-07-01** [`3cdc2415b1`](https://github.com/sgl-project/sglang/commit/3cdc2415b1) [#29217](https://github.com/sgl-project/sglang/pull/29217)
  [MLX] Fix step-bounded profiling for bench tools on Apple Silicon (#29217)
  _Files: `python/sglang/benchmark/offline_throughput.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `test/registered/unit/hardware_backend/mlx/test_scheduler_mixin.py`_
- **2026-06-30** [`f920a37da4`](https://github.com/sgl-project/sglang/commit/f920a37da4) [#29642](https://github.com/sgl-project/sglang/pull/29642)
  [AMD] Copy decode result on forward_stream instead of copy_stream (#29642)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-06-29** [`91cf159696`](https://github.com/sgl-project/sglang/commit/91cf159696) [#29571](https://github.com/sgl-project/sglang/pull/29571)
  [PP] bugfix: include CP size in PP rank offset (#29571)
  _Files: `python/sglang/srt/managers/scheduler_components/request_receiver.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/registered/unit/managers/test_pp_cp_rank_offsets.py`_
- **2026-06-29** [`bb74ed4a8d`](https://github.com/sgl-project/sglang/commit/bb74ed4a8d) [#29549](https://github.com/sgl-project/sglang/pull/29549)
  Replace hasattr with isinstance in SHM feature helpers (#29549)
  _Files: `python/sglang/srt/managers/mm_utils.py`_

## Speculative Decoding  (8 commits)

- **2026-07-06** [`850719ebd9`](https://github.com/sgl-project/sglang/commit/850719ebd9) [#30048](https://github.com/sgl-project/sglang/pull/30048)
  [XPU] Unbreak stage-b: re-add --disable-decode-cuda-graph, quarantine EAGLE3 parity (#30048)
  _Files: `test/registered/spec/eagle/test_spec_eagle_parity.py`_
- **2026-07-02** [`17cce6a85f`](https://github.com/sgl-project/sglang/commit/17cce6a85f) [#29943](https://github.com/sgl-project/sglang/pull/29943)
  Fix shared logits buffer for reduced-vocab draft models (#29943)
  _Files: `python/sglang/srt/layers/logits_processor.py`_
- **2026-07-02** [`4fffc6448b`](https://github.com/sgl-project/sglang/commit/4fffc6448b) [#23180](https://github.com/sgl-project/sglang/pull/23180)
  Speculative decoding support on XPU (#23180)
  _Files: `python/sglang/srt/hardware_backend/xpu/xpu_cudagraph_backend.py`, `python/sglang/srt/model_executor/runner_backend/utils.py`, `python/sglang/srt/speculative/eagle_utils.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` _+5 more__
- **2026-07-01** [`a01afdd526`](https://github.com/sgl-project/sglang/commit/a01afdd526) [#29645](https://github.com/sgl-project/sglang/pull/29645)
  Support real draft tokens to simulated acceptance (#29645)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/speculative/eagle_utils.py`, `python/sglang/srt/speculative/spec_utils.py`_
- **2026-06-30** [`4b4b4af583`](https://github.com/sgl-project/sglang/commit/4b4b4af583) [#29622](https://github.com/sgl-project/sglang/pull/29622)
  Budget EAGLE/STANDALONE draft KV pool in SWA pool configurators (#29622)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`_
- **2026-06-29** [`45314a9fcb`](https://github.com/sgl-project/sglang/commit/45314a9fcb) [#29654](https://github.com/sgl-project/sglang/pull/29654)
  [spec] Fix index_share_for_mtp_iteration being a no-op in EAGLE MTP draft (#29654)
  _Files: `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-06-29** [`5556631789`](https://github.com/sgl-project/sglang/commit/5556631789) [#23838](https://github.com/sgl-project/sglang/pull/23838)
  [Speculative Decoding] Validate vocabulary compatibility in STANDALONE mode (#23838)
  _Files: `python/sglang/srt/speculative/standalone_worker_v2.py`_
- **2026-06-29** [`f480c5f1f9`](https://github.com/sgl-project/sglang/commit/f480c5f1f9) [#29616](https://github.com/sgl-project/sglang/pull/29616)
  [Spec] Frozen-KV MTP: delay target KV binding to pool init + reset stale draft out_cache_loc (#29616)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/frozen_kv_mtp_worker_v2.py`_

## CI / Build  (7 commits)

- **2026-07-06** [`cc7d7ba3dd`](https://github.com/sgl-project/sglang/commit/cc7d7ba3dd) [#30100](https://github.com/sgl-project/sglang/pull/30100)
  [Intel XPU] Bump nightly per-file timeout to 120m and extend XPU CI monitor (#30100)
  _Files: `.github/workflows/nightly-test-intel.yml`, `.github/workflows/xpu-ci-job-monitor.yml`, `scripts/ci/xpu/xpu_ci_start_container.sh`_
- **2026-07-03** [`7820dc60a7`](https://github.com/sgl-project/sglang/commit/7820dc60a7) [#29908](https://github.com/sgl-project/sglang/pull/29908)
  [Apple Silicon] Add labeler config (#29908)
  _Files: `.github/labeler.yml`, `.github/workflows/pr-test-mlx.yml`_
- **2026-07-03** [`860244d4b4`](https://github.com/sgl-project/sglang/commit/860244d4b4) [#29447](https://github.com/sgl-project/sglang/pull/29447)
  [CI] Add per-stage NVIDIA model inventory tool (#29447)
  _Files: `.github/workflows/ci-model-inventory.yml`, `scripts/ci/list_stage_models.py`, `scripts/ci/stage_models_overrides.json`, `scripts/ci/test_list_stage_models.py`_
- **2026-07-03** [`75cdaf432a`](https://github.com/sgl-project/sglang/commit/75cdaf432a) [#29807](https://github.com/sgl-project/sglang/pull/29807)
  Add XPU CI job monitor workflow (#29807)
  _Files: `.github/workflows/xpu-ci-job-monitor.yml`, `scripts/ci/utils/xpu_job_monitor.py`_
- **2026-07-02** [`4605d4d94b`](https://github.com/sgl-project/sglang/commit/4605d4d94b) [#29691](https://github.com/sgl-project/sglang/pull/29691)
  [Apple Silicon] [CI] Add model-free unit-test workflow on macos-26 (#29691)
  _Files: `.github/workflows/pr-test-mlx.yml`_
- **2026-07-01** [`a0d9791810`](https://github.com/sgl-project/sglang/commit/a0d9791810) [#29845](https://github.com/sgl-project/sglang/pull/29845)
  [CI] Fix fused EH norm CI registration (#29845)
  _Files: `test/registered/jit/benchmark/bench_fused_eh_norm.py`, `test/registered/jit/test_fused_eh_norm.py`_
- **2026-06-30** [`3e16be2122`](https://github.com/sgl-project/sglang/commit/3e16be2122) [#29066](https://github.com/sgl-project/sglang/pull/29066)
  [CI] Migrate JIT tests to runner config registration (#29066)

## Structured Output  (1 commits)

- **2026-07-04** [`854b46be99`](https://github.com/sgl-project/sglang/commit/854b46be99) [#29920](https://github.com/sgl-project/sglang/pull/29920)
  feat(parser): resolve special-token suffix at runtime for compatibility (#29920)
  _Files: `python/sglang/srt/constrained/base_grammar_backend.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py` _+6 more__

## LoRA  (1 commits)

- **2026-07-04** [`88db9e033a`](https://github.com/sgl-project/sglang/commit/88db9e033a) [#30101](https://github.com/sgl-project/sglang/pull/30101)
  Adjust KL_THRESHOLD for log probability calculations (#30101)
  _Files: `test/registered/lora/test_lora_qwen3_30b_a3b_instruct_2507_logprob_diff.py`_

## Serving / API  (1 commits)

- **2026-07-03** [`f011d8c2e5`](https://github.com/sgl-project/sglang/commit/f011d8c2e5) [#29703](https://github.com/sgl-project/sglang/pull/29703)
  [Anthropic] Fix missing cache_read_input_tokens in streaming responses (#29703)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_

---
_Generated 2026-07-06 12:11 UTC_