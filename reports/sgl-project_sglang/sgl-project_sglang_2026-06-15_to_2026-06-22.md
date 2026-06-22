# sgl-project/sglang — Weekly Change Report
**Period:** 2026-06-15 → 2026-06-22  |  **Total commits:** 314

## ✨ New Features This Week

- **2026-06-22** [#28670](https://github.com/sgl-project/sglang/pull/28670) — [JIT] Add kpool_topk_transform JIT kernel (#28670)
- **2026-06-22** [#28522](https://github.com/sgl-project/sglang/pull/28522) — [Docs] Add Anthropic-compatible API documentation (#28522)
- **2026-06-22** [#28774](https://github.com/sgl-project/sglang/pull/28774) — [docs][cookbook] Laguna-M.1 playground: add HiCache; refresh EP / DP-Attention notes (#28774)
- **2026-06-22** [#25820](https://github.com/sgl-project/sglang/pull/25820) — [NVIDIA] Support NVFP4 MoE for DeepSeek-V4 (#25820)
- **2026-06-22** [#28643](https://github.com/sgl-project/sglang/pull/28643) — [DOC] [NPU] Update features on Ascend NPU (#28643)
- **2026-06-21** [#28856](https://github.com/sgl-project/sglang/pull/28856) — [Spec] Enable FR-Spec in EAGLE draft-extend CUDA graph by sizing logits buffer from the draft head (#28856)
- **2026-06-21** [#28779](https://github.com/sgl-project/sglang/pull/28779) — [Feature] Add graceful scheduler shutdown; free hisparse host buffer on exit (#28779)
- **2026-06-21** [#28782](https://github.com/sgl-project/sglang/pull/28782) — [Spec] Support FlashInfer CUDA graph for EAGLE draft-extend (#28782)
- **2026-06-21** [#28816](https://github.com/sgl-project/sglang/pull/28816) — Add project rule: prefer msgspec.Struct over dataclasses (#28816)
- **2026-06-20** [#26312](https://github.com/sgl-project/sglang/pull/26312) — [mtp] add rejection sampling for speculative decoding (#26312)
- _…and 56 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-06-22** [`441ae9a5ae`](https://github.com/sgl-project/sglang/commit/441ae9a5ae) [#28885](https://github.com/sgl-project/sglang/pull/28885) — [Lint] Fix black formatting of DeepSeek-R1-MXFP4 MI35x tests (#28885)
- **2026-06-22** [`64e455d4bf`](https://github.com/sgl-project/sglang/commit/64e455d4bf) [#28886](https://github.com/sgl-project/sglang/pull/28886) — Fix lint break on main (#28886)
- **2026-06-22** [`e2540188ce`](https://github.com/sgl-project/sglang/commit/e2540188ce) [#27243](https://github.com/sgl-project/sglang/pull/27243) — [AMD] Clean up DeepSeek-R1-MXFP4 TP2/TP4 MLA GSM8K tests (#27243)
- **2026-06-22** [`fd7874d11b`](https://github.com/sgl-project/sglang/commit/fd7874d11b) [#28495](https://github.com/sgl-project/sglang/pull/28495) — [AMD] Register DP attention test (#28495)
- **2026-06-22** [`73448b0d70`](https://github.com/sgl-project/sglang/commit/73448b0d70) [#28871](https://github.com/sgl-project/sglang/pull/28871) — [AMD] Temporarily disable deepseek V4 in AMD PR test (#28871)
- **2026-06-21** [`a4d0ff3def`](https://github.com/sgl-project/sglang/commit/a4d0ff3def) [#28829](https://github.com/sgl-project/sglang/pull/28829) — [misc] Make NaN-logit sanitization opt-in (default off) (#28829)
- **2026-06-21** [`2552b860a3`](https://github.com/sgl-project/sglang/commit/2552b860a3) [#28337](https://github.com/sgl-project/sglang/pull/28337) — [AMD][bugfix] Place TBO cuda-graph num_token_non_padded buffer on model devices (#28337)
- **2026-06-20** [`95fb1ef697`](https://github.com/sgl-project/sglang/commit/95fb1ef697) [#28810](https://github.com/sgl-project/sglang/pull/28810) — [CI] Remove deprecated test/srt legacy CI setup (#28810)
- **2026-06-20** [`d6d06cdc17`](https://github.com/sgl-project/sglang/commit/d6d06cdc17) [#28074](https://github.com/sgl-project/sglang/pull/28074) — [AMD] Fix no-op dtype cast in _topk_ids_logical_to_physical_dynamic on HIP (#28074)
- **2026-06-20** [`47cad39f34`](https://github.com/sgl-project/sglang/commit/47cad39f34) [#28722](https://github.com/sgl-project/sglang/pull/28722) — [AMD] Optimize o_proj gemm and attn output rope performance (#28722)
- **2026-06-20** [`1115373668`](https://github.com/sgl-project/sglang/commit/1115373668) [#28244](https://github.com/sgl-project/sglang/pull/28244) — [AMD] Fix garbled unquantized Qwen3-30B-A3B output on ROCm/aiter where the aiter CK fused-MoE falls back to Triton with pre-shuffled weights (#28244)
- **2026-06-20** [`653f6735a0`](https://github.com/sgl-project/sglang/commit/653f6735a0) [#28611](https://github.com/sgl-project/sglang/pull/28611) — [AMD] add nightly kv_canary JIT benchmark suite (#28611)
- **2026-06-19** [`871ed0dc0c`](https://github.com/sgl-project/sglang/commit/871ed0dc0c) [#28751](https://github.com/sgl-project/sglang/pull/28751) — Revert "ci: add 4-GPU mi35x runner and rebalance off the saturated 8-GPU pool" (#28751)
- **2026-06-19** [`420004827c`](https://github.com/sgl-project/sglang/commit/420004827c) [#28736](https://github.com/sgl-project/sglang/pull/28736) — [AMD] register 3 tests to stage-b-test-1-gpu-large-amd (batch-6) (#28736)
- **2026-06-19** [`13aab2fc06`](https://github.com/sgl-project/sglang/commit/13aab2fc06) [#28745](https://github.com/sgl-project/sglang/pull/28745) — ci: add 4-GPU mi35x runner and rebalance off the saturated 8-GPU pool (#28745)
- **2026-06-19** [`7c505c2927`](https://github.com/sgl-project/sglang/commit/7c505c2927) [#28357](https://github.com/sgl-project/sglang/pull/28357) — [AMD] fix(jit): port kv_canary write/verify/plan kernels to ROCm (#28357)
- **2026-06-19** [`c436a8161a`](https://github.com/sgl-project/sglang/commit/c436a8161a) [#26639](https://github.com/sgl-project/sglang/pull/26639) — [AMD] Enable HiSparse on ROCm (#26639)
- **2026-06-19** [`3af991fb3e`](https://github.com/sgl-project/sglang/commit/3af991fb3e) [#28173](https://github.com/sgl-project/sglang/pull/28173) — [AMD] Make breakable CUDA graph run on ROCm/HIP (#28173)
- **2026-06-19** [`9bb9d17e1a`](https://github.com/sgl-project/sglang/commit/9bb9d17e1a) [#28682](https://github.com/sgl-project/sglang/pull/28682) — [Spec] Unify speculative grammar token-accept path in decode processing (#28682)
- **2026-06-19** [`24d15dd92e`](https://github.com/sgl-project/sglang/commit/24d15dd92e) [#28541](https://github.com/sgl-project/sglang/pull/28541) — [AMD][DSV4] fix nonetype issue when enabling hicache (#28541)
- **2026-06-19** [`fac11f3bc1`](https://github.com/sgl-project/sglang/commit/fac11f3bc1) [#25094](https://github.com/sgl-project/sglang/pull/25094) — [AMD] Document Mori XGMI for Single-Node PD Disaggregation (#25094)
- **2026-06-19** [`4d94e9471a`](https://github.com/sgl-project/sglang/commit/4d94e9471a) [#28226](https://github.com/sgl-project/sglang/pull/28226) — [AMD] Relax allreduce-fusion residual accuracy tolerance to 1 bf16 ULP (#28226)
- **2026-06-19** [`b36360dc5b`](https://github.com/sgl-project/sglang/commit/b36360dc5b) [#27382](https://github.com/sgl-project/sglang/pull/27382) — [AMD][Perf] Split-KV flash-decode attention for EAGLE target-verify (Triton backend) (#27382)
- **2026-06-18** [`62ab09a478`](https://github.com/sgl-project/sglang/commit/62ab09a478) [#28558](https://github.com/sgl-project/sglang/pull/28558) — [AMD] register 2 spec tests to stage-b-test-1-gpu-large-amd (batch-5) (#28558)
- **2026-06-18** [`c1067f88d6`](https://github.com/sgl-project/sglang/commit/c1067f88d6) [#27793](https://github.com/sgl-project/sglang/pull/27793) — [AMD][Perf] Tune extend attention block sizes for gfx950 (head_dim > 128) (#27793)
- **2026-06-18** [`9fc9d37f6d`](https://github.com/sgl-project/sglang/commit/9fc9d37f6d) [#24082](https://github.com/sgl-project/sglang/pull/24082) — Fix spec decoding with grammar in disagg (#24082)
- **2026-06-18** [`27a374eaef`](https://github.com/sgl-project/sglang/commit/27a374eaef) [#28678](https://github.com/sgl-project/sglang/pull/28678) — [AMD][CI] Use non-gated Qwen3-8B for MI35x disaggregation tests (#28678)
- **2026-06-18** [`6309fb9abb`](https://github.com/sgl-project/sglang/commit/6309fb9abb) [#28378](https://github.com/sgl-project/sglang/pull/28378) — [AMD] Fix Always mask padded topk_ids on HIP to prevent garbage MoE routing (DeepSeek-R1-MXFP4 accuracy regression) (#28378)
- **2026-06-18** [`5d1949152d`](https://github.com/sgl-project/sglang/commit/5d1949152d) [#28458](https://github.com/sgl-project/sglang/pull/28458) — [AMD] ci: add extra-a 1-gpu-large tier (fp8kv-triton, streaming-session, spec-standalone) (#28458)
- **2026-06-18** [`0e5a66dca4`](https://github.com/sgl-project/sglang/commit/0e5a66dca4) [#27837](https://github.com/sgl-project/sglang/pull/27837) — [AMD] Register 3 JIT kernel unit tests for AMD CI (#27837)
- **2026-06-17** [`3e97c9239f`](https://github.com/sgl-project/sglang/commit/3e97c9239f) [#28556](https://github.com/sgl-project/sglang/pull/28556) — chore: bump sgl-kernel version to 0.4.4 (#28556)
- **2026-06-17** [`f5b041622b`](https://github.com/sgl-project/sglang/commit/f5b041622b) [#28520](https://github.com/sgl-project/sglang/pull/28520) — [AMD] Fix deepseek-v4 mtp accept length issue (#28520)
- **2026-06-17** [`9b8c41171a`](https://github.com/sgl-project/sglang/commit/9b8c41171a) [#28473](https://github.com/sgl-project/sglang/pull/28473) — [AMD] Fall back to layer_first layout for kernel write-back on ROCm (#28473)
- **2026-06-17** [`21a95333d4`](https://github.com/sgl-project/sglang/commit/21a95333d4) [#27798](https://github.com/sgl-project/sglang/pull/27798) — [AMD] Add transpose_scale arg for o_proj to fix GLM accuracy issue (#27798)
- **2026-06-17** [`7256ee9871`](https://github.com/sgl-project/sglang/commit/7256ee9871) [#27815](https://github.com/sgl-project/sglang/pull/27815) — [AMD] Update test_aiter_allgather_amd.py data types alignment between benchmark aiter and custom all-reduce kernel (#27815)
- **2026-06-17** [`c01f62e341`](https://github.com/sgl-project/sglang/commit/c01f62e341) [#28486](https://github.com/sgl-project/sglang/pull/28486) — [bugfix] guard NVIDIA SM-capability checks with is_cuda() for AMD/ROCm (#28486)
- **2026-06-17** [`a2aa51c818`](https://github.com/sgl-project/sglang/commit/a2aa51c818) [#28344](https://github.com/sgl-project/sglang/pull/28344) — [AMD] register 4 2-gpu tests to stage-b-test-2-gpu-large-amd (#28344)
- **2026-06-17** [`66ac385f52`](https://github.com/sgl-project/sglang/commit/66ac385f52) [#28469](https://github.com/sgl-project/sglang/pull/28469) — fix(moe): MoRI EP init_mori_op missing BF16 dispatch branch (#28469)
- **2026-06-17** [`0d651e653b`](https://github.com/sgl-project/sglang/commit/0d651e653b) [#28423](https://github.com/sgl-project/sglang/pull/28423) — [AMD] Update v4 amd cookbook (#28423)
- **2026-06-17** [`37ef295c78`](https://github.com/sgl-project/sglang/commit/37ef295c78) [#28216](https://github.com/sgl-project/sglang/pull/28216) — [AMD] Feat/dp moe reduce scatter (#28216)
- **2026-06-16** [`a362ba9da3`](https://github.com/sgl-project/sglang/commit/a362ba9da3) [#27928](https://github.com/sgl-project/sglang/pull/27928) — [AMD] Feat: Add prefill context parallel support for deepseek v4 unified kv attention (#27928)
- **2026-06-16** [`149fabcca7`](https://github.com/sgl-project/sglang/commit/149fabcca7) [#27636](https://github.com/sgl-project/sglang/pull/27636) — [AMD] Fuse sigmoid + mul into single Triton kernel for shared expert gating (#27636)
- **2026-06-16** [`102392df5b`](https://github.com/sgl-project/sglang/commit/102392df5b) [#28404](https://github.com/sgl-project/sglang/pull/28404) — [AMD][Fix] Skip EPLB topk remap when global server args are unset (#28404)
- **2026-06-16** [`0fc2bc4a8b`](https://github.com/sgl-project/sglang/commit/0fc2bc4a8b) [#28290](https://github.com/sgl-project/sglang/pull/28290) — [AMD] Test DeepSeek V4 FlashMLA backend variants nightly (#28290)
- **2026-06-16** [`72d962be88`](https://github.com/sgl-project/sglang/commit/72d962be88) [#27947](https://github.com/sgl-project/sglang/pull/27947) — [AMD] Fix jit-kernel-unit-test-amd: activation.cuh ROCm build + per_token CUDA-only (R165) (#27947)
- **2026-06-16** [`800aaefc9e`](https://github.com/sgl-project/sglang/commit/800aaefc9e) [#28392](https://github.com/sgl-project/sglang/pull/28392) — [AMD] Annotate ATOM source for imported v4 unified attention kernels (#28392)
- **2026-06-16** [`ed9024e09f`](https://github.com/sgl-project/sglang/commit/ed9024e09f) [#28360](https://github.com/sgl-project/sglang/pull/28360) — [AMD] Fix AITER Scout workflow permissions (#28360)
- **2026-06-16** [`448af67a98`](https://github.com/sgl-project/sglang/commit/448af67a98) [#28368](https://github.com/sgl-project/sglang/pull/28368) — ci: run AMD and NPU PR tests on PRs not targeting main (#28368)
- **2026-06-16** [`2dd449ce5e`](https://github.com/sgl-project/sglang/commit/2dd449ce5e) [#27765](https://github.com/sgl-project/sglang/pull/27765) — [AMD-miles] add amd-miles daily docker build workflow (#27765)
- **2026-06-15** [`19e85868f6`](https://github.com/sgl-project/sglang/commit/19e85868f6) [#28313](https://github.com/sgl-project/sglang/pull/28313) — [AMD] Point AITER scout at amd/aiter-ci (#28313)
- **2026-06-15** [`c4ec39a785`](https://github.com/sgl-project/sglang/commit/c4ec39a785) [#28265](https://github.com/sgl-project/sglang/pull/28265) — [AMD] refactor sparse MLA decode kernel for Deepseek V4 triton backend (#28265)
- **2026-06-15** [`da12f36629`](https://github.com/sgl-project/sglang/commit/da12f36629) [#28275](https://github.com/sgl-project/sglang/pull/28275) — [AMD] Refactor unified_kv attention metadata to data class and fuse c4/128 out_loc (#28275)
- **2026-06-15** [`9864059e2b`](https://github.com/sgl-project/sglang/commit/9864059e2b) [#28249](https://github.com/sgl-project/sglang/pull/28249) — [AMD] Update AITER commit (#28249)
- **2026-06-15** [`19c78552dc`](https://github.com/sgl-project/sglang/commit/19c78552dc) [#28263](https://github.com/sgl-project/sglang/pull/28263) — [AMD] Restrict CI image fallback to versioned tags (#28263)
- **2026-06-15** [`63df86f5e7`](https://github.com/sgl-project/sglang/commit/63df86f5e7) [#22985](https://github.com/sgl-project/sglang/pull/22985) — [AMD] Skip eplb bookkeeping and topk remap when EPLB is not in use on mori-ep / HIP (#22985) (#28188)
- **2026-06-15** [`c127ba6483`](https://github.com/sgl-project/sglang/commit/c127ba6483) [#28214](https://github.com/sgl-project/sglang/pull/28214) — [AMD] ci: fix scheduled AMD runs startup failure when calling extra-a suite (#28214)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-06-22 |
| [#16565](https://github.com/sgl-project/sglang/issues/16565) | [Roadmap][Feature] Support Moore Threads (MUSA) GPU | mthreads | 2026-06-22 |
| [#27252](https://github.com/sgl-project/sglang/issues/27252) | [Roadmap]Prefill Context Parallel Refactor | — | 2026-06-22 |
| [#28631](https://github.com/sgl-project/sglang/issues/28631) | [Feature] Cross-backend KV transfer QoS — plumb request priority to P→ | — | 2026-06-22 |
| [#22949](https://github.com/sgl-project/sglang/issues/22949) | Development Roadmap (2026 Q2) | — | 2026-06-22 |
| [#28873](https://github.com/sgl-project/sglang/issues/28873) | [Bug] EAGLE speculative decoding crashes with Mooncake L3 HiCache in s | — | 2026-06-22 |
| [#27574](https://github.com/sgl-project/sglang/issues/27574) | [Agentic Inference] Programmatic KV Cache for Agentic Workloads | high priority | 2026-06-22 |
| [#28866](https://github.com/sgl-project/sglang/issues/28866) | [Parity with CUDA SGLang] DeepSeekv4 Pro not be spamming dozen of env  | — | 2026-06-22 |
| [#28851](https://github.com/sgl-project/sglang/issues/28851) | [Bug] MultiNode Disagg MI355X AMD DeepSeekv4 Pro Accuracy Issues  GSM8 | — | 2026-06-21 |
| [#28852](https://github.com/sgl-project/sglang/issues/28852) | Support MiniMax-M3-MXFP8 on H200 with fallback/dequant path | — | 2026-06-21 |
| [#26751](https://github.com/sgl-project/sglang/issues/26751) | [Bug] Gemma-4 mm: single non-RGB image crashes vision tower and kills  | — | 2026-06-21 |
| [#28826](https://github.com/sgl-project/sglang/issues/28826) | [Bug] GLM-5.2-FP8 DSA fails to load: GlmMoeDsaConfig attribute_map ove | — | 2026-06-21 |
| [#28815](https://github.com/sgl-project/sglang/issues/28815) | Speculative EAGLE verify: greedy/HIP branch missing TP broadcast -> ra | — | 2026-06-21 |
| [#28771](https://github.com/sgl-project/sglang/issues/28771) | EAGLE speculative decoding accept_length continuously degrades over ti | — | 2026-06-20 |
| [#28685](https://github.com/sgl-project/sglang/issues/28685) | [Bug] GLM-5.2-FP8 (DeepSeek-V3.2 / DSA block-fp8) produces wrong outpu | — | 2026-06-19 |
| [#27951](https://github.com/sgl-project/sglang/issues/27951) | [Bug] --moe-runner-backend flashinfer_cutlass + FP8 weights crashes wi | — | 2026-06-19 |
| [#28673](https://github.com/sgl-project/sglang/issues/28673) | [Bug] : MiMoV2 (FP8 over MXFP4) fails to load: KeyError: 'model.layers | — | 2026-06-19 |
| [#28141](https://github.com/sgl-project/sglang/issues/28141) | [Bug] DeepSeek-V4-Flash on ROCm MI350X fails during weight loading: `M | — | 2026-06-19 |
| [#27937](https://github.com/sgl-project/sglang/issues/27937) | [Failure Tracker] PR Test (AMD) | — | 2026-06-19 |
| [#28490](https://github.com/sgl-project/sglang/issues/28490) | [RFC][NPU][DLLM] Add fused tracker and coreset kernels for LLaDA2 Join | — | 2026-06-19 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 59 |
| Other | 36 |
| Multimodal | 34 |
| MoE / Expert Parallel | 28 |
| Prefill / Decode Disaggregation | 20 |
| Docs / Examples | 18 |
| Triton / Kernels | 17 |
| Quantization | 17 |
| Speculative Decoding | 16 |
| ROCm / AMD | 16 |
| Scheduler / Batching | 14 |
| Tensor / Data Parallel | 13 |
| KV Cache / Memory | 13 |
| Models | 5 |
| CI / Build | 4 |
| Serving / API | 3 |
| Structured Output | 1 |

## Attention / FlashInfer  (59 commits)

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
- **2026-06-21** [`8e890391f5`](https://github.com/sgl-project/sglang/commit/8e890391f5) [#28782](https://github.com/sgl-project/sglang/pull/28782)
  [Spec] Support FlashInfer CUDA graph for EAGLE draft-extend (#28782)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-06-21** [`7942d546d1`](https://github.com/sgl-project/sglang/commit/7942d546d1) [#28841](https://github.com/sgl-project/sglang/pull/28841)
  Revert "[Spec] Split init_backends; account draft weights in --mem-fraction-static" (#28841)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/model_runner.py` _+8 more__
- **2026-06-21** [`a51d56d948`](https://github.com/sgl-project/sglang/commit/a51d56d948) [#28838](https://github.com/sgl-project/sglang/pull/28838)
  CI: Pin flash-attn-4 for diffusion CI consistency (#28838)
  _Files: `python/pyproject.toml`_
- **2026-06-21** [`9691a29fe0`](https://github.com/sgl-project/sglang/commit/9691a29fe0) [#28683](https://github.com/sgl-project/sglang/pull/28683)
  [Spec] Split init_backends; account draft weights in --mem-fraction-static (#28683)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/model_runner.py` _+8 more__
- **2026-06-20** [`fe428dd845`](https://github.com/sgl-project/sglang/commit/fe428dd845) [#28807](https://github.com/sgl-project/sglang/pull/28807)
  Clean up startup log noise (#28807)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`_
- **2026-06-20** [`1109acc24b`](https://github.com/sgl-project/sglang/commit/1109acc24b) [#28319](https://github.com/sgl-project/sglang/pull/28319)
  [diffusion] optimize: shard hunyuan text tokens under sp (#28319)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/hunyuanvideo.py`_
- **2026-06-19** [`420004827c`](https://github.com/sgl-project/sglang/commit/420004827c) [#28736](https://github.com/sgl-project/sglang/pull/28736)
  [AMD] register 3 tests to stage-b-test-1-gpu-large-amd (batch-6) (#28736)
  _Files: `test/registered/attention/test_normal_decode_set_metadata.py`, `test/registered/lora/test_lora_update.py`, `test/registered/unit/spec/test_resolve_swa_kv_pool.py`_
- **2026-06-19** [`856b0dc74b`](https://github.com/sgl-project/sglang/commit/856b0dc74b) [#28739](https://github.com/sgl-project/sglang/pull/28739)
  refactor(runner): move kernel warmup into the shared runner lifecycle (warmup()) (#28739)
  _Files: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/__init__.py`, `python/sglang/srt/model_executor/runner/base_runner.py` _+12 more__
- **2026-06-19** [`c436a8161a`](https://github.com/sgl-project/sglang/commit/c436a8161a) [#26639](https://github.com/sgl-project/sglang/pull/26639)
  [AMD] Enable HiSparse on ROCm (#26639)
  _Files: `python/sglang/jit_kernel/csrc/hisparse.cuh`, `python/sglang/srt/arg_groups/hisparse_hook.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/managers/hisparse_coordinator.py` _+8 more__
- **2026-06-19** [`3af991fb3e`](https://github.com/sgl-project/sglang/commit/3af991fb3e) [#28173](https://github.com/sgl-project/sglang/pull/28173)
  [AMD] Make breakable CUDA graph run on ROCm/HIP (#28173)
  _Files: `docs_new/docs/advanced_features/breakable_cuda_graph.mdx`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/model_executor/runner_backend/breakable_cuda_graph_backend.py` _+4 more__
- **2026-06-19** [`1c6331cbd6`](https://github.com/sgl-project/sglang/commit/1c6331cbd6) [#28384](https://github.com/sgl-project/sglang/pull/28384)
  refactor(runner): rename runner replay/load/can_run for the shared surface (#28384)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/forward_batch_info.py` _+16 more__
- **2026-06-19** [`b36360dc5b`](https://github.com/sgl-project/sglang/commit/b36360dc5b) [#27382](https://github.com/sgl-project/sglang/pull/27382)
  [AMD][Perf] Split-KV flash-decode attention for EAGLE target-verify (Triton backend) (#27382)
  _Files: `benchmark/kernels/verify_splitkv_triton/bench_verify_splitkv.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/attention/triton_ops/verify_splitkv.py` _+1 more__
- **2026-06-19** [`ea407df4b0`](https://github.com/sgl-project/sglang/commit/ea407df4b0) [#28346](https://github.com/sgl-project/sglang/pull/28346)
  Use Flashinfer allreduce fusion for MNNVL allreduce for Nemotron (#28346)
  _Files: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py`, `python/sglang/srt/models/nemotron_h_utils.py`, `python/sglang/srt/server_args.py`_
- **2026-06-18** [`c1067f88d6`](https://github.com/sgl-project/sglang/commit/c1067f88d6) [#27793](https://github.com/sgl-project/sglang/pull/27793)
  [AMD][Perf] Tune extend attention block sizes for gfx950 (head_dim > 128) (#27793)
  _Files: `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`, `test/registered/attention/test_triton_attention_kernels.py`_
- **2026-06-18** [`2411737244`](https://github.com/sgl-project/sglang/commit/2411737244) [#28579](https://github.com/sgl-project/sglang/pull/28579)
  [spec decoding] fully overlap spec decoding for hybrid linear attention backend (#28579)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`_
- **2026-06-18** [`cf0afe3223`](https://github.com/sgl-project/sglang/commit/cf0afe3223) [#28642](https://github.com/sgl-project/sglang/pull/28642)
  [FA]Add lost params in fa varlen func (#28642)
  _Files: `python/sglang/jit_kernel/flash_attention.py`_
- **2026-06-18** [`97e3b8998d`](https://github.com/sgl-project/sglang/commit/97e3b8998d) [#28649](https://github.com/sgl-project/sglang/pull/28649)
  Pass quant_config to attention gate projection (#28649)
  _Files: `python/sglang/srt/models/laguna.py`_
- **2026-06-18** [`bb9d31f22d`](https://github.com/sgl-project/sglang/commit/bb9d31f22d) [#28635](https://github.com/sgl-project/sglang/pull/28635)
  [NPU] Add head_dim=256 to _can_use_tnd whitelist (#28635)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-06-18** [`fa71064147`](https://github.com/sgl-project/sglang/commit/fa71064147) [#28559](https://github.com/sgl-project/sglang/pull/28559)
  fix: speculative draft worker clobbering target attention backend (#28559)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v2.py`_
- **2026-06-18** [`3f66873304`](https://github.com/sgl-project/sglang/commit/3f66873304) [#28590](https://github.com/sgl-project/sglang/pull/28590)
  [Docs] DeepSeek-V4 cookbook: drop --disable-flashinfer-autotune from GB300 Flash low-latency (#28590)
  _Files: `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-06-18** [`0188c54fbe`](https://github.com/sgl-project/sglang/commit/0188c54fbe) [#28595](https://github.com/sgl-project/sglang/pull/28595)
  [FA3] Add unit test for only_qv (NoPE) KV decode path (#28595)
  _Files: `test/registered/jit/test_flash_attention_3_only_qv.py`_
- **2026-06-18** [`8d4a22c5af`](https://github.com/sgl-project/sglang/commit/8d4a22c5af) [#28201](https://github.com/sgl-project/sglang/pull/28201)
  [Docs] Add fp8 kv cache for tokenspeed mla docs (#28201)
  _Files: `docs_new/src/snippets/autoregressive/kimi-k25-deployment.jsx`, `docs_new/src/snippets/autoregressive/kimi-k26-deployment.jsx`, `docs_new/src/snippets/autoregressive/kimi-k27-code-deployment.jsx`_
- **2026-06-18** [`3340f4e3da`](https://github.com/sgl-project/sglang/commit/3340f4e3da) [#28185](https://github.com/sgl-project/sglang/pull/28185)
  [GDN][KDA][mem_cache] int8 checkpoint pool for the linear-attn prefix cache (#28185)
  _Files: `benchmark/bench_linear_attention/bench_int8_checkpoint_reuse.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/managers/scheduler_components/pool_stats_observer.py` _+6 more__
- **2026-06-18** [`9888b7b42b`](https://github.com/sgl-project/sglang/commit/9888b7b42b) [#28578](https://github.com/sgl-project/sglang/pull/28578)
  [misc] Trim dead code in trtllm_mha page-table backend; reuse eager page-table buffer (#28578)
  _Files: `python/sglang/srt/layers/attention/triton_ops/trtllm_mha_page_table.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `test/registered/attention/test_trtllm_mha_page_table.py`_
- **2026-06-17** [`d773b49e5b`](https://github.com/sgl-project/sglang/commit/d773b49e5b) [#28553](https://github.com/sgl-project/sglang/pull/28553)
  Fix MXFP8 FlashInfer CUTLASS scale selection (#28553)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`_
- **2026-06-17** [`5ea0d1d093`](https://github.com/sgl-project/sglang/commit/5ea0d1d093) [#27471](https://github.com/sgl-project/sglang/pull/27471)
  add dflash gemma4 support (#27471)
  _Files: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `test/registered/spec/test_gemma4_dflash_31b_extra.py`_
- **2026-06-17** [`cd60c4edd0`](https://github.com/sgl-project/sglang/commit/cd60c4edd0) [#28106](https://github.com/sgl-project/sglang/pull/28106)
  [attn backend] Make seq_lens_cpu optional in trtllm_mha backend (#28106)
  _Files: `python/sglang/srt/layers/attention/triton_ops/trtllm_mha_page_table.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `test/registered/attention/test_trtllm_mha_page_table.py`_
- **2026-06-17** [`3b5aae278e`](https://github.com/sgl-project/sglang/commit/3b5aae278e) [#28221](https://github.com/sgl-project/sglang/pull/28221)
  Fix EagleDraftExtendInput missing kv_indptr crash with triton/DP attention (#28221)
  _Files: `python/sglang/srt/speculative/eagle_info.py`_
- **2026-06-17** [`4b817f5d7f`](https://github.com/sgl-project/sglang/commit/4b817f5d7f) [#28394](https://github.com/sgl-project/sglang/pull/28394)
  Upgrade fa3 hash (#28394)
  _Files: `python/sglang/jit_kernel/flash_attention.py`, `python/sglang/jit_kernel/flash_attention_v3.py`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/csrc/flash_extension.cc` _+2 more__
- **2026-06-17** [`f5b041622b`](https://github.com/sgl-project/sglang/commit/f5b041622b) [#28520](https://github.com/sgl-project/sglang/pull/28520)
  [AMD] Fix deepseek-v4 mtp accept length issue (#28520)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `test/registered/amd/test_deepseek_v4_pro_fp4_mtp.py`_
- **2026-06-17** [`735a256f98`](https://github.com/sgl-project/sglang/commit/735a256f98) [#28176](https://github.com/sgl-project/sglang/pull/28176)
  [diffusion] feat: use LocalAttention for mistral3 encoder (#28176)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/mistral_3.py`_
- **2026-06-17** [`dad890fff1`](https://github.com/sgl-project/sglang/commit/dad890fff1) [#27066](https://github.com/sgl-project/sglang/pull/27066)
  [diffusion] perf: shard text when using sp in flux.1/2 (#27066)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py`_
- **2026-06-17** [`21a95333d4`](https://github.com/sgl-project/sglang/commit/21a95333d4) [#27798](https://github.com/sgl-project/sglang/pull/27798)
  [AMD] Add transpose_scale arg for o_proj to fix GLM accuracy issue (#27798)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`_
- **2026-06-17** [`8fd1694dd2`](https://github.com/sgl-project/sglang/commit/8fd1694dd2) [#27277](https://github.com/sgl-project/sglang/pull/27277)
  Deepseek v4: support mixed dtype compression states (#27277)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/c128_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4_v2.cuh`, `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/environ.py` _+5 more__
- **2026-06-17** [`d0e974f40b`](https://github.com/sgl-project/sglang/commit/d0e974f40b) [#28436](https://github.com/sgl-project/sglang/pull/28436)
  [NPU] Use use_dsa to dispatch Ascend DSA attention (#28436)
  _Files: `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`_
- **2026-06-17** [`a2aa51c818`](https://github.com/sgl-project/sglang/commit/a2aa51c818) [#28344](https://github.com/sgl-project/sglang/pull/28344)
  [AMD] register 4 2-gpu tests to stage-b-test-2-gpu-large-amd (#28344)
  _Files: `test/registered/attention/test_gemma4_swa_triton_oob_regression.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_full.py`, `test/registered/rl/test_patch_torch.py`, `test/registered/scheduler/test_load_snapshot_server.py`_
- **2026-06-17** [`b8a73bfba0`](https://github.com/sgl-project/sglang/commit/b8a73bfba0) [#28333](https://github.com/sgl-project/sglang/pull/28333)
  Call Flashinfer `mm_fp8` for per-tensor FP8 GEMMs on SM100 (#28333)
  _Files: `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-06-17** [`224b1dc775`](https://github.com/sgl-project/sglang/commit/224b1dc775) [#25768](https://github.com/sgl-project/sglang/pull/25768)
  [NPU]Replace ascend vision attn operator (#25768)
  _Files: `python/sglang/srt/layers/attention/vision.py`_
- **2026-06-16** [`9b4432fe18`](https://github.com/sgl-project/sglang/commit/9b4432fe18) [#28446](https://github.com/sgl-project/sglang/pull/28446)
  [HiCache]Asymmetric pool support direct backend (#28446)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/server_args.py`, `test/registered/jit/test_kvcacheio_asymmetric.py`, `test/registered/models_e2e/test_mimo_v2.py` _+2 more__
- **2026-06-16** [`a362ba9da3`](https://github.com/sgl-project/sglang/commit/a362ba9da3) [#27928](https://github.com/sgl-project/sglang/pull/27928)
  [AMD] Feat: Add prefill context parallel support for deepseek v4 unified kv attention (#27928)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/amd/test_deepseek_v4_pro_fp4_cp.py`_
- **2026-06-16** [`0fc2bc4a8b`](https://github.com/sgl-project/sglang/commit/0fc2bc4a8b) [#28290](https://github.com/sgl-project/sglang/pull/28290)
  [AMD] Test DeepSeek V4 FlashMLA backend variants nightly (#28290)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `test/registered/amd/test_deepseek_v4_flash_fp4.py`, `test/registered/amd/test_deepseek_v4_flash_fp8.py`, `test/registered/amd/test_deepseek_v4_pro_fp4.py` _+1 more__
- **2026-06-16** [`800aaefc9e`](https://github.com/sgl-project/sglang/commit/800aaefc9e) [#28392](https://github.com/sgl-project/sglang/pull/28392)
  [AMD] Annotate ATOM source for imported v4 unified attention kernels (#28392)
  _Files: `python/sglang/srt/layers/attention/dsv4/unified_kv_kernels/paged_decode.py`, `python/sglang/srt/layers/attention/dsv4/unified_kv_kernels/paged_decode_indices.py`, `python/sglang/srt/layers/attention/dsv4/unified_kv_kernels/paged_prefill.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`_
- **2026-06-16** [`32685874f3`](https://github.com/sgl-project/sglang/commit/32685874f3) [#23402](https://github.com/sgl-project/sglang/pull/23402)
  Reenable MNNVL backend for FlashInfer allreduce fusion (#23402)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/server_args.py` _+3 more__
- **2026-06-16** [`063ab89ac1`](https://github.com/sgl-project/sglang/commit/063ab89ac1) [#26471](https://github.com/sgl-project/sglang/pull/26471)
  DeepSeek-V4 Online Compress support MTP (#26471)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/c128_online_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/online_c128_mtp.cuh`, `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/jit_kernel/dsv4/online_c128_mtp.py` _+8 more__
- **2026-06-16** [`b3be2e7402`](https://github.com/sgl-project/sglang/commit/b3be2e7402) [#27954](https://github.com/sgl-project/sglang/pull/27954)
  [dsv4] Pad MLA decode q-heads to 64 (not full n_heads) for FlashMLA head64 kernel (#27954)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-06-15** [`81dcb00673`](https://github.com/sgl-project/sglang/commit/81dcb00673) [#28241](https://github.com/sgl-project/sglang/pull/28241)
  [Spec v2] Use decode kernel for TRT-LLM MHA draft extend (#28241)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-06-15** [`4ed698a491`](https://github.com/sgl-project/sglang/commit/4ed698a491) [#27343](https://github.com/sgl-project/sglang/pull/27343)
  fix(fa3): no NaN embeddings with fa_skip_kv_cache under piecewise CUDA graph (#27343)
  _Files: `python/sglang/srt/compilation/compiler_interface.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/prefill_only/test_fa_skip_kv_cache_piecewise_nan.py`_
- **2026-06-15** [`20f4272109`](https://github.com/sgl-project/sglang/commit/20f4272109) [#28073](https://github.com/sgl-project/sglang/pull/28073)
  fix: Fix DSR1 perf regression due to unnecessarily falling back to triton gemm (#28073)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/model_loader/utils.py`, `test/registered/unit/layers/quantization/test_flashinfer_trtllm_fp8_fallback.py`_
- **2026-06-15** [`09e9c4fde3`](https://github.com/sgl-project/sglang/commit/09e9c4fde3) [#28118](https://github.com/sgl-project/sglang/pull/28118)
  【bugfix】The NPU's forward_dsa_prepare_npu also needs special handling for is_nextn (#28118)
  _Files: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`_
- **2026-06-15** [`3df6e2f968`](https://github.com/sgl-project/sglang/commit/3df6e2f968) [#28223](https://github.com/sgl-project/sglang/pull/28223)
  [NPU] Add MiMo-V2-Flash manual testcases (#28223)
  _Files: `python/sglang/test/ascend/test_ascend_utils.py`, `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py`_
- **2026-06-15** [`c4ec39a785`](https://github.com/sgl-project/sglang/commit/c4ec39a785) [#28265](https://github.com/sgl-project/sglang/pull/28265)
  [AMD] refactor sparse MLA decode kernel for Deepseek V4 triton backend (#28265)
  _Files: `python/sglang/srt/layers/attention/nsa/triton_decode/triton_mla_kernels_decode_common.py`, `python/sglang/srt/layers/attention/nsa/triton_decode/triton_mla_kernels_decode_dsv4.py`, `python/sglang/srt/layers/attention/nsa/triton_decode/triton_mla_kernels_decode_fused.py`, `python/sglang/srt/layers/attention/nsa/triton_decode/triton_mla_kernels_decode_optimized.py` _+1 more__
- **2026-06-15** [`da12f36629`](https://github.com/sgl-project/sglang/commit/da12f36629) [#28275](https://github.com/sgl-project/sglang/pull/28275)
  [AMD] Refactor unified_kv attention metadata to data class and fuse c4/128 out_loc (#28275)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`, `python/sglang/srt/layers/attention/dsv4/unified_kv_kernels/env_gate.py`_
- **2026-06-15** [`1a66059c4e`](https://github.com/sgl-project/sglang/commit/1a66059c4e) [#28192](https://github.com/sgl-project/sglang/pull/28192)
  [Spec] Restore index_share_for_mtp_iteration in EAGLE V2 draft worker (#28192)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/standalone_worker_v2.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_draft_runner.py`_

## Other  (36 commits)

- **2026-06-22** [`886b96621d`](https://github.com/sgl-project/sglang/commit/886b96621d) [#28830](https://github.com/sgl-project/sglang/pull/28830)
  Migrate more server args to annotated style (#28830)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/test_server_args_cli_metadata.py`_
- **2026-06-21** [`c9488241e9`](https://github.com/sgl-project/sglang/commit/c9488241e9) [#28814](https://github.com/sgl-project/sglang/pull/28814)
  [Refactor] Auto-derive CLI args from dataclass fields to eliminate duplication (#28814)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/server_args.py`_
- **2026-06-21** [`d331fdd2ba`](https://github.com/sgl-project/sglang/commit/d331fdd2ba) [#28816](https://github.com/sgl-project/sglang/pull/28816)
  Add project rule: prefer msgspec.Struct over dataclasses (#28816)
  _Files: `.claude/rules/no-dataclasses.md`_
- **2026-06-21** [`fbbf559de2`](https://github.com/sgl-project/sglang/commit/fbbf559de2) [#28732](https://github.com/sgl-project/sglang/pull/28732)
  fix bench_one_batch by extending array with array not list (#28732)
  _Files: `python/sglang/bench_one_batch.py`_
- **2026-06-21** [`8a3d6c3403`](https://github.com/sgl-project/sglang/commit/8a3d6c3403) [#28811](https://github.com/sgl-project/sglang/pull/28811)
  Sort pyproject dependency lists (#28811)
  _Files: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml` _+2 more__
- **2026-06-20** [`2cbe1e6404`](https://github.com/sgl-project/sglang/commit/2cbe1e6404) [#28660](https://github.com/sgl-project/sglang/pull/28660)
  [Apple Silicon] [MLX] Fix MlxModelRunnerStub.initialize() signature desync with base (#28660)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `test/registered/unit/hardware_backend/mlx/test_runner_init_contract.py`_
- **2026-06-19** [`364bf976be`](https://github.com/sgl-project/sglang/commit/364bf976be) [#28744](https://github.com/sgl-project/sglang/pull/28744)
  [router] Tokenize prompt once at ingress; forward input_ids to the engine (all policies) (#28744)
  _Files: `experimental/sgl-router/src/policies/cache_aware_zmq.rs`, `experimental/sgl-router/src/policies/mod.rs`, `experimental/sgl-router/src/server/metrics.rs`, `experimental/sgl-router/src/server/routes/chat.rs` _+4 more__
- **2026-06-19** [`c3bae61e16`](https://github.com/sgl-project/sglang/commit/c3bae61e16) [#28665](https://github.com/sgl-project/sglang/pull/28665)
  [Bug] fix(DummyModelLoader): run post_load_weights before process_weights_after_loading (#28665)
  _Files: `python/sglang/srt/model_loader/loader.py`_
- **2026-06-19** [`abf7011cdd`](https://github.com/sgl-project/sglang/commit/abf7011cdd) [#28742](https://github.com/sgl-project/sglang/pull/28742)
  [router] Raise chat body cap to 5 MiB for long contexts (#28742)
  _Files: `experimental/sgl-router/src/server/metrics.rs`, `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/tests/proxy/chat_routing.rs`_
- **2026-06-19** [`d271de64fe`](https://github.com/sgl-project/sglang/commit/d271de64fe) [#28625](https://github.com/sgl-project/sglang/pull/28625)
  [misc] Move bench_one_batch_server into sglang/benchmark/ with a back-compat shim (#28625)
  _Files: `python/sglang/bench_one_batch_server.py`, `python/sglang/benchmark/one_batch_server.py`, `test/registered/kv_canary/test_self_e2e_bench_speed.py`_
- **2026-06-19** [`6fdcb9934c`](https://github.com/sgl-project/sglang/commit/6fdcb9934c) [#28677](https://github.com/sgl-project/sglang/pull/28677)
  fix(runner): size eager static buffers for prefill budget and MLP-sync autotune (#28677)
  _Files: `python/sglang/srt/model_executor/runner/eager_runner.py`, `python/sglang/srt/server_args.py`_
- **2026-06-19** [`ca88b7f1d2`](https://github.com/sgl-project/sglang/commit/ca88b7f1d2) [#23910](https://github.com/sgl-project/sglang/pull/23910)
  fix: remove manual rope parameters injection in `PretrainedConfig` (#23910)
  _Files: `python/sglang/srt/utils/hf_transformers_patches.py`, `test/registered/unit/utils/test_hf_transformers.py`_
- **2026-06-19** [`cab62855f5`](https://github.com/sgl-project/sglang/commit/cab62855f5) [#28717](https://github.com/sgl-project/sglang/pull/28717)
  [router] Align sgl_router_ttft_seconds buckets with engine TTFT grid (#28717)
  _Files: `experimental/sgl-router/src/server/metrics.rs`_
- **2026-06-19** [`5eaae5bacd`](https://github.com/sgl-project/sglang/commit/5eaae5bacd) [#28728](https://github.com/sgl-project/sglang/pull/28728)
  Add CODE_OF_CONDUCT.md (#28728)
  _Files: `CODE_OF_CONDUCT.md`_
- **2026-06-19** [`b6be5dd20f`](https://github.com/sgl-project/sglang/commit/b6be5dd20f) [#28719](https://github.com/sgl-project/sglang/pull/28719)
  [codex] Remove outdated SGLang SOTA skill (#28719)
  _Files: `.claude/skills/sglang-sota-performance/SKILL.md`_
- **2026-06-18** [`67db2ac3e7`](https://github.com/sgl-project/sglang/commit/67db2ac3e7) [#28382](https://github.com/sgl-project/sglang/pull/28382)
  refactor(runner): unify pp_proxy_tensors forward kwarg into one helper (#28382)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-06-18** [`59001267c3`](https://github.com/sgl-project/sglang/commit/59001267c3) [#28617](https://github.com/sgl-project/sglang/pull/28617)
  Fix bench serving base-url-only runs (#28617)
  _Files: `python/sglang/bench_serving.py`, `python/sglang/srt/utils/network.py`_
- **2026-06-18** [`d2539980b6`](https://github.com/sgl-project/sglang/commit/d2539980b6) [#28604](https://github.com/sgl-project/sglang/pull/28604)
  [Fix] don't force hybrid-SWA when sliding_window is disabled (#28604)
  _Files: `python/sglang/srt/configs/laguna.py`, `python/sglang/srt/configs/model_config.py`_
- **2026-06-18** [`4ee7882a46`](https://github.com/sgl-project/sglang/commit/4ee7882a46) [#28443](https://github.com/sgl-project/sglang/pull/28443)
  [XPU] fix(deps): upgrade diffusers to fix fresh installs (#28443)
  _Files: `python/pyproject_xpu.toml`_
- **2026-06-18** [`d27d8b24de`](https://github.com/sgl-project/sglang/commit/d27d8b24de) [#28597](https://github.com/sgl-project/sglang/pull/28597)
  fix (#28597)
  _Files: `.github/CODEOWNERS`_
- **2026-06-18** [`462c01ea6b`](https://github.com/sgl-project/sglang/commit/462c01ea6b) [#26252](https://github.com/sgl-project/sglang/pull/26252)
  [observability] add Ray metric backend wrappers (#26252)
  _Files: `python/sglang/srt/observability/ray_wrappers.py`, `python/sglang/test/observability/__init__.py`, `python/sglang/test/observability/fake_ray.py`, `test/registered/observability/test_metrics.py` _+2 more__
- **2026-06-18** [`cfa4aa988f`](https://github.com/sgl-project/sglang/commit/cfa4aa988f) [#28583](https://github.com/sgl-project/sglang/pull/28583)
  Revert "revert the head_dim assignment from PR 23862" (#28583)
  _Files: `python/sglang/srt/configs/model_config.py`, `test/registered/unit/configs/test_model_config_shapes.py`_
- **2026-06-17** [`b88bada64e`](https://github.com/sgl-project/sglang/commit/b88bada64e) [#28576](https://github.com/sgl-project/sglang/pull/28576)
  [misc] Unify bench seed default to 42 and rename --profile-filename-prefix to --profile-prefix (#28576)
  _Files: `python/sglang/bench_offline_throughput.py`, `python/sglang/bench_one_batch.py`, `python/sglang/bench_serving.py`_
- **2026-06-17** [`bcf298c28c`](https://github.com/sgl-project/sglang/commit/bcf298c28c) [#22053](https://github.com/sgl-project/sglang/pull/22053)
  [HiCache & Bench] add cache hit breakdown in bench_serving (#22053)
  _Files: `python/sglang/bench_serving.py`_
- **2026-06-17** [`5d6b35eabb`](https://github.com/sgl-project/sglang/commit/5d6b35eabb) [#28571](https://github.com/sgl-project/sglang/pull/28571)
  revert the head_dim assignment from PR 23862 (#28571)
  _Files: `python/sglang/srt/configs/model_config.py`, `test/registered/unit/configs/test_model_config_shapes.py`_
- **2026-06-17** [`e053890b6f`](https://github.com/sgl-project/sglang/commit/e053890b6f) [#28563](https://github.com/sgl-project/sglang/pull/28563)
  [Fix] Reuse an already-running server in bench_one_batch_server instead of forking an orphan (#28563)
  _Files: `python/sglang/test/bench_one_batch_server_internal.py`_
- **2026-06-17** [`7cead0fb8f`](https://github.com/sgl-project/sglang/commit/7cead0fb8f) [#28550](https://github.com/sgl-project/sglang/pull/28550)
  Add JonnyKong to CI_PERMISSIONS.json (#28550)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-06-17** [`c17190c059`](https://github.com/sgl-project/sglang/commit/c17190c059) [#28478](https://github.com/sgl-project/sglang/pull/28478)
  update codeowners (#28478)
  _Files: `.github/CODEOWNERS`_
- **2026-06-16** [`77f327cb6e`](https://github.com/sgl-project/sglang/commit/77f327cb6e) [#27313](https://github.com/sgl-project/sglang/pull/27313)
  [2/n] [CP] Add context parallel strategy abstractions (#27313)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/cp/__init__.py`, `python/sglang/srt/layers/cp/base.py`, `python/sglang/srt/layers/cp/interleave.py` _+5 more__
- **2026-06-16** [`556cf54d47`](https://github.com/sgl-project/sglang/commit/556cf54d47) [#28397](https://github.com/sgl-project/sglang/pull/28397)
  [Perf] Avoid per-decode-step host sync in min_new_tokens penalty (#28397)
  _Files: `python/sglang/srt/sampling/penaltylib/min_new_tokens.py`_
- **2026-06-16** [`b23477af44`](https://github.com/sgl-project/sglang/commit/b23477af44) [#28195](https://github.com/sgl-project/sglang/pull/28195)
  bench: infer tokenizer from serving model info (#28195)
  _Files: `python/sglang/bench_serving.py`_
- **2026-06-15** [`4c0457f440`](https://github.com/sgl-project/sglang/commit/4c0457f440) [#28342](https://github.com/sgl-project/sglang/pull/28342)
  [misc] Update codeowner (#28342)
  _Files: `.github/CODEOWNERS`_
- **2026-06-15** [`7e629a2f8c`](https://github.com/sgl-project/sglang/commit/7e629a2f8c) [#28280](https://github.com/sgl-project/sglang/pull/28280)
  Allow overriding tokenizer path in benchmark harness (#28280)
  _Files: `python/sglang/test/bench_one_batch_server_internal.py`_
- **2026-06-15** [`bf186cf8fc`](https://github.com/sgl-project/sglang/commit/bf186cf8fc) [#27802](https://github.com/sgl-project/sglang/pull/27802)
  bugfix revise interface get cpu copy for npu mem pool to align with gpu (#27802)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-06-15** [`a88ba6cc0b`](https://github.com/sgl-project/sglang/commit/a88ba6cc0b) [#28228](https://github.com/sgl-project/sglang/pull/28228)
  [Fix] Reduce power of two to constant time (#28228)
  _Files: `experimental/sgl-router/src/policies/power_of_two.rs`, `experimental/sgl-router/tests/component/policies/power_of_two.rs`_
- **2026-06-15** [`c0dfe4c8ec`](https://github.com/sgl-project/sglang/commit/c0dfe4c8ec) [#27980](https://github.com/sgl-project/sglang/pull/27980)
  [router] Reconcile workers that registered without resolving model_ids (#27980)
  _Files: `experimental/sgl-router/src/discovery/k8s.rs`, `experimental/sgl-router/src/workers/manager.rs`, `experimental/sgl-router/tests/component/workers/manager.rs`_

## Multimodal  (34 commits)

- **2026-06-22** [`4923bb93ae`](https://github.com/sgl-project/sglang/commit/4923bb93ae) [#28913](https://github.com/sgl-project/sglang/pull/28913)
  [diffusion] CI: fix turbo_wan/flux invisible CI cases (#28913)
  _Files: `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/test_utils.py`_
- **2026-06-22** [`0c9e775f2c`](https://github.com/sgl-project/sglang/commit/0c9e775f2c) [#28733](https://github.com/sgl-project/sglang/pull/28733)
  [Diffusion] Fix FastWan2.1 default 480p resolution (#28733)
  _Files: `python/sglang/multimodal_gen/configs/sample/wan.py`, `python/sglang/multimodal_gen/test/unit/test_sampling_params.py`_
- **2026-06-22** [`2b2cd21783`](https://github.com/sgl-project/sglang/commit/2b2cd21783) [#28834](https://github.com/sgl-project/sglang/pull/28834)
  [diffusion] fix: reject cache-dit with fsdp (#28834)
  _Files: `python/sglang/multimodal_gen/runtime/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-06-21** [`320b231ea6`](https://github.com/sgl-project/sglang/commit/320b231ea6) [#28833](https://github.com/sgl-project/sglang/pull/28833)
  [diffusion] chore: bound DiffGenerator local cleanup (#28833)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/diffusion_generator.py`, `python/sglang/multimodal_gen/runtime/scheduler_client.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_generator_shutdown.py`_
- **2026-06-21** [`a7f31a6e1b`](https://github.com/sgl-project/sglang/commit/a7f31a6e1b) [#28835](https://github.com/sgl-project/sglang/pull/28835)
  [diffusion] fix: fix SANA-WM CFG-parallel tensor devices (#28835)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/sana_wm/base.py`, `python/sglang/multimodal_gen/test/unit/sana_wm/test_pipeline_config.py`_
- **2026-06-21** [`c65f4ea692`](https://github.com/sgl-project/sglang/commit/c65f4ea692) [#28791](https://github.com/sgl-project/sglang/pull/28791)
  [diffusion] fix: validate openai sampling dimensions (#28791)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/utils.py`, `python/sglang/multimodal_gen/test/unit/test_openai_utils.py`_
- **2026-06-21** [`6a16573a7f`](https://github.com/sgl-project/sglang/commit/6a16573a7f) [#28790](https://github.com/sgl-project/sglang/pull/28790)
  [diffusion] fix: fix Qwen-Image-Layered string image paths (#28790)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/qwen_image_layered.py`, `python/sglang/multimodal_gen/test/unit/test_disagg_roles.py`_
- **2026-06-21** [`5b3eeaf504`](https://github.com/sgl-project/sglang/commit/5b3eeaf504) [#23377](https://github.com/sgl-project/sglang/pull/23377)
  [Fix] MM pool GPU alloc with base_gpu_id (#23377)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/utils/cuda_ipc_transport_utils.py`_
- **2026-06-20** [`a38eba0f1a`](https://github.com/sgl-project/sglang/commit/a38eba0f1a) [#28778](https://github.com/sgl-project/sglang/pull/28778)
  [diffusion] CI: remove flaky layerwise offload diffusion case (#28778)
  _Files: `python/sglang/multimodal_gen/test/server/accuracy_config.py`, `python/sglang/multimodal_gen/test/server/consistency_threshold.json`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines.json`_
- **2026-06-20** [`c1416bb3ee`](https://github.com/sgl-project/sglang/commit/c1416bb3ee) [#28773](https://github.com/sgl-project/sglang/pull/28773)
  [Diffusion] Keep FastHunyuan VAE resident on high-memory GPUs (#28773)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/model_deployment_config.py`, `python/sglang/multimodal_gen/runtime/server_args_auto_tune.py`_
- **2026-06-19** [`b225f48fcc`](https://github.com/sgl-project/sglang/commit/b225f48fcc) [#28724](https://github.com/sgl-project/sglang/pull/28724)
  [NPU][FIX CI] Set the warm-up mode to "request" for NPU diffusion tests (#28724)
  _Files: `python/sglang/multimodal_gen/test/server/ascend/testcase_configs_npu.py`_
- **2026-06-19** [`31c0a98066`](https://github.com/sgl-project/sglang/commit/31c0a98066) [#28711](https://github.com/sgl-project/sglang/pull/28711)
  [codex] Update diffusion skills for latest main (#28711)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md` _+2 more__
- **2026-06-19** [`af2ec2a0dd`](https://github.com/sgl-project/sglang/commit/af2ec2a0dd) [#28594](https://github.com/sgl-project/sglang/pull/28594)
  [diffusion] perf: merge LTX-2 stage-1 distilled LoRA into the base in original mode (#28594)
  _Files: `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/runtime/pipelines/ltx_2_pipeline.py`, `python/sglang/multimodal_gen/test/server/perf_baselines.json`, `python/sglang/multimodal_gen/test/unit/test_lora_commit_as_base.py`_
- **2026-06-19** [`59eb142ec2`](https://github.com/sgl-project/sglang/commit/59eb142ec2) [#22445](https://github.com/sgl-project/sglang/pull/22445)
  [NPU] [Diffusion] Performance Optimization for LTX-2 Model (#22445)
  _Files: `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`_
- **2026-06-19** [`3b417d3999`](https://github.com/sgl-project/sglang/commit/3b417d3999) [#28708](https://github.com/sgl-project/sglang/pull/28708)
  Revert "[Diffusion] FLUX: fuse FeedForward GELU into up-proj GEMM (cublasLt epilogue)" (#28708)
  _Files: `python/sglang/multimodal_gen/runtime/layers/fused_linear_act/__init__.py`, `python/sglang/multimodal_gen/runtime/layers/fused_linear_act/gelu.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux.py`_
- **2026-06-19** [`547a017a77`](https://github.com/sgl-project/sglang/commit/547a017a77) [#28593](https://github.com/sgl-project/sglang/pull/28593)
  [diffusion] CI: run nightly image comparisons on 2 GPUs (#28593)
  _Files: `scripts/ci/utils/diffusion/comparison_configs.json`_
- **2026-06-19** [`7da92e1112`](https://github.com/sgl-project/sglang/commit/7da92e1112) [#28393](https://github.com/sgl-project/sglang/pull/28393)
  [diffusion] Sana: pack self-attn q/k/v and cross-attn k/v into single GEMMs (#28393)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/sana.py`, `python/sglang/multimodal_gen/runtime/models/dits/sana.py`_
- **2026-06-19** [`7e20e25848`](https://github.com/sgl-project/sglang/commit/7e20e25848) [#28697](https://github.com/sgl-project/sglang/pull/28697)
  [docs] Add B300 cookbook deployment options (#28697)
  _Files: `docs_new/cookbook/autoregressive/InternLM/Intern-S1.mdx`, `docs_new/src/snippets/autoregressive/deepseek-math-v2-deployment.jsx`, `docs_new/src/snippets/autoregressive/deepseek-r1-advanced-deployment.jsx`, `docs_new/src/snippets/autoregressive/deepseek-r1-basic-deployment.jsx` _+23 more__
- **2026-06-18** [`105e095e00`](https://github.com/sgl-project/sglang/commit/105e095e00) [#28632](https://github.com/sgl-project/sglang/pull/28632)
  [Docker] Fix cu12 dev image build: pin torch reinstall + JIT-fallback for missing x86 cubins (#28632)
  _Files: `docker/Dockerfile`_
- **2026-06-18** [`05b3fd0f44`](https://github.com/sgl-project/sglang/commit/05b3fd0f44) [#28533](https://github.com/sgl-project/sglang/pull/28533)
  [diffusion] chore: remove ltx2 snapshot mode (#28533)
  _Files: `docs_new/cookbook/diffusion/LTX/LTX2 & LTX2.3.mdx`, `docs_new/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs_new/src/snippets/diffusion/ltx-deployment.jsx`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py` _+8 more__
- **2026-06-17** [`8aaca72c21`](https://github.com/sgl-project/sglang/commit/8aaca72c21) [#24970](https://github.com/sgl-project/sglang/pull/24970)
  [FIX]Fix Step3-VL multi-image embedding and local patch splitting (#24970)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/models/step3_vl.py`, `python/sglang/srt/models/step3_vl_10b.py`_
- **2026-06-17** [`9371062ef3`](https://github.com/sgl-project/sglang/commit/9371062ef3) [#27884](https://github.com/sgl-project/sglang/pull/27884)
  Fix deep seek ocr2 image processing (#27884)
  _Files: `python/sglang/benchmark/datasets/image.py`_
- **2026-06-17** [`6c8fdb5b62`](https://github.com/sgl-project/sglang/commit/6c8fdb5b62) [#21472](https://github.com/sgl-project/sglang/pull/21472)
  [diffusion] fix: fix PicklingError with --backend diffusers on non-T2I models (#21472)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/diffusers_generic.py`, `python/sglang/multimodal_gen/registry.py`_
- **2026-06-17** [`827fc56e00`](https://github.com/sgl-project/sglang/commit/827fc56e00) [#28474](https://github.com/sgl-project/sglang/pull/28474)
  [router] Multi-arch experimental sgl-router image + fix distroless libpcre2 startup crash (#28474)
  _Files: `.github/workflows/nightly-experimental-sgl-router-docker.yml`, `docker/sgl-router.Dockerfile`_
- **2026-06-16** [`c5b9106c1a`](https://github.com/sgl-project/sglang/commit/c5b9106c1a) [#28304](https://github.com/sgl-project/sglang/pull/28304)
  [perf] Use default torch compile mode for Wan2.2 T2V A14B (#28304)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/base.py`, `python/sglang/multimodal_gen/configs/models/dits/ltx_2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/__init__.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py` _+6 more__
- **2026-06-16** [`637c9f780b`](https://github.com/sgl-project/sglang/commit/637c9f780b) [#27088](https://github.com/sgl-project/sglang/pull/27088)
  [diffusion] fix: add precision consistency layer (#27088)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/adapter_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/bridge_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py` _+19 more__
- **2026-06-16** [`a4a8a614b1`](https://github.com/sgl-project/sglang/commit/a4a8a614b1) [#28317](https://github.com/sgl-project/sglang/pull/28317)
  [diffusion] UX: suppress noisy diffusers torchao warning (#28317)
  _Files: `python/sglang/multimodal_gen/runtime/utils/logging_utils.py`_
- **2026-06-16** [`01e45762ba`](https://github.com/sgl-project/sglang/commit/01e45762ba) [#28324](https://github.com/sgl-project/sglang/pull/28324)
  [diffusion] feat: use srt custom allreduce for tp groups (#28324)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/group_coordinator.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`_
- **2026-06-15** [`3a0dd69f8e`](https://github.com/sgl-project/sglang/commit/3a0dd69f8e) [#28072](https://github.com/sgl-project/sglang/pull/28072)
  Minor refactorings to the LFM2.5 cookbook for accuracy (#28072)
  _Files: `docs_new/cookbook/autoregressive/LiquidAI/LFM2.5.mdx`, `docs_new/docs/supported-models/generative_models.mdx`, `docs_new/docs/supported-models/multimodal_language_models.mdx`_
- **2026-06-15** [`818808d152`](https://github.com/sgl-project/sglang/commit/818808d152) [#28204](https://github.com/sgl-project/sglang/pull/28204)
  [diffusion] optimize: optimize causal conv3d vae padding (#28204)
  _Files: `python/sglang/jit_kernel/diffusion/triton/causal_conv3d_pad.py`, `python/sglang/multimodal_gen/runtime/layers/parallel_conv.py`, `python/sglang/multimodal_gen/runtime/models/vaes/autoencoder_kl_qwenimage.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py`_
- **2026-06-15** [`2a33724c9b`](https://github.com/sgl-project/sglang/commit/2a33724c9b) [#28056](https://github.com/sgl-project/sglang/pull/28056)
  [perf] Reuse a pooled HTTP session for multimodal URL downloads (#28056)
  _Files: `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/utils/common.py`_
- **2026-06-15** [`19c78552dc`](https://github.com/sgl-project/sglang/commit/19c78552dc) [#28263](https://github.com/sgl-project/sglang/pull/28263)
  [AMD] Restrict CI image fallback to versioned tags (#28263)
  _Files: `scripts/ci/amd/amd_ci_start_container.sh`, `scripts/ci/amd/amd_ci_start_container_disagg.sh`_
- **2026-06-15** [`578e936d8d`](https://github.com/sgl-project/sglang/commit/578e936d8d) [#28205](https://github.com/sgl-project/sglang/pull/28205)
  [diffusion] feat: persist torch.compile inductor/triton cache across restarts (#28205)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`_
- **2026-06-15** [`07b9108348`](https://github.com/sgl-project/sglang/commit/07b9108348) [#28166](https://github.com/sgl-project/sglang/pull/28166)
  [Diffusion] FLUX: fuse FeedForward GELU into up-proj GEMM (cublasLt epilogue) (#28166)
  _Files: `python/sglang/multimodal_gen/runtime/layers/fused_linear_act/__init__.py`, `python/sglang/multimodal_gen/runtime/layers/fused_linear_act/gelu.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux.py`_

## MoE / Expert Parallel  (28 commits)

- **2026-06-22** [`c0bb04b67f`](https://github.com/sgl-project/sglang/commit/c0bb04b67f) [#25820](https://github.com/sgl-project/sglang/pull/25820)
  [NVIDIA] Support NVFP4 MoE for DeepSeek-V4 (#25820)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` _+6 more__
- **2026-06-22** [`6779ca8d7f`](https://github.com/sgl-project/sglang/commit/6779ca8d7f) [#28619](https://github.com/sgl-project/sglang/pull/28619)
  Fix Qwen MoE precision issue with PP and all-reduce fusion (#28619)
  _Files: `python/sglang/srt/models/qwen2_moe.py`_
- **2026-06-20** [`95fb1ef697`](https://github.com/sgl-project/sglang/commit/95fb1ef697) [#28810](https://github.com/sgl-project/sglang/pull/28810)
  [CI] Remove deprecated test/srt legacy CI setup (#28810)
  _Files: `scripts/ci/amd/amd_ci_exec.sh`, `scripts/code_sync/utils.py`, `test/README.md`, `test/srt/cpu/arm64/test_moe.py` _+25 more__
- **2026-06-20** [`d6d06cdc17`](https://github.com/sgl-project/sglang/commit/d6d06cdc17) [#28074](https://github.com/sgl-project/sglang/pull/28074)
  [AMD] Fix no-op dtype cast in _topk_ids_logical_to_physical_dynamic on HIP (#28074)
  _Files: `python/sglang/srt/eplb/expert_location_dispatch.py`, `test/registered/unit/eplb/test_dispatch_dtype_preservation.py`_
- **2026-06-20** [`1115373668`](https://github.com/sgl-project/sglang/commit/1115373668) [#28244](https://github.com/sgl-project/sglang/pull/28244)
  [AMD] Fix garbled unquantized Qwen3-30B-A3B output on ROCm/aiter where the aiter CK fused-MoE falls back to Triton with pre-shuffled weights (#28244)
  _Files: `python/sglang/srt/layers/quantization/unquant.py`, `test/registered/amd/accuracy/mi35x/test_qwen3_moe_eval_mi35x.py`_
- **2026-06-19** [`6b945c16f4`](https://github.com/sgl-project/sglang/commit/6b945c16f4) [#28091](https://github.com/sgl-project/sglang/pull/28091)
  [LoRA] Fix experimental fast-path multi-adapter correctness + flashinfer 0.6.12 compatibility (#28091)
  _Files: `python/sglang/jit_kernel/trtllm_lora_temp/data/csrc/fused_activation_quant.cuh`, `python/sglang/jit_kernel/trtllm_lora_temp/data/csrc/fused_permute_quant.cuh`, `python/sglang/jit_kernel/trtllm_lora_temp/data/csrc/trtllm_fused_moe_kernel_launcher.cu`, `python/sglang/jit_kernel/trtllm_lora_temp/data/csrc/trtllm_fused_moe_runner.cu` _+11 more__
- **2026-06-19** [`c7397de571`](https://github.com/sgl-project/sglang/commit/c7397de571) [#28231](https://github.com/sgl-project/sglang/pull/28231)
  Use Marlin for SM120 MXFP4 MoE (#28231)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/mxfp4_moe_sm120_triton.py`, `python/sglang/srt/layers/moe/moe_runner/marlin.py`, `python/sglang/srt/layers/quantization/marlin_utils.py` _+4 more__
- **2026-06-19** [`05ee93c44f`](https://github.com/sgl-project/sglang/commit/05ee93c44f) [#28555](https://github.com/sgl-project/sglang/pull/28555)
  Remove redundant cast and copy in calling `trtllm_fp8_block_scale_moe` (#28555)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`_
- **2026-06-18** [`e3026ef016`](https://github.com/sgl-project/sglang/commit/e3026ef016) [#28421](https://github.com/sgl-project/sglang/pull/28421)
  [3/N][CP] Implement zigzag CP strategy (#28421)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/cp/base.py`, `python/sglang/srt/layers/cp/interleave.py`, `python/sglang/srt/layers/cp/utils.py` _+9 more__
- **2026-06-18** [`bea282cede`](https://github.com/sgl-project/sglang/commit/bea282cede) [#26766](https://github.com/sgl-project/sglang/pull/26766)
  [DeepSeek-V4] Fuse UE8M0 scale rounding into FP8 group quantization (#26766)
  _Files: `python/sglang/jit_kernel/csrc/gemm/per_token_group_quant_8bit_v2.cuh`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/jit/test_per_token_group_quant_8bit_v2.py` _+2 more__
- **2026-06-18** [`792cb3a5d0`](https://github.com/sgl-project/sglang/commit/792cb3a5d0) [#27377](https://github.com/sgl-project/sglang/pull/27377)
  fix: add missing guard for use_jit_ep_activation (#27377)
  _Files: `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`_
- **2026-06-18** [`2a9cce5d27`](https://github.com/sgl-project/sglang/commit/2a9cce5d27) [#28516](https://github.com/sgl-project/sglang/pull/28516)
  [NPU] Add MTP support for GLM-4.7-Flash (#28516)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/models/glm4_moe_lite.py`_
- **2026-06-18** [`9b10821c8e`](https://github.com/sgl-project/sglang/commit/9b10821c8e) [#25144](https://github.com/sgl-project/sglang/pull/25144)
  [NPU] Add Ascend NPU support for DeepSeek-V4 (#25144)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_allocator.py` _+24 more__
- **2026-06-18** [`6309fb9abb`](https://github.com/sgl-project/sglang/commit/6309fb9abb) [#28378](https://github.com/sgl-project/sglang/pull/28378)
  [AMD] Fix Always mask padded topk_ids on HIP to prevent garbage MoE routing (DeepSeek-R1-MXFP4 accuracy regression) (#28378)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-06-17** [`3fb65ebabd`](https://github.com/sgl-project/sglang/commit/3fb65ebabd) [#28459](https://github.com/sgl-project/sglang/pull/28459)
  [RL] Fix FlashInfer TRTLLM MXFP8 dense weight layout (#28459)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`, `test/registered/rl/test_update_weights_from_disk_blackwell.py`_
- **2026-06-17** [`c01f62e341`](https://github.com/sgl-project/sglang/commit/c01f62e341) [#28486](https://github.com/sgl-project/sglang/pull/28486)
  [bugfix] guard NVIDIA SM-capability checks with is_cuda() for AMD/ROCm (#28486)
  _Files: `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/server_args.py`_
- **2026-06-17** [`66ac385f52`](https://github.com/sgl-project/sglang/commit/66ac385f52) [#28469](https://github.com/sgl-project/sglang/pull/28469)
  fix(moe): MoRI EP init_mori_op missing BF16 dispatch branch (#28469)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`_
- **2026-06-17** [`f06e2d3d1f`](https://github.com/sgl-project/sglang/commit/f06e2d3d1f) [#27690](https://github.com/sgl-project/sglang/pull/27690)
  Support asymmetric compressed-tensors MoE (#27690)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`_
- **2026-06-17** [`0ae4740bd1`](https://github.com/sgl-project/sglang/commit/0ae4740bd1) [#27328](https://github.com/sgl-project/sglang/pull/27328)
  fix: add missing clamp_limit for CompressedTensorsWNA16MoE (#27328)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`_
- **2026-06-17** [`9c53853ea3`](https://github.com/sgl-project/sglang/commit/9c53853ea3) [#25702](https://github.com/sgl-project/sglang/pull/25702)
  Use pack topk ids triton kernel for flashinfer_trtllm_routed (#25702)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`_
- **2026-06-17** [`37ef295c78`](https://github.com/sgl-project/sglang/commit/37ef295c78) [#28216](https://github.com/sgl-project/sglang/pull/28216)
  [AMD] Feat/dp moe reduce scatter (#28216)
  _Files: `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/dp_attn/test_dp_attention.py`_
- **2026-06-16** [`13537f8e20`](https://github.com/sgl-project/sglang/commit/13537f8e20) [#27589](https://github.com/sgl-project/sglang/pull/27589)
  Unskip Marlin NVFP4 tests (#27589)
  _Files: `test/manual/models/test_nvidia_nemotron_3_nano_archived.py`, `test/registered/jit/test_gptq_marlin.py`, `test/registered/jit/test_moe_wna16_marlin.py`_
- **2026-06-16** [`92b42c8d8a`](https://github.com/sgl-project/sglang/commit/92b42c8d8a) [#24515](https://github.com/sgl-project/sglang/pull/24515)
  LPLB: linear-programming load balancer for MoE expert parallelism (#24515)
  _Files: `python/pyproject.toml`, `python/sglang/jit_kernel/csrc/lplb/dispatch_probability.cuh`, `python/sglang/jit_kernel/csrc/lplb/ipm.cuh`, `python/sglang/jit_kernel/csrc/lplb/lp_post.cuh` _+15 more__
- **2026-06-16** [`149fabcca7`](https://github.com/sgl-project/sglang/commit/149fabcca7) [#27636](https://github.com/sgl-project/sglang/pull/27636)
  [AMD] Fuse sigmoid + mul into single Triton kernel for shared expert gating (#27636)
  _Files: `python/sglang/jit_kernel/triton/sigmoid_gate_mul.py`, `python/sglang/srt/models/qwen2_moe.py`, `test/registered/kernels/test_sigmoid_gate_mul.py`_
- **2026-06-16** [`102392df5b`](https://github.com/sgl-project/sglang/commit/102392df5b) [#28404](https://github.com/sgl-project/sglang/pull/28404)
  [AMD][Fix] Skip EPLB topk remap when global server args are unset (#28404)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-06-16** [`486ec150d0`](https://github.com/sgl-project/sglang/commit/486ec150d0) [#28293](https://github.com/sgl-project/sglang/pull/28293)
  [NPU] Add NPU fallback for fused Triton gating kernels (#28293)
  _Files: `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`_
- **2026-06-15** [`63df86f5e7`](https://github.com/sgl-project/sglang/commit/63df86f5e7) [#22985](https://github.com/sgl-project/sglang/pull/22985)
  [AMD] Skip eplb bookkeeping and topk remap when EPLB is not in use on mori-ep / HIP (#22985) (#28188)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/layers/moe/topk.py`_
- **2026-06-15** [`441b75ee69`](https://github.com/sgl-project/sglang/commit/441b75ee69) [#27588](https://github.com/sgl-project/sglang/pull/27588)
  [quantization] NVFP4 MoE: split fused w13 gate/up global scales (#27588)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4_moe_scales.py`_

## Prefill / Decode Disaggregation  (20 commits)

- **2026-06-22** [`1adb53f147`](https://github.com/sgl-project/sglang/commit/1adb53f147) [#28718](https://github.com/sgl-project/sglang/pull/28718)
  Fix CP page filtering by request-local position (#28718)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/utils.py`_
- **2026-06-22** [`106d2930a6`](https://github.com/sgl-project/sglang/commit/106d2930a6) [#28363](https://github.com/sgl-project/sglang/pull/28363)
  [core] Gate the overlap WAR barrier on forward reads to recover decode throughput (#28363)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py` _+5 more__
- **2026-06-21** [`6d4ca9bc54`](https://github.com/sgl-project/sglang/commit/6d4ca9bc54) [#28755](https://github.com/sgl-project/sglang/pull/28755)
  Cap SWA pool sizing with chunk cache (#28755)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/minimax_m2_5.mdx`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/decode.py` _+8 more__
- **2026-06-20** [`ff1fc1fbdf`](https://github.com/sgl-project/sglang/commit/ff1fc1fbdf) [#27273](https://github.com/sgl-project/sglang/pull/27273)
  [mem_cache][5/N] refactor: extract host KV cache base layer into pool_host package (#27273)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/pool_host/__init__.py` _+12 more__
- **2026-06-20** [`7516f0db9f`](https://github.com/sgl-project/sglang/commit/7516f0db9f) [#28737](https://github.com/sgl-project/sglang/pull/28737)
  [cookbook] Laguna-M.1: add PD disaggregation section (#28737)
  _Files: `docs_new/cookbook/autoregressive/Poolside/Laguna-M.1.mdx`, `docs_new/src/snippets/configs/poolside/laguna-m1.jsx`_
- **2026-06-19** [`9bb9d17e1a`](https://github.com/sgl-project/sglang/commit/9bb9d17e1a) [#28682](https://github.com/sgl-project/sglang/pull/28682)
  [Spec] Unify speculative grammar token-accept path in decode processing (#28682)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/test/kits/spec_server_kits.py`, `test/registered/disaggregation/test_disaggregation_basic.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py` _+1 more__
- **2026-06-19** [`fac11f3bc1`](https://github.com/sgl-project/sglang/commit/fac11f3bc1) [#25094](https://github.com/sgl-project/sglang/pull/25094)
  [AMD] Document Mori XGMI for Single-Node PD Disaggregation (#25094)
  _Files: `docs_new/docs/references/environment_variables.mdx`_
- **2026-06-18** [`9fc9d37f6d`](https://github.com/sgl-project/sglang/commit/9fc9d37f6d) [#24082](https://github.com/sgl-project/sglang/pull/24082)
  Fix spec decoding with grammar in disagg (#24082)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/disaggregation/test_disaggregation_basic.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py`, `test/registered/unit/spec/test_decode_bookkeeping_ownership.py`_
- **2026-06-18** [`27a374eaef`](https://github.com/sgl-project/sglang/commit/27a374eaef) [#28678](https://github.com/sgl-project/sglang/pull/28678)
  [AMD][CI] Use non-gated Qwen3-8B for MI35x disaggregation tests (#28678)
  _Files: `test/registered/amd/disaggregation/test_disaggregation_basic.py`, `test/registered/amd/disaggregation/test_disaggregation_pp.py`_
- **2026-06-18** [`66a7fd5c0b`](https://github.com/sgl-project/sglang/commit/66a7fd5c0b) [#28151](https://github.com/sgl-project/sglang/pull/28151)
  refactor: mamba radix cache server args initialize (#28151)
  _Files: `python/sglang/srt/arg_groups/nemotron_h_hook.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/server_args.py`_
- **2026-06-18** [`7976928c57`](https://github.com/sgl-project/sglang/commit/7976928c57) [#28086](https://github.com/sgl-project/sglang/pull/28086)
  Abort during chunked prefill + PD peer-liveness abort (#28086)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/test/manual/disaggregation/test_chunked_prefill_abort.py` _+4 more__
- **2026-06-18** [`3b9db3a1f0`](https://github.com/sgl-project/sglang/commit/3b9db3a1f0) [#28302](https://github.com/sgl-project/sglang/pull/28302)
  [Mamba][GDN] Deduplicate spec conv-window intermediate cache via sliding window layout (#28302)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+1 more__
- **2026-06-17** [`d86a7e7018`](https://github.com/sgl-project/sglang/commit/d86a7e7018) [#28162](https://github.com/sgl-project/sglang/pull/28162)
  Custom spec algorithm can handle server args (#28162)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/hisparse_hook.py`, `python/sglang/srt/arg_groups/nemotron_h_hook.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py` _+4 more__
- **2026-06-16** [`175336ff73`](https://github.com/sgl-project/sglang/commit/175336ff73) [#28377](https://github.com/sgl-project/sglang/pull/28377)
  [Chore] update codeowner for mooncake store (#28377)
  _Files: `.github/CODEOWNERS`_
- **2026-06-15** [`33719cfb31`](https://github.com/sgl-project/sglang/commit/33719cfb31) [#28085](https://github.com/sgl-project/sglang/pull/28085)
  [PD] Optimize SWA allocation (#28085)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/allocator/swa.py`, `test/registered/unit/mem_cache/test_swa_alloc_extend_page_estimation.py`_
- **2026-06-15** [`378e66d248`](https://github.com/sgl-project/sglang/commit/378e66d248) [#28238](https://github.com/sgl-project/sglang/pull/28238)
  [PD] Remove outdated backend whitelist for decode radix cache (#28238)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-06-15** [`8bdb007e58`](https://github.com/sgl-project/sglang/commit/8bdb007e58) [#28277](https://github.com/sgl-project/sglang/pull/28277)
  [NPU] Docs op performance optimize (#28277)
  _Files: `docs_new/docs/advanced_features/pd_disaggregation.mdx`, `docs_new/docs/basic_usage/send_request.mdx`, `docs_new/docs/developer_guide/msprobe_debugging_guide.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_operator_performance_optimizing.mdx`_
- **2026-06-15** [`eb349efb14`](https://github.com/sgl-project/sglang/commit/eb349efb14) [#28031](https://github.com/sgl-project/sglang/pull/28031)
  [EPD][BugFix] Fix encode_with_global_cache_mooncake (#28031)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`_
- **2026-06-15** [`bf38a0b03d`](https://github.com/sgl-project/sglang/commit/bf38a0b03d) [#25736](https://github.com/sgl-project/sglang/pull/25736)
  Fix disaggregated decode load token accounting (#25736)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler_components/load_inquirer.py`_
- **2026-06-15** [`37505eca27`](https://github.com/sgl-project/sglang/commit/37505eca27) [#27122](https://github.com/sgl-project/sglang/pull/27122)
  feat: report multimodal (image/audio/video) token counts in usage.prompt_tokens_details (#27122)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py` _+7 more__

## Docs / Examples  (18 commits)

- **2026-06-22** [`5deca2d39f`](https://github.com/sgl-project/sglang/commit/5deca2d39f) [#28643](https://github.com/sgl-project/sglang/pull/28643)
  [DOC] [NPU] Update features on Ascend NPU (#28643)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-06-19** [`d962d18f15`](https://github.com/sgl-project/sglang/commit/d962d18f15) [#28693](https://github.com/sgl-project/sglang/pull/28693)
  docs: add --trust-remote-code to Laguna-M.1 / XS.2 cookbook configs (#28693)
  _Files: `docs_new/cookbook/autoregressive/Poolside/Laguna-M.1.mdx`, `docs_new/cookbook/autoregressive/Poolside/Laguna-XS.2.mdx`, `docs_new/src/snippets/autoregressive/laguna-xs2-deployment.jsx`, `docs_new/src/snippets/configs/poolside/laguna-m1.jsx`_
- **2026-06-18** [`61a8b42c00`](https://github.com/sgl-project/sglang/commit/61a8b42c00) [#28668](https://github.com/sgl-project/sglang/pull/28668)
  docs(minimax-m3): add MMMU-Pro accuracy to B200 benchmark card (#28668)
  _Files: `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx`, `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`_
- **2026-06-18** [`0eded9e208`](https://github.com/sgl-project/sglang/commit/0eded9e208) [#28661](https://github.com/sgl-project/sglang/pull/28661)
  Add Laguna-M.1 cookbook (#28661)
  _Files: `docs_new/cookbook/autoregressive/Poolside/Laguna-M.1.mdx`, `docs_new/cookbook/autoregressive/Poolside/Laguna-XS.2.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json` _+2 more__
- **2026-06-18** [`1981464ba4`](https://github.com/sgl-project/sglang/commit/1981464ba4) [#28589](https://github.com/sgl-project/sglang/pull/28589)
  docs: sync LMSYS SGLang blog cards (#28589)
  _Files: `docs_new/index.mdx`_
- **2026-06-17** [`71b090a8e7`](https://github.com/sgl-project/sglang/commit/71b090a8e7) [#28433](https://github.com/sgl-project/sglang/pull/28433)
  [Ascend]GLM 5.2 deployment (#28433)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_glm5.2_examples.mdx`_
- **2026-06-17** [`ca84d52b78`](https://github.com/sgl-project/sglang/commit/ca84d52b78) [#28321](https://github.com/sgl-project/sglang/pull/28321)
  [Router] [Docs] Refresh policy-selection notes (#28321)
  _Files: `experimental/sgl-router/BENCHMARKS.md`_
- **2026-06-16** [`b8b8992dde`](https://github.com/sgl-project/sglang/commit/b8b8992dde) [#28338](https://github.com/sgl-project/sglang/pull/28338)
  docs: add Amazon SageMaker AI deployment guide (#28338)
  _Files: `docs_new/docs.json`, `docs_new/docs/basic_usage/aws_sagemaker.mdx`, `docs_new/docs/get-started/install.mdx`_
- **2026-06-16** [`33f205d8c5`](https://github.com/sgl-project/sglang/commit/33f205d8c5) [#28454](https://github.com/sgl-project/sglang/pull/28454)
  docs(cookbook): fix GLM-5.2 thinking toggle kwarg + document reasoning effort (#28454)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`_
- **2026-06-16** [`0cb6183432`](https://github.com/sgl-project/sglang/commit/0cb6183432) [#28437](https://github.com/sgl-project/sglang/pull/28437)
  docs(cookbook): add GLM-5.2 deployment cookbook (#28437)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.1.mdx`, `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json` _+2 more__
- **2026-06-16** [`12ebb35439`](https://github.com/sgl-project/sglang/commit/12ebb35439) [#28330](https://github.com/sgl-project/sglang/pull/28330)
  docs: refresh README News section and add Modal to adoption list (#28330)
  _Files: `README.md`_
- **2026-06-16** [`407d3a91db`](https://github.com/sgl-project/sglang/commit/407d3a91db) [#28364](https://github.com/sgl-project/sglang/pull/28364)
  docs: sync LMSYS SGLang blog cards (#28364)
  _Files: `docs_new/index.mdx`_
- **2026-06-15** [`30d8ee87b0`](https://github.com/sgl-project/sglang/commit/30d8ee87b0) [#28004](https://github.com/sgl-project/sglang/pull/28004)
  Add OrcaRouter usage example (#28004)
  _Files: `examples/frontend_language/quick_start/orcarouter_example_chat.py`_
- **2026-06-15** [`81166f382d`](https://github.com/sgl-project/sglang/commit/81166f382d) [#28283](https://github.com/sgl-project/sglang/pull/28283)
  Fix inaccuracies and add NPU constraints in ascend_npu_profiling.mdx. (#28283)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_profiling.mdx`_
- **2026-06-15** [`f8d1d397b6`](https://github.com/sgl-project/sglang/commit/f8d1d397b6) [#28279](https://github.com/sgl-project/sglang/pull/28279)
  [NPU] fix ascend_docs (#28279)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_faq.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_operator_development.mdx`_
- **2026-06-15** [`f768344b1a`](https://github.com/sgl-project/sglang/commit/f768344b1a) [#28295](https://github.com/sgl-project/sglang/pull/28295)
  [DOCS][NPU]Supplementary Notes (#28295)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`_
- **2026-06-15** [`7bd1a9d163`](https://github.com/sgl-project/sglang/commit/7bd1a9d163) [#28284](https://github.com/sgl-project/sglang/pull/28284)
  Update documentation for Ascend NPU Guide (#28284)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_optimization.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_performance_testing.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quick_start.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-06-15** [`edd5eff519`](https://github.com/sgl-project/sglang/commit/edd5eff519) [#28296](https://github.com/sgl-project/sglang/pull/28296)
  [NPU] [DOC] fix issues in ascend_npu_support_new_models (#28296)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_new_models.mdx`_

## Triton / Kernels  (17 commits)

- **2026-06-22** [`06e001347a`](https://github.com/sgl-project/sglang/commit/06e001347a) [#28930](https://github.com/sgl-project/sglang/pull/28930)
  [CI] Update nixl installation to include nixl-cu13 for h20 runner (#28930)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-06-22** [`b8e64fb56d`](https://github.com/sgl-project/sglang/commit/b8e64fb56d) [#28927](https://github.com/sgl-project/sglang/pull/28927)
  [CI] Modify nixl installation to force reinstall (#28927)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-06-22** [`db12bfcdc8`](https://github.com/sgl-project/sglang/commit/db12bfcdc8) [#28670](https://github.com/sgl-project/sglang/pull/28670)
  [JIT] Add kpool_topk_transform JIT kernel (#28670)
  _Files: `python/sglang/jit_kernel/csrc/dsa/kpool_topk_transform.cuh`, `python/sglang/jit_kernel/kpool_topk_transform.py`, `test/registered/jit/test_kpool_topk_transform.py`_
- **2026-06-21** [`3975ea5ac7`](https://github.com/sgl-project/sglang/commit/3975ea5ac7) [#28818](https://github.com/sgl-project/sglang/pull/28818)
  Fix H20 torch import reinstall fallback (#28818)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-06-19** [`2aa7b58aa7`](https://github.com/sgl-project/sglang/commit/2aa7b58aa7) [#28740](https://github.com/sgl-project/sglang/pull/28740)
  refactor(runner): reuse a prepared static buffer for every dummy run (#28740)
  _Files: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/model_executor/runner/base_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-06-19** [`d705a91de1`](https://github.com/sgl-project/sglang/commit/d705a91de1) [#28386](https://github.com/sgl-project/sglang/pull/28386)
  refactor(runner): add EagerRunner, own the eager path, polymorphic dispatch (#28386)
  _Files: `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/__init__.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+1 more__
- **2026-06-19** [`a6db86d535`](https://github.com/sgl-project/sglang/commit/a6db86d535) [#28385](https://github.com/sgl-project/sglang/pull/28385)
  refactor(runner): split BaseRunner (shared) from BaseCudaGraphRunner (#28385)
  _Files: `python/sglang/srt/model_executor/runner/__init__.py`, `python/sglang/srt/model_executor/runner/base_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/base_runner.py`_
- **2026-06-19** [`1c8551169d`](https://github.com/sgl-project/sglang/commit/1c8551169d) [#28551](https://github.com/sgl-project/sglang/pull/28551)
  Add opt-in CUDA-graph capture-trace export (#28551)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/utils/profile_utils.py`_
- **2026-06-17** [`b1d18d562b`](https://github.com/sgl-project/sglang/commit/b1d18d562b) [#28572](https://github.com/sgl-project/sglang/pull/28572)
  chore: bump sglang-kernel version to 0.4.4 (#28572)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`_
- **2026-06-17** [`74155d32bd`](https://github.com/sgl-project/sglang/commit/74155d32bd) [#28311](https://github.com/sgl-project/sglang/pull/28311)
  [NPU] [DOC] Update Ascend NPU docs: HDK 25.5.2, Triton 3.2.1.dev20260530 (#28311)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`_
- **2026-06-16** [`4f9b12c5dd`](https://github.com/sgl-project/sglang/commit/4f9b12c5dd) [#28426](https://github.com/sgl-project/sglang/pull/28426)
  [XPU] Guard tvm_ffi import in dsv4 compress modules under TYPE_CHECKING (#28426)
  _Files: `python/sglang/jit_kernel/dsv4/compress.py`_
- **2026-06-16** [`c0a6c3ce66`](https://github.com/sgl-project/sglang/commit/c0a6c3ce66) [#28002](https://github.com/sgl-project/sglang/pull/28002)
  Fix circular import when sglang.srt.model_executor.runner_backend is imported first (#28002)
  _Files: `python/sglang/srt/model_executor/runner_backend/base_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_backend/breakable_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_backend/full_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_backend/tc_piecewise_cuda_graph_backend.py`_
- **2026-06-16** [`25e696aa8d`](https://github.com/sgl-project/sglang/commit/25e696aa8d) [#28367](https://github.com/sgl-project/sglang/pull/28367)
  Fix Stage B CUDA CI (#28367)
  _Files: `test/registered/kernels/test_mhc_kernels.py`_
- **2026-06-15** [`f870bf1ed0`](https://github.com/sgl-project/sglang/commit/f870bf1ed0) [#27986](https://github.com/sgl-project/sglang/pull/27986)
  [dsv4] Prewarm MHC prenorm kernel at startup (#27986)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `python/sglang/srt/layers/mhc.py`_
- **2026-06-15** [`d5899b95c4`](https://github.com/sgl-project/sglang/commit/d5899b95c4) [#27868](https://github.com/sgl-project/sglang/pull/27868)
  fix(qwen3.5): keep CUDA dual-stream overlap (regressed by #25885) (#27868)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-06-15** [`3b419f66da`](https://github.com/sgl-project/sglang/commit/3b419f66da) [#28273](https://github.com/sgl-project/sglang/pull/28273)
  [JIT] Track angle-bracket includes in source hash (#28273)
  _Files: `python/sglang/jit_kernel/utils.py`_
- **2026-06-15** [`1180b70440`](https://github.com/sgl-project/sglang/commit/1180b70440) [#27624](https://github.com/sgl-project/sglang/pull/27624)
  triton-ascend update (#27624)
  _Files: `docker/npu.Dockerfile`, `scripts/ci/npu/npu_ci_install_dependency.sh`_

## Quantization  (17 commits)

- **2026-06-22** [`441ae9a5ae`](https://github.com/sgl-project/sglang/commit/441ae9a5ae) [#28885](https://github.com/sgl-project/sglang/pull/28885)
  [Lint] Fix black formatting of DeepSeek-R1-MXFP4 MI35x tests (#28885)
- **2026-06-22** [`64e455d4bf`](https://github.com/sgl-project/sglang/commit/64e455d4bf) [#28886](https://github.com/sgl-project/sglang/pull/28886)
  Fix lint break on main (#28886)
  _Files: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp4_mi35x.py`_
- **2026-06-20** [`47cad39f34`](https://github.com/sgl-project/sglang/commit/47cad39f34) [#28722](https://github.com/sgl-project/sglang/pull/28722)
  [AMD] Optimize o_proj gemm and attn output rope performance (#28722)
  _Files: `python/sglang/srt/layers/deepseek_v4_rope.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-06-19** [`871ed0dc0c`](https://github.com/sgl-project/sglang/commit/871ed0dc0c) [#28751](https://github.com/sgl-project/sglang/pull/28751)
  Revert "ci: add 4-GPU mi35x runner and rebalance off the saturated 8-GPU pool" (#28751)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml` _+2 more__
- **2026-06-19** [`13aab2fc06`](https://github.com/sgl-project/sglang/commit/13aab2fc06) [#28745](https://github.com/sgl-project/sglang/pull/28745)
  ci: add 4-GPU mi35x runner and rebalance off the saturated 8-GPU pool (#28745)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml` _+2 more__
- **2026-06-19** [`ab0714d0ee`](https://github.com/sgl-project/sglang/commit/ab0714d0ee) [#28536](https://github.com/sgl-project/sglang/pull/28536)
  ci: run GB300 nightly suite in the standard Nvidia nightly workflow (#28536)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `python/sglang/test/performance_test_runner.py`, `test/registered/gb300/test_deepseek_v32.py`, `test/registered/gb300/test_deepseek_v32_nvfp4.py` _+7 more__
- **2026-06-18** [`f7632ef860`](https://github.com/sgl-project/sglang/commit/f7632ef860) [#28664](https://github.com/sgl-project/sglang/pull/28664)
  [Cookbook] Laguna-M.1: enable FP8 on Blackwell + drop provisional AIME numbers (#28664)
  _Files: `docs_new/cookbook/autoregressive/Poolside/Laguna-M.1.mdx`, `docs_new/src/snippets/configs/poolside/laguna-m1-benchmarks.jsx`, `docs_new/src/snippets/configs/poolside/laguna-m1.jsx`_
- **2026-06-18** [`b7d7dfb4ed`](https://github.com/sgl-project/sglang/commit/b7d7dfb4ed) [#28629](https://github.com/sgl-project/sglang/pull/28629)
  [Bugfix] Fix Intern-S1 FP8 expert count lookup (#28629)
  _Files: `python/sglang/srt/models/interns1.py`_
- **2026-06-18** [`3b61dc32c9`](https://github.com/sgl-project/sglang/commit/3b61dc32c9) [#28546](https://github.com/sgl-project/sglang/pull/28546)
  [diffusion] fix: fix fp8 fused tp scale loading (#28546)
  _Files: `python/sglang/multimodal_gen/runtime/layers/linear.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/test_utils.py`, `python/sglang/multimodal_gen/test/unit/test_parallel_linear_weight_loading.py`_
- **2026-06-18** [`5d1949152d`](https://github.com/sgl-project/sglang/commit/5d1949152d) [#28458](https://github.com/sgl-project/sglang/pull/28458)
  [AMD] ci: add extra-a 1-gpu-large tier (fp8kv-triton, streaming-session, spec-standalone) (#28458)
  _Files: `.github/workflows/pr-test-amd-extra.yml`, `test/registered/quant/test_fp8kv_triton.py`, `test/registered/sessions/test_streaming_session_extra.py`, `test/registered/spec/test_spec_standalone_extra.py` _+1 more__
- **2026-06-17** [`873196f7fa`](https://github.com/sgl-project/sglang/commit/873196f7fa) [#28505](https://github.com/sgl-project/sglang/pull/28505)
  :recycle: [llm][npu][quant] Delegate MXFP8 dense scheme to kernel and use torch.ops.npu (#28505)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`, `python/sglang/srt/layers/quantization/modelslim/schemes/modelslim_mxfp8.py`_
- **2026-06-17** [`2f1390fcb1`](https://github.com/sgl-project/sglang/commit/2f1390fcb1) [#27553](https://github.com/sgl-project/sglang/pull/27553)
  fix: preserve divisible FP8 block K configs on CUDA (#27553)
  _Files: `python/sglang/srt/layers/quantization/fp8_kernel.py`_
- **2026-06-17** [`0f5e14e1d9`](https://github.com/sgl-project/sglang/commit/0f5e14e1d9) [#28318](https://github.com/sgl-project/sglang/pull/28318)
  [diffusion] fix: use Megatron-style tp for native encoders and dits (#28318)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/base_device_communicator.py`, `python/sglang/multimodal_gen/runtime/layers/linear.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/weight_only_fp8.py` _+12 more__
- **2026-06-17** [`72ccfec594`](https://github.com/sgl-project/sglang/commit/72ccfec594) [#28460](https://github.com/sgl-project/sglang/pull/28460)
  docs(cookbook): verify GLM-5.2 single-node B300 (FP8 + BF16) (#28460)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs_new/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-06-16** [`2ad00faae1`](https://github.com/sgl-project/sglang/commit/2ad00faae1) [#28467](https://github.com/sgl-project/sglang/pull/28467)
  [ci] add kimi nvfp4 nightly tests (#28467)
  _Files: `test/registered/quant/test_kimi_k25_nvfp4_eagle.py`_
- **2026-06-16** [`2a8ea70059`](https://github.com/sgl-project/sglang/commit/2a8ea70059) [#22352](https://github.com/sgl-project/sglang/pull/22352)
  :sparkles: [llm][npu][quant] Add W8A8 MXFP8 quantization support for Qwen3 Dense on Ascend NPU (#22352)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quantization.mdx`, `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`, `python/sglang/srt/layers/quantization/fp8.py` _+4 more__
- **2026-06-16** [`72d962be88`](https://github.com/sgl-project/sglang/commit/72d962be88) [#27947](https://github.com/sgl-project/sglang/pull/27947)
  [AMD] Fix jit-kernel-unit-test-amd: activation.cuh ROCm build + per_token CUDA-only (R165) (#27947)
  _Files: `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`, `python/sglang/jit_kernel/csrc/gemm/per_token_group_quant_8bit.cuh`, `test/registered/jit/test_per_token_group_quant_8bit.py`_

## Speculative Decoding  (16 commits)

- **2026-06-22** [`ad9723af03`](https://github.com/sgl-project/sglang/commit/ad9723af03) [#28937](https://github.com/sgl-project/sglang/pull/28937)
  Clean up CUDA graph capture logs (#28937)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/multi_layer_eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/base_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+5 more__
- **2026-06-22** [`2ce32366a0`](https://github.com/sgl-project/sglang/commit/2ce32366a0) [#28870](https://github.com/sgl-project/sglang/pull/28870)
  [Fix][BCG][Spec] Restore EAGLE prefill plumbing dropped by #23906 (#28870)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/cuda_graph/breakable/test_bcg_with_speculative_decoding.py`_
- **2026-06-21** [`4f5ff39bc9`](https://github.com/sgl-project/sglang/commit/4f5ff39bc9) [#28856](https://github.com/sgl-project/sglang/pull/28856)
  [Spec] Enable FR-Spec in EAGLE draft-extend CUDA graph by sizing logits buffer from the draft head (#28856)
  _Files: `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-06-21** [`5351800700`](https://github.com/sgl-project/sglang/commit/5351800700) [#28410](https://github.com/sgl-project/sglang/pull/28410)
  [Bugfix] Fix MTP acceptance regression on plan stream by moving int64 cast before plan stream context (#28410)
  _Files: `python/sglang/srt/speculative/base_spec_worker.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-06-20** [`f42ec350b4`](https://github.com/sgl-project/sglang/commit/f42ec350b4) [#26312](https://github.com/sgl-project/sglang/pull/26312)
  [mtp] add rejection sampling for speculative decoding (#26312)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/server_args.py` _+7 more__
- **2026-06-18** [`62ab09a478`](https://github.com/sgl-project/sglang/commit/62ab09a478) [#28558](https://github.com/sgl-project/sglang/pull/28558)
  [AMD] register 2 spec tests to stage-b-test-1-gpu-large-amd (batch-5) (#28558)
  _Files: `test/registered/spec/eagle/test_adaptive_speculative.py`, `test/registered/spec/test_frozen_kv_mtp.py`_
- **2026-06-17** [`a663500ea9`](https://github.com/sgl-project/sglang/commit/a663500ea9) [#28577](https://github.com/sgl-project/sglang/pull/28577)
  [Test] Fold EAGLE `return_hidden_states` regression into spec triton suite (#28577)
  _Files: `python/sglang/test/kits/spec_server_kits.py`, `python/sglang/test/server_fixtures/spec_eagle_fixture.py`, `test/registered/spec/eagle/test_eagle_hidden_states.py`, `test/registered/spec/eagle/test_spec_eagle_triton.py`_
- **2026-06-17** [`e4fd613def`](https://github.com/sgl-project/sglang/commit/e4fd613def) [#28496](https://github.com/sgl-project/sglang/pull/28496)
  [Spec] Fix return_hidden_states under spec V2 (issue #26163) (#28496)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `test/registered/spec/eagle/test_eagle_hidden_states.py`_
- **2026-06-17** [`753aa89a83`](https://github.com/sgl-project/sglang/commit/753aa89a83) [#28464](https://github.com/sgl-project/sglang/pull/28464)
  [spec decoding] fix mrope_positions in draft extend (#28464)
  _Files: `python/sglang/srt/model_executor/forward_batch_info.py`_
- **2026-06-17** [`3c4130c741`](https://github.com/sgl-project/sglang/commit/3c4130c741) [#28343](https://github.com/sgl-project/sglang/pull/28343)
  [Kimi K2.5] Fix eagle3 aux capture for tp>1 when AR fusion is enabled (#28343)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/deepseek_v2.py`_
- **2026-06-17** [`f86e9b48e8`](https://github.com/sgl-project/sglang/commit/f86e9b48e8) [#28500](https://github.com/sgl-project/sglang/pull/28500)
  [Perf] Make spec-decode penalty H2D non-blocking and share decode cumulate path (#28500)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/speculative/eagle_info_v2.py`_
- **2026-06-17** [`b54f8432ad`](https://github.com/sgl-project/sglang/commit/b54f8432ad) [#28465](https://github.com/sgl-project/sglang/pull/28465)
  Batch EAGLE draft/draft-extend replay memcpys via grouped foreach copy (#28465)
  _Files: `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`_
- **2026-06-16** [`fcca4611fa`](https://github.com/sgl-project/sglang/commit/fcca4611fa) [#27593](https://github.com/sgl-project/sglang/pull/27593)
  [CAR] Let custom allreduce support VMM based allocation (#27593)
  _Files: `python/sglang/jit_kernel/all_reduce.py`, `python/sglang/jit_kernel/csrc/distributed/custom_all_reduce_base.cuh`, `python/sglang/jit_kernel/csrc/distributed/custom_all_reduce_pull.cuh`, `python/sglang/jit_kernel/include/sgl_kernel/distributed/custom_all_reduce.cuh` _+3 more__
- **2026-06-16** [`c6d9d73fd6`](https://github.com/sgl-project/sglang/commit/c6d9d73fd6) [#28325](https://github.com/sgl-project/sglang/pull/28325)
  [Spec][test] fix(kv_canary): assert draft-extend-v2 oracle tokens in token_oracle test (#28325)
  _Files: `test/registered/kv_canary/test_self_unit_token_oracle.py`_
- **2026-06-15** [`ce9fad7196`](https://github.com/sgl-project/sglang/commit/ce9fad7196) [#28043](https://github.com/sgl-project/sglang/pull/28043)
  [Bugfix][DeepSeek-V4] Fix Spec V2 Draft Input ID Dtype for DP Collectives (#28043)
  _Files: `python/sglang/srt/speculative/base_spec_worker.py`_
- **2026-06-15** [`0417951a86`](https://github.com/sgl-project/sglang/commit/0417951a86) [#27882](https://github.com/sgl-project/sglang/pull/27882)
  [Bug Fix] Validate tokenizer-dependent features with skip_tokenizer_init (#27882)
  _Files: `python/sglang/srt/sampling/sampling_params.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/managers/test_stop_str_speculative.py`, `test/registered/unit/sampling/test_sampling_params.py`_

## ROCm / AMD  (16 commits)

- **2026-06-22** [`73448b0d70`](https://github.com/sgl-project/sglang/commit/73448b0d70) [#28871](https://github.com/sgl-project/sglang/pull/28871)
  [AMD] Temporarily disable deepseek V4 in AMD PR test (#28871)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`_
- **2026-06-21** [`a4d0ff3def`](https://github.com/sgl-project/sglang/commit/a4d0ff3def) [#28829](https://github.com/sgl-project/sglang/pull/28829)
  [misc] Make NaN-logit sanitization opt-in (default off) (#28829)
  _Files: `python/sglang/srt/environ.py`, `scripts/ci/amd/amd_ci_exec.sh`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`_
- **2026-06-20** [`653f6735a0`](https://github.com/sgl-project/sglang/commit/653f6735a0) [#28611](https://github.com/sgl-project/sglang/pull/28611)
  [AMD] add nightly kv_canary JIT benchmark suite (#28611)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/jit/benchmark/kv_canary/bench_plan.py`, `test/registered/jit/benchmark/kv_canary/bench_scatter_req_token_ids.py` _+3 more__
- **2026-06-19** [`24d15dd92e`](https://github.com/sgl-project/sglang/commit/24d15dd92e) [#28541](https://github.com/sgl-project/sglang/pull/28541)
  [AMD][DSV4] fix nonetype issue when enabling hicache (#28541)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/server_args.py`_
- **2026-06-19** [`4d94e9471a`](https://github.com/sgl-project/sglang/commit/4d94e9471a) [#28226](https://github.com/sgl-project/sglang/pull/28226)
  [AMD] Relax allreduce-fusion residual accuracy tolerance to 1 bf16 ULP (#28226)
  _Files: `test/registered/ops/test_aiter_allreduce_fusion_amd.py`_
- **2026-06-18** [`0e5a66dca4`](https://github.com/sgl-project/sglang/commit/0e5a66dca4) [#27837](https://github.com/sgl-project/sglang/pull/27837)
  [AMD] Register 3 JIT kernel unit tests for AMD CI (#27837)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/jit/test_clamp_position.py`, `test/registered/jit/test_resolve_future_token_ids.py` _+1 more__
- **2026-06-17** [`3e97c9239f`](https://github.com/sgl-project/sglang/commit/3e97c9239f) [#28556](https://github.com/sgl-project/sglang/pull/28556)
  chore: bump sgl-kernel version to 0.4.4 (#28556)
  _Files: `sgl-kernel/pyproject.toml`, `sgl-kernel/pyproject_cpu.toml`, `sgl-kernel/pyproject_musa.toml`, `sgl-kernel/pyproject_rocm.toml` _+1 more__
- **2026-06-17** [`9b8c41171a`](https://github.com/sgl-project/sglang/commit/9b8c41171a) [#28473](https://github.com/sgl-project/sglang/pull/28473)
  [AMD] Fall back to layer_first layout for kernel write-back on ROCm (#28473)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-17** [`7256ee9871`](https://github.com/sgl-project/sglang/commit/7256ee9871) [#27815](https://github.com/sgl-project/sglang/pull/27815)
  [AMD] Update test_aiter_allgather_amd.py data types alignment between benchmark aiter and custom all-reduce kernel (#27815)
  _Files: `test/registered/ops/test_aiter_allgather_amd.py`_
- **2026-06-17** [`0d651e653b`](https://github.com/sgl-project/sglang/commit/0d651e653b) [#28423](https://github.com/sgl-project/sglang/pull/28423)
  [AMD] Update v4 amd cookbook (#28423)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/_deployment.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs_new/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-06-16** [`ed9024e09f`](https://github.com/sgl-project/sglang/commit/ed9024e09f) [#28360](https://github.com/sgl-project/sglang/pull/28360)
  [AMD] Fix AITER Scout workflow permissions (#28360)
  _Files: `.github/workflows/amd-aiter-scout.yml`_
- **2026-06-16** [`448af67a98`](https://github.com/sgl-project/sglang/commit/448af67a98) [#28368](https://github.com/sgl-project/sglang/pull/28368)
  ci: run AMD and NPU PR tests on PRs not targeting main (#28368)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test-npu.yml`_
- **2026-06-16** [`2dd449ce5e`](https://github.com/sgl-project/sglang/commit/2dd449ce5e) [#27765](https://github.com/sgl-project/sglang/pull/27765)
  [AMD-miles] add amd-miles daily docker build workflow (#27765)
  _Files: `.github/workflows/release-docker-amd-miles-rocm700-nightly.yml`, `.github/workflows/release-docker-amd-miles-rocm720-nightly.yml`_
- **2026-06-15** [`19e85868f6`](https://github.com/sgl-project/sglang/commit/19e85868f6) [#28313](https://github.com/sgl-project/sglang/pull/28313)
  [AMD] Point AITER scout at amd/aiter-ci (#28313)
  _Files: `.github/workflows/amd-aiter-scout.yml`_
- **2026-06-15** [`9864059e2b`](https://github.com/sgl-project/sglang/commit/9864059e2b) [#28249](https://github.com/sgl-project/sglang/pull/28249)
  [AMD] Update AITER commit (#28249)
  _Files: `docker/rocm.Dockerfile`_
- **2026-06-15** [`c127ba6483`](https://github.com/sgl-project/sglang/commit/c127ba6483) [#28214](https://github.com/sgl-project/sglang/pull/28214)
  [AMD] ci: fix scheduled AMD runs startup failure when calling extra-a suite (#28214)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`_

## Scheduler / Batching  (14 commits)

- **2026-06-21** [`2552b860a3`](https://github.com/sgl-project/sglang/commit/2552b860a3) [#28337](https://github.com/sgl-project/sglang/pull/28337)
  [AMD][bugfix] Place TBO cuda-graph num_token_non_padded buffer on model devices (#28337)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `test/registered/unit/batch_overlap/test_tbo_cuda_graph_num_token_device.py`_
- **2026-06-20** [`45d203fb08`](https://github.com/sgl-project/sglang/commit/45d203fb08) [#28694](https://github.com/sgl-project/sglang/pull/28694)
  Fix tokenizer state cleanup on dispatch failure (#28694)
  _Files: `python/sglang/benchmark/one_batch_server.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
- **2026-06-19** [`3ed46f599f`](https://github.com/sgl-project/sglang/commit/3ed46f599f) [#28633](https://github.com/sgl-project/sglang/pull/28633)
  [core] Don't force seq_lens_cpu publication under piecewise CUDA graph (#28633)
  _Files: `python/sglang/srt/managers/overlap_utils.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-06-19** [`88c261c3f3`](https://github.com/sgl-project/sglang/commit/88c261c3f3) [#28532](https://github.com/sgl-project/sglang/pull/28532)
  Fix IndexCache PP topk handoff (#28532)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+3 more__
- **2026-06-19** [`941a11ada3`](https://github.com/sgl-project/sglang/commit/941a11ada3) [#26003](https://github.com/sgl-project/sglang/pull/26003)
  [HiCache] refactor: remove unused transfer buffer (#26003)
  _Files: `python/sglang/srt/managers/cache_controller.py`_
- **2026-06-19** [`ef01618dfb`](https://github.com/sgl-project/sglang/commit/ef01618dfb) [#28573](https://github.com/sgl-project/sglang/pull/28573)
  support MPServer and embedded server for granian to enable muti tokenizer worker (#28573)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-06-18** [`8f6d9ef9a5`](https://github.com/sgl-project/sglang/commit/8f6d9ef9a5) [#28607](https://github.com/sgl-project/sglang/pull/28607)
  [misc] Drop redundant req_pool_indices_cpu guards; fold hisparse into GLM-5.1 e2e (#28607)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/8-gpu-models/test_dsa_models_hisparse.py`, `test/registered/models_e2e/test_dsa_glm5_hisparse.py`, `test/registered/unit/managers/test_schedule_batch_req_pool_indices.py`_
- **2026-06-18** [`c208a96a7d`](https://github.com/sgl-project/sglang/commit/c208a96a7d) [#28514](https://github.com/sgl-project/sglang/pull/28514)
  Fix ScheduleBatch req pool CPU metadata (#28514)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_schedule_batch_req_pool_indices.py`_
- **2026-06-17** [`7fd63f4cf2`](https://github.com/sgl-project/sglang/commit/7fd63f4cf2) [#28408](https://github.com/sgl-project/sglang/pull/28408)
  Remove stale load collection from output streaming hot path (#28408)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-06-17** [`0a28a929dc`](https://github.com/sgl-project/sglang/commit/0a28a929dc) [#28122](https://github.com/sgl-project/sglang/pull/28122)
  [MLX] Add Metal profiling hooks to server profiler (#28122)
  _Files: `python/sglang/srt/hardware_backend/mlx/profiler.py`, `python/sglang/srt/managers/scheduler_components/profiler_manager.py`, `test/registered/unit/hardware_backend/mlx/test_metal_profiler.py`_
- **2026-06-17** [`3bc618485a`](https://github.com/sgl-project/sglang/commit/3bc618485a) [#28491](https://github.com/sgl-project/sglang/pull/28491)
  [Perf] Make latest_output_ids H2D non-blocking in prepare_for_decode (#28491)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-06-16** [`a10eee3d80`](https://github.com/sgl-project/sglang/commit/a10eee3d80) [#28341](https://github.com/sgl-project/sglang/pull/28341)
  [Tokenizer] Fix abort racing server crash when large amount of aborts (#28341)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-06-16** [`799584e173`](https://github.com/sgl-project/sglang/commit/799584e173) [#25643](https://github.com/sgl-project/sglang/pull/25643)
  fix:  get_processor fails when --tokenizer-path lacks model config.json (#25643)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/utils/hf_transformers/processor.py`_
- **2026-06-15** [`cad43d3212`](https://github.com/sgl-project/sglang/commit/cad43d3212) [#28089](https://github.com/sgl-project/sglang/pull/28089)
  [CI] Reclaim leaked /dev/shm segments on server startup (#28089)
  _Files: `python/sglang/srt/distributed/device_communicators/shm_broadcast.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/utils/cuda_ipc_transport_utils.py` _+3 more__

## Tensor / Data Parallel  (13 commits)

- **2026-06-22** [`62b3c8e177`](https://github.com/sgl-project/sglang/commit/62b3c8e177) [#28531](https://github.com/sgl-project/sglang/pull/28531)
  [Intel GPU] Guard tvm_ffi import in dsv4 online mtp module under TYPE_CHECKING to fix import error on XPU (#28531)
  _Files: `python/sglang/jit_kernel/dsv4/online_c128_mtp.py`_
- **2026-06-21** [`54b9b9d0c9`](https://github.com/sgl-project/sglang/commit/54b9b9d0c9) [#28812](https://github.com/sgl-project/sglang/pull/28812)
  Remove threading atexit monkey patch (#28812)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py`_
- **2026-06-19** [`7c505c2927`](https://github.com/sgl-project/sglang/commit/7c505c2927) [#28357](https://github.com/sgl-project/sglang/pull/28357)
  [AMD] fix(jit): port kv_canary write/verify/plan kernels to ROCm (#28357)
  _Files: `python/sglang/jit_kernel/csrc/kv_canary/canary_plan_entries.cuh`, `python/sglang/jit_kernel/csrc/kv_canary/canary_verify.cuh`, `python/sglang/jit_kernel/csrc/kv_canary/canary_write.cuh`, `test/registered/jit/kv_canary/test_const_sync.py` _+9 more__
- **2026-06-18** [`f83e4d5968`](https://github.com/sgl-project/sglang/commit/f83e4d5968) [#28383](https://github.com/sgl-project/sglang/pull/28383)
  refactor(runner): unify eager-forward DP/MLP-sync padding into one helper (#28383)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-06-18** [`cf93712937`](https://github.com/sgl-project/sglang/commit/cf93712937) [#28598](https://github.com/sgl-project/sglang/pull/28598)
  [misc] Share bench HTTP-client base-URL resolution with IPv6-compatible formatting (#28598)
  _Files: `python/sglang/bench_serving.py`, `python/sglang/benchmark/endpoint.py`, `python/sglang/srt/utils/network.py`, `python/sglang/test/send_one.py`_
- **2026-06-18** [`d2b5488392`](https://github.com/sgl-project/sglang/commit/d2b5488392) [#28592](https://github.com/sgl-project/sglang/pull/28592)
  [misc] Centralize bench launch-vs-connect into a reusable acquire_endpoint (#28592)
  _Files: `python/sglang/benchmark/endpoint.py`, `python/sglang/test/bench_one_batch_server_internal.py`_
- **2026-06-18** [`74e2e48c82`](https://github.com/sgl-project/sglang/commit/74e2e48c82) [#26385](https://github.com/sgl-project/sglang/pull/26385)
  Introduce CpuDeviceMixin and CpuSRTPlatform (#26385)
  _Files: `docs_new/docs/hardware-platforms/plugin.mdx`, `python/sglang/srt/platforms/__init__.py`, `python/sglang/srt/platforms/cpu.py`, `test/registered/unit/platforms/test_platform_interface.py`_
- **2026-06-18** [`343aeeef39`](https://github.com/sgl-project/sglang/commit/343aeeef39) [#28400](https://github.com/sgl-project/sglang/pull/28400)
  [Model] Laguna: support per-element output gating (#28400)
  _Files: `python/sglang/srt/configs/laguna.py`, `python/sglang/srt/models/laguna.py`_
- **2026-06-16** [`00081a00d5`](https://github.com/sgl-project/sglang/commit/00081a00d5) [#28448](https://github.com/sgl-project/sglang/pull/28448)
  docs(cookbook): tune GLM-5.2 MTP to 5-1-6 and simplify launch flags (#28448)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs_new/src/snippets/_deployment.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`, `docs_new/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-06-15** [`14f6348524`](https://github.com/sgl-project/sglang/commit/14f6348524) [#28349](https://github.com/sgl-project/sglang/pull/28349)
  [Fix] Demote OpenAIServingResponses init failure log to one-line WARNING (#28349)
  _Files: `python/sglang/srt/entrypoints/http_server.py`_
- **2026-06-15** [`7221be2cec`](https://github.com/sgl-project/sglang/commit/7221be2cec) [#28340](https://github.com/sgl-project/sglang/pull/28340)
  feat(cookbook): MTP --max-running-requests callout + skill sync (#28340)
  _Files: `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`, `docs_new/src/snippets/_deployment.jsx` _+1 more__
- **2026-06-15** [`33f99831f8`](https://github.com/sgl-project/sglang/commit/33f99831f8) [#28207](https://github.com/sgl-project/sglang/pull/28207)
  docs(minimax-m3): refresh B200 benchmarks (tp8, piecewise) + add GPQA (#28207)
  _Files: `docs_new/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx`, `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`_
- **2026-06-15** [`69b02ea68a`](https://github.com/sgl-project/sglang/commit/69b02ea68a) [#24548](https://github.com/sgl-project/sglang/pull/24548)
  [Distributed] Guard torch symm mem all-reduce sizes (#24548)
  _Files: `python/sglang/srt/distributed/device_communicators/torch_symm_mem.py`, `python/sglang/srt/distributed/parallel_state.py`_

## KV Cache / Memory  (13 commits)

- **2026-06-21** [`e6722c751b`](https://github.com/sgl-project/sglang/commit/e6722c751b) [#28779](https://github.com/sgl-project/sglang/pull/28779)
  [Feature] Add graceful scheduler shutdown; free hisparse host buffer on exit (#28779)
  _Files: `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+3 more__
- **2026-06-21** [`7f67965b4d`](https://github.com/sgl-project/sglang/commit/7f67965b4d) [#26923](https://github.com/sgl-project/sglang/pull/26923)
  [BugFix] NCCL deadlock in HiCache writing_check by making all_reduce unconditional (#26923)
  _Files: `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`_
- **2026-06-20** [`28e2096d1c`](https://github.com/sgl-project/sglang/commit/28e2096d1c) [#28161](https://github.com/sgl-project/sglang/pull/28161)
  [sgl] wire SGLANG_OPT_SWA_RELEASE_LEAF_LOCK_AFTER_WINDOW on Unified Cache. (#28161)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-06-19** [`2ad9a5b576`](https://github.com/sgl-project/sglang/commit/2ad9a5b576) [#28726](https://github.com/sgl-project/sglang/pull/28726)
  [UnifiedTree] Use dense model for HiCache+CP KL tests  (#28726)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_cp.py`_
- **2026-06-19** [`6b7ecca663`](https://github.com/sgl-project/sglang/commit/6b7ecca663) [#28434](https://github.com/sgl-project/sglang/pull/28434)
  [HiCache]Support hybrid pool staged H2D kernel (#28434)
  _Files: `python/sglang/jit_kernel/hicache.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` _+8 more__
- **2026-06-18** [`867707f1f2`](https://github.com/sgl-project/sglang/commit/867707f1f2) [#28627](https://github.com/sgl-project/sglang/pull/28627)
  [UnifiedTree]: move some kl test from base to extra stage (#28627)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_hicache_pp_kl.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_cp.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dsv4.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mamba.py`_
- **2026-06-18** [`b7ae7149e8`](https://github.com/sgl-project/sglang/commit/b7ae7149e8) [#27291](https://github.com/sgl-project/sglang/pull/27291)
  [HiCache] Fix SWA L3 cache miss due to a prefetch/hit len mismatch (#27291)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dsv4.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mamba.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_nightly.py`_
- **2026-06-17** [`093908d4c0`](https://github.com/sgl-project/sglang/commit/093908d4c0) [#28371](https://github.com/sgl-project/sglang/pull/28371)
  [LoRA] Fix chunked SGMV (csgmv) CUDA graph segment replay (#28371)
  _Files: `python/sglang/srt/lora/backend/chunked_backend.py`, `python/sglang/srt/lora/triton_ops/chunked_embedding_lora_a.py`, `python/sglang/srt/lora/triton_ops/chunked_sgmv_expand.py`, `python/sglang/srt/lora/triton_ops/chunked_sgmv_shrink.py` _+3 more__
- **2026-06-16** [`78b6a4fabf`](https://github.com/sgl-project/sglang/commit/78b6a4fabf) [#28389](https://github.com/sgl-project/sglang/pull/28389)
  [UnifiedTree]: Clean up some unused dead code. (#28389)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-06-16** [`6c908b3a3a`](https://github.com/sgl-project/sglang/commit/6c908b3a3a) [#28375](https://github.com/sgl-project/sglang/pull/28375)
  [UnifiedTree]: Replace anonymous tuples with NamedTuples in UnifiedRadixCache (#28375)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-06-16** [`e068355831`](https://github.com/sgl-project/sglang/commit/e068355831) [#23994](https://github.com/sgl-project/sglang/pull/23994)
  [spec decoding] supports step 0 in adaptive spec decoding (updating draft kv cache without draft decoding) (#23994)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/speculative/adaptive_spec_params.py`, `python/sglang/srt/speculative/draft_utils.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` _+2 more__
- **2026-06-16** [`b5bcd76a41`](https://github.com/sgl-project/sglang/commit/b5bcd76a41) [#21631](https://github.com/sgl-project/sglang/pull/21631)
  [HiCache & JIT Kernel] Refactoring HiCache Write-Back Kernel (#21631)
  _Files: `benchmark/hicache/bench_hicache_write_back.py`, `python/sglang/jit_kernel/csrc/kvcacheio/hicache.cuh`, `python/sglang/jit_kernel/csrc/kvcacheio/relayout.cuh`, `python/sglang/jit_kernel/csrc/kvcacheio/staged_write_back.cuh` _+8 more__
- **2026-06-15** [`e985422b2b`](https://github.com/sgl-project/sglang/commit/e985422b2b) [#27863](https://github.com/sgl-project/sglang/pull/27863)
  [Fix][MTP][MM] Fix EAGLE v2 chunked-prefill next-token chain crash on multimodal models due to placeholder tokens (#27863)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_

## Models  (5 commits)

- **2026-06-22** [`4e1d25117b`](https://github.com/sgl-project/sglang/commit/4e1d25117b) [#28621](https://github.com/sgl-project/sglang/pull/28621)
  [NPU] update best practice docs from testcase (#28621)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_r1.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_v3_2.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/glm5_1.mdx` _+10 more__
- **2026-06-22** [`93553a67a3`](https://github.com/sgl-project/sglang/commit/93553a67a3) [#27893](https://github.com/sgl-project/sglang/pull/27893)
  [NPU] [DOC] Create deployment tutorials for mainstream models on Ascend NPU (#27893)
  _Files: `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_deepseek_example.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_faq.mdx` _+30 more__
- **2026-06-21** [`643ee748c6`](https://github.com/sgl-project/sglang/commit/643ee748c6) [#28785](https://github.com/sgl-project/sglang/pull/28785)
  [PP] Pass DSA topk through PP warmup proxy buffers (#28785)
  _Files: `python/sglang/srt/model_executor/runner/base_runner.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`, `python/sglang/srt/models/deepseek_v2.py`_
- **2026-06-18** [`b55cf4382d`](https://github.com/sgl-project/sglang/commit/b55cf4382d) [#28613](https://github.com/sgl-project/sglang/pull/28613)
  docs: add DeepSeek-V4 compressed state dtype tip (#28613)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`_
- **2026-06-17** [`732b81d5b9`](https://github.com/sgl-project/sglang/commit/732b81d5b9) [#28483](https://github.com/sgl-project/sglang/pull/28483)
  [Fix] DeepSeek-OCR-2 bench_serving: fix processor loading (#28483)
  _Files: `python/sglang/benchmark/utils.py`_

## CI / Build  (4 commits)

- **2026-06-19** [`3a574846ff`](https://github.com/sgl-project/sglang/commit/3a574846ff) [#28738](https://github.com/sgl-project/sglang/pull/28738)
  [CI] Publish 4-GPU nightly profiler traces (#28738)
  _Files: `.github/workflows/nightly-test-nvidia.yml`_
- **2026-06-19** [`c9c2445146`](https://github.com/sgl-project/sglang/commit/c9c2445146) [#28741](https://github.com/sgl-project/sglang/pull/28741)
  [CI] Bump actions/github-script to v8 (Node 24 runtime) (#28741)
  _Files: `.github/actions/check-pr-test-health/action.yml`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/close-inactive-issues.yml`, `.github/workflows/pr-gate.yml` _+1 more__
- **2026-06-19** [`0146692cc9`](https://github.com/sgl-project/sglang/commit/0146692cc9) [#28721](https://github.com/sgl-project/sglang/pull/28721)
  [CI] Fail fast on empty install_script in Rerun Test workflow (#28721)
  _Files: `.github/workflows/rerun-test.yml`_
- **2026-06-17** [`27291118b9`](https://github.com/sgl-project/sglang/commit/27291118b9) [#28402](https://github.com/sgl-project/sglang/pull/28402)
  Upgrade sgl-deep-gemm to 0.1.3 (#28402)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`_

## Serving / API  (3 commits)

- **2026-06-22** [`018d0c21dc`](https://github.com/sgl-project/sglang/commit/018d0c21dc) [#28522](https://github.com/sgl-project/sglang/pull/28522)
  [Docs] Add Anthropic-compatible API documentation (#28522)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs_new/docs.json`, `docs_new/docs/basic_usage/anthropic_api.mdx`, `docs_new/docs/basic_usage/openai_api.mdx` _+1 more__
- **2026-06-21** [`b4dda8b3ce`](https://github.com/sgl-project/sglang/commit/b4dda8b3ce) [#26773](https://github.com/sgl-project/sglang/pull/26773)
  fix(anthropic): handle mid-conversation system messages (#26773)
  _Files: `python/sglang/srt/entrypoints/anthropic/protocol.py`, `test/registered/openai_server/basic/test_anthropic_server.py`, `test/registered/unit/entrypoints/anthropic/test_serving.py`_
- **2026-06-16** [`265202cda2`](https://github.com/sgl-project/sglang/commit/265202cda2) [#28035](https://github.com/sgl-project/sglang/pull/28035)
  fix(openai): validate assistant tool call arguments before chat template (#28035)
  _Files: `python/sglang/srt/entrypoints/openai/encoding_dsv32.py`, `python/sglang/srt/entrypoints/openai/encoding_dsv4.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_

## Structured Output  (1 commits)

- **2026-06-18** [`53318911ca`](https://github.com/sgl-project/sglang/commit/53318911ca) [#28567](https://github.com/sgl-project/sglang/pull/28567)
  Add get_parallel(): a structured accessor for parallel-topology state (#28567)

---
_Generated 2026-06-22 13:43 UTC_