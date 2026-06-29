# sgl-project/sglang — Weekly Change Report
**Period:** 2026-06-22 → 2026-06-29  |  **Total commits:** 316

## ✨ New Features This Week

- **2026-06-29** [#29632](https://github.com/sgl-project/sglang/pull/29632) — [NPU] [DOC] Update deterministic inference feature support status to A2, A3 (#29632)
- **2026-06-29** [#29640](https://github.com/sgl-project/sglang/pull/29640) — Add Qwen3 MoE tests for PP compatibility with CP and DP (#29640)
- **2026-06-29** [#26929](https://github.com/sgl-project/sglang/pull/26929) — Add stochastic rounding for FP16 Mamba SSM cache (#26929)
- **2026-06-29** [#29338](https://github.com/sgl-project/sglang/pull/29338) — [Spec] Add DFLASH basic sanity CI test (#29338)
- **2026-06-29** [#29549](https://github.com/sgl-project/sglang/pull/29549) — Replace hasattr with isinstance in SHM feature helpers (#29549)
- **2026-06-29** [#28974](https://github.com/sgl-project/sglang/pull/28974) — [weight checker] refactor: add precision branch; allow ULP quant err; used chunked compare (#28974)
- **2026-06-29** [#29378](https://github.com/sgl-project/sglang/pull/29378) — [CPU] enable fused_sigmoid_mul on CPU device (#29378)
- **2026-06-29** [#28308](https://github.com/sgl-project/sglang/pull/28308) — [Intel GPU] add pytorch profiling support for XPU in bench offline throughput and enhance num steps (#28308)
- **2026-06-28** [#29535](https://github.com/sgl-project/sglang/pull/29535) — [scheduler] Add scheduler metrics reporter init hook (#29535)
- **2026-06-28** [#29436](https://github.com/sgl-project/sglang/pull/29436) — feat: first-class session identity in SGLang (#29436)
- _…and 64 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-06-27** [`91f9e7372d`](https://github.com/sgl-project/sglang/commit/91f9e7372d) [#28762](https://github.com/sgl-project/sglang/pull/28762) — [diffusion] CI: refactor CI (#28762)
- **2026-06-27** [`81d3c3ce77`](https://github.com/sgl-project/sglang/commit/81d3c3ce77) [#29373](https://github.com/sgl-project/sglang/pull/29373) — [AMD] [GLM5] Guard cuda_runtime.h for ROCm in fused_metadata_copy (#29373)
- **2026-06-27** [`43435a2f8e`](https://github.com/sgl-project/sglang/commit/43435a2f8e) [#29097](https://github.com/sgl-project/sglang/pull/29097) — [mori] Add a combine-kwargs hook and use_external_inp_buf plumbing (#29097)
- **2026-06-27** [`19abebcc6a`](https://github.com/sgl-project/sglang/commit/19abebcc6a) [#29096](https://github.com/sgl-project/sglang/pull/29096) — [server_args] Make MoRI per-rank dispatch-token requirement overridable (#29096)
- **2026-06-26** [`c470acde2b`](https://github.com/sgl-project/sglang/commit/c470acde2b) [#29333](https://github.com/sgl-project/sglang/pull/29333) — [AMD] Register 1 kernel unit test for AMD nightly CI (#29333)
- **2026-06-26** [`5eebb4b2e8`](https://github.com/sgl-project/sglang/commit/5eebb4b2e8) [#29377](https://github.com/sgl-project/sglang/pull/29377) — [AMD] Fix fused append+remap DeepEP equivalence test on aiter path (#29377)
- **2026-06-26** [`b73e57210a`](https://github.com/sgl-project/sglang/commit/b73e57210a) [#28853](https://github.com/sgl-project/sglang/pull/28853) — [AMD CI] Add nightly Miles ROCm 7.2 MI350X suites (#28853)
- **2026-06-26** [`7f376644e0`](https://github.com/sgl-project/sglang/commit/7f376644e0) [#29313](https://github.com/sgl-project/sglang/pull/29313) — [AMD] [GLM5] Mark EAGLE verified on MI300X/MI325X (gfx942) in GLM-5.1 cookbook (#29313)
- **2026-06-26** [`413aeac0c9`](https://github.com/sgl-project/sglang/commit/413aeac0c9) [#29084](https://github.com/sgl-project/sglang/pull/29084) — [AMD][DI][CI] 1/N: MI355X disaggregation nightly benchmark (#29084)
- **2026-06-25** [`38e857f423`](https://github.com/sgl-project/sglang/commit/38e857f423) [#29236](https://github.com/sgl-project/sglang/pull/29236) — [MUSA][diffusion] Bump torchada version to 0.1.68 (#29236)
- **2026-06-25** [`b7d3c3016d`](https://github.com/sgl-project/sglang/commit/b7d3c3016d) [#29103](https://github.com/sgl-project/sglang/pull/29103) — [AMD] Feat/dsv4 aiter reduce scatter decode (#29103)
- **2026-06-25** [`e6efe10072`](https://github.com/sgl-project/sglang/commit/e6efe10072) [#29197](https://github.com/sgl-project/sglang/pull/29197) — [AMD] Register 5 JIT kernel unit tests for AMD nightly CI (#29197)
- **2026-06-25** [`bc150173b2`](https://github.com/sgl-project/sglang/commit/bc150173b2) [#29234](https://github.com/sgl-project/sglang/pull/29234) — [AMD] Fix stage-b-test-1-gpu-small-amd-nondeterministic timeout after VLM model swap (#29234)
- **2026-06-25** [`0075c8f02b`](https://github.com/sgl-project/sglang/commit/0075c8f02b) [#29194](https://github.com/sgl-project/sglang/pull/29194) — [AMD] [GLM5] GLM-5.1 MXFP4 (MI355X) + enable EAGLE for gfx950 in cookbook (#29194)
- **2026-06-25** [`3d3a7ec031`](https://github.com/sgl-project/sglang/commit/3d3a7ec031) [#28237](https://github.com/sgl-project/sglang/pull/28237) — [AMD] fix(moe): correct fused shared-expert scaling on aiter/DeepEP path (mori all-to-all) (#28237)
- **2026-06-25** [`ec12a28a87`](https://github.com/sgl-project/sglang/commit/ec12a28a87) [#28967](https://github.com/sgl-project/sglang/pull/28967) — [AMD] Register 7 JIT kernel unit tests for AMD nightly CI (#28967)
- **2026-06-25** [`4ba8634780`](https://github.com/sgl-project/sglang/commit/4ba8634780) [#29058](https://github.com/sgl-project/sglang/pull/29058) — [AMD] Register scripted-core chunked-prefill test for AMD extra-a CI (#29058)
- **2026-06-25** [`de2d01c8da`](https://github.com/sgl-project/sglang/commit/de2d01c8da) [#28450](https://github.com/sgl-project/sglang/pull/28450) — [AMD] Fuse shared-expert append + DeepEP remap into one Triton kernel (#28450)
- **2026-06-25** [`9215da2515`](https://github.com/sgl-project/sglang/commit/9215da2515) [#28757](https://github.com/sgl-project/sglang/pull/28757) — [AMD] [GLM5] skip redundant -inf pre-fill of HIP indexer MQA-logits (#28757)
- **2026-06-25** [`d1cf09d4d4`](https://github.com/sgl-project/sglang/commit/d1cf09d4d4) [#29219](https://github.com/sgl-project/sglang/pull/29219) — [AMD-miles] Add a ROCm 7.0 MI35x miles nightly image (#29219)
- **2026-06-25** [`c7734e6871`](https://github.com/sgl-project/sglang/commit/c7734e6871) [#29220](https://github.com/sgl-project/sglang/pull/29220) — [Spec] Dissolve `EagleDraftInputV2Mixin` so spec-info dataclasses hold data only (#29220)
- **2026-06-24** [`e04ed05193`](https://github.com/sgl-project/sglang/commit/e04ed05193) [#28623](https://github.com/sgl-project/sglang/pull/28623) — [CI] reduce CPU CI scope with base-c suite (#28623)
- **2026-06-24** [`20b2817bdf`](https://github.com/sgl-project/sglang/commit/20b2817bdf) [#27833](https://github.com/sgl-project/sglang/pull/27833) — [AMD] Enable BCG on ROCm + route aiter prefill via MHA during PCG/BCG capture for Kimi-2.5 (#27833)
- **2026-06-24** [`7454735be9`](https://github.com/sgl-project/sglang/commit/7454735be9) [#28975](https://github.com/sgl-project/sglang/pull/28975) — [AMD] [GLM5] Add opt-in Triton fp8 sparse-MLA prefill kernel for gfx950 (#28975)
- **2026-06-24** [`5e6d7c1615`](https://github.com/sgl-project/sglang/commit/5e6d7c1615) [#28455](https://github.com/sgl-project/sglang/pull/28455) — [AMD] Fix DeepSeek-V4 fp8 KV path on gfx942 (e4m3fnuz) (#28455)
- **2026-06-24** [`c07811bfc6`](https://github.com/sgl-project/sglang/commit/c07811bfc6) [#29091](https://github.com/sgl-project/sglang/pull/29091) — [AMD] Register MI355X 2N 1P1D disagg nightly workflow for testing (#29091)
- **2026-06-24** [`b2c8f7a22e`](https://github.com/sgl-project/sglang/commit/b2c8f7a22e) [#25090](https://github.com/sgl-project/sglang/pull/25090) — [AMD] Support triton backend decode context parallel for Qwen3.5 (#25090)
- **2026-06-23** [`e0dc8b7137`](https://github.com/sgl-project/sglang/commit/e0dc8b7137) [#28084](https://github.com/sgl-project/sglang/pull/28084) — [AMD] Fuse topk padded-token masking into a single Triton kernel (#28084)
- **2026-06-23** [`af9027f6c9`](https://github.com/sgl-project/sglang/commit/af9027f6c9) [#28938](https://github.com/sgl-project/sglang/pull/28938) — [AMD] Improve performance of dsv4 in high concurrency (#28938)
- **2026-06-23** [`854c688121`](https://github.com/sgl-project/sglang/commit/854c688121) [#28754](https://github.com/sgl-project/sglang/pull/28754) — [Spec] Unify decode KV-commit bookkeeping across spec-v2 workers (#28754)
- **2026-06-23** [`52a90c9a36`](https://github.com/sgl-project/sglang/commit/52a90c9a36) [#28777](https://github.com/sgl-project/sglang/pull/28777) — docs(minimax-m3): use published AMD ROCm images (#28777)
- **2026-06-23** [`7e6587c94a`](https://github.com/sgl-project/sglang/commit/7e6587c94a) [#28981](https://github.com/sgl-project/sglang/pull/28981) — [AMD] Update v4 cookbook to clean env vars (#28981)
- **2026-06-23** [`b42c79c4eb`](https://github.com/sgl-project/sglang/commit/b42c79c4eb) [#28989](https://github.com/sgl-project/sglang/pull/28989) — [AMD] Fix AMD extra scheduled runs cancelling each other (#28989)
- **2026-06-23** [`28d5627fd8`](https://github.com/sgl-project/sglang/commit/28d5627fd8) [#28850](https://github.com/sgl-project/sglang/pull/28850) — [AMD] register kv_canary + mock_model e2e tests to extra-a (1-gpu-small + 2-gpu-large) (#28850)
- **2026-06-22** [`7c23d2255a`](https://github.com/sgl-project/sglang/commit/7c23d2255a) [#28712](https://github.com/sgl-project/sglang/pull/28712) — [minimax-m3] Split 1/4: sparse attention ops + JIT kernels + config foundation (#28712)
- **2026-06-22** [`cee1caaf47`](https://github.com/sgl-project/sglang/commit/cee1caaf47) [#28941](https://github.com/sgl-project/sglang/pull/28941) — [AMD] Fix nightly-8-gpu-mi35x-deepseek-v4-flash-rocm720 OOM issue (#28941)
- **2026-06-22** [`04d952ea10`](https://github.com/sgl-project/sglang/commit/04d952ea10) [#28920](https://github.com/sgl-project/sglang/pull/28920) — [AMD] deepseek-v4 clean env vars (#28920)
- **2026-06-22** [`dd39ef6cec`](https://github.com/sgl-project/sglang/commit/dd39ef6cec) [#28869](https://github.com/sgl-project/sglang/pull/28869) — [AMD] Pin httpx>=0.25.0 to fix anthropic SDK socket_options error (#28869)
- **2026-06-22** [`441ae9a5ae`](https://github.com/sgl-project/sglang/commit/441ae9a5ae) [#28885](https://github.com/sgl-project/sglang/pull/28885) — [Lint] Fix black formatting of DeepSeek-R1-MXFP4 MI35x tests (#28885)
- **2026-06-22** [`64e455d4bf`](https://github.com/sgl-project/sglang/commit/64e455d4bf) [#28886](https://github.com/sgl-project/sglang/pull/28886) — Fix lint break on main (#28886)
- **2026-06-22** [`e2540188ce`](https://github.com/sgl-project/sglang/commit/e2540188ce) [#27243](https://github.com/sgl-project/sglang/pull/27243) — [AMD] Clean up DeepSeek-R1-MXFP4 TP2/TP4 MLA GSM8K tests (#27243)
- **2026-06-22** [`fd7874d11b`](https://github.com/sgl-project/sglang/commit/fd7874d11b) [#28495](https://github.com/sgl-project/sglang/pull/28495) — [AMD] Register DP attention test (#28495)
- **2026-06-22** [`73448b0d70`](https://github.com/sgl-project/sglang/commit/73448b0d70) [#28871](https://github.com/sgl-project/sglang/pull/28871) — [AMD] Temporarily disable deepseek V4 in AMD PR test (#28871)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-06-29 |
| [#27574](https://github.com/sgl-project/sglang/issues/27574) | [Agentic Inference] Programmatic KV Cache for Agentic Workloads | high priority | 2026-06-29 |
| [#29562](https://github.com/sgl-project/sglang/issues/29562) | [Bug] GLM-5.2-NVFP4 error on pro6000 | — | 2026-06-29 |
| [#22092](https://github.com/sgl-project/sglang/issues/22092) | [Feature] Parity with CUDA -  AMD when will it support DWDP based para | inactive | 2026-06-29 |
| [#29590](https://github.com/sgl-project/sglang/issues/29590) | [AMD][multimodal-gen] HIPBLAS_STATUS_NOT_SUPPORTED in torch._scaled_mm | — | 2026-06-29 |
| [#29573](https://github.com/sgl-project/sglang/issues/29573) | [Feature] RFC: Paper Reproduction of LMetric Multiplication Scheduling | — | 2026-06-28 |
| [#28479](https://github.com/sgl-project/sglang/issues/28479) | Clarify maintenance status of legacy TensorDumper vs. new Dumper | — | 2026-06-28 |
| [#28992](https://github.com/sgl-project/sglang/issues/28992) | [Bug] `intel_amx` backend can segfault non-deterministically during lo | — | 2026-06-28 |
| [#28511](https://github.com/sgl-project/sglang/issues/28511) | [RFC] Porting ReplaySSM to SGLang: faster decode and speculative decod | RFC, linear-attention | 2026-06-28 |
| [#28852](https://github.com/sgl-project/sglang/issues/28852) | Support MiniMax-M3-MXFP8 on H200 with fallback/dequant path | — | 2026-06-28 |
| [#22072](https://github.com/sgl-project/sglang/issues/22072) | [Bug] EP/DP decode server hangs at startup on MI325X with MoRI a2a bac | inactive | 2026-06-28 |
| [#29477](https://github.com/sgl-project/sglang/issues/29477) | [Bug] CUDA exception / 8-rank collective abort in NCCL AllReduce_RING_ | — | 2026-06-27 |
| [#25587](https://github.com/sgl-project/sglang/issues/25587) | [Bug] [NPU] Hybrid-GDN MTP speculative decoding is not lossless on Asc | — | 2026-06-27 |
| [#27937](https://github.com/sgl-project/sglang/issues/27937) | [Failure Tracker] PR Test (AMD) | — | 2026-06-26 |
| [#23206](https://github.com/sgl-project/sglang/issues/23206) | [RFC] Sglang non-GPU process rust migration | — | 2026-06-26 |
| [#8715](https://github.com/sgl-project/sglang/issues/8715) | [Roadmap] MoE Refactor | high priority, collaboration | 2026-06-26 |
| [#29144](https://github.com/sgl-project/sglang/issues/29144) | [Bug] EAGLE/NextN speculative decoding + DP attention: collective dead | — | 2026-06-26 |
| [#29375](https://github.com/sgl-project/sglang/issues/29375) | fix: GLM-5.2 DSA backend crashes on AMD MI355X — .view() on non-contig | — | 2026-06-26 |
| [#22464](https://github.com/sgl-project/sglang/issues/22464) | [Parity with CUDA] FP8 & FP4 AMD Multi-Node PD Disagg Nightly Regressi | inactive | 2026-06-26 |
| [#29363](https://github.com/sgl-project/sglang/issues/29363) | [RFC] Cross-architecture model reload: `reload_model()` for architectu | — | 2026-06-26 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 71 |
| Multimodal | 38 |
| MoE / Expert Parallel | 31 |
| Other | 23 |
| Prefill / Decode Disaggregation | 23 |
| KV Cache / Memory | 21 |
| Quantization | 16 |
| Scheduler / Batching | 15 |
| Triton / Kernels | 14 |
| Models | 13 |
| Speculative Decoding | 13 |
| Docs / Examples | 10 |
| Tensor / Data Parallel | 9 |
| ROCm / AMD | 7 |
| CI / Build | 5 |
| Serving / API | 5 |
| Structured Output | 2 |

## Attention / FlashInfer  (71 commits)

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
- **2026-06-28** [`b9b860652e`](https://github.com/sgl-project/sglang/commit/b9b860652e) [#29576](https://github.com/sgl-project/sglang/pull/29576)
  Fix DSA indexer fusion bug causing excessive memory consumption. (#29576)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-06-28** [`6582fc1e5d`](https://github.com/sgl-project/sglang/commit/6582fc1e5d) [#29556](https://github.com/sgl-project/sglang/pull/29556)
  dflash: drop verify_done barrier; rely on scheduler WAR fallback (#29556)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/dflash_info_v2.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-06-28** [`593f5ba68f`](https://github.com/sgl-project/sglang/commit/593f5ba68f) [#29232](https://github.com/sgl-project/sglang/pull/29232)
  [Spec] Replace shared-infra dflash special-cases with capabilities (WAR barrier + seq_lens_cpu) (#29232)
  _Files: `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/dflash_info_v2.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-06-28** [`5747ed3b19`](https://github.com/sgl-project/sglang/commit/5747ed3b19) [#29543](https://github.com/sgl-project/sglang/pull/29543)
  Fix DP-attention SHM feature finalization race (#29543)
  _Files: `python/sglang/srt/managers/scheduler_components/request_receiver.py`_
- **2026-06-28** [`e6cbc8f5fe`](https://github.com/sgl-project/sglang/commit/e6cbc8f5fe) [#29460](https://github.com/sgl-project/sglang/pull/29460)
  Fix SWA cache loc slicing for all attention backends (#29460)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-06-28** [`4e6ce8e4ab`](https://github.com/sgl-project/sglang/commit/4e6ce8e4ab) [#29395](https://github.com/sgl-project/sglang/pull/29395)
  [Spec] Capture DFLASH draft greedy sampling inside the draft decode cuda graph (#29395)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-06-27** [`073de15053`](https://github.com/sgl-project/sglang/commit/073de15053) [#27705](https://github.com/sgl-project/sglang/pull/27705)
  Fuse the DSA (V3.2, GLM-5.x) indexer Q/K paths into single kernels (#27705)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v32/indexer_k.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/jit_kernel/dsv32/__init__.py`, `python/sglang/jit_kernel/dsv32/elementwise.py` _+9 more__
- **2026-06-27** [`e4253b39e2`](https://github.com/sgl-project/sglang/commit/e4253b39e2) [#27397](https://github.com/sgl-project/sglang/pull/27397)
  Support JIT fused A GEMM (MLA down projection) and support GLM-5 hidden size, SM120 (#27397)
  _Files: `python/sglang/jit_kernel/csrc/gemm/dsv3_fused_a_gemm.cuh`, `python/sglang/jit_kernel/cutedsl_dsv3_fused_a_gemm.py`, `python/sglang/jit_kernel/dsv3_fused_a_gemm.py`, `python/sglang/jit_kernel/fused_a_gemm.py` _+4 more__
- **2026-06-27** [`3306233961`](https://github.com/sgl-project/sglang/commit/3306233961) [#28624](https://github.com/sgl-project/sglang/pull/28624)
  [diffusion] optimize: optimize LTX2.3 CFG path (#28624)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/ltx_2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/ltx_2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/model_deployment_config.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py` _+7 more__
- **2026-06-27** [`9214b9338f`](https://github.com/sgl-project/sglang/commit/9214b9338f) [#29413](https://github.com/sgl-project/sglang/pull/29413)
  [DSA] Enable draft-extend CUDA graph for DeepSeek Sparse Attention (#29413)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-06-27** [`c36f166364`](https://github.com/sgl-project/sglang/commit/c36f166364) [#29487](https://github.com/sgl-project/sglang/pull/29487)
  [skill] Remove outdated llm-serving-auto-benchmark skill (#29487)
  _Files: `.claude/skills/llm-serving-auto-benchmark/SKILL.md`, `.claude/skills/llm-serving-auto-benchmark/configs/cookbook-llm/README.md`, `.claude/skills/llm-serving-auto-benchmark/configs/cookbook-llm/deepseek-math-v2.yaml`, `.claude/skills/llm-serving-auto-benchmark/configs/cookbook-llm/deepseek-r1-0528.yaml` _+56 more__
- **2026-06-27** [`09ca4fc96b`](https://github.com/sgl-project/sglang/commit/09ca4fc96b) [#29462](https://github.com/sgl-project/sglang/pull/29462)
  Skip FlashInfer FP8 autotune for MXFP8 quantized models (#29462)
  _Files: `python/sglang/srt/model_executor/runner/base_runner.py`_
- **2026-06-26** [`72812db138`](https://github.com/sgl-project/sglang/commit/72812db138) [#29423](https://github.com/sgl-project/sglang/pull/29423)
  Avoid dynamic Q quantization in trtllm_mha (#29423)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-06-26** [`267d165ad0`](https://github.com/sgl-project/sglang/commit/267d165ad0) [#29455](https://github.com/sgl-project/sglang/pull/29455)
  shm_broadcast: retry bind on EADDRINUSE (fix dp-attention port race) (#29455)
  _Files: `python/sglang/srt/distributed/device_communicators/shm_broadcast.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/utils/network.py`_
- **2026-06-26** [`ee77a7d330`](https://github.com/sgl-project/sglang/commit/ee77a7d330) [#29379](https://github.com/sgl-project/sglang/pull/29379)
  [Fix] DSA: size cudagraph page_table to req_to_token width (#29379)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`_
- **2026-06-26** [`8524678889`](https://github.com/sgl-project/sglang/commit/8524678889) [#29250](https://github.com/sgl-project/sglang/pull/29250)
  Fix MiniMax MSA fallback when fmha plan is unavailable (#29250)
  _Files: `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/msa.py`_
- **2026-06-26** [`f5708c3f91`](https://github.com/sgl-project/sglang/commit/f5708c3f91) [#29374](https://github.com/sgl-project/sglang/pull/29374)
  [NPU] Fix mllama cross-attention crash in ascend extend SDPA (#29374)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_torch_native_backend.py`_
- **2026-06-26** [`a10a24e9a7`](https://github.com/sgl-project/sglang/commit/a10a24e9a7) [#28451](https://github.com/sgl-project/sglang/pull/28451)
  [GDN][KDA] ReplaySSM buffered output-only decode for Linear Attention (#28451)
  _Files: `python/sglang/srt/configs/mamba_utils.py`, `python/sglang/srt/layers/attention/fla/bench_gdn_replayssm_decode.py`, `python/sglang/srt/layers/attention/fla/fused_recurrent_linear_replayssm.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` _+10 more__
- **2026-06-26** [`30ea4c0f4b`](https://github.com/sgl-project/sglang/commit/30ea4c0f4b) [#29067](https://github.com/sgl-project/sglang/pull/29067)
  build(sgl-kernel): bump FlashMLA pin + fix cccl include for CUDA 13 (#29067)
  _Files: `sgl-kernel/cmake/flashmla.cmake`_
- **2026-06-26** [`6c92f9f328`](https://github.com/sgl-project/sglang/commit/6c92f9f328) [#29356](https://github.com/sgl-project/sglang/pull/29356)
  fix(bench): pass DCP_RANK/DCP_WORLD_SIZE to set_mla_kv_buffer_kernel (#29356)
  _Files: `test/registered/jit/benchmark/bench_set_mla_kv_buffer.py`_
- **2026-06-25** [`623300a589`](https://github.com/sgl-project/sglang/commit/623300a589) [#29311](https://github.com/sgl-project/sglang/pull/29311)
  [MLX] Fix FutureMap relay unit test to use RelayPayload (#29311)
  _Files: `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`_
- **2026-06-25** [`1ba7c79761`](https://github.com/sgl-project/sglang/commit/1ba7c79761) [#29267](https://github.com/sgl-project/sglang/pull/29267)
  [CPU] add indices in chunk_gated_delta_rule  (#29267)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/models/qwen3_5.py` _+4 more__
- **2026-06-25** [`c8c6757bed`](https://github.com/sgl-project/sglang/commit/c8c6757bed) [#29345](https://github.com/sgl-project/sglang/pull/29345)
  test(dp-attn): drop --enable-torch-compile from TestDPAttentionDP2TP2 (#29345)
  _Files: `test/registered/dp_attn/test_dp_attention.py`_
- **2026-06-25** [`ea8f4e9f3f`](https://github.com/sgl-project/sglang/commit/ea8f4e9f3f) [#14194](https://github.com/sgl-project/sglang/pull/14194)
  [feature] implement dcp for deepseek_v2 (#14194)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/layers/attention/flashmla_backend.py` _+16 more__
- **2026-06-25** [`b7d3c3016d`](https://github.com/sgl-project/sglang/commit/b7d3c3016d) [#29103](https://github.com/sgl-project/sglang/pull/29103)
  [AMD] Feat/dsv4 aiter reduce scatter decode (#29103)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-06-25** [`e6efe10072`](https://github.com/sgl-project/sglang/commit/e6efe10072) [#29197](https://github.com/sgl-project/sglang/pull/29197)
  [AMD] Register 5 JIT kernel unit tests for AMD nightly CI (#29197)
  _Files: `test/registered/jit/deepseek_v4/test_c128_v2.py`, `test/registered/jit/deepseek_v4/test_c4_v2.py`, `test/registered/jit/diffusion/test_group_norm_silu.py`, `test/registered/jit/diffusion/test_qwen_image_modulation.py` _+1 more__
- **2026-06-25** [`ec12a28a87`](https://github.com/sgl-project/sglang/commit/ec12a28a87) [#28967](https://github.com/sgl-project/sglang/pull/28967)
  [AMD] Register 7 JIT kernel unit tests for AMD nightly CI (#28967)
  _Files: `test/registered/jit/minimax/test_minimax_decode_topk.py`, `test/registered/jit/minimax/test_minimax_store_kv_index.py`, `test/registered/jit/test_deepseek_v4_compress_state_runtime_shapes.py`, `test/registered/jit/test_fused_store_index_cache.py` _+3 more__
- **2026-06-25** [`9215da2515`](https://github.com/sgl-project/sglang/commit/9215da2515) [#28757](https://github.com/sgl-project/sglang/pull/28757)
  [AMD] [GLM5] skip redundant -inf pre-fill of HIP indexer MQA-logits (#28757)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `test/registered/amd/test_dsa_skip_logits_clean.py`_
- **2026-06-25** [`72cac88022`](https://github.com/sgl-project/sglang/commit/72cac88022) [#29105](https://github.com/sgl-project/sglang/pull/29105)
  [NPU] perf: precompute mamba conv-state track indices once per batch (#29105)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`_
- **2026-06-25** [`40439acd0a`](https://github.com/sgl-project/sglang/commit/40439acd0a) [#29233](https://github.com/sgl-project/sglang/pull/29233)
  Sync backend docs with #29063 (#29233)
  _Files: `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `python/sglang/srt/server_args.py`_
- **2026-06-25** [`8314247d9d`](https://github.com/sgl-project/sglang/commit/8314247d9d) [#29228](https://github.com/sgl-project/sglang/pull/29228)
  [Spec] Merge dflash triton kernels into a single `dflash.py` (#29228)
  _Files: `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/triton_ops/dflash.py`, `python/sglang/srt/speculative/triton_ops/dflash_prepare_block.py`_
- **2026-06-25** [`4e155ecc31`](https://github.com/sgl-project/sglang/commit/4e155ecc31) [#26724](https://github.com/sgl-project/sglang/pull/26724)
  [NPU] adaptation to support operator FA3 in deterministic inference on NPU. (#26724)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-06-25** [`c7734e6871`](https://github.com/sgl-project/sglang/commit/c7734e6871) [#29220](https://github.com/sgl-project/sglang/pull/29220)
  [Spec] Dissolve `EagleDraftInputV2Mixin` so spec-info dataclasses hold data only (#29220)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/model_executor/pool_configurator.py` _+11 more__
- **2026-06-25** [`5d4e63d49e`](https://github.com/sgl-project/sglang/commit/5d4e63d49e) [#29063](https://github.com/sgl-project/sglang/pull/29063)
  Sync the changes in #23402 (#29063)
  _Files: `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `test/registered/unit/layers/test_flashinfer_comm_fusion.py`_
- **2026-06-24** [`e26bceb81e`](https://github.com/sgl-project/sglang/commit/e26bceb81e) [#29077](https://github.com/sgl-project/sglang/pull/29077)
  [perf] simplify _apply_cuda_graph_metadata for draft extend in trtllm_mla backend (#29077)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-06-24** [`d3dd184e3e`](https://github.com/sgl-project/sglang/commit/d3dd184e3e) [#29118](https://github.com/sgl-project/sglang/pull/29118)
  [Spec] Fold DFlash verified_id into the shared bonus_tokens relay channel (#29118)
  _Files: `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/speculative/dflash_info_v2.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/triton_ops/dflash_prepare_block.py`_
- **2026-06-24** [`d5e9176f65`](https://github.com/sgl-project/sglang/commit/d5e9176f65) [#27053](https://github.com/sgl-project/sglang/pull/27053)
  [BCG][GLM5] perf: BCG support and prefill enhancements (#27053)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/attention/dsa_backend.py` _+3 more__
- **2026-06-24** [`e97cc339e3`](https://github.com/sgl-project/sglang/commit/e97cc339e3) [#28952](https://github.com/sgl-project/sglang/pull/28952)
  Add DeepSeek V4 Flash demo notebook (#28952)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/demo/deepseek_v4_flash.ipynb`_
- **2026-06-24** [`4992f7a108`](https://github.com/sgl-project/sglang/commit/4992f7a108) [#28144](https://github.com/sgl-project/sglang/pull/28144)
  Fix TRTLLM MHA FP8 KV cache scale handling (#28144)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-06-24** [`a707b2054d`](https://github.com/sgl-project/sglang/commit/a707b2054d) [#29141](https://github.com/sgl-project/sglang/pull/29141)
  [CI] Fix pre-commit failures in MLX backend tests (#29141)
  _Files: `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_runner_pool_contract.py`_
- **2026-06-24** [`c394f812d1`](https://github.com/sgl-project/sglang/commit/c394f812d1) [#28770](https://github.com/sgl-project/sglang/pull/28770)
  [MLX] Fix Apple Silicon server startup; align MLX tests with upstream (#28770)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_runner_pool_contract.py`_
- **2026-06-24** [`20b2817bdf`](https://github.com/sgl-project/sglang/commit/20b2817bdf) [#27833](https://github.com/sgl-project/sglang/pull/27833)
  [AMD] Enable BCG on ROCm + route aiter prefill via MHA during PCG/BCG capture for Kimi-2.5 (#27833)
  _Files: `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `test/registered/amd/test_kimi_k25_mxfp4_bcg_mi35x.py`_
- **2026-06-24** [`5338e44483`](https://github.com/sgl-project/sglang/commit/5338e44483) [#28646](https://github.com/sgl-project/sglang/pull/28646)
  [Intel GPU] fix triton-mla attention on XPU by limiting max_kv_splits to 8 which is default (#28646)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `test/registered/xpu/test_triton_attention_backend.py`_
- **2026-06-24** [`7454735be9`](https://github.com/sgl-project/sglang/commit/7454735be9) [#28975](https://github.com/sgl-project/sglang/pull/28975)
  [AMD] [GLM5] Add opt-in Triton fp8 sparse-MLA prefill kernel for gfx950 (#28975)
  _Files: `python/sglang/srt/layers/attention/dsa/triton_sparse_mla.py`, `python/sglang/srt/layers/attention/dsa_backend.py`_
- **2026-06-24** [`5e6d7c1615`](https://github.com/sgl-project/sglang/commit/5e6d7c1615) [#28455](https://github.com/sgl-project/sglang/pull/28455)
  [AMD] Fix DeepSeek-V4 fp8 KV path on gfx942 (e4m3fnuz) (#28455)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/store.cuh`, `python/sglang/jit_kernel/csrc/dsa/fused_store_index_cache.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/deepseek_v4/fp8_utils.cuh` _+4 more__
- **2026-06-24** [`b2c8f7a22e`](https://github.com/sgl-project/sglang/commit/b2c8f7a22e) [#25090](https://github.com/sgl-project/sglang/pull/25090)
  [AMD] Support triton backend decode context parallel for Qwen3.5 (#25090)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`, `python/sglang/srt/layers/attention/utils.py` _+11 more__
- **2026-06-24** [`9ef1830701`](https://github.com/sgl-project/sglang/commit/9ef1830701) [#29089](https://github.com/sgl-project/sglang/pull/29089)
  [Scheduler] Extract DFlash prefill refill into a standalone MinFreeSlotsDelayer (#29089)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/min_free_slots_delayer.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/server_args.py` _+2 more__
- **2026-06-23** [`6c5f466023`](https://github.com/sgl-project/sglang/commit/6c5f466023) [#28976](https://github.com/sgl-project/sglang/pull/28976)
  [server_args] Reland FA4 page_size auto-force for combined --attention-backend fa4 (#28976)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-06-23** [`31d71c47af`](https://github.com/sgl-project/sglang/commit/31d71c47af) [#28769](https://github.com/sgl-project/sglang/pull/28769)
  [Diffusion] Fix SANA VAE dtype and TurboWan backend selection (#28769)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/sana.py`, `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`_
- **2026-06-23** [`af9027f6c9`](https://github.com/sgl-project/sglang/commit/af9027f6c9) [#28938](https://github.com/sgl-project/sglang/pull/28938)
  [AMD] Improve performance of dsv4 in high concurrency (#28938)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/deepseek_v4_rope.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/models/deepseek_v2.py` _+1 more__
- **2026-06-23** [`7b1a20344c`](https://github.com/sgl-project/sglang/commit/7b1a20344c) [#28789](https://github.com/sgl-project/sglang/pull/28789)
  Re-enable SM90 FlashInfer allreduce fusion with safe backend defaults (#28789)
  _Files: `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/layers/test_flashinfer_comm_fusion.py`_
- **2026-06-23** [`219742c394`](https://github.com/sgl-project/sglang/commit/219742c394) [#28760](https://github.com/sgl-project/sglang/pull/28760)
  [diffusion] optimize: optimize realtime causal attention fastpath (#28760)
  _Files: `python/sglang/multimodal_gen/runtime/layers/kvcache/causal_attention_cache.py`, `python/sglang/multimodal_gen/runtime/models/dits/causal_wanvideo.py`, `python/sglang/multimodal_gen/runtime/models/dits/lingbot_world.py`, `python/sglang/multimodal_gen/test/unit/realtime/test_causal_denoising.py`_
- **2026-06-23** [`d70726a31a`](https://github.com/sgl-project/sglang/commit/d70726a31a) [#28972](https://github.com/sgl-project/sglang/pull/28972)
  Revert "[server_args] fix FA4 page_size auto-force for combined --attention-backend fa4" (#28972)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-06-22** [`6c212a5d6b`](https://github.com/sgl-project/sglang/commit/6c212a5d6b) [#28825](https://github.com/sgl-project/sglang/pull/28825)
  [server_args] fix FA4 page_size auto-force for combined --attention-backend fa4 (#28825)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-06-22** [`770d6b2825`](https://github.com/sgl-project/sglang/commit/770d6b2825) [#28854](https://github.com/sgl-project/sglang/pull/28854)
  [Spec] Add sync-free `fast_prefill_plan` for EAGLE draft-extend CUDA graph (#28854)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`, `test/registered/unit/spec/test_fast_prefill_plan.py`_
- **2026-06-22** [`99c18cceec`](https://github.com/sgl-project/sglang/commit/99c18cceec) [#28674](https://github.com/sgl-project/sglang/pull/28674)
  Sync server arguments and environment variables + update various documentation (#28674)
  _Files: `docs_new/docs.json`, `docs_new/docs/advanced_features/attention_backend.mdx`, `docs_new/docs/advanced_features/expert_parallelism.mdx`, `docs_new/docs/advanced_features/model_loading.mdx` _+3 more__
- **2026-06-22** [`6b2c730bf7`](https://github.com/sgl-project/sglang/commit/6b2c730bf7) [#28644](https://github.com/sgl-project/sglang/pull/28644)
  [codex] Fix DSA indexer in prefill piecewise CUDA graph (#28644)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-06-22** [`cee1caaf47`](https://github.com/sgl-project/sglang/commit/cee1caaf47) [#28941](https://github.com/sgl-project/sglang/pull/28941)
  [AMD] Fix nightly-8-gpu-mi35x-deepseek-v4-flash-rocm720 OOM issue (#28941)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`_
- **2026-06-22** [`04d952ea10`](https://github.com/sgl-project/sglang/commit/04d952ea10) [#28920](https://github.com/sgl-project/sglang/pull/28920)
  [AMD] deepseek-v4 clean env vars (#28920)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/dsv4/unified_kv_kernels/env_gate.py`, `python/sglang/srt/layers/attention/hip_flash_mla.py`, `python/sglang/srt/server_args.py` _+6 more__
- **2026-06-22** [`ead39d38fc`](https://github.com/sgl-project/sglang/commit/ead39d38fc) [#28888](https://github.com/sgl-project/sglang/pull/28888)
  [diffusion] refactor: refactor causal KV local head cache updates (#28888)
  _Files: `python/sglang/multimodal_gen/runtime/layers/kvcache/causal_attention_cache.py`, `python/sglang/multimodal_gen/runtime/models/dits/causal_wanvideo.py`, `python/sglang/multimodal_gen/runtime/models/dits/lingbot_world.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/causal_denoising.py` _+1 more__
- **2026-06-22** [`e2540188ce`](https://github.com/sgl-project/sglang/commit/e2540188ce) [#27243](https://github.com/sgl-project/sglang/pull/27243)
  [AMD] Clean up DeepSeek-R1-MXFP4 TP2/TP4 MLA GSM8K tests (#27243)
  _Files: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`_
- **2026-06-22** [`0642cd5020`](https://github.com/sgl-project/sglang/commit/0642cd5020) [#28759](https://github.com/sgl-project/sglang/pull/28759)
  (chore): bump tokenspeed_mla to 0.1.7 (#28759)
  _Files: `python/pyproject.toml`_
- **2026-06-22** [`be774d0acd`](https://github.com/sgl-project/sglang/commit/be774d0acd) [#28774](https://github.com/sgl-project/sglang/pull/28774)
  [docs][cookbook] Laguna-M.1 playground: add HiCache; refresh EP / DP-Attention notes (#28774)
  _Files: `docs_new/src/snippets/configs/poolside/laguna-m1.jsx`_
- **2026-06-22** [`0c065671c9`](https://github.com/sgl-project/sglang/commit/0c065671c9) [#28855](https://github.com/sgl-project/sglang/pull/28855)
  [Spec] Redo: split init_backends; account draft weights in --mem-fraction-static (#28855)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/model_runner.py` _+14 more__
- **2026-06-22** [`fd7874d11b`](https://github.com/sgl-project/sglang/commit/fd7874d11b) [#28495](https://github.com/sgl-project/sglang/pull/28495)
  [AMD] Register DP attention test (#28495)
  _Files: `test/registered/dp_attn/test_dp_attention.py`_

## Multimodal  (38 commits)

- **2026-06-28** [`4cb6d81bda`](https://github.com/sgl-project/sglang/commit/4cb6d81bda) [#29545](https://github.com/sgl-project/sglang/pull/29545)
  [diffusion] CI: make consistency GT probe robust to transient CDN failures (#29545)
  _Files: `python/sglang/multimodal_gen/test/test_utils.py`_
- **2026-06-28** [`97ddc66209`](https://github.com/sgl-project/sglang/commit/97ddc66209) [#29434](https://github.com/sgl-project/sglang/pull/29434)
  [diffusion] nightly: track SGLang-Diffusion only (#29434)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `scripts/ci/utils/diffusion/comparison_configs.json`, `scripts/ci/utils/diffusion/generate_diffusion_dashboard.py`, `scripts/ci/utils/diffusion/publish_comparison_results.py` _+1 more__
- **2026-06-28** [`643e1cc779`](https://github.com/sgl-project/sglang/commit/643e1cc779) [#29520](https://github.com/sgl-project/sglang/pull/29520)
  fix: fix prefill-aware SWA floor tracking (#29520)
  _Files: `docs_new/src/snippets/configs/baidu/unlimited-ocr.jsx`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/vlm/test_unlimited_ocr_server.py`_
- **2026-06-28** [`4a76699dfc`](https://github.com/sgl-project/sglang/commit/4a76699dfc) [#29514](https://github.com/sgl-project/sglang/pull/29514)
  [diffusion] fix: fix --warmup silently downgrading server-based warmup to request mode (#29514)
  _Files: `python/sglang/multimodal_gen/runtime/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-06-28** [`3d922a51fc`](https://github.com/sgl-project/sglang/commit/3d922a51fc) [#29537](https://github.com/sgl-project/sglang/pull/29537)
  test: remove multimodal piecewise CUDA graph gate test (#29537)
  _Files: `test/srt/test_multimodal_piecewise_cuda_graph_gate.py`_
- **2026-06-27** [`cfd911ad6e`](https://github.com/sgl-project/sglang/commit/cfd911ad6e) [#29507](https://github.com/sgl-project/sglang/pull/29507)
  docs: refine diffusion cookbook overview (#29507)
  _Files: `docs_new/cards/logos/ideogram.png`, `docs_new/cookbook/diffusion/LingBot-World/LingBot-World.mdx`, `docs_new/cookbook/diffusion/Wan/Wan2.1.mdx`, `docs_new/cookbook/diffusion/intro.mdx` _+1 more__
- **2026-06-27** [`91f9e7372d`](https://github.com/sgl-project/sglang/commit/91f9e7372d) [#28762](https://github.com/sgl-project/sglang/pull/28762)
  [diffusion] CI: refactor CI (#28762)
  _Files: `.github/workflows/nightly-test-musa.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test-musa.yml` _+42 more__
- **2026-06-27** [`495f13fa12`](https://github.com/sgl-project/sglang/commit/495f13fa12) [#29361](https://github.com/sgl-project/sglang/pull/29361)
  [KDA-Pilot] Add diffusion residual-gate CUDA fast path for LTX2 (#29361)
  _Files: `python/sglang/jit_kernel/csrc/diffusion/norm_scale_shift.cuh`, `python/sglang/jit_kernel/csrc/diffusion/residual_gate_add.cuh`, `python/sglang/jit_kernel/diffusion/residual_gate_add.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py` _+2 more__
- **2026-06-26** [`18b0e5757e`](https://github.com/sgl-project/sglang/commit/18b0e5757e) [#29390](https://github.com/sgl-project/sglang/pull/29390)
  [Diffusion] Fuse LTX2 Ada values (#29390)
  _Files: `python/sglang/jit_kernel/diffusion/triton/ltx2_ada_values.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `test/registered/jit/diffusion/test_ltx2_ada_values.py`_
- **2026-06-26** [`b91348071e`](https://github.com/sgl-project/sglang/commit/b91348071e) [#29147](https://github.com/sgl-project/sglang/pull/29147)
  [diffusion] optimize: shard qwen text embed in sp  (#29147)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`_
- **2026-06-26** [`aeb4e98108`](https://github.com/sgl-project/sglang/commit/aeb4e98108) [#27420](https://github.com/sgl-project/sglang/pull/27420)
  [diffusion] model: support JoyEcho multi-shot A/V generation support (#27420)
  _Files: `docs_new/cookbook/diffusion/JoyEcho/JoyEcho.mdx`, `docs_new/docs.json`, `python/sglang/multimodal_gen/configs/models/dits/joy_echo.py`, `python/sglang/multimodal_gen/configs/models/vaes/ltx_video.py` _+16 more__
- **2026-06-26** [`5996b54bd3`](https://github.com/sgl-project/sglang/commit/5996b54bd3) [#29281](https://github.com/sgl-project/sglang/pull/29281)
  [KDA-Pilot] Add diffusion causal Conv3D cat-pad CUDA fast path for Cosmos3 (#29281)
  _Files: `python/sglang/jit_kernel/csrc/diffusion/causal_conv3d_cat_pad.cuh`, `python/sglang/jit_kernel/diffusion/causal_conv3d_cat_pad.py`, `python/sglang/multimodal_gen/runtime/layers/parallel_conv.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py` _+2 more__
- **2026-06-25** [`38e857f423`](https://github.com/sgl-project/sglang/commit/38e857f423) [#29236](https://github.com/sgl-project/sglang/pull/29236)
  [MUSA][diffusion] Bump torchada version to 0.1.68 (#29236)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject_other.toml`, `sgl-kernel/pyproject_musa.toml`_
- **2026-06-25** [`890b38c211`](https://github.com/sgl-project/sglang/commit/890b38c211) [#29302](https://github.com/sgl-project/sglang/pull/29302)
  [diffusion] doc: fix diffusion docs and cookbook drift (#29302)
  _Files: `docs_new/cookbook/diffusion/FLUX/FLUX.mdx`, `docs_new/cookbook/diffusion/Krea/Krea-2.mdx`, `docs_new/cookbook/diffusion/MOVA/MOVA.mdx`, `docs_new/cookbook/diffusion/Qwen-Image/Qwen-Image-Edit.mdx` _+8 more__
- **2026-06-25** [`bc150173b2`](https://github.com/sgl-project/sglang/commit/bc150173b2) [#29234](https://github.com/sgl-project/sglang/pull/29234)
  [AMD] Fix stage-b-test-1-gpu-small-amd-nondeterministic timeout after VLM model swap (#29234)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`_
- **2026-06-25** [`7c9804ef21`](https://github.com/sgl-project/sglang/commit/7c9804ef21) [#29253](https://github.com/sgl-project/sglang/pull/29253)
  Add MiMo V2.5 Blackwell vision FA4 recipe (#29253)
  _Files: `docs_new/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx`, `docs_new/src/snippets/autoregressive/mimo-v25-deployment.jsx`_
- **2026-06-25** [`d1cf09d4d4`](https://github.com/sgl-project/sglang/commit/d1cf09d4d4) [#29219](https://github.com/sgl-project/sglang/pull/29219)
  [AMD-miles] Add a ROCm 7.0 MI35x miles nightly image (#29219)
  _Files: `.github/workflows/release-docker-amd-miles-rocm700-nightly.yml`_
- **2026-06-25** [`c268a7edf5`](https://github.com/sgl-project/sglang/commit/c268a7edf5) [#27700](https://github.com/sgl-project/sglang/pull/27700)
  [Bugfix] Fix inverted PP-disable condition for diffusion LLM inference (#27700)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-25** [`ae6f787637`](https://github.com/sgl-project/sglang/commit/ae6f787637) [#22659](https://github.com/sgl-project/sglang/pull/22659)
  [diffusion] rl: add sleep/wake support for diffusion engine (#22659)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/post_training/io_struct.py`, `python/sglang/multimodal_gen/runtime/entrypoints/post_training/weights_api.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/memory_occupation_controller.py` _+1 more__
- **2026-06-24** [`dd4caf9459`](https://github.com/sgl-project/sglang/commit/dd4caf9459) [#29139](https://github.com/sgl-project/sglang/pull/29139)
  [Docs] fix SGLang-diffusion installation links (#29139)
  _Files: `docs_new/cookbook/diffusion/FLUX/FLUX.mdx`, `docs_new/cookbook/diffusion/Krea/Krea-2.mdx`, `docs_new/cookbook/diffusion/MOVA/MOVA.mdx`, `docs_new/cookbook/diffusion/Qwen-Image/Qwen-Image-Edit.mdx` _+2 more__
- **2026-06-24** [`4a4f063b79`](https://github.com/sgl-project/sglang/commit/4a4f063b79) [#29041](https://github.com/sgl-project/sglang/pull/29041)
  [diffusion] fix: paint multiview vae must follow unit dtype (#29041)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/hunyuan3d/paint.py`_
- **2026-06-24** [`0fc815aa2c`](https://github.com/sgl-project/sglang/commit/0fc815aa2c) [#29095](https://github.com/sgl-project/sglang/pull/29095)
  [CI] Temporarily disable openbmb MiniCPM tests (#29095)
  _Files: `test/registered/eval/test_vlms_mmmu_eval.py`, `test/registered/models/test_vlm_models.py`, `test/registered/vlm/test_vision_openai_server_a.py`, `test/registered/vlm/test_vlm_input_format.py`_
- **2026-06-24** [`00eac7ec9b`](https://github.com/sgl-project/sglang/commit/00eac7ec9b) [#28503](https://github.com/sgl-project/sglang/pull/28503)
  [diffusion] fix: disable proxy env in warmup health probe (#28503)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`_
- **2026-06-24** [`26e1d4d847`](https://github.com/sgl-project/sglang/commit/26e1d4d847) [#27392](https://github.com/sgl-project/sglang/pull/27392)
  [KDA-Pilot] Add B200 diffusion norm-scale-shift CUDA fast path for Qwen-Image (#27392)
  _Files: `python/sglang/jit_kernel/csrc/diffusion/norm_scale_shift.cuh`, `python/sglang/jit_kernel/diffusion/cutedsl/scale_residual_norm_scale_shift.py`, `python/sglang/jit_kernel/diffusion/norm_scale_shift_native.py`_
- **2026-06-24** [`0df796473b`](https://github.com/sgl-project/sglang/commit/0df796473b) [#28940](https://github.com/sgl-project/sglang/pull/28940)
  [VLM] Qwen3-VL / Moss-VL ViT preprocessing optimizations (#28940)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/moss_vl.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/processors/base_processor.py` _+2 more__
- **2026-06-24** [`534ac98eb2`](https://github.com/sgl-project/sglang/commit/534ac98eb2) [#28780](https://github.com/sgl-project/sglang/pull/28780)
  [codex] Optimize DMD Wan auto residency on high-memory GPUs (#28780)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py`, `python/sglang/multimodal_gen/registry.py`, `python/sglang/multimodal_gen/runtime/server_args_auto_tune.py`_
- **2026-06-24** [`5beddc8afc`](https://github.com/sgl-project/sglang/commit/5beddc8afc) [#29052](https://github.com/sgl-project/sglang/pull/29052)
  [Diffusion] Add Krea 2 support (#29052)
  _Files: `python/sglang/multimodal_gen/apps/webui/main.py`, `python/sglang/multimodal_gen/configs/models/dits/krea2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/krea2.py`, `python/sglang/multimodal_gen/configs/sample/krea2.py` _+4 more__
- **2026-06-23** [`83d32fbc2f`](https://github.com/sgl-project/sglang/commit/83d32fbc2f) [#29056](https://github.com/sgl-project/sglang/pull/29056)
  remove lora section (#29056)
  _Files: `docs_new/cookbook/diffusion/Krea/Krea-2.mdx`_
- **2026-06-23** [`b5e0965b07`](https://github.com/sgl-project/sglang/commit/b5e0965b07) [#29051](https://github.com/sgl-project/sglang/pull/29051)
  [Diffusion][Cookbook] Add Krea-2 cookbook (#29051)
  _Files: `docs_new/cards/logos/krea.png`, `docs_new/cookbook/diffusion/Krea/Krea-2.mdx`, `docs_new/cookbook/diffusion/intro.mdx`, `docs_new/docs.json`_
- **2026-06-23** [`12b08e620b`](https://github.com/sgl-project/sglang/commit/12b08e620b) [#29011](https://github.com/sgl-project/sglang/pull/29011)
  [Diffusion] [NPU] enable Helios on npu (#29011)
  _Files: `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/schedulers/scheduling_helios.py`_
- **2026-06-23** [`c67d338637`](https://github.com/sgl-project/sglang/commit/c67d338637) [#28266](https://github.com/sgl-project/sglang/pull/28266)
  [Diffusion] enable cache-dit for ERNIE-Image model (#28266)
  _Files: `python/sglang/multimodal_gen/runtime/cache/cache_dit_integration.py`, `python/sglang/multimodal_gen/test/unit/test_cache_dit_integration.py`_
- **2026-06-23** [`52a90c9a36`](https://github.com/sgl-project/sglang/commit/52a90c9a36) [#28777](https://github.com/sgl-project/sglang/pull/28777)
  docs(minimax-m3): use published AMD ROCm images (#28777)
  _Files: `docs_new/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`_
- **2026-06-22** [`4f60378ff5`](https://github.com/sgl-project/sglang/commit/4f60378ff5) [#28647](https://github.com/sgl-project/sglang/pull/28647)
  Fix Kimi-VL GPU image preprocessing crash on non-RGB images (#28647)
  _Files: `python/sglang/srt/multimodal/processors/kimi_k25.py`_
- **2026-06-22** [`669be5448b`](https://github.com/sgl-project/sglang/commit/669be5448b) [#28686](https://github.com/sgl-project/sglang/pull/28686)
  [cuda graph] Enable prefill piecewise CUDA graph for Cohere2Vision (text path) (#28686)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/server_args.py`, `test/srt/test_multimodal_piecewise_cuda_graph_gate.py`_
- **2026-06-22** [`bbe8b7dd8a`](https://github.com/sgl-project/sglang/commit/bbe8b7dd8a) [#28781](https://github.com/sgl-project/sglang/pull/28781)
  [diffusion] CI: restore Hunyuan3D-2 image-to-3D (#28781)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/hunyuan3d/shape.py`, `python/sglang/multimodal_gen/test/server/perf_baselines.json`, `python/sglang/multimodal_gen/test/server/test_server_common.py`, `python/sglang/multimodal_gen/test/server/test_server_utils.py` _+1 more__
- **2026-06-22** [`4923bb93ae`](https://github.com/sgl-project/sglang/commit/4923bb93ae) [#28913](https://github.com/sgl-project/sglang/pull/28913)
  [diffusion] CI: fix turbo_wan/flux invisible CI cases (#28913)
  _Files: `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/test_utils.py`_
- **2026-06-22** [`0c9e775f2c`](https://github.com/sgl-project/sglang/commit/0c9e775f2c) [#28733](https://github.com/sgl-project/sglang/pull/28733)
  [Diffusion] Fix FastWan2.1 default 480p resolution (#28733)
  _Files: `python/sglang/multimodal_gen/configs/sample/wan.py`, `python/sglang/multimodal_gen/test/unit/test_sampling_params.py`_
- **2026-06-22** [`2b2cd21783`](https://github.com/sgl-project/sglang/commit/2b2cd21783) [#28834](https://github.com/sgl-project/sglang/pull/28834)
  [diffusion] fix: reject cache-dit with fsdp (#28834)
  _Files: `python/sglang/multimodal_gen/runtime/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_

## MoE / Expert Parallel  (31 commits)

- **2026-06-29** [`93926b9a95`](https://github.com/sgl-project/sglang/commit/93926b9a95) [#29640](https://github.com/sgl-project/sglang/pull/29640)
  Add Qwen3 MoE tests for PP compatibility with CP and DP (#29640)
  _Files: `test/registered/pp/test_pp_parallel_compat.py`_
- **2026-06-29** [`f85cc94d82`](https://github.com/sgl-project/sglang/commit/f85cc94d82) [#29505](https://github.com/sgl-project/sglang/pull/29505)
  [NPU] Qwen3-VL-30B use split_qkv_rmsnorm_rope for extend (#29505)
  _Files: `python/sglang/srt/models/qwen3_moe.py`_
- **2026-06-28** [`828411e6f1`](https://github.com/sgl-project/sglang/commit/828411e6f1) [#29461](https://github.com/sgl-project/sglang/pull/29461)
  Fix FlashInfer A2A dispatcher during CUDA graph capture (#29461)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`_
- **2026-06-27** [`1589603114`](https://github.com/sgl-project/sglang/commit/1589603114) [#29186](https://github.com/sgl-project/sglang/pull/29186)
  model: support baidu unlimited-ocr (#29186)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `docs_new/cards/logos/baidu.svg`, `docs_new/cookbook/autoregressive/Baidu/Unlimited-OCR.mdx`, `docs_new/cookbook/autoregressive/intro.mdx` _+28 more__
- **2026-06-27** [`43435a2f8e`](https://github.com/sgl-project/sglang/commit/43435a2f8e) [#29097](https://github.com/sgl-project/sglang/pull/29097)
  [mori] Add a combine-kwargs hook and use_external_inp_buf plumbing (#29097)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`_
- **2026-06-26** [`5eebb4b2e8`](https://github.com/sgl-project/sglang/commit/5eebb4b2e8) [#29377](https://github.com/sgl-project/sglang/pull/29377)
  [AMD] Fix fused append+remap DeepEP equivalence test on aiter path (#29377)
  _Files: `test/registered/moe/test_fused_append_remap_deepep.py`_
- **2026-06-26** [`7b02eab7a6`](https://github.com/sgl-project/sglang/commit/7b02eab7a6) [#29452](https://github.com/sgl-project/sglang/pull/29452)
  Revert "[DeepSeek V3] Run routed experts on main stream in dual-stream MoE" (#29452)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-06-26** [`999199f9ff`](https://github.com/sgl-project/sglang/commit/999199f9ff) [#29142](https://github.com/sgl-project/sglang/pull/29142)
  [DeepSeek V3] Run routed experts on main stream in dual-stream MoE (#29142)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-06-26** [`4ce1c180bd`](https://github.com/sgl-project/sglang/commit/4ce1c180bd) [#29270](https://github.com/sgl-project/sglang/pull/29270)
  [sgl-kernel/cpu]: fix arm64 w8a8 moe kernel signature (#29270)
  _Files: `sgl-kernel/csrc/cpu/aarch64/moe.cpp`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`, `test/registered/cpu/arm64/test_moe.py`_
- **2026-06-25** [`212c30d008`](https://github.com/sgl-project/sglang/commit/212c30d008) [#28211](https://github.com/sgl-project/sglang/pull/28211)
  [MoE Refactor] Centralize FlashInfer CUTLASS MoE runner (#28211)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutlass.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_mxfp4.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py` _+4 more__
- **2026-06-25** [`9495737d82`](https://github.com/sgl-project/sglang/commit/9495737d82) [#29308](https://github.com/sgl-project/sglang/pull/29308)
  Fix CI broken by #28450 (#29308)
  _Files: `test/registered/moe/test_topk_padded_region.py`_
- **2026-06-25** [`3d3a7ec031`](https://github.com/sgl-project/sglang/commit/3d3a7ec031) [#28237](https://github.com/sgl-project/sglang/pull/28237)
  [AMD] fix(moe): correct fused shared-expert scaling on aiter/DeepEP path (mori all-to-all) (#28237)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/unit/layers/moe/test_fused_shared_expert_scaling.py`_
- **2026-06-25** [`de2d01c8da`](https://github.com/sgl-project/sglang/commit/de2d01c8da) [#28450](https://github.com/sgl-project/sglang/pull/28450)
  [AMD] Fuse shared-expert append + DeepEP remap into one Triton kernel (#28450)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/moe/test_fused_append_remap_deepep.py`_
- **2026-06-25** [`9fd6d0ec99`](https://github.com/sgl-project/sglang/commit/9fd6d0ec99) [#28953](https://github.com/sgl-project/sglang/pull/28953)
  [LoRA] BF16 support + EP cuda-graph crash fix for experimental_sgl_trtllm MoE-LoRA (#28953)
  _Files: `python/sglang/jit_kernel/trtllm_lora_temp/__init__.py`, `python/sglang/jit_kernel/trtllm_lora_temp/core.py`, `python/sglang/jit_kernel/trtllm_lora_temp/data/csrc/fused_moe/trtllm_backend/trtllm_fused_moe_dev_kernel.cu`, `python/sglang/jit_kernel/trtllm_lora_temp/data/csrc/trtllm_fused_moe_kernel_launcher.cu` _+6 more__
- **2026-06-25** [`8b7a1e908a`](https://github.com/sgl-project/sglang/commit/8b7a1e908a) [#28347](https://github.com/sgl-project/sglang/pull/28347)
  Revert Gemma4 modelopt fp4 MoE backend change (#28347)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-25** [`67b2a9ed0c`](https://github.com/sgl-project/sglang/commit/67b2a9ed0c) [#29042](https://github.com/sgl-project/sglang/pull/29042)
  [NPU] Fix the DeepSeek-V2-Coder model accuracy issue (#29042)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/llada2.py`_
- **2026-06-24** [`f82addd4a8`](https://github.com/sgl-project/sglang/commit/f82addd4a8) [#27939](https://github.com/sgl-project/sglang/pull/27939)
  Support online MXFP8 quantization for ungated MoE (#27939)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-06-24** [`e4bf0043fe`](https://github.com/sgl-project/sglang/commit/e4bf0043fe) [#26980](https://github.com/sgl-project/sglang/pull/26980)
  [fix] Skip routed expert capture for draft model under spec v2 (#26980)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/model_executor/model_runner.py` _+1 more__
- **2026-06-24** [`8e1988b746`](https://github.com/sgl-project/sglang/commit/8e1988b746) [#29075](https://github.com/sgl-project/sglang/pull/29075)
  [Perf] Overlap result D2H copy with the next forward step (#29075)
  _Files: `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/utils.py`, `python/sglang/srt/state_capturer/base.py`_
- **2026-06-24** [`e04ed05193`](https://github.com/sgl-project/sglang/commit/e04ed05193) [#28623](https://github.com/sgl-project/sglang/pull/28623)
  [CI] reduce CPU CI scope with base-c suite (#28623)
  _Files: `test/registered/bench_fn/test_benchmark_datasets_api.py`, `test/registered/debug_utils/comparator/aligner/entrypoint/test_executor.py`, `test/registered/debug_utils/comparator/aligner/entrypoint/test_planner.py`, `test/registered/debug_utils/comparator/aligner/reorderer/test_executor.py` _+87 more__
- **2026-06-23** [`93015a9e6b`](https://github.com/sgl-project/sglang/commit/93015a9e6b) [#29069](https://github.com/sgl-project/sglang/pull/29069)
  fix(runner): autotune flashinfer MoE on a decode-shaped buffer (#29069)
  _Files: `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-06-23** [`fc27ce0666`](https://github.com/sgl-project/sglang/commit/fc27ce0666) [#25665](https://github.com/sgl-project/sglang/pull/25665)
  Add GB10 FP8 fused MoE Triton config (#25665)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=128,N=768,device_name=NVIDIA_GB10,dtype=fp8_w8a8.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe_triton_config.py`_
- **2026-06-23** [`cedb43d522`](https://github.com/sgl-project/sglang/commit/cedb43d522) [#28942](https://github.com/sgl-project/sglang/pull/28942)
  [DeepEP] Gate DeepEP MNNVL on fabric support (#28942)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`_
- **2026-06-23** [`e0dc8b7137`](https://github.com/sgl-project/sglang/commit/e0dc8b7137) [#28084](https://github.com/sgl-project/sglang/pull/28084)
  [AMD] Fuse topk padded-token masking into a single Triton kernel (#28084)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/moe/test_topk_padded_region.py`_
- **2026-06-23** [`e63b57da0b`](https://github.com/sgl-project/sglang/commit/e63b57da0b) [#28292](https://github.com/sgl-project/sglang/pull/28292)
  [Fix] model init / XPU / transformers-v5 / bench-image fixes (#28292)
  _Files: `python/sglang/benchmark/datasets/image.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/models/afmoe.py`, `python/sglang/srt/models/baichuan.py` _+6 more__
- **2026-06-23** [`ba9d5aed98`](https://github.com/sgl-project/sglang/commit/ba9d5aed98) [#28746](https://github.com/sgl-project/sglang/pull/28746)
  Fix nightly CI test for Kimi K2.5 INT4 + H200 (#28746)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`_
- **2026-06-22** [`7c23d2255a`](https://github.com/sgl-project/sglang/commit/7c23d2255a) [#28712](https://github.com/sgl-project/sglang/pull/28712)
  [minimax-m3] Split 1/4: sparse attention ops + JIT kernels + config foundation (#28712)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `docker/rocm.Dockerfile`, `python/sglang/jit_kernel/csrc/minimax/fused_gemma_qknorm_rope.cuh` _+47 more__
- **2026-06-22** [`8dc27f6326`](https://github.com/sgl-project/sglang/commit/8dc27f6326) [#28689](https://github.com/sgl-project/sglang/pull/28689)
  [MoE] dedup triton_kernels backend quant-arg asserts and fill weight dtype guard (#28689)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/triton_kernels_moe.py`_
- **2026-06-22** [`b43bd6824f`](https://github.com/sgl-project/sglang/commit/b43bd6824f) [#28786](https://github.com/sgl-project/sglang/pull/28786)
  [B300] Enable FlashInfer allreduce for Qwen3-VL MoE (#28786)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-22** [`c0bb04b67f`](https://github.com/sgl-project/sglang/commit/c0bb04b67f) [#25820](https://github.com/sgl-project/sglang/pull/25820)
  [NVIDIA] Support NVFP4 MoE for DeepSeek-V4 (#25820)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` _+6 more__
- **2026-06-22** [`6779ca8d7f`](https://github.com/sgl-project/sglang/commit/6779ca8d7f) [#28619](https://github.com/sgl-project/sglang/pull/28619)
  Fix Qwen MoE precision issue with PP and all-reduce fusion (#28619)
  _Files: `python/sglang/srt/models/qwen2_moe.py`_

## Other  (23 commits)

- **2026-06-29** [`bb7d3440b5`](https://github.com/sgl-project/sglang/commit/bb7d3440b5) [#29146](https://github.com/sgl-project/sglang/pull/29146)
  bugfix revise interface get cpu copy for npu mem pool to align with gpu (#29146)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-06-29** [`cd91dd0757`](https://github.com/sgl-project/sglang/commit/cd91dd0757) [#29623](https://github.com/sgl-project/sglang/pull/29623)
  fix test_weight_checker_comparator assertion and ue8m0 scale unpack (#29623)
  _Files: `python/sglang/srt/utils/weight_checker_comparator.py`, `test/registered/unit/utils/test_weight_checker_comparator.py`_
- **2026-06-29** [`d5abafcc1c`](https://github.com/sgl-project/sglang/commit/d5abafcc1c) [#28308](https://github.com/sgl-project/sglang/pull/28308)
  [Intel GPU] add pytorch profiling support for XPU in bench offline throughput and enhance num steps (#28308)
  _Files: `python/sglang/benchmark/offline_throughput.py`_
- **2026-06-28** [`ad30a9958e`](https://github.com/sgl-project/sglang/commit/ad30a9958e) [#29229](https://github.com/sgl-project/sglang/pull/29229)
  Fix dummy weight init for tensor subclasses (#29229)
  _Files: `python/sglang/srt/model_loader/weight_utils.py`_
- **2026-06-27** [`19abebcc6a`](https://github.com/sgl-project/sglang/commit/19abebcc6a) [#29096](https://github.com/sgl-project/sglang/pull/29096)
  [server_args] Make MoRI per-rank dispatch-token requirement overridable (#29096)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-26** [`73741f7074`](https://github.com/sgl-project/sglang/commit/73741f7074) [#29454](https://github.com/sgl-project/sglang/pull/29454)
  Bypass legacy GLM DSA layer types validation (#29454)
  _Files: `python/sglang/srt/utils/hf_transformers/config.py`, `python/sglang/srt/utils/hf_transformers/tokenizer.py`_
- **2026-06-26** [`b6ebdcc92e`](https://github.com/sgl-project/sglang/commit/b6ebdcc92e) [#29348](https://github.com/sgl-project/sglang/pull/29348)
  [test] Split perf table out of fwd occupancy kit report (#29348)
  _Files: `python/sglang/test/kits/fwd_occupancy_kit.py`_
- **2026-06-25** [`65f31acc6c`](https://github.com/sgl-project/sglang/commit/65f31acc6c) [#29341](https://github.com/sgl-project/sglang/pull/29341)
  Add yueming-yuan to CI_PERMISSIONS.json (#29341)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-06-25** [`32bae911f6`](https://github.com/sgl-project/sglang/commit/32bae911f6) [#28899](https://github.com/sgl-project/sglang/pull/28899)
  Add CI permission for jiayisunx (#28899)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-06-25** [`d717e926c1`](https://github.com/sgl-project/sglang/commit/d717e926c1) [#28894](https://github.com/sgl-project/sglang/pull/28894)
  fix(runner): prevent eager token buffer under-allocation (#28894)
  _Files: `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-06-25** [`9305d10099`](https://github.com/sgl-project/sglang/commit/9305d10099) [#28872](https://github.com/sgl-project/sglang/pull/28872)
  [NPU] adapt_fused_rope_qk_mqa_optimize (#28872)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`_
- **2026-06-24** [`fd87a85388`](https://github.com/sgl-project/sglang/commit/fd87a85388) [#29198](https://github.com/sgl-project/sglang/pull/29198)
  Convert SamplingParams to msgspec Struct (#29198)
  _Files: `python/sglang/srt/sampling/sampling_params.py`, `scripts/ci/utils/compute_partitions.py`, `test/registered/unit/sampling/test_sampling_params.py`_
- **2026-06-24** [`d6aacd2801`](https://github.com/sgl-project/sglang/commit/d6aacd2801) [#29121](https://github.com/sgl-project/sglang/pull/29121)
  Handle input-embed-only batches in eager runner (#29121)
  _Files: `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-06-24** [`7430c56b20`](https://github.com/sgl-project/sglang/commit/7430c56b20) [#29004](https://github.com/sgl-project/sglang/pull/29004)
  [Misc] Use logger instead of print() in utils/common.py (#29004)
  _Files: `python/sglang/srt/utils/common.py`, `test/registered/unit/utils/test_common.py`_
- **2026-06-24** [`10e0bcd622`](https://github.com/sgl-project/sglang/commit/10e0bcd622) [#29140](https://github.com/sgl-project/sglang/pull/29140)
  [NPU] fix dcp break (#29140)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-06-24** [`52b89c4948`](https://github.com/sgl-project/sglang/commit/52b89c4948) [#28997](https://github.com/sgl-project/sglang/pull/28997)
  [misc] Add bench_serving compatibility shim (#28997)
  _Files: `python/sglang/bench_offline_throughput.py`, `python/sglang/bench_one_batch.py`, `python/sglang/bench_one_batch_server.py`, `python/sglang/bench_serving.py` _+1 more__
- **2026-06-24** [`f76c6c95be`](https://github.com/sgl-project/sglang/commit/f76c6c95be) [#29085](https://github.com/sgl-project/sglang/pull/29085)
  [misc] Add sglang.bench_offline_throughput deprecation shim (#29085)
  _Files: `python/sglang/bench_offline_throughput.py`, `python/sglang/bench_one_batch.py`, `python/sglang/benchmark/offline_throughput.py`_
- **2026-06-24** [`b448b08401`](https://github.com/sgl-project/sglang/commit/b448b08401) [#28747](https://github.com/sgl-project/sglang/pull/28747)
  [misc] Move bench_offline_throughput into sglang/benchmark/ with a back-compat shim (#28747)
  _Files: `python/sglang/benchmark/offline_throughput.py`, `python/sglang/test/test_utils.py`, `test/manual/perf/test_bench_one_batch_1gpu.py`, `test/registered/core/test_srt_engine.py`_
- **2026-06-23** [`11e7c9e0e6`](https://github.com/sgl-project/sglang/commit/11e7c9e0e6) [#29082](https://github.com/sgl-project/sglang/pull/29082)
  [misc] Add sglang.bench_one_batch deprecation shim (#29082)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/benchmark/one_batch.py`_
- **2026-06-23** [`c864c8d9c2`](https://github.com/sgl-project/sglang/commit/c864c8d9c2) [#28687](https://github.com/sgl-project/sglang/pull/28687)
  [misc] Move bench_one_batch into sglang/benchmark/ with a back-compat shim (#28687)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/test/test_utils.py`, `test/manual/test_forward_split_prefill.py`_
- **2026-06-23** [`fc0d8fa262`](https://github.com/sgl-project/sglang/commit/fc0d8fa262) [#28990](https://github.com/sgl-project/sglang/pull/28990)
  [Lint] fix main's lint (#28990)
- **2026-06-22** [`b28e990161`](https://github.com/sgl-project/sglang/commit/b28e990161) [#28919](https://github.com/sgl-project/sglang/pull/28919)
  Migrate all ServerArgs fields to Annotated style, reduce add_cli_args by ~2400 lines (#28919)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/test_server_args_cli_metadata.py`, `test/registered/unit/test_server_args_migration.py`_
- **2026-06-22** [`886b96621d`](https://github.com/sgl-project/sglang/commit/886b96621d) [#28830](https://github.com/sgl-project/sglang/pull/28830)
  Migrate more server args to annotated style (#28830)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/test_server_args_cli_metadata.py`_

## Prefill / Decode Disaggregation  (23 commits)

- **2026-06-29** [`3b1b512a9a`](https://github.com/sgl-project/sglang/commit/3b1b512a9a) [#29570](https://github.com/sgl-project/sglang/pull/29570)
  Fix disaggregation receiver ZMQ cleanup (#29570)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`_
- **2026-06-28** [`ddc389cf09`](https://github.com/sgl-project/sglang/commit/ddc389cf09) [#28714](https://github.com/sgl-project/sglang/pull/28714)
  [minimax-m3] Split 3/4: disagg K-only index-K transfer (#28714)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py` _+3 more__
- **2026-06-27** [`b030b1a5f3`](https://github.com/sgl-project/sglang/commit/b030b1a5f3) [#27563](https://github.com/sgl-project/sglang/pull/27563)
  hisparse: support NIXL DRAM KV destinations for HiSparse (#27563)
  _Files: `docs_new/docs/advanced_features/hisparse_guide.mdx`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/nixl/conn.py` _+8 more__
- **2026-06-26** [`9c3227b689`](https://github.com/sgl-project/sglang/commit/9c3227b689) [#29459](https://github.com/sgl-project/sglang/pull/29459)
  Fix IPv6 wildcard bootstrap address resolution in disagg (#29459)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `test/registered/unit/disaggregation/test_register_to_bootstrap.py`_
- **2026-06-26** [`be1930133a`](https://github.com/sgl-project/sglang/commit/be1930133a) [#28688](https://github.com/sgl-project/sglang/pull/28688)
  Convert IPC dataclasses to msgspec.Struct with opt-in msgpack transport (#28688)
  _Files: `python/sglang/srt/debug_utils/dumper.py`, `python/sglang/srt/disaggregation/encode_grpc_server.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/entrypoints/engine.py` _+21 more__
- **2026-06-26** [`413aeac0c9`](https://github.com/sgl-project/sglang/commit/413aeac0c9) [#29084](https://github.com/sgl-project/sglang/pull/29084)
  [AMD][DI][CI] 1/N: MI355X disaggregation nightly benchmark (#29084)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`, `scripts/ci/slurm/generate_matrix.py`, `scripts/ci/slurm/launch_mi355x.sh`, `scripts/ci/slurm/nightly-configs.yaml` _+6 more__
- **2026-06-26** [`781537b61d`](https://github.com/sgl-project/sglang/commit/781537b61d) [#27433](https://github.com/sgl-project/sglang/pull/27433)
  [NPU] Nightly CI refactor and enhancement (#27433)
  _Files: `.github/workflows/nightly-test-npu-e2e-multi-node.yml`, `.github/workflows/nightly-test-npu-e2e-single-node.yml`, `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/disaggregation_utils.py` _+54 more__
- **2026-06-25** [`dbe9e3b706`](https://github.com/sgl-project/sglang/commit/dbe9e3b706) [#29316](https://github.com/sgl-project/sglang/pull/29316)
  [PD] Early-send cached-prefix KV overlapping uncached prefill forward (#29316)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-06-25** [`2b64fc7a2c`](https://github.com/sgl-project/sglang/commit/2b64fc7a2c) [#27625](https://github.com/sgl-project/sglang/pull/27625)
  Remove Req.extend_logprob_start_len field and make it pure (#27625)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_prefill_adder.py`_
- **2026-06-25** [`7002a37ea1`](https://github.com/sgl-project/sglang/commit/7002a37ea1) [#27611](https://github.com/sgl-project/sglang/pull/27611)
  Inline extend_range accessors and remove the extend_input_len/fill_len properties (#27611)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/prefill.py` _+15 more__
- **2026-06-25** [`d0524d6433`](https://github.com/sgl-project/sglang/commit/d0524d6433) [#27610](https://github.com/sgl-project/sglang/pull/27610)
  Avoid scattered assignment of extend_input_len and fill_len by merging them into Req.extend_range (#27610)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/dllm/mixin/req.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py` _+10 more__
- **2026-06-25** [`6c839368e0`](https://github.com/sgl-project/sglang/commit/6c839368e0) [#29214](https://github.com/sgl-project/sglang/pull/29214)
  [Cleanup] IPC struct renames, better typing, and SenderWrapper removal (#29214)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/communicator.py`, `python/sglang/srt/managers/embed_types.py` _+7 more__
- **2026-06-24** [`85a3f1f75c`](https://github.com/sgl-project/sglang/commit/85a3f1f75c) [#29124](https://github.com/sgl-project/sglang/pull/29124)
  [Spec] Unify the overlap stash relay behind a RelayPayload dataclass (#29124)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` _+1 more__
- **2026-06-24** [`d5c566e59b`](https://github.com/sgl-project/sglang/commit/d5c566e59b) [#29098](https://github.com/sgl-project/sglang/pull/29098)
  Extract profile request cleanups (#29098)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/grpc_bridge.py`, `python/sglang/srt/entrypoints/grpc_server.py` _+12 more__
- **2026-06-24** [`84a7a84018`](https://github.com/sgl-project/sglang/commit/84a7a84018) [#28897](https://github.com/sgl-project/sglang/pull/28897)
  [PD] Fix data race in NixlKVManager for NIXL backend (#28897)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-06-24** [`33373cbb12`](https://github.com/sgl-project/sglang/commit/33373cbb12) [#28996](https://github.com/sgl-project/sglang/pull/28996)
  [misc] Move bench_serving into sglang.benchmark (#28996)
  _Files: `python/sglang/auto_benchmark_lib.py`, `python/sglang/benchmark/serving.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `python/sglang/test/ci/ci_stress_utils.py` _+10 more__
- **2026-06-23** [`34dd9c28ca`](https://github.com/sgl-project/sglang/commit/34dd9c28ca) [#29012](https://github.com/sgl-project/sglang/pull/29012)
  [Refactor] Introduce sock_send/sock_recv wrappers for zmq IPC (#29012)
  _Files: `python/sglang/srt/debug_utils/dumper.py`, `python/sglang/srt/disaggregation/encode_grpc_server.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/elastic_ep/expert_backup_client.py` _+18 more__
- **2026-06-23** [`a65c68c1fb`](https://github.com/sgl-project/sglang/commit/a65c68c1fb) [#29023](https://github.com/sgl-project/sglang/pull/29023)
  Revert "[CI] Fix flaky optimistic test by adding contention handling" (#29023)
  _Files: `test/registered/disaggregation/test_disaggregation_optimistic_prefill.py`_
- **2026-06-23** [`743ce88bc5`](https://github.com/sgl-project/sglang/commit/743ce88bc5) [#28995](https://github.com/sgl-project/sglang/pull/28995)
  Fix flaky optimistic prefill retry test (#28995)
  _Files: `python/sglang/srt/disaggregation/prefill.py`_
- **2026-06-23** [`62f7ffc492`](https://github.com/sgl-project/sglang/commit/62f7ffc492) [#26574](https://github.com/sgl-project/sglang/pull/26574)
  feat: add Mooncake group semantics (#26574)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/README.md`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `test/registered/unit/mem_cache/test_mooncake_group_semantics.py`_
- **2026-06-22** [`ab21dc984a`](https://github.com/sgl-project/sglang/commit/ab21dc984a) [#28947](https://github.com/sgl-project/sglang/pull/28947)
  [CI] Fix flaky optimistic test by adding contention handling (#28947)
  _Files: `test/registered/disaggregation/test_disaggregation_optimistic_prefill.py`_
- **2026-06-22** [`1adb53f147`](https://github.com/sgl-project/sglang/commit/1adb53f147) [#28718](https://github.com/sgl-project/sglang/pull/28718)
  Fix CP page filtering by request-local position (#28718)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/utils.py`_
- **2026-06-22** [`106d2930a6`](https://github.com/sgl-project/sglang/commit/106d2930a6) [#28363](https://github.com/sgl-project/sglang/pull/28363)
  [core] Gate the overlap WAR barrier on forward reads to recover decode throughput (#28363)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py` _+5 more__

## KV Cache / Memory  (21 commits)

- **2026-06-29** [`f76e707f59`](https://github.com/sgl-project/sglang/commit/f76e707f59) [#29546](https://github.com/sgl-project/sglang/pull/29546)
  Clean up follow-ups for eagle hidden dim clean up (#29546)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`_
- **2026-06-29** [`e1ca92a7fd`](https://github.com/sgl-project/sglang/commit/e1ca92a7fd) [#28974](https://github.com/sgl-project/sglang/pull/28974)
  [weight checker] refactor: add precision branch; allow ULP quant err; used chunked compare (#28974)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler_components/weight_updater.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/utils/weight_checker.py` _+3 more__
- **2026-06-29** [`bd2a5db987`](https://github.com/sgl-project/sglang/commit/bd2a5db987) [#29310](https://github.com/sgl-project/sglang/pull/29310)
  [HiCache] Detect for double-free in HostKVCache (#29310)
  _Files: `python/sglang/srt/mem_cache/pool_host/base.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py`_
- **2026-06-28** [`aaa31eb0a1`](https://github.com/sgl-project/sglang/commit/aaa31eb0a1) [#29436](https://github.com/sgl-project/sglang/pull/29436)
  feat: first-class session identity in SGLang (#29436)
  _Files: `proto/sglang/runtime/v1/sglang.proto`, `python/sglang/lang/backend/runtime_endpoint.py`, `python/sglang/srt/entrypoints/EngineBase.py`, `python/sglang/srt/entrypoints/engine.py` _+20 more__
- **2026-06-27** [`592f6c849b`](https://github.com/sgl-project/sglang/commit/592f6c849b) [#28713](https://github.com/sgl-project/sglang/pull/28713)
  [minimax-m3] Split 2/4: mem-cache / HiCache / sparse KV pool (#28713)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+6 more__
- **2026-06-27** [`c1b5c7e499`](https://github.com/sgl-project/sglang/commit/c1b5c7e499) [#29106](https://github.com/sgl-project/sglang/pull/29106)
  Fix DeepSeek V4 PP HiCache SWA allocation and layer mapping (#29106)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dsv4.py` _+1 more__
- **2026-06-26** [`da0f4f6f92`](https://github.com/sgl-project/sglang/commit/da0f4f6f92) [#28614](https://github.com/sgl-project/sglang/pull/28614)
  [HiCache] remove large host mem constraint (#28614)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool_host.py` _+1 more__
- **2026-06-26** [`c0d4d1897c`](https://github.com/sgl-project/sglang/commit/c0d4d1897c) [#29265](https://github.com/sgl-project/sglang/pull/29265)
  fix: batch BlockRemoved events per radix node (#29265)
  _Files: `python/sglang/srt/mem_cache/events.py`, `test/manual/test_kv_events.py`, `test/registered/unit/mem_cache/test_mamba_unittest.py`, `test/registered/unit/mem_cache/test_radix_cache_unit.py` _+2 more__
- **2026-06-26** [`8fd6e9e017`](https://github.com/sgl-project/sglang/commit/8fd6e9e017) [#29258](https://github.com/sgl-project/sglang/pull/29258)
  Fix fixed-size HiCache capacity under PP (#29258)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/pool_host/base.py`_
- **2026-06-25** [`4ba8634780`](https://github.com/sgl-project/sglang/commit/4ba8634780) [#29058](https://github.com/sgl-project/sglang/pull/29058)
  [AMD] Register scripted-core chunked-prefill test for AMD extra-a CI (#29058)
  _Files: `test/registered/chunked_prefill/test_scripted_core_1gpu.py`_
- **2026-06-25** [`a9270250c3`](https://github.com/sgl-project/sglang/commit/a9270250c3) [#27144](https://github.com/sgl-project/sglang/pull/27144)
  Dllm radix cache npu (#27144)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-06-24** [`76db6c9d9e`](https://github.com/sgl-project/sglang/commit/76db6c9d9e) [#28973](https://github.com/sgl-project/sglang/pull/28973)
  [Refactor] Share CUDA graph memory pool across prefill and decode (#28973)
  _Files: `python/sglang/srt/model_executor/runner_backend/breakable_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_backend/full_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_backend/tc_piecewise_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_utils/pool.py`_
- **2026-06-24** [`03773ae35b`](https://github.com/sgl-project/sglang/commit/03773ae35b) [#28258](https://github.com/sgl-project/sglang/pull/28258)
  [HiCache] Add NIXL FILE cache cleaner (#28258)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/README.md`, `python/sglang/srt/mem_cache/storage/nixl/hicache_nixl.py`, `python/sglang/srt/mem_cache/storage/nixl/nixl.config.toml.sample`, `python/sglang/srt/mem_cache/storage/nixl/nixl_cleaner.py` _+4 more__
- **2026-06-24** [`b6a8000473`](https://github.com/sgl-project/sglang/commit/b6a8000473) [#28422](https://github.com/sgl-project/sglang/pull/28422)
  [bugfix][decode hicache] _storage_hit_query use HybridPrefetchOperation (#28422)
  _Files: `python/sglang/srt/mem_cache/hiradix_cache.py`_
- **2026-06-23** [`0460f277b7`](https://github.com/sgl-project/sglang/commit/0460f277b7) [#29032](https://github.com/sgl-project/sglang/pull/29032)
  Fix manual chunked-prefill test to use req.fill_len after fill_ids refactor (#29032)
  _Files: `test/manual/chunked_prefill/test_scripted_special_case.py`_
- **2026-06-23** [`e67b228d4c`](https://github.com/sgl-project/sglang/commit/e67b228d4c) [#27058](https://github.com/sgl-project/sglang/pull/27058)
  feat: session radix cache (#27058)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/session_radix_cache.py` _+3 more__
- **2026-06-23** [`349a6af6b8`](https://github.com/sgl-project/sglang/commit/349a6af6b8) [#28916](https://github.com/sgl-project/sglang/pull/28916)
  [HiCache] Fix hicache host memory leak by bounding PP-sync work_list (#28916)
  _Files: `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_hiradix_pp_sync_drain.py`_
- **2026-06-23** [`4740f23e1f`](https://github.com/sgl-project/sglang/commit/4740f23e1f) [#28991](https://github.com/sgl-project/sglang/pull/28991)
  Revert "[server_args] compute mem_fraction_static after dp chunked-prefill division" (#28991)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-23** [`de3ec2c437`](https://github.com/sgl-project/sglang/commit/de3ec2c437) [#28884](https://github.com/sgl-project/sglang/pull/28884)
  [server_args] compute mem_fraction_static after dp chunked-prefill division (#28884)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-22** [`c0198fc277`](https://github.com/sgl-project/sglang/commit/c0198fc277) [#28813](https://github.com/sgl-project/sglang/pull/28813)
  [CI] Refactor int checkpoint tests style (#28813)
  _Files: `test/registered/mem_cache/test_int8_checkpoint_store.py`, `test/registered/radix_cache/test_int8_mamba_checkpoint_e2e.py`_
- **2026-06-22** [`70883cb1b0`](https://github.com/sgl-project/sglang/commit/70883cb1b0) [#28904](https://github.com/sgl-project/sglang/pull/28904)
  [UnifiedTree]: Rollback mamba hicache test to direct io backend (#28904)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`, `test/registered/hicache/test_qwen35_hicache.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mamba.py`, `test/registered/unit/mem_cache/test_hicache_staged_write_back_dispatch.py`_

## Quantization  (16 commits)

- **2026-06-29** [`06fd2efedd`](https://github.com/sgl-project/sglang/commit/06fd2efedd) [#29029](https://github.com/sgl-project/sglang/pull/29029)
  [NPU][Bugfix] Fix a ModelSlim loading failure (#29029)
  _Files: `python/sglang/srt/layers/quantization/modelslim/modelslim.py`_
- **2026-06-27** [`a3c5e286f6`](https://github.com/sgl-project/sglang/commit/a3c5e286f6) [#29501](https://github.com/sgl-project/sglang/pull/29501)
  [NPU] [DOC] Fix and update Ascend NPU docs (#29501)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_environment_variables.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_faq.mdx` _+5 more__
- **2026-06-26** [`e745b3af22`](https://github.com/sgl-project/sglang/commit/e745b3af22) [#28662](https://github.com/sgl-project/sglang/pull/28662)
  [Fix] compressed-tensors block FP8: requantize weight scales to UE8M0 for DeepGEMM on Blackwell (#28662)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/manual/quant/test_compressed_tensors_fp8_block_ue8m0.py` _+1 more__
- **2026-06-26** [`c98d31143d`](https://github.com/sgl-project/sglang/commit/c98d31143d) [#26784](https://github.com/sgl-project/sglang/pull/26784)
  update quantization code owner and document quantization contributions (#26784)
  _Files: `.github/CODEOWNERS`, `docs_new/docs.json`, `docs_new/docs/developer_guide/overview.mdx`, `docs_new/docs/developer_guide/quantization_contribution_guide.mdx`_
- **2026-06-26** [`c21c2d9421`](https://github.com/sgl-project/sglang/commit/c21c2d9421) [#29400](https://github.com/sgl-project/sglang/pull/29400)
  [Docs] Cookbook: match playground docker image resolution to deployment (hw|quant) (#29400)
  _Files: `docs_new/src/snippets/_playground.jsx`_
- **2026-06-26** [`dd56a9f069`](https://github.com/sgl-project/sglang/commit/dd56a9f069) [#29380](https://github.com/sgl-project/sglang/pull/29380)
  [Docs] Add NVFP4 quantization to GLM-5.2 cookbook (#29380)
  _Files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-review-pr/SKILL.md` _+4 more__
- **2026-06-26** [`cfc0a0e0e0`](https://github.com/sgl-project/sglang/commit/cfc0a0e0e0) [#18139](https://github.com/sgl-project/sglang/pull/18139)
  Add Intel Quantization Support in SGLang (#18139)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `python/pyproject.toml`, `python/sglang/srt/configs/load_config.py`, `python/sglang/srt/configs/model_config.py` _+4 more__
- **2026-06-26** [`4b0b0ea55f`](https://github.com/sgl-project/sglang/commit/4b0b0ea55f) [#29286](https://github.com/sgl-project/sglang/pull/29286)
  [sgl-kernel/cpu]: exclude amx gemm source from arm build (#29286)
  _Files: `sgl-kernel/csrc/cpu/CMakeLists.txt`, `sgl-kernel/csrc/cpu/aarch64/gemm_int8.cpp`, `sgl-kernel/csrc/cpu/gemm_int8.cpp`_
- **2026-06-25** [`3344b73c80`](https://github.com/sgl-project/sglang/commit/3344b73c80) [#28103](https://github.com/sgl-project/sglang/pull/28103)
  Add DeepSeek V4 Pro GB300 nightly and expand Kimi K25 nightly test (#28103)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `test/registered/gb300/test_deepseek_v4_pro_fp4.py`, `test/registered/gb300/test_glm5_fp8.py`, `test/registered/gb300/test_glm5_nvfp4.py` _+5 more__
- **2026-06-25** [`52c32035eb`](https://github.com/sgl-project/sglang/commit/52c32035eb) [#28928](https://github.com/sgl-project/sglang/pull/28928)
  [diffusion] Add Qwen-Image ModelOpt NVFP4 support (#28928)
  _Files: `docs_new/cookbook/diffusion/Qwen-Image/Qwen-Image.mdx`, `docs_new/docs/sglang-diffusion/quantization.mdx`, `docs_new/src/snippets/diffusion/qwen-image-deployment.jsx`, `python/sglang/multimodal_gen/registry.py` _+6 more__
- **2026-06-25** [`0075c8f02b`](https://github.com/sgl-project/sglang/commit/0075c8f02b) [#29194](https://github.com/sgl-project/sglang/pull/29194)
  [AMD] [GLM5] GLM-5.1 MXFP4 (MI355X) + enable EAGLE for gfx950 in cookbook (#29194)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.1.mdx`, `docs_new/src/snippets/autoregressive/glm-51-deployment.jsx`_
- **2026-06-24** [`3c95a87b66`](https://github.com/sgl-project/sglang/commit/3c95a87b66) [#29201](https://github.com/sgl-project/sglang/pull/29201)
  Fix the CuDNN failure on bmm_fp8 when two libcudart.so exists. (#29201)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-06-24** [`09b808ab7e`](https://github.com/sgl-project/sglang/commit/09b808ab7e) [#28832](https://github.com/sgl-project/sglang/pull/28832)
  [diffusion] fix: fix Qwen-Image-Layered latent shape (#28832)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py` _+3 more__
- **2026-06-24** [`4da23fdc35`](https://github.com/sgl-project/sglang/commit/4da23fdc35) [#27859](https://github.com/sgl-project/sglang/pull/27859)
  [NPU] removes deprecated pr testing files (#27859)
  _Files: `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/basic_function/quant/test_npu_w8a8_quantization.py`_
- **2026-06-22** [`441ae9a5ae`](https://github.com/sgl-project/sglang/commit/441ae9a5ae) [#28885](https://github.com/sgl-project/sglang/pull/28885)
  [Lint] Fix black formatting of DeepSeek-R1-MXFP4 MI35x tests (#28885)
- **2026-06-22** [`64e455d4bf`](https://github.com/sgl-project/sglang/commit/64e455d4bf) [#28886](https://github.com/sgl-project/sglang/pull/28886)
  Fix lint break on main (#28886)
  _Files: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`_

## Scheduler / Batching  (15 commits)

- **2026-06-29** [`91cf159696`](https://github.com/sgl-project/sglang/commit/91cf159696) [#29571](https://github.com/sgl-project/sglang/pull/29571)
  [PP] bugfix: include CP size in PP rank offset (#29571)
  _Files: `python/sglang/srt/managers/scheduler_components/request_receiver.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/registered/unit/managers/test_pp_cp_rank_offsets.py`_
- **2026-06-29** [`bb74ed4a8d`](https://github.com/sgl-project/sglang/commit/bb74ed4a8d) [#29549](https://github.com/sgl-project/sglang/pull/29549)
  Replace hasattr with isinstance in SHM feature helpers (#29549)
  _Files: `python/sglang/srt/managers/mm_utils.py`_
- **2026-06-28** [`c5b9388721`](https://github.com/sgl-project/sglang/commit/c5b9388721) [#29535](https://github.com/sgl-project/sglang/pull/29535)
  [scheduler] Add scheduler metrics reporter init hook (#29535)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-06-26** [`ff89e0fe9a`](https://github.com/sgl-project/sglang/commit/ff89e0fe9a) [#29044](https://github.com/sgl-project/sglang/pull/29044)
  Fix KV event publisher bind conflict under PP (#29044)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/kv_events_publisher.py`, `python/sglang/srt/observability/metrics_collector.py`_
- **2026-06-26** [`ed71fb8f95`](https://github.com/sgl-project/sglang/commit/ed71fb8f95) [#28906](https://github.com/sgl-project/sglang/pull/28906)
  fix(anthropic): detect-and-passthrough mid-conversation system messages (#28906)
  _Files: `python/sglang/srt/entrypoints/anthropic/protocol.py`, `python/sglang/srt/entrypoints/anthropic/serving.py`, `python/sglang/srt/managers/template_detection.py`, `test/registered/unit/entrypoints/anthropic/test_serving.py`_
- **2026-06-25** [`118d6b2e5e`](https://github.com/sgl-project/sglang/commit/118d6b2e5e) [#29224](https://github.com/sgl-project/sglang/pull/29224)
  [Cleanup] Style and type annotation improvements extracted from #28688 (#29224)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py` _+1 more__
- **2026-06-25** [`f9a3720e2b`](https://github.com/sgl-project/sglang/commit/f9a3720e2b) [#28504](https://github.com/sgl-project/sglang/pull/28504)
  Skip empty non-idle output batches (#28504)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`_
- **2026-06-25** [`2812a3c93a`](https://github.com/sgl-project/sglang/commit/2812a3c93a) [#29225](https://github.com/sgl-project/sglang/pull/29225)
  [Spec] Unify spec/non-spec decode result handling and overlap relay-payload gating (#29225)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/utils.py`_
- **2026-06-25** [`563c3418a7`](https://github.com/sgl-project/sglang/commit/563c3418a7) [#27616](https://github.com/sgl-project/sglang/pull/27616)
  Avoid dual semantics of extend_input_len by computing the candidate on the fly (#27616)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `test/registered/unit/managers/test_prefill_adder.py`_
- **2026-06-24** [`7e63feee6f`](https://github.com/sgl-project/sglang/commit/7e63feee6f) [#29207](https://github.com/sgl-project/sglang/pull/29207)
  Add scheduler metrics extension hooks (#29207)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-06-24** [`c6822f81b1`](https://github.com/sgl-project/sglang/commit/c6822f81b1) [#29122](https://github.com/sgl-project/sglang/pull/29122)
  [Spec] Make the overlap bonus-token relay unconditional (#29122)
  _Files: `python/sglang/srt/managers/overlap_utils.py`_
- **2026-06-23** [`ecab3f322e`](https://github.com/sgl-project/sglang/commit/ecab3f322e) [#29079](https://github.com/sgl-project/sglang/pull/29079)
  Revert "Improve MFU metrics for prefill and verify timing" (#29079)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-06-23** [`b60185c41c`](https://github.com/sgl-project/sglang/commit/b60185c41c) [#29000](https://github.com/sgl-project/sglang/pull/29000)
  Improve MFU metrics for prefill and verify timing (#29000)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-06-23** [`0c6e8e9477`](https://github.com/sgl-project/sglang/commit/0c6e8e9477) [#28449](https://github.com/sgl-project/sglang/pull/28449)
  Expand parser auto detection coverage (#28449)
  _Files: `python/sglang/srt/managers/template_detection.py`, `test/registered/unit/managers/test_template_manager.py`_
- **2026-06-23** [`ed0a62e4dd`](https://github.com/sgl-project/sglang/commit/ed0a62e4dd) [#27731](https://github.com/sgl-project/sglang/pull/27731)
  [Mem] Add KV-page double-free checks to the invariant checker (#27731)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/test/server_fixtures/streaming_session_fixture.py`, `test/registered/unit/managers/test_kv_page_invariants.py`_

## Triton / Kernels  (14 commits)

- **2026-06-29** [`bd3b252e0a`](https://github.com/sgl-project/sglang/commit/bd3b252e0a) [#29382](https://github.com/sgl-project/sglang/pull/29382)
  [CPU] use faster exp in silu_and_mul (#29382)
  _Files: `sgl-kernel/csrc/cpu/activation.cpp`_
- **2026-06-29** [`909123ddb8`](https://github.com/sgl-project/sglang/commit/909123ddb8) [#29591](https://github.com/sgl-project/sglang/pull/29591)
  [misc] Use --cuda-graph-max-bs-decode in tests, examples, and docs (#29591)
- **2026-06-29** [`3217410cf6`](https://github.com/sgl-project/sglang/commit/3217410cf6) [#29378](https://github.com/sgl-project/sglang/pull/29378)
  [CPU] enable fused_sigmoid_mul on CPU device (#29378)
  _Files: `python/sglang/srt/models/qwen3_5.py`, `sgl-kernel/csrc/cpu/activation.cpp`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`, `test/registered/cpu/test_activation.py`_
- **2026-06-26** [`714011a40f`](https://github.com/sgl-project/sglang/commit/714011a40f) [#21531](https://github.com/sgl-project/sglang/pull/21531)
  [JIT Kernel] Migrate dsv3_router_gemm from AOT sgl-kernel to JIT kernel (#21531)
  _Files: `python/sglang/jit_kernel/csrc/gemm/dsv3_router_gemm.cuh`, `python/sglang/jit_kernel/dsv3_router_gemm.py`, `python/sglang/srt/models/deepseek_v2.py`, `sgl-kernel/CMakeLists.txt` _+8 more__
- **2026-06-26** [`dc113e8804`](https://github.com/sgl-project/sglang/commit/dc113e8804) [#27783](https://github.com/sgl-project/sglang/pull/27783)
  [Intel GPU] DeepSeek V4 3/N: Support hc_split_sinkhorn on XPU using sgl_kernel (#27783)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-06-25** [`4a8200565e`](https://github.com/sgl-project/sglang/commit/4a8200565e) [#28320](https://github.com/sgl-project/sglang/pull/28320)
  Fused QK GemmaRMSNorm + RoPE + gate kernel for Qwen3.5 (#28320)
  _Files: `python/sglang/srt/layers/fused_qk_rmsnorm_rope_gate.py`, `python/sglang/srt/models/qwen3_5.py`_
- **2026-06-25** [`2c3f007a65`](https://github.com/sgl-project/sglang/commit/2c3f007a65) [#29117](https://github.com/sgl-project/sglang/pull/29117)
  [CPU] optimize GDN prefill performance (#29117)
  _Files: `sgl-kernel/csrc/cpu/mamba/fla.cpp`, `sgl-kernel/csrc/cpu/vec.h`, `test/registered/cpu/test_mamba.py`_
- **2026-06-24** [`39f5de9ba1`](https://github.com/sgl-project/sglang/commit/39f5de9ba1) [#29101](https://github.com/sgl-project/sglang/pull/29101)
  [NPU] bump sgl-kernel-npu to 2026.6.2 (#29101)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-06-24** [`bf231f01a3`](https://github.com/sgl-project/sglang/commit/bf231f01a3) [#27870](https://github.com/sgl-project/sglang/pull/27870)
  [qwen3.5][XPU]Add XPU support for set_embed_and_head and fused QK RMSNorm kernel (#27870)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-06-23** [`c4376aaa88`](https://github.com/sgl-project/sglang/commit/c4376aaa88) [#28968](https://github.com/sgl-project/sglang/pull/28968)
  [Refactor] Remove dead out_cache_loc_swa buffers (#28968)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_utils/buffers.py`_
- **2026-06-22** [`43b1fb95f6`](https://github.com/sgl-project/sglang/commit/43b1fb95f6) [#28950](https://github.com/sgl-project/sglang/pull/28950)
  [CI] Optimize nixl dependency installation script (#28950)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-06-22** [`06e001347a`](https://github.com/sgl-project/sglang/commit/06e001347a) [#28930](https://github.com/sgl-project/sglang/pull/28930)
  [CI] Update nixl installation to include nixl-cu13 for h20 runner (#28930)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-06-22** [`b8e64fb56d`](https://github.com/sgl-project/sglang/commit/b8e64fb56d) [#28927](https://github.com/sgl-project/sglang/pull/28927)
  [CI] Modify nixl installation to force reinstall (#28927)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-06-22** [`db12bfcdc8`](https://github.com/sgl-project/sglang/commit/db12bfcdc8) [#28670](https://github.com/sgl-project/sglang/pull/28670)
  [JIT] Add kpool_topk_transform JIT kernel (#28670)
  _Files: `python/sglang/jit_kernel/csrc/dsa/kpool_topk_transform.cuh`, `python/sglang/jit_kernel/kpool_topk_transform.py`, `test/registered/jit/test_kpool_topk_transform.py`_

## Models  (13 commits)

- **2026-06-29** [`d5133e925b`](https://github.com/sgl-project/sglang/commit/d5133e925b) [#29493](https://github.com/sgl-project/sglang/pull/29493)
  [NPU][Bugfix] Add scoring_func for mimo_v2 (#29493)
  _Files: `python/sglang/srt/models/mimo_v2.py`_
- **2026-06-28** [`ae09b8302f`](https://github.com/sgl-project/sglang/commit/ae09b8302f) [#29502](https://github.com/sgl-project/sglang/pull/29502)
  [CI] Fix GB300 DSV4 Pro FP4 nightly (#29502)
  _Files: `test/registered/gb300/test_deepseek_v4_pro_fp4.py`_
- **2026-06-26** [`cc294829aa`](https://github.com/sgl-project/sglang/commit/cc294829aa) [#29303](https://github.com/sgl-project/sglang/pull/29303)
  [NPU] fix best practicce docs (#29303)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_r1.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_v3_2.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/glm5_1.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/kimi_k2_6.mdx` _+9 more__
- **2026-06-26** [`10ff3c1dcb`](https://github.com/sgl-project/sglang/commit/10ff3c1dcb) [#29293](https://github.com/sgl-project/sglang/pull/29293)
  [NPU] [DOC] Add environment prerequisites to model tutorials (#29293)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/model-tutorials/deepseek_r1.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/model-tutorials/deepseek_v3_2.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/model-tutorials/glm_5_1.mdx` _+10 more__
- **2026-06-25** [`4d06d4c97f`](https://github.com/sgl-project/sglang/commit/4d06d4c97f) [#29266](https://github.com/sgl-project/sglang/pull/29266)
  Sync Gemma4 hardware table with Blackwell recipes (#29266)
  _Files: `docs_new/cookbook/autoregressive/Google/Gemma4.mdx`_
- **2026-06-25** [`ddda4f9028`](https://github.com/sgl-project/sglang/commit/ddda4f9028) [#29111](https://github.com/sgl-project/sglang/pull/29111)
  [Bugfix] Fix Ministral3 init argument forwarding (#29111)
  _Files: `python/sglang/srt/models/ministral3.py`_
- **2026-06-25** [`e4976683f4`](https://github.com/sgl-project/sglang/commit/e4976683f4) [#29261](https://github.com/sgl-project/sglang/pull/29261)
  [Docs] Fix broken links in cookbook (#29261)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/cookbook/autoregressive/GLM/GLM-4.7.mdx`, `docs_new/cookbook/autoregressive/NVIDIA/Nemotron3-Nano-Omni.mdx`_
- **2026-06-25** [`efbe67d237`](https://github.com/sgl-project/sglang/commit/efbe67d237) [#29252](https://github.com/sgl-project/sglang/pull/29252)
  Tune Gemma4 26B-A4B B200 memory recipe (#29252)
  _Files: `docs_new/cookbook/autoregressive/Google/Gemma4.mdx`, `docs_new/src/snippets/autoregressive/gemma4-deployment.jsx`_
- **2026-06-24** [`73d976e375`](https://github.com/sgl-project/sglang/commit/73d976e375) [#29129](https://github.com/sgl-project/sglang/pull/29129)
  [NPU] [DOC] Fix TOC of Ascend NPU Docs (#29129)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`, `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx` _+14 more__
- **2026-06-23** [`abb0717174`](https://github.com/sgl-project/sglang/commit/abb0717174) [#28988](https://github.com/sgl-project/sglang/pull/28988)
  [CI] Fix lint brought by #27527 (#28988)
  _Files: `python/sglang/srt/models/deepseek_ocr.py`, `test/manual/test_create_custom_4d_mask.py`_
- **2026-06-23** [`6cd8d2869b`](https://github.com/sgl-project/sglang/commit/6cd8d2869b) [#27527](https://github.com/sgl-project/sglang/pull/27527)
  Vectorize _create_custom_4d_mask in CustomQwen2Decoder (#27527)
  _Files: `python/sglang/srt/models/deepseek_ocr.py`, `test/manual/test_create_custom_4d_mask.py`_
- **2026-06-22** [`4e1d25117b`](https://github.com/sgl-project/sglang/commit/4e1d25117b) [#28621](https://github.com/sgl-project/sglang/pull/28621)
  [NPU] update best practice docs from testcase (#28621)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_r1.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_v3_2.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/glm5_1.mdx` _+10 more__
- **2026-06-22** [`93553a67a3`](https://github.com/sgl-project/sglang/commit/93553a67a3) [#27893](https://github.com/sgl-project/sglang/pull/27893)
  [NPU] [DOC] Create deployment tutorials for mainstream models on Ascend NPU (#27893)
  _Files: `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_deepseek_example.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_faq.mdx` _+30 more__

## Speculative Decoding  (13 commits)

- **2026-06-28** [`6eedc8f376`](https://github.com/sgl-project/sglang/commit/6eedc8f376) [#29464](https://github.com/sgl-project/sglang/pull/29464)
  Fix EAGLE draft hidden dim extraction and centralize spec helpers (#29464)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py` _+6 more__
- **2026-06-28** [`da802ddcaf`](https://github.com/sgl-project/sglang/commit/da802ddcaf) [#29223](https://github.com/sgl-project/sglang/pull/29223)
  (perf): Shard Kimi-K2.5 Eagle3 draft fc + symm-mem AG (#29223)
  _Files: `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/models/kimi_k25_eagle3.py`, `test/registered/jit/benchmark/bench_symm_mem_all_gather.py` _+1 more__
- **2026-06-26** [`7f376644e0`](https://github.com/sgl-project/sglang/commit/7f376644e0) [#29313](https://github.com/sgl-project/sglang/pull/29313)
  [AMD] [GLM5] Mark EAGLE verified on MI300X/MI325X (gfx942) in GLM-5.1 cookbook (#29313)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.1.mdx`, `docs_new/src/snippets/autoregressive/glm-51-deployment.jsx`_
- **2026-06-24** [`c01ad10d16`](https://github.com/sgl-project/sglang/commit/c01ad10d16) [#29078](https://github.com/sgl-project/sglang/pull/29078)
  [perf] tiny optimize select_index op for draft extend (#29078)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-06-24** [`2c697daf5f`](https://github.com/sgl-project/sglang/commit/2c697daf5f) [#29200](https://github.com/sgl-project/sglang/pull/29200)
  [Cookbook] Nemotron3-Ultra: align MTP draft depth with NVIDIA reference (num_steps 5) (#29200)
  _Files: `docs_new/src/snippets/autoregressive/nemotron3-ultra-deployment.jsx`_
- **2026-06-24** [`24bf8d91bb`](https://github.com/sgl-project/sglang/commit/24bf8d91bb) [#28492](https://github.com/sgl-project/sglang/pull/28492)
  Refactor / simplify `MultiLayerEagleDraftExtendCudaGraphRunner` to use rotation (#28492)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/multi_layer_eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_utils.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` _+1 more__
- **2026-06-24** [`f444b5897b`](https://github.com/sgl-project/sglang/commit/f444b5897b) [#27634](https://github.com/sgl-project/sglang/pull/27634)
  [Spec][1/N] Decoupled speculative decoding: IPC protocol + cross-process request id + server flags (#27634)
  _Files: `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/decoupled_spec_io.py`, `test/registered/unit/server_args/test_server_args.py`, `test/registered/unit/spec/test_decoupled_spec_io.py`_
- **2026-06-23** [`854c688121`](https://github.com/sgl-project/sglang/commit/854c688121) [#28754](https://github.com/sgl-project/sglang/pull/28754)
  [Spec] Unify decode KV-commit bookkeeping across spec-v2 workers (#28754)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/session/streaming_session.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py` _+1 more__
- **2026-06-23** [`28d5627fd8`](https://github.com/sgl-project/sglang/commit/28d5627fd8) [#28850](https://github.com/sgl-project/sglang/pull/28850)
  [AMD] register kv_canary + mock_model e2e tests to extra-a (1-gpu-small + 2-gpu-large) (#28850)
  _Files: `.github/workflows/pr-test-amd-extra.yml`, `test/registered/kv_canary/test_self_e2e_baseline.py`, `test/registered/kv_canary/test_self_e2e_bench_speed.py`, `test/registered/kv_canary/test_self_e2e_pd_baseline.py` _+15 more__
- **2026-06-23** [`a17753e449`](https://github.com/sgl-project/sglang/commit/a17753e449) [#26880](https://github.com/sgl-project/sglang/pull/26880)
  Fix EAGLE draft graph seq_lens_sum padding (#26880)
  _Files: `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`, `test/registered/unit/spec/test_eagle_draft_cuda_graph_runner.py`_
- **2026-06-22** [`bbc853df46`](https://github.com/sgl-project/sglang/commit/bbc853df46) [#28802](https://github.com/sgl-project/sglang/pull/28802)
  fix(schedule_batch): trim stop string when EOS matches in the same step (#28802)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_stop_str_speculative.py`_
- **2026-06-22** [`ad9723af03`](https://github.com/sgl-project/sglang/commit/ad9723af03) [#28937](https://github.com/sgl-project/sglang/pull/28937)
  Clean up CUDA graph capture logs (#28937)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/multi_layer_eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/base_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+5 more__
- **2026-06-22** [`2ce32366a0`](https://github.com/sgl-project/sglang/commit/2ce32366a0) [#28870](https://github.com/sgl-project/sglang/pull/28870)
  [Fix][BCG][Spec] Restore EAGLE prefill plumbing dropped by #23906 (#28870)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/cuda_graph/breakable/test_bcg_with_speculative_decoding.py`_

## Docs / Examples  (10 commits)

- **2026-06-29** [`489017b3d6`](https://github.com/sgl-project/sglang/commit/489017b3d6) [#29632](https://github.com/sgl-project/sglang/pull/29632)
  [NPU] [DOC] Update deterministic inference feature support status to A2, A3 (#29632)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-06-29** [`38d4ffcd86`](https://github.com/sgl-project/sglang/commit/38d4ffcd86) [#28731](https://github.com/sgl-project/sglang/pull/28731)
  [cookbook] drop redundant serve flags (GLM-5.2) + fix M3 page-size note (#28731)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs_new/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx` _+1 more__
- **2026-06-27** [`e0c0c0a45c`](https://github.com/sgl-project/sglang/commit/e0c0c0a45c) [#29486](https://github.com/sgl-project/sglang/pull/29486)
  [Cookbook] GLM-5.2: tune GB300 NVFP4 recipes + fill benchmarks (#29486)
  _Files: `docs_new/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-06-26** [`12f76d115c`](https://github.com/sgl-project/sglang/commit/12f76d115c) [#29466](https://github.com/sgl-project/sglang/pull/29466)
  Update GLM-5.2 B300 and GB300 NVFP4 cookbook settings (#29466)
  _Files: `docs_new/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-06-26** [`f83cbc2516`](https://github.com/sgl-project/sglang/commit/f83cbc2516) [#29321](https://github.com/sgl-project/sglang/pull/29321)
  Add LFM2.5-230M to the LFM2.5 cookbook (#29321)
  _Files: `docs_new/cookbook/autoregressive/LiquidAI/LFM2.5.mdx`, `docs_new/docs/supported-models/generative_models.mdx`, `docs_new/src/snippets/configs/LiquidAI/lfm2.5-benchmarks.jsx`, `docs_new/src/snippets/configs/LiquidAI/lfm2.5.jsx`_
- **2026-06-24** [`dd2d919e21`](https://github.com/sgl-project/sglang/commit/dd2d919e21) [#29135](https://github.com/sgl-project/sglang/pull/29135)
  [Docs] Fix mem-fraction-static default and document how it is computed (#29135)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`_
- **2026-06-23** [`f74a1722e6`](https://github.com/sgl-project/sglang/commit/f74a1722e6) [#22744](https://github.com/sgl-project/sglang/pull/22744)
  [NVIDIA] Support TF32 matmul to improve MiniMax gate gemm performance (#22744)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/server_args.py`_
- **2026-06-23** [`84338df6f0`](https://github.com/sgl-project/sglang/commit/84338df6f0) [#28909](https://github.com/sgl-project/sglang/pull/28909)
  [NPU] [DOC] Update contribution guide of Ascend NPU (#28909)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_contribution_guide.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-06-22** [`34e5e38604`](https://github.com/sgl-project/sglang/commit/34e5e38604) [#28675](https://github.com/sgl-project/sglang/pull/28675)
  [Cookbook] Nemotron3-Ultra: Add mamba-backend and SSM dtype flags (#28675)
  _Files: `docs_new/cookbook/autoregressive/NVIDIA/Nemotron3-Ultra.mdx`, `docs_new/src/snippets/autoregressive/nemotron3-ultra-deployment.jsx`_
- **2026-06-22** [`5deca2d39f`](https://github.com/sgl-project/sglang/commit/5deca2d39f) [#28643](https://github.com/sgl-project/sglang/pull/28643)
  [DOC] [NPU] Update features on Ascend NPU (#28643)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_

## Tensor / Data Parallel  (9 commits)

- **2026-06-29** [`c7b9b92d9a`](https://github.com/sgl-project/sglang/commit/c7b9b92d9a) [#29596](https://github.com/sgl-project/sglang/pull/29596)
  Fix CI caused by https://github.com/sgl-project/sglang/pull/29576 (#29596)
  _Files: `test/registered/kernels/test_dsa_indexer.py`_
- **2026-06-27** [`2f34dbe372`](https://github.com/sgl-project/sglang/commit/2f34dbe372) [#29342](https://github.com/sgl-project/sglang/pull/29342)
  Add native Exa-backed web_search support (#29342)
  _Files: `docs_new/cookbook/autoregressive/OpenAI/GPT-OSS.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py` _+6 more__
- **2026-06-27** [`cd6dedf972`](https://github.com/sgl-project/sglang/commit/cd6dedf972) [#29467](https://github.com/sgl-project/sglang/pull/29467)
  [router] Count requests/responses at the HTTP edge for true intake (#29467)
  _Files: `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/monitoring/grafana-dashboard.json`, `experimental/sgl-router/src/server/app.rs`, `experimental/sgl-router/src/server/metrics.rs` _+6 more__
- **2026-06-25** [`e4696ed62d`](https://github.com/sgl-project/sglang/commit/e4696ed62d) [#29332](https://github.com/sgl-project/sglang/pull/29332)
  [test] Report token tps in fwd occupancy kit and force ignore_eos (#29332)
  _Files: `python/sglang/test/kits/fwd_occupancy_kit.py`_
- **2026-06-24** [`5f30fa258c`](https://github.com/sgl-project/sglang/commit/5f30fa258c) [#26245](https://github.com/sgl-project/sglang/pull/26245)
  Support DP-aware PD router dispatch (#26245)
  _Files: `sgl-model-gateway/src/core/worker.rs`, `sgl-model-gateway/src/core/worker_builder.rs`, `sgl-model-gateway/src/routers/http/pd_router.rs`_
- **2026-06-24** [`6c6fa19a90`](https://github.com/sgl-project/sglang/commit/6c6fa19a90) [#29128](https://github.com/sgl-project/sglang/pull/29128)
  [NPU] Support fsdp for rl_on_policy_target (#29128)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`_
- **2026-06-22** [`adc203dfee`](https://github.com/sgl-project/sglang/commit/adc203dfee) [#26263](https://github.com/sgl-project/sglang/pull/26263)
  fix(router): use full conversation for PD chat cache-aware routing (#26263) (#27430)
  _Files: `sgl-model-gateway/src/routers/http/pd_router.rs`_
- **2026-06-22** [`dd39ef6cec`](https://github.com/sgl-project/sglang/commit/dd39ef6cec) [#28869](https://github.com/sgl-project/sglang/pull/28869)
  [AMD] Pin httpx>=0.25.0 to fix anthropic SDK socket_options error (#28869)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-06-22** [`62b3c8e177`](https://github.com/sgl-project/sglang/commit/62b3c8e177) [#28531](https://github.com/sgl-project/sglang/pull/28531)
  [Intel GPU] Guard tvm_ffi import in dsv4 online mtp module under TYPE_CHECKING to fix import error on XPU (#28531)
  _Files: `python/sglang/jit_kernel/dsv4/online_c128_mtp.py`_

## ROCm / AMD  (7 commits)

- **2026-06-27** [`81d3c3ce77`](https://github.com/sgl-project/sglang/commit/81d3c3ce77) [#29373](https://github.com/sgl-project/sglang/pull/29373)
  [AMD] [GLM5] Guard cuda_runtime.h for ROCm in fused_metadata_copy (#29373)
  _Files: `python/sglang/jit_kernel/csrc/elementwise/fused_metadata_copy.cuh`_
- **2026-06-26** [`c470acde2b`](https://github.com/sgl-project/sglang/commit/c470acde2b) [#29333](https://github.com/sgl-project/sglang/pull/29333)
  [AMD] Register 1 kernel unit test for AMD nightly CI (#29333)
  _Files: `test/registered/kernels/test_gather_spec_extras.py`_
- **2026-06-26** [`b73e57210a`](https://github.com/sgl-project/sglang/commit/b73e57210a) [#28853](https://github.com/sgl-project/sglang/pull/28853)
  [AMD CI] Add nightly Miles ROCm 7.2 MI350X suites (#28853)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm720.yml`_
- **2026-06-24** [`c07811bfc6`](https://github.com/sgl-project/sglang/commit/c07811bfc6) [#29091](https://github.com/sgl-project/sglang/pull/29091)
  [AMD] Register MI355X 2N 1P1D disagg nightly workflow for testing (#29091)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-06-23** [`7e6587c94a`](https://github.com/sgl-project/sglang/commit/7e6587c94a) [#28981](https://github.com/sgl-project/sglang/pull/28981)
  [AMD] Update v4 cookbook to clean env vars (#28981)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-06-23** [`b42c79c4eb`](https://github.com/sgl-project/sglang/commit/b42c79c4eb) [#28989](https://github.com/sgl-project/sglang/pull/28989)
  [AMD] Fix AMD extra scheduled runs cancelling each other (#28989)
  _Files: `.github/workflows/pr-test-amd-extra.yml`_
- **2026-06-22** [`73448b0d70`](https://github.com/sgl-project/sglang/commit/73448b0d70) [#28871](https://github.com/sgl-project/sglang/pull/28871)
  [AMD] Temporarily disable deepseek V4 in AMD PR test (#28871)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`_

## CI / Build  (5 commits)

- **2026-06-28** [`b1da2082ca`](https://github.com/sgl-project/sglang/commit/b1da2082ca) [#28481](https://github.com/sgl-project/sglang/pull/28481)
  chore: bump sgl-deep-gemm build-time apache-tvm-ffi 0.1.9 -> 0.1.11 (#28481)
  _Files: `docker/sgl-deep-gemm.Dockerfile`_
- **2026-06-26** [`eeee3abbbf`](https://github.com/sgl-project/sglang/commit/eeee3abbbf) [#29329](https://github.com/sgl-project/sglang/pull/29329)
  [CI] Fix false spec accept length failure after profiling phase (#29329)
  _Files: `python/sglang/test/performance_test_runner.py`_
- **2026-06-24** [`d46afbf8b4`](https://github.com/sgl-project/sglang/commit/d46afbf8b4) [#28749](https://github.com/sgl-project/sglang/pull/28749)
  Fix nightly CI test for GLM-4.6 + B200 (#28749)
  _Files: `python/sglang/srt/server_args.py`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-06-24** [`6842335fcf`](https://github.com/sgl-project/sglang/commit/6842335fcf) [#28934](https://github.com/sgl-project/sglang/pull/28934)
  [MUSA][24/N] CI:Fix LLM server smoke test (#28934)
  _Files: `test/registered/musa/test_llm_server_smoke_musa.py`_
- **2026-06-22** [`a32f7111e4`](https://github.com/sgl-project/sglang/commit/a32f7111e4) [#28965](https://github.com/sgl-project/sglang/pull/28965)
  [CI] Disable async-assert for base-a tests in rerun-test (#28965)
  _Files: `.github/workflows/rerun-test.yml`_

## Serving / API  (5 commits)

- **2026-06-24** [`e3f1fa9d8e`](https://github.com/sgl-project/sglang/commit/e3f1fa9d8e) [#29108](https://github.com/sgl-project/sglang/pull/29108)
  [misc] Unify benchmark deprecation shims and one_batch_server CLI entrypoint (#29108)
  _Files: `python/sglang/bench_one_batch_server.py`, `python/sglang/bench_serving.py`, `python/sglang/benchmark/datasets/autobench.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py` _+5 more__
- **2026-06-23** [`ed26a109ee`](https://github.com/sgl-project/sglang/commit/ed26a109ee) [#28601](https://github.com/sgl-project/sglang/pull/28601)
  [Fix] Return streaming logprobs when reasoning/tool parser is active (#28601)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-06-22** [`e00703bb2a`](https://github.com/sgl-project/sglang/commit/e00703bb2a) [#28090](https://github.com/sgl-project/sglang/pull/28090)
  fix(frontend): return 400 for missing completions json_schema (#28090)
  _Files: `python/sglang/srt/entrypoints/openai/serving_completions.py`, `test/registered/unit/entrypoints/openai/test_serving_completions.py`_
- **2026-06-22** [`b5e4e289b1`](https://github.com/sgl-project/sglang/commit/b5e4e289b1) [#23507](https://github.com/sgl-project/sglang/pull/23507)
  [gRPC] Native server: Python bridge entrypoint (2/4) (#23507)
  _Files: `python/sglang/srt/entrypoints/grpc_bridge.py`_
- **2026-06-22** [`018d0c21dc`](https://github.com/sgl-project/sglang/commit/018d0c21dc) [#28522](https://github.com/sgl-project/sglang/pull/28522)
  [Docs] Add Anthropic-compatible API documentation (#28522)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs_new/docs.json`, `docs_new/docs/basic_usage/anthropic_api.mdx`, `docs_new/docs/basic_usage/openai_api.mdx` _+1 more__

## Structured Output  (2 commits)

- **2026-06-26** [`13b5bd962a`](https://github.com/sgl-project/sglang/commit/13b5bd962a) [#29102](https://github.com/sgl-project/sglang/pull/29102)
  fix(spec): track current_token in ReasonerGrammarObject (#29102)
  _Files: `python/sglang/srt/constrained/reasoner_grammar_backend.py`, `test/registered/unit/constrained/test_reasoner_grammar_backend.py`_
- **2026-06-24** [`5f76736427`](https://github.com/sgl-project/sglang/commit/5f76736427) [#25071](https://github.com/sgl-project/sglang/pull/25071)
  kimik2_detector fix the normal text detection before tool call.  (#25071)
  _Files: `python/sglang/srt/function_call/kimik2_detector.py`, `test/registered/function_call/test_kimik2_detector.py`_

---
_Generated 2026-06-29 12:42 UTC_