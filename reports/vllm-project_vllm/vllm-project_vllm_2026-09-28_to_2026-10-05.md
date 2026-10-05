# vllm-project/vllm — Weekly Change Report
**Period:** 2026-09-28 → 2026-10-05  |  **Total commits:** 446

## ✨ New Features This Week

- **2026-10-05** [#59827](https://github.com/vllm-project/vllm/pull/59827) — [Model] Add Nemotron 3.5 ASR transcription support (#59827)
- **2026-10-05** [#60060](https://github.com/vllm-project/vllm/pull/60060) — [CI] Add CODEOWNERS for HiSparse (#60060)
- **2026-10-05** [#59211](https://github.com/vllm-project/vllm/pull/59211) — [Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer (#59211)
- **2026-10-05** [#59771](https://github.com/vllm-project/vllm/pull/59771) — [Test] Re-enable Voxtral HF reference test on Transformers v5 (#59771)
- **2026-10-05** [#59246](https://github.com/vllm-project/vllm/pull/59246) — [Attention][MLA] Support fp8_ds_mla KV cache for NoPE-512 models on SM90 (#59246)
- **2026-10-05** [#59632](https://github.com/vllm-project/vllm/pull/59632) — [Performance] Add SM121 TP=2 skinny-GEMM plans (#59632)
- **2026-10-05** [#52824](https://github.com/vllm-project/vllm/pull/52824) — [Model] Declare SupportsEagle3 on Qwen3ASRForConditionalGeneration (#52824)
- **2026-10-05** [#57441](https://github.com/vllm-project/vllm/pull/57441) — feat: Add video support for the Transformers backend (#57441)
- **2026-10-04** [#59377](https://github.com/vllm-project/vllm/pull/59377) — [Kernel][LoRA] Add deterministic split-K=8 LoRA shrink for batch invariance (#59377)
- **2026-10-04** [#59160](https://github.com/vllm-project/vllm/pull/59160) — [Feature] Release the CUDA graph pool on sleep (#59160)
- _…and 84 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-05** [`d23af12cb1`](https://github.com/vllm-project/vllm/commit/d23af12cb1) [#57947](https://github.com/vllm-project/vllm/pull/57947) — [ROCm][Perf] Reach the fused QSA pre-indexer from the AMD path (#57947)
- **2026-10-05** [`30d4032363`](https://github.com/vllm-project/vllm/commit/30d4032363) [#59211](https://github.com/vllm-project/vllm/pull/59211) — [Model][GLM-5.3-Flash] Support DCP for the kpool sparse indexer (#59211)
- **2026-10-05** [`0e468adb43`](https://github.com/vllm-project/vllm/commit/0e468adb43) [#59278](https://github.com/vllm-project/vllm/pull/59278) — [Model] Extend device-side mm normalization to Kimi K2.5 / K3 (#59278)
- **2026-10-05** [`92044241a0`](https://github.com/vllm-project/vllm/commit/92044241a0) [#58014](https://github.com/vllm-project/vllm/pull/58014) — [Bugfix][ROCm] Preserve config during GPU memory profiling (#58014)
- **2026-10-05** [`ac8c2130a8`](https://github.com/vllm-project/vllm/commit/ac8c2130a8) [#59794](https://github.com/vllm-project/vllm/pull/59794) — [ROCm] Bump AITER to 0.1.24.post1 (#59794)
- **2026-10-04** [`f98d1fc493`](https://github.com/vllm-project/vllm/commit/f98d1fc493) [#59550](https://github.com/vllm-project/vllm/pull/59550) — [ROCm][Bugfix] Fix ROCM_ATTN sliding-window boundary (#59550)
- **2026-10-04** [`d61081dc3d`](https://github.com/vllm-project/vllm/commit/d61081dc3d) [#59932](https://github.com/vllm-project/vllm/pull/59932) — [CI] Bump peft to satisfy transformers 5.18 minimum (#59932)
- **2026-10-04** [`9e0b6fcf77`](https://github.com/vllm-project/vllm/commit/9e0b6fcf77) [#59621](https://github.com/vllm-project/vllm/pull/59621) — [CI] Bump Transformers version to 5.18.0 (#59621)
- **2026-10-03** [`4ac0d0eac2`](https://github.com/vllm-project/vllm/commit/4ac0d0eac2) [#54706](https://github.com/vllm-project/vllm/pull/54706) — [ROCm][RDNA3] Fix W4A16 split-K accuracy and determinism (#54706)
- **2026-10-03** [`f03026a548`](https://github.com/vllm-project/vllm/commit/f03026a548) [#59441](https://github.com/vllm-project/vllm/pull/59441) — [Bugfix][MoRIIO] Keep discovery heartbeats running while workers hold the GIL (#59441)
- **2026-10-03** [`b0e21b3083`](https://github.com/vllm-project/vllm/commit/b0e21b3083) [#51274](https://github.com/vllm-project/vllm/pull/51274) — [ROCm][Kimi-K3] Add opt-in gfx942 MXFP4-to-int4 conversion (#51274)
- **2026-10-03** [`c28834df00`](https://github.com/vllm-project/vllm/commit/c28834df00) [#56679](https://github.com/vllm-project/vllm/pull/56679) — [ROCm][CI] Extend AMD coverage for distributed, model, and eval tests (#56679)
- **2026-10-03** [`faa9860dbd`](https://github.com/vllm-project/vllm/commit/faa9860dbd) [#59333](https://github.com/vllm-project/vllm/pull/59333) — [ROCm][CI][AiterExperts] Add test coverage for hidden/intermediate padding correctness (#59333)
- **2026-10-02** [`111f71a6db`](https://github.com/vllm-project/vllm/commit/111f71a6db) [#54049](https://github.com/vllm-project/vllm/pull/54049) — [feat] FlashInfer CuteDSL MegaMoE integration  (#54049)
- **2026-10-02** [`8882b83b34`](https://github.com/vllm-project/vllm/commit/8882b83b34) [#59796](https://github.com/vllm-project/vllm/pull/59796) — [Bugfix] Bump tokenizers to 0.23.2 for duplicate-pattern support (#59796)
- **2026-10-02** [`6abadc2aa7`](https://github.com/vllm-project/vllm/commit/6abadc2aa7) [#59332](https://github.com/vllm-project/vllm/pull/59332) — [ROCm][CI] Add test coverage for VLLM_ROCM_MOE_PADDING memory-stride padding transparency (#59332)
- **2026-10-02** [`4c4003bb5f`](https://github.com/vllm-project/vllm/commit/4c4003bb5f) [#59455](https://github.com/vllm-project/vllm/pull/59455) — [Bugfix] Bind routed-experts capture to the MoE layer, not the kernel (#59455)
- **2026-10-02** [`e2cb5ee46c`](https://github.com/vllm-project/vllm/commit/e2cb5ee46c) [#53341](https://github.com/vllm-project/vllm/pull/53341) — [CI] Replace shellcheck-suppressed patterns flagged in #52572 with clean equivalents (#53341)
- **2026-10-02** [`98b29aa99a`](https://github.com/vllm-project/vllm/commit/98b29aa99a) [#58167](https://github.com/vllm-project/vllm/pull/58167) — [ROCm][Perf][GLM-5.3-Flash] Add AITER topk backend for decodes (#58167)
- **2026-10-02** [`751fa96a49`](https://github.com/vllm-project/vllm/commit/751fa96a49) [#58569](https://github.com/vllm-project/vllm/pull/58569) — [ROCm][Perf][GLM-5.3-Flash] Remove redundant copy after ragged sparse MLA (#58569)
- **2026-10-02** [`0154979656`](https://github.com/vllm-project/vllm/commit/0154979656) [#58344](https://github.com/vllm-project/vllm/pull/58344) — [ROCm][Perf] Kimi-K3 enable prefill checkpoints on ROCm (#58344)
- **2026-10-02** [`e3cae8d2ac`](https://github.com/vllm-project/vllm/commit/e3cae8d2ac) [#57387](https://github.com/vllm-project/vllm/pull/57387) — [Model] Use upstream GLM-5.3 and Qwen4-Exp configs and processor (#57387)
- **2026-10-02** [`eec3c36a47`](https://github.com/vllm-project/vllm/commit/eec3c36a47) [#54805](https://github.com/vllm-project/vllm/pull/54805) — [ROCm][BugFix] Revert AITER PA gluon decode from ROCM_AITER_FA (#54805)
- **2026-10-01** [`e6674262f1`](https://github.com/vllm-project/vllm/commit/e6674262f1) [#59700](https://github.com/vllm-project/vllm/pull/59700) — [Bugfix][CI] Widen DBO+DP+EP GSM8K accuracy margin on ROCm (#59700)
- **2026-10-01** [`d2125ea681`](https://github.com/vllm-project/vllm/commit/d2125ea681) [#59666](https://github.com/vllm-project/vllm/pull/59666) — [ROCm][CI] Raise the MI355 DeepSeek-R1 GSM8K startup wait to 1800s (#59666)
- **2026-10-01** [`ccda9098cc`](https://github.com/vllm-project/vllm/commit/ccda9098cc) [#59593](https://github.com/vllm-project/vllm/pull/59593) — [ROCm][CI] Drop two no-GPU AMD mirrors from the CPU test areas (#59593)
- **2026-10-01** [`d848c4ed3d`](https://github.com/vllm-project/vllm/commit/d848c4ed3d) [#58769](https://github.com/vllm-project/vllm/pull/58769) — [ROCm][Triton] Migrate Kimi-K3 kernels from make_block_ptr to tensor … (#58769)
- **2026-10-01** [`26bfdfb6bc`](https://github.com/vllm-project/vllm/commit/26bfdfb6bc) [#57978](https://github.com/vllm-project/vllm/pull/57978) — [ROCm][Perf] Parallelise AITER MLA page-index expansion over token chunks (#57978)
- **2026-10-01** [`08e03df940`](https://github.com/vllm-project/vllm/commit/08e03df940) [#59454](https://github.com/vllm-project/vllm/pull/59454) — [Bugfix][ROCm] Use a zero default for masked scales in the MXFP8 GEMM (#59454)
- **2026-10-01** [`cfd54ca881`](https://github.com/vllm-project/vllm/commit/cfd54ca881) [#59595](https://github.com/vllm-project/vllm/pull/59595) — [ROCm][CI] Drop four no-GPU CPU groups from the legacy AMD pipeline (#59595)
- **2026-10-01** [`cb6458c5ce`](https://github.com/vllm-project/vllm/commit/cb6458c5ce) [#58997](https://github.com/vllm-project/vllm/pull/58997) — [Core] Remove deprecated mamba_cache_mode "all" (#58997)
- **2026-10-01** [`c4fc3c7d32`](https://github.com/vllm-project/vllm/commit/c4fc3c7d32) [#58921](https://github.com/vllm-project/vllm/pull/58921) — [Bugfix][Spec Decode] Per-module LM heads for multi-layer MTP on Model Runner V2 (#58921)
- **2026-10-01** [`aee8fe202a`](https://github.com/vllm-project/vllm/commit/aee8fe202a) [#58887](https://github.com/vllm-project/vllm/pull/58887) — [Bugfix][ROCm] Fix race on AITER MLA FP8 prefill scheduling metadata under async scheduling (#58887)
- **2026-10-01** [`4c2d277643`](https://github.com/vllm-project/vllm/commit/4c2d277643) [#59327](https://github.com/vllm-project/vllm/pull/59327) — [Perf][DSv4.1] Faster Engram host lookups: sorted rows, inline big lookups (#59327)
- **2026-10-01** [`76d3929916`](https://github.com/vllm-project/vllm/commit/76d3929916) [#55422](https://github.com/vllm-project/vllm/pull/55422) — [Docker] Compile Python bytecode at image build time (#55422)
- **2026-10-01** [`df8fd42116`](https://github.com/vllm-project/vllm/commit/df8fd42116) [#55840](https://github.com/vllm-project/vllm/pull/55840) — [CI][Spec Decode] Add async scheduling accuracy tests (#55840)
- **2026-09-30** [`26ce58b48c`](https://github.com/vllm-project/vllm/commit/26ce58b48c) [#59499](https://github.com/vllm-project/vllm/pull/59499) — [ROCm][CI] Sync two AMD test groups between test-amd.yaml and test_areas (#59499)
- **2026-09-30** [`b56b54bc54`](https://github.com/vllm-project/vllm/commit/b56b54bc54) [#59477](https://github.com/vllm-project/vllm/pull/59477) — [ROCm][CI] Relax simple-nemotron-h-8b GSM8K threshold on ROCm (#59477)
- **2026-09-30** [`ed3f6d1a56`](https://github.com/vllm-project/vllm/commit/ed3f6d1a56) [#59256](https://github.com/vllm-project/vllm/pull/59256) — [ROCm][CI] Remove duplicate MI355 DPX jobs (#59256)
- **2026-09-30** [`b33e1cb172`](https://github.com/vllm-project/vllm/commit/b33e1cb172) [#59253](https://github.com/vllm-project/vllm/pull/59253) — [ROCm]Transpose compressed-tensors MoE weights on device (#59253)
- **2026-09-30** [`8f24ab30a3`](https://github.com/vllm-project/vllm/commit/8f24ab30a3) [#57640](https://github.com/vllm-project/vllm/pull/57640) — [ROCm][Kimi-K3][Perf] Fuse MLA decode KV-cache write and Q-prep via AITER (#57640)
- **2026-09-30** [`d2fb35f66e`](https://github.com/vllm-project/vllm/commit/d2fb35f66e) [#59237](https://github.com/vllm-project/vllm/pull/59237) — [CI][ROCm] Drop the duplicate OAI Triton MoE run from FP8 MoE Kernels (#59237)
- **2026-09-30** [`42a3dd5fec`](https://github.com/vllm-project/vllm/commit/42a3dd5fec) [#59287](https://github.com/vllm-project/vllm/pull/59287) — [ROcm][BugFix][The Rock] Update The Rock dockerfile to most recent Triton 3.8 (#59287)
- **2026-09-30** [`c4df37dfcc`](https://github.com/vllm-project/vllm/commit/c4df37dfcc) [#59372](https://github.com/vllm-project/vllm/pull/59372) — [ROCm][BugFix][The Rock] Fix mori build for the rock (#59372)
- **2026-09-30** [`4e1182a3a6`](https://github.com/vllm-project/vllm/commit/4e1182a3a6) [#55368](https://github.com/vllm-project/vllm/pull/55368) — [ROCm][MoE] Pad the AITER MoE intermediate size at allocation time, and round the expert-group count to a kernel that exists (#55368)
- **2026-09-30** [`2df122e65e`](https://github.com/vllm-project/vllm/commit/2df122e65e) [#58008](https://github.com/vllm-project/vllm/pull/58008) — [ROCm][Perf][GLM-5.3-Flash] "Fit kpool top-k indices to AITER" with a single Triton kernel (#58008)
- **2026-09-30** [`eef8b15d7c`](https://github.com/vllm-project/vllm/commit/eef8b15d7c) [#59427](https://github.com/vllm-project/vllm/pull/59427) — [Security] Bump pyjwt and rand for remaining GHSAs (#59427)
- **2026-09-30** [`a4c4bb418e`](https://github.com/vllm-project/vllm/commit/a4c4bb418e) [#59315](https://github.com/vllm-project/vllm/pull/59315) — [Security] Bump remaining Dependabot packages (excl. ignored) (#59315)
- **2026-09-30** [`91dab0eb7f`](https://github.com/vllm-project/vllm/commit/91dab0eb7f) [#58797](https://github.com/vllm-project/vllm/pull/58797) — [ROCm][Perf] Allocate the pinned PLE prefetch buffer lazily (#58797)
- **2026-09-30** [`50319916a3`](https://github.com/vllm-project/vllm/commit/50319916a3) [#59400](https://github.com/vllm-project/vllm/pull/59400) — [ROCm][CI] Move Basic Models (Other) to MI355 (#59400)
- **2026-09-30** [`16d4ac4ba3`](https://github.com/vllm-project/vllm/commit/16d4ac4ba3) [#58262](https://github.com/vllm-project/vllm/pull/58262) — [ROCm][MoE] Support MiMo-V2.6 MXFP4 on gfx942 (#58262)
- **2026-09-30** [`3627a6a124`](https://github.com/vllm-project/vllm/commit/3627a6a124) [#57979](https://github.com/vllm-project/vllm/pull/57979) — [ROCm][Perf][GLM-5.3-Flash] Stride-aware decode KDA (#57979)
- **2026-09-30** [`8ee4069033`](https://github.com/vllm-project/vllm/commit/8ee4069033) [#58539](https://github.com/vllm-project/vllm/pull/58539) — [ROCm][DSv4.1][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill (#58539)
- **2026-09-30** [`fcd317cf33`](https://github.com/vllm-project/vllm/commit/fcd317cf33) [#58405](https://github.com/vllm-project/vllm/pull/58405) — [ROCm][DSv4][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill (#58405)
- **2026-09-30** [`77e8b02c8d`](https://github.com/vllm-project/vllm/commit/77e8b02c8d) [#58819](https://github.com/vllm-project/vllm/pull/58819) — [ROCm][Perf] Add opt-in a4w4 (FP4 activation) MoE for DeepSeek V4.1 on AITER (#58819)
- **2026-09-30** [`834ad456d3`](https://github.com/vllm-project/vllm/commit/834ad456d3) [#58916](https://github.com/vllm-project/vllm/pull/58916) — [Refactor] Remove dead tests code (#58916)
- **2026-09-30** [`a8e069f81b`](https://github.com/vllm-project/vllm/commit/a8e069f81b) [#58648](https://github.com/vllm-project/vllm/pull/58648) — [Bugfix][MiniMax M3] Share target embeddings with MTP under PP (#58648)
- **2026-09-29** [`eec2a86b1e`](https://github.com/vllm-project/vllm/commit/eec2a86b1e) [#59249](https://github.com/vllm-project/vllm/pull/59249) — [Security] Bump nltk, aiohttp, pillow, and datamodel-code-generator (#59249)
- **2026-09-29** [`5dd693122c`](https://github.com/vllm-project/vllm/commit/5dd693122c) [#51043](https://github.com/vllm-project/vllm/pull/51043) — [MyPy][2/N] Fix mypy errors in small tests/ dirs (#51043)
- **2026-09-29** [`7aa8372ef7`](https://github.com/vllm-project/vllm/commit/7aa8372ef7) [#59262](https://github.com/vllm-project/vllm/pull/59262) — [ROCm][CI] Run Basic Correctness Sleep Mode on MI300 for now (#59262)
- **2026-09-29** [`30ae8248b6`](https://github.com/vllm-project/vllm/commit/30ae8248b6) [#57700](https://github.com/vllm-project/vllm/pull/57700) — [KVConnector][MoRIIO] Support K3 DSpark hybrid READ (#57700)
- **2026-09-29** [`df4dbe46e7`](https://github.com/vllm-project/vllm/commit/df4dbe46e7) [#59227](https://github.com/vllm-project/vllm/pull/59227) — [CI][ROCm] Increase timeouts for AMD MI300 jobs near their limits (#59227)
- **2026-09-29** [`467d81d9a0`](https://github.com/vllm-project/vllm/commit/467d81d9a0) [#56073](https://github.com/vllm-project/vllm/pull/56073) — [ROCm] Upgrade MoRI version on rocm dockers required for WideEP DP16 DI CI enablement and fixes for combine API (#56073)
- **2026-09-29** [`c3a4a36c20`](https://github.com/vllm-project/vllm/commit/c3a4a36c20) [#59201](https://github.com/vllm-project/vllm/pull/59201) — [CI][ROCm] Fix stale basic_correctness path in Model Runner V2 Distributed (#59201)
- **2026-09-29** [`dfc8e0f3e2`](https://github.com/vllm-project/vllm/commit/dfc8e0f3e2) [#58019](https://github.com/vllm-project/vllm/pull/58019) — [Frontend] Support strict MiMo-V2.6 tool calling (#58019)
- **2026-09-29** [`05d89636fc`](https://github.com/vllm-project/vllm/commit/05d89636fc) [#58433](https://github.com/vllm-project/vllm/pull/58433) — [ROCm][CI] Mirror generic GEMM-RS/AR on MI355 (#58433)
- **2026-09-29** [`3acddf01e7`](https://github.com/vllm-project/vllm/commit/3acddf01e7) [#58967](https://github.com/vllm-project/vllm/pull/58967) — [Bugfix][ROCm] Keep Mooncake bootstrap ports bound during startup (#58967)
- **2026-09-29** [`6ebb5bd64f`](https://github.com/vllm-project/vllm/commit/6ebb5bd64f) [#59137](https://github.com/vllm-project/vllm/pull/59137) — [ROCm][CI] Expand MI355 mirrors and route MIG-sized jobs to DPX (#59137)
- **2026-09-29** [`77d9cda688`](https://github.com/vllm-project/vllm/commit/77d9cda688) [#58904](https://github.com/vllm-project/vllm/pull/58904) — [ROCm][Model][Bugfix] Fix GLM-5.2 shared-expert fusion and MTP on the ROCm DSA path (#58904)
- **2026-09-29** [`78fc1e6274`](https://github.com/vllm-project/vllm/commit/78fc1e6274) [#58284](https://github.com/vllm-project/vllm/pull/58284) — [ROCm][CI] Add MI355 TP2 AR-RMS and B200 fusion mirrors (#58284)
- **2026-09-29** [`69d5c81fcd`](https://github.com/vllm-project/vllm/commit/69d5c81fcd) [#58654](https://github.com/vllm-project/vllm/pull/58654) — [ROCm][CI] Mirror split kernel groups on MI355 and fix exposed tests (#58654)
- **2026-09-29** [`0ae480ff1a`](https://github.com/vllm-project/vllm/commit/0ae480ff1a) [#58683](https://github.com/vllm-project/vllm/pull/58683) — [CI][ROCm] Mirror large-model GSM8K evaluations on MI355 (#58683)
- **2026-09-29** [`63b9931b73`](https://github.com/vllm-project/vllm/commit/63b9931b73) [#58671](https://github.com/vllm-project/vllm/pull/58671) — [ROCm][DSv4.1] Paged MXFP4 sparse indexer on aiter's MQA-logits kernel (#58671)
- **2026-09-29** [`491f44adfa`](https://github.com/vllm-project/vllm/commit/491f44adfa) [#51289](https://github.com/vllm-project/vllm/pull/51289) — [Model] Extend device-side mm normalization to Qwen3VL/Qwen3.5/Qwen4Next (#51289)
- **2026-09-29** [`cf971b419a`](https://github.com/vllm-project/vllm/commit/cf971b419a) [#59125](https://github.com/vllm-project/vllm/pull/59125) — [Bugfix] Revert "[ROCm][Perf] Replace torch.topk in DSA candidate block selection" (#59125)
- **2026-09-29** [`0af34418e9`](https://github.com/vllm-project/vllm/commit/0af34418e9) [#58655](https://github.com/vllm-project/vllm/pull/58655) — [ROCm][DSv4.1][Perf] Run the delayed mHC seams through aiter's fused Triton kernel (#58655)
- **2026-09-29** [`70ae0b7435`](https://github.com/vllm-project/vllm/commit/70ae0b7435) [#53492](https://github.com/vllm-project/vllm/pull/53492) — [ROCm][MLA] Enable sparse MLA Gluon kernel from Aiter (#53492)
- **2026-09-28** [`75fad5bbef`](https://github.com/vllm-project/vllm/commit/75fad5bbef) [#58058](https://github.com/vllm-project/vllm/pull/58058) — [Bugfix][ROCm] Drop -1 sentinels when building the ragged sparse-MLA indices (#58058)
- **2026-09-28** [`8a497d7557`](https://github.com/vllm-project/vllm/commit/8a497d7557) [#52395](https://github.com/vllm-project/vllm/pull/52395) — [CI/Build][BugFix][The Rock] Make supports_mm_prefix  return False for ROCm attn and unified attn since Prefix-LM not implemented (#52395)
- **2026-09-28** [`beef814e1d`](https://github.com/vllm-project/vllm/commit/beef814e1d) [#50519](https://github.com/vllm-project/vllm/pull/50519) — [ROCm][CI] Add missing test coverage for upstream parity (#50519)
- **2026-09-28** [`25624f65cf`](https://github.com/vllm-project/vllm/commit/25624f65cf) [#56861](https://github.com/vllm-project/vllm/pull/56861) — [ROCm][MLA] Add an AITER ASM round-robin decode route for DCP multi-token verify (#56861)
- **2026-09-28** [`5ba2e3090b`](https://github.com/vllm-project/vllm/commit/5ba2e3090b) [#59076](https://github.com/vllm-project/vllm/pull/59076) — [ROCm][CI] Increase timeout for Entrypoints Unit (#59076)
- **2026-09-28** [`7a160c6fe5`](https://github.com/vllm-project/vllm/commit/7a160c6fe5) [#59051](https://github.com/vllm-project/vllm/pull/59051) — [ROCm][CI] Pin OpenTelemetry to LMCache's cap in the ROCm images (#59051)
- **2026-09-28** [`b0d2b854f6`](https://github.com/vllm-project/vllm/commit/b0d2b854f6) [#59056](https://github.com/vllm-project/vllm/pull/59056) — [ROCm]Keep LMCache OpenTelemetry on the image's 1.40 stack (#59056)
- **2026-09-28** [`6b24bd8e75`](https://github.com/vllm-project/vllm/commit/6b24bd8e75) [#58208](https://github.com/vllm-project/vllm/pull/58208) — [ROCm][Perf] Replace torch.topk in DSA candidate block selection (#58208)
- **2026-09-28** [`a7ff44355c`](https://github.com/vllm-project/vllm/commit/a7ff44355c) [#54956](https://github.com/vllm-project/vllm/pull/54956) — [ROCm][Perf] Kimi-K3 Enable sharded latent MoE up-projection under EP (#54956)
- **2026-09-28** [`7ba3df63cb`](https://github.com/vllm-project/vllm/commit/7ba3df63cb) [#58983](https://github.com/vllm-project/vllm/pull/58983) — [ROCm][Refactor] Move DeepSeek-V4/V4.1 multi-stream overlap gate to ROCm platform (#58983)
- **2026-09-28** [`20b52e9f5b`](https://github.com/vllm-project/vllm/commit/20b52e9f5b) [#58114](https://github.com/vllm-project/vllm/pull/58114) — [Perf][Qwen3.8] Reduce PLE metadata construction overhead (#58114)
- **2026-09-28** [`f6877f563c`](https://github.com/vllm-project/vllm/commit/f6877f563c) [#57568](https://github.com/vllm-project/vllm/pull/57568) — [Bugfix][Spec Decode] Implement get_top_tokens() on the ROCm DeepSeek V4 MTP drafter (#57568)
- **2026-09-28** [`252279314b`](https://github.com/vllm-project/vllm/commit/252279314b) [#58652](https://github.com/vllm-project/vllm/pull/58652) — Revert "[CI] Shard (H200 MIG 35GB / MI355 DPX) Entrypoints Integration (Pooling) into named jobs (#58652)" (#59011)
- **2026-09-28** [`66d2d4b2e7`](https://github.com/vllm-project/vllm/commit/66d2d4b2e7) [#58451](https://github.com/vllm-project/vllm/pull/58451) — [CI] Split Dynamic Shapes out of (H200 MIG 35GB) PyTorch Compilation + (MI300) mirror (#58451)
- **2026-09-28** [`413ae4b167`](https://github.com/vllm-project/vllm/commit/413ae4b167) [#58652](https://github.com/vllm-project/vllm/pull/58652) — [CI] Shard (H200 MIG 35GB / MI355 DPX) Entrypoints Integration (Pooling) into named jobs (#58652)
- **2026-09-28** [`4694145045`](https://github.com/vllm-project/vllm/commit/4694145045) [#58646](https://github.com/vllm-project/vllm/pull/58646) — [Skills] Update kernel-microbenchmark to include ROCm (#58646)
- **2026-09-28** [`55de40a2fc`](https://github.com/vllm-project/vllm/commit/55de40a2fc) [#58673](https://github.com/vllm-project/vllm/pull/58673) — [Minimax-M3] Add Encoder CUDA graph support (#58673)
- **2026-09-28** [`77fbd9e225`](https://github.com/vllm-project/vllm/commit/77fbd9e225) [#58945](https://github.com/vllm-project/vllm/pull/58945) — [Test][ROCm] Stabilize the mixed OLMoE LoRA test (#58945)
- **2026-09-28** [`31afa4f1bb`](https://github.com/vllm-project/vllm/commit/31afa4f1bb) [#58867](https://github.com/vllm-project/vllm/pull/58867) — [ROCm] Bump AITER to v0.1.23 (#58867)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#56851](https://github.com/vllm-project/vllm/issues/56851) | [RFC]: Request level text and derender output on `/inference/v1/genera | RFC, kimi, k3 | 2026-10-05 |
| [#60072](https://github.com/vllm-project/vllm/issues/60072) | [Tracking] HiSparse | — | 2026-10-05 |
| [#56021](https://github.com/vllm-project/vllm/issues/56021) | [Bug]: On RDNA (gfx12), VLLM_ROCM_USE_AITER=1 force-selects ROCM_AITER | rocm, quantization | 2026-10-05 |
| [#58409](https://github.com/vllm-project/vllm/issues/58409) | [ROCm][Perf][Tracking Issue]: GLM-5.3-Flash | feature request, rocm, glm | 2026-10-05 |
| [#53488](https://github.com/vllm-project/vllm/issues/53488) | [Bug]: `prompt_logprobs` silently corrupted for some requests when MTP | speculative-decoding, quantization | 2026-10-05 |
| [#59575](https://github.com/vllm-project/vllm/issues/59575) | [ROCm][AMD] Qwen3.8-Flash-Next gfx950 / MI355X Performance Optimizatio | performance, rocm, quantization | 2026-10-05 |
| [#57149](https://github.com/vllm-project/vllm/issues/57149) | [ROCm][AMD] Qwen3.8-2.4T-A95B gfx950 / MI355X Performance Optimization | performance, rocm, quantization | 2026-10-05 |
| [#59708](https://github.com/vllm-project/vllm/issues/59708) | [RFC]: Modular and Extensible APIs & Execution Surface for Orchestrato | RFC | 2026-10-05 |
| [#51428](https://github.com/vllm-project/vllm/issues/51428) | [RFC]: Programmatic Session-Aware KV Cache Management | RFC | 2026-10-05 |
| [#59956](https://github.com/vllm-project/vllm/issues/59956) | [Bug]: NIXL: `remove_remote_agent` does not release UCX endpoints, so  | bug, kv-connector | 2026-10-05 |
| [#59413](https://github.com/vllm-project/vllm/issues/59413) | [Bug][ROCm]: GLM-5.3-Flash gibberish at low concurrency | bug, rocm, glm | 2026-10-05 |
| [#49497](https://github.com/vllm-project/vllm/issues/49497) | [Bug]: FlashInfer sampler JIT crashes engine startup when nvcc isn't d | bug | 2026-10-05 |
| [#60008](https://github.com/vllm-project/vllm/issues/60008) | [Performance]: Hybrid Mamba prefix caching (`mamba_cache_mode="align"` | performance | 2026-10-05 |
| [#60019](https://github.com/vllm-project/vllm/issues/60019) | [Bug]: P2P KV offload tier runs NIXL peer registration synchronously i | kv-connector, scheduler | 2026-10-05 |
| [#59055](https://github.com/vllm-project/vllm/issues/59055) | [RFC]: Release all releasable GPU memory in sleep mode (tracking) | feature request, rocm, kimi | 2026-10-05 |
| [#59784](https://github.com/vllm-project/vllm/issues/59784) | [Bug]: Qwen3-VL-Reranker fails to load because Qwen3VLTextConfig has n | bug | 2026-10-05 |
| [#59642](https://github.com/vllm-project/vllm/issues/59642) | [Bug]: Qwen3.8-flash-next 0% MTP acceptance rate in disaggregated PD s | bug, kv-connector | 2026-10-05 |
| [#59725](https://github.com/vllm-project/vllm/issues/59725) | [Feature]: Integrate Cake kernels via FlashInfer: model-by-model track | quantization, kimi | 2026-10-05 |
| [#59086](https://github.com/vllm-project/vllm/issues/59086) | [Bug]: VLLM_BATCH_INVARIANT=1 is not batch-invariant for AWQ models on | bug, quantization | 2026-10-05 |
| [#48312](https://github.com/vllm-project/vllm/issues/48312) | [RFC] Weight Reload Correctness for RL | rocm, RFC, quantization | 2026-10-05 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 94 |
| Other | 48 |
| Attention | 47 |
| Multimodal | 39 |
| Scheduler / Engine | 32 |
| Serving / API | 28 |
| CI / Build | 26 |
| Models | 25 |
| MoE / Expert Parallel | 23 |
| Disaggregation / PD | 20 |
| Speculative Decoding | 15 |
| Quantization | 14 |
| LoRA | 11 |
| KV Cache / Offload | 7 |
| Docs | 7 |
| Perf / Benchmark | 6 |
| Compilation / CUDA Graph | 4 |

## ROCm / AMD  (94 commits)

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
- **2026-10-04** [`f98d1fc493`](https://github.com/vllm-project/vllm/commit/f98d1fc493) [#59550](https://github.com/vllm-project/vllm/pull/59550)
  [ROCm][Bugfix] Fix ROCM_ATTN sliding-window boundary (#59550)
  _Files: `tests/kernels/attention/test_prefix_prefill.py`, `vllm/v1/attention/backends/rocm_attn.py`_
- **2026-10-04** [`d61081dc3d`](https://github.com/vllm-project/vllm/commit/d61081dc3d) [#59932](https://github.com/vllm-project/vllm/pull/59932)
  [CI] Bump peft to satisfy transformers 5.18 minimum (#59932)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/rocm.in` _+1 more__
- **2026-10-04** [`9e0b6fcf77`](https://github.com/vllm-project/vllm/commit/9e0b6fcf77) [#59621](https://github.com/vllm-project/vllm/pull/59621)
  [CI] Bump Transformers version to 5.18.0 (#59621)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+18 more__
- **2026-10-03** [`4ac0d0eac2`](https://github.com/vllm-project/vllm/commit/4ac0d0eac2) [#54706](https://github.com/vllm-project/vllm/pull/54706)
  [ROCm][RDNA3] Fix W4A16 split-K accuracy and determinism (#54706)
  _Files: `csrc/rocm/moe_q_gemm_rdna3.cu`, `csrc/rocm/q_gemm_rdna3.cu`, `csrc/rocm/q_gemm_rdna3_wmma.cu`, `csrc/rocm/qdq_4_rdna3.cuh` _+1 more__
- **2026-10-03** [`b0e21b3083`](https://github.com/vllm-project/vllm/commit/b0e21b3083) [#51274](https://github.com/vllm-project/vllm/pull/51274)
  [ROCm][Kimi-K3] Add opt-in gfx942 MXFP4-to-int4 conversion (#51274)
  _Files: `tests/models/kimi_k3/test_gfx942_int4.py`, `tests/quantization/test_quantization_config_args.py`, `vllm/config/quantization.py`, `vllm/model_executor/layers/quantization/mxfp4.py` _+1 more__
- **2026-10-03** [`c28834df00`](https://github.com/vllm-project/vllm/commit/c28834df00) [#56679](https://github.com/vllm-project/vllm/pull/56679)
  [ROCm][CI] Extend AMD coverage for distributed, model, and eval tests (#56679)
  _Files: `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/e2e_integration.yaml`, `.buildkite/test_areas/lm_eval.yaml` _+2 more__
- **2026-10-03** [`faa9860dbd`](https://github.com/vllm-project/vllm/commit/faa9860dbd) [#59333](https://github.com/vllm-project/vllm/pull/59333)
  [ROCm][CI][AiterExperts] Add test coverage for hidden/intermediate padding correctness (#59333)
  _Files: `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/test_modular_kernel_combinations.py`_
- **2026-10-02** [`111f71a6db`](https://github.com/vllm-project/vllm/commit/111f71a6db) [#54049](https://github.com/vllm-project/vllm/pull/54049)
  [feat] FlashInfer CuteDSL MegaMoE integration  (#54049)
  _Files: `docs/design/moe_kernel_features.md`, `docs/serving/expert_parallel_deployment.md`, `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/mhc/test_mhc_kernels.py` _+29 more__
- **2026-10-02** [`8882b83b34`](https://github.com/vllm-project/vllm/commit/8882b83b34) [#59796](https://github.com/vllm-project/vllm/pull/59796)
  [Bugfix] Bump tokenizers to 0.23.2 for duplicate-pattern support (#59796)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt` _+1 more__
- **2026-10-02** [`6abadc2aa7`](https://github.com/vllm-project/vllm/commit/6abadc2aa7) [#59332](https://github.com/vllm-project/vllm/pull/59332)
  [ROCm][CI] Add test coverage for VLLM_ROCM_MOE_PADDING memory-stride padding transparency (#59332)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/quantization.yaml`, `tests/rocm/test_moe_padding.py`_
- **2026-10-02** [`4c4003bb5f`](https://github.com/vllm-project/vllm/commit/4c4003bb5f) [#59455](https://github.com/vllm-project/vllm/pull/59455)
  [Bugfix] Bind routed-experts capture to the MoE layer, not the kernel (#59455)
  _Files: `tests/kernels/moe/test_flashinfer.py`, `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/kernels/moe/test_routed_experts_capture_monolithic.py`, `tests/model_executor/test_routed_experts_capture.py` _+28 more__
- **2026-10-02** [`e2cb5ee46c`](https://github.com/vllm-project/vllm/commit/e2cb5ee46c) [#53341](https://github.com/vllm-project/vllm/pull/53341)
  [CI] Replace shellcheck-suppressed patterns flagged in #52572 with clean equivalents (#53341)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `tools/install_torchcodec_rocm.sh`, `vllm/utils/numa_wrapper.sh`_
- **2026-10-02** [`98b29aa99a`](https://github.com/vllm-project/vllm/commit/98b29aa99a) [#58167](https://github.com/vllm-project/vllm/pull/58167)
  [ROCm][Perf][GLM-5.3-Flash] Add AITER topk backend for decodes (#58167)
  _Files: `benchmarks/kernels/benchmark_top_k_per_row_decode.py`, `tests/kernels/test_top_k_per_row.py`, `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/_aiter_ops.py` _+4 more__
- **2026-10-02** [`751fa96a49`](https://github.com/vllm-project/vllm/commit/751fa96a49) [#58569](https://github.com/vllm-project/vllm/pull/58569)
  [ROCm][Perf][GLM-5.3-Flash] Remove redundant copy after ragged sparse MLA (#58569)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-10-02** [`0154979656`](https://github.com/vllm-project/vllm/commit/0154979656) [#58344](https://github.com/vllm-project/vllm/pull/58344)
  [ROCm][Perf] Kimi-K3 enable prefill checkpoints on ROCm (#58344)
  _Files: `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/kda_metadata.py` _+3 more__
- **2026-10-02** [`e3cae8d2ac`](https://github.com/vllm-project/vllm/commit/e3cae8d2ac) [#57387](https://github.com/vllm-project/vllm/pull/57387)
  [Model] Use upstream GLM-5.3 and Qwen4-Exp configs and processor (#57387)
  _Files: `requirements/common.txt`, `tests/models/glm5next/test_sequence_parallel.py`, `tests/models/multimodal/processing/test_glm5next.py`, `tests/models/qwen4_exp/test_config.py` _+32 more__
- **2026-10-02** [`eec3c36a47`](https://github.com/vllm-project/vllm/commit/eec3c36a47) [#54805](https://github.com/vllm-project/vllm/pull/54805)
  [ROCm][BugFix] Revert AITER PA gluon decode from ROCM_AITER_FA (#54805)
  _Files: `vllm/v1/attention/backends/rocm_aiter_fa.py`_
- **2026-10-01** [`e6674262f1`](https://github.com/vllm-project/vllm/commit/e6674262f1) [#59700](https://github.com/vllm-project/vllm/pull/59700)
  [Bugfix][CI] Widen DBO+DP+EP GSM8K accuracy margin on ROCm (#59700)
  _Files: `tests/v1/distributed/test_dbo.py`_
- **2026-10-01** [`d2125ea681`](https://github.com/vllm-project/vllm/commit/d2125ea681) [#59666](https://github.com/vllm-project/vllm/pull/59666)
  [ROCm][CI] Raise the MI355 DeepSeek-R1 GSM8K startup wait to 1800s (#59666)
  _Files: `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml`_
- **2026-10-01** [`ccda9098cc`](https://github.com/vllm-project/vllm/commit/ccda9098cc) [#59593](https://github.com/vllm-project/vllm/pull/59593)
  [ROCm][CI] Drop two no-GPU AMD mirrors from the CPU test areas (#59593)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-10-01** [`d848c4ed3d`](https://github.com/vllm-project/vllm/commit/d848c4ed3d) [#58769](https://github.com/vllm-project/vllm/pull/58769)
  [ROCm][Triton] Migrate Kimi-K3 kernels from make_block_ptr to tensor … (#58769)
  _Files: `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk_intra_token_parallel.py`_
- **2026-10-01** [`26bfdfb6bc`](https://github.com/vllm-project/vllm/commit/26bfdfb6bc) [#57978](https://github.com/vllm-project/vllm/pull/57978)
  [ROCm][Perf] Parallelise AITER MLA page-index expansion over token chunks (#57978)
  _Files: `tests/v1/attention/test_expand_page_indices.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-10-01** [`08e03df940`](https://github.com/vllm-project/vllm/commit/08e03df940) [#59454](https://github.com/vllm-project/vllm/pull/59454)
  [Bugfix][ROCm] Use a zero default for masked scales in the MXFP8 GEMM (#59454)
  _Files: `vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py`_
- **2026-10-01** [`cfd54ca881`](https://github.com/vllm-project/vllm/commit/cfd54ca881) [#59595](https://github.com/vllm-project/vllm/pull/59595)
  [ROCm][CI] Drop four no-GPU CPU groups from the legacy AMD pipeline (#59595)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-10-01** [`cb6458c5ce`](https://github.com/vllm-project/vllm/commit/cb6458c5ce) [#58997](https://github.com/vllm-project/vllm/pull/58997)
  [Core] Remove deprecated mamba_cache_mode "all" (#58997)
  _Files: `tests/kernels/mamba/test_cpu_short_conv.py`, `tests/kernels/mamba/test_ssu_dispatch.py`, `tests/test_config.py`, `tests/v1/attention/test_mamba_metadata_builder.py` _+41 more__
- **2026-10-01** [`c4fc3c7d32`](https://github.com/vllm-project/vllm/commit/c4fc3c7d32) [#58921](https://github.com/vllm-project/vllm/pull/58921)
  [Bugfix][Spec Decode] Per-module LM heads for multi-layer MTP on Model Runner V2 (#58921)
  _Files: `vllm/model_executor/models/step3p5_mtp.py`, `vllm/models/inkling/amd/mtp.py`, `vllm/models/inkling/nvidia/mtp.py`, `vllm/v1/worker/gpu/spec_decode/eagle/utils.py` _+2 more__
- **2026-10-01** [`aee8fe202a`](https://github.com/vllm-project/vllm/commit/aee8fe202a) [#58887](https://github.com/vllm-project/vllm/pull/58887)
  [Bugfix][ROCm] Fix race on AITER MLA FP8 prefill scheduling metadata under async scheduling (#58887)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-10-01** [`4c2d277643`](https://github.com/vllm-project/vllm/commit/4c2d277643) [#59327](https://github.com/vllm-project/vllm/pull/59327)
  [Perf][DSv4.1] Faster Engram host lookups: sorted rows, inline big lookups (#59327)
  _Files: `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_engram.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/common/engram.py` _+2 more__
- **2026-10-01** [`76d3929916`](https://github.com/vllm-project/vllm/commit/76d3929916) [#55422](https://github.com/vllm-project/vllm/pull/55422)
  [Docker] Compile Python bytecode at image build time (#55422)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cpu`, `docker/Dockerfile.ppc64le`, `docker/Dockerfile.rock` _+4 more__
- **2026-10-01** [`df8fd42116`](https://github.com/vllm-project/vllm/commit/df8fd42116) [#55840](https://github.com/vllm-project/vllm/pull/55840)
  [CI][Spec Decode] Add async scheduling accuracy tests (#55840)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/engine.yaml`, `tests/v1/e2e/general/accuracy_utils.py`, `tests/v1/e2e/general/test_async_scheduling_accuracy.py`_
- **2026-09-30** [`26ce58b48c`](https://github.com/vllm-project/vllm/commit/26ce58b48c) [#59499](https://github.com/vllm-project/vllm/pull/59499)
  [ROCm][CI] Sync two AMD test groups between test-amd.yaml and test_areas (#59499)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/engine.yaml`_
- **2026-09-30** [`b56b54bc54`](https://github.com/vllm-project/vllm/commit/b56b54bc54) [#59477](https://github.com/vllm-project/vllm/pull/59477)
  [ROCm][CI] Relax simple-nemotron-h-8b GSM8K threshold on ROCm (#59477)
  _Files: `tests/evals/gsm8k/test_gsm8k_offloading.py`_
- **2026-09-30** [`ed3f6d1a56`](https://github.com/vllm-project/vllm/commit/ed3f6d1a56) [#59256](https://github.com/vllm-project/vllm/pull/59256)
  [ROCm][CI] Remove duplicate MI355 DPX jobs (#59256)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-30** [`b33e1cb172`](https://github.com/vllm-project/vllm/commit/b33e1cb172) [#59253](https://github.com/vllm-project/vllm/pull/59253)
  [ROCm]Transpose compressed-tensors MoE weights on device (#59253)
  _Files: `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-09-30** [`8f24ab30a3`](https://github.com/vllm-project/vllm/commit/8f24ab30a3) [#57640](https://github.com/vllm-project/vllm/pull/57640)
  [ROCm][Kimi-K3][Perf] Fuse MLA decode KV-cache write and Q-prep via AITER (#57640)
  _Files: `vllm/models/kimi_k3/amd/mla.py`_
- **2026-09-30** [`d2fb35f66e`](https://github.com/vllm-project/vllm/commit/d2fb35f66e) [#59237](https://github.com/vllm-project/vllm/pull/59237)
  [CI][ROCm] Drop the duplicate OAI Triton MoE run from FP8 MoE Kernels (#59237)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-30** [`42a3dd5fec`](https://github.com/vllm-project/vllm/commit/42a3dd5fec) [#59287](https://github.com/vllm-project/vllm/pull/59287)
  [ROcm][BugFix][The Rock] Update The Rock dockerfile to most recent Triton 3.8 (#59287)
  _Files: `docker/Dockerfile.rock_base`_
- **2026-09-30** [`c4df37dfcc`](https://github.com/vllm-project/vllm/commit/c4df37dfcc) [#59372](https://github.com/vllm-project/vllm/pull/59372)
  [ROCm][BugFix][The Rock] Fix mori build for the rock (#59372)
  _Files: `docker/Dockerfile.rock_base`_
- **2026-09-30** [`4e1182a3a6`](https://github.com/vllm-project/vllm/commit/4e1182a3a6) [#55368](https://github.com/vllm-project/vllm/pull/55368)
  [ROCm][MoE] Pad the AITER MoE intermediate size at allocation time, and round the expert-group count to a kernel that exists (#55368)
  _Files: `tests/kernels/moe/test_rocm_aiter_moe.py`, `tests/kernels/moe/test_rocm_aiter_num_expert_group.py`, `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`_
- **2026-09-30** [`2df122e65e`](https://github.com/vllm-project/vllm/commit/2df122e65e) [#58008](https://github.com/vllm-project/vllm/pull/58008)
  [ROCm][Perf][GLM-5.3-Flash] "Fit kpool top-k indices to AITER" with a single Triton kernel (#58008)
  _Files: `tests/v1/attention/test_rocm_glm5next_sparse.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-09-30** [`eef8b15d7c`](https://github.com/vllm-project/vllm/commit/eef8b15d7c) [#59427](https://github.com/vllm-project/vllm/pull/59427)
  [Security] Bump pyjwt and rand for remaining GHSAs (#59427)
  _Files: `requirements/test/cuda.in`, `requirements/test/rocm.in`, `requirements/test/xpu.in`, `requirements/test/xpu.txt` _+2 more__
- **2026-09-30** [`a4c4bb418e`](https://github.com/vllm-project/vllm/commit/a4c4bb418e) [#59315](https://github.com/vllm-project/vllm/pull/59315)
  [Security] Bump remaining Dependabot packages (excl. ignored) (#59315)
  _Files: `requirements/build/cpu.txt`, `requirements/build/cuda.txt`, `requirements/build/rock.txt`, `requirements/build/rocm.txt` _+15 more__
- **2026-09-30** [`91dab0eb7f`](https://github.com/vllm-project/vllm/commit/91dab0eb7f) [#58797](https://github.com/vllm-project/vllm/pull/58797)
  [ROCm][Perf] Allocate the pinned PLE prefetch buffer lazily (#58797)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/common/ngram_embedding.py`_
- **2026-09-30** [`50319916a3`](https://github.com/vllm-project/vllm/commit/50319916a3) [#59400](https://github.com/vllm-project/vllm/pull/59400)
  [ROCm][CI] Move Basic Models (Other) to MI355 (#59400)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`_
- **2026-09-30** [`16d4ac4ba3`](https://github.com/vllm-project/vllm/commit/16d4ac4ba3) [#58262](https://github.com/vllm-project/vllm/pull/58262)
  [ROCm][MoE] Support MiMo-V2.6 MXFP4 on gfx942 (#58262)
  _Files: `tests/models/quantization/test_mimo_v2_w4a16_routing.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a16_moe.py`_
- **2026-09-30** [`3627a6a124`](https://github.com/vllm-project/vllm/commit/3627a6a124) [#57979](https://github.com/vllm-project/vllm/pull/57979)
  [ROCm][Perf][GLM-5.3-Flash] Stride-aware decode KDA (#57979)
  _Files: `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/fused_recurrent.py`, `vllm/models/glm5next/amd/ops/third_party/kda/kernels.py`_
- **2026-09-30** [`8ee4069033`](https://github.com/vllm-project/vllm/commit/8ee4069033) [#58539](https://github.com/vllm-project/vllm/pull/58539)
  [ROCm][DSv4.1][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill (#58539)
  _Files: `vllm/models/deepseek_v41/amd/rocm.py`_
- **2026-09-30** [`fcd317cf33`](https://github.com/vllm-project/vllm/commit/fcd317cf33) [#58405](https://github.com/vllm-project/vllm/pull/58405)
  [ROCm][DSv4][Perf] Use the shared prefill chunk plan in the ROCm sparse prefill (#58405)
  _Files: `vllm/models/deepseek_v4/amd/rocm.py`_
- **2026-09-30** [`77e8b02c8d`](https://github.com/vllm-project/vllm/commit/77e8b02c8d) [#58819](https://github.com/vllm-project/vllm/pull/58819)
  [ROCm][Perf] Add opt-in a4w4 (FP4 activation) MoE for DeepSeek V4.1 on AITER (#58819)
  _Files: `tests/kernels/moe/test_rocm_aiter_moe.py`, `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/config.py` _+4 more__
- **2026-09-30** [`834ad456d3`](https://github.com/vllm-project/vllm/commit/834ad456d3) [#58916](https://github.com/vllm-project/vllm/pull/58916)
  [Refactor] Remove dead tests code (#58916)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_distributed.yaml`, `tests/compile/passes/test_fusion.py`, `tests/compile/passes/test_fusion_attn.py` _+13 more__
- **2026-09-30** [`a8e069f81b`](https://github.com/vllm-project/vllm/commit/a8e069f81b) [#58648](https://github.com/vllm-project/vllm/pull/58648)
  [Bugfix][MiniMax M3] Share target embeddings with MTP under PP (#58648)
  _Files: `tests/v1/worker/test_spec_decode_embed_sharing_pp.py`, `vllm/model_executor/models/utils.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/mtp.py` _+2 more__
- **2026-09-29** [`eec2a86b1e`](https://github.com/vllm-project/vllm/commit/eec2a86b1e) [#59249](https://github.com/vllm-project/vllm/pull/59249)
  [Security] Bump nltk, aiohttp, pillow, and datamodel-code-generator (#59249)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+5 more__
- **2026-09-29** [`5dd693122c`](https://github.com/vllm-project/vllm/commit/5dd693122c) [#51043](https://github.com/vllm-project/vllm/pull/51043)
  [MyPy][2/N] Fix mypy errors in small tests/ dirs (#51043)
  _Files: `tests/compile/passes/distributed/test_async_tp.py`, `tests/compile/passes/distributed/test_fusion_all_reduce.py`, `tests/compile/passes/distributed/test_sequence_parallelism.py`, `tests/compile/passes/test_fusion_attn.py` _+67 more__
- **2026-09-29** [`7aa8372ef7`](https://github.com/vllm-project/vllm/commit/7aa8372ef7) [#59262](https://github.com/vllm-project/vllm/pull/59262)
  [ROCm][CI] Run Basic Correctness Sleep Mode on MI300 for now (#59262)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/basic_correctness.yaml`_
- **2026-09-29** [`df4dbe46e7`](https://github.com/vllm-project/vllm/commit/df4dbe46e7) [#59227](https://github.com/vllm-project/vllm/pull/59227)
  [CI][ROCm] Increase timeouts for AMD MI300 jobs near their limits (#59227)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-09-29** [`467d81d9a0`](https://github.com/vllm-project/vllm/commit/467d81d9a0) [#56073](https://github.com/vllm-project/vllm/pull/56073)
  [ROCm] Upgrade MoRI version on rocm dockers required for WideEP DP16 DI CI enablement and fixes for combine API (#56073)
  _Files: `docker/Dockerfile.rock_base`, `docker/Dockerfile.rocm_base`, `tests/kernels/moe/test_mori_prepare_finalize.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/mori.py`_
- **2026-09-29** [`c3a4a36c20`](https://github.com/vllm-project/vllm/commit/c3a4a36c20) [#59201](https://github.com/vllm-project/vllm/pull/59201)
  [CI][ROCm] Fix stale basic_correctness path in Model Runner V2 Distributed (#59201)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-29** [`dfc8e0f3e2`](https://github.com/vllm-project/vllm/commit/dfc8e0f3e2) [#58019](https://github.com/vllm-project/vllm/pull/58019)
  [Frontend] Support strict MiMo-V2.6 tool calling (#58019)
  _Files: `docs/features/tool_calling.md`, `requirements/common.txt`, `requirements/rocm.txt`, `requirements/test/cpu.txt` _+13 more__
- **2026-09-29** [`05d89636fc`](https://github.com/vllm-project/vllm/commit/05d89636fc) [#58433](https://github.com/vllm-project/vllm/pull/58433)
  [ROCm][CI] Mirror generic GEMM-RS/AR on MI355 (#58433)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `tests/kernels/test_rocm_gemm_rs_ar.py`_
- **2026-09-29** [`3acddf01e7`](https://github.com/vllm-project/vllm/commit/3acddf01e7) [#58967](https://github.com/vllm-project/vllm/pull/58967)
  [Bugfix][ROCm] Keep Mooncake bootstrap ports bound during startup (#58967)
  _Files: `docs/features/mooncake_connector_usage.md`, `tests/v1/kv_connector/rocm_pd_accuracy_utils.py`, `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py` _+1 more__
- **2026-09-29** [`6ebb5bd64f`](https://github.com/vllm-project/vllm/commit/6ebb5bd64f) [#59137](https://github.com/vllm-project/vllm/pull/59137)
  [ROCm][CI] Expand MI355 mirrors and route MIG-sized jobs to DPX (#59137)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/jit_monitor.yaml` _+11 more__
- **2026-09-29** [`77d9cda688`](https://github.com/vllm-project/vllm/commit/77d9cda688) [#58904](https://github.com/vllm-project/vllm/pull/58904)
  [ROCm][Model][Bugfix] Fix GLM-5.2 shared-expert fusion and MTP on the ROCm DSA path (#58904)
  _Files: `vllm/models/deepseek_v32/amd/model.py`, `vllm/models/deepseek_v32/amd/mtp.py`_
- **2026-09-29** [`78fc1e6274`](https://github.com/vllm-project/vllm/commit/78fc1e6274) [#58284](https://github.com/vllm-project/vllm/pull/58284)
  [ROCm][CI] Add MI355 TP2 AR-RMS and B200 fusion mirrors (#58284)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/compile.yaml`, `tests/compile/fusions_e2e/test_tp2_ar_rms.py`, `tests/compile/fusions_e2e/test_tp2_rocm_moe.py`_
- **2026-09-29** [`69d5c81fcd`](https://github.com/vllm-project/vllm/commit/69d5c81fcd) [#58654](https://github.com/vllm-project/vllm/pull/58654)
  [ROCm][CI] Mirror split kernel groups on MI355 and fix exposed tests (#58654)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/quantization.yaml`, `tests/kernels/test_bf16_skinny_gemm.py` _+2 more__
- **2026-09-29** [`0ae480ff1a`](https://github.com/vllm-project/vllm/commit/0ae480ff1a) [#58683](https://github.com/vllm-project/vllm/pull/58683)
  [CI][ROCm] Mirror large-model GSM8K evaluations on MI355 (#58683)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-R1-TP_MI355.yaml` _+10 more__
- **2026-09-29** [`63b9931b73`](https://github.com/vllm-project/vllm/commit/63b9931b73) [#58671](https://github.com/vllm-project/vllm/pull/58671)
  [ROCm][DSv4.1] Paged MXFP4 sparse indexer on aiter's MQA-logits kernel (#58671)
  _Files: `tests/kernels/attention/test_rocm_paged_mxfp4_indexer.py`, `tests/v1/attention/test_rocm_paged_mxfp4_indexer_plan.py`, `vllm/config/attention.py`, `vllm/model_executor/layers/rocm_paged_mxfp4_indexer.py` _+5 more__
- **2026-09-29** [`491f44adfa`](https://github.com/vllm-project/vllm/commit/491f44adfa) [#51289](https://github.com/vllm-project/vllm/pull/51289)
  [Model] Extend device-side mm normalization to Qwen3VL/Qwen3.5/Qwen4Next (#51289)
  _Files: `docs/design/mm_processing.md`, `tests/models/multimodal/generation_ppl_test/ppl_utils.py`, `tests/models/multimodal/generation_ppl_test/test_qwen.py`, `vllm/model_executor/models/colqwen3.py` _+7 more__
- **2026-09-29** [`cf971b419a`](https://github.com/vllm-project/vllm/commit/cf971b419a) [#59125](https://github.com/vllm-project/vllm/pull/59125)
  [Bugfix] Revert "[ROCm][Perf] Replace torch.topk in DSA candidate block selection" (#59125)
  _Files: `vllm/model_executor/kernels/attention/dsa/candidate_blocks.py`_
- **2026-09-29** [`0af34418e9`](https://github.com/vllm-project/vllm/commit/0af34418e9) [#58655](https://github.com/vllm-project/vllm/pull/58655)
  [ROCm][DSv4.1][Perf] Run the delayed mHC seams through aiter's fused Triton kernel (#58655)
  _Files: `tests/kernels/mhc/test_mhc_kernels.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/kernels/mhc/__init__.py`, `vllm/model_executor/kernels/mhc/aiter.py` _+2 more__
- **2026-09-29** [`70ae0b7435`](https://github.com/vllm-project/vllm/commit/70ae0b7435) [#53492](https://github.com/vllm-project/vllm/pull/53492)
  [ROCm][MLA] Enable sparse MLA Gluon kernel from Aiter (#53492)
  _Files: `tests/v1/attention/test_rocm_aiter_triton_sparse_mla.py`, `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/models/deepseek_v4/amd/rocm.py` _+3 more__
- **2026-09-28** [`75fad5bbef`](https://github.com/vllm-project/vllm/commit/75fad5bbef) [#58058](https://github.com/vllm-project/vllm/pull/58058)
  [Bugfix][ROCm] Drop -1 sentinels when building the ragged sparse-MLA indices (#58058)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-09-28** [`8a497d7557`](https://github.com/vllm-project/vllm/commit/8a497d7557) [#52395](https://github.com/vllm-project/vllm/pull/52395)
  [CI/Build][BugFix][The Rock] Make supports_mm_prefix  return False for ROCm attn and unified attn since Prefix-LM not implemented (#52395)
  _Files: `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`, `vllm/v1/attention/backends/rocm_attn.py`_
- **2026-09-28** [`beef814e1d`](https://github.com/vllm-project/vllm/commit/beef814e1d) [#50519](https://github.com/vllm-project/vllm/pull/50519)
  [ROCm][CI] Add missing test coverage for upstream parity (#50519)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/kernels.yaml` _+7 more__
- **2026-09-28** [`25624f65cf`](https://github.com/vllm-project/vllm/commit/25624f65cf) [#56861](https://github.com/vllm-project/vllm/pull/56861)
  [ROCm][MLA] Add an AITER ASM round-robin decode route for DCP multi-token verify (#56861)
  _Files: `tests/v1/attention/test_rocm_aiter_mla_dcp_cprr.py`, `tests/v1/attention/test_rocm_aiter_mla_dcp_cprr_numerics.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/envs.py` _+1 more__
- **2026-09-28** [`5ba2e3090b`](https://github.com/vllm-project/vllm/commit/5ba2e3090b) [#59076](https://github.com/vllm-project/vllm/pull/59076)
  [ROCm][CI] Increase timeout for Entrypoints Unit (#59076)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-28** [`7a160c6fe5`](https://github.com/vllm-project/vllm/commit/7a160c6fe5) [#59051](https://github.com/vllm-project/vllm/pull/59051)
  [ROCm][CI] Pin OpenTelemetry to LMCache's cap in the ROCm images (#59051)
  _Files: `docker/Dockerfile.rock`, `docker/Dockerfile.rocm`_
- **2026-09-28** [`b0d2b854f6`](https://github.com/vllm-project/vllm/commit/b0d2b854f6) [#59056](https://github.com/vllm-project/vllm/pull/59056)
  [ROCm]Keep LMCache OpenTelemetry on the image's 1.40 stack (#59056)
  _Files: `docker/Dockerfile.rock`, `docker/Dockerfile.rocm`_
- **2026-09-28** [`6b24bd8e75`](https://github.com/vllm-project/vllm/commit/6b24bd8e75) [#58208](https://github.com/vllm-project/vllm/pull/58208)
  [ROCm][Perf] Replace torch.topk in DSA candidate block selection (#58208)
  _Files: `vllm/model_executor/kernels/attention/dsa/candidate_blocks.py`_
- **2026-09-28** [`a7ff44355c`](https://github.com/vllm-project/vllm/commit/a7ff44355c) [#54956](https://github.com/vllm-project/vllm/pull/54956)
  [ROCm][Perf] Kimi-K3 Enable sharded latent MoE up-projection under EP (#54956)
  _Files: `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`_
- **2026-09-28** [`7ba3df63cb`](https://github.com/vllm-project/vllm/commit/7ba3df63cb) [#58983](https://github.com/vllm-project/vllm/pull/58983)
  [ROCm][Refactor] Move DeepSeek-V4/V4.1 multi-stream overlap gate to ROCm platform (#58983)
  _Files: `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/platforms/interface.py`, `vllm/platforms/rocm.py`_
- **2026-09-28** [`20b52e9f5b`](https://github.com/vllm-project/vllm/commit/20b52e9f5b) [#58114](https://github.com/vllm-project/vllm/pull/58114)
  [Perf][Qwen3.8] Reduce PLE metadata construction overhead (#58114)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/amd/ple_layer.py`, `vllm/models/qwen4_exp/nvidia/ple_layer.py`, `vllm/v1/attention/backends/mamba_attn.py` _+1 more__
- **2026-09-28** [`f6877f563c`](https://github.com/vllm-project/vllm/commit/f6877f563c) [#57568](https://github.com/vllm-project/vllm/pull/57568)
  [Bugfix][Spec Decode] Implement get_top_tokens() on the ROCm DeepSeek V4 MTP drafter (#57568)
  _Files: `tests/v1/spec_decode/test_dsv4_mtp_local_argmax.py`, `vllm/models/deepseek_v4/amd/mtp.py`_
- **2026-09-28** [`252279314b`](https://github.com/vllm-project/vllm/commit/252279314b) [#58652](https://github.com/vllm-project/vllm/pull/58652)
  Revert "[CI] Shard (H200 MIG 35GB / MI355 DPX) Entrypoints Integration (Pooling) into named jobs (#58652)" (#59011)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `tests/entrypoints/pooling/scoring/bi_encoder/__init__.py`, `tests/entrypoints/pooling/scoring/cross_encoder/__init__.py`, `tests/entrypoints/pooling/scoring/late_interaction/__init__.py` _+18 more__
- **2026-09-28** [`66d2d4b2e7`](https://github.com/vllm-project/vllm/commit/66d2d4b2e7) [#58451](https://github.com/vllm-project/vllm/pull/58451)
  [CI] Split Dynamic Shapes out of (H200 MIG 35GB) PyTorch Compilation + (MI300) mirror (#58451)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/pytorch.yaml`, `tests/compile/dynamic_shapes/__init__.py`, `tests/compile/dynamic_shapes/test_dynamic_shapes_compilation.py`_
- **2026-09-28** [`413ae4b167`](https://github.com/vllm-project/vllm/commit/413ae4b167) [#58652](https://github.com/vllm-project/vllm/pull/58652)
  [CI] Shard (H200 MIG 35GB / MI355 DPX) Entrypoints Integration (Pooling) into named jobs (#58652)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `tests/entrypoints/pooling/basic/test_factories.py`, `tests/entrypoints/pooling/basic/test_io_processor.py`, `tests/entrypoints/pooling/basic/test_utils.py` _+18 more__
- **2026-09-28** [`4694145045`](https://github.com/vllm-project/vllm/commit/4694145045) [#58646](https://github.com/vllm-project/vllm/pull/58646)
  [Skills] Update kernel-microbenchmark to include ROCm (#58646)
  _Files: `.agents/skills/kernel-microbenchmark/SKILL.md`, `.agents/skills/kernel-microbenchmark/benchmarks/graph_replay_benchmark.py`_
- **2026-09-28** [`55de40a2fc`](https://github.com/vllm-project/vllm/commit/55de40a2fc) [#58673](https://github.com/vllm-project/vllm/pull/58673)
  [Minimax-M3] Add Encoder CUDA graph support (#58673)
  _Files: `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/common/encoder_cudagraph.py`, `vllm/models/minimax_m3/common/vision_tower.py` _+1 more__
- **2026-09-28** [`77fbd9e225`](https://github.com/vllm-project/vllm/commit/77fbd9e225) [#58945](https://github.com/vllm-project/vllm/pull/58945)
  [Test][ROCm] Stabilize the mixed OLMoE LoRA test (#58945)
  _Files: `tests/lora/test_olmoe_tp.py`_
- **2026-09-28** [`31afa4f1bb`](https://github.com/vllm-project/vllm/commit/31afa4f1bb) [#58867](https://github.com/vllm-project/vllm/pull/58867)
  [ROCm] Bump AITER to v0.1.23 (#58867)
  _Files: `docker/Dockerfile.rock_base`, `docker/Dockerfile.rocm_base`, `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a16_moe.py`_

## Other  (48 commits)

- **2026-10-05** [`54d93af9fb`](https://github.com/vllm-project/vllm/commit/54d93af9fb) [#59688](https://github.com/vllm-project/vllm/pull/59688)
  [Bugfix][HiSparse] Reject cudagraph_mode=FULL at startup (#59688)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-10-05** [`f2d8fbf459`](https://github.com/vllm-project/vllm/commit/f2d8fbf459) [#60056](https://github.com/vllm-project/vllm/pull/60056)
  [CI/Build] Run the prefill token scoring test under batch invariance (#60056)
  _Files: `tests/v1/sample/test_logprobs.py`_
- **2026-10-05** [`60932a6401`](https://github.com/vllm-project/vllm/commit/60932a6401) [#58709](https://github.com/vllm-project/vllm/pull/58709)
  [Bugfix][Structured Output] Preserve literal values in Guidance disable_additional_properties (#58709)
  _Files: `tests/v1/structured_output/test_backend_guidance.py`, `vllm/v1/structured_output/backend_guidance.py`_
- **2026-10-04** [`155488d853`](https://github.com/vllm-project/vllm/commit/155488d853) [#59106](https://github.com/vllm-project/vllm/pull/59106)
  [Bugfix][Determinism] Preserve output dtype in batch-invariant mean (#59106)
  _Files: `vllm/model_executor/determinism/batch_invariant.py`_
- **2026-10-03** [`28556f8600`](https://github.com/vllm-project/vllm/commit/28556f8600) [#59661](https://github.com/vllm-project/vllm/pull/59661)
  [Bugfix] Log CRIU failure details before snapshot cleanup (#59661)
  _Files: `tests/entrypoints/launchers/test_launch_cli.py`, `vllm/snapshot/runtime.py`_
- **2026-10-02** [`8e58ac22af`](https://github.com/vllm-project/vllm/commit/8e58ac22af) [#59158](https://github.com/vllm-project/vllm/pull/59158)
  [Feature] Offload KV-init runtime state on sleep (#59158)
  _Files: `tests/basic_correctness/memory/cumem/test_cumem.py`, `vllm/device_allocator/sleep_mode_backend.py`, `vllm/v1/worker/gpu_model_runner.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-10-02** [`866f02db8a`](https://github.com/vllm-project/vllm/commit/866f02db8a) [#59156](https://github.com/vllm-project/vllm/pull/59156)
  [Feature] Release WorkspaceManager scratch on sleep (#59156)
  _Files: `tests/basic_correctness/memory/cumem/test_cumem.py`, `vllm/device_allocator/__init__.py`, `vllm/device_allocator/cumem.py`, `vllm/device_allocator/xpumem.py` _+2 more__
- **2026-10-02** [`e5d33a36e7`](https://github.com/vllm-project/vllm/commit/e5d33a36e7) [#59654](https://github.com/vllm-project/vllm/pull/59654)
  [Bugfix][Rust Frontend] Preserve whitespace in GLM string arguments (#59654)
  _Files: `rust/src/parser/src/tool/glm_xml/mod.rs`_
- **2026-10-02** [`6660926d92`](https://github.com/vllm-project/vllm/commit/6660926d92) [#58932](https://github.com/vllm-project/vllm/pull/58932)
  [Bugfix][CPU] Fix macOS build on Apple Clang < 17: structured binding… (#58932)
  _Files: `csrc/cpu/sgl-kernels/fla.cpp`_
- **2026-10-01** [`e35082e7b6`](https://github.com/vllm-project/vllm/commit/e35082e7b6) [#49821](https://github.com/vllm-project/vllm/pull/49821)
  [Bugfix][CLI] Include inherited field docstrings in get_attr_docs (#49821)
  _Files: `tests/config/test_config_utils.py`, `vllm/config/utils.py`_
- **2026-10-01** [`083060d046`](https://github.com/vllm-project/vllm/commit/083060d046) [#59641](https://github.com/vllm-project/vllm/pull/59641)
  [CI/Build] Add agents auto-label rule (#59641)
  _Files: `.github/mergify.yml`_
- **2026-10-01** [`3a69636645`](https://github.com/vllm-project/vllm/commit/3a69636645) [#59494](https://github.com/vllm-project/vllm/pull/59494)
  [Bugfix][HiSparse] Fix a chunked-prefill preemption livelock (#59494)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/single_type_kv_cache_manager.py`, `vllm/v1/hisparse/coordinator.py`_
- **2026-10-01** [`362cfb72de`](https://github.com/vllm-project/vllm/commit/362cfb72de) [#59638](https://github.com/vllm-project/vllm/pull/59638)
  [Agents] Expose PR checklist skill to Claude (#59638)
  _Files: `.claude/skills/pr-checklist`_
- **2026-10-01** [`08d77cad7b`](https://github.com/vllm-project/vllm/commit/08d77cad7b) [#59257](https://github.com/vllm-project/vllm/pull/59257)
  [Bugfix] Gate Kimi-K3 KDA warmup on sys.modules to skip Kimi import for non-Kimi models (#59257)
  _Files: `vllm/model_executor/warmup/kimi_k3_triton_warmup.py`_
- **2026-10-01** [`24fb5fc08c`](https://github.com/vllm-project/vllm/commit/24fb5fc08c) [#59005](https://github.com/vllm-project/vllm/pull/59005)
  [Rust Frontend] Add `hf` parser for response templates (#59005)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/lib.rs` _+19 more__
- **2026-10-01** [`e12b735109`](https://github.com/vllm-project/vllm/commit/e12b735109) [#57780](https://github.com/vllm-project/vllm/pull/57780)
  [Test] Make Anthropic messages test compatible with SDK 1.x via extra_body (#57780)
  _Files: `tests/entrypoints/anthropic/test_messages.py`_
- **2026-10-01** [`37cecc8141`](https://github.com/vllm-project/vllm/commit/37cecc8141) [#59491](https://github.com/vllm-project/vllm/pull/59491)
  [Bugfix][Tokenizer] Fix off-by-one max_token_id from vocab_size (#59491)
  _Files: `tests/tokenizers_/test_hf.py`, `vllm/tokenizers/hf.py`_
- **2026-10-01** [`b2d3a3b9ad`](https://github.com/vllm-project/vllm/commit/b2d3a3b9ad) [#59395](https://github.com/vllm-project/vllm/pull/59395)
  [Rust Frontend] Split argument grammars into schema resolution and per-model rendering (#59395)
  _Files: `rust/src/chat/tests/grammar_replay/Kimi-K3.json`, `rust/src/chat/tests/grammar_replay/Kimi-K3.txt`, `rust/src/parser/src/output_grammar.rs`, `rust/src/parser/src/output_grammar/arguments.rs` _+1 more__
- **2026-10-01** [`36229e1337`](https://github.com/vllm-project/vllm/commit/36229e1337) [#58358](https://github.com/vllm-project/vllm/pull/58358)
  [Rust Frontend] Token-aware marker parsing for Kimi K3 (#58358)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/parser/unified.rs`, `rust/src/parser/Cargo.toml` _+4 more__
- **2026-10-01** [`ec5ef92c87`](https://github.com/vllm-project/vllm/commit/ec5ef92c87) [#58357](https://github.com/vllm-project/vllm/pull/58357)
  [Rust Frontend] Anchor tokens after pending UTF-8 bytes at their own first byte (#58357)
  _Files: `rust/src/tokenizer/src/incremental.rs`, `rust/src/tokenizer/src/incremental/attribution/tests.rs`_
- **2026-10-01** [`2eaa3bc5ac`](https://github.com/vllm-project/vllm/commit/2eaa3bc5ac) [#58603](https://github.com/vllm-project/vllm/pull/58603)
  [Frontend] Enrich chat_parsing streaming events (#58603)
  _Files: `tests/parser/test_chat_parsing.py`, `vllm/parser/chat_parsing/response_parser.py`_
- **2026-10-01** [`bfbcde26d5`](https://github.com/vllm-project/vllm/commit/bfbcde26d5) [#52141](https://github.com/vllm-project/vllm/pull/52141)
  [Observability] add model initializing duration log (#52141)
  _Files: `vllm/model_executor/model_loader/base_loader.py`_
- **2026-10-01** [`9e6550bd05`](https://github.com/vllm-project/vllm/commit/9e6550bd05) [#58756](https://github.com/vllm-project/vllm/pull/58756)
  [Bugfix] Register IR providers before hashing configuration (#58756)
  _Files: `tests/config/test_config_utils.py`, `vllm/config/kernel.py`_
- **2026-10-01** [`bc505fc823`](https://github.com/vllm-project/vllm/commit/bc505fc823) [#59480](https://github.com/vllm-project/vllm/pull/59480)
  [Bugfix] Support CuTe DSL 4.8.0 block-scale API (#59480)
  _Files: `vllm/cute_utils/_tcgen05.py`_
- **2026-09-30** [`3eb6cec22a`](https://github.com/vllm-project/vllm/commit/3eb6cec22a) [#59282](https://github.com/vllm-project/vllm/pull/59282)
  [Bugfix][HiSparse] Adopt GPU prefix copies after the hit's allocation (#59282)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/hisparse/coordinator.py`_
- **2026-09-30** [`73a5831127`](https://github.com/vllm-project/vllm/commit/73a5831127) [#58602](https://github.com/vllm-project/vllm/pull/58602)
  [Frontend] Port chat_parsing core from Transformers (#58602)
  _Files: `tests/parser/test_chat_parsing.py`, `vllm/parser/chat_parsing/__init__.py`, `vllm/parser/chat_parsing/content_parsers.py`, `vllm/parser/chat_parsing/response_parser.py` _+1 more__
- **2026-09-30** [`ff1b87cca2`](https://github.com/vllm-project/vllm/commit/ff1b87cca2) [#59007](https://github.com/vllm-project/vllm/pull/59007)
  [Bugfix][HiSparse] Preserve host prefix publication after request completion (#59007)
  _Files: `tests/v1/core/test_prefix_caching.py`, `tests/v1/e2e/general/test_hisparse.py`, `vllm/v1/hisparse/coordinator.py`_
- **2026-09-30** [`fc2c801ad9`](https://github.com/vllm-project/vllm/commit/fc2c801ad9) [#59428](https://github.com/vllm-project/vllm/pull/59428)
  Disable mypy `arg-type` and `assignment` checks in tests (#59428)
- **2026-09-30** [`643bbef55c`](https://github.com/vllm-project/vllm/commit/643bbef55c) [#59200](https://github.com/vllm-project/vllm/pull/59200)
  [Refactor] Share workspace and model runner init between GPU and XPU workers (#59200)
  _Files: `vllm/v1/worker/gpu_worker.py`, `vllm/v1/worker/xpu_worker.py`_
- **2026-09-30** [`98b45c1a94`](https://github.com/vllm-project/vllm/commit/98b45c1a94) [#59139](https://github.com/vllm-project/vllm/pull/59139)
  [Feat] Support PP with PCP in GPU Model Runner V2 (#59139)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/pcp_manager.py`_
- **2026-09-30** [`02a3c6dfc5`](https://github.com/vllm-project/vllm/commit/02a3c6dfc5) [#59379](https://github.com/vllm-project/vllm/pull/59379)
  [Test] Skip IPC weight-transfer test on XPU platforms (#59379)
  _Files: `tests/entrypoints/serve/dev/rlhf/state_transitions/test_weight_checker.py`_
- **2026-09-30** [`5a4351ab09`](https://github.com/vllm-project/vllm/commit/5a4351ab09) [#59195](https://github.com/vllm-project/vllm/pull/59195)
  [MM] Keep device input normalization fused when encoder compilation is enabled (#59195)
  _Files: `tests/model_executor/layers/test_mm_input_norm.py`, `vllm/model_executor/layers/fusion/mm_input_norm.py`_
- **2026-09-30** [`5225f1bacb`](https://github.com/vllm-project/vllm/commit/5225f1bacb) [#55939](https://github.com/vllm-project/vllm/pull/55939)
  [MyPy][3/N] Fix MyPy errors in test groups (part 3) (#55939)
- **2026-09-30** [`ae66f9a97c`](https://github.com/vllm-project/vllm/commit/ae66f9a97c) [#58528](https://github.com/vllm-project/vllm/pull/58528)
  [Hardware][PowerPC] Prioritize bfloat16 for auto dtype on PowerPC (#58528)
  _Files: `vllm/config/model.py`_
- **2026-09-30** [`29773c722b`](https://github.com/vllm-project/vllm/commit/29773c722b) [#52314](https://github.com/vllm-project/vllm/pull/52314)
  [Observability] log sub process killing in process manager force kill (#52314)
  _Files: `vllm/utils/system_utils.py`_
- **2026-09-30** [`fcf4750466`](https://github.com/vllm-project/vllm/commit/fcf4750466) [#45290](https://github.com/vllm-project/vllm/pull/45290)
  [Bugfix][Frontend] Constrain forced named tool choice with empty parameters to a JSON object (#45290)
  _Files: `tests/tool_use/test_tool_choice_required.py`, `vllm/tool_parsers/utils.py`_
- **2026-09-30** [`6945d142e5`](https://github.com/vllm-project/vllm/commit/6945d142e5) [#59320](https://github.com/vllm-project/vllm/pull/59320)
  [XPU] Use encoder-only model runner for EC producer instances (#59320)
  _Files: `vllm/v1/worker/xpu_model_runner.py`, `vllm/v1/worker/xpu_worker.py`_
- **2026-09-30** [`90e13fc757`](https://github.com/vllm-project/vllm/commit/90e13fc757) [#59036](https://github.com/vllm-project/vllm/pull/59036)
  [Bugfix][HiSparse] Never allocate GPU pages without host backing (#59036)
  _Files: `tests/test_config.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_prefix_caching.py`, `tests/v1/e2e/general/test_hisparse.py` _+4 more__
- **2026-09-30** [`8039d3cbfd`](https://github.com/vllm-project/vllm/commit/8039d3cbfd) [#59148](https://github.com/vllm-project/vllm/pull/59148)
  [Rust Frontend] Use the MiMo structural-tag builder (#59148)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/parser/src/tool/mimo.rs`, `rust/src/parser/src/unified/kimi_k3/structural_tag.rs`_
- **2026-09-29** [`5e887a078b`](https://github.com/vllm-project/vllm/commit/5e887a078b) [#51810](https://github.com/vllm-project/vllm/pull/51810)
  [Bugfix] Route Step3p5 forced tool choices through XML parser (#51810)
  _Files: `tests/tool_parsers/test_step3p5_tool_parser.py`, `tests/tool_parsers/test_structural_tag_registry.py`, `vllm/tool_parsers/step3p5_tool_parser.py`_
- **2026-09-29** [`d882bddbea`](https://github.com/vllm-project/vllm/commit/d882bddbea) [#59146](https://github.com/vllm-project/vllm/pull/59146)
  [Bugfix][Mamba] Keep the prompt-end prefill checkpoint under sparse retention (#59146)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-09-29** [`1d331f8341`](https://github.com/vllm-project/vllm/commit/1d331f8341) [#59254](https://github.com/vllm-project/vllm/pull/59254)
  [Bugfix] Suppress HarmonyError Unexpected token while expecting start token 200006 (#59254)
  _Files: `tests/parser/test_harmony.py`, `vllm/parser/harmony.py`_
- **2026-09-29** [`19a4d66a0b`](https://github.com/vllm-project/vllm/commit/19a4d66a0b) [#47512](https://github.com/vllm-project/vllm/pull/47512)
  [Bugfix] Avoid JSON constraints for native tool parsers (#47512)
  _Files: `tests/tool_parsers/test_structural_tag_registry.py`, `vllm/tool_parsers/abstract_tool_parser.py`_
- **2026-09-29** [`f5ed3d9c03`](https://github.com/vllm-project/vllm/commit/f5ed3d9c03) [#57298](https://github.com/vllm-project/vllm/pull/57298)
  [Fast Start] Charge daemon-held weights against `gpu_memory_utilization` (#57298)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `tests/v1/worker/test_utils.py`, `vllm/model_executor/model_loader/base_loader.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py` _+3 more__
- **2026-09-29** [`208bb38c80`](https://github.com/vllm-project/vllm/commit/208bb38c80) [#58643](https://github.com/vllm-project/vllm/pull/58643)
  [Bugfix][Rust Frontend] Fix startup with config-only model (#58643)
  _Files: `tests/entrypoints/launchers/api_server/test_api_server_process_manager.py`, `vllm/v1/utils.py`_
- **2026-09-29** [`9af952c555`](https://github.com/vllm-project/vllm/commit/9af952c555) [#59020](https://github.com/vllm-project/vllm/pull/59020)
  [Bugfix][Rust Frontend] Support raise_exception in chat templates (#59020)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/chat/src/renderer/hf/mod.rs`, `rust/src/chat/src/renderer/hf/template.rs`, `rust/src/server/src/error.rs`_
- **2026-09-29** [`28f6739576`](https://github.com/vllm-project/vllm/commit/28f6739576) [#59004](https://github.com/vllm-project/vllm/pull/59004)
  [Rust Frontend] Relax schema-aware tool argument conversion (#59004)
  _Files: `rust/src/parser/src/tool/parameters.rs`_
- **2026-09-28** [`d7f5722d7b`](https://github.com/vllm-project/vllm/commit/d7f5722d7b) [#58747](https://github.com/vllm-project/vllm/pull/58747)
  [Bugfix][Logging] Preserve application log record factories (#58747)
  _Files: `tests/test_logger.py`, `vllm/logger.py`_

## Attention  (47 commits)

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
- **2026-10-04** [`bd42276e1e`](https://github.com/vllm-project/vllm/commit/bd42276e1e) [#58457](https://github.com/vllm-project/vllm/pull/58457)
  [Misc][Platform] Check aligned KV block sizes against every attention backend (#58457)
  _Files: `tests/v1/worker/test_gpu_model_runner.py`, `vllm/platforms/cpu.py`, `vllm/platforms/interface.py`, `vllm/platforms/xpu.py`_
- **2026-10-04** [`ce49174247`](https://github.com/vllm-project/vllm/commit/ce49174247) [#56891](https://github.com/vllm-project/vllm/pull/56891)
  [Bugfix] Fix FlashInfer all_reduce backend selection (#56891)
  _Files: `tests/distributed/test_comm_ops.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-10-03** [`84bcbc6264`](https://github.com/vllm-project/vllm/commit/84bcbc6264) [#59462](https://github.com/vllm-project/vllm/pull/59462)
  [DCP] Enable TokenSpeed MLA with block-interleaved DCP (#59462)
  _Files: `requirements/cuda.txt`, `tests/v1/attention/test_mla_backends.py`, `vllm/v1/attention/backends/mla/tokenspeed_mla.py`_
- **2026-10-03** [`8bdd8d847d`](https://github.com/vllm-project/vllm/commit/8bdd8d847d) [#57443](https://github.com/vllm-project/vllm/pull/57443)
  [GLM 5.3 Perf] Enable fused multi-step decode, 13.3% E2E throughput improvement for concurrency 1 (#57443)
  _Files: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `tests/v1/attention/test_kpool_tail_slot_mapping.py`, `tests/v1/spec_decode/test_eagle_draft_attn_metadata.py`, `tests/v1/worker/test_gpu_autoregressive_speculator.py` _+3 more__
- **2026-10-02** [`4e4d75c459`](https://github.com/vllm-project/vllm/commit/4e4d75c459) [#59464](https://github.com/vllm-project/vllm/pull/59464)
  [GLM5.3 Perf] Reuse sparse MLA index conversion across layers, 3.5~3.9x kernel performance improvement (#59464)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/backends/mla/flashattn_mla_sparse.py`_
- **2026-10-02** [`0979892992`](https://github.com/vllm-project/vllm/commit/0979892992) [#59126](https://github.com/vllm-project/vllm/pull/59126)
  [Bugfix][Multimodal] Fix GLM-5.3-Flash vision tower crashes on image input (#59126)
  _Files: `vllm/models/glm5next/common/multimodal.py`_
- **2026-10-02** [`af2a582d5c`](https://github.com/vllm-project/vllm/commit/af2a582d5c) [#59293](https://github.com/vllm-project/vllm/pull/59293)
  [Bugfix][Spec Decode] Qualify Transformers backend attention layer names with the model prefix (#59293)
  _Files: `tests/v1/e2e/spec_decode/draft_model/test_draft_model.py`, `vllm/model_executor/models/transformers/base.py`_
- **2026-10-02** [`4056c8ac1f`](https://github.com/vllm-project/vllm/commit/4056c8ac1f) [#59309](https://github.com/vllm-project/vllm/pull/59309)
  [Bugfix][HiSparse] Fix MTP acceptance collapse under FULL graphs with a saturated GPU pool (#59309)
  _Files: `docs/design/hisparse.md`, `tests/v1/attention/test_sparse_mla_backends.py`, `tests/v1/e2e/general/test_hisparse.py`, `tests/v1/kv_connector/unit/test_hisparse_connector.py` _+7 more__
- **2026-10-02** [`0cbac6cd13`](https://github.com/vllm-project/vllm/commit/0cbac6cd13) [#55902](https://github.com/vllm-project/vllm/pull/55902)
  [Model][Spec Decode] Enable EAGLE3/DSpark pipeline parallelism for Sarvam MLA (#55902)
  _Files: `vllm/model_executor/models/sarvam.py`_
- **2026-10-02** [`f7999d2e44`](https://github.com/vllm-project/vllm/commit/f7999d2e44) [#59450](https://github.com/vllm-project/vllm/pull/59450)
  [Bugfix][HiSparse] Size the KV cache from the groups HiSparse allocates (#59450)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/worker/test_attn_utils.py`, `vllm/v1/attention/backends/utils.py`, `vllm/v1/core/kv_cache_utils.py` _+4 more__
- **2026-10-02** [`8486f1ebfe`](https://github.com/vllm-project/vllm/commit/8486f1ebfe) [#52162](https://github.com/vllm-project/vllm/pull/52162)
  [Perf][PCP] Shard decode requests across PCP ranks (#52162)
  _Files: `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `tests/v1/attention/test_sparse_mla_backends.py`, `tests/v1/cudagraph/test_cudagraph_manager.py` _+9 more__
- **2026-10-01** [`7566d83bd3`](https://github.com/vllm-project/vllm/commit/7566d83bd3) [#59300](https://github.com/vllm-project/vllm/pull/59300)
  [Attention][MiniMax-M3] NVFP4 KV cache on the MSA sparse attention path (#59300)
  _Files: `CMakeLists.txt`, `cmake/external_projects/fmha_sm100.cmake`, `csrc/libtorch_stable/fused_minimax_m3_qknorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h` _+8 more__
- **2026-10-01** [`e9be5323f0`](https://github.com/vllm-project/vllm/commit/e9be5323f0) [#40337](https://github.com/vllm-project/vllm/pull/40337)
  [Perf] Integrate flash-maxsim Triton kernels for late-interaction scoring (#40337)
  _Files: `tests/v1/worker/test_late_interaction_runner.py`, `vllm/config/pooler.py`, `vllm/entrypoints/cli/serve.py`, `vllm/entrypoints/launchers/api_server/entry.py` _+6 more__
- **2026-10-01** [`b538d807ff`](https://github.com/vllm-project/vllm/commit/b538d807ff) [#59536](https://github.com/vllm-project/vllm/pull/59536)
  [Bugfix][MRV2] Keep GDN prefill checkpoint metadata local to each cache group (#59536)
  _Files: `tests/v1/attention/test_gdn_metadata_builder.py`, `vllm/model_executor/layers/mamba/checkpoint.py`, `vllm/v1/attention/backends/gdn_attn.py`_
- **2026-10-01** [`4d6874d137`](https://github.com/vllm-project/vllm/commit/4d6874d137) [#58845](https://github.com/vllm-project/vllm/pull/58845)
  [GLM 5.3 Perf] Skip qlnorm calculation for MHA, 4.4~7.7% E2E TTFT Improvement (#58845)
  _Files: `tests/kernels/test_fused_deepseek_v32_norm_rope.py`, `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `vllm/models/deepseek_v32/attention.py`, `vllm/models/deepseek_v32/common/kernels.py` _+1 more__
- **2026-10-01** [`87a4bf664f`](https://github.com/vllm-project/vllm/commit/87a4bf664f) [#58763](https://github.com/vllm-project/vllm/pull/58763)
  [Perf][GDN] Slice pure spec-decode rows instead of a host-mask gather (#58763)
  _Files: `tests/v1/attention/test_gdn_metadata_builder.py`, `vllm/v1/attention/backends/gdn_attn.py`_
- **2026-10-01** [`c9578f10ab`](https://github.com/vllm-project/vllm/commit/c9578f10ab) [#57097](https://github.com/vllm-project/vllm/pull/57097)
  [Qwen3.8-Flash-Next] Fuse main QK-norm/RoPE/gate and KV-cache write into the QSA pre-indexer launch (#57097)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/qwen4_exp/test_qsa_prepare.py`, `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/models/qwen4_exp/nvidia/indexer_qsa.py` _+2 more__
- **2026-10-01** [`ac9126e58a`](https://github.com/vllm-project/vllm/commit/ac9126e58a) [#59393](https://github.com/vllm-project/vllm/pull/59393)
  [Rust Frontend] Snapshot structural-tag grammars as readable outlines (#59393)
  _Files: `rust/src/chat/Cargo.toml`, `rust/src/chat/tests/grammar_replay/DeepSeek-V3.2-Exp.txt`, `rust/src/chat/tests/grammar_replay/DeepSeek-V4-Flash.txt`, `rust/src/chat/tests/grammar_replay/DeepSeek-V4.1-Flash.txt` _+14 more__
- **2026-10-01** [`766b4ae54c`](https://github.com/vllm-project/vllm/commit/766b4ae54c) [#54255](https://github.com/vllm-project/vllm/pull/54255)
  [Kimi-K3] Add FlashInfer speculative KDA backend (#54255)
  _Files: `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/utils/flashinfer.py`_
- **2026-10-01** [`edaf3e7b61`](https://github.com/vllm-project/vllm/commit/edaf3e7b61) [#58482](https://github.com/vllm-project/vllm/pull/58482)
  [Attention][SM120] Occupancy-adaptive Triton split-K segment count (#58482)
  _Files: `tests/v1/attention/test_triton_attn_segments.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/backends/triton_attn_diffkv.py`_
- **2026-09-30** [`deb148e730`](https://github.com/vllm-project/vllm/commit/deb148e730) [#52928](https://github.com/vllm-project/vllm/pull/52928)
  [Mamba] Add FlashInfer ReplaySSM support for MTP (#52928)
  _Files: `.buildkite/test_areas/engine.yaml`, `tests/kernels/mamba/test_ssu_dispatch.py`, `tests/model_executor/test_replayssm_warmup.py`, `tests/test_config.py` _+14 more__
- **2026-09-30** [`42f0c17ea7`](https://github.com/vllm-project/vllm/commit/42f0c17ea7) [#57197](https://github.com/vllm-project/vllm/pull/57197)
  [Bugfix][PP][Spec Decode] MiniMax-M3 EAGLE3 aux-state relay at PP > 1 and per-stage FlashInfer autotune (#57197)
  _Files: `tests/model_executor/test_flashinfer_autotune_warmup.py`, `tests/v1/worker/test_eagle3_aux_hidden_states_pp.py`, `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/models/minimax_m3/nvidia/model.py`_
- **2026-09-30** [`5463fe4962`](https://github.com/vllm-project/vllm/commit/5463fe4962) [#57652](https://github.com/vllm-project/vllm/pull/57652)
  [KV-Offloading][TP] : Expand replicated_layout detection to multi-group MLA  (#57652)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/config.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+6 more__
- **2026-09-30** [`93dd80f636`](https://github.com/vllm-project/vllm/commit/93dd80f636) [#54093](https://github.com/vllm-project/vllm/pull/54093)
  [CPU] Conv1d optimised kernel for aarch64 (#54093)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/sgl-kernels/conv.cpp`, `csrc/cpu/sgl-kernels/conv_arm.h`, `csrc/cpu/torch_bindings.cpp` _+5 more__
- **2026-09-30** [`df5668e5c9`](https://github.com/vllm-project/vllm/commit/df5668e5c9) [#57172](https://github.com/vllm-project/vllm/pull/57172)
  [XPU] Dispatch nn.LayerNorm to fused SYCL kernel via CustomOp (#57172)
  _Files: `vllm/_xpu_ops.py`, `vllm/model_executor/layers/layernorm.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/gpt2.py` _+9 more__
- **2026-09-30** [`87228cff01`](https://github.com/vllm-project/vllm/commit/87228cff01) [#59143](https://github.com/vllm-project/vllm/pull/59143)
  [Rust Frontend] Replay roundtrip output grammars through XGrammar (#59143)
  _Files: `rust/src/chat/Cargo.toml`, `rust/src/chat/tests/grammar_replay.py`, `rust/src/chat/tests/grammar_replay.rs`, `rust/src/chat/tests/grammar_replay/DeepSeek-V3.2-Exp.json` _+13 more__
- **2026-09-30** [`1117140edb`](https://github.com/vllm-project/vllm/commit/1117140edb) [#51994](https://github.com/vllm-project/vllm/pull/51994)
  [Bugfix][Model] Fix DiffusionGemma silently freezing attention mask under CUDA graph replay (#51994)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`, `vllm/v1/attention/backends/flash_attn.py`, `vllm/v1/attention/ops/triton_unified_attention.py`_
- **2026-09-30** [`2798f66860`](https://github.com/vllm-project/vllm/commit/2798f66860) [#59235](https://github.com/vllm-project/vllm/pull/59235)
  [Bugfix][HiSparse] Resolve MTP verification rows with a union residency kernel (#59235)
  _Files: `csrc/libtorch_stable/hisparse_kernels.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `docs/design/hisparse.md` _+9 more__
- **2026-09-30** [`678baf5372`](https://github.com/vllm-project/vllm/commit/678baf5372) [#59323](https://github.com/vllm-project/vllm/pull/59323)
  [Dependency] Upgrade FlashInfer to 0.7.0.post1 (#59323)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `requirements/cuda.txt`, `requirements/rubin-prerelease.txt`_
- **2026-09-29** [`c37f86e572`](https://github.com/vllm-project/vllm/commit/c37f86e572) [#55222](https://github.com/vllm-project/vllm/pull/55222)
  [Bugfix] GLM-5.3-Flash: fp8 plan dtype on SM90 sparse MLA, and right-size the indexer prefill workspace (#55222)
  _Files: `tests/v1/attention/test_flashinfer_mla_sparse_sm90.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/models/glm5next/common/attention.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse_sm90.py` _+1 more__
- **2026-09-29** [`faacc13565`](https://github.com/vllm-project/vllm/commit/faacc13565) [#57952](https://github.com/vllm-project/vllm/pull/57952)
  [Perf][KV Connector][Mooncake] Pack hybrid/MLA KV into coalesced transfer regions (#57952)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-09-29** [`cd947f5c62`](https://github.com/vllm-project/vllm/commit/cd947f5c62) [#58182](https://github.com/vllm-project/vllm/pull/58182)
  [MM] Fix compiled ViT attention output layouts (#58182)
  _Files: `tests/v1/attention/test_vit_attn_wrappers.py`, `vllm/v1/attention/ops/vit_attn_wrappers.py`_
- **2026-09-29** [`3e2a7e74a5`](https://github.com/vllm-project/vllm/commit/3e2a7e74a5) [#56960](https://github.com/vllm-project/vllm/pull/56960)
  [Feat][Model] Enable KDA prefill checkpoints for GLM-5.3-Flash (#56960)
  _Files: `tests/models/glm5next/test_kda_recurrent.py`, `tests/v1/attention/test_gdn_metadata_builder.py`, `vllm/model_executor/layers/mamba/checkpoint.py`, `vllm/models/glm5next/common/kda.py` _+2 more__
- **2026-09-29** [`65ed0a2642`](https://github.com/vllm-project/vllm/commit/65ed0a2642) [#55647](https://github.com/vllm-project/vllm/pull/55647)
  [Bugfix][GLM-5.3-Flash] Take video placeholder timestamps from the pixel path's frame sampler (#55647)
  _Files: `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`_
- **2026-09-29** [`35d6fb3187`](https://github.com/vllm-project/vllm/commit/35d6fb3187) [#58371](https://github.com/vllm-project/vllm/pull/58371)
  [Perf][Spec Decode] Enable fused multi-step draft decode for FlashInfer trtllm-gen (#58371)
  _Files: `tests/v1/attention/test_trtllm_attention_integration.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-09-29** [`1fde8ff7da`](https://github.com/vllm-project/vllm/commit/1fde8ff7da) [#58360](https://github.com/vllm-project/vllm/pull/58360)
  [Bugfix] Detect the CUDA toolkit the way FlashInfer does in has_flashinfer() (#58360)
  _Files: `tests/utils_/test_flashinfer_utils.py`, `vllm/utils/flashinfer.py`_
- **2026-09-28** [`754aa29c00`](https://github.com/vllm-project/vllm/commit/754aa29c00) [#58896](https://github.com/vllm-project/vllm/pull/58896)
  [XPU] use rms_norm xpu kernel for context-key normalization (#58896)
  _Files: `vllm/model_executor/models/qwen3_dflash.py`_
- **2026-09-28** [`764413559a`](https://github.com/vllm-project/vllm/commit/764413559a) [#58498](https://github.com/vllm-project/vllm/pull/58498)
  [Bugfix] Don't sync-police or retry FlashInfer all-reduce workspace creation in eager mode (#58498)
  _Files: `tests/distributed/test_comm_ops.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-09-28** [`6d3ea3c2c9`](https://github.com/vllm-project/vllm/commit/6d3ea3c2c9) [#50499](https://github.com/vllm-project/vllm/pull/50499)
  [KVConnector][NIXL] Support packed MLA KV layouts in pipeline-parallel push prefill (#50499)
  _Files: `docs/design/nixl_kv_push_connector.md`, `docs/features/nixl_connector_compatibility.md`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py` _+2 more__
- **2026-09-28** [`94d1462924`](https://github.com/vllm-project/vllm/commit/94d1462924) [#58814](https://github.com/vllm-project/vllm/pull/58814)
  [Bugfix][Kimi-K3] Refresh DSpark context KV cache pointers after the KV cache is re-bound (#58814)
  _Files: `vllm/models/kimi_k3/nvidia/dspark_mla.py`_
- **2026-09-28** [`522101f6ed`](https://github.com/vllm-project/vllm/commit/522101f6ed) [#56711](https://github.com/vllm-project/vllm/pull/56711)
  [Multimodal] Avoid extra d2d for encoder cudagraph with fused input norm (#56711)
  _Files: `vllm/model_executor/layers/fusion/mm_input_norm.py`, `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/v1/attention/ops/vit_attn_wrappers.py`_
- **2026-09-28** [`004e37ece2`](https://github.com/vllm-project/vllm/commit/004e37ece2) [#58557](https://github.com/vllm-project/vllm/pull/58557)
  [Misc] Name each backend and its kernel block sizes in block-size errors (#58557)
  _Files: `tests/v1/worker/test_attn_utils.py`, `tests/v1/worker/test_gpu_model_runner.py`, `vllm/v1/attention/backend.py`, `vllm/v1/worker/utils.py`_
- **2026-09-28** [`dd3bc9c72f`](https://github.com/vllm-project/vllm/commit/dd3bc9c72f) [#58762](https://github.com/vllm-project/vllm/pull/58762)
  [Perf][MRV2] Reuse Mamba/GDN metadata across KV cache groups (#58762)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`, `tests/v1/attention/test_gdn_metadata_builder.py`, `tests/v1/worker/test_gpu_autoregressive_speculator.py`, `vllm/v1/attention/backends/gdn_attn.py` _+1 more__

## Multimodal  (39 commits)

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
- **2026-10-04** [`0872ddf4b9`](https://github.com/vllm-project/vllm/commit/0872ddf4b9) [#56691](https://github.com/vllm-project/vllm/pull/56691)
  [Bugfix][Multimodal] Normalize single-channel audio to 1D (#56691)
  _Files: `tests/multimodal/test_audio.py`, `vllm/multimodal/audio.py`_
- **2026-10-03** [`8c3b720a4d`](https://github.com/vllm-project/vllm/commit/8c3b720a4d) [#59568](https://github.com/vllm-project/vllm/pull/59568)
  [TEST][XPU][CI] disable xpu tests for nonexistent input norm kernels (#59568)
  _Files: `.buildkite/intel_jobs/model_executor_intel.yaml`, `.buildkite/intel_jobs/models_multimodal_intel.yaml`_
- **2026-10-03** [`8e443871f0`](https://github.com/vllm-project/vllm/commit/8e443871f0) [#59288](https://github.com/vllm-project/vllm/pull/59288)
  [CI/Build][NVIDIA] Build Rubin images on the public nvidia/cuda base image (#59288)
  _Files: `.buildkite/release-pipeline.yaml`, `docker/Dockerfile`, `docs/getting_started/installation/gpu.cuda.inc.md`, `requirements/cuda.txt` _+1 more__
- **2026-10-02** [`f700178f90`](https://github.com/vllm-project/vllm/commit/f700178f90) [#59781](https://github.com/vllm-project/vllm/pull/59781)
  [Refactor] Remove dead env and config (#59781)
  _Files: `.buildkite/performance-benchmarks/tests/latency-tests-arm64-cpu.json`, `.buildkite/performance-benchmarks/tests/latency-tests-cpu.json`, `.buildkite/performance-benchmarks/tests/serving-tests-arm64-cpu.json`, `.buildkite/performance-benchmarks/tests/serving-tests-cpu-asr.json` _+12 more__
- **2026-10-02** [`7cfd233538`](https://github.com/vllm-project/vllm/commit/7cfd233538) [#53020](https://github.com/vllm-project/vllm/pull/53020)
  Revert "[Bugfix] Tie lm_head.weight for Nemotron Parse when checkpoint omits it" (#53020) (#59805)
  _Files: `tests/models/multimodal/generation/test_nemotron_parse.py`, `vllm/model_executor/models/nemotron_parse.py`_
- **2026-10-02** [`592c6f3fbc`](https://github.com/vllm-project/vllm/commit/592c6f3fbc) [#58975](https://github.com/vllm-project/vllm/pull/58975)
  [Bugfix][Pooling] Handle multimodal cache misses without crashing (#58975)
  _Files: `tests/entrypoints/pooling/scoring/test_io_processor_unit.py`, `tests/entrypoints/pooling/scoring/test_late_interaction_serving.py`, `tests/test_outputs.py`, `tests/v1/engine/test_llm_engine.py` _+17 more__
- **2026-10-02** [`443dccd3c9`](https://github.com/vllm-project/vllm/commit/443dccd3c9) [#59695](https://github.com/vllm-project/vllm/pull/59695)
  [Bugfix][Multimodal] Fix reference counting of the SHM processor cache (#59695)
  _Files: `tests/distributed/test_shm_storage.py`, `vllm/distributed/device_communicators/shm_object_storage.py`, `vllm/multimodal/cache/base.py`, `vllm/multimodal/cache/shm.py` _+1 more__
- **2026-10-02** [`5688a4dd4a`](https://github.com/vllm-project/vllm/commit/5688a4dd4a) [#59565](https://github.com/vllm-project/vllm/pull/59565)
  [Bugfix][GLM-5.3] Size the image encoder cache from the exact token ceiling (#59565)
  _Files: `tests/models/multimodal/processing/test_glm5next.py`, `vllm/models/glm5next/common/multimodal.py`_
- **2026-10-02** [`c15672cfb4`](https://github.com/vllm-project/vllm/commit/c15672cfb4) [#59417](https://github.com/vllm-project/vllm/pull/59417)
  [Security] Accept zero-sum DeepSeek-OCR pixel tensors (#59417)
  _Files: `tests/models/multimodal/processing/test_deepseek_ocr.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/deepseek_ocr2.py`_
- **2026-10-02** [`b558f160a2`](https://github.com/vllm-project/vllm/commit/b558f160a2) [#59613](https://github.com/vllm-project/vllm/pull/59613)
  [Bugfix] Fix minimax-m3 multimodal processor compatability with Transformers v5.18 (#59613)
  _Files: `vllm/transformers_utils/processors/minimax_m3.py`_
- **2026-10-02** [`ea106db806`](https://github.com/vllm-project/vllm/commit/ea106db806) [#59529](https://github.com/vllm-project/vllm/pull/59529)
  [Bugfix][Bench] Clean up synthetic video files and writers (#59529)
  _Files: `tests/benchmarks/test_random_multimodal_dataset_video.py`, `vllm/benchmarks/datasets/datasets.py`_
- **2026-10-01** [`7b44aad5db`](https://github.com/vllm-project/vllm/commit/7b44aad5db) [#59402](https://github.com/vllm-project/vllm/pull/59402)
  [MyPy] Fix mypy errors in `vllm/model_executor/models/[kK]*` (#59402)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/k2_horizon.py`, `vllm/model_executor/models/kanana_v.py`, `vllm/model_executor/models/keye.py` _+6 more__
- **2026-10-01** [`83cadd65d9`](https://github.com/vllm-project/vllm/commit/83cadd65d9) [#53020](https://github.com/vllm-project/vllm/pull/53020)
  [Bugfix] Tie lm_head.weight for Nemotron Parse when checkpoint omits it (#53020)
  _Files: `tests/models/multimodal/generation/test_nemotron_parse.py`, `vllm/model_executor/models/nemotron_parse.py`_
- **2026-09-30** [`51048b13ce`](https://github.com/vllm-project/vllm/commit/51048b13ce) [#59127](https://github.com/vllm-project/vllm/pull/59127)
  [Docs] Clarify snapshot runtime image support (#59127)
  _Files: `docs/features/initialized_snapshots.md`_
- **2026-09-30** [`a21a3f2ec7`](https://github.com/vllm-project/vllm/commit/a21a3f2ec7) [#59476](https://github.com/vllm-project/vllm/pull/59476)
  [CI] Add supports_multimodal_inputs to test_executor_replace's mock config (#59476)
  _Files: `tests/renderers/test_executor_replace.py`_
- **2026-09-30** [`17e9295dd5`](https://github.com/vllm-project/vllm/commit/17e9295dd5) [#59271](https://github.com/vllm-project/vllm/pull/59271)
  [BugFix][Multimodal] Pick worst-case DeepSeek-V4 VL dummy image size (#59271) (#59373)
  _Files: `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `vllm/models/deepseek_v4/common/mm_preprocess.py`_
- **2026-09-30** [`677e3f5d50`](https://github.com/vllm-project/vllm/commit/677e3f5d50) [#59426](https://github.com/vllm-project/vllm/pull/59426)
  [CI/Build] Fix pre-commit (#59426)
  _Files: `tests/multimodal/test_cache.py`_
- **2026-09-30** [`effdea9a53`](https://github.com/vllm-project/vllm/commit/effdea9a53) [#57168](https://github.com/vllm-project/vllm/pull/57168)
  [MM][Mistral] Add compile support for Pixtral vision encoders (#57168)
  _Files: `tests/compile/fullgraph/test_multimodal_compile.py`, `vllm/model_executor/models/pixtral.py`_
- **2026-09-30** [`3d5625cc3c`](https://github.com/vllm-project/vllm/commit/3d5625cc3c) [#59357](https://github.com/vllm-project/vllm/pull/59357)
  [Security] Authenticate shared-memory multimodal cache handles (#59357)
  _Files: `tests/distributed/test_shm_buffer.py`, `tests/distributed/test_shm_storage.py`, `tests/entrypoints/scale_out/token_in_token_out/test_generate_stream.py`, `tests/multimodal/test_cache.py` _+4 more__
- **2026-09-30** [`c4fa6f36a7`](https://github.com/vllm-project/vllm/commit/c4fa6f36a7) [#59399](https://github.com/vllm-project/vllm/pull/59399)
  [Tests][Multimodal] Cover scoped processor kwargs precedence (#59399)
  _Files: `tests/config/test_multimodal_config.py`_
- **2026-09-30** [`0a30bc3f9a`](https://github.com/vllm-project/vllm/commit/0a30bc3f9a) [#55389](https://github.com/vllm-project/vllm/pull/55389)
  [Model] Extend device-side mm normalization to GLM4V/GLM5Next (#55389)
  _Files: `docs/design/mm_processing.md`, `tests/models/multimodal/generation_ppl_test/test_glm.py`, `tests/models/multimodal/processing/test_glm5next.py`, `vllm/model_executor/models/glm4_1v.py` _+3 more__
- **2026-09-29** [`31876d8ea1`](https://github.com/vllm-project/vllm/commit/31876d8ea1) [#58364](https://github.com/vllm-project/vllm/pull/58364)
  [Bugfix] Fix TorchCodec audio IO correctness (#58364)
  _Files: `docs/features/multimodal_inputs.md`, `tests/multimodal/media/test_audio.py`, `vllm/multimodal/media/audio.py`_
- **2026-09-29** [`8aaeef343a`](https://github.com/vllm-project/vllm/commit/8aaeef343a) [#58938](https://github.com/vllm-project/vllm/pull/58938)
  [Bugfix][MiMo] Declare embedding_fields so an EPD pair can serve images (#58938)
  _Files: `vllm/model_executor/models/mimo_v2_omni.py`_
- **2026-09-29** [`ac7f3e11ea`](https://github.com/vllm-project/vllm/commit/ac7f3e11ea) [#57898](https://github.com/vllm-project/vllm/pull/57898)
  [Bugfix] Profile maximum DeepSeek V4.1 vision features (#57898)
  _Files: `vllm/models/deepseek_v41/common/mm_preprocess.py`_
- **2026-09-29** [`70dc122f81`](https://github.com/vllm-project/vllm/commit/70dc122f81) [#57928](https://github.com/vllm-project/vllm/pull/57928)
  [MM] Enable device normalization for Llama Nemotron VL Embed/Rerank (#57928)
  _Files: `docs/design/mm_processing.md`, `tests/models/multimodal/pooling/test_llama_nemotron_vl.py`, `vllm/model_executor/models/nemotron_vl.py`, `vllm/transformers_utils/processors/nemotron_vl.py`_
- **2026-09-29** [`d86cf91240`](https://github.com/vllm-project/vllm/commit/d86cf91240) [#57531](https://github.com/vllm-project/vllm/pull/57531)
  [MM][Mistral3] Image preprocessing optimization (#57531)
  _Files: `docs/design/mm_processing.md`, `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/layers/fusion/mm_input_norm.py`, `vllm/model_executor/models/lightonocr.py` _+2 more__
- **2026-09-29** [`295a0b8d64`](https://github.com/vllm-project/vllm/commit/295a0b8d64) [#56372](https://github.com/vllm-project/vllm/pull/56372)
  [Bugfix][Multimodal] Fix flat/scoped mm_processor_kwargs merge and resolution (#56372)
  _Files: `tests/config/test_multimodal_config.py`, `tests/models/multimodal/processing/test_gemma4.py`, `tests/models/multimodal/processing/test_mistral3.py`, `tests/models/multimodal/processing/test_qwen2_vl.py` _+7 more__
- **2026-09-29** [`07f1ba2ec6`](https://github.com/vllm-project/vllm/commit/07f1ba2ec6) [#59073](https://github.com/vllm-project/vllm/pull/59073)
  [Multimodal] Remove processsor fallback for fused input norm params resolve (#59073)
  _Files: `vllm/model_executor/layers/fusion/mm_input_norm.py`_
- **2026-09-29** [`aedaba8664`](https://github.com/vllm-project/vllm/commit/aedaba8664) [#59118](https://github.com/vllm-project/vllm/pull/59118)
  [CI/Build] Skip the snapshot runtime on CUDA 12.x images (#59118)
  _Files: `docker/Dockerfile`_
- **2026-09-28** [`2619b6b72b`](https://github.com/vllm-project/vllm/commit/2619b6b72b) [#58251](https://github.com/vllm-project/vllm/pull/58251)
  [Mypy] Fix mypy typing for Voxtral and vision models (#58251)
  _Files: `tests/models/multimodal/generation/test_voxtral_realtime.py`, `tools/pre_commit/mypy.py`, `vllm/model_executor/models/vision.py`, `vllm/model_executor/models/voxtral.py` _+1 more__
- **2026-09-28** [`cd63bf9996`](https://github.com/vllm-project/vllm/commit/cd63bf9996) [#57461](https://github.com/vllm-project/vllm/pull/57461)
  [Bugfix] Use the correct repository revision for secondary artifact loaders (#57461)
  _Files: `vllm/model_executor/models/funaudiochat.py`, `vllm/renderers/hf.py`_
- **2026-09-28** [`ccfd1cea75`](https://github.com/vllm-project/vllm/commit/ccfd1cea75) [#58796](https://github.com/vllm-project/vllm/pull/58796)
  [CPU] Include vLLM Recipes tooling in release image to deploy models using vLLM Recipes (#58796)
  _Files: `docker/Dockerfile.cpu`, `docs/getting_started/installation/cpu.x86.inc.md`, `docs/models/hardware_supported_models/cpu.md`, `tools/recipes/README.md`_
- **2026-09-28** [`fd2f3fcfa5`](https://github.com/vllm-project/vllm/commit/fd2f3fcfa5) [#58693](https://github.com/vllm-project/vllm/pull/58693)
  [CPU] Add video inferencing via torchcodec on s390x (#58693)
  _Files: `docker/Dockerfile.s390x`, `docs/getting_started/installation/cpu.s390x.inc.md`, `requirements/cpu.txt`_
- **2026-09-28** [`0da126676e`](https://github.com/vllm-project/vllm/commit/0da126676e) [#58900](https://github.com/vllm-project/vllm/pull/58900)
  [Bugfix] Fix the two multimodal root tests that fail on main (OpenPangu-VL embed merge, MiMo sink test fixture) (#58900)
  _Files: `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/openpangu_vl.py`_

## Scheduler / Engine  (32 commits)

- **2026-10-04** [`7867d6c52d`](https://github.com/vllm-project/vllm/commit/7867d6c52d) [#59889](https://github.com/vllm-project/vllm/pull/59889)
  [Frontend] Name the served models in the model-not-found 404 (#59889)
  _Files: `vllm/entrypoints/serve/engine/serving.py`_
- **2026-10-03** [`e319f86f15`](https://github.com/vllm-project/vllm/commit/e319f86f15) [#56984](https://github.com/vllm-project/vllm/pull/56984)
  [Feature] Per-row candidate IDs for prefill token scoring (M2 of #56860) (#56984)
  _Files: `docs/training/prompt_token_id_logprobs.md`, `rust/src/engine-core-client/src/protocol/request.rs`, `rust/src/engine-core-client/src/protocol/sampling.rs`, `rust/src/engine-core-client/src/protocol/tensor.rs` _+13 more__
- **2026-10-02** [`c4973d94fe`](https://github.com/vllm-project/vllm/commit/c4973d94fe) [#59015](https://github.com/vllm-project/vllm/pull/59015)
  [Bugfix][Frontend] Avoid generation for empty streaming input (#59015)
  _Files: `tests/v1/e2e/general/test_streaming_input.py`, `tests/v1/streaming_input/test_async_llm_streaming.py`, `vllm/v1/engine/async_llm.py`_
- **2026-10-02** [`f0c44cc7d5`](https://github.com/vllm-project/vllm/commit/f0c44cc7d5) [#57820](https://github.com/vllm-project/vllm/pull/57820)
  [Bugfix] Fix stalled local-only Elastic EP scale-up (#57820)
  _Files: `vllm/v1/engine/utils.py`_
- **2026-10-02** [`9d2a6f52b2`](https://github.com/vllm-project/vllm/commit/9d2a6f52b2) [#59659](https://github.com/vllm-project/vllm/pull/59659)
  [Rust Frontend] Expose gRPC port in Python vllm serve (#59659)
  _Files: `rust/README.md`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/server/examples/external_engine_openai_qwen.rs` _+7 more__
- **2026-10-02** [`fcfacc3499`](https://github.com/vllm-project/vllm/commit/fcfacc3499) [#59046](https://github.com/vllm-project/vllm/pull/59046)
  [Bugfix][Frontend] Seed derender detokenization from the prompt (#59046)
  _Files: `docs/serving/online_serving/derenderer.md`, `requirements/common.txt`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py` _+5 more__
- **2026-10-02** [`d58da79de7`](https://github.com/vllm-project/vllm/commit/d58da79de7) [#58874](https://github.com/vllm-project/vllm/pull/58874)
  [Metrics][P/D] Add KV-fetch stage gauges for async KV loads (#58874)
  _Files: `tests/v1/kv_connector/unit/test_remote_prefill_lifecycle.py`, `tests/v1/kv_connector/unit/utils.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/metrics/loggers.py` _+1 more__
- **2026-10-01** [`9aaef4296f`](https://github.com/vllm-project/vllm/commit/9aaef4296f) [#59555](https://github.com/vllm-project/vllm/pull/59555)
  [Bugfix][Frontend] Check reused prompt token ids against the vocab before streaming (#59555)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/renderers/base.py`, `vllm/renderers/online_renderer.py`, `vllm/v1/engine/input_processor.py`_
- **2026-10-01** [`4a9d6f9572`](https://github.com/vllm-project/vllm/commit/4a9d6f9572) [#55935](https://github.com/vllm-project/vllm/pull/55935)
  [Bugfix] Preserve sampling masks in DELTA and TITO streaming outputs (#55935)
  _Files: `docs/training/sampling_mask.md`, `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/inference/generate/types.rs`, `tests/entrypoints/scale_out/token_in_token_out/test_generate_stream.py` _+4 more__
- **2026-10-01** [`70be6aae19`](https://github.com/vllm-project/vllm/commit/70be6aae19) [#59359](https://github.com/vllm-project/vllm/pull/59359)
  [Feature][Spec Decode] Support sampling mask replay for MRV2 MTP (#59359)
  _Files: `docs/training/sampling_mask.md`, `tests/test_config.py`, `tests/v1/core/test_scheduler.py`, `tests/v1/engine/test_output_processor.py` _+9 more__
- **2026-10-01** [`7314360c9e`](https://github.com/vllm-project/vllm/commit/7314360c9e) [#58542](https://github.com/vllm-project/vllm/pull/58542)
  [Perf][PP] Skip sampled-token broadcasts whose requests leave the engine (#58542)
  _Files: `tests/v1/worker/test_gpu_batch_ordering.py`, `tests/v1/worker/test_pp_utils.py`, `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/model_runner.py` _+3 more__
- **2026-10-01** [`37d6174096`](https://github.com/vllm-project/vllm/commit/37d6174096) [#48867](https://github.com/vllm-project/vllm/pull/48867)
  [Metrics] Add --custom-histogram-buckets to override histogram bucket families (#48867)
  _Files: `docs/usage/metrics.md`, `tests/config/test_observability.py`, `tests/v1/engine/test_engine_args.py`, `tests/v1/metrics/test_histogram_buckets.py` _+4 more__
- **2026-09-30** [`7e583e615c`](https://github.com/vllm-project/vllm/commit/7e583e615c) [#59175](https://github.com/vllm-project/vllm/pull/59175)
  [Bugfix][Core] Fix mamba prefill checkpoint block reservation and prompt-end eviction in align mode (#59175)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/core/kv_cache_manager.py`, `vllm/v1/core/sched/scheduler.py` _+1 more__
- **2026-09-30** [`aba01ef1f7`](https://github.com/vllm-project/vllm/commit/aba01ef1f7) [#59338](https://github.com/vllm-project/vllm/pull/59338)
  [XPU][CI] Skip test_core_engine_actor_manager.py on Intel CI (#59338)
  _Files: `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-09-30** [`2e52a558f0`](https://github.com/vllm-project/vllm/commit/2e52a558f0) [#59029](https://github.com/vllm-project/vllm/pull/59029)
  [Bugfix][Core] Schedule encoder-only prompts larger than one step (#59029)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-09-30** [`f28a508162`](https://github.com/vllm-project/vllm/commit/f28a508162) [#59316](https://github.com/vllm-project/vllm/pull/59316)
  [Feature][Rust Frontend] Add Shutdown control RPC (#59316)
  _Files: `docs/usage/security.md`, `rust/proto/README.md`, `rust/proto/control.proto`, `rust/src/cmd/src/cli.rs` _+6 more__
- **2026-09-30** [`e5f3d08d72`](https://github.com/vllm-project/vllm/commit/e5f3d08d72) [#52864](https://github.com/vllm-project/vllm/pull/52864)
  [Frontend][RL] Align sleep-mode API responses and operation metrics (#52864)
  _Files: `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/metrics/src/api_server.rs`, `rust/src/server/src/middleware/metrics.rs`, `rust/src/server/src/routes/sleep.rs` _+10 more__
- **2026-09-30** [`866fa130fa`](https://github.com/vllm-project/vllm/commit/866fa130fa) [#58946](https://github.com/vllm-project/vllm/pull/58946)
  [Core] Bound UniProc EngineCore startup threads to available CPUs (#58946)
  _Files: `tests/v1/engine/test_startup_watch_processes.py`, `vllm/v1/engine/utils.py`_
- **2026-09-30** [`e006d761a5`](https://github.com/vllm-project/vllm/commit/e006d761a5) [#59107](https://github.com/vllm-project/vllm/pull/59107)
  [Bugfix][CPU][DiffusionGemma] Support narrower canvas w/ sync scheduling (#59107)
  _Files: `examples/features/structured_diffusion/README.md`, `tests/test_sampling_params.py`, `tests/v1/core/test_scheduler.py`, `vllm/config/vllm.py` _+3 more__
- **2026-09-30** [`42d9f8ccdb`](https://github.com/vllm-project/vllm/commit/42d9f8ccdb) [#51350](https://github.com/vllm-project/vllm/pull/51350)
  support rl feature : weight checker (#51350)
  _Files: `docs/training/rlhf.md`, `docs/training/weight_checker.md`, `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/tests.rs` _+11 more__
- **2026-09-29** [`a7a9ac2745`](https://github.com/vllm-project/vllm/commit/a7a9ac2745) [#59240](https://github.com/vllm-project/vllm/pull/59240)
  [Core] Combine per-engine utility results like the Rust client (#59240)
  _Files: `vllm/v1/engine/core_client.py`_
- **2026-09-29** [`91de237333`](https://github.com/vllm-project/vllm/commit/91de237333) [#57648](https://github.com/vllm-project/vllm/pull/57648)
  [Bugfix][DP] add_dp_placement_groups does not require ray[default] (#57648)
  _Files: `tests/v1/engine/test_core_engine_actor_manager.py`, `vllm/v1/engine/utils.py`_
- **2026-09-29** [`afac509a33`](https://github.com/vllm-project/vllm/commit/afac509a33) [#59205](https://github.com/vllm-project/vllm/pull/59205)
  [Bugfix][Rust Frontend] Skip engine-derived metrics under `--disable-log-stats` (#59205)
  _Files: `rust/src/bench/src/mm_processor.rs`, `rust/src/chat/examples/external_engine_chat_qwen.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/engine-core-client/examples/external_engine_logprobs.rs` _+12 more__
- **2026-09-29** [`3f3fbe286f`](https://github.com/vllm-project/vllm/commit/3f3fbe286f) [#58956](https://github.com/vllm-project/vllm/pull/58956)
  [Bugfix][Rust Frontend] Account for new requests in DP routing (#58956)
  _Files: `rust/src/engine-core-client/src/client/state.rs`_
- **2026-09-29** [`4861833ae2`](https://github.com/vllm-project/vllm/commit/4861833ae2) [#59060](https://github.com/vllm-project/vllm/pull/59060)
  [Bugfix][Core] Allow AuxOutput reset after abort without running requests (#59060)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-09-28** [`c68eb98b69`](https://github.com/vllm-project/vllm/commit/c68eb98b69) [#59017](https://github.com/vllm-project/vllm/pull/59017)
  [Bugfix][Frontend] Keep in-flight requests on the same DP engine (#59017)
  _Files: `tests/v1/engine/test_engine_core_client.py`, `vllm/v1/engine/core_client.py`_
- **2026-09-28** [`d28795f1a7`](https://github.com/vllm-project/vllm/commit/d28795f1a7) [#57676](https://github.com/vllm-project/vllm/pull/57676)
  [Bugfix][Scheduler] Refresh max tokens for streaming continuations (#57676)
  _Files: `tests/v1/streaming_input/test_scheduler_streaming.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-09-28** [`42dbe4578c`](https://github.com/vllm-project/vllm/commit/42dbe4578c) [#58947](https://github.com/vllm-project/vllm/pull/58947)
  [Core] Rework scheduler `skipped_waiting` queue (#58947)
  _Files: `rust/src/engine-core-client/src/protocol/stats.rs`, `tests/v1/core/test_scheduler.py`, `tests/v1/core/test_worker_slot_overflow.py`, `tests/v1/kv_connector/unit/test_error_propagation.py` _+9 more__
- **2026-09-28** [`2840ca7a33`](https://github.com/vllm-project/vllm/commit/2840ca7a33) [#57447](https://github.com/vllm-project/vllm/pull/57447)
  [Bugfix][Scheduler] Preserve logprobs across streaming continuations (#57447)
  _Files: `tests/v1/streaming_input/test_scheduler_streaming.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-09-28** [`2f4a975901`](https://github.com/vllm-project/vllm/commit/2f4a975901) [#58259](https://github.com/vllm-project/vllm/pull/58259)
  [Bugfix] Fix resumable request + async scheduling handoff race (#58259)
  _Files: `tests/v1/core/test_async_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-09-28** [`b721a4c709`](https://github.com/vllm-project/vllm/commit/b721a4c709) [#54335](https://github.com/vllm-project/vllm/pull/54335)
  [Feature] Add fixed-token prefill scoring (#54335)
  _Files: `docs/training/prompt_token_id_logprobs.md`, `rust/Cargo.lock`, `rust/src/engine-core-client/src/protocol/output.rs`, `rust/src/engine-core-client/src/protocol/sampling.rs` _+32 more__
- **2026-09-28** [`53d2e16a97`](https://github.com/vllm-project/vllm/commit/53d2e16a97) [#58490](https://github.com/vllm-project/vllm/pull/58490)
  [Bugfix][EPD] Skip sampling for encoder-only async steps (#58490)
  _Files: `tests/v1/engine/test_engine_core.py`, `tests/v1/kv_connector/unit/test_handshake_pp_aggregation.py`, `vllm/v1/engine/core.py`_

## Serving / API  (28 commits)

- **2026-10-04** [`b0eb87fe49`](https://github.com/vllm-project/vllm/commit/b0eb87fe49) [#40986](https://github.com/vllm-project/vllm/pull/40986)
  [Bugfix][Frontend] Return streaming errors before the first token (#40986)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat_error.py`, `tests/entrypoints/openai/completion/test_completion_error.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/completion/serving.py`_
- **2026-10-04** [`bdd31c31de`](https://github.com/vllm-project/vllm/commit/bdd31c31de) [#59521](https://github.com/vllm-project/vllm/pull/59521)
  [CI] Stop requiring both API servers to record weight sync metrics (#59521)
  _Files: `tests/entrypoints/serve/dev/rlhf/test_weight_operation_metrics.py`_
- **2026-10-04** [`6f75cc7d5d`](https://github.com/vllm-project/vllm/commit/6f75cc7d5d) [#59859](https://github.com/vllm-project/vllm/pull/59859)
  [Bugfix][Responses API] Reuse streamed item ids in final harmony response (#59859)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/serving.py`, `vllm/entrypoints/openai/responses/streaming_events.py` _+1 more__
- **2026-10-04** [`50b404e71e`](https://github.com/vllm-project/vllm/commit/50b404e71e) [#47933](https://github.com/vllm-project/vllm/pull/47933)
  [Bugfix][Frontend] Preserve abort finish_reason for scale-out token streams (#47933)
  _Files: `tests/entrypoints/scale_out/token_in_token_out/test_generate_stream.py`, `tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py`, `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-10-03** [`bc21cba967`](https://github.com/vllm-project/vllm/commit/bc21cba967) [#58588](https://github.com/vllm-project/vllm/pull/58588)
  [Frontend] Add output_mode to /inference/v1/generate (RFC #56851 Phase 1) (#58588)
  _Files: `docs/features/disagg_prefill.md`, `docs/serving/online_serving/README.md`, `docs/serving/online_serving/derenderer.md`, `docs/serving/online_serving/token_in_token_out.md` _+14 more__
- **2026-10-02** [`9bd993564f`](https://github.com/vllm-project/vllm/commit/9bd993564f) [#58604](https://github.com/vllm-project/vllm/pull/58604)
  [Frontend] Parse tool calls and reasoning from checkpoint response templates (#58604)
  _Files: `docs/features/tool_calling.md`, `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py` _+14 more__
- **2026-10-02** [`28c57456db`](https://github.com/vllm-project/vllm/commit/28c57456db) [#57693](https://github.com/vllm-project/vllm/pull/57693)
  [Bugfix][Frontend] Accept Anthropic tool_addition and tool_removal content blocks (#57693)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-10-01** [`2a52715ef7`](https://github.com/vllm-project/vllm/commit/2a52715ef7) [#59652](https://github.com/vllm-project/vllm/pull/59652)
  [Bugfix][Responses] Use standard reasoning content-part events (#59652)
  _Files: `tests/entrypoints/openai/responses/conftest.py`, `tests/entrypoints/openai/responses/test_function_call.py`, `tests/entrypoints/openai/responses/test_harmony.py`, `tests/entrypoints/openai/responses/test_streaming_events.py` _+2 more__
- **2026-10-01** [`5d9214d6b2`](https://github.com/vllm-project/vllm/commit/5d9214d6b2) [#59419](https://github.com/vllm-project/vllm/pull/59419)
  [Bugfix][Frontend] Strip `x-anthropic-billing-header` billing header from `/v1/chatcompletions` (#59419)
  _Files: `tests/entrypoints/unit_tests/test_chat_billing_header.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-10-01** [`91fcec1235`](https://github.com/vllm-project/vllm/commit/91fcec1235) [#58739](https://github.com/vllm-project/vllm/pull/58739)
  [Core][Logging] Add built-in JSON formatter (#58739)
  _Files: `.buildkite/test_areas/misc.yaml`, `examples/features/logging_configuration.md`, `tests/entrypoints/launchers/test_cli_args.py`, `tests/test_logger.py` _+7 more__
- **2026-10-01** [`31ec1c3aa1`](https://github.com/vllm-project/vllm/commit/31ec1c3aa1) [#59251](https://github.com/vllm-project/vllm/pull/59251)
  [Bugfix][Rust Frontend] Stop vllm-bench chat latency at the last token (#59251)
  _Files: `rust/src/bench/src/backends/openai_chat.rs`_
- **2026-09-30** [`cff08b461e`](https://github.com/vllm-project/vllm/commit/cff08b461e) [#50300](https://github.com/vllm-project/vllm/pull/50300)
  [Security] Fix chat template resource-exhaustion DoS (GHSA-4hhp-h66f-… (#50300)
  _Files: `rust/Cargo.toml`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/renderer/hf/template.rs`, `tests/renderers/test_executor_replace.py` _+4 more__
- **2026-09-30** [`329e6eee3f`](https://github.com/vllm-project/vllm/commit/329e6eee3f) [#47598](https://github.com/vllm-project/vllm/pull/47598)
  [Bugfix][Frontend] Report named Anthropic tool calls as tool_use (#47598)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-09-30** [`ac68c30872`](https://github.com/vllm-project/vllm/commit/ac68c30872) [#59173](https://github.com/vllm-project/vllm/pull/59173)
  [Bugfix][Frontend] Ignore reused prompt token ids for media in /v1/responses (#59173)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/chat_utils.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/renderers/online_renderer.py`_
- **2026-09-30** [`a3af78384a`](https://github.com/vllm-project/vllm/commit/a3af78384a) [#58003](https://github.com/vllm-project/vllm/pull/58003)
  [Agents] Add API compatibility checking skill (#58003)
  _Files: `.agents/skills/check-api-compat/SKILL.md`, `.agents/skills/check-api-compat/agents/openai.yaml`, `.claude/skills/check-api-compat`_
- **2026-09-30** [`7ca31ef599`](https://github.com/vllm-project/vllm/commit/7ca31ef599) [#59307](https://github.com/vllm-project/vllm/pull/59307)
  [Bugfix][Responses API] Build streamed final response from streamed items (#59307)
  _Files: `tests/entrypoints/openai/responses/conftest.py`, `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/serving.py` _+1 more__
- **2026-09-29** [`0755e69e75`](https://github.com/vllm-project/vllm/commit/0755e69e75) [#55596](https://github.com/vllm-project/vllm/pull/55596)
  [Bugfix][Responses API] Preserve built-in tool output call IDs (#55596)
  _Files: `tests/entrypoints/openai/responses/test_parsable_context_unit.py`, `vllm/entrypoints/mcp/tool.py`, `vllm/entrypoints/openai/responses/context.py`_
- **2026-09-29** [`797505747f`](https://github.com/vllm-project/vllm/commit/797505747f) [#59298](https://github.com/vllm-project/vllm/pull/59298)
  [Bugfix][Frontend] Honor parallel_tool_calls=false in the Responses API (#59298)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/serving.py`, `vllm/entrypoints/serve/utils/tool_calls_utils.py`_
- **2026-09-29** [`4dc57d44c4`](https://github.com/vllm-project/vllm/commit/4dc57d44c4) [#55029](https://github.com/vllm-project/vllm/pull/55029)
  [Frontend] Attach resolved logprobs to streaming derender chunks (#55029)
  _Files: `docs/serving/online_serving/derenderer.md`, `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`, `vllm/renderers/online_derenderer.py`_
- **2026-09-29** [`cd94b21264`](https://github.com/vllm-project/vllm/commit/cd94b21264) [#59236](https://github.com/vllm-project/vllm/pull/59236)
  [Bugfix][Frontend] Return 400 for malformed RL dev route bodies (#59236)
  _Files: `tests/entrypoints/unit_tests/test_dev_route_request_bodies.py`, `vllm/entrypoints/serve/dev/rlhf/api_router.py`, `vllm/entrypoints/serve/dev/rpc/api_router.py`_
- **2026-09-29** [`af5b4857e1`](https://github.com/vllm-project/vllm/commit/af5b4857e1) [#55477](https://github.com/vllm-project/vllm/pull/55477)
  [Fast Start] Support PP (#55477)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/entrypoints/cli/preload.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py` _+1 more__
- **2026-09-29** [`61349e342d`](https://github.com/vllm-project/vllm/commit/61349e342d) [#59172](https://github.com/vllm-project/vllm/pull/59172)
  [Misc] Avoid repeated warnings for merged Anthropic system messages (#59172)
  _Files: `vllm/entrypoints/anthropic/serving.py`_
- **2026-09-29** [`36768d1bfd`](https://github.com/vllm-project/vllm/commit/36768d1bfd) [#58842](https://github.com/vllm-project/vllm/pull/58842)
  [Bugfix][Frontend] Preserve caller parameters in offline pooling (#58842)
  _Files: `vllm/entrypoints/pooling/base/io_processor.py`, `vllm/entrypoints/pooling/pooling/io_processor.py`_
- **2026-09-29** [`c6843d397c`](https://github.com/vllm-project/vllm/commit/c6843d397c) [#55771](https://github.com/vllm-project/vllm/pull/55771)
  [Bugfix][Frontend] Validate reused prompt token ids; render messages for media and echo (#55771)
  _Files: `docs/features/disagg_prefill.md`, `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/entrypoints/chat_utils.py` _+2 more__
- **2026-09-28** [`6f65fde419`](https://github.com/vllm-project/vllm/commit/6f65fde419) [#58958](https://github.com/vllm-project/vllm/pull/58958)
  [Bugfix][Frontend] Apply Harmony adjust_request in batched chat completions (#58958)
  _Files: `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py`, `vllm/renderers/online_renderer.py`_
- **2026-09-28** [`027b6f3a22`](https://github.com/vllm-project/vllm/commit/027b6f3a22) [#58939](https://github.com/vllm-project/vllm/pull/58939)
  [Bugfix][Frontend] Use a fresh parser per choice in non-streaming chat completions (#58939)
  _Files: `vllm/entrypoints/openai/chat_completion/serving.py`_
- **2026-09-28** [`4d07e90653`](https://github.com/vllm-project/vllm/commit/4d07e90653) [#58929](https://github.com/vllm-project/vllm/pull/58929)
  [Bugfix][Frontend] Sample batched chat completions from the adjusted requests (#58929)
  _Files: `vllm/entrypoints/openai/chat_completion/batch_serving.py`_
- **2026-09-28** [`3184226984`](https://github.com/vllm-project/vllm/commit/3184226984) [#58927](https://github.com/vllm-project/vllm/pull/58927)
  [Bugfix][Frontend] Count Responses reasoning tokens per tool round (#58927)
  _Files: `tests/entrypoints/openai/responses/test_parsable_context_unit.py`, `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/serving.py`_

## CI / Build  (26 commits)

- **2026-10-05** [`edde9d2ce4`](https://github.com/vllm-project/vllm/commit/edde9d2ce4) [#59977](https://github.com/vllm-project/vllm/pull/59977)
  Remove redundant dependency requirement for TPU (#59977)
  _Files: `requirements/tpu.txt`_
- **2026-10-05** [`9e931a0c6c`](https://github.com/vllm-project/vllm/commit/9e931a0c6c) [#60060](https://github.com/vllm-project/vllm/pull/60060)
  [CI] Add CODEOWNERS for HiSparse (#60060)
  _Files: `.github/CODEOWNERS`_
- **2026-10-04** [`89439db727`](https://github.com/vllm-project/vllm/commit/89439db727) [#53692](https://github.com/vllm-project/vllm/pull/53692)
  [CI][Docs] Fix decode/prefill consistency test prefix construction; add GLM-4-9B and Phi-4 to batch-invariant tested models (#53692)
  _Files: `docs/features/batch_invariance.md`, `tests/v1/determinism/test_batch_invariance.py`_
- **2026-10-04** [`d64f6cd08a`](https://github.com/vllm-project/vllm/commit/d64f6cd08a) [#59913](https://github.com/vllm-project/vllm/pull/59913)
  [CI] Auto-label pooling PRs and issues (#59913)
  _Files: `.github/mergify.yml`, `.github/workflows/issue_autolabel.yml`_
- **2026-10-03** [`1a001d5842`](https://github.com/vllm-project/vllm/commit/1a001d5842) [#59850](https://github.com/vllm-project/vllm/pull/59850)
  [CI] Drop duplicate bf16 skinny GEMM test from Kimi K3 B200 job (#59850)
  _Files: `.buildkite/test_areas/models_basic.yaml`_
- **2026-10-03** [`9fdb174678`](https://github.com/vllm-project/vllm/commit/9fdb174678) [#59699](https://github.com/vllm-project/vllm/pull/59699)
  [Bugfix] Avoid InfiniBand state in TP1 snapshots (#59699)
  _Files: `.buildkite/scripts/initialized-snapshot-e2e.sh`, `docs/features/initialized_snapshots.md`, `tests/entrypoints/launchers/test_launch_cli.py`, `vllm/snapshot/runtime.py`_
- **2026-10-02** [`8442117446`](https://github.com/vllm-project/vllm/commit/8442117446) [#59396](https://github.com/vllm-project/vllm/pull/59396)
  Upgrade tpu-inference to v0.30.0 (#59396)
  _Files: `requirements/tpu.txt`_
- **2026-10-02** [`1ab18599ca`](https://github.com/vllm-project/vllm/commit/1ab18599ca) [#59657](https://github.com/vllm-project/vllm/pull/59657)
  [Agents] Add pre-commit check for agent files and skills (#59657)
  _Files: `.buildkite/test_areas/misc.yaml`, `.pre-commit-config.yaml`, `docs/contributing/editing-agent-instructions.md`, `rust/CLAUDE.md` _+6 more__
- **2026-10-02** [`167a81fa9c`](https://github.com/vllm-project/vllm/commit/167a81fa9c) [#59772](https://github.com/vllm-project/vllm/pull/59772)
  [CI] Fix ModelExpress handling in weight transfer tests (#59772)
  _Files: `tests/distributed/test_weight_transfer.py`_
- **2026-10-02** [`2a537887de`](https://github.com/vllm-project/vllm/commit/2a537887de) [#59525](https://github.com/vllm-project/vllm/pull/59525)
  [CI] Use vllm_runner in fusions_e2e conftest for reliable GPU cleanup (#59525)
  _Files: `tests/compile/fusions_e2e/conftest.py`_
- **2026-10-02** [`58b3298457`](https://github.com/vllm-project/vllm/commit/58b3298457) [#59614](https://github.com/vllm-project/vllm/pull/59614)
  [Misc] Add Transformers version upper bound in requirements (#59614)
  _Files: `requirements/common.txt`_
- **2026-10-02** [`4caa060053`](https://github.com/vllm-project/vllm/commit/4caa060053) [#59622](https://github.com/vllm-project/vllm/pull/59622)
  [TEST][CI] Fix serve rlhf tests subprocess import errors (#59622)
  _Files: `tests/entrypoints/serve/dev/rlhf/__init__.py`_
- **2026-10-02** [`89772ddb1f`](https://github.com/vllm-project/vllm/commit/89772ddb1f) [#59556](https://github.com/vllm-project/vllm/pull/59556)
  [CI][XPU] Skip CUDA-IPC weight sync metrics test on Intel (#59556)
  _Files: `.buildkite/intel_jobs/entrypoints_intel.yaml`_
- **2026-10-02** [`5b6b657e13`](https://github.com/vllm-project/vllm/commit/5b6b657e13) [#59710](https://github.com/vllm-project/vllm/pull/59710)
  [ci] Update mergify to rebase if behind by 100 commits (#59710)
  _Files: `.github/mergify.yml`_
- **2026-10-01** [`21c08ac458`](https://github.com/vllm-project/vllm/commit/21c08ac458) [#58125](https://github.com/vllm-project/vllm/pull/58125)
  [CI] Deflake shutdown wait-timeout test by synchronizing on request admission (#58125)
  _Files: `tests/entrypoints/launchers/test_shutdown.py`_
- **2026-09-30** [`749192ff41`](https://github.com/vllm-project/vllm/commit/749192ff41) [#59398](https://github.com/vllm-project/vllm/pull/59398)
  [CI] Skip the IPC weight-checker test on non-CUDA platforms (#59398)
  _Files: `tests/entrypoints/serve/dev/rlhf/state_transitions/test_weight_checker.py`_
- **2026-09-30** [`09c47db1ca`](https://github.com/vllm-project/vllm/commit/09c47db1ca) [#58307](https://github.com/vllm-project/vllm/pull/58307)
  [XPU][CI]Skip test_abort_timeout_on_prefiller in nightly (#58307)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-09-29** [`35cd03ebff`](https://github.com/vllm-project/vllm/commit/35cd03ebff) [#59259](https://github.com/vllm-project/vllm/pull/59259)
  [CI] Mint the CRCR report's OIDC token after the wait, not before (#59259)
  _Files: `.buildkite/scripts/crcr-report.sh`_
- **2026-09-29** [`741edeebee`](https://github.com/vllm-project/vllm/commit/741edeebee) [#59202](https://github.com/vllm-project/vllm/pull/59202)
  [Bugfix][CI] Assert the logger call the Anthropic merge warning makes (#59202)
- **2026-09-29** [`998490cd9f`](https://github.com/vllm-project/vllm/commit/998490cd9f) [#58705](https://github.com/vllm-project/vllm/pull/58705)
  [Docs] Speed up docs build ~5x (#58705)
  _Files: `docs/mkdocs/overrides/partials/nav.html`, `mkdocs.yaml`, `requirements/docs.in`, `requirements/docs.txt`_
- **2026-09-29** [`7230dfea50`](https://github.com/vllm-project/vllm/commit/7230dfea50) [#54874](https://github.com/vllm-project/vllm/pull/54874)
  [XPU] Preserve non-contiguous strides when pinning CPU tensors for UVA view (#54874)
  _Files: `.buildkite/intel_jobs/kernels_intel.yaml`, `tests/kernels/core/test_uva.py`, `vllm/utils/torch_utils.py`_
- **2026-09-29** [`869278cbb0`](https://github.com/vllm-project/vllm/commit/869278cbb0) [#59066](https://github.com/vllm-project/vllm/pull/59066)
  [CI] Bound the CRCR report by build age, and stop gating it on a job (#59066)
  _Files: `.buildkite/scripts/crcr-report.sh`, `.buildkite/test_areas/crcr_report.yaml`_
- **2026-09-28** [`6a6c2952fa`](https://github.com/vllm-project/vllm/commit/6a6c2952fa) [#58269](https://github.com/vllm-project/vllm/pull/58269)
  [XPU][CI] Make `test_mamba_prefix_cache` block-size agnostic (#58269)
  _Files: `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `vllm/platforms/xpu.py`_
- **2026-09-28** [`32cc3f1ea8`](https://github.com/vllm-project/vllm/commit/32cc3f1ea8) [#58895](https://github.com/vllm-project/vllm/pull/58895)
  [CI] Drop test-group rules that no longer match the tree (#58895)
  _Files: `.buildkite/test_areas/kernels.yaml`_
- **2026-09-28** [`6c300ddb9e`](https://github.com/vllm-project/vllm/commit/6c300ddb9e) [#59008](https://github.com/vllm-project/vllm/pull/59008)
  [CI][Bugfix] Relax packed_qk_rope_ correctness test to one ULP (#59008)
  _Files: `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/packed_qk_rope.py`_
- **2026-09-28** [`2407f405b5`](https://github.com/vllm-project/vllm/commit/2407f405b5) [#58055](https://github.com/vllm-project/vllm/pull/58055)
  [CI] Allowlist-shrink batch 1: wire 17 root-level tests + drop 5 stale watermarking entries into misc.yaml (#58055)
  _Files: `.buildkite/test_areas/misc.yaml`, `docker/Dockerfile.cpu`, `tests/test_request_input_bounds.py`, `tests/test_triton_utils.py` _+4 more__

## Models  (25 commits)

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
- **2026-10-02** [`f590eb2448`](https://github.com/vllm-project/vllm/commit/f590eb2448) [#59753](https://github.com/vllm-project/vllm/pull/59753)
  [Perf][Qwen4Exp] Add SM121 TP=1 skinny-GEMM plans (#59753)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/qwen4_exp/nvidia/low_latency_gemm.py`_
- **2026-10-02** [`24df2d3fc7`](https://github.com/vllm-project/vllm/commit/24df2d3fc7) [#56742](https://github.com/vllm-project/vllm/pull/56742)
  [Model] Add Qwen4Exp to the Qwen GDN Triton warmup (#56742)
  _Files: `vllm/model_executor/warmup/qwen_triton_warmup.py`_
- **2026-10-02** [`6e4efafc6e`](https://github.com/vllm-project/vllm/commit/6e4efafc6e) [#59701](https://github.com/vllm-project/vllm/pull/59701)
  [Model] Migrate GPT-NeoX, Phi, Seed-OSS and Jais2 to the Transformers modeling backend (#59701)
  _Files: `docs/models/supported_models.md`, `vllm/model_executor/models/gpt_neox.py`, `vllm/model_executor/models/jais2.py`, `vllm/model_executor/models/phi.py` _+4 more__
- **2026-10-02** [`8faacd707f`](https://github.com/vllm-project/vllm/commit/8faacd707f) [#59679](https://github.com/vllm-project/vllm/pull/59679)
  [Model] Migrate Glm, Arcee, CWM and Mellum to the Transformers modeling backend (#59679)
  _Files: `docs/models/supported_models.md`, `vllm/model_executor/models/arcee.py`, `vllm/model_executor/models/bert_with_rope.py`, `vllm/model_executor/models/glm.py` _+2 more__
- **2026-10-01** [`4ed438b79c`](https://github.com/vllm-project/vllm/commit/4ed438b79c) [#59214](https://github.com/vllm-project/vllm/pull/59214)
  [Perf][Qwen4Exp] Add SM100 low-latency decode GEMM plans (#59214)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/qwen4_exp/nvidia/low_latency_gemm.py`_
- **2026-10-01** [`a37c402f32`](https://github.com/vllm-project/vllm/commit/a37c402f32) [#51792](https://github.com/vllm-project/vllm/pull/51792)
  [weight loader] add dtype equality validation between parameter and weight (#51792)
  _Files: `vllm/model_executor/models/utils.py`_
- **2026-09-30** [`863475eb9c`](https://github.com/vllm-project/vllm/commit/863475eb9c) [#54441](https://github.com/vllm-project/vllm/pull/54441)
  docs: add gemma-2, SmolLM2, Qwen2.5-Coder, Llama-3.2-1B to batch invariance tested models (#54441)
  _Files: `docs/features/batch_invariance.md`_
- **2026-09-30** [`fb91712b38`](https://github.com/vllm-project/vllm/commit/fb91712b38) [#59348](https://github.com/vllm-project/vllm/pull/59348)
  [Model] Make the BERT/RoBERTa embedding class a class attribute (#59348)
  _Files: `vllm/model_executor/models/bert.py`, `vllm/model_executor/models/roberta.py`_
- **2026-09-30** [`b81984879a`](https://github.com/vllm-project/vllm/commit/b81984879a) [#55335](https://github.com/vllm-project/vllm/pull/55335)
  [K2 Horizon] fold partial-RoPE permutation into q/k (and norm) weights (#55335)
  _Files: `tests/model_executor/test_k2_horizon_rope_fold.py`, `vllm/model_executor/models/k2_horizon.py`_
- **2026-09-29** [`4e7af3b0de`](https://github.com/vllm-project/vllm/commit/4e7af3b0de) [#50502](https://github.com/vllm-project/vllm/pull/50502)
  [Bugfix][Frontend] Enforce parallel_tool_calls=false in the required-tool grammar (#50502)
  _Files: `tests/tool_parsers/test_functiongemma_tool_parser.py`, `tests/tool_parsers/test_structural_tag_registry.py`, `tests/tool_use/test_tool_choice_required.py`, `vllm/parser/abstract_parser.py` _+4 more__
- **2026-09-29** [`9a190f142c`](https://github.com/vllm-project/vllm/commit/9a190f142c) [#58255](https://github.com/vllm-project/vllm/pull/58255)
  [Mypy] Fix mypy typing for Zamba2 models (#58255)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/zamba2.py`_
- **2026-09-29** [`2454b5a4f0`](https://github.com/vllm-project/vllm/commit/2454b5a4f0) [#58254](https://github.com/vllm-project/vllm/pull/58254)
  [Mypy] Fix mypy typing for Whisper models (#58254)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/whisper.py`, `vllm/model_executor/models/whisper_causal.py`_
- **2026-09-29** [`30f5c01d4e`](https://github.com/vllm-project/vllm/commit/30f5c01d4e) [#59119](https://github.com/vllm-project/vllm/pull/59119)
  [DSv4.1] Avoid runtime recompiles of _ring_slot_mapping_kernel (#59119)
  _Files: `vllm/models/deepseek_v41/compressor.py`_
- **2026-09-29** [`6cbbea8721`](https://github.com/vllm-project/vllm/commit/6cbbea8721) [#49602](https://github.com/vllm-project/vllm/pull/49602)
  [Bugfix] Hoist $defs/definitions in Cohere parser tool schema composition (#49602)
  _Files: `tests/parser/cohere/test_structural_tags.py`, `vllm/parser/cohere_command.py`_
- **2026-09-29** [`13c8589b86`](https://github.com/vllm-project/vllm/commit/13c8589b86) [#57476](https://github.com/vllm-project/vllm/pull/57476)
  fix: return loaded parameters in Aria load_weights (#57476)
  _Files: `vllm/model_executor/models/aria.py`_
- **2026-09-28** [`8cc9aa5ad3`](https://github.com/vllm-project/vllm/commit/8cc9aa5ad3) [#54213](https://github.com/vllm-project/vllm/pull/54213)
  [Bugfix][Model] Gemma4: register aliased embedding scalars as buffers (#54213)
  _Files: `vllm/model_executor/models/gemma4.py`_
- **2026-09-28** [`d6cce94fd4`](https://github.com/vllm-project/vllm/commit/d6cce94fd4) [#58957](https://github.com/vllm-project/vllm/pull/58957)
  [Perf][Qwen4Exp] Fuse HC down projection and SiLU on NVIDIA (#58957)
  _Files: `tests/models/qwen4_exp/test_hc_ops.py`, `vllm/models/qwen4_exp/nvidia/hyperconnection.py`, `vllm/models/qwen4_exp/nvidia/model.py`, `vllm/models/qwen4_exp/nvidia/ops/cute_dsl/__init__.py` _+3 more__
- **2026-09-28** [`1668e5976d`](https://github.com/vllm-project/vllm/commit/1668e5976d) [#58964](https://github.com/vllm-project/vllm/pull/58964)
  [CPU] Use accelerator memory API in DiffusionGemma (#58964)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-09-28** [`b9e2903b89`](https://github.com/vllm-project/vllm/commit/b9e2903b89) [#58239](https://github.com/vllm-project/vllm/pull/58239)
  [Mypy] Fix mypy typing for Ultravox and Unlimited-OCR models (#58239)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/model_loader/reload/torchao_decorator.py`, `vllm/model_executor/models/phi4mm.py`, `vllm/model_executor/models/ultravox.py` _+2 more__
- **2026-09-28** [`39d49539de`](https://github.com/vllm-project/vllm/commit/39d49539de) [#58651](https://github.com/vllm-project/vllm/pull/58651)
  [KimiViT][Perf] Fuse per-layer QK RoPE into one in-place kernel (#58651)
  _Files: `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/packed_qk_rope.py`, `vllm/model_executor/models/kimi_k25_vit.py`_

## MoE / Expert Parallel  (23 commits)

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
- **2026-10-03** [`44198f577f`](https://github.com/vllm-project/vllm/commit/44198f577f) [#58890](https://github.com/vllm-project/vllm/pull/58890)
  [Bugfix][Model] Fix M-RoPE offset double-count in Qwen3-Omni (#58890)
  _Files: `tests/model_executor/test_qwen3_omni_mrope.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`_
- **2026-10-02** [`84593955fa`](https://github.com/vllm-project/vllm/commit/84593955fa) [#57995](https://github.com/vllm-project/vllm/pull/57995)
  [Perf][MoE] Support fp8 combine in FlashInfer one-sided MoE all2all (#57995)
  _Files: `tests/distributed/test_mnnvl_alltoall.py`, `vllm/distributed/device_communicators/all2all.py`, `vllm/envs.py`_
- **2026-10-02** [`d1a974c140`](https://github.com/vllm-project/vllm/commit/d1a974c140) [#56403](https://github.com/vllm-project/vllm/pull/56403)
  [Frontend] Constrain non-strict GLM-4.7 tool calls with a shallow structural tag (#56403)
  _Files: `tests/tool_parsers/test_structural_tag_registry.py`, `vllm/parser/abstract_parser.py`, `vllm/tool_parsers/abstract_tool_parser.py`, `vllm/tool_parsers/glm47_moe_tool_parser.py` _+1 more__
- **2026-10-02** [`9cf087fd14`](https://github.com/vllm-project/vllm/commit/9cf087fd14) [#59731](https://github.com/vllm-project/vllm/pull/59731)
  [Perf] Tune MoE weighted-sum kernel launch configuration (#59731)
  _Files: `tests/kernels/moe/test_moe_fused_mul_sum.py`, `vllm/model_executor/layers/fused_moe/moe_fused_mul_sum.py`_
- **2026-10-02** [`e42d35d4f3`](https://github.com/vllm-project/vllm/commit/e42d35d4f3) [#59481](https://github.com/vllm-project/vllm/pull/59481)
  [Minimax-M3] Keep the native FP8 MMA in the Triton indexer scorers (#59481)
  _Files: `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`_
- **2026-10-02** [`c91dccc080`](https://github.com/vllm-project/vllm/commit/c91dccc080) [#59752](https://github.com/vllm-project/vllm/pull/59752)
  [Bugfix][Quark] Pass grouped-routing arguments to OCP MX monolithic kernels (#59752)
  _Files: `vllm/model_executor/layers/quantization/quark/quark_moe.py`_
- **2026-10-02** [`fa212b8dc5`](https://github.com/vllm-project/vllm/commit/fa212b8dc5) [#59763](https://github.com/vllm-project/vllm/pull/59763)
  [Test] Re-enable Ovis2.5 and Ovis2.6-MoE vLLM tests on Transformers v5 (#59763)
  _Files: `tests/models/multimodal/generation/test_common.py`, `tests/models/registry.py`_
- **2026-10-02** [`5d20979fc9`](https://github.com/vllm-project/vllm/commit/5d20979fc9) [#59762](https://github.com/vllm-project/vllm/pull/59762)
  [Misc] Remove code paths for Transformers < 5.16.1 (#59762)
  _Files: `tests/models/language/generation/test_granite.py`, `tests/models/multimodal/processing/test_transformers_audio.py`, `tests/models/multimodal/processing/test_transformers_image.py`, `tests/models/multimodal/processing/transformers_backend.py` _+14 more__
- **2026-10-02** [`8c60714da5`](https://github.com/vllm-project/vllm/commit/8c60714da5) [#55161](https://github.com/vllm-project/vllm/pull/55161)
  [Bugfix][LoRA] Fall back for high-rank MoE LoRA (#55161)
  _Files: `tests/lora/test_fused_moe_lora_kernel.py`, `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`_
- **2026-10-01** [`5addde2a0a`](https://github.com/vllm-project/vllm/commit/5addde2a0a) [#59434](https://github.com/vllm-project/vllm/pull/59434)
  [CPU][Zen] Pass f32 weight scales to the zentorch INT8 MoE (#59434)
  _Files: `tests/kernels/moe/test_zen_cpu_int8_moe.py`, `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`_
- **2026-10-01** [`e12291d733`](https://github.com/vllm-project/vllm/commit/e12291d733) [#54024](https://github.com/vllm-project/vllm/pull/54024)
  [CPU][Zen] Add DA8W4 (W4A8) int4 support for dense and MoE layers (#54024)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `tests/kernels/quantization/test_zen_da8w4.py`, `vllm/envs.py`, `vllm/model_executor/kernels/linear/mixed_precision/zentorch.py` _+5 more__
- **2026-09-30** [`84f738f187`](https://github.com/vllm-project/vllm/commit/84f738f187) [#56151](https://github.com/vllm-project/vllm/pull/56151)
  [Perf][MiniMax-M3] Triton indexer: decode grid retune + SM12.0 split-K (#56151)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`_
- **2026-09-30** [`0103a9b96f`](https://github.com/vllm-project/vllm/commit/0103a9b96f) [#50030](https://github.com/vllm-project/vllm/pull/50030)
  [Quantization] Add per-token NVFP4 CuTe-DSL MoE backend (#50030)
  _Files: `tests/kernels/moe/test_flashinfer_cutedsl_nvfp4_moe.py`, `tests/quantization/test_online.py`, `tests/quantization/test_trtllm_nvfp4_hidden_dim_padding.py`, `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_moe.py` _+5 more__
- **2026-09-30** [`583637f126`](https://github.com/vllm-project/vllm/commit/583637f126) [#53913](https://github.com/vllm-project/vllm/pull/53913)
  [CPU][Perf] Add vectorized Sampler Kernel (#53913)
  _Files: `benchmarks/kernels/bench_cpu_sampling.py`, `cmake/cpu_extension.cmake`, `csrc/cpu/sampling_kernels.cpp`, `csrc/cpu/torch_bindings.cpp` _+3 more__
- **2026-09-29** [`1ee7f78e80`](https://github.com/vllm-project/vllm/commit/1ee7f78e80) [#58605](https://github.com/vllm-project/vllm/pull/58605)
  [Perf] Reduce redundant Triton sampler warmup specializations (#58605)
  _Files: `vllm/v1/sample/ops/topk_topp_triton.py`_
- **2026-09-29** [`d95d1dcfb9`](https://github.com/vllm-project/vllm/commit/d95d1dcfb9) [#56994](https://github.com/vllm-project/vllm/pull/56994)
  [Bugfix][Frontend] Force reasoning mode for GLM-5.3 chat templates in the GLM MoE parser (#56994)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/reasoning/test_glm4_moe_reasoning_parser.py`, `vllm/parser/glm47_moe.py`_
- **2026-09-28** [`9b29370524`](https://github.com/vllm-project/vllm/commit/9b29370524) [#58950](https://github.com/vllm-project/vllm/pull/58950)
  [Bugfix] Fix moe_wna16 w13 zero-point shard split for 8-bit asym GPTQ MoE (#58950)
  _Files: `tests/quantization/test_moe_wna16.py`, `vllm/model_executor/layers/quantization/moe_wna16.py`_
- **2026-09-28** [`e03875f4d2`](https://github.com/vllm-project/vllm/commit/e03875f4d2) [#59081](https://github.com/vllm-project/vllm/pull/59081)
  [Minimax M3] Enable fp8 indexer cache on triton indexer for non-SM100 architectures.  (#59081)
  _Files: `tests/kernels/attention/test_minimax_m3_fp8_triton_indexer.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`_
- **2026-09-28** [`c01368fd64`](https://github.com/vllm-project/vllm/commit/c01368fd64) [#52798](https://github.com/vllm-project/vllm/pull/52798)
  [Quant] Use canonical N-first weight format for CT WNA16 MoE (#52798)
  _Files: `tests/kernels/quantization/test_int4_emulation_moe.py`, `tests/quantization/test_moe_wna16.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py` _+2 more__

## Disaggregation / PD  (20 commits)

- **2026-10-05** [`b1401e0aa7`](https://github.com/vllm-project/vllm/commit/b1401e0aa7) [#59873](https://github.com/vllm-project/vllm/pull/59873)
  [Bugfix][NIXL] Count heartbeats as remote engine activity (#59873)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-03** [`f03026a548`](https://github.com/vllm-project/vllm/commit/f03026a548) [#59441](https://github.com/vllm-project/vllm/pull/59441)
  [Bugfix][MoRIIO] Keep discovery heartbeats running while workers hold the GIL (#59441)
  _Files: `tests/v1/kv_connector/unit/test_moriio_proxy_routing.py`, `tests/v1/kv_connector/unit/test_moriio_tp_ack.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_heartbeat.py`_
- **2026-10-03** [`5f30fc7031`](https://github.com/vllm-project/vllm/commit/5f30fc7031) [#59347](https://github.com/vllm-project/vllm/pull/59347)
  [Bugfix][KV Connector][Mooncake] Suppress completion for empty pulls (#59347)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-10-03** [`ca0df1f122`](https://github.com/vllm-project/vllm/commit/ca0df1f122) [#59504](https://github.com/vllm-project/vllm/pull/59504)
  [Bugfix][Core] Exempt exactly the blocks an async KV load writes from zeroing (#59504)
  _Files: `tests/v1/core/test_prefix_replay.py`, `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `tests/v1/kv_connector/unit/test_error_propagation.py` _+13 more__
- **2026-10-03** [`7dfe3338d5`](https://github.com/vllm-project/vllm/commit/7dfe3338d5) [#52641](https://github.com/vllm-project/vllm/pull/52641)
  [EPLB] Add contention-aware expert migration batching (#52641)
  _Files: `.buildkite/test_areas/expert_parallelism.yaml`, `tests/distributed/test_eplb_migration_scheduler.py`, `vllm/config/parallel.py`, `vllm/distributed/eplb/async_worker.py` _+2 more__
- **2026-10-02** [`1a9eaa3a68`](https://github.com/vllm-project/vllm/commit/1a9eaa3a68) [#59196](https://github.com/vllm-project/vllm/pull/59196)
  [Doc] Document ECMooncakeConnector for EPD disaggregation (#59196)
  _Files: `docs/features/disagg_encoder.md`, `docs/features/disagg_prefill.md`, `docs/features/mooncake_connector_usage.md`, `docs/features/mooncake_ec_connector_usage.md` _+1 more__
- **2026-10-02** [`a810316c08`](https://github.com/vllm-project/vllm/commit/a810316c08) [#59500](https://github.com/vllm-project/vllm/pull/59500)
  [Bugfix] Keep batch-invariance NCCL pins out of the weight-transfer group (#59500)
  _Files: `tests/distributed/test_weight_transfer.py`, `vllm/distributed/weight_transfer/nccl_common.py`, `vllm/model_executor/determinism/batch_invariant.py`, `vllm/utils/nccl.py`_
- **2026-10-02** [`5a661487e2`](https://github.com/vllm-project/vllm/commit/5a661487e2) [#58399](https://github.com/vllm-project/vllm/pull/58399)
  [Feature] Add native ModelExpress weight transfer backend (#58399)
  _Files: `docs/training/weight_transfer/README.md`, `docs/training/weight_transfer/modelexpress.md`, `tests/distributed/test_weight_transfer.py`, `vllm/distributed/weight_transfer/factory.py` _+1 more__
- **2026-10-02** [`785b990116`](https://github.com/vllm-project/vllm/commit/785b990116) [#58623](https://github.com/vllm-project/vllm/pull/58623)
  [Distributed] Enable custom all-reduce under VLLM_BATCH_INVARIANT (#58623)
  _Files: `docs/features/batch_invariance.md`, `tests/distributed/test_custom_all_reduce.py`, `tests/v1/determinism/test_batch_invariance.py`, `vllm/config/parallel.py` _+3 more__
- **2026-10-01** [`ca65eb67d9`](https://github.com/vllm-project/vllm/commit/ca65eb67d9) [#57930](https://github.com/vllm-project/vllm/pull/57930)
  [Perf][HiSparse] Avoid repeated prefix scans and residency updates (#57930)
  _Files: `tests/v1/core/test_prefix_caching.py`, `tests/v1/kv_connector/unit/test_hisparse_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/hisparse/connector.py`, `vllm/v1/core/single_type_kv_cache_manager.py` _+1 more__
- **2026-10-01** [`ea84051819`](https://github.com/vllm-project/vllm/commit/ea84051819) [#58875](https://github.com/vllm-project/vllm/pull/58875)
  [KVConnector][NIXL] Count completion notifications that arrive after KV expiry (#58875)
  _Files: `docs/features/nixl_connector_usage.md`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py` _+3 more__
- **2026-10-01** [`47de9d4d04`](https://github.com/vllm-project/vllm/commit/47de9d4d04) [#54483](https://github.com/vllm-project/vllm/pull/54483)
  [KV Connector][NIXL] Coalesce host-buffer KV copies across cache groups (#54483)
  _Files: `benchmarks/kernels/benchmark_host_buffer_kv_copy.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-01** [`ab5266769e`](https://github.com/vllm-project/vllm/commit/ab5266769e) [#59192](https://github.com/vllm-project/vllm/pull/59192)
  [CI/Build] Add mooncake auto-label rule and assign topic owners (#59192)
  _Files: `.github/mergify.yml`_
- **2026-10-01** [`e5e38ba9b7`](https://github.com/vllm-project/vllm/commit/e5e38ba9b7) [#58411](https://github.com/vllm-project/vllm/pull/58411)
  [Model Runner V2] Support randomized dummy inputs (#58411)
  _Files: `vllm/distributed/elastic_ep/elastic_execute.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-10-01** [`8bc31bd210`](https://github.com/vllm-project/vllm/commit/8bc31bd210) [#59507](https://github.com/vllm-project/vllm/pull/59507)
  [CI] Deflake the multi-API-server metrics test and Mooncake PD ports (#59507)
  _Files: `tests/entrypoints/serve/dev/rlhf/test_weight_operation_metrics.py`, `tests/v1/kv_connector/mooncake_integration/run_accuracy_test.sh`, `tests/v1/kv_connector/mooncake_integration/test_accuracy.py`_
- **2026-09-30** [`765872e7ed`](https://github.com/vllm-project/vllm/commit/765872e7ed) [#51899](https://github.com/vllm-project/vllm/pull/51899)
  [Core][BugFix] Tag prefix-cache extra keys by source (#51899)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_prefix_caching.py`, `vllm/distributed/kv_events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py` _+3 more__
- **2026-09-29** [`50239dfc4d`](https://github.com/vllm-project/vllm/commit/50239dfc4d) [#57991](https://github.com/vllm-project/vllm/pull/57991)
  [WideEP] Change DeepEPv2 to auto select hybrid mode by default (#57991)
  _Files: `vllm/distributed/device_communicators/all2all.py`, `vllm/envs.py`, `vllm/utils/nccl.py`_
- **2026-09-29** [`30ae8248b6`](https://github.com/vllm-project/vllm/commit/30ae8248b6) [#57700](https://github.com/vllm-project/vllm/pull/57700)
  [KVConnector][MoRIIO] Support K3 DSpark hybrid READ (#57700)
  _Files: `tests/v1/kv_connector/unit/test_moriio_hma_scheduler.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py` _+1 more__
- **2026-09-29** [`4406874e7c`](https://github.com/vllm-project/vllm/commit/4406874e7c) [#58611](https://github.com/vllm-project/vllm/pull/58611)
  [Bugfix][FT] Pass stateless process-group timeouts explicitly (#58611)
  _Files: `tests/test_config.py`, `vllm/config/parallel.py`, `vllm/distributed/stateless_coordinator.py`, `vllm/distributed/utils.py` _+2 more__
- **2026-09-29** [`171d1b9ef6`](https://github.com/vllm-project/vllm/commit/171d1b9ef6) [#53934](https://github.com/vllm-project/vllm/pull/53934)
  [Elastic EP] Support Model Runner V2 (#53934)
  _Files: `tests/v1/cudagraph/test_cudagraph_manager.py`, `tests/v1/engine/test_engine_core_client.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`, `vllm/config/vllm.py` _+8 more__

## Speculative Decoding  (15 commits)

- **2026-10-05** [`b1f229fb75`](https://github.com/vllm-project/vllm/commit/b1f229fb75) [#52824](https://github.com/vllm-project/vllm/pull/52824)
  [Model] Declare SupportsEagle3 on Qwen3ASRForConditionalGeneration (#52824)
  _Files: `vllm/model_executor/models/qwen3_asr.py`_
- **2026-10-05** [`4f52fa35ef`](https://github.com/vllm-project/vllm/commit/4f52fa35ef) [#59990](https://github.com/vllm-project/vllm/pull/59990)
  [Bugfix] Fix Qwen4Exp PLE embedding rejecting INC (AutoRound) checkpoints (#59990)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/common/ngram_embedding.py`_
- **2026-10-04** [`5e56e9af2a`](https://github.com/vllm-project/vllm/commit/5e56e9af2a) [#59160](https://github.com/vllm-project/vllm/pull/59160)
  [Feature] Release the CUDA graph pool on sleep (#59160)
  _Files: `docs/features/sleep_mode.md`, `tests/basic_correctness/memory/cumem/test_cumem.py`, `tests/basic_correctness/memory/sleep_mode/test_sleep_mode.py`, `tests/distributed/test_engram_dp_shard.py` _+12 more__
- **2026-10-02** [`202d497aa8`](https://github.com/vllm-project/vllm/commit/202d497aa8) [#59779](https://github.com/vllm-project/vllm/pull/59779)
  [Bugfix][Watermarking] Keep draft prompt lengths valid under CUDA graphs (#59779)
  _Files: `tests/watermarking/test_watermarking.py`, `vllm/v1/watermarking/spec_decode.py`_
- **2026-10-02** [`e4294144a8`](https://github.com/vllm-project/vllm/commit/e4294144a8) [#59735](https://github.com/vllm-project/vllm/pull/59735)
  [Perf] Keep non-speculative GDN decode on the standard path (#59735)
  _Files: `tests/kernels/mamba/test_gdn_fused_mtp.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-10-01** [`840c7c2f4b`](https://github.com/vllm-project/vllm/commit/840c7c2f4b) [#59639](https://github.com/vllm-project/vllm/pull/59639)
  [Bugfix][Engram] Fix intermittent Triton 3.8 crash in the lookup kernel (#59639)
  _Files: `vllm/models/deepseek_v41/common/engram.py`_
- **2026-10-01** [`bcee730b1a`](https://github.com/vllm-project/vllm/commit/bcee730b1a) [#59530](https://github.com/vllm-project/vllm/pull/59530)
  [Docs] Remove references to removed env vars (#59530)
  _Files: `docs/features/engram.md`, `docs/serving/online_serving/renderer.md`_
- **2026-10-01** [`34c458d27f`](https://github.com/vllm-project/vllm/commit/34c458d27f) [#54442](https://github.com/vllm-project/vllm/pull/54442)
  [Bugfix] Don't let a structured-output request sample from an unmasked row (#54442)
  _Files: `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `tests/v1/worker/test_grammar_invalid_drafts.py`, `vllm/v1/core/sched/output.py`, `vllm/v1/core/sched/scheduler.py` _+4 more__
- **2026-10-01** [`d7c55116ac`](https://github.com/vllm-project/vllm/commit/d7c55116ac) [#59508](https://github.com/vllm-project/vllm/pull/59508)
  [CI] Fix MiniMax-M3 PP aux-state test mock after #58648 (#59508)
  _Files: `tests/v1/worker/test_eagle3_aux_hidden_states_pp.py`_
- **2026-09-30** [`0f8b398158`](https://github.com/vllm-project/vllm/commit/0f8b398158) [#56807](https://github.com/vllm-project/vllm/pull/56807)
  [watermarking] add context deduplication support to speculative decoding (#56807)
  _Files: `docs/features/watermarking.md`, `tests/test_config.py`, `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `tests/watermarking/test_gumbel.py` _+13 more__
- **2026-09-29** [`79a0307d74`](https://github.com/vllm-project/vllm/commit/79a0307d74) [#59171](https://github.com/vllm-project/vllm/pull/59171)
  [Config] Remove Engram CUDA-alike device restrictions (#59171)
  _Files: `tests/test_config.py`, `vllm/config/engram.py`, `vllm/config/vllm.py`_
- **2026-09-29** [`4b2e1cfa7b`](https://github.com/vllm-project/vllm/commit/4b2e1cfa7b) [#58132](https://github.com/vllm-project/vllm/pull/58132)
  [Model] Decoder-side SWA bounded replay for DeepSeek-V4.1 (#58132)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/distributed/test_engram_dp_shard.py`, `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/models/test_deepseek_v41_replay_batch.py` _+5 more__
- **2026-09-29** [`ec5e0c352f`](https://github.com/vllm-project/vllm/commit/ec5e0c352f) [#59068](https://github.com/vllm-project/vllm/pull/59068)
  [Bugfix][Engram] Keep THP tables private when resolving shared memory (#59068)
  _Files: `tests/test_config.py`, `vllm/config/engram.py`_
- **2026-09-28** [`fedbc3b564`](https://github.com/vllm-project/vllm/commit/fedbc3b564) [#58784](https://github.com/vllm-project/vllm/pull/58784)
  [Bugfix][MRV2][Spec Decode] Reject draft slots that were never proposed (#58784)
  _Files: `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `vllm/v1/worker/gpu/spec_decode/rejection_sampler.py`_
- **2026-09-28** [`ef42093a36`](https://github.com/vllm-project/vllm/commit/ef42093a36) [#43091](https://github.com/vllm-project/vllm/pull/43091)
  [Model Runner V2][Spec Decode] Support spec decode with draft model (#43091)
  _Files: `vllm/config/vllm.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/spec_decode/__init__.py`, `vllm/v1/worker/gpu/spec_decode/draft_model/__init__.py` _+2 more__

## Quantization  (14 commits)

- **2026-10-05** [`edca360f13`](https://github.com/vllm-project/vllm/commit/edca360f13) [#59443](https://github.com/vllm-project/vllm/pull/59443)
  [Bugfix][Qwen4Exp] Load PLE tables unquantized under Quark checkpoints (#59443)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/common/ngram_embedding.py`_
- **2026-10-04** [`155d23cb00`](https://github.com/vllm-project/vllm/commit/155d23cb00) [#59159](https://github.com/vllm-project/vllm/pull/59159)
  [Bugfix][XPU] Make DeepSeek V4 FP8 sparse decode graph-capturable (#59159)
  _Files: `vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py`_
- **2026-10-02** [`10f6ab01a9`](https://github.com/vllm-project/vllm/commit/10f6ab01a9) [#59800](https://github.com/vllm-project/vllm/pull/59800)
  [Perf] Use value-only reduction for native per-token FP8 quantization (#59800)
  _Files: `vllm/model_executor/layers/quantization/input_quant_fp8.py`_
- **2026-10-02** [`30e956fad3`](https://github.com/vllm-project/vllm/commit/30e956fad3) [#59135](https://github.com/vllm-project/vllm/pull/59135)
  [Docs] Fix stale W4A16 NVFP4 default kernel in ModelOpt docs (#59135)
  _Files: `docs/features/quantization/modelopt.md`, `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-10-02** [`f0b4b36890`](https://github.com/vllm-project/vllm/commit/f0b4b36890) [#56050](https://github.com/vllm-project/vllm/pull/56050)
  [Bugfix][Quantization] Detect NVFP4 in ModelOpt mixed-precision checkpoints (#56050)
  _Files: `tests/compile/fusions_e2e/models.py`, `tests/compile/fusions_e2e/test_tp1_quant.py`, `tests/config/test_modelopt_mixed_nvfp4.py`, `vllm/config/model.py`_
- **2026-10-02** [`bdfb02674f`](https://github.com/vllm-project/vllm/commit/bdfb02674f) [#56063](https://github.com/vllm-project/vllm/pull/56063)
  [XPU][Kernel] Tune Triton W8A8 block-FP8 GEMM for Intel B70 (#56063)
  _Files: `benchmarks/kernels/benchmark_w8a8_block_fp8.py`, `vllm/model_executor/layers/quantization/utils/configs/N=1536,K=7168,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/quantization/utils/configs/N=2048,K=11008,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/quantization/utils/configs/N=2048,K=2048,device_name=Intel(R)_Arc(TM)_Pro_B70_Graphics,dtype=fp8_w8a8,block_shape=[128,128].json` _+23 more__
- **2026-09-30** [`c32513b99d`](https://github.com/vllm-project/vllm/commit/c32513b99d) [#59431](https://github.com/vllm-project/vllm/pull/59431)
  Add support for unquantized ngram in CT format (#59431)
  _Files: `vllm/models/qwen4_exp/common/ngram_embedding.py`_
- **2026-09-30** [`72e7874fa6`](https://github.com/vllm-project/vllm/commit/72e7874fa6) [#59149](https://github.com/vllm-project/vllm/pull/59149)
  [Hardware][Power] Enable W4A16 (AWQ & GPTQ) quantization on POWER10 using VSX (#59149)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_vsx.hpp`, `csrc/cpu/cpu_wna16.cpp`, `csrc/cpu/torch_bindings.cpp` _+3 more__
- **2026-09-30** [`d71f662606`](https://github.com/vllm-project/vllm/commit/d71f662606) [#58083](https://github.com/vllm-project/vllm/pull/58083)
  [Bugfix][Model][CPU] Fix Mamba2 quantized in_proj weight and scale loading for TP >1 (#58083)
  _Files: `vllm/model_executor/layers/mamba/mamba_mixer2.py`_
- **2026-09-30** [`5faf81a429`](https://github.com/vllm-project/vllm/commit/5faf81a429) [#58268](https://github.com/vllm-project/vllm/pull/58268)
  [CPU][Whisper] Support W4A16 quantized Whisper on the CPU WNA16 kernel (#58268)
  _Files: `tests/kernels/test_awq_int4_to_int8.py`, `tests/models/multimodal/generation/test_whisper.py`, `tests/quantization/test_cpu_wna16.py`, `vllm/_custom_ops.py` _+1 more__
- **2026-09-29** [`f4917dadc8`](https://github.com/vllm-project/vllm/commit/f4917dadc8) [#57163](https://github.com/vllm-project/vllm/pull/57163)
  [Bugfix][Quantization] Stop sleep(level=2) from zeroing compressed-tensors KV scales (#57163)
  _Files: `tests/basic_correctness/memory/sleep_mode/test_sleep_mode.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`_
- **2026-09-29** [`77e52645e9`](https://github.com/vllm-project/vllm/commit/77e52645e9) [#58142](https://github.com/vllm-project/vllm/pull/58142)
  [Bugfix][Model] MiMo: keep fused fp8 qkv_proj pairing state across weight-loading calls (#58142)
  _Files: `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/mimo_v2_mtp.py`_
- **2026-09-28** [`3bd7302396`](https://github.com/vllm-project/vllm/commit/3bd7302396) [#58987](https://github.com/vllm-project/vllm/pull/58987)
  [XPU] skip test_online_quantization_loads_real_weights (#58987)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`_
- **2026-09-28** [`5eaa50f151`](https://github.com/vllm-project/vllm/commit/5eaa50f151) [#58515](https://github.com/vllm-project/vllm/pull/58515)
  [CPU] Build CPU wheels on Ubuntu 22.04 with AMX-FP8 support (#58515)
  _Files: `docker/Dockerfile.cpu`_

## LoRA  (11 commits)

- **2026-10-05** [`f9c9e8ac24`](https://github.com/vllm-project/vllm/commit/f9c9e8ac24) [#60024](https://github.com/vllm-project/vllm/pull/60024)
  [LoRA] Remove tensorizer (#60024)
  _Files: `docs/models/extensions/tensorizer.md`, `examples/features/tensorize_vllm_model.py`, `tests/entrypoints/openai/completion/test_tensorizer_entrypoint.py`, `tests/lora/test_llama_tp.py` _+5 more__
- **2026-10-04** [`1388100560`](https://github.com/vllm-project/vllm/commit/1388100560) [#59377](https://github.com/vllm-project/vllm/pull/59377)
  [Kernel][LoRA] Add deterministic split-K=8 LoRA shrink for batch invariance (#59377)
  _Files: `.buildkite/test_areas/misc.yaml`, `docs/features/batch_invariance.md`, `tests/v1/determinism/test_lora_shrink_batch_invariant.py`, `vllm/lora/ops/triton_ops/kernel_utils.py` _+1 more__
- **2026-10-01** [`a5105dba05`](https://github.com/vllm-project/vllm/commit/a5105dba05) [#59321](https://github.com/vllm-project/vllm/pull/59321)
  [Frontend] Port Step-3.5 parsers to the streaming parser engine (#59321)
  _Files: `docs/features/reasoning_outputs.md`, `docs/features/tool_calling.md`, `tests/parser/engine/test_step3p5.py`, `tests/parser/engine/trace_builder.py` _+8 more__
- **2026-10-01** [`c055c1e075`](https://github.com/vllm-project/vllm/commit/c055c1e075) [#59335](https://github.com/vllm-project/vllm/pull/59335)
  [Core] Include the LoRA path in prefix-cache block hashes (#59335)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/entrypoints/openai/models/serving.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-09-30** [`713ec07655`](https://github.com/vllm-project/vllm/commit/713ec07655) [#55781](https://github.com/vllm-project/vllm/pull/55781)
  [Frontend][RL] Track HTTP weight operation outcomes and concurrency (#55781)
  _Files: `rust/src/metrics/src/api_server.rs`, `rust/src/server/src/routes/tests.rs`, `rust/src/server/src/routes/weight_transfer.rs`, `tests/entrypoints/serve/dev/rlhf/test_weight_operation_metrics.py` _+4 more__
- **2026-09-30** [`bec710fccf`](https://github.com/vllm-project/vllm/commit/bec710fccf) [#59344](https://github.com/vllm-project/vllm/pull/59344)
  [CI] Fix mock type narrowing in LoRA serving test (#59344)
  _Files: `tests/entrypoints/serve/lora/test_serving_models.py`_
- **2026-09-30** [`105a4e097b`](https://github.com/vllm-project/vllm/commit/105a4e097b) [#59286](https://github.com/vllm-project/vllm/pull/59286)
  [Bugfix][Frontend] Reject LoRA adapters named after a served model (#59286)
  _Files: `tests/entrypoints/serve/lora/test_serving_models.py`, `vllm/entrypoints/openai/models/serving.py`_
- **2026-09-29** [`e05095c9e1`](https://github.com/vllm-project/vllm/commit/e05095c9e1) [#59048](https://github.com/vllm-project/vllm/pull/59048)
  [Rust Frontend] Feed parser tests and benchmarks attributed input (#59048)
  _Files: `rust/src/chat/tests/roundtrip.rs`, `rust/src/parser/Cargo.toml`, `rust/src/parser/benches/gemma4.rs`, `rust/src/parser/benches/kimi_k3.rs` _+3 more__
- **2026-09-29** [`17cc3cd80e`](https://github.com/vllm-project/vllm/commit/17cc3cd80e) [#56575](https://github.com/vllm-project/vllm/pull/56575)
  [Model] Engine based plamo3 parser (#56575)
  _Files: `tests/parser/engine/test_plamo3.py`, `tests/parser/engine/test_replay.py`, `tests/parser/engine/trace_builder.py`, `tests/tool_parsers/test_structural_tag_registry.py` _+10 more__
- **2026-09-28** [`953f90d25f`](https://github.com/vllm-project/vllm/commit/953f90d25f) [#57766](https://github.com/vllm-project/vllm/pull/57766)
  [LoRA] Support variable num_labels for sequence classification (#57766)
  _Files: `docs/features/lora.md`, `tests/lora/test_sequence_classification.py`, `vllm/config/lora.py`, `vllm/engine/arg_utils.py` _+4 more__
- **2026-09-28** [`4a190dc518`](https://github.com/vllm-project/vllm/commit/4a190dc518) [#58884](https://github.com/vllm-project/vllm/pull/58884)
  [Model] Enable LoRA support for RobertaForSequenceClassification (#58884)
  _Files: `docs/models/pooling_models/scoring.md`, `vllm/model_executor/models/roberta.py`_

## KV Cache / Offload  (7 commits)

- **2026-10-05** [`0c16eee3f1`](https://github.com/vllm-project/vllm/commit/0c16eee3f1) [#57816](https://github.com/vllm-project/vllm/pull/57816)
  [Bugfix][KV Offload] Reset SimpleCPU eager-store placement state on MRV2 resume (#57816)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-10-04** [`18f8f96025`](https://github.com/vllm-project/vllm/commit/18f8f96025) [#59862](https://github.com/vllm-project/vllm/pull/59862)
  [Bugfix][KV Offload] Release pending CPU lookup pins on cache reset (#59862)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-10-02** [`d648847fe4`](https://github.com/vllm-project/vllm/commit/d648847fe4) [#59229](https://github.com/vllm-project/vllm/pull/59229)
  [CI][Kimi-K3] Test prefix cache reuse with KV offload, P/D and DCP (#59229)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/kimi_k3/test_prefix_cache.py`_
- **2026-09-30** [`73c7cae4d7`](https://github.com/vllm-project/vllm/commit/73c7cae4d7) [#58725](https://github.com/vllm-project/vllm/pull/58725)
  [Bugfix][HiSparse] Stop the host pool feeding device KV cache residency metrics (#58725)
  _Files: `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-09-30** [`279012f94d`](https://github.com/vllm-project/vllm/commit/279012f94d) [#59456](https://github.com/vllm-project/vllm/pull/59456)
  [Docs] Add @wzhao18 to NVIDIA integration and kv offloading code owners (#59456)
  _Files: `.github/CODEOWNERS`, `docs/governance/committers.md`_
- **2026-09-29** [`be255076d0`](https://github.com/vllm-project/vllm/commit/be255076d0) [#58021](https://github.com/vllm-project/vllm/pull/58021)
  [Bugfix] Reject a prefix_match_unit that a single KV cache group cannot honor (#58021)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-09-28** [`a2be4d3cc7`](https://github.com/vllm-project/vllm/commit/a2be4d3cc7) [#58961](https://github.com/vllm-project/vllm/pull/58961)
  [Bugfix][Qwen4Exp] Release the profiling KV cache held by QSA key views (#58961)
  _Files: `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/models/qwen4_exp/common/qsa_cache.py`_

## Docs  (7 commits)

- **2026-10-02** [`6e517b15c1`](https://github.com/vllm-project/vllm/commit/6e517b15c1) [#58476](https://github.com/vllm-project/vllm/pull/58476)
  [Docs] Add ERNIE 4.5 to batch invariance tested models (#58476)
  _Files: `docs/features/batch_invariance.md`_
- **2026-10-02** [`7b6be2f1f4`](https://github.com/vllm-project/vllm/commit/7b6be2f1f4) [#59459](https://github.com/vllm-project/vllm/pull/59459)
  [Docs] Add Reviewers page (#59459)
  _Files: `docs/community/reviewers.md`, `docs/contributing/README.md`, `pyproject.toml`_
- **2026-10-01** [`a47e4a5568`](https://github.com/vllm-project/vllm/commit/a47e4a5568) [#59361](https://github.com/vllm-project/vllm/pull/59361)
  [Doc] Score centering via top-k processed logprobs (#59361)
  _Files: `docs/training/sampling_mask.md`_
- **2026-09-30** [`8fb16ea5a6`](https://github.com/vllm-project/vllm/commit/8fb16ea5a6) [#57084](https://github.com/vllm-project/vllm/pull/57084)
  [Docs] Add PR checklist skill for coding agents (#57084)
  _Files: `.agents/skills/pr-checklist/SKILL.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `AGENTS.md`, `docs/contributing/model/basic.md`_
- **2026-09-30** [`8873ac83bb`](https://github.com/vllm-project/vllm/commit/8873ac83bb) [#59369](https://github.com/vllm-project/vllm/pull/59369)
  [Docs] Add @gau-nernst to CODEOWNERS and committers (#59369)
  _Files: `.github/CODEOWNERS`, `docs/governance/committers.md`_
- **2026-09-30** [`b22494cc0c`](https://github.com/vllm-project/vllm/commit/b22494cc0c) [#59411](https://github.com/vllm-project/vllm/pull/59411)
  [Docs] Reinstate docs build gate for PRs (#59411)
  _Files: `.github/mergify.yml`, `docs/contributing/README.md`, `docs/pre_run_check.sh`_
- **2026-09-29** [`a96ee5935d`](https://github.com/vllm-project/vllm/commit/a96ee5935d) [#50584](https://github.com/vllm-project/vllm/pull/50584)
  [MRV2] Add DRY as a custom logits processor example (#50584)
  _Files: `examples/features/logits_processor/README.md`, `examples/features/logits_processor/dry.py`, `tests/v1/sample/test_dry.py`_

## Perf / Benchmark  (6 commits)

- **2026-10-01** [`f3b77eff64`](https://github.com/vllm-project/vllm/commit/f3b77eff64) [#59247](https://github.com/vllm-project/vllm/pull/59247)
  [Rust][Benchmark] Warn when temperature is left to the server default (#59247)
  _Files: `rust/src/bench/src/config.rs`_
- **2026-09-30** [`1b77cc3d67`](https://github.com/vllm-project/vllm/commit/1b77cc3d67) [#57305](https://github.com/vllm-project/vllm/pull/57305)
  [Benchmark] Add sweep warmup and failure recovery (#57305)
  _Files: `docs/benchmarking/sweeps.md`, `tests/benchmarks/sweep/test_param_sweep.py`, `vllm/benchmarks/sweep/serve.py`, `vllm/benchmarks/sweep/serve_workload.py`_
- **2026-09-29** [`4e0a414c44`](https://github.com/vllm-project/vllm/commit/4e0a414c44) [#58495](https://github.com/vllm-project/vllm/pull/58495)
  [Kernel][Perf] Add TP=2/4/8 per-rank shapes to the sm_120 batch-invariant matmul table (#58495)
  _Files: `vllm/model_executor/determinism/batch_invariant_configs.py`_
- **2026-09-28** [`3d5f4d4cd5`](https://github.com/vllm-project/vllm/commit/3d5f4d4cd5) [#57107](https://github.com/vllm-project/vllm/pull/57107)
  [Perf][Spec Decode] Avoid triton recompiles in the acceptance estimator (#57107)
  _Files: `vllm/v1/worker/gpu/spec_decode/acceptance_estimator.py`_
- **2026-09-28** [`e7c903609f`](https://github.com/vllm-project/vllm/commit/e7c903609f) [#58400](https://github.com/vllm-project/vllm/pull/58400)
  [Perf][MRV2] Allow FULL decode graphs for one-token prompt tails (#58400)
  _Files: `tests/v1/spec_decode/test_dynamic_sd_cug.py`, `tests/v1/worker/test_gpu_batch_ordering.py`, `tests/v1/worker/test_gpu_batch_shard.py`, `tests/v1/worker/test_mamba_hybrid_model_state.py` _+8 more__
- **2026-09-28** [`af7f9488c2`](https://github.com/vllm-project/vllm/commit/af7f9488c2) [#54628](https://github.com/vllm-project/vllm/pull/54628)
  [Benchmark] Add Responses API backend to vllm bench serve (#54628)
  _Files: `docs/benchmarking/cli.md`, `tests/benchmarks/test_responses_request_func.py`, `vllm/benchmarks/datasets/datasets.py`, `vllm/benchmarks/lib/endpoint_request_func.py` _+1 more__

## Compilation / CUDA Graph  (4 commits)

- **2026-09-30** [`d5ee309314`](https://github.com/vllm-project/vllm/commit/d5ee309314) [#48133](https://github.com/vllm-project/vllm/pull/48133)
  [UX] Tag torch.compile log lines with the component being compiled (#48133)
  _Files: `vllm/compilation/backends.py`, `vllm/compilation/decorators.py`, `vllm/compilation/monitor.py`_
- **2026-09-29** [`cb4f016c5d`](https://github.com/vllm-project/vllm/commit/cb4f016c5d) [#52142](https://github.com/vllm-project/vllm/pull/52142)
  [Bugfix] Fix standalone torch.compile cache loading after relocation (#52142)
  _Files: `tests/compile/test_compiler_interface.py`, `vllm/compilation/compiler_interface.py`_
- **2026-09-29** [`4e59d53ab5`](https://github.com/vllm-project/vllm/commit/4e59d53ab5) [#59079](https://github.com/vllm-project/vllm/pull/59079)
  [MRV2] Support stock torch.compile mode (#59079)
  _Files: `tests/compile/fullgraph/test_basic_correctness.py`, `tests/compile/test_config.py`, `tests/compile/test_wrapper.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py` _+3 more__
- **2026-09-29** [`b39f760cc7`](https://github.com/vllm-project/vllm/commit/b39f760cc7) [#57299](https://github.com/vllm-project/vllm/pull/57299)
  [torch.compile] Canonicalize functionalized split slices for fusion pa… (#57299)
  _Files: `tests/compile/passes/test_split_coalescing.py`, `vllm/compilation/passes/utility/split_coalescing.py`_

---
_Generated 2026-10-05 17:11 UTC_