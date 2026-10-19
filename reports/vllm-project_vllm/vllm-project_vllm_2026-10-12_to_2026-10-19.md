# vllm-project/vllm — Weekly Change Report
**Period:** 2026-10-12 → 2026-10-19  |  **Total commits:** 512

## ✨ New Features This Week

- **2026-10-19** [#62329](https://github.com/vllm-project/vllm/pull/62329) — [Model] Support hotwords for MOSS-Transcribe-Diarize (#62329)
- **2026-10-19** [#61727](https://github.com/vllm-project/vllm/pull/61727) — Add Step-5 Preview support (#61727)
- **2026-10-19** [#55537](https://github.com/vllm-project/vllm/pull/55537) — [Kernel] Reject unsupported layouts in CUTLASS 3.x scaled_mm (#55537)
- **2026-10-19** [#53987](https://github.com/vllm-project/vllm/pull/53987) — [Spec Decode][ROCm] Add FLy: entropy-gated deferred verification for draft-model speculative decoding (#53987)
- **2026-10-19** [#62183](https://github.com/vllm-project/vllm/pull/62183) — [Feature][PCP] Support APC and encoder-side SWA bounded replay for DeepSeek-V4.1-Flash (#62183)
- **2026-10-19** [#51488](https://github.com/vllm-project/vllm/pull/51488) — [Core] Reject new requests while generation is paused (#51488)
- **2026-10-19** [#62375](https://github.com/vllm-project/vllm/pull/62375) — [Benchmark][XPU] Support XPU in forward bench graph capture/profiling (#62375)
- **2026-10-19** [#55490](https://github.com/vllm-project/vllm/pull/55490) — [Fast Start] support ep (#55490)
- **2026-10-19** [#56835](https://github.com/vllm-project/vllm/pull/56835) — [XPU] [Feature] Adding triton/sycl GDN toggle (#56835)
- **2026-10-19** [#50396](https://github.com/vllm-project/vllm/pull/50396) — [Quantization][Autoround][ARK] Add ARK W4A16(moe) Support (#50396)
- _…and 87 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-19** [`973dbf8071`](https://github.com/vllm-project/vllm/commit/973dbf8071) [#62273](https://github.com/vllm-project/vllm/pull/62273) — [Doc][ROCm] Align Kimi-K3 MI355X recipe with InferenceX #4215 (#62273)
- **2026-10-19** [`ffa18e55a4`](https://github.com/vllm-project/vllm/commit/ffa18e55a4) [#61345](https://github.com/vllm-project/vllm/pull/61345) — [ROCm][DSv4] Require explicit MXFP4 opt-in for MegaMoE shared-expert fusion (#61345)
- **2026-10-19** [`3e96f9cf63`](https://github.com/vllm-project/vllm/commit/3e96f9cf63) [#62276](https://github.com/vllm-project/vllm/pull/62276) — [ROCm][CI] Bump the ROCm 10 image to torch 2.13 (#62276)
- **2026-10-19** [`5bc26717dd`](https://github.com/vllm-project/vllm/commit/5bc26717dd) [#60816](https://github.com/vllm-project/vllm/pull/60816) — [ROCm][Qwen4Exp] Remove the Qwen3.8-Flash-Next TEP8 MXFP4 emulation guard (#60816)
- **2026-10-19** [`fb61ac07bd`](https://github.com/vllm-project/vllm/commit/fb61ac07bd) [#61943](https://github.com/vllm-project/vllm/pull/61943) — [ROCm][Perf] Use AITER top-k for the DeepSeek-V3.2/GLM-5 sparse indexer (#61943)
- **2026-10-19** [`c1dc2e9cf9`](https://github.com/vllm-project/vllm/commit/c1dc2e9cf9) [#53987](https://github.com/vllm-project/vllm/pull/53987) — [Spec Decode][ROCm] Add FLy: entropy-gated deferred verification for draft-model speculative decoding (#53987)
- **2026-10-19** [`e7023e596d`](https://github.com/vllm-project/vllm/commit/e7023e596d) [#61726](https://github.com/vllm-project/vllm/pull/61726) — [Bugfix][ROCm][MoRIIO] Support heterogeneous TP in WRITE mode for all attention and mamba layers (#61726)
- **2026-10-19** [`e68efc685a`](https://github.com/vllm-project/vllm/commit/e68efc685a) [#62363](https://github.com/vllm-project/vllm/pull/62363) — [CI][AMD] Split LM Eval Small by CDNA generation, unify AMD step titles, clone MoRIIO steps into test-amd.yaml (#62363)
- **2026-10-19** [`6a0b146c16`](https://github.com/vllm-project/vllm/commit/6a0b146c16) [#62371](https://github.com/vllm-project/vllm/pull/62371) — [ROCm][Compile] Fuse AITER static FP8 quant into MLA attention output (#62371)
- **2026-10-19** [`e719b41e22`](https://github.com/vllm-project/vllm/commit/e719b41e22) [#62131](https://github.com/vllm-project/vllm/pull/62131) — [ROCm][Perf][DSv4.1] Mono decode for the DSpark draft layers (#62131)
- **2026-10-19** [`c07c59f821`](https://github.com/vllm-project/vllm/commit/c07c59f821) [#62241](https://github.com/vllm-project/vllm/pull/62241) — [ROCm][Bugfix] Release vLLM's communicators on external-launcher shutdown (#62241)
- **2026-10-19** [`0ee62b99b6`](https://github.com/vllm-project/vllm/commit/0ee62b99b6) [#62286](https://github.com/vllm-project/vllm/pull/62286) — [ROCm][CI] Contain the MI355 DP + EP exit-time abort (#62286)
- **2026-10-19** [`8e5cae09f1`](https://github.com/vllm-project/vllm/commit/8e5cae09f1) [#62280](https://github.com/vllm-project/vllm/pull/62280) — [ROCm][CI] Pin Inductor pointwise configs in the MoRIIO dummy-weight P/D test (#62280)
- **2026-10-18** [`82a24bb82d`](https://github.com/vllm-project/vllm/commit/82a24bb82d) [#62274](https://github.com/vllm-project/vllm/pull/62274) — [Bugfix][ROCm] Only set inductor batch_invariant when torch has it (#62274)
- **2026-10-18** [`e80b6c642f`](https://github.com/vllm-project/vllm/commit/e80b6c642f) [#61819](https://github.com/vllm-project/vllm/pull/61819) — [ROCm][DSv4] Overlap the unfused shared expert with AITER MegaMoE (#61819)
- **2026-10-18** [`494663940b`](https://github.com/vllm-project/vllm/commit/494663940b) [#61454](https://github.com/vllm-project/vllm/pull/61454) — [Qwen4Exp] Clean up HC and PLE implementations for Qwen3.8-Flash-Next (#61454)
- **2026-10-18** [`da9134bc89`](https://github.com/vllm-project/vllm/commit/da9134bc89) [#62161](https://github.com/vllm-project/vllm/pull/62161) — [ROCm][CI] Give the MoE parallel-launch watchdog room for AITER JIT builds (#62161)
- **2026-10-18** [`b2456c622b`](https://github.com/vllm-project/vllm/commit/b2456c622b) [#58761](https://github.com/vllm-project/vllm/pull/58761) — [ROCm][CI] Make ROCm 10.0 the default image; keep ROCm 7.2 as -rocm72 (#58761)
- **2026-10-18** [`03ee2e134d`](https://github.com/vllm-project/vllm/commit/03ee2e134d) [#62213](https://github.com/vllm-project/vllm/pull/62213) — [CI][ROCm] Fix order-dependent test_rocm_aiter_sampler_defers_import (CPU tensors hit Triton) (#62213)
- **2026-10-17** [`2067297b2f`](https://github.com/vllm-project/vllm/commit/2067297b2f) [#61278](https://github.com/vllm-project/vllm/pull/61278) — [ROCm][Perf] Use AITER tuned configs to select a4w4 gemm kernel instead of env var (#61278)
- **2026-10-17** [`3bf25c5097`](https://github.com/vllm-project/vllm/commit/3bf25c5097) [#62087](https://github.com/vllm-project/vllm/pull/62087) — [CI][Bugfix] Ignore AMD CI webhook no-op builds in /amd-ci run and retry (#62087)
- **2026-10-17** [`41b8c15809`](https://github.com/vllm-project/vllm/commit/41b8c15809) [#60544](https://github.com/vllm-project/vllm/pull/60544) — [Feature][MoRIIO] Support hybrid WRITE transfers with DSpark (#60544)
- **2026-10-17** [`a0e7137c4b`](https://github.com/vllm-project/vllm/commit/a0e7137c4b) [#61960](https://github.com/vllm-project/vllm/pull/61960) — [CI][ROCm][Bugfix] DeepSeek V4.1: don't pass expert intermediate padding to AITER (#61960)
- **2026-10-17** [`f019e3e105`](https://github.com/vllm-project/vllm/commit/f019e3e105) [#52968](https://github.com/vllm-project/vllm/pull/52968) — [ROCm] attn res + sigmoid_mul + conv fusions (#52968)
- **2026-10-16** [`28e92eeff2`](https://github.com/vllm-project/vllm/commit/28e92eeff2) [#59552](https://github.com/vllm-project/vllm/pull/59552) — [ROCm][Perf][Kimi-K3] Use AITER Gluon chunk_kda for KDA prefill (#59552)
- **2026-10-16** [`cc2e4fecf2`](https://github.com/vllm-project/vllm/commit/cc2e4fecf2) [#52831](https://github.com/vllm-project/vllm/pull/52831) — [ROCm] [fusion] support ROCm aiter fusion of per tensor quant + rmsnorm (#52831)
- **2026-10-16** [`5bf3d9f665`](https://github.com/vllm-project/vllm/commit/5bf3d9f665) [#59824](https://github.com/vllm-project/vllm/pull/59824) — [ROCm][Kimi-K3] Support DSpark adaptive verification on MI355X (#59824)
- **2026-10-16** [`307c5844ad`](https://github.com/vllm-project/vllm/commit/307c5844ad) [#62048](https://github.com/vllm-project/vllm/pull/62048) — [ROCm][CI] Enable batch invariance for the ngram scheduling accuracy test (#62048)
- **2026-10-16** [`e7a5bdb454`](https://github.com/vllm-project/vllm/commit/e7a5bdb454) [#62053](https://github.com/vllm-project/vllm/pull/62053) — [ROCm][CI] Move Spec Decode Speculators + MTP to MI355 (#62053)
- **2026-10-16** [`706791d516`](https://github.com/vllm-project/vllm/commit/706791d516) [#61955](https://github.com/vllm-project/vllm/pull/61955) — [CI][AMD] Move 17 test groups from MI300 to MI355 and test large DeepSeek/Nemotron evals on AITER (#61955)
- **2026-10-16** [`76081b9ee4`](https://github.com/vllm-project/vllm/commit/76081b9ee4) [#61921](https://github.com/vllm-project/vllm/pull/61921) — [Bugfix][Model] Honor quantization config in Inkling MTP (#61921)
- **2026-10-16** [`8e25bbca19`](https://github.com/vllm-project/vllm/commit/8e25bbca19) [#61843](https://github.com/vllm-project/vllm/pull/61843) — [Refactor] Remove dead code multiple places (#61843)
- **2026-10-16** [`8a6c0449b3`](https://github.com/vllm-project/vllm/commit/8a6c0449b3) [#58589](https://github.com/vllm-project/vllm/pull/58589) — [Bugfix][ROCm][GLM-5.2] Stop forcing skip_final_all_reduce on AMD DSA model path (#58589)
- **2026-10-16** [`fa75d3456d`](https://github.com/vllm-project/vllm/commit/fa75d3456d) [#59857](https://github.com/vllm-project/vllm/pull/59857) — [Feature][PCP] Add DeepSeek-V4.1-Flash support (#59857)
- **2026-10-16** [`074c83a09a`](https://github.com/vllm-project/vllm/commit/074c83a09a) [#61932](https://github.com/vllm-project/vllm/pull/61932) — [CI][Intel] Skip ROCm-only test_topk_gating_enabled_by_cdna on XPU (#61932)
- **2026-10-16** [`b466fbacd2`](https://github.com/vllm-project/vllm/commit/b466fbacd2) [#61895](https://github.com/vllm-project/vllm/pull/61895) — [ROCm][Perf] Any-shape low-latency MoE router GEMM on MI355 (#61895)
- **2026-10-16** [`29345f42a6`](https://github.com/vllm-project/vllm/commit/29345f42a6) [#61471](https://github.com/vllm-project/vllm/pull/61471) — [ROCm][Qwen4Exp] Support HC and MoE sequence parallelism on ROCm (#61471)
- **2026-10-16** [`ef38e8d006`](https://github.com/vllm-project/vllm/commit/ef38e8d006) [#42755](https://github.com/vllm-project/vllm/pull/42755) — [Model][Hardware][AMD][Kernel] Part 2/2 -> Enable e2e QK Norm + RoPE + KV Cache runtime fusion for Qwen3-30B-A3B on ROCM_ATTN (#42755)
- **2026-10-15** [`4a89316efa`](https://github.com/vllm-project/vllm/commit/4a89316efa) [#61713](https://github.com/vllm-project/vllm/pull/61713) — [Core] Drop the Ray driver-node GPU pin left over from the legacy executor (#61713)
- **2026-10-15** [`3f1e57225a`](https://github.com/vllm-project/vllm/commit/3f1e57225a) [#57392](https://github.com/vllm-project/vllm/pull/57392) — [ROCm][Perf][Kimi-K3] Use AITER Gluon KDA kernels for decode and spec decode (#57392)
- **2026-10-15** [`e711723352`](https://github.com/vllm-project/vllm/commit/e711723352) [#58800](https://github.com/vllm-project/vllm/pull/58800) — [ROCm] gfx1250 optimizations and model enablement (#58800)
- **2026-10-15** [`9b99ccb56b`](https://github.com/vllm-project/vllm/commit/9b99ccb56b) [#61861](https://github.com/vllm-project/vllm/pull/61861) — [CI] Shard the AMD mirrors of the DP, RayExecutorV2 and batch invariance steps automatically (#61861)
- **2026-10-15** [`0c25849292`](https://github.com/vllm-project/vllm/commit/0c25849292) [#59406](https://github.com/vllm-project/vllm/pull/59406) — [ROCm][Perf][Bugfix] Probe the preshuffled FP4 GEMM config by logical K (#59406)
- **2026-10-15** [`c414bf0295`](https://github.com/vllm-project/vllm/commit/c414bf0295) [#61817](https://github.com/vllm-project/vllm/pull/61817) — [CI] Shard four AMD mirrors automatically (#61817)
- **2026-10-15** [`16532876e7`](https://github.com/vllm-project/vllm/commit/16532876e7) [#61860](https://github.com/vllm-project/vllm/pull/61860) — [CI] Shard four more AMD mirrors automatically (#61860)
- **2026-10-15** [`105605b8e9`](https://github.com/vllm-project/vllm/commit/105605b8e9) [#60282](https://github.com/vllm-project/vllm/pull/60282) — [ROCm] Support DeepSeek-V4 hash routing in AITER Triton W4A16 MoE (#60282)
- **2026-10-15** [`47fd76e4ce`](https://github.com/vllm-project/vllm/commit/47fd76e4ce) [#56226](https://github.com/vllm-project/vllm/pull/56226) — [ROCm][Perf] Route softmax MoE top-k, including fused shared-expert sigmoid, through AITER topk_gating (#56226)
- **2026-10-15** [`011fa68ca9`](https://github.com/vllm-project/vllm/commit/011fa68ca9) [#55090](https://github.com/vllm-project/vllm/pull/55090) — [ROCm][Perf] Pad fp16/bf16 GEMM weight row stride for L2 cache (#55090)
- **2026-10-15** [`0951fc183c`](https://github.com/vllm-project/vllm/commit/0951fc183c) [#58689](https://github.com/vllm-project/vllm/pull/58689) — [ROCm][DSv4.1] Disambiguate ROCm attention class names (#58689)
- **2026-10-15** [`e8e1e96196`](https://github.com/vllm-project/vllm/commit/e8e1e96196) [#61262](https://github.com/vllm-project/vllm/pull/61262) — [ROCm][DSv4] AITER MegaMoE Fixed-Slot Dispatch For DeepSeek-V4 (#61262)
- **2026-10-15** [`365aaa77bd`](https://github.com/vllm-project/vllm/commit/365aaa77bd) [#56054](https://github.com/vllm-project/vllm/pull/56054) — [Bugfix][DSv4] Remap Quark MTP layer_quant_config onto draft prefixes (#56054)
- **2026-10-15** [`b965ee564d`](https://github.com/vllm-project/vllm/commit/b965ee564d) [#61392](https://github.com/vllm-project/vllm/pull/61392) — [Chore] Use upstream Transformers DeepseekV4Config (#61392)
- **2026-10-15** [`833665cded`](https://github.com/vllm-project/vllm/commit/833665cded) [#59596](https://github.com/vllm-project/vllm/pull/59596) — [ROCm][DI] Enable MoRI FP4 dispatch for mxfp4 w4a4 moe  (#59596)
- **2026-10-15** [`10d2c6083d`](https://github.com/vllm-project/vllm/commit/10d2c6083d) [#58151](https://github.com/vllm-project/vllm/pull/58151) — [ROCm][DSv4.1] Enable DSpark adaptive verification (#58151)
- **2026-10-15** [`f46021a7fa`](https://github.com/vllm-project/vllm/commit/f46021a7fa) [#57773](https://github.com/vllm-project/vllm/pull/57773) — [ROCm][Perf] Enable DPA+ETP prefill compute/comm dual-batch-overlap for DeepSeek-V4 (#57773)
- **2026-10-15** [`429a3da665`](https://github.com/vllm-project/vllm/commit/429a3da665) [#58585](https://github.com/vllm-project/vllm/pull/58585) — [Bugfix][ROCm][Disagg] Allow MoRIIO HMA per-layer block_len (#58585)
- **2026-10-15** [`2abd479aee`](https://github.com/vllm-project/vllm/commit/2abd479aee) [#61720](https://github.com/vllm-project/vllm/pull/61720) — [ROCm][CI] Add AMD job for DeepSeek-V4.1 Mono Decode Numerics (#61720)
- **2026-10-15** [`e57bb4ace7`](https://github.com/vllm-project/vllm/commit/e57bb4ace7) [#61712](https://github.com/vllm-project/vllm/pull/61712) — [Core] Remove the legacy Ray compiled-graph executor (#61712)
- **2026-10-15** [`8530aed2b7`](https://github.com/vllm-project/vllm/commit/8530aed2b7) [#61701](https://github.com/vllm-project/vllm/pull/61701) — [Spec Decode] Remove Medusa and MLP speculator support (#61701)
- **2026-10-14** [`273a04964e`](https://github.com/vllm-project/vllm/commit/273a04964e) [#61697](https://github.com/vllm-project/vllm/pull/61697) — [ROCm] Bump AITER to v0.1.25 and relax the DSv4.1 mono MoE tolerance (#61697)
- **2026-10-14** [`7840bede98`](https://github.com/vllm-project/vllm/commit/7840bede98) [#59678](https://github.com/vllm-project/vllm/pull/59678) — [ROCm][CI] Add AMD jobs for test groups that only exist in tes… (#59678)
- **2026-10-14** [`9a648b4649`](https://github.com/vllm-project/vllm/commit/9a648b4649) [#61654](https://github.com/vllm-project/vllm/pull/61654) — [ROCm][Kimi-K3] Don't read W_UK_T before weight loading in the MLA wrapper (#61654)
- **2026-10-14** [`2622ee21aa`](https://github.com/vllm-project/vllm/commit/2622ee21aa) [#59290](https://github.com/vllm-project/vllm/pull/59290) — [ROCm][BugFix] Don't use AITER rms_norm as an IR OP on gfx90a when AITER always on. (#59290)
- **2026-10-14** [`e96c822660`](https://github.com/vllm-project/vllm/commit/e96c822660) [#60990](https://github.com/vllm-project/vllm/pull/60990) — [Bugfix][ROCm][MiniMax-M3] Reject unbuilt index-head counts in the AITER indexer (#60990)
- **2026-10-14** [`06265beb25`](https://github.com/vllm-project/vllm/commit/06265beb25) [#60296](https://github.com/vllm-project/vllm/pull/60296) — [ROCm] Enable fp8 query for Triton attention (#60296)
- **2026-10-14** [`3f729dafcc`](https://github.com/vllm-project/vllm/commit/3f729dafcc) [#60753](https://github.com/vllm-project/vllm/pull/60753) — [Perf][ROCm][GLM-5.3-Flash] AITER prefill indexer topk (#60753)
- **2026-10-14** [`e534024e49`](https://github.com/vllm-project/vllm/commit/e534024e49) [#60907](https://github.com/vllm-project/vllm/pull/60907) — [ROCm][Bugfix][MLA] Fix FP8 MLA prefill unpad for interleave-padded heads (#60907)
- **2026-10-14** [`52a8cc5316`](https://github.com/vllm-project/vllm/commit/52a8cc5316) [#61650](https://github.com/vllm-project/vllm/pull/61650) — [ROCm][CI] Add dtype to the KDA metadata test's fake model config (#61650)
- **2026-10-14** [`355553ac22`](https://github.com/vllm-project/vllm/commit/355553ac22) [#58354](https://github.com/vllm-project/vllm/pull/58354) — [ROCm][Perf] Drop two dead per-step ops from the AITER sparse MLA metadata build (#58354)
- **2026-10-14** [`eaf25f675a`](https://github.com/vllm-project/vllm/commit/eaf25f675a) [#61032](https://github.com/vllm-project/vllm/pull/61032) — [NIXL] Prepare KV transfer descriptors as NIXL 1.5 strided lists (#61032)
- **2026-10-14** [`81503550f3`](https://github.com/vllm-project/vllm/commit/81503550f3) [#53123](https://github.com/vllm-project/vllm/pull/53123) — [ROCm] Disable AITER FP8/FP4 BMM for MLA by default (#53123)
- **2026-10-14** [`19aba3e4d5`](https://github.com/vllm-project/vllm/commit/19aba3e4d5) [#57797](https://github.com/vllm-project/vllm/pull/57797) — [Bugfix][RL] Load attention sinks through weight_loader for layerwise reload (#57797)
- **2026-10-14** [`f9b65c30c7`](https://github.com/vllm-project/vllm/commit/f9b65c30c7) [#60645](https://github.com/vllm-project/vllm/pull/60645) — [ROCm][Perf] Make AITER FlyDSL GDN prefill default on gfx942/gfx950 (#60645)
- **2026-10-14** [`ec8a372566`](https://github.com/vllm-project/vllm/commit/ec8a372566) [#61559](https://github.com/vllm-project/vllm/pull/61559) — [ROCm][Bugfix] Pin AITER back to v0.1.24.post1 for DSv4.1 mono decode numerics (#61559)
- **2026-10-14** [`30e79c3a76`](https://github.com/vllm-project/vllm/commit/30e79c3a76) [#52183](https://github.com/vllm-project/vllm/pull/52183) — [Core] Update PyTorch to 2.14.0, torchvision to 0.29.0, triton to 3.8.0 (release channel) (#52183)
- **2026-10-14** [`3ccc0a90b6`](https://github.com/vllm-project/vllm/commit/3ccc0a90b6) [#59625](https://github.com/vllm-project/vllm/pull/59625) — [KV Connector] Support sleep mode with MooncakeConnector over RDMA (#59625)
- **2026-10-14** [`2521446ac8`](https://github.com/vllm-project/vllm/commit/2521446ac8) [#61378](https://github.com/vllm-project/vllm/pull/61378) — [ROCm][Perf] Enqueue the default chain first in CSA/HCA at small batch sizes for DeepSeek-V4 (#61378)
- **2026-10-14** [`a1f51a0226`](https://github.com/vllm-project/vllm/commit/a1f51a0226) [#58555](https://github.com/vllm-project/vllm/pull/58555) — [ROCm][MLA] Route gfx942 DCP causal multi-token verify to Triton split-KV decode (#58555)
- **2026-10-14** [`4e0681ed56`](https://github.com/vllm-project/vllm/commit/4e0681ed56) [#56273](https://github.com/vllm-project/vllm/pull/56273) — [Quantization] Support packed NVFP4 Qwen4Exp PLE embeddings (#56273)
- **2026-10-13** [`f43d7e1a0f`](https://github.com/vllm-project/vllm/commit/f43d7e1a0f) [#60679](https://github.com/vllm-project/vllm/pull/60679) — [CI][AMD] Gate Aiter MHA FA on dtype (#60679)
- **2026-10-13** [`7a9d3db896`](https://github.com/vllm-project/vllm/commit/7a9d3db896) [#61230](https://github.com/vllm-project/vllm/pull/61230) — [ROCm] Bump ROCm base images to AITER v1.25.0 (#61230)
- **2026-10-13** [`67516b6c42`](https://github.com/vllm-project/vllm/commit/67516b6c42) [#61207](https://github.com/vllm-project/vllm/pull/61207) — [Bugfix][ROCm][Kimi-K3] Stage fused KDA decode weights after loading (#61207)
- **2026-10-13** [`93d0bd9d50`](https://github.com/vllm-project/vllm/commit/93d0bd9d50) [#61420](https://github.com/vllm-project/vllm/pull/61420) — [ROCm][CI] Drop the -inf padding check from the AITER MQA logits test (#61420)
- **2026-10-13** [`c068db0e1d`](https://github.com/vllm-project/vllm/commit/c068db0e1d) [#58918](https://github.com/vllm-project/vllm/pull/58918) — [Bugfix][Compile] Replace Transformers AOT caching with graph caching (#58918)
- **2026-10-13** [`e83222396f`](https://github.com/vllm-project/vllm/commit/e83222396f) [#57199](https://github.com/vllm-project/vllm/pull/57199) — [ROCm][Perf] W4A16: speed up skinny GEMM decode, including speculative batches (#57199)
- **2026-10-13** [`f395a6b1ad`](https://github.com/vllm-project/vllm/commit/f395a6b1ad) [#46754](https://github.com/vllm-project/vllm/pull/46754) — [ROCM][Bugfix] Deferring to TRITON_ATTN backend for Prefix lm models instead of ROCM_ATTN and fixed minor bug in Gemma3 Multimodal code (#46754)
- **2026-10-13** [`7342dc0317`](https://github.com/vllm-project/vllm/commit/7342dc0317) [#60638](https://github.com/vllm-project/vllm/pull/60638) — [MoRIIO] Require pending remote prefill for READ cache hits (#60638)
- **2026-10-13** [`24aa1191f4`](https://github.com/vllm-project/vllm/commit/24aa1191f4) [#61350](https://github.com/vllm-project/vllm/pull/61350) — [ROCm][Bugfix] Run the AITER AR+RMSNorm fallback test on the platform… (#61350)
- **2026-10-13** [`2cc2e68d1c`](https://github.com/vllm-project/vllm/commit/2cc2e68d1c) [#60043](https://github.com/vllm-project/vllm/pull/60043) — [Core][Mamba] Remove leftovers of mamba_cache_mode="all" (#60043)
- **2026-10-13** [`a6009ea85b`](https://github.com/vllm-project/vllm/commit/a6009ea85b) [#61149](https://github.com/vllm-project/vllm/pull/61149) — [Kernel][Build] Bump DeepGEMM to the 26/09/30 release and adapt the sparse indexer (#61149)
- **2026-10-13** [`0d2689e0df`](https://github.com/vllm-project/vllm/commit/0d2689e0df) [#51309](https://github.com/vllm-project/vllm/pull/51309) — [ROCm][Perf] Skip redundant sparse index remap on non-indexer layers (#51309)
- **2026-10-13** [`2ce8012fa0`](https://github.com/vllm-project/vllm/commit/2ce8012fa0) [#51314](https://github.com/vllm-project/vllm/pull/51314) — [ROCm][Perf] Skip cleaning sparse prefill MQA logits (#51314)
- **2026-10-13** [`f7ba007b5e`](https://github.com/vllm-project/vllm/commit/f7ba007b5e) [#60322](https://github.com/vllm-project/vllm/pull/60322) — [ROCm][MoE] Split AiterExperts by weight-quantization key (#60322)
- **2026-10-13** [`df6c7ad031`](https://github.com/vllm-project/vllm/commit/df6c7ad031) [#61183](https://github.com/vllm-project/vllm/pull/61183) — [Core][Refactor] Move KV cache planning logic to kv_cache_planning.py (#61183)
- **2026-10-13** [`c077dc663d`](https://github.com/vllm-project/vllm/commit/c077dc663d) [#59039](https://github.com/vllm-project/vllm/pull/59039) — [ROCm][Perf][DSv4.1] Enable decoder SWA bounded replay (#59039)
- **2026-10-13** [`cc2a6eea1a`](https://github.com/vllm-project/vllm/commit/cc2a6eea1a) [#61082](https://github.com/vllm-project/vllm/pull/61082) — [ROCm][Perf][DSv4.1] Mono decode on every backbone layer (#61082)
- **2026-10-13** [`c6566bb9f6`](https://github.com/vllm-project/vllm/commit/c6566bb9f6) [#59070](https://github.com/vllm-project/vllm/pull/59070) — [ROCm][MLA] Keep DCP prefill context in FP8 through AllGather (#59070)
- **2026-10-12** [`802feb6770`](https://github.com/vllm-project/vllm/commit/802feb6770) [#57705](https://github.com/vllm-project/vllm/pull/57705) — [Bugfix][KVConnector] Fix MoRI-IO WRITE-mode requests stranded in WAITING_FOR_REMOTE_KVS (#57705)
- **2026-10-12** [`abad32a718`](https://github.com/vllm-project/vllm/commit/abad32a718) [#58547](https://github.com/vllm-project/vllm/pull/58547) — [ROCm][Perf] Fix Gemma AR+RMS prefill fallback (#58547)
- **2026-10-12** [`8055293353`](https://github.com/vllm-project/vllm/commit/8055293353) [#58381](https://github.com/vllm-project/vllm/pull/58381) — [ROCm][MLA] Cut ~21x host dispatch from the MLA metadata build (#58381)
- **2026-10-12** [`c9e62f13c2`](https://github.com/vllm-project/vllm/commit/c9e62f13c2) [#60883](https://github.com/vllm-project/vllm/pull/60883) — [CI][ROCm] Add AITER nightly overlay scripts (#60883)
- **2026-10-12** [`e1a5086256`](https://github.com/vllm-project/vllm/commit/e1a5086256) [#61126](https://github.com/vllm-project/vllm/pull/61126) — [Attention] Remove cascade attention (#61126)
- **2026-10-12** [`e0317b28ce`](https://github.com/vllm-project/vllm/commit/e0317b28ce) [#52231](https://github.com/vllm-project/vllm/pull/52231) — [Feature] Support batch invariance on ROCm (#52231)
- **2026-10-12** [`50b21a2667`](https://github.com/vllm-project/vllm/commit/50b21a2667) [#49263](https://github.com/vllm-project/vllm/pull/49263) — [Perf] [Feat] [ROCm] Add densemha support to ROCm AITER Sparse MLA (#49263)
- **2026-10-12** [`a686c8e1b7`](https://github.com/vllm-project/vllm/commit/a686c8e1b7) [#60502](https://github.com/vllm-project/vllm/pull/60502) — [Triton] Migrate Triton kernels off tl.make_block_ptr for triton-main compat (#60502)
- **2026-10-12** [`8c175f403a`](https://github.com/vllm-project/vllm/commit/8c175f403a) [#61185](https://github.com/vllm-project/vllm/pull/61185) — [CI][ROCm] Compare greedy output only in the AITER attn+quant test (#61185)
- **2026-10-12** [`e3bbaf2369`](https://github.com/vllm-project/vllm/commit/e3bbaf2369) [#61004](https://github.com/vllm-project/vllm/pull/61004) — [ROCm][DSv4] Fuse the shared expert into AITER MegaMoE (#61004)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#61052](https://github.com/vllm-project/vllm/issues/61052) | [Bug]: CPU KV offload crashes with Xid 31 on NVIDIA vGPU — cuMemcpyBat | bug, nvidia | 2026-10-19 |
| [#60072](https://github.com/vllm-project/vllm/issues/60072) | [Tracking] HiSparse bugfixes and performance improvements | — | 2026-10-19 |
| [#62484](https://github.com/vllm-project/vllm/issues/62484) | [Bug]: CPU build fails with 'Torch not compiled with CUDA enabled' in  | nvidia | 2026-10-19 |
| [#37729](https://github.com/vllm-project/vllm/issues/37729) | [Bug]: V1 engine core deadlocks under concurrent load (fp8 + prefix ca | bug | 2026-10-19 |
| [#62466](https://github.com/vllm-project/vllm/issues/62466) | [Bug]: persistent_topk returns indices past the row length when length | — | 2026-10-19 |
| [#60523](https://github.com/vllm-project/vllm/issues/60523) | [RFC]: Improving MooncakeConnector | RFC, kimi, k3 | 2026-10-19 |
| [#62243](https://github.com/vllm-project/vllm/issues/62243) | [RFC]: Module layout for the Mooncake P2P KV connector | — | 2026-10-19 |
| [#61539](https://github.com/vllm-project/vllm/issues/61539) | [RFC]: Explicit row layouts for routed-expert capture | — | 2026-10-19 |
| [#62153](https://github.com/vllm-project/vllm/issues/62153) | [Bug]: Mamba2 hybrid models crash once the prompt is longer than block | quantization | 2026-10-19 |
| [#62356](https://github.com/vllm-project/vllm/issues/62356) | [Bug]: Qwen3-Omni/ASR audio encoder skips quant_config, host-syncs chu | rocm, quantization | 2026-10-19 |
| [#62420](https://github.com/vllm-project/vllm/issues/62420) | [Bug]: EXIF-oriented images (orientation != 1) return 500 on mistral-t | bug, mistral | 2026-10-19 |
| [#61761](https://github.com/vllm-project/vllm/issues/61761) | [RFC]: DFlash2 speculative decoding performance on ROCm (MI355X) | rocm, speculative-decoding, kimi | 2026-10-19 |
| [#53928](https://github.com/vllm-project/vllm/issues/53928) | [Bug]:  [XPU] RuntimeError: causal_conv1d does not support spec-decode | bug, intel-gpu, quantization | 2026-10-19 |
| [#60581](https://github.com/vllm-project/vllm/issues/60581) | [Usage]: ROCm gfx950: MXFP4 activation quant not fused into GEMM; Quar | rocm, usage | 2026-10-19 |
| [#57103](https://github.com/vllm-project/vllm/issues/57103) | [RFC]: Programmable KV Cache: Composable Policies for Agentic Serving | RFC, kimi | 2026-10-19 |
| [#48576](https://github.com/vllm-project/vllm/issues/48576) | [Perf][ROCm] Optimize DSA lightning-indexer fp8_mqa_logits scoring ker | rocm, stale | 2026-10-19 |
| [#49004](https://github.com/vllm-project/vllm/issues/49004) | [Bug]: DBRX MoE weight loading crashes with KeyError after FusedMoE/Mo | bug, stale | 2026-10-19 |
| [#49090](https://github.com/vllm-project/vllm/issues/49090) | [RFC][SpecDecode] Move MTP completeness validation to the weight-updat | stale | 2026-10-19 |
| [#43224](https://github.com/vllm-project/vllm/issues/43224) | [RFC]: Porting compiler fusions to manual fusion | RFC, unstale | 2026-10-19 |
| [#61406](https://github.com/vllm-project/vllm/issues/61406) | [RFC]: vLLM Simulator: CPU-Based CI and Hardware-Aware Performance Sim | RFC, quantization | 2026-10-19 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 104 |
| MoE / Expert Parallel | 59 |
| Attention | 55 |
| Other | 48 |
| Multimodal | 31 |
| CI / Build | 31 |
| Serving / API | 29 |
| Scheduler / Engine | 27 |
| Quantization | 24 |
| Disaggregation / PD | 22 |
| KV Cache / Offload | 21 |
| Models | 15 |
| Speculative Decoding | 15 |
| Perf / Benchmark | 10 |
| Docs | 9 |
| LoRA | 8 |
| Compilation / CUDA Graph | 4 |

## ROCm / AMD  (104 commits)

- **2026-10-19** [`973dbf8071`](https://github.com/vllm-project/vllm/commit/973dbf8071) [#62273](https://github.com/vllm-project/vllm/pull/62273)
  [Doc][ROCm] Align Kimi-K3 MI355X recipe with InferenceX #4215 (#62273)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-19** [`ffa18e55a4`](https://github.com/vllm-project/vllm/commit/ffa18e55a4) [#61345](https://github.com/vllm-project/vllm/pull/61345)
  [ROCm][DSv4] Require explicit MXFP4 opt-in for MegaMoE shared-expert fusion (#61345)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/distributed/device_communicators/all2all.py`, `vllm/envs.py` _+4 more__
- **2026-10-19** [`3e96f9cf63`](https://github.com/vllm-project/vllm/commit/3e96f9cf63) [#62276](https://github.com/vllm-project/vllm/pull/62276)
  [ROCm][CI] Bump the ROCm 10 image to torch 2.13 (#62276)
  _Files: `docker/Dockerfile.rocm_base`, `vllm/distributed/device_communicators/pynccl.py`, `vllm/v1/attention/backends/mla/triton_mla.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-10-19** [`5bc26717dd`](https://github.com/vllm-project/vllm/commit/5bc26717dd) [#60816](https://github.com/vllm-project/vllm/pull/60816)
  [ROCm][Qwen4Exp] Remove the Qwen3.8-Flash-Next TEP8 MXFP4 emulation guard (#60816)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/kernels/moe/test_rocm_aiter_moe.py`, `tests/quantization/test_gfx950_moe.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py` _+1 more__
- **2026-10-19** [`fb61ac07bd`](https://github.com/vllm-project/vllm/commit/fb61ac07bd) [#61943](https://github.com/vllm-project/vllm/pull/61943)
  [ROCm][Perf] Use AITER top-k for the DeepSeek-V3.2/GLM-5 sparse indexer (#61943)
  _Files: `tests/kernels/test_top_k_per_row.py`, `vllm/_aiter_ops.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-10-19** [`c1dc2e9cf9`](https://github.com/vllm-project/vllm/commit/c1dc2e9cf9) [#53987](https://github.com/vllm-project/vllm/pull/53987)
  [Spec Decode][ROCm] Add FLy: entropy-gated deferred verification for draft-model speculative decoding (#53987)
  _Files: `docs/features/speculative_decoding/README.md`, `docs/features/speculative_decoding/fly.md`, `tests/v1/sample/test_rejection_sampler.py`, `tests/v1/spec_decode/test_rejection_sampler_utils.py` _+8 more__
- **2026-10-19** [`e7023e596d`](https://github.com/vllm-project/vllm/commit/e7023e596d) [#61726](https://github.com/vllm-project/vllm/pull/61726)
  [Bugfix][ROCm][MoRIIO] Support heterogeneous TP in WRITE mode for all attention and mamba layers (#61726)
  _Files: `.buildkite/test_areas/misc.yaml`, `docs/features/moriio_connector_usage.md`, `tests/v1/kv_connector/moriio_integration/test_write_dummy_e2e_rocm.py`, `tests/v1/kv_connector/unit/test_moriio_connector.py` _+9 more__
- **2026-10-19** [`e68efc685a`](https://github.com/vllm-project/vllm/commit/e68efc685a) [#62363](https://github.com/vllm-project/vllm/pull/62363)
  [CI][AMD] Split LM Eval Small by CDNA generation, unify AMD step titles, clone MoRIIO steps into test-amd.yaml (#62363)
  _Files: `.buildkite/hardware_tests/amd.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/entrypoints.yaml` _+12 more__
- **2026-10-19** [`6a0b146c16`](https://github.com/vllm-project/vllm/commit/6a0b146c16) [#62371](https://github.com/vllm-project/vllm/pull/62371)
  [ROCm][Compile] Fuse AITER static FP8 quant into MLA attention output (#62371)
  _Files: `tests/compile/passes/test_mla_attn_quant_fusion.py`, `vllm/compilation/passes/fusion/mla_attn_quant_fusion.py`, `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-10-19** [`e719b41e22`](https://github.com/vllm-project/vllm/commit/e719b41e22) [#62131](https://github.com/vllm-project/vllm/pull/62131)
  [ROCm][Perf][DSv4.1] Mono decode for the DSpark draft layers (#62131)
  _Files: `tests/models/test_dsv41_mono_decode.py`, `vllm/models/deepseek_v41/amd/mono/README.md`, `vllm/models/deepseek_v41/amd/mono/attention/front.py`, `vllm/models/deepseek_v41/amd/mono/layer.py` _+2 more__
- **2026-10-19** [`c07c59f821`](https://github.com/vllm-project/vllm/commit/c07c59f821) [#62241](https://github.com/vllm-project/vllm/pull/62241)
  [ROCm][Bugfix] Release vLLM's communicators on external-launcher shutdown (#62241)
  _Files: `vllm/v1/executor/uniproc_executor.py`_
- **2026-10-19** [`0ee62b99b6`](https://github.com/vllm-project/vllm/commit/0ee62b99b6) [#62286](https://github.com/vllm-project/vllm/pull/62286)
  [ROCm][CI] Contain the MI355 DP + EP exit-time abort (#62286)
  _Files: `.buildkite/test_areas/distributed.yaml`_
- **2026-10-19** [`8e5cae09f1`](https://github.com/vllm-project/vllm/commit/8e5cae09f1) [#62280](https://github.com/vllm-project/vllm/pull/62280)
  [ROCm][CI] Pin Inductor pointwise configs in the MoRIIO dummy-weight P/D test (#62280)
  _Files: `tests/v1/kv_connector/moriio_integration/test_write_dummy_e2e_rocm.py`_
- **2026-10-18** [`82a24bb82d`](https://github.com/vllm-project/vllm/commit/82a24bb82d) [#62274](https://github.com/vllm-project/vllm/pull/62274)
  [Bugfix][ROCm] Only set inductor batch_invariant when torch has it (#62274)
  _Files: `vllm/model_executor/determinism/batch_invariant.py`_
- **2026-10-18** [`e80b6c642f`](https://github.com/vllm-project/vllm/commit/e80b6c642f) [#61819](https://github.com/vllm-project/vllm/pull/61819)
  [ROCm][DSv4] Overlap the unfused shared expert with AITER MegaMoE (#61819)
  _Files: `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/model.py`_
- **2026-10-18** [`494663940b`](https://github.com/vllm-project/vllm/commit/494663940b) [#61454](https://github.com/vllm-project/vllm/pull/61454)
  [Qwen4Exp] Clean up HC and PLE implementations for Qwen3.8-Flash-Next (#61454)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/amd/hyperconnection.py`, `vllm/models/qwen4_exp/amd/ple_layer.py`, `vllm/models/qwen4_exp/common/ngram_embedding.py` _+7 more__
- **2026-10-18** [`da9134bc89`](https://github.com/vllm-project/vllm/commit/da9134bc89) [#62161](https://github.com/vllm-project/vllm/pull/62161)
  [ROCm][CI] Give the MoE parallel-launch watchdog room for AITER JIT builds (#62161)
  _Files: `tests/kernels/moe/modular_kernel_tools/parallel_utils.py`_
- **2026-10-18** [`b2456c622b`](https://github.com/vllm-project/vllm/commit/b2456c622b) [#58761](https://github.com/vllm-project/vllm/pull/58761)
  [ROCm][CI] Make ROCm 10.0 the default image; keep ROCm 7.2 as -rocm72 (#58761)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/annotate-rocm-release.sh`, `.buildkite/scripts/cache-rocm-base-wheels.sh`, `.buildkite/scripts/ci-bake-rocm.sh` _+20 more__
- **2026-10-18** [`03ee2e134d`](https://github.com/vllm-project/vllm/commit/03ee2e134d) [#62213](https://github.com/vllm-project/vllm/pull/62213)
  [CI][ROCm] Fix order-dependent test_rocm_aiter_sampler_defers_import (CPU tensors hit Triton) (#62213)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`_
- **2026-10-17** [`2067297b2f`](https://github.com/vllm-project/vllm/commit/2067297b2f) [#61278](https://github.com/vllm-project/vllm/pull/61278)
  [ROCm][Perf] Use AITER tuned configs to select a4w4 gemm kernel instead of env var (#61278)
  _Files: `tests/kernels/quantization/test_rocm_mxfp4.py`, `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/kernels/linear/mxfp4/aiter.py`_
- **2026-10-17** [`3bf25c5097`](https://github.com/vllm-project/vllm/commit/3bf25c5097) [#62087](https://github.com/vllm-project/vllm/pull/62087)
  [CI][Bugfix] Ignore AMD CI webhook no-op builds in /amd-ci run and retry (#62087)
  _Files: `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-10-17** [`41b8c15809`](https://github.com/vllm-project/vllm/commit/41b8c15809) [#60544](https://github.com/vllm-project/vllm/pull/60544)
  [Feature][MoRIIO] Support hybrid WRITE transfers with DSpark (#60544)
  _Files: `.buildkite/test_areas/misc.yaml`, `docs/features/moriio_connector_usage.md`, `examples/disaggregated/disaggregated_serving/moriio_toy_proxy_server.py`, `tests/v1/kv_connector/moriio_integration/__init__.py` _+10 more__
- **2026-10-17** [`a0e7137c4b`](https://github.com/vllm-project/vllm/commit/a0e7137c4b) [#61960](https://github.com/vllm-project/vllm/pull/61960)
  [CI][ROCm][Bugfix] DeepSeek V4.1: don't pass expert intermediate padding to AITER (#61960)
  _Files: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v41/amd/model.py`_
- **2026-10-17** [`f019e3e105`](https://github.com/vllm-project/vllm/commit/f019e3e105) [#52968](https://github.com/vllm-project/vllm/pull/52968)
  [ROCm] attn res + sigmoid_mul + conv fusions (#52968)
  _Files: `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/mla.py`_
- **2026-10-16** [`28e92eeff2`](https://github.com/vllm-project/vllm/commit/28e92eeff2) [#59552](https://github.com/vllm-project/vllm/pull/59552)
  [ROCm][Perf][Kimi-K3] Use AITER Gluon chunk_kda for KDA prefill (#59552)
  _Files: `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/warmup/kimi_k3_triton_warmup.py` _+2 more__
- **2026-10-16** [`cc2e4fecf2`](https://github.com/vllm-project/vllm/commit/cc2e4fecf2) [#52831](https://github.com/vllm-project/vllm/pull/52831)
  [ROCm] [fusion] support ROCm aiter fusion of per tensor quant + rmsnorm (#52831)
  _Files: `tests/compile/passes/test_fusion.py`, `vllm/_aiter_ops.py`, `vllm/compilation/passes/fusion/matcher_utils.py`, `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`_
- **2026-10-16** [`5bf3d9f665`](https://github.com/vllm-project/vllm/commit/5bf3d9f665) [#59824](https://github.com/vllm-project/vllm/pull/59824)
  [ROCm][Kimi-K3] Support DSpark adaptive verification on MI355X (#59824)
  _Files: `tests/models/kimi_k3/test_amd_kda_adaptive_verification.py`, `tests/v1/attention/test_expand_page_indices.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py` _+2 more__
- **2026-10-16** [`307c5844ad`](https://github.com/vllm-project/vllm/commit/307c5844ad) [#62048](https://github.com/vllm-project/vllm/pull/62048)
  [ROCm][CI] Enable batch invariance for the ngram scheduling accuracy test (#62048)
  _Files: `tests/v1/e2e/general/test_async_scheduling_accuracy.py`_
- **2026-10-16** [`e7a5bdb454`](https://github.com/vllm-project/vllm/commit/e7a5bdb454) [#62053](https://github.com/vllm-project/vllm/pull/62053)
  [ROCm][CI] Move Spec Decode Speculators + MTP to MI355 (#62053)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-10-16** [`706791d516`](https://github.com/vllm-project/vllm/commit/706791d516) [#61955](https://github.com/vllm-project/vllm/pull/61955)
  [CI][AMD] Move 17 test groups from MI300 to MI355 and test large DeepSeek/Nemotron evals on AITER (#61955)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/models_language.yaml` _+9 more__
- **2026-10-16** [`76081b9ee4`](https://github.com/vllm-project/vllm/commit/76081b9ee4) [#61921](https://github.com/vllm-project/vllm/pull/61921)
  [Bugfix][Model] Honor quantization config in Inkling MTP (#61921)
  _Files: `vllm/models/inkling/amd/mtp.py`, `vllm/models/inkling/nvidia/mtp.py`_
- **2026-10-16** [`8e25bbca19`](https://github.com/vllm-project/vllm/commit/8e25bbca19) [#61843](https://github.com/vllm-project/vllm/pull/61843)
  [Refactor] Remove dead code multiple places (#61843)
  _Files: `csrc/activation_kernels.cu`, `csrc/ops.h`, `csrc/torch_bindings.cpp`, `tests/kernels/core/test_activation.py` _+6 more__
- **2026-10-16** [`8a6c0449b3`](https://github.com/vllm-project/vllm/commit/8a6c0449b3) [#58589](https://github.com/vllm-project/vllm/pull/58589)
  [Bugfix][ROCm][GLM-5.2] Stop forcing skip_final_all_reduce on AMD DSA model path (#58589)
  _Files: `vllm/models/deepseek_v32/amd/model.py`_
- **2026-10-16** [`fa75d3456d`](https://github.com/vllm-project/vllm/commit/fa75d3456d) [#59857](https://github.com/vllm-project/vllm/pull/59857)
  [Feature][PCP] Add DeepSeek-V4.1-Flash support (#59857)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_engram.py` _+11 more__
- **2026-10-16** [`074c83a09a`](https://github.com/vllm-project/vllm/commit/074c83a09a) [#61932](https://github.com/vllm-project/vllm/pull/61932)
  [CI][Intel] Skip ROCm-only test_topk_gating_enabled_by_cdna on XPU (#61932)
  _Files: `.buildkite/intel_jobs/model_executor_intel.yaml`_
- **2026-10-16** [`b466fbacd2`](https://github.com/vllm-project/vllm/commit/b466fbacd2) [#61895](https://github.com/vllm-project/vllm/pull/61895)
  [ROCm][Perf] Any-shape low-latency MoE router GEMM on MI355 (#61895)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/test_gate_linear_rocm_dispatch.py`, `tests/kernels/test_rocm_fp32_router_gemm.py` _+2 more__
- **2026-10-16** [`29345f42a6`](https://github.com/vllm-project/vllm/commit/29345f42a6) [#61471](https://github.com/vllm-project/vllm/pull/61471)
  [ROCm][Qwen4Exp] Support HC and MoE sequence parallelism on ROCm (#61471)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_distributed.yaml`, `tests/models/qwen4_exp/test_config.py`, `tests/models/qwen4_exp/test_tpsp.py` _+13 more__
- **2026-10-16** [`ef38e8d006`](https://github.com/vllm-project/vllm/commit/ef38e8d006) [#42755](https://github.com/vllm-project/vllm/pull/42755)
  [Model][Hardware][AMD][Kernel] Part 2/2 -> Enable e2e QK Norm + RoPE + KV Cache runtime fusion for Qwen3-30B-A3B on ROCM_ATTN (#42755)
  _Files: `csrc/cache_kernels.cu`, `csrc/ops.h`, `csrc/rocm/attention.cu`, `csrc/rocm/ops.h` _+19 more__
- **2026-10-15** [`4a89316efa`](https://github.com/vllm-project/vllm/commit/4a89316efa) [#61713](https://github.com/vllm-project/vllm/pull/61713)
  [Core] Drop the Ray driver-node GPU pin left over from the legacy executor (#61713)
  _Files: `.buildkite/test_areas/distributed.yaml`, `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+7 more__
- **2026-10-15** [`3f1e57225a`](https://github.com/vllm-project/vllm/commit/3f1e57225a) [#57392](https://github.com/vllm-project/vllm/pull/57392)
  [ROCm][Perf][Kimi-K3] Use AITER Gluon KDA kernels for decode and spec decode (#57392)
  _Files: `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/_aiter_ops.py`, `vllm/models/kimi_k3/amd/kda.py`_
- **2026-10-15** [`e711723352`](https://github.com/vllm-project/vllm/commit/e711723352) [#58800](https://github.com/vllm-project/vllm/pull/58800)
  [ROCm] gfx1250 optimizations and model enablement (#58800)
  _Files: `docker/Dockerfile.rocm_base_gfx1250`, `docker/Dockerfile.rocm_gfx1250`, `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/_aiter_ops.py` _+17 more__
- **2026-10-15** [`9b99ccb56b`](https://github.com/vllm-project/vllm/commit/9b99ccb56b) [#61861](https://github.com/vllm-project/vllm/pull/61861)
  [CI] Shard the AMD mirrors of the DP, RayExecutorV2 and batch invariance steps automatically (#61861)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/misc.yaml`_
- **2026-10-15** [`0c25849292`](https://github.com/vllm-project/vllm/commit/0c25849292) [#59406](https://github.com/vllm-project/vllm/pull/59406)
  [ROCm][Perf][Bugfix] Probe the preshuffled FP4 GEMM config by logical K (#59406)
  _Files: `tests/kernels/quantization/test_rocm_mxfp4.py`, `vllm/_aiter_ops.py`_
- **2026-10-15** [`c414bf0295`](https://github.com/vllm-project/vllm/commit/c414bf0295) [#61817](https://github.com/vllm-project/vllm/pull/61817)
  [CI] Shard four AMD mirrors automatically (#61817)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/quantization.yaml`, `.buildkite/test_areas/spec_decode.yaml`_
- **2026-10-15** [`16532876e7`](https://github.com/vllm-project/vllm/commit/16532876e7) [#61860](https://github.com/vllm-project/vllm/pull/61860)
  [CI] Shard four more AMD mirrors automatically (#61860)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/pytorch.yaml`_
- **2026-10-15** [`105605b8e9`](https://github.com/vllm-project/vllm/commit/105605b8e9) [#60282](https://github.com/vllm-project/vllm/pull/60282)
  [ROCm] Support DeepSeek-V4 hash routing in AITER Triton W4A16 MoE (#60282)
  _Files: `tests/kernels/moe/test_topk_softplus_sqrt.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a16_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py` _+3 more__
- **2026-10-15** [`47fd76e4ce`](https://github.com/vllm-project/vllm/commit/47fd76e4ce) [#56226](https://github.com/vllm-project/vllm/pull/56226)
  [ROCm][Perf] Route softmax MoE top-k, including fused shared-expert sigmoid, through AITER topk_gating (#56226)
  _Files: `benchmarks/kernels/benchmark_fused_topk.py`, `tests/kernels/moe/test_rocm_aiter_topk.py`, `tests/model_executor/test_enabled_custom_ops.py`, `vllm/_aiter_ops.py` _+2 more__
- **2026-10-15** [`011fa68ca9`](https://github.com/vllm-project/vllm/commit/011fa68ca9) [#55090](https://github.com/vllm-project/vllm/pull/55090)
  [ROCm][Perf] Pad fp16/bf16 GEMM weight row stride for L2 cache (#55090)
  _Files: `tests/model_executor/layers/test_rocm_unquantized_gemm.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/utils.py`_
- **2026-10-15** [`0951fc183c`](https://github.com/vllm-project/vllm/commit/0951fc183c) [#58689](https://github.com/vllm-project/vllm/pull/58689)
  [ROCm][DSv4.1] Disambiguate ROCm attention class names (#58689)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`, `tests/v1/attention/test_rocm_aiter_triton_sparse_mla.py` _+7 more__
- **2026-10-15** [`e8e1e96196`](https://github.com/vllm-project/vllm/commit/e8e1e96196) [#61262](https://github.com/vllm-project/vllm/pull/61262)
  [ROCm][DSv4] AITER MegaMoE Fixed-Slot Dispatch For DeepSeek-V4 (#61262)
  _Files: `tests/models/test_deepseek_v4_aiter_mega_moe.py`, `vllm/models/deepseek_v4/amd/mega_moe.py`, `vllm/utils/math_utils.py`_
- **2026-10-15** [`365aaa77bd`](https://github.com/vllm-project/vllm/commit/365aaa77bd) [#56054](https://github.com/vllm-project/vllm/pull/56054)
  [Bugfix][DSv4] Remap Quark MTP layer_quant_config onto draft prefixes (#56054)
  _Files: `vllm/models/deepseek_v4/amd/mtp.py`, `vllm/models/deepseek_v4/quant_config.py`_
- **2026-10-15** [`b965ee564d`](https://github.com/vllm-project/vllm/commit/b965ee564d) [#61392](https://github.com/vllm-project/vllm/pull/61392)
  [Chore] Use upstream Transformers DeepseekV4Config (#61392)
  _Files: `.agents/skills/transformers-upgrade/SKILL.md`, `tests/config/test_model_arch_config.py`, `tests/distributed/test_eplb_spec_decode.py`, `tests/model_executor/layers/test_fused_shared_expert.py` _+27 more__
- **2026-10-15** [`833665cded`](https://github.com/vllm-project/vllm/commit/833665cded) [#59596](https://github.com/vllm-project/vllm/pull/59596)
  [ROCm][DI] Enable MoRI FP4 dispatch for mxfp4 w4a4 moe  (#59596)
  _Files: `tests/kernels/moe/test_mori_moe.py`, `vllm/model_executor/layers/fused_moe/all2all_utils.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/mori.py`_
- **2026-10-15** [`10d2c6083d`](https://github.com/vllm-project/vllm/commit/10d2c6083d) [#58151](https://github.com/vllm-project/vllm/pull/58151)
  [ROCm][DSv4.1] Enable DSpark adaptive verification (#58151)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`, `vllm/models/deepseek_v41/amd/rocm.py` _+1 more__
- **2026-10-15** [`f46021a7fa`](https://github.com/vllm-project/vllm/commit/f46021a7fa) [#57773](https://github.com/vllm-project/vllm/pull/57773)
  [ROCm][Perf] Enable DPA+ETP prefill compute/comm dual-batch-overlap for DeepSeek-V4 (#57773)
  _Files: `tests/kernels/moe/test_naive_dp_ep_dbo.py`, `tests/v1/worker/test_ubatch_offsets.py`, `vllm/config/vllm.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py` _+5 more__
- **2026-10-15** [`429a3da665`](https://github.com/vllm-project/vllm/commit/429a3da665) [#58585](https://github.com/vllm-project/vllm/pull/58585)
  [Bugfix][ROCm][Disagg] Allow MoRIIO HMA per-layer block_len (#58585)
  _Files: `tests/v1/kv_connector/unit/test_moriio_hma_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`_
- **2026-10-15** [`2abd479aee`](https://github.com/vllm-project/vllm/commit/2abd479aee) [#61720](https://github.com/vllm-project/vllm/pull/61720)
  [ROCm][CI] Add AMD job for DeepSeek-V4.1 Mono Decode Numerics (#61720)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-10-15** [`e57bb4ace7`](https://github.com/vllm-project/vllm/commit/e57bb4ace7) [#61712](https://github.com/vllm-project/vllm/pull/61712)
  [Core] Remove the legacy Ray compiled-graph executor (#61712)
  _Files: `.buildkite/hardware_tests/ascend_npu.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`, `docs/serving/parallelism_scaling.md` _+12 more__
- **2026-10-15** [`8530aed2b7`](https://github.com/vllm-project/vllm/commit/8530aed2b7) [#61701](https://github.com/vllm-project/vllm/pull/61701)
  [Spec Decode] Remove Medusa and MLP speculator support (#61701)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/spec_decode.yaml`, `.github/mergify.yml` _+23 more__
- **2026-10-14** [`273a04964e`](https://github.com/vllm-project/vllm/commit/273a04964e) [#61697](https://github.com/vllm-project/vllm/pull/61697)
  [ROCm] Bump AITER to v0.1.25 and relax the DSv4.1 mono MoE tolerance (#61697)
  _Files: `docker/Dockerfile.rock_base`, `docker/Dockerfile.rocm_base`, `tests/models/test_dsv41_mono_numerics.py`_
- **2026-10-14** [`7840bede98`](https://github.com/vllm-project/vllm/commit/7840bede98) [#59678](https://github.com/vllm-project/vllm/pull/59678)
  [ROCm][CI] Add AMD jobs for test groups that only exist in tes… (#59678)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-10-14** [`9a648b4649`](https://github.com/vllm-project/vllm/commit/9a648b4649) [#61654](https://github.com/vllm-project/vllm/pull/61654)
  [ROCm][Kimi-K3] Don't read W_UK_T before weight loading in the MLA wrapper (#61654)
  _Files: `vllm/models/kimi_k3/amd/mla.py`_
- **2026-10-14** [`2622ee21aa`](https://github.com/vllm-project/vllm/commit/2622ee21aa) [#59290](https://github.com/vllm-project/vllm/pull/59290)
  [ROCm][BugFix] Don't use AITER rms_norm as an IR OP on gfx90a when AITER always on. (#59290)
  _Files: `vllm/platforms/rocm.py`_
- **2026-10-14** [`e96c822660`](https://github.com/vllm-project/vllm/commit/e96c822660) [#60990](https://github.com/vllm-project/vllm/pull/60990)
  [Bugfix][ROCm][MiniMax-M3] Reject unbuilt index-head counts in the AITER indexer (#60990)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/amd/indexer_aiter.py`, `vllm/models/minimax_m3/common/sparse_attention.py`_
- **2026-10-14** [`06265beb25`](https://github.com/vllm-project/vllm/commit/06265beb25) [#60296](https://github.com/vllm-project/vllm/pull/60296)
  [ROCm] Enable fp8 query for Triton attention (#60296)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/platforms/rocm.py`, `vllm/v1/attention/backends/triton_attn.py`_
- **2026-10-14** [`3f729dafcc`](https://github.com/vllm-project/vllm/commit/3f729dafcc) [#60753](https://github.com/vllm-project/vllm/pull/60753)
  [Perf][ROCm][GLM-5.3-Flash] AITER prefill indexer topk (#60753)
  _Files: `benchmarks/kernels/benchmark_sparse_indexer_topk_prefill.py`, `vllm/models/glm5next/amd/sparse_indexer.py`_
- **2026-10-14** [`e534024e49`](https://github.com/vllm-project/vllm/commit/e534024e49) [#60907](https://github.com/vllm-project/vllm/pull/60907)
  [ROCm][Bugfix][MLA] Fix FP8 MLA prefill unpad for interleave-padded heads (#60907)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_fp8_prefill.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-10-14** [`52a8cc5316`](https://github.com/vllm-project/vllm/commit/52a8cc5316) [#61650](https://github.com/vllm-project/vllm/pull/61650)
  [ROCm][CI] Add dtype to the KDA metadata test's fake model config (#61650)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`_
- **2026-10-14** [`355553ac22`](https://github.com/vllm-project/vllm/commit/355553ac22) [#58354](https://github.com/vllm-project/vllm/pull/58354)
  [ROCm][Perf] Drop two dead per-step ops from the AITER sparse MLA metadata build (#58354)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-10-14** [`eaf25f675a`](https://github.com/vllm-project/vllm/commit/eaf25f675a) [#61032](https://github.com/vllm-project/vllm/pull/61032)
  [NIXL] Prepare KV transfer descriptors as NIXL 1.5 strided lists (#61032)
  _Files: `docker/Dockerfile.rock`, `docker/Dockerfile.rocm`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py` _+7 more__
- **2026-10-14** [`81503550f3`](https://github.com/vllm-project/vllm/commit/81503550f3) [#53123](https://github.com/vllm-project/vllm/pull/53123)
  [ROCm] Disable AITER FP8/FP4 BMM for MLA by default (#53123)
  _Files: `tests/kernels/quantization/test_rocm_fp8.py`, `tests/kernels/quantization/test_rocm_mxfp4.py`, `vllm/envs.py`, `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-10-14** [`19aba3e4d5`](https://github.com/vllm-project/vllm/commit/19aba3e4d5) [#57797](https://github.com/vllm-project/vllm/pull/57797)
  [Bugfix][RL] Load attention sinks through weight_loader for layerwise reload (#57797)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `tests/model_executor/test_weight_utils.py`, `tests/models/test_deepseek_v4_dspark_rocm.py`, `tests/models/test_dspark_mla.py` _+26 more__
- **2026-10-14** [`f9b65c30c7`](https://github.com/vllm-project/vllm/commit/f9b65c30c7) [#60645](https://github.com/vllm-project/vllm/pull/60645)
  [ROCm][Perf] Make AITER FlyDSL GDN prefill default on gfx942/gfx950 (#60645)
  _Files: `tests/kernels/mamba/test_gdn_rocm_layout_dispatch.py`, `tests/v1/attention/test_gdn_aiter_flydsl.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-10-14** [`ec8a372566`](https://github.com/vllm-project/vllm/commit/ec8a372566) [#61559](https://github.com/vllm-project/vllm/pull/61559)
  [ROCm][Bugfix] Pin AITER back to v0.1.24.post1 for DSv4.1 mono decode numerics (#61559)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `docker/Dockerfile.rock_base`, `docker/Dockerfile.rocm_base`_
- **2026-10-14** [`30e79c3a76`](https://github.com/vllm-project/vllm/commit/30e79c3a76) [#52183](https://github.com/vllm-project/vllm/pull/52183)
  [Core] Update PyTorch to 2.14.0, torchvision to 0.29.0, triton to 3.8.0 (release channel) (#52183)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/quantization.yaml`, `CMakeLists.txt`, `docker/Dockerfile.s390x` _+12 more__
- **2026-10-14** [`2521446ac8`](https://github.com/vllm-project/vllm/commit/2521446ac8) [#61378](https://github.com/vllm-project/vllm/pull/61378)
  [ROCm][Perf] Enqueue the default chain first in CSA/HCA at small batch sizes for DeepSeek-V4 (#61378)
  _Files: `vllm/models/deepseek_v4/amd/rocm.py`_
- **2026-10-14** [`a1f51a0226`](https://github.com/vllm-project/vllm/commit/a1f51a0226) [#58555](https://github.com/vllm-project/vllm/pull/58555)
  [ROCm][MLA] Route gfx942 DCP causal multi-token verify to Triton split-KV decode (#58555)
  _Files: `tests/v1/attention/test_rocm_aiter_mla_dcp_cprr.py`, `tests/v1/attention/test_rocm_aiter_mla_dcp_cprr_numerics.py`, `tests/v1/attention/test_rocm_aiter_mla_dcp_verify_gfx942.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py` _+1 more__
- **2026-10-14** [`4e0681ed56`](https://github.com/vllm-project/vllm/commit/4e0681ed56) [#56273](https://github.com/vllm-project/vllm/pull/56273)
  [Quantization] Support packed NVFP4 Qwen4Exp PLE embeddings (#56273)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/qwen4_exp/test_ple.py`, `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`, `vllm/models/qwen4_exp/amd/ple_layer.py` _+2 more__
- **2026-10-13** [`f43d7e1a0f`](https://github.com/vllm-project/vllm/commit/f43d7e1a0f) [#60679](https://github.com/vllm-project/vllm/pull/60679)
  [CI][AMD] Gate Aiter MHA FA on dtype (#60679)
  _Files: `vllm/platforms/rocm.py`_
- **2026-10-13** [`7a9d3db896`](https://github.com/vllm-project/vllm/commit/7a9d3db896) [#61230](https://github.com/vllm-project/vllm/pull/61230)
  [ROCm] Bump ROCm base images to AITER v1.25.0 (#61230)
  _Files: `docker/Dockerfile.rock_base`, `docker/Dockerfile.rocm_base`_
- **2026-10-13** [`67516b6c42`](https://github.com/vllm-project/vllm/commit/67516b6c42) [#61207](https://github.com/vllm-project/vllm/pull/61207)
  [Bugfix][ROCm][Kimi-K3] Stage fused KDA decode weights after loading (#61207)
  _Files: `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/ops/kda_decode.py`_
- **2026-10-13** [`93d0bd9d50`](https://github.com/vllm-project/vllm/commit/93d0bd9d50) [#61420](https://github.com/vllm-project/vllm/pull/61420)
  [ROCm][CI] Drop the -inf padding check from the AITER MQA logits test (#61420)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`_
- **2026-10-13** [`c068db0e1d`](https://github.com/vllm-project/vllm/commit/c068db0e1d) [#58918](https://github.com/vllm-project/vllm/pull/58918)
  [Bugfix][Compile] Replace Transformers AOT caching with graph caching (#58918)
  _Files: `tests/compile/test_aot_compile.py`, `tests/compile/test_compiler_interface.py`, `tests/v1/attention/test_rocm_attention_backends_selection.py`, `vllm/compilation/backends.py` _+5 more__
- **2026-10-13** [`e83222396f`](https://github.com/vllm-project/vllm/commit/e83222396f) [#57199](https://github.com/vllm-project/vllm/pull/57199)
  [ROCm][Perf] W4A16: speed up skinny GEMM decode, including speculative batches (#57199)
  _Files: `csrc/rocm/skinny_gemms_int4.cu`, `tests/kernels/quantization/test_rdna_hybrid_w4a16.py`, `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`, `vllm/platforms/rocm.py`_
- **2026-10-13** [`f395a6b1ad`](https://github.com/vllm-project/vllm/commit/f395a6b1ad) [#46754](https://github.com/vllm-project/vllm/pull/46754)
  [ROCM][Bugfix] Deferring to TRITON_ATTN backend for Prefix lm models instead of ROCM_ATTN and fixed minor bug in Gemma3 Multimodal code (#46754)
  _Files: `tests/v1/attention/test_rocm_attention_backends_selection.py`, `vllm/model_executor/models/gemma3_mm.py`_
- **2026-10-13** [`24aa1191f4`](https://github.com/vllm-project/vllm/commit/24aa1191f4) [#61350](https://github.com/vllm-project/vllm/pull/61350)
  [ROCm][Bugfix] Run the AITER AR+RMSNorm fallback test on the platform… (#61350)
  _Files: `tests/distributed/test_aiter_rms_fallback.py`_
- **2026-10-13** [`2cc2e68d1c`](https://github.com/vllm-project/vllm/commit/2cc2e68d1c) [#60043](https://github.com/vllm-project/vllm/pull/60043)
  [Core][Mamba] Remove leftovers of mamba_cache_mode="all" (#60043)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/disaggregated.yaml`, `docs/design/hybrid_kv_cache_manager.md`, `docs/features/automatic_prefix_caching.md` _+29 more__
- **2026-10-13** [`a6009ea85b`](https://github.com/vllm-project/vllm/commit/a6009ea85b) [#61149](https://github.com/vllm-project/vllm/pull/61149)
  [Kernel][Build] Bump DeepGEMM to the 26/09/30 release and adapt the sparse indexer (#61149)
  _Files: `cmake/external_projects/deepgemm.cmake`, `csrc/cache_kernels.cu`, `tests/kernels/attention/test_deepgemm_attention.py`, `tests/kernels/attention/test_rocm_paged_mxfp4_indexer.py` _+19 more__
- **2026-10-13** [`0d2689e0df`](https://github.com/vllm-project/vllm/commit/0d2689e0df) [#51309](https://github.com/vllm-project/vllm/pull/51309)
  [ROCm][Perf] Skip redundant sparse index remap on non-indexer layers (#51309)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_sink.py`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_index_remap.py`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `tests/v1/attention/test_rocm_aiter_triton_sparse_mla.py` _+1 more__
- **2026-10-13** [`2ce8012fa0`](https://github.com/vllm-project/vllm/commit/2ce8012fa0) [#51314](https://github.com/vllm-project/vllm/pull/51314)
  [ROCm][Perf] Skip cleaning sparse prefill MQA logits (#51314)
  _Files: `tests/v1/attention/test_rocm_aiter_mla_sparse.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-10-13** [`f7ba007b5e`](https://github.com/vllm-project/vllm/commit/f7ba007b5e) [#60322](https://github.com/vllm-project/vllm/pull/60322)
  [ROCm][MoE] Split AiterExperts by weight-quantization key (#60322)
  _Files: `.buildkite/test-amd.yaml`, `docs/design/moe_kernel_features.md`, `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/modular_kernel_tools/mk_objects.py` _+9 more__
- **2026-10-13** [`df6c7ad031`](https://github.com/vllm-project/vllm/commit/df6c7ad031) [#61183](https://github.com/vllm-project/vllm/pull/61183)
  [Core][Refactor] Move KV cache planning logic to kv_cache_planning.py (#61183)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `tests/models/test_dspark_mla.py`, `tests/models/test_initialization.py` _+17 more__
- **2026-10-13** [`c077dc663d`](https://github.com/vllm-project/vllm/commit/c077dc663d) [#59039](https://github.com/vllm-project/vllm/pull/59039)
  [ROCm][Perf][DSv4.1] Enable decoder SWA bounded replay (#59039)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_deepseek_v41_amd_replay_forward.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/amd/model.py` _+3 more__
- **2026-10-13** [`cc2a6eea1a`](https://github.com/vllm-project/vllm/commit/cc2a6eea1a) [#61082](https://github.com/vllm-project/vllm/pull/61082)
  [ROCm][Perf][DSv4.1] Mono decode on every backbone layer (#61082)
  _Files: `tests/models/test_dsv41_mono_decode.py`, `tests/models/test_dsv41_mono_layers.py`, `vllm/config/kernel.py`, `vllm/engine/arg_utils.py` _+9 more__
- **2026-10-13** [`c6566bb9f6`](https://github.com/vllm-project/vllm/commit/c6566bb9f6) [#59070](https://github.com/vllm-project/vllm/pull/59070)
  [ROCm][MLA] Keep DCP prefill context in FP8 through AllGather (#59070)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`, `tests/kernels/attention/test_rocm_aiter_mla_op_registration.py`, `tests/v1/attention/test_rocm_aiter_mla_dcp_cprr.py` _+5 more__
- **2026-10-12** [`abad32a718`](https://github.com/vllm-project/vllm/commit/abad32a718) [#58547](https://github.com/vllm-project/vllm/pull/58547)
  [ROCm][Perf] Fix Gemma AR+RMS prefill fallback (#58547)
  _Files: `.buildkite/test_areas/distributed.yaml`, `tests/compile/passes/distributed/test_fusion_all_reduce.py`, `tests/distributed/test_aiter_rms_fallback.py`, `vllm/_aiter_ops.py` _+2 more__
- **2026-10-12** [`8055293353`](https://github.com/vllm-project/vllm/commit/8055293353) [#58381](https://github.com/vllm-project/vllm/pull/58381)
  [ROCm][MLA] Cut ~21x host dispatch from the MLA metadata build (#58381)
  _Files: `tests/v1/attention/test_aiter_mla_uniform_mtp_qo_len.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-10-12** [`c9e62f13c2`](https://github.com/vllm-project/vllm/commit/c9e62f13c2) [#60883](https://github.com/vllm-project/vllm/pull/60883)
  [CI][ROCm] Add AITER nightly overlay scripts (#60883)
  _Files: `.buildkite/scripts/rocm/aiter-nightly-overlay.sh`, `.buildkite/scripts/rocm/select_aiter_nightly_wheel.py`_
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

## MoE / Expert Parallel  (59 commits)

- **2026-10-19** [`dde9aca41c`](https://github.com/vllm-project/vllm/commit/dde9aca41c) [#61727](https://github.com/vllm-project/vllm/pull/61727)
  Add Step-5 Preview support (#61727)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `csrc/moe/topk_softmax_kernels.cu`, `docs/models/supported_models.md`, `rust/Cargo.lock` _+76 more__
- **2026-10-19** [`d46cb9a6d4`](https://github.com/vllm-project/vllm/commit/d46cb9a6d4) [#60179](https://github.com/vllm-project/vllm/pull/60179)
  [Bugfix][Weight Cache] Key non-MoE DP daemons as DP=1 like the engine (#60179)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`_
- **2026-10-19** [`852989f580`](https://github.com/vllm-project/vllm/commit/852989f580) [#58231](https://github.com/vllm-project/vllm/pull/58231)
  [Bugfix][Sampler] Fix split top-p masking every token for huge logits (thinking_token_budget + spec decode emits token 0) (#58231)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_triton.py`_
- **2026-10-19** [`b9c48c98de`](https://github.com/vllm-project/vllm/commit/b9c48c98de) [#55490](https://github.com/vllm-project/vllm/pull/55490)
  [Fast Start] support ep (#55490)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/model_executor.yaml`, `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/layers/fused_moe/expert_map_manager.py` _+3 more__
- **2026-10-19** [`dec6ddadc0`](https://github.com/vllm-project/vllm/commit/dec6ddadc0) [#60740](https://github.com/vllm-project/vllm/pull/60740)
  [CPU] Optimize routed INT8 W8A8 MoE GEMM dispatch (#60740)
  _Files: `csrc/cpu/sgl-kernels/gemm.h`, `csrc/cpu/sgl-kernels/moe_int8.cpp`, `tests/kernels/moe/test_cpu_quant_fused_moe.py`_
- **2026-10-19** [`2b50973f43`](https://github.com/vllm-project/vllm/commit/2b50973f43) [#50396](https://github.com/vllm-project/vllm/pull/50396)
  [Quantization][Autoround][ARK] Add ARK W4A16(moe) Support (#50396)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_moe.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_scheme.py`_
- **2026-10-19** [`b0d61e5d26`](https://github.com/vllm-project/vllm/commit/b0d61e5d26) [#62074](https://github.com/vllm-project/vllm/pull/62074)
  [Model] Add Reflection Beam (#62074)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/models/test_beam_construction.py` _+25 more__
- **2026-10-18** [`36e0ae2df2`](https://github.com/vllm-project/vllm/commit/36e0ae2df2) [#60735](https://github.com/vllm-project/vllm/pull/60735)
  [Bugfix][MoE] Keep DeepEP high-throughput buffers alive across DBO streams (#60735)
  _Files: `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ht.py`_
- **2026-10-18** [`371745ebd6`](https://github.com/vllm-project/vllm/commit/371745ebd6) [#62302](https://github.com/vllm-project/vllm/pull/62302)
  [Doc][RL] Document routed experts return for MoE routing replay (R3) (#62302)
  _Files: `docs/training/rlhf.md`, `docs/training/routed_experts.md`, `mkdocs.yaml`_
- **2026-10-17** [`837e87e1c5`](https://github.com/vllm-project/vllm/commit/837e87e1c5) [#61979](https://github.com/vllm-project/vllm/pull/61979)
  [Feature][LoRA][MoE] Expert LoRA for FlashInfer TRTLLM MXFP4 experts (#61979)
  _Files: `tests/lora/test_trtllm_mxfp4_lora_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_lora_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py` _+1 more__
- **2026-10-17** [`39983a5e7a`](https://github.com/vllm-project/vllm/commit/39983a5e7a) [#62126](https://github.com/vllm-project/vllm/pull/62126)
  [Kernel] Add FP32 router GEMM support for Step-5 Preview and Muse Spark Open (#62126)
  _Files: `csrc/fp32_router_gemm.cu`, `csrc/fp32_router_gemm_entry.cu`, `tests/kernels/test_fp32_router_gemm.py`, `vllm/model_executor/layers/fused_moe/router/gate_linear.py`_
- **2026-10-17** [`7b6310c109`](https://github.com/vllm-project/vllm/commit/7b6310c109) [#61996](https://github.com/vllm-project/vllm/pull/61996)
  [Perf][Sampler] Speed up the small-batch split top-p pipeline (#61996)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`, `tests/v1/worker/test_gpu_sampler_flags.py`, `tests/watermarking/test_watermarking.py`, `vllm/model_executor/models/diffusion_gemma.py` _+5 more__
- **2026-10-17** [`ce49c47cbb`](https://github.com/vllm-project/vllm/commit/ce49c47cbb) [#62046](https://github.com/vllm-project/vllm/pull/62046)
  [Bugfix][Sampler] Carry the boundary tie count across blocks in the split top-p mask kernel (#62046)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_triton.py`_
- **2026-10-16** [`596e530675`](https://github.com/vllm-project/vllm/commit/596e530675) [#62042](https://github.com/vllm-project/vllm/pull/62042)
  [Kernel] Add router GEMM kernels for (5120, 256) and BF16 output to ll_bf16_gemm (#62042)
  _Files: `csrc/fp32_router_gemm.cu`, `csrc/fp32_router_gemm_entry.cu`, `tests/kernels/moe/test_routing.py`, `tests/kernels/test_fp32_router_gemm.py` _+8 more__
- **2026-10-16** [`68ebea789a`](https://github.com/vllm-project/vllm/commit/68ebea789a) [#59044](https://github.com/vllm-project/vllm/pull/59044)
  [Perf][MoE] Skip padded work in SM100 FP4 DeepGEMM experts (#59044)
  _Files: `tests/kernels/moe/test_silu_mul_per_token_group_quant_fp8_colmajor.py`, `vllm/model_executor/layers/fused_moe/experts/deep_gemm_moe.py`_
- **2026-10-16** [`cffc0cfa31`](https://github.com/vllm-project/vllm/commit/cffc0cfa31) [#61695](https://github.com/vllm-project/vllm/pull/61695)
  [CI] Fix B200 FusedMoE Layer Kernels hang on NVSHMEM IB setup (#61695)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/moe/modular_kernel_tools/parallel_utils.py`, `tests/kernels/moe/test_moe_layer.py`_
- **2026-10-16** [`642c18d64c`](https://github.com/vllm-project/vllm/commit/642c18d64c) [#61867](https://github.com/vllm-project/vllm/pull/61867)
  [Perf] Kimi K3 Specialized Decode: CuTeDSL Optimized GB300 (1.5-2x) (#61867)
  _Files: `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/model_state.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/__init__.py`, `vllm/models/kimi_k3/nvidia/specialized_decode/cutedsl/__init__.py` _+46 more__
- **2026-10-16** [`a956a8126e`](https://github.com/vllm-project/vllm/commit/a956a8126e) [#61930](https://github.com/vllm-project/vllm/pull/61930)
  [Bugfix][MoE] Keep the gate's hash_indices_table out of RoutedExperts parameters (#61930)
  _Files: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-10-16** [`a8be1500ba`](https://github.com/vllm-project/vllm/commit/a8be1500ba) [#61388](https://github.com/vllm-project/vllm/pull/61388)
  [Bugfix][MoE] Restore TP-sharded routed-expert capture for DP=1 (#61388)
  _Files: `tests/model_executor/test_routed_experts_capture.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/forward_context.py`, `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`_
- **2026-10-15** [`9edcc7fa7e`](https://github.com/vllm-project/vllm/commit/9edcc7fa7e) [#61161](https://github.com/vllm-project/vllm/pull/61161)
  [Bugfix][Spec Decode] Avoid reusing random draws across block verification rounds (#61161)
  _Files: `tests/v1/spec_decode/test_dspark_topk.py`, `tests/v1/spec_decode/test_lilicorr.py`, `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `tests/watermarking/test_gumbel.py` _+4 more__
- **2026-10-15** [`82b9ccaa79`](https://github.com/vllm-project/vllm/commit/82b9ccaa79) [#61773](https://github.com/vllm-project/vllm/pull/61773)
  [Perf][MoE] Skip the TRTLLM fp8-block activation-scale transpose copy (#61773)
  _Files: `tests/kernels/moe/test_flashinfer.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/no_dp_ep.py` _+1 more__
- **2026-10-15** [`4d58fa254a`](https://github.com/vllm-project/vllm/commit/4d58fa254a) [#61538](https://github.com/vllm-project/vllm/pull/61538)
  [MoE] Unify DeepGEMM MegaMoE experts behind one feature-matrix layer; add NVFP4 (#61538)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/moe/test_deep_gemm_mega_moe.py`, `tests/model_executor/test_deep_gemm_warmup.py`, `tests/models/test_deepseek_v4_mega_moe.py` _+6 more__
- **2026-10-15** [`4f49b55c1f`](https://github.com/vllm-project/vllm/commit/4f49b55c1f) [#61293](https://github.com/vllm-project/vllm/pull/61293)
  [MoE] Shape-based padding for FlashInfer TRT-LLM MXFP8 experts (gated and non-gated) (#61293)
  _Files: `tests/kernels/moe/test_flashinfer.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`_
- **2026-10-15** [`d12d5460a5`](https://github.com/vllm-project/vllm/commit/d12d5460a5) [#61643](https://github.com/vllm-project/vllm/pull/61643)
  [Bugfix][MoE] Keep routing rows during DeepSeek V4.1 decoder replay (#61643)
  _Files: `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`_
- **2026-10-15** [`8fa5ae844a`](https://github.com/vllm-project/vllm/commit/8fa5ae844a) [#61328](https://github.com/vllm-project/vllm/pull/61328)
  [Frontend] Let an unset `--tool-strict-level` fall back to the tool parser's default (#61328)
  _Files: `docs/features/tool_calling.md`, `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/chat/src/lib.rs` _+22 more__
- **2026-10-15** [`85c94c1706`](https://github.com/vllm-project/vllm/commit/85c94c1706) [#61723](https://github.com/vllm-project/vllm/pull/61723)
  [Tests][XPU] Skip modelopt_fp4 online MoE re-quantization test on XPU (#61723)
  _Files: `tests/quantization/test_online.py`_
- **2026-10-15** [`bfdbfa1632`](https://github.com/vllm-project/vllm/commit/bfdbfa1632) [#60946](https://github.com/vllm-project/vllm/pull/60946)
  [Bugfix][PCP] Align MoE routing padding with gathered tokens (#60946)
  _Files: `tests/v1/cudagraph/test_cudagraph_manager.py`, `tests/v1/worker/test_gpu_pcp_manager.py`, `tests/v1/worker/test_gpu_target_dependent_ar_speculator.py`, `vllm/v1/worker/gpu/cudagraph_utils.py` _+3 more__
- **2026-10-14** [`984c242ede`](https://github.com/vllm-project/vllm/commit/984c242ede) [#59815](https://github.com/vllm-project/vllm/pull/59815)
  [Quantization] Support compressed-tensors MXFP4 MoE with FP8 activations via Mxfp4MoEMethod (#59815)
  _Files: `tests/quantization/test_compressed_tensors.py`, `vllm/model_executor/kernels/linear/mxfp4/humming.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py` _+8 more__
- **2026-10-14** [`fe98d90a9d`](https://github.com/vllm-project/vllm/commit/fe98d90a9d) [#61556](https://github.com/vllm-project/vllm/pull/61556)
  [Dependency] Update Humming and remove NVFP4 scale workaround (#61556)
  _Files: `requirements/cuda.txt`, `vllm/model_executor/kernels/linear/mixed_precision/humming.py`, `vllm/model_executor/kernels/linear/mxfp4/humming.py`, `vllm/model_executor/kernels/linear/mxfp6/humming.py` _+9 more__
- **2026-10-14** [`ae94e9c9e8`](https://github.com/vllm-project/vllm/commit/ae94e9c9e8) [#61657](https://github.com/vllm-project/vllm/pull/61657)
  [Bugfix] Don't crash DeepGEMM MegaMoE warmup when get_bf16_mega_gate_config is missing (#61657)
  _Files: `vllm/model_executor/warmup/deep_gemm_warmup.py`_
- **2026-10-14** [`0b6d07cbe2`](https://github.com/vllm-project/vllm/commit/0b6d07cbe2) [#56595](https://github.com/vllm-project/vllm/pull/56595)
  [CI/Build] Use FileStore for DeepEP test rendezvous (#56595)
  _Files: `tests/kernels/moe/parallel_utils.py`_
- **2026-10-14** [`3895a8babe`](https://github.com/vllm-project/vllm/commit/3895a8babe) [#61642](https://github.com/vllm-project/vllm/pull/61642)
  [Bugfix] Fix TP loading of small block-FP8 MLA gates in BailingMoeV3 (#61642)
  _Files: `vllm/model_executor/models/bailing_moe_v3.py`_
- **2026-10-14** [`9e2b579aab`](https://github.com/vllm-project/vllm/commit/9e2b579aab) [#61110](https://github.com/vllm-project/vllm/pull/61110)
  [Model] Support EAGLE3/DFlash aux hidden states for GraniteMoe and GraniteMoeShared (#61110)
  _Files: `vllm/model_executor/models/granitemoe.py`, `vllm/model_executor/models/granitemoeshared.py`_
- **2026-10-14** [`2d09fdcdc2`](https://github.com/vllm-project/vllm/commit/2d09fdcdc2) [#61274](https://github.com/vllm-project/vllm/pull/61274)
  [Quantization] Auto-disable DeepGEMM for Kolibri 1 on SM12x (#61274)
  _Files: `vllm/config/vllm.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/utils/deep_gemm.py`_
- **2026-10-14** [`c9bfa574ce`](https://github.com/vllm-project/vllm/commit/c9bfa574ce) [#60276](https://github.com/vllm-project/vllm/pull/60276)
  [Online quantization] Extend re-quantization API to MOE (showcase `NVFP4 modelopt/CT/quark` to any online MOE method) (#60276)
  _Files: `docs/features/quantization/online.md`, `tests/quantization/test_online.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`, `vllm/model_executor/layers/linear.py` _+12 more__
- **2026-10-14** [`2308b6f00b`](https://github.com/vllm-project/vllm/commit/2308b6f00b) [#58897](https://github.com/vllm-project/vllm/pull/58897)
  [Perf][MoE] Cheaper triton_kernels 3.8 routing build in the OAI Triton MoE (#58897)
  _Files: `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`_
- **2026-10-13** [`ad8d39cbab`](https://github.com/vllm-project/vllm/commit/ad8d39cbab) [#59166](https://github.com/vllm-project/vllm/pull/59166)
  [Bugfix] Fix DSpark graph-padding handling in the DeepSeek-V4.1 MoE fused top-k (#59166)
  _Files: `tests/kernels/moe/test_topk_softplus_sqrt.py`, `tests/v1/spec_decode/test_dflash_prepare_inputs.py`, `vllm/model_executor/layers/fused_moe/router/dsv4_topk.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py` _+1 more__
- **2026-10-13** [`698e79f3bd`](https://github.com/vllm-project/vllm/commit/698e79f3bd) [#60827](https://github.com/vllm-project/vllm/pull/60827)
  [Model] Kolibri 1 via the Transformers modeling backend (#60827)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/models/transformers/fusers/test_moe.py`, `vllm/model_executor/models/registry.py` _+2 more__
- **2026-10-13** [`e90158d912`](https://github.com/vllm-project/vllm/commit/e90158d912) [#60733](https://github.com/vllm-project/vllm/pull/60733)
  [Bugfix][MoE] Clamp BLOCK_SIZE_K to the FP8 quantization block in the batched Triton MoE (#60733)
  _Files: `tests/kernels/moe/test_batched_moe.py`, `vllm/model_executor/layers/fused_moe/experts/fused_batched_moe.py`_
- **2026-10-13** [`68fc395554`](https://github.com/vllm-project/vllm/commit/68fc395554) [#59985](https://github.com/vllm-project/vllm/pull/59985)
  [Bugfix] Keep GateLinear batch invariant under VLLM_BATCH_INVARIANT (#59985)
  _Files: `vllm/model_executor/layers/fused_moe/router/gate_linear.py`_
- **2026-10-13** [`c5bda658d2`](https://github.com/vllm-project/vllm/commit/c5bda658d2) [#60096](https://github.com/vllm-project/vllm/pull/60096)
  [Model][MoE] Load MegaMoE experts directly into the DeepGEMM layout (#60096)
  _Files: `tests/models/kimi_k3/test_weight_loading.py`, `tests/models/test_deepseek_v4_mega_moe.py`, `tests/models/test_dspark_mla.py`, `vllm/model_executor/layers/fused_moe/deep_gemm_mega_moe.py` _+7 more__
- **2026-10-13** [`7fad7db330`](https://github.com/vllm-project/vllm/commit/7fad7db330) [#44343](https://github.com/vllm-project/vllm/pull/44343)
  [Perf][Feat] Add generic cuteDSL LL FP32 router (GEMM) (#44343)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/test_ll_fp32w_gemm.py`, `vllm/model_executor/kernels/linear/cute_dsl/_ll_fp32w_dotprod.py`, `vllm/model_executor/kernels/linear/cute_dsl/_ll_router_common.py` _+3 more__
- **2026-10-13** [`6849ca696a`](https://github.com/vllm-project/vllm/commit/6849ca696a) [#59604](https://github.com/vllm-project/vllm/pull/59604)
  [Quantization] Add ModelOpt IQ2_XS, IQ2_XXS, and Q8_0 support via b12x (#59604)
  _Files: `.buildkite/test_areas/kernels.yaml`, `docs/features/quantization/b12x.md`, `setup.py`, `tests/kernels/moe/test_b12x.py` _+11 more__
- **2026-10-13** [`b9b401b2ef`](https://github.com/vllm-project/vllm/commit/b9b401b2ef) [#53911](https://github.com/vllm-project/vllm/pull/53911)
  [Kernel] Fuse DeepEP-v2 decode globalize+align into one launch (#53911)
  _Files: `CMakeLists.txt`, `csrc/moe/fused_globalize_align_block_size.cu`, `csrc/moe/moe_ops.h`, `csrc/moe/torch_bindings.cpp` _+6 more__
- **2026-10-13** [`253e02b95e`](https://github.com/vllm-project/vllm/commit/253e02b95e) [#60468](https://github.com/vllm-project/vllm/pull/60468)
  [Perf] Warm up DeepGEMM MegaMoE kernels before serving (#60468)
  _Files: `tests/model_executor/test_deep_gemm_warmup.py`, `vllm/model_executor/warmup/deep_gemm_warmup.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-10-13** [`183625d4f9`](https://github.com/vllm-project/vllm/commit/183625d4f9) [#60219](https://github.com/vllm-project/vllm/pull/60219)
  [Bugfix] Fall back to auto for unquantized MoE layers when --moe-backend is marlin (#60219)
  _Files: `tests/kernels/moe/test_unquantized_backend_selection.py`, `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`_
- **2026-10-13** [`6f11c220b5`](https://github.com/vllm-project/vllm/commit/6f11c220b5) [#57410](https://github.com/vllm-project/vllm/pull/57410)
  [Transformers backend] Fuse MoE routers that score after the top-k (#57410)
  _Files: `tests/models/transformers/fusers/test_moe.py`, `vllm/model_executor/models/transformers/fusers/moe.py`, `vllm/model_executor/models/transformers/fx_utils.py`, `vllm/model_executor/models/transformers/moe.py` _+2 more__
- **2026-10-13** [`e2ad0ce5f5`](https://github.com/vllm-project/vllm/commit/e2ad0ce5f5) [#61235](https://github.com/vllm-project/vllm/pull/61235)
  [Bugfix][LoRA] Slice expert LoRA by the unpadded per-rank size under TP (#61235)
  _Files: `vllm/lora/layers/fused_moe.py`_
- **2026-10-12** [`189bbfb9f4`](https://github.com/vllm-project/vllm/commit/189bbfb9f4) [#50415](https://github.com/vllm-project/vllm/pull/50415)
  Add MoNe experts pruning support (#50415)
  _Files: `docs/design/expert_substitution.md`, `pyproject.toml`, `tests/kernels/moe/test_expert_substitution.py`, `tests/kernels/moe/test_unquantized_backend_selection.py` _+9 more__
- **2026-10-12** [`1484266938`](https://github.com/vllm-project/vllm/commit/1484266938) [#61213](https://github.com/vllm-project/vllm/pull/61213)
  [Perf] Improve `_topk_topp_kernel()` for masked logits (#61213)
  _Files: `benchmarks/benchmark_topk_topp.py`, `vllm/v1/sample/ops/topk_topp_triton.py`_
- **2026-10-12** [`44f0ddfd7b`](https://github.com/vllm-project/vllm/commit/44f0ddfd7b) [#61253](https://github.com/vllm-project/vllm/pull/61253)
  [Bugfix][Parser] Stop re-parsing the whole GLM tool argument per chunk (#61253)
  _Files: `tests/parser/engine/test_glm47_moe.py`, `tests/parser/engine/test_parser_engine.py`, `vllm/parser/engine/parser_engine.py`, `vllm/parser/engine/parser_engine_config.py` _+1 more__
- **2026-10-12** [`deedc7be00`](https://github.com/vllm-project/vllm/commit/deedc7be00) [#59340](https://github.com/vllm-project/vllm/pull/59340)
  [Perf][Humming] Skip the redundant MoE input copy before the w13 GEMM (#59340)
  _Files: `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`_
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

## Attention  (55 commits)

- **2026-10-19** [`b048630a19`](https://github.com/vllm-project/vllm/commit/b048630a19) [#60805](https://github.com/vllm-project/vllm/pull/60805)
  [Bugfix] Size the HiSparse hot buffer from the rounded sparse top-k width (#60805)
  _Files: `tests/models/test_dspark_mla.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_sparse_mla_kv_cache_layout.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+4 more__
- **2026-10-19** [`018f5ff71a`](https://github.com/vllm-project/vllm/commit/018f5ff71a) [#60118](https://github.com/vllm-project/vllm/pull/60118)
  [Perf][DSv4.1] MegaAttn: wo_a writes wo_b's MXFP8 input (#60118)
  _Files: `cmake/external_projects/deepgemm.cmake`, `tests/kernels/test_dsv41_mega_attn_layouts.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`_
- **2026-10-19** [`fc47cc8fff`](https://github.com/vllm-project/vllm/commit/fc47cc8fff) [#62183](https://github.com/vllm-project/vllm/pull/62183)
  [Feature][PCP] Support APC and encoder-side SWA bounded replay for DeepSeek-V4.1-Flash (#62183)
  _Files: `tests/models/test_deepseek_v41_replay_batch.py`, `tests/models/test_deepseek_v41_replay_start.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/model.py` _+1 more__
- **2026-10-19** [`93de77c5ed`](https://github.com/vllm-project/vllm/commit/93de77c5ed) [#61329](https://github.com/vllm-project/vllm/pull/61329)
  [CPU] Fix underflow in FP8 AMX attention (#61329)
  _Files: `csrc/cpu/cpu_attn_amx.hpp`, `csrc/cpu/cpu_attn_fp8.hpp`, `csrc/cpu/cpu_types_x86.hpp`, `tests/kernels/attention/test_cpu_attn.py`_
- **2026-10-19** [`38168d5b82`](https://github.com/vllm-project/vllm/commit/38168d5b82) [#56835](https://github.com/vllm-project/vllm/pull/56835)
  [XPU] [Feature] Adding triton/sycl GDN toggle (#56835)
  _Files: `vllm/engine/arg_utils.py`, `vllm/model_executor/layers/mamba/gdn/olmo_gdn_linear_attn.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`, `vllm/v1/attention/backends/gdn_attn.py`_
- **2026-10-19** [`66b431888d`](https://github.com/vllm-project/vllm/commit/66b431888d) [#62377](https://github.com/vllm-project/vllm/pull/62377)
  [PCP] Allow decode-only full CUDA graphs for DSv3.2/GLM-5.2/5.3 sparse MLA with DCP=1 (#62377)
  _Files: `vllm/v1/worker/gpu/pcp_manager.py`_
- **2026-10-19** [`689effee6d`](https://github.com/vllm-project/vllm/commit/689effee6d) [#61938](https://github.com/vllm-project/vllm/pull/61938)
  [Bugfix][Attention] Fix Triton MLA decode int32 overflow and logits workspace accounting (#61938)
  _Files: `tests/kernels/attention/test_triton_decode_attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/mla/triton_mla.py` _+1 more__
- **2026-10-19** [`8f17dbf707`](https://github.com/vllm-project/vllm/commit/8f17dbf707) [#61002](https://github.com/vllm-project/vllm/pull/61002)
  [Bugfix][KV Connector] Pair non-divisible hybrid MLA block sizes in NixlConnector (#61002)
  _Files: `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-17** [`c61a1e73c6`](https://github.com/vllm-project/vllm/commit/c61a1e73c6) [#57320](https://github.com/vllm-project/vllm/pull/57320)
  [Feature] Skip MLA weight absorption when weights are pre-processed (#57320)
  _Files: `vllm/models/kimi_k3/nvidia/mla.py`_
- **2026-10-17** [`21e09ea959`](https://github.com/vllm-project/vllm/commit/21e09ea959) [#62179](https://github.com/vllm-project/vllm/pull/62179)
  [Doc] Sync DeepSeek-V4.1-Flash recipe with vllm-project/recipes#1136, #1137 (#62179)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-10-17** [`2b85d9cb65`](https://github.com/vllm-project/vllm/commit/2b85d9cb65) [#61989](https://github.com/vllm-project/vllm/pull/61989)
  [Perf][Bugfix] Prefer MNNVL for single-node FlashInfer allreduce again (#61989)
  _Files: `tests/distributed/test_comm_ops.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-10-17** [`90d6d871d6`](https://github.com/vllm-project/vllm/commit/90d6d871d6) [#62069](https://github.com/vllm-project/vllm/pull/62069)
  [Attention] Add CuTe DSL backend selection for MLA context prefill (#62069)
  _Files: `tests/v1/attention/test_mla_backends.py`, `vllm/config/attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backends/mla/prefill/trtllm_ragged.py`_
- **2026-10-17** [`71c20f73f2`](https://github.com/vllm-project/vllm/commit/71c20f73f2) [#55671](https://github.com/vllm-project/vllm/pull/55671)
  [FlashInfer] Migrate autotune warmup to flashinfer.autotune_v2 managed cache (#55671)
  _Files: `docs/usage/security.md`, `tests/model_executor/test_flashinfer_autotune_warmup.py`, `vllm/model_executor/warmup/flashinfer_autotune_cache.py`, `vllm/model_executor/warmup/flashinfer_sparse_mla_warmup.py` _+2 more__
- **2026-10-17** [`be25977532`](https://github.com/vllm-project/vllm/commit/be25977532) [#62067](https://github.com/vllm-project/vllm/pull/62067)
  [CI][Tests] Account for FP8 KV-cache rounding in MLA reference (#62067)
  _Files: `tests/v1/attention/test_mla_backends.py`_
- **2026-10-16** [`3dc6def360`](https://github.com/vllm-project/vllm/commit/3dc6def360) [#53036](https://github.com/vllm-project/vllm/pull/53036)
  [Attention][Spec Decode] Enable varlen Mamba2 decode for adaptive verification (#53036)
  _Files: `tests/kernels/mamba/test_causal_conv1d.py`, `vllm/v1/attention/backends/mamba2_attn.py`_
- **2026-10-16** [`e365792997`](https://github.com/vllm-project/vllm/commit/e365792997) [#61689](https://github.com/vllm-project/vllm/pull/61689)
  [Dependency] Upgrade TokenSpeed MLA to 2.0.3 (#61689)
  _Files: `requirements/cuda.txt`_
- **2026-10-16** [`05ad0a8ace`](https://github.com/vllm-project/vllm/commit/05ad0a8ace) [#58872](https://github.com/vllm-project/vllm/pull/58872)
  [Perf][DSv4.1] Split fused_wqa_wkv by token across TP ranks on SM90 (#58872)
  _Files: `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/model.py`_
- **2026-10-16** [`af28c171f5`](https://github.com/vllm-project/vllm/commit/af28c171f5) [#61913](https://github.com/vllm-project/vllm/pull/61913)
  [Dependency] Upgrade FlashInfer to 0.7.2 and restore KDA auto backend (#61913)
  _Files: `requirements/cuda.txt`, `vllm/models/kimi_k3/nvidia/kda.py`_
- **2026-10-15** [`d92a4f25f2`](https://github.com/vllm-project/vllm/commit/d92a4f25f2) [#59554](https://github.com/vllm-project/vllm/pull/59554)
  [watermarking] Add DFlash support to dual-key gumbel-max watermarking (#59554)
  _Files: `docs/features/watermarking.md`, `tests/test_config.py`, `tests/watermarking/test_watermarking.py`, `vllm/config/vllm.py` _+6 more__
- **2026-10-15** [`f8460ef236`](https://github.com/vllm-project/vllm/commit/f8460ef236) [#61371](https://github.com/vllm-project/vllm/pull/61371)
  [Kernel][DSv4.1] Bump FlashMLA to the 2026.09.30 release and its interleaved V4.1 KV cache (#61371)
  _Files: `cmake/external_projects/flashmla.cmake`, `csrc/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` _+9 more__
- **2026-10-15** [`54d9b1cb48`](https://github.com/vllm-project/vllm/commit/54d9b1cb48) [#61873](https://github.com/vllm-project/vllm/pull/61873)
  [GLM5.3 Perf] Inplace update draft decode metadata, 1.7% E2E Throughput Improvement (#61873)
  _Files: `vllm/v1/attention/backends/mla/flashinfer_mla_sparse.py`_
- **2026-10-15** [`ee8c47961b`](https://github.com/vllm-project/vllm/commit/ee8c47961b) [#61732](https://github.com/vllm-project/vllm/pull/61732)
  [CI] Use an ungated model as the attention test config default (#61732)
  _Files: `tests/v1/attention/test_attention_backends.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `tests/v1/attention/utils.py`_
- **2026-10-15** [`7cd7982dfd`](https://github.com/vllm-project/vllm/commit/7cd7982dfd) [#59468](https://github.com/vllm-project/vllm/pull/59468)
  [Spec Decode] Don't reserve DFlash/DSpark draft slots in the scheduler token budget (#59468)
  _Files: `tests/test_config.py`, `tests/v1/core/test_scheduler.py`, `vllm/config/speculative.py`, `vllm/config/vllm.py`_
- **2026-10-15** [`c825e1d235`](https://github.com/vllm-project/vllm/commit/c825e1d235) [#58737](https://github.com/vllm-project/vllm/pull/58737)
  [Perf] Fuse the mamba align block-table gather into one Triton kernel, 7 kernels -> 1, 6x speedup on all shapes for this kernel (#58737)
  _Files: `tests/v1/attention/test_mamba_align_block_table.py`, `vllm/v1/attention/backends/utils.py`_
- **2026-10-15** [`24f632ca7e`](https://github.com/vllm-project/vllm/commit/24f632ca7e) [#61647](https://github.com/vllm-project/vllm/pull/61647)
  [Bugfix] Engage indexer TP row sharding on total rows, not per-rank rows (#61647)
  _Files: `tests/v1/attention/test_indexer_tp_row_shard.py`, `vllm/config/attention.py`, `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-10-15** [`766c837bd5`](https://github.com/vllm-project/vllm/commit/766c837bd5) [#61778](https://github.com/vllm-project/vllm/pull/61778)
  [Model] Support every Decision 3.0 size (d3-flash, d3-mini, d3-nano, d3-lite, d3-edge) (#61778)
  _Files: `docs/models/structured_decisions_models.md`, `tests/models/multimodal/pooling/test_d3.py`, `tests/models/registry.py`, `vllm/model_executor/models/d3.py`_
- **2026-10-15** [`7020600b1d`](https://github.com/vllm-project/vllm/commit/7020600b1d) [#61074](https://github.com/vllm-project/vllm/pull/61074)
  [KV Connector][NIXL] Register packed MLA KV rows as a single region (#61074)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-15** [`32feecd91f`](https://github.com/vllm-project/vllm/commit/32feecd91f) [#61763](https://github.com/vllm-project/vllm/pull/61763)
  [CI] Pin DeepSeek-V4.1-Flash-NVFP4 eval to its FP8-Engram revision (#61763)
  _Files: `tests/evals/gsm8k/configs/DeepSeek-V4.1-Flash-NVFP4-DSpark-TP4.yaml`_
- **2026-10-15** [`81e1c3f183`](https://github.com/vllm-project/vllm/commit/81e1c3f183) [#58297](https://github.com/vllm-project/vllm/pull/58297)
  [XPU][MLA] Integrate XPU MLA support into the existing FLASH_ATTN_MLA backend (#58297)
  _Files: `tests/v1/attention/test_mla_backends.py`, `vllm/_xpu_ops.py`, `vllm/platforms/xpu.py`, `vllm/v1/attention/backends/fa_utils.py` _+1 more__
- **2026-10-14** [`7c3f7e5500`](https://github.com/vllm-project/vllm/commit/7c3f7e5500) [#61039](https://github.com/vllm-project/vllm/pull/61039)
  [Perf][DSv4.1] Length-aware candidate block selection in the decode indexer (#61039)
  _Files: `vllm/model_executor/kernels/attention/dsa/candidate_blocks.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-10-14** [`388a610dfb`](https://github.com/vllm-project/vllm/commit/388a610dfb) [#59511](https://github.com/vllm-project/vllm/pull/59511)
  [Perf][DFlash] Capture context combine and anchor in the draft CUDA graph (#59511)
  _Files: `tests/v1/spec_decode/test_lilicorr.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`, `vllm/v1/worker/gpu/spec_decode/lilicorr/speculator.py`_
- **2026-10-14** [`4975fda882`](https://github.com/vllm-project/vllm/commit/4975fda882) [#60948](https://github.com/vllm-project/vllm/pull/60948)
  [Dependency] Upgrade FlashInfer to 0.7.1 (#60948)
  _Files: `requirements/cuda.txt`, `vllm/models/kimi_k3/nvidia/kda.py`_
- **2026-10-14** [`e2e3e2b834`](https://github.com/vllm-project/vllm/commit/e2e3e2b834) [#61416](https://github.com/vllm-project/vllm/pull/61416)
  [CI] Use an ungated model in the DGX Spark XQA test (#61416)
  _Files: `tests/v1/attention/test_attention_backends.py`_
- **2026-10-14** [`3e851a7803`](https://github.com/vllm-project/vllm/commit/3e851a7803) [#61634](https://github.com/vllm-project/vllm/pull/61634)
  [Bugfix][Attention] Make the query contiguous for TRTLLM ragged MLA prefill (#61634)
  _Files: `vllm/v1/attention/backends/mla/prefill/trtllm_ragged.py`_
- **2026-10-14** [`937d6c19df`](https://github.com/vllm-project/vllm/commit/937d6c19df) [#61569](https://github.com/vllm-project/vllm/pull/61569)
  [Perf][GDN] Skip FLA chunk metadata when FlashInfer GDN prefill is active (#61569)
  _Files: `vllm/v1/attention/backends/gdn_attn.py`_
- **2026-10-14** [`badfcdbf91`](https://github.com/vllm-project/vllm/commit/badfcdbf91) [#60050](https://github.com/vllm-project/vllm/pull/60050)
  [Perf][GDN] Internal prefill checkpoints for the FlashInfer GDN prefill backend (#60050)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/mamba/test_gdn_prefill_flashinfer.py`, `tests/v1/attention/test_gdn_metadata_builder.py` _+8 more__
- **2026-10-14** [`a78d050eff`](https://github.com/vllm-project/vllm/commit/a78d050eff) [#61125](https://github.com/vllm-project/vllm/pull/61125)
  [Bugfix] Bump tokenspeed-mla to 2.0.2 to fix nanobind conflict with Triton 3.9 (#61125)
  _Files: `requirements/cuda.txt`_
- **2026-10-13** [`791f92135a`](https://github.com/vllm-project/vllm/commit/791f92135a) [#60908](https://github.com/vllm-project/vllm/pull/60908)
  [Attention] Set ALWAYS cudagraph support for FA4 (#60908)
  _Files: `vllm/v1/attention/backends/flash_attn.py`_
- **2026-10-13** [`292da21f9d`](https://github.com/vllm-project/vllm/commit/292da21f9d) [#60417](https://github.com/vllm-project/vllm/pull/60417)
  [HiSparse] Read GPU-resident KV directly for mixed and BF16 prefills (#60417)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/model_executor/layers/attention/sparse_mla_attention.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse_sm120.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py` _+1 more__
- **2026-10-13** [`2f18d13cf0`](https://github.com/vllm-project/vllm/commit/2f18d13cf0) [#61228](https://github.com/vllm-project/vllm/pull/61228)
  [GLM5.3 Perf] Enable fp8 kv cache for GLM5.3 Flash by default, 9.8% E2E Throughput Improvement (#61228)
  _Files: `vllm/model_executor/models/config.py`_
- **2026-10-13** [`3f550129e8`](https://github.com/vllm-project/vllm/commit/3f550129e8) [#55838](https://github.com/vllm-project/vllm/pull/55838)
  [Perf][Attention][MiniMax-M3] Select CUTLASS MSA by EAGLE3 decode shape (#55838)
  _Files: `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`_
- **2026-10-13** [`624a5ddafd`](https://github.com/vllm-project/vllm/commit/624a5ddafd) [#60654](https://github.com/vllm-project/vllm/pull/60654)
  [Attention] Fetch MLA prefill workspace at use instead of init (#60654)
  _Files: `tests/v1/attention/test_mla_prefill_registry.py`, `vllm/v1/attention/backends/mla/prefill/flashinfer.py`, `vllm/v1/attention/backends/mla/prefill/trtllm_ragged.py`_
- **2026-10-13** [`31e90ac370`](https://github.com/vllm-project/vllm/commit/31e90ac370) [#55866](https://github.com/vllm-project/vllm/pull/55866)
  [Attention] Enable FA4 sparse MQA decode on Blackwell (#55866)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`, `docs/design/attention_backends.md`, `tests/kernels/attention/test_flashinfer_mla_decode.py`, `tests/v1/attention/test_flashmla_nope_sm90_backend_selection.py` _+10 more__
- **2026-10-13** [`206e45d470`](https://github.com/vllm-project/vllm/commit/206e45d470) [#61200](https://github.com/vllm-project/vllm/pull/61200)
  [CI] Shard V1 Attention automatically instead of by fixed pytest shards (#61200)
  _Files: `.buildkite/test_areas/attention.yaml`_
- **2026-10-13** [`656d0d4506`](https://github.com/vllm-project/vllm/commit/656d0d4506) [#61355](https://github.com/vllm-project/vllm/pull/61355)
  [Perf] Tune Triton GDN decode tiles on SM100-family GPUs (#61355)
  _Files: `tests/kernels/fla/test_fused_recurrent_packed_decode.py`, `vllm/third_party/flash_linear_attention/ops/fused_recurrent.py`_
- **2026-10-13** [`86b1c2ef15`](https://github.com/vllm-project/vllm/commit/86b1c2ef15) [#61285](https://github.com/vllm-project/vllm/pull/61285)
  [Attention][DCP] Support a2a DCP comm backend for FlashMLA sparse (#61285)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-10-13** [`380638afbb`](https://github.com/vllm-project/vllm/commit/380638afbb) [#61308](https://github.com/vllm-project/vllm/pull/61308)
  [Model] Add Clef-Flash support (#61308)
  _Files: `docs/serving/online_serving/structured_decisions.md`, `tests/config/test_model_arch_config.py`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `tests/models/multimodal/pooling/test_clef_omni.py` _+7 more__
- **2026-10-13** [`98f7211162`](https://github.com/vllm-project/vllm/commit/98f7211162) [#56148](https://github.com/vllm-project/vllm/pull/56148)
  [Attention][Spec Decode] Multi-query Triton split-K for spec-decode verify, with empty-segment/padding hardening (#56148)
  _Files: `tests/kernels/attention/test_triton_unified_attention.py`, `tests/v1/attention/test_triton_attn_segments.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/ops/triton_attention_helpers.py` _+1 more__
- **2026-10-12** [`d6aca837c3`](https://github.com/vllm-project/vllm/commit/d6aca837c3) [#61023](https://github.com/vllm-project/vllm/pull/61023)
  [Attention] Make the sparse MLA prefill workspace size configurable (#61023)
  _Files: `vllm/config/attention.py`, `vllm/config/vllm.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`, `vllm/v1/attention/backends/mla/indexer.py`_
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

## Other  (48 commits)

- **2026-10-19** [`52e88e25ec`](https://github.com/vllm-project/vllm/commit/52e88e25ec) [#62228](https://github.com/vllm-project/vllm/pull/62228)
  [Core] Remove the obsolete VLLM_USE_RAY_V2_EXECUTOR_BACKEND env var (#62228)
  _Files: `vllm/envs.py`_
- **2026-10-18** [`6540d5c8f8`](https://github.com/vllm-project/vllm/commit/6540d5c8f8) [#52477](https://github.com/vllm-project/vllm/pull/52477)
  [Bugfix][Spec Decode][Structured Output] Drive grammar masks from GPU logit counts (#52477)
  _Files: `tests/v1/spec_decode/test_adaptive_verification.py`, `tests/v1/spec_decode/test_mtp_structured_output.py`, `tests/v1/structured_output/test_structured_output_manager.py`, `tests/v1/worker/test_gpu_batch_shard.py` _+6 more__
- **2026-10-17** [`03e8300d2c`](https://github.com/vllm-project/vllm/commit/03e8300d2c) [#61118](https://github.com/vllm-project/vllm/pull/61118)
  [Bugfix] Enable inductor batch-invariant mode under VLLM_BATCH_INVARIANT (#61118)
  _Files: `vllm/model_executor/determinism/batch_invariant.py`_
- **2026-10-17** [`e744eacf68`](https://github.com/vllm-project/vllm/commit/e744eacf68) [#61933](https://github.com/vllm-project/vllm/pull/61933)
  [Rust Frontend] Validate bad_words limits during request lowering (#61933)
  _Files: `rust/src/text/src/lower.rs`, `rust/src/text/src/lower/token_ids.rs`_
- **2026-10-17** [`4e964b2623`](https://github.com/vllm-project/vllm/commit/4e964b2623) [#61743](https://github.com/vllm-project/vllm/pull/61743)
  [XPU] Fix Event init failure w/ external (#61743)
  _Files: `vllm/v1/worker/xpu_model_runner.py`_
- **2026-10-17** [`b05ede5616`](https://github.com/vllm-project/vllm/commit/b05ede5616) [#62114](https://github.com/vllm-project/vllm/pull/62114)
  [Bugfix][Frontend] Preserve token IDs in completion derender responses (#62114)
  _Files: `tests/entrypoints/scale_out/derender/test_derender.py`, `vllm/renderers/online_derenderer.py`_
- **2026-10-17** [`61bb590877`](https://github.com/vllm-project/vllm/commit/61bb590877) [#61174](https://github.com/vllm-project/vllm/pull/61174)
  [Bugfix][Spec Decode] Clear stale shared block-table rows (#61174)
  _Files: `tests/v1/worker/test_gpu_block_table.py`, `vllm/v1/worker/gpu/block_table.py`_
- **2026-10-17** [`d74f4180cd`](https://github.com/vllm-project/vllm/commit/d74f4180cd) [#61876](https://github.com/vllm-project/vllm/pull/61876)
  [Bugfix][Frontend] Detokenize echoed prompts after truncation (#61876)
  _Files: `tests/renderers/test_completions.py`, `vllm/renderers/base.py`_
- **2026-10-17** [`556ac15eb9`](https://github.com/vllm-project/vllm/commit/556ac15eb9) [#61992](https://github.com/vllm-project/vllm/pull/61992)
  [Bugfix] Remove extra args from CPU's compute slot mapping kernel (#61992)
  _Files: `tests/model_executor/test_triton_dispatcher.py`, `vllm/utils/cpu_triton_utils.py`_
- **2026-10-17** [`f8112704d5`](https://github.com/vllm-project/vllm/commit/f8112704d5) [#61883](https://github.com/vllm-project/vllm/pull/61883)
  [Chore] Use upstream Transformers InklingProcessor (#61883)
  _Files: `vllm/models/inkling/common/mm_preprocess.py`, `vllm/transformers_utils/processors/__init__.py`, `vllm/transformers_utils/processors/inkling.py`_
- **2026-10-17** [`783380af39`](https://github.com/vllm-project/vllm/commit/783380af39) [#61718](https://github.com/vllm-project/vllm/pull/61718)
  [Bugfix] Fix NaN output of the Mamba2 chunk scan kernel on sm90 (#61718)
  _Files: `tests/kernels/mamba/test_mamba_ssm_ssd.py`, `vllm/model_executor/layers/mamba/ops/ssd_chunk_scan.py`_
- **2026-10-16** [`9731f30a03`](https://github.com/vllm-project/vllm/commit/9731f30a03) [#61211](https://github.com/vllm-project/vllm/pull/61211)
  [Bugfix] Keep VLLM_RAY_BUNDLE_INDICES out of the compile cache key (#61211)
  _Files: `tests/test_envs.py`, `vllm/envs.py`_
- **2026-10-16** [`1a5b187066`](https://github.com/vllm-project/vllm/commit/1a5b187066) [#62025](https://github.com/vllm-project/vllm/pull/62025)
  Add @bnellnm to CODEOWNERS (#62025)
  _Files: `.github/CODEOWNERS`_
- **2026-10-16** [`64175d3827`](https://github.com/vllm-project/vllm/commit/64175d3827) [#61852](https://github.com/vllm-project/vllm/pull/61852)
  [Bugfix][Frontend] Keep the parser's tool call IDs in batch derender (#61852)
  _Files: `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_parity.py`, `vllm/renderers/online_derenderer.py`_
- **2026-10-16** [`8f93c64866`](https://github.com/vllm-project/vllm/commit/8f93c64866) [#61924](https://github.com/vllm-project/vllm/pull/61924)
  [Bugfix] remove duplicate hash-routing capability method (#61924)
- **2026-10-15** [`d12ea8e309`](https://github.com/vllm-project/vllm/commit/d12ea8e309) [#61016](https://github.com/vllm-project/vllm/pull/61016)
  [Bugfix][MRV2] Keep input_ids on later PP stages for raw-token models (#61016)
  _Files: `tests/distributed/test_distributed_oot.py`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/__init__.py`, `tests/plugins/vllm_add_dummy_model/vllm_add_dummy_model/my_opt.py`, `tests/plugins_tests/test_oot_registration_online.py` _+2 more__
- **2026-10-15** [`338dab077c`](https://github.com/vllm-project/vllm/commit/338dab077c) [#61812](https://github.com/vllm-project/vllm/pull/61812)
  [Bugfix] Fix Apertus streaming scientific notation (#61812)
  _Files: `tests/tool_parsers/test_apertus_tool_parser.py`, `vllm/tool_parsers/apertus_tool_parser.py`_
- **2026-10-15** [`b7b20b1b8f`](https://github.com/vllm-project/vllm/commit/b7b20b1b8f) [#61757](https://github.com/vllm-project/vllm/pull/61757)
  [Bugfix][Frontend] Leave the final stop token out of chat derender text (#61757)
  _Files: `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/renderers/online_derenderer.py`_
- **2026-10-15** [`9cede34a67`](https://github.com/vllm-project/vllm/commit/9cede34a67) [#61044](https://github.com/vllm-project/vllm/pull/61044)
  [Bugfix] Create cuBLAS handles before memory profiling to avoid OOM (#61044)
  _Files: `vllm/v1/worker/gpu_worker.py`_
- **2026-10-14** [`9b5c6707a3`](https://github.com/vllm-project/vllm/commit/9b5c6707a3) [#61496](https://github.com/vllm-project/vllm/pull/61496)
  [Bugfix][MRV2] Capture DCP FULL cudagraphs with KV context (#61496)
  _Files: `tests/v1/cudagraph/test_cudagraph_manager.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/input_batch.py`_
- **2026-10-14** [`bf6c80c7e8`](https://github.com/vllm-project/vllm/commit/bf6c80c7e8) [#59294](https://github.com/vllm-project/vllm/pull/59294)
  [Misc] Remove tool name from warn logs (#59294)
  _Files: `vllm/renderers/chat_utils/chat_message.py`_
- **2026-10-14** [`efad400092`](https://github.com/vllm-project/vllm/commit/efad400092) [#60869](https://github.com/vllm-project/vllm/pull/60869)
  [HiSparse] Prefault the shared host pool in parallel (#60869)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `tests/v1/worker/test_utils.py`, `vllm/v1/hisparse/runtime.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py`_
- **2026-10-14** [`be4ce2e505`](https://github.com/vllm-project/vllm/commit/be4ce2e505) [#61237](https://github.com/vllm-project/vllm/pull/61237)
  [Bugfix] Share PCP-aware local GPU indexing for NUMA binding (#61237)
  _Files: `tests/utils_/test_numa_utils.py`, `tests/v1/executor/test_vllm_net_devices.py`, `vllm/config/parallel.py`, `vllm/utils/numa_utils.py` _+2 more__
- **2026-10-14** [`f4b8d43a68`](https://github.com/vllm-project/vllm/commit/f4b8d43a68) [#59984](https://github.com/vllm-project/vllm/pull/59984)
  [Bugfix] Keep force-killing the process tree when a child exits mid-walk (#59984)
  _Files: `tests/utils_/test_system_utils.py`, `vllm/utils/system_utils.py`_
- **2026-10-13** [`ac71b17517`](https://github.com/vllm-project/vllm/commit/ac71b17517) [#61323](https://github.com/vllm-project/vllm/pull/61323)
  [Model Loader] Keep norm layers neutral under dummy weight init (#61323)
  _Files: `tests/model_executor/test_weight_utils.py`, `vllm/model_executor/layers/layernorm.py`_
- **2026-10-13** [`de8291e24f`](https://github.com/vllm-project/vllm/commit/de8291e24f) [#59463](https://github.com/vllm-project/vllm/pull/59463)
  [Core] Add lifecycle hooks for worker extensions (#59463)
  _Files: `tests/v1/worker/test_worker_base.py`, `vllm/config/parallel.py`, `vllm/v1/worker/worker_base.py`_
- **2026-10-13** [`818f70c295`](https://github.com/vllm-project/vllm/commit/818f70c295) [#60749](https://github.com/vllm-project/vllm/pull/60749)
  [Bugfix] Mask special added tokens in xgrammar JSON, regex and EBNF grammars (#60749)
  _Files: `tests/v1/structured_output/test_backend_xgrammar_stop_tokens.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-10-13** [`cd7517fb17`](https://github.com/vllm-project/vllm/commit/cd7517fb17) [#60704](https://github.com/vllm-project/vllm/pull/60704)
  [Bugfix] Fix ReplaySSM ring shape assertion when TP does not divide Mamba2 n_groups (#60704)
  _Files: `tests/kernels/mamba/test_ssu_dispatch.py`, `vllm/model_executor/layers/mamba/mamba_utils.py`_
- **2026-10-13** [`54db759eea`](https://github.com/vllm-project/vllm/commit/54db759eea) [#58862](https://github.com/vllm-project/vllm/pull/58862)
  [Bugfix][Structured Output] Reject structural_tag and unhandled specs in backend validation (#58862)
  _Files: `tests/v1/structured_output/test_validation.py`, `vllm/v1/structured_output/backend_lm_format_enforcer.py`, `vllm/v1/structured_output/backend_outlines.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-10-13** [`c7a305ec10`](https://github.com/vllm-project/vllm/commit/c7a305ec10) [#60797](https://github.com/vllm-project/vllm/pull/60797)
  [Bugfix][Mamba] Store conv_kernel - 1 inputs in Mamba2 prefill checkpoints (#60797)
  _Files: `tests/kernels/mamba/test_mamba2_checkpoint_state.py`, `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/model_executor/layers/mamba/ops/ssd_checkpoint.py`_
- **2026-10-13** [`ff305934f1`](https://github.com/vllm-project/vllm/commit/ff305934f1) [#61342](https://github.com/vllm-project/vllm/pull/61342)
  [Tests][Mamba] Wait for accepted counts in fake MTP proposer (#61342)
  _Files: `tests/v1/e2e/general/test_mamba_prefix_cache.py`_
- **2026-10-13** [`69d00bc264`](https://github.com/vllm-project/vllm/commit/69d00bc264) [#61297](https://github.com/vllm-project/vllm/pull/61297)
  [Bugfix] Accept whole-number floats for integer tool arguments in the response parser (#61297)
  _Files: `tests/parser/test_chat_parsing.py`, `vllm/parser/chat_parsing/response_parser.py`_
- **2026-10-13** [`657a2e9417`](https://github.com/vllm-project/vllm/commit/657a2e9417) [#61299](https://github.com/vllm-project/vllm/pull/61299)
  [Rust Frontend] Accept whole-number floats for integer tool arguments (#61299)
  _Files: `rust/src/parser/src/tool/parameters.rs`_
- **2026-10-13** [`c5422f4c46`](https://github.com/vllm-project/vllm/commit/c5422f4c46) [#56129](https://github.com/vllm-project/vllm/pull/56129)
  [Test][Renderer] Cover the reasoning -> reasoning_content mirror in chat message parsing (#56129)
  _Files: `tests/renderers/test_chat_utils.py`_
- **2026-10-13** [`f47792af7f`](https://github.com/vllm-project/vllm/commit/f47792af7f) [#61134](https://github.com/vllm-project/vllm/pull/61134)
  [Model Loader] Make dummy weight init dtype-aware (#61134)
  _Files: `tests/model_executor/test_weight_utils.py`, `vllm/model_executor/model_loader/dummy_loader.py`, `vllm/model_executor/model_loader/weight_utils.py`_
- **2026-10-12** [`7039c7f17b`](https://github.com/vllm-project/vllm/commit/7039c7f17b) [#61220](https://github.com/vllm-project/vllm/pull/61220)
  [Bugfix][Rust Frontend] Omit unset sampling params in render output (#61220)
  _Files: `rust/src/server/src/routes/tests.rs`, `rust/src/text/src/request.rs`, `tests/entrypoints/scale_out/token_in_token_out/test_protocol.py`_
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

## Multimodal  (31 commits)

- **2026-10-19** [`3aad5392ab`](https://github.com/vllm-project/vllm/commit/3aad5392ab) [#62329](https://github.com/vllm-project/vllm/pull/62329)
  [Model] Support hotwords for MOSS-Transcribe-Diarize (#62329)
  _Files: `docs/serving/online_serving/speech_to_text.md`, `tests/models/multimodal/processing/test_moss_transcribe_diarize.py`, `vllm/model_executor/models/moss_transcribe_diarize.py`_
- **2026-10-19** [`3c8245b73d`](https://github.com/vllm-project/vllm/commit/3c8245b73d) [#60792](https://github.com/vllm-project/vllm/pull/60792)
  [Bugfix][Frontend] Align DeepSeek V4.1 images with rendered content (#60792)
  _Files: `tests/tokenizers_/test_deepseek_v41.py`, `vllm/renderers/deepseek_v4.py`, `vllm/renderers/registry.py`, `vllm/tokenizers/deepseek_v41.py` _+1 more__
- **2026-10-19** [`7dc1705433`](https://github.com/vllm-project/vllm/commit/7dc1705433) [#62224](https://github.com/vllm-project/vllm/pull/62224)
  [Bugfix][LoRA] Apply text-only LoRAs to the LM of multimodal wrappers (#62224)
  _Files: `tests/lora/test_lora_manager.py`, `vllm/lora/model_manager.py`_
- **2026-10-19** [`ebf5d31e15`](https://github.com/vllm-project/vllm/commit/ebf5d31e15) [#62237](https://github.com/vllm-project/vllm/pull/62237)
  [Model] Add ColUltraVBERT late-interaction retrieval model (#62237)
  _Files: `docs/models/pooling_models/specific_models.md`, `docs/models/pooling_models/token_embed.md`, `tests/models/multimodal/pooling/test_colultravbert.py`, `tests/models/registry.py` _+5 more__
- **2026-10-19** [`38127f6290`](https://github.com/vllm-project/vllm/commit/38127f6290) [#62204](https://github.com/vllm-project/vllm/pull/62204)
  [Multimodal][Docs] State that retried media downloads count toward the request budget (#62204)
  _Files: `docs/usage/security.md`, `tests/test_connections.py`, `vllm/connections.py`_
- **2026-10-18** [`6b24947628`](https://github.com/vllm-project/vllm/commit/6b24947628) [#61829](https://github.com/vllm-project/vllm/pull/61829)
  [CI/Build] Build DeepEP for SM103 (B300/GB300) in the Docker image (#61829)
  _Files: `docker/Dockerfile`_
- **2026-10-18** [`3c13653738`](https://github.com/vllm-project/vllm/commit/3c13653738) [#60877](https://github.com/vllm-project/vllm/pull/60877)
  [Frontend] Score with the chat template declared by Sentence Transformers CrossEncoders (#60877)
  _Files: `docs/models/pooling_models/scoring.md`, `docs/models/pooling_models/specific_models.md`, `tests/entrypoints/pooling/scoring/test_io_processor_unit.py`, `tests/models/language/pooling_mteb_test/test_nemotron.py` _+3 more__
- **2026-10-18** [`3f1b04e045`](https://github.com/vllm-project/vllm/commit/3f1b04e045) [#61759](https://github.com/vllm-project/vllm/pull/61759)
  [Bugfix] Fix Opencv video backend frames count missing for WebM video inputs (#61759)
  _Files: `tests/multimodal/test_video.py`, `tests/multimodal/utils.py`, `vllm/multimodal/video_decoders/opencv.py`_
- **2026-10-17** [`ec8b20fbf0`](https://github.com/vllm-project/vllm/commit/ec8b20fbf0) [#61365](https://github.com/vllm-project/vllm/pull/61365)
  [Bugfix] Fix Gemma 4 encoder CUDA graph capture OOM at startup (#61365)
  _Files: `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-10-16** [`2268d83bd9`](https://github.com/vllm-project/vllm/commit/2268d83bd9) [#61986](https://github.com/vllm-project/vllm/pull/61986)
  [Bugfix][Multimodal] Honor RGB PNG transparency when loading images (#61986)
  _Files: `docs/features/multimodal_inputs.md`, `tests/multimodal/media/test_image.py`, `tests/multimodal/test_hasher.py`, `tests/multimodal/test_image.py` _+2 more__
- **2026-10-16** [`49cb2bbf71`](https://github.com/vllm-project/vllm/commit/49cb2bbf71) [#61611](https://github.com/vllm-project/vllm/pull/61611)
  [Bugfix] Honor code_revision in config-based tokenizer loading (#61611)
  _Files: `tests/tokenizers_/test_basic.py`, `tests/tokenizers_/test_registry.py`, `vllm/tokenizers/registry.py`_
- **2026-10-15** [`71536bd5f8`](https://github.com/vllm-project/vllm/commit/71536bd5f8) [#46005](https://github.com/vllm-project/vllm/pull/46005)
  [MM][CG] Support ViT full CUDA graph for DeepSeek-VL2 (#46005)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py` _+1 more__
- **2026-10-15** [`427915bed2`](https://github.com/vllm-project/vllm/commit/427915bed2) [#61382](https://github.com/vllm-project/vllm/pull/61382)
  [Build][CPU] Install Run:ai Model Streamer in vllm-openai-cpu image (#61382)
  _Files: `docker/Dockerfile.cpu`_
- **2026-10-15** [`0f0bc4dbb1`](https://github.com/vllm-project/vllm/commit/0f0bc4dbb1) [#61765](https://github.com/vllm-project/vllm/pull/61765)
  [Test] Split the chat_utils tests. (#61765)
  _Files: `tests/renderers/chat_utils/__init__.py`, `tests/renderers/chat_utils/conftest.py`, `tests/renderers/chat_utils/test_assistant.py`, `tests/renderers/chat_utils/test_audio.py` _+11 more__
- **2026-10-15** [`a9fe30e9f6`](https://github.com/vllm-project/vllm/commit/a9fe30e9f6) [#59597](https://github.com/vllm-project/vllm/pull/59597)
  [Bugfix][Multimodal] Recover PyNvVideoCodec decoder slots after failures (#59597)
  _Files: `tests/multimodal/media/test_video.py`, `tests/multimodal/test_gpu_ipc_memory.py`, `tests/multimodal/test_video.py`, `vllm/multimodal/gpu_ipc_memory.py` _+4 more__
- **2026-10-14** [`d1d8e6c096`](https://github.com/vllm-project/vllm/commit/d1d8e6c096) [#60500](https://github.com/vllm-project/vllm/pull/60500)
  [Perf][Nemotron-Parse] Do image rescale/normalize on the device (#60500)
  _Files: `docs/design/mm_processing.md`, `tests/models/multimodal/processing/test_nemotron_parse.py`, `tests/models/registry.py`, `vllm/model_executor/models/nemotron_parse.py`_
- **2026-10-14** [`89cab55086`](https://github.com/vllm-project/vllm/commit/89cab55086) [#61565](https://github.com/vllm-project/vllm/pull/61565)
  [Model] Support Decision 3.0 decision models (vllm-sr/d3) (#61565)
  _Files: `docs/models/structured_decisions_models.md`, `tests/config/test_model_arch_config.py`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `tests/models/multimodal/pooling/test_d3.py` _+8 more__
- **2026-10-14** [`3a5a6b11a3`](https://github.com/vllm-project/vllm/commit/3a5a6b11a3) [#61458](https://github.com/vllm-project/vllm/pull/61458)
  [Perf][Model] Batch PaddleOCR-VL vision encoder and projector (#61458)
  _Files: `vllm/model_executor/models/paddleocr_vl.py`_
- **2026-10-14** [`23fbc2ec2f`](https://github.com/vllm-project/vllm/commit/23fbc2ec2f) [#61585](https://github.com/vllm-project/vllm/pull/61585)
  [Model] Support precomputed image embeddings for LightOnOCR (#61585)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_lightonocr.py`, `vllm/model_executor/models/lightonocr.py`, `vllm/model_executor/models/mistral3.py`_
- **2026-10-14** [`ec317a4618`](https://github.com/vllm-project/vllm/commit/ec317a4618) [#61535](https://github.com/vllm-project/vllm/pull/61535)
  [CI] Keep vLLM log propagation on through the first LLM init in caplog_vllm (#61535)
  _Files: `tests/conftest.py`, `tests/entrypoints/multimodal/llm/test_mm_cache_external_injection.py`_
- **2026-10-14** [`d5e62627a3`](https://github.com/vllm-project/vllm/commit/d5e62627a3) [#61475](https://github.com/vllm-project/vllm/pull/61475)
  [CI] Shard chat APIs, model evals and model tests automatically (#61475)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-10-13** [`12b005eefa`](https://github.com/vllm-project/vllm/commit/12b005eefa) [#52412](https://github.com/vllm-project/vllm/pull/52412)
  [Bugfix] Don't split a multimodal item that a prefill chunk starts exactly on (#52412)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-13** [`669f85e686`](https://github.com/vllm-project/vllm/commit/669f85e686) [#60972](https://github.com/vllm-project/vllm/pull/60972)
  [Misc] Break chat_utils into more maintainable modules. (#60972)
  _Files: `tests/entrypoints/cohere/test_serving_conversion.py`, `tests/entrypoints/unit_tests/test_chat_billing_header.py`, `tests/models/multimodal/processing/test_common.py`, `tests/renderers/test_chat_utils.py` _+17 more__
- **2026-10-13** [`61d9c777bf`](https://github.com/vllm-project/vllm/commit/61d9c777bf) [#61409](https://github.com/vllm-project/vllm/pull/61409)
  [CI] Run the Clef pooler test on GPU (#61409)
  _Files: `tests/models/multimodal/pooling/test_clef_omni.py`_
- **2026-10-13** [`0838cd6593`](https://github.com/vllm-project/vllm/commit/0838cd6593) [#61401](https://github.com/vllm-project/vllm/pull/61401)
  [Bugfix] Load and apply Nemotron Super final vision LayerNorm (#61401)
  _Files: `tests/models/multimodal/test_nano_nemotron_vl.py`, `vllm/model_executor/models/nano_nemotron_vl.py`_
- **2026-10-13** [`426f3bd36b`](https://github.com/vllm-project/vllm/commit/426f3bd36b) [#60979](https://github.com/vllm-project/vllm/pull/60979)
  [Bugfix][Model][Rust Frontend] Qwen3_ASR: Handle ragged Qwen audio batches from Rust frontend (#60979)
  _Files: `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/model_executor/models/qwen3_asr.py`_
- **2026-10-13** [`7173c64e2e`](https://github.com/vllm-project/vllm/commit/7173c64e2e) [#61226](https://github.com/vllm-project/vllm/pull/61226)
  [Security] Bound decoded and downloaded media per request (#61226)
  _Files: `docs/usage/security.md`, `tests/multimodal/media/test_audio.py`, `tests/multimodal/media/test_image.py`, `tests/multimodal/media/test_unprocessable_entity_error.py` _+12 more__
- **2026-10-13** [`5555a2d8f7`](https://github.com/vllm-project/vllm/commit/5555a2d8f7) [#61104](https://github.com/vllm-project/vllm/pull/61104)
  [Bugfix][Model] Fix EXAONE-4.5 image inputs: ViT received un-normalised pixels (#61104)
  _Files: `vllm/model_executor/models/exaone4_5.py`, `vllm/model_executor/models/exaone4_5_mtp.py`_
- **2026-10-13** [`28d679e762`](https://github.com/vllm-project/vllm/commit/28d679e762) [#61272](https://github.com/vllm-project/vllm/pull/61272)
  [Bugfix] Preserve independent tokenizer code_revision in snapshot resolution (#61272)
  _Files: `tests/tokenizers_/test_basic.py`, `vllm/tokenizers/registry.py`_
- **2026-10-12** [`1bdd3fa2d5`](https://github.com/vllm-project/vllm/commit/1bdd3fa2d5) [#59721](https://github.com/vllm-project/vllm/pull/59721)
  [Bugfix][Core] Check multimodal chunk boundaries before encoder cache reuse (#59721)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-12** [`f7a3a7265f`](https://github.com/vllm-project/vllm/commit/f7a3a7265f) [#57146](https://github.com/vllm-project/vllm/pull/57146)
  [Bugfix][Multimodal] Fix Qwen3-ASR audio preprocessing parity (#57146)
  _Files: `tests/models/multimodal/processing/test_qwen3_asr.py`, `vllm/model_executor/models/qwen3_asr.py`, `vllm/transformers_utils/processors/__init__.py`, `vllm/transformers_utils/processors/qwen3_asr.py`_

## CI / Build  (31 commits)

- **2026-10-18** [`072c0886d5`](https://github.com/vllm-project/vllm/commit/072c0886d5) [#56549](https://github.com/vllm-project/vllm/pull/56549)
  [Build] Keep plain CUDA arch when its suffixed variant is also requested (#56549)
  _Files: `cmake/utils.cmake`_
- **2026-10-18** [`953fa442fa`](https://github.com/vllm-project/vllm/commit/953fa442fa) [#62279](https://github.com/vllm-project/vllm/pull/62279)
  [CI] Per-test timeout for Language Models (Extended Pooling) (#62279)
  _Files: `.buildkite/test_areas/models_language.yaml`_
- **2026-10-18** [`83c9a547bf`](https://github.com/vllm-project/vllm/commit/83c9a547bf) [#62221](https://github.com/vllm-project/vllm/pull/62221)
  [CI][Release] Fix release wheel builds: stop excluding tracked recipes/ from Docker context (#62221)
  _Files: `.dockerignore`, `.pre-commit-config.yaml`, `tools/pre_commit/check_dockerignore_tracked.py`_
- **2026-10-18** [`b510857d37`](https://github.com/vllm-project/vllm/commit/b510857d37) [#60896](https://github.com/vllm-project/vllm/pull/60896)
  [Bugfix][Build] Build fused GDN MTP decode for SM80-SM90 with CUDA < 13 (#60896)
  _Files: `CMakeLists.txt`_
- **2026-10-17** [`e56b1603af`](https://github.com/vllm-project/vllm/commit/e56b1603af) [#62132](https://github.com/vllm-project/vllm/pull/62132)
  [Kernel]Add norm fused kernel for Step-5 Preview and Muse Spark Open (#62132)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_muse_spark_qknorm_rope_kv_insert.py`, `csrc/fused_muse_spark_qknorm_rope_kv_insert_kernel.cu`, `csrc/fused_qknorm_rope_cache_kernel.cu` _+6 more__
- **2026-10-16** [`9eb7fb9157`](https://github.com/vllm-project/vllm/commit/9eb7fb9157) [#61265](https://github.com/vllm-project/vllm/pull/61265)
  [Build] Remove unused `tools/install_deepgemm.sh` (#61265)
  _Files: `.buildkite/test_areas/kernels.yaml`, `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-10-16** [`3ddc6702a8`](https://github.com/vllm-project/vllm/commit/3ddc6702a8) [#60356](https://github.com/vllm-project/vllm/pull/60356)
  [XPU][Docker] Bump nixl to 1.5.0 (#60356)
  _Files: `docker/Dockerfile.xpu`_
- **2026-10-16** [`bee95149e2`](https://github.com/vllm-project/vllm/commit/bee95149e2) [#61744](https://github.com/vllm-project/vllm/pull/61744)
  Update DeepGEMM commit (#61744)
  _Files: `.buildkite/check-torch-abi.py`, `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-10-15** [`d6f0b7a416`](https://github.com/vllm-project/vllm/commit/d6f0b7a416) [#61648](https://github.com/vllm-project/vllm/pull/61648)
  [CI] Skip exited descendants when finding the worker in the FT e2e test (#61648)
  _Files: `tests/v1/fault_tolerance/test_fault_tolerance_e2e.py`_
- **2026-10-15** [`69425846f8`](https://github.com/vllm-project/vllm/commit/69425846f8) [#59472](https://github.com/vllm-project/vllm/pull/59472)
  [Bugfix][CPU] Report the real cause when the worker outgrows its memory reservation (#59472)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/v1/worker/test_cpu_worker_kv_budget.py`, `vllm/v1/worker/cpu_worker.py`_
- **2026-10-15** [`7f730b4cea`](https://github.com/vllm-project/vllm/commit/7f730b4cea) [#61782](https://github.com/vllm-project/vllm/pull/61782)
  [CI] Run 4xH100 steps nightly only (#61782)
  _Files: `.buildkite/test_areas/expert_parallelism.yaml`, `.buildkite/test_areas/lm_eval.yaml`_
- **2026-10-15** [`91ed2859c7`](https://github.com/vllm-project/vllm/commit/91ed2859c7) [#61411](https://github.com/vllm-project/vllm/pull/61411)
  [CPU][Zen] Update zentorch to 2.14.0.1 & enable float16 on Venice and later (#61411)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `docs/getting_started/installation/cpu.md`, `docs/getting_started/installation/cpu.x86.inc.md`, `setup.py` _+2 more__
- **2026-10-15** [`ab593678b5`](https://github.com/vllm-project/vllm/commit/ab593678b5) [#61740](https://github.com/vllm-project/vllm/pull/61740)
  [CI][XPU] Ignore test_reload.py on Intel CI (#61740)
  _Files: `.buildkite/intel_jobs/model_executor_intel.yaml`_
- **2026-10-15** [`a400804ce4`](https://github.com/vllm-project/vllm/commit/a400804ce4) [#57026](https://github.com/vllm-project/vllm/pull/57026)
  [CI] Relax MTP sharded sampling cross-boot noise bound (#57026)
  _Files: `tests/v1/e2e/spec_decode/test_sharded_sampling.py`_
- **2026-10-14** [`4b61f300c0`](https://github.com/vllm-project/vllm/commit/4b61f300c0) [#61684](https://github.com/vllm-project/vllm/pull/61684)
  [CI] Fix /ci run reporting a failed merge on fork PRs (#61684)
  _Files: `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-10-14** [`a4d553a46a`](https://github.com/vllm-project/vllm/commit/a4d553a46a) [#61703](https://github.com/vllm-project/vllm/pull/61703)
  Revert "[Build] Update deep_gemm git tag for locality_domain update" (#61703)
  _Files: `.buildkite/check-torch-abi.py`, `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-10-14** [`ded7ae35e5`](https://github.com/vllm-project/vllm/commit/ded7ae35e5) [#61491](https://github.com/vllm-project/vllm/pull/61491)
  [Build] Update deep_gemm git tag for locality_domain update (#61491)
  _Files: `.buildkite/check-torch-abi.py`, `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-10-14** [`47232f3c7f`](https://github.com/vllm-project/vllm/commit/47232f3c7f) [#61652](https://github.com/vllm-project/vllm/pull/61652)
  [Bugfix][CI] Fix renderers tests broken by tool name removal from warn logs (#61652)
  _Files: `tests/renderers/test_chat_utils.py`_
- **2026-10-14** [`13dbf96093`](https://github.com/vllm-project/vllm/commit/13dbf96093) [#61167](https://github.com/vllm-project/vllm/pull/61167)
  [Model Loader] Apply EP weight filtering in InstantTensor (#61167)
  _Files: `requirements/cuda.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+5 more__
- **2026-10-14** [`d36158f919`](https://github.com/vllm-project/vllm/commit/d36158f919) [#61592](https://github.com/vllm-project/vllm/pull/61592)
  [CI] Merge the target branch into stale PRs on /ci run (#61592)
  _Files: `.github/workflows/run-ci-command.yml`, `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`, `docs/contributing/README.md`_
- **2026-10-14** [`bb1438a93f`](https://github.com/vllm-project/vllm/commit/bb1438a93f) [#61590](https://github.com/vllm-project/vllm/pull/61590)
  [CI] Fix Unlimited-OCR loading after upstream `model_type` rename (#61590)
  _Files: `vllm/tokenizers/registry.py`, `vllm/transformers_utils/chat_templates/registry.py`, `vllm/transformers_utils/config.py`_
- **2026-10-14** [`449c05a0ca`](https://github.com/vllm-project/vllm/commit/449c05a0ca) [#61468](https://github.com/vllm-project/vllm/pull/61468)
  [CI][Tests] Upgrade torch version for Rubin prerelease (#61468)
  _Files: `requirements/rubin-prerelease.txt`_
- **2026-10-13** [`0da66a6e46`](https://github.com/vllm-project/vllm/commit/0da66a6e46) [#61474](https://github.com/vllm-project/vllm/pull/61474)
  [CI] Shard batch invariance, Kimi prefix cache, EP eval and generate APIs automatically (#61474)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/models_basic.yaml`_
- **2026-10-13** [`78b32b3fdc`](https://github.com/vllm-project/vllm/commit/78b32b3fdc) [#59482](https://github.com/vllm-project/vllm/pull/59482)
  Revert "[Build] DeepGEMM migration to torch Stable ABI (#59482)" (#61510)
  _Files: `.buildkite/check-torch-abi.py`, `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-10-13** [`a31054f5ef`](https://github.com/vllm-project/vllm/commit/a31054f5ef) [#60428](https://github.com/vllm-project/vllm/pull/60428)
  [NIXL] Bump CUDA 12 NIXL to 1.5.0 (#60428)
  _Files: `requirements/kv_connectors_cu12.txt`_
- **2026-10-13** [`f5fefbffe5`](https://github.com/vllm-project/vllm/commit/f5fefbffe5) [#59482](https://github.com/vllm-project/vllm/pull/59482)
  [Build] DeepGEMM migration to torch Stable ABI (#59482)
  _Files: `.buildkite/check-torch-abi.py`, `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-10-13** [`4e4eab73ed`](https://github.com/vllm-project/vllm/commit/4e4eab73ed) [#61202](https://github.com/vllm-project/vllm/pull/61202)
  [CI] Shard Model Executor and L4 Pipeline + Context Parallelism automatically (#61202)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/model_executor.yaml`_
- **2026-10-13** [`b337523c11`](https://github.com/vllm-project/vllm/commit/b337523c11) [#57911](https://github.com/vllm-project/vllm/pull/57911)
  [XPU] [Test] Extend spawn-safe sitecustomize monkeypatch to XPU (#57911)
  _Files: `.buildkite/intel_jobs/distributed_intel.yaml`, `tests/v1/shutdown/conftest.py`, `tests/v1/shutdown/test_forward_error.py`, `tests/v1/shutdown/test_startup_error.py`_
- **2026-10-12** [`654b725ea9`](https://github.com/vllm-project/vllm/commit/654b725ea9) [#61269](https://github.com/vllm-project/vllm/pull/61269)
  [CI] Pace the CRCR nightly report under the relay rate limit (#61269)
  _Files: `.buildkite/scripts/crcr-report.sh`, `.buildkite/scripts/crcr_report.py`_
- **2026-10-12** [`45bb710eca`](https://github.com/vllm-project/vllm/commit/45bb710eca) [#60456](https://github.com/vllm-project/vllm/pull/60456)
  [CI] Add nightly Python 3.14 smoke test (#60456)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/standalone_tests/python_only_compile.sh`_
- **2026-10-12** [`bfa7e5b7af`](https://github.com/vllm-project/vllm/commit/bfa7e5b7af) [#60784](https://github.com/vllm-project/vllm/pull/60784)
  [XPU][CI] Enable XPU graph in graph tests (#60784)
  _Files: `tests/v1/cudagraph/test_breakable_cudagraph.py`, `tests/v1/cudagraph/test_cudagraph_dispatch.py`, `tests/v1/cudagraph/test_cudagraph_mode.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py`_

## Serving / API  (29 commits)

- **2026-10-19** [`283d48f4eb`](https://github.com/vllm-project/vllm/commit/283d48f4eb) [#62253](https://github.com/vllm-project/vllm/pull/62253)
  [Bugfix][Frontend] Preserve scheduling priority for online and offline beam search (#62253)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/completion/test_completion_error.py`, `tests/samplers/test_beam_search_online.py`, `vllm/entrypoints/generate/beam_search/offline.py` _+4 more__
- **2026-10-19** [`ee22f682ab`](https://github.com/vllm-project/vllm/commit/ee22f682ab) [#61192](https://github.com/vllm-project/vllm/pull/61192)
  [Frontend] systemone: prefill the shared prefix once before the reads on hybrid models (#61192)
  _Files: `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `vllm/entrypoints/openai/decisions/strategies.py`_
- **2026-10-19** [`10e8e921b8`](https://github.com/vllm-project/vllm/commit/10e8e921b8) [#62010](https://github.com/vllm-project/vllm/pull/62010)
  [Bugfix][Frontend] Fix auto truncation without an output token limit (#62010)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/renderers/test_completions.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/responses/protocol.py` _+1 more__
- **2026-10-19** [`6af1e0ae27`](https://github.com/vllm-project/vllm/commit/6af1e0ae27) [#62205](https://github.com/vllm-project/vllm/pull/62205)
  [Bugfix][Frontend] Honor --enable-log-outputs on /v1/completions (#62205)
  _Files: `tests/entrypoints/openai/completion/test_completion_error.py`, `tests/entrypoints/openai/completion/test_completion_text_offset.py`, `vllm/entrypoints/generate/api_router.py`, `vllm/entrypoints/openai/completion/serving.py`_
- **2026-10-19** [`573f2f90b5`](https://github.com/vllm-project/vllm/commit/573f2f90b5) [#58385](https://github.com/vllm-project/vllm/pull/58385)
  [Frontend] Raise VLLMValidationError for an unknown Harmony channel in Responses output parsing (#58385)
  _Files: `tests/entrypoints/openai/responses/test_harmony_utils.py`, `vllm/entrypoints/openai/responses/harmony.py`_
- **2026-10-18** [`ff01a6b14f`](https://github.com/vllm-project/vllm/commit/ff01a6b14f) [#62072](https://github.com/vllm-project/vllm/pull/62072)
  [Bugfix][Frontend] Stop beam search on generation config EOS tokens (#62072)
  _Files: `tests/samplers/test_beam_search.py`, `tests/samplers/test_beam_search_online.py`, `vllm/entrypoints/generate/beam_search/offline.py`, `vllm/entrypoints/generate/beam_search/online.py` _+1 more__
- **2026-10-17** [`eb8de8d1a1`](https://github.com/vllm-project/vllm/commit/eb8de8d1a1) [#47630](https://github.com/vllm-project/vllm/pull/47630)
  [Bugfix][OpenAI] Respect allowed_token_ids in beam search (#47630)
  _Files: `tests/samplers/test_beam_search_online.py`, `vllm/entrypoints/generate/beam_search/offline.py`, `vllm/entrypoints/generate/beam_search/online.py`, `vllm/entrypoints/openai/chat_completion/protocol.py` _+2 more__
- **2026-10-17** [`b3a7e2ff6e`](https://github.com/vllm-project/vllm/commit/b3a7e2ff6e) [#61347](https://github.com/vllm-project/vllm/pull/61347)
  [RL][Frontend] Return weight-version spans on OpenAI completions and chat (#61347)
  _Files: `docs/training/async_rl.md`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/completion/test_completion_error.py`, `vllm/entrypoints/openai/chat_completion/protocol.py` _+3 more__
- **2026-10-16** [`153a17166e`](https://github.com/vllm-project/vllm/commit/153a17166e) [#62052](https://github.com/vllm-project/vllm/pull/62052)
  [Frontend] Add the Beam reasoning and tool parsers (#62052)
  _Files: `docs/features/tool_calling.md`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/parser/unified.rs` _+23 more__
- **2026-10-16** [`4ab99ff136`](https://github.com/vllm-project/vllm/commit/4ab99ff136) [#61990](https://github.com/vllm-project/vllm/pull/61990)
  [Bugfix][Frontend] Honor the constructor chat template in offline scoring (#61990)
  _Files: `docs/models/pooling_models/scoring.md`, `tests/entrypoints/pooling/scoring/test_io_processor_unit.py`, `vllm/entrypoints/pooling/offline.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`_
- **2026-10-16** [`92dc3dd393`](https://github.com/vllm-project/vllm/commit/92dc3dd393) [#61736](https://github.com/vllm-project/vllm/pull/61736)
  [Bugfix] Honor OPT token embedding width for prompt embeddings (#61736)
  _Files: `tests/entrypoints/openai/completion/test_prompt_validation.py`, `tests/models/language/generation/test_common.py`, `tests/models/registry.py`, `tests/renderers/chat_utils/test_prompt_embeds.py` _+5 more__
- **2026-10-15** [`3dcfaeb4e8`](https://github.com/vllm-project/vllm/commit/3dcfaeb4e8) [#59518](https://github.com/vllm-project/vllm/pull/59518)
  [Frontend] Apply each endpoint's top_logprobs cut in derender (#59518)
  _Files: `docs/serving/online_serving/derenderer.md`, `docs/serving/online_serving/renderer.md`, `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/inference/generate/convert.rs` _+8 more__
- **2026-10-15** [`252be28c18`](https://github.com/vllm-project/vllm/commit/252be28c18) [#61427](https://github.com/vllm-project/vllm/pull/61427)
  [Frontend] Replace return_mm_kwargs with an mm_payload enum on render requests (#61427)
  _Files: `docs/serving/online_serving/renderer.md`, `tests/entrypoints/scale_out/token_in_token_out/test_mm_serde.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/generate/base/protocol.py` _+5 more__
- **2026-10-15** [`c6b772cf6b`](https://github.com/vllm-project/vllm/commit/c6b772cf6b) [#61241](https://github.com/vllm-project/vllm/pull/61241)
  [Bugfix][Frontend] Emit kv/ec transfer params at the top level of render output (#61241)
  _Files: `tests/entrypoints/scale_out/render/test_render.py`, `vllm/entrypoints/scale_out/render/serving.py`_
- **2026-10-15** [`80dd705c1d`](https://github.com/vllm-project/vllm/commit/80dd705c1d) [#59324](https://github.com/vllm-project/vllm/pull/59324)
  [Frontend] Make finish_reason and Responses item status truthful (#59324)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/responses/test_parsable_context_unit.py`, `tests/entrypoints/openai/responses/test_responses_utils.py`, `tests/entrypoints/openai/responses/test_serving_responses.py` _+10 more__
- **2026-10-15** [`5d5c3d7c43`](https://github.com/vllm-project/vllm/commit/5d5c3d7c43) [#58143](https://github.com/vllm-project/vllm/pull/58143)
  [Bugfix] Preserve padding token types for cross encoders (#58143)
  _Files: `tests/entrypoints/pooling/scoring/test_io_processor_unit.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`, `vllm/entrypoints/pooling/scoring/utils.py`, `vllm/v1/worker/gpu/model_states/encoder_only.py` _+1 more__
- **2026-10-14** [`9d3dfa2886`](https://github.com/vllm-project/vllm/commit/9d3dfa2886) [#61339](https://github.com/vllm-project/vllm/pull/61339)
  [Benchmark] Add vllm bench forward: exact-shape forward timing (#61339)
  _Files: `.agents/skills/model-microbenchmark/SKILL.md`, `.claude/skills/model-microbenchmark`, `docs/cli/README.md`, `docs/mkdocs/gen_files/generate_argparse.py` _+10 more__
- **2026-10-14** [`467b024f21`](https://github.com/vllm-project/vllm/commit/467b024f21) [#61533](https://github.com/vllm-project/vllm/pull/61533)
  [Rust Frontend] Report vllm-proto schema version in ServerInfo (#61533)
  _Files: `rust/Cargo.lock`, `rust/proto/Cargo.toml`, `rust/proto/README.md`, `rust/proto/control.proto` _+3 more__
- **2026-10-14** [`e1726d9142`](https://github.com/vllm-project/vllm/commit/e1726d9142) [#61550](https://github.com/vllm-project/vllm/pull/61550)
  [Frontend] Add cache salt and tracing to openai decisions (#61550)
  _Files: `vllm/entrypoints/openai/decisions/protocol.py`, `vllm/entrypoints/openai/decisions/serving.py`_
- **2026-10-13** [`6d1daa9fe5`](https://github.com/vllm-project/vllm/commit/6d1daa9fe5) [#60926](https://github.com/vllm-project/vllm/pull/60926)
  [Bugfix][Frontend] Expose completion response schemas in OpenAPI (#60926)
  _Files: `tests/entrypoints/openai/test_openai_schema.py`, `tests/entrypoints/serve/utils/test_api_utils.py`, `vllm/entrypoints/openai/chat_completion/api_router.py`, `vllm/entrypoints/openai/completion/api_router.py` _+1 more__
- **2026-10-13** [`e6e84f350c`](https://github.com/vllm-project/vllm/commit/e6e84f350c) [#60164](https://github.com/vllm-project/vllm/pull/60164)
  [Feature][Pooling] Add offline fixed-length late chunking (#60164)
  _Files: `docs/models/pooling_models/token_embed.md`, `examples/pooling/token_embed/late_chunking_offline.py`, `tests/entrypoints/pooling/test_late_chunking.py`, `tests/entrypoints/pooling/token_embed/test_offline.py` _+11 more__
- **2026-10-12** [`1bc6e072b0`](https://github.com/vllm-project/vllm/commit/1bc6e072b0) [#59314](https://github.com/vllm-project/vllm/pull/59314)
  [Rust Frontend] Add per-request timing metrics to chat and completions (#59314)
  _Files: `rust/src/chat/src/event.rs`, `rust/src/chat/src/output/default/unified.rs`, `rust/src/chat/src/output/harmony/mod.rs`, `rust/src/chat/src/output/harmony/tests.rs` _+24 more__
- **2026-10-12** [`08582942d8`](https://github.com/vllm-project/vllm/commit/08582942d8) [#61236](https://github.com/vllm-project/vllm/pull/61236)
  [Bugfix][Frontend] Honor request_id and X-Request-Id in chat and completions render (#61236)
  _Files: `tests/entrypoints/scale_out/render/test_render.py`, `vllm/entrypoints/scale_out/render/api_router.py`, `vllm/entrypoints/scale_out/render/serving.py`_
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

## Scheduler / Engine  (27 commits)

- **2026-10-19** [`d5b36699b2`](https://github.com/vllm-project/vllm/commit/d5b36699b2) [#51488](https://github.com/vllm-project/vllm/pull/51488)
  [Core] Reject new requests while generation is paused (#51488)
  _Files: `docs/training/async_rl.md`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/stream.rs`, `rust/src/engine-core-client/src/protocol/output.rs` _+30 more__
- **2026-10-19** [`43caf5b352`](https://github.com/vllm-project/vllm/commit/43caf5b352) [#59030](https://github.com/vllm-project/vllm/pull/59030)
  [Bugfix][Core] Requeue encoder-stalled waiting requests (#59030)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-18** [`e0adacc9a6`](https://github.com/vllm-project/vllm/commit/e0adacc9a6) [#61892](https://github.com/vllm-project/vllm/pull/61892)
  [Bugfix][Rust Frontend] Use xgrammar for gRPC structured outputs (#61892)
  _Files: `rust/src/engine-core-client/src/protocol/structured_outputs.rs`, `rust/src/engine-core-client/src/protocol/structured_outputs/xgrammar.rs`, `rust/src/server/src/grpc/convert.rs`, `rust/src/server/src/grpc/tests.rs` _+4 more__
- **2026-10-17** [`255f14599e`](https://github.com/vllm-project/vllm/commit/255f14599e) [#62177](https://github.com/vllm-project/vllm/pull/62177)
  [Bugfix][Rust Frontend] Fix macOS build: read inherited listener family from its address (#62177)
  _Files: `rust/src/engine-core-client/src/transport.rs`_
- **2026-10-17** [`5c1c903501`](https://github.com/vllm-project/vllm/commit/5c1c903501) [#62027](https://github.com/vllm-project/vllm/pull/62027)
  [Perf][Parser] Stream Qwen3 tool argument values incrementally (12 KB call: 2.1 s to 11 ms) (#62027)
  _Files: `tests/parser/engine/test_qwen3.py`, `vllm/parser/mimo.py`, `vllm/parser/qwen3.py`_
- **2026-10-17** [`f98ae6a9fd`](https://github.com/vllm-project/vllm/commit/f98ae6a9fd) [#58778](https://github.com/vllm-project/vllm/pull/58778)
  [Bugfix][Core] Keep resumable sessions that stop while preempted (#58778)
  _Files: `tests/v1/streaming_input/test_async_llm_streaming.py`, `tests/v1/streaming_input/test_scheduler_streaming.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/engine/async_llm.py`_
- **2026-10-17** [`dcd07967ca`](https://github.com/vllm-project/vllm/commit/dcd07967ca) [#61805](https://github.com/vllm-project/vllm/pull/61805)
  [CPU] Keep the hybrid block size across the engine core's config rerun (#61805)
  _Files: `tests/v1/e2e/test_cpu_linear_attn_chunked_prefix.py`, `vllm/platforms/cpu.py`_
- **2026-10-16** [`b088eba944`](https://github.com/vllm-project/vllm/commit/b088eba944) [#62035](https://github.com/vllm-project/vllm/pull/62035)
  [Perf][Parser] Stream MiniMax M2 tool argument values incrementally (16 KB call: 5.9 s to 26 ms) (#62035)
  _Files: `tests/parser/engine/test_minimax_m2.py`, `vllm/parser/minimax_m2.py`_
- **2026-10-15** [`d486219fc2`](https://github.com/vllm-project/vllm/commit/d486219fc2) [#58668](https://github.com/vllm-project/vllm/pull/58668)
  [Bugfix][Core] Uncount stop-trimmed spec tokens from num_computed_tokens (#58668)
  _Files: `tests/v1/streaming_input/test_scheduler_streaming.py`, `vllm/v1/core/sched/async_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-15** [`957d512e96`](https://github.com/vllm-project/vllm/commit/957d512e96) [#58941](https://github.com/vllm-project/vllm/pull/58941)
  [Bugfix][Frontend] Preserve streaming chunk boundaries in RequestOutputCollector (#58941)
  _Files: `tests/v1/engine/test_output_processor.py`, `vllm/v1/engine/async_llm.py`, `vllm/v1/engine/output_processor.py`_
- **2026-10-15** [`ed3050add4`](https://github.com/vllm-project/vllm/commit/ed3050add4) [#54627](https://github.com/vllm-project/vllm/pull/54627)
  [Core] Apply prefill_schedule_interval outside data parallelism (#54627)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `vllm/config/scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-15** [`1463501553`](https://github.com/vllm-project/vllm/commit/1463501553) [#58942](https://github.com/vllm-project/vllm/pull/58942)
  [Bugfix] Terminate streaming sessions on ABORT/ERROR and prevent zombie sessions (#58942)
  _Files: `tests/v1/engine/test_engine_core_client.py`, `tests/v1/engine/test_output_processor.py`, `tests/v1/streaming_input/test_async_llm_streaming.py`, `vllm/v1/engine/async_llm.py` _+2 more__
- **2026-10-15** [`81e42c9987`](https://github.com/vllm-project/vllm/commit/81e42c9987) [#60630](https://github.com/vllm-project/vllm/pull/60630)
  [Feature][Frontend] Control the log level of request JSON body using env var (#60630)
  _Files: `tests/entrypoints/serve/utils/test_request_logger.py`, `vllm/engine/arg_utils.py`, `vllm/entrypoints/serve/utils/request_logger.py`, `vllm/envs.py`_
- **2026-10-14** [`4c5ea86f53`](https://github.com/vllm-project/vllm/commit/4c5ea86f53) [#61494](https://github.com/vllm-project/vllm/pull/61494)
  [Bugfix][Parser] Stream Gemma4 string tool arguments incrementally (#61494)
  _Files: `tests/parser/engine/test_gemma4_streaming_reasoning.py`, `tests/parser/engine/test_parser_engine.py`, `vllm/parser/engine/parser_engine.py`, `vllm/parser/engine/parser_engine_config.py` _+1 more__
- **2026-10-14** [`d3f6b2a7b3`](https://github.com/vllm-project/vllm/commit/d3f6b2a7b3) [#58043](https://github.com/vllm-project/vllm/pull/58043)
  [Frontend] Clean Client Facing 500 Report (#58043)
  _Files: `tests/entrypoints/serve/exception_handling/test_error_sanitization.py`, `vllm/entrypoints/serve/exception_handling/error_response.py`, `vllm/v1/engine/exceptions.py`_
- **2026-10-14** [`2631afd3fe`](https://github.com/vllm-project/vllm/commit/2631afd3fe) [#57378](https://github.com/vllm-project/vllm/pull/57378)
  [Bugfix][Platform] Fall back to torch when device-level NVML memory is unsupported (GB10) (#57378)
  _Files: `tests/engine/test_arg_utils.py`, `vllm/engine/arg_utils.py`, `vllm/platforms/cuda.py`_
- **2026-10-14** [`3f466c852c`](https://github.com/vllm-project/vllm/commit/3f466c852c) [#59928](https://github.com/vllm-project/vllm/pull/59928)
  [Bugfix][Parser] Recover genuine tool calls after unclosed Qwen3 <function= opener in prose (#59928)
  _Files: `tests/parser/engine/test_qwen3.py`, `vllm/parser/qwen3.py`_
- **2026-10-14** [`8a8e2baa02`](https://github.com/vllm-project/vllm/commit/8a8e2baa02) [#61586](https://github.com/vllm-project/vllm/pull/61586)
  [Bugfix][Rust Frontend] Inject VLLM_USE_RUST_FRONTEND=1 into `vllm-rs` managed engine envs  (#61586)
  _Files: `rust/src/managed-engine/src/process.rs`_
- **2026-10-14** [`aa0c433a3e`](https://github.com/vllm-project/vllm/commit/aa0c433a3e) [#61525](https://github.com/vllm-project/vllm/pull/61525)
  [Frontend] Accept `--reasoning-parser none` as the unset default (#61525)
  _Files: `tests/entrypoints/launchers/test_cli_args.py`, `vllm/engine/arg_utils.py`_
- **2026-10-14** [`a2fb482732`](https://github.com/vllm-project/vllm/commit/a2fb482732) [#57139](https://github.com/vllm-project/vllm/pull/57139)
  [KVConnector][P2P] Register peers off the scheduler thread (#57139)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_data_transport.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/data/base.py` _+2 more__
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

## Quantization  (24 commits)

- **2026-10-19** [`bbf59fbad4`](https://github.com/vllm-project/vllm/commit/bbf59fbad4) [#55537](https://github.com/vllm-project/vllm/pull/55537)
  [Kernel] Reject unsupported layouts in CUTLASS 3.x scaled_mm (#55537)
  _Files: `.buildkite/test_areas/kernels.yaml`, `csrc/quantization/w8a8/cutlass/scaled_mm_entry.cu`, `tests/kernels/quantization/test_cutlass_scaled_mm.py`_
- **2026-10-19** [`42472f9903`](https://github.com/vllm-project/vllm/commit/42472f9903) [#61965](https://github.com/vllm-project/vllm/pull/61965)
  [CPU][Bugfix] Flatten >2-D activations in the AMX int8 W8A8 linear path (#61965)
  _Files: `tests/kernels/quantization/test_scaled_mm_kernel_selection.py`, `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`_
- **2026-10-18** [`1b2a666391`](https://github.com/vllm-project/vllm/commit/1b2a666391) [#62245](https://github.com/vllm-project/vllm/pull/62245)
  [Doc][Recipe] Fix for redhat fp8 xeon support issue (#62245)
  _Files: `recipes/models/Qwen/Qwen2.5-VL-7B-Instruct.yaml`, `recipes/models/Qwen/Qwen3-4B.yaml`, `recipes/models/meta-llama/Llama-3.1-8B-Instruct.yaml`, `recipes/models/meta-llama/Llama-3.3-70B-Instruct.yaml` _+1 more__
- **2026-10-17** [`237d99b4af`](https://github.com/vllm-project/vllm/commit/237d99b4af) [#61551](https://github.com/vllm-project/vllm/pull/61551)
  Revert "[Docs] Add train-inference consistency agent skill" (#61551) (#62186)
  _Files: `.agents/skills/train-inference-consistency/SKILL.md`, `.agents/skills/train-inference-consistency/agents/openai.yaml`, `.agents/skills/train-inference-consistency/guides/backward-validation.md`, `.agents/skills/train-inference-consistency/guides/bi-kernels.md` _+14 more__
- **2026-10-17** [`2d8efee9a7`](https://github.com/vllm-project/vllm/commit/2d8efee9a7) [#61551](https://github.com/vllm-project/vllm/pull/61551)
  [Docs] Add train-inference consistency agent skill (#61551)
  _Files: `.agents/skills/train-inference-consistency/SKILL.md`, `.agents/skills/train-inference-consistency/agents/openai.yaml`, `.agents/skills/train-inference-consistency/guides/backward-validation.md`, `.agents/skills/train-inference-consistency/guides/bi-kernels.md` _+14 more__
- **2026-10-17** [`08a65e287e`](https://github.com/vllm-project/vllm/commit/08a65e287e) [#61944](https://github.com/vllm-project/vllm/pull/61944)
  [Bugfix][Kernel] hadacore: don't load past the input on a partial last warp (#61944)
  _Files: `csrc/quantization/hadamard/hadacore/hadamard_transform_cuda.cu`_
- **2026-10-16** [`07f3857fb9`](https://github.com/vllm-project/vllm/commit/07f3857fb9) [#51965](https://github.com/vllm-project/vllm/pull/51965)
  [XPU][Linear][MXFP4] enable torch as mxfp4 linear backend on xpu (#51965)
  _Files: `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/mxfp4/pytorch.py`_
- **2026-10-16** [`fb3fec970e`](https://github.com/vllm-project/vllm/commit/fb3fec970e) [#61716](https://github.com/vllm-project/vllm/pull/61716)
  [Bugfix][Kernel] silu_and_mul_quant: run the vectorized loop (#61716)
  _Files: `csrc/quantization/activation_kernels.cu`_
- **2026-10-15** [`784d1fff0c`](https://github.com/vllm-project/vllm/commit/784d1fff0c) [#59973](https://github.com/vllm-project/vllm/pull/59973)
  [MRV2][Spec Decode] Quantized draft lm_head for drafters that share the target head (#59973)
  _Files: `docs/features/speculative_decoding/mtp.md`, `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_mtp.py`, `tests/v1/worker/test_gpu_draft_lm_head.py`, `tests/v1/worker/test_gpu_worker_weight_transfer.py` _+7 more__
- **2026-10-15** [`4d9a8d6a41`](https://github.com/vllm-project/vllm/commit/4d9a8d6a41) [#61858](https://github.com/vllm-project/vllm/pull/61858)
  [Bugfix] Make Humming DeviceInfo lookups traceable under torch.compile (#61858)
  _Files: `.buildkite/test_areas/quantization.yaml`, `tests/quantization/test_humming_compile.py`, `vllm/utils/humming.py`_
- **2026-10-15** [`de2b869ee9`](https://github.com/vllm-project/vllm/commit/de2b869ee9) [#57331](https://github.com/vllm-project/vllm/pull/57331)
  [Bugfix][Kernel] Register int8 scaled_mm as a custom op (#57331)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/triton.py`_
- **2026-10-14** [`222e00fc44`](https://github.com/vllm-project/vllm/commit/222e00fc44) [#61678](https://github.com/vllm-project/vllm/pull/61678)
  [CI/Build] Fix test_deepseek_v41_mxfp8_scale_loading after #57797 (#61678)
  _Files: `tests/quantization/test_fp8.py`_
- **2026-10-14** [`b4b7eca0ef`](https://github.com/vllm-project/vllm/commit/b4b7eca0ef) [#58032](https://github.com/vllm-project/vllm/pull/58032)
  [Bugfix][Quantization] Clamp FP8 scales before UE8M0 rounding (#58032)
  _Files: `tests/kernels/quantization/test_fp8_quant_group.py`, `vllm/model_executor/layers/quantization/input_quant_fp8.py`_
- **2026-10-14** [`d39c2fb05a`](https://github.com/vllm-project/vllm/commit/d39c2fb05a) [#59935](https://github.com/vllm-project/vllm/pull/59935)
  [Bugfix][Gemma4] Quantize audio towers independently (#59935)
  _Files: `vllm/model_executor/models/gemma4_mm.py`_
- **2026-10-14** [`4dc5add6ea`](https://github.com/vllm-project/vllm/commit/4dc5add6ea) [#51933](https://github.com/vllm-project/vllm/pull/51933)
  [XPU] [Linear] [MXFP8] enable torch as mxfp8 linear backend (#51933)
  _Files: `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/mxfp8/pytorch.py`_
- **2026-10-14** [`77154ca611`](https://github.com/vllm-project/vllm/commit/77154ca611) [#60992](https://github.com/vllm-project/vllm/pull/60992)
  [Perf][Model][Qwen4Exp] QSA: decode four FP8 e4m3 bytes per register below sm_89 (#60992)
  _Files: `vllm/models/qwen4_exp/nvidia/ops/qsa.py`_
- **2026-10-13** [`6a03954b45`](https://github.com/vllm-project/vllm/commit/6a03954b45) [#61477](https://github.com/vllm-project/vllm/pull/61477)
  [CI] Shard quantization, pooling, multimodal APIs, core kernels and PCP eval automatically (#61477)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/models_language.yaml` _+2 more__
- **2026-10-13** [`6463d04601`](https://github.com/vllm-project/vllm/commit/6463d04601) [#46685](https://github.com/vllm-project/vllm/pull/46685)
  Fix write-after-write hazard in xpu KV RoPE triton kernel (#46685)
  _Files: `vllm/models/deepseek_v4/xpu/xpu_qnorm_rope_kv_fp8_insert.py`_
- **2026-10-13** [`c19c263ac8`](https://github.com/vllm-project/vllm/commit/c19c263ac8) [#60927](https://github.com/vllm-project/vllm/pull/60927)
  [GLM 5.3 Perf] Handle two elements at the same time for per token group quant, 2.8% E2E ITL improvement (#60927)
  _Files: `csrc/quantization/w8a8/fp8/per_token_group_quant.cu`_
- **2026-10-13** [`b33cb81237`](https://github.com/vllm-project/vllm/commit/b33cb81237) [#60524](https://github.com/vllm-project/vllm/pull/60524)
  [Bugfix] Keep compressed-tensors wNa16 linear layers batch invariant (#60524)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`_
- **2026-10-13** [`0fae39a014`](https://github.com/vllm-project/vllm/commit/0fae39a014) [#61343](https://github.com/vllm-project/vllm/pull/61343)
  [Perf] per_token_group_quant_8bit: multiply by reciprocal instead of dividing per element (#61343)
  _Files: `csrc/quantization/fused_kernels/layernorm_utils.cuh`, `csrc/quantization/w8a8/fp8/per_token_group_quant.cu`_
- **2026-10-13** [`69d2b6f82d`](https://github.com/vllm-project/vllm/commit/69d2b6f82d) [#51755](https://github.com/vllm-project/vllm/pull/51755)
  [CI][XPU] Standardize test job labels for intel jobs (#51755)
  _Files: `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/intel_jobs/basic_correctness_intel.yaml`, `.buildkite/intel_jobs/benchmarks_intel.yaml`, `.buildkite/intel_jobs/engine_intel.yaml` _+12 more__
- **2026-10-12** [`12e6a585ae`](https://github.com/vllm-project/vllm/commit/12e6a585ae) [#61108](https://github.com/vllm-project/vllm/pull/61108)
  [Fix][Compile] Declare group_shape in the static FP8 quant fusion … (#61108)
  _Files: `vllm/compilation/passes/fusion/matcher_utils.py`_
- **2026-10-12** [`6a70913590`](https://github.com/vllm-project/vllm/commit/6a70913590) [#60976](https://github.com/vllm-project/vllm/pull/60976)
  [XPU] bump up auto-round-lib to 0.16.0 (#60976)
  _Files: `requirements/xpu.txt`, `tests/quantization/test_auto_round.py`_

## Disaggregation / PD  (22 commits)

- **2026-10-19** [`b29be52357`](https://github.com/vllm-project/vllm/commit/b29be52357) [#62392](https://github.com/vllm-project/vllm/pull/62392)
  [Perf][AuxOutput] Do not rescan referenced keys in the routed-experts store (#62392)
  _Files: `tests/distributed/aux_output_connector/test_store.py`, `vllm/distributed/aux_output_connector/store.py`_
- **2026-10-17** [`9c778e9ff8`](https://github.com/vllm-project/vllm/commit/9c778e9ff8) [#62081](https://github.com/vllm-project/vllm/pull/62081)
  [Bugfix][EPLB] Wait for pending expert buffer copies before NIXL READs (#62081)
  _Files: `vllm/distributed/eplb/eplb_communicator.py`_
- **2026-10-17** [`7879f3687b`](https://github.com/vllm-project/vllm/commit/7879f3687b) [#62210](https://github.com/vllm-project/vllm/pull/62210)
  [NIXL] Drop unreachable producer-side notif counting in push mode (#62210)
  _Files: `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/push_worker.py`_
- **2026-10-17** [`6b6a6c5c98`](https://github.com/vllm-project/vllm/commit/6b6a6c5c98) [#60934](https://github.com/vllm-project/vllm/pull/60934)
  [RL] Support per-parameter source layouts for NCCL M2N (#60934)
  _Files: `docs/training/weight_transfer/m2n.md`, `examples/rl/rlhf_m2n.py`, `tests/distributed/test_weight_transfer_m2n.py`, `vllm/distributed/weight_transfer/m2n_common.py` _+4 more__
- **2026-10-16** [`a94c315711`](https://github.com/vllm-project/vllm/commit/a94c315711) [#59559](https://github.com/vllm-project/vllm/pull/59559)
  [DP] Engines own wave wake-ups; drop the front-end FIRST_REQ (#59559)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/coordinator/external.rs`, `rust/src/engine-core-client/src/coordinator/handle.rs`, `rust/src/engine-core-client/src/coordinator/inproc.rs` _+9 more__
- **2026-10-16** [`9a16d43ef0`](https://github.com/vllm-project/vllm/commit/9a16d43ef0) [#61218](https://github.com/vllm-project/vllm/pull/61218)
  [Bugfix][Mooncake] Fix MultiConnector stats and proxy SSE responses (#61218)
  _Files: `.buildkite/test_areas/misc.yaml`, `examples/disaggregated/mooncake_connector/mooncake_connector_proxy.py`, `tests/v1/kv_connector/unit/test_mooncake_proxy.py`, `tests/v1/kv_connector/unit/test_multi_connector.py` _+1 more__
- **2026-10-16** [`dd9e07a25f`](https://github.com/vllm-project/vllm/commit/dd9e07a25f) [#43202](https://github.com/vllm-project/vllm/pull/43202)
  [Feature] Add External LB Mode Support for Elastic EP Scaling (#43202)
  _Files: `tests/distributed/test_elastic_ep.py`, `tests/v1/distributed/test_external_lb_dp.py`, `tests/v1/engine/test_core_engine_actor_manager.py`, `tests/v1/engine/test_engine_core_client.py` _+14 more__
- **2026-10-15** [`de7d70676d`](https://github.com/vllm-project/vllm/commit/de7d70676d) [#61767](https://github.com/vllm-project/vllm/pull/61767)
  [Perf] Low-latency CPU all-reduce for DP metadata syncs (#61767)
  _Files: `.buildkite/test_areas/distributed.yaml`, `tests/distributed/test_cpu_all_reduce.py`, `tests/v1/worker/test_gpu_ubatch_slicing.py`, `vllm/config/parallel.py` _+3 more__
- **2026-10-15** [`49f944be3e`](https://github.com/vllm-project/vllm/commit/49f944be3e) [#61668](https://github.com/vllm-project/vllm/pull/61668)
  [Perf][HiSparse] Reuse pinned host pool after graph profiling (#61668)
  _Files: `tests/v1/worker/test_attn_utils.py`, `tests/v1/worker/test_kv_cache_allocation_scope.py`, `tests/v1/worker/test_utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/hisparse/worker.py` _+2 more__
- **2026-10-15** [`a97d19d792`](https://github.com/vllm-project/vllm/commit/a97d19d792) [#61789](https://github.com/vllm-project/vllm/pull/61789)
  [UMBP][1/10] Add shared connector, runtime contracts, and request lifecycle (#61789)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/umbp/__init__.py`, `vllm/distributed/kv_transfer/kv_connector/v1/umbp/connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/umbp/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/umbp/runtime/__init__.py` _+4 more__
- **2026-10-15** [`1c4c319792`](https://github.com/vllm-project/vllm/commit/1c4c319792) [#61479](https://github.com/vllm-project/vllm/pull/61479)
  [Frontend] Advertise `--enable-x`/`--disable-x` for boolean CLI flags (#61479)
  _Files: `docs/design/shm_tensor_arena.md`, `docs/features/mooncake_ec_connector_usage.md`, `docs/features/preload.md`, `docs/models/structured_decisions_models.md` _+9 more__
- **2026-10-15** [`8f111b22ee`](https://github.com/vllm-project/vllm/commit/8f111b22ee) [#61541](https://github.com/vllm-project/vllm/pull/61541)
  [CI] Run 4xB200 steps nightly only (#61541)
  _Files: `.buildkite/test_areas/disaggregated_mooncake.yaml`, `.buildkite/test_areas/models_basic.yaml`_
- **2026-10-15** [`6605802904`](https://github.com/vllm-project/vllm/commit/6605802904) [#59825](https://github.com/vllm-project/vllm/pull/59825)
  [Perf][KV Connector][Mooncake] Send the KV layout once per peer (#59825)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-10-14** [`3ccc0a90b6`](https://github.com/vllm-project/vllm/commit/3ccc0a90b6) [#59625](https://github.com/vllm-project/vllm/pull/59625)
  [KV Connector] Support sleep mode with MooncakeConnector over RDMA (#59625)
  _Files: `docs/features/nixl_connector_usage.md`, `tests/v1/kv_connector/mooncake_integration/config_sweep_accuracy_test.sh`, `tests/v1/kv_connector/mooncake_integration/run_accuracy_test.sh`, `tests/v1/kv_connector/mooncake_integration/test_accuracy.py` _+10 more__
- **2026-10-14** [`87e7dce3a7`](https://github.com/vllm-project/vllm/commit/87e7dce3a7) [#56716](https://github.com/vllm-project/vllm/pull/56716)
  [MRV2] Keep warmup out of the EPLB load stats (#56716)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2_cudagraph_profiling.py`, `vllm/distributed/eplb/eplb_state.py`, `vllm/v1/worker/gpu/eplb_utils.py`, `vllm/v1/worker/gpu/model_runner.py` _+1 more__
- **2026-10-13** [`8082b62f32`](https://github.com/vllm-project/vllm/commit/8082b62f32) [#60712](https://github.com/vllm-project/vllm/pull/60712)
  [Mooncake] Allow Mamba cache mode `none` for capacity-only workers (#60712)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/scheduler.py`_
- **2026-10-13** [`7342dc0317`](https://github.com/vllm-project/vllm/commit/7342dc0317) [#60638](https://github.com/vllm-project/vllm/pull/60638)
  [MoRIIO] Require pending remote prefill for READ cache hits (#60638)
  _Files: `tests/v1/kv_connector/unit/test_moriio_hma_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`_
- **2026-10-13** [`3ad096faf8`](https://github.com/vllm-project/vllm/commit/3ad096faf8) [#60826](https://github.com/vllm-project/vllm/pull/60826)
  [Bugfix][EC Connector] Don't create hash directories on cache-miss lookups in ECExampleConnector (#60826)
  _Files: `tests/v1/ec_connector/unit/test_ec_example_connector.py`, `vllm/distributed/ec_transfer/ec_connector/example_connector.py`_
- **2026-10-12** [`802feb6770`](https://github.com/vllm-project/vllm/commit/802feb6770) [#57705](https://github.com/vllm-project/vllm/pull/57705)
  [Bugfix][KVConnector] Fix MoRI-IO WRITE-mode requests stranded in WAITING_FOR_REMOTE_KVS (#57705)
  _Files: `tests/v1/kv_connector/unit/test_moriio_write_done_routing.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`_
- **2026-10-12** [`5b0b8f251e`](https://github.com/vllm-project/vllm/commit/5b0b8f251e) [#60941](https://github.com/vllm-project/vllm/pull/60941)
  [Bugfix][HiSparse] Fix TP group hang on steps without scheduled tokens (#60941)
  _Files: `tests/v1/kv_connector/unit/test_hisparse_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/hisparse/worker.py`_
- **2026-10-12** [`258b97ff6b`](https://github.com/vllm-project/vllm/commit/258b97ff6b) [#57904](https://github.com/vllm-project/vllm/pull/57904)
  [Bugfix][EC Connector] Size transfers by measured encoder output widths (#57904)
  _Files: `docs/features/ec_cpu_connector.md`, `tests/v1/ec_connector/unit/cpu/scheduler/test_scheduler.py`, `tests/v1/ec_connector/unit/cpu/test_ec_shared_region.py`, `tests/v1/ec_connector/unit/cpu/worker/test_worker.py` _+14 more__
- **2026-10-12** [`74f4404f58`](https://github.com/vllm-project/vllm/commit/74f4404f58) [#61000](https://github.com/vllm-project/vllm/pull/61000)
  [Bugfix][Distributed] Own SHM out-of-band buffers before releasing read slots (#61000)
  _Files: `tests/distributed/test_shm_broadcast.py`, `vllm/distributed/device_communicators/shm_broadcast.py`_

## KV Cache / Offload  (21 commits)

- **2026-10-19** [`4bd75e952a`](https://github.com/vllm-project/vllm/commit/4bd75e952a) [#60374](https://github.com/vllm-project/vllm/pull/60374)
  [Bugfix][KV Offload][P2P] Report NIXL submission failures and escalate persistent faults to session teardown (#60374)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_data_transport.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/data/base.py` _+4 more__
- **2026-10-17** [`ce8853d27a`](https://github.com/vllm-project/vllm/commit/ce8853d27a) [#61674](https://github.com/vllm-project/vllm/pull/61674)
  [Bugfix][KV Offload] Allow explicit SimpleCPUOffload block counts (#61674)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/simple_kv_offload/test_scheduler.py`, `tests/v1/simple_kv_offload/test_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/simple_cpu_offload_connector.py` _+2 more__
- **2026-10-16** [`b544587408`](https://github.com/vllm-project/vllm/commit/b544587408) [#53558](https://github.com/vllm-project/vllm/pull/53558)
  [Core][Feat] Pluggable KVCacheConfigBuilder for platform/model-specific KV cache planning (#53558)
  _Files: `tests/v1/core/test_kv_cache_config_builder.py`, `vllm/config/model.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/registry.py` _+5 more__
- **2026-10-15** [`33212db2c2`](https://github.com/vllm-project/vllm/commit/33212db2c2) [#61865](https://github.com/vllm-project/vllm/pull/61865)
  [KV Connector][NIXL] Reject NVFP4 KV cache with heterogeneous TP head split (#61865)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-15** [`21f4b6dc84`](https://github.com/vllm-project/vllm/commit/21f4b6dc84) [#59546](https://github.com/vllm-project/vllm/pull/59546)
  [KV Offload] Split the CPU offload region across shm files (#59546)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py`, `vllm/v1/kv_offload/cpu/spec.py`_
- **2026-10-15** [`8b27d27402`](https://github.com/vllm-project/vllm/commit/8b27d27402) [#60279](https://github.com/vllm-project/vllm/pull/60279)
  [Bugfix][KV Offload] Always attempt NIXL agent removal during peer teardown (#60279)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_data_transport.py`, `vllm/v1/kv_offload/tiering/p2p/data/nixl.py`_
- **2026-10-15** [`48f17b77bb`](https://github.com/vllm-project/vllm/commit/48f17b77bb) [#60885](https://github.com/vllm-project/vllm/pull/60885)
  [Bugfix] Reject mismatched float16/bfloat16 KV cache dtype (#60885)
  _Files: `tests/test_config.py`, `vllm/config/cache.py`, `vllm/config/vllm.py`_
- **2026-10-15** [`fc8e08a2a6`](https://github.com/vllm-project/vllm/commit/fc8e08a2a6) [#59096](https://github.com/vllm-project/vllm/pull/59096)
  [Bugfix][KV Offload] Do not let mark_miss() flip a pending or in-flight async lookup probe (#59096)
  _Files: `tests/v1/kv_offload/tiering/test_async_lookup.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `vllm/v1/kv_offload/tiering/async_lookup.py`_
- **2026-10-15** [`c5f8adc0b1`](https://github.com/vllm-project/vllm/commit/c5f8adc0b1) [#58168](https://github.com/vllm-project/vllm/pull/58168)
  [KV Offload] Expose OffloadingManager.lock()/unlock() and service the tiering control plane off the scheduler thread (#58168)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_offload/tiering/test_tier_poll_thread.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py` _+11 more__
- **2026-10-15** [`5341b5ba7d`](https://github.com/vllm-project/vllm/commit/5341b5ba7d) [#59544](https://github.com/vllm-project/vllm/pull/59544)
  [KV Offload] Pin only each worker's own offload slots (#59544)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `vllm/v1/kv_offload/cpu/gpu_worker.py`, `vllm/v1/kv_offload/cpu/host_register.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py`_
- **2026-10-15** [`3f1bcfd82b`](https://github.com/vllm-project/vllm/commit/3f1bcfd82b) [#56836](https://github.com/vllm-project/vllm/pull/56836)
  [Bugfix][KV Offload] Bound unanswered P2P lookup waits (#56836)
  _Files: `tests/v1/kv_offload/tiering/p2p/conftest.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/session/client.py` _+2 more__
- **2026-10-14** [`e2aabc8b15`](https://github.com/vllm-project/vllm/commit/e2aabc8b15) [#59790](https://github.com/vllm-project/vllm/pull/59790)
  [Bugfix][KV Offload][P2P] Keep store pins and AbortAck until NIXL transfers stop (#59790)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_data_transport.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/data/base.py`, `vllm/v1/kv_offload/tiering/p2p/data/nixl.py` _+2 more__
- **2026-10-14** [`02653fa22c`](https://github.com/vllm-project/vllm/commit/02653fa22c) [#59140](https://github.com/vllm-project/vllm/pull/59140)
  [Bugfix][KV Offload] Fix inaccurate proportional store dropping (#59140)
  _Files: `tests/v1/kv_offload/tiering/test_backpressure.py`, `vllm/v1/kv_offload/tiering/backpressure.py`_
- **2026-10-14** [`7115b70c01`](https://github.com/vllm-project/vllm/commit/7115b70c01) [#59329](https://github.com/vllm-project/vllm/pull/59329)
  [Bugfix][KV Offload][P2P] Drop a timed-out store job's blocks from the round's parked supply (#59329)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/session/server.py`_
- **2026-10-14** [`a68dbbad05`](https://github.com/vllm-project/vllm/commit/a68dbbad05) [#57500](https://github.com/vllm-project/vllm/pull/57500)
  [Bugfix][KV Offload] Retain offload mappings after unsafe KVCR startup failure (#57500)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `tests/v1/kv_offload/tiering/test_kvcr_tier.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py`, `vllm/v1/kv_offload/tiering/kvcr/manager.py`_
- **2026-10-14** [`775fefa804`](https://github.com/vllm-project/vllm/commit/775fefa804) [#56867](https://github.com/vllm-project/vllm/pull/56867)
  [Metrics][KV Offload] Add vllm:kv_offload_config_info - generic info metrics for offloading the offloading connector (#56867)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_metrics.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_offload/cpu/test_manager.py` _+13 more__
- **2026-10-14** [`c67c69e657`](https://github.com/vllm-project/vllm/commit/c67c69e657) [#47046](https://github.com/vllm-project/vllm/pull/47046)
  [Bugfix][KV Offload] Track allocated block IDs when num_external_tokens is 0 (#47046)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-13** [`483e0c24c7`](https://github.com/vllm-project/vllm/commit/483e0c24c7) [#59545](https://github.com/vllm-project/vllm/pull/59545)
  [KV Offload] Split replicated-layout pre-faulting across workers (#59545)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py`, `vllm/v1/kv_offload/cpu/spec.py`_
- **2026-10-13** [`bc3ddb198a`](https://github.com/vllm-project/vllm/commit/bc3ddb198a) [#60602](https://github.com/vllm-project/vllm/pull/60602)
  [Model][Qwen4Exp] FP8 QSA main KV cache on Ampere (sm_80, sm_86) (#60602)
  _Files: `vllm/models/qwen4_exp/nvidia/ops/qsa.py`, `vllm/models/qwen4_exp/nvidia/qsa.py`_
- **2026-10-12** [`fe341a53dd`](https://github.com/vllm-project/vllm/commit/fe341a53dd) [#60285](https://github.com/vllm-project/vllm/pull/60285)
  [HiSparse] Report host pool in KV cache capacity logs (#60285)
  _Files: `vllm/v1/core/kv_cache_utils.py`_
- **2026-10-12** [`fabaecbfa5`](https://github.com/vllm-project/vllm/commit/fabaecbfa5) [#61181](https://github.com/vllm-project/vllm/pull/61181)
  [Misc] Expand @ZJY0516 CODEOWNERS to Mamba and KV cache (#61181)
  _Files: `.github/CODEOWNERS`_

## Models  (15 commits)

- **2026-10-19** [`ddefe40e16`](https://github.com/vllm-project/vllm/commit/ddefe40e16) [#62199](https://github.com/vllm-project/vllm/pull/62199)
  [Bugfix][Frontend] Match DeepSeek-V4.1 encoder to the 1017 reference encoding (#62199)
  _Files: `tests/tokenizers_/fixtures/deepseek_v41/test_input_1.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_2.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_3.json`, `tests/tokenizers_/fixtures/deepseek_v41/test_input_4.json` _+9 more__
- **2026-10-19** [`2cea893821`](https://github.com/vllm-project/vllm/commit/2cea893821) [#62200](https://github.com/vllm-project/vllm/pull/62200)
  [Bugfix][Rust Frontend] Match DeepSeek-V4.1 renderer to the 1017 reference encoding (#62200)
  _Files: `rust/src/chat/src/renderer/deepseek.rs`, `rust/src/chat/src/renderer/deepseek_v41/tests.rs`_
- **2026-10-19** [`81f7c69577`](https://github.com/vllm-project/vllm/commit/81f7c69577) [#56270](https://github.com/vllm-project/vllm/pull/56270)
  [Bugfix][Tool Calling] Tool parser non-streaming parse drops post-tool-call text that streaming returns (#56270)
  _Files: `tests/tool_parsers/test_deepseekv3_tool_parser.py`, `vllm/tool_parsers/deepseekv3_tool_parser.py`_
- **2026-10-19** [`4e35590dff`](https://github.com/vllm-project/vllm/commit/4e35590dff) [#62303](https://github.com/vllm-project/vllm/pull/62303)
  [Frontend] Serve Gemma 4 on /v1/systemone and /v1/decisions (#62303)
  _Files: `docs/models/structured_decisions_models.md`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `vllm/entrypoints/openai/decisions/strategies.py`_
- **2026-10-17** [`026f6ab268`](https://github.com/vllm-project/vllm/commit/026f6ab268) [#58857](https://github.com/vllm-project/vllm/pull/58857)
  [Model] DeepSeek-V4/V4.1 VL: stream language-model weights instead of sorting the checkpoint (#58857)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_deepseek_v4_vl_stream_weights.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`_
- **2026-10-17** [`5be4266f5c`](https://github.com/vllm-project/vllm/commit/5be4266f5c) [#61947](https://github.com/vllm-project/vllm/pull/61947)
  [Bugfix][Frontend] Preserve Cohere and Anthropic streaming errors (#61947)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/cohere/test_serving_streaming.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/entrypoints/anthropic/serving.py` _+2 more__
- **2026-10-15** [`a9e90b9d1d`](https://github.com/vllm-project/vllm/commit/a9e90b9d1d) [#61825](https://github.com/vllm-project/vllm/pull/61825)
  [Bugfix][Frontend] Reject Cohere REQUIRED tool choice without tools (#61825)
  _Files: `tests/entrypoints/cohere/test_api_router.py`, `tests/entrypoints/cohere/test_protocol.py`, `vllm/entrypoints/cohere/protocol.py`_
- **2026-10-15** [`716c5225ae`](https://github.com/vllm-project/vllm/commit/716c5225ae) [#57963](https://github.com/vllm-project/vllm/pull/57963)
  [Model] Add AliceAI support (#57963)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/models/test_alice_ai.py` _+5 more__
- **2026-10-15** [`ff5a91a456`](https://github.com/vllm-project/vllm/commit/ff5a91a456) [#60759](https://github.com/vllm-project/vllm/pull/60759)
  [Feature][Model Loader] Apply model-owned MTP shard selection to RunAI ModelStreamer (#60759)
  _Files: `docs/models/extensions/runai_model_streamer.md`, `tests/model_executor/model_loader/runai_streamer_loader/test_runai_model_streamer_loader.py`, `tests/models/test_language_model_cache_is_weak.py`, `vllm/model_executor/model_loader/runai_streamer_loader.py` _+2 more__
- **2026-10-14** [`e73fa00981`](https://github.com/vllm-project/vllm/commit/e73fa00981) [#60586](https://github.com/vllm-project/vllm/pull/60586)
  [Bugfix][Frontend] Apply the JSON schema in Cohere Chat v2 response_format (#60586)
  _Files: `tests/entrypoints/cohere/test_serving_conversion.py`, `vllm/entrypoints/cohere/serving.py`_
- **2026-10-14** [`2c74fd1873`](https://github.com/vllm-project/vllm/commit/2c74fd1873) [#61257](https://github.com/vllm-project/vllm/pull/61257)
  [Model Runner V2] Enable batch-sharded sampling for GPT-OSS (#61257)
  _Files: `tests/v1/e2e/general/test_sharded_sampling.py`, `vllm/model_executor/models/gpt_oss.py`_
- **2026-10-13** [`96fc2da315`](https://github.com/vllm-project/vllm/commit/96fc2da315) [#61437](https://github.com/vllm-project/vllm/pull/61437)
  [Perf][Qwen4Exp] Add SM121 TP=2 merged QSA projection plans (#61437)
  _Files: `vllm/models/qwen4_exp/nvidia/low_latency_gemm.py`_
- **2026-10-13** [`d9a543c500`](https://github.com/vllm-project/vllm/commit/d9a543c500) [#61089](https://github.com/vllm-project/vllm/pull/61089)
  [Bugfix][Frontend] Forward --enable-log-outputs to the Cohere Chat v2 (#61089)
  _Files: `vllm/entrypoints/cohere/serving.py`, `vllm/entrypoints/generate/api_router.py`_
- **2026-10-12** [`56e3b081ae`](https://github.com/vllm-project/vllm/commit/56e3b081ae) [#60020](https://github.com/vllm-project/vllm/pull/60020)
  [Bugfix][weight loader] Stop warning when a parameter only widens the weight (#60020)
  _Files: `vllm/model_executor/models/utils.py`_
- **2026-10-12** [`aa1d44df16`](https://github.com/vllm-project/vllm/commit/aa1d44df16) [#60136](https://github.com/vllm-project/vllm/pull/60136)
  [Bugfix][Rust Frontend] Alias `qwen3_xml` to `qwen3_coder` and add `qwen3_json` for the Qwen JSON format (#60136)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs` _+8 more__

## Speculative Decoding  (15 commits)

- **2026-10-19** [`a608b6e6e0`](https://github.com/vllm-project/vllm/commit/a608b6e6e0) [#62206](https://github.com/vllm-project/vllm/pull/62206)
  [Bugfix][Core] Keep the EAGLE-reachable SWA tail at a shared-prefix junction (#62206)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-10-19** [`1641765ffb`](https://github.com/vllm-project/vllm/commit/1641765ffb) [#60553](https://github.com/vllm-project/vllm/pull/60553)
  [Bugfix][Scheduler] Fix encoder cache deadlock with drafter look-ahead (#60553)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/worker/test_encoder_runner.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-19** [`1aa5b6d9fb`](https://github.com/vllm-project/vllm/commit/1aa5b6d9fb) [#61836](https://github.com/vllm-project/vllm/pull/61836)
  [BugFix][MyPy] Guard Linux-only mmap/fadvise calls with sys.platform (#61836)
  _Files: `vllm/model_executor/model_loader/weight_utils.py`, `vllm/models/deepseek_v41/common/engram.py`_
- **2026-10-19** [`ed871c91c7`](https://github.com/vllm-project/vllm/commit/ed871c91c7) [#62269](https://github.com/vllm-project/vllm/pull/62269)
  [Bugfix][DSv4.1] Keep the Engram all-to-all buffers in one allocator (#62269)
  _Files: `vllm/models/deepseek_v41/common/engram.py`_
- **2026-10-18** [`7c9042c05a`](https://github.com/vllm-project/vllm/commit/7c9042c05a) [#62129](https://github.com/vllm-project/vllm/pull/62129)
  [Bugfix][MRV2] Fix speculative warmup deadlock with pipeline parallelism (#62129)
  _Files: `tests/v1/worker/test_gpu_warmup_blocks.py`, `tests/v1/worker/test_mixed_warmup_gate.py`, `vllm/v1/worker/gpu/warmup.py`_
- **2026-10-17** [`0c5dd18e7a`](https://github.com/vllm-project/vllm/commit/0c5dd18e7a) [#62041](https://github.com/vllm-project/vllm/pull/62041)
  [MRV2] Collect KV transfer results before the drafter runs (#62041)
  _Files: `tests/v1/worker/test_gpu_kv_connector.py`, `vllm/v1/worker/gpu/kv_connector.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-10-17** [`763e3f7c91`](https://github.com/vllm-project/vllm/commit/763e3f7c91) [#46399](https://github.com/vllm-project/vllm/pull/46399)
  [Bugfix][Spec Decode] Disable dynamic speculative decoding for fixed-K proposers instead of crashing (#46399)
  _Files: `vllm/config/vllm.py`_
- **2026-10-17** [`c3de0b37e2`](https://github.com/vllm-project/vllm/commit/c3de0b37e2) [#61455](https://github.com/vllm-project/vllm/pull/61455)
  [Core][Spec Decode] Replace EAGLE group heuristics with explicit draft-layer tags (#61455)
  _Files: `tests/v1/core/test_kv_cache_planning.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/spec_decode/test_mtp.py`, `tests/v1/worker/test_attn_utils.py` _+6 more__
- **2026-10-17** [`ad2688ab30`](https://github.com/vllm-project/vllm/commit/ad2688ab30) [#61809](https://github.com/vllm-project/vllm/pull/61809)
  [Bugfix] Validate draft-token capacity in forward benchmark (#61809)
  _Files: `.agents/skills/model-microbenchmark/SKILL.md`, `tests/benchmarks/test_forward_cli.py`, `vllm/benchmarks/forward/main.py`_
- **2026-10-16** [`663e535640`](https://github.com/vllm-project/vllm/commit/663e535640) [#61451](https://github.com/vllm-project/vllm/pull/61451)
  [Perf][Spec Decode] Skip bonus-logit reduction for short drafts in rejection sampling (#61451)
  _Files: `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-10-14** [`21e207efa1`](https://github.com/vllm-project/vllm/commit/21e207efa1) [#61563](https://github.com/vllm-project/vllm/pull/61563)
  [Bugfix][MRV2][Spec Decode] Honor EAGLE3 single-state draft configuration (#61563)
  _Files: `tests/v1/worker/test_eagle3_aux_hidden_states_pp.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/spec_decode/eagle/eagle3_utils.py`_
- **2026-10-14** [`857ddac4e5`](https://github.com/vllm-project/vllm/commit/857ddac4e5) [#61640](https://github.com/vllm-project/vllm/pull/61640)
  [Perf][MRV2] Skip empty draft-token resets on request admission (#61640)
  _Files: `vllm/v1/worker/gpu/states.py`_
- **2026-10-14** [`c1407a7e86`](https://github.com/vllm-project/vllm/commit/c1407a7e86) [#59260](https://github.com/vllm-project/vllm/pull/59260)
  [Spec Decode][MRV2] Warm up top-k/top-p and greedy rejection kernels for speculative decoding (#59260)
  _Files: `tests/v1/worker/test_mixed_warmup_gate.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/warmup.py`_
- **2026-10-14** [`5d88c034f6`](https://github.com/vllm-project/vllm/commit/5d88c034f6) [#61587](https://github.com/vllm-project/vllm/pull/61587)
  [Security] Reject local verifier references in Speculators metadata (#61587)
  _Files: `docs/features/speculative_decoding/speculators.md`, `tests/transformers_utils/test_speculators_override.py`, `vllm/transformers_utils/config.py`_
- **2026-10-12** [`d0948f754d`](https://github.com/vllm-project/vllm/commit/d0948f754d) [#61240](https://github.com/vllm-project/vllm/pull/61240)
  [Bug] Honor spec decode draft model config (#61240)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/v1/worker/gpu/spec_decode/standalone_ar/speculator.py`_

## Perf / Benchmark  (10 commits)

- **2026-10-19** [`dcf8158cdc`](https://github.com/vllm-project/vllm/commit/dcf8158cdc) [#62341](https://github.com/vllm-project/vllm/pull/62341)
  [Bugfix][Benchmark] Don't count content-free chunks as streamed outputs in chat (#62341)
  _Files: `benchmarks/backend_request_func.py`, `tests/benchmarks/test_endpoint_request_func_timing.py`, `vllm/benchmarks/lib/endpoint_request_func.py`_
- **2026-10-17** [`bafb263664`](https://github.com/vllm-project/vllm/commit/bafb263664) [#59888](https://github.com/vllm-project/vllm/pull/59888)
  [Bugfix][Benchmarks] Name the real cause when the /tokenize alignment probe fails (#59888)
  _Files: `vllm/benchmarks/serve.py`_
- **2026-10-17** [`c0b6f74bee`](https://github.com/vllm-project/vllm/commit/c0b6f74bee) [#61692](https://github.com/vllm-project/vllm/pull/61692)
  [Benchmark] Add per-case kernel profiles to vllm bench forward (#61692)
  _Files: `.agents/skills/model-microbenchmark/SKILL.md`, `docs/cli/README.md`, `tests/benchmarks/test_forward_cli.py`, `vllm/benchmarks/forward/capture.py` _+2 more__
- **2026-10-16** [`de7eeaa87b`](https://github.com/vllm-project/vllm/commit/de7eeaa87b) [#61422](https://github.com/vllm-project/vllm/pull/61422)
  [Perf] Share Triton JIT warmup compilation pool across registered kernels (#61422)
  _Files: `tests/model_executor/test_jit_warmup_triton_launcher.py`, `vllm/model_executor/warmup/jit_warmup.py`, `vllm/model_executor/warmup/jit_warmup_triton_helper.py`_
- **2026-10-15** [`19b0efce30`](https://github.com/vllm-project/vllm/commit/19b0efce30) [#61724](https://github.com/vllm-project/vllm/pull/61724)
  [Perf][Core] Skip the null head of sliding-window block tables (#61724)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_single_type_kv_cache_manager.py`, `vllm/v1/core/block_pool.py`, `vllm/v1/core/kv_cache_manager.py` _+2 more__
- **2026-10-15** [`e10c10a644`](https://github.com/vllm-project/vllm/commit/e10c10a644) [#53910](https://github.com/vllm-project/vllm/pull/53910)
  [Core] Add PROMOTION_LATENCY histogram metric for tiering offload (#53910)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/test_metrics.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/base.py` _+2 more__
- **2026-10-15** [`6fe7401fac`](https://github.com/vllm-project/vllm/commit/6fe7401fac) [#61710](https://github.com/vllm-project/vllm/pull/61710)
  [Perf] Read VLLM_COMPUTE_NANS_IN_LOGITS once per IterationStats (#61710)
  _Files: `vllm/v1/metrics/stats.py`_
- **2026-10-15** [`c54dca96bd`](https://github.com/vllm-project/vllm/commit/c54dca96bd) [#60511](https://github.com/vllm-project/vllm/pull/60511)
  [Bugfix][Benchmark] Fix probe latency and duration in bench serve (#60511)
  _Files: `tests/benchmarks/test_serve_cli.py`, `vllm/benchmarks/serve.py`_
- **2026-10-14** [`2e8a5930f6`](https://github.com/vllm-project/vllm/commit/2e8a5930f6) [#61676](https://github.com/vllm-project/vllm/pull/61676)
  [Benchmark] Remove the temporary bench forward dummy loader (#61676)
  _Files: `.agents/skills/model-microbenchmark/SKILL.md`, `tests/benchmarks/test_forward_cli.py`, `vllm/benchmarks/forward/capture.py`, `vllm/benchmarks/forward/main.py`_
- **2026-10-14** [`02d69c663a`](https://github.com/vllm-project/vllm/commit/02d69c663a) [#51172](https://github.com/vllm-project/vllm/pull/51172)
  [Bugfix][Benchmark] Preserve SSE output across transport chunk boundaries (#51172)
  _Files: `tests/benchmarks/test_endpoint_request_func_timing.py`, `vllm/benchmarks/lib/endpoint_request_func.py`_

## Docs  (9 commits)

- **2026-10-19** [`2aa5080fa0`](https://github.com/vllm-project/vllm/commit/2aa5080fa0) [#60994](https://github.com/vllm-project/vllm/pull/60994)
  [Bugfix][Weight Cache] Include RoPE parameters in IPC cache key (#60994)
  _Files: `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py` _+1 more__
- **2026-10-19** [`3497d72a72`](https://github.com/vllm-project/vllm/commit/3497d72a72) [#62207](https://github.com/vllm-project/vllm/pull/62207)
  [Frontend] Add Muse Spark Open reasoning and tool parsers (#62207)
  _Files: `docs/features/tool_calling.md`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/unified.rs`, `rust/src/parser/src/unified/mod.rs` _+10 more__
- **2026-10-18** [`fe8f2140ee`](https://github.com/vllm-project/vllm/commit/fe8f2140ee) [#62305](https://github.com/vllm-project/vllm/pull/62305)
  [Doc] Document /inference/v1/generate request/response fields and DP rank header (#62305)
  _Files: `docs/serving/online_serving/token_in_token_out.md`, `docs/training/sampling_mask.md`, `examples/scale_out/token_generation_client.py`_
- **2026-10-18** [`2365177ddd`](https://github.com/vllm-project/vllm/commit/2365177ddd) [#62267](https://github.com/vllm-project/vllm/pull/62267)
  [Doc][RL] Document the weight-transfer HTTP protocol for trainers without vLLM (#62267)
  _Files: `docs/training/weight_transfer/README.md`, `docs/training/weight_transfer/ipc.md`, `docs/training/weight_transfer/nccl.md`, `examples/rl/rlhf_http_ipc_no_vllm.py` _+2 more__
- **2026-10-17** [`b515648641`](https://github.com/vllm-project/vllm/commit/b515648641) [#61302](https://github.com/vllm-project/vllm/pull/61302)
  [Doc] Host model recipes in recipes/ (#61302)
- **2026-10-16** [`024c5188bf`](https://github.com/vllm-project/vllm/commit/024c5188bf) [#60437](https://github.com/vllm-project/vllm/pull/60437)
  [Frontend] Resolve logprobs on the parsed streaming derender path (#60437)
  _Files: `docs/serving/online_serving/derenderer.md`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_parity.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py` _+2 more__
- **2026-10-14** [`6ecb39eaa7`](https://github.com/vllm-project/vllm/commit/6ecb39eaa7) [#61588](https://github.com/vllm-project/vllm/pull/61588)
  [Docs] Update structured decisions docs. (#61588)
  _Files: `docs/.nav.yml`, `docs/models/structured_decisions_models.md`, `docs/serving/online_serving/README.md`, `docs/serving/online_serving/decisions.md` _+1 more__
- **2026-10-12** [`69d54eb078`](https://github.com/vllm-project/vllm/commit/69d54eb078) [#61022](https://github.com/vllm-project/vllm/pull/61022)
  [Docs] Fix broken llm-d.ai links on the llm-d integration page (#61022)
  _Files: `docs/deployment/integrations/llm-d.md`_
- **2026-10-12** [`2534a96fcf`](https://github.com/vllm-project/vllm/commit/2534a96fcf) [#61081](https://github.com/vllm-project/vllm/pull/61081)
  [Docs] List additional unauthenticated endpoints (#61081)
  _Files: `docs/usage/security.md`_

## LoRA  (8 commits)

- **2026-10-19** [`37891a98ea`](https://github.com/vllm-project/vllm/commit/37891a98ea) [#61884](https://github.com/vllm-project/vllm/pull/61884)
  [Bugfix] Reject LoRA at config time for models without SupportsLoRA (#61884)
  _Files: `tests/test_config.py`, `vllm/config/lora.py`, `vllm/config/model.py`, `vllm/model_executor/models/mamba2.py` _+2 more__
- **2026-10-19** [`83db1ab496`](https://github.com/vllm-project/vllm/commit/83db1ab496) [#61618](https://github.com/vllm-project/vllm/pull/61618)
  [Bugfix][LoRA] Keep failed activations retryable (#61618)
  _Files: `vllm/lora/model_manager.py`_
- **2026-10-16** [`523d74e2ac`](https://github.com/vllm-project/vllm/commit/523d74e2ac) [#61906](https://github.com/vllm-project/vllm/pull/61906)
  [Bugfix][LoRA] Fix garbage/NaN lora_expand output on SM90 with fp32 i… (#61906)
  _Files: `vllm/lora/ops/triton_ops/lora_expand_op.py`_
- **2026-10-16** [`ae8f41238c`](https://github.com/vllm-project/vllm/commit/ae8f41238c) [#61857](https://github.com/vllm-project/vllm/pull/61857)
  [Bugfix][Parser] Honor a prompt-closed reasoning block in non-streaming parse and reasoning token counts (#61857)
  _Files: `tests/parser/engine/test_qwen3_reasoning.py`, `tests/parser/test_parse.py`, `vllm/parser/abstract_parser.py`, `vllm/parser/engine/adapters.py` _+2 more__
- **2026-10-16** [`4ac1f8d2ac`](https://github.com/vllm-project/vllm/commit/4ac1f8d2ac) [#61574](https://github.com/vllm-project/vllm/pull/61574)
  [Bugfix][Structured Output] Mask grammar-invalid implicit reasoning ends (#61574)
  _Files: `tests/parser/engine/test_parser_engine.py`, `tests/v1/spec_decode/test_mtp_structured_output.py`, `tests/v1/structured_output/test_structured_output_manager.py`, `vllm/parser/engine/adapters.py` _+3 more__
- **2026-10-13** [`c923e7769b`](https://github.com/vllm-project/vllm/commit/c923e7769b) [#60465](https://github.com/vllm-project/vllm/pull/60465)
  [Feat] Add text-only OpenAI Decisions API MVP (#60465)
  _Files: `docs/serving/online_serving/README.md`, `docs/serving/online_serving/decisions.md`, `docs/usage/security.md`, `tests/entrypoints/generate/generative_scoring/test_generative_scoring.py` _+19 more__
- **2026-10-12** [`f3cb10b690`](https://github.com/vllm-project/vllm/commit/f3cb10b690) [#61033](https://github.com/vllm-project/vllm/pull/61033)
  [Model][LoRA] Enable LoRA support for BERT and RoBERTa embedding models (#61033)
  _Files: `docs/models/pooling_models/embed.md`, `vllm/model_executor/models/bert.py`_
- **2026-10-12** [`4c36d21280`](https://github.com/vllm-project/vllm/commit/4c36d21280) [#59801](https://github.com/vllm-project/vllm/pull/59801)
  [Bugfix][LoRA] Apply PEFT rank_pattern / alpha_pattern scaling per module (#59801)
  _Files: `tests/lora/test_lora_weights.py`, `tests/lora/test_peft_helper.py`, `vllm/lora/lora_model.py`, `vllm/lora/lora_weights.py` _+1 more__

## Compilation / CUDA Graph  (4 commits)

- **2026-10-19** [`3788269c98`](https://github.com/vllm-project/vllm/commit/3788269c98) [#62375](https://github.com/vllm-project/vllm/pull/62375)
  [Benchmark][XPU] Support XPU in forward bench graph capture/profiling (#62375)
  _Files: `vllm/benchmarks/forward/capture.py`, `vllm/benchmarks/forward/profile.py`, `vllm/profiler/wrapper.py`_
- **2026-10-15** [`96b5b0ee4b`](https://github.com/vllm-project/vllm/commit/96b5b0ee4b) [#61572](https://github.com/vllm-project/vllm/pull/61572)
  [Model] Enable torch.compile and CUDA graphs for EmbeddingGemma2 (#61572)
  _Files: `vllm/model_executor/models/embedding_gemma2.py`_
- **2026-10-14** [`3723a1ea96`](https://github.com/vllm-project/vllm/commit/3723a1ea96) [#58064](https://github.com/vllm-project/vllm/pull/58064)
  [Bugfix][Transformers backend] Fix CUDA graph capture for dynamic-rope models (#58064)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/transformers/test_dynamic_rope.py`, `vllm/model_executor/models/transformers/base.py`, `vllm/model_executor/models/transformers/utils.py`_
- **2026-10-13** [`877f6df889`](https://github.com/vllm-project/vllm/commit/877f6df889) [#59709](https://github.com/vllm-project/vllm/pull/59709)
  [Bugfix][DSv4] Don't bake the C128 compressor skip into CUDA graphs (#59709)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `vllm/models/deepseek_v4/compressor.py`_

---
_Generated 2026-10-19 15:37 UTC_