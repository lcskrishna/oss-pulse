# vllm-project/vllm — Weekly Change Report
**Period:** 2026-09-07 → 2026-09-14  |  **Total commits:** 389

## ✨ New Features This Week

- **2026-09-14** [#56722](https://github.com/vllm-project/vllm/pull/56722) — [PCP][DCP] Declare FlashMLASparse MTP support at CP interleave > 1 (#56722)
- **2026-09-14** [#53721](https://github.com/vllm-project/vllm/pull/53721) — [ROCm][Connector] SWA+HMA-support in MoRI-IO connector (Gemma4) (#53721)
- **2026-09-14** [#54934](https://github.com/vllm-project/vllm/pull/54934) — [CI][CPU] Add speculative-decoding coverage to CPU CI (#54934)
- **2026-09-14** [#51794](https://github.com/vllm-project/vllm/pull/51794) — [ROCm][Perf] Enable CSA multi-stream overlap for DeepSeek-V4 (#51794)
- **2026-09-14** [#55176](https://github.com/vllm-project/vllm/pull/55176) — [Frontend] Replace `VLLM_ENABLE_SCALE_OUT_ENDPOINTS` with `--enable-scale-out` (#55176)
- **2026-09-14** [#48498](https://github.com/vllm-project/vllm/pull/48498) — [Performance] Add Triton kernel for Gemma3n sparse GELU (#48498)
- **2026-09-14** [#56567](https://github.com/vllm-project/vllm/pull/56567) — [Rust Frontend] Support HTTP RL weight synchronization (#56567)
- **2026-09-14** [#55468](https://github.com/vllm-project/vllm/pull/55468) — [Fast Start] Fast loader support nnode>1 (#55468)
- **2026-09-13** [#55897](https://github.com/vllm-project/vllm/pull/55897) — [LoRA] Add LoRA support for DeepSeek-V4 Flash Vision (#55897)
- **2026-09-13** [#56512](https://github.com/vllm-project/vllm/pull/56512) — [DS V4.1][Engram] Support async prefetch for offloaded engram lookups and engram DP sharding (#56512)
- _…and 68 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-14** [`1d0d1081c4`](https://github.com/vllm-project/vllm/commit/1d0d1081c4) [#53721](https://github.com/vllm-project/vllm/pull/53721) — [ROCm][Connector] SWA+HMA-support in MoRI-IO connector (Gemma4) (#53721)
- **2026-09-14** [`a6c5d6d0fc`](https://github.com/vllm-project/vllm/commit/a6c5d6d0fc) [#51794](https://github.com/vllm-project/vllm/pull/51794) — [ROCm][Perf] Enable CSA multi-stream overlap for DeepSeek-V4 (#51794)
- **2026-09-14** [`dc2e8f1157`](https://github.com/vllm-project/vllm/commit/dc2e8f1157) [#54965](https://github.com/vllm-project/vllm/pull/54965) — [ROCm][Perf] W4A16: keep skinny GEMM zero-points packed 4-bit (#54965)
- **2026-09-14** [`23cfaad497`](https://github.com/vllm-project/vllm/commit/23cfaad497) [#56763](https://github.com/vllm-project/vllm/pull/56763) — [CI] Update entrypoints CI (#56763)
- **2026-09-14** [`78e84261ab`](https://github.com/vllm-project/vllm/commit/78e84261ab) [#48498](https://github.com/vllm-project/vllm/pull/48498) — [Performance] Add Triton kernel for Gemma3n sparse GELU (#48498)
- **2026-09-14** [`cf1584f373`](https://github.com/vllm-project/vllm/commit/cf1584f373) [#56741](https://github.com/vllm-project/vllm/pull/56741) — [Refactor] Normalize DeepSeek V4.1 model package naming (#56741)
- **2026-09-14** [`dfa1984e58`](https://github.com/vllm-project/vllm/commit/dfa1984e58) [#55235](https://github.com/vllm-project/vllm/pull/55235) — [ROCm][Perf] Tune MiniMax-M3 decode top-k for short contexts (#55235)
- **2026-09-13** [`f09c52a587`](https://github.com/vllm-project/vllm/commit/f09c52a587) [#56170](https://github.com/vllm-project/vllm/pull/56170) — [ROCm][Performance] Avoid blocking MiniMax M3 scalar upload (#56170)
- **2026-09-13** [`c711f740b7`](https://github.com/vllm-project/vllm/commit/c711f740b7) [#56349](https://github.com/vllm-project/vllm/pull/56349) — [ROCm] Auto-enable breakable CUDA graphs for DeepseekV41ForCausalLM (#56349)
- **2026-09-12** [`72d4d83157`](https://github.com/vllm-project/vllm/commit/72d4d83157) [#56610](https://github.com/vllm-project/vllm/pull/56610) — [ROCm][Bugfix] Fix elastic EP scaling deadlock (#56610)
- **2026-09-12** [`2f59050eda`](https://github.com/vllm-project/vllm/commit/2f59050eda) [#56555](https://github.com/vllm-project/vllm/pull/56555) — [XPU][CI] Skip ROCm test on non-ROCm platforms (#56555)
- **2026-09-12** [`986e2f870a`](https://github.com/vllm-project/vllm/commit/986e2f870a) [#55522](https://github.com/vllm-project/vllm/pull/55522) — [Refactor][ROCm] Migrate the RDNA3 W4A16 MoE to the oracle/experts pa… (#55522)
- **2026-09-12** [`756794a9a7`](https://github.com/vllm-project/vllm/commit/756794a9a7) [#56392](https://github.com/vllm-project/vllm/pull/56392) — [Frontend] create unified Cohere parser (#56392)
- **2026-09-12** [`d406f09eb8`](https://github.com/vllm-project/vllm/commit/d406f09eb8) [#55252](https://github.com/vllm-project/vllm/pull/55252) — [ROCm][CI] Stage F gating (#55252)
- **2026-09-12** [`30118ba27d`](https://github.com/vllm-project/vllm/commit/30118ba27d) [#56554](https://github.com/vllm-project/vllm/pull/56554) — [DSV4.1] Remove compressor-aware image sentinel token padding (#56554)
- **2026-09-12** [`06e57f622c`](https://github.com/vllm-project/vllm/commit/06e57f622c) [#56526](https://github.com/vllm-project/vllm/pull/56526) — [ROCm][Kimi-K3] Fix non-contiguous state_indices crash and GPU-sync assert in fused KDA/MLA prefill (#56526)
- **2026-09-12** [`46d2b23ac5`](https://github.com/vllm-project/vllm/commit/46d2b23ac5) [#56503](https://github.com/vllm-project/vllm/pull/56503) — [ROCm][DSV4.1][Perf] Use AITER mHC for the delayed pre block (#56503)
- **2026-09-11** [`bbaa1b9340`](https://github.com/vllm-project/vllm/commit/bbaa1b9340) [#56522](https://github.com/vllm-project/vllm/pull/56522) — [ROCm][CI] Extend timeout for `Basic Models (other)` (#56522)
- **2026-09-11** [`2d75e586fc`](https://github.com/vllm-project/vllm/commit/2d75e586fc) [#56153](https://github.com/vllm-project/vllm/pull/56153) — [ROCm][Kernel][DSV4] Remove tl.constexpr to avoid cold-compile churn in indexer gather kernel (#56153)
- **2026-09-11** [`dc07f1638f`](https://github.com/vllm-project/vllm/commit/dc07f1638f) [#56160](https://github.com/vllm-project/vllm/pull/56160) — [Bugfix][MLA] Read sparse model settings from text config (#56160)
- **2026-09-11** [`6fe67cbbf3`](https://github.com/vllm-project/vllm/commit/6fe67cbbf3) [#46994](https://github.com/vllm-project/vllm/pull/46994) — [Spec][V2] Support MTP speculative decoding under pipeline parallelism (#46994)
- **2026-09-11** [`9dd969da09`](https://github.com/vllm-project/vllm/commit/9dd969da09) [#55107](https://github.com/vllm-project/vllm/pull/55107) — [Model][ROCm] Enable DeepSeek V4 Vision (#55107)
- **2026-09-11** [`127143e27f`](https://github.com/vllm-project/vllm/commit/127143e27f) [#53664](https://github.com/vllm-project/vllm/pull/53664) — Revert "[Rocm][Kimi-k3] Fix pipeline_parallel support for the kimik3 DCP mode  (#53664)" (#56429)
- **2026-09-11** [`b87339888d`](https://github.com/vllm-project/vllm/commit/b87339888d) [#56460](https://github.com/vllm-project/vllm/pull/56460) — [httpx migration] Import httpx from huggingface_hub (#56460)
- **2026-09-11** [`5fe77aecfc`](https://github.com/vllm-project/vllm/commit/5fe77aecfc) [#55353](https://github.com/vllm-project/vllm/pull/55353) — [Deprecation] Deprecate items scheduled for 0.29 (#55353)
- **2026-09-11** [`5392fbca2a`](https://github.com/vllm-project/vllm/commit/5392fbca2a) [#56459](https://github.com/vllm-project/vllm/pull/56459) — [ROCm][Docker] Pin AINIC apt repo to snapshot 1.117.5-a-77 (#56459)
- **2026-09-11** [`b4da4d17ae`](https://github.com/vllm-project/vllm/commit/b4da4d17ae) [#56433](https://github.com/vllm-project/vllm/pull/56433) — [ROCm][Bugfix] Fix AITER preshuffled FP8 block-scale kernel (#56433)
- **2026-09-11** [`eb7e894432`](https://github.com/vllm-project/vllm/commit/eb7e894432) [#55667](https://github.com/vllm-project/vllm/pull/55667) — [ROCm][CI] Add HY-V4 generation coverage (#55667)
- **2026-09-11** [`e77daef89e`](https://github.com/vllm-project/vllm/commit/e77daef89e) [#56214](https://github.com/vllm-project/vllm/pull/56214) — [Model] Support DeepSeek-V4.1-Flash (#56214)
- **2026-09-11** [`d0dfe587d5`](https://github.com/vllm-project/vllm/commit/d0dfe587d5) [#55095](https://github.com/vllm-project/vllm/pull/55095) — [Bugfix] Fall back to full decode graphs for noncompiled models (#55095)
- **2026-09-11** [`a9271c750f`](https://github.com/vllm-project/vllm/commit/a9271c750f) [#56356](https://github.com/vllm-project/vllm/pull/56356) — [ROCm][CI] Accept `base-v2-preview` images during content hash lookup for ROCm base images (#56356)
- **2026-09-11** [`ae48466cf3`](https://github.com/vllm-project/vllm/commit/ae48466cf3) [#48247](https://github.com/vllm-project/vllm/pull/48247) — [Perf][ROCm] Add AITER custom AG/RS (DP only) (#48247)
- **2026-09-11** [`828f4f19b4`](https://github.com/vllm-project/vllm/commit/828f4f19b4) [#55239](https://github.com/vllm-project/vllm/pull/55239) — [ROCm][Bugfix] Route GLM-5.3-Flash MTP through ragged sparse MLA (#55239)
- **2026-09-10** [`9163190dda`](https://github.com/vllm-project/vllm/commit/9163190dda) [#56098](https://github.com/vllm-project/vllm/pull/56098) — [ROCm][Bugfix][Perf] Tune multi-stream shared experts use; wvSplitKrc fixes (#56098)
- **2026-09-10** [`7de70fa7ae`](https://github.com/vllm-project/vllm/commit/7de70fa7ae) [#56161](https://github.com/vllm-project/vllm/pull/56161) — [Bugfix][ROCm] Create linear layer biases with `requires_grad=False` (#56161)
- **2026-09-10** [`48cb12c184`](https://github.com/vllm-project/vllm/commit/48cb12c184) [#56190](https://github.com/vllm-project/vllm/pull/56190) — [ROCm][Bugfix] Fix profiler in TheRock image (#56190)
- **2026-09-10** [`8359e15aae`](https://github.com/vllm-project/vllm/commit/8359e15aae) [#53695](https://github.com/vllm-project/vllm/pull/53695) — [ROCm][Feature] Support KV connectors with ROCM_AITER_UNIFIED_ATTN (#53695)
- **2026-09-10** [`7470082f57`](https://github.com/vllm-project/vllm/commit/7470082f57) [#51692](https://github.com/vllm-project/vllm/pull/51692) — [ROCm][Perf] Add bpreshuffled blockscaled fp8 GEMM (#51692)
- **2026-09-10** [`9b959b8657`](https://github.com/vllm-project/vllm/commit/9b959b8657) [#56228](https://github.com/vllm-project/vllm/pull/56228) — [Model] DeepSeek-V4.1-Flash Model Definitions (#56228)
- **2026-09-10** [`6ff479e1f7`](https://github.com/vllm-project/vllm/commit/6ff479e1f7) [#55236](https://github.com/vllm-project/vllm/pull/55236) — [ROCm] Add better kv dtype error discoverability (#55236)
- **2026-09-10** [`9521c60bdc`](https://github.com/vllm-project/vllm/commit/9521c60bdc) [#54038](https://github.com/vllm-project/vllm/pull/54038) — [ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill reland (#54038)
- **2026-09-10** [`7e91760650`](https://github.com/vllm-project/vllm/commit/7e91760650) [#54855](https://github.com/vllm-project/vllm/pull/54855) — [ROCm][Perf] Route large DSV4 sparse prefill to AITER OPUS (#54855)
- **2026-09-10** [`49632fb3ac`](https://github.com/vllm-project/vllm/commit/49632fb3ac) [#56010](https://github.com/vllm-project/vllm/pull/56010) — [CI][XPU] Reject CUDA-IPC weight cache on non-CUDA/ROCm platforms (#56010)
- **2026-09-10** [`588a813a60`](https://github.com/vllm-project/vllm/commit/588a813a60) [#55213](https://github.com/vllm-project/vllm/pull/55213) — [ROCm] [BugFix] Fix AITER MXFP4 ASM-GEMM crash on unfused shared experts (#55213)
- **2026-09-10** [`2a02f6efe3`](https://github.com/vllm-project/vllm/commit/2a02f6efe3) [#53885](https://github.com/vllm-project/vllm/pull/53885) — [CI][ROCm][Disagg] Add GLM-5.2-FP8 to MoRIIO model catalog (#53885)
- **2026-09-09** [`83252ea899`](https://github.com/vllm-project/vllm/commit/83252ea899) [#52664](https://github.com/vllm-project/vllm/pull/52664) — [Performance][ROCm]  Integrate aiter indexer scoring and top-k kernels into MiniMax-M3 sparse attention path (#52664)
- **2026-09-09** [`6983a0883d`](https://github.com/vllm-project/vllm/commit/6983a0883d) [#53602](https://github.com/vllm-project/vllm/pull/53602) — [ROCm][CI] Split MI300 Distributed Compile by graph partition mode (#53602)
- **2026-09-09** [`dcd544486b`](https://github.com/vllm-project/vllm/commit/dcd544486b) [#55887](https://github.com/vllm-project/vllm/pull/55887) — [ROCm][Bugfix] Support shared KV prefill in AITER attention (#55887)
- **2026-09-09** [`cce50657b7`](https://github.com/vllm-project/vllm/commit/cce50657b7) [#56130](https://github.com/vllm-project/vllm/pull/56130) — [ROCm][CI] Use a platform-independent GEMM in the merged-column fuser test (#56130)
- **2026-09-09** [`c69d5d72a6`](https://github.com/vllm-project/vllm/commit/c69d5d72a6) [#56114](https://github.com/vllm-project/vllm/pull/56114) — [CI][ROCm] Increase timeout for AMD MI355 Language Models (Standard) (#56114)
- **2026-09-09** [`3fb676bfad`](https://github.com/vllm-project/vllm/commit/3fb676bfad) [#56106](https://github.com/vllm-project/vllm/pull/56106) — [ROCm][CI] Fix moe layer tests for fp8 dtype compatibility (#56106)
- **2026-09-09** [`1454b71727`](https://github.com/vllm-project/vllm/commit/1454b71727) [#53590](https://github.com/vllm-project/vllm/pull/53590) — Fix ROCm AITER FP8 KV test tolerances. (#53590)
- **2026-09-09** [`d8d53f17c2`](https://github.com/vllm-project/vllm/commit/d8d53f17c2) [#53664](https://github.com/vllm-project/vllm/pull/53664) — [Rocm][Kimi-k3] Add pipeline_parallel support for the kimik3 model (#53664)
- **2026-09-09** [`4e990dfcec`](https://github.com/vllm-project/vllm/commit/4e990dfcec) [#55968](https://github.com/vllm-project/vllm/pull/55968) — [ROCm] Bump AITER to v0.1.21.post2 (#55968)
- **2026-09-09** [`62f3bf58a5`](https://github.com/vllm-project/vllm/commit/62f3bf58a5) [#56035](https://github.com/vllm-project/vllm/pull/56035) — [Bugfix][ROCm][DSv4] Skip launch_pdl=True JIT warmup when PDL is unsupported (#56035)
- **2026-09-09** [`08b3e67b66`](https://github.com/vllm-project/vllm/commit/08b3e67b66) [#45900](https://github.com/vllm-project/vllm/pull/45900) — [ROCm][Perf] Fix Qwen3-vLLM audio encoder TP when heads are not divisible by TP size (#45900)
- **2026-09-09** [`bc8587f829`](https://github.com/vllm-project/vllm/commit/bc8587f829) [#55099](https://github.com/vllm-project/vllm/pull/55099) — [ROCm][Perf][Bugfix] Multi-stream perf improvements; rocprofiler fixes (#55099)
- **2026-09-08** [`60ad959b6f`](https://github.com/vllm-project/vllm/commit/60ad959b6f) [#55513](https://github.com/vllm-project/vllm/pull/55513) — Fix block FP8 MTP in ModelOpt mixed checkpoints (#55513)
- **2026-09-08** [`28a2ccee78`](https://github.com/vllm-project/vllm/commit/28a2ccee78) [#53195](https://github.com/vllm-project/vllm/pull/53195) — [ROCm][DI][CI] Enable WideEP Intranode tests  (#53195)
- **2026-09-08** [`73f61d12aa`](https://github.com/vllm-project/vllm/commit/73f61d12aa) [#55919](https://github.com/vllm-project/vllm/pull/55919) — [CI][ROCm] Increase timeouts for AMD MI300 jobs (#55919)
- **2026-09-08** [`db3814a4f2`](https://github.com/vllm-project/vllm/commit/db3814a4f2) [#55780](https://github.com/vllm-project/vllm/pull/55780) — [Attention] Require explicit DCP support from attention implementations (#55780)
- **2026-09-08** [`2c9d68f80b`](https://github.com/vllm-project/vllm/commit/2c9d68f80b) [#54809](https://github.com/vllm-project/vllm/pull/54809) — [Quant][Kernel] Remove GPTQ Group/Dynamic Activation Ordering (#54809)
- **2026-09-08** [`1a522b6949`](https://github.com/vllm-project/vllm/commit/1a522b6949) [#54112](https://github.com/vllm-project/vllm/pull/54112) — [ROCm] [Docker] Upgrade default AINIC repo to ship libionic 54.0-187-1 (#54112)
- **2026-09-08** [`7c2f1ff495`](https://github.com/vllm-project/vllm/commit/7c2f1ff495) [#54523](https://github.com/vllm-project/vllm/pull/54523) — [Core] Scope PCP-DP validation to GPU manager (#54523)
- **2026-09-08** [`6ddbab03de`](https://github.com/vllm-project/vllm/commit/6ddbab03de) [#50176](https://github.com/vllm-project/vllm/pull/50176) — [4/N][warmup][DSv4] Migrate common attention kernels (#50176)
- **2026-09-08** [`25047604fe`](https://github.com/vllm-project/vllm/commit/25047604fe) [#55808](https://github.com/vllm-project/vllm/pull/55808) — [ROCm][Perf] Remove AITER paged-MQA outputs guard for DeepSeek-V4 (#55808)
- **2026-09-08** [`e41a17e606`](https://github.com/vllm-project/vllm/commit/e41a17e606) [#52263](https://github.com/vllm-project/vllm/pull/52263) — [ROCm][Quantization] Support AMD Quark per-block FP8 for fused MoE layers (#52263)
- **2026-09-08** [`ce6c241ddc`](https://github.com/vllm-project/vllm/commit/ce6c241ddc) [#54787](https://github.com/vllm-project/vllm/pull/54787) — [ROCm][Perf][M3] Fused allreduce+GemmaRMSNorm fast path (#54787)
- **2026-09-08** [`755541443f`](https://github.com/vllm-project/vllm/commit/755541443f) [#53856](https://github.com/vllm-project/vllm/pull/53856) — [Bugfix][ROCm] Mask paged attention V cache padding (#53856)
- **2026-09-08** [`6b5a12c0f8`](https://github.com/vllm-project/vllm/commit/6b5a12c0f8) [#54405](https://github.com/vllm-project/vllm/pull/54405) — [ROCm][CI] Enable HY-V4 model initialization on ROCm (#54405)
- **2026-09-07** [`537af2c3a4`](https://github.com/vllm-project/vllm/commit/537af2c3a4) [#55454](https://github.com/vllm-project/vllm/pull/55454) — [CI] Recover empty multi-node Docker networks and finish partial cleanup (#55454)
- **2026-09-07** [`e476556189`](https://github.com/vllm-project/vllm/commit/e476556189) [#54404](https://github.com/vllm-project/vllm/pull/54404) — [ROCm][CI] Add attention-sink support to ROCm AITER sparse MLA (#54404)
- **2026-09-07** [`195bc9c4a1`](https://github.com/vllm-project/vllm/commit/195bc9c4a1) [#55653](https://github.com/vllm-project/vllm/pull/55653) — [CI][ROCm] Temporarily skip unsupported HY-V4 initialization (#55653)
- **2026-09-07** [`1f778486fc`](https://github.com/vllm-project/vllm/commit/1f778486fc) [#54975](https://github.com/vllm-project/vllm/pull/54975) — [Bugfix][Offloader] Preserve prefetch static-buffer slot ownership (#54975)
- **2026-09-07** [`de69e821b7`](https://github.com/vllm-project/vllm/commit/de69e821b7) [#53161](https://github.com/vllm-project/vllm/pull/53161) — [ROCm][Perf][DeepSeek V4] Fuse native FP8 shared expert with MXFP4 routed experts (#53161)
- **2026-09-07** [`199cb9b964`](https://github.com/vllm-project/vllm/commit/199cb9b964) [#55535](https://github.com/vllm-project/vllm/pull/55535) — [Kernel] Remove unused fake implementation (#55535)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#56830](https://github.com/vllm-project/vllm/issues/56830) | [Bug]: Startup memory-profiling assertion aborts whenever free memory  | bug | 2026-09-14 |
| [#52911](https://github.com/vllm-project/vllm/issues/52911) | [RFC]: DeepSeek-V4 Performance Optimization on ROCm (Phase Two) | rocm, RFC, deepseek, DSv4 | 2026-09-14 |
| [#54363](https://github.com/vllm-project/vllm/issues/54363) | [RFC]: Data integrity and I/O liveness for the filesystem KV offload t | RFC | 2026-09-14 |
| [#56815](https://github.com/vllm-project/vllm/issues/56815) | [Bug]: Engram async prefetch (#56512) reintroduces silent ctx-load dec | bug, quantization | 2026-09-14 |
| [#56832](https://github.com/vllm-project/vllm/issues/56832) | [Bug]: --moe-backend marlin is applied to the unquantized MTP draft Mo | quantization | 2026-09-14 |
| [#56829](https://github.com/vllm-project/vllm/issues/56829) | [Bug]: cu129-nightly image ships torch 2.14.0+cu130 with cu129 torchvi | — | 2026-09-14 |
| [#56605](https://github.com/vllm-project/vllm/issues/56605) | [Bug]: GLM-5.3-Flash degenerates into repeated-token "word salad" in m | bug, glm | 2026-09-14 |
| [#56797](https://github.com/vllm-project/vllm/issues/56797) | [Perf][Spec Decode] DeepSeek-V4.1-Flash DSpark mean acceptance length  | bug, deepseek, DSv4.1 | 2026-09-14 |
| [#48255](https://github.com/vllm-project/vllm/issues/48255) | [Tracking][ROCm][Perf]: DP Attention performance | feature request, rocm | 2026-09-14 |
| [#44219](https://github.com/vllm-project/vllm/issues/44219) | [RFC]: hardware agnostic model definitions in vLLM | RFC | 2026-09-14 |
| [#56699](https://github.com/vllm-project/vllm/issues/56699) | [Bug][HiSparse] Decode engine dies with cudaErrorLaunchFailure in the  | — | 2026-09-14 |
| [#56785](https://github.com/vllm-project/vllm/issues/56785) | [Bug]: HiSparse MLA indexer crashes with CUDA error: invalid argument  | — | 2026-09-14 |
| [#56443](https://github.com/vllm-project/vllm/issues/56443) | [Bug]: DeepSeek-V4.1-Flash + DSpark spec decode hits CUDA device-side  | deepseek, DSv4 | 2026-09-14 |
| [#55626](https://github.com/vllm-project/vllm/issues/55626) | [Bug]: GLM-5.3-Flash: CUDA illegal memory access in FlashInfer SM90 sp | bug, rocm, glm | 2026-09-14 |
| [#54437](https://github.com/vllm-project/vllm/issues/54437) | [Bug]: structured output can sample unconstrained tokens when the draf | structured-output | 2026-09-14 |
| [#54775](https://github.com/vllm-project/vllm/issues/54775) | [Bug]: KDA/gated-delta-rule chunked-scan buffers are outside memory pr | rocm | 2026-09-14 |
| [#56792](https://github.com/vllm-project/vllm/issues/56792) | DSpark checkpoints exported in fill-in (DFlash 1+N) layout silently se | — | 2026-09-14 |
| [#55434](https://github.com/vllm-project/vllm/issues/55434) | [Performance]: GLM-5.3 P/D on GB200 — NIXL issues up to ~112k KV descr | kv-connector, glm | 2026-09-14 |
| [#52225](https://github.com/vllm-project/vllm/issues/52225) | [Bug]: Recurring Xid 13 chip-wide warp errors (misaligned address / il | bug, rocm | 2026-09-14 |
| [#56770](https://github.com/vllm-project/vllm/issues/56770) | [Bug]: compressed-tensors MXFP4 W4A16 is misclassified as W4A4 and dis | bug, quantization | 2026-09-14 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 76 |
| Attention | 53 |
| Multimodal | 34 |
| Other | 31 |
| MoE / Expert Parallel | 27 |
| Disaggregation / PD | 26 |
| CI / Build | 25 |
| Serving / API | 22 |
| Quantization | 20 |
| Models | 19 |
| Speculative Decoding | 12 |
| Scheduler / Engine | 12 |
| Docs | 9 |
| LoRA | 7 |
| Perf / Benchmark | 7 |
| KV Cache / Offload | 5 |
| Compilation / CUDA Graph | 4 |

## ROCm / AMD  (76 commits)

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
- **2026-09-13** [`f09c52a587`](https://github.com/vllm-project/vllm/commit/f09c52a587) [#56170](https://github.com/vllm-project/vllm/pull/56170)
  [ROCm][Performance] Avoid blocking MiniMax M3 scalar upload (#56170)
  _Files: `vllm/models/minimax_m3/common/sparse_attention.py`_
- **2026-09-13** [`c711f740b7`](https://github.com/vllm-project/vllm/commit/c711f740b7) [#56349](https://github.com/vllm-project/vllm/pull/56349)
  [ROCm] Auto-enable breakable CUDA graphs for DeepseekV41ForCausalLM (#56349)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-09-12** [`72d4d83157`](https://github.com/vllm-project/vllm/commit/72d4d83157) [#56610](https://github.com/vllm-project/vllm/pull/56610)
  [ROCm][Bugfix] Fix elastic EP scaling deadlock (#56610)
  _Files: `vllm/distributed/device_communicators/pynccl.py`, `vllm/distributed/elastic_ep/elastic_execute.py`, `vllm/distributed/elastic_ep/standby_state.py`, `vllm/distributed/parallel_state.py`_
- **2026-09-12** [`2f59050eda`](https://github.com/vllm-project/vllm/commit/2f59050eda) [#56555](https://github.com/vllm-project/vllm/pull/56555)
  [XPU][CI] Skip ROCm test on non-ROCm platforms (#56555)
  _Files: `tests/test_config.py`_
- **2026-09-12** [`986e2f870a`](https://github.com/vllm-project/vllm/commit/986e2f870a) [#55522](https://github.com/vllm-project/vllm/pull/55522)
  [Refactor][ROCm] Migrate the RDNA3 W4A16 MoE to the oracle/experts pa… (#55522)
  _Files: `tests/kernels/quantization/test_rdna3_compile_guards.py`, `tests/quantization/test_moe_wna16.py`, `vllm/config/kernel.py`, `vllm/model_executor/layers/fused_moe/experts/rdna3_moe.py` _+6 more__
- **2026-09-12** [`756794a9a7`](https://github.com/vllm-project/vllm/commit/756794a9a7) [#56392](https://github.com/vllm-project/vllm/pull/56392)
  [Frontend] create unified Cohere parser (#56392)
  _Files: `docs/features/reasoning_outputs.md`, `docs/features/tool_calling.md`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt` _+17 more__
- **2026-09-12** [`d406f09eb8`](https://github.com/vllm-project/vllm/commit/d406f09eb8) [#55252](https://github.com/vllm-project/vllm/pull/55252)
  [ROCm][CI] Stage F gating (#55252)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/misc.yaml` _+5 more__
- **2026-09-12** [`30118ba27d`](https://github.com/vllm-project/vllm/commit/30118ba27d) [#56554](https://github.com/vllm-project/vllm/pull/56554)
  [DSV4.1] Remove compressor-aware image sentinel token padding (#56554)
  _Files: `vllm/models/deepseek_v4_1/amd/vl_model.py`, `vllm/models/deepseek_v4_1/common/mm_preprocess.py`, `vllm/models/deepseek_v4_1/nvidia/vl_model.py`, `vllm/transformers_utils/configs/deepseek_v41.py`_
- **2026-09-12** [`06e57f622c`](https://github.com/vllm-project/vllm/commit/06e57f622c) [#56526](https://github.com/vllm-project/vllm/pull/56526)
  [ROCm][Kimi-K3] Fix non-contiguous state_indices crash and GPU-sync assert in fused KDA/MLA prefill (#56526)
  _Files: `vllm/models/kimi_k3/amd/ops/kda_chunk.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-09-12** [`46d2b23ac5`](https://github.com/vllm-project/vllm/commit/46d2b23ac5) [#56503](https://github.com/vllm-project/vllm/pull/56503)
  [ROCm][DSV4.1][Perf] Use AITER mHC for the delayed pre block (#56503)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/kernels/mhc/__init__.py`, `vllm/model_executor/kernels/mhc/aiter.py` _+3 more__
- **2026-09-11** [`bbaa1b9340`](https://github.com/vllm-project/vllm/commit/bbaa1b9340) [#56522](https://github.com/vllm-project/vllm/pull/56522)
  [ROCm][CI] Extend timeout for `Basic Models (other)` (#56522)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`_
- **2026-09-11** [`2d75e586fc`](https://github.com/vllm-project/vllm/commit/2d75e586fc) [#56153](https://github.com/vllm-project/vllm/pull/56153)
  [ROCm][Kernel][DSV4] Remove tl.constexpr to avoid cold-compile churn in indexer gather kernel (#56153)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-09-11** [`dc07f1638f`](https://github.com/vllm-project/vllm/commit/dc07f1638f) [#56160](https://github.com/vllm-project/vllm/pull/56160)
  [Bugfix][MLA] Read sparse model settings from text config (#56160)
  _Files: `tests/v1/attention/test_dspark_noncausal_sparse_mla.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/model_executor/kernels/attention/dsa/dcp_indexer_cutedsl.py` _+7 more__
- **2026-09-11** [`6fe67cbbf3`](https://github.com/vllm-project/vllm/commit/6fe67cbbf3) [#46994](https://github.com/vllm-project/vllm/pull/46994)
  [Spec][V2] Support MTP speculative decoding under pipeline parallelism (#46994)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `tests/v1/e2e/spec_decode/test_mtp_parallel_load.py`, `vllm/model_executor/layers/attention/sparse_mla_attention.py`, `vllm/model_executor/models/deepseek_mtp.py` _+8 more__
- **2026-09-11** [`9dd969da09`](https://github.com/vllm-project/vllm/commit/9dd969da09) [#55107](https://github.com/vllm-project/vllm/pull/55107)
  [Model][ROCm] Enable DeepSeek V4 Vision (#55107)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/models/multimodal/processing/test_tensor_schema.py`, `tests/models/test_deepseek_v4_vl_rocm.py` _+13 more__
- **2026-09-11** [`127143e27f`](https://github.com/vllm-project/vllm/commit/127143e27f) [#53664](https://github.com/vllm-project/vllm/pull/53664)
  Revert "[Rocm][Kimi-k3] Fix pipeline_parallel support for the kimik3 DCP mode  (#53664)" (#56429)
  _Files: `tests/models/test_registry.py`, `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-09-11** [`b87339888d`](https://github.com/vllm-project/vllm/commit/b87339888d) [#56460](https://github.com/vllm-project/vllm/pull/56460)
  [httpx migration] Import httpx from huggingface_hub (#56460)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt` _+3 more__
- **2026-09-11** [`5fe77aecfc`](https://github.com/vllm-project/vllm/commit/5fe77aecfc) [#55353](https://github.com/vllm-project/vllm/pull/55353)
  [Deprecation] Deprecate items scheduled for 0.29 (#55353)
  _Files: `benchmarks/attention_benchmarks/mla_runner.py`, `tests/engine/test_arg_utils.py`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `tests/kernels/test_compressor_kv_cache.py` _+24 more__
- **2026-09-11** [`5392fbca2a`](https://github.com/vllm-project/vllm/commit/5392fbca2a) [#56459](https://github.com/vllm-project/vllm/pull/56459)
  [ROCm][Docker] Pin AINIC apt repo to snapshot 1.117.5-a-77 (#56459)
  _Files: `docker/Dockerfile.rocm`, `docker/Dockerfile.rocm_gfx1250`, `docs/features/moriio_connector_usage.md`_
- **2026-09-11** [`b4da4d17ae`](https://github.com/vllm-project/vllm/commit/b4da4d17ae) [#56433](https://github.com/vllm-project/vllm/pull/56433)
  [ROCm][Bugfix] Fix AITER preshuffled FP8 block-scale kernel (#56433)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/linear.py`, `vllm/models/deepseek_v4/amd/model.py` _+1 more__
- **2026-09-11** [`eb7e894432`](https://github.com/vllm-project/vllm/commit/eb7e894432) [#55667](https://github.com/vllm-project/vllm/pull/55667)
  [ROCm][CI] Add HY-V4 generation coverage (#55667)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_distributed.yaml`, `tests/models/test_hyv4_rocm.py`_
- **2026-09-11** [`e77daef89e`](https://github.com/vllm-project/vllm/commit/e77daef89e) [#56214](https://github.com/vllm-project/vllm/pull/56214)
  [Model] Support DeepSeek-V4.1-Flash (#56214)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/fusion/test_quant_activation_contract.py`, `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/kernels/core/test_fused_q_kv_rmsnorm.py` _+45 more__
- **2026-09-11** [`d0dfe587d5`](https://github.com/vllm-project/vllm/commit/d0dfe587d5) [#55095](https://github.com/vllm-project/vllm/pull/55095)
  [Bugfix] Fall back to full decode graphs for noncompiled models (#55095)
  _Files: `tests/test_config.py`, `tests/v1/spec_decode/test_adaptive_verification.py`, `vllm/config/compilation.py`, `vllm/config/vllm.py` _+3 more__
- **2026-09-11** [`a9271c750f`](https://github.com/vllm-project/vllm/commit/a9271c750f) [#56356](https://github.com/vllm-project/vllm/pull/56356)
  [ROCm][CI] Accept `base-v2-preview` images during content hash lookup for ROCm base images (#56356)
  _Files: `.buildkite/scripts/rocm/refresh-base-image.sh`_
- **2026-09-11** [`ae48466cf3`](https://github.com/vllm-project/vllm/commit/ae48466cf3) [#48247](https://github.com/vllm-project/vllm/pull/48247)
  [Perf][ROCm] Add AITER custom AG/RS (DP only) (#48247)
  _Files: `benchmarks/kernels/benchmark_device_communicators.py`, `tests/distributed/test_comm_ops.py`, `tests/distributed/test_rocm_aiter_custom_ar.py`, `tests/utils.py` _+4 more__
- **2026-09-11** [`828f4f19b4`](https://github.com/vllm-project/vllm/commit/828f4f19b4) [#55239](https://github.com/vllm-project/vllm/pull/55239)
  [ROCm][Bugfix] Route GLM-5.3-Flash MTP through ragged sparse MLA (#55239)
  _Files: `tests/v1/attention/test_rocm_glm5next_sparse.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-09-10** [`9163190dda`](https://github.com/vllm-project/vllm/commit/9163190dda) [#56098](https://github.com/vllm-project/vllm/pull/56098)
  [ROCm][Bugfix][Perf] Tune multi-stream shared experts use; wvSplitKrc fixes (#56098)
  _Files: `csrc/rocm/skinny_gemms.cu`, `tests/kernels/quantization/test_rocm_skinny_gemms.py`, `vllm/distributed/parallel_state.py`, `vllm/model_executor/layers/fused_moe/runner/moe_runner.py` _+2 more__
- **2026-09-10** [`7de70fa7ae`](https://github.com/vllm-project/vllm/commit/7de70fa7ae) [#56161](https://github.com/vllm-project/vllm/pull/56161)
  [Bugfix][ROCm] Create linear layer biases with `requires_grad=False` (#56161)
  _Files: `.buildkite/test-amd.yaml`, `vllm/model_executor/layers/linear.py`_
- **2026-09-10** [`48cb12c184`](https://github.com/vllm-project/vllm/commit/48cb12c184) [#56190](https://github.com/vllm-project/vllm/pull/56190)
  [ROCm][Bugfix] Fix profiler in TheRock image (#56190)
  _Files: `vllm/env_override.py`_
- **2026-09-10** [`8359e15aae`](https://github.com/vllm-project/vllm/commit/8359e15aae) [#53695](https://github.com/vllm-project/vllm/pull/53695)
  [ROCm][Feature] Support KV connectors with ROCM_AITER_UNIFIED_ATTN (#53695)
  _Files: `tests/v1/attention/test_rocm_attention_backends_selection.py`, `tests/v1/kv_connector/unit/test_offloading_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/config.py`, `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`_
- **2026-09-10** [`7470082f57`](https://github.com/vllm-project/vllm/commit/7470082f57) [#51692](https://github.com/vllm-project/vllm/pull/51692)
  [ROCm][Perf] Add bpreshuffled blockscaled fp8 GEMM (#51692)
  _Files: `vllm/_aiter_ops.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`_
- **2026-09-10** [`9b959b8657`](https://github.com/vllm-project/vllm/commit/9b959b8657) [#56228](https://github.com/vllm-project/vllm/pull/56228)
  [Model] DeepSeek-V4.1-Flash Model Definitions (#56228)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `tests/parser/engine/trace_builder.py`, `vllm/model_executor/kernels/attention/dsa/candidate_blocks.py`, `vllm/model_executor/kernels/linear/__init__.py` _+43 more__
- **2026-09-10** [`6ff479e1f7`](https://github.com/vllm-project/vllm/commit/6ff479e1f7) [#55236](https://github.com/vllm-project/vllm/pull/55236)
  [ROCm] Add better kv dtype error discoverability (#55236)
  _Files: `vllm/platforms/rocm.py`_
- **2026-09-10** [`9521c60bdc`](https://github.com/vllm-project/vllm/commit/9521c60bdc) [#54038](https://github.com/vllm-project/vllm/pull/54038)
  [ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill reland (#54038)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/kimi_k3/fused_kda_chunk_kernel_rocm.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+5 more__
- **2026-09-10** [`7e91760650`](https://github.com/vllm-project/vllm/commit/7e91760650) [#54855](https://github.com/vllm-project/vllm/pull/54855)
  [ROCm][Perf] Route large DSV4 sparse prefill to AITER OPUS (#54855)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-09-10** [`49632fb3ac`](https://github.com/vllm-project/vllm/commit/49632fb3ac) [#56010](https://github.com/vllm-project/vllm/pull/56010)
  [CI][XPU] Reject CUDA-IPC weight cache on non-CUDA/ROCm platforms (#56010)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/__init__.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py` _+1 more__
- **2026-09-10** [`588a813a60`](https://github.com/vllm-project/vllm/commit/588a813a60) [#55213](https://github.com/vllm-project/vllm/pull/55213)
  [ROCm] [BugFix] Fix AITER MXFP4 ASM-GEMM crash on unfused shared experts (#55213)
  _Files: `tests/kernels/quantization/test_rocm_mxfp4.py`, `vllm/model_executor/kernels/linear/mxfp4/aiter.py`, `vllm/model_executor/models/qwen3_next.py`_
- **2026-09-10** [`2a02f6efe3`](https://github.com/vllm-project/vllm/commit/2a02f6efe3) [#53885](https://github.com/vllm-project/vllm/pull/53885)
  [CI][ROCm][Disagg] Add GLM-5.2-FP8 to MoRIIO model catalog (#53885)
  _Files: `.buildkite/amd-disagg/models.yaml`, `.buildkite/amd-disagg/pipeline-disagg.yaml`_
- **2026-09-09** [`83252ea899`](https://github.com/vllm-project/vllm/commit/83252ea899) [#52664](https://github.com/vllm-project/vllm/pull/52664)
  [Performance][ROCm]  Integrate aiter indexer scoring and top-k kernels into MiniMax-M3 sparse attention path (#52664)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/amd/indexer_aiter.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py` _+2 more__
- **2026-09-09** [`6983a0883d`](https://github.com/vllm-project/vllm/commit/6983a0883d) [#53602](https://github.com/vllm-project/vllm/pull/53602)
  [ROCm][CI] Split MI300 Distributed Compile by graph partition mode (#53602)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-09** [`dcd544486b`](https://github.com/vllm-project/vllm/commit/dcd544486b) [#55887](https://github.com/vllm-project/vllm/pull/55887)
  [ROCm][Bugfix] Support shared KV prefill in AITER attention (#55887)
  _Files: `tests/kernels/attention/test_rocm_aiter_fa.py`, `vllm/v1/attention/backends/rocm_aiter_fa.py`_
- **2026-09-09** [`cce50657b7`](https://github.com/vllm-project/vllm/commit/cce50657b7) [#56130](https://github.com/vllm-project/vllm/pull/56130)
  [ROCm][CI] Use a platform-independent GEMM in the merged-column fuser test (#56130)
  _Files: `tests/models/transformers/fusers/test_linear.py`_
- **2026-09-09** [`c69d5d72a6`](https://github.com/vllm-project/vllm/commit/c69d5d72a6) [#56114](https://github.com/vllm-project/vllm/pull/56114)
  [CI][ROCm] Increase timeout for AMD MI355 Language Models (Standard) (#56114)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-09** [`3fb676bfad`](https://github.com/vllm-project/vllm/commit/3fb676bfad) [#56106](https://github.com/vllm-project/vllm/pull/56106)
  [ROCm][CI] Fix moe layer tests for fp8 dtype compatibility (#56106)
  _Files: `tests/kernels/moe/test_moe_layer.py`, `tests/kernels/moe/utils.py`_
- **2026-09-09** [`1454b71727`](https://github.com/vllm-project/vllm/commit/1454b71727) [#53590](https://github.com/vllm-project/vllm/pull/53590)
  Fix ROCm AITER FP8 KV test tolerances. (#53590)
  _Files: `tests/kernels/attention/test_rocm_aiter_fa.py`, `tests/kernels/attention/test_rocm_aiter_unified_attn.py`_
- **2026-09-09** [`d8d53f17c2`](https://github.com/vllm-project/vllm/commit/d8d53f17c2) [#53664](https://github.com/vllm-project/vllm/pull/53664)
  [Rocm][Kimi-k3] Add pipeline_parallel support for the kimik3 model (#53664)
  _Files: `tests/models/test_registry.py`, `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-09-09** [`4e990dfcec`](https://github.com/vllm-project/vllm/commit/4e990dfcec) [#55968](https://github.com/vllm-project/vllm/pull/55968)
  [ROCm] Bump AITER to v0.1.21.post2 (#55968)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-09-09** [`62f3bf58a5`](https://github.com/vllm-project/vllm/commit/62f3bf58a5) [#56035](https://github.com/vllm-project/vllm/pull/56035)
  [Bugfix][ROCm][DSv4] Skip launch_pdl=True JIT warmup when PDL is unsupported (#56035)
  _Files: `vllm/models/common/ops/fused_qk_rmsnorm.py`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`_
- **2026-09-09** [`08b3e67b66`](https://github.com/vllm-project/vllm/commit/08b3e67b66) [#45900](https://github.com/vllm-project/vllm/pull/45900)
  [ROCm][Perf] Fix Qwen3-vLLM audio encoder TP when heads are not divisible by TP size (#45900)
  _Files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`_
- **2026-09-09** [`bc8587f829`](https://github.com/vllm-project/vllm/commit/bc8587f829) [#55099](https://github.com/vllm-project/vllm/pull/55099)
  [ROCm][Perf][Bugfix] Multi-stream perf improvements; rocprofiler fixes (#55099)
  _Files: `docker/Dockerfile.rock_base`, `docker/Dockerfile.rocm_base`, `tests/kernels/moe/parallel_utils.py`, `tests/kernels/moe/test_deepep_moe.py`_
- **2026-09-08** [`60ad959b6f`](https://github.com/vllm-project/vllm/commit/60ad959b6f) [#55513](https://github.com/vllm-project/vllm/pull/55513)
  Fix block FP8 MTP in ModelOpt mixed checkpoints (#55513)
  _Files: `tests/models/qwen4_exp/test_config.py`, `tests/quantization/test_modelopt.py`, `vllm/model_executor/layers/quantization/modelopt.py`, `vllm/models/qwen4_exp/amd/mtp.py` _+1 more__
- **2026-09-08** [`28a2ccee78`](https://github.com/vllm-project/vllm/commit/28a2ccee78) [#53195](https://github.com/vllm-project/vllm/pull/53195)
  [ROCm][DI][CI] Enable WideEP Intranode tests  (#53195)
  _Files: `.buildkite/amd-disagg/models.yaml`, `.buildkite/amd-disagg/pipeline-disagg.yaml`, `.buildkite/amd-disagg/run-slurm-disagg-test.sh`, `.buildkite/amd-disagg/run_xPyD_disagg.slurm`_
- **2026-09-08** [`73f61d12aa`](https://github.com/vllm-project/vllm/commit/73f61d12aa) [#55919](https://github.com/vllm-project/vllm/pull/55919)
  [CI][ROCm] Increase timeouts for AMD MI300 jobs (#55919)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-09-08** [`db3814a4f2`](https://github.com/vllm-project/vllm/commit/db3814a4f2) [#55780](https://github.com/vllm-project/vllm/pull/55780)
  [Attention] Require explicit DCP support from attention implementations (#55780)
  _Files: `tests/kernels/attention/test_attention_selector.py`, `tests/test_attention_backend_registry.py`, `tests/v1/attention/test_rocm_attention_backends_selection.py`, `vllm/v1/attention/backend.py` _+11 more__
- **2026-09-08** [`2c9d68f80b`](https://github.com/vllm-project/vllm/commit/2c9d68f80b) [#54809](https://github.com/vllm-project/vllm/pull/54809)
  [Quant][Kernel] Remove GPTQ Group/Dynamic Activation Ordering (#54809)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_machete.py`, `benchmarks/kernels/benchmark_marlin.py`, `csrc/cpu/cpu_wna16.cpp` _+95 more__
- **2026-09-08** [`1a522b6949`](https://github.com/vllm-project/vllm/commit/1a522b6949) [#54112](https://github.com/vllm-project/vllm/pull/54112)
  [ROCm] [Docker] Upgrade default AINIC repo to ship libionic 54.0-187-1 (#54112)
  _Files: `docker/Dockerfile.rocm`, `docker/Dockerfile.rocm_gfx1250`, `docs/features/moriio_connector_usage.md`_
- **2026-09-08** [`7c2f1ff495`](https://github.com/vllm-project/vllm/commit/7c2f1ff495) [#54523](https://github.com/vllm-project/vllm/pull/54523)
  [Core] Scope PCP-DP validation to GPU manager (#54523)
  _Files: `vllm/config/parallel.py`, `vllm/platforms/cuda.py`, `vllm/platforms/rocm.py`_
- **2026-09-08** [`6ddbab03de`](https://github.com/vllm-project/vllm/commit/6ddbab03de) [#50176](https://github.com/vllm-project/vllm/pull/50176)
  [4/N][warmup][DSv4] Migrate common attention kernels (#50176)
  _Files: `tests/kernels/core/test_fused_q_kv_rmsnorm.py`, `tests/model_executor/test_jit_warmup.py`, `vllm/model_executor/warmup/jit_warmup.py`, `vllm/model_executor/warmup/jit_warmup_triton_helper.py` _+15 more__
- **2026-09-08** [`25047604fe`](https://github.com/vllm-project/vllm/commit/25047604fe) [#55808](https://github.com/vllm-project/vllm/pull/55808)
  [ROCm][Perf] Remove AITER paged-MQA outputs guard for DeepSeek-V4 (#55808)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-09-08** [`e41a17e606`](https://github.com/vllm-project/vllm/commit/e41a17e606) [#52263](https://github.com/vllm-project/vllm/pull/52263)
  [ROCm][Quantization] Support AMD Quark per-block FP8 for fused MoE layers (#52263)
  _Files: `tests/quantization/test_quark.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w8a8_fp8.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py` _+1 more__
- **2026-09-08** [`ce6c241ddc`](https://github.com/vllm-project/vllm/commit/ce6c241ddc) [#54787](https://github.com/vllm-project/vllm/pull/54787)
  [ROCm][Perf][M3] Fused allreduce+GemmaRMSNorm fast path (#54787)
  _Files: `vllm/_aiter_ops.py`, `vllm/distributed/device_communicators/aiter_custom_all_reduce.py`, `vllm/model_executor/layers/fused_allreduce_gemma_rms_norm.py`_
- **2026-09-08** [`755541443f`](https://github.com/vllm-project/vllm/commit/755541443f) [#53856](https://github.com/vllm-project/vllm/pull/53856)
  [Bugfix][ROCm] Mask paged attention V cache padding (#53856)
  _Files: `csrc/rocm/attention.cu`, `tests/kernels/attention/test_attention.py`_
- **2026-09-08** [`6b5a12c0f8`](https://github.com/vllm-project/vllm/commit/6b5a12c0f8) [#54405](https://github.com/vllm-project/vllm/pull/54405)
  [ROCm][CI] Enable HY-V4 model initialization on ROCm (#54405)
  _Files: `tests/models/test_registry.py`, `vllm/models/hy_v4/__init__.py`_
- **2026-09-07** [`537af2c3a4`](https://github.com/vllm-project/vllm/commit/537af2c3a4) [#55454](https://github.com/vllm-project/vllm/pull/55454)
  [CI] Recover empty multi-node Docker networks and finish partial cleanup (#55454)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/scripts/run-multi-node-test.sh`_
- **2026-09-07** [`e476556189`](https://github.com/vllm-project/vllm/commit/e476556189) [#54404](https://github.com/vllm-project/vllm/pull/54404)
  [ROCm][CI] Add attention-sink support to ROCm AITER sparse MLA (#54404)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_op_registration.py`, `tests/kernels/attention/test_rocm_aiter_mla_sink.py`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `tests/v1/attention/test_rocm_glm5next_sparse.py` _+4 more__
- **2026-09-07** [`195bc9c4a1`](https://github.com/vllm-project/vllm/commit/195bc9c4a1) [#55653](https://github.com/vllm-project/vllm/pull/55653)
  [CI][ROCm] Temporarily skip unsupported HY-V4 initialization (#55653)
  _Files: `tests/models/test_initialization.py`_
- **2026-09-07** [`1f778486fc`](https://github.com/vllm-project/vllm/commit/1f778486fc) [#54975](https://github.com/vllm-project/vllm/pull/54975)
  [Bugfix][Offloader] Preserve prefetch static-buffer slot ownership (#54975)
  _Files: `tests/model_executor/offloader/test_prefetch.py`, `vllm/model_executor/offloader/prefetch.py`_
- **2026-09-07** [`de69e821b7`](https://github.com/vllm-project/vllm/commit/de69e821b7) [#53161](https://github.com/vllm-project/vllm/pull/53161)
  [ROCm][Perf][DeepSeek V4] Fuse native FP8 shared expert with MXFP4 routed experts (#53161)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`, `vllm/models/deepseek_v4/amd/model.py`_
- **2026-09-07** [`199cb9b964`](https://github.com/vllm-project/vllm/commit/199cb9b964) [#55535](https://github.com/vllm-project/vllm/pull/55535)
  [Kernel] Remove unused fake implementation (#55535)
  _Files: `vllm/_aiter_ops.py`, `vllm/_custom_ops.py`, `vllm/_xpu_ops.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py` _+35 more__

## Attention  (53 commits)

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
- **2026-09-13** [`b23433088b`](https://github.com/vllm-project/vllm/commit/b23433088b) [#55802](https://github.com/vllm-project/vllm/pull/55802)
  [Attention] Remove DCP indexer interleave guard and test TP1 output parity (#55802)
  _Files: `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-09-13** [`186a1e6222`](https://github.com/vllm-project/vllm/commit/186a1e6222) [#55768](https://github.com/vllm-project/vllm/pull/55768)
  [Warmup] Gemma 4 de-JITification (#55768)
  _Files: `vllm/v1/attention/backends/flash_attn.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/vllm_flash_attn/flash_attn_interface.py`_
- **2026-09-13** [`586f652f8d`](https://github.com/vllm-project/vllm/commit/586f652f8d) [#56715](https://github.com/vllm-project/vllm/pull/56715)
  [Bugfix][PCP][DCP] Respect interleave in indexer KV gather mapping (#56715)
  _Files: `tests/v1/attention/test_indexer_dcp_localize.py`, `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-09-13** [`82a85dc1d2`](https://github.com/vllm-project/vllm/commit/82a85dc1d2) [#56305](https://github.com/vllm-project/vllm/pull/56305)
  [Attention] Add Triton/FlashInfer composite for multimodal prefix attention (#56305)
  _Files: `docs/design/attention_backends.md`, `tests/kernels/attention/test_attention_selector.py`, `tests/v1/attention/test_mm_prefix.py`, `tests/v1/spec_decode/test_dflash2.py` _+11 more__
- **2026-09-13** [`dd4c841070`](https://github.com/vllm-project/vllm/commit/dd4c841070) [#55897](https://github.com/vllm-project/vllm/pull/55897)
  [LoRA] Add LoRA support for DeepSeek-V4 Flash Vision (#55897)
  _Files: `docs/models/supported_models.md`, `vllm/lora/ops/triton_ops/lora_shrink_op.py`, `vllm/models/deepseek_v4/common/vl_model.py`_
- **2026-09-13** [`2671fedfc7`](https://github.com/vllm-project/vllm/commit/2671fedfc7) [#56654](https://github.com/vllm-project/vllm/pull/56654)
  [MRV2] Revert explicit Triton JIT warmup migration (#56654)
  _Files: `tests/v1/spec_decode/test_dflash_prepare_inputs.py`, `tests/v1/worker/test_gpu_autoregressive_speculator.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/sample/states.py` _+2 more__
- **2026-09-12** [`ebe1dec2da`](https://github.com/vllm-project/vllm/commit/ebe1dec2da) [#56157](https://github.com/vllm-project/vllm/pull/56157)
  [PCP][DCP] Enable PCP+DCP on sparse-MLA models (#56157)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-DCP4-EP.yaml`, `tests/evals/gsm8k/configs/models-pcp.txt`, `tests/v1/attention/test_indexer_dcp_localize.py` _+17 more__
- **2026-09-12** [`13e221f830`](https://github.com/vllm-project/vllm/commit/13e221f830) [#56562](https://github.com/vllm-project/vllm/pull/56562)
  [Perf] Fuse DSV4.1 input metadata preparation with Triton (#56562)
  _Files: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/attention/ops/metadata.py`_
- **2026-09-12** [`6b153463a8`](https://github.com/vllm-project/vllm/commit/6b153463a8) [#54007](https://github.com/vllm-project/vllm/pull/54007)
  [Build] Define _USE_MATH_DEFINES for FlashMLA targets (#54007)
  _Files: `cmake/external_projects/flashmla.cmake`_
- **2026-09-12** [`d43bb2f37f`](https://github.com/vllm-project/vllm/commit/d43bb2f37f) [#53781](https://github.com/vllm-project/vllm/pull/53781)
  [3/N] HiSparse: host-resident sparse-MLA decode hot-buffering (#53781)
- **2026-09-12** [`120ec4ebd2`](https://github.com/vllm-project/vllm/commit/120ec4ebd2) [#53566](https://github.com/vllm-project/vllm/pull/53566)
  [5/N][warmup][DSv4] Migrate NVIDIA CuTeDSL attention kernels (#53566)
  _Files: `tests/model_executor/test_jit_warmup_cutedsl_launcher.py`, `tests/model_executor/test_jit_warmup_triton_launcher.py`, `vllm/cute_utils/__init__.py`, `vllm/model_executor/kernels/attention/dsa/dcp_indexer_cutedsl.py` _+24 more__
- **2026-09-12** [`a0844fa6c6`](https://github.com/vllm-project/vllm/commit/a0844fa6c6) [#56463](https://github.com/vllm-project/vllm/pull/56463)
  [XPU][CI] skip DeepSeek-V4.1-Flash in `test_tensor_schema.py` (#56463)
  _Files: `.buildkite/intel_jobs/models_multimodal_intel.yaml`_
- **2026-09-11** [`9d88ceb026`](https://github.com/vllm-project/vllm/commit/9d88ceb026) [#56485](https://github.com/vllm-project/vllm/pull/56485)
  [KDA] Update flashKDA to support bf16 checkpoint state (#56485)
  _Files: `cmake/external_projects/flashkda.cmake`, `tests/models/kimi_k3/test_kda.py`_
- **2026-09-11** [`9dcf6bf344`](https://github.com/vllm-project/vllm/commit/9dcf6bf344) [#56181](https://github.com/vllm-project/vllm/pull/56181)
  [BugFix] Fix DP token padding in dflash attention metadata (#56181)
  _Files: `tests/v1/spec_decode/test_eagle_draft_attn_metadata.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`, `vllm/v1/worker/gpu/spec_decode/multi_module_mtp/speculator.py` _+1 more__
- **2026-09-11** [`1e1060f998`](https://github.com/vllm-project/vllm/commit/1e1060f998) [#55356](https://github.com/vllm-project/vllm/pull/55356)
  [Kimi Perf] Group fp8 mla cahche insertion, 4~6x kernel level performance improvement for small batch (#55356)
  _Files: `csrc/libtorch_stable/cache_kernels.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `tests/kernels/attention/test_cache.py` _+2 more__
- **2026-09-11** [`8c1d1c2974`](https://github.com/vllm-project/vllm/commit/8c1d1c2974) [#55127](https://github.com/vllm-project/vllm/pull/55127)
  [Misc] Log FlashInfer allreduce workspace init failure as error (#55127)
  _Files: `vllm/distributed/device_communicators/flashinfer_all_reduce.py`, `vllm/logger.py`_
- **2026-09-11** [`1cf6555214`](https://github.com/vllm-project/vllm/commit/1cf6555214) [#56138](https://github.com/vllm-project/vllm/pull/56138)
  [Bugfix] Pin EPLB and MLA host-to-device transfer buffers (#56138)
  _Files: `tests/distributed/test_eplb_execute.py`, `tests/v1/attention/test_mla_context_chunks.py`, `vllm/distributed/eplb/eplb_communicator.py`, `vllm/model_executor/layers/attention/sparse_mla_attention.py`_
- **2026-09-11** [`4b839c3378`](https://github.com/vllm-project/vllm/commit/4b839c3378) [#50439](https://github.com/vllm-project/vllm/pull/50439)
  [Attention] Extend XQA decode support on SM90 (#50439)
  _Files: `tests/v1/attention/test_attention_backends.py`, `tests/v1/attention/test_flashinfer_dcp_spec_reorder.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-09-11** [`fbf51c7026`](https://github.com/vllm-project/vllm/commit/fbf51c7026) [#55864](https://github.com/vllm-project/vllm/pull/55864)
  [Bugfix] Fix FlashInfer KV sharing with omitted K/V (#55864)
  _Files: `vllm/model_executor/models/gemma4_mtp.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-09-11** [`980c16c8e4`](https://github.com/vllm-project/vllm/commit/980c16c8e4) [#56107](https://github.com/vllm-project/vllm/pull/56107)
  [PCP][Spec Decode] Adds PCP support for single-module MTP and replicated DSpark. (#56107)
  _Files: `tests/v1/spec_decode/test_eagle_draft_attn_metadata.py`, `tests/v1/worker/test_gpu_autoregressive_speculator.py`, `tests/v1/worker/test_gpu_pcp_manager.py`, `vllm/model_executor/layers/sparse_attn_indexer.py` _+7 more__
- **2026-09-10** [`5b6cf93e8e`](https://github.com/vllm-project/vllm/commit/5b6cf93e8e) [#54968](https://github.com/vllm-project/vllm/pull/54968)
  [XPU] Add forward_xpu to Mixer2RMSNormGated and FusedRMSNormGated (#54968)
  _Files: `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/third_party/flash_linear_attention/ops/kda.py`_
- **2026-09-10** [`e6cb56337b`](https://github.com/vllm-project/vllm/commit/e6cb56337b) [#56145](https://github.com/vllm-project/vllm/pull/56145)
  [Core] MRV2 support for fast-prefill (#56145)
  _Files: `.buildkite/test_areas/engine.yaml`, `tests/v1/e2e/general/test_kv_sharing_fast_prefill.py`, `tests/v1/worker/test_attn_utils.py`, `tests/v1/worker/test_gpu_model_runner_v2.py` _+8 more__
- **2026-09-10** [`6ee5bb0a0b`](https://github.com/vllm-project/vllm/commit/6ee5bb0a0b) [#54889](https://github.com/vllm-project/vllm/pull/54889)
  [DCP][Kernel][Perf] Fuse the empty-shard LSE mask into the A2A pack kernel (#54889)
  _Files: `tests/v1/attention/test_dcp_a2a_pack_mask.py`, `vllm/v1/attention/ops/dcp.py`_
- **2026-09-10** [`1768273c13`](https://github.com/vllm-project/vllm/commit/1768273c13) [#55736](https://github.com/vllm-project/vllm/pull/55736)
  [Perf][GLM-5.3-Flash] Decode hot-path cleanups: strided KDA recurrent inputs, NoPE MQA query without concat, no duplicate router GEMM (#55736)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/glm5next/__init__.py`, `tests/models/glm5next/test_kda_recurrent.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+4 more__
- **2026-09-10** [`b47b01cf33`](https://github.com/vllm-project/vllm/commit/b47b01cf33) [#56208](https://github.com/vllm-project/vllm/pull/56208)
  [Model][Frontend] Support DeepSeek-V4.1-Flash in Rust and Python frontends (#56208)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/error.rs` _+48 more__
- **2026-09-10** [`be1cb9834b`](https://github.com/vllm-project/vllm/commit/be1cb9834b) [#56215](https://github.com/vllm-project/vllm/pull/56215)
  [Kernel] Optional Q-norm in fused DSv4 MLA epilogue; group_size=32 for packed FP8 quant (#56215)
  _Files: `csrc/libtorch_stable/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/quantization/w8a8/fp8/per_token_group_quant.cu`, `csrc/libtorch_stable/torch_bindings.cpp` _+2 more__
- **2026-09-10** [`83990f5bcc`](https://github.com/vllm-project/vllm/commit/83990f5bcc) [#55212](https://github.com/vllm-project/vllm/pull/55212)
  [Bugfix][MRV2] Initialize DCP metadata after batch partitioning (#55212)
  _Files: `tests/v1/spec_decode/test_eagle_draft_attn_metadata.py`, `tests/v1/worker/test_gpu_input_batch_v2.py`, `tests/v1/worker/test_gpu_pcp_manager.py`, `tests/v1/worker/test_gpu_ubatch_slicing.py` _+8 more__
- **2026-09-09** [`8c87c333b8`](https://github.com/vllm-project/vllm/commit/8c87c333b8) [#55499](https://github.com/vllm-project/vllm/pull/55499)
  [Perf] Fix TRTLLM ragged prefill perf regression (#55499)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `requirements/cuda.txt`, `tests/v1/attention/test_mla_context_chunks.py` _+2 more__
- **2026-09-09** [`7e95735eb9`](https://github.com/vllm-project/vllm/commit/7e95735eb9) [#55888](https://github.com/vllm-project/vllm/pull/55888)
  [Bugfix] Avoid FlexAttention recompiles when request counts change (#55888)
  _Files: `tests/kernels/test_flex_attention.py`, `vllm/v1/attention/backends/flex_attention.py`_
- **2026-09-09** [`e509d32b5a`](https://github.com/vllm-project/vllm/commit/e509d32b5a) [#55690](https://github.com/vllm-project/vllm/pull/55690)
  [Transformers backend] Enable QKV-Fuser for Gemma4 (#55690)
  _Files: `tests/models/transformers/fusers/test_linear.py`, `tests/models/transformers/fusers/test_mla.py`, `vllm/model_executor/models/transformers/fusers/base.py`, `vllm/model_executor/models/transformers/fusers/glu.py` _+4 more__
- **2026-09-09** [`5acd95906b`](https://github.com/vllm-project/vllm/commit/5acd95906b) [#55458](https://github.com/vllm-project/vllm/pull/55458)
  [Bugfix] Exclude DP token padding from draft attention metadata (#55458)
  _Files: `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`_
- **2026-09-09** [`9e137d8d23`](https://github.com/vllm-project/vllm/commit/9e137d8d23) [#51925](https://github.com/vllm-project/vllm/pull/51925)
  [Kernel] Enable optimized FlashInfer add-RMSNorm NVFP4 fusion (#51925)
  _Files: `tests/compile/passes/test_fusion.py`, `vllm/compilation/passes/fusion/rms_quant_fusion.py`, `vllm/compilation/passes/utility/fix_functionalization.py`_
- **2026-09-08** [`c0d8d5413e`](https://github.com/vllm-project/vllm/commit/c0d8d5413e) [#55301](https://github.com/vllm-project/vllm/pull/55301)
  [Transformers] Generalize merged-column linear fusion (#55301)
  _Files: `tests/models/transformers/fusers/test_linear.py`, `vllm/model_executor/models/transformers/fuser.py`, `vllm/model_executor/models/transformers/fusers/__init__.py`, `vllm/model_executor/models/transformers/fusers/base.py` _+4 more__
- **2026-09-08** [`d29c88f162`](https://github.com/vllm-project/vllm/commit/d29c88f162) [#53007](https://github.com/vllm-project/vllm/pull/53007)
  [Core] Let SWA layers take the primary block size to avoid inflating the KV block LCM (#53007)
  _Files: `tests/v1/attention/test_backend_per_kind.py`, `vllm/model_executor/layers/attention/attention.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-09-08** [`1b2c591cd0`](https://github.com/vllm-project/vllm/commit/1b2c591cd0) [#55031](https://github.com/vllm-project/vllm/pull/55031)
  [Bugfix] speedup nvfp4 kv for FMHA (#55031)
  _Files: `tests/compile/passes/test_fusion_attn.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-09-08** [`bcca76e7db`](https://github.com/vllm-project/vllm/commit/bcca76e7db) [#55908](https://github.com/vllm-project/vllm/pull/55908)
  [Test] Dequantize NVFP4 KV cache scales in the layout the kernel writes (#55908)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/attention/test_cache.py`, `tests/kernels/attention/test_flashinfer_trtllm_attention.py`, `tests/kernels/quantization/nvfp4_utils.py`_
- **2026-09-08** [`6b15bea080`](https://github.com/vllm-project/vllm/commit/6b15bea080) [#53941](https://github.com/vllm-project/vllm/pull/53941)
  [Refactor] Remove utils dead code (#53941)
  _Files: `tests/models/multimodal/generation/test_memory_leak.py`, `vllm/compilation/passes/fx_utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/utils.py`, `vllm/model_executor/layers/utils.py` _+11 more__
- **2026-09-08** [`613ab20f7f`](https://github.com/vllm-project/vllm/commit/613ab20f7f) [#55817](https://github.com/vllm-project/vllm/pull/55817)
  [Model] Enable torch.compile for Sarvam MLA (#55817)
  _Files: `vllm/model_executor/models/sarvam.py`_
- **2026-09-08** [`414057a3d3`](https://github.com/vllm-project/vllm/commit/414057a3d3) [#52156](https://github.com/vllm-project/vllm/pull/52156)
  [Bugfix] Apply attention sinks in the Transformers backend (#52156)
  _Files: `tests/models/transformers/test_backend.py`, `vllm/model_executor/models/transformers/__init__.py`, `vllm/model_executor/models/transformers/base.py`, `vllm/model_executor/models/transformers/fusers/attention.py`_
- **2026-09-08** [`472d8c9125`](https://github.com/vllm-project/vllm/commit/472d8c9125) [#55629](https://github.com/vllm-project/vllm/pull/55629)
  [Perf] Fuse DeepEncoder relative bias in Triton attention (#55629)
  _Files: `vllm/model_executor/models/deepencoder.py`_
- **2026-09-08** [`f6326f53bd`](https://github.com/vllm-project/vllm/commit/f6326f53bd) [#55715](https://github.com/vllm-project/vllm/pull/55715)
  [Perf][GDN] Enable the FlashInfer GDN prefill kernel on SM12x (#55715)
  _Files: `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-09-08** [`eb6b619ab2`](https://github.com/vllm-project/vllm/commit/eb6b619ab2) [#54756](https://github.com/vllm-project/vllm/pull/54756)
  [Bugfix][KV Offload] Register mixed page sizes in one cache group (#54756)
  _Files: `tests/v1/attention/utils.py`, `tests/v1/simple_kv_offload/test_worker.py`, `vllm/v1/simple_kv_offload/worker.py`_
- **2026-09-08** [`a69402aaa8`](https://github.com/vllm-project/vllm/commit/a69402aaa8) [#55364](https://github.com/vllm-project/vllm/pull/55364)
  [Perf] Integrate FlashInfer KDA kernels (#55364)
  _Files: `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/layers/mamba/mamba_utils.py` _+4 more__
- **2026-09-07** [`7cc89a7dda`](https://github.com/vllm-project/vllm/commit/7cc89a7dda) [#55728](https://github.com/vllm-project/vllm/pull/55728)
  [Tests] Update SarvamMLA transformers v5 compatibility reason to hf (#55728)
  _Files: `tests/models/registry.py`_
- **2026-09-07** [`42801b3a6b`](https://github.com/vllm-project/vllm/commit/42801b3a6b) [#53565](https://github.com/vllm-project/vllm/pull/53565)
  [3/N][warmup][DSv4] Migrate FA4 MLA and shared CuTeDSL kernels (#53565)
  _Files: `tests/models/inkling/test_fa4_rel_attention.py`, `tests/v1/attention/test_mla_prefill_quant_output.py`, `vllm/model_executor/warmup/fa4_cutedsl_warmup.py`, `vllm/model_executor/warmup/kernel_warmup.py` _+4 more__
- **2026-09-07** [`1713b9866a`](https://github.com/vllm-project/vllm/commit/1713b9866a) [#53564](https://github.com/vllm-project/vllm/pull/53564)
  [2/N][warmup][DSv4] Migrate sequence and DCP kernels (#53564)
  _Files: `.buildkite/test_areas/model_executor.yaml`, `tests/model_executor/test_jit_warmup.py`, `tests/model_executor/test_jit_warmup_cutedsl_launcher.py`, `tests/model_executor/test_jit_warmup_triton_launcher.py` _+8 more__
- **2026-09-07** [`94e26dd3dd`](https://github.com/vllm-project/vllm/commit/94e26dd3dd) [#54890](https://github.com/vllm-project/vllm/pull/54890)
  [Qwen3.8-Flash-Next] Support FP8 indexer cache for QSA (#54890)
  _Files: `tests/models/qwen4_exp/test_qsa_pre_indexer.py`, `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/models/qwen4_exp/common/qsa_cache.py`, `vllm/models/qwen4_exp/nvidia/indexer_qsa.py` _+1 more__
- **2026-09-07** [`d9105ea800`](https://github.com/vllm-project/vllm/commit/d9105ea800) [#55272](https://github.com/vllm-project/vllm/pull/55272)
  [Qwen3.8-Flash-Next] Remove torch.compile for NVIDIA implementation (#55272)
  _Files: `tests/models/qwen4_exp/test_config.py`, `tests/models/qwen4_exp/test_ple.py`, `tests/models/qwen4_exp/test_qsa_reference.py`, `tests/test_config.py` _+9 more__

## Multimodal  (34 commits)

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
- **2026-09-13** [`8cf9de9080`](https://github.com/vllm-project/vllm/commit/8cf9de9080) [#56528](https://github.com/vllm-project/vllm/pull/56528)
  [Test][Determinism] Cover VLM batch invariance in default execution mode (#56528)
  _Files: `tests/v1/determinism/test_batch_invariance_vlm.py`_
- **2026-09-13** [`fa1b3b1922`](https://github.com/vllm-project/vllm/commit/fa1b3b1922) [#56432](https://github.com/vllm-project/vllm/pull/56432)
  [Bugfix][EPD] Preserve explicit multimodal UUIDs with caches disabled (#56432)
  _Files: `tests/renderers/test_process_multi_modal_uuids.py`, `vllm/renderers/base.py`_
- **2026-09-13** [`a987777755`](https://github.com/vllm-project/vllm/commit/a987777755) [#56652](https://github.com/vllm-project/vllm/pull/56652)
  [Bugfix][Gemma4] Keep image kwargs out of video preprocessing (#56652)
  _Files: `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-09-12** [`1b29c508bc`](https://github.com/vllm-project/vllm/commit/1b29c508bc) [#56401](https://github.com/vllm-project/vllm/pull/56401)
  [Bugfix] Initialize data parser in Nano-Nemotron audio test (#56401)
  _Files: `tests/models/multimodal/test_nano_nemotron_vl.py`_
- **2026-09-12** [`a0914ab7d0`](https://github.com/vllm-project/vllm/commit/a0914ab7d0) [#56398](https://github.com/vllm-project/vllm/pull/56398)
  [Nano-Nemotron] Fix Nano-Nemotron precomputed multimodal embeddings (#56398)
  _Files: `tests/models/multimodal/test_nano_nemotron_vl.py`, `vllm/model_executor/models/nano_nemotron_vl.py`_
- **2026-09-12** [`bde4feb061`](https://github.com/vllm-project/vllm/commit/bde4feb061) [#55171](https://github.com/vllm-project/vllm/pull/55171)
  [XPU][CI] Remove pip install dependency in test yaml files (#55171)
  _Files: `.buildkite/intel_jobs/lm_eval_intel.yaml`, `.buildkite/intel_jobs/misc_intel.yaml`, `.buildkite/intel_jobs/model_executor_intel.yaml`, `.buildkite/intel_jobs/models_multimodal_intel.yaml` _+3 more__
- **2026-09-12** [`485421b1c3`](https://github.com/vllm-project/vllm/commit/485421b1c3) [#56386](https://github.com/vllm-project/vllm/pull/56386)
  [Rust Frontend] Honor HF revisions, offline mode, and cache directory (#56386)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+7 more__
- **2026-09-12** [`31759ccb6d`](https://github.com/vllm-project/vllm/commit/31759ccb6d) [#55047](https://github.com/vllm-project/vllm/pull/55047)
  [Rust Frontend][Multimodal] Accept preprocessed multimodal gRPC features (#55047)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/proto/Cargo.toml`, `rust/proto/README.md` _+12 more__
- **2026-09-11** [`22258a26bc`](https://github.com/vllm-project/vllm/commit/22258a26bc) [#53675](https://github.com/vllm-project/vllm/pull/53675)
  [Multimodal] Use GPU NVDEC for EPD encoder-only instance video media IO (#53675)
  _Files: `tests/config/test_multimodal_config.py`, `tests/multimodal/media/test_video.py`, `tests/multimodal/test_hasher.py`, `tests/multimodal/test_parse.py` _+8 more__
- **2026-09-11** [`295ac4e52e`](https://github.com/vllm-project/vllm/commit/295ac4e52e) [#55326](https://github.com/vllm-project/vllm/pull/55326)
  [Bugfix][Multimodal] Parse decoded video frame lists as a single video (#55326)
  _Files: `tests/multimodal/test_parse.py`, `vllm/multimodal/parse.py`_
- **2026-09-11** [`5ff50f3996`](https://github.com/vllm-project/vllm/commit/5ff50f3996) [#56385](https://github.com/vllm-project/vllm/pull/56385)
  [Bugfix][MM] Fix swapped H/W in dummy video profiling inputs (#56385)
  _Files: `vllm/multimodal/processing/dummy_inputs.py`_
- **2026-09-10** [`a89de950a4`](https://github.com/vllm-project/vllm/commit/a89de950a4) [#56335](https://github.com/vllm-project/vllm/pull/56335)
  [CI/Build] Pin HyperCLOVAX V2 test model revision (#56335)
  _Files: `tests/models/registry.py`_
- **2026-09-10** [`a36dfc93cb`](https://github.com/vllm-project/vllm/commit/a36dfc93cb) [#56310](https://github.com/vllm-project/vllm/pull/56310)
  [Bugfix][Multimodal] Restore cached audio inputs with UUIDs (#56310)
  _Files: `tests/entrypoints/unit_tests/test_chat_utils.py`, `tests/multimodal/test_parse.py`, `vllm/entrypoints/chat_utils.py`, `vllm/multimodal/parse.py`_
- **2026-09-10** [`912d2e79fe`](https://github.com/vllm-project/vllm/commit/912d2e79fe) [#52598](https://github.com/vllm-project/vllm/pull/52598)
  [multimodal][feat] add torchaudio backend to AudioResampler (#52598)
  _Files: `tests/multimodal/test_audio.py`, `vllm/multimodal/audio.py`, `vllm/multimodal/parse.py`_
- **2026-09-10** [`442d36031c`](https://github.com/vllm-project/vllm/commit/442d36031c) [#42785](https://github.com/vllm-project/vllm/pull/42785)
  [MM][CG] Enable encoder CUDA Graph for MiniCPM-V (#42785)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py` _+22 more__
- **2026-09-10** [`479611c0c6`](https://github.com/vllm-project/vllm/commit/479611c0c6) [#56090](https://github.com/vllm-project/vllm/pull/56090)
  [Frontend][EPD] Use JSON arrays for multimodal metadata (#56090)
  _Files: `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/entrypoints/unit_tests/test_chat_utils.py`, `tests/utils_/test_collection_utils.py`, `tests/v1/ec_connector/unit/test_epd_proxy_round_robin.py` _+2 more__
- **2026-09-10** [`6e1d051fc9`](https://github.com/vllm-project/vllm/commit/6e1d051fc9) [#56038](https://github.com/vllm-project/vllm/pull/56038)
  [CI][XPU] skip test_models_text on XPU (#56038)
  _Files: `tests/models/multimodal/pooling/test_phi3v.py`_
- **2026-09-10** [`41cffa9af0`](https://github.com/vllm-project/vllm/commit/41cffa9af0) [#56174](https://github.com/vllm-project/vllm/pull/56174)
  [Rust Frontend] Strongly type wire dtypes and multimodal modalities (#56174)
  _Files: `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/multimodal/audio.rs`, `rust/src/chat/src/multimodal/expand.rs`, `rust/src/chat/src/multimodal/tensor.rs` _+11 more__
- **2026-09-09** [`22d95d1adc`](https://github.com/vllm-project/vllm/commit/22d95d1adc) [#55370](https://github.com/vllm-project/vllm/pull/55370)
  [Bugfix] Make `mm_device_do_normalize` encoder-cudagraph safe (#55370)
  _Files: `tests/models/multimodal/generation/test_qwen2_vl.py`, `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py`_
- **2026-09-09** [`719284fe15`](https://github.com/vllm-project/vllm/commit/719284fe15) [#56078](https://github.com/vllm-project/vllm/pull/56078)
  [Core][Model] Unify XD-RoPE into M-RoPE and derive the channel count (#56078)
  _Files: `tests/kernels/core/test_apply_rotary_emb.py`, `tests/models/transformers/test_backend.py`, `tests/transformers_utils/test_config.py`, `tests/v1/core/test_output.py` _+14 more__
- **2026-09-09** [`94848eda60`](https://github.com/vllm-project/vllm/commit/94848eda60) [#55893](https://github.com/vllm-project/vllm/pull/55893)
  [Bugfix] Fix unreachable None guard in Molmo2 get_candidate_target_fps (#55893)
  _Files: `vllm/multimodal/video.py`_
- **2026-09-09** [`474839f846`](https://github.com/vllm-project/vllm/commit/474839f846) [#55163](https://github.com/vllm-project/vllm/pull/55163)
  [CI/Build] Upload CPU nightly image to Docker Hub (#55163)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/publish-release-images.sh`, `.buildkite/scripts/push-nightly-builds-cpu.sh`_
- **2026-09-08** [`5af4cc33ec`](https://github.com/vllm-project/vllm/commit/5af4cc33ec) [#55941](https://github.com/vllm-project/vllm/pull/55941)
  [Bugfix] Fix OpenPangu multimodal embedding merge (#55941)
  _Files: `tests/models/multimodal/test_openpangu_vl.py`, `vllm/model_executor/models/openpangu_vl.py`_
- **2026-09-08** [`cb22234687`](https://github.com/vllm-project/vllm/commit/cb22234687) [#55889](https://github.com/vllm-project/vllm/pull/55889)
  [CI] Reuse ColQwen3 models across pooling tests (#55889)
  _Files: `tests/models/multimodal/pooling/test_colqwen3.py`_
- **2026-09-08** [`34b9899c8f`](https://github.com/vllm-project/vllm/commit/34b9899c8f) [#55878](https://github.com/vllm-project/vllm/pull/55878)
  [CI] Increase ColQwen3 pooling test memory budget on H200 MIG (#55878)
  _Files: `tests/models/multimodal/pooling/test_colqwen3.py`_
- **2026-09-08** [`782f36cd0c`](https://github.com/vllm-project/vllm/commit/782f36cd0c) [#55779](https://github.com/vllm-project/vllm/pull/55779)
  [Bugfix][InternVL] Stop the video parser consuming image_embeds (#55779)
  _Files: `vllm/model_executor/models/internvl.py`_
- **2026-09-07** [`51da0ca66c`](https://github.com/vllm-project/vllm/commit/51da0ca66c) [#55588](https://github.com/vllm-project/vllm/pull/55588)
  [CI/Build] Unskip ColQwen3 multimodal pooling tests on Transformers v5 (#55588)
  _Files: `tests/models/multimodal/pooling/test_colqwen3.py`_
- **2026-09-07** [`f7f060d253`](https://github.com/vllm-project/vllm/commit/f7f060d253) [#55642](https://github.com/vllm-project/vllm/pull/55642)
  [Bugfix][Audio] Restore soundfile-first automatic decoding (#55642)
  _Files: `docs/features/multimodal_inputs.md`, `tests/multimodal/media/test_audio.py`, `vllm/multimodal/media/audio.py`_
- **2026-09-07** [`ed29dfae6e`](https://github.com/vllm-project/vllm/commit/ed29dfae6e) [#52945](https://github.com/vllm-project/vllm/pull/52945)
  [XPU] Use fused_input_norm kernel in FusedInputNorm (#52945)
  _Files: `vllm/_xpu_ops.py`, `vllm/model_executor/models/vision.py`_

## Other  (31 commits)

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
- **2026-09-13** [`dec0b5d63f`](https://github.com/vllm-project/vllm/commit/dec0b5d63f) [#56676](https://github.com/vllm-project/vllm/pull/56676)
  [Bugfix] Skip Triton autotune inspection without Triton (#56676)
  _Files: `tests/model_executor/test_jit_warmup_triton_launcher.py`, `vllm/model_executor/warmup/jit_warmup_triton_helper.py`_
- **2026-09-13** [`0cf266a469`](https://github.com/vllm-project/vllm/commit/0cf266a469) [#56639](https://github.com/vllm-project/vllm/pull/56639)
  [Pooling] Support prompt embeddings in MRV2 decoder pooling (#56639)
  _Files: `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/pool/pooling_runner.py`_
- **2026-09-12** [`3bb23e2def`](https://github.com/vllm-project/vllm/commit/3bb23e2def) [#56332](https://github.com/vllm-project/vllm/pull/56332)
  [CI/Build] Add DSv4.1 auto-label rules and narrow DSv4 (#56332)
  _Files: `.github/mergify.yml`, `.github/workflows/issue_autolabel.yml`_
- **2026-09-12** [`9d3e991ece`](https://github.com/vllm-project/vllm/commit/9d3e991ece) [#56501](https://github.com/vllm-project/vllm/pull/56501)
  Add @arpera to CODEOWNERS of Structured Output (#56501)
  _Files: `.github/CODEOWNERS`_
- **2026-09-12** [`eed1f3d0c6`](https://github.com/vllm-project/vllm/commit/eed1f3d0c6) [#56378](https://github.com/vllm-project/vllm/pull/56378)
  [Rust Frontend] Support `generation` blocks in HF chat template (#56378)
  _Files: `rust/src/chat/src/renderer/hf/generation.rs`, `rust/src/chat/src/renderer/hf/mod.rs`, `rust/src/chat/src/renderer/hf/template.rs`_
- **2026-09-12** [`5f3e4b7447`](https://github.com/vllm-project/vllm/commit/5f3e4b7447) [#56546](https://github.com/vllm-project/vllm/pull/56546)
  Revert "[Agents] Link Triton skill to JIT kernel warmup guide" (#56546)
  _Files: `.agents/skills/triton-kernel-writing/SKILL.md`_
- **2026-09-11** [`c1b69aa0d4`](https://github.com/vllm-project/vllm/commit/c1b69aa0d4) [#55424](https://github.com/vllm-project/vllm/pull/55424)
  [Bugfix][KV Connector] Only enforce disk block alignment for O_DIRECT (#55424)
  _Files: `tests/v1/simple_kv_offload/test_worker.py`, `vllm/v1/simple_kv_offload/disk_backend.py`_
- **2026-09-11** [`00e5cda926`](https://github.com/vllm-project/vllm/commit/00e5cda926) [#56499](https://github.com/vllm-project/vllm/pull/56499)
  [Agents] Link Triton skill to JIT kernel warmup guide (#56499)
  _Files: `.agents/skills/triton-kernel-writing/SKILL.md`_
- **2026-09-11** [`d5a9d0f59b`](https://github.com/vllm-project/vllm/commit/d5a9d0f59b) [#48866](https://github.com/vllm-project/vllm/pull/48866)
  [Metrics] Consolidate Prometheus histogram bucket defaults into a single module (#48866)
  _Files: `tests/v1/metrics/test_histogram_buckets.py`, `vllm/v1/metrics/buckets.py`, `vllm/v1/metrics/loggers.py`_
- **2026-09-11** [`e3f755b732`](https://github.com/vllm-project/vllm/commit/e3f755b732) [#55352](https://github.com/vllm-project/vllm/pull/55352)
  [CPU] Speedup LM Head on Arm CPUs (#55352)
  _Files: `csrc/cpu/dnnl_helper.cpp`, `csrc/cpu/dnnl_helper.h`, `csrc/cpu/dnnl_kernels.cpp`, `tests/kernels/test_onednn.py`_
- **2026-09-11** [`fadfe1c7d4`](https://github.com/vllm-project/vllm/commit/fadfe1c7d4) [#55450](https://github.com/vllm-project/vllm/pull/55450)
  [Bugfix][Core] Retire Mamba states across null gaps (#55450)
  _Files: `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-09-11** [`e7edf17cea`](https://github.com/vllm-project/vllm/commit/e7edf17cea) [#56379](https://github.com/vllm-project/vllm/pull/56379)
  [EC] Automatically enable embedding inputs on EC/KV consumers (#56379)
  _Files: `vllm/config/vllm.py`_
- **2026-09-10** [`c9355e25e8`](https://github.com/vllm-project/vllm/commit/c9355e25e8) [#55942](https://github.com/vllm-project/vllm/pull/55942)
  [XPU][Bugfix] Add forward_xpu to Ernie4_5_VLRotaryEmbedding (#55942)
  _Files: `vllm/model_executor/layers/rotary_embedding/ernie45_vl_rope.py`_
- **2026-09-10** [`3735c2d5f5`](https://github.com/vllm-project/vllm/commit/3735c2d5f5) [#56058](https://github.com/vllm-project/vllm/pull/56058)
  [Security][Rust Frontend] Normalize HTTP method labels in metrics (#56058)
  _Files: `rust/src/server/src/middleware/metrics.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-09-10** [`285cbce6bd`](https://github.com/vllm-project/vllm/commit/285cbce6bd) [#56018](https://github.com/vllm-project/vllm/pull/56018)
  [Rust Frontend] Resolve unified and split parser selections consistently (#56018)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/parser/mod.rs` _+6 more__
- **2026-09-09** [`26fec6d183`](https://github.com/vllm-project/vllm/commit/26fec6d183) [#53174](https://github.com/vllm-project/vllm/pull/53174)
  [Bugfix] Fix Step-3.5 reasoning parser for structured outputs (#53174)
  _Files: `tests/reasoning/test_step3p5_reasoning_parser.py`, `vllm/reasoning/step3p5_reasoning_parser.py`_
- **2026-09-09** [`c7e9816c6a`](https://github.com/vllm-project/vllm/commit/c7e9816c6a) [#55240](https://github.com/vllm-project/vllm/pull/55240)
  [Bugfix][Rust Frontend] Skip undefined token ids in decode and anchor them zero-width (#55240)
  _Files: `rust/src/tokenizer/src/hf.rs`, `rust/src/tokenizer/src/incremental.rs`_
- **2026-09-09** [`68dcc4fd86`](https://github.com/vllm-project/vllm/commit/68dcc4fd86) [#55328](https://github.com/vllm-project/vllm/pull/55328)
  [Rust Frontend] Make --max-model-len optional for the render server (#55328)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/server/src/render.rs`, `rust/src/server/src/routes/render.rs` _+1 more__
- **2026-09-08** [`c268198715`](https://github.com/vllm-project/vllm/commit/c268198715) [#55472](https://github.com/vllm-project/vllm/pull/55472)
  [Bugfix][Spec Decode] Preserve target parallel config (DCP) for DSpark (#55472)
  _Files: `vllm/v1/worker/gpu/spec_decode/dspark/utils.py`_
- **2026-09-08** [`bfb443a6b6`](https://github.com/vllm-project/vllm/commit/bfb443a6b6) [#55924](https://github.com/vllm-project/vllm/pull/55924)
  [Kimi Bug] Fix kda ima `Triton Error [CUDA]: an illegal memory access was encountered` (#55924)
  _Files: `vllm/models/kimi_k3/nvidia/kda.py`_
- **2026-09-08** [`18615ad1ee`](https://github.com/vllm-project/vllm/commit/18615ad1ee) [#55949](https://github.com/vllm-project/vllm/pull/55949)
  [Bugfix] Handle null RoPE parameters for NoPE layers (#55949)
  _Files: `tests/test_config.py`, `tests/transformers_utils/test_config.py`, `vllm/config/model.py`, `vllm/transformers_utils/config.py`_
- **2026-09-08** [`f998862d46`](https://github.com/vllm-project/vllm/commit/f998862d46) [#53379](https://github.com/vllm-project/vllm/pull/53379)
  [Bugfix] Fix Kimi K3 loading with interleaved weight streams (#53379)
  _Files: `tests/models/kimi_k3/test_weight_loading.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-09-08** [`9ea8f3ffc3`](https://github.com/vllm-project/vllm/commit/9ea8f3ffc3) [#55307](https://github.com/vllm-project/vllm/pull/55307)
  [Bugfix] Honor STEP token pooling in DispatchPooler.for_seq_cls (#55307)
  _Files: `examples/pooling/token_classify/forced_alignment_online.py`, `tests/model_executor/layers/test_pooler_methods.py`, `vllm/model_executor/layers/pooler/special.py`_
- **2026-09-08** [`9c297e3b8b`](https://github.com/vllm-project/vllm/commit/9c297e3b8b) [#55755](https://github.com/vllm-project/vllm/pull/55755)
  [Kernel] PDL enablement for fusedQKNormRopeKernel (#55755)
  _Files: `csrc/libtorch_stable/fused_qknorm_rope_kernel.cu`_
- **2026-09-08** [`869f78732b`](https://github.com/vllm-project/vllm/commit/869f78732b) [#55747](https://github.com/vllm-project/vllm/pull/55747)
  [Kimi Bug] Fix kimi k3 AssertionError assert 0 <= checkpoint_idx < len(blocks) (#55747)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-09-07** [`252ed87621`](https://github.com/vllm-project/vllm/commit/252ed87621) [#55761](https://github.com/vllm-project/vllm/pull/55761)
  [Bugfix] Restore Responses validation error boundary (#55761)
  _Files: `vllm/renderers/online_renderer.py`_
- **2026-09-07** [`9cc7793e32`](https://github.com/vllm-project/vllm/commit/9cc7793e32) [#54022](https://github.com/vllm-project/vllm/pull/54022)
  [Bugfix] Gracefully handle unsupported reasoning_effort in chat templates (#54022)
  _Files: `tests/renderers/test_hf.py`, `vllm/renderers/hf.py`_

## MoE / Expert Parallel  (27 commits)

- **2026-09-14** [`79f0be21ff`](https://github.com/vllm-project/vllm/commit/79f0be21ff) [#56773](https://github.com/vllm-project/vllm/pull/56773)
  [Bugfix][CPU] Fix DeepSeek-R1 (FP8 MLA + MoE) correctness on CPU backend (#56773)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`, `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`_
- **2026-09-14** [`9f03b510c3`](https://github.com/vllm-project/vllm/commit/9f03b510c3) [#55914](https://github.com/vllm-project/vllm/pull/55914)
  [DSv4 Bug] fix dsv4 start up error `NotImplementedError: DeepSeek V4 MegaMoE currently requires expert parallel` (#55914)
  _Files: `vllm/config/speculative.py`_
- **2026-09-13** [`fa008bdccf`](https://github.com/vllm-project/vllm/commit/fa008bdccf) [#56464](https://github.com/vllm-project/vllm/pull/56464)
  [Perf][Kernel] Integrate DeepSelect TopK for the DSA sparse indexer (#56464)
  _Files: `CMakeLists.txt`, `cmake/external_projects/deepselect.cmake`, `setup.py`, `tests/kernels/test_top_k_per_row.py` _+4 more__
- **2026-09-13** [`aed894c190`](https://github.com/vllm-project/vllm/commit/aed894c190) [#56323](https://github.com/vllm-project/vllm/pull/56323)
  [6/N][warmup][DSv4] Migrate sampling, and DFlash JIT kernels (#56323)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/samplers.yaml`, `tests/model_executor/test_jit_warmup.py`, `tests/model_executor/test_jit_warmup_triton_launcher.py` _+23 more__
- **2026-09-12** [`1ee4be4dbc`](https://github.com/vllm-project/vllm/commit/1ee4be4dbc) [#56599](https://github.com/vllm-project/vllm/pull/56599)
  [CI] Update DeepSeek V4.1 MegaMoE routing test (#56599)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`_
- **2026-09-12** [`658c8131c7`](https://github.com/vllm-project/vllm/commit/658c8131c7) [#54985](https://github.com/vllm-project/vllm/pull/54985)
  [Elastic EP] Reuse CUDA graphs across reconfiguration (#54985)
  _Files: `requirements/kv_connectors.txt`, `tests/distributed/test_elastic_ep.py`, `tests/distributed/test_eplb_utils.py`, `vllm/config/parallel.py` _+18 more__
- **2026-09-12** [`dca96bf97b`](https://github.com/vllm-project/vllm/commit/dca96bf97b) [#54416](https://github.com/vllm-project/vllm/pull/54416)
  [Bugfix][Spec Decode] Avoid fastsafetensors deadlock for PP draft models (#54416)
  _Files: `tests/v1/spec_decode/test_draft_attention_backend_override.py`, `tests/v1/spec_decode/test_draft_moe_backend_override.py`, `vllm/v1/worker/gpu/spec_decode/dflash/utils.py`, `vllm/v1/worker/gpu/spec_decode/dspark/utils.py` _+2 more__
- **2026-09-11** [`8a7f98c8c3`](https://github.com/vllm-project/vllm/commit/8a7f98c8c3) [#53280](https://github.com/vllm-project/vllm/pull/53280)
  [Kernel][MoE] Optimize batched_moe_align_block_size with cooperative writes (#53280)
  _Files: `benchmarks/kernels/benchmark_moe_align_block_size.py`, `csrc/libtorch_stable/moe/moe_align_sum_kernels.cu`, `tests/kernels/moe/test_moe_align_block_size.py`_
- **2026-09-11** [`b5d4186300`](https://github.com/vllm-project/vllm/commit/b5d4186300) [#55548](https://github.com/vllm-project/vllm/pull/55548)
  [Bugfix][LoRA] Use stored rsLoRA scaling factor in MoE expert packing (#55548)
  _Files: `tests/lora/test_lora_weights.py`, `vllm/lora/lora_weights.py`_
- **2026-09-10** [`bdea2777ea`](https://github.com/vllm-project/vllm/commit/bdea2777ea) [#55579](https://github.com/vllm-project/vllm/pull/55579)
  [Bugfix][MoE] Fix batched CUTLASS workspace overallocation (#55579)
  _Files: `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`_
- **2026-09-10** [`7d8d71e989`](https://github.com/vllm-project/vllm/commit/7d8d71e989) [#43272](https://github.com/vllm-project/vllm/pull/43272)
  [Bugfix] Qwen3-VL(-MoE): pass architectures to with_hf_config for pipeline parallelism (#43272)
  _Files: `vllm/model_executor/models/qwen3_vl.py`, `vllm/model_executor/models/qwen3_vl_moe.py`_
- **2026-09-10** [`73fb19151f`](https://github.com/vllm-project/vllm/commit/73fb19151f) [#55465](https://github.com/vllm-project/vllm/pull/55465)
  [Fast Start] Support fp4 (#55465)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/model_executor/kernels/linear/nvfp4/cutlass.py`, `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py` _+10 more__
- **2026-09-10** [`fe26c705f7`](https://github.com/vllm-project/vllm/commit/fe26c705f7) [#55921](https://github.com/vllm-project/vllm/pull/55921)
  [Model] Add Bailing V3 VL support (#55921)
  _Files: `docs/models/supported_models.md`, `tests/model_executor/test_bailing_mrope.py`, `tests/models/multimodal/processing/test_bailing_moe_v3_vl.py`, `tests/models/multimodal/test_mapping.py` _+15 more__
- **2026-09-10** [`c3ccc0e957`](https://github.com/vllm-project/vllm/commit/c3ccc0e957) [#55355](https://github.com/vllm-project/vllm/pull/55355)
  [Model] Add DeepSeek-V4 CPU backend (#55355)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `benchmarks/kernels/cpu/benchmark_cpu_fused_moe.py`, `cmake/cpu_extension.cmake`, `csrc/cpu/sgl-kernels/common.h` _+43 more__
- **2026-09-09** [`83fe99399e`](https://github.com/vllm-project/vllm/commit/83fe99399e) [#55713](https://github.com/vllm-project/vllm/pull/55713)
  [Spec Decode] Add NVFP4 DSpark gathered top-k projection (#55713)
  _Files: `tests/v1/spec_decode/test_dspark_topk.py`, `vllm/model_executor/layers/quantization/modelopt.py`, `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`, `vllm/model_executor/models/qwen3_dspark.py`_
- **2026-09-09** [`cc4210f671`](https://github.com/vllm-project/vllm/commit/cc4210f671) [#55899](https://github.com/vllm-project/vllm/pull/55899)
  [Perf] Improve BF16x3 router GEMM accuracy and make it default on sm100 (#55899)
  _Files: `tests/kernels/test_bf16x3_router_gemm_cutedsl.py`, `vllm/config/kernel.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/layers/fused_moe/router/bf16x3_router_gemm_cutedsl.py` _+2 more__
- **2026-09-09** [`fc6b6e1feb`](https://github.com/vllm-project/vllm/commit/fc6b6e1feb) [#55417](https://github.com/vllm-project/vllm/pull/55417)
  [Rust Frontend] Correctly parse whitespace framing in model output (#55417)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/reasoning/mod.rs`, `rust/src/chat/src/parser/reasoning/tests.rs`, `rust/src/chat/tests/roundtrip.rs` _+32 more__
- **2026-09-08** [`9c2d21046b`](https://github.com/vllm-project/vllm/commit/9c2d21046b) [#54788](https://github.com/vllm-project/vllm/pull/54788)
  [Bugfix][Spec Decode] Honour the draft's moe_backend on Model Runner V2 (#54788)
  _Files: `tests/v1/spec_decode/test_draft_moe_backend_override.py`, `vllm/v1/worker/gpu/spec_decode/eagle/utils.py`_
- **2026-09-08** [`8e1f97e709`](https://github.com/vllm-project/vllm/commit/8e1f97e709) [#55890](https://github.com/vllm-project/vllm/pull/55890)
  [Qwen3.8-Flash-Next] Tune FP8 TP2/TP4 Triton MoE on B200 (#55890)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=512,N=160,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[32,32].json`, `vllm/model_executor/layers/fused_moe/configs/E=512,N=320,device_name=NVIDIA_B200,dtype=fp8_w8a8,block_shape=[64,64].json`_
- **2026-09-08** [`96eccb8f49`](https://github.com/vllm-project/vllm/commit/96eccb8f49) [#55453](https://github.com/vllm-project/vllm/pull/55453)
  [CI] Restore clean GPU state before OAI Triton MoE tests (#55453)
  _Files: `tests/kernels/moe/conftest.py`_
- **2026-09-08** [`7fa2c63796`](https://github.com/vllm-project/vllm/commit/7fa2c63796) [#55377](https://github.com/vllm-project/vllm/pull/55377)
  [Bugfix] Autotune FlashInfer deferred MoE decode kernels before CUDA graph capture (#55377)
  _Files: `tests/model_executor/test_flashinfer_autotune_warmup.py`, `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/utils/flashinfer.py`_
- **2026-09-08** [`12579c7f01`](https://github.com/vllm-project/vllm/commit/12579c7f01) [#54668](https://github.com/vllm-project/vllm/pull/54668)
  [Kernel][Perf] Tune H20 block-FP8 MoE low-batch configs (+21%) (#54668)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=256,N=256,device_name=NVIDIA_H20-3e,dtype=fp8_w8a8,block_shape=[128,128].json`_
- **2026-09-08** [`9dbdf8e9af`](https://github.com/vllm-project/vllm/commit/9dbdf8e9af) [#53163](https://github.com/vllm-project/vllm/pull/53163)
  [Bugfix][Quantization][MoE] Normalise an unset group_size on the compressed-tensors WNA16 MoE path (#53163)
  _Files: `tests/quantization/test_moe_wna16.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_wna16.py`_
- **2026-09-07** [`5e6f6a8ed4`](https://github.com/vllm-project/vllm/commit/5e6f6a8ed4) [#52651](https://github.com/vllm-project/vllm/pull/52651)
  [Bugfix][Quantization][XPU] Fix moe_wna16 linear weight loading (#52651)
  _Files: `tests/quantization/test_moe_wna16.py`, `vllm/model_executor/layers/quantization/moe_wna16.py`, `vllm/platforms/xpu.py`_
- **2026-09-07** [`9b85112e13`](https://github.com/vllm-project/vllm/commit/9b85112e13) [#53580](https://github.com/vllm-project/vllm/pull/53580)
  [XPU] Route grouped_topk to the fused _moe_C kernel on XPU (#53580)
  _Files: `vllm/_custom_ops.py`, `vllm/model_executor/layers/fused_moe/router/grouped_topk_router.py`_
- **2026-09-07** [`5893426b88`](https://github.com/vllm-project/vllm/commit/5893426b88) [#53586](https://github.com/vllm-project/vllm/pull/53586)
  [Bugfix] DSv4 MXFP4 selector: stop narrowing explicit aliases to their BF16 variant (#53586)
  _Files: `tests/kernels/moe/test_b12x.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-09-07** [`6748217fb9`](https://github.com/vllm-project/vllm/commit/6748217fb9) [#55407](https://github.com/vllm-project/vllm/pull/55407)
  [Bugfix] Fix Kimi K3 NVFP4 MoE weight conversion OOM (#55407)
  _Files: `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`_

## Disaggregation / PD  (26 commits)

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
- **2026-09-13** [`319cc5ef19`](https://github.com/vllm-project/vllm/commit/319cc5ef19) [#56657](https://github.com/vllm-project/vllm/pull/56657)
  [Performance][EPD] Reduce Python proxy serialization overhead (#56657)
  _Files: `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/v1/ec_connector/unit/test_epd_proxy_retry.py`_
- **2026-09-13** [`7fe8fc803d`](https://github.com/vllm-project/vllm/commit/7fe8fc803d) [#56645](https://github.com/vllm-project/vllm/pull/56645)
  [NIXL][PCP][DCP] Expose PCP producer KV shards as transfer ranks (#56645)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `tests/v1/kv_connector/unit/test_tp_mapping.py`, `tests/v1/kv_connector/unit/utils.py` _+9 more__
- **2026-09-12** [`e19a3e172e`](https://github.com/vllm-project/vllm/commit/e19a3e172e) [#56629](https://github.com/vllm-project/vllm/pull/56629)
  [5/N] Share HiSparse host cache across TP ranks (reopens #52760) (#56629)
  _Files: `docs/design/hisparse.md`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `tests/v1/kv_offload/cpu/test_shared_offload_region.py` _+10 more__
- **2026-09-12** [`29332cf936`](https://github.com/vllm-project/vllm/commit/29332cf936) [#56061](https://github.com/vllm-project/vllm/pull/56061)
  [4/N] Expose HiSparse cache metrics via KV connector stats (#56061)
  _Files: `csrc/libtorch_stable/hisparse_kernels.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `tests/v1/kv_connector/unit/test_hisparse_stats.py` _+5 more__
- **2026-09-12** [`372477d2d9`](https://github.com/vllm-project/vllm/commit/372477d2d9) [#55088](https://github.com/vllm-project/vllm/pull/55088)
  [Bugfix][Examples] Launch prefill and decode concurrently in NixlPushConnector demo (#55088)
  _Files: `examples/disaggregated/disaggregated_serving/disagg_proxy_pushconnector_demo.py`_
- **2026-09-12** [`56d7270138`](https://github.com/vllm-project/vllm/commit/56d7270138) [#54689](https://github.com/vllm-project/vllm/pull/54689)
  [Bugfix][NIXL] Don't evict a remote engine a transfer is still reading from (#54689)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-09-11** [`ce08bb5b34`](https://github.com/vllm-project/vllm/commit/ce08bb5b34) [#56033](https://github.com/vllm-project/vllm/pull/56033)
  [Bugfix][Mooncake] Fix heterogeneous PP transfer completion (#56033)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-09-11** [`07b7553465`](https://github.com/vllm-project/vllm/commit/07b7553465) [#54736](https://github.com/vllm-project/vllm/pull/54736)
  [Feature][SimpleCPU] Load fine-grained hybrid prefix hits (#54736)
  _Files: `tests/v1/simple_kv_offload/test_kv_events.py`, `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/simple_cpu_offload_connector.py`, `vllm/v1/core/kv_cache_coordinator.py` _+2 more__
- **2026-09-10** [`7cdd9304ae`](https://github.com/vllm-project/vllm/commit/7cdd9304ae) [#55531](https://github.com/vllm-project/vllm/pull/55531)
  [KV Connector] Support symmetric DCP disagg for hybrid mamba models (#55531)
  _Files: `vllm/config/parallel.py`, `vllm/config/vllm.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py` _+1 more__
- **2026-09-10** [`93911fcf68`](https://github.com/vllm-project/vllm/commit/93911fcf68) [#53903](https://github.com/vllm-project/vllm/pull/53903)
  [NIXL][PCP] Report replicated-PCP ranks > 0 as done sending instead of hiding them (#53903)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py`_
- **2026-09-09** [`138d137b5b`](https://github.com/vllm-project/vllm/commit/138d137b5b) [#52615](https://github.com/vllm-project/vllm/pull/52615)
  [Refactor][kv_offload]: rename `block`→`chunk` (#52615)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_metrics.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_offload/cpu/policies/test_factory.py` _+30 more__
- **2026-09-09** [`9ffb8cea96`](https://github.com/vllm-project/vllm/commit/9ffb8cea96) [#54973](https://github.com/vllm-project/vllm/pull/54973)
  [CI] Add e2e test for scale-out EC connector flow (#54973)
  _Files: `.buildkite/test_areas/disaggregated_ec.yaml`, `tests/entrypoints/scale_out/ec_integration/README.md`, `tests/entrypoints/scale_out/ec_integration/run_scale_out_ec_e2e_test.sh`, `tests/entrypoints/scale_out/ec_integration/test_scale_out_ec_e2e.py` _+1 more__
- **2026-09-09** [`d2906091bf`](https://github.com/vllm-project/vllm/commit/d2906091bf) [#52516](https://github.com/vllm-project/vllm/pull/52516)
  [Bugfix] Fix Mooncake heterogeneous TP with replicated GQA heads (#52516)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-09-09** [`bf7eee9d7b`](https://github.com/vllm-project/vllm/commit/bf7eee9d7b) [#40416](https://github.com/vllm-project/vllm/pull/40416)
  [Bugfix][EC Connector] Fix ECExampleConnector load device under TP>1 (#40416)
  _Files: `tests/v1/ec_connector/unit/test_ec_example_connector.py`, `vllm/distributed/ec_transfer/ec_connector/example_connector.py`_
- **2026-09-09** [`41541636fd`](https://github.com/vllm-project/vllm/commit/41541636fd) [#54033](https://github.com/vllm-project/vllm/pull/54033)
  [Refactor][EC Connector] Add backend extension points to ECCPUWorker (#54033)
  _Files: `tests/v1/ec_connector/unit/cpu/worker/test_worker.py`, `vllm/distributed/ec_transfer/ec_connector/cpu/worker/__init__.py`_
- **2026-09-09** [`f1aeff6007`](https://github.com/vllm-project/vllm/commit/f1aeff6007) [#55290](https://github.com/vllm-project/vllm/pull/55290)
  [Bugfix][EC Connector] Fail the request, not the engine, when a remote encoding cannot arrive (#55290)
  _Files: `tests/v1/ec_connector/integration/README.md`, `tests/v1/ec_connector/integration/test_nixl_failure.py`, `tests/v1/ec_connector/unit/test_scheduler_nixl_consumer.py`, `tests/v1/ec_connector/unit/test_scheduler_nixl_producer.py` _+4 more__
- **2026-09-09** [`0b066293f3`](https://github.com/vllm-project/vllm/commit/0b066293f3) [#54853](https://github.com/vllm-project/vllm/pull/54853)
  [Core][KV Connector] Resolve connector block tables for every scheduled request (#54853)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `tests/v1/kv_connector/unit/test_scheduler_kv_connector_override.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/scheduler.py` _+2 more__
- **2026-09-09** [`4aadb0f14d`](https://github.com/vllm-project/vllm/commit/4aadb0f14d) [#53491](https://github.com/vllm-project/vllm/pull/53491)
  [Core] Enhance cpu<->gpu sync checking to include paged async copies (#53491)
  _Files: `tests/utils_/test_gpu_sync_debug.py`, `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`, `vllm/envs.py`, `vllm/model_executor/offloader/uva.py` _+1 more__
- **2026-09-08** [`e0aaef85f3`](https://github.com/vllm-project/vllm/commit/e0aaef85f3) [#53780](https://github.com/vllm-project/vllm/pull/53780)
  [2/N][KV Connector][NIXL] Support per-region transfer geometry (#53780)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py` _+5 more__
- **2026-09-07** [`49eb2accf0`](https://github.com/vllm-project/vllm/commit/49eb2accf0) [#47505](https://github.com/vllm-project/vllm/pull/47505)
  [KVConnector] Guard lmcache_mp_connector state transition with num_external_tokens (#47505)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`_
- **2026-09-07** [`34b1e9f7a6`](https://github.com/vllm-project/vllm/commit/34b1e9f7a6) [#54643](https://github.com/vllm-project/vllm/pull/54643)
  [Bugfix][MooncakeStore] Fix finish-time save crash on hybrid models (#54643)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/scheduler.py`_
- **2026-09-07** [`6fbb00b188`](https://github.com/vllm-project/vllm/commit/6fbb00b188) [#41567](https://github.com/vllm-project/vllm/pull/41567)
  [EPD] Add ECMooncakeConnector for encoder cache over Mooncake TransferEngine (#41567)
  _Files: `.buildkite/test_areas/disaggregated_mooncake.yaml`, `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/v1/core/test_encoder_cache_manager.py`, `tests/v1/core/test_scheduler.py` _+26 more__

## CI / Build  (25 commits)

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
- **2026-09-13** [`b6e2aa748b`](https://github.com/vllm-project/vllm/commit/b6e2aa748b) [#56707](https://github.com/vllm-project/vllm/pull/56707)
  [CI] Initialize warmup registry in V2 QSA runner fixture (#56707)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2.py`_
- **2026-09-13** [`de500290ff`](https://github.com/vllm-project/vllm/commit/de500290ff) [#56670](https://github.com/vllm-project/vllm/pull/56670)
  [XPU][CI] fix jit_warmup_triton_launcher (#56670)
  _Files: `tests/model_executor/test_jit_warmup_triton_launcher.py`_
- **2026-09-13** [`1cfd972816`](https://github.com/vllm-project/vllm/commit/1cfd972816) [#56672](https://github.com/vllm-project/vllm/pull/56672)
  [CI] Fix NIXL transfer-rank geometry fixture (#56672)
  _Files: `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`_
- **2026-09-12** [`dff76bc3e8`](https://github.com/vllm-project/vllm/commit/dff76bc3e8) [#55799](https://github.com/vllm-project/vllm/pull/55799)
  [Bugfix][CI] skip conftest for NPU compatibility test (#55799)
  _Files: `.buildkite/scripts/hardware_ci/run-npu-test.sh`_
- **2026-09-12** [`d86257e283`](https://github.com/vllm-project/vllm/commit/d86257e283) [#56596](https://github.com/vllm-project/vllm/pull/56596)
  [CI/Build] Give the Torch ABI audit time to start (#56596)
  _Files: `.buildkite/test_areas/torch_abi.yaml`_
- **2026-09-12** [`33fa95a0cf`](https://github.com/vllm-project/vllm/commit/33fa95a0cf) [#56541](https://github.com/vllm-project/vllm/pull/56541)
  [CI] Sample GPU utilization and memory alongside test timelines (#56541)
  _Files: `.buildkite/scripts/ci-otel/README.md`, `.buildkite/scripts/ci-otel/ci_gpu.py`, `.buildkite/scripts/ci-otel/ci_otel.py`, `.buildkite/scripts/ci-otel/ci_otel.sh` _+1 more__
- **2026-09-12** [`ec6b0494fe`](https://github.com/vllm-project/vllm/commit/ec6b0494fe) [#54927](https://github.com/vllm-project/vllm/pull/54927)
  [CI] Bump CUTLASS DSL to 4.7 (#54927)
  _Files: `cmake/external_projects/tml_fa4.cmake`, `requirements/cuda.txt`_
- **2026-09-11** [`dffb863c97`](https://github.com/vllm-project/vllm/commit/dffb863c97) [#56388](https://github.com/vllm-project/vllm/pull/56388)
  Upgrade tpu-inference to v0.29.0 (#56388)
  _Files: `requirements/tpu.txt`_
- **2026-09-11** [`e6821ceac9`](https://github.com/vllm-project/vllm/commit/e6821ceac9) [#56355](https://github.com/vllm-project/vllm/pull/56355)
  [XPU][CI] Add decord to test requirements (#56355)
  _Files: `requirements/test/xpu.in`, `requirements/test/xpu.txt`_
- **2026-09-10** [`46bae7e98c`](https://github.com/vllm-project/vllm/commit/46bae7e98c) [#56247](https://github.com/vllm-project/vllm/pull/56247)
  [CI/Build][CPU] Fix flaky rust downloads, broken prune flag, and triton-cpu cache coupling (#56247)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test.sh`, `docker/Dockerfile.cpu`, `vllm/v1/worker/cpu_worker.py`_
- **2026-09-10** [`364679feab`](https://github.com/vllm-project/vllm/commit/364679feab) [#56264](https://github.com/vllm-project/vllm/pull/56264)
  [CI] Enable ruff `INP` to require `__init__.py` under `vllm/` (#56264)
  _Files: `pyproject.toml`_
- **2026-09-10** [`978c22f54b`](https://github.com/vllm-project/vllm/commit/978c22f54b) [#56014](https://github.com/vllm-project/vllm/pull/56014)
  [XPU] update triton-xpu 3.8.0 shim layer (#56014)
  _Files: `.buildkite/scripts/xpu/publish-triton-shim.sh`_
- **2026-09-09** [`385dce36bc`](https://github.com/vllm-project/vllm/commit/385dce36bc) [#54640](https://github.com/vllm-project/vllm/pull/54640)
  [CI/Build][Hardware][NVIDIA] Add public CUDA 13.4 Rubin build path (#54640)
  _Files: `docker/Dockerfile`, `docs/getting_started/installation/gpu.cuda.inc.md`, `requirements/rubin-prerelease.txt`_
- **2026-09-09** [`27b63fb8f8`](https://github.com/vllm-project/vllm/commit/27b63fb8f8) [#55852](https://github.com/vllm-project/vllm/pull/55852)
  [CI][XPU] skip test_sampling_mask_tensors_match_finite_support on XPU (#55852)
  _Files: `tests/v1/test_outputs.py`_
- **2026-09-09** [`21a117ad87`](https://github.com/vllm-project/vllm/commit/21a117ad87) [#55965](https://github.com/vllm-project/vllm/pull/55965)
  [CI][IR] Speed up vLLM IR test group (#55965)
  _Files: `tests/ir/test_inplace_op.py`, `tests/ir/test_op.py`, `tests/kernels/ir/test_ir_ops.py`, `tests/kernels/ir/test_layernorm.py`_
- **2026-09-08** [`05e52f6336`](https://github.com/vllm-project/vllm/commit/05e52f6336) [#55877](https://github.com/vllm-project/vllm/pull/55877)
  [CI] Fix ARM64 test dependency builds with GCC 15 (#55877)
  _Files: `docker/Dockerfile.cpu`_
- **2026-09-08** [`808353f477`](https://github.com/vllm-project/vllm/commit/808353f477) [#52346](https://github.com/vllm-project/vllm/pull/52346)
  [CI] Split long misc test groups by command (#52346)
  _Files: `.buildkite/test_areas/misc.yaml`_
- **2026-09-08** [`06334fae2d`](https://github.com/vllm-project/vllm/commit/06334fae2d) [#55376](https://github.com/vllm-project/vllm/pull/55376)
  [Build] Remove obsolete TPU Dockerfile (#55376)
  _Files: `docker/Dockerfile.tpu`_
- **2026-09-07** [`58f09211dd`](https://github.com/vllm-project/vllm/commit/58f09211dd) [#55604](https://github.com/vllm-project/vllm/pull/55604)
  [CI] Synchronize shared offload unlink test before observing pathname (#55604)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`_
- **2026-09-07** [`ad2f18e8af`](https://github.com/vllm-project/vllm/commit/ad2f18e8af) [#55731](https://github.com/vllm-project/vllm/pull/55731)
  [CI] reduce npu CI use time and add timeout (#55731)
  _Files: `.buildkite/hardware_tests/ascend_npu.yaml`, `.buildkite/scripts/hardware_ci/run-npu-test.sh`_

## Serving / API  (22 commits)

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
- **2026-09-13** [`2e9f7bb454`](https://github.com/vllm-project/vllm/commit/2e9f7bb454) [#56573](https://github.com/vllm-project/vllm/pull/56573)
  [Pooling] Report actual input token usage for scoring APIs (#56573)
  _Files: `tests/models/language/pooling/test_max_tokens_per_doc.py`, `vllm/entrypoints/pooling/scoring/serving.py`_
- **2026-09-11** [`7ef4d9bfed`](https://github.com/vllm-project/vllm/commit/7ef4d9bfed) [#55305](https://github.com/vllm-project/vllm/pull/55305)
  [Bugfix][Responses] Fix browser.find action type (#55305)
  _Files: `tests/entrypoints/openai/responses/test_harmony_utils.py`, `tests/entrypoints/openai/responses/test_streaming_events.py`, `vllm/entrypoints/openai/responses/harmony.py`, `vllm/entrypoints/openai/responses/streaming_events.py`_
- **2026-09-11** [`a2bc2ffb2c`](https://github.com/vllm-project/vllm/commit/a2bc2ffb2c) [#56415](https://github.com/vllm-project/vllm/pull/56415)
  [Bugfix][Pooling] Restore token limits for offline Jina scoring (#56415)
  _Files: `tests/entrypoints/pooling/scoring/test_jina_ranking_io_processor_unit.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`_
- **2026-09-11** [`69db1c26b4`](https://github.com/vllm-project/vllm/commit/69db1c26b4) [#56365](https://github.com/vllm-project/vllm/pull/56365)
  [CI/Build][Rust Frontend] Publish vllm-proto on crates.io (#56365)
  _Files: `.github/workflows/proto-crate.yml`, `.pre-commit-config.yaml`, `rust/Cargo.lock`, `rust/Cargo.toml` _+6 more__
- **2026-09-11** [`fe4d4109c2`](https://github.com/vllm-project/vllm/commit/fe4d4109c2) [#56369](https://github.com/vllm-project/vllm/pull/56369)
  [Frontend][last/N] Move all non-OpenAI content out of the OpenAI folder. (#56369)
  _Files: `tests/entrypoints/openai/test_async_tokenization.py`, `tests/entrypoints/serve/utils/test_sse_keep_alive.py`, `vllm/entrypoints/openai/chat_completion/api_router.py`, `vllm/entrypoints/openai/completion/api_router.py` _+1 more__
- **2026-09-10** [`360f33f61c`](https://github.com/vllm-project/vllm/commit/360f33f61c) [#55325](https://github.com/vllm-project/vllm/pull/55325)
  [Bugfix] Set stop_sequence explicitly in streaming message_delta event (#55325)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-09-10** [`ae71862c51`](https://github.com/vllm-project/vllm/commit/ae71862c51) [#56070](https://github.com/vllm-project/vllm/pull/56070)
  [Bugfix][Frontend] Check EC requirements for each metadata item (#56070)
  _Files: `tests/entrypoints/scale_out/token_in_token_out/test_mm_serde.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`_
- **2026-09-10** [`db723d245a`](https://github.com/vllm-project/vllm/commit/db723d245a) [#55710](https://github.com/vllm-project/vllm/pull/55710)
  [Bugfix] Honor explicit empty and zero CLI arguments (#55710)
  _Files: `vllm/entrypoints/cli/openai.py`_
- **2026-09-10** [`8c34a37232`](https://github.com/vllm-project/vllm/commit/8c34a37232) [#56103](https://github.com/vllm-project/vllm/pull/56103)
  [Refactor] Extract maybe_run_omni() and defer CLI imports past omni early-return (#56103)
  _Files: `vllm/entrypoints/cli/main.py`_
- **2026-09-09** [`56d001faf0`](https://github.com/vllm-project/vllm/commit/56d001faf0) [#53824](https://github.com/vllm-project/vllm/pull/53824)
  [Bugfix] Detect OpenAI content format when message.content is passed through macro parameters (#53824)
  _Files: `tests/renderers/test_hf.py`, `vllm/renderers/hf.py`_
- **2026-09-09** [`114abd1c11`](https://github.com/vllm-project/vllm/commit/114abd1c11) [#55974](https://github.com/vllm-project/vllm/pull/55974)
  [Bugfix][Frontend] Reject unsupported Responses API input items with 400 instead of 500 (#55974)
  _Files: `vllm/entrypoints/openai/responses/utils.py`_
- **2026-09-08** [`bf339618d1`](https://github.com/vllm-project/vllm/commit/bf339618d1) [#49104](https://github.com/vllm-project/vllm/pull/49104)
  [Misc] Bump `openai` to `>=2.25.0` to support namespace tools types (#49104)
  _Files: `requirements/common.txt`_
- **2026-09-08** [`6c73b08dec`](https://github.com/vllm-project/vllm/commit/6c73b08dec) [#55618](https://github.com/vllm-project/vllm/pull/55618)
  [Bugfix] reject string file on translation like transcription (#55618)
  _Files: `vllm/entrypoints/speech_to_text/translation/protocol.py`_
- **2026-09-07** [`fdfa0a1659`](https://github.com/vllm-project/vllm/commit/fdfa0a1659) [#55665](https://github.com/vllm-project/vllm/pull/55665)
  [Pooling] Honor request_id from request bodies (#55665)
  _Files: `tests/entrypoints/pooling/token_embed/test_online.py`, `vllm/entrypoints/pooling/base/serving.py`_
- **2026-09-07** [`ecd600d91e`](https://github.com/vllm-project/vllm/commit/ecd600d91e) [#55551](https://github.com/vllm-project/vllm/pull/55551)
  [Pooling] Honor max_embed_len for chunked embeddings (#55551)
  _Files: `vllm/entrypoints/pooling/base/protocol.py`_
- **2026-09-07** [`167858ea17`](https://github.com/vllm-project/vllm/commit/167858ea17) [#55701](https://github.com/vllm-project/vllm/pull/55701)
  [Frontend] Migrate Responses harmony input validation to VLLMValidationError (#55701)
  _Files: `tests/entrypoints/openai/responses/test_harmony_utils.py`, `tests/entrypoints/openai/responses/test_response_input_to_harmony.py`, `vllm/entrypoints/openai/responses/harmony.py`_
- **2026-09-07** [`6a2a2bb02b`](https://github.com/vllm-project/vllm/commit/6a2a2bb02b) [#50195](https://github.com/vllm-project/vllm/pull/50195)
  [Frontend] Add stateless /v1/responses/render endpoint (#50195)
  _Files: `docs/serving/online_serving/README.md`, `docs/serving/online_serving/renderer.md`, `docs/usage/security.md`, `tests/entrypoints/launchers/test_cli_args.py` _+15 more__
- **2026-09-07** [`7dbe386833`](https://github.com/vllm-project/vllm/commit/7dbe386833) [#50257](https://github.com/vllm-project/vllm/pull/50257)
  [Frontend] Migrate Responses API validation errors to VLLMValidationError (#50257)
  _Files: `tests/entrypoints/openai/parser/test_harmony_utils.py`, `tests/entrypoints/openai/responses/test_responses_utils.py`, `vllm/entrypoints/openai/parser/harmony_utils.py`, `vllm/entrypoints/openai/responses/utils.py`_

## Quantization  (20 commits)

- **2026-09-14** [`39545e475d`](https://github.com/vllm-project/vllm/commit/39545e475d) [#56394](https://github.com/vllm-project/vllm/pull/56394)
  Revert "[CI][XPU] Disable model runner V2 for XPU quantization test for some partially pre-quantized models" (#56394)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`_
- **2026-09-13** [`71888f507a`](https://github.com/vllm-project/vllm/commit/71888f507a) [#56688](https://github.com/vllm-project/vllm/pull/56688)
  [Perf] Avoid redundant conversions in FP8 dummy initialization (#56688)
  _Files: `vllm/model_executor/model_loader/weight_utils.py`_
- **2026-09-13** [`b7e0cdac5d`](https://github.com/vllm-project/vllm/commit/b7e0cdac5d) [#52501](https://github.com/vllm-project/vllm/pull/52501)
  [Bugfix] Detect unloaded NVFP4 weight scales with a NaN sentinel (#52501)
  _Files: `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-09-13** [`c2ea9f1a5f`](https://github.com/vllm-project/vllm/commit/c2ea9f1a5f) [#56478](https://github.com/vllm-project/vllm/pull/56478)
  [Kernel][Perf][Quantization] Fix odd-row performance cliff in per-token-group quantization (#56478)
  _Files: `csrc/libtorch_stable/quantization/w8a8/fp8/per_token_group_quant.cu`, `tests/kernels/quantization/test_per_token_group_quant.py`_
- **2026-09-13** [`533dbe424b`](https://github.com/vllm-project/vllm/commit/533dbe424b) [#55656](https://github.com/vllm-project/vllm/pull/55656)
  [Misc] Clean up fast loader daemon quant method verification (#55656)
  _Files: `vllm/model_executor/model_loader/base_loader.py`, `vllm/model_executor/model_loader/weight_cache/__init__.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py` _+1 more__
- **2026-09-12** [`7ee8a6dd01`](https://github.com/vllm-project/vllm/commit/7ee8a6dd01) [#56122](https://github.com/vllm-project/vllm/pull/56122)
  [watermarking] Dual-key gumbel-max watermarking for speculative decoding support (#56122)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `docs/features/watermarking.md`, `tests/engine/test_arg_utils.py`, `tests/evals/gsm8k/configs/Qwen3-4B-FP8-DSpark-watermark-TP2.yaml` _+24 more__
- **2026-09-12** [`7bcca16729`](https://github.com/vllm-project/vllm/commit/7bcca16729) [#56452](https://github.com/vllm-project/vllm/pull/56452)
  [Bugfix] Fix DeepGEMM FP8 warmup coverage (#56452)
  _Files: `tests/model_executor/test_deep_gemm_warmup.py`, `vllm/model_executor/kernels/linear/scaled_mm/BlockScaledMMLinearKernel.py`, `vllm/model_executor/kernels/linear/scaled_mm/deep_gemm.py`, `vllm/model_executor/warmup/deep_gemm_warmup.py`_
- **2026-09-12** [`c377114636`](https://github.com/vllm-project/vllm/commit/c377114636) [#56594](https://github.com/vllm-project/vllm/pull/56594)
  [Bugfix][CI] Update CuTeDSL indexer Q sentinel test for migrated wrappers (#56594)
  _Files: `tests/kernels/test_fused_indexer_q_rope_quant.py`, `vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py`_
- **2026-09-11** [`6376c601ed`](https://github.com/vllm-project/vllm/commit/6376c601ed) [#55681](https://github.com/vllm-project/vllm/pull/55681)
  [XPU][Tests] Enable test_per_token_group_quant_int8 on XPU (#55681)
  _Files: `tests/kernels/quantization/test_per_token_group_quant.py`_
- **2026-09-10** [`40e6042ec8`](https://github.com/vllm-project/vllm/commit/40e6042ec8) [#54574](https://github.com/vllm-project/vllm/pull/54574)
  [Feature][Spec Decode] MTP with separate (possibly quantized) lm head for nemotron (#54574)
  _Files: `vllm/config/speculative.py`, `vllm/model_executor/models/nemotron_h_mtp.py`_
- **2026-09-10** [`5c0aeb5954`](https://github.com/vllm-project/vllm/commit/5c0aeb5954) [#56179](https://github.com/vllm-project/vllm/pull/56179)
  [CI][XPU] Disable model runner V2 for XPU quantization test for some partially  pre-quantized models (#56179)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`_
- **2026-09-09** [`3116c5d06b`](https://github.com/vllm-project/vllm/commit/3116c5d06b) [#54371](https://github.com/vllm-project/vllm/pull/54371)
  [Qwen4Exp] Support UVA PLE-offload and Engram tensor parallelism (#54371)
  _Files: `tests/engine/test_arg_utils.py`, `tests/models/qwen4_exp/test_ple.py`, `tests/test_config.py`, `vllm/config/__init__.py` _+12 more__
- **2026-09-09** [`28a73ccfba`](https://github.com/vllm-project/vllm/commit/28a73ccfba) [#53319](https://github.com/vllm-project/vllm/pull/53319)
  [Kernel] Add NVFP4 support to the torch linear backend (#53319)
  _Files: `tests/models/quantization/test_nvfp4.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/nvfp4/pytorch.py`_
- **2026-09-08** [`8ebc5b0a18`](https://github.com/vllm-project/vllm/commit/8ebc5b0a18) [#55643](https://github.com/vllm-project/vllm/pull/55643)
  [Bugfix] Fix NVFP4 fused SiLU+mul scale allocation and global scale direction (#55643)
  _Files: `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/compile/passes/test_silu_mul_quant_manual_fusion.py`, `tests/kernels/quantization/test_silu_mul_nvfp4_quant.py` _+1 more__
- **2026-09-08** [`13cf9e05c1`](https://github.com/vllm-project/vllm/commit/13cf9e05c1) [#55170](https://github.com/vllm-project/vllm/pull/55170)
  [Perf][Quant][NVFP4] Prefer W4A4 linear kernels over weight-only ones on SM120/121 (#55170)
  _Files: `tests/kernels/quantization/test_nvfp4_kernel_selection.py`, `vllm/model_executor/kernels/linear/__init__.py`_
- **2026-09-08** [`607a6e48c5`](https://github.com/vllm-project/vllm/commit/607a6e48c5) [#55797](https://github.com/vllm-project/vllm/pull/55797)
  [CI/Build] Fix unused fake implementation testing (#55797)
  _Files: `tests/kernels/helion/test_dynamic_per_token_scaled_fp8_quant.py`, `tests/kernels/helion/test_fused_qk_norm_rope.py`, `tests/kernels/helion/test_per_token_group_fp8_quant.py`, `tests/kernels/helion/test_rms_norm_dynamic_per_token_quant.py` _+2 more__
- **2026-09-07** [`392db567b2`](https://github.com/vllm-project/vllm/commit/392db567b2) [#55660](https://github.com/vllm-project/vllm/pull/55660)
  [CI] [Test] skip test_wna16_cuda_high_bit_skips_humming on non-CUDA platforms (#55660)
  _Files: `tests/quantization/test_auto_round.py`_
- **2026-09-07** [`f43ef1531d`](https://github.com/vllm-project/vllm/commit/f43ef1531d) [#55630](https://github.com/vllm-project/vllm/pull/55630)
  [CI] fix pre-commit (#55630)
  _Files: `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8.cu`_
- **2026-09-07** [`294fbb4f59`](https://github.com/vllm-project/vllm/commit/294fbb4f59) [#52890](https://github.com/vllm-project/vllm/pull/52890)
  add 2/3/5/6/7 CUDA support in AutoRound format (#52890)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/inc.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_scheme.py`_
- **2026-09-07** [`4df80187b5`](https://github.com/vllm-project/vllm/commit/4df80187b5) [#55180](https://github.com/vllm-project/vllm/pull/55180)
  [Kernel] SM 12.x blockwise FP8: swizzle the CTA raster when the weight exceeds the L2 (#55180)
  _Files: `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8.cu`, `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh`, `tests/kernels/quantization/test_cutlass_scaled_mm.py`_

## Models  (19 commits)

- **2026-09-14** [`6623fe5b4e`](https://github.com/vllm-project/vllm/commit/6623fe5b4e) [#49417](https://github.com/vllm-project/vllm/pull/49417)
  [Bugfix] MiniCPM-V 4.6: fix ViT self-attn qkv weight loading (#49417)
  _Files: `vllm/model_executor/models/minicpmv4_6.py`_
- **2026-09-14** [`eb42686a30`](https://github.com/vllm-project/vllm/commit/eb42686a30) [#56299](https://github.com/vllm-project/vllm/pull/56299)
  [Bugfix][Frontend] Support Responses text types in DeepSeek V4.1 (#56299)
  _Files: `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`_
- **2026-09-13** [`e52be1a62d`](https://github.com/vllm-project/vllm/commit/e52be1a62d) [#50178](https://github.com/vllm-project/vllm/pull/50178)
  [9/N][warmup][DSv4] Migrate MHC TileLang kernels (#50178)
  _Files: `tests/kernels/test_mhc_jit_warmup.py`, `tests/kernels/test_mhc_kernels.py`, `vllm/model_executor/kernels/mhc/tilelang.py`, `vllm/model_executor/kernels/mhc/tilelang_kernels.py` _+5 more__
- **2026-09-12** [`fd7cd4b883`](https://github.com/vllm-project/vllm/commit/fd7cd4b883) [#56600](https://github.com/vllm-project/vllm/pull/56600)
  [CI] Fix Qwen3 Omni DSpark load test config (#56600)
  _Files: `tests/model_executor/test_qwen3_omni.py`_
- **2026-09-11** [`c191787a68`](https://github.com/vllm-project/vllm/commit/c191787a68) [#56446](https://github.com/vllm-project/vllm/pull/56446)
  [Bugfix] Align vLLM YaRN with Transformers and stop re-scaling max_model_len (#56446)
  _Files: `tests/test_config.py`, `tests/transformers_utils/test_config.py`, `vllm/config/model.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py` _+7 more__
- **2026-09-11** [`a5b714eee4`](https://github.com/vllm-project/vllm/commit/a5b714eee4) [#53699](https://github.com/vllm-project/vllm/pull/53699)
  [Bugfix] Fix Qwen3-VL and Cosmos3-Edge text architectures for CPU and pipeline parallelism (#53699)
  _Files: `vllm/model_executor/models/cosmos3_edge.py`_
- **2026-09-11** [`912dfb3758`](https://github.com/vllm-project/vllm/commit/912dfb3758) [#56017](https://github.com/vllm-project/vllm/pull/56017)
  [Bugfix][Scoring] Warn when serving original Qwen3 reranker without chat template (#56017)
  _Files: `tests/entrypoints/pooling/test_io_processor.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`_
- **2026-09-11** [`79c137c6ad`](https://github.com/vllm-project/vllm/commit/79c137c6ad) [#56260](https://github.com/vllm-project/vllm/pull/56260)
  [Bugfix][Rust Frontend][Renderer] Align DeepSeek tool-call arguments with deepseek-recipe (#56260)
  _Files: `rust/src/chat/src/renderer/deepseek.rs`, `rust/src/chat/src/renderer/deepseek_v4/tests.rs`_
- **2026-09-10** [`983b7e28c9`](https://github.com/vllm-project/vllm/commit/983b7e28c9) [#54192](https://github.com/vllm-project/vllm/pull/54192)
  [Bugfix] Avoid MistralCommonBackend for HF tokenizers (#54192)
  _Files: `tests/tokenizers_/test_registry.py`, `tests/v1/structured_output/test_mistral_common_tokenizer.py`, `vllm/tokenizers/hf.py`, `vllm/tokenizers/registry.py` _+3 more__
- **2026-09-10** [`f9083cb83a`](https://github.com/vllm-project/vllm/commit/f9083cb83a) [#54157](https://github.com/vllm-project/vllm/pull/54157)
  [Mypy] Fix typing for R/S models (#54157)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/radio.py`, `vllm/model_executor/models/registry.py`, `vllm/model_executor/models/roberta.py` _+11 more__
- **2026-09-10** [`6fd08c45e6`](https://github.com/vllm-project/vllm/commit/6fd08c45e6) [#55913](https://github.com/vllm-project/vllm/pull/55913)
  [XPU][Bugfix] Fix FalconH1 pipeline-parallel execution (#55913)
  _Files: `vllm/model_executor/models/falcon_h1.py`_
- **2026-09-09** [`4ebf61ebda`](https://github.com/vllm-project/vllm/commit/4ebf61ebda) [#56146](https://github.com/vllm-project/vllm/pull/56146)
  [Cohere] Bound remaining request priorities to the MessagePack int64 range (#56146)
  _Files: `vllm/entrypoints/cohere/protocol.py`, `vllm/entrypoints/generate/generative_scoring/serving.py`, `vllm/entrypoints/pooling/embed/protocol.py`_
- **2026-09-09** [`42d76ee35a`](https://github.com/vllm-project/vllm/commit/42d76ee35a) [#56112](https://github.com/vllm-project/vllm/pull/56112)
  [Docs] Fix griffe docstring indentation warning in `SupportsMRoPE` (#56112)
  _Files: `vllm/model_executor/models/interfaces.py`_
- **2026-09-09** [`95cf420ac1`](https://github.com/vllm-project/vllm/commit/95cf420ac1) [#56011](https://github.com/vllm-project/vllm/pull/56011)
  [CI][Test][Spec Decode] Fix CI failure of Qwen3 Omni DSpark loader mock (#56011)
  _Files: `tests/model_executor/test_qwen3_omni.py`_
- **2026-09-09** [`050f29caf1`](https://github.com/vllm-project/vllm/commit/050f29caf1) [#55411](https://github.com/vllm-project/vllm/pull/55411)
  [Rust Frontend] Simplify reasoning parser initialization and test organization (#55411)
  _Files: `rust/src/parser/src/reasoning/cohere_cmd.rs`, `rust/src/parser/src/reasoning/deepseek_r1.rs`, `rust/src/parser/src/reasoning/delimited.rs`, `rust/src/parser/src/reasoning/hy.rs` _+6 more__
- **2026-09-08** [`5133e1d285`](https://github.com/vllm-project/vllm/commit/5133e1d285) [#55735](https://github.com/vllm-project/vllm/pull/55735)
  [Frontend] Migrate input-validation errors to VLLMValidationError (harmony/mistral/chat_utils/params) (#55735)
  _Files: `tests/entrypoints/openai/test_render_parity.py`, `tests/entrypoints/unit_tests/test_chat_utils.py`, `tests/tokenizers_/test_mistral.py`, `vllm/entrypoints/chat_utils.py` _+3 more__
- **2026-09-07** [`70584f69b1`](https://github.com/vllm-project/vllm/commit/70584f69b1) [#54774](https://github.com/vllm-project/vllm/pull/54774)
  [Model] Add Cohere Compass model (#54774)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/cohere_compass.py`, `vllm/model_executor/models/registry.py`, `vllm/transformers_utils/config.py`_
- **2026-09-07** [`f2d45f26bd`](https://github.com/vllm-project/vllm/commit/f2d45f26bd) [#54917](https://github.com/vllm-project/vllm/pull/54917)
  [Bugfix][Gemma] Conditionally create KV projections/norms on KV-shared layers (#54917)
  _Files: `tests/models/language/generation/test_gemma.py`, `vllm/model_executor/models/gemma3n.py`, `vllm/model_executor/models/gemma4.py`_
- **2026-09-07** [`3dc7a68ce4`](https://github.com/vllm-project/vllm/commit/3dc7a68ce4) [#54797](https://github.com/vllm-project/vllm/pull/54797)
  [Perf] Extend Qwen Triton warmup to avoid first-request latency spikes (#54797)
  _Files: `tests/model_executor/test_mamba_triton_warmup.py`, `tests/model_executor/test_qwen_triton_warmup.py`, `tests/model_executor/test_qwen_vl_triton_warmup.py`, `vllm/model_executor/warmup/kernel_warmup.py` _+3 more__

## Speculative Decoding  (12 commits)

- **2026-09-14** [`c676e4930b`](https://github.com/vllm-project/vllm/commit/c676e4930b) [#55133](https://github.com/vllm-project/vllm/pull/55133)
  [Spec Decode] Fix Qwen3 DSpark d2t requirement for padded-vocab drafts (#55133)
  _Files: `tests/model_executor/test_qwen3_omni.py`, `vllm/model_executor/models/qwen3_dspark.py`_
- **2026-09-14** [`47fbd36e6d`](https://github.com/vllm-project/vllm/commit/47fbd36e6d) [#56791](https://github.com/vllm-project/vllm/pull/56791)
  [Bugfix] Trim stale consequence claims from unannotated-eagle warning (#56791)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-09-14** [`a5f6f61a8a`](https://github.com/vllm-project/vllm/commit/a5f6f61a8a) [#54934](https://github.com/vllm-project/vllm/pull/54934)
  [CI][CPU] Add speculative-decoding coverage to CPU CI (#54934)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/scripts/hardware_ci/run-cpu-test.sh`, `docs/features/README.md`, `tests/v1/e2e/test_cpu_spec_decode.py`_
- **2026-09-13** [`d2d649e674`](https://github.com/vllm-project/vllm/commit/d2d649e674) [#56512](https://github.com/vllm-project/vllm/pull/56512)
  [DS V4.1][Engram] Support async prefetch for offloaded engram lookups and engram DP sharding (#56512)
  _Files: `.buildkite/test_areas/distributed.yaml`, `tests/distributed/test_engram_dp_shard.py`, `tests/engine/test_arg_utils.py`, `tests/kernels/test_engram.py` _+8 more__
- **2026-09-13** [`e7a3963339`](https://github.com/vllm-project/vllm/commit/e7a3963339) [#56682](https://github.com/vllm-project/vllm/pull/56682)
  [Bugfix] Avoid repeated dummy initialization and random CPU Engram fills (#56682)
  _Files: `vllm/model_executor/model_loader/dummy_loader.py`, `vllm/model_executor/model_loader/weight_utils.py`, `vllm/models/deepseek_v4_1/common/engram.py`_
- **2026-09-10** [`b28c3e1568`](https://github.com/vllm-project/vllm/commit/b28c3e1568) [#54713](https://github.com/vllm-project/vllm/pull/54713)
  [BugFix] Retain both replay boundaries so an EAGLE resend of a block-aligned prompt still hits (#54713)
  _Files: `tests/v1/core/test_prefix_caching.py`, `tests/v1/core/test_single_type_kv_cache_manager.py`, `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-09-09** [`e8064a96d0`](https://github.com/vllm-project/vllm/commit/e8064a96d0) [#55745](https://github.com/vllm-project/vllm/pull/55745)
  [Bugfix][V2] record_stream idx_mapping in the PP draft broadcast (#55745)
  _Files: `vllm/v1/worker/gpu/pp_utils.py`_
- **2026-09-09** [`c55e15a44e`](https://github.com/vllm-project/vllm/commit/c55e15a44e) [#51450](https://github.com/vllm-project/vllm/pull/51450)
  [Structured Output] Keep invalid structured-output requests from stopping the engine (#51450)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/structured_output/test_guidance_negative_draft_tokens.py`, `tests/v1/structured_output/test_scheduler_speculative_padding.py`, `vllm/v1/core/sched/scheduler.py` _+2 more__
- **2026-09-08** [`263c4ff95f`](https://github.com/vllm-project/vllm/commit/263c4ff95f) [#53945](https://github.com/vllm-project/vllm/pull/53945)
  [Bugfix][Spec Decode] Cache the Mamba state at the block-grid position of EAGLE resume (#53945)
  _Files: `docs/features/automatic_prefix_caching.md`, `tests/v1/core/prefix_cache/test_mamba_eagle_resume_checkpoint.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_mamba_align_chunk_split.py` _+8 more__
- **2026-09-08** [`54da70c1eb`](https://github.com/vllm-project/vllm/commit/54da70c1eb) [#53052](https://github.com/vllm-project/vllm/pull/53052)
  [Feature] Support EAGLE3 for Sarvam (#53052)
  _Files: `vllm/model_executor/models/sarvam.py`_
- **2026-09-07** [`b339d75a41`](https://github.com/vllm-project/vllm/commit/b339d75a41) [#55369](https://github.com/vllm-project/vllm/pull/55369)
  [Bugfix][Spec Decode] Resolve n_predict from text_config for Qwen3.5 multimodal MTP (#55369)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_qwen3_5_mtp_config.py`, `vllm/config/speculative.py`_
- **2026-09-07** [`4a806d08ee`](https://github.com/vllm-project/vllm/commit/4a806d08ee) [#52771](https://github.com/vllm-project/vllm/pull/52771)
  [Bugfix] OffloadingConnector: stop zeroing offload hits under MTP/EAGLE spec decode (#52771)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_

## Scheduler / Engine  (12 commits)

- **2026-09-14** [`214248c7d8`](https://github.com/vllm-project/vllm/commit/214248c7d8) [#56695](https://github.com/vllm-project/vllm/pull/56695)
  [CI] Move smaller H200 workloads to 18GB MIG slices (#56695)
  _Files: `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/samplers.yaml`_
- **2026-09-12** [`22f6e4eccb`](https://github.com/vllm-project/vllm/commit/22f6e4eccb) [#54821](https://github.com/vllm-project/vllm/pull/54821)
  [Frontend][Rust] Reject empty structured-output values (#54821)
  _Files: `rust/src/engine-core-client/src/protocol/structured_outputs.rs`, `rust/src/server/src/grpc/convert.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/openai/utils/structured_outputs.rs`_
- **2026-09-11** [`988d9b6777`](https://github.com/vllm-project/vllm/commit/988d9b6777) [#56405](https://github.com/vllm-project/vllm/pull/56405)
  [Rust Frontend][gRPC] Surface engine generation errors (#56405)
  _Files: `rust/src/server/src/grpc/convert.rs`, `rust/src/server/src/grpc/inference.rs`, `rust/src/server/src/grpc/tests.rs`_
- **2026-09-11** [`84030bbe3d`](https://github.com/vllm-project/vllm/commit/84030bbe3d) [#49675](https://github.com/vllm-project/vllm/pull/49675)
  [Bugfix][Core] Stop zero-progress preemption cascades for deferred KV frees (#49675)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/test_deferred_block_free.py`, `tests/v1/core/utils.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-09-10** [`9e25706560`](https://github.com/vllm-project/vllm/commit/9e25706560) [#56141](https://github.com/vllm-project/vllm/pull/56141)
  [Bugfix] Tolerate misspelled DSML tool_calls wrapper (#56141)
  _Files: `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_delegating_replay.py`, `tests/parser/engine/test_engine.py`, `tests/parser/engine/test_replay.py` _+5 more__
- **2026-09-10** [`ea40bb9e90`](https://github.com/vllm-project/vllm/commit/ea40bb9e90) [#54053](https://github.com/vllm-project/vllm/pull/54053)
  [feature] Watermarked generation and detection (Gumbel-max algorithm) (#54053)
  _Files: `docs/features/watermarking.md`, `examples/basic/online_serving/watermark_detection_server.py`, `tests/engine/test_arg_utils.py`, `tests/entrypoints/openai/test_watermarking.py` _+28 more__
- **2026-09-09** [`65f3fca568`](https://github.com/vllm-project/vllm/commit/65f3fca568) [#54264](https://github.com/vllm-project/vllm/pull/54264)
  [Bugfix][Parser] Seed-OSS turn-boundary tokens + boundary-fallback tests (#54264)
  _Files: `tests/parser/engine/test_qwen3_reasoning.py`, `tests/parser/engine/test_seed_oss.py`, `vllm/parser/seed_oss.py`_
- **2026-09-09** [`c6ba5e89d6`](https://github.com/vllm-project/vllm/commit/c6ba5e89d6) [#55772](https://github.com/vllm-project/vllm/pull/55772)
  [Bugfix][Elastic EP] Route only to surviving engines during scale-down (#55772)
  _Files: `tests/v1/engine/test_engine_core_client.py`, `vllm/v1/engine/core_client.py`_
- **2026-09-09** [`d98c8c030b`](https://github.com/vllm-project/vllm/commit/d98c8c030b) [#55954](https://github.com/vllm-project/vllm/pull/55954)
  [Bugfix] Parse DSML tool calls when the model omits the tool_calls wrapper (#55954)
  _Files: `tests/parser/engine/test_deepseek_v32.py`, `tests/parser/engine/test_deepseek_v4.py`, `tests/tool_parsers/test_deepseekv4_tool_parser.py`, `vllm/parser/deepseek_v32.py` _+1 more__
- **2026-09-08** [`5db652225f`](https://github.com/vllm-project/vllm/commit/5db652225f) [#55606](https://github.com/vllm-project/vllm/pull/55606)
  [Bugfix] Validate extension integers before engine serialization (#55606)
  _Files: `tests/test_sampling_params.py`, `vllm/sampling_params.py`_
- **2026-09-07** [`cd64c2dea9`](https://github.com/vllm-project/vllm/commit/cd64c2dea9) [#55124](https://github.com/vllm-project/vllm/pull/55124)
  [Docs] Clarify admission control limits apply server-wide, not per DP rank (#55124)
  _Files: `docs/serving/data_parallel_deployment.md`, `vllm/config/scheduler.py`_
- **2026-09-07** [`c3ec0d29f5`](https://github.com/vllm-project/vllm/commit/c3ec0d29f5) [#55237](https://github.com/vllm-project/vllm/pull/55237)
  [Bugfix] Fix cuda profiler missing bug (#55237)
  _Files: `tests/v1/engine/test_async_llm.py`, `vllm/v1/engine/async_llm.py`_

## Docs  (9 commits)

- **2026-09-14** [`767d1c4d47`](https://github.com/vllm-project/vllm/commit/767d1c4d47) [#56467](https://github.com/vllm-project/vllm/pull/56467)
  [Docs] Move russellb to emeritus committer (#56467)
  _Files: `.github/CODEOWNERS`, `docs/contributing/vulnerability_management.md`, `docs/governance/committers.md`_
- **2026-09-11** [`9a35c081e8`](https://github.com/vllm-project/vllm/commit/9a35c081e8) [#56269](https://github.com/vllm-project/vllm/pull/56269)
  [Docs] Correct API key authentication scope (/inference does NOT bypass the API key) (#56269)
  _Files: `docs/usage/security.md`_
- **2026-09-11** [`5c642796e8`](https://github.com/vllm-project/vllm/commit/5c642796e8) [#56414](https://github.com/vllm-project/vllm/pull/56414)
  [Docs] Add Nebius Serverless AI deployment guide (#56414)
  _Files: `docs/deployment/frameworks/nebius.md`_
- **2026-09-10** [`3078e7cbe1`](https://github.com/vllm-project/vllm/commit/3078e7cbe1) [#56286](https://github.com/vllm-project/vllm/pull/56286)
  [Docs]: quote variable-bearing wheel URLs (#56286)
  _Files: `docs/getting_started/installation/cpu.arm.inc.md`, `docs/getting_started/installation/cpu.x86.inc.md`, `docs/getting_started/installation/gpu.cuda.inc.md`_
- **2026-09-10** [`e83d57d8ae`](https://github.com/vllm-project/vllm/commit/e83d57d8ae) [#51646](https://github.com/vllm-project/vllm/pull/51646)
  [Doc] Sync KV event medium terminology after #48123 (#51646)
  _Files: `docs/features/kv_offloading_usage.md`_
- **2026-09-10** [`08426d51ef`](https://github.com/vllm-project/vllm/commit/08426d51ef) [#55476](https://github.com/vllm-project/vllm/pull/55476)
  [Docs][Security] Clarify reporter credit and CVE publication timing (#55476)
  _Files: `SECURITY.md`, `docs/contributing/vulnerability_management.md`_
- **2026-09-09** [`de650b55af`](https://github.com/vllm-project/vllm/commit/de650b55af) [#54584](https://github.com/vllm-project/vllm/pull/54584)
  [Docs] Update README.md MkDocs to give option to run dev-server on different port. (#54584)
  _Files: `docs/contributing/README.md`, `docs/getting_started/installation/gpu.apple.inc.md`_
- **2026-09-09** [`a97dacb710`](https://github.com/vllm-project/vllm/commit/a97dacb710) [#54522](https://github.com/vllm-project/vllm/pull/54522)
  [Docs][EC Connector] CPU EC Connector usage Docs (#54522)
  _Files: `docs/features/ec_cpu_connector.md`_
- **2026-09-07** [`58ad1f3b89`](https://github.com/vllm-project/vllm/commit/58ad1f3b89) [#55691](https://github.com/vllm-project/vllm/pull/55691)
  [Docs] Add OLMo 2 to batch-invariance tested models (#55691)
  _Files: `docs/features/batch_invariance.md`_

## LoRA  (7 commits)

- **2026-09-14** [`663d7f679e`](https://github.com/vllm-project/vllm/commit/663d7f679e) [#53353](https://github.com/vllm-project/vllm/pull/53353)
  [Bugfix] Fix --lora-modules name=path parsing when path contains '=' (#53353)
  _Files: `vllm/entrypoints/launchers/cli_args.py`_
- **2026-09-12** [`80650454dc`](https://github.com/vllm-project/vllm/commit/80650454dc) [#56329](https://github.com/vllm-project/vllm/pull/56329)
  [CI] Give every Buildkite step an explicit key, and a hook to enforce it (#56329)
  _Files: `.buildkite/intel_jobs/basic_correctness_intel.yaml`, `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/kernels_intel.yaml`, `.buildkite/intel_jobs/lora_intel.yaml` _+8 more__
- **2026-09-09** [`a207d7ce1d`](https://github.com/vllm-project/vllm/commit/a207d7ce1d) [#55310](https://github.com/vllm-project/vllm/pull/55310)
  [Bugfix][LoRA] Log when an adapter applies no weights (#55310)
  _Files: `vllm/lora/model_manager.py`_
- **2026-09-09** [`af51d0ef03`](https://github.com/vllm-project/vllm/commit/af51d0ef03) [#56004](https://github.com/vllm-project/vllm/pull/56004)
  [Pooling] Report LoRA adapter names in responses (#56004)
  _Files: `vllm/entrypoints/pooling/base/serving.py`, `vllm/entrypoints/pooling/scoring/serving.py`_
- **2026-09-08** [`29f46ac475`](https://github.com/vllm-project/vllm/commit/29f46ac475) [#55223](https://github.com/vllm-project/vllm/pull/55223)
  [Perf] Eliminate full-history reasoning scans for structured outputs (#55223)
  _Files: `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_parser_engine.py`, `tests/v1/spec_decode/test_mtp_structured_output.py`, `tests/v1/structured_output/test_reasoning_structured_output.py` _+4 more__
- **2026-09-08** [`b105d8284f`](https://github.com/vllm-project/vllm/commit/b105d8284f) [#55865](https://github.com/vllm-project/vllm/pull/55865)
  [LoRA] Clarify target module matching logic (#55865)
  _Files: `vllm/lora/model_manager.py`_
- **2026-09-07** [`8648446515`](https://github.com/vllm-project/vllm/commit/8648446515) [#53689](https://github.com/vllm-project/vllm/pull/53689)
  [XPU][LoRA] Support LoRA for DeepSeek V4 on XPU (#53689)
  _Files: `vllm/models/deepseek_v4/xpu/model.py`_

## Perf / Benchmark  (7 commits)

- **2026-09-14** [`3b533197a9`](https://github.com/vllm-project/vllm/commit/3b533197a9) [#56683](https://github.com/vllm-project/vllm/pull/56683)
  [Perf] Parallelize mHC pre-norm JIT warmup (#56683)
  _Files: `vllm/model_executor/kernels/mhc/warmup.py`, `vllm/model_executor/warmup/jit_warmup.py`_
- **2026-09-13** [`93e051e290`](https://github.com/vllm-project/vllm/commit/93e051e290) [#55508](https://github.com/vllm-project/vllm/pull/55508)
  [Bugfix][Benchmark] Make streaming TTFT/E2E latency accounting consistent across endpoints (#55508)
  _Files: `benchmarks/backend_request_func.py`, `tests/benchmarks/test_endpoint_request_func_timing.py`, `vllm/benchmarks/lib/endpoint_request_func.py`_
- **2026-09-11** [`0c1e89ceb9`](https://github.com/vllm-project/vllm/commit/0c1e89ceb9) [#55426](https://github.com/vllm-project/vllm/pull/55426)
  [Bugfix][Kimi-K3] Fix KDA projection overlap on Hopper (#55426)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py`_
- **2026-09-11** [`9dcab80215`](https://github.com/vllm-project/vllm/commit/9dcab80215) [#56300](https://github.com/vllm-project/vllm/pull/56300)
  [Bugfix][Bench] Fix bench mm-processor crash in shared request sampling (#56300)
  _Files: `tests/benchmarks/test_throughput_cli.py`, `vllm/benchmarks/throughput.py`_
- **2026-09-10** [`2e0ee66cab`](https://github.com/vllm-project/vllm/commit/2e0ee66cab) [#55819](https://github.com/vllm-project/vllm/pull/55819)
  [Perf] Use UVA-backed contents for MRV2 apply_write (#55819)
  _Files: `tests/kernels/core/test_uva.py`, `vllm/v1/worker/gpu/buffer_utils.py`_
- **2026-09-10** [`86aca66191`](https://github.com/vllm-project/vllm/commit/86aca66191) [#56159](https://github.com/vllm-project/vllm/pull/56159)
  [Kimi K3 Perf] Avoid KDA mixed-batch gather/scatter, 5.2%~7.7% E2E Throughput Improvement (#56159)
  _Files: `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py` _+2 more__
- **2026-09-08** [`0a742da274`](https://github.com/vllm-project/vllm/commit/0a742da274) [#55223](https://github.com/vllm-project/vllm/pull/55223)
  [Perf] Eliminate full-history reasoning scans for structured outputs (#55223)

## KV Cache / Offload  (5 commits)

- **2026-09-14** [`c612e2bff0`](https://github.com/vllm-project/vllm/commit/c612e2bff0) [#55823](https://github.com/vllm-project/vllm/pull/55823)
  [Bugfix][KV Offload] Reuse in-flight async lookup probes (#55823)
  _Files: `tests/v1/kv_offload/tiering/test_async_lookup.py`, `vllm/v1/kv_offload/tiering/async_lookup.py`_
- **2026-09-13** [`c351fd3c64`](https://github.com/vllm-project/vllm/commit/c351fd3c64) [#50388](https://github.com/vllm-project/vllm/pull/50388)
  [Core] Fix ValueError on KV load failure with a hybrid KV cache (#50388)
  _Files: `tests/v1/kv_connector/unit/test_kv_load_failure_recovery.py`, `tests/v1/kv_connector/unit/utils.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-09-13** [`410f6da5c4`](https://github.com/vllm-project/vllm/commit/410f6da5c4) [#56621](https://github.com/vllm-project/vllm/pull/56621)
  [Bugfix][KV Offload] Submit CPU stores on no-forward steps (#56621)
  _Files: `tests/v1/simple_kv_offload/test_worker.py`, `vllm/v1/simple_kv_offload/worker.py`_
- **2026-09-08** [`5ebce2391e`](https://github.com/vllm-project/vllm/commit/5ebce2391e) [#54998](https://github.com/vllm-project/vllm/pull/54998)
  [Bugfix][KV Offload] Respect prefix-cache bypass in SimpleCPUOffload (#54998)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-09-08** [`81dabe2e5d`](https://github.com/vllm-project/vllm/commit/81dabe2e5d) [#55712](https://github.com/vllm-project/vllm/pull/55712)
  [Bugfix][KV Offload] Validate SWA coverage at unaligned cache-hit boundaries (#55712)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_

## Compilation / CUDA Graph  (4 commits)

- **2026-09-14** [`73d2a8cf86`](https://github.com/vllm-project/vllm/commit/73d2a8cf86) [#51700](https://github.com/vllm-project/vllm/pull/51700)
  [2/2][Model Runner V2] FULL CUDA graph capture for microbatched steps (DBO) (#51700)
  _Files: `tests/v1/worker/test_gpu_ubatch_slicing.py`, `vllm/config/vllm.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/dp_utils.py` _+2 more__
- **2026-09-11** [`cc5dd0a857`](https://github.com/vllm-project/vllm/commit/cc5dd0a857) [#56312](https://github.com/vllm-project/vllm/pull/56312)
  [MRV1] Scope breakable cudagraphs to the piecewise path only (#56312)
  _Files: `tests/v1/cudagraph/test_breakable_cudagraph.py`, `vllm/compilation/breakable_cudagraph.py`, `vllm/compilation/cuda_graph.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-09-11** [`89dbb26445`](https://github.com/vllm-project/vllm/commit/89dbb26445) [#56447](https://github.com/vllm-project/vllm/pull/56447)
  [Bugfix] Fix GLM-OCR MTP position masking during CUDA graph capture (#56447)
  _Files: `vllm/model_executor/models/glm_ocr_mtp.py`_
- **2026-09-08** [`07950d4734`](https://github.com/vllm-project/vllm/commit/07950d4734) [#55774](https://github.com/vllm-project/vllm/pull/55774)
  [Kimi Bug] Fix kimi k3 startup cuda graph issue with recoverSSM (#55774)
  _Files: `tests/v1/cudagraph/test_cudagraph_manager.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`_

---
_Generated 2026-09-14 15:04 UTC_