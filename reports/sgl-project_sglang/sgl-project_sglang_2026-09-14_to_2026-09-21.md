# sgl-project/sglang — Weekly Change Report
**Period:** 2026-09-14 → 2026-09-21  |  **Total commits:** 406

## ✨ New Features This Week

- **2026-09-21** [#40577](https://github.com/sgl-project/sglang/pull/40577) — [Docs][NPU] Add MiMo-V2.5-Pro FP4 DFlash best practice on Ascend NPU (#40577)
- **2026-09-21** [#40575](https://github.com/sgl-project/sglang/pull/40575) — [NPU] [DOC] Add kimi k3 cookbook for 950PR/DT Series (#40575)
- **2026-09-21** [#40532](https://github.com/sgl-project/sglang/pull/40532) — [sgl-router] Add SGLang-compatible DeepSeek V4.1 Flash rendering (#40532)
- **2026-09-21** [#40390](https://github.com/sgl-project/sglang/pull/40390) — [sgl-router] Add Kimi-K3 rendering with SGLang parity (#40390)
- **2026-09-21** [#40113](https://github.com/sgl-project/sglang/pull/40113) — [AMD][DI][CI] Add a SPUR cluster profile to AMD DI CI  (#40113)
- **2026-09-21** [#29189](https://github.com/sgl-project/sglang/pull/29189) — [Feature] Gigachat 3.5 support (#29189)
- **2026-09-21** [#32792](https://github.com/sgl-project/sglang/pull/32792) — [XPU]Enable HiSparse hierarchical sparse KV cache on Intel XPU (#32792)
- **2026-09-21** [#33649](https://github.com/sgl-project/sglang/pull/33649) — Update to the cookbook for XPU-supported models (#33649)
- **2026-09-21** [#36187](https://github.com/sgl-project/sglang/pull/36187) — [npu]add chunk gdn kernel and unify ssm state layout for ascend gdn backend (#36187)
- **2026-09-21** [#40487](https://github.com/sgl-project/sglang/pull/40487) — [diffusion] docs: add verified DGX Spark recipe for Qwen-Image 2.1 (#40487)
- _…and 78 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-21** [`b86a30afba`](https://github.com/sgl-project/sglang/commit/b86a30afba) [#40113](https://github.com/sgl-project/sglang/pull/40113) — [AMD][DI][CI] Add a SPUR cluster profile to AMD DI CI  (#40113)
- **2026-09-20** [`e54009240a`](https://github.com/sgl-project/sglang/commit/e54009240a) [#38901](https://github.com/sgl-project/sglang/pull/38901) — [AMD][DSV4] feat: enable DSpark with fp8 unified_kv on gfx950 (#38901)
- **2026-09-20** [`59dd2fc734`](https://github.com/sgl-project/sglang/commit/59dd2fc734) [#39837](https://github.com/sgl-project/sglang/pull/39837) — [2/N] [Kernel] Fuse padding-preserving HiSparse slot translation (#39837)
- **2026-09-19** [`2305242f51`](https://github.com/sgl-project/sglang/commit/2305242f51) [#40205](https://github.com/sgl-project/sglang/pull/40205) — [AMD][DSV4] fix: skip compressed-KV metadata on the draft worker in the HIP radix backend (#40205)
- **2026-09-19** [`c5326d28a3`](https://github.com/sgl-project/sglang/commit/c5326d28a3) [#39968](https://github.com/sgl-project/sglang/pull/39968) — [AMD] dsv4: pick kv_splits per index stream, not by occupancy alone (#39968)
- **2026-09-19** [`993d1fccba`](https://github.com/sgl-project/sglang/commit/993d1fccba) [#37152](https://github.com/sgl-project/sglang/pull/37152) — [ROCm] Widen the HiCache JIT copy rounds and enable the K-only host pool (#37152)
- **2026-09-19** [`0b0d2c257a`](https://github.com/sgl-project/sglang/commit/0b0d2c257a) [#40325](https://github.com/sgl-project/sglang/pull/40325) — [Fix] Repair CI fixtures and ROCm speculative tree device checks (#40325)
- **2026-09-19** [`986959e3c4`](https://github.com/sgl-project/sglang/commit/986959e3c4) [#40197](https://github.com/sgl-project/sglang/pull/40197) — [Refactor] Deduplicate kernel helpers and remove unused code (#40197)
- **2026-09-18** [`cd4dd81c22`](https://github.com/sgl-project/sglang/commit/cd4dd81c22) [#40186](https://github.com/sgl-project/sglang/pull/40186) — [AMD][DSV4] fix: drop shadowing local get_exec import that breaks model startup on ROCm (#40186)
- **2026-09-18** [`45938a24ae`](https://github.com/sgl-project/sglang/commit/45938a24ae) [#40148](https://github.com/sgl-project/sglang/pull/40148) — [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260916, use HIP Top-K (#40148)
- **2026-09-18** [`2dee23a876`](https://github.com/sgl-project/sglang/commit/2dee23a876) [#35573](https://github.com/sgl-project/sglang/pull/35573) — [ROCm][diffusion] Enable fused qk norm and rope on ROCm (#35573)
- **2026-09-18** [`f65c70bb7d`](https://github.com/sgl-project/sglang/commit/f65c70bb7d) [#40033](https://github.com/sgl-project/sglang/pull/40033) — [Kernel] Move CUDA and ROCm speculative kernels to JIT (#40033)
- **2026-09-17** [`7bc9152447`](https://github.com/sgl-project/sglang/commit/7bc9152447) [#39966](https://github.com/sgl-project/sglang/pull/39966) — [Test] Consolidate kernel tests under plural kernels tree (#39966)
- **2026-09-17** [`1f0c73e9bd`](https://github.com/sgl-project/sglang/commit/1f0c73e9bd) [#39921](https://github.com/sgl-project/sglang/pull/39921) — [DSV4] Generalize attention metadata, sparse prefill, and KV pool over compress ratios (#39921)
- **2026-09-17** [`4f52a27563`](https://github.com/sgl-project/sglang/commit/4f52a27563) [#35123](https://github.com/sgl-project/sglang/pull/35123) — [AMD] Fix DSV4 FP4 dequant path for AITER on ROCm (#35123)
- **2026-09-17** [`6c73368c32`](https://github.com/sgl-project/sglang/commit/6c73368c32) [#37778](https://github.com/sgl-project/sglang/pull/37778) — [AMD][DSV4] Enable hicache on deepseek-v4 fp8 unified attn (#37778)
- **2026-09-17** [`1f60ddef5d`](https://github.com/sgl-project/sglang/commit/1f60ddef5d) [#28403](https://github.com/sgl-project/sglang/pull/28403) — [PD] Introduce runtime role switching between prefill and decode (#28403)
- **2026-09-17** [`11c35b8433`](https://github.com/sgl-project/sglang/commit/11c35b8433) [#38878](https://github.com/sgl-project/sglang/pull/38878) — [AMD] Load fused shared experts for Qwen4-Exp and Qwen3.5 MTP (#38878)
- **2026-09-17** [`2d08cc5ede`](https://github.com/sgl-project/sglang/commit/2d08cc5ede) [#38184](https://github.com/sgl-project/sglang/pull/38184) — [AMD][Spec] Enable GDN ReplaySSM target-verify on ROCm (#38184)
- **2026-09-17** [`71ef869ece`](https://github.com/sgl-project/sglang/commit/71ef869ece) [#39513](https://github.com/sgl-project/sglang/pull/39513) — [AMD][Bugfix] Fix vattn_asm HIP error 709 under CUDA graph capture on ROCm 10 (#39513)
- **2026-09-17** [`fa8d22e665`](https://github.com/sgl-project/sglang/commit/fa8d22e665) [#39910](https://github.com/sgl-project/sglang/pull/39910) — [AMD][DSV4] Allow moe_a2a_backend='mori' with DSpark + dp attention (#39910)
- **2026-09-17** [`241a5b9823`](https://github.com/sgl-project/sglang/commit/241a5b9823) [#36576](https://github.com/sgl-project/sglang/pull/36576) — MiniMax-M3: allow shared-experts fusion on ROCm gfx942 and newer (#36576)
- **2026-09-17** [`7780882f18`](https://github.com/sgl-project/sglang/commit/7780882f18) [#39875](https://github.com/sgl-project/sglang/pull/39875) — [AMD][bugfix] Fix dsv4 server launch (#39875)
- **2026-09-16** [`a813224e78`](https://github.com/sgl-project/sglang/commit/a813224e78) [#37810](https://github.com/sgl-project/sglang/pull/37810) — [ROCm][DSV4] Enable breakable CUDA graph prefill (#37810)
- **2026-09-16** [`a3bf25dc62`](https://github.com/sgl-project/sglang/commit/a3bf25dc62) [#39763](https://github.com/sgl-project/sglang/pull/39763) — [AMD] Clamp MORI intranode grid GPUs (#39763)
- **2026-09-16** [`5a0c1e21e9`](https://github.com/sgl-project/sglang/commit/5a0c1e21e9) [#37740](https://github.com/sgl-project/sglang/pull/37740) — [AMD] Preserve deterministic inference when Lean Attention is enabled (#37740)
- **2026-09-16** [`2cbfaefbf9`](https://github.com/sgl-project/sglang/commit/2cbfaefbf9) [#38453](https://github.com/sgl-project/sglang/pull/38453) — [AMD] Avoid the FP8 wo_a path when the weight is BF16 (#38453)
- **2026-09-16** [`f60652a43e`](https://github.com/sgl-project/sglang/commit/f60652a43e) [#39702](https://github.com/sgl-project/sglang/pull/39702) — [AMD] Update deepseek-v4 PDI and cache policy setting for agentic workload (#39702)
- **2026-09-16** [`444b29c932`](https://github.com/sgl-project/sglang/commit/444b29c932) [#39293](https://github.com/sgl-project/sglang/pull/39293) — [Diffusion] Clean up obsolete worker plumbing, dead helpers, and tests (#39293)
- **2026-09-16** [`954bb6804a`](https://github.com/sgl-project/sglang/commit/954bb6804a) [#39547](https://github.com/sgl-project/sglang/pull/39547) — [AMD][bugfix] Fix DSV4 MTP crash (#39547)
- **2026-09-16** [`6331e43081`](https://github.com/sgl-project/sglang/commit/6331e43081) [#39631](https://github.com/sgl-project/sglang/pull/39631) — [AMD] Prefer HIP Top-K for GLM-5.x on ROCm (#39631)
- **2026-09-16** [`a9bb4d7d45`](https://github.com/sgl-project/sglang/commit/a9bb4d7d45) [#39572](https://github.com/sgl-project/sglang/pull/39572) — [AMD] Align Qwen3.5 MI355X HiCache cookbook with kernel / page_first (#39572)
- **2026-09-16** [`f920be4b09`](https://github.com/sgl-project/sglang/commit/f920be4b09) [#39155](https://github.com/sgl-project/sglang/pull/39155) — [AMD] GLM-5.2 NextN: cast draft fused MoE to per-channel FP8 (#39155)
- **2026-09-16** [`7eedd57ab0`](https://github.com/sgl-project/sglang/commit/7eedd57ab0) [#37134](https://github.com/sgl-project/sglang/pull/37134) — [ROCm] Fix EAGLE spec-decode verify silently sampling greedy on HIP (#37134)
- **2026-09-15** [`87c9f78e99`](https://github.com/sgl-project/sglang/commit/87c9f78e99) [#39584](https://github.com/sgl-project/sglang/pull/39584) — [Fix][PD] Give prefill and decode their own RDMA NICs in disaggregation tests (#39584)
- **2026-09-15** [`03ea13a545`](https://github.com/sgl-project/sglang/commit/03ea13a545) [#38632](https://github.com/sgl-project/sglang/pull/38632) — [AMD][CI] Consolidate AMD workflows and retire ROCm 7.0 CI (#38632)
- **2026-09-14** [`0163f8ff74`](https://github.com/sgl-project/sglang/commit/0163f8ff74) [#35233](https://github.com/sgl-project/sglang/pull/35233) — [AMD] Fix registered HiCache host pointer aliases (#35233)
- **2026-09-14** [`242d8a70c0`](https://github.com/sgl-project/sglang/commit/242d8a70c0) [#39406](https://github.com/sgl-project/sglang/pull/39406) — [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260913, enable TOPK_V2 (#39406)
- **2026-09-14** [`5aa9b8fb3e`](https://github.com/sgl-project/sglang/commit/5aa9b8fb3e) [#37413](https://github.com/sgl-project/sglang/pull/37413) — [AMD][DSV4] feat: enable fp8 two-pool unified_kv on gfx950 (#37413)
- **2026-09-14** [`95140a7b0c`](https://github.com/sgl-project/sglang/commit/95140a7b0c) [#39396](https://github.com/sgl-project/sglang/pull/39396) — [docs] DeepSeek-V4: MI355X PD disaggregation recipes for all three strategies (#39396)
- **2026-09-14** [`5200508b0f`](https://github.com/sgl-project/sglang/commit/5200508b0f) [#32888](https://github.com/sgl-project/sglang/pull/32888) — [AMD][gfx95] Fill the chunked-prefill compute budget exactly (#32888)
- **2026-09-14** [`3eeb7d37f9`](https://github.com/sgl-project/sglang/commit/3eeb7d37f9) [#39172](https://github.com/sgl-project/sglang/pull/39172) — [AMD] gfx950 assembly attention: length-aware split-KV for dynamic workload (#39172)
- **2026-09-14** [`ce66ba2844`](https://github.com/sgl-project/sglang/commit/ce66ba2844) [#39360](https://github.com/sgl-project/sglang/pull/39360) — [AMD] Fix AITER FP8-Q unified-attention Test (#39360)
- **2026-09-14** [`edf9584be9`](https://github.com/sgl-project/sglang/commit/edf9584be9) [#39356](https://github.com/sgl-project/sglang/pull/39356) — [AMD][CI] Disable Wave attention test file on ROCm 10 (#39356)
- **2026-09-14** [`2f5cc8e33e`](https://github.com/sgl-project/sglang/commit/2f5cc8e33e) [#39358](https://github.com/sgl-project/sglang/pull/39358) — [AMD] Align Qwen3.5 MI355X cookbook with AttnFP8-V2 and HiCache direct / page_first_direct (#39358)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-09-21 |
| [#37813](https://github.com/sgl-project/sglang/issues/37813) | [Tracking] GLM-5.3-Flash on SM120: required fixes, carry status and re | — | 2026-09-21 |
| [#39499](https://github.com/sgl-project/sglang/issues/39499) | [Roadmap] SGLang dLLM Serving | — | 2026-09-21 |
| [#40574](https://github.com/sgl-project/sglang/issues/40574) | [Feature][DSv4.1] Tracking: every backend's two-level candidate indexe | — | 2026-09-21 |
| [#40232](https://github.com/sgl-project/sglang/issues/40232) | [Bug] HiCache staged write-back: the 128 KiB batch path passes registe | — | 2026-09-21 |
| [#40558](https://github.com/sgl-project/sglang/issues/40558) | [Bug] sm_120 - tvm.error.InternalError: Error in function 'TllmGenFmha | — | 2026-09-21 |
| [#40504](https://github.com/sgl-project/sglang/issues/40504) | [Bug] Hardcoded fp32 dtypes in KDA short-convs cause 2x bandwidth wast | — | 2026-09-21 |
| [#40522](https://github.com/sgl-project/sglang/issues/40522) | [RFC] Decouple the SWA sidecar page size from the full-attention page  | — | 2026-09-21 |
| [#38515](https://github.com/sgl-project/sglang/issues/38515) | sgl_kernel AOT: rmsnorm NoKernelImage on sm_75 while silu_and_mul / ge | — | 2026-09-20 |
| [#38707](https://github.com/sgl-project/sglang/issues/38707) | [Bug][ROCm] PP + DSA: HIP fault on multi-chunk prefill; failure thresh | — | 2026-09-20 |
| [#34510](https://github.com/sgl-project/sglang/issues/34510) | [Tracking] PD disaggregation shared-protocol unification | — | 2026-09-20 |
| [#33522](https://github.com/sgl-project/sglang/issues/33522) | [Roadmap]Fast Engine Recovery: Weight Cache Daemon | — | 2026-09-20 |
| [#39963](https://github.com/sgl-project/sglang/issues/39963) | [RFC] Asymmetric P/D deployment for DeepSeek-V4.1 Flash | — | 2026-09-20 |
| [#40156](https://github.com/sgl-project/sglang/issues/40156) | [Bug] EAGLE spec-decode: num_token_non_padded is 0 for draft batches,  | — | 2026-09-20 |
| [#23206](https://github.com/sgl-project/sglang/issues/23206) | [RFC] Sglang non-GPU process rust migration | — | 2026-09-19 |
| [#32657](https://github.com/sgl-project/sglang/issues/32657) | [RFC] A Unified KV-Cache Sparsity Framework for Post-Hoc Sparse Attent | — | 2026-09-19 |
| [#40320](https://github.com/sgl-project/sglang/issues/40320) | [Bug] FlashInfer autotune cache is discarded every boot under MoE expe | — | 2026-09-19 |
| [#40305](https://github.com/sgl-project/sglang/issues/40305) | [Feature] Make SGLANG_DEBUG_MEMORY_POOL effective on the default page_ | — | 2026-09-19 |
| [#39173](https://github.com/sgl-project/sglang/issues/39173) | [Bug] DeepSeek-V4.1-Flash + Engram: profiled SPS table (compact ragged | — | 2026-09-19 |
| [#40286](https://github.com/sgl-project/sglang/issues/40286) | [Bug] GLM-5.3-Flash has no usable DSA attention backend on SM121 (DGX  | — | 2026-09-19 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 85 |
| Prefill / Decode Disaggregation | 59 |
| Other | 50 |
| MoE / Expert Parallel | 37 |
| Multimodal | 32 |
| KV Cache / Memory | 27 |
| Scheduler / Batching | 17 |
| Quantization | 15 |
| CI / Build | 13 |
| Triton / Kernels | 13 |
| Tensor / Data Parallel | 11 |
| Docs / Examples | 10 |
| Models | 10 |
| Speculative Decoding | 7 |
| ROCm / AMD | 6 |
| Structured Output | 6 |
| Serving / API | 5 |
| LoRA | 3 |

## Attention / FlashInfer  (85 commits)

- **2026-09-21** [`69d1e5cfe0`](https://github.com/sgl-project/sglang/commit/69d1e5cfe0) [#40577](https://github.com/sgl-project/sglang/pull/40577)
  [Docs][NPU] Add MiMo-V2.5-Pro FP4 DFlash best practice on Ascend NPU (#40577)
  _Files: `docs/docs.json`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/mimo_v2_5_pro.mdx`_
- **2026-09-21** [`0f6761b54f`](https://github.com/sgl-project/sglang/commit/0f6761b54f) [#40532](https://github.com/sgl-project/sglang/pull/40532)
  [sgl-router] Add SGLang-compatible DeepSeek V4.1 Flash rendering (#40532)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/tokenizer/chat_formatter.rs` _+5 more__
- **2026-09-21** [`b63f8416b3`](https://github.com/sgl-project/sglang/commit/b63f8416b3) [#29189](https://github.com/sgl-project/sglang/pull/29189)
  [Feature] Gigachat 3.5 support (#29189)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/supported-models/generative_models.mdx`, `python/sglang/srt/arg_groups/model_overrides/__init__.py`, `python/sglang/srt/arg_groups/model_overrides/gigachat35.py` _+13 more__
- **2026-09-21** [`d20cd9d77f`](https://github.com/sgl-project/sglang/commit/d20cd9d77f) [#32792](https://github.com/sgl-project/sglang/pull/32792)
  [XPU]Enable HiSparse hierarchical sparse KV cache on Intel XPU (#32792)
  _Files: `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/mem_cache/hisparse_memory_pool.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/pool_host/common.py` _+3 more__
- **2026-09-21** [`176dbcb85d`](https://github.com/sgl-project/sglang/commit/176dbcb85d) [#36187](https://github.com/sgl-project/sglang/pull/36187)
  [npu]add chunk gdn kernel and unify ssm state layout for ascend gdn backend (#36187)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`, `test/registered/npu/basic_function/HiCache/test_npu_hicache_mha.py`, `test/registered/npu/basic_function/HiCache/test_npu_hicache_mla.py`_
- **2026-09-20** [`acd20a516e`](https://github.com/sgl-project/sglang/commit/acd20a516e) [#40496](https://github.com/sgl-project/sglang/pull/40496)
  [CI] Give the kernel lane a 5090 suite and move kernel-only tests off the general lane (#40496)
  _Files: `.github/workflows/pr-test-jit-kernel.yml`, `test/registered/e2e/models/test_deepseek_v3_mtp.py`, `test/registered/kernels/ops/attention/test_dsa_metadata.py`, `test/registered/kernels/ops/attention/test_dsa_transform_index.py` _+9 more__
- **2026-09-20** [`d97aed2c90`](https://github.com/sgl-project/sglang/commit/d97aed2c90) [#40163](https://github.com/sgl-project/sglang/pull/40163)
  Fix TopK v2 fallback when 16-block cluster capacity is zero (#40163)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/utils/occupancy.py`, `python/sglang/kernels/ops/attention/dsv4/topk.py`_
- **2026-09-20** [`95521da18d`](https://github.com/sgl-project/sglang/commit/95521da18d) [#40217](https://github.com/sgl-project/sglang/pull/40217)
  [DeepSeek-V4.1] Bound dense prefill indexer memory (#40217)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/candidate_indexer.py`, `python/sglang/srt/layers/attention/dsv4/dense_prefill_indexer.py`, `test/registered/kernels/ops/attention/test_dense_prefill_indexer.py` _+1 more__
- **2026-09-20** [`5f017ffabb`](https://github.com/sgl-project/sglang/commit/5f017ffabb) [#40392](https://github.com/sgl-project/sglang/pull/40392)
  Update test cases and performance testing framework (#40392)
  _Files: `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_gpqa.py`, `test/registered/npu/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in8k_out1k_50ms.py`_
- **2026-09-20** [`0024efa0de`](https://github.com/sgl-project/sglang/commit/0024efa0de) [#40294](https://github.com/sgl-project/sglang/pull/40294)
  [CI] Derive registered-test kind from the registry call instead of the path (#40294)
  _Files: `.pre-commit-config.yaml`, `scripts/lint/check_registered_tests.py`, `scripts/lint/test_check_no_bare_pytest_main.py`, `scripts/lint/test_check_registered_tests.py` _+20 more__
- **2026-09-20** [`2a0cb2f04e`](https://github.com/sgl-project/sglang/commit/2a0cb2f04e) [#40116](https://github.com/sgl-project/sglang/pull/40116)
  [Diffusion][MiniMax-H3] Add SM120 Sage compute for SubBlock sparse attention (#40116)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/README.md`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse_attn.py`, `python/sglang/multimodal_gen/test/unit/test_subblock_sparse_attention.py` _+2 more__
- **2026-09-20** [`dc002c85fc`](https://github.com/sgl-project/sglang/commit/dc002c85fc) [#40427](https://github.com/sgl-project/sglang/pull/40427)
  [Test] Fix OOT DFlash hook test resolving the draft config over the network (#40427)
  _Files: `test/registered/unit/spec/test_oot_dflash_hooks.py`_
- **2026-09-20** [`99a44c88d4`](https://github.com/sgl-project/sglang/commit/99a44c88d4) [#38740](https://github.com/sgl-project/sglang/pull/38740)
  Add out-of-tree DFlash extension points (#38740)
  _Files: `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/platforms/interface.py`, `python/sglang/srt/speculative/dflash_worker_v2.py` _+2 more__
- **2026-09-20** [`9f21fbc34b`](https://github.com/sgl-project/sglang/commit/9f21fbc34b) [#39695](https://github.com/sgl-project/sglang/pull/39695)
  [GLM-5.3-Flash] Reduce KPool planning synchronization and overlap indexer preparation (#39695)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_kpool.py`, `python/sglang/srt/layers/attention/dsa/kpool_plan.py`, `python/sglang/srt/managers/schedule_batch.py` _+5 more__
- **2026-09-20** [`c8eb54c41d`](https://github.com/sgl-project/sglang/commit/c8eb54c41d) [#39688](https://github.com/sgl-project/sglang/pull/39688)
  Fuse GLM-5.3-Flash KDA projections and prefill metadata (#39688)
  _Files: `python/sglang/kernels/ops/attention/fla/kda.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py` _+10 more__
- **2026-09-20** [`dd83b54611`](https://github.com/sgl-project/sglang/commit/dd83b54611) [#40389](https://github.com/sgl-project/sglang/pull/40389)
  Update linear attention code owner directory (#40389)
  _Files: `.github/CODEOWNERS`_
- **2026-09-20** [`59dd2fc734`](https://github.com/sgl-project/sglang/commit/59dd2fc734) [#39837](https://github.com/sgl-project/sglang/pull/39837)
  [2/N] [Kernel] Fuse padding-preserving HiSparse slot translation (#39837)
  _Files: `python/sglang/kernels/ops/kvcache/hisparse_slot_mapping.py`, `python/sglang/srt/mem_cache/hisparse_memory_pool.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`, `test/registered/amd/test_rocm_hisparse_fused_kv_gpu.py` _+3 more__
- **2026-09-20** [`d2f291c934`](https://github.com/sgl-project/sglang/commit/d2f291c934) [#39820](https://github.com/sgl-project/sglang/pull/39820)
  [NPU][DSV4]dsv4 enable cpp (#39820)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_memory_pool.py`, `test/registered/unit/npu/attention/test_npu_ascend_dsv4_backend.py`_
- **2026-09-19** [`7a6c652c77`](https://github.com/sgl-project/sglang/commit/7a6c652c77) [#40135](https://github.com/sgl-project/sglang/pull/40135)
  [HiCache] Auto-size the host pool to fit available host memory (#40135)
  _Files: `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/mem_cache/hicache_auto_size.py`, `python/sglang/srt/mem_cache/host_memory.py` _+9 more__
- **2026-09-19** [`2305242f51`](https://github.com/sgl-project/sglang/commit/2305242f51) [#40205](https://github.com/sgl-project/sglang/pull/40205)
  [AMD][DSV4] fix: skip compressed-KV metadata on the draft worker in the HIP radix backend (#40205)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-09-19** [`c5326d28a3`](https://github.com/sgl-project/sglang/commit/c5326d28a3) [#39968](https://github.com/sgl-project/sglang/pull/39968)
  [AMD] dsv4: pick kv_splits per index stream, not by occupancy alone (#39968)
  _Files: `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/paged_decode.py`, `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/runtime.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-09-19** [`7b67a96640`](https://github.com/sgl-project/sglang/commit/7b67a96640) [#39095](https://github.com/sgl-project/sglang/pull/39095)
  [DSV4] Chunk the indexer MQA logits by query rows under a free-memory budget (#39095)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py`, `python/sglang/srt/layers/attention/mqa_logits_utils.py` _+2 more__
- **2026-09-19** [`993d1fccba`](https://github.com/sgl-project/sglang/commit/993d1fccba) [#37152](https://github.com/sgl-project/sglang/pull/37152)
  [ROCm] Widen the HiCache JIT copy rounds and enable the K-only host pool (#37152)
  _Files: `python/sglang/kernels/jit/csrc/kvcacheio/hicache.cuh`, `python/sglang/kernels/ops/kvcache/hicache.py`, `python/sglang/srt/mem_cache/pool_host/mha.py`, `test/registered/kernels/ops/kvcache/test_hicache.py` _+1 more__
- **2026-09-19** [`d1acbe0746`](https://github.com/sgl-project/sglang/commit/d1acbe0746) [#39957](https://github.com/sgl-project/sglang/pull/39957)
  [DSV4.1] Big fused wo_a quant (#39957)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/wo_a_fused.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/mbarrier.cuh`, `python/sglang/kernels/jit/utils/__init__.py`, `python/sglang/kernels/jit/utils/compile/__init__.py` _+8 more__
- **2026-09-19** [`0b0d2c257a`](https://github.com/sgl-project/sglang/commit/0b0d2c257a) [#40325](https://github.com/sgl-project/sglang/pull/40325)
  [Fix] Repair CI fixtures and ROCm speculative tree device checks (#40325)
  _Files: `python/sglang/kernels/jit/csrc/speculative/tree.cuh`, `test/registered/kernels/ops/attention/test_q8kv8_sparse_prefill_backend.py`, `test/registered/unit/hardware_backend/mlx/test_metal_profiler.py`, `test/registered/unit/managers/test_disagg_idle_step_counters.py`_
- **2026-09-19** [`5d703de9e4`](https://github.com/sgl-project/sglang/commit/5d703de9e4) [#40304](https://github.com/sgl-project/sglang/pull/40304)
  [HiCache] Size MHA host pools from device row width (#40304)
  _Files: `python/sglang/srt/mem_cache/pool_host/mha.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py`_
- **2026-09-19** [`929230a6f0`](https://github.com/sgl-project/sglang/commit/929230a6f0) [#39088](https://github.com/sgl-project/sglang/pull/39088)
  Fix GLM-OCR MTP multimodal embeddings and positions (#39088)
  _Files: `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/models/glm4v.py`, `python/sglang/srt/models/glm_ocr_nextn.py` _+13 more__
- **2026-09-18** [`d346b214fb`](https://github.com/sgl-project/sglang/commit/d346b214fb) [#36340](https://github.com/sgl-project/sglang/pull/36340)
  feat(kv-cache): support SM100 NVFP4 GenMHA and speculative decoding (#36340)
  _Files: `docs/docs/advanced_features/quantized_kv_cache.mdx`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/arg_groups/pipeline.py` _+15 more__
- **2026-09-18** [`248c202b46`](https://github.com/sgl-project/sglang/commit/248c202b46) [#39859](https://github.com/sgl-project/sglang/pull/39859)
  Use runtime token widths for Triton speculative verification (#39859)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/spec_info.py`, `python/sglang/test/kits/attention_unittest/attention_methods/gdn_attention.py` _+6 more__
- **2026-09-18** [`1b200ffaaa`](https://github.com/sgl-project/sglang/commit/1b200ffaaa) [#40039](https://github.com/sgl-project/sglang/pull/40039)
  [Quant] Serve 32-wide-K ue8m0 block-FP8 linears through the FlashInfer MXFP8 GEMMs (#40039)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/mxfp8_input.py`, `python/sglang/srt/models/deepseek_v4.py` _+3 more__
- **2026-09-18** [`7e6d5cbfac`](https://github.com/sgl-project/sglang/commit/7e6d5cbfac) [#39879](https://github.com/sgl-project/sglang/pull/39879)
  [NPU] Gate DFlash replay metadata refresh behind spec_algorithm check (#39879)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`_
- **2026-09-18** [`4dbba37965`](https://github.com/sgl-project/sglang/commit/4dbba37965) [#39419](https://github.com/sgl-project/sglang/pull/39419)
  Verify the Ling-3.0-flash-VL FP4 lane on H200 and disable shared-expert fusion in quant recipes (#39419)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash-VL.mdx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash-vl-benchmarks.jsx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash-vl.jsx`_
- **2026-09-18** [`f447bb7080`](https://github.com/sgl-project/sglang/commit/f447bb7080) [#39680](https://github.com/sgl-project/sglang/pull/39680)
  [Kernel] Coalesce the KDA CuTe DSL decode state transpose: ~3x faster, bit-identical (#39680)
  _Files: `python/sglang/kernels/ops/attention/cutedsl_kda.py`_
- **2026-09-18** [`f65c70bb7d`](https://github.com/sgl-project/sglang/commit/f65c70bb7d) [#40033](https://github.com/sgl-project/sglang/pull/40033)
  [Kernel] Move CUDA and ROCm speculative kernels to JIT (#40033)
  _Files: `.github/workflows/nightly-test-musa.yml`, `.github/workflows/pr-test-amd.yml`, `.github/workflows/pr-test-musa.yml`, `python/sglang/kernels/aot/CMakeLists.txt` _+25 more__
- **2026-09-17** [`b98a2d1096`](https://github.com/sgl-project/sglang/commit/b98a2d1096) [#40036](https://github.com/sgl-project/sglang/pull/40036)
  [Docs] GLM-5.3-Flash cookbook: temporarily remove the DCP option (#40036)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-09-17** [`e4cbb28ea1`](https://github.com/sgl-project/sglang/commit/e4cbb28ea1) [#39133](https://github.com/sgl-project/sglang/pull/39133)
  [router] Improve SGLang chat render parity (#39133)
  _Files: `experimental/sgl-router/src/policies/mod.rs`, `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/src/tokenizer/chat_formatter.rs`, `experimental/sgl-router/tests/component/tokenizer/mod.rs` _+12 more__
- **2026-09-17** [`a9fb1c3238`](https://github.com/sgl-project/sglang/commit/a9fb1c3238) [#39427](https://github.com/sgl-project/sglang/pull/39427)
  dsv4(npu): support prefill context parallelism with interleave and zigzag (#39427)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/layers/attention/dsa/dsa_npu_indexer.py` _+8 more__
- **2026-09-17** [`a1b4ec02ae`](https://github.com/sgl-project/sglang/commit/a1b4ec02ae) [#39438](https://github.com/sgl-project/sglang/pull/39438)
  [NPU][Diffusion] FA MXFP8 and modelslim w4a4f8 and w8a8f8 support for Wan2.2 and FLUX (#39438)
  _Files: `docs/docs/sglang-diffusion/environment_variables.mdx`, `python/sglang/multimodal_gen/configs/models/dits/wanvideo.py`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/ascend_fa.py` _+5 more__
- **2026-09-17** [`2d08cc5ede`](https://github.com/sgl-project/sglang/commit/2d08cc5ede) [#38184](https://github.com/sgl-project/sglang/pull/38184)
  [AMD][Spec] Enable GDN ReplaySSM target-verify on ROCm (#38184)
  _Files: `python/sglang/kernels/ops/attention/fla/gdn_replayssm_spec_decode.py`_
- **2026-09-17** [`acfde25d34`](https://github.com/sgl-project/sglang/commit/acfde25d34) [#39870](https://github.com/sgl-project/sglang/pull/39870)
  Carry deferred attention operands and reuse multimodal shared memory (#39870)
  _Files: `python/sglang/srt/layers/radix_attention.py`, `python/sglang/srt/managers/mm_utils.py`, `test/registered/unit/layers/test_radix_attention.py`, `test/registered/unit/managers/test_mm_shm_error_consensus.py`_
- **2026-09-17** [`71ef869ece`](https://github.com/sgl-project/sglang/commit/71ef869ece) [#39513](https://github.com/sgl-project/sglang/pull/39513)
  [AMD][Bugfix] Fix vattn_asm HIP error 709 under CUDA graph capture on ROCm 10 (#39513)
  _Files: `python/sglang/kernels/ops/attention/vattn_asm_gfx950/__init__.py`, `test/registered/amd/test_vattn_segplan_mi35x.py`_
- **2026-09-17** [`fd6f96bf96`](https://github.com/sgl-project/sglang/commit/fd6f96bf96) [#39835](https://github.com/sgl-project/sglang/pull/39835)
  Re-land dp-attention local control broadcast test (#39835)
  _Files: `python/sglang/test/kits/pause_generation_kit.py`, `test/registered/e2e/dp_attn/test_dp_attention_local_control_broadcast.py`_
- **2026-09-17** [`c525ed8f02`](https://github.com/sgl-project/sglang/commit/c525ed8f02) [#39882](https://github.com/sgl-project/sglang/pull/39882)
  [diffusion] fix: preserve explicit attention backends during autotune (#39882)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/test/unit/test_attention_backend_autotune.py`_
- **2026-09-17** [`1c4b130bf7`](https://github.com/sgl-project/sglang/commit/1c4b130bf7) [#39906](https://github.com/sgl-project/sglang/pull/39906)
  [CI] Unify basic and speculative sanity accuracy checks with MMLU (#39906)
  _Files: `python/sglang/test/kits/eval_accuracy_kit.py`, `test/registered/core/test_basic_sanity.py`, `test/registered/core/test_basic_sanity_dflash.py`, `test/registered/core/test_basic_sanity_dspark.py` _+1 more__
- **2026-09-17** [`4fb9b5b5ba`](https://github.com/sgl-project/sglang/commit/4fb9b5b5ba) [#32500](https://github.com/sgl-project/sglang/pull/32500)
  feat(hicache): support NPU Mamba states with FIA and async IO (#32500)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `python/sglang/srt/mem_cache/pool_host/mamba.py`, `python/sglang/srt/mem_cache/pool_host/mha.py`, `test/registered/npu/basic_function/HiCache/test_npu_hicache_mamba.py` _+2 more__
- **2026-09-17** [`4c85172f3a`](https://github.com/sgl-project/sglang/commit/4c85172f3a) [#39089](https://github.com/sgl-project/sglang/pull/39089)
  [HiCache] Back up MXFP8 KV scales in the host pool (#39089)
  _Files: `python/sglang/srt/mem_cache/pool_host/mha.py`, `python/sglang/srt/mem_cache/pool_host/mha_mxfp8.py`, `test/registered/unit/mem_cache/test_mxfp8_mha_pool_host_unit.py`_
- **2026-09-17** [`0443e3179f`](https://github.com/sgl-project/sglang/commit/0443e3179f) [#39124](https://github.com/sgl-project/sglang/pull/39124)
  fix(kda_prefill): fence shared writes before async proxy reads (#39124)
  _Files: `python/sglang/kernels/jit/csrc/attention/kda_prefill.cu`_
- **2026-09-17** [`7780882f18`](https://github.com/sgl-project/sglang/commit/7780882f18) [#39875](https://github.com/sgl-project/sglang/pull/39875)
  [AMD][bugfix] Fix dsv4 server launch (#39875)
  _Files: `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/kv_layout.cuh`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-09-17** [`408d2334c3`](https://github.com/sgl-project/sglang/commit/408d2334c3) [#39664](https://github.com/sgl-project/sglang/pull/39664)
  dsv4.1: mHC computation and compensated projections (#39664)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`_
- **2026-09-16** [`c2443458e1`](https://github.com/sgl-project/sglang/commit/c2443458e1) [#39656](https://github.com/sgl-project/sglang/pull/39656)
  dsv4.1: RoPE and FP4 packing kernels (#39656)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/fp4_indexer_rope.cuh`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_rope.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_rope_fake_quant.py`_
- **2026-09-16** [`35b7589e1a`](https://github.com/sgl-project/sglang/commit/35b7589e1a) [#39671](https://github.com/sgl-project/sglang/pull/39671)
  dsv4.1: candidate indexer library (#39671)
  _Files: `python/sglang/kernels/ops/attention/dsv4/candidate_blocks.py`, `python/sglang/kernels/ops/attention/dsv4/indexer_postprocess.py`, `python/sglang/srt/layers/attention/dsv4/candidate_indexer.py`, `python/sglang/srt/layers/attention/dsv4/candidate_indexer_deep_gemm.py` _+2 more__
- **2026-09-16** [`13d593b6cf`](https://github.com/sgl-project/sglang/commit/13d593b6cf) [#39652](https://github.com/sgl-project/sglang/pull/39652)
  dsv4.1: compression, KV I/O, and metadata kernels (#39652)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c1.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/c2.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh` _+15 more__
- **2026-09-16** [`a813224e78`](https://github.com/sgl-project/sglang/commit/a813224e78) [#37810](https://github.com/sgl-project/sglang/pull/37810)
  [ROCm][DSV4] Enable breakable CUDA graph prefill (#37810)
  _Files: `python/sglang/kernels/ops/attention/dsv4_attn_metadata_kernels.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py` _+4 more__
- **2026-09-16** [`5aaa18207c`](https://github.com/sgl-project/sglang/commit/5aaa18207c) [#39828](https://github.com/sgl-project/sglang/pull/39828)
  Revert "[CI] Add e2e test for dp-attention local control broadcast" (#39828)
  _Files: `test/registered/e2e/dp_attn/test_dp_attention_local_control_broadcast.py`_
- **2026-09-16** [`e7f7447333`](https://github.com/sgl-project/sglang/commit/e7f7447333) [#37615](https://github.com/sgl-project/sglang/pull/37615)
  [kv-shard 2/4] Sharded pools (#37615)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/kv_shard_hooks.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/mem_cache/page_interleave.py` _+4 more__
- **2026-09-16** [`76e06febab`](https://github.com/sgl-project/sglang/commit/76e06febab) [#39437](https://github.com/sgl-project/sglang/pull/39437)
  [CI] Add e2e test for dp-attention local control broadcast (#39437)
  _Files: `test/registered/e2e/dp_attn/test_dp_attention_local_control_broadcast.py`_
- **2026-09-16** [`5a0c1e21e9`](https://github.com/sgl-project/sglang/commit/5a0c1e21e9) [#37740](https://github.com/sgl-project/sglang/pull/37740)
  [AMD] Preserve deterministic inference when Lean Attention is enabled (#37740)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`_
- **2026-09-16** [`faaff1eca8`](https://github.com/sgl-project/sglang/commit/faaff1eca8) [#39648](https://github.com/sgl-project/sglang/pull/39648)
  dsv4.1: Top-k kernels and candidate selection (#39648)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/block_amax.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/candidate_block_table.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/topk_bf16_small.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh` _+8 more__
- **2026-09-16** [`91f691c490`](https://github.com/sgl-project/sglang/commit/91f691c490) [#39646](https://github.com/sgl-project/sglang/pull/39646)
  dsv4.1: standalone kernels and Python wrappers (#39646)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/flashmla_sched_meta.cuh`, `python/sglang/kernels/jit/csrc/gemm/small_gemm_bf16.cuh`, `python/sglang/kernels/jit/csrc/gemm/tiny_gemm.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/gemm/dot_product.cuh` _+21 more__
- **2026-09-16** [`444b29c932`](https://github.com/sgl-project/sglang/commit/444b29c932) [#39293](https://github.com/sgl-project/sglang/pull/39293)
  [Diffusion] Clean up obsolete worker plumbing, dead helpers, and tests (#39293)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/group_coordinator.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/runtime/entrypoints/cli/utils.py`, `python/sglang/multimodal_gen/runtime/launch_server.py` _+16 more__
- **2026-09-16** [`954bb6804a`](https://github.com/sgl-project/sglang/commit/954bb6804a) [#39547](https://github.com/sgl-project/sglang/pull/39547)
  [AMD][bugfix] Fix DSV4 MTP crash (#39547)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-09-16** [`537ac52c5b`](https://github.com/sgl-project/sglang/commit/537ac52c5b) [#39295](https://github.com/sgl-project/sglang/pull/39295)
  [SRT] Clean up no-op compiler pass, dead helpers, and migration tests (#39295)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/compilation/backend.py` _+13 more__
- **2026-09-16** [`c9a8fba991`](https://github.com/sgl-project/sglang/commit/c9a8fba991) [#36534](https://github.com/sgl-project/sglang/pull/36534)
  [DSV4][BCG] Optimize the heavy memory use of C4 Indexer when BCG is enabled (#36534)
  _Files: `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/pipeline.py` _+19 more__
- **2026-09-15** [`4da5599e93`](https://github.com/sgl-project/sglang/commit/4da5599e93) [#39328](https://github.com/sgl-project/sglang/pull/39328)
  Fix first-token metadata and reused attention-layer indexing (#39328)
  _Files: `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/observability/req_time_stats.py`, `test/registered/unit/model_executor/model_runner_components/test_cuda_graph_setup.py`, `test/registered/unit/observability/test_req_time_stats.py`_
- **2026-09-15** [`e4a6b090f4`](https://github.com/sgl-project/sglang/commit/e4a6b090f4) [#39553](https://github.com/sgl-project/sglang/pull/39553)
  [CI] Run test_unified_radix_cache_kl_dcp on cutedsl_mla with bf16 KV cache (#39553)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dcp.py`_
- **2026-09-15** [`8a20062652`](https://github.com/sgl-project/sglang/commit/8a20062652) [#39423](https://github.com/sgl-project/sglang/pull/39423)
  [NPU][Bugfix] Disable pinned memory to fix DeepSeek-V2 DP-attention hang (#39423)
  _Files: `python/sglang/srt/platforms/npu.py`, `test/registered/unit/platforms/test_platform_interface.py`_
- **2026-09-15** [`2c37b90ad6`](https://github.com/sgl-project/sglang/commit/2c37b90ad6) [#39487](https://github.com/sgl-project/sglang/pull/39487)
  [Fix][DCP] Localize widened KV ids in MLA retraction CPU backup/restore (#39487)
  _Files: `python/sglang/srt/layers/dcp/layout.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/pool_host/base.py`, `python/sglang/srt/mem_cache/pool_host/mla.py` _+2 more__
- **2026-09-15** [`bdf8886ad3`](https://github.com/sgl-project/sglang/commit/bdf8886ad3) [#39389](https://github.com/sgl-project/sglang/pull/39389)
  [NPU] [DOC] Rename NPU hardware to Ascend A2/A3 Series product (#39389)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-R1.mdx`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_1.mdx`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx` _+62 more__
- **2026-09-15** [`99060191e7`](https://github.com/sgl-project/sglang/commit/99060191e7) [#36821](https://github.com/sgl-project/sglang/pull/36821)
  [KDA] Support ReplaySSM ring-write in the fused chain-verify kernel (#36821)
  _Files: `benchmark/kernels/bench_kda_verify_sweep.py`, `python/sglang/kernels/ops/attention/fla/fused_kda_conv_recurrent_verify.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `test/registered/kernel/attention/test_kda_fused_verify_backend.py` _+1 more__
- **2026-09-15** [`a23fd557ed`](https://github.com/sgl-project/sglang/commit/a23fd557ed) [#38687](https://github.com/sgl-project/sglang/pull/38687)
  [Kernel] Add OOT dispatch for clamp position (#38687)
  _Files: `python/sglang/kernels/ops/attention/clamp_position.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/kernels/ops/attention/test_clamp_position.py`_
- **2026-09-14** [`0163f8ff74`](https://github.com/sgl-project/sglang/commit/0163f8ff74) [#35233](https://github.com/sgl-project/sglang/pull/35233)
  [AMD] Fix registered HiCache host pointer aliases (#35233)
  _Files: `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h` _+11 more__
- **2026-09-14** [`d72e59508b`](https://github.com/sgl-project/sglang/commit/d72e59508b) [#38346](https://github.com/sgl-project/sglang/pull/38346)
  Reland fix(qsa): clamp the compress gather to the rows (#38346) (#39446)
  _Files: `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`_
- **2026-09-14** [`7465e42b7a`](https://github.com/sgl-project/sglang/commit/7465e42b7a) [#38833](https://github.com/sgl-project/sglang/pull/38833)
  [NPU][CI] Add CANN 9.1.0 and Ascend a5 nightly suites (#38833)
  _Files: `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_fp8_4p_gpqa_a5.py` _+4 more__
- **2026-09-14** [`433c999dd0`](https://github.com/sgl-project/sglang/commit/433c999dd0) [#39403](https://github.com/sgl-project/sglang/pull/39403)
  [NPU][CI] Fix sglang.test.ascend import failure in multi-node e2e pods (#39403)
  _Files: `python/sglang/test/ascend/e2e/run_npu_testcase.sh`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py`, `test/registered/npu/basic_function/dp_attn/test_npu_dp_attention.py`_
- **2026-09-14** [`87db743021`](https://github.com/sgl-project/sglang/commit/87db743021) [#39353](https://github.com/sgl-project/sglang/pull/39353)
  [NPU] Fix device mismatch in SWA mask for DSpark verify graph capture (#39353)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-09-14** [`66c7bc838e`](https://github.com/sgl-project/sglang/commit/66c7bc838e) [#39405](https://github.com/sgl-project/sglang/pull/39405)
  [misc] Revert #38346, #33426, #39061 and #39219 (#39405)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_kda_conv_recurrent_verify.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py` _+5 more__
- **2026-09-14** [`5aa9b8fb3e`](https://github.com/sgl-project/sglang/commit/5aa9b8fb3e) [#37413](https://github.com/sgl-project/sglang/pull/37413)
  [AMD][DSV4] feat: enable fp8 two-pool unified_kv on gfx950 (#37413)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/kernels/ops/attention/dsv4/compress.py`, `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/env_gate.py`, `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/layout.py` _+17 more__
- **2026-09-14** [`3eeb7d37f9`](https://github.com/sgl-project/sglang/commit/3eeb7d37f9) [#39172](https://github.com/sgl-project/sglang/pull/39172)
  [AMD] gfx950 assembly attention: length-aware split-KV for dynamic workload (#39172)
  _Files: `python/sglang/kernels/ops/attention/unified_attention_3d_mtp.py`, `python/sglang/kernels/ops/attention/vattn_asm_gfx950/__init__.py`, `python/sglang/kernels/ops/attention/vattn_asm_gfx950/vattn3_core.s`, `python/sglang/kernels/ops/attention/vattn_asm_gfx950/vred.s` _+2 more__
- **2026-09-14** [`ce66ba2844`](https://github.com/sgl-project/sglang/commit/ce66ba2844) [#39360](https://github.com/sgl-project/sglang/pull/39360)
  [AMD] Fix AITER FP8-Q unified-attention Test (#39360)
  _Files: `test/registered/attention/test_aiter_fp8_q_unified_attention.py`_
- **2026-09-14** [`edf9584be9`](https://github.com/sgl-project/sglang/commit/edf9584be9) [#39356](https://github.com/sgl-project/sglang/pull/39356)
  [AMD][CI] Disable Wave attention test file on ROCm 10 (#39356)
  _Files: `test/registered/attention/test_wave_attention_kernels.py`_
- **2026-09-14** [`2fd835b9c1`](https://github.com/sgl-project/sglang/commit/2fd835b9c1) [#39219](https://github.com/sgl-project/sglang/pull/39219)
  [Fix] Don't write conv state from the fused KDA verify kernel (#39219)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_kda_conv_recurrent_verify.py`, `test/registered/kernels/test_fused_kda_conv_recurrent_verify.py`_
- **2026-09-14** [`60f6f03409`](https://github.com/sgl-project/sglang/commit/60f6f03409) [#39061](https://github.com/sgl-project/sglang/pull/39061)
  Fix MUSA detection in compiled prefill path (#39061)
  _Files: `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/utils/common.py`, `test/registered/cp/test_cp_strategy_unit.py`, `test/registered/unit/utils/test_common.py`_
- **2026-09-14** [`f2111715cd`](https://github.com/sgl-project/sglang/commit/f2111715cd) [#33426](https://github.com/sgl-project/sglang/pull/33426)
  [fa] Make the FlashAttention backend extensible by subclasses (#33426)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/attention/unittests/dense/test_fa4.py`_
- **2026-09-14** [`5a132c061b`](https://github.com/sgl-project/sglang/commit/5a132c061b) [#39232](https://github.com/sgl-project/sglang/pull/39232)
  [Perf] trtllm_mla: reuse the fused fp8 KV/Q prepare on target verify (#39232)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-09-14** [`6410800af9`](https://github.com/sgl-project/sglang/commit/6410800af9) [#37418](https://github.com/sgl-project/sglang/pull/37418)
  [unified-memory] Enable prefill cuda-graph capture (#37418)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/e2e/models/test_inkling_unified.py`, `test/registered/unit/layers/attention/test_flashattention_graph_metadata.py` _+1 more__

## Prefill / Decode Disaggregation  (59 commits)

- **2026-09-21** [`b54d5b7c7b`](https://github.com/sgl-project/sglang/commit/b54d5b7c7b) [#28652](https://github.com/sgl-project/sglang/pull/28652)
  disaggregation: Fix FakeKVSender queue accumulation (#28652)
  _Files: `python/sglang/srt/disaggregation/fake/conn.py`, `test/registered/unit/disaggregation/test_fake_kv_sender.py`_
- **2026-09-21** [`501b7851e4`](https://github.com/sgl-project/sglang/commit/501b7851e4) [#39206](https://github.com/sgl-project/sglang/pull/39206)
  [diffusion] CI: guard E2E/loading latency with runner-aware baselines (#39206)
  _Files: `.github/actions/check-pr-test-health/action.test.cjs`, `.github/actions/check-pr-test-health/action.yml`, `.github/workflows/lint.yml`, `.github/workflows/pr-test-multimodal-gen.yml` _+32 more__
- **2026-09-21** [`76a9065bef`](https://github.com/sgl-project/sglang/commit/76a9065bef) [#40502](https://github.com/sgl-project/sglang/pull/40502)
  [Fix] Raise on undelivered embeddings in `send_with_url`, fix broken tests (#40502)
  _Files: `python/sglang/srt/disaggregation/encoder/server.py`, `test/registered/disaggregation/test_epd_disaggregation.py`, `test/registered/observability/test_encoder_server_metrics.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4_moe_dispatch.py`_
- **2026-09-20** [`f6483e479f`](https://github.com/sgl-project/sglang/commit/f6483e479f) [#40288](https://github.com/sgl-project/sglang/pull/40288)
  [Test] Drop cause-less disabled tests, fix XPU lane, demote quality gates off base-c (#40288)
  _Files: `.github/workflows/pr-test-extra.yml`, `test/registered/disaggregation/test_disaggregation_xpu.py`, `test/registered/e2e/models/test_dsa_glm52_dp_mtp.py`, `test/registered/e2e/models/test_dsa_glm52_tp_mtp.py` _+10 more__
- **2026-09-20** [`b3e4d198af`](https://github.com/sgl-project/sglang/commit/b3e4d198af) [#40376](https://github.com/sgl-project/sglang/pull/40376)
  [PD] Bound cached-prefix DCP transfers by pack capacity (#40376)
  _Files: `benchmark/disaggregation/bench_cached_prefix.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/dcp_pack.py` _+4 more__
- **2026-09-20** [`8923f4d779`](https://github.com/sgl-project/sglang/commit/8923f4d779) [#40469](https://github.com/sgl-project/sglang/pull/40469)
  [Test] Fix optimistic prefill disaggregation test after mamba radix cache removal (#40469)
  _Files: `test/registered/disaggregation/test_disaggregation_optimistic_prefill.py`_
- **2026-09-20** [`f4c256354c`](https://github.com/sgl-project/sglang/commit/f4c256354c) [#40045](https://github.com/sgl-project/sglang/pull/40045)
  [kimi k3][pd disagg] support pp prefill + dcp decode with dspark (#40045)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` _+17 more__
- **2026-09-20** [`020703923d`](https://github.com/sgl-project/sglang/commit/020703923d) [#36700](https://github.com/sgl-project/sglang/pull/36700)
  [PP + HiCache] Add PP Prefetch Tickets for eager cross-stage storage prefetch (#36700)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py` _+6 more__
- **2026-09-20** [`113f6f080e`](https://github.com/sgl-project/sglang/commit/113f6f080e) [#40284](https://github.com/sgl-project/sglang/pull/40284)
  [PD] Enter the custom mem pool once when allocating DCP pack buffers (#40284)
  _Files: `python/sglang/srt/disaggregation/mooncake/utils.py`, `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-09-20** [`d82d653f96`](https://github.com/sgl-project/sglang/commit/d82d653f96) [#40184](https://github.com/sgl-project/sglang/pull/40184)
  Enable optimistic prefill for Mamba radix-cache models (#40184)
  _Files: `python/sglang/srt/arg_groups/serving_hook.py`, `python/sglang/srt/disaggregation/prefill.py`, `test/registered/disaggregation/test_disaggregation_optimistic_prefill.py`_
- **2026-09-20** [`e9300f643e`](https://github.com/sgl-project/sglang/commit/e9300f643e) [#39565](https://github.com/sgl-project/sglang/pull/39565)
  [Unified Cache][9/N] add opt-in MLA load deduplication for Mooncake Linker (#39565)
  _Files: `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/unified_cache/linker_mla_dedup.py` _+1 more__
- **2026-09-20** [`f9c2791460`](https://github.com/sgl-project/sglang/commit/f9c2791460) [#39983](https://github.com/sgl-project/sglang/pull/39983)
  [diffusion] model: support qwen-image-2.1 (#39983)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/cookbook/diffusion/intro.mdx`, `docs/docs.json`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx` _+48 more__
- **2026-09-19** [`3a64faa1f2`](https://github.com/sgl-project/sglang/commit/3a64faa1f2) [#39378](https://github.com/sgl-project/sglang/pull/39378)
  Fix disagg PP MTP for GLM-5.2 (#39378)
  _Files: `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` _+8 more__
- **2026-09-19** [`3a5f52e144`](https://github.com/sgl-project/sglang/commit/3a5f52e144) [#40071](https://github.com/sgl-project/sglang/pull/40071)
  Record a process's placement at publish, not at group build (#40071)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` _+43 more__
- **2026-09-19** [`6e1338dd1e`](https://github.com/sgl-project/sglang/commit/6e1338dd1e) [#40262](https://github.com/sgl-project/sglang/pull/40262)
  Fix prefetch attempt cleanup on abort (#40262)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-09-19** [`677c1cbdc9`](https://github.com/sgl-project/sglang/commit/677c1cbdc9) [#40004](https://github.com/sgl-project/sglang/pull/40004)
  [Metrics] Propagate idle gaps across all scheduler loops (#40004)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` _+4 more__
- **2026-09-19** [`8189e3896b`](https://github.com/sgl-project/sglang/commit/8189e3896b) [#40003](https://github.com/sgl-project/sglang/pull/40003)
  [PD] Skip singleton transfer-status all-reduces (#40003)
  _Files: `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`, `test/registered/unit/managers/test_scheduler_on_idle_load.py`_
- **2026-09-19** [`5e9342d16f`](https://github.com/sgl-project/sglang/commit/5e9342d16f) [#38792](https://github.com/sgl-project/sglang/pull/38792)
  [PP][DeepSeek V4] Overlap communication and optimize SM120 prefill (#38792)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/serving_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` _+13 more__
- **2026-09-19** [`c475ac5eaf`](https://github.com/sgl-project/sglang/commit/c475ac5eaf) [#37547](https://github.com/sgl-project/sglang/pull/37547)
  [diffusion] feat: out of tree platform support (#37547)
  _Files: `docs/docs/hardware-platforms/plugin.mdx`, `docs/docs/sglang-diffusion/contributing.mdx`, `docs/docs/sglang-diffusion/disaggregation.mdx`, `docs/docs/sglang-diffusion/environment_variables.mdx` _+36 more__
- **2026-09-19** [`10b0bcfd18`](https://github.com/sgl-project/sglang/commit/10b0bcfd18) [#40263](https://github.com/sgl-project/sglang/pull/40263)
  [PD] Allow decode radix cache and HiCache L1/L2 with DCP (#40263)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-09-19** [`d507accadc`](https://github.com/sgl-project/sglang/commit/d507accadc) [#40264](https://github.com/sgl-project/sglang/pull/40264)
  [Test] Drop dead and strictly-subsumed CI test registrations (#40264)
  _Files: `test/manual/test_trtllm_mla.py`, `test/registered/debug_utils/test_dump_comparator.py`, `test/registered/e2e/models/test_nvidia_nemotron_3_super_bf16.py`, `test/registered/e2e/models_large/test_deepseek_v3_cutedsl_4gpu.py` _+15 more__
- **2026-09-19** [`fa7e83fd09`](https://github.com/sgl-project/sglang/commit/fa7e83fd09) [#40070](https://github.com/sgl-project/sglang/pull/40070)
  Name the two widths of the WORLD group (#40070)
  _Files: `python/sglang/srt/disaggregation/ascend/transfer_engine.py`, `python/sglang/srt/elastic_ep/elastic_ep.py`, `python/sglang/srt/elastic_ep/expert_backup_client.py`, `python/sglang/srt/managers/scheduler.py` _+9 more__
- **2026-09-19** [`5931fd60ee`](https://github.com/sgl-project/sglang/commit/5931fd60ee) [#39477](https://github.com/sgl-project/sglang/pull/39477)
  Support unified memory page-envelope transfers in PD (#39477)
  _Files: `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+23 more__
- **2026-09-19** [`d0730a0e8b`](https://github.com/sgl-project/sglang/commit/d0730a0e8b) [#40067](https://github.com/sgl-project/sglang/pull/40067)
  Give the attention-DP width and rank one home (#40067)
  _Files: `python/sglang/srt/debug_utils/dumper.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/engram.py` _+7 more__
- **2026-09-18** [`ceb1d2e580`](https://github.com/sgl-project/sglang/commit/ceb1d2e580) [#40043](https://github.com/sgl-project/sglang/pull/40043)
  [PD] Enable optimistic prefill with buffer-only L3 write-through HiCache (#40043)
  _Files: `python/sglang/srt/arg_groups/serving_hook.py`, `python/sglang/srt/disaggregation/prefill.py`, `test/registered/disaggregation/test_disaggregation_optimistic_prefill.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-09-18** [`6cc9090d1f`](https://github.com/sgl-project/sglang/commit/6cc9090d1f) [#40075](https://github.com/sgl-project/sglang/pull/40075)
  [mem_cache] Release up to `owned_kv_len` on radix cache insert (#40075)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/chunk_cache.py` _+22 more__
- **2026-09-18** [`f86f60081d`](https://github.com/sgl-project/sglang/commit/f86f60081d) [#39415](https://github.com/sgl-project/sglang/pull/39415)
  [NPU] Adapt hicache for K3 hybrid models (#39415)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/pool_host/mamba.py` _+7 more__
- **2026-09-18** [`6215aecd51`](https://github.com/sgl-project/sglang/commit/6215aecd51) [#19084](https://github.com/sgl-project/sglang/pull/19084)
  [diffusion] feat: add metrics support (#19084)
  _Files: `docs/docs.json`, `docs/docs/references/production_metrics.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/production_metrics.mdx` _+13 more__
- **2026-09-17** [`7bc9152447`](https://github.com/sgl-project/sglang/commit/7bc9152447) [#39966](https://github.com/sgl-project/sglang/pull/39966)
  [Test] Consolidate kernel tests under plural kernels tree (#39966)
  _Files: `.claude/skills/write-sglang-test/SKILL.md`, `.github/workflows/_pr-test-check-changes.yml`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/README.md`, `python/sglang/srt/distributed/device_communicators/configs/custom_all_reduce_v2.py` _+49 more__
- **2026-09-17** [`1f0c73e9bd`](https://github.com/sgl-project/sglang/commit/1f0c73e9bd) [#39921](https://github.com/sgl-project/sglang/pull/39921)
  [DSV4] Generalize attention metadata, sparse prefill, and KV pool over compress ratios (#39921)
  _Files: `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` _+14 more__
- **2026-09-17** [`6c73368c32`](https://github.com/sgl-project/sglang/commit/6c73368c32) [#37778](https://github.com/sgl-project/sglang/pull/37778)
  [AMD][DSV4] Enable hicache on deepseek-v4 fp8 unified attn (#37778)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool_host.py` _+5 more__
- **2026-09-17** [`1f60ddef5d`](https://github.com/sgl-project/sglang/commit/1f60ddef5d) [#28403](https://github.com/sgl-project/sglang/pull/28403)
  [PD] Introduce runtime role switching between prefill and decode (#28403)
  _Files: `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py` _+23 more__
- **2026-09-17** [`15b256bdb0`](https://github.com/sgl-project/sglang/commit/15b256bdb0) [#29668](https://github.com/sgl-project/sglang/pull/29668)
  [HiCache] fix: resolve Mooncake local_hostname per node for runtime attach (#29668)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/README.md`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `test/registered/unit/mem_cache/test_mooncake_store_config.py`_
- **2026-09-17** [`329ffc89b9`](https://github.com/sgl-project/sglang/commit/329ffc89b9) [#31926](https://github.com/sgl-project/sglang/pull/31926)
  [Mooncake] Fix silent SSD offload corruption when TP/PP ranks share ssd_offload_path (#31926)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `test/registered/unit/mem_cache/test_mooncake_ssd_offload_path.py`_
- **2026-09-16** [`1b78083b42`](https://github.com/sgl-project/sglang/commit/1b78083b42) [#39500](https://github.com/sgl-project/sglang/pull/39500)
  [PD] Add optional KV transfer checksums (#39500)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/adler32_checksum.cuh`, `python/sglang/kernels/ops/memory/adler32.py`, `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/disaggregation/checksum.py` _+8 more__
- **2026-09-16** [`cc171fbad0`](https://github.com/sgl-project/sglang/commit/cc171fbad0) [#35802](https://github.com/sgl-project/sglang/pull/35802)
  feat: support custom OTLP trace service name (#35802)
  _Files: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/runtime/utils/trace_wrapper.py`, `python/sglang/srt/arg_groups/fields/observability.py`, `python/sglang/srt/disaggregation/encoder/runtime.py` _+6 more__
- **2026-09-16** [`7b7620774c`](https://github.com/sgl-project/sglang/commit/7b7620774c) [#38774](https://github.com/sgl-project/sglang/pull/38774)
  Fix device context during NIXL backend initialization (#38774)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-09-16** [`3f8eb35ead`](https://github.com/sgl-project/sglang/commit/3f8eb35ead) [#38935](https://github.com/sgl-project/sglang/pull/38935)
  [PD] Do not admit intake-rejected requests to a PD handoff (#38935)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/scheduler.py` _+1 more__
- **2026-09-16** [`2f7d04da5d`](https://github.com/sgl-project/sglang/commit/2f7d04da5d) [#39677](https://github.com/sgl-project/sglang/pull/39677)
  dsv4.1: Rust extension modules for image preprocessing, KV pool names, and PD bootstrap (#39677)
  _Files: `rust/sglang-mm/src/dsv41/mod.rs`, `rust/sglang-mm/src/lib.rs`, `rust/sglang-radix-tree/src/python_bindings.rs`, `rust/sglang-radix-tree/src/unified_tree_core.rs` _+1 more__
- **2026-09-16** [`dbd7281b06`](https://github.com/sgl-project/sglang/commit/dbd7281b06) [#38402](https://github.com/sgl-project/sglang/pull/38402)
  fix(npu): fix hybrid KV transfer with PP prefill in PD disaggregation (#38402)
  _Files: `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/models/kimi_k3.py` _+2 more__
- **2026-09-15** [`2929a39927`](https://github.com/sgl-project/sglang/commit/2929a39927) [#36729](https://github.com/sgl-project/sglang/pull/36729)
  Use a shared byte budget for unified hybrid-SWA memory (#36729)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py` _+28 more__
- **2026-09-15** [`87c9f78e99`](https://github.com/sgl-project/sglang/commit/87c9f78e99) [#39584](https://github.com/sgl-project/sglang/pull/39584)
  [Fix][PD] Give prefill and decode their own RDMA NICs in disaggregation tests (#39584)
  _Files: `python/sglang/test/server_fixtures/disaggregation_fixture.py`, `test/registered/disaggregation/test_disaggregation_aarch64.py`, `test/registered/disaggregation/test_disaggregation_decode_offload.py`, `test/registered/disaggregation/test_disaggregation_different_tp.py` _+8 more__
- **2026-09-15** [`7f5dd19256`](https://github.com/sgl-project/sglang/commit/7f5dd19256) [#39283](https://github.com/sgl-project/sglang/pull/39283)
  [HiCache] Rework the buffer-mode storage prefetch pipeline and retry bookkeeping (#39283)
  _Files: `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/npu/dsv4/c128_sidecar_component.py`, `python/sglang/srt/managers/schedule_batch.py` _+39 more__
- **2026-09-15** [`47a157f257`](https://github.com/sgl-project/sglang/commit/47a157f257) [#39611](https://github.com/sgl-project/sglang/pull/39611)
  [CI][Disaggregation] Fix EADDRINUSE flake in test_disaggregation_dwdp_gpt_oss (#39611)
  _Files: `test/registered/disaggregation/test_disaggregation_dwdp_gpt_oss.py`_
- **2026-09-15** [`832ec39cc0`](https://github.com/sgl-project/sglang/commit/832ec39cc0) [#38984](https://github.com/sgl-project/sglang/pull/38984)
  [Intra-node PD][DSV4] Pack all layers into one batch for INTRA_NODE_NVLINK path (#38984)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `test/registered/unit/disaggregation/test_mooncake_custom_mem_pool_batch.py`, `test/registered/unit/disaggregation/test_mooncake_transfer_batching.py`_
- **2026-09-15** [`a2a261963f`](https://github.com/sgl-project/sglang/commit/a2a261963f) [#39600](https://github.com/sgl-project/sglang/pull/39600)
  [CI] Fix SWA decode radix cache NIXL import (#39600)
  _Files: `test/registered/disaggregation/test_disaggregation_decode_radix_cache_swa.py`_
- **2026-09-15** [`1895cabfa8`](https://github.com/sgl-project/sglang/commit/1895cabfa8) [#38503](https://github.com/sgl-project/sglang/pull/38503)
  Fix mooncake scale joiner groups (#38503)
  _Files: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/parallel_state.py`_
- **2026-09-15** [`8565b11003`](https://github.com/sgl-project/sglang/commit/8565b11003) [#39544](https://github.com/sgl-project/sglang/pull/39544)
  [misc] Trim redundant variants from the 8-gpu-h20 disaggregation test suite (#39544)
  _Files: `test/registered/disaggregation/test_disaggregation_decode_radix_cache.py`, `test/registered/disaggregation/test_disaggregation_dp_attention.py`, `test/registered/disaggregation/test_disaggregation_nixl.py`, `test/registered/disaggregation/test_disaggregation_pp.py` _+1 more__
- **2026-09-15** [`860fa83a9f`](https://github.com/sgl-project/sglang/commit/860fa83a9f) [#39545](https://github.com/sgl-project/sglang/pull/39545)
  [CI] Wait for a killed test server's GPU memory before the next launch (#39545)
  _Files: `.claude/skills/write-sglang-test/SKILL.md`, `python/sglang/test/runners.py`, `python/sglang/test/test_utils.py`, `test/registered/ep/test_deepep_large.py` _+7 more__
- **2026-09-15** [`ebd37705e4`](https://github.com/sgl-project/sglang/commit/ebd37705e4) [#39332](https://github.com/sgl-project/sglang/pull/39332)
  [PD][LoRA] Gate decode admission on adapter slots (#39332)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/e2e/disaggregation/test_disaggregation_lora.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py` _+1 more__
- **2026-09-15** [`3f871a246c`](https://github.com/sgl-project/sglang/commit/3f871a246c) [#37482](https://github.com/sgl-project/sglang/pull/37482)
  feat(agent sessions): attribute stored KV cache blocks to sessions (#37482)
  _Files: `experimental/sgl-router/sgl-kv-indexer/src/bridge.rs`, `experimental/sgl-router/src/policies/kv_events/subscriber.rs`, `experimental/sgl-router/src/policies/kv_events/wire.rs`, `experimental/sgl-router/tests/component/policies/zmq_helpers.rs` _+18 more__
- **2026-09-15** [`4b186cfea5`](https://github.com/sgl-project/sglang/commit/4b186cfea5) [#39368](https://github.com/sgl-project/sglang/pull/39368)
  [CI][PD] Skip the flaky decode HiCache file-backend disaggregation test (#39368)
  _Files: `test/registered/disaggregation/test_disaggregation_decode_radix_cache.py`_
- **2026-09-14** [`dad8c074e7`](https://github.com/sgl-project/sglang/commit/dad8c074e7) [#39318](https://github.com/sgl-project/sglang/pull/39318)
  Scope prefetch cache state to the request attempt (#39318)
  _Files: `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py` _+17 more__
- **2026-09-14** [`5c2de3f355`](https://github.com/sgl-project/sglang/commit/5c2de3f355) [#39357](https://github.com/sgl-project/sglang/pull/39357)
  [PD] Preserve the prefill rank during rebootstrap (#39357)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-09-14** [`95140a7b0c`](https://github.com/sgl-project/sglang/commit/95140a7b0c) [#39396](https://github.com/sgl-project/sglang/pull/39396)
  [docs] DeepSeek-V4: MI355X PD disaggregation recipes for all three strategies (#39396)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-14** [`4c71d14fba`](https://github.com/sgl-project/sglang/commit/4c71d14fba) [#39162](https://github.com/sgl-project/sglang/pull/39162)
  [HiCache][LoRA] Simplify decode offload hash inputs (#39162)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `test/registered/unit/disaggregation/test_specv2_kvcache_offloading.py`_
- **2026-09-14** [`bf9773e1da`](https://github.com/sgl-project/sglang/commit/bf9773e1da) [#37425](https://github.com/sgl-project/sglang/pull/37425)
  HiCache: Add @rank_consensus to various functions (#37425)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `python/sglang/test/server_fixtures/default_fixture.py`, `python/sglang/test/test_utils.py`, `test/registered/hicache/test_hicache_spec_file_storage.py` _+20 more__
- **2026-09-14** [`ca8ecc6a6f`](https://github.com/sgl-project/sglang/commit/ca8ecc6a6f) [#37382](https://github.com/sgl-project/sglang/pull/37382)
  [NPU] Support DSV4 host memory cache management (#37382)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/c128_sidecar_component.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_allocator.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_memory_pool.py`, `python/sglang/srt/managers/schedule_batch.py` _+8 more__
- **2026-09-14** [`2ec4bbcbd4`](https://github.com/sgl-project/sglang/commit/2ec4bbcbd4) [#37506](https://github.com/sgl-project/sglang/pull/37506)
  [unified-memory] PD disaggregation for every unified pool shape (#37506)
  _Files: `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` _+14 more__

## Other  (50 commits)

- **2026-09-21** [`630b1ef322`](https://github.com/sgl-project/sglang/commit/630b1ef322) [#40537](https://github.com/sgl-project/sglang/pull/40537)
  [sgl-router] Fix reorg admission proxy test build after BucketResolver::new (#40537)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/src/policies_reorg/session_aware.rs`, `experimental/sgl-router/tests/proxy/chat_routing/reorg.rs`_
- **2026-09-21** [`a9871012ac`](https://github.com/sgl-project/sglang/commit/a9871012ac) [#40271](https://github.com/sgl-project/sglang/pull/40271)
  [sgl-router] refactor - generalized admission policy definitions (#40271)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/src/policies_reorg/admission.rs`, `experimental/sgl-router/src/policies_reorg/cache_aware.rs`, `experimental/sgl-router/src/policies_reorg/power_of_two.rs` _+8 more__
- **2026-09-21** [`f5f3c38aad`](https://github.com/sgl-project/sglang/commit/f5f3c38aad) [#38786](https://github.com/sgl-project/sglang/pull/38786)
  [Fix] Preserve YaRN scaling when extending rotary caches (#38786)
  _Files: `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/layers/rotary_embedding/rope_variant.py`, `python/sglang/srt/layers/rotary_embedding/yarn.py`, `test/registered/unit/layers/test_yarn_cache_extension.py`_
- **2026-09-21** [`fcb080bd40`](https://github.com/sgl-project/sglang/commit/fcb080bd40) [#40366](https://github.com/sgl-project/sglang/pull/40366)
  [sgl-router] refactor - cache-aware policy (#40366)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/src/buckets_reorg.rs`, `experimental/sgl-router/src/policies_reorg/cache_aware.rs`, `experimental/sgl-router/src/policies_reorg/mod.rs` _+5 more__
- **2026-09-21** [`4027740569`](https://github.com/sgl-project/sglang/commit/4027740569) [#40379](https://github.com/sgl-project/sglang/pull/40379)
  [sgl-router] refactor - session-aware policy (#40379)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/src/policies_reorg/mod.rs`, `experimental/sgl-router/src/policies_reorg/session_aware.rs`, `experimental/sgl-router/tests/component/main.rs` _+3 more__
- **2026-09-20** [`aedda8377e`](https://github.com/sgl-project/sglang/commit/aedda8377e) [#40241](https://github.com/sgl-project/sglang/pull/40241)
  [sgl-router] refactor - layout BucketResolver, Bucket, EngineGroup and implement PowerOfTwo (#40241)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/src/buckets_reorg.rs`, `experimental/sgl-router/src/lib.rs`, `experimental/sgl-router/src/policies_reorg/admission.rs` _+11 more__
- **2026-09-20** [`f31a7bd45c`](https://github.com/sgl-project/sglang/commit/f31a7bd45c) [#39777](https://github.com/sgl-project/sglang/pull/39777)
  Use pinned memory for asynchronous sampling metadata transfers (#39777)
  _Files: `python/sglang/srt/layers/logprob_processor.py`, `python/sglang/srt/sampling/penaltylib/frequency_penalty.py`, `python/sglang/srt/sampling/penaltylib/min_new_tokens.py`, `python/sglang/srt/sampling/penaltylib/presence_penalty.py` _+3 more__
- **2026-09-20** [`745de73ba3`](https://github.com/sgl-project/sglang/commit/745de73ba3) [#40483](https://github.com/sgl-project/sglang/pull/40483)
  Add CODEOWNERS entry for sglang-renderer (#40483)
  _Files: `.github/CODEOWNERS`_
- **2026-09-20** [`c610c40399`](https://github.com/sgl-project/sglang/commit/c610c40399) [#39867](https://github.com/sgl-project/sglang/pull/39867)
  [sgl-router] refactor - config and organize CLI options (#39867)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/sampling.rs`, `experimental/sgl-router/src/config/types.rs`_
- **2026-09-20** [`671630abf1`](https://github.com/sgl-project/sglang/commit/671630abf1) [#39861](https://github.com/sgl-project/sglang/pull/39861)
  [sgl-router] refactor - main startup logic (#39861)
  _Files: `experimental/sgl-router/src/main.rs`_
- **2026-09-20** [`99d53fe0c2`](https://github.com/sgl-project/sglang/commit/99d53fe0c2) [#39848](https://github.com/sgl-project/sglang/pull/39848)
  [sgl-router] refactor - chat_completions() into modules (#39848)
  _Files: `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/src/server/routes/chat/forward.rs`, `experimental/sgl-router/src/server/routes/chat/preparation.rs`_
- **2026-09-19** [`36aa8479ef`](https://github.com/sgl-project/sglang/commit/36aa8479ef) [#40290](https://github.com/sgl-project/sglang/pull/40290)
  [Test] Fix fusion-group mocks after runtime context migration (#40290)
  _Files: `test/registered/unit/layers/test_layer_communicator_fusion_gate.py`_
- **2026-09-19** [`6533223502`](https://github.com/sgl-project/sglang/commit/6533223502) [#40303](https://github.com/sgl-project/sglang/pull/40303)
  [Lint] Fix logits processor formatting on main (#40303)
  _Files: `python/sglang/srt/layers/logits_processor.py`_
- **2026-09-19** [`5b42d10edf`](https://github.com/sgl-project/sglang/commit/5b42d10edf) [#40259](https://github.com/sgl-project/sglang/pull/40259)
  fix: restrict SafeUnpickler to explicit globals (#40259)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-09-19** [`afe71f4b9e`](https://github.com/sgl-project/sglang/commit/afe71f4b9e) [#40068](https://github.com/sgl-project/sglang/pull/40068)
  Read process groups through the runtime context (#40068)
- **2026-09-18** [`b876213548`](https://github.com/sgl-project/sglang/commit/b876213548) [#40257](https://github.com/sgl-project/sglang/pull/40257)
  [Test] Add a ci-test-audit skill cataloging CI and test audit patterns (#40257)
  _Files: `.claude/skills/ci-test-audit/SKILL.md`, `.claude/skills/ci-test-audit/action-items.md`_
- **2026-09-18** [`6bd1a0af1d`](https://github.com/sgl-project/sglang/commit/6bd1a0af1d) [#39452](https://github.com/sgl-project/sglang/pull/39452)
  Add registration for external model configurations (#39452)
  _Files: `python/sglang/srt/configs/model_config.py`, `test/registered/unit/configs/test_model_config.py`_
- **2026-09-18** [`4e0b56c811`](https://github.com/sgl-project/sglang/commit/4e0b56c811) [#39464](https://github.com/sgl-project/sglang/pull/39464)
  [Router] Treat an upstream 503/429 as backpressure, not a breaker fault (2/3) (#39464)
  _Files: `experimental/sgl-router/src/health/circuit_breaker.rs`, `experimental/sgl-router/src/proxy/mod.rs`_
- **2026-09-18** [`a6cf05817f`](https://github.com/sgl-project/sglang/commit/a6cf05817f) [#38798](https://github.com/sgl-project/sglang/pull/38798)
  dsv4.1: remaining model and runtime integration (#38798)
- **2026-09-18** [`6de4666e43`](https://github.com/sgl-project/sglang/commit/6de4666e43) [#39463](https://github.com/sgl-project/sglang/pull/39463)
  [Router] Derive error status from a failure class; preserve the worker's status (1/3) (#39463)
  _Files: `experimental/sgl-router/monitoring/grafana-dashboard.json`, `experimental/sgl-router/src/proxy/mod.rs`, `experimental/sgl-router/src/server/error.rs`, `experimental/sgl-router/tests/proxy/chat_routing.rs` _+1 more__
- **2026-09-18** [`1fdd6c8921`](https://github.com/sgl-project/sglang/commit/1fdd6c8921) [#37969](https://github.com/sgl-project/sglang/pull/37969)
  [Runtime] Let out-of-tree platforms provide full graph backends (#37969)
  _Files: `python/sglang/srt/model_executor/runner_backend/utils.py`, `python/sglang/srt/platforms/interface.py`, `test/registered/unit/model_executor/runner_backend/test_backend_resolution.py`_
- **2026-09-18** [`956d414dad`](https://github.com/sgl-project/sglang/commit/956d414dad) [#40121](https://github.com/sgl-project/sglang/pull/40121)
  Update ci permission (#40121)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-09-18** [`3bf243d6a9`](https://github.com/sgl-project/sglang/commit/3bf243d6a9) [#39167](https://github.com/sgl-project/sglang/pull/39167)
  [Router] Shard the cache-aware KV tree by chain root (#39167)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/benches/tree_lookup.rs`, `experimental/sgl-router/src/policies/kv_events/index.rs` _+3 more__
- **2026-09-18** [`3d1b9e7549`](https://github.com/sgl-project/sglang/commit/3d1b9e7549) [#39482](https://github.com/sgl-project/sglang/pull/39482)
  [Bugfix] Include SM121 in DeepGEMM packed-scale selection (#39482)
  _Files: `python/sglang/srt/layers/deep_gemm_wrapper/configurer.py`_
- **2026-09-18** [`a407915c17`](https://github.com/sgl-project/sglang/commit/a407915c17) [#39690](https://github.com/sgl-project/sglang/pull/39690)
  [CPU] Avoid prefill CP predicates during decode graph capture (#39690)
  _Files: `python/sglang/srt/layers/communicator.py`_
- **2026-09-17** [`72d9419bef`](https://github.com/sgl-project/sglang/commit/72d9419bef) [#39170](https://github.com/sgl-project/sglang/pull/39170)
  [Router] Sample k random candidates for the min-load fallback (--min-load-choices) (#39170)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/policies/admission.rs`, `experimental/sgl-router/src/policies/cache_aware.rs` _+5 more__
- **2026-09-17** [`575759d90a`](https://github.com/sgl-project/sglang/commit/575759d90a) [#39413](https://github.com/sgl-project/sglang/pull/39413)
  [NPU] Support nccl backend for --remote-instance-weight-loader (#39413)
  _Files: `python/sglang/srt/connector/remote_instance.py`, `python/sglang/srt/model_executor/model_runner_components/weight_exporter.py`_
- **2026-09-17** [`882577451e`](https://github.com/sgl-project/sglang/commit/882577451e) [#39858](https://github.com/sgl-project/sglang/pull/39858)
  Restrict SafeUnpickler standard-library globals (#39858)
  _Files: `python/sglang/srt/utils/common.py`, `test/registered/unit/utils/test_safe_unpickler.py`_
- **2026-09-17** [`7782a2a1c8`](https://github.com/sgl-project/sglang/commit/7782a2a1c8) [#39398](https://github.com/sgl-project/sglang/pull/39398)
  [Benchmark] Limit warmup concurrency in serving benchmark (#39398)
  _Files: `python/sglang/benchmark/serving.py`_
- **2026-09-17** [`0daa040e48`](https://github.com/sgl-project/sglang/commit/0daa040e48) [#39874](https://github.com/sgl-project/sglang/pull/39874)
  Support LongBench v2 in one-batch server benchmarks (#39874)
  _Files: `python/sglang/benchmark/one_batch_server.py`_
- **2026-09-16** [`3e03879f68`](https://github.com/sgl-project/sglang/commit/3e03879f68) [#39016](https://github.com/sgl-project/sglang/pull/39016)
  [Router] Drain readiness before SIGTERM shutdown so k8s deregisters the pod first (#39016)
  _Files: `experimental/sgl-router/src/main.rs`, `experimental/sgl-router/src/server/app_context.rs`, `experimental/sgl-router/src/server/mod.rs`, `experimental/sgl-router/src/server/shutdown.rs` _+6 more__
- **2026-09-16** [`ad94978adf`](https://github.com/sgl-project/sglang/commit/ad94978adf) [#39459](https://github.com/sgl-project/sglang/pull/39459)
  [sgl-router] Rename chat encoder to chat formatter (#39459)
  _Files: `experimental/sgl-router/src/policies/mod.rs`, `experimental/sgl-router/src/server/metrics.rs`, `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/src/tokenizer/mod.rs` _+4 more__
- **2026-09-16** [`e41026f434`](https://github.com/sgl-project/sglang/commit/e41026f434) [#39458](https://github.com/sgl-project/sglang/pull/39458)
  [sgl-router] Forward input_ids only for string content; count tokenize errors only when forwardable (#39458)
  _Files: `experimental/sgl-router/src/server/metrics.rs`, `experimental/sgl-router/src/server/routes/chat.rs`_
- **2026-09-16** [`8baeded6f3`](https://github.com/sgl-project/sglang/commit/8baeded6f3) [#39169](https://github.com/sgl-project/sglang/pull/39169)
  [Router] Pin to the prefix owner when the whole fleet is queueing (--saturation-queue-floor) (#39169)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/policies/admission.rs`, `experimental/sgl-router/src/policies/cache_aware.rs` _+5 more__
- **2026-09-16** [`54f0d72adf`](https://github.com/sgl-project/sglang/commit/54f0d72adf) [#39001](https://github.com/sgl-project/sglang/pull/39001)
  [Router] Fleet-wide sampling contract 2/3: enforce and inject per request (#39001)
  _Files: `experimental/sgl-router/src/server/error.rs`, `experimental/sgl-router/src/server/metrics.rs`, `experimental/sgl-router/src/server/routes/chat.rs`_
- **2026-09-16** [`7835f1de9a`](https://github.com/sgl-project/sglang/commit/7835f1de9a) [#39015](https://github.com/sgl-project/sglang/pull/39015)
  [Router] Add the shutdown-drain configuration surface (#39015)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/policies/factory.rs` _+19 more__
- **2026-09-16** [`5beb2fd552`](https://github.com/sgl-project/sglang/commit/5beb2fd552) [#39404](https://github.com/sgl-project/sglang/pull/39404)
  [NPU] Avoid device synchronization in Ascend sampling (#39404)
  _Files: `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/sampling/sampling_batch_info.py`, `test/registered/unit/sampling/test_ascend_sampler.py`, `test/registered/unit/sampling/test_sampling_batch_info.py`_
- **2026-09-16** [`e2d56bbbfc`](https://github.com/sgl-project/sglang/commit/e2d56bbbfc) [#39713](https://github.com/sgl-project/sglang/pull/39713)
  [Router] Bound the e2e worker memory budget so prefill graph capture stops OOMing (#39713)
  _Files: `experimental/sgl-router/tests/e2e/infra/model_specs.py`_
- **2026-09-16** [`c1f5b4736a`](https://github.com/sgl-project/sglang/commit/c1f5b4736a) [#39168](https://github.com/sgl-project/sglang/pull/39168)
  [Router] Add --worker-queue-limit: stop sending cache-affinity traffic to a queueing worker (#39168)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/policies/admission.rs`, `experimental/sgl-router/src/policies/cache_aware.rs` _+7 more__
- **2026-09-16** [`5f17e3a75f`](https://github.com/sgl-project/sglang/commit/5f17e3a75f) [#39000](https://github.com/sgl-project/sglang/pull/39000)
  [Router] Fleet-wide sampling contract 1/3: the config surface (#39000)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/sampling.rs`, `experimental/sgl-router/src/config/types.rs` _+20 more__
- **2026-09-16** [`bbef93e22a`](https://github.com/sgl-project/sglang/commit/bbef93e22a) [#39111](https://github.com/sgl-project/sglang/pull/39111)
  [Router] Add a KV storage-tier coverage row to the Grafana dashboard (4/4) (#39111)
  _Files: `experimental/sgl-router/monitoring/grafana-dashboard.json`_
- **2026-09-15** [`63845a1bb2`](https://github.com/sgl-project/sglang/commit/63845a1bb2) [#39004](https://github.com/sgl-project/sglang/pull/39004)
  [router] Resolve a wire protocol per worker at registration (#39004)
  _Files: `experimental/sgl-router/src/workers/introspect.rs`, `experimental/sgl-router/src/workers/manager.rs`, `experimental/sgl-router/src/workers/mod.rs`, `experimental/sgl-router/src/workers/registry.rs` _+2 more__
- **2026-09-15** [`fb91baedab`](https://github.com/sgl-project/sglang/commit/fb91baedab) [#39110](https://github.com/sgl-project/sglang/pull/39110)
  [Router] Real-GPU e2e coverage for storage-tier-aware cache routing (3/4) (#39110)
  _Files: `experimental/sgl-router/tests/e2e/chat_completions/test_hicache_storage_tiers.py`, `experimental/sgl-router/tests/e2e/infra/model_pool.py`_
- **2026-09-15** [`0e9b6bf8d8`](https://github.com/sgl-project/sglang/commit/0e9b6bf8d8) [#39322](https://github.com/sgl-project/sglang/pull/39322)
  [Router] Extract worker selection into policies::selection (no behavior change) (#39322)
  _Files: `experimental/sgl-router/src/policies/mod.rs`, `experimental/sgl-router/src/policies/selection.rs`, `experimental/sgl-router/src/server/routes/chat.rs`_
- **2026-09-15** [`6c514ab025`](https://github.com/sgl-project/sglang/commit/6c514ab025) [#39227](https://github.com/sgl-project/sglang/pull/39227)
  Force reasoning mode for GLM-5.3 chat templates (#39227)
  _Files: `python/sglang/srt/parser/template_detection.py`, `test/registered/unit/parser/test_template_manager.py`_
- **2026-09-15** [`45b511b2ef`](https://github.com/sgl-project/sglang/commit/45b511b2ef) [#39108](https://github.com/sgl-project/sglang/pull/39108)
  [Router] Honor KV-event storage tiers in the cache-aware tree (1/4) (#39108)
  _Files: `experimental/sgl-router/src/policies/kv_events/index.rs`, `experimental/sgl-router/src/policies/kv_events/mod.rs`, `experimental/sgl-router/src/policies/kv_events/tree.rs`, `experimental/sgl-router/tests/component/policies/kv_events_tree_concurrent.rs` _+1 more__
- **2026-09-15** [`fc4193a63c`](https://github.com/sgl-project/sglang/commit/fc4193a63c) [#38097](https://github.com/sgl-project/sglang/pull/38097)
  [HiCache] Remove duplicate benchmark result fields (#38097)
  _Files: `benchmark/hicache/bench_serving.py`_
- **2026-09-15** [`8874c51a96`](https://github.com/sgl-project/sglang/commit/8874c51a96) [#39284](https://github.com/sgl-project/sglang/pull/39284)
  [Benchmark] Add an opt-out for the token-capacity check (#39284)
  _Files: `python/sglang/benchmark/one_batch_server.py`_
- **2026-09-14** [`710a044caf`](https://github.com/sgl-project/sglang/commit/710a044caf) [#39483](https://github.com/sgl-project/sglang/pull/39483)
  [dLLM] Add rwang5203 as code owner and grant CI permissions (#39483)
  _Files: `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS`_
- **2026-09-14** [`7b4972a9cb`](https://github.com/sgl-project/sglang/commit/7b4972a9cb) [#39337](https://github.com/sgl-project/sglang/pull/39337)
  chore: add hzh0425 and xiezhq-hermann as Rust tree and HiSparse code owners (#39337)
  _Files: `.github/CODEOWNERS`_

## MoE / Expert Parallel  (37 commits)

- **2026-09-20** [`42875bcd2a`](https://github.com/sgl-project/sglang/commit/42875bcd2a) [#38932](https://github.com/sgl-project/sglang/pull/38932)
  fix(modelopt): dispatch NVFP4 MoE on the cached backend, not the live global (#38932)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4_moe_dispatch.py`_
- **2026-09-20** [`983e643854`](https://github.com/sgl-project/sglang/commit/983e643854) [#40448](https://github.com/sgl-project/sglang/pull/40448)
  [Feature] support bf16 MoE router and mxfp4 MoE for MiMo V2 (#40448)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/srt/models/mimo_v2.py`_
- **2026-09-20** [`d903351a66`](https://github.com/sgl-project/sglang/commit/d903351a66) [#38831](https://github.com/sgl-project/sglang/pull/38831)
  [NPU][bugfix] update low latency quantization input and update MXFP8 tests (#38831)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/moe/utils.py`, `test/registered/unit/npu/quantization/test_fp4_moe_methods.py`_
- **2026-09-19** [`9cc7da2ab0`](https://github.com/sgl-project/sglang/commit/9cc7da2ab0) [#38080](https://github.com/sgl-project/sglang/pull/38080)
  [MegaMoE] Wire Qwen MoE blocks to DeepGEMM MegaMoE (MXFP4 and NVFP4 experts) (#38080)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/mega_moe_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/pipeline.py` _+11 more__
- **2026-09-19** [`76f9213a41`](https://github.com/sgl-project/sglang/commit/76f9213a41) [#40353](https://github.com/sgl-project/sglang/pull/40353)
  [Fix] Keep mHC context out of non-V4 compiled MoE forwards (#40353)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-09-19** [`83e29d6c5a`](https://github.com/sgl-project/sglang/commit/83e29d6c5a) [#38220](https://github.com/sgl-project/sglang/pull/38220)
  [perf] Optimize w4a8 MoE for glm5.2 on H200 (#38220)
  _Files: `python/sglang/kernels/aot/csrc/moe/cutlass_moe/w4a8/w4a8_grouped_mm_c3x.cu`_
- **2026-09-19** [`7fac84b639`](https://github.com/sgl-project/sglang/commit/7fac84b639) [#39704](https://github.com/sgl-project/sglang/pull/39704)
  [DSV4.1] Reduce mHC, metadata and small-batch router overhead (#39704)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mhc_post_combine_norm_prefill.cuh`, `python/sglang/kernels/jit/csrc/distributed/all_reduce_fusion.cuh`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`, `python/sglang/kernels/ops/communication/all_reduce_mhc_combine.py` _+11 more__
- **2026-09-19** [`cb22f2451e`](https://github.com/sgl-project/sglang/commit/cb22f2451e) [#40265](https://github.com/sgl-project/sglang/pull/40265)
  [Cleanup] Deduplicate kernel tests, diffusion fixtures and benchmark helpers (#40265)
  _Files: `benchmark/kernels/attention/fa4_benchmark_utils.py`, `benchmark/kernels/deepep/deepep_utils.py`, `benchmark/kernels/deepep/tuning_deepep.py`, `benchmark/kernels/deepseek/benchmark_deepgemm_fp8_gemm.py` _+21 more__
- **2026-09-19** [`986959e3c4`](https://github.com/sgl-project/sglang/commit/986959e3c4) [#40197](https://github.com/sgl-project/sglang/pull/40197)
  [Refactor] Deduplicate kernel helpers and remove unused code (#40197)
  _Files: `python/sglang/kernels/jit/csrc/attention/kda_packed_decode.cuh`, `python/sglang/kernels/jit/csrc/inkling/inkling_ar_fused_decode.cuh`, `python/sglang/kernels/jit/csrc/inkling/inkling_ar_scattered_sconv.cuh`, `python/sglang/kernels/jit/csrc/moe/moe_align_kernel.cu` _+24 more__
- **2026-09-18** [`0e5347db82`](https://github.com/sgl-project/sglang/commit/0e5347db82) [#40030](https://github.com/sgl-project/sglang/pull/40030)
  Support MXFP8 and deferred route weighting in DeepEP v2 (#40030)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/kernels/ops/quantization/int8_kernel.py` _+16 more__
- **2026-09-18** [`7714b182f2`](https://github.com/sgl-project/sglang/commit/7714b182f2) [#40187](https://github.com/sgl-project/sglang/pull/40187)
  [Bugfix] Fix top-1 MoE routing with non-unit scaling (#40187)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`_
- **2026-09-18** [`81363bf8cb`](https://github.com/sgl-project/sglang/commit/81363bf8cb) [#36176](https://github.com/sgl-project/sglang/pull/36176)
  [kernel] Share the warp vectorized copy and enforce its alignment (#36176)
  _Files: `.claude/skills/add-jit-kernel/SKILL.md`, `python/sglang/kernels/jit/benchmark/marker.py`, `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/candidate_block_table.cuh` _+30 more__
- **2026-09-18** [`d6090f92bf`](https://github.com/sgl-project/sglang/commit/d6090f92bf) [#39881](https://github.com/sgl-project/sglang/pull/39881)
  [NPU] Fuse MXFP4 W4A8 MoE gmm1 + swiglu + requant into one kernel (#39881)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py`, `python/sglang/srt/layers/moe/moe_runner/ascend.py`_
- **2026-09-18** [`1e8699fda3`](https://github.com/sgl-project/sglang/commit/1e8699fda3) [#32963](https://github.com/sgl-project/sglang/pull/32963)
  [NVIDIA][comm] Merge EP+MoE-TP post-experts all-reduces into one _TP reduction (#32963)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `python/sglang/srt/layers/moe/__init__.py`, `python/sglang/srt/layers/moe/utils.py` _+5 more__
- **2026-09-18** [`8ac39c66d8`](https://github.com/sgl-project/sglang/commit/8ac39c66d8) [#39589](https://github.com/sgl-project/sglang/pull/39589)
  [NPU] support kimi k3 on A5 and improve performance (#39589)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_accept.py`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/parallel.py`, `python/sglang/srt/arg_groups/parallel_hook.py` _+23 more__
- **2026-09-18** [`c46bf5e990`](https://github.com/sgl-project/sglang/commit/c46bf5e990) [#40105](https://github.com/sgl-project/sglang/pull/40105)
  [MoE] Disable FlashInfer fused finalize by default for numerical accuracy (#40105)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`_
- **2026-09-18** [`0dad91d50f`](https://github.com/sgl-project/sglang/commit/0dad91d50f) [#35260](https://github.com/sgl-project/sglang/pull/35260)
  Fix int4 MoE tuner config filename (#35260)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`, `test/registered/unit/layers/moe/test_fused_moe_triton_config.py`_
- **2026-09-18** [`826d5170ae`](https://github.com/sgl-project/sglang/commit/826d5170ae) [#38780](https://github.com/sgl-project/sglang/pull/38780)
  [Bug] Guard FlashInfer CUTLASS MoE against 0-token inputs (#38780)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutlass.py`_
- **2026-09-17** [`e970453b43`](https://github.com/sgl-project/sglang/commit/e970453b43) [#38420](https://github.com/sgl-project/sglang/pull/38420)
  [NPU]Refactor weight processing and add NPUSwigluLimit activation (#38420)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/activation.py`, `python/sglang/srt/hardware_backend/npu/quantization/fp4_moe_methods.py`, `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py`, `python/sglang/srt/layers/moe/moe_runner/ascend.py` _+2 more__
- **2026-09-17** [`aebae58b8c`](https://github.com/sgl-project/sglang/commit/aebae58b8c) [#39920](https://github.com/sgl-project/sglang/pull/39920)
  [Moe] Fix flashinfer_trtllm silently dropping swiglu_limit clamped SwiGLU activation (#39920)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`_
- **2026-09-17** [`44bd359082`](https://github.com/sgl-project/sglang/commit/44bd359082) [#39382](https://github.com/sgl-project/sglang/pull/39382)
  [NPU][Diffusion] Optimize SenseNova-U1 batched generation (#39382)
  _Files: `docs/cookbook/diffusion/SenseNova/SenseNova-U1.5-8B-MoT.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/sensenova_u1.py`, `python/sglang/multimodal_gen/configs/sample/sensenova_u1.py` _+7 more__
- **2026-09-17** [`fa8d22e665`](https://github.com/sgl-project/sglang/commit/fa8d22e665) [#39910](https://github.com/sgl-project/sglang/pull/39910)
  [AMD][DSV4] Allow moe_a2a_backend='mori' with DSpark + dp attention (#39910)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`_
- **2026-09-17** [`241a5b9823`](https://github.com/sgl-project/sglang/commit/241a5b9823) [#36576](https://github.com/sgl-project/sglang/pull/36576)
  MiniMax-M3: allow shared-experts fusion on ROCm gfx942 and newer (#36576)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`_
- **2026-09-17** [`84d7604b7e`](https://github.com/sgl-project/sglang/commit/84d7604b7e) [#39439](https://github.com/sgl-project/sglang/pull/39439)
  [XPU] weekly simple model enablement 2026/09/14 (#39439)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_flash_with_topk_idx.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/tests/test_sparse_gqa.py` _+7 more__
- **2026-09-16** [`f0bf652534`](https://github.com/sgl-project/sglang/commit/f0bf652534) [#38526](https://github.com/sgl-project/sglang/pull/38526)
  Add Ling-3.0-flash-VL model support (#38526)
  _Files: `python/sglang/kernels/ops/attention/rotary_triton.py`, `python/sglang/srt/arg_groups/model_overrides/__init__.py`, `python/sglang/srt/arg_groups/model_overrides/bailing_moe_v3.py`, `python/sglang/srt/arg_groups/overrides.py` _+33 more__
- **2026-09-16** [`a3bf25dc62`](https://github.com/sgl-project/sglang/commit/a3bf25dc62) [#39763](https://github.com/sgl-project/sglang/pull/39763)
  [AMD] Clamp MORI intranode grid GPUs (#39763)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`_
- **2026-09-16** [`fc5a979f21`](https://github.com/sgl-project/sglang/commit/fc5a979f21) [#39678](https://github.com/sgl-project/sglang/pull/39678)
  [misc] Merge FlashInfer autotune caches across spec workers, pad MXFP4 TP shards, drop dead ngram attrs (#39678)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/mxfp4_flashinfer_trtllm_moe.py`, `python/sglang/srt/managers/scheduler.py` _+2 more__
- **2026-09-16** [`a64be2e430`](https://github.com/sgl-project/sglang/commit/a64be2e430) [#38913](https://github.com/sgl-project/sglang/pull/38913)
  [Kernel] Add H20 block-FP8 MoE configs for GLM-5.3-Flash EP4/EP8 (#38913)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=36,N=2048,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=72,N=2048,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`_
- **2026-09-16** [`935cbf24ec`](https://github.com/sgl-project/sglang/commit/935cbf24ec) [#39613](https://github.com/sgl-project/sglang/pull/39613)
  Accept MXFP8 dispatch in FlashInfer A2A TRT-LLM MoE (#39613)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`_
- **2026-09-16** [`d4ad368ed9`](https://github.com/sgl-project/sglang/commit/d4ad368ed9) [#28723](https://github.com/sgl-project/sglang/pull/28723)
  [Intel XPU] Enable fused_moe_triton tuning on XPU and add tuned DeepSeek-OCR-2 configs (#28723)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton_sep.py`, `python/pyproject_xpu.toml`, `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py` _+3 more__
- **2026-09-16** [`f920be4b09`](https://github.com/sgl-project/sglang/commit/f920be4b09) [#39155](https://github.com/sgl-project/sglang/pull/39155)
  [AMD] GLM-5.2 NextN: cast draft fused MoE to per-channel FP8 (#39155)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8_moe.py`, `python/sglang/srt/models/glm4_moe.py`, `test/registered/unit/models/test_glm_nextn_moe_ptpc.py`_
- **2026-09-15** [`0dabef3d30`](https://github.com/sgl-project/sglang/commit/0dabef3d30) [#39574](https://github.com/sgl-project/sglang/pull/39574)
  [misc] Fix tool-call index, graph padded-row count, and prefill-graph input_embeds refresh (#39574)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/model_executor/runner/base_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+4 more__
- **2026-09-15** [`406c9c71d8`](https://github.com/sgl-project/sglang/commit/406c9c71d8) [#38160](https://github.com/sgl-project/sglang/pull/38160)
  [Feature] Support BF16 and batch-invariant inference with DeepEP v2 (#38160)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/arg_groups/moe_hook.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` _+12 more__
- **2026-09-15** [`17ba2c2e7c`](https://github.com/sgl-project/sglang/commit/17ba2c2e7c) [#38890](https://github.com/sgl-project/sglang/pull/38890)
  Support non-strict GLM47 tool calls with EBNF constraints (#38890)
  _Files: `python/sglang/srt/constrained/base_grammar_backend.py`, `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/constrained/reasoner_grammar_backend.py`, `python/sglang/srt/entrypoints/openai/protocol.py` _+10 more__
- **2026-09-15** [`37ebacb50f`](https://github.com/sgl-project/sglang/commit/37ebacb50f) [#31804](https://github.com/sgl-project/sglang/pull/31804)
  [EPLB] Drop defensive getattr for ep_dispatch_algorithm (#31804)
  _Files: `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/unit/eplb/test_waterfill_eplb.py`_
- **2026-09-15** [`e687b8d6af`](https://github.com/sgl-project/sglang/commit/e687b8d6af) [#37748](https://github.com/sgl-project/sglang/pull/37748)
  [CPU] Implement fused QK Norm and RoPE kernels (#37748)
  _Files: `python/sglang/kernels/aot/csrc/cpu/norm.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/utils.py` _+1 more__
- **2026-09-15** [`5dde6e8f02`](https://github.com/sgl-project/sglang/commit/5dde6e8f02) [#39223](https://github.com/sgl-project/sglang/pull/39223)
  Fix MegaMoE buffer allocation and caching for effective SM budgets (#39223)
  _Files: `python/sglang/srt/layers/moe/mega_moe.py`, `test/registered/unit/layers/moe/test_mega_moe_deepgemm_api.py`_

## Multimodal  (32 commits)

- **2026-09-21** [`50ec9702d0`](https://github.com/sgl-project/sglang/commit/50ec9702d0) [#40573](https://github.com/sgl-project/sglang/pull/40573)
  [diffusion] docs: update ComfyUI sections, trimmed examples, and the RTX 5090 DiT-resident recipe (1.42x) for Qwen-Image-2.1 cookbook (#40573)
  _Files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-review-pr/SKILL.md`, `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `docs/cookbook/diffusion/Ernie-Image/Ernie-Image.mdx` _+19 more__
- **2026-09-21** [`8faa2d6731`](https://github.com/sgl-project/sglang/commit/8faa2d6731) [#40544](https://github.com/sgl-project/sglang/pull/40544)
  [NPU][Diffusion] Disable loading latency checks in Ascend fixtures (#40544)
  _Files: `python/sglang/multimodal_gen/test/server/ascend/conftest.py`_
- **2026-09-21** [`c2f860af1c`](https://github.com/sgl-project/sglang/commit/c2f860af1c) [#39956](https://github.com/sgl-project/sglang/pull/39956)
  [ci][xpu] Record device time in the multimodal_gen perf lane (#39956)
  _Files: `.github/workflows/pr-test-xpu.yml`, `python/sglang/multimodal_gen/test/server/perf_baselines/xpu_b60.json`_
- **2026-09-21** [`292e3ccc0c`](https://github.com/sgl-project/sglang/commit/292e3ccc0c) [#39955](https://github.com/sgl-project/sglang/pull/39955)
  [ci][xpu] Re-seed the wan2_1_t2v_1.3b perf baseline on Arc Pro B60 (#39955)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines/xpu_b60.json`_
- **2026-09-21** [`1da8ac10e1`](https://github.com/sgl-project/sglang/commit/1da8ac10e1) [#33649](https://github.com/sgl-project/sglang/pull/33649)
  Update to the cookbook for XPU-supported models (#33649)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-OCR-2.mdx`, `docs/cookbook/autoregressive/Google/Gemma4.mdx`, `docs/cookbook/autoregressive/Meta/Llama3.1.mdx`, `docs/cookbook/autoregressive/Meta/Llama3.3-70B.mdx` _+15 more__
- **2026-09-21** [`6ad78f2281`](https://github.com/sgl-project/sglang/commit/6ad78f2281) [#40487](https://github.com/sgl-project/sglang/pull/40487)
  [diffusion] docs: add verified DGX Spark recipe for Qwen-Image 2.1 (#40487)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/src/snippets/configs/Qwen/qwen-image-2.1.jsx`_
- **2026-09-21** [`b912db67ea`](https://github.com/sgl-project/sglang/commit/b912db67ea) [#40472](https://github.com/sgl-project/sglang/pull/40472)
  [diffusion] fix: keep Qwen-Image 2.1 prefix KV per layer under Cache-DiT (#40472)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/docs/sglang-diffusion/cache_dit.mdx`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image21.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py`_
- **2026-09-21** [`3a0324fb9b`](https://github.com/sgl-project/sglang/commit/3a0324fb9b) [#40481](https://github.com/sgl-project/sglang/pull/40481)
  [diffusion] optimization: reduce Qwen-Image 2.1 vae and graph warmup memory (#40481)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/autoencoder_kl_qwenimage21.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/qwen_image21.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21_cuda.py`_
- **2026-09-20** [`791c7850d0`](https://github.com/sgl-project/sglang/commit/791c7850d0) [#39705](https://github.com/sgl-project/sglang/pull/39705)
  [Diffusion] Enable shared RMSNorm dispatch for SenseNova-U1 (#39705)
  _Files: `python/sglang/multimodal_gen/runtime/models/sensenova_u1/neo_unify/modeling_qwen3.py`, `python/sglang/multimodal_gen/test/unit/test_sensenova_u1.py`, `python/sglang/srt/layers/layernorm.py`_
- **2026-09-20** [`414adef060`](https://github.com/sgl-project/sglang/commit/414adef060) [#40293](https://github.com/sgl-project/sglang/pull/40293)
  [CI] skip srt rust extension builds for diffusion-only PRs (#40293)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/pr-test-multimodal-gen.yml`, `.github/workflows/pr-test.yml`, `scripts/ci/cuda/ci_install_dependency.sh` _+1 more__
- **2026-09-20** [`2d216a11f8`](https://github.com/sgl-project/sglang/commit/2d216a11f8) [#38996](https://github.com/sgl-project/sglang/pull/38996)
  [Model] Serve DeepSeek-OCR-2 with its official 768px local-crop geometry (#38996)
  _Files: `python/sglang/srt/configs/deepseek_ocr.py`, `python/sglang/srt/models/deepseek_ocr.py`, `python/sglang/srt/multimodal/processors/deepseek_ocr.py`, `test/registered/unit/multimodal/test_deepseek_ocr_geometry.py`_
- **2026-09-20** [`031bff5dd3`](https://github.com/sgl-project/sglang/commit/031bff5dd3) [#40408](https://github.com/sgl-project/sglang/pull/40408)
  [diffusion] chore: batch qwen-image 2.1 targets and document measured deployment recipes (#40408)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs/docs/sglang-diffusion/dynamic_batching.mdx`, `docs/src/snippets/_deployment.jsx` _+6 more__
- **2026-09-19** [`090263eff6`](https://github.com/sgl-project/sglang/commit/090263eff6) [#38750](https://github.com/sgl-project/sglang/pull/38750)
  [VLM] avoid CUDA placement on non-CUDA platforms (#38750)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `test/registered/unit/managers/test_mm_process_config.py`, `test/registered/unit/multimodal/test_processor_device_selection.py`_
- **2026-09-19** [`81421b91e9`](https://github.com/sgl-project/sglang/commit/81421b91e9) [#40069](https://github.com/sgl-project/sglang/pull/40069)
  One read path for every parallel name (#40069)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/runtime_context.py`, `test/registered/unit/server_args/test_resolution_declarations.py` _+1 more__
- **2026-09-18** [`2394b231c2`](https://github.com/sgl-project/sglang/commit/2394b231c2) [#39185](https://github.com/sgl-project/sglang/pull/39185)
  Fix Mistral3 retaining every vision-tower layer to read one (#39185)
  _Files: `python/sglang/srt/models/llava.py`, `python/sglang/srt/models/mistral.py`, `test/registered/unit/models/test_mistral3_vision_feature.py`_
- **2026-09-18** [`5e4b94b134`](https://github.com/sgl-project/sglang/commit/5e4b94b134) [#40005](https://github.com/sgl-project/sglang/pull/40005)
  [MM] Skip VMM error gathers for text-only requests (#40005)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/multimodal/test_gpu_feature_transport.py`_
- **2026-09-18** [`9784d5f979`](https://github.com/sgl-project/sglang/commit/9784d5f979) [#39883](https://github.com/sgl-project/sglang/pull/39883)
  [diffusion] doc: sync CFG and tracing documentation (#39883)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/cookbook/diffusion/SANA-WM/SANA-WM.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`_
- **2026-09-18** [`2dee23a876`](https://github.com/sgl-project/sglang/commit/2dee23a876) [#35573](https://github.com/sgl-project/sglang/pull/35573)
  [ROCm][diffusion] Enable fused qk norm and rope on ROCm (#35573)
  _Files: `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py`_
- **2026-09-17** [`25c9f724d4`](https://github.com/sgl-project/sglang/commit/25c9f724d4) [#30368](https://github.com/sgl-project/sglang/pull/30368)
  fix(multimodal): handle tensor images in exact-token preprocessing (#30368)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `test/registered/vlm/test_token_id_retokenize_e2e.py`_
- **2026-09-17** [`f3c0256771`](https://github.com/sgl-project/sglang/commit/f3c0256771) [#39884](https://github.com/sgl-project/sglang/pull/39884)
  [diffusion] chore: remove retired auto-residency workload helpers (#39884)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/auto_residency.py`, `python/sglang/multimodal_gen/test/unit/test_auto_residency.py`_
- **2026-09-17** [`2733afe54e`](https://github.com/sgl-project/sglang/commit/2733afe54e) [#36825](https://github.com/sgl-project/sglang/pull/36825)
  [diffusion] Fix the XPU capability gates that broke the Wan2.2 A14B DiT path (#36825)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/common/platform.py`, `python/sglang/kernels/ops/diffusion/layout/wan_causal_cache_triton.py`, `python/sglang/kernels/ops/diffusion/modulate/scale_shift_triton.py` _+8 more__
- **2026-09-17** [`c89c63fa38`](https://github.com/sgl-project/sglang/commit/c89c63fa38) [#39668](https://github.com/sgl-project/sglang/pull/39668)
  dsv4.1: vision tower and image preprocessing (#39668)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/deepseek_v41_vit.py`, `python/sglang/srt/multimodal/deepseek_v41_image_processing.py`, `python/sglang/srt/multimodal/processors/deepseek_v41.py` _+2 more__
- **2026-09-16** [`2cb51f5d22`](https://github.com/sgl-project/sglang/commit/2cb51f5d22) [#33452](https://github.com/sgl-project/sglang/pull/33452)
  [CPU] [Diffusion] Add fused scale-shift and norm kernels for CPU (#33452)
  _Files: `python/sglang/kernels/aot/csrc/cpu/normd.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/kernels/ops/diffusion/modulate/scale_shift_triton.py`, `python/sglang/multimodal_gen/runtime/layers/custom_op.py` _+2 more__
- **2026-09-15** [`b803cfa0c4`](https://github.com/sgl-project/sglang/commit/b803cfa0c4) [#39329](https://github.com/sgl-project/sglang/pull/39329)
  Add external multimodal processors to the Rust frontend (#39329)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/rust_server/server.py`, `rust/sglang-mm/src/pipeline.rs` _+16 more__
- **2026-09-15** [`1aeeb25e86`](https://github.com/sgl-project/sglang/commit/1aeeb25e86) [#39585](https://github.com/sgl-project/sglang/pull/39585)
  [NPU][CI] Scope NPU nightly artifact dirs by image; fix stale glm5_2 case (#39585)
  _Files: `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu-e2e-multi-node.yml`, `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`_
- **2026-09-15** [`fb01a079a6`](https://github.com/sgl-project/sglang/commit/fb01a079a6) [#39411](https://github.com/sgl-project/sglang/pull/39411)
  [NPU] [CI] Fix multimodal_gen filter leakage and add daily scheduled run (#39411)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-09-15** [`b510881157`](https://github.com/sgl-project/sglang/commit/b510881157) [#39278](https://github.com/sgl-project/sglang/pull/39278)
  [Fix][Qwen-VL] Normalize <image> sentinel on artifact fast path (#39278)
  _Files: `python/sglang/srt/multimodal/processors/qwen_vl.py`_
- **2026-09-15** [`c9fbe5f655`](https://github.com/sgl-project/sglang/commit/c9fbe5f655) [#39148](https://github.com/sgl-project/sglang/pull/39148)
  [MM] Add flag to force Kimi image preprocessing onto CPU (#39148)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/multimodal/processors/kimi_k25.py`_
- **2026-09-15** [`a25f213bc4`](https://github.com/sgl-project/sglang/commit/a25f213bc4) [#39373](https://github.com/sgl-project/sglang/pull/39373)
  [diffusion] docs: give the RTX 5090 its own H3 recipe, measured on a physical desktop (#39373)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx`_
- **2026-09-14** [`39e147443b`](https://github.com/sgl-project/sglang/commit/39e147443b) [#39145](https://github.com/sgl-project/sglang/pull/39145)
  [Session] Fix image append positions and parent metadata (#39145)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/sessions/test_session_control.py`_
- **2026-09-14** [`42b5af8c62`](https://github.com/sgl-project/sglang/commit/42b5af8c62) [#39244](https://github.com/sgl-project/sglang/pull/39244)
  [diffusion] docs: refresh the VDN-H3 on b200 numbers in cookbook (#39244)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/runtime/utils/model_overlay.py`_
- **2026-09-14** [`3480112a9c`](https://github.com/sgl-project/sglang/commit/3480112a9c) [#39303](https://github.com/sgl-project/sglang/pull/39303)
  [diffusion] fix: serve requests that turn cfg off on a cfg-parallel server (#39303)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/input_validation.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/runtime/utils/logging_utils.py`, `python/sglang/multimodal_gen/test/unit/test_cfg_parallel_warmup.py` _+1 more__

## KV Cache / Memory  (27 commits)

- **2026-09-20** [`4a9dc5c4af`](https://github.com/sgl-project/sglang/commit/4a9dc5c4af) [#40272](https://github.com/sgl-project/sglang/pull/40272)
  [sgl-router] refactor - move policy-required states under src/state (#40272)
  _Files: `experimental/sgl-router/benches/tree_lookup.rs`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs` _+74 more__
- **2026-09-20** [`efa7be2091`](https://github.com/sgl-project/sglang/commit/efa7be2091) [#40418](https://github.com/sgl-project/sglang/pull/40418)
  [Simulator][Compatibility] Adapt to latest KV cache pool interfaces (#40418)
  _Files: `tools/sglang-simulator/src/sglang_simulator/simulation/sglang/model_runner.py`, `tools/sglang-simulator/test/test_simulation_cache_hit_ratio.py`, `tools/sglang-simulator/test/test_simulation_sglang_runner.py`_
- **2026-09-20** [`9f3d275940`](https://github.com/sgl-project/sglang/commit/9f3d275940) [#37870](https://github.com/sgl-project/sglang/pull/37870)
  [HiCache] Fix sparse hybrid transfer layer IDs (#37870)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py` _+6 more__
- **2026-09-20** [`e54009240a`](https://github.com/sgl-project/sglang/commit/e54009240a) [#38901](https://github.com/sgl-project/sglang/pull/38901)
  [AMD][DSV4] feat: enable DSpark with fp8 unified_kv on gfx950 (#38901)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/e2e/dsv4/test_dsv4_unified_fp8_scatter.py` _+2 more__
- **2026-09-20** [`a8a4d86be9`](https://github.com/sgl-project/sglang/commit/a8a4d86be9) [#40313](https://github.com/sgl-project/sglang/pull/40313)
  Remove swa and mamba radix cache (#40313)
  _Files: `python/sglang/srt/arg_groups/mamba_hook.py`, `python/sglang/srt/arg_groups/model_overrides/qwen4_exp.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/kv_canary/radix_cache_walker.py` _+20 more__
- **2026-09-20** [`df0dc44931`](https://github.com/sgl-project/sglang/commit/df0dc44931) [#40354](https://github.com/sgl-project/sglang/pull/40354)
  [Fix] Forward SWA prealloc reclaim through the DSV4 HiSparse allocator (#40354)
  _Files: `python/sglang/srt/mem_cache/allocator/hisparse.py`, `test/registered/unit/mem_cache/test_hisparse_allocator.py`_
- **2026-09-19** [`9e5a62a767`](https://github.com/sgl-project/sglang/commit/9e5a62a767) [#40038](https://github.com/sgl-project/sglang/pull/40038)
  [Logprob] Serve input-logprob temporaries from CUDA-graph-pool dead space (#40038)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/logprob_processor.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/utils.py` _+6 more__
- **2026-09-18** [`f3851486cb`](https://github.com/sgl-project/sglang/commit/f3851486cb) [#38948](https://github.com/sgl-project/sglang/pull/38948)
  [Perf] Fuse SWA page lookup and mapping clear (#38948)
  _Files: `python/sglang/kernels/ops/memory/allocator.py`, `python/sglang/srt/mem_cache/allocator/swa.py`, `test/registered/kernels/ops/memory/test_swa_page_free.py`, `test/registered/unit/mem_cache/test_swa_unittest.py`_
- **2026-09-18** [`81a199f56a`](https://github.com/sgl-project/sglang/commit/81a199f56a) [#40013](https://github.com/sgl-project/sglang/pull/40013)
  [HiCache] Read the in-flight buffer backup's node id from its snapshot in sanity_check (#40013)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-18** [`a0534f8cca`](https://github.com/sgl-project/sglang/commit/a0534f8cca) [#40042](https://github.com/sgl-project/sglang/pull/40042)
  [HiCache] Stop arming a prefetch retry for a too-short storage span (#40042)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-18** [`f5a1434700`](https://github.com/sgl-project/sglang/commit/f5a1434700) [#40239](https://github.com/sgl-project/sglang/pull/40239)
  [HiCache] Document transfer arguments (#40239)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py`, `rust/sglang-radix-tree/src/tests/components/mamba.rs`_
- **2026-09-18** [`6a9c7001d3`](https://github.com/sgl-project/sglang/commit/6a9c7001d3) [#40007](https://github.com/sgl-project/sglang/pull/40007)
  [Logprob] Borrow graph-pool memory for input logprob logits construction (#40007)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/logprob_processor.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/runner_utils/pool.py` _+4 more__
- **2026-09-18** [`191172fa74`](https://github.com/sgl-project/sglang/commit/191172fa74) [#39980](https://github.com/sgl-project/sglang/pull/39980)
  [Unified Tree] fix: exempt host-locked aux nodes from the sanity_check host-LRU check (#39980)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `rust/sglang-radix-tree/src/tests/unified_tree_core.rs`, `rust/sglang-radix-tree/src/unified_tree_core.rs`_
- **2026-09-18** [`20518d8518`](https://github.com/sgl-project/sglang/commit/20518d8518) [#35204](https://github.com/sgl-project/sglang/pull/35204)
  [Scheduler] Align `RadixCache` no-insert cleanup with `kv_len_to_handle` (#35204)
  _Files: `python/sglang/srt/mem_cache/radix_cache.py`, `test/registered/unit/mem_cache/test_decode_radix_lock_ref.py`_
- **2026-09-17** [`6ca866ea29`](https://github.com/sgl-project/sglang/commit/6ca866ea29) [#39050](https://github.com/sgl-project/sglang/pull/39050)
  [HiCache][Perf] fix: batch HiCache D2H submits per step for hybrid pools (#39050)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/pool_host/mamba.py` _+4 more__
- **2026-09-17** [`1a90ae6727`](https://github.com/sgl-project/sglang/commit/1a90ae6727) [#34012](https://github.com/sgl-project/sglang/pull/34012)
  Add Agentic-Aware Tail-Optimized LRU eviction to the unified radix cache (#34012)
  _Files: `docs/docs/advanced_features/radix_eviction_policy.mdx`, `python/sglang/srt/arg_groups/choices.py`, `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py` _+5 more__
- **2026-09-17** [`8ae4a39b50`](https://github.com/sgl-project/sglang/commit/8ae4a39b50) [#37474](https://github.com/sgl-project/sglang/pull/37474)
  Gate mamba extra-buffer predicates on uses_mamba_radix_cache (#37474)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/model_overrides/inkling.py`, `python/sglang/srt/arg_groups/overrides.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-09-17** [`6460082c05`](https://github.com/sgl-project/sglang/commit/6460082c05) [#39115](https://github.com/sgl-project/sglang/pull/39115)
  [Mamba] Fix checkpoint depth for prefixes that end off the radix page (#39115)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_mamba_checkpoint_depth.py`_
- **2026-09-17** [`4793f56835`](https://github.com/sgl-project/sglang/commit/4793f56835) [#39699](https://github.com/sgl-project/sglang/pull/39699)
  [HiCache] Keep hybrid transfer layer maps stage-local under PP (#39699)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`_
- **2026-09-16** [`0e528dc9ff`](https://github.com/sgl-project/sglang/commit/0e528dc9ff) [#39426](https://github.com/sgl-project/sglang/pull/39426)
  bugfix:fix unifiedcache c128 radix cache management (#39426)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/c128_sidecar_component.py`, `python/sglang/srt/mem_cache/unified_cache/components/base.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-09-16** [`6b33338242`](https://github.com/sgl-project/sglang/commit/6b33338242) [#39567](https://github.com/sgl-project/sglang/pull/39567)
  [HiCache] Forward prefix metadata to v2 storage calls (#39567)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`_
- **2026-09-16** [`4e9e407d37`](https://github.com/sgl-project/sglang/commit/4e9e407d37) [#39280](https://github.com/sgl-project/sglang/pull/39280)
  [HiCache] Label radix-cache metrics per rank and split the "shrunk" prefetch reason (#39280)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `python/sglang/srt/observability/metrics_collector.py` _+3 more__
- **2026-09-15** [`49f540f3c0`](https://github.com/sgl-project/sglang/commit/49f540f3c0) [#39480](https://github.com/sgl-project/sglang/pull/39480)
  [HiCache] Optimize buffer-mode storage existence bookkeeping (#39480)
  _Files: `python/sglang/srt/mem_cache/buffer_mode/storage_existence_cache.py`_
- **2026-09-15** [`ddd4600197`](https://github.com/sgl-project/sglang/commit/ddd4600197) [#39516](https://github.com/sgl-project/sglang/pull/39516)
  [Fix] HiCache startup ImportError on the pinned kernel wheel (#39516)
  _Files: `python/sglang/srt/mem_cache/pool_host/common.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/kernels/ops/kvcache/test_hicache_page_first_write_back.py`_
- **2026-09-14** [`f81fbc749a`](https://github.com/sgl-project/sglang/commit/f81fbc749a) [#38941](https://github.com/sgl-project/sglang/pull/38941)
  [Fix] Merge adjacent KV-row frees so a mid-page split under DCP cannot double-free (#38941)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/common.py`, `test/registered/unit/mem_cache/test_free_kv_row_coalesce.py`_
- **2026-09-14** [`5200508b0f`](https://github.com/sgl-project/sglang/commit/5200508b0f) [#32888](https://github.com/sgl-project/sglang/pull/32888)
  [AMD][gfx95] Fill the chunked-prefill compute budget exactly (#32888)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_policy.py`_
- **2026-09-14** [`0d95a9c1ff`](https://github.com/sgl-project/sglang/commit/0d95a9c1ff) [#38925](https://github.com/sgl-project/sglang/pull/38925)
  [HiCache] Keep the file backend temp file name within NAME_MAX (#38925)
  _Files: `python/sglang/srt/mem_cache/hicache_storage.py`_

## Scheduler / Batching  (17 commits)

- **2026-09-20** [`22f02cc339`](https://github.com/sgl-project/sglang/commit/22f02cc339) [#40411](https://github.com/sgl-project/sglang/pull/40411)
  [Test] Fix scheduler fixtures after prefill burst counting (#40411)
  _Files: `test/registered/unit/managers/test_auxiliary_output.py`, `test/registered/unit/managers/test_disagg_idle_step_counters.py`_
- **2026-09-19** [`8139a1740e`](https://github.com/sgl-project/sglang/commit/8139a1740e) [#40006](https://github.com/sgl-project/sglang/pull/40006)
  [Scheduler] Count complete prefill bursts and their tokens (#40006)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-09-19** [`111aeedd37`](https://github.com/sgl-project/sglang/commit/111aeedd37) [#40222](https://github.com/sgl-project/sglang/pull/40222)
  [Runtime] Add decode CUDA graph hooks for eager logits processing (#40222)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/graph_shared_output.py`, `python/sglang/srt/model_executor/model_runner.py` _+4 more__
- **2026-09-18** [`fa521e2758`](https://github.com/sgl-project/sglang/commit/fa521e2758) [#40010](https://github.com/sgl-project/sglang/pull/40010)
  [MM] Copy placeholder ids to CUDA asynchronously (#40010)
  _Files: `python/sglang/srt/managers/mm_utils.py`_
- **2026-09-18** [`6e1d9c1464`](https://github.com/sgl-project/sglang/commit/6e1d9c1464) [#40098](https://github.com/sgl-project/sglang/pull/40098)
  [profiler] Ignore PREBUILT batches in profile-by-stage (#40098)
  _Files: `python/sglang/srt/managers/scheduler_components/profiler_manager.py`_
- **2026-09-18** [`65ef55e2a8`](https://github.com/sgl-project/sglang/commit/65ef55e2a8) [#40024](https://github.com/sgl-project/sglang/pull/40024)
  [Scheduler] Add shortest-prefill-first scheduling (#40024)
  _Files: `python/sglang/srt/arg_groups/fields/schedule.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_prefill_adder.py` _+2 more__
- **2026-09-18** [`0214954f26`](https://github.com/sgl-project/sglang/commit/0214954f26) [#39915](https://github.com/sgl-project/sglang/pull/39915)
  [gRPC] Stream engine state changes (#39915)
  _Files: `proto/sglang/runtime/v1/sglang.proto`, `python/sglang/srt/entrypoints/grpc_bridge.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `rust/sglang-grpc/src/bridge.rs` _+2 more__
- **2026-09-17** [`3401b75240`](https://github.com/sgl-project/sglang/commit/3401b75240) [#39666](https://github.com/sgl-project/sglang/pull/39666)
  dsv4.1: Engram module and request history support (#39666)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/engram.py`, `python/sglang/srt/managers/schedule_batch.py` _+4 more__
- **2026-09-17** [`33d46376a6`](https://github.com/sgl-project/sglang/commit/33d46376a6) [#38504](https://github.com/sgl-project/sglang/pull/38504)
  [HiCache] Yield idle scheduler so storage workers can drain (#38504)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_on_idle_load.py`_
- **2026-09-16** [`f45aad44bd`](https://github.com/sgl-project/sglang/commit/f45aad44bd) [#37488](https://github.com/sgl-project/sglang/pull/37488)
  [gRPC] Expose native pause status (#37488)
  _Files: `proto/sglang/runtime/v1/sglang.proto`, `python/sglang/srt/entrypoints/grpc_bridge.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+7 more__
- **2026-09-16** [`5f6dd44edc`](https://github.com/sgl-project/sglang/commit/5f6dd44edc) [#39561](https://github.com/sgl-project/sglang/pull/39561)
  [NPU] [bugfix] Fix undefined require_attn_tp_allgather (#39561)
  _Files: `python/sglang/srt/managers/scheduler_pp_mixin.py`_
- **2026-09-15** [`d58342deab`](https://github.com/sgl-project/sglang/commit/d58342deab) [#39560](https://github.com/sgl-project/sglang/pull/39560)
  [Fix] Release NCCL on scheduler exit and let the ASGI server own shutdown (#39560)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+1 more__
- **2026-09-15** [`073fdf97cc`](https://github.com/sgl-project/sglang/commit/073fdf97cc) [#39164](https://github.com/sgl-project/sglang/pull/39164)
  Generalize auxiliary outputs (#39164)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/managers/auxiliary_output.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/utils.py` _+3 more__
- **2026-09-15** [`4f52c9948b`](https://github.com/sgl-project/sglang/commit/4f52c9948b) [#38176](https://github.com/sgl-project/sglang/pull/38176)
  keeping router GEMM in fp32 for deterministic inference (DeepSeek V3/V4) (#38176)
  _Files: `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/models/deepseek_v2.py`_
- **2026-09-15** [`06992c92ad`](https://github.com/sgl-project/sglang/commit/06992c92ad) [#39534](https://github.com/sgl-project/sglang/pull/39534)
  [Fix] Aggregate all IPC weight update responses (#39534)
  _Files: `python/sglang/srt/managers/tokenizer_control_mixin.py`_
- **2026-09-14** [`6e755e4114`](https://github.com/sgl-project/sglang/commit/6e755e4114) [#36625](https://github.com/sgl-project/sglang/pull/36625)
  [Logging] Downgrade missing TokenizerManager request state log to warning (#36625)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-09-14** [`2fca6d69aa`](https://github.com/sgl-project/sglang/commit/2fca6d69aa) [#39371](https://github.com/sgl-project/sglang/pull/39371)
  bumping sgl-deep-gemm to 0.2.0 (#39371)
  _Files: `python/pyproject.toml`, `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `test/registered/unit/batch_invariant_ops/test_batch_invariant_ops.py`_

## Quantization  (15 commits)

- **2026-09-21** [`62ba964848`](https://github.com/sgl-project/sglang/commit/62ba964848) [#38779](https://github.com/sgl-project/sglang/pull/38779)
  Fix: post-load staging regression breaks offload meta/sharded_gpu modes (#38779)
  _Files: `python/sglang/srt/model_loader/post_load.py`, `test/registered/unit/test_quantization_post_load.py`_
- **2026-09-20** [`6880a47955`](https://github.com/sgl-project/sglang/commit/6880a47955) [#40455](https://github.com/sgl-project/sglang/pull/40455)
  [diffusion] docs: simplify Qwen-Image 2.1 cookbook (#40455)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs/docs/sglang-diffusion/dynamic_batching.mdx`, `docs/docs/sglang-diffusion/quantization.mdx` _+1 more__
- **2026-09-19** [`567d5925fe`](https://github.com/sgl-project/sglang/commit/567d5925fe) [#40308](https://github.com/sgl-project/sglang/pull/40308)
  Fix mxfp4 padding test stubbing an accessor the module no longer imports (#40308)
  _Files: `test/registered/unit/layers/quantization/test_mxfp4_trtllm_padding.py`_
- **2026-09-19** [`f1fbbd17bb`](https://github.com/sgl-project/sglang/commit/f1fbbd17bb) [#40104](https://github.com/sgl-project/sglang/pull/40104)
  [diffusion] chore: update Cache-DiT to 1.5.1 for DMD Calibrator, SVDQuant DQ, etc (#40104)
  _Files: `.gitignore`, `docs/docs/sglang-diffusion/cache_dit.mdx`, `docs/docs/sglang-diffusion/environment_variables.mdx`, `python/pyproject.toml` _+7 more__
- **2026-09-18** [`45938a24ae`](https://github.com/sgl-project/sglang/commit/45938a24ae) [#40148](https://github.com/sgl-project/sglang/pull/40148)
  [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260916, use HIP Top-K (#40148)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-09-18** [`6c7c5e78de`](https://github.com/sgl-project/sglang/commit/6c7c5e78de) [#39823](https://github.com/sgl-project/sglang/pull/39823)
  [NPU] Run arch35 block-FP8 dense linears on the native MXFP8 GEMM (#39823)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/w8a8_mxfp8.py`, `python/sglang/srt/layers/quantization/fp8.py`_
- **2026-09-17** [`4f52a27563`](https://github.com/sgl-project/sglang/commit/4f52a27563) [#35123](https://github.com/sgl-project/sglang/pull/35123)
  [AMD] Fix DSV4 FP4 dequant path for AITER on ROCm (#35123)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`_
- **2026-09-17** [`923e4a56d4`](https://github.com/sgl-project/sglang/commit/923e4a56d4) [#39892](https://github.com/sgl-project/sglang/pull/39892)
  [CI] Fix sanity evaluation and diffusion test suite blockers (#39892)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `python/sglang/test/kits/hellaswag_kit.py`, `python/sglang/test/test_programs.py`, `scripts/lint/check_registered_tests.py` _+3 more__
- **2026-09-16** [`46ae84df15`](https://github.com/sgl-project/sglang/commit/46ae84df15) [#39657](https://github.com/sgl-project/sglang/pull/39657)
  dsv4.1: Hopper FP8 matmul kernels and tuning (#39657)
  _Files: `python/sglang/kernels/ops/quantization/configs/N=1152,K=5120,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[32, 32].json`, `python/sglang/kernels/ops/quantization/configs/N=1792,K=5120,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[32, 32].json`, `python/sglang/kernels/ops/quantization/configs/N=25600,K=6144,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[32, 32].json`, `python/sglang/kernels/ops/quantization/configs/N=4096,K=1280,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[32, 32].json` _+4 more__
- **2026-09-16** [`2cbfaefbf9`](https://github.com/sgl-project/sglang/commit/2cbfaefbf9) [#38453](https://github.com/sgl-project/sglang/pull/38453)
  [AMD] Avoid the FP8 wo_a path when the weight is BF16 (#38453)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`_
- **2026-09-16** [`4678536df6`](https://github.com/sgl-project/sglang/commit/4678536df6) [#32618](https://github.com/sgl-project/sglang/pull/32618)
  [CPU] Add fp8_per_tensor_scaled_mm_cpu kernel (#32618)
  _Files: `python/sglang/kernels/aot/csrc/cpu/bmm.cpp`, `python/sglang/kernels/aot/csrc/cpu/gemm.h`, `python/sglang/kernels/aot/csrc/cpu/gemm_fp8.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp` _+3 more__
- **2026-09-16** [`f11cd8ab0e`](https://github.com/sgl-project/sglang/commit/f11cd8ab0e) [#35605](https://github.com/sgl-project/sglang/pull/35605)
  [XPU] Use torch scaled_mm for XPU block FP8 linear (#35605)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/registered/e2e/xpu/test_xpu_fp8_linear.py`_
- **2026-09-14** [`242d8a70c0`](https://github.com/sgl-project/sglang/commit/242d8a70c0) [#39406](https://github.com/sgl-project/sglang/pull/39406)
  [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260913, enable TOPK_V2 (#39406)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-09-14** [`a4781c9fe5`](https://github.com/sgl-project/sglang/commit/a4781c9fe5) [#37384](https://github.com/sgl-project/sglang/pull/37384)
  [NPU] Fix error due to missing parameter quant_linear passing (#37384)
  _Files: `python/sglang/srt/layers/quantization/modelslim/modelslim.py`_
- **2026-09-14** [`2f5cc8e33e`](https://github.com/sgl-project/sglang/commit/2f5cc8e33e) [#39358](https://github.com/sgl-project/sglang/pull/39358)
  [AMD] Align Qwen3.5 MI355X cookbook with AttnFP8-V2 and HiCache direct / page_first_direct (#39358)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_

## CI / Build  (13 commits)

- **2026-09-21** [`70b5b03e78`](https://github.com/sgl-project/sglang/commit/70b5b03e78) [#40549](https://github.com/sgl-project/sglang/pull/40549)
  [NPU][CI] Fix paths-filter negation that makes every PR run the NPU tier (#40549)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-09-20** [`3dbdd700e2`](https://github.com/sgl-project/sglang/commit/3dbdd700e2) [#40474](https://github.com/sgl-project/sglang/pull/40474)
  [CI] update CI permissions (#40474)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-09-19** [`9e2298e913`](https://github.com/sgl-project/sglang/commit/9e2298e913) [#40349](https://github.com/sgl-project/sglang/pull/40349)
  [CI] Propagate full-run fast-fail policy to reusable workflows (#40349)
  _Files: `.github/workflows/pr-test.yml`_
- **2026-09-18** [`bbfcda48ce`](https://github.com/sgl-project/sglang/commit/bbfcda48ce) [#40147](https://github.com/sgl-project/sglang/pull/40147)
  [CI] Add a unified-memory rerun test group (#40147)
  _Files: `scripts/ci/rerun_test_groups.json`_
- **2026-09-18** [`d337b865af`](https://github.com/sgl-project/sglang/commit/d337b865af) [#39953](https://github.com/sgl-project/sglang/pull/39953)
  Update NPU tag to post4 version and related scripts (#39953)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-09-18** [`c055dc6ff6`](https://github.com/sgl-project/sglang/commit/c055dc6ff6) [#40055](https://github.com/sgl-project/sglang/pull/40055)
  [CI] Check B200 NUMA mapping against sysfs numa_node (#40055)
  _Files: `test/registered/utils/test_numa_utils.py`_
- **2026-09-17** [`126c2f1bc1`](https://github.com/sgl-project/sglang/commit/126c2f1bc1) [#40017](https://github.com/sgl-project/sglang/pull/40017)
  [CI] Add metamergebot to CI permissions (#40017)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-09-17** [`7ccbf5fd04`](https://github.com/sgl-project/sglang/commit/7ccbf5fd04) [#39952](https://github.com/sgl-project/sglang/pull/39952)
  [NPU][CI] Increase e2e multi-node test timeout to 210 minutes (#39952)
  _Files: `python/sglang/test/ascend/e2e/run_npu_e2e_test.py`_
- **2026-09-17** [`f6f69334ba`](https://github.com/sgl-project/sglang/commit/f6f69334ba) [#39796](https://github.com/sgl-project/sglang/pull/39796)
  [XPU] Allow the nightly XPU docker build to target a branch or tag (#39796)
  _Files: `.github/workflows/release-docker-intel-xpu-nightly.yml`_
- **2026-09-16** [`5212797880`](https://github.com/sgl-project/sglang/commit/5212797880) [#39732](https://github.com/sgl-project/sglang/pull/39732)
  [NPU] fix npu docker workspace directory (#39732)
  _Files: `docker/npu.Dockerfile`_
- **2026-09-16** [`ad28b91fae`](https://github.com/sgl-project/sglang/commit/ad28b91fae) [#39697](https://github.com/sgl-project/sglang/pull/39697)
  ci: fix always-failing coverage job, add by-GPU-count view (#39697)
  _Files: `.github/workflows/ci-coverage-overview.yml`, `scripts/ci/utils/ci_coverage_report.py`_
- **2026-09-16** [`afde31a2f5`](https://github.com/sgl-project/sglang/commit/afde31a2f5) [#39006](https://github.com/sgl-project/sglang/pull/39006)
  [router] Speak cleartext h2c on both edges: serve it inbound, forward it outbound (#39006)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/main.rs` _+13 more__
- **2026-09-15** [`e89d8facab`](https://github.com/sgl-project/sglang/commit/e89d8facab) [#39457](https://github.com/sgl-project/sglang/pull/39457)
  [sgl-router] Prepare dynamo-render dependencies (#39457)
  _Files: `.github/workflows/pr-test-sgl-router.yml`, `.gitignore`, `docker/sgl-router.Dockerfile`, `experimental/sgl-router/Cargo.lock` _+4 more__

## Triton / Kernels  (13 commits)

- **2026-09-20** [`2fa6b94e34`](https://github.com/sgl-project/sglang/commit/2fa6b94e34) [#39200](https://github.com/sgl-project/sglang/pull/39200)
  [Perf] Fuse the glm5_next mHC attn->MLP boundary (#39200)
  _Files: `python/sglang/srt/layers/communicator_mhc.py`, `python/sglang/srt/models/glm5_next.py`, `test/registered/kernels/ops/layernorm/test_mhc_kernels.py`_
- **2026-09-20** [`2e2d8a2fda`](https://github.com/sgl-project/sglang/commit/2e2d8a2fda) [#40495](https://github.com/sgl-project/sglang/pull/40495)
  [CI] Drive per-commit stage jobs from a runner table instead of copied job blocks (#40495)
  _Files: `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test-jit-kernel.yml`, `.github/workflows/pr-test.yml`_
- **2026-09-20** [`d229952e25`](https://github.com/sgl-project/sglang/commit/d229952e25) [#35452](https://github.com/sgl-project/sglang/pull/35452)
  [Fix] Preserve model runner contracts in prefill CUDA graphs (#35452)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/unit/model_executor/test_prefill_cuda_graph_runner.py`_
- **2026-09-20** [`e97614d10c`](https://github.com/sgl-project/sglang/commit/e97614d10c) [#39928](https://github.com/sgl-project/sglang/pull/39928)
  [Qwen4-Exp] Build the offloaded PLE table on the meta device so --ple-offload-embedding never materialises it on the accelerator (#39928)
  _Files: `python/sglang/srt/models/qwen4_exp.py`, `test/registered/kernels/ops/embeddings/test_qwen4_ple_offload.py`_
- **2026-09-20** [`ee5fcdf0d9`](https://github.com/sgl-project/sglang/commit/ee5fcdf0d9) [#40157](https://github.com/sgl-project/sglang/pull/40157)
  Update SGLANG_KERNEL_NPU_TAG to version 2026.9.0.post5 (#40157)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-09-19** [`c3aa09b0db`](https://github.com/sgl-project/sglang/commit/c3aa09b0db) [#40208](https://github.com/sgl-project/sglang/pull/40208)
  [Kernel] Fuse hc_combine_norm for mid-size verify batches (9-96 rows) (#40208)
  _Files: `python/sglang/kernels/ops/layernorm/hc_combine_norm.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-09-19** [`8ea0ee300d`](https://github.com/sgl-project/sglang/commit/8ea0ee300d) [#39234](https://github.com/sgl-project/sglang/pull/39234)
  perf(sampling): avoid GPU syncs when applying custom logit processors (#39234)
  _Files: `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/sampling/custom_logit_processor.py`, `python/sglang/srt/sampling/sampling_batch_info.py`, `test/registered/kernels/ops/sampling/test_apply_custom_logit_processor.py` _+3 more__
- **2026-09-17** [`9d0a8d7536`](https://github.com/sgl-project/sglang/commit/9d0a8d7536) [#37939](https://github.com/sgl-project/sglang/pull/37939)
  [CPU] Upgrade torch cpu dependencies to version 2.14. (#37939)
  _Files: `python/pyproject_cpu.toml`, `python/sglang/kernels/aot/csrc/cpu/CMakeLists.txt`, `python/sglang/kernels/aot/pyproject_cpu.toml`_
- **2026-09-16** [`d78b35076a`](https://github.com/sgl-project/sglang/commit/d78b35076a) [#39855](https://github.com/sgl-project/sglang/pull/39855)
  [CI] Fix missing elfutils headers in CUDA 13.4 DeepGEMM build (#39855)
  _Files: `docker/Dockerfile.cu134`_
- **2026-09-15** [`2c0a70960c`](https://github.com/sgl-project/sglang/commit/2c0a70960c) [#39474](https://github.com/sgl-project/sglang/pull/39474)
  [qwen 3.8 next] reuse old cuda stream instead of endlessly creating streams (#39474)
  _Files: `python/sglang/srt/models/qwen4_exp.py`_
- **2026-09-15** [`a2b4e8888f`](https://github.com/sgl-project/sglang/commit/a2b4e8888f) [#39347](https://github.com/sgl-project/sglang/pull/39347)
  Allow CUDA VMM feature transport with the Rust frontend (#39347)
  _Files: `python/sglang/srt/arg_groups/serving_hook.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-09-14** [`2123aca87e`](https://github.com/sgl-project/sglang/commit/2123aca87e) [#38409](https://github.com/sgl-project/sglang/pull/38409)
  [Fix] Wait for PDL before reading DeepSeek V4 K cache locations (#38409)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh`_
- **2026-09-14** [`96a95171c7`](https://github.com/sgl-project/sglang/commit/96a95171c7) [#39346](https://github.com/sgl-project/sglang/pull/39346)
  chore: bump sglang-kernel version to 0.4.7 (#39346)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`_

## Tensor / Data Parallel  (11 commits)

- **2026-09-20** [`404dee10c0`](https://github.com/sgl-project/sglang/commit/404dee10c0) [#38339](https://github.com/sgl-project/sglang/pull/38339)
  [NPU] add coverage-based precision test selection pipeline (#38339)
  _Files: `.github/workflows/_npu-analyze-failure.yml`, `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/coverage-collection-npu.yml` _+6 more__
- **2026-09-20** [`7b1c2ed0a4`](https://github.com/sgl-project/sglang/commit/7b1c2ed0a4) [#36718](https://github.com/sgl-project/sglang/pull/36718)
  [rust-renderer] Standalone preprocessing (#36718)
  _Files: `docker/renderer.Dockerfile`, `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/sglang-renderer/Cargo.toml` _+47 more__
- **2026-09-18** [`803f0c93d2`](https://github.com/sgl-project/sglang/commit/803f0c93d2) [#39871](https://github.com/sgl-project/sglang/pull/39871)
  Fix DSA partial DP-TP mode log to use derived attn_tp_size (#39871)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`_
- **2026-09-17** [`a98d921658`](https://github.com/sgl-project/sglang/commit/a98d921658) [#39899](https://github.com/sgl-project/sglang/pull/39899)
  [DP Attn] Fix crash for no token all-gather case (#39899)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `test/registered/unit/model_executor/test_mlp_sync_pad_unpad.py`_
- **2026-09-17** [`11c35b8433`](https://github.com/sgl-project/sglang/commit/11c35b8433) [#38878](https://github.com/sgl-project/sglang/pull/38878)
  [AMD] Load fused shared experts for Qwen4-Exp and Qwen3.5 MTP (#38878)
  _Files: `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen4_exp.py`_
- **2026-09-16** [`d634320e48`](https://github.com/sgl-project/sglang/commit/d634320e48) [#39014](https://github.com/sgl-project/sglang/pull/39014)
  [Router] Count open HTTP exchanges until their response body finishes (#39014)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/src/server/app.rs`, `experimental/sgl-router/src/server/app_context.rs` _+4 more__
- **2026-09-16** [`100e1cd0d9`](https://github.com/sgl-project/sglang/commit/100e1cd0d9) [#34712](https://github.com/sgl-project/sglang/pull/34712)
  [Fix] Spawn, don't fork, the benchmark server process (#34712)
  _Files: `python/sglang/benchmark/endpoint.py`, `test/registered/unit/bench/test_benchmark_endpoint.py`_
- **2026-09-15** [`24874f90a3`](https://github.com/sgl-project/sglang/commit/24874f90a3) [#39636](https://github.com/sgl-project/sglang/pull/39636)
  [Test] Fix DeepGEMM batch invariance test output dtype (#39636)
  _Files: `test/registered/unit/batch_invariant_ops/test_batch_invariant_ops.py`_
- **2026-09-15** [`c0b8725f5a`](https://github.com/sgl-project/sglang/commit/c0b8725f5a) [#39237](https://github.com/sgl-project/sglang/pull/39237)
  Fix /model_info serialization when a config value is a class (#39237)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/utils/msgspec_utils.py`, `test/registered/unit/entrypoints/test_server_info.py`_
- **2026-09-15** [`276663a79d`](https://github.com/sgl-project/sglang/commit/276663a79d) [#34981](https://github.com/sgl-project/sglang/pull/34981)
  [model-loader] Split weight loading from postprocessing (#34981)
  _Files: `python/sglang/srt/model_loader/loader.py`, `test/registered/unit/model_loader/test_default_model_loader.py`_
- **2026-09-14** [`6388b6cfb1`](https://github.com/sgl-project/sglang/commit/6388b6cfb1) [#36472](https://github.com/sgl-project/sglang/pull/36472)
  [feat] Add base NpuSRTPlatform implementation (#36472)
  _Files: `python/sglang/srt/platforms/__init__.py`, `python/sglang/srt/platforms/npu.py`, `test/registered/unit/platforms/test_platform_interface.py`_

## Docs / Examples  (10 commits)

- **2026-09-21** [`b410010087`](https://github.com/sgl-project/sglang/commit/b410010087) [#40575](https://github.com/sgl-project/sglang/pull/40575)
  [NPU] [DOC] Add kimi k3 cookbook for 950PR/DT Series (#40575)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/_kimi_k3_mamba_ratio_calculator.jsx`, `docs/src/snippets/_playground.jsx` _+1 more__
- **2026-09-20** [`5c69e32abe`](https://github.com/sgl-project/sglang/commit/5c69e32abe) [#40402](https://github.com/sgl-project/sglang/pull/40402)
  [NPU] [DOC] fix typos, heading levels and terminology in NPU docs (#40402)
  _Files: `docs/docs/hardware-platforms/ascend-npus/development/operator_development.mdx`, `docs/docs/hardware-platforms/ascend-npus/evaluation/accuracy_evaluation.mdx`, `docs/docs/hardware-platforms/ascend-npus/faq.mdx`, `docs/docs/hardware-platforms/ascend-npus/mindspore_backend.mdx` _+2 more__
- **2026-09-20** [`c1a1eb5f66`](https://github.com/sgl-project/sglang/commit/c1a1eb5f66) [#40276](https://github.com/sgl-project/sglang/pull/40276)
  docs: sync LMSYS SGLang blog cards (#40276)
  _Files: `docs/index.mdx`_
- **2026-09-18** [`aed3fb1cdd`](https://github.com/sgl-project/sglang/commit/aed3fb1cdd) [#39465](https://github.com/sgl-project/sglang/pull/39465)
  [Router] Log every request at one site; derive its outcome from the final status (3/3) (#39465)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/monitoring/grafana-dashboard.json` _+6 more__
- **2026-09-18** [`50a7de47d5`](https://github.com/sgl-project/sglang/commit/50a7de47d5) [#40034](https://github.com/sgl-project/sglang/pull/40034)
  [Benchmark] Add agentic rollout simulator and offline explorer (#40034)
  _Files: `benchmark/agentic-rollout/README.md`, `benchmark/agentic-rollout/explore.py`, `benchmark/agentic-rollout/metrics.py`, `benchmark/agentic-rollout/plot.py` _+9 more__
- **2026-09-18** [`6952538980`](https://github.com/sgl-project/sglang/commit/6952538980) [#40058](https://github.com/sgl-project/sglang/pull/40058)
  [NPU] [DOC] delete unsupported api --disable-hybrid-swa-memory for npu (#40058)
  _Files: `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`_
- **2026-09-16** [`b02e16a895`](https://github.com/sgl-project/sglang/commit/b02e16a895) [#39002](https://github.com/sgl-project/sglang/pull/39002)
  [Router] Fleet-wide sampling contract 3/3: splice injection without re-serializing (#39002)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/tests/proxy/main.rs`, `experimental/sgl-router/tests/proxy/sampling_overrides.rs`_
- **2026-09-15** [`3c48c1e967`](https://github.com/sgl-project/sglang/commit/3c48c1e967) [#39109](https://github.com/sgl-project/sglang/pull/39109)
  [Router] Expose the KV storage-tier stream and tree occupancy on /metrics (2/4) (#39109)
  _Files: `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/src/main.rs`, `experimental/sgl-router/src/policies/kv_events/index.rs`, `experimental/sgl-router/src/policies/kv_events/mod.rs` _+5 more__
- **2026-09-15** [`575163ff32`](https://github.com/sgl-project/sglang/commit/575163ff32) [#39555](https://github.com/sgl-project/sglang/pull/39555)
  [NPU] [DOC] delete unsupported models in npu docs (#39555)
  _Files: `docs/docs/hardware-platforms/ascend-npus/reference/support_models.mdx`_
- **2026-09-14** [`f539c1fc65`](https://github.com/sgl-project/sglang/commit/f539c1fc65) [#38737](https://github.com/sgl-project/sglang/pull/38737)
  [sgl-router] Stream outcome observability for 2xx SSE streams (#38737)
  _Files: `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/src/proxy/mod.rs`, `experimental/sgl-router/src/proxy/sse.rs`, `experimental/sgl-router/src/server/metrics.rs` _+2 more__

## Models  (10 commits)

- **2026-09-21** [`0abb251a20`](https://github.com/sgl-project/sglang/commit/0abb251a20) [#40530](https://github.com/sgl-project/sglang/pull/40530)
  [sgl-router] Match DeepSeek V4 rendering to SGLang (#40530)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/tokenizer/chat_formatter.rs`, `experimental/sgl-router/src/tokenizer/deepseek.rs`, `experimental/sgl-router/src/tokenizer/mod.rs` _+4 more__
- **2026-09-20** [`c2c3629f2d`](https://github.com/sgl-project/sglang/commit/c2c3629f2d) [#38805](https://github.com/sgl-project/sglang/pull/38805)
  [Kimi-K3] O(1) expert weight lookup in load_weights (#38805)
  _Files: `python/sglang/srt/models/kimi_k3.py`_
- **2026-09-18** [`21e6c98ccb`](https://github.com/sgl-project/sglang/commit/21e6c98ccb) [#39773](https://github.com/sgl-project/sglang/pull/39773)
  Fix corrupted chat prompts on mistral_common tokenizers (tool_choice auto never fires) (#39773)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_chat_prompt_round_trip.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-09-18** [`3ce3b4969f`](https://github.com/sgl-project/sglang/commit/3ce3b4969f) [#39919](https://github.com/sgl-project/sglang/pull/39919)
  [NPU] Avoid repeated BF16 wo_a weight transposes in DeepSeek-V4 decode (#39919)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/manual/dsv4/bench_npu_wo_a.py`_
- **2026-09-16** [`43390f63f5`](https://github.com/sgl-project/sglang/commit/43390f63f5) [#39662](https://github.com/sgl-project/sglang/pull/39662)
  [qwen 3.8 next] change the testing model in test_qwen4_exp_models.py (#39662)
  _Files: `test/registered/e2e/models/test_qwen4_exp_models.py`_
- **2026-09-16** [`00a9a81b67`](https://github.com/sgl-project/sglang/commit/00a9a81b67) [#39813](https://github.com/sgl-project/sglang/pull/39813)
  [NPU][CI] Fail fast and speed up long-running qwen3.6 accuracy cases (#39813)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`, `test/registered/npu/accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_1p_gpqa.py`, `test/registered/npu/accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in3k5_out1k5_50ms_gpqa.py`_
- **2026-09-16** [`9c8d4641ff`](https://github.com/sgl-project/sglang/commit/9c8d4641ff) [#39720](https://github.com/sgl-project/sglang/pull/39720)
  [Fix] Fix GLM5 mHC PP forward (#39720)
  _Files: `python/sglang/srt/models/glm5_next.py`_
- **2026-09-15** [`08b1922405`](https://github.com/sgl-project/sglang/commit/08b1922405) [#35809](https://github.com/sgl-project/sglang/pull/35809)
  fix(gemma4): set lm_head_is_tied for Gemma4UnifiedForConditionalGeneration (#35809)
  _Files: `python/sglang/srt/models/gemma4_unified.py`_
- **2026-09-15** [`5298d85218`](https://github.com/sgl-project/sglang/commit/5298d85218) [#39366](https://github.com/sgl-project/sglang/pull/39366)
  fix: stop shadowing the DSpark shared-experts fusion guard (#39366)
  _Files: `python/sglang/srt/models/deepseek_v4_dspark.py`_
- **2026-09-14** [`d5f1c593c1`](https://github.com/sgl-project/sglang/commit/d5f1c593c1) [#39047](https://github.com/sgl-project/sglang/pull/39047)
  [NPU] Remove temperature/top_p from Qwen3.5-397B-A17B perf test (#39047)
  _Files: `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py`_

## Speculative Decoding  (7 commits)

- **2026-09-18** [`da2f434951`](https://github.com/sgl-project/sglang/commit/da2f434951) [#39502](https://github.com/sgl-project/sglang/pull/39502)
  [Spec] Add explicit prefill shared-read capability for plugins (#39502)
  _Files: `python/sglang/srt/model_executor/runner_utils/shared_read_event.py`, `python/sglang/srt/speculative/spec_info.py`, `python/sglang/srt/speculative/spec_registry.py`, `test/registered/unit/model_executor/runner/test_prefill_shared_read_done.py`_
- **2026-09-18** [`740f57a02c`](https://github.com/sgl-project/sglang/commit/740f57a02c) [#35798](https://github.com/sgl-project/sglang/pull/35798)
  [Spec] Fix CDF boundary handling in `TreeSpeculativeSamplingTargetOnly` (#35798)
  _Files: `python/sglang/kernels/jit/include/sgl_kernel/speculative/sampling.cuh`, `test/registered/kernels/ops/speculative/test_speculative_sampling.py`_
- **2026-09-17** [`25ce8063f7`](https://github.com/sgl-project/sglang/commit/25ce8063f7) [#30775](https://github.com/sgl-project/sglang/pull/30775)
  Pipeline parallelism x speculative decoding (EAGLE/MTP) compatibility (#30775)
  _Files: `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` _+14 more__
- **2026-09-16** [`7d5696b3a1`](https://github.com/sgl-project/sglang/commit/7d5696b3a1) [#39653](https://github.com/sgl-project/sglang/pull/39653)
  dsv4.1: communication kernels and wrappers (#39653)
  _Files: `python/sglang/kernels/jit/csrc/distributed/all_reduce_fusion.cuh`, `python/sglang/kernels/jit/csrc/distributed/custom_all_reduce.cuh`, `python/sglang/kernels/jit/csrc/distributed/nvlink_comm.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/distributed/ptx.cuh` _+5 more__
- **2026-09-16** [`7eedd57ab0`](https://github.com/sgl-project/sglang/commit/7eedd57ab0) [#37134](https://github.com/sgl-project/sglang/pull/37134)
  [ROCm] Fix EAGLE spec-decode verify silently sampling greedy on HIP (#37134)
  _Files: `python/sglang/kernels/ops/speculative/reject_sampling.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_utils.py` _+3 more__
- **2026-09-15** [`df254b0a11`](https://github.com/sgl-project/sglang/commit/df254b0a11) [#38630](https://github.com/sgl-project/sglang/pull/38630)
  [profiler] Label draft-runner steps DRAFT and target verify VERIFY in step spans (#38630)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/utils/profile_utils.py`, `test/registered/unit/managers/test_detailed_annotations.py`_
- **2026-09-14** [`9128d57966`](https://github.com/sgl-project/sglang/commit/9128d57966) [#38554](https://github.com/sgl-project/sglang/pull/38554)
  [Spec] Allow speculative workers to stage prefill shared reads (#38554)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner_utils/shared_read_event.py`, `test/registered/unit/model_executor/runner/test_prefill_shared_read_done.py`_

## ROCm / AMD  (6 commits)

- **2026-09-21** [`b86a30afba`](https://github.com/sgl-project/sglang/commit/b86a30afba) [#40113](https://github.com/sgl-project/sglang/pull/40113)
  [AMD][DI][CI] Add a SPUR cluster profile to AMD DI CI  (#40113)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`, `scripts/ci/slurm/launch_mi355x.sh`_
- **2026-09-18** [`cd4dd81c22`](https://github.com/sgl-project/sglang/commit/cd4dd81c22) [#40186](https://github.com/sgl-project/sglang/pull/40186)
  [AMD][DSV4] fix: drop shadowing local get_exec import that breaks model startup on ROCm (#40186)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`_
- **2026-09-16** [`f60652a43e`](https://github.com/sgl-project/sglang/commit/f60652a43e) [#39702](https://github.com/sgl-project/sglang/pull/39702)
  [AMD] Update deepseek-v4 PDI and cache policy setting for agentic workload (#39702)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-16** [`6331e43081`](https://github.com/sgl-project/sglang/commit/6331e43081) [#39631](https://github.com/sgl-project/sglang/pull/39631)
  [AMD] Prefer HIP Top-K for GLM-5.x on ROCm (#39631)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`_
- **2026-09-16** [`a9bb4d7d45`](https://github.com/sgl-project/sglang/commit/a9bb4d7d45) [#39572](https://github.com/sgl-project/sglang/pull/39572)
  [AMD] Align Qwen3.5 MI355X HiCache cookbook with kernel / page_first (#39572)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-09-15** [`03ea13a545`](https://github.com/sgl-project/sglang/commit/03ea13a545) [#38632](https://github.com/sgl-project/sglang/pull/38632)
  [AMD][CI] Consolidate AMD workflows and retire ROCm 7.0 CI (#38632)
  _Files: `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/bot-bump-sglang-version.yml` _+13 more__

## Structured Output  (6 commits)

- **2026-09-21** [`8d08dfdab7`](https://github.com/sgl-project/sglang/commit/8d08dfdab7) [#40554](https://github.com/sgl-project/sglang/pull/40554)
  [Fix] Add gigachat35 to the tool-call and reasoning parser name lists (#40554)
  _Files: `python/sglang/srt/function_call/parser_names.py`, `python/sglang/srt/parser/reasoning_parser_names.py`_
- **2026-09-21** [`ab03a8e7eb`](https://github.com/sgl-project/sglang/commit/ab03a8e7eb) [#40201](https://github.com/sgl-project/sglang/pull/40201)
  [Perf] Fork-safe import: no CUDA context at import time, lighter argument parsing (#40201)
  _Files: `python/sglang/cli/utils.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/function_call/parser_names.py`, `python/sglang/srt/parser/reasoning_parser_names.py` _+7 more__
- **2026-09-20** [`80da4432d0`](https://github.com/sgl-project/sglang/commit/80da4432d0) [#40440](https://github.com/sgl-project/sglang/pull/40440)
  [Simulator] Fix meta host memory budgets on constrained runners (#40440)
  _Files: `.github/workflows/_pr-test-simulator-cpu.yml`, `tools/sglang-simulator/src/sglang_simulator/simulation/sglang/mem_pool_host.py`_
- **2026-09-17** [`464fffbec8`](https://github.com/sgl-project/sglang/commit/464fffbec8) [#39665](https://github.com/sgl-project/sglang/pull/39665)
  dsv4.1: chat encoding and tool parsing (#39665)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/entrypoints/openai/chat_encoding.py`, `python/sglang/srt/entrypoints/openai/encoding_dsv41.py`, `python/sglang/srt/entrypoints/openai/protocol.py` _+9 more__
- **2026-09-16** [`dc067c7d8c`](https://github.com/sgl-project/sglang/commit/dc067c7d8c) [#39869](https://github.com/sgl-project/sglang/pull/39869)
  [Fix] Allow closed object schemas in Outlines prevalidation (#39869)
  _Files: `python/sglang/srt/constrained/json_schema_validation.py`, `test/registered/unit/constrained/test_json_schema_validation.py`_
- **2026-09-16** [`869674b3a7`](https://github.com/sgl-project/sglang/commit/869674b3a7) [#37839](https://github.com/sgl-project/sglang/pull/37839)
  [Fix] Prevalidate JSON Schema support per grammar backend (#37839)
  _Files: `python/sglang/srt/constrained/json_schema_validation.py`, `python/sglang/srt/constrained/outlines_backend.py`, `python/sglang/srt/constrained/xgrammar_backend.py`, `test/registered/unit/constrained/test_json_schema_validation.py`_

## Serving / API  (5 commits)

- **2026-09-21** [`11ecdbf39f`](https://github.com/sgl-project/sglang/commit/11ecdbf39f) [#40526](https://github.com/sgl-project/sglang/pull/40526)
  Clean up startup logging and streamline log audits (#40526)
  _Files: `.claude/skills/clean-startup-log/SKILL.md`, `.claude/skills/clean-startup-log/references/noise-sources.md`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/utils/common.py`_
- **2026-09-19** [`111b905bd1`](https://github.com/sgl-project/sglang/commit/111b905bd1) [#38604](https://github.com/sgl-project/sglang/pull/38604)
  fix(openai): recover logprobs token bytes from token_id (UTF-8 fragments) (#38604)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_completions.py`, `python/sglang/srt/entrypoints/openai/utils.py`_
- **2026-09-18** [`0be8a0af0e`](https://github.com/sgl-project/sglang/commit/0be8a0af0e) [#39364](https://github.com/sgl-project/sglang/pull/39364)
  [DSV4] fix: keep the TileLang JIT cache under SGLANG_CACHE_DIR (#39364)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/environ.py`_
- **2026-09-18** [`db39b7f961`](https://github.com/sgl-project/sglang/commit/db39b7f961) [#34776](https://github.com/sgl-project/sglang/pull/34776)
  [Fix] Guard conditional top-logprob keys in the completions echo path (#34776)
  _Files: `python/sglang/srt/entrypoints/openai/serving_completions.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_completions.py`_
- **2026-09-15** [`07e1918924`](https://github.com/sgl-project/sglang/commit/07e1918924) [#38939](https://github.com/sgl-project/sglang/pull/38939)
  [Rust] Use Dynamo native renderers when chat templates are missing (#38939)
  _Files: `python/sglang/srt/rust_server/config.py`, `rust/Cargo.lock`, `rust/sglang-server/Cargo.toml`, `rust/sglang-server/src/api_server/openai.rs` _+5 more__

## LoRA  (3 commits)

- **2026-09-21** [`2016f5e7a1`](https://github.com/sgl-project/sglang/commit/2016f5e7a1) [#40390](https://github.com/sgl-project/sglang/pull/40390)
  [sgl-router] Add Kimi-K3 rendering with SGLang parity (#40390)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/tokenizer/adapter.rs` _+12 more__
- **2026-09-17** [`3ce7e2a29f`](https://github.com/sgl-project/sglang/commit/3ce7e2a29f) [#38983](https://github.com/sgl-project/sglang/pull/38983)
  [sgl-router] Render chat prompts with dynamo-render (#38983)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs` _+29 more__
- **2026-09-16** [`279339f113`](https://github.com/sgl-project/sglang/commit/279339f113) [#39485](https://github.com/sgl-project/sglang/pull/39485)
  [sgl-router] Share model-file discovery for chat formatters (#39485)
  _Files: `experimental/sgl-router/src/tokenizer/adapter.rs`_

---
_Generated 2026-09-21 15:04 UTC_