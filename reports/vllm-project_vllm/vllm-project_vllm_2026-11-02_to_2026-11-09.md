# vllm-project/vllm — Weekly Change Report
**Period:** 2026-11-02 → 2026-11-09  |  **Total commits:** 675

## ✨ New Features This Week

- **2026-11-09** [#66307](https://github.com/vllm-project/vllm/pull/66307) — [CI][ROCm] Add AMD HC kernel tests for Qwen4 Exp and mirror the B200 HC step (#66307)
- **2026-11-09** [#66537](https://github.com/vllm-project/vllm/pull/66537) — [Perf][MoE] Add H200 FP8 config for GLM-5.3-Flash TP8 (#66537)
- **2026-11-09** [#66413](https://github.com/vllm-project/vllm/pull/66413) — [Transformers backend] Support LoRA on lm_head and on any input embedding name (#66413)
- **2026-11-09** [#63847](https://github.com/vllm-project/vllm/pull/63847) — [ROCm][Kernel] Support persistent_topk on ROCm (#63847)
- **2026-11-09** [#64693](https://github.com/vllm-project/vllm/pull/64693) — [ROCm][MoRIIO] Support PP for prefill instance in PD disaggregated serving with MoRI WRITE mode (#64693)
- **2026-11-09** [#66545](https://github.com/vllm-project/vllm/pull/66545) — [Transformers backend] Support batch-sharded sampling (#66545)
- **2026-11-09** [#65735](https://github.com/vllm-project/vllm/pull/65735) — [Model] Add transcription to the Transformers modeling backend (#65735)
- **2026-11-09** [#55855](https://github.com/vllm-project/vllm/pull/55855) — [Feature][KV Offload] Add RDMA-capable OBJ tier (#55855) (#56192)
- **2026-11-09** [#66119](https://github.com/vllm-project/vllm/pull/66119) — [Rust Frontend] Support --log-level and --logging-config (#66119)
- **2026-11-09** [#66478](https://github.com/vllm-project/vllm/pull/66478) — [Frontend] Default --enable-scale-out to VLLM_SERVER_DEV_MODE (#66478)
- _…and 95 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-11-09** [`e5bec1ddd4`](https://github.com/vllm-project/vllm/commit/e5bec1ddd4) [#66611](https://github.com/vllm-project/vllm/pull/66611) — [ROCm][CI] Restore the simple-nemotron-h-8b GSM8K threshold on ROCm (#66611)
- **2026-11-09** [`85f6a26455`](https://github.com/vllm-project/vllm/commit/85f6a26455) [#65349](https://github.com/vllm-project/vllm/pull/65349) — [Perf] Warm up JIT kernels that only long prefills, eager drafters and constrained decoding reach (#65349)
- **2026-11-09** [`fe48798e86`](https://github.com/vllm-project/vllm/commit/fe48798e86) [#65940](https://github.com/vllm-project/vllm/pull/65940) — [ROCm][CI] Run the MI355 BF16 AR-RMS fusion E2E matrices nightly with a per-PR subset (#65940)
- **2026-11-09** [`e090987a3b`](https://github.com/vllm-project/vllm/commit/e090987a3b) [#66307](https://github.com/vllm-project/vllm/pull/66307) — [CI][ROCm] Add AMD HC kernel tests for Qwen4 Exp and mirror the B200 HC step (#66307)
- **2026-11-09** [`bbaef29734`](https://github.com/vllm-project/vllm/commit/bbaef29734) [#66338](https://github.com/vllm-project/vllm/pull/66338) — [CI][ROCm] Restore the AMD mirror of Fault Tolerance E2E (#66338)
- **2026-11-09** [`5b54aea9ec`](https://github.com/vllm-project/vllm/commit/5b54aea9ec) [#66425](https://github.com/vllm-project/vllm/pull/66425) — [CI][Deps] Bump truststore to 0.10.5 to stop the OpenSSL segfault in HF downloads (#66425)
- **2026-11-09** [`9ad0029883`](https://github.com/vllm-project/vllm/commit/9ad0029883) [#63847](https://github.com/vllm-project/vllm/pull/63847) — [ROCm][Kernel] Support persistent_topk on ROCm (#63847)
- **2026-11-09** [`56e5608d0f`](https://github.com/vllm-project/vllm/commit/56e5608d0f) [#64693](https://github.com/vllm-project/vllm/pull/64693) — [ROCm][MoRIIO] Support PP for prefill instance in PD disaggregated serving with MoRI WRITE mode (#64693)
- **2026-11-09** [`d7710bf059`](https://github.com/vllm-project/vllm/commit/d7710bf059) [#66397](https://github.com/vllm-project/vllm/pull/66397) — [ROCm][Bugfix] Build DSv4.1 replay builders at warmup and the DSv4/DSv4.1 mono runner at load (#66397)
- **2026-11-09** [`946690f392`](https://github.com/vllm-project/vllm/commit/946690f392) [#66548](https://github.com/vllm-project/vllm/pull/66548) — [ROCm][CI] Fix stale W4A16 intermediate_pad expectation in AITER MXFP4 padding test (#66548)
- **2026-11-09** [`166c03874e`](https://github.com/vllm-project/vllm/commit/166c03874e) [#66268](https://github.com/vllm-project/vllm/pull/66268) — [Recipe][ROCm] MiniMax-M3.1-Flash MI355X AgentX PD disaggregation over MoRI-IO (#66268)
- **2026-11-09** [`85b52c9f53`](https://github.com/vllm-project/vllm/commit/85b52c9f53) [#55855](https://github.com/vllm-project/vllm/pull/55855) — [Feature][KV Offload] Add RDMA-capable OBJ tier (#55855) (#56192)
- **2026-11-09** [`f86a3e29d7`](https://github.com/vllm-project/vllm/commit/f86a3e29d7) [#65559](https://github.com/vllm-project/vllm/pull/65559) — [ROCm][KV Offload] SimpleCPUOffload: batch copies on SDMA with hipMemcpyFlagExtPreferCE (HIP 7.16+) (#65559)
- **2026-11-09** [`e9ac740259`](https://github.com/vllm-project/vllm/commit/e9ac740259) [#65995](https://github.com/vllm-project/vllm/pull/65995) — [Bugfix][ROCm] Support AITER's preload() in FlyDSL INT4 QuickReduce init (#65995)
- **2026-11-09** [`5dd9b8b5e9`](https://github.com/vllm-project/vllm/commit/5dd9b8b5e9) [#66316](https://github.com/vllm-project/vllm/pull/66316) — [CI][ROCm] Mirror LM Eval ReplaySSM on MI355 (#66316)
- **2026-11-09** [`6ae300e589`](https://github.com/vllm-project/vllm/commit/6ae300e589) [#66310](https://github.com/vllm-project/vllm/pull/66310) — [CI][ROCm] Mirror MiniMax-M3 Model Tests on MI355 (#66310)
- **2026-11-09** [`a3c14efbc7`](https://github.com/vllm-project/vllm/commit/a3c14efbc7) [#66308](https://github.com/vllm-project/vllm/pull/66308) — [CI][ROCm] Mirror BF16x3 Router GEMM Kernels on MI355 (#66308)
- **2026-11-09** [`fdd90995db`](https://github.com/vllm-project/vllm/commit/fdd90995db) [#63096](https://github.com/vllm-project/vllm/pull/63096) — [ROCm][Spec Decode] Enable fused multi-step draft decode for ROCM_AITER_UNIFIED_ATTN (#63096)
- **2026-11-09** [`b936e1427f`](https://github.com/vllm-project/vllm/commit/b936e1427f) [#66177](https://github.com/vllm-project/vllm/pull/66177) — [Spec Decode][PP] Centralize auxiliary hidden-state relay (#66177)
- **2026-11-09** [`3f6f0fd08f`](https://github.com/vllm-project/vllm/commit/3f6f0fd08f) [#66434](https://github.com/vllm-project/vllm/pull/66434) — [CI][ROCm] Keep FLA's shared memory probe from initializing HIP (#66434)
- **2026-11-09** [`62902f6ce6`](https://github.com/vllm-project/vllm/commit/62902f6ce6) [#66350](https://github.com/vllm-project/vllm/pull/66350) — [Bugfix][ROCm] Let the FP8 MoE oracle fall back when the global AITER flag can't serve the layer (#66350)
- **2026-11-08** [`3b33a845c6`](https://github.com/vllm-project/vllm/commit/3b33a845c6) [#66206](https://github.com/vllm-project/vllm/pull/66206) — [ROCm][Test] Cover the MXFP4 W4A16 intermediate pad that reaches AITER (#66206)
- **2026-11-08** [`fd0c471b3a`](https://github.com/vllm-project/vllm/commit/fd0c471b3a) [#63401](https://github.com/vllm-project/vllm/pull/63401) — [Bugfix][ROCm] Size the extensible KV cache from exact VRAM use, not 2 MB-rounded free memory (#63401)
- **2026-11-08** [`5d840812d3`](https://github.com/vllm-project/vllm/commit/5d840812d3) [#66313](https://github.com/vllm-project/vllm/pull/66313) — [Deps] Bump tensorizer to 2.12.1 for Python 3.14 (#66313)
- **2026-11-08** [`c3a347a548`](https://github.com/vllm-project/vllm/commit/c3a347a548) [#66334](https://github.com/vllm-project/vllm/pull/66334) — [Model] Muse Spark Open Cleanup (#66334)
- **2026-11-08** [`c6b2d6ecbb`](https://github.com/vllm-project/vllm/commit/c6b2d6ecbb) [#62675](https://github.com/vllm-project/vllm/pull/62675) — [Bugfix][ROCm] Pad Qwen4Exp PLE n-gram inputs for piecewise CUDA graph replays (#62675)
- **2026-11-08** [`81a63508a7`](https://github.com/vllm-project/vllm/commit/81a63508a7) [#66189](https://github.com/vllm-project/vllm/pull/66189) — [ROCm][CI] Wait for DPX GPU lock to avoid collisions (#66189)
- **2026-11-08** [`cbe948fe0c`](https://github.com/vllm-project/vllm/commit/cbe948fe0c) [#66343](https://github.com/vllm-project/vllm/pull/66343) — [Recipe] Kimi-K3.1-Pro: add MI355X concurrency-1 preset, align with InferenceX#4887 (#66343)
- **2026-11-08** [`d76fe936a1`](https://github.com/vllm-project/vllm/commit/d76fe936a1) [#65092](https://github.com/vllm-project/vllm/pull/65092) — [Bugfix][ROCm] Reserve kpool decode indexer logits in workspace during profiling (#65092)
- **2026-11-08** [`fd8f3f398e`](https://github.com/vllm-project/vllm/commit/fd8f3f398e) [#66328](https://github.com/vllm-project/vllm/pull/66328) — [CI][ROCm] Force fork in test_preprocess_error_handling (#66328)
- **2026-11-08** [`666d42c222`](https://github.com/vllm-project/vllm/commit/666d42c222) [#66329](https://github.com/vllm-project/vllm/pull/66329) — [CI][ROCm][UMBP] Run the load setup store outside the 200 ms runtime (#66329)
- **2026-11-07** [`b46907cce0`](https://github.com/vllm-project/vllm/commit/b46907cce0) [#63166](https://github.com/vllm-project/vllm/pull/63166) — [ROCm][CI] Fix the test_qwen.py failure when AITER is on (#63166)
- **2026-11-07** [`308a3253c6`](https://github.com/vllm-project/vllm/commit/308a3253c6) [#66297](https://github.com/vllm-project/vllm/pull/66297) — [ROCm][CI] Make Zen5 CPU tests optional (#66297)
- **2026-11-07** [`5a4377a103`](https://github.com/vllm-project/vllm/commit/5a4377a103) [#61813](https://github.com/vllm-project/vllm/pull/61813) — [Chore] Use upstream Transformers MiniMaxM3VLConfig (#61813)
- **2026-11-07** [`7759f27e4a`](https://github.com/vllm-project/vllm/commit/7759f27e4a) [#65957](https://github.com/vllm-project/vllm/pull/65957) — [ROCm][CI] Cache only a ROCm stack the PR's CI pushed itself (#65957)
- **2026-11-07** [`6b3c7ce724`](https://github.com/vllm-project/vllm/commit/6b3c7ce724) [#65743](https://github.com/vllm-project/vllm/pull/65743) — [Refactor] Remove dead code kernels (#65743)
- **2026-11-07** [`a34565bc77`](https://github.com/vllm-project/vllm/commit/a34565bc77) [#49459](https://github.com/vllm-project/vllm/pull/49459) — [Model Loader] Remove per-load completeness checks (#49459)
- **2026-11-07** [`1ecc9cc4ce`](https://github.com/vllm-project/vllm/commit/1ecc9cc4ce) [#64994](https://github.com/vllm-project/vllm/pull/64994) — [Perf][DCP] Up-project the MLA decode output before the A2A merge (#64994)
- **2026-11-07** [`87187154b7`](https://github.com/vllm-project/vllm/commit/87187154b7) [#65508](https://github.com/vllm-project/vllm/pull/65508) — [ROCm][Perf][MiniMax-M3.1] Emit the o_proj MXFP8 input from the NVFP4 sparse decode kernel (#65508)
- **2026-11-07** [`339017c3ed`](https://github.com/vllm-project/vllm/commit/339017c3ed) [#64476](https://github.com/vllm-project/vllm/pull/64476) — [Spec Decode][DSpark] Fuse the Markov bias and block combine into Gumbel sampling (#64476)
- **2026-11-07** [`f98575ec13`](https://github.com/vllm-project/vllm/commit/f98575ec13) [#66205](https://github.com/vllm-project/vllm/pull/66205) — [ROCm][CI] Fix skip condition for test_block_fp8.py  (#66205)
- **2026-11-07** [`204e2ece5f`](https://github.com/vllm-project/vllm/commit/204e2ece5f) [#66217](https://github.com/vllm-project/vllm/pull/66217) — [ROCm][CI] Set speculative_config in test_rocm_triton_attn_dsv4.py to fix (MI355 DPX) Attention Kernels Shard %N (#66217)
- **2026-11-07** [`1648fefab9`](https://github.com/vllm-project/vllm/commit/1648fefab9) [#61796](https://github.com/vllm-project/vllm/pull/61796) — [Test][UMBP][8/10] Add standalone runtime coverage (#61796)
- **2026-11-07** [`80e0cd68f8`](https://github.com/vllm-project/vllm/commit/80e0cd68f8) [#66188](https://github.com/vllm-project/vllm/pull/66188) — [Recipe][ROCm] MiniMax-M3.1-Flash MI355X AgentX: nightly image and the opt-in optimizations (#66188)
- **2026-11-07** [`8176238c97`](https://github.com/vllm-project/vllm/commit/8176238c97) [#61816](https://github.com/vllm-project/vllm/pull/61816) — [ROCm][Bugfix] Stop declaring the MXFP4 MoE intermediate padding to AITER (#61816)
- **2026-11-06** [`2aca74f916`](https://github.com/vllm-project/vllm/commit/2aca74f916) [#62298](https://github.com/vllm-project/vllm/pull/62298) — [CI][ROCm] Run ROCm-capable tests that are currently skipped on AMD (#62298)
- **2026-11-06** [`2ced9ceb97`](https://github.com/vllm-project/vllm/commit/2ced9ceb97) [#65517](https://github.com/vllm-project/vllm/pull/65517) — [Bugfix][ROCm][MoE] Fix tkw1 rejecting count-free expert metadata, rename AITER QuantMethod (#65517)
- **2026-11-06** [`a41a6e1cd9`](https://github.com/vllm-project/vllm/commit/a41a6e1cd9) [#64131](https://github.com/vllm-project/vllm/pull/64131) — [ROCm][CI] Keep nightlies off PR-writable images and trim the csrc cache key (#64131)
- **2026-11-06** [`91630dd0c8`](https://github.com/vllm-project/vllm/commit/91630dd0c8) [#65145](https://github.com/vllm-project/vllm/pull/65145) — [CI] Bake hash-locked KV connectors into the CI image and re-enable their jobs (#65145)
- **2026-11-06** [`10c8574264`](https://github.com/vllm-project/vllm/commit/10c8574264) [#63890](https://github.com/vllm-project/vllm/pull/63890) — [ROCm][Perf] Use AITER's all-gather for small TP all-gathers (#63890)
- **2026-11-06** [`266e163d1e`](https://github.com/vllm-project/vllm/commit/266e163d1e) [#61448](https://github.com/vllm-project/vllm/pull/61448) — [ROCm][Model] Add fusions for Muse Glimmer for AMD backend (#61448)
- **2026-11-06** [`035acf120f`](https://github.com/vllm-project/vllm/commit/035acf120f) [#62718](https://github.com/vllm-project/vllm/pull/62718) — [ROCm][Build][3/5] Speed up ROCm build: split the skinny GEMMs per kernel family and trim torch headers (#62718)
- **2026-11-06** [`1ae936d539`](https://github.com/vllm-project/vllm/commit/1ae936d539) [#63365](https://github.com/vllm-project/vllm/pull/63365) — [ROCm][Build][5/5] Speed up ROCm build: instantiate the fused MUSE-Spark op per head size (#63365)
- **2026-11-06** [`65773f0696`](https://github.com/vllm-project/vllm/commit/65773f0696) [#63574](https://github.com/vllm-project/vllm/pull/63574) — [Security] Raise patched runtime and test dependency floors (#63574)
- **2026-11-06** [`d06fe4960e`](https://github.com/vllm-project/vllm/commit/d06fe4960e) [#65804](https://github.com/vllm-project/vllm/pull/65804) — [Spec Decode] Treat standalone draft model prefill as decode (#65804)
- **2026-11-06** [`8af2080e71`](https://github.com/vllm-project/vllm/commit/8af2080e71) [#66046](https://github.com/vllm-project/vllm/pull/66046) — [ROCm][CI] Skip the unlimited OCR tests until the ROCm CK OCR2 DASH updates land (#66046)
- **2026-11-06** [`cf0e7c7e55`](https://github.com/vllm-project/vllm/commit/cf0e7c7e55) [#66044](https://github.com/vllm-project/vllm/pull/66044) — [Doc][Bugfix] Fix strict docs build broken by unresolved autorefs (#66044)
- **2026-11-06** [`51ae6f4da1`](https://github.com/vllm-project/vllm/commit/51ae6f4da1) [#65914](https://github.com/vllm-project/vllm/pull/65914) — [Model Loader] One finish for every update path; drop refresh_derived_weights (#65914)
- **2026-11-06** [`bda81524e4`](https://github.com/vllm-project/vllm/commit/bda81524e4) [#65971](https://github.com/vllm-project/vllm/pull/65971) — [ROCm][Kernel] Follow-ups to the gfx942 MLA Triton verify kernel (#65971)
- **2026-11-06** [`c2c7158a01`](https://github.com/vllm-project/vllm/commit/c2c7158a01) [#65937](https://github.com/vllm-project/vllm/pull/65937) — [ROCm] Bump AITER to v0.1.28.post1 (#65937)
- **2026-11-06** [`e336407a3d`](https://github.com/vllm-project/vllm/commit/e336407a3d) [#65478](https://github.com/vllm-project/vllm/pull/65478) — [ROCm][Perf][MiniMax-M3.1] Fuse the FFN-side MXFP8 activation quant into the post-attention norm and swiglu (#65478)
- **2026-11-06** [`405aaa3d51`](https://github.com/vllm-project/vllm/commit/405aaa3d51) [#65530](https://github.com/vllm-project/vllm/pull/65530) — [ROCm][Perf][MiniMax-M3.1] Retune the MXFP8 dot_scaled GEMM tiles for M=17-256 (#65530)
- **2026-11-06** [`b8a3e82dcd`](https://github.com/vllm-project/vllm/commit/b8a3e82dcd) [#65481](https://github.com/vllm-project/vllm/pull/65481) — [ROCm][Perf][MiniMax-M3.1] Pick the NVFP4 sparse decode splits per XCD, not per CU (#65481)
- **2026-11-06** [`2eae5ee9be`](https://github.com/vllm-project/vllm/commit/2eae5ee9be) [#65722](https://github.com/vllm-project/vllm/pull/65722) — [Bugfix][ROCm] Stop AITER FA from skipping 1-token prompts in prefill/extend (#65722)
- **2026-11-06** [`e740badc2e`](https://github.com/vllm-project/vllm/commit/e740badc2e) [#64958](https://github.com/vllm-project/vllm/pull/64958) — [ROCm][Kimi-K3] Support Mooncake consumers with specialized decode (#64958)
- **2026-11-06** [`3eab4a4768`](https://github.com/vllm-project/vllm/commit/3eab4a4768) [#65988](https://github.com/vllm-project/vllm/pull/65988) — [ROCm][CI] Let /ci rocm cache start its main build on AMD CI (#65988)
- **2026-11-06** [`84e17e1ba5`](https://github.com/vllm-project/vllm/commit/84e17e1ba5) [#65386](https://github.com/vllm-project/vllm/pull/65386) — Minimax m3.1 dspark drafter monokernel (#65386)
- **2026-11-06** [`1e89fd1125`](https://github.com/vllm-project/vllm/commit/1e89fd1125) [#65267](https://github.com/vllm-project/vllm/pull/65267) — [Perf][ROCm][MiniMax-M3.1] Add opt-in parallel decode top-k (#65267)
- **2026-11-06** [`a7809d0cc5`](https://github.com/vllm-project/vllm/commit/a7809d0cc5) [#65968](https://github.com/vllm-project/vllm/pull/65968) — [Docs][ROCm] Fix stale AMD recipe images for GLM-5 and GLM-5.1 (#65968)
- **2026-11-06** [`c59d545909`](https://github.com/vllm-project/vllm/commit/c59d545909) [#65599](https://github.com/vllm-project/vllm/pull/65599) — [ROCm][Step5] Use one warp for CSA prefill sparse attention on CDNA3/CDNA4 (#65599)
- **2026-11-06** [`6f74a43da1`](https://github.com/vllm-project/vllm/commit/6f74a43da1) [#65249](https://github.com/vllm-project/vllm/pull/65249) — [ROCm][DSv4.1] Enable prefix-cache SWA replay on gfx942 (#65249)
- **2026-11-05** [`96a6a37e86`](https://github.com/vllm-project/vllm/commit/96a6a37e86) [#62717](https://github.com/vllm-project/vllm/pull/62717) — [ROCm][Build][2/5] Speed up ROCm build: split the topk softplus-sqrt instantiations per dtype (#62717)
- **2026-11-05** [`6128b9072d`](https://github.com/vllm-project/vllm/commit/6128b9072d) [#60487](https://github.com/vllm-project/vllm/pull/60487) — [Bugfix][ROCm] Count attention sinks once in AITER FA chunked-context extend (#60487)
- **2026-11-05** [`5f2edcec96`](https://github.com/vllm-project/vllm/commit/5f2edcec96) [#63364](https://github.com/vllm-project/vllm/pull/63364) — [ROCm][Build][4/5] Speed up ROCm build: instantiate the int4 skinny GEMM per output width (#63364)
- **2026-11-05** [`c0b393a064`](https://github.com/vllm-project/vllm/commit/c0b393a064) [#65912](https://github.com/vllm-project/vllm/pull/65912) — [ROCm][CI] Fix flaky streaming checks in test_translation_validation (#65912)
- **2026-11-05** [`4d77f0b236`](https://github.com/vllm-project/vllm/commit/4d77f0b236) [#65276](https://github.com/vllm-project/vllm/pull/65276) — [ROCm][CI] Cache a PR's ROCm base image for main with `/ci rocm cache` (#65276)
- **2026-11-05** [`82aeedf8db`](https://github.com/vllm-project/vllm/commit/82aeedf8db) [#65908](https://github.com/vllm-project/vllm/pull/65908) — [ROCm][CI] Fix flaky layer 0 bound in test_dsv4_mono_layers (#65908)
- **2026-11-05** [`c8168f5ab0`](https://github.com/vllm-project/vllm/commit/c8168f5ab0) [#65916](https://github.com/vllm-project/vllm/pull/65916) — [ROCm][CI] Shard Spec Decode AL MTP with pytest-shard after the Gemma4 dataset split (#65916)
- **2026-11-05** [`831dd92674`](https://github.com/vllm-project/vllm/commit/831dd92674) [#65895](https://github.com/vllm-project/vllm/pull/65895) — [CI] Use a repository-scoped Docker Hub secret for release publishing (#65895)
- **2026-11-05** [`7940e5e06f`](https://github.com/vllm-project/vllm/commit/7940e5e06f) [#65889](https://github.com/vllm-project/vllm/pull/65889) — [CI] Limit ROCm Docker Hub login to image publishing (#65889)
- **2026-11-05** [`1efcaa98ff`](https://github.com/vllm-project/vllm/commit/1efcaa98ff) [#63956](https://github.com/vllm-project/vllm/pull/63956) — [Perf][DSA] Token-sharded sparse-MLA prefill under TP; remove indexer row sharding (#63956)
- **2026-11-05** [`732e49d442`](https://github.com/vllm-project/vllm/commit/732e49d442) [#63231](https://github.com/vllm-project/vllm/pull/63231) — [Core] Change default --block-size from 16 to 64 (#63231)
- **2026-11-05** [`7187c01de5`](https://github.com/vllm-project/vllm/commit/7187c01de5) [#59124](https://github.com/vllm-project/vllm/pull/59124) — [ROCm][Perf][MLA] Add opt-in FlyDSL FP8 prefill attention for AITER MLA (#59124)
- **2026-11-05** [`ae96354d8b`](https://github.com/vllm-project/vllm/commit/ae96354d8b) [#63730](https://github.com/vllm-project/vllm/pull/63730) — [ROCm][Perf] Kimi-K3 prefill GEMMs on AITER tuned kernels (#63730)
- **2026-11-05** [`c2bc949186`](https://github.com/vllm-project/vllm/commit/c2bc949186) [#65812](https://github.com/vllm-project/vllm/pull/65812) — [Bugfix] Honor checkpoint FP8 KV scales in Qwen4Exp QSA (#65812)
- **2026-11-05** [`db914cad5b`](https://github.com/vllm-project/vllm/commit/db914cad5b) [#63117](https://github.com/vllm-project/vllm/pull/63117) — [Bugfix][ROCm] Take the AITER MLA KV cache dtype from the group's spec (#63117)
- **2026-11-05** [`e5d0ef3527`](https://github.com/vllm-project/vllm/commit/e5d0ef3527) [#64886](https://github.com/vllm-project/vllm/pull/64886) — [Bugfix][ROCm][Kimi-K3] Refresh derived weight copies after in-place weight writes (#64886)
- **2026-11-05** [`49c1a73a2e`](https://github.com/vllm-project/vllm/commit/49c1a73a2e) [#63891](https://github.com/vllm-project/vllm/pull/63891) — [ROCm][Perf][DSv4.1] Run DSpark's fused Markov sampling on gfx950 with --monokernel (#63891)
- **2026-11-05** [`1929f16945`](https://github.com/vllm-project/vllm/commit/1929f16945) [#63888](https://github.com/vllm-project/vllm/pull/63888) — [ROCm][Perf][DSv4.1] Skip the top-k -1 fill on the rows vLLM's decode top-k writes (#63888)
- **2026-11-05** [`aa81e6784e`](https://github.com/vllm-project/vllm/commit/aa81e6784e) [#62725](https://github.com/vllm-project/vllm/pull/62725) — [ROCm][Bugfix] Serve gfx942 MLA verify past 4 tokens with a Triton kernel (#62725)
- **2026-11-05** [`c6ae8d68f2`](https://github.com/vllm-project/vllm/commit/c6ae8d68f2) [#63027](https://github.com/vllm-project/vllm/pull/63027) — [ROCm][Perf][DSv4.1] Mono: tuned K1/K2 for the TP2 compress-ratio-2 layers on MI355X (#63027)
- **2026-11-04** [`cb2cf10f71`](https://github.com/vllm-project/vllm/commit/cb2cf10f71) [#65585](https://github.com/vllm-project/vllm/pull/65585) — [CI] Enroll the MI300 Batch Invariance (Distributed) mirror in automatic sharding (#65585)
- **2026-11-04** [`c5d1d77d2b`](https://github.com/vllm-project/vllm/commit/c5d1d77d2b) [#62057](https://github.com/vllm-project/vllm/pull/62057) — [ROCm][Model] Add Beam 1.0 support on ROCm  (#62057)
- **2026-11-04** [`beaa72618e`](https://github.com/vllm-project/vllm/commit/beaa72618e) [#60919](https://github.com/vllm-project/vllm/pull/60919) — [JIT][ROCm] Fully warmup GLM-5.3-Flash (#60919)
- **2026-11-04** [`1706c7be7f`](https://github.com/vllm-project/vllm/commit/1706c7be7f) [#64656](https://github.com/vllm-project/vllm/pull/64656) — [Test][UMBP] Restore a Mamba2 hybrid end to end through UMBP (#64656)
- **2026-11-04** [`586d2f7324`](https://github.com/vllm-project/vllm/commit/586d2f7324) [#63367](https://github.com/vllm-project/vllm/pull/63367) — [ROCm][DSv4.1] Shard the Engram gate so TP ranks gather only the value slice (#63367)
- **2026-11-04** [`9b34fec744`](https://github.com/vllm-project/vllm/commit/9b34fec744) [#61770](https://github.com/vllm-project/vllm/pull/61770) — [Bugfix][ROCm][Qwen4Exp] Remap Quark layer names for the MTP draft model (#61770)
- **2026-11-04** [`7871c62b61`](https://github.com/vllm-project/vllm/commit/7871c62b61) [#59802](https://github.com/vllm-project/vllm/pull/59802) — [ROCm][DSv4.1][Perf] Overlap the mHC gate projection with attention and FFN (#59802)
- **2026-11-04** [`67e6ea21a7`](https://github.com/vllm-project/vllm/commit/67e6ea21a7) [#65425](https://github.com/vllm-project/vllm/pull/65425) — [ROCm][CI] Restore the Torch Stable ABI Audit mirror with a locked audit tool (#65425)
- **2026-11-04** [`bb6f5ca3f4`](https://github.com/vllm-project/vllm/commit/bb6f5ca3f4) [#65641](https://github.com/vllm-project/vllm/pull/65641) — [ROCm][CI] Skip the GPU coredump in MonoKernel fault-injection tests (#65641)
- **2026-11-04** [`5225a1f17f`](https://github.com/vllm-project/vllm/commit/5225a1f17f) [#64658](https://github.com/vllm-project/vllm/pull/64658) — [Test][UMBP] Cover end-to-end restore while the embedded DRAM pool is evicting (#64658)
- **2026-11-04** [`ca8bd4c055`](https://github.com/vllm-project/vllm/commit/ca8bd4c055) [#65432](https://github.com/vllm-project/vllm/pull/65432) — [ROCm][Perf][MiniMax-M3.1] Score DSpark 7 decode locally below 3 requests instead of via indexer CP (#65432)
- **2026-11-04** [`dd4e40142a`](https://github.com/vllm-project/vllm/commit/dd4e40142a) [#64836](https://github.com/vllm-project/vllm/pull/64836) — [ROCm][Step5] Exercise the real CSA decode and engine paths in tests (#64836)
- **2026-11-04** [`e5d9bad98e`](https://github.com/vllm-project/vllm/commit/e5d9bad98e) [#64763](https://github.com/vllm-project/vllm/pull/64763) — [ROCm][HY4] Use breakable graphs without torch.compile (#64763)
- **2026-11-04** [`c0c8373c23`](https://github.com/vllm-project/vllm/commit/c0c8373c23) [#65087](https://github.com/vllm-project/vllm/pull/65087) — [ROCm][Perf][MiniMax-M3.1] Four-wave decode top-k for the NVFP4 indexer (#65087)
- **2026-11-03** [`8426f16135`](https://github.com/vllm-project/vllm/commit/8426f16135) [#63419](https://github.com/vllm-project/vllm/pull/63419) — [ROCm] Migrate Aiter sigmoid to topk_gating (#63419)
- **2026-11-03** [`81f1baa731`](https://github.com/vllm-project/vllm/commit/81f1baa731) [#63949](https://github.com/vllm-project/vllm/pull/63949) — [ROCm][CI] Untrusted base builds wait for main's images instead of rebuilding them (#63949)
- **2026-11-03** [`472e23f7da`](https://github.com/vllm-project/vllm/commit/472e23f7da) [#64132](https://github.com/vllm-project/vllm/pull/64132) — [ROCm][CI] Bake the fast-exit plugin into the test image and fix the ray-compat pin strip (#64132)
- **2026-11-03** [`81a2879403`](https://github.com/vllm-project/vllm/commit/81a2879403) [#62565](https://github.com/vllm-project/vllm/pull/62565) — [ROCm][Perf] Fix Kimi-K2.6 int4 MoE prefill regression on Triton 3.8 (gfx950 tuned config) (#62565)
- **2026-11-03** [`275816d060`](https://github.com/vllm-project/vllm/commit/275816d060) [#62750](https://github.com/vllm-project/vllm/pull/62750) — [Quantization] Block Hadamard input rotation for linear layers: online `mxfp4_hadamard32` and Quark online-rotation checkpoints (#62750)
- **2026-11-03** [`32a4dbfdaf`](https://github.com/vllm-project/vllm/commit/32a4dbfdaf) [#64241](https://github.com/vllm-project/vllm/pull/64241) — [CI] Pin existing dependency hashes and enforce immutable references (#64241)
- **2026-11-03** [`4d2fa5637c`](https://github.com/vllm-project/vllm/commit/4d2fa5637c) [#60418](https://github.com/vllm-project/vllm/pull/60418) — [ROCm] [RDNA] [Perf] Add tuned configs for TRITON_ATTN kernel and swap places of TRITON_ATTN and ROCM_ATTN in priority list (#60418)
- **2026-11-03** [`8d3db204b6`](https://github.com/vllm-project/vllm/commit/8d3db204b6) [#64317](https://github.com/vllm-project/vllm/pull/64317) — [ROCm][Perf] Keep 32-bit buffer addressing for per-token-head KV and AITER cross-attention fallback (#64317)
- **2026-11-03** [`ac16e0caa4`](https://github.com/vllm-project/vllm/commit/ac16e0caa4) [#65322](https://github.com/vllm-project/vllm/pull/65322) — [ROCm][Perf] W4A16: retune int4 skinny GEMM decode tuples for gfx115x (#65322)
- **2026-11-03** [`c1d8fade8d`](https://github.com/vllm-project/vllm/commit/c1d8fade8d) [#56450](https://github.com/vllm-project/vllm/pull/56450) — [ROCm][Perf] Encoder prefill attention on gfx1151: split-D head dims, alignment hint, launch config (#56450)
- **2026-11-03** [`a12e122206`](https://github.com/vllm-project/vllm/commit/a12e122206) [#56307](https://github.com/vllm-project/vllm/pull/56307) — [ROCm][Kernel] New "hip" GDN backend for gfx1151 (#56307)
- **2026-11-03** [`bb86df34d7`](https://github.com/vllm-project/vllm/commit/bb86df34d7) [#65418](https://github.com/vllm-project/vllm/pull/65418) — [Bugfix][ROCm] Raise the extensible KV cache margin floor to 3 GiB (#65418)
- **2026-11-03** [`7c284bf150`](https://github.com/vllm-project/vllm/commit/7c284bf150) [#63835](https://github.com/vllm-project/vllm/pull/63835) — [ROCm][Perf][Bugfix] wvSplitK: launch tiles of their own for gfx1151 and gfx1150; fix bigType for A_CHUNK 16 (#63835)
- **2026-11-03** [`0eeae6a473`](https://github.com/vllm-project/vllm/commit/0eeae6a473) [#65030](https://github.com/vllm-project/vllm/pull/65030) — [Perf][Model] DeepSeek V4/V4.1 Vision: encode a call's images in packed passes (#65030)
- **2026-11-03** [`22d05b87bb`](https://github.com/vllm-project/vllm/commit/22d05b87bb) [#65296](https://github.com/vllm-project/vllm/pull/65296) — [Model Loader] DeepSeek-V4 ROCm: keep the preshuffle scales out of the module's parameters (#65296)
- **2026-11-03** [`a8718969d2`](https://github.com/vllm-project/vllm/commit/a8718969d2) [#64330](https://github.com/vllm-project/vllm/pull/64330) — [Bugfix][ROCm][MoRIIO] Wait for MoRIIO WRITE mode completions in short chunks (#64330)
- **2026-11-03** [`67791dd94d`](https://github.com/vllm-project/vllm/commit/67791dd94d) [#62802](https://github.com/vllm-project/vllm/pull/62802) — [EPD] Support DeepSeek-V4.1 image metadata-only inputs (#62802)
- **2026-11-03** [`7ff48230e7`](https://github.com/vllm-project/vllm/commit/7ff48230e7) [#63204](https://github.com/vllm-project/vllm/pull/63204) — [Refactor][ROCm][MoE] Let each AiterExperts subclass own its AITER call args (#63204)
- **2026-11-03** [`75be138428`](https://github.com/vllm-project/vllm/commit/75be138428) [#64096](https://github.com/vllm-project/vllm/pull/64096) — [KV Connector][Spec Decode] Support lookahead block hashes in KV connectors (#64096)
- **2026-11-03** [`8a702b18a1`](https://github.com/vllm-project/vllm/commit/8a702b18a1) [#63076](https://github.com/vllm-project/vllm/pull/63076) — [ROCm][Perf] Triton sigmoid+bias top-k when MoE grouping eliminates nothing (#63076)
- **2026-11-03** [`254a2a3390`](https://github.com/vllm-project/vllm/commit/254a2a3390) [#61435](https://github.com/vllm-project/vllm/pull/61435) — [ROCm][Perf][Kimi-K3] Specialized decode on MI355X: K1/K2 + MLA M1a/M1b (FlyDSL, TP8, DCP1/DCP8) (#61435)
- **2026-11-02** [`5da6f2e274`](https://github.com/vllm-project/vllm/commit/5da6f2e274) [#64174](https://github.com/vllm-project/vllm/pull/64174) — [CI] Enroll four Nightly steps and three AMD mirrors in automatic sharding (#64174)
- **2026-11-02** [`f5044745aa`](https://github.com/vllm-project/vllm/commit/f5044745aa) [#64839](https://github.com/vllm-project/vllm/pull/64839) — [ROCm][CI] Add a build.sh prebuild mode for maintainer-approved stack builds (#64839)
- **2026-11-02** [`af751a9edc`](https://github.com/vllm-project/vllm/commit/af751a9edc) [#64657](https://github.com/vllm-project/vllm/pull/64657) — [Test][UMBP] Cover TP=2 restore through per-rank MORI pools (#64657)
- **2026-11-02** [`27072f9cd3`](https://github.com/vllm-project/vllm/commit/27072f9cd3) [#63426](https://github.com/vllm-project/vllm/pull/63426) — [ROCm][CI] Print the native backtrace of a fault in AMD CI pytest runs (#63426)
- **2026-11-02** [`bf1dbed3ea`](https://github.com/vllm-project/vllm/commit/bf1dbed3ea) [#64833](https://github.com/vllm-project/vllm/pull/64833) — [ROCm][Step5] Require CDNA3 or newer for the sparse attention layers (#64833)
- **2026-11-02** [`26d198bd56`](https://github.com/vllm-project/vllm/commit/26d198bd56) [#64692](https://github.com/vllm-project/vllm/pull/64692) — [Model Loader] Refill weight-derived tensors in place on every post-load rerun (#64692)
- **2026-11-02** [`901f26dfcd`](https://github.com/vllm-project/vllm/commit/901f26dfcd) [#62270](https://github.com/vllm-project/vllm/pull/62270) — [ROCm][Perf][MiniMax-M3] Enable the fp8 indexer cache on gfx942 (#62270)
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

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#66387](https://github.com/vllm-project/vllm/issues/66387) | [Bug]: DFlash acceptance collapses at tensor parallel > 1 (MiMo-V2.6-F | — | 2026-11-09 |
| [#66610](https://github.com/vllm-project/vllm/issues/66610) | [Bug]: /detokenize returns 200 and silently drops out-of-vocabulary to | bug | 2026-11-09 |
| [#66525](https://github.com/vllm-project/vllm/issues/66525) | [Bug]: Gemma4 suppression-token cache causes UnexpectedTracerError on  | bug, tpu | 2026-11-09 |
| [#66587](https://github.com/vllm-project/vllm/issues/66587) | [ROCm][AMD] DeepSeek-V4.1-Flash gfx950 / MI355X Performance Optimizati | rocm, deepseek | 2026-11-09 |
| [#66588](https://github.com/vllm-project/vllm/issues/66588) | [ROCm][AMD] MiniMax-M3 gfx950 / MI355X Performance Optimization (vLLM) | rocm, minimax | 2026-11-09 |
| [#66392](https://github.com/vllm-project/vllm/issues/66392) | [Bug]: /v1/systemone caps Clef-Flash choice questions at 26 options, t | bug | 2026-11-09 |
| [#66250](https://github.com/vllm-project/vllm/issues/66250) | [Bug]: phi-2 crashes with CUDA illegal memory access during compile/wa | bug | 2026-11-09 |
| [#66557](https://github.com/vllm-project/vllm/issues/66557) | [Performance]: Adaptive verification's varlen decode graphs lose Trito | — | 2026-11-09 |
| [#60904](https://github.com/vllm-project/vllm/issues/60904) | [RFC]: A standard for Specialized (MonoKernels) Decodes in vllm/models | rocm, RFC, quantization, kimi | 2026-11-09 |
| [#65543](https://github.com/vllm-project/vllm/issues/65543) | [RFC]: Scheduler-owned persistent state, initially for cache-aware str | scheduler | 2026-11-09 |
| [#66192](https://github.com/vllm-project/vllm/issues/66192) | [Bug]: SM100 default prefill CUDA-graph grid (up to 8192 tokens, #6340 | — | 2026-11-09 |
| [#64572](https://github.com/vllm-project/vllm/issues/64572) | [Performance]: Triton and other eager attention backends re-derive K/V | quantization | 2026-11-09 |
| [#54477](https://github.com/vllm-project/vllm/issues/54477) | [RFC]: Direct Weight Reload for RL Training | RFC, quantization, kimi, k3 | 2026-11-09 |
| [#66452](https://github.com/vllm-project/vllm/issues/66452) | [Bug]: FlashInfer pinned planner workspace reuse corrupts async prefil | — | 2026-11-09 |
| [#64295](https://github.com/vllm-project/vllm/issues/64295) | [RFC]: Let replicas read each other's GPU KV cache (L1 sharing) | rocm | 2026-11-09 |
| [#64018](https://github.com/vllm-project/vllm/issues/64018) | [ROCm][AMD] Muse Spark Open PTPC-FP8 gfx942 Performance Optimization | performance, rocm | 2026-11-09 |
| [#59575](https://github.com/vllm-project/vllm/issues/59575) | [ROCm][AMD] Qwen3.8-Flash-Next gfx950 / MI355X Performance Optimizatio | performance, rocm, quantization, kimi | 2026-11-09 |
| [#66491](https://github.com/vllm-project/vllm/issues/66491) | [RFC]: Packed-weight INT4 GEMM (W4A16 / W4A8) for RDNA4 (gfx1200/gfx12 | rocm, RFC, quantization | 2026-11-09 |
| [#66467](https://github.com/vllm-project/vllm/issues/66467) | [RFC]: Faster Engram / PLE `disk_offload`: io_uring + O_DIRECT row rea | RFC | 2026-11-09 |
| [#57149](https://github.com/vllm-project/vllm/issues/57149) | [ROCm][AMD] Qwen3.8-2.4T-A95B gfx950 / MI355X Performance Optimization | performance, rocm, quantization, kimi | 2026-11-09 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 148 |
| Attention | 77 |
| MoE / Expert Parallel | 60 |
| Other | 55 |
| Multimodal | 45 |
| Serving / API | 43 |
| Models | 39 |
| CI / Build | 37 |
| KV Cache / Offload | 30 |
| Scheduler / Engine | 29 |
| Quantization | 29 |
| Disaggregation / PD | 24 |
| Perf / Benchmark | 18 |
| Speculative Decoding | 15 |
| LoRA | 11 |
| Docs | 10 |
| Compilation / CUDA Graph | 3 |
| Distributed | 2 |

## ROCm / AMD  (148 commits)

- **2026-11-09** [`e5bec1ddd4`](https://github.com/vllm-project/vllm/commit/e5bec1ddd4) [#66611](https://github.com/vllm-project/vllm/pull/66611)
  [ROCm][CI] Restore the simple-nemotron-h-8b GSM8K threshold on ROCm (#66611)
  _Files: `tests/evals/gsm8k/test_gsm8k_offloading.py`_
- **2026-11-09** [`85f6a26455`](https://github.com/vllm-project/vllm/commit/85f6a26455) [#65349](https://github.com/vllm-project/vllm/pull/65349)
  [Perf] Warm up JIT kernels that only long prefills, eager drafters and constrained decoding reach (#65349)
  _Files: `tests/distributed/test_dcp_a2a.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`, `tests/v1/attention/test_dcp_a2a_pack_mask.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+6 more__
- **2026-11-09** [`fe48798e86`](https://github.com/vllm-project/vllm/commit/fe48798e86) [#65940](https://github.com/vllm-project/vllm/pull/65940)
  [ROCm][CI] Run the MI355 BF16 AR-RMS fusion E2E matrices nightly with a per-PR subset (#65940)
  _Files: `.buildkite/test_areas/compile.yaml`_
- **2026-11-09** [`e090987a3b`](https://github.com/vllm-project/vllm/commit/e090987a3b) [#66307](https://github.com/vllm-project/vllm/pull/66307)
  [CI][ROCm] Add AMD HC kernel tests for Qwen4 Exp and mirror the B200 HC step (#66307)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/qwen4_exp/test_hc_ops_amd.py`_
- **2026-11-09** [`bbaef29734`](https://github.com/vllm-project/vllm/commit/bbaef29734) [#66338](https://github.com/vllm-project/vllm/pull/66338)
  [CI][ROCm] Restore the AMD mirror of Fault Tolerance E2E (#66338)
  _Files: `.buildkite/test_areas/fault_tolerance.yaml`_
- **2026-11-09** [`5b54aea9ec`](https://github.com/vllm-project/vllm/commit/5b54aea9ec) [#66425](https://github.com/vllm-project/vllm/pull/66425)
  [CI][Deps] Bump truststore to 0.10.5 to stop the OpenSSL segfault in HF downloads (#66425)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/kv_connectors_cuda.txt`, `requirements/test/rocm.txt` _+1 more__
- **2026-11-09** [`9ad0029883`](https://github.com/vllm-project/vllm/commit/9ad0029883) [#63847](https://github.com/vllm-project/vllm/pull/63847)
  [ROCm][Kernel] Support persistent_topk on ROCm (#63847)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `benchmarks/kernels/benchmark_top_k_per_row_decode.py`, `csrc/core/cuda_compat.h` _+10 more__
- **2026-11-09** [`56e5608d0f`](https://github.com/vllm-project/vllm/commit/56e5608d0f) [#64693](https://github.com/vllm-project/vllm/pull/64693)
  [ROCm][MoRIIO] Support PP for prefill instance in PD disaggregated serving with MoRI WRITE mode (#64693)
  _Files: `docs/features/moriio_connector_usage.md`, `tests/v1/kv_connector/unit/test_moriio_connector.py`, `tests/v1/kv_connector/unit/test_moriio_hetero_tp_write.py`, `tests/v1/kv_connector/unit/test_moriio_hma_scheduler.py` _+8 more__
- **2026-11-09** [`d7710bf059`](https://github.com/vllm-project/vllm/commit/d7710bf059) [#66397](https://github.com/vllm-project/vllm/pull/66397)
  [ROCm][Bugfix] Build DSv4.1 replay builders at warmup and the DSv4/DSv4.1 mono runner at load (#66397)
  _Files: `tests/models/test_deepseek_v41_replay_batch.py`, `tests/models/test_dsv4_mono_decode.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mono_decode.py` _+3 more__
- **2026-11-09** [`946690f392`](https://github.com/vllm-project/vllm/commit/946690f392) [#66548](https://github.com/vllm-project/vllm/pull/66548)
  [ROCm][CI] Fix stale W4A16 intermediate_pad expectation in AITER MXFP4 padding test (#66548)
  _Files: `tests/kernels/moe/test_modular_kernel_combinations.py`_
- **2026-11-09** [`166c03874e`](https://github.com/vllm-project/vllm/commit/166c03874e) [#66268](https://github.com/vllm-project/vllm/pull/66268)
  [Recipe][ROCm] MiniMax-M3.1-Flash MI355X AgentX PD disaggregation over MoRI-IO (#66268)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-11-09** [`f86a3e29d7`](https://github.com/vllm-project/vllm/commit/f86a3e29d7) [#65559](https://github.com/vllm-project/vllm/pull/65559)
  [ROCm][KV Offload] SimpleCPUOffload: batch copies on SDMA with hipMemcpyFlagExtPreferCE (HIP 7.16+) (#65559)
  _Files: `tests/v1/simple_kv_offload/test_hip_mem_ops.py`, `vllm/v1/simple_kv_offload/cuda_mem_ops.py`_
- **2026-11-09** [`e9ac740259`](https://github.com/vllm-project/vllm/commit/e9ac740259) [#65995](https://github.com/vllm-project/vllm/pull/65995)
  [Bugfix][ROCm] Support AITER's preload() in FlyDSL INT4 QuickReduce init (#65995)
  _Files: `tests/distributed/test_rocm_quick_reduce.py`, `vllm/distributed/device_communicators/quick_all_reduce.py`_
- **2026-11-09** [`5dd9b8b5e9`](https://github.com/vllm-project/vllm/commit/5dd9b8b5e9) [#66316](https://github.com/vllm-project/vllm/pull/66316)
  [CI][ROCm] Mirror LM Eval ReplaySSM on MI355 (#66316)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/Nemotron-3-Super-120B-A12B-FP8-ReplaySSM-align-MI355.yaml`, `tests/evals/gsm8k/configs/models-mi355-replayssm.txt`_
- **2026-11-09** [`6ae300e589`](https://github.com/vllm-project/vllm/commit/6ae300e589) [#66310](https://github.com/vllm-project/vllm/pull/66310)
  [CI][ROCm] Mirror MiniMax-M3 Model Tests on MI355 (#66310)
  _Files: `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/models_basic.yaml`_
- **2026-11-09** [`a3c14efbc7`](https://github.com/vllm-project/vllm/commit/a3c14efbc7) [#66308](https://github.com/vllm-project/vllm/pull/66308)
  [CI][ROCm] Mirror BF16x3 Router GEMM Kernels on MI355 (#66308)
  _Files: `.buildkite/test_areas/kernels.yaml`_
- **2026-11-09** [`fdd90995db`](https://github.com/vllm-project/vllm/commit/fdd90995db) [#63096](https://github.com/vllm-project/vllm/pull/63096)
  [ROCm][Spec Decode] Enable fused multi-step draft decode for ROCM_AITER_UNIFIED_ATTN (#63096)
  _Files: `tests/v1/attention/test_triton_attn_metadata_builder.py`, `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`_
- **2026-11-09** [`b936e1427f`](https://github.com/vllm-project/vllm/commit/b936e1427f) [#66177](https://github.com/vllm-project/vllm/pull/66177)
  [Spec Decode][PP] Centralize auxiliary hidden-state relay (#66177)
  _Files: `docs/features/speculative_decoding/eagle.md`, `tests/v1/e2e/spec_decode/eagle/test_eagle3_pp.py`, `tests/v1/worker/test_eagle3_aux_hidden_states_pp.py`, `vllm/benchmarks/forward/capture.py` _+19 more__
- **2026-11-09** [`3f6f0fd08f`](https://github.com/vllm-project/vllm/commit/3f6f0fd08f) [#66434](https://github.com/vllm-project/vllm/pull/66434)
  [CI][ROCm] Keep FLA's shared memory probe from initializing HIP (#66434)
  _Files: `vllm/third_party/flash_linear_attention/ops/utils.py`_
- **2026-11-09** [`62902f6ce6`](https://github.com/vllm-project/vllm/commit/62902f6ce6) [#66350](https://github.com/vllm-project/vllm/pull/66350)
  [Bugfix][ROCm] Let the FP8 MoE oracle fall back when the global AITER flag can't serve the layer (#66350)
  _Files: `tests/kernels/moe/test_moe_kernel_oracle.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`_
- **2026-11-08** [`3b33a845c6`](https://github.com/vllm-project/vllm/commit/3b33a845c6) [#66206](https://github.com/vllm-project/vllm/pull/66206)
  [ROCm][Test] Cover the MXFP4 W4A16 intermediate pad that reaches AITER (#66206)
  _Files: `tests/kernels/moe/test_rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`_
- **2026-11-08** [`fd0c471b3a`](https://github.com/vllm-project/vllm/commit/fd0c471b3a) [#63401](https://github.com/vllm-project/vllm/pull/63401)
  [Bugfix][ROCm] Size the extensible KV cache from exact VRAM use, not 2 MB-rounded free memory (#63401)
  _Files: `tests/utils_/test_rocm_vram_lookup.py`, `tests/v1/worker/test_extensible_kv_cache.py`, `tests/v1/worker/test_gpu_worker.py`, `tests/v1/worker/test_rocm_device_memory.py` _+6 more__
- **2026-11-08** [`5d840812d3`](https://github.com/vllm-project/vllm/commit/5d840812d3) [#66313](https://github.com/vllm-project/vllm/pull/66313)
  [Deps] Bump tensorizer to 2.12.1 for Python 3.14 (#66313)
  _Files: `requirements/rocm.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+6 more__
- **2026-11-08** [`c3a347a548`](https://github.com/vllm-project/vllm/commit/c3a347a548) [#66334](https://github.com/vllm-project/vllm/pull/66334)
  [Model] Muse Spark Open Cleanup (#66334)
  _Files: `csrc/fp32_router_gemm.cu`, `docs/features/tool_calling.md`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/multimodal/models/muse_spark.rs` _+65 more__
- **2026-11-08** [`c6b2d6ecbb`](https://github.com/vllm-project/vllm/commit/c6b2d6ecbb) [#62675](https://github.com/vllm-project/vllm/pull/62675)
  [Bugfix][ROCm] Pad Qwen4Exp PLE n-gram inputs for piecewise CUDA graph replays (#62675)
  _Files: `tests/models/qwen4_exp/test_config.py`, `vllm/models/qwen4_exp/amd/model_state.py`_
- **2026-11-08** [`81a63508a7`](https://github.com/vllm-project/vllm/commit/81a63508a7) [#66189](https://github.com/vllm-project/vllm/pull/66189)
  [ROCm][CI] Wait for DPX GPU lock to avoid collisions (#66189)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-11-08** [`cbe948fe0c`](https://github.com/vllm-project/vllm/commit/cbe948fe0c) [#66343](https://github.com/vllm-project/vllm/pull/66343)
  [Recipe] Kimi-K3.1-Pro: add MI355X concurrency-1 preset, align with InferenceX#4887 (#66343)
  _Files: `recipes/models/moonshotai/Kimi-K3.1-Pro.yaml`_
- **2026-11-08** [`d76fe936a1`](https://github.com/vllm-project/vllm/commit/d76fe936a1) [#65092](https://github.com/vllm-project/vllm/pull/65092)
  [Bugfix][ROCm] Reserve kpool decode indexer logits in workspace during profiling (#65092)
  _Files: `tests/models/glm5next/test_sparse_indexer_topk_dispatch.py`, `vllm/models/glm5next/amd/sparse_indexer.py`_
- **2026-11-08** [`fd8f3f398e`](https://github.com/vllm-project/vllm/commit/fd8f3f398e) [#66328](https://github.com/vllm-project/vllm/pull/66328)
  [CI][ROCm] Force fork in test_preprocess_error_handling (#66328)
  _Files: `tests/v1/engine/test_preprocess_error_handling.py`_
- **2026-11-08** [`666d42c222`](https://github.com/vllm-project/vllm/commit/666d42c222) [#66329](https://github.com/vllm-project/vllm/pull/66329)
  [CI][ROCm][UMBP] Run the load setup store outside the 200 ms runtime (#66329)
  _Files: `tests/v1/kv_connector/umbp_integration/test_mori_standalone_gpu.py`_
- **2026-11-07** [`b46907cce0`](https://github.com/vllm-project/vllm/commit/b46907cce0) [#63166](https://github.com/vllm-project/vllm/pull/63166)
  [ROCm][CI] Fix the test_qwen.py failure when AITER is on (#63166)
  _Files: `tests/models/multimodal/generation_ppl_test/conftest.py`, `tests/models/multimodal/generation_ppl_test/test_qwen.py`_
- **2026-11-07** [`308a3253c6`](https://github.com/vllm-project/vllm/commit/308a3253c6) [#66297](https://github.com/vllm-project/vllm/pull/66297)
  [ROCm][CI] Make Zen5 CPU tests optional (#66297)
  _Files: `.buildkite/hardware_tests/zen.yaml`_
- **2026-11-07** [`5a4377a103`](https://github.com/vllm-project/vllm/commit/5a4377a103) [#61813](https://github.com/vllm-project/vllm/pull/61813)
  [Chore] Use upstream Transformers MiniMaxM3VLConfig (#61813)
  _Files: `tests/distributed/test_minimax_m3_indexer_cp_tp.py`, `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/test_minimax_m3_dspark_draft.py`, `tests/model_executor/layers/test_fused_shared_expert.py` _+25 more__
- **2026-11-07** [`7759f27e4a`](https://github.com/vllm-project/vllm/commit/7759f27e4a) [#65957](https://github.com/vllm-project/vllm/pull/65957)
  [ROCm][CI] Cache only a ROCm stack the PR's CI pushed itself (#65957)
  _Files: `.buildkite/scripts/rocm/build.sh`, `.github/workflows/ci-command-tests.yml`, `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py` _+1 more__
- **2026-11-07** [`6b3c7ce724`](https://github.com/vllm-project/vllm/commit/6b3c7ce724) [#65743](https://github.com/vllm-project/vllm/pull/65743)
  [Refactor] Remove dead code kernels (#65743)
  _Files: `vllm/_aiter_ops.py`, `vllm/model_executor/kernels/linear/cute_dsl/_ll_fp32w_dotprod.py`, `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`, `vllm/model_executor/layers/quantization/humming.py` _+8 more__
- **2026-11-07** [`a34565bc77`](https://github.com/vllm-project/vllm/commit/a34565bc77) [#49459](https://github.com/vllm-project/vllm/pull/49459)
  [Model Loader] Remove per-load completeness checks (#49459)
  _Files: `tests/model_executor/model_loader/test_expert_substitution.py`, `tests/model_executor/model_loader/test_load_plan.py`, `tests/model_executor/model_loader/test_mtp_validation.py`, `tests/model_executor/model_loader/test_reload_lifecycle.py` _+50 more__
- **2026-11-07** [`1ecc9cc4ce`](https://github.com/vllm-project/vllm/commit/1ecc9cc4ce) [#64994](https://github.com/vllm-project/vllm/pull/64994)
  [Perf][DCP] Up-project the MLA decode output before the A2A merge (#64994)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`, `tests/distributed/test_dcp_a2a.py`, `tests/distributed/test_dcp_direct_a2a_lse_reduce.py` _+4 more__
- **2026-11-07** [`87187154b7`](https://github.com/vllm-project/vllm/commit/87187154b7) [#65508](https://github.com/vllm-project/vllm/pull/65508)
  [ROCm][Perf][MiniMax-M3.1] Emit the o_proj MXFP8 input from the NVFP4 sparse decode kernel (#65508)
  _Files: `tests/kernels/attention/test_minimax_m3_nvfp4_sparse_decode.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/nvfp4_sparse_decode/host.py`, `vllm/models/minimax_m3/amd/ops/nvfp4_sparse_decode/kernel.py` _+1 more__
- **2026-11-07** [`339017c3ed`](https://github.com/vllm-project/vllm/commit/339017c3ed) [#64476](https://github.com/vllm-project/vllm/pull/64476)
  [Spec Decode][DSpark] Fuse the Markov bias and block combine into Gumbel sampling (#64476)
  _Files: `tests/kernels/models/amd/test_dsv41_gfx942_fused_markov.py`, `tests/models/deepseek_v41/nvidia/test_fused_markov.py`, `tests/v1/spec_decode/test_dspark_topk.py`, `tests/v1/worker/test_gpu_gumbel_sample.py` _+2 more__
- **2026-11-07** [`f98575ec13`](https://github.com/vllm-project/vllm/commit/f98575ec13) [#66205](https://github.com/vllm-project/vllm/pull/66205)
  [ROCm][CI] Fix skip condition for test_block_fp8.py  (#66205)
  _Files: `tests/kernels/moe/test_block_fp8.py`_
- **2026-11-07** [`204e2ece5f`](https://github.com/vllm-project/vllm/commit/204e2ece5f) [#66217](https://github.com/vllm-project/vllm/pull/66217)
  [ROCm][CI] Set speculative_config in test_rocm_triton_attn_dsv4.py to fix (MI355 DPX) Attention Kernels Shard %N (#66217)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`_
- **2026-11-07** [`1648fefab9`](https://github.com/vllm-project/vllm/commit/1648fefab9) [#61796](https://github.com/vllm-project/vllm/pull/61796)
  [Test][UMBP][8/10] Add standalone runtime coverage (#61796)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `tests/v1/kv_connector/umbp_integration/test_mori_standalone_gpu.py`, `tests/v1/kv_connector/umbp_test_utils.py` _+3 more__
- **2026-11-07** [`80e0cd68f8`](https://github.com/vllm-project/vllm/commit/80e0cd68f8) [#66188](https://github.com/vllm-project/vllm/pull/66188)
  [Recipe][ROCm] MiniMax-M3.1-Flash MI355X AgentX: nightly image and the opt-in optimizations (#66188)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-11-07** [`8176238c97`](https://github.com/vllm-project/vllm/commit/8176238c97) [#61816](https://github.com/vllm-project/vllm/pull/61816)
  [ROCm][Bugfix] Stop declaring the MXFP4 MoE intermediate padding to AITER (#61816)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/kernels/moe/test_rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`_
- **2026-11-06** [`2aca74f916`](https://github.com/vllm-project/vllm/commit/2aca74f916) [#62298](https://github.com/vllm-project/vllm/pull/62298)
  [CI][ROCm] Run ROCm-capable tests that are currently skipped on AMD (#62298)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/compile.yaml` _+83 more__
- **2026-11-06** [`2ced9ceb97`](https://github.com/vllm-project/vllm/commit/2ced9ceb97) [#65517](https://github.com/vllm-project/vllm/pull/65517)
  [Bugfix][ROCm][MoE] Fix tkw1 rejecting count-free expert metadata, rename AITER QuantMethod (#65517)
  _Files: `tests/kernels/moe/test_mori_moe.py`, `tests/kernels/moe/test_muse_spark_rocm_bf16_moe.py`, `tests/kernels/moe/test_rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py` _+3 more__
- **2026-11-06** [`a41a6e1cd9`](https://github.com/vllm-project/vllm/commit/a41a6e1cd9) [#64131](https://github.com/vllm-project/vllm/pull/64131)
  [ROCm][CI] Keep nightlies off PR-writable images and trim the csrc cache key (#64131)
  _Files: `.buildkite/scripts/rocm/build.sh`, `docker/Dockerfile.rocm`, `tests/tools/test_rocm_build.py`_
- **2026-11-06** [`91630dd0c8`](https://github.com/vllm-project/vllm/commit/91630dd0c8) [#65145](https://github.com/vllm-project/vllm/pull/65145)
  [CI] Bake hash-locked KV connectors into the CI image and re-enable their jobs (#65145)
  _Files: `.buildkite/scripts/check-kv-connectors.sh`, `.buildkite/scripts/install-kv-connectors.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/disaggregated.yaml` _+20 more__
- **2026-11-06** [`10c8574264`](https://github.com/vllm-project/vllm/commit/10c8574264) [#63890](https://github.com/vllm-project/vllm/pull/63890)
  [ROCm][Perf] Use AITER's all-gather for small TP all-gathers (#63890)
  _Files: `benchmarks/kernels/benchmark_device_communicators.py`, `tests/distributed/test_comm_ops.py`, `vllm/distributed/device_communicators/aiter_custom_all_reduce.py`, `vllm/distributed/device_communicators/cuda_communicator.py`_
- **2026-11-06** [`266e163d1e`](https://github.com/vllm-project/vllm/commit/266e163d1e) [#61448](https://github.com/vllm-project/vllm/pull/61448)
  [ROCm][Model] Add fusions for Muse Glimmer for AMD backend (#61448)
  _Files: `tests/compile/passes/test_muse_glimmer_sandwich_norm_fusion.py`, `tests/compile/passes/test_rocm_aiter_qk_norm_rope_kvcache_fusion.py`, `vllm/compilation/passes/fusion/muse_glimmer_qk_rope_cache_fusion.py`, `vllm/compilation/passes/fusion/muse_glimmer_sandwich_norm_fusion.py` _+2 more__
- **2026-11-06** [`035acf120f`](https://github.com/vllm-project/vllm/commit/035acf120f) [#62718](https://github.com/vllm-project/vllm/pull/62718)
  [ROCm][Build][3/5] Speed up ROCm build: split the skinny GEMMs per kernel family and trim torch headers (#62718)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`, `CMakeLists.txt`, `csrc/rocm/quickreduce/custom_quickreduce.cu` _+10 more__
- **2026-11-06** [`1ae936d539`](https://github.com/vllm-project/vllm/commit/1ae936d539) [#63365](https://github.com/vllm-project/vllm/pull/63365)
  [ROCm][Build][5/5] Speed up ROCm build: instantiate the fused MUSE-Spark op per head size (#63365)
  _Files: `CMakeLists.txt`, `csrc/fused_muse_spark_qknorm_rope_kv_insert_api.cu`, `csrc/fused_muse_spark_qknorm_rope_kv_insert_entry.h`, `csrc/fused_muse_spark_qknorm_rope_kv_insert_hd128.cu` _+3 more__
- **2026-11-06** [`65773f0696`](https://github.com/vllm-project/vllm/commit/65773f0696) [#63574](https://github.com/vllm-project/vllm/pull/63574)
  [Security] Raise patched runtime and test dependency floors (#63574)
  _Files: `docker/Dockerfile.rocm`, `requirements/common.txt`, `requirements/docs.in`, `requirements/docs.txt` _+7 more__
- **2026-11-06** [`d06fe4960e`](https://github.com/vllm-project/vllm/commit/d06fe4960e) [#65804](https://github.com/vllm-project/vllm/pull/65804)
  [Spec Decode] Treat standalone draft model prefill as decode (#65804)
  _Files: `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py`, `tests/models/kimi_k3/test_amd_kda_checkpoint.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `tests/v1/attention/test_attention_backends.py` _+7 more__
- **2026-11-06** [`8af2080e71`](https://github.com/vllm-project/vllm/commit/8af2080e71) [#66046](https://github.com/vllm-project/vllm/pull/66046)
  [ROCm][CI] Skip the unlimited OCR tests until the ROCm CK OCR2 DASH updates land (#66046)
  _Files: `tests/models/multimodal/generation/test_unlimited_ocr.py`, `tests/v1/attention/test_unlimited_ocr2.py`_
- **2026-11-06** [`cf0e7c7e55`](https://github.com/vllm-project/vllm/commit/cf0e7c7e55) [#66044](https://github.com/vllm-project/vllm/pull/66044)
  [Doc][Bugfix] Fix strict docs build broken by unresolved autorefs (#66044)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py`, `vllm/models/minimax_m3/amd/mono/drafter/attention.py`, `vllm/models/minimax_m3/amd/mono/drafter/device.py`_
- **2026-11-06** [`51ae6f4da1`](https://github.com/vllm-project/vllm/commit/51ae6f4da1) [#65914](https://github.com/vllm-project/vllm/pull/65914)
  [Model Loader] One finish for every update path; drop refresh_derived_weights (#65914)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/distributed/weight_transfer/sparse_nccl_engine.py`, `vllm/model_executor/layers/fused_moe/runner/moe_runner.py` _+16 more__
- **2026-11-06** [`bda81524e4`](https://github.com/vllm-project/vllm/commit/bda81524e4) [#65971](https://github.com/vllm-project/vllm/pull/65971)
  [ROCm][Kernel] Follow-ups to the gfx942 MLA Triton verify kernel (#65971)
  _Files: `tests/kernels/attention/test_triton_decode_attention.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`, `vllm/v1/attention/ops/triton_decode_attention.py`_
- **2026-11-06** [`c2c7158a01`](https://github.com/vllm-project/vllm/commit/c2c7158a01) [#65937](https://github.com/vllm-project/vllm/pull/65937)
  [ROCm] Bump AITER to v0.1.28.post1 (#65937)
  _Files: `docker/Dockerfile.rocm_base`, `docker/Dockerfile.rocm_base_gfx1250`_
- **2026-11-06** [`e336407a3d`](https://github.com/vllm-project/vllm/commit/e336407a3d) [#65478](https://github.com/vllm-project/vllm/pull/65478)
  [ROCm][Perf][MiniMax-M3.1] Fuse the FFN-side MXFP8 activation quant into the post-attention norm and swiglu (#65478)
  _Files: `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/model_executor/layers/fused_allreduce_gemma_rms_norm.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/__init__.py` _+1 more__
- **2026-11-06** [`405aaa3d51`](https://github.com/vllm-project/vllm/commit/405aaa3d51) [#65530](https://github.com/vllm-project/vllm/pull/65530)
  [ROCm][Perf][MiniMax-M3.1] Retune the MXFP8 dot_scaled GEMM tiles for M=17-256 (#65530)
  _Files: `tests/kernels/quantization/test_rocm_mxfp8_linear.py`, `vllm/model_executor/kernels/linear/mxfp8/rocm_native.py`_
- **2026-11-06** [`b8a3e82dcd`](https://github.com/vllm-project/vllm/commit/b8a3e82dcd) [#65481](https://github.com/vllm-project/vllm/pull/65481)
  [ROCm][Perf][MiniMax-M3.1] Pick the NVFP4 sparse decode splits per XCD, not per CU (#65481)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/attention/test_minimax_m3_nvfp4_sparse_decode.py`, `vllm/models/minimax_m3/amd/ops/nvfp4_sparse_decode/host.py`_
- **2026-11-06** [`2eae5ee9be`](https://github.com/vllm-project/vllm/commit/2eae5ee9be) [#65722](https://github.com/vllm-project/vllm/pull/65722)
  [Bugfix][ROCm] Stop AITER FA from skipping 1-token prompts in prefill/extend (#65722)
  _Files: `tests/kernels/attention/test_rocm_aiter_fa.py`, `vllm/v1/attention/backends/rocm_aiter_fa.py`_
- **2026-11-06** [`e740badc2e`](https://github.com/vllm-project/vllm/commit/e740badc2e) [#64958](https://github.com/vllm-project/vllm/pull/64958)
  [ROCm][Kimi-K3] Support Mooncake consumers with specialized decode (#64958)
  _Files: `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py`_
- **2026-11-06** [`3eab4a4768`](https://github.com/vllm-project/vllm/commit/3eab4a4768) [#65988](https://github.com/vllm-project/vllm/pull/65988)
  [ROCm][CI] Let /ci rocm cache start its main build on AMD CI (#65988)
  _Files: `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-11-06** [`84e17e1ba5`](https://github.com/vllm-project/vllm/commit/84e17e1ba5) [#65386](https://github.com/vllm-project/vllm/pull/65386)
  Minimax m3.1 dspark drafter monokernel (#65386)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`, `tests/models/minimax_m3/test_dspark_drafter.py` _+10 more__
- **2026-11-06** [`1e89fd1125`](https://github.com/vllm-project/vllm/commit/1e89fd1125) [#65267](https://github.com/vllm-project/vllm/pull/65267)
  [Perf][ROCm][MiniMax-M3.1] Add opt-in parallel decode top-k (#65267)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`, `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`, `vllm/envs.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py` _+1 more__
- **2026-11-06** [`a7809d0cc5`](https://github.com/vllm-project/vllm/commit/a7809d0cc5) [#65968](https://github.com/vllm-project/vllm/pull/65968)
  [Docs][ROCm] Fix stale AMD recipe images for GLM-5 and GLM-5.1 (#65968)
  _Files: `recipes/models/zai-org/GLM-5.1.yaml`, `recipes/models/zai-org/GLM-5.yaml`_
- **2026-11-06** [`c59d545909`](https://github.com/vllm-project/vllm/commit/c59d545909) [#65599](https://github.com/vllm-project/vllm/pull/65599)
  [ROCm][Step5] Use one warp for CSA prefill sparse attention on CDNA3/CDNA4 (#65599)
  _Files: `vllm/models/step5/amd/ops/csa_paged.py`_
- **2026-11-06** [`6f74a43da1`](https://github.com/vllm-project/vllm/commit/6f74a43da1) [#65249](https://github.com/vllm-project/vllm/pull/65249)
  [ROCm][DSv4.1] Enable prefix-cache SWA replay on gfx942 (#65249)
  _Files: `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/attention.py`_
- **2026-11-05** [`96a6a37e86`](https://github.com/vllm-project/vllm/commit/96a6a37e86) [#62717](https://github.com/vllm-project/vllm/pull/62717)
  [ROCm][Build][2/5] Speed up ROCm build: split the topk softplus-sqrt instantiations per dtype (#62717)
  _Files: `CMakeLists.txt`, `csrc/moe/topk_softplus_sqrt.cu`, `csrc/moe/topk_softplus_sqrt_bf16_int32.cu`, `csrc/moe/topk_softplus_sqrt_bf16_int64.cu` _+8 more__
- **2026-11-05** [`6128b9072d`](https://github.com/vllm-project/vllm/commit/6128b9072d) [#60487](https://github.com/vllm-project/vllm/pull/60487)
  [Bugfix][ROCm] Count attention sinks once in AITER FA chunked-context extend (#60487)
  _Files: `tests/kernels/attention/test_rocm_aiter_fa.py`, `vllm/v1/attention/backends/rocm_aiter_fa.py`_
- **2026-11-05** [`5f2edcec96`](https://github.com/vllm-project/vllm/commit/5f2edcec96) [#63364](https://github.com/vllm-project/vllm/pull/63364)
  [ROCm][Build][4/5] Speed up ROCm build: instantiate the int4 skinny GEMM per output width (#63364)
  _Files: `CMakeLists.txt`, `csrc/rocm/skinny_gemms_int4.cuh`, `csrc/rocm/skinny_gemms_int4.h`, `csrc/rocm/skinny_gemms_int4_api.cu` _+5 more__
- **2026-11-05** [`c0b393a064`](https://github.com/vllm-project/vllm/commit/c0b393a064) [#65912](https://github.com/vllm-project/vllm/pull/65912)
  [ROCm][CI] Fix flaky streaming checks in test_translation_validation (#65912)
  _Files: `tests/entrypoints/speech_to_text/translation/test_translation_validation.py`_
- **2026-11-05** [`4d77f0b236`](https://github.com/vllm-project/vllm/commit/4d77f0b236) [#65276](https://github.com/vllm-project/vllm/pull/65276)
  [ROCm][CI] Cache a PR's ROCm base image for main with `/ci rocm cache` (#65276)
  _Files: `.buildkite/scripts/rocm/build.sh`, `.github/workflows/pre-commit.yml`, `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py` _+2 more__
- **2026-11-05** [`82aeedf8db`](https://github.com/vllm-project/vllm/commit/82aeedf8db) [#65908](https://github.com/vllm-project/vllm/pull/65908)
  [ROCm][CI] Fix flaky layer 0 bound in test_dsv4_mono_layers (#65908)
  _Files: `tests/models/test_dsv4_mono_layers.py`_
- **2026-11-05** [`c8168f5ab0`](https://github.com/vllm-project/vllm/commit/c8168f5ab0) [#65916](https://github.com/vllm-project/vllm/pull/65916)
  [ROCm][CI] Shard Spec Decode AL MTP with pytest-shard after the Gemma4 dataset split (#65916)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-11-05** [`831dd92674`](https://github.com/vllm-project/vllm/commit/831dd92674) [#65895](https://github.com/vllm-project/vllm/pull/65895)
  [CI] Use a repository-scoped Docker Hub secret for release publishing (#65895)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/cleanup-nightly-builds.sh`, `.buildkite/scripts/rocm/publish.sh`, `docs/contributing/ci/nightly_builds.md`_
- **2026-11-05** [`7940e5e06f`](https://github.com/vllm-project/vllm/commit/7940e5e06f) [#65889](https://github.com/vllm-project/vllm/pull/65889)
  [CI] Limit ROCm Docker Hub login to image publishing (#65889)
  _Files: `.buildkite/release-pipeline.yaml`_
- **2026-11-05** [`1efcaa98ff`](https://github.com/vllm-project/vllm/commit/1efcaa98ff) [#63956](https://github.com/vllm-project/vllm/pull/63956)
  [Perf][DSA] Token-sharded sparse-MLA prefill under TP; remove indexer row sharding (#63956)
  _Files: `.buildkite/test_areas/distributed.yaml`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_index_remap.py`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` _+17 more__
- **2026-11-05** [`732e49d442`](https://github.com/vllm-project/vllm/commit/732e49d442) [#63231](https://github.com/vllm-project/vllm/pull/63231)
  [Core] Change default --block-size from 16 to 64 (#63231)
  _Files: `tests/config/test_config_utils.py`, `tests/model_executor/test_flashinfer_autotune_warmup.py`, `tests/v1/kv_connector/unit/test_example_connector.py`, `tests/v1/kv_connector/unit/test_offloading_connector.py` _+2 more__
- **2026-11-05** [`7187c01de5`](https://github.com/vllm-project/vllm/commit/7187c01de5) [#59124](https://github.com/vllm-project/vllm/pull/59124)
  [ROCm][Perf][MLA] Add opt-in FlyDSL FP8 prefill attention for AITER MLA (#59124)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_flydsl_fp8_prefill.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_mla_prefill_selector.py`, `vllm/config/attention.py` _+4 more__
- **2026-11-05** [`ae96354d8b`](https://github.com/vllm-project/vllm/commit/ae96354d8b) [#63730](https://github.com/vllm-project/vllm/pull/63730)
  [ROCm][Perf] Kimi-K3 prefill GEMMs on AITER tuned kernels (#63730)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `tests/model_executor/test_rocm_aiter_gemm_warmup.py`, `vllm/config/kernel.py`, `vllm/model_executor/warmup/kernel_warmup.py` _+1 more__
- **2026-11-05** [`c2bc949186`](https://github.com/vllm-project/vllm/commit/c2bc949186) [#65812](https://github.com/vllm-project/vllm/pull/65812)
  [Bugfix] Honor checkpoint FP8 KV scales in Qwen4Exp QSA (#65812)
  _Files: `vllm/models/qwen4_exp/amd/qsa.py`, `vllm/models/qwen4_exp/nvidia/qsa.py`_
- **2026-11-05** [`db914cad5b`](https://github.com/vllm-project/vllm/commit/db914cad5b) [#63117](https://github.com/vllm-project/vllm/pull/63117)
  [Bugfix][ROCm] Take the AITER MLA KV cache dtype from the group's spec (#63117)
  _Files: `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-11-05** [`e5d0ef3527`](https://github.com/vllm-project/vllm/commit/e5d0ef3527) [#64886](https://github.com/vllm-project/vllm/pull/64886)
  [Bugfix][ROCm][Kimi-K3] Refresh derived weight copies after in-place weight writes (#64886)
  _Files: `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/distributed/weight_transfer/sparse_nccl_engine.py`, `vllm/model_executor/model_loader/reload/inplace.py`, `vllm/model_executor/model_loader/weight_utils.py` _+2 more__
- **2026-11-05** [`49c1a73a2e`](https://github.com/vllm-project/vllm/commit/49c1a73a2e) [#63891](https://github.com/vllm-project/vllm/pull/63891)
  [ROCm][Perf][DSv4.1] Run DSpark's fused Markov sampling on gfx950 with --monokernel (#63891)
  _Files: `tests/kernels/models/amd/test_dsv41_gfx942_fused_markov.py`, `tests/models/test_dsv41_mono_decode.py`, `vllm/models/deepseek_v41/amd/ops/__init__.py`, `vllm/models/deepseek_v41/amd/ops/fused_markov.py` _+1 more__
- **2026-11-05** [`1929f16945`](https://github.com/vllm-project/vllm/commit/1929f16945) [#63888](https://github.com/vllm-project/vllm/pull/63888)
  [ROCm][Perf][DSv4.1] Skip the top-k -1 fill on the rows vLLM's decode top-k writes (#63888)
  _Files: `tests/kernels/attention/test_rocm_paged_mxfp4_indexer.py`, `tests/v1/attention/test_rocm_paged_mxfp4_indexer_plan.py`, `vllm/v1/attention/ops/rocm_paged_mxfp4_indexer.py`_
- **2026-11-05** [`aa81e6784e`](https://github.com/vllm-project/vllm/commit/aa81e6784e) [#62725](https://github.com/vllm-project/vllm/pull/62725)
  [ROCm][Bugfix] Serve gfx942 MLA verify past 4 tokens with a Triton kernel (#62725)
  _Files: `tests/kernels/attention/test_triton_decode_attention.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py` _+1 more__
- **2026-11-05** [`c6ae8d68f2`](https://github.com/vllm-project/vllm/commit/c6ae8d68f2) [#63027](https://github.com/vllm-project/vllm/pull/63027)
  [ROCm][Perf][DSv4.1] Mono: tuned K1/K2 for the TP2 compress-ratio-2 layers on MI355X (#63027)
  _Files: `tests/models/test_dsv41_mono_numerics.py`, `vllm/models/deepseek_v41/amd/mono/README.md`, `vllm/models/deepseek_v41/amd/mono/attention/back.py`, `vllm/models/deepseek_v41/amd/mono/attention/front.py` _+8 more__
- **2026-11-04** [`cb2cf10f71`](https://github.com/vllm-project/vllm/commit/cb2cf10f71) [#65585](https://github.com/vllm-project/vllm/pull/65585)
  [CI] Enroll the MI300 Batch Invariance (Distributed) mirror in automatic sharding (#65585)
  _Files: `.buildkite/test_areas/misc.yaml`_
- **2026-11-04** [`c5d1d77d2b`](https://github.com/vllm-project/vllm/commit/c5d1d77d2b) [#62057](https://github.com/vllm-project/vllm/pull/62057)
  [ROCm][Model] Add Beam 1.0 support on ROCm  (#62057)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `recipes/models/reflection/Beam-1.0-501B-A23B.yaml`, `tests/models/test_beam_construction.py`, `tests/models/test_beam_numerics.py` _+13 more__
- **2026-11-04** [`beaa72618e`](https://github.com/vllm-project/vllm/commit/beaa72618e) [#60919](https://github.com/vllm-project/vllm/pull/60919)
  [JIT][ROCm] Fully warmup GLM-5.3-Flash (#60919)
  _Files: `tests/model_executor/test_jit_warmup_triton_launcher.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/warmup/jit_warmup_triton_helper.py`, `vllm/models/glm5next/amd/ops/kpool_compress.py` _+3 more__
- **2026-11-04** [`586d2f7324`](https://github.com/vllm-project/vllm/commit/586d2f7324) [#63367](https://github.com/vllm-project/vllm/pull/63367)
  [ROCm][DSv4.1] Shard the Engram gate so TP ranks gather only the value slice (#63367)
  _Files: `tests/kernels/test_engram.py`, `vllm/models/deepseek_v41/amd/engram.py`, `vllm/models/deepseek_v41/amd/model.py`, `vllm/models/deepseek_v41/common/engram.py`_
- **2026-11-04** [`9b34fec744`](https://github.com/vllm-project/vllm/commit/9b34fec744) [#61770](https://github.com/vllm-project/vllm/pull/61770)
  [Bugfix][ROCm][Qwen4Exp] Remap Quark layer names for the MTP draft model (#61770)
  _Files: `tests/models/qwen4_exp/test_config.py`, `vllm/models/qwen4_exp/amd/mtp.py`, `vllm/models/qwen4_exp/nvidia/mtp.py`_
- **2026-11-04** [`7871c62b61`](https://github.com/vllm-project/vllm/commit/7871c62b61) [#59802](https://github.com/vllm-project/vllm/pull/59802)
  [ROCm][DSv4.1][Perf] Overlap the mHC gate projection with attention and FFN (#59802)
  _Files: `tests/kernels/mhc/test_mhc_kernels.py`, `vllm/model_executor/kernels/mhc/triton.py`, `vllm/models/deepseek_v41/amd/mhc.py`, `vllm/models/deepseek_v41/amd/model.py` _+1 more__
- **2026-11-04** [`67e6ea21a7`](https://github.com/vllm-project/vllm/commit/67e6ea21a7) [#65425](https://github.com/vllm-project/vllm/pull/65425)
  [ROCm][CI] Restore the Torch Stable ABI Audit mirror with a locked audit tool (#65425)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/torch_abi.yaml`, `requirements/test/rocm.in`, `requirements/test/rocm.txt`_
- **2026-11-04** [`bb6f5ca3f4`](https://github.com/vllm-project/vllm/commit/bb6f5ca3f4) [#65641](https://github.com/vllm-project/vllm/pull/65641)
  [ROCm][CI] Skip the GPU coredump in MonoKernel fault-injection tests (#65641)
  _Files: `tests/models/minimax_m3/amd_specialized_decode/test_model.py`_
- **2026-11-04** [`ca8bd4c055`](https://github.com/vllm-project/vllm/commit/ca8bd4c055) [#65432](https://github.com/vllm-project/vllm/pull/65432)
  [ROCm][Perf][MiniMax-M3.1] Score DSpark 7 decode locally below 3 requests instead of via indexer CP (#65432)
  _Files: `tests/kernels/attention/test_minimax_m3_nvfp4_index.py`, `vllm/models/minimax_m3/amd/indexer_nvfp4.py`_
- **2026-11-04** [`dd4e40142a`](https://github.com/vllm-project/vllm/commit/dd4e40142a) [#64836](https://github.com/vllm-project/vllm/pull/64836)
  [ROCm][Step5] Exercise the real CSA decode and engine paths in tests (#64836)
  _Files: `tests/models/step5/test_amd_csa_paged.py`, `tests/models/step5/test_amd_fp8_kv_init.py`, `tests/models/step5/test_amd_model.py`_
- **2026-11-04** [`e5d9bad98e`](https://github.com/vllm-project/vllm/commit/e5d9bad98e) [#64763](https://github.com/vllm-project/vllm/pull/64763)
  [ROCm][HY4] Use breakable graphs without torch.compile (#64763)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `docs/models/hy4.md`, `docs/models/supported_models.md`, `tests/models/test_hyv4_rocm.py` _+2 more__
- **2026-11-04** [`c0c8373c23`](https://github.com/vllm-project/vllm/commit/c0c8373c23) [#65087](https://github.com/vllm-project/vllm/pull/65087)
  [ROCm][Perf][MiniMax-M3.1] Four-wave decode top-k for the NVFP4 indexer (#65087)
  _Files: `tests/kernels/attention/test_minimax_m3_index_topk_decode.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/host.py`, `vllm/models/minimax_m3/amd/ops/index_topk_decode/prefill_kernel.py`_
- **2026-11-03** [`8426f16135`](https://github.com/vllm-project/vllm/commit/8426f16135) [#63419](https://github.com/vllm-project/vllm/pull/63419)
  [ROCm] Migrate Aiter sigmoid to topk_gating (#63419)
  _Files: `tests/model_executor/test_enabled_custom_ops.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_router.py`_
- **2026-11-03** [`81f1baa731`](https://github.com/vllm-project/vllm/commit/81f1baa731) [#63949](https://github.com/vllm-project/vllm/pull/63949)
  [ROCm][CI] Untrusted base builds wait for main's images instead of rebuilding them (#63949)
  _Files: `.buildkite/scripts/rocm/build.sh`, `tests/tools/test_rocm_build.py`_
- **2026-11-03** [`472e23f7da`](https://github.com/vllm-project/vllm/commit/472e23f7da) [#64132](https://github.com/vllm-project/vllm/pull/64132)
  [ROCm][CI] Bake the fast-exit plugin into the test image and fix the ray-compat pin strip (#64132)
  _Files: `.buildkite/scripts/check-ray-compatibility.sh`, `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `docker/Dockerfile.rocm`_
- **2026-11-03** [`81a2879403`](https://github.com/vllm-project/vllm/commit/81a2879403) [#62565](https://github.com/vllm-project/vllm/pull/62565)
  [ROCm][Perf] Fix Kimi-K2.6 int4 MoE prefill regression on Triton 3.8 (gfx950 tuned config) (#62565)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=384,N=256,device_name=AMD_Instinct_MI350X,dtype=int4_w4a16.json`, `vllm/model_executor/layers/fused_moe/configs/E=384,N=256,device_name=AMD_Instinct_MI350_OAM,dtype=int4_w4a16.json`, `vllm/model_executor/layers/fused_moe/configs/E=384,N=256,device_name=AMD_Instinct_MI355X,dtype=int4_w4a16.json`, `vllm/model_executor/layers/fused_moe/configs/E=384,N=256,device_name=AMD_Instinct_MI355_OAM,dtype=int4_w4a16.json`_
- **2026-11-03** [`275816d060`](https://github.com/vllm-project/vllm/commit/275816d060) [#62750](https://github.com/vllm-project/vllm/pull/62750)
  [Quantization] Block Hadamard input rotation for linear layers: online `mxfp4_hadamard32` and Quark online-rotation checkpoints (#62750)
  _Files: `docs/features/quantization/online.md`, `tests/quantization/test_input_hadamard.py`, `tests/quantization/test_quantization_config_args.py`, `tests/quantization/test_quark.py` _+8 more__
- **2026-11-03** [`32a4dbfdaf`](https://github.com/vllm-project/vllm/commit/32a4dbfdaf) [#64241](https://github.com/vllm-project/vllm/pull/64241)
  [CI] Pin existing dependency hashes and enforce immutable references (#64241)
  _Files: `.buildkite/test_areas/misc.yaml`, `.github/workflows/recipes.yml`, `.pre-commit-config.yaml`, `.readthedocs.yaml` _+15 more__
- **2026-11-03** [`4d2fa5637c`](https://github.com/vllm-project/vllm/commit/4d2fa5637c) [#60418](https://github.com/vllm-project/vllm/pull/60418)
  [ROCm] [RDNA] [Perf] Add tuned configs for TRITON_ATTN kernel and swap places of TRITON_ATTN and ROCM_ATTN in priority list (#60418)
  _Files: `tests/v1/attention/test_rocm_attention_backends_selection.py`, `vllm/platforms/rocm.py`, `vllm/v1/attention/ops/triton_unified_attention.py`_
- **2026-11-03** [`8d3db204b6`](https://github.com/vllm-project/vllm/commit/8d3db204b6) [#64317](https://github.com/vllm-project/vllm/pull/64317)
  [ROCm][Perf] Keep 32-bit buffer addressing for per-token-head KV and AITER cross-attention fallback (#64317)
  _Files: `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`, `vllm/v1/attention/backends/triton_attn.py`_
- **2026-11-03** [`ac16e0caa4`](https://github.com/vllm-project/vllm/commit/ac16e0caa4) [#65322](https://github.com/vllm-project/vllm/pull/65322)
  [ROCm][Perf] W4A16: retune int4 skinny GEMM decode tuples for gfx115x (#65322)
  _Files: `csrc/rocm/skinny_gemms_int4.cu`, `tests/kernels/quantization/test_rdna_hybrid_w4a16.py`_
- **2026-11-03** [`c1d8fade8d`](https://github.com/vllm-project/vllm/commit/c1d8fade8d) [#56450](https://github.com/vllm-project/vllm/pull/56450)
  [ROCm][Perf] Encoder prefill attention on gfx1151: split-D head dims, alignment hint, launch config (#56450)
  _Files: `benchmarks/kernels/benchmark_vit_prefill_attn.py`, `tests/kernels/attention/test_triton_prefill_attention.py`, `vllm/v1/attention/ops/triton_prefill_attention.py`_
- **2026-11-03** [`a12e122206`](https://github.com/vllm-project/vllm/commit/a12e122206) [#56307](https://github.com/vllm-project/vllm/pull/56307)
  [ROCm][Kernel] New "hip" GDN backend for gfx1151 (#56307)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_gdn_chunk.py`, `csrc/rocm/ops.h`, `csrc/rocm/rdna35_gdn_chunked.cu` _+9 more__
- **2026-11-03** [`bb86df34d7`](https://github.com/vllm-project/vllm/commit/bb86df34d7) [#65418](https://github.com/vllm-project/vllm/pull/65418)
  [Bugfix][ROCm] Raise the extensible KV cache margin floor to 3 GiB (#65418)
  _Files: `vllm/v1/worker/extensible_kv_cache.py`_
- **2026-11-03** [`7c284bf150`](https://github.com/vllm-project/vllm/commit/7c284bf150) [#63835](https://github.com/vllm-project/vllm/pull/63835)
  [ROCm][Perf][Bugfix] wvSplitK: launch tiles of their own for gfx1151 and gfx1150; fix bigType for A_CHUNK 16 (#63835)
  _Files: `csrc/rocm/skinny_gemms.cu`, `tests/kernels/quantization/test_rocm_skinny_gemms.py`_
- **2026-11-03** [`0eeae6a473`](https://github.com/vllm-project/vllm/commit/0eeae6a473) [#65030](https://github.com/vllm-project/vllm/pull/65030)
  [Perf][Model] DeepSeek V4/V4.1 Vision: encode a call's images in packed passes (#65030)
  _Files: `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v4/common/vl_model.py`, `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/nvidia/vl_model.py`_
- **2026-11-03** [`22d05b87bb`](https://github.com/vllm-project/vllm/commit/22d05b87bb) [#65296](https://github.com/vllm-project/vllm/pull/65296)
  [Model Loader] DeepSeek-V4 ROCm: keep the preshuffle scales out of the module's parameters (#65296)
  _Files: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`_
- **2026-11-03** [`a8718969d2`](https://github.com/vllm-project/vllm/commit/a8718969d2) [#64330](https://github.com/vllm-project/vllm/pull/64330)
  [Bugfix][ROCm][MoRIIO] Wait for MoRIIO WRITE mode completions in short chunks (#64330)
  _Files: `tests/v1/kv_connector/unit/test_moriio_tp_ack.py`, `tests/v1/kv_connector/unit/test_moriio_transfer_completion.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`_
- **2026-11-03** [`67791dd94d`](https://github.com/vllm-project/vllm/commit/67791dd94d) [#62802](https://github.com/vllm-project/vllm/pull/62802)
  [EPD] Support DeepSeek-V4.1 image metadata-only inputs (#62802)
  _Files: `tests/models/multimodal/processing/test_deepseek_v4_vl.py`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/models/deepseek_v41/amd/vl_model.py`, `vllm/models/deepseek_v41/common/mm_preprocess.py` _+3 more__
- **2026-11-03** [`7ff48230e7`](https://github.com/vllm-project/vllm/commit/7ff48230e7) [#63204](https://github.com/vllm-project/vllm/pull/63204)
  [Refactor][ROCm][MoE] Let each AiterExperts subclass own its AITER call args (#63204)
  _Files: `tests/kernels/moe/test_modular_kernel_combinations.py`, `tests/kernels/moe/test_mori_moe.py`, `tests/kernels/moe/test_muse_spark_rocm_bf16_moe.py`, `tests/kernels/moe/test_rocm_aiter_moe.py` _+4 more__
- **2026-11-03** [`75be138428`](https://github.com/vllm-project/vllm/commit/75be138428) [#64096](https://github.com/vllm-project/vllm/pull/64096)
  [KV Connector][Spec Decode] Support lookahead block hashes in KV connectors (#64096)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`, `tests/models/test_muse_spark_rocm_mono.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/e2e/spec_decode/mtp/qwen3_5/test_mtp.py` _+34 more__
- **2026-11-03** [`8a702b18a1`](https://github.com/vllm-project/vllm/commit/8a702b18a1) [#63076](https://github.com/vllm-project/vllm/pull/63076)
  [ROCm][Perf] Triton sigmoid+bias top-k when MoE grouping eliminates nothing (#63076)
  _Files: `tests/kernels/moe/test_rocm_aiter_topk.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/layers/fused_moe/router/rocm_sigmoid_bias_flat_topk.py`_
- **2026-11-03** [`254a2a3390`](https://github.com/vllm-project/vllm/commit/254a2a3390) [#61435](https://github.com/vllm-project/vllm/pull/61435)
  [ROCm][Perf][Kimi-K3] Specialized decode on MI355X: K1/K2 + MLA M1a/M1b (FlyDSL, TP8, DCP1/DCP8) (#61435)
  _Files: `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/decode.py` _+3 more__
- **2026-11-02** [`5da6f2e274`](https://github.com/vllm-project/vllm/commit/5da6f2e274) [#64174](https://github.com/vllm-project/vllm/pull/64174)
  [CI] Enroll four Nightly steps and three AMD mirrors in automatic sharding (#64174)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-11-02** [`f5044745aa`](https://github.com/vllm-project/vllm/commit/f5044745aa) [#64839](https://github.com/vllm-project/vllm/pull/64839)
  [ROCm][CI] Add a build.sh prebuild mode for maintainer-approved stack builds (#64839)
  _Files: `.buildkite/scripts/rocm/build.sh`_
- **2026-11-02** [`af751a9edc`](https://github.com/vllm-project/vllm/commit/af751a9edc) [#64657](https://github.com/vllm-project/vllm/pull/64657)
  [Test][UMBP] Cover TP=2 restore through per-rank MORI pools (#64657)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `tests/v1/kv_connector/umbp_integration/test_mori_token_e2e.py`_
- **2026-11-02** [`27072f9cd3`](https://github.com/vllm-project/vllm/commit/27072f9cd3) [#63426](https://github.com/vllm-project/vllm/pull/63426)
  [ROCm][CI] Print the native backtrace of a fault in AMD CI pytest runs (#63426)
  _Files: `.buildkite/ci_config_rocm.yaml`, `.buildkite/scripts/hardware_ci/amd_ci_fast_exit.py`, `.buildkite/scripts/hardware_ci/amd_ci_fault_trap.c`, `.buildkite/test-amd.yaml` _+3 more__
- **2026-11-02** [`bf1dbed3ea`](https://github.com/vllm-project/vllm/commit/bf1dbed3ea) [#64833](https://github.com/vllm-project/vllm/pull/64833)
  [ROCm][Step5] Require CDNA3 or newer for the sparse attention layers (#64833)
  _Files: `docs/models/supported_models.md`, `vllm/models/step5/amd/model.py`_
- **2026-11-02** [`26d198bd56`](https://github.com/vllm-project/vllm/commit/26d198bd56) [#64692](https://github.com/vllm-project/vllm/pull/64692)
  [Model Loader] Refill weight-derived tensors in place on every post-load rerun (#64692)
  _Files: `.buildkite/test_areas/quantization.yaml`, `.buildkite/test_areas/spec_decode.yaml`, `tests/kernels/moe/test_b12x.py`, `tests/kernels/moe/test_muse_spark_trtllm_moe.py` _+70 more__
- **2026-11-02** [`901f26dfcd`](https://github.com/vllm-project/vllm/commit/901f26dfcd) [#62270](https://github.com/vllm-project/vllm/pull/62270)
  [ROCm][Perf][MiniMax-M3] Enable the fp8 indexer cache on gfx942 (#62270)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `csrc/fused_minimax_m3_qknorm_rope_kv_insert_kernel.cu`, `tests/kernels/attention/test_minimax_m3.py` _+5 more__
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

## Attention  (77 commits)

- **2026-11-09** [`e19e540a9e`](https://github.com/vllm-project/vllm/commit/e19e540a9e) [#66289](https://github.com/vllm-project/vllm/pull/66289)
  [Bugfix][Qwen3.5] Replace FlashInfer GemmaRMSNorm JIT with Triton for arch<sm80 (#66289)
  _Files: `tests/models/qwen3_5/test_gemma_add_rms_norm_quant.py`, `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/models/qwen3_5/nvidia/model.py`, `vllm/models/qwen3_5/nvidia/ops/fused_norm_quant.py` _+1 more__
- **2026-11-09** [`8d5589b2a5`](https://github.com/vllm-project/vllm/commit/8d5589b2a5) [#54737](https://github.com/vllm-project/vllm/pull/54737)
  [Doc] Fix stale attention_kernels.cu reference in paged_attention.md (#54737)
  _Files: `docs/design/paged_attention.md`_
- **2026-11-09** [`21ef2e5b0a`](https://github.com/vllm-project/vllm/commit/21ef2e5b0a) [#51951](https://github.com/vllm-project/vllm/pull/51951)
  [Bugfix][Model] Fix Inkling NVIDIA sconv cache block-size mismatch (#51951)
  _Files: `tests/models/inkling/test_qkvr_prep.py`, `vllm/models/inkling/nvidia/attention.py`, `vllm/models/inkling/nvidia/model.py`, `vllm/models/inkling/nvidia/sconv_swa_attn.py` _+1 more__
- **2026-11-08** [`f905e70070`](https://github.com/vllm-project/vllm/commit/f905e70070) [#66263](https://github.com/vllm-project/vllm/pull/66263)
  [Bugfix] Do not initialize CUDA when importing vendored FLA (#66263)
  _Files: `vllm/third_party/flash_linear_attention/ops/utils.py`_
- **2026-11-08** [`d1879210a4`](https://github.com/vllm-project/vllm/commit/d1879210a4) [#65627](https://github.com/vllm-project/vllm/pull/65627)
  [Bugfix][Attention] Keep FA sliding window active under batch invariance (#65627)
  _Files: `tests/v1/determinism/test_batch_invariance.py`, `vllm/v1/attention/backends/flash_attn.py`_
- **2026-11-07** [`35b4c82ee4`](https://github.com/vllm-project/vllm/commit/35b4c82ee4) [#65275](https://github.com/vllm-project/vllm/pull/65275)
  [Bugfix][MRV2] Use promised max_query_len for encoder-only FULL CUDA graphs (#65275)
  _Files: `.buildkite/test_areas/cuda.yaml`, `tests/v1/cudagraph/test_encoder_only_full_cudagraph.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/worker/gpu/model_states/encoder_only.py`_
- **2026-11-07** [`876179bd8c`](https://github.com/vllm-project/vllm/commit/876179bd8c) [#66228](https://github.com/vllm-project/vllm/pull/66228)
  [Build][MiniMax-M3] Bump fmha_sm100 to 51f4f5c (#66228)
  _Files: `cmake/external_projects/fmha_sm100.cmake`_
- **2026-11-06** [`f8b116409c`](https://github.com/vllm-project/vllm/commit/f8b116409c) [#66010](https://github.com/vllm-project/vllm/pull/66010)
  [Sleep Mode] Level 2 discards only parameters (#66010)
  _Files: `docs/features/sleep_mode.md`, `tests/basic_correctness/memory/cumem/test_cumem.py`, `tests/basic_correctness/memory/sleep_mode/test_sleep_mode.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py` _+14 more__
- **2026-11-06** [`09109f9622`](https://github.com/vllm-project/vllm/commit/09109f9622) [#63795](https://github.com/vllm-project/vllm/pull/63795)
  [Spec Decode] DSpark: sliding-window MLA draft layers (#63795)
  _Files: `tests/kernels/attention/test_triton_decode_attention.py`, `tests/kernels/attention/test_triton_mla_causal_verify_flatten.py`, `tests/v1/core/test_kv_cache_planning.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+5 more__
- **2026-11-06** [`a7a5d0919b`](https://github.com/vllm-project/vllm/commit/a7a5d0919b) [#65652](https://github.com/vllm-project/vllm/pull/65652)
  [torch.compile] Replace config `compute_hash` with `compile_factors` (#65652)
  _Files: `docs/design/torch_compile.md`, `rust/src/engine-core-client/src/protocol/handshake.rs`, `tests/compile/fullgraph/test_toy_llama.py`, `tests/compile/test_compiler_interface.py` _+49 more__
- **2026-11-06** [`9dbb5e37d5`](https://github.com/vllm-project/vllm/commit/9dbb5e37d5) [#64986](https://github.com/vllm-project/vllm/pull/64986)
  [Bugfix][Attention] Fix KV-sharing fast prefill hang from unsynchronized host offsets (#64986)
  _Files: `tests/v1/attention/test_kv_sharing_fast_prefill_metadata.py`, `vllm/v1/attention/backends/utils.py`_
- **2026-11-06** [`4bfcd5d65f`](https://github.com/vllm-project/vllm/commit/4bfcd5d65f) [#65778](https://github.com/vllm-project/vllm/pull/65778)
  [Bugfix][Multimodal] Fix FlashInfer ViT attention for GLM-4.1V, GLM-OCR and GLM-5.3-Flash (#65778)
  _Files: `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/glm_ocr.py`, `vllm/models/glm5next/common/multimodal.py`_
- **2026-11-06** [`a8e96e18b2`](https://github.com/vllm-project/vllm/commit/a8e96e18b2) [#65554](https://github.com/vllm-project/vllm/pull/65554)
  [Bugfix] Fix startup illegal memory access from unaligned extensible KV cache segments (#65554)
  _Files: `tests/kernels/attention/test_flashmla_sparse.py`, `tests/v1/worker/test_extensible_kv_cache.py`, `tests/v1/worker/test_gpu_worker.py`, `vllm/v1/worker/extensible_kv_cache.py` _+1 more__
- **2026-11-05** [`86fdabec0c`](https://github.com/vllm-project/vllm/commit/86fdabec0c) [#65986](https://github.com/vllm-project/vllm/pull/65986)
  [Recipes] Update DeepSeek-V4.1-Flash AgentX presets for GB200 and B200 (#65986)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-11-05** [`644f052052`](https://github.com/vllm-project/vllm/commit/644f052052) [#65883](https://github.com/vllm-project/vllm/pull/65883)
  [Perf][MiniMax-M3] Don't sync when building sparse-attention prefill metadata (#65883)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/sparse_attention.py`_
- **2026-11-05** [`073049553c`](https://github.com/vllm-project/vllm/commit/073049553c) [#65518](https://github.com/vllm-project/vllm/pull/65518)
  [Build] Bump vllm-flash-attn to compress fatbins with --compress-mode=size (#65518)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`_
- **2026-11-05** [`d60c4404e2`](https://github.com/vllm-project/vllm/commit/d60c4404e2) [#60372](https://github.com/vllm-project/vllm/pull/60372)
  [Kernel] Integrate FA4 SM90 FP8 MMA for Gemma-4 full attention (#60372)
  _Files: `.buildkite/lm-eval-harness/configs/gemma-4-31B-it-FP8-dynamic.yaml`, `.buildkite/lm-eval-harness/configs/models-large-hopper.txt`, `.buildkite/lm-eval-harness/test_lm_eval_correctness.py`, `cmake/external_projects/vllm_flash_attn.cmake` _+5 more__
- **2026-11-05** [`03bd3c6848`](https://github.com/vllm-project/vllm/commit/03bd3c6848) [#65745](https://github.com/vllm-project/vllm/pull/65745)
  [Model] Add Ricursive Ripple-65B support (#65745)
  _Files: `docs/features/reasoning_outputs.md`, `docs/features/tool_calling.md`, `docs/models/supported_models.md`, `recipes/models/ricursiveAI/Ripple-65B-Preview.yaml` _+23 more__
- **2026-11-05** [`b02e2287b2`](https://github.com/vllm-project/vllm/commit/b02e2287b2) [#64095](https://github.com/vllm-project/vllm/pull/64095)
  [Core][MLA] Cross-layer KV cache sharing for attention layers (#64095)
  _Files: `tests/v1/worker/test_attn_utils.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/attention_layer_base.py`, `vllm/v1/attention/backends/mla/cpu_mla.py` _+1 more__
- **2026-11-05** [`6a6f804796`](https://github.com/vllm-project/vllm/commit/6a6f804796) [#64856](https://github.com/vllm-project/vllm/pull/64856)
  [Bugfix][MiniMax-M3.1] Reserve MSA Q8KV4 prefill workspace (#64856)
  _Files: `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/sparse_attention_msa.py`_
- **2026-11-05** [`25c148c602`](https://github.com/vllm-project/vllm/commit/25c148c602) [#65834](https://github.com/vllm-project/vllm/pull/65834)
  [Docs] Fix missing MLA verify parameter types in API docs (#65834)
  _Files: `vllm/v1/attention/ops/triton_decode_attention.py`_
- **2026-11-05** [`7dca18e206`](https://github.com/vllm-project/vllm/commit/7dca18e206) [#64510](https://github.com/vllm-project/vllm/pull/64510)
  [Perf] Enable native small-head kernels in SM90 sparse FlashMLA (#64510)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-11-05** [`edc7181bdb`](https://github.com/vllm-project/vllm/commit/edc7181bdb) [#64880](https://github.com/vllm-project/vllm/pull/64880)
  [Bugfix][LoRA] Apply DeepSeek-V4 compressor and wo_a adapters (#64880)
  _Files: `tests/lora/test_layers.py`, `vllm/lora/layers/custom_layer.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/grouped_wo_a.py` _+6 more__
- **2026-11-05** [`1a983e2eb2`](https://github.com/vllm-project/vllm/commit/1a983e2eb2) [#65817](https://github.com/vllm-project/vllm/pull/65817)
  [Recipe] Add ERNIE-5.5-Flash recipe (#65817)
  _Files: `recipes/models/baidu/ERNIE-5.5-Flash.yaml`_
- **2026-11-05** [`4ab4404e24`](https://github.com/vllm-project/vllm/commit/4ab4404e24) [#65763](https://github.com/vllm-project/vllm/pull/65763)
  [CI][Kernels] Make the MiniMax-M3 decode top-k test deterministic (#65763)
  _Files: `tests/kernels/attention/test_minimax_m3.py`_
- **2026-11-05** [`7ecc83a987`](https://github.com/vllm-project/vllm/commit/7ecc83a987) [#60762](https://github.com/vllm-project/vllm/pull/60762)
  [Bugfix][DSv4.1] Declare 64-token kernel blocks for SM120 sparse backends (#60762)
  _Files: `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-11-05** [`29e58d1bbd`](https://github.com/vllm-project/vllm/commit/29e58d1bbd) [#65598](https://github.com/vllm-project/vllm/pull/65598)
  [Bugfix][Attention] Keep FlashInfer TRTLLM prefill query offsets in a persistent buffer (#65598)
  _Files: `tests/v1/attention/test_flashinfer_trtllm_prefill_cudagraph.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-11-04** [`d42c8a8d8f`](https://github.com/vllm-project/vllm/commit/d42c8a8d8f) [#64479](https://github.com/vllm-project/vllm/pull/64479)
  [XPU][Perf] Reuse GDN metadata across KV cache groups on XPU (#64479)
  _Files: `vllm/v1/attention/backends/gdn_attn.py`, `vllm/v1/worker/mamba_utils.py`_
- **2026-11-04** [`b4acf7bb21`](https://github.com/vllm-project/vllm/commit/b4acf7bb21) [#65553](https://github.com/vllm-project/vllm/pull/65553)
  [GLM 5.3 Perf] Enable fp8 kv cache for glm 5.3 flash draft model dspark, 960MB GPU memory saved each rank (#65553)
  _Files: `vllm/model_executor/models/config.py`_
- **2026-11-04** [`750cad1973`](https://github.com/vllm-project/vllm/commit/750cad1973) [#55688](https://github.com/vllm-project/vllm/pull/55688)
  [Mamba] Unify FI ReplaySSM STP/MTP/Prefix Caching Lifecycle (#55688)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `docs/features/automatic_prefix_caching.md`, `tests/evals/gsm8k/configs/Nemotron-3-Super-120B-A12B-NVFP4-ReplaySSM-align.yaml` _+40 more__
- **2026-11-04** [`f9b40a5d4c`](https://github.com/vllm-project/vllm/commit/f9b40a5d4c) [#65522](https://github.com/vllm-project/vllm/pull/65522)
  [Bugfix] Keep the HiSparse FlashInfer all-reduce backend on lazy workspace creation (#65522)
  _Files: `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-11-04** [`e826fa88b0`](https://github.com/vllm-project/vllm/commit/e826fa88b0) [#64129](https://github.com/vllm-project/vllm/pull/64129)
  [Perf][DCP] Sparse indexer: key only significant bits in the DCP top-k merge (#64129)
  _Files: `tests/v1/attention/test_indexer_dcp_localize.py`, `vllm/model_executor/kernels/attention/dsa/dcp_indexer_cutedsl.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/models/glm5next/nvidia/sparse_indexer.py`_
- **2026-11-04** [`da0b6ac221`](https://github.com/vllm-project/vllm/commit/da0b6ac221) [#64016](https://github.com/vllm-project/vllm/pull/64016)
  [Model] Add Unlimited-OCR-2 DASH attention support (#64016)
  _Files: `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/models_multimodal.yaml`, `docs/models/supported_models.md`, `examples/generate/multimodal/vision_language_multi_image_offline.py` _+20 more__
- **2026-11-04** [`66df311e82`](https://github.com/vllm-project/vllm/commit/66df311e82) [#65417](https://github.com/vllm-project/vllm/pull/65417)
  [MyPy][8b/N] Fix and enforce remaining tests/models subdirectories (#65417)
  _Files: `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_layers.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_sparse_mla_cute.py`, `tests/models/deepseek_v41/nvidia/test_swapab_decode.py` _+1 more__
- **2026-11-04** [`59519ec0ee`](https://github.com/vllm-project/vllm/commit/59519ec0ee) [#60252](https://github.com/vllm-project/vllm/pull/60252)
  [Bugfix][Spec Decode] Keep SW draft block a divisor of the primary block (#60252)
  _Files: `tests/v1/attention/test_backend_per_kind.py`, `vllm/model_executor/layers/attention/attention.py`_
- **2026-11-04** [`d39d1b0f94`](https://github.com/vllm-project/vllm/commit/d39d1b0f94) [#63012](https://github.com/vllm-project/vllm/pull/63012)
  [Bugfix][Attention] Stop advertising head_dim 64 in the b12x backend (#63012)
  _Files: `tests/v1/attention/test_b12x.py`, `vllm/v1/attention/backends/b12x.py`_
- **2026-11-04** [`790be385c8`](https://github.com/vllm-project/vllm/commit/790be385c8) [#62265](https://github.com/vllm-project/vllm/pull/62265)
  [Bugfix][Attention] Let b12x pick its default KV block size (#62265)
  _Files: `tests/v1/attention/test_b12x.py`, `vllm/v1/attention/backends/b12x.py`_
- **2026-11-04** [`abf98672ce`](https://github.com/vllm-project/vllm/commit/abf98672ce) [#63406](https://github.com/vllm-project/vllm/pull/63406)
  [Core][CUDA Graph] Separate prefill (token) and decode (request) CUDA graph capture sizes (#63406)
  _Files: `docs/design/torch_compile.md`, `tests/compile/test_config.py`, `tests/v1/cudagraph/test_cudagraph_manager.py`, `tests/v1/spec_decode/test_dynamic_sd_cug.py` _+13 more__
- **2026-11-04** [`b81f32630a`](https://github.com/vllm-project/vllm/commit/b81f32630a) [#65416](https://github.com/vllm-project/vllm/pull/65416)
  [XPU] fix case test_p2p_lifecycle_e2e.py and test_mm_prefix_lm.py (#65416)
  _Files: `tests/v1/kv_offload/tiering/test_p2p_lifecycle_e2e.py`, `vllm/v1/attention/ops/triton_prefill_attention.py`_
- **2026-11-04** [`d3a3230931`](https://github.com/vllm-project/vllm/commit/d3a3230931) [#64059](https://github.com/vllm-project/vllm/pull/64059)
  [Bugfix] Fix DFlash draft acceptance of 0 with FULL CUDA graphs (#64059)
  _Files: `tests/v1/e2e/spec_decode/acceptance_rates/dflash/test_dflash.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`, `vllm/v1/worker/gpu/spec_decode/speculator.py`_
- **2026-11-04** [`cfc9f681e9`](https://github.com/vllm-project/vllm/commit/cfc9f681e9) [#65488](https://github.com/vllm-project/vllm/pull/65488)
  [Perf][Spec Decode] Pad DFlash draft inputs on extra programs of the same launch (#65488)
  _Files: `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`_
- **2026-11-03** [`f352490fc0`](https://github.com/vllm-project/vllm/commit/f352490fc0) [#60989](https://github.com/vllm-project/vllm/pull/60989)
  [MRV2][Spec Decode] Refactor AR speculators and enable CUDA Graph for draft model (#60989)
  _Files: `tests/v1/cudagraph/test_cudagraph_manager.py`, `tests/v1/spec_decode/test_dflash_profile.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/model_runner.py` _+7 more__
- **2026-11-03** [`ae525e95b9`](https://github.com/vllm-project/vllm/commit/ae525e95b9) [#64559](https://github.com/vllm-project/vllm/pull/64559)
  [HiSparse] Remove dead code, unused custom-op arguments, and a stale connector check (#64559)
  _Files: `csrc/hisparse_kernels.cu`, `csrc/ops.h`, `csrc/torch_bindings.cpp`, `tests/test_config.py` _+13 more__
- **2026-11-03** [`7b5492075d`](https://github.com/vllm-project/vllm/commit/7b5492075d) [#64916](https://github.com/vllm-project/vllm/pull/64916)
  [Spec Decode][Perf] Fuse DFlash2 candidate edge scoring into a Triton kernel (#64916)
  _Files: `tests/v1/spec_decode/test_dflash2.py`, `vllm/model_executor/models/qwen3_dflash2.py`, `vllm/models/beam/nvidia/dflash2.py`, `vllm/models/beam/nvidia/dflash2_ops.py`_
- **2026-11-03** [`b80941d3ca`](https://github.com/vllm-project/vllm/commit/b80941d3ca) [#65046](https://github.com/vllm-project/vllm/pull/65046)
  [Bugfix][DSv4] Skip empty compressed indexer prefill chunks (#65046)
  _Files: `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-11-03** [`b210285e84`](https://github.com/vllm-project/vllm/commit/b210285e84) [#64989](https://github.com/vllm-project/vllm/pull/64989)
  [Bugfix][HiSparse] Release temporary device KV bindings after graph profiling (#64989)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `tests/v1/worker/test_attn_utils.py`, `tests/v1/worker/test_utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/hisparse/worker.py` _+3 more__
- **2026-11-03** [`8ba4fe5f11`](https://github.com/vllm-project/vllm/commit/8ba4fe5f11) [#65214](https://github.com/vllm-project/vllm/pull/65214)
  [HiSparse] Support the extensible KV cache (#65214)
  _Files: `tests/v1/core/test_kv_cache_planning.py`, `tests/v1/e2e/general/test_hisparse.py`, `tests/v1/worker/test_attn_utils.py`, `tests/v1/worker/test_gpu_warmup_blocks.py` _+9 more__
- **2026-11-03** [`5daa9a6bb9`](https://github.com/vllm-project/vllm/commit/5daa9a6bb9) [#65258](https://github.com/vllm-project/vllm/pull/65258)
  [Doc] MiniMax-M3.1-Flash: drop DEP4 c96 and c128 from the GB300 AgentX presets (#65258)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-11-03** [`39dbf51839`](https://github.com/vllm-project/vllm/commit/39dbf51839) [#63801](https://github.com/vllm-project/vllm/pull/63801)
  [Perf][HiSparse] Prefetch speculative groups with bounded copy workers (#63801)
  _Files: `.buildkite/test_areas/attention.yaml`, `benchmarks/kernels/benchmark_hisparse_gather.py`, `csrc/hisparse_kernels.cu`, `docs/design/hisparse.md` _+3 more__
- **2026-11-03** [`4b01cbad1b`](https://github.com/vllm-project/vllm/commit/4b01cbad1b) [#62633](https://github.com/vllm-project/vllm/pull/62633)
  [Perf][Kernel][DSv4.1] Swap-AB CuTe DSL decode attention for small TP2/TP4 steps (#62633)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `benchmarks/kernels/benchmark_dsv41_mega_attn.py`, `tests/models/deepseek_v41/nvidia/test_swapab_decode.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py` _+1 more__
- **2026-11-03** [`b14e2f2792`](https://github.com/vllm-project/vllm/commit/b14e2f2792) [#65350](https://github.com/vllm-project/vllm/pull/65350)
  [Bugfix][Spec Decode] Use vllm.config.replace for the MRV1 DFlash draft config (#65350)
  _Files: `vllm/v1/spec_decode/dflash.py`_
- **2026-11-03** [`9226d6e59c`](https://github.com/vllm-project/vllm/commit/9226d6e59c) [#62367](https://github.com/vllm-project/vllm/pull/62367)
  [Feature] Support batch invariance for ShortConv (LFM2) models (#62367)
  _Files: `docs/features/batch_invariance.md`, `vllm/v1/attention/backends/short_conv_attn.py`_
- **2026-11-03** [`cf31617992`](https://github.com/vllm-project/vllm/commit/cf31617992) [#65033](https://github.com/vllm-project/vllm/pull/65033)
  [Mamba][MRV2] Plan Triton ReplaySSM decode on the GPU and support Model Runner V2 (#65033)
  _Files: `tests/kernels/mamba/test_replayssm_plan.py`, `tests/v1/attention/test_replayssm_metadata_builder.py`, `tests/v1/e2e/test_replayssm_decode.py`, `tests/v1/worker/test_utils.py` _+7 more__
- **2026-11-03** [`a5d8174ea0`](https://github.com/vllm-project/vllm/commit/a5d8174ea0) [#57245](https://github.com/vllm-project/vllm/pull/57245)
  [LoRA] Add DeepSeek V4.1 language-model adapter support (#57245)
  _Files: `tests/lora/test_layers.py`, `tests/v1/attention/test_deepseek_v4_swa_visible.py`, `vllm/lora/layers/__init__.py`, `vllm/lora/layers/custom_layer.py` _+7 more__
- **2026-11-03** [`45d0ac9ee1`](https://github.com/vllm-project/vllm/commit/45d0ac9ee1) [#64974](https://github.com/vllm-project/vllm/pull/64974)
  [Refactor][DSv4.1] Remove duplicated code (#64974)
  _Files: `tests/v1/attention/test_flashinfer_sparse_mla_sm120_api.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` _+5 more__
- **2026-11-03** [`a0d909f539`](https://github.com/vllm-project/vllm/commit/a0d909f539) [#56996](https://github.com/vllm-project/vllm/pull/56996)
  [Perf][Attention] Source Triton metadata builder geometry from kv_cache_spec (#56996)
  _Files: `tests/v1/attention/test_group_head_counts.py`, `vllm/v1/attention/backends/triton_attn.py`_
- **2026-11-03** [`bca1bc6516`](https://github.com/vllm-project/vllm/commit/bca1bc6516) [#61609](https://github.com/vllm-project/vllm/pull/61609)
  [Attention][DCP] Support DCP on the FlashMLA sparse bf16 KV path (#61609)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-11-03** [`0834bcf6f2`](https://github.com/vllm-project/vllm/commit/0834bcf6f2) [#63123](https://github.com/vllm-project/vllm/pull/63123)
  [Bugfix][Distributed] Gate FlashInfer all-reduce on 16-byte row widths  (#63123)
  _Files: `.buildkite/test_areas/distributed.yaml`, `tests/distributed/test_flashinfer_all_reduce.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-11-03** [`3c01fae696`](https://github.com/vllm-project/vllm/commit/3c01fae696) [#64417](https://github.com/vllm-project/vllm/pull/64417)
  [Perf] Skip custom-op dispatch for FlashInfer dense GEMMs in eager (#64417)
  _Files: `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`, `vllm/model_executor/kernels/linear/scaled_mm/flashinfer.py`, `vllm/model_executor/layers/quantization/utils/mxfp8_utils.py`, `vllm/model_executor/layers/utils.py` _+2 more__
- **2026-11-02** [`628c455e9e`](https://github.com/vllm-project/vllm/commit/628c455e9e) [#64806](https://github.com/vllm-project/vllm/pull/64806)
  [Bugfix][Attention] Bound SM100 decode indexer logits with query-row chunks (#64806)
  _Files: `docs/configuration/conserving_memory.md`, `tests/kernels/test_top_k_per_row.py`, `vllm/envs.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-11-02** [`9a3ee89b91`](https://github.com/vllm-project/vllm/commit/9a3ee89b91) [#62623](https://github.com/vllm-project/vllm/pull/62623)
  [XPU][Test] Skip attention fusion splitting_ops check on XPU (#62623)
  _Files: `tests/compile/test_config.py`_
- **2026-11-02** [`a11d3a15f6`](https://github.com/vllm-project/vllm/commit/a11d3a15f6) [#65178](https://github.com/vllm-project/vllm/pull/65178)
  [Perf][DCP] Sparse indexer: read the rank-major DCP top-k gather in place (#65178)
  _Files: `tests/v1/attention/test_indexer_dcp_localize.py`, `vllm/model_executor/kernels/attention/dsa/dcp_indexer_cutedsl.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-11-02** [`3a228c1fef`](https://github.com/vllm-project/vllm/commit/3a228c1fef) [#59999](https://github.com/vllm-project/vllm/pull/59999)
  [Bugfix] FlashInfer: declare only KV layouts it can address (#59999)
  _Files: `tests/v1/attention/test_attention_backends.py`, `vllm/v1/attention/backends/flashinfer.py`, `vllm/v1/attention/backends/utils.py`_
- **2026-11-02** [`28dd9c36b5`](https://github.com/vllm-project/vllm/commit/28dd9c36b5) [#62632](https://github.com/vllm-project/vllm/pull/62632)
  [Perf][Kernel][DSv4.1] Copy-based Q zero-pad for large eager mega-attention steps (#62632)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn.py`_
- **2026-11-02** [`4910ee107c`](https://github.com/vllm-project/vllm/commit/4910ee107c) [#65201](https://github.com/vllm-project/vllm/pull/65201)
  [Bugfix][HiSparse] Avoid the MNNVL FlashInfer all-reduce with HiSparse (#65201)
  _Files: `tests/distributed/test_comm_ops.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-11-02** [`ca66f0906f`](https://github.com/vllm-project/vllm/commit/ca66f0906f) [#64475](https://github.com/vllm-project/vllm/pull/64475)
  [MiniMax-M3.1][P/D] NIXL KV-head re-sharding for per-head-contiguous NVFP4 pages (#64475)
  _Files: `tests/kernels/test_fused_minimax_m3_qknorm_rope_kv_insert.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+2 more__
- **2026-11-02** [`4a0dfc7b2f`](https://github.com/vllm-project/vllm/commit/4a0dfc7b2f) [#61641](https://github.com/vllm-project/vllm/pull/61641)
  [Perf][Kernel] Convert two FP8 values per cvt in the FP8 quant kernels (#61641)
  _Files: `csrc/attention/merge_attn_states.cu`, `csrc/core/cuda_compat.h`, `csrc/quantization/fused_kernels/layernorm_utils.cuh`, `csrc/quantization/fused_kernels/quant_conversions.cuh` _+4 more__
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

## MoE / Expert Parallel  (60 commits)

- **2026-11-09** [`6d0de315ec`](https://github.com/vllm-project/vllm/commit/6d0de315ec) [#65406](https://github.com/vllm-project/vllm/pull/65406)
  [Bugfix][MoE] Count the expert down-projection bias once under TP (#65406)
  _Files: `tests/kernels/moe/test_moe_layer.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-11-09** [`5f2aca75a8`](https://github.com/vllm-project/vllm/commit/5f2aca75a8) [#66537](https://github.com/vllm-project/vllm/pull/66537)
  [Perf][MoE] Add H200 FP8 config for GLM-5.3-Flash TP8 (#66537)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=288,N=256,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128,128].json`_
- **2026-11-09** [`5ea76f99bb`](https://github.com/vllm-project/vllm/commit/5ea76f99bb) [#64315](https://github.com/vllm-project/vllm/pull/64315)
  [Model][Qwen4Exp] Run routed experts on DeepGEMM MegaMoE (MXFP8 or MXFP4) (#64315)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/qwen4_exp/test_mega_moe.py`, `vllm/model_executor/warmup/deep_gemm_warmup.py`, `vllm/models/qwen4_exp/nvidia/mega_moe.py` _+1 more__
- **2026-11-09** [`1648e80a6a`](https://github.com/vllm-project/vllm/commit/1648e80a6a) [#66486](https://github.com/vllm-project/vllm/pull/66486)
  [Bugfix][LoRA] Fix MoE LoRA correctness under DP + EP (#66486)
  _Files: `tests/lora/test_lora_functions.py`, `tests/lora/test_olmoe_tp.py`, `tests/lora/test_punica_ops.py`, `vllm/lora/ops/triton_ops/lora_kernel_metadata.py` _+6 more__
- **2026-11-09** [`b6ed63d2ac`](https://github.com/vllm-project/vllm/commit/b6ed63d2ac) [#64437](https://github.com/vllm-project/vllm/pull/64437)
  [Bugfix][LoRA] Use 3D MoE LoRA wrapper for Gemma4 (#64437)
  _Files: `tests/lora/test_gemma4_moe_lora.py`, `vllm/model_executor/models/gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-11-09** [`b0fd6874a0`](https://github.com/vllm-project/vllm/commit/b0fd6874a0) [#60609](https://github.com/vllm-project/vllm/pull/60609)
  [XPU] Bump up kernel 0.1.17, change MoE and MLA interfaces (#60609)
  _Files: `requirements/xpu.txt`, `vllm/_custom_ops.py`, `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py` _+1 more__
- **2026-11-09** [`4088c2838a`](https://github.com/vllm-project/vllm/commit/4088c2838a) [#66037](https://github.com/vllm-project/vllm/pull/66037)
  [Core][Kimi K3.1] KV cache and attention changes to serve Kimi K3.1 at TP8 (Kimi K3.1 split 3/5) (#66037)
  _Files: `tests/models/kimi_k3/nvidia/specialized_decode/test_specialized_decode_dep.py`, `tests/models/kimi_k3/nvidia/specialized_decode/test_specialized_decode_dsa.py`, `tests/models/kimi_k3/nvidia/specialized_decode/test_specialized_decode_dsa_sparse.py`, `tests/models/kimi_k3/nvidia/specialized_decode/test_specialized_decode_moe.py` _+30 more__
- **2026-11-09** [`199c2e4bff`](https://github.com/vllm-project/vllm/commit/199c2e4bff) [#51006](https://github.com/vllm-project/vllm/pull/51006)
  [MoE] Make fused MoE routers pluggable (#51006)
  _Files: `docs/design/plugin_system.md`, `tests/kernels/moe/test_routing.py`, `vllm/model_executor/layers/fused_moe/router/fused_moe_router.py`_
- **2026-11-09** [`3213796cd3`](https://github.com/vllm-project/vllm/commit/3213796cd3) [#66441](https://github.com/vllm-project/vllm/pull/66441)
  [CI] Fix docstring style in benchmark_batched_moe.py (#66441)
  _Files: `benchmarks/kernels/benchmark_batched_moe.py`_
- **2026-11-09** [`e5f2ea9be8`](https://github.com/vllm-project/vllm/commit/e5f2ea9be8) [#66287](https://github.com/vllm-project/vllm/pull/66287)
  [Sleep Mode] Remove level-2 workarounds that #66010 makes unnecessary (#66287)
  _Files: `tests/lora/test_layers.py`, `tests/v1/worker/test_gpu_worker_weight_transfer.py`, `vllm/lora/layers/logits_processor.py`, `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py` _+8 more__
- **2026-11-08** [`0555390170`](https://github.com/vllm-project/vllm/commit/0555390170) [#46871](https://github.com/vllm-project/vllm/pull/46871)
  [XPU] All-to-all Expert-Parallellism backend for batched MoE (#46871)
  _Files: `benchmarks/kernels/benchmark_batched_moe.py`, `benchmarks/kernels/merge_batched_moe_configs.py`, `tests/kernels/moe/test_alltoall_batched_capacity.py`, `vllm/config/parallel.py` _+34 more__
- **2026-11-08** [`15166efabb`](https://github.com/vllm-project/vllm/commit/15166efabb) [#65766](https://github.com/vllm-project/vllm/pull/65766)
  [DeepSeek-V4] Support sequence parallelism with pipeline parallelism for MegaMoE (#65766)
  _Files: `tests/models/test_deepseek_v4_fi_moe_ep.py`, `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-11-08** [`73d0083d28`](https://github.com/vllm-project/vllm/commit/73d0083d28) [#66190](https://github.com/vllm-project/vllm/pull/66190)
  [Bugfix][Qwen2.5-Omni] Size the video encoder budget from the processor's video limits (#66190)
  _Files: `tests/models/multimodal/processing/test_qwen2_5_omni.py`, `tests/models/multimodal/processing/test_qwen3_omni.py`, `vllm/model_executor/models/clef_omni.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py` _+1 more__
- **2026-11-07** [`57d8e025e9`](https://github.com/vllm-project/vllm/commit/57d8e025e9) [#66100](https://github.com/vllm-project/vllm/pull/66100)
  [CPU][Refactor] Move CPU ops wrappers to vllm/_cpu_ops.py (#66100)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/hardware_tests/zen.yaml`, `benchmarks/kernels/cpu/benchmark_cpu_attn.py`, `benchmarks/kernels/cpu/benchmark_cpu_fused_moe.py` _+43 more__
- **2026-11-07** [`9dd8328eb9`](https://github.com/vllm-project/vllm/commit/9dd8328eb9) [#66273](https://github.com/vllm-project/vllm/pull/66273)
  [Kimi-K3] Keep the latent-MoE tail fusion under sleep mode (#66273)
  _Files: `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`_
- **2026-11-07** [`c9e4cb2b79`](https://github.com/vllm-project/vllm/commit/c9e4cb2b79) [#59767](https://github.com/vllm-project/vllm/pull/59767)
  [Model] Migrate Aria to the Transformers modeling backend (#59767)
  _Files: `docs/models/supported_models.md`, `examples/generate/multimodal/vision_language_multi_image_offline.py`, `tests/lora/test_lora_manager.py`, `tests/models/multimodal/generation/test_common.py` _+6 more__
- **2026-11-07** [`a8dacd7238`](https://github.com/vllm-project/vllm/commit/a8dacd7238) [#66015](https://github.com/vllm-project/vllm/pull/66015)
  [Bugfix][MoE] Stop DeepGEMM's MLOPart helper once MegaMoE caches its SM map (#66015)
  _Files: `vllm/model_executor/layers/fused_moe/deep_gemm_mega_moe.py`_
- **2026-11-07** [`2f58f98557`](https://github.com/vllm-project/vllm/commit/2f58f98557) [#66227](https://github.com/vllm-project/vllm/pull/66227)
  [Perf][MiniMax-M3] Warm up DeepGEMM NVFP4 MegaMoE kernels before serving (#66227)
  _Files: `tests/model_executor/test_deep_gemm_warmup.py`, `vllm/model_executor/warmup/deep_gemm_warmup.py`, `vllm/models/minimax_m3/nvidia/model.py`_
- **2026-11-06** [`8b60d59945`](https://github.com/vllm-project/vllm/commit/8b60d59945) [#57823](https://github.com/vllm-project/vllm/pull/57823)
  [Bugfix][MoE] Respect padded row strides in top-k routing (#57823)
  _Files: `csrc/moe/topk_softmax_kernels.cu`, `tests/kernels/moe/test_fused_topk.py`_
- **2026-11-06** [`05737d01eb`](https://github.com/vllm-project/vllm/commit/05737d01eb) [#64410](https://github.com/vllm-project/vllm/pull/64410)
  [Quantization] Support w4afp8 checkpoints on the W4A8 FP8 MoE path (#64410)
  _Files: `vllm/model_executor/layers/quantization/__init__.py`, `vllm/model_executor/layers/quantization/w4afp8.py`_
- **2026-11-06** [`2e4da26899`](https://github.com/vllm-project/vllm/commit/2e4da26899) [#65746](https://github.com/vllm-project/vllm/pull/65746)
  [GLM 5.3 Perf] Expand fp8 moe tma for sm100, 1.03~1.60x kernel performance improvement (#65746)
  _Files: `tests/kernels/moe/test_block_fp8.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`_
- **2026-11-06** [`687c607faf`](https://github.com/vllm-project/vllm/commit/687c607faf) [#65955](https://github.com/vllm-project/vllm/pull/65955)
  [Quantization] Avoid importing humming when resolving quantization configs (#65955)
  _Files: `vllm/model_executor/layers/quantization/utils/humming/moe.py`, `vllm/model_executor/layers/quantization/utils/humming/schema.py`_
- **2026-11-06** [`fae0ac86ad`](https://github.com/vllm-project/vllm/commit/fae0ac86ad) [#66097](https://github.com/vllm-project/vllm/pull/66097)
  [Model] Use the upstream config for Qwen3-ASR (#66097)
  _Files: `vllm/model_executor/models/qwen3_asr.py`, `vllm/model_executor/models/qwen3_asr_forced_aligner.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`, `vllm/transformers_utils/config.py` _+3 more__
- **2026-11-06** [`0dbab8add1`](https://github.com/vllm-project/vllm/commit/0dbab8add1) [#63349](https://github.com/vllm-project/vllm/pull/63349)
  [MOE oracle][Refactor][1/N] Deduplicate the MoE oracle selection and backend code (#63349)
  _Files: `tests/kernels/moe/test_moe_kernel_oracle.py`, `tests/quantization/test_online.py`, `vllm/model_executor/layers/fused_moe/oracle/base.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py` _+8 more__
- **2026-11-06** [`6c13a380b1`](https://github.com/vllm-project/vllm/commit/6c13a380b1) [#61593](https://github.com/vllm-project/vllm/pull/61593)
  [CPU] Enable gelu_tanh activation support for Gemma4 MoE (#61593)
  _Files: `csrc/cpu/dynamic_4bit_int_moe_cpu.cpp`, `vllm/model_executor/layers/fused_moe/experts/cpu_int4_moe.py`_
- **2026-11-06** [`9465d04afc`](https://github.com/vllm-project/vllm/commit/9465d04afc) [#66017](https://github.com/vllm-project/vllm/pull/66017)
  [Bugfix][Qwen3-Omni] Size the video encoder budget from the processor's video limits (#66017)
  _Files: `tests/models/multimodal/processing/test_qwen3_omni.py`, `vllm/model_executor/models/clef_omni.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`_
- **2026-11-06** [`ba15685ab7`](https://github.com/vllm-project/vllm/commit/ba15685ab7) [#64352](https://github.com/vllm-project/vllm/pull/64352)
  [Model Loader] Direct reload: reset MoE expert padding at begin (#64352)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/moe/test_fp8_tp_loading.py`, `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py` _+2 more__
- **2026-11-06** [`e6c60746e6`](https://github.com/vllm-project/vllm/commit/e6c60746e6) [#65930](https://github.com/vllm-project/vllm/pull/65930)
  [Dependency] Upgrade FlashInfer to 0.7.3 (#65930)
  _Files: `requirements/cuda.txt`, `tests/distributed/test_mnnvl_alltoall.py`, `tests/kernels/moe/test_moe_layer.py`, `vllm/distributed/device_communicators/all2all.py` _+4 more__
- **2026-11-05** [`24a49203ee`](https://github.com/vllm-project/vllm/commit/24a49203ee) [#54109](https://github.com/vllm-project/vllm/pull/54109)
  [MoE][DeepEPV2] Add PaddedStandard activation format (#54109)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-sm100-fi-mxfp4-mxfp8-trtllm-deepep-v2.yaml`, `tests/evals/gpt_oss/configs/models-b200-deepep-v2.txt`, `tests/evals/gsm8k/configs/moe-refactor-dp-ep/Qwen3-30B-A3B-BF16-fi-trtllm-deepep-v2.yaml` _+45 more__
- **2026-11-05** [`df05643664`](https://github.com/vllm-project/vllm/commit/df05643664) [#62759](https://github.com/vllm-project/vllm/pull/62759)
  [Quant] LUT-B MoE with MXFP8 activations: native Rubin kernel + emulation (#62759)
  _Files: `CMakeLists.txt`, `csrc/moe/lut_b_moe_sm107.cu`, `csrc/moe/moe_ops.h`, `csrc/moe/torch_bindings.cpp` _+12 more__
- **2026-11-05** [`c03d46c7a8`](https://github.com/vllm-project/vllm/commit/c03d46c7a8) [#65825](https://github.com/vllm-project/vllm/pull/65825)
  [Bugfix][LoRA] Align GPT-OSS MXFP4 LoRA TP shards with base weights (#65825)
  _Files: `vllm/lora/layers/fused_moe.py`_
- **2026-11-05** [`463e23b1de`](https://github.com/vllm-project/vllm/commit/463e23b1de) [#64689](https://github.com/vllm-project/vllm/pull/64689)
  [Feature][MoE] Allow a shared routed-expert row restorer (#64689)
  _Files: `docs/training/routed_experts.md`, `tests/model_executor/test_routed_experts_capture.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `tests/v1/worker/test_gpu_ubatch_slicing.py` _+1 more__
- **2026-11-05** [`9901ffcb4a`](https://github.com/vllm-project/vllm/commit/9901ffcb4a) [#51808](https://github.com/vllm-project/vllm/pull/51808)
  [Online quantization] Support activation quant key override for online MXFP4 linear/MOE quant methods (#51808)
  _Files: `docs/features/quantization/online.md`, `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/kernels/quantization/test_mxfp4_w4a8_rdna3.py`, `tests/model_executor/layers/test_fused_shared_expert.py` _+12 more__
- **2026-11-05** [`1ab4476ac9`](https://github.com/vllm-project/vllm/commit/1ab4476ac9) [#65088](https://github.com/vllm-project/vllm/pull/65088)
  [Bugfix][Model] Fix Ling3 SwiGLU clamping (#65088)
  _Files: `vllm/model_executor/layers/fused_moe/activation.py`, `vllm/model_executor/models/bailing_moe_v3.py`_
- **2026-11-05** [`305a8396f5`](https://github.com/vllm-project/vllm/commit/305a8396f5) [#63711](https://github.com/vllm-project/vllm/pull/63711)
  [CPU][Zen] Enable Laguna MoE on Zen CPU via grouped W8A16 (DA8W8) (#63711)
  _Files: `tests/kernels/moe/test_cpu_fused_moe.py`, `tests/kernels/quantization/test_zen_da8w4.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/experts/zentorch_moe.py` _+2 more__
- **2026-11-05** [`7e3c015543`](https://github.com/vllm-project/vllm/commit/7e3c015543) [#60895](https://github.com/vllm-project/vllm/pull/60895)
  [Perf][GLM-5.3-Flash] DeepGEMM FP8 MegaMoE with fused shared experts (#60895)
  _Files: `tests/models/glm5next/test_mega_moe.py`, `vllm/model_executor/layers/quantization/utils/mxfp8_utils.py`, `vllm/models/glm5next/common/model.py`, `vllm/models/glm5next/common/mtp.py` _+1 more__
- **2026-11-04** [`ff9b7d3ae3`](https://github.com/vllm-project/vllm/commit/ff9b7d3ae3) [#65542](https://github.com/vllm-project/vllm/pull/65542)
  [Kernel] Marlin: remove 8-bit (INT8/FP8) activation support, rely on Humming (#65542)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_machete.py`, `benchmarks/kernels/benchmark_marlin.py`, `csrc/moe/marlin_moe_wna16/kernel.h` _+48 more__
- **2026-11-04** [`42c043c6b0`](https://github.com/vllm-project/vllm/commit/42c043c6b0) [#64760](https://github.com/vllm-project/vllm/pull/64760)
  [GLM 5.3 Perf] Sorted-A TMA for FP8 MoE down projection on H200, 6.0%~ 7.6% E2E Throughput Improvement (#64760)
  _Files: `tests/kernels/moe/test_block_fp8.py`, `vllm/model_executor/layers/fused_moe/configs/E=256,N=256,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128,128]_down.json`, `vllm/model_executor/layers/fused_moe/configs/E=256,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128,128]_down.json`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py` _+1 more__
- **2026-11-04** [`ef9339e64d`](https://github.com/vllm-project/vllm/commit/ef9339e64d) [#65438](https://github.com/vllm-project/vllm/pull/65438)
  [Model] Optimize Muse Spark GEMM and communication-norm fusion (#65438)
  _Files: `vllm/model_executor/layers/fused_moe/router/gate_linear.py`, `vllm/models/common/ops/sequence_parallel.py`, `vllm/models/muse_spark/nvidia/hybrid_moe.py`, `vllm/models/muse_spark/nvidia/mega_moe.py` _+3 more__
- **2026-11-04** [`75f6761497`](https://github.com/vllm-project/vllm/commit/75f6761497) [#64583](https://github.com/vllm-project/vllm/pull/64583)
  [Bugfix][Kimi-K3] Fall back from the latent-MoE tail fusion under sleep mode (#64583)
  _Files: `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`_
- **2026-11-04** [`11558e37e4`](https://github.com/vllm-project/vllm/commit/11558e37e4) [#62172](https://github.com/vllm-project/vllm/pull/62172)
  [Perf][Kernel] Let cooperative_topk read the BF16 indexer logits (#62172)
  _Files: `csrc/cooperative_topk.cu`, `csrc/cooperative_topk.cuh`, `csrc/cooperative_topk_overflow.cuh`, `csrc/topk_histogram_4096.cuh` _+5 more__
- **2026-11-04** [`c58e7f6d05`](https://github.com/vllm-project/vllm/commit/c58e7f6d05) [#63921](https://github.com/vllm-project/vllm/pull/63921)
  [Perf][DSv4.1] Extend the latency_specialized decode on NVIDIA (#63921)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/distributed/test_custom_all_reduce.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_all_gather.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/test_decode_topk.py` _+37 more__
- **2026-11-04** [`5c97556318`](https://github.com/vllm-project/vllm/commit/5c97556318) [#65498](https://github.com/vllm-project/vllm/pull/65498)
  [Perf][MoE] Skip the combine staging copy in flashinfer_nvlink_one_sided (#65498)
  _Files: `tests/distributed/test_mnnvl_alltoall.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_one_sided.py`_
- **2026-11-04** [`62966a7e00`](https://github.com/vllm-project/vllm/commit/62966a7e00) [#62234](https://github.com/vllm-project/vllm/pull/62234)
  [Bugfix][Spec Decode] Align speculator hidden norm in GLM-4.5/4.6 MoE and GLM-OCR MTP with GLM5Next to recycle post-final-hidden. (#62234)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `tests/v1/e2e/spec_decode/mtp/glm/__init__.py`, `tests/v1/e2e/spec_decode/mtp/glm/test_mtp.py`, `tests/v1/spec_decode/test_llm_base_proposer_sampling.py` _+5 more__
- **2026-11-04** [`ba9a98b881`](https://github.com/vllm-project/vllm/commit/ba9a98b881) [#64077](https://github.com/vllm-project/vllm/pull/64077)
  [Perf] Muse Spark Open Specialized Decode: Optimized GB300 Decode (1.5x) (#64077)
  _Files: `vllm/models/muse_spark/common/dspark.py`, `vllm/models/muse_spark/nvidia/model.py`, `vllm/models/muse_spark/nvidia/model_state.py`, `vllm/models/muse_spark/nvidia/specialized_decode/__init__.py` _+38 more__
- **2026-11-04** [`7981158d3e`](https://github.com/vllm-project/vllm/commit/7981158d3e) [#56606](https://github.com/vllm-project/vllm/pull/56606)
  [Bugfix][Quantization] Fix online MoE weight conversion `KeyError: 'weight_scale'` with Humming (#56606)
  _Files: `tests/quantization/test_fp8.py`, `tests/quantization/test_online.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py` _+2 more__
- **2026-11-04** [`3b7181e972`](https://github.com/vllm-project/vllm/commit/3b7181e972) [#65504](https://github.com/vllm-project/vllm/pull/65504)
  [Step5] Allow MegaMoE with pipeline parallelism (#65504)
  _Files: `vllm/models/step5/nvidia/mega_moe.py`, `vllm/models/step5/nvidia/model.py`_
- **2026-11-03** [`ab4e04d2dc`](https://github.com/vllm-project/vllm/commit/ab4e04d2dc) [#64580](https://github.com/vllm-project/vllm/pull/64580)
  [Kernel][DSA] Restore FP32 indexer MQA logits for non-DeepSeek models and add `indexer_logits_dtype` (#64580)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `cmake/external_projects/deepgemm.cmake`, `docs/configuration/conserving_memory.md`, `tests/kernels/attention/test_deepgemm_attention.py` _+14 more__
- **2026-11-03** [`fbb488f7d2`](https://github.com/vllm-project/vllm/commit/fbb488f7d2) [#57167](https://github.com/vllm-project/vllm/pull/57167)
  [Bugfix][MoE] Reject non-contiguous routing tensors (#57167)
  _Files: `csrc/moe/moe_align_sum_kernels.cu`, `tests/kernels/moe/test_moe.py`, `tests/kernels/moe/test_moe_align_block_size.py`, `tests/kernels/moe/test_routing.py` _+2 more__
- **2026-11-03** [`ff74259da3`](https://github.com/vllm-project/vllm/commit/ff74259da3) [#65452](https://github.com/vllm-project/vllm/pull/65452)
  [Misc] Add LiteTopK acknowledgement to fused_mqa_topk (#65452)
  _Files: `csrc/fused_mqa_topk/fused_mqa_topk.cu`_
- **2026-11-03** [`a900ac810e`](https://github.com/vllm-project/vllm/commit/a900ac810e) [#65185](https://github.com/vllm-project/vllm/pull/65185)
  [Compile] Fix compile warning topk `csrc/topk_histogram_4096_overflow.cuh` (#65185)
  _Files: `csrc/topk_histogram_4096.cuh`, `csrc/topk_histogram_4096_overflow.cuh`_
- **2026-11-03** [`44965a1097`](https://github.com/vllm-project/vllm/commit/44965a1097) [#63672](https://github.com/vllm-project/vllm/pull/63672)
  [Fast Start] Support online FP8 and CUTLASS NVFP4 weight-cache restarts (#63672)
  _Files: `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`, `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py` _+3 more__
- **2026-11-03** [`c7a7607519`](https://github.com/vllm-project/vllm/commit/c7a7607519) [#62275](https://github.com/vllm-project/vllm/pull/62275)
  [Bugfix] Disable CUTLASS FP4 MoE backend on sm_110 (#62275)
  _Files: `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`_
- **2026-11-03** [`9b14bef3be`](https://github.com/vllm-project/vllm/commit/9b14bef3be) [#56102](https://github.com/vllm-project/vllm/pull/56102)
  [Bugfix][Kernel] Fix cooperative top-k dispatch on SM110 (#56102)
  _Files: `vllm/model_executor/layers/indexer_topk.py`, `vllm/models/qwen4_exp/nvidia/ops/qsa_indexer.py`_
- **2026-11-03** [`18538fef06`](https://github.com/vllm-project/vllm/commit/18538fef06) [#65152](https://github.com/vllm-project/vllm/pull/65152)
  [Kernel] Enable Step5 SwiGLU in TRTLLM MoE (#65152)
  _Files: `docs/design/moe_kernel_features.md`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`_
- **2026-11-03** [`437288d18a`](https://github.com/vllm-project/vllm/commit/437288d18a) [#58868](https://github.com/vllm-project/vllm/pull/58868)
  [Perf][Model Loader] Fault in mmap'd weight pages before host-to-device copies on integrated GPUs (#58868)
  _Files: `tests/model_executor/test_utils.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/vocab_parallel_embedding.py` _+3 more__
- **2026-11-03** [`cd1effa2e7`](https://github.com/vllm-project/vllm/commit/cd1effa2e7) [#65051](https://github.com/vllm-project/vllm/pull/65051)
  [Bugfix][LoRA][XPU] Skip MoE-LoRA shrink/expand when no LoRA is active (#65051)
  _Files: `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`_
- **2026-11-02** [`187f1a27dc`](https://github.com/vllm-project/vllm/commit/187f1a27dc) [#65059](https://github.com/vllm-project/vllm/pull/65059)
  [Bugfix][Kernel] Only set PDL launch attr for MoE top-k gating on SM90+ (#65059)
  _Files: `csrc/moe/topk_softmax_kernels.cu`_
- **2026-11-02** [`37e16689fa`](https://github.com/vllm-project/vllm/commit/37e16689fa) [#64659](https://github.com/vllm-project/vllm/pull/64659)
  [Perf][MiniMax-M3] Sequence parallelism and GEMM-RS for TP + MegaMoE (#64659)
  _Files: `benchmarks/kernels/benchmark_gemm_rs_ar.py`, `tests/kernels/test_gemm_rs_ar.py`, `vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py`, `vllm/models/minimax_m3/nvidia/model.py`_
- **2026-11-02** [`16d667348d`](https://github.com/vllm-project/vllm/commit/16d667348d) [#64914](https://github.com/vllm-project/vllm/pull/64914)
  [MRV2] Cap torch.topk rows in chunked prompt logprobs (#64914)
  _Files: `tests/v1/sample/test_logprobs.py`, `vllm/v1/worker/gpu/sample/prompt_logprob.py`_

## Other  (55 commits)

- **2026-11-09** [`97df49e943`](https://github.com/vllm-project/vllm/commit/97df49e943) [#65156](https://github.com/vllm-project/vllm/pull/65156)
  [Bugfix][Frontend] Close the parent's listening sockets after launching the Rust frontend (#65156)
  _Files: `tests/entrypoints/launchers/api_server/test_api_server_process_manager.py`, `vllm/v1/utils.py`_
- **2026-11-09** [`bf1ada663a`](https://github.com/vllm-project/vllm/commit/bf1ada663a) [#66482](https://github.com/vllm-project/vllm/pull/66482)
  [Core][Bugfix] Run the warmup dummy forward on every PP rank before the GPU sync check (#66482)
  _Files: `tests/v1/worker/test_gpu_worker.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-11-09** [`8a782b05b9`](https://github.com/vllm-project/vllm/commit/8a782b05b9) [#66518](https://github.com/vllm-project/vllm/pull/66518)
  [Refactor][SleepMode] Make CuMemAllocator helpers overridable (#66518)
  _Files: `tests/basic_correctness/memory/cumem/test_cumem.py`, `tests/basic_correctness/memory/sleep_mode/test_sleep_mode.py`, `vllm/device_allocator/cumem.py`_
- **2026-11-09** [`1fc9a6fcd1`](https://github.com/vllm-project/vllm/commit/1fc9a6fcd1) [#61492](https://github.com/vllm-project/vllm/pull/61492)
  [Bugfix][Metrics] Periodic stats line: dead Preemptions field + Finished count (#61492)
  _Files: `tests/v1/metrics/test_logging_stat_logger.py`, `vllm/v1/metrics/loggers.py`_
- **2026-11-09** [`c2320e37f1`](https://github.com/vllm-project/vllm/commit/c2320e37f1) [#66119](https://github.com/vllm-project/vllm/pull/66119)
  [Rust Frontend] Support --log-level and --logging-config (#66119)
  _Files: `rust/Cargo.lock`, `rust/src/bench/src/main.rs`, `rust/src/cmd/Cargo.toml`, `rust/src/cmd/src/cli.rs` _+7 more__
- **2026-11-09** [`eafe6af276`](https://github.com/vllm-project/vllm/commit/eafe6af276) [#66476](https://github.com/vllm-project/vllm/pull/66476)
  [Rust Frontend] Accept FastAPI boolean spellings for reset_connector (#66476)
  _Files: `rust/src/server/src/routes/sleep.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-11-09** [`3a092abe98`](https://github.com/vllm-project/vllm/commit/3a092abe98) [#66477](https://github.com/vllm-project/vllm/pull/66477)
  [Rust Frontend] Keep special tokens' spelling in logprob tokens (#66477)
  _Files: `rust/src/text/src/output/decoded.rs`, `rust/src/text/src/output/logprobs.rs`_
- **2026-11-09** [`feed3a4475`](https://github.com/vllm-project/vllm/commit/feed3a4475) [#64499](https://github.com/vllm-project/vllm/pull/64499)
  [Bugfix][CPU] Name the cause when a DP rank's assigned NUMA nodes don't exist (#64499)
  _Files: `tests/utils_/test_cpu_resource_utils.py`, `vllm/utils/cpu_resource_utils.py`, `vllm/utils/ompmultiprocessing.py`, `vllm/v1/worker/cpu_worker.py`_
- **2026-11-08** [`83630ab85e`](https://github.com/vllm-project/vllm/commit/83630ab85e) [#59994](https://github.com/vllm-project/vllm/pull/59994)
  [Bugfix] Offload model runner construction buffers on sleep (#59994)
  _Files: `tests/basic_correctness/memory/cumem/test_cumem.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-11-08** [`c724bb35d4`](https://github.com/vllm-project/vllm/commit/c724bb35d4) [#65323](https://github.com/vllm-project/vllm/pull/65323)
  [XPU][UT] Preserve RoPE buffer dtype for HF reference in the privacy-filter model test on XPU (#65323)
  _Files: `tests/conftest.py`_
- **2026-11-07** [`aac1b2a4f3`](https://github.com/vllm-project/vllm/commit/aac1b2a4f3) [#63373](https://github.com/vllm-project/vllm/pull/63373)
  [Core] Remove Model Runner V1 (#63373)
- **2026-11-07** [`690364833e`](https://github.com/vllm-project/vllm/commit/690364833e) [#64528](https://github.com/vllm-project/vllm/pull/64528)
  [Misc] Bump ruff to v0.17.2 and enable UP032, UP042, B007, F403 and F405 (#64528)
- **2026-11-07** [`afe295e707`](https://github.com/vllm-project/vllm/commit/afe295e707) [#66080](https://github.com/vllm-project/vllm/pull/66080)
  [Bugfix][DeepGEMM] Match relax warmup M values to the vendored SM100 heuristic (#66080)
  _Files: `vllm/model_executor/warmup/deep_gemm_warmup.py`_
- **2026-11-06** [`bc01b9b83d`](https://github.com/vllm-project/vllm/commit/bc01b9b83d) [#62529](https://github.com/vllm-project/vllm/pull/62529)
  [Tests] Add TP2 PCP2 canonical mapping byte coverage (#62529)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_canonical_mapping.py`_
- **2026-11-06** [`4d82b56913`](https://github.com/vllm-project/vllm/commit/4d82b56913) [#66048](https://github.com/vllm-project/vllm/pull/66048)
  [BugFix] Fix/spec decode insert resampled race (#66048)
  _Files: `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-11-06** [`829902026f`](https://github.com/vllm-project/vllm/commit/829902026f) [#60047](https://github.com/vllm-project/vllm/pull/60047)
  [Bugfix] Register the aten::mm out_dtype overloads for batch invariance (#60047)
  _Files: `tests/v1/determinism/test_matmul_batch_invariant.py`, `vllm/model_executor/determinism/batch_invariant.py`_
- **2026-11-06** [`4b6d1cc419`](https://github.com/vllm-project/vllm/commit/4b6d1cc419) [#60438](https://github.com/vllm-project/vllm/pull/60438)
  [Bugfix] Fall back from DeepGEMM when nvcc is older than 12.9 (#60438)
  _Files: `tests/utils_/test_deep_gemm_utils.py`, `vllm/utils/deep_gemm.py`_
- **2026-11-06** [`f29cbad494`](https://github.com/vllm-project/vllm/commit/f29cbad494) [#66012](https://github.com/vllm-project/vllm/pull/66012)
  [Bugfix] Do not retry safetensors metadata lookup in offline mode (#66012)
  _Files: `vllm/transformers_utils/config.py`_
- **2026-11-06** [`7cf31d2f19`](https://github.com/vllm-project/vllm/commit/7cf31d2f19) [#65977](https://github.com/vllm-project/vllm/pull/65977)
  [Misc] Add NIXL team to nixl label (#65977)
  _Files: `.github/mergify.yml`_
- **2026-11-06** [`f358f0578a`](https://github.com/vllm-project/vllm/commit/f358f0578a) [#64164](https://github.com/vllm-project/vllm/pull/64164)
  [Ray][Metrics] Keep Ray metrics usable without Ray Serve (#64164)
  _Files: `vllm/v1/metrics/ray_wrappers.py`_
- **2026-11-06** [`61968a50d5`](https://github.com/vllm-project/vllm/commit/61968a50d5) [#65229](https://github.com/vllm-project/vllm/pull/65229)
  [Bugfix][Spec Decode] Avoid catastrophic cancellation in the acceptance estimator (#65229)
  _Files: `tests/v1/spec_decode/test_acceptance_estimator.py`, `vllm/v1/worker/gpu/spec_decode/acceptance_estimator.py`_
- **2026-11-06** [`7045518494`](https://github.com/vllm-project/vllm/commit/7045518494) [#65725](https://github.com/vllm-project/vllm/pull/65725)
  [Recipe] Kimi-K3.1-Pro: add TPU serving via vllm-torchtpu (#65725)
  _Files: `recipes/models/moonshotai/Kimi-K3.1-Pro.yaml`_
- **2026-11-06** [`a3b181bfba`](https://github.com/vllm-project/vllm/commit/a3b181bfba) [#64478](https://github.com/vllm-project/vllm/pull/64478)
  [XPU][UT] Temporarily Skip CUDA-IPC weight cache test (#64478)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`_
- **2026-11-05** [`2c5ef61e3e`](https://github.com/vllm-project/vllm/commit/2c5ef61e3e) [#65852](https://github.com/vllm-project/vllm/pull/65852)
  [Rust Frontend] Return FastAPI-style JSON 400 errors for bad dev route query strings (#65852)
  _Files: `rust/Cargo.lock`, `rust/src/server/Cargo.toml`, `rust/src/server/src/error.rs`, `rust/src/server/src/routes/cache.rs` _+6 more__
- **2026-11-05** [`e3bf8105a2`](https://github.com/vllm-project/vllm/commit/e3bf8105a2) [#65851](https://github.com/vllm-project/vllm/pull/65851)
  [Rust Frontend] Keep whitespace in HY tool-call argument names (#65851)
  _Files: `rust/src/parser/src/tool/hy.rs`_
- **2026-11-05** [`76a0ccc209`](https://github.com/vllm-project/vllm/commit/76a0ccc209) [#65623](https://github.com/vllm-project/vllm/pull/65623)
  [Rust Frontend] Pass assistant and tool content parts to HF templates like Python (#65623)
  _Files: `rust/src/chat/src/renderer/hf/mod.rs`_
- **2026-11-05** [`507a3f7f12`](https://github.com/vllm-project/vllm/commit/507a3f7f12) [#64562](https://github.com/vllm-project/vllm/pull/64562)
  [HiSparse][Core] Move HiSparse hot-page stride alignment into its spec (#64562)
  _Files: `vllm/v1/core/kv_cache_planning.py`, `vllm/v1/kv_cache_interface.py`_
- **2026-11-05** [`5a2633f63d`](https://github.com/vllm-project/vllm/commit/5a2633f63d) [#63606](https://github.com/vllm-project/vllm/pull/63606)
  [Bugfix][Frontend] Use the default template of multi-template processors (#63606)
  _Files: `tests/entrypoints/scale_out/render/test_launch_render.py`, `tests/renderers/test_hf.py`, `vllm/renderers/hf.py`_
- **2026-11-05** [`a2bcb5657a`](https://github.com/vllm-project/vllm/commit/a2bcb5657a) [#65806](https://github.com/vllm-project/vllm/pull/65806)
  [Bugfix][MiniMax-M3] Initialize the shard record in the indexer QKV layer (#65806)
  _Files: `tests/model_executor/model_loader/test_stacked_shard_tracking.py`, `vllm/model_executor/layers/linear.py`_
- **2026-11-05** [`52bc0c150a`](https://github.com/vllm-project/vllm/commit/52bc0c150a) [#65294](https://github.com/vllm-project/vllm/pull/65294)
  [Rust Frontend] Keep developer messages in place for templates without the role (#65294)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/chat/src/renderer/hf/developer.rs`, `rust/src/chat/src/renderer/hf/format.rs`, `rust/src/chat/src/renderer/hf/mod.rs` _+2 more__
- **2026-11-04** [`d7aa780f1a`](https://github.com/vllm-project/vllm/commit/d7aa780f1a) [#64782](https://github.com/vllm-project/vllm/pull/64782)
  [Bugfix][CUDA] Use CUDA memory accounting for integrated GPUs on WSL (#64782)
  _Files: `tests/utils_/test_mem_utils.py`, `tests/v1/worker/test_extensible_kv_cache.py`, `vllm/utils/mem_utils.py`_
- **2026-11-04** [`1706c7be7f`](https://github.com/vllm-project/vllm/commit/1706c7be7f) [#64656](https://github.com/vllm-project/vllm/pull/64656)
  [Test][UMBP] Restore a Mamba2 hybrid end to end through UMBP (#64656)
  _Files: `tests/v1/kv_connector/umbp_integration/test_mori_token_e2e.py`_
- **2026-11-04** [`7663a8c524`](https://github.com/vllm-project/vllm/commit/7663a8c524) [#65684](https://github.com/vllm-project/vllm/pull/65684)
  [Recipe] Add Kimi K3.1 Pro recipes (#65684)
  _Files: `recipes/models/moonshotai/Kimi-K3.1-Pro.yaml`_
- **2026-11-04** [`c126ebf159`](https://github.com/vllm-project/vllm/commit/c126ebf159) [#61463](https://github.com/vllm-project/vllm/pull/61463)
  [Bugfix][Kernel] Sync cluster before DSMEM stores in ll_bf16 split-K router GEMM (#61463)
  _Files: `vllm/model_executor/kernels/linear/cute_dsl/_ll_bf16_splitk.py`_
- **2026-11-04** [`b9877a8ca7`](https://github.com/vllm-project/vllm/commit/b9877a8ca7) [#65001](https://github.com/vllm-project/vllm/pull/65001)
  [Rust Frontend] Support --log-error-stack (#65001)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/server/src/config.rs` _+5 more__
- **2026-11-04** [`101269e80f`](https://github.com/vllm-project/vllm/commit/101269e80f) [#63752](https://github.com/vllm-project/vllm/pull/63752)
  [Bugfix][Model Loader] Reject stacked weights that received only some shards (#63752)
  _Files: `tests/model_executor/model_loader/test_stacked_shard_tracking.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/model_loader/default_loader.py`, `vllm/models/step5/nvidia/model.py`_
- **2026-11-04** [`5225a1f17f`](https://github.com/vllm-project/vllm/commit/5225a1f17f) [#64658](https://github.com/vllm-project/vllm/pull/64658)
  [Test][UMBP] Cover end-to-end restore while the embedded DRAM pool is evicting (#64658)
  _Files: `tests/v1/kv_connector/umbp_integration/test_mori_token_e2e.py`_
- **2026-11-04** [`caec40bce7`](https://github.com/vllm-project/vllm/commit/caec40bce7) [#65377](https://github.com/vllm-project/vllm/pull/65377)
  [Rust Frontend] Drop tool calls under tool_choice=none for split tool parsers (#65377)
  _Files: `rust/src/chat/src/output/default/mod.rs`_
- **2026-11-04** [`977186dd51`](https://github.com/vllm-project/vllm/commit/977186dd51) [#65372](https://github.com/vllm-project/vllm/pull/65372)
  [Rust Frontend] Accept FastAPI boolean spellings on dev route query parameters (#65372)
  _Files: `rust/src/server/src/routes/cache.rs`, `rust/src/server/src/routes/pause.rs`, `rust/src/server/src/routes/tests.rs`, `rust/src/server/src/routes/world_size.rs` _+1 more__
- **2026-11-04** [`e4d8b3596b`](https://github.com/vllm-project/vllm/commit/e4d8b3596b) [#65144](https://github.com/vllm-project/vllm/pull/65144)
  [Bugfix][Rust Frontend] Include error sources in HTTP 400 messages (#65144)
  _Files: `rust/src/server/src/error.rs`, `rust/src/server/src/lib.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-11-04** [`e940c1f380`](https://github.com/vllm-project/vllm/commit/e940c1f380) [#65528](https://github.com/vllm-project/vllm/pull/65528)
  [Spec Decode] Clean up AR speculator decode path (#65528)
  _Files: `tests/v1/worker/test_gpu_target_dependent_ar_speculator.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`, `vllm/v1/worker/gpu/spec_decode/standalone_ar/speculator.py`, `vllm/v1/worker/gpu/spec_decode/target_dependent_ar/speculator.py`_
- **2026-11-04** [`d3fb7166e0`](https://github.com/vllm-project/vllm/commit/d3fb7166e0) [#65274](https://github.com/vllm-project/vllm/pull/65274)
  [Bugfix] Step3 tool parser: coerce nullable and object/array parameters by schema (#65274)
  _Files: `tests/tool_parsers/test_step3_tool_parser.py`, `vllm/tool_parsers/step3_tool_parser.py`_
- **2026-11-03** [`1fc9d008eb`](https://github.com/vllm-project/vllm/commit/1fc9d008eb) [#64518](https://github.com/vllm-project/vllm/pull/64518)
  [Bugfix][Tool Parser] Keep raw text for string parameters with union/enum/$ref schemas (Muse, MiniCPM5, Poolside) (#64518)
  _Files: `rust/src/parser/src/schema.rs`, `rust/src/parser/src/unified/muse.rs`, `tests/tool_parsers/test_minicpm5xml_tool_parser.py`, `tests/tool_parsers/test_poolside_v1_tool_parser.py` _+6 more__
- **2026-11-03** [`71866b9a78`](https://github.com/vllm-project/vllm/commit/71866b9a78) [#65467](https://github.com/vllm-project/vllm/pull/65467)
  [Recipe] Kimi-K3: refresh B300 AgentX preset to InferenceX #4381 head (#65467)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-11-03** [`e5b2faeb5c`](https://github.com/vllm-project/vllm/commit/e5b2faeb5c) [#65457](https://github.com/vllm-project/vllm/pull/65457)
  [Bugfix] Keep the extensible tensor's PyCapsule_New prototype private (#65457)
  _Files: `tests/utils_/test_extensible_tensor.py`, `vllm/utils/extensible_tensor.py`_
- **2026-11-03** [`2173d7121f`](https://github.com/vllm-project/vllm/commit/2173d7121f) [#65174](https://github.com/vllm-project/vllm/pull/65174)
  [Bugfix][Kimi-VL] Set pad_token_id explicitly in KimiVLConfig (#65174)
  _Files: `vllm/transformers_utils/configs/kimi_vl.py`_
- **2026-11-03** [`66360a5cd0`](https://github.com/vllm-project/vllm/commit/66360a5cd0) [#65281](https://github.com/vllm-project/vllm/pull/65281)
  [Model Loader] Direct reload: lay the checkpoint out where a relocated weight now starts (#65281)
  _Files: `tests/model_executor/model_loader/test_direct_reload.py`, `vllm/model_executor/model_loader/reload/direct.py`_
- **2026-11-03** [`893d65b0a6`](https://github.com/vllm-project/vllm/commit/893d65b0a6) [#65153](https://github.com/vllm-project/vllm/pull/65153)
  [Bugfix][Step5] Size the KV block to the CSA tail ring (#65153)
  _Files: `tests/models/step5/test_csa_tail_ring_block_size.py`, `vllm/models/step5/common/csa_tail_ring.py`_
- **2026-11-03** [`82a48b7c1e`](https://github.com/vllm-project/vllm/commit/82a48b7c1e) [#65127](https://github.com/vllm-project/vllm/pull/65127)
  [Bugfix] Validate global model seed range (#65127)
  _Files: `tests/entrypoints/llm/test_prompt_validation.py`, `vllm/config/model.py`_
- **2026-11-03** [`c80f43a24c`](https://github.com/vllm-project/vllm/commit/c80f43a24c) [#65238](https://github.com/vllm-project/vllm/pull/65238)
  [CI/Build] Add batch-invariance auto-label rule (#65238)
  _Files: `.github/mergify.yml`, `.github/workflows/issue_autolabel.yml`_
- **2026-11-03** [`74ea8d37c2`](https://github.com/vllm-project/vllm/commit/74ea8d37c2) [#65041](https://github.com/vllm-project/vllm/pull/65041)
  [Bugfix][MRV2][Spec Decode] Keep P/D prompt tails on FULL graphs with adaptive verification (#65041)
  _Files: `tests/v1/cudagraph/test_cudagraph_manager.py`, `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/dp_utils.py` _+2 more__
- **2026-11-03** [`9cd2e98b59`](https://github.com/vllm-project/vllm/commit/9cd2e98b59) [#65060](https://github.com/vllm-project/vllm/pull/65060)
  [Bugfix][KV Connector] Fix KV role detection for MultiConnector with nested connectors (#65060)
  _Files: `tests/v1/kv_connector/unit/test_multi_connector.py`, `vllm/config/kv_transfer.py`_
- **2026-11-02** [`5c8ae7c74a`](https://github.com/vllm-project/vllm/commit/5c8ae7c74a) [#63974](https://github.com/vllm-project/vllm/pull/63974)
  [Bugfix][Rust Frontend] Match Python text-part joining for HF templates (#63974)
  _Files: `rust/src/chat/src/renderer/hf/mod.rs`_
- **2026-11-02** [`1b95bc6c6b`](https://github.com/vllm-project/vllm/commit/1b95bc6c6b) [#63901](https://github.com/vllm-project/vllm/pull/63901)
  [Rust Frontend][1/3] Map developer messages to system for templates without the developer role (#63901)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/chat/src/renderer/hf/mod.rs`, `rust/src/chat/src/renderer/hf/template.rs`_
- **2026-11-02** [`e8ec12c5ed`](https://github.com/vllm-project/vllm/commit/e8ec12c5ed) [#61219](https://github.com/vllm-project/vllm/pull/61219)
  [Bugfix][Spec Decode] V2 rejection sampler: return logprob_token_ids scores (#61219)
  _Files: `tests/v1/worker/test_gpu_batch_shard.py`, `tests/v1/worker/test_gpu_rejection_sampler_chunking.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/sample/sampler.py` _+1 more__

## Multimodal  (45 commits)

- **2026-11-09** [`32e0f4077b`](https://github.com/vllm-project/vllm/commit/32e0f4077b) [#66417](https://github.com/vllm-project/vllm/pull/66417)
  [Bugfix][Pooling] Keep CLIP and SigLIP special tokens for chat text embeddings (#66417)
  _Files: `examples/pooling/embed/vision_embedding_online.py`, `tests/entrypoints/pooling/embed/test_online_dual_encoder.py`, `vllm/transformers_utils/chat_templates/registry.py`, `vllm/transformers_utils/chat_templates/template_clip.jinja` _+1 more__
- **2026-11-09** [`68a62a2940`](https://github.com/vllm-project/vllm/commit/68a62a2940) [#65735](https://github.com/vllm-project/vllm/pull/65735)
  [Model] Add transcription to the Transformers modeling backend (#65735)
  _Files: `docs/models/supported_models.md`, `docs/serving/online_serving/speech_to_text.md`, `tests/entrypoints/speech_to_text/transcription/test_transcription_inter_chunk_spacing.py`, `tests/entrypoints/speech_to_text/transcription/test_transcription_validation.py` _+17 more__
- **2026-11-09** [`8db73f26c1`](https://github.com/vllm-project/vllm/commit/8db73f26c1) [#66117](https://github.com/vllm-project/vllm/pull/66117)
  [Bugfix][Frontend] Reject translation on models that cannot translate (#66117)
  _Files: `docs/serving/online_serving/speech_to_text.md`, `tests/entrypoints/speech_to_text/translation/test_translation_validation.py`, `vllm/entrypoints/speech_to_text/base/utils.py`, `vllm/model_executor/models/cohere_asr.py` _+7 more__
- **2026-11-09** [`9ee62c8c1e`](https://github.com/vllm-project/vllm/commit/9ee62c8c1e) [#66106](https://github.com/vllm-project/vllm/pull/66106)
  [Rust Frontend] Support tool_reference content parts (#66106)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/renderer/deepseek.rs`, `rust/src/chat/src/renderer/deepseek_v4/fixtures/tool_search_references.txt` _+14 more__
- **2026-11-09** [`821851eab0`](https://github.com/vllm-project/vllm/commit/821851eab0) [#66432](https://github.com/vllm-project/vllm/pull/66432)
  [Bugfix][Multimodal] Fill the Qwen2-VL video budget up to the context length (#66432)
  _Files: `docs/configuration/conserving_memory.md`, `tests/models/multimodal/generation/test_qwen2_5_vl.py`, `tests/models/multimodal/processing/test_qwen2_vl.py`, `vllm/model_executor/models/qwen2_vl.py`_
- **2026-11-08** [`d2c5f9ad5f`](https://github.com/vllm-project/vllm/commit/d2c5f9ad5f) [#65351](https://github.com/vllm-project/vllm/pull/65351)
  [Multimodal][Bugfix] Fix Step3-VL encoder output aliasing and guard shared CUDA graph capture buffers (#65351)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/step3_vl.py` _+2 more__
- **2026-11-08** [`325bc507bc`](https://github.com/vllm-project/vllm/commit/325bc507bc) [#65227](https://github.com/vllm-project/vllm/pull/65227)
  [Perf][Multimodal] Encoder CUDA graphs: one replay per batch, finer grid up to one max budget (#65227)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/config/compilation.py`, `vllm/model_executor/models/deepseek_vl2.py` _+5 more__
- **2026-11-08** [`7a90549f7e`](https://github.com/vllm-project/vllm/commit/7a90549f7e) [#66358](https://github.com/vllm-project/vllm/pull/66358)
  [CI] Fix ruff on main after dots_ocr test change (#66358)
  _Files: `tests/models/multimodal/generation/test_common.py`_
- **2026-11-08** [`b65f945008`](https://github.com/vllm-project/vllm/commit/b65f945008) [#64543](https://github.com/vllm-project/vllm/pull/64543)
  [Bugfix][Model] Fix dots_ocr vision tower QKV split for TP > 1 (#64543)
  _Files: `tests/models/multimodal/generation/test_common.py`, `vllm/model_executor/models/dots_ocr.py`_
- **2026-11-08** [`5efb24d542`](https://github.com/vllm-project/vllm/commit/5efb24d542) [#57810](https://github.com/vllm-project/vllm/pull/57810)
  [Core][KVConnector] Keep the offloaded KV tier across pause/sleep (#57810)
  _Files: `docs/features/sleep_mode.md`, `docs/training/async_rl.md`, `rust/Cargo.lock`, `rust/proto/Cargo.toml` _+20 more__
- **2026-11-08** [`ebc97ad8d0`](https://github.com/vllm-project/vllm/commit/ebc97ad8d0) [#65084](https://github.com/vllm-project/vllm/pull/65084)
  [Multimodal] Refactor encoder cuda graph to support share graph buffer reuse (#65084)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/v1/worker/encoder_cudagraph.py`_
- **2026-11-06** [`0bebae99a3`](https://github.com/vllm-project/vllm/commit/0bebae99a3) [#60308](https://github.com/vllm-project/vllm/pull/60308)
  [Bugfix][Frontend] Return 400 for images rejected by Pillow's bomb check (#60308)
  _Files: `tests/multimodal/media/test_image.py`, `vllm/multimodal/media/image.py`_
- **2026-11-06** [`ff05baf8ba`](https://github.com/vllm-project/vllm/commit/ff05baf8ba) [#66028](https://github.com/vllm-project/vllm/pull/66028)
  [Rust Frontend] Kimi K3.1 chat renderer (Kimi K3.1 split 2/5) (#66028)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/multimodal/models.rs` _+7 more__
- **2026-11-06** [`49c3307392`](https://github.com/vllm-project/vllm/commit/49c3307392) [#65808](https://github.com/vllm-project/vllm/pull/65808)
  [Bugfix] Fix DP ViT all-gather dtype mismatch when the first parameter is fp32 (#65808)
  _Files: `vllm/model_executor/models/vision.py`_
- **2026-11-06** [`11199bcb78`](https://github.com/vllm-project/vllm/commit/11199bcb78) [#65828](https://github.com/vllm-project/vllm/pull/65828)
  [Model] Add LFM3-Audio (#65828)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_lfm3_audio.py`, `tests/models/registry.py`, `vllm/model_executor/models/lfm3_audio.py` _+6 more__
- **2026-11-06** [`3012587f04`](https://github.com/vllm-project/vllm/commit/3012587f04) [#65620](https://github.com/vllm-project/vllm/pull/65620)
  [Doc] Document multimodal requirements for the Transformers modeling … (#65620)
  _Files: `docs/models/supported_models.md`_
- **2026-11-06** [`2c8ca1b381`](https://github.com/vllm-project/vllm/commit/2c8ca1b381) [#60978](https://github.com/vllm-project/vllm/pull/60978)
  [Bugfix][Pooling] Use embedding_dim for pooling output size (#60978)
  _Files: `tests/models/multimodal/pooling/test_embedding_gemma2.py`, `vllm/config/model.py`_
- **2026-11-06** [`9db59643e4`](https://github.com/vllm-project/vllm/commit/9db59643e4) [#64606](https://github.com/vllm-project/vllm/pull/64606)
  [CI] Enroll 8 jobs in automatic sharding (#64606)
  _Files: `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-11-06** [`3fe0d44219`](https://github.com/vllm-project/vllm/commit/3fe0d44219) [#66079](https://github.com/vllm-project/vllm/pull/66079)
  [CI][Bugfix] Fix EmbeddingGemma2 encoder contract test after Gemma-4 DP encoder (#66079)
  _Files: `tests/models/multimodal/pooling/test_embedding_gemma2.py`_
- **2026-11-06** [`6eef078ce8`](https://github.com/vllm-project/vllm/commit/6eef078ce8) [#65363](https://github.com/vllm-project/vllm/pull/65363)
  [Bugfix][Multimodal] Handle media cache eviction during reads (#65363)
  _Files: `docs/features/multimodal_inputs.md`, `tests/multimodal/media/test_connector.py`, `vllm/multimodal/media/connector.py`_
- **2026-11-06** [`6c15c6cc53`](https://github.com/vllm-project/vllm/commit/6c15c6cc53) [#53369](https://github.com/vllm-project/vllm/pull/53369)
  [Bugfix][Frontend] Match default MM LoRA for OpenAI input_audio parts (#53369)
  _Files: `tests/entrypoints/serve/lora/test_serving_models.py`, `vllm/entrypoints/serve/engine/serving.py`_
- **2026-11-06** [`de05fd1db9`](https://github.com/vllm-project/vllm/commit/de05fd1db9) [#60314](https://github.com/vllm-project/vllm/pull/60314)
  [Model] Support data-parallel multimodal encoder for Gemma-4 (#60314)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`, `vllm/model_executor/models/embedding_gemma2.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-11-06** [`9151e80b23`](https://github.com/vllm-project/vllm/commit/9151e80b23) [#66029](https://github.com/vllm-project/vllm/pull/66029)
  [XPU] increase gpu_memory_utilization for test_granite4_vision.py (#66029)
  _Files: `tests/models/multimodal/generation/test_granite4_vision.py`_
- **2026-11-06** [`fce61a05a7`](https://github.com/vllm-project/vllm/commit/fce61a05a7) [#64885](https://github.com/vllm-project/vllm/pull/64885)
  [Bugfix][Pooling] Enable Matryoshka dimensions for EmbeddingGemma 2 (#64885)
  _Files: `tests/models/multimodal/pooling/test_embedding_gemma2.py`, `vllm/model_executor/models/config.py`_
- **2026-11-05** [`ef8870b09f`](https://github.com/vllm-project/vllm/commit/ef8870b09f) [#65761](https://github.com/vllm-project/vllm/pull/65761)
  [Bugfix][Multimodal] Encoder CUDA graph: cap each graph's frame slots at its token budget (#65761)
  _Files: `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/v1/worker/encoder_cudagraph.py`_
- **2026-11-05** [`30cff7b177`](https://github.com/vllm-project/vllm/commit/30cff7b177) [#65442](https://github.com/vllm-project/vllm/pull/65442)
  [CI][Test] Skip unavailable models before spawning a test process (#65442)
  _Files: `tests/models/multimodal/processing/test_tensor_schema.py`, `tests/models/test_initialization.py`, `tests/models/utils.py`_
- **2026-11-05** [`3eb8a5b166`](https://github.com/vllm-project/vllm/commit/3eb8a5b166) [#65875](https://github.com/vllm-project/vllm/pull/65875)
  [Bugfix][CI] Fix duplicate max_num_seqs in Llama Nemotron VL pooling test (#65875)
  _Files: `tests/models/multimodal/pooling/test_llama_nemotron_vl.py`_
- **2026-11-05** [`c436239f8c`](https://github.com/vllm-project/vllm/commit/c436239f8c) [#65776](https://github.com/vllm-project/vllm/pull/65776)
  [CI Failure] Move Multimodal Models (Extended Pooling) to h200_35gb (#65776)
  _Files: `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-11-05** [`d8588b71ff`](https://github.com/vllm-project/vllm/commit/d8588b71ff) [#65805](https://github.com/vllm-project/vllm/pull/65805)
  [XPU] skipp unsupported test cases in CI (#65805)
  _Files: `.buildkite/intel_jobs/entrypoints_intel.yaml`, `.buildkite/intel_jobs/models_multimodal_intel.yaml`_
- **2026-11-05** [`92b1573ecd`](https://github.com/vllm-project/vllm/commit/92b1573ecd) [#65412](https://github.com/vllm-project/vllm/pull/65412)
  [Bugfix] Granite4Vision: strip padding tiles for list pixel_values (#65412)
  _Files: `tests/models/multimodal/generation/test_granite4_vision.py`, `vllm/model_executor/models/granite4_vision.py`_
- **2026-11-05** [`fd75a7a920`](https://github.com/vllm-project/vllm/commit/fd75a7a920) [#62702](https://github.com/vllm-project/vllm/pull/62702)
  [Perf][Core] Keep prompt token ids as int32 buffers (#62702)
  _Files: `rust/src/chat/tests/chat.rs`, `rust/src/engine-core-client/examples/external_engine_logprobs.rs`, `rust/src/engine-core-client/src/prompt_block_hasher.rs`, `rust/src/engine-core-client/src/protocol/request.rs` _+50 more__
- **2026-11-05** [`495c61cfd9`](https://github.com/vllm-project/vllm/commit/495c61cfd9) [#65577](https://github.com/vllm-project/vllm/pull/65577)
  [MM] Support mm_device_do_normalize for Gemma 4 (#65577)
  _Files: `docs/design/mm_processing.md`, `tests/models/multimodal/generation_ppl_test/gemma.py`, `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/diffusion_gemma.py` _+3 more__
- **2026-11-04** [`9b173af5a9`](https://github.com/vllm-project/vllm/commit/9b173af5a9) [#65234](https://github.com/vllm-project/vllm/pull/65234)
  [CI] Shard Multimodal Models (Extended Generation 1) automatically, with spawned engines (#65234)
  _Files: `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-11-04** [`947bd30e0b`](https://github.com/vllm-project/vllm/commit/947bd30e0b) [#65399](https://github.com/vllm-project/vllm/pull/65399)
  [Bugfix][Scheduler] Respect disabled chunked prefill for multimodal requests (#65399)
  _Files: `tests/models/multimodal/pooling/test_llama_nemotron_vl.py`, `tests/v1/core/test_scheduler.py`, `vllm/config/scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-11-04** [`6ba10507e1`](https://github.com/vllm-project/vllm/commit/6ba10507e1) [#65689](https://github.com/vllm-project/vllm/pull/65689)
  [Bugfix][Multimodal] Don't validate model-built dummy inputs against mm limits (#65689)
  _Files: `vllm/model_executor/models/kimi_audio.py`, `vllm/model_executor/models/moss_transcribe_diarize.py`, `vllm/model_executor/models/pixtral.py`, `vllm/model_executor/models/voxtral.py`_
- **2026-11-04** [`56dc7b70ce`](https://github.com/vllm-project/vllm/commit/56dc7b70ce) [#65688](https://github.com/vllm-project/vllm/pull/65688)
  [Recipe] Kimi-K3.1-Pro: pin Docker images, drop pip, add Rubin VR200 (#65688)
  _Files: `recipes/models/moonshotai/Kimi-K3.1-Pro.yaml`_
- **2026-11-04** [`802d4b8603`](https://github.com/vllm-project/vllm/commit/802d4b8603) [#65579](https://github.com/vllm-project/vllm/pull/65579)
  [Bugfix][Multimodal] Fix tensor conversion in audio parsing and hashing (#65579)
  _Files: `docs/features/multimodal_inputs.md`, `tests/models/multimodal/generation/test_whisper.py`, `tests/multimodal/test_parse.py`, `vllm/multimodal/hasher.py` _+1 more__
- **2026-11-04** [`349b21487a`](https://github.com/vllm-project/vllm/commit/349b21487a) [#65441](https://github.com/vllm-project/vllm/pull/65441)
  [CI][Model] Fill the model info cache once in the model init and tensor schema tests (#65441)
  _Files: `tests/models/multimodal/processing/test_tensor_schema.py`, `tests/models/test_initialization.py`, `tests/models/test_registry.py`, `vllm/model_executor/models/registry.py`_
- **2026-11-04** [`34d5de18cd`](https://github.com/vllm-project/vllm/commit/34d5de18cd) [#64028](https://github.com/vllm-project/vllm/pull/64028)
  [CI/Build] Publish nightly EFA image to DockerHub (#64028)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/docker-build-metadata-args.sh`, `docs/contributing/dockerfile/dockerfile.md`, `tests/tools/test_docker_build_metadata_args.py`_
- **2026-11-03** [`2142c95e67`](https://github.com/vllm-project/vllm/commit/2142c95e67) [#56277](https://github.com/vllm-project/vllm/pull/56277)
  [MM] Mistral vision Encoder CG support  (#56277)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `tests/models/multimodal/generation/test_pixtral.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py` _+3 more__
- **2026-11-03** [`65a904538d`](https://github.com/vllm-project/vllm/commit/65a904538d) [#65271](https://github.com/vllm-project/vllm/pull/65271)
  [Bugfix][Scheduler] Don't split a multimodal item when a prefix cache hit ends inside it (#65271)
  _Files: `tests/models/multimodal/generation/test_mm_prefix_lm.py`, `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-11-03** [`0eb619dc52`](https://github.com/vllm-project/vllm/commit/0eb619dc52) [#62097](https://github.com/vllm-project/vllm/pull/62097)
  [Bugfix][LoRA] Account for CLIP CLS rows in LLaVA-NeXT-Video tower mappings (#62097)
  _Files: `tests/models/multimodal/processing/test_llava_next_video.py`, `vllm/model_executor/models/llava_next_video.py`_
- **2026-11-03** [`1eec157dcd`](https://github.com/vllm-project/vllm/commit/1eec157dcd) [#64487](https://github.com/vllm-project/vllm/pull/64487)
  [MM] Support mm_device_do_normalize for gemma3. (#64487)
  _Files: `docs/design/mm_processing.md`, `tests/model_executor/layers/test_mm_input_norm.py`, `tests/models/multimodal/generation_ppl_test/gemma.py`, `tests/models/multimodal/generation_ppl_test/ppl_utils.py` _+4 more__
- **2026-11-03** [`9a519c0585`](https://github.com/vllm-project/vllm/commit/9a519c0585) [#65226](https://github.com/vllm-project/vllm/pull/65226)
  [Bugfix][Multimodal] Pad MiniMax-M3 encoder graph cu_seqlens with zero-length sequences (#65226)
  _Files: `vllm/models/minimax_m3/common/encoder_cudagraph.py`_
- **2026-11-02** [`24d7bc9aab`](https://github.com/vllm-project/vllm/commit/24d7bc9aab) [#64594](https://github.com/vllm-project/vllm/pull/64594)
  [CI] Enroll the remaining Models (basic, multimodal, language) jobs in automatic sharding (22 jobs) (#64594)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_language.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_

## Serving / API  (43 commits)

- **2026-11-09** [`0ee57d457f`](https://github.com/vllm-project/vllm/commit/0ee57d457f) [#66403](https://github.com/vllm-project/vllm/pull/66403)
  [Bugfix][Frontend] Render messages for return_prompt_text with reused prompt token ids (#66403)
  _Files: `docs/features/disagg_prefill.md`, `tests/entrypoints/openai/chat_completion/test_chat_completion.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/renderers/online_renderer.py`_
- **2026-11-09** [`ded03c9db5`](https://github.com/vllm-project/vllm/commit/ded03c9db5) [#66478](https://github.com/vllm-project/vllm/pull/66478)
  [Frontend] Default --enable-scale-out to VLLM_SERVER_DEV_MODE (#66478)
  _Files: `docs/serving/online_serving/README.md`, `docs/serving/online_serving/token_in_token_out.md`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+3 more__
- **2026-11-09** [`846767191e`](https://github.com/vllm-project/vllm/commit/846767191e) [#66107](https://github.com/vllm-project/vllm/pull/66107)
  [Rust Frontend] Accept `spaces_between_special_tokens` as a no-op (#66107)
  _Files: `rust/src/server/src/routes/openai/chat_completions/types.rs`, `rust/src/server/src/routes/openai/chat_completions/validate.rs`, `rust/src/server/src/routes/openai/completions/types.rs`, `rust/src/server/src/routes/openai/completions/validate.rs` _+3 more__
- **2026-11-09** [`e0aef07c01`](https://github.com/vllm-project/vllm/commit/e0aef07c01) [#66104](https://github.com/vllm-project/vllm/pull/66104)
  [Rust Frontend] Export vllm:request_render_duration_seconds (#66104)
  _Files: `rust/Cargo.lock`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/lib.rs`, `rust/src/metrics/src/lib.rs` _+6 more__
- **2026-11-09** [`eec1403877`](https://github.com/vllm-project/vllm/commit/eec1403877) [#64041](https://github.com/vllm-project/vllm/pull/64041)
  [Bugfix] Report reasoning and cached tokens in chat derender usage (#64041)
  _Files: `docs/serving/online_serving/derenderer.md`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_parity.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py` _+2 more__
- **2026-11-09** [`343b5a56a8`](https://github.com/vllm-project/vllm/commit/343b5a56a8) [#66481](https://github.com/vllm-project/vllm/pull/66481)
  [Frontend] Mark disabled scale-out routes in the startup route log (#66481)
  _Files: `vllm/entrypoints/launchers/launcher.py`, `vllm/entrypoints/launchers/utils/constants.py`, `vllm/entrypoints/scale_out/factories.py`_
- **2026-11-09** [`518dc3c998`](https://github.com/vllm-project/vllm/commit/518dc3c998) [#60274](https://github.com/vllm-project/vllm/pull/60274)
  [Rust Frontend] support --enable-force-include-usage (#60274)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/server/src/config.rs` _+3 more__
- **2026-11-08** [`0915f490c4`](https://github.com/vllm-project/vllm/commit/0915f490c4) [#65866](https://github.com/vllm-project/vllm/pull/65866)
  [Bugfix] Move model inspection RPC out of LLM.__repr__ (#65866)
  _Files: `docs/serving/offline_inference.md`, `tests/entrypoints/llm/test_collective_rpc.py`, `vllm/entrypoints/llm.py`_
- **2026-11-08** [`b20931448f`](https://github.com/vllm-project/vllm/commit/b20931448f) [#65168](https://github.com/vllm-project/vllm/pull/65168)
  [Fast start] Pluggable shared stores for daemon warmup caches (#65168)
  _Files: `.buildkite/test_areas/distributed.yaml`, `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/entrypoints/cli/preload.py` _+3 more__
- **2026-11-06** [`5a92788a1b`](https://github.com/vllm-project/vllm/commit/5a92788a1b) [#64781](https://github.com/vllm-project/vllm/pull/64781)
  [Bugfix] Read generate usage.prompt_tokens in non-streaming derender (#64781)
  _Files: `tests/entrypoints/scale_out/derender/test_derender.py`, `vllm/entrypoints/scale_out/derender/serving.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`, `vllm/renderers/online_derenderer.py`_
- **2026-11-06** [`fd77011424`](https://github.com/vllm-project/vllm/commit/fd77011424) [#65697](https://github.com/vllm-project/vllm/pull/65697)
  [Bugfix][Frontend] Count prompts over max_model_len in Anthropic count_tokens (#65697)
  _Files: `tests/entrypoints/anthropic/test_messages.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-11-06** [`4c40d683c3`](https://github.com/vllm-project/vllm/commit/4c40d683c3) [#63173](https://github.com/vllm-project/vllm/pull/63173)
  [Bugfix][Frontend] Honor token ID logprob overrides on derender paths (#63173)
  _Files: `docs/serving/online_serving/derenderer.md`, `docs/serving/online_serving/token_in_token_out.md`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py` _+10 more__
- **2026-11-06** [`8d5b5f1063`](https://github.com/vllm-project/vllm/commit/8d5b5f1063) [#52875](https://github.com/vllm-project/vllm/pull/52875)
  [Perf][Frontend] Render plain completion stream deltas from a template (#52875)
  _Files: `tests/entrypoints/openai/completion/test_completion_error.py`, `tests/entrypoints/openai/completion/test_stream_frame_template.py`, `vllm/entrypoints/openai/completion/serving.py`_
- **2026-11-05** [`beb72da79f`](https://github.com/vllm-project/vllm/commit/beb72da79f) [#65954](https://github.com/vllm-project/vllm/pull/65954)
  [Bugfix][Frontend] Accept Anthropic thinking.type=between_tools on the Messages API (#65954)
  _Files: `docs/features/reasoning_outputs.md`, `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/anthropic/serving.py` _+1 more__
- **2026-11-05** [`14d147a7a0`](https://github.com/vllm-project/vllm/commit/14d147a7a0) [#65867](https://github.com/vllm-project/vllm/pull/65867)
  [Perf][Frontend] Write run-batch JSON responses without parsing them back (#65867)
  _Files: `tests/entrypoints/launchers/test_run_batch.py`, `vllm/entrypoints/launchers/run_batch.py`_
- **2026-11-05** [`85a4d15d62`](https://github.com/vllm-project/vllm/commit/85a4d15d62) [#65854](https://github.com/vllm-project/vllm/pull/65854)
  [Rust Frontend] Accept an empty tools array like OpenAI (#65854)
  _Files: `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/openai/chat_completions/validate.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-11-05** [`ad451c2289`](https://github.com/vllm-project/vllm/commit/ad451c2289) [#65863](https://github.com/vllm-project/vllm/pull/65863)
  [Rust Frontend] Echo prompt-cache and safety_identifier fields in Responses (#65863)
  _Files: `rust/src/server/src/routes/openai/responses/convert.rs`, `rust/src/server/src/routes/openai/responses/types.rs`, `rust/src/server/src/routes/openai/responses/validate.rs`, `rust/src/server/src/routes/tests/responses.rs`_
- **2026-11-05** [`29f7e70132`](https://github.com/vllm-project/vllm/commit/29f7e70132) [#65853](https://github.com/vllm-project/vllm/pull/65853)
  [Rust Frontend] Support namespace tools in the Responses API (#65853)
  _Files: `rust/src/server/src/routes/openai/responses.rs`, `rust/src/server/src/routes/openai/responses/convert.rs`, `rust/src/server/src/routes/openai/responses/streaming.rs`, `rust/src/server/src/routes/openai/responses/tools.rs` _+2 more__
- **2026-11-05** [`273c0e514b`](https://github.com/vllm-project/vllm/commit/273c0e514b) [#65624](https://github.com/vllm-project/vllm/pull/65624)
  [Rust Frontend] Support echo with truncate_prompt_tokens (#65624)
  _Files: `rust/src/server/src/routes/openai/chat_completions/validate.rs`, `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/completions/convert.rs`, `rust/src/server/src/routes/openai/completions/validate.rs` _+3 more__
- **2026-11-05** [`29e0386ebd`](https://github.com/vllm-project/vllm/commit/29e0386ebd) [#65621](https://github.com/vllm-project/vllm/pull/65621)
  [Rust Frontend] Accept refusal content parts in assistant messages (#65621)
  _Files: `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/openai/utils/types.rs`_
- **2026-11-05** [`a981cad6cb`](https://github.com/vllm-project/vllm/commit/a981cad6cb) [#65625](https://github.com/vllm-project/vllm/pull/65625)
  [Rust Frontend] Support n > 1 choices (#65625)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/llm/src/lib.rs` _+18 more__
- **2026-11-04** [`e4991c1feb`](https://github.com/vllm-project/vllm/commit/e4991c1feb) [#64935](https://github.com/vllm-project/vllm/pull/64935)
  [Bugfix][Frontend] Report reasoning tokens in batched chat completions (#64935)
  _Files: `docs/serving/online_serving/openai_compatible_server.md`, `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `tests/entrypoints/openai/chat_completion/test_include_reasoning.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py`_
- **2026-11-04** [`d656b8fa5f`](https://github.com/vllm-project/vllm/commit/d656b8fa5f) [#64471](https://github.com/vllm-project/vllm/pull/64471)
  [Bugfix][Rust Frontend] Accept empty message content like the Python frontend (#64471)
  _Files: `rust/src/server/src/routes/openai/utils/types.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-11-04** [`5611db5969`](https://github.com/vllm-project/vllm/commit/5611db5969) [#64492](https://github.com/vllm-project/vllm/pull/64492)
  [Bugfix][Rust Frontend] Accept assistant turns without content like Python (#64492)
  _Files: `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-11-04** [`e0768d8731`](https://github.com/vllm-project/vllm/commit/e0768d8731) [#63189](https://github.com/vllm-project/vllm/pull/63189)
  [Bugfix][Frontend] Handle buffered JSON embedding responses in run-batch (#63189)
  _Files: `docs/cli/README.md`, `tests/entrypoints/launchers/test_run_batch.py`, `vllm/entrypoints/launchers/run_batch.py`_
- **2026-11-04** [`44d9f92e05`](https://github.com/vllm-project/vllm/commit/44d9f92e05) [#65547](https://github.com/vllm-project/vllm/pull/65547)
  [Bugfix][Frontend] Accept an empty tools array like OpenAI (#65547)
  _Files: `tests/tool_use/test_chat_completion_request_validations.py`, `tests/tool_use/test_chat_completions.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/serve/tokenize/protocol.py`_
- **2026-11-04** [`e517bc1347`](https://github.com/vllm-project/vllm/commit/e517bc1347) [#65374](https://github.com/vllm-project/vllm/pull/65374)
  [Rust Frontend] Omit unset usage prompt_tokens_details and message annotations like Python (#65374)
  _Files: `rust/src/server/src/routes/openai/chat_completions/types.rs`, `rust/src/server/src/routes/openai/utils/types.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-11-04** [`af261bab7f`](https://github.com/vllm-project/vllm/commit/af261bab7f) [#59736](https://github.com/vllm-project/vllm/pull/59736)
  [Bugfix][Rust Frontend] Fail token-less streams in vllm-bench openai-chat (#59736)
  _Files: `rust/src/bench/src/backends/mod.rs`, `rust/src/bench/src/backends/openai_chat.rs`, `rust/src/bench/src/backends/openai_completions.rs`_
- **2026-11-03** [`c3fd4ff448`](https://github.com/vllm-project/vllm/commit/c3fd4ff448) [#65459](https://github.com/vllm-project/vllm/pull/65459)
  [Bugfix][Frontend] Support min_tokens in the Anthropic Messages API (#65459)
  _Files: `tests/entrypoints/anthropic/test_messages.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-11-03** [`4da6e71556`](https://github.com/vllm-project/vllm/commit/4da6e71556) [#65423](https://github.com/vllm-project/vllm/pull/65423)
  [Perf][Startup] Keep openai out of import vllm.config via lazy ToolServer import (#65423)
  _Files: `tests/standalone_tests/lazy_imports.py`, `vllm/reasoning/abs_reasoning_parsers.py`_
- **2026-11-03** [`d8a13402fe`](https://github.com/vllm-project/vllm/commit/d8a13402fe) [#65389](https://github.com/vllm-project/vllm/pull/65389)
  [Bugfix] Keep default max_tokens in rendered sampling_params (#65389)
  _Files: `tests/entrypoints/scale_out/render/test_render.py`, `tests/entrypoints/scale_out/token_in_token_out/test_protocol.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`_
- **2026-11-03** [`6b3488cc97`](https://github.com/vllm-project/vllm/commit/6b3488cc97) [#63434](https://github.com/vllm-project/vllm/pull/63434)
  [Bugfix][Frontend] Pass the caller's prompt_token_ids to the chat derender parser (#63434)
  _Files: `docs/serving/online_serving/derenderer.md`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/parser/test_response_template.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py` _+1 more__
- **2026-11-03** [`eb409c9aa2`](https://github.com/vllm-project/vllm/commit/eb409c9aa2) [#63902](https://github.com/vllm-project/vllm/pull/63902)
  [Rust Frontend] Add the stateless Responses API (streaming and non-streaming) (#63902)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/stream.rs`, `rust/src/server/src/middleware/offload.rs`, `rust/src/server/src/routes.rs` _+13 more__
- **2026-11-03** [`a801d9ea3a`](https://github.com/vllm-project/vllm/commit/a801d9ea3a) [#60177](https://github.com/vllm-project/vllm/pull/60177)
  [Bugfix][Benchmark] Preserve Rust SSE payloads across chunks and comments (#60177)
  _Files: `rust/src/bench/src/backends/openai_chat.rs`, `rust/src/bench/src/backends/openai_completions.rs`, `rust/src/bench/src/backends/streaming.rs`_
- **2026-11-03** [`aa59a1967b`](https://github.com/vllm-project/vllm/commit/aa59a1967b) [#65036](https://github.com/vllm-project/vllm/pull/65036)
  [Bugfix][Frontend] Report the prompt cache split in the first streamed usage (#65036)
  _Files: `tests/entrypoints/anthropic/test_messages.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/entrypoints/openai/chat_completion/serving.py`_
- **2026-11-03** [`e11a5ada53`](https://github.com/vllm-project/vllm/commit/e11a5ada53) [#64626](https://github.com/vllm-project/vllm/pull/64626)
  [Bugfix][Rust Frontend] Don't count content-free chunks as streamed outputs in vllm-bench chat (#64626)
  _Files: `rust/src/bench/src/backends/mod.rs`, `rust/src/bench/src/backends/openai_chat.rs`_
- **2026-11-03** [`20f0890b60`](https://github.com/vllm-project/vllm/commit/20f0890b60) [#64728](https://github.com/vllm-project/vllm/pull/64728)
  [Bugfix] Stop offline beam search at the context limit (#64728)
  _Files: `docs/models/generative_models.md`, `tests/samplers/test_beam_search.py`, `tests/samplers/test_beam_search_online.py`, `vllm/entrypoints/generate/beam_search/offline.py`_
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

## Models  (39 commits)

- **2026-11-09** [`8581ff0667`](https://github.com/vllm-project/vllm/commit/8581ff0667) [#66559](https://github.com/vllm-project/vllm/pull/66559)
  [Transformers backend] Migrate Phi3 (#66559)
  _Files: `docs/models/supported_models.md`, `tests/models/transformers/test_dynamic_rope.py`, `vllm/model_executor/models/phi3.py`, `vllm/model_executor/models/phi4siglip.py` _+3 more__
- **2026-11-09** [`7c35455091`](https://github.com/vllm-project/vllm/commit/7c35455091) [#66545](https://github.com/vllm-project/vllm/pull/66545)
  [Transformers backend] Support batch-sharded sampling (#66545)
  _Files: `tests/v1/e2e/general/test_sharded_sampling.py`, `vllm/model_executor/models/transformers/causal.py`_
- **2026-11-09** [`b389f03ff6`](https://github.com/vllm-project/vllm/commit/b389f03ff6) [#65524](https://github.com/vllm-project/vllm/pull/65524)
  [Perf][DSv4.1] Replay one row for far prefill chunks (#65524)
  _Files: `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/config/compilation.py`, `vllm/models/deepseek_v41/nvidia/decoder_replay_cudagraph.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`_
- **2026-11-09** [`49bfed4bdb`](https://github.com/vllm-project/vllm/commit/49bfed4bdb) [#66103](https://github.com/vllm-project/vllm/pull/66103)
  [Rust Frontend] Join text parts in the renderer for DeepSeek V3.2 and /v1/responses (#66103)
  _Files: `rust/src/chat/src/renderer/deepseek_v32/encoding.rs`, `rust/src/chat/src/renderer/deepseek_v32/tests.rs`, `rust/src/server/src/routes/openai/responses/convert.rs`_
- **2026-11-09** [`3ac8ba9faa`](https://github.com/vllm-project/vllm/commit/3ac8ba9faa) [#65949](https://github.com/vllm-project/vllm/pull/65949)
  [Bugfix] Map compressed-tensors KV-cache scale names for GPT-J (#65949)
  _Files: `tests/model_executor/test_weight_utils.py`, `vllm/model_executor/models/gpt_j.py`_
- **2026-11-09** [`c7cda53c85`](https://github.com/vllm-project/vllm/commit/c7cda53c85) [#66238](https://github.com/vllm-project/vllm/pull/66238)
  [CPU][recipes] Add Qwen3-VL-4B-Instruct support for Intel Xeon 6 (#66238)
  _Files: `recipes/models/Qwen/Qwen3-VL-4B-Instruct.yaml`_
- **2026-11-09** [`000a53c272`](https://github.com/vllm-project/vllm/commit/000a53c272) [#66461](https://github.com/vllm-project/vllm/pull/66461)
  [Bugfix][Qwen4Exp] Exclude the HC padding shard from the loaded-shard check (#66461)
  _Files: `tests/models/qwen4_exp/test_hc_ops.py`, `vllm/models/qwen4_exp/nvidia/hyperconnection.py`_
- **2026-11-08** [`34b780fe66`](https://github.com/vllm-project/vllm/commit/34b780fe66) [#66393](https://github.com/vllm-project/vllm/pull/66393)
  [Transformers backend] Migrate Gemma and StableLM (#66393)
  _Files: `docs/models/supported_models.md`, `tests/models/language/generation/test_gemma.py`, `vllm/model_executor/models/gemma.py`, `vllm/model_executor/models/paligemma.py` _+3 more__
- **2026-11-08** [`794c9608f5`](https://github.com/vllm-project/vllm/commit/794c9608f5) [#66388](https://github.com/vllm-project/vllm/pull/66388)
  [Model] Use the upstream config for MOSS-Transcribe-Diarize (#66388)
  _Files: `vllm/transformers_utils/config.py`, `vllm/transformers_utils/configs/__init__.py`, `vllm/transformers_utils/configs/moss_transcribe_diarize.py`_
- **2026-11-06** [`9c345f0951`](https://github.com/vllm-project/vllm/commit/9c345f0951) [#66030](https://github.com/vllm-project/vllm/pull/66030)
  [Model] Kimi K3.1: model files and NVIDIA specialized decode (Kimi K3.1 split 1/5) (#66030)
- **2026-11-06** [`8bb1147817`](https://github.com/vllm-project/vllm/commit/8bb1147817) [#65874](https://github.com/vllm-project/vllm/pull/65874)
  [Kernel][Perf] Fused GDN MTP: Support DSpark K=8 and use idle SMs at small batch sizes (#65874)
  _Files: `csrc/gdn/fused_gdn_decode_kernel.cu`, `tests/kernels/fla/test_fused_gdn_post_conv.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-11-06** [`a9961c2c3e`](https://github.com/vllm-project/vllm/commit/a9961c2c3e) [#66064](https://github.com/vllm-project/vllm/pull/66064)
  [Perf][GDN] Fuse prefill state gather/scatter with the shared Triton kernels (#66064)
  _Files: `tests/kernels/mamba/test_gather_scatter_states.py`, `tests/model_executor/test_qwen_triton_warmup.py`, `tests/models/kimi_k3/test_kda.py`, `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` _+3 more__
- **2026-11-06** [`3899755028`](https://github.com/vllm-project/vllm/commit/3899755028) [#65827](https://github.com/vllm-project/vllm/pull/65827)
  [Model] Add LFM3-VL (#65827)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/lfm3_vl.py` _+6 more__
- **2026-11-06** [`1a2bb39cd7`](https://github.com/vllm-project/vllm/commit/1a2bb39cd7) [#65989](https://github.com/vllm-project/vllm/pull/65989)
  [Bugfix][Gemma4] Read per-layer embeddings on later pipeline stages (#65989)
  _Files: `tests/models/language/generation/test_gemma.py`, `vllm/model_executor/models/gemma4.py`_
- **2026-11-06** [`c96e5f60bb`](https://github.com/vllm-project/vllm/commit/c96e5f60bb) [#65826](https://github.com/vllm-project/vllm/pull/65826)
  [Model] Add LFM3-Text (#65826)
  _Files: `docs/models/supported_models.md`, `tests/kernels/mamba/test_causal_conv1d.py`, `tests/model_executor/test_lfm3.py`, `tests/models/registry.py` _+6 more__
- **2026-11-05** [`871147447b`](https://github.com/vllm-project/vllm/commit/871147447b) [#65750](https://github.com/vllm-project/vllm/pull/65750)
  [CI] Pass --models=llama3.2 so Rust Frontend Tool Use gets a shard plan (#65750)
  _Files: `.buildkite/test_areas/rust_frontend.yaml`_
- **2026-11-05** [`4a0b90a7b0`](https://github.com/vllm-project/vllm/commit/4a0b90a7b0) [#64561](https://github.com/vllm-project/vllm/pull/64561)
  [CI] Shard Spec Decode AL MTP automatically and split its Gemma4 test by dataset (#64561)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `tests/v1/e2e/spec_decode/acceptance_rates/mtp_other/test_mtp.py`_
- **2026-11-05** [`83fcf52ec3`](https://github.com/vllm-project/vllm/commit/83fcf52ec3) [#64898](https://github.com/vllm-project/vllm/pull/64898)
  [Perf][Qwen4Exp] Fuse HyperConnection up projection and gate mix for long prefills (#64898)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `CMakeLists.txt`, `csrc/qwen4_exp/hc_up_gate_mix.cu`, `csrc/torch_bindings.cpp` _+3 more__
- **2026-11-05** [`4d7230955b`](https://github.com/vllm-project/vllm/commit/4d7230955b) [#65692](https://github.com/vllm-project/vllm/pull/65692)
  [Perf][Qwen4Exp] Route the PLE shard copy through copy_weight_ (#65692)
  _Files: `vllm/models/qwen4_exp/common/ple.py`_
- **2026-11-05** [`76f5e47017`](https://github.com/vllm-project/vllm/commit/76f5e47017) [#65293](https://github.com/vllm-project/vllm/pull/65293)
  [Rust Frontend] Choose chat content format by probing the template (#65293)
  _Files: `rust/src/chat/src/renderer/glm5_next/tests.rs`, `rust/src/chat/src/renderer/hf/format.rs`, `rust/src/chat/src/renderer/hf/mod.rs`, `rust/src/chat/src/renderer/hf/template.rs` _+34 more__
- **2026-11-04** [`9a56d4fec6`](https://github.com/vllm-project/vllm/commit/9a56d4fec6) [#65619](https://github.com/vllm-project/vllm/pull/65619)
  [Perf][Qwen4Exp] Share the QSA top-k buffer across layers (#65619)
  _Files: `vllm/models/qwen4_exp/nvidia/model.py`, `vllm/models/qwen4_exp/nvidia/mtp.py`, `vllm/models/qwen4_exp/nvidia/qsa.py`_
- **2026-11-04** [`db92777662`](https://github.com/vllm-project/vllm/commit/db92777662) [#65375](https://github.com/vllm-project/vllm/pull/65375)
  [Rust Frontend] Drop incomplete tool-call markup at the end of output like Python (#65375)
  _Files: `rust/src/chat/src/output/default/unified.rs`, `rust/src/parser/src/tool/deepseek_dsml/mod.rs`, `rust/src/parser/src/tool/deepseek_json/deepseek_v3.rs`, `rust/src/parser/src/tool/deepseek_json/deepseek_v31.rs` _+21 more__
- **2026-11-04** [`bf4510cf19`](https://github.com/vllm-project/vllm/commit/bf4510cf19) [#65445](https://github.com/vllm-project/vllm/pull/65445)
  [Model] Canary: require `language` and test translation (#65445)
  _Files: `docs/serving/online_serving/speech_to_text.md`, `tests/entrypoints/speech_to_text/translation/test_translation_validation.py`, `vllm/model_executor/models/canary.py`_
- **2026-11-04** [`537d919f52`](https://github.com/vllm-project/vllm/commit/537d919f52) [#65371](https://github.com/vllm-project/vllm/pull/65371)
  [Rust Frontend] Coerce replayed tool-call arguments that are not an object (#65371)
  _Files: `rust/src/chat/src/renderer/deepseek_v32/encoding.rs`, `rust/src/chat/src/renderer/deepseek_v32/tests.rs`, `rust/src/chat/src/renderer/glm5_next/encoding.rs`, `rust/src/chat/src/renderer/glm5_next/tests.rs` _+4 more__
- **2026-11-04** [`5492477bee`](https://github.com/vllm-project/vllm/commit/5492477bee) [#65376](https://github.com/vllm-project/vllm/pull/65376)
  [Rust Frontend] Return 501 for /generative_scoring and the opt-in Cohere v2 chat routes (#65376)
  _Files: `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-11-04** [`128eb0f9ca`](https://github.com/vllm-project/vllm/commit/128eb0f9ca) [#63348](https://github.com/vllm-project/vllm/pull/63348)
  [Docs] Add Qwen3-4B and tidy Qwen entries in batch invariance tested models (#63348)
  _Files: `docs/features/batch_invariance.md`_
- **2026-11-04** [`643d6531fe`](https://github.com/vllm-project/vllm/commit/643d6531fe) [#62647](https://github.com/vllm-project/vllm/pull/62647)
  [Bugfix][Frontend] Materialize DeepSeek V4.1 content iterators before deepcopy (#62647)
  _Files: `tests/tokenizers_/test_deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py`_
- **2026-11-03** [`eab6a8b276`](https://github.com/vllm-project/vllm/commit/eab6a8b276) [#64743](https://github.com/vllm-project/vllm/pull/64743)
  [Bugfix][Mistral] Carry token ids in stream state for byte-fallback tokens (#64743)
  _Files: `docs/serving/online_serving/derenderer.md`, `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`, `vllm/renderers/online_derenderer.py`_
- **2026-11-03** [`866bccf083`](https://github.com/vllm-project/vllm/commit/866bccf083) [#65206](https://github.com/vllm-project/vllm/pull/65206)
  [Bugfix][Model] Share one RoPE cache across Muse Spark NVIDIA layers (#65206)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_muse_spark_nvidia_shared_rope.py`, `vllm/models/muse_spark/nvidia/model.py`_
- **2026-11-03** [`3d18166d45`](https://github.com/vllm-project/vllm/commit/3d18166d45) [#64442](https://github.com/vllm-project/vllm/pull/64442)
  [Perf][DSpark][DSv4.1] Fuse the Markov sampling loop on NVIDIA by inverse CDF (#64442)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/deepseek_v41/nvidia/test_fused_markov.py`, `vllm/models/deepseek_v41/nvidia/dspark.py`, `vllm/models/deepseek_v41/nvidia/ops/fused_markov.py`_
- **2026-11-03** [`20ca5e895d`](https://github.com/vllm-project/vllm/commit/20ca5e895d) [#65093](https://github.com/vllm-project/vllm/pull/65093)
  [Bugfix][Pooling] Fix scoring token limits with MistralTokenizer (#65093)
  _Files: `tests/entrypoints/pooling/scoring/test_bi_encoder_offline.py`, `tests/entrypoints/pooling/scoring/test_utils.py`, `vllm/entrypoints/pooling/scoring/utils.py`_
- **2026-11-03** [`4fe358738b`](https://github.com/vllm-project/vllm/commit/4fe358738b) [#65050](https://github.com/vllm-project/vllm/pull/65050)
  [Kernel] Enable CuteDSL GDN prefill on SM110 (#65050)
  _Files: `tests/kernels/mamba/test_gdn_prefill_cutedsl.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`, `vllm/model_executor/layers/mamba/ops/gdn_chunk_cutedsl/kernel_kkt_inv_uw.py`, `vllm/model_executor/layers/mamba/ops/gdn_chunk_cutedsl/kernel_o.py`_
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

## CI / Build  (37 commits)

- **2026-11-09** [`ceb319b5cc`](https://github.com/vllm-project/vllm/commit/ceb319b5cc) [#63352](https://github.com/vllm-project/vllm/pull/63352)
  [CI][Test] Bias test_stop_reason toward the stop token (#63352)
  _Files: `tests/detokenizer/test_stop_reason.py`_
- **2026-11-08** [`9b9bd049a7`](https://github.com/vllm-project/vllm/commit/9b9bd049a7) [#65158](https://github.com/vllm-project/vllm/pull/65158)
  [CI] Add check-docstring-style pre-commit hook and use single backticks in docstrings (#65158)
- **2026-11-07** [`52e8596181`](https://github.com/vllm-project/vllm/commit/52e8596181) [#56246](https://github.com/vllm-project/vllm/pull/56246)
  [CI][XPU] Add Rust Frontend CI coverage for Intel GPU (#56246)
  _Files: `.buildkite/intel_jobs/rust_frontend_intel.yaml`_
- **2026-11-06** [`0d5306aaca`](https://github.com/vllm-project/vllm/commit/0d5306aaca) [#66175](https://github.com/vllm-project/vllm/pull/66175)
  [CI] Recompile the KV connector lock against the raised opentelemetry floors (#66175)
  _Files: `.pre-commit-config.yaml`, `requirements/test/kv_connectors_cuda.overrides`, `requirements/test/kv_connectors_cuda.txt`, `tools/kv_connector_lock.py`_
- **2026-11-06** [`bd24e246b0`](https://github.com/vllm-project/vllm/commit/bd24e246b0) [#66111](https://github.com/vllm-project/vllm/pull/66111)
  [CI] Reuse the HF reference across use_prompt_embeds (#66111)
  _Files: `tests/models/language/generation/test_common.py`_
- **2026-11-06** [`1c8ecd744d`](https://github.com/vllm-project/vllm/commit/1c8ecd744d) [#65514](https://github.com/vllm-project/vllm/pull/65514)
  [CI] Run PyTorch Compilation root tests in one pytest, with test_config.py's forked tests spawned (#65514)
  _Files: `.buildkite/test_areas/pytorch.yaml`, `tests/compile/test_compile_ranges.py`, `tests/compile/test_config.py`, `tests/compile/test_graph_partition.py` _+1 more__
- **2026-11-06** [`1b2505c033`](https://github.com/vllm-project/vllm/commit/1b2505c033) [#66016](https://github.com/vllm-project/vllm/pull/66016)
  [Build][Bugfix] Never fall back from an x.yf CUDA arch to a lower minor (#66016)
  _Files: `cmake/utils.cmake`, `tests/test_cmake_utils.py`_
- **2026-11-06** [`aa4022dc81`](https://github.com/vllm-project/vllm/commit/aa4022dc81) [#66039](https://github.com/vllm-project/vllm/pull/66039)
  [XPU][CI] Correct deselected file path in entrypoints/scale_out test (#66039)
  _Files: `.buildkite/intel_jobs/entrypoints_intel.yaml`_
- **2026-11-06** [`d3155eea6a`](https://github.com/vllm-project/vllm/commit/d3155eea6a) [#66005](https://github.com/vllm-project/vllm/pull/66005)
  [CI][Frontend] Pin the derender n2 parity cases to top-1 sampling (#66005)
  _Files: `tests/entrypoints/scale_out/derender/test_derender_parity.py`_
- **2026-11-05** [`bc9a3ac5dc`](https://github.com/vllm-project/vllm/commit/bc9a3ac5dc) [#64802](https://github.com/vllm-project/vllm/pull/64802)
  [Bugfix] Update humming-kernels version to 0.1.19 (#64802)
  _Files: `requirements/cuda.txt`_
- **2026-11-05** [`fd31b066bb`](https://github.com/vllm-project/vllm/commit/fd31b066bb) [#59041](https://github.com/vllm-project/vllm/pull/59041)
  [CI][Test] Use file:// rendezvous in the Ray multi-GPU test harness (#59041)
  _Files: `tests/utils.py`_
- **2026-11-05** [`723b1c1aa1`](https://github.com/vllm-project/vllm/commit/723b1c1aa1) [#65910](https://github.com/vllm-project/vllm/pull/65910)
  [CI][Step5] Pin the starting block size in the CSA tail ring test (#65910)
  _Files: `tests/models/step5/test_csa_tail_ring_block_size.py`_
- **2026-11-05** [`2f8c840032`](https://github.com/vllm-project/vllm/commit/2f8c840032) [#64187](https://github.com/vllm-project/vllm/pull/64187)
  [Perf][Model Loader] Make the EP weight filter EPLB-aware (#64187)
  _Files: `.buildkite/test_areas/expert_parallelism.yaml`, `tests/model_executor/model_loader/test_ep_weight_filter.py`, `tests/model_executor/model_loader/test_ep_weight_filter_eplb.py`, `vllm/config/parallel.py` _+2 more__
- **2026-11-05** [`c5ff008806`](https://github.com/vllm-project/vllm/commit/c5ff008806) [#65669](https://github.com/vllm-project/vllm/pull/65669)
  [CPU][Zen] Update zentorch to 2.14.0.2 (#65669)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/scripts/hardware_ci/run-zen-cpu-test.sh`, `setup.py`_
- **2026-11-05** [`bc93b8d2db`](https://github.com/vllm-project/vllm/commit/bc93b8d2db) [#64826](https://github.com/vllm-project/vllm/pull/64826)
  [CI] Run Distributed Features examples once and shard its pytest commands (#64826)
  _Files: `.buildkite/test_areas/distributed.yaml`_
- **2026-11-05** [`90b7739938`](https://github.com/vllm-project/vllm/commit/90b7739938) [#65494](https://github.com/vllm-project/vllm/pull/65494)
  [Build] Update DeepGEMM pin to latest main (#65494)
  _Files: `cmake/external_projects/deepgemm.cmake`_
- **2026-11-05** [`f9621239eb`](https://github.com/vllm-project/vllm/commit/f9621239eb) [#65753](https://github.com/vllm-project/vllm/pull/65753)
  [CI] Consolidate per-version model labels into vendor/family labels (#65753)
  _Files: `.github/mergify.yml`, `.github/workflows/issue_autolabel.yml`_
- **2026-11-05** [`46f36fa294`](https://github.com/vllm-project/vllm/commit/46f36fa294) [#65762](https://github.com/vllm-project/vllm/pull/65762)
  [CI] Let ci-selector decide csrc/ changes on CUDA (#65762)
  _Files: `.buildkite/ci_config.yaml`_
- **2026-11-04** [`520cae222b`](https://github.com/vllm-project/vllm/commit/520cae222b) [#65473](https://github.com/vllm-project/vllm/pull/65473)
  [CI] Run test_depyf_integration in a spawned process (#65473)
  _Files: `tests/compile/fullgraph/test_full_graph.py`_
- **2026-11-04** [`4527515cd7`](https://github.com/vllm-project/vllm/commit/4527515cd7) [#59526](https://github.com/vllm-project/vllm/pull/59526)
  [CI] Run pip-compile pre-commit hooks only when requirements change (#59526)
  _Files: `.github/workflows/pip-compile-drift.yml`, `.github/workflows/pre-commit.yml`, `.pre-commit-config.yaml`_
- **2026-11-04** [`0cb25c3574`](https://github.com/vllm-project/vllm/commit/0cb25c3574) [#65540](https://github.com/vllm-project/vllm/pull/65540)
  [Build] Marlin: drop SM12x-specific cubins and rely on compute_80 PTX (#65540)
  _Files: `CMakeLists.txt`_
- **2026-11-04** [`c902b75ac1`](https://github.com/vllm-project/vllm/commit/c902b75ac1) [#65567](https://github.com/vllm-project/vllm/pull/65567)
  [CI] Run H100 fusion config sweeps and batch invariance nightly only (#65567)
  _Files: `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/misc.yaml`_
- **2026-11-04** [`25e7c5728d`](https://github.com/vllm-project/vllm/commit/25e7c5728d) [#64762](https://github.com/vllm-project/vllm/pull/64762)
  [CI] Use test models from the vllm-project Hub org (#64762)
- **2026-11-04** [`ae0bd3d48a`](https://github.com/vllm-project/vllm/commit/ae0bd3d48a) [#63977](https://github.com/vllm-project/vllm/pull/63977)
  [XPU] upgrade to torch 2.15 (#63977)
  _Files: `docker/Dockerfile.xpu`, `docs/getting_started/installation/gpu.xpu.inc.md`, `requirements/test/xpu.txt`, `requirements/xpu.txt`_
- **2026-11-04** [`173d063acd`](https://github.com/vllm-project/vllm/commit/173d063acd) [#65482](https://github.com/vllm-project/vllm/pull/65482)
  [CI] Enroll RL Entrypoints in automatic sharding (#65482)
  _Files: `.buildkite/test_areas/rl.yaml`_
- **2026-11-04** [`9b0c924958`](https://github.com/vllm-project/vllm/commit/9b0c924958) [#65443](https://github.com/vllm-project/vllm/pull/65443)
  [CI][Test] Skip multi-node-only pipeline-parallel cases at collection (#65443)
  _Files: `tests/distributed/test_pipeline_parallel.py`_
- **2026-11-03** [`79d0899cca`](https://github.com/vllm-project/vllm/commit/79d0899cca) [#65460](https://github.com/vllm-project/vllm/pull/65460)
  [CI] Enroll 1 step in automatic sharding: UMBP Connector TP2 Integration (#65460)
  _Files: `.buildkite/test_areas/misc.yaml`_
- **2026-11-03** [`70eaf457c3`](https://github.com/vllm-project/vllm/commit/70eaf457c3) [#65428](https://github.com/vllm-project/vllm/pull/65428)
  [Bugfix][CI] Keep the chat template on NixlConnector PD + SD acceptance prompts (#65428)
  _Files: `tests/v1/kv_connector/nixl_integration/test_spec_decode_acceptance.py`_
- **2026-11-03** [`84b1cf6e69`](https://github.com/vllm-project/vllm/commit/84b1cf6e69) [#65047](https://github.com/vllm-project/vllm/pull/65047)
  [XPU] update triton-xpu 3.9.0 shim layer (#65047)
  _Files: `.buildkite/scripts/xpu/publish-triton-shim.sh`_
- **2026-11-03** [`97c198cd47`](https://github.com/vllm-project/vllm/commit/97c198cd47) [#63641](https://github.com/vllm-project/vllm/pull/63641)
  [XPU][Test] Use current platform device in test_compile_ranges (#63641)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `tests/compile/test_compile_ranges.py`_
- **2026-11-03** [`b016eaaf52`](https://github.com/vllm-project/vllm/commit/b016eaaf52) [#64396](https://github.com/vllm-project/vllm/pull/64396)
  [CI][XPU] Extend batch-invariance tests in Intel CI (#64396)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`_
- **2026-11-03** [`5c4b94beec`](https://github.com/vllm-project/vllm/commit/5c4b94beec) [#64651](https://github.com/vllm-project/vllm/pull/64651)
  [XPU][CI] add EPD test into intel CI (#64651)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`_
- **2026-11-02** [`b2a9480dc7`](https://github.com/vllm-project/vllm/commit/b2a9480dc7) [#65211](https://github.com/vllm-project/vllm/pull/65211)
  [CI] Enroll 6 jobs in automatic sharding (#65211)
  _Files: `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/models_basic.yaml`_
- **2026-11-02** [`d292ac4cbb`](https://github.com/vllm-project/vllm/commit/d292ac4cbb) [#64788](https://github.com/vllm-project/vllm/pull/64788)
  [CI] Enroll Spec Decode AL DSpark and UMBP Connector Integration in automatic sharding (#64788)
  _Files: `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/spec_decode.yaml`_
- **2026-11-02** [`c34e5867a8`](https://github.com/vllm-project/vllm/commit/c34e5867a8) [#64272](https://github.com/vllm-project/vllm/pull/64272)
  [CI] Enroll 13 jobs in automatic sharding (#64272)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `.buildkite/test_areas/spec_decode.yaml`_
- **2026-11-02** [`db7f2d7c44`](https://github.com/vllm-project/vllm/commit/db7f2d7c44) [#65162](https://github.com/vllm-project/vllm/pull/65162)
  [Build] Fetch `triton_kernels` from a source tarball instead of a `git clone` (avoiding +400 MB pull) (#65162)
  _Files: `cmake/external_projects/triton_kernels.cmake`_
- **2026-11-02** [`ccafd6c65c`](https://github.com/vllm-project/vllm/commit/ccafd6c65c) [#64585](https://github.com/vllm-project/vllm/pull/64585)
  [NIXL][CI/Build] Bump NIXL to 1.5.2 and drop source build for Rubin (#64585)
  _Files: `.buildkite/release-pipeline.yaml`, `docker/Dockerfile`, `docker/versions.json`, `docs/contributing/dockerfile/dockerfile.md` _+3 more__

## KV Cache / Offload  (30 commits)

- **2026-11-09** [`85b52c9f53`](https://github.com/vllm-project/vllm/commit/85b52c9f53) [#55855](https://github.com/vllm-project/vllm/pull/55855)
  [Feature][KV Offload] Add RDMA-capable OBJ tier (#55855) (#56192)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/tiering/obj/config.py`, `vllm/v1/kv_offload/tiering/obj/manager.py`_
- **2026-11-08** [`80e2e486f2`](https://github.com/vllm-project/vllm/commit/80e2e486f2) [#65137](https://github.com/vllm-project/vllm/pull/65137)
  [Bugfix][KV Connector] Keep same-host NIXL on NVLink with the extensible KV cache (#65137)
  _Files: `docs/features/nixl_connector_usage.md`, `tests/utils_/test_vmm_driver.py`, `tests/v1/engine/test_engine_args.py`, `vllm/config/cache.py` _+3 more__
- **2026-11-08** [`b022bb7a48`](https://github.com/vllm-project/vllm/commit/b022bb7a48) [#65640](https://github.com/vllm-project/vllm/pull/65640)
  [Bugfix][KV Offload] Refresh streaming request keys after preemption (#65640)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-11-08** [`5dcc7fb261`](https://github.com/vllm-project/vllm/commit/5dcc7fb261) [#64298](https://github.com/vllm-project/vllm/pull/64298)
  [Bugfix][KV Offload][P2P] Fail never-sent fetches locally (#64298)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/manager.py` _+2 more__
- **2026-11-07** [`7a07e2342e`](https://github.com/vllm-project/vllm/commit/7a07e2342e) [#60130](https://github.com/vllm-project/vllm/pull/60130)
  [KV Offload] SimpleCPUOffload: one host buffer per rank, opt-in HugeTLB pages (#60130)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/simple_kv_offload/conftest.py`, `tests/v1/simple_kv_offload/test_host_buffer.py`, `tests/v1/simple_kv_offload/test_worker.py` _+9 more__
- **2026-11-06** [`3204273e8d`](https://github.com/vllm-project/vllm/commit/3204273e8d) [#65463](https://github.com/vllm-project/vllm/pull/65463)
  [Bugfix][KV Cache] Re-fit `--max-model-len auto` after the extensible KV cache shrinks (#65463)
  _Files: `tests/v1/core/test_kv_cache_planning.py`, `tests/v1/worker/test_gpu_target_dependent_ar_speculator.py`, `vllm/v1/core/kv_cache_planning.py`, `vllm/v1/engine/core.py` _+4 more__
- **2026-11-06** [`3becade3b0`](https://github.com/vllm-project/vllm/commit/3becade3b0) [#66019](https://github.com/vllm-project/vllm/pull/66019)
  [CI][KV Offload] Pin GPU block size in test_p2p_cache_reset_with_absent_decoder (#66019)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`_
- **2026-11-05** [`5b62a2853d`](https://github.com/vllm-project/vllm/commit/5b62a2853d) [#65631](https://github.com/vllm-project/vllm/pull/65631)
  [Bugfix][KV Offload] Keep whole-chunk max_load_tokens caps with sliding window groups (#65631)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-11-05** [`9f8c539a3b`](https://github.com/vllm-project/vllm/commit/9f8c539a3b) [#65124](https://github.com/vllm-project/vllm/pull/65124)
  [Bugfix][KV Offload][P2P] Abort inbound loads when draining for a cache reset (#65124)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/manager.py`, `vllm/v1/kv_offload/tiering/p2p/session/client.py` _+1 more__
- **2026-11-05** [`0b3a608dd7`](https://github.com/vllm-project/vllm/commit/0b3a608dd7) [#65237](https://github.com/vllm-project/vllm/pull/65237)
  [Bugfix][KV Offload] Keep lazy SimpleCPUOffload stores at the GPU eviction end (#65237)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-11-04** [`575cc1faf4`](https://github.com/vllm-project/vllm/commit/575cc1faf4) [#64677](https://github.com/vllm-project/vllm/pull/64677)
  [Bugfix][UMBP] Copy every KV cache layout's per-head runs (#64677)
  _Files: `tests/v1/kv_connector/unit/test_umbp_embedded.py`, `vllm/distributed/kv_transfer/kv_connector/v1/umbp/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/umbp/runtime/embedded.py`_
- **2026-11-04** [`31f84f6b95`](https://github.com/vllm-project/vllm/commit/31f84f6b95) [#65198](https://github.com/vllm-project/vllm/pull/65198)
  [GLM 5.3 Perf] Align draft model kv cache dtype align with target, 50% GPU Memory saved for each draft model (#65198)
  _Files: `vllm/model_executor/models/config.py`_
- **2026-11-04** [`a92efadb30`](https://github.com/vllm-project/vllm/commit/a92efadb30) [#59383](https://github.com/vllm-project/vllm/pull/59383)
  [Bugfix][KV Offload] Return lazily offloaded GPU blocks to the eviction end (#59383)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/core/block_pool.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-11-04** [`226104db52`](https://github.com/vllm-project/vllm/commit/226104db52) [#63696](https://github.com/vllm-project/vllm/pull/63696)
  [KV Offload] Describe complete stores from request context (#63696)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py` _+1 more__
- **2026-11-04** [`0b5a44fe08`](https://github.com/vllm-project/vllm/commit/0b5a44fe08) [#65331](https://github.com/vllm-project/vllm/pull/65331)
  [Bugfix][KV Connector] Mooncake store: register the committed blocks of an extensible KV cache (#65331)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-11-03** [`260b0c6d7e`](https://github.com/vllm-project/vllm/commit/260b0c6d7e) [#65413](https://github.com/vllm-project/vllm/pull/65413)
  [Bugfix] Size the extensible KV cache from UMA-corrected free memory (#65413)
  _Files: `tests/utils_/test_mem_utils.py`, `tests/v1/worker/test_extensible_kv_cache.py`, `vllm/platforms/cuda.py`, `vllm/platforms/interface.py` _+2 more__
- **2026-11-03** [`a5db4c9ff5`](https://github.com/vllm-project/vllm/commit/a5db4c9ff5) [#65455](https://github.com/vllm-project/vllm/pull/65455)
  [KV Offload] Adapt to the new KVCR key adapter API (#65455)
  _Files: `.buildkite/scripts/install-kv-offload.sh`, `tests/v1/kv_offload/tiering/test_kvcr_tier.py`, `vllm/v1/kv_offload/tiering/kvcr/manager.py`_
- **2026-11-03** [`80ca61b6d9`](https://github.com/vllm-project/vllm/commit/80ca61b6d9) [#56076](https://github.com/vllm-project/vllm/pull/56076)
  [KV Offload] Refactor cpu offloading - calculate gpu pointers and introduce fs ABC (#56076)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_offload/cpu/test_canonical_layout.py`, `tests/v1/kv_offload/cpu/test_gpu_worker.py` _+8 more__
- **2026-11-03** [`8210387296`](https://github.com/vllm-project/vllm/commit/8210387296) [#57474](https://github.com/vllm-project/vllm/pull/57474)
  [Perf][KV Offload] Publish async lookup results per request group (#57474)
  _Files: `tests/v1/kv_offload/tiering/test_async_lookup.py`, `vllm/v1/kv_offload/tiering/async_lookup.py`_
- **2026-11-03** [`4d1c44780c`](https://github.com/vllm-project/vllm/commit/4d1c44780c) [#64686](https://github.com/vllm-project/vllm/pull/64686)
  [Bugfix][KV Offload][P2P] Clean up both roles on request finish (#64686)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `vllm/v1/kv_offload/tiering/p2p/manager.py`_
- **2026-11-03** [`43067f6df6`](https://github.com/vllm-project/vllm/commit/43067f6df6) [#65279](https://github.com/vllm-project/vllm/pull/65279)
  [Bugfix][KV Offload] Preserve SWA null-page offsets after store retry (#65279)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-11-03** [`ffdf26702a`](https://github.com/vllm-project/vllm/commit/ffdf26702a) [#64299](https://github.com/vllm-project/vllm/pull/64299)
  [Bugfix][KV Offload][P2P] Settle buffered terminal messages after disconnect (#64299)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `tests/v1/kv_offload/tiering/test_p2p_lifecycle_e2e.py`, `vllm/v1/kv_offload/tiering/p2p/session/session.py`_
- **2026-11-03** [`ddbe9beb75`](https://github.com/vllm-project/vllm/commit/ddbe9beb75) [#64993](https://github.com/vllm-project/vllm/pull/64993)
  [Test][KV Offload] Update stale partial-tail scheduler expectations (#64993)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`_
- **2026-11-03** [`eb239e34c2`](https://github.com/vllm-project/vllm/commit/eb239e34c2) [#64558](https://github.com/vllm-project/vllm/pull/64558)
  [Bugfix][KV Offload] Count each key once per request toward store_threshold (#64558)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/v1/kv_offload/cpu/manager.py`_
- **2026-11-03** [`8cf1277362`](https://github.com/vllm-project/vllm/commit/8cf1277362) [#65225](https://github.com/vllm-project/vllm/pull/65225)
  [Bugfix] Pad extensible KV cache segments instead of rounding the block count (#65225)
  _Files: `tests/v1/core/test_kv_cache_planning.py`, `tests/v1/engine/test_engine_args.py`, `tests/v1/worker/test_extensible_kv_cache.py`, `tests/v1/worker/test_gpu_worker.py` _+8 more__
- **2026-11-02** [`8278030eba`](https://github.com/vllm-project/vllm/commit/8278030eba) [#64472](https://github.com/vllm-project/vllm/pull/64472)
  [Bugfix][Core] Keep KV cache zeroing for mixed-precision UniformTypeKVCacheSpecs groups (#64472)
  _Files: `.buildkite/test_areas/distributed.yaml`, `docs/features/quantization/quantized_kvcache.md`, `tests/distributed/test_pipeline_parallel.py`, `tests/v1/core/test_kv_cache_utils.py` _+3 more__
- **2026-11-02** [`5cdeea9b13`](https://github.com/vllm-project/vllm/commit/5cdeea9b13) [#64444](https://github.com/vllm-project/vllm/pull/64444)
  [Bugfix][KV Offload] Publish successful stores to lookup state (#64444)
  _Files: `tests/v1/kv_offload/tiering/test_async_lookup.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/tiering/async_lookup.py` _+2 more__
- **2026-11-02** [`8c8d25a963`](https://github.com/vllm-project/vllm/commit/8c8d25a963) [#63988](https://github.com/vllm-project/vllm/pull/63988)
  [Bugfix][KV Offload] Drain unfetched P2P stores before cache reset (#63988)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/manager.py` _+2 more__
- **2026-11-02** [`fc86a5fba6`](https://github.com/vllm-project/vllm/commit/fc86a5fba6) [#64300](https://github.com/vllm-project/vllm/pull/64300)
  [Bugfix][KV Offload][P2P] Avoid leaking failed IDs for finished requests (#64300)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `tests/v1/kv_offload/tiering/test_p2p_lifecycle_e2e.py`, `vllm/v1/kv_offload/tiering/p2p/manager.py` _+1 more__
- **2026-11-02** [`f1df4a3ae9`](https://github.com/vllm-project/vllm/commit/f1df4a3ae9) [#64819](https://github.com/vllm-project/vllm/pull/64819)
  [Bugfix][KV Offload][P2P] Disconnect a peer whose registration fails (#64819)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/session/session.py`_

## Scheduler / Engine  (29 commits)

- **2026-11-09** [`f1d17fe83c`](https://github.com/vllm-project/vllm/commit/f1d17fe83c) [#66224](https://github.com/vllm-project/vllm/pull/66224)
  [Core] Simplify `prefill_schedule_interval` outside data parallelism (#66224)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `tests/v1/engine/test_engine_core.py`, `tests/v1/kv_connector/unit/test_handshake_pp_aggregation.py` _+3 more__
- **2026-11-09** [`a6cf455ad9`](https://github.com/vllm-project/vllm/commit/a6cf455ad9) [#63337](https://github.com/vllm-project/vllm/pull/63337)
  [Bugfix] Tell a stopped engine core apart from a dead one during AsyncLLM shutdown (#63337)
  _Files: `tests/v1/engine/test_async_llm_shutdown_race.py`, `vllm/v1/engine/async_llm.py`, `vllm/v1/engine/core_client.py`_
- **2026-11-09** [`3f898e55c6`](https://github.com/vllm-project/vllm/commit/3f898e55c6) [#65629](https://github.com/vllm-project/vllm/pull/65629)
  [Rust Frontend][Perf] Reduce per-request output channel memory (#65629)
  _Files: `rust/src/engine-core-client/src/client/output_channel.rs`_
- **2026-11-09** [`9ff2963a79`](https://github.com/vllm-project/vllm/commit/9ff2963a79) [#65864](https://github.com/vllm-project/vllm/pull/65864)
  [Rust Frontend] Return routed experts on non-streaming chat and completions (#65864)
  _Files: `docs/training/routed_experts.md`, `rust/src/chat/src/event.rs`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/default/unified.rs` _+26 more__
- **2026-11-09** [`7a8338f849`](https://github.com/vllm-project/vllm/commit/7a8338f849) [#66105](https://github.com/vllm-project/vllm/pull/66105)
  [Rust Frontend] Export SimpleCPUOffload KV connector metrics (#66105)
  _Files: `rust/src/engine-core-client/src/metrics.rs`, `rust/src/engine-core-client/src/protocol/stats.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py` _+1 more__
- **2026-11-08** [`73864f8360`](https://github.com/vllm-project/vllm/commit/73864f8360) [#66315](https://github.com/vllm-project/vllm/pull/66315)
  [Bugfix][Mamba] Validate CLI stochastic rounding against the platform (#66315)
  _Files: `vllm/engine/arg_utils.py`_
- **2026-11-07** [`5a763c3649`](https://github.com/vllm-project/vllm/commit/5a763c3649) [#65792](https://github.com/vllm-project/vllm/pull/65792)
  [BugFix][DP] Hash the parallel config before engine init for DP validation (#65792)
  _Files: `tests/v1/engine/test_startup_watch_processes.py`, `vllm/v1/engine/utils.py`_
- **2026-11-06** [`51300e32e4`](https://github.com/vllm-project/vllm/commit/51300e32e4) [#64159](https://github.com/vllm-project/vllm/pull/64159)
  [Bugfix][DP] Log cross-engine step statistics ordering at debug level (#64159)
  _Files: `docs/usage/troubleshooting.md`, `vllm/v1/engine/coordinator.py`_
- **2026-11-06** [`b2094acc88`](https://github.com/vllm-project/vllm/commit/b2094acc88) [#42837](https://github.com/vllm-project/vllm/pull/42837)
  [feature] shuffle safetensor weight files (#42837)
  _Files: `vllm/config/load.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/model_loader/default_loader.py`, `vllm/model_executor/model_loader/weight_utils.py`_
- **2026-11-06** [`0f0172d903`](https://github.com/vllm-project/vllm/commit/0f0172d903) [#62517](https://github.com/vllm-project/vllm/pull/62517)
  [Bugfix][Parser] DeepSeek V4.1: don't leak a `<｜DSML｜ tool_calls>` opener into content (#62517)
  _Files: `tests/parser/engine/test_deepseek_v41.py`, `vllm/parser/deepseek_v41.py`_
- **2026-11-05** [`14d3ec2b89`](https://github.com/vllm-project/vllm/commit/14d3ec2b89) [#65285](https://github.com/vllm-project/vllm/pull/65285)
  [Perf][Core] Cache parked async KV loads' admission reservations (#65285)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/kv_connector/unit/utils.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-11-05** [`2d9d3093ea`](https://github.com/vllm-project/vllm/commit/2d9d3093ea) [#65636](https://github.com/vllm-project/vllm/pull/65636)
  [Rust Frontend] Report system_fingerprint from the engine's config hash (#65636)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/engine-core-client/src/mock_engine.rs` _+15 more__
- **2026-11-05** [`cb59326aee`](https://github.com/vllm-project/vllm/commit/cb59326aee) [#65622](https://github.com/vllm-project/vllm/pull/65622)
  [Rust Frontend] Count vllm:watermark_requests from the engine-reported flag (#65622)
  _Files: `docs/features/watermarking.md`, `rust/src/engine-core-client/src/protocol/output.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py` _+4 more__
- **2026-11-05** [`22a25cfac2`](https://github.com/vllm-project/vllm/commit/22a25cfac2) [#65635](https://github.com/vllm-project/vllm/pull/65635)
  [Rust Frontend] Export vllm:cache_config_info like Python (#65635)
  _Files: `rust/src/engine-core-client/src/metrics.rs`, `rust/src/engine-core-client/src/mock_engine.rs`, `rust/src/engine-core-client/src/protocol/handshake.rs`, `rust/src/engine-core-client/src/tests/client.rs` _+4 more__
- **2026-11-05** [`ee85faa128`](https://github.com/vllm-project/vllm/commit/ee85faa128) [#63488](https://github.com/vllm-project/vllm/pull/63488)
  [Bugfix] Restore engine memory budget after IPC fallback (#63488)
  _Files: `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `tests/v1/worker/test_gpu_worker.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py` _+2 more__
- **2026-11-05** [`37e8a69c60`](https://github.com/vllm-project/vllm/commit/37e8a69c60) [#64695](https://github.com/vllm-project/vllm/pull/64695)
  [Rust Frontend] Generate through an `Llm` trait (#64695)
  _Files: `rust/Cargo.lock`, `rust/src/bench/src/mm_processor.rs`, `rust/src/chat/examples/external_engine_chat_qwen.rs`, `rust/src/chat/src/error.rs` _+24 more__
- **2026-11-04** [`2a777ce26e`](https://github.com/vllm-project/vllm/commit/2a777ce26e) [#54625](https://github.com/vllm-project/vllm/pull/54625)
  [Core] Add cache-aware admission ordering (#54625)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `vllm/config/scheduler.py`, `vllm/engine/arg_utils.py` _+2 more__
- **2026-11-04** [`925db4c416`](https://github.com/vllm-project/vllm/commit/925db4c416) [#62729](https://github.com/vllm-project/vllm/pull/62729)
  [Bugfix] Honor add_generation_prompt and continue_final_message in the DeepSeek V4.1 tokenizer (#62729)
  _Files: `tests/parser/engine/test_deepseek_v41.py`, `tests/tokenizers_/test_deepseek_v41.py`, `vllm/parser/deepseek_v41.py`, `vllm/tokenizers/deepseek_v41.py` _+1 more__
- **2026-11-04** [`3983afd34d`](https://github.com/vllm-project/vllm/commit/3983afd34d) [#64697](https://github.com/vllm-project/vllm/pull/64697)
  [Rust Frontend] Support --skip-tokenizer-init (#64697)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/chat/src/backend/tokenizerless.rs`, `rust/src/chat/src/error.rs` _+24 more__
- **2026-11-04** [`654d9b5ad0`](https://github.com/vllm-project/vllm/commit/654d9b5ad0) [#65369](https://github.com/vllm-project/vllm/pull/65369)
  [Rust Frontend] Stop binding --data-parallel-rank to VLLM_DP_RANK (#65369)
  _Files: `rust/src/managed-engine/src/data_parallel.rs`_
- **2026-11-04** [`ea8052b0fd`](https://github.com/vllm-project/vllm/commit/ea8052b0fd) [#65370](https://github.com/vllm-project/vllm/pull/65370)
  [Rust Frontend] Accept Python underscore and dotted flag forms under vllm-rs serve (#65370)
  _Files: `rust/Cargo.lock`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/managed-engine/Cargo.toml`, `rust/src/managed-engine/src/cli.rs`_
- **2026-11-04** [`0f01fd2b04`](https://github.com/vllm-project/vllm/commit/0f01fd2b04) [#65300](https://github.com/vllm-project/vllm/pull/65300)
  [Perf][Core] Keep per-request token and block id lists out of the cyclic GC (#65300)
  _Files: `tests/utils_/test_gc_utils.py`, `tests/v1/core/test_output.py`, `tests/v1/core/test_prefix_caching.py`, `tests/v1/engine/test_output_processor.py` _+13 more__
- **2026-11-03** [`febcc8ca79`](https://github.com/vllm-project/vllm/commit/febcc8ca79) [#61194](https://github.com/vllm-project/vllm/pull/61194)
  [Bugfix][Watermarking] Skip incomplete opening contexts (#61194)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `docs/features/watermarking.md`, `tests/watermarking/golden_candidates.py`, `tests/watermarking/test_engine_compatibility.py` _+8 more__
- **2026-11-03** [`40837c5d0e`](https://github.com/vllm-project/vllm/commit/40837c5d0e) [#64797](https://github.com/vllm-project/vllm/pull/64797)
  [Recipes Tool][CPU] Remove obsolete TP/DP NUMA binding workaround (#64797)
  _Files: `tools/recipes/SWEEP_TUNING.md`, `tools/recipes/hardware_detection.py`, `tools/recipes/recipe_json_to_vllm_config.py`, `tools/recipes/sweep/scheduler_fallback.py` _+2 more__
- **2026-11-03** [`4c45411134`](https://github.com/vllm-project/vllm/commit/4c45411134) [#62966](https://github.com/vllm-project/vllm/pull/62966)
  [Core] Add watermark_config.enforce to override request opt-outs in EngineCore (#62966)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `docs/features/watermarking.md`, `tests/engine/test_arg_utils.py`, `tests/samplers/test_beam_search_online.py` _+12 more__
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

## Quantization  (29 commits)

- **2026-11-09** [`bf19789e96`](https://github.com/vllm-project/vllm/commit/bf19789e96) [#66034](https://github.com/vllm-project/vllm/pull/66034)
  [XPU][CI]Migrate several B70 jobs from intel_gpu to intel_gpu_k8s (#66034)
  _Files: `.buildkite/intel_jobs/distributed_intel.yaml`, `.buildkite/intel_jobs/lm_eval_intel.yaml`, `.buildkite/intel_jobs/models_language_intel.yaml`, `.buildkite/intel_jobs/quantization_intel.yaml` _+1 more__
- **2026-11-07** [`c06ddca81c`](https://github.com/vllm-project/vllm/commit/c06ddca81c) [#63540](https://github.com/vllm-project/vllm/pull/63540)
  [Perf][DSv4] Process 4 heads per program in fused_inv_rope_fp8_quant (#63540)
  _Files: `tests/kernels/test_fused_inv_rope_fp8_quant.py`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`_
- **2026-11-07** [`5629b26146`](https://github.com/vllm-project/vllm/commit/5629b26146) [#66125](https://github.com/vllm-project/vllm/pull/66125)
  [XPU] skip test_online_hadamard_target_wraps_resolved_method UT (#66125)
  _Files: `tests/quantization/test_online.py`_
- **2026-11-06** [`c2a6042014`](https://github.com/vllm-project/vllm/commit/c2a6042014) [#65791](https://github.com/vllm-project/vllm/pull/65791)
  [Perf] Vectorize silu_and_mul_per_block_quant for large inputs (#65791)
  _Files: `csrc/quantization/fused_kernels/fused_silu_mul_block_quant.cu`, `tests/kernels/core/test_fused_silu_mul_block_quant.py`_
- **2026-11-06** [`86564975c5`](https://github.com/vllm-project/vllm/commit/86564975c5) [#64168](https://github.com/vllm-project/vllm/pull/64168)
  [Bugfix] Fix Gemma 4 vision crash with online FP8 quantization (#64168)
  _Files: `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-11-06** [`2feae41cd6`](https://github.com/vllm-project/vllm/commit/2feae41cd6) [#61821](https://github.com/vllm-project/vllm/pull/61821)
  [Perf][Kernel] Add the bias in the SM120 NVFP4 CUTLASS GEMM epilogue (#61821)
  _Files: `csrc/ops.h`, `csrc/quantization/fp4/nvfp4_scaled_mm_entry.cu`, `csrc/quantization/fp4/nvfp4_scaled_mm_sm120_kernels.cu`, `csrc/torch_bindings.cpp` _+3 more__
- **2026-11-05** [`2cbcb8fb67`](https://github.com/vllm-project/vllm/commit/2cbcb8fb67) [#65484](https://github.com/vllm-project/vllm/pull/65484)
  [CI] Shard Quantization Kernels automatically instead of by hand (#65484)
  _Files: `.buildkite/test_areas/kernels.yaml`_
- **2026-11-05** [`0997a174a5`](https://github.com/vllm-project/vllm/commit/0997a174a5) [#65810](https://github.com/vllm-project/vllm/pull/65810)
  [CI] Drop the removed input_dtype arg from the Zen DA8W4 test (#65810)
  _Files: `tests/kernels/quantization/test_zen_da8w4.py`_
- **2026-11-05** [`3f47d6bec5`](https://github.com/vllm-project/vllm/commit/3f47d6bec5) [#60824](https://github.com/vllm-project/vllm/pull/60824)
  [ZenCPU] Add zen5 CPU tests reusing the pushed zen image (#60824)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/hardware_tests/zen.yaml`, `.buildkite/image_build/image_build_zen_cpu.sh`, `.buildkite/scripts/hardware_ci/run-zen-cpu-test.sh` _+2 more__
- **2026-11-05** [`19e3cfb4f8`](https://github.com/vllm-project/vllm/commit/19e3cfb4f8) [#65552](https://github.com/vllm-project/vllm/pull/65552)
  [CI][DSv4.1] Give the MXFP8 linear test stub a params_dtype (#65552)
  _Files: `tests/models/deepseek_v41/nvidia/specialized_decode/test_kernels.py`_
- **2026-11-04** [`ebf2d13c40`](https://github.com/vllm-project/vllm/commit/ebf2d13c40) [#62881](https://github.com/vllm-project/vllm/pull/62881)
  [Bugfix][Test] Rotate KV into RHT domain in the INT4 unified attn test (#62881)
  _Files: `.buildkite/intel_jobs/quantization_intel.yaml`, `tests/quantization/test_per_token_kv_cache.py`_
- **2026-11-04** [`3f0bcc3d25`](https://github.com/vllm-project/vllm/commit/3f0bcc3d25) [#62836](https://github.com/vllm-project/vllm/pull/62836)
  [Bugfix] Fix GPTQ checkpoint loading for PLaMo3 (#62836)
  _Files: `vllm/model_executor/models/plamo3.py`_
- **2026-11-04** [`69d27bf800`](https://github.com/vllm-project/vllm/commit/69d27bf800) [#64119](https://github.com/vllm-project/vllm/pull/64119)
  [Fast Start] Support ModelOpt CUTLASS block FP8 cache restarts (#64119)
  _Files: `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-11-04** [`625d2d74ea`](https://github.com/vllm-project/vllm/commit/625d2d74ea) [#64182](https://github.com/vllm-project/vllm/pull/64182)
  [Feature][Quantization] Support AWQ/GPTQ Marlin cache restarts (#64182)
  _Files: `vllm/model_executor/layers/quantization/auto_awq.py`, `vllm/model_executor/layers/quantization/auto_gptq.py`_
- **2026-11-03** [`a0d7356b98`](https://github.com/vllm-project/vllm/commit/a0d7356b98) [#65495](https://github.com/vllm-project/vllm/pull/65495)
  [CI][Test] Validate manual NVFP4 fusion in NVIDIA Qwen mixed-precision test (#65495)
  _Files: `tests/compile/fusions_e2e/models.py`, `tests/compile/fusions_e2e/test_tp1_quant.py`_
- **2026-11-03** [`523991fec0`](https://github.com/vllm-project/vllm/commit/523991fec0) [#64723](https://github.com/vllm-project/vllm/pull/64723)
  [Perf][Qwen3.5] (NVIDIA path) Fused AR+norm+quant (#64723)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/qwen3_5/test_fused_allreduce_norm_quant.py`, `vllm/models/qwen3_5/nvidia/model.py`, `vllm/models/qwen3_5/nvidia/ops/fused_allreduce_norm_quant.py`_
- **2026-11-03** [`cc329910bd`](https://github.com/vllm-project/vllm/commit/cc329910bd) [#65496](https://github.com/vllm-project/vllm/pull/65496)
  [Bugfix][MiniMax-M3] Don't emit MXFP8 from the input norm under sequence parallelism (#65496)
  _Files: `vllm/models/minimax_m3/nvidia/model.py`_
- **2026-11-03** [`37753d9dd9`](https://github.com/vllm-project/vllm/commit/37753d9dd9) [#65230](https://github.com/vllm-project/vllm/pull/65230)
  [Quantization] Remove QuTLASS and fp_quant, run QuIP NVFP4 on Humming (#65230)
  _Files: `.buildkite/hardware_tests/ascend_npu.yaml`, `.buildkite/test_areas/kernels.yaml`, `CMakeLists.txt`, `benchmarks/kernels/benchmark_mxfp4_qutlass.py` _+20 more__
- **2026-11-03** [`d5a50f41d9`](https://github.com/vllm-project/vllm/commit/d5a50f41d9) [#65253](https://github.com/vllm-project/vllm/pull/65253)
  [Bugfix][Benchmark] Preserve inactive expert IDs in synthetic forward routing (#65253)
  _Files: `.buildkite/test_areas/quantization.yaml`, `docs/benchmarking/cli.md`, `tests/benchmarks/test_forward_cli.py`, `vllm/benchmarks/forward/routing.py`_
- **2026-11-03** [`39a7f9bf50`](https://github.com/vllm-project/vllm/commit/39a7f9bf50) [#63754](https://github.com/vllm-project/vllm/pull/63754)
  [Fast Start] Support ModelOpt CUTLASS FP8 weight-cache restarts (#63754)
  _Files: `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-11-03** [`a625e62062`](https://github.com/vllm-project/vllm/commit/a625e62062) [#63514](https://github.com/vllm-project/vllm/pull/63514)
  [Bugfix][Kernel] hadacore: fix skipped wait_group on partial-chunk warp for odd row counts (#63514) (#63614)
  _Files: `csrc/quantization/hadamard/hadacore/hadamard_transform_cuda.cu`, `tests/kernels/quantization/test_hadacore.py`_
- **2026-11-03** [`77d2790e78`](https://github.com/vllm-project/vllm/commit/77d2790e78) [#65097](https://github.com/vllm-project/vllm/pull/65097)
  [XPU][CI]Increase memory for Quantization test and deselect timeout case in v1/shutdown (#65097)
  _Files: `.buildkite/intel_jobs/distributed_intel.yaml`, `.buildkite/intel_jobs/quantization_intel.yaml`_
- **2026-11-03** [`608365b0f2`](https://github.com/vllm-project/vllm/commit/608365b0f2) [#64312](https://github.com/vllm-project/vllm/pull/64312)
  [Quantization] Support CSF-compressed NVFP4 block scales in ModelOpt (#64312)
  _Files: `vllm/model_executor/layers/quantization/modelopt.py`, `vllm/model_executor/layers/quantization/utils/nvfp4_utils.py`_
- **2026-11-03** [`eb2975565a`](https://github.com/vllm-project/vllm/commit/eb2975565a) [#61755](https://github.com/vllm-project/vllm/pull/61755)
  [Bugfix][Kernel] Fill K-padded output in silu_and_mul_nvfp4_quant (#61755)
  _Files: `csrc/quantization/fp4/activation_nvfp4_quant_fusion_kernels.cu`, `tests/kernels/quantization/nvfp4_utils.py`, `tests/kernels/quantization/test_silu_mul_nvfp4_quant.py`_
- **2026-11-02** [`57371c4e28`](https://github.com/vllm-project/vllm/commit/57371c4e28) [#60479](https://github.com/vllm-project/vllm/pull/60479)
  [Bugfix] Keep GPTQ linear layers batch invariant (#60479)
  _Files: `tests/kernels/quantization/test_gptq.py`, `vllm/model_executor/determinism/batch_invariant.py`, `vllm/model_executor/layers/quantization/auto_gptq.py`_
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

## Disaggregation / PD  (24 commits)

- **2026-11-09** [`7dce8d697f`](https://github.com/vllm-project/vllm/commit/7dce8d697f) [#66504](https://github.com/vllm-project/vllm/pull/66504)
  [CI][Bugfix] Use a free port for the Mooncake client in the weight-cache tests (#66504)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`_
- **2026-11-09** [`116025c68f`](https://github.com/vllm-project/vllm/commit/116025c68f) [#66412](https://github.com/vllm-project/vllm/pull/66412)
  [CI][KV Connector] Shard the NIXL PD accuracy core sweep and use decode-only CUDA graphs (#66412)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_core_test.sh`, `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`_
- **2026-11-08** [`71eb0c24fa`](https://github.com/vllm-project/vllm/commit/71eb0c24fa) [#65939](https://github.com/vllm-project/vllm/pull/65939)
  [Bugfix][Mooncake] Bound store prefix lookups with a circuit breaker (#65939)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_lookup.py`, `vllm/distributed/kv_transfer/kv_connector/utils.py` _+1 more__
- **2026-11-06** [`ad457ad744`](https://github.com/vllm-project/vllm/commit/ad457ad744) [#59746](https://github.com/vllm-project/vllm/pull/59746)
  [Bugfix][NIXL] Pair P/D blocks by the last token with different block sizes (#59746)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py` _+1 more__
- **2026-11-06** [`cce6818ec7`](https://github.com/vllm-project/vllm/commit/cce6818ec7) [#65667](https://github.com/vllm-project/vllm/pull/65667)
  [Bugfix][MRV2]  Read routed experts from unkeyed full blocks (#65667)
  _Files: `tests/distributed/aux_output_connector/test_store.py`, `vllm/distributed/aux_output_connector/routed_experts.py`, `vllm/distributed/aux_output_connector/worker.py`_
- **2026-11-06** [`d254f6a9bd`](https://github.com/vllm-project/vllm/commit/d254f6a9bd) [#65235](https://github.com/vllm-project/vllm/pull/65235)
  [RL][Model Loader] Load plan: plan_loads and TraceTensor (#65235)
  _Files: `tests/distributed/test_weight_transfer.py`, `tests/model_executor/model_loader/test_load_plan.py`, `vllm/distributed/weight_transfer/nccl_common.py`, `vllm/distributed/weight_transfer/nccl_engine.py` _+7 more__
- **2026-11-06** [`518c624a1c`](https://github.com/vllm-project/vllm/commit/518c624a1c) [#65831](https://github.com/vllm-project/vllm/pull/65831)
  [Perf][Core] Reduce per-block CPU cost of KV block allocation and caching (#65831)
  _Files: `tests/v1/core/test_prefix_caching.py`, `tests/v1/core/test_scheduler.py`, `tests/v1/kv_connector/unit/test_decode_bench_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py` _+7 more__
- **2026-11-05** [`ef70c6a23f`](https://github.com/vllm-project/vllm/commit/ef70c6a23f) [#65539](https://github.com/vllm-project/vllm/pull/65539)
  [Bugfix][Distributed] Fix PP rank derivation when prefill context parallelism is enabled (#65539)
  _Files: `.buildkite/test_areas/distributed.yaml`, `tests/distributed/test_pipeline_partition.py`, `tests/test_config.py`, `tests/utils_/test_ray_utils.py` _+5 more__
- **2026-11-05** [`3199780ac6`](https://github.com/vllm-project/vllm/commit/3199780ac6) [#65160](https://github.com/vllm-project/vllm/pull/65160)
  [Feature][MooncakeStore] Add automatic deployment cache prefixes (#65160)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_cache_prefix.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-11-05** [`80ff32c69c`](https://github.com/vllm-project/vllm/commit/80ff32c69c) [#61292](https://github.com/vllm-project/vllm/pull/61292)
  [KV Connector][Mooncake] Start async lookup when a request arrives via on_new_request (#61292)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py` _+2 more__
- **2026-11-05** [`ebac032b92`](https://github.com/vllm-project/vllm/commit/ebac032b92) [#65773](https://github.com/vllm-project/vllm/pull/65773)
  [Core] Cheapen the spin while waiting for model output (#65773)
  _Files: `tests/distributed/test_shm_broadcast.py`, `tests/v1/engine/test_inputs_during_step.py`, `tests/v1/executor/test_future_wrapper_poll.py`, `vllm/distributed/device_communicators/shm_broadcast.py` _+2 more__
- **2026-11-05** [`8fd219ec84`](https://github.com/vllm-project/vllm/commit/8fd219ec84) [#65593](https://github.com/vllm-project/vllm/pull/65593)
  [Bugfix][EC Connector] Make control-plane ZMQ heartbeats take effect (#65593)
  _Files: `tests/v1/ec_connector/unit/test_control.py`, `vllm/distributed/ec_transfer/ec_connector/cpu/control/zmq.py`_
- **2026-11-04** [`98468d0f66`](https://github.com/vllm-project/vllm/commit/98468d0f66) [#59747](https://github.com/vllm-project/vllm/pull/59747)
  [Bugfix][NIXL] Reject push handshakes between different P/D block sizes (#59747)
  _Files: `docs/features/nixl_connector_compatibility.md`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+1 more__
- **2026-11-04** [`b43366fa4b`](https://github.com/vllm-project/vllm/commit/b43366fa4b) [#60181](https://github.com/vllm-project/vllm/pull/60181)
  [Bugfix][NIXL] Fix host-buffer h2d sync overwriting received KV (#60181)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-11-04** [`101cfd1001`](https://github.com/vllm-project/vllm/commit/101cfd1001) [#55835](https://github.com/vllm-project/vllm/pull/55835)
  [Bugfix][Distributed] Keep cross-node MNNVL groups off CUDA IPC all-reduce (#55835)
  _Files: `tests/distributed/test_custom_all_reduce.py`, `vllm/distributed/device_communicators/custom_all_reduce.py`_
- **2026-11-04** [`cbc77173ed`](https://github.com/vllm-project/vllm/commit/cbc77173ed) [#65466](https://github.com/vllm-project/vllm/pull/65466)
  [Core] Handle new requests and aborts while waiting for model output (#65466)
  _Files: `tests/distributed/test_shm_broadcast.py`, `tests/v1/engine/test_engine_core.py`, `tests/v1/engine/test_inputs_during_step.py`, `tests/v1/executor/test_future_wrapper_poll.py` _+3 more__
- **2026-11-04** [`0db3734d51`](https://github.com/vllm-project/vllm/commit/0db3734d51) [#65076](https://github.com/vllm-project/vllm/pull/65076)
  [KVConnector][Mooncake] Add per-GPU device names for MooncakeStoreConnector (#65076)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py` _+1 more__
- **2026-11-04** [`bc21bd9211`](https://github.com/vllm-project/vllm/commit/bc21bd9211) [#59844](https://github.com/vllm-project/vllm/pull/59844)
  [Bugfix][DeepEP] Upgrade to 2.1 and retain per-context GIN completion ordering (#59844)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `docs/serving/expert_parallel_deployment.md`, `tools/ep_kernels/install_python_libraries.sh` _+2 more__
- **2026-11-04** [`be2ccc43aa`](https://github.com/vllm-project/vllm/commit/be2ccc43aa) [#65529](https://github.com/vllm-project/vllm/pull/65529)
  [Recipe] Kimi-K3: add B200 AgentX aggregated Mooncake preset (#65529)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-11-03** [`56e993a689`](https://github.com/vllm-project/vllm/commit/56e993a689) [#65319](https://github.com/vllm-project/vllm/pull/65319)
  [Core][KV Connector] Start capped async KV loads while the batch is full (#65319)
  _Files: `tests/v1/kv_connector/unit/test_remote_prefill_lifecycle.py`, `tests/v1/kv_connector/unit/utils.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `vllm/config/scheduler.py` _+4 more__
- **2026-11-03** [`32d6ddea18`](https://github.com/vllm-project/vllm/commit/32d6ddea18) [#61795](https://github.com/vllm-project/vllm/pull/61795)
  [UMBP][7/10] Add standalone mode backed by a node-local server (#61795)
  _Files: `docs/features/umbp_store_connector_usage.md`, `vllm/distributed/kv_transfer/kv_connector/v1/umbp/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/umbp/runtime/__init__.py`, `vllm/distributed/kv_transfer/kv_connector/v1/umbp/runtime/embedded.py` _+3 more__
- **2026-11-03** [`f1fd044b70`](https://github.com/vllm-project/vllm/commit/f1fd044b70) [#63420](https://github.com/vllm-project/vllm/pull/63420)
  [Mooncake] Support selective leases for prefix lookups (#63420)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py` _+3 more__
- **2026-11-02** [`a9cf9df752`](https://github.com/vllm-project/vllm/commit/a9cf9df752) [#61764](https://github.com/vllm-project/vllm/pull/61764)
  [Bugfix][EC Connector] Allocate producer control ports at startup (#61764)
  _Files: `docs/features/ec_cpu_connector.md`, `tests/v1/ec_connector/integration/test_nixl_failure.py`, `tests/v1/ec_connector/unit/test_control.py`, `tests/v1/ec_connector/unit/test_scheduler_nixl_ctor.py` _+3 more__
- **2026-11-02** [`62c9b6263c`](https://github.com/vllm-project/vllm/commit/62c9b6263c) [#63971](https://github.com/vllm-project/vllm/pull/63971)
  [Bugfix][Mooncake] Let decodes reuse divergent local hybrid prefix hits (#63971)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_

## Perf / Benchmark  (18 commits)

- **2026-11-09** [`b73373040d`](https://github.com/vllm-project/vllm/commit/b73373040d) [#65583](https://github.com/vllm-project/vllm/pull/65583)
  [Bugfix][Benchmark] Fix bench throughput crash with BlazeEdit HF datasets (#65583)
  _Files: `vllm/benchmarks/throughput.py`_
- **2026-11-09** [`871473fa24`](https://github.com/vllm-project/vllm/commit/871473fa24) [#66483](https://github.com/vllm-project/vllm/pull/66483)
  [Bench] Time target sampling in vllm bench forward (#66483)
  _Files: `.agents/skills/model-microbenchmark/SKILL.md`, `docs/cli/README.md`, `tests/benchmarks/test_forward_cli.py`, `vllm/benchmarks/forward/batch.py` _+4 more__
- **2026-11-07** [`a28953d959`](https://github.com/vllm-project/vllm/commit/a28953d959) [#65589](https://github.com/vllm-project/vllm/pull/65589)
  [Perf][Startup] Don't import vllm.parser from vllm.v1.structured_output (#65589)
  _Files: `tests/standalone_tests/lazy_imports.py`, `tests/v1/structured_output/test_structured_output_manager.py`, `vllm/reasoning/abs_reasoning_parsers.py`, `vllm/v1/structured_output/__init__.py`_
- **2026-11-07** [`dfebb42d09`](https://github.com/vllm-project/vllm/commit/dfebb42d09) [#66021](https://github.com/vllm-project/vllm/pull/66021)
  [Perf][RL] Validate sparse weight patches in one pass (#66021)
  _Files: `tests/model_executor/model_loader/test_checkpoint_weight_patch.py`, `vllm/model_executor/model_loader/checkpoint_weight_patch.py`_
- **2026-11-06** [`365d04acd9`](https://github.com/vllm-project/vllm/commit/365d04acd9) [#60010](https://github.com/vllm-project/vllm/pull/60010)
  [Bugfix][Benchmark] Clean up sweep workers after the server exits (#60010)
  _Files: `docs/benchmarking/sweeps.md`, `tests/benchmarks/sweep/test_server_process.py`, `vllm/benchmarks/sweep/server.py`_
- **2026-11-06** [`4fab5a0747`](https://github.com/vllm-project/vllm/commit/4fab5a0747) [#64831](https://github.com/vllm-project/vllm/pull/64831)
  [Bugfix][Benchmark] Fix bench mm-processor crash with HF datasets (#64831)
  _Files: `tests/benchmarks/test_throughput_cli.py`, `vllm/benchmarks/throughput.py`_
- **2026-11-05** [`cb95d994f4`](https://github.com/vllm-project/vllm/commit/cb95d994f4) [#60882](https://github.com/vllm-project/vllm/pull/60882)
  [Perf][ToolParser] Scan required-tool streaming deltas incrementally (#60882)
  _Files: `tests/parser/test_streaming.py`, `tests/tool_use/test_tool_choice_required.py`, `vllm/parser/abstract_parser.py`, `vllm/tool_parsers/streaming.py`_
- **2026-11-04** [`b1f5f61559`](https://github.com/vllm-project/vllm/commit/b1f5f61559) [#64937](https://github.com/vllm-project/vllm/pull/64937)
  [Bugfix][Benchmark] Count reasoning_content deltas as streamed outputs in chat (#64937)
  _Files: `benchmarks/backend_request_func.py`, `tests/benchmarks/test_endpoint_request_func_timing.py`, `vllm/benchmarks/lib/endpoint_request_func.py`_
- **2026-11-04** [`2d858ac60a`](https://github.com/vllm-project/vllm/commit/2d858ac60a) [#64946](https://github.com/vllm-project/vllm/pull/64946)
  [Rust][Benchmark] Map --output-len to the sharegpt and hf datasets (#64946)
  _Files: `rust/src/bench/src/cli.rs`, `rust/src/bench/src/config.rs`_
- **2026-11-04** [`e423d35725`](https://github.com/vllm-project/vllm/commit/e423d35725) [#64308](https://github.com/vllm-project/vllm/pull/64308)
  [Rust][Benchmark] Record ramp-up runs in the result JSON and filename (#64308)
  _Files: `rust/src/bench/src/benchmark.rs`, `rust/src/bench/src/cli.rs`, `rust/src/bench/src/config.rs`, `rust/src/bench/src/output/json.rs` _+1 more__
- **2026-11-04** [`441d978206`](https://github.com/vllm-project/vllm/commit/441d978206) [#62203](https://github.com/vllm-project/vllm/pull/62203)
  [Perf][ToolParser] Scan Kimi K3 streaming tool calls incrementally (#62203)
  _Files: `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/tool_parsers/kimi_k3_tool_parser.py`_
- **2026-11-04** [`fb4a2174c9`](https://github.com/vllm-project/vllm/commit/fb4a2174c9) [#65284](https://github.com/vllm-project/vllm/pull/65284)
  [Rust][Benchmark] Keep transport failures visible in measured requests (#65284)
  _Files: `rust/src/bench/README.md`, `rust/src/bench/src/benchmark.rs`_
- **2026-11-04** [`a512f0e727`](https://github.com/vllm-project/vllm/commit/a512f0e727) [#65100](https://github.com/vllm-project/vllm/pull/65100)
  [Perf][Spec Decode] Skip vocab blocks with no target token in the resample kernel (#65100)
  _Files: `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `tests/v1/worker/test_gpu_rejection_sampler_chunking.py`, `tests/v1/worker/test_gpu_sampler_flags.py`, `vllm/v1/worker/gpu/sample/sampler.py` _+3 more__
- **2026-11-03** [`6dc6d2c0f3`](https://github.com/vllm-project/vllm/commit/6dc6d2c0f3) [#63742](https://github.com/vllm-project/vllm/pull/63742)
  [Perf][Mamba] Use the shared checkpoint exporter for Mamba2 and drop ssd_checkpoint (#63742)
  _Files: `tests/kernels/mamba/test_checkpoint_exporter.py`, `tests/kernels/mamba/test_mamba2_checkpoint_state.py`, `vllm/model_executor/layers/mamba/checkpoint.py`, `vllm/model_executor/layers/mamba/mamba_mixer2.py` _+1 more__
- **2026-11-03** [`8b30f56b1a`](https://github.com/vllm-project/vllm/commit/8b30f56b1a) [#65245](https://github.com/vllm-project/vllm/pull/65245)
  [Bugfix][Benchmark] Skip the client-side chat template on chat backends (#65245)
  _Files: `tests/benchmarks/test_custom_dataset_chat_template_kwargs.py`, `vllm/benchmarks/datasets/datasets.py`_
- **2026-11-03** [`61249811c1`](https://github.com/vllm-project/vllm/commit/61249811c1) [#57519](https://github.com/vllm-project/vllm/pull/57519)
  [Bugfix][Benchmark] Fail streams that end in a server error event (#57519)
  _Files: `benchmarks/backend_request_func.py`, `tests/benchmarks/test_endpoint_request_func_timing.py`, `vllm/benchmarks/lib/endpoint_request_func.py`_
- **2026-11-02** [`bb197a852f`](https://github.com/vllm-project/vllm/commit/bb197a852f) [#61680](https://github.com/vllm-project/vllm/pull/61680)
  [Perf][HiSparse] Segment host KV pool backing files (#61680)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `tests/v1/worker/test_utils.py`, `vllm/v1/hisparse/runtime.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py` _+1 more__
- **2026-11-02** [`f48cc6262e`](https://github.com/vllm-project/vllm/commit/f48cc6262e) [#65083](https://github.com/vllm-project/vllm/pull/65083)
  [Bugfix][Benchmark] Keep numeric-string prompts as strings in CustomDataset (#65083)
  _Files: `tests/benchmarks/test_custom_dataset_seed.py`, `vllm/benchmarks/datasets/datasets.py`_

## Speculative Decoding  (15 commits)

- **2026-11-09** [`931a0d5ba4`](https://github.com/vllm-project/vllm/commit/931a0d5ba4) [#60390](https://github.com/vllm-project/vllm/pull/60390)
  [Model][Core] Share the CPU-offloaded Qwen4Exp PLE table across co-located DP replicas (#60390)
  _Files: `docs/features/engram.md`, `tests/distributed/test_engram_dp_shard.py`, `tests/models/qwen4_exp/test_ple.py`, `vllm/distributed/parallel_state.py` _+3 more__
- **2026-11-09** [`083fbac021`](https://github.com/vllm-project/vllm/commit/083fbac021) [#58094](https://github.com/vllm-project/vllm/pull/58094)
  [Bugfix][Spec Decode] Propagate rope hf_overrides to MTP draft (#58094)
  _Files: `tests/config/test_speculative_draft_hf_overrides.py`, `vllm/config/model.py`, `vllm/config/speculative.py`, `vllm/v1/worker/gpu/spec_decode/speculator_config.py`_
- **2026-11-07** [`0e7ce45962`](https://github.com/vllm-project/vllm/commit/0e7ce45962) [#66000](https://github.com/vllm-project/vllm/pull/66000)
  [Bugfix][Step5][Spec Decode] Skip VllmConfig re-validation for the MTP draft config (#66000)
  _Files: `tests/models/step5/test_mtp_config.py`, `vllm/config/model.py`, `vllm/config/vllm.py`, `vllm/models/step5/nvidia/mtp.py`_
- **2026-11-07** [`4683d46541`](https://github.com/vllm-project/vllm/commit/4683d46541) [#66165](https://github.com/vllm-project/vllm/pull/66165)
  [Sleep] Warn when level-2 sleep discards draft weights (#66165)
  _Files: `docs/features/sleep_mode.md`, `vllm/v1/worker/gpu_worker.py`_
- **2026-11-07** [`b4dffa5095`](https://github.com/vllm-project/vllm/commit/b4dffa5095) [#64829](https://github.com/vllm-project/vllm/pull/64829)
  [CPU][Perf] Speed up GDN speculative-decode recurrent update (#64829)
  _Files: `benchmarks/kernels/cpu/benchmark_cpu_gdn_spec.py`, `csrc/cpu/sgl-kernels/fla.cpp`, `tests/kernels/mamba/cpu/test_cpu_gdn_ops.py`_
- **2026-11-06** [`c9fce07da3`](https://github.com/vllm-project/vllm/commit/c9fce07da3) [#65270](https://github.com/vllm-project/vllm/pull/65270)
  [MRV2][Spec Decode] Fix mixed draft-model warmup token budget (#65270)
  _Files: `tests/v1/worker/test_gpu_warmup_blocks.py`, `tests/v1/worker/test_mixed_warmup_gate.py`, `vllm/model_executor/warmup/step5_dsa_warmup.py`, `vllm/v1/worker/gpu/model_runner.py` _+2 more__
- **2026-11-06** [`b67e3a1830`](https://github.com/vllm-project/vllm/commit/b67e3a1830) [#63304](https://github.com/vllm-project/vllm/pull/63304)
  [Frontend] Remove dead helpers and sync type annotations in entrypoints and config (#63304)
  _Files: `docs/serving/online_serving/openai_compatible_server.md`, `vllm/config/speculative.py`, `vllm/entrypoints/common/cli_args.py`, `vllm/entrypoints/generate/base/serving.py` _+5 more__
- **2026-11-06** [`3f34cac035`](https://github.com/vllm-project/vllm/commit/3f34cac035) [#65816](https://github.com/vllm-project/vllm/pull/65816)
  [Bugfix][DeepSeek-V4] Share the target embedding with the MTP drafter under PP (#65816)
  _Files: `tests/models/test_registry.py`, `vllm/models/deepseek_v4/nvidia/mtp.py`_
- **2026-11-06** [`4593e73c85`](https://github.com/vllm-project/vllm/commit/4593e73c85) [#65710](https://github.com/vllm-project/vllm/pull/65710)
  [Bugfix][Structured Output] Handle EOS in speculative Guidance batches (#65710)
  _Files: `tests/entrypoints/llm/test_struct_output_generate.py`, `tests/v1/structured_output/test_backend_guidance.py`, `vllm/v1/structured_output/backend_guidance.py`_
- **2026-11-04** [`20d7dd9ac1`](https://github.com/vllm-project/vllm/commit/20d7dd9ac1) [#65449](https://github.com/vllm-project/vllm/pull/65449)
  [Bugfix][Spec Decode] Initialize Mistral EAGLE weight-loader state (#65449)
  _Files: `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`_
- **2026-11-03** [`ab9f51f101`](https://github.com/vllm-project/vllm/commit/ab9f51f101) [#65439](https://github.com/vllm-project/vllm/pull/65439)
  [CI][Tests] Remove timing dependence from Engram prefetch synchronization test (#65439)
  _Files: `tests/kernels/test_engram.py`_
- **2026-11-03** [`bf45b38f0d`](https://github.com/vllm-project/vllm/commit/bf45b38f0d) [#65125](https://github.com/vllm-project/vllm/pull/65125)
  [Bugfix][Spec Decode] Muse Spark DSpark: initialize _context_kv_proj so the draft loads (#65125)
  _Files: `tests/transformers_utils/test_muse_spark_config.py`, `vllm/models/muse_spark/common/dspark.py`_
- **2026-11-03** [`44e70e086a`](https://github.com/vllm-project/vllm/commit/44e70e086a) [#65175](https://github.com/vllm-project/vllm/pull/65175)
  [Spec Decode] Support XPress + Acceptance Estimator (#65175)
  _Files: `docs/features/speculative_decoding/adaptive_verification.md`, `tests/v1/e2e/spec_decode/acceptance_rates/xpress/test_xpress.py`, `tests/v1/e2e/spec_decode/draft_model/test_draft_model.py`, `tests/v1/spec_decode/test_xpress_head.py` _+2 more__
- **2026-11-03** [`190df0b900`](https://github.com/vllm-project/vllm/commit/190df0b900) [#60339](https://github.com/vllm-project/vllm/pull/60339)
  [Spec Decode][MRV2] Suffix decoding speculator for Model Runner V2 (#60339)
  _Files: `docs/features/speculative_decoding/README.md`, `docs/features/speculative_decoding/adaptive_verification.md`, `docs/features/speculative_decoding/suffix.md`, `tests/test_config.py` _+16 more__
- **2026-11-02** [`f451c6254f`](https://github.com/vllm-project/vllm/commit/f451c6254f) [#63870](https://github.com/vllm-project/vllm/pull/63870)
  [Rust Frontend][gRPC] Separate liveness from inference readiness (#63870)
  _Files: `docs/deployment/k8s.md`, `rust/README.md`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs` _+13 more__

## LoRA  (11 commits)

- **2026-11-09** [`7841981e7a`](https://github.com/vllm-project/vllm/commit/7841981e7a) [#66413](https://github.com/vllm-project/vllm/pull/66413)
  [Transformers backend] Support LoRA on lm_head and on any input embedding name (#66413)
  _Files: `tests/lora/test_llama_tp.py`, `tests/lora/test_transformers_model.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/transformers/base.py` _+1 more__
- **2026-11-06** [`d5486971ea`](https://github.com/vllm-project/vllm/commit/d5486971ea) [#64681](https://github.com/vllm-project/vllm/pull/64681)
  [Bugfix][LoRA] Give Mamba-1 LoRA layers every row of the batch (#64681)
  _Files: `vllm/model_executor/layers/mamba/mamba_mixer.py`_
- **2026-11-06** [`5b698ca44a`](https://github.com/vllm-project/vllm/commit/5b698ca44a) [#57851](https://github.com/vllm-project/vllm/pull/57851)
  [Bugfix][LoRA] Handle leading missing packed groups (#57851)
  _Files: `tests/lora/test_layers.py`, `vllm/lora/layers/column_parallel_linear.py`_
- **2026-11-05** [`0f09cebe09`](https://github.com/vllm-project/vllm/commit/0f09cebe09) [#65850](https://github.com/vllm-project/vllm/pull/65850)
  [Rust Frontend] Add the max_lora label to vllm:lora_requests_info (#65850)
  _Files: `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/metrics.rs`, `rust/src/metrics/src/scheduler.rs`_
- **2026-11-04** [`541556886c`](https://github.com/vllm-project/vllm/commit/541556886c) [#65302](https://github.com/vllm-project/vllm/pull/65302)
  [Model] Add ZAYA1 support (#65302)
  _Files: `docs/features/reasoning_outputs.md`, `docs/features/tool_calling.md`, `docs/models/supported_models.md`, `tests/models/language/generation/test_hybrid.py` _+11 more__
- **2026-11-03** [`8eff67c67a`](https://github.com/vllm-project/vllm/commit/8eff67c67a) [#65216](https://github.com/vllm-project/vllm/pull/65216)
  [Frontend] Add granite_toolcall_parser for Granite 4.2 tool calling (#65216)
  _Files: `docs/features/tool_calling.md`, `tests/tool_parsers/test_granite_toolcall_parser.py`, `vllm/parser/engine/registered_adapters.py`, `vllm/parser/granite_toolcall.py` _+2 more__
- **2026-11-03** [`43b8d05710`](https://github.com/vllm-project/vllm/commit/43b8d05710) [#60213](https://github.com/vllm-project/vllm/pull/60213)
  [Metrics][Frontend] Expose request render duration metric (#60213)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat_error.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/completion/test_completion_error.py`, `tests/entrypoints/openai/completion/test_lora_resolvers.py` _+6 more__
- **2026-11-03** [`0acdae3ec5`](https://github.com/vllm-project/vllm/commit/0acdae3ec5) [#61162](https://github.com/vllm-project/vllm/pull/61162)
  [Bugfix][MRV2][LoRA] Disable KV-sharing fast prefill for LoRA batches (#61162)
  _Files: `tests/v1/worker/test_attn_utils.py`, `vllm/config/cache.py`, `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-11-03** [`b7486648bb`](https://github.com/vllm-project/vllm/commit/b7486648bb) [#62470](https://github.com/vllm-project/vllm/pull/62470)
  [Bugfix][LoRA] Scale embedding LoRA deltas by the base layer's embed_scale (#62470)
  _Files: `tests/lora/test_layers.py`, `vllm/lora/layers/vocab_parallel_embedding.py`_
- **2026-11-02** [`eecf8dbb2b`](https://github.com/vllm-project/vllm/commit/eecf8dbb2b) [#64616](https://github.com/vllm-project/vllm/pull/64616)
  [Bugfix][LoRA] Fix KeyError crash when a LoRA name is reloaded with requests in flight (#64616)
  _Files: `tests/lora/test_lora_functions.py`, `vllm/lora/request.py`_
- **2026-11-02** [`08e3f26458`](https://github.com/vllm-project/vllm/commit/08e3f26458) [#65008](https://github.com/vllm-project/vllm/pull/65008)
  [CI] Lower gpu_memory_utilization in test_gemma4_lora (#65008)
  _Files: `tests/lora/test_gemma4_tp.py`_

## Docs  (10 commits)

- **2026-11-09** [`9922c0ced3`](https://github.com/vllm-project/vllm/commit/9922c0ced3) [#66092](https://github.com/vllm-project/vllm/pull/66092)
  [Doc] Raise the bar for in-tree kernel translation units (#66092)
  _Files: `.agents/skills/pr-checklist/SKILL.md`, `AGENTS.md`, `csrc/AGENTS.md`_
- **2026-11-08** [`cf5cea2da3`](https://github.com/vllm-project/vllm/commit/cf5cea2da3) [#56508](https://github.com/vllm-project/vllm/pull/56508)
  [Test][EC Connector] Add the no-NIXL import test the docs refer to (#56508)
  _Files: `docs/features/ec_cpu_connector.md`, `tests/v1/ec_connector/unit/test_no_nixl_imports.py`_
- **2026-11-07** [`d90f5573a3`](https://github.com/vllm-project/vllm/commit/d90f5573a3) [#64588](https://github.com/vllm-project/vllm/pull/64588)
  [Doc][Recipe] MiMo-V2.5-Pro: split fused --max-model-len base arg (#64588)
  _Files: `recipes/models/XiaomiMiMo/MiMo-V2.5-Pro.yaml`_
- **2026-11-06** [`047f6bfbb2`](https://github.com/vllm-project/vllm/commit/047f6bfbb2) [#66123](https://github.com/vllm-project/vllm/pull/66123)
  [Bugfix] Preserve embedding size overrides (#66123)
  _Files: `docs/models/pooling_models/embed.md`, `vllm/config/model.py`_
- **2026-11-06** [`3cd3a7ad1c`](https://github.com/vllm-project/vllm/commit/3cd3a7ad1c) [#66062](https://github.com/vllm-project/vllm/pull/66062)
  [Doc][Bugfix] Fix strict docs build broken by subclassing mocked torch classes (#66062)
  _Files: `docs/mkdocs/gen_files/generate_argparse.py`_
- **2026-11-06** [`441a9755dd`](https://github.com/vllm-project/vllm/commit/441a9755dd) [#65557](https://github.com/vllm-project/vllm/pull/65557)
  [Doc] Add vllm-iluvatar core Gpu to the Vllm support list (#65557)
  _Files: `README.md`, `docs/README.md`_
- **2026-11-05** [`33d64b68fa`](https://github.com/vllm-project/vllm/commit/33d64b68fa) [#65679](https://github.com/vllm-project/vllm/pull/65679)
  [Bugfix] Require fastokens >= 0.3.5 for VLLM_USE_FASTOKENS (#65679)
  _Files: `docs/configuration/optimization.md`, `recipes/models/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16.yaml`, `vllm/envs.py`, `vllm/tokenizers/fastokens.py`_
- **2026-11-04** [`7fcb4dffd3`](https://github.com/vllm-project/vllm/commit/7fcb4dffd3) [#64551](https://github.com/vllm-project/vllm/pull/64551)
  [Bugfix][Rust Frontend] Reject --dataset-path with synthetic vllm-bench datasets (#64551)
  _Files: `rust/src/bench/README.md`, `rust/src/bench/src/cli.rs`, `rust/src/bench/src/config.rs`_
- **2026-11-03** [`33f68ea7fb`](https://github.com/vllm-project/vllm/commit/33f68ea7fb) [#65292](https://github.com/vllm-project/vllm/pull/65292)
  [Doc] Point to the vllm-state-transition-verifier branch from the NCCL weight transfer docs (#65292)
  _Files: `docs/training/rlhf.md`, `docs/training/weight_checker.md`, `docs/training/weight_transfer/README.md`, `docs/training/weight_transfer/nccl.md`_
- **2026-11-03** [`c67dcaab6f`](https://github.com/vllm-project/vllm/commit/c67dcaab6f) [#65199](https://github.com/vllm-project/vllm/pull/65199)
  [Docs] List the Nemotron-3-Diarization plugin (#65199)
  _Files: `docs/models/supported_models.md`_

## Compilation / CUDA Graph  (3 commits)

- **2026-11-06** [`74bb7664f7`](https://github.com/vllm-project/vllm/commit/74bb7664f7) [#64622](https://github.com/vllm-project/vllm/pull/64622)
  [Startup] Skip the CUDA graph memory profile when its estimate is disabled (#64622)
  _Files: `tests/v1/worker/test_gpu_worker.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-11-03** [`40941f2c4b`](https://github.com/vllm-project/vllm/commit/40941f2c4b) [#65091](https://github.com/vllm-project/vllm/pull/65091)
  [Bugfix][CI/Build] Use compilation config to control breakable cuda graph (#65091)
  _Files: `tests/conftest.py`, `tests/test_config.py`, `tests/v1/e2e/spec_decode/test_sharded_sampling.py`, `vllm/compilation/breakable_cudagraph.py` _+8 more__
- **2026-11-02** [`b18775f893`](https://github.com/vllm-project/vllm/commit/b18775f893) [#62560](https://github.com/vllm-project/vllm/pull/62560)
  [Core][MRV2] Warm up the sampler after CUDA graph capture to stop memory growth under load (#62560)
  _Files: `vllm/v1/worker/gpu_worker.py`_

## Distributed  (2 commits)

- **2026-11-04** [`213e64562b`](https://github.com/vllm-project/vllm/commit/213e64562b) [#65537](https://github.com/vllm-project/vllm/pull/65537)
  [MiniMax-M3] Support sequence parallelism with pipeline parallelism (#65537)
  _Files: `vllm/models/minimax_m3/nvidia/model.py`_
- **2026-11-04** [`ba2d99fd4a`](https://github.com/vllm-project/vllm/commit/ba2d99fd4a) [#57042](https://github.com/vllm-project/vllm/pull/57042)
  [Kernel] Accumulate ranks in absolute order in 2-stage custom all-reduce (#57042)
  _Files: `csrc/custom_all_reduce.cuh`, `docs/features/batch_invariance.md`, `tests/distributed/test_custom_all_reduce.py`, `vllm/model_executor/determinism/batch_invariant.py`_

---
_Generated 2026-11-09 18:47 UTC_