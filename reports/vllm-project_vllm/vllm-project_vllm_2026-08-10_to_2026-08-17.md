# vllm-project/vllm — Weekly Change Report
**Period:** 2026-08-10 → 2026-08-17  |  **Total commits:** 312

## ✨ New Features This Week

- **2026-08-17** [#52502](https://github.com/vllm-project/vllm/pull/52502) — [Hardware][NVIDIA] Add GB10 fused-MoE fp8 tuning configs (E=256, E=512) (#52502)
- **2026-08-17** [#50492](https://github.com/vllm-project/vllm/pull/50492) — [Doc] Add MatrixHub as a model loading source (#50492)
- **2026-08-17** [#52256](https://github.com/vllm-project/vllm/pull/52256) — [ROCm][CI] Enable ViT CUDA graph tests on AMD gfx950 GPUs (#52256)
- **2026-08-16** [#52425](https://github.com/vllm-project/vllm/pull/52425) — [ModelRunner v2] Support Transformers pooling model  (#52425)
- **2026-08-16** [#52514](https://github.com/vllm-project/vllm/pull/52514) — [Core] Add CuMemAllocator.discard() for tag-selective GPU memory release (#52514)
- **2026-08-15** [#51901](https://github.com/vllm-project/vllm/pull/51901) — [CI/Build] Add warning for unsupported global PTX architecture requests in...  (#51901)
- **2026-08-15** [#45802](https://github.com/vllm-project/vllm/pull/45802) — [Frontend]  Support count_reasoning_tokens in the Streaming Parser Engine (#45802)
- **2026-08-14** [#52374](https://github.com/vllm-project/vllm/pull/52374) — [MRV2] Support attention-free models (#52374)
- **2026-08-14** [#50597](https://github.com/vllm-project/vllm/pull/50597) — [ROCm]Remove special-case SiTU support model-specific gating (#50597)
- **2026-08-14** [#51316](https://github.com/vllm-project/vllm/pull/51316) — [Rust Frontend][gRPC] Add RL lifecycle control (#51316)
- _…and 49 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-17** [`311b3513af`](https://github.com/vllm-project/vllm/commit/311b3513af) [#52565](https://github.com/vllm-project/vllm/pull/52565) — [ROCm][CI] Avoid forcing FlashAttention in the ColPali pooling test (#52565)
- **2026-08-17** [`71b578b9cc`](https://github.com/vllm-project/vllm/commit/71b578b9cc) [#49514](https://github.com/vllm-project/vllm/pull/49514) — [ROCm][CI] Use the same-build wheel in Python-only CI (#49514)
- **2026-08-17** [`0ad04cff1b`](https://github.com/vllm-project/vllm/commit/0ad04cff1b) [#52256](https://github.com/vllm-project/vllm/pull/52256) — [ROCm][CI] Enable ViT CUDA graph tests on AMD gfx950 GPUs (#52256)
- **2026-08-16** [`ef43e3101b`](https://github.com/vllm-project/vllm/commit/ef43e3101b) [#52212](https://github.com/vllm-project/vllm/pull/52212) — [ROCm][DSV4][Perf] Optimize Triton sparse-MLA decode on gfx950 (#52212)
- **2026-08-16** [`6914d60b1e`](https://github.com/vllm-project/vllm/commit/6914d60b1e) [#49544](https://github.com/vllm-project/vllm/pull/49544) — [ROCm][Perf] gfx942: use FlyDSL fp8 MQA logits kernel (ROCm/aiter#3913) (#49544)
- **2026-08-16** [`fe1c317157`](https://github.com/vllm-project/vllm/commit/fe1c317157) [#52356](https://github.com/vllm-project/vllm/pull/52356) — [Bugfix][ROCm] Skip FP8 MLA prefill PS-metadata build for chunked-context batches (#52356)
- **2026-08-15** [`97388c44f9`](https://github.com/vllm-project/vllm/commit/97388c44f9) [#51538](https://github.com/vllm-project/vllm/pull/51538) — [Bugfix] Make DSV4 sparse MLA work end-to-end for plain decode, MTP, and DSpark (#51538)
- **2026-08-15** [`44fc57d7b7`](https://github.com/vllm-project/vllm/commit/44fc57d7b7) [#49515](https://github.com/vllm-project/vllm/pull/49515) — [ROCm][CI] Select CPU platform for native no-GPU jobs (#49515)
- **2026-08-15** [`615d4cfade`](https://github.com/vllm-project/vllm/commit/615d4cfade) [#43107](https://github.com/vllm-project/vllm/pull/43107) — [Core] Check for GPU<->CPU syncs during CI (#43107)
- **2026-08-14** [`9df9b0b0a1`](https://github.com/vllm-project/vllm/commit/9df9b0b0a1) [#52400](https://github.com/vllm-project/vllm/pull/52400) — [ROCm]: Drop pybind11 from Dockerfile.rocm to prevent version mismatch (#52400)
- **2026-08-14** [`c794754062`](https://github.com/vllm-project/vllm/commit/c794754062) [#50597](https://github.com/vllm-project/vllm/pull/50597) — [ROCm]Remove special-case SiTU support model-specific gating (#50597)
- **2026-08-14** [`9b0ab5dd53`](https://github.com/vllm-project/vllm/commit/9b0ab5dd53) [#51216](https://github.com/vllm-project/vllm/pull/51216) — [ROCm][AMD] Enable preshuffled sparse indexing for 16-token blocks (#51216)
- **2026-08-14** [`59d1af5698`](https://github.com/vllm-project/vllm/commit/59d1af5698) [#49365](https://github.com/vllm-project/vllm/pull/49365) — Detect ROCm wheel variant from environment for precompiled wheels. (#49365)
- **2026-08-13** [`73b83949f7`](https://github.com/vllm-project/vllm/commit/73b83949f7) [#51633](https://github.com/vllm-project/vllm/pull/51633) — [Platform] Add check_runner_kv_caches_multi_layer (#51633)
- **2026-08-13** [`11c3fa4adc`](https://github.com/vllm-project/vllm/commit/11c3fa4adc) [#52139](https://github.com/vllm-project/vllm/pull/52139) — [Bugfix][ROCm][CI] Give the AITER MLA decode metadata stub its MLA dims (#52139)
- **2026-08-13** [`c5b7c069a4`](https://github.com/vllm-project/vllm/commit/c5b7c069a4) [#51159](https://github.com/vllm-project/vllm/pull/51159) — [ROCm] Defer `tilelang` import through its import `from vllm.tilelang_utils import tilelang` and relaxed `has_tilelang` (#51159)
- **2026-08-13** [`b96bcd0b47`](https://github.com/vllm-project/vllm/commit/b96bcd0b47) [#51280](https://github.com/vllm-project/vllm/pull/51280) — [ROCm][CI] Solidify entrypoint LLM lifecycle (#51280)
- **2026-08-13** [`f3c1638927`](https://github.com/vllm-project/vllm/commit/f3c1638927) [#51653](https://github.com/vllm-project/vllm/pull/51653) — [ROCm] Enable V2 model runner for Kimi-K3 on ROCm (#51653)
- **2026-08-13** [`5fee0a872d`](https://github.com/vllm-project/vllm/commit/5fee0a872d) [#51998](https://github.com/vllm-project/vllm/pull/51998) — chore: Upstream Cohere parser fixes + tests (#51998)
- **2026-08-13** [`f96261637c`](https://github.com/vllm-project/vllm/commit/f96261637c) [#51862](https://github.com/vllm-project/vllm/pull/51862) — [ROCm][Perf] Kimi-K3 Remove prefill pipeline stall in chunk KDA (#51862)
- **2026-08-13** [`373592ef57`](https://github.com/vllm-project/vllm/commit/373592ef57) [#52092](https://github.com/vllm-project/vllm/pull/52092) — [CPU] Ship triton-cpu wheel and fix several hardcoded pin_memory=True (#52092)
- **2026-08-13** [`903d2efe7e`](https://github.com/vllm-project/vllm/commit/903d2efe7e) [#51772](https://github.com/vllm-project/vllm/pull/51772) — [Attention][MLA] Fuse Kimi-K3 chunked-context K/V packing (#51772)
- **2026-08-13** [`3d204dfdaa`](https://github.com/vllm-project/vllm/commit/3d204dfdaa) [#52024](https://github.com/vllm-project/vllm/pull/52024) — Revert "[Perf][ROCm] Dual-stream decode with hipgraphs" (#52024)
- **2026-08-13** [`b369f10d5c`](https://github.com/vllm-project/vllm/commit/b369f10d5c) [#51821](https://github.com/vllm-project/vllm/pull/51821) — [Bugfix][ROCm][CI] Restore the DeepSeek-V4 input GEMM override point (#51821)
- **2026-08-13** [`caf9e8f7d5`](https://github.com/vllm-project/vllm/commit/caf9e8f7d5) [#52043](https://github.com/vllm-project/vllm/pull/52043) — [CI] Force source builds for hybrid dependencies (#52043)
- **2026-08-12** [`98f86b9c02`](https://github.com/vllm-project/vllm/commit/98f86b9c02) [#50017](https://github.com/vllm-project/vllm/pull/50017) — [ROCm] [bugfix] Chunked prefill paged decode masked load perf  (#50017)
- **2026-08-12** [`7f7a32cfec`](https://github.com/vllm-project/vllm/commit/7f7a32cfec) [#47808](https://github.com/vllm-project/vllm/pull/47808) — [Spec Decode] DSpark confidence-scheduled verification (#47808)
- **2026-08-12** [`d20a031d33`](https://github.com/vllm-project/vllm/commit/d20a031d33) [#51980](https://github.com/vllm-project/vllm/pull/51980) — [Bugfix][ROCm][MoE] Update AITER MXFP4 W4A16 tests to the renamed expert_mask (#51980)
- **2026-08-12** [`b745d08de1`](https://github.com/vllm-project/vllm/commit/b745d08de1) [#51860](https://github.com/vllm-project/vllm/pull/51860) — [ROCm][K3] Dequantize the fp8 decode query for MLA backends without quant-query support - TRITON_MLA (#51860)
- **2026-08-12** [`324f452f64`](https://github.com/vllm-project/vllm/commit/324f452f64) [#51464](https://github.com/vllm-project/vllm/pull/51464) — [ROCm] update triton in base docker for gluon compatibility (#51464)
- **2026-08-12** [`9035151d6c`](https://github.com/vllm-project/vllm/commit/9035151d6c) [#51255](https://github.com/vllm-project/vllm/pull/51255) — [Model] Add native Dots3 NOTE multimodal support (#51255)
- **2026-08-12** [`7f9173dfa2`](https://github.com/vllm-project/vllm/commit/7f9173dfa2) [#50654](https://github.com/vllm-project/vllm/pull/50654) — [ROCm][Perf] Kimi-K3 Fused kernel for KDA decode (#50654)
- **2026-08-12** [`20727e2841`](https://github.com/vllm-project/vllm/commit/20727e2841) [#50268](https://github.com/vllm-project/vllm/pull/50268) — [Hardware][AMD] Enable fused bf16→fp32 router GEMM on ROCm (#50268)
- **2026-08-12** [`793ca6998a`](https://github.com/vllm-project/vllm/commit/793ca6998a) [#51729](https://github.com/vllm-project/vllm/pull/51729) — [Docs][RL] Rewrite weight-transfer docs; standardize examples (#51729)
- **2026-08-12** [`045a986f3b`](https://github.com/vllm-project/vllm/commit/045a986f3b) [#51877](https://github.com/vllm-project/vllm/pull/51877) — [ROCm][CI] Speed Up ROCm Skinny GEMM Tests (reduced parameterizations,  (#51877)
- **2026-08-12** [`47ececb58e`](https://github.com/vllm-project/vllm/commit/47ececb58e) [#48223](https://github.com/vllm-project/vllm/pull/48223) — [Perf][ROCm] Dual-stream decode with hipgraphs (#48223)
- **2026-08-12** [`466855a2bf`](https://github.com/vllm-project/vllm/commit/466855a2bf) [#47017](https://github.com/vllm-project/vllm/pull/47017) — [ROCm] Enable DeepSeek-V4 on gfx11 (#47017)
- **2026-08-11** [`3e372c5ff2`](https://github.com/vllm-project/vllm/commit/3e372c5ff2) [#51837](https://github.com/vllm-project/vllm/pull/51837) — [Bugfix][ROCm] Give KV-first attention blocks their own page in hybrid models (#51837)
- **2026-08-11** [`0f0cb918b7`](https://github.com/vllm-project/vllm/commit/0f0cb918b7) [#49758](https://github.com/vllm-project/vllm/pull/49758) — [ROCm][MoE] Fix expert_map vs AITER expert_mask for non-AITER experts under EP (#49758)
- **2026-08-11** [`fd04edef3e`](https://github.com/vllm-project/vllm/commit/fd04edef3e) [#51838](https://github.com/vllm-project/vllm/pull/51838) — [Refactor] Delete dead code in models (#51838)
- **2026-08-11** [`1ab2801dde`](https://github.com/vllm-project/vllm/commit/1ab2801dde) [#50907](https://github.com/vllm-project/vllm/pull/50907) — [ROCm] Remove stale SDPA and skinny GEMM workarounds (#50907)
- **2026-08-11** [`c65aa2ee6c`](https://github.com/vllm-project/vllm/commit/c65aa2ee6c) [#51668](https://github.com/vllm-project/vllm/pull/51668) — Bump Transformers version to 5.15.0 (#51668)
- **2026-08-11** [`5426311d91`](https://github.com/vllm-project/vllm/commit/5426311d91) [#47896](https://github.com/vllm-project/vllm/pull/47896) — [Kernel][ROCm][Perf] FlyDSL decode-attention kernel for 4-bit TurboQuant KV cache  (#47896)
- **2026-08-11** [`12bea3eedc`](https://github.com/vllm-project/vllm/commit/12bea3eedc) [#51145](https://github.com/vllm-project/vllm/pull/51145) — [Bugfix][ROCm] Fix DeepSeek V4 DSpark probabilistic startup (#51145)
- **2026-08-11** [`a311916a29`](https://github.com/vllm-project/vllm/commit/a311916a29) [#46849](https://github.com/vllm-project/vllm/pull/46849) — [MRV2][Spec] Fuse AR speculator multi-step decodes back into one CUDA graph (#46849)
- **2026-08-11** [`1044d19998`](https://github.com/vllm-project/vllm/commit/1044d19998) [#51473](https://github.com/vllm-project/vllm/pull/51473) — [ROCm][DSV4] Preserve native MXFP4 TP8 shard allocation (#51473)
- **2026-08-11** [`2acb055ed7`](https://github.com/vllm-project/vllm/commit/2acb055ed7) [#44201](https://github.com/vllm-project/vllm/pull/44201) — [CPU][Zen] Route BF16 MoE inference through zentorch on AMD (#44201)
- **2026-08-11** [`75903e5067`](https://github.com/vllm-project/vllm/commit/75903e5067) [#51666](https://github.com/vllm-project/vllm/pull/51666) — [CI][AMD] Persist the openai-harmony tiktoken vocab cache across jobs (#51666)
- **2026-08-11** [`419b51b385`](https://github.com/vllm-project/vllm/commit/419b51b385) [#51721](https://github.com/vllm-project/vllm/pull/51721) — [Bugfix][ROCm][CI] Stabilize build context and source caches (#51721)
- **2026-08-10** [`1482d2e015`](https://github.com/vllm-project/vllm/commit/1482d2e015) [#47030](https://github.com/vllm-project/vllm/pull/47030) — [ROCm][DistInf] Enable vLLM DI CI with buildkite/slurm (#47030)
- **2026-08-10** [`79c865b838`](https://github.com/vllm-project/vllm/commit/79c865b838) [#51430](https://github.com/vllm-project/vllm/pull/51430) — [Perf] Narrow DeepSeek V4 eager CUDA graph region (#51430)
- **2026-08-10** [`0e2d78028c`](https://github.com/vllm-project/vllm/commit/0e2d78028c) [#51682](https://github.com/vllm-project/vllm/pull/51682) — [Bugfix][Kimi-K3] Give the AMD packed KDA decode kernel the state-index stride (#51682)
- **2026-08-10** [`37fbf52084`](https://github.com/vllm-project/vllm/commit/37fbf52084) [#51011](https://github.com/vllm-project/vllm/pull/51011) — [ROCm][MLA] [K3] Fix fp8 KV cache decode on the AITER MLA backend (#51011)
- **2026-08-10** [`436be94e13`](https://github.com/vllm-project/vllm/commit/436be94e13) [#51635](https://github.com/vllm-project/vllm/pull/51635) — [ROCm][Bugfix] Use TCP store when AITER custom all-reduce is enabled (#51635)
- **2026-08-10** [`74c94b9f29`](https://github.com/vllm-project/vllm/commit/74c94b9f29) [#51422](https://github.com/vllm-project/vllm/pull/51422) — [CI] Upgrade huggingface-hub to 1.27.0 (#51422)
- **2026-08-10** [`31cd109f18`](https://github.com/vllm-project/vllm/commit/31cd109f18) [#40958](https://github.com/vllm-project/vllm/pull/40958) — [ROCm][CI] Extend ROCm AITER MHA (FA) coverage (#40958)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#48645](https://github.com/vllm-project/vllm/issues/48645) | [Bug]: deepseek_v4 parser: reply without </think> routes the whole ans | — | 2026-08-17 |
| [#52594](https://github.com/vllm-project/vllm/issues/52594) | [Bug]: muse_glimmer cannot combine reasoning with structured outputs — | bug | 2026-08-17 |
| [#49224](https://github.com/vllm-project/vllm/issues/49224) | [Bug]: Model Runner V2 (now default for dense models) skips CUDA graph | bug | 2026-08-17 |
| [#52591](https://github.com/vllm-project/vllm/issues/52591) | [Bug]: two logger calls have mismatched %-args, so the log record is d | — | 2026-08-17 |
| [#48310](https://github.com/vllm-project/vllm/issues/48310) | [RFC] Sleep/Wake Correctness for RL | RFC | 2026-08-17 |
| [#52404](https://github.com/vllm-project/vllm/issues/52404) | [Bug]: 4 B200 GPU ，DP 4 + EP（or TP 4 + EP），Deepseek V4 Flash 0731 , si | bug | 2026-08-17 |
| [#52585](https://github.com/vllm-project/vllm/issues/52585) | [Performance][ROCm] gfx1100 long-prefill: unified attention BLOCK_M=16 | rocm, quantization | 2026-08-17 |
| [#50834](https://github.com/vllm-project/vllm/issues/50834) | [RFC]:  Unify the Tensor Type for Device-Pointer Storage to `torch.uin | RFC | 2026-08-17 |
| [#52568](https://github.com/vllm-project/vllm/issues/52568) | [Bug]: Qwen3.5-9B hybrid-GDN + dynamic LoRA on H20 produces NaN output | bug | 2026-08-17 |
| [#52576](https://github.com/vllm-project/vllm/issues/52576) | [Bug]: Triton MoE and block-FP8 GEMMs mishandle the K tile — an out-of | quantization | 2026-08-17 |
| [#52409](https://github.com/vllm-project/vllm/issues/52409) | EPD Tracker | — | 2026-08-17 |
| [#50682](https://github.com/vllm-project/vllm/issues/50682) | [ROCm][AMD] Kimi-K3 Gap and Roadmap Tracking | rocm, kimi, k3 | 2026-08-17 |
| [#52089](https://github.com/vllm-project/vllm/issues/52089) | [Bug]: Continuous Host Memory Growth / Possible Memory Leak with V2 Ru | bug | 2026-08-17 |
| [#38979](https://github.com/vllm-project/vllm/issues/38979) | [Bug]: Regression in vllm 0.19.0 - The page size of the layer is not d | bug, stale | 2026-08-17 |
| [#42490](https://github.com/vllm-project/vllm/issues/42490) | [Bug]: Async double streaming_update with shared-prefix reuse can leav | bug, stale | 2026-08-17 |
| [#42533](https://github.com/vllm-project/vllm/issues/42533) | [Bug]: ngram_gpu speculative decoding can propose draft tokens past ma | stale | 2026-08-17 |
| [#42842](https://github.com/vllm-project/vllm/issues/42842) | Code quality scan: 233 findings (A-, 81/100) | stale | 2026-08-17 |
| [#42876](https://github.com/vllm-project/vllm/issues/42876) | [Bug]: v0.21.0 release notes claim 'DeepSeek V4: AMD/ROCm support' but | rocm, stale | 2026-08-17 |
| [#42895](https://github.com/vllm-project/vllm/issues/42895) | [Bug]: NIXL disagg fails for Qwen3.5 hybrid model when prefill TP4 and | bug, stale | 2026-08-17 |
| [#42898](https://github.com/vllm-project/vllm/issues/42898) | [Bug]: Poor Qwen3.5 NVFP4 disagg GSM8K accuracy with 2p1d (2xTEP8 pref | bug, stale | 2026-08-17 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 56 |
| Other | 40 |
| Attention | 40 |
| MoE / Expert Parallel | 29 |
| CI / Build | 25 |
| Multimodal | 22 |
| Models | 17 |
| Serving / API | 16 |
| Scheduler / Engine | 15 |
| Quantization | 12 |
| Speculative Decoding | 11 |
| KV Cache / Offload | 8 |
| Disaggregation / PD | 7 |
| Perf / Benchmark | 5 |
| Docs | 4 |
| LoRA | 3 |
| Compilation / CUDA Graph | 2 |

## ROCm / AMD  (56 commits)

- **2026-08-17** [`311b3513af`](https://github.com/vllm-project/vllm/commit/311b3513af) [#52565](https://github.com/vllm-project/vllm/pull/52565)
  [ROCm][CI] Avoid forcing FlashAttention in the ColPali pooling test (#52565)
  _Files: `tests/models/multimodal/pooling/test_colpali.py`_
- **2026-08-17** [`71b578b9cc`](https://github.com/vllm-project/vllm/commit/71b578b9cc) [#49514](https://github.com/vllm-project/vllm/pull/49514)
  [ROCm][CI] Use the same-build wheel in Python-only CI (#49514)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `tests/standalone_tests/python_only_compile.sh`_
- **2026-08-17** [`0ad04cff1b`](https://github.com/vllm-project/vllm/commit/0ad04cff1b) [#52256](https://github.com/vllm-project/vllm/pull/52256)
  [ROCm][CI] Enable ViT CUDA graph tests on AMD gfx950 GPUs (#52256)
  _Files: `.buildkite/test-amd.yaml`, `docs/design/cuda_graphs_multimodal.md`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py`_
- **2026-08-16** [`ef43e3101b`](https://github.com/vllm-project/vllm/commit/ef43e3101b) [#52212](https://github.com/vllm-project/vllm/pull/52212)
  [ROCm][DSV4][Perf] Optimize Triton sparse-MLA decode on gfx950 (#52212)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/kernels/test_compressor_kv_cache.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py` _+1 more__
- **2026-08-16** [`6914d60b1e`](https://github.com/vllm-project/vllm/commit/6914d60b1e) [#49544](https://github.com/vllm-project/vllm/pull/49544)
  [ROCm][Perf] gfx942: use FlyDSL fp8 MQA logits kernel (ROCm/aiter#3913) (#49544)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-08-16** [`fe1c317157`](https://github.com/vllm-project/vllm/commit/fe1c317157) [#52356](https://github.com/vllm-project/vllm/pull/52356)
  [Bugfix][ROCm] Skip FP8 MLA prefill PS-metadata build for chunked-context batches (#52356)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-08-15** [`97388c44f9`](https://github.com/vllm-project/vllm/commit/97388c44f9) [#51538](https://github.com/vllm-project/vllm/pull/51538)
  [Bugfix] Make DSV4 sparse MLA work end-to-end for plain decode, MTP, and DSpark (#51538)
  _Files: `csrc/libtorch_stable/cooperative_topk.cuh`, `csrc/libtorch_stable/persistent_topk.cuh`, `tests/kernels/attention/test_flashmla_sparse.py`, `tests/kernels/moe/test_ocp_mx_moe.py` _+16 more__
- **2026-08-15** [`44fc57d7b7`](https://github.com/vllm-project/vllm/commit/44fc57d7b7) [#49515](https://github.com/vllm-project/vllm/pull/49515)
  [ROCm][CI] Select CPU platform for native no-GPU jobs (#49515)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `tests/test_zen_cpu_platform_detection.py`, `vllm/platforms/__init__.py`_
- **2026-08-15** [`615d4cfade`](https://github.com/vllm-project/vllm/commit/615d4cfade) [#43107](https://github.com/vllm-project/vllm/pull/43107)
  [Core] Check for GPU<->CPU syncs during CI (#43107)
  _Files: `.buildkite/test_areas/plugins.yaml`, `docker/Dockerfile`, `docker/Dockerfile.rocm`, `tests/models/multimodal/generation/test_mm_prefix_lm.py` _+40 more__
- **2026-08-14** [`9df9b0b0a1`](https://github.com/vllm-project/vllm/commit/9df9b0b0a1) [#52400](https://github.com/vllm-project/vllm/pull/52400)
  [ROCm]: Drop pybind11 from Dockerfile.rocm to prevent version mismatch (#52400)
  _Files: `docker/Dockerfile.rocm`_
- **2026-08-14** [`c794754062`](https://github.com/vllm-project/vllm/commit/c794754062) [#50597](https://github.com/vllm-project/vllm/pull/50597)
  [ROCm]Remove special-case SiTU support model-specific gating (#50597)
  _Files: `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/mxfp4.py`_
- **2026-08-14** [`9b0ab5dd53`](https://github.com/vllm-project/vllm/commit/9b0ab5dd53) [#51216](https://github.com/vllm-project/vllm/pull/51216)
  [ROCm][AMD] Enable preshuffled sparse indexing for 16-token blocks (#51216)
  _Files: `tests/v1/worker/test_gpu_model_runner.py`, `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-08-14** [`59d1af5698`](https://github.com/vllm-project/vllm/commit/59d1af5698) [#49365](https://github.com/vllm-project/vllm/pull/49365)
  Detect ROCm wheel variant from environment for precompiled wheels. (#49365)
  _Files: `setup.py`, `tests/standalone_tests/python_only_compile.sh`_
- **2026-08-13** [`73b83949f7`](https://github.com/vllm-project/vllm/commit/73b83949f7) [#51633](https://github.com/vllm-project/vllm/pull/51633)
  [Platform] Add check_runner_kv_caches_multi_layer (#51633)
  _Files: `vllm/platforms/cpu.py`, `vllm/platforms/cuda.py`, `vllm/platforms/interface.py`, `vllm/platforms/rocm.py` _+2 more__
- **2026-08-13** [`11c3fa4adc`](https://github.com/vllm-project/vllm/commit/11c3fa4adc) [#52139](https://github.com/vllm-project/vllm/pull/52139)
  [Bugfix][ROCm][CI] Give the AITER MLA decode metadata stub its MLA dims (#52139)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_decode_metadata.py`_
- **2026-08-13** [`c5b7c069a4`](https://github.com/vllm-project/vllm/commit/c5b7c069a4) [#51159](https://github.com/vllm-project/vllm/pull/51159)
  [ROCm] Defer `tilelang` import through its import `from vllm.tilelang_utils import tilelang` and relaxed `has_tilelang` (#51159)
  _Files: `docs/assets/contributing/dockerfile-stages-dependency.png`, `tests/jit_monitor/test_hooks.py`, `tests/kernels/test_mhc_tilelang_jit.py`, `tools/pre_commit/check_forbidden_imports.py` _+4 more__
- **2026-08-13** [`b96bcd0b47`](https://github.com/vllm-project/vllm/commit/b96bcd0b47) [#51280](https://github.com/vllm-project/vllm/pull/51280)
  [ROCm][CI] Solidify entrypoint LLM lifecycle (#51280)
  _Files: `tests/entrypoints/llm/offline_mode/test_offline_mode.py`, `tests/entrypoints/llm/test_chat.py`, `tests/entrypoints/llm/test_collective_rpc.py`, `tests/entrypoints/llm/test_generate.py` _+20 more__
- **2026-08-13** [`f3c1638927`](https://github.com/vllm-project/vllm/commit/f3c1638927) [#51653](https://github.com/vllm-project/vllm/pull/51653)
  [ROCm] Enable V2 model runner for Kimi-K3 on ROCm (#51653)
  _Files: `vllm/config/vllm.py`_
- **2026-08-13** [`5fee0a872d`](https://github.com/vllm-project/vllm/commit/5fee0a872d) [#51998](https://github.com/vllm-project/vllm/pull/51998)
  chore: Upstream Cohere parser fixes + tests (#51998)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/rocm.in` _+6 more__
- **2026-08-13** [`f96261637c`](https://github.com/vllm-project/vllm/commit/f96261637c) [#51862](https://github.com/vllm-project/vllm/pull/51862)
  [ROCm][Perf] Kimi-K3 Remove prefill pipeline stall in chunk KDA (#51862)
  _Files: `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py` _+1 more__
- **2026-08-13** [`373592ef57`](https://github.com/vllm-project/vllm/commit/373592ef57) [#52092](https://github.com/vllm-project/vllm/pull/52092)
  [CPU] Ship triton-cpu wheel and fix several hardcoded pin_memory=True (#52092)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `docker/Dockerfile.cpu`, `vllm/model_executor/models/granite_speech.py`, `vllm/model_executor/models/qwen3_vl.py` _+4 more__
- **2026-08-13** [`903d2efe7e`](https://github.com/vllm-project/vllm/commit/903d2efe7e) [#51772](https://github.com/vllm-project/vllm/pull/51772)
  [Attention][MLA] Fuse Kimi-K3 chunked-context K/V packing (#51772)
  _Files: `csrc/libtorch_stable/fused_kimi_k3_mla_key_concat_kv_cache_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py` _+11 more__
- **2026-08-13** [`3d204dfdaa`](https://github.com/vllm-project/vllm/commit/3d204dfdaa) [#52024](https://github.com/vllm-project/vllm/pull/52024)
  Revert "[Perf][ROCm] Dual-stream decode with hipgraphs" (#52024)
  _Files: `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`, `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`_
- **2026-08-13** [`b369f10d5c`](https://github.com/vllm-project/vllm/commit/b369f10d5c) [#51821](https://github.com/vllm-project/vllm/pull/51821)
  [Bugfix][ROCm][CI] Restore the DeepSeek-V4 input GEMM override point (#51821)
  _Files: `vllm/models/deepseek_v4/attention.py`_
- **2026-08-13** [`caf9e8f7d5`](https://github.com/vllm-project/vllm/commit/caf9e8f7d5) [#52043](https://github.com/vllm-project/vllm/pull/52043)
  [CI] Force source builds for hybrid dependencies (#52043)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_language.yaml`_
- **2026-08-12** [`98f86b9c02`](https://github.com/vllm-project/vllm/commit/98f86b9c02) [#50017](https://github.com/vllm-project/vllm/pull/50017)
  [ROCm] [bugfix] Chunked prefill paged decode masked load perf  (#50017)
  _Files: `vllm/v1/attention/ops/chunked_prefill_paged_decode.py`_
- **2026-08-12** [`7f7a32cfec`](https://github.com/vllm-project/vllm/commit/7f7a32cfec) [#47808](https://github.com/vllm-project/vllm/pull/47808)
  [Spec Decode] DSpark confidence-scheduled verification (#47808)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `docs/features/speculative_decoding/README.md`, `docs/features/speculative_decoding/adaptive_verification.md`, `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-DSpark-confidence-TP4.yaml` _+36 more__
- **2026-08-12** [`d20a031d33`](https://github.com/vllm-project/vllm/commit/d20a031d33) [#51980](https://github.com/vllm-project/vllm/pull/51980)
  [Bugfix][ROCm][MoE] Update AITER MXFP4 W4A16 tests to the renamed expert_mask (#51980)
  _Files: `tests/kernels/moe/test_rocm_aiter_moe.py`_
- **2026-08-12** [`b745d08de1`](https://github.com/vllm-project/vllm/commit/b745d08de1) [#51860](https://github.com/vllm-project/vllm/pull/51860)
  [ROCm][K3] Dequantize the fp8 decode query for MLA backends without quant-query support - TRITON_MLA (#51860)
  _Files: `vllm/models/kimi_k3/nvidia/mla.py`_
- **2026-08-12** [`324f452f64`](https://github.com/vllm-project/vllm/commit/324f452f64) [#51464](https://github.com/vllm-project/vllm/pull/51464)
  [ROCm] update triton in base docker for gluon compatibility (#51464)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-08-12** [`9035151d6c`](https://github.com/vllm-project/vllm/commit/9035151d6c) [#51255](https://github.com/vllm-project/vllm/pull/51255)
  [Model] Add native Dots3 NOTE multimodal support (#51255)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_causal_verify_mask.py`, `tests/models/registry.py`, `tests/models/test_registry.py`, `tests/tool_parsers/test_dots_tool_parser.py` _+24 more__
- **2026-08-12** [`7f9173dfa2`](https://github.com/vllm-project/vllm/commit/7f9173dfa2) [#50654](https://github.com/vllm-project/vllm/pull/50654)
  [ROCm][Perf] Kimi-K3 Fused kernel for KDA decode (#50654)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py`, `csrc/libtorch_stable/kimi_k3/fused_kda_decode_kernel_rocm.cu`, `tests/models/kimi_k3/test_amd_kda_decode.py` _+2 more__
- **2026-08-12** [`20727e2841`](https://github.com/vllm-project/vllm/commit/20727e2841) [#50268](https://github.com/vllm-project/vllm/pull/50268)
  [Hardware][AMD] Enable fused bf16→fp32 router GEMM on ROCm (#50268)
  _Files: `tests/kernels/test_gate_linear_rocm_dispatch.py`, `vllm/model_executor/layers/fused_moe/router/gate_linear.py`_
- **2026-08-12** [`793ca6998a`](https://github.com/vllm-project/vllm/commit/793ca6998a) [#51729](https://github.com/vllm-project/vllm/pull/51729)
  [Docs][RL] Rewrite weight-transfer docs; standardize examples (#51729)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`, `docs/training/weight_transfer/README.md`, `docs/training/weight_transfer/base.md` _+12 more__
- **2026-08-12** [`045a986f3b`](https://github.com/vllm-project/vllm/commit/045a986f3b) [#51877](https://github.com/vllm-project/vllm/pull/51877)
  [ROCm][CI] Speed Up ROCm Skinny GEMM Tests (reduced parameterizations,  (#51877)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/quantization/test_rocm_skinny_gemms.py`_
- **2026-08-12** [`47ececb58e`](https://github.com/vllm-project/vllm/commit/47ececb58e) [#48223](https://github.com/vllm-project/vllm/pull/48223)
  [Perf][ROCm] Dual-stream decode with hipgraphs (#48223)
  _Files: `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`, `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`_
- **2026-08-12** [`466855a2bf`](https://github.com/vllm-project/vllm/commit/466855a2bf) [#47017](https://github.com/vllm-project/vllm/pull/47017)
  [ROCm] Enable DeepSeek-V4 on gfx11 (#47017)
  _Files: `vllm/_aiter_ops.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/platforms/rocm.py`_
- **2026-08-11** [`3e372c5ff2`](https://github.com/vllm-project/vllm/commit/3e372c5ff2) [#51837](https://github.com/vllm-project/vllm/pull/51837)
  [Bugfix][ROCm] Give KV-first attention blocks their own page in hybrid models (#51837)
  _Files: `tests/v1/worker/test_attn_utils.py`, `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-08-11** [`0f0cb918b7`](https://github.com/vllm-project/vllm/commit/0f0cb918b7) [#49758](https://github.com/vllm-project/vllm/pull/49758)
  [ROCm][MoE] Fix expert_map vs AITER expert_mask for non-AITER experts under EP (#49758)
  _Files: `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp8_moe.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py` _+2 more__
- **2026-08-11** [`fd04edef3e`](https://github.com/vllm-project/vllm/commit/fd04edef3e) [#51838](https://github.com/vllm-project/vllm/pull/51838)
  [Refactor] Delete dead code in models (#51838)
  _Files: `vllm/lora/layers/fused_moe.py`, `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`, `vllm/model_executor/layers/fused_moe/runner/moe_runner_interface.py`, `vllm/model_executor/models/AXK1.py` _+21 more__
- **2026-08-11** [`1ab2801dde`](https://github.com/vllm-project/vllm/commit/1ab2801dde) [#50907](https://github.com/vllm-project/vllm/pull/50907)
  [ROCm] Remove stale SDPA and skinny GEMM workarounds (#50907)
  _Files: `csrc/libtorch_stable/moe/moe_align_sum_kernels.cu`, `examples/rl/rlhf_async_new_apis.py`, `tests/entrypoints/multimodal/openai/chat_completion/test_vision.py`, `tests/entrypoints/openai/chat_completion/test_completion_with_function_calling.py` _+52 more__
- **2026-08-11** [`c65aa2ee6c`](https://github.com/vllm-project/vllm/commit/c65aa2ee6c) [#51668](https://github.com/vllm-project/vllm/pull/51668)
  Bump Transformers version to 5.15.0 (#51668)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt` _+7 more__
- **2026-08-11** [`5426311d91`](https://github.com/vllm-project/vllm/commit/5426311d91) [#47896](https://github.com/vllm-project/vllm/pull/47896)
  [Kernel][ROCm][Perf] FlyDSL decode-attention kernel for 4-bit TurboQuant KV cache  (#47896)
  _Files: `tests/kernels/turboquant/__init__.py`, `tests/kernels/turboquant/test_flydsl_turboquant_decode.py`, `vllm/platforms/rocm.py`, `vllm/v1/attention/backends/turboquant_attn.py` _+9 more__
- **2026-08-11** [`12bea3eedc`](https://github.com/vllm-project/vllm/commit/12bea3eedc) [#51145](https://github.com/vllm-project/vllm/pull/51145)
  [Bugfix][ROCm] Fix DeepSeek V4 DSpark probabilistic startup (#51145)
  _Files: `vllm/models/deepseek_v4/amd/dspark.py`_
- **2026-08-11** [`a311916a29`](https://github.com/vllm-project/vllm/commit/a311916a29) [#46849](https://github.com/vllm-project/vllm/pull/46849)
  [MRV2][Spec] Fuse AR speculator multi-step decodes back into one CUDA graph (#46849)
  _Files: `docs/design/model_runner_v2.md`, `tests/v1/worker/test_gpu_autoregressive_speculator.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/v1/attention/backend.py` _+6 more__
- **2026-08-11** [`1044d19998`](https://github.com/vllm-project/vllm/commit/1044d19998) [#51473](https://github.com/vllm-project/vllm/pull/51473)
  [ROCm][DSV4] Preserve native MXFP4 TP8 shard allocation (#51473)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-08-11** [`2acb055ed7`](https://github.com/vllm-project/vllm/commit/2acb055ed7) [#44201](https://github.com/vllm-project/vllm/pull/44201)
  [CPU][Zen] Route BF16 MoE inference through zentorch on AMD (#44201)
  _Files: `setup.py`, `tests/kernels/moe/test_zen_cpu_fused_moe.py`, `vllm/model_executor/kernels/linear/zentorch_utils.py`, `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`_
- **2026-08-11** [`75903e5067`](https://github.com/vllm-project/vllm/commit/75903e5067) [#51666](https://github.com/vllm-project/vllm/pull/51666)
  [CI][AMD] Persist the openai-harmony tiktoken vocab cache across jobs (#51666)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-08-11** [`419b51b385`](https://github.com/vllm-project/vllm/commit/419b51b385) [#51721](https://github.com/vllm-project/vllm/pull/51721)
  [Bugfix][ROCm][CI] Stabilize build context and source caches (#51721)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `docker/Dockerfile.rocm`_
- **2026-08-10** [`1482d2e015`](https://github.com/vllm-project/vllm/commit/1482d2e015) [#47030](https://github.com/vllm-project/vllm/pull/47030)
  [ROCm][DistInf] Enable vLLM DI CI with buildkite/slurm (#47030)
  _Files: `.buildkite/amd-disagg/cluster.sh`, `.buildkite/amd-disagg/models.yaml`, `.buildkite/amd-disagg/pipeline-disagg.yaml`, `.buildkite/amd-disagg/run-slurm-disagg-test.sh` _+2 more__
- **2026-08-10** [`79c865b838`](https://github.com/vllm-project/vllm/commit/79c865b838) [#51430](https://github.com/vllm-project/vllm/pull/51430)
  [Perf] Narrow DeepSeek V4 eager CUDA graph region (#51430)
  _Files: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-08-10** [`0e2d78028c`](https://github.com/vllm-project/vllm/commit/0e2d78028c) [#51682](https://github.com/vllm-project/vllm/pull/51682)
  [Bugfix][Kimi-K3] Give the AMD packed KDA decode kernel the state-index stride (#51682)
  _Files: `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`_
- **2026-08-10** [`37fbf52084`](https://github.com/vllm-project/vllm/commit/37fbf52084) [#51011](https://github.com/vllm-project/vllm/pull/51011)
  [ROCm][MLA] [K3] Fix fp8 KV cache decode on the AITER MLA backend (#51011)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_head_padding.py`, `tests/v1/attention/test_rocm_aiter_mla_fp8_decode_routing.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-08-10** [`436be94e13`](https://github.com/vllm-project/vllm/commit/436be94e13) [#51635](https://github.com/vllm-project/vllm/pull/51635)
  [ROCm][Bugfix] Use TCP store when AITER custom all-reduce is enabled (#51635)
  _Files: `vllm/utils/network_utils.py`, `vllm/v1/executor/multiproc_executor.py`, `vllm/v1/executor/uniproc_executor.py`_
- **2026-08-10** [`74c94b9f29`](https://github.com/vllm-project/vllm/commit/74c94b9f29) [#51422](https://github.com/vllm-project/vllm/pull/51422)
  [CI] Upgrade huggingface-hub to 1.27.0 (#51422)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt` _+1 more__
- **2026-08-10** [`31cd109f18`](https://github.com/vllm-project/vllm/commit/31cd109f18) [#40958](https://github.com/vllm-project/vllm/pull/40958)
  [ROCm][CI] Extend ROCm AITER MHA (FA) coverage (#40958)
  _Files: `tests/kernels/attention/test_aiter_flash_attn.py`, `tests/kernels/attention/test_rocm_aiter_fa.py`_

## Other  (40 commits)

- **2026-08-17** [`a02cfccbc6`](https://github.com/vllm-project/vllm/commit/a02cfccbc6) [#50729](https://github.com/vllm-project/vllm/pull/50729)
  [Bugfix][Mamba] Fix overlapping state copy race (#50729)
  _Files: `tests/v1/worker/test_mamba_utils.py`, `vllm/v1/worker/mamba_utils.py`_
- **2026-08-17** [`6664d397bf`](https://github.com/vllm-project/vllm/commit/6664d397bf) [#52329](https://github.com/vllm-project/vllm/pull/52329)
  [Performance][MRV2] Cache logits-processing request state (#52329)
  _Files: `tests/v1/worker/test_gpu_sampler_flags.py`, `tests/v1/worker/test_gpu_thinking_budget.py`, `vllm/v1/worker/gpu/sample/sampler.py`_
- **2026-08-16** [`fdab2b10bc`](https://github.com/vllm-project/vllm/commit/fdab2b10bc) [#52425](https://github.com/vllm-project/vllm/pull/52425)
  [ModelRunner v2] Support Transformers pooling model  (#52425)
  _Files: `tests/models/transformers/test_backend.py`, `vllm/v1/worker/gpu/model_states/__init__.py`_
- **2026-08-16** [`9409f59e09`](https://github.com/vllm-project/vllm/commit/9409f59e09) [#52514](https://github.com/vllm-project/vllm/pull/52514)
  [Core] Add CuMemAllocator.discard() for tag-selective GPU memory release (#52514)
  _Files: `tests/basic_correctness/test_mem.py`, `vllm/device_allocator/__init__.py`, `vllm/device_allocator/cumem.py`, `vllm/device_allocator/xpumem.py`_
- **2026-08-15** [`c94cdd0ae0`](https://github.com/vllm-project/vllm/commit/c94cdd0ae0) [#49613](https://github.com/vllm-project/vllm/pull/49613)
  [Bugfix][Sampling] Clear empty side on thinking-budget asymmetric SWAP (#49613)
  _Files: `tests/v1/sample/test_thinking_budget_state.py`, `vllm/v1/sample/thinking_budget_state.py`_
- **2026-08-15** [`5cecfc0137`](https://github.com/vllm-project/vllm/commit/5cecfc0137) [#52431](https://github.com/vllm-project/vllm/pull/52431)
  [Bugfix] Fix modelscope usage (#52431)
  _Files: `vllm/envs.py`, `vllm/transformers_utils/utils.py`_
- **2026-08-14** [`aa31003573`](https://github.com/vllm-project/vllm/commit/aa31003573) [#51664](https://github.com/vllm-project/vllm/pull/51664)
  [Bugfix][Helm] Fix chart resource references (#51664)
  _Files: `examples/deployment/chart-helm/Chart.yaml`, `examples/deployment/chart-helm/templates/_helpers.tpl`, `examples/deployment/chart-helm/templates/deployment.yaml`, `examples/deployment/chart-helm/templates/hpa.yaml` _+5 more__
- **2026-08-14** [`20405bfb15`](https://github.com/vllm-project/vllm/commit/20405bfb15) [#51989](https://github.com/vllm-project/vllm/pull/51989)
  [Bugfix] Fix Cosmos3-Edge processor after transformers 5.15 release (#51989)
  _Files: `tests/models/registry.py`, `vllm/transformers_utils/processors/cosmos3_edge.py`_
- **2026-08-14** [`3c8676aebb`](https://github.com/vllm-project/vllm/commit/3c8676aebb) [#51650](https://github.com/vllm-project/vllm/pull/51650)
  [PP][XPU]Overlap async-scheduling PP sampled-token broadcast with compute (#51650)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-08-14** [`ac7509e2b1`](https://github.com/vllm-project/vllm/commit/ac7509e2b1) [#51099](https://github.com/vllm-project/vllm/pull/51099)
  [Bugfix][CPU][RISC-V] Fix build: make FP32Vec copy constructors non-explicit (#51099)
  _Files: `csrc/cpu/cpu_types_riscv_impl.hpp`_
- **2026-08-14** [`d18bb7b390`](https://github.com/vllm-project/vllm/commit/d18bb7b390) [#52237](https://github.com/vllm-project/vllm/pull/52237)
  [UT] fix device of test_outputs.py (#52237)
  _Files: `tests/v1/test_outputs.py`_
- **2026-08-14** [`fe4c5dcd4c`](https://github.com/vllm-project/vllm/commit/fe4c5dcd4c) [#52118](https://github.com/vllm-project/vllm/pull/52118)
  [XPU] [Bugfix] process ragged weights in xpu linear backend (#52118)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`_
- **2026-08-14** [`38f097fab8`](https://github.com/vllm-project/vllm/commit/38f097fab8) [#51796](https://github.com/vllm-project/vllm/pull/51796)
  [Bugfix] Reject NUL byte in structured_outputs.regex (#51796)
  _Files: `tests/v1/structured_output/test_validation.py`, `vllm/sampling_params.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-08-13** [`e6b2a8ad5e`](https://github.com/vllm-project/vllm/commit/e6b2a8ad5e) [#50595](https://github.com/vllm-project/vllm/pull/50595)
  [Bugfix][Structured Output] Mask request stop tokens in xgrammar until grammar terminates (#50595)
  _Files: `tests/parser/test_harmony.py`, `vllm/parser/harmony.py`_
- **2026-08-13** [`170592a931`](https://github.com/vllm-project/vllm/commit/170592a931) [#52172](https://github.com/vllm-project/vllm/pull/52172)
  [Bugfix] Disable sequence parallelism for Dots3 NOTE (#52172)
  _Files: `vllm/models/dots3_note/nvidia/model.py`_
- **2026-08-13** [`015660da91`](https://github.com/vllm-project/vllm/commit/015660da91) [#52145](https://github.com/vllm-project/vllm/pull/52145)
  [Misc] Add missing return type annotations in outputs.py (#52145)
  _Files: `vllm/outputs.py`_
- **2026-08-13** [`10bcad2523`](https://github.com/vllm-project/vllm/commit/10bcad2523) [#52123](https://github.com/vllm-project/vllm/pull/52123)
  Update CODEOWNERS (#52123)
  _Files: `.github/CODEOWNERS`_
- **2026-08-13** [`79f3183f86`](https://github.com/vllm-project/vllm/commit/79f3183f86) [#52058](https://github.com/vllm-project/vllm/pull/52058)
  [Bugfix] Bound KV block zeroing launch geometry (#52058)
  _Files: `tests/v1/worker/test_kv_block_zeroer.py`, `vllm/v1/worker/utils.py`_
- **2026-08-13** [`f9538af28c`](https://github.com/vllm-project/vllm/commit/f9538af28c) [#52076](https://github.com/vllm-project/vllm/pull/52076)
  [Core] Clearer comments in `BlockPool.free_blocks()` (#52076)
  _Files: `vllm/v1/core/block_pool.py`_
- **2026-08-12** [`34735aceda`](https://github.com/vllm-project/vllm/commit/34735aceda) [#52028](https://github.com/vllm-project/vllm/pull/52028)
  [Bugfix] Pin DeepEP by its full commit hash (#52028)
  _Files: `tools/ep_kernels/install_python_libraries.sh`_
- **2026-08-12** [`02ac17851d`](https://github.com/vllm-project/vllm/commit/02ac17851d) [#51917](https://github.com/vllm-project/vllm/pull/51917)
  [Refactor][MRV2] Unify uniform decode token count helper (#51917)
  _Files: `tests/v1/spec_decode/test_dynamic_sd_cug.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-08-12** [`f2906b492e`](https://github.com/vllm-project/vllm/commit/f2906b492e) [#49505](https://github.com/vllm-project/vllm/pull/49505)
  [Bugfix] Avoid repeated layerwise reload warning scans (#49505)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/model_loader/reload/layerwise.py`_
- **2026-08-12** [`3fa89225bc`](https://github.com/vllm-project/vllm/commit/3fa89225bc) [#51652](https://github.com/vllm-project/vllm/pull/51652)
  [CI/Build] Use file rendezvous for local distributed tests (#51652)
  _Files: `tests/compile/passes/distributed/test_async_tp.py`, `tests/distributed/test_dcp_a2a.py`, `tests/utils_/test_network_utils.py`_
- **2026-08-12** [`f067737b2a`](https://github.com/vllm-project/vllm/commit/f067737b2a) [#51840](https://github.com/vllm-project/vllm/pull/51840)
  [Bugfix][TieredOffloading] : Return HIT_PENDING when KV promotion is triggered (#51840)
  _Files: `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/manager.py`_
- **2026-08-12** [`0a94d85a66`](https://github.com/vllm-project/vllm/commit/0a94d85a66) [#51865](https://github.com/vllm-project/vllm/pull/51865)
  [Bugfix][MRV2] Require all requests to be decoding for uniform-decode dispatch (#51865)
  _Files: `tests/v1/spec_decode/test_dynamic_sd_cug.py`, `tests/v1/worker/test_gpu_batch_ordering.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/input_batch.py` _+5 more__
- **2026-08-11** [`cb30f6f8dd`](https://github.com/vllm-project/vllm/commit/cb30f6f8dd) [#51736](https://github.com/vllm-project/vllm/pull/51736)
  [Testing] Fix test_sharded_state_loader (#51736)
  _Files: `tests/model_executor/model_loader/test_sharded_state_loader.py`_
- **2026-08-11** [`ded6c452c3`](https://github.com/vllm-project/vllm/commit/ded6c452c3) [#51850](https://github.com/vllm-project/vllm/pull/51850)
  [Bugfix] Support HF-config compat for Inkling (#51850)
  _Files: `vllm/models/inkling/configs.py`_
- **2026-08-11** [`9cc347ae42`](https://github.com/vllm-project/vllm/commit/9cc347ae42) [#45042](https://github.com/vllm-project/vllm/pull/45042)
  Enable `MiniCPMV` for vLLM in CI (#45042)
  _Files: `tests/models/registry.py`_
- **2026-08-11** [`457a5f34db`](https://github.com/vllm-project/vllm/commit/457a5f34db) [#50020](https://github.com/vllm-project/vllm/pull/50020)
  [Bugfix][MRV2] Support encoder timing stats in model runner V2 (#50020)
  _Files: `tests/v1/worker/test_encoder_runner.py`, `vllm/v1/worker/gpu/mm/encoder_runner.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/model_states/encoder_decoder.py` _+3 more__
- **2026-08-11** [`f863387250`](https://github.com/vllm-project/vllm/commit/f863387250) [#51770](https://github.com/vllm-project/vllm/pull/51770)
  [XPU] Fix UVA weight offloading (non-pinned-tensor views and static Triton launcher) (#51770)
  _Files: `vllm/platforms/xpu.py`, `vllm/utils/torch_utils.py`_
- **2026-08-11** [`78e7fdd1ab`](https://github.com/vllm-project/vllm/commit/78e7fdd1ab) [#51627](https://github.com/vllm-project/vllm/pull/51627)
  [Bugfix][CPU] Make the Apple Silicon BF16 probe fall back instead of raising (#51627)
  _Files: `vllm/platforms/cpu.py`_
- **2026-08-11** [`ce07118669`](https://github.com/vllm-project/vllm/commit/ce07118669) [#51766](https://github.com/vllm-project/vllm/pull/51766)
  [Bugfix][Core] Preserve Mamba running CoW after external hits (#51766)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-08-11** [`490259c1f6`](https://github.com/vllm-project/vllm/commit/490259c1f6) [#50977](https://github.com/vllm-project/vllm/pull/50977)
  profiler: add PrivateUse1 activity support for custom backends (#50977)
  _Files: `vllm/profiler/wrapper.py`_
- **2026-08-11** [`d8c70f2243`](https://github.com/vllm-project/vllm/commit/d8c70f2243) [#51235](https://github.com/vllm-project/vllm/pull/51235)
  [Rust Frontend] Upgrade MiniJinja to 2.22 & remove method lookup workaround (#51235)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/renderer/hf/mod.rs` _+1 more__
- **2026-08-10** [`98a4144a41`](https://github.com/vllm-project/vllm/commit/98a4144a41) [#51097](https://github.com/vllm-project/vllm/pull/51097)
  [Bugfix] Preserve non-logitproc entry points in tests (#51097)
  _Files: `tests/v1/logits_processors/test_custom_offline.py`, `tests/v1/logits_processors/utils.py`_
- **2026-08-10** [`05f0a80016`](https://github.com/vllm-project/vllm/commit/05f0a80016) [#49227](https://github.com/vllm-project/vllm/pull/49227)
  [Bugfix][Structured Output] Mask request stop tokens in xgrammar until grammar terminates (#49227)
  _Files: `tests/v1/structured_output/test_backend_xgrammar_stop_tokens.py`, `vllm/v1/structured_output/__init__.py`, `vllm/v1/structured_output/backend_guidance.py`, `vllm/v1/structured_output/backend_lm_format_enforcer.py` _+3 more__
- **2026-08-10** [`3a749ce816`](https://github.com/vllm-project/vllm/commit/3a749ce816) [#51424](https://github.com/vllm-project/vllm/pull/51424)
  [Build] Skip precompiled wheel fetch during metadata hooks (#51424)
  _Files: `setup.py`_
- **2026-08-10** [`3dafaef027`](https://github.com/vllm-project/vllm/commit/3dafaef027) [#51573](https://github.com/vllm-project/vllm/pull/51573)
  [Bugfix][Core] Emit --no-{key} for false BooleanOptionalAction flags in YAML config (#51573)
  _Files: `tests/utils_/test_argparse_utils.py`, `vllm/utils/argparse_utils.py`_
- **2026-08-10** [`7303c66f68`](https://github.com/vllm-project/vllm/commit/7303c66f68) [#48171](https://github.com/vllm-project/vllm/pull/48171)
  [Bugfix] Fix lfm2 tool parser dropping calls with brackets or newline… (#48171)
  _Files: `tests/tool_parsers/test_lfm2_tool_parser.py`, `tests/tool_parsers/test_utils.py`, `vllm/tool_parsers/lfm2_tool_parser.py`, `vllm/tool_parsers/utils.py`_
- **2026-08-10** [`a123159f7a`](https://github.com/vllm-project/vllm/commit/a123159f7a) [#48798](https://github.com/vllm-project/vllm/pull/48798)
  Add tiering offloading metrics (#48798)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_metrics.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py` _+12 more__

## Attention  (40 commits)

- **2026-08-17** [`292187dd8c`](https://github.com/vllm-project/vllm/commit/292187dd8c) [#52492](https://github.com/vllm-project/vllm/pull/52492)
  [Bugfix][DSv4] Keep indexer scoring in breakable graphs (#52492)
  _Files: `vllm/models/deepseek_v4/attention.py`_
- **2026-08-17** [`a18c9b56ff`](https://github.com/vllm-project/vllm/commit/a18c9b56ff) [#52458](https://github.com/vllm-project/vllm/pull/52458)
  [Kimi-K3][Perf] Update FlashKDA for automatic K2 V-split (#52458)
  _Files: `cmake/external_projects/flashkda.cmake`_
- **2026-08-16** [`1f0e0bf612`](https://github.com/vllm-project/vllm/commit/1f0e0bf612) [#52050](https://github.com/vllm-project/vllm/pull/52050)
  [Bugfix][Attention] Temporarily disable FA4 head-dim 256 (#52050)
  _Files: `tests/models/multimodal/pooling/test_colpali.py`, `vllm/v1/attention/backends/fa_utils.py`, `vllm/v1/attention/backends/flash_attn.py`_
- **2026-08-16** [`8efa13b700`](https://github.com/vllm-project/vllm/commit/8efa13b700) [#52401](https://github.com/vllm-project/vllm/pull/52401)
  [Bugfix] Pick the DeepSeek V4 eager cudagraph region per model runner (#52401)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`, `vllm/models/deepseek_v4/attention.py`_
- **2026-08-16** [`edd4c8176c`](https://github.com/vllm-project/vllm/commit/edd4c8176c) [#51318](https://github.com/vllm-project/vllm/pull/51318)
  [Bugfix][DSv4] Revert adaptive C128A metadata packing (#51318)
  _Files: `tests/kernels/attention/test_flashmla_sparse.py`, `vllm/models/deepseek_v4/sparse_mla.py`_
- **2026-08-15** [`acb0f1dcdb`](https://github.com/vllm-project/vllm/commit/acb0f1dcdb) [#52288](https://github.com/vllm-project/vllm/pull/52288)
  [Bugfix][Spec Decode] DSpark: inherit the target's attention backend when the speculative config names none (#52288)
  _Files: `vllm/v1/worker/gpu/spec_decode/dspark/utils.py`_
- **2026-08-14** [`d6f17f3d53`](https://github.com/vllm-project/vllm/commit/d6f17f3d53) [#52374](https://github.com/vllm-project/vllm/pull/52374)
  [MRV2] Support attention-free models (#52374)
  _Files: `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/model_states/__init__.py`_
- **2026-08-14** [`3e3ceb1961`](https://github.com/vllm-project/vllm/commit/3e3ceb1961) [#52369](https://github.com/vllm-project/vllm/pull/52369)
  [Perf] Avoid more GPU<->CPU syncs in multimodal encoders (#52369)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/interns1.py` _+5 more__
- **2026-08-14** [`e078a2238a`](https://github.com/vllm-project/vllm/commit/e078a2238a) [#52241](https://github.com/vllm-project/vllm/pull/52241)
  [Bugfix] Widen flashinfer.comm import guard so a failed import doesn't abort engine startup (#52241)
  _Files: `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`_
- **2026-08-14** [`03a8d0b1ed`](https://github.com/vllm-project/vllm/commit/03a8d0b1ed) [#50487](https://github.com/vllm-project/vllm/pull/50487)
  [Model][Spec Decode] Tap the pre-norm AttnRes mixture as the Kimi K3 DFlash aux state (#50487)
  _Files: `tests/models/kimi_k3/test_aux_attn_res_stream.py`, `tests/models/kimi_k3/test_eagle3.py`, `vllm/envs.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-14** [`cdc4824a21`](https://github.com/vllm-project/vllm/commit/cdc4824a21) [#48684](https://github.com/vllm-project/vllm/pull/48684)
  [Misc] Remove `override_attention_dtype` (#48684)
  _Files: `vllm/config/model.py`, `vllm/engine/arg_utils.py`_
- **2026-08-14** [`1f7427bc0a`](https://github.com/vllm-project/vllm/commit/1f7427bc0a) [#52265](https://github.com/vllm-project/vllm/pull/52265)
  [UT][XPU] fix b12x UT (#52265)
  _Files: `tests/model_executor/kernels/test_b12x_mxfp8_linear.py`, `vllm/utils/flashinfer.py`_
- **2026-08-14** [`57bd0ed441`](https://github.com/vllm-project/vllm/commit/57bd0ed441) [#51704](https://github.com/vllm-project/vllm/pull/51704)
  [5/N][KV-Cache Layout Refactor] Backend-published KV packing via customize_spec (#51704)
  _Files: `tests/quantization/test_turboquant.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/test_kv_cache_spec_registry.py`, `tests/v1/worker/test_dsv4_packed_zeroer_geometry.py` _+14 more__
- **2026-08-14** [`63a9a5010a`](https://github.com/vllm-project/vllm/commit/63a9a5010a) [#52164](https://github.com/vllm-project/vllm/pull/52164)
  [Attention][DSA] Take the native decode path for MTP=3 on SM90 (#52164)
  _Files: `tests/kernels/attention/test_deepgemm_attention.py`, `tests/v1/attention/test_indexer_native_next_n.py`, `vllm/utils/deep_gemm.py`, `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-08-14** [`6adad08767`](https://github.com/vllm-project/vllm/commit/6adad08767) [#51655](https://github.com/vllm-project/vllm/pull/51655)
  Add Muse Glimmer model support (#51655)
  _Files: `examples/tool_chat_template_muse_glimmer.jinja`, `tests/models/registry.py`, `tests/models/utils.py`, `tests/tool_use/test_muse_glimmer.py` _+17 more__
- **2026-08-14** [`827a2af806`](https://github.com/vllm-project/vllm/commit/827a2af806) [#48666](https://github.com/vllm-project/vllm/pull/48666)
  [Kernel] Gemma-4 FA4 FP8 Kernel (#48666)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`, `vllm/model_executor/layers/attention/attention.py`, `vllm/platforms/interface.py`, `vllm/v1/attention/backend.py` _+4 more__
- **2026-08-13** [`b652dedd0c`](https://github.com/vllm-project/vllm/commit/b652dedd0c) [#52148](https://github.com/vllm-project/vllm/pull/52148)
  [Attention] Fix FlashInfer SM12x prefill with sinks (#52148)
  _Files: `tests/v1/attention/test_attention_backends.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-08-13** [`2e2ffd104b`](https://github.com/vllm-project/vllm/commit/2e2ffd104b) [#52210](https://github.com/vllm-project/vllm/pull/52210)
  [CI Failure] Fix CUDA wheel build for the Kimi K3 fused MLA kernel (#52210)
  _Files: `csrc/libtorch_stable/fused_kimi_k3_mla_key_concat_kv_cache_kernel.cu`_
- **2026-08-13** [`6014f9e672`](https://github.com/vllm-project/vllm/commit/6014f9e672) [#52079](https://github.com/vllm-project/vllm/pull/52079)
  [Kimi-K3] Add GEMM-RS for sequence parallelism (#52079)
  _Files: `.buildkite/test_areas/distributed.yaml`, `benchmarks/kernels/benchmark_kimi_k3_gemm_rs.py`, `tests/kernels/test_kimi_k3_gemm_rs.py`, `tests/models/kimi_k3/test_sequence_parallel.py` _+7 more__
- **2026-08-13** [`2d24355eb8`](https://github.com/vllm-project/vllm/commit/2d24355eb8) [#52030](https://github.com/vllm-project/vllm/pull/52030)
  [Bugfix] Fix packed GDN decode launch for large batch-head grids (#52030)
  _Files: `tests/kernels/test_fused_recurrent_packed_decode.py`, `vllm/third_party/flash_linear_attention/ops/fused_recurrent.py`_
- **2026-08-13** [`2ac1f683f1`](https://github.com/vllm-project/vllm/commit/2ac1f683f1) [#51256](https://github.com/vllm-project/vllm/pull/51256)
  [BugFix] Reserve the bonus query slot in DFlash scheduling budget (#51256)
  _Files: `tests/test_config.py`, `vllm/config/speculative.py`_
- **2026-08-13** [`5936bac7d7`](https://github.com/vllm-project/vllm/commit/5936bac7d7) [#51218](https://github.com/vllm-project/vllm/pull/51218)
  [Bugfix] Report FULL_ATTENTION for uniform-base UniformTypeKVCacheSpecs groups instead of UNKNOWN (#51218)
  _Files: `tests/v1/test_kv_cache_spec_registry.py`, `vllm/v1/kv_cache_interface.py`_
- **2026-08-12** [`fe889ac925`](https://github.com/vllm-project/vllm/commit/fe889ac925) [#51311](https://github.com/vllm-project/vllm/pull/51311)
  [K3 Perf] Flash kda out kernel for prefill, 1.1~1.4x kernel performance improvement (#51311)
  _Files: `vllm/models/kimi_k3/nvidia/kda.py`_
- **2026-08-12** [`aeece10c06`](https://github.com/vllm-project/vllm/commit/aeece10c06) [#51928](https://github.com/vllm-project/vllm/pull/51928)
  [Bugfix][XPU] Run GDN attention as eager break under breakable cudagraph (#51928)
  _Files: `vllm/_xpu_ops.py`_
- **2026-08-12** [`10b7766a90`](https://github.com/vllm-project/vllm/commit/10b7766a90) [#51913](https://github.com/vllm-project/vllm/pull/51913)
  [Attention] Move context_lens_tensor compute into GDN prefill path (#51913)
  _Files: `vllm/v1/attention/backends/gdn_attn.py`_
- **2026-08-12** [`f97e502969`](https://github.com/vllm-project/vllm/commit/f97e502969) [#51738](https://github.com/vllm-project/vllm/pull/51738)
  [Perf] Avoid more GPU<->CPU syncs on the model execution path (#51738)
  _Files: `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/diffusion_gemma.py`, `vllm/model_executor/models/gemma4_mm.py`, `vllm/model_executor/models/glm4_1v.py` _+11 more__
- **2026-08-11** [`1d2d83a07f`](https://github.com/vllm-project/vllm/commit/1d2d83a07f) [#49718](https://github.com/vllm-project/vllm/pull/49718)
  [Attention] Add FlashInfer XQA decode support on SM12x (#49718)
  _Files: `tests/kernels/attention/test_use_trtllm_attention.py`, `tests/v1/attention/test_attention_backends.py`, `vllm/utils/flashinfer.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-08-11** [`b2ab096017`](https://github.com/vllm-project/vllm/commit/b2ab096017) [#51857](https://github.com/vllm-project/vllm/pull/51857)
  [Docs] Fix broken autorefs cross-reference in TurboQuant v2 docstring (#51857)
  _Files: `vllm/v1/attention/ops/turboquant_soa/triton_turboquant_decode_v2.py`_
- **2026-08-11** [`cc668c5b72`](https://github.com/vllm-project/vllm/commit/cc668c5b72) [#51854](https://github.com/vllm-project/vllm/pull/51854)
  [CI][Bugfix][V1] Remove stale FlashAttention metadata arguments (#51854)
  _Files: `tests/v1/worker/test_gpu_autoregressive_speculator.py`_
- **2026-08-11** [`4f2f31b82e`](https://github.com/vllm-project/vllm/commit/4f2f31b82e) [#51363](https://github.com/vllm-project/vllm/pull/51363)
  [Bugfix][Attention] Forward per-head FP8 descales through FA4 (#51363)
  _Files: `vllm/vllm_flash_attn/flash_attn_interface.py`_
- **2026-08-11** [`e3fe212eaf`](https://github.com/vllm-project/vllm/commit/e3fe212eaf) [#51749](https://github.com/vllm-project/vllm/pull/51749)
  [Bugfix] Generalize KV block zeroing to `AttentionSpec` (#51749)
  _Files: `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/worker/test_kv_block_zeroer.py`, `vllm/v1/core/single_type_kv_cache_manager.py`, `vllm/v1/worker/utils.py`_
- **2026-08-11** [`513f83e7ec`](https://github.com/vllm-project/vllm/commit/513f83e7ec) [#51756](https://github.com/vllm-project/vllm/pull/51756)
  [Bugfix] Take the sliding window from the layer, not the KV cache group (#51756)
  _Files: `tests/v1/attention/test_group_sliding_window.py`, `tests/v1/e2e/general/test_correctness_sliding_window.py`, `vllm/v1/attention/backends/cpu_attn.py`, `vllm/v1/attention/backends/flash_attn.py`_
- **2026-08-11** [`6c95a641e9`](https://github.com/vllm-project/vllm/commit/6c95a641e9) [#49315](https://github.com/vllm-project/vllm/pull/49315)
  [2/N][Feat][Perf] Add new warmup infrastructure for JITs. Add predicate filtering for JIT warmup, and migrate Inkling FA4 (#49315)
  _Files: `tests/model_executor/test_jit_warmup.py`, `tests/models/inkling/test_fa4_rel_attention.py`, `tests/models/inkling/test_fa4_warmup.py`, `vllm/config/kernel.py` _+8 more__
- **2026-08-11** [`608c12473f`](https://github.com/vllm-project/vllm/commit/608c12473f) [#51733](https://github.com/vllm-project/vllm/pull/51733)
  [Attention] Fix MLA prefill workspace allocation size (#51733)
  _Files: `tests/distributed/test_dcp_direct_a2a_lse_reduce.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/attention/sparse_mla_attention.py`_
- **2026-08-11** [`c76a425278`](https://github.com/vllm-project/vllm/commit/c76a425278) [#51739](https://github.com/vllm-project/vllm/pull/51739)
  [Kernel] Optimize long-context MLA cache gathers (#51739)
  _Files: `.buildkite/test_areas/kernels.yaml`, `benchmarks/kernels/benchmark_cp_gather.py`, `csrc/libtorch_stable/cache_kernels.cu`, `tests/kernels/attention/test_cache.py` _+2 more__
- **2026-08-11** [`99e62b802c`](https://github.com/vllm-project/vllm/commit/99e62b802c) [#49519](https://github.com/vllm-project/vllm/pull/49519)
  [Bugfix][Model Loader] Defer post-load attention weight processing (#49519)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/layers/attention/__init__.py`, `vllm/model_executor/model_loader/reload/layerwise.py`, `vllm/model_executor/model_loader/utils.py`_
- **2026-08-11** [`1a1727330a`](https://github.com/vllm-project/vllm/commit/1a1727330a) [#50713](https://github.com/vllm-project/vllm/pull/50713)
  [CI] Solidify speculative decoding E2E coverage (#50713)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `tests/v1/e2e/spec_decode/acceptance_rates/dflash/test_dflash.py`, `tests/v1/e2e/spec_decode/acceptance_rates/dspark/test_dspark.py`, `tests/v1/e2e/spec_decode/acceptance_rates/mtp_other/test_medusa.py` _+14 more__
- **2026-08-10** [`c3cac8c63d`](https://github.com/vllm-project/vllm/commit/c3cac8c63d) [#49815](https://github.com/vllm-project/vllm/pull/49815)
  [Bugfix][MiMo] Apply vision attention sinks in the window attention path (#49815)
  _Files: `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/v1/attention/ops/triton_prefill_attention.py`_
- **2026-08-10** [`63ac04a61e`](https://github.com/vllm-project/vllm/commit/63ac04a61e) [#50484](https://github.com/vllm-project/vllm/pull/50484)
  [Kimi-K3] DCP support (#50484)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/attention/dcp_utils/dcp_direct_a2a_lse_reduce.cu`, `csrc/libtorch_stable/attention/dcp_utils/dcp_direct_common.cuh`, `csrc/libtorch_stable/attention/dcp_utils/dcp_direct_kv_gather.cu` _+15 more__
- **2026-08-10** [`d40c3e3c00`](https://github.com/vllm-project/vllm/commit/d40c3e3c00) [#50693](https://github.com/vllm-project/vllm/pull/50693)
  Fix DSpark warmup without sparse index buffer (#50693)
  _Files: `vllm/models/deepseek_v4/nvidia/flashmla.py`_

## MoE / Expert Parallel  (29 commits)

- **2026-08-17** [`7ea4b40954`](https://github.com/vllm-project/vllm/commit/7ea4b40954) [#52502](https://github.com/vllm-project/vllm/pull/52502)
  [Hardware][NVIDIA] Add GB10 fused-MoE fp8 tuning configs (E=256, E=512) (#52502)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=256,N=512,device_name=NVIDIA_GB10,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/fused_moe/configs/E=512,N=512,device_name=NVIDIA_GB10,dtype=fp8_w8a8,block_shape=[128,128].json`_
- **2026-08-17** [`967e104fad`](https://github.com/vllm-project/vllm/commit/967e104fad) [#52550](https://github.com/vllm-project/vllm/pull/52550)
  [Config] Unify indexer cache dtype under attention_config.indexer_kv_dtype (#52550)
  _Files: `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-DSpark-confidence-TP4.yaml`, `tests/evals/gsm8k/configs/moe-refactor/DeepSeek-V4-Flash-deepgemm-mega-moe.yaml`, `vllm/config/attention.py`, `vllm/models/deepseek_v4/attention.py` _+2 more__
- **2026-08-16** [`7d7b6f26f4`](https://github.com/vllm-project/vllm/commit/7d7b6f26f4) [#52221](https://github.com/vllm-project/vllm/pull/52221)
  [Refactor] Remove dead code for quantization (#52221)
  _Files: `tests/kernels/quantization/test_block_int8.py`, `vllm/model_executor/kernels/linear/base.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/auto_awq.py` _+10 more__
- **2026-08-15** [`ed0f4750f8`](https://github.com/vllm-project/vllm/commit/ed0f4750f8) [#52445](https://github.com/vllm-project/vllm/pull/52445)
  [Bugfix][Model] Kimi-K3 MegaMoE: pass situ_beta/situ_linear_beta to fp8_fp4_mega_moe (#52445)
  _Files: `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-14** [`81e81dac1f`](https://github.com/vllm-project/vllm/commit/81e81dac1f) [#52327](https://github.com/vllm-project/vllm/pull/52327)
  [CI] Shard MoE refactor B200 eval (#52327)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/moe-refactor/config-b200-shard-0.txt`, `tests/evals/gsm8k/configs/moe-refactor/config-b200-shard-1.txt`, `tests/evals/gsm8k/configs/moe-refactor/config-b200-shard-2.txt` _+1 more__
- **2026-08-14** [`925ea7e60f`](https://github.com/vllm-project/vllm/commit/925ea7e60f) [#50589](https://github.com/vllm-project/vllm/pull/50589)
  [CI][Test] Seed the DeepEP v2 MoE workers, not just the parent (#50589)
  _Files: `tests/kernels/moe/test_deepep_v2_moe.py`_
- **2026-08-14** [`83ded8d839`](https://github.com/vllm-project/vllm/commit/83ded8d839) [#52331](https://github.com/vllm-project/vllm/pull/52331)
  [Test][LoRA] Speed up the LoRA test job (#52331)
  _Files: `tests/lora/test_fused_moe_lora_kernel.py`, `tests/lora/test_layers.py`, `tests/lora/test_punica_ops.py`, `tests/lora/test_punica_ops_fp8.py`_
- **2026-08-14** [`bda4c3e8ee`](https://github.com/vllm-project/vllm/commit/bda4c3e8ee) [#51583](https://github.com/vllm-project/vllm/pull/51583)
  [CPU] Fold the MXFP4 block scale in 2 instructions instead of 4 (#51583)
  _Files: `csrc/cpu/sgl-kernels/vec.h`, `tests/kernels/moe/test_cpu_quant_fused_moe.py`_
- **2026-08-13** [`80d6d557f3`](https://github.com/vllm-project/vllm/commit/80d6d557f3) [#52147](https://github.com/vllm-project/vllm/pull/52147)
  Standardise weight tying on `ParallelLMHead.tie_weights` (#52147)
  _Files: `vllm/model_executor/models/arctic.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/bloom.py`, `vllm/model_executor/models/chameleon.py` _+52 more__
- **2026-08-13** [`8e1131e1d1`](https://github.com/vllm-project/vllm/commit/8e1131e1d1) [#52114](https://github.com/vllm-project/vllm/pull/52114)
  [Model] [Quantization] Add Ling hybrid MXFP4 routed experts support (#52114)
  _Files: `vllm/model_executor/models/bailing_moe_v3.py`, `vllm/model_executor/models/bailing_moe_v3_mtp.py`_
- **2026-08-13** [`399f97424e`](https://github.com/vllm-project/vllm/commit/399f97424e) [#50874](https://github.com/vllm-project/vllm/pull/50874)
  [Bugfix][R3] Size monolithic routing replay buffer for DP (#50874)
  _Files: `vllm/model_executor/layers/fused_moe/modular_kernel.py`, `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`_
- **2026-08-13** [`9a276d6375`](https://github.com/vllm-project/vllm/commit/9a276d6375) [#52003](https://github.com/vllm-project/vllm/pull/52003)
  [Mypy Fix] Mypy fix for "vllm/model_executor/models/[cC][dD]" (#52003)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/clip.py`, `vllm/model_executor/models/cohere2_moe.py`, `vllm/model_executor/models/cohere2_vision.py` _+20 more__
- **2026-08-13** [`61826c1c6f`](https://github.com/vllm-project/vllm/commit/61826c1c6f) [#51624](https://github.com/vllm-project/vllm/pull/51624)
  [Hardware][Power] Unqualized MoE Backend for Power (VSX) (#51624)
  _Files: `csrc/cpu/cpu_fused_moe.cpp`, `csrc/cpu/micro_gemm/cpu_micro_gemm_vsx.hpp`, `csrc/cpu/utils.hpp`, `tests/kernels/moe/test_cpu_fused_moe.py` _+2 more__
- **2026-08-12** [`23f360edaa`](https://github.com/vllm-project/vllm/commit/23f360edaa) [#52009](https://github.com/vllm-project/vllm/pull/52009)
  [CI Bug] Fix ci moe test (#52009)
  _Files: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-triton.yaml`_
- **2026-08-12** [`e62abc37d4`](https://github.com/vllm-project/vllm/commit/e62abc37d4) [#49139](https://github.com/vllm-project/vllm/pull/49139)
  [Bugfix][Kernel] Fix persistent top-k histogram reuse after short rows (#49139)
  _Files: `csrc/libtorch_stable/persistent_topk.cuh`, `tests/kernels/test_top_k_per_row.py`_
- **2026-08-12** [`e60f3c4c13`](https://github.com/vllm-project/vllm/commit/e60f3c4c13) [#46845](https://github.com/vllm-project/vllm/pull/46845)
  [Bugfix] Fix MiniMax-M3 compressed-tensors FP8 MoE SwiGLU params (#46845)
  _Files: `tests/quantization/test_compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w8a8_fp8.py`_
- **2026-08-12** [`4eef91c03c`](https://github.com/vllm-project/vllm/commit/4eef91c03c) [#51831](https://github.com/vllm-project/vllm/pull/51831)
  [Model] Support R3 capture with DeepGEMM MegaMoE (#51831)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-12** [`3ac9525507`](https://github.com/vllm-project/vllm/commit/3ac9525507) [#50074](https://github.com/vllm-project/vllm/pull/50074)
  [Bugfix][Quantization] Reuse online NVFP4 MoE kernel across reloads (#50074)
  _Files: `tests/quantization/test_online.py`, `vllm/model_executor/layers/quantization/online/nvfp4.py`_
- **2026-08-11** [`36f4630d89`](https://github.com/vllm-project/vllm/commit/36f4630d89) [#50727](https://github.com/vllm-project/vllm/pull/50727)
  [Bugfix][MoE] Fix fused block-scale orientation (#50727)
  _Files: `tests/kernels/moe/test_moe_weight_loading_padded.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`, `vllm/model_executor/models/qwen3_moe.py` _+1 more__
- **2026-08-11** [`52be12cfac`](https://github.com/vllm-project/vllm/commit/52be12cfac) [#50569](https://github.com/vllm-project/vllm/pull/50569)
  feat: allow shared expert overlapping for FlashInfer one-sided all-to-all (#50569)
  _Files: `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`_
- **2026-08-11** [`5b5eae2394`](https://github.com/vllm-project/vllm/commit/5b5eae2394) [#49444](https://github.com/vllm-project/vllm/pull/49444)
  [Misc] Enable test_silu_mul_fp8_quant_deep_gemm on XPU (#49444)
  _Files: `tests/kernels/moe/test_silu_mul_fp8_quant_deep_gemm.py`, `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`_
- **2026-08-11** [`0fb9897df1`](https://github.com/vllm-project/vllm/commit/0fb9897df1) [#51819](https://github.com/vllm-project/vllm/pull/51819)
  [Bugfix][MoE] Support GELU tanh in FlashInfer B12x MoE (#51819)
  _Files: `vllm/model_executor/layers/fused_moe/experts/flashinfer_b12x_moe.py`_
- **2026-08-11** [`dd7cc85f17`](https://github.com/vllm-project/vllm/commit/dd7cc85f17) [#51407](https://github.com/vllm-project/vllm/pull/51407)
  Add MoE output contract for MoE tail fusion (#51407)
  _Files: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`, `vllm/model_executor/layers/fused_moe/moe_output.py`_
- **2026-08-10** [`3e174bb73c`](https://github.com/vllm-project/vllm/commit/3e174bb73c) [#47352](https://github.com/vllm-project/vllm/pull/47352)
  [Model Runner V2][MTP] Share topk index buffer between draft steps (#47352)
  _Files: `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`, `vllm/v1/worker/gpu/spec_decode/mtp/speculator.py`_
- **2026-08-10** [`405bc86768`](https://github.com/vllm-project/vllm/commit/405bc86768) [#51507](https://github.com/vllm-project/vllm/pull/51507)
  [Perf] Launch the top-k/top-p Triton sampler kernel with 8 warps (#51507)
  _Files: `vllm/v1/sample/ops/topk_topp_triton.py`_
- **2026-08-10** [`8fea1d306f`](https://github.com/vllm-project/vllm/commit/8fea1d306f) [#43680](https://github.com/vllm-project/vllm/pull/43680)
  Fix uniform_random routing simulation to sample without replacement (#43680)
  _Files: `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`_
- **2026-08-10** [`ec21f61d82`](https://github.com/vllm-project/vllm/commit/ec21f61d82) [#51672](https://github.com/vllm-project/vllm/pull/51672)
  [Misc] Enable test_fused_moe_wn16 on XPU (#51672)
  _Files: `tests/kernels/moe/test_moe.py`_
- **2026-08-10** [`ba1cdcfcf0`](https://github.com/vllm-project/vllm/commit/ba1cdcfcf0) [#51265](https://github.com/vllm-project/vllm/pull/51265)
  `[Model][Quantization] Add Ling-3.0-flash-fp8 support` (#51265)
  _Files: `tests/quantization/test_quark.py`, `vllm/model_executor/layers/quantization/auto_awq.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/utils/quant_utils.py` _+2 more__
- **2026-08-10** [`3b4c86e489`](https://github.com/vllm-project/vllm/commit/3b4c86e489) [#51419](https://github.com/vllm-project/vllm/pull/51419)
  [Bugfix][Quantization] Fix fp32 weight scale for mxfp4 quantization and per-expert checkpoint mapping (#51419)
  _Files: `vllm/model_executor/layers/fused_moe/routed_experts.py`, `vllm/model_executor/layers/quantization/mxfp4.py`_

## CI / Build  (25 commits)

- **2026-08-16** [`6b0b850a8b`](https://github.com/vllm-project/vllm/commit/6b0b850a8b) [#52496](https://github.com/vllm-project/vllm/pull/52496)
  [CI] Fit small KV-offload evals within shared memory (#52496)
  _Files: `tests/evals/gsm8k/test_gsm8k_offloading.py`_
- **2026-08-15** [`d4801990a4`](https://github.com/vllm-project/vllm/commit/d4801990a4) [#51901](https://github.com/vllm-project/vllm/pull/51901)
  [CI/Build] Add warning for unsupported global PTX architecture requests in...  (#51901)
  _Files: `CMakeLists.txt`, `cmake/utils.cmake`, `docs/getting_started/installation/gpu.cuda.inc.md`, `tests/test_cmake_utils.py`_
- **2026-08-14** [`bb4b448f98`](https://github.com/vllm-project/vllm/commit/bb4b448f98) [#52326](https://github.com/vllm-project/vllm/pull/52326)
  [CI] Shard Humming H100 eval (#52326)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/humming/config-h100-shard-0.txt`, `tests/evals/gsm8k/configs/humming/config-h100-shard-1.txt`, `tests/evals/gsm8k/configs/humming/config-h100-shard-2.txt`_
- **2026-08-14** [`549cef0b0b`](https://github.com/vllm-project/vllm/commit/549cef0b0b) [#52322](https://github.com/vllm-project/vllm/pull/52322)
  [CI] Shard extended pooling model tests (#52322)
  _Files: `.buildkite/test_areas/models_language.yaml`_
- **2026-08-14** [`624999aae5`](https://github.com/vllm-project/vllm/commit/624999aae5) [#52138](https://github.com/vllm-project/vllm/pull/52138)
  [XPU]bump up vllm_xpu_kernels to 0.1.13.2 (#52138)
  _Files: `requirements/xpu.txt`_
- **2026-08-14** [`d4c24e6f5d`](https://github.com/vllm-project/vllm/commit/d4c24e6f5d) [#52252](https://github.com/vllm-project/vllm/pull/52252)
  [CI] Increase extended generation test timeout (#52252)
  _Files: `.buildkite/test_areas/models_language.yaml`_
- **2026-08-14** [`8e6d8e4f6a`](https://github.com/vllm-project/vllm/commit/8e6d8e4f6a) [#52108](https://github.com/vllm-project/vllm/pull/52108)
  [XPU][CI/Release][3/N] Add xpu wheel release to release pipeline (#52108)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/generate-and-upload-nightly-index.sh`, `.buildkite/scripts/generate-nightly-index.py`, `.buildkite/scripts/xpu/publish-triton-shim.sh` _+2 more__
- **2026-08-13** [`1c3633acaf`](https://github.com/vllm-project/vllm/commit/1c3633acaf) [#52127](https://github.com/vllm-project/vllm/pull/52127)
  [CI/Build][CPU] Shrink triton-cpu-build layer by dropping build artifacts (#52127)
  _Files: `docker/Dockerfile.cpu`_
- **2026-08-13** [`5658391af7`](https://github.com/vllm-project/vllm/commit/5658391af7) [#51882](https://github.com/vllm-project/vllm/pull/51882)
  Remove NIXL reinstall step (#51882)
  _Files: `docker/Dockerfile`, `requirements/kv_connectors.txt`_
- **2026-08-13** [`63344913a6`](https://github.com/vllm-project/vllm/commit/63344913a6) [#50513](https://github.com/vllm-project/vllm/pull/50513)
  [XPU] update UMD to 26.27 (#50513)
  _Files: `docker/Dockerfile.xpu`_
- **2026-08-12** [`7aa248fcfe`](https://github.com/vllm-project/vllm/commit/7aa248fcfe) [#51935](https://github.com/vllm-project/vllm/pull/51935)
  [XPU][CI/Release][2/N] add triton shim in xpu requirements (#51935)
  _Files: `.pre-commit-config.yaml`, `requirements/test/xpu.txt`, `requirements/xpu.txt`_
- **2026-08-12** [`10f9b5d74f`](https://github.com/vllm-project/vllm/commit/10f9b5d74f) [#51923](https://github.com/vllm-project/vllm/pull/51923)
  [CI/Release][XPU] fix workdir path for triton shim job (#51923)
  _Files: `.buildkite/scripts/xpu/publish-triton-shim.sh`_
- **2026-08-12** [`a53ad85913`](https://github.com/vllm-project/vllm/commit/a53ad85913) [#51905](https://github.com/vllm-project/vllm/pull/51905)
  [XPU][CI]Change to use global VLLM_DISABLE_COMPILE_CACHE=1 in Intel GPU CI (#51905)
  _Files: `.buildkite/intel_jobs/basic_correctness.yaml`, `.buildkite/intel_jobs/benchmarks_intel.yaml`, `.buildkite/intel_jobs/model_executor_intel.yaml`, `.buildkite/intel_jobs/model_runner_v2_intel.yaml` _+5 more__
- **2026-08-12** [`f4e9bb01de`](https://github.com/vllm-project/vllm/commit/f4e9bb01de) [#51759](https://github.com/vllm-project/vllm/pull/51759)
  [CI/Release][1/N][XPU] Publish XPU Triton shim index (#51759)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/xpu/publish-triton-shim.sh`_
- **2026-08-12** [`23f25aac14`](https://github.com/vllm-project/vllm/commit/23f25aac14) [#50804](https://github.com/vllm-project/vllm/pull/50804)
  [CI] Stabilize tensor IPC multiprocessing tests (#50804)
  _Files: `tests/v1/test_tensor_ipc_queue.py`_
- **2026-08-11** [`ca9c8cbd1b`](https://github.com/vllm-project/vllm/commit/ca9c8cbd1b) [#51832](https://github.com/vllm-project/vllm/pull/51832)
  [CI] Support partial torch requirement contexts (#51832)
  _Files: `use_existing_torch.py`_
- **2026-08-11** [`5b184f775a`](https://github.com/vllm-project/vllm/commit/5b184f775a) [#51308](https://github.com/vllm-project/vllm/pull/51308)
  connects vLLM Recipes with vLLM's native config-based deployment and benchmark (#51308)
  _Files: `docs/benchmarking/README.md`, `docs/configuration/serve_args.md`, `docs/deployment/docker.md`, `docs/models/hardware_supported_models/cpu.md` _+2 more__
- **2026-08-11** [`52c70b210c`](https://github.com/vllm-project/vllm/commit/52c70b210c) [#50826](https://github.com/vllm-project/vllm/pull/50826)
  [XPU] [Linear] enable torch linear backend for blockwise  gemm on xpu (#50826)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `vllm/model_executor/kernels/linear/__init__.py`_
- **2026-08-11** [`b76cf758db`](https://github.com/vllm-project/vllm/commit/b76cf758db) [#50831](https://github.com/vllm-project/vllm/pull/50831)
  [XPU] install xpu-manager for device monitor (#50831)
  _Files: `docker/Dockerfile.xpu`_
- **2026-08-10** [`3c6b2e9c08`](https://github.com/vllm-project/vllm/commit/3c6b2e9c08) [#51732](https://github.com/vllm-project/vllm/pull/51732)
  [CI] Add /ci cancel command (#51732)
  _Files: `.github/workflows/new_pr_bot.yml`, `.github/workflows/run-ci-command.yml`, `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-08-10** [`21c667aa64`](https://github.com/vllm-project/vllm/commit/21c667aa64) [#51184](https://github.com/vllm-project/vllm/pull/51184)
  [Docker] Cache test dependencies before vLLM install (#51184)
  _Files: `docker/Dockerfile`, `docs/assets/contributing/dockerfile-stages-dependency.png`, `docs/contributing/dockerfile/dockerfile.md`, `tools/pre_commit/update-dockerfile-graph.sh`_
- **2026-08-10** [`bd6536071c`](https://github.com/vllm-project/vllm/commit/bd6536071c) [#51213](https://github.com/vllm-project/vllm/pull/51213)
  [XPU][Test] Pin block size in test_multi_connector (#51213)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `tests/v1/kv_connector/unit/test_multi_connector.py`_
- **2026-08-10** [`789c4f905e`](https://github.com/vllm-project/vllm/commit/789c4f905e) [#51566](https://github.com/vllm-project/vllm/pull/51566)
  [CI] Bump CUTLASS DSL to 4.6.2 (#51566)
  _Files: `requirements/cuda.txt`_
- **2026-08-10** [`51562de5ab`](https://github.com/vllm-project/vllm/commit/51562de5ab) [#51604](https://github.com/vllm-project/vllm/pull/51604)
  [CI][XPU] Add VLLM_DISABLE_COMPILE_CACHE=1 for other random failed cases in Intel GPU CI (#51604)
  _Files: `.buildkite/intel_jobs/benchmarks_intel.yaml`, `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-08-10** [`d89ba6481b`](https://github.com/vllm-project/vllm/commit/d89ba6481b) [#50441](https://github.com/vllm-project/vllm/pull/50441)
  [XPU] bump up xpu kernel to v0.1.12.3 (#50441)
  _Files: `requirements/xpu.txt`_

## Multimodal  (22 commits)

- **2026-08-17** [`5fd7a88838`](https://github.com/vllm-project/vllm/commit/5fd7a88838) [#52578](https://github.com/vllm-project/vllm/pull/52578)
  [CI/Build] Fix accident pre-commit breakage due to concurrent merge (#52578)
  _Files: `tests/models/multimodal/pooling/test_colpali.py`_
- **2026-08-16** [`eee538d5da`](https://github.com/vllm-project/vllm/commit/eee538d5da) [#52482](https://github.com/vllm-project/vllm/pull/52482)
  [Bugfix][V1][Multimodal] Ignore stale same-step encoder cache evictions (#52482)
  _Files: `tests/v1/core/test_encoder_cache_manager.py`, `vllm/v1/core/encoder_cache_manager.py`_
- **2026-08-16** [`e3c1cb54fc`](https://github.com/vllm-project/vllm/commit/e3c1cb54fc) [#52417](https://github.com/vllm-project/vllm/pull/52417)
  [CI/Build] Avoid duplicate runner startup for multimodal test (#52417)
  _Files: `tests/models/multimodal/generation/test_phi4mm.py`, `tests/models/multimodal/generation/test_qwen2_vl.py`, `tests/models/multimodal/generation/vlm_utils/case_filtering.py`, `tests/models/multimodal/generation/vlm_utils/runners.py` _+1 more__
- **2026-08-16** [`84530eb235`](https://github.com/vllm-project/vllm/commit/84530eb235) [#52441](https://github.com/vllm-project/vllm/pull/52441)
  [Bugfix][Multimodal] Keep Gemma 4 video frame counts on CPU (#52441)
  _Files: `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-08-14** [`694db075f8`](https://github.com/vllm-project/vllm/commit/694db075f8) [#52323](https://github.com/vllm-project/vllm/pull/52323)
  [CI] Shard multimodal extended generation 2 (#52323)
  _Files: `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-08-14** [`66728feb1f`](https://github.com/vllm-project/vllm/commit/66728feb1f) [#49852](https://github.com/vllm-project/vllm/pull/49852)
  [MRV2][Multimodal] Enable encoder cuda graph for model runner v2 (#49852)
  _Files: `vllm/v1/worker/encoder_cudagraph.py`, `vllm/v1/worker/gpu/mm/encoder_runner.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/model_states/interface.py`_
- **2026-08-14** [`b8165e5e58`](https://github.com/vllm-project/vllm/commit/b8165e5e58) [#52261](https://github.com/vllm-project/vllm/pull/52261)
  [Frontend] Consolidate entrypoint exception handler (#52261)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/cohere/test_api_router.py`, `tests/entrypoints/serve/exception_handling/__init__.py`, `tests/entrypoints/serve/exception_handling/test_error_sanitization.py` _+27 more__
- **2026-08-13** [`96acd473a7`](https://github.com/vllm-project/vllm/commit/96acd473a7) [#52122](https://github.com/vllm-project/vllm/pull/52122)
  [Bugfix][MiniCPM-V] Fix AssertionError in get_dummy_mm_data when passing VideoDummyOptions to _get_dummy_images (#52122)
  _Files: `vllm/model_executor/models/minicpmv.py`_
- **2026-08-13** [`95c9144424`](https://github.com/vllm-project/vllm/commit/95c9144424) [#42662](https://github.com/vllm-project/vllm/pull/42662)
  [LoRA][Gemma4] Support vision tower LoRA (#42662)
  _Files: `.buildkite/test_areas/lora.yaml`, `docs/models/supported_models.md`, `tests/lora/conftest.py`, `tests/lora/test_gemma4_tp.py` _+6 more__
- **2026-08-13** [`37c3bdf5a7`](https://github.com/vllm-project/vllm/commit/37c3bdf5a7) [#50221](https://github.com/vllm-project/vllm/pull/50221)
  fix(security): enforce audio decode duration limit in NanoNemotronVL (#50221)
  _Files: `tests/models/multimodal/test_nano_nemotron_vl.py`, `vllm/model_executor/models/nano_nemotron_vl.py`_
- **2026-08-13** [`903da602f3`](https://github.com/vllm-project/vllm/commit/903da602f3) [#52134](https://github.com/vllm-project/vllm/pull/52134)
  [Docs] Fix `WhisperEncoderLayer.forward` docstring in `dots3_note` (#52134)
  _Files: `vllm/models/dots3_note/nvidia/audio_encoder.py`_
- **2026-08-13** [`8eb35c5217`](https://github.com/vllm-project/vllm/commit/8eb35c5217) [#52064](https://github.com/vllm-project/vllm/pull/52064)
  [CI] Mirror external test assets in vLLM S3 (#52064)
  _Files: `tests/entrypoints/multimodal/openai/chat_completion/test_video.py`, `tests/entrypoints/pooling/classify/test_online_vision.py`, `tests/evals/gsm8k/gsm8k_eval.py`, `tests/models/multimodal/pooling/test_jinavl_reranker.py` _+1 more__
- **2026-08-12** [`4c51ceb11b`](https://github.com/vllm-project/vllm/commit/4c51ceb11b) [#51139](https://github.com/vllm-project/vllm/pull/51139)
  [Bugfix][Multimodal] Invalidate retained PyNvVideoCodec decoder after failure (#51139)
  _Files: `tests/multimodal/assets/unsupported_8k_h264.mp4`, `tests/multimodal/test_video.py`, `vllm/multimodal/video.py`_
- **2026-08-12** [`86e2ab50aa`](https://github.com/vllm-project/vllm/commit/86e2ab50aa) [#51120](https://github.com/vllm-project/vllm/pull/51120)
  [Bugfix][Frontend] Return 400 for invalid PyNvVideoCodec video input (#51120)
  _Files: `tests/multimodal/media/test_video.py`, `tests/multimodal/test_video.py`, `vllm/multimodal/video.py`_
- **2026-08-12** [`6accb779a3`](https://github.com/vllm-project/vllm/commit/6accb779a3) [#51911](https://github.com/vllm-project/vllm/pull/51911)
  [CI] Add registry layer cache to x86 CPU image build (#51911)
  _Files: `.buildkite/image_build/image_build_cpu.sh`, `docker/Dockerfile.cpu`_
- **2026-08-12** [`3962042304`](https://github.com/vllm-project/vllm/commit/3962042304) [#46747](https://github.com/vllm-project/vllm/pull/46747)
  [Bugfix][V1][Multimodal] Recover from P0/P1 processor cache drift (#46747) (#46747)
  _Files: `rust/src/chat/tests/chat.rs`, `rust/src/engine-core-client/src/protocol/output.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py` _+9 more__
- **2026-08-11** [`3fb7bb46d6`](https://github.com/vllm-project/vllm/commit/3fb7bb46d6) [#51774](https://github.com/vllm-project/vllm/pull/51774)
  [Perf] Avoid repeated multimodal prompt update scans (#51774)
  _Files: `tests/multimodal/test_processing.py`, `vllm/multimodal/processing/processor.py`_
- **2026-08-11** [`dc5101fb1b`](https://github.com/vllm-project/vllm/commit/dc5101fb1b) [#51734](https://github.com/vllm-project/vllm/pull/51734)
  replace batch_norm to numerically identical without cudnn (#51734)
  _Files: `docs/design/mm_processing.md`, `tests/models/test_vision.py`, `vllm/model_executor/models/vision.py`_
- **2026-08-11** [`33584901ba`](https://github.com/vllm-project/vllm/commit/33584901ba) [#51478](https://github.com/vllm-project/vllm/pull/51478)
  [Frontend] Add content_parts to /inference/v1/generate for raw multim… (#51478)
  _Files: `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/inference/generate/convert.rs`, `rust/src/server/src/routes/inference/generate/types.rs`, `rust/src/server/src/routes/render.rs` _+3 more__
- **2026-08-10** [`8a9f9f762a`](https://github.com/vllm-project/vllm/commit/8a9f9f762a) [#51735](https://github.com/vllm-project/vllm/pull/51735)
  [CI] Parallelize release image publishing (#51735)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/publish-release-images.sh`_
- **2026-08-10** [`640a09086d`](https://github.com/vllm-project/vllm/commit/640a09086d) [#49948](https://github.com/vllm-project/vllm/pull/49948)
  Fix DoS via sample-rate forgery bypassing audio decode duration guard (#49948)
  _Files: `docs/usage/security.md`, `tests/multimodal/media/test_audio.py`, `vllm/entrypoints/speech_to_text/base/serving.py`, `vllm/envs.py` _+1 more__
- **2026-08-10** [`cf8f3a3bb2`](https://github.com/vllm-project/vllm/commit/cf8f3a3bb2) [#51657](https://github.com/vllm-project/vllm/pull/51657)
  [2/N] Harden Transformers modelling backend multi-modal path (#51657)
  _Files: `tests/models/transformers/test_backend.py`, `vllm/model_executor/models/transformers/base.py`, `vllm/model_executor/models/transformers/multimodal.py`_

## Models  (17 commits)

- **2026-08-16** [`83f591d7f6`](https://github.com/vllm-project/vllm/commit/83f591d7f6) [#51967](https://github.com/vllm-project/vllm/pull/51967)
  [Perf][DSV4] Optimize global top-k index kernel with compile-time constants (#51967)
  _Files: `vllm/models/deepseek_v4/common/ops/cache_utils.py`_
- **2026-08-16** [`836aac92ff`](https://github.com/vllm-project/vllm/commit/836aac92ff) [#52084](https://github.com/vllm-project/vllm/pull/52084)
  [Perf][DSV4] Optimize sparse top-k metadata kernels for higher prefill throughput (#52084)
  _Files: `vllm/models/deepseek_v4/common/ops/cache_utils.py`_
- **2026-08-14** [`103c419f04`](https://github.com/vllm-project/vllm/commit/103c419f04) [#52277](https://github.com/vllm-project/vllm/pull/52277)
  [Perf][Frontend] Vectorize Cohere binary embedding bit-packing (#52277)
  _Files: `tests/entrypoints/pooling/embed/test_protocol.py`, `vllm/entrypoints/pooling/embed/protocol.py`_
- **2026-08-14** [`c05d75aaa9`](https://github.com/vllm-project/vllm/commit/c05d75aaa9) [#50685](https://github.com/vllm-project/vllm/pull/50685)
  [Bugfix][Refactor] Keep Qwen3Next layer boundaries sequence parallel (#50685)
  _Files: `vllm/model_executor/models/interns2_mobius.py`, `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_next.py`, `vllm/model_executor/models/qwen3_next_mtp.py`_
- **2026-08-14** [`1be3628367`](https://github.com/vllm-project/vllm/commit/1be3628367) [#51674](https://github.com/vllm-project/vllm/pull/51674)
  [Kernel][Perf] Add fused CUDA post-conv MTP decode kernel for Qwen3.5 GDN (#51674)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/gdn/fused_gdn_decode_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+8 more__
- **2026-08-13** [`69d4c3a06b`](https://github.com/vllm-project/vllm/commit/69d4c3a06b) [#52091](https://github.com/vllm-project/vllm/pull/52091)
  Auto-ping Cohere on related issues (#52091)
  _Files: `.github/mergify.yml`, `.github/workflows/issue_autolabel.yml`_
- **2026-08-13** [`b245d8e73f`](https://github.com/vllm-project/vllm/commit/b245d8e73f) [#52173](https://github.com/vllm-project/vllm/pull/52173)
  Apply logit softcapping in Transformers modelling backend (#52173)
  _Files: `vllm/model_executor/models/transformers/causal.py`_
- **2026-08-13** [`b8baa31a28`](https://github.com/vllm-project/vllm/commit/b8baa31a28) [#49458](https://github.com/vllm-project/vllm/pull/49458)
  Hardware-agnostic model definition via HF transformer backend (1/N) (#49458)
  _Files: `tests/models/transformers/test_layer_registry.py`, `vllm/envs.py`, `vllm/model_executor/hw_agnostic/__init__.py`, `vllm/model_executor/hw_agnostic/custom_op.py` _+6 more__
- **2026-08-13** [`89c8401c8a`](https://github.com/vllm-project/vllm/commit/89c8401c8a) [#52037](https://github.com/vllm-project/vllm/pull/52037)
  [Model] Skip unused Jina V5 output layers (#52037)
  _Files: `vllm/model_executor/models/jina.py`_
- **2026-08-12** [`025d56a11e`](https://github.com/vllm-project/vllm/commit/025d56a11e) [#52035](https://github.com/vllm-project/vllm/pull/52035)
  [Build] Update DeepGEMM pin to deepseek-ai nv_dev tip (#52035)
  _Files: `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-08-12** [`b1b752042f`](https://github.com/vllm-project/vllm/commit/b1b752042f) [#51841](https://github.com/vllm-project/vllm/pull/51841)
  Avoid long-blocking H2D copies in ViT (#51841)
  _Files: `vllm/model_executor/models/qwen3_vl.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-08-11** [`be2e274ef5`](https://github.com/vllm-project/vllm/commit/be2e274ef5) [#51773](https://github.com/vllm-project/vllm/pull/51773)
  Fix docs on `main` (#51773)
  _Files: `vllm/model_executor/models/transformers/base.py`_
- **2026-08-11** [`65b7662d3f`](https://github.com/vllm-project/vllm/commit/65b7662d3f) [#51556](https://github.com/vllm-project/vllm/pull/51556)
  [Bugfix][Frontend] Report Cohere stop sequences correctly (#51556)
  _Files: `tests/entrypoints/cohere/test_serving_conversion.py`, `tests/entrypoints/cohere/test_serving_streaming.py`, `vllm/entrypoints/cohere/serving.py`_
- **2026-08-11** [`f1e921b6d6`](https://github.com/vllm-project/vllm/commit/f1e921b6d6) [#51144](https://github.com/vllm-project/vllm/pull/51144)
  [Rust Frontend] Support dynamic tools from developer messages (#51144)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/default/structural_tag.rs` _+24 more__
- **2026-08-11** [`b2506d62ae`](https://github.com/vllm-project/vllm/commit/b2506d62ae) [#51461](https://github.com/vllm-project/vllm/pull/51461)
  [MM][CG][BugFix] Fix Ernie-4.5-VL encoder CG postprocess for multi-path outputs (#51461)
  _Files: `vllm/model_executor/models/ernie45_vl.py`_
- **2026-08-10** [`8bcc916a98`](https://github.com/vllm-project/vllm/commit/8bcc916a98) [#51727](https://github.com/vllm-project/vllm/pull/51727)
  [Bugfix] Fix DeepSeek V4/3.2 tokenizer vocab size overcount crashing guided decoding (#51727)
  _Files: `vllm/tokenizers/deepseek_v32.py`, `vllm/tokenizers/deepseek_v4.py`_
- **2026-08-10** [`70b84f0bcb`](https://github.com/vllm-project/vllm/commit/70b84f0bcb) [#49797](https://github.com/vllm-project/vllm/pull/49797)
  Fix Gemma 4 for upcoming Transformers version (#49797)
  _Files: `tests/config/test_model_arch_config.py`, `tests/models/transformers/fusers/test_linear.py`, `vllm/config/model.py`, `vllm/config/model_arch.py` _+11 more__

## Serving / API  (16 commits)

- **2026-08-17** [`93550cc4cd`](https://github.com/vllm-project/vllm/commit/93550cc4cd) [#52309](https://github.com/vllm-project/vllm/pull/52309)
  [Frontend] Consolidate entrypoint middleware (#52309)
  _Files: `tests/entrypoints/serve/middleware/__init__.py`, `tests/entrypoints/serve/middleware/test_authentication_middleware.py`, `tests/entrypoints/serve/middleware/test_optional_middleware.py`, `vllm/entrypoints/launchers/__init__.py` _+10 more__
- **2026-08-17** [`a6a2a93f9b`](https://github.com/vllm-project/vllm/commit/a6a2a93f9b) [#52528](https://github.com/vllm-project/vllm/pull/52528)
  [Bugfix][Frontend] Guard remaining before-validators against non-object JSON bodies (#52528)
  _Files: `tests/entrypoints/unit_tests/test_non_object_body_validation.py`, `vllm/entrypoints/openai/completion/protocol.py`, `vllm/entrypoints/openai/responses/protocol.py`, `vllm/entrypoints/pooling/base/protocol.py` _+3 more__
- **2026-08-16** [`70aaec832b`](https://github.com/vllm-project/vllm/commit/70aaec832b) [#52246](https://github.com/vllm-project/vllm/pull/52246)
  [Bugfix][Anthropic] Return 4xx for client-caused errors in /v1/messages (#52246)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/serve/exception_handling/test_error_sanitization.py`, `vllm/entrypoints/anthropic/api_router.py`_
- **2026-08-15** [`42156466db`](https://github.com/vllm-project/vllm/commit/42156466db) [#52384](https://github.com/vllm-project/vllm/pull/52384)
  [Rust Frontend][gRPC] Preserve skip_special_tokens decoding option (#52384)
  _Files: `rust/proto/inference.proto`, `rust/src/server/src/grpc/convert.rs`_
- **2026-08-13** [`7553aac77b`](https://github.com/vllm-project/vllm/commit/7553aac77b) [#51906](https://github.com/vllm-project/vllm/pull/51906)
  [Frontend] Add routed-experts prompt offset (#51906)
  _Files: `tests/entrypoints/openai/completion/test_completion.py`, `tests/entrypoints/openai/test_return_routed_experts.py`, `tests/entrypoints/openai/test_stop_token_ids.py`, `tests/utils_/test_serial_utils.py` _+9 more__
- **2026-08-13** [`152c913a63`](https://github.com/vllm-project/vllm/commit/152c913a63) [#52098](https://github.com/vllm-project/vllm/pull/52098)
  [Frontend] Log output token IDs at DEBUG level (#52098)
  _Files: `tests/entrypoints/serve/utils/test_request_logger.py`, `vllm/entrypoints/openai/cli_args.py`, `vllm/entrypoints/serve/utils/request_logger.py`_
- **2026-08-13** [`d0ae25e2f2`](https://github.com/vllm-project/vllm/commit/d0ae25e2f2) [#52021](https://github.com/vllm-project/vllm/pull/52021)
  [Bugfix] Preserve Anthropic disable_parallel_tool_use (#52021)
  _Files: `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-08-13** [`7bc1660bd6`](https://github.com/vllm-project/vllm/commit/7bc1660bd6) [#51931](https://github.com/vllm-project/vllm/pull/51931)
  [Misc] Use VLLMValidationError in pooling input validation (#51931)
  _Files: `tests/entrypoints/pooling/basic/test_encode.py`, `tests/entrypoints/pooling/test_io_processor.py`, `vllm/entrypoints/pooling/base/io_processor.py`_
- **2026-08-12** [`6ea6c42659`](https://github.com/vllm-project/vllm/commit/6ea6c42659) [#51997](https://github.com/vllm-project/vllm/pull/51997)
  [Bugfix] Bound Anthropic stop sequences (#51997)
  _Files: `vllm/entrypoints/anthropic/protocol.py`_
- **2026-08-12** [`8151f2ad43`](https://github.com/vllm-project/vllm/commit/8151f2ad43) [#51999](https://github.com/vllm-project/vllm/pull/51999)
  [Docs] Warn that --api-key does not gate all endpoints (#51999)
  _Files: `docs/serving/online_serving/openai_compatible_server.md`, `vllm/entrypoints/openai/cli_args.py`_
- **2026-08-12** [`3ee2df3033`](https://github.com/vllm-project/vllm/commit/3ee2df3033) [#51463](https://github.com/vllm-project/vllm/pull/51463)
  [Frontend] Make `model` optional on all `/derender` request classes (#51463)
  _Files: `tests/entrypoints/scale_out/derender/test_derender.py`, `vllm/entrypoints/scale_out/derender/serving.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`_
- **2026-08-11** [`adc1200597`](https://github.com/vllm-project/vllm/commit/adc1200597) [#51753](https://github.com/vllm-project/vllm/pull/51753)
  [Misc] Use VLLMValidationError in scoring input validation (#51753)
  _Files: `tests/entrypoints/pooling/scoring/test_utils.py`, `vllm/entrypoints/pooling/scoring/utils.py`_
- **2026-08-11** [`48bada6ea4`](https://github.com/vllm-project/vllm/commit/48bada6ea4) [#51654](https://github.com/vllm-project/vllm/pull/51654)
  Fix chat completion 500 on non-object JSON bodies (#51654)
  _Files: `tests/entrypoints/openai/chat_completion/test_non_object_body_validation.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`_
- **2026-08-10** [`8977ea8895`](https://github.com/vllm-project/vllm/commit/8977ea8895) [#50333](https://github.com/vllm-project/vllm/pull/50333)
  [Perf] Skip detokenization in offline beam search (#50333)
  _Files: `vllm/entrypoints/generate/beam_search/offline.py`_
- **2026-08-10** [`635dd6aae6`](https://github.com/vllm-project/vllm/commit/635dd6aae6) [#51276](https://github.com/vllm-project/vllm/pull/51276)
  [Build][gRPC] Publish protobuf schemas to Buf (#51276)
  _Files: `.github/workflows/buf.yml`, `rust/proto/README.md`, `rust/proto/buf.md`, `rust/proto/buf.yaml`_
- **2026-08-10** [`ea3115e30b`](https://github.com/vllm-project/vllm/commit/ea3115e30b) [#51557](https://github.com/vllm-project/vllm/pull/51557)
  [CI] Stabilize DP supervisor lifecycle tests (#51557)
  _Files: `tests/entrypoints/openai/test_dp_supervisor.py`_

## Scheduler / Engine  (15 commits)

- **2026-08-16** [`41f12a0daf`](https://github.com/vllm-project/vllm/commit/41f12a0daf) [#52394](https://github.com/vllm-project/vllm/pull/52394)
  [Bugfix] Raise `VLLMValidationError` from structured output validators (#52394)
  _Files: `tests/entrypoints/llm/test_struct_output_generate.py`, `tests/v1/structured_output/test_validation.py`, `vllm/entrypoints/openai/engine/protocol.py`, `vllm/sampling_params.py` _+4 more__
- **2026-08-14** [`f473870ecf`](https://github.com/vllm-project/vllm/commit/f473870ecf) [#51316](https://github.com/vllm-project/vllm/pull/51316)
  [Rust Frontend][gRPC] Add RL lifecycle control (#51316)
  _Files: `docs/training/weight_transfer/README.md`, `docs/usage/security.md`, `rust/proto/control.proto`, `rust/src/engine-core-client/src/client.rs` _+13 more__
- **2026-08-14** [`b216db3ed0`](https://github.com/vllm-project/vllm/commit/b216db3ed0) [#51795](https://github.com/vllm-project/vllm/pull/51795)
  [Bugfix] Reject negative token ids as out-of-vocabulary (#51795)
  _Files: `tests/entrypoints/pooling/embed/test_online.py`, `vllm/v1/engine/input_processor.py`_
- **2026-08-13** [`64ca614fe4`](https://github.com/vllm-project/vllm/commit/64ca614fe4) [#47692](https://github.com/vllm-project/vllm/pull/47692)
  [Bugfix] Fix `--data-parallel-start-rank 0` being treated as unset in `create_engine_config` (#47692)
  _Files: `tests/v1/engine/test_engine_args.py`, `vllm/engine/arg_utils.py`_
- **2026-08-13** [`50ba4bc6b2`](https://github.com/vllm-project/vllm/commit/50ba4bc6b2) [#49577](https://github.com/vllm-project/vllm/pull/49577)
  [Feature] Mask Replay (#49577)
  _Files: `docs/training/sampling_mask.md`, `rust/src/engine-core-client/src/protocol/output.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py` _+20 more__
- **2026-08-13** [`7bbbf7c8e5`](https://github.com/vllm-project/vllm/commit/7bbbf7c8e5) [#51251](https://github.com/vllm-project/vllm/pull/51251)
  [Core] Configure custom encoder cache managers from VllmConfig (#51251)
  _Files: `vllm/config/ec_manager_config.py`, `vllm/engine/arg_utils.py`, `vllm/v1/core/encoder_cache_manager.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-12** [`8e958902ee`](https://github.com/vllm-project/vllm/commit/8e958902ee) [#51843](https://github.com/vllm-project/vllm/pull/51843)
  [Bugfix] Disable fine-grained prefix-cache hits for incompatible hybrid KV layouts (#51843)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-11** [`4988df2eb8`](https://github.com/vllm-project/vllm/commit/4988df2eb8) [#51726](https://github.com/vllm-project/vllm/pull/51726)
  [Config] Update default `_max_num_batched_tokens` from 8192 to 16384 (#51726)
  _Files: `tests/v1/engine/test_engine_args.py`, `vllm/engine/arg_utils.py`_
- **2026-08-11** [`b64a2708b0`](https://github.com/vllm-project/vllm/commit/b64a2708b0) [#51447](https://github.com/vllm-project/vllm/pull/51447)
  Bound generation inputs before expensive work (#51447)
  _Files: `rust/src/server/src/routes/openai/utils/types.rs`, `tests/test_request_input_bounds.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py` _+7 more__
- **2026-08-11** [`0914ed2e81`](https://github.com/vllm-project/vllm/commit/0914ed2e81) [#51725](https://github.com/vllm-project/vllm/pull/51725)
  [Perf] Adaptive budget for spec scheduled input tokens, ~60% better Kimi K3 DSpark TTFT (#51725)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `vllm/config/vllm.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-10** [`fa722b9f01`](https://github.com/vllm-project/vllm/commit/fa722b9f01) [#51178](https://github.com/vllm-project/vllm/pull/51178)
  [Rust Frontend][gRPC] Add explicit data-parallel rank routing (#51178)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/state.rs` _+15 more__
- **2026-08-10** [`3f142bd85e`](https://github.com/vllm-project/vllm/commit/3f142bd85e) [#51296](https://github.com/vllm-project/vllm/pull/51296)
  [Bugfix] Align deepseek v4 parser thinking default with tokenizer (#51296)
  _Files: `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/trace_builder.py`, `vllm/parser/deepseek_v4.py`_
- **2026-08-10** [`243c63baf5`](https://github.com/vllm-project/vllm/commit/243c63baf5) [#51603](https://github.com/vllm-project/vllm/pull/51603)
  [V1][Scheduler] Apply Mamba alignment before encoder caps (#51603)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-10** [`61c1dd0966`](https://github.com/vllm-project/vllm/commit/61c1dd0966) [#49579](https://github.com/vllm-project/vllm/pull/49579)
  [EC Connector] Call to EC Connector update_connector_output from scheduler (#49579)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-10** [`0820125ae9`](https://github.com/vllm-project/vllm/commit/0820125ae9) [#50528](https://github.com/vllm-project/vllm/pull/50528)
  [Bugfix][Parser] Emit REASONING_END for Inkling tool calls that follow no thinking block (#50528)
  _Files: `tests/parser/engine/test_engine.py`, `tests/parser/engine/test_inkling.py`, `vllm/parser/engine/streaming_parser_engine.py`, `vllm/parser/inkling.py`_

## Quantization  (12 commits)

- **2026-08-17** [`53e211d292`](https://github.com/vllm-project/vllm/commit/53e211d292) [#52570](https://github.com/vllm-project/vllm/pull/52570)
  [CI/Build] Reduce more duplicate runner startup in tests (#52570)
  _Files: `tests/models/language/pooling/test_colbert.py`, `tests/models/language/pooling/test_truncation_control.py`, `tests/models/multimodal/generation/test_whisper.py`, `tests/models/multimodal/pooling/test_clip.py` _+6 more__
- **2026-08-14** [`d87ef456ab`](https://github.com/vllm-project/vllm/commit/d87ef456ab) [#52328](https://github.com/vllm-project/vllm/pull/52328)
  [CI] Shard Quantization job into 4 parallel shards (≤30 min target) (#52328)
  _Files: `.buildkite/test_areas/quantization.yaml`_
- **2026-08-14** [`3c79b1a8bf`](https://github.com/vllm-project/vllm/commit/3c79b1a8bf) [#52016](https://github.com/vllm-project/vllm/pull/52016)
  [Kernel] Add B12X dense linear backends (#52016)
  _Files: `docs/features/quantization/b12x.md`, `setup.py`, `tests/kernels/quantization/test_block_fp8.py`, `tests/model_executor/kernels/test_b12x_mxfp4_linear.py` _+13 more__
- **2026-08-13** [`48825acc23`](https://github.com/vllm-project/vllm/commit/48825acc23) [#51793](https://github.com/vllm-project/vllm/pull/51793)
  [Quantization] Remove dead `QuantizationConfig.is_mxfp4_quant` (#51793)
  _Files: `vllm/model_executor/layers/quantization/base_config.py`, `vllm/model_executor/layers/quantization/mxfp4.py`, `vllm/model_executor/layers/quantization/quark/quark.py`, `vllm/models/deepseek_v4/quant_config.py`_
- **2026-08-12** [`19d61b1273`](https://github.com/vllm-project/vllm/commit/19d61b1273) [#51359](https://github.com/vllm-project/vllm/pull/51359)
  [Bugfix] Initialize DeepGemmQuantScaleFMT oracle lazily; bound QuantFP8 UE8M0 packed path to group_size 128 (#51359)
  _Files: `tests/kernels/quantization/test_fp8_quant_group.py`, `vllm/model_executor/layers/quantization/input_quant_fp8.py`, `vllm/utils/deep_gemm.py`_
- **2026-08-12** [`0fb168e6ee`](https://github.com/vllm-project/vllm/commit/0fb168e6ee) [#52007](https://github.com/vllm-project/vllm/pull/52007)
  [CI Bug] Fix ci qwen3.5 (#52007)
  _Files: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2.yaml`_
- **2026-08-12** [`8c011da6d0`](https://github.com/vllm-project/vllm/commit/8c011da6d0) [#50787](https://github.com/vllm-project/vllm/pull/50787)
  [XPU] Route block-quantized FP8 weights to the W8A8 kernel (#50787)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`_
- **2026-08-12** [`d462dee37d`](https://github.com/vllm-project/vllm/commit/d462dee37d) [#51872](https://github.com/vllm-project/vllm/pull/51872)
  [Bugfix][Triton] Make fp8_min/fp8_max constexpr in _quantize_pad_fp8_kernel (#51872)
  _Files: `vllm/kernels/triton/qkv_padded_fp8_quant.py`_
- **2026-08-11** [`90fd4a333f`](https://github.com/vllm-project/vllm/commit/90fd4a333f) [#51446](https://github.com/vllm-project/vllm/pull/51446)
  Preserve revision pins in secondary artifact loaders (#51446)
  _Files: `tests/config/test_model_arch_config.py`, `tests/test_quantization_revision_pin.py`, `tests/test_tensorizer_revision_pin.py`, `tests/transformers_utils/test_config.py` _+7 more__
- **2026-08-10** [`b22afe45ac`](https://github.com/vllm-project/vllm/commit/b22afe45ac) [#51148](https://github.com/vllm-project/vllm/pull/51148)
  [CPU] Enable GPTQ and AWQ quantization for s390x (#51148)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_vxe.hpp`, `csrc/cpu/torch_bindings.cpp`, `docs/getting_started/installation/cpu.md` _+1 more__
- **2026-08-10** [`7ce84b99ce`](https://github.com/vllm-project/vllm/commit/7ce84b99ce) [#51379](https://github.com/vllm-project/vllm/pull/51379)
  [CPU] Restore linear dispatch for small unquantized GEMMs (#51379)
  _Files: `vllm/model_executor/layers/utils.py`_
- **2026-08-10** [`751f2ccdd3`](https://github.com/vllm-project/vllm/commit/751f2ccdd3) [#47205](https://github.com/vllm-project/vllm/pull/47205)
  [Kernel][XPU] Tensor-descriptor operand loads for Triton W8A8 scaled_mm (#47205)
  _Files: `tests/kernels/quantization/test_triton_scaled_mm.py`, `vllm/_custom_ops.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/triton.py` _+1 more__

## Speculative Decoding  (11 commits)

- **2026-08-16** [`4d2a68d64d`](https://github.com/vllm-project/vllm/commit/4d2a68d64d) [#52436](https://github.com/vllm-project/vllm/pull/52436)
  [Bugfix][Spec Decode][Structured Output] DSpark: fix the grammar bitmask mapping when the draft budget is zero (#52436)
  _Files: `tests/v1/spec_decode/test_adaptive_verification.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/structured_outputs.py`_
- **2026-08-16** [`1b079c40ff`](https://github.com/vllm-project/vllm/commit/1b079c40ff) [#52311](https://github.com/vllm-project/vllm/pull/52311)
  [Bugfix][Model Runner V2][Spec Decode] Fix off-by-one in bad_words draft-prefix matching (#52311)
  _Files: `tests/v1/worker/test_gpu_bad_words.py`, `vllm/v1/worker/gpu/sample/bad_words.py`_
- **2026-08-16** [`6593754e61`](https://github.com/vllm-project/vllm/commit/6593754e61) [#52419](https://github.com/vllm-project/vllm/pull/52419)
  [Bugfix][Spec Decode] Keep EAGLE cache registration on the partial-hash-hit path (#52419)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `vllm/v1/core/kv_cache_coordinator.py`_
- **2026-08-15** [`7b544ecb52`](https://github.com/vllm-project/vllm/commit/7b544ecb52) [#49793](https://github.com/vllm-project/vllm/pull/49793)
  [Spec Decode][Perf] Fuse the MTP trailing all-reduce; local-argmax draft tokens (#49793)
  _Files: `vllm/models/deepseek_v32/nvidia/mtp.py`_
- **2026-08-13** [`51def7848a`](https://github.com/vllm-project/vllm/commit/51def7848a) [#52223](https://github.com/vllm-project/vllm/pull/52223)
  [Bugfix] Reapply 50869 (#52223)
  _Files: `vllm/config/speculative.py`_
- **2026-08-13** [`83d4c6196a`](https://github.com/vllm-project/vllm/commit/83d4c6196a) [#52171](https://github.com/vllm-project/vllm/pull/52171)
  [Bugfix] Declare SupportsEagle3 on KimiLinearForCausalLM (#52171)
  _Files: `tests/models/kimi_k3/test_eagle3.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-13** [`443fa5aca0`](https://github.com/vllm-project/vllm/commit/443fa5aca0) [#51611](https://github.com/vllm-project/vllm/pull/51611)
  [Doc] Fix stale rejection_sample_method and synthetic_acceptance_rate (#51611)
  _Files: `docs/features/speculative_decoding/README.md`_
- **2026-08-11** [`5af7c8dad7`](https://github.com/vllm-project/vllm/commit/5af7c8dad7) [#51812](https://github.com/vllm-project/vllm/pull/51812)
  [Bugfix] Align Qwen GDN gates with speculative tokens (#51812)
  _Files: `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-08-11** [`529d010351`](https://github.com/vllm-project/vllm/commit/529d010351) [#51500](https://github.com/vllm-project/vllm/pull/51500)
  [Doc] Fix typos in speculative decoding docs (#51500)
  _Files: `docs/features/speculative_decoding/README.md`, `docs/features/speculative_decoding/draft_model.md`, `docs/features/speculative_decoding/mlp.md`, `docs/features/speculative_decoding/n_gram.md`_
- **2026-08-10** [`355a338b8f`](https://github.com/vllm-project/vllm/commit/355a338b8f) [#51602](https://github.com/vllm-project/vllm/pull/51602)
  [BugFix][SpecDecode] Fix dspark parallel_drafting_token_id init bug (#51602)
  _Files: `vllm/v1/spec_decode/llm_base_proposer.py`_
- **2026-08-10** [`900d09f91a`](https://github.com/vllm-project/vllm/commit/900d09f91a) [#50734](https://github.com/vllm-project/vllm/pull/50734)
  [Bugfix][Model] Fix Qwen3.5 MTP for text-only checkpoints (#50734)
  _Files: `tests/models/test_qwen3_5_mtp_config.py`, `vllm/config/speculative.py`, `vllm/multimodal/registry.py`_

## KV Cache / Offload  (8 commits)

- **2026-08-13** [`f80b66f548`](https://github.com/vllm-project/vllm/commit/f80b66f548) [#50062](https://github.com/vllm-project/vllm/pull/50062)
  [Model Runner V2][Spec Decode] Add KV cache support for multi-layer MTP (#50062)
  _Files: `tests/config/test_speculative_draft_hf_overrides.py`, `tests/v1/core/test_scheduler.py`, `vllm/config/speculative.py`, `vllm/v1/core/kv_cache_coordinator.py` _+6 more__
- **2026-08-13** [`15227b934a`](https://github.com/vllm-project/vllm/commit/15227b934a) [#51614](https://github.com/vllm-project/vllm/pull/51614)
  [Bugfix][KV Offload] Emit self-describing CPU events at KV-group block granularity (#51614)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py`_
- **2026-08-13** [`f9a0f629bd`](https://github.com/vllm-project/vllm/commit/f9a0f629bd) [#51879](https://github.com/vllm-project/vllm/pull/51879)
  [KV Offload] Expose data-parallel topology to offloading backends (#51879)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `tests/v1/kv_offload/test_factory.py`, `tests/v1/kv_offload/test_file_mapper.py` _+4 more__
- **2026-08-11** [`61874f9842`](https://github.com/vllm-project/vllm/commit/61874f9842) [#51612](https://github.com/vllm-project/vllm/pull/51612)
  [4/N][KV-Cache Layout Refactor] Promote local KV cache specs via a class-changing replace helper (#51612)
  _Files: `vllm/v1/core/kv_cache_utils.py`, `vllm/v1/kv_cache_interface.py`_
- **2026-08-11** [`d648236199`](https://github.com/vllm-project/vllm/commit/d648236199) [#51806](https://github.com/vllm-project/vllm/pull/51806)
  [XPU][CI] Fix ExampleConnector KV cache device selection (#51806)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `tests/v1/kv_connector/unit/test_example_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`_
- **2026-08-11** [`0fec3d652b`](https://github.com/vllm-project/vllm/commit/0fec3d652b) [#51622](https://github.com/vllm-project/vllm/pull/51622)
  [Bugfix][KV Offload] Centralize shared mmap cleanup in CPU worker (#51622)
  _Files: `tests/v1/kv_offload/cpu/test_gpu_worker.py`, `vllm/v1/kv_offload/cpu/gpu_worker.py`_
- **2026-08-11** [`07443bea29`](https://github.com/vllm-project/vllm/commit/07443bea29) [#51482](https://github.com/vllm-project/vllm/pull/51482)
  [BugFix][Core] free_blocks: restore prepend (LIFO) reuse order when prefix caching is off (#51482)
  _Files: `vllm/v1/core/block_pool.py`_
- **2026-08-10** [`81840a172f`](https://github.com/vllm-project/vllm/commit/81840a172f) [#48414](https://github.com/vllm-project/vllm/pull/48414)
  [KV Connector] Canonical CPU layout for parallelism-agnostic KV offload (#48414)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `tests/v1/kv_offload/cpu/test_canonical_layout.py`, `tests/v1/kv_offload/cpu/test_gpu_worker.py`, `tests/v1/kv_offload/cpu/test_shared_offload_region.py` _+8 more__

## Disaggregation / PD  (7 commits)

- **2026-08-16** [`dc9ae4b8ac`](https://github.com/vllm-project/vllm/commit/dc9ae4b8ac) [#52372](https://github.com/vllm-project/vllm/pull/52372)
  [Bugfix][Mooncake] Reference GPU blocks for in-flight store jobs and key the store ledger by store_job_id (#52372)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py` _+3 more__
- **2026-08-15** [`fa9d67f782`](https://github.com/vllm-project/vllm/commit/fa9d67f782) [#49585](https://github.com/vllm-project/vllm/pull/49585)
  [EC Connector] Added Build Connector Worker Meta for EC Connector (#49585)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/v1/ec_connector/unit/test_ec_output_aggregator.py`, `tests/v1/ec_connector/unit/test_worker_ec_connector.py`, `tests/v1/executor/test_executor.py` _+12 more__
- **2026-08-14** [`653cc6faca`](https://github.com/vllm-project/vllm/commit/653cc6faca) [#50620](https://github.com/vllm-project/vllm/pull/50620)
  [Bugfix][NIXL] Include transfer mode (push/pull) in the compatibility hash (#50620)
  _Files: `docs/features/nixl_connector_compatibility.md`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+4 more__
- **2026-08-13** [`6e502b62cb`](https://github.com/vllm-project/vllm/commit/6e502b62cb) [#51813](https://github.com/vllm-project/vllm/pull/51813)
  fix and test EPLB balancedness calculation (#51813)
  _Files: `tests/distributed/test_eplb_algo.py`, `vllm/distributed/eplb/eplb_state.py`_
- **2026-08-11** [`0f2ea973be`](https://github.com/vllm-project/vllm/commit/0f2ea973be) [#51688](https://github.com/vllm-project/vllm/pull/51688)
  [KV Connector][Offloading] Keep per-layer KV registration when canonical_layout is requested (#51688)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`_
- **2026-08-11** [`f37dff22fc`](https://github.com/vllm-project/vllm/commit/f37dff22fc) [#51259](https://github.com/vllm-project/vllm/pull/51259)
  [Bugfix] Import each packed IPC export once on the consumer side (#51259)
  _Files: `vllm/distributed/weight_transfer/ipc_engine.py`, `vllm/distributed/weight_transfer/packed_tensor.py`_
- **2026-08-10** [`11ba93f364`](https://github.com/vllm-project/vllm/commit/11ba93f364) [#50999](https://github.com/vllm-project/vllm/pull/50999)
  [BugFix] Use file:// rendezvous for single-node executors to eliminate startup port races (#50999)
  _Files: `tests/distributed/test_file_store.py`, `vllm/distributed/parallel_state.py`, `vllm/utils/network_utils.py`, `vllm/v1/executor/multiproc_executor.py` _+2 more__

## Perf / Benchmark  (5 commits)

- **2026-08-17** [`0ff370b51c`](https://github.com/vllm-project/vllm/commit/0ff370b51c) [#52588](https://github.com/vllm-project/vllm/pull/52588)
  docs: fix incorrect --custom-skip-chat-template flag reference (#52588)
  _Files: `docs/benchmarking/cli.md`_
- **2026-08-13** [`63550515b4`](https://github.com/vllm-project/vllm/commit/63550515b4) [#45423](https://github.com/vllm-project/vllm/pull/45423)
  [Bugfix] Correct prompt lengths for timed_traces benchmark (#45423)
  _Files: `vllm/benchmarks/datasets/datasets.py`, `vllm/benchmarks/lib/endpoint_request_func.py`, `vllm/benchmarks/serve.py`_
- **2026-08-13** [`c4e969294e`](https://github.com/vllm-project/vllm/commit/c4e969294e) [#50534](https://github.com/vllm-project/vllm/pull/50534)
  [XPU] Add tuned Mamba SSU configs for Intel Arc Pro B70 (#50534)
  _Files: `benchmarks/kernels/benchmark_selective_state_update.py`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=128,dstate=256,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics,cache_dtype=float16.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=128,dstate=256,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics,cache_dtype=float32.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics,cache_dtype=float16.json` _+1 more__
- **2026-08-11** [`a367cdbca0`](https://github.com/vllm-project/vllm/commit/a367cdbca0) [#48789](https://github.com/vllm-project/vllm/pull/48789)
  [Profiler] Add minimal Triton Proton profiling backend (#48789)
  _Files: `docs/contributing/profiling.md`, `tests/v1/worker/test_gpu_profiler.py`, `vllm/benchmarks/latency.py`, `vllm/config/profiler.py` _+3 more__
- **2026-08-10** [`fac808b36f`](https://github.com/vllm-project/vllm/commit/fac808b36f) [#49436](https://github.com/vllm-project/vllm/pull/49436)
  [Perf][Hybrid] 3D-grid tiling of the state-copy Triton kernels (#49436)
  _Files: `tests/kernels/mamba/test_memcpy_u64_tiled.py`, `tests/kernels/mamba/test_precopy_mamba_align.py`, `vllm/v1/worker/mamba_utils.py`_

## Docs  (4 commits)

- **2026-08-17** [`502af5ed00`](https://github.com/vllm-project/vllm/commit/502af5ed00) [#50492](https://github.com/vllm-project/vllm/pull/50492)
  [Doc] Add MatrixHub as a model loading source (#50492)
  _Files: `docs/models/supported_models.md`_
- **2026-08-14** [`69e0e58da1`](https://github.com/vllm-project/vllm/commit/69e0e58da1) [#52289](https://github.com/vllm-project/vllm/pull/52289)
  [Doc] Update model support information (#52289)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`_
- **2026-08-12** [`9b3382685e`](https://github.com/vllm-project/vllm/commit/9b3382685e) [#51878](https://github.com/vllm-project/vllm/pull/51878)
  [Tools] vLLM Recipes conversion : support different data types variants and strategies (#51878)
  _Files: `tools/recipes/README.md`, `tools/recipes/recipe_json_to_vllm_config.py`_
- **2026-08-10** [`3a79957b62`](https://github.com/vllm-project/vllm/commit/3a79957b62) [#49353](https://github.com/vllm-project/vllm/pull/49353)
  [Doc] Add Crusoe Managed Inference deployment guide (#49353)
  _Files: `docs/deployment/frameworks/crusoe.md`_

## LoRA  (3 commits)

- **2026-08-15** [`ac2ae8798c`](https://github.com/vllm-project/vllm/commit/ac2ae8798c) [#45802](https://github.com/vllm-project/vllm/pull/45802)
  [Frontend]  Support count_reasoning_tokens in the Streaming Parser Engine (#45802)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/responses/test_serving_responses.py`, `tests/parser/engine/test_engine.py`, `tests/parser/engine/test_parser_engine.py` _+12 more__
- **2026-08-13** [`b908a21f9a`](https://github.com/vllm-project/vllm/commit/b908a21f9a) [#48215](https://github.com/vllm-project/vllm/pull/48215)
  [Model][LoRA] Add tower/connector LoRA support for Ultravox (#48215)
  _Files: `vllm/model_executor/models/ultravox.py`, `vllm/model_executor/models/whisper.py`_
- **2026-08-11** [`d8f840071e`](https://github.com/vllm-project/vllm/commit/d8f840071e) [#51780](https://github.com/vllm-project/vllm/pull/51780)
  [Model] Enable tower and connector LoRA for Keye (#51780)
  _Files: `vllm/model_executor/models/keye.py`_

## Compilation / CUDA Graph  (2 commits)

- **2026-08-13** [`71b0da7c4e`](https://github.com/vllm-project/vllm/commit/71b0da7c4e) [#52005](https://github.com/vllm-project/vllm/pull/52005)
  [Bugfix] Fix .../mrope.py::apply_interleaved_rope() when torch.compile is used in torch==2.13 (#52005)
  _Files: `tests/kernels/core/test_mrope.py`, `vllm/model_executor/layers/rotary_embedding/mrope.py`_
- **2026-08-11** [`87668ab69b`](https://github.com/vllm-project/vllm/commit/87668ab69b) [#51768](https://github.com/vllm-project/vllm/pull/51768)
  [Bugfix] Guard DeepSeek V4 MRV1 piecewise CUDA graphs (#51768)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_

---
_Generated 2026-08-17 08:55 UTC_