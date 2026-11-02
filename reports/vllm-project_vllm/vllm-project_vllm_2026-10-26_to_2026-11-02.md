# vllm-project/vllm — Weekly Change Report
**Period:** 2026-10-26 → 2026-11-02  |  **Total commits:** 590

## ✨ New Features This Week

- **2026-11-02** [#64589](https://github.com/vllm-project/vllm/pull/64589) — [Docs] Add DeepSeek-V4.1-Flash MI325X AgentX preset (#64589)
- **2026-11-02** [#65005](https://github.com/vllm-project/vllm/pull/65005) — [Docs][Model] Add Parakeet TDT transcription support via plugin (#65005)
- **2026-11-02** [#64179](https://github.com/vllm-project/vllm/pull/64179) — [Model] Enable --mm-encoder-tp-mode data for MiMo-V2.6 (#64179)
- **2026-11-01** [#64607](https://github.com/vllm-project/vllm/pull/64607) — [Recipe] Qwen3.5-397B-A17B: add the B200 NVFP4 TP2 agentic preset (#64607)
- **2026-10-31** [#64805](https://github.com/vllm-project/vllm/pull/64805) — [Docs][ROCm] Add MiniMax-M3.1-Flash MI355X TP4 AgentX preset (#64805)
- **2026-10-31** [#64804](https://github.com/vllm-project/vllm/pull/64804) — [Docs][ROCm] Add DeepSeek-V4.1-Flash MI355X TP8 concurrency-1 AgentX preset (#64804)
- **2026-10-31** [#62956](https://github.com/vllm-project/vllm/pull/62956) — [Perf][glm5next] Add SM121 TP=2 skinny-GEMM plans for GLM-5.3-Flash (#62956)
- **2026-10-31** [#61361](https://github.com/vllm-project/vllm/pull/61361) — [MORI] Add MORI EP V2 support (#61361)
- **2026-10-31** [#64650](https://github.com/vllm-project/vllm/pull/64650) — [Perf][Qwen3.8] Add SM103 skinny GEMM plans for TP=1 (#64650)
- **2026-10-31** [#64215](https://github.com/vllm-project/vllm/pull/64215) — [Model] Add NVIDIA Canary (nvidia/canary-1b-v2) speech-to-text support (#64215)
- _…and 85 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-11-02** [`84e59a3b74`](https://github.com/vllm-project/vllm/commit/84e59a3b74) [#62716](https://github.com/vllm-project/vllm/pull/62716) — [ROCm][Build][1/5] Speed up ROCm build: generate the paged attention instantiations from one variant list (#62716)
- **2026-11-02** [`542bc671b7`](https://github.com/vllm-project/vllm/commit/542bc671b7) [#64589](https://github.com/vllm-project/vllm/pull/64589) — [Docs] Add DeepSeek-V4.1-Flash MI325X AgentX preset (#64589)
- **2026-11-02** [`887eef12e1`](https://github.com/vllm-project/vllm/commit/887eef12e1) [#60102](https://github.com/vllm-project/vllm/pull/60102) — [ROCm][DSv4.1][Perf] Route gfx942 sparse MLA prefill to AITER pa_prefill_sparse (#60102)
- **2026-11-02** [`eff37e8e24`](https://github.com/vllm-project/vllm/commit/eff37e8e24) [#64448](https://github.com/vllm-project/vllm/pull/64448) — [ROCm][MiniMax-M3.1] NVFP4 indexer: decode CP for DSpark 7 (#64448)
- **2026-11-02** [`4890c7ff35`](https://github.com/vllm-project/vllm/commit/4890c7ff35) [#65184](https://github.com/vllm-project/vllm/pull/65184) — [ROCm][CI] Gate MoRI EPv2 modular-kernel cases on the production EPv2 checks (#65184)
- **2026-11-02** [`a708b0f639`](https://github.com/vllm-project/vllm/commit/a708b0f639) [#64734](https://github.com/vllm-project/vllm/pull/64734) — [ROCm][CI] Raise the MI355 DeepSeek-V3.2 GSM8K startup wait to 1800s (#64734)
- **2026-11-02** [`f9db1756e9`](https://github.com/vllm-project/vllm/commit/f9db1756e9) [#57678](https://github.com/vllm-project/vllm/pull/57678) — [Model Loader] One post-load hook signature; the loader runs every module's hook (#57678)
- **2026-11-02** [`380c8e438c`](https://github.com/vllm-project/vllm/commit/380c8e438c) [#65157](https://github.com/vllm-project/vllm/pull/65157) — [Docs] Fix accidental cross-references in docstrings (#65157)
- **2026-11-02** [`a487973b6f`](https://github.com/vllm-project/vllm/commit/a487973b6f) [#65140](https://github.com/vllm-project/vllm/pull/65140) — [ROCm][CI] Fix Muse Spark RoPE cache leak between tests (#65140)
- **2026-11-02** [`5689c2790c`](https://github.com/vllm-project/vllm/commit/5689c2790c) [#65080](https://github.com/vllm-project/vllm/pull/65080) — [Bugfix][ROCm] Muse Spark: merge the two process_weights_after_loading hooks (#65080)
- **2026-11-02** [`51c6dfd8c8`](https://github.com/vllm-project/vllm/commit/51c6dfd8c8) [#64029](https://github.com/vllm-project/vllm/pull/64029) — [ROCm][Perf][Kimi-K3] Specialized decode K2: sentinel all-reduces, pre-AR loads, tagged x rows (#64029)
- **2026-11-02** [`0e5b2ba118`](https://github.com/vllm-project/vllm/commit/0e5b2ba118) [#64179](https://github.com/vllm-project/vllm/pull/64179) — [Model] Enable --mm-encoder-tp-mode data for MiMo-V2.6 (#64179)
- **2026-11-02** [`b2fcbdd164`](https://github.com/vllm-project/vllm/commit/b2fcbdd164) [#64355](https://github.com/vllm-project/vllm/pull/64355) — [CI] Enroll five steps and four AMD mirrors in automatic sharding (#64355)
- **2026-11-02** [`4c393ce427`](https://github.com/vllm-project/vllm/commit/4c393ce427) [#64181](https://github.com/vllm-project/vllm/pull/64181) — [CI] Enroll three standalone AMD steps in automatic sharding (#64181)
- **2026-11-02** [`be09292f09`](https://github.com/vllm-project/vllm/commit/be09292f09) [#63440](https://github.com/vllm-project/vllm/pull/63440) — [ROCm][Perf][Muse Spark] FlyDSL decode monokernel for DSpark verify steps on MI355X (--monokernel) (#63440)
- **2026-11-02** [`3d23773f10`](https://github.com/vllm-project/vllm/commit/3d23773f10) [#64614](https://github.com/vllm-project/vllm/pull/64614) — [Bugfix][ROCm] Use 64-bit row offsets in the RDNA hybrid W4A16 GEMM (#64614)
- **2026-11-02** [`cc69774820`](https://github.com/vllm-project/vllm/commit/cc69774820) [#63892](https://github.com/vllm-project/vllm/pull/63892) — [ROCm][Perf][DSv4.1] Mono: batch TP4 K2's X8 copies, load its push's peer bases late (#63892)
- **2026-11-02** [`de53c2deed`](https://github.com/vllm-project/vllm/commit/de53c2deed) [#61950](https://github.com/vllm-project/vllm/pull/61950) — [Bugfix][ROCm] Fix Kimi K3 online quantization with padded projections (#61950)
- **2026-11-01** [`63d3d39c84`](https://github.com/vllm-project/vllm/commit/63d3d39c84) [#59961](https://github.com/vllm-project/vllm/pull/59961) — [Bugfix][DSv3.2] Carry the shared indexer top-k across pipeline stages (#59961)
- **2026-10-31** [`564ac0de1b`](https://github.com/vllm-project/vllm/commit/564ac0de1b) [#64792](https://github.com/vllm-project/vllm/pull/64792) — [Docs][ROCm] Mistral Large 4 recipe: adds TP4 and lowest-latency presets  (#64792)
- **2026-10-31** [`b03e788812`](https://github.com/vllm-project/vllm/commit/b03e788812) [#64805](https://github.com/vllm-project/vllm/pull/64805) — [Docs][ROCm] Add MiniMax-M3.1-Flash MI355X TP4 AgentX preset (#64805)
- **2026-10-31** [`3f9d184738`](https://github.com/vllm-project/vllm/commit/3f9d184738) [#64804](https://github.com/vllm-project/vllm/pull/64804) — [Docs][ROCm] Add DeepSeek-V4.1-Flash MI355X TP8 concurrency-1 AgentX preset (#64804)
- **2026-10-31** [`25fc60723c`](https://github.com/vllm-project/vllm/commit/25fc60723c) [#60618](https://github.com/vllm-project/vllm/pull/60618) — [Perf][Kernel] Single-launch fused scoring+top-k kernel for sparse-indexer prefill, without materializing logits (#60618)
- **2026-10-31** [`50f622bdcf`](https://github.com/vllm-project/vllm/commit/50f622bdcf) [#63174](https://github.com/vllm-project/vllm/pull/63174) — Skip redundant weight tensor clones for loaders that yield owned tensors (#63174)
- **2026-10-31** [`7b77ed581d`](https://github.com/vllm-project/vllm/commit/7b77ed581d) [#64368](https://github.com/vllm-project/vllm/pull/64368) — [Spec Decode][ROCm] draft_lm_head_quantization for DSpark drafters (#64368)
- **2026-10-31** [`d5301a4f54`](https://github.com/vllm-project/vllm/commit/d5301a4f54) [#61361](https://github.com/vllm-project/vllm/pull/61361) — [MORI] Add MORI EP V2 support (#61361)
- **2026-10-31** [`c4f54cf5b3`](https://github.com/vllm-project/vllm/commit/c4f54cf5b3) [#63116](https://github.com/vllm-project/vllm/pull/63116) — [Bugfix][ROCm] Size AITER MLA persistent metadata for every decode query length (#63116)
- **2026-10-31** [`e3eec51570`](https://github.com/vllm-project/vllm/commit/e3eec51570) [#63297](https://github.com/vllm-project/vllm/pull/63297) — [ROCm][Kimi-K3] Keep KDA prefill checkpoints with the gluon backend (#63297)
- **2026-10-31** [`138dfa5463`](https://github.com/vllm-project/vllm/commit/138dfa5463) [#64094](https://github.com/vllm-project/vllm/pull/64094) — [ROCm][DSv4.1][Perf]  Enable prefix-cache SWA replay on gfx950 (#64094)
- **2026-10-31** [`58f245c69d`](https://github.com/vllm-project/vllm/commit/58f245c69d) [#64820](https://github.com/vllm-project/vllm/pull/64820) — [Kernel] Qwen4Exp: compute HyperConnection and PLE gate row offsets in int64 (#64820)
- **2026-10-31** [`17550580e9`](https://github.com/vllm-project/vllm/commit/17550580e9) [#61837](https://github.com/vllm-project/vllm/pull/61837) — [ROCm][Model] Step-5-Preview support on ROCm (#61837)
- **2026-10-30** [`59d58fd261`](https://github.com/vllm-project/vllm/commit/59d58fd261) [#64740](https://github.com/vllm-project/vllm/pull/64740) — [ROCm][CI] Run MI355 MoE Kernels on a full MI355 instead of DPX (#64740)
- **2026-10-30** [`d2d550c3fc`](https://github.com/vllm-project/vllm/commit/d2d550c3fc) [#64602](https://github.com/vllm-project/vllm/pull/64602) — [CI] Remove the retired A100 queue's steps; keep their live AMD mirrors standalone (#64602)
- **2026-10-30** [`14a5bb4adc`](https://github.com/vllm-project/vllm/commit/14a5bb4adc) [#64357](https://github.com/vllm-project/vllm/pull/64357) — [Model Loader] Run the model-level post-load hook once at the end of every load and reload (#64357)
- **2026-10-30** [`67d677bdef`](https://github.com/vllm-project/vllm/commit/67d677bdef) [#64577](https://github.com/vllm-project/vllm/pull/64577) — [ROCm][CI] Prebuild mamba-ssm and causal-conv1d into the CI test image (#64577)
- **2026-10-30** [`7495e9e5a4`](https://github.com/vllm-project/vllm/commit/7495e9e5a4) [#63774](https://github.com/vllm-project/vllm/pull/63774) — [ROCm] Bump AITER to v0.1.27 (#63774)
- **2026-10-30** [`644a9f5d27`](https://github.com/vllm-project/vllm/commit/644a9f5d27) [#64779](https://github.com/vllm-project/vllm/pull/64779) — [Deps] Upgrade to huggingface_hub 2 (#64779)
- **2026-10-30** [`42379a4c24`](https://github.com/vllm-project/vllm/commit/42379a4c24) [#63205](https://github.com/vllm-project/vllm/pull/63205) — [Model Runner V2][Spec Decode] Speculator config classes and custom speculators (#63205)
- **2026-10-30** [`e811e502ef`](https://github.com/vllm-project/vllm/commit/e811e502ef) [#64727](https://github.com/vllm-project/vllm/pull/64727) — [ROCm][CI] Fix AITER MXFP4 padding tests failing instead of skipping on MI300 (#64727)
- **2026-10-30** [`dc4dd5a221`](https://github.com/vllm-project/vllm/commit/dc4dd5a221) [#62007](https://github.com/vllm-project/vllm/pull/62007) — [ROCm][DI][CI]  Add DeepSeek-V3 NIXL accuracy steps (#62007)
- **2026-10-30** [`ca5c2d7843`](https://github.com/vllm-project/vllm/commit/ca5c2d7843) [#64708](https://github.com/vllm-project/vllm/pull/64708) — [ROCm][CI] Drop LD_PRELOAD from the subprocess env in test_amd_ci_fast_exit (#64708)
- **2026-10-30** [`8a2a5e4c40`](https://github.com/vllm-project/vllm/commit/8a2a5e4c40) [#64004](https://github.com/vllm-project/vllm/pull/64004) — [ROCm][Kimi-K3][Perf] Cut gfx942 MXFP4-to-int4 requant time under pure TP (#64004)
- **2026-10-30** [`617135eed3`](https://github.com/vllm-project/vllm/commit/617135eed3) [#61794](https://github.com/vllm-project/vllm/pull/61794) — [Test][UMBP][6/10] Add embedded runtime and MORI integration coverage (#61794)
- **2026-10-30** [`336d883f41`](https://github.com/vllm-project/vllm/commit/336d883f41) [#64569](https://github.com/vllm-project/vllm/pull/64569) — [CI] Enroll 6 steps and 10 AMD mirrors in automatic sharding (#64569)
- **2026-10-30** [`d492ee7862`](https://github.com/vllm-project/vllm/commit/d492ee7862) [#64110](https://github.com/vllm-project/vllm/pull/64110) — [Qwen4Exp] Remove FlashAttention dependency and standardize QSA naming (#64110)
- **2026-10-30** [`1353e1926f`](https://github.com/vllm-project/vllm/commit/1353e1926f) [#60867](https://github.com/vllm-project/vllm/pull/60867) — [KV Connector][ROCm] MoRIIO: hybrid READ for several attention groups and shared-group speculative methods (#60867)
- **2026-10-30** [`1fbde73aa1`](https://github.com/vllm-project/vllm/commit/1fbde73aa1) [#64529](https://github.com/vllm-project/vllm/pull/64529) — [CI] Bump Transformers version to 5.22.0 (#64529)
- **2026-10-30** [`8730884ab1`](https://github.com/vllm-project/vllm/commit/8730884ab1) [#64655](https://github.com/vllm-project/vllm/pull/64655) — [CI][ROCm] Check skinny-GEMM guard dispatch without torch.profiler (#64655)
- **2026-10-30** [`6d01893483`](https://github.com/vllm-project/vllm/commit/6d01893483) [#64567](https://github.com/vllm-project/vllm/pull/64567) — [ROCm][Bugfix] Skip AITER tuned GEMM when M*N >= 2^31 on gfx950 (#64567)
- **2026-10-30** [`2eae56c4ba`](https://github.com/vllm-project/vllm/commit/2eae56c4ba) [#64610](https://github.com/vllm-project/vllm/pull/64610) — [ROCm][CI] Update ROCm AITER nightly staging index (#64610)
- **2026-10-30** [`e49ea84e92`](https://github.com/vllm-project/vllm/commit/e49ea84e92) [#63885](https://github.com/vllm-project/vllm/pull/63885) — [ROCm][Perf][DSv4.1] Build the SWA decode metadata in one launch  (#63885)
- **2026-10-30** [`f81a414fae`](https://github.com/vllm-project/vllm/commit/f81a414fae) [#63054](https://github.com/vllm-project/vllm/pull/63054) — [Bugfix][ROCm] Use 64-bit row offsets in the Triton W4A16 GEMM (#63054)
- **2026-10-30** [`daccf69eb2`](https://github.com/vllm-project/vllm/commit/daccf69eb2) [#64619](https://github.com/vllm-project/vllm/pull/64619) — [CI][Kimi-K3] Add enable_adaptive_verification to the KDA checkpoint test stub (#64619)
- **2026-10-29** [`10579b71eb`](https://github.com/vllm-project/vllm/commit/10579b71eb) [#64544](https://github.com/vllm-project/vllm/pull/64544) — [Docs][ROCm] Mistral Large 4 recipe: ROCm image tag, MI355X, TP4 replica launch (#64544)
- **2026-10-29** [`434eadcbf8`](https://github.com/vllm-project/vllm/commit/434eadcbf8) [#64115](https://github.com/vllm-project/vllm/pull/64115) — [CI] Enroll two steps and two AMD mirrors in automatic sharding (#64115)
- **2026-10-29** [`f97a8d6647`](https://github.com/vllm-project/vllm/commit/f97a8d6647) [#64101](https://github.com/vllm-project/vllm/pull/64101) — [ROCm][Perf][DSv4.1] Mono decode at TP8 on MI355X (#64101)
- **2026-10-29** [`2abde627d9`](https://github.com/vllm-project/vllm/commit/2abde627d9) [#64378](https://github.com/vllm-project/vllm/pull/64378) — [ROCm][Quantization] NVFP4 MoE re-quantization and fused shared experts through online quantization (#64378)
- **2026-10-29** [`e18e2c70c5`](https://github.com/vllm-project/vllm/commit/e18e2c70c5) [#63816](https://github.com/vllm-project/vllm/pull/63816) — [Bugfix][ROCm][DSv4.1] Guard NaN scores in gfx942 mono routing (#63816)
- **2026-10-29** [`0124e16a6c`](https://github.com/vllm-project/vllm/commit/0124e16a6c) [#62481](https://github.com/vllm-project/vllm/pull/62481) — [ROCm] Monitor FlyDSL JIT compilation after warmup (#62481)
- **2026-10-29** [`bc57dc9d53`](https://github.com/vllm-project/vllm/commit/bc57dc9d53) [#63384](https://github.com/vllm-project/vllm/pull/63384) — [Transformers backend] Migrate OLMoE and fix MoE LoRA (#63384)
- **2026-10-29** [`bba4d9afec`](https://github.com/vllm-project/vllm/commit/bba4d9afec) [#61939](https://github.com/vllm-project/vllm/pull/61939) — [ROCm] Revamp CI/release deployment: collapse image tiers, unify build pipeline (#61939)
- **2026-10-29** [`6c71831f25`](https://github.com/vllm-project/vllm/commit/6c71831f25) [#62976](https://github.com/vllm-project/vllm/pull/62976) — [CI][ROCm][MoE] Add AITER_MOE_SORT_BACKEND MXFP4 DSV4 test coverage (#62976)
- **2026-10-29** [`e3f03f4f89`](https://github.com/vllm-project/vllm/commit/e3f03f4f89) [#62996](https://github.com/vllm-project/vllm/pull/62996) — [ROCm][Tests] Un-skip AITER MXFP4 padding-matrix and token-padding tests (#62996)
- **2026-10-29** [`d04560f56b`](https://github.com/vllm-project/vllm/commit/d04560f56b) [#64322](https://github.com/vllm-project/vllm/pull/64322) — [Doc] DeepSeek-V4-Pro: add MI355X AgentX source profiles (#64322)
- **2026-10-29** [`de83f55848`](https://github.com/vllm-project/vllm/commit/de83f55848) [#64532](https://github.com/vllm-project/vllm/pull/64532) — [ROCm][DSv4.1] Lift the skinny-GEMM cap in the gfx942 draft lm_head test (#64532)
- **2026-10-29** [`8d4c96804b`](https://github.com/vllm-project/vllm/commit/8d4c96804b) [#64049](https://github.com/vllm-project/vllm/pull/64049) — [CI] Bump Transformers version to 5.21.1 (#64049)
- **2026-10-29** [`f1266682b2`](https://github.com/vllm-project/vllm/commit/f1266682b2) [#64423](https://github.com/vllm-project/vllm/pull/64423) — [Bugfix][ROCm][DBO] Create hipBLASLt handles in microbatch threads before graph capture (#64423)
- **2026-10-29** [`e5571b97fc`](https://github.com/vllm-project/vllm/commit/e5571b97fc) [#64169](https://github.com/vllm-project/vllm/pull/64169) — [Mistral] Use get_grammar_for_chat_request in MistralParser and require mistral-common 1.13.0 (#64169)
- **2026-10-29** [`fb7def9ef9`](https://github.com/vllm-project/vllm/commit/fb7def9ef9) [#64008](https://github.com/vllm-project/vllm/pull/64008) — [ROCm][Perf] Reuse compiled FlyDSL host launchers (#64008)
- **2026-10-29** [`ee1056b317`](https://github.com/vllm-project/vllm/commit/ee1056b317) [#64474](https://github.com/vllm-project/vllm/pull/64474) — [Doc] Fix MiniMax-M3 docstring cross-references (#64474)
- **2026-10-29** [`a0e31b7353`](https://github.com/vllm-project/vllm/commit/a0e31b7353) [#63053](https://github.com/vllm-project/vllm/pull/63053) — [CI][ROCM][Bug] Elastic DP doesn't work with AITER-on (#63053)
- **2026-10-29** [`fa3b9d1377`](https://github.com/vllm-project/vllm/commit/fa3b9d1377) [#52838](https://github.com/vllm-project/vllm/pull/52838) — [Bugfix][AMD] A GPU-CPU KV transfer fault in OffloadingConnector takes the engine down instead of degrading the cache. (#52838)
- **2026-10-29** [`abaec97b42`](https://github.com/vllm-project/vllm/commit/abaec97b42) [#63179](https://github.com/vllm-project/vllm/pull/63179) — [ROCm] Fuse tiny-M MXFP8 quant into the block32 GEMM; guard lm_head skinny-GEMM by weight size (#63179)
- **2026-10-29** [`1aea05364f`](https://github.com/vllm-project/vllm/commit/1aea05364f) [#60477](https://github.com/vllm-project/vllm/pull/60477) — [Bugfix] DSA: all-reduce partial hidden_states before PP send (#60477)
- **2026-10-29** [`7ab756940a`](https://github.com/vllm-project/vllm/commit/7ab756940a) [#63047](https://github.com/vllm-project/vllm/pull/63047) — [Bugfix][DSv4.1] Budget prefill memory the startup profile misses (#63047)
- **2026-10-29** [`66875d3127`](https://github.com/vllm-project/vllm/commit/66875d3127) [#64356](https://github.com/vllm-project/vllm/pull/64356) — [Spec Decode] Batch-sharded draft logits refactor (#64356)
- **2026-10-29** [`bcbcd02e53`](https://github.com/vllm-project/vllm/commit/bcbcd02e53) [#63915](https://github.com/vllm-project/vllm/pull/63915) — [ROCm][Perf] Fuse MXFP8 activation quant into the 1x32 dot_scaled linear for M <= 16 (#63915)
- **2026-10-29** [`d6fbd94782`](https://github.com/vllm-project/vllm/commit/d6fbd94782) [#51012](https://github.com/vllm-project/vllm/pull/51012) — [Models] Deprecate `torch.compile` for Qwen3.5 models (#51012)
- **2026-10-29** [`a6c3635e36`](https://github.com/vllm-project/vllm/commit/a6c3635e36) [#64064](https://github.com/vllm-project/vllm/pull/64064) — [ROCm][Model] Enable ROCm AITER unified attention for MiMo-V2.6 (#64064)
- **2026-10-29** [`45fd60d4d5`](https://github.com/vllm-project/vllm/commit/45fd60d4d5) [#61529](https://github.com/vllm-project/vllm/pull/61529) — [ROCm][Qwen4Exp] Enable fp8 KV and indexer caches on the AMD QSA path (#61529)
- **2026-10-29** [`b7f0dda503`](https://github.com/vllm-project/vllm/commit/b7f0dda503) [#62990](https://github.com/vllm-project/vllm/pull/62990) — [ROCm][Kimi-K3] Allow DSpark adaptive verification with DCP on ROCM_AITER_MLA (#62990)
- **2026-10-28** [`ce775739e9`](https://github.com/vllm-project/vllm/commit/ce775739e9) [#64377](https://github.com/vllm-project/vllm/pull/64377) — [CI][ROCm] Drop nvidia-cuda-cccl from the ROCm test lockfile again (#64377)
- **2026-10-28** [`a3ce9ceefe`](https://github.com/vllm-project/vllm/commit/a3ce9ceefe) [#64010](https://github.com/vllm-project/vllm/pull/64010) — [CI] Re-enable disabled jobs whose installs are already locked (#64010)
- **2026-10-28** [`7b87062308`](https://github.com/vllm-project/vllm/commit/7b87062308) [#61699](https://github.com/vllm-project/vllm/pull/61699) — [Bugfix][Spec Decode] Honor standalone draft load config (#61699)
- **2026-10-28** [`892cb19816`](https://github.com/vllm-project/vllm/commit/892cb19816) [#63042](https://github.com/vllm-project/vllm/pull/63042) — [MyPy][8/N] Enable strict checking for model test subdirectories (#63042)
- **2026-10-28** [`8321d1119b`](https://github.com/vllm-project/vllm/commit/8321d1119b) [#64302](https://github.com/vllm-project/vllm/pull/64302) — [CI] Exclude nvidia-cuda-cccl from the ROCm test lockfile (#64302)
- **2026-10-28** [`af4db2a675`](https://github.com/vllm-project/vllm/commit/af4db2a675) [#61457](https://github.com/vllm-project/vllm/pull/61457) — [Quantization] Enable per-layer fused shared expert selection (#61457)
- **2026-10-28** [`6cfb375fd6`](https://github.com/vllm-project/vllm/commit/6cfb375fd6) [#61793](https://github.com/vllm-project/vllm/pull/61793) — [UMBP][5/10] Add MORI embedded DRAM runtime and transfer handling (#61793)
- **2026-10-28** [`df028dffa5`](https://github.com/vllm-project/vllm/commit/df028dffa5) [#64063](https://github.com/vllm-project/vllm/pull/64063) — Ship mamba SSU and Helion tuned kernel configs in wheel package_data (#64063)
- **2026-10-28** [`5ea8301982`](https://github.com/vllm-project/vllm/commit/5ea8301982) [#62077](https://github.com/vllm-project/vllm/pull/62077) — [CI] Move Attention, Quantization and MoE kernel tests and their AMD mirrors from fixed to automatic shards (#62077)
- **2026-10-28** [`1cb31be702`](https://github.com/vllm-project/vllm/commit/1cb31be702) [#63637](https://github.com/vllm-project/vllm/pull/63637) — [ROCm][MiniMax-M3.1] Fuse MXFP8 activation quant into the Gemma input_layernorm for qkv_proj (#63637)
- **2026-10-28** [`b71c1d5f14`](https://github.com/vllm-project/vllm/commit/b71c1d5f14) [#64158](https://github.com/vllm-project/vllm/pull/64158) — [ROCm][Bugfix][Kimi-K3] Build the folded q_b_proj / W_UK weight on the root model (#64158)
- **2026-10-28** [`11a3634094`](https://github.com/vllm-project/vllm/commit/11a3634094) [#62513](https://github.com/vllm-project/vllm/pull/62513) — [CI] Shard Humming B200/H100 evals and two entrypoints AMD mirrors automatically (#62513)
- **2026-10-27** [`bb7ea479c6`](https://github.com/vllm-project/vllm/commit/bb7ea479c6) [#63409](https://github.com/vllm-project/vllm/pull/63409) — [ROCm][Bugfix][Kimi-K3] Pass zero positions to the fused MLA decode q-prep kernel (#63409)
- **2026-10-27** [`274a5e19a1`](https://github.com/vllm-project/vllm/commit/274a5e19a1) [#63155](https://github.com/vllm-project/vllm/pull/63155) — [Perf][DSv4.1] Capture the decoder replay graphs on the model graphs' stream (#63155)
- **2026-10-27** [`9af236a332`](https://github.com/vllm-project/vllm/commit/9af236a332) [#63735](https://github.com/vllm-project/vllm/pull/63735) — [Bugfix][Perf][ROCm] RDNA launch config for kernel_paged_attention_2d (#63735)
- **2026-10-27** [`d0c20bb840`](https://github.com/vllm-project/vllm/commit/d0c20bb840) [#61863](https://github.com/vllm-project/vllm/pull/61863) — [ROCm][Perf][Attention] Keep the bf16 attention prefill when FP8 padding would double the heads (#61863)
- **2026-10-27** [`eaf1627c01`](https://github.com/vllm-project/vllm/commit/eaf1627c01) [#52970](https://github.com/vllm-project/vllm/pull/52970) — [ROCm][aiter] officially supporting aiter Triton kernels+dsv4 on RDNA3 (#52970)
- **2026-10-27** [`94ad4dfbae`](https://github.com/vllm-project/vllm/commit/94ad4dfbae) [#60710](https://github.com/vllm-project/vllm/pull/60710) — [ROCm][Perf] W4A16: opt-in dense weight cache for RDNA hybrid prefill (#60710)
- **2026-10-27** [`6aa70c4bec`](https://github.com/vllm-project/vllm/commit/6aa70c4bec) [#60110](https://github.com/vllm-project/vllm/pull/60110) — [ROCm][Perf][Kimi-K3] Fold q_b_proj and W_UK into one GEMM for the MLA decode query (#60110)
- **2026-10-27** [`889d635dd7`](https://github.com/vllm-project/vllm/commit/889d635dd7) [#53166](https://github.com/vllm-project/vllm/pull/53166) — [Perf][ROCm][Attention] Fuse Kimi-K3 MLA chunked-context gather on AITER (#53166)
- **2026-10-27** [`228b1e3d23`](https://github.com/vllm-project/vllm/commit/228b1e3d23) [#59668](https://github.com/vllm-project/vllm/pull/59668) — [ROCm][DSV4.1][Perf] Single-launch DSA decode candidate mask (#59668)
- **2026-10-27** [`83909ad84b`](https://github.com/vllm-project/vllm/commit/83909ad84b) [#57015](https://github.com/vllm-project/vllm/pull/57015) — [ROCm][Perf] W4A16: widen skinny GEMM LDS activation loads to b128 (#57015)
- **2026-10-27** [`e7fa26d5c8`](https://github.com/vllm-project/vllm/commit/e7fa26d5c8) [#63996](https://github.com/vllm-project/vllm/pull/63996) — [Model][Spec Decode] Refactor #41834 with useful improvements (#63996)
- **2026-10-27** [`f8f7634cb4`](https://github.com/vllm-project/vllm/commit/f8f7634cb4) [#63342](https://github.com/vllm-project/vllm/pull/63342) — [ROCm][Perf][Kimi-K3] Use block_m=128 for the fused KDA prefill conv1d (#63342)
- **2026-10-27** [`8d88bc5d81`](https://github.com/vllm-project/vllm/commit/8d88bc5d81) [#60154](https://github.com/vllm-project/vllm/pull/60154) — [ROCm][DSv4/4.1] Fuse inverse RoPE and MXFP8 quant into the aiter sparse MLA and sparse MLA gating changes (#60154)
- **2026-10-27** [`5f1a564181`](https://github.com/vllm-project/vllm/commit/5f1a564181) [#63726](https://github.com/vllm-project/vllm/pull/63726) — [Recipe][AMD] Refresh Kimi-K3 PD configurations (#63726)
- **2026-10-27** [`de58886274`](https://github.com/vllm-project/vllm/commit/de58886274) [#62120](https://github.com/vllm-project/vllm/pull/62120) — [CI] Move B200 Kernels and MoE Refactor evals from manual to automatic shards (#62120)
- **2026-10-27** [`eb5e8d1cc8`](https://github.com/vllm-project/vllm/commit/eb5e8d1cc8) [#62537](https://github.com/vllm-project/vllm/pull/62537) — [CI] Move L4 Distributed Models and LoRA TP and their AMD mirrors from fixed to automatic shards (#62537)
- **2026-10-27** [`659defd662`](https://github.com/vllm-project/vllm/commit/659defd662) [#61904](https://github.com/vllm-project/vllm/pull/61904) — [CI] Shard the AMD mirrors of Basic Models (Other) and PCP automatically (#61904)
- **2026-10-27** [`f62e80ff04`](https://github.com/vllm-project/vllm/commit/f62e80ff04) [#63907](https://github.com/vllm-project/vllm/pull/63907) — [CI] Enroll 4 steps and 2 AMD mirrors in automatic sharding (#63907)
- **2026-10-27** [`7c713621f3`](https://github.com/vllm-project/vllm/commit/7c713621f3) [#63850](https://github.com/vllm-project/vllm/pull/63850) — [CI][ROCm] Preflight idle-GPU check in test_pp_cudagraph (#63850)
- **2026-10-27** [`5314c58281`](https://github.com/vllm-project/vllm/commit/5314c58281) [#63332](https://github.com/vllm-project/vllm/pull/63332) — [ROCm][Recipe] Qwen3.8-Flash-Next: add MI355X Quark MXFP4 variant (TP1/TP2) (#63332)
- **2026-10-27** [`5c1eb11cb3`](https://github.com/vllm-project/vllm/commit/5c1eb11cb3) [#60234](https://github.com/vllm-project/vllm/pull/60234) — [Bugfix] Allow pipeline parallelism for Qwen4Exp PLE models and their MTP drafter (#60234)
- **2026-10-27** [`6fe3d447ac`](https://github.com/vllm-project/vllm/commit/6fe3d447ac) [#62141](https://github.com/vllm-project/vllm/pull/62141) — [CI][AMD] Mirror ReplaySSM, MiniMax-M3 attention kernels and Kimi K3 prefix cache on MI355 (#62141)
- **2026-10-27** [`3d81a510f9`](https://github.com/vllm-project/vllm/commit/3d81a510f9) [#48989](https://github.com/vllm-project/vllm/pull/48989) — [ROCm] DeepSeek-V4-Pro PD Disaggregation through MORI IO KV Connector on AMD GPUs (#48989)
- **2026-10-27** [`1e10a92d1d`](https://github.com/vllm-project/vllm/commit/1e10a92d1d) [#63833](https://github.com/vllm-project/vllm/pull/63833) — [Bugfix][ROCm] Wait on per-slot events in packed NCCL consumer (#63833)
- **2026-10-27** [`9b8944f500`](https://github.com/vllm-project/vllm/commit/9b8944f500) [#63868](https://github.com/vllm-project/vllm/pull/63868) — [Docs][Recipe] Align MiniMax-M3 MI355X AgentX monokernel profile (#63868)
- **2026-10-27** [`ed1a730795`](https://github.com/vllm-project/vllm/commit/ed1a730795) [#63689](https://github.com/vllm-project/vllm/pull/63689) — [Bugfix][ROCm][DSv4] Give zero and subnormal mono MXFP8 groups vLLM's scale code (#63689)
- **2026-10-26** [`26cbb47d48`](https://github.com/vllm-project/vllm/commit/26cbb47d48) [#63554](https://github.com/vllm-project/vllm/pull/63554) — [Spec Decode][Sampling] Batch-sharded draft logits (#63554)
- **2026-10-26** [`967c39f89e`](https://github.com/vllm-project/vllm/commit/967c39f89e) [#63408](https://github.com/vllm-project/vllm/pull/63408) — [CI] List one test path per line in Buildkite pytest commands to avoid merge conflicts (#63408)
- **2026-10-26** [`70d67f19dc`](https://github.com/vllm-project/vllm/commit/70d67f19dc) [#63828](https://github.com/vllm-project/vllm/pull/63828) — [ROCm][CI] Release checkpoint page cache between language generation … (#63828)
- **2026-10-26** [`442f3d989e`](https://github.com/vllm-project/vllm/commit/442f3d989e) [#63557](https://github.com/vllm-project/vllm/pull/63557) — [CI][ROCm] Take NIXL PD accuracy side-channel ports from below the ephemeral range (#63557)
- **2026-10-26** [`ad42b456f9`](https://github.com/vllm-project/vllm/commit/ad42b456f9) [#63453](https://github.com/vllm-project/vllm/pull/63453) — [CI][ROCm] Take MoRIIO P/D test port blocks from below the ephemeral range (#63453)
- **2026-10-26** [`088e6a4d68`](https://github.com/vllm-project/vllm/commit/088e6a4d68) [#63559](https://github.com/vllm-project/vllm/pull/63559) — [CI][ROCm] Skip the AITER MoE garbage-rows test for fp8 per-tensor until the AITER fix (#63559)
- **2026-10-26** [`94b35f3780`](https://github.com/vllm-project/vllm/commit/94b35f3780) [#63558](https://github.com/vllm-project/vllm/pull/63558) — [Bugfix][ROCm] Keep the AITER GDN decode fast path off for the DS conv-state layout (#63558)
- **2026-10-26** [`9744ada582`](https://github.com/vllm-project/vllm/commit/9744ada582) [#63576](https://github.com/vllm-project/vllm/pull/63576) — [Bugfix][ROCm][DSv4.1] Await krdy before K2's combine reads klen in index-source launches (#63576)
- **2026-10-26** [`536854bf10`](https://github.com/vllm-project/vllm/commit/536854bf10) [#59255](https://github.com/vllm-project/vllm/pull/59255) — [ROCm] Enable expert parallelism for AITER Triton W4A16 MoE (#59255)
- **2026-10-26** [`df8b5d3781`](https://github.com/vllm-project/vllm/commit/df8b5d3781) [#63760](https://github.com/vllm-project/vllm/pull/63760) — [ROCm][CI] Raise MI300 Core Operation Kernels timeout to 90 min (#63760)
- **2026-10-26** [`50a184f435`](https://github.com/vllm-project/vllm/commit/50a184f435) [#63256](https://github.com/vllm-project/vllm/pull/63256) — [RL] Declare weight ownership and layout on ParamMeta (#63256)
- **2026-10-26** [`d0d681e40d`](https://github.com/vllm-project/vllm/commit/d0d681e40d) [#63669](https://github.com/vllm-project/vllm/pull/63669) — [ROCm][Perf] Make MXFP4 the default indexer K cache dtype for DeepSeek-V4 (#63669)
- **2026-10-26** [`c3941c032d`](https://github.com/vllm-project/vllm/commit/c3941c032d) [#63099](https://github.com/vllm-project/vllm/pull/63099) — [Bugfix][ROCm] Match the DeepSeek-V4.1 FP8 config in the shared-expert FSE compatibility check (#63099)
- **2026-10-26** [`9bea474d65`](https://github.com/vllm-project/vllm/commit/9bea474d65) [#59478](https://github.com/vllm-project/vllm/pull/59478) — [ROCm][Perf] Use AITER FlyDSL INT4 QuickReduce when INT4 QuickReduce is selected (#59478)
- **2026-10-26** [`ae3bc684e0`](https://github.com/vllm-project/vllm/commit/ae3bc684e0) [#63665](https://github.com/vllm-project/vllm/pull/63665) — [Doc][ROCm] Update DeepSeek-V4.1-Flash MI355X AgentX scheduling profiles (#63665)
- **2026-10-26** [`2f34dce583`](https://github.com/vllm-project/vllm/commit/2f34dce583) [#63657](https://github.com/vllm-project/vllm/pull/63657) — [Doc][ROCm] Update Kimi-K3 MI355X AgentX scheduling cells (#63657)
- **2026-10-26** [`00b6c4c565`](https://github.com/vllm-project/vllm/commit/00b6c4c565) [#59774](https://github.com/vllm-project/vllm/pull/59774) — [ROCm] Octave KV (`ROCM_OCTAVE`): native 3-bit KV cache backend for AMD GPUs (#59774)
- **2026-10-26** [`0f6b261910`](https://github.com/vllm-project/vllm/commit/0f6b261910) [#61879](https://github.com/vllm-project/vllm/pull/61879) — [Model] Add Muse Spark Open support (#61879)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#56851](https://github.com/vllm-project/vllm/issues/56851) | [RFC]: Request level text and derender output on `/inference/v1/genera | RFC, kimi, k3 | 2026-11-02 |
| [#65204](https://github.com/vllm-project/vllm/issues/65204) | [Bug]: Extensible KV cache + KV offload connector fails to start: gran | bug, quantization | 2026-11-02 |
| [#65205](https://github.com/vllm-project/vllm/issues/65205) | [Bug]: Muse Spark (NVIDIA path): 46 private fp32 RoPE tables of 1M row | nvidia | 2026-11-02 |
| [#49569](https://github.com/vllm-project/vllm/issues/49569) | [Feature]: Plan for enabling mypy in tests directory | feature request, quantization | 2026-11-02 |
| [#37191](https://github.com/vllm-project/vllm/issues/37191) | [Bug]: Benchmark tuning MoE kernel config fails due to triton 3.6 | bug, stale | 2026-11-02 |
| [#52916](https://github.com/vllm-project/vllm/issues/52916) | [RFC] Adaptive spin grace + bounded arch waits (aarch64 WFET, x86 WAIT | cpu | 2026-11-02 |
| [#49926](https://github.com/vllm-project/vllm/issues/49926) | [Bug]: EngineDeadError NVFP4 marlin | bug, quantization | 2026-11-02 |
| [#51035](https://github.com/vllm-project/vllm/issues/51035) | [Bug]: DeepSeek-V4 sparse-decode MLA kernel wedges in a spin loop with | — | 2026-11-02 |
| [#38256](https://github.com/vllm-project/vllm/issues/38256) | [RFC]: Incremental MoE Expert Offloading — GPU Cache + Async Pipeline | — | 2026-11-02 |
| [#65190](https://github.com/vllm-project/vllm/issues/65190) | [ROCm][Bug] SimpleCPUOffloadConnector wedges engine (0 tok/s) with Mus | rocm | 2026-11-02 |
| [#64793](https://github.com/vllm-project/vllm/issues/64793) | [Bug]: Responses API rejects `developer` role for Mistral Large 4 with | bug, mistral | 2026-11-02 |
| [#57406](https://github.com/vllm-project/vllm/issues/57406) | [Feature]: GLM 5.3 Performance Optimization | feature request, glm | 2026-11-02 |
| [#65193](https://github.com/vllm-project/vllm/issues/65193) | [Bug][Quantization] MXFP8 linear kernel selection ignores the requeste | quantization | 2026-11-02 |
| [#59038](https://github.com/vllm-project/vllm/issues/59038) | [RFC]: DeepSeek-V4.1-Flash performance on MI325X (gfx942) | rocm, deepseek, DSv4.1 | 2026-11-02 |
| [#54966](https://github.com/vllm-project/vllm/issues/54966) | [CI][Refactor] Comprehensive `AiterExperts` test coverage and possible | feature request, rocm, quantization, kimi | 2026-11-02 |
| [#65173](https://github.com/vllm-project/vllm/issues/65173) | [Bug] DeepSeek V4.1 Flash selects the last optional tool parameter bas | bug, structured-output, tool-calling, deepseek, DSv4.1 | 2026-11-02 |
| [#65172](https://github.com/vllm-project/vllm/issues/65172) | [RFC]: Holemiss: Selective Recovery of Partially Lost LLM Cache State | RFC | 2026-11-02 |
| [#62532](https://github.com/vllm-project/vllm/issues/62532) | [RFC]: [V1 Scheduler][KV Offload] Eliminate 1.0–1.8s Re-Queueing Stall | RFC, scheduler | 2026-11-02 |
| [#65151](https://github.com/vllm-project/vllm/issues/65151) | [Feature][ROCm]: Configurable HIP host wait policy for WSL GPU workers | feature request, rocm | 2026-11-02 |
| [#56482](https://github.com/vllm-project/vllm/issues/56482) | [Bug]: DSML tool-call recovery (#55954) emits ghost empty-argument cal | tool-calling | 2026-11-02 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 136 |
| Attention | 65 |
| KV Cache / Offload | 47 |
| MoE / Expert Parallel | 43 |
| Serving / API | 39 |
| Other | 38 |
| Scheduler / Engine | 34 |
| Multimodal | 32 |
| Models | 30 |
| Disaggregation / PD | 25 |
| Speculative Decoding | 22 |
| CI / Build | 20 |
| Quantization | 19 |
| LoRA | 14 |
| Perf / Benchmark | 11 |
| Docs | 9 |
| Compilation / CUDA Graph | 6 |

## ROCm / AMD  (136 commits)

- **2026-11-02** [`84e59a3b74`](https://github.com/vllm-project/vllm/commit/84e59a3b74) [#62716](https://github.com/vllm-project/vllm/pull/62716)
  [ROCm][Build][1/5] Speed up ROCm build: generate the paged attention instantiations from one variant list (#62716)
  _Files: `CMakeLists.txt`, `csrc/rocm/.gitignore`, `csrc/rocm/attention_dispatch.cu`, `csrc/rocm/attention_kernels.cuh` _+14 more__
- **2026-11-02** [`542bc671b7`](https://github.com/vllm-project/vllm/commit/542bc671b7) [#64589](https://github.com/vllm-project/vllm/pull/64589)
  [Docs] Add DeepSeek-V4.1-Flash MI325X AgentX preset (#64589)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-11-02** [`887eef12e1`](https://github.com/vllm-project/vllm/commit/887eef12e1) [#60102](https://github.com/vllm-project/vllm/pull/60102)
  [ROCm][DSv4.1][Perf] Route gfx942 sparse MLA prefill to AITER pa_prefill_sparse (#60102)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-11-02** [`eff37e8e24`](https://github.com/vllm-project/vllm/commit/eff37e8e24) [#64448](https://github.com/vllm-project/vllm/pull/64448)
  [ROCm][MiniMax-M3.1] NVFP4 indexer: decode CP for DSpark 7 (#64448)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`, `vllm/models/minimax_m3/amd/indexer_msa.py` _+3 more__
- **2026-11-02** [`4890c7ff35`](https://github.com/vllm-project/vllm/commit/4890c7ff35) [#65184](https://github.com/vllm-project/vllm/pull/65184)
  [ROCm][CI] Gate MoRI EPv2 modular-kernel cases on the production EPv2 checks (#65184)
  _Files: `tests/kernels/moe/modular_kernel_tools/mk_objects.py`_
- **2026-11-02** [`a708b0f639`](https://github.com/vllm-project/vllm/commit/a708b0f639) [#64734](https://github.com/vllm-project/vllm/pull/64734)
  [ROCm][CI] Raise the MI355 DeepSeek-V3.2 GSM8K startup wait to 1800s (#64734)
  _Files: `tests/evals/gsm8k/configs/DeepSeek-V3.2-DP_MI355.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V3.2-TP_MI355.yaml`_
- **2026-11-02** [`f9db1756e9`](https://github.com/vllm-project/vllm/commit/f9db1756e9) [#57678](https://github.com/vllm-project/vllm/pull/57678)
  [Model Loader] One post-load hook signature; the loader runs every module's hook (#57678)
  _Files: `tests/compile/passes/test_mla_attn_quant_fusion.py`, `tests/kernels/core/test_vit_fp8_scaling.py`, `tests/model_executor/model_loader/test_reload.py`, `tests/models/kimi_k3/test_amd_qb_uk_fold.py` _+19 more__
- **2026-11-02** [`380c8e438c`](https://github.com/vllm-project/vllm/commit/380c8e438c) [#65157](https://github.com/vllm-project/vllm/pull/65157)
  [Docs] Fix accidental cross-references in docstrings (#65157)
  _Files: `vllm/_custom_ops.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/back.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/layer.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/stages/moe.py` _+2 more__
- **2026-11-02** [`a487973b6f`](https://github.com/vllm-project/vllm/commit/a487973b6f) [#65140](https://github.com/vllm-project/vllm/pull/65140)
  [ROCm][CI] Fix Muse Spark RoPE cache leak between tests (#65140)
  _Files: `tests/models/test_muse_spark_rocm_shared_rope.py`_
- **2026-11-02** [`5689c2790c`](https://github.com/vllm-project/vllm/commit/5689c2790c) [#65080](https://github.com/vllm-project/vllm/pull/65080)
  [Bugfix][ROCm] Muse Spark: merge the two process_weights_after_loading hooks (#65080)
  _Files: `vllm/models/muse_spark/amd/model.py`_
- **2026-11-02** [`51c6dfd8c8`](https://github.com/vllm-project/vllm/commit/51c6dfd8c8) [#64029](https://github.com/vllm-project/vllm/pull/64029)
  [ROCm][Perf][Kimi-K3] Specialized decode K2: sentinel all-reduces, pre-AR loads, tagged x rows (#64029)
  _Files: `tests/models/kimi_k3/amd_specialized_decode/test_engine_fault.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`, `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md` _+18 more__
- **2026-11-02** [`0e5b2ba118`](https://github.com/vllm-project/vllm/commit/0e5b2ba118) [#64179](https://github.com/vllm-project/vllm/pull/64179)
  [Model] Enable --mm-encoder-tp-mode data for MiMo-V2.6 (#64179)
  _Files: `.buildkite/test-amd.yaml`, `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/mimo_v2_omni.py`_
- **2026-11-02** [`b2fcbdd164`](https://github.com/vllm-project/vllm/commit/b2fcbdd164) [#64355](https://github.com/vllm-project/vllm/pull/64355)
  [CI] Enroll five steps and four AMD mirrors in automatic sharding (#64355)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/models_language.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-11-02** [`4c393ce427`](https://github.com/vllm-project/vllm/commit/4c393ce427) [#64181](https://github.com/vllm-project/vllm/pull/64181)
  [CI] Enroll three standalone AMD steps in automatic sharding (#64181)
  _Files: `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/models_basic.yaml`_
- **2026-11-02** [`be09292f09`](https://github.com/vllm-project/vllm/commit/be09292f09) [#63440](https://github.com/vllm-project/vllm/pull/63440)
  [ROCm][Perf][Muse Spark] FlyDSL decode monokernel for DSpark verify steps on MI355X (--monokernel) (#63440)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `pyproject.toml`, `recipes/models/meta-models/Muse-Spark-Open-816B-A42B.yaml`, `tests/models/test_muse_spark_logits_local.py` _+14 more__
- **2026-11-02** [`3d23773f10`](https://github.com/vllm-project/vllm/commit/3d23773f10) [#64614](https://github.com/vllm-project/vllm/pull/64614)
  [Bugfix][ROCm] Use 64-bit row offsets in the RDNA hybrid W4A16 GEMM (#64614)
  _Files: `tests/kernels/quantization/test_rdna_hybrid_w4a16.py`, `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`_
- **2026-11-02** [`cc69774820`](https://github.com/vllm-project/vllm/commit/cc69774820) [#63892](https://github.com/vllm-project/vllm/pull/63892)
  [ROCm][Perf][DSv4.1] Mono: batch TP4 K2's X8 copies, load its push's peer bases late (#63892)
  _Files: `tests/models/test_dsv41_mono_numerics.py`, `vllm/models/deepseek_v41/amd/mono/layer.py`, `vllm/models/deepseek_v41/amd/mono/stages/moe.py`_
- **2026-11-02** [`de53c2deed`](https://github.com/vllm-project/vllm/commit/de53c2deed) [#61950](https://github.com/vllm-project/vllm/pull/61950)
  [Bugfix][ROCm] Fix Kimi K3 online quantization with padded projections (#61950)
  _Files: `vllm/models/kimi_k3/amd/kda.py`_
- **2026-11-01** [`63d3d39c84`](https://github.com/vllm-project/vllm/commit/63d3d39c84) [#59961](https://github.com/vllm-project/vllm/pull/59961)
  [Bugfix][DSv3.2] Carry the shared indexer top-k across pipeline stages (#59961)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/deepseek_v32/test_pp_topk.py`, `tests/models/deepseek_v32/test_sequence_parallel.py`, `vllm/model_executor/models/utils.py` _+8 more__
- **2026-10-31** [`564ac0de1b`](https://github.com/vllm-project/vllm/commit/564ac0de1b) [#64792](https://github.com/vllm-project/vllm/pull/64792)
  [Docs][ROCm] Mistral Large 4 recipe: adds TP4 and lowest-latency presets  (#64792)
  _Files: `recipes/models/mistralai/Mistral-Large-4-1T-A52B.yaml`_
- **2026-10-31** [`b03e788812`](https://github.com/vllm-project/vllm/commit/b03e788812) [#64805](https://github.com/vllm-project/vllm/pull/64805)
  [Docs][ROCm] Add MiniMax-M3.1-Flash MI355X TP4 AgentX preset (#64805)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-10-31** [`3f9d184738`](https://github.com/vllm-project/vllm/commit/3f9d184738) [#64804](https://github.com/vllm-project/vllm/pull/64804)
  [Docs][ROCm] Add DeepSeek-V4.1-Flash MI355X TP8 concurrency-1 AgentX preset (#64804)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-10-31** [`25fc60723c`](https://github.com/vllm-project/vllm/commit/25fc60723c) [#60618](https://github.com/vllm-project/vllm/pull/60618)
  [Perf][Kernel] Single-launch fused scoring+top-k kernel for sparse-indexer prefill, without materializing logits (#60618)
  _Files: `.buildkite/test_areas/kernels.yaml`, `CMakeLists.txt`, `csrc/fused_mqa_topk/candidates.cuh`, `csrc/fused_mqa_topk/common.cuh` _+18 more__
- **2026-10-31** [`50f622bdcf`](https://github.com/vllm-project/vllm/commit/50f622bdcf) [#63174](https://github.com/vllm-project/vllm/pull/63174)
  Skip redundant weight tensor clones for loaders that yield owned tensors (#63174)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `requirements/rocm.txt`, `requirements/test/cpu.txt` _+12 more__
- **2026-10-31** [`7b77ed581d`](https://github.com/vllm-project/vllm/commit/7b77ed581d) [#64368](https://github.com/vllm-project/vllm/pull/64368)
  [Spec Decode][ROCm] draft_lm_head_quantization for DSpark drafters (#64368)
  _Files: `tests/model_executor/test_qwen3_omni.py`, `vllm/config/speculative.py`, `vllm/v1/worker/gpu/spec_decode/dspark/config.py`, `vllm/v1/worker/gpu/spec_decode/dspark/utils.py` _+2 more__
- **2026-10-31** [`d5301a4f54`](https://github.com/vllm-project/vllm/commit/d5301a4f54) [#61361](https://github.com/vllm-project/vllm/pull/61361)
  [MORI] Add MORI EP V2 support (#61361)
  _Files: `docs/serving/expert_parallel_deployment.md`, `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/modular_kernel_tools/mk_objects.py`, `tests/kernels/moe/test_moe_layer.py` _+16 more__
- **2026-10-31** [`c4f54cf5b3`](https://github.com/vllm-project/vllm/commit/c4f54cf5b3) [#63116](https://github.com/vllm-project/vllm/pull/63116)
  [Bugfix][ROCm] Size AITER MLA persistent metadata for every decode query length (#63116)
  _Files: `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-10-31** [`e3eec51570`](https://github.com/vllm-project/vllm/commit/e3eec51570) [#63297](https://github.com/vllm-project/vllm/pull/63297)
  [ROCm][Kimi-K3] Keep KDA prefill checkpoints with the gluon backend (#63297)
  _Files: `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_amd_kda_chunk.py`, `vllm/models/kimi_k3/amd/kda.py`_
- **2026-10-31** [`138dfa5463`](https://github.com/vllm-project/vllm/commit/138dfa5463) [#64094](https://github.com/vllm-project/vllm/pull/64094)
  [ROCm][DSv4.1][Perf]  Enable prefix-cache SWA replay on gfx950 (#64094)
  _Files: `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/attention.py`_
- **2026-10-31** [`58f245c69d`](https://github.com/vllm-project/vllm/commit/58f245c69d) [#64820](https://github.com/vllm-project/vllm/pull/64820)
  [Kernel] Qwen4Exp: compute HyperConnection and PLE gate row offsets in int64 (#64820)
  _Files: `vllm/models/qwen4_exp/amd/ops/hc.py`, `vllm/models/qwen4_exp/common/ops/ple.py`, `vllm/models/qwen4_exp/nvidia/ops/hc.py`_
- **2026-10-31** [`17550580e9`](https://github.com/vllm-project/vllm/commit/17550580e9) [#61837](https://github.com/vllm-project/vllm/pull/61837)
  [ROCm][Model] Step-5-Preview support on ROCm (#61837)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `docs/models/supported_models.md`, `tests/config/test_step5_mtp_config.py` _+42 more__
- **2026-10-30** [`59d58fd261`](https://github.com/vllm-project/vllm/commit/59d58fd261) [#64740](https://github.com/vllm-project/vllm/pull/64740)
  [ROCm][CI] Run MI355 MoE Kernels on a full MI355 instead of DPX (#64740)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-10-30** [`d2d550c3fc`](https://github.com/vllm-project/vllm/commit/d2d550c3fc) [#64602](https://github.com/vllm-project/vllm/pull/64602)
  [CI] Remove the retired A100 queue's steps; keep their live AMD mirrors standalone (#64602)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/misc.yaml`, `tests/evals/gsm8k/configs/humming/config-a100-act-int8-shard-0.txt` _+4 more__
- **2026-10-30** [`14a5bb4adc`](https://github.com/vllm-project/vllm/commit/14a5bb4adc) [#64357](https://github.com/vllm-project/vllm/pull/64357)
  [Model Loader] Run the model-level post-load hook once at the end of every load and reload (#64357)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `tests/model_executor/model_loader/tensorizer_loader/test_tensorizer.py`, `tests/model_executor/model_loader/test_expert_substitution.py` _+42 more__
- **2026-10-30** [`67d677bdef`](https://github.com/vllm-project/vllm/commit/67d677bdef) [#64577](https://github.com/vllm-project/vllm/pull/64577)
  [ROCm][CI] Prebuild mamba-ssm and causal-conv1d into the CI test image (#64577)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_language.yaml`, `docker/Dockerfile.rocm`_
- **2026-10-30** [`7495e9e5a4`](https://github.com/vllm-project/vllm/commit/7495e9e5a4) [#63774](https://github.com/vllm-project/vllm/pull/63774)
  [ROCm] Bump AITER to v0.1.27 (#63774)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-10-30** [`644a9f5d27`](https://github.com/vllm-project/vllm/commit/644a9f5d27) [#64779](https://github.com/vllm-project/vllm/pull/64779)
  [Deps] Upgrade to huggingface_hub 2 (#64779)
  _Files: `requirements/build/rock.txt`, `requirements/common.txt`, `requirements/rocm.txt`, `requirements/test/cpu.txt` _+6 more__
- **2026-10-30** [`42379a4c24`](https://github.com/vllm-project/vllm/commit/42379a4c24) [#63205](https://github.com/vllm-project/vllm/pull/63205)
  [Model Runner V2][Spec Decode] Speculator config classes and custom speculators (#63205)
  _Files: `docs/features/speculative_decoding/README.md`, `tests/config/test_speculative_draft_hf_overrides.py`, `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/models/kimi_k3/test_amd_kda_checkpoint.py` _+63 more__
- **2026-10-30** [`e811e502ef`](https://github.com/vllm-project/vllm/commit/e811e502ef) [#64727](https://github.com/vllm-project/vllm/pull/64727)
  [ROCm][CI] Fix AITER MXFP4 padding tests failing instead of skipping on MI300 (#64727)
  _Files: `tests/kernels/moe/test_modular_kernel_combinations.py`_
- **2026-10-30** [`dc4dd5a221`](https://github.com/vllm-project/vllm/commit/dc4dd5a221) [#62007](https://github.com/vllm-project/vllm/pull/62007)
  [ROCm][DI][CI]  Add DeepSeek-V3 NIXL accuracy steps (#62007)
  _Files: `.buildkite/amd-disagg/cluster.sh`, `.buildkite/amd-disagg/pipeline-disagg.yaml`, `.buildkite/amd-disagg/run-slurm-disagg-test.sh`, `.buildkite/amd-disagg/run_xPyD_disagg.slurm` _+1 more__
- **2026-10-30** [`ca5c2d7843`](https://github.com/vllm-project/vllm/commit/ca5c2d7843) [#64708](https://github.com/vllm-project/vllm/pull/64708)
  [ROCm][CI] Drop LD_PRELOAD from the subprocess env in test_amd_ci_fast_exit (#64708)
  _Files: `tests/tools/test_amd_ci_fast_exit.py`_
- **2026-10-30** [`8a2a5e4c40`](https://github.com/vllm-project/vllm/commit/8a2a5e4c40) [#64004](https://github.com/vllm-project/vllm/pull/64004)
  [ROCm][Kimi-K3][Perf] Cut gfx942 MXFP4-to-int4 requant time under pure TP (#64004)
  _Files: `tests/kernels/quantization/test_k3_gfx942_int4_requant.py`, `vllm/model_executor/layers/quantization/mxfp4.py`_
- **2026-10-30** [`617135eed3`](https://github.com/vllm-project/vllm/commit/617135eed3) [#61794](https://github.com/vllm-project/vllm/pull/61794)
  [Test][UMBP][6/10] Add embedded runtime and MORI integration coverage (#61794)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/misc.yaml`, `docker/Dockerfile.rocm_base` _+8 more__
- **2026-10-30** [`336d883f41`](https://github.com/vllm-project/vllm/commit/336d883f41) [#64569](https://github.com/vllm-project/vllm/pull/64569)
  [CI] Enroll 6 steps and 10 AMD mirrors in automatic sharding (#64569)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/misc.yaml` _+1 more__
- **2026-10-30** [`d492ee7862`](https://github.com/vllm-project/vllm/commit/d492ee7862) [#64110](https://github.com/vllm-project/vllm/pull/64110)
  [Qwen4Exp] Remove FlashAttention dependency and standardize QSA naming (#64110)
  _Files: `tests/models/qwen4_exp/test_qsa_amd.py`, `tests/models/qwen4_exp/test_qsa_prepare.py`, `tests/models/qwen4_exp/test_qsa_prepare_amd.py`, `tests/models/qwen4_exp/test_qsa_reference.py` _+7 more__
- **2026-10-30** [`1353e1926f`](https://github.com/vllm-project/vllm/commit/1353e1926f) [#60867](https://github.com/vllm-project/vllm/pull/60867)
  [KV Connector][ROCm] MoRIIO: hybrid READ for several attention groups and shared-group speculative methods (#60867)
  _Files: `docs/features/moriio_connector_usage.md`, `tests/v1/kv_connector/unit/test_moriio_hetero_tp_write.py`, `tests/v1/kv_connector/unit/test_moriio_hma_scheduler.py`, `tests/v1/kv_connector/unit/test_moriio_kv_layout.py` _+2 more__
- **2026-10-30** [`1fbde73aa1`](https://github.com/vllm-project/vllm/commit/1fbde73aa1) [#64529](https://github.com/vllm-project/vllm/pull/64529)
  [CI] Bump Transformers version to 5.22.0 (#64529)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+6 more__
- **2026-10-30** [`8730884ab1`](https://github.com/vllm-project/vllm/commit/8730884ab1) [#64655](https://github.com/vllm-project/vllm/pull/64655)
  [CI][ROCm] Check skinny-GEMM guard dispatch without torch.profiler (#64655)
  _Files: `tests/model_executor/layers/test_lmhead_skinny_gemm_guard.py`_
- **2026-10-30** [`6d01893483`](https://github.com/vllm-project/vllm/commit/6d01893483) [#64567](https://github.com/vllm-project/vllm/pull/64567)
  [ROCm][Bugfix] Skip AITER tuned GEMM when M*N >= 2^31 on gfx950 (#64567)
  _Files: `vllm/model_executor/layers/utils.py`_
- **2026-10-30** [`2eae56c4ba`](https://github.com/vllm-project/vllm/commit/2eae56c4ba) [#64610](https://github.com/vllm-project/vllm/pull/64610)
  [ROCm][CI] Update ROCm AITER nightly staging index (#64610)
  _Files: `.buildkite/scripts/rocm/select_aiter_nightly_wheel.py`_
- **2026-10-30** [`e49ea84e92`](https://github.com/vllm-project/vllm/commit/e49ea84e92) [#63885](https://github.com/vllm-project/vllm/pull/63885)
  [ROCm][Perf][DSv4.1] Build the SWA decode metadata in one launch  (#63885)
  _Files: `tests/models/test_dsv41_mono_decode.py`, `vllm/models/deepseek_v41/amd/ops/__init__.py`, `vllm/models/deepseek_v41/amd/ops/swa_decode_meta.py`, `vllm/models/deepseek_v41/amd/rocm.py`_
- **2026-10-30** [`f81a414fae`](https://github.com/vllm-project/vllm/commit/f81a414fae) [#63054](https://github.com/vllm-project/vllm/pull/63054)
  [Bugfix][ROCm] Use 64-bit row offsets in the Triton W4A16 GEMM (#63054)
  _Files: `tests/kernels/quantization/test_triton_w4a16.py`, `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`_
- **2026-10-30** [`daccf69eb2`](https://github.com/vllm-project/vllm/commit/daccf69eb2) [#64619](https://github.com/vllm-project/vllm/pull/64619)
  [CI][Kimi-K3] Add enable_adaptive_verification to the KDA checkpoint test stub (#64619)
  _Files: `tests/models/kimi_k3/test_amd_kda_checkpoint.py`_
- **2026-10-29** [`10579b71eb`](https://github.com/vllm-project/vllm/commit/10579b71eb) [#64544](https://github.com/vllm-project/vllm/pull/64544)
  [Docs][ROCm] Mistral Large 4 recipe: ROCm image tag, MI355X, TP4 replica launch (#64544)
  _Files: `recipes/models/mistralai/Mistral-Large-4-1T-A52B.yaml`_
- **2026-10-29** [`434eadcbf8`](https://github.com/vllm-project/vllm/commit/434eadcbf8) [#64115](https://github.com/vllm-project/vllm/pull/64115)
  [CI] Enroll two steps and two AMD mirrors in automatic sharding (#64115)
  _Files: `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-10-29** [`f97a8d6647`](https://github.com/vllm-project/vllm/commit/f97a8d6647) [#64101](https://github.com/vllm-project/vllm/pull/64101)
  [ROCm][Perf][DSv4.1] Mono decode at TP8 on MI355X (#64101)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_dsv41_mono_layers.py`, `tests/models/test_dsv41_mono_numerics.py`, `vllm/models/deepseek_v41/amd/mono/README.md` _+4 more__
- **2026-10-29** [`2abde627d9`](https://github.com/vllm-project/vllm/commit/2abde627d9) [#64378](https://github.com/vllm-project/vllm/pull/64378)
  [ROCm][Quantization] NVFP4 MoE re-quantization and fused shared experts through online quantization (#64378)
  _Files: `tests/kernels/moe/test_moe_weight_loading_padded.py`, `tests/kernels/quantization/test_nvfp4_emulation.py`, `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/model_executor/model_loader/test_reload.py` _+24 more__
- **2026-10-29** [`e18e2c70c5`](https://github.com/vllm-project/vllm/commit/e18e2c70c5) [#63816](https://github.com/vllm-project/vllm/pull/63816)
  [Bugfix][ROCm][DSv4.1] Guard NaN scores in gfx942 mono routing (#63816)
  _Files: `tests/kernels/models/amd/test_dsv41_mono_gfx942.py`, `vllm/models/deepseek_v41/amd/mono/stages/moe.py`_
- **2026-10-29** [`0124e16a6c`](https://github.com/vllm-project/vllm/commit/0124e16a6c) [#62481](https://github.com/vllm-project/vllm/pull/62481)
  [ROCm] Monitor FlyDSL JIT compilation after warmup (#62481)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/jit_monitor.yaml`, `tests/jit_monitor/conftest.py`, `tests/jit_monitor/test_flydsl_contract.py` _+2 more__
- **2026-10-29** [`bc57dc9d53`](https://github.com/vllm-project/vllm/commit/bc57dc9d53) [#63384](https://github.com/vllm-project/vllm/pull/63384)
  [Transformers backend] Migrate OLMoE and fix MoE LoRA (#63384)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/lora.yaml`, `.buildkite/test_areas/misc.yaml`, `docs/models/supported_models.md` _+9 more__
- **2026-10-29** [`bba4d9afec`](https://github.com/vllm-project/vllm/commit/bba4d9afec) [#61939](https://github.com/vllm-project/vllm/pull/61939)
  [ROCm] Revamp CI/release deployment: collapse image tiers, unify build pipeline (#61939)
  _Files: `.buildkite/ci_config_rocm.yaml`, `.buildkite/hardware_tests/amd.yaml`, `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/annotate-rocm-release.sh` _+37 more__
- **2026-10-29** [`6c71831f25`](https://github.com/vllm-project/vllm/commit/6c71831f25) [#62976](https://github.com/vllm-project/vllm/pull/62976)
  [CI][ROCm][MoE] Add AITER_MOE_SORT_BACKEND MXFP4 DSV4 test coverage (#62976)
  _Files: `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/test_modular_kernel_combinations.py`_
- **2026-10-29** [`e3f03f4f89`](https://github.com/vllm-project/vllm/commit/e3f03f4f89) [#62996](https://github.com/vllm-project/vllm/pull/62996)
  [ROCm][Tests] Un-skip AITER MXFP4 padding-matrix and token-padding tests (#62996)
  _Files: `tests/kernels/moe/test_modular_kernel_combinations.py`_
- **2026-10-29** [`d04560f56b`](https://github.com/vllm-project/vllm/commit/d04560f56b) [#64322](https://github.com/vllm-project/vllm/pull/64322)
  [Doc] DeepSeek-V4-Pro: add MI355X AgentX source profiles (#64322)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4-Pro.yaml`_
- **2026-10-29** [`de83f55848`](https://github.com/vllm-project/vllm/commit/de83f55848) [#64532](https://github.com/vllm-project/vllm/pull/64532)
  [ROCm][DSv4.1] Lift the skinny-GEMM cap in the gfx942 draft lm_head test (#64532)
  _Files: `tests/kernels/models/amd/test_dsv41_gfx942_draft_lm_head.py`_
- **2026-10-29** [`8d4c96804b`](https://github.com/vllm-project/vllm/commit/8d4c96804b) [#64049](https://github.com/vllm-project/vllm/pull/64049)
  [CI] Bump Transformers version to 5.21.1 (#64049)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+6 more__
- **2026-10-29** [`f1266682b2`](https://github.com/vllm-project/vllm/commit/f1266682b2) [#64423](https://github.com/vllm-project/vllm/pull/64423)
  [Bugfix][ROCm][DBO] Create hipBLASLt handles in microbatch threads before graph capture (#64423)
  _Files: `vllm/v1/worker/gpu/ubatch_utils.py`_
- **2026-10-29** [`e5571b97fc`](https://github.com/vllm-project/vllm/commit/e5571b97fc) [#64169](https://github.com/vllm-project/vllm/pull/64169)
  [Mistral] Use get_grammar_for_chat_request in MistralParser and require mistral-common 1.13.0 (#64169)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+9 more__
- **2026-10-29** [`fb7def9ef9`](https://github.com/vllm-project/vllm/commit/fb7def9ef9) [#64008](https://github.com/vllm-project/vllm/pull/64008)
  [ROCm][Perf] Reuse compiled FlyDSL host launchers (#64008)
  _Files: `vllm/models/deepseek_v4/amd/mono/runner.py`, `vllm/models/deepseek_v41/amd/mono/runner.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/attention/kda.py`, `vllm/models/kimi_k3/amd/specialized_decode/mono/layer.py` _+3 more__
- **2026-10-29** [`ee1056b317`](https://github.com/vllm-project/vllm/commit/ee1056b317) [#64474](https://github.com/vllm-project/vllm/pull/64474)
  [Doc] Fix MiniMax-M3 docstring cross-references (#64474)
  _Files: `vllm/models/minimax_m3/amd/mono/kernels/index_score.py`, `vllm/models/minimax_m3/amd/mono/runner.py`, `vllm/models/minimax_m3/amd/ops/nvfp4_index_prefill/kernel_shared.py`_
- **2026-10-29** [`a0e31b7353`](https://github.com/vllm-project/vllm/commit/a0e31b7353) [#63053](https://github.com/vllm-project/vllm/pull/63053)
  [CI][ROCM][Bug] Elastic DP doesn't work with AITER-on (#63053)
  _Files: `vllm/distributed/device_communicators/cuda_communicator.py`, `vllm/distributed/elastic_ep/elastic_execute.py`_
- **2026-10-29** [`fa3b9d1377`](https://github.com/vllm-project/vllm/commit/fa3b9d1377) [#52838](https://github.com/vllm-project/vllm/pull/52838)
  [Bugfix][AMD] A GPU-CPU KV transfer fault in OffloadingConnector takes the engine down instead of degrading the cache. (#52838)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker_metadata.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py` _+7 more__
- **2026-10-29** [`abaec97b42`](https://github.com/vllm-project/vllm/commit/abaec97b42) [#63179](https://github.com/vllm-project/vllm/pull/63179)
  [ROCm] Fuse tiny-M MXFP8 quant into the block32 GEMM; guard lm_head skinny-GEMM by weight size (#63179)
  _Files: `tests/kernels/quantization/test_rocm_mxfp8_linear.py`, `tests/model_executor/layers/test_lmhead_skinny_gemm_guard.py`, `vllm/envs.py`, `vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py` _+2 more__
- **2026-10-29** [`1aea05364f`](https://github.com/vllm-project/vllm/commit/1aea05364f) [#60477](https://github.com/vllm-project/vllm/pull/60477)
  [Bugfix] DSA: all-reduce partial hidden_states before PP send (#60477)
  _Files: `tests/models/deepseek_v32/test_sequence_parallel.py`, `vllm/models/deepseek_v32/amd/model.py`, `vllm/models/deepseek_v32/nvidia/model.py`, `vllm/models/dots3_note/nvidia/model.py`_
- **2026-10-29** [`7ab756940a`](https://github.com/vllm-project/vllm/commit/7ab756940a) [#63047](https://github.com/vllm-project/vllm/pull/63047)
  [Bugfix][DSv4.1] Budget prefill memory the startup profile misses (#63047)
  _Files: `tests/distributed/test_engram_dp_shard.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/models/deepseek_v41/amd/model.py` _+2 more__
- **2026-10-29** [`66875d3127`](https://github.com/vllm-project/vllm/commit/66875d3127) [#64356](https://github.com/vllm-project/vllm/pull/64356)
  [Spec Decode] Batch-sharded draft logits refactor (#64356)
  _Files: `tests/kernels/models/amd/test_dsv41_gfx942_fused_markov.py`, `tests/v1/spec_decode/test_dspark_topk.py`, `tests/v1/spec_decode/test_lilicorr.py`, `tests/v1/spec_decode/test_rejection_sampler_utils.py` _+18 more__
- **2026-10-29** [`bcbcd02e53`](https://github.com/vllm-project/vllm/commit/bcbcd02e53) [#63915](https://github.com/vllm-project/vllm/pull/63915)
  [ROCm][Perf] Fuse MXFP8 activation quant into the 1x32 dot_scaled linear for M <= 16 (#63915)
  _Files: `tests/kernels/quantization/test_rocm_mxfp8_linear.py`, `vllm/model_executor/kernels/linear/mxfp8/rocm_native.py`_
- **2026-10-29** [`d6fbd94782`](https://github.com/vllm-project/vllm/commit/d6fbd94782) [#51012](https://github.com/vllm-project/vllm/pull/51012)
  [Models] Deprecate `torch.compile` for Qwen3.5 models (#51012)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/lm_eval.yaml` _+25 more__
- **2026-10-29** [`a6c3635e36`](https://github.com/vllm-project/vllm/commit/a6c3635e36) [#64064](https://github.com/vllm-project/vllm/pull/64064)
  [ROCm][Model] Enable ROCm AITER unified attention for MiMo-V2.6 (#64064)
  _Files: `.buildkite/test-amd.yaml`, `benchmarks/kernels/benchmark_reshape_and_cache_flash.py`, `csrc/cache_kernels.cu`, `tests/kernels/attention/test_cache.py` _+6 more__
- **2026-10-29** [`45fd60d4d5`](https://github.com/vllm-project/vllm/commit/45fd60d4d5) [#61529](https://github.com/vllm-project/vllm/pull/61529)
  [ROCm][Qwen4Exp] Enable fp8 KV and indexer caches on the AMD QSA path (#61529)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/qwen4_exp/test_qsa_amd.py`, `tests/models/qwen4_exp/test_qsa_prepare_amd.py`, `tests/models/qwen4_exp/test_qsa_reference.py` _+6 more__
- **2026-10-29** [`b7f0dda503`](https://github.com/vllm-project/vllm/commit/b7f0dda503) [#62990](https://github.com/vllm-project/vllm/pull/62990)
  [ROCm][Kimi-K3] Allow DSpark adaptive verification with DCP on ROCM_AITER_MLA (#62990)
  _Files: `tests/v1/attention/test_rocm_aiter_mla_dcp_cprr_numerics.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-10-28** [`ce775739e9`](https://github.com/vllm-project/vllm/commit/ce775739e9) [#64377](https://github.com/vllm-project/vllm/pull/64377)
  [CI][ROCm] Drop nvidia-cuda-cccl from the ROCm test lockfile again (#64377)
  _Files: `requirements/test/rocm.txt`_
- **2026-10-28** [`a3ce9ceefe`](https://github.com/vllm-project/vllm/commit/a3ce9ceefe) [#64010](https://github.com/vllm-project/vllm/pull/64010)
  [CI] Re-enable disabled jobs whose installs are already locked (#64010)
  _Files: `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `tools/pre_commit/test_tethering_allowlist.txt`_
- **2026-10-28** [`7b87062308`](https://github.com/vllm-project/vllm/commit/7b87062308) [#61699](https://github.com/vllm-project/vllm/pull/61699)
  [Bugfix][Spec Decode] Honor standalone draft load config (#61699)
  _Files: `requirements/test/rocm.txt`, `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/v1/spec_decode/draft_model.py`, `vllm/v1/worker/gpu/spec_decode/extract_hidden_states.py` _+1 more__
- **2026-10-28** [`892cb19816`](https://github.com/vllm-project/vllm/commit/892cb19816) [#63042](https://github.com/vllm-project/vllm/pull/63042)
  [MyPy][8/N] Enable strict checking for model test subdirectories (#63042)
  _Files: `tests/models/inkling/test_contract_validation.py`, `tests/models/inkling/test_mtp_input_fusion.py`, `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `tests/models/kimi_k3/test_amd_attn_res.py` _+18 more__
- **2026-10-28** [`8321d1119b`](https://github.com/vllm-project/vllm/commit/8321d1119b) [#64302](https://github.com/vllm-project/vllm/pull/64302)
  [CI] Exclude nvidia-cuda-cccl from the ROCm test lockfile (#64302)
  _Files: `.pre-commit-config.yaml`, `requirements/test/rocm.txt`_
- **2026-10-28** [`af4db2a675`](https://github.com/vllm-project/vllm/commit/af4db2a675) [#61457](https://github.com/vllm-project/vllm/pull/61457)
  [Quantization] Enable per-layer fused shared expert selection (#61457)
  _Files: `tests/kernels/moe/test_fp8_tp_loading.py`, `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/model_executor/model_loader/test_reload.py`, `tests/models/test_deepseek_v4_vl_rocm.py` _+33 more__
- **2026-10-28** [`df028dffa5`](https://github.com/vllm-project/vllm/commit/df028dffa5) [#64063](https://github.com/vllm-project/vllm/pull/64063)
  Ship mamba SSU and Helion tuned kernel configs in wheel package_data (#64063)
  _Files: `setup.py`_
- **2026-10-28** [`5ea8301982`](https://github.com/vllm-project/vllm/commit/5ea8301982) [#62077](https://github.com/vllm-project/vllm/pull/62077)
  [CI] Move Attention, Quantization and MoE kernel tests and their AMD mirrors from fixed to automatic shards (#62077)
  _Files: `.buildkite/test_areas/kernels.yaml`_
- **2026-10-28** [`1cb31be702`](https://github.com/vllm-project/vllm/commit/1cb31be702) [#63637](https://github.com/vllm-project/vllm/pull/63637)
  [ROCm][MiniMax-M3.1] Fuse MXFP8 activation quant into the Gemma input_layernorm for qkv_proj (#63637)
  _Files: `tests/fusion/test_quant_activation_contract.py`, `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/model_executor/kernels/linear/mxfp8/rocm_native.py`, `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py` _+3 more__
- **2026-10-28** [`b71c1d5f14`](https://github.com/vllm-project/vllm/commit/b71c1d5f14) [#64158](https://github.com/vllm-project/vllm/pull/64158)
  [ROCm][Bugfix][Kimi-K3] Build the folded q_b_proj / W_UK weight on the root model (#64158)
  _Files: `tests/models/kimi_k3/test_amd_qb_uk_fold.py`, `vllm/models/kimi_k3/amd/model.py`_
- **2026-10-28** [`11a3634094`](https://github.com/vllm-project/vllm/commit/11a3634094) [#62513](https://github.com/vllm-project/vllm/pull/62513)
  [CI] Shard Humming B200/H100 evals and two entrypoints AMD mirrors automatically (#62513)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/humming/config-h100-shard-0.txt`, `tests/evals/gsm8k/configs/humming/config-h100-shard-1.txt` _+2 more__
- **2026-10-27** [`bb7ea479c6`](https://github.com/vllm-project/vllm/commit/bb7ea479c6) [#63409](https://github.com/vllm-project/vllm/pull/63409)
  [ROCm][Bugfix][Kimi-K3] Pass zero positions to the fused MLA decode q-prep kernel (#63409)
  _Files: `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/mla.py`_
- **2026-10-27** [`274a5e19a1`](https://github.com/vllm-project/vllm/commit/274a5e19a1) [#63155](https://github.com/vllm-project/vllm/pull/63155)
  [Perf][DSv4.1] Capture the decoder replay graphs on the model graphs' stream (#63155)
  _Files: `tests/models/test_deepseek_v41_decoder_replay_layers.py`, `tests/v1/cudagraph/test_breakable_cudagraph.py`, `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/distributed/parallel_state.py` _+9 more__
- **2026-10-27** [`9af236a332`](https://github.com/vllm-project/vllm/commit/9af236a332) [#63735](https://github.com/vllm-project/vllm/pull/63735)
  [Bugfix][Perf][ROCm] RDNA launch config for kernel_paged_attention_2d (#63735)
  _Files: `tests/kernels/attention/test_prefix_prefill.py`, `vllm/v1/attention/ops/chunked_prefill_paged_decode.py`_
- **2026-10-27** [`d0c20bb840`](https://github.com/vllm-project/vllm/commit/d0c20bb840) [#61863](https://github.com/vllm-project/vllm/pull/61863)
  [ROCm][Perf][Attention] Keep the bf16 attention prefill when FP8 padding would double the heads (#61863)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_fp8_prefill.py`, `tests/kernels/attention/test_rocm_aiter_mla_head_padding.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-10-27** [`eaf1627c01`](https://github.com/vllm-project/vllm/commit/eaf1627c01) [#52970](https://github.com/vllm-project/vllm/pull/52970)
  [ROCm][aiter] officially supporting aiter Triton kernels+dsv4 on RDNA3 (#52970)
  _Files: `vllm/_aiter_ops.py`, `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`, `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py` _+4 more__
- **2026-10-27** [`94ad4dfbae`](https://github.com/vllm-project/vllm/commit/94ad4dfbae) [#60710](https://github.com/vllm-project/vllm/pull/60710)
  [ROCm][Perf] W4A16: opt-in dense weight cache for RDNA hybrid prefill (#60710)
  _Files: `tests/kernels/quantization/test_rdna_hybrid_w4a16.py`, `vllm/config/kernel.py`, `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`_
- **2026-10-27** [`6aa70c4bec`](https://github.com/vllm-project/vllm/commit/6aa70c4bec) [#60110](https://github.com/vllm-project/vllm/pull/60110)
  [ROCm][Perf][Kimi-K3] Fold q_b_proj and W_UK into one GEMM for the MLA decode query (#60110)
  _Files: `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `tests/models/kimi_k3/test_amd_qb_uk_fold.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/mla.py`_
- **2026-10-27** [`889d635dd7`](https://github.com/vllm-project/vllm/commit/889d635dd7) [#53166](https://github.com/vllm-project/vllm/pull/53166)
  [Perf][ROCm][Attention] Fuse Kimi-K3 MLA chunked-context gather on AITER (#53166)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_prefill_fusions.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-10-27** [`228b1e3d23`](https://github.com/vllm-project/vllm/commit/228b1e3d23) [#59668](https://github.com/vllm-project/vllm/pull/59668)
  [ROCm][DSV4.1][Perf] Single-launch DSA decode candidate mask (#59668)
  _Files: `tests/kernels/attention/test_rocm_aiter_candidate_mask.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-10-27** [`83909ad84b`](https://github.com/vllm-project/vllm/commit/83909ad84b) [#57015](https://github.com/vllm-project/vllm/pull/57015)
  [ROCm][Perf] W4A16: widen skinny GEMM LDS activation loads to b128 (#57015)
  _Files: `csrc/rocm/skinny_gemms_int4.cu`_
- **2026-10-27** [`e7fa26d5c8`](https://github.com/vllm-project/vllm/commit/e7fa26d5c8) [#63996](https://github.com/vllm-project/vllm/pull/63996)
  [Model][Spec Decode] Refactor #41834 with useful improvements (#63996)
  _Files: `tests/kernels/mhc/test_mhc_kernels.py`, `tests/v1/spec_decode/test_eagle.py`, `tests/v1/spec_decode/test_mtp.py`, `vllm/model_executor/kernels/mhc/tilelang.py` _+10 more__
- **2026-10-27** [`f8f7634cb4`](https://github.com/vllm-project/vllm/commit/f8f7634cb4) [#63342](https://github.com/vllm-project/vllm/pull/63342)
  [ROCm][Perf][Kimi-K3] Use block_m=128 for the fused KDA prefill conv1d (#63342)
  _Files: `tests/models/kimi_k3/test_amd_kda_fused_conv1d.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/kda_metadata.py`_
- **2026-10-27** [`8d88bc5d81`](https://github.com/vllm-project/vllm/commit/8d88bc5d81) [#60154](https://github.com/vllm-project/vllm/pull/60154)
  [ROCm][DSv4/4.1] Fuse inverse RoPE and MXFP8 quant into the aiter sparse MLA and sparse MLA gating changes (#60154)
  _Files: `tests/v1/attention/test_rocm_aiter_triton_sparse_mla.py`, `vllm/_aiter_ops.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v41/amd/rocm.py`_
- **2026-10-27** [`5f1a564181`](https://github.com/vllm-project/vllm/commit/5f1a564181) [#63726](https://github.com/vllm-project/vllm/pull/63726)
  [Recipe][AMD] Refresh Kimi-K3 PD configurations (#63726)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-27** [`de58886274`](https://github.com/vllm-project/vllm/commit/de58886274) [#62120](https://github.com/vllm-project/vllm/pull/62120)
  [CI] Move B200 Kernels and MoE Refactor evals from manual to automatic shards (#62120)
  _Files: `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/moe-refactor/config-b200-shard-0.txt`, `tests/evals/gsm8k/configs/moe-refactor/config-b200-shard-1.txt` _+8 more__
- **2026-10-27** [`eb5e8d1cc8`](https://github.com/vllm-project/vllm/commit/eb5e8d1cc8) [#62537](https://github.com/vllm-project/vllm/pull/62537)
  [CI] Move L4 Distributed Models and LoRA TP and their AMD mirrors from fixed to automatic shards (#62537)
  _Files: `.buildkite/test_areas/lora.yaml`, `.buildkite/test_areas/models_distributed.yaml`_
- **2026-10-27** [`659defd662`](https://github.com/vllm-project/vllm/commit/659defd662) [#61904](https://github.com/vllm-project/vllm/pull/61904)
  [CI] Shard the AMD mirrors of Basic Models (Other) and PCP automatically (#61904)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/models_basic.yaml`_
- **2026-10-27** [`f62e80ff04`](https://github.com/vllm-project/vllm/commit/f62e80ff04) [#63907](https://github.com/vllm-project/vllm/pull/63907)
  [CI] Enroll 4 steps and 2 AMD mirrors in automatic sharding (#63907)
  _Files: `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_multimodal.yaml`, `.buildkite/test_areas/rust_frontend.yaml`_
- **2026-10-27** [`7c713621f3`](https://github.com/vllm-project/vllm/commit/7c713621f3) [#63850](https://github.com/vllm-project/vllm/pull/63850)
  [CI][ROCm] Preflight idle-GPU check in test_pp_cudagraph (#63850)
  _Files: `tests/distributed/test_pp_cudagraph.py`_
- **2026-10-27** [`5314c58281`](https://github.com/vllm-project/vllm/commit/5314c58281) [#63332](https://github.com/vllm-project/vllm/pull/63332)
  [ROCm][Recipe] Qwen3.8-Flash-Next: add MI355X Quark MXFP4 variant (TP1/TP2) (#63332)
  _Files: `recipes/models/Qwen/Qwen3.8-Flash-Next.yaml`_
- **2026-10-27** [`5c1eb11cb3`](https://github.com/vllm-project/vllm/commit/5c1eb11cb3) [#60234](https://github.com/vllm-project/vllm/pull/60234)
  [Bugfix] Allow pipeline parallelism for Qwen4Exp PLE models and their MTP drafter (#60234)
  _Files: `tests/models/qwen4_exp/test_config.py`, `tests/v1/core/test_kv_cache_planning.py`, `vllm/model_executor/models/config.py`, `vllm/models/qwen4_exp/amd/model.py` _+6 more__
- **2026-10-27** [`6fe3d447ac`](https://github.com/vllm-project/vllm/commit/6fe3d447ac) [#62141](https://github.com/vllm-project/vllm/pull/62141)
  [CI][AMD] Mirror ReplaySSM, MiniMax-M3 attention kernels and Kimi K3 prefix cache on MI355 (#62141)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/models_basic.yaml` _+4 more__
- **2026-10-27** [`3d81a510f9`](https://github.com/vllm-project/vllm/commit/3d81a510f9) [#48989](https://github.com/vllm-project/vllm/pull/48989)
  [ROCm] DeepSeek-V4-Pro PD Disaggregation through MORI IO KV Connector on AMD GPUs (#48989)
  _Files: `.buildkite/amd-disagg/models.yaml`, `.buildkite/amd-disagg/pipeline-disagg.yaml`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout.py`_
- **2026-10-27** [`1e10a92d1d`](https://github.com/vllm-project/vllm/commit/1e10a92d1d) [#63833](https://github.com/vllm-project/vllm/pull/63833)
  [Bugfix][ROCm] Wait on per-slot events in packed NCCL consumer (#63833)
  _Files: `vllm/distributed/weight_transfer/packed_tensor.py`_
- **2026-10-27** [`9b8944f500`](https://github.com/vllm-project/vllm/commit/9b8944f500) [#63868](https://github.com/vllm-project/vllm/pull/63868)
  [Docs][Recipe] Align MiniMax-M3 MI355X AgentX monokernel profile (#63868)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`_
- **2026-10-27** [`ed1a730795`](https://github.com/vllm-project/vllm/commit/ed1a730795) [#63689](https://github.com/vllm-project/vllm/pull/63689)
  [Bugfix][ROCm][DSv4] Give zero and subnormal mono MXFP8 groups vLLM's scale code (#63689)
  _Files: `vllm/models/deepseek_v4/amd/mono/attention/device.py`, `vllm/models/deepseek_v4/amd/mono/stages/moe.py`, `vllm/models/deepseek_v41/amd/mono/attention/device.py`, `vllm/models/deepseek_v41/amd/mono/stages/moe.py`_
- **2026-10-26** [`26cbb47d48`](https://github.com/vllm-project/vllm/commit/26cbb47d48) [#63554](https://github.com/vllm-project/vllm/pull/63554)
  [Spec Decode][Sampling] Batch-sharded draft logits (#63554)
  _Files: `tests/kernels/models/amd/test_dsv41_gfx942_fused_markov.py`, `tests/v1/spec_decode/test_dspark_topk.py`, `tests/v1/spec_decode/test_lilicorr.py`, `tests/v1/spec_decode/test_rejection_sampler_utils.py` _+15 more__
- **2026-10-26** [`967c39f89e`](https://github.com/vllm-project/vllm/commit/967c39f89e) [#63408](https://github.com/vllm-project/vllm/pull/63408)
  [CI] List one test path per line in Buildkite pytest commands to avoid merge conflicts (#63408)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/intel_jobs/basic_correctness_intel.yaml`, `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/entrypoints_intel.yaml` _+25 more__
- **2026-10-26** [`70d67f19dc`](https://github.com/vllm-project/vllm/commit/70d67f19dc) [#63828](https://github.com/vllm-project/vllm/pull/63828)
  [ROCm][CI] Release checkpoint page cache between language generation … (#63828)
  _Files: `tests/models/language/generation/conftest.py`_
- **2026-10-26** [`442f3d989e`](https://github.com/vllm-project/vllm/commit/442f3d989e) [#63557](https://github.com/vllm-project/vllm/pull/63557)
  [CI][ROCm] Take NIXL PD accuracy side-channel ports from below the ephemeral range (#63557)
  _Files: `tests/v1/kv_connector/rocm_pd_accuracy_utils.py`_
- **2026-10-26** [`ad42b456f9`](https://github.com/vllm-project/vllm/commit/ad42b456f9) [#63453](https://github.com/vllm-project/vllm/pull/63453)
  [CI][ROCm] Take MoRIIO P/D test port blocks from below the ephemeral range (#63453)
  _Files: `tests/v1/kv_connector/moriio_integration/test_write_dummy_e2e_rocm.py`_
- **2026-10-26** [`088e6a4d68`](https://github.com/vllm-project/vllm/commit/088e6a4d68) [#63559](https://github.com/vllm-project/vllm/pull/63559)
  [CI][ROCm] Skip the AITER MoE garbage-rows test for fp8 per-tensor until the AITER fix (#63559)
  _Files: `tests/kernels/moe/test_modular_kernel_combinations.py`_
- **2026-10-26** [`94b35f3780`](https://github.com/vllm-project/vllm/commit/94b35f3780) [#63558](https://github.com/vllm-project/vllm/pull/63558)
  [Bugfix][ROCm] Keep the AITER GDN decode fast path off for the DS conv-state layout (#63558)
  _Files: `tests/kernels/mamba/test_gdn_rocm_layout_dispatch.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-10-26** [`9744ada582`](https://github.com/vllm-project/vllm/commit/9744ada582) [#63576](https://github.com/vllm-project/vllm/pull/63576)
  [Bugfix][ROCm][DSv4.1] Await krdy before K2's combine reads klen in index-source launches (#63576)
  _Files: `vllm/models/deepseek_v41/amd/mono/attention/back.py`_
- **2026-10-26** [`536854bf10`](https://github.com/vllm-project/vllm/commit/536854bf10) [#59255](https://github.com/vllm-project/vllm/pull/59255)
  [ROCm] Enable expert parallelism for AITER Triton W4A16 MoE (#59255)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/kernels/moe/test_topk_softplus_sqrt.py`, `tests/models/quantization/test_gpt_oss.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a16_moe.py` _+1 more__
- **2026-10-26** [`df8b5d3781`](https://github.com/vllm-project/vllm/commit/df8b5d3781) [#63760](https://github.com/vllm-project/vllm/pull/63760)
  [ROCm][CI] Raise MI300 Core Operation Kernels timeout to 90 min (#63760)
  _Files: `.buildkite/test_areas/kernels.yaml`_
- **2026-10-26** [`50a184f435`](https://github.com/vllm-project/vllm/commit/50a184f435) [#63256](https://github.com/vllm-project/vllm/pull/63256)
  [RL] Declare weight ownership and layout on ParamMeta (#63256)
  _Files: `docs/training/weight_transfer/README.md`, `docs/training/weight_transfer/base.md`, `docs/training/weight_transfer/ipc.md`, `docs/training/weight_transfer/m2n.md` _+18 more__
- **2026-10-26** [`d0d681e40d`](https://github.com/vllm-project/vllm/commit/d0d681e40d) [#63669](https://github.com/vllm-project/vllm/pull/63669)
  [ROCm][Perf] Make MXFP4 the default indexer K cache dtype for DeepSeek-V4 (#63669)
  _Files: `vllm/config/attention.py`, `vllm/platforms/rocm.py`_
- **2026-10-26** [`c3941c032d`](https://github.com/vllm-project/vllm/commit/c3941c032d) [#63099](https://github.com/vllm-project/vllm/pull/63099)
  [Bugfix][ROCm] Match the DeepSeek-V4.1 FP8 config in the shared-expert FSE compatibility check (#63099)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `vllm/model_executor/layers/quantization/utils/config_utils.py`_
- **2026-10-26** [`9bea474d65`](https://github.com/vllm-project/vllm/commit/9bea474d65) [#59478](https://github.com/vllm-project/vllm/pull/59478)
  [ROCm][Perf] Use AITER FlyDSL INT4 QuickReduce when INT4 QuickReduce is selected (#59478)
  _Files: `tests/distributed/test_aiter_rms_fallback.py`, `tests/distributed/test_quick_all_reduce.py`, `tests/distributed/test_rocm_quick_reduce.py`, `vllm/_aiter_ops.py` _+1 more__
- **2026-10-26** [`ae3bc684e0`](https://github.com/vllm-project/vllm/commit/ae3bc684e0) [#63665](https://github.com/vllm-project/vllm/pull/63665)
  [Doc][ROCm] Update DeepSeek-V4.1-Flash MI355X AgentX scheduling profiles (#63665)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-10-26** [`2f34dce583`](https://github.com/vllm-project/vllm/commit/2f34dce583) [#63657](https://github.com/vllm-project/vllm/pull/63657)
  [Doc][ROCm] Update Kimi-K3 MI355X AgentX scheduling cells (#63657)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-26** [`00b6c4c565`](https://github.com/vllm-project/vllm/commit/00b6c4c565) [#59774](https://github.com/vllm-project/vllm/pull/59774)
  [ROCm] Octave KV (`ROCM_OCTAVE`): native 3-bit KV cache backend for AMD GPUs (#59774)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `CMakeLists.txt`, `benchmarks/attention_benchmarks/benchmark.py` _+26 more__
- **2026-10-26** [`0f6b261910`](https://github.com/vllm-project/vllm/commit/0f6b261910) [#61879](https://github.com/vllm-project/vllm/pull/61879)
  [Model] Add Muse Spark Open support (#61879)
  _Files: `benchmarks/kernels/benchmark_muse_spark_qknorm_rope_kv_insert.py`, `tests/distributed/test_comm_ops.py`, `tests/kernels/core/test_muse_spark_norms.py`, `tests/kernels/moe/muse_spark_utils.py` _+46 more__

## Attention  (65 commits)

- **2026-11-02** [`45fc9fd048`](https://github.com/vllm-project/vllm/commit/45fc9fd048) [#64984](https://github.com/vllm-project/vllm/pull/64984)
  [Bugfix][MM] Keep FlashInfer cu_seqlens halves aligned in Qwen3-VL encoder CUDA graph replay (#64984)
  _Files: `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/model_executor/models/qwen3_vl.py`_
- **2026-11-02** [`3b6eeb0606`](https://github.com/vllm-project/vllm/commit/3b6eeb0606) [#64759](https://github.com/vllm-project/vllm/pull/64759)
  [Bugfix][Kimi-K3] Pin FlashKDA and FlashMLA with NaN fixes (#64759)
  _Files: `cmake/external_projects/flashkda.cmake`, `cmake/external_projects/flashmla.cmake`_
- **2026-11-02** [`6044ab0609`](https://github.com/vllm-project/vllm/commit/6044ab0609) [#64076](https://github.com/vllm-project/vllm/pull/64076)
  [Refactor] Remove dead code multiple places (#64076)
  _Files: `tests/v1/core/test_async_scheduler.py`, `vllm/v1/attention/backends/cpu_attn.py`, `vllm/v1/attention/backends/flashinfer.py`, `vllm/v1/attention/backends/turboquant_attn.py` _+7 more__
- **2026-11-02** [`01b6a05b7b`](https://github.com/vllm-project/vllm/commit/01b6a05b7b) [#58618](https://github.com/vllm-project/vllm/pull/58618)
  [Bugfix][KV Offload] Anchor the partial-tail lookup on the full-attention prefix (#58618)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-11-02** [`860da3dafd`](https://github.com/vllm-project/vllm/commit/860da3dafd) [#56492](https://github.com/vllm-project/vllm/pull/56492)
  [Core] Extensible KV cache (#56492)
  _Files: `.buildkite/lm-eval-harness/test_lm_eval_correctness.py`, `tests/compile/fullgraph/test_full_graph.py`, `tests/conftest.py`, `tests/distributed/test_pp_cudagraph.py` _+52 more__
- **2026-11-02** [`7fc467825d`](https://github.com/vllm-project/vllm/commit/7fc467825d) [#65044](https://github.com/vllm-project/vllm/pull/65044)
  [Doc] Move the Ascend content of the recipes to vllm-ascend overlays (#65044)
  _Files: `.agents/skills/model-recipes/SKILL.md`, `recipes/README.md`, `recipes/models/Qwen/Qwen3-30B-A3B.yaml`, `recipes/models/Qwen/Qwen3.5-397B-A17B.yaml` _+7 more__
- **2026-11-02** [`bc09e63d79`](https://github.com/vllm-project/vllm/commit/bc09e63d79) [#61267](https://github.com/vllm-project/vllm/pull/61267)
  [Bugfix][LoRA] respect `attention_k_eq_v=True` QKK LoRA layers (#61267)
  _Files: `tests/lora/test_lora_manager.py`, `vllm/lora/model_manager.py`, `vllm/model_executor/models/gemma4.py`_
- **2026-11-02** [`23b8984195`](https://github.com/vllm-project/vllm/commit/23b8984195) [#63232](https://github.com/vllm-project/vllm/pull/63232)
  [Perf][FlashAttention] FA4: pass no FP8 descale for a unit per-tensor scale (#63232)
  _Files: `tests/v1/attention/test_attention_backends.py`, `vllm/v1/attention/backends/flash_attn.py`_
- **2026-11-02** [`dfe4a3025d`](https://github.com/vllm-project/vllm/commit/dfe4a3025d) [#64944](https://github.com/vllm-project/vllm/pull/64944)
  [Model] Nemotron-3.5-Transcribe: pack the audio tower's valid frames for MMEncoderAttention (#64944)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_nemotron3_5_transcribe.py`, `vllm/model_executor/models/nemotron3_5_transcribe_audio.py`_
- **2026-11-02** [`72a340466f`](https://github.com/vllm-project/vllm/commit/72a340466f) [#60543](https://github.com/vllm-project/vllm/pull/60543)
  [Bugfix][DSv4.1] Autotune the sparse indexer's wq_b GEMM (#60543)
  _Files: `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/models/deepseek_v41/attention.py`_
- **2026-11-01** [`8530a778f7`](https://github.com/vllm-project/vllm/commit/8530a778f7) [#56155](https://github.com/vllm-project/vllm/pull/56155)
  [Core][Attention] Resolve per-layer KV dtype in attention runtime (#56155)
  _Files: `tests/v1/attention/test_attention_backends.py`, `tests/v1/core/test_kv_cache_utils.py`, `vllm/model_executor/layers/attention/attention.py`, `vllm/model_executor/layers/quantization/base_config.py` _+3 more__
- **2026-11-01** [`3a90cc6fd0`](https://github.com/vllm-project/vllm/commit/3a90cc6fd0) [#64910](https://github.com/vllm-project/vllm/pull/64910)
  [Doc] MiniMax-M3.1-Flash: update the GB300 AgentX presets (#64910)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-11-01** [`a906122246`](https://github.com/vllm-project/vllm/commit/a906122246) [#64909](https://github.com/vllm-project/vllm/pull/64909)
  [Doc] MiniMax-M3.1-Flash: update the GB200 AgentX presets (#64909)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-10-31** [`78161c28da`](https://github.com/vllm-project/vllm/commit/78161c28da) [#54399](https://github.com/vllm-project/vllm/pull/54399)
  [Bugfix][Model] Fix CohereASR FP16 attention bias dtype (#54399)
  _Files: `tests/models/multimodal/test_cohere_asr.py`, `vllm/model_executor/models/cohere_asr.py`_
- **2026-10-31** [`54beee831b`](https://github.com/vllm-project/vllm/commit/54beee831b) [#62192](https://github.com/vllm-project/vllm/pull/62192)
  [Kernel] Batch invariance: pin FlashInfer FP8 bmm and W4A16 NVFP4 kernels (#62192)
  _Files: `tests/kernels/quantization/test_nvfp4_kernel_selection.py`, `tests/v1/determinism/test_cutlass_batch_invariance.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/utils/flashinfer.py`_
- **2026-10-31** [`4aba9bf3a4`](https://github.com/vllm-project/vllm/commit/4aba9bf3a4) [#64338](https://github.com/vllm-project/vllm/pull/64338)
  [Bugfix] Flashinfer attention warmup deadlock under PP>1 (#64338)
  _Files: `tests/model_executor/test_attention_warmup.py`, `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-10-31** [`e5196e2959`](https://github.com/vllm-project/vllm/commit/e5196e2959) [#62956](https://github.com/vllm-project/vllm/pull/62956)
  [Perf][glm5next] Add SM121 TP=2 skinny-GEMM plans for GLM-5.3-Flash (#62956)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/model_executor/kernels/linear/cute_dsl/skinny_gemm_plans.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/utils.py` _+2 more__
- **2026-10-31** [`602811546b`](https://github.com/vllm-project/vllm/commit/602811546b) [#61614](https://github.com/vllm-project/vllm/pull/61614)
  [Perf][GLM-5.3-Flash] Update FlashKDA pin, consume row-strided QKV directly (#61614)
  _Files: `cmake/external_projects/flashkda.cmake`, `vllm/models/glm5next/common/kda.py`_
- **2026-10-30** [`d90e35cffa`](https://github.com/vllm-project/vllm/commit/d90e35cffa) [#64821](https://github.com/vllm-project/vllm/pull/64821)
  [Doc] MiniMax-M3.1-Flash: add GB300 InferenceX AgentX presets (#64821)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-10-30** [`2f6f7861ba`](https://github.com/vllm-project/vllm/commit/2f6f7861ba) [#63761](https://github.com/vllm-project/vllm/pull/63761)
  [Bugfix] Fix int32 token offset overflows in Qwen3.5 attention and GDN prefill kernels (#63761)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/fla/test_chunk_int64_offsets.py`, `tests/kernels/fla/test_fla_layernorm_guard.py`, `tests/kernels/fla/test_fused_gdn_post_conv.py` _+8 more__
- **2026-10-30** [`913fccd118`](https://github.com/vllm-project/vllm/commit/913fccd118) [#46370](https://github.com/vllm-project/vllm/pull/46370)
  [Feature] Initial support for fault tolerant ep using scale-down (#46370)
  _Files: `.buildkite/test_areas/fault_tolerance.yaml`, `docs/serving/expert_parallel_deployment.md`, `tests/model_executor/model_loader/test_reload.py`, `tests/v1/engine/test_admission_control.py` _+33 more__
- **2026-10-30** [`4a8dc13adc`](https://github.com/vllm-project/vllm/commit/4a8dc13adc) [#64595](https://github.com/vllm-project/vllm/pull/64595)
  [CI] Enroll the remaining Compile, PyTorch, CUDA and ABI jobs in automatic sharding (29 jobs) (#64595)
  _Files: `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/jit_monitor.yaml` _+2 more__
- **2026-10-30** [`53624fc952`](https://github.com/vllm-project/vllm/commit/53624fc952) [#61971](https://github.com/vllm-project/vllm/pull/61971)
  [Perf][DSv4.1] Bump FlashMLA to pass int64 positions to MegaAttn (#61971)
  _Files: `benchmarks/kernels/benchmark_dsv41_mega_attn.py`, `cmake/external_projects/flashmla.cmake`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`_
- **2026-10-30** [`d14f72c7fe`](https://github.com/vllm-project/vllm/commit/d14f72c7fe) [#62424](https://github.com/vllm-project/vllm/pull/62424)
  [Rust Frontend] Add native GLM-5.3 / GLM-5.3-Flash chat rendering (#62424)
  _Files: `recipes/models/zai-org/GLM-5.3-Flash.yaml`, `recipes/models/zai-org/GLM-5.3.yaml`, `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/renderer/glm5_next/encoding.rs` _+14 more__
- **2026-10-30** [`a17e79abde`](https://github.com/vllm-project/vllm/commit/a17e79abde) [#64071](https://github.com/vllm-project/vllm/pull/64071)
  [EPD] Metadata-only image and video inputs for GLM-5.3-Flash (#64071)
  _Files: `tests/models/glm5next/test_epd_metadata.py`, `tests/models/multimodal/processing/test_glm5next.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/models/glm5next/common/multimodal.py`_
- **2026-10-29** [`98fc6da9d7`](https://github.com/vllm-project/vllm/commit/98fc6da9d7) [#59131](https://github.com/vllm-project/vllm/pull/59131)
  [Perf][DSv4.1] Gather the compressed KV once per KV-source group in prefill (#59131)
  _Files: `tests/v1/worker/test_workspace.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`, `vllm/v1/worker/workspace.py`_
- **2026-10-29** [`28dd46d791`](https://github.com/vllm-project/vllm/commit/28dd46d791) [#60103](https://github.com/vllm-project/vllm/pull/60103)
  [Perf][HiSparse] Fuse per-layer slot invalidation and shorten the all-resident resolver path (#60103)
  _Files: `csrc/hisparse_kernels.cu`, `csrc/ops.h`, `csrc/torch_bindings.cpp`, `tests/v1/attention/test_sparse_mla_backends.py` _+4 more__
- **2026-10-29** [`cebe109723`](https://github.com/vllm-project/vllm/commit/cebe109723) [#60229](https://github.com/vllm-project/vllm/pull/60229)
  [Spec Decode][GLM-5.3-Flash] Support adaptive verification (#60229)
  _Files: `tests/kernels/mamba/test_gdn_fused_mtp.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `tests/v1/attention/test_gdn_metadata_builder.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` _+4 more__
- **2026-10-29** [`fa1cf1d436`](https://github.com/vllm-project/vllm/commit/fa1cf1d436) [#64419](https://github.com/vllm-project/vllm/pull/64419)
  [Perf][GDN] Allocate GDN core output uninitialized, write FlashInfer prefill in place (#64419)
  _Files: `tests/kernels/mamba/test_gdn_forward_core_split.py`, `tests/kernels/mamba/test_gdn_fused_mtp.py`, `tests/kernels/mamba/test_gdn_prefill_flashinfer.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py` _+1 more__
- **2026-10-29** [`dbd49af222`](https://github.com/vllm-project/vllm/commit/dbd49af222) [#64111](https://github.com/vllm-project/vllm/pull/64111)
  [New Model] Add MiniMax-M3.1-Flash Model and Kernels (#64111)
- **2026-10-28** [`65ff14056a`](https://github.com/vllm-project/vllm/commit/65ff14056a) [#64238](https://github.com/vllm-project/vllm/pull/64238)
  [Bugfix][HiSparse] Fix compact KV row regression tests (#64238)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`_
- **2026-10-28** [`af8f27d5d7`](https://github.com/vllm-project/vllm/commit/af8f27d5d7) [#64259](https://github.com/vllm-project/vllm/pull/64259)
  [CI][Bugfix] Fit the MLA backend bf16 atol to a bf16 SDPA reference (#64259)
  _Files: `tests/v1/attention/test_mla_backends.py`_
- **2026-10-28** [`3a7552056c`](https://github.com/vllm-project/vllm/commit/3a7552056c) [#64283](https://github.com/vllm-project/vllm/pull/64283)
  [Doc] MiniMax-M3.1-Flash: add the GB200 AgentX presets (#64283)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-10-28** [`366beb2215`](https://github.com/vllm-project/vllm/commit/366beb2215) [#64284](https://github.com/vllm-project/vllm/pull/64284)
  [Doc] MiniMax-M3.1-Flash: add the GB300 AgentX presets (#64284)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-10-28** [`4da2a82a24`](https://github.com/vllm-project/vllm/commit/4da2a82a24) [#63791](https://github.com/vllm-project/vllm/pull/63791)
  [Bugfix][Attention] FlashInfer sparse MLA: launch at most 65535 tokens per trtllm-gen call  (#63791)
  _Files: `tests/v1/attention/test_flashinfer_sparse_mla_workspace.py`, `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse.py`_
- **2026-10-28** [`ee9ba37199`](https://github.com/vllm-project/vllm/commit/ee9ba37199) [#64282](https://github.com/vllm-project/vllm/pull/64282)
  [Model] Add Nemotron-3.5-Transcribe (#64282)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_nemotron3_5_transcribe.py`, `tests/models/registry.py`, `tests/v1/spec_decode/test_dflash2.py` _+11 more__
- **2026-10-28** [`ed6b8f4cd2`](https://github.com/vllm-project/vllm/commit/ed6b8f4cd2) [#63914](https://github.com/vllm-project/vllm/pull/63914)
  [Bugfix][DSv4.1] Keep the specialized decode's FlashInfer paths on newer FlashInfer (#63914)
  _Files: `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_numerics.py`, `vllm/models/deepseek_v41/nvidia/specialized_decode/AGENTS.md`, `vllm/models/deepseek_v41/nvidia/specialized_decode/__init__.py` _+2 more__
- **2026-10-28** [`317081fb6d`](https://github.com/vllm-project/vllm/commit/317081fb6d) [#62860](https://github.com/vllm-project/vllm/pull/62860)
  [Bugfix][DSA] Reserve the decode indexer logits in the memory profile (#62860)
  _Files: `tests/v1/attention/test_indexer_tp_row_shard.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-10-28** [`edad8b03c5`](https://github.com/vllm-project/vllm/commit/edad8b03c5) [#61294](https://github.com/vllm-project/vllm/pull/61294)
  [Bugfix] Merge supported KV cache layouts across pipeline stages instead of asserting they match (#61294)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/attention/backends/utils.py`_
- **2026-10-28** [`dbcf568821`](https://github.com/vllm-project/vllm/commit/dbcf568821) [#58305](https://github.com/vllm-project/vllm/pull/58305)
  [Perf][SM120][MLA] Use compact FP8 KV rows for NoPE models (#58305)
  _Files: `csrc/cache_kernels.cu`, `tests/kernels/attention/test_cache.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_sparse_mla_backends.py` _+7 more__
- **2026-10-28** [`458334f00f`](https://github.com/vllm-project/vllm/commit/458334f00f) [#63819](https://github.com/vllm-project/vllm/pull/63819)
  [MRV2][Spec Decode] Close DFlash/DSpark and adaptive-verification JIT warmup gaps (#63819)
  _Files: `tests/v1/spec_decode/test_acceptance_estimator.py`, `tests/v1/spec_decode/test_dflash_prepare_inputs.py`, `tests/v1/worker/test_gpu_warmup_blocks.py`, `tests/v1/worker/test_mixed_warmup_gate.py` _+3 more__
- **2026-10-28** [`ebaa812475`](https://github.com/vllm-project/vllm/commit/ebaa812475) [#61659](https://github.com/vllm-project/vllm/pull/61659)
  [Bugfix][HiSparse] Pad staged prefill KV to avoid a trtllm-gen out-of-bounds read (#61659)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/hisparse/runtime.py`_
- **2026-10-28** [`66f1d0fa16`](https://github.com/vllm-project/vllm/commit/66f1d0fa16) [#62739](https://github.com/vllm-project/vllm/pull/62739)
  [Bugfix][HiSparse] Read resident prefill rows by request state slot (#62739)
  _Files: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `tests/v1/attention/test_sparse_mla_backends.py`, `tests/v1/kv_connector/unit/test_hisparse_connector.py`, `vllm/v1/attention/backends/mla/index_group.py` _+3 more__
- **2026-10-27** [`8697bbae4c`](https://github.com/vllm-project/vllm/commit/8697bbae4c) [#59392](https://github.com/vllm-project/vllm/pull/59392)
  [Bugfix][Attention] Fix FlashInfer MLA DCP decode on ragged spec-decode batches (#59392)
  _Files: `tests/v1/attention/test_flashinfer_mla_dcp.py`, `vllm/v1/attention/backends/mla/flashinfer_mla.py`_
- **2026-10-27** [`7bf13a3db1`](https://github.com/vllm-project/vllm/commit/7bf13a3db1) [#64081](https://github.com/vllm-project/vllm/pull/64081)
  [CI][Test] Adjust TRT-LLM and GDN numerical tolerances for Rubin (#64081)
  _Files: `tests/kernels/attention/test_flashinfer_trtllm_attention.py`, `tests/kernels/fla/test_fused_gdn_post_conv.py`_
- **2026-10-27** [`70cb50dab2`](https://github.com/vllm-project/vllm/commit/70cb50dab2) [#62592](https://github.com/vllm-project/vllm/pull/62592)
  [Feature][HiSparse] Add a platform backend for device operations (#62592)
  _Files: `docs/design/hisparse.md`, `tests/test_config.py`, `tests/v1/attention/test_sparse_mla_backends.py`, `tests/v1/core/test_kv_cache_planning.py` _+13 more__
- **2026-10-27** [`a2ad4b74b9`](https://github.com/vllm-project/vllm/commit/a2ad4b74b9) [#62011](https://github.com/vllm-project/vllm/pull/62011)
  [Perf] Enable DeepGEMM sparse MQA logits on the FP8 indexer cache, DSv4.1 (#62011)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `vllm/config/attention.py`, `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py` _+4 more__
- **2026-10-27** [`bfa2a43345`](https://github.com/vllm-project/vllm/commit/bfa2a43345) [#64107](https://github.com/vllm-project/vllm/pull/64107)
  [CI] Fix stale NVFP4 decode test selector on DGX Spark (#64107)
  _Files: `.buildkite/test_areas/attention.yaml`_
- **2026-10-27** [`741584f8ca`](https://github.com/vllm-project/vllm/commit/741584f8ca) [#58744](https://github.com/vllm-project/vllm/pull/58744)
  [Bugfix][MLA] Gather nvfp4_ds_mla chunked-context KV with the NVFP4 kernel (#58744)
  _Files: `csrc/cache_kernels.cu`, `csrc/nvfp4_ds_mla_cache.h`, `csrc/nvfp4_ds_mla_cache_kernels.cu`, `csrc/ops.h` _+7 more__
- **2026-10-27** [`a75277a0a1`](https://github.com/vllm-project/vllm/commit/a75277a0a1) [#64108](https://github.com/vllm-project/vllm/pull/64108)
  [Doc] MiniMax-M3.1-Flash: add the B300 single-node AgentX presets (#64108)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-10-27** [`bf4b3b5cb8`](https://github.com/vllm-project/vllm/commit/bf4b3b5cb8) [#63973](https://github.com/vllm-project/vllm/pull/63973)
  [CI][CPU] Initialize DFlash test FC after loading weights (#63973)
  _Files: `tests/v1/spec_decode/test_dflash2.py`_
- **2026-10-27** [`a91a1d06b7`](https://github.com/vllm-project/vllm/commit/a91a1d06b7) [#62318](https://github.com/vllm-project/vllm/pull/62318)
  [Bugfix][Model] Qwen3.8-Flash-Next: load checkpoints with quantized q/k/v and a BF16 QSA indexer (#62318)
  _Files: `tests/models/qwen4_exp/test_config.py`, `vllm/models/qwen4_exp/nvidia/model.py`, `vllm/models/qwen4_exp/nvidia/qsa.py`_
- **2026-10-27** [`08b989da99`](https://github.com/vllm-project/vllm/commit/08b989da99) [#63063](https://github.com/vllm-project/vllm/pull/63063)
  [Perf][DSpark] Stack DeepSeek V41 context WKV projections (#63063)
  _Files: `tests/models/test_dspark_mla.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`_
- **2026-10-27** [`115b59a2da`](https://github.com/vllm-project/vllm/commit/115b59a2da) [#63857](https://github.com/vllm-project/vllm/pull/63857)
  [Recipes Tool] Fix TP auto-detection for heterogeneous per-layer attention models (#63857)
  _Files: `tools/recipes/model_constraints.py`_
- **2026-10-27** [`a23d7dc3f1`](https://github.com/vllm-project/vllm/commit/a23d7dc3f1) [#63738](https://github.com/vllm-project/vllm/pull/63738)
  [Bugfix][CPU] Run encoder-only attention bidirectionally in CPU_ATTN (#63738)
  _Files: `tests/kernels/attention/test_cpu_attn.py`, `tests/v1/attention/test_group_head_counts.py`, `vllm/model_executor/models/embedding_gemma2.py`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-10-27** [`8e26dec5f5`](https://github.com/vllm-project/vllm/commit/8e26dec5f5) [#57420](https://github.com/vllm-project/vllm/pull/57420)
  [Kernel][MiniMax-M3] Add Triton query-tiled sparse prefill tuned on Hopper (#57420)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/test_minimax_m3_sparse_attn_fp8_scale.py`, `vllm/models/minimax_m3/common/sparse_attention.py` _+1 more__
- **2026-10-27** [`8977b13a1c`](https://github.com/vllm-project/vllm/commit/8977b13a1c) [#59986](https://github.com/vllm-project/vllm/pull/59986)
  [Bugfix][Attention] Keep DSV4.1 sparse prefill out of FULL cudagraphs (#59986)
  _Files: `tests/v1/worker/test_attn_utils.py`, `vllm/models/deepseek_v41/compressor.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/flashmla.py` _+1 more__
- **2026-10-27** [`94f56ce92c`](https://github.com/vllm-project/vllm/commit/94f56ce92c) [#63864](https://github.com/vllm-project/vllm/pull/63864)
  [Perf] Tune the Triton packed GDN decode tile on SM90 (#63864)
  _Files: `vllm/third_party/flash_linear_attention/ops/fused_recurrent.py`_
- **2026-10-27** [`fe77d0906b`](https://github.com/vllm-project/vllm/commit/fe77d0906b) [#60942](https://github.com/vllm-project/vllm/pull/60942)
  [Bugfix] Fix Triton prefill attention OutOfResources on GPUs with 99KiB shared memory (#60942)
  _Files: `tests/kernels/attention/test_triton_prefill_attention.py`, `vllm/v1/attention/ops/triton_prefill_attention.py`_
- **2026-10-26** [`6597ceafbc`](https://github.com/vllm-project/vllm/commit/6597ceafbc) [#63638](https://github.com/vllm-project/vllm/pull/63638)
  [Perf][Kimi K3] Opt-in KV-balanced FP8 MLA decode for agentic workloads (#63638)
  _Files: `tests/models/kimi_k3/test_kv_balanced_mla.py`, `vllm/models/kimi_k3/nvidia/kv_balanced_mla/__init__.py`, `vllm/models/kimi_k3/nvidia/kv_balanced_mla/backend.py`, `vllm/models/kimi_k3/nvidia/kv_balanced_mla/core.py` _+4 more__
- **2026-10-26** [`4eb5df8038`](https://github.com/vllm-project/vllm/commit/4eb5df8038) [#61527](https://github.com/vllm-project/vllm/pull/61527)
  [Kimi-K3] Route the fp8 chunked-context K/V pack through FlashInfer where it has a fused kernel (#61527)
  _Files: `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`, `vllm/utils/flashinfer.py`_
- **2026-10-26** [`533906528c`](https://github.com/vllm-project/vllm/commit/533906528c) [#63436](https://github.com/vllm-project/vllm/pull/63436)
  [Bugfix][Spec Decode] DFlash: run the aux hidden state FC in the draft dtype (#63436)
  _Files: `tests/v1/spec_decode/test_dflash2.py`, `vllm/model_executor/models/qwen3_dflash.py`_
- **2026-10-26** [`a2ecc8ac4d`](https://github.com/vllm-project/vllm/commit/a2ecc8ac4d) [#61263](https://github.com/vllm-project/vllm/pull/61263)
  [Perf][HiSparse] Reduce residency hash probes (#61263)
  _Files: `csrc/hisparse_kernels.cu`, `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/hisparse/runtime.py`_
- **2026-10-26** [`6674eedd28`](https://github.com/vllm-project/vllm/commit/6674eedd28) [#63530](https://github.com/vllm-project/vllm/pull/63530)
  [XPU] Fix MLA cache op arguments (#63530)
  _Files: `vllm/_custom_ops.py`_
- **2026-10-26** [`bbf3d92190`](https://github.com/vllm-project/vllm/commit/bbf3d92190) [#63560](https://github.com/vllm-project/vllm/pull/63560)
  [Recipe] DeepSeek-V4.1-Flash: AgentX lanes as tuned presets (#63560)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`, `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`, `recipes/models/moonshotai/Kimi-K3.yaml`_

## KV Cache / Offload  (47 commits)

- **2026-11-02** [`f1df4a3ae9`](https://github.com/vllm-project/vllm/commit/f1df4a3ae9) [#64819](https://github.com/vllm-project/vllm/pull/64819)
  [Bugfix][KV Offload][P2P] Disconnect a peer whose registration fails (#64819)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/session/session.py`_
- **2026-11-01** [`b8c04dd3b4`](https://github.com/vllm-project/vllm/commit/b8c04dd3b4) [#63927](https://github.com/vllm-project/vllm/pull/63927)
  [Perf][KV Offload] Keep offload event metadata out of the cyclic GC (#63927)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py`_
- **2026-11-01** [`5d55ef1590`](https://github.com/vllm-project/vllm/commit/5d55ef1590) [#63900](https://github.com/vllm-project/vllm/pull/63900)
  [KV Offload] Remove unused touch from CachePolicy and OffloadingManager (#63900)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_offload/cpu/policies/test_factory.py`, `tests/v1/kv_offload/cpu/test_manager.py` _+9 more__
- **2026-11-01** [`17e675965d`](https://github.com/vllm-project/vllm/commit/17e675965d) [#63695](https://github.com/vllm-project/vllm/pull/63695)
  [KV Offload] Carry request context on raw stored events (#63695)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/base.py` _+3 more__
- **2026-10-30** [`a93c7fb73b`](https://github.com/vllm-project/vllm/commit/a93c7fb73b) [#64188](https://github.com/vllm-project/vllm/pull/64188)
  [Doc] Fix Case 4 math rendering in hybrid KV cache manager (#64188)
  _Files: `docs/design/hybrid_kv_cache_manager.md`_
- **2026-10-30** [`d15be0856d`](https://github.com/vllm-project/vllm/commit/d15be0856d) [#64612](https://github.com/vllm-project/vllm/pull/64612)
  [GLM5.3 Perf] Switching dlfash fp8 kv cache draft model, 2.85 GB memory saved per rank (#64612)
  _Files: `vllm/model_executor/models/config.py`_
- **2026-10-30** [`dfe4d99e42`](https://github.com/vllm-project/vllm/commit/dfe4d99e42) [#63249](https://github.com/vllm-project/vllm/pull/63249)
  [Bugfix][KV Offload] Preserve stored event prefix order (#63249)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-30** [`4d1376a492`](https://github.com/vllm-project/vllm/commit/4d1376a492) [#54307](https://github.com/vllm-project/vllm/pull/54307)
  [KV Connector] Support heterogeneous TP sharing for hybrid KV cache in Mooncake Store (#54307)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_layout.py` _+8 more__
- **2026-10-30** [`fac2ce2eb3`](https://github.com/vllm-project/vllm/commit/fac2ce2eb3) [#62613](https://github.com/vllm-project/vllm/pull/62613)
  [KV Offload] Emit self-describing events for recurrent state groups (#62613)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py`_
- **2026-10-29** [`4b47db922b`](https://github.com/vllm-project/vllm/commit/4b47db922b) [#64555](https://github.com/vllm-project/vllm/pull/64555)
  [CI][KV Offload][P2P] Wait for the handshake in the idle peer-hit tests (#64555)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`_
- **2026-10-29** [`55b677b2d1`](https://github.com/vllm-project/vllm/commit/55b677b2d1) [#64400](https://github.com/vllm-project/vllm/pull/64400)
  [Bugfix][KV Offload] Deduplicate in-flight partial-tail loads (#64400)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-29** [`4440f0e263`](https://github.com/vllm-project/vllm/commit/4440f0e263) [#59099](https://github.com/vllm-project/vllm/pull/59099)
  [Bugfix][KV Offload] Make reset_cache re-entrant (#59099)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-29** [`4158395108`](https://github.com/vllm-project/vllm/commit/4158395108) [#63618](https://github.com/vllm-project/vllm/pull/63618)
  [Bugfix][KV Offload] Let idle P2P-only engines park (#63618)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/test_tier_poll_thread.py`, `vllm/v1/kv_offload/tiering/manager.py` _+1 more__
- **2026-10-29** [`4a8c0da9e2`](https://github.com/vllm-project/vllm/commit/4a8c0da9e2) [#62930](https://github.com/vllm-project/vllm/pull/62930)
  [KV Offload] Reject secondary tiers on engines that span nodes (#62930)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/test_factory.py`, `vllm/v1/kv_offload/tiering/spec.py`_
- **2026-10-29** [`482e473253`](https://github.com/vllm-project/vllm/commit/482e473253) [#63566](https://github.com/vllm-project/vllm/pull/63566)
  [Bugfix][KV Offload] Pin a shared-prefix junction when a sparse group cuts the offload hit (#63566)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-29** [`a57d25617f`](https://github.com/vllm-project/vllm/commit/a57d25617f) [#63788](https://github.com/vllm-project/vllm/pull/63788)
  [Bugfix][KV Offload][OBJ] Don't lose a completed transfer when telemetry is unavailable (#63788)
  _Files: `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/tiering/obj/manager.py`_
- **2026-10-29** [`491067f445`](https://github.com/vllm-project/vllm/commit/491067f445) [#64251](https://github.com/vllm-project/vllm/pull/64251)
  [Bugfix][KV Offload][P2P] Fault a peer whose source WRITE stalls (#64251)
  _Files: `docs/usage/security.md`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/envs.py`, `vllm/v1/kv_offload/tiering/p2p/session/server.py` _+1 more__
- **2026-10-29** [`d0ab3ba9b4`](https://github.com/vllm-project/vllm/commit/d0ab3ba9b4) [#59322](https://github.com/vllm-project/vllm/pull/59322)
  [Perf][KV Offload] Avoid repeated hash-prefix scans (#59322)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-29** [`429eb22788`](https://github.com/vllm-project/vllm/commit/429eb22788) [#63937](https://github.com/vllm-project/vllm/pull/63937)
  [Bugfix][KV Offload] Do not offload the partially computed block of a request that finished with an error (#63937)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-29** [`8b286ac2b4`](https://github.com/vllm-project/vllm/commit/8b286ac2b4) [#64501](https://github.com/vllm-project/vllm/pull/64501)
  [Bugfix][KV Offload][P2P] Prefill locally while a peer handshake is pending (#64501)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `vllm/v1/kv_offload/tiering/p2p/manager.py`_
- **2026-10-29** [`3c39dda2a5`](https://github.com/vllm-project/vllm/commit/3c39dda2a5) [#64345](https://github.com/vllm-project/vllm/pull/64345)
  [Performance][KV Offload] Avoid zero-filling the SimpleCPUOffload host KV pool (#64345)
  _Files: `vllm/v1/simple_kv_offload/worker.py`_
- **2026-10-29** [`c1b7dffa14`](https://github.com/vllm-project/vllm/commit/c1b7dffa14) [#62444](https://github.com/vllm-project/vllm/pull/62444)
  [Bugfix][KV Offload] Refresh CPU LRU for GPU-hit prefixes in eager SimpleCPUOffload (#62444)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-10-29** [`16777da347`](https://github.com/vllm-project/vllm/commit/16777da347) [#64256](https://github.com/vllm-project/vllm/pull/64256)
  [Bugfix][KV Offload][P2P] Fail a timed-out load at once, defer releasing its slots (#64256)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/manager.py`, `vllm/v1/kv_offload/tiering/p2p/session/client.py` _+1 more__
- **2026-10-29** [`fed7de909f`](https://github.com/vllm-project/vllm/commit/fed7de909f) [#64224](https://github.com/vllm-project/vllm/pull/64224)
  [KV Offload] Update KVCR to v0.2.0 (#64224)
  _Files: `.buildkite/scripts/install-kv-offload.sh`, `tests/v1/kv_offload/tiering/test_kvcr_tier.py`, `vllm/v1/kv_offload/tiering/kvcr/manager.py`_
- **2026-10-28** [`65faf4efa0`](https://github.com/vllm-project/vllm/commit/65faf4efa0) [#63237](https://github.com/vllm-project/vllm/pull/63237)
  [Refactor][R3] Initialize routed experts capturer before KV cache profiling (#63237)
  _Files: `tests/model_executor/test_routed_experts_capture.py`, `tests/v1/worker/test_gpu_model_runner_v2.py`, `tests/v1/worker/test_gpu_worker.py`, `vllm/distributed/aux_output_connector/worker.py` _+2 more__
- **2026-10-28** [`a1cfd2c1b5`](https://github.com/vllm-project/vllm/commit/a1cfd2c1b5) [#64250](https://github.com/vllm-project/vllm/pull/64250)
  [Bugfix][KV Offload][P2P] Retain unconfirmed source WRITEs across session teardown (#64250)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_data_transport.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/data/base.py` _+4 more__
- **2026-10-28** [`0beab6c251`](https://github.com/vllm-project/vllm/commit/0beab6c251) [#63779](https://github.com/vllm-project/vllm/pull/63779)
  [KV Offload][Tiering] Let a tier fail a promotion and defer releasing its chunks (#63779)
  _Files: `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/base.py`, `vllm/v1/kv_offload/tiering/manager.py`, `vllm/v1/kv_offload/tiering/metrics.py` _+1 more__
- **2026-10-28** [`f4fd1ab68e`](https://github.com/vllm-project/vllm/commit/f4fd1ab68e) [#63207](https://github.com/vllm-project/vllm/pull/63207)
  [Bugfix][KV Offload][P2P] Stop DEALER monitor before closing its reader (#63207)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_zmq_transport.py`, `vllm/v1/kv_offload/tiering/p2p/control/zmq.py`_
- **2026-10-28** [`77f58e5304`](https://github.com/vllm-project/vllm/commit/77f58e5304) [#64229](https://github.com/vllm-project/vllm/pull/64229)
  [Bugfix][KV Offload] Count bounded-replay SWA allocations in the lazy walk target (#64229)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-10-27** [`36f5ff3172`](https://github.com/vllm-project/vllm/commit/36f5ff3172) [#63889](https://github.com/vllm-project/vllm/pull/63889)
  [Perf][KV Offload] Reduce KVCR adapter overhead (#63889)
  _Files: `tests/v1/kv_offload/tiering/test_kvcr_tier.py`, `vllm/v1/kv_offload/tiering/kvcr/manager.py`_
- **2026-10-27** [`c6f6e6a983`](https://github.com/vllm-project/vllm/commit/c6f6e6a983) [#63841](https://github.com/vllm-project/vllm/pull/63841)
  [GLM5.3 Perf] Enable dspark fp8 kv cache for draft model, 5.38 GB GPU Memory saved per rank (#63841)
  _Files: `vllm/model_executor/models/config.py`_
- **2026-10-27** [`e3883b7a7e`](https://github.com/vllm-project/vllm/commit/e3883b7a7e) [#60469](https://github.com/vllm-project/vllm/pull/60469)
  [KV Offload] Align KVCR cache recency with request prefixes (#60469)
  _Files: `tests/v1/kv_offload/tiering/test_kvcr_tier.py`, `vllm/v1/kv_offload/tiering/kvcr/manager.py`_
- **2026-10-27** [`3bc521d9e6`](https://github.com/vllm-project/vllm/commit/3bc521d9e6) [#61543](https://github.com/vllm-project/vllm/pull/61543)
  [Bugfix][HiSparse][KV Connector] Fix DecodeBenchConnector crash on bounded KV cache groups (#61543)
  _Files: `tests/v1/kv_connector/unit/test_decode_bench_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`_
- **2026-10-26** [`c13d4a5a46`](https://github.com/vllm-project/vllm/commit/c13d4a5a46) [#57646](https://github.com/vllm-project/vllm/pull/57646)
  [KV Offload] Expose the processed prefix at request finalization (#57646)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/v1/kv_offload/base.py`_
- **2026-10-26** [`9633997299`](https://github.com/vllm-project/vllm/commit/9633997299) [#63781](https://github.com/vllm-project/vllm/pull/63781)
  [KV Offload][P2P] Fail faster: per-mode load timeout, shorter abort-ack and lookup timeouts (#63781)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/manager.py`, `vllm/v1/kv_offload/tiering/p2p/session/client.py` _+1 more__
- **2026-10-26** [`e113018f50`](https://github.com/vllm-project/vllm/commit/e113018f50) [#61050](https://github.com/vllm-project/vllm/pull/61050)
  [Bugfix][KV Offload] Preserve running request prefixes across LRU store batches (#61050)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/cpu/policies/test_factory.py`, `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/v1/kv_offload/cpu/manager.py` _+3 more__
- **2026-10-26** [`51d2a85594`](https://github.com/vllm-project/vllm/commit/51d2a85594) [#63708](https://github.com/vllm-project/vllm/pull/63708)
  [Bugfix][KV Offload][P2P] Never block in ZmqConnection.send() (#63708)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_zmq_transport.py`, `vllm/v1/kv_offload/tiering/p2p/control/zmq.py`_
- **2026-10-26** [`14aefcd4f9`](https://github.com/vllm-project/vllm/commit/14aefcd4f9) [#62929](https://github.com/vllm-project/vllm/pull/62929)
  [Bugfix][KV Offload] Hold promotions after a cache reset until jobs report (#62929)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/test_offloading_connector.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py` _+3 more__
- **2026-10-26** [`8a4b018f1c`](https://github.com/vllm-project/vllm/commit/8a4b018f1c) [#63628](https://github.com/vllm-project/vllm/pull/63628)
  [Bugfix][KV Offload] Roll back failed P2P NIXL registration (#63628)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_data_transport.py`, `vllm/v1/kv_offload/tiering/p2p/data/nixl.py`_
- **2026-10-26** [`8c6e770a1c`](https://github.com/vllm-project/vllm/commit/8c6e770a1c) [#63655](https://github.com/vllm-project/vllm/pull/63655)
  [Bugfix][KV Offload][OBJ] Namespace object keys by blocks_per_chunk (#63655)
  _Files: `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/tiering/obj/manager.py`_
- **2026-10-26** [`a64fc94081`](https://github.com/vllm-project/vllm/commit/a64fc94081) [#60574](https://github.com/vllm-project/vllm/pull/60574)
  [Bugfix][KV Offload] Preserve new loads during same-step resume (#60574)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-26** [`f682f1dc32`](https://github.com/vllm-project/vllm/commit/f682f1dc32) [#63664](https://github.com/vllm-project/vllm/pull/63664)
  [Bugfix][KV Offload][P2P] Mark the session dead when its ConnectAck send fails (#63664)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/session/session.py`_
- **2026-10-26** [`5b06b5f8e9`](https://github.com/vllm-project/vllm/commit/5b06b5f8e9) [#53902](https://github.com/vllm-project/vllm/pull/53902)
  [Metrics][KV Offload] Fill vllm:kv_offload_config_info with the CPU cache capacity (#53902)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_offload/conftest.py` _+12 more__
- **2026-10-26** [`71294c2e9a`](https://github.com/vllm-project/vllm/commit/71294c2e9a) [#63498](https://github.com/vllm-project/vllm/pull/63498)
  [Bugfix][KV Offload][P2P] Exclude rc_gda lanes from the P2P NIXL agent (#63498)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_data_transport.py`, `vllm/v1/kv_offload/tiering/p2p/data/nixl.py`_
- **2026-10-26** [`1d3f05aadb`](https://github.com/vllm-project/vllm/commit/1d3f05aadb) [#63652](https://github.com/vllm-project/vllm/pull/63652)
  [Bugfix][KV Offload] Do not store sliding-window chunks with null blocks (#63652)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_connector/unit/test_offloading_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-26** [`fe5fe8ba5f`](https://github.com/vllm-project/vllm/commit/fe5fe8ba5f) [#61961](https://github.com/vllm-project/vllm/pull/61961)
  [KV Offload] Load small CPU-tier hits synchronously within the step (#61961)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py` _+6 more__
- **2026-10-26** [`2fb320d830`](https://github.com/vllm-project/vllm/commit/2fb320d830) [#61589](https://github.com/vllm-project/vllm/pull/61589)
  [Core][Spec Decode] Lookahead block hashes for EAGLE prefix caching (#61589)
  _Files: `examples/features/kv_events/kv_events_subscriber.py`, `tests/distributed/test_kv_cache_events.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `tests/v1/core/prefix_cache/test_mamba_eagle_resume_checkpoint.py` _+23 more__

## MoE / Expert Parallel  (43 commits)

- **2026-11-02** [`187f1a27dc`](https://github.com/vllm-project/vllm/commit/187f1a27dc) [#65059](https://github.com/vllm-project/vllm/pull/65059)
  [Bugfix][Kernel] Only set PDL launch attr for MoE top-k gating on SM90+ (#65059)
  _Files: `csrc/moe/topk_softmax_kernels.cu`_
- **2026-11-02** [`37e16689fa`](https://github.com/vllm-project/vllm/commit/37e16689fa) [#64659](https://github.com/vllm-project/vllm/pull/64659)
  [Perf][MiniMax-M3] Sequence parallelism and GEMM-RS for TP + MegaMoE (#64659)
  _Files: `benchmarks/kernels/benchmark_gemm_rs_ar.py`, `tests/kernels/test_gemm_rs_ar.py`, `vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py`, `vllm/models/minimax_m3/nvidia/model.py`_
- **2026-11-02** [`16d667348d`](https://github.com/vllm-project/vllm/commit/16d667348d) [#64914](https://github.com/vllm-project/vllm/pull/64914)
  [MRV2] Cap torch.topk rows in chunked prompt logprobs (#64914)
  _Files: `tests/v1/sample/test_logprobs.py`, `vllm/v1/worker/gpu/sample/prompt_logprob.py`_
- **2026-11-01** [`2a4792ddcc`](https://github.com/vllm-project/vllm/commit/2a4792ddcc) [#64955](https://github.com/vllm-project/vllm/pull/64955)
  [Perf][MoE] Fuse padding skipping in grouped and Muse prepared routing (#64955)
  _Files: `.buildkite/test_areas/kernels.yaml`, `csrc/moe/grouped_topk_kernels.cu`, `csrc/moe/moe_ops.h`, `csrc/moe/torch_bindings.cpp` _+9 more__
- **2026-10-31** [`d8fad9202a`](https://github.com/vllm-project/vllm/commit/d8fad9202a) [#64751](https://github.com/vllm-project/vllm/pull/64751)
  [Bugfix][Spec Decode] Honor draft moe/attention backend overrides for MRV2 standalone draft model (#64751)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/v1/worker/gpu/spec_decode/standalone_ar/speculator.py`_
- **2026-10-31** [`042f30f6e8`](https://github.com/vllm-project/vllm/commit/042f30f6e8) [#64653](https://github.com/vllm-project/vllm/pull/64653)
  [Perf][LoRA][MoE] Use the shrink/expand kernels for MoE-LoRA batches of up to 64 tokens (#64653)
  _Files: `tests/lora/test_fused_moe_lora_kernel.py`, `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`, `vllm/lora/ops/triton_ops/utils.py`_
- **2026-10-31** [`0aa72a450c`](https://github.com/vllm-project/vllm/commit/0aa72a450c) [#64673](https://github.com/vllm-project/vllm/pull/64673)
  [Perf][Parser] Skip tool-argument conversions after a replaced value (#64673)
  _Files: `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/engine/parser_engine.py`_
- **2026-10-30** [`e31cf3dec7`](https://github.com/vllm-project/vllm/commit/e31cf3dec7) [#64138](https://github.com/vllm-project/vllm/pull/64138)
  [Perf][DSA] Read BF16 logits directly in persistent top-k (#64138)
  _Files: `csrc/persistent_topk.cuh`, `csrc/persistent_topk_overflow.cuh`, `csrc/sampled_topk.cuh`, `csrc/topk.cu` _+7 more__
- **2026-10-30** [`becbaea9f5`](https://github.com/vllm-project/vllm/commit/becbaea9f5) [#64638](https://github.com/vllm-project/vllm/pull/64638)
  [Perf] Fuse all-gather and norm for Muse Spark hybrid MoE (#64638)
  _Files: `csrc/moe/muse_spark_routing.cu`, `tests/kernels/moe/test_muse_spark_trtllm_moe.py`, `vllm/models/muse_spark/nvidia/hybrid_moe.py`, `vllm/models/muse_spark/nvidia/mega_moe.py` _+1 more__
- **2026-10-30** [`2bfb8f1674`](https://github.com/vllm-project/vllm/commit/2bfb8f1674) [#64467](https://github.com/vllm-project/vllm/pull/64467)
  [Perf][MoE] Use 32-row tiles in prepare_megamoe_inputs from 1024 tokens (#64467)
  _Files: `tests/kernels/moe/test_deep_gemm_mega_moe.py`, `vllm/model_executor/layers/fused_moe/prepare_megamoe.py`_
- **2026-10-30** [`fa9356aba6`](https://github.com/vllm-project/vllm/commit/fa9356aba6) [#64065](https://github.com/vllm-project/vllm/pull/64065)
  [Bugfix][XPU] Add record_logical_topk_ready to XPUMLASparseImpl (#64065)
  _Files: `.buildkite/intel_jobs/kernels_intel.yaml`, `tests/v1/attention/test_xpu_mla_sparse_backend.py`, `vllm/v1/attention/backends/mla/xpu_mla_sparse.py`_
- **2026-10-30** [`36ed4327d2`](https://github.com/vllm-project/vllm/commit/36ed4327d2) [#64553](https://github.com/vllm-project/vllm/pull/64553)
  [Kernel] Add CUDA routing kernel for Muse Spark Open (#64553)
  _Files: `CMakeLists.txt`, `csrc/moe/moe_ops.h`, `csrc/moe/muse_spark_routing.cu`, `csrc/moe/torch_bindings.cpp` _+3 more__
- **2026-10-30** [`f2ba523d67`](https://github.com/vllm-project/vllm/commit/f2ba523d67) [#64576](https://github.com/vllm-project/vllm/pull/64576)
  [CI][MoE] Start every MoE kernel test file from a clean GPU state (#64576)
  _Files: `tests/kernels/moe/conftest.py`_
- **2026-10-29** [`255431b5ed`](https://github.com/vllm-project/vllm/commit/255431b5ed) [#64535](https://github.com/vllm-project/vllm/pull/64535)
  [Bugfix][Parser] Parse closed GLM-4.7 tool arguments once while streaming (#64535)
  _Files: `tests/parser/engine/test_glm47_moe.py`, `vllm/parser/glm47_moe.py`_
- **2026-10-29** [`b2f46e785f`](https://github.com/vllm-project/vllm/commit/b2f46e785f) [#62009](https://github.com/vllm-project/vllm/pull/62009)
  [Perf][EPLB][DSv4] Add a symm_mem weight-migration backend and fuse MegaMoE replica mapping (#62009)
  _Files: `.buildkite/test_areas/distributed.yaml`, `docs/serving/expert_parallel_deployment.md`, `tests/distributed/test_eplb_execute.py`, `tests/distributed/test_eplb_migration_scheduler.py` _+13 more__
- **2026-10-29** [`262eefc9f2`](https://github.com/vllm-project/vllm/commit/262eefc9f2) [#64525](https://github.com/vllm-project/vllm/pull/64525)
  [Model] Support hybrid MegaMoE/TRT-LLM execution for Muse Spark NVFP4 (#64525)
  _Files: `tests/kernels/moe/test_muse_spark_trtllm_moe.py`, `vllm/models/common/ops/sequence_parallel.py`, `vllm/models/muse_spark/nvidia/hybrid_moe.py`, `vllm/models/muse_spark/nvidia/mega_moe.py` _+2 more__
- **2026-10-29** [`21db9ecf2a`](https://github.com/vllm-project/vllm/commit/21db9ecf2a) [#63585](https://github.com/vllm-project/vllm/pull/63585)
  [Model] Support Ming3-ASR (inclusionAI/Ming-3.0-asr-tiny) (#63585)
  _Files: `docs/contributing/model/transcription.md`, `docs/models/supported_models.md`, `examples/generate/multimodal/audio_language_offline.py`, `recipes/models/inclusionAI/Ming-3.0-asr-tiny.yaml` _+17 more__
- **2026-10-29** [`18450e5ef7`](https://github.com/vllm-project/vllm/commit/18450e5ef7) [#61107](https://github.com/vllm-project/vllm/pull/61107)
  [Fusion] Fuse Qwen MoE shared MLP activation quantization (#61107)
  _Files: `vllm/model_executor/models/qwen2_moe.py`_
- **2026-10-29** [`a94b768d96`](https://github.com/vllm-project/vllm/commit/a94b768d96) [#64037](https://github.com/vllm-project/vllm/pull/64037)
  [Kernel][MiniMax-M3] Enable SM90 split-K in the Triton indexer (#64037)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`_
- **2026-10-28** [`e10ef091ba`](https://github.com/vllm-project/vllm/commit/e10ef091ba) [#62407](https://github.com/vllm-project/vllm/pull/62407)
  [Quantization] Keep deleted and renamed params registered after process_weights_after_loading (#62407)
  _Files: `tests/kernels/quantization/test_triton_w4a16.py`, `tests/kernels/quantization/test_zen_da8w4.py`, `tests/model_executor/test_utils.py`, `tests/quantization/test_auto_round.py` _+51 more__
- **2026-10-28** [`165213f911`](https://github.com/vllm-project/vllm/commit/165213f911) [#63871](https://github.com/vllm-project/vllm/pull/63871)
  [Bugfix][Muse] Finalize dummy-loaded MegaMoE weights (#63871)
  _Files: `docs/features/quantization/modelopt.md`, `tests/quantization/test_blackwell_moe.py`, `vllm/models/muse_spark/nvidia/mega_moe.py`, `vllm/models/muse_spark/nvidia/model.py`_
- **2026-10-28** [`1c787a25cc`](https://github.com/vllm-project/vllm/commit/1c787a25cc) [#62797](https://github.com/vllm-project/vllm/pull/62797)
  [Bugfix][LoRA] Reject non-linear expert placement with EP (#62797)
  _Files: `tests/lora/test_moe_lora_ep_load.py`, `vllm/lora/layers/fused_moe.py`_
- **2026-10-28** [`0106c8abce`](https://github.com/vllm-project/vllm/commit/0106c8abce) [#61831](https://github.com/vllm-project/vllm/pull/61831)
  [CI] Shard FP8 MoE kernels and L4 Humming eval automatically (#61831)
  _Files: `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/lm_eval.yaml`_
- **2026-10-27** [`c56706e88e`](https://github.com/vllm-project/vllm/commit/c56706e88e) [#63820](https://github.com/vllm-project/vllm/pull/63820)
  [Perf] Use TMA for MOE up/down proj, 3.1~3.4% E2E Throughput Improvement for GLM5.3 (#63820)
  _Files: `tests/kernels/moe/test_block_fp8.py`, `tests/kernels/moe/test_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`_
- **2026-10-27** [`f03b704da2`](https://github.com/vllm-project/vllm/commit/f03b704da2) [#62133](https://github.com/vllm-project/vllm/pull/62133)
  [Bugfix][Kernel] Fix OAI Triton MXFP4 MoE on SM110 (#62133)
  _Files: `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`_
- **2026-10-27** [`08d94f0176`](https://github.com/vllm-project/vllm/commit/08d94f0176) [#63920](https://github.com/vllm-project/vllm/pull/63920)
  [Model] Add JIT warmup for Muse Spark NVFP4 MegaMoE input preparation (#63920)
  _Files: `vllm/models/muse_spark/nvidia/model.py`, `vllm/models/muse_spark/nvidia/ops/prepare_megamoe_nvfp4.py`_
- **2026-10-27** [`ef2f382fd1`](https://github.com/vllm-project/vllm/commit/ef2f382fd1) [#63894](https://github.com/vllm-project/vllm/pull/63894)
  [Bugfix][LoRA] Avoid double rounding in fused MoE expand (#63894)
  _Files: `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`_
- **2026-10-27** [`0076619a94`](https://github.com/vllm-project/vllm/commit/0076619a94) [#61903](https://github.com/vllm-project/vllm/pull/61903)
  [Perf][Kernel] Add a CuteDSL BF16x3 router GEMM for fp32 router weights on Hopper (#61903)
  _Files: `.buildkite/test_areas/kernels.yaml`, `.github/CODEOWNERS`, `tests/kernels/test_bf16x3_router_gemm_cutedsl.py`, `vllm/model_executor/layers/fused_moe/router/bf16x3_router_gemm_sm100.py` _+3 more__
- **2026-10-27** [`c325754771`](https://github.com/vllm-project/vllm/commit/c325754771) [#60514](https://github.com/vllm-project/vllm/pull/60514)
  [Bugfix] Fall back from DeepGEMM and FlashInfer sampling when nvcc is missing (#60514)
  _Files: `tests/utils_/test_deep_gemm_utils.py`, `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/utils/deep_gemm.py`, `vllm/v1/sample/ops/topk_topp_sampler.py`_
- **2026-10-26** [`2feedbe8dc`](https://github.com/vllm-project/vllm/commit/2feedbe8dc) [#63541](https://github.com/vllm-project/vllm/pull/63541)
  [Perf][MoE] Size the DeepGEMM MegaMoE symmetric buffer for one sequence-parallel shard (#63541)
  _Files: `vllm/model_executor/layers/fused_moe/deep_gemm_mega_moe.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-10-26** [`1fd6337e22`](https://github.com/vllm-project/vllm/commit/1fd6337e22) [#61038](https://github.com/vllm-project/vllm/pull/61038)
  [Bugfix] Keep legacy WNA16 MoE dispatch on Triton under batch invariance (#61038)
  _Files: `vllm/model_executor/layers/fused_moe/fused_moe.py`_
- **2026-10-26** [`12d54c2948`](https://github.com/vllm-project/vllm/commit/12d54c2948) [#51605](https://github.com/vllm-project/vllm/pull/51605)
  [XPU][MoE] Resize batched Triton MoE tiles and change grid order (#51605)
  _Files: `tests/kernels/moe/test_batched_moe.py`, `vllm/model_executor/layers/fused_moe/experts/fused_batched_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`_
- **2026-10-26** [`f3bdb0e025`](https://github.com/vllm-project/vllm/commit/f3bdb0e025) [#63101](https://github.com/vllm-project/vllm/pull/63101)
  [Perf][MXFP4] Optimize activation quant for mxfp4. 3x kernel speedup, 5% throughput improvement (#63101)
  _Files: `benchmarks/kernels/benchmark_mxfp4_experts_activation_quant.py`, `csrc/ops.h`, `csrc/quantization/fp4/mxfp4_experts_quant.cu`, `csrc/quantization/w8a8/cutlass/moe/moe_data.cu` _+5 more__
- **2026-10-26** [`3090266d88`](https://github.com/vllm-project/vllm/commit/3090266d88) [#63475](https://github.com/vllm-project/vllm/pull/63475)
  [Bugfix][Kernel] persistent_topk: sync the CTA around radix barrier arrivals (#63475)
  _Files: `csrc/persistent_topk.cuh`_
- **2026-10-26** [`89f0c8c668`](https://github.com/vllm-project/vllm/commit/89f0c8c668) [#62525](https://github.com/vllm-project/vllm/pull/62525)
  [MoE][Model] Gemma 4: skip CUDA-graph padding rows in the routing kernel (#62525)
  _Files: `tests/kernels/moe/test_gemma4router.py`, `tests/kernels/moe/test_topk_softplus_sqrt.py`, `vllm/model_executor/layers/fused_moe/router/base_router.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py` _+2 more__
- **2026-10-26** [`9e3db48873`](https://github.com/vllm-project/vllm/commit/9e3db48873) [#61685](https://github.com/vllm-project/vllm/pull/61685)
  [MoE] Add locality-domain allocation for FlashInfer CuTeDSL NVFP4 (#61685)
  _Files: `.buildkite/test_areas/distributed.yaml`, `tests/distributed/test_localization.py`, `tests/kernels/moe/test_flashinfer_cutedsl_nvfp4_moe.py`, `vllm/distributed/localization.py` _+6 more__
- **2026-10-26** [`4f140a23de`](https://github.com/vllm-project/vllm/commit/4f140a23de) [#63698](https://github.com/vllm-project/vllm/pull/63698)
  [Bugfix] Initialize valid ModelOpt NVFP4 MoE dummy scales (#63698)
  _Files: `docs/features/quantization/modelopt.md`, `tests/quantization/test_blackwell_moe.py`, `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-10-26** [`33a73daf17`](https://github.com/vllm-project/vllm/commit/33a73daf17) [#62936](https://github.com/vllm-project/vllm/pull/62936)
  [2/N][Bugfix] Make persistent TopK exact on candidate overflow (#62936)
  _Files: `csrc/persistent_topk.cuh`, `csrc/persistent_topk_overflow.cuh`, `csrc/topk.cu`, `csrc/topk_histogram_4096.cuh` _+2 more__
- **2026-10-26** [`61b2527bdb`](https://github.com/vllm-project/vllm/commit/61b2527bdb) [#62763](https://github.com/vllm-project/vllm/pull/62763)
  [Perf][MoE] Add H200 FP8 fused MoE config for Beam-1.0 TP8 (#62763)
  _Files: `benchmarks/kernels/benchmark_moe.py`, `vllm/model_executor/layers/fused_moe/configs/E=256,N=320,device_name=NVIDIA_H200,dtype=fp8_w8a8.json`_
- **2026-10-26** [`14d593115d`](https://github.com/vllm-project/vllm/commit/14d593115d) [#61636](https://github.com/vllm-project/vllm/pull/61636)
  [Bugfix][LoRA] Fix double pinning of 3D MoE LoRA and EP dummy LoRA sizing (#61636)
  _Files: `tests/lora/test_lora_manager.py`, `vllm/lora/model_manager.py`_
- **2026-10-26** [`2f1cb151fd`](https://github.com/vllm-project/vllm/commit/2f1cb151fd) [#59931](https://github.com/vllm-project/vllm/pull/59931)
  [Bugfix] Preserve fp16 in legacy fused MoE LoRA (#59931)
  _Files: `tests/lora/test_fused_moe_lora_kernel.py`, `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`_
- **2026-10-26** [`fcb787055e`](https://github.com/vllm-project/vllm/commit/fcb787055e) [#61875](https://github.com/vllm-project/vllm/pull/61875)
  [Perf][DeepSeek V4] Declare MXFP8 MoE activations and run them as block FP8 on Hopper (#61875)
  _Files: `tests/quantization/test_fp8.py`, `tests/quantization/test_humming_mxfp4_block_fp8.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/models/deepseek_v4/quant_config.py` _+1 more__
- **2026-10-26** [`5a224c1ef3`](https://github.com/vllm-project/vllm/commit/5a224c1ef3) [#63506](https://github.com/vllm-project/vllm/pull/63506)
  [Fast Start] Key the weight cache on MoE and linear kernel backends (#63506)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py`, `vllm/model_executor/model_loader/weight_cache/protocol.py`_

## Serving / API  (39 commits)

- **2026-11-02** [`e92bac311c`](https://github.com/vllm-project/vllm/commit/e92bac311c) [#63302](https://github.com/vllm-project/vllm/pull/63302)
  [Frontend] Validate JSON body and request_ids in /inference/v1/abort_requests (#63302)
  _Files: `vllm/entrypoints/scale_out/token_in_token_out/api_router.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`_
- **2026-11-02** [`7ff608a03c`](https://github.com/vllm-project/vllm/commit/7ff608a03c) [#63103](https://github.com/vllm-project/vllm/pull/63103)
  [Frontend] Stream derender on /inference/v1/generate (#63103)
  _Files: `docs/serving/online_serving/derenderer.md`, `docs/serving/online_serving/token_in_token_out.md`, `tests/entrypoints/scale_out/derender/test_derender_parity.py`, `tests/entrypoints/scale_out/token_in_token_out/test_generate_stream.py` _+5 more__
- **2026-11-02** [`e8570ef757`](https://github.com/vllm-project/vllm/commit/e8570ef757) [#65166](https://github.com/vllm-project/vllm/pull/65166)
  [Perf][Frontend] Validate plain embedding inputs before the full union (#65166)
  _Files: `tests/entrypoints/pooling/embed/test_io_processor.py`, `vllm/entrypoints/pooling/embed/protocol.py`_
- **2026-11-02** [`30565c3937`](https://github.com/vllm-project/vllm/commit/30565c3937) [#63137](https://github.com/vllm-project/vllm/pull/63137)
  [Rust Frontend] Accept duplicate reasoning aliases in chat messages (#63137)
  _Files: `rust/src/server/src/routes/openai/utils/types.rs`_
- **2026-11-02** [`76c6f3f2a9`](https://github.com/vllm-project/vllm/commit/76c6f3f2a9) [#64599](https://github.com/vllm-project/vllm/pull/64599)
  [CI] Enroll the remaining Rust frontend and OpenAI API correctness jobs in automatic sharding (6 jobs) (#64599)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/rust_frontend.yaml`_
- **2026-11-02** [`945d0a268b`](https://github.com/vllm-project/vllm/commit/945d0a268b) [#35508](https://github.com/vllm-project/vllm/pull/35508)
  [Responses] Normalize OpenResponses input items to match openai-python SDK requirements (#35508)
  _Files: `tests/entrypoints/openai/parser/test_harmony_utils.py`, `tests/entrypoints/openai/responses/test_function_call_parsing.py`, `tests/entrypoints/openai/responses/test_protocol.py`, `tests/entrypoints/openai/responses/test_responses_utils.py` _+4 more__
- **2026-10-31** [`0c63ce9f0e`](https://github.com/vllm-project/vllm/commit/0c63ce9f0e) [#64757](https://github.com/vllm-project/vllm/pull/64757)
  [Bugfix][Frontend] Report prompt_tokens_details in batched chat completions (#64757)
  _Files: `docs/serving/online_serving/openai_compatible_server.md`, `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py`_
- **2026-10-31** [`5829ca82e8`](https://github.com/vllm-project/vllm/commit/5829ca82e8) [#64575](https://github.com/vllm-project/vllm/pull/64575)
  [Frontend] Reject Anthropic-defined tools by type in /v1/messages (#64575)
  _Files: `docs/serving/integrations/claude_code.md`, `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/anthropic/test_messages.py`, `vllm/entrypoints/anthropic/protocol.py`_
- **2026-10-31** [`8777b4c86c`](https://github.com/vllm-project/vllm/commit/8777b4c86c) [#64674](https://github.com/vllm-project/vllm/pull/64674)
  [Perf][Frontend] Decode streamed custom-tool input incrementally (#64674)
  _Files: `tests/entrypoints/openai/responses/test_streaming_events.py`, `vllm/entrypoints/openai/responses/streaming_events.py`, `vllm/entrypoints/openai/responses/utils.py`_
- **2026-10-30** [`6de8c7ba51`](https://github.com/vllm-project/vllm/commit/6de8c7ba51) [#64526](https://github.com/vllm-project/vllm/pull/64526)
  [Rust Frontend] Support return_prompt_text (#64526)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/request.rs`, `rust/src/chat/src/stream.rs`, `rust/src/chat/tests/chat.rs` _+7 more__
- **2026-10-30** [`c817cc0f8b`](https://github.com/vllm-project/vllm/commit/c817cc0f8b) [#64219](https://github.com/vllm-project/vllm/pull/64219)
  [Rust Frontend] Report completion_tokens_details only when reasoning tokens are counted (#64219)
  _Files: `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/utils/types.rs` _+2 more__
- **2026-10-30** [`515b8753e3`](https://github.com/vllm-project/vllm/commit/515b8753e3) [#64223](https://github.com/vllm-project/vllm/pull/64223)
  [Rust Frontend] Support --max-log-len (#64223)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/server/src/config.rs` _+6 more__
- **2026-10-30** [`d8a7945791`](https://github.com/vllm-project/vllm/commit/d8a7945791) [#64220](https://github.com/vllm-project/vllm/pull/64220)
  [Rust Frontend] Report prompt logprobs on streamed completions echo like Python (#64220)
  _Files: `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/completions/convert.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-10-30** [`52737e03b8`](https://github.com/vllm-project/vllm/commit/52737e03b8) [#64218](https://github.com/vllm-project/vllm/pull/64218)
  [Rust Frontend] Support return_weight_versions (#64218)
  _Files: `rust/src/chat/src/event.rs`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/default/unified.rs`, `rust/src/chat/src/output/harmony/mod.rs` _+21 more__
- **2026-10-30** [`8bad43e2c0`](https://github.com/vllm-project/vllm/commit/8bad43e2c0) [#48951](https://github.com/vllm-project/vllm/pull/48951)
  [Rust Frontend] Fix bad_words handling in /v1/completions (#48951)
  _Files: `rust/src/server/src/routes/openai/completions/convert.rs`, `rust/src/server/src/routes/openai/completions/types.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-10-30** [`19e24f0ca8`](https://github.com/vllm-project/vllm/commit/19e24f0ca8) [#63692](https://github.com/vllm-project/vllm/pull/63692)
  [Fast Start] Stop preload groups when a daemon rank exits (#63692)
  _Files: `.buildkite/test_areas/distributed.yaml`, `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/entrypoints/cli/preload.py`_
- **2026-10-30** [`c05e9edb78`](https://github.com/vllm-project/vllm/commit/c05e9edb78) [#62753](https://github.com/vllm-project/vllm/pull/62753)
  [Bugfix][Benchmark] Count tool call deltas as generated tokens in openai-responses (#62753)
  _Files: `tests/benchmarks/test_responses_request_func.py`, `vllm/benchmarks/lib/endpoint_request_func.py`_
- **2026-10-30** [`32a73034d5`](https://github.com/vllm-project/vllm/commit/32a73034d5) [#64557](https://github.com/vllm-project/vllm/pull/64557)
  [Bugfix][Rust Frontend] Count tool call deltas as generated tokens in vllm-bench openai-responses (#64557)
  _Files: `rust/src/bench/src/backends/openai_responses.rs`_
- **2026-10-29** [`971378f466`](https://github.com/vllm-project/vllm/commit/971378f466) [#63594](https://github.com/vllm-project/vllm/pull/63594)
  [Bugfix][Frontend] Probe non-jinja renderers for inline system message support (Anthropic API) (#63594)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-10-29** [`51be9ea6a3`](https://github.com/vllm-project/vllm/commit/51be9ea6a3) [#64503](https://github.com/vllm-project/vllm/pull/64503)
  [Security] Enforce request template trust for structured decisions (#64503)
  _Files: `docs/models/structured_decisions_models.md`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `tests/entrypoints/generate/structured_decisions/test_structured_decisions_e2e.py`, `vllm/entrypoints/generate/structured_decisions/serving.py`_
- **2026-10-29** [`a8a0520e43`](https://github.com/vllm-project/vllm/commit/a8a0520e43) [#57990](https://github.com/vllm-project/vllm/pull/57990)
  [Bugfix] [Frontend] Preserve prompt_logprobs in /v1/completions/derender (#57990)
  _Files: `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/entrypoints/scale_out/derender/serving.py`, `vllm/renderers/online_derenderer.py`_
- **2026-10-29** [`5c19391400`](https://github.com/vllm-project/vllm/commit/5c19391400) [#63896](https://github.com/vllm-project/vllm/pull/63896)
  [Frontend] Support thinking_token_budget in the Responses API (#63896)
  _Files: `docs/features/reasoning_outputs.md`, `tests/entrypoints/openai/chat_completion/test_thinking_token_budget.py`, `tests/entrypoints/openai/responses/test_sampling_params.py`, `vllm/entrypoints/openai/responses/protocol.py`_
- **2026-10-29** [`d8e6fbe461`](https://github.com/vllm-project/vllm/commit/d8e6fbe461) [#64367](https://github.com/vllm-project/vllm/pull/64367)
  [Bugfix] Consume prompt embedding sentinel IDs before model execution (#64367)
  _Files: `docs/features/prompt_embeds.md`, `tests/entrypoints/openai/chat_completion/test_chat_completion_with_prompt_embeds.py`, `tests/renderers/test_hf.py`, `vllm/renderers/hf.py`_
- **2026-10-28** [`9b9eeb283a`](https://github.com/vllm-project/vllm/commit/9b9eeb283a) [#64170](https://github.com/vllm-project/vllm/pull/64170)
  [Doc] Fix long-text embedding example pooler config and GPU pinning (#64170)
  _Files: `examples/pooling/embed/openai_embedding_long_text/README.md`, `examples/pooling/embed/openai_embedding_long_text/service.sh`_
- **2026-10-28** [`9fc019a749`](https://github.com/vllm-project/vllm/commit/9fc019a749) [#64097](https://github.com/vllm-project/vllm/pull/64097)
  [Frontend] Support /v1/completions in run-batch (#64097)
  _Files: `examples/features/openai_batch/README.md`, `tests/entrypoints/launchers/test_run_batch.py`, `vllm/entrypoints/launchers/run_batch.py`_
- **2026-10-28** [`e82e6d422f`](https://github.com/vllm-project/vllm/commit/e82e6d422f) [#55200](https://github.com/vllm-project/vllm/pull/55200)
  [Bugfix][Pooling] Reject prompt-wide truncation for Jina ranking (#55200)
  _Files: `docs/models/pooling_models/token_embed.md`, `tests/entrypoints/pooling/scoring/test_jina_ranking_io_processor_unit.py`, `tests/models/language/pooling/test_jina_reranker_v3.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`_
- **2026-10-28** [`665bfc8aae`](https://github.com/vllm-project/vllm/commit/665bfc8aae) [#52120](https://github.com/vllm-project/vllm/pull/52120)
  [Security] Fix ReDoS in validation error path sanitizer (#52120)
  _Files: `tests/entrypoints/serve/exception_handling/test_error_sanitization.py`, `vllm/entrypoints/serve/exception_handling/utils.py`_
- **2026-10-28** [`b766f15983`](https://github.com/vllm-project/vllm/commit/b766f15983) [#64020](https://github.com/vllm-project/vllm/pull/64020)
  [Bugfix][Frontend] fix Anthropic inline-system probe crashing startup (#64020)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-10-28** [`e4c2afdc17`](https://github.com/vllm-project/vllm/commit/e4c2afdc17) [#63964](https://github.com/vllm-project/vllm/pull/63964)
  [Rust Frontend] Reject max_tokens above max_model_len like Python (#63964)
  _Files: `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/utils/mod.rs`, `rust/src/server/src/routes/render.rs` _+2 more__
- **2026-10-28** [`6376fda7a9`](https://github.com/vllm-project/vllm/commit/6376fda7a9) [#59694](https://github.com/vllm-project/vllm/pull/59694)
  [Bugfix][Rust Frontend] Use server-reported prompt_tokens in vllm-bench (#59694)
  _Files: `rust/src/bench/src/backends/mod.rs`, `rust/src/bench/src/backends/openai_chat.rs`, `rust/src/bench/src/backends/openai_completions.rs`, `rust/src/bench/src/backends/openai_responses.rs` _+3 more__
- **2026-10-27** [`447d28eef2`](https://github.com/vllm-project/vllm/commit/447d28eef2) [#63292](https://github.com/vllm-project/vllm/pull/63292)
  [Rust Frontend] Group prompt-cache usage and report created_cache_tokens (#63292)
  _Files: `rust/src/chat/src/output/harmony/tests.rs`, `rust/src/chat/src/output/structured.rs`, `rust/src/chat/src/stream.rs`, `rust/src/cmd/src/cli.rs` _+12 more__
- **2026-10-27** [`2fb5111bba`](https://github.com/vllm-project/vllm/commit/2fb5111bba) [#63789](https://github.com/vllm-project/vllm/pull/63789)
  [Perf][Rust Frontend] Skip detokenization for gRPC requests that read no text (#63789)
  _Files: `rust/proto/inference.proto`, `rust/src/server/src/grpc/convert.rs`, `rust/src/server/src/grpc/tests.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs` _+6 more__
- **2026-10-27** [`7fe793a5d5`](https://github.com/vllm-project/vllm/commit/7fe793a5d5) [#63769](https://github.com/vllm-project/vllm/pull/63769)
  [Rust Frontend] Support --enable-log-outputs and --enable-log-deltas (#63769)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/server/src/config.rs` _+7 more__
- **2026-10-27** [`22d1bc8814`](https://github.com/vllm-project/vllm/commit/22d1bc8814) [#63772](https://github.com/vllm-project/vllm/pull/63772)
  [Rust Frontend] Stream kv_transfer_params on the final chunk like Python (#63772)
  _Files: `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/types.rs`, `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/completions/types.rs`_
- **2026-10-27** [`924f8ae7e5`](https://github.com/vllm-project/vllm/commit/924f8ae7e5) [#63766](https://github.com/vllm-project/vllm/pull/63766)
  [Rust Frontend] Serialize unset completions and first-chunk keys as null like Python (#63766)
  _Files: `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/types.rs`, `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/completions/types.rs` _+1 more__
- **2026-10-27** [`63773149fd`](https://github.com/vllm-project/vllm/commit/63773149fd) [#63764](https://github.com/vllm-project/vllm/pull/63764)
  [Rust Frontend] Advance streamed completion text_offset by reported tokens (#63764)
  _Files: `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/utils/logprobs.rs`_
- **2026-10-26** [`01b05cd69d`](https://github.com/vllm-project/vllm/commit/01b05cd69d) [#55699](https://github.com/vllm-project/vllm/pull/55699)
  [Bugfix][Frontend] Stop SSL certificate watchers when HTTP serving exits (#55699)
  _Files: `tests/entrypoints/launchers/test_ssl_cert_refresher.py`, `vllm/entrypoints/launchers/launcher.py`_
- **2026-10-26** [`c36154742e`](https://github.com/vllm-project/vllm/commit/c36154742e) [#58885](https://github.com/vllm-project/vllm/pull/58885)
  [Bugfix][Rust Frontend] Use prefiller cache hits for P/D usage (#58885)
  _Files: `rust/src/llm/src/lib.rs`, `rust/src/llm/src/output.rs`, `rust/src/llm/src/request.rs`, `rust/src/llm/tests/generate.rs` _+1 more__
- **2026-10-26** [`059e2de6d8`](https://github.com/vllm-project/vllm/commit/059e2de6d8) [#62450](https://github.com/vllm-project/vllm/pull/62450)
  [Bugfix][Frontend] Preserve DP rank in Responses requests (#62450)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/serving.py`_

## Other  (38 commits)

- **2026-11-02** [`5c8ae7c74a`](https://github.com/vllm-project/vllm/commit/5c8ae7c74a) [#63974](https://github.com/vllm-project/vllm/pull/63974)
  [Bugfix][Rust Frontend] Match Python text-part joining for HF templates (#63974)
  _Files: `rust/src/chat/src/renderer/hf/mod.rs`_
- **2026-11-02** [`1b95bc6c6b`](https://github.com/vllm-project/vllm/commit/1b95bc6c6b) [#63901](https://github.com/vllm-project/vllm/pull/63901)
  [Rust Frontend][1/3] Map developer messages to system for templates without the developer role (#63901)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/chat/src/renderer/hf/mod.rs`, `rust/src/chat/src/renderer/hf/template.rs`_
- **2026-11-02** [`e8ec12c5ed`](https://github.com/vllm-project/vllm/commit/e8ec12c5ed) [#61219](https://github.com/vllm-project/vllm/pull/61219)
  [Bugfix][Spec Decode] V2 rejection sampler: return logprob_token_ids scores (#61219)
  _Files: `tests/v1/worker/test_gpu_batch_shard.py`, `tests/v1/worker/test_gpu_rejection_sampler_chunking.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/sample/sampler.py` _+1 more__
- **2026-10-31** [`cfa9f96f5e`](https://github.com/vllm-project/vllm/commit/cfa9f96f5e) [#61542](https://github.com/vllm-project/vllm/pull/61542)
  [Bugfix][Tool Parser] Preserve whitespace in HYV4 argument names (#61542)
  _Files: `tests/tool_parsers/test_hy_v4_tool_parser.py`, `tests/tool_parsers/test_structural_tag_registry.py`, `vllm/tool_parsers/hy_v4_tool_parser.py`_
- **2026-10-31** [`42258ca4af`](https://github.com/vllm-project/vllm/commit/42258ca4af) [#64841](https://github.com/vllm-project/vllm/pull/64841)
  [ModelRunner V2] Reduce peak memory of chunked prompt logprobs (#64841)
  _Files: `tests/v1/sample/test_logprobs.py`, `vllm/v1/worker/gpu/sample/prompt_logprob.py`_
- **2026-10-31** [`1633271451`](https://github.com/vllm-project/vllm/commit/1633271451) [#64269](https://github.com/vllm-project/vllm/pull/64269)
  [Pooling] Speed up ColBERT reranking with batched token heads (#64269)
  _Files: `tests/model_executor/layers/test_pooler_methods.py`, `vllm/model_executor/layers/pooler/tokwise/heads.py`, `vllm/model_executor/layers/pooler/tokwise/poolers.py`_
- **2026-10-31** [`8ecf86ba83`](https://github.com/vllm-project/vllm/commit/8ecf86ba83) [#30614](https://github.com/vllm-project/vllm/pull/30614)
  [Feature] Default EPLB num_redundant_experts to minimum valid value (#30614)
  _Files: `tests/test_config.py`, `vllm/config/parallel.py`, `vllm/config/vllm.py`_
- **2026-10-31** [`1944a235a2`](https://github.com/vllm-project/vllm/commit/1944a235a2) [#64830](https://github.com/vllm-project/vllm/pull/64830)
  [Config] Move V2-only checks into V1 model runner unsupported features (#64830)
  _Files: `tests/test_config.py`, `tests/v1/spec_decode/test_custom_speculator.py`, `vllm/config/vllm.py`_
- **2026-10-30** [`212f3666a8`](https://github.com/vllm-project/vllm/commit/212f3666a8) [#63482](https://github.com/vllm-project/vllm/pull/63482)
  [Bugfix] [Tokenizer] Preserve Hub model identity when loading tokenizer snapshots (#63482)
  _Files: `tests/tokenizers_/test_registry.py`, `vllm/tokenizers/registry.py`_
- **2026-10-30** [`ed14230f4f`](https://github.com/vllm-project/vllm/commit/ed14230f4f) [#63922](https://github.com/vllm-project/vllm/pull/63922)
  [Bugfix] Skip more weight formats in the tokenizer/processor snapshot (#63922)
  _Files: `pyproject.toml`, `vllm/transformers_utils/repo_utils.py`_
- **2026-10-30** [`c9af9acc6a`](https://github.com/vllm-project/vllm/commit/c9af9acc6a) [#61380](https://github.com/vllm-project/vllm/pull/61380)
  [Bugfix] Resolve HF paths when loading sharded state (#61380)
  _Files: `tests/model_executor/model_loader/test_sharded_state_loader.py`, `vllm/model_executor/model_loader/sharded_state_loader.py`_
- **2026-10-30** [`deacc36701`](https://github.com/vllm-project/vllm/commit/deacc36701) [#64630](https://github.com/vllm-project/vllm/pull/64630)
  [Bugfix][SleepMode] Exact-size, reusable pinned CPU backup for level-1 sleep (#64630)
  _Files: `tests/basic_correctness/memory/cumem/test_cumem.py`, `vllm/device_allocator/cumem.py`, `vllm/device_allocator/xpumem.py`_
- **2026-10-30** [`8b9a4341db`](https://github.com/vllm-project/vllm/commit/8b9a4341db) [#62674](https://github.com/vllm-project/vllm/pull/62674)
  [Bugfix] Retry incomplete HTTP response bodies (#62674)
  _Files: `tests/test_connections.py`, `vllm/connections.py`_
- **2026-10-30** [`a70e48deba`](https://github.com/vllm-project/vllm/commit/a70e48deba) [#64274](https://github.com/vllm-project/vllm/pull/64274)
  [Rust Frontend] Reject chat templates for native renderers (#64274)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/error.rs`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/renderer/hf/mod.rs` _+2 more__
- **2026-10-30** [`dc420193b7`](https://github.com/vllm-project/vllm/commit/dc420193b7) [#64615](https://github.com/vllm-project/vllm/pull/64615)
  [Bugfix][Frontend] Leave GLM-4.7 array and object tool arguments unpinned (#64615)
  _Files: `tests/tool_parsers/test_structural_tag_registry.py`, `vllm/tool_parsers/structural_tag_registry.py`_
- **2026-10-29** [`24e80c2614`](https://github.com/vllm-project/vllm/commit/24e80c2614) [#64113](https://github.com/vllm-project/vllm/pull/64113)
  [CI/Build] Add nixl auto-label rule and assign topic owners (#64113)
  _Files: `.github/mergify.yml`_
- **2026-10-29** [`d1ad431de6`](https://github.com/vllm-project/vllm/commit/d1ad431de6) [#64279](https://github.com/vllm-project/vllm/pull/64279)
  [Bugfix][Compile] Fix KV-cache corruption under whole-graph compile (revert #42129) (#64279)
  _Files: `tests/compile/test_inductor_fallback_allow_list_patch.py`, `tests/compile/test_inductor_operator_str_patch.py`, `tests/models/transformers/test_backend.py`, `vllm/env_override.py`_
- **2026-10-29** [`a1e212757c`](https://github.com/vllm-project/vllm/commit/a1e212757c) [#64390](https://github.com/vllm-project/vllm/pull/64390)
  [Bugfix][Rust Frontend] Rust vllm-bench accepts --max-concurrency 0 and hangs forever (Python rejects it since #54887) (#64390)
  _Files: `rust/src/bench/src/config.rs`, `rust/src/bench/src/mm_processor.rs`, `rust/src/bench/src/sweep.rs`_
- **2026-10-29** [`0d6f92ae7c`](https://github.com/vllm-project/vllm/commit/0d6f92ae7c) [#64137](https://github.com/vllm-project/vllm/pull/64137)
  [Bugfix][Spec Decode] Don't specialize MRV2 logits-stats kernels on num_logits (#64137)
  _Files: `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-10-29** [`8d3f6f7e78`](https://github.com/vllm-project/vllm/commit/8d3f6f7e78) [#64013](https://github.com/vllm-project/vllm/pull/64013)
  [Bugfix] Parenthesize penalties Triton chained `or` for Ascend backends (#64013)
  _Files: `vllm/v1/worker/gpu/sample/penalties.py`_
- **2026-10-28** [`00d4b78221`](https://github.com/vllm-project/vllm/commit/00d4b78221) [#63960](https://github.com/vllm-project/vllm/pull/63960)
  [Rust Frontend] Count gpt-oss reasoning tokens like Python (#63960)
  _Files: `rust/src/chat/src/output/harmony/mod.rs`, `rust/src/chat/src/output/harmony/tests.rs`_
- **2026-10-28** [`65de04f8b7`](https://github.com/vllm-project/vllm/commit/65de04f8b7) [#63963](https://github.com/vllm-project/vllm/pull/63963)
  [Rust Frontend] Accept list-form chat templates like Transformers (#63963)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/renderer/hf/mod.rs`, `rust/src/text/src/backend/hf/config.rs`, `rust/src/text/src/backend/hf/mod.rs`_
- **2026-10-27** [`e96b490b12`](https://github.com/vllm-project/vllm/commit/e96b490b12) [#63989](https://github.com/vllm-project/vllm/pull/63989)
  [Bugfix][Kimi-K3] Reserve KDA prefill workspace before profiling (#63989)
  _Files: `vllm/models/kimi_k3/nvidia/kda.py`_
- **2026-10-27** [`a94c4481e0`](https://github.com/vllm-project/vllm/commit/a94c4481e0) [#63707](https://github.com/vllm-project/vllm/pull/63707)
  [Bugfix][Rust Frontend] Bump fastokens to 0.3.5 (#63707)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/tokenizer/src/hf.rs`_
- **2026-10-27** [`ca8dbccf20`](https://github.com/vllm-project/vllm/commit/ca8dbccf20) [#63999](https://github.com/vllm-project/vllm/pull/63999)
  [Bugfix] Forward launch grid to Triton kernel overrides (#63999)
  _Files: `tests/model_executor/test_triton_dispatcher.py`, `vllm/triton_utils/dispatcher.py`_
- **2026-10-27** [`de096755ad`](https://github.com/vllm-project/vllm/commit/de096755ad) [#60991](https://github.com/vllm-project/vllm/pull/60991)
  [Bugfix] Fuse GLM-5.3 KDA q|k|v convs into one conv1d parameter (#60991)
  _Files: `tests/models/glm5next/test_kda_conv_weight_refit.py`, `tests/models/glm5next/test_kda_recurrent.py`, `vllm/models/glm5next/common/kda.py`, `vllm/models/glm5next/common/model.py`_
- **2026-10-27** [`cebcc5d8c7`](https://github.com/vllm-project/vllm/commit/cebcc5d8c7) [#63548](https://github.com/vllm-project/vllm/pull/63548)
  [Bugfix] Keep MRV2 model state in the runtime pool under sleep mode (#63548)
  _Files: `tests/basic_correctness/memory/sleep_mode/test_sleep_mode.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-10-27** [`8701c9b751`](https://github.com/vllm-project/vllm/commit/8701c9b751) [#55112](https://github.com/vllm-project/vllm/pull/55112)
  [Bugfix][Core] Copy every overlaid KV view in copy_kv_cache_blocks_inplace (#55112)
  _Files: `tests/v1/worker/test_attn_utils.py`, `vllm/v1/worker/utils.py`_
- **2026-10-27** [`5b7742a13f`](https://github.com/vllm-project/vllm/commit/5b7742a13f) [#63154](https://github.com/vllm-project/vllm/pull/63154)
  [Bugfix][MRV2] Release the warmup memory cached on the capture streams (#63154)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-10-26** [`eb703fbb3d`](https://github.com/vllm-project/vllm/commit/eb703fbb3d) [#45188](https://github.com/vllm-project/vllm/pull/45188)
  [BugFix] [Build] Fix for where setup.py fails with MAX_JOBS invalid literal error (#45188)
  _Files: `setup.py`_
- **2026-10-26** [`3f45273050`](https://github.com/vllm-project/vllm/commit/3f45273050) [#55669](https://github.com/vllm-project/vllm/pull/55669)
  [Bugfix][Tool Parser] Anchor Jamba streamed tool arguments to what was sent (#55669)
  _Files: `tests/tool_parsers/test_jamba_tool_parser.py`, `vllm/tool_parsers/jamba_tool_parser.py`_
- **2026-10-26** [`eca54bd1d9`](https://github.com/vllm-project/vllm/commit/eca54bd1d9) [#60968](https://github.com/vllm-project/vllm/pull/60968)
  [Bugfix][Tool Parser] Keep Step3 parameter values that contain '<' (#60968)
  _Files: `tests/tool_parsers/test_step3_tool_parser.py`, `vllm/tool_parsers/step3_tool_parser.py`_
- **2026-10-26** [`20bf65ad33`](https://github.com/vllm-project/vllm/commit/20bf65ad33) [#61128](https://github.com/vllm-project/vllm/pull/61128)
  [Bugfix][Rust Frontend] Read the text config under `thinker_config` (#61128)
  _Files: `rust/src/text/src/backend/hf/config.rs`_
- **2026-10-26** [`9da5ba7e49`](https://github.com/vllm-project/vllm/commit/9da5ba7e49) [#47840](https://github.com/vllm-project/vllm/pull/47840)
  [Rust Frontend] Make HTTP request body limit configurable via VLLM_HTTP_MAX_REQUEST_BODY_SIZE (#47840)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/server/src/config.rs`, `rust/src/server/src/lib.rs` _+3 more__
- **2026-10-26** [`7f56f453ed`](https://github.com/vllm-project/vllm/commit/7f56f453ed) [#57926](https://github.com/vllm-project/vllm/pull/57926)
  [Bugfix][Core][MRV2] Profile the sampler with the params the warm-up actually uses (#57926)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-10-26** [`51d43b3683`](https://github.com/vllm-project/vllm/commit/51d43b3683) [#61792](https://github.com/vllm-project/vllm/pull/61792)
  [Test][UMBP][4/10] Cover async lookup, hybrid cache, events, and metrics (#61792)
  _Files: `tests/v1/kv_connector/unit/test_umbp_async_lookup.py`, `tests/v1/kv_connector/unit/test_umbp_core.py`, `tests/v1/kv_connector/unit/test_umbp_events.py`, `tests/v1/kv_connector/unit/test_umbp_hybrid.py`_
- **2026-10-26** [`2a2717d9b8`](https://github.com/vllm-project/vllm/commit/2a2717d9b8) [#63531](https://github.com/vllm-project/vllm/pull/63531)
  [XPU] Fix Kimi-Linear model dispatch (#63531)
  _Files: `tests/models/test_registry.py`, `vllm/models/kimi_k3/__init__.py`_
- **2026-10-26** [`7128f568ac`](https://github.com/vllm-project/vllm/commit/7128f568ac) [#58243](https://github.com/vllm-project/vllm/pull/58243)
  [Bugfix][MRV2] Reserve encoder graph memory without decoder graphs (#58243)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2_cudagraph_profiling.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu_worker.py`_

## Scheduler / Engine  (34 commits)

- **2026-11-02** [`6ad164f7a6`](https://github.com/vllm-project/vllm/commit/6ad164f7a6) [#64838](https://github.com/vllm-project/vllm/pull/64838)
  [Mamba] Postpone --mamba-cache-mode removal to v0.34.0 (#64838)
  _Files: `vllm/engine/arg_utils.py`_
- **2026-11-02** [`fa62ea99c1`](https://github.com/vllm-project/vllm/commit/fa62ea99c1) [#64294](https://github.com/vllm-project/vllm/pull/64294)
  [Bugfix][Rust Frontend][ZMQ] Run ZMQ transport I/O on the dedicated runtime (#64294)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/tests/client.rs`_
- **2026-11-02** [`785b0e4822`](https://github.com/vllm-project/vllm/commit/785b0e4822) [#64265](https://github.com/vllm-project/vllm/pull/64265)
  [Rust Frontend] Run utility calls to completion when the caller is cancelled (#64265)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/tests/client.rs`_
- **2026-11-02** [`90cd144054`](https://github.com/vllm-project/vllm/commit/90cd144054) [#64597](https://github.com/vllm-project/vllm/pull/64597)
  [CI] Enroll the remaining Engine and Basic Correctness jobs in automatic sharding (17 jobs) (#64597)
  _Files: `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/engine.yaml`_
- **2026-10-31** [`e318ac0979`](https://github.com/vllm-project/vllm/commit/e318ac0979) [#63842](https://github.com/vllm-project/vllm/pull/63842)
  [Perf][Frontend] Compute prompt block hashes in the Rust frontend (#63842)
  _Files: `.buildkite/test_areas/misc.yaml`, `docker/Dockerfile.cpu`, `rust/Cargo.lock`, `rust/src/engine-core-client/Cargo.toml` _+16 more__
- **2026-10-31** [`5a233286c6`](https://github.com/vllm-project/vllm/commit/5a233286c6) [#62967](https://github.com/vllm-project/vllm/pull/62967)
  [Bugfix][gRPC] Drain in-flight RPCs and engine work within --shutdown-timeout (#62967)
  _Files: `tests/entrypoints/launchers/test_grpc_shutdown.py`, `vllm/entrypoints/launchers/grpc_server.py`_
- **2026-10-31** [`c7a683bde5`](https://github.com/vllm-project/vllm/commit/c7a683bde5) [#64675](https://github.com/vllm-project/vllm/pull/64675)
  [Bugfix][Parser] Parse closed Qwen3 tool parameters once while streaming (#64675)
  _Files: `tests/parser/engine/test_qwen3.py`, `vllm/parser/qwen3.py`_
- **2026-10-30** [`4c38b653af`](https://github.com/vllm-project/vllm/commit/4c38b653af) [#64457](https://github.com/vllm-project/vllm/pull/64457)
  [Bugfix][Core] Keep offline DP ranks' collectives aligned with async scheduling (#64457)
  _Files: `tests/v1/engine/test_llm_engine.py`, `vllm/v1/engine/core_client.py`, `vllm/v1/engine/llm_engine.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-10-30** [`d731ff9280`](https://github.com/vllm-project/vllm/commit/d731ff9280) [#46335](https://github.com/vllm-project/vllm/pull/46335)
  [Doc] Fix %% rendering in CLI reference for --safetensors-load-strategy (#46335)
  _Files: `vllm/config/load.py`, `vllm/engine/arg_utils.py`_
- **2026-10-30** [`5cae6fd0c9`](https://github.com/vllm-project/vllm/commit/5cae6fd0c9) [#64232](https://github.com/vllm-project/vllm/pull/64232)
  [Rust Frontend] Log one structured access log event per HTTP response (#64232)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/server/examples/external_engine_openai_qwen.rs` _+8 more__
- **2026-10-30** [`a23fd99034`](https://github.com/vllm-project/vllm/commit/a23fd99034) [#64222](https://github.com/vllm-project/vllm/pull/64222)
  [Rust Frontend] Support --root-path (#64222)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/server/examples/external_engine_openai_qwen.rs` _+4 more__
- **2026-10-30** [`2b313cd97b`](https://github.com/vllm-project/vllm/commit/2b313cd97b) [#64512](https://github.com/vllm-project/vllm/pull/64512)
  [Rust Frontend] Export UMBP connector transfer metrics like Python (#64512)
  _Files: `rust/src/engine-core-client/src/metrics.rs`, `rust/src/engine-core-client/src/protocol/stats.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py` _+1 more__
- **2026-10-30** [`8559100040`](https://github.com/vllm-project/vllm/commit/8559100040) [#64451](https://github.com/vllm-project/vllm/pull/64451)
  [Rust Frontend] Support hybrid and external DP LB in `vllm-rs serve` (#64451)
  _Files: `rust/README.md`, `rust/src/bench/src/mm_processor.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+8 more__
- **2026-10-30** [`c20fc8a857`](https://github.com/vllm-project/vllm/commit/c20fc8a857) [#64450](https://github.com/vllm-project/vllm/pull/64450)
  [Rust Frontend] Let the handshake owner serve a range of DP ranks (#64450)
  _Files: `rust/src/bench/src/mm_processor.rs`, `rust/src/chat/examples/external_engine_chat_qwen.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+15 more__
- **2026-10-30** [`aa85ff7f13`](https://github.com/vllm-project/vllm/commit/aa85ff7f13) [#64449](https://github.com/vllm-project/vllm/pull/64449)
  [Bugfix][Rust Frontend] Send the DP rendezvous in coordinated-DP INIT (#64449)
  _Files: `rust/src/engine-core-client/src/protocol/handshake.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/transport.rs`, `rust/src/engine-core-client/src/transport/dp_rendezvous.rs`_
- **2026-10-30** [`c82702543c`](https://github.com/vllm-project/vllm/commit/c82702543c) [#64285](https://github.com/vllm-project/vllm/pull/64285)
  [XPU][CI] Enable streaming input e2e test on XPU (#64285)
  _Files: `.buildkite/intel_jobs/engine_intel.yaml`, `tests/v1/e2e/general/test_streaming_input.py`_
- **2026-10-29** [`4541fcdd83`](https://github.com/vllm-project/vllm/commit/4541fcdd83) [#38741](https://github.com/vllm-project/vllm/pull/38741)
  [Doc] Add Scheduler section to V1 architecture overview (#38741)
  _Files: `docs/design/arch_overview.md`_
- **2026-10-29** [`974927f804`](https://github.com/vllm-project/vllm/commit/974927f804) [#58780](https://github.com/vllm-project/vllm/pull/58780)
  [Bugfix][Parser] Stream DeepSeek V4/V3.2 string tool arguments incrementally (#58780)
  _Files: `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_deepseek_v41.py`, `tests/tool_parsers/test_deepseekv32_tool_parser.py`, `tests/tool_parsers/test_deepseekv4_tool_parser.py` _+3 more__
- **2026-10-28** [`d482020608`](https://github.com/vllm-project/vllm/commit/d482020608) [#63827](https://github.com/vllm-project/vllm/pull/63827)
  [Bugfix][Core] Defer async KV loads on HiSparse decoders until in-flight steps finish (#63827)
  _Files: `tests/v1/core/test_deferred_block_free.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-28** [`9f0893f1ad`](https://github.com/vllm-project/vllm/commit/9f0893f1ad) [#64348](https://github.com/vllm-project/vllm/pull/64348)
  [CI][Bugfix] Fix flaky port race in test_coordination_store_held_only_by_the_online_dp_master (#64348)
  _Files: `tests/v1/engine/test_core_engine_actor_manager.py`_
- **2026-10-28** [`f60edccd00`](https://github.com/vllm-project/vllm/commit/f60edccd00) [#64177](https://github.com/vllm-project/vllm/pull/64177)
  [Bugfix] Omit null `annotations` and `usage.prompt_tokens_details` in chat completions (#64177)
  _Files: `tests/entrypoints/openai/completion/test_completion_text_offset.py`, `tests/entrypoints/openai/test_tool_choice_content_none.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/serve/engine/protocol.py`_
- **2026-10-28** [`68eca9af01`](https://github.com/vllm-project/vllm/commit/68eca9af01) [#63962](https://github.com/vllm-project/vllm/pull/63962)
  [Rust Frontend] Export vllm:num_requests_kv_fetch_by_stage like Python (#63962)
  _Files: `rust/src/engine-core-client/src/metrics.rs`, `rust/src/engine-core-client/src/protocol/stats.rs`, `rust/src/llm/src/log_stats.rs`, `rust/src/metrics/src/scheduler.rs`_
- **2026-10-28** [`9df11cf608`](https://github.com/vllm-project/vllm/commit/9df11cf608) [#63959](https://github.com/vllm-project/vllm/pull/63959)
  [Rust Frontend] Export vllm:engine_sleep_state like Python (#63959)
  _Files: `rust/src/engine-core-client/examples/external_engine_utility_call.rs`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/metrics.rs` _+6 more__
- **2026-10-27** [`4d95f222e6`](https://github.com/vllm-project/vllm/commit/4d95f222e6) [#61258](https://github.com/vllm-project/vllm/pull/61258)
  [Feature][Core] Enable best-effort NUMA binding by default (#61258)
  _Files: `docs/configuration/optimization.md`, `tests/engine/test_arg_utils.py`, `tests/utils_/test_numa_utils.py`, `tests/utils_/test_system_utils.py` _+6 more__
- **2026-10-27** [`405276b8f0`](https://github.com/vllm-project/vllm/commit/405276b8f0) [#63709](https://github.com/vllm-project/vllm/pull/63709)
  [Rust Frontend] Detect Lark grammars like the Python engine (#63709)
  _Files: `rust/src/chat/src/output/structural_tag.rs`_
- **2026-10-27** [`803bc13cf9`](https://github.com/vllm-project/vllm/commit/803bc13cf9) [#62312](https://github.com/vllm-project/vllm/pull/62312)
  [Rust Frontend] Add --reasoning-effort-map to rewrite request reasoning efforts (#62312)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/lib.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+5 more__
- **2026-10-27** [`984a4181de`](https://github.com/vllm-project/vllm/commit/984a4181de) [#63763](https://github.com/vllm-project/vllm/pull/63763)
  [Rust Frontend] Keep completions top_logprobs and prompt_logprobs in the engine's order like Python (#63763)
  _Files: `rust/Cargo.toml`, `rust/src/server/src/routes/openai/utils/logprobs.rs`, `rust/src/server/src/routes/openai/utils/types.rs`_
- **2026-10-27** [`dacd7e2cb8`](https://github.com/vllm-project/vllm/commit/dacd7e2cb8) [#63771](https://github.com/vllm-project/vllm/pull/63771)
  [Rust Frontend] Forward profiler_kwargs from /start_profile (#63771)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/server/src/routes/profile.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-10-27** [`c56cdbea15`](https://github.com/vllm-project/vllm/commit/c56cdbea15) [#60856](https://github.com/vllm-project/vllm/pull/60856)
  [Bugfix][Rust Frontend] Decode current NIXL connector stats (#60856)
  _Files: `rust/src/engine-core-client/src/metrics.rs`, `rust/src/engine-core-client/src/protocol/stats.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py` _+1 more__
- **2026-10-27** [`05a303fdc8`](https://github.com/vllm-project/vllm/commit/05a303fdc8) [#62570](https://github.com/vllm-project/vllm/pull/62570)
  [Core][Frontend] Process checkpoint lifecycle with HTTP prepare/status/resume (#62570)
  _Files: `docs/serving/online_serving/README.md`, `docs/usage/security.md`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/protocol/utility.rs` _+14 more__
- **2026-10-27** [`4bb600439d`](https://github.com/vllm-project/vllm/commit/4bb600439d) [#63765](https://github.com/vllm-project/vllm/pull/63765)
  [Rust Frontend] Report the engine's VllmConfig in /server_info (#63765)
  _Files: `rust/src/engine-core-client/src/mock_engine.rs`, `rust/src/engine-core-client/src/protocol/handshake.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py` _+4 more__
- **2026-10-27** [`3ea7bd6bc5`](https://github.com/vllm-project/vllm/commit/3ea7bd6bc5) [#63767](https://github.com/vllm-project/vllm/pull/63767)
  [Rust Frontend] Export request metric series at startup like Python (#63767)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/llm/src/lib.rs`, `rust/src/llm/src/request_metrics.rs`, `rust/src/llm/tests/generate.rs`_
- **2026-10-26** [`2383ff0014`](https://github.com/vllm-project/vllm/commit/2383ff0014) [#62734](https://github.com/vllm-project/vllm/pull/62734)
  [Fast Start] Detect weight cache daemon exit in zero-copy engines (#62734)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py`_
- **2026-10-26** [`ee65d02902`](https://github.com/vllm-project/vllm/commit/ee65d02902) [#62456](https://github.com/vllm-project/vllm/pull/62456)
  [Rust Frontend] Select one structured outputs backend for every route (#62456)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/structural_tag.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+11 more__

## Multimodal  (32 commits)

- **2026-11-02** [`24d7bc9aab`](https://github.com/vllm-project/vllm/commit/24d7bc9aab) [#64594](https://github.com/vllm-project/vllm/pull/64594)
  [CI] Enroll the remaining Models (basic, multimodal, language) jobs in automatic sharding (22 jobs) (#64594)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_language.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-10-30** [`6a95c89c37`](https://github.com/vllm-project/vllm/commit/6a95c89c37) [#64618](https://github.com/vllm-project/vllm/pull/64618)
  [Multimodal] Cache PyNvVideoCodec decoder caps (#64618)
  _Files: `tests/multimodal/test_video.py`, `vllm/multimodal/video_decoders/pynvvideocodec.py`_
- **2026-10-30** [`8472c01d81`](https://github.com/vllm-project/vllm/commit/8472c01d81) [#64495](https://github.com/vllm-project/vllm/pull/64495)
  [Bugfix] Preserve multimodal processor-cache hits during request eviction (#64495)
  _Files: `docs/configuration/optimization.md`, `tests/entrypoints/multimodal/openai/chat_completion/test_vision.py`, `tests/models/multimodal/processing/test_common.py`, `tests/utils_/test_cache.py` _+3 more__
- **2026-10-30** [`b8141bd33e`](https://github.com/vllm-project/vllm/commit/b8141bd33e) [#64635](https://github.com/vllm-project/vllm/pull/64635)
  [CI] Continue automatic PyTorch Fullgraph sharding (#64635)
  _Files: `.buildkite/test_areas/pytorch.yaml`, `tests/compile/fullgraph/test_full_graph.py`, `tests/compile/fullgraph/test_multimodal_compile.py`_
- **2026-10-30** [`e7aad419de`](https://github.com/vllm-project/vllm/commit/e7aad419de) [#61973](https://github.com/vllm-project/vllm/pull/61973)
  [Bugfix] Preserve batch audio handler error status codes (#61973)
  _Files: `tests/entrypoints/launchers/test_run_batch.py`, `vllm/entrypoints/launchers/run_batch.py`_
- **2026-10-30** [`335dd77b09`](https://github.com/vllm-project/vllm/commit/335dd77b09) [#64644](https://github.com/vllm-project/vllm/pull/64644)
  [CI] Fix mypy errors in test_glm5next.py (#64644)
  _Files: `tests/models/multimodal/processing/test_glm5next.py`_
- **2026-10-30** [`83bae4923f`](https://github.com/vllm-project/vllm/commit/83bae4923f) [#64342](https://github.com/vllm-project/vllm/pull/64342)
  [CI] Fix mypy multimodels tests folder (#64342)
  _Files: `tests/models/multimodal/conftest.py`, `tests/models/multimodal/generation/test_common.py`, `tests/models/multimodal/generation/test_maverick.py`, `tests/models/multimodal/generation/test_nemotron_parse_35.py` _+54 more__
- **2026-10-29** [`9957f74617`](https://github.com/vllm-project/vllm/commit/9957f74617) [#64362](https://github.com/vllm-project/vllm/pull/64362)
  [Bugfix] Add chat template fallback for OpenVLA (#64362)
  _Files: `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/processing/test_openvla.py`, `vllm/transformers_utils/chat_templates/registry.py`, `vllm/transformers_utils/chat_templates/template_openvla.jinja`_
- **2026-10-29** [`604b961640`](https://github.com/vllm-project/vllm/commit/604b961640) [#53011](https://github.com/vllm-project/vllm/pull/53011)
  [Bugfix] Avoid eager torch.compile in Kimi K2.5 vision helper (#53011)
  _Files: `vllm/model_executor/models/kimi_k25_vit.py`_
- **2026-10-29** [`5a4f307d9c`](https://github.com/vllm-project/vllm/commit/5a4f307d9c) [#57924](https://github.com/vllm-project/vllm/pull/57924)
  [MM] Move Nemotron VL image normalization to device (#57924)
  _Files: `docs/design/mm_processing.md`, `tests/models/multimodal/test_nano_nemotron_vl.py`, `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/transformers_utils/processors/nano_nemotron_vl.py`_
- **2026-10-29** [`cf3f6405b8`](https://github.com/vllm-project/vllm/commit/cf3f6405b8) [#63218](https://github.com/vllm-project/vllm/pull/63218)
  [Bugfix] Default Nemotron Omni mamba_ssm_cache_dtype to float32 (#63218)
  _Files: `tests/models/multimodal/test_nano_nemotron_vl.py`, `vllm/model_executor/models/config.py`_
- **2026-10-29** [`d83a7df60a`](https://github.com/vllm-project/vllm/commit/d83a7df60a) [#58468](https://github.com/vllm-project/vllm/pull/58468)
  [Model] Update RADIO vision encoder to match the current Transformers version (#58468)
  _Files: `tests/models/multimodal/pooling/test_radio.py`, `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/nemotron_parse3_5.py`, `vllm/model_executor/models/radio.py` _+1 more__
- **2026-10-29** [`34091a07c7`](https://github.com/vllm-project/vllm/commit/34091a07c7) [#59938](https://github.com/vllm-project/vllm/pull/59938)
  [XPU] use multimodal_rotary_embedding xpu kernel for mrope (#59938)
  _Files: `vllm/model_executor/layers/rotary_embedding/mrope.py`_
- **2026-10-29** [`3966924d56`](https://github.com/vllm-project/vllm/commit/3966924d56) [#64105](https://github.com/vllm-project/vllm/pull/64105)
  [BugFix]/minicpm ocr downsample mode (#64105)
  _Files: `tests/models/multimodal/processing/test_minicpm_ocr.py`, `vllm/model_executor/models/minicpm_ocr.py`_
- **2026-10-29** [`38b1775405`](https://github.com/vllm-project/vllm/commit/38b1775405) [#64228](https://github.com/vllm-project/vllm/pull/64228)
  [XPU][UT] reuse test_phi3v.py::test_models_text on XPU (#64228)
  _Files: `tests/models/multimodal/pooling/test_phi3v.py`_
- **2026-10-29** [`36d4ef654a`](https://github.com/vllm-project/vllm/commit/36d4ef654a) [#64387](https://github.com/vllm-project/vllm/pull/64387)
  [CI] Import the merge-base commit's image cache in PR builds (#64387)
  _Files: `.buildkite/image_build/image_build.sh`_
- **2026-10-28** [`c91ab83dce`](https://github.com/vllm-project/vllm/commit/c91ab83dce) [#64287](https://github.com/vllm-project/vllm/pull/64287)
  [Model] Remove Keye-VL and Keye-VL-1.5 (#64287)
  _Files: `docs/models/supported_models.md`, `examples/generate/multimodal/vision_language_multi_image_offline.py`, `examples/generate/multimodal/vision_language_offline.py`, `tests/model_executor/test_keye_mrope.py` _+6 more__
- **2026-10-28** [`ab0e5ef795`](https://github.com/vllm-project/vllm/commit/ab0e5ef795) [#59198](https://github.com/vllm-project/vllm/pull/59198)
  [Build] keep CUDA PyTorch wheels aligned with image (#59198)
  _Files: `docker/Dockerfile`_
- **2026-10-28** [`76c4ad2f15`](https://github.com/vllm-project/vllm/commit/76c4ad2f15) [#64091](https://github.com/vllm-project/vllm/pull/64091)
  [Bugfix][Multimodal] Fix DeepSeek-OCR zero-sum patch guard in _encode… (#64091)
  _Files: `tests/models/multimodal/generation/test_deepseek_ocr.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/deepseek_ocr2.py`_
- **2026-10-28** [`26302eb938`](https://github.com/vllm-project/vllm/commit/26302eb938) [#57411](https://github.com/vllm-project/vllm/pull/57411)
  [Security] Bound FunAudioChat runtime audio to the profiled duration (#57411)
  _Files: `tests/models/multimodal/processing/test_funaudiochat.py`, `vllm/model_executor/models/funaudiochat.py`_
- **2026-10-28** [`7e3e3f6ab6`](https://github.com/vllm-project/vllm/commit/7e3e3f6ab6) [#64189](https://github.com/vllm-project/vllm/pull/64189)
  [CI][Bugfix] Pin the ColUltraVBERT test checkpoint to the revision vLLM supports (#64189)
  _Files: `tests/models/multimodal/pooling/test_colultravbert.py`, `tests/models/registry.py`_
- **2026-10-28** [`9bc1c8b4fe`](https://github.com/vllm-project/vllm/commit/9bc1c8b4fe) [#64180](https://github.com/vllm-project/vllm/pull/64180)
  [Doc] Add autotrust/JEV-27B-VL multimodal recipe (vLLM >= 0.32.0) (#64180)
  _Files: `recipes/models/autotrust/JEV-27B-VL.yaml`_
- **2026-10-27** [`a9b727a612`](https://github.com/vllm-project/vllm/commit/a9b727a612) [#63274](https://github.com/vllm-project/vllm/pull/63274)
  [UX] Remove `--hf-overrides` necessity for Qwen3-ASR-ForceAligner (#63274)
  _Files: `docs/models/pooling_models/token_classify.md`, `examples/pooling/token_classify/forced_alignment_offline.py`, `tests/models/multimodal/pooling/test_qwen3_asr_forced_aligner.py`, `vllm/model_executor/models/qwen3_asr_forced_aligner.py` _+1 more__
- **2026-10-27** [`40fe396b60`](https://github.com/vllm-project/vllm/commit/40fe396b60) [#64032](https://github.com/vllm-project/vllm/pull/64032)
  [Bugfix][Multimodal] Return 400 when local media access is disabled (#64032)
  _Files: `tests/entrypoints/scale_out/render/test_render_multimodal.py`, `tests/multimodal/media/test_connector.py`, `vllm/multimodal/media/connector.py`_
- **2026-10-27** [`a657fd6082`](https://github.com/vllm-project/vllm/commit/a657fd6082) [#62497](https://github.com/vllm-project/vllm/pull/62497)
  [Test][Multimodal] Add end-to-end CLI test for vllm bench mm-processor (#62497)
  _Files: `tests/benchmarks/test_mm_processor_cli.py`_
- **2026-10-27** [`d81d6a93c9`](https://github.com/vllm-project/vllm/commit/d81d6a93c9) [#63433](https://github.com/vllm-project/vllm/pull/63433)
  [Bugfix][Multimodal] Return 400 for corrupt AVIF and BLP images (#63433)
  _Files: `tests/multimodal/media/test_image.py`, `vllm/multimodal/media/image.py`_
- **2026-10-26** [`537a79f0fc`](https://github.com/vllm-project/vllm/commit/537a79f0fc) [#63422](https://github.com/vllm-project/vllm/pull/63422)
  [CI] Add missing `&&` in the Multi-Modal Models (Standard) 3 command (#63422)
  _Files: `.buildkite/intel_jobs/models_multimodal_intel.yaml`_
- **2026-10-26** [`373614f66d`](https://github.com/vllm-project/vllm/commit/373614f66d) [#57368](https://github.com/vllm-project/vllm/pull/57368)
  [Bugfix][Multimodal] Release consumed MRV2 CPU inputs (#57368)
  _Files: `tests/models/multimodal/generation/test_memory_leak.py`, `tests/v1/core/test_scheduler.py`, `tests/v1/worker/test_encoder_runner.py`, `vllm/v1/core/sched/output.py` _+3 more__
- **2026-10-26** [`ffcabb8c7a`](https://github.com/vllm-project/vllm/commit/ffcabb8c7a) [#58768](https://github.com/vllm-project/vllm/pull/58768)
  [docker] add vllm-openai-efa target (#58768)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/publish-release-images.sh`, `docker/Dockerfile`, `docker/Dockerfile.efa` _+2 more__
- **2026-10-26** [`d7aa93b378`](https://github.com/vllm-project/vllm/commit/d7aa93b378) [#63661](https://github.com/vllm-project/vllm/pull/63661)
  [Rust Frontend] Update multimodal video frames sampling API (#63661)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/multimodal/models/muse_spark.rs`_
- **2026-10-26** [`4b1c04e76f`](https://github.com/vllm-project/vllm/commit/4b1c04e76f) [#63651](https://github.com/vllm-project/vllm/pull/63651)
  [Doc] Update Muse Spark Open  (#63651)
  _Files: `docs/models/supported_models.md`, `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/multimodal/models/muse_spark.rs`, `tests/models/registry.py`_
- **2026-10-26** [`d7595a7678`](https://github.com/vllm-project/vllm/commit/d7595a7678) [#63629](https://github.com/vllm-project/vllm/pull/63629)
  [Bugfix] Fix MOSS-Audio meta initialization (#63629)
  _Files: `tests/models/multimodal/processing/test_moss_audio.py`, `vllm/model_executor/models/moss_audio.py`_

## Models  (30 commits)

- **2026-11-02** [`3fbc8d8b4f`](https://github.com/vllm-project/vllm/commit/3fbc8d8b4f) [#65118](https://github.com/vllm-project/vllm/pull/65118)
  [Bugfix][Mistral] Keep skip_special_tokens for MistralTokenizer in Responses / legacy parser path (#65118)
  _Files: `tests/parser/mistral/test_tool_calls.py`, `vllm/parser/mistral.py`_
- **2026-11-02** [`f4aeb1cb8b`](https://github.com/vllm-project/vllm/commit/f4aeb1cb8b) [#64920](https://github.com/vllm-project/vllm/pull/64920)
  [Model] Muse Glimmer: reuse in-tree RMSNorm / GemmaRMSNorm (#64920)
  _Files: `vllm/model_executor/models/muse_glimmer.py`_
- **2026-11-02** [`5c5c6f788e`](https://github.com/vllm-project/vllm/commit/5c5c6f788e) [#65005](https://github.com/vllm-project/vllm/pull/65005)
  [Docs][Model] Add Parakeet TDT transcription support via plugin (#65005)
  _Files: `docs/models/supported_models.md`, `docs/usage/v1_guide.md`_
- **2026-11-02** [`b10a8c2c81`](https://github.com/vllm-project/vllm/commit/b10a8c2c81) [#65045](https://github.com/vllm-project/vllm/pull/65045)
  [Model] Remove redundant Muse Spark configuration overrides (#65045)
  _Files: `vllm/models/muse_spark/nvidia/model.py`_
- **2026-11-02** [`410ab341a8`](https://github.com/vllm-project/vllm/commit/410ab341a8) [#63992](https://github.com/vllm-project/vllm/pull/63992)
  [Bugfix][Tool Parser] Parse bare FunctionGemma arguments and stream them as valid JSON (#63992)
  _Files: `tests/entrypoints/tool_parsers/test_functiongemma_tool_parser.py`, `tests/tool_parsers/test_functiongemma_tool_parser.py`, `vllm/tool_parsers/functiongemma_tool_parser.py`_
- **2026-11-02** [`c215f14835`](https://github.com/vllm-project/vllm/commit/c215f14835) [#64971](https://github.com/vllm-project/vllm/pull/64971)
  [Bugfix][Frontend] Fix tool_reference results on DeepSeek V4.1 and /v1/messages (#64971)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/scale_out/render/test_render.py`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/entrypoints/anthropic/serving.py` _+1 more__
- **2026-11-02** [`ea836290a7`](https://github.com/vllm-project/vllm/commit/ea836290a7) [#64816](https://github.com/vllm-project/vllm/pull/64816)
  [Perf][DSv4.1] Vectorize first-layer HC expansion copy (#64816)
  _Files: `tests/kernels/mhc/test_mhc_kernels.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`_
- **2026-11-01** [`b2d07f59c7`](https://github.com/vllm-project/vllm/commit/b2d07f59c7) [#64999](https://github.com/vllm-project/vllm/pull/64999)
  [Bugfix][GDN] Restore in_proj_ba overlap on CUDA (#64999)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/qwen3_5/test_gdn_ba_overlap.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-10-31** [`87cb835db2`](https://github.com/vllm-project/vllm/commit/87cb835db2) [#64869](https://github.com/vllm-project/vllm/pull/64869)
  [Misc] Allow weights mapper to transform weights (#64869)
  _Files: `tests/models/test_utils.py`, `vllm/model_executor/models/utils.py`, `vllm/model_executor/models/whisper.py`_
- **2026-10-31** [`10da92ff28`](https://github.com/vllm-project/vllm/commit/10da92ff28) [#63415](https://github.com/vllm-project/vllm/pull/63415)
  [Bugfix][Model] Make compile_mm_encoder work for RADIO/NaViT encoders (#63415)
  _Files: `vllm/model_executor/models/nemotron_parse3_5.py`, `vllm/model_executor/models/radio.py`_
- **2026-10-31** [`900b8b08e2`](https://github.com/vllm-project/vllm/commit/900b8b08e2) [#64650](https://github.com/vllm-project/vllm/pull/64650)
  [Perf][Qwen3.8] Add SM103 skinny GEMM plans for TP=1 (#64650)
  _Files: `vllm/models/qwen4_exp/nvidia/low_latency_gemm.py`_
- **2026-10-31** [`886b845ef1`](https://github.com/vllm-project/vllm/commit/886b845ef1) [#64215](https://github.com/vllm-project/vllm/pull/64215)
  [Model] Add NVIDIA Canary (nvidia/canary-1b-v2) speech-to-text support (#64215)
  _Files: `docs/models/supported_models.md`, `tests/entrypoints/speech_to_text/correctness/test_transcription_api_correctness.py`, `tests/models/registry.py`, `vllm/model_executor/models/canary.py` _+1 more__
- **2026-10-31** [`2b009fc6d1`](https://github.com/vllm-project/vllm/commit/2b009fc6d1) [#63098](https://github.com/vllm-project/vllm/pull/63098)
  [Feature][DSv4.1] Enable PCP with PP or DP (#63098)
  _Files: `tests/models/test_deepseek_v41_pcp.py`, `vllm/models/deepseek_v41/nvidia/model.py`_
- **2026-10-30** [`24420b7a34`](https://github.com/vllm-project/vllm/commit/24420b7a34) [#60218](https://github.com/vllm-project/vllm/pull/60218)
  [hw-agnostic] Opt-in infrastructure for OOT plugins (#60218)
  _Files: `docs/design/custom_op.md`, `tests/models/transformers/test_layer_registry.py`, `tests/models/transformers/test_layer_registry_e2e.py`, `vllm/model_executor/hw_agnostic/__init__.py` _+3 more__
- **2026-10-30** [`89a9a03710`](https://github.com/vllm-project/vllm/commit/89a9a03710) [#51953](https://github.com/vllm-project/vllm/pull/51953)
  [Bugfix][MRV2] Fix DiffusionGemma runtime OOM via tiled logits projection (#51953)
  _Files: `tests/v1/worker/test_gpu_diffusion_sampler.py`, `vllm/model_executor/models/diffusion_gemma.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/model_states/interface.py`_
- **2026-10-29** [`9a0f9b45df`](https://github.com/vllm-project/vllm/commit/9a0f9b45df) [#64019](https://github.com/vllm-project/vllm/pull/64019)
  [Bugfix][Pooling] Skip weight tying for omitted LM heads (#64019)
  _Files: `vllm/model_executor/models/utils.py`_
- **2026-10-29** [`5cdbd0520e`](https://github.com/vllm-project/vllm/commit/5cdbd0520e) [#64527](https://github.com/vllm-project/vllm/pull/64527)
  [Docs] Add Mistral-Large-4-1T-A52B recipe (#64527)
  _Files: `recipes/models/mistralai/Mistral-Large-4-1T-A52B.yaml`_
- **2026-10-29** [`914d61fc53`](https://github.com/vllm-project/vllm/commit/914d61fc53) [#64425](https://github.com/vllm-project/vllm/pull/64425)
  [Perf] Qwen3.5 GDN: overlap in_proj_ba with in_proj_qkvz on the aux stream (#64425)
  _Files: `tests/kernels/mamba/test_gdn_fused_mtp.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`, `vllm/models/qwen3_5/nvidia/model.py`_
- **2026-10-29** [`510d15c49e`](https://github.com/vllm-project/vllm/commit/510d15c49e) [#64506](https://github.com/vllm-project/vllm/pull/64506)
  [Bugfix][Model] Nemotron 3.5 Super VL: support the native transformers config (#64506)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/nano_nemotron_vl.py`_
- **2026-10-29** [`1ca0dfb976`](https://github.com/vllm-project/vllm/commit/1ca0dfb976) [#64481](https://github.com/vllm-project/vllm/pull/64481)
  [Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM100 (#64481)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`_
- **2026-10-29** [`3765000a37`](https://github.com/vllm-project/vllm/commit/3765000a37) [#64482](https://github.com/vllm-project/vllm/pull/64482)
  [Perf][Qwen3.8] Add SM100 skinny GEMM plans for TP=1 (#64482)
  _Files: `vllm/models/qwen4_exp/nvidia/low_latency_gemm.py`_
- **2026-10-28** [`d929755b7a`](https://github.com/vllm-project/vllm/commit/d929755b7a) [#64316](https://github.com/vllm-project/vllm/pull/64316)
  [Doc] DeepSeek-V4-Pro: add B200 InferenceX AgentX presets (#64316)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4-Pro.yaml`_
- **2026-10-27** [`90309f6b74`](https://github.com/vllm-project/vllm/commit/90309f6b74) [#60490](https://github.com/vllm-project/vllm/pull/60490)
  [Bugfix][Qwen4Exp] Reserve QSA indexer prefill workspace during memory profiling (#60490)
  _Files: `vllm/models/qwen4_exp/nvidia/qsa.py`_
- **2026-10-27** [`0232bb3060`](https://github.com/vllm-project/vllm/commit/0232bb3060) [#63768](https://github.com/vllm-project/vllm/pull/63768)
  [Rust Frontend] Accept parenthesized and name-only Gemma 4 tool calls like Python (#63768)
  _Files: `rust/src/parser/src/unified/gemma4.rs`_
- **2026-10-27** [`ace90aeb24`](https://github.com/vllm-project/vllm/commit/ace90aeb24) [#63762](https://github.com/vllm-project/vllm/pull/63762)
  [Rust Frontend] Separate DeepSeek V4 content blocks like deepseek-recipe (#63762)
  _Files: `rust/src/chat/src/renderer/deepseek.rs`, `rust/src/chat/src/renderer/deepseek_v4/tests.rs`, `rust/src/chat/src/renderer/deepseek_v41/tests.rs`_
- **2026-10-27** [`5d35ce3934`](https://github.com/vllm-project/vllm/commit/5d35ce3934) [#63812](https://github.com/vllm-project/vllm/pull/63812)
  [Frontend][Mistral] Forward response_format to mistral-common chat templating (#63812)
  _Files: `tests/entrypoints/serve/tokenize/test_serving_tokenization.py`, `tests/renderers/test_mistral.py`, `tests/tokenizers_/test_mistral.py`, `vllm/entrypoints/serve/tokenize/protocol.py` _+2 more__
- **2026-10-26** [`af6665b5dd`](https://github.com/vllm-project/vllm/commit/af6665b5dd) [#61994](https://github.com/vllm-project/vllm/pull/61994)
  [Spec Decode] Support PCP with DSpark for DeepSeek-V4.1 (#61994)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `tests/models/test_deepseek_v41_pcp.py`, `tests/v1/worker/test_gpu_pcp_manager.py`, `vllm/models/deepseek_v41/compressor.py` _+3 more__
- **2026-10-26** [`c84ff6b3f4`](https://github.com/vllm-project/vllm/commit/c84ff6b3f4) [#62219](https://github.com/vllm-project/vllm/pull/62219)
  [Kernel][Perf] Add H100 tuned configs for Llama-3.1-8B and Qwen3-8B to the batch-invariant matmul table (#62219)
  _Files: `vllm/model_executor/determinism/batch_invariant_configs.py`_
- **2026-10-26** [`0abec7309e`](https://github.com/vllm-project/vllm/commit/0abec7309e) [#62201](https://github.com/vllm-project/vllm/pull/62201)
  [Model] Add native support for Lfm2BidirectionalModel (#62201)
  _Files: `docs/models/pooling_models/embed.md`, `tests/models/language/pooling/test_embedding.py`, `tests/models/registry.py`, `vllm/model_executor/models/lfm2.py` _+1 more__
- **2026-10-26** [`41d9d1e14d`](https://github.com/vllm-project/vllm/commit/41d9d1e14d) [#61094](https://github.com/vllm-project/vllm/pull/61094)
  [Frontend] Add --reasoning-effort-map to rewrite request reasoning efforts (#61094)
  _Files: `docs/features/reasoning_outputs.md`, `tests/entrypoints/common/test_cli_args.py`, `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py` _+15 more__

## Disaggregation / PD  (25 commits)

- **2026-11-02** [`a9cf9df752`](https://github.com/vllm-project/vllm/commit/a9cf9df752) [#61764](https://github.com/vllm-project/vllm/pull/61764)
  [Bugfix][EC Connector] Allocate producer control ports at startup (#61764)
  _Files: `docs/features/ec_cpu_connector.md`, `tests/v1/ec_connector/integration/test_nixl_failure.py`, `tests/v1/ec_connector/unit/test_control.py`, `tests/v1/ec_connector/unit/test_scheduler_nixl_ctor.py` _+3 more__
- **2026-11-02** [`62c9b6263c`](https://github.com/vllm-project/vllm/commit/62c9b6263c) [#63971](https://github.com/vllm-project/vllm/pull/63971)
  [Bugfix][Mooncake] Let decodes reuse divergent local hybrid prefix hits (#63971)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-10-31** [`8b55f9195a`](https://github.com/vllm-project/vllm/commit/8b55f9195a) [#63416](https://github.com/vllm-project/vllm/pull/63416)
  [KV Connector][NIXL] Pair KV regions by layer for every transfer (#63416)
  _Files: `docs/design/nixl_kv_push_connector.md`, `docs/features/nixl_connector_compatibility.md`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py` _+7 more__
- **2026-10-30** [`be712f5601`](https://github.com/vllm-project/vllm/commit/be712f5601) [#64691](https://github.com/vllm-project/vllm/pull/64691)
  [RL] NCCL weight transfer: release cached memory after a weight update (#64691)
  _Files: `vllm/distributed/weight_transfer/nccl_engine.py`_
- **2026-10-30** [`5423fb8b93`](https://github.com/vllm-project/vllm/commit/5423fb8b93) [#63886](https://github.com/vllm-project/vllm/pull/63886)
  [Spec Decode][DSpark] Batch-sharded sequential block (#63886)
  _Files: `tests/distributed/test_pynccl.py`, `tests/v1/e2e/spec_decode/test_sharded_sampling.py`, `tests/v1/worker/test_gpu_batch_shard.py`, `vllm/distributed/device_communicators/pynccl.py` _+7 more__
- **2026-10-30** [`32b30dfe46`](https://github.com/vllm-project/vllm/commit/32b30dfe46) [#64617](https://github.com/vllm-project/vllm/pull/64617)
  [Recipe] Kimi-K3: add B300 AgentX aggregated Mooncake preset (#64617)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-30** [`8493b34b7b`](https://github.com/vllm-project/vllm/commit/8493b34b7b) [#62979](https://github.com/vllm-project/vllm/pull/62979)
  [Bugfix][HiSparse] Reserve in-flight imports' host pages at admission (#62979)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/distributed/kv_transfer/kv_connector/v1/hisparse/connector.py`, `vllm/v1/core/single_type_kv_cache_manager.py`, `vllm/v1/hisparse/coordinator.py`_
- **2026-10-29** [`8084f0624d`](https://github.com/vllm-project/vllm/commit/8084f0624d) [#64582](https://github.com/vllm-project/vllm/pull/64582)
  [Bugfix][KV Connector][NIXL] Fix Mamba region stride on block-outermost layouts (#64582)
  _Files: `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-29** [`aa738c38c3`](https://github.com/vllm-project/vllm/commit/aa738c38c3) [#64193](https://github.com/vllm-project/vllm/pull/64193)
  [KV Connector][Mooncake] Renew prefill KV leases from the decoder (#64193)
  _Files: `docs/features/mooncake_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-10-29** [`03098917ad`](https://github.com/vllm-project/vllm/commit/03098917ad) [#57022](https://github.com/vllm-project/vllm/pull/57022)
  [Bugfix] Fail loudly instead of no-op NCCL weight transfer (#57022)
  _Files: `tests/distributed/test_weight_transfer.py`, `vllm/distributed/weight_transfer/nccl_common.py`_
- **2026-10-29** [`31f173d26d`](https://github.com/vllm-project/vllm/commit/31f173d26d) [#57662](https://github.com/vllm-project/vllm/pull/57662)
  [Bugfix][NIXL] Dedup transfer regions by (base_addr, block_len) (#57662)
  _Files: `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-29** [`bfa4d6d2ad`](https://github.com/vllm-project/vllm/commit/bfa4d6d2ad) [#59934](https://github.com/vllm-project/vllm/pull/59934)
  [KV Connector] Support sleep mode with MooncakeStoreConnector (#59934)
  _Files: `tests/v1/kv_connector/unit/test_config.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-10-29** [`0c81a0371f`](https://github.com/vllm-project/vllm/commit/0c81a0371f) [#62905](https://github.com/vllm-project/vllm/pull/62905)
  [KV Connector][NIXL] Add a ucx_backend_params key for UCX backend init params (#62905)
  _Files: `docs/features/nixl_connector_usage.md`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-29** [`f79a3a7d48`](https://github.com/vllm-project/vllm/commit/f79a3a7d48) [#63513](https://github.com/vllm-project/vllm/pull/63513)
  [KV Connector] Mooncake store: skip padding in stored KV blocks (#63513)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_layout.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py` _+1 more__
- **2026-10-28** [`6cfb375fd6`](https://github.com/vllm-project/vllm/commit/6cfb375fd6) [#61793](https://github.com/vllm-project/vllm/pull/61793)
  [UMBP][5/10] Add MORI embedded DRAM runtime and transfer handling (#61793)
  _Files: `docs/features/README.md`, `docs/features/umbp_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_umbp_embedded.py`, `vllm/distributed/kv_transfer/kv_connector/factory.py` _+2 more__
- **2026-10-28** [`066d979934`](https://github.com/vllm-project/vllm/commit/066d979934) [#64230](https://github.com/vllm-project/vllm/pull/64230)
  [KV Connector][NIXL] Select push mode for NixlConnector via transfer_mode (#64230)
  _Files: `docs/design/nixl_kv_push_connector.md`, `tests/v1/kv_connector/unit/test_config.py`, `vllm/distributed/kv_transfer/kv_connector/factory.py`_
- **2026-10-28** [`2b678ac739`](https://github.com/vllm-project/vllm/commit/2b678ac739) [#62557](https://github.com/vllm-project/vllm/pull/62557)
  [RL] Support per-update source ranks for NCCL weight transfer (#62557)
  _Files: `.buildkite/test_areas/distributed.yaml`, `docs/training/weight_transfer/README.md`, `docs/training/weight_transfer/nccl.md`, `examples/rl/rlhf_nccl_multi_source.py` _+3 more__
- **2026-10-27** [`e1e77a279d`](https://github.com/vllm-project/vllm/commit/e1e77a279d) [#60960](https://github.com/vllm-project/vllm/pull/60960)
  [Bugfix] Bound prefix cache reuse by the first requested prompt score (#60960)
  _Files: `docs/training/prompt_token_id_logprobs.md`, `rust/src/server/src/routes/inference/generate.rs`, `rust/src/text/src/lower.rs`, `rust/src/text/src/lower/logprobs.rs` _+20 more__
- **2026-10-27** [`2897401370`](https://github.com/vllm-project/vllm/commit/2897401370) [#62478](https://github.com/vllm-project/vllm/pull/62478)
  [Perf][KV Connector][Mooncake] Vectorize transfer descriptor build (#62478)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-10-27** [`4ddc7aa40f`](https://github.com/vllm-project/vllm/commit/4ddc7aa40f) [#62317](https://github.com/vllm-project/vllm/pull/62317)
  [KV Connector][NIXL] Read only a group's own regions in hybrid SSM transfers (#62317)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-10-27** [`a5b257a34b`](https://github.com/vllm-project/vllm/commit/a5b257a34b) [#63064](https://github.com/vllm-project/vllm/pull/63064)
  [Docs][KV Connector] Document standalone Mooncake EGM deployment (#63064)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `examples/disaggregated/mooncake_store/egm_provider.py`_
- **2026-10-26** [`2841f08b4a`](https://github.com/vllm-project/vllm/commit/2841f08b4a) [#63142](https://github.com/vllm-project/vllm/pull/63142)
  [KVConnector][Mooncake] Coalesce descending block ids to reduce descriptor number for Mooncake TE (#63142)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-10-26** [`3e75ccba29`](https://github.com/vllm-project/vllm/commit/3e75ccba29) [#62330](https://github.com/vllm-project/vllm/pull/62330)
  [Bugfix][DCP] Finalize the NIXL DCP interleave size before profiling (#62330)
  _Files: `tests/models/test_initialization.py`, `tests/test_config.py`, `tests/v1/core/test_kv_cache_planning.py`, `tests/v1/core/utils.py` _+10 more__
- **2026-10-26** [`beeed65c10`](https://github.com/vllm-project/vllm/commit/beeed65c10) [#62242](https://github.com/vllm-project/vllm/pull/62242)
  [Bugfix][KV Connector] Report every transfer group as loaded in DecodeBenchConnector (#62242)
  _Files: `tests/v1/core/test_prefix_replay.py`, `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`_
- **2026-10-26** [`330c5bffee`](https://github.com/vllm-project/vllm/commit/330c5bffee) [#63224](https://github.com/vllm-project/vllm/pull/63224)
  [Bugfix][KV Events] Prevent replay truncation when the send queue fills (#63224)
  _Files: `tests/distributed/test_events.py`, `vllm/config/kv_events.py`, `vllm/distributed/kv_events.py`_

## Speculative Decoding  (22 commits)

- **2026-11-02** [`f451c6254f`](https://github.com/vllm-project/vllm/commit/f451c6254f) [#63870](https://github.com/vllm-project/vllm/pull/63870)
  [Rust Frontend][gRPC] Separate liveness from inference readiness (#63870)
  _Files: `docs/deployment/k8s.md`, `rust/README.md`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs` _+13 more__
- **2026-10-30** [`dd5f5eebd7`](https://github.com/vllm-project/vllm/commit/dd5f5eebd7) [#62111](https://github.com/vllm-project/vllm/pull/62111)
  [Bugfix] Fix multi-layer MTP module selection for Qwen3.5 and Qwen3-Next (#62111)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/models/test_qwen3_5_mtp_config.py`, `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_mtp.py` _+5 more__
- **2026-10-30** [`c8dbb1cb26`](https://github.com/vllm-project/vllm/commit/c8dbb1cb26) [#57770](https://github.com/vllm-project/vllm/pull/57770)
  [Perf][Spec Decode] Split-vocabulary Triton argmax for the DSpark greedy draft (#57770)
  _Files: `tests/v1/worker/test_gpu_gumbel_sample.py`, `vllm/v1/worker/gpu/sample/greedy_argmax.py`, `vllm/v1/worker/gpu/spec_decode/dspark/speculator.py`, `vllm/v1/worker/gpu/spec_decode/speculator.py`_
- **2026-10-30** [`b44a48cef1`](https://github.com/vllm-project/vllm/commit/b44a48cef1) [#59958](https://github.com/vllm-project/vllm/pull/59958)
  [Qwen4Exp] PLE disk offload (#59958)
  _Files: `docs/features/engram.md`, `tests/models/qwen4_exp/test_config.py`, `tests/models/qwen4_exp/test_ple.py`, `tests/test_config.py` _+4 more__
- **2026-10-30** [`322f90a2a3`](https://github.com/vllm-project/vllm/commit/322f90a2a3) [#63219](https://github.com/vllm-project/vllm/pull/63219)
  [Bugfix][Spec Decode] Per-request draft retention for structured output under PP (#63219)
  _Files: `.buildkite/test_areas/engine.yaml`, `tests/v1/e2e/spec_decode/draft_model/test_draft_model.py`, `tests/v1/e2e/spec_decode/draft_model/test_structured_output_pp.py`, `tests/v1/spec_decode/test_rejection_sampler_utils.py` _+10 more__
- **2026-10-29** [`4e0ad57203`](https://github.com/vllm-project/vllm/commit/4e0ad57203) [#62359](https://github.com/vllm-project/vllm/pull/62359)
  [Perf][DSv4.1] Share Engram host tables as host-NUMA cuMem across DP ranks (#62359)
  _Files: `tests/distributed/test_engram_dp_shard.py`, `vllm/config/engram.py`, `vllm/model_executor/model_loader/weight_utils.py`, `vllm/models/deepseek_v41/common/engram.py` _+2 more__
- **2026-10-29** [`d8fdf4f61b`](https://github.com/vllm-project/vllm/commit/d8fdf4f61b) [#64458](https://github.com/vllm-project/vllm/pull/64458)
  [MRV2][PP] Fix spec-decode draft/sampled-token broadcast issues (#64458)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/pp_utils.py` _+1 more__
- **2026-10-29** [`d295942d0d`](https://github.com/vllm-project/vllm/commit/d295942d0d) [#63275](https://github.com/vllm-project/vllm/pull/63275)
  [Spec Decode] Support trace replay with speculative decoding (#63275)
  _Files: `docs/serving/online_serving/trace_replay.md`, `tests/v1/sample/test_logprobs.py`, `tests/v1/sample/test_trace_replay_params.py`, `tests/v1/spec_decode/test_rejection_sampler_utils.py` _+5 more__
- **2026-10-28** [`6ba5dbeeb0`](https://github.com/vllm-project/vllm/commit/6ba5dbeeb0) [#61270](https://github.com/vllm-project/vllm/pull/61270)
  [Model] Support MTP drafts in the Transformers modeling backend (#61270)
  _Files: `tests/config/test_speculative_draft_hf_overrides.py`, `tests/models/registry.py`, `tests/models/transformers/test_backend.py`, `tests/test_config.py` _+5 more__
- **2026-10-28** [`cdd2750cd5`](https://github.com/vllm-project/vllm/commit/cdd2750cd5) [#61464](https://github.com/vllm-project/vllm/pull/61464)
  [MRV2][DBO] Support DBO with speculative decoding and DCP (#61464)
  _Files: `tests/test_config.py`, `tests/v1/distributed/test_dbo.py`, `tests/v1/worker/test_gpu_target_dependent_ar_speculator.py`, `tests/v1/worker/test_gpu_ubatch_slicing.py` _+7 more__
- **2026-10-28** [`5118d990fb`](https://github.com/vllm-project/vllm/commit/5118d990fb) [#62796](https://github.com/vllm-project/vllm/pull/62796)
  [Bugfix][Spec Decode] Align adaptive draft prefill graph padding (#62796)
  _Files: `tests/v1/cudagraph/test_cudagraph_manager.py`, `vllm/benchmarks/forward/speculator.py`, `vllm/v1/worker/gpu/dp_utils.py`, `vllm/v1/worker/gpu/spec_decode/speculator.py` _+1 more__
- **2026-10-28** [`820be160ce`](https://github.com/vllm-project/vllm/commit/820be160ce) [#64151](https://github.com/vllm-project/vllm/pull/64151)
  [Spec Decode] Disable batch-sharded draft logits for PCP (#64151)
  _Files: `vllm/v1/worker/gpu/spec_decode/speculator.py`_
- **2026-10-27** [`c4f2bb4abb`](https://github.com/vllm-project/vllm/commit/c4f2bb4abb) [#61557](https://github.com/vllm-project/vllm/pull/61557)
  [Bugfix][Spec Decode] Preserve grammar-invalid drafts for rejection sampling (#61557)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `tests/v1/core/test_scheduler.py`, `tests/v1/e2e/general/test_async_scheduling.py`, `tests/v1/e2e/general/test_async_scheduling_accuracy.py` _+9 more__
- **2026-10-27** [`e3ba8d00db`](https://github.com/vllm-project/vllm/commit/e3ba8d00db) [#63873](https://github.com/vllm-project/vllm/pull/63873)
  [Bugfix][Bench] Handle packed hybrid KV and speculative recurrent state (#63873)
  _Files: `docs/cli/README.md`, `tests/benchmarks/test_forward_cli.py`, `vllm/benchmarks/forward/batch.py`, `vllm/benchmarks/forward/kv_init.py` _+1 more__
- **2026-10-27** [`4216a234cf`](https://github.com/vllm-project/vllm/commit/4216a234cf) [#61877](https://github.com/vllm-project/vllm/pull/61877)
  [Rust Frontend] Add per-request speculative decoding metrics (#61877)
  _Files: `rust/src/chat/src/event.rs`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/default/unified.rs`, `rust/src/chat/src/output/harmony/mod.rs` _+14 more__
- **2026-10-27** [`b29caba14e`](https://github.com/vllm-project/vllm/commit/b29caba14e) [#61832](https://github.com/vllm-project/vllm/pull/61832)
  [CI] Shard draft decoding, Qwen eval and scheduling automatically (#61832)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/spec_decode.yaml`_
- **2026-10-27** [`2b08392a5f`](https://github.com/vllm-project/vllm/commit/2b08392a5f) [#63853](https://github.com/vllm-project/vllm/pull/63853)
  [Bugfix][Spec Decode] Apply the draft max_model_len limit before model config hooks (#63853)
  _Files: `tests/config/test_speculative_draft_limits_max_model_len.py`, `vllm/config/vllm.py`_
- **2026-10-26** [`41f5146b5b`](https://github.com/vllm-project/vllm/commit/41f5146b5b) [#63421](https://github.com/vllm-project/vllm/pull/63421)
  [Spec Decode] Replace torch.compile'd AV draft-budget selection with a Triton kernel (#63421)
  _Files: `tests/v1/spec_decode/test_adaptive_verification.py`, `tests/v1/worker/test_mixed_warmup_gate.py`, `vllm/v1/worker/gpu/spec_decode/adaptive_verification.py`, `vllm/v1/worker/gpu/warmup.py`_
- **2026-10-26** [`29be2f2560`](https://github.com/vllm-project/vllm/commit/29be2f2560) [#62301](https://github.com/vllm-project/vllm/pull/62301)
  [Bugfix][Spec Decode] Preserve DP replica index for standalone draft models (#62301)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/v1/worker/gpu/spec_decode/standalone_ar/speculator.py`_
- **2026-10-26** [`85e199e60c`](https://github.com/vllm-project/vllm/commit/85e199e60c) [#62091](https://github.com/vllm-project/vllm/pull/62091)
  [Perf][DSv4.1] Read GPU Engram tables from peers' HBM instead of DP collectives (#62091)
  _Files: `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_engram.py`, `vllm/distributed/parallel_state.py`, `vllm/models/deepseek_v41/common/engram.py` _+1 more__
- **2026-10-26** [`39e6a1aafc`](https://github.com/vllm-project/vllm/commit/39e6a1aafc) [#63622](https://github.com/vllm-project/vllm/pull/63622)
  [Benchmark] Include speculative drafting in bench forward (#63622)
  _Files: `.agents/skills/model-microbenchmark/SKILL.md`, `docs/cli/README.md`, `tests/benchmarks/test_forward_cli.py`, `vllm/benchmarks/forward/batch.py` _+5 more__
- **2026-10-26** [`290582fbc5`](https://github.com/vllm-project/vllm/commit/290582fbc5) [#63068](https://github.com/vllm-project/vllm/pull/63068)
  [Bugfix][Multimodal] Respect meta initialization for Engram offload (#63068)
  _Files: `tests/kernels/test_engram.py`, `vllm/models/deepseek_v41/common/engram.py`_

## CI / Build  (20 commits)

- **2026-11-02** [`ccafd6c65c`](https://github.com/vllm-project/vllm/commit/ccafd6c65c) [#64585](https://github.com/vllm-project/vllm/pull/64585)
  [NIXL][CI/Build] Bump NIXL to 1.5.2 and drop source build for Rubin (#64585)
  _Files: `.buildkite/release-pipeline.yaml`, `docker/Dockerfile`, `docker/versions.json`, `docs/contributing/dockerfile/dockerfile.md` _+3 more__
- **2026-10-31** [`06f36c1222`](https://github.com/vllm-project/vllm/commit/06f36c1222) [#64579](https://github.com/vllm-project/vllm/pull/64579)
  [NIXL] Bump NIXL version to 1.5.2 (#64579)
  _Files: `docker/Dockerfile.xpu`, `requirements/kv_connectors.txt`, `requirements/kv_connectors_cu12.txt`_
- **2026-10-30** [`00ba900aa8`](https://github.com/vllm-project/vllm/commit/00ba900aa8) [#64633](https://github.com/vllm-project/vllm/pull/64633)
  [XPU] Use GitHub release page index URL for vllm-xpu-kernels (#64633)
  _Files: `requirements/xpu.txt`_
- **2026-10-30** [`0e34db705f`](https://github.com/vllm-project/vllm/commit/0e34db705f) [#64590](https://github.com/vllm-project/vllm/pull/64590)
  [CI] Enroll the remaining LM Eval jobs in automatic sharding (30 jobs) (#64590)
  _Files: `.buildkite/test_areas/lm_eval.yaml`_
- **2026-10-30** [`15a9677306`](https://github.com/vllm-project/vllm/commit/15a9677306) [#64596](https://github.com/vllm-project/vllm/pull/64596)
  [CI] Enroll the remaining Misc and Samplers jobs in automatic sharding (17 jobs) (#64596)
  _Files: `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/samplers.yaml`_
- **2026-10-30** [`c5e37f1922`](https://github.com/vllm-project/vllm/commit/c5e37f1922) [#64593](https://github.com/vllm-project/vllm/pull/64593)
  [CI] Enroll the remaining Distributed, EP and fault-tolerance jobs in automatic sharding (25 jobs) (#64593)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/expert_parallelism.yaml`, `.buildkite/test_areas/fault_tolerance.yaml`, `.buildkite/test_areas/models_distributed.yaml`_
- **2026-10-30** [`fc84d05acb`](https://github.com/vllm-project/vllm/commit/fc84d05acb) [#64592](https://github.com/vllm-project/vllm/pull/64592)
  [CI] Enroll the remaining Spec Decode jobs in automatic sharding (21 jobs) (#64592)
  _Files: `.buildkite/test_areas/spec_decode.yaml`_
- **2026-10-30** [`a9a8222926`](https://github.com/vllm-project/vllm/commit/a9a8222926) [#64591](https://github.com/vllm-project/vllm/pull/64591)
  [CI] Enroll the remaining Kernels jobs in automatic sharding (30 jobs) (#64591)
  _Files: `.buildkite/test_areas/kernels.yaml`_
- **2026-10-29** [`28a5fba06b`](https://github.com/vllm-project/vllm/commit/28a5fba06b) [#64411](https://github.com/vllm-project/vllm/pull/64411)
  [Kernel] Update DeepGEMM commit (#64411)
  _Files: `cmake/external_projects/deepgemm.cmake`_
- **2026-10-28** [`15cc0a8deb`](https://github.com/vllm-project/vllm/commit/15cc0a8deb) [#64318](https://github.com/vllm-project/vllm/pull/64318)
  [CI] Enroll Language Models (Standard) in automatic sharding (#64318)
  _Files: `.buildkite/test_areas/models_language.yaml`_
- **2026-10-28** [`0fddee1f58`](https://github.com/vllm-project/vllm/commit/0fddee1f58) [#64328](https://github.com/vllm-project/vllm/pull/64328)
  [CI] Bump GitHub Actions versions and replace node20 pre-commit/action (#64328)
  _Files: `.github/workflows/buf.yml`, `.github/workflows/issue_autolabel.yml`, `.github/workflows/macos-smoke-test.yml`, `.github/workflows/notify-ci-authorized.yml` _+6 more__
- **2026-10-28** [`08a236fa43`](https://github.com/vllm-project/vllm/commit/08a236fa43) [#64057](https://github.com/vllm-project/vllm/pull/64057)
  [CI][XPU] Deselect Mamba deep-sleep case in Intel CI (#64057)
  _Files: `.buildkite/intel_jobs/basic_correctness_intel.yaml`_
- **2026-10-28** [`84e4553673`](https://github.com/vllm-project/vllm/commit/84e4553673) [#63895](https://github.com/vllm-project/vllm/pull/63895)
  [CI][XPU] Give test_mrv2_weight_offloading more GPU memory headroom (#63895)
  _Files: `tests/basic_correctness/cpu_offload/test_cpu_offload.py`_
- **2026-10-27** [`0855defde8`](https://github.com/vllm-project/vllm/commit/0855defde8) [#63817](https://github.com/vllm-project/vllm/pull/63817)
  Revert "[NIXL] Bump NIXL version to 1.5.1" (#63817) (#64085)
  _Files: `requirements/kv_connectors.txt`, `requirements/kv_connectors_cu12.txt`_
- **2026-10-27** [`b3de57ad51`](https://github.com/vllm-project/vllm/commit/b3de57ad51) [#58232](https://github.com/vllm-project/vllm/pull/58232)
  [CI][Bugfix] Set gpu_memory_utilization for the Spark GPQA eval config (#58232)
  _Files: `tests/evals/gpt_oss/configs/gpt-oss-20b-sm120.yaml`_
- **2026-10-27** [`9e0bc7a651`](https://github.com/vllm-project/vllm/commit/9e0bc7a651) [#64021](https://github.com/vllm-project/vllm/pull/64021)
  [CI] Remove codeowner for pre-commit allowlists (#64021)
  _Files: `.github/CODEOWNERS`_
- **2026-10-27** [`4e3d49dda2`](https://github.com/vllm-project/vllm/commit/4e3d49dda2) [#61844](https://github.com/vllm-project/vllm/pull/61844)
  [revert] [Build] Fix QuTLASS compilation with PyTorch 2.13 (#61844)
  _Files: `cmake/external_projects/qutlass.cmake`_
- **2026-10-26** [`7a1ebe4ef5`](https://github.com/vllm-project/vllm/commit/7a1ebe4ef5) [#63817](https://github.com/vllm-project/vllm/pull/63817)
  [NIXL] Bump NIXL version to 1.5.1 (#63817)
  _Files: `requirements/kv_connectors.txt`, `requirements/kv_connectors_cu12.txt`_
- **2026-10-26** [`25ba0af777`](https://github.com/vllm-project/vllm/commit/25ba0af777) [#63840](https://github.com/vllm-project/vllm/pull/63840)
  [CI][Frontend] Let the SSL refresher test's fake server accept peer_loads (#63840)
  _Files: `tests/entrypoints/launchers/test_ssl_cert_refresher.py`_
- **2026-10-26** [`cd9aa5b5ee`](https://github.com/vllm-project/vllm/commit/cd9aa5b5ee) [#63601](https://github.com/vllm-project/vllm/pull/63601)
  [Bugfix][Platform] Keep PIN_MEMORY eager; avoid resolving platform during import vllm (#63601)
  _Files: `.buildkite/test_areas/plugins.yaml`, `tests/test_force_first_config.py`, `vllm/env_override.py`, `vllm/envs.py` _+4 more__

## Quantization  (19 commits)

- **2026-11-02** [`b5814faa25`](https://github.com/vllm-project/vllm/commit/b5814faa25) [#64815](https://github.com/vllm-project/vllm/pull/64815)
  [Perf][MXFP8] Keep DeepSeek-V4.1 fusions on the torch._scaled_mm kernel (#64815)
  _Files: `tests/fusion/test_quant_activation_contract.py`, `vllm/model_executor/kernels/linear/mxfp8/pytorch.py`, `vllm/models/deepseek_v41/common/ops/query_quant.py`, `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`_
- **2026-11-02** [`bbac37abba`](https://github.com/vllm-project/vllm/commit/bbac37abba) [#64598](https://github.com/vllm-project/vllm/pull/64598)
  [CI] Enroll the remaining quantization and benchmarks jobs in automatic sharding (4 jobs) (#64598)
  _Files: `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/quantization.yaml`_
- **2026-11-02** [`318c4db661`](https://github.com/vllm-project/vllm/commit/318c4db661) [#64852](https://github.com/vllm-project/vllm/pull/64852)
  [Perf][MiniMax-M3] (NVIDIA-only) Fused norm+quant MXFP8 (#64852)
  _Files: `tests/models/minimax_m3/test_norm_mxfp8.py`, `vllm/models/minimax_m3/nvidia/model.py`, `vllm/models/minimax_m3/nvidia/ops/norm_mxfp8.py`_
- **2026-11-02** [`49fee5b34c`](https://github.com/vllm-project/vllm/commit/49fee5b34c) [#65000](https://github.com/vllm-project/vllm/pull/65000)
  [Kernel] Batch invariance: combine the NVFP4 linear kernel overrides (follow-up to #62192) (#65000)
  _Files: `tests/kernels/quantization/test_nvfp4_kernel_selection.py`, `vllm/model_executor/kernels/linear/__init__.py`_
- **2026-11-01** [`e0d00e4b8e`](https://github.com/vllm-project/vllm/commit/e0d00e4b8e) [#64607](https://github.com/vllm-project/vllm/pull/64607)
  [Recipe] Qwen3.5-397B-A17B: add the B200 NVFP4 TP2 agentic preset (#64607)
  _Files: `recipes/models/Qwen/Qwen3.5-397B-A17B.yaml`_
- **2026-10-31** [`b5755c3ba5`](https://github.com/vllm-project/vllm/commit/b5755c3ba5) [#64336](https://github.com/vllm-project/vllm/pull/64336)
  [RL][Model Loader] Direct weight reload: write checkpoint tensors into the live model (#64336)
  _Files: `tests/model_executor/model_loader/test_direct_reload.py`, `tests/quantization/test_keep_param_objects.py`, `tests/v1/worker/test_gpu_model_runner.py`, `tests/v1/worker/test_gpu_worker_weight_transfer.py` _+13 more__
- **2026-10-30** [`6c19299fca`](https://github.com/vllm-project/vllm/commit/6c19299fca) [#64509](https://github.com/vllm-project/vllm/pull/64509)
  [Perf][Qwen3.5] (NVIDIA-only) Fused norm+quant and gate+quant (#64509)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/kernels/core/test_fused_sigmoid_gate_mul.py`, `tests/kernels/mamba/test_gdn_output_projection.py`, `tests/models/qwen3_5/__init__.py` _+7 more__
- **2026-10-30** [`75d14e84e3`](https://github.com/vllm-project/vllm/commit/75d14e84e3) [#64666](https://github.com/vllm-project/vllm/pull/64666)
  [Docs] Fix dead links to moved llm-d, Dynamo, TPU, Ray and Tensorizer pages (#64666)
  _Files: `docs/.nav.yml`, `docs/deployment/integrations/dynamo.md`, `docs/deployment/integrations/llm-d.md`, `docs/design/metrics.md` _+4 more__
- **2026-10-30** [`8b10bda57c`](https://github.com/vllm-project/vllm/commit/8b10bda57c) [#64494](https://github.com/vllm-project/vllm/pull/64494)
  [Kernel] Add size-gated PDL to silu_and_mul_nvfp4_quant (#64494)
  _Files: `csrc/quantization/fp4/activation_nvfp4_quant_fusion_kernels.cu`_
- **2026-10-29** [`5cf5c8fa6d`](https://github.com/vllm-project/vllm/commit/5cf5c8fa6d) [#60163](https://github.com/vllm-project/vllm/pull/60163)
  [Bugfix][Quantization] Fix Humming FP8 linear for per-tensor/per-channel FP8 weights (#60163)
  _Files: `tests/quantization/test_fp8.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/online/fp8.py`_
- **2026-10-29** [`b42f25b00c`](https://github.com/vllm-project/vllm/commit/b42f25b00c) [#63382](https://github.com/vllm-project/vllm/pull/63382)
  [Bugfix][NVFP4] Fix NaN logits and garbage output from uninitialized fused act+quant scales (#63382)
  _Files: `csrc/quantization/fp4/activation_nvfp4_quant_fusion_kernels.cu`, `tests/kernels/quantization/test_silu_mul_nvfp4_quant.py`_
- **2026-10-28** [`f4bf6a93b6`](https://github.com/vllm-project/vllm/commit/f4bf6a93b6) [#64349](https://github.com/vllm-project/vllm/pull/64349)
  [CI] Bump pre-commit hooks (except ruff) (#64349)
  _Files: `.pre-commit-config.yaml`, `csrc/cpu/cpu_types_scalar.hpp`, `csrc/quantization/w8a8/fp8/common.cu`, `csrc/quantization/w8a8/fp8/per_token_group_quant.cu` _+5 more__
- **2026-10-28** [`6abdff5930`](https://github.com/vllm-project/vllm/commit/6abdff5930) [#63018](https://github.com/vllm-project/vllm/pull/63018)
  [Perf][DSv4.1] Tile the NVFP4 compressed-KV dequant-gather (#63018)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `vllm/models/deepseek_v41/common/ops/cache_utils.py`_
- **2026-10-28** [`41dd82e6a7`](https://github.com/vllm-project/vllm/commit/41dd82e6a7) [#63975](https://github.com/vllm-project/vllm/pull/63975)
  [XPU][CI] Fix test_tp1_fp8_fusions rms_quant_fusion on XPU (#63975)
  _Files: `tests/compile/fusions_e2e/test_tp1_quant.py`_
- **2026-10-28** [`a91b939bfb`](https://github.com/vllm-project/vllm/commit/a91b939bfb) [#63872](https://github.com/vllm-project/vllm/pull/63872)
  [Bugfix][Bench] Support Muse balanced routing (#63872)
  _Files: `.buildkite/test_areas/quantization.yaml`, `tests/benchmarks/test_forward_cli.py`, `vllm/benchmarks/forward/routing.py`_
- **2026-10-27** [`43111fd1f0`](https://github.com/vllm-project/vllm/commit/43111fd1f0) [#53104](https://github.com/vllm-project/vllm/pull/53104)
  [Bugfix][Spec Decode] Fix eagle draft sharing with a quantized lm_head (#53104)
  _Files: `tests/v1/worker/test_gpu_spec_decode_eagle_utils.py`, `vllm/v1/worker/gpu/spec_decode/eagle/utils.py`_
- **2026-10-26** [`0a95e4d73c`](https://github.com/vllm-project/vllm/commit/0a95e4d73c) [#61362](https://github.com/vllm-project/vllm/pull/61362)
  [XPU][FP8] Use per-token dynamic FP8 activation quantization (#61362)
  _Files: `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/online/fp8.py`_
- **2026-10-26** [`5be249d0ad`](https://github.com/vllm-project/vllm/commit/5be249d0ad) [#62026](https://github.com/vllm-project/vllm/pull/62026)
  [Kernel] Allow registering OOT block-scaled FP8 linear kernels (#62026)
  _Files: `tests/kernels/quantization/test_scaled_mm_kernel_selection.py`, `vllm/model_executor/kernels/linear/__init__.py`_
- **2026-10-26** [`d26d5db01f`](https://github.com/vllm-project/vllm/commit/d26d5db01f) [#63658](https://github.com/vllm-project/vllm/pull/63658)
  [XPU][CI] Enable test_fusion_rmsnorm_quant on XPU (#63658)
  _Files: `tests/compile/passes/test_fusion.py`_

## LoRA  (14 commits)

- **2026-11-02** [`eecf8dbb2b`](https://github.com/vllm-project/vllm/commit/eecf8dbb2b) [#64616](https://github.com/vllm-project/vllm/pull/64616)
  [Bugfix][LoRA] Fix KeyError crash when a LoRA name is reloaded with requests in flight (#64616)
  _Files: `tests/lora/test_lora_functions.py`, `vllm/lora/request.py`_
- **2026-11-02** [`08e3f26458`](https://github.com/vllm-project/vllm/commit/08e3f26458) [#65008](https://github.com/vllm-project/vllm/pull/65008)
  [CI] Lower gpu_memory_utilization in test_gemma4_lora (#65008)
  _Files: `tests/lora/test_gemma4_tp.py`_
- **2026-10-30** [`040abb262c`](https://github.com/vllm-project/vllm/commit/040abb262c) [#61995](https://github.com/vllm-project/vllm/pull/61995)
  [CPU][MRv2] Enable MRv2 for non-triton CPU backends (#61995)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `.buildkite/test_areas/misc.yaml`, `cmake/cpu_extension.cmake`, `csrc/cpu/block_table.cpp` _+58 more__
- **2026-10-30** [`1114488f15`](https://github.com/vllm-project/vllm/commit/1114488f15) [#64514](https://github.com/vllm-project/vllm/pull/64514)
  [Rust Frontend] Support VLLM_SKIP_MODEL_NAME_VALIDATION (#64514)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/server/src/config.rs`, `rust/src/server/src/grpc/convert.rs` _+15 more__
- **2026-10-30** [`96c80f8af7`](https://github.com/vllm-project/vllm/commit/96c80f8af7) [#63005](https://github.com/vllm-project/vllm/pull/63005)
  [Perf][Frontend] Build run-batch TypeAdapters once instead of per request (#63005)
  _Files: `tests/entrypoints/launchers/test_run_batch.py`, `vllm/entrypoints/launchers/run_batch.py`_
- **2026-10-30** [`e152c70570`](https://github.com/vllm-project/vllm/commit/e152c70570) [#64513](https://github.com/vllm-project/vllm/pull/64513)
  [Rust Frontend] Report the generate response envelope like Python (#64513)
  _Files: `rust/src/server/src/lora.rs`, `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/inference/generate/convert.rs`, `rust/src/server/src/routes/inference/generate/types.rs` _+3 more__
- **2026-10-29** [`f5aa164b51`](https://github.com/vllm-project/vllm/commit/f5aa164b51) [#63489](https://github.com/vllm-project/vllm/pull/63489)
  [Bugfix][LoRA] Refuse adapters with LoRA on modules vLLM does not wrap (#63489)
  _Files: `tests/lora/test_sequence_classification.py`, `vllm/lora/lora_model.py`, `vllm/lora/model_manager.py`, `vllm/lora/worker_manager.py`_
- **2026-10-29** [`dc9278ee27`](https://github.com/vllm-project/vllm/commit/dc9278ee27) [#63286](https://github.com/vllm-project/vllm/pull/63286)
  [Bugfix][LoRA] Load the head of SEQ_CLS adapters saved without modules_to_save (#63286)
  _Files: `vllm/lora/peft_helper.py`_
- **2026-10-28** [`fd3469f453`](https://github.com/vllm-project/vllm/commit/fd3469f453) [#61956](https://github.com/vllm-project/vllm/pull/61956)
  [XPU] bump xpu-kernels to v0.1.16.2 (#61956)
  _Files: `.buildkite/intel_jobs/lora_intel.yaml`, `requirements/xpu.txt`_
- **2026-10-28** [`4eb15aa369`](https://github.com/vllm-project/vllm/commit/4eb15aa369) [#63961](https://github.com/vllm-project/vllm/pull/63961)
  [Rust Frontend] Return 404 for a missing LoRA adapter path like Python (#63961)
  _Files: `rust/src/server/src/error.rs`, `rust/src/server/src/grpc/control.rs`, `rust/src/server/src/lora.rs`, `rust/src/server/src/routes/lora.rs`_
- **2026-10-28** [`06e172b5cf`](https://github.com/vllm-project/vllm/commit/06e172b5cf) [#59341](https://github.com/vllm-project/vllm/pull/59341)
  [Bugfix][Spec Decode] Align MRV2 lm_head LoRA with logits rows (#59341)
  _Files: `tests/v1/worker/test_mrv2_lmhead_lora.py`, `vllm/v1/worker/gpu/lora_utils.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-10-26** [`938be2d83d`](https://github.com/vllm-project/vllm/commit/938be2d83d) [#63569](https://github.com/vllm-project/vllm/pull/63569)
  [Tool Calling] Migrate llama3_json parser to parser engine (#63569)
  _Files: `tests/parser/engine/test_delegating_replay.py`, `tests/parser/engine/test_granite.py`, `tests/parser/engine/test_llama_json.py`, `tests/parser/engine/test_replay.py` _+12 more__
- **2026-10-26** [`f1ac0cf20d`](https://github.com/vllm-project/vllm/commit/f1ac0cf20d) [#63694](https://github.com/vllm-project/vllm/pull/63694)
  [XPU][UT] Allow HF reference models to load LoRA adapters by adding PEFT to XPU test dependencies (#63694)
  _Files: `requirements/test/xpu.in`, `requirements/test/xpu.txt`, `tests/models/language/generation/test_hybrid.py`_
- **2026-10-26** [`93dc587bd9`](https://github.com/vllm-project/vllm/commit/93dc587bd9) [#59989](https://github.com/vllm-project/vllm/pull/59989)
  [Bugfix] Fix Qwen3-VL reranker crash on missing tie_word_embeddings in text config (#59989)
  _Files: `vllm/model_executor/models/adapters.py`_

## Perf / Benchmark  (11 commits)

- **2026-11-02** [`bb197a852f`](https://github.com/vllm-project/vllm/commit/bb197a852f) [#61680](https://github.com/vllm-project/vllm/pull/61680)
  [Perf][HiSparse] Segment host KV pool backing files (#61680)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `tests/v1/worker/test_utils.py`, `vllm/v1/hisparse/runtime.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py` _+1 more__
- **2026-11-02** [`f48cc6262e`](https://github.com/vllm-project/vllm/commit/f48cc6262e) [#65083](https://github.com/vllm-project/vllm/pull/65083)
  [Bugfix][Benchmark] Keep numeric-string prompts as strings in CustomDataset (#65083)
  _Files: `tests/benchmarks/test_custom_dataset_seed.py`, `vllm/benchmarks/datasets/datasets.py`_
- **2026-10-29** [`61a6f8138f`](https://github.com/vllm-project/vllm/commit/61a6f8138f) [#61777](https://github.com/vllm-project/vllm/pull/61777)
  [Bugfix][Bench] Aggregate DP running requests for profiling (#61777)
  _Files: `rust/src/bench/src/benchmark.rs`, `rust/src/bench/src/cli.rs`_
- **2026-10-28** [`d7f68d4c7d`](https://github.com/vllm-project/vllm/commit/d7f68d4c7d) [#62748](https://github.com/vllm-project/vllm/pull/62748)
  [Perf][MRV2] Skip idle sampler staged writes (#62748)
  _Files: `docs/features/custom_logitsprocs.md`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/sample/logits_processor/interface.py`_
- **2026-10-28** [`c105af4292`](https://github.com/vllm-project/vllm/commit/c105af4292) [#62240](https://github.com/vllm-project/vllm/pull/62240)
  [Perf][DSA] Rank the prefill indexer logits with DeepSelect in BF16 (#62240)
  _Files: `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-10-28** [`deb1a97eb8`](https://github.com/vllm-project/vllm/commit/deb1a97eb8) [#64227](https://github.com/vllm-project/vllm/pull/64227)
  [Bugfix][Benchmark] Restore --input-len/--output-len/--prefix-len in vllm bench throughput (#64227)
  _Files: `tests/benchmarks/test_throughput_cli.py`, `vllm/benchmarks/throughput.py`_
- **2026-10-28** [`6282c4c5cf`](https://github.com/vllm-project/vllm/commit/6282c4c5cf) [#64167](https://github.com/vllm-project/vllm/pull/64167)
  [Bench] Default to Zipf routing for forward benchmarks with dummy weights (#64167)
  _Files: `.agents/skills/model-microbenchmark/SKILL.md`, `docs/benchmarking/cli.md`, `docs/cli/README.md`, `tests/benchmarks/test_forward_cli.py` _+2 more__
- **2026-10-27** [`b4a0830f66`](https://github.com/vllm-project/vllm/commit/b4a0830f66) [#62464](https://github.com/vllm-project/vllm/pull/62464)
  [Perf] Avoid redundant tensor operations during serialization (#62464)
  _Files: `tests/v1/test_serial_utils.py`, `vllm/utils/torch_utils.py`, `vllm/v1/utils.py`_
- **2026-10-27** [`939ff73503`](https://github.com/vllm-project/vllm/commit/939ff73503) [#63785](https://github.com/vllm-project/vllm/pull/63785)
  [Perf] Drop BasevLLMParameter's Python `__torch_function__` (#63785)
  _Files: `tests/model_executor/test_utils.py`, `vllm/model_executor/parameter.py`_
- **2026-10-27** [`f09d5e30c3`](https://github.com/vllm-project/vllm/commit/f09d5e30c3) [#51109](https://github.com/vllm-project/vllm/pull/51109)
  [Rust][Benchmark] Fix multi-turn input token accounting (#51109)
  _Files: `rust/src/bench/src/metrics/calculator.rs`, `rust/src/bench/src/multi_turn.rs`_
- **2026-10-26** [`78e2f79601`](https://github.com/vllm-project/vllm/commit/78e2f79601) [#63633](https://github.com/vllm-project/vllm/pull/63633)
  [Perf][MRV2] Stage buffer contents by reference and copy straight into UVA (#63633)
  _Files: `tests/kernels/core/test_uva.py`, `vllm/utils/torch_utils.py`, `vllm/v1/worker/gpu/buffer_utils.py`, `vllm/v1/worker/gpu/mm/rope.py`_

## Docs  (9 commits)

- **2026-10-30** [`d0d3005aff`](https://github.com/vllm-project/vllm/commit/d0d3005aff) [#64665](https://github.com/vllm-project/vllm/pull/64665)
  [Doc] Kimi-K3: move the GB300 AgentX presets to the Oct 26 points with KV-balanced decode (#64665)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-29** [`dc45a5f552`](https://github.com/vllm-project/vllm/commit/dc45a5f552) [#60899](https://github.com/vllm-project/vllm/pull/60899)
  [Doc] Add k8s-aibom to deployment integrations (#60899)
  _Files: `docs/deployment/integrations/k8s-aibom.md`_
- **2026-10-29** [`b91df5a9f7`](https://github.com/vllm-project/vllm/commit/b91df5a9f7) [#64554](https://github.com/vllm-project/vllm/pull/64554)
  [Docs] Diff against the merge base in the docs build gate (#64554)
  _Files: `docs/pre_run_check.sh`_
- **2026-10-29** [`5082c45853`](https://github.com/vllm-project/vllm/commit/5082c45853) [#62500](https://github.com/vllm-project/vllm/pull/62500)
  [Docs] Add vllm-iluvatar to custom_op.md (#62500)
  _Files: `docs/design/custom_op.md`_
- **2026-10-28** [`88d3995ea1`](https://github.com/vllm-project/vllm/commit/88d3995ea1) [#64186](https://github.com/vllm-project/vllm/pull/64186)
  [Feature][Core] Add opt-in multi-worker CUDA checkpoint sleep (#64186)
  _Files: `docs/features/sleep_mode.md`, `tests/basic_correctness/memory/sleep_mode/test_process_checkpoint.py`, `tests/v1/executor/test_cuda_checkpoint_executor.py`, `tests/v1/executor/test_cuda_process_checkpoint.py` _+2 more__
- **2026-10-27** [`815df3af10`](https://github.com/vllm-project/vllm/commit/815df3af10) [#64114](https://github.com/vllm-project/vllm/pull/64114)
  [Doc] MiniMax-M3: GB200 AgentX presets (TP4/TP8) (#64114)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`_
- **2026-10-26** [`b82393b773`](https://github.com/vllm-project/vllm/commit/b82393b773) [#63852](https://github.com/vllm-project/vllm/pull/63852)
  [Doc] Kimi-K3: refresh the GB300 AgentX xPyD preset and add the 3P1D DEP16 preset (#63852)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-26** [`74340c7300`](https://github.com/vllm-project/vllm/commit/74340c7300) [#63036](https://github.com/vllm-project/vllm/pull/63036)
  [docs] correct NIXL hybrid SSM heterogeneous TP support (#63036)
  _Files: `docs/features/nixl_connector_compatibility.md`_
- **2026-10-26** [`256d8b40d0`](https://github.com/vllm-project/vllm/commit/256d8b40d0) [#62885](https://github.com/vllm-project/vllm/pull/62885)
  [Doc] Kolibri 1 reasoning and tool-call parsing via HF response template (#62885)
  _Files: `docs/features/reasoning_outputs.md`, `docs/features/tool_calling.md`_

## Compilation / CUDA Graph  (6 commits)

- **2026-11-02** [`b18775f893`](https://github.com/vllm-project/vllm/commit/b18775f893) [#62560](https://github.com/vllm-project/vllm/pull/62560)
  [Core][MRV2] Warm up the sampler after CUDA graph capture to stop memory growth under load (#62560)
  _Files: `vllm/v1/worker/gpu_worker.py`_
- **2026-10-30** [`2fab35893b`](https://github.com/vllm-project/vllm/commit/2fab35893b) [#60873](https://github.com/vllm-project/vllm/pull/60873)
  [Bugfix] Fix depyf incompatibility with Inductor's set_sys_modules (#60873)
  _Files: `tests/compile/backend.py`, `tests/compile/fullgraph/test_full_graph.py`, `tests/compile/test_depyf_compat.py`, `vllm/compilation/depyf_compat.py` _+1 more__
- **2026-10-30** [`a20280f30e`](https://github.com/vllm-project/vllm/commit/a20280f30e) [#63247](https://github.com/vllm-project/vllm/pull/63247)
  [Compile] Make the compile cache device-neutral with compile_on_one_rank (#63247)
  _Files: `.buildkite/test_areas/distributed.yaml`, `tests/compile/test_aot_compile.py`, `vllm/compilation/compiler_interface.py`, `vllm/envs.py`_
- **2026-10-27** [`dc4d977d97`](https://github.com/vllm-project/vllm/commit/dc4d977d97) [#63778](https://github.com/vllm-project/vllm/pull/63778)
  [MRV2] Let the runner decide whether to profile CUDA graph memory (#63778)
  _Files: `vllm/v1/worker/gpu_worker.py`_
- **2026-10-27** [`f81f0f2509`](https://github.com/vllm-project/vllm/commit/f81f0f2509) [#63427](https://github.com/vllm-project/vllm/pull/63427)
  [Bugfix][CUDA Graph] Weak-ref nested outputs of captured graphs (#63427)
  _Files: `tests/utils_/test_torch_utils.py`, `vllm/utils/torch_utils.py`_
- **2026-10-26** [`4135590ffe`](https://github.com/vllm-project/vllm/commit/4135590ffe) [#63431](https://github.com/vllm-project/vllm/pull/63431)
  [Bugfix][MRV2] Skip adaptive verification cost profiling in the CUDA graph memory-profiling pass (#63431)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/v1/worker/gpu/model_runner.py`_

---
_Generated 2026-11-02 18:18 UTC_