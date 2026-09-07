# sgl-project/sglang — Weekly Change Report
**Period:** 2026-08-31 → 2026-09-07  |  **Total commits:** 421

## ✨ New Features This Week

- **2026-09-07** [#38295](https://github.com/sgl-project/sglang/pull/38295) — Add MiniCPM5-2B cookbook (#38295)
- **2026-09-07** [#37373](https://github.com/sgl-project/sglang/pull/37373) — [NPU] Add NPU arch35 support and enhance DSV4 processing in DeepSeek-V4 (#37373)
- **2026-09-07** [#37691](https://github.com/sgl-project/sglang/pull/37691) — [AMD] Support aiter fa mha chunked kv for Kimi-K3 (#37691)
- **2026-09-07** [#36654](https://github.com/sgl-project/sglang/pull/36654) — [XPU] Re-add intel xpu on triton paths in diffusion platforms  (#36654)
- **2026-09-07** [#37376](https://github.com/sgl-project/sglang/pull/37376) — [kernel] add fused silu mul quant fp8 (#37376)
- **2026-09-07** [#31113](https://github.com/sgl-project/sglang/pull/31113) — [Intel][XPU] Add NUMA node binding support for Intel XPU (#31113)
- **2026-09-07** [#30430](https://github.com/sgl-project/sglang/pull/30430) — Fuse Nemotron latent MoE projection and shared add (#30430)
- **2026-09-07** [#37601](https://github.com/sgl-project/sglang/pull/37601) — [AMD] support qlen>1 for aiter gluon path for Kimi K3 (#37601)
- **2026-09-07** [#24959](https://github.com/sgl-project/sglang/pull/24959) — XPU: Enable GLM5.1 (GlmMoeDsaForCausalLM) DSA Attention (#24959)
- **2026-09-07** [#36709](https://github.com/sgl-project/sglang/pull/36709) — [MUSA] Add installation guide and Dockerfile (#36709)
- _…and 101 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-07** [`a8edafff7c`](https://github.com/sgl-project/sglang/commit/a8edafff7c) [#38227](https://github.com/sgl-project/sglang/pull/38227) — [AMD][gfx95] DSV4 wo_b (dp-attention): route to tuned bpreshuffle GEMM instead of triton (#38227)
- **2026-09-07** [`644841c50c`](https://github.com/sgl-project/sglang/commit/644841c50c) [#37691](https://github.com/sgl-project/sglang/pull/37691) — [AMD] Support aiter fa mha chunked kv for Kimi-K3 (#37691)
- **2026-09-07** [`b99175dc7d`](https://github.com/sgl-project/sglang/commit/b99175dc7d) [#38049](https://github.com/sgl-project/sglang/pull/38049) — [Config] Round 6.4: the runtime reads the bags, not the record (#38049)
- **2026-09-07** [`df2f34cca1`](https://github.com/sgl-project/sglang/commit/df2f34cca1) [#38259](https://github.com/sgl-project/sglang/pull/38259) — Drop stale test_mla_gluon_h12_fp8.py broken by aiter gluon rewrite (#38259)
- **2026-09-07** [`503511c963`](https://github.com/sgl-project/sglang/commit/503511c963) [#38256](https://github.com/sgl-project/sglang/pull/38256) — [AMD] Cherry-pick aiter commit for dsv4 a8w8 bpreshuffle gemm config (#38256)
- **2026-09-07** [`1d5d85260c`](https://github.com/sgl-project/sglang/commit/1d5d85260c) [#37601](https://github.com/sgl-project/sglang/pull/37601) — [AMD] support qlen>1 for aiter gluon path for Kimi K3 (#37601)
- **2026-09-07** [`b9b39f222d`](https://github.com/sgl-project/sglang/commit/b9b39f222d) [#37784](https://github.com/sgl-project/sglang/pull/37784) — [AMD] Update ROCm AITER pin to 4ad9983 (#37784)
- **2026-09-07** [`15aa2fb843`](https://github.com/sgl-project/sglang/commit/15aa2fb843) [#37124](https://github.com/sgl-project/sglang/pull/37124) — [ROCm] Take the fused DSA metadata kernels and drop redundant work from the absorb path (#37124)
- **2026-09-06** [`2c05ed4e77`](https://github.com/sgl-project/sglang/commit/2c05ed4e77) [#37720](https://github.com/sgl-project/sglang/pull/37720) — [ROCm] Stage large pageable H2D copies instead of pinning them in place (#37720)
- **2026-09-06** [`6cee9285a3`](https://github.com/sgl-project/sglang/commit/6cee9285a3) [#37591](https://github.com/sgl-project/sglang/pull/37591) — [ROCm] Make DSA indexer top-k exact with cooperative selection (#37591)
- **2026-09-06** [`f5819b09bf`](https://github.com/sgl-project/sglang/commit/f5819b09bf) [#38163](https://github.com/sgl-project/sglang/pull/38163) — Revert "[AMD][DSV4] Fix unified-KV pool sizing and SWA ring accounting" (#38163)
- **2026-09-05** [`514b45fd34`](https://github.com/sgl-project/sglang/commit/514b45fd34) [#30315](https://github.com/sgl-project/sglang/pull/30315) — [AMD][DSV4] Fix unified-KV pool sizing and SWA ring accounting (#30315)
- **2026-09-05** [`0bdc15d20f`](https://github.com/sgl-project/sglang/commit/0bdc15d20f) [#34424](https://github.com/sgl-project/sglang/pull/34424) — [AMD] Fix ROCm VAE Conv2D fast path breaking spatial-parallel decode (#34424)
- **2026-09-05** [`d50e9a9756`](https://github.com/sgl-project/sglang/commit/d50e9a9756) [#38093](https://github.com/sgl-project/sglang/pull/38093) — [Test] Prune redundant unified-memory allocator and pool tests (#38093)
- **2026-09-05** [`0645398a32`](https://github.com/sgl-project/sglang/commit/0645398a32) [#38072](https://github.com/sgl-project/sglang/pull/38072) — [mem_cache] Move the unified-memory allocators into `allocator/` and split the composites out (#38072)
- **2026-09-05** [`3c2724c48d`](https://github.com/sgl-project/sglang/commit/3c2724c48d) [#35770](https://github.com/sgl-project/sglang/pull/35770) — [AMD] Optimize Kimi-K3 Triton MLA prefill on gfx950 (#35770)
- **2026-09-04** [`dae126d510`](https://github.com/sgl-project/sglang/commit/dae126d510) [#37658](https://github.com/sgl-project/sglang/pull/37658) — [AMD][DSv4] Fuse inverse-RoPE into the fp8 wo_a quant (stacked on #37423) (#37658)
- **2026-09-04** [`7f89cc5286`](https://github.com/sgl-project/sglang/commit/7f89cc5286) [#37580](https://github.com/sgl-project/sglang/pull/37580) — [AMD] Skip unused TOPK v2 plan kernel on ROCm (#37580)
- **2026-09-04** [`1bda9694b7`](https://github.com/sgl-project/sglang/commit/1bda9694b7) [#37423](https://github.com/sgl-project/sglang/pull/37423) — [AMD][DSv4] Switch output projection gemm (oproj_a) to fp8 (#37423)
- **2026-09-04** [`31ebd8f437`](https://github.com/sgl-project/sglang/commit/31ebd8f437) [#37764](https://github.com/sgl-project/sglang/pull/37764) — [AMD][DSv4] Fuse the DSv4 FP4 indexer prefill-schedule preamble into one kernel (#37764)
- **2026-09-04** [`cb32dbc9e0`](https://github.com/sgl-project/sglang/commit/cb32dbc9e0) [#35176](https://github.com/sgl-project/sglang/pull/35176) — [AMD] [Kimi-K3] Fuse the KDA input projection into a single GEMM on ROCm (#35176)
- **2026-09-04** [`4e756ecc4a`](https://github.com/sgl-project/sglang/commit/4e756ecc4a) [#37119](https://github.com/sgl-project/sglang/pull/37119) — [AMD] CI: fix Lean decode crash on the EAGLE path (#37119)
- **2026-09-04** [`7825e5ffca`](https://github.com/sgl-project/sglang/commit/7825e5ffca) [#35092](https://github.com/sgl-project/sglang/pull/35092) — [AMD] Fix DSV4 unified attention sink TP slice (#35092)
- **2026-09-04** [`225129fe44`](https://github.com/sgl-project/sglang/commit/225129fe44) [#37829](https://github.com/sgl-project/sglang/pull/37829) — [AMD] Update v4 amd cookbook 0903 (#37829)
- **2026-09-04** [`6147a54ddf`](https://github.com/sgl-project/sglang/commit/6147a54ddf) [#37874](https://github.com/sgl-project/sglang/pull/37874) — [PD] Bound transfer engine init with `SGLANG_DISAGGREGATION_ENGINE_INIT_TIMEOUT` (#37874)
- **2026-09-03** [`2bb25dc18b`](https://github.com/sgl-project/sglang/commit/2bb25dc18b) [#37667](https://github.com/sgl-project/sglang/pull/37667) — [Speculative Decoding] Add native UNO serving support (#37667)
- **2026-09-03** [`dd091f43cd`](https://github.com/sgl-project/sglang/commit/dd091f43cd) [#37781](https://github.com/sgl-project/sglang/pull/37781) — [AMD] Update kimi-k3 amd cookbook 0903 (#37781)
- **2026-09-03** [`f59a4840c5`](https://github.com/sgl-project/sglang/commit/f59a4840c5) [#37779](https://github.com/sgl-project/sglang/pull/37779) — [AMD][CI] Correct MI355X Slurm exclude node (#37779)
- **2026-09-03** [`429ac2d82c`](https://github.com/sgl-project/sglang/commit/429ac2d82c) [#37713](https://github.com/sgl-project/sglang/pull/37713) — [AMD] Fix DSv4 draft extend taking the target compression path during prefill (#37713)
- **2026-09-03** [`a6001478f4`](https://github.com/sgl-project/sglang/commit/a6001478f4) [#33838](https://github.com/sgl-project/sglang/pull/33838) — [AMD] Perf Kimi-K3 MoE optimization (#33838)
- **2026-09-03** [`7ed29eba80`](https://github.com/sgl-project/sglang/commit/7ed29eba80) [#37660](https://github.com/sgl-project/sglang/pull/37660) — [AMD] Fix FP4 indexer OOR (#37660)
- **2026-09-03** [`1fb85053e7`](https://github.com/sgl-project/sglang/commit/1fb85053e7) [#36349](https://github.com/sgl-project/sglang/pull/36349) — [AMD][Diffusion] Migrate FlyDSL fused norm kernels to the v0.3.0 stable API (#36349)
- **2026-09-03** [`030d7e7e9b`](https://github.com/sgl-project/sglang/commit/030d7e7e9b) [#37118](https://github.com/sgl-project/sglang/pull/37118) — [ROCm] Define the DSA head-gate graph helpers on HIP (#37118)
- **2026-09-03** [`db1eb48651`](https://github.com/sgl-project/sglang/commit/db1eb48651) [#37485](https://github.com/sgl-project/sglang/pull/37485) — [CI] Graceful teardown for the PD and HiSparse server fixtures (#37485)
- **2026-09-02** [`5a1275a519`](https://github.com/sgl-project/sglang/commit/5a1275a519) [#37550](https://github.com/sgl-project/sglang/pull/37550) — Converge the two SWA predicates, and stop conditioning the capture sink on the pool (#37550)
- **2026-09-02** [`2d799c28f4`](https://github.com/sgl-project/sglang/commit/2d799c28f4) [#37647](https://github.com/sgl-project/sglang/pull/37647) — [CI] Authenticate and retry git clones in install scripts (#37647)
- **2026-09-02** [`f8cbf000f4`](https://github.com/sgl-project/sglang/commit/f8cbf000f4) [#37353](https://github.com/sgl-project/sglang/pull/37353) — [AMD] Enable FP4 indexer for Deepseek V4 (#37353)
- **2026-09-02** [`99b9109553`](https://github.com/sgl-project/sglang/commit/99b9109553) [#37586](https://github.com/sgl-project/sglang/pull/37586) — [AMD] Run ROCm 7.0 shadow tests every two days- #37582 (#37586)
- **2026-09-02** [`ebfd8c60e5`](https://github.com/sgl-project/sglang/commit/ebfd8c60e5) [#37504](https://github.com/sgl-project/sglang/pull/37504) — [CI] Install sgl-eval from PyPI through the test extra (#37504)
- **2026-09-02** [`01c3a5f54f`](https://github.com/sgl-project/sglang/commit/01c3a5f54f) [#36646](https://github.com/sgl-project/sglang/pull/36646) — [misc] Resolve SWA ownership at enqueue time for grouped free() (#36646)
- **2026-09-02** [`0157f1f552`](https://github.com/sgl-project/sglang/commit/0157f1f552) [#37518](https://github.com/sgl-project/sglang/pull/37518) — [AMD][CI] Exclude unavailable MI355X nodes and skip 4N nightly (#37518)
- **2026-09-02** [`dc276264cb`](https://github.com/sgl-project/sglang/commit/dc276264cb) [#34198](https://github.com/sgl-project/sglang/pull/34198) — [AMD] Perf Kimi-K3 fuse ROCm KDA decode boundary (#34198)
- **2026-09-01** [`9978aaec8b`](https://github.com/sgl-project/sglang/commit/9978aaec8b) [#36960](https://github.com/sgl-project/sglang/pull/36960) — [ROCm][Bugfix] Cap the DSA MQA-logits budget at AITER's buffer_store limit (#36960)
- **2026-09-01** [`0b1ce3d140`](https://github.com/sgl-project/sglang/commit/0b1ce3d140) [#36890](https://github.com/sgl-project/sglang/pull/36890) — [Feature] Unified memory: support decode context parallelism for Kimi-Linear (#36890)
- **2026-09-01** [`bb3e3cbceb`](https://github.com/sgl-project/sglang/commit/bb3e3cbceb) [#37439](https://github.com/sgl-project/sglang/pull/37439) — [AMD] Fix v4 topk issue (#37439)
- **2026-09-01** [`44a92e54b9`](https://github.com/sgl-project/sglang/commit/44a92e54b9) [#37438](https://github.com/sgl-project/sglang/pull/37438) — [AMD] fix aiter cannot get heuristic kernel regression (#37438)
- **2026-09-01** [`3103bc7462`](https://github.com/sgl-project/sglang/commit/3103bc7462) [#37409](https://github.com/sgl-project/sglang/pull/37409) — [AMD][CI] Add daily ROCm 10 and ROCm 7.2 test coverage (#37409)
- **2026-09-01** [`ce7e79b32c`](https://github.com/sgl-project/sglang/commit/ce7e79b32c) [#36216](https://github.com/sgl-project/sglang/pull/36216) — [AMD] Fix nightly ROCm 7.0 image build: patch missing <optional> include in AITER topk kernel (#36216)
- **2026-09-01** [`ed122ea984`](https://github.com/sgl-project/sglang/commit/ed122ea984) [#36851](https://github.com/sgl-project/sglang/pull/36851) — [AMD] Enable topk v2 GLM ROCm (#36851)
- **2026-09-01** [`b425897366`](https://github.com/sgl-project/sglang/commit/b425897366) [#37242](https://github.com/sgl-project/sglang/pull/37242) — [AMD] Gate the aiter memory-reserve exemption behind an env var (#37242)
- **2026-09-01** [`6c72b49a57`](https://github.com/sgl-project/sglang/commit/6c72b49a57) [#36608](https://github.com/sgl-project/sglang/pull/36608) — Revert "[AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X (#36608)" (#37380)
- **2026-09-01** [`5edcd0a445`](https://github.com/sgl-project/sglang/commit/5edcd0a445) [#33237](https://github.com/sgl-project/sglang/pull/33237) — [FlashInfer V0.6.18] feat(dsv4): support --dsa-topk-backend flashinfer with fused top-k (#33237)
- **2026-09-01** [`8a191554e3`](https://github.com/sgl-project/sglang/commit/8a191554e3) [#34647](https://github.com/sgl-project/sglang/pull/34647) — [AMD] Enable 12-head MLA aiter fp8 Gluon decode (batched bh16bn128). (#34647)
- **2026-09-01** [`458987b5ac`](https://github.com/sgl-project/sglang/commit/458987b5ac) [#509](https://github.com/sgl-project/sglang/pull/509) — [AMD][MORI] Bump MoRI to 7c51d18 for ionic RoCE dmabuf fix (#509) (#37286)
- **2026-09-01** [`22337e9c56`](https://github.com/sgl-project/sglang/commit/22337e9c56) [#37307](https://github.com/sgl-project/sglang/pull/37307) — fix(unified-memory): forward the KV-index translator through every wrapper backend (#37307)
- **2026-08-31** [`961beee9e5`](https://github.com/sgl-project/sglang/commit/961beee9e5) [#35154](https://github.com/sgl-project/sglang/pull/35154) — fix(unified-memory): four boot/correctness fixes on the hybrid model paths (#35154)
- **2026-08-31** [`95f0f41021`](https://github.com/sgl-project/sglang/commit/95f0f41021) [#34074](https://github.com/sgl-project/sglang/pull/34074) — [CI] Move tests onto the right CI stages (#34074)
- **2026-08-31** [`07d84ebd6d`](https://github.com/sgl-project/sglang/commit/07d84ebd6d) [#36933](https://github.com/sgl-project/sglang/pull/36933) — [2/N][Mixed] Mixed chunk prefill with spec enabled (#36933)
- **2026-08-31** [`0674be736c`](https://github.com/sgl-project/sglang/commit/0674be736c) [#37225](https://github.com/sgl-project/sglang/pull/37225) — [AMD] build gfx1250 release image from main (#37225)
- **2026-08-31** [`3865efc9f7`](https://github.com/sgl-project/sglang/commit/3865efc9f7) [#36871](https://github.com/sgl-project/sglang/pull/36871) — [AMD] support gfx1250 on ROCM 10 (#36871)
- **2026-08-31** [`8bb776dc48`](https://github.com/sgl-project/sglang/commit/8bb776dc48) [#34613](https://github.com/sgl-project/sglang/pull/34613) — feat(unified-memory): read unified pool from attention backends fa3/flashinfer/trtllm_mha/flashmla (#34613)
- **2026-08-31** [`3a6ed55999`](https://github.com/sgl-project/sglang/commit/3a6ed55999) [#37194](https://github.com/sgl-project/sglang/pull/37194) — [Fix] Shut hicache test servers down gracefully before SIGKILL (#37194)
- **2026-08-31** [`5972211977`](https://github.com/sgl-project/sglang/commit/5972211977) [#37132](https://github.com/sgl-project/sglang/pull/37132) — [AMD] Fix the QuickReduce bf16 cast failing to build for CDNA (#37132)
- **2026-08-31** [`7700602278`](https://github.com/sgl-project/sglang/commit/7700602278) [#35281](https://github.com/sgl-project/sglang/pull/35281) — [PD] Align defensive protocol behavior across Mooncake, NIXL, and Mori (#35281)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#37451](https://github.com/sgl-project/sglang/issues/37451) | [Failure Tracker] PR Test (AMD) | ci-failure-tracker | 2026-09-07 |
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-09-07 |
| [#30209](https://github.com/sgl-project/sglang/issues/30209) | [Bug] GlmMoeDsa (GLM-5.2) FP4 + EAGLE: illegal memory access in flashi | — | 2026-09-07 |
| [#38334](https://github.com/sgl-project/sglang/issues/38334) | [RFC] Gluon MegaMoE: SGLang Integration and Multi-Node Support | — | 2026-09-07 |
| [#37372](https://github.com/sgl-project/sglang/issues/37372) | [Feature] [RFC] [HiCache] Out-of-process HiCache data plane with devic | — | 2026-09-07 |
| [#27252](https://github.com/sgl-project/sglang/issues/27252) | [Roadmap]Prefill Context Parallel Refactor | — | 2026-09-07 |
| [#31504](https://github.com/sgl-project/sglang/issues/31504) | [Proposal] Fuse static FP8 activation quantization into producer kerne | — | 2026-09-07 |
| [#35252](https://github.com/sgl-project/sglang/issues/35252) | [Bug] MoE tuner writes config files the runtime never reads (int4_w4a1 | — | 2026-09-07 |
| [#37813](https://github.com/sgl-project/sglang/issues/37813) | [Tracking] GLM-5.3-Flash on SM120: required fixes, carry status and re | — | 2026-09-06 |
| [#33185](https://github.com/sgl-project/sglang/issues/33185) | [Bug] DeepSeek-V4-Flash-0731: reasoning_effort mapped one level off —  | — | 2026-09-06 |
| [#38143](https://github.com/sgl-project/sglang/issues/38143) | [Bug] MiniMax-M3 W4A16 (compressed-tensors) on 2x DGX Spark (sm_121, T | — | 2026-09-06 |
| [#32441](https://github.com/sgl-project/sglang/issues/32441) | [Bug] [MLX] test_batched_decode_matches_solo asserts bitwise solo/batc | — | 2026-09-06 |
| [#32321](https://github.com/sgl-project/sglang/issues/32321) | [RFC] Apple Silicon serving redesign: Torch-owned SRT path with an exp | apple-silicon | 2026-09-06 |
| [#37519](https://github.com/sgl-project/sglang/issues/37519) | [Roadmap][Feature] Support T-Head PPU | — | 2026-09-06 |
| [#33522](https://github.com/sgl-project/sglang/issues/33522) | [Roadmap]Fast Engine Recovery: Weight Cache Daemon | — | 2026-09-05 |
| [#23206](https://github.com/sgl-project/sglang/issues/23206) | [RFC] Sglang non-GPU process rust migration | — | 2026-09-05 |
| [#36226](https://github.com/sgl-project/sglang/issues/36226) | [Performance] Multiple potential avoidable scheduler, sampling, and st | — | 2026-09-05 |
| [#38004](https://github.com/sgl-project/sglang/issues/38004) | [RFC] Quantization module layout: Config, Scheme, backend kernels | — | 2026-09-04 |
| [#35270](https://github.com/sgl-project/sglang/issues/35270) | [Bug] Radix cache `evictable_size()` double-counts shared pages, killi | — | 2026-09-04 |
| [#38029](https://github.com/sgl-project/sglang/issues/38029) | [Bug] EAGLE DSA draft backend misses KVIndexTranslator in FP8 MHA pref | — | 2026-09-04 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 98 |
| Multimodal | 53 |
| Prefill / Decode Disaggregation | 41 |
| MoE / Expert Parallel | 40 |
| KV Cache / Memory | 38 |
| Quantization | 24 |
| Other | 23 |
| Triton / Kernels | 22 |
| CI / Build | 18 |
| ROCm / AMD | 15 |
| Tensor / Data Parallel | 11 |
| Scheduler / Batching | 10 |
| Docs / Examples | 9 |
| Models | 9 |
| Speculative Decoding | 4 |
| LoRA | 2 |
| Structured Output | 2 |
| Serving / API | 2 |

## Attention / FlashInfer  (98 commits)

- **2026-09-07** [`8ae962021d`](https://github.com/sgl-project/sglang/commit/8ae962021d) [#36143](https://github.com/sgl-project/sglang/pull/36143)
  Use fp32 in TRTLLM all reduce buffers  (#36143)
  _Files: `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `test/registered/unit/layers/test_flashinfer_comm_fusion.py`_
- **2026-09-07** [`b5766336d4`](https://github.com/sgl-project/sglang/commit/b5766336d4) [#37926](https://github.com/sgl-project/sglang/pull/37926)
  [Perf] Unified memory: close the DCP decode gap on Blackwell (#37926)
  _Files: `python/sglang/kernels/ops/mamba/mamba_state_indices_triton.py`, `python/sglang/kernels/ops/memory/__init__.py`, `python/sglang/kernels/ops/memory/virtual_slot.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py` _+17 more__
- **2026-09-07** [`a8edafff7c`](https://github.com/sgl-project/sglang/commit/a8edafff7c) [#38227](https://github.com/sgl-project/sglang/pull/38227)
  [AMD][gfx95] DSV4 wo_b (dp-attention): route to tuned bpreshuffle GEMM instead of triton (#38227)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-09-07** [`644841c50c`](https://github.com/sgl-project/sglang/commit/644841c50c) [#37691](https://github.com/sgl-project/sglang/pull/37691)
  [AMD] Support aiter fa mha chunked kv for Kimi-K3 (#37691)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/deepseek_common/attention_backend_handler.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_methods.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` _+2 more__
- **2026-09-07** [`e24e31efd9`](https://github.com/sgl-project/sglang/commit/e24e31efd9) [#36298](https://github.com/sgl-project/sglang/pull/36298)
  Fix/whisper xpu varlen encoder decoder (#36298)
  _Files: `python/sglang/srt/layers/attention/xpu_backend.py`, `test/registered/unit/layers/attention/test_encoder_decoder_varlen_gather.py`, `test/registered/xpu/test_xpu_encoder_decoder_varlen.py`_
- **2026-09-07** [`df2f34cca1`](https://github.com/sgl-project/sglang/commit/df2f34cca1) [#38259](https://github.com/sgl-project/sglang/pull/38259)
  Drop stale test_mla_gluon_h12_fp8.py broken by aiter gluon rewrite (#38259)
  _Files: `test/registered/attention/test_mla_gluon_h12_fp8.py`_
- **2026-09-07** [`1d5d85260c`](https://github.com/sgl-project/sglang/commit/1d5d85260c) [#37601](https://github.com/sgl-project/sglang/pull/37601)
  [AMD] support qlen>1 for aiter gluon path for Kimi K3 (#37601)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/aiter_mla_gluon.py`, `test/registered/attention/test_aiter_gluon_h12_fp8.py`_
- **2026-09-07** [`30d0eb2ca9`](https://github.com/sgl-project/sglang/commit/30d0eb2ca9) [#35629](https://github.com/sgl-project/sglang/pull/35629)
  [NPU] Adapt DFlash2 speculative decoding to Ascend NPUs (#35629)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `test/registered/unit/spec/test_dflash_extra_buffer_lazy.py`, `test/registered/unit/spec/test_dflash_logits.py`_
- **2026-09-07** [`15aa2fb843`](https://github.com/sgl-project/sglang/commit/15aa2fb843) [#37124](https://github.com/sgl-project/sglang/pull/37124)
  [ROCm] Take the fused DSA metadata kernels and drop redundant work from the absorb path (#37124)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`_
- **2026-09-06** [`2e8c03e2c7`](https://github.com/sgl-project/sglang/commit/2e8c03e2c7) [#34142](https://github.com/sgl-project/sglang/pull/34142)
  Fix inflated row pitch when a CP round-robin shard has a single row (#34142)
  _Files: `python/sglang/srt/layers/attention/dsa/utils.py`_
- **2026-09-06** [`97c6978369`](https://github.com/sgl-project/sglang/commit/97c6978369) [#36507](https://github.com/sgl-project/sglang/pull/36507)
  GLM-5.3-Flash support (#36507)
- **2026-09-05** [`09daea94ac`](https://github.com/sgl-project/sglang/commit/09daea94ac) [#38152](https://github.com/sgl-project/sglang/pull/38152)
  Support NoPE layers in the tokenspeed_mla FP8 prefill hook (#38152)
  _Files: `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py`, `test/registered/attention/unittests/mla/test_tokenspeed_mla.py`_
- **2026-09-05** [`4b802c052b`](https://github.com/sgl-project/sglang/commit/4b802c052b) [#37990](https://github.com/sgl-project/sglang/pull/37990)
  test(npu): remove obsolete npu pr nightly cases, move accuracy cases to full (#37990)
  _Files: `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/full-test-npu.yml`, `.github/workflows/nightly-test-npu.yml`, `test/registered/npu/accuracy/deepseek_v3_2/test_npu_deepseek_v3_2_8p_aime25.py` _+56 more__
- **2026-09-05** [`0ea8378085`](https://github.com/sgl-project/sglang/commit/0ea8378085) [#37959](https://github.com/sgl-project/sglang/pull/37959)
  [diffusion] feat: support request-scoped skip-softmax attention (#37959)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py` _+12 more__
- **2026-09-05** [`d50e9a9756`](https://github.com/sgl-project/sglang/commit/d50e9a9756) [#38093](https://github.com/sgl-project/sglang/pull/38093)
  [Test] Prune redundant unified-memory allocator and pool tests (#38093)
  _Files: `test/registered/models_e2e/test_kimi_linear_unified_memory.py`, `test/registered/page_major/test_page_major_gpt_oss.py`, `test/registered/page_major/test_page_major_qwen_hybrid.py`, `test/registered/unit/layers/attention/test_kv_translate_ownership.py` _+17 more__
- **2026-09-05** [`3c2724c48d`](https://github.com/sgl-project/sglang/commit/3c2724c48d) [#35770](https://github.com/sgl-project/sglang/pull/35770)
  [AMD] Optimize Kimi-K3 Triton MLA prefill on gfx950 (#35770)
  _Files: `python/sglang/kernels/ops/attention/extend_attention.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/model_executor/forward_batch_deepseek_mha_mixin.py` _+4 more__
- **2026-09-04** [`db89f639ef`](https://github.com/sgl-project/sglang/commit/db89f639ef) [#35544](https://github.com/sgl-project/sglang/pull/35544)
  [GDN] Amortize ReplaySSM checkpoint materialization (#35544)
  _Files: `python/sglang/kernels/ops/attention/fla/gdn_replayssm_spec_decode.py`, `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/configs/mamba_utils.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py` _+5 more__
- **2026-09-04** [`07199fa220`](https://github.com/sgl-project/sglang/commit/07199fa220) [#36267](https://github.com/sgl-project/sglang/pull/36267)
  [Performance] Optimize Qwen3.5 GDN prefill projection layouts (#36267)
  _Files: `python/sglang/kernels/ops/attention/fla/l2norm.py`, `python/sglang/kernels/ops/attention/fla/layernorm_gated.py`, `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py` _+3 more__
- **2026-09-04** [`dc6b5d1f5a`](https://github.com/sgl-project/sglang/commit/dc6b5d1f5a) [#38011](https://github.com/sgl-project/sglang/pull/38011)
  [CI][NPU] Remove model tests from PR-test pipeline (#38011)
  _Files: `.github/workflows/pr-test-npu.yml`, `test/registered/npu/accuracy/glm4_7_flash/test_npu_glm4_7_flash_1p_gsm8k.py`, `test/registered/npu/accuracy/qwen3_5_9b/test_npu_qwen3_5_9b_bf16_1p_gsm8k.py`, `test/registered/npu/accuracy/qwen3_vl_30b_a3b/test_npu_qwen3_vl_30b_a3b_bf16_2p_gsm8k.py` _+10 more__
- **2026-09-04** [`44c786679f`](https://github.com/sgl-project/sglang/commit/44c786679f) [#37546](https://github.com/sgl-project/sglang/pull/37546)
  [sp] Make attention-TP sequence sharding a per-forward batch property (#37546)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`, `python/sglang/srt/kv_canary/perturb/slot_picker.py` _+36 more__
- **2026-09-04** [`0b57847ebf`](https://github.com/sgl-project/sglang/commit/0b57847ebf) [#37836](https://github.com/sgl-project/sglang/pull/37836)
  Fix mamba radix cache ssm state indexing (#37836)
  _Files: `python/sglang/kernels/ops/mamba/triton_ops/ssd_combined.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/layers/attention/mamba/mamba2_metadata.py` _+2 more__
- **2026-09-04** [`31ebd8f437`](https://github.com/sgl-project/sglang/commit/31ebd8f437) [#37764](https://github.com/sgl-project/sglang/pull/37764)
  [AMD][DSv4] Fuse the DSv4 FP4 indexer prefill-schedule preamble into one kernel (#37764)
  _Files: `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_hip.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_schedule_hip.py`_
- **2026-09-04** [`d122ca99b2`](https://github.com/sgl-project/sglang/commit/d122ca99b2) [#32902](https://github.com/sgl-project/sglang/pull/32902)
  [Bugfix] Fix Llama 4 FA3 local attention with paged KV cache (#32902)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`_
- **2026-09-04** [`4e756ecc4a`](https://github.com/sgl-project/sglang/commit/4e756ecc4a) [#37119](https://github.com/sgl-project/sglang/pull/37119)
  [AMD] CI: fix Lean decode crash on the EAGLE path (#37119)
  _Files: `python/sglang/kernels/ops/attention/decode_attention.py`_
- **2026-09-04** [`7825e5ffca`](https://github.com/sgl-project/sglang/commit/7825e5ffca) [#35092](https://github.com/sgl-project/sglang/pull/35092)
  [AMD] Fix DSV4 unified attention sink TP slice (#35092)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-09-04** [`e787de5478`](https://github.com/sgl-project/sglang/commit/e787de5478) [#37532](https://github.com/sgl-project/sglang/pull/37532)
  [XPU][CI] Move XPU tests to nightly and add per-subclass server launch timeout (#37532)
  _Files: `python/sglang/test/server_fixtures/spec_eagle_fixture.py`, `test/registered/spec/eagle/test_spec_eagle_parity.py`, `test/registered/xpu/test_deepseek_ocr_triton.py`, `test/registered/xpu/test_gemma_4_e2b.py` _+1 more__
- **2026-09-04** [`3ad3f23ed5`](https://github.com/sgl-project/sglang/commit/3ad3f23ed5) [#37206](https://github.com/sgl-project/sglang/pull/37206)
  [Comm] Drop the in-tree MNNVL CuTe DSL port in favor of FlashInfer 0.6.18 (#37206)
  _Files: `python/sglang/kernels/ops/communication/mnnvl_cutedsl/__init__.py`, `python/sglang/kernels/ops/communication/mnnvl_cutedsl/config.py`, `python/sglang/kernels/ops/communication/mnnvl_cutedsl/cute_dsl_primitives.py`, `python/sglang/kernels/ops/communication/mnnvl_cutedsl/kernel_bt/__init__.py` _+13 more__
- **2026-09-04** [`ff1285cc28`](https://github.com/sgl-project/sglang/commit/ff1285cc28) [#36223](https://github.com/sgl-project/sglang/pull/36223)
  [CP V1 Deprecation 2/5] Make strategy prefill CP canonical (#36223)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/environ.py` _+5 more__
- **2026-09-04** [`9ed2721c6d`](https://github.com/sgl-project/sglang/commit/9ed2721c6d) [#36843](https://github.com/sgl-project/sglang/pull/36843)
  [NPU] fix extend_seq_lens_cpu shape in eager mode (#36843)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `test/registered/npu/performance/minimax_m2_5/test_npu_minimax_m2_5_w8a8_4p_in64k_out1k_prefix90_50ms.py`_
- **2026-09-03** [`2da5802bfa`](https://github.com/sgl-project/sglang/commit/2da5802bfa) [#37737](https://github.com/sgl-project/sglang/pull/37737)
  [Cookbook] DeepSeek-V4 DGX Spark: v2 image + Flash Official NVFP4 and Flash Vision FP4 cells (#37737)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-03** [`4e37882a93`](https://github.com/sgl-project/sglang/commit/4e37882a93) [#37332](https://github.com/sgl-project/sglang/pull/37332)
  [Diffusion][minimax-h3] Add SM120 support for SubBlock sparse attention (#37332)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/README.md`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/__init__.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/router.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse_attn.py` _+3 more__
- **2026-09-03** [`3239baef25`](https://github.com/sgl-project/sglang/commit/3239baef25) [#37760](https://github.com/sgl-project/sglang/pull/37760)
  [CI][NPU] Fix kimi_k2_6 16p in64k perf test and dsv4-flash testcases (#37760)
  _Files: `python/sglang/test/ascend/e2e/run_npu_testcase.sh`, `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_gpqa.py`, `test/registered/npu/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_1p1d_16p_in8k_out1k_50ms.py`, `test/registered/npu/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in32k_out1k_50ms.py` _+2 more__
- **2026-09-03** [`f5bed255c0`](https://github.com/sgl-project/sglang/commit/f5bed255c0) [#36735](https://github.com/sgl-project/sglang/pull/36735)
  [diffusion] feat: support key masks on USPAttention's replicated-prefix path (#36735)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/test/unit/test_usp_attention_replicated_prefix.py`_
- **2026-09-03** [`2bb25dc18b`](https://github.com/sgl-project/sglang/commit/2bb25dc18b) [#37667](https://github.com/sgl-project/sglang/pull/37667)
  [Speculative Decoding] Add native UNO serving support (#37667)
  _Files: `benchmark/uno/README.md`, `benchmark/uno/__init__.py`, `benchmark/uno/math_data.py`, `benchmark/uno/math_grader.py` _+47 more__
- **2026-09-03** [`a11dba1a01`](https://github.com/sgl-project/sglang/commit/a11dba1a01) [#37693](https://github.com/sgl-project/sglang/pull/37693)
  [Feature] Unified memory: support decode context parallelism for the trtllm_mla family (#37693)
  _Files: `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/layers/attention/cutedsl_mla_backend.py`, `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py` _+4 more__
- **2026-09-03** [`429ac2d82c`](https://github.com/sgl-project/sglang/commit/429ac2d82c) [#37713](https://github.com/sgl-project/sglang/pull/37713)
  [AMD] Fix DSv4 draft extend taking the target compression path during prefill (#37713)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-09-03** [`7ed29eba80`](https://github.com/sgl-project/sglang/commit/7ed29eba80) [#37660](https://github.com/sgl-project/sglang/pull/37660)
  [AMD] Fix FP4 indexer OOR (#37660)
  _Files: `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_hip.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `test/registered/kernels/ops/attention/test_fp4_indexer_hip.py`_
- **2026-09-03** [`030d7e7e9b`](https://github.com/sgl-project/sglang/commit/030d7e7e9b) [#37118](https://github.com/sgl-project/sglang/pull/37118)
  [ROCm] Define the DSA head-gate graph helpers on HIP (#37118)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/dsa_prefill_cuda_graph.py`, `test/registered/unit/layers/attention/test_dsa_head_gate_guard.py`_
- **2026-09-03** [`4229088a48`](https://github.com/sgl-project/sglang/commit/4229088a48) [#33911](https://github.com/sgl-project/sglang/pull/33911)
  feat(kernels): generalize persistent CuTe JIT cache (#33911)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/kernels/jit/cute_aot_cache.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/cache_utils.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py` _+2 more__
- **2026-09-03** [`6e41f1ad29`](https://github.com/sgl-project/sglang/commit/6e41f1ad29) [#37489](https://github.com/sgl-project/sglang/pull/37489)
  [Fix] Preserve FP32 in SM107 MXFP8 fallback (#37489)
  _Files: `python/sglang/srt/layers/quantization/mxfp4.py`, `test/registered/unit/layers/quantization/test_mxfp4_flashinfer_activation_prep.py`_
- **2026-09-03** [`5c46ce37f5`](https://github.com/sgl-project/sglang/commit/5c46ce37f5) [#37669](https://github.com/sgl-project/sglang/pull/37669)
  [Fix] Apply the attention-CP broadcast result in PP dynamic-chunk profiling (#37669)
  _Files: `python/sglang/srt/distributed/communication_op.py`, `python/sglang/srt/managers/scheduler_components/request_receiver.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/registered/unit/managers/test_pp_cp_rank_offsets.py`_
- **2026-09-03** [`3421d4375b`](https://github.com/sgl-project/sglang/commit/3421d4375b) [#37576](https://github.com/sgl-project/sglang/pull/37576)
  [Docs] GLM-5.3-Flash cookbook: drop stale EP caveat, add B300/H100/B200 FP8 speed data (#37576)
  _Files: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-09-02** [`5ddca6819e`](https://github.com/sgl-project/sglang/commit/5ddca6819e) [#37560](https://github.com/sgl-project/sglang/pull/37560)
  Fix unified SWA: size a non-owner's v2p by the id space it must address (#37560)
  _Files: `python/sglang/srt/mem_cache/multi_ended_allocator.py`, `test/registered/attention/test_gemma4_unified_swa_virtual_ids.py`, `test/registered/unit/mem_cache/test_unified_swa_shared_virtual_ids.py`_
- **2026-09-02** [`5a1275a519`](https://github.com/sgl-project/sglang/commit/5a1275a519) [#37550](https://github.com/sgl-project/sglang/pull/37550)
  Converge the two SWA predicates, and stop conditioning the capture sink on the pool (#37550)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py` _+2 more__
- **2026-09-02** [`d9848b9ecd`](https://github.com/sgl-project/sglang/commit/d9848b9ecd) [#37512](https://github.com/sgl-project/sglang/pull/37512)
  Build the unified read stream directly, without the page-table rectangle (#37512)
  _Files: `python/sglang/kernels/ops/attention/metadata.py`, `python/sglang/kernels/ops/kvcache/__init__.py`, `python/sglang/kernels/ops/kvcache/kv_read_table.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` _+7 more__
- **2026-09-02** [`718bd39fe0`](https://github.com/sgl-project/sglang/commit/718bd39fe0) [#37505](https://github.com/sgl-project/sglang/pull/37505)
  [Fix] DP attention: correct the decode->extend prefix off-by-one (#37505)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `test/registered/unit/managers/scheduler_components/test_dp_attn.py`, `test/registered/unit/managers/test_schedule_batch_convert_decode_to_extend.py` _+1 more__
- **2026-09-02** [`3c9cea8f10`](https://github.com/sgl-project/sglang/commit/3c9cea8f10) [#35546](https://github.com/sgl-project/sglang/pull/35546)
  [EAGLE] Prune draft-extend logits to selected rows (#35546)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/model_executor/input_buffers.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_info.py` _+4 more__
- **2026-09-02** [`fe45af1e6f`](https://github.com/sgl-project/sglang/commit/fe45af1e6f) [#36970](https://github.com/sgl-project/sglang/pull/36970)
  perf(gdn): select ReplaySSM verify loop unrolling by shape (#36970)
  _Files: `python/sglang/kernels/ops/attention/cutedsl_gdn_mtp_ring.py`, `test/registered/attention/unittests/gdn/test_gdn_cutedsl_ring_verify.py`_
- **2026-09-02** [`f586654518`](https://github.com/sgl-project/sglang/commit/f586654518) [#37480](https://github.com/sgl-project/sglang/pull/37480)
  [diffusion] feat: support FastH3 (4-step VSA-distilled MiniMax-H3) with a VSA-H3 attention backend (#37480)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs/docs/sglang-diffusion/quantization.mdx` _+22 more__
- **2026-09-02** [`ebfd8c60e5`](https://github.com/sgl-project/sglang/commit/ebfd8c60e5) [#37504](https://github.com/sgl-project/sglang/pull/37504)
  [CI] Install sgl-eval from PyPI through the test extra (#37504)
  _Files: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.github/workflows/_pr-test-stage-cpu.yml`, `docker/xeon.Dockerfile`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx` _+28 more__
- **2026-09-02** [`4b329482e8`](https://github.com/sgl-project/sglang/commit/4b329482e8) [#34893](https://github.com/sgl-project/sglang/pull/34893)
  [diffusion] feat: support cube sparse attention for minimax h3 (#34893)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/cube_sparse_attn/__init__.py` _+14 more__
- **2026-09-02** [`9175590aa0`](https://github.com/sgl-project/sglang/commit/9175590aa0) [#37441](https://github.com/sgl-project/sglang/pull/37441)
  [diffusion] refactor: admit explicit attention backends by capability (#37441)
  _Files: `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/models/dits/base.py` _+6 more__
- **2026-09-02** [`d585cec4bd`](https://github.com/sgl-project/sglang/commit/d585cec4bd) [#37343](https://github.com/sgl-project/sglang/pull/37343)
  Fix nondeterministic FlashInfer GDN alignment test (#37343)
  _Files: `test/registered/unit/layers/attention/test_gdn_flashinfer_alignment.py`_
- **2026-09-02** [`26f760d5c0`](https://github.com/sgl-project/sglang/commit/26f760d5c0) [#32733](https://github.com/sgl-project/sglang/pull/32733)
  [CPU] Support FP8 KV cache (#32733)
  _Files: `python/sglang/kernels/aot/csrc/cpu/decode.cpp`, `python/sglang/kernels/aot/csrc/cpu/extend.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/kernels/aot/csrc/cpu/vec_pack.h` _+10 more__
- **2026-09-02** [`22195709d1`](https://github.com/sgl-project/sglang/commit/22195709d1) [#36824](https://github.com/sgl-project/sglang/pull/36824)
  [diffusion] refactor: remove component loader capability switches (#36824)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/bridge_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/image_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py` _+13 more__
- **2026-09-02** [`dde0ecdb90`](https://github.com/sgl-project/sglang/commit/dde0ecdb90) [#37437](https://github.com/sgl-project/sglang/pull/37437)
  [diffusion] feat: support spargeattention (#37437)
  _Files: `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/sparge_attn.py`, `python/sglang/multimodal_gen/runtime/models/dits/base.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py` _+4 more__
- **2026-09-02** [`dc276264cb`](https://github.com/sgl-project/sglang/commit/dc276264cb) [#34198](https://github.com/sgl-project/sglang/pull/34198)
  [AMD] Perf Kimi-K3 fuse ROCm KDA decode boundary (#34198)
  _Files: `python/sglang/kernels/ops/attention/kda_fused_decode_aiter_hip.py`, `python/sglang/kernels/ops/kimi_k3/flydsl/__init__.py`, `python/sglang/kernels/ops/kimi_k3/flydsl/kernels/__init__.py`, `python/sglang/kernels/ops/kimi_k3/flydsl/kernels/kimi_k3_kda_decode.py` _+8 more__
- **2026-09-02** [`6d34a4d3ce`](https://github.com/sgl-project/sglang/commit/6d34a4d3ce) [#37492](https://github.com/sgl-project/sglang/pull/37492)
  [Cookbook] Verify DeepSeek-V4 Flash Vision on GB300 (#37492)
  _Files: `docs/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-01** [`ed82bea146`](https://github.com/sgl-project/sglang/commit/ed82bea146) [#37479](https://github.com/sgl-project/sglang/pull/37479)
  [Cookbook] DeepSeek-V4: add DGX Spark (2x GB10) Flash Official FP4 recipe (#37479)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-01** [`9978aaec8b`](https://github.com/sgl-project/sglang/commit/9978aaec8b) [#36960](https://github.com/sgl-project/sglang/pull/36960)
  [ROCm][Bugfix] Cap the DSA MQA-logits budget at AITER's buffer_store limit (#36960)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `test/registered/unit/layers/attention/test_dsa_mqa_logits_chunking.py`_
- **2026-09-01** [`b24c8f10e7`](https://github.com/sgl-project/sglang/commit/b24c8f10e7) [#32218](https://github.com/sgl-project/sglang/pull/32218)
  [FlashInfer] Avoid D2H sync for sliding-window lengths (#32218)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`, `test/registered/attention/unittests/swa/test_flashinfer.py`_
- **2026-09-01** [`0f18d389b4`](https://github.com/sgl-project/sglang/commit/0f18d389b4) [#37468](https://github.com/sgl-project/sglang/pull/37468)
  [Cookbook] Verify DeepSeek-V4 Flash Vision balanced and high-throughput on B200 (#37468)
  _Files: `docs/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-01** [`442c7c1e29`](https://github.com/sgl-project/sglang/commit/442c7c1e29) [#37412](https://github.com/sgl-project/sglang/pull/37412)
  [Docs] GLM-5.3-Flash cookbook: add NVFP4 FP8+TRT-LLM benchmark rows (follow-up to #37109) (#37412)
  _Files: `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-09-01** [`0b1ce3d140`](https://github.com/sgl-project/sglang/commit/0b1ce3d140) [#36890](https://github.com/sgl-project/sglang/pull/36890)
  [Feature] Unified memory: support decode context parallelism for Kimi-Linear (#36890)
  _Files: `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/kernels/ops/kvcache/mla_buffer.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py` _+16 more__
- **2026-09-01** [`3315356cc0`](https://github.com/sgl-project/sglang/commit/3315356cc0) [#37360](https://github.com/sgl-project/sglang/pull/37360)
  docs(cookbook): enable FlashInfer GDN for Qwen3.5 B200 (#37360)
  _Files: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-09-01** [`a2b8681d1d`](https://github.com/sgl-project/sglang/commit/a2b8681d1d) [#37453](https://github.com/sgl-project/sglang/pull/37453)
  [CI][MLX] Restore the mamba_branching_seqlen attribute the MLX runner reads off a request (#37453)
  _Files: `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`_
- **2026-09-01** [`9a05b470fa`](https://github.com/sgl-project/sglang/commit/9a05b470fa) [#36911](https://github.com/sgl-project/sglang/pull/36911)
  [Memory] Size the CUDA graph pool from warmup measurements and fix graph-pool borrowing (#36911)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/kv_pool_runtime.py` _+13 more__
- **2026-09-01** [`bb3e3cbceb`](https://github.com/sgl-project/sglang/commit/bb3e3cbceb) [#37439](https://github.com/sgl-project/sglang/pull/37439)
  [AMD] Fix v4 topk issue (#37439)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-09-01** [`44a92e54b9`](https://github.com/sgl-project/sglang/commit/44a92e54b9) [#37438](https://github.com/sgl-project/sglang/pull/37438)
  [AMD] fix aiter cannot get heuristic kernel regression (#37438)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-09-01** [`b6c06e1efb`](https://github.com/sgl-project/sglang/commit/b6c06e1efb) [#36831](https://github.com/sgl-project/sglang/pull/36831)
  [DSA] Drop the redundant 512 from the top-k transform entry-point names (#36831)
  _Files: `python/sglang/kernels/ops/attention/dsv4/__init__.py`, `python/sglang/kernels/ops/attention/dsv4/topk.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py` _+3 more__
- **2026-09-01** [`3ae54c6ca2`](https://github.com/sgl-project/sglang/commit/3ae54c6ca2) [#37431](https://github.com/sgl-project/sglang/pull/37431)
  test(npu): add DSV4-Flash / GLM-5.2 / Kimi-K3 gpqa accuracy cases (#37431)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_gpqa.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w4a8_16p_gpqa.py` _+4 more__
- **2026-09-01** [`4c2c169e6b`](https://github.com/sgl-project/sglang/commit/4c2c169e6b) [#36329](https://github.com/sgl-project/sglang/pull/36329)
  [NPU]Strip padding before FIA kernel for vision encoder padded sequences (#36329)
  _Files: `python/sglang/srt/layers/attention/vision.py`_
- **2026-09-01** [`b425897366`](https://github.com/sgl-project/sglang/commit/b425897366) [#37242](https://github.com/sgl-project/sglang/pull/37242)
  [AMD] Gate the aiter memory-reserve exemption behind an env var (#37242)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/environ.py`_
- **2026-09-01** [`c16a8fc899`](https://github.com/sgl-project/sglang/commit/c16a8fc899) [#36813](https://github.com/sgl-project/sglang/pull/36813)
  [NPU] [bugfix] Fix NPU MLA HiCache backup accessing missing data_ptrs. (#36813)
  _Files: `python/sglang/srt/mem_cache/pool_host/mla.py`_
- **2026-09-01** [`dc1ae02684`](https://github.com/sgl-project/sglang/commit/dc1ae02684) [#37392](https://github.com/sgl-project/sglang/pull/37392)
  [Cookbook] Add the DFlash2 speculative option to GLM-5.3 (#37392)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`_
- **2026-09-01** [`6c72b49a57`](https://github.com/sgl-project/sglang/commit/6c72b49a57) [#36608](https://github.com/sgl-project/sglang/pull/36608)
  Revert "[AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X (#36608)" (#37380)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-09-01** [`5edcd0a445`](https://github.com/sgl-project/sglang/commit/5edcd0a445) [#33237](https://github.com/sgl-project/sglang/pull/33237)
  [FlashInfer V0.6.18] feat(dsv4): support --dsa-topk-backend flashinfer with fused top-k (#33237)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` _+4 more__
- **2026-09-01** [`379e33d87e`](https://github.com/sgl-project/sglang/commit/379e33d87e) [#37351](https://github.com/sgl-project/sglang/pull/37351)
  [Cookbook] Add NVFP4 options for DeepSeek-V4 Flash Official (0731) and Pro Official (0813) (#37351)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-01** [`03b33cbe5d`](https://github.com/sgl-project/sglang/commit/03b33cbe5d) [#37374](https://github.com/sgl-project/sglang/pull/37374)
  [CI] Fix hybrid wrapper test fake missing kv_index_translator (#37374)
  _Files: `test/registered/attention/test_trtllm_mha_graph_metadata.py`_
- **2026-09-01** [`8a191554e3`](https://github.com/sgl-project/sglang/commit/8a191554e3) [#34647](https://github.com/sgl-project/sglang/pull/34647)
  [AMD] Enable 12-head MLA aiter fp8 Gluon decode (batched bh16bn128). (#34647)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/aiter_mla_gluon.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py` _+1 more__
- **2026-09-01** [`60548501bb`](https://github.com/sgl-project/sglang/commit/60548501bb) [#37109](https://github.com/sgl-project/sglang/pull/37109)
  [Docs] Add NVFP4 section to GLM-5.3-Flash cookbook (#37109)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-09-01** [`33ed29a0ee`](https://github.com/sgl-project/sglang/commit/33ed29a0ee) [#37345](https://github.com/sgl-project/sglang/pull/37345)
  test: update hybrid attention runner fixtures (#37345)
  _Files: `test/registered/attention/test_trtllm_mha_graph_metadata.py`, `test/registered/unit/layers/attention/test_verify_mask.py`, `test/registered/unit/model_executor/model_runner_components/test_attention_backend_setup.py`, `test/registered/unit/spec/test_dflash_overlap_hostsync.py`_
- **2026-09-01** [`22337e9c56`](https://github.com/sgl-project/sglang/commit/22337e9c56) [#37307](https://github.com/sgl-project/sglang/pull/37307)
  fix(unified-memory): forward the KV-index translator through every wrapper backend (#37307)
  _Files: `python/sglang/srt/layers/attention/dots_hybrid_backend.py`, `python/sglang/srt/layers/attention/hybrid_attn_backend.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py` _+4 more__
- **2026-09-01** [`71cee04ebe`](https://github.com/sgl-project/sglang/commit/71cee04ebe) [#36680](https://github.com/sgl-project/sglang/pull/36680)
  [Diffusion] Optimize Qwen-Image TP collectives and attention (#36680)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image.mdx`, `docs/docs/sglang-diffusion/performance-optimization.mdx`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py` _+15 more__
- **2026-09-01** [`f50b4ad7ae`](https://github.com/sgl-project/sglang/commit/f50b4ad7ae) [#33926](https://github.com/sgl-project/sglang/pull/33926)
  [DCP] Support decode context parallelism on the trtllm_mla decode path (#33926)
  _Files: `python/sglang/srt/layers/attention/cutedsl_mla_backend.py`, `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `test/registered/dcp/test_tokenspeed_mla_dcp_metadata.py` _+1 more__
- **2026-08-31** [`455232de6e`](https://github.com/sgl-project/sglang/commit/455232de6e) [#37301](https://github.com/sgl-project/sglang/pull/37301)
  [Cookbook] Enable DSpark on the DeepSeek-V4 Flash Vision low-latency recipes (#37301)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-08-31** [`961beee9e5`](https://github.com/sgl-project/sglang/commit/961beee9e5) [#35154](https://github.com/sgl-project/sglang/pull/35154)
  fix(unified-memory): four boot/correctness fixes on the hybrid model paths (#35154)
  _Files: `python/sglang/kernels/jit/csrc/inkling/causal_conv1d.cuh`, `python/sglang/kernels/jit/csrc/inkling/draft_extend_sconv.cuh`, `python/sglang/kernels/jit/csrc/inkling/fused_decode_update.cuh`, `python/sglang/kernels/jit/csrc/inkling/gather_scatter_sconv.cuh` _+13 more__
- **2026-08-31** [`88cf5c9541`](https://github.com/sgl-project/sglang/commit/88cf5c9541) [#37293](https://github.com/sgl-project/sglang/pull/37293)
  [Cookbook] Add DeepSeek-V4-Flash-Vision-Exp to the DeepSeek-V4 page (#37293)
  _Files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx` _+4 more__
- **2026-08-31** [`07d84ebd6d`](https://github.com/sgl-project/sglang/commit/07d84ebd6d) [#36933](https://github.com/sgl-project/sglang/pull/36933)
  [2/N][Mixed] Mixed chunk prefill with spec enabled (#36933)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/schedule_batch.py` _+9 more__
- **2026-08-31** [`a874b83c2c`](https://github.com/sgl-project/sglang/commit/a874b83c2c) [#37214](https://github.com/sgl-project/sglang/pull/37214)
  test: re-enable DSV4-Flash W8A8 8p nightly perf cases (#37214)
  _Files: `test/registered/npu/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in32k_out1k_50ms.py`, `test/registered/npu/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in8k_out1k_50ms.py`_
- **2026-08-31** [`a53718e88c`](https://github.com/sgl-project/sglang/commit/a53718e88c) [#37219](https://github.com/sgl-project/sglang/pull/37219)
  fix(ci): update attention backend test fixtures (#37219)
  _Files: `python/sglang/multimodal_gen/test/unit/test_attention_backend_selector.py`_
- **2026-08-31** [`712a720c8a`](https://github.com/sgl-project/sglang/commit/712a720c8a) [#33722](https://github.com/sgl-project/sglang/pull/33722)
  [KDA] Fused-accept state advance for FlashInfer KDA MTP verify (#33722)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashinfer.py`, `python/sglang/srt/layers/attention/mamba/mamba2_metadata.py` _+1 more__
- **2026-08-31** [`f61bb7b40a`](https://github.com/sgl-project/sglang/commit/f61bb7b40a) [#37170](https://github.com/sgl-project/sglang/pull/37170)
  [unified-memory] Drop the vacated 'dense' qualifier and the restating comments (#37170)
  _Files: `python/sglang/kernels/ops/kvcache/kv_read_table.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/unified_memory_pool.py` _+14 more__
- **2026-08-31** [`8bb776dc48`](https://github.com/sgl-project/sglang/commit/8bb776dc48) [#34613](https://github.com/sgl-project/sglang/pull/34613)
  feat(unified-memory): read unified pool from attention backends fa3/flashinfer/trtllm_mha/flashmla (#34613)
  _Files: `python/sglang/kernels/ops/attention/metadata.py`, `python/sglang/kernels/ops/kvcache/kv_indices.py`, `python/sglang/kernels/ops/kvcache/trtllm_mha_graph_metadata.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py` _+27 more__
- **2026-08-31** [`29578d5578`](https://github.com/sgl-project/sglang/commit/29578d5578) [#35245](https://github.com/sgl-project/sglang/pull/35245)
  refactor(unified-memory): translate the KV write location once, at ForwardBatch construction (#35245)
  _Files: `python/sglang/kernels/ops/kvcache/__init__.py`, `python/sglang/kernels/ops/kvcache/kv_indices.py`, `python/sglang/kernels/ops/kvcache/kv_read_table.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py` _+24 more__
- **2026-08-31** [`62c470697e`](https://github.com/sgl-project/sglang/commit/62c470697e) [#36907](https://github.com/sgl-project/sglang/pull/36907)
  [diffusion] chore: enforce component attention backend application (#36907)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py` _+8 more__
- **2026-08-31** [`3139ceaeec`](https://github.com/sgl-project/sglang/commit/3139ceaeec) [#33318](https://github.com/sgl-project/sglang/pull/33318)
  [XPU] Use SYCL kernels for topk_transform on XPU (#33318)
  _Files: `python/sglang/kernels/ops/attention/dsv4/topk.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py`_
- **2026-08-31** [`4f761e8649`](https://github.com/sgl-project/sglang/commit/4f761e8649) [#36954](https://github.com/sgl-project/sglang/pull/36954)
  [Deps] Bump FlashInfer to 0.6.18 (#36954)
  _Files: `docker/Dockerfile`, `docker/kimi_k3/apply_deepep_k3_patch.sh`, `docker/kimi_k3/kimi_k3_cu12.Dockerfile`, `docker/kimi_k3/kimi_k3_cu13.Dockerfile` _+5 more__

## Multimodal  (53 commits)

- **2026-09-07** [`ba6d3df69a`](https://github.com/sgl-project/sglang/commit/ba6d3df69a) [#38296](https://github.com/sgl-project/sglang/pull/38296)
  [diffusion] doc: document verified GB300 and derived GB200 H3 recipes (#38296)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/scripts/check_cookbook_configs.mjs`, `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx`_
- **2026-09-07** [`15d2cbcc90`](https://github.com/sgl-project/sglang/commit/15d2cbcc90) [#38185](https://github.com/sgl-project/sglang/pull/38185)
  [diffusion] CI: validate every repeated server request (#38185)
  _Files: `docs/docs/sglang-diffusion/ci_perf.mdx`, `python/sglang/multimodal_gen/test/server/conftest.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json` _+3 more__
- **2026-09-07** [`97dcbf9410`](https://github.com/sgl-project/sglang/commit/97dcbf9410) [#36654](https://github.com/sgl-project/sglang/pull/36654)
  [XPU] Re-add intel xpu on triton paths in diffusion platforms  (#36654)
  _Files: `python/sglang/kernels/ops/diffusion/common/platform.py`, `python/sglang/multimodal_gen/runtime/platforms/__init__.py`_
- **2026-09-07** [`ff08bcdda9`](https://github.com/sgl-project/sglang/commit/ff08bcdda9) [#38226](https://github.com/sgl-project/sglang/pull/38226)
  [diffusion] UX: quiet internal warmup frame searches (#38226)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/diffusers_generic.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/longlive2.py` _+6 more__
- **2026-09-07** [`e3140fb9d4`](https://github.com/sgl-project/sglang/commit/e3140fb9d4) [#38239](https://github.com/sgl-project/sglang/pull/38239)
  [diffusion] CI: rebalance 2-gpu shards and cut the job timeout to 45m (#38239)
  _Files: `.github/workflows/pr-test-multimodal-gen.yml`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/unit/test_suite_partitioning.py`_
- **2026-09-07** [`b83f1bdd21`](https://github.com/sgl-project/sglang/commit/b83f1bdd21) [#38225](https://github.com/sgl-project/sglang/pull/38225)
  [diffusion] fix: stabilize H3 reference audio across repeated requests (#38225)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_audio_vae/audio_vae.py`, `python/sglang/multimodal_gen/test/test_utils.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_vae_parallel_modes.py`_
- **2026-09-06** [`f3d05644db`](https://github.com/sgl-project/sglang/commit/f3d05644db) [#35674](https://github.com/sgl-project/sglang/pull/35674)
  [diffusion] docs+skill: document which components to stream under layerwise offload (#35674)
  _Files: `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-performance/SKILL.md`_
- **2026-09-06** [`ade1da017f`](https://github.com/sgl-project/sglang/commit/ade1da017f) [#37456](https://github.com/sgl-project/sglang/pull/37456)
  [diffusion] docs: verify the DGX Spark H3 recipe (#37456)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx`_
- **2026-09-06** [`a176ba2f7b`](https://github.com/sgl-project/sglang/commit/a176ba2f7b) [#37916](https://github.com/sgl-project/sglang/pull/37916)
  [diffusion] feat: measure warmup memory and layer usage per phase for residency calibration (1/4) (#37916)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/ltx_2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/sana_wm.py` _+53 more__
- **2026-09-06** [`938dc5621d`](https://github.com/sgl-project/sglang/commit/938dc5621d) [#38127](https://github.com/sgl-project/sglang/pull/38127)
  [diffusion] refactor: reuse plain state-dict loading without per-model classes (#38127)
  _Files: `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/composed_pipeline_base.py`, `python/sglang/multimodal_gen/test/unit/test_component_loader_identity.py` _+1 more__
- **2026-09-06** [`a9944aec01`](https://github.com/sgl-project/sglang/commit/a9944aec01) [#38172](https://github.com/sgl-project/sglang/pull/38172)
  [diffusion] CI: guard the allocated vram peak with reporting the reserved one (#38172)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/test/server/conftest.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/5090.json`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json` _+4 more__
- **2026-09-06** [`d61378af77`](https://github.com/sgl-project/sglang/commit/d61378af77) [#38148](https://github.com/sgl-project/sglang/pull/38148)
  docs(diffusion): add per-model tuning decision table to performance guide (#38148)
  _Files: `docs/docs/sglang-diffusion/performance-optimization.mdx`_
- **2026-09-06** [`67e3ccda97`](https://github.com/sgl-project/sglang/commit/67e3ccda97) [#38171](https://github.com/sgl-project/sglang/pull/38171)
  [diffusion] fix: restore non-layer placeholders before releasing host copies (#38171)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-09-05** [`eda10c3678`](https://github.com/sgl-project/sglang/commit/eda10c3678) [#38110](https://github.com/sgl-project/sglang/pull/38110)
  [Diffusion] Enable breakable CUDA graph for JoyEcho (#38110)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/joy_echo/denoising.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`_
- **2026-09-05** [`50c1bf0db0`](https://github.com/sgl-project/sglang/commit/50c1bf0db0) [#38020](https://github.com/sgl-project/sglang/pull/38020)
  [Diffusion] Port the Wan VAE decoder fast paths to the Qwen-Image VAE (#38020)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md`, `python/sglang/multimodal_gen/runtime/models/vaes/autoencoder_kl_qwenimage.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wan_vae_cuda_opt.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py` _+1 more__
- **2026-09-05** [`0bdc15d20f`](https://github.com/sgl-project/sglang/commit/0bdc15d20f) [#34424](https://github.com/sgl-project/sglang/pull/34424)
  [AMD] Fix ROCm VAE Conv2D fast path breaking spatial-parallel decode (#34424)
  _Files: `python/sglang/multimodal_gen/runtime/layers/parallel_conv.py`, `python/sglang/multimodal_gen/runtime/platforms/rocm.py`_
- **2026-09-05** [`da76fa073f`](https://github.com/sgl-project/sglang/commit/da76fa073f) [#38012](https://github.com/sgl-project/sglang/pull/38012)
  [diffusion] fix: fix host-resident vocab tables loaded on GPU (#38012)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_host_resident_vocab_table.py`_
- **2026-09-05** [`e980c1a2f1`](https://github.com/sgl-project/sglang/commit/e980c1a2f1) [#37971](https://github.com/sgl-project/sglang/pull/37971)
  fix(glm4v): disambiguate mixed image video offsets (#37971)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/glm4v.py`, `test/registered/unit/multimodal/test_glm4v_mixed_offsets.py`_
- **2026-09-05** [`d6e0a8cbf4`](https://github.com/sgl-project/sglang/commit/d6e0a8cbf4) [#38042](https://github.com/sgl-project/sglang/pull/38042)
  [diffusion] add Helios per-token gated-residual fusion (quality-gated) (#38042)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/sites/helios_gated_residual_site.py`, `python/sglang/multimodal_gen/runtime/models/dits/helios.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py` _+1 more__
- **2026-09-05** [`85da5457de`](https://github.com/sgl-project/sglang/commit/85da5457de) [#38001](https://github.com/sgl-project/sglang/pull/38001)
  [diffusion] auto-keep video DiT resident on high-memory GPUs (#38001)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/helios.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/sana_wm.py`, `python/sglang/multimodal_gen/runtime/server_args/auto_tune.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-09-04** [`9c254df8cd`](https://github.com/sgl-project/sglang/commit/9c254df8cd) [#37965](https://github.com/sgl-project/sglang/pull/37965)
  [diffusion] fix: preserve mapped courier tensor lifetime (#37965)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/5090.json`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json` _+3 more__
- **2026-09-04** [`5cd2a7661d`](https://github.com/sgl-project/sglang/commit/5cd2a7661d) [#38023](https://github.com/sgl-project/sglang/pull/38023)
  fix: reformat cosmos3_edge.py to satisfy ruff-format (#38023)
  _Files: `python/sglang/srt/multimodal/processors/cosmos3_edge.py`_
- **2026-09-04** [`88021b0734`](https://github.com/sgl-project/sglang/commit/88021b0734) [#37915](https://github.com/sgl-project/sglang/pull/37915)
  [diffusion] chore: make nightly performance measurements robust (#37915)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_nightly_comparison.py`, `python/sglang/multimodal_gen/test/unit/test_openai_image_api.py` _+4 more__
- **2026-09-04** [`978cc228ca`](https://github.com/sgl-project/sglang/commit/978cc228ca) [#37967](https://github.com/sgl-project/sglang/pull/37967)
  [Rust] Bound multimodal media ingress (#37967)
  _Files: `python/sglang/srt/rust_server/config.py`, `rust/sglang-mm/README.md`, `rust/sglang-mm/src/common/fetch.rs`, `rust/sglang-mm/src/driver.rs` _+3 more__
- **2026-09-04** [`3b678549c3`](https://github.com/sgl-project/sglang/commit/3b678549c3) [#37945](https://github.com/sgl-project/sglang/pull/37945)
  [diffusion] chore: warm up minimax-h3 at the served clip shape (#37945)
  _Files: `python/sglang/multimodal_gen/configs/sample/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_admission.py`_
- **2026-09-04** [`12735c2d76`](https://github.com/sgl-project/sglang/commit/12735c2d76) [#34660](https://github.com/sgl-project/sglang/pull/34660)
  [mm] refactor mm code for rust tokenizer manager (#34660)
  _Files: `python/sglang/srt/rust_server/multimodal.py`, `python/sglang/srt/rust_server/server.py`, `rust/sglang-mm/src/qwen_vl/mod.rs`, `rust/sglang-server/src/lib.rs` _+12 more__
- **2026-09-04** [`01e66a62db`](https://github.com/sgl-project/sglang/commit/01e66a62db) [#37890](https://github.com/sgl-project/sglang/pull/37890)
  [Diffusion] Improve BCG warmup frame-count diagnostics for video models (#37890)
  _Files: `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/runner.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`_
- **2026-09-04** [`06b8749803`](https://github.com/sgl-project/sglang/commit/06b8749803) [#37891](https://github.com/sgl-project/sglang/pull/37891)
  [Diffusion][Docs] Add single-GPU large-VRAM performance notes (B300) (#37891)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-performance/SKILL.md`_
- **2026-09-04** [`97d081ac76`](https://github.com/sgl-project/sglang/commit/97d081ac76) [#37805](https://github.com/sgl-project/sglang/pull/37805)
  [diffusion] chore: remove unreachable cosmos3 transfer encoding (#37805)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`_
- **2026-09-04** [`c1b4d535d7`](https://github.com/sgl-project/sglang/commit/c1b4d535d7) [#37895](https://github.com/sgl-project/sglang/pull/37895)
  [CI] Fix lint (#37895)
  _Files: `python/sglang/multimodal_gen/test/unit/test_webui.py`_
- **2026-09-04** [`5e81d462c3`](https://github.com/sgl-project/sglang/commit/5e81d462c3) [#33994](https://github.com/sgl-project/sglang/pull/33994)
  [diffusion] fix: only use fused qk_norm on nvidia gpu (#33994)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`_
- **2026-09-04** [`6c63d678d5`](https://github.com/sgl-project/sglang/commit/6c63d678d5) [#36320](https://github.com/sgl-project/sglang/pull/36320)
  [diffusion] webui: fix minimax h3 webui inference settings (#36320)
  _Files: `python/sglang/multimodal_gen/apps/webui/README.md`, `python/sglang/multimodal_gen/apps/webui/main.py`, `python/sglang/multimodal_gen/apps/webui/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_webui.py`_
- **2026-09-04** [`667bc043dc`](https://github.com/sgl-project/sglang/commit/667bc043dc) [#37687](https://github.com/sgl-project/sglang/pull/37687)
  [CI] remove MINIMAX_H3_HF_TOKEN (#37687)
  _Files: `.github/workflows/pr-test-multimodal-gen.yml`_
- **2026-09-04** [`2a0602c7ac`](https://github.com/sgl-project/sglang/commit/2a0602c7ac) [#37835](https://github.com/sgl-project/sglang/pull/37835)
  [diffusion] optimization: unfused w2 bias on SM12.x (cuBLAS 16x16 kernel mis-dispatch) for minimax-h3 vae decoder: (#37835)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/base_module.py`_
- **2026-09-03** [`bf71035d39`](https://github.com/sgl-project/sglang/commit/bf71035d39) [#37266](https://github.com/sgl-project/sglang/pull/37266)
  [diffusion] MiniMax-H3: tiered AdaLN plan cache (pinned-host tier + per-plan LRU) (#37266)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py` _+11 more__
- **2026-09-03** [`14444c6a04`](https://github.com/sgl-project/sglang/commit/14444c6a04) [#35922](https://github.com/sgl-project/sglang/pull/35922)
  [diffusion] feat: add maybe_record_function profiler spans for request phases (#35922)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/executors/pipeline_executor.py` _+1 more__
- **2026-09-03** [`1fb85053e7`](https://github.com/sgl-project/sglang/commit/1fb85053e7) [#36349](https://github.com/sgl-project/sglang/pull/36349)
  [AMD][Diffusion] Migrate FlyDSL fused norm kernels to the v0.3.0 stable API (#36349)
  _Files: `python/sglang/kernels/ops/diffusion/norm/fused_residual_norm_flydsl.py`, `test/registered/kernels/ops/diffusion/test_norm_flydsl.py`_
- **2026-09-03** [`4b0edb25f2`](https://github.com/sgl-project/sglang/commit/4b0edb25f2) [#35313](https://github.com/sgl-project/sglang/pull/35313)
  [CPU] Update base image to Ubuntu 26.04 (#35313)
  _Files: `docker/xeon.Dockerfile`_
- **2026-09-03** [`fbf909b460`](https://github.com/sgl-project/sglang/commit/fbf909b460) [#37320](https://github.com/sgl-project/sglang/pull/37320)
  [Fix] Alpha-channel images and tool-result media ordering (port of #36507) (#37320)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/glm4v.py` _+10 more__
- **2026-09-03** [`ff04a00d73`](https://github.com/sgl-project/sglang/commit/ff04a00d73) [#37330](https://github.com/sgl-project/sglang/pull/37330)
  Reduce tokenizer overhead and offload CUDA VMM publication (#37330)
  _Files: `python/sglang/srt/constrained/llguidance_backend.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/utils/cuda_vmm_transport_utils.py`, `test/registered/unit/multimodal/test_cuda_vmm_transport.py` _+1 more__
- **2026-09-02** [`f6aed6ec53`](https://github.com/sgl-project/sglang/commit/f6aed6ec53) [#36987](https://github.com/sgl-project/sglang/pull/36987)
  [diffusion] doc: rewrite stale diffusion compatibility matrix (#36987)
  _Files: `docs/cookbook/diffusion/FLUX/FLUX.mdx`, `docs/cookbook/diffusion/Krea/Krea-2.mdx`, `docs/cookbook/diffusion/MOVA/MOVA.mdx`, `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-Edit.mdx` _+13 more__
- **2026-09-02** [`fe3d4b9bbb`](https://github.com/sgl-project/sglang/commit/fe3d4b9bbb) [#37566](https://github.com/sgl-project/sglang/pull/37566)
  fix: restore missing get_component_forced_attn_backend import in minimax_h3 (#37566)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`_
- **2026-09-02** [`2f03d305e9`](https://github.com/sgl-project/sglang/commit/2f03d305e9) [#37340](https://github.com/sgl-project/sglang/pull/37340)
  [XPU] Add Regular Docker Image Release workflow for Intel XPU (#37340)
  _Files: `.github/workflows/release-docker-intel-xpu.yml`_
- **2026-09-02** [`1aa8299d1d`](https://github.com/sgl-project/sglang/commit/1aa8299d1d) [#37422](https://github.com/sgl-project/sglang/pull/37422)
  [Diffusion] Add cumulative extra-high quality tier (#37422)
  _Files: `docs/cookbook/diffusion/LingBot-World/LingBot-World-2.0.mdx`, `docs/cookbook/diffusion/LingBot-World/LingBot-World.mdx`, `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx` _+30 more__
- **2026-09-01** [`5993f91f84`](https://github.com/sgl-project/sglang/commit/5993f91f84) [#37385](https://github.com/sgl-project/sglang/pull/37385)
  [Kernel] Register merged diffusion agent kernels with KDA backend (#37385)
  _Files: `python/sglang/kernels/fused_op.py`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/norm_scale_shift_jit.py`, `python/sglang/kernels/spec.py` _+2 more__
- **2026-09-01** [`ce7e79b32c`](https://github.com/sgl-project/sglang/commit/ce7e79b32c) [#36216](https://github.com/sgl-project/sglang/pull/36216)
  [AMD] Fix nightly ROCm 7.0 image build: patch missing <optional> include in AITER topk kernel (#36216)
  _Files: `docker/rocm.Dockerfile`_
- **2026-09-01** [`ae2bd5728b`](https://github.com/sgl-project/sglang/commit/ae2bd5728b) [#37047](https://github.com/sgl-project/sglang/pull/37047)
  [vlm] fix: contain multimodal feature transport failures (#37047)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+12 more__
- **2026-09-01** [`079afaffb1`](https://github.com/sgl-project/sglang/commit/079afaffb1) [#37112](https://github.com/sgl-project/sglang/pull/37112)
  [Diffusion] Fuse FLUX.2 gated residual normalization on Blackwell (#37112)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/flux2_gated_resnorm.cuh`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/flux2_gated_resnorm_jit.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py` _+1 more__
- **2026-08-31** [`1da86b9801`](https://github.com/sgl-project/sglang/commit/1da86b9801) [#37220](https://github.com/sgl-project/sglang/pull/37220)
  [Rust] Split and rename embedded server components (#37220)
  _Files: `python/sglang/srt/managers/rust_server.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/idle_sleeper.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py` _+37 more__
- **2026-08-31** [`771e613d96`](https://github.com/sgl-project/sglang/commit/771e613d96) [#37144](https://github.com/sgl-project/sglang/pull/37144)
  [Diffusion] Fuse Qwen-Image final adaptive LayerNorm (#37144)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`, `test/registered/kernels/benchmark/diffusion/bench_qwen_image_modulation.py`, `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-08-31** [`0674be736c`](https://github.com/sgl-project/sglang/commit/0674be736c) [#37225](https://github.com/sgl-project/sglang/pull/37225)
  [AMD] build gfx1250 release image from main (#37225)
  _Files: `.github/workflows/release-docker-amd-rocm10.yml`_
- **2026-08-31** [`df75ec5f77`](https://github.com/sgl-project/sglang/commit/df75ec5f77) [#35877](https://github.com/sgl-project/sglang/pull/35877)
  [Intel GPU] Add rust support to XPU docker images (#35877)
  _Files: `docker/xpu.Dockerfile`_
- **2026-08-31** [`bb5e619860`](https://github.com/sgl-project/sglang/commit/bb5e619860) [#37116](https://github.com/sgl-project/sglang/pull/37116)
  [diffusion] perf: absorb Qwen-Image output projection biases (#37116)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/norm_scale_shift.cuh`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/norm_scale_shift_jit.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py` _+1 more__

## Prefill / Decode Disaggregation  (41 commits)

- **2026-09-07** [`62a4a6ea0e`](https://github.com/sgl-project/sglang/commit/62a4a6ea0e) [#37373](https://github.com/sgl-project/sglang/pull/37373)
  [NPU] Add NPU arch35 support and enhance DSV4 processing in DeepSeek-V4 (#37373)
  _Files: `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/disaggregation/ascend/transfer_engine.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/environ.py` _+21 more__
- **2026-09-07** [`df623d3cbd`](https://github.com/sgl-project/sglang/commit/df623d3cbd) [#38195](https://github.com/sgl-project/sglang/pull/38195)
  fix: keep queued Mooncake linker loads after abort (#38195)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`_
- **2026-09-07** [`b99175dc7d`](https://github.com/sgl-project/sglang/commit/b99175dc7d) [#38049](https://github.com/sgl-project/sglang/pull/38049)
  [Config] Round 6.4: the runtime reads the bags, not the record (#38049)
  _Files: `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/encoder/grpc_server.py`, `python/sglang/srt/disaggregation/encoder/http_server.py` _+81 more__
- **2026-09-06** [`31d28a2961`](https://github.com/sgl-project/sglang/commit/31d28a2961) [#38112](https://github.com/sgl-project/sglang/pull/38112)
  [NPU] Fix failed test cases in pr‑test‑npu and improve execution efficiency (#38112)
  _Files: `.github/workflows/pr-test-npu.yml`, `python/sglang/multimodal_gen/test/server/ascend/conftest.py`, `python/sglang/multimodal_gen/test/server/ascend/testcase_configs_npu.py`, `test/registered/npu/basic_function/parallel_strategy/data_parallelism/test_npu_load_balance_method.py` _+7 more__
- **2026-09-06** [`8ef646a5c6`](https://github.com/sgl-project/sglang/commit/8ef646a5c6) [#36944](https://github.com/sgl-project/sglang/pull/36944)
  fix(vlm): contain EPD request lifecycle failures (#36944)
  _Files: `python/sglang/srt/disaggregation/encoder/grpc_server.py`, `python/sglang/srt/disaggregation/encoder/http_server.py`, `python/sglang/srt/disaggregation/encoder/runtime.py`, `python/sglang/srt/disaggregation/encoder/server.py` _+4 more__
- **2026-09-06** [`febb360519`](https://github.com/sgl-project/sglang/commit/febb360519) [#36988](https://github.com/sgl-project/sglang/pull/36988)
  [VLM] retire aborted disaggregated prefill results (#36988)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `test/registered/disaggregation/test_disaggregation_basic.py`, `test/registered/disaggregation/test_disaggregation_chunked_prefill_abort.py`, `test/registered/unit/disaggregation/test_prefill_abort_result_cleanup.py` _+1 more__
- **2026-09-06** [`f5819b09bf`](https://github.com/sgl-project/sglang/commit/f5819b09bf) [#38163](https://github.com/sgl-project/sglang/pull/38163)
  Revert "[AMD][DSV4] Fix unified-KV pool sizing and SWA ring accounting" (#38163)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/kernels/ops/attention/dsv4/attn.py`, `python/sglang/kernels/ops/attention/dsv4/compress.py`, `python/sglang/srt/disaggregation/decode.py` _+19 more__
- **2026-09-05** [`514b45fd34`](https://github.com/sgl-project/sglang/commit/514b45fd34) [#30315](https://github.com/sgl-project/sglang/pull/30315)
  [AMD][DSV4] Fix unified-KV pool sizing and SWA ring accounting (#30315)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/kernels/ops/attention/dsv4/attn.py`, `python/sglang/kernels/ops/attention/dsv4/compress.py`, `python/sglang/srt/disaggregation/decode.py` _+19 more__
- **2026-09-05** [`5df60a21cd`](https://github.com/sgl-project/sglang/commit/5df60a21cd) [#36945](https://github.com/sgl-project/sglang/pull/36945)
  fix(vlm): harden EPD receiver validation and liveness (#36945)
  _Files: `python/sglang/srt/disaggregation/encoder/receiver.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/multimodal/processors/base_processor.py` _+8 more__
- **2026-09-05** [`a18106bbc3`](https://github.com/sgl-project/sglang/commit/a18106bbc3) [#36949](https://github.com/sgl-project/sglang/pull/36949)
  fix(vlm): make EPD cache publication transactional (#36949)
  _Files: `python/sglang/srt/disaggregation/encoder/runtime.py`, `python/sglang/srt/disaggregation/encoder/server.py`, `python/sglang/srt/distributed/device_communicators/mooncake_transfer_engine.py`, `python/sglang/srt/mem_cache/embedding_cache_controller.py` _+2 more__
- **2026-09-05** [`0454c074b4`](https://github.com/sgl-project/sglang/commit/0454c074b4) [#38103](https://github.com/sgl-project/sglang/pull/38103)
  [mem_cache] Clean up unified allocator leftovers (#38103)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/hisparse.py`, `python/sglang/srt/mem_cache/allocator/paged.py` _+4 more__
- **2026-09-05** [`3a770da756`](https://github.com/sgl-project/sglang/commit/3a770da756) [#34565](https://github.com/sgl-project/sglang/pull/34565)
  [Unified Tree] Support Branching-Point Caching for the SWA Component (#34565)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` _+6 more__
- **2026-09-05** [`0645398a32`](https://github.com/sgl-project/sglang/commit/0645398a32) [#38072](https://github.com/sgl-project/sglang/pull/38072)
  [mem_cache] Move the unified-memory allocators into `allocator/` and split the composites out (#38072)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/managers/scheduler_components/pool_stats_observer.py`, `python/sglang/srt/mem_cache/allocator/base.py` _+25 more__
- **2026-09-04** [`010dc955be`](https://github.com/sgl-project/sglang/commit/010dc955be) [#37636](https://github.com/sgl-project/sglang/pull/37636)
  [Metrics] Export scheduler stage wall time (#37636)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py` _+13 more__
- **2026-09-04** [`8b1d8c1703`](https://github.com/sgl-project/sglang/commit/8b1d8c1703) [#37461](https://github.com/sgl-project/sglang/pull/37461)
  [Metrics] Add rolling scheduler utilization counters (#37461)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py` _+7 more__
- **2026-09-04** [`4349538c02`](https://github.com/sgl-project/sglang/commit/4349538c02) [#33572](https://github.com/sgl-project/sglang/pull/33572)
  [model] add cosmos3 reasoner to llm only inference (#33572)
  _Files: `docker/Dockerfile`, `docs/docs/supported-models/multimodal_language_models.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/srt/configs/__init__.py` _+18 more__
- **2026-09-04** [`ed67b73081`](https://github.com/sgl-project/sglang/commit/ed67b73081) [#37804](https://github.com/sgl-project/sglang/pull/37804)
  [diffusion] UX: reduce hot-path server log noise (#37804)
  _Files: `python/sglang/multimodal_gen/runtime/disaggregation/orchestrator.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`, `python/sglang/multimodal_gen/runtime/vla/cuda_graph.py`_
- **2026-09-04** [`6147a54ddf`](https://github.com/sgl-project/sglang/commit/6147a54ddf) [#37874](https://github.com/sgl-project/sglang/pull/37874)
  [PD] Bound transfer engine init with `SGLANG_DISAGGREGATION_ENGINE_INIT_TIMEOUT` (#37874)
  _Files: `python/sglang/srt/disaggregation/ascend/transfer_engine.py`, `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `python/sglang/srt/distributed/device_communicators/mooncake_transfer_engine.py` _+3 more__
- **2026-09-03** [`4dc9cda5f9`](https://github.com/sgl-project/sglang/commit/4dc9cda5f9) [#37454](https://github.com/sgl-project/sglang/pull/37454)
  [PD] Gate deferred decode KV release on backend capability (#37454)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/fake/conn.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-09-03** [`2a980cbf10`](https://github.com/sgl-project/sglang/commit/2a980cbf10) [#37729](https://github.com/sgl-project/sglang/pull/37729)
  [mem_cache] Require page-aligned starts in `free_segment` and drop the boundary trim (#37729)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/paged.py`, `python/sglang/srt/mem_cache/multi_ended_allocator.py` _+3 more__
- **2026-09-03** [`abed680320`](https://github.com/sgl-project/sglang/commit/abed680320) [#37381](https://github.com/sgl-project/sglang/pull/37381)
  [Unified Cache][5/N]: Integrate external linker mode end to end (#37381)
  _Files: `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py` _+9 more__
- **2026-09-03** [`3bac084d4e`](https://github.com/sgl-project/sglang/commit/3bac084d4e) [#37654](https://github.com/sgl-project/sglang/pull/37654)
  [Model] Add native IFM K2 Horizon serving support (#37654)
  _Files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/k2_horizon.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/constrained/grammar_manager.py` _+30 more__
- **2026-09-03** [`db1eb48651`](https://github.com/sgl-project/sglang/commit/db1eb48651) [#37485](https://github.com/sgl-project/sglang/pull/37485)
  [CI] Graceful teardown for the PD and HiSparse server fixtures (#37485)
  _Files: `python/sglang/test/server_fixtures/disaggregation_fixture.py`, `test/registered/amd/accuracy/mi30x/test_glm51_hisparse_eval_mi30x.py`, `test/registered/amd/accuracy/mi35x/test_glm51_hisparse_eval_mi35x.py`, `test/registered/models_e2e/test_dsa_glm52_hisparse.py` _+2 more__
- **2026-09-02** [`c05f8ae830`](https://github.com/sgl-project/sglang/commit/c05f8ae830) [#37146](https://github.com/sgl-project/sglang/pull/37146)
  [PD] Optimize paged allocator free-list release (#37146)
  _Files: `python/sglang/srt/hardware_backend/npu/allocator_npu.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/paged.py` _+4 more__
- **2026-09-02** [`3a855b050a`](https://github.com/sgl-project/sglang/commit/3a855b050a) [#37483](https://github.com/sgl-project/sglang/pull/37483)
  fix(disagg): poll receivers during decode preallocation (#37483)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-09-02** [`f8cbf000f4`](https://github.com/sgl-project/sglang/commit/f8cbf000f4) [#37353](https://github.com/sgl-project/sglang/pull/37353)
  [AMD] Enable FP4 indexer for Deepseek V4 (#37353)
  _Files: `docker/rocm.Dockerfile`, `python/sglang/kernels/ops/attention/dsv4/compress.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_hip.py`, `python/sglang/srt/arg_groups/serving_hook.py` _+17 more__
- **2026-09-02** [`8b596c10b0`](https://github.com/sgl-project/sglang/commit/8b596c10b0) [#37302](https://github.com/sgl-project/sglang/pull/37302)
  [PD] Diversify fake-prefill handoff tokens (#37302)
  _Files: `python/sglang/srt/disaggregation/decode.py`_
- **2026-09-01** [`3484f7f836`](https://github.com/sgl-project/sglang/commit/3484f7f836) [#36721](https://github.com/sgl-project/sglang/pull/36721)
  [mem_cache] Add `free_kv_row` to release a request's kv row by row range (#36721)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/chunk_cache.py`, `python/sglang/srt/mem_cache/common.py` _+8 more__
- **2026-09-01** [`959ca033eb`](https://github.com/sgl-project/sglang/commit/959ca033eb) [#37299](https://github.com/sgl-project/sglang/pull/37299)
  refactor(hicache): simplify decode offload state bookkeeping (#37299)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/disaggregation/kv_events.py`, `test/registered/unit/disaggregation/test_specv2_kvcache_offloading.py`_
- **2026-09-01** [`b21000aef1`](https://github.com/sgl-project/sglang/commit/b21000aef1) [#37205](https://github.com/sgl-project/sglang/pull/37205)
  [Unified Cache][4/N]: Add Mooncake backend for external linker (#37205)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`_
- **2026-09-01** [`3b14f37b74`](https://github.com/sgl-project/sglang/commit/3b14f37b74) [#37339](https://github.com/sgl-project/sglang/pull/37339)
  [Fix] Use real ReqKvInfo in unit-test req mocks (#37339)
  _Files: `test/registered/unit/beam_search/test_fork.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`, `test/registered/unit/managers/test_hisparse_unit.py`, `test/registered/unit/managers/test_priority_scheduling_disaggregation.py` _+3 more__
- **2026-08-31** [`ef9e58fd6d`](https://github.com/sgl-project/sglang/commit/ef9e58fd6d) [#35177](https://github.com/sgl-project/sglang/pull/35177)
  feat(unified-memory): three sub-pools for mamba + hybrid-SWA models (#35177)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/managers/scheduler_components/pool_stats_observer.py`, `python/sglang/srt/mem_cache/common.py` _+10 more__
- **2026-08-31** [`2530204502`](https://github.com/sgl-project/sglang/commit/2530204502) [#37167](https://github.com/sgl-project/sglang/pull/37167)
  [mem_cache] Make release, row-reuse asserts, and presence checks read the KV record (#37167)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_req_to_token_pool.py`, `python/sglang/srt/managers/scheduler.py` _+9 more__
- **2026-08-31** [`48098b5f23`](https://github.com/sgl-project/sglang/commit/48098b5f23) [#37221](https://github.com/sgl-project/sglang/pull/37221)
  [Rust] Derive server address and accept signed env values (#37221)
  _Files: `python/sglang/srt/rust_server/server.py`, `rust/sglang-server/src/api_server/disaggregation/bootstrap.rs`, `rust/sglang-server/src/api_server/native_api.rs`, `rust/sglang-server/src/lib.rs` _+4 more__
- **2026-08-31** [`9e9d26a4af`](https://github.com/sgl-project/sglang/commit/9e9d26a4af) [#37201](https://github.com/sgl-project/sglang/pull/37201)
  Fix Mooncake serving benchmark trace rows (#37201)
  _Files: `python/sglang/benchmark/serving.py`_
- **2026-08-31** [`9cf157c252`](https://github.com/sgl-project/sglang/commit/9cf157c252) [#32710](https://github.com/sgl-project/sglang/pull/32710)
  [Radix Cache] Add Rust TreeCore backend with shared parity tests (#32710)
  _Files: `.github/actions/download-rust-ext/action.yml`, `.github/workflows/_pr-test-rust-ext-build.yml`, `.github/workflows/release-pypi-nightly.yml`, `.github/workflows/release-pypi-pr.yml` _+68 more__
- **2026-08-31** [`2cb3f32b03`](https://github.com/sgl-project/sglang/commit/2cb3f32b03) [#36875](https://github.com/sgl-project/sglang/pull/36875)
  [diffusion] chore: preserve exact component identity during loading (#36875)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/runtime/disaggregation/roles.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/adapter_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py` _+6 more__
- **2026-08-31** [`3a6ed55999`](https://github.com/sgl-project/sglang/commit/3a6ed55999) [#37194](https://github.com/sgl-project/sglang/pull/37194)
  [Fix] Shut hicache test servers down gracefully before SIGKILL (#37194)
  _Files: `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`, `test/registered/disaggregation/test_disaggregation_decode_offload.py`, `test/registered/hicache/test_hicache_storage.py`, `test/registered/hicache/test_hicache_storage_file_backend.py` _+9 more__
- **2026-08-31** [`5d12ad4fd7`](https://github.com/sgl-project/sglang/commit/5d12ad4fd7) [#37164](https://github.com/sgl-project/sglang/pull/37164)
  [mem_cache] Move mamba state and `retraction_backup` into `ReqKvInfo` (#37164)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/auxiliary_state.py`, `python/sglang/srt/hardware_backend/mlx/model_runner.py` _+26 more__
- **2026-08-31** [`2ea6d17eab`](https://github.com/sgl-project/sglang/commit/2ea6d17eab) [#37166](https://github.com/sgl-project/sglang/pull/37166)
  fix(staging): make empty staging rings reusable (#37166)
  _Files: `python/sglang/srt/disaggregation/common/staging_buffer.py`, `python/sglang/srt/disaggregation/common/staging_handler.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-08-31** [`7700602278`](https://github.com/sgl-project/sglang/commit/7700602278) [#35281](https://github.com/sgl-project/sglang/pull/35281)
  [PD] Align defensive protocol behavior across Mooncake, NIXL, and Mori (#35281)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`_

## MoE / Expert Parallel  (40 commits)

- **2026-09-07** [`861d40f3ee`](https://github.com/sgl-project/sglang/commit/861d40f3ee) [#34919](https://github.com/sgl-project/sglang/pull/34919)
  Fix DSpark CUDA graph replay with MegaMoE TP attention (#34919)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py`_
- **2026-09-07** [`b6c31b155c`](https://github.com/sgl-project/sglang/commit/b6c31b155c) [#36228](https://github.com/sgl-project/sglang/pull/36228)
  [CP V1 Deprecation 3/5] Remove generic prefill CP v1 runtime (#36228)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/arg_groups/pipeline.py` _+30 more__
- **2026-09-07** [`aaf9a95763`](https://github.com/sgl-project/sglang/commit/aaf9a95763) [#38113](https://github.com/sgl-project/sglang/pull/38113)
  [Config] Round 6.5: a namespace declares what it derives, next to what it derives it from (#38113)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/benchmark/one_batch.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/test/unit/test_component_accuracy_parallel_runtime.py` _+52 more__
- **2026-09-07** [`a8b2f36dee`](https://github.com/sgl-project/sglang/commit/a8b2f36dee) [#37376](https://github.com/sgl-project/sglang/pull/37376)
  [kernel] add fused silu mul quant fp8 (#37376)
  _Files: `python/sglang/kernels/aot/benchmark/bench_silu_quant_fp8.py`, `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `test/registered/kernels/ops/quantization/test_fused_silu_mul_quant_fp8.py`_
- **2026-09-07** [`214313ee79`](https://github.com/sgl-project/sglang/commit/214313ee79) [#30430](https://github.com/sgl-project/sglang/pull/30430)
  Fuse Nemotron latent MoE projection and shared add (#30430)
  _Files: `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/nemotron_h.py`, `test/registered/unit/layers/quantization/test_unquant_apply_with_addend.py`, `test/registered/unit/models/test_nemotron_h_shared_add.py`_
- **2026-09-07** [`c4e52a1051`](https://github.com/sgl-project/sglang/commit/c4e52a1051) [#24959](https://github.com/sgl-project/sglang/pull/24959)
  XPU: Enable GLM5.1 (GlmMoeDsaForCausalLM) DSA Attention (#24959)
  _Files: `python/sglang/kernels/ops/attention/dsa/index_buf_accessor.py`, `python/sglang/srt/arg_groups/memory_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py` _+9 more__
- **2026-09-07** [`30705c004c`](https://github.com/sgl-project/sglang/commit/30705c004c) [#33608](https://github.com/sgl-project/sglang/pull/33608)
  [Deepseek V4] Keep fp32 routing weights in the mxfp4 trtllm MoE (#33608)
  _Files: `python/sglang/srt/layers/quantization/mxfp4_flashinfer_trtllm_moe.py`_
- **2026-09-06** [`28457f0dca`](https://github.com/sgl-project/sglang/commit/28457f0dca) [#37199](https://github.com/sgl-project/sglang/pull/37199)
  fix(gpt-oss): avoid duplicate MoE reduction with DP attention (#37199)
  _Files: `python/sglang/srt/models/gpt_oss.py`, `test/registered/models_e2e/test_gpt_oss_4gpu_mxfp4.py`_
- **2026-09-05** [`dc2843801d`](https://github.com/sgl-project/sglang/commit/dc2843801d) [#37622](https://github.com/sgl-project/sglang/pull/37622)
  perf(lfm2): fuse gating and short convolution on SM90 (#37622)
  _Files: `python/sglang/kernels/ops/mamba/lfm_short_conv.py`, `python/sglang/srt/models/lfm2_moe.py`, `test/registered/kernels/ops/mamba/test_lfm_short_conv.py`_
- **2026-09-05** [`1e6f18bfeb`](https://github.com/sgl-project/sglang/commit/1e6f18bfeb) [#32405](https://github.com/sgl-project/sglang/pull/32405)
  [MoE Refactor] Migrate SM100 trtllm-gen mxfp4 MoE onto MoeRunner (#32405)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutlass.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `test/registered/unit/layers/quantization/test_mxfp4_situ_output.py` _+2 more__
- **2026-09-05** [`bd16c22a04`](https://github.com/sgl-project/sglang/commit/bd16c22a04) [#38044](https://github.com/sgl-project/sglang/pull/38044)
  [diffusion] fuse LingBot MoE group-limited top-k index selection (#38044)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/routing/__init__.py` _+5 more__
- **2026-09-05** [`d49180019b`](https://github.com/sgl-project/sglang/commit/d49180019b) [#38085](https://github.com/sgl-project/sglang/pull/38085)
  fix(moe): cast filtered-activation expert_ids to int32 for torch.compile (#38085)
  _Files: `python/sglang/kernels/ops/activation/activation.py`, `test/registered/kernels/ops/activation/test_activation.py`_
- **2026-09-05** [`92a4d8b5ee`](https://github.com/sgl-project/sglang/commit/92a4d8b5ee) [#33930](https://github.com/sgl-project/sglang/pull/33930)
  Clean logging under --weight-loader-prefetch-checkpoints (#33930)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`, `python/sglang/srt/layers/cp/cp_decode_attn_tp.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` _+15 more__
- **2026-09-05** [`55bf3380e0`](https://github.com/sgl-project/sglang/commit/55bf3380e0) [#36805](https://github.com/sgl-project/sglang/pull/36805)
  Support Hy4-preview (#36805)
  _Files: `python/sglang/kernels/ops/layernorm/__init__.py`, `python/sglang/kernels/ops/layernorm/hy4_ihc.py`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/kernels/ops/moe/triton_pad_expert_counts.py` _+43 more__
- **2026-09-04** [`54c2c99feb`](https://github.com/sgl-project/sglang/commit/54c2c99feb) [#37910](https://github.com/sgl-project/sglang/pull/37910)
  [Diffusion] Fuse LingBot per-token gated residual and RMSNorm modulate (#37910)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/kda_kernels/csrc/diffusion/residual_gate_add.cuh`, `python/sglang/kernels/kda_kernels/residual_gate_add_jit.py`, `python/sglang/kernels/ops/diffusion/__init__.py` _+5 more__
- **2026-09-04** [`72078cd7f5`](https://github.com/sgl-project/sglang/commit/72078cd7f5) [#35751](https://github.com/sgl-project/sglang/pull/35751)
  [XPU] Support GPT-OSS MXFP4 checkpoints on Intel XPU (#35751)
  _Files: `docs/docs/advanced_features/quantization.mdx`, `docs/docs/hardware-platforms/xpu.mdx`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/quantization/__init__.py` _+1 more__
- **2026-09-03** [`fd70325c10`](https://github.com/sgl-project/sglang/commit/fd70325c10) [#37665](https://github.com/sgl-project/sglang/pull/37665)
  [CI] Add dspark + dsv4 e2e test (#37665)
  _Files: `test/registered/models_e2e/test_deepseek_v4_flash_fp4_b200.py`, `test/registered/models_e2e/test_deepseek_v4_flash_fp4_megamoe_b200.py`_
- **2026-09-03** [`392841f47c`](https://github.com/sgl-project/sglang/commit/392841f47c) [#37825](https://github.com/sgl-project/sglang/pull/37825)
  [Bugfix] Support K2 Horizon MoE without MoVA (#37825)
  _Files: `python/sglang/srt/models/xllm.py`_
- **2026-09-03** [`a6001478f4`](https://github.com/sgl-project/sglang/commit/a6001478f4) [#33838](https://github.com/sgl-project/sglang/pull/33838)
  [AMD] Perf Kimi-K3 MoE optimization (#33838)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `test/registered/unit/layers/moe/test_topk_correction_bias_cache.py`, `test/registered/unit/layers/quantization/test_mxfp4_situ_output.py` _+1 more__
- **2026-09-03** [`397aeca376`](https://github.com/sgl-project/sglang/commit/397aeca376) [#37623](https://github.com/sgl-project/sglang/pull/37623)
  fix(benchmark): support Glm4MoeLite in fused MoE tuner (#37623)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`_
- **2026-09-03** [`02d9b3060a`](https://github.com/sgl-project/sglang/commit/02d9b3060a) [#37723](https://github.com/sgl-project/sglang/pull/37723)
  [Docs] Update K2 Horizon MoE model names (#37723)
  _Files: `docs/cookbook/autoregressive/IFM/K2-Horizon.mdx`, `docs/src/snippets/configs/IFM/k2-horizon.jsx`_
- **2026-09-03** [`2641e427be`](https://github.com/sgl-project/sglang/commit/2641e427be) [#37193](https://github.com/sgl-project/sglang/pull/37193)
  Xpu/weekly simple model enablement 2026 08 30 (#37193)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/ernie45_moe_vl.py` _+8 more__
- **2026-09-02** [`19c30dff56`](https://github.com/sgl-project/sglang/commit/19c30dff56) [#29927](https://github.com/sgl-project/sglang/pull/29927)
  [SM120] DeepSeek-V4: DeepGEMM paged-MQA indexer +FP4 MoE+ page-split  (#29927)
  _Files: `python/sglang/kernels/ops/attention/flash_mla_sm120.py`, `python/sglang/kernels/ops/layernorm/mhc.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` _+7 more__
- **2026-09-02** [`acea43079f`](https://github.com/sgl-project/sglang/commit/acea43079f) [#36407](https://github.com/sgl-project/sglang/pull/36407)
  Fix native MoE handling of noncontiguous top-k IDs (#36407)
  _Files: `python/sglang/srt/layers/moe/fused_moe_native.py`, `test/registered/unit/layers/moe/test_fused_moe_native.py`_
- **2026-09-02** [`c66a285c94`](https://github.com/sgl-project/sglang/commit/c66a285c94) [#37477](https://github.com/sgl-project/sglang/pull/37477)
  [Kernel] GLM 5.3 Flash related kernels (ported from #36507) (#37477)
  _Files: `python/sglang/kernels/jit/csrc/dsa/kpool_topk_transform.cuh`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dsa/transform_index.py`, `python/sglang/kernels/ops/attention/fla/kda.py` _+12 more__
- **2026-09-02** [`33428d3dae`](https://github.com/sgl-project/sglang/commit/33428d3dae) [#37331](https://github.com/sgl-project/sglang/pull/37331)
  Fix GPU kernel ordering and MXFP8 quantization dispatch (#37331)
  _Files: `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/registered/kernels/ops/moe/test_minimax_m3_mxfp8.py`_
- **2026-09-01** [`221a6273ce`](https://github.com/sgl-project/sglang/commit/221a6273ce) [#36811](https://github.com/sgl-project/sglang/pull/36811)
  [Kernel] Avoid zero-bias allocation in fused softmax routing (#36811)
  _Files: `python/sglang/kernels/ops/moe/moe_fused_gate.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/kernels/ops/moe/test_moe_fused_gate.py`_
- **2026-09-01** [`e57e934bcc`](https://github.com/sgl-project/sglang/commit/e57e934bcc) [#32882](https://github.com/sgl-project/sglang/pull/32882)
  [Bugfix] Accept int64 top-k IDs in FlashInfer routed MoE packer (#32882)
  _Files: `python/sglang/kernels/ops/moe/pack_topk_ids.py`_
- **2026-09-01** [`ee462b5899`](https://github.com/sgl-project/sglang/commit/ee462b5899) [#37158](https://github.com/sgl-project/sglang/pull/37158)
  [Kernel] Add tuned LFM2.5 Triton MoE configs on B300 (#37158)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=32,N=1792,device_name=NVIDIA_B300_SXM6_AC.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=32,N=1792,device_name=NVIDIA_B300_SXM6_AC_down.json`_
- **2026-09-01** [`5e79110122`](https://github.com/sgl-project/sglang/commit/5e79110122) [#37338](https://github.com/sgl-project/sglang/pull/37338)
  [Fix][CPU] fix xeon ci failure by test_qwen35_flashinfer_fusion (#37338)
  _Files: `test/registered/unit/layers/moe/test_qwen35_flashinfer_fusion.py`_
- **2026-09-01** [`5b04408784`](https://github.com/sgl-project/sglang/commit/5b04408784) [#34967](https://github.com/sgl-project/sglang/pull/34967)
  [MoE] Add FlashInfer SM90 MXFP4 W4A8 CUTLASS MoE (#34967)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx` _+9 more__
- **2026-09-01** [`e6f21cdadc`](https://github.com/sgl-project/sglang/commit/e6f21cdadc) [#36624](https://github.com/sgl-project/sglang/pull/36624)
  [Cohere Command-A-Plus] Optimize decode and BCG capture on SM10X (#36624)
  _Files: `python/sglang/srt/arg_groups/model_overrides/__init__.py`, `python/sglang/srt/arg_groups/model_overrides/cohere2_moe.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/cohere2_moe.py` _+1 more__
- **2026-09-01** [`97744189b8`](https://github.com/sgl-project/sglang/commit/97744189b8) [#37317](https://github.com/sgl-project/sglang/pull/37317)
  [Kernel] Raise shape limits in shared FLA and MoE kernels (ported from #36507) (#37317)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `python/sglang/kernels/ops/attention/fla/cumsum.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py` _+1 more__
- **2026-09-01** [`9a85473a89`](https://github.com/sgl-project/sglang/commit/9a85473a89) [#35120](https://github.com/sgl-project/sglang/pull/35120)
  [FlashInfer v0.6.18] add FlashInfer CuTe DSL NVFP4 W4A16 mode (#35120)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/moe_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/logits_processor.py` _+8 more__
- **2026-09-01** [`07c8f7294d`](https://github.com/sgl-project/sglang/commit/07c8f7294d) [#37279](https://github.com/sgl-project/sglang/pull/37279)
  Bump sgl-deep-gemm to 0.1.7 (#37279)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/arg_groups/mega_moe_hook.py`, `python/sglang/srt/layers/moe/mega_moe.py` _+4 more__
- **2026-08-31** [`95f0f41021`](https://github.com/sgl-project/sglang/commit/95f0f41021) [#34074](https://github.com/sgl-project/sglang/pull/34074)
  [CI] Move tests onto the right CI stages (#34074)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/weekly-test-cpu.yml`, `.github/workflows/weekly-test-nvidia.yml`, `python/sglang/test/test_utils.py` _+71 more__
- **2026-08-31** [`d60d658f5f`](https://github.com/sgl-project/sglang/commit/d60d658f5f) [#37159](https://github.com/sgl-project/sglang/pull/37159)
  [Kernel] Add GB300 Triton MoE configs for GLM-4.5 FP8 (#37159)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=161,N=192,device_name=NVIDIA_GB300,dtype=fp8_w8a8,per_channel_quant=True.json`_
- **2026-08-31** [`3865efc9f7`](https://github.com/sgl-project/sglang/commit/3865efc9f7) [#36871](https://github.com/sgl-project/sglang/pull/36871)
  [AMD] support gfx1250 on ROCM 10 (#36871)
  _Files: `.github/workflows/release-docker-amd-rocm7_15-nightly.yml`, `docker/rocm.Dockerfile`, `python/pyproject_other.toml`, `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce_base.h` _+31 more__
- **2026-08-31** [`4f997a432a`](https://github.com/sgl-project/sglang/commit/4f997a432a) [#36985](https://github.com/sgl-project/sglang/pull/36985)
  test: re-enable FlashInfer per-token NVFP4 coverage (#36985)
  _Files: `test/registered/backends/test_flashinfer_nvfp4_online_moe_backend.py`, `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`_
- **2026-08-31** [`046454404a`](https://github.com/sgl-project/sglang/commit/046454404a) [#31041](https://github.com/sgl-project/sglang/pull/31041)
  [Spec] Add LFM2 and LFM2-MoE DSpark speculative decoding support (#31041)
  _Files: `python/sglang/kernels/ops/speculative/dspark/fused_kv_write.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/models/lfm2.py`, `python/sglang/srt/models/lfm2_dspark.py` _+1 more__

## KV Cache / Memory  (38 commits)

- **2026-09-07** [`c5367fa964`](https://github.com/sgl-project/sglang/commit/c5367fa964) [#38315](https://github.com/sgl-project/sglang/pull/38315)
  [CI] Fix stale ServerArgs fake in chunked-SGMV LoRA test (#38315)
  _Files: `test/registered/kernels/ops/gemm/test_chunked_sgmv_cuda_graph.py`_
- **2026-09-07** [`6e312af8c2`](https://github.com/sgl-project/sglang/commit/6e312af8c2) [#38204](https://github.com/sgl-project/sglang/pull/38204)
  fix: collect prefix hash values iteratively (#38204)
  _Files: `python/sglang/srt/mem_cache/mamba_radix_cache.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`_
- **2026-09-07** [`f25848913d`](https://github.com/sgl-project/sglang/commit/f25848913d) [#38138](https://github.com/sgl-project/sglang/pull/38138)
  fix: preserve SWA host lock on node split (#38138)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py`_
- **2026-09-06** [`5bebe7a033`](https://github.com/sgl-project/sglang/commit/5bebe7a033) [#38108](https://github.com/sgl-project/sglang/pull/38108)
  [Router] Add bucket-aware policy domains and native cache indexing (#38108)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/benches/policy_select.rs`, `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/monitoring/grafana-dashboard.json` _+72 more__
- **2026-09-05** [`4b44a1cde2`](https://github.com/sgl-project/sglang/commit/4b44a1cde2) [#37795](https://github.com/sgl-project/sglang/pull/37795)
  [Refactor] Let eviction policies take construction parameters (#37795)
  _Files: `docs/docs.json`, `docs/docs/advanced_features/radix_eviction_policy.mdx`, `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py` _+5 more__
- **2026-09-05** [`f1f2380d2b`](https://github.com/sgl-project/sglang/commit/f1f2380d2b) [#37578](https://github.com/sgl-project/sglang/pull/37578)
  [Unified Cache][6/N]: Add UMBP external linker (#37578)
  _Files: `python/sglang/srt/mem_cache/registry.py`, `python/sglang/srt/mem_cache/storage/umbp/umbp_direct_linker.py`, `python/sglang/srt/mem_cache/storage/umbp/umbp_host_allocator.py`, `python/sglang/srt/mem_cache/storage/umbp/umbp_store.py` _+5 more__
- **2026-09-05** [`a44bb397a9`](https://github.com/sgl-project/sglang/commit/a44bb397a9) [#37938](https://github.com/sgl-project/sglang/pull/37938)
  [Perf] Vectorize alloc_extend_naive to remove the per-request Python loop (#37938)
  _Files: `python/sglang/srt/mem_cache/allocator/paged.py`_
- **2026-09-04** [`01e19ddf55`](https://github.com/sgl-project/sglang/commit/01e19ddf55) [#38021](https://github.com/sgl-project/sglang/pull/38021)
  chore: add code owners for the Rust radix tree core (#38021)
  _Files: `.github/CODEOWNERS`_
- **2026-09-04** [`0d0e2f92be`](https://github.com/sgl-project/sglang/commit/0d0e2f92be) [#37424](https://github.com/sgl-project/sglang/pull/37424)
  [HiCache] Buffer mode support sidecar pool (#37424)
  _Files: `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_buffer_mode_sidecar.py`_
- **2026-09-04** [`19b46863f3`](https://github.com/sgl-project/sglang/commit/19b46863f3) [#37278](https://github.com/sgl-project/sglang/pull/37278)
  fix: align write-through pending across tree cores (#37278)
  _Files: `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py` _+9 more__
- **2026-09-04** [`e4adf63275`](https://github.com/sgl-project/sglang/commit/e4adf63275) [#36415](https://github.com/sgl-project/sglang/pull/36415)
  [Fix] Vacuous marker writes in the cache tests, and an undebited Mamba admission slot (#36415)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-04** [`f3b2725609`](https://github.com/sgl-project/sglang/commit/f3b2725609) [#37898](https://github.com/sgl-project/sglang/pull/37898)
  sm120 32GB mem-tier: raise decode cuda-graph max_bs 24->48 + chunked_prefill 2k->4k (#37898)
  _Files: `python/sglang/srt/arg_groups/memory_hook.py`_
- **2026-09-04** [`67248e04b4`](https://github.com/sgl-project/sglang/commit/67248e04b4) [#37876](https://github.com/sgl-project/sglang/pull/37876)
  [mem_cache] Route hybrid SWA full-side kv-row frees through `free_segment` (#37876)
  _Files: `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/swa.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/multi_ended_allocator.py` _+7 more__
- **2026-09-04** [`f478b2bb2d`](https://github.com/sgl-project/sglang/commit/f478b2bb2d) [#35255](https://github.com/sgl-project/sglang/pull/35255)
  Fix: abort handling for dispatched requests after client disconnect (#35255)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_scheduler_chunked_abort_race.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py` _+2 more__
- **2026-09-04** [`59799a3687`](https://github.com/sgl-project/sglang/commit/59799a3687) [#33824](https://github.com/sgl-project/sglang/pull/33824)
  [Simulator] Add high-fidelity CPU-based inference simulator (#33824)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/_pr-test-simulator-cpu.yml`, `.github/workflows/pr-test-extra.yml`, `.gitignore` _+77 more__
- **2026-09-03** [`b44496389c`](https://github.com/sgl-project/sglang/commit/b44496389c) [#37883](https://github.com/sgl-project/sglang/pull/37883)
  [HiCache] Count hit allocations and in-flight backups in the buffer pipeline idle check (#37883)
  _Files: `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`_
- **2026-09-03** [`a480f388b2`](https://github.com/sgl-project/sglang/commit/a480f388b2) [#37503](https://github.com/sgl-project/sglang/pull/37503)
  [HiCache] L3 storage prefetch lifecycle metrics and cross-tier attribution fixes (#37503)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py` _+15 more__
- **2026-09-03** [`05dbe64dff`](https://github.com/sgl-project/sglang/commit/05dbe64dff) [#37567](https://github.com/sgl-project/sglang/pull/37567)
  Fix buffer-mode idle tracking and VLM memory sizing (#37567)
  _Files: `python/sglang/srt/arg_groups/memory_hook.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`_
- **2026-09-03** [`d0c95f6c91`](https://github.com/sgl-project/sglang/commit/d0c95f6c91) [#37464](https://github.com/sgl-project/sglang/pull/37464)
  [HiCache] buffer mode: anchor-lock staged prefetches by default (#37464)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-03** [`68978f8d52`](https://github.com/sgl-project/sglang/commit/68978f8d52) [#37502](https://github.com/sgl-project/sglang/pull/37502)
  [Scheduler] Count the parked chunked-prefill request in the busy mem check (#37502)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`_
- **2026-09-03** [`23ab10a63e`](https://github.com/sgl-project/sglang/commit/23ab10a63e) [#36403](https://github.com/sgl-project/sglang/pull/36403)
  Support speculative decoding with unified SWA memory (#36403)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/multi_ended_allocator.py`, `python/sglang/srt/model_executor/pool_configurator.py`_
- **2026-09-03** [`33a22b1b08`](https://github.com/sgl-project/sglang/commit/33a22b1b08) [#37844](https://github.com/sgl-project/sglang/pull/37844)
  [Cache] Forward fast prefix matching capability (#37844)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/managers/test_load_inquirer.py`_
- **2026-09-03** [`54da74e83e`](https://github.com/sgl-project/sglang/commit/54da74e83e) [#37675](https://github.com/sgl-project/sglang/pull/37675)
  [Fix] Broadcast PP dynamic-chunk profiling failures so every rank disables together (#37675)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/dynamic_chunk_sizer.py`_
- **2026-09-03** [`cf3173aeb9`](https://github.com/sgl-project/sglang/commit/cf3173aeb9) [#37324](https://github.com/sgl-project/sglang/pull/37324)
  [Perf] Walk the radix tree by offset instead of re-slicing token storage (ported from #36507) (#37324)
  _Files: `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`_
- **2026-09-03** [`a522c8a4b6`](https://github.com/sgl-project/sglang/commit/a522c8a4b6) [#37674](https://github.com/sgl-project/sglang/pull/37674)
  [misc] Extract PP dynamic chunk sizing into a `DynamicChunkSizer` scheduler component (#37674)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/dynamic_chunk_sizer.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/manual/chunked_prefill/test_scripted_pp.py` _+1 more__
- **2026-09-02** [`18d5ffb42a`](https://github.com/sgl-project/sglang/commit/18d5ffb42a) [#37511](https://github.com/sgl-project/sglang/pull/37511)
  Size the unified read-table grid from bs, and fuse the allocator's tombstone scatters (#37511)
  _Files: `python/sglang/kernels/ops/kvcache/kv_read_table.py`, `python/sglang/kernels/ops/memory/__init__.py`, `python/sglang/kernels/ops/memory/virtual_slot.py`, `python/sglang/srt/mem_cache/multi_ended_allocator.py` _+1 more__
- **2026-09-02** [`19c7679e9e`](https://github.com/sgl-project/sglang/commit/19c7679e9e) [#36723](https://github.com/sgl-project/sglang/pull/36723)
  [mem_cache] Make `free_swa` sync-free on `page_size == 1` (#36723)
  _Files: `python/sglang/srt/mem_cache/allocator/swa.py`, `test/registered/kv_canary/test_self_e2e_perturb_req_to_token.py`, `test/registered/unit/mem_cache/test_swa_unittest.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-02** [`862a909a08`](https://github.com/sgl-project/sglang/commit/862a909a08) [#37509](https://github.com/sgl-project/sglang/pull/37509)
  [Fix] Lock PP dynamic-chunk profiling requests before releasing through the tree cache (#37509)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`_
- **2026-09-02** [`01c3a5f54f`](https://github.com/sgl-project/sglang/commit/01c3a5f54f) [#36646](https://github.com/sgl-project/sglang/pull/36646)
  [misc] Resolve SWA ownership at enqueue time for grouped free() (#36646)
  _Files: `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/swa.py`, `test/registered/unit/mem_cache/test_swa_unittest.py`_
- **2026-09-02** [`832d029870`](https://github.com/sgl-project/sglang/commit/832d029870) [#37481](https://github.com/sgl-project/sglang/pull/37481)
  [mem_cache] Split duplicate insert frees at the SWA eviction floor (#37481)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `rust/sglang-radix-tree/src/tests/components/swa.rs`, `rust/sglang-radix-tree/src/unified_tree_core.rs`, `test/registered/unit/mem_cache/test_rust_tree_core_integration.py` _+1 more__
- **2026-09-02** [`a6a19f9290`](https://github.com/sgl-project/sglang/commit/a6a19f9290) [#37494](https://github.com/sgl-project/sglang/pull/37494)
  [Bugfix] Skip absent radix lock during cache cleanup (#37494)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_lock_ref.py`_
- **2026-09-01** [`83a9b5dd88`](https://github.com/sgl-project/sglang/commit/83a9b5dd88) [#37463](https://github.com/sgl-project/sglang/pull/37463)
  [mem_cache] Drop the `torch.unique` sync from the SWA page expansion (#37463)
  _Files: `python/sglang/srt/mem_cache/allocator/swa.py`_
- **2026-09-01** [`c34f378342`](https://github.com/sgl-project/sglang/commit/c34f378342) [#34362](https://github.com/sgl-project/sglang/pull/34362)
  fix(nixl): make FILE path-mode devId globally unique (#34362)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/nixl_registry.py`_
- **2026-09-01** [`a77283fb02`](https://github.com/sgl-project/sglang/commit/a77283fb02) [#37290](https://github.com/sgl-project/sglang/pull/37290)
  [Rust] Rename mem-cache to sglang-radix-tree (#37290)
  _Files: `.github/workflows/_pr-test-rust-ext-build.yml`, `.gitignore`, `.pre-commit-config.yaml`, `python/setup.py` _+26 more__
- **2026-08-31** [`98cb3535b7`](https://github.com/sgl-project/sglang/commit/98cb3535b7) [#35158](https://github.com/sgl-project/sglang/pull/35158)
  feat(unified-memory): byte-budget sizing, feasibility floor, and a conservation verifier (#35158)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` _+5 more__
- **2026-08-31** [`5d92e60783`](https://github.com/sgl-project/sglang/commit/5d92e60783) [#37151](https://github.com/sgl-project/sglang/pull/37151)
  [Unified Cache Linker][3/N]: Add backend-independent linker core (#37151)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_hiradix_pp_sync_drain.py`, `test/registered/unit/mem_cache/test_unified_cache_linker.py`_
- **2026-08-31** [`9a9e167179`](https://github.com/sgl-project/sglang/commit/9a9e167179) [#35588](https://github.com/sgl-project/sglang/pull/35588)
  [Bugfix] Fix full prefill CUDA graph padding and EAGLE capture (#35588)
  _Files: `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/cuda_graph/full_prefill/test_full_cuda_graph_prefill.py` _+3 more__
- **2026-08-31** [`62f86ce470`](https://github.com/sgl-project/sglang/commit/62f86ce470) [#37182](https://github.com/sgl-project/sglang/pull/37182)
  [CI] Fix unreachable FakeReq field initialization (#37182)
  _Files: `test/registered/unit/mem_cache/test_streaming_session_unit.py`_

## Quantization  (24 commits)

- **2026-09-06** [`e3f7097591`](https://github.com/sgl-project/sglang/commit/e3f7097591) [#38128](https://github.com/sgl-project/sglang/pull/38128)
  [diffusion] refactor: consolidate plain state-dict component loaders (#38128)
  _Files: `python/sglang/multimodal_gen/configs/models/base.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/adapter_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/bridge_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py` _+17 more__
- **2026-09-05** [`ccf9fe6590`](https://github.com/sgl-project/sglang/commit/ccf9fe6590) [#38082](https://github.com/sgl-project/sglang/pull/38082)
  [Kernel] Add KDA FP8 skinny GEMM for SM120 (#38082)
  _Files: `python/sglang/kernels/kda_kernels/README.md`, `python/sglang/kernels/kda_kernels/csrc/diffusion/causal_conv3d_cat_pad.cuh`, `python/sglang/kernels/kda_kernels/csrc/diffusion/ltx2_qknorm_split_rope.cuh`, `python/sglang/kernels/kda_kernels/csrc/diffusion/norm_scale_shift.cuh` _+10 more__
- **2026-09-05** [`756d0e0a85`](https://github.com/sgl-project/sglang/commit/756d0e0a85) [#38033](https://github.com/sgl-project/sglang/pull/38033)
  [Model] Add K2 Horizon FP8 checkpoint support (#38033)
  _Files: `python/sglang/srt/models/xllm.py`, `test/registered/unit/models/test_xllm.py`_
- **2026-09-05** [`bc727bc4ee`](https://github.com/sgl-project/sglang/commit/bc727bc4ee) [#38006](https://github.com/sgl-project/sglang/pull/38006)
  [FP8] SM120: route FP8 linear to per-tensor (cudnn/nvjet) instead of channelwise cutlass (#38006)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`_
- **2026-09-04** [`b42569a0f1`](https://github.com/sgl-project/sglang/commit/b42569a0f1) [#31755](https://github.com/sgl-project/sglang/pull/31755)
  [Quant][ue8m0 fix] group requant_weight_ue8m0 reduce reserved gpu memory (#31755)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-09-04** [`dae126d510`](https://github.com/sgl-project/sglang/commit/dae126d510) [#37658](https://github.com/sgl-project/sglang/pull/37658)
  [AMD][DSv4] Fuse inverse-RoPE into the fp8 wo_a quant (stacked on #37423) (#37658)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_common/amd/deepseek_v4_wo_a_fp8.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-09-04** [`1bda9694b7`](https://github.com/sgl-project/sglang/commit/1bda9694b7) [#37423](https://github.com/sgl-project/sglang/pull/37423)
  [AMD][DSv4] Switch output projection gemm (oproj_a) to fp8 (#37423)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/models/deepseek_common/amd/deepseek_v4_wo_a_fp8.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-09-04** [`94eb15eb6c`](https://github.com/sgl-project/sglang/commit/94eb15eb6c) [#36380](https://github.com/sgl-project/sglang/pull/36380)
  [diffusion] quant: support fp8 mixed precision for cosmos3 (#36380)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_fp8_step_precision.py`, `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py` _+1 more__
- **2026-09-04** [`795dd7abce`](https://github.com/sgl-project/sglang/commit/795dd7abce) [#37816](https://github.com/sgl-project/sglang/pull/37816)
  [diffusion] feat: compose third-party component bundles safely (#37816)
  _Files: `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/runtime/loader/minimax_h3_weights.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py` _+6 more__
- **2026-09-03** [`4372b8efa7`](https://github.com/sgl-project/sglang/commit/4372b8efa7) [#37552](https://github.com/sgl-project/sglang/pull/37552)
  [1/N] Quantization Refactor: remove dead code and dedup the FP4 marlin helpers (#37552)
  _Files: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/humming_utils.py` _+8 more__
- **2026-09-03** [`619ab2bcce`](https://github.com/sgl-project/sglang/commit/619ab2bcce) [#37849](https://github.com/sgl-project/sglang/pull/37849)
  Fix block-scale swizzling device placement (#37849)
  _Files: `python/sglang/srt/layers/quantization/utils.py`_
- **2026-09-03** [`9cb38a3d57`](https://github.com/sgl-project/sglang/commit/9cb38a3d57) [#37616](https://github.com/sgl-project/sglang/pull/37616)
  [diffusion] feat: filter duplicate precision variants across custom loaders (#37616)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/upsampler_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py` _+6 more__
- **2026-09-03** [`0dd66def7c`](https://github.com/sgl-project/sglang/commit/0dd66def7c) [#36922](https://github.com/sgl-project/sglang/pull/36922)
  [chore] harden checkpoint quantization metadata parsing (#36922)
  _Files: `python/sglang/multimodal_gen/test/unit/test_image_encoder_loader.py`, `python/sglang/srt/model_loader/checkpoint_quantization.py`, `test/registered/unit/model_loader/test_modelopt_loader.py`, `test/registered/unit/test_checkpoint_quantization.py`_
- **2026-09-02** [`f4c17fed07`](https://github.com/sgl-project/sglang/commit/f4c17fed07) [#37096](https://github.com/sgl-project/sglang/pull/37096)
  [Diffusion] Fuse FLUX.2 NVFP4 FC1, SwiGLU, and FC2 quantization (#37096)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/sites/flux2_nvfp4_swiglu_quant_site.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py` _+4 more__
- **2026-09-02** [`c593527f33`](https://github.com/sgl-project/sglang/commit/c593527f33) [#36865](https://github.com/sgl-project/sglang/pull/36865)
  [Kernel] Add KDA NVFP4 GEMM for Qwen3.x on SM120 (#36865)
  _Files: `python/sglang/kernels/kda_kernels/.clang-format`, `python/sglang/kernels/kda_kernels/README.md`, `python/sglang/kernels/kda_kernels/__init__.py`, `python/sglang/kernels/kda_kernels/causal_conv3d_cat_pad_jit.py` _+20 more__
- **2026-09-01** [`1c3ad92438`](https://github.com/sgl-project/sglang/commit/1c3ad92438) [#37162](https://github.com/sgl-project/sglang/pull/37162)
  [Diffusion] Fuse FLUX.2 ModelOpt FP8 producers and QKV packing (#37162)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/flux2_qkv_epilogue.cuh`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/layout/flux2_token_cat_fp8_triton.py`, `python/sglang/kernels/ops/diffusion/norm/layernorm_modulate_triton.py` _+12 more__
- **2026-09-01** [`1591dcd91a`](https://github.com/sgl-project/sglang/commit/1591dcd91a) [#35703](https://github.com/sgl-project/sglang/pull/35703)
  [diffusion] fix: fix loading a block-FP8 quantized MiniMax-H3 DiT (#35703)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_dit_contract.py`_
- **2026-09-01** [`175973d834`](https://github.com/sgl-project/sglang/commit/175973d834) [#37129](https://github.com/sgl-project/sglang/pull/37129)
  [Diffusion] Fuse Qwen-Image residual norm and NVFP4 quantization (#37129)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/norm_scale_shift.cuh`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/norm_scale_shift_jit.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py` _+2 more__
- **2026-09-01** [`6715debb2a`](https://github.com/sgl-project/sglang/commit/6715debb2a) [#37123](https://github.com/sgl-project/sglang/pull/37123)
  [Diffusion] Fuse Qwen-Image FP8 QKV projection and Blackwell epilogue (#37123)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qwen_qkv_epilogue.cuh`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/qwen_qkv_epilogue_jit.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py` _+5 more__
- **2026-08-31** [`52e1c24744`](https://github.com/sgl-project/sglang/commit/52e1c24744) [#37141](https://github.com/sgl-project/sglang/pull/37141)
  [Diffusion] Fuse FLUX.2 token concatenation and NVFP4 quantization (#37141)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/flux2_token_cat_nvfp4.cuh`, `python/sglang/kernels/jit/utils/deps.py`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/layout/flux2_token_cat_nvfp4_jit.py` _+5 more__
- **2026-08-31** [`1ed9bfac2c`](https://github.com/sgl-project/sglang/commit/1ed9bfac2c) [#37156](https://github.com/sgl-project/sglang/pull/37156)
  [Diffusion] Fuse Qwen-Image FP8 norm and activation quantization (#37156)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/norm_scale_shift.cuh`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/norm_scale_shift_jit.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py` _+3 more__
- **2026-08-31** [`28690f5aa5`](https://github.com/sgl-project/sglang/commit/28690f5aa5) [#36916](https://github.com/sgl-project/sglang/pull/36916)
  [diffusion] chore: detect quantized transformer replacements (#36916)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/base.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`, `python/sglang/multimodal_gen/test/unit/test_transformer_quant.py`_
- **2026-08-31** [`881cbfe54c`](https://github.com/sgl-project/sglang/commit/881cbfe54c) [#36991](https://github.com/sgl-project/sglang/pull/36991)
  [diffusion] feat: add exact component precision overrides (#36991)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/image_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/sound_tokenizer_loader.py` _+20 more__
- **2026-08-31** [`a9d5ca723a`](https://github.com/sgl-project/sglang/commit/a9d5ca723a) [#35805](https://github.com/sgl-project/sglang/pull/35805)
  [CPU] Fix weight missing issue in fused_input_proj_cpu for GPTQ INT4 for Qwen 3.5 (#35805)
  _Files: `python/sglang/srt/models/qwen3_5.py`_

## Other  (23 commits)

- **2026-09-07** [`4d23a4fa6d`](https://github.com/sgl-project/sglang/commit/4d23a4fa6d) [#37436](https://github.com/sgl-project/sglang/pull/37436)
  [Test] Consolidate test cleanup and CI taxonomy (net -11.4K lines) (#37436)
- **2026-09-07** [`6a1ff90f2d`](https://github.com/sgl-project/sglang/commit/6a1ff90f2d) [#38244](https://github.com/sgl-project/sglang/pull/38244)
  [CPU] use CustomTestCase for registered CPU tests (#38244)
  _Files: `test/registered/cpu/test_binding.py`, `test/registered/cpu/test_request_decompression.py`, `test/registered/cpu/test_request_headers.py`, `test/registered/cpu/test_server_args_backend.py`_
- **2026-09-07** [`503e36cbae`](https://github.com/sgl-project/sglang/commit/503e36cbae) [#38278](https://github.com/sgl-project/sglang/pull/38278)
  Tiny Update CI Permission (#38278)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-09-07** [`c8207e32b6`](https://github.com/sgl-project/sglang/commit/c8207e32b6) [#31113](https://github.com/sgl-project/sglang/pull/31113)
  [Intel][XPU] Add NUMA node binding support for Intel XPU (#31113)
  _Files: `python/sglang/srt/utils/numa_utils.py`, `test/registered/utils/test_numa_utils.py`, `test/registered/xpu/test_numa_utils_xpu.py`_
- **2026-09-07** [`6252993afe`](https://github.com/sgl-project/sglang/commit/6252993afe) [#38238](https://github.com/sgl-project/sglang/pull/38238)
  chore: update CI test est_time values (#38238)
- **2026-09-06** [`be00a543a7`](https://github.com/sgl-project/sglang/commit/be00a543a7) [#38117](https://github.com/sgl-project/sglang/pull/38117)
  perf: use Gumbel-max trick in the main sampler to cut decode CPU dispatch (#38117)
  _Files: `python/sglang/srt/layers/sampler.py`_
- **2026-09-05** [`ae3205ba28`](https://github.com/sgl-project/sglang/commit/ae3205ba28) [#37610](https://github.com/sgl-project/sglang/pull/37610)
  Fail fast on undersized swa pool (#37610)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-09-05** [`ecd97de1fc`](https://github.com/sgl-project/sglang/commit/ecd97de1fc) [#37843](https://github.com/sgl-project/sglang/pull/37843)
  [Router] Add load-aware prefill admission and bounded policy proposals (#37843)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/main.rs` _+51 more__
- **2026-09-04** [`d7f235daca`](https://github.com/sgl-project/sglang/commit/d7f235daca) [#37966](https://github.com/sgl-project/sglang/pull/37966)
  [Memory] Retire graph borrow pool before updating static runs (#37966)
  _Files: `python/sglang/srt/model_executor/runner_utils/pool.py`, `test/registered/unit/model_executor/runner_utils/test_graph_pool_borrow.py`_
- **2026-09-04** [`e3305b3b87`](https://github.com/sgl-project/sglang/commit/e3305b3b87) [#37922](https://github.com/sgl-project/sglang/pull/37922)
  Add code owner for sglang-simulator (#37922)
  _Files: `.github/CODEOWNERS`_
- **2026-09-03** [`0e5414fd2f`](https://github.com/sgl-project/sglang/commit/0e5414fd2f) [#37873](https://github.com/sgl-project/sglang/pull/37873)
  [Test] Allow top-k cutoff ties in `test_sampling_mask_matches_topk_logprobs` (#37873)
  _Files: `test/registered/sampling/test_sampling_mask.py`_
- **2026-09-03** [`27b7a2dc3b`](https://github.com/sgl-project/sglang/commit/27b7a2dc3b) [#34187](https://github.com/sgl-project/sglang/pull/34187)
  [Kimi K3] Rework skipped-think fix as opt-in force_nonempty_content with streaming coverage (#34187)
  _Files: `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/parser/test_kimik3_reasoning_parser.py`_
- **2026-09-03** [`e59a576f03`](https://github.com/sgl-project/sglang/commit/e59a576f03) [#36617](https://github.com/sgl-project/sglang/pull/36617)
  fix test/manual/test_forward_split_prefill.py UT due to many refactors and design changes (#36617)
  _Files: `test/manual/test_forward_split_prefill.py`_
- **2026-09-03** [`57c26a84e0`](https://github.com/sgl-project/sglang/commit/57c26a84e0) [#37210](https://github.com/sgl-project/sglang/pull/37210)
  [chore] Add .git-blame-ignore-revs for the black -> ruff-format reformat (#37210) (#37695)
  _Files: `.git-blame-ignore-revs`_
- **2026-09-03** [`046cdaabaa`](https://github.com/sgl-project/sglang/commit/046cdaabaa) [#36630](https://github.com/sgl-project/sglang/pull/36630)
  [Sampling] Capture masks from sampler support (#36630)
  _Files: `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/sampling/sampling_batch_info.py`, `test/registered/sampling/test_sampling_mask.py`_
- **2026-09-02** [`1109e44305`](https://github.com/sgl-project/sglang/commit/1109e44305) [#37529](https://github.com/sgl-project/sglang/pull/37529)
  update CODEOWNERS (#37529)
  _Files: `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS`_
- **2026-09-02** [`ffd273bf4a`](https://github.com/sgl-project/sglang/commit/ffd273bf4a) [#37209](https://github.com/sgl-project/sglang/pull/37209)
  Add polisettyvarma into CI_PERMISSION list (#37209)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-09-02** [`a58751d54d`](https://github.com/sgl-project/sglang/commit/a58751d54d) [#37335](https://github.com/sgl-project/sglang/pull/37335)
  [Fix ] Fix Spark2.5 hybrid SWA config (#37335)
  _Files: `python/sglang/srt/configs/spark2_5.py`_
- **2026-09-01** [`fb8d7eedda`](https://github.com/sgl-project/sglang/commit/fb8d7eedda) [#35491](https://github.com/sgl-project/sglang/pull/35491)
  Fix dummy initialization of inverse weight scales (#35491)
  _Files: `python/sglang/srt/model_loader/weight_utils.py`_
- **2026-09-01** [`49db27528a`](https://github.com/sgl-project/sglang/commit/49db27528a) [#35787](https://github.com/sgl-project/sglang/pull/35787)
  fix(test): deflake zmq load-snapshot round-trip tests (#35787)
  _Files: `test/registered/unit/managers/test_load_snapshot_backends.py`_
- **2026-08-31** [`579270d459`](https://github.com/sgl-project/sglang/commit/579270d459) [#37226](https://github.com/sgl-project/sglang/pull/37226)
  [Rust] Simplify request defaults and document batch header ABI (#37226)
  _Files: `rust/sglang-server/src/message/request.rs`, `rust/sglang-server/src/message/response.rs`_
- **2026-08-31** [`549166b819`](https://github.com/sgl-project/sglang/commit/549166b819) [#37249](https://github.com/sgl-project/sglang/pull/37249)
  fix(gateway): bump wfaas to 1.0.2 so ContinueNextStep unblocks dependents (#37249)
  _Files: `sgl-model-gateway/Cargo.toml`_
- **2026-08-31** [`0da6a66856`](https://github.com/sgl-project/sglang/commit/0da6a66856) [#37035](https://github.com/sgl-project/sglang/pull/37035)
  [MLX] Fix startup crash when reporting preloaded weights (#37035)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_runner_pool_contract.py`_

## Triton / Kernels  (22 commits)

- **2026-09-07** [`7d37b86ff2`](https://github.com/sgl-project/sglang/commit/7d37b86ff2) [#37886](https://github.com/sgl-project/sglang/pull/37886)
  Remove obsolete CUDA graph buffer population methods (#37886)
  _Files: `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_utils/buffers.py` _+1 more__
- **2026-09-07** [`39a80354aa`](https://github.com/sgl-project/sglang/commit/39a80354aa) [#36709](https://github.com/sgl-project/sglang/pull/36709)
  [MUSA] Add installation guide and Dockerfile (#36709)
  _Files: `docker/musa.Dockerfile`, `docs/docs/hardware-platforms/mthreads_gpu.mdx`, `docs/docs/hardware-platforms/overview.mdx`, `docs/index.mdx` _+2 more__
- **2026-09-07** [`707da81e84`](https://github.com/sgl-project/sglang/commit/707da81e84) [#35604](https://github.com/sgl-project/sglang/pull/35604)
  [CPU] Add native CPU kernel for MurmurHash32 (#35604)
  _Files: `python/sglang/kernels/aot/csrc/cpu/sampling.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/kernels/ops/sampling/murmur_hash.py`, `test/registered/cpu/test_sampling.py`_
- **2026-09-05** [`6a0c55fd6c`](https://github.com/sgl-project/sglang/commit/6a0c55fd6c) [#37696](https://github.com/sgl-project/sglang/pull/37696)
  [CI] Pin the Rust TreeCore build to the resolved libtorch instead of interpreter discovery (#37696)
  _Files: `python/sglang/srt/rust_extensions/torch_build.py`, `scripts/ci/cuda/ci_install_dependency.sh`, `test/registered/rust/test_rust_extension.py`, `test/registered/unit/tools/test_cuda_ci_install_dependency.py`_
- **2026-09-05** [`a74470e904`](https://github.com/sgl-project/sglang/commit/a74470e904) [#38039](https://github.com/sgl-project/sglang/pull/38039)
  fix(mamba): unify causal_conv1d col* dtype to x (MiniCPM-V-4.6 GDN prefill bf16/fp16 mismatch) (#38039)
  _Files: `python/sglang/kernels/ops/mamba/causal_conv1d_triton.py`, `test/registered/layers/mamba/test_causal_conv1d.py`_
- **2026-09-04** [`ebae8ee21e`](https://github.com/sgl-project/sglang/commit/ebae8ee21e) [#37937](https://github.com/sgl-project/sglang/pull/37937)
  [Fix] Register triton.runtime.cache.triton_key in the MPS stub so torch.compile keeps working (#37937)
  _Files: `python/sglang/_platform_stubs.py`, `test/registered/unit/platforms/test_mps_triton_stub.py`_
- **2026-09-03** [`0610a6539d`](https://github.com/sgl-project/sglang/commit/0610a6539d) [#37881](https://github.com/sgl-project/sglang/pull/37881)
  [CI] Add Lark notifications for CUDA CI status, runner health, and queue time (#37881)
  _Files: `.github/workflows/ci-lark-notify.yml`, `scripts/ci_monitor/README.md`, `scripts/ci_monitor/lark_notify.py`_
- **2026-09-03** [`54cadad151`](https://github.com/sgl-project/sglang/commit/54cadad151) [#37731](https://github.com/sgl-project/sglang/pull/37731)
  [Router] Add composable scoring and eligibility policies (#37731)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/policies/cache_aware_zmq.rs` _+32 more__
- **2026-09-03** [`49e6e81830`](https://github.com/sgl-project/sglang/commit/49e6e81830) [#37689](https://github.com/sgl-project/sglang/pull/37689)
  [CI] Accept t64-suffixed apt packages in the install skip check (#37689)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-09-03** [`80e8302d03`](https://github.com/sgl-project/sglang/commit/80e8302d03) [#36615](https://github.com/sgl-project/sglang/pull/36615)
  Add SGLANG_CRASH_ON_JIT_COMPILE to forbid on-the-fly JIT compilation (#36615)
  _Files: `python/sglang/kernels/jit/utils/compile/cache.py`, `python/sglang/kernels/jit/utils/compile/loader.py`, `python/sglang/srt/environ.py`_
- **2026-09-02** [`4bc34117f1`](https://github.com/sgl-project/sglang/commit/4bc34117f1) [#37672](https://github.com/sgl-project/sglang/pull/37672)
  [CI] Install lmms-eval from PyPI, drop human-eval install, add clone token fallback (#37672)
  _Files: `.github/workflows/rerun-test.yml`, `scripts/ci/cuda/ci_install_dependency.sh`, `scripts/ci/utils/git_clone_with_retry.sh`_
- **2026-09-02** [`ad6e830858`](https://github.com/sgl-project/sglang/commit/ad6e830858) [#37657](https://github.com/sgl-project/sglang/pull/37657)
  [Bugfix] Key CUDA graph dedup signatures on kernel function identity (#37657)
  _Files: `python/sglang/srt/model_executor/runner_backend/cuda_graph_dedup_mixin.py`_
- **2026-09-02** [`d9ae1ebabd`](https://github.com/sgl-project/sglang/commit/d9ae1ebabd) [#37508](https://github.com/sgl-project/sglang/pull/37508)
  [CI] Preserve NCCL 2.30.7 after dependency installs (#37508)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-09-02** [`66de38f30c`](https://github.com/sgl-project/sglang/commit/66de38f30c) [#37300](https://github.com/sgl-project/sglang/pull/37300)
  Decouple ragged CUDA graph request and token capacities (#37300)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`_
- **2026-09-02** [`9cc43ca4e1`](https://github.com/sgl-project/sglang/commit/9cc43ca4e1) [#37399](https://github.com/sgl-project/sglang/pull/37399)
  [NPU] Update sgl-kernel-npu version to 2026.9.0 and move memfabric deps into pyproject (#37399)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `docker/npu.Dockerfile`, `python/pyproject_npu.toml` _+1 more__
- **2026-09-01** [`f8618714c5`](https://github.com/sgl-project/sglang/commit/f8618714c5) [#36220](https://github.com/sgl-project/sglang/pull/36220)
  add reindex_device_id to device OOT plugin (#36220)
  _Files: `python/sglang/srt/platforms/cuda.py`, `python/sglang/srt/platforms/device_mixin.py`, `python/sglang/srt/utils/common.py`_
- **2026-09-01** [`cb6dd58fbe`](https://github.com/sgl-project/sglang/commit/cb6dd58fbe) [#34693](https://github.com/sgl-project/sglang/pull/34693)
  [Kernel] Replace dsv3_router_gemm with the unified tiny GEMM (#34693)
  _Files: `python/sglang/kernels/jit/csrc/gemm/dsv3_router_gemm.cuh`, `python/sglang/kernels/jit/csrc/gemm/tiny_gemm.cuh`, `python/sglang/kernels/ops/gemm/__init__.py`, `python/sglang/kernels/ops/gemm/dsv3_router_gemm.py` _+11 more__
- **2026-09-01** [`4c7ff0d906`](https://github.com/sgl-project/sglang/commit/4c7ff0d906) [#37435](https://github.com/sgl-project/sglang/pull/37435)
  [CI] Double JIT kernel unit test timeout (#37435)
  _Files: `.github/workflows/pr-test-jit-kernel.yml`_
- **2026-09-01** [`00689c0c94`](https://github.com/sgl-project/sglang/commit/00689c0c94) [#37406](https://github.com/sgl-project/sglang/pull/37406)
  [CI] Add entrypoint to hc_combine test for standalone execution (#37406)
  _Files: `test/registered/kernels/ops/layernorm/test_hc_combine.py`_
- **2026-09-01** [`b68702be99`](https://github.com/sgl-project/sglang/commit/b68702be99) [#35118](https://github.com/sgl-project/sglang/pull/35118)
  [DSV4] hc-prenorm: fuse the combine step into a Triton kernel (#35118)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/kernels/ops/layernorm/test_hc_combine.py`_
- **2026-08-31** [`b77cac06a9`](https://github.com/sgl-project/sglang/commit/b77cac06a9) [#36248](https://github.com/sgl-project/sglang/pull/36248)
  [PP] Support prefill CUDA graph proxy tensors (#36248)
  _Files: `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/memory_hook.py`, `python/sglang/srt/layers/cp/bcg.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py` _+8 more__
- **2026-08-31** [`afbca97f74`](https://github.com/sgl-project/sglang/commit/afbca97f74) [#36422](https://github.com/sgl-project/sglang/pull/36422)
  add suffix for xpu kernel upload space (#36422)
  _Files: `.github/workflows/release-whl-kernel-xpu.yml`, `scripts/update_kernel_whl_index.py`_

## CI / Build  (18 commits)

- **2026-09-05** [`9acbf75159`](https://github.com/sgl-project/sglang/commit/9acbf75159) [#38132](https://github.com/sgl-project/sglang/pull/38132)
  [CI][NPU] Fix pr-test-npu failing at Install dependencies with set: Illegal option -o pipefail (#38132)
  _Files: `.github/workflows/_npu-pr-test-stage.yml`_
- **2026-09-05** [`0948e6ebed`](https://github.com/sgl-project/sglang/commit/0948e6ebed) [#35489](https://github.com/sgl-project/sglang/pull/35489)
  [CI] Remove metrics artifact mechanism from nightly NPU workflows (#35489)
  _Files: `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu-e2e-multi-node.yml`, `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/run_npu_e2e_test.py`_
- **2026-09-05** [`09f542b23a`](https://github.com/sgl-project/sglang/commit/09f542b23a) [#37618](https://github.com/sgl-project/sglang/pull/37618)
  [CI] Add /rerun-test --changed to rerun every test file a PR modifies (#37618)
  _Files: `docs/docs/developer_guide/contribution_guide.mdx`, `scripts/ci/utils/slash_command_handler.py`, `test/registered/unit/tools/test_slash_command_handler.py`_
- **2026-09-04** [`55509b3f42`](https://github.com/sgl-project/sglang/commit/55509b3f42) [#38015](https://github.com/sgl-project/sglang/pull/38015)
  [NPU] Optimize the execution logic of NPU pr‑test tasks (#38015)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-09-04** [`ca7b8efd87`](https://github.com/sgl-project/sglang/commit/ca7b8efd87) [#37930](https://github.com/sgl-project/sglang/pull/37930)
  [CI] Fix handle_platform_cp_compatibility reading legacy CP flags off the record (#37930)
  _Files: `python/sglang/srt/arg_groups/parallel_hook.py`_
- **2026-09-04** [`a5f07b1241`](https://github.com/sgl-project/sglang/commit/a5f07b1241) [#37820](https://github.com/sgl-project/sglang/pull/37820)
  [CI] Build the Rust extensions for aarch64 too (#37820)
  _Files: `.github/workflows/_pr-test-rust-ext-build.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test.yml` _+2 more__
- **2026-09-04** [`8770c1db1f`](https://github.com/sgl-project/sglang/commit/8770c1db1f) [#37395](https://github.com/sgl-project/sglang/pull/37395)
  [CPU][CI]: rename Xeon CPU CI suites to stage-*-intel (#37395)
- **2026-09-03** [`81b0e4985a`](https://github.com/sgl-project/sglang/commit/81b0e4985a) [#37572](https://github.com/sgl-project/sglang/pull/37572)
  Modify KUBE_JOB_NAME to fix the problem of the string being too long (#37572)
  _Files: `.github/workflows/nightly-test-npu-e2e-multi-node.yml`_
- **2026-09-03** [`28262c20df`](https://github.com/sgl-project/sglang/commit/28262c20df) [#37210](https://github.com/sgl-project/sglang/pull/37210)
  [CI][RFC] Replace black-jupyter with ruff-format (#37210)
- **2026-09-02** [`a6da3a4922`](https://github.com/sgl-project/sglang/commit/a6da3a4922) [#37522](https://github.com/sgl-project/sglang/pull/37522)
  [CI] Re-enable GB300 jobs (#37522)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/release-whl-deepgemm.yml`, `.github/workflows/rerun-test.yml`_
- **2026-09-02** [`403a15c163`](https://github.com/sgl-project/sglang/commit/403a15c163) [#37252](https://github.com/sgl-project/sglang/pull/37252)
  [CI] Batch CPU test workers (#37252)
  _Files: `.github/workflows/_pr-test-stage-cpu.yml`, `python/sglang/test/ci/fork_test_worker.py`, `test/registered/unit/test_fork_test_worker.py`_
- **2026-09-02** [`e874ae64cd`](https://github.com/sgl-project/sglang/commit/e874ae64cd) [#37230](https://github.com/sgl-project/sglang/pull/37230)
  [XPU][CI] Enable nightly-xpu-8-gpu suite: declare + wire runner job (#37230)
  _Files: `.github/workflows/nightly-test-intel.yml`, `test/run_suite.py`_
- **2026-09-02** [`db017e3490`](https://github.com/sgl-project/sglang/commit/db017e3490) [#37258](https://github.com/sgl-project/sglang/pull/37258)
  Build Rust extensions on hosted runners in parallel (#37258)
  _Files: `.github/workflows/_pr-test-rust-ext-build.yml`, `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/seed-rust-ext-cache.yml`_
- **2026-09-02** [`73a2414289`](https://github.com/sgl-project/sglang/commit/73a2414289) [#37452](https://github.com/sgl-project/sglang/pull/37452)
  [CI] Double the base-b-test-1-gpu-large timeout (#37452)
  _Files: `.github/workflows/pr-test.yml`_
- **2026-09-01** [`60f881b40c`](https://github.com/sgl-project/sglang/commit/60f881b40c) [#35500](https://github.com/sgl-project/sglang/pull/35500)
  [CI/NPU] Isolate multi-node tests by run_id to prevent concurrent-run… (#35500)
  _Files: `.github/workflows/nightly-test-npu-e2e-multi-node.yml`, `python/sglang/test/ascend/e2e/k8s_multi_pd_mix.yaml.jinja2`, `python/sglang/test/ascend/e2e/k8s_multi_pd_mix_green.yaml.jinja2`, `python/sglang/test/ascend/e2e/k8s_multi_pd_separation.yaml.jinja2` _+4 more__
- **2026-09-01** [`783af667fb`](https://github.com/sgl-project/sglang/commit/783af667fb) [#36699](https://github.com/sgl-project/sglang/pull/36699)
  xpu: record per-model metrics to jsonl for nightly dashboard (#36699)
  _Files: `.github/workflows/nightly-test-intel.yml`, `.github/workflows/xpu-ci-job-monitor.yml`, `python/sglang/srt/environ.py`, `python/sglang/test/ci/ci_utils.py` _+2 more__
- **2026-08-31** [`5e679b0cad`](https://github.com/sgl-project/sglang/commit/5e679b0cad) [#37203](https://github.com/sgl-project/sglang/pull/37203)
  [CI] Speed up lint: cache pre-commit envs + mint, drop redundant work (#37203)
  _Files: `.github/workflows/lint.yml`_
- **2026-08-31** [`10b67aa7a1`](https://github.com/sgl-project/sglang/commit/10b67aa7a1) [#36814](https://github.com/sgl-project/sglang/pull/36814)
  xpu: move prefill-only model tests to the nightly-xpu-1-gpu grid (#36814)
  _Files: `test/registered/xpu/test_xpu_classification.py`, `test/registered/xpu/test_xpu_embedding.py`, `test/registered/xpu/test_xpu_rerank.py`, `test/registered/xpu/test_xpu_reward.py`_

## ROCm / AMD  (15 commits)

- **2026-09-07** [`503511c963`](https://github.com/sgl-project/sglang/commit/503511c963) [#38256](https://github.com/sgl-project/sglang/pull/38256)
  [AMD] Cherry-pick aiter commit for dsv4 a8w8 bpreshuffle gemm config (#38256)
  _Files: `docker/rocm.Dockerfile`_
- **2026-09-07** [`b9b39f222d`](https://github.com/sgl-project/sglang/commit/b9b39f222d) [#37784](https://github.com/sgl-project/sglang/pull/37784)
  [AMD] Update ROCm AITER pin to 4ad9983 (#37784)
  _Files: `docker/rocm.Dockerfile`_
- **2026-09-06** [`2c05ed4e77`](https://github.com/sgl-project/sglang/commit/2c05ed4e77) [#37720](https://github.com/sgl-project/sglang/pull/37720)
  [ROCm] Stage large pageable H2D copies instead of pinning them in place (#37720)
  _Files: `python/sglang/srt/arg_groups/platform_hook.py`, `test/registered/unit/test_rocm_pageable_h2d_staging.py`_
- **2026-09-04** [`7f89cc5286`](https://github.com/sgl-project/sglang/commit/7f89cc5286) [#37580](https://github.com/sgl-project/sglang/pull/37580)
  [AMD] Skip unused TOPK v2 plan kernel on ROCm (#37580)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`_
- **2026-09-04** [`cb32dbc9e0`](https://github.com/sgl-project/sglang/commit/cb32dbc9e0) [#35176](https://github.com/sgl-project/sglang/pull/35176)
  [AMD] [Kimi-K3] Fuse the KDA input projection into a single GEMM on ROCm (#35176)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/amd/test_kimi_k3_kda_inproj_fusion.py`_
- **2026-09-04** [`225129fe44`](https://github.com/sgl-project/sglang/commit/225129fe44) [#37829](https://github.com/sgl-project/sglang/pull/37829)
  [AMD] Update v4 amd cookbook 0903 (#37829)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-03** [`dd091f43cd`](https://github.com/sgl-project/sglang/commit/dd091f43cd) [#37781](https://github.com/sgl-project/sglang/pull/37781)
  [AMD] Update kimi-k3 amd cookbook 0903 (#37781)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-09-03** [`f59a4840c5`](https://github.com/sgl-project/sglang/commit/f59a4840c5) [#37779](https://github.com/sgl-project/sglang/pull/37779)
  [AMD][CI] Correct MI355X Slurm exclude node (#37779)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-09-02** [`2d799c28f4`](https://github.com/sgl-project/sglang/commit/2d799c28f4) [#37647](https://github.com/sgl-project/sglang/pull/37647)
  [CI] Authenticate and retry git clones in install scripts (#37647)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`, `scripts/ci/cuda/ci_install_dependency.sh`, `scripts/ci/utils/git_clone_with_retry.sh`_
- **2026-09-02** [`99b9109553`](https://github.com/sgl-project/sglang/commit/99b9109553) [#37586](https://github.com/sgl-project/sglang/pull/37586)
  [AMD] Run ROCm 7.0 shadow tests every two days- #37582 (#37586)
  _Files: `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd.yml`_
- **2026-09-02** [`0157f1f552`](https://github.com/sgl-project/sglang/commit/0157f1f552) [#37518](https://github.com/sgl-project/sglang/pull/37518)
  [AMD][CI] Exclude unavailable MI355X nodes and skip 4N nightly (#37518)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-09-01** [`3103bc7462`](https://github.com/sgl-project/sglang/commit/3103bc7462) [#37409](https://github.com/sgl-project/sglang/pull/37409)
  [AMD][CI] Add daily ROCm 10 and ROCm 7.2 test coverage (#37409)
  _Files: `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd-extra.yml`, `.github/workflows/pr-test-amd-rocm720.yml`_
- **2026-09-01** [`ed122ea984`](https://github.com/sgl-project/sglang/commit/ed122ea984) [#36851](https://github.com/sgl-project/sglang/pull/36851)
  [AMD] Enable topk v2 GLM ROCm (#36851)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`_
- **2026-09-01** [`458987b5ac`](https://github.com/sgl-project/sglang/commit/458987b5ac) [#509](https://github.com/sgl-project/sglang/pull/509)
  [AMD][MORI] Bump MoRI to 7c51d18 for ionic RoCE dmabuf fix (#509) (#37286)
  _Files: `docker/rocm.Dockerfile`_
- **2026-08-31** [`5972211977`](https://github.com/sgl-project/sglang/commit/5972211977) [#37132](https://github.com/sgl-project/sglang/pull/37132)
  [AMD] Fix the QuickReduce bf16 cast failing to build for CDNA (#37132)
  _Files: `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce.cuh`, `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce_base.h`_

## Tensor / Data Parallel  (11 commits)

- **2026-09-07** [`755f97c622`](https://github.com/sgl-project/sglang/commit/755f97c622) [#38314](https://github.com/sgl-project/sglang/pull/38314)
  [CI] Fix the DSpark dp-tier unit test fixture after #34919 (#38314)
  _Files: `test/registered/spec/dspark/test_dspark_dp_tier.py`_
- **2026-09-07** [`98f69ccbf3`](https://github.com/sgl-project/sglang/commit/98f69ccbf3) [#38048](https://github.com/sgl-project/sglang/pull/38048)
  [Config] Round 6.3: the record remembers how it was asked for, and is sealed while resolution runs (#38048)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/grpc_bridge.py`, `python/sglang/srt/entrypoints/http_server.py` _+2 more__
- **2026-09-07** [`1c992bbd94`](https://github.com/sgl-project/sglang/commit/1c992bbd94) [#37179](https://github.com/sgl-project/sglang/pull/37179)
  [CPU] Fix shm allreduce collision and sglang-router import (#37179)
  _Files: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/utils/__init__.py`, `python/sglang/srt/utils/numa_utils.py`_
- **2026-09-06** [`6cee9285a3`](https://github.com/sgl-project/sglang/commit/6cee9285a3) [#37591](https://github.com/sgl-project/sglang/pull/37591)
  [ROCm] Make DSA indexer top-k exact with cooperative selection (#37591)
  _Files: `3rdparty/amd/wheel/sgl-kernel/rocm_hipify.py`, `python/sglang/kernels/aot/csrc/elementwise/topk.hip`, `python/sglang/kernels/aot/include/hip/dsa_topk_coop.cuh`, `python/sglang/kernels/aot/setup_rocm.py` _+1 more__
- **2026-09-05** [`613d87becd`](https://github.com/sgl-project/sglang/commit/613d87becd) [#38038](https://github.com/sgl-project/sglang/pull/38038)
  [Memory] Reuse output storage across full prefill CUDA graphs (#38038)
  _Files: `python/sglang/srt/model_executor/runner_backend/full_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_backend/utils.py`, `test/registered/unit/model_executor/runner_backend/test_full_cuda_graph_backend.py`_
- **2026-09-05** [`65f7957142`](https://github.com/sgl-project/sglang/commit/65f7957142) [#38078](https://github.com/sgl-project/sglang/pull/38078)
  fix: gather CP-sharded tokens before TP-sharded dense MLP under prefill CP (#38078)
  _Files: `python/sglang/srt/layers/communicator.py`, `test/registered/unit/layers/test_layer_communicator_fusion_gate.py`, `test/registered/unit/layers/test_layer_scatter_modes_cp_dense_mlp.py`_
- **2026-09-04** [`2216697f90`](https://github.com/sgl-project/sglang/commit/2216697f90) [#37750](https://github.com/sgl-project/sglang/pull/37750)
  [Docs] Refresh TPU model list and link cookbooks (#37750)
  _Files: `docs/docs/hardware-platforms/tpu.mdx`_
- **2026-09-02** [`982aa8acfc`](https://github.com/sgl-project/sglang/commit/982aa8acfc) [#37471](https://github.com/sgl-project/sglang/pull/37471)
  [Bugfix] Load Qwen3.5 MTP embedding under PP (#37471)
  _Files: `python/sglang/srt/models/qwen3_5_mtp.py`, `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`_
- **2026-09-02** [`2d9c64394f`](https://github.com/sgl-project/sglang/commit/2d9c64394f) [#35443](https://github.com/sgl-project/sglang/pull/35443)
  Fix reasoning metrics and add TPOT to bench_multiturn (#35443)
  _Files: `benchmark/hicache/bench_multiturn.py`, `python/sglang/benchmark/serving.py`, `python/sglang/test/kits/cache_hit_kit.py`, `test/registered/unit/test_cache_hit_kit_metrics.py`_
- **2026-09-01** [`562b661e0e`](https://github.com/sgl-project/sglang/commit/562b661e0e) [#30915](https://github.com/sgl-project/sglang/pull/30915)
  [Feature] Megatron LayerNorm sequence parallelism (--enable-layernorm-sp) (#30915)
  _Files: `python/sglang/srt/arg_groups/layernorm_sp_hook.py`, `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/layers/communicator.py` _+7 more__
- **2026-08-31** [`cf51650335`](https://github.com/sgl-project/sglang/commit/cf51650335) [#37195](https://github.com/sgl-project/sglang/pull/37195)
  fix(config): retain pre-engine resolution declarations (#37195)
  _Files: `python/sglang/srt/arg_groups/pipeline.py`, `test/registered/unit/server_args/test_resolution_declarations.py`_

## Scheduler / Batching  (10 commits)

- **2026-09-07** [`a88e852fab`](https://github.com/sgl-project/sglang/commit/a88e852fab) [#38279](https://github.com/sgl-project/sglang/pull/38279)
  [Sampling] Allow sampling-mask replay with DisallowedTokensLogitsProcessor (#38279)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/sampling/custom_logit_processor.py`, `test/registered/sampling/test_sampling_mask.py`, `test/registered/unit/managers/test_sampling_mask_validation.py`_
- **2026-09-06** [`ae54ccb25d`](https://github.com/sgl-project/sglang/commit/ae54ccb25d) [#38139](https://github.com/sgl-project/sglang/pull/38139)
  [Router] Publish cache-aware load state (#38139)
  _Files: `python/sglang/srt/managers/scheduler_components/load_publisher.py`, `test/registered/unit/managers/test_loadstat_wire.py`_
- **2026-09-04** [`8a98f11078`](https://github.com/sgl-project/sglang/commit/8a98f11078) [#34488](https://github.com/sgl-project/sglang/pull/34488)
  [feature] Add response-level input/output token ids to chat completions via SglExt (#34488)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/server_args.py` _+2 more__
- **2026-09-04** [`e3eeabbbfa`](https://github.com/sgl-project/sglang/commit/e3eeabbbfa) [#38067](https://github.com/sgl-project/sglang/pull/38067)
  [Profiler] Add SGLANG_PROFILE_BY_STAGE_DECODE_MIN_BS to defer the decode-stage capture (#38067)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler_components/profiler_manager.py`_
- **2026-09-04** [`0eff0f7460`](https://github.com/sgl-project/sglang/commit/0eff0f7460) [#38065](https://github.com/sgl-project/sglang/pull/38065)
  Add num_prealloc_ready_tokens to decode load snapshot (#38065)
  _Files: `python/sglang/srt/managers/load_snapshot.py`, `python/sglang/srt/managers/scheduler_components/load_inquirer.py`_
- **2026-09-04** [`fbf8f1dbf6`](https://github.com/sgl-project/sglang/commit/fbf8f1dbf6) [#37888](https://github.com/sgl-project/sglang/pull/37888)
  [Fix] Coordinate FullCG prefix variants across DP ranks (#37888)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/model_executor/forward_batch_info.py` _+2 more__
- **2026-09-03** [`66d60433c1`](https://github.com/sgl-project/sglang/commit/66d60433c1) [#37285](https://github.com/sgl-project/sglang/pull/37285)
  state_capturer: pin the exact host-cache size via mmap + cudaHostRegister (#37285)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/state_capturer/base.py`, `python/sglang/srt/state_capturer/indexer_topk.py`, `python/sglang/srt/state_capturer/routed_experts.py`_
- **2026-09-02** [`f8f04bafa8`](https://github.com/sgl-project/sglang/commit/f8f04bafa8) [#37327](https://github.com/sgl-project/sglang/pull/37327)
  Rust server: align launcher and request validation behavior (#37327)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/rust_server/server.py`, `rust/sglang-server/src/api_server/native_api.rs` _+9 more__
- **2026-09-02** [`b83bf7a65f`](https://github.com/sgl-project/sglang/commit/b83bf7a65f) [#37297](https://github.com/sgl-project/sglang/pull/37297)
  [Bugfix] Avoid scanning crash-dump token buffers during GC (#37297)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-08-31** [`2138494272`](https://github.com/sgl-project/sglang/commit/2138494272) [#37222](https://github.com/sgl-project/sglang/pull/37222)
  [Rust] Keep sampling and scheduler wire schemas in sync (#37222)
  _Files: `rust/sglang-server/src/message/sampling.rs`, `test/registered/unit/managers/test_io_struct.py`, `test/registered/unit/sampling/test_sampling_params.py`_

## Docs / Examples  (9 commits)

- **2026-09-07** [`e4008de757`](https://github.com/sgl-project/sglang/commit/e4008de757) [#38295](https://github.com/sgl-project/sglang/pull/38295)
  Add MiniCPM5-2B cookbook (#38295)
  _Files: `docs/cookbook/autoregressive/OpenBMB/MiniCPM-V-4_6.mdx`, `docs/cookbook/autoregressive/OpenBMB/MiniCPM5-2B.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-09-05** [`3b64169f9d`](https://github.com/sgl-project/sglang/commit/3b64169f9d) [#37878](https://github.com/sgl-project/sglang/pull/37878)
  [Cookbook] Kimi-K3: add measured B300 1x8 Unified 8k/1k speed numbers (#37878)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3-benchmarks.jsx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-09-04** [`320bdd1ee2`](https://github.com/sgl-project/sglang/commit/320bdd1ee2) [#37989](https://github.com/sgl-project/sglang/pull/37989)
  [Docs] Document --retraction-policy, --return-hidden-states-mode, --language-model-only (#37989)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`_
- **2026-09-04** [`b168f905c8`](https://github.com/sgl-project/sglang/commit/b168f905c8) [#31031](https://github.com/sgl-project/sglang/pull/31031)
  [Intel GPU] Align XPU toml file for rust support (#31031)
  _Files: `docs/docs/hardware-platforms/xpu.mdx`, `python/pyproject_xpu.toml`_
- **2026-09-03** [`3ffacf949b`](https://github.com/sgl-project/sglang/commit/3ffacf949b) [#37788](https://github.com/sgl-project/sglang/pull/37788)
  [Docs] [BugFix] Sync --tool-call-parser and --reasoning-parser lists with the code (#37788)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`_
- **2026-09-03** [`354ed6d66b`](https://github.com/sgl-project/sglang/commit/354ed6d66b) [#37799](https://github.com/sgl-project/sglang/pull/37799)
  [NPU] [DOC] Refresh supported models and features on NPU (#37799)
  _Files: `docs/docs/hardware-platforms/ascend-npus/development/operator_performance_optimizing.mdx`, `docs/docs/hardware-platforms/ascend-npus/optimization/profiling.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_models.mdx`_
- **2026-09-03** [`98ef7d8ae6`](https://github.com/sgl-project/sglang/commit/98ef7d8ae6) [#37655](https://github.com/sgl-project/sglang/pull/37655)
  docs: add K2 Horizon cookbook recipes and H200 results (#37655)
  _Files: `docs/cards/logos/ifm.png`, `docs/cookbook/autoregressive/IFM/K2-Horizon.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-09-03** [`f15748d965`](https://github.com/sgl-project/sglang/commit/f15748d965) [#37469](https://github.com/sgl-project/sglang/pull/37469)
  [bench] Support real-traffic replay with early-stop-aware steady-state metrics in bench_one_batch_server (#37469)
  _Files: `docs/docs/developer_guide/benchmark_and_profiling.mdx`, `python/sglang/benchmark/one_batch_server.py`, `python/sglang/benchmark/stream_metrics.py`_
- **2026-09-02** [`9c70d22721`](https://github.com/sgl-project/sglang/commit/9c70d22721) [#35368](https://github.com/sgl-project/sglang/pull/35368)
  Update GLM-5.2 NVFP4 B200/B300 for AgentX HiCache (#35368)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`_

## Models  (9 commits)

- **2026-09-07** [`cfa989b7af`](https://github.com/sgl-project/sglang/commit/cfa989b7af) [#38280](https://github.com/sgl-project/sglang/pull/38280)
  [CI] Fix stale CP-v1 mock patches in NextN mm-embed test (#38280)
  _Files: `test/registered/unit/models/test_deepseek_nextn_mm_embed.py`_
- **2026-09-07** [`45c24444b1`](https://github.com/sgl-project/sglang/commit/45c24444b1) [#38046](https://github.com/sgl-project/sglang/pull/38046)
  [Config] Round 6.1: "unset" gets its own spelling, and the declaration says what it means (#38046)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/arg_groups/model_overrides/deepseek_v4.py`, `python/sglang/srt/arg_groups/model_overrides/inkling.py` _+4 more__
- **2026-09-07** [`0afba909e7`](https://github.com/sgl-project/sglang/commit/0afba909e7) [#37800](https://github.com/sgl-project/sglang/pull/37800)
  [XPU][CI] Fix empty nightly dashboard (#37800)
  _Files: `.github/workflows/nightly-test-intel.yml`, `.github/workflows/xpu-ci-job-monitor.yml`, `python/sglang/test/ci/ci_utils.py`, `test/registered/xpu/test_deepseek_ocr_2_olmbench.py`_
- **2026-09-07** [`e0a83a2215`](https://github.com/sgl-project/sglang/commit/e0a83a2215) [#38221](https://github.com/sgl-project/sglang/pull/38221)
  test(xpu): pin --mem-fraction-static=0.7 for DeepSeek-OCR test (#38221)
  _Files: `test/registered/xpu/test_deepseek_ocr.py`_
- **2026-09-05** [`32a1d55431`](https://github.com/sgl-project/sglang/commit/32a1d55431) [#37378](https://github.com/sgl-project/sglang/pull/37378)
  fix(modelopt_fp4): skip NVFP4 swiglu-fusion interleave for shared experts with swiglu_limit (#37378)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-09-05** [`991368d880`](https://github.com/sgl-project/sglang/commit/991368d880) [#37510](https://github.com/sgl-project/sglang/pull/37510)
  Fix Muse Glimmer ModelOpt mixed weight mapping (#37510)
  _Files: `python/sglang/srt/models/muse_glimmer.py`, `test/registered/unit/model_loader/test_modelopt_loader.py`_
- **2026-09-04** [`c8ba8996c4`](https://github.com/sgl-project/sglang/commit/c8ba8996c4) [#38026](https://github.com/sgl-project/sglang/pull/38026)
  Update DeepSeek-V4 Pro for B200 FP4 agentic HiCache DSpark (#38026)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`_
- **2026-08-31** [`63b2adbeac`](https://github.com/sgl-project/sglang/commit/63b2adbeac) [#36459](https://github.com/sgl-project/sglang/pull/36459)
  [NPU] Fix evalscope accuracy parsing and add glm5_1 aime26 request timeout (#36459)
  _Files: `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`, `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py`, `test/registered/npu/accuracy/qwen3_next_80b_a3b_instruct/test_npu_qwen3_next_80b_w8a8_2p_in6k_out1k5_bs16_aime25.py`, `test/registered/npu/performance/kimi_k2_6/test_npu_kimi_k2_6_w4a8_16p_in64k_out1k_100ms.py`_
- **2026-08-31** [`4dc7dc8518`](https://github.com/sgl-project/sglang/commit/4dc7dc8518) [#35244](https://github.com/sgl-project/sglang/pull/35244)
  [Fix] Transformers-fallback (GPT-NeoX) + KV pool config (DeepSeek-VL2) (#35244)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/transformers.py`, `test/registered/unit/configs/test_model_config_shapes.py`, `test/registered/unit/model_loader/test_transformers_fallback.py`_

## Speculative Decoding  (4 commits)

- **2026-09-03** [`87d60a2229`](https://github.com/sgl-project/sglang/commit/87d60a2229) [#37329](https://github.com/sgl-project/sglang/pull/37329)
  Improve CUDA graph and speculative execution output handling (#37329)
  _Files: `python/sglang/srt/layers/aux_hidden_states.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/models/dspark.py` _+4 more__
- **2026-09-02** [`3fa6b86504`](https://github.com/sgl-project/sglang/commit/3fa6b86504) [#36752](https://github.com/sgl-project/sglang/pull/36752)
  [Spec] Publish the final multi-layer EAGLE shared-read event (#36752)
  _Files: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`, `test/registered/unit/spec/test_multi_layer_eagle_shared_read_event.py`_
- **2026-09-02** [`83bd2c473f`](https://github.com/sgl-project/sglang/commit/83bd2c473f) [#37274](https://github.com/sgl-project/sglang/pull/37274)
  Allow custom policy for adaptive speculative decoding (#37274)
  _Files: `python/sglang/srt/speculative/adaptive_runtime_state.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/unit/spec/test_adaptive_runtime_state.py`_
- **2026-08-31** [`3ed3326631`](https://github.com/sgl-project/sglang/commit/3ed3326631) [#36897](https://github.com/sgl-project/sglang/pull/36897)
  Decouple speculative draft capacity from runtime state (#36897)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/speculative/spec_info.py`, `python/sglang/srt/speculative/spec_registry.py` _+2 more__

## LoRA  (2 commits)

- **2026-09-07** [`ed82def55f`](https://github.com/sgl-project/sglang/commit/ed82def55f) [#38047](https://github.com/sgl-project/sglang/pull/38047)
  [Config] Round 6.2: the field declarations move to their namespaces, and the record is assembled from them (#38047)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/choices.py`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/__init__.py` _+14 more__
- **2026-09-04** [`516cfbd362`](https://github.com/sgl-project/sglang/commit/516cfbd362) [#37872](https://github.com/sgl-project/sglang/pull/37872)
  Fix UNO test adapter subdirectory resolution (#37872)
  _Files: `test/registered/spec/uno/test_uno.py`_

## Structured Output  (2 commits)

- **2026-09-05** [`77aee20259`](https://github.com/sgl-project/sglang/commit/77aee20259) [#32151](https://github.com/sgl-project/sglang/pull/32151)
  [Model] Add support for Nanbeige4.2 (#32151)
  _Files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/nanbeige.py`, `python/sglang/srt/function_call/function_call_parser.py` _+5 more__
- **2026-09-03** [`8b0501399e`](https://github.com/sgl-project/sglang/commit/8b0501399e) [#37884](https://github.com/sgl-project/sglang/pull/37884)
  [CI] Improve Lark CI cards: structured layout, PDT timestamps, slow-only queue digest (#37884)
  _Files: `.github/workflows/ci-lark-notify.yml`, `scripts/ci_monitor/README.md`, `scripts/ci_monitor/lark_notify.py`_

## Serving / API  (2 commits)

- **2026-09-04** [`3e873c2110`](https://github.com/sgl-project/sglang/commit/3e873c2110) [#32172](https://github.com/sgl-project/sglang/pull/32172)
  [Docs] Clarify OpenAI chat template defaults (#32172)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/basic_usage/openai_api_completions.mdx`_
- **2026-08-31** [`6580d5cd9a`](https://github.com/sgl-project/sglang/commit/6580d5cd9a) [#36101](https://github.com/sgl-project/sglang/pull/36101)
  weight cache: key daemon paths by GPU UUID (#36101)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py` _+7 more__

---
_Generated 2026-09-07 14:11 UTC_