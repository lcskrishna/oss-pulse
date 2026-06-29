# vllm-project/vllm — Weekly Change Report
**Period:** 2026-06-22 → 2026-06-29  |  **Total commits:** 323

## ✨ New Features This Week

- **2026-06-29** [#47008](https://github.com/vllm-project/vllm/pull/47008) — [XPU] exclude unsupported models for test_tensor_sechma.py (#47008)
- **2026-06-29** [#47018](https://github.com/vllm-project/vllm/pull/47018) — [mypy] Enable mypy for tests directory (#47018)
- **2026-06-29** [#47011](https://github.com/vllm-project/vllm/pull/47011) — [CI Failure] Add transformers version check for openai/privacy-filter (#47011)
- **2026-06-29** [#46800](https://github.com/vllm-project/vllm/pull/46800) — [Rust Frontend] Add Harmony Renderer for GPT-OSS (#46800)
- **2026-06-29** [#42920](https://github.com/vllm-project/vllm/pull/42920) — [CPU] Support cpu compressed-tensor w8a8 int8 moe (#42920)
- **2026-06-28** [#41026](https://github.com/vllm-project/vllm/pull/41026) — [Model] Add support for openai/privacy-filter (#41026)
- **2026-06-28** [#46629](https://github.com/vllm-project/vllm/pull/46629) — [OCP MX ] Add back emulation to available OCP MX backends list (#46629)
- **2026-06-28** [#46876](https://github.com/vllm-project/vllm/pull/46876) — [GLM5] Implement op fusion for GLM5/DSV3.2 (#46876)
- **2026-06-28** [#45033](https://github.com/vllm-project/vllm/pull/45033) — [ROCm][Perf][MLA] Add AITER FlashAttention MLA prefill backend (`ROCM_AITER_FA`) (#45033)
- **2026-06-28** [#46846](https://github.com/vllm-project/vllm/pull/46846) — [Render][Speculator] Add return_loss_mask to render endpoint for training data generation (#46846)
- _…and 66 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-06-29** [`3483240b7e`](https://github.com/vllm-project/vllm/commit/3483240b7e) [#44512](https://github.com/vllm-project/vllm/pull/44512) — [Frontend] Consolidate scale out entrypoints (#44512)
- **2026-06-29** [`db28ae2d07`](https://github.com/vllm-project/vllm/commit/db28ae2d07) [#46999](https://github.com/vllm-project/vllm/pull/46999) — [ROCm][CI] Explicitly tear down multimodal offline LLMs (#46999)
- **2026-06-28** [`c2127a25c7`](https://github.com/vllm-project/vllm/commit/c2127a25c7) [#46895](https://github.com/vllm-project/vllm/pull/46895) — [ROCm][CI] Fix `rlhf_async_new_apis` Example On ROCm (#46895)
- **2026-06-28** [`5ecae3266c`](https://github.com/vllm-project/vllm/commit/5ecae3266c) [#45033](https://github.com/vllm-project/vllm/pull/45033) — [ROCm][Perf][MLA] Add AITER FlashAttention MLA prefill backend (`ROCM_AITER_FA`) (#45033)
- **2026-06-28** [`a2a92cbbaa`](https://github.com/vllm-project/vllm/commit/a2a92cbbaa) [#46930](https://github.com/vllm-project/vllm/pull/46930) — [Hardware][AMD][CI] Tweak mirrored tests; improve CI base dependency change detection (#46930)
- **2026-06-28** [`c7ca0bccae`](https://github.com/vllm-project/vllm/commit/c7ca0bccae) [#44313](https://github.com/vllm-project/vllm/pull/44313) — [ROCm][Perf] Add Fused Shared Expert (FSE) support for GLM-4.5/6/7 (#44313)
- **2026-06-28** [`a65f93fb2e`](https://github.com/vllm-project/vllm/commit/a65f93fb2e) [#46886](https://github.com/vllm-project/vllm/pull/46886) — [ROCm][CI] Add ci_base metadata for external cache orchestration (#46886)
- **2026-06-27** [`9036c89ee4`](https://github.com/vllm-project/vllm/commit/9036c89ee4) [#46928](https://github.com/vllm-project/vllm/pull/46928) — [Hardware][AMD][CI] Patch Whisper multi LoRA test to use TRITON_ATTN for now (#46928)
- **2026-06-27** [`51a99565c3`](https://github.com/vllm-project/vllm/commit/51a99565c3) [#46474](https://github.com/vllm-project/vllm/pull/46474) — [ROCm][Perf] Fused shared expert for Minimax M3 (#46474)
- **2026-06-27** [`867fd5e8ed`](https://github.com/vllm-project/vllm/commit/867fd5e8ed) [#46184](https://github.com/vllm-project/vllm/pull/46184) — [ROCm][Perf] Use flydsl moe with Minimax-M3 mxfp8 weights on gfx950 and implemented moe-backend selection (#46184)
- **2026-06-27** [`9fd00ee006`](https://github.com/vllm-project/vllm/commit/9fd00ee006) [#46905](https://github.com/vllm-project/vllm/pull/46905) — [ROCm][CI] Move remaining mi250_2 tests out of the MI250 queue (#46905)
- **2026-06-27** [`091d13976c`](https://github.com/vllm-project/vllm/commit/091d13976c) [#46891](https://github.com/vllm-project/vllm/pull/46891) — [ROCm][CI] Add TRITON_ATTN score absolute tolerance floor (#46891)
- **2026-06-27** [`68ee8300a0`](https://github.com/vllm-project/vllm/commit/68ee8300a0) [#46409](https://github.com/vllm-project/vllm/pull/46409) — [ROCm][CI]Fix test_concat_and_cache_mla_rope_fused on ROCm (#46409)
- **2026-06-27** [`00e045b7c7`](https://github.com/vllm-project/vllm/commit/00e045b7c7) [#46758](https://github.com/vllm-project/vllm/pull/46758) — [ROCm][CI TG] refactor and fix deepep_moe test group (#46758)
- **2026-06-27** [`17a71d8702`](https://github.com/vllm-project/vllm/commit/17a71d8702) [#46658](https://github.com/vllm-project/vllm/pull/46658) — [ROCm][CI] Relax fused layernorm quant test tolerances for one-ULP outliers (#46658)
- **2026-06-27** [`1a92dfcce4`](https://github.com/vllm-project/vllm/commit/1a92dfcce4) [#35232](https://github.com/vllm-project/vllm/pull/35232) — [Build] Show error message when using ROCm with LTO and different compilers (#35232)
- **2026-06-26** [`2ff76a5e85`](https://github.com/vllm-project/vllm/commit/2ff76a5e85) [#46760](https://github.com/vllm-project/vllm/pull/46760) — [ROCm][Bugfix] Pass num_kv_splits to aiter mla_reduce_v1 (#46760)
- **2026-06-26** [`6e2fb02fe5`](https://github.com/vllm-project/vllm/commit/6e2fb02fe5) [#46851](https://github.com/vllm-project/vllm/pull/46851) — [ROCm][CI] Fix rlhf_nccl.py on ROCm (#46851)
- **2026-06-26** [`274325dd43`](https://github.com/vllm-project/vllm/commit/274325dd43) [#46867](https://github.com/vllm-project/vllm/pull/46867) — [ROCm][CI] Remove V1 Sample + Logits from mi250 Queue (#46867)
- **2026-06-26** [`95e6442a6b`](https://github.com/vllm-project/vllm/commit/95e6442a6b) [#46859](https://github.com/vllm-project/vllm/pull/46859) — [Hardware][AMD][CI] Fix Kernels Quantization test timeout (#46859)
- **2026-06-26** [`3d3b96488f`](https://github.com/vllm-project/vllm/commit/3d3b96488f) [#46705](https://github.com/vllm-project/vllm/pull/46705) — Migrate Voxtral to mistral-common 1.11.5 audio API (#46705)
- **2026-06-26** [`c2507fb293`](https://github.com/vllm-project/vllm/commit/c2507fb293) [#46545](https://github.com/vllm-project/vllm/pull/46545) — [ROCm] [MoE] [Perf] Shared-expert fusion for bias-routed MoE; enable on MiniMax-M3 mxfp8 model (#46545)
- **2026-06-26** [`8921c4be88`](https://github.com/vllm-project/vllm/commit/8921c4be88) [#46122](https://github.com/vllm-project/vllm/pull/46122) — [ROCm] [Performance] Optimize aiter moe for DeepSeekV4 (#46122)
- **2026-06-26** [`8e394244a5`](https://github.com/vllm-project/vllm/commit/8e394244a5) [#46419](https://github.com/vllm-project/vllm/pull/46419) — [ROCm]Enable AITER MoE backend for MiniMax-M3-MXFP4 (#46419)
- **2026-06-26** [`302954e5f6`](https://github.com/vllm-project/vllm/commit/302954e5f6) [#46823](https://github.com/vllm-project/vllm/pull/46823) — [ROCm] [CI] fix transcription flakiness AMD: Entrypoints Integration (API Server OpenAI - Part 1) (mi325_1) (#46823)
- **2026-06-26** [`d980a3cc6e`](https://github.com/vllm-project/vllm/commit/d980a3cc6e) [#46780](https://github.com/vllm-project/vllm/pull/46780) — [ROCm] Fix AITER_UNIFIED_ATTN Dispatching After AITER Bump (#46780)
- **2026-06-26** [`35a49fcfc2`](https://github.com/vllm-project/vllm/commit/35a49fcfc2) [#46749](https://github.com/vllm-project/vllm/pull/46749) — [CI][Bugfix] Spawn engine in mm cache sleep test to fix ROCm HIP error (#46749)
- **2026-06-26** [`915e99ec67`](https://github.com/vllm-project/vllm/commit/915e99ec67) [#46741](https://github.com/vllm-project/vllm/pull/46741) — [ROCm][Bugfix] Fix HIP fork re-init in multimodal offline examples (#46741)
- **2026-06-26** [`1a4984520e`](https://github.com/vllm-project/vllm/commit/1a4984520e) [#46792](https://github.com/vllm-project/vllm/pull/46792) — [Hardware][AMD][CI] Fix AMD CI image build (#46792)
- **2026-06-25** [`27da2a2ac4`](https://github.com/vllm-project/vllm/commit/27da2a2ac4) [#46691](https://github.com/vllm-project/vllm/pull/46691) — [Hardware][AMD][CI] Use Triton-based AITER MHA for LM Eval Qwen-3.5 Models Tests (#46691)
- **2026-06-25** [`2a6f8f0c05`](https://github.com/vllm-project/vllm/commit/2a6f8f0c05) [#39238](https://github.com/vllm-project/vllm/pull/39238) — [ROCm][CI] Fine-tuning queues and test names (#39238)
- **2026-06-25** [`e53a17232c`](https://github.com/vllm-project/vllm/commit/e53a17232c) [#46692](https://github.com/vllm-project/vllm/pull/46692) — [ROCm]: Bump aiter to 0.1.16.post2 (#46692)
- **2026-06-25** [`96eb8ddc41`](https://github.com/vllm-project/vllm/commit/96eb8ddc41) [#46671](https://github.com/vllm-project/vllm/pull/46671) — [CI] Re-enable skipped glm and seedoss parser tests (#46671)
- **2026-06-25** [`1744adc256`](https://github.com/vllm-project/vllm/commit/1744adc256) [#45666](https://github.com/vllm-project/vllm/pull/45666) — [ROCM] [Communication] Add INT3 quantization method for quickreduce (#45666)
- **2026-06-25** [`cdfa2fd7e9`](https://github.com/vllm-project/vllm/commit/cdfa2fd7e9) [#46729](https://github.com/vllm-project/vllm/pull/46729) — [ROCm][CI] rm duplicate Distributed Torchrun ci test (#46729)
- **2026-06-25** [`2365b7a8e7`](https://github.com/vllm-project/vllm/commit/2365b7a8e7) [#46668](https://github.com/vllm-project/vllm/pull/46668) — [Hardware][AMD][CI] Mirror Basic Models (Others) and Weight Loading Multiple GPU test groups (#46668)
- **2026-06-25** [`c63cd4906c`](https://github.com/vllm-project/vllm/commit/c63cd4906c) [#46546](https://github.com/vllm-project/vllm/pull/46546) — [ROCm][ [Perf] sparse attention optimization on minimax-m3  (#46546)
- **2026-06-25** [`77c1d9fe9b`](https://github.com/vllm-project/vllm/commit/77c1d9fe9b) [#40784](https://github.com/vllm-project/vllm/pull/40784) — [ROCm][Perf] Tune wvSplitK on gfx1151 (#40784)
- **2026-06-25** [`e2af449c39`](https://github.com/vllm-project/vllm/commit/e2af449c39) [#46686](https://github.com/vllm-project/vllm/pull/46686) — [Hardware][AMD][CI] Move Metrics, Tracing (2 GPUs) & make optional (#46686)
- **2026-06-25** [`3f5a1e1733`](https://github.com/vllm-project/vllm/commit/3f5a1e1733) [#46573](https://github.com/vllm-project/vllm/pull/46573) — [ROCm][CI] Expand basic correctness target suites (#46573)
- **2026-06-25** [`710ebaa189`](https://github.com/vllm-project/vllm/commit/710ebaa189) [#46114](https://github.com/vllm-project/vllm/pull/46114) — [ROCm][Bugfix] Fix chunk alignment when using context parallelism with TRITON_MLA (#46114)
- **2026-06-25** [`dc55936f64`](https://github.com/vllm-project/vllm/commit/dc55936f64) [#46650](https://github.com/vllm-project/vllm/pull/46650) — [AMD][CI] Fix Pipeline + Context Parallelism test group (#46650)
- **2026-06-25** [`6e3a983cf3`](https://github.com/vllm-project/vllm/commit/6e3a983cf3) [#46655](https://github.com/vllm-project/vllm/pull/46655) — [ROCm] Remove erroneous inclusion of gptq_marlin as supported quant scheme on ROCm (#46655)
- **2026-06-24** [`d6696e2385`](https://github.com/vllm-project/vllm/commit/d6696e2385) [#46636](https://github.com/vllm-project/vllm/pull/46636) — [ROCm] Begin Deprecation Window for CUDA_VISIBLE_DEVICES on ROCm (#46636)
- **2026-06-24** [`cf57311187`](https://github.com/vllm-project/vllm/commit/cf57311187) [#46386](https://github.com/vllm-project/vllm/pull/46386) — Run DeepSeek-V2-Lite prefetch-offload eval eager on ROCm (#46386)
- **2026-06-24** [`b3a688cb9e`](https://github.com/vllm-project/vllm/commit/b3a688cb9e) [#46548](https://github.com/vllm-project/vllm/pull/46548) — [ROCm] Fix OOB During Model Warmup With `ROCM_ATTN` and MRV2 (#46548)
- **2026-06-24** [`61ee183d28`](https://github.com/vllm-project/vllm/commit/61ee183d28) [#46414](https://github.com/vllm-project/vllm/pull/46414) — [ROCm] Fix AITER FP8 quantization schema tests (#46414)
- **2026-06-24** [`d7c1821b5a`](https://github.com/vllm-project/vllm/commit/d7c1821b5a) [#45810](https://github.com/vllm-project/vllm/pull/45810) — [Model][MiniMax-M3] Add pipeline parallelism support (#45810)
- **2026-06-24** [`549c7074cd`](https://github.com/vllm-project/vllm/commit/549c7074cd) [#46580](https://github.com/vllm-project/vllm/pull/46580) — [ROCm][CI] Skip the MoE Marlin tile-padding helper assertion (#46580)
- **2026-06-24** [`e2bdc24612`](https://github.com/vllm-project/vllm/commit/e2bdc24612) [#45998](https://github.com/vllm-project/vllm/pull/45998) — [ROCm][Bugfix] Fix `use_v2_model_runner` inside Ray driver thread (#45998)
- **2026-06-24** [`bcbeaac786`](https://github.com/vllm-project/vllm/commit/bcbeaac786) [#46537](https://github.com/vllm-project/vllm/pull/46537) — [ROCm][CI] Stage C-II of gating additional test groups (#46537)
- **2026-06-23** [`80e511772f`](https://github.com/vllm-project/vllm/commit/80e511772f) [#44434](https://github.com/vllm-project/vllm/pull/44434) — [ROCm][Bugfix][Perf] enable shared expert fusion for Qwen3.5 (#44434)
- **2026-06-23** [`84f13374b3`](https://github.com/vllm-project/vllm/commit/84f13374b3) [#46164](https://github.com/vllm-project/vllm/pull/46164) — [CI] Fix `test_auto_gptq` on ROCm CI (#46164)
- **2026-06-23** [`b28103e1ca`](https://github.com/vllm-project/vllm/commit/b28103e1ca) [#46520](https://github.com/vllm-project/vllm/pull/46520) — [ROCm][CI] Shard LM Eval Qwen3-5 Models (B200-MI355) in AMD CI (#46520)
- **2026-06-23** [`68afd78897`](https://github.com/vllm-project/vllm/commit/68afd78897) [#46203](https://github.com/vllm-project/vllm/pull/46203) — [Bugfix][ROCm] Fix cumem sleep and teardown (#46203)
- **2026-06-23** [`e368415daa`](https://github.com/vllm-project/vllm/commit/e368415daa) [#46142](https://github.com/vllm-project/vllm/pull/46142) — [AMD][OCP MX][CI] Fix tests to not dispatch on `UNFUSED_TRITON` backend on MI300, improve w_mxfp4_a_fp8 emulation support (#46142)
- **2026-06-23** [`ceae5bcbda`](https://github.com/vllm-project/vllm/commit/ceae5bcbda) [#45219](https://github.com/vllm-project/vllm/pull/45219) — [ROCm][CI] Fix nixl tests (#45219)
- **2026-06-23** [`6691f087a6`](https://github.com/vllm-project/vllm/commit/6691f087a6) [#45892](https://github.com/vllm-project/vllm/pull/45892) — [Minimax-M3] BF16/FP8 Indexer using MSA (#45892)
- **2026-06-23** [`fd50a66015`](https://github.com/vllm-project/vllm/commit/fd50a66015) [#46160](https://github.com/vllm-project/vllm/pull/46160) — [CI][ROCm] Skip unsupported test cases on ROCm (#46160)
- **2026-06-23** [`84586c9acc`](https://github.com/vllm-project/vllm/commit/84586c9acc) [#46410](https://github.com/vllm-project/vllm/pull/46410) — [ROCm][CI] fix fp8 range in vit_fp8_quant (#46410)
- **2026-06-23** [`568874fec2`](https://github.com/vllm-project/vllm/commit/568874fec2) [#45869](https://github.com/vllm-project/vllm/pull/45869) — [ROCm][CI] pass merge-base to container for python-only wheel metadata (#45869)
- **2026-06-23** [`2aaaf3febd`](https://github.com/vllm-project/vllm/commit/2aaaf3febd) [#46260](https://github.com/vllm-project/vllm/pull/46260) — [ROCm][Test] Fix stale test_gfx950_moe MXFP4 oracle tests (#46260)
- **2026-06-23** [`156b12667c`](https://github.com/vllm-project/vllm/commit/156b12667c) [#46431](https://github.com/vllm-project/vllm/pull/46431) — [ROCm][CI] Skip Quark mxfp4 tests unless Quark version is compatible with Torch version (#46431)
- **2026-06-23** [`d32575a2d2`](https://github.com/vllm-project/vllm/commit/d32575a2d2) [#46332](https://github.com/vllm-project/vllm/pull/46332) — [ROCm][P/D] Support MoRIIO heterogeneous TP fan-in (#46332)
- **2026-06-23** [`20b5af55c1`](https://github.com/vllm-project/vllm/commit/20b5af55c1) [#43673](https://github.com/vllm-project/vllm/pull/43673) — [ROCm][Perf] DSv3.2: fuse MLA Q concat+fp8-quant in forward_mqa (#43673)
- **2026-06-23** [`7e47fb72b5`](https://github.com/vllm-project/vllm/commit/7e47fb72b5) [#46290](https://github.com/vllm-project/vllm/pull/46290) — [ROCm][P/D] Fix MoRIIO WRITE mode for mixed KV layouts (#46290)
- **2026-06-22** [`91ba720b75`](https://github.com/vllm-project/vllm/commit/91ba720b75) [#46148](https://github.com/vllm-project/vllm/pull/46148) — [ROCm][CI] Only require q_scale==1.0 for fp8 query in RocmAttention (#46148)
- **2026-06-22** [`c97e8f99d6`](https://github.com/vllm-project/vllm/commit/c97e8f99d6) [#43721](https://github.com/vllm-project/vllm/pull/43721) — [ROCm][Quantization][4/N] refactor quark_moe fp8 w/ oracle (#43721)
- **2026-06-22** [`6f6bd3b8fe`](https://github.com/vllm-project/vllm/commit/6f6bd3b8fe) [#46417](https://github.com/vllm-project/vllm/pull/46417) — [ROCm][CI] Increase the max wait time for server startup (#46417)
- **2026-06-22** [`70ef4d3009`](https://github.com/vllm-project/vllm/commit/70ef4d3009) [#46418](https://github.com/vllm-project/vllm/pull/46418) — [ROCm][CI] Purging away redundant test group definitions (#46418)
- **2026-06-22** [`fbf9ff7cf4`](https://github.com/vllm-project/vllm/commit/fbf9ff7cf4) [#46401](https://github.com/vllm-project/vllm/pull/46401) — [CI][ROCm] Restrict MLA cross-layer KV cache test to supported backends on ROCm (#46401)
- **2026-06-22** [`2b4a7491ec`](https://github.com/vllm-project/vllm/commit/2b4a7491ec) [#46141](https://github.com/vllm-project/vllm/pull/46141) — [ROCm][CI] Query total device memory via amdsmi to avoid HIP init (#46141)
- **2026-06-22** [`89accad2cc`](https://github.com/vllm-project/vllm/commit/89accad2cc) [#45931](https://github.com/vllm-project/vllm/pull/45931) — [ROCm][DSV4] Disable TileLang MHC dispatch on gfx942 (#45931)
- **2026-06-22** [`f3df7a7231`](https://github.com/vllm-project/vllm/commit/f3df7a7231) [#45955](https://github.com/vllm-project/vllm/pull/45955) — [ROCm][CI] Enable kv_connector unit tests on ROCm (#45955)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#47025](https://github.com/vllm-project/vllm/issues/47025) | [Bug]: Crash on using JSON structured output with speculative decoding | bug | 2026-06-29 |
| [#35465](https://github.com/vllm-project/vllm/issues/35465) | [Bug]: No available shared memory broadcast block found in 60 seconds. | bug | 2026-06-29 |
| [#46726](https://github.com/vllm-project/vllm/issues/46726) | [Bug]: sparse-MLA indexer error with  GLM 5.2 NVFP4 on RTX 6000 Pro SM | bug | 2026-06-29 |
| [#34752](https://github.com/vllm-project/vllm/issues/34752) | [Bug]: Improve `--kv-cache-dtype` behavior when checkpoint specifies ` | bug, good first issue, stale | 2026-06-29 |
| [#47005](https://github.com/vllm-project/vllm/issues/47005) | [Bug]: AssertionError: Overwriting existing tensor attribute: weight_l | bug | 2026-06-29 |
| [#44300](https://github.com/vllm-project/vllm/issues/44300) | [Feature]: Could you help with  implement the KV cache pruning feature | feature request, rocm | 2026-06-29 |
| [#46996](https://github.com/vllm-project/vllm/issues/46996) | [Bug]: Triton 3.8 NVIDIA availability probe poisons forked CUDA init a | — | 2026-06-29 |
| [#46985](https://github.com/vllm-project/vllm/issues/46985) | [Bug]: Why does kv-cache-dtype=fp8 OOM more easily than bf16/fp16 on l | bug | 2026-06-29 |
| [#35541](https://github.com/vllm-project/vllm/issues/35541) | [Bug]: vLLM hangs indefinitely with low `num_gpu_blocks_override` | bug, stale | 2026-06-29 |
| [#35896](https://github.com/vllm-project/vllm/issues/35896) | [Bug]: [CPU Backend] ARM build fails with distro/downstream PyTorch th | stale, cpu | 2026-06-29 |
| [#37900](https://github.com/vllm-project/vllm/issues/37900) | [Bug]: Engine V1 crash with WorkerProc leaked shared_memory on multi-G | bug, stale | 2026-06-29 |
| [#38459](https://github.com/vllm-project/vllm/issues/38459) | [Bug]: `limit_mm_per_prompt` is ineffective for Qwen3-VL | bug, stale | 2026-06-29 |
| [#33689](https://github.com/vllm-project/vllm/issues/33689) | [RFC]: KV Offloading Roadmap | RFC, keep-open | 2026-06-29 |
| [#34994](https://github.com/vllm-project/vllm/issues/34994) | [Feature]: Infrastructure Improvements for ROCm CI | feature request, rocm | 2026-06-28 |
| [#46715](https://github.com/vllm-project/vllm/issues/46715) | [Bug]: When the startup parameter "--max-model-len  auto --enable-chun | bug | 2026-06-28 |
| [#40554](https://github.com/vllm-project/vllm/issues/40554) | [AMD][CI Failure][Tracker] Static dashboard tracker for current CI fai | rocm, ci-failure | 2026-06-28 |
| [#45885](https://github.com/vllm-project/vllm/issues/45885) | [Bug]: ROCm MiniMax M3 MXFP8 Disagg not working | bug, rocm | 2026-06-28 |
| [#46967](https://github.com/vllm-project/vllm/issues/46967) | [Feature]:[New Model] Gemma4UnifiedForConditionalGeneration (google/ge | feature request | 2026-06-28 |
| [#46933](https://github.com/vllm-project/vllm/issues/46933) | [Bug]: CPU KV-Offloading CUDA Graph capture hang | bug | 2026-06-28 |
| [#41733](https://github.com/vllm-project/vllm/issues/41733) | [Roadmap] 2026 Q2 vLLM × RL Roadmap | — | 2026-06-28 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 74 |
| MoE / Expert Parallel | 51 |
| Other | 33 |
| Attention | 29 |
| Scheduler / Engine | 19 |
| Multimodal | 18 |
| Models | 14 |
| Serving / API | 14 |
| Quantization | 14 |
| CI / Build | 14 |
| KV Cache / Offload | 12 |
| Disaggregation / PD | 9 |
| Speculative Decoding | 8 |
| LoRA | 6 |
| Docs | 5 |
| Compilation / CUDA Graph | 1 |
| Distributed | 1 |
| Perf / Benchmark | 1 |

## ROCm / AMD  (74 commits)

- **2026-06-29** [`3483240b7e`](https://github.com/vllm-project/vllm/commit/3483240b7e) [#44512](https://github.com/vllm-project/vllm/pull/44512)
  [Frontend] Consolidate scale out entrypoints (#44512)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `docs/examples/README.md` _+41 more__
- **2026-06-29** [`db28ae2d07`](https://github.com/vllm-project/vllm/commit/db28ae2d07) [#46999](https://github.com/vllm-project/vllm/pull/46999)
  [ROCm][CI] Explicitly tear down multimodal offline LLMs (#46999)
  _Files: `tests/conftest.py`, `tests/entrypoints/multimodal/conftest.py`, `tests/entrypoints/multimodal/llm/test_chat.py`, `tests/entrypoints/multimodal/llm/test_mm_cache_external_injection.py` _+2 more__
- **2026-06-28** [`c2127a25c7`](https://github.com/vllm-project/vllm/commit/c2127a25c7) [#46895](https://github.com/vllm-project/vllm/pull/46895)
  [ROCm][CI] Fix `rlhf_async_new_apis` Example On ROCm (#46895)
  _Files: `examples/rl/rlhf_async_new_apis.py`_
- **2026-06-28** [`5ecae3266c`](https://github.com/vllm-project/vllm/commit/5ecae3266c) [#45033](https://github.com/vllm-project/vllm/pull/45033)
  [ROCm][Perf][MLA] Add AITER FlashAttention MLA prefill backend (`ROCM_AITER_FA`) (#45033)
  _Files: `tests/v1/attention/test_mla_prefill_registry.py`, `tests/v1/attention/test_mla_prefill_selector.py`, `vllm/v1/attention/backends/mla/prefill/aiter_flash_attn.py`, `vllm/v1/attention/backends/mla/prefill/registry.py` _+1 more__
- **2026-06-28** [`a2a92cbbaa`](https://github.com/vllm-project/vllm/commit/a2a92cbbaa) [#46930](https://github.com/vllm-project/vllm/pull/46930)
  [Hardware][AMD][CI] Tweak mirrored tests; improve CI base dependency change detection (#46930)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/distributed.yaml` _+2 more__
- **2026-06-28** [`c7ca0bccae`](https://github.com/vllm-project/vllm/commit/c7ca0bccae) [#44313](https://github.com/vllm-project/vllm/pull/44313)
  [ROCm][Perf] Add Fused Shared Expert (FSE) support for GLM-4.5/6/7 (#44313)
  _Files: `vllm/model_executor/models/glm4_moe.py`, `vllm/model_executor/models/glm4_moe_mtp.py`_
- **2026-06-28** [`a65f93fb2e`](https://github.com/vllm-project/vllm/commit/a65f93fb2e) [#46886](https://github.com/vllm-project/vllm/pull/46886)
  [ROCm][CI] Add ci_base metadata for external cache orchestration (#46886)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `docker/ci-rocm.hcl`_
- **2026-06-27** [`9036c89ee4`](https://github.com/vllm-project/vllm/commit/9036c89ee4) [#46928](https://github.com/vllm-project/vllm/pull/46928)
  [Hardware][AMD][CI] Patch Whisper multi LoRA test to use TRITON_ATTN for now (#46928)
  _Files: `tests/lora/test_whisper.py`_
- **2026-06-27** [`51a99565c3`](https://github.com/vllm-project/vllm/commit/51a99565c3) [#46474](https://github.com/vllm-project/vllm/pull/46474)
  [ROCm][Perf] Fused shared expert for Minimax M3 (#46474)
  _Files: `vllm/models/minimax_m3/amd/model.py`_
- **2026-06-27** [`867fd5e8ed`](https://github.com/vllm-project/vllm/commit/867fd5e8ed) [#46184](https://github.com/vllm-project/vllm/pull/46184)
  [ROCm][Perf] Use flydsl moe with Minimax-M3 mxfp8 weights on gfx950 and implemented moe-backend selection (#46184)
  _Files: `tests/kernels/moe/test_mxfp8_aiter_backend_selection.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp8_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py` _+1 more__
- **2026-06-27** [`9fd00ee006`](https://github.com/vllm-project/vllm/commit/9fd00ee006) [#46905](https://github.com/vllm-project/vllm/pull/46905)
  [ROCm][CI] Move remaining mi250_2 tests out of the MI250 queue (#46905)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-06-27** [`091d13976c`](https://github.com/vllm-project/vllm/commit/091d13976c) [#46891](https://github.com/vllm-project/vllm/pull/46891)
  [ROCm][CI] Add TRITON_ATTN score absolute tolerance floor (#46891)
  _Files: `tests/entrypoints/pooling/scoring/test_cross_encoder_online_vision.py`_
- **2026-06-27** [`68ee8300a0`](https://github.com/vllm-project/vllm/commit/68ee8300a0) [#46409](https://github.com/vllm-project/vllm/pull/46409)
  [ROCm][CI]Fix test_concat_and_cache_mla_rope_fused on ROCm (#46409)
  _Files: `tests/kernels/core/test_rotary_embedding_mla_cache_fused.py`_
- **2026-06-27** [`00e045b7c7`](https://github.com/vllm-project/vllm/commit/00e045b7c7) [#46758](https://github.com/vllm-project/vllm/pull/46758)
  [ROCm][CI TG] refactor and fix deepep_moe test group (#46758)
  _Files: `tests/kernels/moe/test_deepep_moe.py`, `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/kernels/moe/utils.py`_
- **2026-06-27** [`17a71d8702`](https://github.com/vllm-project/vllm/commit/17a71d8702) [#46658](https://github.com/vllm-project/vllm/pull/46658)
  [ROCm][CI] Relax fused layernorm quant test tolerances for one-ULP outliers (#46658)
  _Files: `tests/kernels/core/test_fused_quant_layernorm.py`, `tests/kernels/core/test_layernorm.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`, `tests/kernels/utils.py`_
- **2026-06-27** [`1a92dfcce4`](https://github.com/vllm-project/vllm/commit/1a92dfcce4) [#35232](https://github.com/vllm-project/vllm/pull/35232)
  [Build] Show error message when using ROCm with LTO and different compilers (#35232)
  _Files: `CMakeLists.txt`_
- **2026-06-26** [`2ff76a5e85`](https://github.com/vllm-project/vllm/commit/2ff76a5e85) [#46760](https://github.com/vllm-project/vllm/pull/46760)
  [ROCm][Bugfix] Pass num_kv_splits to aiter mla_reduce_v1 (#46760)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-06-26** [`6e2fb02fe5`](https://github.com/vllm-project/vllm/commit/6e2fb02fe5) [#46851](https://github.com/vllm-project/vllm/pull/46851)
  [ROCm][CI] Fix rlhf_nccl.py on ROCm (#46851)
  _Files: `examples/rl/rlhf_nccl.py`_
- **2026-06-26** [`274325dd43`](https://github.com/vllm-project/vllm/commit/274325dd43) [#46867](https://github.com/vllm-project/vllm/pull/46867)
  [ROCm][CI] Remove V1 Sample + Logits from mi250 Queue (#46867)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-06-26** [`95e6442a6b`](https://github.com/vllm-project/vllm/commit/95e6442a6b) [#46859](https://github.com/vllm-project/vllm/pull/46859)
  [Hardware][AMD][CI] Fix Kernels Quantization test timeout (#46859)
  _Files: `tests/kernels/quantization/test_nvfp4_emulation.py`_
- **2026-06-26** [`3d3b96488f`](https://github.com/vllm-project/vllm/commit/3d3b96488f) [#46705](https://github.com/vllm-project/vllm/pull/46705)
  Migrate Voxtral to mistral-common 1.11.5 audio API (#46705)
  _Files: `examples/generate/multimodal/audio_language_offline.py`, `requirements/common.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+8 more__
- **2026-06-26** [`c2507fb293`](https://github.com/vllm-project/vllm/commit/c2507fb293) [#46545](https://github.com/vllm-project/vllm/pull/46545)
  [ROCm] [MoE] [Perf] Shared-expert fusion for bias-routed MoE; enable on MiniMax-M3 mxfp8 model (#46545)
  _Files: `vllm/model_executor/layers/fused_moe/experts/mxfp8_native_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`, `vllm/model_executor/layers/fused_moe/router/router_factory.py` _+1 more__
- **2026-06-26** [`8921c4be88`](https://github.com/vllm-project/vllm/commit/8921c4be88) [#46122](https://github.com/vllm-project/vllm/pull/46122)
  [ROCm] [Performance] Optimize aiter moe for DeepSeekV4 (#46122)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-06-26** [`8e394244a5`](https://github.com/vllm-project/vllm/commit/8e394244a5) [#46419](https://github.com/vllm-project/vllm/pull/46419)
  [ROCm]Enable AITER MoE backend for MiniMax-M3-MXFP4 (#46419)
  _Files: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/models/minimax_m3/amd/model.py`_
- **2026-06-26** [`302954e5f6`](https://github.com/vllm-project/vllm/commit/302954e5f6) [#46823](https://github.com/vllm-project/vllm/pull/46823)
  [ROCm] [CI] fix transcription flakiness AMD: Entrypoints Integration (API Server OpenAI - Part 1) (mi325_1) (#46823)
  _Files: `tests/entrypoints/openai/test_run_batch.py`_
- **2026-06-26** [`d980a3cc6e`](https://github.com/vllm-project/vllm/commit/d980a3cc6e) [#46780](https://github.com/vllm-project/vllm/pull/46780)
  [ROCm] Fix AITER_UNIFIED_ATTN Dispatching After AITER Bump (#46780)
  _Files: `.buildkite/hardware_tests/amd.yaml`, `docs/design/attention_backends.md`, `tests/compile/passes/test_fusion_attn.py`, `tests/kernels/attention/test_rocm_aiter_unified_attn.py` _+2 more__
- **2026-06-26** [`35a49fcfc2`](https://github.com/vllm-project/vllm/commit/35a49fcfc2) [#46749](https://github.com/vllm-project/vllm/pull/46749)
  [CI][Bugfix] Spawn engine in mm cache sleep test to fix ROCm HIP error (#46749)
  _Files: `tests/multimodal/test_cache.py`_
- **2026-06-26** [`915e99ec67`](https://github.com/vllm-project/vllm/commit/915e99ec67) [#46741](https://github.com/vllm-project/vllm/pull/46741)
  [ROCm][Bugfix] Fix HIP fork re-init in multimodal offline examples (#46741)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-06-26** [`1a4984520e`](https://github.com/vllm-project/vllm/commit/1a4984520e) [#46792](https://github.com/vllm-project/vllm/pull/46792)
  [Hardware][AMD][CI] Fix AMD CI image build (#46792)
  _Files: `csrc/libtorch_stable/layernorm_kernels.cu`_
- **2026-06-25** [`27da2a2ac4`](https://github.com/vllm-project/vllm/commit/27da2a2ac4) [#46691](https://github.com/vllm-project/vllm/pull/46691)
  [Hardware][AMD][CI] Use Triton-based AITER MHA for LM Eval Qwen-3.5 Models Tests (#46691)
  _Files: `.buildkite/test-amd.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`, `vllm/v1/attention/ops/vit_attn_wrappers.py`_
- **2026-06-25** [`2a6f8f0c05`](https://github.com/vllm-project/vllm/commit/2a6f8f0c05) [#39238](https://github.com/vllm-project/vllm/pull/39238)
  [ROCm][CI] Fine-tuning queues and test names (#39238)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/e2e_integration.yaml` _+2 more__
- **2026-06-25** [`e53a17232c`](https://github.com/vllm-project/vllm/commit/e53a17232c) [#46692](https://github.com/vllm-project/vllm/pull/46692)
  [ROCm]: Bump aiter to 0.1.16.post2 (#46692)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-06-25** [`96eb8ddc41`](https://github.com/vllm-project/vllm/commit/96eb8ddc41) [#46671](https://github.com/vllm-project/vllm/pull/46671)
  [CI] Re-enable skipped glm and seedoss parser tests (#46671)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`_
- **2026-06-25** [`1744adc256`](https://github.com/vllm-project/vllm/commit/1744adc256) [#45666](https://github.com/vllm-project/vllm/pull/45666)
  [ROCM] [Communication] Add INT3 quantization method for quickreduce (#45666)
  _Files: `csrc/custom_quickreduce.cu`, `csrc/quickreduce/base.h`, `csrc/quickreduce/quick_reduce.h`, `csrc/quickreduce/quick_reduce_impl.cuh` _+3 more__
- **2026-06-25** [`cdfa2fd7e9`](https://github.com/vllm-project/vllm/commit/cdfa2fd7e9) [#46729](https://github.com/vllm-project/vllm/pull/46729)
  [ROCm][CI] rm duplicate Distributed Torchrun ci test (#46729)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-06-25** [`2365b7a8e7`](https://github.com/vllm-project/vllm/commit/2365b7a8e7) [#46668](https://github.com/vllm-project/vllm/pull/46668)
  [Hardware][AMD][CI] Mirror Basic Models (Others) and Weight Loading Multiple GPU test groups (#46668)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/weight_loading.yaml`_
- **2026-06-25** [`c63cd4906c`](https://github.com/vllm-project/vllm/commit/c63cd4906c) [#46546](https://github.com/vllm-project/vllm/pull/46546)
  [ROCm][ [Perf] sparse attention optimization on minimax-m3  (#46546)
  _Files: `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py` _+1 more__
- **2026-06-25** [`77c1d9fe9b`](https://github.com/vllm-project/vllm/commit/77c1d9fe9b) [#40784](https://github.com/vllm-project/vllm/pull/40784)
  [ROCm][Perf] Tune wvSplitK on gfx1151 (#40784)
  _Files: `csrc/rocm/skinny_gemms.cu`_
- **2026-06-25** [`e2af449c39`](https://github.com/vllm-project/vllm/commit/e2af449c39) [#46686](https://github.com/vllm-project/vllm/pull/46686)
  [Hardware][AMD][CI] Move Metrics, Tracing (2 GPUs) & make optional (#46686)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`_
- **2026-06-25** [`3f5a1e1733`](https://github.com/vllm-project/vllm/commit/3f5a1e1733) [#46573](https://github.com/vllm-project/vllm/pull/46573)
  [ROCm][CI] Expand basic correctness target suites (#46573)
  _Files: `.buildkite/test-amd.yaml`, `tests/basic_correctness/test_basic_correctness.py`, `tests/conftest.py`, `tests/utils.py`_
- **2026-06-25** [`710ebaa189`](https://github.com/vllm-project/vllm/commit/710ebaa189) [#46114](https://github.com/vllm-project/vllm/pull/46114)
  [ROCm][Bugfix] Fix chunk alignment when using context parallelism with TRITON_MLA (#46114)
  _Files: `tests/distributed/test_context_parallel.py`, `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-06-25** [`dc55936f64`](https://github.com/vllm-project/vllm/commit/dc55936f64) [#46650](https://github.com/vllm-project/vllm/pull/46650)
  [AMD][CI] Fix Pipeline + Context Parallelism test group (#46650)
  _Files: `tests/distributed/test_pp_cudagraph.py`_
- **2026-06-25** [`6e3a983cf3`](https://github.com/vllm-project/vllm/commit/6e3a983cf3) [#46655](https://github.com/vllm-project/vllm/pull/46655)
  [ROCm] Remove erroneous inclusion of gptq_marlin as supported quant scheme on ROCm (#46655)
  _Files: `vllm/platforms/rocm.py`_
- **2026-06-24** [`d6696e2385`](https://github.com/vllm-project/vllm/commit/d6696e2385) [#46636](https://github.com/vllm-project/vllm/pull/46636)
  [ROCm] Begin Deprecation Window for CUDA_VISIBLE_DEVICES on ROCm (#46636)
  _Files: `vllm/platforms/rocm.py`_
- **2026-06-24** [`cf57311187`](https://github.com/vllm-project/vllm/commit/cf57311187) [#46386](https://github.com/vllm-project/vllm/pull/46386)
  Run DeepSeek-V2-Lite prefetch-offload eval eager on ROCm (#46386)
  _Files: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_prefetch_offload.sh`_
- **2026-06-24** [`b3a688cb9e`](https://github.com/vllm-project/vllm/commit/b3a688cb9e) [#46548](https://github.com/vllm-project/vllm/pull/46548)
  [ROCm] Fix OOB During Model Warmup With `ROCM_ATTN` and MRV2 (#46548)
  _Files: `csrc/rocm/attention.cu`, `tests/kernels/attention/test_attention.py`, `tests/kernels/quantization/test_triton_scaled_mm.py`_
- **2026-06-24** [`61ee183d28`](https://github.com/vllm-project/vllm/commit/61ee183d28) [#46414](https://github.com/vllm-project/vllm/pull/46414)
  [ROCm] Fix AITER FP8 quantization schema tests (#46414)
  _Files: `tests/rocm/aiter/test_quant_op_schema.py`_
- **2026-06-24** [`d7c1821b5a`](https://github.com/vllm-project/vllm/commit/d7c1821b5a) [#45810](https://github.com/vllm-project/vllm/pull/45810)
  [Model][MiniMax-M3] Add pipeline parallelism support (#45810)
  _Files: `docs/models/supported_models.md`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/nvidia/model.py`_
- **2026-06-24** [`549c7074cd`](https://github.com/vllm-project/vllm/commit/549c7074cd) [#46580](https://github.com/vllm-project/vllm/pull/46580)
  [ROCm][CI] Skip the MoE Marlin tile-padding helper assertion (#46580)
  _Files: `tests/kernels/quantization/test_marlin_tile_padding.py`_
- **2026-06-24** [`e2bdc24612`](https://github.com/vllm-project/vllm/commit/e2bdc24612) [#45998](https://github.com/vllm-project/vllm/pull/45998)
  [ROCm][Bugfix] Fix `use_v2_model_runner` inside Ray driver thread (#45998)
  _Files: `.buildkite/test_areas/distributed.yaml`, `vllm/triton_utils/importing.py`_
- **2026-06-24** [`bcbeaac786`](https://github.com/vllm-project/vllm/commit/bcbeaac786) [#46537](https://github.com/vllm-project/vllm/pull/46537)
  [ROCm][CI] Stage C-II of gating additional test groups (#46537)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/engine.yaml` _+6 more__
- **2026-06-23** [`80e511772f`](https://github.com/vllm-project/vllm/commit/80e511772f) [#44434](https://github.com/vllm-project/vllm/pull/44434)
  [ROCm][Bugfix][Perf] enable shared expert fusion for Qwen3.5 (#44434)
  _Files: `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`_
- **2026-06-23** [`84f13374b3`](https://github.com/vllm-project/vllm/commit/84f13374b3) [#46164](https://github.com/vllm-project/vllm/pull/46164)
  [CI] Fix `test_auto_gptq` on ROCm CI (#46164)
  _Files: `tests/quantization/test_configs.py`_
- **2026-06-23** [`b28103e1ca`](https://github.com/vllm-project/vllm/commit/b28103e1ca) [#46520](https://github.com/vllm-project/vllm/pull/46520)
  [ROCm][CI] Shard LM Eval Qwen3-5 Models (B200-MI355) in AMD CI (#46520)
  _Files: `.buildkite/test-amd.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`_
- **2026-06-23** [`68afd78897`](https://github.com/vllm-project/vllm/commit/68afd78897) [#46203](https://github.com/vllm-project/vllm/pull/46203)
  [Bugfix][ROCm] Fix cumem sleep and teardown (#46203)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/basic_correctness.yaml`, `csrc/cumem_allocator.cpp`, `vllm/device_allocator/__init__.py` _+3 more__
- **2026-06-23** [`e368415daa`](https://github.com/vllm-project/vllm/commit/e368415daa) [#46142](https://github.com/vllm-project/vllm/pull/46142)
  [AMD][OCP MX][CI] Fix tests to not dispatch on `UNFUSED_TRITON` backend on MI300, improve w_mxfp4_a_fp8 emulation support (#46142)
  _Files: `tests/models/quantization/test_gpt_oss.py`, `tests/quantization/test_quark.py`, `vllm/model_executor/layers/fused_moe/experts/ocp_mx_emulation_moe.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py` _+3 more__
- **2026-06-23** [`ceae5bcbda`](https://github.com/vllm-project/vllm/commit/ceae5bcbda) [#45219](https://github.com/vllm-project/vllm/pull/45219)
  [ROCm][CI] Fix nixl tests (#45219)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/disaggregated.yaml`, `tests/config/test_model_arch_config.py`, `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` _+4 more__
- **2026-06-23** [`6691f087a6`](https://github.com/vllm-project/vllm/commit/6691f087a6) [#45892](https://github.com/vllm-project/vllm/pull/45892)
  [Minimax-M3] BF16/FP8 Indexer using MSA (#45892)
  _Files: `cmake/external_projects/fmha_sm100.cmake`, `csrc/libtorch_stable/fused_minimax_m3_qknorm_rope_kv_insert_kernel.cu`, `setup.py`, `tests/kernels/attention/test_minimax_m3.py` _+9 more__
- **2026-06-23** [`fd50a66015`](https://github.com/vllm-project/vllm/commit/fd50a66015) [#46160](https://github.com/vllm-project/vllm/pull/46160)
  [CI][ROCm] Skip unsupported test cases on ROCm (#46160)
  _Files: `tests/quantization/test_compressed_tensors.py`, `tests/quantization/test_modelopt.py`_
- **2026-06-23** [`84586c9acc`](https://github.com/vllm-project/vllm/commit/84586c9acc) [#46410](https://github.com/vllm-project/vllm/pull/46410)
  [ROCm][CI] fix fp8 range in vit_fp8_quant (#46410)
  _Files: `tests/kernels/core/test_vit_fp8_quant.py`_
- **2026-06-23** [`568874fec2`](https://github.com/vllm-project/vllm/commit/568874fec2) [#45869](https://github.com/vllm-project/vllm/pull/45869)
  [ROCm][CI] pass merge-base to container for python-only wheel metadata (#45869)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/test_areas/misc.yaml`, `tests/standalone_tests/python_only_compile.sh`_
- **2026-06-23** [`2aaaf3febd`](https://github.com/vllm-project/vllm/commit/2aaaf3febd) [#46260](https://github.com/vllm-project/vllm/pull/46260)
  [ROCm][Test] Fix stale test_gfx950_moe MXFP4 oracle tests (#46260)
  _Files: `tests/quantization/test_gfx950_moe.py`_
- **2026-06-23** [`156b12667c`](https://github.com/vllm-project/vllm/commit/156b12667c) [#46431](https://github.com/vllm-project/vllm/pull/46431)
  [ROCm][CI] Skip Quark mxfp4 tests unless Quark version is compatible with Torch version (#46431)
  _Files: `tests/evals/gsm8k/test_gsm8k_correctness.py`, `tests/kernels/moe/test_ocp_mx_moe.py`_
- **2026-06-23** [`d32575a2d2`](https://github.com/vllm-project/vllm/commit/d32575a2d2) [#46332](https://github.com/vllm-project/vllm/pull/46332)
  [ROCm][P/D] Support MoRIIO heterogeneous TP fan-in (#46332)
  _Files: `tests/v1/kv_connector/unit/test_moriio_connector.py`, `tests/v1/kv_connector/unit/test_moriio_kv_layout.py`, `tests/v1/kv_connector/unit/test_moriio_tp_ack.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py` _+2 more__
- **2026-06-23** [`20b5af55c1`](https://github.com/vllm-project/vllm/commit/20b5af55c1) [#43673](https://github.com/vllm-project/vllm/pull/43673)
  [ROCm][Perf] DSv3.2: fuse MLA Q concat+fp8-quant in forward_mqa (#43673)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-06-23** [`7e47fb72b5`](https://github.com/vllm-project/vllm/commit/7e47fb72b5) [#46290](https://github.com/vllm-project/vllm/pull/46290)
  [ROCm][P/D] Fix MoRIIO WRITE mode for mixed KV layouts (#46290)
  _Files: `tests/v1/kv_connector/unit/test_moriio_connector.py`, `tests/v1/kv_connector/unit/test_moriio_kv_layout.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py` _+2 more__
- **2026-06-22** [`91ba720b75`](https://github.com/vllm-project/vllm/commit/91ba720b75) [#46148](https://github.com/vllm-project/vllm/pull/46148)
  [ROCm][CI] Only require q_scale==1.0 for fp8 query in RocmAttention (#46148)
  _Files: `vllm/v1/attention/backends/rocm_attn.py`_
- **2026-06-22** [`c97e8f99d6`](https://github.com/vllm-project/vllm/commit/c97e8f99d6) [#43721](https://github.com/vllm-project/vllm/pull/43721)
  [ROCm][Quantization][4/N] refactor quark_moe fp8 w/ oracle (#43721)
  _Files: `tests/evals/gsm8k/configs/Qwen3-30B-A3B-Thinking-2507-FP8.yaml`, `tests/evals/gsm8k/configs/Qwen3-30B-A3B-Thinking-2507-PTPC-FP8.yaml`, `tests/evals/gsm8k/configs/models-mi3xx-fp8-and-mixed.txt`, `tests/evals/gsm8k/test_gsm8k_correctness.py` _+1 more__
- **2026-06-22** [`6f6bd3b8fe`](https://github.com/vllm-project/vllm/commit/6f6bd3b8fe) [#46417](https://github.com/vllm-project/vllm/pull/46417)
  [ROCm][CI] Increase the max wait time for server startup (#46417)
  _Files: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-EMU-TP2.yaml`_
- **2026-06-22** [`70ef4d3009`](https://github.com/vllm-project/vllm/commit/70ef4d3009) [#46418](https://github.com/vllm-project/vllm/pull/46418)
  [ROCm][CI] Purging away redundant test group definitions (#46418)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-06-22** [`fbf9ff7cf4`](https://github.com/vllm-project/vllm/commit/fbf9ff7cf4) [#46401](https://github.com/vllm-project/vllm/pull/46401)
  [CI][ROCm] Restrict MLA cross-layer KV cache test to supported backends on ROCm (#46401)
  _Files: `tests/v1/kv_connector/unit/test_kv_cache_layout.py`_
- **2026-06-22** [`2b4a7491ec`](https://github.com/vllm-project/vllm/commit/2b4a7491ec) [#46141](https://github.com/vllm-project/vllm/pull/46141)
  [ROCm][CI] Query total device memory via amdsmi to avoid HIP init (#46141)
  _Files: `vllm/platforms/rocm.py`_
- **2026-06-22** [`89accad2cc`](https://github.com/vllm-project/vllm/commit/89accad2cc) [#45931](https://github.com/vllm-project/vllm/pull/45931)
  [ROCm][DSV4] Disable TileLang MHC dispatch on gfx942 (#45931)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/model_executor/layers/mhc.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mtp.py`_
- **2026-06-22** [`f3df7a7231`](https://github.com/vllm-project/vllm/commit/f3df7a7231) [#45955](https://github.com/vllm-project/vllm/pull/45955)
  [ROCm][CI] Enable kv_connector unit tests on ROCm (#45955)
  _Files: `.buildkite/scripts/install-kv-connectors.sh`, `.buildkite/test_areas/misc.yaml`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `tests/v1/kv_connector/unit/test_offloading_connector.py`_

## MoE / Expert Parallel  (51 commits)

- **2026-06-29** [`e186107870`](https://github.com/vllm-project/vllm/commit/e186107870) [#45961](https://github.com/vllm-project/vllm/pull/45961)
  [Bugfix] Use native SiLU activation in CPU fused MoE (#45961)
  _Files: `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`_
- **2026-06-29** [`f6bb8682ee`](https://github.com/vllm-project/vllm/commit/f6bb8682ee) [#47009](https://github.com/vllm-project/vllm/pull/47009)
  Fix docs on main (#47009)
  _Files: `docs/design/moe_kernel_features.md`_
- **2026-06-29** [`58d6a6e60a`](https://github.com/vllm-project/vllm/commit/58d6a6e60a) [#42920](https://github.com/vllm-project/vllm/pull/42920)
  [CPU] Support cpu compressed-tensor w8a8 int8 moe (#42920)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `tests/kernels/moe/test_cpu_quant_fused_moe.py`, `tests/quantization/test_cpu_w8a8.py`, `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py` _+2 more__
- **2026-06-29** [`a2abce646f`](https://github.com/vllm-project/vllm/commit/a2abce646f) [#38128](https://github.com/vllm-project/vllm/pull/38128)
  [EPLB] Mask padding in EPLB load recording (#38128)
  _Files: `tests/distributed/test_eplb_fused_moe_layer_dep_nvfp4.py`, `tests/kernels/moe/test_moe_layer.py`, `tests/kernels/moe/test_routing.py`, `tests/model_executor/test_routed_experts_capture.py` _+13 more__
- **2026-06-29** [`311ad689ad`](https://github.com/vllm-project/vllm/commit/311ad689ad) [#46956](https://github.com/vllm-project/vllm/pull/46956)
  Remove boilerplate missed by #46820 (#46956)
  _Files: `vllm/model_executor/models/gemma4_unified.py`, `vllm/model_executor/models/mllama4.py`, `vllm/model_executor/models/param2moe.py`, `vllm/model_executor/models/sarvam.py` _+2 more__
- **2026-06-28** [`4dfbf1503b`](https://github.com/vllm-project/vllm/commit/4dfbf1503b) [#41026](https://github.com/vllm-project/vllm/pull/41026)
  [Model] Add support for openai/privacy-filter (#41026)
  _Files: `docs/models/pooling_models/token_classify.md`, `tests/models/language/pooling/test_token_classification.py`, `tests/models/registry.py`, `vllm/model_executor/layers/fused_moe/oracle/unquantized.py` _+4 more__
- **2026-06-28** [`03c6d01c30`](https://github.com/vllm-project/vllm/commit/03c6d01c30) [#46629](https://github.com/vllm-project/vllm/pull/46629)
  [OCP MX ] Add back emulation to available OCP MX backends list (#46629)
  _Files: `tests/models/quantization/test_gpt_oss.py`, `tests/quantization/test_quark.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-06-28** [`89876b0c54`](https://github.com/vllm-project/vllm/commit/89876b0c54) [#46876](https://github.com/vllm-project/vllm/pull/46876)
  [GLM5] Implement op fusion for GLM5/DSV3.2 (#46876)
  _Files: `tests/kernels/test_fused_deepseek_v32_norm_rope.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`, `vllm/model_executor/layers/sparse_attn_indexer.py` _+5 more__
- **2026-06-28** [`5c91039c41`](https://github.com/vllm-project/vllm/commit/5c91039c41) [#46635](https://github.com/vllm-project/vllm/pull/46635)
  [GLM5.2 Perf] Replace MOE all-reduce with reduce-scatter, 3.1%~3.2 E2E Throughput improvement (#46635)
  _Files: `vllm/model_executor/models/deepseek_v2.py`_
- **2026-06-27** [`35e3850fa9`](https://github.com/vllm-project/vllm/commit/35e3850fa9) [#46915](https://github.com/vllm-project/vllm/pull/46915)
  [Bugfix][Test] Fix test_flashinfer_cutlass_mxfp4_fused_moe on sm90 (stale weight/scale interleave) (#46915)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`_
- **2026-06-27** [`ddd3855a28`](https://github.com/vllm-project/vllm/commit/ddd3855a28) [#45924](https://github.com/vllm-project/vllm/pull/45924)
  [MoE Backend] add HPC-Ops MoE backend (#45924)
  _Files: `docs/design/moe_kernel_features.md`, `vllm/config/kernel.py`, `vllm/model_executor/layers/fused_moe/hpc_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py` _+1 more__
- **2026-06-26** [`d8eb734d94`](https://github.com/vllm-project/vllm/commit/d8eb734d94) [#46820](https://github.com/vllm-project/vllm/pull/46820)
  Fix Transformers backend FP8 MoE and remove some boilerplate (#46820)
  _Files: `vllm/model_executor/models/AXK1.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py` _+25 more__
- **2026-06-26** [`c6554f321c`](https://github.com/vllm-project/vllm/commit/c6554f321c) [#46769](https://github.com/vllm-project/vllm/pull/46769)
  [CPU] Fix macOS/Apple Silicon hang by enabling OpenMP in the build (#46769)
  _Files: `.github/actionlint.yaml`, `.github/workflows/macos-smoke-test.yml`, `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_attn_impl.hpp` _+6 more__
- **2026-06-26** [`37ce34922f`](https://github.com/vllm-project/vllm/commit/37ce34922f) [#46735](https://github.com/vllm-project/vllm/pull/46735)
  [CI] Fix failing CUDA graph capture in Triton MOE (#46735)
  _Files: `vllm/model_executor/layers/fused_moe/experts/nvfp4_emulation_moe.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`_
- **2026-06-26** [`c7645bce04`](https://github.com/vllm-project/vllm/commit/c7645bce04) [#46706](https://github.com/vllm-project/vllm/pull/46706)
  Remove grok model arch from vllm (#46706)
  _Files: `docs/configuration/optimization.md`, `docs/models/supported_models.md`, `tests/models/language/generation/test_grok.py`, `tests/models/registry.py` _+9 more__
- **2026-06-26** [`552a9dbe59`](https://github.com/vllm-project/vllm/commit/552a9dbe59) [#44667](https://github.com/vllm-project/vllm/pull/44667)
  [NVFP4][Emulation] Fuse NVFP4 weight dequantization with compute in triton kernel for w13/w2 MOE MLP linears (#44667)
  _Files: `tests/kernels/quantization/test_nvfp4_emulation.py`, `vllm/model_executor/layers/fused_moe/experts/nvfp4_emulation_moe.py`, `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`_
- **2026-06-25** [`e8c24a7695`](https://github.com/vllm-project/vllm/commit/e8c24a7695) [#46643](https://github.com/vllm-project/vllm/pull/46643)
  [Kernel] Vectorized fp32 `moe_sum` reduction and support any topk (#46643)
  _Files: `csrc/libtorch_stable/moe/moe_align_sum_kernels.cu`, `tests/kernels/moe/test_moe.py`_
- **2026-06-25** [`8b4d93ba2b`](https://github.com/vllm-project/vllm/commit/8b4d93ba2b) [#46651](https://github.com/vllm-project/vllm/pull/46651)
  [Perf] Remove redundant clone for GLM, Deepseek etc (#46651)
  _Files: `vllm/model_executor/models/AXK1.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/glm4_moe_lite.py`, `vllm/model_executor/models/openpangu.py`_
- **2026-06-25** [`e8e7b592d1`](https://github.com/vllm-project/vllm/commit/e8e7b592d1) [#46642](https://github.com/vllm-project/vllm/pull/46642)
  [Kernel][MoE] Tune block-FP8 fused MoE for low-batch decode (#46642)
  _Files: `benchmarks/kernels/benchmark_moe.py`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=768,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/fused_moe/configs/E=160,N=640,device_name=NVIDIA_H100,dtype=fp8_w8a8,block_shape=[128,128].json` _+6 more__
- **2026-06-25** [`9bfd878a48`](https://github.com/vllm-project/vllm/commit/9bfd878a48) [#43461](https://github.com/vllm-project/vllm/pull/43461)
  [MoE] [MoE Refactor] Add moe kernel oracle abc 37753 (#43461)
  _Files: `tests/kernels/moe/test_moe_kernel_oracle.py`, `vllm/model_executor/layers/fused_moe/oracle/__init__.py`, `vllm/model_executor/layers/fused_moe/oracle/base.py`, `vllm/model_executor/layers/fused_moe/oracle/unquantized.py` _+1 more__
- **2026-06-25** [`4d3b4b9b01`](https://github.com/vllm-project/vllm/commit/4d3b4b9b01) [#46584](https://github.com/vllm-project/vllm/pull/46584)
  [Rust Frontend] Make `ToolParserOutput` a seq of `ToolParserEvent` to preserve order (#46584)
  _Files: `rust/src/chat/src/output/default/unified.rs`, `rust/src/parser/benches/utils/mod.rs`, `rust/src/parser/python/src/lib.rs`, `rust/src/parser/src/tool/deepseek_dsml/deepseek_v32.rs` _+28 more__
- **2026-06-25** [`76c3c4ff63`](https://github.com/vllm-project/vllm/commit/76c3c4ff63) [#46583](https://github.com/vllm-project/vllm/pull/46583)
  [Rust Frontend] Introduce unified parser interface & combined parser (#46583)
  _Files: `pyproject.toml`, `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/Cargo.toml` _+70 more__
- **2026-06-25** [`1273a8f05a`](https://github.com/vllm-project/vllm/commit/1273a8f05a) [#36559](https://github.com/vllm-project/vllm/pull/36559)
  [Kernel] Add swap AB optimization to fused_moe_kernel (#36559)
  _Files: `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/utils.py`_
- **2026-06-24** [`fc7fc421e9`](https://github.com/vllm-project/vllm/commit/fc7fc421e9) [#46518](https://github.com/vllm-project/vllm/pull/46518)
  [Kernel][MoE] Allow FlashInfer MXINT4 MoE for gated SiLU (#46518)
  _Files: `tests/kernels/moe/test_marlin_vs_trtllm_mxint4.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_mxint4_moe.py`_
- **2026-06-24** [`d7ab9be775`](https://github.com/vllm-project/vllm/commit/d7ab9be775) [#46408](https://github.com/vllm-project/vllm/pull/46408)
  [Bugfix] Support -1 (invalid/non-local) slots in topk_ids for Triton MoE (#46408)
  _Files: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`_
- **2026-06-24** [`6a1570711c`](https://github.com/vllm-project/vllm/commit/6a1570711c) [#46406](https://github.com/vllm-project/vllm/pull/46406)
  [Bugfix] Support non-power-of-2 top_k in legacy triton_kernels routing (#46406)
  _Files: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`_
- **2026-06-24** [`3c43237233`](https://github.com/vllm-project/vllm/commit/3c43237233) [#46560](https://github.com/vllm-project/vllm/pull/46560)
  [Bugfix][Model Runner V2][Spec Decode] Fix int32 offset overflow in sampler kernels (#46560)
  _Files: `tests/v1/sample/test_logprobs.py`, `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_triton.py`, `vllm/v1/worker/gpu/sample/bad_words.py` _+6 more__
- **2026-06-24** [`24d5186138`](https://github.com/vllm-project/vllm/commit/24d5186138) [#46339](https://github.com/vllm-project/vllm/pull/46339)
  [Bugfix] Re-enable FP8 MoE on NVIDIA Thor (#46339)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/quantization/w8a8/cutlass/scaled_mm_entry.cu`_
- **2026-06-24** [`7dc036058b`](https://github.com/vllm-project/vllm/commit/7dc036058b) [#44720](https://github.com/vllm-project/vllm/pull/44720)
  [Doc] Document Qwen3.6 (dense + MoE) ViT CUDA graph support (#44720)
  _Files: `docs/design/cuda_graphs_multimodal.md`_
- **2026-06-24** [`061043eaca`](https://github.com/vllm-project/vllm/commit/061043eaca) [#46353](https://github.com/vllm-project/vllm/pull/46353)
  [CPU][Perf] Accelerate unquantized MoE for AArch64 (#46353)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `benchmarks/kernels/cpu/benchmark_cpu_fused_moe.py`, `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_fused_moe.cpp` _+11 more__
- **2026-06-24** [`191826ec61`](https://github.com/vllm-project/vllm/commit/191826ec61) [#46550](https://github.com/vllm-project/vllm/pull/46550)
  [CI/Build] Fix topk histogram build on SM75 (#46550)
  _Files: `csrc/libtorch_stable/topk_histogram_4096.cuh`_
- **2026-06-24** [`96de8bb389`](https://github.com/vllm-project/vllm/commit/96de8bb389) [#46549](https://github.com/vllm-project/vllm/pull/46549)
  [MoE] Free unused MXFP4 scales in OAI Triton Backend (#46549)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/mxfp4.py`_
- **2026-06-24** [`9d6fdc2901`](https://github.com/vllm-project/vllm/commit/9d6fdc2901) [#46385](https://github.com/vllm-project/vllm/pull/46385)
  [Kernel] GLM5 Router GEMM (#46385)
  _Files: `csrc/libtorch_stable/moe/dsv3_router_gemm_bf16_out.cu`, `csrc/libtorch_stable/moe/dsv3_router_gemm_entry.cu`, `csrc/libtorch_stable/moe/dsv3_router_gemm_float_out.cu`, `vllm/model_executor/layers/fused_moe/router/gate_linear.py`_
- **2026-06-24** [`4ed8eaafb0`](https://github.com/vllm-project/vllm/commit/4ed8eaafb0) [#46057](https://github.com/vllm-project/vllm/pull/46057)
  [Rust Frontend] Integrate `xgrammar-structural-tag` for `strict` and `required` tool calling (#46057)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/error.rs` _+19 more__
- **2026-06-23** [`855cd4d787`](https://github.com/vllm-project/vllm/commit/855cd4d787) [#43008](https://github.com/vllm-project/vllm/pull/43008)
  [Perf][DSv4/DSv3.2] Add cluster-cooperative topK kernel for low-latency scenarios (#43008)
  _Files: `.buildkite/test_areas/kernels.yaml`, `CMakeLists.txt`, `csrc/libtorch_stable/cooperative_topk.cu`, `csrc/libtorch_stable/cooperative_topk.cuh` _+6 more__
- **2026-06-23** [`0a3e2dbc09`](https://github.com/vllm-project/vllm/commit/0a3e2dbc09) [#46428](https://github.com/vllm-project/vllm/pull/46428)
  [Optimization] Skip DP padding tokens in MoE (#46428)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/envs.py`, `vllm/forward_context.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py` _+5 more__
- **2026-06-23** [`0d4d164488`](https://github.com/vllm-project/vllm/commit/0d4d164488) [#46492](https://github.com/vllm-project/vllm/pull/46492)
  [Bugfix] Allow flashinfer_cutlass as a clamped NVFP4 MoE backend (#46492)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py`_
- **2026-06-23** [`0775b882ba`](https://github.com/vllm-project/vllm/commit/0775b882ba) [#45836](https://github.com/vllm-project/vllm/pull/45836)
  [NVFP4 MoE/Deepseek V4] Marlin: wire SwiGLU clamp + allow it for clamped models on non-Blackwell (#45836)
  _Files: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py`_
- **2026-06-23** [`acce57d8dd`](https://github.com/vllm-project/vllm/commit/acce57d8dd) [#44514](https://github.com/vllm-project/vllm/pull/44514)
  Deprecate old FP8 online MoE quantization class (#44514)
  _Files: `tests/quantization/test_fp8.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/model_loader/base_loader.py`_
- **2026-06-23** [`37a682d392`](https://github.com/vllm-project/vllm/commit/37a682d392) [#45703](https://github.com/vllm-project/vllm/pull/45703)
  [Kernel] Extend Marlin thread-tile padding to MoE (WNA16 + FP8/MXFP8) (#45703)
  _Files: `tests/kernels/quantization/test_marlin_tile_padding.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/quantization/auto_awq.py`, `vllm/model_executor/layers/quantization/auto_gptq.py` _+3 more__
- **2026-06-23** [`f4d5f73ffa`](https://github.com/vllm-project/vllm/commit/f4d5f73ffa) [#45818](https://github.com/vllm-project/vllm/pull/45818)
  [Bugfix]: Fix unquantized gpt-oss weight loading broken by FusedMoE r… (#45818)
  _Files: `vllm/model_executor/models/gpt_oss.py`_
- **2026-06-23** [`f3410b3bb1`](https://github.com/vllm-project/vllm/commit/f3410b3bb1) [#45404](https://github.com/vllm-project/vllm/pull/45404)
  fix(moe_wna16): access tp_size via moe_config for RoutedExperts compatibility (#45404)
  _Files: `vllm/model_executor/layers/quantization/moe_wna16.py`_
- **2026-06-23** [`04c2a8deac`](https://github.com/vllm-project/vllm/commit/04c2a8deac) [#46432](https://github.com/vllm-project/vllm/pull/46432)
  [DeepEP V2] Fill invalid recv_topk_idx with -1 (#46432)
  _Files: `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_v2.py`_
- **2026-06-23** [`8207ce0850`](https://github.com/vllm-project/vllm/commit/8207ce0850) [#46420](https://github.com/vllm-project/vllm/pull/46420)
  [Bugfix] Fix humming lm_head crash and FusedMoE weight_shape coercion (#46420)
  _Files: `tests/evals/gsm8k/configs/gemma-4-E4B-it-qat-mobile-ct.yaml`, `tests/evals/gsm8k/configs/models-small.txt`, `tests/evals/gsm8k/test_gsm8k_correctness.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py` _+1 more__
- **2026-06-23** [`e48592066e`](https://github.com/vllm-project/vllm/commit/e48592066e) [#46404](https://github.com/vllm-project/vllm/pull/46404)
  [DeepEP V2] Bound num_max_tokens_per_rank in do_expand=False (#46404)
  _Files: `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_v2.py`_
- **2026-06-22** [`ca5b24695b`](https://github.com/vllm-project/vllm/commit/ca5b24695b) [#41161](https://github.com/vllm-project/vllm/pull/41161)
  Fix static actorder handling for compressed-tensors WNA16 MoE (#41161)
  _Files: `tests/quantization/test_compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_wna16.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_wna16_marlin.py`_
- **2026-06-22** [`c0b2d8f471`](https://github.com/vllm-project/vllm/commit/c0b2d8f471) [#43362](https://github.com/vllm-project/vllm/pull/43362)
  [Bugfix] FusedMoE: coerce shape-(1,) per-tensor scales to 0-D scalar … (#43362)
  _Files: `tests/kernels/moe/test_moe_weight_loading_padded.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-06-22** [`44d95069e9`](https://github.com/vllm-project/vllm/commit/44d95069e9) [#43477](https://github.com/vllm-project/vllm/pull/43477)
  Enable DeepSeek V4 and GLM-5.1 on SM120 (#43477)
  _Files: `.buildkite/intel_jobs/expert_parallelism_intel.yaml`, `.buildkite/intel_jobs/models_multimodal_intel.yaml`, `cmake/external_projects/deepgemm.cmake`, `cmake/external_projects/qutlass.cmake` _+33 more__
- **2026-06-22** [`ccd49f6821`](https://github.com/vllm-project/vllm/commit/ccd49f6821) [#41722](https://github.com/vllm-project/vllm/pull/41722)
  [MyPy] Fix mypy for `vllm/lora` (#41722)
  _Files: `tests/lora/test_lora_manager.py`, `tools/pre_commit/mypy.py`, `vllm/lora/layers/base_linear.py`, `vllm/lora/layers/column_parallel_linear.py` _+11 more__
- **2026-06-22** [`9037498c22`](https://github.com/vllm-project/vllm/commit/9037498c22) [#44517](https://github.com/vllm-project/vllm/pull/44517)
  [DSV4][XPU] Pass gemm1_clamp_limit to XpuFusedMoe (#44517)
  _Files: `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`_
- **2026-06-22** [`485bbe1c6f`](https://github.com/vllm-project/vllm/commit/485bbe1c6f) [#46163](https://github.com/vllm-project/vllm/pull/46163)
  [CI] Fix missing `tp_size` attribute on `RoutedExperts` (#46163)
  _Files: `vllm/model_executor/layers/quantization/moe_wna16.py`_

## Other  (33 commits)

- **2026-06-29** [`a4e3cb40d0`](https://github.com/vllm-project/vllm/commit/a4e3cb40d0) [#47018](https://github.com/vllm-project/vllm/pull/47018)
  [mypy] Enable mypy for tests directory (#47018)
  _Files: `tools/pre_commit/mypy.py`_
- **2026-06-29** [`5274c1181d`](https://github.com/vllm-project/vllm/commit/5274c1181d) [#46800](https://github.com/vllm-project/vllm/pull/46800)
  [Rust Frontend] Add Harmony Renderer for GPT-OSS (#46800)
  _Files: `rust/Cargo.lock`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/lib.rs` _+23 more__
- **2026-06-27** [`b6caeb5a09`](https://github.com/vllm-project/vllm/commit/b6caeb5a09) [#46878](https://github.com/vllm-project/vllm/pull/46878)
  [Model Runner V2][Spec Decode] Use fp32 uniform threshold for acceptance (#46878)
  _Files: `vllm/v1/worker/gpu/sample/gumbel.py`, `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-06-27** [`56aa067bf0`](https://github.com/vllm-project/vllm/commit/56aa067bf0) [#46927](https://github.com/vllm-project/vllm/pull/46927)
  [CI Bug] Fix h100 `AssertionError: Cold-start child failed` (#46927)
  _Files: `tests/compile/h100/test_startup.py`_
- **2026-06-26** [`77f8796d16`](https://github.com/vllm-project/vllm/commit/77f8796d16) [#46437](https://github.com/vllm-project/vllm/pull/46437)
  [Frontend][Gpt-oss] Use `process_eos()` to flush Harmony Parser outputs. (#46437)
  _Files: `tests/parser/test_harmony.py`, `vllm/parser/harmony.py`_
- **2026-06-26** [`e71bc6da85`](https://github.com/vllm-project/vllm/commit/e71bc6da85) [#46799](https://github.com/vllm-project/vllm/pull/46799)
  [Rust Frontend] Use `oss-harmony` for Harmony output processing (#46799)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`_
- **2026-06-26** [`63e161f296`](https://github.com/vllm-project/vllm/commit/63e161f296) [#46486](https://github.com/vllm-project/vllm/pull/46486)
  [Bugfix][Tool Parser] PoolsideV1: fix string whitespace and required named tool choice (#46486)
  _Files: `tests/tool_parsers/test_poolside_v1_tool_parser.py`, `vllm/tool_parsers/poolside_v1_tool_parser.py`_
- **2026-06-26** [`5b33041746`](https://github.com/vllm-project/vllm/commit/5b33041746) [#46773](https://github.com/vllm-project/vllm/pull/46773)
  [ModelRunner V2] Fix whisper test (#46773)
  _Files: `vllm/v1/worker/gpu/mm/encoder_cache.py`, `vllm/v1/worker/gpu/model_states/mm_pruning.py`_
- **2026-06-26** [`e312c5cb25`](https://github.com/vllm-project/vllm/commit/e312c5cb25) [#46507](https://github.com/vllm-project/vllm/pull/46507)
  [Rust Frontend] Make Granite4 string argument scanning incremental (#46507)
  _Files: `rust/src/parser/Cargo.toml`, `rust/src/parser/benches/granite4.rs`, `rust/src/parser/src/tool/json/granite4.rs`, `rust/src/parser/src/utils.rs`_
- **2026-06-26** [`3daea7ceb9`](https://github.com/vllm-project/vllm/commit/3daea7ceb9) [#46759](https://github.com/vllm-project/vllm/pull/46759)
  [Bugfix][MRV2] Forward seq_lens_cpu_upper_bound for mamba hybrid models (#46759)
  _Files: `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`_
- **2026-06-26** [`32bb3195f0`](https://github.com/vllm-project/vllm/commit/32bb3195f0) [#46746](https://github.com/vllm-project/vllm/pull/46746)
  [ModelRunner V2] Bound memory for large logprobs requests (#46746)
  _Files: `vllm/v1/worker/gpu/sample/logprob.py`_
- **2026-06-25** [`c53994e134`](https://github.com/vllm-project/vllm/commit/c53994e134) [#46665](https://github.com/vllm-project/vllm/pull/46665)
  [Model Runner V2][Spec Decode] Use log1p to compute residual during rejection sampling (#46665)
  _Files: `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-06-25** [`efb5acffd5`](https://github.com/vllm-project/vllm/commit/efb5acffd5) [#46382](https://github.com/vllm-project/vllm/pull/46382)
  [Bugfix] fix: stream Mimimax m2 tool call string arguments (#46382)
  _Files: `vllm/parser/minimax_m2.py`_
- **2026-06-24** [`e06a83445c`](https://github.com/vllm-project/vllm/commit/e06a83445c) [#46101](https://github.com/vllm-project/vllm/pull/46101)
  [Bugfix] Normalize slashes in Helion GPU names (#46101)
  _Files: `tests/kernels/helion/test_utils.py`, `vllm/kernels/helion/utils.py`_
- **2026-06-24** [`2801b11156`](https://github.com/vllm-project/vllm/commit/2801b11156) [#45914](https://github.com/vllm-project/vllm/pull/45914)
  [Test] Pin block_size in auto-fit max_model_len test (#45914)
  _Files: `tests/v1/e2e/general/test_context_length.py`_
- **2026-06-24** [`007b5a52ed`](https://github.com/vllm-project/vllm/commit/007b5a52ed) [#46511](https://github.com/vllm-project/vllm/pull/46511)
  [Log] Update to log once  (#46511)
  _Files: `vllm/platforms/cpu.py`, `vllm/platforms/cuda.py`, `vllm/platforms/interface.py`, `vllm/platforms/xpu.py`_
- **2026-06-24** [`160c80a34c`](https://github.com/vllm-project/vllm/commit/160c80a34c) [#46582](https://github.com/vllm-project/vllm/pull/46582)
  [Rust Frontend] Raise frontend JSON body limit (#46582)
  _Files: `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-06-23** [`abc33134fa`](https://github.com/vllm-project/vllm/commit/abc33134fa) [#46530](https://github.com/vllm-project/vllm/pull/46530)
  [CI Test] Mark batch invariance test flaky (#46530)
  _Files: `tests/v1/determinism/test_batch_invariance.py`_
- **2026-06-23** [`6617db1bfb`](https://github.com/vllm-project/vllm/commit/6617db1bfb) [#46308](https://github.com/vllm-project/vllm/pull/46308)
  [Bugfix][Frontend] Emit non-ASCII tool-call arguments without \uXXXX escapes (#46308)
  _Files: `tests/tool_parsers/test_hunyuan_a13b_tool_parser.py`, `tests/tool_parsers/test_seed_oss_tool_parser.py`, `tests/tool_parsers/test_xlam_tool_parser.py`, `vllm/tool_parsers/hunyuan_a13b_tool_parser.py` _+2 more__
- **2026-06-23** [`899d72a58c`](https://github.com/vllm-project/vllm/commit/899d72a58c) [#45389](https://github.com/vllm-project/vllm/pull/45389)
  [Bugfix][ToolParser] Handle braces in required tool streaming strings (#45389)
  _Files: `tests/tool_use/test_tool_choice_required.py`, `vllm/tool_parsers/streaming.py`_
- **2026-06-23** [`d8e422ccda`](https://github.com/vllm-project/vllm/commit/d8e422ccda) [#45718](https://github.com/vllm-project/vllm/pull/45718)
  [Bugfix] Parse MiniMax M3 streaming reasoning by text markers (#45718)
  _Files: `tests/reasoning/test_minimax_m3_reasoning_parser.py`, `vllm/reasoning/minimax_m3_reasoning_parser.py`_
- **2026-06-23** [`2d721ab5d8`](https://github.com/vllm-project/vllm/commit/2d721ab5d8) [#46348](https://github.com/vllm-project/vllm/pull/46348)
  [Rust Frontend] Align Rust allowed_token_ids validation with Python (#46348)
  _Files: `rust/src/server/src/error.rs`, `rust/src/server/src/routes/tests.rs`, `rust/src/text/src/error.rs`, `rust/src/text/src/lib.rs` _+2 more__
- **2026-06-23** [`a46f3eb232`](https://github.com/vllm-project/vllm/commit/a46f3eb232) [#46245](https://github.com/vllm-project/vllm/pull/46245)
  [Bugfix][Model Runner V2] Preserve all allowed_token_ids in the logit bias kernel (#46245)
  _Files: `tests/v1/sample/test_sampling_params_e2e.py`, `vllm/v1/worker/gpu/sample/logit_bias.py`_
- **2026-06-22** [`82ede09a5a`](https://github.com/vllm-project/vllm/commit/82ede09a5a) [#46278](https://github.com/vllm-project/vllm/pull/46278)
  [Bugfix][KVConnector] Fix SimpleCPUOffloadConnector GPU->CPU store race (#46278)
  _Files: `tests/v1/simple_kv_offload/test_worker.py`, `vllm/v1/simple_kv_offload/copy_backend.py`, `vllm/v1/simple_kv_offload/cuda_mem_ops.py`, `vllm/v1/simple_kv_offload/worker.py`_
- **2026-06-22** [`fbf520cf3a`](https://github.com/vllm-project/vllm/commit/fbf520cf3a) [#46096](https://github.com/vllm-project/vllm/pull/46096)
  [MRV2] Generalize use of `WhisperModelState` (#46096)
  _Files: `vllm/v1/worker/gpu/model_states/__init__.py`, `vllm/v1/worker/gpu/model_states/default.py`, `vllm/v1/worker/gpu/model_states/encoder_decoder.py`, `vllm/v1/worker/gpu/model_states/interface.py`_
- **2026-06-22** [`1c7bc18318`](https://github.com/vllm-project/vllm/commit/1c7bc18318) [#46365](https://github.com/vllm-project/vllm/pull/46365)
  [Bugfix][CPU] Fix CPU model runner v2 (#46365)
  _Files: `vllm/v1/worker/cpu/shm.py`_
- **2026-06-22** [`a4610da0c6`](https://github.com/vllm-project/vllm/commit/a4610da0c6) [#46373](https://github.com/vllm-project/vllm/pull/46373)
  [docs] link security docs from AGENTS (#46373)
  _Files: `AGENTS.md`_
- **2026-06-22** [`d2c671c29b`](https://github.com/vllm-project/vllm/commit/d2c671c29b) [#44324](https://github.com/vllm-project/vllm/pull/44324)
  [CPU][RISC-V] Add RVV micro GEMM for WNA16 (#44324)
  _Files: `csrc/cpu/cpu_wna16.cpp`, `csrc/cpu/micro_gemm/cpu_micro_gemm_rvv.hpp`, `csrc/cpu/utils.hpp`, `vllm/model_executor/kernels/linear/mixed_precision/cpu.py`_
- **2026-06-22** [`78739e3bda`](https://github.com/vllm-project/vllm/commit/78739e3bda) [#46313](https://github.com/vllm-project/vllm/pull/46313)
  [Bugfix] Reject matryoshka embedding dimensions above hidden size (#46313)
  _Files: `tests/test_pooling_params.py`, `vllm/pooling_params.py`_
- **2026-06-22** [`1c4b51b990`](https://github.com/vllm-project/vllm/commit/1c4b51b990) [#46352](https://github.com/vllm-project/vllm/pull/46352)
  Temporarily skip M3 on CI (#46352)
  _Files: `tests/models/registry.py`_
- **2026-06-22** [`68567ef2df`](https://github.com/vllm-project/vllm/commit/68567ef2df) [#46216](https://github.com/vllm-project/vllm/pull/46216)
  [CPUOffloadingManager] Maintain evictable list in LRUCachePolicy (#46216)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/v1/kv_offload/cpu/manager.py`, `vllm/v1/kv_offload/cpu/policies/base.py` _+1 more__
- **2026-06-22** [`6bc6f2d86d`](https://github.com/vllm-project/vllm/commit/6bc6f2d86d) [#45939](https://github.com/vllm-project/vllm/pull/45939)
  [1/N][Core] add partial prefix cache primitives (#45939)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_primitives.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/block_pool.py` _+1 more__
- **2026-06-22** [`31124749d1`](https://github.com/vllm-project/vllm/commit/31124749d1) [#46113](https://github.com/vllm-project/vllm/pull/46113)
  [Bugfix] [Rust Frontend] Fix stop string truncation with repeated matches (#46113)
  _Files: `rust/src/text/src/output/decoded.rs`_

## Attention  (29 commits)

- **2026-06-28** [`4b643c463e`](https://github.com/vllm-project/vllm/commit/4b643c463e) [#46961](https://github.com/vllm-project/vllm/pull/46961)
  [GLM5] Fix minor typo (#46961)
  _Files: `vllm/models/deepseek_v32/nvidia/attention.py`_
- **2026-06-28** [`c6741b2ad4`](https://github.com/vllm-project/vllm/commit/c6741b2ad4) [#46564](https://github.com/vllm-project/vllm/pull/46564)
  [Model] Support Unlimited OCR (#46564)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/v1/core/test_single_type_kv_cache_manager.py`, `vllm/config/model.py` _+31 more__
- **2026-06-27** [`d0f800811b`](https://github.com/vllm-project/vllm/commit/d0f800811b) [#46644](https://github.com/vllm-project/vllm/pull/46644)
  [Build] Update vllm to point to vllm-project/flash-attention commit that builds FA3 with torch stable API.  (#46644)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`_
- **2026-06-26** [`1d41009e81`](https://github.com/vllm-project/vllm/commit/1d41009e81) [#46753](https://github.com/vllm-project/vllm/pull/46753)
  [ModelRunner V2] Fix cross-attention block table sizing (#46753)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-06-26** [`c40d307731`](https://github.com/vllm-project/vllm/commit/c40d307731) [#36701](https://github.com/vllm-project/vllm/pull/36701)
  [Core] Remove FlashAttention block size restriction for hybrid models (#36701)
  _Files: `vllm/v1/attention/backends/flash_attn.py`_
- **2026-06-26** [`65e655d295`](https://github.com/vllm-project/vllm/commit/65e655d295) [#46808](https://github.com/vllm-project/vllm/pull/46808)
  [GLM-5] Add DSV3.2/GLM5 to `vllm/models/` (#46808)
  _Files: `vllm/models/deepseek_v32/__init__.py`, `vllm/models/deepseek_v32/nvidia/__init__.py`, `vllm/models/deepseek_v32/nvidia/attention.py`, `vllm/models/deepseek_v32/nvidia/model.py` _+1 more__
- **2026-06-26** [`02a1f23711`](https://github.com/vllm-project/vllm/commit/02a1f23711) [#46761](https://github.com/vllm-project/vllm/pull/46761)
  [DFlash] Fuse precompute kv per-layer rmsnorms (#46761)
  _Files: `csrc/libtorch_stable/layernorm_kernels.cu`, `tests/kernels/core/test_batched_weight_rms_norm.py`, `vllm/model_executor/models/qwen3_dflash.py`_
- **2026-06-26** [`5314665bad`](https://github.com/vllm-project/vllm/commit/5314665bad) [#46770](https://github.com/vllm-project/vllm/pull/46770)
  [Model Runner V2][DFlash] Enable dflash attention backend selection (#46770)
  _Files: `vllm/v1/worker/gpu/spec_decode/dflash/utils.py`_
- **2026-06-25** [`8fa36fbbeb`](https://github.com/vllm-project/vllm/commit/8fa36fbbeb) [#46506](https://github.com/vllm-project/vllm/pull/46506)
  [Bugfix] FLASHINFER_MLA_SPARSE_SM120 compatibility with GLM-5 NVFP4 (#46506)
  _Files: `vllm/v1/attention/backends/mla/flashinfer_mla_sparse_sm120.py`_
- **2026-06-25** [`2396d91e93`](https://github.com/vllm-project/vllm/commit/2396d91e93) [#44029](https://github.com/vllm-project/vllm/pull/44029)
  [CPU][Spec Decode] Enable DFlash SD for CPU (#44029)
  _Files: `csrc/cpu/spec_decode_utils.cpp`, `csrc/cpu/torch_bindings.cpp`, `docs/design/attention_backends.md`, `vllm/model_executor/models/qwen3_dflash.py` _+4 more__
- **2026-06-25** [`fc61c6fc26`](https://github.com/vllm-project/vllm/commit/fc61c6fc26) [#46392](https://github.com/vllm-project/vllm/pull/46392)
  [Perf] Enable + tune FlashInfer fused allreduce at world_size=16 on SM 10.3 (GB300) (#46392)
  _Files: `benchmarks/kernels/benchmark_fused_collective.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`, `vllm/config/compilation.py`_
- **2026-06-24** [`49f2104c53`](https://github.com/vllm-project/vllm/commit/49f2104c53) [#44044](https://github.com/vllm-project/vllm/pull/44044)
  [Feature] Support DCP with FP8 KV cache in MLA decode path (#44044)
  _Files: `tests/kernels/attention/test_cache.py`, `tests/v1/attention/test_mla_backends.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backends/mla/flashmla.py`_
- **2026-06-24** [`d511b5bae9`](https://github.com/vllm-project/vllm/commit/d511b5bae9) [#40469](https://github.com/vllm-project/vllm/pull/40469)
  Chore: Fix minor doc sentence, grammar, quote errors (#40469)
  _Files: `docs/design/hybrid_kv_cache_manager.md`, `docs/design/paged_attention.md`, `vllm/v1/engine/__init__.py`_
- **2026-06-24** [`70749fdcca`](https://github.com/vllm-project/vllm/commit/70749fdcca) [#40835](https://github.com/vllm-project/vllm/pull/40835)
  [Feature] Triton INT4 per-token-head KV cache quantization (#40835)
  _Files: `docs/design/attention_backends.md`, `tests/models/quantization/test_per_token_kv_cache.py`, `tests/quantization/test_per_token_kv_cache.py`, `vllm/config/cache.py` _+6 more__
- **2026-06-24** [`ede54b926e`](https://github.com/vllm-project/vllm/commit/ede54b926e) [#46555](https://github.com/vllm-project/vllm/pull/46555)
  set AttentionCGSupport.UNIFORM_BATCH for fa2 on xpu (#46555)
  _Files: `vllm/v1/attention/backends/flash_attn.py`_
- **2026-06-24** [`dc0d318177`](https://github.com/vllm-project/vllm/commit/dc0d318177) [#46189](https://github.com/vllm-project/vllm/pull/46189)
  [Attention] Add FLASH_ATTN_MLA_SPARSE backend for Hopper sparse MLA (#46189)
  _Files: `docs/design/attention_backends.md`, `vllm/platforms/cuda.py`, `vllm/v1/attention/backends/mla/flashattn_mla_sparse.py`, `vllm/v1/attention/backends/registry.py`_
- **2026-06-23** [`11b56b2ff2`](https://github.com/vllm-project/vllm/commit/11b56b2ff2) [#46393](https://github.com/vllm-project/vllm/pull/46393)
  [Kernel] Add FlashInferCutedslMxfp8LinearKernel (cute-dsl mm_mxfp8) (#46393)
  _Files: `vllm/config/kernel.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/mxfp8/flashinfer.py`_
- **2026-06-23** [`7c2e08451a`](https://github.com/vllm-project/vllm/commit/7c2e08451a) [#46517](https://github.com/vllm-project/vllm/pull/46517)
  [Docker] Remove redundant flashinfer download-cubin step (#46517)
  _Files: `docker/Dockerfile`_
- **2026-06-23** [`ef361de916`](https://github.com/vllm-project/vllm/commit/ef361de916) [#46435](https://github.com/vllm-project/vllm/pull/46435)
  [Model Runer V2][DFlash] Fix lm head sharing for dflash (#46435)
  _Files: `vllm/v1/worker/gpu/spec_decode/dflash/utils.py`_
- **2026-06-23** [`9f5117820f`](https://github.com/vllm-project/vllm/commit/9f5117820f) [#46135](https://github.com/vllm-project/vllm/pull/46135)
  [HARDWARE][POWER] Enable fp16 support for PowerPC (#46135)
  _Files: `csrc/cpu/cpu_attn_impl.hpp`, `csrc/cpu/cpu_attn_vsx.hpp`, `csrc/cpu/cpu_types_vsx.hpp`, `csrc/cpu/mla_decode.cpp` _+2 more__
- **2026-06-23** [`430a95ae3a`](https://github.com/vllm-project/vllm/commit/430a95ae3a) [#45845](https://github.com/vllm-project/vllm/pull/45845)
  [v1][kvcache] Honor prefix-cache retention interval for Mamba/linear attention (#45845)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-06-23** [`56e5797511`](https://github.com/vllm-project/vllm/commit/56e5797511) [#45375](https://github.com/vllm-project/vllm/pull/45375)
  [Quant] Enable modelopt_mixed on Turing (SM75) (#45375)
  _Files: `docs/design/attention_backends.md`, `vllm/model_executor/layers/quantization/modelopt.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-06-22** [`183b5f27ea`](https://github.com/vllm-project/vllm/commit/183b5f27ea) [#44053](https://github.com/vllm-project/vllm/pull/44053)
  [Bugfix][V1][TurboQuant] Reserve workspace before CUDA graph capture (#44053)
  _Files: `tests/quantization/test_turboquant.py`, `vllm/v1/attention/backends/turboquant_attn.py`_
- **2026-06-22** [`d1a38c2762`](https://github.com/vllm-project/vllm/commit/d1a38c2762) [#42235](https://github.com/vllm-project/vllm/pull/42235)
  [Kernel][Performance] Add FlashInfer cutedsl NVFP4 GEMM backend (#42235)
  _Files: `tests/kernels/quantization/test_flashinfer_nvfp4_scaled_mm.py`, `tests/models/quantization/test_nvfp4.py`, `vllm/compilation/passes/fusion/collective_fusion.py`, `vllm/config/kernel.py` _+2 more__
- **2026-06-22** [`aa4990a9a2`](https://github.com/vllm-project/vllm/commit/aa4990a9a2) [#45111](https://github.com/vllm-project/vllm/pull/45111)
  [Attention] Re-enable cross-layer KV cache layout for MLA via stride-aware kernels (#45111)
  _Files: `csrc/libtorch_stable/attention/mla/sm100_cutlass_mla_kernel.cu`, `csrc/libtorch_stable/cache_kernels.cu`, `tests/kernels/attention/test_cutlass_mla_decode.py`, `tests/kernels/attention/test_mla_cross_layer_kernel_equivalence.py` _+9 more__
- **2026-06-22** [`3c8e49596c`](https://github.com/vllm-project/vllm/commit/3c8e49596c) [#46108](https://github.com/vllm-project/vllm/pull/46108)
  [Model] ColQwen3.5: fix retrieval correctness (bias + bidirectional) (#46108)
  _Files: `docs/models/pooling_models/token_embed.md`, `examples/pooling/score/colqwen3_5_rerank_online.py`, `tests/models/multimodal/pooling/test_colqwen3_5.py`, `vllm/model_executor/layers/attention/attention.py` _+3 more__
- **2026-06-22** [`cec2ec1176`](https://github.com/vllm-project/vllm/commit/cec2ec1176) [#45100](https://github.com/vllm-project/vllm/pull/45100)
  [Bugfix] Avoid racy accepted counts in async spec decode (#45100)
  _Files: `tests/v1/attention/test_gdn_metadata_builder.py`, `vllm/v1/attention/backends/gdn_attn.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-06-22** [`d14e551a53`](https://github.com/vllm-project/vllm/commit/d14e551a53) [#45993](https://github.com/vllm-project/vllm/pull/45993)
  [Model] Remove MiniMaxText01, MiniMaxVL01, MiniMaxForCausalLM (#45993)
  _Files: `docs/contributing/model/basic.md`, `docs/features/tool_calling.md`, `docs/models/supported_models.md`, `docs/usage/v1_guide.md` _+16 more__
- **2026-06-22** [`db32b53e30`](https://github.com/vllm-project/vllm/commit/db32b53e30) [#43081](https://github.com/vllm-project/vllm/pull/43081)
  [SpecDecode] Support DFlash with FlashInfer  (#43081)
  _Files: `docs/design/attention_backends.md`, `tests/kernels/attention/test_attention_selector.py`, `vllm/v1/attention/backends/flashinfer.py`_

## Scheduler / Engine  (19 commits)

- **2026-06-28** [`09841ae705`](https://github.com/vllm-project/vllm/commit/09841ae705) [#46846](https://github.com/vllm-project/vllm/pull/46846)
  [Render][Speculator] Add return_loss_mask to render endpoint for training data generation (#46846)
  _Files: `tests/entrypoints/serve/render/test_render.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/serve/disagg/protocol.py`, `vllm/entrypoints/serve/render/serving.py` _+3 more__
- **2026-06-26** [`658b54efe4`](https://github.com/vllm-project/vllm/commit/658b54efe4) [#46771](https://github.com/vllm-project/vllm/pull/46771)
  [ModelRunner V2] Update scheduler tests to cover MRV2 paths (#46771)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`_
- **2026-06-26** [`950ee4c2e4`](https://github.com/vllm-project/vllm/commit/950ee4c2e4) [#44226](https://github.com/vllm-project/vllm/pull/44226)
  [API] Add token offsets to render endpoints (/v1/.../render) (#44226)
  _Files: `tests/entrypoints/openai/test_render_token_offsets.py`, `tests/entrypoints/serve/render/test_render.py`, `tests/renderers/test_completions.py`, `tests/renderers/test_token_offsets.py` _+9 more__
- **2026-06-25** [`c5e3c40877`](https://github.com/vllm-project/vllm/commit/c5e3c40877) [#46628](https://github.com/vllm-project/vllm/pull/46628)
  Fix P/D with DP Supervisor (#46628)
  _Files: `vllm/v1/engine/core.py`_
- **2026-06-25** [`d490b98162`](https://github.com/vllm-project/vllm/commit/d490b98162) [#45237](https://github.com/vllm-project/vllm/pull/45237)
  [Core] Avoid mixed length specdec batches via padding (#45237)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-06-25** [`9b215ae60b`](https://github.com/vllm-project/vllm/commit/9b215ae60b) [#44610](https://github.com/vllm-project/vllm/pull/44610)
  [Rust Frontend] Forward `VLLM_ENGINE_READY_TIMEOUT_S` via `--args-json` (#44610)
  _Files: `vllm/v1/utils.py`_
- **2026-06-25** [`36fd7e8b86`](https://github.com/vllm-project/vllm/commit/36fd7e8b86) [#46394](https://github.com/vllm-project/vllm/pull/46394)
  [SimpleCPUOffloadConnector] Fix remaining global→block conversions under PCP/DCP (#46394)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-06-24** [`84c2f9f0fb`](https://github.com/vllm-project/vllm/commit/84c2f9f0fb) [#46344](https://github.com/vllm-project/vllm/pull/46344)
  [Frontend] Fix Kimi K2 tool call IDs for required tool choice (#46344)
  _Files: `tests/entrypoints/openai/chat_completion/test_completion_with_function_calling.py`, `tests/entrypoints/openai/responses/test_parsable_context_unit.py`, `tests/parser/test_parse.py`, `tests/parser/test_streaming.py` _+7 more__
- **2026-06-24** [`1cd3e0e945`](https://github.com/vllm-project/vllm/commit/1cd3e0e945) [#46627](https://github.com/vllm-project/vllm/pull/46627)
  [Bug] Fix `IndentationError: expected an indented block after 'with' statement` (#46627)
  _Files: `vllm/v1/engine/core.py`_
- **2026-06-24** [`93ec645878`](https://github.com/vllm-project/vllm/commit/93ec645878) [#44483](https://github.com/vllm-project/vllm/pull/44483)
  [Bugfix] Fix illegal memory access from a forward during a partial wake_up (#44483)
  _Files: `vllm/v1/engine/core.py`_
- **2026-06-24** [`f1a6703edd`](https://github.com/vllm-project/vllm/commit/f1a6703edd) [#46220](https://github.com/vllm-project/vllm/pull/46220)
  [Bugfix][Config] Keep pydantic validation for fields with a TYPE_CHECKING Literal alias (#46220)
  _Files: `vllm/config/load.py`, `vllm/config/model.py`, `vllm/engine/arg_utils.py`_
- **2026-06-24** [`ce9f64020b`](https://github.com/vllm-project/vllm/commit/ce9f64020b) [#46360](https://github.com/vllm-project/vllm/pull/46360)
  [Rust Frontend] Pass effective `reasoning_parser_kwargs` for structured output (#46360)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/renderer/deepseek_v32/mod.rs`, `rust/src/chat/src/renderer/deepseek_v4/mod.rs`, `rust/src/chat/src/renderer/hf/mod.rs` _+15 more__
- **2026-06-24** [`6af0559ddb`](https://github.com/vllm-project/vllm/commit/6af0559ddb) [#46532](https://github.com/vllm-project/vllm/pull/46532)
  [Core][DP] Throttle prefills based on local prefill work (#46532)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-06-23** [`d86c66c981`](https://github.com/vllm-project/vllm/commit/d86c66c981) [#46167](https://github.com/vllm-project/vllm/pull/46167)
  [Feat] Add runtime monitor for post-warmup CuTeDSL compilation (#46167)
  _Files: `tests/engine/test_arg_utils.py`, `tests/test_jit_monitor.py`, `vllm/config/observability.py`, `vllm/engine/arg_utils.py` _+3 more__
- **2026-06-23** [`25bc3be49c`](https://github.com/vllm-project/vllm/commit/25bc3be49c) [#46359](https://github.com/vllm-project/vllm/pull/46359)
  [Rust Frontend] Correct `--reasoning-parser` semantics (#46359)
  _Files: `.buildkite/test_areas/rust_frontend.yaml`, `rust/Cargo.lock`, `rust/src/cmd/Cargo.toml`, `rust/src/cmd/src/cli.rs` _+3 more__
- **2026-06-23** [`6c427dd401`](https://github.com/vllm-project/vllm/commit/6c427dd401) [#44105](https://github.com/vllm-project/vllm/pull/44105)
  [BugFix] Omit empty tool_calls from OpenAI chat responses (#44105)
  _Files: `tests/entrypoints/openai/chat_completion/test_completion_with_function_calling.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/test_tool_choice_content_none.py`, `vllm/entrypoints/openai/chat_completion/protocol.py` _+1 more__
- **2026-06-23** [`8db12169a4`](https://github.com/vllm-project/vllm/commit/8db12169a4) [#46351](https://github.com/vllm-project/vllm/pull/46351)
  fix: stream Qwen3 tool call string arguments (#46351)
  _Files: `tests/parser/engine/test_parser_engine.py`, `tests/parser/engine/test_qwen3.py`, `vllm/parser/engine/parser_engine.py`, `vllm/parser/qwen3.py`_
- **2026-06-22** [`80abe0de7d`](https://github.com/vllm-project/vllm/commit/80abe0de7d) [#46137](https://github.com/vllm-project/vllm/pull/46137)
  [Rust Frontend] Support thinking_token_budget for chat and completions (#46137)
  _Files: `rust/src/engine-core-client/src/protocol/mod.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py`, `rust/src/server/src/error.rs` _+9 more__
- **2026-06-22** [`1eb2cc961e`](https://github.com/vllm-project/vllm/commit/1eb2cc961e) [#46022](https://github.com/vllm-project/vllm/pull/46022)
  [Frontend] Refactor ServingTokenization entrypoint. (#46022)
  _Files: `tests/entrypoints/serve/tokenize/test_serving_tokenization.py`, `vllm/entrypoints/anthropic/api_router.py`, `vllm/entrypoints/openai/api_server.py`, `vllm/entrypoints/openai/engine/serving.py` _+11 more__

## Multimodal  (18 commits)

- **2026-06-29** [`59575da46d`](https://github.com/vllm-project/vllm/commit/59575da46d) [#47008](https://github.com/vllm-project/vllm/pull/47008)
  [XPU] exclude unsupported models for test_tensor_sechma.py (#47008)
  _Files: `.buildkite/intel_jobs/models_multimodal_intel.yaml`, `tests/models/multimodal/processing/test_common.py`_
- **2026-06-29** [`4559c43a95`](https://github.com/vllm-project/vllm/commit/4559c43a95) [#43591](https://github.com/vllm-project/vllm/pull/43591)
  [MM][CG] Gemma3 Encoder CUDA Graph (#43591)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/gemma3_mm.py`_
- **2026-06-28** [`7544286b04`](https://github.com/vllm-project/vllm/commit/7544286b04) [#46552](https://github.com/vllm-project/vllm/pull/46552)
  [Bugfix] Transformers backend: recompute `mm_token_type_ids` per request for M-RoPE (#46552)
  _Files: `vllm/model_executor/models/transformers/multimodal.py`_
- **2026-06-28** [`35e6c86caa`](https://github.com/vllm-project/vllm/commit/35e6c86caa) [#46034](https://github.com/vllm-project/vllm/pull/46034)
  [Bugfix][MM][CG] Enable dual-path ViT CUDA graph for Step3-VL (#46034)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `vllm/model_executor/models/step3_vl.py`_
- **2026-06-27** [`af16446bf3`](https://github.com/vllm-project/vllm/commit/af16446bf3) [#44465](https://github.com/vllm-project/vllm/pull/44465)
  Vram semaphore infra (#44465)
  _Files: `requirements/cuda.txt`, `tests/multimodal/test_gpu_ipc_memory.py`, `tests/multimodal/test_video.py`, `tests/v1/worker/test_gpu_worker.py` _+7 more__
- **2026-06-26** [`abc71548ef`](https://github.com/vllm-project/vllm/commit/abc71548ef) [#46831](https://github.com/vllm-project/vllm/pull/46831)
  [CI/Build][CPU] Add test image cache clean-up  (#46831)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test.sh`_
- **2026-06-26** [`1502cf6274`](https://github.com/vllm-project/vllm/commit/1502cf6274) [#45263](https://github.com/vllm-project/vllm/pull/45263)
  Fix relative allowed local media paths (#45263)
  _Files: `tests/multimodal/media/test_connector.py`, `vllm/multimodal/media/connector.py`_
- **2026-06-26** [`1d3f4cb3a4`](https://github.com/vllm-project/vllm/commit/1d3f4cb3a4) [#46719](https://github.com/vllm-project/vllm/pull/46719)
  [Rust Frontend] Extract renderer fixture test utilities (#46719)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/multimodal.rs` _+5 more__
- **2026-06-25** [`a2e8ec3d52`](https://github.com/vllm-project/vllm/commit/a2e8ec3d52) [#46736](https://github.com/vllm-project/vllm/pull/46736)
  [CI] Depend GPQA Eval DGX Spark job on arm64 image build (#46736)
  _Files: `.buildkite/test_areas/lm_eval.yaml`_
- **2026-06-25** [`6f3da461d1`](https://github.com/vllm-project/vllm/commit/6f3da461d1) [#46093](https://github.com/vllm-project/vllm/pull/46093)
  [Pooling] Fix Cohere embed billed image token accounting for mixed-content inputs (#46093)
  _Files: `vllm/entrypoints/pooling/embed/serving.py`_
- **2026-06-24** [`62890e204c`](https://github.com/vllm-project/vllm/commit/62890e204c) [#46467](https://github.com/vllm-project/vllm/pull/46467)
  Fix duplicated logging when loading a corrupt or partial video (#46467)
  _Files: `vllm/multimodal/video.py`_
- **2026-06-24** [`d4448b511d`](https://github.com/vllm-project/vllm/commit/d4448b511d) [#45973](https://github.com/vllm-project/vllm/pull/45973)
  [XPU][Docker] switch to ubuntu 24.04 as base image (#45973)
  _Files: `.buildkite/scripts/hardware_ci/run-intel-test.sh`, `docker/Dockerfile.xpu`_
- **2026-06-24** [`52fbe12283`](https://github.com/vllm-project/vllm/commit/52fbe12283) [#46543](https://github.com/vllm-project/vllm/pull/46543)
  [Perf][Multimodal] Avoid building a full timestamps list in video frame sampling (#46543)
  _Files: `vllm/multimodal/video.py`_
- **2026-06-24** [`489abadfb8`](https://github.com/vllm-project/vllm/commit/489abadfb8) [#44124](https://github.com/vllm-project/vllm/pull/44124)
  feat: support to OpenMOSS-Team (#44124)
  _Files: `docs/models/supported_models.md`, `tests/benchmarks/test_throughput_cli.py`, `tests/entrypoints/openai/chat_completion/test_chat.py`, `tests/models/multimodal/generation/test_moss_audio.py` _+7 more__
- **2026-06-23** [`83fa302ca4`](https://github.com/vllm-project/vllm/commit/83fa302ca4) [#46463](https://github.com/vllm-project/vllm/pull/46463)
  fix(security): prevent infinite loop in split_audio with NaN audio sa… (#46463)
  _Files: `tests/multimodal/test_audio.py`, `vllm/multimodal/audio.py`_
- **2026-06-23** [`a8481be7a9`](https://github.com/vllm-project/vllm/commit/a8481be7a9) [#46051](https://github.com/vllm-project/vllm/pull/46051)
  [Rust Frontend][Perf] Use dedicated runtime for HTTP/request-processing/ZMQ (#46051)
  _Files: `rust/src/chat/src/multimodal.rs`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/error.rs` _+9 more__
- **2026-06-22** [`6cc2c9ba3a`](https://github.com/vllm-project/vllm/commit/6cc2c9ba3a) [#39541](https://github.com/vllm-project/vllm/pull/39541)
  [CI] Add DGX Spark GPQA smoke test (#39541)
  _Files: `.buildkite/image_build/image_build_arm64.sh`, `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-sm120.yaml`, `tests/evals/gpt_oss/configs/models-spark.txt`_
- **2026-06-22** [`b529bfd6c5`](https://github.com/vllm-project/vllm/commit/b529bfd6c5) [#45768](https://github.com/vllm-project/vllm/pull/45768)
  [XPU][CI] Add agent_tags for Intel GPU CI (#45768)
  _Files: `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/intel_jobs/basic_correctness.yaml`, `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/expert_parallelism_intel.yaml` _+6 more__

## Models  (14 commits)

- **2026-06-29** [`eddfd4cf21`](https://github.com/vllm-project/vllm/commit/eddfd4cf21) [#46750](https://github.com/vllm-project/vllm/pull/46750)
  [Perf][2/N] Expand Triton kernel warmup coverage, Qwen (#46750)
  _Files: `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/model_executor/warmup/qwen_triton_warmup.py`_
- **2026-06-29** [`ab132ee98b`](https://github.com/vllm-project/vllm/commit/ab132ee98b) [#46567](https://github.com/vllm-project/vllm/pull/46567)
  Fix model info cache for package models (#46567)
  _Files: `tests/models/test_registry.py`, `vllm/model_executor/models/registry.py`_
- **2026-06-29** [`0e207dac78`](https://github.com/vllm-project/vllm/commit/0e207dac78) [#46835](https://github.com/vllm-project/vllm/pull/46835)
  [Bugfix] Transformers backend: apply learned lm_head.bias for tied-embedding models (#46835)
  _Files: `vllm/model_executor/layers/vocab_parallel_embedding.py`, `vllm/model_executor/models/transformers/base.py`, `vllm/model_executor/models/transformers/causal.py`_
- **2026-06-28** [`6eb63a1da6`](https://github.com/vllm-project/vllm/commit/6eb63a1da6) [#46600](https://github.com/vllm-project/vllm/pull/46600)
  [Bugfix][DSv3.2] Skip indexer weights for index-cache-skipped layers (#46600)
  _Files: `vllm/model_executor/models/deepseek_v2.py`_
- **2026-06-27** [`d706dec904`](https://github.com/vllm-project/vllm/commit/d706dec904) [#44551](https://github.com/vllm-project/vllm/pull/44551)
  fix: Correct reasoning-end detection for prompt history (#44551)
  _Files: `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `tests/reasoning/test_cohere_command_reasoning_parser.py`, `vllm/reasoning/cohere_command_reasoning_parser.py`_
- **2026-06-27** [`c6dd32a810`](https://github.com/vllm-project/vllm/commit/c6dd32a810) [#46762](https://github.com/vllm-project/vllm/pull/46762)
  [ModelRunner V2] Support realtime embeddings (#46762)
  _Files: `tests/v1/worker/test_encoder_runner.py`, `vllm/model_executor/models/diffusion_gemma.py`, `vllm/v1/worker/gpu/mm/encoder_runner.py`, `vllm/v1/worker/gpu/model_runner.py` _+2 more__
- **2026-06-26** [`b94f212e37`](https://github.com/vllm-project/vllm/commit/b94f212e37) [#46776](https://github.com/vllm-project/vllm/pull/46776)
  [ModelRunner V2] Deduplicate ModelState init logic (#46776)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`, `vllm/v1/worker/gpu/model_states/default.py`, `vllm/v1/worker/gpu/model_states/encoder_decoder.py`, `vllm/v1/worker/gpu/model_states/interface.py`_
- **2026-06-25** [`72adb20a6a`](https://github.com/vllm-project/vllm/commit/72adb20a6a) [#46605](https://github.com/vllm-project/vllm/pull/46605)
  [Model] Remove AquilaForCausalLM, AquilaModel (#46605)
  _Files: `docs/models/supported_models.md`, `tests/distributed/test_pipeline_parallel.py`, `tests/models/registry.py`, `vllm/model_executor/models/registry.py`_
- **2026-06-24** [`84c62e1cbd`](https://github.com/vllm-project/vllm/commit/84c62e1cbd) [#46535](https://github.com/vllm-project/vllm/pull/46535)
  [Model Runner V2][MM] Support EVS (#46535)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen3_vl.py` _+6 more__
- **2026-06-24** [`4cd1a84c88`](https://github.com/vllm-project/vllm/commit/4cd1a84c88) [#46362](https://github.com/vllm-project/vllm/pull/46362)
  [Model] Remove BaiChuanForCausalLM and BaichuanForCausalLM (#46362)
  _Files: `docs/models/hardware_supported_models/xpu.md`, `docs/models/supported_models.md`, `examples/template_baichuan.jinja`, `rust/src/chat/src/renderer/hf/format.rs` _+6 more__
- **2026-06-24** [`ac1fa74616`](https://github.com/vllm-project/vllm/commit/ac1fa74616) [#46495](https://github.com/vllm-project/vllm/pull/46495)
  [Bugfix] Fix NemotronLayerNorm1P hardcoded cuda device type (#46495)
  _Files: `vllm/model_executor/models/nemotron.py`_
- **2026-06-23** [`40e5522121`](https://github.com/vllm-project/vllm/commit/40e5522121) [#46197](https://github.com/vllm-project/vllm/pull/46197)
  [Docs] Add Qwen3 forced alignment online example (#46197)
  _Files: `examples/pooling/token_classify/forced_alignment_online.py`_
- **2026-06-23** [`901a3b091c`](https://github.com/vllm-project/vllm/commit/901a3b091c) [#46441](https://github.com/vllm-project/vllm/pull/46441)
  fix gpt_oss pp>1 with ep (#46441)
  _Files: `vllm/model_executor/models/gpt_oss.py`_
- **2026-06-22** [`435f82d61a`](https://github.com/vllm-project/vllm/commit/435f82d61a) [#46341](https://github.com/vllm-project/vllm/pull/46341)
  [Bugfix] Fix Llama4ForCausalLM initialization test failure (#46341)
  _Files: `tests/models/utils.py`_

## Serving / API  (14 commits)

- **2026-06-29** [`9e86352c60`](https://github.com/vllm-project/vllm/commit/9e86352c60) [#47011](https://github.com/vllm-project/vllm/pull/47011)
  [CI Failure] Add transformers version check for openai/privacy-filter (#47011)
  _Files: `tests/models/language/pooling/test_token_classification.py`_
- **2026-06-27** [`8bf064f8d3`](https://github.com/vllm-project/vllm/commit/8bf064f8d3) [#46782](https://github.com/vllm-project/vllm/pull/46782)
  Fixed chunked embedding aggregation with request-id metadata (#46782)
  _Files: `tests/entrypoints/pooling/embed/test_io_processor.py`, `vllm/entrypoints/pooling/embed/io_processor.py`, `vllm/entrypoints/pooling/typing.py`_
- **2026-06-27** [`455f25aa13`](https://github.com/vllm-project/vllm/commit/455f25aa13) [#46775](https://github.com/vllm-project/vllm/pull/46775)
  [CLI] Add flag to print TTFT and TPS in `vllm chat` (#46775)
  _Files: `docs/cli/README.md`, `vllm/entrypoints/cli/openai.py`_
- **2026-06-26** [`dccb412e2c`](https://github.com/vllm-project/vllm/commit/dccb412e2c) [#46843](https://github.com/vllm-project/vllm/pull/46843)
  [Bugfix][Parser] Pass token IDs to parser.parse() in Responses API and batch serving (#46843)
  _Files: `vllm/entrypoints/openai/chat_completion/batch_serving.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/serving.py`_
- **2026-06-26** [`d350fa8ddd`](https://github.com/vllm-project/vllm/commit/d350fa8ddd) [#46733](https://github.com/vllm-project/vllm/pull/46733)
  [Bugfix][Rust Frontend] Reject min_tokens above max_tokens (#46733)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/server/src/error.rs`, `rust/src/server/src/grpc/mod.rs`, `rust/src/server/src/grpc/tests.rs` _+2 more__
- **2026-06-24** [`e48f2aa4ca`](https://github.com/vllm-project/vllm/commit/e48f2aa4ca) [#46525](https://github.com/vllm-project/vllm/pull/46525)
  [Bugfix][Frontend] Emit a content block for empty Anthropic completions (#46525)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-06-23** [`3cc871aaf1`](https://github.com/vllm-project/vllm/commit/3cc871aaf1) [#46422](https://github.com/vllm-project/vllm/pull/46422)
  [Perf] Skip detokenization in online beam search (#46422)
  _Files: `vllm/entrypoints/generate/beam_search/online.py`_
- **2026-06-23** [`275b43183c`](https://github.com/vllm-project/vllm/commit/275b43183c) [#39896](https://github.com/vllm-project/vllm/pull/39896)
  [MyPy] Fix mypy for `vllm/benchmarks` (#39896)
  _Files: `tools/pre_commit/mypy.py`, `vllm/benchmarks/datasets/create_txt_slices_dataset.py`, `vllm/benchmarks/datasets/datasets.py`, `vllm/benchmarks/latency.py` _+20 more__
- **2026-06-23** [`f59db63732`](https://github.com/vllm-project/vllm/commit/f59db63732) [#45048](https://github.com/vllm-project/vllm/pull/45048)
  [Bugfix] GPT-OSS Autodrop reasoning in Response API and cleanup (#45048)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/parser/test_harmony_render_parity.py`, `vllm/entrypoints/openai/parser/harmony_utils.py`, `vllm/entrypoints/openai/responses/harmony.py` _+1 more__
- **2026-06-23** [`1bf149f334`](https://github.com/vllm-project/vllm/commit/1bf149f334) [#46457](https://github.com/vllm-project/vllm/pull/46457)
  Filter Pydantic-internal markers from validation error param (#46457)
  _Files: `tests/entrypoints/serve/utils/test_server_utils.py`, `vllm/entrypoints/serve/utils/server_utils.py`_
- **2026-06-23** [`2a675a7b9f`](https://github.com/vllm-project/vllm/commit/2a675a7b9f) [#44361](https://github.com/vllm-project/vllm/pull/44361)
  [Bugfix] Responses API assistant EasyInputMessageParam input (#44361)
  _Files: `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/responses/test_responses_utils.py`, `vllm/entrypoints/openai/responses/protocol.py`, `vllm/entrypoints/openai/responses/utils.py`_
- **2026-06-23** [`accaa434f3`](https://github.com/vllm-project/vllm/commit/accaa434f3) [#46219](https://github.com/vllm-project/vllm/pull/46219)
  [Rust Frontend]  Support echo for token-ID completion prompts (#46219)
  _Files: `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/completions/convert.rs`, `rust/src/server/src/routes/openai/completions/validate.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-06-23** [`3ce5823762`](https://github.com/vllm-project/vllm/commit/3ce5823762) [#46030](https://github.com/vllm-project/vllm/pull/46030)
  [Refactor] Responses API parser state into conversation context (#46030)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/serving.py`_
- **2026-06-22** [`f2069b005b`](https://github.com/vllm-project/vllm/commit/f2069b005b) [#46119](https://github.com/vllm-project/vllm/pull/46119)
  [Pooling] Validate non-negative rerank top_n (#46119)
  _Files: `vllm/entrypoints/pooling/scoring/protocol.py`_

## Quantization  (14 commits)

- **2026-06-29** [`5051698e41`](https://github.com/vllm-project/vllm/commit/5051698e41) [#44589](https://github.com/vllm-project/vllm/pull/44589)
  Remove unnecessary `load_weights` methods (#44589)
  _Files: `tests/model_executor/test_weight_utils.py`, `vllm/lora/worker_manager.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/base_config.py` _+50 more__
- **2026-06-27** [`ea2ead1db3`](https://github.com/vllm-project/vllm/commit/ea2ead1db3) [#46818](https://github.com/vllm-project/vllm/pull/46818)
  [Misc] Fix incorrect layer type annotation in Fp8LinearMethod (#46818)
  _Files: `vllm/model_executor/layers/quantization/fp8.py`_
- **2026-06-27** [`b588f66dc2`](https://github.com/vllm-project/vllm/commit/b588f66dc2) [#46862](https://github.com/vllm-project/vllm/pull/46862)
  [GLM5.2 Perf] `fused_indexer_q_rope_quant` triton kernel, 1.9% ~ 3.3% E2E Throughput improvement. (#46862)
  _Files: `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/model_executor/models/deepseek_v2.py`_
- **2026-06-26** [`701a23d99f`](https://github.com/vllm-project/vllm/commit/701a23d99f) [#45719](https://github.com/vllm-project/vllm/pull/45719)
  [Bugfix][Model] Support tensor parallelism for DiffusionGemma (#45719) (#46177)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/DiffusionGemma-26B-A4B-it-FP8-dynamic.yaml`, `tests/evals/gsm8k/configs/models-small-tp.txt`, `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-06-26** [`ad28d605e6`](https://github.com/vllm-project/vllm/commit/ad28d605e6) [#45544](https://github.com/vllm-project/vllm/pull/45544)
  [Bugfix] Default tie_weights to sharing the weight (fix tied quantized embeddings, e.g. ModelOpt Gemma4) (#45544)
  _Files: `vllm/model_executor/layers/quantization/base_config.py`_
- **2026-06-25** [`e45b279928`](https://github.com/vllm-project/vllm/commit/e45b279928) [#46316](https://github.com/vllm-project/vllm/pull/46316)
  [Bugfix] Fix NVFP4+MTP crash: force unquantized mtp.fc for Qwen3Next (#46316)
  _Files: `vllm/model_executor/models/qwen3_next_mtp.py`_
- **2026-06-25** [`638b1a99cc`](https://github.com/vllm-project/vllm/commit/638b1a99cc) [#45269](https://github.com/vllm-project/vllm/pull/45269)
  [CPU][RISC-V] Add RVV path for W4A8 INT4 GEMM (#45269)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_riscv_defs.hpp`, `csrc/cpu/sgl-kernels/gemm_int4.cpp`, `csrc/cpu/sgl-kernels/vec.h` _+1 more__
- **2026-06-25** [`23aed9b0ee`](https://github.com/vllm-project/vllm/commit/23aed9b0ee) [#46508](https://github.com/vllm-project/vllm/pull/46508)
  [Kernel] Enable PDL for per_token_group_quant_8bit_kernel (#46508)
  _Files: `csrc/libtorch_stable/quantization/w8a8/fp8/per_token_group_quant.cu`_
- **2026-06-24** [`56ca5997ea`](https://github.com/vllm-project/vllm/commit/56ca5997ea) [#46389](https://github.com/vllm-project/vllm/pull/46389)
  Humming support for 2/3/5/6/7-bit pack-quantized weight-only inference (#46389)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/__init__.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `vllm/scalar_type.py`_
- **2026-06-23** [`547d2c40d7`](https://github.com/vllm-project/vllm/commit/547d2c40d7) [#44763](https://github.com/vllm-project/vllm/pull/44763)
  Add weights padding for fp8 per-block online quantization (#44763)
  _Files: `vllm/model_executor/layers/quantization/online/fp8.py`_
- **2026-06-23** [`33f50773cb`](https://github.com/vllm-project/vllm/commit/33f50773cb) [#46398](https://github.com/vllm-project/vllm/pull/46398)
  [Doc] Fix typos, grammar, and broken commands across docs (#46398)
  _Files: `docs/benchmarking/cli.md`, `docs/configuration/optimization.md`, `docs/design/cuda_graphs.md`, `docs/design/metrics.md` _+7 more__
- **2026-06-22** [`6ead164e52`](https://github.com/vllm-project/vllm/commit/6ead164e52) [#46161](https://github.com/vllm-project/vllm/pull/46161)
  [CI] Add TP=4 requirement to `test_mixed_precision_model_accuracies` (#46161)
  _Files: `tests/quantization/test_mixed_precision.py`_
- **2026-06-22** [`e4b3da3feb`](https://github.com/vllm-project/vllm/commit/e4b3da3feb) [#43752](https://github.com/vllm-project/vllm/pull/43752)
  [Quantization][CI] add humming lm-eval test (#43752)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `requirements/cuda.txt`, `tests/evals/gsm8k/configs/humming/Qwen3-30B-A3B-MXFP4A16-humming-act-fp8.yaml`, `tests/evals/gsm8k/configs/humming/Qwen3-30B-A3B-MXFP4A16-humming.yaml` _+5 more__
- **2026-06-22** [`3da4a1b124`](https://github.com/vllm-project/vllm/commit/3da4a1b124) [#43404](https://github.com/vllm-project/vllm/pull/43404)
  [XPU] add awq format for INCXPULinear (#43404)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_linear.py`_

## CI / Build  (14 commits)

- **2026-06-27** [`2e058851d3`](https://github.com/vllm-project/vllm/commit/2e058851d3) [#44984](https://github.com/vllm-project/vllm/pull/44984)
  fix(docker): eliminate race conditions in shared buildkit cache mounts (#44984)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.nightly_torch`, `docker/Dockerfile.xpu`_
- **2026-06-26** [`3f67477497`](https://github.com/vllm-project/vllm/commit/3f67477497) [#46854](https://github.com/vllm-project/vllm/pull/46854)
  [CI] Don't try and download files that we already know don't exist (#46854)
  _Files: `tests/transformers_utils/test_repo_utils.py`, `vllm/transformers_utils/config.py`, `vllm/transformers_utils/repo_utils.py`_
- **2026-06-26** [`75fdcc82a5`](https://github.com/vllm-project/vllm/commit/75fdcc82a5) [#46873](https://github.com/vllm-project/vllm/pull/46873)
  [CI] Add @ivanium to CODEOWNERS for KV-cache/offload areas (#46873)
  _Files: `.github/CODEOWNERS`_
- **2026-06-26** [`dbc49b6b99`](https://github.com/vllm-project/vllm/commit/dbc49b6b99) [#45166](https://github.com/vllm-project/vllm/pull/45166)
  [CI][NIXL] Fix NIXL EP import canary for the nixl 1.3.0 wheel and pin nixl==1.3.0 (#45166)
  _Files: `requirements/kv_connectors.txt`, `tests/v1/kv_connector/nixl_integration/test_nixl_imports.py`_
- **2026-06-26** [`ae7c8ec223`](https://github.com/vllm-project/vllm/commit/ae7c8ec223) [#46696](https://github.com/vllm-project/vllm/pull/46696)
  [Rust Frontend] Switch `rustls` to `native-tls`/OpenSSL (#46696)
  _Files: `.buildkite/scripts/run-rust-frontend-cargo-ci.sh`, `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/deny.toml` _+4 more__
- **2026-06-25** [`d3130d878c`](https://github.com/vllm-project/vllm/commit/d3130d878c) [#38290](https://github.com/vllm-project/vllm/pull/38290)
  [CI] Pin GitHub Actions to commit hashes in macos-smoke-test.yml (#38290)
  _Files: `.github/workflows/macos-smoke-test.yml`_
- **2026-06-25** [`92221485aa`](https://github.com/vllm-project/vllm/commit/92221485aa) [#46702](https://github.com/vllm-project/vllm/pull/46702)
  [CPU][CI/Build] Allow more CPU CI agents  (#46702)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test.sh`_
- **2026-06-25** [`a6f41ab678`](https://github.com/vllm-project/vllm/commit/a6f41ab678) [#46674](https://github.com/vllm-project/vllm/pull/46674)
  [XPU][CI]Refine .buildkite/ci_config_intel.yaml for Intel GPU CI (#46674)
  _Files: `.buildkite/ci_config_intel.yaml`_
- **2026-06-24** [`563c628968`](https://github.com/vllm-project/vllm/commit/563c628968) [#46607](https://github.com/vllm-project/vllm/pull/46607)
  [XPU] bump up vllm_xpu_kernels to v0.1.10.1 (#46607)
  _Files: `requirements/xpu.txt`_
- **2026-06-24** [`556bc4e3a0`](https://github.com/vllm-project/vllm/commit/556bc4e3a0) [#46568](https://github.com/vllm-project/vllm/pull/46568)
  Upgrade tpu-inference to v0.23.0 (#46568)
  _Files: `requirements/tpu.txt`_
- **2026-06-23** [`fa36f86d77`](https://github.com/vllm-project/vllm/commit/fa36f86d77) [#45772](https://github.com/vllm-project/vllm/pull/45772)
  [CI] Torch 2.11 flaky test_spec_decode_logprobs and gritlm tests (#45772)
  _Files: `tests/models/language/pooling/test_gritlm.py`, `tests/v1/sample/test_logprobs.py`_
- **2026-06-22** [`e2fe837572`](https://github.com/vllm-project/vllm/commit/e2fe837572) [#46388](https://github.com/vllm-project/vllm/pull/46388)
  [CI] Fix CPU-Multi-Modal Model Tests timeout by adding a 4th shard (#46388)
  _Files: `.buildkite/hardware_tests/cpu.yaml`_
- **2026-06-22** [`09cdcf34aa`](https://github.com/vllm-project/vllm/commit/09cdcf34aa) [#46327](https://github.com/vllm-project/vllm/pull/46327)
  [XPU] update nixl to v1.2.0 (#46327)
  _Files: `docker/Dockerfile.xpu`_
- **2026-06-22** [`b5a2adec4b`](https://github.com/vllm-project/vllm/commit/b5a2adec4b) [#46356](https://github.com/vllm-project/vllm/pull/46356)
  [XPU][CI]Skip v1/spec_decode/test_speculators_correctness.py in intel GPU nightly (#46356)
  _Files: `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_

## KV Cache / Offload  (12 commits)

- **2026-06-25** [`1aad125815`](https://github.com/vllm-project/vllm/commit/1aad125815) [#46202](https://github.com/vllm-project/vllm/pull/46202)
  [CPU] Enable chunked prefill and prefix caching for qwen3.5 (#46202)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `csrc/cpu/sgl-kernels/conv.cpp`, `tests/kernels/mamba/cpu/test_cpu_gdn_ops.py`, `tests/v1/e2e/test_cpu_linear_attn_chunked_prefix.py` _+3 more__
- **2026-06-24** [`e7df232288`](https://github.com/vllm-project/vllm/commit/e7df232288) [#46252](https://github.com/vllm-project/vllm/pull/46252)
  [KV Offload] Gate packed HMA KV cache on cross-layer config (#46252)
  _Files: `tests/v1/core/test_contiguous_kv_packing.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py`, `vllm/envs.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-06-24** [`f889325c51`](https://github.com/vllm-project/vllm/commit/f889325c51) [#45850](https://github.com/vllm-project/vllm/pull/45850)
  [KV Offload] Use background thread for mmap / cpu_tensors pinning (#45850)
  _Files: `vllm/v1/kv_offload/cpu/gpu_worker.py`_
- **2026-06-24** [`bb61177e49`](https://github.com/vllm-project/vllm/commit/bb61177e49) [#46363](https://github.com/vllm-project/vllm/pull/46363)
  [KV Offloading] Replace `bool|None` lookup return with LookupResult enum (#46363)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_offload/cpu/test_manager.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py` _+10 more__
- **2026-06-24** [`cf9fd6457e`](https://github.com/vllm-project/vllm/commit/cf9fd6457e) [#46284](https://github.com/vllm-project/vllm/pull/46284)
  Fix KV offload request-finished lifecycle contract (#46284)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/v1/kv_offload/base.py` _+1 more__
- **2026-06-24** [`f237e16b41`](https://github.com/vllm-project/vllm/commit/f237e16b41) [#45053](https://github.com/vllm-project/vllm/pull/45053)
  [KV Offload] Replace OffloadingHandler with OffloadingWorker (#45053)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_offload/cpu/test_gpu_worker.py`, `tests/v1/kv_offload/test_worker.py` _+9 more__
- **2026-06-24** [`d20dbf921b`](https://github.com/vllm-project/vllm/commit/d20dbf921b) [#46412](https://github.com/vllm-project/vllm/pull/46412)
  [Mooncake] Only check and store new KV cache range (#46412)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py` _+2 more__
- **2026-06-23** [`7d47cff933`](https://github.com/vllm-project/vllm/commit/7d47cff933) [#46379](https://github.com/vllm-project/vllm/pull/46379)
  [Bugfix][KV Offload] Fix swap_blocks_batch on the default stream (#46379)
  _Files: `csrc/libtorch_stable/cache_kernels.cu`, `tests/v1/kv_offload/cpu/test_swap_blocks_batch.py`_
- **2026-06-23** [`091bc1026e`](https://github.com/vllm-project/vllm/commit/091bc1026e) [#45959](https://github.com/vllm-project/vllm/pull/45959)
  [KV Offloading] Add tiering metric plumbing (#45959)
  _Files: `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/base.py`, `vllm/v1/kv_offload/tiering/factory.py`, `vllm/v1/kv_offload/tiering/manager.py` _+1 more__
- **2026-06-23** [`9d3317172c`](https://github.com/vllm-project/vllm/commit/9d3317172c) [#46429](https://github.com/vllm-project/vllm/pull/46429)
  [XPU][CI]fix xpu kv cache layout test (#46429)
  _Files: `tests/v1/kv_connector/unit/test_kv_cache_layout.py`_
- **2026-06-22** [`3ce15fd574`](https://github.com/vllm-project/vllm/commit/3ce15fd574) [#45080](https://github.com/vllm-project/vllm/pull/45080)
  [v1][kvconnector] DecodeBenchConnector: fill list/tuple (Mamba/KDA) KV caches (#45080)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`_
- **2026-06-22** [`9a938df64e`](https://github.com/vllm-project/vllm/commit/9a938df64e) [#46355](https://github.com/vllm-project/vllm/pull/46355)
  [Test][KV Offloading] Add unit tests for OffloadingSpecFactory and SecondaryTierFactory (#46355)
  _Files: `tests/v1/kv_offload/__init__.py`, `tests/v1/kv_offload/test_factory.py`, `tests/v1/kv_offload/tiering/__init__.py`, `tests/v1/kv_offload/tiering/test_factory.py`_

## Disaggregation / PD  (9 commits)

- **2026-06-28** [`95528527ea`](https://github.com/vllm-project/vllm/commit/95528527ea) [#46855](https://github.com/vllm-project/vllm/pull/46855)
  [Bugfix][Mooncake] Fix Mooncake lookup prefixes with DCP > 1 (#46855)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-06-28** [`798185d438`](https://github.com/vllm-project/vllm/commit/798185d438) [#46888](https://github.com/vllm-project/vllm/pull/46888)
  [KV-Offloading] Fix tensors_per_block stride (#46888)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py`_
- **2026-06-25** [`15be78732b`](https://github.com/vllm-project/vllm/commit/15be78732b) [#45019](https://github.com/vllm-project/vllm/pull/45019)
  [NIXL][Mamba] Add Mamba1 support to NIXL P/D disaggregation (#45019)
  _Files: `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/test_accuracy.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+1 more__
- **2026-06-25** [`9e88e969c0`](https://github.com/vllm-project/vllm/commit/9e88e969c0) [#45971](https://github.com/vllm-project/vllm/pull/45971)
  [Perf][KVConnector][Mooncake] Parallelize KV load with a receive-thread pool (#45971)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`, `vllm/envs.py`_
- **2026-06-24** [`b69816043a`](https://github.com/vllm-project/vllm/commit/b69816043a) [#46595](https://github.com/vllm-project/vllm/pull/46595)
  [Bugfix][MooncakeStore] track resumed requests via scheduler's resumed_req_ids (#46595)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-06-24** [`a2cb08b3d5`](https://github.com/vllm-project/vllm/commit/a2cb08b3d5) [#46473](https://github.com/vllm-project/vllm/pull/46473)
  [Misc][PD] Disable bidirectional xfer mode for NixlPushConnector (#46473)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/nixl/push_scheduler.py`_
- **2026-06-24** [`05a0caba91`](https://github.com/vllm-project/vllm/commit/05a0caba91) [#46188](https://github.com/vllm-project/vllm/pull/46188)
  [Mooncake] Optimize lookup pool key string construction (#46188)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-06-22** [`ac614587f5`](https://github.com/vllm-project/vllm/commit/ac614587f5) [#45013](https://github.com/vllm-project/vllm/pull/45013)
  [EPLB] Enable nixl eplb communicator for elastic ep (#45013)
  _Files: `tests/distributed/test_elastic_ep.py`, `tests/distributed/test_eplb_execute.py`, `vllm/config/parallel.py`, `vllm/distributed/elastic_ep/elastic_execute.py` _+3 more__
- **2026-06-22** [`a9f7b2d41c`](https://github.com/vllm-project/vllm/commit/a9f7b2d41c) [#43468](https://github.com/vllm-project/vllm/pull/43468)
  [feature][kv_offload] Self-describing KV events for OffloadingConnector (#43468)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py` _+5 more__

## Speculative Decoding  (8 commits)

- **2026-06-29** [`0472436541`](https://github.com/vllm-project/vllm/commit/0472436541) [#46968](https://github.com/vllm-project/vllm/pull/46968)
  [Spec Decode] Avoid redundant hidden-states gather in draft prefill (#46968)
  _Files: `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`_
- **2026-06-28** [`11a12305c0`](https://github.com/vllm-project/vllm/commit/11a12305c0) [#46786](https://github.com/vllm-project/vllm/pull/46786)
  [Model Runner V2][Spec Decode] Handle tuple hidden states from MTP draft models (#46786)
  _Files: `tests/v1/worker/test_gpu_autoregressive_speculator.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`, `vllm/v1/worker/gpu/spec_decode/gemma4/speculator.py`, `vllm/v1/worker/gpu/spec_decode/mtp/speculator.py`_
- **2026-06-26** [`652d962bc9`](https://github.com/vllm-project/vllm/commit/652d962bc9) [#46448](https://github.com/vllm-project/vllm/pull/46448)
  [Model Runner V2][Spec Decode] Reduce TP communication for draft token generation (#46448)
  _Files: `vllm/v1/worker/gpu/spec_decode/speculator.py`_
- **2026-06-25** [`dda3aca47f`](https://github.com/vllm-project/vllm/commit/dda3aca47f) [#46488](https://github.com/vllm-project/vllm/pull/46488)
  [Speculative Decoding] Propagate norm_output and fc_norm config for Eagle3 speculators (#46488)
  _Files: `vllm/transformers_utils/configs/speculators/algos.py`_
- **2026-06-24** [`4c5bc41ba6`](https://github.com/vllm-project/vllm/commit/4c5bc41ba6) [#45956](https://github.com/vllm-project/vllm/pull/45956)
  [Bugfix][Spec Decode] Fix probabilistic sampling for parallel drafting (#45956)
  _Files: `tests/v1/spec_decode/test_eagle.py`, `vllm/v1/spec_decode/llm_base_proposer.py`_
- **2026-06-24** [`7ee4d22009`](https://github.com/vllm-project/vllm/commit/7ee4d22009) [#46533](https://github.com/vllm-project/vllm/pull/46533)
  [Spec Decode] Reject placeholder (-1) draft tokens in rejection sampler (#46533)
  _Files: `tests/v1/sample/test_rejection_sampler.py`, `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `vllm/v1/sample/rejection_sampler.py`, `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-06-23** [`3554ada5d8`](https://github.com/vllm-project/vllm/commit/3554ada5d8) [#46069](https://github.com/vllm-project/vllm/pull/46069)
  [CPU][Bugfix][Speculative Decoding] Accept USE_FP64_GUMBEL in CPU recovered-tokens sampler (#46069)
  _Files: `vllm/utils/cpu_triton_utils.py`_
- **2026-06-22** [`3e6529cc0e`](https://github.com/vllm-project/vllm/commit/3e6529cc0e) [#46315](https://github.com/vllm-project/vllm/pull/46315)
  [Bugfix][Spec Decode] Fix EAGLE drafter multimodal encoder cache misses (#46315)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/worker/test_encoder_runner.py`, `tests/v1/worker/test_gpu_model_runner_mm_gather.py`, `vllm/v1/core/sched/scheduler.py` _+3 more__

## LoRA  (6 commits)

- **2026-06-25** [`f9e684499f`](https://github.com/vllm-project/vllm/commit/f9e684499f) [#46602](https://github.com/vllm-project/vllm/pull/46602)
  [Rust Frontend] Migrate gemma4 to unified parser (#46602)
  _Files: `pyproject.toml`, `rust/Cargo.toml`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/default/structural_tag.rs` _+19 more__
- **2026-06-25** [`cd347298e8`](https://github.com/vllm-project/vllm/commit/cd347298e8) [#46314](https://github.com/vllm-project/vllm/pull/46314)
  [Frontend] Port seed_oss to the streaming parser engine as a Qwen3 subclass (#46314)
  _Files: `tests/parser/engine/test_seed_oss.py`, `tests/parser/engine/trace_builder.py`, `tests/reasoning/test_seedoss_reasoning_parser.py`, `tests/tool_parsers/test_seed_oss_tool_parser.py` _+9 more__
- **2026-06-24** [`0bc479e6eb`](https://github.com/vllm-project/vllm/commit/0bc479e6eb) [#46542](https://github.com/vllm-project/vllm/pull/46542)
  [Perf][LoRA] Replace O(n) list.index() with a dict in convert_mapping (#46542)
  _Files: `vllm/lora/punica_wrapper/utils.py`_
- **2026-06-23** [`9f6f296428`](https://github.com/vllm-project/vllm/commit/9f6f296428) [#46494](https://github.com/vllm-project/vllm/pull/46494)
  [CI/Build] Remove BaiChuanForCausalLM from the LoRA test (#46494)
  _Files: `tests/lora/test_lora_checkpoints.py`_
- **2026-06-23** [`e51e700470`](https://github.com/vllm-project/vllm/commit/e51e700470) [#45715](https://github.com/vllm-project/vllm/pull/45715)
  [LoRA] Gate all_gather on fully_sharded_loras inside _mcp_apply; rewrite regression test (#45715)
  _Files: `vllm/lora/layers/column_parallel_linear.py`_
- **2026-06-23** [`31ca9504b1`](https://github.com/vllm-project/vllm/commit/31ca9504b1) [#44285](https://github.com/vllm-project/vllm/pull/44285)
  [Frontend] Split ServingRender into renderer and entrypoint. (#44285)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat_error.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/completion/test_completion_error.py`, `tests/entrypoints/openai/completion/test_lora_resolvers.py` _+22 more__

## Docs  (5 commits)

- **2026-06-26** [`bf292b5f6b`](https://github.com/vllm-project/vllm/commit/bf292b5f6b) [#46071](https://github.com/vllm-project/vllm/pull/46071)
  [Docs] Remove BambaForCausalLM from supported hybrid models list (#46071)
  _Files: `docs/usage/v1_guide.md`_
- **2026-06-26** [`5e3dad04b1`](https://github.com/vllm-project/vllm/commit/5e3dad04b1) [#46783](https://github.com/vllm-project/vllm/pull/46783)
  [Misc] Move the legacy api_server.py to the examples directory. (#46783)
  _Files: `docs/design/arch_overview.md`, `docs/examples/README.md`, `examples/applications/api_server/client.py`, `examples/applications/api_server/server.py` _+1 more__
- **2026-06-23** [`a04654da23`](https://github.com/vllm-project/vllm/commit/a04654da23) [#46452](https://github.com/vllm-project/vllm/pull/46452)
  Doc: fix missing GLM-5.x in supported models (#46452)
  _Files: `docs/models/supported_models.md`_
- **2026-06-22** [`6871738777`](https://github.com/vllm-project/vllm/commit/6871738777) [#46376](https://github.com/vllm-project/vllm/pull/46376)
  [Doc] Document pull request limit (#46376)
  _Files: `docs/contributing/README.md`_
- **2026-06-22** [`2e2c47928b`](https://github.com/vllm-project/vllm/commit/2e2c47928b) [#45940](https://github.com/vllm-project/vllm/pull/45940)
  [Doc] Update MiniMax-M3  (#45940)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`_

## Compilation / CUDA Graph  (1 commits)

- **2026-06-26** [`4e07ca2c92`](https://github.com/vllm-project/vllm/commit/4e07ca2c92) [#44800](https://github.com/vllm-project/vllm/pull/44800)
  [Core] Add `VLLM_GPU_SYNC_CHECK` env var (#44800)
  _Files: `tests/utils_/test_gpu_sync_debug.py`, `vllm/compilation/compiler_interface.py`, `vllm/envs.py`, `vllm/utils/gpu_sync_debug.py` _+1 more__

## Distributed  (1 commits)

- **2026-06-26** [`cc7981599e`](https://github.com/vllm-project/vllm/commit/cc7981599e) [#46405](https://github.com/vllm-project/vllm/pull/46405)
  [Refactor] Remove dead kernel code (#46405)
  _Files: `csrc/custom_all_reduce_test.cu`, `csrc/ops.h`, `vllm/_custom_ops.py`_

## Perf / Benchmark  (1 commits)

- **2026-06-24** [`7f99e80c3b`](https://github.com/vllm-project/vllm/commit/7f99e80c3b) [#46425](https://github.com/vllm-project/vllm/pull/46425)
  [Perf][ThinkingBudget] reduce search space for thinking tokens (#46425)
  _Files: `tests/v1/logits_processors/test_correctness.py`, `vllm/v1/sample/thinking_budget_state.py`_

---
_Generated 2026-06-29 12:44 UTC_