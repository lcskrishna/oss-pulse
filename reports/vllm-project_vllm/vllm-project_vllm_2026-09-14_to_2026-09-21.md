# vllm-project/vllm — Weekly Change Report
**Period:** 2026-09-14 → 2026-09-21  |  **Total commits:** 446

## ✨ New Features This Week

- **2026-09-21** [#52362](https://github.com/vllm-project/vllm/pull/52362) — [ROCm][DSv4] Enable DSpark adaptive verification (#52362)
- **2026-09-21** [#57913](https://github.com/vllm-project/vllm/pull/57913) — [MM] Move `supports_multimodal_inputs` and cache out of registry (#57913)
- **2026-09-21** [#57922](https://github.com/vllm-project/vllm/pull/57922) — [Frontend] Add streaming parity tests and docs for derender (#57922)
- **2026-09-21** [#57876](https://github.com/vllm-project/vllm/pull/57876) — [CI][ROCm] Add ten AMD parity groups (#57876)
- **2026-09-21** [#45635](https://github.com/vllm-project/vllm/pull/45635) — [AuxOutput] Add block-keyed storage for routed-expert outputs (#45635)
- **2026-09-21** [#54535](https://github.com/vllm-project/vllm/pull/54535) — [AMD][Minimax-M3][perf] Enable packed LBHNC AITER QK-norm fusion for MiniMax-M3 on ROCm (#54535)
- **2026-09-21** [#57526](https://github.com/vllm-project/vllm/pull/57526) — [Perf][ROCm] Add a ROCm path for Hy4 and compile the backbone (#57526)
- **2026-09-21** [#57742](https://github.com/vllm-project/vllm/pull/57742) — [Docs] Add ECMooncakeConnector usage example for EPD (#57742)
- **2026-09-20** [#56685](https://github.com/vllm-project/vllm/pull/56685) — [Feature][Humming] Humming feature integration (#56685)
- **2026-09-20** [#56625](https://github.com/vllm-project/vllm/pull/56625) — [DSV4.1] Add encoder cuda graph support for deepseek-v4.1-flash (#56625)
- _…and 70 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-21** [`e34685dfc0`](https://github.com/vllm-project/vllm/commit/e34685dfc0) [#52362](https://github.com/vllm-project/vllm/pull/52362) — [ROCm][DSv4] Enable DSpark adaptive verification (#52362)
- **2026-09-21** [`7488b5780f`](https://github.com/vllm-project/vllm/commit/7488b5780f) [#57869](https://github.com/vllm-project/vllm/pull/57869) — [ROCm][Tests] Reduce host memory when downcasting FP32 HF references (#57869)
- **2026-09-21** [`82daf9f575`](https://github.com/vllm-project/vllm/commit/82daf9f575) [#57876](https://github.com/vllm-project/vllm/pull/57876) — [CI][ROCm] Add ten AMD parity groups (#57876)
- **2026-09-21** [`04c1f4a407`](https://github.com/vllm-project/vllm/commit/04c1f4a407) [#57906](https://github.com/vllm-project/vllm/pull/57906) — [Bugfix][ROCm][DSv4.1] Disable SWA bounded replay on ROCm (#57906)
- **2026-09-21** [`0aee727ff6`](https://github.com/vllm-project/vllm/commit/0aee727ff6) [#57903](https://github.com/vllm-project/vllm/pull/57903) — [CI][ROCm] Increase timeout for MI300 Distributed DP Extended (#57903)
- **2026-09-21** [`8902dbb177`](https://github.com/vllm-project/vllm/commit/8902dbb177) [#57877](https://github.com/vllm-project/vllm/pull/57877) — [CI][ROCm] Mirror remaining portable suites without duplicate coverage (#57877)
- **2026-09-21** [`b8cf275382`](https://github.com/vllm-project/vllm/commit/b8cf275382) [#54535](https://github.com/vllm-project/vllm/pull/54535) — [AMD][Minimax-M3][perf] Enable packed LBHNC AITER QK-norm fusion for MiniMax-M3 on ROCm (#54535)
- **2026-09-21** [`f05b88751e`](https://github.com/vllm-project/vllm/commit/f05b88751e) [#57870](https://github.com/vllm-project/vllm/pull/57870) — [CI][ROCm] Make Python-only installation failures blocking (#57870)
- **2026-09-21** [`0ff0477ff9`](https://github.com/vllm-project/vllm/commit/0ff0477ff9) [#57526](https://github.com/vllm-project/vllm/pull/57526) — [Perf][ROCm] Add a ROCm path for Hy4 and compile the backbone (#57526)
- **2026-09-21** [`76ee20c1ec`](https://github.com/vllm-project/vllm/commit/76ee20c1ec) [#57864](https://github.com/vllm-project/vllm/pull/57864) — [ROCm][Tests] Avoid pooling cleanup waits against live shared engines (#57864)
- **2026-09-21** [`6dfd87f596`](https://github.com/vllm-project/vllm/commit/6dfd87f596) [#57491](https://github.com/vllm-project/vllm/pull/57491) — [ROCm][DSv4.1] Keep the Engram tables in host memory on ROCm (#57491)
- **2026-09-20** [`9679173788`](https://github.com/vllm-project/vllm/commit/9679173788) [#51052](https://github.com/vllm-project/vllm/pull/51052) — [KVConnector][MoRIIO] Transfer hybrid mamba/KDA recurrent state in READ mode (#51052)
- **2026-09-20** [`01f1f58f10`](https://github.com/vllm-project/vllm/commit/01f1f58f10) [#57450](https://github.com/vllm-project/vllm/pull/57450) — [ROCm][CI] Query HIP device memory for test GPU teardown waits. (#57450)
- **2026-09-20** [`4868312128`](https://github.com/vllm-project/vllm/commit/4868312128) [#57621](https://github.com/vllm-project/vllm/pull/57621) — [Refactor] Remove dead kernel code (#57621)
- **2026-09-20** [`27757dde02`](https://github.com/vllm-project/vllm/commit/27757dde02) [#56625](https://github.com/vllm-project/vllm/pull/56625) — [DSV4.1] Add encoder cuda graph support for deepseek-v4.1-flash (#56625)
- **2026-09-20** [`0e110f696d`](https://github.com/vllm-project/vllm/commit/0e110f696d) [#54894](https://github.com/vllm-project/vllm/pull/54894) — [ROCm][DSV4][Perf] Use FP8 WO_A output projection (#54894)
- **2026-09-20** [`1596fa5f88`](https://github.com/vllm-project/vllm/commit/1596fa5f88) [#57434](https://github.com/vllm-project/vllm/pull/57434) — [ROCm][DSv4.1][Perf] Reuse the decode topk ragged metadata across layers (#57434)
- **2026-09-19** [`36fa72d2d0`](https://github.com/vllm-project/vllm/commit/36fa72d2d0) [#57701](https://github.com/vllm-project/vllm/pull/57701) — [GLM5.3 Perf] Size the GLM-5 sparse indexer decode workspace, 3072 MiB GPU memory saved (#57701)
- **2026-09-19** [`fbe8a157fb`](https://github.com/vllm-project/vllm/commit/fbe8a157fb) [#53623](https://github.com/vllm-project/vllm/pull/53623) — [ROCm][Perf] Enable the AITER GDN decode fast path for flat qkvz layouts (#53623)
- **2026-09-19** [`4cc15f2121`](https://github.com/vllm-project/vllm/commit/4cc15f2121) [#57316](https://github.com/vllm-project/vllm/pull/57316) — [Quantization] Let ModelOpt MXFP8 layers load pre-processed weights  Purpose (#57316)
- **2026-09-19** [`59e6682c21`](https://github.com/vllm-project/vllm/commit/59e6682c21) [#53009](https://github.com/vllm-project/vllm/pull/53009) — [CI][AMD] Bump torchao to v18 for Python 3.14 (#53009)
- **2026-09-19** [`468663a5e5`](https://github.com/vllm-project/vllm/commit/468663a5e5) [#56885](https://github.com/vllm-project/vllm/pull/56885) — [ROCm] Bump AITER to v0.1.22.post1 (#56885)
- **2026-09-18** [`1dc2d854c1`](https://github.com/vllm-project/vllm/commit/1dc2d854c1) [#56227](https://github.com/vllm-project/vllm/pull/56227) — [Feat][Model] Support encoder-side SWA-bounded replay for DeepSeek-V4.1-Flash (#56227)
- **2026-09-18** [`0390299309`](https://github.com/vllm-project/vllm/commit/0390299309) [#57583](https://github.com/vllm-project/vllm/pull/57583) — [ROCm][CI] Shard MI300 Entrypoints Integration (Pooling) (#57583)
- **2026-09-18** [`2c3fb4c545`](https://github.com/vllm-project/vllm/commit/2c3fb4c545) [#56162](https://github.com/vllm-project/vllm/pull/56162) — [CI][ROCm] Deprecate DinD for MI250 test groups (#56162)
- **2026-09-18** [`71fc70d3ae`](https://github.com/vllm-project/vllm/commit/71fc70d3ae) [#50455](https://github.com/vllm-project/vllm/pull/50455) — [ROCm][DSv4] Fix sparse-indexer logits collapse on gfx950/gfx942 (#50455)
- **2026-09-18** [`c58532c86b`](https://github.com/vllm-project/vllm/commit/c58532c86b) [#57272](https://github.com/vllm-project/vllm/pull/57272) — [Frontend] Upgrade XGrammar to 0.2.7 and Rust structural tags to 0.3.0 (#57272)
- **2026-09-18** [`4c6c1a40b3`](https://github.com/vllm-project/vllm/commit/4c6c1a40b3) [#57328](https://github.com/vllm-project/vllm/pull/57328) — [ROCm][Bugfix] Fix intermittent ROCR host segfault (#57328)
- **2026-09-18** [`d12c276853`](https://github.com/vllm-project/vllm/commit/d12c276853) [#57425](https://github.com/vllm-project/vllm/pull/57425) — [Bugfix][ROCm] Alias SparseAttnIndexerKpool.forward_cuda to forward_native (GLM-5.3-Flash boot crash) (#57425)
- **2026-09-18** [`7b94293627`](https://github.com/vllm-project/vllm/commit/7b94293627) [#57160](https://github.com/vllm-project/vllm/pull/57160) — [Bugfix][ROCm][KV Offload] Use private pinned tensors for CPU KV offload (#57160)
- **2026-09-18** [`213c379fca`](https://github.com/vllm-project/vllm/commit/213c379fca) [#57426](https://github.com/vllm-project/vllm/pull/57426) — [ROCm][Bugfix] Gate AITER MXFP8 MoE on the aiter enable flag (#57426)
- **2026-09-17** [`a524f80b1f`](https://github.com/vllm-project/vllm/commit/a524f80b1f) [#57289](https://github.com/vllm-project/vllm/pull/57289) — [AMD][Bugfix] Make the nested-RoPE patch reach automatic validation (#57289)
- **2026-09-17** [`e0050f287a`](https://github.com/vllm-project/vllm/commit/e0050f287a) [#57252](https://github.com/vllm-project/vllm/pull/57252) — [Bugfix][ROCm] Add record_logical_topk_ready to ROCMAiterMLASparseImpl (GLM-5.3-Flash boot crash) (#57252)
- **2026-09-17** [`d3074acdda`](https://github.com/vllm-project/vllm/commit/d3074acdda) [#53837](https://github.com/vllm-project/vllm/pull/53837) — [AMD][CI][The Rock] Fix language models standard for The Rock on mi355 (#53837)
- **2026-09-17** [`acc2ed2a5f`](https://github.com/vllm-project/vllm/commit/acc2ed2a5f) [#54849](https://github.com/vllm-project/vllm/pull/54849) — [ROCm][CI][The Rock 10] Fix (MI355) Quantized Models failure on The Rock 10 with Triton 3.8.x (#54849)
- **2026-09-17** [`9a5bd373cf`](https://github.com/vllm-project/vllm/commit/9a5bd373cf) [#57398](https://github.com/vllm-project/vllm/pull/57398) — [CI] Retire Weight Loading smoke tests (#57398)
- **2026-09-17** [`a9a7e45f31`](https://github.com/vllm-project/vllm/commit/a9a7e45f31) [#57055](https://github.com/vllm-project/vllm/pull/57055) — [ROCm] Restore `VLLM_ROCM_USE_AITER_FP4_ASM_GEMM` and default w4a4 ASM GEMM back to off (#57055)
- **2026-09-17** [`ff6b5808c4`](https://github.com/vllm-project/vllm/commit/ff6b5808c4) [#53792](https://github.com/vllm-project/vllm/pull/53792) — [ROCm] Resolve the indexer fp8 cache dtype once at import (#53792)
- **2026-09-17** [`e30bf70c5d`](https://github.com/vllm-project/vllm/commit/e30bf70c5d) [#57380](https://github.com/vllm-project/vllm/pull/57380) — [ROCm][CI] Fix Entrypoints Integration (Pooling) tests on TheRock image (#57380)
- **2026-09-17** [`fef55fd26d`](https://github.com/vllm-project/vllm/commit/fef55fd26d) [#57385](https://github.com/vllm-project/vllm/pull/57385) — [ROCm][CI] Adapt MoE tests to the triton_kernels 3.8 API (#57385)
- **2026-09-17** [`d7e755c230`](https://github.com/vllm-project/vllm/commit/d7e755c230) [#57295](https://github.com/vllm-project/vllm/pull/57295) — [Bugfix] Fix wrong vLLM version reported by pip install (proto-v* tag collision) (#57295)
- **2026-09-17** [`1df336c3ba`](https://github.com/vllm-project/vllm/commit/1df336c3ba) [#48249](https://github.com/vllm-project/vllm/pull/48249) — [Perf][ROCm] Enable AITER QuickReduce + RMSNorm fusion (#48249)
- **2026-09-17** [`3affd35f31`](https://github.com/vllm-project/vllm/commit/3affd35f31) [#56359](https://github.com/vllm-project/vllm/pull/56359) — [Fix][ROCm] MXFP4 MoE round-up inflates TP-sharded expert weights on CDNA3, starving KV cache (#56359)
- **2026-09-17** [`438434b5b5`](https://github.com/vllm-project/vllm/commit/438434b5b5) [#56849](https://github.com/vllm-project/vllm/pull/56849) — [ROCm][Perf] Insert MiniMax-M3 sparse-PA K/V without a contiguous copy (#56849)
- **2026-09-17** [`0eae9acd4d`](https://github.com/vllm-project/vllm/commit/0eae9acd4d) [#56590](https://github.com/vllm-project/vllm/pull/56590) — [Bugfix][ROCm][MoE] Fall back instead of crashing when AITER MoE is requested for a non-gated (is_act_and_mul=False) model (#56590)
- **2026-09-17** [`8be3ca35f3`](https://github.com/vllm-project/vllm/commit/8be3ca35f3) [#57375](https://github.com/vllm-project/vllm/pull/57375) — [ROCm][CI] Fix AMD CI pipeline upload rejected by an invalid block-step key (#57375)
- **2026-09-17** [`667b26e50b`](https://github.com/vllm-project/vllm/commit/667b26e50b) [#57192](https://github.com/vllm-project/vllm/pull/57192) — [Bugfix][ROCm][GLM-5.3-Flash] Apply deferred tilelang.jit already on attribute access (#57192)
- **2026-09-17** [`f1c2f6ada8`](https://github.com/vllm-project/vllm/commit/f1c2f6ada8) [#57080](https://github.com/vllm-project/vllm/pull/57080) — [ROCm][CI] Stage H gating and MI355 test reallocation (#57080)
- **2026-09-17** [`528fa835fd`](https://github.com/vllm-project/vllm/commit/528fa835fd) [#56343](https://github.com/vllm-project/vllm/pull/56343) — [ROCm] Stage large pageable H2D copies instead of registering them (#56343)
- **2026-09-17** [`fdcd42350b`](https://github.com/vllm-project/vllm/commit/fdcd42350b) [#56853](https://github.com/vllm-project/vllm/pull/56853) — [ROCm][Perf] Enable HCA dual-stream overlap for DeepSeek-V4 (#56853)
- **2026-09-17** [`2d8a5c5741`](https://github.com/vllm-project/vllm/commit/2d8a5c5741) [#57229](https://github.com/vllm-project/vllm/pull/57229) — [ROCm][Bugfix] Reduce CUDA graph divergences (#57229)
- **2026-09-17** [`68f2c7e74f`](https://github.com/vllm-project/vllm/commit/68f2c7e74f) [#57249](https://github.com/vllm-project/vllm/pull/57249) — [ROCm][CI] Fix Nixl+Offloading PD edge cases on TheRock image (#57249)
- **2026-09-17** [`19b6ff62f2`](https://github.com/vllm-project/vllm/commit/19b6ff62f2) [#56726](https://github.com/vllm-project/vllm/pull/56726) — [ROCm][Bugfix] Ignore descales for unquantized AITER caches (#56726)
- **2026-09-17** [`3e267bae70`](https://github.com/vllm-project/vllm/commit/3e267bae70) [#55934](https://github.com/vllm-project/vllm/pull/55934) — [ROCm] triton+triton_kernels 3.8 mxfp4 MoE support (gpt-oss + DeepSeek-V4) (#55934)
- **2026-09-17** [`95f4925c3a`](https://github.com/vllm-project/vllm/commit/95f4925c3a) [#57074](https://github.com/vllm-project/vllm/pull/57074) — [ROCm][CI] Enable AITER FP8/unquantized cases in modular-kernel sweep + fix MoRI per-tensor FP8 dispatch (#57074)
- **2026-09-16** [`91b96a533c`](https://github.com/vllm-project/vllm/commit/91b96a533c) [#57056](https://github.com/vllm-project/vllm/pull/57056) — [ROCm][CI] Shard MI300 Multimodal Processor (#57056)
- **2026-09-16** [`bc0f47cd03`](https://github.com/vllm-project/vllm/commit/bc0f47cd03) [#57132](https://github.com/vllm-project/vllm/pull/57132) — [ROCm][Bugfix] Revert #56433 + #51692 to fix accuracy breakdown for DeepSeek-V4 (#57132)
- **2026-09-16** [`6ca2b23e22`](https://github.com/vllm-project/vllm/commit/6ca2b23e22) [#54248](https://github.com/vllm-project/vllm/pull/54248) — [ROCm] Expose kFp8DynamicTokenSym on AITER PTPC linears (#54248)
- **2026-09-16** [`ec4a3a5370`](https://github.com/vllm-project/vllm/commit/ec4a3a5370) [#56108](https://github.com/vllm-project/vllm/pull/56108) — [CI] Bump Transformers version to 5.17.0 (#56108)
- **2026-09-16** [`d6a1677d55`](https://github.com/vllm-project/vllm/commit/d6a1677d55) [#56935](https://github.com/vllm-project/vllm/pull/56935) — [Model][DSv4.1] FlashMLA mega attention and the NVFP4 compressed KV cache (#56935)
- **2026-09-16** [`ab35354c21`](https://github.com/vllm-project/vllm/commit/ab35354c21) [#55991](https://github.com/vllm-project/vllm/pull/55991) — [ROCm][AITER] Skip AITER norm kernels when flattening to 2D would copy (#55991)
- **2026-09-16** [`b3b13c1292`](https://github.com/vllm-project/vllm/commit/b3b13c1292) [#57112](https://github.com/vllm-project/vllm/pull/57112) — [ROCm][CI] Fix MLA RoPE fused-kernel tests for TheRock image (#57112)
- **2026-09-16** [`4fe9e6f6e5`](https://github.com/vllm-project/vllm/commit/4fe9e6f6e5) [#55358](https://github.com/vllm-project/vllm/pull/55358) — [Refactor][GLM-5.3-Flash] Move sparse_attn_indexer_kpool into the model folder and split AMD/NVIDIA (#55358)
- **2026-09-16** [`711768fc17`](https://github.com/vllm-project/vllm/commit/711768fc17) [#56351](https://github.com/vllm-project/vllm/pull/56351) — [CI][ROCm] Add opt-in TheRock builds for AMD CI (#56351)
- **2026-09-16** [`22bb158c21`](https://github.com/vllm-project/vllm/commit/22bb158c21) [#53674](https://github.com/vllm-project/vllm/pull/53674) — [Bugfix][ROCm] Fix MiniMax-M3 fused MXFP8 block scale (#53674)
- **2026-09-16** [`a4d2d9d95e`](https://github.com/vllm-project/vllm/commit/a4d2d9d95e) [#53940](https://github.com/vllm-project/vllm/pull/53940) — [ROCm][Kimi-K3] Enable a4w4 flydsl kernels for KimiK3 (#53940)
- **2026-09-16** [`c8d1cf077a`](https://github.com/vllm-project/vllm/commit/c8d1cf077a) [#56176](https://github.com/vllm-project/vllm/pull/56176) — [ROCm] [Bugfix] Enable Load and Inference of GLM-5.3-Flash Quark MXFP4 Checkpoint (#56176)
- **2026-09-15** [`18f8aa0465`](https://github.com/vllm-project/vllm/commit/18f8aa0465) [#56845](https://github.com/vllm-project/vllm/pull/56845) — [Refactor] Remove dead kernel code (#56845)
- **2026-09-15** [`dffbb714e4`](https://github.com/vllm-project/vllm/commit/dffbb714e4) [#56743](https://github.com/vllm-project/vllm/pull/56743) — [ROCm][Perf] Optimize DSV4.1 K=512 decode top-k on gfx950 (#56743)
- **2026-09-15** [`35dc273072`](https://github.com/vllm-project/vllm/commit/35dc273072) [#55966](https://github.com/vllm-project/vllm/pull/55966) — [ROCm][Spec Decode] Add Aiter MLA decode support non-causal draft block (#55966)
- **2026-09-15** [`e6eb0d120c`](https://github.com/vllm-project/vllm/commit/e6eb0d120c) [#56893](https://github.com/vllm-project/vllm/pull/56893) — [Model][DSv4.1] Store the whole KV in MXFP8 (FlashMLA V4.1 record) (#56893)
- **2026-09-15** [`3192898754`](https://github.com/vllm-project/vllm/commit/3192898754) [#56921](https://github.com/vllm-project/vllm/pull/56921) — [ROCm][CI] Prepare TheRock image for CI (#56921)
- **2026-09-15** [`ef5f7cd119`](https://github.com/vllm-project/vllm/commit/ef5f7cd119) [#56560](https://github.com/vllm-project/vllm/pull/56560) — [ROCm][DSv4.1][Perf] Dequantize the MXFP8 weight once when dot_scaled cannot be used (#56560)
- **2026-09-15** [`a7576447b8`](https://github.com/vllm-project/vllm/commit/a7576447b8) [#56687](https://github.com/vllm-project/vllm/pull/56687) — [ROCm][Bugfix] Initialize Ray NIXL agents for sharded RDT (#56687)
- **2026-09-14** [`00972dfd72`](https://github.com/vllm-project/vllm/commit/00972dfd72) [#56513](https://github.com/vllm-project/vllm/pull/56513) — [ROCm][DSV4.1][Perf] Fold the mHC post step into the delayed pre projection (#56513)
- **2026-09-14** [`dabc4362b4`](https://github.com/vllm-project/vllm/commit/dabc4362b4) [#56628](https://github.com/vllm-project/vllm/pull/56628) — [ROCm][DSV4.1][Perf] Stride the DSA decode candidate mask over the live context (#56628)
- **2026-09-14** [`d4ee7fe7a9`](https://github.com/vllm-project/vllm/commit/d4ee7fe7a9) [#51204](https://github.com/vllm-project/vllm/pull/51204) — [Quantization] Select linear backends per quantization (#51204)
- **2026-09-14** [`1d0d1081c4`](https://github.com/vllm-project/vllm/commit/1d0d1081c4) [#53721](https://github.com/vllm-project/vllm/pull/53721) — [ROCm][Connector] SWA+HMA-support in MoRI-IO connector (Gemma4) (#53721)
- **2026-09-14** [`a6c5d6d0fc`](https://github.com/vllm-project/vllm/commit/a6c5d6d0fc) [#51794](https://github.com/vllm-project/vllm/pull/51794) — [ROCm][Perf] Enable CSA multi-stream overlap for DeepSeek-V4 (#51794)
- **2026-09-14** [`dc2e8f1157`](https://github.com/vllm-project/vllm/commit/dc2e8f1157) [#54965](https://github.com/vllm-project/vllm/pull/54965) — [ROCm][Perf] W4A16: keep skinny GEMM zero-points packed 4-bit (#54965)
- **2026-09-14** [`23cfaad497`](https://github.com/vllm-project/vllm/commit/23cfaad497) [#56763](https://github.com/vllm-project/vllm/pull/56763) — [CI] Update entrypoints CI (#56763)
- **2026-09-14** [`78e84261ab`](https://github.com/vllm-project/vllm/commit/78e84261ab) [#48498](https://github.com/vllm-project/vllm/pull/48498) — [Performance] Add Triton kernel for Gemma3n sparse GELU (#48498)
- **2026-09-14** [`cf1584f373`](https://github.com/vllm-project/vllm/commit/cf1584f373) [#56741](https://github.com/vllm-project/vllm/pull/56741) — [Refactor] Normalize DeepSeek V4.1 model package naming (#56741)
- **2026-09-14** [`dfa1984e58`](https://github.com/vllm-project/vllm/commit/dfa1984e58) [#55235](https://github.com/vllm-project/vllm/pull/55235) — [ROCm][Perf] Tune MiniMax-M3 decode top-k for short contexts (#55235)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#57064](https://github.com/vllm-project/vllm/issues/57064) | [Bug][ROCm][Attention][KV Connector] DeepSeek-V3.2 / GLM-5.x DSA spars | rocm, deepseek, kv-connector, glm | 2026-09-21 |
| [#57149](https://github.com/vllm-project/vllm/issues/57149) | [ROCm][AMD] Qwen3.8-2.4T-A95B gfx950 / MI355X Performance Optimization | performance, rocm, quantization | 2026-09-21 |
| [#57956](https://github.com/vllm-project/vllm/issues/57956) | [Bug]: AMD mirror declarations disagree with test-amd.yaml steps - dec | rocm | 2026-09-21 |
| [#52682](https://github.com/vllm-project/vllm/issues/52682) | [Bug]: Qwen3.8-27B-FP8 hangs indefinitely at startup during CUDA-graph | rocm | 2026-09-21 |
| [#57960](https://github.com/vllm-project/vllm/issues/57960) | [Feature]: [ROCm][AITER][Hy4] Enable gfx950 MXFP8 MoE and dense linear | feature request, rocm | 2026-09-21 |
| [#49547](https://github.com/vllm-project/vllm/issues/49547) | FlashInfer + spec-decode silently downgrades to PIECEWISE cudagraphs ( | — | 2026-09-21 |
| [#57950](https://github.com/vllm-project/vllm/issues/57950) | [Bug]: FunctionGemma rejects hyphenated tool names only in non-streami | bug, tool-calling | 2026-09-21 |
| [#46249](https://github.com/vllm-project/vllm/issues/46249) | [Bug]: [Regression] Qwen3.6-27B tool calls fail on Responses API when  | bug, structured-output, speculative-decoding, tool-calling | 2026-09-21 |
| [#57927](https://github.com/vllm-project/vllm/issues/57927) | [Bug]: Chunked embeddings break dot-product scoring with `use_activati | bug | 2026-09-21 |
| [#57938](https://github.com/vllm-project/vllm/issues/57938) | [Bug]: AssertionError in _update_from_kv_xfer_finished when LMCache KV | bug, rocm, kv-connector | 2026-09-21 |
| [#56605](https://github.com/vllm-project/vllm/issues/56605) | [Bug]: GLM-5.3-Flash degenerates into repeated-token "word salad" in m | bug, glm | 2026-09-21 |
| [#57929](https://github.com/vllm-project/vllm/issues/57929) | [Bug]: `/v1/completions/derender` drops requested `prompt_logprobs` | bug | 2026-09-21 |
| [#54453](https://github.com/vllm-project/vllm/issues/54453) | [Performance]: muse_glimmer makes decoding quadratic under structured  | structured-output, tool-calling | 2026-09-21 |
| [#50189](https://github.com/vllm-project/vllm/issues/50189) | [Bug]: Xid 31 MMU fault (illegal write) with flashinfer_b12x MoE backe | — | 2026-09-21 |
| [#57936](https://github.com/vllm-project/vllm/issues/57936) | [Bug]: --kv-cache-memory suggestion double-counts CUDAGraph memory (re | bug | 2026-09-21 |
| [#57935](https://github.com/vllm-project/vllm/issues/57935) | [Bug]: `/v1/chat/completions/batch` leaks hidden reasoning through log | bug, tool-calling | 2026-09-21 |
| [#57932](https://github.com/vllm-project/vllm/issues/57932) | [Bug]: SM120 / RTX PRO 6000 Blackwell: GLM-5.3-Flash fails with FlashI | bug, glm | 2026-09-21 |
| [#49730](https://github.com/vllm-project/vllm/issues/49730) | [Bug][Qwen 3.5 4B][H100]: Performance of DFlash is lower than expected | bug, quantization | 2026-09-21 |
| [#57740](https://github.com/vllm-project/vllm/issues/57740) | [Bug]: User-authored <|image_pad|> in text is misrecognized as image p | bug | 2026-09-21 |
| [#57759](https://github.com/vllm-project/vllm/issues/57759) | [Bug]: FULL_AND_PIECEWISE capture fails intermittently with cudaErrorN | bug | 2026-09-21 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 83 |
| MoE / Expert Parallel | 48 |
| Attention | 43 |
| Other | 40 |
| Multimodal | 34 |
| Scheduler / Engine | 29 |
| CI / Build | 28 |
| Serving / API | 23 |
| Disaggregation / PD | 23 |
| Models | 22 |
| KV Cache / Offload | 16 |
| Speculative Decoding | 15 |
| Quantization | 13 |
| Perf / Benchmark | 9 |
| Docs | 8 |
| LoRA | 8 |
| Compilation / CUDA Graph | 4 |

## ROCm / AMD  (83 commits)

- **2026-09-21** [`e34685dfc0`](https://github.com/vllm-project/vllm/commit/e34685dfc0) [#52362](https://github.com/vllm-project/vllm/pull/52362)
  [ROCm][DSv4] Enable DSpark adaptive verification (#52362)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/models/test_deepseek_v4_dspark_rocm.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`, `vllm/models/deepseek_v4/amd/dspark.py` _+2 more__
- **2026-09-21** [`7488b5780f`](https://github.com/vllm-project/vllm/commit/7488b5780f) [#57869](https://github.com/vllm-project/vllm/pull/57869)
  [ROCm][Tests] Reduce host memory when downcasting FP32 HF references (#57869)
  _Files: `tests/conftest.py`_
- **2026-09-21** [`82daf9f575`](https://github.com/vllm-project/vllm/commit/82daf9f575) [#57876](https://github.com/vllm-project/vllm/pull/57876)
  [CI][ROCm] Add ten AMD parity groups (#57876)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/disaggregated_ec.yaml`, `.buildkite/test_areas/disaggregated_mooncake.yaml` _+12 more__
- **2026-09-21** [`04c1f4a407`](https://github.com/vllm-project/vllm/commit/04c1f4a407) [#57906](https://github.com/vllm-project/vllm/pull/57906)
  [Bugfix][ROCm][DSv4.1] Disable SWA bounded replay on ROCm (#57906)
  _Files: `vllm/models/deepseek_v41/attention.py`_
- **2026-09-21** [`0aee727ff6`](https://github.com/vllm-project/vllm/commit/0aee727ff6) [#57903](https://github.com/vllm-project/vllm/pull/57903)
  [CI][ROCm] Increase timeout for MI300 Distributed DP Extended (#57903)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-21** [`8902dbb177`](https://github.com/vllm-project/vllm/commit/8902dbb177) [#57877](https://github.com/vllm-project/vllm/pull/57877)
  [CI][ROCm] Mirror remaining portable suites without duplicate coverage (#57877)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/models_basic.yaml` _+7 more__
- **2026-09-21** [`b8cf275382`](https://github.com/vllm-project/vllm/commit/b8cf275382) [#54535](https://github.com/vllm-project/vllm/pull/54535)
  [AMD][Minimax-M3][perf] Enable packed LBHNC AITER QK-norm fusion for MiniMax-M3 on ROCm (#54535)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/_aiter_ops.py`, `vllm/models/minimax_m3/amd/model.py`_
- **2026-09-21** [`f05b88751e`](https://github.com/vllm-project/vllm/commit/f05b88751e) [#57870](https://github.com/vllm-project/vllm/pull/57870)
  [CI][ROCm] Make Python-only installation failures blocking (#57870)
  _Files: `.buildkite/test_areas/misc.yaml`_
- **2026-09-21** [`0ff0477ff9`](https://github.com/vllm-project/vllm/commit/0ff0477ff9) [#57526](https://github.com/vllm-project/vllm/pull/57526)
  [Perf][ROCm] Add a ROCm path for Hy4 and compile the backbone (#57526)
  _Files: `tests/models/test_hyv4_rocm.py`, `vllm/models/hy_v4/__init__.py`, `vllm/models/hy_v4/amd/__init__.py`, `vllm/models/hy_v4/amd/model.py`_
- **2026-09-21** [`76ee20c1ec`](https://github.com/vllm-project/vllm/commit/76ee20c1ec) [#57864](https://github.com/vllm-project/vllm/pull/57864)
  [ROCm][Tests] Avoid pooling cleanup waits against live shared engines (#57864)
  _Files: `tests/models/language/pooling/conftest.py`, `tests/models/language/pooling_mteb_test/conftest.py`, `tests/models/multimodal/pooling/conftest.py`_
- **2026-09-21** [`6dfd87f596`](https://github.com/vllm-project/vllm/commit/6dfd87f596) [#57491](https://github.com/vllm-project/vllm/pull/57491)
  [ROCm][DSv4.1] Keep the Engram tables in host memory on ROCm (#57491)
  _Files: `tests/kernels/test_engram.py`, `tests/test_config.py`, `vllm/config/engram.py`, `vllm/config/vllm.py` _+1 more__
- **2026-09-20** [`01f1f58f10`](https://github.com/vllm-project/vllm/commit/01f1f58f10) [#57450](https://github.com/vllm-project/vllm/pull/57450)
  [ROCm][CI] Query HIP device memory for test GPU teardown waits. (#57450)
  _Files: `tests/compile/passes/conftest.py`, `tests/conftest.py`, `tests/kernels/moe/conftest.py`, `tests/utils.py`_
- **2026-09-20** [`4868312128`](https://github.com/vllm-project/vllm/commit/4868312128) [#57621](https://github.com/vllm-project/vllm/pull/57621)
  [Refactor] Remove dead kernel code (#57621)
  _Files: `csrc/cpu/sgl-kernels/common.h`, `csrc/libtorch_stable/cuda_vec_utils.cuh`, `csrc/libtorch_stable/moe/moe_wna16_utils.h`, `csrc/libtorch_stable/quantization/gptq/matrix_view.cuh` _+8 more__
- **2026-09-20** [`27757dde02`](https://github.com/vllm-project/vllm/commit/27757dde02) [#56625](https://github.com/vllm-project/vllm/pull/56625)
  [DSV4.1] Add encoder cuda graph support for deepseek-v4.1-flash (#56625)
  _Files: `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/models/multimodal/processing/test_tensor_schema.py`, `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v41/amd/vl_model.py` _+2 more__
- **2026-09-20** [`0e110f696d`](https://github.com/vllm-project/vllm/commit/0e110f696d) [#54894](https://github.com/vllm-project/vllm/pull/54894)
  [ROCm][DSV4][Perf] Use FP8 WO_A output projection (#54894)
  _Files: `tests/models/test_deepseek_v4_rocm_wo_a.py`, `vllm/models/deepseek_v4/amd/rocm.py`_
- **2026-09-20** [`1596fa5f88`](https://github.com/vllm-project/vllm/commit/1596fa5f88) [#57434](https://github.com/vllm-project/vllm/pull/57434)
  [ROCm][DSv4.1][Perf] Reuse the decode topk ragged metadata across layers (#57434)
  _Files: `vllm/models/deepseek_v41/amd/rocm.py`_
- **2026-09-19** [`36fa72d2d0`](https://github.com/vllm-project/vllm/commit/36fa72d2d0) [#57701](https://github.com/vllm-project/vllm/pull/57701)
  [GLM5.3 Perf] Size the GLM-5 sparse indexer decode workspace, 3072 MiB GPU memory saved (#57701)
  _Files: `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`_
- **2026-09-19** [`fbe8a157fb`](https://github.com/vllm-project/vllm/commit/fbe8a157fb) [#53623](https://github.com/vllm-project/vllm/pull/53623)
  [ROCm][Perf] Enable the AITER GDN decode fast path for flat qkvz layouts (#53623)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/mamba/test_gdn_rocm_layout_dispatch.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-09-19** [`4cc15f2121`](https://github.com/vllm-project/vllm/commit/4cc15f2121) [#57316](https://github.com/vllm-project/vllm/pull/57316)
  [Quantization] Let ModelOpt MXFP8 layers load pre-processed weights  Purpose (#57316)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel.py`, `vllm/model_executor/kernels/linear/mxfp8/emulation.py`, `vllm/model_executor/kernels/linear/mxfp8/flashinfer.py` _+2 more__
- **2026-09-19** [`59e6682c21`](https://github.com/vllm-project/vllm/commit/59e6682c21) [#53009](https://github.com/vllm-project/vllm/pull/53009)
  [CI][AMD] Bump torchao to v18 for Python 3.14 (#53009)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-19** [`468663a5e5`](https://github.com/vllm-project/vllm/commit/468663a5e5) [#56885](https://github.com/vllm-project/vllm/pull/56885)
  [ROCm] Bump AITER to v0.1.22.post1 (#56885)
  _Files: `docker/Dockerfile.rock_base`, `docker/Dockerfile.rocm_base`_
- **2026-09-18** [`1dc2d854c1`](https://github.com/vllm-project/vllm/commit/1dc2d854c1) [#56227](https://github.com/vllm-project/vllm/pull/56227)
  [Feat][Model] Support encoder-side SWA-bounded replay for DeepSeek-V4.1-Flash (#56227)
  _Files: `tests/models/test_deepseek_v41_replay_start.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `tests/v1/attention/test_dspark_noncausal_sparse_mla.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` _+26 more__
- **2026-09-18** [`0390299309`](https://github.com/vllm-project/vllm/commit/0390299309) [#57583](https://github.com/vllm-project/vllm/pull/57583)
  [ROCm][CI] Shard MI300 Entrypoints Integration (Pooling) (#57583)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-18** [`2c3fb4c545`](https://github.com/vllm-project/vllm/commit/2c3fb4c545) [#56162](https://github.com/vllm-project/vllm/pull/56162)
  [CI][ROCm] Deprecate DinD for MI250 test groups (#56162)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/distributed.yaml` _+14 more__
- **2026-09-18** [`71fc70d3ae`](https://github.com/vllm-project/vllm/commit/71fc70d3ae) [#50455](https://github.com/vllm-project/vllm/pull/50455)
  [ROCm][DSv4] Fix sparse-indexer logits collapse on gfx950/gfx942 (#50455)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-09-18** [`c58532c86b`](https://github.com/vllm-project/vllm/commit/c58532c86b) [#57272](https://github.com/vllm-project/vllm/pull/57272)
  [Frontend] Upgrade XGrammar to 0.2.7 and Rust structural tags to 0.3.0 (#57272)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt` _+11 more__
- **2026-09-18** [`4c6c1a40b3`](https://github.com/vllm-project/vllm/commit/4c6c1a40b3) [#57328](https://github.com/vllm-project/vllm/pull/57328)
  [ROCm][Bugfix] Fix intermittent ROCR host segfault (#57328)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-09-18** [`d12c276853`](https://github.com/vllm-project/vllm/commit/d12c276853) [#57425](https://github.com/vllm-project/vllm/pull/57425)
  [Bugfix][ROCm] Alias SparseAttnIndexerKpool.forward_cuda to forward_native (GLM-5.3-Flash boot crash) (#57425)
  _Files: `vllm/models/glm5next/amd/sparse_indexer.py`_
- **2026-09-18** [`7b94293627`](https://github.com/vllm-project/vllm/commit/7b94293627) [#57160](https://github.com/vllm-project/vllm/pull/57160)
  [Bugfix][ROCm][KV Offload] Use private pinned tensors for CPU KV offload (#57160)
  _Files: `tests/v1/kv_offload/test_factory.py`, `vllm/v1/kv_offload/cpu/spec.py`_
- **2026-09-18** [`213c379fca`](https://github.com/vllm-project/vllm/commit/213c379fca) [#57426](https://github.com/vllm-project/vllm/pull/57426)
  [ROCm][Bugfix] Gate AITER MXFP8 MoE on the aiter enable flag (#57426)
  _Files: `tests/kernels/moe/test_mxfp8_aiter_backend_selection.py`, `tests/models/quantization/test_mxfp8.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp8_moe.py`_
- **2026-09-17** [`a524f80b1f`](https://github.com/vllm-project/vllm/commit/a524f80b1f) [#57289](https://github.com/vllm-project/vllm/pull/57289)
  [AMD][Bugfix] Make the nested-RoPE patch reach automatic validation (#57289)
  _Files: `vllm/transformers_utils/config.py`_
- **2026-09-17** [`e0050f287a`](https://github.com/vllm-project/vllm/commit/e0050f287a) [#57252](https://github.com/vllm-project/vllm/pull/57252)
  [Bugfix][ROCm] Add record_logical_topk_ready to ROCMAiterMLASparseImpl (GLM-5.3-Flash boot crash) (#57252)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-09-17** [`d3074acdda`](https://github.com/vllm-project/vllm/commit/d3074acdda) [#53837](https://github.com/vllm-project/vllm/pull/53837)
  [AMD][CI][The Rock] Fix language models standard for The Rock on mi355 (#53837)
  _Files: `tests/models/language/generation/test_common.py`, `tests/models/registry.py`_
- **2026-09-17** [`acc2ed2a5f`](https://github.com/vllm-project/vllm/commit/acc2ed2a5f) [#54849](https://github.com/vllm-project/vllm/pull/54849)
  [ROCm][CI][The Rock 10] Fix (MI355) Quantized Models failure on The Rock 10 with Triton 3.8.x (#54849)
  _Files: `vllm/model_executor/kernels/linear/mxfp8/rocm_native.py`_
- **2026-09-17** [`9a5bd373cf`](https://github.com/vllm-project/vllm/commit/9a5bd373cf) [#57398](https://github.com/vllm-project/vllm/pull/57398)
  [CI] Retire Weight Loading smoke tests (#57398)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/weight_loading.yaml`, `.github/CODEOWNERS`, `tests/kernels/quantization/test_rocm_compressed_tensors_w4a16.py` _+6 more__
- **2026-09-17** [`a9a7e45f31`](https://github.com/vllm-project/vllm/commit/a9a7e45f31) [#57055](https://github.com/vllm-project/vllm/pull/57055)
  [ROCm] Restore `VLLM_ROCM_USE_AITER_FP4_ASM_GEMM` and default w4a4 ASM GEMM back to off (#57055)
  _Files: `tests/kernels/quantization/test_rocm_mxfp4.py`, `vllm/_aiter_ops.py`, `vllm/envs.py`_
- **2026-09-17** [`ff6b5808c4`](https://github.com/vllm-project/vllm/commit/ff6b5808c4) [#53792](https://github.com/vllm-project/vllm/pull/53792)
  [ROCm] Resolve the indexer fp8 cache dtype once at import (#53792)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-09-17** [`e30bf70c5d`](https://github.com/vllm-project/vllm/commit/e30bf70c5d) [#57380](https://github.com/vllm-project/vllm/pull/57380)
  [ROCm][CI] Fix Entrypoints Integration (Pooling) tests on TheRock image (#57380)
  _Files: `tests/entrypoints/pooling/scoring/test_cross_encoder_online_vision.py`_
- **2026-09-17** [`fef55fd26d`](https://github.com/vllm-project/vllm/commit/fef55fd26d) [#57385](https://github.com/vllm-project/vllm/pull/57385)
  [ROCm][CI] Adapt MoE tests to the triton_kernels 3.8 API (#57385)
  _Files: `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `tests/kernels/moe/test_modular_oai_triton_moe.py`, `tests/kernels/moe/utils.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py` _+1 more__
- **2026-09-17** [`d7e755c230`](https://github.com/vllm-project/vllm/commit/d7e755c230) [#57295](https://github.com/vllm-project/vllm/pull/57295)
  [Bugfix] Fix wrong vLLM version reported by pip install (proto-v* tag collision) (#57295)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `setup.py`, `tools/build_rust.py`_
- **2026-09-17** [`1df336c3ba`](https://github.com/vllm-project/vllm/commit/1df336c3ba) [#48249](https://github.com/vllm-project/vllm/pull/48249)
  [Perf][ROCm] Enable AITER QuickReduce + RMSNorm fusion (#48249)
  _Files: `tests/distributed/test_quick_all_reduce.py`, `vllm/_aiter_ops.py`_
- **2026-09-17** [`3affd35f31`](https://github.com/vllm-project/vllm/commit/3affd35f31) [#56359](https://github.com/vllm-project/vllm/pull/56359)
  [Fix][ROCm] MXFP4 MoE round-up inflates TP-sharded expert weights on CDNA3, starving KV cache (#56359)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-09-17** [`438434b5b5`](https://github.com/vllm-project/vllm/commit/438434b5b5) [#56849](https://github.com/vllm-project/vllm/pull/56849)
  [ROCm][Perf] Insert MiniMax-M3 sparse-PA K/V without a contiguous copy (#56849)
  _Files: `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/models/minimax_m3/amd/model.py`_
- **2026-09-17** [`0eae9acd4d`](https://github.com/vllm-project/vllm/commit/0eae9acd4d) [#56590](https://github.com/vllm-project/vllm/pull/56590)
  [Bugfix][ROCm][MoE] Fall back instead of crashing when AITER MoE is requested for a non-gated (is_act_and_mul=False) model (#56590)
  _Files: `tests/kernels/moe/test_unquantized_backend_selection.py`, `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`_
- **2026-09-17** [`8be3ca35f3`](https://github.com/vllm-project/vllm/commit/8be3ca35f3) [#57375](https://github.com/vllm-project/vllm/pull/57375)
  [ROCm][CI] Fix AMD CI pipeline upload rejected by an invalid block-step key (#57375)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-17** [`667b26e50b`](https://github.com/vllm-project/vllm/commit/667b26e50b) [#57192](https://github.com/vllm-project/vllm/pull/57192)
  [Bugfix][ROCm][GLM-5.3-Flash] Apply deferred tilelang.jit already on attribute access (#57192)
  _Files: `tests/kernels/test_mhc_tilelang_jit.py`, `vllm/tilelang_utils/__init__.py`_
- **2026-09-17** [`f1c2f6ada8`](https://github.com/vllm-project/vllm/commit/f1c2f6ada8) [#57080](https://github.com/vllm-project/vllm/pull/57080)
  [ROCm][CI] Stage H gating and MI355 test reallocation (#57080)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/disaggregated.yaml` _+19 more__
- **2026-09-17** [`528fa835fd`](https://github.com/vllm-project/vllm/commit/528fa835fd) [#56343](https://github.com/vllm-project/vllm/pull/56343)
  [ROCm] Stage large pageable H2D copies instead of registering them (#56343)
  _Files: `vllm/platforms/rocm.py`_
- **2026-09-17** [`fdcd42350b`](https://github.com/vllm-project/vllm/commit/fdcd42350b) [#56853](https://github.com/vllm-project/vllm/pull/56853)
  [ROCm][Perf] Enable HCA dual-stream overlap for DeepSeek-V4 (#56853)
  _Files: `vllm/models/deepseek_v4/amd/rocm.py`_
- **2026-09-17** [`2d8a5c5741`](https://github.com/vllm-project/vllm/commit/2d8a5c5741) [#57229](https://github.com/vllm-project/vllm/pull/57229)
  [ROCm][Bugfix] Reduce CUDA graph divergences (#57229)
  _Files: `tests/test_config.py`, `vllm/distributed/parallel_state.py`, `vllm/platforms/rocm.py`, `vllm/v1/worker/gpu_model_runner.py` _+1 more__
- **2026-09-17** [`68f2c7e74f`](https://github.com/vllm-project/vllm/commit/68f2c7e74f) [#57249](https://github.com/vllm-project/vllm/pull/57249)
  [ROCm][CI] Fix Nixl+Offloading PD edge cases on TheRock image (#57249)
  _Files: `docker/Dockerfile.rock`, `tests/v1/kv_connector/nixl_integration/test_multi_connector_edge_cases.py`_
- **2026-09-17** [`19b6ff62f2`](https://github.com/vllm-project/vllm/commit/19b6ff62f2) [#56726](https://github.com/vllm-project/vllm/pull/56726)
  [ROCm][Bugfix] Ignore descales for unquantized AITER caches (#56726)
  _Files: `tests/v1/attention/test_attention_backends.py`, `vllm/v1/attention/backends/rocm_aiter_fa.py`_
- **2026-09-17** [`3e267bae70`](https://github.com/vllm-project/vllm/commit/3e267bae70) [#55934](https://github.com/vllm-project/vllm/pull/55934)
  [ROCm] triton+triton_kernels 3.8 mxfp4 MoE support (gpt-oss + DeepSeek-V4) (#55934)
  _Files: `docker/Dockerfile.rock`, `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a16_moe.py` _+5 more__
- **2026-09-17** [`95f4925c3a`](https://github.com/vllm-project/vllm/commit/95f4925c3a) [#57074](https://github.com/vllm-project/vllm/pull/57074)
  [ROCm][CI] Enable AITER FP8/unquantized cases in modular-kernel sweep + fix MoRI per-tensor FP8 dispatch (#57074)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/modular_kernel_tools/mk_objects.py`, `tests/kernels/moe/test_modular_kernel_combinations.py` _+2 more__
- **2026-09-16** [`91b96a533c`](https://github.com/vllm-project/vllm/commit/91b96a533c) [#57056](https://github.com/vllm-project/vllm/pull/57056)
  [ROCm][CI] Shard MI300 Multimodal Processor (#57056)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-16** [`bc0f47cd03`](https://github.com/vllm-project/vllm/commit/bc0f47cd03) [#57132](https://github.com/vllm-project/vllm/pull/57132)
  [ROCm][Bugfix] Revert #56433 + #51692 to fix accuracy breakdown for DeepSeek-V4 (#57132)
  _Files: `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/aiter.py` _+4 more__
- **2026-09-16** [`6ca2b23e22`](https://github.com/vllm-project/vllm/commit/6ca2b23e22) [#54248](https://github.com/vllm-project/vllm/pull/54248)
  [ROCm] Expose kFp8DynamicTokenSym on AITER PTPC linears (#54248)
  _Files: `tests/fusion/test_quant_activation_contract.py`, `tests/quantization/test_quark.py`, `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`, `vllm/model_executor/layers/quantization/online/fp8.py` _+1 more__
- **2026-09-16** [`ec4a3a5370`](https://github.com/vllm-project/vllm/commit/ec4a3a5370) [#56108](https://github.com/vllm-project/vllm/pull/56108)
  [CI] Bump Transformers version to 5.17.0 (#56108)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt` _+13 more__
- **2026-09-16** [`d6a1677d55`](https://github.com/vllm-project/vllm/commit/d6a1677d55) [#56935](https://github.com/vllm-project/vllm/pull/56935)
  [Model][DSv4.1] FlashMLA mega attention and the NVFP4 compressed KV cache (#56935)
  _Files: `benchmarks/kernels/benchmark_dsv41_mega_attn.py`, `csrc/libtorch_stable/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+16 more__
- **2026-09-16** [`ab35354c21`](https://github.com/vllm-project/vllm/commit/ab35354c21) [#55991](https://github.com/vllm-project/vllm/pull/55991)
  [ROCm][AITER] Skip AITER norm kernels when flattening to 2D would copy (#55991)
  _Files: `tests/kernels/ir/test_aiter_norm_dispatch.py`, `vllm/kernels/aiter_ops.py`_
- **2026-09-16** [`b3b13c1292`](https://github.com/vllm-project/vllm/commit/b3b13c1292) [#57112](https://github.com/vllm-project/vllm/pull/57112)
  [ROCm][CI] Fix MLA RoPE fused-kernel tests for TheRock image (#57112)
  _Files: `tests/kernels/core/test_rotary_embedding_mla_cache_fused.py`_
- **2026-09-16** [`4fe9e6f6e5`](https://github.com/vllm-project/vllm/commit/4fe9e6f6e5) [#55358](https://github.com/vllm-project/vllm/pull/55358)
  [Refactor][GLM-5.3-Flash] Move sparse_attn_indexer_kpool into the model folder and split AMD/NVIDIA (#55358)
  _Files: `tests/v1/attention/test_sparse_indexer_decode_seq_lens.py`, `vllm/models/glm5next/amd/sparse_indexer.py`, `vllm/models/glm5next/common/attention.py`, `vllm/models/glm5next/common/sparse_indexer.py` _+2 more__
- **2026-09-16** [`711768fc17`](https://github.com/vllm-project/vllm/commit/711768fc17) [#56351](https://github.com/vllm-project/vllm/pull/56351)
  [CI][ROCm] Add opt-in TheRock builds for AMD CI (#56351)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/scripts/rocm/build-config.sh`, `.buildkite/scripts/rocm/refresh-base-image.sh` _+1 more__
- **2026-09-16** [`22bb158c21`](https://github.com/vllm-project/vllm/commit/22bb158c21) [#53674](https://github.com/vllm-project/vllm/pull/53674)
  [Bugfix][ROCm] Fix MiniMax-M3 fused MXFP8 block scale (#53674)
  _Files: `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`_
- **2026-09-16** [`a4d2d9d95e`](https://github.com/vllm-project/vllm/commit/a4d2d9d95e) [#53940](https://github.com/vllm-project/vllm/pull/53940)
  [ROCm][Kimi-K3] Enable a4w4 flydsl kernels for KimiK3 (#53940)
  _Files: `tests/kernels/moe/test_rocm_aiter_moe.py`, `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py` _+1 more__
- **2026-09-16** [`c8d1cf077a`](https://github.com/vllm-project/vllm/commit/c8d1cf077a) [#56176](https://github.com/vllm-project/vllm/pull/56176)
  [ROCm] [Bugfix] Enable Load and Inference of GLM-5.3-Flash Quark MXFP4 Checkpoint (#56176)
  _Files: `tests/quantization/test_quark.py`, `vllm/models/glm5next/__init__.py`, `vllm/models/glm5next/common/__init__.py`, `vllm/models/glm5next/common/attention.py` _+4 more__
- **2026-09-15** [`18f8aa0465`](https://github.com/vllm-project/vllm/commit/18f8aa0465) [#56845](https://github.com/vllm-project/vllm/pull/56845)
  [Refactor] Remove dead kernel code (#56845)
  _Files: `vllm/model_executor/layers/mamba/ops/replayssm_config.py`, `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/inkling/amd/ops/lamport.py`, `vllm/models/inkling/amd/ops/mm_towers.py` _+4 more__
- **2026-09-15** [`dffbb714e4`](https://github.com/vllm-project/vllm/commit/dffbb714e4) [#56743](https://github.com/vllm-project/vllm/pull/56743)
  [ROCm][Perf] Optimize DSV4.1 K=512 decode top-k on gfx950 (#56743)
  _Files: `csrc/libtorch_stable/sampler.cu`, `tests/kernels/test_top_k_per_row.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-09-15** [`35dc273072`](https://github.com/vllm-project/vllm/commit/35dc273072) [#55966](https://github.com/vllm-project/vllm/pull/55966)
  [ROCm][Spec Decode] Add Aiter MLA decode support non-causal draft block (#55966)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_fp8_support.py`, `tests/v1/attention/test_rocm_aiter_mla_fp8_decode_routing.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/_aiter_ops.py` _+1 more__
- **2026-09-15** [`e6eb0d120c`](https://github.com/vllm-project/vllm/commit/e6eb0d120c) [#56893](https://github.com/vllm-project/vllm/pull/56893)
  [Model][DSv4.1] Store the whole KV in MXFP8 (FlashMLA V4.1 record) (#56893)
  _Files: `cmake/external_projects/flashmla.cmake`, `csrc/libtorch_stable/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+10 more__
- **2026-09-15** [`3192898754`](https://github.com/vllm-project/vllm/commit/3192898754) [#56921](https://github.com/vllm-project/vllm/pull/56921)
  [ROCm][CI] Prepare TheRock image for CI (#56921)
  _Files: `docker/Dockerfile.rock`, `docker/Dockerfile.rock_base`_
- **2026-09-15** [`ef5f7cd119`](https://github.com/vllm-project/vllm/commit/ef5f7cd119) [#56560](https://github.com/vllm-project/vllm/pull/56560)
  [ROCm][DSv4.1][Perf] Dequantize the MXFP8 weight once when dot_scaled cannot be used (#56560)
  _Files: `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/model_executor/kernels/linear/mxfp8/rocm_native.py`_
- **2026-09-15** [`a7576447b8`](https://github.com/vllm-project/vllm/commit/a7576447b8) [#56687](https://github.com/vllm-project/vllm/pull/56687)
  [ROCm][Bugfix] Initialize Ray NIXL agents for sharded RDT (#56687)
  _Files: `tests/distributed/test_sharded_rdt_producer.py`, `vllm/distributed/nixl_utils.py`, `vllm/distributed/weight_transfer/sharded_rdt_common.py`, `vllm/distributed/weight_transfer/sharded_rdt_engine.py` _+1 more__
- **2026-09-14** [`00972dfd72`](https://github.com/vllm-project/vllm/commit/00972dfd72) [#56513](https://github.com/vllm-project/vllm/pull/56513)
  [ROCm][DSV4.1][Perf] Fold the mHC post step into the delayed pre projection (#56513)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/kernels/mhc/aiter.py`, `vllm/model_executor/layers/mhc.py` _+1 more__
- **2026-09-14** [`dabc4362b4`](https://github.com/vllm-project/vllm/commit/dabc4362b4) [#56628](https://github.com/vllm-project/vllm/pull/56628)
  [ROCm][DSV4.1][Perf] Stride the DSA decode candidate mask over the live context (#56628)
  _Files: `tests/kernels/attention/test_rocm_aiter_candidate_mask.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-09-14** [`d4ee7fe7a9`](https://github.com/vllm-project/vllm/commit/d4ee7fe7a9) [#51204](https://github.com/vllm-project/vllm/pull/51204)
  [Quantization] Select linear backends per quantization (#51204)
  _Files: `docs/features/quantization/README.md`, `tests/kernels/quantization/test_scaled_mm_kernel_selection.py`, `tests/model_executor/kernels/test_b12x_linear.py`, `vllm/config/kernel.py` _+2 more__
- **2026-09-14** [`1d0d1081c4`](https://github.com/vllm-project/vllm/commit/1d0d1081c4) [#53721](https://github.com/vllm-project/vllm/pull/53721)
  [ROCm][Connector] SWA+HMA-support in MoRI-IO connector (Gemma4) (#53721)
  _Files: `tests/v1/kv_connector/unit/test_moriio_connector.py`, `tests/v1/kv_connector/unit/test_moriio_routing.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`_
- **2026-09-14** [`a6c5d6d0fc`](https://github.com/vllm-project/vllm/commit/a6c5d6d0fc) [#51794](https://github.com/vllm-project/vllm/pull/51794)
  [ROCm][Perf] Enable CSA multi-stream overlap for DeepSeek-V4 (#51794)
  _Files: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/cpu/cpu_sparse.py`_
- **2026-09-14** [`dc2e8f1157`](https://github.com/vllm-project/vllm/commit/dc2e8f1157) [#54965](https://github.com/vllm-project/vllm/pull/54965)
  [ROCm][Perf] W4A16: keep skinny GEMM zero-points packed 4-bit (#54965)
  _Files: `csrc/rocm/skinny_gemms_int4.cu`, `csrc/rocm/torch_bindings.cpp`, `tests/kernels/quantization/test_rdna_hybrid_w4a16.py`, `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`_
- **2026-09-14** [`23cfaad497`](https://github.com/vllm-project/vllm/commit/23cfaad497) [#56763](https://github.com/vllm-project/vllm/pull/56763)
  [CI] Update entrypoints CI (#56763)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`_
- **2026-09-14** [`78e84261ab`](https://github.com/vllm-project/vllm/commit/78e84261ab) [#48498](https://github.com/vllm-project/vllm/pull/48498)
  [Performance] Add Triton kernel for Gemma3n sparse GELU (#48498)
  _Files: `benchmarks/kernels/benchmark_gelu_and_mul_sparse.py`, `tests/compile/passes/ir/test_lowering.py`, `tests/compile/test_aot_compile.py`, `tests/kernels/ir/test_activation.py` _+11 more__
- **2026-09-14** [`cf1584f373`](https://github.com/vllm-project/vllm/commit/cf1584f373) [#56741](https://github.com/vllm-project/vllm/pull/56741)
  [Refactor] Normalize DeepSeek V4.1 model package naming (#56741)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.github/mergify.yml`, `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/core/test_fused_q_kv_rmsnorm.py` _+40 more__
- **2026-09-14** [`dfa1984e58`](https://github.com/vllm-project/vllm/commit/dfa1984e58) [#55235](https://github.com/vllm-project/vllm/pull/55235)
  [ROCm][Perf] Tune MiniMax-M3 decode top-k for short contexts (#55235)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/amd/ops/index_topk.py`_

## MoE / Expert Parallel  (48 commits)

- **2026-09-21** [`0b7f11a1ee`](https://github.com/vllm-project/vllm/commit/0b7f11a1ee) [#45635](https://github.com/vllm-project/vllm/pull/45635)
  [AuxOutput] Add block-keyed storage for routed-expert outputs (#45635)
  _Files: `tests/config/test_aux_output_config.py`, `tests/distributed/aux_output_connector/test_store.py`, `tests/entrypoints/openai/test_return_routed_experts.py`, `tests/entrypoints/scale_out/token_in_token_out/test_return_routed_experts.py` _+28 more__
- **2026-09-21** [`6654bcbfca`](https://github.com/vllm-project/vllm/commit/6654bcbfca) [#57277](https://github.com/vllm-project/vllm/pull/57277)
  [MRV2][XPU] use xpu sample kernel in mrv2 sampler (#57277)
  _Files: `vllm/v1/sample/ops/topk_topp_sampler.py`, `vllm/v1/watermarking/gpu_sampler.py`, `vllm/v1/worker/gpu/sample/sampler.py`_
- **2026-09-21** [`a15dbbd63d`](https://github.com/vllm-project/vllm/commit/a15dbbd63d) [#57855](https://github.com/vllm-project/vllm/pull/57855)
  [XPU][CI] fallback to 7-args of moe_align_block_size (#57855)
  _Files: `vllm/_custom_ops.py`_
- **2026-09-20** [`7d99c2c4fd`](https://github.com/vllm-project/vllm/commit/7d99c2c4fd) [#56685](https://github.com/vllm-project/vllm/pull/56685)
  [Feature][Humming] Humming feature integration (#56685)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `csrc/libtorch_stable/moe/moe_align_sum_kernels.cu`, `csrc/libtorch_stable/moe/moe_ops.h`, `csrc/libtorch_stable/moe/moe_permute_unpermute_op.cu` _+58 more__
- **2026-09-20** [`9b2f34cad4`](https://github.com/vllm-project/vllm/commit/9b2f34cad4) [#57784](https://github.com/vllm-project/vllm/pull/57784)
  [Feature] support bf16 MoE router and mxfp4 MoE for MiMo V2 (#57784)
  _Files: `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/model_executor/models/qwen3_dflash.py`_
- **2026-09-20** [`bf01fc4a31`](https://github.com/vllm-project/vllm/commit/bf01fc4a31) [#57546](https://github.com/vllm-project/vllm/pull/57546)
  [GLM-5.3-Flash] Route kpool indexer top-k through the shared   SparseIndexerTopk dispatcher (#57546)
  _Files: `tests/kernels/test_top_k_per_row.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/model_executor/layers/indexer_topk.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`_
- **2026-09-20** [`e5fce7b56b`](https://github.com/vllm-project/vllm/commit/e5fce7b56b) [#57421](https://github.com/vllm-project/vllm/pull/57421)
  [Core][Kernel] Share persistent workspaces for Marlin and Humming (#57421)
  _Files: `tests/kernels/moe/test_moe.py`, `tests/kernels/moe/test_moe_permute_unpermute.py`, `tests/kernels/quantization/test_marlin_gemm.py`, `tests/kernels/quantization/test_marlin_tile_padding.py` _+17 more__
- **2026-09-19** [`674b6d95d6`](https://github.com/vllm-project/vllm/commit/674b6d95d6) [#57641](https://github.com/vllm-project/vllm/pull/57641)
  [CI][Bugfix] Fix MoE reprocess test mock after #57405's kernel refactor (#57641)
  _Files: `tests/kernels/moe/test_flashinfer.py`_
- **2026-09-18** [`50d812b66a`](https://github.com/vllm-project/vllm/commit/50d812b66a) [#57604](https://github.com/vllm-project/vllm/pull/57604)
  [Perf][DSV4.1] Optimize MegaMoE staging and NVFP4 cache gathers (#57604)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/ops/prepare_megamoe.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py` _+1 more__
- **2026-09-18** [`8a5cf54387`](https://github.com/vllm-project/vllm/commit/8a5cf54387) [#57576](https://github.com/vllm-project/vllm/pull/57576)
  [Multimodal] Type dummy options per modality (#57576)
  _Files: `tests/models/multimodal/processing/test_audioflamingo3.py`, `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_molmo2.py`, `tests/models/multimodal/processing/test_qwen3_vl.py` _+89 more__
- **2026-09-18** [`017dced6a6`](https://github.com/vllm-project/vllm/commit/017dced6a6) [#57465](https://github.com/vllm-project/vllm/pull/57465)
  [DeepSeek V4] Fix fused MoE expert distribution (#57465)
  _Files: `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-09-18** [`dbf4b89cf2`](https://github.com/vllm-project/vllm/commit/dbf4b89cf2) [#57556](https://github.com/vllm-project/vllm/pull/57556)
  [Misc] Remove unnecessary Transformers version guards (#57556)
  _Files: `tests/basic_correctness/test_basic_correctness.py`, `tests/lora/test_qwenvl.py`, `tests/models/language/generation/test_common.py`, `tests/models/multimodal/generation/test_common.py` _+7 more__
- **2026-09-18** [`1cdf1689e5`](https://github.com/vllm-project/vllm/commit/1cdf1689e5) [#53162](https://github.com/vllm-project/vllm/pull/53162)
  [Quantization][XPU] Enable int8_w8a8 MoE on the Triton backend for XPU (#53162)
  _Files: `tests/quantization/test_int8_moe_oracle.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`_
- **2026-09-18** [`911548247a`](https://github.com/vllm-project/vllm/commit/911548247a) [#52101](https://github.com/vllm-project/vllm/pull/52101)
  [Distributed][MoonEP] BF16 integration of MoonEP balanced EP backend (#52101)
  _Files: `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-moonep.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/config-b200.txt`, `tests/evals/gsm8k/test_gsm8k_correctness.py`, `tests/kernels/moe/test_moonep_bf16_poc.py` _+11 more__
- **2026-09-18** [`04a3a00eb7`](https://github.com/vllm-project/vllm/commit/04a3a00eb7) [#57361](https://github.com/vllm-project/vllm/pull/57361)
  [CI] Raise GSM8K startup max wait to 2400s for flaky 30B+ MoE eval configs (#57361)
  _Files: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP2-PCP2-EP.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-AutoFp8-deepgemm-deepep-ll.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-Fp8-CT-Block-deepgemm-deepep-ll.yaml`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-NvFp4-CT-fi-cutedsl-deepep-ll.yaml` _+1 more__
- **2026-09-18** [`b346479065`](https://github.com/vllm-project/vllm/commit/b346479065) [#49942](https://github.com/vllm-project/vllm/pull/49942)
  [CPU] Add CPU FP8 W8A8 linear/MoE support (#49942)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_attn.cpp`, `csrc/cpu/cpu_isa.cpp`, `csrc/cpu/sgl-kernels/common.h` _+16 more__
- **2026-09-18** [`6df2b1a8c6`](https://github.com/vllm-project/vllm/commit/6df2b1a8c6) [#48606](https://github.com/vllm-project/vllm/pull/48606)
  [Quantization] Support native Quark W4A16 INT4/UINT4 exports in vLLM (#48606)
  _Files: `tests/quantization/test_quark.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`, `vllm/model_executor/layers/quantization/auto_awq.py` _+5 more__
- **2026-09-18** [`2bbdfcfcfe`](https://github.com/vllm-project/vllm/commit/2bbdfcfcfe) [#57327](https://github.com/vllm-project/vllm/pull/57327)
  [Perf][GLM5.3-Flash] Use cooperative top-k for small GLM decode batches (#57327)
  _Files: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`_
- **2026-09-17** [`ac78445bc9`](https://github.com/vllm-project/vllm/commit/ac78445bc9) [#57405](https://github.com/vllm-project/vllm/pull/57405)
  [MoE] Encapsulate TRT-LLM BF16 weight layout handling (#57405)
  _Files: `tests/kernels/moe/test_flashinfer.py`, `tests/kernels/moe/test_moe_weight_loading_padded.py`, `tests/kernels/moe/test_trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py` _+3 more__
- **2026-09-17** [`2b02c6c29b`](https://github.com/vllm-project/vllm/commit/2b02c6c29b) [#49819](https://github.com/vllm-project/vllm/pull/49819)
  [Model] Add Cohere2MoE Eagle3 auxiliary hidden states (#49819)
  _Files: `tests/v1/spec_decode/test_dflash_causality.py`, `vllm/model_executor/models/cohere2_moe.py`_
- **2026-09-17** [`ac2f0ea82c`](https://github.com/vllm-project/vllm/commit/ac2f0ea82c) [#56079](https://github.com/vllm-project/vllm/pull/56079)
  [MoE][Bugfix] Skip SP padded rows in grouped MoE routing (#56079)
  _Files: `tests/kernels/moe/test_grouped_topk.py`, `tests/kernels/moe/test_routing.py`, `tests/v1/worker/test_gpu_model_runner.py`, `tests/v1/worker/test_gpu_model_runner_v2.py` _+8 more__
- **2026-09-17** [`41f9104fa6`](https://github.com/vllm-project/vllm/commit/41f9104fa6) [#56266](https://github.com/vllm-project/vllm/pull/56266)
  [DSv4.1] Integrate Mega-Gate from DeepGEMM (#56266)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/test_mhc_kernels.py`, `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/dspark.py` _+5 more__
- **2026-09-17** [`b2f2bd71ba`](https://github.com/vllm-project/vllm/commit/b2f2bd71ba) [#57402](https://github.com/vllm-project/vllm/pull/57402)
  [CI][Bugfix] Add tp_shard_with_padding to padded MoE reload test mock (#57402)
  _Files: `tests/model_executor/model_loader/test_reload.py`_
- **2026-09-17** [`e960ead0aa`](https://github.com/vllm-project/vllm/commit/e960ead0aa) [#54320](https://github.com/vllm-project/vllm/pull/54320)
  [Mypy] Fix mypy typing for Transformers models (#54320)
  _Files: `tests/models/transformers/fusers/test_mla.py`, `tools/pre_commit/mypy.py`, `vllm/compilation/decorators.py`, `vllm/model_executor/models/transformers/__init__.py` _+12 more__
- **2026-09-17** [`861a299adc`](https://github.com/vllm-project/vllm/commit/861a299adc) [#57270](https://github.com/vllm-project/vllm/pull/57270)
  [Bugfix][Model Runner V2] Route dummy tokens to MoE experts during profiling (#57270)
  _Files: `tests/v1/worker/test_gpu_input_batch_v2.py`, `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-09-17** [`78fdf4efb8`](https://github.com/vllm-project/vllm/commit/78fdf4efb8) [#54699](https://github.com/vllm-project/vllm/pull/54699)
  [Bugfix][MoE] Convert FlashInfer BF16 weights in place (#54699)
  _Files: `tests/kernels/moe/test_flashinfer.py`, `tests/kernels/moe/test_moe_weight_loading_padded.py`, `tests/kernels/moe/test_trtllm_bf16_moe.py`, `tests/model_executor/model_loader/test_reload.py` _+5 more__
- **2026-09-17** [`117cf43fb6`](https://github.com/vllm-project/vllm/commit/117cf43fb6) [#55316](https://github.com/vllm-project/vllm/pull/55316)
  [HARDWARE][POWER] Enable W8A8 INT8 MoE on POWER (#55316)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_fused_moe_int8.cpp`, `csrc/cpu/cpu_types_vsx.hpp`, `csrc/cpu/micro_gemm/cpu_micro_gemm_int8_vsx.hpp` _+4 more__
- **2026-09-17** [`fe284ea17d`](https://github.com/vllm-project/vllm/commit/fe284ea17d) [#53914](https://github.com/vllm-project/vllm/pull/53914)
  [BugFxi] Fix DeepGEMM FP8 workspace over allocation (#53914)
  _Files: `tests/kernels/moe/test_deepgemm.py`, `vllm/model_executor/layers/fused_moe/deep_gemm_utils.py`, `vllm/model_executor/layers/fused_moe/experts/deep_gemm_moe.py`_
- **2026-09-17** [`2e50824766`](https://github.com/vllm-project/vllm/commit/2e50824766) [#48956](https://github.com/vllm-project/vllm/pull/48956)
  [Bugfix] Fall back to native sampling when FlashInfer cannot target the GPU (#48956)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_sampler.py`_
- **2026-09-17** [`08633cb5cd`](https://github.com/vllm-project/vllm/commit/08633cb5cd) [#55867](https://github.com/vllm-project/vllm/pull/55867)
  [Qwen3.8-Flash-Next] Enable FP8 TP with FlashInfer TRTLLM MoE (#55867)
  _Files: `tests/kernels/moe/test_fp8_tp_loading.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py` _+1 more__
- **2026-09-17** [`bd2d7ae7c1`](https://github.com/vllm-project/vllm/commit/bd2d7ae7c1) [#57268](https://github.com/vllm-project/vllm/pull/57268)
  [Perf] Reuse MoE workspace for DeepGEMM warmup (#57268)
  _Files: `vllm/model_executor/warmup/deep_gemm_warmup.py`_
- **2026-09-17** [`e6b1a5e5e3`](https://github.com/vllm-project/vllm/commit/e6b1a5e5e3) [#44987](https://github.com/vllm-project/vllm/pull/44987)
  [XPU] Enable XPU eplb (#44987)
  _Files: `tests/conftest.py`, `tests/distributed/eplb_utils.py`, `tests/distributed/test_elastic_ep.py`, `tests/distributed/test_eplb_algo.py` _+12 more__
- **2026-09-17** [`c38f92aae7`](https://github.com/vllm-project/vllm/commit/c38f92aae7) [#57236](https://github.com/vllm-project/vllm/pull/57236)
  [A2A] Allow EPLB + SharedExpert Overlap + DeepEPv2 (#57236)
  _Files: `vllm/distributed/device_communicators/all2all.py`, `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`_
- **2026-09-17** [`ed769b4a45`](https://github.com/vllm-project/vllm/commit/ed769b4a45) [#57210](https://github.com/vllm-project/vllm/pull/57210)
  [A2A] Add DeepEPv2 to SP Supported List (#57210)
  _Files: `vllm/config/parallel.py`, `vllm/model_executor/layers/fused_moe/all2all_utils.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_v2.py`_
- **2026-09-16** [`30b847c1fa`](https://github.com/vllm-project/vllm/commit/30b847c1fa) [#57204](https://github.com/vllm-project/vllm/pull/57204)
  [Perf][DSV4.1] Remove MegaMoE padding and shared padding workaround (#57204)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-09-16** [`0b9e018fb9`](https://github.com/vllm-project/vllm/commit/0b9e018fb9) [#53610](https://github.com/vllm-project/vllm/pull/53610)
  [MM] Further cleanup _apply_hf_processor_main (#53610)
  _Files: `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md`, `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/bailing_moe_v3_vl.py` _+70 more__
- **2026-09-16** [`e97ff80613`](https://github.com/vllm-project/vllm/commit/e97ff80613) [#54016](https://github.com/vllm-project/vllm/pull/54016)
  [BugFix][PCP] Handle missing DP metadata in one-sided EP (#54016)
  _Files: `vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_one_sided.py`_
- **2026-09-16** [`ceb87de065`](https://github.com/vllm-project/vllm/commit/ceb87de065) [#55988](https://github.com/vllm-project/vllm/pull/55988)
  [Misc] Remove no-op self-assignments across vLLM (#55988)
  _Files: `vllm/model_executor/layers/fused_moe/routed_experts.py`, `vllm/model_executor/models/deepencoder.py`, `vllm/model_executor/models/mimo_v2_omni.py`, `vllm/model_executor/models/step3p5.py`_
- **2026-09-16** [`03f67b3ad1`](https://github.com/vllm-project/vllm/commit/03f67b3ad1) [#56568](https://github.com/vllm-project/vllm/pull/56568)
  [Perf][DSV4.1] Pad shared experts for native MegaMoE fusion (#56568)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-09-16** [`8be5205abb`](https://github.com/vllm-project/vllm/commit/8be5205abb) [#56635](https://github.com/vllm-project/vllm/pull/56635)
  [Parser] Fix: correct parser frontend handling of reasoning end and boundary tokens (#56635)
  _Files: `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/engine/parser_engine.py`, `vllm/parser/glm47_moe.py`_
- **2026-09-15** [`c6fa1f05d1`](https://github.com/vllm-project/vllm/commit/c6fa1f05d1) [#56346](https://github.com/vllm-project/vllm/pull/56346)
  [Perf][Kernel] Add sampled filtering for persistent top-k (#56346)
  _Files: `benchmarks/kernels/benchmark_persistent_topk.py`, `csrc/libtorch_stable/persistent_topk.cuh`, `csrc/libtorch_stable/sampled_topk.cuh`, `csrc/libtorch_stable/topk.cu` _+1 more__
- **2026-09-15** [`0136df94b0`](https://github.com/vllm-project/vllm/commit/0136df94b0) [#56387](https://github.com/vllm-project/vllm/pull/56387)
  [Bugfix][Spec Decode][MoE] Avoid uninitialized EPLB state in DeepSeek V4.1 DSpark drafter (#56387)
  _Files: `tests/v1/worker/test_dspark_utils.py`, `vllm/v1/worker/gpu/spec_decode/dspark/utils.py`_
- **2026-09-15** [`4bac767695`](https://github.com/vllm-project/vllm/commit/4bac767695) [#52301](https://github.com/vllm-project/vllm/pull/52301)
  [Perf][Nemotron] Skip redundant latent-MoE all-reduce at TP>1 (~13% decode win) (#52301)
  _Files: `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`, `vllm/model_executor/models/nemotron_h.py`_
- **2026-09-15** [`24bfbd5d4d`](https://github.com/vllm-project/vllm/commit/24bfbd5d4d) [#56200](https://github.com/vllm-project/vllm/pull/56200)
  [Refactor] Derive is_reasoning_end from the engine grammar (#56200)
  _Files: `tests/parser/engine/test_gemma4_streaming_reasoning.py`, `tests/parser/engine/test_qwen3_reasoning.py`, `vllm/parser/deepseek_v32.py`, `vllm/parser/deepseek_v4.py` _+9 more__
- **2026-09-15** [`8263ea12bd`](https://github.com/vllm-project/vllm/commit/8263ea12bd) [#56876](https://github.com/vllm-project/vllm/pull/56876)
  [Build] Move DeepGEMM pin to the vLLM fork and update the Mega MoE call convention (#56876)
  _Files: `cmake/external_projects/deepgemm.cmake`, `docker/Dockerfile`, `tools/build_deepgemm_C.py`, `tools/install_deepgemm.sh` _+2 more__
- **2026-09-15** [`9d14fd3095`](https://github.com/vllm-project/vllm/commit/9d14fd3095) [#52781](https://github.com/vllm-project/vllm/pull/52781)
  [Kernel][MoE] DeepEP v2: async finalize to overlap shared experts with combine (#52781)
  _Files: `tests/kernels/moe/test_deepep_v2_async_finalize.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_v2.py`_
- **2026-09-14** [`79f0be21ff`](https://github.com/vllm-project/vllm/commit/79f0be21ff) [#56773](https://github.com/vllm-project/vllm/pull/56773)
  [Bugfix][CPU] Fix DeepSeek-R1 (FP8 MLA + MoE) correctness on CPU backend (#56773)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`, `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`_
- **2026-09-14** [`9f03b510c3`](https://github.com/vllm-project/vllm/commit/9f03b510c3) [#55914](https://github.com/vllm-project/vllm/pull/55914)
  [DSv4 Bug] fix dsv4 start up error `NotImplementedError: DeepSeek V4 MegaMoE currently requires expert parallel` (#55914)
  _Files: `vllm/config/speculative.py`_

## Attention  (43 commits)

- **2026-09-21** [`97dc6b19d2`](https://github.com/vllm-project/vllm/commit/97dc6b19d2) [#57885](https://github.com/vllm-project/vllm/pull/57885)
  [Perf][Attention] Avoid redundant sparse attention metadata operations (#57885)
  _Files: `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/attention/backends/mla/sparse_swa.py`_
- **2026-09-21** [`86ce4d10e2`](https://github.com/vllm-project/vllm/commit/86ce4d10e2) [#57811](https://github.com/vllm-project/vllm/pull/57811)
  [BUGFIX][HY4]  Record indexer completion event for full CUDA graph capture (#57811)
  _Files: `vllm/models/hy_v4/nvidia/attention.py`_
- **2026-09-20** [`f648eed23d`](https://github.com/vllm-project/vllm/commit/f648eed23d) [#56810](https://github.com/vllm-project/vllm/pull/56810)
  [Bugfix][KV Offload] Skip non-prefix-cacheable groups in SimpleCPUOffload (GLM-5.3-Flash kpool tail and QSA) (#56810)
  _Files: `tests/v1/simple_kv_offload/test_kv_events.py`, `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-09-20** [`1b9fa3eaa8`](https://github.com/vllm-project/vllm/commit/1b9fa3eaa8) [#57534](https://github.com/vllm-project/vllm/pull/57534)
  [Perf][GLM] Fuse the kpool tail slot mapping into one Triton kernel (#57534)
  _Files: `tests/v1/attention/test_kpool_tail_slot_mapping.py`, `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-09-20** [`db1bfdd4fb`](https://github.com/vllm-project/vllm/commit/db1bfdd4fb) [#57477](https://github.com/vllm-project/vllm/pull/57477)
  [Bugfix][GLM-5.3-Flash] Address kpool tail blocks by the padded indexer stride in the NVIDIA prefill seed kernel (#57477)
  _Files: `tests/kernels/test_kpool_decode_update_batched.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`_
- **2026-09-20** [`92b40f5a14`](https://github.com/vllm-project/vllm/commit/92b40f5a14) [#56045](https://github.com/vllm-project/vllm/pull/56045)
  [CPU][Perf] refactor paged attention for Arm CPUs (#56045)
  _Files: `csrc/cpu/cpu_attn_impl.hpp`, `csrc/cpu/cpu_attn_neon.hpp`, `csrc/cpu/cpu_attn_neon_bfmmla.hpp`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-09-20** [`a7fda4c88b`](https://github.com/vllm-project/vllm/commit/a7fda4c88b) [#49435](https://github.com/vllm-project/vllm/pull/49435)
  [Bugfix] Fix SM100 fp8_ds_mla cache scales (#49435)
  _Files: `csrc/libtorch_stable/cache_kernels.cu`, `csrc/libtorch_stable/fused_kimi_k3_mla_key_concat_kv_cache_kernel.cu`, `tests/kernels/attention/test_cache.py`, `tests/kernels/attention/test_flashmla_sparse.py` _+4 more__
- **2026-09-19** [`38537331d3`](https://github.com/vllm-project/vllm/commit/38537331d3) [#57667](https://github.com/vllm-project/vllm/pull/57667)
  [Bugfix][DSA] Avoid runtime JIT for offset candidate end buffers (#57667)
  _Files: `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`_
- **2026-09-19** [`038cb14bd7`](https://github.com/vllm-project/vllm/commit/038cb14bd7) [#57647](https://github.com/vllm-project/vllm/pull/57647)
  [CI][Bugfix] Correct the Laguna DFlash acceptance-length reference (#57647)
  _Files: `tests/v1/e2e/spec_decode/acceptance_rates/dflash/test_dflash.py`_
- **2026-09-18** [`62af3df734`](https://github.com/vllm-project/vllm/commit/62af3df734) [#57575](https://github.com/vllm-project/vllm/pull/57575)
  [Bugfix][MLA] Reserve sparse prefill buffers before KV cache sizing (#57575)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/models/hy_v4/nvidia/flashmla_sparse.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-09-18** [`2bdae2a5a8`](https://github.com/vllm-project/vllm/commit/2bdae2a5a8) [#57563](https://github.com/vllm-project/vllm/pull/57563)
  [fix] Mistral-Large-3 accuracy regression on `main` (#57563)
  _Files: `tests/transformers_utils/test_config.py`, `vllm/model_executor/models/AXK1.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/models/deepseek_v32/attention.py` _+4 more__
- **2026-09-18** [`32636580a6`](https://github.com/vllm-project/vllm/commit/32636580a6) [#51065](https://github.com/vllm-project/vllm/pull/51065)
  [Bugfix][MLA] TritonMLA: fix illegal memory access on causal multi-token decode (#51065)
  _Files: `tests/kernels/attention/test_triton_mla_causal_verify_flatten.py`, `vllm/v1/attention/backends/mla/triton_mla.py`_
- **2026-09-18** [`42a33039eb`](https://github.com/vllm-project/vllm/commit/42a33039eb) [#55190](https://github.com/vllm-project/vllm/pull/55190)
  [Perf] Fuse CohereASR relative attention score accumulation (#55190)
  _Files: `tests/models/multimodal/test_cohere_asr.py`, `vllm/model_executor/models/cohere_asr.py`_
- **2026-09-18** [`70df48dc3d`](https://github.com/vllm-project/vllm/commit/70df48dc3d) [#57317](https://github.com/vllm-project/vllm/pull/57317)
  [Bugfix][KV Cache][GLM-5.3-Flash] Disable slot mapping kernel for the kpool tail buffer (#57317)
  _Files: `tests/v1/attention/test_kpool_tail_slot_mapping.py`, `tests/v1/worker/test_gpu_kpool_tail_slot_mapping.py`, `vllm/v1/kv_cache_interface.py`_
- **2026-09-18** [`64563d0ec4`](https://github.com/vllm-project/vllm/commit/64563d0ec4) [#57454](https://github.com/vllm-project/vllm/pull/57454)
  [Bugfix][DSv4.1] Preserve NaN-scored candidate block indices (#57454)
  _Files: `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `vllm/model_executor/kernels/attention/dsa/candidate_blocks.py`_
- **2026-09-17** [`48f663c37f`](https://github.com/vllm-project/vllm/commit/48f663c37f) [#56431](https://github.com/vllm-project/vllm/pull/56431)
  [XPU] Fix incorrect context-key normalization for Qwen DFlash-based models (#56431)
  _Files: `vllm/model_executor/models/qwen3_dflash.py`_
- **2026-09-17** [`80447d2765`](https://github.com/vllm-project/vllm/commit/80447d2765) [#57432](https://github.com/vllm-project/vllm/pull/57432)
  [Bugfix][DSv4.1] Fix FlashInfer DSpark non-causal attention (#57432)
  _Files: `tests/v1/attention/test_dspark_noncausal_sparse_mla.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/v1/attention/backends/mla/sparse_swa.py`_
- **2026-09-17** [`db7a24c230`](https://github.com/vllm-project/vllm/commit/db7a24c230) [#55960](https://github.com/vllm-project/vllm/pull/55960)
  [Perf] Add fused DFlash2 grouped convolution (#55960)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `tests/v1/e2e/spec_decode/acceptance_rates/dflash/test_dflash.py`, `tests/v1/spec_decode/test_dflash2.py`, `vllm/model_executor/models/qwen3_dflash2.py`_
- **2026-09-17** [`9612f77077`](https://github.com/vllm-project/vllm/commit/9612f77077) [#56902](https://github.com/vllm-project/vllm/pull/56902)
  [Bugfix] Release stale FlashMLA workspace views after growth (#56902)
  _Files: `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-09-17** [`99ea5f525d`](https://github.com/vllm-project/vllm/commit/99ea5f525d) [#57334](https://github.com/vllm-project/vllm/pull/57334)
  [CI] Raise DSv4-Flash disaggregated engine readiness timeout to 1800s (#57334)
  _Files: `.buildkite/test_areas/disaggregated.yaml`_
- **2026-09-17** [`4e5ffda19d`](https://github.com/vllm-project/vllm/commit/4e5ffda19d) [#57285](https://github.com/vllm-project/vllm/pull/57285)
  [Bugfix] Isolate supplemental FlashInfer BF16 autotuning (#57285)
  _Files: `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/utils/flashinfer.py`_
- **2026-09-17** [`b3079e6e46`](https://github.com/vllm-project/vllm/commit/b3079e6e46) [#54674](https://github.com/vllm-project/vllm/pull/54674)
  [Perf][DSpark] Stack DeepSeek V4 context WKV projections (#54674)
  _Files: `tests/models/test_dspark_mla.py`, `vllm/models/deepseek_v4/nvidia/dspark.py`_
- **2026-09-17** [`9854b580df`](https://github.com/vllm-project/vllm/commit/9854b580df) [#56799](https://github.com/vllm-project/vllm/pull/56799)
  [Bugfix][KV Offload] Compact canonical MLA rows (#56799)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/config.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py`_
- **2026-09-16** [`9f9e1dac26`](https://github.com/vllm-project/vllm/commit/9f9e1dac26) [#57152](https://github.com/vllm-project/vllm/pull/57152)
  [Bugfix][Model] Restore causal image SWA for DeepSeek V4.1 (#57152)
  _Files: `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` _+4 more__
- **2026-09-16** [`6a2fdf9ac6`](https://github.com/vllm-project/vllm/commit/6a2fdf9ac6) [#56034](https://github.com/vllm-project/vllm/pull/56034)
  [Model] Optimize Sarvam MLA routing and preserve FP32 router logits (#56034)
  _Files: `vllm/model_executor/models/sarvam.py`_
- **2026-09-16** [`5f203baedb`](https://github.com/vllm-project/vllm/commit/5f203baedb) [#57141](https://github.com/vllm-project/vllm/pull/57141)
  [Docs] Split slash-combined docstring parameters (#57141)
  _Files: `vllm/_custom_ops.py`, `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`, `vllm/utils/deep_gemm.py`_
- **2026-09-16** [`f37c550bf6`](https://github.com/vllm-project/vllm/commit/f37c550bf6) [#56538](https://github.com/vllm-project/vllm/pull/56538)
  [Feature][Frontend] Expose effective attention block size for DCP (#56538)
  _Files: `docs/serving/context_parallel_deployment.md`, `rust/Cargo.toml`, `rust/proto/README.md`, `rust/proto/control.proto` _+14 more__
- **2026-09-15** [`031f5810c1`](https://github.com/vllm-project/vllm/commit/031f5810c1) [#56545](https://github.com/vllm-project/vllm/pull/56545)
  [Build][NVIDIA] Update public Rubin dependencies and MSA compatibility (#56545)
  _Files: `cmake/external_projects/fmha_sm100.cmake`, `docker/Dockerfile`, `requirements/rubin-prerelease.txt`_
- **2026-09-15** [`0fefffc934`](https://github.com/vllm-project/vllm/commit/0fefffc934) [#50494](https://github.com/vllm-project/vllm/pull/50494)
  [KVConnector][NIXL] Support attention-HMA layouts in pipeline-parallel push prefill (#50494)
  _Files: `docs/design/nixl_kv_push_connector.md`, `docs/features/nixl_connector_compatibility.md`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py` _+4 more__
- **2026-09-15** [`1257512305`](https://github.com/vllm-project/vllm/commit/1257512305) [#56254](https://github.com/vllm-project/vllm/pull/56254)
  [DSA] Wire DeepGEMM sparse MQA logits into the DeepSeek V4.1 indexer (#56254)
  _Files: `tests/kernels/test_fused_indexer_q_rope_quant.py`, `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `vllm/config/attention.py`, `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py` _+9 more__
- **2026-09-15** [`f2aad6aa70`](https://github.com/vllm-project/vllm/commit/f2aad6aa70) [#56888](https://github.com/vllm-project/vllm/pull/56888)
  [MRV2] Buffer util simplifications (#56888)
  _Files: `tests/utils_/test_torch_utils.py`, `tests/v1/attention/test_indexer_dcp_localize.py`, `tests/v1/worker/test_gpu_pcp_manager.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+17 more__
- **2026-09-15** [`df42d112ee`](https://github.com/vllm-project/vllm/commit/df42d112ee) [#57041](https://github.com/vllm-project/vllm/pull/57041)
  [Config] Infer HiSparse attention config from HiSparseConnector (#57041)
  _Files: `tests/test_config.py`, `vllm/config/attention.py`, `vllm/config/vllm.py`_
- **2026-09-15** [`241e9391ed`](https://github.com/vllm-project/vllm/commit/241e9391ed) [#55879](https://github.com/vllm-project/vllm/pull/55879)
  [Bugfix][Attention] Stabilize sparse-MLA DCP for GLM PCP evals (#55879)
  _Files: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-DCP4-EP.yaml`, `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP2-PCP2-EP.yaml`, `tests/v1/attention/test_dcp_a2a_pack_mask.py`, `tests/v1/attention/test_flashinfer_sparse_mla_workspace.py` _+6 more__
- **2026-09-15** [`836bb3839f`](https://github.com/vllm-project/vllm/commit/836bb3839f) [#56969](https://github.com/vllm-project/vllm/pull/56969)
  [Bugfix] Prevent out-of-bounds access in FlashInfer SM90 sparse MLA mixed batches (#56969)
  _Files: `tests/v1/attention/test_flashinfer_mla_sparse_sm90.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse_sm90.py`_
- **2026-09-15** [`51918e252a`](https://github.com/vllm-project/vllm/commit/51918e252a) [#56825](https://github.com/vllm-project/vllm/pull/56825)
  [Bugfix][SparseMLA] Fix piecewise cudagraph capture crash in index group (#56825)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/forward_context.py`, `vllm/v1/attention/backends/mla/index_group.py`, `vllm/v1/hisparse/runtime.py`_
- **2026-09-14** [`3bb0a03f35`](https://github.com/vllm-project/vllm/commit/3bb0a03f35) [#52228](https://github.com/vllm-project/vllm/pull/52228)
  [Model Runner V2] Acceptance estimation for adaptive verification (#52228)
  _Files: `tests/v1/spec_decode/test_acceptance_estimator.py`, `tests/v1/worker/test_gpu_autoregressive_speculator.py`, `tests/v1/worker/test_gpu_extract_hidden_states_speculator.py`, `vllm/config/speculative.py` _+5 more__
- **2026-09-14** [`7702ee87db`](https://github.com/vllm-project/vllm/commit/7702ee87db) [#55538](https://github.com/vllm-project/vllm/pull/55538)
  [Bugfix][DSA] Write nvfp4_ds_mla from the fused norm+rope kernel (#55538)
  _Files: `csrc/libtorch_stable/nvfp4_ds_mla_cache_kernels.cu`, `tests/kernels/test_fused_deepseek_v32_norm_rope.py`, `vllm/models/deepseek_v32/attention.py`, `vllm/models/deepseek_v32/common/kernels.py`_
- **2026-09-14** [`435c96f9db`](https://github.com/vllm-project/vllm/commit/435c96f9db) [#55624](https://github.com/vllm-project/vllm/pull/55624)
  [V1][Metrics] Support Sliding Window Attention (SWA) and hybrid layers in MFU/MBU estimation (#55624)
  _Files: `tests/v1/metrics/test_perf_metrics.py`, `vllm/v1/metrics/perf.py`_
- **2026-09-14** [`4be3dcf0fc`](https://github.com/vllm-project/vllm/commit/4be3dcf0fc) [#56722](https://github.com/vllm-project/vllm/pull/56722)
  [PCP][DCP] Declare FlashMLASparse MTP support at CP interleave > 1 (#56722)
  _Files: `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-09-14** [`e0c04c7b4d`](https://github.com/vllm-project/vllm/commit/e0c04c7b4d) [#53696](https://github.com/vllm-project/vllm/pull/53696)
  [Bugfix][Models] Fix OpenPangu sleep mode with static sinks (#53696)
  _Files: `vllm/model_executor/layers/attention/static_sink_attention.py`, `vllm/model_executor/models/openpangu.py`_
- **2026-09-14** [`3f55ad2f07`](https://github.com/vllm-project/vllm/commit/3f55ad2f07) [#55309](https://github.com/vllm-project/vllm/pull/55309)
  [Qwen3.8-Flash-Next] Fuse PLE residual and QSA output gate (#55309)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/models/qwen4_exp/nvidia/model.py`, `vllm/models/qwen4_exp/nvidia/ops/ple.py` _+3 more__
- **2026-09-14** [`238cb2b191`](https://github.com/vllm-project/vllm/commit/238cb2b191) [#55738](https://github.com/vllm-project/vllm/pull/55738)
  [Perf][GLM-5.3-Flash] Dense/masked-MHA sparse prefill for the NoPE (256, 0, 256) layout + skip the NoPE K concat (#55738)
  _Files: `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_mla_prefill_selector.py`, `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+2 more__
- **2026-09-14** [`b443c1cc4e`](https://github.com/vllm-project/vllm/commit/b443c1cc4e) [#55737](https://github.com/vllm-project/vllm/pull/55737)
  [Perf][GLM-5.3-Flash] Use FlashKDA for KDA chunked prefill (1.7-3.8x faster than the Triton chunk path) (#55737)
  _Files: `vllm/models/glm5next/nvidia/kda.py`_

## Other  (40 commits)

- **2026-09-21** [`15859bb3a1`](https://github.com/vllm-project/vllm/commit/15859bb3a1) [#57545](https://github.com/vllm-project/vllm/pull/57545)
  [Test] Organize structured output utility tests (#57545)
  _Files: `tests/v1/structured_output/test_utils.py`_
- **2026-09-21** [`3c84ad13ed`](https://github.com/vllm-project/vllm/commit/3c84ad13ed) [#48416](https://github.com/vllm-project/vllm/pull/48416)
  [Bugfix] Fix xgrammar feature gate bypass when JSON Schema type is a list (#48416)
  _Files: `tests/v1/structured_output/test_utils.py`, `tests/v1/structured_output/test_validation.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-09-21** [`8ec00ec2bc`](https://github.com/vllm-project/vllm/commit/8ec00ec2bc) [#57868](https://github.com/vllm-project/vllm/pull/57868)
  [Tests] Release HF embedding weights after prompt extraction (#57868)
  _Files: `tests/models/language/generation/test_common.py`_
- **2026-09-21** [`3df4ae153e`](https://github.com/vllm-project/vllm/commit/3df4ae153e) [#57783](https://github.com/vllm-project/vllm/pull/57783)
  [Core][KDA] Generalize Mamba prefill checkpoint builder and exporter (#57783)
  _Files: `tests/models/kimi_k3/test_kda.py`, `vllm/model_executor/layers/mamba/checkpoint.py`, `vllm/model_executor/layers/mamba/kda_checkpoint.py`, `vllm/models/kimi_k3/nvidia/kda.py` _+1 more__
- **2026-09-20** [`1c3ef2ad4c`](https://github.com/vllm-project/vllm/commit/1c3ef2ad4c) [#57591](https://github.com/vllm-project/vllm/pull/57591)
  [XPU][UT]Fix test_mnnvl_alltoall device and distributed backend (#57591)
  _Files: `tests/distributed/test_mnnvl_alltoall.py`, `tests/utils.py`_
- **2026-09-20** [`f4fc5aae7f`](https://github.com/vllm-project/vllm/commit/f4fc5aae7f) [#57581](https://github.com/vllm-project/vllm/pull/57581)
  [XPU][UT]Using the device_control_env_var to restrict visible device on different platform (#57581)
  _Files: `tests/distributed/test_multiproc_executor.py`_
- **2026-09-19** [`133b71e0be`](https://github.com/vllm-project/vllm/commit/133b71e0be) [#52500](https://github.com/vllm-project/vllm/pull/52500)
  [Bugfix] Take padded path for ragged decode batches in sparse_attn_indexer (#52500)
  _Files: `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-09-19** [`a5a30471ff`](https://github.com/vllm-project/vllm/commit/a5a30471ff) [#55928](https://github.com/vllm-project/vllm/pull/55928)
  [Tests] Cover get_unhashed_block_ids_all_groups (#55928)
  _Files: `tests/v1/core/test_prefix_caching.py`_
- **2026-09-19** [`c3b4844634`](https://github.com/vllm-project/vllm/commit/c3b4844634) [#57669](https://github.com/vllm-project/vllm/pull/57669)
  [Docs] Explain pointer-alignment JIT specialization in Triton skill (#57669)
  _Files: `.agents/skills/triton-kernel-writing/SKILL.md`_
- **2026-09-17** [`6a344d8c85`](https://github.com/vllm-project/vllm/commit/6a344d8c85) [#54990](https://github.com/vllm-project/vllm/pull/54990)
  [Bugfix][Metrics] Do not log a 0.0% prefix cache hit rate before any query (#54990)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/metrics/loggers.py`_
- **2026-09-17** [`f3aa88d230`](https://github.com/vllm-project/vllm/commit/f3aa88d230) [#57098](https://github.com/vllm-project/vllm/pull/57098)
  [Kimi K3 Bug] Fix kimi k3 reasoning parser (#57098)
  _Files: `vllm/reasoning/kimi_k3_reasoning_parser.py`_
- **2026-09-17** [`6a7de3ba3a`](https://github.com/vllm-project/vllm/commit/6a7de3ba3a) [#53864](https://github.com/vllm-project/vllm/pull/53864)
  [Bugfix][GDN] Fix CuteDSL BF16 KKT inversion divergence (#53864)
  _Files: `tests/kernels/mamba/test_gdn_prefill_cutedsl.py`, `vllm/model_executor/layers/mamba/ops/gdn_chunk_cutedsl/kernel_kkt_inv_uw.py`_
- **2026-09-17** [`75c71390d5`](https://github.com/vllm-project/vllm/commit/75c71390d5) [#48115](https://github.com/vllm-project/vllm/pull/48115)
  [Bugfix] Escape control characters in xgrammar choice grammar (#48115)
  _Files: `tests/v1/structured_output/test_utils.py`, `vllm/v1/structured_output/utils.py`_
- **2026-09-17** [`0ef8366ba3`](https://github.com/vllm-project/vllm/commit/0ef8366ba3) [#57357](https://github.com/vllm-project/vllm/pull/57357)
  [Frontend] Only show the summary line of config docstrings in `--help` (#57357)
  _Files: `tests/utils_/test_argparse_utils.py`, `vllm/utils/argparse_utils.py`_
- **2026-09-17** [`a85dd55177`](https://github.com/vllm-project/vllm/commit/a85dd55177) [#57189](https://github.com/vllm-project/vllm/pull/57189)
  Fix Laguna patch mutating flat RoPE parameters (#57189)
  _Files: `tests/test_config.py`, `vllm/transformers_utils/config.py`_
- **2026-09-17** [`91a4c40b45`](https://github.com/vllm-project/vllm/commit/91a4c40b45) [#56609](https://github.com/vllm-project/vllm/pull/56609)
  [Compile] Fix compile warning #177-D (#56609)
  _Files: `csrc/libtorch_stable/cache_kernels.cu`_
- **2026-09-17** [`b1f9ebc0c3`](https://github.com/vllm-project/vllm/commit/b1f9ebc0c3) [#57127](https://github.com/vllm-project/vllm/pull/57127)
  [Test][Core] Add hybrid model prefix cache hit-rate coverage (#57127)
  _Files: `tests/v1/core/prefix_cache/test_hybrid_prefix_cache_hit_rate.py`_
- **2026-09-17** [`a615f53364`](https://github.com/vllm-project/vllm/commit/a615f53364) [#57070](https://github.com/vllm-project/vllm/pull/57070)
  [Bugfix][Metrics][MFU] Size activation traffic from the model dtype (#57070)
  _Files: `tests/v1/metrics/test_perf_metrics.py`, `vllm/v1/metrics/perf.py`_
- **2026-09-16** [`8c1557a79c`](https://github.com/vllm-project/vllm/commit/8c1557a79c) [#52136](https://github.com/vllm-project/vllm/pull/52136)
  Add `pydocstyle` to the `ruff` rules (#52136)
- **2026-09-16** [`f8b5c11468`](https://github.com/vllm-project/vllm/commit/f8b5c11468) [#51483](https://github.com/vllm-project/vllm/pull/51483)
  [Bugfix][Kimi-K3] Do not classify a stateless first chunk as a decode (#51483)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`_
- **2026-09-16** [`3bb7826214`](https://github.com/vllm-project/vllm/commit/3bb7826214) [#56883](https://github.com/vllm-project/vllm/pull/56883)
  [Agent] Add agent instructions for parser directories (#56883)
  _Files: `vllm/parser/AGENTS.md`, `vllm/parser/CLAUDE.md`, `vllm/reasoning/AGENTS.md`, `vllm/reasoning/CLAUDE.md` _+2 more__
- **2026-09-16** [`82731931ae`](https://github.com/vllm-project/vllm/commit/82731931ae) [#54923](https://github.com/vllm-project/vllm/pull/54923)
  [Bugfix][CPU] Fall back to CpuPlatform when zentorch fails to import (#54923)
  _Files: `tests/test_zen_cpu_platform_detection.py`, `vllm/platforms/__init__.py`_
- **2026-09-16** [`f30a195bbb`](https://github.com/vllm-project/vllm/commit/f30a195bbb) [#57050](https://github.com/vllm-project/vllm/pull/57050)
  [Bugfix] Fix incorrect Mamba block allocation estimate that prevents request admission (#57050)
  _Files: `tests/v1/core/test_single_type_kv_cache_manager.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-09-16** [`323a29d8f2`](https://github.com/vllm-project/vllm/commit/323a29d8f2) [#55451](https://github.com/vllm-project/vllm/pull/55451)
  [Bugfix] Unreadable `prompt_embeds` payload should be a 400, not a 500 (#55451)
  _Files: `tests/renderers/test_prompt_embeds_payload_validation.py`, `tests/renderers/test_sparse_tensor_concurrent_race.py`, `tests/renderers/test_sparse_tensor_validation.py`, `vllm/renderers/embed_utils.py`_
- **2026-09-16** [`4ace5cd9d8`](https://github.com/vllm-project/vllm/commit/4ace5cd9d8) [#50097](https://github.com/vllm-project/vllm/pull/50097)
  [XPU] fix_test_worker_memory_snapshot_for_xpu (#50097)
  _Files: `tests/v1/worker/test_worker_memory_snapshot.py`_
- **2026-09-16** [`0673de9800`](https://github.com/vllm-project/vllm/commit/0673de9800) [#57033](https://github.com/vllm-project/vllm/pull/57033)
  [Rust Frontend][Metrics] Add per-request preemption histogram (#57033)
  _Files: `rust/src/llm/src/request_metrics.rs`, `rust/src/llm/tests/generate.rs`, `rust/src/metrics/src/request.rs`_
- **2026-09-16** [`b0898a4937`](https://github.com/vllm-project/vllm/commit/b0898a4937) [#41074](https://github.com/vllm-project/vllm/pull/41074)
  [Misc] Allow install empty package from pip (#41074)
  _Files: `setup.py`, `vllm/envs.py`_
- **2026-09-15** [`b6ce714354`](https://github.com/vllm-project/vllm/commit/b6ce714354) [#54098](https://github.com/vllm-project/vllm/pull/54098)
  [Bugfix] Format kernel-import errors eagerly so warning_once does not retain them (#54098)
  _Files: `vllm/platforms/cpu.py`, `vllm/platforms/cuda.py`, `vllm/platforms/interface.py`_
- **2026-09-15** [`cd10ed6f9f`](https://github.com/vllm-project/vllm/commit/cd10ed6f9f) [#42904](https://github.com/vllm-project/vllm/pull/42904)
  [feature] [xgrammar] support `patternProperties`/`propertyNames`/`unevaluatedProperties` kw for object types (#42904)
  _Files: `tests/v1/structured_output/test_utils.py`, `tests/v1/structured_output/test_validation.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-09-15** [`f84b0c4bce`](https://github.com/vllm-project/vllm/commit/f84b0c4bce) [#56908](https://github.com/vllm-project/vllm/pull/56908)
  [Model Runner V2] Tolerate lack of pinned memory support (#56908)
  _Files: `vllm/v1/worker/cpu/buffer_utils.py`, `vllm/v1/worker/gpu/buffer_utils.py`_
- **2026-09-15** [`567f745c1b`](https://github.com/vllm-project/vllm/commit/567f745c1b) [#56472](https://github.com/vllm-project/vllm/pull/56472)
  [Bugfix] Export weight-cache IPC tensors separately for each client (#56472)
  _Files: `vllm/model_executor/model_loader/weight_cache/daemon.py`_
- **2026-09-15** [`ceaa9f95dd`](https://github.com/vllm-project/vllm/commit/ceaa9f95dd) [#56899](https://github.com/vllm-project/vllm/pull/56899)
  [Minor] Invert MRV1 specdec method fallback logic (#56899)
  _Files: `vllm/config/vllm.py`_
- **2026-09-15** [`772e4f05fa`](https://github.com/vllm-project/vllm/commit/772e4f05fa) [#56915](https://github.com/vllm-project/vllm/pull/56915)
  [Bugfix][Rust] Fix HF multi-turn dataset integration (#56915)
  _Files: `rust/src/bench/src/datasets/multi_turn.rs`, `rust/src/bench/src/multi_turn.rs`_
- **2026-09-14** [`bbbd0a02c9`](https://github.com/vllm-project/vllm/commit/bbbd0a02c9) [#56382](https://github.com/vllm-project/vllm/pull/56382)
  [Bugfix] Carry over queued work when materializing the dedicated stream (#56382)
  _Files: `vllm/utils/torch_utils.py`_
- **2026-09-14** [`ba2ae9f239`](https://github.com/vllm-project/vllm/commit/ba2ae9f239) [#56666](https://github.com/vllm-project/vllm/pull/56666)
  [MRV2] Run pooling post processing on non-final PP ranks (#56666)
  _Files: `vllm/v1/worker/gpu_worker.py`_
- **2026-09-14** [`d320a21431`](https://github.com/vllm-project/vllm/commit/d320a21431) [#56866](https://github.com/vllm-project/vllm/pull/56866)
  [Bugfix][Rust Frontend] Restore prost test dependency (#56866)
  _Files: `rust/Cargo.lock`, `rust/src/server/Cargo.toml`_
- **2026-09-14** [`ff5f6d41b1`](https://github.com/vllm-project/vllm/commit/ff5f6d41b1) [#50894](https://github.com/vllm-project/vllm/pull/50894)
  [Bugfix] Scale KV page size for hidden states extraction with TP (#50894)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-09-14** [`dc89fdfb0e`](https://github.com/vllm-project/vllm/commit/dc89fdfb0e) [#56016](https://github.com/vllm-project/vllm/pull/56016)
  [CPU][Profiler] Group torch profiler tables by input shape when record_shapes is on (#56016)
  _Files: `vllm/profiler/wrapper.py`_
- **2026-09-14** [`dbf49dad11`](https://github.com/vllm-project/vllm/commit/dbf49dad11) [#56669](https://github.com/vllm-project/vllm/pull/56669)
  [Fast Start] Use GPU uuid as socket folder identifier (#56669)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py`, `vllm/model_executor/model_loader/weight_cache/protocol.py`_
- **2026-09-14** [`52dd0d7562`](https://github.com/vllm-project/vllm/commit/52dd0d7562) [#55468](https://github.com/vllm-project/vllm/pull/55468)
  [Fast Start] Fast loader support nnode>1 (#55468)
  _Files: `vllm/model_executor/model_loader/weight_cache/daemon.py`_

## Multimodal  (34 commits)

- **2026-09-21** [`c8824a1e42`](https://github.com/vllm-project/vllm/commit/c8824a1e42) [#57913](https://github.com/vllm-project/vllm/pull/57913)
  [MM] Move `supports_multimodal_inputs` and cache out of registry (#57913)
  _Files: `tests/config/test_multimodal_config.py`, `tests/entrypoints/generate/generative_scoring/test_generative_scoring.py`, `tests/entrypoints/openai/chat_completion/test_chat_error.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py` _+32 more__
- **2026-09-21** [`606d124b37`](https://github.com/vllm-project/vllm/commit/606d124b37) [#57234](https://github.com/vllm-project/vllm/pull/57234)
  [Bugfix][Multimodal] Tolerate malformed EXIF in Molmo 2 image preprocessing (#57234)
  _Files: `vllm/model_executor/models/molmo2.py`_
- **2026-09-21** [`7268f6e38e`](https://github.com/vllm-project/vllm/commit/7268f6e38e) [#57833](https://github.com/vllm-project/vllm/pull/57833)
  [Security] Prefer fresh multimodal payloads over a stale receiver cache (#57833)
  _Files: `tests/multimodal/test_cache.py`, `vllm/multimodal/cache.py`_
- **2026-09-21** [`9598487bc1`](https://github.com/vllm-project/vllm/commit/9598487bc1) [#53758](https://github.com/vllm-project/vllm/pull/53758)
  [Bugfix][Model] Mistral3: align placeholder grid with public processor (#53758)
  _Files: `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`_
- **2026-09-21** [`59f1527280`](https://github.com/vllm-project/vllm/commit/59f1527280) [#57769](https://github.com/vllm-project/vllm/pull/57769)
  [Bugfix] Fix Whisper engine crash on audio clips longer than 30s (#57769)
  _Files: `tests/models/multimodal/processing/test_whisper.py`, `vllm/model_executor/models/whisper.py`_
- **2026-09-21** [`ff0c885494`](https://github.com/vllm-project/vllm/commit/ff0c885494) [#57589](https://github.com/vllm-project/vllm/pull/57589)
  [Bugfix] DiffusionGemma: fix multimodal support (#57589)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-09-20** [`27b7757f63`](https://github.com/vllm-project/vllm/commit/27b7757f63) [#57076](https://github.com/vllm-project/vllm/pull/57076)
  [Bugfix][Frontend] Bound the prompt after multimodal expansion (#57076)
  _Files: `tests/renderers/test_truncate_after_mm_expansion.py`, `vllm/renderers/base.py`, `vllm/renderers/hf.py`_
- **2026-09-19** [`751f6807d9`](https://github.com/vllm-project/vllm/commit/751f6807d9) [#57674](https://github.com/vllm-project/vllm/pull/57674)
  [Refactor] Use dynamic MM cache in processor (#57674)
  _Files: `tests/models/multimodal/processing/test_audio_in_video.py`, `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_gemma4.py`, `tests/models/multimodal/processing/test_mllama4.py` _+19 more__
- **2026-09-19** [`a8d1aa9c99`](https://github.com/vllm-project/vllm/commit/a8d1aa9c99) [#54283](https://github.com/vllm-project/vllm/pull/54283)
  [Bugfix][Multimodal] Frame the multi-modal hash digest input (#54283)
  _Files: `tests/multimodal/test_hasher.py`, `tests/multimodal/test_processing.py`, `vllm/multimodal/hasher.py`_
- **2026-09-19** [`01c7bf8813`](https://github.com/vllm-project/vllm/commit/01c7bf8813) [#57487](https://github.com/vllm-project/vllm/pull/57487)
  [Bugfix][Model] Fix Aria expert weight names and layout (#57487)
  _Files: `tests/models/multimodal/test_aria.py`, `vllm/model_executor/models/aria.py`_
- **2026-09-19** [`9d75dd4544`](https://github.com/vllm-project/vllm/commit/9d75dd4544) [#57371](https://github.com/vllm-project/vllm/pull/57371)
  [CI] Deflake pooling shards with GPU teardown fixtures between tests (#57371)
  _Files: `tests/models/language/pooling/conftest.py`, `tests/models/language/pooling/test_colbert.py`, `tests/models/language/pooling/test_nomic_max_model_len.py`, `tests/models/language/pooling_mteb_test/conftest.py` _+1 more__
- **2026-09-18** [`2b8a5495a8`](https://github.com/vllm-project/vllm/commit/2b8a5495a8) [#54142](https://github.com/vllm-project/vllm/pull/54142)
  [Mypy] Fix mypy typing for N/O models (#54142)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/aimv2.py`, `vllm/model_executor/models/interfaces.py` _+15 more__
- **2026-09-18** [`cc09352e5c`](https://github.com/vllm-project/vllm/commit/cc09352e5c) [#56882](https://github.com/vllm-project/vllm/pull/56882)
  [Bugfix][Multimodal] Preserve DeepSeek V4 image block spacing (#56882)
  _Files: `tests/tokenizers_/fixtures/deepseek_v4/test_input_5.json`, `tests/tokenizers_/fixtures/deepseek_v4/test_output_5.txt`, `tests/tokenizers_/test_deepseek_v4.py`, `vllm/renderers/deepseek_v4.py` _+1 more__
- **2026-09-18** [`f2b6152ec2`](https://github.com/vllm-project/vllm/commit/f2b6152ec2) [#57359](https://github.com/vllm-project/vllm/pull/57359)
  [CI] Add flaky rerun markers / timeout skips to sibling tests lacking them (#57359)
  _Files: `tests/models/language/pooling/test_token_classification.py`, `tests/multimodal/media/test_connector.py`_
- **2026-09-18** [`67a8a3f926`](https://github.com/vllm-project/vllm/commit/67a8a3f926) [#57142](https://github.com/vllm-project/vllm/pull/57142)
  [Bugfix][CPU] Fix macOS multimodal SHM cache initialization (#57142)
  _Files: `tests/test_envs.py`, `vllm/envs.py`_
- **2026-09-17** [`092bdd6d57`](https://github.com/vllm-project/vllm/commit/092bdd6d57) [#44890](https://github.com/vllm-project/vllm/pull/44890)
  [Frontend][Core] Add release_kv_cache_memory() API (#44890)
  _Files: `docs/features/sleep_mode.md`, `rust/src/engine-core-client/src/client.rs`, `rust/src/mock-engine/src/engine.rs`, `rust/src/mock-engine/src/tests.rs` _+20 more__
- **2026-09-17** [`668d6c3a77`](https://github.com/vllm-project/vllm/commit/668d6c3a77) [#56316](https://github.com/vllm-project/vllm/pull/56316)
  [CI] Shard multimodal Processor 1->4 (#56316)
  _Files: `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-09-17** [`4f9a41ac94`](https://github.com/vllm-project/vllm/commit/4f9a41ac94) [#55953](https://github.com/vllm-project/vllm/pull/55953)
  [CI/Build][Hardware][NVIDIA] Add Rubin CUDA 13.4 nightly images (#55953)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/cleanup-nightly-builds.sh`, `docker/Dockerfile`, `tests/v1/engine/test_output_processor.py` _+2 more__
- **2026-09-17** [`0d72627565`](https://github.com/vllm-project/vllm/commit/0d72627565) [#57095](https://github.com/vllm-project/vllm/pull/57095)
  [Perf][EPD] Batch image requests per encoder (#57095)
  _Files: `examples/disaggregated/disaggregated_encoder/README.md`, `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/v1/ec_connector/unit/test_ec_example_connector.py`, `tests/v1/ec_connector/unit/test_epd_proxy_retry.py` _+2 more__
- **2026-09-17** [`de24e51908`](https://github.com/vllm-project/vllm/commit/de24e51908) [#56922](https://github.com/vllm-project/vllm/pull/56922)
  [MM][V2] Enable encoder-only ViT CUDA graph capture (#56922)
  _Files: `.buildkite/test_areas/disaggregated_mooncake.yaml`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py`, `tests/v1/ec_connector/integration/run_epd_mooncake_ec_full_pipeline.sh` _+3 more__
- **2026-09-17** [`2743dc4f92`](https://github.com/vllm-project/vllm/commit/2743dc4f92) [#56242](https://github.com/vllm-project/vllm/pull/56242)
  [Feature][Multimodal] Add cross-encoder caching to Mooncake P2P (#56242)
  _Files: `docs/features/cross_encoder_cache.md`, `docs/features/disagg_encoder.md`, `tests/v1/ec_connector/unit/test_cross_encoder_cache.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py` _+11 more__
- **2026-09-16** [`0983aef8da`](https://github.com/vllm-project/vllm/commit/0983aef8da) [#53187](https://github.com/vllm-project/vllm/pull/53187)
  [Frontend] Return prompt metadata from /inference/v1/generate (#53187)
  _Files: `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/inference/generate/convert.rs`, `rust/src/server/src/routes/inference/generate/types.rs`, `rust/src/server/src/routes/render.rs` _+5 more__
- **2026-09-16** [`403f182c02`](https://github.com/vllm-project/vllm/commit/403f182c02) [#56872](https://github.com/vllm-project/vllm/pull/56872)
  [MM] Keep raw pixels through dp-sharded ViT path (#56872)
  _Files: `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/model_executor/models/vision.py`_
- **2026-09-16** [`35f6047c1a`](https://github.com/vllm-project/vllm/commit/35f6047c1a) [#56912](https://github.com/vllm-project/vllm/pull/56912)
  [XPU][Bugfix] Fix Qwen2-Audio ValueError on audio clips longer than 30s (#56912)
  _Files: `vllm/model_executor/models/qwen2_audio.py`_
- **2026-09-16** [`9ca6dbba71`](https://github.com/vllm-project/vllm/commit/9ca6dbba71) [#56527](https://github.com/vllm-project/vllm/pull/56527)
  fix(multimodal): tolerate malformed EXIF metadata during hashing (#56527) (#56576)
  _Files: `tests/multimodal/test_hasher.py`, `vllm/multimodal/hasher.py`_
- **2026-09-16** [`af1c01499b`](https://github.com/vllm-project/vllm/commit/af1c01499b) [#56904](https://github.com/vllm-project/vllm/pull/56904)
  [Bugfix] Make GPU sync checks safe under torch.compile (#56904)
  _Files: `tests/models/multimodal/generation/test_voxtral_realtime.py`, `tests/utils_/test_gpu_sync_debug.py`, `vllm/utils/gpu_sync_debug.py`_
- **2026-09-15** [`1e47ec00d2`](https://github.com/vllm-project/vllm/commit/1e47ec00d2) [#56721](https://github.com/vllm-project/vllm/pull/56721)
  [Bugfix][Gemma 4] Don't read fft_length when profiling unified audio (#56721)
  _Files: `tests/models/multimodal/processing/test_gemma4_unified.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-09-15** [`8765952755`](https://github.com/vllm-project/vllm/commit/8765952755) [#56597](https://github.com/vllm-project/vllm/pull/56597)
  [CI/Build] Retry CPU image stream interruptions (#56597)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test.sh`_
- **2026-09-14** [`995e8581f4`](https://github.com/vllm-project/vllm/commit/995e8581f4) [#51167](https://github.com/vllm-project/vllm/pull/51167)
  [Model] Voxtral Realtime: add support for `CUDAGraphMode.FULL_DECODE_ONLY` (#51167)
  _Files: `tests/models/multimodal/generation/test_voxtral_realtime.py`, `vllm/model_executor/models/voxtral_realtime.py`, `vllm/model_executor/models/whisper_causal.py`_
- **2026-09-14** [`9d4d9aa5bc`](https://github.com/vllm-project/vllm/commit/9d4d9aa5bc) [#55071](https://github.com/vllm-project/vllm/pull/55071)
  [LoRA][Refactor] Unify multimodal LoRA token count hooks (#55071)
  _Files: `tests/models/multimodal/processing/test_llava_next_video.py`, `vllm/model_executor/models/blip2.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/gemma3_mm.py` _+19 more__
- **2026-09-14** [`7b1ea3f524`](https://github.com/vllm-project/vllm/commit/7b1ea3f524) [#56366](https://github.com/vllm-project/vllm/pull/56366)
  [Bugfix][Rust Frontend][Multimodal] Align DeepSeek V4.1 and Kimi K3 media with rendered placeholders (#56366)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/renderer/deepseek.rs`, `rust/src/chat/src/renderer/deepseek_v32/mod.rs` _+14 more__
- **2026-09-14** [`ea723c81c3`](https://github.com/vllm-project/vllm/commit/ea723c81c3) [#56729](https://github.com/vllm-project/vllm/pull/56729)
  [Security] Cap Qwen-VL video sampling knobs (#56729)
  _Files: `vllm/multimodal/video.py`_
- **2026-09-14** [`934b1fcbcb`](https://github.com/vllm-project/vllm/commit/934b1fcbcb) [#55176](https://github.com/vllm-project/vllm/pull/55176)
  [Frontend] Replace `VLLM_ENABLE_SCALE_OUT_ENDPOINTS` with `--enable-scale-out` (#55176)
  _Files: `docs/serving/online_serving/README.md`, `docs/serving/online_serving/derenderer.md`, `docs/serving/online_serving/renderer.md`, `docs/usage/security.md` _+20 more__
- **2026-09-14** [`a2685f2cda`](https://github.com/vllm-project/vllm/commit/a2685f2cda) [#54323](https://github.com/vllm-project/vllm/pull/54323)
  [Bugfix][Multimodal] Validate base64 video payloads, matching image and audio (#54323)
  _Files: `vllm/multimodal/media/video.py`_

## Scheduler / Engine  (29 commits)

- **2026-09-21** [`3918f3c5a3`](https://github.com/vllm-project/vllm/commit/3918f3c5a3) [#57460](https://github.com/vllm-project/vllm/pull/57460)
  [Profiler] Unify platform-aware torch profiling (#57460)
  _Files: `docs/contributing/profiling.md`, `tests/v1/engine/test_async_llm.py`, `tests/v1/worker/test_gpu_profiler.py`, `vllm/config/profiler.py` _+5 more__
- **2026-09-21** [`1185254851`](https://github.com/vllm-project/vllm/commit/1185254851) [#54581](https://github.com/vllm-project/vllm/pull/54581)
  [Bugfix][KV Connector] Propagate cache reset failure during sleep (#54581)
  _Files: `vllm/v1/engine/core.py`_
- **2026-09-20** [`10e6a7f210`](https://github.com/vllm-project/vllm/commit/10e6a7f210) [#43310](https://github.com/vllm-project/vllm/pull/43310)
  [Frontend] Expose per-request spec decode metrics in generate API (#43310)
  _Files: `rust/src/engine-core-client/src/protocol/output.rs`, `rust/src/llm/src/output.rs`, `rust/src/llm/tests/generate.rs`, `rust/src/server/src/routes/inference/generate.rs` _+8 more__
- **2026-09-19** [`5302d1fe40`](https://github.com/vllm-project/vllm/commit/5302d1fe40) [#56497](https://github.com/vllm-project/vllm/pull/56497)
  [Model Runner V2] Support custom logits processors (#56497)
  _Files: `docs/features/custom_logitsprocs.md`, `tests/test_config.py`, `tests/test_sampling_params.py`, `tests/v1/engine/test_input_processor_trace_replay.py` _+28 more__
- **2026-09-18** [`56cac80b14`](https://github.com/vllm-project/vllm/commit/56cac80b14) [#57520](https://github.com/vllm-project/vllm/pull/57520)
  [Deprecation] Remove assistant_token_mask support (#57520)
  _Files: `tests/entrypoints/scale_out/render/test_render.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/scale_out/render/serving.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py` _+3 more__
- **2026-09-18** [`a7156060c1`](https://github.com/vllm-project/vllm/commit/a7156060c1) [#53936](https://github.com/vllm-project/vllm/pull/53936)
  [Core] Make parallel sampling (n>1) reqs admission atomic (#53936)
  _Files: `tests/v1/engine/test_admission_control.py`, `vllm/v1/engine/async_llm.py`_
- **2026-09-18** [`5397f967b9`](https://github.com/vllm-project/vllm/commit/5397f967b9) [#56649](https://github.com/vllm-project/vllm/pull/56649)
  [CI] Add residual timeout headroom after JIT rollback (#56649)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/spec_decode.yaml`_
- **2026-09-18** [`95d723700b`](https://github.com/vllm-project/vllm/commit/95d723700b) [#56777](https://github.com/vllm-project/vllm/pull/56777)
  [Rust Frontend] Return sampling masks over gRPC (#56777)
  _Files: `rust/Cargo.lock`, `rust/proto/Cargo.toml`, `rust/proto/inference.proto`, `rust/src/chat/src/output/default/unified.rs` _+19 more__
- **2026-09-18** [`39e33db7f3`](https://github.com/vllm-project/vllm/commit/39e33db7f3) [#56271](https://github.com/vllm-project/vllm/pull/56271)
  [Frontend] Fix the parsing of missing `string=` in DeepSeek V4 (#56271)
  _Files: `rust/src/parser/src/tool/deepseek_dsml/deepseek_v32.rs`, `rust/src/parser/src/tool/deepseek_dsml/deepseek_v4.rs`, `rust/src/parser/src/tool/deepseek_dsml/deepseek_v41/tests.rs`, `rust/src/parser/src/tool/deepseek_dsml/mod.rs` _+4 more__
- **2026-09-18** [`dee37d8911`](https://github.com/vllm-project/vllm/commit/dee37d8911) [#56268](https://github.com/vllm-project/vllm/pull/56268)
  [Frontend] Add `--tool-strict-level` for server-side control for structural tag activation (#56268)
  _Files: `docs/features/tool_calling.md`, `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/chat/src/lib.rs` _+31 more__
- **2026-09-17** [`9ff08f9493`](https://github.com/vllm-project/vllm/commit/9ff08f9493) [#57269](https://github.com/vllm-project/vllm/pull/57269)
  [Bugfix] Honor skip_reading_prefix_cache for KV connector hits (#57269)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-09-17** [`23cd0346ce`](https://github.com/vllm-project/vllm/commit/23cd0346ce) [#53636](https://github.com/vllm-project/vllm/pull/53636)
  [CPU] Align scheduler and NIXL CPU affinity per local rank (#53636)
  _Files: `docs/getting_started/installation/cpu.md`, `vllm/platforms/cpu.py`, `vllm/utils/ompmultiprocessing.py`_
- **2026-09-17** [`2307a1d16c`](https://github.com/vllm-project/vllm/commit/2307a1d16c) [#57226](https://github.com/vllm-project/vllm/pull/57226)
  [Core] Don't issue a blocking collective RPC during engine handshake (#57226)
  _Files: `tests/v1/engine/test_engine_core_client.py`, `vllm/v1/engine/core.py`_
- **2026-09-17** [`f730a93d2b`](https://github.com/vllm-project/vllm/commit/f730a93d2b) [#56758](https://github.com/vllm-project/vllm/pull/56758)
  [Scheduler] Add --max-num-active-seqs to cap RUNNING admission (#56758)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `vllm/config/scheduler.py`, `vllm/engine/arg_utils.py` _+1 more__
- **2026-09-17** [`28ec03bc6e`](https://github.com/vllm-project/vllm/commit/28ec03bc6e) [#56533](https://github.com/vllm-project/vllm/pull/56533)
  [Bugfix][Rust Frontend] Accept appended EngineCoreOutput fields (#56533)
  _Files: `rust/src/engine-core-client/src/protocol/mod.rs`, `rust/src/engine-core-client/src/protocol/output.rs`, `rust/src/engine-core-client/src/protocol/serde_utils.rs`, `rust/src/engine-core-client/src/tests/client.rs` _+1 more__
- **2026-09-16** [`6c3d9816af`](https://github.com/vllm-project/vllm/commit/6c3d9816af) [#57104](https://github.com/vllm-project/vllm/pull/57104)
  [BugFix][KV Connector] Fix Deadlock with KVConnector + MTP under KV Pressure (#57104)
  _Files: `tests/v1/kv_connector/unit/test_remote_prefill_lifecycle.py`, `tests/v1/kv_connector/unit/utils.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-09-16** [`6b6bf6b3c3`](https://github.com/vllm-project/vllm/commit/6b6bf6b3c3) [#55702](https://github.com/vllm-project/vllm/pull/55702)
  [Bugfix] Remove unsupported comma-separated detailed trace values (#55702)
  _Files: `vllm/config/observability.py`, `vllm/engine/arg_utils.py`_
- **2026-09-16** [`42919b49c5`](https://github.com/vllm-project/vllm/commit/42919b49c5) [#54222](https://github.com/vllm-project/vllm/pull/54222)
  [P/D] Report prefill worker cache hits in prompt_tokens_details (#54222)
  _Files: `tests/v1/engine/test_output_processor.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/engine/output_processor.py`_
- **2026-09-16** [`903285fbcc`](https://github.com/vllm-project/vllm/commit/903285fbcc) [#52370](https://github.com/vllm-project/vllm/pull/52370)
  [Bugfix] Let an optional Literal flag accept the None it advertises (#52370)
  _Files: `tests/engine/test_arg_utils.py`, `vllm/engine/arg_utils.py`_
- **2026-09-16** [`118e17f5ff`](https://github.com/vllm-project/vllm/commit/118e17f5ff) [#48599](https://github.com/vllm-project/vllm/pull/48599)
  [Platform] Move env check function to platform interface (#48599)
  _Files: `vllm/engine/arg_utils.py`, `vllm/envs.py`, `vllm/platforms/interface.py`_
- **2026-09-16** [`622934e61f`](https://github.com/vllm-project/vllm/commit/622934e61f) [#56015](https://github.com/vllm-project/vllm/pull/56015)
  [XPU] Honor device_ids for worker device placement (#56015)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `vllm/v1/engine/core.py`, `vllm/v1/worker/xpu_worker.py`_
- **2026-09-16** [`c16bb6068f`](https://github.com/vllm-project/vllm/commit/c16bb6068f) [#51026](https://github.com/vllm-project/vllm/pull/51026)
  [Bugfix][Rust Frontend] Tolerate NaN-corrupted logprobs in engine-core (#51026)
  _Files: `rust/src/engine-core-client/src/protocol/logprobs.rs`, `rust/src/engine-core-client/src/protocol/logprobs/tests.rs`, `rust/src/server/src/routes/openai/utils/logprobs.rs`_
- **2026-09-16** [`bfd713bf8b`](https://github.com/vllm-project/vllm/commit/bfd713bf8b) [#56931](https://github.com/vllm-project/vllm/pull/56931)
  [Rust Frontend] Support HF config overrides `--hf-overrides` (#56931)
  _Files: `rust/Cargo.lock`, `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/cmd/Cargo.toml` _+12 more__
- **2026-09-15** [`f0fbc98c48`](https://github.com/vllm-project/vllm/commit/f0fbc98c48) [#54746](https://github.com/vllm-project/vllm/pull/54746)
  [Frontend] Share max_num_queued_reqs across API server processes (#54746)
  _Files: `tests/entrypoints/launchers/api_server/test_api_server_process_manager.py`, `tests/v1/engine/test_admission_control.py`, `vllm/v1/engine/admission_control.py`, `vllm/v1/engine/async_llm.py` _+2 more__
- **2026-09-15** [`78eaaad2c7`](https://github.com/vllm-project/vllm/commit/78eaaad2c7) [#56990](https://github.com/vllm-project/vllm/pull/56990)
  [Rust Frontend] Add iteration token histogram (#56990)
  _Files: `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/metrics.rs`, `rust/src/metrics/src/request.rs`, `rust/src/mock-engine/src/engine.rs` _+1 more__
- **2026-09-15** [`5be911ee87`](https://github.com/vllm-project/vllm/commit/5be911ee87) [#53124](https://github.com/vllm-project/vllm/pull/53124)
  [Bugfix] Load reasoning parser plugins before headless engine config (#53124)
  _Files: `tests/entrypoints/cli/test_serve.py`, `vllm/entrypoints/cli/serve.py`_
- **2026-09-15** [`84e5f3edac`](https://github.com/vllm-project/vllm/commit/84e5f3edac) [#56844](https://github.com/vllm-project/vllm/pull/56844)
  [Bugfix] Validate routed-expert prompt offsets before engine submission (#56844)
  _Files: `tests/test_request_input_bounds.py`, `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/engine/input_processor.py`_
- **2026-09-14** [`1713a09491`](https://github.com/vllm-project/vllm/commit/1713a09491) [#56338](https://github.com/vllm-project/vllm/pull/56338)
  [Rust Frontend] Forward per-request watermarking controls (#56338)
  _Files: `docs/features/watermarking.md`, `rust/proto/inference.proto`, `rust/src/engine-core-client/src/protocol/sampling.rs`, `rust/src/engine-core-client/src/tests/client.rs` _+10 more__
- **2026-09-14** [`214248c7d8`](https://github.com/vllm-project/vllm/commit/214248c7d8) [#56695](https://github.com/vllm-project/vllm/pull/56695)
  [CI] Move smaller H200 workloads to 18GB MIG slices (#56695)
  _Files: `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/samplers.yaml`_

## CI / Build  (28 commits)

- **2026-09-21** [`db7f1f6714`](https://github.com/vllm-project/vllm/commit/db7f1f6714) [#57889](https://github.com/vllm-project/vllm/pull/57889)
  [CI][XPU] Deselect Ray UT in XPU V1 test Job (#57889)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`_
- **2026-09-21** [`eb87980585`](https://github.com/vllm-project/vllm/commit/eb87980585) [#57554](https://github.com/vllm-project/vllm/pull/57554)
  [Build] Fix DeepGEMM CUDA 12.9 release builds (#57554)
  _Files: `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-09-20** [`708c2495c0`](https://github.com/vllm-project/vllm/commit/708c2495c0) [#57467](https://github.com/vllm-project/vllm/pull/57467)
  [Test][Core] Compute the expected hybrid prefix-cache hit instead of hard-coding it (#57467)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `tests/v1/core/prefix_cache/test_hybrid_prefix_cache_hit_rate.py`_
- **2026-09-19** [`729ebac498`](https://github.com/vllm-project/vllm/commit/729ebac498) [#57362](https://github.com/vllm-project/vllm/pull/57362)
  [CI] Reclaim GPU memory between model initialization tests (#57362)
  _Files: `tests/models/test_initialization.py`_
- **2026-09-18** [`5bb596201a`](https://github.com/vllm-project/vllm/commit/5bb596201a) [#57287](https://github.com/vllm-project/vllm/pull/57287)
  [CI] Raise Elastic EP Scaling step timeout 30m -> 40m (#57287)
  _Files: `.buildkite/test_areas/expert_parallelism.yaml`_
- **2026-09-17** [`f46968cb6e`](https://github.com/vllm-project/vllm/commit/f46968cb6e) [#57367](https://github.com/vllm-project/vllm/pull/57367)
  [CI] Make ci-clean-log.sh portable to macOS/BSD sed (#57367)
  _Files: `.buildkite/scripts/ci-clean-log.sh`_
- **2026-09-17** [`da3c07bf7d`](https://github.com/vllm-project/vllm/commit/da3c07bf7d) [#57301](https://github.com/vllm-project/vllm/pull/57301)
  [XPU][CI] skip test_hybrid_prefix_cache_hit_rate (#57301)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`_
- **2026-09-17** [`683f6c8edf`](https://github.com/vllm-project/vllm/commit/683f6c8edf) [#57335](https://github.com/vllm-project/vllm/pull/57335)
  [CI] Raise H200 LM Eval Large Models timeout to 120 min (#57335)
  _Files: `.buildkite/test_areas/lm_eval.yaml`_
- **2026-09-17** [`88afb77700`](https://github.com/vllm-project/vllm/commit/88afb77700) [#54978](https://github.com/vllm-project/vllm/pull/54978)
  [CPU][s390x] Pin protobuf to 7.36.1 and drop C++ extension removal workaround (#54978)
  _Files: `docker/Dockerfile.s390x`, `docs/getting_started/installation/cpu.s390x.inc.md`, `requirements/common.txt`_
- **2026-09-17** [`5efbf0886a`](https://github.com/vllm-project/vllm/commit/5efbf0886a) [#56913](https://github.com/vllm-project/vllm/pull/56913)
  [CI] Support `FORCE_COLOR` env var; enable colors in CPU CI output (#56913)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `.buildkite/scripts/hardware_ci/run-cpu-test.sh`, `tests/test_logger.py`, `vllm/envs.py` _+1 more__
- **2026-09-17** [`062f81d8ef`](https://github.com/vllm-project/vllm/commit/062f81d8ef) [#56532](https://github.com/vllm-project/vllm/pull/56532)
  Use skip-redaction option for crcr-report (#56532)
  _Files: `.buildkite/scripts/crcr-report.sh`_
- **2026-09-16** [`929aa2a7ed`](https://github.com/vllm-project/vllm/commit/929aa2a7ed) [#57218](https://github.com/vllm-project/vllm/pull/57218)
  [Build] Bump DeepGEMM pin to a6bbb80 (#57218)
  _Files: `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-09-16** [`24a63b3340`](https://github.com/vllm-project/vllm/commit/24a63b3340) [#57211](https://github.com/vllm-project/vllm/pull/57211)
  [CI][Bugfix] Initialize _transfer_layer_group_ids in region_pull_worker fixture (#57211)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`_
- **2026-09-16** [`651a88c09a`](https://github.com/vllm-project/vllm/commit/651a88c09a) [#57212](https://github.com/vllm-project/vllm/pull/57212)
  [CI] Ignore ruff D209, rejoin the docstrings it split, and silence incompatible-rule warnings (#57212)
- **2026-09-15** [`a2e8f1ea94`](https://github.com/vllm-project/vllm/commit/a2e8f1ea94) [#56934](https://github.com/vllm-project/vllm/pull/56934)
  [XPU][CI]Skip test_chat_completion_with_tools in Intel GPU CI (#56934)
  _Files: `.buildkite/intel_jobs/entrypoints_intel.yaml`_
- **2026-09-15** [`abb4cb9fc5`](https://github.com/vllm-project/vllm/commit/abb4cb9fc5) [#56324](https://github.com/vllm-project/vllm/pull/56324)
  [CI] Shard V1 KV Connectors 1→4 (#56324)
  _Files: `.buildkite/test_areas/misc.yaml`_
- **2026-09-15** [`2983fc6286`](https://github.com/vllm-project/vllm/commit/2983fc6286) [#56955](https://github.com/vllm-project/vllm/pull/56955)
  [CI] Fix NIXL push worker test stub after failure deferral (#56955)
  _Files: `tests/v1/kv_connector/unit/test_nixl_push_connector.py`_
- **2026-09-15** [`2e2fdaa99a`](https://github.com/vllm-project/vllm/commit/2e2fdaa99a) [#56601](https://github.com/vllm-project/vllm/pull/56601)
  [CI] Extend Arm CPU kernel shard timeout (#56601)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`_
- **2026-09-15** [`caf56ce9da`](https://github.com/vllm-project/vllm/commit/caf56ce9da) [#56819](https://github.com/vllm-project/vllm/pull/56819)
  [CI] Pass the scale-out endpoint flag in EC E2E (#56819)
  _Files: `docs/usage/security.md`, `tests/entrypoints/scale_out/ec_integration/run_scale_out_ec_e2e_test.sh`_
- **2026-09-15** [`a491b6039d`](https://github.com/vllm-project/vllm/commit/a491b6039d) [#56941](https://github.com/vllm-project/vllm/pull/56941)
  [CI] Drop root privileges for the OTel GPU sampler (#56941)
  _Files: `.buildkite/scripts/ci-otel/ci_otel.sh`, `.buildkite/scripts/ci-otel/tests/test_ci_otel.py`_
- **2026-09-15** [`a08dffe215`](https://github.com/vllm-project/vllm/commit/a08dffe215) [#56783](https://github.com/vllm-project/vllm/pull/56783)
  [XPU][CI] update gpt-oss package version (#56783)
  _Files: `.buildkite/intel_jobs/lm_eval_intel.yaml`, `requirements/test/xpu.txt`_
- **2026-09-14** [`bdad63c90a`](https://github.com/vllm-project/vllm/commit/bdad63c90a) [#56169](https://github.com/vllm-project/vllm/pull/56169)
  [CI] Check target branch freshness before starting CI (#56169)
  _Files: `.github/workflows/run-ci-command.yml`, `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`, `docs/contributing/README.md`_
- **2026-09-14** [`56ca9904ce`](https://github.com/vllm-project/vllm/commit/56ca9904ce) [#56808](https://github.com/vllm-project/vllm/pull/56808)
  [CI] Initialize ubatch runner in cudagraph unit test (#56808)
  _Files: `tests/v1/cudagraph/test_breakable_cudagraph.py`_
- **2026-09-14** [`e82794f48f`](https://github.com/vllm-project/vllm/commit/e82794f48f) [#56671](https://github.com/vllm-project/vllm/pull/56671)
  [CI][Test] Mock CPU backend block sizes in kv_connector unit conftest (#56671)
  _Files: `tests/v1/kv_connector/unit/conftest.py`_
- **2026-09-14** [`5236bef721`](https://github.com/vllm-project/vllm/commit/5236bef721) [#56766](https://github.com/vllm-project/vllm/pull/56766)
  [CI] Keep OTel bytecode out of mounted checkouts (#56766)
  _Files: `.buildkite/scripts/ci-otel/ci_otel.sh`, `.buildkite/scripts/ci-otel/tests/test_ci_otel.py`_
- **2026-09-14** [`dc36fcce90`](https://github.com/vllm-project/vllm/commit/dc36fcce90) [#56747](https://github.com/vllm-project/vllm/pull/56747)
  [CI] Collect GPU memory telemetry for MIG slices (#56747)
  _Files: `.buildkite/scripts/ci-otel/README.md`, `.buildkite/scripts/ci-otel/ci_gpu.py`, `.buildkite/scripts/ci-otel/tests/test_ci_otel.py`_
- **2026-09-14** [`2d9c30a7b5`](https://github.com/vllm-project/vllm/commit/2d9c30a7b5) [#56710](https://github.com/vllm-project/vllm/pull/56710)
  [CI][Bugfix] Complete FSE fixture R-SWA contract (#56710)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`_
- **2026-09-14** [`fe49665eb3`](https://github.com/vllm-project/vllm/commit/fe49665eb3) [#56704](https://github.com/vllm-project/vllm/pull/56704)
  [XPU][CI] update test requirements (#56704)
  _Files: `requirements/test/xpu.in`, `requirements/test/xpu.txt`_

## Serving / API  (23 commits)

- **2026-09-21** [`21aa17c128`](https://github.com/vllm-project/vllm/commit/21aa17c128) [#57948](https://github.com/vllm-project/vllm/pull/57948)
  [Bugfix][Frontend] Accept diarized transcription responses in run-batch (#57948)
  _Files: `vllm/entrypoints/launchers/run_batch.py`_
- **2026-09-21** [`887cf91e30`](https://github.com/vllm-project/vllm/commit/887cf91e30) [#57498](https://github.com/vllm-project/vllm/pull/57498)
  [Pooling] Fix normalization of chunked long-text embeddings (#57498)
  _Files: `vllm/entrypoints/pooling/embed/io_processor.py`_
- **2026-09-21** [`8b98b7d0b4`](https://github.com/vllm-project/vllm/commit/8b98b7d0b4) [#57922](https://github.com/vllm-project/vllm/pull/57922)
  [Frontend] Add streaming parity tests and docs for derender (#57922)
  _Files: `docs/serving/online_serving/derenderer.md`, `tests/entrypoints/scale_out/derender/test_derender_parity.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `tests/entrypoints/scale_out/derender/utils.py` _+1 more__
- **2026-09-18** [`70164bdadc`](https://github.com/vllm-project/vllm/commit/70164bdadc) [#50550](https://github.com/vllm-project/vllm/pull/50550)
  [Frontend] Add stream reasoning and tool calls from the derender endpoint (#50550)
  _Files: `docs/serving/online_serving/derenderer.md`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/entrypoints/scale_out/derender/serving.py` _+2 more__
- **2026-09-17** [`e8a2a0a8bb`](https://github.com/vllm-project/vllm/commit/e8a2a0a8bb) [#57058](https://github.com/vllm-project/vllm/pull/57058)
  [Bugfix][Frontend] Reject stop strings on --tokens-only servers instead of silently ignoring them (#57058)
  _Files: `tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py`, `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-09-17** [`b978df3299`](https://github.com/vllm-project/vllm/commit/b978df3299) [#57302](https://github.com/vllm-project/vllm/pull/57302)
  Revert "[Frontend] Omit absent fields from /inference/v1/generate stream chunks" (#57302)
  _Files: `rust/src/server/src/routes/inference/generate.rs`, `tests/entrypoints/scale_out/token_in_token_out/test_generate_stream.py`, `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-09-17** [`8538017f4b`](https://github.com/vllm-project/vllm/commit/8538017f4b) [#57264](https://github.com/vllm-project/vllm/pull/57264)
  [Frontend] Omit absent fields from /inference/v1/generate stream chunks (#57264)
  _Files: `rust/src/server/src/routes/inference/generate.rs`, `tests/entrypoints/scale_out/token_in_token_out/test_generate_stream.py`, `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-09-16** [`fbf2c5e8be`](https://github.com/vllm-project/vllm/commit/fbf2c5e8be) [#55084](https://github.com/vllm-project/vllm/pull/55084)
  [Frontend] Add per-request metrics to Responses API (#55084)
  _Files: `docs/features/per_request_metrics.md`, `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/generate/api_router.py`, `vllm/entrypoints/openai/responses/context.py` _+2 more__
- **2026-09-16** [`5a6ccc5892`](https://github.com/vllm-project/vllm/commit/5a6ccc5892) [#57222](https://github.com/vllm-project/vllm/pull/57222)
  [Bugfix] Add Responses cache_write_tokens for API compat and CC parity (#57222)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `tests/entrypoints/unit_tests/test_context.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/protocol.py` _+1 more__
- **2026-09-16** [`e0705731be`](https://github.com/vllm-project/vllm/commit/e0705731be) [#57194](https://github.com/vllm-project/vllm/pull/57194)
  [Refactor] Remove unused interface methods (#57194)
  _Files: `tests/entrypoints/openai/responses/test_parsable_context_unit.py`, `tests/entrypoints/openai/test_tool_choice_content_none.py`, `tests/entrypoints/unit_tests/test_context.py`, `tests/tool_parsers/test_structural_tag_registry.py` _+1 more__
- **2026-09-16** [`9639cbde04`](https://github.com/vllm-project/vllm/commit/9639cbde04) [#57116](https://github.com/vllm-project/vllm/pull/57116)
  [Rust Frontend] Expose local DP size in gRPC Control metadata (#57116)
  _Files: `rust/proto/control.proto`, `rust/src/server/src/grpc/control.rs`, `rust/src/server/src/grpc/tests.rs`_
- **2026-09-16** [`0384e72693`](https://github.com/vllm-project/vllm/commit/0384e72693) [#57045](https://github.com/vllm-project/vllm/pull/57045)
  [UX] Add thinking support to `vllm chat` (#57045)
  _Files: `vllm/entrypoints/cli/openai.py`_
- **2026-09-16** [`18553c5c9f`](https://github.com/vllm-project/vllm/commit/18553c5c9f) [#51367](https://github.com/vllm-project/vllm/pull/51367)
  [Kernel] Use Murmur3 RNG for Gumbel sampling (#51367)
  _Files: `tests/entrypoints/llm/test_struct_output_generate.py`, `tests/entrypoints/openai/chat_completion/test_include_reasoning.py`, `tests/entrypoints/openai/completion/test_completion.py`, `tests/v1/worker/test_gpu_gumbel_sample.py` _+1 more__
- **2026-09-16** [`e0301afb2a`](https://github.com/vllm-project/vllm/commit/e0301afb2a) [#56988](https://github.com/vllm-project/vllm/pull/56988)
  [Bugfix][Responses] Clean up MCP tool sessions once before closing them (#56988)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/context.py`_
- **2026-09-16** [`7d4bba5498`](https://github.com/vllm-project/vllm/commit/7d4bba5498) [#55912](https://github.com/vllm-project/vllm/pull/55912)
  [Doc] Show how to get Responses prompt token IDs (#55912)
  _Files: `docs/serving/online_serving/README.md`, `docs/serving/online_serving/openai_compatible_server.md`, `docs/serving/online_serving/renderer.md`_
- **2026-09-16** [`1fd119def5`](https://github.com/vllm-project/vllm/commit/1fd119def5) [#56505](https://github.com/vllm-project/vllm/pull/56505)
  [Pooling] Cap max-length padding for chunked embeddings (#56505)
  _Files: `vllm/entrypoints/pooling/base/protocol.py`_
- **2026-09-15** [`2fcc524788`](https://github.com/vllm-project/vllm/commit/2fcc524788) [#57024](https://github.com/vllm-project/vllm/pull/57024)
  [Bugfix] Avoid nested score cancellation handlers for /v1/score alias (#57024)
  _Files: `vllm/entrypoints/pooling/scoring/api_router.py`_
- **2026-09-15** [`ca67438c08`](https://github.com/vllm-project/vllm/commit/ca67438c08) [#56249](https://github.com/vllm-project/vllm/pull/56249)
  [Bugfix][Frontend] Handle aborted requests in beam search (#56249)
  _Files: `tests/samplers/test_beam_search.py`, `tests/samplers/test_beam_search_online.py`, `vllm/entrypoints/generate/beam_search/offline.py`, `vllm/entrypoints/generate/beam_search/online.py` _+1 more__
- **2026-09-15** [`a72c046463`](https://github.com/vllm-project/vllm/commit/a72c046463) [#55602](https://github.com/vllm-project/vllm/pull/55602)
  [Bugfix] Avoid nested rerank cancellation handlers (#55602)
  _Files: `vllm/entrypoints/pooling/scoring/api_router.py`_
- **2026-09-14** [`e6b4e47d2d`](https://github.com/vllm-project/vllm/commit/e6b4e47d2d) [#56406](https://github.com/vllm-project/vllm/pull/56406)
  [Bugfix][Rust Frontend] Preserve selected-token logprob mode (#56406)
  _Files: `rust/src/server/src/grpc/convert.rs`_
- **2026-09-14** [`10e8d5614c`](https://github.com/vllm-project/vllm/commit/10e8d5614c) [#56211](https://github.com/vllm-project/vllm/pull/56211)
  [Bugfix][Beam Search] Respect skip_special_tokens during decoding (#56211)
  _Files: `tests/samplers/test_beam_search_online.py`, `vllm/entrypoints/generate/beam_search/offline.py`, `vllm/entrypoints/generate/beam_search/online.py`, `vllm/entrypoints/openai/chat_completion/protocol.py` _+2 more__
- **2026-09-14** [`67111973ee`](https://github.com/vllm-project/vllm/commit/67111973ee) [#56746](https://github.com/vllm-project/vllm/pull/56746)
  [Frontend] Move grpc_server to launchers. (#56746)
  _Files: `tests/entrypoints/launchers/test_grpc_health.py`, `vllm/entrypoints/cli/serve.py`, `vllm/entrypoints/grpc_server.py`, `vllm/entrypoints/launchers/grpc_server.py`_
- **2026-09-14** [`7632f767f0`](https://github.com/vllm-project/vllm/commit/7632f767f0) [#56567](https://github.com/vllm-project/vllm/pull/56567)
  [Rust Frontend] Support HTTP RL weight synchronization (#56567)
  _Files: `rust/README.md`, `rust/src/server/src/error.rs`, `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/abort_requests.rs` _+4 more__

## Disaggregation / PD  (23 commits)

- **2026-09-21** [`7ddd461a28`](https://github.com/vllm-project/vllm/commit/7ddd461a28) [#57742](https://github.com/vllm-project/vllm/pull/57742)
  [Docs] Add ECMooncakeConnector usage example for EPD (#57742)
  _Files: `docs/features/disagg_encoder.md`_
- **2026-09-20** [`17e50b9b76`](https://github.com/vllm-project/vllm/commit/17e50b9b76) [#57779](https://github.com/vllm-project/vllm/pull/57779)
  [XPU][UT]Bugfix when the process can't see all the world_size meet accuracy issue. (#57779)
  _Files: `vllm/distributed/device_communicators/xpu_communicator.py`_
- **2026-09-20** [`9679173788`](https://github.com/vllm-project/vllm/commit/9679173788) [#51052](https://github.com/vllm-project/vllm/pull/51052)
  [KVConnector][MoRIIO] Transfer hybrid mamba/KDA recurrent state in READ mode (#51052)
  _Files: `examples/disaggregated/disaggregated_serving/moriio_toy_proxy_server.py`, `tests/v1/kv_connector/unit/test_moriio_connector.py`, `tests/v1/kv_connector/unit/test_moriio_hma_scheduler.py`, `tests/v1/kv_connector/unit/test_moriio_kv_layout.py` _+7 more__
- **2026-09-20** [`70fc7bd695`](https://github.com/vllm-project/vllm/commit/70fc7bd695) [#54176](https://github.com/vllm-project/vllm/pull/54176)
  [Feature][EPD] Support dynamic EPD (EC-connector) proxy (#54176)
  _Files: `examples/disaggregated/disaggregated_encoder/README.md`, `examples/disaggregated/disaggregated_encoder/disagg_1e1p1d_example.sh`, `examples/disaggregated/disaggregated_encoder/disagg_1e1pd_example.sh`, `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py` _+4 more__
- **2026-09-19** [`90531daf6d`](https://github.com/vllm-project/vllm/commit/90531daf6d) [#55844](https://github.com/vllm-project/vllm/pull/55844)
  [Core][Frontend] Bind KV-event publishers at port 0 and expose the bound endpoints (#55844)
  _Files: `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/kv_event_sources.rs`, `rust/src/server/src/routes/tests.rs`, `tests/distributed/conftest.py` _+7 more__
- **2026-09-18** [`6aab78f477`](https://github.com/vllm-project/vllm/commit/6aab78f477) [#56841](https://github.com/vllm-project/vllm/pull/56841)
  [Bugfix][KVConnector] Make ExampleHiddenStatesConnector abort-safe (#56841)
  _Files: `tests/v1/kv_connector/unit/test_hidden_states_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`_
- **2026-09-18** [`49e0427ca5`](https://github.com/vllm-project/vllm/commit/49e0427ca5) [#57570](https://github.com/vllm-project/vllm/pull/57570)
  [Bugfix][NIXL] Avoid receive reports for notification-only requests (#57570)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/kv_connector/unit/test_kv_load_failure_recovery.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py`_
- **2026-09-18** [`164dca8d1e`](https://github.com/vllm-project/vllm/commit/164dca8d1e) [#55854](https://github.com/vllm-project/vllm/pull/55854)
  [Nixl] Separate transport-failure metrics from KV expiry (#55854)
  _Files: `docs/features/nixl_connector_usage.md`, `tests/v1/kv_connector/unit/test_bidirectional_kv_transfer.py`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py` _+5 more__
- **2026-09-17** [`67e5b0acc9`](https://github.com/vllm-project/vllm/commit/67e5b0acc9) [#57049](https://github.com/vllm-project/vllm/pull/57049)
  [Bugfix][HiSparse][NIXL] Import full blocks without tail prefill on D (#57049)
  _Files: `tests/v1/core/test_prefix_caching.py`, `tests/v1/worker/test_utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/hisparse/worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+4 more__
- **2026-09-17** [`9e1cd262cb`](https://github.com/vllm-project/vllm/commit/9e1cd262cb) [#56950](https://github.com/vllm-project/vllm/pull/56950)
  [Bugfix] Use DP index for dense DP weight updates and EC CPU region (#56950)
  _Files: `tests/v1/ec_connector/unit/cpu/test_ec_shared_region.py`, `tests/v1/worker/test_gpu_worker_weight_transfer.py`, `vllm/distributed/ec_transfer/ec_connector/cpu/common.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-09-17** [`b6e7c1f1f0`](https://github.com/vllm-project/vllm/commit/b6e7c1f1f0) [#57145](https://github.com/vllm-project/vllm/pull/57145)
  [kv_offload] Skip scratch groups (#57145)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/config.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py`_
- **2026-09-17** [`0bfc7a15d0`](https://github.com/vllm-project/vllm/commit/0bfc7a15d0) [#57283](https://github.com/vllm-project/vllm/pull/57283)
  [CI] Fix ruff docstring violations in EC connector files (#57283)
  _Files: `vllm/distributed/ec_transfer/ec_connector/base.py`, `vllm/distributed/ec_transfer/ec_connector/metrics.py`_
- **2026-09-17** [`fa3622a4a1`](https://github.com/vllm-project/vllm/commit/fa3622a4a1) [#54960](https://github.com/vllm-project/vllm/pull/54960)
  [EC Connector] Add Metrics Collection (#54960)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/ec_connector/unit/test_ec_connector_metrics.py`, `tests/v1/ec_connector/unit/test_ec_output_aggregator.py`, `tests/v1/ec_connector/unit/test_worker_ec_connector.py` _+8 more__
- **2026-09-16** [`fc8132a5e5`](https://github.com/vllm-project/vllm/commit/fc8132a5e5) [#57068](https://github.com/vllm-project/vllm/pull/57068)
  [Bugfix] Fix np.float64 leaking into the KV transfer metrics log (#57068)
  _Files: `tests/v1/kv_connector/unit/test_hf3fs_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_stats.py`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py` _+3 more__
- **2026-09-16** [`804e5377aa`](https://github.com/vllm-project/vllm/commit/804e5377aa) [#57077](https://github.com/vllm-project/vllm/pull/57077)
  [Bugfix][HiSparse][PD] Align region-mapped pulls across logical block sizes (#57077)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py`_
- **2026-09-16** [`8b1d188046`](https://github.com/vllm-project/vllm/commit/8b1d188046) [#56855](https://github.com/vllm-project/vllm/pull/56855)
  [Bugfix][Mooncake] Report request-level KV load failures under HMA (#56855)
  _Files: `tests/v1/kv_connector/unit/test_kv_load_failure_recovery.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hma.py`, `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py` _+5 more__
- **2026-09-15** [`7b7e117c29`](https://github.com/vllm-project/vllm/commit/7b7e117c29) [#56735](https://github.com/vllm-project/vllm/pull/56735)
  [CI] Extend DSv4 engine readiness timeout on main (#56735)
  _Files: `.buildkite/test_areas/disaggregated.yaml`_
- **2026-09-15** [`45779ef99f`](https://github.com/vllm-project/vllm/commit/45779ef99f) [#56104](https://github.com/vllm-project/vllm/pull/56104)
  [Bugfix][NIXL] Fix multiple handles xfer race (#56104)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py` _+1 more__
- **2026-09-15** [`381c61e008`](https://github.com/vllm-project/vllm/commit/381c61e008) [#56640](https://github.com/vllm-project/vllm/pull/56640)
  [Bugfix][NIXL] Report a full prefix cache hit as finished (#56640)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py` _+3 more__
- **2026-09-14** [`0ca7aef4e3`](https://github.com/vllm-project/vllm/commit/0ca7aef4e3) [#56317](https://github.com/vllm-project/vllm/pull/56317)
  [Bugfix][NixlPush] Guard _remote_agents read in _do_send_reg_notif (X1) (#56317)
  _Files: `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/push_worker.py`_
- **2026-09-14** [`1678b39627`](https://github.com/vllm-project/vllm/commit/1678b39627) [#56786](https://github.com/vllm-project/vllm/pull/56786)
  [Bugfix][EPD] Preserve media processing options in encoder requests (#56786)
  _Files: `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/v1/ec_connector/unit/test_epd_proxy_retry.py`_
- **2026-09-14** [`2c7ee87223`](https://github.com/vllm-project/vllm/commit/2c7ee87223) [#50984](https://github.com/vllm-project/vllm/pull/50984)
  [Bugfix][Mooncake] Report failed remote KV loads to the scheduler (#50984)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-09-14** [`58d45fd767`](https://github.com/vllm-project/vllm/commit/58d45fd767) [#55027](https://github.com/vllm-project/vllm/pull/55027)
  [Bugfix][KV Connector] MooncakeStore: exclude non-prefix-cacheable (QSA ring) groups; fix align-mode check (#55027)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py` _+7 more__

## Models  (22 commits)

- **2026-09-21** [`9b49f92344`](https://github.com/vllm-project/vllm/commit/9b49f92344) [#57603](https://github.com/vllm-project/vllm/pull/57603)
  [Perf][DSV4.1] Overlap mHC coefficients for small TP batches (#57603)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/model_executor/kernels/mhc/tilelang_kernels.py`, `vllm/model_executor/kernels/mhc/warmup.py`, `vllm/models/deepseek_v41/nvidia/model.py` _+2 more__
- **2026-09-20** [`e378275a8f`](https://github.com/vllm-project/vllm/commit/e378275a8f) [#57745](https://github.com/vllm-project/vllm/pull/57745)
  [Model] Pass intermediate_tensors to the model when capturing CUDA gr… (#57745)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`_
- **2026-09-20** [`d05da62e9c`](https://github.com/vllm-project/vllm/commit/d05da62e9c) [#54871](https://github.com/vllm-project/vllm/pull/54871)
  [XPU] fix incorrect gdn kernel log for XPU path (#54871)
  _Files: `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-09-20** [`0c90804c0b`](https://github.com/vllm-project/vllm/commit/0c90804c0b) [#57462](https://github.com/vllm-project/vllm/pull/57462)
  [Bugfix] DiffusionGemma: cast the self-conditioning soft embed to the buffer dtype (#57462)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-09-19** [`6af44e2887`](https://github.com/vllm-project/vllm/commit/6af44e2887) [#57654](https://github.com/vllm-project/vllm/pull/57654)
  [Bugfix][CPU] Fix DeepSeek V4.1 import without Triton (#57654)
  _Files: `tests/test_triton_utils.py`, `vllm/triton_utils/importing.py`, `vllm/v1/worker/gpu/sample/gumbel.py`_
- **2026-09-18** [`63d9ad0a3a`](https://github.com/vllm-project/vllm/commit/63d9ad0a3a) [#57417](https://github.com/vllm-project/vllm/pull/57417)
  [Model] DiffusionGemma: honor logprob_token_ids on the converging step (#57417)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-09-18** [`e562003adb`](https://github.com/vllm-project/vllm/commit/e562003adb) [#56325](https://github.com/vllm-project/vllm/pull/56325)
  [Tokenizer] Drop dead Mistral tokenizer shims for transformers#41962 (#56325)
  _Files: `vllm/tokenizers/mistral.py`_
- **2026-09-18** [`2909ad8fa4`](https://github.com/vllm-project/vllm/commit/2909ad8fa4) [#51856](https://github.com/vllm-project/vllm/pull/51856)
  [Bugfix] Attach request-level tools to existing system message in DeepSeek V4 Python renderer (#51856)
  _Files: `tests/tokenizers_/fixtures/deepseek_v4/test_output_1.txt`, `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4.py`_
- **2026-09-18** [`2c88fb131c`](https://github.com/vllm-project/vllm/commit/2c88fb131c) [#57414](https://github.com/vllm-project/vllm/pull/57414)
  [Bugfix] DiffusionGemma: hand out stashed logprobs only on the committing step (#57414)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-09-17** [`7bbce752b8`](https://github.com/vllm-project/vllm/commit/7bbce752b8) [#57273](https://github.com/vllm-project/vllm/pull/57273)
  [Perf][Model] Qwen4Exp QSA: sm_90 tuning table for _select_config (#57273)
  _Files: `vllm/models/qwen4_exp/nvidia/ops/qsa.py`_
- **2026-09-17** [`e52da038d1`](https://github.com/vllm-project/vllm/commit/e52da038d1) [#56998](https://github.com/vllm-project/vllm/pull/56998)
  [Rust Frontend] Normalize native renderer reasoning controls (#56998)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/chat/src/error.rs`, `rust/src/chat/src/lib.rs` _+25 more__
- **2026-09-16** [`6ecd97f1b7`](https://github.com/vllm-project/vllm/commit/6ecd97f1b7) [#56441](https://github.com/vllm-project/vllm/pull/56441)
  [Perf][DSpark] Add KV-only context insertion across V4.1 cache formats (#56441)
  _Files: `csrc/libtorch_stable/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `tests/kernels/test_compressor_kv_cache.py` _+1 more__
- **2026-09-16** [`ccbaed5b91`](https://github.com/vllm-project/vllm/commit/ccbaed5b91) [#56096](https://github.com/vllm-project/vllm/pull/56096)
  [XPU] Route to fused_qk_rmsnorm_rope_gate triton kernel (#56096)
  _Files: `vllm/model_executor/models/qwen3_next.py`_
- **2026-09-15** [`2f46a1d9c6`](https://github.com/vllm-project/vllm/commit/2f46a1d9c6) [#57044](https://github.com/vllm-project/vllm/pull/57044)
  [CI] Keep Qwen3 Omni DSpark config fixture complete (#57044)
  _Files: `tests/model_executor/test_qwen3_omni.py`_
- **2026-09-15** [`142020c6c2`](https://github.com/vllm-project/vllm/commit/142020c6c2) [#56593](https://github.com/vllm-project/vllm/pull/56593)
  [Bugfix][Rust Frontend] Honor `add_generation_prompt` in DeepSeek V3.2/V4/V4.1 renderers (#56593)
  _Files: `rust/src/chat/src/renderer/deepseek.rs`, `rust/src/chat/src/renderer/deepseek_v32/encoding.rs`, `rust/src/chat/src/renderer/deepseek_v32/tests.rs`, `rust/src/chat/src/renderer/deepseek_v4/tests.rs` _+1 more__
- **2026-09-15** [`2c2cbd84fd`](https://github.com/vllm-project/vllm/commit/2c2cbd84fd) [#56408](https://github.com/vllm-project/vllm/pull/56408)
  [Frontend] Use XGrammar schema constraints for DeepSeek V4.1 (#56408)
  _Files: `tests/tool_parsers/test_structural_tag_registry.py`, `vllm/tool_parsers/structural_tag_registry.py`_
- **2026-09-15** [`eb61707851`](https://github.com/vllm-project/vllm/commit/eb61707851) [#56706](https://github.com/vllm-project/vllm/pull/56706)
  [Bugfix] Fix stale HPC QK-norm weights after weight refit (#56706)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/layers/hpc/hpc_ihc.py`, `vllm/model_executor/layers/hpc/hpc_module.py`, `vllm/model_executor/layers/hpc/rope_norm.py` _+2 more__
- **2026-09-15** [`a529c1a748`](https://github.com/vllm-project/vllm/commit/a529c1a748) [#53444](https://github.com/vllm-project/vllm/pull/53444)
  [Bugfix] Handle bare and malformed tool call openers in Gemma4 parser (#53444)
  _Files: `tests/tool_parsers/test_gemma4_tool_parser.py`, `vllm/parser/gemma4.py`_
- **2026-09-14** [`b7e8dd8f37`](https://github.com/vllm-project/vllm/commit/b7e8dd8f37) [#56309](https://github.com/vllm-project/vllm/pull/56309)
  [watermarking hardening]  Add e2e test and basic GSM8K quality tests (#56309)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-4B-watermark.yaml`, `tests/evals/gsm8k/configs/models-watermark.txt`, `tests/watermarking/test_watermarking_e2e.py`_
- **2026-09-14** [`b3124a8237`](https://github.com/vllm-project/vllm/commit/b3124a8237) [#56071](https://github.com/vllm-project/vllm/pull/56071)
  [Model] Add support for Nanbeige4.2 (transformers backend) (#56071)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/registry.py`_
- **2026-09-14** [`6623fe5b4e`](https://github.com/vllm-project/vllm/commit/6623fe5b4e) [#49417](https://github.com/vllm-project/vllm/pull/49417)
  [Bugfix] MiniCPM-V 4.6: fix ViT self-attn qkv weight loading (#49417)
  _Files: `vllm/model_executor/models/minicpmv4_6.py`_
- **2026-09-14** [`eb42686a30`](https://github.com/vllm-project/vllm/commit/eb42686a30) [#56299](https://github.com/vllm-project/vllm/pull/56299)
  [Bugfix][Frontend] Support Responses text types in DeepSeek V4.1 (#56299)
  _Files: `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`_

## KV Cache / Offload  (16 commits)

- **2026-09-18** [`23e26e0588`](https://github.com/vllm-project/vllm/commit/23e26e0588) [#50045](https://github.com/vllm-project/vllm/pull/50045)
  [KV Offloading] Back-pressure detection and remediation (#50045)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/test_backpressure.py`, `vllm/v1/kv_offload/tiering/backpressure.py` _+9 more__
- **2026-09-18** [`4991f97669`](https://github.com/vllm-project/vllm/commit/4991f97669) [#57485](https://github.com/vllm-project/vllm/pull/57485)
  [XPU] sleep mode: fix KV cache release test (#57485)
  _Files: `tests/basic_correctness/test_mem.py`_
- **2026-09-18** [`bf13ecc2f7`](https://github.com/vllm-project/vllm/commit/bf13ecc2f7) [#57102](https://github.com/vllm-project/vllm/pull/57102)
  [Perf][MRV2] Share token-to-request mappings across KV cache groups (#57102)
  _Files: `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-09-17** [`ccde9c61e9`](https://github.com/vllm-project/vllm/commit/ccde9c61e9) [#56925](https://github.com/vllm-project/vllm/pull/56925)
  [Bugfix] Restore KV cache metadata GET method for external event consumer (#56925)
  _Files: `tests/v1/engine/test_kv_cache_group_metadata.py`, `vllm/v1/engine/core.py`_
- **2026-09-17** [`40b40d1d39`](https://github.com/vllm-project/vllm/commit/40b40d1d39) [#51081](https://github.com/vllm-project/vllm/pull/51081)
  [Bugfix][KV Offload] Register the offload region in chunks (#51081)
  _Files: `tests/v1/kv_offload/cpu/test_canonical_layout.py`, `tests/v1/kv_offload/cpu/test_gpu_worker.py`, `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `vllm/distributed/device_communicators/cuda_wrapper.py` _+1 more__
- **2026-09-16** [`dff1bde84d`](https://github.com/vllm-project/vllm/commit/dff1bde84d) [#55557](https://github.com/vllm-project/vllm/pull/55557)
  [Model] Qwen4Exp: fp8_e4m3 main KV cache on the QSA path (#55557)
  _Files: `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/models/qwen4_exp/nvidia/ops/qsa.py`, `vllm/models/qwen4_exp/nvidia/qsa.py`_
- **2026-09-16** [`f12fe10c5c`](https://github.com/vllm-project/vllm/commit/f12fe10c5c) [#51787](https://github.com/vllm-project/vllm/pull/51787)
  [Bugfix][KV Offload] Track cache recency once per request (#51787)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_offload/cpu/test_manager.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py` _+6 more__
- **2026-09-16** [`0f8fa53acf`](https://github.com/vllm-project/vllm/commit/0f8fa53acf) [#54014](https://github.com/vllm-project/vllm/pull/54014)
  [Bugfix][KV Offload] Check cgroup memory before SHM allocation (#54014)
  _Files: `tests/distributed/test_shm_broadcast.py`, `tests/utils_/test_cpu_resource_utils.py`, `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `vllm/distributed/device_communicators/shm_broadcast.py` _+3 more__
- **2026-09-16** [`961c5b6b7e`](https://github.com/vllm-project/vllm/commit/961c5b6b7e) [#56709](https://github.com/vllm-project/vllm/pull/56709)
  [Bugfix][KV Offload] Restore MTP-retained sliding-window history (#56709)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-09-16** [`75dc588269`](https://github.com/vllm-project/vllm/commit/75dc588269) [#55885](https://github.com/vllm-project/vllm/pull/55885)
  [KV Offload] Add per-request `max_load_tokens control` (#55885)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-09-16** [`85c1f58d50`](https://github.com/vllm-project/vllm/commit/85c1f58d50) [#55055](https://github.com/vllm-project/vllm/pull/55055)
  [BugFix][Model Runner V2][Spec Decode] Fix decode instance's multi-layer MTP kv caches during P/D (#55055)
  _Files: `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `tests/v1/kv_connector/unit/utils.py`, `vllm/config/vllm.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_scheduler.py` _+3 more__
- **2026-09-15** [`38ca7a899c`](https://github.com/vllm-project/vllm/commit/38ca7a899c) [#57027](https://github.com/vllm-project/vllm/pull/57027)
  [Bugfix][HiSparse] Preserve per-layer offsets in KV cache bindings (#57027)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-HiSparse.yaml`, `tests/evals/gsm8k/configs/models-hisparse.txt`, `vllm/v1/hisparse/binding.py`_
- **2026-09-15** [`000c7df9ff`](https://github.com/vllm-project/vllm/commit/000c7df9ff) [#53624](https://github.com/vllm-project/vllm/pull/53624)
  [KV Offload] Add KVCR secondary-tier adapter (#53624)
  _Files: `.buildkite/scripts/install-kv-offload.sh`, `.buildkite/test_areas/misc.yaml`, `tests/v1/kv_offload/tiering/test_factory.py`, `tests/v1/kv_offload/tiering/test_kvcr_tier.py` _+3 more__
- **2026-09-15** [`e45bb43984`](https://github.com/vllm-project/vllm/commit/e45bb43984) [#56486](https://github.com/vllm-project/vllm/pull/56486)
  [Bugfix][KV Offload] Ignore pending chunks in invalid sliding windows (#56486)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-09-14** [`e85c8826ce`](https://github.com/vllm-project/vllm/commit/e85c8826ce) [#55650](https://github.com/vllm-project/vllm/pull/55650)
  [Bugfix] Make KV cache and MFU log lines backend-neutral (#55650)
  _Files: `vllm/v1/core/kv_cache_utils.py`, `vllm/v1/metrics/loggers.py`, `vllm/v1/metrics/perf.py`_
- **2026-09-14** [`c612e2bff0`](https://github.com/vllm-project/vllm/commit/c612e2bff0) [#55823](https://github.com/vllm-project/vllm/pull/55823)
  [Bugfix][KV Offload] Reuse in-flight async lookup probes (#55823)
  _Files: `tests/v1/kv_offload/tiering/test_async_lookup.py`, `vllm/v1/kv_offload/tiering/async_lookup.py`_

## Speculative Decoding  (15 commits)

- **2026-09-21** [`76ffb0d374`](https://github.com/vllm-project/vllm/commit/76ffb0d374) [#57651](https://github.com/vllm-project/vllm/pull/57651)
  [Model][Engram] Share host tables across co-located DP replicas by default (#57651)
  _Files: `tests/distributed/test_engram_dp_shard.py`, `tests/engine/test_arg_utils.py`, `tests/test_config.py`, `vllm/config/engram.py` _+3 more__
- **2026-09-21** [`9a70c233cd`](https://github.com/vllm-project/vllm/commit/9a70c233cd) [#57643](https://github.com/vllm-project/vllm/pull/57643)
  [Perf][DSV4.1] Fuse TP all-reduce with mHC input preparation (#57643)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/all_reduce_mhc.cu`, `tests/distributed/test_custom_all_reduce.py`, `tests/distributed/test_engram_dp_shard.py` _+5 more__
- **2026-09-21** [`d2983f2f16`](https://github.com/vllm-project/vllm/commit/d2983f2f16) [#56734](https://github.com/vllm-project/vllm/pull/56734)
  [Bugfix][Spec Decode] Stop dummy draft decode steps from writing KV through stale block-table rows (#56734)
  _Files: `tests/v1/worker/test_gpu_block_table.py`, `vllm/v1/worker/gpu/block_table.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`, `vllm/v1/worker/gpu/spec_decode/multi_module_mtp/speculator.py` _+1 more__
- **2026-09-20** [`49ee12d742`](https://github.com/vllm-project/vllm/commit/49ee12d742) [#57382](https://github.com/vllm-project/vllm/pull/57382)
  [Misc] Rename --enable-mamba-fine-grained-prefix-cache (#53945 follow-up) (#57382)
  _Files: `docs/features/automatic_prefix_caching.md`, `tests/v1/core/prefix_cache/test_mamba_eagle_resume_checkpoint.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_mamba_align_chunk_split.py` _+6 more__
- **2026-09-17** [`493d4b3c04`](https://github.com/vllm-project/vllm/commit/493d4b3c04) [#57356](https://github.com/vllm-project/vllm/pull/57356)
  [bugfix] Mark draft tokens to rebuilt their embeddings. (#57356)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-09-17** [`c58ff535f4`](https://github.com/vllm-project/vllm/commit/c58ff535f4) [#56930](https://github.com/vllm-project/vllm/pull/56930)
  [Bugfix][Spec Decode] Fix EAGLE and dense draft startup with EP (#56930)
  _Files: `tests/test_config.py`, `vllm/config/speculative.py`_
- **2026-09-16** [`975dca5bb5`](https://github.com/vllm-project/vllm/commit/975dca5bb5) [#57140](https://github.com/vllm-project/vllm/pull/57140)
  [Perf][GDN] Scatter mixed speculative outputs into the caller buffer (#57140)
  _Files: `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-09-15** [`9446ea1680`](https://github.com/vllm-project/vllm/commit/9446ea1680) [#53458](https://github.com/vllm-project/vllm/pull/53458)
  [Bugfix][Spec Decode] Only create draft_id_to_target_id when draft vocab differs (#53458)
  _Files: `vllm/model_executor/models/deepseek_eagle3.py`, `vllm/model_executor/models/llama_eagle3.py`, `vllm/model_executor/models/qwen3_eagle3.py`_
- **2026-09-15** [`e6960af33b`](https://github.com/vllm-project/vllm/commit/e6960af33b) [#48200](https://github.com/vllm-project/vllm/pull/48200)
  [Refactor] StructuredOutputManager x Speculative Decoding Refactor (#48200)
  _Files: `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_parser_engine.py`, `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/test_scheduler.py` _+8 more__
- **2026-09-15** [`073f883b56`](https://github.com/vllm-project/vllm/commit/073f883b56) [#56903](https://github.com/vllm-project/vllm/pull/56903)
  [Perf][DSpark] Collapse DeepSeek-V4.1 draft states before SP all-gather (#56903)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`_
- **2026-09-15** [`f547c23ec9`](https://github.com/vllm-project/vllm/commit/f547c23ec9) [#56794](https://github.com/vllm-project/vllm/pull/56794)
  [Bugfix][Kimi-K3] Keep transient checkpoints out of prefix-cache eviction (#56794)
  _Files: `tests/v1/core/prefix_cache/test_mamba_eagle_resume_checkpoint.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-09-14** [`5372e72a98`](https://github.com/vllm-project/vllm/commit/5372e72a98) [#56633](https://github.com/vllm-project/vllm/pull/56633)
  [Perf][DSv4.1] Fold the mHC post block into the delayed pre projection (#56633)
  _Files: `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_mhc_jit_warmup.py`, `tests/kernels/test_mhc_kernels.py`, `vllm/model_executor/kernels/mhc/tilelang.py` _+4 more__
- **2026-09-14** [`c676e4930b`](https://github.com/vllm-project/vllm/commit/c676e4930b) [#55133](https://github.com/vllm-project/vllm/pull/55133)
  [Spec Decode] Fix Qwen3 DSpark d2t requirement for padded-vocab drafts (#55133)
  _Files: `tests/model_executor/test_qwen3_omni.py`, `vllm/model_executor/models/qwen3_dspark.py`_
- **2026-09-14** [`47fbd36e6d`](https://github.com/vllm-project/vllm/commit/47fbd36e6d) [#56791](https://github.com/vllm-project/vllm/pull/56791)
  [Bugfix] Trim stale consequence claims from unannotated-eagle warning (#56791)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-09-14** [`a5f6f61a8a`](https://github.com/vllm-project/vllm/commit/a5f6f61a8a) [#54934](https://github.com/vllm-project/vllm/pull/54934)
  [CI][CPU] Add speculative-decoding coverage to CPU CI (#54934)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/scripts/hardware_ci/run-cpu-test.sh`, `docs/features/README.md`, `tests/v1/e2e/test_cpu_spec_decode.py`_

## Quantization  (13 commits)

- **2026-09-19** [`211e252d0b`](https://github.com/vllm-project/vllm/commit/211e252d0b) [#57508](https://github.com/vllm-project/vllm/pull/57508)
  [Bugfix][Model] Fix MiMo-V2.5 fused fp8 qkv_proj sharding (pre-shard count is num_key_value_heads; MTP path too) (#57508)
  _Files: `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`_
- **2026-09-19** [`2fd6268e6d`](https://github.com/vllm-project/vllm/commit/2fd6268e6d) [#57364](https://github.com/vllm-project/vllm/pull/57364)
  [CI] Deflake MTEB score tests with per-model mteb_tol and reruns (#57364)
  _Files: `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`, `tests/models/language/pooling_mteb_test/mteb_score_utils.py`, `tests/models/language/pooling_mteb_test/test_baai.py`, `tests/models/language/pooling_mteb_test/test_bge_reranker_v2_gemma.py` _+13 more__
- **2026-09-18** [`76d517fd12`](https://github.com/vllm-project/vllm/commit/76d517fd12) [#57430](https://github.com/vllm-project/vllm/pull/57430)
  [Quantization] Support kimi-k3 routed expert quant (#57430)
  _Files: `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-09-18** [`44dd18fe0b`](https://github.com/vllm-project/vllm/commit/44dd18fe0b) [#55911](https://github.com/vllm-project/vllm/pull/55911)
  [Model][Gemma4] Load Weights with AutoWeightsLoader (#55911)
  _Files: `tests/lora/test_lora_checkpoints.py`, `tests/models/language/generation/test_gemma.py`, `tests/models/test_utils.py`, `tests/quantization/test_modelopt.py` _+4 more__
- **2026-09-18** [`8da75d6190`](https://github.com/vllm-project/vllm/commit/8da75d6190) [#57377](https://github.com/vllm-project/vllm/pull/57377)
  C3x SM100 FP8 blockwise - Pad activation scales to multiple of 4 (#57377)
  _Files: `.buildkite/test_areas/kernels.yaml`, `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm100_fp8_dispatch.cuh`, `tests/kernels/quantization/test_block_fp8.py`_
- **2026-09-17** [`b78fbab4be`](https://github.com/vllm-project/vllm/commit/b78fbab4be) [#57190](https://github.com/vllm-project/vllm/pull/57190)
  [Docs] Fix the typos in the document (#57190)
  _Files: `docs/benchmarking/cli.md`, `docs/benchmarking/dashboard.md`, `docs/contributing/README.md`, `docs/design/metrics.md` _+5 more__
- **2026-09-16** [`62f9482583`](https://github.com/vllm-project/vllm/commit/62f9482583) [#52956](https://github.com/vllm-project/vllm/pull/52956)
  [Tests] Delete deprecate torchao tests for v1 configs (#52956)
  _Files: `tests/quantization/test_torchao.py`_
- **2026-09-16** [`2bdbbc8080`](https://github.com/vllm-project/vllm/commit/2bdbbc8080) [#55884](https://github.com/vllm-project/vllm/pull/55884)
  [BugFix] Fix is_supported of cutlass FP8 linear (selected and fails on A100) (#55884)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`_
- **2026-09-16** [`b68408043d`](https://github.com/vllm-project/vllm/commit/b68408043d) [#56985](https://github.com/vllm-project/vllm/pull/56985)
  [Bugfix][CPU] Add per-tensor FP8 W8A16 kernel to fix Ministral crash on CPU (#56985)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test.sh`, `tests/kernels/quantization/test_cpu_fp8_scaled_mm.py`, `tests/v1/e2e/test_cpu_spec_decode.py`, `vllm/model_executor/kernels/linear/__init__.py` _+2 more__
- **2026-09-15** [`bb55077411`](https://github.com/vllm-project/vllm/commit/bb55077411) [#56962](https://github.com/vllm-project/vllm/pull/56962)
  [Perf][Kernel] Integrate Mega-mHC from DeepGEMM for DeepSeek V4.1  (reopen of #56255) (#56962)
  _Files: `tests/kernels/quantization/test_block_fp8.py`, `tests/kernels/test_mhc_kernels.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/__init__.py` _+2 more__
- **2026-09-15** [`ec6b14c044`](https://github.com/vllm-project/vllm/commit/ec6b14c044) [#56677](https://github.com/vllm-project/vllm/pull/56677)
  [CI] Select the supported DCP backend for PCP eval (#56677)
  _Files: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-DCP4-EP.yaml`_
- **2026-09-14** [`03dc26e639`](https://github.com/vllm-project/vllm/commit/03dc26e639) [#53793](https://github.com/vllm-project/vllm/pull/53793)
  [Perf][Kernel][Quantization] Fuse ReLU2 with static FP8 activation quantization (#53793)
  _Files: `tests/compile/passes/test_silu_mul_quant_manual_fusion.py`, `tests/fusion/test_quant_activation_contract.py`, `tests/kernels/test_fused_quant_activation.py`, `tests/kernels/test_relu2_fp8_quant.py` _+8 more__
- **2026-09-14** [`39545e475d`](https://github.com/vllm-project/vllm/commit/39545e475d) [#56394](https://github.com/vllm-project/vllm/pull/56394)
  Revert "[CI][XPU] Disable model runner V2 for XPU quantization test for some partially pre-quantized models" (#56394)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`_

## Perf / Benchmark  (9 commits)

- **2026-09-20** [`601e1c7c51`](https://github.com/vllm-project/vllm/commit/601e1c7c51) [#57416](https://github.com/vllm-project/vllm/pull/57416)
  [Perf] Give a prefill-only batch the model state's number of logit rows (#57416)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-09-19** [`41c4a3ed4e`](https://github.com/vllm-project/vllm/commit/41c4a3ed4e) [#57456](https://github.com/vllm-project/vllm/pull/57456)
  [Kernel][Perf] Add sm_120 (RTX PRO 6000 / RTX 50) tuned configs for batch-invariant persistent matmul (#57456)
  _Files: `vllm/model_executor/determinism/batch_invariant_configs.py`_
- **2026-09-18** [`d5f0a6e829`](https://github.com/vllm-project/vllm/commit/d5f0a6e829) [#57502](https://github.com/vllm-project/vllm/pull/57502)
  [Bugfix][DBO] Fix DeepEP low-latency profiling crash with DP+EP+DBO (#57502)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-09-17** [`09c379ab61`](https://github.com/vllm-project/vllm/commit/09c379ab61) [#57355](https://github.com/vllm-project/vllm/pull/57355)
  [Bugfix] Max-load throughput cliff when `max_num_seqs` is not a multiple of 8 (#57355)
  _Files: `tests/compile/test_config.py`, `vllm/config/vllm.py`_
- **2026-09-16** [`1085b64425`](https://github.com/vllm-project/vllm/commit/1085b64425) [#57083](https://github.com/vllm-project/vllm/pull/57083)
  [Benchmark] Retire stale benchmarks and consolidate RMSNorm (#57083)
  _Files: `benchmarks/cutlass_benchmarks/utils.py`, `benchmarks/cutlass_benchmarks/w8a8_benchmarks.py`, `benchmarks/cutlass_benchmarks/weight_shapes.py`, `benchmarks/kernels/benchmark_rmsnorm.py` _+3 more__
- **2026-09-15** [`64856080b0`](https://github.com/vllm-project/vllm/commit/64856080b0) [#56760](https://github.com/vllm-project/vllm/pull/56760)
  [Bugfix] Measure complete pooling responses (#56760)
  _Files: `vllm/benchmarks/lib/endpoint_request_func.py`_
- **2026-09-14** [`f0a61bd438`](https://github.com/vllm-project/vllm/commit/f0a61bd438) [#51104](https://github.com/vllm-project/vllm/pull/51104)
  [Rust][Benchmark] Support HF ShareGPT datasets in multi-turn mode (#51104)
  _Files: `rust/src/bench/README.md`, `rust/src/bench/src/config.rs`, `rust/src/bench/src/multi_turn.rs`_
- **2026-09-14** [`8e08cef46e`](https://github.com/vllm-project/vllm/commit/8e08cef46e) [#56662](https://github.com/vllm-project/vllm/pull/56662)
  [Bugfix] Redact credentials from benchmark logs (#56662)
  _Files: `benchmarks/multi_turn/benchmark_serving_multi_turn.py`, `vllm/benchmarks/lib/utils.py`, `vllm/benchmarks/serve.py`_
- **2026-09-14** [`3b533197a9`](https://github.com/vllm-project/vllm/commit/3b533197a9) [#56683](https://github.com/vllm-project/vllm/pull/56683)
  [Perf] Parallelize mHC pre-norm JIT warmup (#56683)
  _Files: `vllm/model_executor/kernels/mhc/warmup.py`, `vllm/model_executor/warmup/jit_warmup.py`_

## Docs  (8 commits)

- **2026-09-21** [`3e67044972`](https://github.com/vllm-project/vllm/commit/3e67044972) [#57314](https://github.com/vllm-project/vllm/pull/57314)
  [Doc] Refresh Kthena integration guide (#57314)
  _Files: `docs/deployment/integrations/kthena.md`_
- **2026-09-20** [`03f8301387`](https://github.com/vllm-project/vllm/commit/03f8301387) [#57306](https://github.com/vllm-project/vllm/pull/57306)
  Add one-step recipe serving (#57306)
  _Files: `tools/recipes/README.md`, `tools/recipes/serve_with_recipe.sh`_
- **2026-09-17** [`d2a2a82954`](https://github.com/vllm-project/vllm/commit/d2a2a82954) [#57233](https://github.com/vllm-project/vllm/pull/57233)
  [Rust Frontend] Bump vllm-proto to 0.3.0 (#57233)
  _Files: `rust/Cargo.lock`, `rust/proto/Cargo.toml`, `rust/proto/README.md`_
- **2026-09-16** [`fdfcbbcac7`](https://github.com/vllm-project/vllm/commit/fdfcbbcac7) [#57046](https://github.com/vllm-project/vllm/pull/57046)
  [CI/Build][Rust Frontend] Retire Buf schema publishing (#57046)
  _Files: `.github/workflows/buf.yml`, `rust/proto/README.md`, `rust/proto/buf.md`, `rust/proto/buf.yaml`_
- **2026-09-15** [`79e205e8cd`](https://github.com/vllm-project/vllm/commit/79e205e8cd) [#55283](https://github.com/vllm-project/vllm/pull/55283)
  [Doc] Clarify ITL vs TPOT Prometheus metrics (#55283)
  _Files: `docs/design/metrics.md`, `examples/observability/prometheus_grafana/grafana.json`_
- **2026-09-15** [`17bc3e106a`](https://github.com/vllm-project/vllm/commit/17bc3e106a) [#53453](https://github.com/vllm-project/vllm/pull/53453)
  [KVConnector][P2P] Configurable unbound-store timeout and one-RTT rejection of a late fetch (#53453)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `vllm/v1/kv_offload/tiering/p2p/manager.py`_
- **2026-09-14** [`d392ac836e`](https://github.com/vllm-project/vllm/commit/d392ac836e) [#55016](https://github.com/vllm-project/vllm/pull/55016)
  [Doc][Metrics] Fix spec-decode PromQL examples to use the exposed names (#55016)
  _Files: `vllm/v1/spec_decode/metrics.py`_
- **2026-09-14** [`767d1c4d47`](https://github.com/vllm-project/vllm/commit/767d1c4d47) [#56467](https://github.com/vllm-project/vllm/pull/56467)
  [Docs] Move russellb to emeritus committer (#56467)
  _Files: `.github/CODEOWNERS`, `docs/contributing/vulnerability_management.md`, `docs/governance/committers.md`_

## LoRA  (8 commits)

- **2026-09-20** [`0748d3bd57`](https://github.com/vllm-project/vllm/commit/0748d3bd57) [#57708](https://github.com/vllm-project/vllm/pull/57708)
  [Model][LoRA] Enable LoRA support for VoyageQwen3BidirectionalEmbedModel (#57708)
  _Files: `vllm/model_executor/models/voyage.py`_
- **2026-09-18** [`a1bf8ac12d`](https://github.com/vllm-project/vllm/commit/a1bf8ac12d) [#56456](https://github.com/vllm-project/vllm/pull/56456)
  [Bugfix][MRV2] Match fast-prefill padding to active LoRA batches (#56456)
  _Files: `tests/v1/worker/test_attn_utils.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/mm_encoder_model_runner.py`_
- **2026-09-16** [`ca542ee154`](https://github.com/vllm-project/vllm/commit/ca542ee154) [#57148](https://github.com/vllm-project/vllm/pull/57148)
  [Model][LoRA] Enable LoRA support for ModernBertModel (#57148)
  _Files: `docs/models/pooling_models/embed.md`, `vllm/model_executor/models/modernbert.py`_
- **2026-09-16** [`c81eb3e69c`](https://github.com/vllm-project/vllm/commit/c81eb3e69c) [#53555](https://github.com/vllm-project/vllm/pull/53555)
  [LoRA] Support modules_to_save for sequence classification (#53555)
  _Files: `.buildkite/test_areas/lora.yaml`, `docs/features/lora.md`, `examples/pooling/classify/classification_with_lora_offline.py`, `tests/entrypoints/serve/lora/test_lora_adapters.py` _+16 more__
- **2026-09-16** [`0d8173d153`](https://github.com/vllm-project/vllm/commit/0d8173d153) [#51366](https://github.com/vllm-project/vllm/pull/51366)
  [Bugfix][Frontend] Lazy-import model_hosting_container_standards to prevent log suppression (#51366)
  _Files: `vllm/entrypoints/serve/lora/api_router.py`, `vllm/entrypoints/serve/sagemaker/api_router.py`_
- **2026-09-16** [`a31ec3a68b`](https://github.com/vllm-project/vllm/commit/a31ec3a68b) [#56231](https://github.com/vllm-project/vllm/pull/56231)
  [LoRA][Nemotron] Add LoRA support for Nemotron VL models (for the language model only) (#56231)
  _Files: `docs/models/supported_models.md`, `vllm/model_executor/models/nano_nemotron_vl.py`_
- **2026-09-15** [`7dbc3d62c3`](https://github.com/vllm-project/vllm/commit/7dbc3d62c3) [#56898](https://github.com/vllm-project/vllm/pull/56898)
  [Cleanup] Remove vestigial `tpu_input_batch.py` (#56898)
  _Files: `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `vllm/v1/worker/lora_model_runner_mixin.py`, `vllm/v1/worker/mamba_utils.py`, `vllm/v1/worker/tpu_input_batch.py`_
- **2026-09-14** [`663d7f679e`](https://github.com/vllm-project/vllm/commit/663d7f679e) [#53353](https://github.com/vllm-project/vllm/pull/53353)
  [Bugfix] Fix --lora-modules name=path parsing when path contains '=' (#53353)
  _Files: `vllm/entrypoints/launchers/cli_args.py`_

## Compilation / CUDA Graph  (4 commits)

- **2026-09-21** [`67513c8b67`](https://github.com/vllm-project/vllm/commit/67513c8b67) [#57874](https://github.com/vllm-project/vllm/pull/57874)
  [Bugfix][DSV4.1] Restrict mHC overlap to full CUDA graphs (#57874)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`_
- **2026-09-15** [`676650397f`](https://github.com/vllm-project/vllm/commit/676650397f) [#53867](https://github.com/vllm-project/vllm/pull/53867)
  [Feature][PCP] Support decode-only FULL CUDA graphs (#53867)
  _Files: `tests/v1/worker/test_gpu_pcp_manager.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/model_runner.py` _+1 more__
- **2026-09-14** [`0a5747d410`](https://github.com/vllm-project/vllm/commit/0a5747d410) [#51084](https://github.com/vllm-project/vllm/pull/51084)
  [Profiler] Add Proton CUDA graph attribution for MRV2 (#51084)
  _Files: `docs/contributing/profiling.md`, `tests/v1/worker/test_gpu_profiler.py`, `vllm/config/profiler.py`, `vllm/config/vllm.py` _+4 more__
- **2026-09-14** [`73d2a8cf86`](https://github.com/vllm-project/vllm/commit/73d2a8cf86) [#51700](https://github.com/vllm-project/vllm/pull/51700)
  [2/2][Model Runner V2] FULL CUDA graph capture for microbatched steps (DBO) (#51700)
  _Files: `tests/v1/worker/test_gpu_ubatch_slicing.py`, `vllm/config/vllm.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/dp_utils.py` _+2 more__

---
_Generated 2026-09-21 15:09 UTC_