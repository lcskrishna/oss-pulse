# sgl-project/sglang — Weekly Change Report
**Period:** 2026-09-21 → 2026-09-28  |  **Total commits:** 459

## ✨ New Features This Week

- **2026-09-28** [#41364](https://github.com/sgl-project/sglang/pull/41364) — [DeepSelect] Add page-table transform to top-k and tighten the layout contract (#41364)
- **2026-09-28** [#41545](https://github.com/sgl-project/sglang/pull/41545) — [Doc] Add kernel benchmark rule on L2 cache reuse (#41545)
- **2026-09-28** [#40943](https://github.com/sgl-project/sglang/pull/40943) — [AMD][DSV4] moe: enable shared-expert fusion on the grouped-topk path (megamoe) (#40943)
- **2026-09-28** [#39539](https://github.com/sgl-project/sglang/pull/39539) — perf(multimodal): offload CPU feature hashing with bounded admission (#39539)
- **2026-09-28** [#39354](https://github.com/sgl-project/sglang/pull/39354) — docs: add prefill context parallelism guide and design draft (#39354)
- **2026-09-28** [#39060](https://github.com/sgl-project/sglang/pull/39060) — feat(npu): Support returning indexer top-k results (#39060)
- **2026-09-28** [#40664](https://github.com/sgl-project/sglang/pull/40664) — [Intel GPU] Xpu/weekly simple model enablement 2026 09 21 (#40664)
- **2026-09-28** [#36903](https://github.com/sgl-project/sglang/pull/36903) — [AMD] Add GLM-5.3-Flash MI35x nightly test (#36903)
- **2026-09-28** [#38762](https://github.com/sgl-project/sglang/pull/38762) — [diffusion] feat: support multiple task types for pipelines (#38762)
- **2026-09-27** [#37462](https://github.com/sgl-project/sglang/pull/37462) — [Spec] Add LiLiCorr: a candidate-lattice reranker for DFlash drafts (#37462)
- _…and 94 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-28** [`fa443412c5`](https://github.com/sgl-project/sglang/commit/fa443412c5) [#41161](https://github.com/sgl-project/sglang/pull/41161) — [AMD] [GLM5] Fuse shared expert into AITER MoE on gfx950 (#41161)
- **2026-09-28** [`85be04978d`](https://github.com/sgl-project/sglang/commit/85be04978d) [#40943](https://github.com/sgl-project/sglang/pull/40943) — [AMD][DSV4] moe: enable shared-expert fusion on the grouped-topk path (megamoe) (#40943)
- **2026-09-28** [`34f090053e`](https://github.com/sgl-project/sglang/commit/34f090053e) [#41387](https://github.com/sgl-project/sglang/pull/41387) — [AMD] [Docker] Remove unused LLVM 18 setup from ROCm TileLang build (#41387)
- **2026-09-28** [`25de80780a`](https://github.com/sgl-project/sglang/commit/25de80780a) [#36903](https://github.com/sgl-project/sglang/pull/36903) — [AMD] Add GLM-5.3-Flash MI35x nightly test (#36903)
- **2026-09-28** [`3d2827236d`](https://github.com/sgl-project/sglang/commit/3d2827236d) [#41137](https://github.com/sgl-project/sglang/pull/41137) — [AMD] Register Triton data movement tests in PR CI (#41137)
- **2026-09-27** [`81f27fb3a7`](https://github.com/sgl-project/sglang/commit/81f27fb3a7) [#41443](https://github.com/sgl-project/sglang/pull/41443) — [Refactor] Replace LayerScatterModes with LayerFacts and remove ScatterMode (#41443)
- **2026-09-27** [`0e907b755d`](https://github.com/sgl-project/sglang/commit/0e907b755d) [#41439](https://github.com/sgl-project/sglang/pull/41439) — [Refactor] Split the layer communicator into a package (move only) (#41439)
- **2026-09-27** [`b252aceffe`](https://github.com/sgl-project/sglang/commit/b252aceffe) [#41458](https://github.com/sgl-project/sglang/pull/41458) — [AMD] Update v4 cookbook for megamoe, fp8 kv attn, BCG (#41458)
- **2026-09-27** [`effb752188`](https://github.com/sgl-project/sglang/commit/effb752188) [#41019](https://github.com/sgl-project/sglang/pull/41019) — dsv4.1-amd: KV cache layouts, FP4 indexer, compressor and router kernels (#41019)
- **2026-09-27** [`425a1f8f24`](https://github.com/sgl-project/sglang/commit/425a1f8f24) [#41377](https://github.com/sgl-project/sglang/pull/41377) — [AMD] Honor an explicit triton moe_runner_backend for mxfp8 on ROCm (#41377)
- **2026-09-26** [`c73f7077eb`](https://github.com/sgl-project/sglang/commit/c73f7077eb) [#41356](https://github.com/sgl-project/sglang/pull/41356) — [AMD] Fix jit broken on rocm env (#41356)
- **2026-09-26** [`0e2aac500b`](https://github.com/sgl-project/sglang/commit/0e2aac500b) [#36505](https://github.com/sgl-project/sglang/pull/36505) — [ROCm][Perf] aiter: page-level KV view for gfx950 fp8 page-64 asm prefill (#36505)
- **2026-09-26** [`f35ec18d8b`](https://github.com/sgl-project/sglang/commit/f35ec18d8b) [#41297](https://github.com/sgl-project/sglang/pull/41297) — [Test] Remove more unit tests that mirror implementation or never run in CI (#41297)
- **2026-09-25** [`1f6ce4b068`](https://github.com/sgl-project/sglang/commit/1f6ce4b068) [#41286](https://github.com/sgl-project/sglang/pull/41286) — [Test] Remove unit tests that only mirror implementation or never run in CI (#41286)
- **2026-09-25** [`efd9a40bb8`](https://github.com/sgl-project/sglang/commit/efd9a40bb8) [#39660](https://github.com/sgl-project/sglang/pull/39660) — [PD] Share one head-slice helper across mooncake, mori, and nixl (#39660)
- **2026-09-25** [`27e883a20d`](https://github.com/sgl-project/sglang/commit/27e883a20d) [#41018](https://github.com/sgl-project/sglang/pull/41018) — dsv4.1-amd: gfx950 MXFP8 matmul kernels and fp8-grid producers (#41018)
- **2026-09-25** [`f88572a57c`](https://github.com/sgl-project/sglang/commit/f88572a57c) [#41216](https://github.com/sgl-project/sglang/pull/41216) — [Test] Add in-process sgl-eval adapter and move validated GSM8K tests to it (#41216)
- **2026-09-25** [`f337f01b80`](https://github.com/sgl-project/sglang/commit/f337f01b80) [#41215](https://github.com/sgl-project/sglang/pull/41215) — [Test] Remove dead eval modules and point GSM8K/MMLU docs to sgl-eval (#41215)
- **2026-09-25** [`0154f72b48`](https://github.com/sgl-project/sglang/commit/0154f72b48) [#39064](https://github.com/sgl-project/sglang/pull/39064) — [ROCm][Bugfix] Keep quantization for mixed Quark Qwen3.5 MTP checkpoints (#39064)
- **2026-09-25** [`515f5be77e`](https://github.com/sgl-project/sglang/commit/515f5be77e) [#35619](https://github.com/sgl-project/sglang/pull/35619) — [AMD] Integrate Aiter MegaMoEv2 for DeepSeek-V4 (#35619)
- **2026-09-25** [`ec070ec8c8`](https://github.com/sgl-project/sglang/commit/ec070ec8c8) [#41159](https://github.com/sgl-project/sglang/pull/41159) — [AMD] Fix int32 offset overflow in Triton DSv4 KV store kernels (#41159)
- **2026-09-25** [`9dc4c5d891`](https://github.com/sgl-project/sglang/commit/9dc4c5d891) [#40907](https://github.com/sgl-project/sglang/pull/40907) — [AMD] Restore non-DCP Mamba checkpoint donation to fix agent-mode cache hit at high conc with HiCache (#40907)
- **2026-09-24** [`0c578d97fe`](https://github.com/sgl-project/sglang/commit/0c578d97fe) [#41049](https://github.com/sgl-project/sglang/pull/41049) — [DSV4] Size compressed pools from one per-ratio table in DSV4PoolConfigurator (#41049)
- **2026-09-24** [`36f59982fa`](https://github.com/sgl-project/sglang/commit/36f59982fa) [#36559](https://github.com/sgl-project/sglang/pull/36559) — MoE: small-batch sorting path with fused mxfp8 quantisation (#36559)
- **2026-09-24** [`0b53305f48`](https://github.com/sgl-project/sglang/commit/0b53305f48) [#36574](https://github.com/sgl-project/sglang/pull/36574) — MiniMax-M3: MXFP8 dense-only block convert + aiter MXFP8 MoE on gfx950 (#36574)
- **2026-09-24** [`1446e24d13`](https://github.com/sgl-project/sglang/commit/1446e24d13) [#41120](https://github.com/sgl-project/sglang/pull/41120) — [AMD] Add .co for deepseek v4 fp8 decode kernel and add group decode opt (#41120)
- **2026-09-24** [`6a14b80141`](https://github.com/sgl-project/sglang/commit/6a14b80141) [#41109](https://github.com/sgl-project/sglang/pull/41109) — [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260923 daily (#41109)
- **2026-09-24** [`8ec65e89c1`](https://github.com/sgl-project/sglang/commit/8ec65e89c1) [#40387](https://github.com/sgl-project/sglang/pull/40387) — [AMD] ci: move the Miles ROCm 7.2 nightly build to 7.2.4 (#40387)
- **2026-09-24** [`ea5baf4022`](https://github.com/sgl-project/sglang/commit/ea5baf4022) [#40922](https://github.com/sgl-project/sglang/pull/40922) — [Refactor] Retire the model-specific Kimi K3 kernel namespace (#40922)
- **2026-09-24** [`a69583f70f`](https://github.com/sgl-project/sglang/commit/a69583f70f) [#40996](https://github.com/sgl-project/sglang/pull/40996) — [AMD] Add tuned dsv4 shape (#40996)
- **2026-09-24** [`0a59830114`](https://github.com/sgl-project/sglang/commit/0a59830114) [#40878](https://github.com/sgl-project/sglang/pull/40878) — [AMD][DSV4] fp8 unified_kv decode: wave-aware split count past 40 tokens (#40878)
- **2026-09-24** [`d94d784441`](https://github.com/sgl-project/sglang/commit/d94d784441) [#39059](https://github.com/sgl-project/sglang/pull/39059) — [AMD] Tune Triton sparse MLA on gfx950 and make split-K workspaces graph-safe (#39059)
- **2026-09-24** [`a164c6d9f1`](https://github.com/sgl-project/sglang/commit/a164c6d9f1) [#40812](https://github.com/sgl-project/sglang/pull/40812) — [AMD] Register mem-cache unit tests in PR CI (#40812)
- **2026-09-24** [`43af9fcbb6`](https://github.com/sgl-project/sglang/commit/43af9fcbb6) [#41053](https://github.com/sgl-project/sglang/pull/41053) — [AMD][DI][CI] Move MI355X disagg nightly to ROCm 10 (#41053)
- **2026-09-24** [`9f6fc55332`](https://github.com/sgl-project/sglang/commit/9f6fc55332) [#37751](https://github.com/sgl-project/sglang/pull/37751) — [AMD][Diffusion] FlyDSL fused norm kernels on wave32 targets (gfx1250) (#37751)
- **2026-09-24** [`32290dda2c`](https://github.com/sgl-project/sglang/commit/32290dda2c) [#40204](https://github.com/sgl-project/sglang/pull/40204) — [AMD] Small-M MXFP4 fused-MoE kernel for gfx950 (Qwen) (#40204)
- **2026-09-24** [`7a9feacf91`](https://github.com/sgl-project/sglang/commit/7a9feacf91) [#41024](https://github.com/sgl-project/sglang/pull/41024) — [Docs] DeepSeek-V4 MI355X Pro Official PD pairs with DSpark and UMBP (#41024)
- **2026-09-24** [`0dc8b29e15`](https://github.com/sgl-project/sglang/commit/0dc8b29e15) [#40710](https://github.com/sgl-project/sglang/pull/40710) — [ROCm][DSA] Enable AITER fused FP8 indexer writer (#40710)
- **2026-09-24** [`8eedf616f5`](https://github.com/sgl-project/sglang/commit/8eedf616f5) [#41026](https://github.com/sgl-project/sglang/pull/41026) — [AMD][DI][CI] Say which image the MI355X nightly ran on (#41026)
- **2026-09-24** [`e2f4fedf04`](https://github.com/sgl-project/sglang/commit/e2f4fedf04) [#40754](https://github.com/sgl-project/sglang/pull/40754) — [AMD] Critical fix enabling Qwen3.8 FP8: restore dropped fused shared-expert weights (#40754)
- **2026-09-24** [`e98b2f7538`](https://github.com/sgl-project/sglang/commit/e98b2f7538) [#34695](https://github.com/sgl-project/sglang/pull/34695) — [AMD] Speed up Wan2.2 DiT FP8 attention per-tensor quantization (#34695)
- **2026-09-24** [`8b5d77c268`](https://github.com/sgl-project/sglang/commit/8b5d77c268) [#38876](https://github.com/sgl-project/sglang/pull/38876) — [AMD] Add a Triton packed sparse decode path for QSA on ROCm (#38876)
- **2026-09-24** [`81b81664a6`](https://github.com/sgl-project/sglang/commit/81b81664a6) [#40946](https://github.com/sgl-project/sglang/pull/40946) — Revert "[AMD] Fix DeepSeek-V4 accuracy by not passing num_token_non_padded to MoE topk" (#40946)
- **2026-09-24** [`ec75d3d30f`](https://github.com/sgl-project/sglang/commit/ec75d3d30f) [#36549](https://github.com/sgl-project/sglang/pull/36549) — MiniMax-M3: allocate the lightning-indexer K cache in fp8 on gfx95 (#36549)
- **2026-09-23** [`4fa2c9c1de`](https://github.com/sgl-project/sglang/commit/4fa2c9c1de) [#36546](https://github.com/sgl-project/sglang/pull/36546) — MiniMax-M3: run the sparse prefill main attention through AITER Gluon paged attention (#36546)
- **2026-09-23** [`a89f849158`](https://github.com/sgl-project/sglang/commit/a89f849158) [#38340](https://github.com/sgl-project/sglang/pull/38340) — [ROCm] Fuse the MLA q absorb into the RoPE + KV-write kernel on gfx950 (#38340)
- **2026-09-23** [`401d5aedf3`](https://github.com/sgl-project/sglang/commit/401d5aedf3) [#40879](https://github.com/sgl-project/sglang/pull/40879) — [AMD] Drop the unreachable vLLM fallback from ROCm FP8 activation quant (#40879)
- **2026-09-23** [`aa0b65c7c7`](https://github.com/sgl-project/sglang/commit/aa0b65c7c7) [#39804](https://github.com/sgl-project/sglang/pull/39804) — [AMD] Fix DeepSeek-V4 accuracy by not passing num_token_non_padded to MoE topk (#39804)
- **2026-09-23** [`48c3854620`](https://github.com/sgl-project/sglang/commit/48c3854620) [#39790](https://github.com/sgl-project/sglang/pull/39790) — [ROCm] feat: enable aiter allreduce fusion for GLM models (#39790)
- **2026-09-23** [`aa0feca536`](https://github.com/sgl-project/sglang/commit/aa0feca536) [#40813](https://github.com/sgl-project/sglang/pull/40813) — [AMD][DI][CI] Use a node-local model cache on the SPUR cluster (#40813)
- **2026-09-23** [`58988bee2f`](https://github.com/sgl-project/sglang/commit/58988bee2f) [#40844](https://github.com/sgl-project/sglang/pull/40844) — [AMD] Add diffusion (Wan2.2) extras to gfx1151 Docker image (#40844)
- **2026-09-23** [`40048f6e51`](https://github.com/sgl-project/sglang/commit/40048f6e51) [#34061](https://github.com/sgl-project/sglang/pull/34061) — [dLLM] feat: support DiffusionGemma serving (#34061)
- **2026-09-22** [`c19dc43cc7`](https://github.com/sgl-project/sglang/commit/c19dc43cc7) [#39779](https://github.com/sgl-project/sglang/pull/39779) — [AMD] [GLM-5.3-Flash Day 0] Load the MXFP4 MTP draft layer (#39779)
- **2026-09-22** [`3afdde5f05`](https://github.com/sgl-project/sglang/commit/3afdde5f05) [#39341](https://github.com/sgl-project/sglang/pull/39341) — [AMD] [GLM-5.3-Flash Day 0] Enable the k-pool DSA indexer on gfx950 (#39341)
- **2026-09-22** [`077c319914`](https://github.com/sgl-project/sglang/commit/077c319914) [#39778](https://github.com/sgl-project/sglang/pull/39778) — [AMD] [GLM-5.3-Flash Day 0] Enable speculative decoding (MTP) on ROCm (#39778)
- **2026-09-22** [`d6cc283da7`](https://github.com/sgl-project/sglang/commit/d6cc283da7) [#38547](https://github.com/sgl-project/sglang/pull/38547) — [AMD] [GLM-5.3-Flash Day 0] Enable zero-RoPE TileLang DSA on gfx950 (#38547)
- **2026-09-22** [`720617bb5b`](https://github.com/sgl-project/sglang/commit/720617bb5b) [#39901](https://github.com/sgl-project/sglang/pull/39901) — [AMD] Reuse KV gather indices across ASM context prefill layers (#39901)
- **2026-09-22** [`debbb5cde9`](https://github.com/sgl-project/sglang/commit/debbb5cde9) [#40557](https://github.com/sgl-project/sglang/pull/40557) — [AMD] Drop the redundant scale zero-fill before AITER per-tensor FP8 quant (#40557)
- **2026-09-22** [`3f00fb7e2e`](https://github.com/sgl-project/sglang/commit/3f00fb7e2e) [#40123](https://github.com/sgl-project/sglang/pull/40123) — [AMD] Register unified KV page-zeroing test in PR CI (#40123)
- **2026-09-22** [`70a2bb2a30`](https://github.com/sgl-project/sglang/commit/70a2bb2a30) [#40641](https://github.com/sgl-project/sglang/pull/40641) — [AMD][DI] Keep loopback in UCX_NET_DEVICES (#40641)
- **2026-09-22** [`790551c382`](https://github.com/sgl-project/sglang/commit/790551c382) [#35872](https://github.com/sgl-project/sglang/pull/35872) — [AMD] Skip full-vocab softmax in EAGLE topk==1 draft on ROCm (#35872)
- **2026-09-22** [`c2f14bfbc4`](https://github.com/sgl-project/sglang/commit/c2f14bfbc4) [#39503](https://github.com/sgl-project/sglang/pull/39503) — [AMD] Use exact CU share for gfx950 segment-plan headroom (#39503)
- **2026-09-22** [`d00adfd19c`](https://github.com/sgl-project/sglang/commit/d00adfd19c) [#39525](https://github.com/sgl-project/sglang/pull/39525) — [AMD] Fix deferred Kimi-K3 forget gate in fused in-projection (#39525)
- **2026-09-22** [`6412ad8c64`](https://github.com/sgl-project/sglang/commit/6412ad8c64) [#39902](https://github.com/sgl-project/sglang/pull/39902) — [AMD] Pack Qwen3.5 GDN input projections on ROCm (#39902)
- **2026-09-22** [`8ac19cc19f`](https://github.com/sgl-project/sglang/commit/8ac19cc19f) [#39066](https://github.com/sgl-project/sglang/pull/39066) — [AMD][Kimi-K3] Fix deferred KDA gate projection and update DCP cookbook (#39066)
- **2026-09-22** [`04c0913434`](https://github.com/sgl-project/sglang/commit/04c0913434) [#31446](https://github.com/sgl-project/sglang/pull/31446) — [HiSparse] Add MHA hisparse support for MiniMax M3 (#31446)
- **2026-09-22** [`095e45100b`](https://github.com/sgl-project/sglang/commit/095e45100b) [#38545](https://github.com/sgl-project/sglang/pull/38545) — [AMD] [GLM-5.3-Flash Day 0] Route mHC through AITER on gfx950 (#38545)
- **2026-09-22** [`264da63319`](https://github.com/sgl-project/sglang/commit/264da63319) [#39965](https://github.com/sgl-project/sglang/pull/39965) — [AMD] Update ROCm AITER pin to acf8fdf9 (#39965)
- **2026-09-22** [`e1daf68304`](https://github.com/sgl-project/sglang/commit/e1daf68304) [#39317](https://github.com/sgl-project/sglang/pull/39317) — [AMD] [GLM-5.3-Flash Day 0] Honor fused and per-expert names in quark `exclude` (#39317)
- **2026-09-22** [`b44e248682`](https://github.com/sgl-project/sglang/commit/b44e248682) [#38546](https://github.com/sgl-project/sglang/pull/38546) — [AMD] [GLM-5.3-Flash Day 0] Enable FP8 and Quark MXFP4 MoE on gfx950 (#38546)
- **2026-09-22** [`90cf471723`](https://github.com/sgl-project/sglang/commit/90cf471723) [#39340](https://github.com/sgl-project/sglang/pull/39340) — [AMD] [GLM-5.3-Flash Day 0] Support non-2048 top-k widths in the DSA page-table transform (#39340)
- **2026-09-22** [`bc30fa1759`](https://github.com/sgl-project/sglang/commit/bc30fa1759) [#40598](https://github.com/sgl-project/sglang/pull/40598) — [AMD][Fix] AgentX HIP TPOT regression when SGLANG_SIMULATE_ACC_LEN is set (#40598)
- **2026-09-22** [`31b577bb08`](https://github.com/sgl-project/sglang/commit/31b577bb08) [#38875](https://github.com/sgl-project/sglang/pull/38875) — [AMD] Pad QSA MQA decode Q-heads to 16 for ROCm MFMA (#38875)
- **2026-09-22** [`042b6a488f`](https://github.com/sgl-project/sglang/commit/042b6a488f) [#39338](https://github.com/sgl-project/sglang/pull/39338) — [AMD] [GLM-5.3-Flash Day 0] Enable zero-RoPE MHA prefill on ROCm (#39338)
- **2026-09-21** [`0c53fec476`](https://github.com/sgl-project/sglang/commit/0c53fec476) [#39775](https://github.com/sgl-project/sglang/pull/39775) — [ROCm] fix: remove extra bf16 -> fp32 cast in jit grouped topk kernel path (#39775)
- **2026-09-21** [`a5c2cc517c`](https://github.com/sgl-project/sglang/commit/a5c2cc517c) [#40527](https://github.com/sgl-project/sglang/pull/40527) — [CI] Split the CI control labels into four axes and resolve them live (#40527)
- **2026-09-21** [`66f19f5c46`](https://github.com/sgl-project/sglang/commit/66f19f5c46) [#40570](https://github.com/sgl-project/sglang/pull/40570) — [AMD] Enable HiCache for GLM-5.2 MI355X throughput recipe (#40570)
- **2026-09-21** [`8bde82c0ad`](https://github.com/sgl-project/sglang/commit/8bde82c0ad) [#39339](https://github.com/sgl-project/sglang/pull/39339) — [AMD] [GLM-5.3-Flash Day 0] Build the fused DSA k-pool top-k JIT kernel on HIP (#39339)
- **2026-09-21** [`acac4dd9d9`](https://github.com/sgl-project/sglang/commit/acac4dd9d9) [#40632](https://github.com/sgl-project/sglang/pull/40632) — [Refactor] Clean up parallel runtime comments (#40632)
- **2026-09-21** [`e0c2e8dc4d`](https://github.com/sgl-project/sglang/commit/e0c2e8dc4d) [#39987](https://github.com/sgl-project/sglang/pull/39987) — [AMD] Tune Qwen3.5 TP4 GDN recurrent launch on gfx950 (#39987)
- **2026-09-21** [`2d0e94e3a3`](https://github.com/sgl-project/sglang/commit/2d0e94e3a3) [#40340](https://github.com/sgl-project/sglang/pull/40340) — Check the topology identities where the layout is written, and build at the published widths (#40340)
- **2026-09-21** [`ae7a516ba7`](https://github.com/sgl-project/sglang/commit/ae7a516ba7) [#39026](https://github.com/sgl-project/sglang/pull/39026) — feat: use XGrammar V4.1 DSML parameter constraints (#39026)
- **2026-09-21** [`90b3f8544c`](https://github.com/sgl-project/sglang/commit/90b3f8544c) [#39986](https://github.com/sgl-project/sglang/pull/39986) — [AMD] Use Triton softmax routing for Qwen3.5 on gfx950 (#39986)
- **2026-09-21** [`632919e498`](https://github.com/sgl-project/sglang/commit/632919e498) [#37762](https://github.com/sgl-project/sglang/pull/37762) — [AMD] Fix DeepSeek-R1-MXFP4 accuracy with AITER FP8 (#37762)
- **2026-09-21** [`3c71bb018a`](https://github.com/sgl-project/sglang/commit/3c71bb018a) [#37889](https://github.com/sgl-project/sglang/pull/37889) — [AMD] Enable GLM DSA prefill top-k to the v2 kernel (#37889)
- **2026-09-21** [`800613a74b`](https://github.com/sgl-project/sglang/commit/800613a74b) [#40505](https://github.com/sgl-project/sglang/pull/40505) — [Test] Split the serving perf tests by topic into `basic_perf/` and route their thresholds through a kit (#40505)
- **2026-09-21** [`b86a30afba`](https://github.com/sgl-project/sglang/commit/b86a30afba) [#40113](https://github.com/sgl-project/sglang/pull/40113) — [AMD][DI][CI] Add a SPUR cluster profile to AMD DI CI  (#40113)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-09-28 |
| [#41539](https://github.com/sgl-project/sglang/issues/41539) | [Bug] A worker whose launcher died during startup sends SIGQUIT to PID | — | 2026-09-28 |
| [#39991](https://github.com/sgl-project/sglang/issues/39991) | [RFC] Align KV cache events with vLLM's schema so shared consumers hav | — | 2026-09-28 |
| [#40843](https://github.com/sgl-project/sglang/issues/40843) | [Bug] Severe repetition and degenerate loops in reasoning/output when  | — | 2026-09-28 |
| [#37519](https://github.com/sgl-project/sglang/issues/37519) | [Roadmap][Feature] Support T-Head PPU | — | 2026-09-28 |
| [#41514](https://github.com/sgl-project/sglang/issues/41514) | [RFC / HiCache] Same-node peer L2 sharing across DP ranks via /dev/shm | — | 2026-09-28 |
| [#40877](https://github.com/sgl-project/sglang/issues/40877) | [SM120] Field report: DeepSeek-V4.1-Flash in production on 8x RTX PRO  | — | 2026-09-28 |
| [#23206](https://github.com/sgl-project/sglang/issues/23206) | [RFC] Sglang non-GPU process rust migration | — | 2026-09-27 |
| [#41192](https://github.com/sgl-project/sglang/issues/41192) | [Bug] Diffusion Qwen-Image-2.1: TP=2 output corrupted with dense chrom | — | 2026-09-27 |
| [#33355](https://github.com/sgl-project/sglang/issues/33355) | [Feature][DCP] symm_a2a backend: peer-direct A2A for MLA decode on sin | — | 2026-09-26 |
| [#37393](https://github.com/sgl-project/sglang/issues/37393) | [Bug] Kimi-K3 chunked prefill submits different VocabParallelEmbedding | — | 2026-09-26 |
| [#40574](https://github.com/sgl-project/sglang/issues/40574) | [Feature][DSv4.1] Tracking: every backend's two-level candidate indexe | — | 2026-09-26 |
| [#36889](https://github.com/sgl-project/sglang/issues/36889) | [DFLASH] Mamba state cache silently caps effective concurrency on hybr | — | 2026-09-26 |
| [#41299](https://github.com/sgl-project/sglang/issues/41299) | [Bug][ROCm] Qwen3.8-Flash-Next (qwen4_exp) crashes with HSAIL hardware | — | 2026-09-26 |
| [#36938](https://github.com/sgl-project/sglang/issues/36938) | [Bug] Prefill input logprobs are served from the wrong request when a  | — | 2026-09-25 |
| [#40926](https://github.com/sgl-project/sglang/issues/40926) | [Bug] HiCache + hybrid (SSM/Mamba): failed cudaHostRegister on a secon | — | 2026-09-25 |
| [#41152](https://github.com/sgl-project/sglang/issues/41152) | [Bug][AMD] aiter unified attention: Gemma 2/3 batched generations run  | — | 2026-09-25 |
| [#41151](https://github.com/sgl-project/sglang/issues/41151) | [Perf] Padded decode CUDA-graph slots cost more with longer contexts o | — | 2026-09-25 |
| [#21443](https://github.com/sgl-project/sglang/issues/21443) | [Feature][MPS] Better memory management for Apple Silicon Macs | — | 2026-09-25 |
| [#36522](https://github.com/sgl-project/sglang/issues/36522) | [RFC] KV Cache Compression API (KVTC, nvCOMP, ...) | — | 2026-09-25 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 105 |
| MoE / Expert Parallel | 71 |
| Multimodal | 51 |
| Prefill / Decode Disaggregation | 48 |
| Other | 37 |
| KV Cache / Memory | 29 |
| Quantization | 16 |
| Scheduler / Batching | 14 |
| Triton / Kernels | 13 |
| ROCm / AMD | 13 |
| Models | 11 |
| CI / Build | 11 |
| Docs / Examples | 10 |
| Speculative Decoding | 9 |
| Tensor / Data Parallel | 9 |
| Serving / API | 5 |
| Structured Output | 5 |
| LoRA | 2 |

## Attention / FlashInfer  (105 commits)

- **2026-09-28** [`8151378c1a`](https://github.com/sgl-project/sglang/commit/8151378c1a) [#41364](https://github.com/sgl-project/sglang/pull/41364)
  [DeepSelect] Add page-table transform to top-k and tighten the layout contract (#41364)
  _Files: `python/sglang/kernels/jit/csrc/deep_select/README.md`, `python/sglang/kernels/jit/csrc/deep_select/entry.cuh`, `python/sglang/kernels/jit/csrc/deep_select/vendor/.clang-format`, `python/sglang/kernels/jit/csrc/deep_select/vendor/3rdparty/kerutils/README.md` _+23 more__
- **2026-09-28** [`da3eb6db32`](https://github.com/sgl-project/sglang/commit/da3eb6db32) [#41144](https://github.com/sgl-project/sglang/pull/41144)
  [Unified Memory] Fix Inkling conv-checkpoint track ids written to virtual slot numbers (#41144)
  _Files: `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_hybrid_bitexact.py`_
- **2026-09-28** [`bddeb61d94`](https://github.com/sgl-project/sglang/commit/bddeb61d94) [#38133](https://github.com/sgl-project/sglang/pull/38133)
  [Unified Memory] fix: preserve FP8 dtype in unified MHA pool (#38133)
  _Files: `python/sglang/srt/mem_cache/unified_memory_pool.py`, `test/registered/unit/mem_cache/test_unified_mha_views.py`_
- **2026-09-28** [`6582425854`](https://github.com/sgl-project/sglang/commit/6582425854) [#41165](https://github.com/sgl-project/sglang/pull/41165)
  Let predicate-registered linear-attention models carry the mamba radix-cache leaves (#41165)
  _Files: `python/sglang/srt/arg_groups/mamba_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/linear_attn_model_registry.py` _+2 more__
- **2026-09-28** [`f4de6abee6`](https://github.com/sgl-project/sglang/commit/f4de6abee6) [#39060](https://github.com/sgl-project/sglang/pull/39060)
  feat(npu): Support returning indexer top-k results (#39060)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/state_capturer/indexer_topk.py`, `python/sglang/test/ascend/test_ascend_utils.py` _+3 more__
- **2026-09-28** [`25de80780a`](https://github.com/sgl-project/sglang/commit/25de80780a) [#36903](https://github.com/sgl-project/sglang/pull/36903)
  [AMD] Add GLM-5.3-Flash MI35x nightly test (#36903)
  _Files: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py`, `test/run_suite.py`_
- **2026-09-28** [`3d2827236d`](https://github.com/sgl-project/sglang/commit/3d2827236d) [#41137](https://github.com/sgl-project/sglang/pull/41137)
  [AMD] Register Triton data movement tests in PR CI (#41137)
  _Files: `test/registered/attention/test_gdn_fused_split_head_ratios.py`, `test/registered/kernels/ops/embeddings/test_vocab_parallel_embedding.py`_
- **2026-09-27** [`0971450c16`](https://github.com/sgl-project/sglang/commit/0971450c16) [#41436](https://github.com/sgl-project/sglang/pull/41436)
  [Fix] LongCat-Flash under attention DP: branch and merge the dense FFNs through the communicators (#41436)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/longcat_flash.py`, `test/registered/unit/layers/test_communicator_ffn_exit.py`, `test/registered/unit/layers/test_declared_decoder_boundary.py` _+1 more__
- **2026-09-27** [`2e7f0bb28c`](https://github.com/sgl-project/sglang/commit/2e7f0bb28c) [#41428](https://github.com/sgl-project/sglang/pull/41428)
  [Refactor] Publish the LoRA token layout from the batch's FFN input rows (#41428)
  _Files: `python/sglang/srt/layers/communicator.py`, `test/registered/unit/layers/test_communicator_ffn_exit.py`, `test/registered/unit/layers/test_declared_decoder_boundary.py`, `test/registered/unit/layers/test_layer_communicator_fusion_gate.py` _+5 more__
- **2026-09-27** [`6f2d2437b6`](https://github.com/sgl-project/sglang/commit/6f2d2437b6) [#41425](https://github.com/sgl-project/sglang/pull/41425)
  [Refactor] Run MHC layers on the shared boundary steps with MHC's residual operations (#41425)
  _Files: `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_mhc.py`, `python/sglang/srt/layers/dp_attention.py` _+9 more__
- **2026-09-27** [`f5ae989a0e`](https://github.com/sgl-project/sglang/commit/f5ae989a0e) [#41424](https://github.com/sgl-project/sglang/pull/41424)
  [Refactor] Choose fully-DP dense and DSA / MLA prefill CP layers' steps from declarations (#41424)
  _Files: `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py`, `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_dsa_cp.py` _+5 more__
- **2026-09-27** [`cad9eaf27d`](https://github.com/sgl-project/sglang/commit/cad9eaf27d) [#41423](https://github.com/sgl-project/sglang/pull/41423)
  [Fix] Gather a dense FFN's input across attention DP and CP in one DP sum (#41423)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/dp_attention.py`, `test/registered/unit/layers/test_declared_decoder_boundary.py`, `test/registered/unit/layers/test_dp_attention_cp_gather.py`_
- **2026-09-27** [`1c919e401d`](https://github.com/sgl-project/sglang/commit/1c919e401d) [#41422](https://github.com/sgl-project/sglang/pull/41422)
  [Fix] Keep one copy of CP-replicated rows in the DP gather (#41422)
  _Files: `python/sglang/srt/layers/dp_attention.py`, `test/registered/unit/layers/test_dp_attention_cp_replicas.py`_
- **2026-09-27** [`7a833ad0a2`](https://github.com/sgl-project/sglang/commit/7a833ad0a2) [#41421](https://github.com/sgl-project/sglang/pull/41421)
  [Refactor] Choose a GQA prefill CP extend's steps from declarations (#41421)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/nemotron_h.py`, `test/registered/unit/layers/test_communicator_ffn_exit.py` _+8 more__
- **2026-09-27** [`380a4d0332`](https://github.com/sgl-project/sglang/commit/380a4d0332) [#41420](https://github.com/sgl-project/sglang/pull/41420)
  [Refactor] Run every batch of a layer from one BoundarySteps (#41420)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/layers/communicator_mhc.py`, `test/registered/unit/layers/test_communicator_ffn_exit.py` _+8 more__
- **2026-09-27** [`9f87d28db6`](https://github.com/sgl-project/sglang/commit/9f87d28db6) [#41419](https://github.com/sgl-project/sglang/pull/41419)
  [Refactor] Choose the LayerNorm SP region's and input-scattered batches' steps from declarations (#41419)
  _Files: `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `test/registered/unit/layers/test_communicator_ffn_exit.py`, `test/registered/unit/layers/test_communicator_layout.py` _+7 more__
- **2026-09-27** [`78eee88113`](https://github.com/sgl-project/sglang/commit/78eee88113) [#37462](https://github.com/sgl-project/sglang/pull/37462)
  [Spec] Add LiLiCorr: a candidate-lattice reranker for DFlash drafts (#37462)
  _Files: `docs/docs/advanced_features/speculative_decoding.mdx`, `python/sglang/kernels/ops/speculative/__init__.py`, `python/sglang/kernels/ops/speculative/lilicorr.py`, `python/sglang/srt/environ.py` _+7 more__
- **2026-09-27** [`c311bc9611`](https://github.com/sgl-project/sglang/commit/c311bc9611) [#41344](https://github.com/sgl-project/sglang/pull/41344)
  [VLM] Introduce FA4 into ViT for SM100/SM103 (#41344)
  _Files: `benchmark/kernels/attention/bench_flash_attention_tmem_red_max.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/flash_fwd_sm100.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/softmax.py` _+5 more__
- **2026-09-27** [`588049fe2e`](https://github.com/sgl-project/sglang/commit/588049fe2e) [#41309](https://github.com/sgl-project/sglang/pull/41309)
  [diffusion] fix: run an all-valid attention mask on the backend's unmasked kernel (#41309)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/test/unit/test_usp_all_valid_key_mask.py`_
- **2026-09-26** [`cdbea5dccf`](https://github.com/sgl-project/sglang/commit/cdbea5dccf) [#41349](https://github.com/sgl-project/sglang/pull/41349)
  [CI] Move DeepSelect into the attention kernel group to fix the namespace test (#41349)
  _Files: `python/sglang/kernels/jit/csrc/deepselect/README.md`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/deep_select.py`, `test/registered/kernels/ops/attention/test_deep_select.py` _+1 more__
- **2026-09-26** [`a947b56bc7`](https://github.com/sgl-project/sglang/commit/a947b56bc7) [#41341](https://github.com/sgl-project/sglang/pull/41341)
  [CI] Add __main__ entry to test_deep_select.py (#41341)
  _Files: `test/registered/kernels/ops/attention/test_deep_select.py`_
- **2026-09-26** [`d3fcf8997c`](https://github.com/sgl-project/sglang/commit/d3fcf8997c) [#41255](https://github.com/sgl-project/sglang/pull/41255)
  [Refactor] Run the LayerNorm SP region's boundary steps in the communicator itself (#41255)
  _Files: `python/sglang/srt/layers/communicator.py`, `test/registered/unit/layers/test_communicator_ffn_exit.py`, `test/registered/unit/layers/test_layer_communicator_fusion_gate.py`, `test/registered/unit/layers/test_layernorm_sp.py` _+3 more__
- **2026-09-26** [`7bc988446d`](https://github.com/sgl-project/sglang/commit/7bc988446d) [#40556](https://github.com/sgl-project/sglang/pull/40556)
  [DeepSeek V4.1] Add DeepSelect JIT kernel. (#40556)
  _Files: `python/sglang/kernels/jit/csrc/deepselect/README.md`, `python/sglang/kernels/jit/csrc/deepselect/entry.cuh`, `python/sglang/kernels/jit/csrc/deepselect/vendor/.clang-format`, `python/sglang/kernels/jit/csrc/deepselect/vendor/3rdparty/kerutils/README.md` _+23 more__
- **2026-09-26** [`4bb645b8e2`](https://github.com/sgl-project/sglang/commit/4bb645b8e2) [#41311](https://github.com/sgl-project/sglang/pull/41311)
  [DSA] Fix the pooled-indexer breakable prefill bridge under DP attention (#41311)
  _Files: `python/sglang/srt/layers/attention/dsa/kpool_prefill_cuda_graph.py`, `test/registered/e2e/models/test_glm53_flash_b200.py`_
- **2026-09-26** [`8772916e06`](https://github.com/sgl-project/sglang/commit/8772916e06) [#41125](https://github.com/sgl-project/sglang/pull/41125)
  [DSv4.1] Move the low-ratio index top-k into dsv4/low_ratio_indexer (#41125)
  _Files: `python/sglang/kernels/ops/attention/dsv4/candidate_blocks.py`, `python/sglang/kernels/ops/attention/dsv4/topk.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/candidate_indexer.py` _+14 more__
- **2026-09-26** [`0e2aac500b`](https://github.com/sgl-project/sglang/commit/0e2aac500b) [#36505](https://github.com/sgl-project/sglang/pull/36505)
  [ROCm][Perf] aiter: page-level KV view for gfx950 fp8 page-64 asm prefill (#36505)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `test/manual/test_aiter_paged_kv_view.py`_
- **2026-09-26** [`63d320c723`](https://github.com/sgl-project/sglang/commit/63d320c723) [#40854](https://github.com/sgl-project/sglang/pull/40854)
  [DSA] Chunk the kpool indexer MQA logits by query rows under a free-memory budget (#40854)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer_kpool.py`, `test/registered/unit/layers/test_kpool_stream_scheduling.py`_
- **2026-09-26** [`0967a013c2`](https://github.com/sgl-project/sglang/commit/0967a013c2) [#41291](https://github.com/sgl-project/sglang/pull/41291)
  [DSv4.1] Move the ratio-1/2 index top-k ops into kernels/ops/attention/dsv4 (#41291)
  _Files: `python/sglang/kernels/ops/attention/dsv4/candidate_blocks.py`, `python/sglang/kernels/ops/attention/dsv4/candidate_table.py`, `python/sglang/kernels/ops/attention/dsv4/index_logits.py`, `python/sglang/kernels/ops/attention/dsv4/topk.py` _+7 more__
- **2026-09-25** [`1f6ce4b068`](https://github.com/sgl-project/sglang/commit/1f6ce4b068) [#41286](https://github.com/sgl-project/sglang/pull/41286)
  [Test] Remove unit tests that only mirror implementation or never run in CI (#41286)
  _Files: `test/registered/unit/checkpoint_engine/test_checkpoint_engine_worker.py`, `test/registered/unit/entrypoints/test_http2_server_config.py`, `test/registered/unit/layers/test_moriep_mxfp8_dispatch.py`, `test/registered/unit/managers/test_flat_raw_top_logprobs.py` _+11 more__
- **2026-09-25** [`2afd343934`](https://github.com/sgl-project/sglang/commit/2afd343934) [#41284](https://github.com/sgl-project/sglang/pull/41284)
  [misc] Call all_gather_single / reduce_scatter_single to drop torch deprecation warnings (#41284)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/device_communicators/base_device_communicator.py`, `python/sglang/multimodal_gen/runtime/distributed/utils.py`, `python/sglang/srt/distributed/device_communicators/hpu_communicator.py`, `python/sglang/srt/distributed/device_communicators/npu_communicator.py` _+8 more__
- **2026-09-25** [`c421d16563`](https://github.com/sgl-project/sglang/commit/c421d16563) [#36389](https://github.com/sgl-project/sglang/pull/36389)
  [sglang][lora] Support DP attention in LoRA backends (#36389)
  _Files: `docs/docs/advanced_features/lora.mdx`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_mhc.py`, `python/sglang/srt/layers/logits_processor.py` _+21 more__
- **2026-09-25** [`f337f01b80`](https://github.com/sgl-project/sglang/commit/f337f01b80) [#41215](https://github.com/sgl-project/sglang/pull/41215)
  [Test] Remove dead eval modules and point GSM8K/MMLU docs to sgl-eval (#41215)
  _Files: `.claude/skills/cookbook-review-pr/SKILL.md`, `.claude/skills/generate-profile/SKILL.md`, `.gitignore`, `benchmark/deepseek_v3/README.md` _+76 more__
- **2026-09-25** [`963e9fb42d`](https://github.com/sgl-project/sglang/commit/963e9fb42d) [#41197](https://github.com/sgl-project/sglang/pull/41197)
  [Refactor] Leave the FFN reduction to the next layer under attention DP (#41197)
  _Files: `python/sglang/srt/layers/communicator.py`, `test/registered/unit/batch_overlap/test_tbo_unreduced_input.py`, `test/registered/unit/layers/test_communicator_ffn_exit.py`, `test/registered/unit/layers/test_layer_communicator_fusion_gate.py` _+3 more__
- **2026-09-25** [`51c92e8df1`](https://github.com/sgl-project/sglang/commit/51c92e8df1) [#41193](https://github.com/sgl-project/sglang/pull/41193)
  [Fix] Complete the all-reduce when the flashinfer fused norm declines a batch (#41193)
  _Files: `python/sglang/srt/layers/layernorm.py`, `test/registered/unit/layers/test_layernorm_allreduce_fusion.py`_
- **2026-09-25** [`cec70a4708`](https://github.com/sgl-project/sglang/commit/cec70a4708) [#41062](https://github.com/sgl-project/sglang/pull/41062)
  [Fix] Keep the target's DP sync slot in draft scopes (#41062)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/model_executor/forward_batch_info.py` _+6 more__
- **2026-09-25** [`37ebcac3c4`](https://github.com/sgl-project/sglang/commit/37ebcac3c4) [#32269](https://github.com/sgl-project/sglang/pull/32269)
  Support XQA backend for SpecDec verify (#32269)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `test/registered/attention/test_trtllm_mha_graph_metadata.py`_
- **2026-09-25** [`a2025b8c4d`](https://github.com/sgl-project/sglang/commit/a2025b8c4d) [#41091](https://github.com/sgl-project/sglang/pull/41091)
  [DSV4] Account for FlashMLA physical KV page padding in memory budgets (#41091)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-09-24** [`0c578d97fe`](https://github.com/sgl-project/sglang/commit/0c578d97fe) [#41049](https://github.com/sgl-project/sglang/pull/41049)
  [DSV4] Size compressed pools from one per-ratio table in DSV4PoolConfigurator (#41049)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/model_executor/pool_configurator.py` _+2 more__
- **2026-09-24** [`a1eb691ab5`](https://github.com/sgl-project/sglang/commit/a1eb691ab5) [#41046](https://github.com/sgl-project/sglang/pull/41046)
  [Docs] Enable Qwen3.8 Flash Next NVIDIA NVFP4 on B200/B300/GB300 (#41046)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-flash-next.jsx`_
- **2026-09-24** [`1446e24d13`](https://github.com/sgl-project/sglang/commit/1446e24d13) [#41120](https://github.com/sgl-project/sglang/pull/41120)
  [AMD] Add .co for deepseek v4 fp8 decode kernel and add group decode opt (#41120)
  _Files: `docker/rocm.Dockerfile`, `python/sglang/kernels/ops/attention/dsv4/asm/gfx950/mla_v4/mla_a8w8_qh64_qseqlen1_gqaratio64_nm.co`, `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/grouped_verify_streams.py`, `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/runtime.py` _+1 more__
- **2026-09-24** [`a80055d3c6`](https://github.com/sgl-project/sglang/commit/a80055d3c6) [#41083](https://github.com/sgl-project/sglang/pull/41083)
  [Fix] Broadcast requests along attention CP before attention TP (#41083)
  _Files: `python/sglang/srt/distributed/communication_op.py`, `test/registered/unit/distributed/test_attn_cp_tp_broadcast.py`_
- **2026-09-24** [`7c9f74c6e1`](https://github.com/sgl-project/sglang/commit/7c9f74c6e1) [#41082](https://github.com/sgl-project/sglang/pull/41082)
  [Fix] Step-3.5: stop dense layers from summing their output twice under DP attention (#41082)
  _Files: `python/sglang/srt/models/step3p5.py`, `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`_
- **2026-09-24** [`f404db94d4`](https://github.com/sgl-project/sglang/commit/f404db94d4) [#40858](https://github.com/sgl-project/sglang/pull/40858)
  [DP attention] Publish DP buffer sizes from a ForwardBatch (#40858)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/batch_overlap/test_tbo_filter_batch_marker.py` _+2 more__
- **2026-09-24** [`86b3558b41`](https://github.com/sgl-project/sglang/commit/86b3558b41) [#41138](https://github.com/sgl-project/sglang/pull/41138)
  [Fix] Skip the DCP target-verify MLA kernel during FlashInfer autotune (#41138)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `test/registered/dcp/test_trtllm_mla_family_dcp_metadata.py`_
- **2026-09-24** [`984994e3aa`](https://github.com/sgl-project/sglang/commit/984994e3aa) [#40805](https://github.com/sgl-project/sglang/pull/40805)
  fix: Triton 3.8 compatbility to support DSV4.1-Flash in CUDA 13.4 image (Rubin) (#40805)
  _Files: `python/sglang/kernels/ops/attention/dsv4/decode_attention_sm100_gluon.py`_
- **2026-09-24** [`4142235c2b`](https://github.com/sgl-project/sglang/commit/4142235c2b) [#40524](https://github.com/sgl-project/sglang/pull/40524)
  [NPU] Update CANN version to 9.1.0 (#40524)
  _Files: `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/coverage-collection-npu.yml`, `.github/workflows/diffusion-ci-gt-gen-npu.yml` _+11 more__
- **2026-09-24** [`0a59830114`](https://github.com/sgl-project/sglang/commit/0a59830114) [#40878](https://github.com/sgl-project/sglang/pull/40878)
  [AMD][DSV4] fp8 unified_kv decode: wave-aware split count past 40 tokens (#40878)
  _Files: `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/runtime.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-09-24** [`d94d784441`](https://github.com/sgl-project/sglang/commit/d94d784441) [#39059](https://github.com/sgl-project/sglang/pull/39059)
  [AMD] Tune Triton sparse MLA on gfx950 and make split-K workspaces graph-safe (#39059)
  _Files: `python/sglang/kernels/ops/attention/dsa/triton_sparse_mla.py`, `python/sglang/kernels/ops/attention/dsa/triton_sparse_mla_decode.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/kernels/ops/attention/test_triton_sparse_mla_hip.py`_
- **2026-09-24** [`a164c6d9f1`](https://github.com/sgl-project/sglang/commit/a164c6d9f1) [#40812](https://github.com/sgl-project/sglang/pull/40812)
  [AMD] Register mem-cache unit tests in PR CI (#40812)
  _Files: `test/registered/unit/mem_cache/test_asymmetric_mha_pool.py`, `test/registered/unit/mem_cache/test_hicache_load_back_timing.py`_
- **2026-09-24** [`0dc8b29e15`](https://github.com/sgl-project/sglang/commit/0dc8b29e15) [#40710](https://github.com/sgl-project/sglang/pull/40710)
  [ROCm][DSA] Enable AITER fused FP8 indexer writer (#40710)
  _Files: `python/sglang/kernels/ops/attention/dsa/fp8_fused_writer_hip.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `test/registered/amd/test_fp8_fused_dsa_writer_gfx950.py` _+1 more__
- **2026-09-24** [`be495a6174`](https://github.com/sgl-project/sglang/commit/be495a6174) [#40796](https://github.com/sgl-project/sglang/pull/40796)
  [Fix] Use cached prefix lengths for FlashInfer full-attention ragged prefill (#40796)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`, `test/registered/attention/unittests/swa/test_flashinfer.py`_
- **2026-09-24** [`5c44214d6a`](https://github.com/sgl-project/sglang/commit/5c44214d6a) [#37213](https://github.com/sgl-project/sglang/pull/37213)
  [XPU] Qwen3.8-flash-next enablement (#37213)
  _Files: `python/sglang/kernels/ops/mamba/mamba_state_scatter_triton.py`, `python/sglang/srt/hardware_backend/xpu/kernels/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/layers/hyperconnection.py` _+2 more__
- **2026-09-24** [`f4b90382a2`](https://github.com/sgl-project/sglang/commit/f4b90382a2) [#40804](https://github.com/sgl-project/sglang/pull/40804)
  [RL] Keep DSA cuda-graph state and the graph pool intact across TMS pause/resume (#40804)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/model_executor/runner_backend/full_cuda_graph_backend.py`, `test/registered/kernels/ops/attention/test_dsa_indexer.py`, `test/registered/kernels/ops/attention/test_dsa_multi_ctas_counter.py`_
- **2026-09-24** [`e98b2f7538`](https://github.com/sgl-project/sglang/commit/e98b2f7538) [#34695](https://github.com/sgl-project/sglang/pull/34695)
  [AMD] Speed up Wan2.2 DiT FP8 attention per-tensor quantization (#34695)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py`_
- **2026-09-24** [`8b5d77c268`](https://github.com/sgl-project/sglang/commit/8b5d77c268) [#38876](https://github.com/sgl-project/sglang/pull/38876)
  [AMD] Add a Triton packed sparse decode path for QSA on ROCm (#38876)
  _Files: `python/sglang/srt/layers/attention/qsa/sparse_attn.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`_
- **2026-09-24** [`81cb895b85`](https://github.com/sgl-project/sglang/commit/81cb895b85) [#40989](https://github.com/sgl-project/sglang/pull/40989)
  [Fix] Recover from stale torch extension locks in every `cpp_extension` loader (#40989)
  _Files: `python/sglang/kernels/ops/attention/linear/kda_ptx_prefill/__init__.py`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/ext/hunyuan3d_rasterizer/__init__.py`, `python/sglang/kernels/ops/diffusion/ext/mesh_processor/__init__.py` _+5 more__
- **2026-09-24** [`ec75d3d30f`](https://github.com/sgl-project/sglang/commit/ec75d3d30f) [#36549](https://github.com/sgl-project/sglang/pull/36549)
  MiniMax-M3: allocate the lightning-indexer K cache in fp8 on gfx95 (#36549)
  _Files: `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+1 more__
- **2026-09-23** [`208f6f7501`](https://github.com/sgl-project/sglang/commit/208f6f7501) [#40794](https://github.com/sgl-project/sglang/pull/40794)
  [Spec] Support DFLASH for Kimi K3 (#40794)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`, `python/sglang/srt/models/kimi_k3.py`_
- **2026-09-23** [`f2a1366584`](https://github.com/sgl-project/sglang/commit/f2a1366584) [#36560](https://github.com/sgl-project/sglang/pull/36560)
  MiniMax-M3: wave64 histogram-select decode top-k, and raise kMaxNumBlocks for CUDA graphs (#36560)
  _Files: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `python/sglang/kernels/ops/attention/minimax_decode_topk.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`_
- **2026-09-23** [`4fa2c9c1de`](https://github.com/sgl-project/sglang/commit/4fa2c9c1de) [#36546](https://github.com/sgl-project/sglang/pull/36546)
  MiniMax-M3: run the sparse prefill main attention through AITER Gluon paged attention (#36546)
  _Files: `python/sglang/kernels/ops/attention/minimax_sparse/prefill/flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/minimax_sparse/prefill/topk_sparse.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py` _+2 more__
- **2026-09-23** [`701cf7e47e`](https://github.com/sgl-project/sglang/commit/701cf7e47e) [#40867](https://github.com/sgl-project/sglang/pull/40867)
  [Refactor] Run Nemotron-H DP attention through the standard layer communicator (#40867)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/layers/attention/mamba/mamba2_metadata.py`, `python/sglang/srt/layers/radix_linear_attention.py` _+7 more__
- **2026-09-23** [`9ebe42238b`](https://github.com/sgl-project/sglang/commit/9ebe42238b) [#40800](https://github.com/sgl-project/sglang/pull/40800)
  [Fix] Reduce Nemotron MTP attention outputs once (#40800)
  _Files: `python/sglang/srt/models/nemotron_h_mtp.py`, `test/registered/unit/models/test_nemotron_h_mtp_reduction.py`_
- **2026-09-23** [`f2f223e697`](https://github.com/sgl-project/sglang/commit/f2f223e697) [#40683](https://github.com/sgl-project/sglang/pull/40683)
  Allow attention layers to opt out of the prefill wrapper (#40683)
  _Files: `python/sglang/srt/layers/radix_attention.py`, `test/registered/unit/layers/test_radix_attention.py`_
- **2026-09-23** [`4cd63da996`](https://github.com/sgl-project/sglang/commit/4cd63da996) [#38778](https://github.com/sgl-project/sglang/pull/38778)
  [Unified Cache] Dedup replicated MLA/DSA KV in the UMBP direct linker (#38778)
  _Files: `python/sglang/srt/mem_cache/storage/umbp/umbp_direct_linker.py`, `test/registered/unit/mem_cache/test_umbp_direct_linker_rank_keys.py`_
- **2026-09-23** [`a89f849158`](https://github.com/sgl-project/sglang/commit/a89f849158) [#38340](https://github.com/sgl-project/sglang/pull/38340)
  [ROCm] Fuse the MLA q absorb into the RoPE + KV-write kernel on gfx950 (#38340)
  _Files: `python/sglang/srt/layers/rocm_linear_utils.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`, `test/registered/unit/models/test_rocm_mla_absorb_fusion_gate.py`_
- **2026-09-23** [`86cb4a0f97`](https://github.com/sgl-project/sglang/commit/86cb4a0f97) [#40862](https://github.com/sgl-project/sglang/pull/40862)
  [CI] Update GLM-5.3-Flash H200/B200 test args (#40862)
  _Files: `test/registered/e2e/models/test_glm53_flash_b200.py`, `test/registered/e2e/models/test_glm53_flash_h200.py`_
- **2026-09-23** [`525f14040d`](https://github.com/sgl-project/sglang/commit/525f14040d) [#40824](https://github.com/sgl-project/sglang/pull/40824)
  [NPU]fix ci hicache oom (#40824)
  _Files: `test/registered/npu/basic_function/HiCache/test_npu_hicache_mha.py`, `test/registered/npu/basic_function/HiCache/test_npu_hicache_mla.py`_
- **2026-09-22** [`06008c170d`](https://github.com/sgl-project/sglang/commit/06008c170d) [#40431](https://github.com/sgl-project/sglang/pull/40431)
  [dsv4.1]Optimize FP4 indexer by skipping invisible tiles (#40431)
  _Files: `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`, `test/registered/kernels/ops/attention/test_fp4_indexer.py`_
- **2026-09-22** [`c19dc43cc7`](https://github.com/sgl-project/sglang/commit/c19dc43cc7) [#39779](https://github.com/sgl-project/sglang/pull/39779)
  [AMD] [GLM-5.3-Flash Day 0] Load the MXFP4 MTP draft layer (#39779)
  _Files: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/glm5_next_nextn.py`, `test/registered/unit/layers/quantization/test_quark_config.py`, `test/registered/unit/models/test_glm5_next_modelopt.py`_
- **2026-09-22** [`3afdde5f05`](https://github.com/sgl-project/sglang/commit/3afdde5f05) [#39341](https://github.com/sgl-project/sglang/pull/39341)
  [AMD] [GLM-5.3-Flash Day 0] Enable the k-pool DSA indexer on gfx950 (#39341)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer_kpool.py`, `python/sglang/srt/layers/attention/dsa/kpool_fp8_index.py`, `test/registered/unit/layers/attention/test_dsa_mqa_logits_chunking.py`, `test/registered/unit/layers/attention/test_kpool_preshuffled_cache_layout.py`_
- **2026-09-22** [`077c319914`](https://github.com/sgl-project/sglang/commit/077c319914) [#39778](https://github.com/sgl-project/sglang/pull/39778)
  [AMD] [GLM-5.3-Flash Day 0] Enable speculative decoding (MTP) on ROCm (#39778)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer_kpool.py`, `python/sglang/srt/layers/attention/dsa/kpool_plan.py`_
- **2026-09-22** [`d6cc283da7`](https://github.com/sgl-project/sglang/commit/d6cc283da7) [#38547](https://github.com/sgl-project/sglang/pull/38547)
  [AMD] [GLM-5.3-Flash Day 0] Enable zero-RoPE TileLang DSA on gfx950 (#38547)
  _Files: `python/sglang/kernels/ops/attention/dsa/dequant_k_cache.py`, `python/sglang/kernels/ops/attention/dsa/quant_k_cache.py`, `python/sglang/kernels/ops/attention/dsa/tilelang_kernel.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+1 more__
- **2026-09-22** [`4cbf290fb9`](https://github.com/sgl-project/sglang/commit/4cbf290fb9) [#40637](https://github.com/sgl-project/sglang/pull/40637)
  [Fix] Handle chunked paged MQA metadata in DSV4.1 eager forwards (#40637)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/candidate_indexer_deep_gemm.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py` _+1 more__
- **2026-09-22** [`720617bb5b`](https://github.com/sgl-project/sglang/commit/720617bb5b) [#39901](https://github.com/sgl-project/sglang/pull/39901)
  [AMD] Reuse KV gather indices across ASM context prefill layers (#39901)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/amd/test_asm_context_prefill_gather_indices.py`_
- **2026-09-22** [`c79510cc2a`](https://github.com/sgl-project/sglang/commit/c79510cc2a) [#40352](https://github.com/sgl-project/sglang/pull/40352)
  [DSv4.1] Score prefill consumer index layers on candidate blocks with DeepGEMM (#40352)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/candidate_indexer.py`, `python/sglang/srt/layers/attention/dsv4/candidate_indexer_deep_gemm.py`, `python/sglang/srt/layers/attention/dsv4/dense_prefill_indexer.py` _+1 more__
- **2026-09-22** [`9d58189c12`](https://github.com/sgl-project/sglang/commit/9d58189c12) [#40175](https://github.com/sgl-project/sglang/pull/40175)
  [diffusion] attention: add fp8_fa_sm120 FP8 backend for SM120 GPUs (#40175)
  _Files: `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/kernels/ops/attention/fp8_fa_sm120/__init__.py`, `python/sglang/kernels/ops/attention/fp8_fa_sm120/fused_prep.py`, `python/sglang/kernels/ops/attention/fp8_fa_sm120/kernel.py` _+5 more__
- **2026-09-22** [`c2f14bfbc4`](https://github.com/sgl-project/sglang/commit/c2f14bfbc4) [#39503](https://github.com/sgl-project/sglang/pull/39503)
  [AMD] Use exact CU share for gfx950 segment-plan headroom (#39503)
  _Files: `python/sglang/kernels/ops/attention/vattn_asm_gfx950/__init__.py`, `test/registered/unit/layers/attention/test_vattn_asm_segment_plan.py`_
- **2026-09-22** [`4c81cd1b09`](https://github.com/sgl-project/sglang/commit/4c81cd1b09) [#40685](https://github.com/sgl-project/sglang/pull/40685)
  [KDA] Fix missing beta sigmoid in PTX prefill (#40685)
  _Files: `python/sglang/srt/layers/attention/linear/kernels/kda_ptx.py`, `test/registered/kernels/ops/attention/test_kda_prefill.py`, `test/registered/unit/layers/attention/linear/kernels/test_kda_ptx.py`_
- **2026-09-22** [`a0781f2714`](https://github.com/sgl-project/sglang/commit/a0781f2714) [#40497](https://github.com/sgl-project/sglang/pull/40497)
  [Docs] GLM-5.3/5.3-Flash cookbooks: enable reasoning/tool-call parsers by default via auto (#40497)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`_
- **2026-09-22** [`095e45100b`](https://github.com/sgl-project/sglang/commit/095e45100b) [#38545](https://github.com/sgl-project/sglang/pull/38545)
  [AMD] [GLM-5.3-Flash Day 0] Route mHC through AITER on gfx950 (#38545)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`, `test/registered/kernels/ops/layernorm/test_mhc_aiter_hip.py`_
- **2026-09-22** [`e1daf68304`](https://github.com/sgl-project/sglang/commit/e1daf68304) [#39317](https://github.com/sgl-project/sglang/pull/39317)
  [AMD] [GLM-5.3-Flash Day 0] Honor fused and per-expert names in quark `exclude` (#39317)
  _Files: `python/sglang/srt/layers/quantization/quark/utils.py`, `test/registered/unit/layers/quantization/test_quark_utils.py`_
- **2026-09-22** [`90cf471723`](https://github.com/sgl-project/sglang/commit/90cf471723) [#39340](https://github.com/sgl-project/sglang/pull/39340)
  [AMD] [GLM-5.3-Flash Day 0] Support non-2048 top-k widths in the DSA page-table transform (#39340)
  _Files: `python/sglang/kernels/ops/attention/dsa/transform_index.py`, `test/registered/kernels/ops/attention/test_dsa_transform_index.py`_
- **2026-09-22** [`e332e1b84e`](https://github.com/sgl-project/sglang/commit/e332e1b84e) [#39524](https://github.com/sgl-project/sglang/pull/39524)
  [Fix] Don't write conv state from the fused KDA verify kernel (#39524)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_kda_conv_recurrent_verify.py`, `test/registered/kernels/ops/attention/test_fused_kda_conv_recurrent_verify.py`_
- **2026-09-22** [`31b577bb08`](https://github.com/sgl-project/sglang/commit/31b577bb08) [#38875](https://github.com/sgl-project/sglang/pull/38875)
  [AMD] Pad QSA MQA decode Q-heads to 16 for ROCm MFMA (#38875)
  _Files: `python/sglang/srt/layers/attention/qsa/mqa.py`_
- **2026-09-22** [`042b6a488f`](https://github.com/sgl-project/sglang/commit/042b6a488f) [#39338](https://github.com/sgl-project/sglang/pull/39338)
  [AMD] [GLM-5.3-Flash Day 0] Enable zero-RoPE MHA prefill on ROCm (#39338)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha_rocm.py`, `test/registered/unit/models/test_nope_mha_k_cast.py`_
- **2026-09-22** [`c53cc8e1eb`](https://github.com/sgl-project/sglang/commit/c53cc8e1eb) [#40371](https://github.com/sgl-project/sglang/pull/40371)
  [NPU][BugFix] Avoid M-RoPE recompilation for variable sequence lengths (#40371)
  _Files: `python/sglang/kernels/ops/attention/mrope.py`_
- **2026-09-22** [`61d0cf2074`](https://github.com/sgl-project/sglang/commit/61d0cf2074) [#32673](https://github.com/sgl-project/sglang/pull/32673)
  [Spec] Windowed draft-decode attention for built-in EAGLE / MTP drafts (#32673)
  _Files: `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/srt/arg_groups/fields/spec.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py` _+4 more__
- **2026-09-22** [`9fdb71732a`](https://github.com/sgl-project/sglang/commit/9fdb71732a) [#33778](https://github.com/sgl-project/sglang/pull/33778)
  Avoid materializing GDN QKV tensors during target verification (#33778)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`, `python/sglang/srt/layers/attention/linear/kernels/kernel_backend.py`, `test/registered/attention/unittests/gdn/test_gdn_replayssm_spec_fold.py` _+2 more__
- **2026-09-21** [`00986c81be`](https://github.com/sgl-project/sglang/commit/00986c81be) [#40310](https://github.com/sgl-project/sglang/pull/40310)
  Support GLM-5.3-Flash hybrid attention CPU offload and PD index mapping (#40310)
  _Files: `python/sglang/kernels/ops/attention/dsa/transform_index.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_kpool.py`, `python/sglang/srt/utils/offloader.py`, `test/registered/kernels/ops/attention/test_dsa_transform_index.py`_
- **2026-09-21** [`f532ad1f9a`](https://github.com/sgl-project/sglang/commit/f532ad1f9a) [#40607](https://github.com/sgl-project/sglang/pull/40607)
  Fix GLM-5.3 forget-gate shape for nvCUTEDSL verify (#40607)
  _Files: `python/sglang/srt/layers/attention/linear/kda_backend.py`_
- **2026-09-21** [`e0c2e8dc4d`](https://github.com/sgl-project/sglang/commit/e0c2e8dc4d) [#39987](https://github.com/sgl-project/sglang/pull/39987)
  [AMD] Tune Qwen3.5 TP4 GDN recurrent launch on gfx950 (#39987)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `test/registered/kernels/ops/attention/test_fused_verify_triton_gdn.py`_
- **2026-09-21** [`11e661fd45`](https://github.com/sgl-project/sglang/commit/11e661fd45) [#39175](https://github.com/sgl-project/sglang/pull/39175)
  [Fix] Don't free the multi-CTAs KV counter the decode graphs captured (#39175)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/kernels/ops/attention/test_dsa_multi_ctas_counter.py`_
- **2026-09-21** [`1d3243d05f`](https://github.com/sgl-project/sglang/commit/1d3243d05f) [#40344](https://github.com/sgl-project/sglang/pull/40344)
  Take the parallel getters off the package's public surface (#40344)
  _Files: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`, `python/sglang/srt/distributed/device_communicators/triton_symm_mem_ag.py`, `python/sglang/srt/distributed/gated_launch.py` _+3 more__
- **2026-09-21** [`65be3fa71a`](https://github.com/sgl-project/sglang/commit/65be3fa71a) [#40341](https://github.com/sgl-project/sglang/pull/40341)
  A runner and the objects it builds freeze the placement they describe (#40341)
  _Files: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` _+9 more__
- **2026-09-21** [`ae7a516ba7`](https://github.com/sgl-project/sglang/commit/ae7a516ba7) [#39026](https://github.com/sgl-project/sglang/pull/39026)
  feat: use XGrammar V4.1 DSML parameter constraints (#39026)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` _+13 more__
- **2026-09-21** [`632919e498`](https://github.com/sgl-project/sglang/commit/632919e498) [#37762](https://github.com/sgl-project/sglang/pull/37762)
  [AMD] Fix DeepSeek-R1-MXFP4 accuracy with AITER FP8 (#37762)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`_
- **2026-09-21** [`7a6191c4b9`](https://github.com/sgl-project/sglang/commit/7a6191c4b9) [#40256](https://github.com/sgl-project/sglang/pull/40256)
  Preallocate HiCache MHA staging before post-capture KV sizing (#40256)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/pool_host/mha.py` _+3 more__
- **2026-09-21** [`7ad55e4386`](https://github.com/sgl-project/sglang/commit/7ad55e4386) [#40278](https://github.com/sgl-project/sglang/pull/40278)
  [HiCache] TMA-staged host<->device KV transfer kernel (sm_90+) (#40278)
  _Files: `python/sglang/kernels/jit/csrc/kvcacheio/hicache_tma.cuh`, `python/sglang/kernels/ops/kvcache/hicache.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/pool_host/mha.py` _+3 more__
- **2026-09-21** [`0cb37c018c`](https://github.com/sgl-project/sglang/commit/0cb37c018c) [#40517](https://github.com/sgl-project/sglang/pull/40517)
  [KDA] Enable ReplaySSM for GLM-5.3 Flash (#40517)
  _Files: `python/sglang/srt/configs/hybrid_arch.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`_
- **2026-09-21** [`3c71bb018a`](https://github.com/sgl-project/sglang/commit/3c71bb018a) [#37889](https://github.com/sgl-project/sglang/pull/37889)
  [AMD] Enable GLM DSA prefill top-k to the v2 kernel (#37889)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/ops/attention/dsv4/topk.py`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py` _+1 more__
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

## MoE / Expert Parallel  (71 commits)

- **2026-09-28** [`fa443412c5`](https://github.com/sgl-project/sglang/commit/fa443412c5) [#41161](https://github.com/sgl-project/sglang/pull/41161)
  [AMD] [GLM5] Fuse shared expert into AITER MoE on gfx950 (#41161)
  _Files: `python/sglang/srt/models/glm5_next.py`, `test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py`, `test/registered/unit/layers/moe/test_fused_shared_expert_scaling.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`_
- **2026-09-28** [`85be04978d`](https://github.com/sgl-project/sglang/commit/85be04978d) [#40943](https://github.com/sgl-project/sglang/pull/40943)
  [AMD][DSV4] moe: enable shared-expert fusion on the grouped-topk path (megamoe) (#40943)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-09-28** [`6be9c78cf4`](https://github.com/sgl-project/sglang/commit/6be9c78cf4) [#40664](https://github.com/sgl-project/sglang/pull/40664)
  [Intel GPU] Xpu/weekly simple model enablement 2026 09 21 (#40664)
  _Files: `.pre-commit-config.yaml`, `python/sglang/check_env.py`, `python/sglang/multimodal_gen/test/server/consistency_thresholds/intel_xpu_b60.json`, `python/sglang/multimodal_gen/test/server/perf_baselines/xpu_b60.json` _+8 more__
- **2026-09-28** [`cc012abd21`](https://github.com/sgl-project/sglang/commit/cc012abd21) [#41002](https://github.com/sgl-project/sglang/pull/41002)
  [CI] fix CI regression on xeon (#41002)
  _Files: `test/registered/cpu/test_subblock_sparse_attention.py`, `test/registered/moe/test_hash_topk.py`_
- **2026-09-27** [`81f27fb3a7`](https://github.com/sgl-project/sglang/commit/81f27fb3a7) [#41443](https://github.com/sgl-project/sglang/pull/41443)
  [Refactor] Replace LayerScatterModes with LayerFacts and remove ScatterMode (#41443)
  _Files: `python/sglang/srt/layers/communicator/__init__.py`, `python/sglang/srt/layers/communicator/layer.py`, `python/sglang/srt/layers/communicator/layout.py`, `python/sglang/srt/models/bailing_moe.py` _+45 more__
- **2026-09-27** [`06d012eaca`](https://github.com/sgl-project/sglang/commit/06d012eaca) [#41442](https://github.com/sgl-project/sglang/pull/41442)
  [Refactor] Give a layer its CuTe DSL kernels at construction instead of a subclass (#41442)
  _Files: `python/sglang/srt/layers/communicator/layer.py`, `python/sglang/srt/layers/moe/cutedsl_ar_fusion.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/qwen3_5.py` _+1 more__
- **2026-09-27** [`341d5273bd`](https://github.com/sgl-project/sglang/commit/341d5273bd) [#41441](https://github.com/sgl-project/sglang/pull/41441)
  [Refactor] Build the boundary into any stage with one construction (#41441)
  _Files: `python/sglang/srt/layers/communicator/__init__.py`, `python/sglang/srt/layers/communicator/boundary.py`, `python/sglang/srt/layers/communicator/layer.py`, `python/sglang/srt/layers/communicator/ops.py` _+12 more__
- **2026-09-27** [`644014bc98`](https://github.com/sgl-project/sglang/commit/644014bc98) [#41440](https://github.com/sgl-project/sglang/pull/41440)
  [Refactor] Declare each stage's residual read and update, and give each stage its own entry (#41440)
  _Files: `python/sglang/srt/layers/communicator/__init__.py`, `python/sglang/srt/layers/communicator/boundary.py`, `python/sglang/srt/layers/communicator/layer.py`, `python/sglang/srt/layers/communicator/ops.py` _+18 more__
- **2026-09-27** [`0e907b755d`](https://github.com/sgl-project/sglang/commit/0e907b755d) [#41439](https://github.com/sgl-project/sglang/pull/41439)
  [Refactor] Split the layer communicator into a package (move only) (#41439)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator/__init__.py` _+36 more__
- **2026-09-27** [`427c9e05c1`](https://github.com/sgl-project/sglang/commit/427c9e05c1) [#41438](https://github.com/sgl-project/sglang/pull/41438)
  [Refactor] Choose every layer's boundaries from declarations and remove the scatter-mode selection (#41438)
  _Files: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/layers/attention/dsa/dsa_npu_indexer.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_mhc.py` _+8 more__
- **2026-09-27** [`4fac02fe5d`](https://github.com/sgl-project/sglang/commit/4fac02fe5d) [#41435](https://github.com/sgl-project/sglang/pull/41435)
  [Refactor] Choose MoE layers' boundaries from declarations when moe_dp_size equals attn_cp_size (#41435)
  _Files: `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `test/registered/unit/layers/test_boundary_edges.py`, `test/registered/unit/layers/test_declared_decoder_boundary.py`_
- **2026-09-27** [`31329c222c`](https://github.com/sgl-project/sglang/commit/31329c222c) [#41432](https://github.com/sgl-project/sglang/pull/41432)
  [Fix] Run MoE layers under attention DP and GQA prefill CP on the declared DP × CP gather (#41432)
  _Files: `python/sglang/srt/layers/communicator.py`, `test/registered/unit/layers/test_declared_decoder_boundary.py`, `test/registered/unit/layers/test_dp_attention_cp_gather.py`_
- **2026-09-27** [`f0ecf15c84`](https://github.com/sgl-project/sglang/commit/f0ecf15c84) [#41431](https://github.com/sgl-project/sglang/pull/41431)
  [Refactor] Move CuTe DSL-fused layers onto the declared boundaries and FFN-exit kernel entries (#41431)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/cutedsl_ar_fusion.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/qwen2_moe.py` _+4 more__
- **2026-09-27** [`6f370c3bcd`](https://github.com/sgl-project/sglang/commit/6f370c3bcd) [#41429](https://github.com/sgl-project/sglang/pull/41429)
  [Refactor] Build each decoder boundary from the declarations of its two sides (#41429)
  _Files: `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `test/registered/unit/layers/moe/test_cutedsl_ar_fusion.py`, `test/registered/unit/layers/test_boundary_edges.py` _+8 more__
- **2026-09-27** [`c289656434`](https://github.com/sgl-project/sglang/commit/c289656434) [#41427](https://github.com/sgl-project/sglang/pull/41427)
  [Refactor] Let the MoE declare whether its skipped reduction is one TP all-reduce (#41427)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/__init__.py`, `python/sglang/srt/layers/moe/utils.py`, `test/registered/unit/layers/test_declared_decoder_boundary.py` _+1 more__
- **2026-09-27** [`deaa7f1463`](https://github.com/sgl-project/sglang/commit/deaa7f1463) [#41426](https://github.com/sgl-project/sglang/pull/41426)
  [Refactor] Run two-batch-overlap layers on the declared boundaries (#41426)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/deepseek_v2.py` _+12 more__
- **2026-09-27** [`846181f1c4`](https://github.com/sgl-project/sglang/commit/846181f1c4) [#41418](https://github.com/sgl-project/sglang/pull/41418)
  [Refactor] Give the fused prepare_mlp kernels an explicit contract (#41418)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/cutedsl_ar_fusion.py`, `test/registered/unit/layers/moe/test_cutedsl_ar_fusion.py`, `test/registered/unit/layers/test_declared_decoder_boundary.py`_
- **2026-09-27** [`446d181e23`](https://github.com/sgl-project/sglang/commit/446d181e23) [#41417](https://github.com/sgl-project/sglang/pull/41417)
  [Refactor] Choose the boundaries of plain-TP dense layers and MoE layers from declarations (#41417)
  _Files: `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/cutedsl_ar_fusion.py`, `test/registered/unit/layers/moe/test_cutedsl_ar_fusion.py` _+1 more__
- **2026-09-27** [`b252aceffe`](https://github.com/sgl-project/sglang/commit/b252aceffe) [#41458](https://github.com/sgl-project/sglang/pull/41458)
  [AMD] Update v4 cookbook for megamoe, fp8 kv attn, BCG (#41458)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-27** [`effb752188`](https://github.com/sgl-project/sglang/commit/effb752188) [#41019](https://github.com/sgl-project/sglang/pull/41019)
  dsv4.1-amd: KV cache layouts, FP4 indexer, compressor and router kernels (#41019)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c1.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/fp4_indexer_rope.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/fp4_indexer_rope_hip.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh` _+22 more__
- **2026-09-27** [`425a1f8f24`](https://github.com/sgl-project/sglang/commit/425a1f8f24) [#41377](https://github.com/sgl-project/sglang/pull/41377)
  [AMD] Honor an explicit triton moe_runner_backend for mxfp8 on ROCm (#41377)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `test/registered/unit/test_mxfp8_moe_runner_backend.py`_
- **2026-09-26** [`e1e97e8b49`](https://github.com/sgl-project/sglang/commit/e1e97e8b49) [#41292](https://github.com/sgl-project/sglang/pull/41292)
  Pin triton_kernels num_warps for MXFP4 MoE below Hopper (6x gpt-oss decode on RTX 4090) (#41292)
  _Files: `python/sglang/srt/layers/quantization/mxfp4.py`_
- **2026-09-26** [`bd37e7f513`](https://github.com/sgl-project/sglang/commit/bd37e7f513) [#41257](https://github.com/sgl-project/sglang/pull/41257)
  [Refactor] Choose a dense layer's boundaries under attention DP from both sides' declarations (#41257)
  _Files: `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/layers/communicator_mhc.py` _+7 more__
- **2026-09-26** [`35b369ebba`](https://github.com/sgl-project/sglang/commit/35b369ebba) [#41254](https://github.com/sgl-project/sglang/pull/41254)
  [Refactor] Declare at construction the layers whose FFN completes its own reduction (#41254)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/gigachat35.py` _+13 more__
- **2026-09-26** [`8fc3ce48da`](https://github.com/sgl-project/sglang/commit/8fc3ce48da) [#41252](https://github.com/sgl-project/sglang/pull/41252)
  [Refactor] Choose prepare_attn / prepare_mlp steps and fused kernels at construction (#41252)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/layers/communicator_mhc.py`, `python/sglang/srt/layers/moe/cutedsl_ar_fusion.py` _+6 more__
- **2026-09-25** [`3450d68d4e`](https://github.com/sgl-project/sglang/commit/3450d68d4e) [#41200](https://github.com/sgl-project/sglang/pull/41200)
  [Refactor] Decide an FFN exit's completion once and declare the group it owes (#41200)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `python/sglang/srt/layers/moe/__init__.py`, `python/sglang/srt/layers/moe/utils.py` _+8 more__
- **2026-09-25** [`26a3214cda`](https://github.com/sgl-project/sglang/commit/26a3214cda) [#41199](https://github.com/sgl-project/sglang/pull/41199)
  [Refactor] Take a layer's last-layer fact from its scatter-mode plan (#41199)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/layers/communicator_mhc.py`, `python/sglang/srt/models/bailing_moe.py` _+24 more__
- **2026-09-25** [`9d7f44bdbb`](https://github.com/sgl-project/sglang/commit/9d7f44bdbb) [#41196](https://github.com/sgl-project/sglang/pull/41196)
  [Refactor] Carry a deferred FFN all-reduce as UnreducedOutput and complete it in the next layer without the fused kernel (#41196)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_mhc.py`, `python/sglang/srt/layers/moe/__init__.py` _+23 more__
- **2026-09-25** [`402df23188`](https://github.com/sgl-project/sglang/commit/402df23188) [#41195](https://github.com/sgl-project/sglang/pull/41195)
  [Fix] Stop counting a deferred FFN sum more than once: replicated TP1 shared expert, dense reduce_scatterv (#41195)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/deepseek_v2.py` _+5 more__
- **2026-09-25** [`1409f469be`](https://github.com/sgl-project/sglang/commit/1409f469be) [#41194](https://github.com/sgl-project/sglang/pull/41194)
  [Fix] Plan NextN / MTP draft layers as one-layer models and fix the Bailing V2 NextN draft (#41194)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/step3p5.py` _+2 more__
- **2026-09-25** [`515f5be77e`](https://github.com/sgl-project/sglang/commit/515f5be77e) [#35619](https://github.com/sgl-project/sglang/pull/35619)
  [AMD] Integrate Aiter MegaMoEv2 for DeepSeek-V4 (#35619)
  _Files: `python/sglang/srt/arg_groups/mega_moe_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/eplb/eplb_map_record_fused.py`, `python/sglang/srt/eplb/expert_distribution.py` _+11 more__
- **2026-09-25** [`0fb699ac03`](https://github.com/sgl-project/sglang/commit/0fb699ac03) [#41067](https://github.com/sgl-project/sglang/pull/41067)
  [diffusion] model: support Ming-Image Design and Design-Layer (#41067)
  _Files: `docs/cookbook/diffusion/inclusionAI/Ming-Image.mdx`, `docs/cookbook/diffusion/intro.mdx`, `docs/docs.json`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx` _+29 more__
- **2026-09-25** [`9c8340a2e5`](https://github.com/sgl-project/sglang/commit/9c8340a2e5) [#41201](https://github.com/sgl-project/sglang/pull/41201)
  [DeepEP v2] Let a model package supply its per-rank prefill dispatch bound (#41201)
  _Files: `python/sglang/srt/arg_groups/moe_hook.py`, `python/sglang/srt/configs/moe_model_registry.py`, `test/registered/unit/layers/moe/test_hpc_ops_runner_guard.py`_
- **2026-09-25** [`e0b4d66733`](https://github.com/sgl-project/sglang/commit/e0b4d66733) [#41061](https://github.com/sgl-project/sglang/pull/41061)
  [Perf] Lazy-load built-in model definitions and nixl_ep at startup (#41061)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/nixl.py`, `python/sglang/srt/model_loader/utils.py`, `python/sglang/srt/models/registry.py`, `test/registered/unit/models/test_model_registry.py`_
- **2026-09-24** [`36f59982fa`](https://github.com/sgl-project/sglang/commit/36f59982fa) [#36559](https://github.com/sgl-project/sglang/pull/36559)
  MoE: small-batch sorting path with fused mxfp8 quantisation (#36559)
  _Files: `python/sglang/kernels/ops/moe/moe_sorting_small.py`, `python/sglang/kernels/ops/moe/mxfp8_moe_amd_gfx95.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py` _+1 more__
- **2026-09-24** [`0b53305f48`](https://github.com/sgl-project/sglang/commit/0b53305f48) [#36574](https://github.com/sgl-project/sglang/pull/36574)
  MiniMax-M3: MXFP8 dense-only block convert + aiter MXFP8 MoE on gfx950 (#36574)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` _+1 more__
- **2026-09-24** [`62ae032c46`](https://github.com/sgl-project/sglang/commit/62ae032c46) [#41097](https://github.com/sgl-project/sglang/pull/41097)
  [Refactor] Share the MoE output all-reduce between models (#41097)
  _Files: `python/sglang/srt/layers/moe/__init__.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_linear.py` _+17 more__
- **2026-09-24** [`5df1667077`](https://github.com/sgl-project/sglang/commit/5df1667077) [#41081](https://github.com/sgl-project/sglang/pull/41081)
  [Refactor] Pass each layer stack's output through a communicator exit (#41081)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/bailing_moe_nextn.py` _+29 more__
- **2026-09-24** [`07a3735e94`](https://github.com/sgl-project/sglang/commit/07a3735e94) [#41080](https://github.com/sgl-project/sglang/pull/41080)
  [Fix] Complete the deferred FFN all-reduce before deepstack addition and aux hidden-state capture (#41080)
  _Files: `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_v3.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py` _+7 more__
- **2026-09-24** [`928e683f94`](https://github.com/sgl-project/sglang/commit/928e683f94) [#41079](https://github.com/sgl-project/sglang/pull/41079)
  [Fix] Complete the deferred FFN all-reduce before a pipeline-parallel send (#41079)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/bailing_moe_v3.py` _+19 more__
- **2026-09-24** [`5bb24e399d`](https://github.com/sgl-project/sglang/commit/5bb24e399d) [#38726](https://github.com/sgl-project/sglang/pull/38726)
  [Quant] ModelOpt mixed precision: dispatch block-FP8 MoE experts and derive the block size (#38726)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/unit/model_loader/test_modelopt_loader.py`_
- **2026-09-24** [`ea5baf4022`](https://github.com/sgl-project/sglang/commit/ea5baf4022) [#40922](https://github.com/sgl-project/sglang/pull/40922)
  [Refactor] Retire the model-specific Kimi K3 kernel namespace (#40922)
  _Files: `python/sglang/kernels/README.md`, `python/sglang/kernels/ops/__init__.py`, `python/sglang/kernels/ops/activation/__init__.py`, `python/sglang/kernels/ops/activation/_jit_situ_and_mul.py` _+48 more__
- **2026-09-24** [`3177d10ca6`](https://github.com/sgl-project/sglang/commit/3177d10ca6) [#39816](https://github.com/sgl-project/sglang/pull/39816)
  Refactor the Cute-DSL AR fusion to support DeepseekV2 archs (GLM-5.3, etc.) (#39816)
  _Files: `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/moe_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/distributed/bootstrap.py` _+16 more__
- **2026-09-24** [`ce06a14444`](https://github.com/sgl-project/sglang/commit/ce06a14444) [#40612](https://github.com/sgl-project/sglang/pull/40612)
  [Diffusion] migrate the whole _register_configs from registry.py to the model own config file (#40612)
  _Files: `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/ernie_image.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/flux.py` _+28 more__
- **2026-09-24** [`32290dda2c`](https://github.com/sgl-project/sglang/commit/32290dda2c) [#40204](https://github.com/sgl-project/sglang/pull/40204)
  [AMD] Small-M MXFP4 fused-MoE kernel for gfx950 (Qwen) (#40204)
  _Files: `python/sglang/kernels/ops/moe/smallm_moe_gfx950/__init__.py`, `python/sglang/kernels/ops/moe/smallm_moe_gfx950/smallm_moe.hip`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `test/registered/amd/test_smallm_moe_gfx950.py`_
- **2026-09-24** [`77983865d8`](https://github.com/sgl-project/sglang/commit/77983865d8) [#39939](https://github.com/sgl-project/sglang/pull/39939)
  [Moe] Honor swiglu_limit clamped activation in flashinfer_cutlass runner (#39939)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutlass.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4_moe.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/layers/quantization/unquant.py` _+1 more__
- **2026-09-24** [`f4d9d2e670`](https://github.com/sgl-project/sglang/commit/f4d9d2e670) [#40777](https://github.com/sgl-project/sglang/pull/40777)
  [RL] Add RL weight-update sessions and support updating spec draft runners (#40777)
  _Files: `docs/docs/advanced_features/sglang_for_rl.mdx`, `python/sglang/srt/entrypoints/EngineBase.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py` _+33 more__
- **2026-09-24** [`81b81664a6`](https://github.com/sgl-project/sglang/commit/81b81664a6) [#40946](https://github.com/sgl-project/sglang/pull/40946)
  Revert "[AMD] Fix DeepSeek-V4 accuracy by not passing num_token_non_padded to MoE topk" (#40946)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-09-23** [`f766397f2e`](https://github.com/sgl-project/sglang/commit/f766397f2e) [#40971](https://github.com/sgl-project/sglang/pull/40971)
  [Refactor] Trim server configuration and runtime context comments (#40971)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/choices.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/field_order.py` _+49 more__
- **2026-09-23** [`ab0c31bd94`](https://github.com/sgl-project/sglang/commit/ab0c31bd94) [#40871](https://github.com/sgl-project/sglang/pull/40871)
  [Refactor] Move eleven more MoE models to LayerCommunicator.ffn_exit (#40871)
  _Files: `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/bailing_moe_v3.py`, `python/sglang/srt/models/glm4_moe_lite.py` _+7 more__
- **2026-09-23** [`e1048a215c`](https://github.com/sgl-project/sglang/commit/e1048a215c) [#40870](https://github.com/sgl-project/sglang/pull/40870)
  [Refactor] Let LayerCommunicator own the FFN exit in Qwen3-MoE, DeepSeek-V2 and GLM4-MoE (#40870)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/qwen3_moe.py` _+1 more__
- **2026-09-23** [`e31cbc01a2`](https://github.com/sgl-project/sglang/commit/e31cbc01a2) [#40868](https://github.com/sgl-project/sglang/pull/40868)
  [Fix] Stop deferring the last layer's FFN all-reduce in five models (#40868)
  _Files: `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/bailing_moe_nextn.py`, `python/sglang/srt/models/minimax_m3.py` _+4 more__
- **2026-09-23** [`0e80c73c92`](https://github.com/sgl-project/sglang/commit/0e80c73c92) [#40799](https://github.com/sgl-project/sglang/pull/40799)
  [Fix] Avoid duplicate residual in LongCat MoE shortcut (#40799)
  _Files: `python/sglang/srt/models/longcat_flash.py`, `test/registered/unit/models/test_longcat_flash_shortcut.py`_
- **2026-09-23** [`5c154c214d`](https://github.com/sgl-project/sglang/commit/5c154c214d) [#40895](https://github.com/sgl-project/sglang/pull/40895)
  Revert " [NPU] Enable piecewise CUDA graph support on NPU" (#40895)
  _Files: `python/sglang/kernels/ops/attention/fla/layernorm_gated.py`, `python/sglang/kernels/ops/elementwise/elementwise.py`, `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/compilation/npu_piecewise_backend.py` _+8 more__
- **2026-09-23** [`16e353d93e`](https://github.com/sgl-project/sglang/commit/16e353d93e) [#40438](https://github.com/sgl-project/sglang/pull/40438)
  [NPU] Skip fused gmm1+swiglu for swiglu_limit (SiLU-with-clamp) checkpoints (#40438)
  _Files: `python/sglang/srt/layers/moe/moe_runner/ascend.py`_
- **2026-09-23** [`2d25767759`](https://github.com/sgl-project/sglang/commit/2d25767759) [#28417](https://github.com/sgl-project/sglang/pull/28417)
  [NPU] Enable piecewise CUDA graph support on NPU (#28417)
  _Files: `python/sglang/kernels/ops/attention/fla/layernorm_gated.py`, `python/sglang/kernels/ops/elementwise/elementwise.py`, `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/compilation/npu_piecewise_backend.py` _+8 more__
- **2026-09-23** [`de123f38bb`](https://github.com/sgl-project/sglang/commit/de123f38bb) [#33723](https://github.com/sgl-project/sglang/pull/33723)
  [3/N] elastic-ep: Recapture decode CUDA graphs after scale-up (#33723)
  _Files: `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/elastic_ep/elastic_ep.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` _+14 more__
- **2026-09-23** [`aa0b65c7c7`](https://github.com/sgl-project/sglang/commit/aa0b65c7c7) [#39804](https://github.com/sgl-project/sglang/pull/39804)
  [AMD] Fix DeepSeek-V4 accuracy by not passing num_token_non_padded to MoE topk (#39804)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-09-23** [`d4dcce12d4`](https://github.com/sgl-project/sglang/commit/d4dcce12d4) [#35958](https://github.com/sgl-project/sglang/pull/35958)
  [npu] decoding procedure optimization on qwen3.5/3.6 (#35958)
  _Files: `python/sglang/srt/layers/attention/linear/kernels/gdn_triton.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`_
- **2026-09-23** [`28be39f72e`](https://github.com/sgl-project/sglang/commit/28be39f72e) [#40466](https://github.com/sgl-project/sglang/pull/40466)
  [deepep_v2] support GLM-5.3-Flash (Glm5NextForConditionalGeneration) (#40466)
  _Files: `python/sglang/srt/configs/moe_model_registry.py`, `python/sglang/srt/models/glm5_next.py`_
- **2026-09-23** [`40048f6e51`](https://github.com/sgl-project/sglang/commit/40048f6e51) [#34061](https://github.com/sgl-project/sglang/pull/34061)
  [dLLM] feat: support DiffusionGemma serving (#34061)
  _Files: `benchmark/dllm/README.md`, `benchmark/dllm/bench_diffusion_gemma.py`, `python/sglang/srt/arg_groups/dllm_hook.py`, `python/sglang/srt/arg_groups/model_overrides/gemma4.py` _+28 more__
- **2026-09-22** [`7b977ce5dc`](https://github.com/sgl-project/sglang/commit/7b977ce5dc) [#40672](https://github.com/sgl-project/sglang/pull/40672)
  [Fix] Decide the MoE padded-row bound from the layer scatter mode (#40672)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/bailing_moe.py` _+17 more__
- **2026-09-22** [`b44e248682`](https://github.com/sgl-project/sglang/commit/b44e248682) [#38546](https://github.com/sgl-project/sglang/pull/38546)
  [AMD] [GLM-5.3-Flash Day 0] Enable FP8 and Quark MXFP4 MoE on gfx950 (#38546)
  _Files: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` _+4 more__
- **2026-09-22** [`56fee88e23`](https://github.com/sgl-project/sglang/commit/56fee88e23) [#35504](https://github.com/sgl-project/sglang/pull/35504)
  fix(moe): support Llama4 NVFP4 router input weights on SM120 (#35504)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutlass.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`_
- **2026-09-21** [`0c53fec476`](https://github.com/sgl-project/sglang/commit/0c53fec476) [#39775](https://github.com/sgl-project/sglang/pull/39775)
  [ROCm] fix: remove extra bf16 -> fp32 cast in jit grouped topk kernel path (#39775)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-09-21** [`8bde82c0ad`](https://github.com/sgl-project/sglang/commit/8bde82c0ad) [#39339](https://github.com/sgl-project/sglang/pull/39339)
  [AMD] [GLM-5.3-Flash Day 0] Build the fused DSA k-pool top-k JIT kernel on HIP (#39339)
  _Files: `python/sglang/kernels/jit/csrc/dsa/kpool_topk_transform.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh`, `test/registered/kernels/ops/moe/test_kpool_topk_transform_fused.py`_
- **2026-09-21** [`1ed6822039`](https://github.com/sgl-project/sglang/commit/1ed6822039) [#40617](https://github.com/sgl-project/sglang/pull/40617)
  [Test] Anchor `basic_perf` thresholds to each metric's measured spread (#40617)
  _Files: `test/registered/basic_perf/test_embeddings_api.py`, `test/registered/basic_perf/test_lora_latency.py`, `test/registered/basic_perf/test_moe_throughput.py`, `test/registered/basic_perf/test_pp_throughput.py` _+5 more__
- **2026-09-21** [`90b3f8544c`](https://github.com/sgl-project/sglang/commit/90b3f8544c) [#39986](https://github.com/sgl-project/sglang/pull/39986)
  [AMD] Use Triton softmax routing for Qwen3.5 on gfx950 (#39986)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/amd/test_qwen35_moe_softmax_topk.py`_
- **2026-09-21** [`f702a0be29`](https://github.com/sgl-project/sglang/commit/f702a0be29) [#40611](https://github.com/sgl-project/sglang/pull/40611)
  Revert "[Diffusion] migrate the whole _register_configs from registry.py to the model own config file" (#40611)
  _Files: `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/ernie_image.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/flux.py` _+28 more__
- **2026-09-21** [`e6931ca889`](https://github.com/sgl-project/sglang/commit/e6931ca889) [#40475](https://github.com/sgl-project/sglang/pull/40475)
  [Diffusion] migrate the whole _register_configs from registry.py to the model own config file (#40475)
  _Files: `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/ernie_image.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/flux.py` _+28 more__
- **2026-09-21** [`800613a74b`](https://github.com/sgl-project/sglang/commit/800613a74b) [#40505](https://github.com/sgl-project/sglang/pull/40505)
  [Test] Split the serving perf tests by topic into `basic_perf/` and route their thresholds through a kit (#40505)
  _Files: `python/sglang/test/kits/perf_bench_kit.py`, `python/sglang/test/kits/vlm_perf_kit.py`, `python/sglang/test/test_utils.py`, `test/registered/basic_perf/test_eagle3_latency.py` _+17 more__

## Multimodal  (51 commits)

- **2026-09-28** [`2e7e0802f4`](https://github.com/sgl-project/sglang/commit/2e7e0802f4) [#41339](https://github.com/sgl-project/sglang/pull/41339)
  [diffusion] Qwen-Image 2.1: fuse Q/K RMSNorm + RoPE + KV packing into one CUDA kernel and project Q/K/V with one packed GEMM (#41339)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_complex_rope.cuh`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/qknorm_complex_rope_jit.py` _+5 more__
- **2026-09-28** [`090439bf8f`](https://github.com/sgl-project/sglang/commit/090439bf8f) [#41540](https://github.com/sgl-project/sglang/pull/41540)
  [diffusion] docs: consolidate Qwen-Image 2.1 guidance in its cookbook (#41540)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `python/sglang/multimodal_gen/README.md`_
- **2026-09-28** [`6caf0ff4ae`](https://github.com/sgl-project/sglang/commit/6caf0ff4ae) [#39539](https://github.com/sgl-project/sglang/pull/39539)
  perf(multimodal): offload CPU feature hashing with bounded admission (#39539)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/hash_executor.py`, `test/registered/unit/managers/test_mm_hashes.py`_
- **2026-09-28** [`c02eaadeb2`](https://github.com/sgl-project/sglang/commit/c02eaadeb2) [#40439](https://github.com/sgl-project/sglang/pull/40439)
  [diffusion] optimization: populate cpu weight stores before host registration to speedup layerwise-offload initialization (#40439)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-09-28** [`6c4f36e47a`](https://github.com/sgl-project/sglang/commit/6c4f36e47a) [#39679](https://github.com/sgl-project/sglang/pull/39679)
  Rust server unify datapath for mm and generate requests (#39679)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/rust_server/multimodal.py`, `python/sglang/srt/rust_server/server.py`, `python/sglang/test/server_fixtures/rust_mm_transport_fixture.py` _+49 more__
- **2026-09-28** [`8b2ca8ecc2`](https://github.com/sgl-project/sglang/commit/8b2ca8ecc2) [#38762](https://github.com/sgl-project/sglang/pull/38762)
  [diffusion] feat: support multiple task types for pipelines (#38762)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py` _+21 more__
- **2026-09-27** [`b2800461e5`](https://github.com/sgl-project/sglang/commit/b2800461e5) [#41266](https://github.com/sgl-project/sglang/pull/41266)
  [Diffusion] Reuse bit-exact packed SwiGLU for Ming-Image (#41266)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/ming_image.py`_
- **2026-09-27** [`84622ce9d5`](https://github.com/sgl-project/sglang/commit/84622ce9d5) [#41272](https://github.com/sgl-project/sglang/pull/41272)
  [diffusion] fix: lora-wrapped linears crash qwen-image and minimax-h3 inference (#41272)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`_
- **2026-09-27** [`a0ba1968b1`](https://github.com/sgl-project/sglang/commit/a0ba1968b1) [#34418](https://github.com/sgl-project/sglang/pull/34418)
  [Diffusion] Apply latent-ids and packing to caller-provided initial latents (#34418)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/latent_preparation.py`, `python/sglang/multimodal_gen/test/unit/test_provided_latents_preparation.py`_
- **2026-09-27** [`ae47bcd4da`](https://github.com/sgl-project/sglang/commit/ae47bcd4da) [#35684](https://github.com/sgl-project/sglang/pull/35684)
  [diffusion] feat: minimax-h3 spectrum skip-step + fused RMSNorm/AdaLN (#35684)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/spectrum.mdx`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-performance/SKILL.md`, `python/sglang/multimodal_gen/configs/sample/minimax_h3.py` _+6 more__
- **2026-09-27** [`2a14f65fd7`](https://github.com/sgl-project/sglang/commit/2a14f65fd7) [#36192](https://github.com/sgl-project/sglang/pull/36192)
  [diffusion] feat: support in-place lora merge/unmerge under layerwise offload (#36192)
  _Files: `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py` _+1 more__
- **2026-09-27** [`0bc074db83`](https://github.com/sgl-project/sglang/commit/0bc074db83) [#41305](https://github.com/sgl-project/sglang/pull/41305)
  [KDA+Kimi K3] Speed up SANA-Video residual gate add on H200 (#41305)
  _Files: `python/sglang/kernels/kda_kernels/residual_gate_add_jit.py`_
- **2026-09-27** [`acc15c193b`](https://github.com/sgl-project/sglang/commit/acc15c193b) [#34416](https://github.com/sgl-project/sglang/pull/34416)
  [Diffusion] Preserve per-sample rollout trajectories across multi-output merge (#34416)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/diffusion_generator.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/post_training/rl_dataclasses.py`, `python/sglang/multimodal_gen/test/unit/test_multi_output_rollout_trajectory.py`_
- **2026-09-26** [`e538489e0e`](https://github.com/sgl-project/sglang/commit/e538489e0e) [#41298](https://github.com/sgl-project/sglang/pull/41298)
  [diffusion] fix: copy small files into overlay materialized trees instead of linking them (#41298)
  _Files: `python/sglang/multimodal_gen/runtime/utils/model_overlay.py`, `python/sglang/multimodal_gen/test/unit/test_model_overlay.py`_
- **2026-09-26** [`dfdbff931d`](https://github.com/sgl-project/sglang/commit/dfdbff931d) [#41150](https://github.com/sgl-project/sglang/pull/41150)
  [diffusion] fix: fix Qwen-Image 2.1 default RGBA output (#41150)
  _Files: `python/sglang/multimodal_gen/configs/sample/qwenimage21.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py`_
- **2026-09-26** [`2ee82fe158`](https://github.com/sgl-project/sglang/commit/2ee82fe158) [#41011](https://github.com/sgl-project/sglang/pull/41011)
  [diffusion] model: support Anima Base v1.0 (#41011)
  _Files: `docs/cookbook/diffusion/CircleStone/Anima.mdx`, `docs/docs.json`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/configs/CircleStone/anima.jsx` _+22 more__
- **2026-09-26** [`85374532f2`](https://github.com/sgl-project/sglang/commit/85374532f2) [#40490](https://github.com/sgl-project/sglang/pull/40490)
  [diffusion] Fuse lossless Klein packed QK RMSNorm and RoPE on Hopper (#40490)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/flux2_qknorm_rope_triton.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py` _+1 more__
- **2026-09-25** [`6d35cee7fc`](https://github.com/sgl-project/sglang/commit/6d35cee7fc) [#40621](https://github.com/sgl-project/sglang/pull/40621)
  Fix multimodal feature offload races (#40621)
  _Files: `python/sglang/srt/managers/mm_schedule.py`, `python/sglang/srt/managers/mm_utils.py`_
- **2026-09-25** [`31b931edc3`](https://github.com/sgl-project/sglang/commit/31b931edc3) [#28131](https://github.com/sgl-project/sglang/pull/28131)
  fix(multimodal): return 400 for corrupt image inputs (#28131)
  _Files: `python/sglang/srt/utils/common.py`, `test/registered/unit/utils/test_common.py`_
- **2026-09-25** [`2f5c9ac43d`](https://github.com/sgl-project/sglang/commit/2f5c9ac43d) [#40486](https://github.com/sgl-project/sglang/pull/40486)
  [diffusion] Enable lossless Cosmos3 Super T2I QK fusion on Hopper TP2 (#40486)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/test/unit/test_cosmos3.py`_
- **2026-09-25** [`a749d84303`](https://github.com/sgl-project/sglang/commit/a749d84303) [#34417](https://github.com/sgl-project/sglang/pull/34417)
  [Diffusion] Fix AttributeError in grouped forward_batch by installing the residency manager (#34417)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/composed_pipeline_base.py`, `python/sglang/multimodal_gen/test/unit/test_pipeline_residency_manager_install.py`_
- **2026-09-25** [`6103a8c743`](https://github.com/sgl-project/sglang/commit/6103a8c743) [#41095](https://github.com/sgl-project/sglang/pull/41095)
  [diffusion] feat: add opt-in SRT prompt enhancement to image and video APIs (#41095)
  _Files: `docs/cookbook/diffusion/Ideogram/Ideogram4.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/api/openai_api.mdx`, `docs/docs/sglang-diffusion/models_with_pe.mdx` _+7 more__
- **2026-09-24** [`2f2f9d12f8`](https://github.com/sgl-project/sglang/commit/2f2f9d12f8) [#38965](https://github.com/sgl-project/sglang/pull/38965)
  [Score API] Setwise Scoring Support (#38965)
  _Files: `benchmark/prefill_only/bench_setwise_score.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/engine_score_mixin.py`, `python/sglang/srt/entrypoints/openai/protocol.py` _+14 more__
- **2026-09-24** [`ec7eb6bd79`](https://github.com/sgl-project/sglang/commit/ec7eb6bd79) [#41130](https://github.com/sgl-project/sglang/pull/41130)
  [diffusion] update code owner (#41130)
  _Files: `.github/CODEOWNERS`_
- **2026-09-24** [`c6565c1a6d`](https://github.com/sgl-project/sglang/commit/c6565c1a6d) [#40388](https://github.com/sgl-project/sglang/pull/40388)
  [Diffusion] Enable lossless SANA-Video eager conv fusions for 12.6% lower latency (#40388)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/multimodal_gen/runtime/models/dits/sana.py`, `python/sglang/multimodal_gen/runtime/models/dits/sana_video.py`_
- **2026-09-24** [`26c63335e2`](https://github.com/sgl-project/sglang/commit/26c63335e2) [#40425](https://github.com/sgl-project/sglang/pull/40425)
  [Diffusion] Fuse lossless LingBot World FP32 normalization (#40425)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/kda_kernels/layernorm_modulate_triton.py`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/modulate/scale_shift_triton.py` _+2 more__
- **2026-09-24** [`c85df5becc`](https://github.com/sgl-project/sglang/commit/c85df5becc) [#40405](https://github.com/sgl-project/sglang/pull/40405)
  [Diffusion] Fuse lossless Wan VAE post-ops for LongLive 2 I2V (#40405)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/jit/csrc/elementwise/wan_norm_silu_post.cuh`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/wan_norm_silu_post.py` _+2 more__
- **2026-09-24** [`261cb826e6`](https://github.com/sgl-project/sglang/commit/261cb826e6) [#40384](https://github.com/sgl-project/sglang/pull/40384)
  [Diffusion] Fuse LongCat GELU+cat and support Edit-Turbo BCG (#40384)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/gelu_tanh_cat.cuh`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/activation/gelu_tanh_cat_jit.py`, `python/sglang/multimodal_gen/configs/sample/longcat_image.py` _+6 more__
- **2026-09-24** [`9f6fc55332`](https://github.com/sgl-project/sglang/commit/9f6fc55332) [#37751](https://github.com/sgl-project/sglang/pull/37751)
  [AMD][Diffusion] FlyDSL fused norm kernels on wave32 targets (gfx1250) (#37751)
  _Files: `python/sglang/kernels/ops/diffusion/norm/fused_residual_norm_flydsl.py`_
- **2026-09-24** [`8eedf616f5`](https://github.com/sgl-project/sglang/commit/8eedf616f5) [#41026](https://github.com/sgl-project/sglang/pull/41026)
  [AMD][DI][CI] Say which image the MI355X nightly ran on (#41026)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-09-23** [`8993f790be`](https://github.com/sgl-project/sglang/commit/8993f790be) [#40374](https://github.com/sgl-project/sglang/pull/40374)
  [Diffusion] Fuse lossless SenseNova RoPE for 5% faster H200 inference (#40374)
  _Files: `python/sglang/multimodal_gen/configs/sample/sensenova_u1.py`, `python/sglang/multimodal_gen/runtime/models/sensenova_u1/neo_unify/modeling_qwen3.py`, `python/sglang/multimodal_gen/test/unit/test_sensenova_u1.py`_
- **2026-09-23** [`4e60d70ba4`](https://github.com/sgl-project/sglang/commit/4e60d70ba4) [#40494](https://github.com/sgl-project/sglang/pull/40494)
  [Diffusion] Fuse Joy Image Edit QKV concatenation and avoid QK copies (#40494)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/layout/joint_qkv_cat_triton.py`, `python/sglang/multimodal_gen/runtime/models/dits/joy_image.py` _+1 more__
- **2026-09-23** [`172b1b4825`](https://github.com/sgl-project/sglang/commit/172b1b4825) [#40386](https://github.com/sgl-project/sglang/pull/40386)
  [Diffusion] Accelerate Cosmos3 Edge on Hopper with lossless fusions (#40386)
  _Files: `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/test/unit/test_cosmos3.py`, `test/registered/kernels/benchmark/diffusion/bench_cosmos3_edge_fusions.py` _+1 more__
- **2026-09-23** [`a3d11f9d95`](https://github.com/sgl-project/sglang/commit/a3d11f9d95) [#40599](https://github.com/sgl-project/sglang/pull/40599)
  [diffusion] feat: support permanent lifetime for layerwise resident layers (#40599)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `docs/src/snippets/configs/Qwen/qwen-image-2.1.jsx`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py` _+6 more__
- **2026-09-23** [`58988bee2f`](https://github.com/sgl-project/sglang/commit/58988bee2f) [#40844](https://github.com/sgl-project/sglang/pull/40844)
  [AMD] Add diffusion (Wan2.2) extras to gfx1151 Docker image (#40844)
  _Files: `docker/rocm-gfx1151.Dockerfile`, `python/pyproject_other.toml`_
- **2026-09-23** [`973fb44471`](https://github.com/sgl-project/sglang/commit/973fb44471) [#40568](https://github.com/sgl-project/sglang/pull/40568)
  [Diffusion] Support MiniMax-H3 PDD(Parallel Decoding Distillation) inference (#40568)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/timestep_preparation.py` _+3 more__
- **2026-09-23** [`c2bc456b64`](https://github.com/sgl-project/sglang/commit/c2bc456b64) [#40818](https://github.com/sgl-project/sglang/pull/40818)
  [chore] point agents at the cookbook before test configs (#40818)
  _Files: `.claude/rules/cookbook-first.md`, `python/sglang/multimodal_gen/.claude/CLAUDE.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-performance/SKILL.md`_
- **2026-09-22** [`8ab21c8a94`](https://github.com/sgl-project/sglang/commit/8ab21c8a94) [#40639](https://github.com/sgl-project/sglang/pull/40639)
  [ci] publish renderer image (#40639)
  _Files: `.github/workflows/release-docker-renderer.yml`_
- **2026-09-22** [`4a1b69abc8`](https://github.com/sgl-project/sglang/commit/4a1b69abc8) [#40593](https://github.com/sgl-project/sglang/pull/40593)
  [diffusion] docs: correct the resident-layer help text to match its scope (#40593)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py` _+1 more__
- **2026-09-22** [`2524b61f9b`](https://github.com/sgl-project/sglang/commit/2524b61f9b) [#40592](https://github.com/sgl-project/sglang/pull/40592)
  [diffusion] feat: allow a component use retain its layerwise resident set (#40592)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_residency_strategies.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-09-22** [`5f9c6b9eb0`](https://github.com/sgl-project/sglang/commit/5f9c6b9eb0) [#40590](https://github.com/sgl-project/sglang/pull/40590)
  [diffusion] fix: separate a use-scoped layerwise release from release_all (#40590)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_residency_strategies.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-09-22** [`a1b2b976fe`](https://github.com/sgl-project/sglang/commit/a1b2b976fe) [#40507](https://github.com/sgl-project/sglang/pull/40507)
  [diffusion] CI: restore public Qwen-Image 2.1 TP2 E2E coverage (#40507)
  _Files: `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/test_utils.py`_
- **2026-09-22** [`582389cec5`](https://github.com/sgl-project/sglang/commit/582389cec5) [#40646](https://github.com/sgl-project/sglang/pull/40646)
  [Fix] Keep diffusion encoder TP context bindings consistent (#40646)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/test/unit/test_component_accuracy_parallel_runtime.py`_
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

## Prefill / Decode Disaggregation  (48 commits)

- **2026-09-28** [`e75e3b8a98`](https://github.com/sgl-project/sglang/commit/e75e3b8a98) [#30899](https://github.com/sgl-project/sglang/pull/30899)
  [Bugfix] fix(hicache): wait for decode offload before retraction (#30899)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_
- **2026-09-28** [`55cc90b533`](https://github.com/sgl-project/sglang/commit/55cc90b533) [#41378](https://github.com/sgl-project/sglang/pull/41378)
  [CI] Real-model Kimi-Linear PD parity at page, DCP virtual-page, chunk and cached-prefix boundaries (#41378)
  _Files: `python/sglang/test/kits/pd_parity_kit.py`, `test/registered/disaggregation/test_disaggregation_kimi_linear.py`_
- **2026-09-27** [`14ab74ef95`](https://github.com/sgl-project/sglang/commit/14ab74ef95) [#41402](https://github.com/sgl-project/sglang/pull/41402)
  [PD] Fan drain abort ACKs out to every decode peer of the room (#41402)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/disaggregation/test_deferred_decode_kv_release.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py` _+1 more__
- **2026-09-27** [`f1e62e3a2e`](https://github.com/sgl-project/sglang/commit/f1e62e3a2e) [#35990](https://github.com/sgl-project/sglang/pull/35990)
  [diffusion] feat: add MiniMax-H3 to ComfyUI integrated mode (#35990)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs.json`, `docs/docs/sglang-diffusion/comfyui.mdx`, `docs/docs/sglang-diffusion/index.mdx` _+58 more__
- **2026-09-27** [`d27efca353`](https://github.com/sgl-project/sglang/commit/d27efca353) [#41312](https://github.com/sgl-project/sglang/pull/41312)
  [mem_cache] Never free the protected prefix on request release (#41312)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/disaggregation/test_specv2_kvcache_offloading.py`_
- **2026-09-26** [`7bdd8fe6ec`](https://github.com/sgl-project/sglang/commit/7bdd8fe6ec) [#41321](https://github.com/sgl-project/sglang/pull/41321)
  [CI] Merge the Kimi-Linear PD DCP4 nightly tests and drop exact-token parity (#41321)
  _Files: `test/registered/disaggregation/test_kimi_linear_pd_dcp4.py`, `test/registered/e2e/disaggregation/test_kimi_linear_pd_dcp4.py`, `test/registered/e2e/disaggregation/test_kimi_linear_pd_dcp4_dspark.py`_
- **2026-09-26** [`3ecb6cd729`](https://github.com/sgl-project/sglang/commit/3ecb6cd729) [#41276](https://github.com/sgl-project/sglang/pull/41276)
  [MemCache] Unify component eviction cursors and lock receipts (#41276)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py` _+29 more__
- **2026-09-26** [`f35ec18d8b`](https://github.com/sgl-project/sglang/commit/f35ec18d8b) [#41297](https://github.com/sgl-project/sglang/pull/41297)
  [Test] Remove more unit tests that mirror implementation or never run in CI (#41297)
  _Files: `test/registered/unit/configs/test_linear_attn_model_registry.py`, `test/registered/unit/constrained/test_base_grammar_backend.py`, `test/registered/unit/constrained/test_grammar_manager.py`, `test/registered/unit/disaggregation/test_encode_server.py` _+52 more__
- **2026-09-26** [`4273e7de77`](https://github.com/sgl-project/sglang/commit/4273e7de77) [#41261](https://github.com/sgl-project/sglang/pull/41261)
  [PD] fix: cache resumed decode-radix requests from root instead of an unlocked re-match (#41261)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/mem_cache/test_decode_radix_lock_ref.py`_
- **2026-09-26** [`50e50e13ab`](https://github.com/sgl-project/sglang/commit/50e50e13ab) [#39731](https://github.com/sgl-project/sglang/pull/39731)
  [DCP] Use logical token capacity for PD admission and load reporting (#39731)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` _+2 more__
- **2026-09-25** [`efd9a40bb8`](https://github.com/sgl-project/sglang/commit/efd9a40bb8) [#39660](https://github.com/sgl-project/sglang/pull/39660)
  [PD] Share one head-slice helper across mooncake, mori, and nixl (#39660)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/disaggregation/test_disaggregation_different_tp.py` _+1 more__
- **2026-09-25** [`516ab77619`](https://github.com/sgl-project/sglang/commit/516ab77619) [#41280](https://github.com/sgl-project/sglang/pull/41280)
  [Test] Route all sgl-eval benchmarks through run_sgl_eval and deprecate run_eval (#41280)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`, `docs/docs/developer_guide/evaluating_new_models.mdx`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/ascend/test_ascend_utils.py` _+40 more__
- **2026-09-25** [`cf5df82680`](https://github.com/sgl-project/sglang/commit/cf5df82680) [#38652](https://github.com/sgl-project/sglang/pull/38652)
  [KVCache] Support lmcache unified radix cache (#38652)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/arg_groups/mamba_hook.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py` _+16 more__
- **2026-09-25** [`f88572a57c`](https://github.com/sgl-project/sglang/commit/f88572a57c) [#41216](https://github.com/sgl-project/sglang/pull/41216)
  [Test] Add in-process sgl-eval adapter and move validated GSM8K tests to it (#41216)
  _Files: `python/sglang/test/run_eval.py`, `python/sglang/test/sgl_eval_utils.py`, `test/README.md`, `test/manual/4-gpu-models/test_qwen35_models_archived.py` _+54 more__
- **2026-09-25** [`24b6930076`](https://github.com/sgl-project/sglang/commit/24b6930076) [#40986](https://github.com/sgl-project/sglang/pull/40986)
  [Sampling] Stream sampling masks as per-request arrays (#40986)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/managers/detokenizer_manager.py` _+14 more__
- **2026-09-25** [`7325b38412`](https://github.com/sgl-project/sglang/commit/7325b38412) [#40793](https://github.com/sgl-project/sglang/pull/40793)
  [PD] Honor gracefully_exit in disaggregation event loops and keep non-zero-rank launchers alive on SIGTERM (#40793)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py` _+1 more__
- **2026-09-25** [`8ca82118e0`](https://github.com/sgl-project/sglang/commit/8ca82118e0) [#40988](https://github.com/sgl-project/sglang/pull/40988)
  [mem_cache] Drop `is_insert` from `cache_finished_req`; release rows from `release_kv_cache` (#40988)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/chunk_cache.py`, `python/sglang/srt/mem_cache/common.py` _+17 more__
- **2026-09-24** [`7c5bdb940c`](https://github.com/sgl-project/sglang/commit/7c5bdb940c) [#41103](https://github.com/sgl-project/sglang/pull/41103)
  [PD] Add a `none` decode retraction backup and subclass seams in the PD queues (#41103)
  _Files: `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py` _+1 more__
- **2026-09-24** [`78b382b1ad`](https://github.com/sgl-project/sglang/commit/78b382b1ad) [#39478](https://github.com/sgl-project/sglang/pull/39478)
  Support unified memory decode host pools (#39478)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/cache_controller.py` _+20 more__
- **2026-09-24** [`cd11037009`](https://github.com/sgl-project/sglang/commit/cd11037009) [#41023](https://github.com/sgl-project/sglang/pull/41023)
  [PD] Enable deferred decode-side KV release by default (#41023)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py` _+2 more__
- **2026-09-24** [`efff836911`](https://github.com/sgl-project/sglang/commit/efff836911) [#40238](https://github.com/sgl-project/sglang/pull/40238)
  [PD] Add decode host receive for custom transfer backends (#40238)
  _Files: `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py` _+21 more__
- **2026-09-24** [`c3685dff42`](https://github.com/sgl-project/sglang/commit/c3685dff42) [#40932](https://github.com/sgl-project/sglang/pull/40932)
  [Sampling] Add selected/support sampling logprob modes (#40932)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py` _+22 more__
- **2026-09-23** [`79fec592a8`](https://github.com/sgl-project/sglang/commit/79fec592a8) [#40638](https://github.com/sgl-project/sglang/pull/40638)
  [Refactor] Read parallel placement in consumers (#40638)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/encoder/preprocessor.py`, `python/sglang/srt/disaggregation/encoder/server.py` _+39 more__
- **2026-09-23** [`954458567e`](https://github.com/sgl-project/sglang/commit/954458567e) [#40807](https://github.com/sgl-project/sglang/pull/40807)
  [mem_cache] Remove unreachable RadixCache paths in KV canary and HiCache accessors (#40807)
  _Files: `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/kv_canary/pool_patcher/buffer_alloc.py`, `python/sglang/srt/kv_canary/radix_cache_walker.py`, `python/sglang/srt/kv_canary/runner/swa_divergence.py` _+11 more__
- **2026-09-23** [`58f622ebc4`](https://github.com/sgl-project/sglang/commit/58f622ebc4) [#38978](https://github.com/sgl-project/sglang/pull/38978)
  Reduce decode bootstrap latency with request-owned speculative KV (#38978)
  _Files: `python/sglang/srt/arg_groups/serving_hook.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+5 more__
- **2026-09-23** [`9d267655e3`](https://github.com/sgl-project/sglang/commit/9d267655e3) [#40792](https://github.com/sgl-project/sglang/pull/40792)
  Fix NIXL transfer of MXFP8 KV block scales (#40792)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-09-22** [`d34f7b2326`](https://github.com/sgl-project/sglang/commit/d34f7b2326) [#40780](https://github.com/sgl-project/sglang/pull/40780)
  [mem_cache] Clean up SWA/Mamba radix cache leftovers and drop SGLANG_ENABLE_UNIFIED_RADIX_TREE (#40780)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/docs/advanced_features/session_radix_cache.mdx`, `docs/docs/references/environment_variables.mdx`, `docs/src/snippets/configs/thinkingmachines/inkling-small.jsx` _+33 more__
- **2026-09-22** [`91c329cc86`](https://github.com/sgl-project/sglang/commit/91c329cc86) [#40707](https://github.com/sgl-project/sglang/pull/40707)
  Take the model config out of the parallel group build, and finish retiring the parallel getters (#40707)
  _Files: `benchmark/kernels/all_reduce/benchmark_mscclpp.py`, `benchmark/kernels/all_reduce/benchmark_torch_symm_mem.py`, `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/disaggregation/encoder/server.py` _+13 more__
- **2026-09-22** [`6fd98c98b9`](https://github.com/sgl-project/sglang/commit/6fd98c98b9) [#40501](https://github.com/sgl-project/sglang/pull/40501)
  [Qwen3.8-Next] Pipeline-parallel serving and PD-prefill MTP for Qwen4-Exp (#40501)
  _Files: `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/models/qwen4_exp.py` _+4 more__
- **2026-09-22** [`bc3a63ebdb`](https://github.com/sgl-project/sglang/commit/bc3a63ebdb) [#40309](https://github.com/sgl-project/sglang/pull/40309)
  [Fix] Missing SWA eviction during decode preallocation (#40309)
  _Files: `python/sglang/srt/disaggregation/decode.py`_
- **2026-09-22** [`861b11f087`](https://github.com/sgl-project/sglang/commit/861b11f087) [#40711](https://github.com/sgl-project/sglang/pull/40711)
  [PD] Simplify late-abort quiescent ack branch to else (#40711)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`_
- **2026-09-22** [`8ef6d31cb9`](https://github.com/sgl-project/sglang/commit/8ef6d31cb9) [#40645](https://github.com/sgl-project/sglang/pull/40645)
  [PD] Preserve abort ACKs until in-flight KV transfers drain (#40645)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-09-22** [`70a2bb2a30`](https://github.com/sgl-project/sglang/commit/70a2bb2a30) [#40641](https://github.com/sgl-project/sglang/pull/40641)
  [AMD][DI] Keep loopback in UCX_NET_DEVICES (#40641)
  _Files: `python/sglang/test/server_fixtures/disaggregation_fixture.py`_
- **2026-09-22** [`771c9d782d`](https://github.com/sgl-project/sglang/commit/771c9d782d) [#39973](https://github.com/sgl-project/sglang/pull/39973)
  [PD] Validate Mooncake EFA allocator compatibility (#39973)
  _Files: `docs/docs/advanced_features/pd_disaggregation.mdx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mooncake/utils.py` _+1 more__
- **2026-09-22** [`04c0913434`](https://github.com/sgl-project/sglang/commit/04c0913434) [#31446](https://github.com/sgl-project/sglang/pull/31446)
  [HiSparse] Add MHA hisparse support for MiniMax M3 (#31446)
  _Files: `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs/docs/advanced_features/hisparse_guide.mdx`, `python/sglang/kernels/jit/csrc/kvcacheio/hisparse.cuh`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` _+23 more__
- **2026-09-22** [`018b73c7a0`](https://github.com/sgl-project/sglang/commit/018b73c7a0) [#40500](https://github.com/sgl-project/sglang/pull/40500)
  [PD] Pack draft KV head slices for DCP transfers (#40500)
  _Files: `python/sglang/kernels/ops/kvcache/pd_dcp_gather.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/dcp_pack.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+2 more__
- **2026-09-22** [`046cd6f4ea`](https://github.com/sgl-project/sglang/commit/046cd6f4ea) [#40540](https://github.com/sgl-project/sglang/pull/40540)
  [XPU][ci]: disable XPU NIXL disaggregation test (#40540)
  _Files: `.github/workflows/pr-test-xpu.yml`, `test/registered/disaggregation/test_disaggregation_xpu.py`_
- **2026-09-21** [`506698761d`](https://github.com/sgl-project/sglang/commit/506698761d) [#37507](https://github.com/sgl-project/sglang/pull/37507)
  [unified-memory] Hierarchical cache for every unified pool shape (#37507)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py` _+22 more__
- **2026-09-21** [`acac4dd9d9`](https://github.com/sgl-project/sglang/commit/acac4dd9d9) [#40632](https://github.com/sgl-project/sglang/pull/40632)
  [Refactor] Clean up parallel runtime comments (#40632)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/test/unit/test_component_accuracy_parallel_runtime.py`, `python/sglang/srt/arg_groups/arg_utils.py` _+59 more__
- **2026-09-21** [`bccf691b22`](https://github.com/sgl-project/sglang/commit/bccf691b22) [#40345](https://github.com/sgl-project/sglang/pull/40345)
  Bringing the parallel runtime up becomes a phase, not a side effect (#40345)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/managers/scheduler.py` _+5 more__
- **2026-09-21** [`970e946e4f`](https://github.com/sgl-project/sglang/commit/970e946e4f) [#40343](https://github.com/sgl-project/sglang/pull/40343)
  Retire the per-runner parallel record (#40343)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/fields/device.py`, `python/sglang/srt/disaggregation/decode.py` _+75 more__
- **2026-09-21** [`73f071db52`](https://github.com/sgl-project/sglang/commit/73f071db52) [#40342](https://github.com/sgl-project/sglang/pull/40342)
  Deprecate the parallel getters the context answers, and ratchet them shut (#40342)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/test/unit/test_component_accuracy_parallel_runtime.py`, `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/fields/parallel.py` _+40 more__
- **2026-09-21** [`2d0e94e3a3`](https://github.com/sgl-project/sglang/commit/2d0e94e3a3) [#40340](https://github.com/sgl-project/sglang/pull/40340)
  Check the topology identities where the layout is written, and build at the published widths (#40340)
  _Files: `benchmark/hf3fs/bench_zerocopy.py`, `benchmark/kernels/all_reduce/benchmark_all_reduce.py`, `benchmark/kernels/all_reduce/benchmark_fused_ar_rms_amd.py`, `benchmark/kernels/all_reduce/benchmark_fused_ar_rms_quant_amd.py` _+39 more__
- **2026-09-21** [`0db1a93adb`](https://github.com/sgl-project/sglang/commit/0db1a93adb) [#40339](https://github.com/sgl-project/sglang/pull/40339)
  State the draft's whole topology in its scope, and read the rest from the context (#40339)
  _Files: `python/sglang/srt/disaggregation/kv_events.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/kv_events_publisher.py` _+18 more__
- **2026-09-21** [`f0940fe3a6`](https://github.com/sgl-project/sglang/commit/f0940fe3a6) [#40610](https://github.com/sgl-project/sglang/pull/40610)
  Update DeepSeek-V4 Pro for B200 FP4 agentic PD disaggregation (#40610)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-21** [`b54d5b7c7b`](https://github.com/sgl-project/sglang/commit/b54d5b7c7b) [#28652](https://github.com/sgl-project/sglang/pull/28652)
  disaggregation: Fix FakeKVSender queue accumulation (#28652)
  _Files: `python/sglang/srt/disaggregation/fake/conn.py`, `test/registered/unit/disaggregation/test_fake_kv_sender.py`_
- **2026-09-21** [`501b7851e4`](https://github.com/sgl-project/sglang/commit/501b7851e4) [#39206](https://github.com/sgl-project/sglang/pull/39206)
  [diffusion] CI: guard E2E/loading latency with runner-aware baselines (#39206)
  _Files: `.github/actions/check-pr-test-health/action.test.cjs`, `.github/actions/check-pr-test-health/action.yml`, `.github/workflows/lint.yml`, `.github/workflows/pr-test-multimodal-gen.yml` _+32 more__
- **2026-09-21** [`76a9065bef`](https://github.com/sgl-project/sglang/commit/76a9065bef) [#40502](https://github.com/sgl-project/sglang/pull/40502)
  [Fix] Raise on undelivered embeddings in `send_with_url`, fix broken tests (#40502)
  _Files: `python/sglang/srt/disaggregation/encoder/server.py`, `test/registered/disaggregation/test_epd_disaggregation.py`, `test/registered/observability/test_encoder_server_metrics.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4_moe_dispatch.py`_

## Other  (37 commits)

- **2026-09-28** [`2f88c65289`](https://github.com/sgl-project/sglang/commit/2f88c65289) [#40688](https://github.com/sgl-project/sglang/pull/40688)
  [Router] Serve the cache-aware tree at /internal/kv_snapshot (2/13) (#40688)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/src/main.rs`, `experimental/sgl-router/src/server/app.rs` _+8 more__
- **2026-09-28** [`df378bca42`](https://github.com/sgl-project/sglang/commit/df378bca42) [#40687](https://github.com/sgl-project/sglang/pull/40687)
  [Router] Give the cache-aware tree a snapshot surface (1/13) (#40687)
  _Files: `experimental/sgl-router/src/state/kv_events/tree.rs`, `experimental/sgl-router/src/state/kv_events/tree/snapshot.rs`_
- **2026-09-27** [`583fada954`](https://github.com/sgl-project/sglang/commit/583fada954) [#40477](https://github.com/sgl-project/sglang/pull/40477)
  Port chat_parsing core (#40477)
  _Files: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml` _+6 more__
- **2026-09-27** [`d10a09ecf3`](https://github.com/sgl-project/sglang/commit/d10a09ecf3) [#40930](https://github.com/sgl-project/sglang/pull/40930)
  Add MiniMax arch fallback to auto parser resolution (#40930)
  _Files: `python/sglang/srt/parser/template_detection.py`, `test/registered/unit/parser/test_template_manager.py`_
- **2026-09-27** [`1ba84a4b59`](https://github.com/sgl-project/sglang/commit/1ba84a4b59) [#39889](https://github.com/sgl-project/sglang/pull/39889)
  [bench] Take each request's prompt length from the server (#39889)
  _Files: `python/sglang/benchmark/serving.py`, `test/registered/unit/bench/test_bench_serving_prompt_len.py`_
- **2026-09-26** [`710a41ba57`](https://github.com/sgl-project/sglang/commit/710a41ba57) [#41342](https://github.com/sgl-project/sglang/pull/41342)
  [sgl-router] Book the input_ids forwarding outcome only for built bodies (#41342)
  _Files: `experimental/sgl-router/src/server/routes/chat/preparation.rs`_
- **2026-09-26** [`c081d4aacc`](https://github.com/sgl-project/sglang/commit/c081d4aacc) [#41253](https://github.com/sgl-project/sglang/pull/41253)
  [Refactor] Drive an FFN exit's flags and its completion from one selection (#41253)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_mhc.py`, `test/registered/unit/layers/test_communicator_ffn_exit.py`, `test/registered/unit/layers/test_layer_communicator_fusion_gate.py` _+1 more__
- **2026-09-26** [`7152aabdcb`](https://github.com/sgl-project/sglang/commit/7152aabdcb) [#41185](https://github.com/sgl-project/sglang/pull/41185)
  [sgl-router] Track input_ids forwarding outcomes per chat request (#41185)
  _Files: `experimental/sgl-router/monitoring/grafana-dashboard.json`, `experimental/sgl-router/src/server/metrics.rs`, `experimental/sgl-router/src/server/routes/chat/preparation.rs`, `experimental/sgl-router/tests/proxy/roundrobin_input_ids.rs`_
- **2026-09-25** [`ac62ddf164`](https://github.com/sgl-project/sglang/commit/ac62ddf164) [#41246](https://github.com/sgl-project/sglang/pull/41246)
  [Rust frontend] Decode input_ids without untagged buffering (#41246)
  _Files: `rust/sglang-server/src/message/request.rs`_
- **2026-09-25** [`67bb6a58d0`](https://github.com/sgl-project/sglang/commit/67bb6a58d0) [#41132](https://github.com/sgl-project/sglang/pull/41132)
  Revert "[NPU] Fuse FIA KV-cache K/V writes into one npu_scatter_pa_kv_cache call" (#41132)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-09-25** [`8f5a636f8d`](https://github.com/sgl-project/sglang/commit/8f5a636f8d) [#41191](https://github.com/sgl-project/sglang/pull/41191)
  [Refactor] Build prepare_mlp and the layout moves from named steps (#41191)
  _Files: `python/sglang/srt/layers/communicator.py`, `test/registered/unit/layers/test_prepare_attn_steps.py`_
- **2026-09-24** [`752801e4d1`](https://github.com/sgl-project/sglang/commit/752801e4d1) [#28960](https://github.com/sgl-project/sglang/pull/28960)
  fix(sampling): validate sampling_seed is an int within int64 range (#28960)
  _Files: `python/sglang/srt/sampling/sampling_params.py`, `test/registered/unit/sampling/test_sampling_params.py`_
- **2026-09-24** [`41812afe43`](https://github.com/sgl-project/sglang/commit/41812afe43) [#40510](https://github.com/sgl-project/sglang/pull/40510)
  [NPU] Fix DSV4 hard-coding kv dtype (#40510)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_memory_pool.py`_
- **2026-09-24** [`d65503fece`](https://github.com/sgl-project/sglang/commit/d65503fece) [#40905](https://github.com/sgl-project/sglang/pull/40905)
  [NPU] Remove the LLaDA2.0-mini basic-function test case (#40905)
  _Files: `test/registered/npu/basic_function/dllm/test_npu_llada2_mini.py`_
- **2026-09-24** [`90663ccb41`](https://github.com/sgl-project/sglang/commit/90663ccb41) [#40337](https://github.com/sgl-project/sglang/pull/40337)
  [DSV4] fix: size the C4 state ring by the page it is addressed by (#40337)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-09-23** [`542a043f1b`](https://github.com/sgl-project/sglang/commit/542a043f1b) [#37284](https://github.com/sgl-project/sglang/pull/37284)
  [RL] Release the weight-checker snapshot once compare passes (#37284)
  _Files: `python/sglang/srt/utils/weight_checker.py`, `test/registered/unit/utils/test_weight_checker.py`_
- **2026-09-23** [`0010f56a0d`](https://github.com/sgl-project/sglang/commit/0010f56a0d) [#40976](https://github.com/sgl-project/sglang/pull/40976)
  [Test] Remove obsolete configuration migration guards (#40976)
  _Files: `test/registered/unit/server_args/test_resolution_declarations.py`, `test/registered/unit/test_global_config_read_ratchet.py`, `test/registered/unit/test_runtime_context.py`, `test/registered/unit/test_server_args_namespaces.py`_
- **2026-09-23** [`7dd9640752`](https://github.com/sgl-project/sglang/commit/7dd9640752) [#40869](https://github.com/sgl-project/sglang/pull/40869)
  [Refactor] Compare token layouts instead of group sizes when selecting communicator paths (#40869)
  _Files: `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `test/registered/unit/layers/test_communicator_layout.py`_
- **2026-09-23** [`f2eebd5533`](https://github.com/sgl-project/sglang/commit/f2eebd5533) [#40700](https://github.com/sgl-project/sglang/pull/40700)
  [RL] Fix Kimi K3 expert-count lookup for routed-expert capture (#40700)
  _Files: `python/sglang/srt/configs/kimi_linear.py`_
- **2026-09-23** [`3fdd63a562`](https://github.com/sgl-project/sglang/commit/3fdd63a562) [#40445](https://github.com/sgl-project/sglang/pull/40445)
  [NPU] Fuse FIA KV-cache K/V writes into one npu_scatter_pa_kv_cache call (#40445)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-09-23** [`ced0a2c98c`](https://github.com/sgl-project/sglang/commit/ced0a2c98c) [#40743](https://github.com/sgl-project/sglang/pull/40743)
  [Hisparse] fix: account for MiniMax HiSparse full-pool memory (#40743)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`_
- **2026-09-22** [`db73f35f4a`](https://github.com/sgl-project/sglang/commit/db73f35f4a) [#40725](https://github.com/sgl-project/sglang/pull/40725)
  Fix the Inkling per-expert sync test and collect it in the weekly CPU run (#40725)
  _Files: `test/registered/unit/models/test_inkling_per_expert_sync.py`_
- **2026-09-22** [`1815e490de`](https://github.com/sgl-project/sglang/commit/1815e490de) [#39312](https://github.com/sgl-project/sglang/pull/39312)
  [observability] Fix negative queue_time for retracted requests (#39312)
  _Files: `python/sglang/srt/observability/req_time_stats.py`, `test/registered/unit/observability/test_req_time_stats.py`_
- **2026-09-22** [`2032f3a071`](https://github.com/sgl-project/sglang/commit/2032f3a071) [#39461](https://github.com/sgl-project/sglang/pull/39461)
  [Router] Abort the engine when a client disconnects mid-request (#39461)
  _Files: `experimental/sgl-router/src/proxy/abort.rs`, `experimental/sgl-router/src/proxy/mod.rs`, `experimental/sgl-router/src/server/app.rs`, `experimental/sgl-router/src/server/metrics.rs` _+11 more__
- **2026-09-22** [`877a293d6d`](https://github.com/sgl-project/sglang/commit/877a293d6d) [#40659](https://github.com/sgl-project/sglang/pull/40659)
  [Benchmark] Optionally clear HiCache storage between cases (#40659)
  _Files: `python/sglang/benchmark/one_batch_server.py`_
- **2026-09-22** [`59a723ef1e`](https://github.com/sgl-project/sglang/commit/59a723ef1e) [#40292](https://github.com/sgl-project/sglang/pull/40292)
  [sgl-router] refactor - SLO ordering for bucket selection (#40292)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/src/buckets_reorg.rs`, `experimental/sgl-router/src/server/routes/chat/reorg.rs`, `experimental/sgl-router/tests/component/main.rs` _+4 more__
- **2026-09-22** [`27f796ca6c`](https://github.com/sgl-project/sglang/commit/27f796ca6c) [#40604](https://github.com/sgl-project/sglang/pull/40604)
  [sgl-router] Fix readiness, IPv6 discovery, logging, and model validation (#40604)
  _Files: `experimental/sgl-router/src/discovery/k8s.rs`, `experimental/sgl-router/src/main.rs`, `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/src/server/routes/health.rs` _+1 more__
- **2026-09-22** [`9eda772a21`](https://github.com/sgl-project/sglang/commit/9eda772a21) [#40661](https://github.com/sgl-project/sglang/pull/40661)
  [Test] Handle tied top-k indices in graph-pool logprob regression (#40661)
  _Files: `test/registered/unit/model_executor/runner_utils/test_graph_pool_borrow.py`_
- **2026-09-21** [`22587fb15c`](https://github.com/sgl-project/sglang/commit/22587fb15c) [#40642](https://github.com/sgl-project/sglang/pull/40642)
  [Fix] Run KV canary hooks for context-parallel prefill (#40642)
  _Files: `python/sglang/srt/kv_canary/api.py`, `test/registered/mock_model/test_e2e_cp.py`_
- **2026-09-21** [`d47b8c454c`](https://github.com/sgl-project/sglang/commit/d47b8c454c) [#40603](https://github.com/sgl-project/sglang/pull/40603)
  [sgl-router] Release cancelled circuit-breaker probes (#40603)
  _Files: `experimental/sgl-router/src/health/circuit_breaker.rs`, `experimental/sgl-router/src/proxy/mod.rs`_
- **2026-09-21** [`d5fdab7022`](https://github.com/sgl-project/sglang/commit/d5fdab7022) [#40602](https://github.com/sgl-project/sglang/pull/40602)
  chore: add NIXL owners and CI access (#40602)
  _Files: `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS`_
- **2026-09-21** [`008470abd8`](https://github.com/sgl-project/sglang/commit/008470abd8) [#40391](https://github.com/sgl-project/sglang/pull/40391)
  [sgl-router] Bound streaming lifetimes and release guards on idle disconnect (#40391)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/main.rs` _+7 more__
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

## KV Cache / Memory  (29 commits)

- **2026-09-27** [`e581520c67`](https://github.com/sgl-project/sglang/commit/e581520c67) [#39726](https://github.com/sgl-project/sglang/pull/39726)
  [HiCache] Add the page-unified KV load-back JIT kernel  (#39726)
  _Files: `python/sglang/kernels/jit/csrc/kvcacheio/hicache.cuh`, `python/sglang/kernels/ops/kvcache/hicache.py`, `test/registered/kernels/ops/kvcache/test_hicache.py`_
- **2026-09-27** [`37556c1b91`](https://github.com/sgl-project/sglang/commit/37556c1b91) [#41281](https://github.com/sgl-project/sglang/pull/41281)
  [mem_cache] Replace `cache_finished_req` with `insert_req`; `release_kv_cache` frees and unpins (#41281)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/chunk_cache.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+20 more__
- **2026-09-27** [`38d865489a`](https://github.com/sgl-project/sglang/commit/38d865489a) [#41345](https://github.com/sgl-project/sglang/pull/41345)
  [DSV4.1][HiCache] fix: wait for the layer transfer before reading low-ratio index-K (#41345)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `test/registered/unit/mem_cache/test_dsv4_compressed_pools.py`_
- **2026-09-26** [`fc9e1c8d29`](https://github.com/sgl-project/sglang/commit/fc9e1c8d29) [#41328](https://github.com/sgl-project/sglang/pull/41328)
  [MemCache] Fix LMCache component cursors and per-cache backend selection (#41328)
  _Files: `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/storage/lmcache/lmcache_unified_radix_cache.py`, `python/sglang/srt/mem_cache/unified_cache/component_type.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+3 more__
- **2026-09-26** [`c10fa03fc4`](https://github.com/sgl-project/sglang/commit/c10fa03fc4) [#41325](https://github.com/sgl-project/sglang/pull/41325)
  Make sliding-window caching and speculative batch padding extensible (#41325)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/registry.py` _+13 more__
- **2026-09-25** [`671000aee6`](https://github.com/sgl-project/sglang/commit/671000aee6) [#41248](https://github.com/sgl-project/sglang/pull/41248)
  [unified-memory] Honor move gates in float relocation and size auto HiCache from host capacity (#41248)
  _Files: `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py`, `python/sglang/srt/mem_cache/hicache_auto_size.py`, `test/registered/unit/mem_cache/test_hicache_auto_size.py`, `test/registered/unit/mem_cache/test_multi_ended_allocator.py` _+1 more__
- **2026-09-25** [`434c2e3adc`](https://github.com/sgl-project/sglang/commit/434c2e3adc) [#41092](https://github.com/sgl-project/sglang/pull/41092)
  [HiCache] fix: Drain pending backups before internal Mamba write-back (#41092)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-25** [`cbe137727e`](https://github.com/sgl-project/sglang/commit/cbe137727e) [#40456](https://github.com/sgl-project/sglang/pull/40456)
  [HiCache] Give trailing sidecar storage transfers a contiguous prefix_keys chain (#40456)
  _Files: `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`_
- **2026-09-25** [`ec070ec8c8`](https://github.com/sgl-project/sglang/commit/ec070ec8c8) [#41159](https://github.com/sgl-project/sglang/pull/41159)
  [AMD] Fix int32 offset overflow in Triton DSv4 KV store kernels (#41159)
  _Files: `python/sglang/kernels/ops/kvcache/triton_store_cache.py`_
- **2026-09-25** [`16d1c93b3d`](https://github.com/sgl-project/sglang/commit/16d1c93b3d) [#41208](https://github.com/sgl-project/sglang/pull/41208)
  [feat] add a system one compatible /v1/systemone route (#41208)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/docs.json`, `docs/docs/basic_usage/native_api.mdx` _+15 more__
- **2026-09-24** [`466e985f4b`](https://github.com/sgl-project/sglang/commit/466e985f4b) [#40960](https://github.com/sgl-project/sglang/pull/40960)
  [HiCache] Batch buffer-only KV backups within each flush (#40960)
  _Files: `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `test/registered/unit/mem_cache/test_buffer_mode_sidecar.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-24** [`3ec86307f2`](https://github.com/sgl-project/sglang/commit/3ec86307f2) [#41179](https://github.com/sgl-project/sglang/pull/41179)
  Fix mixed chunk prefill with DP speculative coordination (#41179)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/spec/eagle/test_dp_spec_prefill_coordination_mixed.py`, `test/registered/unit/spec/test_dp_spec_prefill_coordination.py`_
- **2026-09-24** [`1b03d31b31`](https://github.com/sgl-project/sglang/commit/1b03d31b31) [#41155](https://github.com/sgl-project/sglang/pull/41155)
  [Test] Run the Qwen3.5 Triton DCP nightly with the radix cache enabled (#41155)
  _Files: `test/registered/dcp/test_qwen3p5_triton_dcp.py`_
- **2026-09-24** [`77173ffb08`](https://github.com/sgl-project/sglang/commit/77173ffb08) [#40712](https://github.com/sgl-project/sglang/pull/40712)
  [HiCache] Demote SWA KV to host on write_back eviction instead of dropping it (#40712)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/swa.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-24** [`28ec6700da`](https://github.com/sgl-project/sglang/commit/28ec6700da) [#40512](https://github.com/sgl-project/sglang/pull/40512)
  [HiCache] Make host reclamation independent of transfer order (#40512)
  _Files: `python/sglang/srt/mem_cache/pool_host/group.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py`_
- **2026-09-24** [`cae4927fbf`](https://github.com/sgl-project/sglang/commit/cae4927fbf) [#41048](https://github.com/sgl-project/sglang/pull/41048)
  [DSV4] Budget the ratio-2 pair state pool in DSV4PoolConfigurator (#41048)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/mem_cache/test_dsv4_compress_write_pad.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-09-24** [`cc6e8b0f25`](https://github.com/sgl-project/sglang/commit/cc6e8b0f25) [#40983](https://github.com/sgl-project/sglang/pull/40983)
  [Fix] Derive per-runner hybrid SWA layer ids on ModelLayerInfo instead of mutating ModelConfig (#40983)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/layer_setup.py` _+4 more__
- **2026-09-24** [`621136e094`](https://github.com/sgl-project/sglang/commit/621136e094) [#40963](https://github.com/sgl-project/sglang/pull/40963)
  [mem_cache] Remove unused helpers in mem_cache, storage backends, and metrics (#40963)
  _Files: `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hisparse_memory_pool.py` _+12 more__
- **2026-09-23** [`c39a1c0663`](https://github.com/sgl-project/sglang/commit/c39a1c0663) [#40798](https://github.com/sgl-project/sglang/pull/40798)
  [mem_cache] Free the rows below the SWA evict floor on all-SWA request release (#40798)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/chunk_cache.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/pure_swa_radix_cache.py` _+5 more__
- **2026-09-23** [`66ce8c55cc`](https://github.com/sgl-project/sglang/commit/66ce8c55cc) [#40831](https://github.com/sgl-project/sglang/pull/40831)
  [HiCache] ci: add HiCache and unified radix rerun group (#40831)
  _Files: `scripts/ci/rerun_test_groups.json`_
- **2026-09-22** [`4ce23542bf`](https://github.com/sgl-project/sglang/commit/4ce23542bf) [#40787](https://github.com/sgl-project/sglang/pull/40787)
  [HiCache] Remove the unused HiRadixCache (#40787)
  _Files: `.github/labeler.yml`, `docs/docs/advanced_features/hicache_storage_runtime_attach_detach.mdx`, `python/sglang/srt/distributed/communication_tags.py`, `python/sglang/srt/managers/cache_controller.py` _+15 more__
- **2026-09-22** [`b77833c504`](https://github.com/sgl-project/sglang/commit/b77833c504) [#40357](https://github.com/sgl-project/sglang/pull/40357)
  [MM] Keep scheduler padding in packed token arrays (#40357)
  _Files: `benchmark/io/bench_mm_token_padding.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/rust_tree_core/adapter.py` _+60 more__
- **2026-09-22** [`9a53f75124`](https://github.com/sgl-project/sglang/commit/9a53f75124) [#40775](https://github.com/sgl-project/sglang/pull/40775)
  [mem_cache] Remove the experimental C++ radix tree (#40775)
  _Files: `.github/labeler.yml`, `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/cpp_radix_tree/.clang-format` _+12 more__
- **2026-09-22** [`6f4c2b9b91`](https://github.com/sgl-project/sglang/commit/6f4c2b9b91) [#40680](https://github.com/sgl-project/sglang/pull/40680)
  [HiCache] Demote internal-node mamba states on write_back eviction (#40680)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/mamba.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-22** [`ddebc52f23`](https://github.com/sgl-project/sglang/commit/ddebc52f23) [#38468](https://github.com/sgl-project/sglang/pull/38468)
  [kv-shard 3/4] Enable Control plane (#38468)
  _Files: `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/mem_cache/page_interleave.py`, `python/sglang/srt/mem_cache/page_interleave_pool.py`, `test/registered/unit/managers/scheduler_components/test_invariant_checker.py` _+2 more__
- **2026-09-22** [`3f00fb7e2e`](https://github.com/sgl-project/sglang/commit/3f00fb7e2e) [#40123](https://github.com/sgl-project/sglang/pull/40123)
  [AMD] Register unified KV page-zeroing test in PR CI (#40123)
  _Files: `test/registered/unit/mem_cache/test_unified_handout_zeroing.py`_
- **2026-09-22** [`15eba3b464`](https://github.com/sgl-project/sglang/commit/15eba3b464) [#27265](https://github.com/sgl-project/sglang/pull/27265)
  Feat: Add TensorCast storage as a new HiCache backend (#27265)
  _Files: `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/pool_host/common.py`, `python/sglang/srt/mem_cache/storage/backend_factory.py` _+7 more__
- **2026-09-21** [`44bdf225d8`](https://github.com/sgl-project/sglang/commit/44bdf225d8) [#40618](https://github.com/sgl-project/sglang/pull/40618)
  Fix lint failure from MXFP8 reserved-slot test location (#40618)
  _Files: `test/registered/kernels/ops/kvcache/test_mxfp8_kv_reserved_slot.py`_
- **2026-09-21** [`5a6a1bb883`](https://github.com/sgl-project/sglang/commit/5a6a1bb883) [#35351](https://github.com/sgl-project/sglang/pull/35351)
  [mxfp8-kv] Skip writes to the reserved CUDA-graph padding slot (#35351)
  _Files: `python/sglang/kernels/ops/quantization/mxfp8_interleave_sf.py`, `python/sglang/kernels/ops/quantization/mxfp8_quant.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/kernel/quantization/test_mxfp8_kv_reserved_slot.py`_

## Quantization  (16 commits)

- **2026-09-25** [`27e883a20d`](https://github.com/sgl-project/sglang/commit/27e883a20d) [#41018](https://github.com/sgl-project/sglang/pull/41018)
  dsv4.1-amd: gfx950 MXFP8 matmul kernels and fp8-grid producers (#41018)
  _Files: `benchmark/kernels/quantization/tuning_mxfp8_native_gfx95.py`, `python/sglang/kernels/jit/csrc/deepseek_v4/mxfp8_gemv_gfx95.cuh`, `python/sglang/kernels/ops/activation/silu_and_mul_clamp_hip.py`, `python/sglang/kernels/ops/gemm/gfx95_batched_gemm_bf16_fp8_grid.py` _+6 more__
- **2026-09-25** [`0154f72b48`](https://github.com/sgl-project/sglang/commit/0154f72b48) [#39064](https://github.com/sgl-project/sglang/pull/39064)
  [ROCm][Bugfix] Keep quantization for mixed Quark Qwen3.5 MTP checkpoints (#39064)
  _Files: `python/sglang/srt/models/qwen3_5_mtp.py`, `test/registered/unit/models/test_qwen3_5_mtp_quant_config.py`_
- **2026-09-24** [`961404b010`](https://github.com/sgl-project/sglang/commit/961404b010) [#41090](https://github.com/sgl-project/sglang/pull/41090)
  [DSV4] Fix TRTLLM uniform FP8 KV memory budgeting (#41090)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-09-24** [`5bb850d536`](https://github.com/sgl-project/sglang/commit/5bb850d536) [#41084](https://github.com/sgl-project/sglang/pull/41084)
  [Refactor] Split prepare_attn into a reduction step and per-quant-format residual steps (#41084)
  _Files: `python/sglang/srt/layers/communicator.py`, `test/registered/unit/layers/test_prepare_attn_steps.py`_
- **2026-09-24** [`6a14b80141`](https://github.com/sgl-project/sglang/commit/6a14b80141) [#41109](https://github.com/sgl-project/sglang/pull/41109)
  [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260923 daily (#41109)
  _Files: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-09-24** [`a69583f70f`](https://github.com/sgl-project/sglang/commit/a69583f70f) [#40996](https://github.com/sgl-project/sglang/pull/40996)
  [AMD] Add tuned dsv4 shape (#40996)
  _Files: `python/sglang/kernels/ops/quantization/configs/N=1024,K=4096,device_name=AMD_Instinct_MI455X,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/kernels/ops/quantization/configs/N=2048,K=4096,device_name=AMD_Instinct_MI455X,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/kernels/ops/quantization/configs/N=32768,K=1024,device_name=AMD_Instinct_MI455X,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/kernels/ops/quantization/configs/N=4096,K=2048,device_name=AMD_Instinct_MI455X,dtype=fp8_w8a8,block_shape=[128, 128].json` _+4 more__
- **2026-09-24** [`e2f4fedf04`](https://github.com/sgl-project/sglang/commit/e2f4fedf04) [#40754](https://github.com/sgl-project/sglang/pull/40754)
  [AMD] Critical fix enabling Qwen3.8 FP8: restore dropped fused shared-expert weights (#40754)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-09-23** [`c3e985203a`](https://github.com/sgl-project/sglang/commit/c3e985203a) [#40924](https://github.com/sgl-project/sglang/pull/40924)
  [Diffusion] Remove unused standalone benchmarks and deduplicate kernel tests (#40924)
  _Files: `test/registered/kernels/benchmark/diffusion/bench_diffusion_nvfp4_scaled_mm.py`, `test/registered/kernels/benchmark/diffusion/bench_fused_norm_scale_shift.py`, `test/registered/kernels/benchmark/diffusion/bench_ltx2_qknorm_split_rope.py`, `test/registered/kernels/benchmark/diffusion/bench_norm_impls.py` _+5 more__
- **2026-09-23** [`abef3efb64`](https://github.com/sgl-project/sglang/commit/abef3efb64) [#40378](https://github.com/sgl-project/sglang/pull/40378)
  [Diffusion] Fuse rounded SwiGLU for quantized MiniMax-H3 MLPs (#40378)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`_
- **2026-09-23** [`401d5aedf3`](https://github.com/sgl-project/sglang/commit/401d5aedf3) [#40879](https://github.com/sgl-project/sglang/pull/40879)
  [AMD] Drop the unreachable vLLM fallback from ROCm FP8 activation quant (#40879)
  _Files: `python/sglang/kernels/ops/quantization/fp8_kernel.py`_
- **2026-09-23** [`abca3b2e52`](https://github.com/sgl-project/sglang/commit/abca3b2e52) [#39781](https://github.com/sgl-project/sglang/pull/39781)
  [Intel GPU] Add DeepSeek-V2-Lite-Chat-FP8 gsm8k e2e accuracy nightly test on XPU (#39781)
  _Files: `test/registered/xpu/llm_models/test_xpu_deepseek_v2_lite_chat_fp8_gsm8k_eval.py`_
- **2026-09-22** [`cb8dab06be`](https://github.com/sgl-project/sglang/commit/cb8dab06be) [#40714](https://github.com/sgl-project/sglang/pull/40714)
  [NPU] [DOC] Remove duplicated features in npu docs (#40714)
  _Files: `docs/docs/hardware-platforms/ascend-npus/optimization/quantization.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`_
- **2026-09-22** [`debbb5cde9`](https://github.com/sgl-project/sglang/commit/debbb5cde9) [#40557](https://github.com/sgl-project/sglang/pull/40557)
  [AMD] Drop the redundant scale zero-fill before AITER per-tensor FP8 quant (#40557)
  _Files: `python/sglang/kernels/ops/quantization/fp8_kernel.py`_
- **2026-09-22** [`6412ad8c64`](https://github.com/sgl-project/sglang/commit/6412ad8c64) [#39902](https://github.com/sgl-project/sglang/pull/39902)
  [AMD] Pack Qwen3.5 GDN input projections on ROCm (#39902)
  _Files: `python/sglang/srt/model_executor/model_runner_components/weight_updater.py`, `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/test_qwen35_gdn_packed_fp8_in_proj.py`, `test/registered/amd/test_qwen35_gdn_packed_in_proj.py` _+1 more__
- **2026-09-22** [`9b59fc5db5`](https://github.com/sgl-project/sglang/commit/9b59fc5db5) [#40628](https://github.com/sgl-project/sglang/pull/40628)
  [ModelOpt][PP] Keep BF16 shared experts out of the NVFP4 fusion so TP1 pipeline stages can load (#40628)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4.py`_
- **2026-09-21** [`62ba964848`](https://github.com/sgl-project/sglang/commit/62ba964848) [#38779](https://github.com/sgl-project/sglang/pull/38779)
  Fix: post-load staging regression breaks offload meta/sharded_gpu modes (#38779)
  _Files: `python/sglang/srt/model_loader/post_load.py`, `test/registered/unit/test_quantization_post_load.py`_

## Scheduler / Batching  (14 commits)

- **2026-09-27** [`df1fc6ab64`](https://github.com/sgl-project/sglang/commit/df1fc6ab64) [#39964](https://github.com/sgl-project/sglang/pull/39964)
  [kv-shard 3/4] Enable Control Plane B (#39964)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `test/registered/unit/managers/test_dcp_logical_capacity.py` _+2 more__
- **2026-09-26** [`9cd6616c24`](https://github.com/sgl-project/sglang/commit/9cd6616c24) [#41256](https://github.com/sgl-project/sglang/pull/41256)
  [Refactor] Pick the two-batch-overlap split's layout moves once and remove execute (#41256)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/communicator.py`_
- **2026-09-26** [`3ed56a341b`](https://github.com/sgl-project/sglang/commit/3ed56a341b) [#41188](https://github.com/sgl-project/sglang/pull/41188)
  [Score API] Setwise scoring: CausalLM support (batched + --enable-mis) (#41188)
  _Files: `python/sglang/srt/entrypoints/engine_score_mixin.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/managers/io_struct.py` _+6 more__
- **2026-09-25** [`95047d3464`](https://github.com/sgl-project/sglang/commit/95047d3464) [#41287](https://github.com/sgl-project/sglang/pull/41287)
  [Fix] Fix cpu CI fail introduced by pr #38652 (#41287)
  _Files: `test/registered/unit/managers/test_scheduler_flush_cache_after_retract.py`_
- **2026-09-25** [`9dc4c5d891`](https://github.com/sgl-project/sglang/commit/9dc4c5d891) [#40907](https://github.com/sgl-project/sglang/pull/40907)
  [AMD] Restore non-DCP Mamba checkpoint donation to fix agent-mode cache hit at high conc with HiCache (#40907)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_mamba_checkpoint_depth.py`_
- **2026-09-24** [`bb1c98baa2`](https://github.com/sgl-project/sglang/commit/bb1c98baa2) [#41096](https://github.com/sgl-project/sglang/pull/41096)
  Fix TBO child batch missing dp_spec_prefill_coordination_applied (#41096)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`_
- **2026-09-24** [`174a5f37b9`](https://github.com/sgl-project/sglang/commit/174a5f37b9) [#40826](https://github.com/sgl-project/sglang/pull/40826)
  [feature] add per-item candidate token scoring and calibration (#40826)
  _Files: `examples/runtime/semantic_scoring/semif.py`, `python/sglang/srt/entrypoints/engine_score_mixin.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_score.py` _+5 more__
- **2026-09-24** [`03fcbe147f`](https://github.com/sgl-project/sglang/commit/03fcbe147f) [#39607](https://github.com/sgl-project/sglang/pull/39607)
  [NPU] Support batch invariant FIA graphs for deterministic inference (#39607)
  _Files: `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/hardware_backend/npu/batch_invariant_ops/npu_batch_invariant_ops.py`_
- **2026-09-23** [`6fe4b66f5c`](https://github.com/sgl-project/sglang/commit/6fe4b66f5c) [#40779](https://github.com/sgl-project/sglang/pull/40779)
  [RL] Keep pause_generation and weight updates from deadlocking each other (#40779)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/idle_sleeper.py`, `python/sglang/srt/managers/scheduler_components/weight_updater.py`, `test/registered/unit/managers/test_scheduler_flush_cache_after_retract.py`_
- **2026-09-23** [`890a9605ce`](https://github.com/sgl-project/sglang/commit/890a9605ce) [#40802](https://github.com/sgl-project/sglang/pull/40802)
  [Metrics] Log forward and forward+idle occupancy over total wall time (#40802)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`_
- **2026-09-23** [`7fef014d51`](https://github.com/sgl-project/sglang/commit/7fef014d51) [#38891](https://github.com/sgl-project/sglang/pull/38891)
  feat(kv-hints): add kv hint envelope to request transport (#38891)
  _Files: `proto/sglang/runtime/v1/sglang.proto`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/kv_hints.py` _+7 more__
- **2026-09-23** [`2bc435d32e`](https://github.com/sgl-project/sglang/commit/2bc435d32e) [#40312](https://github.com/sgl-project/sglang/pull/40312)
  [HiCache] fix: bound the controller reset join so a stalled storage thread cannot hang the scheduler (#40312)
  _Files: `python/sglang/srt/managers/cache_controller.py`_
- **2026-09-22** [`15ba54bd5d`](https://github.com/sgl-project/sglang/commit/15ba54bd5d) [#39486](https://github.com/sgl-project/sglang/pull/39486)
  perf(engine): avoid timed waits for Engine responses (#39486)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
- **2026-09-21** [`0229025127`](https://github.com/sgl-project/sglang/commit/0229025127) [#40499](https://github.com/sgl-project/sglang/pull/40499)
  [Spec][PP] Launch extend microbatches before the spec output exchange (#40499)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/registered/unit/managers/test_pp_cp_rank_offsets.py`_

## Triton / Kernels  (13 commits)

- **2026-09-28** [`0318a8d0af`](https://github.com/sgl-project/sglang/commit/0318a8d0af) [#41545](https://github.com/sgl-project/sglang/pull/41545)
  [Doc] Add kernel benchmark rule on L2 cache reuse (#41545)
  _Files: `.claude/rules/kernel-benchmark.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`_
- **2026-09-28** [`e8eeff2956`](https://github.com/sgl-project/sglang/commit/e8eeff2956) [#41220](https://github.com/sgl-project/sglang/pull/41220)
  [XPU] Bump sglang-kernel-xpu wheel to v0.3.0 (#41220)
  _Files: `python/pyproject_xpu.toml`_
- **2026-09-28** [`6cbdfec453`](https://github.com/sgl-project/sglang/commit/6cbdfec453) [#40814](https://github.com/sgl-project/sglang/pull/40814)
  [Fix][NPU] Fix performance degradation caused by serial execution of two-stage ACL op calls on graph (#40814)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py`_
- **2026-09-27** [`aa7a976807`](https://github.com/sgl-project/sglang/commit/aa7a976807) [#41166](https://github.com/sgl-project/sglang/pull/41166)
  [qwen 3.8 next] Fuse small CUDA graph input buffer copies (#41166)
  _Files: `python/sglang/kernels/ops/memory/small_copy.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/runner_utils/buffers.py`, `test/registered/kernels/ops/memory/test_small_copy.py`_
- **2026-09-26** [`a5c8afab48`](https://github.com/sgl-project/sglang/commit/a5c8afab48) [#41223](https://github.com/sgl-project/sglang/pull/41223)
  [Perf] Mamba2 selective_state_update up to 2x faster on B200 via 8x1 launch config for dstate 128 (+7.5% Nemotron-3-Super serving) (#41223)
  _Files: `python/sglang/kernels/ops/mamba/triton_ops/mamba_ssm.py`_
- **2026-09-26** [`38ec649048`](https://github.com/sgl-project/sglang/commit/38ec649048) [#41243](https://github.com/sgl-project/sglang/pull/41243)
  [Refactor] Restore logical kernel groups and test organization (#41243)
- **2026-09-24** [`b129504f0e`](https://github.com/sgl-project/sglang/commit/b129504f0e) [#40041](https://github.com/sgl-project/sglang/pull/40041)
  [qwen 3.8 next] Fuse Qwen PLE gate and convolution preparation for target verify (#40041)
  _Files: `python/sglang/kernels/ops/qwen4_ple.py`, `python/sglang/srt/models/qwen4_exp.py`_
- **2026-09-23** [`3f697899a3`](https://github.com/sgl-project/sglang/commit/3f697899a3) [#40819](https://github.com/sgl-project/sglang/pull/40819)
  ci: reinstall torch/triton left incomplete by a cancelled job (#40819)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-09-23** [`2909f84e3b`](https://github.com/sgl-project/sglang/commit/2909f84e3b) [#40767](https://github.com/sgl-project/sglang/pull/40767)
  [JIT] Add an occupancy-preserving L1 carveout preference (#40767)
  _Files: `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh`, `test/registered/kernels/ops/elementwise/launch_carveout.cuh`, `test/registered/kernels/ops/elementwise/test_launch_carveout.py`_
- **2026-09-23** [`4bb5611dba`](https://github.com/sgl-project/sglang/commit/4bb5611dba) [#40851](https://github.com/sgl-project/sglang/pull/40851)
  [Fix] Give the full prefill CUDA graph replay view the captured bucket's input_ids (#40851)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/unit/model_executor/runner/test_prefill_cuda_graph_padding.py`_
- **2026-09-22** [`5c18780c31`](https://github.com/sgl-project/sglang/commit/5c18780c31) [#40686](https://github.com/sgl-project/sglang/pull/40686)
  [Router] Keep e2e workers inside the job's CUDA_VISIBLE_DEVICES allotment (#40686)
  _Files: `experimental/sgl-router/tests/e2e/conftest.py`, `experimental/sgl-router/tests/e2e/infra/model_pool.py`, `experimental/sgl-router/tests/e2e/infra/test_model_pool.py`, `experimental/sgl-router/tests/e2e/test_gpu_allotment.py`_
- **2026-09-22** [`35eb7cf8d6`](https://github.com/sgl-project/sglang/commit/35eb7cf8d6) [#33520](https://github.com/sgl-project/sglang/pull/33520)
  [Intel][XPU][KVCanary] Enable KV Canary on Intel XPU (#33520)
  _Files: `python/sglang/kernels/ops/kv_canary/_dispatch.py`, `python/sglang/kernels/ops/kv_canary/plan/api.py`, `python/sglang/kernels/ops/kv_canary/verify.py`, `python/sglang/kernels/ops/kv_canary/verify_ref.py` _+25 more__
- **2026-09-22** [`c4d3770a68`](https://github.com/sgl-project/sglang/commit/c4d3770a68) [#40640](https://github.com/sgl-project/sglang/pull/40640)
  [Kimi K3] Fix CUDA graph stream explosion (#40640)
  _Files: `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/models/test_kimi_k3_bfa_overlap.py`_

## ROCm / AMD  (13 commits)

- **2026-09-28** [`34f090053e`](https://github.com/sgl-project/sglang/commit/34f090053e) [#41387](https://github.com/sgl-project/sglang/pull/41387)
  [AMD] [Docker] Remove unused LLVM 18 setup from ROCm TileLang build (#41387)
  _Files: `docker/rocm.Dockerfile`_
- **2026-09-26** [`c73f7077eb`](https://github.com/sgl-project/sglang/commit/c73f7077eb) [#41356](https://github.com/sgl-project/sglang/pull/41356)
  [AMD] Fix jit broken on rocm env (#41356)
  _Files: `python/sglang/kernels/jit/include/sgl_kernel/runtime.cuh`_
- **2026-09-24** [`8ec65e89c1`](https://github.com/sgl-project/sglang/commit/8ec65e89c1) [#40387](https://github.com/sgl-project/sglang/pull/40387)
  [AMD] ci: move the Miles ROCm 7.2 nightly build to 7.2.4 (#40387)
  _Files: `.github/workflows/release-docker-amd-miles-rocm724-nightly.yml`_
- **2026-09-24** [`43af9fcbb6`](https://github.com/sgl-project/sglang/commit/43af9fcbb6) [#41053](https://github.com/sgl-project/sglang/pull/41053)
  [AMD][DI][CI] Move MI355X disagg nightly to ROCm 10 (#41053)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-09-24** [`7a9feacf91`](https://github.com/sgl-project/sglang/commit/7a9feacf91) [#41024](https://github.com/sgl-project/sglang/pull/41024)
  [Docs] DeepSeek-V4 MI355X Pro Official PD pairs with DSpark and UMBP (#41024)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-23** [`48c3854620`](https://github.com/sgl-project/sglang/commit/48c3854620) [#39790](https://github.com/sgl-project/sglang/pull/39790)
  [ROCm] feat: enable aiter allreduce fusion for GLM models (#39790)
  _Files: `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/layers/communicator.py`, `test/registered/ops/test_aiter_allreduce_fusion_amd.py` _+1 more__
- **2026-09-23** [`aa0feca536`](https://github.com/sgl-project/sglang/commit/aa0feca536) [#40813](https://github.com/sgl-project/sglang/pull/40813)
  [AMD][DI][CI] Use a node-local model cache on the SPUR cluster (#40813)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`, `scripts/ci/slurm/launch_mi355x.sh`_
- **2026-09-22** [`d00adfd19c`](https://github.com/sgl-project/sglang/commit/d00adfd19c) [#39525](https://github.com/sgl-project/sglang/pull/39525)
  [AMD] Fix deferred Kimi-K3 forget gate in fused in-projection (#39525)
  _Files: `test/registered/amd/test_kimi_k3_kda_inproj_fusion.py`_
- **2026-09-22** [`8ac19cc19f`](https://github.com/sgl-project/sglang/commit/8ac19cc19f) [#39066](https://github.com/sgl-project/sglang/pull/39066)
  [AMD][Kimi-K3] Fix deferred KDA gate projection and update DCP cookbook (#39066)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`, `python/sglang/srt/models/kimi_k3.py`_
- **2026-09-22** [`264da63319`](https://github.com/sgl-project/sglang/commit/264da63319) [#39965](https://github.com/sgl-project/sglang/pull/39965)
  [AMD] Update ROCm AITER pin to acf8fdf9 (#39965)
  _Files: `docker/rocm.Dockerfile`_
- **2026-09-21** [`a5c2cc517c`](https://github.com/sgl-project/sglang/commit/a5c2cc517c) [#40527](https://github.com/sgl-project/sglang/pull/40527)
  [CI] Split the CI control labels into four axes and resolve them live (#40527)
  _Files: `.claude/skills/ci-test-audit/action-items.md`, `.claude/skills/ci-workflow-guide/SKILL.md`, `.claude/skills/write-sglang-test/SKILL.md`, `.github/MAINTAINER.md` _+18 more__
- **2026-09-21** [`66f19f5c46`](https://github.com/sgl-project/sglang/commit/66f19f5c46) [#40570](https://github.com/sgl-project/sglang/pull/40570)
  [AMD] Enable HiCache for GLM-5.2 MI355X throughput recipe (#40570)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-09-21** [`b86a30afba`](https://github.com/sgl-project/sglang/commit/b86a30afba) [#40113](https://github.com/sgl-project/sglang/pull/40113)
  [AMD][DI][CI] Add a SPUR cluster profile to AMD DI CI  (#40113)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`, `scripts/ci/slurm/launch_mi355x.sh`_

## Models  (11 commits)

- **2026-09-28** [`47ad1928a2`](https://github.com/sgl-project/sglang/commit/47ad1928a2) [#41226](https://github.com/sgl-project/sglang/pull/41226)
  [sgl-router] Scope input_ids forwarding by renderer: all text chats for DeepSeek-V4 (#41226)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/server/metrics.rs`, `experimental/sgl-router/src/server/routes/chat/preparation.rs`, `experimental/sgl-router/src/tokenizer/chat_formatter.rs` _+6 more__
- **2026-09-28** [`546bfa7221`](https://github.com/sgl-project/sglang/commit/546bfa7221) [#41164](https://github.com/sgl-project/sglang/pull/41164)
  [Kimi-K3] Merge fused_qkvg_proj into the loader-seeded packed_modules_mapping (#41164)
  _Files: `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/models/test_kimi_k3_packed_modules_mapping.py`_
- **2026-09-27** [`55d2ee5546`](https://github.com/sgl-project/sglang/commit/55d2ee5546) [#41437](https://github.com/sgl-project/sglang/pull/41437)
  [Refactor] Step-3.5: complete the dense MLP's sum through ffn_exit (#41437)
  _Files: `python/sglang/srt/models/step3p5.py`, `test/registered/unit/models/test_last_layer_communicator.py`, `test/registered/unit/models/test_step3p5_dense_reduce_scatter.py`_
- **2026-09-27** [`ecb8e9fc8f`](https://github.com/sgl-project/sglang/commit/ecb8e9fc8f) [#41434](https://github.com/sgl-project/sglang/pull/41434)
  [Refactor] Falcon-H1: complete the FFN's sum through ffn_exit (#41434)
  _Files: `python/sglang/srt/models/falcon_h1.py`, `test/registered/unit/layers/test_communicator_ffn_exit.py`_
- **2026-09-27** [`b4584ab838`](https://github.com/sgl-project/sglang/commit/b4584ab838) [#41221](https://github.com/sgl-project/sglang/pull/41221)
  [sgl-router] Take SGLang's render defaults: --default-chat-template-kwargs and thinking/effort envs (#41221)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs` _+27 more__
- **2026-09-25** [`b7f6d04a9a`](https://github.com/sgl-project/sglang/commit/b7f6d04a9a) [#41198](https://github.com/sgl-project/sglang/pull/41198)
  [Refactor] Move Step-3.5, GLM5-Next, Dots3, MiniMax-M3 and Qwen3.5 onto ffn_exit (#41198)
  _Files: `python/sglang/srt/models/dots3_common/modeling.py`, `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/qwen3_5.py` _+2 more__
- **2026-09-24** [`6bbd689ab4`](https://github.com/sgl-project/sglang/commit/6bbd689ab4) [#39929](https://github.com/sgl-project/sglang/pull/39929)
  [Bugfix] Align DeepSeek-V4.1 reasoning effort budgets (#39929)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `python/sglang/srt/entrypoints/openai/encoding_dsv41.py`_
- **2026-09-23** [`379e8f916b`](https://github.com/sgl-project/sglang/commit/379e8f916b) [#40801](https://github.com/sgl-project/sglang/pull/40801)
  [Fix] Capture complete Nemotron auxiliary hidden states (#40801)
  _Files: `python/sglang/srt/models/nemotron_h.py`, `test/registered/unit/models/test_nemotron_h_aux_capture.py`_
- **2026-09-23** [`0b0f947265`](https://github.com/sgl-project/sglang/commit/0b0f947265) [#39538](https://github.com/sgl-project/sglang/pull/39538)
  [CPU] Add fused_sigmod_mul_cpu operators to the Meta Muse Glimmer model. (#39538)
  _Files: `python/sglang/srt/models/muse_glimmer.py`_
- **2026-09-22** [`d72629e4ba`](https://github.com/sgl-project/sglang/commit/d72629e4ba) [#40770](https://github.com/sgl-project/sglang/pull/40770)
  Add GB200/GB300 hardware to Qwen3.5 (#40770)
  _Files: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-09-21** [`0abb251a20`](https://github.com/sgl-project/sglang/commit/0abb251a20) [#40530](https://github.com/sgl-project/sglang/pull/40530)
  [sgl-router] Match DeepSeek V4 rendering to SGLang (#40530)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/tokenizer/chat_formatter.rs`, `experimental/sgl-router/src/tokenizer/deepseek.rs`, `experimental/sgl-router/src/tokenizer/mod.rs` _+4 more__

## CI / Build  (11 commits)

- **2026-09-28** [`0823651b0b`](https://github.com/sgl-project/sglang/commit/0823651b0b) [#41075](https://github.com/sgl-project/sglang/pull/41075)
  [XPU] Disable test_ngram_corpus on XPU and detect XPU tests dynamically in CI filter (#41075)
  _Files: `.github/workflows/pr-test-xpu.yml`, `scripts/ci/xpu/detect_xpu_test_changes.py`_
- **2026-09-26** [`c842d32b0a`](https://github.com/sgl-project/sglang/commit/c842d32b0a) [#41285](https://github.com/sgl-project/sglang/pull/41285)
  [CI] Harden `/rerun-test` dispatch and partitioning (#41285)
  _Files: `.github/workflows/rerun-test.yml`, `scripts/ci/partition_rerun_tests.py`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/unit/tools/test_slash_command_handler.py`_
- **2026-09-25** [`62122c838a`](https://github.com/sgl-project/sglang/commit/62122c838a) [#41224](https://github.com/sgl-project/sglang/pull/41224)
  [XPU] Disable test_ngram_corpus on XPU and extend XPU CI path filter (#41224)
  _Files: `.github/workflows/pr-test-xpu.yml`, `test/registered/unit/spec/test_ngram_corpus.py`_
- **2026-09-24** [`81f2b43ab5`](https://github.com/sgl-project/sglang/commit/81f2b43ab5) [#40999](https://github.com/sgl-project/sglang/pull/40999)
  [ci] pr-gate: add generic require-label input and support pull_request_target (#40999)
  _Files: `.github/workflows/pr-gate.yml`_
- **2026-09-23** [`1d59ce7c90`](https://github.com/sgl-project/sglang/commit/1d59ce7c90) [#40760](https://github.com/sgl-project/sglang/pull/40760)
  fix: partition selective CI reruns into matrix jobs (#40760)
  _Files: `.github/workflows/rerun-test.yml`, `scripts/ci/partition_rerun_tests.py`_
- **2026-09-23** [`224a247d5b`](https://github.com/sgl-project/sglang/commit/224a247d5b) [#40749](https://github.com/sgl-project/sglang/pull/40749)
  [HiSparse] ci: add cross-directory rerun test group (#40749)
  _Files: `scripts/ci/rerun_test_groups.json`_
- **2026-09-23** [`0cd8be351d`](https://github.com/sgl-project/sglang/commit/0cd8be351d) [#40791](https://github.com/sgl-project/sglang/pull/40791)
  ci: stop Runner Utilization Report from draining the shared API quota (#40791)
  _Files: `scripts/ci/utils/runner_utilization_report.py`_
- **2026-09-22** [`a7b96fdad7`](https://github.com/sgl-project/sglang/commit/a7b96fdad7) [#40636](https://github.com/sgl-project/sglang/pull/40636)
  [ci] run cpu ci for renderer-only changes (#40636)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/_pr-test-stage-cpu.yml`, `.github/workflows/pr-test.yml`_
- **2026-09-22** [`244db08d60`](https://github.com/sgl-project/sglang/commit/244db08d60) [#40133](https://github.com/sgl-project/sglang/pull/40133)
  [NPU][CI] Constrain evalscope dependency versions (#40133)
  _Files: `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `python/sglang/test/ascend/e2e/run_evalscope.sh`_
- **2026-09-21** [`b18ca9ca44`](https://github.com/sgl-project/sglang/commit/b18ca9ca44) [#40620](https://github.com/sgl-project/sglang/pull/40620)
  [CI] Bump sgl-eval to 0.1.2 (#40620)
  _Files: `.github/workflows/_npu-pr-test-stage.yml`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` _+1 more__
- **2026-09-21** [`70b5b03e78`](https://github.com/sgl-project/sglang/commit/70b5b03e78) [#40549](https://github.com/sgl-project/sglang/pull/40549)
  [NPU][CI] Fix paths-filter negation that makes every PR run the NPU tier (#40549)
  _Files: `.github/workflows/pr-test-npu.yml`_

## Docs / Examples  (10 commits)

- **2026-09-28** [`6aacca2d91`](https://github.com/sgl-project/sglang/commit/6aacca2d91) [#40689](https://github.com/sgl-project/sglang/pull/40689)
  [Router] Name a replica's siblings with --kv-peer-selector (3/13) (#40689)
  _Files: `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs` _+6 more__
- **2026-09-24** [`17a7484c06`](https://github.com/sgl-project/sglang/commit/17a7484c06) [#40866](https://github.com/sgl-project/sglang/pull/40866)
  [chore] surface the cookbook to users who pip install sglang (#40866)
  _Files: `README.md`, `python/pyproject.toml`, `python/sglang/cli/generate.py`, `python/sglang/cli/main.py` _+1 more__
- **2026-09-24** [`82cdd72588`](https://github.com/sgl-project/sglang/commit/82cdd72588) [#41000](https://github.com/sgl-project/sglang/pull/41000)
  [NPU] [DOC] Remove --enforce-shared-experts-fusion from npu docs (#41000)
  _Files: `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`_
- **2026-09-23** [`ffac53d779`](https://github.com/sgl-project/sglang/commit/ffac53d779) [#40969](https://github.com/sgl-project/sglang/pull/40969)
  [Doc] Add H200 recipes to MiMo-V2.6 cookbook (#40969)
  _Files: `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`, `docs/src/snippets/configs/XiaomiMiMo/mimo-v2.6.jsx`_
- **2026-09-23** [`2e3568567b`](https://github.com/sgl-project/sglang/commit/2e3568567b) [#40766](https://github.com/sgl-project/sglang/pull/40766)
  [sgl-router] Launch reorg routing with existing policy options (#40766)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs` _+8 more__
- **2026-09-22** [`c08ffef709`](https://github.com/sgl-project/sglang/commit/c08ffef709) [#40655](https://github.com/sgl-project/sglang/pull/40655)
  docs: sync LMSYS SGLang blog cards (#40655)
  _Files: `docs/index.mdx`_
- **2026-09-22** [`542c817bfa`](https://github.com/sgl-project/sglang/commit/542c817bfa) [#40114](https://github.com/sgl-project/sglang/pull/40114)
  [Docs] Fix benchmark table column overflow in cookbook deployment panel (#40114)
  _Files: `docs/custom.css`, `docs/src/snippets/_deployment.jsx`_
- **2026-09-22** [`c948114d58`](https://github.com/sgl-project/sglang/commit/c948114d58) [#40647](https://github.com/sgl-project/sglang/pull/40647)
  [DOC] Update quickstart guide to use `sglang serve` for launching the server (#40647)
  _Files: `docs/docs/get-started/quickstart.mdx`_
- **2026-09-21** [`2261c2e618`](https://github.com/sgl-project/sglang/commit/2261c2e618) [#40622](https://github.com/sgl-project/sglang/pull/40622)
  Add MiMo-V2.6 cookbook (#40622)
  _Files: `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx`, `docs/cookbook/autoregressive/Xiaomi/MiMo-V2.6.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+1 more__
- **2026-09-21** [`b410010087`](https://github.com/sgl-project/sglang/commit/b410010087) [#40575](https://github.com/sgl-project/sglang/pull/40575)
  [NPU] [DOC] Add kimi k3 cookbook for 950PR/DT Series (#40575)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/_kimi_k3_mamba_ratio_calculator.jsx`, `docs/src/snippets/_playground.jsx` _+1 more__

## Speculative Decoding  (9 commits)

- **2026-09-28** [`7ee7bef79d`](https://github.com/sgl-project/sglang/commit/7ee7bef79d) [#39354](https://github.com/sgl-project/sglang/pull/39354)
  docs: add prefill context parallelism guide and design draft (#39354)
  _Files: `docs/docs.json`, `docs/docs/advanced_features/overview.mdx`, `docs/docs/advanced_features/prefill_cp.mdx`_
- **2026-09-24** [`1417345f5f`](https://github.com/sgl-project/sglang/commit/1417345f5f) [#40118](https://github.com/sgl-project/sglang/pull/40118)
  [Experimental] Preserve speculative decoding during prefill across DP ranks (#40118)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+7 more__
- **2026-09-23** [`eb5e8c84be`](https://github.com/sgl-project/sglang/commit/eb5e8c84be) [#31362](https://github.com/sgl-project/sglang/pull/31362)
  Speculative Decoding with NGRAM support for XPU (#31362)
  _Files: `python/sglang/kernels/ops/speculative/__init__.py`, `python/sglang/kernels/ops/speculative/reconstruct_tree.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/speculative/ngram_worker.py` _+2 more__
- **2026-09-22** [`790551c382`](https://github.com/sgl-project/sglang/commit/790551c382) [#35872](https://github.com/sgl-project/sglang/pull/35872)
  [AMD] Skip full-vocab softmax in EAGLE topk==1 draft on ROCm (#35872)
  _Files: `python/sglang/kernels/ops/speculative/topk1.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/kernels/ops/speculative/test_spec_topk1.py`_
- **2026-09-22** [`367e3700cf`](https://github.com/sgl-project/sglang/commit/367e3700cf) [#40111](https://github.com/sgl-project/sglang/pull/40111)
  avoid host sync in DSpark prefill slot expansion (#40111)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-09-22** [`bc22e1de9e`](https://github.com/sgl-project/sglang/commit/bc22e1de9e) [#40658](https://github.com/sgl-project/sglang/pull/40658)
  [DSpark] Fix draft CUDA graph stream explosion (#40658)
  _Files: `python/sglang/srt/distributed/parallel_state.py`_
- **2026-09-22** [`b01961e295`](https://github.com/sgl-project/sglang/commit/b01961e295) [#40651](https://github.com/sgl-project/sglang/pull/40651)
  [LFM2-VL] Add DSpark speculative decoding (#40651)
  _Files: `python/sglang/srt/models/lfm2_vl.py`_
- **2026-09-22** [`bc30fa1759`](https://github.com/sgl-project/sglang/commit/bc30fa1759) [#40598](https://github.com/sgl-project/sglang/pull/40598)
  [AMD][Fix] AgentX HIP TPOT regression when SGLANG_SIMULATE_ACC_LEN is set (#40598)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `test/registered/unit/spec/test_eagle_gate_routing.py`_
- **2026-09-22** [`98c8dee23b`](https://github.com/sgl-project/sglang/commit/98c8dee23b) [#40654](https://github.com/sgl-project/sglang/pull/40654)
  Fix lint failure from draft-decode window test location (#40654)
  _Files: `test/registered/kernels/ops/speculative/test_draft_decode_window.py`_

## Tensor / Data Parallel  (9 commits)

- **2026-09-27** [`19eb56fa57`](https://github.com/sgl-project/sglang/commit/19eb56fa57) [#41433](https://github.com/sgl-project/sglang/pull/41433)
  [Fix] Falcon-H1: count the Mamba mixer's output once under tensor parallelism (#41433)
  _Files: `python/sglang/srt/models/falcon_h1.py`, `test/registered/unit/models/test_falcon_h1_mixer_sums.py`_
- **2026-09-27** [`8c43c667cb`](https://github.com/sgl-project/sglang/commit/8c43c667cb) [#41430](https://github.com/sgl-project/sglang/pull/41430)
  [Refactor] Nemotron-H: build each layer's boundaries from its stage and the previous one (#41430)
  _Files: `python/sglang/srt/layers/boundary_layout.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py` _+6 more__
- **2026-09-25** [`3fc7a669bf`](https://github.com/sgl-project/sglang/commit/3fc7a669bf) [#41207](https://github.com/sgl-project/sglang/pull/41207)
  [CI] Move GLM-5.2 layer-split test to extra-b-test-8-gpu-b300 (#41207)
  _Files: `test/registered/e2e/models/test_dsa_glm52_pd_mtp_cp_layersplit.py`_
- **2026-09-24** [`e047e50d4e`](https://github.com/sgl-project/sglang/commit/e047e50d4e) [#37442](https://github.com/sgl-project/sglang/pull/37442)
  Add 8-node AllReduce/AllGather and MNVLS algorithm support to MSCCL++ (#37442)
  _Files: `benchmark/kernels/all_gather/benchmark_mscclpp.py`, `benchmark/kernels/all_reduce/benchmark_mscclpp.py`, `docker/Dockerfile`, `python/sglang/srt/arg_groups/fields/exec_.py` _+4 more__
- **2026-09-24** [`182f62d2de`](https://github.com/sgl-project/sglang/commit/182f62d2de) [#41162](https://github.com/sgl-project/sglang/pull/41162)
  [Fix] Patch set_dp_buffer_len_from_batch in DP spec prefill coordination test (#41162)
  _Files: `test/registered/unit/spec/test_dp_spec_prefill_coordination.py`_
- **2026-09-23** [`78980a3b0b`](https://github.com/sgl-project/sglang/commit/78980a3b0b) [#40795](https://github.com/sgl-project/sglang/pull/40795)
  [misc] Remove deprecated endpoints, env vars and aliases past two releases (#40795)
- **2026-09-22** [`01275aab6b`](https://github.com/sgl-project/sglang/commit/01275aab6b) [#40644](https://github.com/sgl-project/sglang/pull/40644)
  fix(grpc): expose native response timeout as a server argument (#40644)
  _Files: `python/sglang/srt/arg_groups/fields/serving.py`, `python/sglang/srt/arg_groups/serving_hook.py`, `python/sglang/srt/entrypoints/http_server.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-09-22** [`1d025491f3`](https://github.com/sgl-project/sglang/commit/1d025491f3) [#40667](https://github.com/sgl-project/sglang/pull/40667)
  [Test] Set DP size in the mocked Metal profiler test (#40667)
  _Files: `test/registered/unit/hardware_backend/mlx/test_metal_profiler.py`_
- **2026-09-21** [`14e9c40a72`](https://github.com/sgl-project/sglang/commit/14e9c40a72) [#39993](https://github.com/sgl-project/sglang/pull/39993)
  [Observability] Expose python/rust frontend identity in `/server_info` (#39993)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `rust/sglang-server/src/api_server/common.rs`, `test/registered/unit/entrypoints/test_server_info.py`_

## Serving / API  (5 commits)

- **2026-09-28** [`6405cf2881`](https://github.com/sgl-project/sglang/commit/6405cf2881) [#41517](https://github.com/sgl-project/sglang/pull/41517)
  Fix chat template cache key order (#41517)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`_
- **2026-09-25** [`3e7e652900`](https://github.com/sgl-project/sglang/commit/3e7e652900) [#28135](https://github.com/sgl-project/sglang/pull/28135)
  fix(openai): reject request-supplied chat_template by default (#28135)
  _Files: `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/serving.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py` _+1 more__
- **2026-09-22** [`66454d704b`](https://github.com/sgl-project/sglang/commit/66454d704b) [#40260](https://github.com/sgl-project/sglang/pull/40260)
  [Feature] Support --tokenizer-worker-num > 1 in the offline Engine API (#40260)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `test/registered/e2e/entrypoints/test_engine_multi_tokenizer.py`_
- **2026-09-22** [`b4701d672d`](https://github.com/sgl-project/sglang/commit/b4701d672d) [#40747](https://github.com/sgl-project/sglang/pull/40747)
  [rust-renderer] decouple renderer sampling from protocols (#40747)
  _Files: `rust/sglang-renderer/src/lib.rs`, `rust/sglang-renderer/src/openai/protocol.rs`, `rust/sglang-renderer/src/preprocessing/mod.rs`, `rust/sglang-renderer/src/preprocessing/sampling.rs`_
- **2026-09-21** [`11ecdbf39f`](https://github.com/sgl-project/sglang/commit/11ecdbf39f) [#40526](https://github.com/sgl-project/sglang/pull/40526)
  Clean up startup logging and streamline log audits (#40526)
  _Files: `.claude/skills/clean-startup-log/SKILL.md`, `.claude/skills/clean-startup-log/references/noise-sources.md`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/utils/common.py`_

## Structured Output  (5 commits)

- **2026-09-23** [`5b8d8b2f88`](https://github.com/sgl-project/sglang/commit/5b8d8b2f88) [#40468](https://github.com/sgl-project/sglang/pull/40468)
  [Fix] Keep Inkling automatic tool grammar active across the response (#40468)
  _Files: `python/sglang/srt/constrained/reasoner_grammar_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/constrained/test_reasoner_grammar_backend.py`_
- **2026-09-22** [`19ee4b566b`](https://github.com/sgl-project/sglang/commit/19ee4b566b) [#39632](https://github.com/sgl-project/sglang/pull/39632)
  fix(function_call): buffer complete DeepSeek DSML invokes (#39632)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/function_call/deepseekv32_detector.py`, `python/sglang/srt/function_call/utils.py`, `python/sglang/srt/parser/reasoning_parser.py` _+4 more__
- **2026-09-22** [`a9f02b0fa4`](https://github.com/sgl-project/sglang/commit/a9f02b0fa4) [#36120](https://github.com/sgl-project/sglang/pull/36120)
  [NPU] Fix xgrammar apply_vocab_mask device dispatch to use torch.ops.npu (#36120)
  _Files: `python/sglang/srt/constrained/xgrammar_backend.py`_
- **2026-09-21** [`8d08dfdab7`](https://github.com/sgl-project/sglang/commit/8d08dfdab7) [#40554](https://github.com/sgl-project/sglang/pull/40554)
  [Fix] Add gigachat35 to the tool-call and reasoning parser name lists (#40554)
  _Files: `python/sglang/srt/function_call/parser_names.py`, `python/sglang/srt/parser/reasoning_parser_names.py`_
- **2026-09-21** [`ab03a8e7eb`](https://github.com/sgl-project/sglang/commit/ab03a8e7eb) [#40201](https://github.com/sgl-project/sglang/pull/40201)
  [Perf] Fork-safe import: no CUDA context at import time, lighter argument parsing (#40201)
  _Files: `python/sglang/cli/utils.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/function_call/parser_names.py`, `python/sglang/srt/parser/reasoning_parser_names.py` _+7 more__

## LoRA  (2 commits)

- **2026-09-25** [`d3e3945e41`](https://github.com/sgl-project/sglang/commit/d3e3945e41) [#39379](https://github.com/sgl-project/sglang/pull/39379)
  [LoRA] Size dense row/column-parallel LoRA buffers from the base linear's real shard (#39379)
  _Files: `python/sglang/srt/lora/mem_pool.py`, `test/registered/unit/lora/test_mem_pool_ep_unit.py`_
- **2026-09-21** [`2016f5e7a1`](https://github.com/sgl-project/sglang/commit/2016f5e7a1) [#40390](https://github.com/sgl-project/sglang/pull/40390)
  [sgl-router] Add Kimi-K3 rendering with SGLang parity (#40390)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/tokenizer/adapter.rs` _+12 more__

---
_Generated 2026-09-28 16:43 UTC_