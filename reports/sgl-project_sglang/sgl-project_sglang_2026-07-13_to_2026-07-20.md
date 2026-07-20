# sgl-project/sglang — Weekly Change Report
**Period:** 2026-07-13 → 2026-07-20  |  **Total commits:** 344

## ✨ New Features This Week

- **2026-07-20** [#30246](https://github.com/sgl-project/sglang/pull/30246) — [XPU][NIGHTLY] Add 8 XPU nightly tests, enable 1-gpu suite (#30246)
- **2026-07-20** [#31732](https://github.com/sgl-project/sglang/pull/31732) — Support GPT-OSS zigzag CP with TRTLLM-MHA (#31732)
- **2026-07-20** [#31681](https://github.com/sgl-project/sglang/pull/31681) — Add Inkling model support (#31681)
- **2026-07-20** [#31649](https://github.com/sgl-project/sglang/pull/31649) — Enable GPT-OSS TinyGEMM on CUDA 13 (#31649)
- **2026-07-20** [#31126](https://github.com/sgl-project/sglang/pull/31126) — [Intel XPU] Enable (biased) grouped topk for xpu (#31126)
- **2026-07-19** [#31717](https://github.com/sgl-project/sglang/pull/31717) — Add houseroad to CI_PERMISSIONS.json (#31717)
- **2026-07-19** [#29972](https://github.com/sgl-project/sglang/pull/29972) — Support MiMo V2.5 with zigzag context parallelism (#29972)
- **2026-07-19** [#29353](https://github.com/sgl-project/sglang/pull/29353) — [Scheduler] Add `SGLANG_FORCE_COARSE_WAR_BARRIER` opt-in for a whole-forward WAR barrier (#29353)
- **2026-07-18** [#30272](https://github.com/sgl-project/sglang/pull/30272) — Implement SM120 DeepSeek V4 flashinfer_mxfp4 moe runner backend + TP2 (#30272)
- **2026-07-18** [#31580](https://github.com/sgl-project/sglang/pull/31580) — [plugin] oot torch profiler activity support (#31580)
- _…and 59 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-20** [`17fdd8487f`](https://github.com/sgl-project/sglang/commit/17fdd8487f) [#31737](https://github.com/sgl-project/sglang/pull/31737) — [AMD] Update qwen3.5 cookbook (#31737)
- **2026-07-19** [`555267ed05`](https://github.com/sgl-project/sglang/commit/555267ed05) [#31688](https://github.com/sgl-project/sglang/pull/31688) — Fix ROCm fused KV and KDA paths (#31688)
- **2026-07-19** [`377c93d54e`](https://github.com/sgl-project/sglang/commit/377c93d54e) [#30940](https://github.com/sgl-project/sglang/pull/30940) — [AMD] Gate TP4 o_proj/qkv CK block-FP8 GEMM shapes to Triton (ROCm 7.0 Qwen-3.5) (#30940)
- **2026-07-19** [`c68392c535`](https://github.com/sgl-project/sglang/commit/c68392c535) [#31675](https://github.com/sgl-project/sglang/pull/31675) — [AMD] Fix DeepSeek MLA prefill shape mismatch on HIP eager fallback (missing mha_companion_layers) (#31675)
- **2026-07-18** [`7fbe91c6ea`](https://github.com/sgl-project/sglang/commit/7fbe91c6ea) [#31492](https://github.com/sgl-project/sglang/pull/31492) — [AMD] register 8 JIT kernel benchmarks to jit-kernel-benchmark-test-amd (#31492)
- **2026-07-18** [`87dc211b87`](https://github.com/sgl-project/sglang/commit/87dc211b87) [#31634](https://github.com/sgl-project/sglang/pull/31634) — [MUSA] Fix sglang-kernel build (#31634)
- **2026-07-17** [`c95026aed3`](https://github.com/sgl-project/sglang/commit/c95026aed3) [#31484](https://github.com/sgl-project/sglang/pull/31484) — Upgrade llguidance to 1.7.6 (#31484)
- **2026-07-17** [`c00206c68c`](https://github.com/sgl-project/sglang/commit/c00206c68c) [#31496](https://github.com/sgl-project/sglang/pull/31496) — chore: bump sgl-kernel version to 0.4.5 (#31496)
- **2026-07-17** [`fec6131844`](https://github.com/sgl-project/sglang/commit/fec6131844) [#30506](https://github.com/sgl-project/sglang/pull/30506) — [AMD] Disable DSA fused top-k v2 on ROCm for GLM-5.x / DeepSeek-V3.2 (#30506)
- **2026-07-17** [`2c64b7782e`](https://github.com/sgl-project/sglang/commit/2c64b7782e) [#31368](https://github.com/sgl-project/sglang/pull/31368) — [AMD][PD] Fix early-send cached-prefix KV racing the prefill forward on mori (#31368)
- **2026-07-17** [`53229e88da`](https://github.com/sgl-project/sglang/commit/53229e88da) [#31515](https://github.com/sgl-project/sglang/pull/31515) — [AMD] Fix stale imports in test_fused_fp8_kv_write.py (#31515)
- **2026-07-17** [`c546afc147`](https://github.com/sgl-project/sglang/commit/c546afc147) [#31379](https://github.com/sgl-project/sglang/pull/31379) — [AMD] Register 2 CPU/triton unit + kernel tests for AMD 1-GPU PR CI (#31379)
- **2026-07-17** [`1ac1ffea0c`](https://github.com/sgl-project/sglang/commit/1ac1ffea0c) [#31307](https://github.com/sgl-project/sglang/pull/31307) — [Kernel] Fill non-CUDA coverage: HIP (aiter/rocm-triton) + Ascend NPU backends (RFC #29630) (#31307)
- **2026-07-17** [`27a52d2530`](https://github.com/sgl-project/sglang/commit/27a52d2530) [#31452](https://github.com/sgl-project/sglang/pull/31452) — [Docs] Tune DeepSeek-V4 HiCache for MI355X PD (#31452)
- **2026-07-16** [`8c9833f9a9`](https://github.com/sgl-project/sglang/commit/8c9833f9a9) [#31454](https://github.com/sgl-project/sglang/pull/31454) — cookbook(qwen3.5): bump AMD ROCm docker images to v0.5.15.post1 (#31454)
- **2026-07-16** [`e2d021d4ab`](https://github.com/sgl-project/sglang/commit/e2d021d4ab) [#30238](https://github.com/sgl-project/sglang/pull/30238) — [AMD] Support two batch overlap with MTP on DeepSeekV4 (#30238)
- **2026-07-16** [`4d60c4540c`](https://github.com/sgl-project/sglang/commit/4d60c4540c) [#31436](https://github.com/sgl-project/sglang/pull/31436) — [AMD] Skip AMD nightly local registry push (#31436)
- **2026-07-16** [`3264477a07`](https://github.com/sgl-project/sglang/commit/3264477a07) [#31122](https://github.com/sgl-project/sglang/pull/31122) — [Docs] Add AMD-specific HiCache config for DeepSeek V4 playground (#31122)
- **2026-07-16** [`01b003255a`](https://github.com/sgl-project/sglang/commit/01b003255a) [#26852](https://github.com/sgl-project/sglang/pull/26852) — [AMD]Reuse fused FP8 KV cache write on standard aiter prefill/decode (#26852)
- **2026-07-16** [`8c5e0cee18`](https://github.com/sgl-project/sglang/commit/8c5e0cee18) [#31406](https://github.com/sgl-project/sglang/pull/31406) — [AMD] Bump MoRI to f7e6ac6 to fix ROCm install_dependency build break (#31406)
- **2026-07-16** [`14095ef78a`](https://github.com/sgl-project/sglang/commit/14095ef78a) [#31342](https://github.com/sgl-project/sglang/pull/31342) — [AMD] Disable CUDA IPC multimodal transport on ROCm in MMMU VLM tests (#31342)
- **2026-07-15** [`67148447a6`](https://github.com/sgl-project/sglang/commit/67148447a6) [#31088](https://github.com/sgl-project/sglang/pull/31088) — [AMD] Register 3 CPU-bound / triton unit + light-integration tests for AMD 1-GPU PR CI (#31088)
- **2026-07-15** [`ec32590025`](https://github.com/sgl-project/sglang/commit/ec32590025) [#30706](https://github.com/sgl-project/sglang/pull/30706) — feat(moriep): add fp4 combine dtype (SGLANG_MORI_COMBINE_DTYPE=fp4) (#30706)
- **2026-07-15** [`e78051a419`](https://github.com/sgl-project/sglang/commit/e78051a419) [#30355](https://github.com/sgl-project/sglang/pull/30355) — [AMD] [Fix] Fix --attention-backend triton work for DeepSeek MLA on MI355 (null-K + decode dispatch + RoPE) (#30355)
- **2026-07-15** [`d36e96ce23`](https://github.com/sgl-project/sglang/commit/d36e96ce23) [#30359](https://github.com/sgl-project/sglang/pull/30359) — [AMD] Enable mamba-extra-buffer for Qwen3.5 on ROCm (#30359)
- **2026-07-15** [`a8b60433c2`](https://github.com/sgl-project/sglang/commit/a8b60433c2) [#31131](https://github.com/sgl-project/sglang/pull/31131) — [AMD] Fix DSV4 JIT build on rocm  (#31131)
- **2026-07-15** [`fbcbe0a986`](https://github.com/sgl-project/sglang/commit/fbcbe0a986) [#30651](https://github.com/sgl-project/sglang/pull/30651) — cookbook(deepseek-v4): add MORI disagg backend for AMD + bump MI355X image (#30651)
- **2026-07-15** [`1afab30577`](https://github.com/sgl-project/sglang/commit/1afab30577) [#29432](https://github.com/sgl-project/sglang/pull/29432) — Fix bookkeeping fields not encapsulated with real allocations in normal alloc, PD pre-alloc, DFlash and EAGLE (#29432)
- **2026-07-15** [`e789ca24a7`](https://github.com/sgl-project/sglang/commit/e789ca24a7) [#29431](https://github.com/sgl-project/sglang/pull/29431) — Lightweight extract allocation logic from mem_cache/common.py to more clearly show nearly parallel variants (#29431)
- **2026-07-15** [`d8d76c4d12`](https://github.com/sgl-project/sglang/commit/d8d76c4d12) [#29427](https://github.com/sgl-project/sglang/pull/29427) — Introduce req.kv container for coupled owned kv field lifecycle (#29427)
- **2026-07-15** [`a3194d3585`](https://github.com/sgl-project/sglang/commit/a3194d3585) [#30622](https://github.com/sgl-project/sglang/pull/30622) — [AMD] Remove ROCm page_first+kernel -> layer_first HiCache fallback (follow-up to #28534) (#30622)
- **2026-07-15** [`ba5be86d42`](https://github.com/sgl-project/sglang/commit/ba5be86d42) [#30792](https://github.com/sgl-project/sglang/pull/30792) — [Kernel] Migrate DSA + DSV4 attention kernels to sglang.kernels (RFC #29630, Phase 2.5, 5/7) (#30792)
- **2026-07-15** [`aafa706f8f`](https://github.com/sgl-project/sglang/commit/aafa706f8f) [#31258](https://github.com/sgl-project/sglang/pull/31258) — [AMD] Update qwen3.5 cookbook (#31258)
- **2026-07-14** [`a5c3e0283f`](https://github.com/sgl-project/sglang/commit/a5c3e0283f) [#30351](https://github.com/sgl-project/sglang/pull/30351) — [Bug fix] Account for KV replication fan-out in transfer-byte metrics (#30351)
- **2026-07-14** [`1a35440c4a`](https://github.com/sgl-project/sglang/commit/1a35440c4a) [#30789](https://github.com/sgl-project/sglang/pull/30789) — [Kernel] Migrate generic attention kernels to sglang.kernels (RFC #29630, Phase 2.5, 4/7) (#30789)
- **2026-07-14** [`64a70c9097`](https://github.com/sgl-project/sglang/commit/64a70c9097) [#31143](https://github.com/sgl-project/sglang/pull/31143) — [AMD] jit_kernel: complete utils.cuh HIP-compat (cudaDevAttr / cudaDeviceGetAttribute) (#31143)
- **2026-07-14** [`e9ef06c560`](https://github.com/sgl-project/sglang/commit/e9ef06c560) [#30787](https://github.com/sgl-project/sglang/pull/30787) — [Kernel] Migrate top-level srt/layers stray kernels to sglang.kernels (RFC #29630, Phase 2.5, 3/7) (#30787)
- **2026-07-14** [`ee464fedc6`](https://github.com/sgl-project/sglang/commit/ee464fedc6) [#30786](https://github.com/sgl-project/sglang/pull/30786) — [Kernel] Migrate scattered MoE kernels to sglang.kernels (RFC #29630, Phase 2.5, 2/7) (#30786)
- **2026-07-14** [`423b8485fb`](https://github.com/sgl-project/sglang/commit/423b8485fb) [#23754](https://github.com/sgl-project/sglang/pull/23754) — [Quantization] add humming quantization kernel (#23754)
- **2026-07-13** [`e2728ac504`](https://github.com/sgl-project/sglang/commit/e2728ac504) [#30998](https://github.com/sgl-project/sglang/pull/30998) — [Spec] Remove dead `padded_static_len` and stale `SGLANG_ENABLE_SPEC_V2` references (#30998)
- **2026-07-13** [`805385414e`](https://github.com/sgl-project/sglang/commit/805385414e) [#31058](https://github.com/sgl-project/sglang/pull/31058) — chore: bump docs install version to 0.5.15 (#31058)
- **2026-07-13** [`c0f1f7e062`](https://github.com/sgl-project/sglang/commit/c0f1f7e062) [#30977](https://github.com/sgl-project/sglang/pull/30977) — [Spec] Rename `num_tokens_per_bs` to `num_tokens_per_req` (#30977)
- **2026-07-13** [`80965db8d3`](https://github.com/sgl-project/sglang/commit/80965db8d3) [#30942](https://github.com/sgl-project/sglang/pull/30942) — [AMD] Pin cmake==4.3.4 in ROCm Dockerfile to fix MoRI gtest_discover build break (#30942)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-07-20 |
| [#29562](https://github.com/sgl-project/sglang/issues/29562) | [Bug] GLM-5.2-NVFP4 error on pro6000 | — | 2026-07-20 |
| [#31359](https://github.com/sgl-project/sglang/issues/31359) | [Tracking] Inkling Day-0 Support | high priority, new-model | 2026-07-20 |
| [#30928](https://github.com/sgl-project/sglang/issues/30928) | [RFC] Position-Independent KV Cache Reuse for Agentic/RAG Workloads | — | 2026-07-20 |
| [#30734](https://github.com/sgl-project/sglang/issues/30734) | [Roadmap] GLM-5.2 + AMD/ROCm DSpark support | — | 2026-07-20 |
| [#30321](https://github.com/sgl-project/sglang/issues/30321) | [Bug] GLM-5.2 with MTP+Hicache+Mooncake occasionally produces garbled  | — | 2026-07-20 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-07-20 |
| [#31490](https://github.com/sgl-project/sglang/issues/31490) | [Bug] GSM8K accuracy regression on DeepSeek-V4-Flash-FP8 (dp8ep8, gfx9 | — | 2026-07-19 |
| [#30209](https://github.com/sgl-project/sglang/issues/30209) | [Bug] GlmMoeDsa (GLM-5.2) FP4 + EAGLE: illegal memory access in flashi | — | 2026-07-19 |
| [#27252](https://github.com/sgl-project/sglang/issues/27252) | [Roadmap]Prefill Context Parallel Refactor | — | 2026-07-19 |
| [#31699](https://github.com/sgl-project/sglang/issues/31699) | [Bug]: DeepSeek-V4(-Pro) DP-attention (data-parallel-size>1) produces  | — | 2026-07-19 |
| [#31588](https://github.com/sgl-project/sglang/issues/31588) | [Bug] Inkling multi-layer EAGLE auto KV sizing OOMs while allocating d | — | 2026-07-18 |
| [#16565](https://github.com/sgl-project/sglang/issues/16565) | [Roadmap][Feature] Support Moore Threads (MUSA) GPU | mthreads | 2026-07-18 |
| [#31641](https://github.com/sgl-project/sglang/issues/31641) | [Bug] NVFP4 KV cache batched decode (trtllm_mha / SM120 XQA) produces  | — | 2026-07-18 |
| [#31632](https://github.com/sgl-project/sglang/issues/31632) | [Bug] TP subprocess SIGSEGV in dsa_indexer._get_k_bf16 (JIT bf16 kerne | — | 2026-07-18 |
| [#31600](https://github.com/sgl-project/sglang/issues/31600) | [Bug] glm-5.2-w4afp8 +l2(hicache)+l3(mooncake) kvcache dram cluster ,c | — | 2026-07-18 |
| [#31594](https://github.com/sgl-project/sglang/issues/31594) | [Bug] [AMD] Qwen3.5 GatedDeltaNet + dp-attention on ROCm/MoRI: HIP "in | — | 2026-07-17 |
| [#31533](https://github.com/sgl-project/sglang/issues/31533) | [Bug] xgrammar-constrained requests never terminate when tokenizer eos | — | 2026-07-17 |
| [#31545](https://github.com/sgl-project/sglang/issues/31545) | [Bug][ROCm] MI355X: CUDA-graph decode kernels are captured but async-d | — | 2026-07-17 |
| [#29630](https://github.com/sgl-project/sglang/issues/29630) | [RFC] Introduce a unified sglang.kernels namespace for kernel organiza | RFC, jit-kernel, kernel | 2026-07-17 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 72 |
| MoE / Expert Parallel | 46 |
| Prefill / Decode Disaggregation | 29 |
| Multimodal | 27 |
| KV Cache / Memory | 20 |
| Scheduler / Batching | 19 |
| Speculative Decoding | 19 |
| Triton / Kernels | 18 |
| Other | 17 |
| Quantization | 17 |
| ROCm / AMD | 15 |
| CI / Build | 12 |
| Tensor / Data Parallel | 12 |
| Models | 8 |
| Docs / Examples | 6 |
| LoRA | 4 |
| Serving / API | 2 |
| Structured Output | 1 |

## Attention / FlashInfer  (72 commits)

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
- **2026-07-19** [`555267ed05`](https://github.com/sgl-project/sglang/commit/555267ed05) [#31688](https://github.com/sgl-project/sglang/pull/31688)
  Fix ROCm fused KV and KDA paths (#31688)
  _Files: `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/srt/models/utils.py`_
- **2026-07-19** [`688a6d23f1`](https://github.com/sgl-project/sglang/commit/688a6d23f1) [#31705](https://github.com/sgl-project/sglang/pull/31705)
  [DeepSeek-V4] Fix idle-rank dummy-extend sparse-prefill crash under DP breakable CUDA graph (#31705)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-07-19** [`d4801be447`](https://github.com/sgl-project/sglang/commit/d4801be447) [#30868](https://github.com/sgl-project/sglang/pull/30868)
  fix: fix vlm cuda graph shape stability (#30868)
  _Files: `python/sglang/srt/compilation/compile.py`, `python/sglang/srt/compilation/cuda_piecewise_backend.py`, `python/sglang/srt/compilation/xpu_piecewise_backend.py`, `python/sglang/srt/layers/attention/vision.py` _+7 more__
- **2026-07-19** [`a03ca46a28`](https://github.com/sgl-project/sglang/commit/a03ca46a28) [#31474](https://github.com/sgl-project/sglang/pull/31474)
  Fix KDA prefix caching under mamba extra_buffer and enable it for kimi_linear (#31474)
  _Files: `python/sglang/kernels/ops/attention/fla/kda.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py` _+7 more__
- **2026-07-19** [`7a03d30149`](https://github.com/sgl-project/sglang/commit/7a03d30149) [#29972](https://github.com/sgl-project/sglang/pull/29972)
  Support MiMo V2.5 with zigzag context parallelism (#29972)
  _Files: `python/sglang/srt/distributed/device_communicators/pynccl.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/layers/attention/dsa/utils.py` _+13 more__
- **2026-07-19** [`c68392c535`](https://github.com/sgl-project/sglang/commit/c68392c535) [#31675](https://github.com/sgl-project/sglang/pull/31675)
  [AMD] Fix DeepSeek MLA prefill shape mismatch on HIP eager fallback (missing mha_companion_layers) (#31675)
  _Files: `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-07-19** [`609fe1c0d1`](https://github.com/sgl-project/sglang/commit/609fe1c0d1) [#31672](https://github.com/sgl-project/sglang/pull/31672)
  fix(gemma4): prevent attention mask offset overflow (#31672)
  _Files: `python/sglang/srt/models/gemma4_mm.py`_
- **2026-07-19** [`b8ec544946`](https://github.com/sgl-project/sglang/commit/b8ec544946) [#30514](https://github.com/sgl-project/sglang/pull/30514)
  [DSA] Integrate Q8KV8 FP8 Sparse MLA Prefill into the DSA Backend (DeepSeek-V3.2) (#30514)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`, `docs_new/docs/advanced_features/attention_backend.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/jit_kernel/csrc/sparse_mla_q8kv8_prefill_sm90/kernel.cuh` _+6 more__
- **2026-07-18** [`99f5a6f46b`](https://github.com/sgl-project/sglang/commit/99f5a6f46b) [#31501](https://github.com/sgl-project/sglang/pull/31501)
  [flashinfer] Pass window_left at plan time for the SWA paged prefill wrapper (#31501)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`, `test/registered/attention/unittests/swa/test_flashinfer.py`_
- **2026-07-18** [`ece02ffc9c`](https://github.com/sgl-project/sglang/commit/ece02ffc9c) [#31659](https://github.com/sgl-project/sglang/pull/31659)
  [NPU] FIX CMB illusion of garbled characters acc problems, in prefix cache mtp scenarios. (#31659)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`_
- **2026-07-18** [`9306278fbc`](https://github.com/sgl-project/sglang/commit/9306278fbc) [#24013](https://github.com/sgl-project/sglang/pull/24013)
  vlm: batch cross-request vit encoding and reuse attention metadata (#24013)
  _Files: `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/models/dots_vlm_vit.py` _+18 more__
- **2026-07-18** [`72c4ed1a3f`](https://github.com/sgl-project/sglang/commit/72c4ed1a3f) [#31468](https://github.com/sgl-project/sglang/pull/31468)
  [Spec] DFlash: remove per-step host syncs so the CPU runs a full step ahead (spec-v2 overlap) (#31468)
  _Files: `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/hybrid_attn_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py` _+7 more__
- **2026-07-18** [`7a896215e7`](https://github.com/sgl-project/sglang/commit/7a896215e7) [#31619](https://github.com/sgl-project/sglang/pull/31619)
  [CP] Migrate MLA prefill CP (DeepSeek V3) to CP-v2 zigzag strategy (#31619)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/cp/utils.py`, `python/sglang/srt/layers/cp/zigzag.py`, `python/sglang/srt/model_executor/runner/eager_runner.py` _+3 more__
- **2026-07-18** [`67e7f8d13a`](https://github.com/sgl-project/sglang/commit/67e7f8d13a) [#30838](https://github.com/sgl-project/sglang/pull/30838)
  [JIT] Refactor dtype traits into DTypeTrait and unify warp reductions (#30838)
  _Files: `.claude/skills/add-jit-kernel/SKILL.md`, `docs_new/docs/developer_guide/development_jit_kernel_guide.mdx`, `python/sglang/jit_kernel/__main__.py`, `python/sglang/jit_kernel/benchmark/marker.py` _+15 more__
- **2026-07-17** [`42a058c760`](https://github.com/sgl-project/sglang/commit/42a058c760) [#31558](https://github.com/sgl-project/sglang/pull/31558)
  optimize: avoid fla l2-norm recompilation by token count (#31558)
  _Files: `python/sglang/kernels/ops/attention/fla/l2norm.py`_
- **2026-07-17** [`a01a8e1ed9`](https://github.com/sgl-project/sglang/commit/a01a8e1ed9) [#31610](https://github.com/sgl-project/sglang/pull/31610)
  docs(cookbook): replace pinned nightly/dev images with :latest (#31610)
  _Files: `docs_new/cookbook/autoregressive/Google/Gemma4.mdx`, `docs_new/cookbook/autoregressive/InclusionAI/Ling-2.5-1T.mdx`, `docs_new/cookbook/autoregressive/InclusionAI/Ring-2.5-1T.mdx`, `docs_new/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx` _+11 more__
- **2026-07-17** [`ec6a3163b7`](https://github.com/sgl-project/sglang/commit/ec6a3163b7) [#21601](https://github.com/sgl-project/sglang/pull/21601)
  [Feature] Add FP4 KV Cache Design and support SM120 GPUs (#21601)
  _Files: `docs_new/docs/advanced_features/attention_backend.mdx`, `docs_new/docs/advanced_features/quantized_kv_cache.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/layers/attention/attention_registry.py` _+15 more__
- **2026-07-17** [`ae3f62613a`](https://github.com/sgl-project/sglang/commit/ae3f62613a) [#31508](https://github.com/sgl-project/sglang/pull/31508)
  docs(cookbook): fix stale/pruned Docker image tags (#31508)
  _Files: `docs_new/cookbook/autoregressive/NVIDIA/Nemotron3-Super.mdx`, `docs_new/cookbook/autoregressive/StepFun/Step-3.7-Flash.mdx`, `docs_new/cookbook/autoregressive/Xiaomi/MiMo-V2-Flash.mdx`, `docs_new/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx`_
- **2026-07-17** [`53229e88da`](https://github.com/sgl-project/sglang/commit/53229e88da) [#31515](https://github.com/sgl-project/sglang/pull/31515)
  [AMD] Fix stale imports in test_fused_fp8_kv_write.py (#31515)
  _Files: `test/registered/attention/test_fused_fp8_kv_write.py`_
- **2026-07-17** [`681c223570`](https://github.com/sgl-project/sglang/commit/681c223570) [#31439](https://github.com/sgl-project/sglang/pull/31439)
  refactor: wrap split backends once on full-attention backends (#31439)
  _Files: `python/sglang/srt/model_executor/model_runner_components/attention_backend_setup.py`, `test/registered/unit/model_executor/model_runner_components/test_attention_backend_setup.py`_
- **2026-07-17** [`24a8944e15`](https://github.com/sgl-project/sglang/commit/24a8944e15) [#31391](https://github.com/sgl-project/sglang/pull/31391)
  fix: enable Kimi multimodal breakable prefill cuda graph replay (#31391)
  _Files: `python/sglang/srt/layers/radix_attention.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/model_executor/model_runner_components/layer_setup.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+3 more__
- **2026-07-17** [`6e3be088a9`](https://github.com/sgl-project/sglang/commit/6e3be088a9) [#31527](https://github.com/sgl-project/sglang/pull/31527)
  [Spec] Allocate the verify tree-mask scratch on the target backend only (#31527)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-07-17** [`45824c69ca`](https://github.com/sgl-project/sglang/commit/45824c69ca) [#31381](https://github.com/sgl-project/sglang/pull/31381)
  fa3: build the topk>1 verify replay page table on-device (#31381)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`_
- **2026-07-17** [`12af7e6c34`](https://github.com/sgl-project/sglang/commit/12af7e6c34) [#31005](https://github.com/sgl-project/sglang/pull/31005)
  [NPU] Fix DSA top-k seed buffer shape for MTP IndexShare (#31005)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-07-17** [`9910ef8167`](https://github.com/sgl-project/sglang/commit/9910ef8167) [#31090](https://github.com/sgl-project/sglang/pull/31090)
  flashmla: sync-free spec via device-side draft-extend (#31090)
  _Files: `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/speculative/draft_utils.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-07-16** [`44f4ea917c`](https://github.com/sgl-project/sglang/commit/44f4ea917c) [#31364](https://github.com/sgl-project/sglang/pull/31364)
  fa3: sync-free eagle spec via fixed-window draft-extend metadata (#31364)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`_
- **2026-07-16** [`4ad418d2c3`](https://github.com/sgl-project/sglang/commit/4ad418d2c3) [#31114](https://github.com/sgl-project/sglang/pull/31114)
  Push test case scripts from test repo to main upstream community repository (#31114)
  _Files: `.github/workflows/nightly-test-npu-e2e-single-node.yml`, `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/ascend/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in8k_out1k_50ms.py` _+10 more__
- **2026-07-16** [`7d0fd5101d`](https://github.com/sgl-project/sglang/commit/7d0fd5101d) [#31227](https://github.com/sgl-project/sglang/pull/31227)
  optimization: shard kimi dp image feature transport and misc optimizations (#31227)
  _Files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/models/kimi_k25.py` _+9 more__
- **2026-07-16** [`e5f9804e26`](https://github.com/sgl-project/sglang/commit/e5f9804e26) [#31241](https://github.com/sgl-project/sglang/pull/31241)
  Refining fused A GEMM dispatch (#31241)
  _Files: `python/sglang/jit_kernel/csrc/gemm/dsv3_fused_a_gemm.cuh`, `python/sglang/jit_kernel/fused_a_gemm.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py` _+1 more__
- **2026-07-16** [`a798a2aeea`](https://github.com/sgl-project/sglang/commit/a798a2aeea) [#30169](https://github.com/sgl-project/sglang/pull/30169)
  [GDN/KDA] Fuse SM100 CuteDSL prefill state I/O into the chunk h kernel (#30169)
  _Files: `python/sglang/kernels/ops/attention/linear/gdn_blackwell/__init__.py`, `python/sglang/kernels/ops/attention/linear/gdn_blackwell/kernel_h.py`, `python/sglang/kernels/ops/attention/linear/kda_blackwell/__init__.py`, `python/sglang/kernels/ops/attention/linear/kda_blackwell/kernel_h.py` _+4 more__
- **2026-07-16** [`01b003255a`](https://github.com/sgl-project/sglang/commit/01b003255a) [#26852](https://github.com/sgl-project/sglang/pull/26852)
  [AMD]Reuse fused FP8 KV cache write on standard aiter prefill/decode (#26852)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/attention/test_fused_fp8_kv_write.py`_
- **2026-07-16** [`dc60f65661`](https://github.com/sgl-project/sglang/commit/dc60f65661) [#31385](https://github.com/sgl-project/sglang/pull/31385)
  chore: bump tokenspeed_mla to 0.1.8 (#31385)
  _Files: `python/pyproject.toml`_
- **2026-07-16** [`d9003dd452`](https://github.com/sgl-project/sglang/commit/d9003dd452) [#31204](https://github.com/sgl-project/sglang/pull/31204)
  fix: skip unsafe automatic prefill graph capture (#31204)
  _Files: `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `test/registered/unit/model_executor/model_runner_components/test_cuda_graph_setup.py`_
- **2026-07-16** [`7647a9d260`](https://github.com/sgl-project/sglang/commit/7647a9d260) [#29690](https://github.com/sgl-project/sglang/pull/29690)
  Fuse the preprocess kernels of trtllm-gen attention (#29690)
  _Files: `python/sglang/jit_kernel/csrc/attention/fused_fp8_qkv_kv_cache.cuh`, `python/sglang/jit_kernel/fused_fp8_qkv_kv_cache.py`, `python/sglang/kernels/ops/kvcache/trtllm_fp8_kv_kernel.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py` _+3 more__
- **2026-07-16** [`ac23be8d09`](https://github.com/sgl-project/sglang/commit/ac23be8d09) [#29669](https://github.com/sgl-project/sglang/pull/29669)
  Skip MXFP8 autotune on dense GEMM, which causes IMA (#29669)
  _Files: `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`_
- **2026-07-16** [`1cc9493747`](https://github.com/sgl-project/sglang/commit/1cc9493747) [#31244](https://github.com/sgl-project/sglang/pull/31244)
  [Spec] Converge DP-attention spec width scaling onto `num_tokens_per_req` (#31244)
  _Files: `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/models/mindspore.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py` _+8 more__
- **2026-07-15** [`3101c1258c`](https://github.com/sgl-project/sglang/commit/3101c1258c) [#30012](https://github.com/sgl-project/sglang/pull/30012)
  [DSv4] Use BF16 instead of FP32 for indexer score computation (#30012)
  _Files: `python/sglang/srt/layers/attention/dsv4/indexer.py`_
- **2026-07-15** [`67148447a6`](https://github.com/sgl-project/sglang/commit/67148447a6) [#31088](https://github.com/sgl-project/sglang/pull/31088)
  [AMD] Register 3 CPU-bound / triton unit + light-integration tests for AMD 1-GPU PR CI (#31088)
  _Files: `test/registered/attention/test_chunk_gated_delta_rule.py`, `test/registered/observability/test_encoder_server_metrics.py`, `test/registered/unit/spec/test_eagle_worker_v2_topk1_fastpath.py`_
- **2026-07-15** [`e78051a419`](https://github.com/sgl-project/sglang/commit/e78051a419) [#30355](https://github.com/sgl-project/sglang/pull/30355)
  [AMD] [Fix] Fix --attention-backend triton work for DeepSeek MLA on MI355 (null-K + decode dispatch + RoPE) (#30355)
  _Files: `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `test/registered/unit/models/test_deepseek_mla_dispatch.py`_
- **2026-07-15** [`18043aec20`](https://github.com/sgl-project/sglang/commit/18043aec20) [#31332](https://github.com/sgl-project/sglang/pull/31332)
  [CI] Fix TRTLLM MHA graph metadata test fixture (#31332)
  _Files: `test/registered/attention/test_trtllm_mha_graph_metadata.py`_
- **2026-07-15** [`a649b5a9db`](https://github.com/sgl-project/sglang/commit/a649b5a9db) [#30113](https://github.com/sgl-project/sglang/pull/30113)
  [KDA] Add FlashInfer SM100 KDA decode + MTP (target_verify) backend (#30113)
  _Files: `benchmark/bench_linear_attention/bench_kda_flashinfer_mtp.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashinfer.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py` _+2 more__
- **2026-07-15** [`e789ca24a7`](https://github.com/sgl-project/sglang/commit/e789ca24a7) [#29431](https://github.com/sgl-project/sglang/pull/29431)
  Lightweight extract allocation logic from mem_cache/common.py to more clearly show nearly parallel variants (#29431)
  _Files: `python/sglang/srt/debug_utils/pr_fix_toggle.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_allocator.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/allocation.py` _+7 more__
- **2026-07-15** [`e77d95c3d5`](https://github.com/sgl-project/sglang/commit/e77d95c3d5) [#30670](https://github.com/sgl-project/sglang/pull/30670)
  Pass per-forward overrides to ForwardBatch.init_new as explicit arguments (#30670)
  _Files: `.claude/rules/forward-batch-init-new-purity.md`, `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `python/sglang/srt/managers/schedule_batch.py` _+12 more__
- **2026-07-15** [`c00131ebaa`](https://github.com/sgl-project/sglang/commit/c00131ebaa) [#30793](https://github.com/sgl-project/sglang/pull/30793)
  [Kernel] Migrate linear-attention, MiniMax-sparse and diffusion kernels to sglang.kernels (RFC #29630, Phase 2.5, 6/7) (#30793)
  _Files: `.pre-commit-config.yaml`, `benchmark/bench_linear_attention/bench_gdn_prefill_cutedsl.py`, `benchmark/bench_linear_attention/bench_kda_prefill_cutedsl.py`, `python/sglang/kernels/ops/attention/__init__.py` _+40 more__
- **2026-07-15** [`ba5be86d42`](https://github.com/sgl-project/sglang/commit/ba5be86d42) [#30792](https://github.com/sgl-project/sglang/pull/30792)
  [Kernel] Migrate DSA + DSV4 attention kernels to sglang.kernels (RFC #29630, Phase 2.5, 5/7) (#30792)
  _Files: `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dsa/__init__.py`, `python/sglang/kernels/ops/attention/dsa/cp_split.py`, `python/sglang/kernels/ops/attention/dsa/dequant_k_cache.py` _+56 more__
- **2026-07-15** [`4ae9cc3c81`](https://github.com/sgl-project/sglang/commit/4ae9cc3c81) [#31231](https://github.com/sgl-project/sglang/pull/31231)
  Fix gate stride for 4D decode layouts (#31231)
  _Files: `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`_
- **2026-07-15** [`46b675ce70`](https://github.com/sgl-project/sglang/commit/46b675ce70) [#28059](https://github.com/sgl-project/sglang/pull/28059)
  [Intel GPU] DeepSeek V4 11/N: support fp8_paged_mqa_logits_triton from sgl-kernel to run on XPU (#28059)
  _Files: `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py`_
- **2026-07-15** [`76dc427806`](https://github.com/sgl-project/sglang/commit/76dc427806) [#31013](https://github.com/sgl-project/sglang/pull/31013)
  [Spec] Single-source `num_tokens_per_req` derivation and access (#31013)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py` _+19 more__
- **2026-07-15** [`a9cf5e68e6`](https://github.com/sgl-project/sglang/commit/a9cf5e68e6) [#30365](https://github.com/sgl-project/sglang/pull/30365)
  [DSV4] Remove per-step seqlen D2H from speculative to make overlap scheduler work (#30365)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsv4_attention.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_draft_runner.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_target_verify_runner.py` _+1 more__
- **2026-07-14** [`771e386332`](https://github.com/sgl-project/sglang/commit/771e386332) [#31125](https://github.com/sgl-project/sglang/pull/31125)
  Disable flaky DSV4-Flash FP4 BCG determinism test (nondeterminism from #30898 idle-rank dummy extend) (#31125)
  _Files: `test/registered/models_e2e/test_deepseek_v4_flash_fp4_b200.py`_
- **2026-07-14** [`0d89564d27`](https://github.com/sgl-project/sglang/commit/0d89564d27) [#30457](https://github.com/sgl-project/sglang/pull/30457)
  Support scheduler_recv_interval (recv skipper) under DP-attention (#30457)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/managers/scheduler_components/request_receiver.py` _+3 more__
- **2026-07-14** [`271e5ef5c3`](https://github.com/sgl-project/sglang/commit/271e5ef5c3) [#31199](https://github.com/sgl-project/sglang/pull/31199)
  [CI] Fix Flash MLA SM120 test import path (#31199)
  _Files: `test/registered/kernels/test_flash_mla_backends.py`_
- **2026-07-14** [`ed2fcd3201`](https://github.com/sgl-project/sglang/commit/ed2fcd3201) [#31167](https://github.com/sgl-project/sglang/pull/31167)
  Extract attention-backend setup into a module (#31167)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/attention_backend_setup.py`_
- **2026-07-14** [`d15f6a9ac3`](https://github.com/sgl-project/sglang/commit/d15f6a9ac3) [#31154](https://github.com/sgl-project/sglang/pull/31154)
  Introduce NgramEmbeddingManager component (#31154)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/model_runner.py` _+7 more__
- **2026-07-14** [`e20c346541`](https://github.com/sgl-project/sglang/commit/e20c346541) [#31150](https://github.com/sgl-project/sglang/pull/31150)
  Extract hybrid-arch helpers into configs.hybrid_arch and ModelConfig (#31150)
  _Files: `python/sglang/srt/configs/hybrid_arch.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/layers/attention/attention_registry.py` _+12 more__
- **2026-07-14** [`7e229e2a81`](https://github.com/sgl-project/sglang/commit/7e229e2a81) [#30992](https://github.com/sgl-project/sglang/pull/30992)
  support GLM-5.2 MTP index sharing with prefill CP (#30992)
  _Files: `python/sglang/srt/layers/attention/dsa/transform_index.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/server_args.py` _+3 more__
- **2026-07-14** [`0c01971eeb`](https://github.com/sgl-project/sglang/commit/0c01971eeb) [#28046](https://github.com/sgl-project/sglang/pull/28046)
  [Intel GPU] DeepSeek V4 9/N: use sgl-kernel implementation of hadamard_transform on XPU (#28046)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-07-14** [`cfe4eefabb`](https://github.com/sgl-project/sglang/commit/cfe4eefabb) [#27639](https://github.com/sgl-project/sglang/pull/27639)
  [diffusion] model: support LongLive 2.0 T2V and I2V inference (#27639)
  _Files: `docs_new/cookbook/diffusion/LongLive/LongLive-2.0.mdx`, `docs_new/docs.json`, `docs_new/docs/sglang-diffusion/compatibility_matrix.mdx`, `python/sglang/multimodal_gen/configs/models/dits/__init__.py` _+18 more__
- **2026-07-13** [`47030b28be`](https://github.com/sgl-project/sglang/commit/47030b28be) [#31056](https://github.com/sgl-project/sglang/pull/31056)
  Fix MockDSV4ModelRunner missing spec_algorithm (#31056)
  _Files: `python/sglang/test/kits/attention_unittest/attention_methods/dsv4_attention.py`_
- **2026-07-13** [`2ab531cfcf`](https://github.com/sgl-project/sglang/commit/2ab531cfcf) [#29589](https://github.com/sgl-project/sglang/pull/29589)
  fa3/fa4: sync-free for all backends and phases (#29589)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-07-13** [`f49cbbd67d`](https://github.com/sgl-project/sglang/commit/f49cbbd67d) [#31001](https://github.com/sgl-project/sglang/pull/31001)
  Fix GLM/DeepSeek NVFP4 + flashinfer_trtllm long-context "!!!!" collapse (NaN routing) (#31001)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-07-13** [`48fff1f2bd`](https://github.com/sgl-project/sglang/commit/48fff1f2bd) [#31008](https://github.com/sgl-project/sglang/pull/31008)
  [Spec] Deduplicate spec-v2 worker lifecycle boilerplate into BaseSpecWorker (#31008)
  _Files: `python/sglang/srt/speculative/base_spec_worker.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` _+5 more__
- **2026-07-13** [`c0f1f7e062`](https://github.com/sgl-project/sglang/commit/c0f1f7e062) [#30977](https://github.com/sgl-project/sglang/pull/30977)
  [Spec] Rename `num_tokens_per_bs` to `num_tokens_per_req` (#30977)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`, `python/sglang/srt/kv_canary/capacities.py`, `python/sglang/srt/layers/attention/aiter_backend.py` _+34 more__
- **2026-07-13** [`be9791071a`](https://github.com/sgl-project/sglang/commit/be9791071a) [#31036](https://github.com/sgl-project/sglang/pull/31036)
  [NPU] [DOC] Fix Ascend NPU docs issues found by AIDD (#31036)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_contribution_guide.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_operator_development.mdx` _+33 more__
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

## MoE / Expert Parallel  (46 commits)

- **2026-07-20** [`1843384c7a`](https://github.com/sgl-project/sglang/commit/1843384c7a) [#31311](https://github.com/sgl-project/sglang/pull/31311)
  Fix LongCat-2.0 real EP (deepep): double all-reduce + ScMoE RoPE crash (#31311)
  _Files: `python/sglang/srt/models/longcat_flash.py`_
- **2026-07-20** [`1f637a65b9`](https://github.com/sgl-project/sglang/commit/1f637a65b9) [#31707](https://github.com/sgl-project/sglang/pull/31707)
  [NPU] bugfix for W4A8MoE bias 3D dimension mismatch problem (#31707)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py`_
- **2026-07-20** [`bab1dd0d12`](https://github.com/sgl-project/sglang/commit/bab1dd0d12) [#31126](https://github.com/sgl-project/sglang/pull/31126)
  [Intel XPU] Enable (biased) grouped topk for xpu (#31126)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/xpu/test_topk.py`_
- **2026-07-18** [`216b750c8f`](https://github.com/sgl-project/sglang/commit/216b750c8f) [#31582](https://github.com/sgl-project/sglang/pull/31582)
  [Kernel] Sweep decoupled scattered kernels into sglang.kernels.ops (RFC #29630) (#31582)
  _Files: `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/cute_utils/__init__.py`, `python/sglang/kernels/ops/attention/cute_utils/_tcgen05.py`, `python/sglang/kernels/ops/attention/cute_utils/cvt.py` _+18 more__
- **2026-07-18** [`faf6894093`](https://github.com/sgl-project/sglang/commit/faf6894093) [#30272](https://github.com/sgl-project/sglang/pull/30272)
  Implement SM120 DeepSeek V4 flashinfer_mxfp4 moe runner backend + TP2 (#30272)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`, `python/sglang/jit_kernel/csrc/gemm/marlin_moe/marlin_template.h`, `python/sglang/kernels/ops/attention/dsa/tilelang_kernel.py` _+14 more__
- **2026-07-18** [`359009fa00`](https://github.com/sgl-project/sglang/commit/359009fa00) [#31449](https://github.com/sgl-project/sglang/pull/31449)
  [Bugfix][NPU] Fix/Refactor routed scaling factor application in MoE routing (#31449)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/models/llada2.py`, `test/registered/ascend/basic_function/dllm/test_npu_llada2_mini.py`_
- **2026-07-17** [`304a529558`](https://github.com/sgl-project/sglang/commit/304a529558) [#31625](https://github.com/sgl-project/sglang/pull/31625)
  Revert "Bump FlashInfer to 0.6.15 and revert regressions" (#31625)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py` _+3 more__
- **2026-07-17** [`2c856abbe3`](https://github.com/sgl-project/sglang/commit/2c856abbe3) [#31498](https://github.com/sgl-project/sglang/pull/31498)
  [Fix] Enable chunked input-logprob processing by default to cap peak memory (#31498)
  _Files: `.github/workflows/pr-states.yml`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/lora/backend/triton_backend.py` _+2 more__
- **2026-07-17** [`c546afc147`](https://github.com/sgl-project/sglang/commit/c546afc147) [#31379](https://github.com/sgl-project/sglang/pull/31379)
  [AMD] Register 2 CPU/triton unit + kernel tests for AMD 1-GPU PR CI (#31379)
  _Files: `test/registered/moe/test_zero_experts.py`, `test/registered/unit/distributed/test_cuda_wrapper.py`_
- **2026-07-17** [`d67aa05697`](https://github.com/sgl-project/sglang/commit/d67aa05697) [#31502](https://github.com/sgl-project/sglang/pull/31502)
  Bump FlashInfer to 0.6.15 and revert regressions (#31502)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py` _+3 more__
- **2026-07-17** [`486a56be56`](https://github.com/sgl-project/sglang/commit/486a56be56) [#31304](https://github.com/sgl-project/sglang/pull/31304)
  [CPU] improve silu performance by replacing fp32 div with rcp14 (#31304)
  _Files: `sgl-kernel/csrc/cpu/activation.cpp`, `sgl-kernel/csrc/cpu/conv3d.cpp`, `sgl-kernel/csrc/cpu/decode.cpp`, `sgl-kernel/csrc/cpu/flash_attn.h` _+11 more__
- **2026-07-17** [`8432eafd3d`](https://github.com/sgl-project/sglang/commit/8432eafd3d) [#31292](https://github.com/sgl-project/sglang/pull/31292)
  [Kernel] Decouple KernelBackend from device + device-based CapabilityRequirement (RFC #29630) (#31292)
  _Files: `python/sglang/kernels/README.md`, `python/sglang/kernels/__init__.py`, `python/sglang/kernels/fused_op.py`, `python/sglang/kernels/ops/activation/__init__.py` _+13 more__
- **2026-07-16** [`77d23a796e`](https://github.com/sgl-project/sglang/commit/77d23a796e) [#30164](https://github.com/sgl-project/sglang/pull/30164)
  [1/N] elastic-ep: Add runtime EP scale-up (#30164)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/elastic_ep/elastic_ep.py` _+30 more__
- **2026-07-16** [`bff489284b`](https://github.com/sgl-project/sglang/commit/bff489284b) [#25763](https://github.com/sgl-project/sglang/pull/25763)
  [Feature] Support DeepSeek-V4 Wint4Abf16 and Win4Afp8. (#25763)
  _Files: `python/sglang/jit_kernel/csrc/gemm/per_tensor_quant_fp8.cuh`, `python/sglang/jit_kernel/per_tensor_quant_fp8.py`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py` _+8 more__
- **2026-07-16** [`a614821341`](https://github.com/sgl-project/sglang/commit/a614821341) [#31373](https://github.com/sgl-project/sglang/pull/31373)
  [Docs] Align B200 DeepSeek-V4-Pro balanced recipe with MegaMoE (#31373)
  _Files: `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-07-16** [`e73f323464`](https://github.com/sgl-project/sglang/commit/e73f323464) [#31400](https://github.com/sgl-project/sglang/pull/31400)
  [JIT] Reduce MoE fused gate CI test sweep (#31400)
  _Files: `test/registered/jit/test_moe_fused_gate.py`_
- **2026-07-16** [`0a64139c94`](https://github.com/sgl-project/sglang/commit/0a64139c94) [#30975](https://github.com/sgl-project/sglang/pull/30975)
  Fix --moe-a2a-backend silently ignored for LongCat-2.0 (moe_topk missing from gate) (#30975)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-07-16** [`3a8ddd3fd0`](https://github.com/sgl-project/sglang/commit/3a8ddd3fd0) [#31038](https://github.com/sgl-project/sglang/pull/31038)
  [XPU] Route topk_sigmoid and topk_softmax to AOT sgl-kernel-xpu symbols (#31038)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-07-16** [`871c648203`](https://github.com/sgl-project/sglang/commit/871c648203) [#31388](https://github.com/sgl-project/sglang/pull/31388)
  [NPU]revert add scoring func for GLM 4.7 Flash (#31388)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/models/glm4_moe_lite.py`_
- **2026-07-16** [`edb2059139`](https://github.com/sgl-project/sglang/commit/edb2059139) [#28309](https://github.com/sgl-project/sglang/pull/28309)
  Support Flashinfer one-sided A2A + CuteDSL MoE for Nemotron Ultra (#28309)
  _Files: `python/sglang/srt/layers/moe/flashinfer_cutedsl_moe.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/moe/topk.py` _+3 more__
- **2026-07-16** [`5d004a20c5`](https://github.com/sgl-project/sglang/commit/5d004a20c5) [#29929](https://github.com/sgl-project/sglang/pull/29929)
  Fix FlashInfer A2A top-k ID dtype (#29929)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`, `test/registered/ep/test_flashinfer_a2a.py`_
- **2026-07-15** [`7a973c03a0`](https://github.com/sgl-project/sglang/commit/7a973c03a0) [#31367](https://github.com/sgl-project/sglang/pull/31367)
  [Bugfix] Stamp capture-time num_tokens_per_req in multi-layer EAGLE; close jit_kernel CI filter gaps (#31367)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `test/registered/attention/test_kda_decode_flashinfer.py`, `test/registered/attention/test_trtllm_mha_graph_metadata.py` _+8 more__
- **2026-07-15** [`26cb0fcdda`](https://github.com/sgl-project/sglang/commit/26cb0fcdda) [#30182](https://github.com/sgl-project/sglang/pull/30182)
  Empty `_REQ_TYPES_WITH_OPAQUE_FIELDS` on the msgpack IPC path (#29465 Task 4) (#30182)
  _Files: `.gitignore`, `python/sglang/srt/elastic_ep/expert_backup_client.py`, `python/sglang/srt/elastic_ep/expert_backup_manager.py`, `python/sglang/srt/entrypoints/http_server.py` _+8 more__
- **2026-07-15** [`ec32590025`](https://github.com/sgl-project/sglang/commit/ec32590025) [#30706](https://github.com/sgl-project/sglang/pull/30706)
  feat(moriep): add fp4 combine dtype (SGLANG_MORI_COMBINE_DTYPE=fp4) (#30706)
  _Files: `docker/rocm.Dockerfile`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `test/manual/ep/test_moriep_combine_dtype.py`_
- **2026-07-15** [`e76cc75cfa`](https://github.com/sgl-project/sglang/commit/e76cc75cfa) [#31371](https://github.com/sgl-project/sglang/pull/31371)
  [CI] Remove nightly registrations redundant with scheduled stage runs (#31371)
  _Files: `test/registered/jit/deepseek_v4/test_c128_v2.py`, `test/registered/jit/deepseek_v4/test_c4_v2.py`, `test/registered/jit/deepseek_v4/test_fp4_indexer.py`, `test/registered/jit/diffusion/test_diffusion_modelopt_fp8_scaled_mm.py` _+47 more__
- **2026-07-15** [`241937af87`](https://github.com/sgl-project/sglang/commit/241937af87) [#31107](https://github.com/sgl-project/sglang/pull/31107)
  [NPU] Determine the topk norm_type through scoring_func (#31107)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/models/glm4_moe_lite.py`_
- **2026-07-15** [`980acd6eca`](https://github.com/sgl-project/sglang/commit/980acd6eca) [#29007](https://github.com/sgl-project/sglang/pull/29007)
  Fix MoE TP allreduce to use NCCL symmetric memory via in-pool output allocation (#29007)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` _+2 more__
- **2026-07-15** [`4aadf94146`](https://github.com/sgl-project/sglang/commit/4aadf94146) [#30795](https://github.com/sgl-project/sglang/pull/30795)
  [Kernel] Relocate vendored fla and mamba kernel trees to sglang.kernels (RFC #29630, Phase 2.5, 7/7) (#30795)
  _Files: `benchmark/bench_linear_attention/bench_cutedsl_kda_decode.py`, `benchmark/bench_linear_attention/bench_fused_gate_cumsum.py`, `benchmark/bench_linear_attention/bench_gdn_decode.py`, `benchmark/bench_linear_attention/bench_gdn_prefill.py` _+84 more__
- **2026-07-15** [`532cd337ed`](https://github.com/sgl-project/sglang/commit/532cd337ed) [#28428](https://github.com/sgl-project/sglang/pull/28428)
  [Intel GPU] DeepSeek V4 12/N: use sgl-kernel implementation of silu_and_mul_clamp to run on XPU (#28428)
  _Files: `python/sglang/jit_kernel/dsv4/moe.py`_
- **2026-07-14** [`31548781e0`](https://github.com/sgl-project/sglang/commit/31548781e0) [#31110](https://github.com/sgl-project/sglang/pull/31110)
  [CPU] bypass scoring_func argument in topk for cpu device (#31110)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/cpu/test_spec_eagle_parity_cpu.py`_
- **2026-07-14** [`1a35440c4a`](https://github.com/sgl-project/sglang/commit/1a35440c4a) [#30789](https://github.com/sgl-project/sglang/pull/30789)
  [Kernel] Migrate generic attention kernels to sglang.kernels (RFC #29630, Phase 2.5, 4/7) (#30789)
  _Files: `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/kernels/ops/attention/flash_mla_sm120.py`, `python/sglang/kernels/ops/attention/flash_mla_sm120_triton.py` _+31 more__
- **2026-07-14** [`0fe2dbd42c`](https://github.com/sgl-project/sglang/commit/0fe2dbd42c) [#31169](https://github.com/sgl-project/sglang/pull/31169)
  Split initialize() into orchestration helpers (#31169)
  _Files: `python/sglang/srt/elastic_ep/elastic_ep.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-07-14** [`54f99a21d5`](https://github.com/sgl-project/sglang/commit/54f99a21d5) [#31166](https://github.com/sgl-project/sglang/pull/31166)
  Narrow component dependencies to injected fields instead of ModelRunner (#31166)
  _Files: `python/sglang/srt/elastic_ep/expert_backup_client.py`, `python/sglang/srt/eplb/eplb_manager.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/utils/weight_checker.py` _+1 more__
- **2026-07-14** [`6999007a13`](https://github.com/sgl-project/sglang/commit/6999007a13) [#31165](https://github.com/sgl-project/sglang/pull/31165)
  Drop ModelRunner's duplicated parallel-degree fields and read them via self.ps (#31165)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/elastic_ep/expert_backup_client.py`, `python/sglang/srt/eplb/eplb_manager.py` _+16 more__
- **2026-07-14** [`d6cf2908ce`](https://github.com/sgl-project/sglang/commit/d6cf2908ce) [#31162](https://github.com/sgl-project/sglang/pull/31162)
  Introduce KVCacheConfigurator and migrate KV-cache config logic (#31162)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/kv_pool_runtime.py` _+2 more__
- **2026-07-14** [`08798dba0d`](https://github.com/sgl-project/sglang/commit/08798dba0d) [#31159](https://github.com/sgl-project/sglang/pull/31159)
  Extract MoE/EP setup into a moe_ep_setup module (#31159)
  _Files: `python/sglang/srt/eplb/eplb_manager.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/moe_ep_setup.py`_
- **2026-07-14** [`440aebdfe0`](https://github.com/sgl-project/sglang/commit/440aebdfe0) [#31158](https://github.com/sgl-project/sglang/pull/31158)
  Extract small single-function helpers into modules (#31158)
  _Files: `python/sglang/srt/elastic_ep/elastic_ep.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/misc_utils.py`_
- **2026-07-14** [`c9b4081016`](https://github.com/sgl-project/sglang/commit/c9b4081016) [#31149](https://github.com/sgl-project/sglang/pull/31149)
  Extract expert location updating into EPLBManager (#31149)
  _Files: `python/sglang/srt/eplb/eplb_manager.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-07-14** [`702bddcee8`](https://github.com/sgl-project/sglang/commit/702bddcee8) [#27375](https://github.com/sgl-project/sglang/pull/27375)
  [Model] Add support for JetBrains' Mellum v2 code generation model (#27375)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `docs_new/docs/supported-models/generative_models.mdx`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/mellum.py` _+3 more__
- **2026-07-14** [`9756f768a6`](https://github.com/sgl-project/sglang/commit/9756f768a6) [#30448](https://github.com/sgl-project/sglang/pull/30448)
  Refactor FP4 quantization and remove deprecated JIT kernels (#30448)
  _Files: `benchmark/kernels/flashinfer_allreduce_fusion/README.md`, `benchmark/kernels/flashinfer_allreduce_fusion/benchmark_fused_collective.py`, `benchmark/kernels/quantization/bench_fp4_quant.py`, `docs_new/docs/advanced_features/quantization.mdx` _+34 more__
- **2026-07-14** [`e9ef06c560`](https://github.com/sgl-project/sglang/commit/e9ef06c560) [#30787](https://github.com/sgl-project/sglang/pull/30787)
  [Kernel] Migrate top-level srt/layers stray kernels to sglang.kernels (RFC #29630, Phase 2.5, 3/7) (#30787)
  _Files: `benchmark/kernels/bench_fused_gate_sigmoid_mul_add.py`, `benchmark/kernels/bench_fused_sigmoid_mul.py`, `python/sglang/jit_kernel/dsv4/elementwise.py`, `python/sglang/kernels/ops/attention/__init__.py` _+33 more__
- **2026-07-14** [`ee464fedc6`](https://github.com/sgl-project/sglang/commit/ee464fedc6) [#30786](https://github.com/sgl-project/sglang/pull/30786)
  [Kernel] Migrate scattered MoE kernels to sglang.kernels (RFC #29630, Phase 2.5, 2/7) (#30786)
  _Files: `python/sglang/jit_kernel/tests/test_minimax_m3_mxfp8.py`, `python/sglang/kernels/ops/moe/__init__.py`, `python/sglang/kernels/ops/moe/deepep_waterfill_kernels.py`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py` _+27 more__
- **2026-07-14** [`423b8485fb`](https://github.com/sgl-project/sglang/commit/423b8485fb) [#23754](https://github.com/sgl-project/sglang/pull/23754)
  [Quantization] add humming quantization kernel (#23754)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/pyproject.toml`, `python/sglang/jit_kernel/csrc/moe/moe_permute_prepare.cu`, `python/sglang/jit_kernel/moe_permute_prepare.py` _+29 more__
- **2026-07-13** [`2cf2920d07`](https://github.com/sgl-project/sglang/commit/2cf2920d07) [#28220](https://github.com/sgl-project/sglang/pull/28220)
  [FlashInfer v0.6.13] Use CuTe DSL backend for FlashInfer per-token NVFP4 quantization (#28220)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/nvfp4_online.py`, `python/sglang/srt/model_loader/loader.py`_
- **2026-07-13** [`eb31b5310c`](https://github.com/sgl-project/sglang/commit/eb31b5310c) [#27350](https://github.com/sgl-project/sglang/pull/27350)
  Support Waterfill with MegaMoE backend (#27350)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`, `docs_new/docs/references/environment_variables.mdx` _+10 more__
- **2026-07-13** [`08d6d297e5`](https://github.com/sgl-project/sglang/commit/08d6d297e5) [#29909](https://github.com/sgl-project/sglang/pull/29909)
  [Bugfix][NPU] Fix Hunyuan3 model where MoE's routing_scaling_ratio is missing on NPU (#29909)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`_

## Prefill / Decode Disaggregation  (29 commits)

- **2026-07-20** [`50c118704a`](https://github.com/sgl-project/sglang/commit/50c118704a) [#31325](https://github.com/sgl-project/sglang/pull/31325)
  [diffusion] disagg: handle numpy arrays in cross-role transfer field extraction (#31325)
  _Files: `python/sglang/multimodal_gen/runtime/disaggregation/scheduler_mixin.py`_
- **2026-07-19** [`cce5fe7696`](https://github.com/sgl-project/sglang/commit/cce5fe7696) [#31687](https://github.com/sgl-project/sglang/pull/31687)
  [Scheduler] Move the WAR barrier to right after each `run_batch` launch (#31687)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-07-17** [`2db21daf8d`](https://github.com/sgl-project/sglang/commit/2db21daf8d) [#31584](https://github.com/sgl-project/sglang/pull/31584)
  Fix Heartbeat Checker in KV Manager Disaggregation (#31584)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`_
- **2026-07-17** [`2c64b7782e`](https://github.com/sgl-project/sglang/commit/2c64b7782e) [#31368](https://github.com/sgl-project/sglang/pull/31368)
  [AMD][PD] Fix early-send cached-prefix KV racing the prefill forward on mori (#31368)
  _Files: `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/disaggregation/prefill.py`_
- **2026-07-17** [`68d324d697`](https://github.com/sgl-project/sglang/commit/68d324d697) [#31306](https://github.com/sgl-project/sglang/pull/31306)
  [PD] Fix send_multipart blocking after prefill failure (#31306)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`_
- **2026-07-16** [`5cbea10e2f`](https://github.com/sgl-project/sglang/commit/5cbea10e2f) [#31134](https://github.com/sgl-project/sglang/pull/31134)
  Fix LongCat n-gram embedding in PD-disaggregated scheduler loops (#31134)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`_
- **2026-07-16** [`095a817612`](https://github.com/sgl-project/sglang/commit/095a817612) [#26411](https://github.com/sgl-project/sglang/pull/26411)
  [Bugfix][HiCache] measure load-back duration with CUDA events (#26411)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` _+6 more__
- **2026-07-15** [`2d00e20a52`](https://github.com/sgl-project/sglang/commit/2d00e20a52) [#30997](https://github.com/sgl-project/sglang/pull/30997)
  [Disagg][Qwen3.5] Fix heterogeneous attn-TP scatter transfer: GDN conv sub-block slice + GQA replicated-KV head map (#30997)
  _Files: `python/sglang/srt/configs/mamba_utils.py`, `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/staging_buffer.py` _+5 more__
- **2026-07-15** [`c879f3da5c`](https://github.com/sgl-project/sglang/commit/c879f3da5c) [#30036](https://github.com/sgl-project/sglang/pull/30036)
  [diffusion] rl: support rl rollout for the wan pipeline via a per-request scheduler switch (#30036)
  _Files: `python/sglang/multimodal_gen/runtime/disaggregation/scheduler_mixin.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/timestep_preparation.py`, `python/sglang/multimodal_gen/runtime/post_training/rollout_denoising_mixin.py`, `python/sglang/multimodal_gen/runtime/post_training/rollout_scheduler.py`_
- **2026-07-15** [`8ed82afcc8`](https://github.com/sgl-project/sglang/commit/8ed82afcc8) [#25663](https://github.com/sgl-project/sglang/pull/25663)
  [MoE Refactor] [NPU] Refactor Ascend MoE implementation to reduce code duplication and align with community design (#25663)
  _Files: `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`, `docs_new/docs/advanced_features/pd_disaggregation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_optimization.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_r1.mdx` _+50 more__
- **2026-07-15** [`f2c875d1c8`](https://github.com/sgl-project/sglang/commit/f2c875d1c8) [#30748](https://github.com/sgl-project/sglang/pull/30748)
  [PD] Route PD server warmup to every DP rank (#30748)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `test/registered/unit/entrypoints/test_http_server_warmup.py`_
- **2026-07-15** [`1afab30577`](https://github.com/sgl-project/sglang/commit/1afab30577) [#29432](https://github.com/sgl-project/sglang/pull/29432)
  Fix bookkeeping fields not encapsulated with real allocations in normal alloc, PD pre-alloc, DFlash and EAGLE (#29432)
  _Files: `python/sglang/kernels/ops/speculative/__init__.py`, `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py` _+8 more__
- **2026-07-15** [`c315df49bb`](https://github.com/sgl-project/sglang/commit/c315df49bb) [#29430](https://github.com/sgl-project/sglang/pull/29430)
  Fix abusing presence of req.req_pool_idx to indicate the presence of req.kv resources (#29430)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/mem_cache/common.py` _+2 more__
- **2026-07-15** [`2d979f1d8c`](https://github.com/sgl-project/sglang/commit/2d979f1d8c) [#29429](https://github.com/sgl-project/sglang/pull/29429)
  Let the presence of req.kv indicate the existence of owned kv resources (#29429)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py` _+4 more__
- **2026-07-15** [`27256aee5b`](https://github.com/sgl-project/sglang/commit/27256aee5b) [#29428](https://github.com/sgl-project/sglang/pull/29428)
  Let cache backend do not couple with owned committed kv details and avoid kv_committed_freed/kv_overallocated_freed fields (#29428)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py` _+20 more__
- **2026-07-15** [`d8d76c4d12`](https://github.com/sgl-project/sglang/commit/d8d76c4d12) [#29427](https://github.com/sgl-project/sglang/pull/29427)
  Introduce req.kv container for coupled owned kv field lifecycle (#29427)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_allocator.py`, `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/managers/schedule_batch.py` _+20 more__
- **2026-07-15** [`201ddeaba1`](https://github.com/sgl-project/sglang/commit/201ddeaba1) [#30677](https://github.com/sgl-project/sglang/pull/30677)
  Avoid relaying per-step outputs through ScheduleBatch fields in disagg prefill and PP (#30677)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`_
- **2026-07-14** [`cb47a68717`](https://github.com/sgl-project/sglang/commit/cb47a68717) [#31173](https://github.com/sgl-project/sglang/pull/31173)
  [PD] Stride KV token->page indices on device before D2H copy (#31173)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/mem_cache/common.py`_
- **2026-07-14** [`a5c3e0283f`](https://github.com/sgl-project/sglang/commit/a5c3e0283f) [#30351](https://github.com/sgl-project/sglang/pull/30351)
  [Bug fix] Account for KV replication fan-out in transfer-byte metrics (#30351)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py` _+1 more__
- **2026-07-14** [`bbb5702a3c`](https://github.com/sgl-project/sglang/commit/bbb5702a3c) [#30937](https://github.com/sgl-project/sglang/pull/30937)
  fix: avoid double KV release on disaggregated prefill grammar errors (#30937)
  _Files: `python/sglang/srt/disaggregation/prefill.py`_
- **2026-07-14** [`725920915f`](https://github.com/sgl-project/sglang/commit/725920915f) [#31161](https://github.com/sgl-project/sglang/pull/31161)
  Introduce ModelRunner.ps ParallelState (#31161)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/parallel_state_wrapper.py`, `python/sglang/srt/hardware_backend/mlx/tp_worker.py` _+24 more__
- **2026-07-14** [`1dc48c2c3b`](https://github.com/sgl-project/sglang/commit/1dc48c2c3b) [#31160](https://github.com/sgl-project/sglang/pull/31160)
  Absorb capturer setup and extract the shared-mooncake gate (#31160)
  _Files: `python/sglang/srt/distributed/device_communicators/mooncake_transfer_engine.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/state_capturer/indexer_topk.py`, `python/sglang/srt/state_capturer/routed_experts.py` _+1 more__
- **2026-07-14** [`b1a60ad00d`](https://github.com/sgl-project/sglang/commit/b1a60ad00d) [#31145](https://github.com/sgl-project/sglang/pull/31145)
  Clean up ModelRunner by renaming effective-token property and remove dead code (#31145)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-07-14** [`1b4176cc46`](https://github.com/sgl-project/sglang/commit/1b4176cc46) [#31075](https://github.com/sgl-project/sglang/pull/31075)
  [PD] Fix optimistic prefill inflight-queue hangs on parked/aborted reqs (#31075)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/prefill.py`_
- **2026-07-14** [`78dc581518`](https://github.com/sgl-project/sglang/commit/78dc581518) [#30839](https://github.com/sgl-project/sglang/pull/30839)
  [bug-fix] Stabilize GLM-5.2 MTP IndexShare across PD and CUDA graph replay (#30839)
  _Files: `python/sglang/srt/debug_utils/pr_fix_toggle.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` _+15 more__
- **2026-07-13** [`a909077d22`](https://github.com/sgl-project/sglang/commit/a909077d22) [#27408](https://github.com/sgl-project/sglang/pull/27408)
  Return top-p/top-k sampling mask/nucleas (#27408)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/environ.py` _+16 more__
- **2026-07-13** [`e2728ac504`](https://github.com/sgl-project/sglang/commit/e2728ac504) [#30998](https://github.com/sgl-project/sglang/pull/30998)
  [Spec] Remove dead `padded_static_len` and stale `SGLANG_ENABLE_SPEC_V2` references (#30998)
  _Files: `.claude/skills/cookbook-migrate-model/SKILL.md`, `docs_new/docs/advanced_features/pd_disaggregation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_r1.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_v3_2.mdx` _+61 more__
- **2026-07-13** [`a74bee2261`](https://github.com/sgl-project/sglang/commit/a74bee2261) [#30352](https://github.com/sgl-project/sglang/pull/30352)
  [PD] Handle NIXL abort notifications (#30352)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-07-13** [`9dd57ef8c4`](https://github.com/sgl-project/sglang/commit/9dd57ef8c4) [#30616](https://github.com/sgl-project/sglang/pull/30616)
  [mem_cache][7/N] refactor: move  MLATokenToKVPoolHost to pool_host.mla (#30616)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` _+9 more__

## Multimodal  (27 commits)

- **2026-07-20** [`2eed35d738`](https://github.com/sgl-project/sglang/commit/2eed35d738) [#31301](https://github.com/sgl-project/sglang/pull/31301)
  perf: avoid temporary VLM encoder gather padding (#31301)
  _Files: `python/sglang/srt/multimodal/mm_utils.py`, `test/registered/unit/multimodal/test_mrope_encoder_utils.py`_
- **2026-07-20** [`9f8e916131`](https://github.com/sgl-project/sglang/commit/9f8e916131) [#31263](https://github.com/sgl-project/sglang/pull/31263)
  [diffusion] post_training: run weight update under torch.inference_mode() (#31263)
  _Files: `python/sglang/multimodal_gen/runtime/post_training/weights_updater.py`_
- **2026-07-20** [`6a25dd7b5f`](https://github.com/sgl-project/sglang/commit/6a25dd7b5f) [#31298](https://github.com/sgl-project/sglang/pull/31298)
  fix: warm up Kimi VLM vision encoder at startup (#31298)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `test/registered/unit/entrypoints/test_server_warmup.py`_
- **2026-07-18** [`573c075fef`](https://github.com/sgl-project/sglang/commit/573c075fef) [#31665](https://github.com/sgl-project/sglang/pull/31665)
  CI: synchronize prefill graph test fixtures (#31665)
  _Files: `test/registered/unit/configs/test_multimodal_piecewise_cuda_graph.py`, `test/registered/unit/model_executor/runner/test_prefill_cuda_graph_padding.py`_
- **2026-07-18** [`44e4999ab2`](https://github.com/sgl-project/sglang/commit/44e4999ab2) [#31354](https://github.com/sgl-project/sglang/pull/31354)
  [Diffusion] Use SGLang server for ERNIE-Image prompt enhancement (#31354)
  _Files: `docs_new/docs/sglang-diffusion/api/cli.mdx`, `docs_new/docs/sglang-diffusion/models_with_pe.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/pe_loader.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`_
- **2026-07-17** [`d389039337`](https://github.com/sgl-project/sglang/commit/d389039337) [#31233](https://github.com/sgl-project/sglang/pull/31233)
  [diffusion] Opt in Qwen and Wan multi-output conditioning expansion (#31233)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py` _+1 more__
- **2026-07-17** [`85ac56c823`](https://github.com/sgl-project/sglang/commit/85ac56c823) [#30109](https://github.com/sgl-project/sglang/pull/30109)
  docs: simplify diffusion new model guide (#30109)
  _Files: `docs_new/docs/sglang-diffusion/support_new_models.mdx`_
- **2026-07-17** [`40a3bd7659`](https://github.com/sgl-project/sglang/commit/40a3bd7659) [#31507](https://github.com/sgl-project/sglang/pull/31507)
  [Docs] Mistral Medium 3.5 cookbook: replace stale day-0 dev images with latest (#31507)
  _Files: `docs_new/cookbook/autoregressive/Mistral/Mistral-Medium-3.5.mdx`_
- **2026-07-16** [`8c9833f9a9`](https://github.com/sgl-project/sglang/commit/8c9833f9a9) [#31454](https://github.com/sgl-project/sglang/pull/31454)
  cookbook(qwen3.5): bump AMD ROCm docker images to v0.5.15.post1 (#31454)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3.5.mdx`_
- **2026-07-16** [`3bc7c54111`](https://github.com/sgl-project/sglang/commit/3bc7c54111) [#31467](https://github.com/sgl-project/sglang/pull/31467)
  [NPU] Updated baselines for GLM-Image (#31467)
  _Files: `python/sglang/multimodal_gen/test/server/ascend/perf_baselines_npu.json`_
- **2026-07-16** [`f8eac995aa`](https://github.com/sgl-project/sglang/commit/f8eac995aa) [#31313](https://github.com/sgl-project/sglang/pull/31313)
  [diffusion] test: fix GLM-Image AR model-path to resolve local snapshot subfolder (#31313)
  _Files: `python/sglang/multimodal_gen/test/single_test_file/test_ar_models.py`_
- **2026-07-16** [`22453ca63c`](https://github.com/sgl-project/sglang/commit/22453ca63c) [#31390](https://github.com/sgl-project/sglang/pull/31390)
  docker: build HPC-Ops into the GPU image (#31390)
  _Files: `docker/Dockerfile`_
- **2026-07-16** [`14095ef78a`](https://github.com/sgl-project/sglang/commit/14095ef78a) [#31342](https://github.com/sgl-project/sglang/pull/31342)
  [AMD] Disable CUDA IPC multimodal transport on ROCm in MMMU VLM tests (#31342)
  _Files: `python/sglang/test/kits/mmmu_vlm_kit.py`_
- **2026-07-15** [`5abec3fbf8`](https://github.com/sgl-project/sglang/commit/5abec3fbf8) [#31343](https://github.com/sgl-project/sglang/pull/31343)
  Fix MiMo-V2 on Blackwell: FA3 fallback and TP-aware audio weight loading (#31343)
  _Files: `python/sglang/srt/models/mimo_audio.py`, `python/sglang/srt/models/mimo_v2.py`, `python/sglang/srt/models/mimo_v2_asr.py`, `python/sglang/srt/models/mimo_vl.py`_
- **2026-07-15** [`9d147fdca1`](https://github.com/sgl-project/sglang/commit/9d147fdca1) [#31027](https://github.com/sgl-project/sglang/pull/31027)
  [Multimodal] Support n>1 outputs for GLM-Image generation (#31027)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/glm_image.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/glm_image.py` _+2 more__
- **2026-07-15** [`c9b17403e7`](https://github.com/sgl-project/sglang/commit/c9b17403e7) [#30621](https://github.com/sgl-project/sglang/pull/30621)
  Fix image URL response for multiple outputs (#30621)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/test/unit/test_openai_image_api.py`_
- **2026-07-15** [`947a14d617`](https://github.com/sgl-project/sglang/commit/947a14d617) [#30904](https://github.com/sgl-project/sglang/pull/30904)
  feat: unify multimodal feature transport (#30904)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py`, `python/sglang/srt/multimodal/processors/midashenglm.py`, `python/sglang/srt/multimodal/processors/moss_vl.py` _+3 more__
- **2026-07-15** [`fbcbe0a986`](https://github.com/sgl-project/sglang/commit/fbcbe0a986) [#30651](https://github.com/sgl-project/sglang/pull/30651)
  cookbook(deepseek-v4): add MORI disagg backend for AMD + bump MI355X image (#30651)
  _Files: `docs_new/src/snippets/_playground.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-07-15** [`43124cdd90`](https://github.com/sgl-project/sglang/commit/43124cdd90) [#30867](https://github.com/sgl-project/sglang/pull/30867)
  fix: fix image benchmark backend parity (#30867)
  _Files: `python/sglang/benchmark/datasets/image.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`_
- **2026-07-15** [`90f10cbe26`](https://github.com/sgl-project/sglang/commit/90f10cbe26) [#31029](https://github.com/sgl-project/sglang/pull/31029)
  [diffusion] post_training: Add LoRA IPC weight sync via lora_merge mode (#31029)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/post_training/io_struct.py`, `python/sglang/multimodal_gen/runtime/entrypoints/post_training/weights_api.py`, `python/sglang/multimodal_gen/runtime/pipelines/stable_diffusion_3.py`, `python/sglang/multimodal_gen/runtime/post_training/gpu_worker_post_training_mixin.py` _+1 more__
- **2026-07-14** [`43241b7f3f`](https://github.com/sgl-project/sglang/commit/43241b7f3f) [#31177](https://github.com/sgl-project/sglang/pull/31177)
  [diffusion] model: support fal Ideogram V4 Fast and Instant (#31177)
  _Files: `docs_new/cookbook/diffusion/Ideogram/Ideogram4.mdx`, `docs_new/docs/sglang-diffusion/compatibility_matrix.mdx`, `python/sglang/multimodal_gen/configs/models/dits/__init__.py`, `python/sglang/multimodal_gen/configs/models/dits/ideogram.py` _+13 more__
- **2026-07-14** [`7e0b29ac03`](https://github.com/sgl-project/sglang/commit/7e0b29ac03) [#31132](https://github.com/sgl-project/sglang/pull/31132)
  docs: add VLA card image to cookbook overview (#31132)
  _Files: `docs_new/cards/VLA-card.png`, `docs_new/cookbook/intro.mdx`_
- **2026-07-14** [`23b2c6f1ce`](https://github.com/sgl-project/sglang/commit/23b2c6f1ce) [#31101](https://github.com/sgl-project/sglang/pull/31101)
  docs: fix diffusion cookbook overview cards (#31101)
  _Files: `docs_new/cards/logos/joyai-echo.svg`, `docs_new/cookbook/diffusion/JoyEcho/JoyEcho.mdx`, `docs_new/cookbook/diffusion/intro.mdx`, `docs_new/docs.json`_
- **2026-07-14** [`41ad0d9c26`](https://github.com/sgl-project/sglang/commit/41ad0d9c26) [#30620](https://github.com/sgl-project/sglang/pull/30620)
  Allow prefill breakable CUDA graph for Qwen3.5 via multimodal opt-in allowlist (#30620)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-07-14** [`33f83011e0`](https://github.com/sgl-project/sglang/commit/33f83011e0) [#30869](https://github.com/sgl-project/sglang/pull/30869)
  fix: fix Kimi-VL encoder parallelism (#30869)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/kimi_vl.py`, `python/sglang/srt/models/kimi_vl_moonvit.py`, `python/sglang/srt/multimodal/mm_utils.py` _+6 more__
- **2026-07-13** [`92fc692411`](https://github.com/sgl-project/sglang/commit/92fc692411) [#31064](https://github.com/sgl-project/sglang/pull/31064)
  fix: include OpenSSL headers in runtime image (#31064)
  _Files: `docker/Dockerfile`_
- **2026-07-13** [`7da30f4e55`](https://github.com/sgl-project/sglang/commit/7da30f4e55) [#30889](https://github.com/sgl-project/sglang/pull/30889)
  feat: enable piecewise prefill graph for Kimi K2.5/K2.7 (#30889)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/configs/test_multimodal_piecewise_cuda_graph.py`_

## KV Cache / Memory  (20 commits)

- **2026-07-20** [`49b9c46f41`](https://github.com/sgl-project/sglang/commit/49b9c46f41) [#27877](https://github.com/sgl-project/sglang/pull/27877)
  [dLLM] Reuse block KV/req slots in place across FDFO rounds (#27877)
  _Files: `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/allocation.py` _+1 more__
- **2026-07-19** [`b3570a4531`](https://github.com/sgl-project/sglang/commit/b3570a4531) [#31655](https://github.com/sgl-project/sglang/pull/31655)
  [Refactor] Unify input logprob processing on a single chunked path (#31655)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/logprob_processor.py`, `python/sglang/srt/lora/layers.py`, `python/sglang/srt/lora/utils.py` _+1 more__
- **2026-07-19** [`942bf04ef9`](https://github.com/sgl-project/sglang/commit/942bf04ef9) [#29353](https://github.com/sgl-project/sglang/pull/29353)
  [Scheduler] Add `SGLANG_FORCE_COARSE_WAR_BARRIER` opt-in for a whole-forward WAR barrier (#29353)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-07-18** [`10908a6793`](https://github.com/sgl-project/sglang/commit/10908a6793) [#31662](https://github.com/sgl-project/sglang/pull/31662)
  [Fix] Respect cache_protected_len in ChunkCache and disabled-radix release paths (#31662)
  _Files: `python/sglang/srt/mem_cache/chunk_cache.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `test/registered/unit/mem_cache/test_pure_swa_chunk_cache.py`_
- **2026-07-18** [`5609f8e509`](https://github.com/sgl-project/sglang/commit/5609f8e509) [#31643](https://github.com/sgl-project/sglang/pull/31643)
  Reset only the used mamba state on radix cache hit (#31643)
  _Files: `python/sglang/srt/mem_cache/mamba_radix_cache.py`, `test/registered/unit/mem_cache/test_mamba_unittest.py`_
- **2026-07-18** [`48ae829f6e`](https://github.com/sgl-project/sglang/commit/48ae829f6e) [#31648](https://github.com/sgl-project/sglang/pull/31648)
  Reset only the used mamba state on unified radix cache (#31648)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/mamba_component.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-07-18** [`38b29dcd6c`](https://github.com/sgl-project/sglang/commit/38b29dcd6c) [#31653](https://github.com/sgl-project/sglang/pull/31653)
  Fix SM120 NVFP4 KV cache test OOM (#31653)
  _Files: `test/registered/models_e2e/test_llama8b_nvfp4_kv_cache_sm120.py`, `test/registered/quant/test_llama8b_nvfp4_kv_cache_sm120.py`_
- **2026-07-18** [`19c53c44a0`](https://github.com/sgl-project/sglang/commit/19c53c44a0) [#31639](https://github.com/sgl-project/sglang/pull/31639)
  [Fix] Account zero-logprob sequences correctly in chunked logprob stitching (#31639)
  _Files: `python/sglang/srt/layers/logprob_processor.py`, `test/registered/unit/layers/test_logprob_chunk_stitching.py`_
- **2026-07-17** [`44e3dd2713`](https://github.com/sgl-project/sglang/commit/44e3dd2713) [#30658](https://github.com/sgl-project/sglang/pull/30658)
  [HiCache] Optimize HiCache host pool free-list release (#30658)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/pool_host/base.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py`_
- **2026-07-16** [`7cd55c6818`](https://github.com/sgl-project/sglang/commit/7cd55c6818) [#19320](https://github.com/sgl-project/sglang/pull/19320)
  [HiCache] Optimize L2 mem allocation when cache miss in L3 (#19320)
  _Files: `benchmark/hf3fs/bench_zerocopy.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` _+3 more__
- **2026-07-16** [`b296e1a503`](https://github.com/sgl-project/sglang/commit/b296e1a503) [#30535](https://github.com/sgl-project/sglang/pull/30535)
  [hicache]: add  mamba concurrency io transfer kernel (#30535)
  _Files: `python/sglang/jit_kernel/csrc/kvcacheio/transfer_mamba.cuh`, `python/sglang/jit_kernel/transfer_mamba.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `test/registered/jit/test_transfer_mamba.py`_
- **2026-07-16** [`5af65d8542`](https://github.com/sgl-project/sglang/commit/5af65d8542) [#29609](https://github.com/sgl-project/sglang/pull/29609)
  [DeepSeek-V4] Support BF16 Compress State for Online C128 (#29609)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/c128_online_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/online_c128_mtp.cuh`, `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/jit_kernel/dsv4/online_c128_mtp.py` _+3 more__
- **2026-07-15** [`7e7129acd7`](https://github.com/sgl-project/sglang/commit/7e7129acd7) [#31321](https://github.com/sgl-project/sglang/pull/31321)
  [Bugfix] Release Mamba cache after PP dynamic chunk profiling (#31321)
  _Files: `python/sglang/srt/managers/scheduler_pp_mixin.py`_
- **2026-07-15** [`23f2b77d82`](https://github.com/sgl-project/sglang/commit/23f2b77d82) [#27106](https://github.com/sgl-project/sglang/pull/27106)
  Make UTs compatible for XPU (#27106)
  _Files: `python/sglang/srt/debug_utils/dump_comparator.py`, `test/registered/debug_utils/test_tensor_dump_forward_hook.py`, `test/registered/kernels/test_fused_topk_deepseek.py`, `test/registered/unit/mem_cache/test_radix_cache_unit.py`_
- **2026-07-15** [`b4fdce3b63`](https://github.com/sgl-project/sglang/commit/b4fdce3b63) [#31092](https://github.com/sgl-project/sglang/pull/31092)
  Fix post-capture KV sizing for SWA pools (#31092)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/server_args.py`_
- **2026-07-14** [`463a3f4248`](https://github.com/sgl-project/sglang/commit/463a3f4248) [#31059](https://github.com/sgl-project/sglang/pull/31059)
  [Mamba] Support configurable conv-window layouts (#31059)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/mem_cache/test_mamba_unittest.py`_
- **2026-07-14** [`cfd17301a8`](https://github.com/sgl-project/sglang/commit/cfd17301a8) [#31163](https://github.com/sgl-project/sglang/pull/31163)
  Extract per-architecture KV-cache pool builders into KVCacheConfigurator (#31163)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/model_executor/pool_configurator.py` _+1 more__
- **2026-07-14** [`45dfa318fb`](https://github.com/sgl-project/sglang/commit/45dfa318fb) [#31147](https://github.com/sgl-project/sglang/pull/31147)
  Extract kv cache dtype configuration into mem_cache (#31147)
  _Files: `python/sglang/srt/mem_cache/kv_cache_dtype.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-07-14** [`afa3c06d1f`](https://github.com/sgl-project/sglang/commit/afa3c06d1f) [#30468](https://github.com/sgl-project/sglang/pull/30468)
  Using UnifiedRadixTree by default for SWA, Mamba, and DSA models (#30468)
  _Files: `python/sglang/srt/kv_canary/radix_cache_walker.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/registry.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+2 more__
- **2026-07-13** [`978bce2063`](https://github.com/sgl-project/sglang/commit/978bce2063) [#29191](https://github.com/sgl-project/sglang/pull/29191)
  [HiCache & HybridModel] nixl hicache backend support hybrid models (#29191)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/storage/nixl/README.md`, `python/sglang/srt/mem_cache/storage/nixl/hicache_nixl.py`, `test/registered/unit/mem_cache/test_hicache_nixl_storage.py`_

## Scheduler / Batching  (19 commits)

- **2026-07-20** [`fce5c75a30`](https://github.com/sgl-project/sglang/commit/fce5c75a30) [#31701](https://github.com/sgl-project/sglang/pull/31701)
  [NPU] Fix vit graph tnd cu seqlens (#31701)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`, `python/sglang/srt/managers/mm_utils.py`_
- **2026-07-20** [`b15a83983c`](https://github.com/sgl-project/sglang/commit/b15a83983c) [#31746](https://github.com/sgl-project/sglang/pull/31746)
  [Fix] Release hierarchical cache host pool on graceful shutdown (#31746)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/hicache/test_hicache_storage.py`_
- **2026-07-18** [`071e649288`](https://github.com/sgl-project/sglang/commit/071e649288) [#25213](https://github.com/sgl-project/sglang/pull/25213)
  fix(rpc) Synchronize RPC requests only within the TP group. (#25213)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-07-18** [`ab3d421c30`](https://github.com/sgl-project/sglang/commit/ab3d421c30) [#31580](https://github.com/sgl-project/sglang/pull/31580)
  [plugin] oot torch profiler activity support (#31580)
  _Files: `python/sglang/srt/managers/scheduler_components/profiler_manager.py`, `python/sglang/srt/platforms/device_mixin.py`, `python/sglang/srt/utils/profile_utils.py`_
- **2026-07-18** [`f926c30c57`](https://github.com/sgl-project/sglang/commit/f926c30c57) [#31369](https://github.com/sgl-project/sglang/pull/31369)
  Revert "Fix mamba track-boundary seqlen under overlap scheduler (#31369)" (#31622)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`_
- **2026-07-17** [`444bbd866d`](https://github.com/sgl-project/sglang/commit/444bbd866d) [#31539](https://github.com/sgl-project/sglang/pull/31539)
  [CI] Fix invalid suite name breaking all PR test lanes (#31539)
  _Files: `test/registered/unit/managers/test_scheduler_init_req_max_new_tokens.py`_
- **2026-07-17** [`bf417440e9`](https://github.com/sgl-project/sglang/commit/bf417440e9) [#22591](https://github.com/sgl-project/sglang/pull/22591)
  [Scheduler] Add `SGLANG_MAX_NEW_TOKENS_LIMIT` to cap per-request `max_new_tokens` (#22591)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_init_req_max_new_tokens.py`_
- **2026-07-17** [`dfa6278370`](https://github.com/sgl-project/sglang/commit/dfa6278370) [#31517](https://github.com/sgl-project/sglang/pull/31517)
  [Fix] Publish idle scheduler metrics immediately when the running-reqs gauge is stale (#31517)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`_
- **2026-07-17** [`0675d3033f`](https://github.com/sgl-project/sglang/commit/0675d3033f) [#31369](https://github.com/sgl-project/sglang/pull/31369)
  Fix mamba track-boundary seqlen under overlap scheduler (#31369)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`_
- **2026-07-16** [`d28e35b1a1`](https://github.com/sgl-project/sglang/commit/d28e35b1a1) [#31495](https://github.com/sgl-project/sglang/pull/31495)
  Fix num_running_reqs gauge on disagg prefill servers (#31495)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`_
- **2026-07-16** [`db7e6807de`](https://github.com/sgl-project/sglang/commit/db7e6807de) [#30682](https://github.com/sgl-project/sglang/pull/30682)
  [BugFix] Preserve tokenizer worker fanout when `skip_tokenizer_init` is enabled (#30682)
  _Files: `python/sglang/srt/managers/scheduler_components/ipc_channels.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/server_args.py`, `test/registered/tokenizer/test_skip_tokenizer_init.py` _+1 more__
- **2026-07-16** [`b871a509e6`](https://github.com/sgl-project/sglang/commit/b871a509e6) [#31392](https://github.com/sgl-project/sglang/pull/31392)
  [Fix] Wire the detokenizer soft watchdog into the multi-http-worker event loop (#31392)
  _Files: `python/sglang/srt/managers/multi_tokenizer_mixin.py`_
- **2026-07-16** [`1c4892d7bb`](https://github.com/sgl-project/sglang/commit/1c4892d7bb) [#27998](https://github.com/sgl-project/sglang/pull/27998)
  [Mamba] Fix spec-v2 + extra_buffer crash (guard None mamba_next_track_idx) (#27998)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-07-15** [`01343d2759`](https://github.com/sgl-project/sglang/commit/01343d2759) [#30676](https://github.com/sgl-project/sglang/pull/30676)
  Avoid implicit running_batch access in dllm and pdmux scheduling (#30676)
  _Files: `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/multiplex/multiplexing_mixin.py`_
- **2026-07-15** [`21c62b9830`](https://github.com/sgl-project/sglang/commit/21c62b9830) [#30675](https://github.com/sgl-project/sglang/pull/30675)
  Rewrite pause_generation retract path as req-level release and requeue for clarity (#30675)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_
- **2026-07-15** [`1967b9ec99`](https://github.com/sgl-project/sglang/commit/1967b9ec99) [#30674](https://github.com/sgl-project/sglang/pull/30674)
  Fix missed hisparse release and stale field cleanup in pause retract (#30674)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_
- **2026-07-15** [`b6cc897fea`](https://github.com/sgl-project/sglang/commit/b6cc897fea) [#30673](https://github.com/sgl-project/sglang/pull/30673)
  Fix non-existent abort mode in Scheduler.pause_generation and inline retract_all (#30673)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_
- **2026-07-15** [`861d97d24d`](https://github.com/sgl-project/sglang/commit/861d97d24d) [#30669](https://github.com/sgl-project/sglang/pull/30669)
  Remove dead ScheduleBatch fields and avoid inplace seq_lens bump (#30669)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/managers/test_schedule_batch_prepare_for_decode.py`_
- **2026-07-14** [`50d1edaa7f`](https://github.com/sgl-project/sglang/commit/50d1edaa7f) [#31222](https://github.com/sgl-project/sglang/pull/31222)
  [misc] Move SchedulerRecvSkipper into scheduler_components (#31222)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/managers/scheduler_components/recv_skipper.py`, `test/registered/unit/managers/test_scheduler_recv_skipper.py`_

## Speculative Decoding  (19 commits)

- **2026-07-20** [`35f2d4f761`](https://github.com/sgl-project/sglang/commit/35f2d4f761) [#31273](https://github.com/sgl-project/sglang/pull/31273)
  Fix no-padding CUDA graph admission (#31273)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`_
- **2026-07-17** [`01a96720c6`](https://github.com/sgl-project/sglang/commit/01a96720c6) [#31620](https://github.com/sgl-project/sglang/pull/31620)
  [spec decoding] replace torch.multinomial with several native torch op in rejection sampling (#31620)
  _Files: `python/sglang/srt/speculative/spec_utils.py`_
- **2026-07-17** [`e2d2e8d07e`](https://github.com/sgl-project/sglang/commit/e2d2e8d07e) [#31614](https://github.com/sgl-project/sglang/pull/31614)
  [spec decoding] fix multi_layer_eagle rotate_input_ids kernel registration (#31614)
  _Files: `python/sglang/kernels/ops/speculative/__init__.py`, `python/sglang/kernels/ops/speculative/multi_layer_eagle.py`_
- **2026-07-17** [`d310fce85f`](https://github.com/sgl-project/sglang/commit/d310fce85f) [#31519](https://github.com/sgl-project/sglang/pull/31519)
  [Fix] Update PR #25015 revert for fused topk=1 draft postprocess (#31519)
  _Files: `python/sglang/srt/debug_utils/pr_fix_toggle.py`_
- **2026-07-16** [`dc0b3eb68f`](https://github.com/sgl-project/sglang/commit/dc0b3eb68f) [#30948](https://github.com/sgl-project/sglang/pull/30948)
  [2/3] [EAGLE] perf: Fuse TP vocab-parallel embedding (#30948)
  _Files: `python/sglang/kernels/ops/__init__.py`, `python/sglang/kernels/ops/embeddings/__init__.py`, `python/sglang/kernels/ops/embeddings/vocab_parallel_embedding.py`, `python/sglang/srt/layers/vocab_parallel_embedding.py` _+3 more__
- **2026-07-16** [`d539bf2cda`](https://github.com/sgl-project/sglang/commit/d539bf2cda) [#30947](https://github.com/sgl-project/sglang/pull/30947)
  [1/3] [EAGLE] perf: Fuse topk=1 draft postprocess (#30947)
  _Files: `python/sglang/kernels/ops/speculative/__init__.py`, `python/sglang/kernels/ops/speculative/topk1.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/jit/benchmark/bench_spec_topk1.py` _+2 more__
- **2026-07-16** [`9a4d640244`](https://github.com/sgl-project/sglang/commit/9a4d640244) [#31434](https://github.com/sgl-project/sglang/pull/31434)
  [Perf] Cache uniform ragged-verify layout for DSpark verify-all compact (#31434)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_planner.py`_
- **2026-07-16** [`fc1e3797b7`](https://github.com/sgl-project/sglang/commit/fc1e3797b7) [#31255](https://github.com/sgl-project/sglang/pull/31255)
  [Spec] Split the capture width from `num_tokens_per_req` and gate replay on it (#31255)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/model_executor/runner/base_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+5 more__
- **2026-07-16** [`1f34911de7`](https://github.com/sgl-project/sglang/commit/1f34911de7) [#30456](https://github.com/sgl-project/sglang/pull/30456)
  [NemotronH] Load shared embed_tokens/lm_head in MTP draft weights (#30456)
  _Files: `python/sglang/srt/models/nemotron_h.py`, `test/registered/unit/models/test_nemotron_h_weight_loading.py`_
- **2026-07-16** [`b55228cfdb`](https://github.com/sgl-project/sglang/commit/b55228cfdb) [#31380](https://github.com/sgl-project/sglang/pull/31380)
  [Spec] Consolidate the verify step into eagle_worker_common.run_eagle_verify (#31380)
  _Files: `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-07-16** [`ac4fa6496c`](https://github.com/sgl-project/sglang/commit/ac4fa6496c) [#31294](https://github.com/sgl-project/sglang/pull/31294)
  Skip no-op EAGLE sampling renormalization (#31294)
  _Files: `python/sglang/srt/speculative/eagle_utils.py`_
- **2026-07-15** [`b0b2dfbda1`](https://github.com/sgl-project/sglang/commit/b0b2dfbda1) [#31375](https://github.com/sgl-project/sglang/pull/31375)
  [Spec] Extract the shared draft() tail into build_eagle_verify_input (#31375)
  _Files: `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`, `test/registered/unit/spec/test_eagle_worker_v2_topk1_fastpath.py`_
- **2026-07-15** [`dc078ddd2a`](https://github.com/sgl-project/sglang/commit/dc078ddd2a) [#31257](https://github.com/sgl-project/sglang/pull/31257)
  [Spec] Extract stateless draft prepare helpers into eagle_worker_common (#31257)
  _Files: `python/sglang/srt/kv_canary/plan_input.py`, `python/sglang/srt/speculative/base_spec_worker.py`, `python/sglang/srt/speculative/eagle_worker_common.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` _+2 more__
- **2026-07-15** [`52a88fb212`](https://github.com/sgl-project/sglang/commit/52a88fb212) [#30672](https://github.com/sgl-project/sglang/pull/30672)
  Avoid mutating ScheduleBatch fields in place (#30672)
  _Files: `.claude/rules/schedule-batch-out-of-place-mutation.md`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/unit/managers/test_schedule_batch_out_of_place.py`_
- **2026-07-15** [`ca0ee3f1a8`](https://github.com/sgl-project/sglang/commit/ca0ee3f1a8) [#31078](https://github.com/sgl-project/sglang/pull/31078)
  [Spec] Consolidate spec-worker weight updates into BaseSpecWorker via draft_runners (#31078)
  _Files: `python/sglang/srt/speculative/base_spec_worker.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-07-14** [`6507d4a090`](https://github.com/sgl-project/sglang/commit/6507d4a090) [#31148](https://github.com/sgl-project/sglang/pull/31148)
  Introduce WeightUpdater and WeightExporter components (#31148)
  _Files: `python/sglang/srt/managers/scheduler_components/weight_updater.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/__init__.py` _+7 more__
- **2026-07-14** [`2cf753c4fe`](https://github.com/sgl-project/sglang/commit/2cf753c4fe) [#31142](https://github.com/sgl-project/sglang/pull/31142)
  Clarify ModelRunner.dp_size into attn_dp_size (#31142)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py` _+1 more__
- **2026-07-14** [`c124bec99d`](https://github.com/sgl-project/sglang/commit/c124bec99d) [#30995](https://github.com/sgl-project/sglang/pull/30995)
  [CI] Disable gated Llama-2 EAGLE spec tests to unblock Xeon CPU CI (#30995)
  _Files: `test/registered/cpu/test_spec_eagle_cpu.py`, `test/registered/cpu/test_spec_eagle_topk_cpu.py`_
- **2026-07-13** [`9fec359a60`](https://github.com/sgl-project/sglang/commit/9fec359a60) [#30331](https://github.com/sgl-project/sglang/pull/30331)
  [Fix] Load HunyuanV3 NextN final_layernorm into the draft head's output norm (#30331)
  _Files: `python/sglang/srt/models/hunyuan_v3_nextn.py`, `test/registered/unit/models/test_hunyuan_v3_nextn_weight_loading.py`_

## Triton / Kernels  (18 commits)

- **2026-07-20** [`8bf2ab9be9`](https://github.com/sgl-project/sglang/commit/8bf2ab9be9) [#31649](https://github.com/sgl-project/sglang/pull/31649)
  Enable GPT-OSS TinyGEMM on CUDA 13 (#31649)
  _Files: `python/sglang/srt/models/gpt_oss.py`_
- **2026-07-20** [`5325cee7ea`](https://github.com/sgl-project/sglang/commit/5325cee7ea) [#31541](https://github.com/sgl-project/sglang/pull/31541)
  Bug fix in compress to support XPU (#31541)
  _Files: `python/sglang/jit_kernel/dsv4/compress.py`_
- **2026-07-18** [`d7b9425529`](https://github.com/sgl-project/sglang/commit/d7b9425529) [#31636](https://github.com/sgl-project/sglang/pull/31636)
  [NPU] fix: skip Triton embedding kernel on NPU to avoid kernel launch failure (#31636)
  _Files: `python/sglang/srt/layers/vocab_parallel_embedding.py`_
- **2026-07-18** [`6c6175fabd`](https://github.com/sgl-project/sglang/commit/6c6175fabd) [#31487](https://github.com/sgl-project/sglang/pull/31487)
  perf: avoid excessive prefill CUDA graph padding (#31487)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/unit/model_executor/runner/test_prefill_cuda_graph_padding.py`_
- **2026-07-17** [`0ad0ff2e9e`](https://github.com/sgl-project/sglang/commit/0ad0ff2e9e) [#31618](https://github.com/sgl-project/sglang/pull/31618)
  chore: bump sglang-kernel version to 0.4.5 (#31618)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`_
- **2026-07-17** [`619609aa5a`](https://github.com/sgl-project/sglang/commit/619609aa5a) [#31546](https://github.com/sgl-project/sglang/pull/31546)
  [Kernel] Simplify sglang.kernels tests to idiomatic pytest style (RFC #29630) (#31546)
  _Files: `test/registered/kernels/test_fused_op.py`, `test/registered/kernels/test_fused_op_gpu_parity.py`, `test/registered/kernels/test_kernels_namespace.py`_
- **2026-07-17** [`96dd96c02b`](https://github.com/sgl-project/sglang/commit/96dd96c02b) [#31532](https://github.com/sgl-project/sglang/pull/31532)
  [DCP] Auto-disable tc_piecewise and breakable prefill CUDA graphs under DCP (#31532)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-17** [`37f94cb7a0`](https://github.com/sgl-project/sglang/commit/37f94cb7a0) [#28439](https://github.com/sgl-project/sglang/pull/28439)
  [Intel GPU] DeepSeek V4 13/N: use sgl-kernel implementation of kernels in V2 Compressor to run on XPU (#28439)
  _Files: `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/jit_kernel/tests/deepseek_v4/common.py`, `test/registered/jit/deepseek_v4/test_c128_v2.py`, `test/registered/jit/deepseek_v4/test_c4_v2.py` _+1 more__
- **2026-07-16** [`f28ce5c420`](https://github.com/sgl-project/sglang/commit/f28ce5c420) [#31140](https://github.com/sgl-project/sglang/pull/31140)
  [XPU]REPO cache dtype xpu align with cuda (#31140)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`_
- **2026-07-16** [`0b04e9da83`](https://github.com/sgl-project/sglang/commit/0b04e9da83) [#29692](https://github.com/sgl-project/sglang/pull/29692)
  Use fused A GEMM for `fc1_latent_proj` in NemotronH (#29692)
  _Files: `python/sglang/jit_kernel/fused_a_gemm.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/nemotron_h.py`_
- **2026-07-15** [`41e0b4b369`](https://github.com/sgl-project/sglang/commit/41e0b4b369) [#31171](https://github.com/sgl-project/sglang/pull/31171)
  [CPU] add fused input proj for qwen3.5 (#31171)
  _Files: `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/models/qwen3_5.py`, `sgl-kernel/csrc/cpu/model/qwen3.cpp`, `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp` _+1 more__
- **2026-07-15** [`0832d856ca`](https://github.com/sgl-project/sglang/commit/0832d856ca) [#29508](https://github.com/sgl-project/sglang/pull/29508)
  [Bugfix] fix quickreduce acc error in cudagraph mode (#29508)
  _Files: `sgl-kernel/csrc/allreduce/quick_all_reduce.h`, `test/manual/test_quick_allreduce.py`_
- **2026-07-15** [`b22f20b660`](https://github.com/sgl-project/sglang/commit/b22f20b660) [#31035](https://github.com/sgl-project/sglang/pull/31035)
  [CI] Fix CUDA 12 NVIDIA wheel cleanup (#31035)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-07-14** [`ee000f6734`](https://github.com/sgl-project/sglang/commit/ee000f6734) [#31042](https://github.com/sgl-project/sglang/pull/31042)
  [CI] Fix SGLANG_JIT_KERNEL_RUN_FULL_TESTS never activating the nightly full jit-kernel sweep (#31042)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/jit_kernel/utils.py`, `python/sglang/srt/environ.py`_
- **2026-07-14** [`bf04cc9b14`](https://github.com/sgl-project/sglang/commit/bf04cc9b14) [#31168](https://github.com/sgl-project/sglang/pull/31168)
  Extract cuda-graph setup into a module (#31168)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`_
- **2026-07-13** [`86c59ac1aa`](https://github.com/sgl-project/sglang/commit/86c59ac1aa) [#31062](https://github.com/sgl-project/sglang/pull/31062)
  Revert "[Tiny] Enable Full Cuda Graph with Page size = 1" (#31062)
  _Files: `python/sglang/srt/arg_groups/overrides.py`_
- **2026-07-13** [`11a82af5f8`](https://github.com/sgl-project/sglang/commit/11a82af5f8) [#28113](https://github.com/sgl-project/sglang/pull/28113)
  [Platform] Route pin memory availability through current_platform (#28113)
  _Files: `docs_new/docs/hardware-platforms/plugin.mdx`, `python/sglang/srt/platforms/cpu.py`, `python/sglang/srt/platforms/cuda.py`, `python/sglang/srt/platforms/device_mixin.py` _+3 more__
- **2026-07-13** [`b44ac5d49a`](https://github.com/sgl-project/sglang/commit/b44ac5d49a) [#30835](https://github.com/sgl-project/sglang/pull/30835)
  [Tiny] Enable Full Cuda Graph with Page size = 1 (#30835)
  _Files: `python/sglang/srt/arg_groups/overrides.py`_

## Other  (17 commits)

- **2026-07-20** [`02236fa38c`](https://github.com/sgl-project/sglang/commit/02236fa38c) [#31681](https://github.com/sgl-project/sglang/pull/31681)
  Add Inkling model support (#31681)
- **2026-07-19** [`7d64858093`](https://github.com/sgl-project/sglang/commit/7d64858093) [#31717](https://github.com/sgl-project/sglang/pull/31717)
  Add houseroad to CI_PERMISSIONS.json (#31717)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-07-18** [`b3a0185cab`](https://github.com/sgl-project/sglang/commit/b3a0185cab) [#31601](https://github.com/sgl-project/sglang/pull/31601)
  model_runner: extract post-memory-pool wiring into _init_post_memory (#31601)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-07-18** [`a5c0b94034`](https://github.com/sgl-project/sglang/commit/a5c0b94034) [#31281](https://github.com/sgl-project/sglang/pull/31281)
  Let CI server launches wait longer for ports held by a dying predecessor (#31281)
  _Files: `python/sglang/srt/utils/network.py`, `python/sglang/test/test_utils.py`_
- **2026-07-17** [`5e7eed4c00`](https://github.com/sgl-project/sglang/commit/5e7eed4c00) [#30547](https://github.com/sgl-project/sglang/pull/30547)
  [MLX] Honor --max-running-requests in the model runner stub (#30547)
  _Files: `python/sglang/srt/hardware_backend/mlx/kv_cache/auxiliary_state.py`, `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `test/registered/unit/hardware_backend/mlx/test_max_running_requests.py`_
- **2026-07-17** [`27ea5ed070`](https://github.com/sgl-project/sglang/commit/27ea5ed070) [#31441](https://github.com/sgl-project/sglang/pull/31441)
  [XPU] Fix dtype mismatch in MRotaryEmbedding.forward_xpu by calling _… (#31441)
  _Files: `python/sglang/srt/layers/rotary_embedding/mrope.py`_
- **2026-07-16** [`640101da13`](https://github.com/sgl-project/sglang/commit/640101da13) [#31494](https://github.com/sgl-project/sglang/pull/31494)
  [Fix] Deflake score engine determinism tests (#31494)
  _Files: `test/registered/prefill_only/test_score_engine.py`_
- **2026-07-16** [`059ac7efe8`](https://github.com/sgl-project/sglang/commit/059ac7efe8) [#31098](https://github.com/sgl-project/sglang/pull/31098)
  Don't fail server startup when psutil can't parse /proc/meminfo (GB300 ShadowCallStack) (#31098)
  _Files: `python/sglang/srt/utils/network.py`_
- **2026-07-15** [`495ae9aaa6`](https://github.com/sgl-project/sglang/commit/495ae9aaa6) [#31232](https://github.com/sgl-project/sglang/pull/31232)
  Fix Ministral3 accuracy issue by aligning YaRN RoPE scaling with Transformers implementation (#31232)
  _Files: `python/sglang/srt/layers/rotary_embedding/factory.py`, `python/sglang/srt/layers/rotary_embedding/yarn.py`_
- **2026-07-15** [`dec0836302`](https://github.com/sgl-project/sglang/commit/dec0836302) [#31211](https://github.com/sgl-project/sglang/pull/31211)
  Fix processor config loading for object-storage model paths (#31211)
  _Files: `python/sglang/srt/utils/hf_transformers/processor.py`, `test/registered/unit/utils/test_hf_transformers.py`_
- **2026-07-14** [`08c46e1f1a`](https://github.com/sgl-project/sglang/commit/08c46e1f1a) [#31070](https://github.com/sgl-project/sglang/pull/31070)
  Add dummy forward batch preparation hook (#31070)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/base_runner.py`_
- **2026-07-14** [`a5a71c6c26`](https://github.com/sgl-project/sglang/commit/a5a71c6c26) [#30585](https://github.com/sgl-project/sglang/pull/30585)
  Enhance mechanical-refactor-verify skill with a whole-chain verifier, new relocation primitives, and generator inference (#30585)
  _Files: `.claude/skills/mechanical-refactor-verify/SKILL.md`, `.claude/skills/mechanical-refactor-verify/guide-construct-proof.md`, `.claude/skills/mechanical-refactor-verify/guide-modify-skill.md`, `.claude/skills/mechanical-refactor-verify/guide-split.md` _+26 more__
- **2026-07-14** [`17c04602c6`](https://github.com/sgl-project/sglang/commit/17c04602c6) [#31157](https://github.com/sgl-project/sglang/pull/31157)
  Extract spec aux-hidden-state resolution into a module (#31157)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/spec_aux_hidden_state.py`, `python/sglang/srt/model_executor/pool_configurator.py`_
- **2026-07-14** [`39e508b7fc`](https://github.com/sgl-project/sglang/commit/39e508b7fc) [#31156](https://github.com/sgl-project/sglang/pull/31156)
  Extract layer-index setup into a module (#31156)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/layer_setup.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`_
- **2026-07-14** [`5b540b16de`](https://github.com/sgl-project/sglang/commit/5b540b16de) [#31155](https://github.com/sgl-project/sglang/pull/31155)
  Extract load_model helpers into a load_model_utils module (#31155)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`_
- **2026-07-14** [`0f20f52e5e`](https://github.com/sgl-project/sglang/commit/0f20f52e5e) [#31153](https://github.com/sgl-project/sglang/pull/31153)
  Introduce RemoteInstanceWeightTransporter component (#31153)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/remote_instance_weight_transporter.py`_
- **2026-07-13** [`22c08a9bee`](https://github.com/sgl-project/sglang/commit/22c08a9bee) [#30956](https://github.com/sgl-project/sglang/pull/30956)
  Preserve RMSNorm shape in batch-invariant mode (#30956)
  _Files: `python/sglang/srt/layers/layernorm.py`_

## Quantization  (17 commits)

- **2026-07-20** [`829e9ce9d5`](https://github.com/sgl-project/sglang/commit/829e9ce9d5) [#31748](https://github.com/sgl-project/sglang/pull/31748)
  Lower AutoRound quantization MMLU threshold (#31748)
  _Files: `test/registered/quant/test_autoround_quantization.py`_
- **2026-07-19** [`377c93d54e`](https://github.com/sgl-project/sglang/commit/377c93d54e) [#30940](https://github.com/sgl-project/sglang/pull/30940)
  [AMD] Gate TP4 o_proj/qkv CK block-FP8 GEMM shapes to Triton (ROCm 7.0 Qwen-3.5) (#30940)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-07-18** [`7fbe91c6ea`](https://github.com/sgl-project/sglang/commit/7fbe91c6ea) [#31492](https://github.com/sgl-project/sglang/pull/31492)
  [AMD] register 8 JIT kernel benchmarks to jit-kernel-benchmark-test-amd (#31492)
  _Files: `test/registered/jit/benchmark/bench_custom_all_reduce.py`, `test/registered/jit/benchmark/bench_fp8_blockwise_gemm.py`, `test/registered/jit/benchmark/bench_post_reorder_deepgemm.py`, `test/registered/jit/benchmark/bench_symm_mem_all_gather.py` _+4 more__
- **2026-07-18** [`238b2b2c9c`](https://github.com/sgl-project/sglang/commit/238b2b2c9c) [#31109](https://github.com/sgl-project/sglang/pull/31109)
  Remove QServe and FBGEMM FP8 quantization (#31109)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/multimodal_gen/runtime/layers/linear.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/linear.py` _+14 more__
- **2026-07-17** [`7fc3fb9657`](https://github.com/sgl-project/sglang/commit/7fc3fb9657) [#31094](https://github.com/sgl-project/sglang/pull/31094)
  Remove deprecated Mamba flags from doc, wrong FP8 GEMM docstrings and change Nemotron image to 0.5.15 (#31094)
  _Files: `docs_new/cookbook/autoregressive/InclusionAI/Ling-2.6.mdx`, `docs_new/cookbook/autoregressive/InternLM/Intern-S2-Preview.mdx`, `docs_new/cookbook/autoregressive/LiquidAI/LFM2.5.mdx`, `docs_new/cookbook/autoregressive/NVIDIA/Nemotron3-Ultra.mdx` _+20 more__
- **2026-07-17** [`bbd2a3fe4a`](https://github.com/sgl-project/sglang/commit/bbd2a3fe4a) [#23795](https://github.com/sgl-project/sglang/pull/23795)
  :sparkles: [llm][npu][quant] Add W4A4 MXFP4 quantization support for Qwen3 Dense on Ascend NPU (#23795)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quantization.mdx`, `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`, `python/sglang/srt/layers/quantization/__init__.py` _+4 more__
- **2026-07-17** [`302c3b97d2`](https://github.com/sgl-project/sglang/commit/302c3b97d2) [#31174](https://github.com/sgl-project/sglang/pull/31174)
  fix: Qwen3.5-35B-A3B-AWQ w2_weight KeyError and related params for CPU (#31174)
  _Files: `python/sglang/srt/layers/quantization/awq/awq.py`, `python/sglang/srt/models/qwen3_5.py`_
- **2026-07-16** [`dee91c51cf`](https://github.com/sgl-project/sglang/commit/dee91c51cf) [#28983](https://github.com/sgl-project/sglang/pull/28983)
  perf(deepseek_v4): enable SGLANG_OPT_FP8_WO_A_GEMM on sm90 (Hopper) (#28983)
  _Files: `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/server_args.py`, `test/manual/dsv4/test_wo_a_fp8_sm90.py`_
- **2026-07-16** [`7f9a902cd9`](https://github.com/sgl-project/sglang/commit/7f9a902cd9) [#31185](https://github.com/sgl-project/sglang/pull/31185)
  fix(humming): handle missing quant_method (#31185)
  _Files: `python/sglang/srt/layers/quantization/humming.py`_
- **2026-07-15** [`ab627e5d75`](https://github.com/sgl-project/sglang/commit/ab627e5d75) [#30976](https://github.com/sgl-project/sglang/pull/30976)
  fix: load the right mtp lm head quantization (#30976)
  _Files: `python/sglang/srt/models/nemotron_h_mtp.py`_
- **2026-07-14** [`cad8fe7a66`](https://github.com/sgl-project/sglang/commit/cad8fe7a66) [#31146](https://github.com/sgl-project/sglang/pull/31146)
  Extract leaf helpers out of ModelRunner into utility modules (#31146)
  _Files: `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`, `python/sglang/srt/layers/model_parallel.py`, `python/sglang/srt/layers/quantization/fp4_kv_cache_quant_method.py`, `python/sglang/srt/model_executor/model_runner.py` _+4 more__
- **2026-07-14** [`2ced88238a`](https://github.com/sgl-project/sglang/commit/2ced88238a) [#30458](https://github.com/sgl-project/sglang/pull/30458)
  [NPU] [BUGFIX] Fix input parameters of swiglu_oai operator (#30458)
  _Files: `python/sglang/srt/layers/quantization/unquant.py`_
- **2026-07-14** [`7431f35fd8`](https://github.com/sgl-project/sglang/commit/7431f35fd8) [#30438](https://github.com/sgl-project/sglang/pull/30438)
  Delete CUTLASS FP8 blockwise for SM90 and SM100, move SM120 to JIT and add SwapAB (#30438)
  _Files: `python/sglang/jit_kernel/csrc/gemm/fp8_blockwise/fp8_blockwise_scaled_mm_entry.cuh`, `python/sglang/jit_kernel/csrc/gemm/fp8_blockwise/fp8_blockwise_scaled_mm_sm120.cuh`, `python/sglang/jit_kernel/fp8_blockwise_gemm.py`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh` _+13 more__
- **2026-07-14** [`e489685509`](https://github.com/sgl-project/sglang/commit/e489685509) [#27873](https://github.com/sgl-project/sglang/pull/27873)
  [Intel GPU] DeepSeek V4 5/N: Use sgl-kernel implementation of fused_q_indexer_rope_hadamard_quant to run on XPU (#27873)
  _Files: `python/sglang/jit_kernel/dsv4/elementwise.py`_
- **2026-07-14** [`4c997310f5`](https://github.com/sgl-project/sglang/commit/4c997310f5) [#31089](https://github.com/sgl-project/sglang/pull/31089)
  [Kernel] Hotfix: update sgl-kernel imports of relocated fp8_kernel (RFC #29630 #30784) (#31089)
  _Files: `sgl-kernel/benchmark/bench_fp8_blockwise_gemm.py`, `sgl-kernel/benchmark/bench_per_token_group_quant_8bit.py`, `sgl-kernel/tests/test_per_token_group_quant_8bit.py`_
- **2026-07-13** [`cfc3d0555e`](https://github.com/sgl-project/sglang/commit/cfc3d0555e) [#29151](https://github.com/sgl-project/sglang/pull/29151)
  Fix ModelOpt NVFP4 scalar scales for merged linears (#29151)
  _Files: `python/sglang/srt/layers/linear.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4.py`_
- **2026-07-13** [`874fc07d9b`](https://github.com/sgl-project/sglang/commit/874fc07d9b) [#30784](https://github.com/sgl-project/sglang/pull/30784)
  [Kernel] Migrate scattered quantization kernels to sglang.kernels (RFC #29630, Phase 2.5, 1/7) (#30784)

## ROCm / AMD  (15 commits)

- **2026-07-20** [`17fdd8487f`](https://github.com/sgl-project/sglang/commit/17fdd8487f) [#31737](https://github.com/sgl-project/sglang/pull/31737)
  [AMD] Update qwen3.5 cookbook (#31737)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs_new/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-07-17** [`c00206c68c`](https://github.com/sgl-project/sglang/commit/c00206c68c) [#31496](https://github.com/sgl-project/sglang/pull/31496)
  chore: bump sgl-kernel version to 0.4.5 (#31496)
  _Files: `sgl-kernel/pyproject.toml`, `sgl-kernel/pyproject_cpu.toml`, `sgl-kernel/pyproject_musa.toml`, `sgl-kernel/pyproject_rocm.toml` _+1 more__
- **2026-07-17** [`fec6131844`](https://github.com/sgl-project/sglang/commit/fec6131844) [#30506](https://github.com/sgl-project/sglang/pull/30506)
  [AMD] Disable DSA fused top-k v2 on ROCm for GLM-5.x / DeepSeek-V3.2 (#30506)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-17** [`1ac1ffea0c`](https://github.com/sgl-project/sglang/commit/1ac1ffea0c) [#31307](https://github.com/sgl-project/sglang/pull/31307)
  [Kernel] Fill non-CUDA coverage: HIP (aiter/rocm-triton) + Ascend NPU backends (RFC #29630) (#31307)
  _Files: `python/sglang/kernels/fused_op.py`, `python/sglang/kernels/ops/activation/__init__.py`, `python/sglang/kernels/ops/layernorm/__init__.py`, `python/sglang/kernels/spec.py` _+2 more__
- **2026-07-17** [`27a52d2530`](https://github.com/sgl-project/sglang/commit/27a52d2530) [#31452](https://github.com/sgl-project/sglang/pull/31452)
  [Docs] Tune DeepSeek-V4 HiCache for MI355X PD (#31452)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/_playground.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-07-16** [`4d60c4540c`](https://github.com/sgl-project/sglang/commit/4d60c4540c) [#31436](https://github.com/sgl-project/sglang/pull/31436)
  [AMD] Skip AMD nightly local registry push (#31436)
  _Files: `.github/workflows/release-docker-amd-nightly.yml`, `.github/workflows/release-docker-amd-rocm720-nightly.yml`_
- **2026-07-16** [`3264477a07`](https://github.com/sgl-project/sglang/commit/3264477a07) [#31122](https://github.com/sgl-project/sglang/pull/31122)
  [Docs] Add AMD-specific HiCache config for DeepSeek V4 playground (#31122)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/_playground.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-07-16** [`8c5e0cee18`](https://github.com/sgl-project/sglang/commit/8c5e0cee18) [#31406](https://github.com/sgl-project/sglang/pull/31406)
  [AMD] Bump MoRI to f7e6ac6 to fix ROCm install_dependency build break (#31406)
  _Files: `docker/rocm.Dockerfile`_
- **2026-07-15** [`d36e96ce23`](https://github.com/sgl-project/sglang/commit/d36e96ce23) [#30359](https://github.com/sgl-project/sglang/pull/30359)
  [AMD] Enable mamba-extra-buffer for Qwen3.5 on ROCm (#30359)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-15** [`a8b60433c2`](https://github.com/sgl-project/sglang/commit/a8b60433c2) [#31131](https://github.com/sgl-project/sglang/pull/31131)
  [AMD] Fix DSV4 JIT build on rocm  (#31131)
  _Files: `python/sglang/jit_kernel/include/sgl_kernel/runtime.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`_
- **2026-07-15** [`a3194d3585`](https://github.com/sgl-project/sglang/commit/a3194d3585) [#30622](https://github.com/sgl-project/sglang/pull/30622)
  [AMD] Remove ROCm page_first+kernel -> layer_first HiCache fallback (follow-up to #28534) (#30622)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-07-15** [`aafa706f8f`](https://github.com/sgl-project/sglang/commit/aafa706f8f) [#31258](https://github.com/sgl-project/sglang/pull/31258)
  [AMD] Update qwen3.5 cookbook (#31258)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs_new/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-07-14** [`64a70c9097`](https://github.com/sgl-project/sglang/commit/64a70c9097) [#31143](https://github.com/sgl-project/sglang/pull/31143)
  [AMD] jit_kernel: complete utils.cuh HIP-compat (cudaDevAttr / cudaDeviceGetAttribute) (#31143)
  _Files: `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`_
- **2026-07-13** [`805385414e`](https://github.com/sgl-project/sglang/commit/805385414e) [#31058](https://github.com/sgl-project/sglang/pull/31058)
  chore: bump docs install version to 0.5.15 (#31058)
  _Files: `docs_new/docs/get-started/install.mdx`, `docs_new/docs/hardware-platforms/amd_gpu.mdx`_
- **2026-07-13** [`80965db8d3`](https://github.com/sgl-project/sglang/commit/80965db8d3) [#30942](https://github.com/sgl-project/sglang/pull/30942)
  [AMD] Pin cmake==4.3.4 in ROCm Dockerfile to fix MoRI gtest_discover build break (#30942)
  _Files: `docker/rocm.Dockerfile`_

## CI / Build  (12 commits)

- **2026-07-20** [`3f48245080`](https://github.com/sgl-project/sglang/commit/3f48245080) [#31764](https://github.com/sgl-project/sglang/pull/31764)
  [CI] Temporarily disable GB300 jobs (runner availability) (#31764)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/release-whl-deepgemm.yml`_
- **2026-07-20** [`2f14d6c6f2`](https://github.com/sgl-project/sglang/commit/2f14d6c6f2) [#31749](https://github.com/sgl-project/sglang/pull/31749)
  ci: run nvidia nightly every 2 days at 14:00 UTC (7am PT) (#31749)
  _Files: `.github/workflows/nightly-test-nvidia.yml`_
- **2026-07-19** [`1a317839d7`](https://github.com/sgl-project/sglang/commit/1a317839d7) [#31702](https://github.com/sgl-project/sglang/pull/31702)
  ci: lower VL PP gsm8k threshold to 0.60 (0.65 has zero margin on H100) (#31702)
  _Files: `test/registered/pp/test_pp_single_node_extra.py`_
- **2026-07-18** [`e48eabbeee`](https://github.com/sgl-project/sglang/commit/e48eabbeee) [#31442](https://github.com/sgl-project/sglang/pull/31442)
  ci: add MLX to coverage report backend display order (#31442)
  _Files: `scripts/ci/utils/ci_coverage_report.py`_
- **2026-07-17** [`19f4859b30`](https://github.com/sgl-project/sglang/commit/19f4859b30) [#31571](https://github.com/sgl-project/sglang/pull/31571)
  [CI] Exclude current process memory from GPU idle check (#31571)
  _Files: `python/sglang/test/test_utils.py`_
- **2026-07-17** [`e835512303`](https://github.com/sgl-project/sglang/commit/e835512303) [#31512](https://github.com/sgl-project/sglang/pull/31512)
  Add nightly test for GLM5.2 LayerSplit (#31512)
  _Files: `test/registered/models_e2e/test_dsa_glm52_cache_layer_split.py`_
- **2026-07-17** [`27ad9d11b1`](https://github.com/sgl-project/sglang/commit/27ad9d11b1) [#31509](https://github.com/sgl-project/sglang/pull/31509)
  [CI] Wait for GPU memory release before each test class setUpClass (#31509)
  _Files: `python/sglang/test/test_utils.py`_
- **2026-07-17** [`7355e0cb87`](https://github.com/sgl-project/sglang/commit/7355e0cb87) [#30731](https://github.com/sgl-project/sglang/pull/30731)
  [NPU] custom-ops adapt (#30731)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `docker/npu.Dockerfile`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-07-16** [`0b372d03de`](https://github.com/sgl-project/sglang/commit/0b372d03de) [#31416](https://github.com/sgl-project/sglang/pull/31416)
  [CI] Guard partition consumers against failed check-changes and degenerate fits (#31416)
  _Files: `.github/workflows/pr-test.yml`, `scripts/ci/utils/compute_partitions.py`_
- **2026-07-16** [`238448f4c8`](https://github.com/sgl-project/sglang/commit/238448f4c8) [#31396](https://github.com/sgl-project/sglang/pull/31396)
  ci: fix runner utilization report undercounting busy time ~25x (#31396)
  _Files: `.github/workflows/runner-utilization.yml`, `scripts/ci/utils/runner_utilization_report.py`, `scripts/ci/utils/test_runner_utilization_report.py`_
- **2026-07-14** [`21a6d08557`](https://github.com/sgl-project/sglang/commit/21a6d08557) [#31234](https://github.com/sgl-project/sglang/pull/31234)
  ci: strip invisible Unicode format chars from slash-command input (#31234)
  _Files: `scripts/ci/utils/slash_command_handler.py`_
- **2026-07-14** [`464fe1b77c`](https://github.com/sgl-project/sglang/commit/464fe1b77c) [#31080](https://github.com/sgl-project/sglang/pull/31080)
  [CI] Use torch.testing.assert_close in custom-all-reduce test (~1400x faster compare) (#31080)
  _Files: `test/registered/jit/test_custom_all_reduce.py`_

## Tensor / Data Parallel  (12 commits)

- **2026-07-18** [`d86ae51fcf`](https://github.com/sgl-project/sglang/commit/d86ae51fcf) [#31530](https://github.com/sgl-project/sglang/pull/31530)
  metrics: allow extra labels on HTTP request/response Prometheus metrics (#31530)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-07-18** [`639261f7b2`](https://github.com/sgl-project/sglang/commit/639261f7b2) [#31624](https://github.com/sgl-project/sglang/pull/31624)
  [Refactor] Move output logprob processing into the logprob_processor layer (#31624)
  _Files: `python/sglang/srt/layers/logprob_processor.py`, `python/sglang/srt/layers/sampler.py`_
- **2026-07-18** [`87dc211b87`](https://github.com/sgl-project/sglang/commit/87dc211b87) [#31634](https://github.com/sgl-project/sglang/pull/31634)
  [MUSA] Fix sglang-kernel build (#31634)
  _Files: `.github/workflows/nightly-test-musa.yml`, `.github/workflows/pr-test-musa.yml`, `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject_other.toml` _+3 more__
- **2026-07-17** [`132ade55cd`](https://github.com/sgl-project/sglang/commit/132ade55cd) [#31049](https://github.com/sgl-project/sglang/pull/31049)
  [Kernel] Rewrite JIT custom all-reduce (v2) with a decoupled kernel/storage design (#31049)
  _Files: `python/sglang/jit_kernel/all_reduce.py`, `python/sglang/jit_kernel/benchmark/utils.py`, `python/sglang/jit_kernel/csrc/distributed/communicator.cuh`, `python/sglang/jit_kernel/csrc/distributed/custom_all_reduce.cuh` _+19 more__
- **2026-07-17** [`8f765bc1c9`](https://github.com/sgl-project/sglang/commit/8f765bc1c9) [#31550](https://github.com/sgl-project/sglang/pull/31550)
  [Docs] Inkling cookbook: mark B300/GB300 recipes verified, tune B300 MTP mem fractions (#31550)
  _Files: `docs_new/cookbook/autoregressive/ThinkingMachines/Inkling.mdx`, `docs_new/src/snippets/configs/thinkingmachines/inkling.jsx`_
- **2026-07-16** [`e2d021d4ab`](https://github.com/sgl-project/sglang/commit/e2d021d4ab) [#30238](https://github.com/sgl-project/sglang/pull/30238)
  [AMD] Support two batch overlap with MTP on DeepSeekV4 (#30238)
  _Files: `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/amd/test_deepseek_v4_pro_fp4_tbo_mtp.py`_
- **2026-07-15** [`d2b1243be0`](https://github.com/sgl-project/sglang/commit/d2b1243be0) [#31333](https://github.com/sgl-project/sglang/pull/31333)
  docs: document CUDA crash dump output (#31333)
  _Files: `docs_new/docs/advanced_features/observability.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`_
- **2026-07-15** [`5af670284e`](https://github.com/sgl-project/sglang/commit/5af670284e) [#31289](https://github.com/sgl-project/sglang/pull/31289)
  [CI] Lower GLM-5.2 NVFP4 MTP speed threshold (#31289)
  _Files: `test/registered/models_e2e/test_dsa_glm52_nvfp4_tp_mtp.py`_
- **2026-07-14** [`04af94d150`](https://github.com/sgl-project/sglang/commit/04af94d150) [#30870](https://github.com/sgl-project/sglang/pull/30870)
  fix: avoid tilelang cuda runtime pollution (#30870)
  _Files: `python/sglang/srt/distributed/device_communicators/cuda_wrapper.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/distributed/test_cuda_wrapper.py`_
- **2026-07-14** [`f853293440`](https://github.com/sgl-project/sglang/commit/f853293440) [#30619](https://github.com/sgl-project/sglang/pull/30619)
  [NPU] Fix CPU device for node topology probe (#30619)
  _Files: `python/sglang/srt/distributed/parallel_state.py`_
- **2026-07-14** [`caa85ea022`](https://github.com/sgl-project/sglang/commit/caa85ea022) [#31152](https://github.com/sgl-project/sglang/pull/31152)
  Extract init_torch_distributed and refactor into functions (#31152)
  _Files: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-07-13** [`f391c71758`](https://github.com/sgl-project/sglang/commit/f391c71758) [#31039](https://github.com/sgl-project/sglang/pull/31039)
  [NPU] [DOC] --pp-size can not be used witgh --tp-size (#31039)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_

## Models  (8 commits)

- **2026-07-17** [`ead703815e`](https://github.com/sgl-project/sglang/commit/ead703815e) [#31514](https://github.com/sgl-project/sglang/pull/31514)
  [DCP] Enable decode context parallel for Kimi K2.5 NVFP4 (#31514)
  _Files: `python/sglang/srt/layers/dcp/comm.py`, `python/sglang/srt/models/kimi_k25.py`_
- **2026-07-16** [`1b9f228838`](https://github.com/sgl-project/sglang/commit/1b9f228838) [#31411](https://github.com/sgl-project/sglang/pull/31411)
  [Docs] Playground: migrate CP knob to canonical prefill-CP flags, align gating with runtime semantics (#31411)
  _Files: `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `docs_new/cookbook/autoregressive/Tencent/Hy3.mdx`, `docs_new/src/snippets/_playground.jsx`, `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3.jsx` _+4 more__
- **2026-07-16** [`bc525dcf90`](https://github.com/sgl-project/sglang/commit/bc525dcf90) [#30520](https://github.com/sgl-project/sglang/pull/30520)
  [Cookbook][CPU]Update CPU model support info in Cookbook (#30520)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-OCR-2.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-R1.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V3_1.mdx` _+19 more__
- **2026-07-14** [`bdc9848c25`](https://github.com/sgl-project/sglang/commit/bdc9848c25) [#29886](https://github.com/sgl-project/sglang/pull/29886)
  [Doc]Standardize the names of PyTorch NPU-related software throughout the documentation by replacing them all with `TorchNPU`. (#29886)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_faq.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/model-tutorials/deepseek_r1.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/model-tutorials/deepseek_v3_2.mdx` _+11 more__
- **2026-07-14** [`96c2ebc58b`](https://github.com/sgl-project/sglang/commit/96c2ebc58b) [#31124](https://github.com/sgl-project/sglang/pull/31124)
  [docs] Note the default dsa-topk-backend on all DSA-model cookbook pages (#31124)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-Math-V2.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`, `docs_new/cookbook/autoregressive/GLM/GLM-5.1.mdx`, `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx` _+2 more__
- **2026-07-14** [`2f79d334f2`](https://github.com/sgl-project/sglang/commit/2f79d334f2) [#30987](https://github.com/sgl-project/sglang/pull/30987)
  [Bugfix] Fix DeepSeek ForwardFlags across custom op boundary (#30987)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-07-13** [`50ed4c011f`](https://github.com/sgl-project/sglang/commit/50ed4c011f) [#28964](https://github.com/sgl-project/sglang/pull/28964)
  Remove legacy Sphinx docs/ and finish the Mintlify cutover (#28964)
- **2026-07-13** [`cbcbef6811`](https://github.com/sgl-project/sglang/commit/cbcbef6811) [#30968](https://github.com/sgl-project/sglang/pull/30968)
  [Bugfix] Fix Nemotron ForwardFlags across custom op boundary (#30968)
  _Files: `python/sglang/srt/models/nemotron_h.py`, `test/registered/models_e2e/test_nvidia_nemotron_3_nano.py`_

## Docs / Examples  (6 commits)

- **2026-07-17** [`eaeb779ea4`](https://github.com/sgl-project/sglang/commit/eaeb779ea4) [#31577](https://github.com/sgl-project/sglang/pull/31577)
  [Doc] Update GLM5.2 Cookbook with LayerSplit usage (#31577)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`_
- **2026-07-16** [`6275114548`](https://github.com/sgl-project/sglang/commit/6275114548) [#31316](https://github.com/sgl-project/sglang/pull/31316)
  [NPU] [DOC] Update model names supported on Ascend NPU (#31316)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_models.mdx`_
- **2026-07-16** [`34f5691ea1`](https://github.com/sgl-project/sglang/commit/34f5691ea1) [#31386](https://github.com/sgl-project/sglang/pull/31386)
  docs: sync LMSYS SGLang blog cards (#31386)
  _Files: `docs_new/index.mdx`_
- **2026-07-15** [`dd2e4cdc99`](https://github.com/sgl-project/sglang/commit/dd2e4cdc99) [#31360](https://github.com/sgl-project/sglang/pull/31360)
  Add Inkling cookbook (#31360)
  _Files: `docs_new/cards/logos/thinkingmachines.png`, `docs_new/cookbook/autoregressive/ThinkingMachines/Inkling.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json` _+2 more__
- **2026-07-15** [`b8a00e2ec8`](https://github.com/sgl-project/sglang/commit/b8a00e2ec8) [#31242](https://github.com/sgl-project/sglang/pull/31242)
  docs: sync LMSYS SGLang blog cards (#31242)
  _Files: `docs_new/index.mdx`_
- **2026-07-13** [`b677babc62`](https://github.com/sgl-project/sglang/commit/b677babc62) [#30571](https://github.com/sgl-project/sglang/pull/30571)
  docs: sync LMSYS SGLang blog cards (#30571)
  _Files: `docs_new/index.mdx`_

## LoRA  (4 commits)

- **2026-07-17** [`632adff9fd`](https://github.com/sgl-project/sglang/commit/632adff9fd) [#20071](https://github.com/sgl-project/sglang/pull/20071)
  refactor logprob processor layer (#20071)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/logprob_processor.py`, `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/lora/layers.py` _+3 more__
- **2026-07-16** [`68f4de162d`](https://github.com/sgl-project/sglang/commit/68f4de162d) [#31489](https://github.com/sgl-project/sglang/pull/31489)
  [Docs] Remove Inkling H200 LoRA BF16 cookbook command (#31489)
  _Files: `docs_new/src/snippets/configs/thinkingmachines/inkling.jsx`_
- **2026-07-16** [`40517b593b`](https://github.com/sgl-project/sglang/commit/40517b593b) [#31418](https://github.com/sgl-project/sglang/pull/31418)
  [docs] Inkling cookbook: LoRA cells require --disable-prefill-cuda-graph (#31418)
  _Files: `docs_new/src/snippets/configs/thinkingmachines/inkling.jsx`_
- **2026-07-14** [`205a2f2de4`](https://github.com/sgl-project/sglang/commit/205a2f2de4) [#31151](https://github.com/sgl-project/sglang/pull/31151)
  Move LoRA cuda-graph buffers and logging into LoRAManager (#31151)
  _Files: `python/sglang/srt/lora/lora_manager.py`, `python/sglang/srt/model_executor/model_runner.py`_

## Serving / API  (2 commits)

- **2026-07-13** [`0ee236ebdf`](https://github.com/sgl-project/sglang/commit/0ee236ebdf) [#30533](https://github.com/sgl-project/sglang/pull/30533)
  more fixes for Nemotron 3 parser for tool call and force nonempty content (#30533)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/parser/test_reasoning_parser.py`_
- **2026-07-13** [`afaa17a7f2`](https://github.com/sgl-project/sglang/commit/afaa17a7f2) [#29579](https://github.com/sgl-project/sglang/pull/29579)
  [Feature] Add --default-chat-template-kwargs server arg (#29579)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_

## Structured Output  (1 commits)

- **2026-07-17** [`c95026aed3`](https://github.com/sgl-project/sglang/commit/c95026aed3) [#31484](https://github.com/sgl-project/sglang/pull/31484)
  Upgrade llguidance to 1.7.6 (#31484)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` _+6 more__

---
_Generated 2026-07-20 11:09 UTC_