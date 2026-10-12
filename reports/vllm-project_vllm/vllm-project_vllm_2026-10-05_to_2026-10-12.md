# vllm-project/vllm — Weekly Change Report
**Period:** 2026-10-05 → 2026-10-12  |  **Total commits:** 455

## ✨ New Features This Week

- **2026-10-12** [#60456](https://github.com/vllm-project/vllm/pull/60456) — [CI] Add nightly Python 3.14 smoke test (#60456)
- **2026-10-12** [#52231](https://github.com/vllm-project/vllm/pull/52231) — [Feature] Support batch invariance on ROCm (#52231)
- **2026-10-12** [#49263](https://github.com/vllm-project/vllm/pull/49263) — [Perf] [Feat] [ROCm] Add densemha support to ROCm AITER Sparse MLA (#49263)
- **2026-10-12** [#61033](https://github.com/vllm-project/vllm/pull/61033) — [Model][LoRA] Enable LoRA support for BERT and RoBERTa embedding models (#61033)
- **2026-10-12** [#57549](https://github.com/vllm-project/vllm/pull/57549) — [EPLB] Add EPLB support to dspark draft models (DeepSeekV4) (#57549)
- **2026-10-12** [#61064](https://github.com/vllm-project/vllm/pull/61064) — [Model] Support Cloudflare/clef-omni on /v1/systemone (#61064)
- **2026-10-12** [#56322](https://github.com/vllm-project/vllm/pull/56322) — [Qwen4Exp] support Sequence Parallelism for Qwen3.8-Flash-Next (#56322)
- **2026-10-12** [#59549](https://github.com/vllm-project/vllm/pull/59549) — [Rust Frontend] Support logprob_token_ids on OpenAI endpoints (#59549)
- **2026-10-12** [#57322](https://github.com/vllm-project/vllm/pull/57322) — [Frontend] Support CustomToolCall in the non-Harmony Responses API (#57322)
- **2026-10-12** [#55812](https://github.com/vllm-project/vllm/pull/55812) — [Metrics] Add admission rejection metrics (#55812)
- _…and 65 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-12** [`e1a5086256`](https://github.com/vllm-project/vllm/commit/e1a5086256) [#61126](https://github.com/vllm-project/vllm/pull/61126) — [Attention] Remove cascade attention (#61126)
- **2026-10-12** [`e0317b28ce`](https://github.com/vllm-project/vllm/commit/e0317b28ce) [#52231](https://github.com/vllm-project/vllm/pull/52231) — [Feature] Support batch invariance on ROCm (#52231)
- **2026-10-12** [`50b21a2667`](https://github.com/vllm-project/vllm/commit/50b21a2667) [#49263](https://github.com/vllm-project/vllm/pull/49263) — [Perf] [Feat] [ROCm] Add densemha support to ROCm AITER Sparse MLA (#49263)
- **2026-10-12** [`a686c8e1b7`](https://github.com/vllm-project/vllm/commit/a686c8e1b7) [#60502](https://github.com/vllm-project/vllm/pull/60502) — [Triton] Migrate Triton kernels off tl.make_block_ptr for triton-main compat (#60502)
- **2026-10-12** [`8c175f403a`](https://github.com/vllm-project/vllm/commit/8c175f403a) [#61185](https://github.com/vllm-project/vllm/pull/61185) — [CI][ROCm] Compare greedy output only in the AITER attn+quant test (#61185)
- **2026-10-12** [`e3bbaf2369`](https://github.com/vllm-project/vllm/commit/e3bbaf2369) [#61004](https://github.com/vllm-project/vllm/pull/61004) — [ROCm][DSv4] Fuse the shared expert into AITER MegaMoE (#61004)
- **2026-10-11** [`c059bee812`](https://github.com/vllm-project/vllm/commit/c059bee812) [#61014](https://github.com/vllm-project/vllm/pull/61014) — [MRV2] Switch CI tests still running on MRV1 unnecessarily (#61014)
- **2026-10-10** [`a98247ab4d`](https://github.com/vllm-project/vllm/commit/a98247ab4d) [#59853](https://github.com/vllm-project/vllm/pull/59853) — [Model] Drop the 4x M-RoPE cache headroom for Qwen3-VL, Qwen3.5 and Qwen3.8 (#59853)
- **2026-10-10** [`7d0b4e57aa`](https://github.com/vllm-project/vllm/commit/7d0b4e57aa) [#56360](https://github.com/vllm-project/vllm/pull/56360) — [ROCm] Remove MRV1 model exceptions (#56360)
- **2026-10-10** [`2d69083c4a`](https://github.com/vllm-project/vllm/commit/2d69083c4a) [#55104](https://github.com/vllm-project/vllm/pull/55104) — [ROCm][MXFP4] Align the AITER W4A4 MoE intermediate size to 128 (#55104)
- **2026-10-10** [`193922d6ff`](https://github.com/vllm-project/vllm/commit/193922d6ff) [#60397](https://github.com/vllm-project/vllm/pull/60397) — [ROCm][Perf][DSv4.1] Mono decode layer for DeepSeek-V4.1-Flash on MI355X (#60397)
- **2026-10-09** [`02e55d2af3`](https://github.com/vllm-project/vllm/commit/02e55d2af3) [#57169](https://github.com/vllm-project/vllm/pull/57169) — [KV Cache] GLM-5.3-Flash: use the generic packed KV layout; CircularBufferSpec tail with speculative ring slots (#57169)
- **2026-10-09** [`b74233860d`](https://github.com/vllm-project/vllm/commit/b74233860d) [#60872](https://github.com/vllm-project/vllm/pull/60872) — [CI][ROCm] Wait for VRAM to settle before building LLM in test_full_graph (#60872)
- **2026-10-09** [`fc39317392`](https://github.com/vllm-project/vllm/commit/fc39317392) [#60446](https://github.com/vllm-project/vllm/pull/60446) — [Bugfix][Kernel] Remove invalid NC from Kimi-K3 KDA autotune keys (#60446)
- **2026-10-09** [`81c993658e`](https://github.com/vllm-project/vllm/commit/81c993658e) [#59732](https://github.com/vllm-project/vllm/pull/59732) — [ROCm][Perf] Fuse main QK-norm/RoPE/gate and KV-cache write into the AMD QSA prepare launch (#59732)
- **2026-10-09** [`2c99ee9333`](https://github.com/vllm-project/vllm/commit/2c99ee9333) [#60623](https://github.com/vllm-project/vllm/pull/60623) — [Chore] Remove vendored code made redundant by Transformers 5.16.1 (#60623)
- **2026-10-09** [`a6f43e57d6`](https://github.com/vllm-project/vllm/commit/a6f43e57d6) [#59523](https://github.com/vllm-project/vllm/pull/59523) — [ROCm] Enable the cuMem CUDA-graph pool offload on ROCm (#59523)
- **2026-10-09** [`560fae64cd`](https://github.com/vllm-project/vllm/commit/560fae64cd) [#59420](https://github.com/vllm-project/vllm/pull/59420) — [ROCm][Bugfix] Pass per-sequence context lengths to the AITER paged MQA-logits kernels (#59420)
- **2026-10-09** [`dd30786fef`](https://github.com/vllm-project/vllm/commit/dd30786fef) [#60016](https://github.com/vllm-project/vllm/pull/60016) — [CI] Enable Zen CPU image build on AMD CI (#60016)
- **2026-10-09** [`88a419649e`](https://github.com/vllm-project/vllm/commit/88a419649e) [#60717](https://github.com/vllm-project/vllm/pull/60717) — [ROCm][Kimi-K3] Use vLLM's FP8 max in the fused AttnRes quantization (#60717)
- **2026-10-08** [`240785b82c`](https://github.com/vllm-project/vllm/commit/240785b82c) [#59528](https://github.com/vllm-project/vllm/pull/59528) — [Bugfix] Keep the GLM-5.3 kpool tail and Qwen4 QSA ring out of the null block (#59528)
- **2026-10-08** [`c5c1161382`](https://github.com/vllm-project/vllm/commit/c5c1161382) [#59447](https://github.com/vllm-project/vllm/pull/59447) — [ROCm][Build] Fail fast when `setup.py develop` deps aren't pip-preinstalled (#59447)
- **2026-10-08** [`18751bc6a7`](https://github.com/vllm-project/vllm/commit/18751bc6a7) [#59334](https://github.com/vllm-project/vllm/pull/59334) — [ROCm][CI] Add coverage for AiterExperts token padding: inf/nan garbage rows (#59334)
- **2026-10-08** [`d8fa463e2b`](https://github.com/vllm-project/vllm/commit/d8fa463e2b) [#60533](https://github.com/vllm-project/vllm/pull/60533) — [Bugfix][Prefix caching] Fix inconsistent hybrid Mamba prefix cache boundaries (#60533)
- **2026-10-08** [`f4dde3132c`](https://github.com/vllm-project/vllm/commit/f4dde3132c) [#60633](https://github.com/vllm-project/vllm/pull/60633) — [CI][ROCm] Reuse AITER's prebuilt MoE module in the modular-kernel harness (#60633)
- **2026-10-08** [`9f3d70e081`](https://github.com/vllm-project/vllm/commit/9f3d70e081) [#55686](https://github.com/vllm-project/vllm/pull/55686) — [Quantization] Enable shared expert fusion compatibility with online `shared_expert` quantization (showcase: along Quark MXFP4 routed experts) (#55686)
- **2026-10-08** [`e2414ec1db`](https://github.com/vllm-project/vllm/commit/e2414ec1db) [#60021](https://github.com/vllm-project/vllm/pull/60021) — [ROCm][Qwen4Exp] Use fused PLE Triton kernels on the AMD backend (#60021)
- **2026-10-08** [`194bd72be7`](https://github.com/vllm-project/vllm/commit/194bd72be7) [#60517](https://github.com/vllm-project/vllm/pull/60517) — [Compile] Remove torch.compile-based sequence parallelism and AsyncTP (#60517)
- **2026-10-08** [`072d49bb6e`](https://github.com/vllm-project/vllm/commit/072d49bb6e) [#56959](https://github.com/vllm-project/vllm/pull/56959) — [Platform] Support platform-specific MLA prefill backend selection (#56959)
- **2026-10-08** [`994b8b77be`](https://github.com/vllm-project/vllm/commit/994b8b77be) [#60388](https://github.com/vllm-project/vllm/pull/60388) — [Bugfix][ROCm] RDNA3 W4A16 MoE: handle the N-first CT weight layout (#60388)
- **2026-10-08** [`d80ddaac73`](https://github.com/vllm-project/vllm/commit/d80ddaac73) [#59591](https://github.com/vllm-project/vllm/pull/59591) — [ROCm][Perf] Kimi-K3 Store only the current rank's shards in latent MoE up-proj  (#59591)
- **2026-10-08** [`273e099693`](https://github.com/vllm-project/vllm/commit/273e099693) [#59412](https://github.com/vllm-project/vllm/pull/59412) — [Bugfix][ROCm] Select page-aligned kernel blocks for pooled indexers so the block table addresses storage pages (GLM-5.3-Flash) (#59412)
- **2026-10-08** [`2f7f05c256`](https://github.com/vllm-project/vllm/commit/2f7f05c256) [#53250](https://github.com/vllm-project/vllm/pull/53250) — [Bugfix][MoRIIO] Prevent remote KV reload after decoder preemption (#53250)
- **2026-10-08** [`458ba2edf8`](https://github.com/vllm-project/vllm/commit/458ba2edf8) [#59069](https://github.com/vllm-project/vllm/pull/59069) — [ROCm][Kimi-K3] Fuse AttnRes output with per-token FP8 input quantization (#59069)
- **2026-10-08** [`fb2ac82458`](https://github.com/vllm-project/vllm/commit/fb2ac82458) [#56638](https://github.com/vllm-project/vllm/pull/56638) — [ROCm][DSv4.1][Perf] Replace the Torch prefill combine with the shared combine_topk_swa_indices kernel (#56638)
- **2026-10-08** [`4ac0179f8a`](https://github.com/vllm-project/vllm/commit/4ac0179f8a) [#60159](https://github.com/vllm-project/vllm/pull/60159) — [ROCm][Perf] Use native merge_attn_states kernel on gfx942/gfx950 (#60159)
- **2026-10-08** [`5dd4a628dd`](https://github.com/vllm-project/vllm/commit/5dd4a628dd) [#60367](https://github.com/vllm-project/vllm/pull/60367) — [ROCm][Bugfix] Map sleep-mode cuMem memory for the host (#60367)
- **2026-10-08** [`87d9996abe`](https://github.com/vllm-project/vllm/commit/87d9996abe) [#58584](https://github.com/vllm-project/vllm/pull/58584) — [ROCm][Perf][GLM-5.3-Flash] BF16 splitk kernel for sparse MLA decode (#58584)
- **2026-10-08** [`9dba339d07`](https://github.com/vllm-project/vllm/commit/9dba339d07) [#60389](https://github.com/vllm-project/vllm/pull/60389) — [Bugfix][ROCm] Keep MLA derived weights in place on weight reload (#60389)
- **2026-10-07** [`947dd62c07`](https://github.com/vllm-project/vllm/commit/947dd62c07) [#60462](https://github.com/vllm-project/vllm/pull/60462) — [CI] Fix failing test_deepseek_v4_rocm_dspark* tests (#60462)
- **2026-10-07** [`e572e02d21`](https://github.com/vllm-project/vllm/commit/e572e02d21) [#60152](https://github.com/vllm-project/vllm/pull/60152) — [UX] Skip checkpoint shards an MTP head does not load  (#60152)
- **2026-10-07** [`a8260cbc5c`](https://github.com/vllm-project/vllm/commit/a8260cbc5c) [#60381](https://github.com/vllm-project/vllm/pull/60381) — [CI] Bump Transformers version to 5.19.0 (#60381)
- **2026-10-07** [`d64a18832b`](https://github.com/vllm-project/vllm/commit/d64a18832b) [#59285](https://github.com/vllm-project/vllm/pull/59285) — [ROCm][Triton] Migrating MiniMax-M3 kernels from make_block_ptr to tensor descriptors (#59285)
- **2026-10-07** [`240ee8de9e`](https://github.com/vllm-project/vllm/commit/240ee8de9e) [#55053](https://github.com/vllm-project/vllm/pull/55053) — [Bugfix][KV Connector][ROCm] Fix MoRI-IO KV block-offset for speculative decoding (MTP) (#55053)
- **2026-10-07** [`71f9a74920`](https://github.com/vllm-project/vllm/commit/71f9a74920) [#60392](https://github.com/vllm-project/vllm/pull/60392) — [CI][ROCm] Re-enable the DSv4.1 decoder replay graph test on ROCm (#60392)
- **2026-10-07** [`548597367e`](https://github.com/vllm-project/vllm/commit/548597367e) [#57560](https://github.com/vllm-project/vllm/pull/57560) — [ROCm][Perf] Add AITER FlyDSL GDN prefill backend (#57560)
- **2026-10-07** [`f6e3944e31`](https://github.com/vllm-project/vllm/commit/f6e3944e31) [#59685](https://github.com/vllm-project/vllm/pull/59685) — [ROCm][DSv4] AITER MegaMoEV2 Integration For DeepSeek V4 (#59685)
- **2026-10-07** [`5281e49908`](https://github.com/vllm-project/vllm/commit/5281e49908) [#52619](https://github.com/vllm-project/vllm/pull/52619) — [ROCm][Perf] Enable medium-skinny dispatch in RDNAHybridW4A16LinearKernel (#52619)
- **2026-10-07** [`efb8d85f24`](https://github.com/vllm-project/vllm/commit/efb8d85f24) [#60292](https://github.com/vllm-project/vllm/pull/60292) — [ROCm][CI] Add FP32 rounding slack to accuracy test near-tie upper bounds (#60292)
- **2026-10-07** [`2a54f6b625`](https://github.com/vllm-project/vllm/commit/2a54f6b625) [#59221](https://github.com/vllm-project/vllm/pull/59221) — [ROCm][Perf][GLM-5.3-Flash] Enable AITER fused shared experts on gfx950 (#59221)
- **2026-10-07** [`d9503dc503`](https://github.com/vllm-project/vllm/commit/d9503dc503) [#59945](https://github.com/vllm-project/vllm/pull/59945) — [Bugfix][Qwen4Exp] Derive the QSA head_dim from the unsharded head count (#59945)
- **2026-10-07** [`02d8a94e61`](https://github.com/vllm-project/vllm/commit/02d8a94e61) [#60378](https://github.com/vllm-project/vllm/pull/60378) — [CI][ROCm] Skip DSv4.1 decoder replay graph test on ROCm (#60378)
- **2026-10-07** [`df417f780a`](https://github.com/vllm-project/vllm/commit/df417f780a) [#59164](https://github.com/vllm-project/vllm/pull/59164) — [Bugfix][MoRIIO] Exclude synchronous READ destinations from KV zeroing (#59164)
- **2026-10-07** [`42ecc8eebe`](https://github.com/vllm-project/vllm/commit/42ecc8eebe) [#59948](https://github.com/vllm-project/vllm/pull/59948) — [CI][RL] Consolidate RL entrypoint tests under tests/entrypoints/rl (#59948)
- **2026-10-07** [`2342343746`](https://github.com/vllm-project/vllm/commit/2342343746) [#59965](https://github.com/vllm-project/vllm/pull/59965) — [ROCm][DCP] Default MLA DCP verify to the round-robin asm decode where it applies (#59965)
- **2026-10-07** [`4b4eb6277a`](https://github.com/vllm-project/vllm/commit/4b4eb6277a) [#60323](https://github.com/vllm-project/vllm/pull/60323) — [CI] Remove AMD mirror of CPU-only Rust frontend cargo steps (#60323)
- **2026-10-06** [`385d86a6cf`](https://github.com/vllm-project/vllm/commit/385d86a6cf) [#57057](https://github.com/vllm-project/vllm/pull/57057) — [Attention] Add UltraQuant 4-bit KV cache backend (FlyDSL D=256) (#57057)
- **2026-10-06** [`e37e51dd24`](https://github.com/vllm-project/vllm/commit/e37e51dd24) [#56318](https://github.com/vllm-project/vllm/pull/56318) — [Metrics] Expose cached prompt tokens by cache tier (#56318)
- **2026-10-06** [`29f955cce0`](https://github.com/vllm-project/vllm/commit/29f955cce0) [#54857](https://github.com/vllm-project/vllm/pull/54857) — [ROCm] Fuse MLA dual RMSNorm + FP8 group quant for DeepSeek-R1 (#54857)
- **2026-10-06** [`b267fe4881`](https://github.com/vllm-project/vllm/commit/b267fe4881) [#56301](https://github.com/vllm-project/vllm/pull/56301) — [ROCm][Perf] W4A16: pad gfx11 weight and activation strides (#56301)
- **2026-10-06** [`edfccc9469`](https://github.com/vllm-project/vllm/commit/edfccc9469) [#59132](https://github.com/vllm-project/vllm/pull/59132) — [ROCM][Perf] Add ROCM_SEGMENTED_ATTN attention-backend works across RDNA3/3.5/4 (#59132)
- **2026-10-06** [`efd001756b`](https://github.com/vllm-project/vllm/commit/efd001756b) [#57750](https://github.com/vllm-project/vllm/pull/57750) — [ROCm] Disable AITER attention query quantization on RDNA3 (#57750)
- **2026-10-06** [`97bd8c74eb`](https://github.com/vllm-project/vllm/commit/97bd8c74eb) [#56720](https://github.com/vllm-project/vllm/pull/56720) — [ROCm][DSv4.1][Perf] One-pass dequantize and a gather-sized grid for the compressed K cache (#56720)
- **2026-10-05** [`fa423b614c`](https://github.com/vllm-project/vllm/commit/fa423b614c) [#60100](https://github.com/vllm-project/vllm/pull/60100) — [CI][ROCm] Wait for engine teardown between LM Eval models (#60100)
- **2026-10-05** [`182247257f`](https://github.com/vllm-project/vllm/commit/182247257f) [#52668](https://github.com/vllm-project/vllm/pull/52668) — [ROCm][Perf] Use a stacked hipBLASLt GEMM for the bf16x3 router  (#52668)
- **2026-10-05** [`d23af12cb1`](https://github.com/vllm-project/vllm/commit/d23af12cb1) [#57947](https://github.com/vllm-project/vllm/pull/57947) — [ROCm][Perf] Reach the fused QSA pre-indexer from the AMD path (#57947)
- **2026-10-05** [`30d4032363`](https://github.com/vllm-project/vllm/commit/30d4032363) [#59211](https://github.com/vllm-project/vllm/pull/59211) — [Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer (#59211)
- **2026-10-05** [`0e468adb43`](https://github.com/vllm-project/vllm/commit/0e468adb43) [#59278](https://github.com/vllm-project/vllm/pull/59278) — [Model] Extend device-side mm normalization to Kimi K2.5 / K3 (#59278)
- **2026-10-05** [`92044241a0`](https://github.com/vllm-project/vllm/commit/92044241a0) [#58014](https://github.com/vllm-project/vllm/pull/58014) — [Bugfix][ROCm] Preserve config during GPU memory profiling (#58014)
- **2026-10-05** [`ac8c2130a8`](https://github.com/vllm-project/vllm/commit/ac8c2130a8) [#59794](https://github.com/vllm-project/vllm/pull/59794) — [ROCm] Bump AITER to 0.1.24.post1 (#59794)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#61252](https://github.com/vllm-project/vllm/issues/61252) | [Bug]: Ministral 3 Fails to Run with Error About PixtralRotaryEmbeddin | bug | 2026-10-12 |
| [#61249](https://github.com/vllm-project/vllm/issues/61249) | [Bug]: /v1/systemone tokenizes the whole state once per question, so d | — | 2026-10-12 |
| [#60904](https://github.com/vllm-project/vllm/issues/60904) | [RFC]: A standard for MonoKernels in vllm/models | rocm, RFC, quantization, kimi | 2026-10-12 |
| [#32335](https://github.com/vllm-project/vllm/issues/32335) | [Feature]: Extract KV-Cache update from all attention backends | help wanted, good first issue, feature request | 2026-10-12 |
| [#60072](https://github.com/vllm-project/vllm/issues/60072) | [Tracking] HiSparse bugfixes and performance improvements | — | 2026-10-12 |
| [#60935](https://github.com/vllm-project/vllm/issues/60935) | [RFC][MoE]: Support dispatcher-native token dropping for MoE expert ca | RFC | 2026-10-12 |
| [#57406](https://github.com/vllm-project/vllm/issues/57406) | [Feature]: GLM 5.3 Performance Optimization | feature request, glm | 2026-10-12 |
| [#60791](https://github.com/vllm-project/vllm/issues/60791) | [Bug]: MiniMax-M3: PP startup, NIXL+PP prefill, NIXL+HMA+DSpark, offlo | kv-connector, minimax | 2026-10-12 |
| [#61206](https://github.com/vllm-project/vllm/issues/61206) | [Bug]: Qwen Tool Calling errors - 3 parser issues | bug, tool-calling, qwen | 2026-10-12 |
| [#61215](https://github.com/vllm-project/vllm/issues/61215) | [Bug]: /v1/systemone returns noise for thinking-only Qwen3 checkpoints | tool-calling | 2026-10-12 |
| [#61197](https://github.com/vllm-project/vllm/issues/61197) | [Bug]: MTP draft ignores target `--revision` (loads default branch) –  | bug, quantization | 2026-10-12 |
| [#61204](https://github.com/vllm-project/vllm/issues/61204) | [Bug]: [ROCm] requirements/rocm.txt hard-requires mooncake-transfer-en | rocm | 2026-10-12 |
| [#47930](https://github.com/vllm-project/vllm/issues/47930) | [Bug]: DFlash/DSpark draft acceptance collapses with automatic prefix  | bug | 2026-10-12 |
| [#48388](https://github.com/vllm-project/vllm/issues/48388) | [Usage]: Unevenly allocate gpu memory | usage, stale | 2026-10-12 |
| [#60561](https://github.com/vllm-project/vllm/issues/60561) | [Performance][NIXL] BLHNC MLA caches lost whole-row registration in #5 | kv-connector | 2026-10-12 |
| [#60703](https://github.com/vllm-project/vllm/issues/60703) | [Bug]: glm47 streaming parser silently swallows the rest of the stream | tool-calling | 2026-10-12 |
| [#61189](https://github.com/vllm-project/vllm/issues/61189) | [Bug]: /v1/systemone reads score levels named "1".."5" one level high, | — | 2026-10-12 |
| [#61172](https://github.com/vllm-project/vllm/issues/61172) | [Bug]: Anthropic Messages silently drops unsupported system content bl | bug | 2026-10-12 |
| [#60523](https://github.com/vllm-project/vllm/issues/60523) | [RFC]: Improving MooncakeConnector | RFC, kimi, k3 | 2026-10-12 |
| [#61150](https://github.com/vllm-project/vllm/issues/61150) | [Bug]: PIECEWISE CUDA graphs give wrong outputs when vllm::moe_forward | — | 2026-10-12 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 67 |
| Attention | 63 |
| Other | 55 |
| Serving / API | 39 |
| MoE / Expert Parallel | 35 |
| Scheduler / Engine | 30 |
| Disaggregation / PD | 28 |
| CI / Build | 26 |
| Models | 25 |
| Multimodal | 25 |
| Quantization | 15 |
| Speculative Decoding | 15 |
| KV Cache / Offload | 10 |
| Docs | 8 |
| LoRA | 6 |
| Perf / Benchmark | 6 |
| Distributed | 1 |
| Compilation / CUDA Graph | 1 |

## ROCm / AMD  (67 commits)

- **2026-10-12** [`e1a5086256`](https://github.com/vllm-project/vllm/commit/e1a5086256) [#61126](https://github.com/vllm-project/vllm/pull/61126)
  [Attention] Remove cascade attention (#61126)
  _Files: `docs/design/cuda_graphs.md`, `tests/conftest.py`, `tests/kernels/attention/test_cascade_flash_attn.py`, `tests/kernels/attention/test_prefix_prefill.py` _+44 more__
- **2026-10-12** [`e0317b28ce`](https://github.com/vllm-project/vllm/commit/e0317b28ce) [#52231](https://github.com/vllm-project/vllm/pull/52231)
  [Feature] Support batch invariance on ROCm (#52231)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `docs/features/batch_invariance.md`, `tests/kernels/quantization/test_triton_scaled_mm.py` _+27 more__
- **2026-10-12** [`50b21a2667`](https://github.com/vllm-project/vllm/commit/50b21a2667) [#49263](https://github.com/vllm-project/vllm/pull/49263)
  [Perf] [Feat] [ROCm] Add densemha support to ROCm AITER Sparse MLA (#49263)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/attention.yaml`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `tests/v1/attention/test_rocm_glm5next_sparse.py` _+3 more__
- **2026-10-12** [`a686c8e1b7`](https://github.com/vllm-project/vllm/commit/a686c8e1b7) [#60502](https://github.com/vllm-project/vllm/pull/60502)
  [Triton] Migrate Triton kernels off tl.make_block_ptr for triton-main compat (#60502)
  _Files: `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`, `vllm/models/inkling/amd/ops/fa4_rel_attention.py`, `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py` _+12 more__
- **2026-10-12** [`8c175f403a`](https://github.com/vllm-project/vllm/commit/8c175f403a) [#61185](https://github.com/vllm-project/vllm/pull/61185)
  [CI][ROCm] Compare greedy output only in the AITER attn+quant test (#61185)
  _Files: `tests/compile/correctness_e2e/test_attn_quant.py`_
- **2026-10-12** [`e3bbaf2369`](https://github.com/vllm-project/vllm/commit/e3bbaf2369) [#61004](https://github.com/vllm-project/vllm/pull/61004)
  [ROCm][DSv4] Fuse the shared expert into AITER MegaMoE (#61004)
  _Files: `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/distributed/device_communicators/all2all.py`, `vllm/envs.py`, `vllm/models/deepseek_v4/amd/mega_moe.py` _+1 more__
- **2026-10-11** [`c059bee812`](https://github.com/vllm-project/vllm/commit/c059bee812) [#61014](https://github.com/vllm-project/vllm/pull/61014)
  [MRV2] Switch CI tests still running on MRV1 unnecessarily (#61014)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/quantization.yaml`, `tests/basic_correctness/memory/sleep_mode/test_sleep_mode.py`, `tests/compile/correctness_e2e/test_attn_quant.py` _+8 more__
- **2026-10-10** [`a98247ab4d`](https://github.com/vllm-project/vllm/commit/a98247ab4d) [#59853](https://github.com/vllm-project/vllm/pull/59853)
  [Model] Drop the 4x M-RoPE cache headroom for Qwen3-VL, Qwen3.5 and Qwen3.8 (#59853)
  _Files: `vllm/config/model.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/mrope.py`, `vllm/model_executor/models/qwen3.py` _+7 more__
- **2026-10-10** [`7d0b4e57aa`](https://github.com/vllm-project/vllm/commit/7d0b4e57aa) [#56360](https://github.com/vllm-project/vllm/pull/56360)
  [ROCm] Remove MRV1 model exceptions (#56360)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-10-10** [`2d69083c4a`](https://github.com/vllm-project/vllm/commit/2d69083c4a) [#55104](https://github.com/vllm-project/vllm/pull/55104)
  [ROCm][MXFP4] Align the AITER W4A4 MoE intermediate size to 128 (#55104)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-10-10** [`193922d6ff`](https://github.com/vllm-project/vllm/commit/193922d6ff) [#60397](https://github.com/vllm-project/vllm/pull/60397)
  [ROCm][Perf][DSv4.1] Mono decode layer for DeepSeek-V4.1-Flash on MI355X (#60397)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_dsv41_mono_decode.py`, `tests/models/test_dsv41_mono_layers.py`, `tests/models/test_dsv41_mono_numerics.py` _+29 more__
- **2026-10-09** [`02e55d2af3`](https://github.com/vllm-project/vllm/commit/02e55d2af3) [#57169](https://github.com/vllm-project/vllm/pull/57169)
  [KV Cache] GLM-5.3-Flash: use the generic packed KV layout; CircularBufferSpec tail with speculative ring slots (#57169)
  _Files: `tests/kernels/attention/test_deepgemm_attention.py`, `tests/kernels/attention/test_rocm_aiter_mla_sink.py`, `tests/model_executor/test_jit_warmup_triton_launcher.py`, `tests/v1/attention/test_dspark_noncausal_sparse_mla.py` _+79 more__
- **2026-10-09** [`b74233860d`](https://github.com/vllm-project/vllm/commit/b74233860d) [#60872](https://github.com/vllm-project/vllm/pull/60872)
  [CI][ROCm] Wait for VRAM to settle before building LLM in test_full_graph (#60872)
  _Files: `tests/compile/fullgraph/test_full_graph.py`_
- **2026-10-09** [`fc39317392`](https://github.com/vllm-project/vllm/commit/fc39317392) [#60446](https://github.com/vllm-project/vllm/pull/60446)
  [Bugfix][Kernel] Remove invalid NC from Kimi-K3 KDA autotune keys (#60446)
  _Files: `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra.py`_
- **2026-10-09** [`81c993658e`](https://github.com/vllm-project/vllm/commit/81c993658e) [#59732](https://github.com/vllm-project/vllm/pull/59732)
  [ROCm][Perf] Fuse main QK-norm/RoPE/gate and KV-cache write into the AMD QSA prepare launch (#59732)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/qwen4_exp/test_qsa_amd.py`, `tests/models/qwen4_exp/test_qsa_prepare_amd.py`, `vllm/config/compilation.py` _+3 more__
- **2026-10-09** [`2c99ee9333`](https://github.com/vllm-project/vllm/commit/2c99ee9333) [#60623](https://github.com/vllm-project/vllm/pull/60623)
  [Chore] Remove vendored code made redundant by Transformers 5.16.1 (#60623)
  _Files: `.agents/skills/transformers-upgrade/SKILL.md`, `.agents/skills/transformers-upgrade/agents/openai.yaml`, `.agents/skills/transformers-upgrade/scripts/diff_dumps.py`, `.agents/skills/transformers-upgrade/scripts/dump_configs.py` _+72 more__
- **2026-10-09** [`a6f43e57d6`](https://github.com/vllm-project/vllm/commit/a6f43e57d6) [#59523](https://github.com/vllm-project/vllm/pull/59523)
  [ROCm] Enable the cuMem CUDA-graph pool offload on ROCm (#59523)
  _Files: `csrc/cumem_allocator.cpp`, `docs/features/sleep_mode.md`, `tests/basic_correctness/memory/cumem/test_cumem.py`, `tests/basic_correctness/memory/sleep_mode/test_sleep_mode.py` _+5 more__
- **2026-10-09** [`560fae64cd`](https://github.com/vllm-project/vllm/commit/560fae64cd) [#59420](https://github.com/vllm-project/vllm/pull/59420)
  [ROCm][Bugfix] Pass per-sequence context lengths to the AITER paged MQA-logits kernels (#59420)
  _Files: `tests/v1/attention/test_rocm_paged_mqa_context_lens.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-10-09** [`dd30786fef`](https://github.com/vllm-project/vllm/commit/dd30786fef) [#60016](https://github.com/vllm-project/vllm/pull/60016)
  [CI] Enable Zen CPU image build on AMD CI (#60016)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/image_build/image_build_zen_cpu.sh`_
- **2026-10-09** [`88a419649e`](https://github.com/vllm-project/vllm/commit/88a419649e) [#60717](https://github.com/vllm-project/vllm/pull/60717)
  [ROCm][Kimi-K3] Use vLLM's FP8 max in the fused AttnRes quantization (#60717)
  _Files: `tests/models/kimi_k3/test_amd_attn_res.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py`_
- **2026-10-08** [`240785b82c`](https://github.com/vllm-project/vllm/commit/240785b82c) [#59528](https://github.com/vllm-project/vllm/pull/59528)
  [Bugfix] Keep the GLM-5.3 kpool tail and Qwen4 QSA ring out of the null block (#59528)
  _Files: `tests/models/qwen4_exp/test_qsa_pre_indexer_amd.py`, `tests/models/qwen4_exp/test_qsa_reference.py`, `tests/v1/attention/test_kpool_tail_slot_mapping.py`, `vllm/models/qwen4_exp/common/qsa_cache.py` _+1 more__
- **2026-10-08** [`c5c1161382`](https://github.com/vllm-project/vllm/commit/c5c1161382) [#59447](https://github.com/vllm-project/vllm/pull/59447)
  [ROCm][Build] Fail fast when `setup.py develop` deps aren't pip-preinstalled (#59447)
  _Files: `setup.py`_
- **2026-10-08** [`18751bc6a7`](https://github.com/vllm-project/vllm/commit/18751bc6a7) [#59334](https://github.com/vllm-project/vllm/pull/59334)
  [ROCm][CI] Add coverage for AiterExperts token padding: inf/nan garbage rows (#59334)
  _Files: `tests/kernels/moe/test_modular_kernel_combinations.py`_
- **2026-10-08** [`d8fa463e2b`](https://github.com/vllm-project/vllm/commit/d8fa463e2b) [#60533](https://github.com/vllm-project/vllm/pull/60533)
  [Bugfix][Prefix caching] Fix inconsistent hybrid Mamba prefix cache boundaries (#60533)
  _Files: `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `tests/models/kimi_k3/test_prefix_cache.py`, `tests/v1/attention/test_gdn_metadata_builder.py` _+13 more__
- **2026-10-08** [`f4dde3132c`](https://github.com/vllm-project/vllm/commit/f4dde3132c) [#60633](https://github.com/vllm-project/vllm/pull/60633)
  [CI][ROCm] Reuse AITER's prebuilt MoE module in the modular-kernel harness (#60633)
  _Files: `tests/kernels/moe/modular_kernel_tools/common.py`_
- **2026-10-08** [`9f3d70e081`](https://github.com/vllm-project/vllm/commit/9f3d70e081) [#55686](https://github.com/vllm-project/vllm/pull/55686)
  [Quantization] Enable shared expert fusion compatibility with online `shared_expert` quantization (showcase: along Quark MXFP4 routed experts) (#55686)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/model_executor/model_loader/test_reload.py`, `tests/models/kimi_k3/test_gfx942_int4.py`, `tests/quantization/test_auto_gptq.py` _+20 more__
- **2026-10-08** [`e2414ec1db`](https://github.com/vllm-project/vllm/commit/e2414ec1db) [#60021](https://github.com/vllm-project/vllm/pull/60021)
  [ROCm][Qwen4Exp] Use fused PLE Triton kernels on the AMD backend (#60021)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/amd/model.py`, `vllm/models/qwen4_exp/amd/mtp.py`, `vllm/models/qwen4_exp/amd/ple_layer.py` _+4 more__
- **2026-10-08** [`194bd72be7`](https://github.com/vllm-project/vllm/commit/194bd72be7) [#60517](https://github.com/vllm-project/vllm/pull/60517)
  [Compile] Remove torch.compile-based sequence parallelism and AsyncTP (#60517)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/compile.yaml`, `docs/design/cuda_graphs.md`, `docs/design/fusions.md` _+30 more__
- **2026-10-08** [`072d49bb6e`](https://github.com/vllm-project/vllm/commit/072d49bb6e) [#56959](https://github.com/vllm-project/vllm/pull/56959)
  [Platform] Support platform-specific MLA prefill backend selection (#56959)
  _Files: `docs/mkdocs/gen_files/generate_attention_backends.py`, `tests/v1/attention/test_mla_prefill_selector.py`, `vllm/platforms/cpu.py`, `vllm/platforms/interface.py` _+7 more__
- **2026-10-08** [`994b8b77be`](https://github.com/vllm-project/vllm/commit/994b8b77be) [#60388](https://github.com/vllm-project/vllm/pull/60388)
  [Bugfix][ROCm] RDNA3 W4A16 MoE: handle the N-first CT weight layout (#60388)
  _Files: `tests/kernels/quantization/test_rdna3_moe_w4a16.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_wna16.py`_
- **2026-10-08** [`d80ddaac73`](https://github.com/vllm-project/vllm/commit/d80ddaac73) [#59591](https://github.com/vllm-project/vllm/pull/59591)
  [ROCm][Perf] Kimi-K3 Store only the current rank's shards in latent MoE up-proj  (#59591)
  _Files: `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`, `vllm/models/kimi_k3/amd/linear.py`_
- **2026-10-08** [`273e099693`](https://github.com/vllm-project/vllm/commit/273e099693) [#59412](https://github.com/vllm-project/vllm/pull/59412)
  [Bugfix][ROCm] Select page-aligned kernel blocks for pooled indexers so the block table addresses storage pages (GLM-5.3-Flash) (#59412)
  _Files: `tests/v1/attention/test_kpool_indexer_block_sizes.py`, `vllm/v1/worker/utils.py`_
- **2026-10-08** [`458ba2edf8`](https://github.com/vllm-project/vllm/commit/458ba2edf8) [#59069](https://github.com/vllm-project/vllm/pull/59069)
  [ROCm][Kimi-K3] Fuse AttnRes output with per-token FP8 input quantization (#59069)
  _Files: `benchmarks/kernels/benchmark_kimi_k3_amd_fp8_fusions.py`, `tests/models/kimi_k3/test_amd_attn_res.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/kda.py` _+3 more__
- **2026-10-08** [`fb2ac82458`](https://github.com/vllm-project/vllm/commit/fb2ac82458) [#56638](https://github.com/vllm-project/vllm/pull/56638)
  [ROCm][DSv4.1][Perf] Replace the Torch prefill combine with the shared combine_topk_swa_indices kernel (#56638)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`_
- **2026-10-08** [`4ac0179f8a`](https://github.com/vllm-project/vllm/commit/4ac0179f8a) [#60159](https://github.com/vllm-project/vllm/pull/60159)
  [ROCm][Perf] Use native merge_attn_states kernel on gfx942/gfx950 (#60159)
  _Files: `vllm/v1/attention/ops/merge_attn_states.py`_
- **2026-10-08** [`5dd4a628dd`](https://github.com/vllm-project/vllm/commit/5dd4a628dd) [#60367](https://github.com/vllm-project/vllm/pull/60367)
  [ROCm][Bugfix] Map sleep-mode cuMem memory for the host (#60367)
  _Files: `csrc/cumem_allocator.cpp`, `tests/basic_correctness/memory/sleep_mode/test_sleep_mode.py`_
- **2026-10-08** [`87d9996abe`](https://github.com/vllm-project/vllm/commit/87d9996abe) [#58584](https://github.com/vllm-project/vllm/pull/58584)
  [ROCm][Perf][GLM-5.3-Flash] BF16 splitk kernel for sparse MLA decode (#58584)
  _Files: `benchmarks/kernels/benchmark_sparse_mla_decode_bf16.py`, `tests/kernels/attention/test_rocm_aiter_mla_sink.py`, `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py` _+1 more__
- **2026-10-08** [`9dba339d07`](https://github.com/vllm-project/vllm/commit/9dba339d07) [#60389](https://github.com/vllm-project/vllm/pull/60389)
  [Bugfix][ROCm] Keep MLA derived weights in place on weight reload (#60389)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-10-07** [`947dd62c07`](https://github.com/vllm-project/vllm/commit/947dd62c07) [#60462](https://github.com/vllm-project/vllm/pull/60462)
  [CI] Fix failing test_deepseek_v4_rocm_dspark* tests (#60462)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_deepseek_v4_dspark_rocm.py`_
- **2026-10-07** [`e572e02d21`](https://github.com/vllm-project/vllm/commit/e572e02d21) [#60152](https://github.com/vllm-project/vllm/pull/60152)
  [UX] Skip checkpoint shards an MTP head does not load  (#60152)
  _Files: `tests/model_executor/model_loader/test_filter_duplicate_safetensors.py`, `vllm/model_executor/model_loader/default_loader.py`, `vllm/model_executor/model_loader/weight_utils.py`, `vllm/model_executor/models/nemotron_h_mtp.py` _+5 more__
- **2026-10-07** [`a8260cbc5c`](https://github.com/vllm-project/vllm/commit/a8260cbc5c) [#60381](https://github.com/vllm-project/vllm/pull/60381)
  [CI] Bump Transformers version to 5.19.0 (#60381)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+8 more__
- **2026-10-07** [`d64a18832b`](https://github.com/vllm-project/vllm/commit/d64a18832b) [#59285](https://github.com/vllm-project/vllm/pull/59285)
  [ROCm][Triton] Migrating MiniMax-M3 kernels from make_block_ptr to tensor descriptors (#59285)
  _Files: `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`_
- **2026-10-07** [`240ee8de9e`](https://github.com/vllm-project/vllm/commit/240ee8de9e) [#55053](https://github.com/vllm-project/vllm/pull/55053)
  [Bugfix][KV Connector][ROCm] Fix MoRI-IO KV block-offset for speculative decoding (MTP) (#55053)
  _Files: `tests/v1/kv_connector/unit/test_moriio_connector.py`, `tests/v1/kv_connector/unit/test_moriio_kv_layout.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout.py`_
- **2026-10-07** [`71f9a74920`](https://github.com/vllm-project/vllm/commit/71f9a74920) [#60392](https://github.com/vllm-project/vllm/pull/60392)
  [CI][ROCm] Re-enable the DSv4.1 decoder replay graph test on ROCm (#60392)
  _Files: `tests/models/test_deepseek_v41_decoder_replay_layers.py`_
- **2026-10-07** [`548597367e`](https://github.com/vllm-project/vllm/commit/548597367e) [#57560](https://github.com/vllm-project/vllm/pull/57560)
  [ROCm][Perf] Add AITER FlyDSL GDN prefill backend (#57560)
  _Files: `tests/v1/attention/test_gdn_aiter_flydsl.py`, `vllm/_aiter_ops.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py` _+1 more__
- **2026-10-07** [`f6e3944e31`](https://github.com/vllm-project/vllm/commit/f6e3944e31) [#59685](https://github.com/vllm-project/vllm/pull/59685)
  [ROCm][DSv4] AITER MegaMoEV2 Integration For DeepSeek V4 (#59685)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `tests/models/test_deepseek_v4_vl_rocm.py` _+6 more__
- **2026-10-07** [`5281e49908`](https://github.com/vllm-project/vllm/commit/5281e49908) [#52619](https://github.com/vllm-project/vllm/pull/52619)
  [ROCm][Perf] Enable medium-skinny dispatch in RDNAHybridW4A16LinearKernel (#52619)
  _Files: `tests/kernels/quantization/test_rdna_hybrid_w4a16.py`, `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`_
- **2026-10-07** [`efb8d85f24`](https://github.com/vllm-project/vllm/commit/efb8d85f24) [#60292](https://github.com/vllm-project/vllm/pull/60292)
  [ROCm][CI] Add FP32 rounding slack to accuracy test near-tie upper bounds (#60292)
  _Files: `tests/v1/e2e/general/accuracy_utils.py`_
- **2026-10-07** [`2a54f6b625`](https://github.com/vllm-project/vllm/commit/2a54f6b625) [#59221](https://github.com/vllm-project/vllm/pull/59221)
  [ROCm][Perf][GLM-5.3-Flash] Enable AITER fused shared experts on gfx950 (#59221)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py`_
- **2026-10-07** [`d9503dc503`](https://github.com/vllm-project/vllm/commit/d9503dc503) [#59945](https://github.com/vllm-project/vllm/pull/59945)
  [Bugfix][Qwen4Exp] Derive the QSA head_dim from the unsharded head count (#59945)
  _Files: `vllm/models/qwen4_exp/amd/qsa.py`, `vllm/models/qwen4_exp/nvidia/qsa.py`_
- **2026-10-07** [`02d8a94e61`](https://github.com/vllm-project/vllm/commit/02d8a94e61) [#60378](https://github.com/vllm-project/vllm/pull/60378)
  [CI][ROCm] Skip DSv4.1 decoder replay graph test on ROCm (#60378)
  _Files: `tests/models/test_deepseek_v41_decoder_replay_layers.py`_
- **2026-10-07** [`42ecc8eebe`](https://github.com/vllm-project/vllm/commit/42ecc8eebe) [#59948](https://github.com/vllm-project/vllm/pull/59948)
  [CI][RL] Consolidate RL entrypoint tests under tests/entrypoints/rl (#59948)
  _Files: `.buildkite/intel_jobs/entrypoints_intel.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/rl.yaml` _+16 more__
- **2026-10-07** [`2342343746`](https://github.com/vllm-project/vllm/commit/2342343746) [#59965](https://github.com/vllm-project/vllm/pull/59965)
  [ROCm][DCP] Default MLA DCP verify to the round-robin asm decode where it applies (#59965)
  _Files: `tests/v1/attention/test_rocm_aiter_mla_dcp_cprr.py`, `vllm/envs.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-10-07** [`4b4eb6277a`](https://github.com/vllm-project/vllm/commit/4b4eb6277a) [#60323](https://github.com/vllm-project/vllm/pull/60323)
  [CI] Remove AMD mirror of CPU-only Rust frontend cargo steps (#60323)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/rust_frontend_cargo.yaml`_
- **2026-10-06** [`385d86a6cf`](https://github.com/vllm-project/vllm/commit/385d86a6cf) [#57057](https://github.com/vllm-project/vllm/pull/57057)
  [Attention] Add UltraQuant 4-bit KV cache backend (FlyDSL D=256) (#57057)
  _Files: `tests/kernels/ultraquant/test_config.py`, `tests/kernels/ultraquant/test_decode_vs_reference.py`, `tests/kernels/ultraquant/test_dequant_vs_reference.py`, `tests/kernels/ultraquant/test_flydsl_decode_d256.py` _+18 more__
- **2026-10-06** [`29f955cce0`](https://github.com/vllm-project/vllm/commit/29f955cce0) [#54857](https://github.com/vllm-project/vllm/pull/54857)
  [ROCm] Fuse MLA dual RMSNorm + FP8 group quant for DeepSeek-R1 (#54857)
  _Files: `tests/compile/passes/test_fuse_mla_dual_rms_norm.py`, `vllm/_aiter_ops.py`, `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`_
- **2026-10-06** [`b267fe4881`](https://github.com/vllm-project/vllm/commit/b267fe4881) [#56301](https://github.com/vllm-project/vllm/pull/56301)
  [ROCm][Perf] W4A16: pad gfx11 weight and activation strides (#56301)
  _Files: `benchmarks/kernels/benchmark_rdna_hybrid_w4a16_gemm.py`, `csrc/rocm/skinny_gemms_int4.cu`, `tests/kernels/quantization/test_rdna_hybrid_w4a16.py`, `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`_
- **2026-10-06** [`edfccc9469`](https://github.com/vllm-project/vllm/commit/edfccc9469) [#59132](https://github.com/vllm-project/vllm/pull/59132)
  [ROCM][Perf] Add ROCM_SEGMENTED_ATTN attention-backend works across RDNA3/3.5/4 (#59132)
  _Files: `tests/kernels/attention/test_segmented_attention.py`, `tests/v1/attention/test_rocm_attention_backends_selection.py`, `vllm/config/kernel.py`, `vllm/model_executor/models/qwen3_dflash.py` _+5 more__
- **2026-10-06** [`efd001756b`](https://github.com/vllm-project/vllm/commit/efd001756b) [#57750](https://github.com/vllm-project/vllm/pull/57750)
  [ROCm] Disable AITER attention query quantization on RDNA3 (#57750)
  _Files: `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`_
- **2026-10-06** [`97bd8c74eb`](https://github.com/vllm-project/vllm/commit/97bd8c74eb) [#56720](https://github.com/vllm-project/vllm/pull/56720)
  [ROCm][DSv4.1][Perf] One-pass dequantize and a gather-sized grid for the compressed K cache (#56720)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`_
- **2026-10-05** [`fa423b614c`](https://github.com/vllm-project/vllm/commit/fa423b614c) [#60100](https://github.com/vllm-project/vllm/pull/60100)
  [CI][ROCm] Wait for engine teardown between LM Eval models (#60100)
  _Files: `.buildkite/lm-eval-harness/test_lm_eval_correctness.py`_
- **2026-10-05** [`182247257f`](https://github.com/vllm-project/vllm/commit/182247257f) [#52668](https://github.com/vllm-project/vllm/pull/52668)
  [ROCm][Perf] Use a stacked hipBLASLt GEMM for the bf16x3 router  (#52668)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/test_bf16x3_router_gemm_rocm.py`, `tests/kernels/test_gate_linear_rocm_dispatch.py`, `vllm/model_executor/layers/fused_moe/router/bf16x3_router_gemm_rocm.py` _+1 more__
- **2026-10-05** [`d23af12cb1`](https://github.com/vllm-project/vllm/commit/d23af12cb1) [#57947](https://github.com/vllm-project/vllm/pull/57947)
  [ROCm][Perf] Reach the fused QSA pre-indexer from the AMD path (#57947)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/qwen4_exp/test_qsa_amd.py`, `tests/models/qwen4_exp/test_qsa_pre_indexer_amd.py`, `vllm/models/qwen4_exp/amd/indexer_qsa.py` _+1 more__
- **2026-10-05** [`30d4032363`](https://github.com/vllm-project/vllm/commit/30d4032363) [#59211](https://github.com/vllm-project/vllm/pull/59211)
  [Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer (#59211)
  _Files: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `tests/v1/core/test_kv_cache_utils.py`, `vllm/model_executor/kernels/attention/dsa/dcp_indexer_cutedsl.py`, `vllm/models/glm5next/amd/sparse_indexer.py` _+5 more__
- **2026-10-05** [`0e468adb43`](https://github.com/vllm-project/vllm/commit/0e468adb43) [#59278](https://github.com/vllm-project/vllm/pull/59278)
  [Model] Extend device-side mm normalization to Kimi K2.5 / K3 (#59278)
  _Files: `docs/design/mm_processing.md`, `tests/models/multimodal/processing/test_kimi_k3.py`, `vllm/model_executor/layers/fusion/mm_input_norm.py`, `vllm/model_executor/models/kimi_k25.py` _+7 more__
- **2026-10-05** [`92044241a0`](https://github.com/vllm-project/vllm/commit/92044241a0) [#58014](https://github.com/vllm-project/vllm/pull/58014)
  [Bugfix][ROCm] Preserve config during GPU memory profiling (#58014)
  _Files: `tests/v1/worker/test_gpu_worker.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-10-05** [`ac8c2130a8`](https://github.com/vllm-project/vllm/commit/ac8c2130a8) [#59794](https://github.com/vllm-project/vllm/pull/59794)
  [ROCm] Bump AITER to 0.1.24.post1 (#59794)
  _Files: `docker/Dockerfile.rock_base`, `docker/Dockerfile.rocm_base`_

## Attention  (63 commits)

- **2026-10-12** [`c75cb63cd2`](https://github.com/vllm-project/vllm/commit/c75cb63cd2) [#56322](https://github.com/vllm-project/vllm/pull/56322)
  [Qwen4Exp] support Sequence Parallelism for Qwen3.8-Flash-Next (#56322)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_distributed.yaml`, `tests/kernels/core/test_vocab_parallel_embedding.py`, `tests/models/qwen4_exp/test_config.py` _+19 more__
- **2026-10-12** [`5a09062632`](https://github.com/vllm-project/vllm/commit/5a09062632) [#60781](https://github.com/vllm-project/vllm/pull/60781)
  [Rust Frontend] Compose answer constraints into parser-owned output grammars (#60781)
  _Files: `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/structural_tag.rs`, `rust/src/chat/tests/grammar_replay.py`, `rust/src/chat/tests/grammar_replay/DeepSeek-V3.2-Exp.json` _+37 more__
- **2026-10-12** [`a33d46b471`](https://github.com/vllm-project/vllm/commit/a33d46b471) [#58936](https://github.com/vllm-project/vllm/pull/58936)
  [Bugfix][XPU] Forward softcap and alibi_slopes in xpu_ops.flash_attn_varlen_func (#58936)
  _Files: `vllm/_xpu_ops.py`_
- **2026-10-12** [`36f3972812`](https://github.com/vllm-project/vllm/commit/36f3972812) [#60692](https://github.com/vllm-project/vllm/pull/60692)
  [Spec Decode] Skip metadata build for dflash/dspark when all model backends support it (#60692)
  _Files: `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `tests/v1/attention/test_triton_attn_metadata_builder.py`, `tests/v1/attention/test_triton_attn_segments.py`, `tests/v1/worker/test_gpu_target_dependent_ar_speculator.py` _+7 more__
- **2026-10-12** [`fe4df3df0e`](https://github.com/vllm-project/vllm/commit/fe4df3df0e) [#61079](https://github.com/vllm-project/vllm/pull/61079)
  [Bugfix][GLM-5.3-Flash] Restore MTP index sharing across draft iterations (#61079)
  _Files: `tests/config/test_speculative_draft_hf_overrides.py`, `vllm/config/speculative.py`_
- **2026-10-12** [`f147949be8`](https://github.com/vllm-project/vllm/commit/f147949be8) [#57297](https://github.com/vllm-project/vllm/pull/57297)
  [XPU] limit FA kernel block size to multipleOf 64 (#57297)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `tests/v1/kv_connector/unit/test_bidirectional_kv_transfer.py`, `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hma.py` _+7 more__
- **2026-10-11** [`3fe917abb1`](https://github.com/vllm-project/vllm/commit/3fe917abb1) [#61013](https://github.com/vllm-project/vllm/pull/61013)
  [Bugfix][MRV2] Fix FlashInfer attention and ReplaySSM warmups on MRV2 (#61013)
  _Files: `tests/model_executor/test_attention_warmup.py`, `vllm/model_executor/warmup/attention_warmup.py`, `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/model_executor/warmup/minimax_m3_msa_warmup.py` _+1 more__
- **2026-10-11** [`f26d9f432c`](https://github.com/vllm-project/vllm/commit/f26d9f432c) [#59147](https://github.com/vllm-project/vllm/pull/59147)
  [Bugfix][GLM-5.3-Flash] Honor `--mamba-ssm-cache-dtype` for the KDA recurrent state (#59147)
  _Files: `tests/models/glm5next/test_kda_state_dtype.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py`_
- **2026-10-11** [`3e8e1364ff`](https://github.com/vllm-project/vllm/commit/3e8e1364ff) [#54951](https://github.com/vllm-project/vllm/pull/54951)
  [Perf][GLM-5.3-Flash] Shard long-context indexer prefill rows across TP (#54951)
  _Files: `tests/v1/attention/test_indexer_tp_row_shard.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`, `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-10-11** [`2eb491e18b`](https://github.com/vllm-project/vllm/commit/2eb491e18b) [#60684](https://github.com/vllm-project/vllm/pull/60684)
  [Perf][MiniMax-M3] MSA prefill attends with the E4M3 query; bump fmha_sm100 to 968061a (#60684)
  _Files: `cmake/external_projects/fmha_sm100.cmake`, `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`_
- **2026-10-10** [`f2376cdc4d`](https://github.com/vllm-project/vllm/commit/f2376cdc4d) [#60085](https://github.com/vllm-project/vllm/pull/60085)
  [Fast Start] Preload the FlashInfer autotune table on the weight cache daemon (#60085)
  _Files: `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `tests/model_executor/test_flashinfer_autotune_warmup.py`, `vllm/entrypoints/cli/preload.py` _+6 more__
- **2026-10-10** [`46fb84c2d4`](https://github.com/vllm-project/vllm/commit/46fb84c2d4) [#60855](https://github.com/vllm-project/vllm/pull/60855)
  [Model] Support EAGLE3/DFlash aux hidden states for Granite (#60855)
  _Files: `vllm/model_executor/models/granite.py`_
- **2026-10-10** [`d5f356dae0`](https://github.com/vllm-project/vllm/commit/d5f356dae0) [#60647](https://github.com/vllm-project/vllm/pull/60647)
  [HiSparse] Own GPU residency instead of editing core block-table rows (#60647)
  _Files: `csrc/libtorch_stable/hisparse_kernels.cu`, `tests/v1/attention/test_sparse_mla_backends.py`, `tests/v1/core/test_prefix_caching.py`, `tests/v1/kv_connector/unit/test_hisparse_connector.py` _+11 more__
- **2026-10-10** [`9bd074a996`](https://github.com/vllm-project/vllm/commit/9bd074a996) [#60452](https://github.com/vllm-project/vllm/pull/60452)
  [Attention] Decode an NVFP4 KV cache with XQA on SM12x (#60452)
  _Files: `.buildkite/test_areas/attention.yaml`, `tests/v1/attention/test_attention_backends.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-10-10** [`29e4d2d42e`](https://github.com/vllm-project/vllm/commit/29e4d2d42e) [#58765](https://github.com/vllm-project/vllm/pull/58765)
  [Frontend][Build] Add `vllm download-kernels` for FlashInfer precompiled kernels (#58765)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `README.md`, `docker/Dockerfile`, `docker/versions.json` _+11 more__
- **2026-10-10** [`f1a3c60558`](https://github.com/vllm-project/vllm/commit/f1a3c60558) [#59085](https://github.com/vllm-project/vllm/pull/59085)
  [Feature][Attention] Cover a whole spec-verify in one DiffKV split-KV program (#59085)
  _Files: `tests/kernels/attention/test_triton_unified_attention_diffkv.py`, `vllm/v1/attention/ops/triton_unified_attention_diffkv.py`_
- **2026-10-10** [`1dfe9fbdae`](https://github.com/vllm-project/vllm/commit/1dfe9fbdae) [#59360](https://github.com/vllm-project/vllm/pull/59360)
  [Core] Release FlashInfer allreduce workspace with --enable-nccl-comm-suspend (#59360)
  _Files: `tests/distributed/test_comm_ops.py`, `vllm/distributed/device_communicators/cuda_communicator.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-10-10** [`7d1d8660d6`](https://github.com/vllm-project/vllm/commit/7d1d8660d6) [#60754](https://github.com/vllm-project/vllm/pull/60754)
  [MRV2] Miscellaneous code structure updates (#60754)
  _Files: `tests/v1/spec_decode/test_ngram_gpu.py`, `tests/v1/worker/test_gpu_kv_connector.py`, `tests/v1/worker/test_gpu_model_runner_v2.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py` _+14 more__
- **2026-10-10** [`f8e6e365ae`](https://github.com/vllm-project/vllm/commit/f8e6e365ae) [#60695](https://github.com/vllm-project/vllm/pull/60695)
  [Bugfix][Mooncake] Save the EAGLE attention proof with hybrid Mamba partial tails (#60695)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/kimi_k3/test_prefix_cache.py`, `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py` _+7 more__
- **2026-10-09** [`03a7d3776f`](https://github.com/vllm-project/vllm/commit/03a7d3776f) [#60345](https://github.com/vllm-project/vllm/pull/60345)
  [Perf] Support minimum KV splits configuration for TokenSpeed MLA decode  (#60345)
  _Files: `tests/engine/test_arg_utils.py`, `tests/v1/attention/test_mla_backends.py`, `vllm/config/attention.py`, `vllm/v1/attention/backends/mla/tokenspeed_mla.py`_
- **2026-10-09** [`ed7ae705a1`](https://github.com/vllm-project/vllm/commit/ed7ae705a1) [#60736](https://github.com/vllm-project/vllm/pull/60736)
  [Bugfix][MRV2] Use int64 index mappings to fix row-offset overflow (#60736)
  _Files: `tests/v1/worker/test_gpu_row_offsets_i64.py`, `vllm/v1/worker/gpu/buffer_utils.py`, `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/model_runner.py` _+6 more__
- **2026-10-09** [`3d52578e13`](https://github.com/vllm-project/vllm/commit/3d52578e13) [#60614](https://github.com/vllm-project/vllm/pull/60614)
  [Security] Do not retain Phi-4 MM audio attention matrices (#60614)
  _Files: `tests/model_executor/test_phi4mm_attention.py`, `vllm/model_executor/models/phi4mm_audio.py`, `vllm/model_executor/models/phi4mm_utils.py`_
- **2026-10-09** [`d095e61c0b`](https://github.com/vllm-project/vllm/commit/d095e61c0b) [#60763](https://github.com/vllm-project/vllm/pull/60763)
  [Bugfix][Spec Decode] Fix GLM-5.3-Flash DFlash2/EAGLE3 aux hidden-state capture with the upstream config (#60763)
  _Files: `vllm/models/glm5next/common/model.py`_
- **2026-10-09** [`19c0bed584`](https://github.com/vllm-project/vllm/commit/19c0bed584) [#59612](https://github.com/vllm-project/vllm/pull/59612)
  [Fusion] Support 3D activation quantization fusion and enable it for Pixtral (#59612)
  _Files: `tests/fusion/test_quant_activation_contract.py`, `tests/kernels/quantization/test_flashinfer_nvfp4_scaled_mm.py`, `tests/kernels/test_fused_quant_activation.py`, `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py` _+2 more__
- **2026-10-09** [`ad73a4740d`](https://github.com/vllm-project/vllm/commit/ad73a4740d) [#59894](https://github.com/vllm-project/vllm/pull/59894)
  [Perf][DSv4.1] Trim the last KV-source layer in decoder replay (#59894)
  _Files: `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/decoder_replay_layers.py` _+2 more__
- **2026-10-08** [`1afb029839`](https://github.com/vllm-project/vllm/commit/1afb029839) [#60682](https://github.com/vllm-project/vllm/pull/60682)
  [Bugfix][HiSparse] Route by swap-row capacity, not the index-group workspace (#60682)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/backends/mla/index_group.py`, `vllm/v1/hisparse/runtime.py`_
- **2026-10-08** [`fff10d2072`](https://github.com/vllm-project/vllm/commit/fff10d2072) [#60620](https://github.com/vllm-project/vllm/pull/60620)
  [Attention] Allow an NVFP4 KV cache on SM90 with fa2 (#60620)
  _Files: `tests/kernels/attention/test_flashinfer.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-10-08** [`2274e86842`](https://github.com/vllm-project/vllm/commit/2274e86842) [#56983](https://github.com/vllm-project/vllm/pull/56983)
  [Spec Decode][Model] Support DFlash2 draft models with GLM-5.3-Flash (#56983)
  _Files: `vllm/models/glm5next/common/model.py`_
- **2026-10-08** [`1664c4f444`](https://github.com/vllm-project/vllm/commit/1664c4f444) [#54597](https://github.com/vllm-project/vllm/pull/54597)
  [Bugfix][MiniMax-M3] Guard sparse decode sentinel indices (#54597)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`_
- **2026-10-08** [`0fc0cefb4e`](https://github.com/vllm-project/vllm/commit/0fc0cefb4e) [#60364](https://github.com/vllm-project/vllm/pull/60364)
  [Bugfix] Don't int-sort attention-type names in --kv-cache-dtype-skip-layers for packed KV dtypes (#60364)
  _Files: `vllm/engine/arg_utils.py`_
- **2026-10-08** [`fd928e5f3c`](https://github.com/vllm-project/vllm/commit/fd928e5f3c) [#60271](https://github.com/vllm-project/vllm/pull/60271)
  [Bugfix] Check batch-invariance support for every attention backend (#60271)
  _Files: `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-10-08** [`4ed4c4433b`](https://github.com/vllm-project/vllm/commit/4ed4c4433b) [#60429](https://github.com/vllm-project/vllm/pull/60429)
  [Bugfix][HiSparse] Drop the unaccounted, write-only prefill mirror staging buffer (#60429)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `tests/v1/worker/test_attn_utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/hisparse/worker.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+2 more__
- **2026-10-08** [`ba77c4c130`](https://github.com/vllm-project/vllm/commit/ba77c4c130) [#60156](https://github.com/vllm-project/vllm/pull/60156)
  [Bugfix][Attention] Preserve small FP8 softmax weights in Triton attention (#60156)
  _Files: `tests/kernels/attention/test_triton_unified_attention.py`, `vllm/v1/attention/ops/triton_unified_attention.py`_
- **2026-10-08** [`e265b77982`](https://github.com/vllm-project/vllm/commit/e265b77982) [#60515](https://github.com/vllm-project/vllm/pull/60515)
  [CI][Mamba] Use well-conditioned prompts for FlashInfer ReplaySSM parity tests (#60515)
  _Files: `tests/v1/e2e/test_replayssm_decode.py`_
- **2026-10-08** [`70bdce6133`](https://github.com/vllm-project/vllm/commit/70bdce6133) [#60032](https://github.com/vllm-project/vllm/pull/60032)
  [Model][GLM-5.3-Flash] Warm up the DCP top-k merge kernels for the kpool indexer (#60032)
  _Files: `vllm/models/glm5next/nvidia/sparse_indexer.py`_
- **2026-10-08** [`816173ca9d`](https://github.com/vllm-project/vllm/commit/816173ca9d) [#60434](https://github.com/vllm-project/vllm/pull/60434)
  [Kernel] Remove WAR for LL CuTeDSL BF16 GEMM (#60434)
  _Files: `tests/kernels/test_flashinfer_bf16_gemm.py`, `tests/model_executor/test_flashinfer_autotune_warmup.py`, `vllm/model_executor/layers/utils.py`, `vllm/model_executor/warmup/kernel_warmup.py` _+1 more__
- **2026-10-08** [`1fbbfa1657`](https://github.com/vllm-project/vllm/commit/1fbbfa1657) [#59733](https://github.com/vllm-project/vllm/pull/59733)
  [Bugfix][Kimi-K3] Declare max_tp_shards on the DSpark MLA KV cache spec (#59733)
  _Files: `tests/models/test_dspark_mla.py`, `vllm/models/kimi_k3/nvidia/mla.py`_
- **2026-10-08** [`a4b14e57b6`](https://github.com/vllm-project/vllm/commit/a4b14e57b6) [#41091](https://github.com/vllm-project/vllm/pull/41091)
  [Platform] Allow BackendEnum dynamic register (#41091)
  _Files: `tests/test_attention_backend_registry.py`, `tests/v1/attention/test_mla_prefill_registry.py`, `vllm/v1/attention/backends/mla/prefill/registry.py`, `vllm/v1/attention/backends/registry.py`_
- **2026-10-08** [`8faac3dd2a`](https://github.com/vllm-project/vllm/commit/8faac3dd2a) [#59655](https://github.com/vllm-project/vllm/pull/59655)
  [Bugfix] [Spec Decode]   DeepSeek V4/V4.1 NVFP4: keep ignored MTP/DSpark experts on MXFP4 (#59655)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/quantization.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml`, `tests/evals/gsm8k/configs/models-spec-decode.txt` _+2 more__
- **2026-10-07** [`b803edbc9f`](https://github.com/vllm-project/vllm/commit/b803edbc9f) [#60289](https://github.com/vllm-project/vllm/pull/60289)
  [Model] Streamline EmbeddingGemma 2 config resolution and harmonize Triton prefill attention (#60289)
  _Files: `tests/models/multimodal/pooling/test_embedding_gemma2.py`, `vllm/model_executor/models/config.py`, `vllm/transformers_utils/config.py`_
- **2026-10-07** [`fba462e008`](https://github.com/vllm-project/vllm/commit/fba462e008) [#58165](https://github.com/vllm-project/vllm/pull/58165)
  [Bugfix]Fix FlashInfer warmup crash: autotune(tuning_buckets=...) must round M up, not down (Invalid MXFP8 split-K tactic with spec-decode) (#58165)
  _Files: `tests/model_executor/test_flashinfer_autotune_warmup.py`, `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-10-07** [`554340f3d3`](https://github.com/vllm-project/vllm/commit/554340f3d3) [#46963](https://github.com/vllm-project/vllm/pull/46963)
  [Attention] Support NVFP4 KV cache on SM8x and SM12x with FlashInfer (#46963)
  _Files: `tests/kernels/attention/test_flashinfer.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-10-07** [`9367d8b969`](https://github.com/vllm-project/vllm/commit/9367d8b969) [#57992](https://github.com/vllm-project/vllm/pull/57992)
  [Bugfix][MLA] Scope DSpark non-causal capability to builder layers (#57992)
  _Files: `tests/v1/attention/test_mla_noncausal.py`, `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-10-07** [`aecb717f10`](https://github.com/vllm-project/vllm/commit/aecb717f10) [#59050](https://github.com/vllm-project/vllm/pull/59050)
  [CI] Allowlist-shrink batch 2: wire 9 tests/models/ files into Buildkite, fix 2 stale bugs found (#59050)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_dspark_mla.py`, `tests/models/transformers/test_layer_registry.py`, `tests/models/transformers/test_layer_registry_e2e.py` _+3 more__
- **2026-10-07** [`fe51194e2d`](https://github.com/vllm-project/vllm/commit/fe51194e2d) [#60194](https://github.com/vllm-project/vllm/pull/60194)
  [Bugfix][MiniMax-M3] Fence decode indexer shared-memory stage reuse (#60194)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/nvidia/ops/index_decode_score.py`_
- **2026-10-06** [`e43db1f5e2`](https://github.com/vllm-project/vllm/commit/e43db1f5e2) [#60029](https://github.com/vllm-project/vllm/pull/60029)
  Pad to 64 not 128 Q heads in flashMLA sparse (#60029)
  _Files: `vllm/models/hy_v4/nvidia/flashmla_sparse.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-10-06** [`3403e0f176`](https://github.com/vllm-project/vllm/commit/3403e0f176) [#57635](https://github.com/vllm-project/vllm/pull/57635)
  [Bugfix] Persist FlashInfer autotune cache per rank to fix the rank-0-only cache-hit deadlock (#57635)
  _Files: `tests/model_executor/test_flashinfer_autotune_warmup.py`, `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-10-06** [`02b83919aa`](https://github.com/vllm-project/vllm/commit/02b83919aa) [#60254](https://github.com/vllm-project/vllm/pull/60254)
  [Model] Support EmbeddingGemma2 multimodal pooling architecture (#60254)
  _Files: `tests/models/multimodal/pooling/test_embedding_gemma2.py`, `tests/models/registry.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/embedding_gemma2.py` _+3 more__
- **2026-10-06** [`fcf53d240c`](https://github.com/vllm-project/vllm/commit/fcf53d240c) [#58463](https://github.com/vllm-project/vllm/pull/58463)
  [Spec Decode] Remove eager metadata rebuild during MTP fused multi-step decode (#58463)
  _Files: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/mla/flashattn_mla_sparse.py`, `vllm/v1/attention/backends/mla/indexer.py` _+4 more__
- **2026-10-06** [`3313825983`](https://github.com/vllm-project/vllm/commit/3313825983) [#59992](https://github.com/vllm-project/vllm/pull/59992)
  [Bugfix][DiffusionGemma] Read the causal mask as int32 and compile the sample step (#59992)
  _Files: `csrc/cpu/cpu_attn.cpp`, `csrc/cpu/cpu_attn_impl.hpp`, `tests/kernels/attention/test_cpu_attn.py`, `tests/v1/sample/test_diffusion_gemma_reads.py` _+1 more__
- **2026-10-06** [`31e2443c90`](https://github.com/vllm-project/vllm/commit/31e2443c90) [#60080](https://github.com/vllm-project/vllm/pull/60080)
  [Model] LongCat-Flash: scale MLA norms while loading and drop the post-load sweep (#60080)
  _Files: `vllm/model_executor/models/longcat_flash.py`, `vllm/model_executor/models/longcat_flash_mtp.py`_
- **2026-10-06** [`e11962fc1c`](https://github.com/vllm-project/vllm/commit/e11962fc1c) [#57329](https://github.com/vllm-project/vllm/pull/57329)
  [Feat][Mamba2] Enable internal prefill checkpoints (#57329)
  _Files: `tests/entrypoints/tool_parsers/test_granite4_tool_parser.py`, `tests/kernels/mamba/test_mamba2_checkpoint_state.py`, `tests/v1/attention/test_mamba2_prefill_checkpoints.py`, `vllm/model_executor/layers/mamba/checkpoint.py` _+4 more__
- **2026-10-06** [`6ad2e06c4a`](https://github.com/vllm-project/vllm/commit/6ad2e06c4a) [#60052](https://github.com/vllm-project/vllm/pull/60052)
  fix: exclude flashinfer-jit-cache from wheel install_requires (#60052)
  _Files: `setup.py`_
- **2026-10-06** [`9a1f6fd4cb`](https://github.com/vllm-project/vllm/commit/9a1f6fd4cb) [#60064](https://github.com/vllm-project/vllm/pull/60064)
  [Model][DeepSeek-V4.1] Permute mega-attention wq_b / wo_a while loading (#60064)
  _Files: `tests/kernels/test_dsv41_mega_attn_layouts.py`, `vllm/models/deepseek_v41/common/ops/fused_layout.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` _+1 more__
- **2026-10-06** [`21d93d0d8c`](https://github.com/vllm-project/vllm/commit/21d93d0d8c) [#58128](https://github.com/vllm-project/vllm/pull/58128)
  [Attention][Model] FP8 KV cache for Triton DiffKV and MiMo-V2.6-Flash (#58128)
  _Files: `tests/kernels/attention/test_triton_unified_attention_diffkv.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`, `vllm/v1/attention/backends/triton_attn_diffkv.py` _+1 more__
- **2026-10-06** [`30ab428235`](https://github.com/vllm-project/vllm/commit/30ab428235) [#59751](https://github.com/vllm-project/vllm/pull/59751)
  [Bugfix][Attention] Restrict FlashInfer sparse MLA FULL graphs to decode (#59751)
  _Files: `tests/v1/attention/test_dspark_noncausal_sparse_mla.py`, `tests/v1/worker/test_attn_utils.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse.py`_
- **2026-10-06** [`b2863c0de9`](https://github.com/vllm-project/vllm/commit/b2863c0de9) [#56881](https://github.com/vllm-project/vllm/pull/56881)
  [Kimi-K3] Use the fused K/V pack kernel on the decode-context-parallel prefill path (#56881)
  _Files: `tests/models/kimi_k3/test_mla_prefill_context.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/models/kimi_k3/nvidia/mla.py`_
- **2026-10-05** [`0eac152707`](https://github.com/vllm-project/vllm/commit/0eac152707) [#56531](https://github.com/vllm-project/vllm/pull/56531)
  [Bugfix] Route every speculation-capable row through the speculative path so recurrent state stays consistent (#56531)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`, `tests/v1/attention/test_gdn_zero_draft_spec_rows.py`, `tests/v1/worker/test_gpu_model_runner_prefill_tail_classification.py`, `tests/v1/worker/test_mamba_hybrid_model_state.py` _+4 more__
- **2026-10-05** [`74c5cbcd7b`](https://github.com/vllm-project/vllm/commit/74c5cbcd7b) [#57053](https://github.com/vllm-project/vllm/pull/57053)
  [Bugfix][MRV2][Spec Decode] Honor dynamic K in autoregressive speculators, 1.2~1.3x kernel perf improvement (#57053)
  _Files: `tests/v1/cudagraph/test_cudagraph_manager.py`, `tests/v1/worker/test_gpu_autoregressive_speculator.py`, `tests/v1/worker/test_gpu_model_runner_v2.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py` _+11 more__
- **2026-10-05** [`ff53f32409`](https://github.com/vllm-project/vllm/commit/ff53f32409) [#59246](https://github.com/vllm-project/vllm/pull/59246)
  [Attention][MLA] Support fp8_ds_mla KV cache for NoPE-512 models on SM90 (#59246)
  _Files: `tests/v1/attention/test_flashmla_nope_sm90_backend_selection.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/backend.py` _+1 more__
- **2026-10-05** [`4ff028d77e`](https://github.com/vllm-project/vllm/commit/4ff028d77e) [#60023](https://github.com/vllm-project/vllm/pull/60023)
  [Bugfix][Qwen4Exp] Honor --kv-cache-dtype-skip-layers in QSA attention (#60023)
  _Files: `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/models/qwen4_exp/nvidia/qsa.py`_
- **2026-10-05** [`ae53b06898`](https://github.com/vllm-project/vllm/commit/ae53b06898) [#56974](https://github.com/vllm-project/vllm/pull/56974)
  [Bugfix][GLM-5.3-Flash] Keep batch x heads out of gridDim.z in the GLM-5.3-Flash fused recurrent KDA kernel (#56974)
  _Files: `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`_
- **2026-10-05** [`e8a53a55e6`](https://github.com/vllm-project/vllm/commit/e8a53a55e6) [#56198](https://github.com/vllm-project/vllm/pull/56198)
  [Bugfix][Attention] Support int4_per_token_head on non-power-of-two head sizes (#56198)
  _Files: `tests/kernels/attention/test_attention_selector.py`, `vllm/v1/attention/ops/int4_per_token_head.py`_

## Other  (55 commits)

- **2026-10-12** [`6e6e86078a`](https://github.com/vllm-project/vllm/commit/6e6e86078a) [#60766](https://github.com/vllm-project/vllm/pull/60766)
  [Bugfix][Platform] Don't resolve current_platform during import vllm (#60766)
  _Files: `tests/plugins/vllm_add_dummy_platform/vllm_add_dummy_platform/__init__.py`, `tests/plugins_tests/test_platform_plugins.py`, `vllm/utils/torch_utils.py`_
- **2026-10-12** [`d79b52b182`](https://github.com/vllm-project/vllm/commit/d79b52b182) [#60721](https://github.com/vllm-project/vllm/pull/60721)
  [Misc] Consolidate csrc shared headers and prune dead code (#60721)
- **2026-10-12** [`3facf822b7`](https://github.com/vllm-project/vllm/commit/3facf822b7) [#60825](https://github.com/vllm-project/vllm/pull/60825)
  [Performance] Load HF tokenizers and processors from a local snapshot (#60825)
  _Files: `tests/tokenizers_/test_basic.py`, `tests/transformers_utils/test_processor.py`, `vllm/tokenizers/registry.py`, `vllm/transformers_utils/processor.py` _+1 more__
- **2026-10-12** [`314ab8cffd`](https://github.com/vllm-project/vllm/commit/314ab8cffd) [#61047](https://github.com/vllm-project/vllm/pull/61047)
  [Bugfix][Structured Output] Drain compilation tasks before releasing the backend (#61047)
  _Files: `tests/v1/structured_output/test_structured_output_manager.py`, `vllm/v1/structured_output/__init__.py`_
- **2026-10-12** [`ac28877f0e`](https://github.com/vllm-project/vllm/commit/ac28877f0e) [#60945](https://github.com/vllm-project/vllm/pull/60945)
  [Bugfix] Fix out-of-bounds lookahead in adaptive block verification (#60945)
  _Files: `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-10-12** [`f5cda48c90`](https://github.com/vllm-project/vllm/commit/f5cda48c90) [#59937](https://github.com/vllm-project/vllm/pull/59937)
  [Bugfix][Rust Frontend] Export corrupted request metric (#59937)
  _Files: `rust/src/llm/src/request_metrics.rs`, `rust/src/llm/tests/generate.rs`, `rust/src/metrics/src/request.rs`_
- **2026-10-12** [`0466bd36ea`](https://github.com/vllm-project/vllm/commit/0466bd36ea) [#59190](https://github.com/vllm-project/vllm/pull/59190)
  [Rust Frontend] Build the Kimi K3 full-output grammar from its parser mode (#59190)
  _Files: `rust/src/chat/tests/grammar_replay/Kimi-K3.json`, `rust/src/chat/tests/grammar_replay/Kimi-K3.txt`, `rust/src/parser/src/output_grammar.rs`, `rust/src/parser/src/unified/kimi_k3.rs` _+4 more__
- **2026-10-12** [`e05201aa2e`](https://github.com/vllm-project/vllm/commit/e05201aa2e) [#61158](https://github.com/vllm-project/vllm/pull/61158)
  [XPU] refine memory release for sleep mode (#61158)
  _Files: `vllm/device_allocator/xpumem.py`, `vllm/model_executor/model_loader/sharded_state_loader.py`_
- **2026-10-12** [`5bed289707`](https://github.com/vllm-project/vllm/commit/5bed289707) [#60984](https://github.com/vllm-project/vllm/pull/60984)
  [DX] Update CODEOWNERS for entrypoints (#60984)
  _Files: `.github/CODEOWNERS`_
- **2026-10-12** [`f4114e068e`](https://github.com/vllm-project/vllm/commit/f4114e068e) [#61065](https://github.com/vllm-project/vllm/pull/61065)
  [Bugfix][Frontend] Preserve token IDs in chat derender responses (#61065)
  _Files: `tests/entrypoints/scale_out/derender/test_derender_parity.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `tests/entrypoints/scale_out/derender/utils.py`, `vllm/renderers/online_derenderer.py`_
- **2026-10-12** [`124b89d5b7`](https://github.com/vllm-project/vllm/commit/124b89d5b7) [#59962](https://github.com/vllm-project/vllm/pull/59962)
  [Bugfix][RecoverSSM] Correct aligned state indices at exact block boundaries (#59962)
  _Files: `tests/models/kimi_k3/test_kda.py`, `tests/v1/worker/test_mamba_hybrid_model_state.py`, `vllm/models/kimi_k3/nvidia/ops/recoverssm.py`, `vllm/v1/worker/gpu/model_states/recoverssm.py`_
- **2026-10-12** [`cc9b0f097d`](https://github.com/vllm-project/vllm/commit/cc9b0f097d) [#60917](https://github.com/vllm-project/vllm/pull/60917)
  [Fix] MiniMax: fix CUDA IPC handle exchange on cuda-bindings >= 13.4 (#60917)
  _Files: `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`_
- **2026-10-11** [`26a488ad93`](https://github.com/vllm-project/vllm/commit/26a488ad93) [#60966](https://github.com/vllm-project/vllm/pull/60966)
  [Fast Start][Bugfix] Snapshot GPU memory after external weights are ready (#60966)
  _Files: `vllm/v1/worker/gpu_worker.py`_
- **2026-10-11** [`ef42b4385f`](https://github.com/vllm-project/vllm/commit/ef42b4385f) [#57516](https://github.com/vllm-project/vllm/pull/57516)
  [Bugfix] Reclaim cached GPU memory during weight loading (#57516)
  _Files: `vllm/model_executor/model_loader/base_loader.py`_
- **2026-10-11** [`f8471164bf`](https://github.com/vllm-project/vllm/commit/f8471164bf) [#60937](https://github.com/vllm-project/vllm/pull/60937)
  [MRV2] Detatch weight-reload logic from MRV1 (#60937)
  _Files: `tests/v1/worker/test_gpu_model_runner.py`, `tests/v1/worker/test_gpu_worker_weight_transfer.py`, `vllm/model_executor/model_loader/reload/inplace.py`, `vllm/v1/worker/gpu/model_runner.py` _+2 more__
- **2026-10-10** [`838526c7e5`](https://github.com/vllm-project/vllm/commit/838526c7e5) [#60680](https://github.com/vllm-project/vllm/pull/60680)
  [Compile] Fix sampler compile warning (#60680)
  _Files: `csrc/libtorch_stable/sampler.cu`_
- **2026-10-10** [`c1692c85f1`](https://github.com/vllm-project/vllm/commit/c1692c85f1) [#60522](https://github.com/vllm-project/vllm/pull/60522)
  [Misc] mv chat_utils.py to renderers. (#60522)
- **2026-10-10** [`ff440c7805`](https://github.com/vllm-project/vllm/commit/ff440c7805) [#57881](https://github.com/vllm-project/vllm/pull/57881)
  [BreakableCG] Add eager break for Mamba-family ops (#57881)
  _Files: `vllm/model_executor/layers/mamba/gdn/olmo_gdn_linear_attn.py`, `vllm/model_executor/layers/mamba/linear/minimax_linear_attn.py`, `vllm/model_executor/layers/mamba/mamba_mixer.py`, `vllm/model_executor/layers/mamba/mamba_mixer2.py` _+1 more__
- **2026-10-10** [`acec1b1d84`](https://github.com/vllm-project/vllm/commit/acec1b1d84) [#57511](https://github.com/vllm-project/vllm/pull/57511)
  [Bugfix][XPU] Remove stale W4A8 weight after repacking (#57511)
  _Files: `vllm/model_executor/kernels/linear/mixed_precision/xpu.py`_
- **2026-10-09** [`fa94ad4143`](https://github.com/vllm-project/vllm/commit/fa94ad4143) [#60724](https://github.com/vllm-project/vllm/pull/60724)
  [Test] Allow one bf16 ulp in the fused mHC post/pre residual check (#60724)
  _Files: `tests/kernels/mhc/test_mhc_kernels.py`_
- **2026-10-09** [`e0cb3efce0`](https://github.com/vllm-project/vllm/commit/e0cb3efce0) [#60748](https://github.com/vllm-project/vllm/pull/60748)
  [Bugfix][Structured Output] Decode choice specs as JSON in outlines and LMFE (#60748)
  _Files: `tests/v1/structured_output/test_structured_output_manager.py`, `vllm/v1/structured_output/backend_lm_format_enforcer.py`, `vllm/v1/structured_output/backend_outlines.py`_
- **2026-10-09** [`ce4603cad6`](https://github.com/vllm-project/vllm/commit/ce4603cad6) [#59861](https://github.com/vllm-project/vllm/pull/59861)
  [Bugfix][Rust Frontend] Pass through raw characters in byte-level decode (#59861)
  _Files: `rust/src/tokenizer/src/byte_level_decode.rs`, `rust/src/tokenizer/src/hf.rs`_
- **2026-10-09** [`9adba10f3f`](https://github.com/vllm-project/vllm/commit/9adba10f3f) [#60840](https://github.com/vllm-project/vllm/pull/60840)
  [Bugfix] Fix pre-commit check (#60840)
  _Files: `tools/recipes/sweep/sweep_html_report.py`_
- **2026-10-09** [`28d76f3bad`](https://github.com/vllm-project/vllm/commit/28d76f3bad) [#60359](https://github.com/vllm-project/vllm/pull/60359)
  [Bugfix][Structured Output] Reject unsupported regex inside groups (#60359)
  _Files: `tests/v1/structured_output/test_backend_outlines.py`, `vllm/v1/structured_output/backend_outlines.py`_
- **2026-10-09** [`f43e4c39e3`](https://github.com/vllm-project/vllm/commit/f43e4c39e3) [#57594](https://github.com/vllm-project/vllm/pull/57594)
  [Structured Output] Allow propertyNames with additionalProperties on xgrammar (#57594)
  _Files: `tests/v1/structured_output/test_backend_xgrammar.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-10-09** [`f0a5f111f2`](https://github.com/vllm-project/vllm/commit/f0a5f111f2) [#56765](https://github.com/vllm-project/vllm/pull/56765)
  [XPU] Add tuned Mamba SSU configs for Intel Arc Pro B60 (#56765)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=128,dstate=256,device_name=Intel(R)_Arc(TM)_Pro_B60_Graphics,cache_dtype=float16.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=128,dstate=256,device_name=Intel(R)_Arc(TM)_Pro_B60_Graphics,cache_dtype=float32.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=Intel(R)_Arc(TM)_Pro_B60_Graphics,cache_dtype=float16.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=Intel(R)_Arc(TM)_Pro_B60_Graphics,cache_dtype=float32.json` _+4 more__
- **2026-10-09** [`e31b823bf5`](https://github.com/vllm-project/vllm/commit/e31b823bf5) [#60747](https://github.com/vllm-project/vllm/pull/60747)
  [Bugfix][Tool Parser] Use LongCat tags in the LongCat structural tag (#60747)
  _Files: `tests/tool_parsers/test_structural_tag_registry.py`, `vllm/tool_parsers/longcat_tool_parser.py`, `vllm/tool_parsers/structural_tag_registry.py`_
- **2026-10-09** [`9824159d94`](https://github.com/vllm-project/vllm/commit/9824159d94) [#60709](https://github.com/vllm-project/vllm/pull/60709)
  [Bugfix] Fix InternLM2 tool parser dropping characters from streamed arguments (#60709)
  _Files: `tests/tool_parsers/test_internlm2_tool_parser.py`, `vllm/tool_parsers/internlm2_tool_parser.py`_
- **2026-10-08** [`e41d5d5543`](https://github.com/vllm-project/vllm/commit/e41d5d5543) [#60412](https://github.com/vllm-project/vllm/pull/60412)
  [Bugfix] Don't warn about missing watermark config for default requests (#60412)
  _Files: `tests/watermarking/test_compatibility.py`, `vllm/config/vllm.py`_
- **2026-10-08** [`0751f5272f`](https://github.com/vllm-project/vllm/commit/0751f5272f) [#59917](https://github.com/vllm-project/vllm/pull/59917)
  [Bugfix] Scope deprecated CLI argument warnings to the parser that defines them (#59917)
  _Files: `tests/utils_/test_argparse_utils.py`, `vllm/utils/argparse_utils.py`_
- **2026-10-08** [`73c742b09c`](https://github.com/vllm-project/vllm/commit/73c742b09c) [#58067](https://github.com/vllm-project/vllm/pull/58067)
  [Bugfix] Make disable_any_whitespace actually disable whitespace on xgrammar (#58067)
  _Files: `tests/v1/structured_output/test_backend_xgrammar.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-10-08** [`e73895a5df`](https://github.com/vllm-project/vllm/commit/e73895a5df) [#59336](https://github.com/vllm-project/vllm/pull/59336)
  [Bugfix] Make `suppress_stdout` redirect fd 1 instead of `sys.stdout.fileno()` (#59336)
  _Files: `tests/utils_/test_system_utils.py`, `vllm/utils/system_utils.py`_
- **2026-10-08** [`4cf1307e72`](https://github.com/vllm-project/vllm/commit/4cf1307e72) [#57565](https://github.com/vllm-project/vllm/pull/57565)
  [XPU] Add tuned Mamba SSU configs for 2 more B70 shapes (#57565)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=256,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics,cache_dtype=float16.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=256,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics,cache_dtype=float32.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=64,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics,cache_dtype=float16.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=64,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics,cache_dtype=float32.json`_
- **2026-10-08** [`8733a21d55`](https://github.com/vllm-project/vllm/commit/8733a21d55) [#60398](https://github.com/vllm-project/vllm/pull/60398)
  [Core] Bound execute_dummy_batch RPC waits by the execute-model timeout (#60398)
  _Files: `tests/v1/executor/test_multiproc_executor.py`, `vllm/v1/executor/multiproc_executor.py`_
- **2026-10-08** [`fdfc171a74`](https://github.com/vllm-project/vllm/commit/fdfc171a74) [#60354](https://github.com/vllm-project/vllm/pull/60354)
  [Bugfix][ToolParser] Stream every tool call when one delta completes several (#60354)
  _Files: `tests/tool_use/test_tool_choice_required.py`, `vllm/parser/abstract_parser.py`, `vllm/renderers/online_derenderer.py`, `vllm/tool_parsers/streaming.py`_
- **2026-10-07** [`38dc8ee500`](https://github.com/vllm-project/vllm/commit/38dc8ee500) [#59749](https://github.com/vllm-project/vllm/pull/59749)
  [Bugfix] Validate tool-parser/tokenizer compatibility at startup (#59749)
  _Files: `vllm/parser/parser_manager.py`_
- **2026-10-07** [`d6fe5dca68`](https://github.com/vllm-project/vllm/commit/d6fe5dca68) [#58911](https://github.com/vllm-project/vllm/pull/58911)
  [Bugfix][Parser] Emit buffered post-reasoning text when no tool parser is configured (#58911)
  _Files: `tests/parser/test_streaming.py`, `vllm/parser/abstract_parser.py`_
- **2026-10-07** [`d169c5a903`](https://github.com/vllm-project/vllm/commit/d169c5a903) [#60111](https://github.com/vllm-project/vllm/pull/60111)
  [Docs] Add disagg PD flow-example guidance to /pr-checklist skill (#60111)
  _Files: `.agents/skills/pr-checklist/SKILL.md`_
- **2026-10-07** [`3d6853b32c`](https://github.com/vllm-project/vllm/commit/3d6853b32c) [#55601](https://github.com/vllm-project/vllm/pull/55601)
  [Bugfix] Seed hybrid mamba state index with mamba_block_size on prefix-cache hits (#55601)
  _Files: `tests/v1/worker/test_mamba_hybrid_model_state.py`, `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`_
- **2026-10-07** [`c83935b300`](https://github.com/vllm-project/vllm/commit/c83935b300) [#58124](https://github.com/vllm-project/vllm/pull/58124)
  [Bugfix][Model Loader] Support reload_weights with runai_streamer load format (#58124)
  _Files: `tests/model_executor/model_loader/runai_streamer_loader/test_runai_model_streamer_loader.py`, `tests/model_executor/model_loader/runai_streamer_loader/test_runai_model_streamer_s3.py`, `tests/v1/worker/test_gpu_model_runner.py`, `vllm/model_executor/model_loader/runai_streamer_loader.py` _+1 more__
- **2026-10-07** [`90f4936d9e`](https://github.com/vllm-project/vllm/commit/90f4936d9e) [#60192](https://github.com/vllm-project/vllm/pull/60192)
  [CI/Build] Widen the ragged prefill scoring tolerance, drop batch invariance (#60192)
  _Files: `tests/v1/sample/test_logprobs.py`_
- **2026-10-07** [`8a26869bca`](https://github.com/vllm-project/vllm/commit/8a26869bca) [#60210](https://github.com/vllm-project/vllm/pull/60210)
  [Bugfix] Index Mamba align state copies by request slot in MRV2 (#60210)
  _Files: `tests/kernels/mamba/test_precopy_mamba_align.py`, `tests/v1/worker/test_mamba_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/model_states/interface.py` _+2 more__
- **2026-10-06** [`bf049ddb8f`](https://github.com/vllm-project/vllm/commit/bf049ddb8f) [#60235](https://github.com/vllm-project/vllm/pull/60235)
  [Docs] Run pr-checklist before opening a PR (#60235)
  _Files: `.agents/skills/pr-checklist/SKILL.md`, `AGENTS.md`_
- **2026-10-06** [`049507aa76`](https://github.com/vllm-project/vllm/commit/049507aa76) [#59061](https://github.com/vllm-project/vllm/pull/59061)
  [Bugfix][Structured Output] Flag multi-branch allOf as unsupported for xgrammar (#59061)
  _Files: `tests/v1/structured_output/test_backend_xgrammar.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-10-06** [`68088ed392`](https://github.com/vllm-project/vllm/commit/68088ed392) [#59886](https://github.com/vllm-project/vllm/pull/59886)
  Fix grammar in `BlockPool.reset_prefix_cache` docstring: "to invalid" → "to invalidate" (#59886)
  _Files: `vllm/v1/core/block_pool.py`_
- **2026-10-06** [`1e5d0ea888`](https://github.com/vllm-project/vllm/commit/1e5d0ea888) [#46779](https://github.com/vllm-project/vllm/pull/46779)
  [CI/Build] Fix incorrect CLI arg validation tests in test_cli_args.py (#46779)
  _Files: `tests/entrypoints/launchers/test_cli_args.py`_
- **2026-10-06** [`48eb44b719`](https://github.com/vllm-project/vllm/commit/48eb44b719) [#60157](https://github.com/vllm-project/vllm/pull/60157)
  [Bugfix][KVConnector][NIXL] Fix TP handshake test after per-region FA desc flags (#60157)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`_
- **2026-10-06** [`6fa67afed9`](https://github.com/vllm-project/vllm/commit/6fa67afed9) [#59759](https://github.com/vllm-project/vllm/pull/59759)
  [Bugfix][Core] Retire stale Mamba spec blocks in prefill checkpoint steps (#59759)
  _Files: `tests/v1/core/test_single_type_kv_cache_manager.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-10-06** [`9bf4e51030`](https://github.com/vllm-project/vllm/commit/9bf4e51030) [#54850](https://github.com/vllm-project/vllm/pull/54850)
  [Bugfix][Frontend] Malformed `$defs` in a tool schema should be a 400, not a 500 (#54850)
  _Files: `tests/tool_use/test_tool_choice_required.py`, `vllm/tool_parsers/utils.py`_
- **2026-10-05** [`2e06395fd3`](https://github.com/vllm-project/vllm/commit/2e06395fd3) [#59879](https://github.com/vllm-project/vllm/pull/59879)
  [Bugfix][Frontend] Build tool-call grammars from the tools the prompt renders (#59879)
  _Files: `tests/tool_parsers/test_structural_tag_registry.py`, `tests/tool_use/test_tool_choice_required.py`, `vllm/parser/abstract_parser.py`, `vllm/parser/harmony.py` _+2 more__
- **2026-10-05** [`3fb1cd796b`](https://github.com/vllm-project/vllm/commit/3fb1cd796b) [#60073](https://github.com/vllm-project/vllm/pull/60073)
  [Frontend] Extract parse and assembly out of batch chat derender (#60073)
  _Files: `vllm/renderers/online_derenderer.py`_
- **2026-10-05** [`877ddcc456`](https://github.com/vllm-project/vllm/commit/877ddcc456) [#59105](https://github.com/vllm-project/vllm/pull/59105)
  [Bugfix][Spec Decode] Reserve the bonus KV slot for fill-in DSpark (#59105)
  _Files: `tests/v1/worker/test_gpu_warmup_blocks.py`, `vllm/config/vllm.py`_
- **2026-10-05** [`54d93af9fb`](https://github.com/vllm-project/vllm/commit/54d93af9fb) [#59688](https://github.com/vllm-project/vllm/pull/59688)
  [Bugfix][HiSparse] Reject cudagraph_mode=FULL at startup (#59688)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-10-05** [`f2d8fbf459`](https://github.com/vllm-project/vllm/commit/f2d8fbf459) [#60056](https://github.com/vllm-project/vllm/pull/60056)
  [CI/Build] Run the prefill token scoring test under batch invariance (#60056)
  _Files: `tests/v1/sample/test_logprobs.py`_
- **2026-10-05** [`60932a6401`](https://github.com/vllm-project/vllm/commit/60932a6401) [#58709](https://github.com/vllm-project/vllm/pull/58709)
  [Bugfix][Structured Output] Preserve literal values in Guidance disable_additional_properties (#58709)
  _Files: `tests/v1/structured_output/test_backend_guidance.py`, `vllm/v1/structured_output/backend_guidance.py`_

## Serving / API  (39 commits)

- **2026-10-12** [`c599b5971f`](https://github.com/vllm-project/vllm/commit/c599b5971f) [#55717](https://github.com/vllm-project/vllm/pull/55717)
  [Bugfix][Frontend] Return all logprobs when completions requests logprobs=-1 (#55717)
  _Files: `tests/entrypoints/openai/completion/test_completion_error.py`, `vllm/entrypoints/openai/completion/serving.py`_
- **2026-10-12** [`fa39582756`](https://github.com/vllm-project/vllm/commit/fa39582756) [#60676](https://github.com/vllm-project/vllm/pull/60676)
  [Frontend] Serve LiquidAI/d1-3B on /v1/systemone (#60676)
  _Files: `docs/serving/online_serving/structured_decisions.md`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `vllm/entrypoints/generate/structured_decisions/strategies.py`_
- **2026-10-12** [`f022975964`](https://github.com/vllm-project/vllm/commit/f022975964) [#61212](https://github.com/vllm-project/vllm/pull/61212)
  [Bugfix] Reject beam search in completion render (#61212)
  _Files: `tests/entrypoints/scale_out/render/test_render.py`, `vllm/entrypoints/scale_out/render/serving.py`_
- **2026-10-12** [`8d7b93fec2`](https://github.com/vllm-project/vllm/commit/8d7b93fec2) [#60251](https://github.com/vllm-project/vllm/pull/60251)
  [Frontend] Report stop_reason on /inference/v1/generate and pass it through derender (#60251)
  _Files: `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/inference/generate/types.rs`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py` _+4 more__
- **2026-10-12** [`21445806bd`](https://github.com/vllm-project/vllm/commit/21445806bd) [#59549](https://github.com/vllm-project/vllm/pull/59549)
  [Rust Frontend] Support logprob_token_ids on OpenAI endpoints (#59549)
  _Files: `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/openai/chat_completions/types.rs`, `rust/src/server/src/routes/openai/chat_completions/validate.rs`, `rust/src/server/src/routes/openai/completions/convert.rs` _+4 more__
- **2026-10-12** [`d4e92ccc37`](https://github.com/vllm-project/vllm/commit/d4e92ccc37) [#58839](https://github.com/vllm-project/vllm/pull/58839)
  [Bugfix][Frontend] Honor endpoint plugin route overrides (#58839)
  _Files: `docs/design/endpoint_plugins.md`, `tests/plugins_tests/test_endpoint_plugins.py`, `vllm/entrypoints/launchers/app.py`, `vllm/plugins/endpoint_plugins/interface.py`_
- **2026-10-11** [`f425a21208`](https://github.com/vllm-project/vllm/commit/f425a21208) [#57243](https://github.com/vllm-project/vllm/pull/57243)
  [Bugfix][Frontend] Support scalar priority and wire priority into LLM.chat() (#57243)
  _Files: `tests/entrypoints/llm/test_chat.py`, `tests/entrypoints/llm/test_generate.py`, `tests/entrypoints/unit_tests/test_offline_utils.py`, `vllm/entrypoints/common/offline.py` _+1 more__
- **2026-10-11** [`1789f09588`](https://github.com/vllm-project/vllm/commit/1789f09588) [#61042](https://github.com/vllm-project/vllm/pull/61042)
  [Frontend] Explain disabled scale-out endpoints with opt-in hints (#61042)
  _Files: `docs/usage/security.md`, `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/tests.rs`, `tests/entrypoints/scale_out/test_factories.py` _+1 more__
- **2026-10-11** [`fcae5c9887`](https://github.com/vllm-project/vllm/commit/fcae5c9887) [#61009](https://github.com/vllm-project/vllm/pull/61009)
  [Security] Restrict default CORS origins (#61009)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/server/src/config.rs`, `rust/src/server/src/middleware/cors.rs` _+4 more__
- **2026-10-10** [`187a0eb98a`](https://github.com/vllm-project/vllm/commit/187a0eb98a) [#60982](https://github.com/vllm-project/vllm/pull/60982)
  [Bugfix][Frontend] Forward --enable-log-outputs to the Anthropic handler (#60982)
  _Files: `vllm/entrypoints/anthropic/serving.py`, `vllm/entrypoints/generate/api_router.py`_
- **2026-10-10** [`c41b2639e2`](https://github.com/vllm-project/vllm/commit/c41b2639e2) [#60973](https://github.com/vllm-project/vllm/pull/60973)
  [Bugfix][Responses API] Complete cache-write token accounting (#60973)
  _Files: `tests/entrypoints/openai/responses/test_parsable_context_unit.py`, `tests/entrypoints/unit_tests/test_context.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/serving.py`_
- **2026-10-10** [`8ea646b827`](https://github.com/vllm-project/vllm/commit/8ea646b827) [#60922](https://github.com/vllm-project/vllm/pull/60922)
  [Rust Frontend][gRPC] Remove `GenerateStream` producer task so disconnects abort requests (#60922)
  _Files: `rust/Cargo.lock`, `rust/src/server/Cargo.toml`, `rust/src/server/src/grpc/inference.rs`, `rust/src/server/src/grpc/tests.rs`_
- **2026-10-09** [`c811943137`](https://github.com/vllm-project/vllm/commit/c811943137) [#60876](https://github.com/vllm-project/vllm/pull/60876)
  [Bugfix][Frontend] Reject beam search with echo and logprobs in /v1/completions (#60876)
  _Files: `tests/entrypoints/openai/completion/test_completion_error.py`, `vllm/entrypoints/openai/completion/protocol.py`_
- **2026-10-09** [`1a3a7a8f01`](https://github.com/vllm-project/vllm/commit/1a3a7a8f01) [#57035](https://github.com/vllm-project/vllm/pull/57035)
  [Bugfix] Treat max_tokens as output upper bound, not input-space reservation (#57035)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/responses/test_serving_responses.py`, `tests/entrypoints/pooling/embed/test_protocol.py`, `tests/models/language/pooling/test_truncation_control.py` _+3 more__
- **2026-10-09** [`75e3b17c05`](https://github.com/vllm-project/vllm/commit/75e3b17c05) [#60841](https://github.com/vllm-project/vllm/pull/60841)
  [Frontend] Add cache salt support to generative scoring (#60841)
  _Files: `docs/serving/online_serving/generative_scoring.md`, `docs/usage/security.md`, `tests/entrypoints/generate/generative_scoring/test_generative_scoring.py`, `tests/entrypoints/unit_tests/test_non_object_body_validation.py` _+1 more__
- **2026-10-09** [`18c19eaf23`](https://github.com/vllm-project/vllm/commit/18c19eaf23) [#60786](https://github.com/vllm-project/vllm/pull/60786)
  [Frontend] Add cache salt and tracing to structured decisions (#60786)
  _Files: `docs/serving/online_serving/structured_decisions.md`, `docs/usage/security.md`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `tests/entrypoints/unit_tests/test_non_object_body_validation.py` _+3 more__
- **2026-10-09** [`8a03ccf7b3`](https://github.com/vllm-project/vllm/commit/8a03ccf7b3) [#60728](https://github.com/vllm-project/vllm/pull/60728)
  [Frontend] Add return_mm_kwargs to render requests (#60728)
  _Files: `docs/serving/online_serving/renderer.md`, `tests/entrypoints/scale_out/token_in_token_out/test_mm_serde.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/openai/chat_completion/protocol.py` _+4 more__
- **2026-10-09** [`8cbd5d0300`](https://github.com/vllm-project/vllm/commit/8cbd5d0300) [#60696](https://github.com/vllm-project/vllm/pull/60696)
  [Frontend] structured decisions: noul and score question types (#60696)
  _Files: `docs/serving/online_serving/structured_decisions.md`, `tests/entrypoints/generate/structured_decisions/test_question_types.py`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `tests/entrypoints/generate/structured_decisions/test_structured_decisions_e2e.py` _+2 more__
- **2026-10-09** [`fa312090cb`](https://github.com/vllm-project/vllm/commit/fa312090cb) [#60723](https://github.com/vllm-project/vllm/pull/60723)
  [Frontend] Accept each connection on the least loaded API worker (#60723)
  _Files: `tests/entrypoints/launchers/test_balanced_accepts.py`, `vllm/entrypoints/launchers/api_server/entry.py`, `vllm/entrypoints/launchers/launcher.py`, `vllm/v1/utils.py`_
- **2026-10-09** [`112a282915`](https://github.com/vllm-project/vllm/commit/112a282915) [#60668](https://github.com/vllm-project/vllm/pull/60668)
  [Bugfix][Frontend] Keep streamed completion text_offset in step with tokens (#60668)
  _Files: `tests/entrypoints/openai/completion/test_completion_text_offset.py`, `vllm/entrypoints/openai/completion/serving.py`_
- **2026-10-09** [`51ef239768`](https://github.com/vllm-project/vllm/commit/51ef239768) [#59836](https://github.com/vllm-project/vllm/pull/59836)
  [Rust Frontend] Carry reasoning controls over gRPC (#59836)
  _Files: `rust/Cargo.lock`, `rust/proto/Cargo.toml`, `rust/proto/README.md`, `rust/proto/inference.proto` _+1 more__
- **2026-10-08** [`2ddde19e8e`](https://github.com/vllm-project/vllm/commit/2ddde19e8e) [#48084](https://github.com/vllm-project/vllm/pull/48084)
  [Frontend] Support min_p in the Responses API (#48084)
  _Files: `docs/serving/online_serving/openai_compatible_server.md`, `tests/benchmarks/test_responses_request_func.py`, `tests/entrypoints/openai/responses/test_sampling_params.py`, `vllm/benchmarks/serve.py` _+1 more__
- **2026-10-08** [`ae9adec905`](https://github.com/vllm-project/vllm/commit/ae9adec905) [#60677](https://github.com/vllm-project/vllm/pull/60677)
  [Frontend] Expose /v1/systemone without an opt-in flag (#60677)
  _Files: `docs/serving/online_serving/structured_decisions.md`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `tests/entrypoints/generate/structured_decisions/test_structured_decisions_e2e.py`, `tests/entrypoints/openai/test_openai_schema.py` _+4 more__
- **2026-10-08** [`56e6da2c47`](https://github.com/vllm-project/vllm/commit/56e6da2c47) [#56592](https://github.com/vllm-project/vllm/pull/56592)
  [Bugfix][Frontend] Honor stop_token_ids on the Responses API (#56592)
  _Files: `tests/entrypoints/openai/responses/test_sampling_params.py`, `vllm/entrypoints/openai/responses/protocol.py`_
- **2026-10-08** [`705e124c05`](https://github.com/vllm-project/vllm/commit/705e124c05) [#60651](https://github.com/vllm-project/vllm/pull/60651)
  [Bugfix] Followup to #59299: preserve Unicode in structured decision state prompts (#60651)
  _Files: `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `vllm/entrypoints/generate/structured_decisions/serving.py`_
- **2026-10-08** [`d33872dfeb`](https://github.com/vllm-project/vllm/commit/d33872dfeb) [#59299](https://github.com/vllm-project/vllm/pull/59299)
  [Feat] Structured decisions endpoint (`/v1/systemone`) (#59299)
  _Files: `docs/serving/online_serving/README.md`, `docs/serving/online_serving/structured_decisions.md`, `docs/usage/security.md`, `tests/entrypoints/generate/structured_decisions/__init__.py` _+13 more__
- **2026-10-08** [`b49c921a27`](https://github.com/vllm-project/vllm/commit/b49c921a27) [#60286](https://github.com/vllm-project/vllm/pull/60286)
  [Bugfix][Rust Frontend] Always include token_ids in completion stream choices (#60286)
  _Files: `rust/src/server/src/routes/openai/completions.rs`_
- **2026-10-08** [`0f112d1800`](https://github.com/vllm-project/vllm/commit/0f112d1800) [#47696](https://github.com/vllm-project/vllm/pull/47696)
  [Bugfix][Pooling] Preserve cache_salt for chunked embeddings (#47696)
  _Files: `vllm/entrypoints/pooling/embed/io_processor.py`_
- **2026-10-08** [`29ae81fe83`](https://github.com/vllm-project/vllm/commit/29ae81fe83) [#60115](https://github.com/vllm-project/vllm/pull/60115)
  [Rust Frontend] Preserve explicit zero sampling values in gRPC requests (#60115)
  _Files: `rust/proto/inference.proto`, `rust/src/server/src/grpc/convert.rs`, `rust/src/server/src/grpc/tests.rs`_
- **2026-10-08** [`3722645539`](https://github.com/vllm-project/vllm/commit/3722645539) [#60507](https://github.com/vllm-project/vllm/pull/60507)
  [Bugfix][Frontend] Accept successful 2xx responses for batch output uploads (#60507)
  _Files: `tests/entrypoints/launchers/test_run_batch.py`, `vllm/entrypoints/launchers/run_batch.py`_
- **2026-10-08** [`2dd887426e`](https://github.com/vllm-project/vllm/commit/2dd887426e) [#59959](https://github.com/vllm-project/vllm/pull/59959)
  [Bugfix][Frontend] Do not modify caller params in LLM.score() (#59959)
  _Files: `tests/entrypoints/pooling/test_io_processor.py`, `vllm/entrypoints/pooling/offline.py`_
- **2026-10-08** [`1995c0fcd0`](https://github.com/vllm-project/vllm/commit/1995c0fcd0) [#59180](https://github.com/vllm-project/vllm/pull/59180)
  [Bugfix][Frontend] Apply output_config and thinking in Anthropic count_tokens (#59180)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-10-08** [`ed825aafc0`](https://github.com/vllm-project/vllm/commit/ed825aafc0) [#59723](https://github.com/vllm-project/vllm/pull/59723)
  [Bugfix][Frontend] Fix Responses namespace aliases in named tool calling (#59723)
  _Files: `docs/features/tool_calling.md`, `tests/tool_use/test_tool_choice_required.py`, `vllm/entrypoints/openai/responses/protocol.py`, `vllm/tool_parsers/utils.py`_
- **2026-10-07** [`14e3902d51`](https://github.com/vllm-project/vllm/commit/14e3902d51) [#59837](https://github.com/vllm-project/vllm/pull/59837)
  [Frontend][Rust] Add gRPC forbidden token sequences and cache usage (#59837)
  _Files: `rust/proto/inference.proto`, `rust/src/server/src/grpc/convert.rs`, `rust/src/server/src/grpc/tests.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs` _+4 more__
- **2026-10-07** [`db6e3cd8c4`](https://github.com/vllm-project/vllm/commit/db6e3cd8c4) [#60310](https://github.com/vllm-project/vllm/pull/60310)
  [Bugfix][Frontend] Log the full request body when max_log_len is unset (#60310)
  _Files: `tests/entrypoints/serve/utils/test_request_logger.py`, `vllm/entrypoints/serve/utils/request_logger.py`_
- **2026-10-07** [`d77cf81156`](https://github.com/vllm-project/vllm/commit/d77cf81156) [#60307](https://github.com/vllm-project/vllm/pull/60307)
  [Bugfix][Frontend] Honor default penalties in batch chat completions (#60307)
  _Files: `tests/entrypoints/openai/test_penalty_default_resolution.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`_
- **2026-10-06** [`7b665f7a58`](https://github.com/vllm-project/vllm/commit/7b665f7a58) [#58181](https://github.com/vllm-project/vllm/pull/58181)
  [Frontend] Integer token IDs for generate output logprobs (GenerateLogProbs) (#58181)
  _Files: `docs/serving/online_serving/derenderer.md`, `docs/serving/online_serving/renderer.md`, `docs/serving/online_serving/token_in_token_out.md`, `rust/src/server/src/routes/inference/generate.rs` _+14 more__
- **2026-10-06** [`1a86733c7b`](https://github.com/vllm-project/vllm/commit/1a86733c7b) [#57786](https://github.com/vllm-project/vllm/pull/57786)
  [Docs] Add model recipes skill (#57786)
  _Files: `.agents/skills/model-recipes/SKILL.md`, `.agents/skills/model-recipes/agents/openai.yaml`, `.agents/skills/model-recipes/scripts/read_recipe.sh`, `.claude/skills/model-recipes`_
- **2026-10-05** [`4a705c7b54`](https://github.com/vllm-project/vllm/commit/4a705c7b54) [#47838](https://github.com/vllm-project/vllm/pull/47838)
  [Bugfix][Frontend] Preserve logprobs when top_logprobs is null (#47838)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat.py`, `tests/entrypoints/openai/responses/test_sampling_params.py`, `vllm/entrypoints/generate/base/protocol.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py` _+3 more__

## MoE / Expert Parallel  (35 commits)

- **2026-10-12** [`ffec221276`](https://github.com/vllm-project/vllm/commit/ffec221276) [#61041](https://github.com/vllm-project/vllm/pull/61041)
  [Bugfix][DSv4.1] Match decoder-replay input_ids dtype for FlashInfer MegaMoE (#61041)
  _Files: `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`_
- **2026-10-12** [`716961cf1f`](https://github.com/vllm-project/vllm/commit/716961cf1f) [#59900](https://github.com/vllm-project/vllm/pull/59900)
  [Bugfix] Drop enable_in_kernel_fc2_reduce from FlashInfer CuteDSL MegaMoE config (#59900)
  _Files: `tests/kernels/moe/test_flashinfer_moe_ep.py`, `vllm/model_executor/layers/fused_moe/flashinfer_moe_ep.py`_
- **2026-10-12** [`a281ad32f0`](https://github.com/vllm-project/vllm/commit/a281ad32f0) [#57549](https://github.com/vllm-project/vllm/pull/57549)
  [EPLB] Add EPLB support to dspark draft models (DeepSeekV4) (#57549)
  _Files: `tests/distributed/test_eplb_spec_decode.py`, `tests/models/test_deepseek_v4_mega_moe.py`, `tests/models/test_dspark_mla.py`, `tests/v1/worker/test_dspark_utils.py` _+8 more__
- **2026-10-12** [`b3ee560ae8`](https://github.com/vllm-project/vllm/commit/b3ee560ae8) [#59042](https://github.com/vllm-project/vllm/pull/59042)
  [Bugfix][MoE] Apply expert_map remapping for CUTLASS FP4 MOE expert parallel (#59042)
  _Files: `tests/kernels/moe/test_cutlass_moe.py`, `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py` _+2 more__
- **2026-10-12** [`092c35dd15`](https://github.com/vllm-project/vllm/commit/092c35dd15) [#61064](https://github.com/vllm-project/vllm/pull/61064)
  [Model] Support Cloudflare/clef-omni on /v1/systemone (#61064)
  _Files: `docs/serving/online_serving/structured_decisions.md`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `tests/model_executor/model_loader/test_filter_duplicate_safetensors.py`, `tests/models/multimodal/pooling/test_clef_omni.py` _+16 more__
- **2026-10-12** [`7900d2eabc`](https://github.com/vllm-project/vllm/commit/7900d2eabc) [#60726](https://github.com/vllm-project/vllm/pull/60726)
  [Test] Accept tied tokens at the k-th value in the Triton top-k test (#60726)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`_
- **2026-10-12** [`03091e28b8`](https://github.com/vllm-project/vllm/commit/03091e28b8) [#59026](https://github.com/vllm-project/vllm/pull/59026)
  [Bugfix] Read Ling quantization_config from top-level config for Bailing V3 VL (#59026)
  _Files: `vllm/model_executor/models/bailing_moe_v3.py`_
- **2026-10-10** [`3709632ff2`](https://github.com/vllm-project/vllm/commit/3709632ff2) [#60120](https://github.com/vllm-project/vllm/pull/60120)
  [Refactor] Remove dead code multiple places (#60120)
  _Files: `vllm/_custom_ops.py`, `vllm/lora/model_manager.py`, `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`, `vllm/model_executor/models/bert.py` _+8 more__
- **2026-10-10** [`bf16c9c139`](https://github.com/vllm-project/vllm/commit/bf16c9c139) [#60187](https://github.com/vllm-project/vllm/pull/60187)
  [Bugfix][Model] K-EXAONE: restore loading of pre-2.0 configs and apply RoPE to the MTP layer (#60187)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/exaone_moe.py`, `vllm/model_executor/models/registry.py`_
- **2026-10-10** [`364bc81a9e`](https://github.com/vllm-project/vllm/commit/364bc81a9e) [#60812](https://github.com/vllm-project/vllm/pull/60812)
  [Bugfix][LoRA] Fix GPT-OSS gate/up interleaving with mixed MoE LoRA formats (#60812)
  _Files: `tests/lora/test_gptoss_tp.py`, `vllm/model_executor/layers/fused_moe/experts/lora_experts_mixin.py`_
- **2026-10-10** [`02aa10539f`](https://github.com/vllm-project/vllm/commit/02aa10539f) [#57108](https://github.com/vllm-project/vllm/pull/57108)
  [Bugfix][ModelLoader] Make enable_weights_track check quantized layers (#57108)
  _Files: `tests/model_executor/model_loader/test_registry.py`, `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`, `vllm/model_executor/model_loader/default_loader.py`_
- **2026-10-09** [`0cc0460870`](https://github.com/vllm-project/vllm/commit/0cc0460870) [#57787](https://github.com/vllm-project/vllm/pull/57787)
  [XPU]Fix the accuracy issue when meet topk_ids=-1 on DP+EP scenarios (#57787)
  _Files: `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`_
- **2026-10-09** [`201e537d98`](https://github.com/vllm-project/vllm/commit/201e537d98) [#59924](https://github.com/vllm-project/vllm/pull/59924)
  [Bugfix][LoRA] Validate incompatible MoE adapter formats (#59924)
  _Files: `docs/features/lora.md`, `tests/lora/test_lora_manager.py`, `vllm/lora/model_manager.py`, `vllm/lora/worker_manager.py`_
- **2026-10-08** [`e3a29aa9b3`](https://github.com/vllm-project/vllm/commit/e3a29aa9b3) [#60447](https://github.com/vllm-project/vllm/pull/60447)
  [Bugfix][MoE] Size the permute scratch from its inputs (#60447)
  _Files: `benchmarks/kernels/benchmark_moe_permute_unpermute.py`, `tests/kernels/moe/test_moe.py`, `tests/kernels/moe/test_moe_permute_unpermute.py`, `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py` _+3 more__
- **2026-10-08** [`fc494822ea`](https://github.com/vllm-project/vllm/commit/fc494822ea) [#58878](https://github.com/vllm-project/vllm/pull/58878)
  [Test][Quantization] Gate CUTLASS W4A8 kernel tests to SM90 (#58878)
  _Files: `tests/kernels/quantization/test_cutlass_w4a8.py`, `tests/kernels/quantization/test_cutlass_w4a8_moe.py`_
- **2026-10-08** [`30c7405890`](https://github.com/vllm-project/vllm/commit/30c7405890) [#60079](https://github.com/vllm-project/vllm/pull/60079)
  [MoE] MXFP4 oracle: add CUTLASS W4A4 backend and BF16 activation fallback (#60079)
  _Files: `tests/kernels/moe/test_cutlass_moe.py`, `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-10-08** [`fd0216d3b5`](https://github.com/vllm-project/vllm/commit/fd0216d3b5) [#60221](https://github.com/vllm-project/vllm/pull/60221)
  [Bugfix][CPU] Fix fused Gumbel-max wrapping-window bias (#60221)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `.buildkite/test_areas/kernels.yaml`, `csrc/cpu/sampling_kernels.cpp` _+2 more__
- **2026-10-08** [`e58f8dde7f`](https://github.com/vllm-project/vllm/commit/e58f8dde7f) [#60098](https://github.com/vllm-project/vllm/pull/60098)
  [Bugfix] Use FusedMoEWithLoRA for shared MoE LoRAs on 3D models (#60098)
  _Files: `vllm/config/lora.py`, `vllm/lora/model_manager.py`_
- **2026-10-08** [`81198e97ba`](https://github.com/vllm-project/vllm/commit/81198e97ba) [#58053](https://github.com/vllm-project/vllm/pull/58053)
  [Refactor] Abstract DeepGemm MegaMOE backend (#58053)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/model_executor/layers/fused_moe/deep_gemm_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/ops/prepare_megamoe.py` _+1 more__
- **2026-10-07** [`f38c6778ce`](https://github.com/vllm-project/vllm/commit/f38c6778ce) [#56740](https://github.com/vllm-project/vllm/pull/56740)
  [quantization] Add per-token NVFP4 quantization MoE support for ReLU2 (#56740)
  _Files: `tests/evals/gsm8k/configs/Nemotron-3-Super-120B-A12B-NVFP4-per-token.yaml`, `tests/evals/gsm8k/configs/models-blackwell-ep.txt`, `tests/kernels/moe/test_trtllm_nvfp4_moe.py`, `tests/model_executor/model_loader/test_weight_cache.py` _+14 more__
- **2026-10-07** [`a982c81e3e`](https://github.com/vllm-project/vllm/commit/a982c81e3e) [#60281](https://github.com/vllm-project/vllm/pull/60281)
  [Bugfix] Limit GlmMoeDsaForCausalLM fp8 KV cache default to SM100 (#60281)
  _Files: `vllm/model_executor/models/config.py`_
- **2026-10-07** [`f7f62d1916`](https://github.com/vllm-project/vllm/commit/f7f62d1916) [#53065](https://github.com/vllm-project/vllm/pull/53065)
  [XPU][MoE] Tune Triton fused MoE for Intel XPU (#53065)
  _Files: `benchmarks/kernels/benchmark_moe.py`, `vllm/model_executor/layers/fused_moe/configs/E=128,N=384,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics.json`, `vllm/model_executor/layers/fused_moe/configs/E=64,N=1024,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics.json`, `vllm/model_executor/layers/fused_moe/configs/E=64,N=512,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics.json`_
- **2026-10-07** [`6b75dfb8a1`](https://github.com/vllm-project/vllm/commit/6b75dfb8a1) [#60242](https://github.com/vllm-project/vllm/pull/60242)
  [Misc] Report a missing DeepSelect extension only when it is requested (#60242)
  _Files: `vllm/model_executor/layers/indexer_topk.py`_
- **2026-10-07** [`283d76d56a`](https://github.com/vllm-project/vllm/commit/283d76d56a) [#58373](https://github.com/vllm-project/vllm/pull/58373)
  [Bugfix] Widen ep_gather output offset to int64 (#58373)
  _Files: `tests/kernels/moe/test_deepgemm.py`, `vllm/model_executor/layers/fused_moe/deep_gemm_utils.py`_
- **2026-10-06** [`5ab4e4445b`](https://github.com/vllm-project/vllm/commit/5ab4e4445b) [#59128](https://github.com/vllm-project/vllm/pull/59128)
  [Perf][MoE] Skip padded work in block-FP8 DeepGEMM experts (#59128)
  _Files: `tests/kernels/moe/test_deepgemm.py`, `tests/kernels/moe/test_silu_mul_per_token_group_quant_fp8_colmajor.py`, `vllm/model_executor/layers/fused_moe/deep_gemm_utils.py`, `vllm/model_executor/layers/fused_moe/experts/deep_gemm_moe.py` _+1 more__
- **2026-10-06** [`d1f3d8b870`](https://github.com/vllm-project/vllm/commit/d1f3d8b870) [#56997](https://github.com/vllm-project/vllm/pull/56997)
  [Quantization] Prefer Humming before Marlin backends on SM90 (#56997)
  _Files: `tests/kernels/quantization/test_scaled_mm_kernel_selection.py`, `tests/quantization/test_modelopt.py`, `tests/quantization/test_online.py`, `vllm/model_executor/kernels/linear/__init__.py` _+9 more__
- **2026-10-06** [`f8d92cae41`](https://github.com/vllm-project/vllm/commit/f8d92cae41) [#55684](https://github.com/vllm-project/vllm/pull/55684)
  [Quantization] Layer re-quantization for linear layers through online quantization API (MXFP8 -> FP8 PTPC showcase) (#55684)
  _Files: `docs/features/quantization/online.md`, `tests/quantization/test_online.py`, `vllm/model_executor/layers/quantization/base_config.py`, `vllm/model_executor/layers/quantization/modelopt.py` _+8 more__
- **2026-10-06** [`4a99ca40d6`](https://github.com/vllm-project/vllm/commit/4a99ca40d6) [#49194](https://github.com/vllm-project/vllm/pull/49194)
  [Perf][MoE] Eliminate staging from NCCL symmetric reduce-scatter (#49194)
  _Files: `tests/distributed/test_mnnvl_alltoall.py`, `tests/distributed/test_nccl_symm_mem.py`, `vllm/distributed/device_communicators/all2all.py`, `vllm/distributed/device_communicators/base_device_communicator.py` _+4 more__
- **2026-10-06** [`40c86ae1ce`](https://github.com/vllm-project/vllm/commit/40c86ae1ce) [#58877](https://github.com/vllm-project/vllm/pull/58877)
  [Kernel] Enable OAI Triton MXFP4 MoE on SM12x (#58877)
  _Files: `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`_
- **2026-10-06** [`8c417a2dae`](https://github.com/vllm-project/vllm/commit/8c417a2dae) [#59842](https://github.com/vllm-project/vllm/pull/59842)
  [Bugfix][Model] Fix Qwen3-Omni interleaved M-RoPE boundary positions (#59842)
  _Files: `tests/model_executor/test_qwen3_omni_mrope.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`_
- **2026-10-05** [`6dd813e0b7`](https://github.com/vllm-project/vllm/commit/6dd813e0b7) [#59571](https://github.com/vllm-project/vllm/pull/59571)
  [Bugfix][MoE] Allow MiniMax2 routing in TRTLLM BF16 monolithic backend (#59571)
  _Files: `tests/kernels/moe/test_unquantized_backend_selection.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`_
- **2026-10-05** [`d0d6e5f3a2`](https://github.com/vllm-project/vllm/commit/d0d6e5f3a2) [#59975](https://github.com/vllm-project/vllm/pull/59975)
  [Bugfix] Fix Mamba page size AssertionError with spec decoding on GraniteMoeHybrid, FalconH1 and Zamba2 (#59975)
  _Files: `tests/v1/attention/test_attention_backends_selection.py`, `vllm/model_executor/models/falcon_h1.py`, `vllm/model_executor/models/granitemoehybrid.py`, `vllm/model_executor/models/zamba2.py`_
- **2026-10-05** [`51eeb0c58f`](https://github.com/vllm-project/vllm/commit/51eeb0c58f) [#59031](https://github.com/vllm-project/vllm/pull/59031)
  [Bugfix] Load stacked expert weights for non-gated MoE (#59031)
  _Files: `tests/kernels/moe/test_moe_weight_loading_padded.py`, `vllm/lora/utils.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py` _+2 more__
- **2026-10-05** [`e3af5bf3ce`](https://github.com/vllm-project/vllm/commit/e3af5bf3ce) [#60017](https://github.com/vllm-project/vllm/pull/60017)
  [LoRA] Code cleanup (#60017)
  _Files: `vllm/config/lora.py`, `vllm/lora/model_manager.py`, `vllm/model_executor/models/bailing_moe_v3_vl.py`, `vllm/model_executor/models/cohere_compass.py` _+3 more__
- **2026-10-05** [`4a30c4cad0`](https://github.com/vllm-project/vllm/commit/4a30c4cad0) [#59927](https://github.com/vllm-project/vllm/pull/59927)
  [Model][DeepSeek-V4] Make MegaMoE shared-expert finalize independent of linear post-load order (#59927)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`_

## Scheduler / Engine  (30 commits)

- **2026-10-12** [`a7b7bc1fbe`](https://github.com/vllm-project/vllm/commit/a7b7bc1fbe) [#58715](https://github.com/vllm-project/vllm/pull/58715)
  [Metrics] Count finished requests by watermark status (#58715)
  _Files: `docs/features/watermarking.md`, `tests/v1/engine/test_output_processor.py`, `tests/v1/metrics/test_histogram_buckets.py`, `tests/watermarking/test_watermarking_e2e.py` _+3 more__
- **2026-10-12** [`32b05addc1`](https://github.com/vllm-project/vllm/commit/32b05addc1) [#60249](https://github.com/vllm-project/vllm/pull/60249)
  [Bugfix][Rust Frontend] Restore DP wave delivery after XPUB reconnects (#60249)
  _Files: `rust/src/engine-core-client/src/coordinator/bootstrap.rs`, `rust/src/engine-core-client/src/coordinator/inproc.rs`, `rust/src/engine-core-client/src/tests/client.rs`_
- **2026-10-12** [`3b9e462774`](https://github.com/vllm-project/vllm/commit/3b9e462774) [#59631](https://github.com/vllm-project/vllm/pull/59631)
  [Bugfix][Rust Frontend] Correct DP routing after request removal (#59631)
  _Files: `rust/src/engine-core-client/src/client/state.rs`_
- **2026-10-12** [`ee8f7ea449`](https://github.com/vllm-project/vllm/commit/ee8f7ea449) [#60858](https://github.com/vllm-project/vllm/pull/60858)
  [CI] Enroll a fourth batch of five steps in automatic sharding (#60858)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/misc.yaml`_
- **2026-10-12** [`83773ecdf3`](https://github.com/vllm-project/vllm/commit/83773ecdf3) [#57322](https://github.com/vllm-project/vllm/pull/57322)
  [Frontend] Support CustomToolCall in the non-Harmony Responses API (#57322)
  _Files: `tests/entrypoints/openai/responses/test_protocol.py`, `tests/entrypoints/openai/responses/test_responses_utils.py`, `tests/entrypoints/openai/responses/test_streaming_events.py`, `tests/tool_parsers/test_gemma4_tool_parser.py` _+18 more__
- **2026-10-12** [`99b44c7a42`](https://github.com/vllm-project/vllm/commit/99b44c7a42) [#55812](https://github.com/vllm-project/vllm/pull/55812)
  [Metrics] Add admission rejection metrics (#55812)
  _Files: `docs/design/metrics.md`, `tests/entrypoints/serve/instrumentator/test_metrics.py`, `tests/v1/engine/test_admission_control.py`, `vllm/v1/engine/async_llm.py` _+1 more__
- **2026-10-12** [`4163a80142`](https://github.com/vllm-project/vllm/commit/4163a80142) [#61070](https://github.com/vllm-project/vllm/pull/61070)
  [Rust Frontend] Return weight-version spans on final outputs (#61070)
  _Files: `docs/serving/online_serving/token_in_token_out.md`, `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/client/output_channel.rs`, `rust/src/engine-core-client/src/client/state.rs` _+8 more__
- **2026-10-11** [`c85616efc6`](https://github.com/vllm-project/vllm/commit/c85616efc6) [#58674](https://github.com/vllm-project/vllm/pull/58674)
  [Model] Support MiniCPM-V 4.7 (#58674)
  _Files: `docs/models/supported_models.md`, `tests/model_executor/test_minicpmv.py`, `tests/model_executor/test_minicpmv4_7.py`, `tests/models/registry.py` _+9 more__
- **2026-10-11** [`b89852aad0`](https://github.com/vllm-project/vllm/commit/b89852aad0) [#59582](https://github.com/vllm-project/vllm/pull/59582)
  [RL][Frontend] Return token-level weight-version spans on final outputs (#59582)
  _Files: `docs/serving/online_serving/token_in_token_out.md`, `docs/training/async_rl.md`, `examples/rl/rlhf_async_new_apis.py`, `rust/src/engine-core-client/src/protocol/output.rs` _+10 more__
- **2026-10-10** [`276fbcff27`](https://github.com/vllm-project/vllm/commit/276fbcff27) [#60923](https://github.com/vllm-project/vllm/pull/60923)
  [Deprecation] Remove scheduled deprecated items (#60923)
  _Files: `rust/src/server/src/routes/pause.rs`, `vllm/benchmarks/throughput.py`, `vllm/engine/protocol.py`, `vllm/entrypoints/pooling/pooling/io_processor.py` _+3 more__
- **2026-10-10** [`fa5cfd48d5`](https://github.com/vllm-project/vllm/commit/fa5cfd48d5) [#60828](https://github.com/vllm-project/vllm/pull/60828)
  [Refactor] Deduplicate trace header handling in BaseServing (#60828)
  _Files: `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `vllm/entrypoints/generate/base/serving.py`, `vllm/entrypoints/generate/generative_scoring/serving.py`, `vllm/entrypoints/generate/structured_decisions/serving.py` _+3 more__
- **2026-10-09** [`35e920d671`](https://github.com/vllm-project/vllm/commit/35e920d671) [#60589](https://github.com/vllm-project/vllm/pull/60589)
  [Rust Frontend] Support `--stream-interval` and per-request `stream_interval` (#60589)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/engine-core-client/examples/external_engine_logprobs.rs` _+21 more__
- **2026-10-09** [`04462732a4`](https://github.com/vllm-project/vllm/commit/04462732a4) [#60714](https://github.com/vllm-project/vllm/pull/60714)
  [Bugfix] Reject max_num_scheduled_tokens=0 at config time instead of hanging (#60714)
  _Files: `tests/test_config.py`, `vllm/config/scheduler.py`_
- **2026-10-09** [`ad8a6065f4`](https://github.com/vllm-project/vllm/commit/ad8a6065f4) [#52298](https://github.com/vllm-project/vllm/pull/52298)
  [Bugfix] Validate guidance tokenizer compatibility before EngineCore (#52298)
  _Files: `tests/v1/structured_output/test_validation.py`, `vllm/sampling_params.py`, `vllm/v1/structured_output/backend_guidance.py`_
- **2026-10-09** [`5dc9bcd8cd`](https://github.com/vllm-project/vllm/commit/5dc9bcd8cd) [#60546](https://github.com/vllm-project/vllm/pull/60546)
  [Rust Frontend] Pass reasoning controls through render -> generate (#60546)
  _Files: `rust/src/engine-core-client/src/protocol/request.rs`, `rust/src/server/src/routes/inference/generate/convert.rs`, `rust/src/server/src/routes/inference/generate/types.rs`, `rust/src/server/src/routes/render.rs` _+1 more__
- **2026-10-09** [`9a585c62aa`](https://github.com/vllm-project/vllm/commit/9a585c62aa) [#60588](https://github.com/vllm-project/vllm/pull/60588)
  [Rust Frontend] Box rarely-set fields of per-token output types (#60588)
  _Files: `rust/src/chat/src/event.rs`, `rust/src/chat/src/output/mod.rs`, `rust/src/chat/src/output/structured.rs`, `rust/src/chat/src/stream.rs` _+12 more__
- **2026-10-09** [`a6b39f0262`](https://github.com/vllm-project/vllm/commit/a6b39f0262) [#57757](https://github.com/vllm-project/vllm/pull/57757)
  [Bugfix] Clean up async client sockets after event loop closure (#57757)
  _Files: `vllm/v1/engine/core_client.py`_
- **2026-10-09** [`196483e25b`](https://github.com/vllm-project/vllm/commit/196483e25b) [#57307](https://github.com/vllm-project/vllm/pull/57307)
  [Tools] Recipes sweep workflow (#57307)
  _Files: `tools/recipes/README.md`, `tools/recipes/RUNTIME_TUNING.md`, `tools/recipes/SWEEP_TUNING.md`, `tools/recipes/VISUALIZATION.md` _+13 more__
- **2026-10-09** [`b8bd335754`](https://github.com/vllm-project/vllm/commit/b8bd335754) [#60662](https://github.com/vllm-project/vllm/pull/60662)
  [CI] Enroll five more steps in automatic sharding (#60662)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/pytorch.yaml`_
- **2026-10-08** [`bab0ac61f8`](https://github.com/vllm-project/vllm/commit/bab0ac61f8) [#59263](https://github.com/vllm-project/vllm/pull/59263)
  [Bugfix][Frontend] Forward the reasoning wiring to the engine for batch chat completions (#59263)
  _Files: `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py`, `vllm/entrypoints/openai/chat_completion/serving.py`_
- **2026-10-08** [`c4a5ff5c18`](https://github.com/vllm-project/vllm/commit/c4a5ff5c18) [#52299](https://github.com/vllm-project/vllm/pull/52299)
  [Frontend] shutdown engine core and its sub processes asap when initializing (#52299)
  _Files: `tests/v1/engine/test_engine_core_shutdown_signal.py`, `vllm/v1/engine/core.py`_
- **2026-10-08** [`194da61de1`](https://github.com/vllm-project/vllm/commit/194da61de1) [#49053](https://github.com/vllm-project/vllm/pull/49053)
  [Bugfix] Reject negative --device-ids indices instead of selecting the wrong device (#49053)
  _Files: `tests/engine/test_arg_utils.py`, `vllm/engine/arg_utils.py`_
- **2026-10-08** [`7816afdb25`](https://github.com/vllm-project/vllm/commit/7816afdb25) [#60572](https://github.com/vllm-project/vllm/pull/60572)
  [Bugfix][Core] Drain async KV loads in pause(mode="wait"), and pause the drain test only once a request is in flight (#60572)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/distributed/test_async_llm_dp.py`, `vllm/v1/core/sched/interface.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-08** [`f226af0e11`](https://github.com/vllm-project/vllm/commit/f226af0e11) [#54113](https://github.com/vllm-project/vllm/pull/54113)
  [Bugfix] Eliminate frontend ZMQ port TOCTOU with inherited listeners (#54113)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+14 more__
- **2026-10-07** [`e6fc81bc78`](https://github.com/vllm-project/vllm/commit/e6fc81bc78) [#48039](https://github.com/vllm-project/vllm/pull/48039)
  [Bugfix][Scheduler] Let pooling chunked prefill use full context (#48039)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-06** [`4516896626`](https://github.com/vllm-project/vllm/commit/4516896626) [#60241](https://github.com/vllm-project/vllm/pull/60241)
  [CI/Build] Warm the DP engines before measuring load balance in test_load (#60241)
  _Files: `tests/v1/distributed/test_async_llm_dp.py`_
- **2026-10-06** [`09e0ce3d82`](https://github.com/vllm-project/vllm/commit/09e0ce3d82) [#54835](https://github.com/vllm-project/vllm/pull/54835)
  [Bugfix][Frontend] Apply model-default reasoning parser in GPU-less render server (#54835)
  _Files: `tests/entrypoints/launchers/render/__init__.py`, `tests/entrypoints/launchers/render/test_app_state.py`, `tests/entrypoints/scale_out/derender/test_derender.py`, `vllm/engine/arg_utils.py` _+2 more__
- **2026-10-06** [`2b32d9ac6a`](https://github.com/vllm-project/vllm/commit/2b32d9ac6a) [#59103](https://github.com/vllm-project/vllm/pull/59103)
  [Bugfix][Core] Drop stale block hashes when a session truncates tokens (#59103)
  _Files: `tests/v1/streaming_input/test_scheduler_streaming.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-05** [`c32495d58f`](https://github.com/vllm-project/vllm/commit/c32495d58f) [#56801](https://github.com/vllm-project/vllm/pull/56801)
  [watermark] compatibility validation (#56801)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `docs/features/watermarking.md`, `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/cohere/test_serving_conversion.py` _+41 more__
- **2026-10-05** [`d09ff77637`](https://github.com/vllm-project/vllm/commit/d09ff77637) [#59788](https://github.com/vllm-project/vllm/pull/59788)
  [Bugfix] Give each data-parallel engine its own global RNG streams (#59788)
  _Files: `tests/utils_/test_torch_utils.py`, `vllm/utils/torch_utils.py`, `vllm/v1/worker/cpu_worker.py`, `vllm/v1/worker/gpu_worker.py`_

## Disaggregation / PD  (28 commits)

- **2026-10-12** [`5b0b8f251e`](https://github.com/vllm-project/vllm/commit/5b0b8f251e) [#60941](https://github.com/vllm-project/vllm/pull/60941)
  [Bugfix][HiSparse] Fix TP group hang on steps without scheduled tokens (#60941)
  _Files: `tests/v1/kv_connector/unit/test_hisparse_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/hisparse/worker.py`_
- **2026-10-12** [`258b97ff6b`](https://github.com/vllm-project/vllm/commit/258b97ff6b) [#57904](https://github.com/vllm-project/vllm/pull/57904)
  [Bugfix][EC Connector] Size transfers by measured encoder output widths (#57904)
  _Files: `docs/features/ec_cpu_connector.md`, `tests/v1/ec_connector/unit/cpu/scheduler/test_scheduler.py`, `tests/v1/ec_connector/unit/cpu/test_ec_shared_region.py`, `tests/v1/ec_connector/unit/cpu/worker/test_worker.py` _+14 more__
- **2026-10-12** [`74f4404f58`](https://github.com/vllm-project/vllm/commit/74f4404f58) [#61000](https://github.com/vllm-project/vllm/pull/61000)
  [Bugfix][Distributed] Own SHM out-of-band buffers before releasing read slots (#61000)
  _Files: `tests/distributed/test_shm_broadcast.py`, `vllm/distributed/device_communicators/shm_broadcast.py`_
- **2026-10-11** [`bd5bbce6e4`](https://github.com/vllm-project/vllm/commit/bd5bbce6e4) [#61060](https://github.com/vllm-project/vllm/pull/61060)
  [RL] Release weight-transfer communicators without stopping inference (#61060)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/tests.rs`, `rust/src/server/src/routes/weight_transfer.rs` _+18 more__
- **2026-10-11** [`3c062d391d`](https://github.com/vllm-project/vllm/commit/3c062d391d) [#52235](https://github.com/vllm-project/vllm/pull/52235)
  [Bugfix] Support 0-dim tensors in packed weight transfer (#52235)
  _Files: `tests/distributed/test_packed_tensor.py`, `vllm/distributed/weight_transfer/packed_tensor.py`_
- **2026-10-09** [`04b02fc8a5`](https://github.com/vllm-project/vllm/commit/04b02fc8a5) [#51207](https://github.com/vllm-project/vllm/pull/51207)
  [Core] shm tensor arena for efficient cpu->gpu worker broadcast (#51207)
  _Files: `docs/design/shm_tensor_arena.md`, `tests/distributed/test_shm_broadcast.py`, `tools/pre_commit/check_forbidden_imports.py`, `vllm/config/parallel.py` _+4 more__
- **2026-10-09** [`4c43254d52`](https://github.com/vllm-project/vllm/commit/4c43254d52) [#59485](https://github.com/vllm-project/vllm/pull/59485)
  [HiSparse] Report host-pool block residency as HiSparse metrics (#59485)
  _Files: `docs/usage/metrics.md`, `tests/v1/kv_connector/unit/test_hisparse_connector.py`, `tests/v1/kv_connector/unit/test_hisparse_stats.py`, `tests/v1/worker/test_utils.py` _+3 more__
- **2026-10-09** [`3766a67a32`](https://github.com/vllm-project/vllm/commit/3766a67a32) [#60449](https://github.com/vllm-project/vllm/pull/60449)
  [WideEP] Explain how to fix a too-old NCCL for DeepEP v2 (#60449)
  _Files: `tools/ep_kernels/README.md`, `tools/ep_kernels/install_python_libraries.sh`, `vllm/distributed/device_communicators/all2all.py`, `vllm/utils/import_utils.py`_
- **2026-10-09** [`a0f28d73a8`](https://github.com/vllm-project/vllm/commit/a0f28d73a8) [#52110](https://github.com/vllm-project/vllm/pull/52110)
  [sharded state loader] support pp in sharded state loader (#52110)
  _Files: `examples/features/sharded_state/save_sharded_state_offline.py`, `tests/model_executor/model_loader/test_sharded_state_loader.py`, `vllm/distributed/parallel_state.py`, `vllm/model_executor/model_loader/sharded_state_loader.py`_
- **2026-10-09** [`83ed0c7c09`](https://github.com/vllm-project/vllm/commit/83ed0c7c09) [#58860](https://github.com/vllm-project/vllm/pull/58860)
  [Bugfix][NIXL] Fix receive post-process for different P/D block sizes (#58860)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-09** [`bacbbe1878`](https://github.com/vllm-project/vllm/commit/bacbbe1878) [#57734](https://github.com/vllm-project/vllm/pull/57734)
  [Bugfix][NIXL] Guard record_transfer against None telemetry (#57734)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/nixl/stats.py`_
- **2026-10-09** [`4274ae956c`](https://github.com/vllm-project/vllm/commit/4274ae956c) [#59875](https://github.com/vllm-project/vllm/pull/59875)
  [Bugfix][EC Connector] Release shared memory on NIXL setup failure (#59875)
  _Files: `tests/v1/ec_connector/unit/test_scheduler_nixl_ctor.py`, `vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/__init__.py`_
- **2026-10-08** [`72d59adc2c`](https://github.com/vllm-project/vllm/commit/72d59adc2c) [#59997](https://github.com/vllm-project/vllm/pull/59997)
  [Bugfix][KV Connector][NIXL] Transfer the whole PLE short-conv page in disaggregated P/D (#59997)
  _Files: `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py`_
- **2026-10-08** [`9bbc581560`](https://github.com/vllm-project/vllm/commit/9bbc581560) [#60472](https://github.com/vllm-project/vllm/pull/60472)
  [Bugfix] Close MessageQueue zmq resources via finalizer to avoid exit (#60472)
  _Files: `tests/distributed/test_shm_broadcast.py`, `vllm/distributed/device_communicators/shm_broadcast.py`_
- **2026-10-08** [`2f7f05c256`](https://github.com/vllm-project/vllm/commit/2f7f05c256) [#53250](https://github.com/vllm-project/vllm/pull/53250)
  [Bugfix][MoRIIO] Prevent remote KV reload after decoder preemption (#53250)
  _Files: `tests/v1/kv_connector/unit/test_moriio_connector.py`, `tests/v1/kv_connector/unit/test_moriio_hma_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`_
- **2026-10-08** [`daa9085143`](https://github.com/vllm-project/vllm/commit/daa9085143) [#60161](https://github.com/vllm-project/vllm/pull/60161)
  [KV Connector][NIXL] Register HiSparse host pool under single TP Rank (#60161)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py`_
- **2026-10-08** [`4187ade7b8`](https://github.com/vllm-project/vllm/commit/4187ade7b8) [#57849](https://github.com/vllm-project/vllm/pull/57849)
  [Frontend] Consolidate rl entrypoints. (#57849)
  _Files: `.github/CODEOWNERS`, `tests/entrypoints/rl/return_routed_experts/test_route_request_bodies.py`, `tests/entrypoints/rl/weight_transfer_metrics/__init__.py`, `tests/entrypoints/rl/weight_transfer_metrics/test_across_api_servers_metrics.py` _+11 more__
- **2026-10-08** [`caff2b44cb`](https://github.com/vllm-project/vllm/commit/caff2b44cb) [#51018](https://github.com/vllm-project/vllm/pull/51018)
  [BugFix] Pick the DP world-group port at bind time via the coordination store (#51018)
  _Files: `tests/v1/engine/test_core_engine_actor_manager.py`, `tests/v1/engine/test_dp_world_group_port.py`, `vllm/distributed/parallel_state.py`, `vllm/v1/engine/utils.py`_
- **2026-10-07** [`ef63c23d35`](https://github.com/vllm-project/vllm/commit/ef63c23d35) [#59197](https://github.com/vllm-project/vllm/pull/59197)
  [Bugfix][DSv4.1] Skip SWA bounded replay for KV loads that carry the window (#59197)
  _Files: `tests/distributed/aux_output_connector/test_store.py`, `tests/v1/core/test_prefix_caching.py`, `tests/v1/core/test_prefix_replay.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py` _+5 more__
- **2026-10-07** [`df417f780a`](https://github.com/vllm-project/vllm/commit/df417f780a) [#59164](https://github.com/vllm-project/vllm/pull/59164)
  [Bugfix][MoRIIO] Exclude synchronous READ destinations from KV zeroing (#59164)
  _Files: `tests/v1/kv_connector/unit/test_moriio_hma_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/base.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`_
- **2026-10-06** [`e37e51dd24`](https://github.com/vllm-project/vllm/commit/e37e51dd24) [#56318](https://github.com/vllm-project/vllm/pull/56318)
  [Metrics] Expose cached prompt tokens by cache tier (#56318)
  _Files: `rust/src/engine-core-client/src/metrics.rs`, `rust/src/engine-core-client/src/protocol/stats.rs`, `rust/src/metrics/src/scheduler.rs`, `tests/v1/core/test_scheduler.py` _+32 more__
- **2026-10-06** [`3faf214051`](https://github.com/vllm-project/vllm/commit/3faf214051) [#55937](https://github.com/vllm-project/vllm/pull/55937)
  [vllm-bench, feature] Added support for Mooncake-style, timed-traces replay. (#55937)
  _Files: `rust/src/bench/AGENTS.md`, `rust/src/bench/src/benchmark.rs`, `rust/src/bench/src/cli.rs`, `rust/src/bench/src/config.rs` _+8 more__
- **2026-10-06** [`15c1cc12ac`](https://github.com/vllm-project/vllm/commit/15c1cc12ac) [#55804](https://github.com/vllm-project/vllm/pull/55804)
  [Bugfix][EPLB] Use group-local ranks for torch P2P transfers (#55804)
  _Files: `tests/distributed/test_eplb_execute.py`, `vllm/distributed/eplb/eplb_communicator.py`_
- **2026-10-06** [`9465e1c783`](https://github.com/vllm-project/vllm/commit/9465e1c783) [#55471](https://github.com/vllm-project/vllm/pull/55471)
  [Bugfix][NIXL] Recover locally invalidated pull peer metadata (#55471)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+1 more__
- **2026-10-06** [`2537629eb2`](https://github.com/vllm-project/vllm/commit/2537629eb2) [#60107](https://github.com/vllm-project/vllm/pull/60107)
  [Bugfix][KVConnector][NIXL] Size per-region replicate flags by each region's block count (#60107)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-06** [`0e8f8ecba8`](https://github.com/vllm-project/vllm/commit/0e8f8ecba8) [#60108](https://github.com/vllm-project/vllm/pull/60108)
  [Bugfix][KVConnector][NIXL] Return NumPy descriptors from mixed-memory local registration (#60108)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-05** [`2e3154aa18`](https://github.com/vllm-project/vllm/commit/2e3154aa18) [#58949](https://github.com/vllm-project/vllm/pull/58949)
  [HiSparse] Log steady-state max concurrency and expose host-tier utilization gauges (#58949)
  _Files: `docs/design/hisparse.md`, `docs/mkdocs/gen_files/generate_metrics.py`, `docs/usage/metrics.md`, `tests/v1/core/test_kv_cache_utils.py` _+8 more__
- **2026-10-05** [`b1401e0aa7`](https://github.com/vllm-project/vllm/commit/b1401e0aa7) [#59873](https://github.com/vllm-project/vllm/pull/59873)
  [Bugfix][NIXL] Count heartbeats as remote engine activity (#59873)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_

## CI / Build  (26 commits)

- **2026-10-12** [`45bb710eca`](https://github.com/vllm-project/vllm/commit/45bb710eca) [#60456](https://github.com/vllm-project/vllm/pull/60456)
  [CI] Add nightly Python 3.14 smoke test (#60456)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/standalone_tests/python_only_compile.sh`_
- **2026-10-12** [`bfa7e5b7af`](https://github.com/vllm-project/vllm/commit/bfa7e5b7af) [#60784](https://github.com/vllm-project/vllm/pull/60784)
  [XPU][CI] Enable XPU graph in graph tests (#60784)
  _Files: `tests/v1/cudagraph/test_breakable_cudagraph.py`, `tests/v1/cudagraph/test_cudagraph_dispatch.py`, `tests/v1/cudagraph/test_cudagraph_mode.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py`_
- **2026-10-10** [`be0823357f`](https://github.com/vllm-project/vllm/commit/be0823357f) [#60404](https://github.com/vllm-project/vllm/pull/60404)
  [TEST][XPU][CI] Fix ci uva kernel test instability 2 (#60404)
  _Files: `tests/kernels/core/test_uva.py`_
- **2026-10-09** [`783ac12071`](https://github.com/vllm-project/vllm/commit/783ac12071) [#60925](https://github.com/vllm-project/vllm/pull/60925)
  [CI] Accept whitespace around /ci commands and reply instead of going silent (#60925)
  _Files: `.github/workflows/run-ci-command.yml`, `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-10-09** [`1dc60dd367`](https://github.com/vllm-project/vllm/commit/1dc60dd367) [#60894](https://github.com/vllm-project/vllm/pull/60894)
  [CI] Pin pydantic in the mypy pre-commit hook (#60894)
  _Files: `.pre-commit-config.yaml`_
- **2026-10-09** [`90ba2f34b5`](https://github.com/vllm-project/vllm/commit/90ba2f34b5) [#58871](https://github.com/vllm-project/vllm/pull/58871)
  [Build] Find compatible published wheels for precompiled installs (#58871)
  _Files: `.buildkite/test_areas/misc.yaml`, `docs/getting_started/installation/gpu.cuda.inc.md`, `setup.py`, `tests/standalone_tests/test_precompiled_wheel.py`_
- **2026-10-09** [`7368fadebd`](https://github.com/vllm-project/vllm/commit/7368fadebd) [#60817](https://github.com/vllm-project/vllm/pull/60817)
  [CI Failure] Move MTEB tests to h200_35gb (#60817)
  _Files: `.buildkite/test_areas/models_language.yaml`_
- **2026-10-09** [`295c062db8`](https://github.com/vllm-project/vllm/commit/295c062db8) [#60488](https://github.com/vllm-project/vllm/pull/60488)
  Remove sudo from dockerfile command (#60488)
  _Files: `docker/Dockerfile`_
- **2026-10-08** [`972195f4f5`](https://github.com/vllm-project/vllm/commit/972195f4f5) [#60312](https://github.com/vllm-project/vllm/pull/60312)
  [CI][Build] build macos wheels using abi3 (#60312)
  _Files: `.buildkite/scripts/build-macos-wheel.sh`_
- **2026-10-08** [`242e4213fc`](https://github.com/vllm-project/vllm/commit/242e4213fc) [#60259](https://github.com/vllm-project/vllm/pull/60259)
  [Doc] Require GCC 13 for CUDA source builds (#60259)
  _Files: `CMakeLists.txt`, `docs/getting_started/installation/gpu.cuda.inc.md`_
- **2026-10-08** [`dfaabf91ac`](https://github.com/vllm-project/vllm/commit/dfaabf91ac) [#60558](https://github.com/vllm-project/vllm/pull/60558)
  [XPU] [CI] Fix stale ignore path for weight_transfer_metrics tests on Intel CI (#60558)
  _Files: `.buildkite/intel_jobs/entrypoints_intel.yaml`_
- **2026-10-08** [`c4cd88d9fe`](https://github.com/vllm-project/vllm/commit/c4cd88d9fe) [#60540](https://github.com/vllm-project/vllm/pull/60540)
  [CI] Make (H100) Distributed DP + EP optional (#60540)
  _Files: `.buildkite/test_areas/distributed.yaml`_
- **2026-10-08** [`1283362e76`](https://github.com/vllm-project/vllm/commit/1283362e76) [#56775](https://github.com/vllm-project/vllm/pull/56775)
  [CI] Add headroom and selection coverage for H200 fast lanes (#56775)
  _Files: `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/misc.yaml`_
- **2026-10-07** [`13f8c453ee`](https://github.com/vllm-project/vllm/commit/13f8c453ee) [#52213](https://github.com/vllm-project/vllm/pull/52213)
  [CI][Releases] Trigger `perf-eval` Through Release Pipeline (#52213)
  _Files: `.buildkite/release-pipeline.yaml`_
- **2026-10-07** [`703c29179c`](https://github.com/vllm-project/vllm/commit/703c29179c) [#60201](https://github.com/vllm-project/vllm/pull/60201)
  [TEST][XPU][CI] Generalize model runner prefill tail classification tests to all platforms (#60201)
  _Files: `tests/v1/worker/test_gpu_model_runner_prefill_tail_classification.py`_
- **2026-10-06** [`aad4579bbe`](https://github.com/vllm-project/vllm/commit/aad4579bbe) [#60190](https://github.com/vllm-project/vllm/pull/60190)
  Upgrade tpu-inference to v0.31.0 (#60190)
  _Files: `requirements/tpu.txt`_
- **2026-10-06** [`cc73cca9c8`](https://github.com/vllm-project/vllm/commit/cc73cca9c8) [#48962](https://github.com/vllm-project/vllm/pull/48962)
  [Build] Migrate vendored DeepGEMM from pybind to TORCH_LIBRARY (abi3) (#48962)
  _Files: `cmake/external_projects/deepgemm.cmake`, `tools/build_deepgemm_C.py`, `tools/check_wheel_deepgemm.py`, `tools/install_deepgemm.sh` _+1 more__
- **2026-10-06** [`cbe1f9740d`](https://github.com/vllm-project/vllm/commit/cbe1f9740d) [#56907](https://github.com/vllm-project/vllm/pull/56907)
  [NIXL] Bump NIXL version to 1.5.0 (#56907)
  _Files: `requirements/kv_connectors.txt`_
- **2026-10-06** [`0719975cee`](https://github.com/vllm-project/vllm/commit/0719975cee) [#60182](https://github.com/vllm-project/vllm/pull/60182)
  [CI][Rust Frontend] Pass `--locked` to cargo binstall (#60182)
  _Files: `.buildkite/scripts/run-rust-frontend-cargo-ci.sh`_
- **2026-10-06** [`b3082d3044`](https://github.com/vllm-project/vllm/commit/b3082d3044) [#59744](https://github.com/vllm-project/vllm/pull/59744)
  [Rust Frontend] Remove the PyO3 tool-parser bridge (#59744)
  _Files: `.buildkite/scripts/run-rust-frontend-cargo-ci.sh`, `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/parser/python/Cargo.toml` _+5 more__
- **2026-10-06** [`533d81b4b0`](https://github.com/vllm-project/vllm/commit/533d81b4b0) [#52888](https://github.com/vllm-project/vllm/pull/52888)
  [ZenCPU][Test] Add zentorch/torch version pin consistency test (#52888)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `docker/Dockerfile.cpu`, `docs/getting_started/installation/cpu.md`, `tests/test_zentorch_version_pin.py`_
- **2026-10-06** [`4e198cef83`](https://github.com/vllm-project/vllm/commit/4e198cef83) [#60041](https://github.com/vllm-project/vllm/pull/60041)
  [TEST][XPU][CI] Fix ci uva kernel test instability (#60041)
  _Files: `tests/kernels/core/test_uva.py`_
- **2026-10-05** [`89a00995c9`](https://github.com/vllm-project/vllm/commit/89a00995c9) [#59769](https://github.com/vllm-project/vllm/pull/59769)
  [CI] Read each profiler round's trace as it stops in test_gpu_profiler (#59769)
  _Files: `tests/v1/worker/test_gpu_profiler.py`_
- **2026-10-05** [`8542c3eff5`](https://github.com/vllm-project/vllm/commit/8542c3eff5) [#60116](https://github.com/vllm-project/vllm/pull/60116)
  [CI] Fix test_mixed_warmup_gate after #57053 (#60116)
  _Files: `tests/v1/worker/test_mixed_warmup_gate.py`_
- **2026-10-05** [`edde9d2ce4`](https://github.com/vllm-project/vllm/commit/edde9d2ce4) [#59977](https://github.com/vllm-project/vllm/pull/59977)
  Remove redundant dependency requirement for TPU (#59977)
  _Files: `requirements/tpu.txt`_
- **2026-10-05** [`9e931a0c6c`](https://github.com/vllm-project/vllm/commit/9e931a0c6c) [#60060](https://github.com/vllm-project/vllm/pull/60060)
  [CI] Add CODEOWNERS for HiSparse (#60060)
  _Files: `.github/CODEOWNERS`_

## Models  (25 commits)

- **2026-10-12** [`aa1d44df16`](https://github.com/vllm-project/vllm/commit/aa1d44df16) [#60136](https://github.com/vllm-project/vllm/pull/60136)
  [Bugfix][Rust Frontend] Alias `qwen3_xml` to `qwen3_coder` and add `qwen3_json` for the Qwen JSON format (#60136)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs` _+8 more__
- **2026-10-10** [`699c892dd5`](https://github.com/vllm-project/vllm/commit/699c892dd5) [#60246](https://github.com/vllm-project/vllm/pull/60246)
  [Perf] Skip the M-RoPE warmup when every holder of the RoPE fuses it (#60246)
  _Files: `tests/model_executor/test_qwen_vl_triton_warmup.py`, `vllm/model_executor/warmup/qwen_vl_triton_warmup.py`_
- **2026-10-10** [`a205fb3177`](https://github.com/vllm-project/vllm/commit/a205fb3177) [#60954](https://github.com/vllm-project/vllm/pull/60954)
  [Bugfix][Model] Restore AXK1 config defaults dropped with the vendored config (#60954)
  _Files: `vllm/model_executor/models/AXK1.py`_
- **2026-10-10** [`3c802af3cf`](https://github.com/vllm-project/vllm/commit/3c802af3cf) [#60466](https://github.com/vllm-project/vllm/pull/60466)
  [Feat][Frontend] structured decisions: DiffusionGemma read strategy (#60466)
  _Files: `docs/serving/online_serving/structured_decisions.md`, `tests/entrypoints/generate/structured_decisions/test_question_types.py`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `vllm/entrypoints/generate/api_router.py` _+2 more__
- **2026-10-09** [`970dc63478`](https://github.com/vllm-project/vllm/commit/970dc63478) [#60854](https://github.com/vllm-project/vllm/pull/60854)
  [Docs] Add Giga-Embeddings bidirectional Qwen3 usage to embed docs (#60854)
  _Files: `docs/models/pooling_models/embed.md`_
- **2026-10-09** [`5cadabfafd`](https://github.com/vllm-project/vllm/commit/5cadabfafd) [#46368](https://github.com/vllm-project/vllm/pull/46368)
  [Docs] Add Qwen2.5-Coder-7B-Instruct to batch invariance tested models (#46368)
  _Files: `docs/features/batch_invariance.md`_
- **2026-10-09** [`82e89e9944`](https://github.com/vllm-project/vllm/commit/82e89e9944) [#60776](https://github.com/vllm-project/vllm/pull/60776)
  [Perf][Qwen4Exp] Retune H200 M=4 merged QSA LL-GEMM plan (#60776)
  _Files: `vllm/models/qwen4_exp/nvidia/low_latency_gemm.py`_
- **2026-10-09** [`a1cd0ec650`](https://github.com/vllm-project/vllm/commit/a1cd0ec650) [#60415](https://github.com/vllm-project/vllm/pull/60415)
  [Model] Add zerank-2 reranker (#60415)
  _Files: `docs/models/pooling_models/scoring.md`, `examples/pooling/score/template/zerank2.jinja`, `examples/pooling/score/using_template_offline.py`, `examples/pooling/score/using_template_online.py` _+1 more__
- **2026-10-09** [`4611c2c3d2`](https://github.com/vllm-project/vllm/commit/4611c2c3d2) [#59829](https://github.com/vllm-project/vllm/pull/59829)
  [BugFix][DiffusionGemma][CPU] Copy async output snapshots instead of aliasing reused buffers (#59829)
  _Files: `tests/distributed/aux_output_connector/test_store.py`, `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/v1/worker/gpu/async_utils.py`_
- **2026-10-08** [`0004536dd0`](https://github.com/vllm-project/vllm/commit/0004536dd0) [#60529](https://github.com/vllm-project/vllm/pull/60529)
  [XPU][Graph] Replace boolean-mask assignment with `torch.where` (#60529)
  _Files: `vllm/model_executor/models/mimo_mtp.py`_
- **2026-10-07** [`bc8dd4ad27`](https://github.com/vllm-project/vllm/commit/bc8dd4ad27) [#59408](https://github.com/vllm-project/vllm/pull/59408)
  [Rust Frontend] Share `SchemaRoot` between argument coercion and grammars (#59408)
  _Files: `rust/src/parser/src/lib.rs`, `rust/src/parser/src/output_grammar/arguments.rs`, `rust/src/parser/src/schema.rs`, `rust/src/parser/src/tool/parameters.rs` _+2 more__
- **2026-10-07** [`7436a7f119`](https://github.com/vllm-project/vllm/commit/7436a7f119) [#59563](https://github.com/vllm-project/vllm/pull/59563)
  [Rust Frontend] Backtrack from safe text at a complete marker (#59563)
  _Files: `rust/src/parser/src/tool/json/mod.rs`, `rust/src/parser/src/tool/json/qwen.rs`, `rust/src/parser/src/unified/hf/parser.rs`, `rust/src/parser/src/utils.rs`_
- **2026-10-07** [`43b4aaea3e`](https://github.com/vllm-project/vllm/commit/43b4aaea3e) [#60309](https://github.com/vllm-project/vllm/pull/60309)
  [Bugfix][Frontend] Return 4xx for client errors in /cohere/v2/chat (#60309)
  _Files: `tests/entrypoints/cohere/test_api_router.py`, `vllm/entrypoints/cohere/api_router.py`_
- **2026-10-07** [`ef014bdf06`](https://github.com/vllm-project/vllm/commit/ef014bdf06) [#59072](https://github.com/vllm-project/vllm/pull/59072)
  [Bugfix][Frontend] Return logprobs in Cohere Chat v2 responses (#59072)
  _Files: `tests/entrypoints/cohere/test_serving_conversion.py`, `vllm/entrypoints/cohere/serving.py`_
- **2026-10-06** [`ae19af883a`](https://github.com/vllm-project/vllm/commit/ae19af883a) [#60295](https://github.com/vllm-project/vllm/pull/60295)
  [CI] Require transformers 5.19 for the EmbeddingGemma2 registry test (#60295)
  _Files: `tests/models/registry.py`_
- **2026-10-06** [`bb87d227d4`](https://github.com/vllm-project/vllm/commit/bb87d227d4) [#60280](https://github.com/vllm-project/vllm/pull/60280)
  [Bugfix][Model] Fix mypy safe-super error in EmbeddingGemma2Model (#60280)
  _Files: `vllm/model_executor/models/embedding_gemma2.py`_
- **2026-10-06** [`6bbad6acdf`](https://github.com/vllm-project/vllm/commit/6bbad6acdf) [#60203](https://github.com/vllm-project/vllm/pull/60203)
  [Rust Frontend] Pass tool defer_loading through to chat templates (#60203)
  _Files: `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/default/unified.rs`, `rust/src/chat/src/output/harmony/tests.rs`, `rust/src/chat/src/renderer/deepseek_v32/tests.rs` _+24 more__
- **2026-10-06** [`a3e0243b1c`](https://github.com/vllm-project/vllm/commit/a3e0243b1c) [#54844](https://github.com/vllm-project/vllm/pull/54844)
  [Bugfix][Parser] Mistral pre-v11: don't fail requests on unexpected tool call JSON (#54844)
  _Files: `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`_
- **2026-10-06** [`5cd8a2626b`](https://github.com/vllm-project/vllm/commit/5cd8a2626b) [#60036](https://github.com/vllm-project/vllm/pull/60036)
  [Bugfix][Structured Output] Cap JSON schema nesting to prevent 500s and API-server stalls (#60036)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat_error.py`, `tests/parser/cohere/test_structural_tags.py`, `tests/parser/mistral/test_tool_calls.py`, `tests/parser/test_abstract_parser.py` _+7 more__
- **2026-10-05** [`18c8a65edd`](https://github.com/vllm-project/vllm/commit/18c8a65edd) [#60059](https://github.com/vllm-project/vllm/pull/60059)
  [BugFix][Frontend] Pass reasoning_ended through render → generate (#60059) (#60062)
  _Files: `tests/entrypoints/cohere/test_api_router.py`, `tests/entrypoints/scale_out/render/test_render.py`, `tests/entrypoints/scale_out/token_in_token_out/test_protocol.py`, `tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py` _+7 more__
- **2026-10-05** [`64cb683842`](https://github.com/vllm-project/vllm/commit/64cb683842) [#59827](https://github.com/vllm-project/vllm/pull/59827)
  [Model] Add Nemotron 3.5 ASR transcription support (#59827)
  _Files: `docs/models/supported_models.md`, `docs/usage/v1_guide.md`, `vllm/model_executor/models/registry.py`_
- **2026-10-05** [`55b80221ed`](https://github.com/vllm-project/vllm/commit/55b80221ed) [#60027](https://github.com/vllm-project/vllm/pull/60027)
  [Perf][Qwen4Exp] Keep the HC up projection on the skinny GEMM path (#60027)
  _Files: `vllm/model_executor/kernels/linear/cute_dsl/skinny_gemm.py`, `vllm/models/qwen4_exp/nvidia/low_latency_gemm.py`_
- **2026-10-05** [`c04c79e50d`](https://github.com/vllm-project/vllm/commit/c04c79e50d) [#59632](https://github.com/vllm-project/vllm/pull/59632)
  [Performance] Add SM121 TP=2 skinny-GEMM plans (#59632)
  _Files: `vllm/models/qwen4_exp/nvidia/low_latency_gemm.py`_
- **2026-10-05** [`042ab0305c`](https://github.com/vllm-project/vllm/commit/042ab0305c) [#59533](https://github.com/vllm-project/vllm/pull/59533)
  [Perf][Qwen4Exp] Merge QSA QKVG and indexer QK projections (#59533)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `tests/models/qwen4_exp/test_qsa_prepare.py`, `vllm/models/qwen4_exp/nvidia/low_latency_gemm.py`, `vllm/models/qwen4_exp/nvidia/model.py` _+2 more__
- **2026-10-05** [`49e0f47978`](https://github.com/vllm-project/vllm/commit/49e0f47978) [#58560](https://github.com/vllm-project/vllm/pull/58560)
  [Bugfix][DSv4.1] Keep the compressor ring out of the null block (#58560)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `vllm/models/deepseek_v41/compressor.py`_

## Multimodal  (25 commits)

- **2026-10-12** [`f7a3a7265f`](https://github.com/vllm-project/vllm/commit/f7a3a7265f) [#57146](https://github.com/vllm-project/vllm/pull/57146)
  [Bugfix][Multimodal] Fix Qwen3-ASR audio preprocessing parity (#57146)
  _Files: `tests/models/multimodal/processing/test_qwen3_asr.py`, `vllm/model_executor/models/qwen3_asr.py`, `vllm/transformers_utils/processors/__init__.py`, `vllm/transformers_utils/processors/qwen3_asr.py`_
- **2026-10-11** [`b99fdbe1f8`](https://github.com/vllm-project/vllm/commit/b99fdbe1f8) [#61061](https://github.com/vllm-project/vllm/pull/61061)
  [Bugfix] Respect the configured offline chat template (#61061)
  _Files: `tests/entrypoints/multimodal/llm/test_mm_processor_kwargs.py`, `vllm/entrypoints/common/offline.py`_
- **2026-10-11** [`61f084b5f3`](https://github.com/vllm-project/vllm/commit/61f084b5f3) [#55203](https://github.com/vllm-project/vllm/pull/55203)
  [Bugfix][Multimodal] Fix per-video cache option reuse (#55203)
  _Files: `tests/models/multimodal/processing/test_qwen3_vl.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/multimodal/processing/processor.py`_
- **2026-10-10** [`5ca26880ad`](https://github.com/vllm-project/vllm/commit/5ca26880ad) [#48074](https://github.com/vllm-project/vllm/pull/48074)
  Optimize ppc64le vLLM runtime image size (#48074)
  _Files: `docker/Dockerfile.ppc64le`, `docker/build_vllm_ppc64le.sh`_
- **2026-10-09** [`c17fadcfdc`](https://github.com/vllm-project/vllm/commit/c17fadcfdc) [#59865](https://github.com/vllm-project/vllm/pull/59865)
  [XPU] fix fused_input_norm for MM (#59865)
  _Files: `.buildkite/intel_jobs/model_executor_intel.yaml`, `.buildkite/intel_jobs/models_multimodal_intel.yaml`, `vllm/model_executor/layers/fusion/mm_input_norm.py`_
- **2026-10-09** [`2186b89a9a`](https://github.com/vllm-project/vllm/commit/2186b89a9a) [#45022](https://github.com/vllm-project/vllm/pull/45022)
  [Bugfix][Model] Voxtral realtime: fix boot OOM and engine crash at max_model_len (#45022)
  _Files: `tests/models/multimodal/generation/test_voxtral_realtime.py`, `vllm/entrypoints/speech_to_text/realtime/connection.py`, `vllm/model_executor/models/voxtral_realtime.py`_
- **2026-10-09** [`81d9c45e4b`](https://github.com/vllm-project/vllm/commit/81d9c45e4b) [#60598](https://github.com/vllm-project/vllm/pull/60598)
  [Docs] [Multimodal] Note that per-request media_io_kwargs needs --trust-request-mm… (#60598)
  _Files: `docs/features/multimodal_inputs.md`_
- **2026-10-09** [`702ce313f4`](https://github.com/vllm-project/vllm/commit/702ce313f4) [#60196](https://github.com/vllm-project/vllm/pull/60196)
  [Perf][Multimodal] Sort multimodal encoder inputs by modality (#60196)
  _Files: `tests/v1/worker/test_encoder_runner.py`, `tests/v1/worker/test_gpu_model_runner.py`, `vllm/v1/worker/gpu/mm/encoder_runner.py`, `vllm/v1/worker/gpu/mm/lora.py` _+1 more__
- **2026-10-08** [`ab905a885d`](https://github.com/vllm-project/vllm/commit/ab905a885d) [#60253](https://github.com/vllm-project/vllm/pull/60253)
  [CI] Run GH200 test on the shared arm64 CI image (#60253)
  _Files: `.buildkite/hardware_tests/gh200.yaml`, `.buildkite/scripts/hardware_ci/run-gh200-test.sh`_
- **2026-10-08** [`459764104d`](https://github.com/vllm-project/vllm/commit/459764104d) [#58052](https://github.com/vllm-project/vllm/pull/58052)
  [Frontend] Move offline_utils.py to entrypoints/common. (#58052)
  _Files: `.github/CODEOWNERS`, `tests/entrypoints/multimodal/llm/test_mm_processor_kwargs.py`, `tests/entrypoints/unit_tests/test_offline_utils.py`, `vllm/entrypoints/common/__init__.py` _+5 more__
- **2026-10-08** [`032d39e9b4`](https://github.com/vllm-project/vllm/commit/032d39e9b4) [#58817](https://github.com/vllm-project/vllm/pull/58817)
  [XPU][CI] Split Intel jobs to improve B50 utilization (#58817)
  _Files: `.buildkite/intel_jobs/lora_intel.yaml`, `.buildkite/intel_jobs/misc_intel.yaml`, `.buildkite/intel_jobs/model_executor_intel.yaml`, `.buildkite/intel_jobs/models_multimodal_intel.yaml` _+2 more__
- **2026-10-08** [`ee406adf0c`](https://github.com/vllm-project/vllm/commit/ee406adf0c) [#60501](https://github.com/vllm-project/vllm/pull/60501)
  [Bugfix] Fix ZeroDivisionError in Qwen3-VL video sampling when the source fps is unknown (#60501)
  _Files: `tests/multimodal/test_video.py`, `vllm/multimodal/video.py`_
- **2026-10-08** [`95307ac6d4`](https://github.com/vllm-project/vllm/commit/95307ac6d4) [#60519](https://github.com/vllm-project/vllm/pull/60519)
  [Doc] Update ViT CUDA graph design doc (#60519)
  _Files: `docs/design/cuda_graphs_multimodal.md`_
- **2026-10-08** [`775792f2d5`](https://github.com/vllm-project/vllm/commit/775792f2d5) [#60272](https://github.com/vllm-project/vllm/pull/60272)
  [Bugfix] Reland #53020: tie lm_head.weight for Nemotron Parse when checkpoint omits it (#60272)
  _Files: `tests/models/multimodal/generation/test_nemotron_parse.py`, `vllm/model_executor/models/nemotron_parse.py`_
- **2026-10-08** [`8352b2427f`](https://github.com/vllm-project/vllm/commit/8352b2427f) [#58925](https://github.com/vllm-project/vllm/pull/58925)
  [Multimodal] Optimize encoder cudagraph padding logic (#58925)
  _Files: `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/model_executor/models/kimi_k25.py`, `vllm/models/deepseek_v41/common/vl_cudagraph.py`, `vllm/utils/math_utils.py` _+1 more__
- **2026-10-07** [`4ac5a36a8e`](https://github.com/vllm-project/vllm/commit/4ac5a36a8e) [#60090](https://github.com/vllm-project/vllm/pull/60090)
  [CI/Build][NVIDIA] Build NIXL with NIXL EP from source in Rubin image (#60090)
  _Files: `.buildkite/release-pipeline.yaml`, `docker/Dockerfile`, `docker/versions.json`, `docs/contributing/dockerfile/dockerfile.md` _+2 more__
- **2026-10-07** [`b47ec440bc`](https://github.com/vllm-project/vllm/commit/b47ec440bc) [#59487](https://github.com/vllm-project/vllm/pull/59487)
  [CI] Stamp provenance labels on the torch-nightly image so Initialized Snapshot E2E can run (#59487)
  _Files: `.buildkite/image_build/image_build_torch_nightly.sh`_
- **2026-10-07** [`3ca00a8261`](https://github.com/vllm-project/vllm/commit/3ca00a8261) [#60371](https://github.com/vllm-project/vllm/pull/60371)
  [CI] Skip EmbeddingGemma2 pooling tests needing transformers >= 5.19.0 (#60371)
  _Files: `tests/models/multimodal/pooling/test_embedding_gemma2.py`_
- **2026-10-06** [`4ea0c28bc4`](https://github.com/vllm-project/vllm/commit/4ea0c28bc4) [#60240](https://github.com/vllm-project/vllm/pull/60240)
  [Bugfix] Warn only on per-request do_normalize/do_rescale overrides (#60240)
  _Files: `vllm/config/multimodal.py`_
- **2026-10-06** [`6fddc9b21e`](https://github.com/vllm-project/vllm/commit/6fddc9b21e) [#57875](https://github.com/vllm-project/vllm/pull/57875)
  [Profiler] Add per-session profiling controls to Python and Rust frontends (#57875)
  _Files: `docs/contributing/profiling.md`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/error.rs`, `rust/src/server/src/error.rs` _+21 more__
- **2026-10-05** [`87954c5b04`](https://github.com/vllm-project/vllm/commit/87954c5b04) [#60063](https://github.com/vllm-project/vllm/pull/60063)
  [CI/Build] Declare the video modality on the CohereCompass reference model (#60063)
  _Files: `tests/models/multimodal/generation/test_transformers_video.py`, `tests/models/multimodal/generation/vlm_utils/model_utils.py`_
- **2026-10-05** [`528772a4bf`](https://github.com/vllm-project/vllm/commit/528772a4bf) [#59942](https://github.com/vllm-project/vllm/pull/59942)
  [Bugfix][Core] Retain encoder cache references for repeated multimodal inputs (#59942)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-05** [`d3547f9d03`](https://github.com/vllm-project/vllm/commit/d3547f9d03) [#59771](https://github.com/vllm-project/vllm/pull/59771)
  [Test] Re-enable Voxtral HF reference test on Transformers v5 (#59771)
  _Files: `tests/models/multimodal/generation/test_voxtral.py`_
- **2026-10-05** [`710ac56e69`](https://github.com/vllm-project/vllm/commit/710ac56e69) [#60022](https://github.com/vllm-project/vllm/pull/60022)
  [Security] Restrict Pillow image formats on untrusted media paths (#60022)
  _Files: `tests/multimodal/media/test_image.py`, `vllm/multimodal/image.py`, `vllm/multimodal/media/image.py`, `vllm/transformers_utils/processors/kimi_k25_vision_fused.py`_
- **2026-10-05** [`34051ad714`](https://github.com/vllm-project/vllm/commit/34051ad714) [#57441](https://github.com/vllm-project/vllm/pull/57441)
  feat: Add video support for the Transformers backend (#57441)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/generation/test_transformers_audio.py`, `tests/models/multimodal/generation/test_transformers_video.py`, `tests/models/multimodal/processing/test_transformers_video.py` _+5 more__

## Quantization  (15 commits)

- **2026-10-12** [`12e6a585ae`](https://github.com/vllm-project/vllm/commit/12e6a585ae) [#61108](https://github.com/vllm-project/vllm/pull/61108)
  [Fix][Compile] Declare group_shape in the static FP8 quant fusion … (#61108)
  _Files: `vllm/compilation/passes/fusion/matcher_utils.py`_
- **2026-10-12** [`6a70913590`](https://github.com/vllm-project/vllm/commit/6a70913590) [#60976](https://github.com/vllm-project/vllm/pull/60976)
  [XPU] bump up auto-round-lib to 0.16.0 (#60976)
  _Files: `requirements/xpu.txt`, `tests/quantization/test_auto_round.py`_
- **2026-10-10** [`9f1c783886`](https://github.com/vllm-project/vllm/commit/9f1c783886) [#60725](https://github.com/vllm-project/vllm/pull/60725)
  [Test] Allow one fp8 step on K bytes in the kpool decode fuzz test (#60725)
  _Files: `tests/kernels/test_kpool_decode_update_batched.py`_
- **2026-10-09** [`4e318ac563`](https://github.com/vllm-project/vllm/commit/4e318ac563) [#56027](https://github.com/vllm-project/vllm/pull/56027)
  [XPU] fix online fp8_per_channel quantization (#56027)
  _Files: `.buildkite/intel_jobs/quantization.yaml`, `tests/quantization/test_fp8_per_channel.py`, `vllm/platforms/xpu.py`_
- **2026-10-09** [`efd141047d`](https://github.com/vllm-project/vllm/commit/efd141047d) [#60757](https://github.com/vllm-project/vllm/pull/60757)
  [CI] Enroll a third batch of five steps in automatic sharding (#60757)
  _Files: `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/misc.yaml` _+1 more__
- **2026-10-09** [`59ffd73e85`](https://github.com/vllm-project/vllm/commit/59ffd73e85) [#60716](https://github.com/vllm-project/vllm/pull/60716)
  [Bugfix][Kernel] Restore FP fusion for indexer Q quantization (#60716)
  _Files: `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`_
- **2026-10-09** [`efaca9547d`](https://github.com/vllm-project/vllm/commit/efaca9547d) [#59923](https://github.com/vllm-project/vllm/pull/59923)
  [Perf][DSv4.1] Exchange packed FP8 Engram rows across DP and feed wkv MXFP8 (#59923)
  _Files: `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_engram.py`, `vllm/models/deepseek_v41/common/engram.py`, `vllm/models/deepseek_v41/common/ops/query_quant.py` _+2 more__
- **2026-10-08** [`24be8c0bca`](https://github.com/vllm-project/vllm/commit/24be8c0bca) [#60591](https://github.com/vllm-project/vllm/pull/60591)
  [CI] Remove dead in-tree TPU (torch_xla) CI scripts (#60591)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test.sh`, `.buildkite/scripts/hardware_ci/run-tpu-v1-test-part2.sh`, `.buildkite/scripts/hardware_ci/run-tpu-v1-test.sh`, `.buildkite/scripts/tpu/cleanup_docker.sh` _+7 more__
- **2026-10-08** [`21d9758459`](https://github.com/vllm-project/vllm/commit/21d9758459) [#60402](https://github.com/vllm-project/vllm/pull/60402)
  Remove Python 3.10 support now that it is EOL (#60402)
  _Files: `.pre-commit-config.yaml`, `AGENTS.md`, `CMakeLists.txt`, `docker/Dockerfile.cpu` _+63 more__
- **2026-10-08** [`7d47ac2ddb`](https://github.com/vllm-project/vllm/commit/7d47ac2ddb) [#60492](https://github.com/vllm-project/vllm/pull/60492)
  [CI] Enroll five steps in automatic sharding (#60492)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/quantization.yaml`, `.buildkite/test_areas/spec_decode.yaml`_
- **2026-10-08** [`814301b268`](https://github.com/vllm-project/vllm/commit/814301b268) [#60411](https://github.com/vllm-project/vllm/pull/60411)
  [Bugfix][Quant] Read safetensors headers of checkpoints with other file names (#60411)
  _Files: `tests/quantization/test_auto_gptq.py`, `tests/transformers_utils/test_config.py`, `vllm/model_executor/layers/quantization/utils/gptq_utils.py`, `vllm/transformers_utils/config.py`_
- **2026-10-08** [`9e3e37cb3c`](https://github.com/vllm-project/vllm/commit/9e3e37cb3c) [#60383](https://github.com/vllm-project/vllm/pull/60383)
  [TEST][XPU][CI] disable tests of unsupported quantization (#60383)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-10-07** [`32fbfa15e8`](https://github.com/vllm-project/vllm/commit/32fbfa15e8) [#60337](https://github.com/vllm-project/vllm/pull/60337)
  [Bugfix][Quantization] Accept folded NVFP4 scales for Humming A16 (#60337)
  _Files: `vllm/model_executor/layers/quantization/utils/humming/schema.py`_
- **2026-10-06** [`b0b23a48d4`](https://github.com/vllm-project/vllm/commit/b0b23a48d4) [#60142](https://github.com/vllm-project/vllm/pull/60142)
  [Bugfix] Fix Qwen4Exp FP8 PLE pinned lookup kernel failing to compile below SM89 (#60142)
  _Files: `vllm/models/qwen4_exp/common/ngram_embedding.py`, `vllm/triton_utils/importing.py`_
- **2026-10-05** [`edca360f13`](https://github.com/vllm-project/vllm/commit/edca360f13) [#59443](https://github.com/vllm-project/vllm/pull/59443)
  [Bugfix][Qwen4Exp] Load PLE tables unquantized under Quark checkpoints (#59443)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/common/ngram_embedding.py`_

## Speculative Decoding  (15 commits)

- **2026-10-11** [`239a3fa3a8`](https://github.com/vllm-project/vllm/commit/239a3fa3a8) [#61046](https://github.com/vllm-project/vllm/pull/61046)
  [Sleep] Retain draft-private weights with existing parameter selector (#61046)
  _Files: `docs/features/sleep_mode.md`, `tests/v1/worker/test_gpu_worker.py`, `vllm/config/model.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-10-11** [`2339bd39d6`](https://github.com/vllm-project/vllm/commit/2339bd39d6) [#61012](https://github.com/vllm-project/vllm/pull/61012)
  [Bugfix][Mooncake] Use the EAGLE replay boundary when retaining sliding-window tails (#61012)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py`, `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-10-10** [`10cc2f6ae2`](https://github.com/vllm-project/vllm/commit/10cc2f6ae2) [#55504](https://github.com/vllm-project/vllm/pull/55504)
  [Bugfix] Bound GDN speculative decode query widths (#55504)
  _Files: `tests/v1/worker/test_mamba_hybrid_model_state.py`, `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`_
- **2026-10-09** [`51144dd83e`](https://github.com/vllm-project/vllm/commit/51144dd83e) [#47616](https://github.com/vllm-project/vllm/pull/47616)
  [Bugfix][Spec Decode] Trim token_ids/logprobs left past a stop string under speculative decoding (#47616)
  _Files: `tests/detokenizer/test_stop_string_while_stop_model_terminates.py`, `vllm/v1/engine/detokenizer.py`, `vllm/v1/engine/output_processor.py`_
- **2026-10-09** [`ffdde24f54`](https://github.com/vllm-project/vllm/commit/ffdde24f54) [#60913](https://github.com/vllm-project/vllm/pull/60913)
  [Docs] Document adaptive verification without a confidence head (#60913)
  _Files: `docs/features/speculative_decoding/adaptive_verification.md`_
- **2026-10-09** [`89ac8d971b`](https://github.com/vllm-project/vllm/commit/89ac8d971b) [#60715](https://github.com/vllm-project/vllm/pull/60715)
  [CI][Test] Allow 10% ngram acceptance drop under preemption on CUDA in test_async_scheduling_accuracy (#60715)
  _Files: `tests/v1/e2e/general/test_async_scheduling_accuracy.py`_
- **2026-10-09** [`bc713cf8cc`](https://github.com/vllm-project/vllm/commit/bc713cf8cc) [#55923](https://github.com/vllm-project/vllm/pull/55923)
  [Bugfix]MooncakeConnect add query timeout and retry (#55923)
  _Files: `docs/features/mooncake_connector_usage.md`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`, `vllm/models/deepseek_v41/common/engram.py`_
- **2026-10-09** [`581692cc0f`](https://github.com/vllm-project/vllm/commit/581692cc0f) [#57633](https://github.com/vllm-project/vllm/pull/57633)
  [Bugfix][Spec Decode] Fix multimodal embedding merge in Llama 4 and Mistral Large 3 EAGLE drafters (#57633)
  _Files: `tests/v1/worker/test_gpu_target_dependent_ar_speculator.py`, `vllm/model_executor/models/llama4_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`_
- **2026-10-07** [`6ee9be6b3c`](https://github.com/vllm-project/vllm/commit/6ee9be6b3c) [#60335](https://github.com/vllm-project/vllm/pull/60335)
  [Spec Decode] Rename AR speculators to StandaloneAR / TargetDependentAR (#60335)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `tests/v1/cudagraph/test_cudagraph_manager.py`, `tests/v1/worker/test_gpu_target_dependent_ar_speculator.py`, `vllm/v1/worker/gpu/model_runner.py` _+10 more__
- **2026-10-07** [`6c2925fe5f`](https://github.com/vllm-project/vllm/commit/6c2925fe5f) [#55708](https://github.com/vllm-project/vllm/pull/55708)
  [Bugfix][Core] Preserve speculative metrics when coalescing outputs (#55708)
  _Files: `tests/test_outputs.py`, `vllm/outputs.py`_
- **2026-10-06** [`b6d8e8afd9`](https://github.com/vllm-project/vllm/commit/b6d8e8afd9) [#60300](https://github.com/vllm-project/vllm/pull/60300)
  [Bugfix][MRV2][Spec Decode] Accept num_speculative_tokens in NgramGPUSpeculator.propose (#60300)
  _Files: `vllm/v1/worker/gpu/spec_decode/ngram/speculator.py`_
- **2026-10-06** [`819852df6b`](https://github.com/vllm-project/vllm/commit/819852df6b) [#40704](https://github.com/vllm-project/vllm/pull/40704)
  [ModelRunner V2] Speculative Decoding NGram GPU Implementations (#40704)
  _Files: `tests/test_config.py`, `tests/v1/spec_decode/test_max_len.py`, `tests/v1/spec_decode/test_ngram_gpu.py`, `tests/v1/worker/test_gpu_extract_hidden_states_speculator.py` _+10 more__
- **2026-10-06** [`ad0f67a7ec`](https://github.com/vllm-project/vllm/commit/ad0f67a7ec) [#59541](https://github.com/vllm-project/vllm/pull/59541)
  [Bugfix][Spec Decode] Keep heterogeneous-vocab draft models on Model Runner V1 (#59541)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-10-05** [`b1f229fb75`](https://github.com/vllm-project/vllm/commit/b1f229fb75) [#52824](https://github.com/vllm-project/vllm/pull/52824)
  [Model] Declare SupportsEagle3 on Qwen3ASRForConditionalGeneration (#52824)
  _Files: `vllm/model_executor/models/qwen3_asr.py`_
- **2026-10-05** [`4f52fa35ef`](https://github.com/vllm-project/vllm/commit/4f52fa35ef) [#59990](https://github.com/vllm-project/vllm/pull/59990)
  [Bugfix] Fix Qwen4Exp PLE embedding rejecting INC (AutoRound) checkpoints (#59990)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/common/ngram_embedding.py`_

## KV Cache / Offload  (10 commits)

- **2026-10-11** [`01abe975b5`](https://github.com/vllm-project/vllm/commit/01abe975b5) [#59880](https://github.com/vllm-project/vllm/pull/59880)
  [Bugfix][KV Connector] Fix speculative block reservations across KV cache groups (#59880)
  _Files: `tests/v1/kv_connector/unit/test_remote_prefill_lifecycle.py`, `tests/v1/kv_connector/unit/utils.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-10** [`2bea22002d`](https://github.com/vllm-project/vllm/commit/2bea22002d) [#58497](https://github.com/vllm-project/vllm/pull/58497)
  [BUG] Fix KV offload shared-memory slot selection using worker rank (#58497)
  _Files: `tests/v1/kv_offload/test_factory.py`, `vllm/v1/kv_offload/cpu/spec.py`, `vllm/v1/kv_offload/tiering/spec.py`_
- **2026-10-09** [`1c47ebfc57`](https://github.com/vllm-project/vllm/commit/1c47ebfc57) [#60053](https://github.com/vllm-project/vllm/pull/60053)
  [Docs] Fix VLLM_CPU_KVCACHE_SPACE default and units (#60053)
  _Files: `docs/configuration/conserving_memory.md`, `docs/getting_started/installation/cpu.md`, `vllm/platforms/cpu.py`_
- **2026-10-09** [`b027ac8312`](https://github.com/vllm-project/vllm/commit/b027ac8312) [#51956](https://github.com/vllm-project/vllm/pull/51956)
  [XPU] Support register KV offload mmap region as pinned host memory on XPU (#51956)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `tests/v1/kv_offload/test_factory.py`, `vllm/v1/kv_offload/cpu/gpu_worker.py`, `vllm/v1/kv_offload/cpu/host_register.py` _+2 more__
- **2026-10-08** [`e161a0798c`](https://github.com/vllm-project/vllm/commit/e161a0798c) [#60269](https://github.com/vllm-project/vllm/pull/60269)
  [Perf][Core] Reduce free KV cache queue overhead (#60269)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-10-07** [`08567505b0`](https://github.com/vllm-project/vllm/commit/08567505b0) [#58088](https://github.com/vllm-project/vllm/pull/58088)
  [Bugfix][KV Offload] Restore KVCR construction through the secondary-tier factory (#58088)
  _Files: `tests/v1/kv_offload/tiering/test_kvcr_tier.py`, `vllm/v1/kv_offload/tiering/kvcr/manager.py`_
- **2026-10-07** [`17c70c8953`](https://github.com/vllm-project/vllm/commit/17c70c8953) [#59899](https://github.com/vllm-project/vllm/pull/59899)
  [KV Offload] Update KVCR adapter to pool-and-index API (#59899)
  _Files: `.buildkite/scripts/install-kv-offload.sh`, `tests/v1/kv_offload/tiering/test_kvcr_tier.py`, `vllm/v1/kv_offload/tiering/kvcr/manager.py`_
- **2026-10-06** [`fba31f31a9`](https://github.com/vllm-project/vllm/commit/fba31f31a9) [#60140](https://github.com/vllm-project/vllm/pull/60140)
  [GLM5.3 Perf] Switch to fp8 kv cache by default for GLM, 2.3%~5.5% E2E Throughput Improvement (#60140)
  _Files: `vllm/model_executor/models/config.py`_
- **2026-10-06** [`25385102fe`](https://github.com/vllm-project/vllm/commit/25385102fe) [#60071](https://github.com/vllm-project/vllm/pull/60071)
  [Bugfix][KV Offload] Honor speculative cacheability in SimpleCPU (#60071)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-10-05** [`0c16eee3f1`](https://github.com/vllm-project/vllm/commit/0c16eee3f1) [#57816](https://github.com/vllm-project/vllm/pull/57816)
  [Bugfix][KV Offload] Reset SimpleCPU eager-store placement state on MRV2 resume (#57816)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_

## Docs  (8 commits)

- **2026-10-12** [`2534a96fcf`](https://github.com/vllm-project/vllm/commit/2534a96fcf) [#61081](https://github.com/vllm-project/vllm/pull/61081)
  [Docs] List additional unauthenticated endpoints (#61081)
  _Files: `docs/usage/security.md`_
- **2026-10-11** [`93d2cab35e`](https://github.com/vllm-project/vllm/commit/93d2cab35e) [#51504](https://github.com/vllm-project/vllm/pull/51504)
  [Security] Fix P2P ZMQ socket exhaustion via unbounded peer sessions (#51504)
  _Files: `docs/usage/security.md`, `tests/test_envs.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py` _+5 more__
- **2026-10-07** [`b9767299db`](https://github.com/vllm-project/vllm/commit/b9767299db) [#59074](https://github.com/vllm-project/vllm/pull/59074)
  [Bugfix] Respect Inductor deterministic mode in combo-kernel defaults (#59074)
  _Files: `docs/design/debug_vllm_compile.md`, `tests/compile/test_config.py`, `vllm/config/compilation.py`_
- **2026-10-07** [`c741bfca70`](https://github.com/vllm-project/vllm/commit/c741bfca70) [#60416](https://github.com/vllm-project/vllm/pull/60416)
  [Docs] Add review areas for andylolu2 (#60416)
  _Files: `docs/community/reviewers.md`_
- **2026-10-07** [`cbee82324c`](https://github.com/vllm-project/vllm/commit/cbee82324c) [#59949](https://github.com/vllm-project/vllm/pull/59949)
  [Docs][RL] Move pause/resume and batch invariance examples to examples/rl (#59949)
  _Files: `.github/CODEOWNERS`, `docs/usage/reproducibility.md`, `examples/rl/batch_invariance/reproducibility_offline.py`, `examples/rl/pause_resume/data_parallel_pause_resume.py` _+2 more__
- **2026-10-06** [`dac35c5b66`](https://github.com/vllm-project/vllm/commit/dac35c5b66) [#60114](https://github.com/vllm-project/vllm/pull/60114)
  [Misc] Add chat-completion options to gsm8k_eval.py CLI (#60114)
  _Files: `tests/evals/gsm8k/README.md`, `tests/evals/gsm8k/gsm8k_eval.py`_
- **2026-10-06** [`8bd7737a03`](https://github.com/vllm-project/vllm/commit/8bd7737a03) [#59811](https://github.com/vllm-project/vllm/pull/59811)
  [Docs] Clarify that vLLM does not isolate tenants sharing a server (#59811)
  _Files: `docs/usage/security.md`_
- **2026-10-05** [`88f3c601b3`](https://github.com/vllm-project/vllm/commit/88f3c601b3) [#60092](https://github.com/vllm-project/vllm/pull/60092)
  [Docs] Add reviewer area of interest for TheEpicDolphin (#60092)
  _Files: `docs/community/reviewers.md`_

## LoRA  (6 commits)

- **2026-10-12** [`f3cb10b690`](https://github.com/vllm-project/vllm/commit/f3cb10b690) [#61033](https://github.com/vllm-project/vllm/pull/61033)
  [Model][LoRA] Enable LoRA support for BERT and RoBERTa embedding models (#61033)
  _Files: `docs/models/pooling_models/embed.md`, `vllm/model_executor/models/bert.py`_
- **2026-10-12** [`4c36d21280`](https://github.com/vllm-project/vllm/commit/4c36d21280) [#59801](https://github.com/vllm-project/vllm/pull/59801)
  [Bugfix][LoRA] Apply PEFT rank_pattern / alpha_pattern scaling per module (#59801)
  _Files: `tests/lora/test_lora_weights.py`, `tests/lora/test_peft_helper.py`, `vllm/lora/lora_model.py`, `vllm/lora/lora_weights.py` _+1 more__
- **2026-10-09** [`1ee69dde9c`](https://github.com/vllm-project/vllm/commit/1ee69dde9c) [#60225](https://github.com/vllm-project/vllm/pull/60225)
  [Bugfix][LoRA] Reject PEFT adapter features vLLM does not implement (#60225)
  _Files: `tests/entrypoints/serve/lora/test_lora_adapters.py`, `tests/lora/test_peft_helper.py`, `tests/lora/test_utils.py`, `vllm/lora/peft_helper.py` _+1 more__
- **2026-10-08** [`c23ca06b6d`](https://github.com/vllm-project/vllm/commit/c23ca06b6d) [#59627](https://github.com/vllm-project/vllm/pull/59627)
  [Bugfix][Structured Output] Feed the token that implicitly ends reasoning to the grammar (#59627)
  _Files: `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_parser_engine.py`, `tests/v1/spec_decode/test_mtp_structured_output.py`, `tests/v1/structured_output/test_structured_output_manager.py` _+3 more__
- **2026-10-06** [`5145e35e50`](https://github.com/vllm-project/vllm/commit/5145e35e50) [#59743](https://github.com/vllm-project/vllm/pull/59743)
  [Frontend] Port the MiniMax M3 tool parser to the parser engine (#59743)
  _Files: `tests/parser/engine/test_minimax_m3.py`, `tests/parser/engine/test_replay.py`, `tests/parser/engine/trace_builder.py`, `tests/tool_parsers/test_minimax_m3_tool_parser.py` _+3 more__
- **2026-10-05** [`f9c9e8ac24`](https://github.com/vllm-project/vllm/commit/f9c9e8ac24) [#60024](https://github.com/vllm-project/vllm/pull/60024)
  [LoRA] Remove tensorizer (#60024)
  _Files: `docs/models/extensions/tensorizer.md`, `examples/features/tensorize_vllm_model.py`, `tests/entrypoints/openai/completion/test_tensorizer_entrypoint.py`, `tests/lora/test_llama_tp.py` _+5 more__

## Perf / Benchmark  (6 commits)

- **2026-10-08** [`8d10c38b73`](https://github.com/vllm-project/vllm/commit/8d10c38b73) [#60497](https://github.com/vllm-project/vllm/pull/60497)
  [Perf] Reduce fallback decode CPU by 69% at 32K (#60497)
  _Files: `tests/tokenizers_/test_detokenize.py`, `vllm/tokenizers/detokenizer_utils.py`_
- **2026-10-08** [`8674a794c7`](https://github.com/vllm-project/vllm/commit/8674a794c7) [#56875](https://github.com/vllm-project/vllm/pull/56875)
  [Perf] Enable Kimi K3 shared expert sharding with DeepEP v2 (#56875)
  _Files: `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-10-08** [`a58bdd0d4e`](https://github.com/vllm-project/vllm/commit/a58bdd0d4e) [#58685](https://github.com/vllm-project/vllm/pull/58685)
  [Perf] JIT monitor: hook TileLang JITImpl.compile instead of __call__ (#58685)
  _Files: `tests/jit_monitor/test_hooks.py`, `vllm/utils/jit_monitor.py`_
- **2026-10-07** [`956960f85f`](https://github.com/vllm-project/vllm/commit/956960f85f) [#60215](https://github.com/vllm-project/vllm/pull/60215)
  [Perf][MRV2] Avoid stream syncs in NonUvaBuffer host-to-device copies (#60215)
  _Files: `tests/kernels/core/test_uva.py`, `vllm/v1/worker/gpu/buffer_utils.py`_
- **2026-10-06** [`e82b80099a`](https://github.com/vllm-project/vllm/commit/e82b80099a) [#60083](https://github.com/vllm-project/vllm/pull/60083)
  [Perf][HiSparse] Cache per-request residency instead of rescanning every page each step (#60083)
  _Files: `vllm/v1/hisparse/coordinator.py`_
- **2026-10-06** [`3e182185aa`](https://github.com/vllm-project/vllm/commit/3e182185aa) [#60129](https://github.com/vllm-project/vllm/pull/60129)
  [Deprecation] Deprecate sonet dataset as scheduled (#60129)
  _Files: `benchmarks/sonnet.txt`, `docs/benchmarking/cli.md`, `pyproject.toml`, `rust/src/bench/AGENTS.md` _+14 more__

## Distributed  (1 commits)

- **2026-10-06** [`888074b42d`](https://github.com/vllm-project/vllm/commit/888074b42d) [#60170](https://github.com/vllm-project/vllm/pull/60170)
  [CPU][Recipes] Detect model head constraints for automatic tensor parallel selection in vLLM Recipes Tool (#60170)
  _Files: `tools/recipes/RUNTIME_TUNING.md`, `tools/recipes/model_constraints.py`, `tools/recipes/runtime_tuning.py`_

## Compilation / CUDA Graph  (1 commits)

- **2026-10-06** [`eb2901b735`](https://github.com/vllm-project/vllm/commit/eb2901b735) [#59532](https://github.com/vllm-project/vllm/pull/59532)
  [Perf][DSv4.1] Run decoder replay layers in CUDA graphs and trim in PIECEWISE graphs (#59532)
  _Files: `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/config/compilation.py` _+6 more__

---
_Generated 2026-10-12 17:47 UTC_