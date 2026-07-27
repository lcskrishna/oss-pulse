# vllm-project/vllm — Weekly Change Report
**Period:** 2026-07-20 → 2026-07-27  |  **Total commits:** 278

## ✨ New Features This Week

- **2026-07-27** [#48841](https://github.com/vllm-project/vllm/pull/48841) — [ROCm] [Model] Enable TML inkling (#48841)
- **2026-07-27** [#47514](https://github.com/vllm-project/vllm/pull/47514) — [Quantization][INC]Add MXFP8 Linear Support (#47514)
- **2026-07-27** [#49502](https://github.com/vllm-project/vllm/pull/49502) — [3/N][Core][KV Connector] Support reliable partial-tail KV offload for sub-block prompts (#49502)
- **2026-07-27** [#49571](https://github.com/vllm-project/vllm/pull/49571) — [Hardware][Power] Add FAST_EXP for Power (#49571)
- **2026-07-27** [#49422](https://github.com/vllm-project/vllm/pull/49422) — [XPU][CI] Add more test cases in Intel GPU CI (#49422)
- **2026-07-27** [#49895](https://github.com/vllm-project/vllm/pull/49895) — [CI] Add kimi and k3 auto-labeling rules (#49895)
- **2026-07-27** [#49394](https://github.com/vllm-project/vllm/pull/49394) — [XPU] Enable QK Norm + RoPE fusion pass on XPU (#49394)
- **2026-07-27** [#49331](https://github.com/vllm-project/vllm/pull/49331) — [ModelRunner V2] Support encoder-only attention (#49331)
- **2026-07-26** [#46877](https://github.com/vllm-project/vllm/pull/46877) — [Core][Distributed] Add process-checkpoint lifecycle hooks for communicators (starting with Flashinfer) (#46877)
- **2026-07-26** [#45429](https://github.com/vllm-project/vllm/pull/45429) — [Model] Support top_k and top_p sampling for DiffusionGemma (#45429)
- _…and 37 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-27** [`30fbd05537`](https://github.com/vllm-project/vllm/commit/30fbd05537) [#49909](https://github.com/vllm-project/vllm/pull/49909) — [ROCm] Use backend-default dot precision for ReplaySSM (#49909)
- **2026-07-27** [`0906123953`](https://github.com/vllm-project/vllm/commit/0906123953) [#48841](https://github.com/vllm-project/vllm/pull/48841) — [ROCm] [Model] Enable TML inkling (#48841)
- **2026-07-27** [`bc3629b1c4`](https://github.com/vllm-project/vllm/commit/bc3629b1c4) [#49732](https://github.com/vllm-project/vllm/pull/49732) — [ROCm][CI] Skip three torchao tests of gfx950 until `torchao==0.18` is released (#49732)
- **2026-07-27** [`312ea82e75`](https://github.com/vllm-project/vllm/commit/312ea82e75) [#49837](https://github.com/vllm-project/vllm/pull/49837) — [CI][ROCm] Make hf-xet reconstruction safe on shared NFS (#49837)
- **2026-07-27** [`394beb633b`](https://github.com/vllm-project/vllm/commit/394beb633b) [#49843](https://github.com/vllm-project/vllm/pull/49843) — [Bugfix][ROCm] Use batch DMA for CPU KV cache loads (#49843)
- **2026-07-27** [`7f599d7854`](https://github.com/vllm-project/vllm/commit/7f599d7854) [#46913](https://github.com/vllm-project/vllm/pull/46913) — [communication] [bugfix] fix quickreduce acc error in cudagraph mode (#46913)
- **2026-07-27** [`e09900436c`](https://github.com/vllm-project/vllm/commit/e09900436c) [#49915](https://github.com/vllm-project/vllm/pull/49915) — [CI][ROCm] Reduce kernel test runtime (#49915)
- **2026-07-27** [`49f31d7cee`](https://github.com/vllm-project/vllm/commit/49f31d7cee) [#49913](https://github.com/vllm-project/vllm/pull/49913) — [ROCm] Make vllm_c RMSNorm output contiguous (#49913)
- **2026-07-27** [`da99ffcc13`](https://github.com/vllm-project/vllm/commit/da99ffcc13) [#49516](https://github.com/vllm-project/vllm/pull/49516) — [ROCm][CI] Keep native datasets cache off shared NFS (#49516)
- **2026-07-27** [`854c33f380`](https://github.com/vllm-project/vllm/commit/854c33f380) [#49911](https://github.com/vllm-project/vllm/pull/49911) — [CI][ROCm] Keep global GPU memory cleanup opt-in (#49911)
- **2026-07-27** [`ac87549cbd`](https://github.com/vllm-project/vllm/commit/ac87549cbd) [#49916](https://github.com/vllm-project/vllm/pull/49916) — [CI][ROCm] Reduce V1 attention test runtime (#49916)
- **2026-07-27** [`ffc4f08c8e`](https://github.com/vllm-project/vllm/commit/ffc4f08c8e) [#46116](https://github.com/vllm-project/vllm/pull/46116) — [Core][KV-transfer] MoRIIO: heterogeneous TP<->DP prefill/decode read routing (#46116)
- **2026-07-25** [`ca0defa343`](https://github.com/vllm-project/vllm/commit/ca0defa343) [#49726](https://github.com/vllm-project/vllm/pull/49726) — Make bare `hugging_face` imports forbidden (#49726)
- **2026-07-25** [`0ba2aa35a8`](https://github.com/vllm-project/vllm/commit/0ba2aa35a8) [#49242](https://github.com/vllm-project/vllm/pull/49242) — Stabilize GPU memory teardown between ROCm CI tests (#49242)
- **2026-07-25** [`d9cd774198`](https://github.com/vllm-project/vllm/commit/d9cd774198) [#49763](https://github.com/vllm-project/vllm/pull/49763) — [ROCm][CI] Force native compile caches onto local disk (#49763)
- **2026-07-24** [`33c4f3551c`](https://github.com/vllm-project/vllm/commit/33c4f3551c) [#49739](https://github.com/vllm-project/vllm/pull/49739) — [ROCm][CI] Wait for ROCm VRAM to settle between compiled and eager LL… (#49739)
- **2026-07-24** [`caa9cad31e`](https://github.com/vllm-project/vllm/commit/caa9cad31e) [#49737](https://github.com/vllm-project/vllm/pull/49737) — [ROCm][Docker] Drop MORI_GPU_ARCHS so MoRI autodetects the device arch (#49737)
- **2026-07-24** [`7513d071bd`](https://github.com/vllm-project/vllm/commit/7513d071bd) [#49733](https://github.com/vllm-project/vllm/pull/49733) — [ROCm][CI] Fix XPASS(strict) on mixed audio embeds test (#49733)
- **2026-07-24** [`84d26b9ee3`](https://github.com/vllm-project/vllm/commit/84d26b9ee3) [#49729](https://github.com/vllm-project/vllm/pull/49729) — [Model] Remove Plamo2 (#49729)
- **2026-07-24** [`2279575cd9`](https://github.com/vllm-project/vllm/commit/2279575cd9) [#47206](https://github.com/vllm-project/vllm/pull/47206) — [AMD][Bugfix][EPLB] Fix elastic EP scaling accuracy on ROCm (#47206)
- **2026-07-24** [`41798069f3`](https://github.com/vllm-project/vllm/commit/41798069f3) [#49257](https://github.com/vllm-project/vllm/pull/49257) — [CI][AMD] Deprecate DinD for MI355 tests (#49257)
- **2026-07-24** [`8eac21a602`](https://github.com/vllm-project/vllm/commit/8eac21a602) [#49673](https://github.com/vllm-project/vllm/pull/49673) — [ROCM] Fix AITER Fused AllReduce RMSNorm for Transformers Backend (#49673)
- **2026-07-24** [`0d77325b10`](https://github.com/vllm-project/vllm/commit/0d77325b10) [#49223](https://github.com/vllm-project/vllm/pull/49223) — Bump Transformers version to 5.14.1 (#49223)
- **2026-07-24** [`80c9d5d5e0`](https://github.com/vllm-project/vllm/commit/80c9d5d5e0) [#48050](https://github.com/vllm-project/vllm/pull/48050) — [ROCm][Quantization] Add Quark W4A8 (INT4-FP8) MoE CI coverage (#48050)
- **2026-07-24** [`1479bd9e9d`](https://github.com/vllm-project/vllm/commit/1479bd9e9d) [#49270](https://github.com/vllm-project/vllm/pull/49270) — [ROCm][CI] Prepare AMD mirrors for regating (#49270)
- **2026-07-23** [`4501a6d56b`](https://github.com/vllm-project/vllm/commit/4501a6d56b) [#49551](https://github.com/vllm-project/vllm/pull/49551) — [ROCm][CI] Language Models tests tiny-mixtral with aiter fix (#49551)
- **2026-07-23** [`27ffbfde8d`](https://github.com/vllm-project/vllm/commit/27ffbfde8d) [#48044](https://github.com/vllm-project/vllm/pull/48044) — Fused Shared Expert Support for AMD Quark DeepSeek-V4 Model Checkpoints (#48044)
- **2026-07-22** [`53c2f20dd9`](https://github.com/vllm-project/vllm/commit/53c2f20dd9) [#49350](https://github.com/vllm-project/vllm/pull/49350) — [ROCm][CI] skip moe weight padding for eplb (#49350)
- **2026-07-22** [`387189c429`](https://github.com/vllm-project/vllm/commit/387189c429) [#47992](https://github.com/vllm-project/vllm/pull/47992) — [ROCm] Remove redundant AITER fused_qk_rmsnorm probe (avoids config-time HIP init) (#47992)
- **2026-07-22** [`16aca639b7`](https://github.com/vllm-project/vllm/commit/16aca639b7) [#49251](https://github.com/vllm-project/vllm/pull/49251) — [ROCm] Upgrade NIXL and UCX (#49251)
- **2026-07-22** [`ba18929079`](https://github.com/vllm-project/vllm/commit/ba18929079) [#49178](https://github.com/vllm-project/vllm/pull/49178) — [Bugfix][SpecDecode] Scope MTP completeness checks outside bucketed updates (#49178)
- **2026-07-22** [`0500ca6a58`](https://github.com/vllm-project/vllm/commit/0500ca6a58) [#49380](https://github.com/vllm-project/vllm/pull/49380) — [CI][Bugfix] Fix ROCm FP8 KV cache dtype in attention backend test (#49380)
- **2026-07-21** [`05781e21dd`](https://github.com/vllm-project/vllm/commit/05781e21dd) [#49329](https://github.com/vllm-project/vllm/pull/49329) — [ROCm][CI] Fix order-dependent failure in test_flash_attn_accepts_handled_fp8_variants (MI355) (#49329)
- **2026-07-21** [`61e10f0116`](https://github.com/vllm-project/vllm/commit/61e10f0116) [#48845](https://github.com/vllm-project/vllm/pull/48845) — [ROCm][CI] Fix AITER MLA fp8 decode metadata regression test (#48845)
- **2026-07-21** [`6e96891ba0`](https://github.com/vllm-project/vllm/commit/6e96891ba0) [#48683](https://github.com/vllm-project/vllm/pull/48683) — [ROCm] Bump AITER to v0.1.16.post5 (#48683)
- **2026-07-20** [`a2b1f9fc3b`](https://github.com/vllm-project/vllm/commit/a2b1f9fc3b) [#49245](https://github.com/vllm-project/vllm/pull/49245) — [ROCm] [Release] [Bugfix] Fix the per commit wheel release pipeline. (#49245)
- **2026-07-20** [`5feb3950e5`](https://github.com/vllm-project/vllm/commit/5feb3950e5) [#49234](https://github.com/vllm-project/vllm/pull/49234) — [ROCm][CI] fix test_rocm_quick_reduce.py (#49234)
- **2026-07-20** [`752bd10647`](https://github.com/vllm-project/vllm/commit/752bd10647) [#49128](https://github.com/vllm-project/vllm/pull/49128) — [ROCm][CI] Fix sparse MLA metadata sync fixture (#49128)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#49954](https://github.com/vllm-project/vllm/issues/49954) | [Bug]: Responses code_interpreter returns HTTP 500 when tool arguments | bug | 2026-07-27 |
| [#41663](https://github.com/vllm-project/vllm/issues/41663) | [Bug]: XPU TP=2 on dual Intel Arc Pro B70 (Battlemage): GP fault + xe  | bug, intel-gpu | 2026-07-27 |
| [#49694](https://github.com/vllm-project/vllm/issues/49694) | [Bug]: ngram_gpu spec decode + structured outputs (xgrammar) + async s | bug | 2026-07-27 |
| [#35519](https://github.com/vllm-project/vllm/issues/35519) | [Bug]: Qwen3.5 NVFP4 models crash on ARM64 GB10 DGX Spark (CUDA illega | bug, unstale | 2026-07-27 |
| [#49927](https://github.com/vllm-project/vllm/issues/49927) | [Perf] #48137 costs ~10.6% spec-decode acceptance and #48660 shifts ou | cpu | 2026-07-27 |
| [#49893](https://github.com/vllm-project/vllm/issues/49893) | [Bug]: SpeculativeConfig method="draft_model" cannot load mixed-precis | bug, quantization | 2026-07-27 |
| [#37003](https://github.com/vllm-project/vllm/issues/37003) | [RFC]: Context-Aware KV-Cache Retention API (Prioritized Evictions) | RFC | 2026-07-27 |
| [#34694](https://github.com/vllm-project/vllm/issues/34694) | [Bug]: BF16 NVFP4 Marlin produces garbled output on GPUs without nativ | bug | 2026-07-27 |
| [#49413](https://github.com/vllm-project/vllm/issues/49413) | [RFC]: KV offload event path refactor — provenance-carrying events and | — | 2026-07-27 |
| [#48193](https://github.com/vllm-project/vllm/issues/48193) | [Roadmap] Cold Start Q3 2026 | — | 2026-07-27 |
| [#38587](https://github.com/vllm-project/vllm/issues/38587) | [Bug]: RCCL RDNA3 gfx1100 Tp2 ROCM at startup | bug, rocm, stale | 2026-07-27 |
| [#49926](https://github.com/vllm-project/vllm/issues/49926) | [Bug]: EngineDeadError NVFP4 marlin | bug, quantization | 2026-07-27 |
| [#37151](https://github.com/vllm-project/vllm/issues/37151) | [Bug]: [ROCm][gfx1151] Engine Core segfaults in libhsa-runtime64.so wh | bug, rocm, stale | 2026-07-27 |
| [#37167](https://github.com/vllm-project/vllm/issues/37167) | [Bug]: responses API, combining of message and tool call | bug, stale | 2026-07-27 |
| [#37242](https://github.com/vllm-project/vllm/issues/37242) | [Community] RTX 5090 (Blackwell sm_120) + WSL2 2.7.0: CUDA graphs work | stale | 2026-07-27 |
| [#39694](https://github.com/vllm-project/vllm/issues/39694) | [RFC]:  PR de-dup/Similarity-Check  CI workflow ? | RFC, unstale | 2026-07-27 |
| [#40919](https://github.com/vllm-project/vllm/issues/40919) | [Bug]: RMSNormGated input_guard breaks torch.compile dynamo tracing | bug, stale | 2026-07-27 |
| [#40999](https://github.com/vllm-project/vllm/issues/40999) | [Feature][FP8] Opt-in `ParallelLMHead` quantization in legacy `Fp8Conf | stale | 2026-07-27 |
| [#49924](https://github.com/vllm-project/vllm/issues/49924) | [Bug][XPU]: GDN attention silently corrupts memory under load — fix me | bug, intel-gpu | 2026-07-27 |
| [#49920](https://github.com/vllm-project/vllm/issues/49920) | [Bug]: DiffusionGemma - Unconditional minimax_m3 warmup import in kern | bug | 2026-07-27 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 37 |
| Other | 37 |
| Attention | 35 |
| MoE / Expert Parallel | 23 |
| CI / Build | 23 |
| KV Cache / Offload | 17 |
| Multimodal | 17 |
| Scheduler / Engine | 16 |
| Quantization | 15 |
| Models | 14 |
| Disaggregation / PD | 11 |
| Serving / API | 11 |
| Docs | 6 |
| Perf / Benchmark | 5 |
| Compilation / CUDA Graph | 4 |
| LoRA | 4 |
| Speculative Decoding | 3 |

## ROCm / AMD  (37 commits)

- **2026-07-27** [`30fbd05537`](https://github.com/vllm-project/vllm/commit/30fbd05537) [#49909](https://github.com/vllm-project/vllm/pull/49909)
  [ROCm] Use backend-default dot precision for ReplaySSM (#49909)
  _Files: `.buildkite/test-amd.yaml`, `vllm/model_executor/layers/mamba/ops/selective_state_update_replayssm_output_only.py`_
- **2026-07-27** [`0906123953`](https://github.com/vllm-project/vllm/commit/0906123953) [#48841](https://github.com/vllm-project/vllm/pull/48841)
  [ROCm] [Model] Enable TML inkling (#48841)
  _Files: `benchmarks/kernels/benchmark_inkling_qkvr_prep.py`, `tests/models/inkling/rocm/conftest.py`, `tests/models/inkling/rocm/test_model_alignment.py`, `tests/models/inkling/rocm/test_mxfp4_load.py` _+29 more__
- **2026-07-27** [`bc3629b1c4`](https://github.com/vllm-project/vllm/commit/bc3629b1c4) [#49732](https://github.com/vllm-project/vllm/pull/49732)
  [ROCm][CI] Skip three torchao tests of gfx950 until `torchao==0.18` is released (#49732)
  _Files: `tests/quantization/test_torchao.py`_
- **2026-07-27** [`312ea82e75`](https://github.com/vllm-project/vllm/commit/312ea82e75) [#49837](https://github.com/vllm-project/vllm/pull/49837)
  [CI][ROCm] Make hf-xet reconstruction safe on shared NFS (#49837)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-07-27** [`394beb633b`](https://github.com/vllm-project/vllm/commit/394beb633b) [#49843](https://github.com/vllm-project/vllm/pull/49843)
  [Bugfix][ROCm] Use batch DMA for CPU KV cache loads (#49843)
  _Files: `tests/v1/kv_offload/cpu/test_gpu_worker.py`, `vllm/v1/kv_offload/cpu/gpu_worker.py`_
- **2026-07-27** [`7f599d7854`](https://github.com/vllm-project/vllm/commit/7f599d7854) [#46913](https://github.com/vllm-project/vllm/pull/46913)
  [communication] [bugfix] fix quickreduce acc error in cudagraph mode (#46913)
  _Files: `csrc/quickreduce/quick_reduce.h`, `tests/distributed/test_rocm_quick_reduce.py`_
- **2026-07-27** [`e09900436c`](https://github.com/vllm-project/vllm/commit/e09900436c) [#49915](https://github.com/vllm-project/vllm/pull/49915)
  [CI][ROCm] Reduce kernel test runtime (#49915)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/core/test_fused_quant_layernorm.py`, `tests/kernels/core/test_vit_fp8_scaling.py`_
- **2026-07-27** [`49f31d7cee`](https://github.com/vllm-project/vllm/commit/49f31d7cee) [#49913](https://github.com/vllm-project/vllm/pull/49913)
  [ROCm] Make vllm_c RMSNorm output contiguous (#49913)
  _Files: `tests/kernels/ir/test_layernorm.py`, `vllm/kernels/vllm_c.py`_
- **2026-07-27** [`da99ffcc13`](https://github.com/vllm-project/vllm/commit/da99ffcc13) [#49516](https://github.com/vllm-project/vllm/pull/49516)
  [ROCm][CI] Keep native datasets cache off shared NFS (#49516)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-07-27** [`854c33f380`](https://github.com/vllm-project/vllm/commit/854c33f380) [#49911](https://github.com/vllm-project/vllm/pull/49911)
  [CI][ROCm] Keep global GPU memory cleanup opt-in (#49911)
  _Files: `tests/conftest.py`_
- **2026-07-27** [`ac87549cbd`](https://github.com/vllm-project/vllm/commit/ac87549cbd) [#49916](https://github.com/vllm-project/vllm/pull/49916)
  [CI][ROCm] Reduce V1 attention test runtime (#49916)
  _Files: `.buildkite/test-amd.yaml`, `tests/v1/attention/test_mla_backends.py`_
- **2026-07-25** [`ca0defa343`](https://github.com/vllm-project/vllm/commit/ca0defa343) [#49726](https://github.com/vllm-project/vllm/pull/49726)
  Make bare `hugging_face` imports forbidden (#49726)
  _Files: `tests/conftest.py`, `tests/distributed/test_rocm_quick_reduce.py`, `tests/entrypoints/conftest.py`, `tests/entrypoints/multimodal/openai/chat_completion/test_chat_completion_with_mixed_audio_embeds.py` _+25 more__
- **2026-07-25** [`0ba2aa35a8`](https://github.com/vllm-project/vllm/commit/0ba2aa35a8) [#49242](https://github.com/vllm-project/vllm/pull/49242)
  Stabilize GPU memory teardown between ROCm CI tests (#49242)
  _Files: `tests/conftest.py`, `tests/lora/test_qwenvl.py`, `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`_
- **2026-07-25** [`d9cd774198`](https://github.com/vllm-project/vllm/commit/d9cd774198) [#49763](https://github.com/vllm-project/vllm/pull/49763)
  [ROCm][CI] Force native compile caches onto local disk (#49763)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-07-24** [`33c4f3551c`](https://github.com/vllm-project/vllm/commit/33c4f3551c) [#49739](https://github.com/vllm-project/vllm/pull/49739)
  [ROCm][CI] Wait for ROCm VRAM to settle between compiled and eager LL… (#49739)
  _Files: `tests/compile/test_dynamic_shapes_compilation.py`_
- **2026-07-24** [`caa9cad31e`](https://github.com/vllm-project/vllm/commit/caa9cad31e) [#49737](https://github.com/vllm-project/vllm/pull/49737)
  [ROCm][Docker] Drop MORI_GPU_ARCHS so MoRI autodetects the device arch (#49737)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-07-24** [`7513d071bd`](https://github.com/vllm-project/vllm/commit/7513d071bd) [#49733](https://github.com/vllm-project/vllm/pull/49733)
  [ROCm][CI] Fix XPASS(strict) on mixed audio embeds test (#49733)
  _Files: `tests/entrypoints/multimodal/openai/chat_completion/test_chat_completion_with_mixed_audio_embeds.py`_
- **2026-07-24** [`84d26b9ee3`](https://github.com/vllm-project/vllm/commit/84d26b9ee3) [#49729](https://github.com/vllm-project/vllm/pull/49729)
  [Model] Remove Plamo2 (#49729)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_language.yaml`, `docs/design/custom_op.md`, `docs/models/supported_models.md` _+9 more__
- **2026-07-24** [`2279575cd9`](https://github.com/vllm-project/vllm/commit/2279575cd9) [#47206](https://github.com/vllm-project/vllm/pull/47206)
  [AMD][Bugfix][EPLB] Fix elastic EP scaling accuracy on ROCm (#47206)
  _Files: `vllm/distributed/eplb/eplb_state.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-07-24** [`41798069f3`](https://github.com/vllm-project/vllm/commit/41798069f3) [#49257](https://github.com/vllm-project/vllm/pull/49257)
  [CI][AMD] Deprecate DinD for MI355 tests (#49257)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-07-24** [`8eac21a602`](https://github.com/vllm-project/vllm/commit/8eac21a602) [#49673](https://github.com/vllm-project/vllm/pull/49673)
  [ROCM] Fix AITER Fused AllReduce RMSNorm for Transformers Backend (#49673)
  _Files: `tests/compile/fusions_e2e/test_tp2_ar_rms.py`, `vllm/_aiter_ops.py`_
- **2026-07-24** [`0d77325b10`](https://github.com/vllm-project/vllm/commit/0d77325b10) [#49223](https://github.com/vllm-project/vllm/pull/49223)
  Bump Transformers version to 5.14.1 (#49223)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt` _+4 more__
- **2026-07-24** [`80c9d5d5e0`](https://github.com/vllm-project/vllm/commit/80c9d5d5e0) [#48050](https://github.com/vllm-project/vllm/pull/48050)
  [ROCm][Quantization] Add Quark W4A8 (INT4-FP8) MoE CI coverage (#48050)
  _Files: `tests/quantization/test_quark.py`_
- **2026-07-24** [`1479bd9e9d`](https://github.com/vllm-project/vllm/commit/1479bd9e9d) [#49270](https://github.com/vllm-project/vllm/pull/49270)
  [ROCm][CI] Prepare AMD mirrors for regating (#49270)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/basic_correctness.yaml` _+19 more__
- **2026-07-23** [`4501a6d56b`](https://github.com/vllm-project/vllm/commit/4501a6d56b) [#49551](https://github.com/vllm-project/vllm/pull/49551)
  [ROCm][CI] Language Models tests tiny-mixtral with aiter fix (#49551)
  _Files: `tests/models/language/generation/test_common.py`_
- **2026-07-23** [`27ffbfde8d`](https://github.com/vllm-project/vllm/commit/27ffbfde8d) [#48044](https://github.com/vllm-project/vllm/pull/48044)
  Fused Shared Expert Support for AMD Quark DeepSeek-V4 Model Checkpoints (#48044)
  _Files: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mtp.py`, `vllm/models/deepseek_v4/quant_config.py`_
- **2026-07-22** [`53c2f20dd9`](https://github.com/vllm-project/vllm/commit/53c2f20dd9) [#49350](https://github.com/vllm-project/vllm/pull/49350)
  [ROCm][CI] skip moe weight padding for eplb (#49350)
  _Files: `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`_
- **2026-07-22** [`387189c429`](https://github.com/vllm-project/vllm/commit/387189c429) [#47992](https://github.com/vllm-project/vllm/pull/47992)
  [ROCm] Remove redundant AITER fused_qk_rmsnorm probe (avoids config-time HIP init) (#47992)
  _Files: `vllm/_aiter_ops.py`, `vllm/compilation/passes/pass_manager.py`, `vllm/config/vllm.py`_
- **2026-07-22** [`16aca639b7`](https://github.com/vllm-project/vllm/commit/16aca639b7) [#49251](https://github.com/vllm-project/vllm/pull/49251)
  [ROCm] Upgrade NIXL and UCX (#49251)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `docker/Dockerfile.rocm`, `docker/ci-rocm.hcl`, `docker/docker-bake-rocm.hcl` _+6 more__
- **2026-07-22** [`ba18929079`](https://github.com/vllm-project/vllm/commit/ba18929079) [#49178](https://github.com/vllm-project/vllm/pull/49178)
  [Bugfix][SpecDecode] Scope MTP completeness checks outside bucketed updates (#49178)
  _Files: `tests/model_executor/model_loader/test_mtp_validation.py`, `vllm/distributed/weight_transfer/ipc_engine.py`, `vllm/distributed/weight_transfer/nccl_engine.py`, `vllm/model_executor/model_loader/mtp_validation.py` _+10 more__
- **2026-07-22** [`0500ca6a58`](https://github.com/vllm-project/vllm/commit/0500ca6a58) [#49380](https://github.com/vllm-project/vllm/pull/49380)
  [CI][Bugfix] Fix ROCm FP8 KV cache dtype in attention backend test (#49380)
  _Files: `tests/v1/attention/test_attention_backends.py`_
- **2026-07-21** [`05781e21dd`](https://github.com/vllm-project/vllm/commit/05781e21dd) [#49329](https://github.com/vllm-project/vllm/pull/49329)
  [ROCm][CI] Fix order-dependent failure in test_flash_attn_accepts_handled_fp8_variants (MI355) (#49329)
  _Files: `tests/kernels/attention/test_attention_selector.py`_
- **2026-07-21** [`61e10f0116`](https://github.com/vllm-project/vllm/commit/61e10f0116) [#48845](https://github.com/vllm-project/vllm/pull/48845)
  [ROCm][CI] Fix AITER MLA fp8 decode metadata regression test (#48845)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_decode_metadata.py`_
- **2026-07-21** [`6e96891ba0`](https://github.com/vllm-project/vllm/commit/6e96891ba0) [#48683](https://github.com/vllm-project/vllm/pull/48683)
  [ROCm] Bump AITER to v0.1.16.post5 (#48683)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-07-20** [`a2b1f9fc3b`](https://github.com/vllm-project/vllm/commit/a2b1f9fc3b) [#49245](https://github.com/vllm-project/vllm/pull/49245)
  [ROCm] [Release] [Bugfix] Fix the per commit wheel release pipeline. (#49245)
  _Files: `.buildkite/release-pipeline.yaml`_
- **2026-07-20** [`5feb3950e5`](https://github.com/vllm-project/vllm/commit/5feb3950e5) [#49234](https://github.com/vllm-project/vllm/pull/49234)
  [ROCm][CI] fix test_rocm_quick_reduce.py (#49234)
  _Files: `tests/distributed/test_rocm_quick_reduce.py`_
- **2026-07-20** [`752bd10647`](https://github.com/vllm-project/vllm/commit/752bd10647) [#49128](https://github.com/vllm-project/vllm/pull/49128)
  [ROCm][CI] Fix sparse MLA metadata sync fixture (#49128)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`_

## Other  (37 commits)

- **2026-07-27** [`cbc3a87200`](https://github.com/vllm-project/vllm/commit/cbc3a87200) [#49907](https://github.com/vllm-project/vllm/pull/49907)
  [Tokenizer] Use HF config for HF tokenizers (#49907)
  _Files: `vllm/tokenizers/registry.py`_
- **2026-07-27** [`74d3b799e1`](https://github.com/vllm-project/vllm/commit/74d3b799e1) [#49429](https://github.com/vllm-project/vllm/pull/49429)
  [Bugfix] Fix mHC block-M prenorm GEMM cross-row reduction carry-over (#49429)
  _Files: `vllm/model_executor/kernels/mhc/tilelang_kernels.py`_
- **2026-07-27** [`439f336212`](https://github.com/vllm-project/vllm/commit/439f336212) [#49736](https://github.com/vllm-project/vllm/pull/49736)
  [Core] Fix gpu<->cpu syncs in MRV2 mamba_hybrid.py (#49736)
  _Files: `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`_
- **2026-07-26** [`9e50e1037e`](https://github.com/vllm-project/vllm/commit/9e50e1037e) [#49857](https://github.com/vllm-project/vllm/pull/49857)
  [Bugfix][CuMem] Make KV-cache wake cleanup tag-safe (#49857)
  _Files: `vllm/device_allocator/cumem.py`_
- **2026-07-26** [`0da6e7f3d6`](https://github.com/vllm-project/vllm/commit/0da6e7f3d6) [#49134](https://github.com/vllm-project/vllm/pull/49134)
  [Bugfix] Reject contradictory custom-op directives (#49134)
  _Files: `tests/compile/test_config.py`, `vllm/config/compilation.py`, `vllm/model_executor/custom_op.py`_
- **2026-07-25** [`dbd80cc031`](https://github.com/vllm-project/vllm/commit/dbd80cc031) [#49777](https://github.com/vllm-project/vllm/pull/49777)
  [UX] DCP Topology Validation (#49777)
  _Files: `vllm/config/model.py`_
- **2026-07-25** [`ee1d996367`](https://github.com/vllm-project/vllm/commit/ee1d996367) [#49814](https://github.com/vllm-project/vllm/pull/49814)
  [Build] Fix for DeepEP manylinux pidfd sycall usage (#49814)
  _Files: `tools/ep_kernels/install_python_libraries.sh`_
- **2026-07-25** [`9321aff536`](https://github.com/vllm-project/vllm/commit/9321aff536) [#49805](https://github.com/vllm-project/vllm/pull/49805)
  [Bugfix] Wait for the linear bias before layerwise online processing (#49805)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/model_loader/reload/layerwise.py`, `vllm/model_executor/model_loader/reload/meta.py`, `vllm/model_executor/model_loader/reload/utils.py`_
- **2026-07-25** [`2e0da24150`](https://github.com/vllm-project/vllm/commit/2e0da24150) [#45117](https://github.com/vllm-project/vllm/pull/45117)
  Mergify message not on cancelled (#45117)
  _Files: `.github/mergify.yml`_
- **2026-07-25** [`1423569ff5`](https://github.com/vllm-project/vllm/commit/1423569ff5) [#48852](https://github.com/vllm-project/vllm/pull/48852)
  [Bugfix][Tool Parser] Fix dropped streaming arguments in Jamba and InternLM2 parsers (#48852)
  _Files: `tests/tool_parsers/test_internlm2_tool_parser.py`, `tests/tool_parsers/test_jamba_tool_parser.py`, `vllm/tool_parsers/internlm2_tool_parser.py`, `vllm/tool_parsers/jamba_tool_parser.py`_
- **2026-07-25** [`318b527cc2`](https://github.com/vllm-project/vllm/commit/318b527cc2) [#49419](https://github.com/vllm-project/vllm/pull/49419)
  [XPU] add warning for xpu graph limitations (#49419)
  _Files: `vllm/platforms/xpu.py`_
- **2026-07-25** [`6a1acac3fe`](https://github.com/vllm-project/vllm/commit/6a1acac3fe) [#49655](https://github.com/vllm-project/vllm/pull/49655)
  [BUGFIX] Fix log capture in KV test (#49655)
  _Files: `tests/v1/core/test_kv_cache_utils.py`_
- **2026-07-24** [`e222c33f2f`](https://github.com/vllm-project/vllm/commit/e222c33f2f) [#49727](https://github.com/vllm-project/vllm/pull/49727)
  [Bugfix] Register axk1 config to fix A.X-K1 init (#49727)
  _Files: `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/AXK1.py`, `vllm/transformers_utils/model_arch_config_convertor.py`_
- **2026-07-24** [`7b40fb9645`](https://github.com/vllm-project/vllm/commit/7b40fb9645) [#49247](https://github.com/vllm-project/vllm/pull/49247)
  [UX] Reject incompatible nested runtime overrides (#49247)
  _Files: `tests/test_config.py`, `tests/v1/worker/test_gpu_model_runner.py`, `vllm/config/utils.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-24** [`163ecba377`](https://github.com/vllm-project/vllm/commit/163ecba377) [#49586](https://github.com/vllm-project/vllm/pull/49586)
  [Bugfix] Skip linear bias in layerwise reload to avoid corruption (#49586)
  _Files: `vllm/model_executor/model_loader/reload/meta.py`_
- **2026-07-23** [`b354734d17`](https://github.com/vllm-project/vllm/commit/b354734d17) [#49603](https://github.com/vllm-project/vllm/pull/49603)
  [Bug] Fix batch invariance rms norm comparison (#49603)
  _Files: `tests/v1/determinism/test_rms_norm_batch_invariant.py`_
- **2026-07-23** [`b91a40e729`](https://github.com/vllm-project/vllm/commit/b91a40e729) [#49626](https://github.com/vllm-project/vllm/pull/49626)
  [Bugfix] Restore structured output logger initialization (#49626)
  _Files: `vllm/v1/structured_output/__init__.py`_
- **2026-07-23** [`494845e79f`](https://github.com/vllm-project/vllm/commit/494845e79f) [#49364](https://github.com/vllm-project/vllm/pull/49364)
  Revert "[MRV2] Always build attn metadata at capture time" (#49364) (#49451)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/cudagraph_utils.py`_
- **2026-07-23** [`638d6e9757`](https://github.com/vllm-project/vllm/commit/638d6e9757) [#44239](https://github.com/vllm-project/vllm/pull/44239)
  [Bugfix][CI/Build] Fix Plamo2 HF runner crash on transformers v5 (_tied_weights_keys list→dict) (#44239)
  _Files: `tests/conftest.py`, `tests/models/registry.py`_
- **2026-07-23** [`521aa80f71`](https://github.com/vllm-project/vllm/commit/521aa80f71) [#48399](https://github.com/vllm-project/vllm/pull/48399)
  [Core] Simplify KVBlockZeroer index tensor handling (#48399)
  _Files: `tests/v1/worker/test_kv_block_zeroer.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`, `vllm/v1/worker/utils.py`_
- **2026-07-22** [`7d10a4cfce`](https://github.com/vllm-project/vllm/commit/7d10a4cfce) [#49001](https://github.com/vllm-project/vllm/pull/49001)
  [Bugfix] Retry config read to survive concurrent HF cache refresh (#49001)
  _Files: `vllm/transformers_utils/config.py`_
- **2026-07-22** [`0f6cf7f628`](https://github.com/vllm-project/vllm/commit/0f6cf7f628) [#49045](https://github.com/vllm-project/vllm/pull/49045)
  [Rust Frontend] Extract request preparation from the inference path (#49045)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/text/src/lib.rs`_
- **2026-07-22** [`9df2f91232`](https://github.com/vllm-project/vllm/commit/9df2f91232) [#49396](https://github.com/vllm-project/vllm/pull/49396)
  [Renderer] Offload derender CPU work to renderer thread pool (#49396)
  _Files: `vllm/renderers/online_derenderer.py`_
- **2026-07-22** [`75576c63be`](https://github.com/vllm-project/vllm/commit/75576c63be) [#49398](https://github.com/vllm-project/vllm/pull/49398)
  Add auto label for xpu relate issue (#49398)
  _Files: `.github/workflows/issue_autolabel.yml`_
- **2026-07-22** [`6049424b7e`](https://github.com/vllm-project/vllm/commit/6049424b7e) [#49364](https://github.com/vllm-project/vllm/pull/49364)
  [MRV2] Always build attn metadata at capture time (#49364)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/cudagraph_utils.py`_
- **2026-07-21** [`60d443f738`](https://github.com/vllm-project/vllm/commit/60d443f738) [#48655](https://github.com/vllm-project/vllm/pull/48655)
  [CI/Build][The Rock][BugFix] Use fork method in test_multiproc_executor_multi_node for py 3.14 compat and fix test_multiproc_executor_shutdown_cleanup  (#48655)
  _Files: `tests/distributed/test_multiproc_executor.py`, `vllm/v1/executor/multiproc_executor.py`_
- **2026-07-21** [`5b3762a7f0`](https://github.com/vllm-project/vllm/commit/5b3762a7f0) [#49021](https://github.com/vllm-project/vllm/pull/49021)
  [Bugfix][CPU] Fix Clang OpenMP build on macOS (#49021)
  _Files: `csrc/cpu/cpu_attn_vec.hpp`_
- **2026-07-21** [`adc98f04d0`](https://github.com/vllm-project/vllm/commit/adc98f04d0) [#49298](https://github.com/vllm-project/vllm/pull/49298)
  [Misc] Add @esmeetu to codeowners for rust/src/bench (#49298)
  _Files: `.github/CODEOWNERS`_
- **2026-07-21** [`d9aa35161d`](https://github.com/vllm-project/vllm/commit/d9aa35161d) [#49269](https://github.com/vllm-project/vllm/pull/49269)
  Update BGE-M3 token expectations for leading spaces (#49269)
  _Files: `tests/plugins_tests/test_bge_m3_sparse_io_processor_plugins.py`_
- **2026-07-21** [`0a684ab0c0`](https://github.com/vllm-project/vllm/commit/0a684ab0c0) [#48444](https://github.com/vllm-project/vllm/pull/48444)
  [Bugfix] Fix WSL circular import from pin_memory warning_once (#48444)
  _Files: `vllm/platforms/cuda.py`, `vllm/platforms/interface.py`_
- **2026-07-21** [`2e2e626b40`](https://github.com/vllm-project/vllm/commit/2e2e626b40) [#48317](https://github.com/vllm-project/vllm/pull/48317)
  [Bugfix] Count per-group blocks in get_max_concurrency_for_kv_cache_config (#48317)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-07-21** [`af91f4b3e4`](https://github.com/vllm-project/vllm/commit/af91f4b3e4) [#49235](https://github.com/vllm-project/vllm/pull/49235)
  [Cleanup] Remove unused StructuredOutputRequest.status field (#49235)
  _Files: `vllm/v1/structured_output/request.py`_
- **2026-07-20** [`58b2012aa2`](https://github.com/vllm-project/vllm/commit/58b2012aa2) [#49208](https://github.com/vllm-project/vllm/pull/49208)
  [copy of #45208] CuMem slept-L1 fragmentation accounting (#49208)
  _Files: `tests/models/language/pooling/test_reward.py`, `tests/utils_/test_mem_utils.py`, `vllm/utils/mem_utils.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-20** [`b23bd73f54`](https://github.com/vllm-project/vllm/commit/b23bd73f54) [#47245](https://github.com/vllm-project/vllm/pull/47245)
  [XPU]add sycl path for Mhc (#47245)
  _Files: `vllm/model_executor/layers/mhc.py`_
- **2026-07-20** [`818cf61e91`](https://github.com/vllm-project/vllm/commit/818cf61e91) [#49042](https://github.com/vllm-project/vllm/pull/49042)
  [Rust Frontend] Fix macro-based content format detection (#49042)
  _Files: `rust/src/chat/src/renderer/hf/format.rs`, `rust/src/chat/src/renderer/hf/mod.rs`_
- **2026-07-20** [`9459fc6471`](https://github.com/vllm-project/vllm/commit/9459fc6471) [#45989](https://github.com/vllm-project/vllm/pull/45989)
  [Bugfix][RL] Set vLLM config during weight reload (#45989)
  _Files: `tests/v1/worker/test_gpu_worker_weight_transfer.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-20** [`dcfebf93f4`](https://github.com/vllm-project/vllm/commit/dcfebf93f4) [#48674](https://github.com/vllm-project/vllm/pull/48674)
  [Bugfix] Fix logprobs token-string collision from SentencePiece space… (#48674)
  _Files: `tests/tokenizers_/test_detokenize.py`, `vllm/tokenizers/detokenizer_utils.py`_

## Attention  (35 commits)

- **2026-07-27** [`8061dc26bd`](https://github.com/vllm-project/vllm/commit/8061dc26bd) [#49392](https://github.com/vllm-project/vllm/pull/49392)
  [Bugfix] Normalize sparse MLA warmup compression ratios (#49392)
  _Files: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-07-27** [`544cb724c8`](https://github.com/vllm-project/vllm/commit/544cb724c8) [#48577](https://github.com/vllm-project/vllm/pull/48577)
  [CPU][Spec Decode] Optimize GDN conv path for speculative decoding (#48577)
  _Files: `csrc/cpu/sgl-kernels/conv.cpp`, `csrc/cpu/torch_bindings.cpp`, `tests/kernels/mamba/cpu/test_cpu_gdn_ops.py`, `vllm/_custom_ops.py` _+1 more__
- **2026-07-27** [`f0553889c0`](https://github.com/vllm-project/vllm/commit/f0553889c0) [#48366](https://github.com/vllm-project/vllm/pull/48366)
  [Bugfix] Prevent NaN poisoning in xpu_mla_sparse for fully-masked index chunks (#48366)
  _Files: `tests/kernels/attention/test_xpu_mla_sparse.py`, `vllm/v1/attention/ops/xpu_mla_sparse.py`_
- **2026-07-27** [`fdaa0d9e59`](https://github.com/vllm-project/vllm/commit/fdaa0d9e59) [#49331](https://github.com/vllm-project/vllm/pull/49331)
  [ModelRunner V2] Support encoder-only attention (#49331)
  _Files: `tests/models/language/pooling/test_embedding.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/block_table.py`, `vllm/v1/worker/gpu/model_runner.py` _+4 more__
- **2026-07-26** [`b5b61c622c`](https://github.com/vllm-project/vllm/commit/b5b61c622c) [#46877](https://github.com/vllm-project/vllm/pull/46877)
  [Core][Distributed] Add process-checkpoint lifecycle hooks for communicators (starting with Flashinfer) (#46877)
  _Files: `tests/distributed/test_comm_ops.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`, `vllm/distributed/device_communicators/all2all.py`, `vllm/distributed/device_communicators/base_device_communicator.py` _+6 more__
- **2026-07-26** [`7eca0e1a64`](https://github.com/vllm-project/vllm/commit/7eca0e1a64) [#48906](https://github.com/vllm-project/vllm/pull/48906)
  [KV Offload] Deduplicate replicated MLA KV in the shared CPU region (#48906)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/test_gsm8k_offloading.py`, `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py` _+10 more__
- **2026-07-26** [`1240c74c0a`](https://github.com/vllm-project/vllm/commit/1240c74c0a) [#49372](https://github.com/vllm-project/vllm/pull/49372)
  [Bugfix] Respect declared attention contract for ColQwen3.5 retrievers (#49372)
  _Files: `tests/models/multimodal/pooling/test_colqwen3_5.py`, `vllm/model_executor/models/config.py`_
- **2026-07-25** [`3e74c60b9c`](https://github.com/vllm-project/vllm/commit/3e74c60b9c) [#49587](https://github.com/vllm-project/vllm/pull/49587)
  [Docs] Use `gen-files` for generated docs content (#49587)
  _Files: `.gitignore`, `.markdownlint.yaml`, `.pre-commit-config.yaml`, `docs/.nav.yml` _+30 more__
- **2026-07-25** [`d1a8ba63d9`](https://github.com/vllm-project/vllm/commit/d1a8ba63d9) [#49149](https://github.com/vllm-project/vllm/pull/49149)
  [Bugfix][MiniMax-M3] Fix token-major top-k buffer handling in Triton … (#49149)
  _Files: `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/sparse_attention.py`_
- **2026-07-25** [`fe5145765f`](https://github.com/vllm-project/vllm/commit/fe5145765f) [#48796](https://github.com/vllm-project/vllm/pull/48796)
  [Core] Keep attention backends eligible for text-only serving of prefix-LM models (#48796)
  _Files: `tests/config/test_multimodal_config.py`, `tests/models/utils.py`, `vllm/config/model.py`, `vllm/transformers_utils/model_arch_config_convertor.py`_
- **2026-07-25** [`aaaeda98dc`](https://github.com/vllm-project/vllm/commit/aaaeda98dc) [#49770](https://github.com/vllm-project/vllm/pull/49770)
  [CI] fix compile test | refactor VLLM_DISABLE_COMPILE_CACHE for tests (#49770)
  _Files: `tests/compile/passes/test_fusion_attn.py`, `tests/compile/passes/test_mla_attn_quant_fusion.py`, `tests/compile/test_compile_ranges.py`, `tests/conftest.py`_
- **2026-07-24** [`213f681f81`](https://github.com/vllm-project/vllm/commit/213f681f81) [#49768](https://github.com/vllm-project/vllm/pull/49768)
  Revert "[Perf][GLM-5.2] Blackwell decode optimizations" (#49768)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/bf16_skinny_gemm.cu`, `csrc/libtorch_stable/bf16_skinny_gemm_entry.cu`, `csrc/libtorch_stable/dsv3_fused_a_gemm.cu` _+25 more__
- **2026-07-24** [`8c13ee5735`](https://github.com/vllm-project/vllm/commit/8c13ee5735) [#49387](https://github.com/vllm-project/vllm/pull/49387)
  Add `sm_107` for Rubin (#49387)
  _Files: `CMakeLists.txt`, `cmake/external_projects/deepgemm.cmake`, `cmake/external_projects/flashmla.cmake`, `cmake/external_projects/qutlass.cmake` _+2 more__
- **2026-07-24** [`866fea2b99`](https://github.com/vllm-project/vllm/commit/866fea2b99) [#48018](https://github.com/vllm-project/vllm/pull/48018)
  [Kernel] ReplaySSM: cache SSM inputs for faster Mamba2 standard decode (#48018)
  _Files: `benchmarks/replayssm/e2e_decode_speedup.py`, `tests/kernels/mamba/test_replayssm_prefill_decode_equivalence_mamba2.py`, `tests/kernels/mamba/test_replayssm_standard_decode_mamba2.py`, `tests/kernels/mamba/utils.py` _+19 more__
- **2026-07-24** [`dd72658e7d`](https://github.com/vllm-project/vllm/commit/dd72658e7d) [#48597](https://github.com/vllm-project/vllm/pull/48597)
  [Perf][GLM-5.2] Blackwell decode optimizations (#48597)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/bf16_skinny_gemm.cu`, `csrc/libtorch_stable/bf16_skinny_gemm_entry.cu`, `csrc/libtorch_stable/dsv3_fused_a_gemm.cu` _+25 more__
- **2026-07-23** [`e18f0037a5`](https://github.com/vllm-project/vllm/commit/e18f0037a5) [#48776](https://github.com/vllm-project/vllm/pull/48776)
  [Bugfix][KV cache] Support sparse-MLA targets with SWA drafts (#48776)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-07-22** [`f3a920a076`](https://github.com/vllm-project/vllm/commit/f3a920a076) [#48993](https://github.com/vllm-project/vllm/pull/48993)
  [Core][DSV4] Compact MXFP4 indexer KV cache and packed group overlays (#48993)
  _Files: `tests/v1/core/test_contiguous_kv_packing.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-07-22** [`917fdb5bf7`](https://github.com/vllm-project/vllm/commit/917fdb5bf7) [#49467](https://github.com/vllm-project/vllm/pull/49467)
  [Bugfix] Fix DeepGEMM warmup when using `FlashInferFp8DeepGEMMDynamicBlockScaledKernel` (#49467)
  _Files: `vllm/model_executor/warmup/deep_gemm_warmup.py`_
- **2026-07-22** [`431934522b`](https://github.com/vllm-project/vllm/commit/431934522b) [#49423](https://github.com/vllm-project/vllm/pull/49423)
  [CI] Fix stale/fragile untethered kernels-root tests (#49423)
  _Files: `tests/kernels/conftest.py`, `tests/kernels/test_flex_attention.py`, `tests/kernels/test_fused_inv_rope_fp8_quant.py`, `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py` _+2 more__
- **2026-07-22** [`61a09532f2`](https://github.com/vllm-project/vllm/commit/61a09532f2) [#48914](https://github.com/vllm-project/vllm/pull/48914)
  Bump Flashinfer version to 0.6.15 (#48914)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `requirements/cuda.txt`_
- **2026-07-22** [`c79ff5f918`](https://github.com/vllm-project/vllm/commit/c79ff5f918) [#49326](https://github.com/vllm-project/vllm/pull/49326)
  [Build] Bump vllm-flash-attn to C++20-compatible commit for torch-nightly (#49326)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`_
- **2026-07-22** [`7c21548ce3`](https://github.com/vllm-project/vllm/commit/7c21548ce3) [#49297](https://github.com/vllm-project/vllm/pull/49297)
  [PD][Bugfix] Fix NIXL hybrid MLA+mamba heterogeneous TP (#49297)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py`_
- **2026-07-22** [`060b5f61dc`](https://github.com/vllm-project/vllm/commit/060b5f61dc) [#49294](https://github.com/vllm-project/vllm/pull/49294)
  [Bugfix][Attention] Ignore empty MLA context chunks during merge (#49294)
  _Files: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`, `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP2-PCP2-EP.yaml`, `tests/kernels/attention/test_merge_attn_states.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+1 more__
- **2026-07-21** [`a7d00ec051`](https://github.com/vllm-project/vllm/commit/a7d00ec051) [#48524](https://github.com/vllm-project/vllm/pull/48524)
  [Bugfix] DFlash fc sized wrong when num_target_layers != num_hidden_layers (#48524)
  _Files: `tests/v1/spec_decode/test_dflash_causality.py`, `vllm/model_executor/models/qwen3_dflash.py`, `vllm/v1/worker/gpu/spec_decode/eagle/eagle3_utils.py`_
- **2026-07-21** [`96a739289e`](https://github.com/vllm-project/vllm/commit/96a739289e) [#49016](https://github.com/vllm-project/vllm/pull/49016)
  [Bugfix] fix cutalss version upgrade bug, need update MSG new commit (#49016)
  _Files: `cmake/external_projects/fmha_sm100.cmake`, `requirements/cuda.txt`_
- **2026-07-21** [`7bb49be4d1`](https://github.com/vllm-project/vllm/commit/7bb49be4d1) [#49306](https://github.com/vllm-project/vllm/pull/49306)
  [Bugfix] Handle MLA fallback during FA4 JIT warmup (#49306)
  _Files: `vllm/model_executor/warmup/fa4_cutedsl_warmup.py`_
- **2026-07-21** [`6700813f86`](https://github.com/vllm-project/vllm/commit/6700813f86) [#44456](https://github.com/vllm-project/vllm/pull/44456)
  [3/N][KV-Cache Layout Refactor] Standardize Mamba cache; drop `get_transfer_cache_regions` (#44456)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `vllm/distributed/kv_transfer/kv_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+6 more__
- **2026-07-21** [`adfbbc1005`](https://github.com/vllm-project/vllm/commit/adfbbc1005) [#49177](https://github.com/vllm-project/vllm/pull/49177)
  Propagate Flash Attention cache configuration to Ray workers (#49177)
  _Files: `vllm/ray/ray_env.py`_
- **2026-07-21** [`72d16aee15`](https://github.com/vllm-project/vllm/commit/72d16aee15) [#49231](https://github.com/vllm-project/vllm/pull/49231)
  [CI] Exercise FA3 FP8 attention on SM90 (#49231)
  _Files: `tests/quantization/test_fp8.py`_
- **2026-07-20** [`2396a61108`](https://github.com/vllm-project/vllm/commit/2396a61108) [#45964](https://github.com/vllm-project/vllm/pull/45964)
  [Attention][MLA][DCP] Query replication for MLA decode (DeepSeek-V2/R1 + Kimi-K2.5) (#45964)
  _Files: `tests/v1/attention/test_mla_backends.py`, `vllm/envs.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/linear.py` _+2 more__
- **2026-07-20** [`642076d26c`](https://github.com/vllm-project/vllm/commit/642076d26c) [#48639](https://github.com/vllm-project/vllm/pull/48639)
  Support loading sample_from_anchor flag from speculators config (#48639)
  _Files: `vllm/transformers_utils/configs/speculators/algos.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`, `vllm/v1/worker/gpu/spec_decode/dspark/speculator.py`_
- **2026-07-20** [`4ec199b66a`](https://github.com/vllm-project/vllm/commit/4ec199b66a) [#44492](https://github.com/vllm-project/vllm/pull/44492)
  [Bugfix][Spec-Decode] Populate draft seq_lens_cpu_upper_bound for spec-decode attention metadata (#44492)
  _Files: `tests/v1/spec_decode/test_eagle_draft_attn_metadata.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`, `vllm/v1/worker/gpu/spec_decode/speculator.py`_
- **2026-07-20** [`7ca017778f`](https://github.com/vllm-project/vllm/commit/7ca017778f) [#47451](https://github.com/vllm-project/vllm/pull/47451)
  [Feat][Perf] Add new warmup infrastructure for JITs (#47451)
  _Files: `.buildkite/test_areas/model_executor.yaml`, `tests/model_executor/test_jit_warmup.py`, `vllm/config/kernel.py`, `vllm/model_executor/warmup/cutedsl_warmup.py` _+10 more__
- **2026-07-20** [`bd091079cb`](https://github.com/vllm-project/vllm/commit/bd091079cb) [#42569](https://github.com/vllm-project/vllm/pull/42569)
  [Attention] FlashAttention 4 SM100 FP8 kv cache support (#42569)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`, `docs/design/attention_backends.md`, `tests/models/quantization/test_fp8.py`, `tests/v1/attention/test_attention_backends.py` _+4 more__
- **2026-07-20** [`5c9f6557d7`](https://github.com/vllm-project/vllm/commit/5c9f6557d7) [#47641](https://github.com/vllm-project/vllm/pull/47641)
  [Hardware][CPU] Enable granite-4 model on cpu (#47641)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_vsx.hpp` _+17 more__

## MoE / Expert Parallel  (23 commits)

- **2026-07-27** [`eb290ab673`](https://github.com/vllm-project/vllm/commit/eb290ab673) [#49591](https://github.com/vllm-project/vllm/pull/49591)
  [Bugfix][CPU] Zero-pad MoE intermediate size for grouped-gemm TP alignment (#49591)
  _Files: `tests/kernels/moe/test_cpu_fused_moe.py`, `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`_
- **2026-07-27** [`c314af1abf`](https://github.com/vllm-project/vllm/commit/c314af1abf) [#48637](https://github.com/vllm-project/vllm/pull/48637)
  [CPU][Perf] INT8 Fused MoE Kernel for Arm CPUs (#48637)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_fused_moe.cpp`, `csrc/cpu/cpu_fused_moe_activations.hpp`, `csrc/cpu/cpu_fused_moe_int8.cpp` _+8 more__
- **2026-07-26** [`0111002323`](https://github.com/vllm-project/vllm/commit/0111002323) [#46340](https://github.com/vllm-project/vllm/pull/46340)
  [Kernel] TD operand loads for batched MoE GEMM (moe_mmk) on XPU (#46340)
  _Files: `tests/kernels/moe/test_batched_moe.py`, `vllm/config/kernel.py`, `vllm/model_executor/layers/fused_moe/all2all_utils.py`, `vllm/model_executor/layers/fused_moe/experts/fused_batched_moe.py` _+5 more__
- **2026-07-25** [`7fe6d3c76b`](https://github.com/vllm-project/vllm/commit/7fe6d3c76b) [#48763](https://github.com/vllm-project/vllm/pull/48763)
  [Perf] Fix moe `reduce_scatter` perf regression by removing additional comm, 5% E2E throughput gain back. (#48763)
  _Files: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/models/deepseek_v32/nvidia/mtp.py`_
- **2026-07-24** [`5d8e90a966`](https://github.com/vllm-project/vllm/commit/5d8e90a966) [#45321](https://github.com/vllm-project/vllm/pull/45321)
  [WideEP] Update NCCL to 2.30.7 to enable DeepEPv2 in the vllm/vllm-openai image (#45321)
  _Files: `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/model_runner_v2.yaml`, `docker/Dockerfile`, `docker/versions.json` _+9 more__
- **2026-07-24** [`d65acd83d8`](https://github.com/vllm-project/vllm/commit/d65acd83d8) [#49258](https://github.com/vllm-project/vllm/pull/49258)
  [Model] Support llm-compressor Inkling NVFP4 weights (#49258)
  _Files: `tests/models/inkling/test_moe_weight_layout.py`, `vllm/models/inkling/nvidia/model.py`, `vllm/models/inkling/nvidia/moe.py`_
- **2026-07-24** [`da54a5bf05`](https://github.com/vllm-project/vllm/commit/da54a5bf05) [#49654](https://github.com/vllm-project/vllm/pull/49654)
  [Docs] Fix broken anchor links in serving/pooling/MoE docs (#49654)
  _Files: `docs/design/fused_moe_modular_kernel.md`, `docs/models/pooling_models/README.md`, `docs/models/pooling_models/scoring.md`, `docs/serving/online_serving/README.md`_
- **2026-07-23** [`46f01a50ac`](https://github.com/vllm-project/vllm/commit/46f01a50ac) [#49609](https://github.com/vllm-project/vllm/pull/49609)
  [CI][Bugfix] Fix test isolation in block_int8/ptpc_fp8 MoE kernel tests (#49609)
  _Files: `tests/kernels/moe/test_block_int8.py`, `tests/kernels/moe/test_triton_moe_ptpc_fp8.py`_
- **2026-07-23** [`b0cb1da1bd`](https://github.com/vllm-project/vllm/commit/b0cb1da1bd) [#49486](https://github.com/vllm-project/vllm/pull/49486)
  [DSv4 Perf] Skip topk and router when not needed, 3.4% E2E TTFT improvement for Decode case (#49486)
  _Files: `vllm/models/deepseek_v4/attention.py`_
- **2026-07-23** [`ac36a7a1e7`](https://github.com/vllm-project/vllm/commit/ac36a7a1e7) [#48630](https://github.com/vllm-project/vllm/pull/48630)
  [MRV2][Spec Decode] Avoid rejection sampler OOM by chunking (#48630)
  _Files: `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `tests/v1/test_outputs.py`, `tests/v1/worker/test_gpu_rejection_sampler_chunking.py`, `vllm/config/model.py` _+8 more__
- **2026-07-23** [`9a698f3255`](https://github.com/vllm-project/vllm/commit/9a698f3255) [#49487](https://github.com/vllm-project/vllm/pull/49487)
  [Performance][Model] Avoid transient Inkling result allocations (performance, and OOM prevention on smaller memory configurations) (#49487)
  _Files: `vllm/models/inkling/nvidia/mlp.py`, `vllm/models/inkling/nvidia/moe.py`_
- **2026-07-23** [`b07ec92faa`](https://github.com/vllm-project/vllm/commit/b07ec92faa) [#49489](https://github.com/vllm-project/vllm/pull/49489)
  [Bugfix] Make shared NVFP4 MoE scales writable (#49489)
  _Files: `tests/quantization/test_trtllm_nvfp4_hidden_dim_padding.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`_
- **2026-07-22** [`4b594b4aa1`](https://github.com/vllm-project/vllm/commit/4b594b4aa1) [#49452](https://github.com/vllm-project/vllm/pull/49452)
  [Bugfix][CI] Fix `topk_softplus_sqrt` no-op on non-XPU platforms (#49452)
  _Files: `vllm/_custom_ops.py`_
- **2026-07-22** [`d6dbdb9b0d`](https://github.com/vllm-project/vllm/commit/d6dbdb9b0d) [#49408](https://github.com/vllm-project/vllm/pull/49408)
  [XPU] WA of topk_softplus_sqrt arg mismatch on XPU (#49408)
  _Files: `vllm/_custom_ops.py`_
- **2026-07-22** [`06da482fb4`](https://github.com/vllm-project/vllm/commit/06da482fb4) [#49395](https://github.com/vllm-project/vllm/pull/49395)
  [XPU] WA of topk_softmax arg mismatch on XPU (#49395)
  _Files: `vllm/_custom_ops.py`_
- **2026-07-22** [`ec59c1579f`](https://github.com/vllm-project/vllm/commit/ec59c1579f) [#44120](https://github.com/vllm-project/vllm/pull/44120)
  [MoE Refactor] Migrate MoeWNA16Method quantization method over to using the new MK oracle scheme. (#44120)
  _Files: `tests/quantization/test_auto_gptq.py`, `tests/quantization/test_moe_wna16.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py` _+7 more__
- **2026-07-21** [`85f638a2b8`](https://github.com/vllm-project/vllm/commit/85f638a2b8) [#48979](https://github.com/vllm-project/vllm/pull/48979)
  skip cudagraph/DP padding in topk (#48979)
  _Files: `csrc/libtorch_stable/moe/moe_ops.h`, `csrc/libtorch_stable/moe/topk_softmax_kernels.cu`, `csrc/libtorch_stable/moe/topk_softplus_sqrt_kernels.cu`, `csrc/libtorch_stable/moe/torch_bindings.cpp` _+6 more__
- **2026-07-21** [`1134545b6f`](https://github.com/vllm-project/vllm/commit/1134545b6f) [#48641](https://github.com/vllm-project/vllm/pull/48641)
  Revert "[Sampler] Stop upcasting logits to fp32 in apply_sampling_params" (#48641) (#49033)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_triton.py`, `vllm/v1/worker/gpu/sample/logit_bias.py` _+1 more__
- **2026-07-21** [`8def3cdde2`](https://github.com/vllm-project/vllm/commit/8def3cdde2) [#48917](https://github.com/vllm-project/vllm/pull/48917)
  [Bugfix] Propagate quant_config to LFM2 ShortConv projections (#48917)
  _Files: `vllm/model_executor/layers/mamba/short_conv.py`, `vllm/model_executor/models/lfm2.py`, `vllm/model_executor/models/lfm2_moe.py`_
- **2026-07-20** [`97a668152b`](https://github.com/vllm-project/vllm/commit/97a668152b) [#44214](https://github.com/vllm-project/vllm/pull/44214)
  [RL Infra][FlashInfer] Enable router replay output from FlashInfer monolithic MoE kernel (#44214)
  _Files: `tests/kernels/moe/test_routed_experts_capture_monolithic.py`, `tests/model_executor/test_routed_experts_capture.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py` _+7 more__
- **2026-07-20** [`e2d7adeb64`](https://github.com/vllm-project/vllm/commit/e2d7adeb64) [#49161](https://github.com/vllm-project/vllm/pull/49161)
  [Rust Frontend] Bump `xgrammar-structural-tag` and enable local extension (#49161)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/default/structural_tag.rs` _+16 more__
- **2026-07-20** [`0a5069e4e3`](https://github.com/vllm-project/vllm/commit/0a5069e4e3) [#48563](https://github.com/vllm-project/vllm/pull/48563)
  [Bugfix][Gemma4] Fix ModelOpt mixed-precision MoE config mapping (#48563)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/model_executor/models/gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-07-20** [`df13b5aef5`](https://github.com/vllm-project/vllm/commit/df13b5aef5) [#47122](https://github.com/vllm-project/vllm/pull/47122)
  [XPU] [MoE] add quant input when prepare for fusedmoe (#47122)
  _Files: `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`, `vllm/model_executor/layers/fused_moe/topk_weight_and_reduce.py`, `vllm/model_executor/layers/fused_moe/utils.py`_

## CI / Build  (23 commits)

- **2026-07-27** [`afc94523c9`](https://github.com/vllm-project/vllm/commit/afc94523c9) [#49939](https://github.com/vllm-project/vllm/pull/49939)
  [XPU][CI] Use platform device in InputBatch V2 test (#49939)
  _Files: `tests/v1/worker/test_gpu_input_batch_v2.py`_
- **2026-07-27** [`ff6173997d`](https://github.com/vllm-project/vllm/commit/ff6173997d) [#49895](https://github.com/vllm-project/vllm/pull/49895)
  [CI] Add kimi and k3 auto-labeling rules (#49895)
  _Files: `.github/mergify.yml`, `.github/workflows/issue_autolabel.yml`_
- **2026-07-26** [`0934b26790`](https://github.com/vllm-project/vllm/commit/0934b26790) [#49901](https://github.com/vllm-project/vllm/pull/49901)
  [CI/Build] Refresh tags before building macOS wheel (#49901)
  _Files: `.buildkite/scripts/build-macos-wheel.sh`_
- **2026-07-26** [`0164022c90`](https://github.com/vllm-project/vllm/commit/0164022c90) [#49853](https://github.com/vllm-project/vllm/pull/49853)
  [CI] Fix speech correctness check rejecting improved WER (#49853)
  _Files: `tests/entrypoints/speech_to_text/correctness/test_transcription_api_correctness.py`_
- **2026-07-26** [`2e860de498`](https://github.com/vllm-project/vllm/commit/2e860de498) [#49782](https://github.com/vllm-project/vllm/pull/49782)
  [Doc] Add compile cache volume example to the Docker deployment page (#49782)
  _Files: `docs/deployment/docker.md`_
- **2026-07-26** [`b153ae6089`](https://github.com/vllm-project/vllm/commit/b153ae6089) [#49651](https://github.com/vllm-project/vllm/pull/49651)
  [XPU][CI] add heterogeneous TP UT (#49651)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`_
- **2026-07-26** [`7a6a5b3667`](https://github.com/vllm-project/vllm/commit/7a6a5b3667) [#49773](https://github.com/vllm-project/vllm/pull/49773)
  [CI] Compute speech WER directly with jiwer (#49773)
  _Files: `tests/entrypoints/speech_to_text/correctness/test_transcription_api_correctness.py`_
- **2026-07-25** [`9a50464698`](https://github.com/vllm-project/vllm/commit/9a50464698) [#49800](https://github.com/vllm-project/vllm/pull/49800)
  [CI] Stop flaky test from downloading model every time (#49800)
  _Files: `tests/model_executor/model_loader/instanttensor_loader/test_weight_utils.py`_
- **2026-07-24** [`9e6746b3c7`](https://github.com/vllm-project/vllm/commit/9e6746b3c7) [#49749](https://github.com/vllm-project/vllm/pull/49749)
  [CI] Stabilize memory-sensitive compile and structured output tests (#49749)
  _Files: `tests/compile/fullgraph/test_basic_correctness.py`, `tests/entrypoints/llm/test_struct_output_generate.py`_
- **2026-07-24** [`7e51939e25`](https://github.com/vllm-project/vllm/commit/7e51939e25) [#49508](https://github.com/vllm-project/vllm/pull/49508)
  [CI] Avoid unnecessary Hugging Face metadata requests (#49508)
  _Files: `vllm/config/model.py`, `vllm/model_executor/model_loader/default_loader.py`_
- **2026-07-24** [`9863102ed9`](https://github.com/vllm-project/vllm/commit/9863102ed9) [#49509](https://github.com/vllm-project/vllm/pull/49509)
  [CI] Reuse loaded config for cached tokenizer (#49509)
  _Files: `tests/tokenizers_/test_registry.py`, `vllm/tokenizers/registry.py`_
- **2026-07-24** [`2ac125123a`](https://github.com/vllm-project/vllm/commit/2ac125123a) [#49513](https://github.com/vllm-project/vllm/pull/49513)
  [CI] Use explicit devices in IR tests (#49513)
  _Files: `tests/kernels/ir/test_layernorm.py`, `vllm/ir/ops/layernorm.py`_
- **2026-07-23** [`c6fe94b4d5`](https://github.com/vllm-project/vllm/commit/c6fe94b4d5) [#49606](https://github.com/vllm-project/vllm/pull/49606)
  [CI] Bump PyTorch Compilation Unit Tests timeout to 150 min (#49606)
  _Files: `.buildkite/test_areas/pytorch.yaml`_
- **2026-07-23** [`f00efc5265`](https://github.com/vllm-project/vllm/commit/f00efc5265) [#49510](https://github.com/vllm-project/vllm/pull/49510)
  [CI] Isolate cudagraph tests in child processes (#49510)
  _Files: `tests/v1/cudagraph/test_cudagraph_mode.py`_
- **2026-07-23** [`f83de6d44c`](https://github.com/vllm-project/vllm/commit/f83de6d44c) [#49523](https://github.com/vllm-project/vllm/pull/49523)
  [CPU][Docs] Update docs and dockerfile for s390x (#49523)
  _Files: `docker/Dockerfile.s390x`, `docs/getting_started/installation/cpu.md`, `docs/getting_started/installation/cpu.s390x.inc.md`_
- **2026-07-22** [`b44311b6ef`](https://github.com/vllm-project/vllm/commit/b44311b6ef) [#49388](https://github.com/vllm-project/vllm/pull/49388)
  [CI] stabilize GDN prefill CuTeDSL test (#49388)
  _Files: `tests/kernels/mamba/test_gdn_prefill_cutedsl.py`_
- **2026-07-22** [`b0d7875180`](https://github.com/vllm-project/vllm/commit/b0d7875180) [#49450](https://github.com/vllm-project/vllm/pull/49450)
  [CI] Increase timeout of pytorch-compilation-unit-tests (#49450)
  _Files: `.buildkite/test_areas/pytorch.yaml`_
- **2026-07-22** [`1a659a0c37`](https://github.com/vllm-project/vllm/commit/1a659a0c37) [#49431](https://github.com/vllm-project/vllm/pull/49431)
  Upgrade tpu-inference to v0.25.0 (#49431)
  _Files: `requirements/tpu.txt`_
- **2026-07-21** [`1dca300653`](https://github.com/vllm-project/vllm/commit/1dca300653) [#49339](https://github.com/vllm-project/vllm/pull/49339)
  [CI] Fix and wire encoder/manager cudagraph unit tests (#49339)
  _Files: `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/misc.yaml`, `tests/v1/cudagraph/test_encoder_cudagraph.py`_
- **2026-07-21** [`fca252d59e`](https://github.com/vllm-project/vllm/commit/fca252d59e) [#49351](https://github.com/vllm-project/vllm/pull/49351)
  [CI][Bugfix] Reduce max_model_len in OOT embedding test to fix KV-cache OOM on small GPUs (#49351)
  _Files: `tests/plugins_tests/test_oot_registration_offline.py`_
- **2026-07-21** [`5aab491bc9`](https://github.com/vllm-project/vllm/commit/5aab491bc9) [#49325](https://github.com/vllm-project/vllm/pull/49325)
  [CI] Wire tests/models/inkling into a B200 job (#49325)
  _Files: `.buildkite/test_areas/models_basic.yaml`_
- **2026-07-21** [`97a98006b0`](https://github.com/vllm-project/vllm/commit/97a98006b0) [#47879](https://github.com/vllm-project/vllm/pull/47879)
  Update qutlass cmake for stable abi (#47879)
  _Files: `cmake/external_projects/qutlass.cmake`, `vllm/_custom_ops.py`_
- **2026-07-20** [`2730b657c4`](https://github.com/vllm-project/vllm/commit/2730b657c4) [#49108](https://github.com/vllm-project/vllm/pull/49108)
  [Bugfix] Fix broken NVVM caused by CuteDSL 4.6.0 (#49108)
  _Files: `.buildkite/test_areas/kernels.yaml`, `vllm/cute_utils/_tcgen05.py`_

## KV Cache / Offload  (17 commits)

- **2026-07-27** [`77cba0259f`](https://github.com/vllm-project/vllm/commit/77cba0259f) [#48123](https://github.com/vllm-project/vllm/pull/48123)
  [KV Offloading] Per-request tier filtering with TierFilter/TierMatcher (#48123)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_offload/cpu/test_manager.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py` _+12 more__
- **2026-07-27** [`d742856610`](https://github.com/vllm-project/vllm/commit/d742856610) [#49502](https://github.com/vllm-project/vllm/pull/49502)
  [3/N][Core][KV Connector] Support reliable partial-tail KV offload for sub-block prompts (#49502)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py` _+9 more__
- **2026-07-27** [`53397fbfac`](https://github.com/vllm-project/vllm/commit/53397fbfac) [#49823](https://github.com/vllm-project/vllm/pull/49823)
  [Bugfix][KV Offload][P2P] Fix EngineCore crash reconnecting to a reaped peer (#49823)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_zmq_transport.py`, `vllm/v1/kv_offload/tiering/p2p/control/base.py`, `vllm/v1/kv_offload/tiering/p2p/control/zmq.py`_
- **2026-07-26** [`b68d7ef262`](https://github.com/vllm-project/vllm/commit/b68d7ef262) [#49438](https://github.com/vllm-project/vllm/pull/49438)
  [Bugfix][KV Offload] Namespace auto cache dtype by effective dtype (#49438)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/offloading/config.py`_
- **2026-07-26** [`7154856f3d`](https://github.com/vllm-project/vllm/commit/7154856f3d) [#47791](https://github.com/vllm-project/vllm/pull/47791)
  [Bugfix] Fix handling 5D KV cache in kv_postprocess_layout_on_receive (#47791)
  _Files: `vllm/distributed/kv_transfer/kv_connector/utils.py`_
- **2026-07-26** [`3f1d40960f`](https://github.com/vllm-project/vllm/commit/3f1d40960f) [#49285](https://github.com/vllm-project/vllm/pull/49285)
  [KV Offload] Fix num_tokens_after_batch for different termination types (#49285)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-07-26** [`5559679229`](https://github.com/vllm-project/vllm/commit/5559679229) [#49052](https://github.com/vllm-project/vllm/pull/49052)
  [Bugfix][KV Offload] Bound unaligned SWA loads by physical GPU blocks (#49052)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-07-26** [`7a29a3c54c`](https://github.com/vllm-project/vllm/commit/7a29a3c54c) [#49440](https://github.com/vllm-project/vllm/pull/49440)
  [Bugfix][KV Offload] Namespace persistent cache by model runner (#49440)
  _Files: `tests/v1/kv_offload/test_file_mapper.py`, `vllm/v1/kv_offload/file_mapper.py`_
- **2026-07-25** [`d30b1ecd1b`](https://github.com/vllm-project/vllm/commit/d30b1ecd1b) [#49671](https://github.com/vllm-project/vllm/pull/49671)
  [Bugfix][KV Offloading] Defer request finalization until final store (#49671)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-07-25** [`a82f1b388f`](https://github.com/vllm-project/vllm/commit/a82f1b388f) [#48017](https://github.com/vllm-project/vllm/pull/48017)
  [Perf][V1] Skip LRU hash-split in free_blocks when prefix caching is off (#48017)
  _Files: `vllm/v1/core/block_pool.py`_
- **2026-07-24** [`89f6aa3a9e`](https://github.com/vllm-project/vllm/commit/89f6aa3a9e) [#49734](https://github.com/vllm-project/vllm/pull/49734)
  [KV Offload][CI] Fall back to buffered I/O without O_DIRECT; fix flaky api-server test (#49734)
  _Files: `tests/entrypoints/unit_tests/_api_server_spawn_workers.py`, `tests/entrypoints/unit_tests/test_api_server_process_manager.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `vllm/v1/kv_offload/tiering/fs/io.py` _+1 more__
- **2026-07-24** [`275556c35c`](https://github.com/vllm-project/vllm/commit/275556c35c) [#49623](https://github.com/vllm-project/vllm/pull/49623)
  [Bugfix] Detect mixed precision in packed KV cache specs (#49623)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/kv_cache_interface.py`_
- **2026-07-21** [`94ed0bf4e0`](https://github.com/vllm-project/vllm/commit/94ed0bf4e0) [#49146](https://github.com/vllm-project/vllm/pull/49146)
  [Bugfix][KV Offloading] Handle queued request aborts without allocated KV blocks (#49146)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-07-20** [`fbfe58133d`](https://github.com/vllm-project/vllm/commit/fbfe58133d) [#48911](https://github.com/vllm-project/vllm/pull/48911)
  [Bugfix][KV Offload] Preserve reachable tails for hybrid SWA groups (#48911)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-07-20** [`f007cceb42`](https://github.com/vllm-project/vllm/commit/f007cceb42) [#48679](https://github.com/vllm-project/vllm/pull/48679)
  [KV Offload] Support self-describing KV events with TieringOffloadingSpec (#48679)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py` _+2 more__
- **2026-07-20** [`5245c80564`](https://github.com/vllm-project/vllm/commit/5245c80564) [#49100](https://github.com/vllm-project/vllm/pull/49100)
  [Doc] Document blocks_per_chunk in the KV offloading guide (#49100)
  _Files: `docs/features/kv_offloading_usage.md`_
- **2026-07-20** [`9bc266d923`](https://github.com/vllm-project/vllm/commit/9bc266d923) [#49071](https://github.com/vllm-project/vllm/pull/49071)
  [Bugfix][KV Offload] Propagate EAGLE mode to SimpleCPU coordinator (#49071)
  _Files: `vllm/v1/simple_kv_offload/manager.py`_

## Multimodal  (17 commits)

- **2026-07-25** [`70009fb934`](https://github.com/vllm-project/vllm/commit/70009fb934) [#46837](https://github.com/vllm-project/vllm/pull/46837)
  [MM][CG] Support ViT CUDA Graph for Gemma-4 (#46837)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-07-25** [`6b0103d1c9`](https://github.com/vllm-project/vllm/commit/6b0103d1c9) [#49822](https://github.com/vllm-project/vllm/pull/49822)
  [CI] Stabilize Pooling Rerank Equivalence Test (#49822)
  _Files: `tests/entrypoints/pooling/scoring/test_cross_encoder_online_vision.py`_
- **2026-07-25** [`b9b6306ebe`](https://github.com/vllm-project/vllm/commit/b9b6306ebe) [#39330](https://github.com/vllm-project/vllm/pull/39330)
  feat[vLLM × v5]: Add audio support for the Transformers backend (#39330)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/generation/test_transformers_audio.py`, `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_transformers_audio.py` _+4 more__
- **2026-07-25** [`94682b79f4`](https://github.com/vllm-project/vllm/commit/94682b79f4) [#49753](https://github.com/vllm-project/vllm/pull/49753)
  [multimodal] Make PyNvVideoCodec decoder concurrency configurable (#49753)
  _Files: `docs/features/multimodal_inputs.md`, `tests/multimodal/media/test_video.py`, `tests/multimodal/test_gpu_ipc_memory.py`, `tests/multimodal/test_video.py` _+3 more__
- **2026-07-24** [`c064fa52b6`](https://github.com/vllm-project/vllm/commit/c064fa52b6) [#49484](https://github.com/vllm-project/vllm/pull/49484)
  Fix GLM-4.1V video placeholder token ID handling. (#49484)
  _Files: `tests/models/multimodal/processing/test_glm4_1v.py`, `vllm/model_executor/models/glm4_1v.py`_
- **2026-07-24** [`d02df748bf`](https://github.com/vllm-project/vllm/commit/d02df748bf) [#48973](https://github.com/vllm-project/vllm/pull/48973)
  [Bugfix] Accept RFC 2397 parameters in base64 data URLs (#48973)
  _Files: `tests/multimodal/media/test_connector.py`, `vllm/multimodal/media/connector.py`_
- **2026-07-23** [`75ccdf3145`](https://github.com/vllm-project/vllm/commit/75ccdf3145) [#48155](https://github.com/vllm-project/vllm/pull/48155)
  [Core] Update PyTorch to 2.13.0, torchvision to 0.28.0, triton to 3.7.1 (#48155)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-compatibility-test.sh`, `CMakeLists.txt`, `docker/Dockerfile`, `docker/versions.json` _+11 more__
- **2026-07-23** [`80c7683923`](https://github.com/vllm-project/vllm/commit/80c7683923) [#49477](https://github.com/vllm-project/vllm/pull/49477)
  [Perf] Defer MM embeds loading off the event loop (#49477)
  _Files: `vllm/entrypoints/chat_utils.py`, `vllm/multimodal/media/connector.py`_
- **2026-07-22** [`2dc5a72e7e`](https://github.com/vllm-project/vllm/commit/2dc5a72e7e) [#49400](https://github.com/vllm-project/vllm/pull/49400)
  [Bugfix][Renderer] Rebuild vision chunk UUIDs in async render path (#49400)
  _Files: `vllm/renderers/hf.py`_
- **2026-07-22** [`2f75e7f712`](https://github.com/vllm-project/vllm/commit/2f75e7f712) [#49374](https://github.com/vllm-project/vllm/pull/49374)
  [CI] Increase timeouts for jobs exceeding current limits (#49374)
  _Files: `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/entrypoints.yaml` _+4 more__
- **2026-07-22** [`1750e443f2`](https://github.com/vllm-project/vllm/commit/1750e443f2) [#49322](https://github.com/vllm-project/vllm/pull/49322)
  [Misc] Move PyNvVideoCodec stuff out of gpu worker (#49322)
  _Files: `tests/config/test_multimodal_config.py`, `tests/multimodal/test_gpu_ipc_memory.py`, `tests/v1/worker/test_gpu_worker.py`, `vllm/config/multimodal.py` _+2 more__
- **2026-07-21** [`33178f9006`](https://github.com/vllm-project/vllm/commit/33178f9006) [#49292](https://github.com/vllm-project/vllm/pull/49292)
  Fix Qwen3-VL M-RoPE on the Transformers modeling backend (grids + compile) (#49292)
  _Files: `vllm/model_executor/models/transformers/multimodal.py`_
- **2026-07-21** [`4d30c510ce`](https://github.com/vllm-project/vllm/commit/4d30c510ce) [#49190](https://github.com/vllm-project/vllm/pull/49190)
  [bugfix] Fix Cosmos3 Edge checkpoint weights filtering, video loading, prompt expansion (#49190)
  _Files: `tests/models/multimodal/processing/test_cosmos3_edge.py`, `tests/models/multimodal/test_mapping.py`, `tests/multimodal/test_video.py`, `vllm/model_executor/models/cosmos3_edge.py` _+1 more__
- **2026-07-21** [`ea0e9c8f2e`](https://github.com/vllm-project/vllm/commit/ea0e9c8f2e) [#47985](https://github.com/vllm-project/vllm/pull/47985)
  [MRV2] Add encoder cache profiling implementation (#47985)
  _Files: `vllm/multimodal/encoder_budget.py`, `vllm/v1/worker/gpu/mm/encoder_cache.py`, `vllm/v1/worker/gpu/mm/encoder_runner.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-07-21** [`e78a0c8e59`](https://github.com/vllm-project/vllm/commit/e78a0c8e59) [#49148](https://github.com/vllm-project/vllm/pull/49148)
  [XPU][Doc] Update XPU docker image documents (#49148)
  _Files: `README.md`, `docs/getting_started/installation/gpu.xpu.inc.md`, `docs/getting_started/quickstart.md`_
- **2026-07-20** [`15cb8e140d`](https://github.com/vllm-project/vllm/commit/15cb8e140d) [#49159](https://github.com/vllm-project/vllm/pull/49159)
  [Multimodal] Allow keeping original image mode for ImageIO (#49159)
  _Files: `tests/multimodal/media/test_connector.py`, `tests/multimodal/media/test_image.py`, `vllm/multimodal/media/connector.py`, `vllm/multimodal/media/image.py` _+1 more__
- **2026-07-20** [`f1f1259692`](https://github.com/vllm-project/vllm/commit/f1f1259692) [#48781](https://github.com/vllm-project/vllm/pull/48781)
  [Rust Frontend] Use zero-copy slicing for multimodal tensors (#48781)
  _Files: `rust/src/chat/src/multimodal/item.rs`, `rust/src/chat/src/multimodal/tensor.rs`, `rust/src/chat/src/multimodal/video.rs`, `rust/src/engine-core-client/src/protocol/tensor.rs`_

## Scheduler / Engine  (16 commits)

- **2026-07-27** [`fd9d2ede6f`](https://github.com/vllm-project/vllm/commit/fd9d2ede6f) [#49944](https://github.com/vllm-project/vllm/pull/49944)
  [Rust Frontend] Keep `--max-model-len` engine-owned (#49944)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/managed-engine/src/cli.rs`_
- **2026-07-27** [`29fdeab254`](https://github.com/vllm-project/vllm/commit/29fdeab254) [#49422](https://github.com/vllm-project/vllm/pull/49422)
  [XPU][CI] Add more test cases in Intel GPU CI (#49422)
  _Files: `.buildkite/intel_jobs/benchmarks_intel.yaml`, `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/model_executor_intel.yaml`, `.buildkite/intel_jobs/model_runner_v2_intel.yaml` _+1 more__
- **2026-07-27** [`8040ef2426`](https://github.com/vllm-project/vllm/commit/8040ef2426) [#49754](https://github.com/vllm-project/vllm/pull/49754)
  [Frontend] expose stream_interval as req sampling param (#49754)
  _Files: `tests/v1/engine/test_output_processor.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`, `vllm/sampling_params.py` _+1 more__
- **2026-07-25** [`26d725c334`](https://github.com/vllm-project/vllm/commit/26d725c334) [#49803](https://github.com/vllm-project/vllm/pull/49803)
  [Model] Add VaultGemma via Transformers modeling backend (#49803)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/models/qwen2.py` _+2 more__
- **2026-07-24** [`453f01783d`](https://github.com/vllm-project/vllm/commit/453f01783d) [#49124](https://github.com/vllm-project/vllm/pull/49124)
  [UX] Improve data-parallel launch validation (#49124)
  _Files: `vllm/engine/arg_utils.py`_
- **2026-07-24** [`833483f357`](https://github.com/vllm-project/vllm/commit/833483f357) [#48218](https://github.com/vllm-project/vllm/pull/48218)
  Encoder cache extension hooks (#48218)
  _Files: `tests/v1/worker/test_gpu_model_runner_mm_gather.py`, `vllm/config/__init__.py`, `vllm/config/ec_manager_config.py`, `vllm/config/vllm.py` _+4 more__
- **2026-07-23** [`0416dab275`](https://github.com/vllm-project/vllm/commit/0416dab275) [#44993](https://github.com/vllm-project/vllm/pull/44993)
  [Bugfix][Structured Output][Spec Decode] Advance grammar across reasoning boundary (#44993)
  _Files: `tests/v1/structured_output/test_reasoning_structured_output.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/structured_output/__init__.py`_
- **2026-07-23** [`1ad84fea86`](https://github.com/vllm-project/vllm/commit/1ad84fea86) [#49391](https://github.com/vllm-project/vllm/pull/49391)
  [Bugfix][Spec Decode] Select earliest-completing stop string in check_stop_strings (#49391)
  _Files: `tests/detokenizer/test_check_stop_strings.py`, `vllm/v1/engine/detokenizer.py`_
- **2026-07-23** [`12213c6795`](https://github.com/vllm-project/vllm/commit/12213c6795) [#47312](https://github.com/vllm-project/vllm/pull/47312)
  [Bugfix] handle grammar compilation failures to avoid engine crash (#47312)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/interface.py`, `vllm/v1/core/sched/scheduler.py` _+3 more__
- **2026-07-23** [`229e01e9e1`](https://github.com/vllm-project/vllm/commit/229e01e9e1) [#48425](https://github.com/vllm-project/vllm/pull/48425)
  [BugFix] Handle per-group prefix-hit divergence for hybrid models with KV connector (#48425)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/core/kv_cache_manager.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-07-22** [`3de4b2bf3c`](https://github.com/vllm-project/vllm/commit/3de4b2bf3c) [#48748](https://github.com/vllm-project/vllm/pull/48748)
  [Bugfix][Parser] Fix special tokens (EOS/BOS) leaking into reasoning content (#48748)
  _Files: `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_parser_engine.py`, `vllm/parser/engine/streaming_parser_engine.py`_
- **2026-07-22** [`a1c15bcb0f`](https://github.com/vllm-project/vllm/commit/a1c15bcb0f) [#49356](https://github.com/vllm-project/vllm/pull/49356)
  [CI][Bugfix] Fix and wire streaming-input tests (#49356)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/v1/streaming_input/test_gpu_model_runner_streaming.py`, `tests/v1/streaming_input/test_gpu_model_runner_v2_streaming.py`, `tests/v1/streaming_input/test_scheduler_streaming.py`_
- **2026-07-21** [`8950394e0a`](https://github.com/vllm-project/vllm/commit/8950394e0a) [#48860](https://github.com/vllm-project/vllm/pull/48860)
  [Bugfix] Prefix-cache metrics double-counted when a KV connector defers requests (#48860)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `tests/v1/kv_connector/unit/utils.py`, `vllm/v1/core/kv_cache_manager.py` _+1 more__
- **2026-07-21** [`f25953cc59`](https://github.com/vllm-project/vllm/commit/f25953cc59) [#49113](https://github.com/vllm-project/vllm/pull/49113)
  [Bugfix][Rust Frontend] Handle zero-column logprobs payloads without panicking (#49113)
  _Files: `rust/src/engine-core-client/src/protocol/logprobs.rs`, `rust/src/engine-core-client/src/protocol/logprobs/tests.rs`_
- **2026-07-21** [`6bcda970fd`](https://github.com/vllm-project/vllm/commit/6bcda970fd) [#49129](https://github.com/vllm-project/vllm/pull/49129)
  [CI][NIXL] Isolate concurrent engine internal ports (#49129)
  _Files: `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`_
- **2026-07-21** [`1940c8441e`](https://github.com/vllm-project/vllm/commit/1940c8441e) [#48992](https://github.com/vllm-project/vllm/pull/48992)
  [Rust Frontend][gRPC] Add engine-aware health reporting (#48992)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs` _+5 more__

## Quantization  (15 commits)

- **2026-07-27** [`5d07e268b1`](https://github.com/vllm-project/vllm/commit/5d07e268b1) [#47514](https://github.com/vllm-project/vllm/pull/47514)
  [Quantization][INC]Add MXFP8 Linear Support (#47514)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/inc.py`, `vllm/model_executor/layers/quantization/inc/schemes/__init__.py`, `vllm/model_executor/layers/quantization/inc/schemes/factory.py` _+3 more__
- **2026-07-27** [`8de50e46d4`](https://github.com/vllm-project/vllm/commit/8de50e46d4) [#49376](https://github.com/vllm-project/vllm/pull/49376)
  [Docs] Document NVFP4 GEMM kernel selection and Marlin weight-only fallback (#49376)
  _Files: `docs/features/quantization/modelopt.md`_
- **2026-07-26** [`48ebd6f2f1`](https://github.com/vllm-project/vllm/commit/48ebd6f2f1) [#49226](https://github.com/vllm-project/vllm/pull/49226)
  [Bugfix][KVConnector] Disable cross-layer KV blocks for per-token-head quant (#49226)
  _Files: `vllm/v1/worker/kv_connector_model_runner_mixin.py`_
- **2026-07-24** [`5c5434e2d8`](https://github.com/vllm-project/vllm/commit/5c5434e2d8) [#49693](https://github.com/vllm-project/vllm/pull/49693)
  Remove Quantization test parallelism (#49693)
  _Files: `.buildkite/test_areas/quantization.yaml`_
- **2026-07-24** [`bf27e34ebb`](https://github.com/vllm-project/vllm/commit/bf27e34ebb) [#41276](https://github.com/vllm-project/vllm/pull/41276)
  [CompressedTensors] DeepSeek4 CT Quantization Support (#41276)
  _Files: `vllm/models/deepseek_v4/nvidia/ops/o_proj.py`_
- **2026-07-23** [`0e36e3bbd1`](https://github.com/vllm-project/vllm/commit/0e36e3bbd1) [#49512](https://github.com/vllm-project/vllm/pull/49512)
  [CI] Use explicit devices in quantization tests (#49512)
  _Files: `tests/kernels/quantization/test_block_int8.py`, `tests/kernels/quantization/test_int8_kernel.py`_
- **2026-07-23** [`c8db00b16c`](https://github.com/vllm-project/vllm/commit/c8db00b16c) [#48816](https://github.com/vllm-project/vllm/pull/48816)
  Fix GPTQ quantized Qwen3.5 MTP weight loading with spec decode (#48816)
  _Files: `vllm/model_executor/models/qwen3_5_mtp.py`_
- **2026-07-22** [`191146dba5`](https://github.com/vllm-project/vllm/commit/191146dba5) [#49492](https://github.com/vllm-project/vllm/pull/49492)
  Add quantization label automation (#49492)
  _Files: `.github/mergify.yml`, `.github/workflows/issue_autolabel.yml`_
- **2026-07-22** [`910cc8543a`](https://github.com/vllm-project/vllm/commit/910cc8543a) [#49427](https://github.com/vllm-project/vllm/pull/49427)
  [Bugfix] Restore `gather_and_maybe_dequant_cache` OOB guard (#49427)
  _Files: `csrc/libtorch_stable/cache_kernels.cu`, `tests/kernels/test_cache_kernels.py`_
- **2026-07-21** [`47f1b47a73`](https://github.com/vllm-project/vllm/commit/47f1b47a73) [#49241](https://github.com/vllm-project/vllm/pull/49241)
  Ci/add laguna xs gsm8k (#49241)
  _Files: `tests/evals/gsm8k/configs/Laguna-XS.2-NVFP4.yaml`, `tests/evals/gsm8k/configs/models-blackwell.txt`_
- **2026-07-21** [`0d9210a502`](https://github.com/vllm-project/vllm/commit/0d9210a502) [#47268](https://github.com/vllm-project/vllm/pull/47268)
  Fixes non-coalesced HBM access in marlin_int4_fp8_preprocess_kernel_awq (#47268)
  _Files: `csrc/libtorch_stable/quantization/marlin/marlin_int4_fp8_preprocess.cu`_
- **2026-07-20** [`9dd62d80ab`](https://github.com/vllm-project/vllm/commit/9dd62d80ab) [#48952](https://github.com/vllm-project/vllm/pull/48952)
  Cosmos3 FP8 ModelOpt/Diffusers remapping (#48952)
  _Files: `tests/models/multimodal/test_mapping.py`, `vllm/model_executor/models/cosmos3.py`_
- **2026-07-20** [`8ce53a616e`](https://github.com/vllm-project/vllm/commit/8ce53a616e) [#47574](https://github.com/vllm-project/vllm/pull/47574)
  [Bugfix] Zero new KV blocks for quantized + sliding-window hybrid caches (#47574)
  _Files: `vllm/v1/kv_cache_interface.py`_
- **2026-07-20** [`823eaf667d`](https://github.com/vllm-project/vllm/commit/823eaf667d) [#48334](https://github.com/vllm-project/vllm/pull/48334)
  [XPU] FP8 o_proj with fp8_bmm and load-time scale transpose (#48334)
  _Files: `vllm/_xpu_ops.py`, `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`, `vllm/models/deepseek_v4/xpu/model.py` _+1 more__
- **2026-07-20** [`1dcbbd9cac`](https://github.com/vllm-project/vllm/commit/1dcbbd9cac) [#43024](https://github.com/vllm-project/vllm/pull/43024)
  [CI] Move compatible 1xL4 jobs to H200 35GB MIG (#43024)
  _Files: `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/misc.yaml` _+13 more__

## Models  (14 commits)

- **2026-07-26** [`21fd9e85a0`](https://github.com/vllm-project/vllm/commit/21fd9e85a0) [#45429](https://github.com/vllm-project/vllm/pull/45429)
  [Model] Support top_k and top_p sampling for DiffusionGemma (#45429)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-07-26** [`30b0714031`](https://github.com/vllm-project/vllm/commit/30b0714031) [#49531](https://github.com/vllm-project/vllm/pull/49531)
  [Perf] DeepSeek-OCR-2 TTFT Optimize (#49531)
  _Files: `vllm/model_executor/models/deepencoder2.py`_
- **2026-07-25** [`33ef67e9fb`](https://github.com/vllm-project/vllm/commit/33ef67e9fb) [#49403](https://github.com/vllm-project/vllm/pull/49403)
  [BugFix] Increase the max supported duration for MOSS-TD (#49403)
  _Files: `vllm/model_executor/models/moss_transcribe_diarize.py`_
- **2026-07-25** [`dbcc1cdd0a`](https://github.com/vllm-project/vllm/commit/dbcc1cdd0a) [#49786](https://github.com/vllm-project/vllm/pull/49786)
  [Model] Remove Ouro (#49786)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/ouro.py`, `vllm/model_executor/models/registry.py`_
- **2026-07-25** [`190be7dad2`](https://github.com/vllm-project/vllm/commit/190be7dad2) [#49781](https://github.com/vllm-project/vllm/pull/49781)
  [Docs] Fix confusing docstring indentation in nemotron_h.py (#49781)
  _Files: `vllm/model_executor/models/nemotron_h.py`_
- **2026-07-24** [`972848f276`](https://github.com/vllm-project/vllm/commit/972848f276) [#49704](https://github.com/vllm-project/vllm/pull/49704)
  [Bugfix] Support non-uniform page sizes in KVBlockZeroer (#49704)
  _Files: `tests/v1/worker/test_kv_block_zeroer.py`, `vllm/model_executor/warmup/qwen_triton_warmup.py`, `vllm/v1/worker/utils.py`_
- **2026-07-24** [`7bdf8cc37c`](https://github.com/vllm-project/vllm/commit/7bdf8cc37c) [#48769](https://github.com/vllm-project/vllm/pull/48769)
  [Bugfix] Fix humming kernel crash when layer.has_bias is None (#48769)
  _Files: `vllm/model_executor/models/hy_v3.py`_
- **2026-07-23** [`4080263bb2`](https://github.com/vllm-project/vllm/commit/4080263bb2) [#49485](https://github.com/vllm-project/vllm/pull/49485)
  [Bugfix][Model] Remove SciPy dependency from Inkling scale planning (#49485)
  _Files: `tests/models/inkling/test_contract_validation.py`, `vllm/models/inkling/common/towers.py`_
- **2026-07-22** [`37e370fe93`](https://github.com/vllm-project/vllm/commit/37e370fe93) [#48957](https://github.com/vllm-project/vllm/pull/48957)
  [DSv4 Perf] Skip empty c128 kernel launch, around 2x kernel performance improvement. (#48957)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `vllm/models/deepseek_v4/compressor.py`_
- **2026-07-21** [`b8fb56d970`](https://github.com/vllm-project/vllm/commit/b8fb56d970) [#49243](https://github.com/vllm-project/vllm/pull/49243)
  [CI] Add gemma-4-E4B-it-assistant to CI gsm8k for GemmaMTP (#49243)
  _Files: `tests/evals/gsm8k/configs/gemma-4-E4B-it-qat-mobile-ct.yaml`_
- **2026-07-21** [`5812e1a66b`](https://github.com/vllm-project/vllm/commit/5812e1a66b) [#41653](https://github.com/vllm-project/vllm/pull/41653)
  [Test] Add DeepSeek MTP parallel-load tests (#41653)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `tests/v1/e2e/spec_decode/test_mtp_parallel_load.py`_
- **2026-07-21** [`c67650f04b`](https://github.com/vllm-project/vllm/commit/c67650f04b) [#45991](https://github.com/vllm-project/vllm/pull/45991)
  [XPU][DeepSeekV4]Add DeepSeek-V4 fuse_index_q SYCL kernel path (#45991)
  _Files: `vllm/_xpu_ops.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`_
- **2026-07-21** [`3e0c887511`](https://github.com/vllm-project/vllm/commit/3e0c887511) [#47298](https://github.com/vllm-project/vllm/pull/47298)
  [Bugfix] Fix Ovis2_5 special tokens for transformers v5 (#47298)
  _Files: `vllm/model_executor/models/ovis2_5.py`, `vllm/transformers_utils/processors/ovis2_5.py`_
- **2026-07-20** [`f878367898`](https://github.com/vllm-project/vllm/commit/f878367898) [#49193](https://github.com/vllm-project/vllm/pull/49193)
  [Revert][Bugfix] Restore MiniCPM-V 4.6 ViT QKV weight loader (#49193)
  _Files: `vllm/model_executor/models/minicpmv4_6.py`_

## Disaggregation / PD  (11 commits)

- **2026-07-27** [`ffc4f08c8e`](https://github.com/vllm-project/vllm/commit/ffc4f08c8e) [#46116](https://github.com/vllm-project/vllm/pull/46116)
  [Core][KV-transfer] MoRIIO: heterogeneous TP<->DP prefill/decode read routing (#46116)
  _Files: `tests/v1/kv_connector/unit/test_moriio_routing_fairness.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`_
- **2026-07-25** [`0b0bd2b5f6`](https://github.com/vllm-project/vllm/commit/0b0bd2b5f6) [#44428](https://github.com/vllm-project/vllm/pull/44428)
  [Feature] Add fault tolerance framework (simplified) for DP+EP external LB deployments (#44428)
  _Files: `.buildkite/test_areas/fault_tolerance.yaml`, `tests/test_config.py`, `tests/v1/fault_tolerance/__init__.py`, `tests/v1/fault_tolerance/test_fault_tolerance_e2e.py` _+23 more__
- **2026-07-25** [`0b1a8bb1f6`](https://github.com/vllm-project/vllm/commit/0b1a8bb1f6) [#49802](https://github.com/vllm-project/vllm/pull/49802)
  [Bugfix][CI] Fix stale Mooncake lookup expectation broken by a merge race (#49802)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`_
- **2026-07-25** [`70052fb924`](https://github.com/vllm-project/vllm/commit/70052fb924) [#49499](https://github.com/vllm-project/vllm/pull/49499)
  [Bugfix][KV Connector][Mooncake] Keep TP-sharded Mamba state out of the KV-head dedup (#49499)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-07-24** [`589a5b884b`](https://github.com/vllm-project/vllm/commit/589a5b884b) [#49221](https://github.com/vllm-project/vllm/pull/49221)
  [PD][NixlPush][Bugfix] Fix blocking handshake call on writer thread (#49221)
  _Files: `docs/design/nixl_kv_push_connector.md`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/push_worker.py`_
- **2026-07-23** [`2659467497`](https://github.com/vllm-project/vllm/commit/2659467497) [#49593](https://github.com/vllm-project/vllm/pull/49593)
  [CI][PD] Add hybrid SSM P_TP>D_TP accuracy sweep entry (#49593)
  _Files: `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh`_
- **2026-07-23** [`10c75477b0`](https://github.com/vllm-project/vllm/commit/10c75477b0) [#45224](https://github.com/vllm-project/vllm/pull/45224)
  [Bugfix][Core] shm_broadcast: bound idle reader waits and release read slots (#45224)
  _Files: `tests/distributed/test_shm_broadcast.py`, `vllm/distributed/device_communicators/shm_broadcast.py`_
- **2026-07-23** [`a76df87db8`](https://github.com/vllm-project/vllm/commit/a76df87db8) [#49481](https://github.com/vllm-project/vllm/pull/49481)
  [MooncakeStore] Re-derive full external hits on stored boundaries (#49481)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py` _+4 more__
- **2026-07-23** [`a4904ba903`](https://github.com/vllm-project/vllm/commit/a4904ba903) [#48531](https://github.com/vllm-project/vllm/pull/48531)
  [Perf][KVConnector][Mooncake] Vectorize prepare_value on the KV load path (#48531)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_prepare_values.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-07-20** [`4938d44a3b`](https://github.com/vllm-project/vllm/commit/4938d44a3b) [#47871](https://github.com/vllm-project/vllm/pull/47871)
  [CPU] fixes heterogeneous NIXL KV transfer into CPU_ATTN decode workers (#47871)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/platforms/cpu.py`_
- **2026-07-20** [`37bf988c2f`](https://github.com/vllm-project/vllm/commit/37bf988c2f) [#47295](https://github.com/vllm-project/vllm/pull/47295)
  [XPU][Bugfix] Fix GroupCoordinator device_index (#47295)
  _Files: `vllm/distributed/parallel_state.py`_

## Serving / API  (11 commits)

- **2026-07-23** [`a49d37c6b9`](https://github.com/vllm-project/vllm/commit/a49d37c6b9) [#49511](https://github.com/vllm-project/vllm/pull/49511)
  [CI] Disable reasoning in Responses smoke test (#49511)
  _Files: `tests/entrypoints/openai/responses/test_simple.py`_
- **2026-07-23** [`239fc73553`](https://github.com/vllm-project/vllm/commit/239fc73553) [#49217](https://github.com/vllm-project/vllm/pull/49217)
  [Misc] Use VLLMValidationError in chat_utils content-part validation (#49217)
  _Files: `vllm/entrypoints/chat_utils.py`_
- **2026-07-22** [`c79ad3ae21`](https://github.com/vllm-project/vllm/commit/c79ad3ae21) [#49255](https://github.com/vllm-project/vllm/pull/49255)
  [Rust Frontend][gRPC] Add abort control RPC (#49255)
  _Files: `rust/proto/vllm_grpc.proto`, `rust/src/server/src/grpc/health.rs`, `rust/src/server/src/grpc/mod.rs`, `rust/src/server/src/grpc/tests.rs` _+1 more__
- **2026-07-22** [`4809de7317`](https://github.com/vllm-project/vllm/commit/4809de7317) [#49344](https://github.com/vllm-project/vllm/pull/49344)
  [Misc] Fix terminal output logo coloring (#49344)
  _Files: `vllm/entrypoints/serve/utils/api_utils.py`_
- **2026-07-21** [`08e5067561`](https://github.com/vllm-project/vllm/commit/08e5067561) [#49359](https://github.com/vllm-project/vllm/pull/49359)
  [CI] Bump timeout of `entrypoints-integration-api-server-openai-part-2` (#49359)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/misc.yaml`_
- **2026-07-21** [`040cbf95cc`](https://github.com/vllm-project/vllm/commit/040cbf95cc) [#49214](https://github.com/vllm-project/vllm/pull/49214)
  [Misc] Use VLLMValidationError in chat completion tool and batch validators (#49214)
  _Files: `vllm/entrypoints/openai/chat_completion/protocol.py`_
- **2026-07-21** [`616c9bd0f4`](https://github.com/vllm-project/vllm/commit/616c9bd0f4) [#45839](https://github.com/vllm-project/vllm/pull/45839)
  [Frontend] Support additional sampling parameters for translation API (#45839)
  _Files: `vllm/entrypoints/speech_to_text/translation/protocol.py`_
- **2026-07-20** [`b7c20d0cfa`](https://github.com/vllm-project/vllm/commit/b7c20d0cfa) [#48938](https://github.com/vllm-project/vllm/pull/48938)
  [chore] adjust logo be more friendly to white background terminal (#48938)
  _Files: `vllm/entrypoints/serve/utils/api_utils.py`_
- **2026-07-20** [`530ee36a0d`](https://github.com/vllm-project/vllm/commit/530ee36a0d) [#49144](https://github.com/vllm-project/vllm/pull/49144)
  fix(openai): reject non-numeric logprobs with 400 instead of 500 (#49144)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat_error.py`, `tests/entrypoints/openai/completion/test_completion_error.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`_
- **2026-07-20** [`d835ad572c`](https://github.com/vllm-project/vllm/commit/d835ad572c) [#49111](https://github.com/vllm-project/vllm/pull/49111)
  [Bugfix][Rust Frontend] Map missing prompt logprobs for single-token prompts in chat and raw generate (#49111)
  _Files: `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/utils/logprobs.rs`_
- **2026-07-20** [`c01618fdc8`](https://github.com/vllm-project/vllm/commit/c01618fdc8) [#48930](https://github.com/vllm-project/vllm/pull/48930)
  [Rust][Benchmark] Integrate `vllm-bench` to `vllm-rs` & `vllm` CLI (#48930)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/bench/src/cli.rs`, `rust/src/bench/src/config.rs` _+8 more__

## Docs  (6 commits)

- **2026-07-26** [`da3a252fd1`](https://github.com/vllm-project/vllm/commit/da3a252fd1) [#48021](https://github.com/vllm-project/vllm/pull/48021)
  [KVOffload][P2P] Generic P2P secondary tier: peer lookup and serving via ParentManager (#48021)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/tiering/p2p/p2p_connector_proxy.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py` _+7 more__
- **2026-07-23** [`fc5fda105f`](https://github.com/vllm-project/vllm/commit/fc5fda105f) [#49474](https://github.com/vllm-project/vllm/pull/49474)
  [Docs] Re-add Reo.dev analytics beacon (#49474)
  _Files: `docs/mkdocs/javascript/reo.js`, `mkdocs.yaml`_
- **2026-07-21** [`0d9e60619b`](https://github.com/vllm-project/vllm/commit/0d9e60619b) [#49299](https://github.com/vllm-project/vllm/pull/49299)
  [Misc][Docs] Fix XPU compute-runtime driver link version mismatch (#49299)
  _Files: `docs/getting_started/installation/gpu.xpu.inc.md`_
- **2026-07-21** [`1d874867ea`](https://github.com/vllm-project/vllm/commit/1d874867ea) [#47212](https://github.com/vllm-project/vllm/pull/47212)
  [Misc][Docs] Fix broken protocol link in speech_to_text doc (#47212)
  _Files: `docs/serving/online_serving/speech_to_text.md`_
- **2026-07-20** [`ae10e855ab`](https://github.com/vllm-project/vllm/commit/ae10e855ab) [#47210](https://github.com/vllm-project/vllm/pull/47210)
  [Misc][Docs] Remove duplicate CodeGeex4 row in XPU model table (#47210)
  _Files: `docs/models/hardware_supported_models/xpu.md`_
- **2026-07-20** [`47d0597ca2`](https://github.com/vllm-project/vllm/commit/47d0597ca2) [#47211](https://github.com/vllm-project/vllm/pull/47211)
  [Misc][Docs] Fix broken csrc kernel links in fusions doc (#47211)
  _Files: `docs/design/fusions.md`_

## Perf / Benchmark  (5 commits)

- **2026-07-27** [`f19ee27e39`](https://github.com/vllm-project/vllm/commit/f19ee27e39) [#49571](https://github.com/vllm-project/vllm/pull/49571)
  [Hardware][Power] Add FAST_EXP for Power (#49571)
  _Files: `benchmarks/kernels/cpu/benchmark_cpu_attn.py`, `csrc/cpu/cpu_arch_macros.h`, `csrc/cpu/cpu_types_vsx.hpp`_
- **2026-07-26** [`8d28b48d01`](https://github.com/vllm-project/vllm/commit/8d28b48d01) [#49524](https://github.com/vllm-project/vllm/pull/49524)
  [Perf] Isolate MM preprocessing on its own executor (#49524)
  _Files: `tests/test_config.py`, `vllm/config/model.py`, `vllm/renderers/base.py`_
- **2026-07-24** [`a454a1dd25`](https://github.com/vllm-project/vllm/commit/a454a1dd25) [#49180](https://github.com/vllm-project/vllm/pull/49180)
  [Bugfix][Benchmarks] Restore --skip-tokenizer-init with custom dataset (#49180)
  _Files: `tests/benchmarks/test_skip_tokenizer_init.py`, `vllm/benchmarks/datasets/datasets.py`, `vllm/benchmarks/serve.py`_
- **2026-07-21** [`eb44b3aaa4`](https://github.com/vllm-project/vllm/commit/eb44b3aaa4) [#49295](https://github.com/vllm-project/vllm/pull/49295)
  [Rust][Benchmark] Use async HTTP clients (#49295)
  _Files: `rust/Cargo.lock`, `rust/src/bench/Cargo.toml`, `rust/src/bench/src/benchmark.rs`, `rust/src/bench/src/datasets/custom.rs` _+11 more__
- **2026-07-21** [`8688a06d67`](https://github.com/vllm-project/vllm/commit/8688a06d67) [#48937](https://github.com/vllm-project/vllm/pull/48937)
  [Rust][Benchmark] Use `tracing` for logs (#48937)
  _Files: `rust/Cargo.lock`, `rust/src/bench/Cargo.toml`, `rust/src/bench/src/backends/pooling.rs`, `rust/src/bench/src/benchmark.rs` _+20 more__

## Compilation / CUDA Graph  (4 commits)

- **2026-07-27** [`bf4f633b4c`](https://github.com/vllm-project/vllm/commit/bf4f633b4c) [#49394](https://github.com/vllm-project/vllm/pull/49394)
  [XPU] Enable QK Norm + RoPE fusion pass on XPU (#49394)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `vllm/compilation/passes/pass_manager.py`, `vllm/platforms/xpu.py`_
- **2026-07-22** [`149daf0d72`](https://github.com/vllm-project/vllm/commit/149daf0d72) [#47573](https://github.com/vllm-project/vllm/pull/47573)
  [Bugfix] Exclude location-derived path vars from torch.compile cache factors (#47573)
  _Files: `tests/config/test_config_utils.py`, `vllm/envs.py`_
- **2026-07-21** [`de6ec294ef`](https://github.com/vllm-project/vllm/commit/de6ec294ef) [#49302](https://github.com/vllm-project/vllm/pull/49302)
  [Bugfix] Fix DSA crash under breakable piecewise cudagraphs (#49302)
  _Files: `tests/v1/cudagraph/test_breakable_cudagraph.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/model_states/default.py`_
- **2026-07-21** [`f890e1dbe2`](https://github.com/vllm-project/vllm/commit/f890e1dbe2) [#48843](https://github.com/vllm-project/vllm/pull/48843)
  [BugFix] Set graph_pool_id before FULL CUDA graph capture in ModelRunner V2 (#48843)
  _Files: `tests/v1/cudagraph/test_cudagraph_manager.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`_

## LoRA  (4 commits)

- **2026-07-27** [`50aa830482`](https://github.com/vllm-project/vllm/commit/50aa830482) [#49751](https://github.com/vllm-project/vllm/pull/49751)
  [BugFix][MRV2] Don't create dummy requests longer than `max_model_len` (#49751)
  _Files: `tests/v1/worker/test_gpu_input_batch_v2.py`, `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/lora_utils.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-07-24** [`0231dd5467`](https://github.com/vllm-project/vllm/commit/0231dd5467) [#49385](https://github.com/vllm-project/vllm/pull/49385)
  [BugFix][LoRA] Skip marlin-backend gpt-oss LoRA tests on XPU (#49385)
  _Files: `tests/lora/test_gptoss_tp.py`_
- **2026-07-22** [`61c9ef986a`](https://github.com/vllm-project/vllm/commit/61c9ef986a) [#49153](https://github.com/vllm-project/vllm/pull/49153)
  [Frontend] Parallelize preprocessing within the same request for pooling models online serving. (#49153)
  _Files: `tests/entrypoints/pooling/embed/test_io_processor.py`, `tests/entrypoints/pooling/scoring/test_cross_encoder_offline.py`, `tests/entrypoints/serve/lora/test_serving_models.py`, `vllm/entrypoints/pooling/base/io_processor.py` _+13 more__
- **2026-07-21** [`7a98c7a392`](https://github.com/vllm-project/vllm/commit/7a98c7a392) [#49244](https://github.com/vllm-project/vllm/pull/49244)
  [Misc] Remove old now unsupported `max_num_partial_prefills` and `max_long_partial_prefills` (#49244)
  _Files: `tests/lora/test_worker.py`, `vllm/config/scheduler.py`, `vllm/engine/arg_utils.py`_

## Speculative Decoding  (3 commits)

- **2026-07-27** [`5f89a03dcb`](https://github.com/vllm-project/vllm/commit/5f89a03dcb) [#49910](https://github.com/vllm-project/vllm/pull/49910)
  [CI] Explicitly tear down speculative decode runners (#49910)
  _Files: `tests/v1/spec_decode/test_max_len.py`_
- **2026-07-23** [`76bf55240c`](https://github.com/vllm-project/vllm/commit/76bf55240c) [#49415](https://github.com/vllm-project/vllm/pull/49415)
  [Bugfix] Fix DeepSeek-V4 DSpark draft shared-expert padding for TP > 8 (#49415)
  _Files: `vllm/models/deepseek_v4/nvidia/dspark.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/mtp.py`_
- **2026-07-21** [`b2b8f679d0`](https://github.com/vllm-project/vllm/commit/b2b8f679d0) [#47953](https://github.com/vllm-project/vllm/pull/47953)
  [Bugfix][Spec Decode] Restrict embedding-width share guard to EAGLE drafts (#47953)
  _Files: `vllm/v1/spec_decode/llm_base_proposer.py`_

---
_Generated 2026-07-27 11:35 UTC_