# sgl-project/sglang — Weekly Change Report
**Period:** 2026-07-06 → 2026-07-13  |  **Total commits:** 274

## ✨ New Features This Week

- **2026-07-13** [#27350](https://github.com/sgl-project/sglang/pull/27350) — Support Waterfill with MegaMoE backend (#27350)
- **2026-07-13** [#30889](https://github.com/sgl-project/sglang/pull/30889) — feat: enable piecewise prefill graph for Kimi K2.5/K2.7 (#30889)
- **2026-07-13** [#30898](https://github.com/sgl-project/sglang/pull/30898) — Enable breakable prefill CUDA graph for DP attention (#30898)
- **2026-07-12** [#30261](https://github.com/sgl-project/sglang/pull/30261) — [Spec] Add DSpark: confidence-scheduled speculative decoding (#30261)
- **2026-07-12** [#30944](https://github.com/sgl-project/sglang/pull/30944) — [Spec] Add kill-switch env for draft-extend CUDA graph capture (#30944)
- **2026-07-12** [#30871](https://github.com/sgl-project/sglang/pull/30871) — profile: add vlm prefill profiler ranges (#30871)
- **2026-07-12** [#30879](https://github.com/sgl-project/sglang/pull/30879) — bench: support random image resolutions (#30879)
- **2026-07-11** [#30853](https://github.com/sgl-project/sglang/pull/30853) — [Spec] Enable draft extend cuda graph for DeepSeek-V4 attention backend (#30853)
- **2026-07-11** [#30843](https://github.com/sgl-project/sglang/pull/30843) — [DOCS][NPU]update npu support features and models (#30843)
- **2026-07-11** [#30782](https://github.com/sgl-project/sglang/pull/30782) — Add diffusion BCG prompt conditioning guard (#30782)
- _…and 63 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-13** [`80965db8d3`](https://github.com/sgl-project/sglang/commit/80965db8d3) [#30942](https://github.com/sgl-project/sglang/pull/30942) — [AMD] Pin cmake==4.3.4 in ROCm Dockerfile to fix MoRI gtest_discover build break (#30942)
- **2026-07-12** [`6cc9352dfe`](https://github.com/sgl-project/sglang/commit/6cc9352dfe) [#30261](https://github.com/sgl-project/sglang/pull/30261) — [Spec] Add DSpark: confidence-scheduled speculative decoding (#30261)
- **2026-07-11** [`bbcfcaeefe`](https://github.com/sgl-project/sglang/commit/bbcfcaeefe) [#27546](https://github.com/sgl-project/sglang/pull/27546) — fix(pd): do not abort when req.disagg_prefill_dp_rank is used (#27546)
- **2026-07-10** [`789bc3995c`](https://github.com/sgl-project/sglang/commit/789bc3995c) [#30587](https://github.com/sgl-project/sglang/pull/30587) — [AMD-miles] Bump miles rocm700-mi35x base image and migrate nightly test onto it (#30587)
- **2026-07-10** [`4a8e1b07a2`](https://github.com/sgl-project/sglang/commit/4a8e1b07a2) [#30447](https://github.com/sgl-project/sglang/pull/30447) — [diffusion] refactor: reorganize runtime utility and server_args modules (#30447)
- **2026-07-09** [`8d0fd34150`](https://github.com/sgl-project/sglang/commit/8d0fd34150) [#29417](https://github.com/sgl-project/sglang/pull/29417) — [AMD] Enable unified-KV HiCache on DeepSeek-V4 (#29417)
- **2026-07-09** [`462b6171bd`](https://github.com/sgl-project/sglang/commit/462b6171bd) [#30339](https://github.com/sgl-project/sglang/pull/30339) — [AMD] Fix stale SWA ring buffer on radix prefix reuse for DeepSeek-V4 with unified_kv backend (#30339)
- **2026-07-09** [`26ba3458d3`](https://github.com/sgl-project/sglang/commit/26ba3458d3) [#28788](https://github.com/sgl-project/sglang/pull/28788) — [AMD] Fix int32 offset overflow in Triton decode-attention kernels (#28788)
- **2026-07-09** [`336b64ecce`](https://github.com/sgl-project/sglang/commit/336b64ecce) [#29479](https://github.com/sgl-project/sglang/pull/29479) — [AMD] fix dsv4 indexer dtype dispatch on gfx950 (#29479)
- **2026-07-09** [`bd7e54d737`](https://github.com/sgl-project/sglang/commit/bd7e54d737) [#30557](https://github.com/sgl-project/sglang/pull/30557) — [AMD] Fix AITER custom all-gather CUDA-graph capture crash under torch_memory_saver (#30557)
- **2026-07-09** [`d74619b373`](https://github.com/sgl-project/sglang/commit/d74619b373) [#28534](https://github.com/sgl-project/sglang/pull/28534) — [AMD] Enable JIT staged HiCache write-back and fix CPU-index crash (#28534)
- **2026-07-09** [`cf8f1df6e8`](https://github.com/sgl-project/sglang/commit/cf8f1df6e8) [#30307](https://github.com/sgl-project/sglang/pull/30307) — [AMD] add dedicated jit-kernel-benchmark-test-amd stage + register portable JIT benches (#30307)
- **2026-07-08** [`07ef650ef7`](https://github.com/sgl-project/sglang/commit/07ef650ef7) [#30265](https://github.com/sgl-project/sglang/pull/30265) — [AMD] Fix GLM-5.2 MTP Quark excludes (#30265)
- **2026-07-08** [`c55190a638`](https://github.com/sgl-project/sglang/commit/c55190a638) [#30446](https://github.com/sgl-project/sglang/pull/30446) — [AMD] Register 2 CPU-bound 1-GPU tests (phase_checker, scripted_runtime_core) for AMD PR CI (#30446)
- **2026-07-08** [`47a6dfd708`](https://github.com/sgl-project/sglang/commit/47a6dfd708) [#30212](https://github.com/sgl-project/sglang/pull/30212) — [AMD] Register 3 ROCm-portable JIT kernel tests for AMD CI (#30212)
- **2026-07-08** [`8d2b66fd90`](https://github.com/sgl-project/sglang/commit/8d2b66fd90) [#29275](https://github.com/sgl-project/sglang/pull/29275) — Fix gfx95 bpreshuffle FP8 activation scale layout (#29275)
- **2026-07-08** [`fc378f843e`](https://github.com/sgl-project/sglang/commit/fc378f843e) [#30534](https://github.com/sgl-project/sglang/pull/30534) — [AMD] Temporarily reduce AMD scheduled test frequency to save resource (#30534)
- **2026-07-08** [`96368a5f77`](https://github.com/sgl-project/sglang/commit/96368a5f77) [#28658](https://github.com/sgl-project/sglang/pull/28658) — [AMD] Fuse shared-expert sigmoid + bf16->fp32 cast into the MoE append kernel (3 kernels -> 1) (#28658)
- **2026-07-08** [`669b4bc72b`](https://github.com/sgl-project/sglang/commit/669b4bc72b) [#30496](https://github.com/sgl-project/sglang/pull/30496) — [AMD] Gate stage-c on stage-b-test-1-gpu-large-amd (#30496)
- **2026-07-08** [`7709a1f358`](https://github.com/sgl-project/sglang/commit/7709a1f358) [#30348](https://github.com/sgl-project/sglang/pull/30348) — [refactor] ctx.resources: named slots, stream leases, and workspace buffer leases (#30348)
- **2026-07-08** [`b7cca0bf8f`](https://github.com/sgl-project/sglang/commit/b7cca0bf8f) [#30347](https://github.com/sgl-project/sglang/pull/30347) — [refactor] Collect MoE and DP-attention runtime state into typed flag groups (#30347)
- **2026-07-08** [`be32c57598`](https://github.com/sgl-project/sglang/commit/be32c57598) [#30346](https://github.com/sgl-project/sglang/pull/30346) — [refactor] Read resolved config from server_args fields; retire the flags mirror tier (#30346)
- **2026-07-08** [`9bf122a455`](https://github.com/sgl-project/sglang/commit/9bf122a455) [#30386](https://github.com/sgl-project/sglang/pull/30386) — [AMD] Run MI355X disaggregation Nightly Test with runtime checkout code mechanism (#30386)
- **2026-07-07** [`b363249423`](https://github.com/sgl-project/sglang/commit/b363249423) [#30309](https://github.com/sgl-project/sglang/pull/30309) — [AMD] ci: run multimodal_gen unit suite on AMD (#30309)
- **2026-07-07** [`60f502a4fd`](https://github.com/sgl-project/sglang/commit/60f502a4fd) [#30207](https://github.com/sgl-project/sglang/pull/30207) — [AMD] Register 2 hardware-agnostic 1-GPU PR tests for AMD CI (#30207)
- **2026-07-07** [`090efa27a2`](https://github.com/sgl-project/sglang/commit/090efa27a2) [#30290](https://github.com/sgl-project/sglang/pull/30290) — [AMD] Register 5 CI-verified 1-GPU kernel/attention unit tests for AMD PR CI (#30290)
- **2026-07-07** [`40a68521c9`](https://github.com/sgl-project/sglang/commit/40a68521c9) [#30374](https://github.com/sgl-project/sglang/pull/30374) — [AMD] Fix DeepSeekV4 server cutlass error (#30374)
- **2026-07-07** [`9ddea8d9ef`](https://github.com/sgl-project/sglang/commit/9ddea8d9ef) [#30302](https://github.com/sgl-project/sglang/pull/30302) — [AMD] [MORI-EP] Skip LocalExpertCount kernel in decode graph when not recording (#30302)
- **2026-07-07** [`dabd4cfcfd`](https://github.com/sgl-project/sglang/commit/dabd4cfcfd) [#30313](https://github.com/sgl-project/sglang/pull/30313) — [AMD] Cap DSV4 Flash max_total_num_tokens (#30313)
- **2026-07-07** [`9a6f8e5992`](https://github.com/sgl-project/sglang/commit/9a6f8e5992) [#30333](https://github.com/sgl-project/sglang/pull/30333) — [AMD] Fix DeepSeek V4 MTP accuracy issue (#30333)
- **2026-07-06** [`52c6e27e7e`](https://github.com/sgl-project/sglang/commit/52c6e27e7e) [#29673](https://github.com/sgl-project/sglang/pull/29673) — [AMD][diffusion] fix: disable layernorm torch.compile decorator in eager mode on ROCm to avoid memory-access fault (#29673)
- **2026-07-06** [`80decc78ec`](https://github.com/sgl-project/sglang/commit/80decc78ec) [#30237](https://github.com/sgl-project/sglang/pull/30237) — [AMD][DeepSeek V4] Set SGLANG_OPT_FLASHMLA_SPARSE_PREFILL to false on hip code path (#30237)
- **2026-07-06** [`81735ecf80`](https://github.com/sgl-project/sglang/commit/81735ecf80) [#29362](https://github.com/sgl-project/sglang/pull/29362) — [AMD ]Feat/dsv4 ep tbo prefill (#29362)
- **2026-07-06** [`c9ceab34cf`](https://github.com/sgl-project/sglang/commit/c9ceab34cf) [#29394](https://github.com/sgl-project/sglang/pull/29394) — [AMD] [Docker] Update MoRI to v1.2.1 (#29394)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-07-13 |
| [#30854](https://github.com/sgl-project/sglang/issues/30854) | [Bug] GLM-5.2 MTP + PD disaggregation decode crashes at dsa_seed_topk  | — | 2026-07-13 |
| [#31015](https://github.com/sgl-project/sglang/issues/31015) | [Feature] [Roadmap] Support Hygon HCU GPUs | — | 2026-07-13 |
| [#31010](https://github.com/sgl-project/sglang/issues/31010) | [Playground] Verified cell: mi355x / pro / fp4 / high-throughput / sin | — | 2026-07-13 |
| [#31007](https://github.com/sgl-project/sglang/issues/31007) | DeepSeek-V4 FP4: MI355X uses 50% more weight memory per GPU than B200  | — | 2026-07-13 |
| [#30734](https://github.com/sgl-project/sglang/issues/30734) | [Roadmap] GLM-5.2 + AMD/ROCm DSpark support | — | 2026-07-13 |
| [#30145](https://github.com/sgl-project/sglang/issues/30145) | [Feature] Unified Radix Cache Split: TreeCore | — | 2026-07-13 |
| [#30321](https://github.com/sgl-project/sglang/issues/30321) | [Bug] GLM-5.2 with MTP+Hicache+Mooncake occasionally produces garbled  | — | 2026-07-13 |
| [#30919](https://github.com/sgl-project/sglang/issues/30919) | [Bug] cu13 nightly image (>=20260711): flashinfer 0.6.14 dropped cuda- | — | 2026-07-13 |
| [#30931](https://github.com/sgl-project/sglang/issues/30931) | [Build] Build without CUDA | — | 2026-07-12 |
| [#30928](https://github.com/sgl-project/sglang/issues/30928) | [RFC] Position-Independent KV Cache Reuse for Agentic/RAG Workloads | — | 2026-07-12 |
| [#29630](https://github.com/sgl-project/sglang/issues/29630) | [RFC] Introduce a unified sglang.kernels namespace for kernel organiza | RFC, jit-kernel, kernel | 2026-07-10 |
| [#30781](https://github.com/sgl-project/sglang/issues/30781) | [Bug] sgl-model-gateway router rejects /v1/responses requests with too | — | 2026-07-10 |
| [#27574](https://github.com/sgl-project/sglang/issues/27574) | [Agentic Inference] Programmatic KV Cache for Agentic Workloads | high priority | 2026-07-10 |
| [#30760](https://github.com/sgl-project/sglang/issues/30760) | [Bug] HiCache prefetch all_reduce deadlock with TP=4, no PP — mismatch | — | 2026-07-10 |
| [#30696](https://github.com/sgl-project/sglang/issues/30696) | [RFC] RuntimeContext as the configuration API | — | 2026-07-09 |
| [#30664](https://github.com/sgl-project/sglang/issues/30664) | [Bug] Module Import Failure on Non-NVIDIA Hardware | — | 2026-07-09 |
| [#26399](https://github.com/sgl-project/sglang/issues/26399) | [Bug] GLM-5.1 TP8 EAGLE verify hangs when KV pool is near-full, watchd | — | 2026-07-09 |
| [#24488](https://github.com/sgl-project/sglang/issues/24488) | [Help] [Performance] PD disaggregation on H200 shows no throughput gai | — | 2026-07-09 |
| [#30599](https://github.com/sgl-project/sglang/issues/30599) | [Feature][AMD] Officially support consumer Radeon RDNA3/RDNA4 (gfx1100 | — | 2026-07-09 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 62 |
| MoE / Expert Parallel | 33 |
| Multimodal | 28 |
| Prefill / Decode Disaggregation | 26 |
| Other | 21 |
| KV Cache / Memory | 19 |
| Docs / Examples | 18 |
| Triton / Kernels | 16 |
| Quantization | 11 |
| Scheduler / Batching | 11 |
| Tensor / Data Parallel | 9 |
| ROCm / AMD | 6 |
| Speculative Decoding | 4 |
| CI / Build | 4 |
| Serving / API | 3 |
| Models | 2 |
| LoRA | 1 |

## Attention / FlashInfer  (62 commits)

- **2026-07-13** [`2225817424`](https://github.com/sgl-project/sglang/commit/2225817424) [#30767](https://github.com/sgl-project/sglang/pull/30767)
  [NPU] [DOC] Optimize and fix docs issues on Ascend NPU (#30767)
  _Files: `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_faq.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_glm5.2_examples.mdx` _+32 more__
- **2026-07-13** [`82e7cdcff9`](https://github.com/sgl-project/sglang/commit/82e7cdcff9) [#30973](https://github.com/sgl-project/sglang/pull/30973)
  [Misc] Remove a few dead code paths in DSA (#30973)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py`, `python/sglang/srt/layers/attention/dsa_backend.py`_
- **2026-07-13** [`4cec9ef9d7`](https://github.com/sgl-project/sglang/commit/4cec9ef9d7) [#30846](https://github.com/sgl-project/sglang/pull/30846)
  [Fix] Forward on_after_cuda_graph_warmup through HybridLinearAttnBackend (#30846)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`_
- **2026-07-13** [`b94ac87e0c`](https://github.com/sgl-project/sglang/commit/b94ac87e0c) [#30898](https://github.com/sgl-project/sglang/pull/30898)
  Enable breakable prefill CUDA graph for DP attention (#30898)
  _Files: `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+5 more__
- **2026-07-12** [`7a82178277`](https://github.com/sgl-project/sglang/commit/7a82178277) [#30945](https://github.com/sgl-project/sglang/pull/30945)
  [Fix] Disable FlashInfer allreduce fusion in Nemotron-3-Nano lm-eval test (#30945)
  _Files: `test/registered/models_e2e/test_nvidia_nemotron_3_nano.py`_
- **2026-07-12** [`5ba3c5147e`](https://github.com/sgl-project/sglang/commit/5ba3c5147e) [#30944](https://github.com/sgl-project/sglang/pull/30944)
  [Spec] Add kill-switch env for draft-extend CUDA graph capture (#30944)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`, `test/registered/cp/test_deepseek_v4_flash_fp4_b200_cp.py`_
- **2026-07-12** [`96a04cb13f`](https://github.com/sgl-project/sglang/commit/96a04cb13f) [#30873](https://github.com/sgl-project/sglang/pull/30873)
  Fix DeepEP CI test registration (#30873)
  _Files: `.github/workflows/pr-test-extra.yml`, `test/registered/cp/test_gqa_prefill_cp.py`, `test/registered/rl/test_return_routed_experts.py`, `test/run_suite.py`_
- **2026-07-12** [`bce3fc987d`](https://github.com/sgl-project/sglang/commit/bce3fc987d) [#30878](https://github.com/sgl-project/sglang/pull/30878)
  perf: reuse MoonViT FA3 max-seqlen metadata (#30878)
  _Files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/models/kimi_k25.py`, `test/registered/unit/layers/attention/test_vision_max_seqlen.py`_
- **2026-07-12** [`592c04381d`](https://github.com/sgl-project/sglang/commit/592c04381d) [#29939](https://github.com/sgl-project/sglang/pull/29939)
  Update test repository case scripts to the main community (#29939)
  _Files: `test/registered/ascend/accuracy/deepseek_v3_2/test_npu_deepseek_v3_2_8p_aime25.py`, `test/registered/ascend/accuracy/glm4_6v_flash/test_npu_glm4_6v_flash_1p_mmmu.py`, `test/registered/ascend/accuracy/qwen3_vl_30b_a3b_thinking/test_npu_qwen3_vl_30b_a3b_thinking_1p_mmmu.py`, `test/registered/ascend/accuracy/qwen3_vl_8b_thinking/test_npu_qwen3_vl_8b_thinking_1p_mmmu.py` _+18 more__
- **2026-07-11** [`4884f6fbee`](https://github.com/sgl-project/sglang/commit/4884f6fbee) [#30896](https://github.com/sgl-project/sglang/pull/30896)
  [Fix] Unify ForwardBatch extend lens cpu fields to their declared list type (#30896)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/manual/attention/test_flashattn_backend.py` _+2 more__
- **2026-07-11** [`d8ef76682e`](https://github.com/sgl-project/sglang/commit/d8ef76682e) [#30857](https://github.com/sgl-project/sglang/pull/30857)
  [Spec] Extract shared draft worker construction and generalize draft sampler capture (#30857)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/models/deepseek_v4.py` _+4 more__
- **2026-07-11** [`7bac9c8cdb`](https://github.com/sgl-project/sglang/commit/7bac9c8cdb) [#30853](https://github.com/sgl-project/sglang/pull/30853)
  [Spec] Enable draft extend cuda graph for DeepSeek-V4 attention backend (#30853)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-07-11** [`07165d5daa`](https://github.com/sgl-project/sglang/commit/07165d5daa) [#30478](https://github.com/sgl-project/sglang/pull/30478)
  Add DCP to runtime parallel context (#30478)
  _Files: `python/sglang/kernels/ops/kvcache/mla_buffer.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py` _+12 more__
- **2026-07-10** [`649ce5dd3d`](https://github.com/sgl-project/sglang/commit/649ce5dd3d) [#30633](https://github.com/sgl-project/sglang/pull/30633)
  model: support Pi0.5 (#30633)
  _Files: `docs_new/cookbook/intro.mdx`, `docs_new/cookbook/vla/OpenPI/Pi0.5.mdx`, `docs_new/cookbook/vla/intro.mdx`, `docs_new/docs.json` _+57 more__
- **2026-07-10** [`7b99900980`](https://github.com/sgl-project/sglang/commit/7b99900980) [#30790](https://github.com/sgl-project/sglang/pull/30790)
  Fix hybrid attention graph hook test fixture (#30790)
  _Files: `test/registered/attention/test_trtllm_mha_graph_metadata.py`_
- **2026-07-10** [`ecb7fb3989`](https://github.com/sgl-project/sglang/commit/ecb7fb3989) [#30627](https://github.com/sgl-project/sglang/pull/30627)
  Fix CuTe DSL DSA paged MQA export (#30627)
  _Files: `python/sglang/jit_kernel/dsa/__init__.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-07-10** [`fef5eda4fb`](https://github.com/sgl-project/sglang/commit/fef5eda4fb) [#30711](https://github.com/sgl-project/sglang/pull/30711)
  [Refactor] Split DeepSeek-V4 MQALayer into a reusable attention base (#30711)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-07-10** [`7966f6be86`](https://github.com/sgl-project/sglang/commit/7966f6be86) [#30454](https://github.com/sgl-project/sglang/pull/30454)
  [NPU] fix npu import cutlass error (#30454)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-07-10** [`dda61b476e`](https://github.com/sgl-project/sglang/commit/dda61b476e) [#30708](https://github.com/sgl-project/sglang/pull/30708)
  [style] Extract init-static values in forward path (#30708)
  _Files: `python/sglang/srt/layers/attention/hybrid_attn_backend.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/model_executor/forward_batch_info.py` _+4 more__
- **2026-07-10** [`5ce5e1ee3e`](https://github.com/sgl-project/sglang/commit/5ce5e1ee3e) [#30716](https://github.com/sgl-project/sglang/pull/30716)
  [Diffusion] Revert CPU AMX optimizations (#30716)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/amx_attn.py`, `python/sglang/multimodal_gen/runtime/layers/linear.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py` _+8 more__
- **2026-07-10** [`295f85df08`](https://github.com/sgl-project/sglang/commit/295f85df08) [#30680](https://github.com/sgl-project/sglang/pull/30680)
  Fix DFlash mamba verify init ordering (#30680)
  _Files: `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-07-09** [`504570f425`](https://github.com/sgl-project/sglang/commit/504570f425) [#30695](https://github.com/sgl-project/sglang/pull/30695)
  [Refactor] Make DeepSeek-V4 attention backend tolerate an absent CPU seq_lens mirror (#30695)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-07-09** [`c53559ba10`](https://github.com/sgl-project/sglang/commit/c53559ba10) [#30690](https://github.com/sgl-project/sglang/pull/30690)
  [misc] Remove unit test cases that fail the admission criteria (#30690)
  _Files: `.codespellrc`, `python/sglang/srt/parser/conversation.py`, `test/registered/unit/entrypoints/anthropic/test_serving.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py` _+16 more__
- **2026-07-09** [`26ba3458d3`](https://github.com/sgl-project/sglang/commit/26ba3458d3) [#28788](https://github.com/sgl-project/sglang/pull/28788)
  [AMD] Fix int32 offset overflow in Triton decode-attention kernels (#28788)
  _Files: `python/sglang/srt/layers/attention/triton_ops/decode_attention.py`, `test/registered/attention/test_triton_attention_kernels.py`_
- **2026-07-09** [`2e4d6368c3`](https://github.com/sgl-project/sglang/commit/2e4d6368c3) [#29734](https://github.com/sgl-project/sglang/pull/29734)
  [GDN] Auto-select FlashInfer GDN prefill on validated SM100 configs (#29734)
  _Files: `docs_new/docs/advanced_features/attention_backend.mdx`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py` _+2 more__
- **2026-07-09** [`336b64ecce`](https://github.com/sgl-project/sglang/commit/336b64ecce) [#29479](https://github.com/sgl-project/sglang/pull/29479)
  [AMD] fix dsv4 indexer dtype dispatch on gfx950 (#29479)
  _Files: `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/dsv4/unified_kv_kernels/paged_decode.py`_
- **2026-07-09** [`06eb1b1838`](https://github.com/sgl-project/sglang/commit/06eb1b1838) [#30491](https://github.com/sgl-project/sglang/pull/30491)
  [refactor] Split the DP gathered-buffer state between flags.dp and ctx.forward (#30491)
  _Files: `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_nextn.py`, `python/sglang/srt/runtime_context.py` _+1 more__
- **2026-07-09** [`d74619b373`](https://github.com/sgl-project/sglang/commit/d74619b373) [#28534](https://github.com/sgl-project/sglang/pull/28534)
  [AMD] Enable JIT staged HiCache write-back and fix CPU-index crash (#28534)
  _Files: `python/sglang/jit_kernel/csrc/kvcacheio/hicache.cuh`, `python/sglang/jit_kernel/csrc/kvcacheio/staged_write_back.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`, `python/sglang/srt/managers/cache_controller.py` _+3 more__
- **2026-07-09** [`0562ccb1a8`](https://github.com/sgl-project/sglang/commit/0562ccb1a8) [#30586](https://github.com/sgl-project/sglang/pull/30586)
  Move breakable CUDA graph back into model_executor/runner_backend_utils (#30586)
  _Files: `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/replay_token.py`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/runner.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/srt/breakable_cuda_graph/__init__.py` _+7 more__
- **2026-07-09** [`3b43df5b6d`](https://github.com/sgl-project/sglang/commit/3b43df5b6d) [#27862](https://github.com/sgl-project/sglang/pull/27862)
  Support speculative decoding on CPU (#27862)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+32 more__
- **2026-07-09** [`177c048c68`](https://github.com/sgl-project/sglang/commit/177c048c68) [#28527](https://github.com/sgl-project/sglang/pull/28527)
  [Diffusion][CPU] Adding AMX optimizations for CPU platform (#28527)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/amx_attn.py`, `python/sglang/multimodal_gen/runtime/layers/linear.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py` _+8 more__
- **2026-07-09** [`cf8f1df6e8`](https://github.com/sgl-project/sglang/commit/cf8f1df6e8) [#30307](https://github.com/sgl-project/sglang/pull/30307)
  [AMD] add dedicated jit-kernel-benchmark-test-amd stage + register portable JIT benches (#30307)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/jit/benchmark/bench_activation.py`, `test/registered/jit/benchmark/bench_add_constant.py` _+15 more__
- **2026-07-08** [`cc13e2eae7`](https://github.com/sgl-project/sglang/commit/cc13e2eae7) [#30563](https://github.com/sgl-project/sglang/pull/30563)
  [CI] Move piecewise CUDA graph (pcg) tests to nightly (#30563)
  _Files: `test/registered/cuda_graph/piecewise/test_pcg_glm52_fp4.py`, `test/registered/cuda_graph/piecewise/test_pcg_glm52_fp8_tp8.py`, `test/registered/cuda_graph/piecewise/test_pcg_with_speculative_decoding.py`, `test/registered/cuda_graph/piecewise/test_pcg_with_speculative_decoding_dflash.py` _+3 more__
- **2026-07-08** [`8d2b66fd90`](https://github.com/sgl-project/sglang/commit/8d2b66fd90) [#29275](https://github.com/sgl-project/sglang/pull/29275)
  Fix gfx95 bpreshuffle FP8 activation scale layout (#29275)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` _+2 more__
- **2026-07-08** [`33c3dfd7e0`](https://github.com/sgl-project/sglang/commit/33c3dfd7e0) [#27436](https://github.com/sgl-project/sglang/pull/27436)
  [diffusion] Enable breakable CUDA graph (BCG) for diffusion DiTs (#27436)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/glm_image.py`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/__init__.py`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/model_padders/__init__.py`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/model_padders/ideogram.py` _+27 more__
- **2026-07-08** [`c7ca332fb0`](https://github.com/sgl-project/sglang/commit/c7ca332fb0) [#30255](https://github.com/sgl-project/sglang/pull/30255)
  Fix DSV4 prefill large Triton recompilation idle across context lengths (#30255)
  _Files: `python/sglang/srt/layers/attention/dsv4/metadata_kernel.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`_
- **2026-07-08** [`fa278a762c`](https://github.com/sgl-project/sglang/commit/fa278a762c) [#30439](https://github.com/sgl-project/sglang/pull/30439)
  Fix FA3 prefill CP NaNs (#30439)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-07-08** [`7bc343470f`](https://github.com/sgl-project/sglang/commit/7bc343470f) [#29218](https://github.com/sgl-project/sglang/pull/29218)
  [Spec] DFlash: support pure-MLA targets with an fp8 KV cache (Kimi-K2.x-NVFP4) (#29218)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `test/registered/quant/test_kimi_k26_nvfp4_dflash.py`_
- **2026-07-08** [`68901ba387`](https://github.com/sgl-project/sglang/commit/68901ba387) [#29777](https://github.com/sgl-project/sglang/pull/29777)
  [diffusion] Support SP for Krea-2 (#29777)
  _Files: `docs_new/cookbook/diffusion/Krea/Krea-2.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/krea2.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/krea2.py` _+1 more__
- **2026-07-08** [`fa185ed84d`](https://github.com/sgl-project/sglang/commit/fa185ed84d) [#29742](https://github.com/sgl-project/sglang/pull/29742)
  [diffusion] fix: fix z-Image accuracy (#29742)
  _Files: `python/sglang/jit_kernel/diffusion/triton/zimage_native_norm.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/zimage.py`, `python/sglang/multimodal_gen/runtime/layers/attention/__init__.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py` _+7 more__
- **2026-07-07** [`48ad6a83cf`](https://github.com/sgl-project/sglang/commit/48ad6a83cf) [#30140](https://github.com/sgl-project/sglang/pull/30140)
  [DeepSeek-V4] Enable non-paged indexer by default for large prefill chunks (#30140)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `test/registered/unit/layers/test_dsv4_nonpaged_indexer.py`_
- **2026-07-07** [`090efa27a2`](https://github.com/sgl-project/sglang/commit/090efa27a2) [#30290](https://github.com/sgl-project/sglang/pull/30290)
  [AMD] Register 5 CI-verified 1-GPU kernel/attention unit tests for AMD PR CI (#30290)
  _Files: `test/registered/attention/test_gdn_noncontiguous_stride.py`, `test/registered/attention/test_kda_kernels.py`, `test/registered/attention/test_trtllm_mha_page_table.py`, `test/registered/kernels/test_dsa_metadata.py` _+1 more__
- **2026-07-07** [`40a68521c9`](https://github.com/sgl-project/sglang/commit/40a68521c9) [#30374](https://github.com/sgl-project/sglang/pull/30374)
  [AMD] Fix DeepSeekV4 server cutlass error (#30374)
  _Files: `python/sglang/jit_kernel/dsa/__init__.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-07-07** [`bbc537035a`](https://github.com/sgl-project/sglang/commit/bbc537035a) [#30378](https://github.com/sgl-project/sglang/pull/30378)
  [DSA] Re-enable fused top-k v2 for MTP: clamp padded-row seq_lens to >= 0 (#30378)
  _Files: `python/sglang/jit_kernel/dsv4/topk.py`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/attention/triton_ops/dsa_metadata.py` _+2 more__
- **2026-07-07** [`e339c83f82`](https://github.com/sgl-project/sglang/commit/e339c83f82) [#30275](https://github.com/sgl-project/sglang/pull/30275)
  [Model] Support LongCat 2.0 FP8 (#30275)
  _Files: `python/sglang/jit_kernel/csrc/ngram_embedding.cuh`, `python/sglang/jit_kernel/ngram_embedding.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/longcat_flash.py` _+19 more__
- **2026-07-07** [`f32b4ecd26`](https://github.com/sgl-project/sglang/commit/f32b4ecd26) [#29964](https://github.com/sgl-project/sglang/pull/29964)
  [Docs] Use trtllm_mha for Qwen3.6 B300 (#29964)
  _Files: `docs_new/src/snippets/autoregressive/qwen36-deployment.jsx`_
- **2026-07-07** [`dabd4cfcfd`](https://github.com/sgl-project/sglang/commit/dabd4cfcfd) [#30313](https://github.com/sgl-project/sglang/pull/30313)
  [AMD] Cap DSV4 Flash max_total_num_tokens (#30313)
  _Files: `scripts/ci/slurm/launch_mi355x.sh`, `scripts/ci/slurm/recipes/mi355x-fp4/dsv4flash/1k1k/1p1d-dp8ep8-mtp.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/dsv4flash/1k1k/1p1d-dp8ep8.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/dsv4flash/1k1k/1p1d-mtp.yaml` _+5 more__
- **2026-07-07** [`fefc1743a9`](https://github.com/sgl-project/sglang/commit/fefc1743a9) [#25220](https://github.com/sgl-project/sglang/pull/25220)
  Cute-DSL FP8 MQA logits  (#25220)
  _Files: `benchmark/kernels/deepseek/benchmark_cute_dsl_fp8_paged_mqa_logits.py`, `python/sglang/jit_kernel/cutedsl_fp8_paged_mqa_logits.py`, `python/sglang/jit_kernel/dsa/__init__.py`, `python/sglang/jit_kernel/dsa/cutedsl_paged_mqa_logits.py` _+8 more__
- **2026-07-07** [`9bd02dc5b9`](https://github.com/sgl-project/sglang/commit/9bd02dc5b9) [#29383](https://github.com/sgl-project/sglang/pull/29383)
  feat(sgl-kernel): add InfLLM v2 attention kernels (#29383)
  _Files: `.codespellrc`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/csrc/common_extension.cc`, `sgl-kernel/csrc/infllm_v2/flash_attn/flash_api.cpp` _+29 more__
- **2026-07-07** [`be70bfbdbb`](https://github.com/sgl-project/sglang/commit/be70bfbdbb) [#30274](https://github.com/sgl-project/sglang/pull/30274)
  [DSA] Fold page-table into fused top-k v2 (decode): drop page_size=1 expansion (#30274)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/attention/triton_ops/dsa_metadata.py`_
- **2026-07-07** [`16372b4c5f`](https://github.com/sgl-project/sglang/commit/16372b4c5f) [#29787](https://github.com/sgl-project/sglang/pull/29787)
  [Spec] Anchor GLM-5.2 MTP IndexShare topk on the draft-extend step (#29787)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_nextn.py` _+8 more__
- **2026-07-07** [`df06e03662`](https://github.com/sgl-project/sglang/commit/df06e03662) [#30097](https://github.com/sgl-project/sglang/pull/30097)
  [MLX] Size the attention KV pool at the compute dtype for quantized models (#30097)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_pool_dtype.py`_
- **2026-07-07** [`6279805962`](https://github.com/sgl-project/sglang/commit/6279805962) [#27867](https://github.com/sgl-project/sglang/pull/27867)
  [DSv4] Loading Time Weight Dequant (#27867)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/model_loader/loader.py` _+1 more__
- **2026-07-07** [`3cbb7568bd`](https://github.com/sgl-project/sglang/commit/3cbb7568bd) [#27988](https://github.com/sgl-project/sglang/pull/27988)
  [Experimental] Full Cuda Graph Support for Prefill (#27988)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/model_executor/cuda_graph_config.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+3 more__
- **2026-07-06** [`093256aa4b`](https://github.com/sgl-project/sglang/commit/093256aa4b) [#29368](https://github.com/sgl-project/sglang/pull/29368)
  [Mamba] Fix long-prefill accuracy drop in radix prefix-cache state restore (#29368)
  _Files: `python/sglang/srt/layers/attention/mamba/mamba2_metadata.py`_
- **2026-07-06** [`1579a82d17`](https://github.com/sgl-project/sglang/commit/1579a82d17) [#30125](https://github.com/sgl-project/sglang/pull/30125)
  [MLX] Fix FakeOverlapScheduler test stub broken by forward_ct accounting (#30125)
  _Files: `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`_
- **2026-07-06** [`8f40b5eb3f`](https://github.com/sgl-project/sglang/commit/8f40b5eb3f) [#29699](https://github.com/sgl-project/sglang/pull/29699)
  When attention TP for linear and full attention, use Flashinfer allreduce fusion (#29699)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/models/nemotron_h.py`_
- **2026-07-06** [`1b481deade`](https://github.com/sgl-project/sglang/commit/1b481deade) [#29403](https://github.com/sgl-project/sglang/pull/29403)
  feat: sync npu nightly test improvements from Ascend testcases (#29403)
  _Files: `.github/workflows/nightly-test-npu-e2e-single-node.yml`, `.github/workflows/nightly-test-npu.yml`, `.github/workflows/pr-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py` _+33 more__
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

## MoE / Expert Parallel  (33 commits)

- **2026-07-13** [`eb31b5310c`](https://github.com/sgl-project/sglang/commit/eb31b5310c) [#27350](https://github.com/sgl-project/sglang/pull/27350)
  Support Waterfill with MegaMoE backend (#27350)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`, `docs_new/docs/references/environment_variables.mdx` _+10 more__
- **2026-07-13** [`08d6d297e5`](https://github.com/sgl-project/sglang/commit/08d6d297e5) [#29909](https://github.com/sgl-project/sglang/pull/29909)
  [Bugfix][NPU] Fix Hunyuan3 model where MoE's routing_scaling_ratio is missing on NPU (#29909)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`_
- **2026-07-12** [`80856aba85`](https://github.com/sgl-project/sglang/commit/80856aba85) [#30828](https://github.com/sgl-project/sglang/pull/30828)
  Make the mxfp8 MoE runner backend list extensible (#30828)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/server_args.py`_
- **2026-07-12** [`a358abd651`](https://github.com/sgl-project/sglang/commit/a358abd651) [#30866](https://github.com/sgl-project/sglang/pull/30866)
  chore: update vlm moe config and tune scripts (#30866)
  _Files: `benchmark/kernels/flashinfer_allreduce_fusion/benchmark_fused_collective.py`, `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=128,N=768,device_name=NVIDIA_H200.json` _+5 more__
- **2026-07-11** [`348e6fd29b`](https://github.com/sgl-project/sglang/commit/348e6fd29b) [#30847](https://github.com/sgl-project/sglang/pull/30847)
  [Fix] Guard kernel OOB accesses and harden runtime edge cases (#30847)
  _Files: `python/sglang/benchmark/one_batch_server.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/kernels/ops/kvcache/trtllm_mha_page_table.py`, `python/sglang/srt/eplb/expert_location.py` _+4 more__
- **2026-07-11** [`a91c2e6596`](https://github.com/sgl-project/sglang/commit/a91c2e6596) [#30121](https://github.com/sgl-project/sglang/pull/30121)
  [Apple Silicon] [CI] Move the MLX lane to the check-changes + pr-gate composite (#30121)
  _Files: `.github/workflows/pr-test-mlx.yml`, `python/sglang/test/ci/ci_register.py`, `test/registered/mlx/models_e2e/test_qwen2_moe_mlx_correctness.py`, `test/registered/mlx/models_e2e/test_qwen3_moe_mlx_correctness.py` _+11 more__
- **2026-07-11** [`51c5ddbe65`](https://github.com/sgl-project/sglang/commit/51c5ddbe65) [#30829](https://github.com/sgl-project/sglang/pull/30829)
  [eplb] chunk expert-weight P2P on CUDA to prevent NCCL rebalance hang (#30829)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/eplb/expert_location_updater.py`_
- **2026-07-11** [`0663ebc783`](https://github.com/sgl-project/sglang/commit/0663ebc783) [#28715](https://github.com/sgl-project/sglang/pull/28715)
  [minimax-m3] Split 4/4: model + VL + glue + function-call + fp8 quant + generic infra (#28715)
  _Files: `python/sglang/jit_kernel/csrc/gemm/per_token_group_quant_8bit.cuh`, `python/sglang/jit_kernel/moe_fused_gate.py`, `python/sglang/jit_kernel/per_token_group_quant_8bit.py`, `python/sglang/srt/arg_groups/overrides.py` _+41 more__
- **2026-07-11** [`fc2ef35308`](https://github.com/sgl-project/sglang/commit/fc2ef35308) [#30802](https://github.com/sgl-project/sglang/pull/30802)
  [refactor] Move MLP collective flags onto ForwardFlags (#30802)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/linear.py` _+33 more__
- **2026-07-10** [`3dc93a12ca`](https://github.com/sgl-project/sglang/commit/3dc93a12ca) [#30646](https://github.com/sgl-project/sglang/pull/30646)
  Improve EPLB dispatch handling and diagnostics (#30646)
  _Files: `python/sglang/srt/eplb/eplb_manager.py`, `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/eplb/expert_location_dispatch.py` _+4 more__
- **2026-07-10** [`7045e0fdff`](https://github.com/sgl-project/sglang/commit/7045e0fdff) [#30754](https://github.com/sgl-project/sglang/pull/30754)
  Seed sgl-kernel topk sigmoid tests on all backends (#30754)
  _Files: `sgl-kernel/tests/test_moe_topk_sigmoid.py`_
- **2026-07-10** [`2c6cd1ef41`](https://github.com/sgl-project/sglang/commit/2c6cd1ef41) [#29910](https://github.com/sgl-project/sglang/pull/29910)
  [Dep] Upgrade flashinfer to 0.6.14 (#29910)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/utils/common.py` _+2 more__
- **2026-07-10** [`b2f9a95867`](https://github.com/sgl-project/sglang/commit/b2f9a95867) [#29030](https://github.com/sgl-project/sglang/pull/29030)
  [NPU] use standalone group for moe ep (#29030)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`_
- **2026-07-09** [`87992eeec4`](https://github.com/sgl-project/sglang/commit/87992eeec4) [#30460](https://github.com/sgl-project/sglang/pull/30460)
  [DeepSeek V2] Reorder dual-stream MoE to main-first to avoid CUDA graph stream explosion (#30460)
  _Files: `python/sglang/srt/model_executor/runner_utils/capture_mode.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/utils/common.py`_
- **2026-07-09** [`b717546fab`](https://github.com/sgl-project/sglang/commit/b717546fab) [#28982](https://github.com/sgl-project/sglang/pull/28982)
  fix(mtp): avoid mtp perf regression in deepseek when enable eplb (#28982)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-07-09** [`a9e804623e`](https://github.com/sgl-project/sglang/commit/a9e804623e) [#30641](https://github.com/sgl-project/sglang/pull/30641)
  Allow EPLB manual test to use FlashInfer A2A (#30641)
  _Files: `test/manual/ep/test_eplb.py`_
- **2026-07-09** [`fef2128e19`](https://github.com/sgl-project/sglang/commit/fef2128e19) [#30490](https://github.com/sgl-project/sglang/pull/30490)
  [refactor] Add the per-forward flags tier: ctx.forward (#30490)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py` _+3 more__
- **2026-07-09** [`0ffed946f2`](https://github.com/sgl-project/sglang/commit/0ffed946f2) [#29480](https://github.com/sgl-project/sglang/pull/29480)
  [NPU] Add extra topk_weights input in deepep ll dispatch (#29480)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`_
- **2026-07-08** [`07ef650ef7`](https://github.com/sgl-project/sglang/commit/07ef650ef7) [#30265](https://github.com/sgl-project/sglang/pull/30265)
  [AMD] Fix GLM-5.2 MTP Quark excludes (#30265)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/glm4_moe.py`_
- **2026-07-08** [`ca8f15cd70`](https://github.com/sgl-project/sglang/commit/ca8f15cd70) [#30242](https://github.com/sgl-project/sglang/pull/30242)
  Fix FlashInfer A2A IMA by DP-synchronizing the decode graph bucket (#30242) (#30450)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`, `python/sglang/srt/utils/common.py`, `test/registered/unit/test_legacy_global_ratchet.py`_
- **2026-07-08** [`04e4fadff3`](https://github.com/sgl-project/sglang/commit/04e4fadff3) [#30323](https://github.com/sgl-project/sglang/pull/30323)
  Use FP32 logits in MoEGate fallbacks (#30323)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-07-08** [`b8ca06fdad`](https://github.com/sgl-project/sglang/commit/b8ca06fdad) [#30387](https://github.com/sgl-project/sglang/pull/30387)
  Fix zero expert routed ids for MoE backends (#30387)
  _Files: `python/sglang/srt/layers/moe/ep_moe/kernels.py`, `test/registered/moe/test_zero_experts.py`_
- **2026-07-08** [`96368a5f77`](https://github.com/sgl-project/sglang/commit/96368a5f77) [#28658](https://github.com/sgl-project/sglang/pull/28658)
  [AMD] Fuse shared-expert sigmoid + bf16->fp32 cast into the MoE append kernel (3 kernels -> 1) (#28658)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_kernels.py`, `python/sglang/srt/models/qwen2_moe.py`_
- **2026-07-08** [`8a868f8c00`](https://github.com/sgl-project/sglang/commit/8a868f8c00) [#30443](https://github.com/sgl-project/sglang/pull/30443)
  [NVIDIA] Allow modelopt_mixed quantization with flashinfer_cutedsl MoE runner (#30443)
  _Files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/server_args.py`_
- **2026-07-08** [`7709a1f358`](https://github.com/sgl-project/sglang/commit/7709a1f358) [#30348](https://github.com/sgl-project/sglang/pull/30348)
  [refactor] ctx.resources: named slots, stream leases, and workspace buffer leases (#30348)
  _Files: `python/sglang/srt/compilation/backend.py`, `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/eplb/lplb_solver.py` _+41 more__
- **2026-07-08** [`b7cca0bf8f`](https://github.com/sgl-project/sglang/commit/b7cca0bf8f) [#30347](https://github.com/sgl-project/sglang/pull/30347)
  [refactor] Collect MoE and DP-attention runtime state into typed flag groups (#30347)
  _Files: `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/runtime_context.py`, `test/registered/ops/test_aiter_allreduce_fusion_amd.py` _+3 more__
- **2026-07-08** [`be32c57598`](https://github.com/sgl-project/sglang/commit/be32c57598) [#30346](https://github.com/sgl-project/sglang/pull/30346)
  [refactor] Read resolved config from server_args fields; retire the flags mirror tier (#30346)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/logits_processor.py` _+56 more__
- **2026-07-08** [`49109d4267`](https://github.com/sgl-project/sglang/commit/49109d4267) [#30426](https://github.com/sgl-project/sglang/pull/30426)
  [Tiny] Fix Import Error for Pure TP config with flashinfer_mxfp4 (#30426)
  _Files: `python/sglang/srt/layers/moe/moe_runner/runner.py`_
- **2026-07-07** [`60f502a4fd`](https://github.com/sgl-project/sglang/commit/60f502a4fd) [#30207](https://github.com/sgl-project/sglang/pull/30207)
  [AMD] Register 2 hardware-agnostic 1-GPU PR tests for AMD CI (#30207)
  _Files: `test/registered/lora/test_moe_lora_info.py`, `test/registered/unit/managers/test_customized_info_streaming.py`_
- **2026-07-07** [`9ddea8d9ef`](https://github.com/sgl-project/sglang/commit/9ddea8d9ef) [#30302](https://github.com/sgl-project/sglang/pull/30302)
  [AMD] [MORI-EP] Skip LocalExpertCount kernel in decode graph when not recording (#30302)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`_
- **2026-07-07** [`1da7d3a50b`](https://github.com/sgl-project/sglang/commit/1da7d3a50b) [#26771](https://github.com/sgl-project/sglang/pull/26771)
  [MoE] Retire the AOT moe_fused_gate / kimi_k2_moe_fused_gate gate kernels (#26771) (#29997)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/benchmark/bench_kimi_k2_moe_fused_gate.py`, `sgl-kernel/benchmark/bench_moe_fused_gate.py` _+15 more__
- **2026-07-07** [`4145e595cf`](https://github.com/sgl-project/sglang/commit/4145e595cf) [#29440](https://github.com/sgl-project/sglang/pull/29440)
  [MLX] Add correctness tests for qwen2_moe and qwen3_moe (#29440)
  _Files: `test/registered/mlx/models_e2e/test_qwen2_moe_mlx_correctness.py`, `test/registered/mlx/models_e2e/test_qwen3_moe_mlx_correctness.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_reference_correctness.py`_
- **2026-07-07** [`4b5c612257`](https://github.com/sgl-project/sglang/commit/4b5c612257) [#22660](https://github.com/sgl-project/sglang/pull/22660)
  Skip redundant moe_sum_reduce for single-expert routing on XPU (#22660)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `test/registered/moe/test_fused_moe.py`_

## Multimodal  (28 commits)

- **2026-07-13** [`7da30f4e55`](https://github.com/sgl-project/sglang/commit/7da30f4e55) [#30889](https://github.com/sgl-project/sglang/pull/30889)
  feat: enable piecewise prefill graph for Kimi K2.5/K2.7 (#30889)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/configs/test_multimodal_piecewise_cuda_graph.py`_
- **2026-07-12** [`f1c247edf9`](https://github.com/sgl-project/sglang/commit/f1c247edf9) [#30871](https://github.com/sgl-project/sglang/pull/30871)
  profile: add vlm prefill profiler ranges (#30871)
  _Files: `python/sglang/srt/managers/mm_utils.py`_
- **2026-07-12** [`af66370d81`](https://github.com/sgl-project/sglang/commit/af66370d81) [#30879](https://github.com/sgl-project/sglang/pull/30879)
  bench: support random image resolutions (#30879)
  _Files: `python/sglang/benchmark/datasets/image.py`, `python/sglang/benchmark/serving.py`, `test/registered/bench_fn/test_bench_serving_reasoning_stream.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`_
- **2026-07-11** [`65abb23842`](https://github.com/sgl-project/sglang/commit/65abb23842) [#30782](https://github.com/sgl-project/sglang/pull/30782)
  Add diffusion BCG prompt conditioning guard (#30782)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/single_test_file/test_diffusion_bcg_zimage_turbo.py`_
- **2026-07-11** [`e3ceccf781`](https://github.com/sgl-project/sglang/commit/e3ceccf781) [#27551](https://github.com/sgl-project/sglang/pull/27551)
  [dLLM] Make FDFO a framework capability for all dLLM algorithms (#27551)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`, `docs_new/docs/supported-models/diffusion_language_models.mdx`, `python/sglang/srt/dllm/algorithm/base.py`, `python/sglang/srt/dllm/algorithm/joint_threshold.py` _+10 more__
- **2026-07-10** [`7de33ce806`](https://github.com/sgl-project/sglang/commit/7de33ce806) [#26505](https://github.com/sgl-project/sglang/pull/26505)
  fix: fix mm processor double bos (#26505)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `test/registered/unit/managers/test_mm_process_config.py`_
- **2026-07-10** [`789bc3995c`](https://github.com/sgl-project/sglang/commit/789bc3995c) [#30587](https://github.com/sgl-project/sglang/pull/30587)
  [AMD-miles] Bump miles rocm700-mi35x base image and migrate nightly test onto it (#30587)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm700.yml`, `.github/workflows/release-docker-amd-miles-rocm700-nightly.yml`_
- **2026-07-10** [`559854fe6a`](https://github.com/sgl-project/sglang/commit/559854fe6a) [#30791](https://github.com/sgl-project/sglang/pull/30791)
  [diffusion] docs: sync cookbook and log hygiene (#30791)
  _Files: `docs_new/cookbook/diffusion/intro.mdx`, `docs_new/docs/sglang-diffusion/api/cli.mdx`, `docs_new/docs/sglang-diffusion/deployment_cookbook.mdx`, `python/sglang/multimodal_gen/README.md` _+1 more__
- **2026-07-10** [`e9493a015c`](https://github.com/sgl-project/sglang/commit/e9493a015c) [#30584](https://github.com/sgl-project/sglang/pull/30584)
  Fix diffusion BCG lifetime and add Z-Image-Turbo CI (#30584)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/pr-test-multimodal-gen.yml`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py` _+4 more__
- **2026-07-10** [`a38cfc6768`](https://github.com/sgl-project/sglang/commit/a38cfc6768) [#27576](https://github.com/sgl-project/sglang/pull/27576)
  [diffusion] doc: update cosmos3 cookbook (#27576)
  _Files: `docs_new/cookbook/diffusion/Cosmos/Cosmos3.mdx`_
- **2026-07-10** [`ccd2028def`](https://github.com/sgl-project/sglang/commit/ccd2028def) [#30709](https://github.com/sgl-project/sglang/pull/30709)
  [style] Extract init-static values in tokenizer + multimodal path (#30709)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py` _+1 more__
- **2026-07-09** [`7aab39a18b`](https://github.com/sgl-project/sglang/commit/7aab39a18b) [#25381](https://github.com/sgl-project/sglang/pull/25381)
  [Diffusion] SGLang backend for GLM Image AR. Step 1 - Separate server (#25381)
  _Files: `docs_new/docs/sglang-diffusion/api/cli.mdx`, `docs_new/docs/sglang-diffusion/models_with_ar.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/glm_image.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vl_encoder_loader.py` _+11 more__
- **2026-07-09** [`61602b95fb`](https://github.com/sgl-project/sglang/commit/61602b95fb) [#30602](https://github.com/sgl-project/sglang/pull/30602)
  [Fix] Prevent silent VLM server crash when /dev/shm is exhausted during multimodal feature transport (#30602)
  _Files: `python/sglang/srt/managers/mm_utils.py`_
- **2026-07-09** [`395a2201e4`](https://github.com/sgl-project/sglang/commit/395a2201e4) [#28926](https://github.com/sgl-project/sglang/pull/28926)
  [diffusion] rl: enable RL rollout path for LTX-2.3 post-training (#28926)
  _Files: `python/sglang/multimodal_gen/configs/sample/ltx_2.py`, `python/sglang/multimodal_gen/runtime/entrypoints/post_training/rollout_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/post_training/utils.py`, `python/sglang/multimodal_gen/runtime/pipelines/ltx_2_pipeline.py` _+2 more__
- **2026-07-08** [`3d96bb9721`](https://github.com/sgl-project/sglang/commit/3d96bb9721) [#30518](https://github.com/sgl-project/sglang/pull/30518)
  [diffusion] chore: rename lingbot world v2 (#30518)
  _Files: `docs_new/cookbook/diffusion/LingBot-World/LingBot-World-2.0.mdx`, `python/sglang/multimodal_gen/registry.py`_
- **2026-07-08** [`d4963f5c55`](https://github.com/sgl-project/sglang/commit/d4963f5c55) [#30006](https://github.com/sgl-project/sglang/pull/30006)
  Fix prefill CUDA graph disabled for deeply-nested multimodal models (#30006)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-07-08** [`db40fd83d2`](https://github.com/sgl-project/sglang/commit/db40fd83d2) [#30361](https://github.com/sgl-project/sglang/pull/30361)
  [diffusion] model: support LingBot-World 2.0 (#30361)
  _Files: `docs_new/cookbook/diffusion/LingBot-World/LingBot-World-2.0.mdx`, `docs_new/cookbook/diffusion/intro.mdx`, `docs_new/docs.json`, `python/sglang/multimodal_gen/configs/pipeline_configs/__init__.py` _+2 more__
- **2026-07-07** [`b363249423`](https://github.com/sgl-project/sglang/commit/b363249423) [#30309](https://github.com/sgl-project/sglang/pull/30309)
  [AMD] ci: run multimodal_gen unit suite on AMD (#30309)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `scripts/ci/utils/ci_coverage_report.py`_
- **2026-07-07** [`11cea29c90`](https://github.com/sgl-project/sglang/commit/11cea29c90) [#30150](https://github.com/sgl-project/sglang/pull/30150)
  [diffusion][cache-dit] add dual-transformer Cache-DiT adapter specs (#30150)
  _Files: `python/sglang/multimodal_gen/runtime/cache/cache_dit_integration.py`, `python/sglang/multimodal_gen/test/unit/test_cache_dit_integration.py`_
- **2026-07-07** [`267ff1b5f9`](https://github.com/sgl-project/sglang/commit/267ff1b5f9) [#30278](https://github.com/sgl-project/sglang/pull/30278)
  Fix LTX2 RoPE JIT kernel CI (#30278)
  _Files: `python/sglang/jit_kernel/csrc/diffusion/ltx2_qknorm_split_rope.cuh`, `test/registered/jit/diffusion/test_ltx2_qknorm_split_rope.py`_
- **2026-07-07** [`7047afafec`](https://github.com/sgl-project/sglang/commit/7047afafec) [#29989](https://github.com/sgl-project/sglang/pull/29989)
  [diffusion] fix: slice img_shapes per-sample in rollout response extractor (#29989)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/post_training/rollout_api.py`_
- **2026-07-07** [`6c1fb8a937`](https://github.com/sgl-project/sglang/commit/6c1fb8a937) [#30241](https://github.com/sgl-project/sglang/pull/30241)
  [diffusion] fix: fix ragged-caption dynamic-batching accuracy bug in ernie-Image (#30241)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/ernie_image.py`, `python/sglang/multimodal_gen/runtime/models/dits/ernie_image.py`, `python/sglang/multimodal_gen/test/unit/test_ernie_image_pipeline_config.py`_
- **2026-07-06** [`1c23954cb9`](https://github.com/sgl-project/sglang/commit/1c23954cb9) [#29331](https://github.com/sgl-project/sglang/pull/29331)
  [NPU] Add new diffusion tests  (#29331)
  _Files: `python/sglang/multimodal_gen/test/server/ascend/perf_baselines_npu.json`, `python/sglang/multimodal_gen/test/server/ascend/testcase_configs_npu.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/testcase_configs.py` _+1 more__
- **2026-07-06** [`ca73c77055`](https://github.com/sgl-project/sglang/commit/ca73c77055) [#29755](https://github.com/sgl-project/sglang/pull/29755)
  [Diffusion] cache cross-attn K/V across denoise steps for Helios (#29755)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/helios.py`_
- **2026-07-06** [`52c6e27e7e`](https://github.com/sgl-project/sglang/commit/52c6e27e7e) [#29673](https://github.com/sgl-project/sglang/pull/29673)
  [AMD][diffusion] fix: disable layernorm torch.compile decorator in eager mode on ROCm to avoid memory-access fault (#29673)
  _Files: `python/sglang/multimodal_gen/runtime/layers/layernorm.py`_
- **2026-07-06** [`5f98f62a8a`](https://github.com/sgl-project/sglang/commit/5f98f62a8a) [#30086](https://github.com/sgl-project/sglang/pull/30086)
  [diffusion] perf: tp-shard every text/image encoder across the full DiT replica (any parallelism) (#30086)
  _Files: `python/sglang/multimodal_gen/configs/models/encoders/base.py`, `python/sglang/multimodal_gen/configs/models/encoders/t5.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/image_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py` _+8 more__
- **2026-07-06** [`de00b838c4`](https://github.com/sgl-project/sglang/commit/de00b838c4) [#30148](https://github.com/sgl-project/sglang/pull/30148)
  [diffusion] fix: pass progressive params through image API (#30148)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`_
- **2026-07-06** [`9d00385b63`](https://github.com/sgl-project/sglang/commit/9d00385b63) [#30180](https://github.com/sgl-project/sglang/pull/30180)
  Cleanup: relocate temp_set_env and consolidate multi-device/CUDA helpers in common.py (#30180)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/utils/common.py` _+3 more__

## Prefill / Decode Disaggregation  (26 commits)

- **2026-07-13** [`9dd57ef8c4`](https://github.com/sgl-project/sglang/commit/9dd57ef8c4) [#30616](https://github.com/sgl-project/sglang/pull/30616)
  [mem_cache][7/N] refactor: move  MLATokenToKVPoolHost to pool_host.mla (#30616)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` _+9 more__
- **2026-07-12** [`c616d5a55e`](https://github.com/sgl-project/sglang/commit/c616d5a55e) [#30951](https://github.com/sgl-project/sglang/pull/30951)
  [PD] Improve optimistic prefill (#30951)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/observability/req_time_stats.py` _+2 more__
- **2026-07-12** [`6cc9352dfe`](https://github.com/sgl-project/sglang/commit/6cc9352dfe) [#30261](https://github.com/sgl-project/sglang/pull/30261)
  [Spec] Add DSpark: confidence-scheduled speculative decoding (#30261)
  _Files: `python/sglang/benchmark/dspark_sps_profiler.py`, `python/sglang/benchmark/dspark_sts_fit.py`, `python/sglang/benchmark/serving.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` _+80 more__
- **2026-07-11** [`bbcfcaeefe`](https://github.com/sgl-project/sglang/commit/bbcfcaeefe) [#27546](https://github.com/sgl-project/sglang/pull/27546)
  fix(pd): do not abort when req.disagg_prefill_dp_rank is used (#27546)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/fake/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+3 more__
- **2026-07-11** [`90688366d9`](https://github.com/sgl-project/sglang/commit/90688366d9) [#30737](https://github.com/sgl-project/sglang/pull/30737)
  test(disagg): set MC_GID_INDEX on RoCE hosts so mooncake KV transfer works (#30737)
  _Files: `python/sglang/test/server_fixtures/disaggregation_fixture.py`_
- **2026-07-10** [`4a8e1b07a2`](https://github.com/sgl-project/sglang/commit/4a8e1b07a2) [#30447](https://github.com/sgl-project/sglang/pull/30447)
  [diffusion] refactor: reorganize runtime utility and server_args modules (#30447)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image.py`, `python/sglang/multimodal_gen/runtime/disaggregation/disagg_args.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py` _+32 more__
- **2026-07-10** [`1d8e3c248b`](https://github.com/sgl-project/sglang/commit/1d8e3c248b) [#30408](https://github.com/sgl-project/sglang/pull/30408)
  Fix DSV4 HiSparse SWA tail allocation forwarding (#30408)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/allocator/hisparse.py`, `test/registered/unit/managers/test_hisparse_unit.py`, `test/registered/unit/mem_cache/test_hisparse_allocator.py`_
- **2026-07-10** [`23390589f7`](https://github.com/sgl-project/sglang/commit/23390589f7) [#30713](https://github.com/sgl-project/sglang/pull/30713)
  [misc] Remove unit test cases that fail the admission criteria (round 3) (#30713)
  _Files: `test/registered/unit/batch_invariant_ops/test_batch_invariant_ops.py`, `test/registered/unit/constrained/test_base_grammar_backend.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`, `test/registered/unit/entrypoints/openai/test_serving_completions.py` _+15 more__
- **2026-07-10** [`7b9b2e4798`](https://github.com/sgl-project/sglang/commit/7b9b2e4798) [#30710](https://github.com/sgl-project/sglang/pull/30710)
  [style] Extract init-static values in memory-cache path (#30710)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/storage/eic/eic_storage.py`, `python/sglang/srt/mem_cache/storage/hf3fs/storage_hf3fs.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`_
- **2026-07-10** [`1e75ba236e`](https://github.com/sgl-project/sglang/commit/1e75ba236e) [#29408](https://github.com/sgl-project/sglang/pull/29408)
  Avoid implicit field-based side channel in Scheduler planning (#29408)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py` _+9 more__
- **2026-07-10** [`5be9c9f7c6`](https://github.com/sgl-project/sglang/commit/5be9c9f7c6) [#29407](https://github.com/sgl-project/sglang/pull/29407)
  Localize cur_batch field in Scheduler to avoid field-based state access (#29407)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py` _+6 more__
- **2026-07-09** [`8e54517f02`](https://github.com/sgl-project/sglang/commit/8e54517f02) [#29421](https://github.com/sgl-project/sglang/pull/29421)
  [Feat][GLM5.2] Add DSA Cache Layer Split under Prefill CP (#29421)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` _+17 more__
- **2026-07-09** [`e703f9e566`](https://github.com/sgl-project/sglang/commit/e703f9e566) [#30492](https://github.com/sgl-project/sglang/pull/30492)
  [refactor] Adopt get_parallel() everywhere and close out the parallel wrapper surface (#30492)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/configs/bailing_hybrid.py`, `python/sglang/srt/configs/falcon_h1.py`, `python/sglang/srt/configs/granitemoehybrid.py` _+67 more__
- **2026-07-09** [`65b14881c5`](https://github.com/sgl-project/sglang/commit/65b14881c5) [#30489](https://github.com/sgl-project/sglang/pull/30489)
  [refactor] Move the EP dispatcher and fusion-workspace manager state onto ctx.resources (#30489)
  _Files: `python/sglang/srt/elastic_ep/elastic_ep.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/moe/token_dispatcher/mooncake.py` _+3 more__
- **2026-07-09** [`866ae6848f`](https://github.com/sgl-project/sglang/commit/866ae6848f) [#25372](https://github.com/sgl-project/sglang/pull/25372)
  [PDD] Add true request retraction for PDD (#25372)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/prefill.py` _+8 more__
- **2026-07-09** [`1c9eb6bb0b`](https://github.com/sgl-project/sglang/commit/1c9eb6bb0b) [#30461](https://github.com/sgl-project/sglang/pull/30461)
  [DSV4] Fix draft SWA transfer for disaggregated MTP (#30461)
  _Files: `python/sglang/srt/disaggregation/utils.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-07-08** [`096551eed6`](https://github.com/sgl-project/sglang/commit/096551eed6) [#30409](https://github.com/sgl-project/sglang/pull/30409)
  Make CUDA graph disabling PD-role-aware (prefill/decode) (#30409)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` _+1 more__
- **2026-07-08** [`cc7d6659fd`](https://github.com/sgl-project/sglang/commit/cc7d6659fd) [#30440](https://github.com/sgl-project/sglang/pull/30440)
  feat(grpc): support disaggregated generation requests (#30440)
  _Files: `proto/sglang/runtime/v1/sglang.proto`, `rust/sglang-grpc/src/utils/request_utils.rs`_
- **2026-07-08** [`10e7f2925f`](https://github.com/sgl-project/sglang/commit/10e7f2925f) [#30435](https://github.com/sgl-project/sglang/pull/30435)
  [Fix] Chain the seq_lens publish event records so prebuilt seeding keeps the forward fence (#30435)
  _Files: `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/speculative/eagle_disaggregation.py`_
- **2026-07-08** [`108a183f6b`](https://github.com/sgl-project/sglang/commit/108a183f6b) [#30249](https://github.com/sgl-project/sglang/pull/30249)
  [mem_cache][6/N] refactor: move MHA host-pool into pool_host/mha.py (#30249)
  _Files: `benchmark/hf3fs/bench_zerocopy.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` _+11 more__
- **2026-07-08** [`c9303a08da`](https://github.com/sgl-project/sglang/commit/c9303a08da) [#29834](https://github.com/sgl-project/sglang/pull/29834)
  Fix scheduler crash on prefill-unreachable decode abort (#29834)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-07-08** [`b14f7b4f75`](https://github.com/sgl-project/sglang/commit/b14f7b4f75) [#30299](https://github.com/sgl-project/sglang/pull/30299)
  [refactor] Move model-capability adjustments into the resolution pipeline (#30299)
  _Files: `python/sglang/compile_deep_gemm.py`, `python/sglang/lang/backend/runtime_endpoint.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py` _+25 more__
- **2026-07-08** [`9bf122a455`](https://github.com/sgl-project/sglang/commit/9bf122a455) [#30386](https://github.com/sgl-project/sglang/pull/30386)
  [AMD] Run MI355X disaggregation Nightly Test with runtime checkout code mechanism (#30386)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`, `scripts/ci/slurm/launch_mi355x.sh`_
- **2026-07-07** [`36b449af19`](https://github.com/sgl-project/sglang/commit/36b449af19) [#28441](https://github.com/sgl-project/sglang/pull/28441)
  [EPD] Optimize multimodal global cache with paged embedding pool (#28441)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/embedding_cache_controller.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_embedding_store.py`, `test/registered/unit/mem_cache/test_embedding_cache_controller.py`_
- **2026-07-07** [`541f9221da`](https://github.com/sgl-project/sglang/commit/541f9221da) [#27564](https://github.com/sgl-project/sglang/pull/27564)
  feat(metrics): add Prometheus metrics for the EPD encoder server (#27564)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/observability/metrics_collector.py`, `python/sglang/srt/observability/req_time_stats.py`, `test/registered/observability/test_encoder_server_metrics.py`_
- **2026-07-06** [`b41552334d`](https://github.com/sgl-project/sglang/commit/b41552334d) [#30222](https://github.com/sgl-project/sglang/pull/30222)
  Fix disagg speculative decoding with NIXL connector (#30222)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`_

## Other  (21 commits)

- **2026-07-13** [`22c08a9bee`](https://github.com/sgl-project/sglang/commit/22c08a9bee) [#30956](https://github.com/sgl-project/sglang/pull/30956)
  Preserve RMSNorm shape in batch-invariant mode (#30956)
  _Files: `python/sglang/srt/layers/layernorm.py`_
- **2026-07-12** [`539253e1d5`](https://github.com/sgl-project/sglang/commit/539253e1d5) [#30927](https://github.com/sgl-project/sglang/pull/30927)
  Gate Rust extension builds (#30927)
  _Files: `python/setup.py`, `python/sglang/srt/server_args.py`_
- **2026-07-10** [`bc82b06400`](https://github.com/sgl-project/sglang/commit/bc82b06400) [#30810](https://github.com/sgl-project/sglang/pull/30810)
  Add ZYHowell to CI_PERMISSIONS.json (#30810)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-07-10** [`7090a49198`](https://github.com/sgl-project/sglang/commit/7090a49198) [#30788](https://github.com/sgl-project/sglang/pull/30788)
  update codeowners (#30788)
  _Files: `.github/CODEOWNERS`_
- **2026-07-10** [`94de28764c`](https://github.com/sgl-project/sglang/commit/94de28764c) [#30643](https://github.com/sgl-project/sglang/pull/30643)
  Fix TiktokenTokenizer missing num_special_tokens_to_add (#30643)
  _Files: `python/sglang/srt/tokenizer/tiktoken_tokenizer.py`_
- **2026-07-10** [`6174f1cad8`](https://github.com/sgl-project/sglang/commit/6174f1cad8) [#30766](https://github.com/sgl-project/sglang/pull/30766)
  [test] Set init-static attrs in mm_process_config mock fixtures (#30766)
  _Files: `test/registered/unit/managers/test_mm_process_config.py`_
- **2026-07-10** [`77b7698cad`](https://github.com/sgl-project/sglang/commit/77b7698cad) [#30649](https://github.com/sgl-project/sglang/pull/30649)
  Add tanujtiwari1998 to CI_PERMISSIONS.json (#30649)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-07-09** [`c46b291c77`](https://github.com/sgl-project/sglang/commit/c46b291c77) [#30701](https://github.com/sgl-project/sglang/pull/30701)
  [misc] Add init-static value extraction to the general code style rule (#30701)
  _Files: `.claude/rules/general-code-style.md`_
- **2026-07-09** [`6ab7a65d94`](https://github.com/sgl-project/sglang/commit/6ab7a65d94) [#30657](https://github.com/sgl-project/sglang/pull/30657)
  Support grad injection and step override in the dumper's model dump (#30657)
  _Files: `python/sglang/srt/debug_utils/dumper.py`, `test/registered/debug_utils/test_dumper.py`_
- **2026-07-09** [`5b28465eb9`](https://github.com/sgl-project/sglang/commit/5b28465eb9) [#30656](https://github.com/sgl-project/sglang/pull/30656)
  Cap diagnostic detail computation for failing tensors (#30656)
  _Files: `python/sglang/srt/debug_utils/comparator/bundle_comparator.py`, `python/sglang/srt/debug_utils/comparator/entrypoint.py`, `python/sglang/srt/debug_utils/comparator/tensor_comparator/comparator.py`, `test/registered/debug_utils/comparator/tensor_comparator/test_comparator.py` _+1 more__
- **2026-07-09** [`287291c232`](https://github.com/sgl-project/sglang/commit/287291c232) [#30655](https://github.com/sgl-project/sglang/pull/30655)
  Fix rel_diff being nan for bitwise-identical tensors (#30655)
  _Files: `python/sglang/srt/debug_utils/comparator/tensor_comparator/comparator.py`, `test/registered/debug_utils/comparator/tensor_comparator/test_comparator.py`_
- **2026-07-09** [`c02b032da0`](https://github.com/sgl-project/sglang/commit/c02b032da0) [#30631](https://github.com/sgl-project/sglang/pull/30631)
  [fix] Repoint the prefetch-dispatch test at the loader's current config binding (#30631)
  _Files: `test/registered/unit/model_loader/test_prefetch_checkpoints.py`_
- **2026-07-09** [`1f15308dca`](https://github.com/sgl-project/sglang/commit/1f15308dca) [#30493](https://github.com/sgl-project/sglang/pull/30493)
  [refactor] Retire the legacy config accessor and the remaining process singletons (#30493)
- **2026-07-09** [`bc5d376c2c`](https://github.com/sgl-project/sglang/commit/bc5d376c2c) [#30615](https://github.com/sgl-project/sglang/pull/30615)
  [Bench] Add fixed-prompt mode and per-request spec accept length metrics (#30615)
  _Files: `python/sglang/benchmark/one_batch_server.py`, `python/sglang/benchmark/serving.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_common.py`_
- **2026-07-09** [`9e4483d725`](https://github.com/sgl-project/sglang/commit/9e4483d725) [#30608](https://github.com/sgl-project/sglang/pull/30608)
  [misc] Add unit test admission criteria to agent rules (#30608)
  _Files: `.claude/rules/unit-test-admission.md`_
- **2026-07-09** [`6bce72d968`](https://github.com/sgl-project/sglang/commit/6bce72d968) [#30235](https://github.com/sgl-project/sglang/pull/30235)
  [Intel GPU] xpu_piecewise: fall back to eager when PCG capture stream is unset (#30235)
  _Files: `python/sglang/srt/compilation/xpu_piecewise_backend.py`_
- **2026-07-08** [`bc607ff650`](https://github.com/sgl-project/sglang/commit/bc607ff650) [#30483](https://github.com/sgl-project/sglang/pull/30483)
  Enhance mechanical refactor proof construction and verification skill (#30483)
  _Files: `.claude/skills/mechanical-refactor-verify/SKILL.md`, `.claude/skills/mechanical-refactor-verify/guide-construct-proof.md`, `.claude/skills/mechanical-refactor-verify/guide-split.md`, `.claude/skills/mechanical-refactor-verify/guide-verify-proof.md` _+25 more__
- **2026-07-08** [`6af1d5ff2d`](https://github.com/sgl-project/sglang/commit/6af1d5ff2d) [#28978](https://github.com/sgl-project/sglang/pull/28978)
  Enhance large class styles and code styles (#28978)
  _Files: `.claude/rules/general-code-style.md`, `.claude/rules/modify-component-must-read.md`, `.claude/skills/large-class-init-style/SKILL.md`, `.claude/skills/large-class-style/SKILL.md`_
- **2026-07-07** [`efdf02a38a`](https://github.com/sgl-project/sglang/commit/efdf02a38a) [#30312](https://github.com/sgl-project/sglang/pull/30312)
  [NPU]Add support --pre-warm-nccl (#30312)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/server_args.py`_
- **2026-07-06** [`e2b55bdbab`](https://github.com/sgl-project/sglang/commit/e2b55bdbab) [#28401](https://github.com/sgl-project/sglang/pull/28401)
  NUMA: probe numactl binding and fall back when --membind is rejected (#28401)
  _Files: `python/sglang/srt/utils/numa_utils.py`, `test/registered/utils/test_numa_utils.py`_
- **2026-07-06** [`24c42c90be`](https://github.com/sgl-project/sglang/commit/24c42c90be) [#30186](https://github.com/sgl-project/sglang/pull/30186)
  Clean up ServerArgs post-init dispatch (#30186)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/managers/test_mm_process_config.py`, `test/registered/unit/server_args/test_server_args.py`_

## KV Cache / Memory  (19 commits)

- **2026-07-11** [`ed554aac17`](https://github.com/sgl-project/sglang/commit/ed554aac17) [#30747](https://github.com/sgl-project/sglang/pull/30747)
  Fix: add grammar sync in PP for structured output (#30747)
  _Files: `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/distributed/communication_tags.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` _+2 more__
- **2026-07-10** [`7998fecfd1`](https://github.com/sgl-project/sglang/commit/7998fecfd1) [#30574](https://github.com/sgl-project/sglang/pull/30574)
  [kv canary] Support UnifiedRadixCache in kv-canary and bracket nested model.forward (#30574)
  _Files: `python/sglang/srt/kv_canary/api.py`, `python/sglang/srt/kv_canary/radix_cache_walker.py`, `python/sglang/srt/kv_canary/runner/canary_manager.py`, `python/sglang/srt/model_executor/runner/base_runner.py` _+1 more__
- **2026-07-10** [`0299393758`](https://github.com/sgl-project/sglang/commit/0299393758) [#30626](https://github.com/sgl-project/sglang/pull/30626)
  [UnifiedTree]: Sync mamba int8 checkpoint (#30626)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/mamba_component.py`, `test/registered/radix_cache/test_int8_mamba_checkpoint_e2e.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-07-10** [`2286e25a21`](https://github.com/sgl-project/sglang/commit/2286e25a21) [#30636](https://github.com/sgl-project/sglang/pull/30636)
  [UnifiedTree]: Sync Replay SSM  (#30636)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/mamba_component.py`_
- **2026-07-09** [`a36c873147`](https://github.com/sgl-project/sglang/commit/a36c873147) [#30703](https://github.com/sgl-project/sglang/pull/30703)
  [misc] Remove unit test cases that fail the admission criteria (round 2) (#30703)
  _Files: `.claude/rules/unit-test-admission.md`, `test/registered/unit/constrained/test_grammar_manager.py`, `test/registered/unit/entrypoints/openai/test_protocol.py`, `test/registered/unit/function_call/test_hunyuan_detector.py` _+20 more__
- **2026-07-09** [`b86466d54b`](https://github.com/sgl-project/sglang/commit/b86466d54b) [#30702](https://github.com/sgl-project/sglang/pull/30702)
  Make KvVmmArena JIT stub unique per process (#30702)
  _Files: `python/sglang/srt/mem_cache/kv_vmm_backing.py`_
- **2026-07-09** [`8d0fd34150`](https://github.com/sgl-project/sglang/commit/8d0fd34150) [#29417](https://github.com/sgl-project/sglang/pull/29417)
  [AMD] Enable unified-KV HiCache on DeepSeek-V4 (#29417)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` _+4 more__
- **2026-07-09** [`462b6171bd`](https://github.com/sgl-project/sglang/commit/462b6171bd) [#30339](https://github.com/sgl-project/sglang/pull/30339)
  [AMD] Fix stale SWA ring buffer on radix prefix reuse for DeepSeek-V4 with unified_kv backend (#30339)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/swa_radix_cache.py`_
- **2026-07-09** [`b0ecbceed9`](https://github.com/sgl-project/sglang/commit/b0ecbceed9) [#30653](https://github.com/sgl-project/sglang/pull/30653)
  [Bugfix] Migrate retired parallel accessors (#30653)
  _Files: `python/sglang/srt/layers/cp/utils.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/models/glm_image_vl.py`, `test/registered/unit/mem_cache/test_dsa_layer_split_broadcast.py`_
- **2026-07-08** [`fda87173ab`](https://github.com/sgl-project/sglang/commit/fda87173ab) [#30310](https://github.com/sgl-project/sglang/pull/30310)
  Revert "Increase the KV cache pool when using indexShare by 15% (#30310)" (#30472)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/model_executor/pool_configurator.py`_
- **2026-07-08** [`455ab36eeb`](https://github.com/sgl-project/sglang/commit/455ab36eeb) [#30310](https://github.com/sgl-project/sglang/pull/30310)
  Increase the KV cache pool when using indexShare by 15% (#30310)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/model_executor/pool_configurator.py`_
- **2026-07-08** [`9f5948c391`](https://github.com/sgl-project/sglang/commit/9f5948c391) [#29716](https://github.com/sgl-project/sglang/pull/29716)
  feat(mem_cache): add client-side metadata cache for HiCacheFile storage (#29716)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/storage/file/lru_file_evictor.py`, `test/registered/unit/mem_cache/test_hicache_file_lru_unit.py`_
- **2026-07-07** [`2ad9a243f5`](https://github.com/sgl-project/sglang/commit/2ad9a243f5) [#30157](https://github.com/sgl-project/sglang/pull/30157)
  Size KV pool after CUDA graph capture (opt-in) (#30157)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/swa.py` _+6 more__
- **2026-07-07** [`7fdc1cef17`](https://github.com/sgl-project/sglang/commit/7fdc1cef17) [#29701](https://github.com/sgl-project/sglang/pull/29701)
  [fix] Fix two trunk test regressions due to flexkv change (#29701) (#30372)
  _Files: `python/sglang/srt/mem_cache/storage/flexkv/flexkv_radix_cache.py`, `test/registered/unit/mem_cache/test_registry.py`_
- **2026-07-07** [`50aa97da45`](https://github.com/sgl-project/sglang/commit/50aa97da45) [#29701](https://github.com/sgl-project/sglang/pull/29701)
  Feat/flexkv main connector (#29701)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/registry.py`, `python/sglang/srt/mem_cache/storage/flexkv/README.md`, `python/sglang/srt/mem_cache/storage/flexkv/__init__.py` _+6 more__
- **2026-07-07** [`9a6f8e5992`](https://github.com/sgl-project/sglang/commit/9a6f8e5992) [#30333](https://github.com/sgl-project/sglang/pull/30333)
  [AMD] Fix DeepSeek V4 MTP accuracy issue (#30333)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_compress_state.py`_
- **2026-07-07** [`669fd4b8a5`](https://github.com/sgl-project/sglang/commit/669fd4b8a5) [#29887](https://github.com/sgl-project/sglang/pull/29887)
  [PP] Fix start_layer_id with pp in get kv_buffer_shape (#29887)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-07-07** [`abafe0022e`](https://github.com/sgl-project/sglang/commit/abafe0022e) [#30281](https://github.com/sgl-project/sglang/pull/30281)
  [Unified Radix Cache] Rename tree variables to cache in unittest (#30281)
  _Files: `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-07-07** [`c3da0a2582`](https://github.com/sgl-project/sglang/commit/c3da0a2582) [#30181](https://github.com/sgl-project/sglang/pull/30181)
  [MLX] Fix single-token chunked-prefill continuation misrouted as decode (#30181)
  _Files: `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `test/registered/unit/hardware_backend/mlx/test_tp_worker_routing.py`_

## Docs / Examples  (18 commits)

- **2026-07-11** [`79f096d43b`](https://github.com/sgl-project/sglang/commit/79f096d43b) [#30843](https://github.com/sgl-project/sglang/pull/30843)
  [DOCS][NPU]update npu support features and models (#30843)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_models.mdx`_
- **2026-07-11** [`e1d51be91f`](https://github.com/sgl-project/sglang/commit/e1d51be91f) [#30837](https://github.com/sgl-project/sglang/pull/30837)
  [Tiny] Fix a typo in cookbook (#30837)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`_
- **2026-07-10** [`e8646701c1`](https://github.com/sgl-project/sglang/commit/e8646701c1) [#30826](https://github.com/sgl-project/sglang/pull/30826)
  Update GLM-5.2 NVFP4 cookbook (#30826)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs_new/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-07-09** [`4153410477`](https://github.com/sgl-project/sglang/commit/4153410477) [#30647](https://github.com/sgl-project/sglang/pull/30647)
  [NPU] [DOC] remove unsupported models from Ascend NPU models list (#30647)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_models.mdx`_
- **2026-07-09** [`d8791fb5e3`](https://github.com/sgl-project/sglang/commit/d8791fb5e3) [#30494](https://github.com/sgl-project/sglang/pull/30494)
  [docs] Add the sglang-runtime-context skill (#30494)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`_
- **2026-07-09** [`666a09fe2a`](https://github.com/sgl-project/sglang/commit/666a09fe2a) [#30146](https://github.com/sgl-project/sglang/pull/30146)
  Disable multi-threaded load by default when prefetch is on (#30146)
  _Files: `docs_new/docs/advanced_features/model_loading.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-07-09** [`69ddbf9ef6`](https://github.com/sgl-project/sglang/commit/69ddbf9ef6) [#30577](https://github.com/sgl-project/sglang/pull/30577)
  [NPU] [DOC] fix model name error on Ascend NPU (#30577)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_models.mdx`_
- **2026-07-09** [`2b3d9ad375`](https://github.com/sgl-project/sglang/commit/2b3d9ad375) [#30579](https://github.com/sgl-project/sglang/pull/30579)
  [Tiny] Fix docstring in CP abstractions (#30579)
  _Files: `python/sglang/srt/layers/cp/interleave.py`, `python/sglang/srt/layers/cp/zigzag.py`_
- **2026-07-08** [`042228a195`](https://github.com/sgl-project/sglang/commit/042228a195) [#30504](https://github.com/sgl-project/sglang/pull/30504)
  [NPU] [DOC] Remove unsupported options of features on Ascend NPU (#30504)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_models.mdx`_
- **2026-07-07** [`631213c3bf`](https://github.com/sgl-project/sglang/commit/631213c3bf) [#29404](https://github.com/sgl-project/sglang/pull/29404)
  Add DeepReinforce Ornith-1.0 to cookbook (#29404)
  _Files: `docs_new/cards/logos/deepreinforce.png`, `docs_new/cookbook/autoregressive/DeepReinforce/Ornith-1.0.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json` _+1 more__
- **2026-07-07** [`d88644b430`](https://github.com/sgl-project/sglang/commit/d88644b430) [#30395](https://github.com/sgl-project/sglang/pull/30395)
  docs: sync LMSYS SGLang blog cards (#30395)
  _Files: `docs_new/index.mdx`_
- **2026-07-07** [`cfd3fdc54f`](https://github.com/sgl-project/sglang/commit/cfd3fdc54f) [#30370](https://github.com/sgl-project/sglang/pull/30370)
  [NPU] [DOC] Update features and mainstream models on ascend npu (#30370)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quick_start.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_models.mdx`_
- **2026-07-07** [`2d9f0b3317`](https://github.com/sgl-project/sglang/commit/2d9f0b3317) [#30328](https://github.com/sgl-project/sglang/pull/30328)
  [NPU] [DOC] Update arguments detail to NPU support features page (#30328)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-07-07** [`998acf7df8`](https://github.com/sgl-project/sglang/commit/998acf7df8) [#30324](https://github.com/sgl-project/sglang/pull/30324)
  [DOCS][NPU]update npu support features (#30324)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-07-07** [`3a679459e5`](https://github.com/sgl-project/sglang/commit/3a679459e5) [#29215](https://github.com/sgl-project/sglang/pull/29215)
  [bench] Add agentic-trace multi-turn dataset to bench_serving (#29215)
  _Files: `docs_new/docs/developer_guide/bench_serving.mdx`, `python/sglang/benchmark/datasets/__init__.py`, `python/sglang/benchmark/datasets/agentic_trace.py`, `python/sglang/benchmark/serving.py` _+1 more__
- **2026-07-07** [`cf4edda956`](https://github.com/sgl-project/sglang/commit/cf4edda956) [#30311](https://github.com/sgl-project/sglang/pull/30311)
  docs: sync LMSYS SGLang blog cards (#30311)
  _Files: `docs_new/index.mdx`_
- **2026-07-06** [`b3ab56545b`](https://github.com/sgl-project/sglang/commit/b3ab56545b) [#25364](https://github.com/sgl-project/sglang/pull/25364)
  Add Accuracy Benchmark for OCR models (#25364)
  _Files: `benchmark/ocr/README.md`, `benchmark/ocr/bench_sglang.py`, `benchmark/ocr/eval_utils.py`, `benchmark/ocr/generate_report.py` _+5 more__
- **2026-07-06** [`6f22790943`](https://github.com/sgl-project/sglang/commit/6f22790943) [#30201](https://github.com/sgl-project/sglang/pull/30201)
  cookbook: add Hunyuan 3 (Hy3) Day-0 page (#30201)
  _Files: `docs_new/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`, `docs_new/cookbook/autoregressive/Tencent/Hy3.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json` _+2 more__

## Triton / Kernels  (16 commits)

- **2026-07-12** [`24d59d8d74`](https://github.com/sgl-project/sglang/commit/24d59d8d74) [#30858](https://github.com/sgl-project/sglang/pull/30858)
  Fix CUDA 12 Docker dependency resolution (#30858)
  _Files: `docker/Dockerfile`_
- **2026-07-12** [`14bef7cd11`](https://github.com/sgl-project/sglang/commit/14bef7cd11) [#30580](https://github.com/sgl-project/sglang/pull/30580)
  fix: lazy load TileLang MHC kernels (#30580)
  _Files: `python/sglang/srt/layers/deepseek_v4_rope.py`, `python/sglang/srt/layers/mhc.py`_
- **2026-07-11** [`32cb89d412`](https://github.com/sgl-project/sglang/commit/32cb89d412) [#30813](https://github.com/sgl-project/sglang/pull/30813)
  ci: prune uv cache in job teardown to bound its growth (#30813)
  _Files: `scripts/ci/cuda/ci_cleanup_venv.sh`_
- **2026-07-10** [`6ed9843b57`](https://github.com/sgl-project/sglang/commit/6ed9843b57) [#30044](https://github.com/sgl-project/sglang/pull/30044)
  [Kernel] Introduce sglang.kernels namespace and migrate scattered triton_ops kernels (RFC #29630, Phase 2) (#30044)
- **2026-07-10** [`b76dd0be69`](https://github.com/sgl-project/sglang/commit/b76dd0be69) [#27757](https://github.com/sgl-project/sglang/pull/27757)
  Fix Mistral GSM8K chat eval (#27757)
  _Files: `python/pyproject.toml`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_common.py`, `python/sglang/test/simple_eval_gsm8k.py` _+6 more__
- **2026-07-10** [`073b36853f`](https://github.com/sgl-project/sglang/commit/073b36853f) [#30604](https://github.com/sgl-project/sglang/pull/30604)
  [CPU] update fla.cpp to support when num_head_v is not multiples of 16 (#30604)
  _Files: `sgl-kernel/csrc/cpu/mamba/fla.cpp`, `test/registered/cpu/test_mamba.py`_
- **2026-07-09** [`7e936f690e`](https://github.com/sgl-project/sglang/commit/7e936f690e) [#30699](https://github.com/sgl-project/sglang/pull/30699)
  [Tiny] Fix Lint in #30645 (#30699)
  _Files: `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/topk_impl.cuh`_
- **2026-07-09** [`10bb2eff3d`](https://github.com/sgl-project/sglang/commit/10bb2eff3d) [#27918](https://github.com/sgl-project/sglang/pull/27918)
  [BCG] Restore Qwen3.5 MRoPE fusion under breakable CUDA graph (#27918)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`_
- **2026-07-09** [`bda1dc0d95`](https://github.com/sgl-project/sglang/commit/bda1dc0d95) [#30645](https://github.com/sgl-project/sglang/pull/30645)
  [DSA] Fix top-k v2 emitting invalid indices under tie overflow / inf scores (IMA in FA3 sparse decode) (#30645)
  _Files: `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/topk_impl.cuh`_
- **2026-07-09** [`122b3266a2`](https://github.com/sgl-project/sglang/commit/122b3266a2) [#29729](https://github.com/sgl-project/sglang/pull/29729)
  Add opt-in SGLANG_ROPE_CACHE_FP32 to keep RoPE cache in fp32 on non-CUDA (#29729)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/rotary_embedding/base.py`_
- **2026-07-09** [`fdf6c70e3a`](https://github.com/sgl-project/sglang/commit/fdf6c70e3a) [#30597](https://github.com/sgl-project/sglang/pull/30597)
  fix arm test_norm.py error (#30597)
  _Files: `sgl-kernel/csrc/cpu/norm.cpp`_
- **2026-07-08** [`f3c3eea608`](https://github.com/sgl-project/sglang/commit/f3c3eea608) [#29925](https://github.com/sgl-project/sglang/pull/29925)
  ci: make multi-GPU jit test hangs attributable from the CI log (#29925)
  _Files: `python/sglang/jit_kernel/mp.py`, `python/sglang/jit_kernel/tests/utils.py`_
- **2026-07-07** [`946804e042`](https://github.com/sgl-project/sglang/commit/946804e042) [#30356](https://github.com/sgl-project/sglang/pull/30356)
  Disable FA3 sparse mask kernels by default (#30356)
  _Files: `sgl-kernel/CMakeLists.txt`_
- **2026-07-07** [`99db3b0fa5`](https://github.com/sgl-project/sglang/commit/99db3b0fa5) [#30306](https://github.com/sgl-project/sglang/pull/30306)
  ci: run jit-kernel tests on scheduled full runs (#30306)
  _Files: `.github/workflows/pr-test-jit-kernel.yml`, `.github/workflows/pr-test.yml`_
- **2026-07-07** [`30fb0dd851`](https://github.com/sgl-project/sglang/commit/30fb0dd851) [#30216](https://github.com/sgl-project/sglang/pull/30216)
  [CPU] add fused_qk_gemma_norm and refactor norm kernel implementation (#30216)
  _Files: `python/sglang/srt/models/qwen3_5.py`, `sgl-kernel/csrc/cpu/norm.cpp`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`, `sgl-kernel/csrc/cpu/vec.h` _+2 more__
- **2026-07-06** [`c016c6f355`](https://github.com/sgl-project/sglang/commit/c016c6f355) [#26788](https://github.com/sgl-project/sglang/pull/26788)
  [JIT Kernel] DeepSeek-V4 DSA indexer: faster top-k + page-table transform (runtime k <= 2048) (#26788)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/jit_kernel/dsv4/topk.py`, `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/topk/cluster.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/topk/common.cuh` _+7 more__

## Quantization  (11 commits)

- **2026-07-13** [`874fc07d9b`](https://github.com/sgl-project/sglang/commit/874fc07d9b) [#30784](https://github.com/sgl-project/sglang/pull/30784)
  [Kernel] Migrate scattered quantization kernels to sglang.kernels (RFC #29630, Phase 2.5, 1/7) (#30784)
- **2026-07-10** [`edd91cbdd5`](https://github.com/sgl-project/sglang/commit/edd91cbdd5) [#27168](https://github.com/sgl-project/sglang/pull/27168)
  [diffusion] feat: support action output for cosmos3 (#27168)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py` _+25 more__
- **2026-07-09** [`40a522203c`](https://github.com/sgl-project/sglang/commit/40a522203c) [#25694](https://github.com/sgl-project/sglang/pull/25694)
  [Quantization][Bugfix]: Join multi-arg RuntimeError in Quark _check_scheme_supported (#25694)
  _Files: `python/sglang/srt/layers/quantization/quark/quark.py`, `test/registered/unit/layers/quantization/test_quark_config.py`_
- **2026-07-09** [`48d98b7c68`](https://github.com/sgl-project/sglang/commit/48d98b7c68) [#25519](https://github.com/sgl-project/sglang/pull/25519)
  [Quantization][bugfix] Correct E8M0 NaN-sentinel detection in e8m0_to_f32 (#25519)
  _Files: `python/sglang/srt/layers/quantization/quark/utils.py`, `test/registered/unit/layers/quantization/test_quark_utils.py`_
- **2026-07-09** [`966350408e`](https://github.com/sgl-project/sglang/commit/966350408e) [#25467](https://github.com/sgl-project/sglang/pull/25467)
  [Quantization] Update error message strings with correct framework name in Quark/compressed-tensors (#25467)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/utils.py`_
- **2026-07-08** [`d7dcdf3efd`](https://github.com/sgl-project/sglang/commit/d7dcdf3efd) [#27926](https://github.com/sgl-project/sglang/pull/27926)
  [DSV4] perf: Make FP8 quant output tensor contiguous (#27926)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/fp8_wo_a_group_major_quant.cuh`, `python/sglang/jit_kernel/dsv4/__init__.py`, `python/sglang/jit_kernel/dsv4/fp8_wo_a.py`, `python/sglang/srt/models/deepseek_v4.py` _+1 more__
- **2026-07-07** [`e2ea7aafad`](https://github.com/sgl-project/sglang/commit/e2ea7aafad) [#30397](https://github.com/sgl-project/sglang/pull/30397)
  [Cherry pick to release/v0.5.15] Fix NVFP4 online quantization (#30397)
  _Files: `python/sglang/srt/layers/quantization/nvfp4_online.py`_
- **2026-07-07** [`ead1e490b5`](https://github.com/sgl-project/sglang/commit/ead1e490b5) [#30320](https://github.com/sgl-project/sglang/pull/30320)
  [Doc] Add LongCat 2.0 FP8 cookbook (#30320)
  _Files: `docs_new/cards/logos/meituan.png`, `docs_new/cookbook/autoregressive/Meituan/LongCat-2.0.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json` _+2 more__
- **2026-07-07** [`e85ef54877`](https://github.com/sgl-project/sglang/commit/e85ef54877) [#30117](https://github.com/sgl-project/sglang/pull/30117)
  Support Cutedsl BF16 GEMM JIT kernel (#30117)
  _Files: `python/sglang/jit_kernel/cutedsl_bf16_gemm.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/models/deepseek_v2.py` _+2 more__
- **2026-07-06** [`3abdbab9bb`](https://github.com/sgl-project/sglang/commit/3abdbab9bb) [#23650](https://github.com/sgl-project/sglang/pull/23650)
  :sparkles: [llm][npu][quant] Add W4A8 MXFP quantization support for Qwen3 Dense on Ascend NPU (#23650)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quantization.mdx`, `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`, `python/sglang/srt/hardware_backend/npu/utils.py` _+6 more__
- **2026-07-06** [`b1942fc3ea`](https://github.com/sgl-project/sglang/commit/b1942fc3ea) [#27906](https://github.com/sgl-project/sglang/pull/27906)
  [Model] Support Qwen3.6 ModelOpt mixed NVFP4 (#27906)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/layers/vocab_parallel_embedding.py` _+4 more__

## Scheduler / Batching  (11 commits)

- **2026-07-12** [`81d273f73b`](https://github.com/sgl-project/sglang/commit/81d273f73b) [#30897](https://github.com/sgl-project/sglang/pull/30897)
  Handle coredump dirs and cache hit updates (#30897)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-07-10** [`5e3dc5dd5f`](https://github.com/sgl-project/sglang/commit/5e3dc5dd5f) [#30215](https://github.com/sgl-project/sglang/pull/30215)
  Fix immediate profiler step range boundary (#30215)
  _Files: `python/sglang/srt/managers/scheduler_components/profiler_manager.py`_
- **2026-07-10** [`b5e75b9423`](https://github.com/sgl-project/sglang/commit/b5e75b9423) [#30707](https://github.com/sgl-project/sglang/pull/30707)
  [style] Extract init-static values in scheduler hot path (#30707)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`_
- **2026-07-10** [`32c8973ce8`](https://github.com/sgl-project/sglang/commit/32c8973ce8) [#30573](https://github.com/sgl-project/sglang/pull/30573)
  Configurable decode retraction order (#30573)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/server_args.py`_
- **2026-07-10** [`69368d7593`](https://github.com/sgl-project/sglang/commit/69368d7593) [#29406](https://github.com/sgl-project/sglang/pull/29406)
  Stop reading cur_batch in is_fully_idle and abort_request (#29406)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`_
- **2026-07-10** [`2e66707399`](https://github.com/sgl-project/sglang/commit/2e66707399) [#29405](https://github.com/sgl-project/sglang/pull/29405)
  Fix pipeline-parallel abort missing in-flight requests in non-current microbatch slots (#29405)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/manual/scheduler/test_scripted_pp_abort.py`_
- **2026-07-10** [`cfc66e05c5`](https://github.com/sgl-project/sglang/commit/cfc66e05c5) [#30630](https://github.com/sgl-project/sglang/pull/30630)
  [tokenizer] Support pluggable tokenizer worker class in multi-tokenizer mode (#30630)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/managers/test_multi_tokenizer_mixin.py`_
- **2026-07-09** [`1959335997`](https://github.com/sgl-project/sglang/commit/1959335997) [#30525](https://github.com/sgl-project/sglang/pull/30525)
  refactor(load-snapshot): build LoadSnapshot directly, drop legacy get_loads IPC (#30525)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/load_snapshot.py`, `python/sglang/srt/managers/scheduler.py` _+4 more__
- **2026-07-09** [`64e2a73c80`](https://github.com/sgl-project/sglang/commit/64e2a73c80) [#30606](https://github.com/sgl-project/sglang/pull/30606)
  [Fix] Serialize FanOutCommunicator queueing calls with a FIFO-fair asyncio.Lock (#30606)
  _Files: `python/sglang/srt/managers/communicator.py`, `test/registered/unit/managers/test_fanout_communicator.py`_
- **2026-07-08** [`8f9307736a`](https://github.com/sgl-project/sglang/commit/8f9307736a) [#30471](https://github.com/sgl-project/sglang/pull/30471)
  [misc] Add CI-only guards for the FutureMap seq_lens relay (#30471)
  _Files: `python/sglang/srt/managers/overlap_utils.py`_
- **2026-07-08** [`45019b56ce`](https://github.com/sgl-project/sglang/commit/45019b56ce) [#30463](https://github.com/sgl-project/sglang/pull/30463)
  [Bugfix] Map reasoning_effort=low to Nemotron-3 Super low_effort + warn on unsupported levels (#30463)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/managers/template_detection.py`, `test/registered/unit/entrypoints/openai/test_protocol.py` _+2 more__

## Tensor / Data Parallel  (9 commits)

- **2026-07-11** [`9b4bb415dd`](https://github.com/sgl-project/sglang/commit/9b4bb415dd) [#30834](https://github.com/sgl-project/sglang/pull/30834)
  [cuda-graph] Size breakable-graph shared buffer from warmup output; slice by produced row count (#30834)
  _Files: `python/sglang/srt/model_executor/runner_backend/breakable_cuda_graph_backend.py`_
- **2026-07-09** [`7132af28de`](https://github.com/sgl-project/sglang/commit/7132af28de) [#30396](https://github.com/sgl-project/sglang/pull/30396)
  Fix garbage output for bare-tekken Mistral checkpoints (e.g. Leanstral) (#30396)
  _Files: `python/sglang/srt/utils/hf_transformers/common.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py`, `python/sglang/srt/utils/hf_transformers/tokenizer.py`, `test/registered/unit/tokenizer/test_tekken_tokenizer_routing.py`_
- **2026-07-09** [`0d7e8cfb85`](https://github.com/sgl-project/sglang/commit/0d7e8cfb85) [#30654](https://github.com/sgl-project/sglang/pull/30654)
  Support per-regex diff-threshold predicates in the tensor comparator (#30654)
  _Files: `python/sglang/srt/debug_utils/comparator/aligner/unsharder/executor.py`, `python/sglang/srt/debug_utils/comparator/bundle_comparator.py`, `python/sglang/srt/debug_utils/comparator/entrypoint.py`, `python/sglang/srt/debug_utils/comparator/tensor_comparator/comparator.py` _+13 more__
- **2026-07-09** [`bd7e54d737`](https://github.com/sgl-project/sglang/commit/bd7e54d737) [#30557](https://github.com/sgl-project/sglang/pull/30557)
  [AMD] Fix AITER custom all-gather CUDA-graph capture crash under torch_memory_saver (#30557)
  _Files: `python/sglang/srt/distributed/parallel_state.py`_
- **2026-07-08** [`074bb928f0`](https://github.com/sgl-project/sglang/commit/074bb928f0) [#26052](https://github.com/sgl-project/sglang/pull/26052)
  Move template manager files under parser; update CODEOWNERS (#26052)
  _Files: `.github/CODEOWNERS`, `python/sglang/srt/entrypoints/anthropic/serving.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py` _+10 more__
- **2026-07-08** [`4c5fe42be4`](https://github.com/sgl-project/sglang/commit/4c5fe42be4) [#30512](https://github.com/sgl-project/sglang/pull/30512)
  [DSA] Fix IMA in fused top-k v2: write all output slots on tie overflow (#30512)
  _Files: `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/topk_impl.cuh`_
- **2026-07-07** [`3d2e7cc601`](https://github.com/sgl-project/sglang/commit/3d2e7cc601) [#23508](https://github.com/sgl-project/sglang/pull/23508)
  [gRPC] Native server: launcher + HTTP + server args wiring (3/4) (#23508)
  _Files: `python/sglang/launch_server.py`, `python/sglang/srt/entrypoints/grpc_server.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/environ.py` _+2 more__
- **2026-07-06** [`d8462f4961`](https://github.com/sgl-project/sglang/commit/d8462f4961) [#29783](https://github.com/sgl-project/sglang/pull/29783)
  Fixes for NVFP4 numerical accuracy for router GEMM output and wrong correction bias cast (#29783)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-07-06** [`7c9bb316cf`](https://github.com/sgl-project/sglang/commit/7c9bb316cf) [#30214](https://github.com/sgl-project/sglang/pull/30214)
  docs(cookbook): total (input+output) throughput per GPU + percentile latency labels (#30214)
  _Files: `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/benchmarks.jsx.tmpl`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-review-pr/SKILL.md` _+9 more__

## ROCm / AMD  (6 commits)

- **2026-07-13** [`80965db8d3`](https://github.com/sgl-project/sglang/commit/80965db8d3) [#30942](https://github.com/sgl-project/sglang/pull/30942)
  [AMD] Pin cmake==4.3.4 in ROCm Dockerfile to fix MoRI gtest_discover build break (#30942)
  _Files: `docker/rocm.Dockerfile`_
- **2026-07-08** [`c55190a638`](https://github.com/sgl-project/sglang/commit/c55190a638) [#30446](https://github.com/sgl-project/sglang/pull/30446)
  [AMD] Register 2 CPU-bound 1-GPU tests (phase_checker, scripted_runtime_core) for AMD PR CI (#30446)
  _Files: `test/registered/scripted_runtime/test_scripted_runtime_core.py`, `test/registered/utils/test_phase_checker.py`_
- **2026-07-08** [`47a6dfd708`](https://github.com/sgl-project/sglang/commit/47a6dfd708) [#30212](https://github.com/sgl-project/sglang/pull/30212)
  [AMD] Register 3 ROCm-portable JIT kernel tests for AMD CI (#30212)
  _Files: `test/registered/jit/test_dsv32_indexer_fusion.py`, `test/registered/jit/test_rmsnorm.py`, `test/registered/jit/test_rope.py`_
- **2026-07-08** [`fc378f843e`](https://github.com/sgl-project/sglang/commit/fc378f843e) [#30534](https://github.com/sgl-project/sglang/pull/30534)
  [AMD] Temporarily reduce AMD scheduled test frequency to save resource (#30534)
  _Files: `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/pr-test-amd.yml`_
- **2026-07-08** [`669b4bc72b`](https://github.com/sgl-project/sglang/commit/669b4bc72b) [#30496](https://github.com/sgl-project/sglang/pull/30496)
  [AMD] Gate stage-c on stage-b-test-1-gpu-large-amd (#30496)
  _Files: `.github/workflows/pr-test-amd.yml`_
- **2026-07-06** [`c9ceab34cf`](https://github.com/sgl-project/sglang/commit/c9ceab34cf) [#29394](https://github.com/sgl-project/sglang/pull/29394)
  [AMD] [Docker] Update MoRI to v1.2.1 (#29394)
  _Files: `docker/rocm.Dockerfile`_

## Speculative Decoding  (4 commits)

- **2026-07-11** [`268b8e127f`](https://github.com/sgl-project/sglang/commit/268b8e127f) [#30589](https://github.com/sgl-project/sglang/pull/30589)
  [NPU][bugfix] Fix NPU KernelLaunch Failure in rotate_input_ids_triton with Empty Batch (#30589)
  _Files: `python/sglang/kernels/ops/speculative/multi_layer_eagle.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-07-07** [`801571e949`](https://github.com/sgl-project/sglang/commit/801571e949) [#30303](https://github.com/sgl-project/sglang/pull/30303)
  [spec decoding] support rejection sampling in multi layer eagle (#30303)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` _+1 more__
- **2026-07-07** [`c861896721`](https://github.com/sgl-project/sglang/commit/c861896721) [#30297](https://github.com/sgl-project/sglang/pull/30297)
  [refactor] Resolve config declarations onto server_args at the end of __post_init__ (#30297)
  _Files: `python/sglang/srt/arg_groups/hisparse_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/server_args.py` _+7 more__
- **2026-07-06** [`850719ebd9`](https://github.com/sgl-project/sglang/commit/850719ebd9) [#30048](https://github.com/sgl-project/sglang/pull/30048)
  [XPU] Unbreak stage-b: re-add --disable-decode-cuda-graph, quarantine EAGLE3 parity (#30048)
  _Files: `test/registered/spec/eagle/test_spec_eagle_parity.py`_

## CI / Build  (4 commits)

- **2026-07-10** [`3f1694f5e0`](https://github.com/sgl-project/sglang/commit/3f1694f5e0) [#30697](https://github.com/sgl-project/sglang/pull/30697)
  Update sgl-deep-gemm to 0.1.4.post1 (#30697)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`_
- **2026-07-08** [`937734d3ed`](https://github.com/sgl-project/sglang/commit/937734d3ed) [#30495](https://github.com/sgl-project/sglang/pull/30495)
  ci(nightly): add force_baseline_update dispatch input for precision job (#30495)
  _Files: `.github/workflows/nightly-test-nvidia.yml`_
- **2026-07-07** [`0bf7ddb481`](https://github.com/sgl-project/sglang/commit/0bf7ddb481) [#30308](https://github.com/sgl-project/sglang/pull/30308)
  docs(install): add nightly install + docker tag guidance, and auto-bump version on release tag (#30308)
  _Files: `.github/workflows/bot-bump-docs-version.yml`, `docs_new/docs/get-started/install.mdx`, `scripts/release/README.md`, `scripts/release/bump_docs_install_version.py`_
- **2026-07-06** [`cc7d7ba3dd`](https://github.com/sgl-project/sglang/commit/cc7d7ba3dd) [#30100](https://github.com/sgl-project/sglang/pull/30100)
  [Intel XPU] Bump nightly per-file timeout to 120m and extend XPU CI monitor (#30100)
  _Files: `.github/workflows/nightly-test-intel.yml`, `.github/workflows/xpu-ci-job-monitor.yml`, `scripts/ci/xpu/xpu_ci_start_container.sh`_

## Serving / API  (3 commits)

- **2026-07-10** [`4fcc994be1`](https://github.com/sgl-project/sglang/commit/4fcc994be1) [#30811](https://github.com/sgl-project/sglang/pull/30811)
  Support priority request header override (#30811)
  _Files: `python/sglang/srt/entrypoints/request_headers.py`, `test/registered/cpu/test_request_headers.py`_
- **2026-07-10** [`fd19a76237`](https://github.com/sgl-project/sglang/commit/fd19a76237) [#29883](https://github.com/sgl-project/sglang/pull/29883)
  [BUG] fix strip streaming empty-string suffix from DSV4 tool arguments (#29883)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-07-09** [`078f06fbf4`](https://github.com/sgl-project/sglang/commit/078f06fbf4) [#30623](https://github.com/sgl-project/sglang/pull/30623)
  [Refactor] Share chat encoding dispatch between serving and offline tools (#30623)
  _Files: `python/sglang/benchmark/one_batch_server.py`, `python/sglang/srt/entrypoints/openai/chat_encoding.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`_

## Models  (2 commits)

- **2026-07-13** [`cbcbef6811`](https://github.com/sgl-project/sglang/commit/cbcbef6811) [#30968](https://github.com/sgl-project/sglang/pull/30968)
  [Bugfix] Fix Nemotron ForwardFlags across custom op boundary (#30968)
  _Files: `python/sglang/srt/models/nemotron_h.py`, `test/registered/models_e2e/test_nvidia_nemotron_3_nano.py`_
- **2026-07-07** [`6875df3378`](https://github.com/sgl-project/sglang/commit/6875df3378) [#30400](https://github.com/sgl-project/sglang/pull/30400)
  [Cherry pick to release/v0.5.15] Fix NVILA weight loading (#30400)
  _Files: `python/sglang/srt/models/nvila.py`, `python/sglang/srt/models/nvila_lite.py`_

## LoRA  (1 commits)

- **2026-07-07** [`5e9032c527`](https://github.com/sgl-project/sglang/commit/5e9032c527) [#30358](https://github.com/sgl-project/sglang/pull/30358)
  [NPU]Modify LoRA heading in ascend_npu_support_features.mdx to specify Qwen model limitations. (#30358)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_

---
_Generated 2026-07-13 11:22 UTC_