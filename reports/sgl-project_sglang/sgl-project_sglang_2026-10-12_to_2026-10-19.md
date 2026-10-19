# sgl-project/sglang — Weekly Change Report
**Period:** 2026-10-12 → 2026-10-19  |  **Total commits:** 516

## ✨ New Features This Week

- **2026-10-19** [#42557](https://github.com/sgl-project/sglang/pull/42557) — [Feat] paged-experts: Serve MoE models whose weights do not fit VRAM (#42557)
- **2026-10-19** [#44402](https://github.com/sgl-project/sglang/pull/44402) — [Feat] sgl-router: Add --decode-dispatch-limit to pick decode DP ranks near KV arrival (#44402)
- **2026-10-19** [#44518](https://github.com/sgl-project/sglang/pull/44518) — [Feat] nemotron: Port Nemotron 3.5 Super serving changes (#44518)
- **2026-10-19** [#36632](https://github.com/sgl-project/sglang/pull/36632) — [Feat] [CPU] model: Support LTX and MOVA models on CPU (#36632)
- **2026-10-19** [#44624](https://github.com/sgl-project/sglang/pull/44624) — [Feat] [CPU] model: Support Muse models on CPU (#44624)
- **2026-10-19** [#44996](https://github.com/sgl-project/sglang/pull/44996) — [CI] diffusion: tighten H100 baselines and enable B200 performance checks (#44996)
- **2026-10-19** [#43345](https://github.com/sgl-project/sglang/pull/43345) — [Perf] [XPU] server_args: Enable fused QK-norm + RoPE by default (#43345)
- **2026-10-19** [#45050](https://github.com/sgl-project/sglang/pull/45050) — [Feat] dsv4.1: Return prompt logprobs under encoder SWA bounded replay (#45050)
- **2026-10-19** [#41675](https://github.com/sgl-project/sglang/pull/41675) — [CI] [NPU] tests: Reduce HiCache sizes and enable expandable pinned memory in focused tests (#41675)
- **2026-10-19** [#42118](https://github.com/sgl-project/sglang/pull/42118) — [Feat] rust/grpc: Add ListModels, Detokenize, and Abort to api.v1 (#42118)
- _…and 106 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-19** [`7c4cc5a51c`](https://github.com/sgl-project/sglang/commit/7c4cc5a51c) [#41229](https://github.com/sgl-project/sglang/pull/41229) — [Perf] [AMD] attention: Spread uneven Triton decode batches across XCDs (#41229)
- **2026-10-19** [`a90e9c5dd8`](https://github.com/sgl-project/sglang/commit/a90e9c5dd8) [#44443](https://github.com/sgl-project/sglang/pull/44443) — [Fix] [AMD] mhc: Bound the Triton fused post+pre buffer cache (#44443)
- **2026-10-19** [`8111841103`](https://github.com/sgl-project/sglang/commit/8111841103) [#43733](https://github.com/sgl-project/sglang/pull/43733) — [Perf] deepseek-v4.1: Replay the breakable prefill CUDA graph at any context length (#43733)
- **2026-10-19** [`5d9c956f8e`](https://github.com/sgl-project/sglang/commit/5d9c956f8e) [#45070](https://github.com/sgl-project/sglang/pull/45070) — [Doc] [AMD] dsv4: Update amd cookbook 1016 (#45070)
- **2026-10-19** [`3d588779e1`](https://github.com/sgl-project/sglang/commit/3d588779e1) [#40674](https://github.com/sgl-project/sglang/pull/40674) — [CI] [AMD] test: Run UMBP HiCache E2E through standalone DRAM server (#40674)
- **2026-10-19** [`8d3eee46a7`](https://github.com/sgl-project/sglang/commit/8d3eee46a7) [#44927](https://github.com/sgl-project/sglang/pull/44927) — [Perf] [AMD] deepseek-v4: Skip top-k refinement for proven positive-zero ties (#44927)
- **2026-10-18** [`e9b22a0818`](https://github.com/sgl-project/sglang/commit/e9b22a0818) [#44601](https://github.com/sgl-project/sglang/pull/44601) — [Perf] [AMD] monokernels: Let a plugin skip per-step attention metadata (#44601)
- **2026-10-18** [`a5b21145e1`](https://github.com/sgl-project/sglang/commit/a5b21145e1) [#44969](https://github.com/sgl-project/sglang/pull/44969) — [Refactor] attention: Separate decode metadata from pool ownership (#44969)
- **2026-10-18** [`f1cf2e1005`](https://github.com/sgl-project/sglang/commit/f1cf2e1005) [#44412](https://github.com/sgl-project/sglang/pull/44412) — [Fix] [AMD] mori: Look up elided DSA state entries by the paired dst index (#44412)
- **2026-10-18** [`396e97e5dd`](https://github.com/sgl-project/sglang/commit/396e97e5dd) [#44409](https://github.com/sgl-project/sglang/pull/44409) — [CI] [AMD] ci/slurm: Add a Mooncake KV-transfer test to the MI355X disaggregation nightly (#44409)
- **2026-10-18** [`8a4239fbdc`](https://github.com/sgl-project/sglang/commit/8a4239fbdc) [#44404](https://github.com/sgl-project/sglang/pull/44404) — [Fix] [AMD] mooncake: Bump Mooncake to v0.3.14-rc1 for cross-node KV transfer (#44404)
- **2026-10-18** [`f96a7326e6`](https://github.com/sgl-project/sglang/commit/f96a7326e6) [#43952](https://github.com/sgl-project/sglang/pull/43952) — [Fix] [AMD] diffusion: Prevent ComponentResidencyError after compile warmup (#43952)
- **2026-10-18** [`00f6cdcd1b`](https://github.com/sgl-project/sglang/commit/00f6cdcd1b) [#44089](https://github.com/sgl-project/sglang/pull/44089) — [Fix] [AMD] kda: Reject match_cutedsl_decode on ROCm and skip its parity tests (#44089)
- **2026-10-18** [`3626978a13`](https://github.com/sgl-project/sglang/commit/3626978a13) [#43991](https://github.com/sgl-project/sglang/pull/43991) — [Fix] [AMD] kda: Match the fused verify Q/K norm to its reference kernel (#43991)
- **2026-10-18** [`e5dc10e73b`](https://github.com/sgl-project/sglang/commit/e5dc10e73b) [#44903](https://github.com/sgl-project/sglang/pull/44903) — [Doc] [AMD] dsv41: Update amd cookbook 1016 (#44903)
- **2026-10-18** [`d20d010574`](https://github.com/sgl-project/sglang/commit/d20d010574) [#44948](https://github.com/sgl-project/sglang/pull/44948) — [Fix] deepseek-v4.1: Exchange late-layer DP row counts before the forward (#44948)
- **2026-10-17** [`563cd60345`](https://github.com/sgl-project/sglang/commit/563cd60345) [#44934](https://github.com/sgl-project/sglang/pull/44934) — [Fix] [AMD] deepseek-v4.1: Reject attention DP with encoder SWA bounded replay on ROCm (#44934)
- **2026-10-17** [`05ce0e980f`](https://github.com/sgl-project/sglang/commit/05ce0e980f) [#42901](https://github.com/sgl-project/sglang/pull/42901) — [Perf] deepseek-v4.1: Skip wasted layer 20 work on earlier prompt tokens under decoder bounded replay (#42901)
- **2026-10-17** [`a2953d7b7f`](https://github.com/sgl-project/sglang/commit/a2953d7b7f) [#44850](https://github.com/sgl-project/sglang/pull/44850) — [Fix] deepseek-v4.1: Serve prompt-logprob requests under decoder SWA bounded replay (#44850)
- **2026-10-17** [`01dc08e23f`](https://github.com/sgl-project/sglang/commit/01dc08e23f) [#42787](https://github.com/sgl-project/sglang/pull/42787) — [Refactor] dsv41: Shard Engram tables on hash-column boundaries (#42787)
- **2026-10-17** [`3603824541`](https://github.com/sgl-project/sglang/commit/3603824541) [#44403](https://github.com/sgl-project/sglang/pull/44403) — [Perf] DSv4.1: Enable decoder bounded replay by default (#44403)
- **2026-10-16** [`80c54e6ac5`](https://github.com/sgl-project/sglang/commit/80c54e6ac5) [#42716](https://github.com/sgl-project/sglang/pull/42716) — [Fix] [AMD] hicache: Serve encoder-replay prefix hits with a paged DSpark draft SWA (#42716)
- **2026-10-16** [`ed2ebad342`](https://github.com/sgl-project/sglang/commit/ed2ebad342) [#44454](https://github.com/sgl-project/sglang/pull/44454) — [Doc] [AMD] cookbook: Refresh DeepSeek V4 AgentX PD recipe optimizations (#44454)
- **2026-10-16** [`4afae5568b`](https://github.com/sgl-project/sglang/commit/4afae5568b) [#44657](https://github.com/sgl-project/sglang/pull/44657) — [Perf] [AMD] dsv4: Add a separate MegaMoE decode instance (#44657)
- **2026-10-16** [`2adc76ad61`](https://github.com/sgl-project/sglang/commit/2adc76ad61) [#41903](https://github.com/sgl-project/sglang/pull/41903) — [Perf] [AMD] dsv4: reuse the q_lora fp8 quant for the C4 indexer wq_b (4/8) (#41903)
- **2026-10-16** [`9246acd462`](https://github.com/sgl-project/sglang/commit/9246acd462) [#44620](https://github.com/sgl-project/sglang/pull/44620) — [CI] [AMD] aiter: pin aiter commit to 2bb549 for rocm10.1 gfx1250 (#44620)
- **2026-10-16** [`baf451fcd6`](https://github.com/sgl-project/sglang/commit/baf451fcd6) [#44008](https://github.com/sgl-project/sglang/pull/44008) — [Perf] [AMD] dsv4: carry aiter DSv4 GEMM tuned rows and mHC tile_m=16 until aiter ships them (7/8) (#44008)
- **2026-10-16** [`f05da43d44`](https://github.com/sgl-project/sglang/commit/f05da43d44) [#30929](https://github.com/sgl-project/sglang/pull/30929) — [Feat] [AMD] disagg: Support DSV4 decode radix cache on ROCm unified KV (bf16/fp8, DSpark) (#30929)
- **2026-10-16** [`42eb556e66`](https://github.com/sgl-project/sglang/commit/42eb556e66) [#44007](https://github.com/sgl-project/sglang/pull/44007) — [Perf] [AMD] dsv4: optional e8m0 mxscale GEMM for dense 128x128 fp8 linears (6/8) (#44007)
- **2026-10-16** [`6efc96abf9`](https://github.com/sgl-project/sglang/commit/6efc96abf9) [#44006](https://github.com/sgl-project/sglang/pull/44006) — [Perf] [AMD] dsv4: FP4 indexer on aiter's row-group kernel for decode and target-verify (5/8) (#44006)
- **2026-10-16** [`9fde8bcc46`](https://github.com/sgl-project/sglang/commit/9fde8bcc46) [#44004](https://github.com/sgl-project/sglang/pull/44004) — [Perf] [AMD] moe: small-batch sort with histogram + bitonic sort for 32 < P <= 256 (3/8) (#44004)
- **2026-10-16** [`f0ff18353d`](https://github.com/sgl-project/sglang/commit/f0ff18353d) [#44003](https://github.com/sgl-project/sglang/pull/44003) — [Perf] [AMD] dsv4: fp8 verify writes the SWA ring in the fused norm/rope kernel (2/8) (#44003)
- **2026-10-16** [`ab5858ac8a`](https://github.com/sgl-project/sglang/commit/ab5858ac8a) [#44016](https://github.com/sgl-project/sglang/pull/44016) — [Perf] [AMD] dsv4: fp8 unified_kv decode/verify on FlyDSL v4 nm decode with a latency-model split plan (1/8) (#44016)
- **2026-10-16** [`536cdb4b04`](https://github.com/sgl-project/sglang/commit/536cdb4b04) [#44621](https://github.com/sgl-project/sglang/pull/44621) — [Feat] [AMD] docker: Install the sgl-amd-mono monokernel plugin in the ROCm image (#44621)
- **2026-10-16** [`fad7d95a7f`](https://github.com/sgl-project/sglang/commit/fad7d95a7f) [#44673](https://github.com/sgl-project/sglang/pull/44673) — [Fix] deepseek-v4.1: Keep the DSpark draft SWA out of the radix tree (#44673)
- **2026-10-16** [`bdc4ec15ce`](https://github.com/sgl-project/sglang/commit/bdc4ec15ce) [#44405](https://github.com/sgl-project/sglang/pull/44405) — [Perf] [AMD] dspark: No per-step host sync in decode (1/4) (#44405)
- **2026-10-16** [`a448fdf316`](https://github.com/sgl-project/sglang/commit/a448fdf316) [#44267](https://github.com/sgl-project/sglang/pull/44267) — [Perf] [AMD] qwen3: Fuse QK-norm + RoPE + KV cache write for dense Qwen3 decode (#44267)
- **2026-10-16** [`ed8c3139f1`](https://github.com/sgl-project/sglang/commit/ed8c3139f1) [#41303](https://github.com/sgl-project/sglang/pull/41303) — [Fix] deepseek-v4.1: Keep the full SWA window for short bounded-replay extends (#41303)
- **2026-10-15** [`4cca7fcd3e`](https://github.com/sgl-project/sglang/commit/4cca7fcd3e) [#44590](https://github.com/sgl-project/sglang/pull/44590) — chore: bump sgl-kernel version to 0.4.10 (#44590)
- **2026-10-15** [`ec7ab9d0c2`](https://github.com/sgl-project/sglang/commit/ec7ab9d0c2) [#44353](https://github.com/sgl-project/sglang/pull/44353) — [Feat] [AMD] monokernels: one runtime switch for vendor monokernel plugins (#44353)
- **2026-10-15** [`bba535ebb4`](https://github.com/sgl-project/sglang/commit/bba535ebb4) [#44534](https://github.com/sgl-project/sglang/pull/44534) — [Fix] [AMD] docker: Repair the AITER build step after the 2bb549102 pin bump (#44534)
- **2026-10-15** [`5ef8319f16`](https://github.com/sgl-project/sglang/commit/5ef8319f16) [#27702](https://github.com/sgl-project/sglang/pull/27702) — [Perf] [AMD] attention: Enable diffusion BF16 attention and MXFP4 compilation (#27702)
- **2026-10-15** [`e87e32b311`](https://github.com/sgl-project/sglang/commit/e87e32b311) [#42699](https://github.com/sgl-project/sglang/pull/42699) — [Feat] [AMD] docker: Release ROCm 10.1 for gfx1250 in parallel with ROCm 10.0 (#42699)
- **2026-10-15** [`2f5407da28`](https://github.com/sgl-project/sglang/commit/2f5407da28) [#44266](https://github.com/sgl-project/sglang/pull/44266) — [Fix] [AMD] qwen3: Fix KV cache write in the fused QK-norm + mRoPE decode path (#44266)
- **2026-10-15** [`2092160d42`](https://github.com/sgl-project/sglang/commit/2092160d42) [#41988](https://github.com/sgl-project/sglang/pull/41988) — [AMD][Diffusion] Route unquantized linears through aiter tgemm on gfx1250 (#41988)
- **2026-10-15** [`f7ad4345b8`](https://github.com/sgl-project/sglang/commit/f7ad4345b8) [#43607](https://github.com/sgl-project/sglang/pull/43607) — [Refactor] deepseek-v4: Use explicit stage boundaries and row transport (#43607)
- **2026-10-15** [`71a17dbc24`](https://github.com/sgl-project/sglang/commit/71a17dbc24) [#42148](https://github.com/sgl-project/sglang/pull/42148) — [AMD][CI] setup: Skip redundant pip-cache chown walk and MORI rebuild (#42148)
- **2026-10-15** [`28703575f9`](https://github.com/sgl-project/sglang/commit/28703575f9) [#44379](https://github.com/sgl-project/sglang/pull/44379) — [AMD] Update ROCm AITER pin to 2bb549102 (#44379)
- **2026-10-15** [`676c038aa5`](https://github.com/sgl-project/sglang/commit/676c038aa5) [#40657](https://github.com/sgl-project/sglang/pull/40657) — [diffusion] fix: fix the load duration missing from subclassed server tests (#40657)
- **2026-10-15** [`4dc9b5c68c`](https://github.com/sgl-project/sglang/commit/4dc9b5c68c) [#44311](https://github.com/sgl-project/sglang/pull/44311) — [Test] [AMD] diffusion: Expect CUDA-only fast paths to be off on ROCm in kernel tests (#44311)
- **2026-10-15** [`4851d182a1`](https://github.com/sgl-project/sglang/commit/4851d182a1) [#44368](https://github.com/sgl-project/sglang/pull/44368) — [Doc][AMD] Update v41 amd cookbook 1015 (#44368)
- **2026-10-15** [`a12814c158`](https://github.com/sgl-project/sglang/commit/a12814c158) [#43643](https://github.com/sgl-project/sglang/pull/43643) — [Perf] [AMD] dsa: Enable the gfx950 fused DSA indexer for block-FP8 wq_b/wk (#43643)
- **2026-10-15** [`c5c4bbbd25`](https://github.com/sgl-project/sglang/commit/c5c4bbbd25) [#43642](https://github.com/sgl-project/sglang/pull/43642) — [Perf] [AMD] dsa: Run DSA prefill under breakable CUDA graphs on HIP (#43642)
- **2026-10-15** [`8333ccfccb`](https://github.com/sgl-project/sglang/commit/8333ccfccb) [#43770](https://github.com/sgl-project/sglang/pull/43770) — [Fix] [AMD] diffusion: Compare ReduceOp by identity so the compiled TP all-reduce stays one graph (#43770)
- **2026-10-14** [`d3dc14eb38`](https://github.com/sgl-project/sglang/commit/d3dc14eb38) [#40857](https://github.com/sgl-project/sglang/pull/40857) — [mem_cache][PD] Fix decode radix cache ownership and allow EAGLE/EAGLE3 with decode radix cache (#40857)
- **2026-10-14** [`1737251730`](https://github.com/sgl-project/sglang/commit/1737251730) [#44096](https://github.com/sgl-project/sglang/pull/44096) — [Test] [AMD] diffusion: Run the IPC all-to-all transport tests only on CUDA (#44096)
- **2026-10-14** [`c54ba66cd4`](https://github.com/sgl-project/sglang/commit/c54ba66cd4) [#43639](https://github.com/sgl-project/sglang/pull/43639) — [Perf] Enable native MXFP4 routing and CuTeDSL fusion for MiMo (#43639)
- **2026-10-14** [`6f646563a2`](https://github.com/sgl-project/sglang/commit/6f646563a2) [#40660](https://github.com/sgl-project/sglang/pull/40660) — [AMD] diffusion: expect the residual-gate fast path to be off on ROCm in test_modulate (#40660)
- **2026-10-14** [`0d130f1915`](https://github.com/sgl-project/sglang/commit/0d130f1915) [#39724](https://github.com/sgl-project/sglang/pull/39724) — [Qwen3.8 CP 4/4] Prefill context parallel E2E support of Qwen3.8 (#39724)
- **2026-10-14** [`e29eee18df`](https://github.com/sgl-project/sglang/commit/e29eee18df) [#43945](https://github.com/sgl-project/sglang/pull/43945) — [AMD][DI][CI] nightly mi355x disagg: stage packed logs under RUNNER_TEMP, not /tmp (#43945)
- **2026-10-14** [`7e226b1b71`](https://github.com/sgl-project/sglang/commit/7e226b1b71) [#43640](https://github.com/sgl-project/sglang/pull/43640) — [AMD] Use the preallocated EAGLE topk=1 draft chain on HIP (#43640)
- **2026-10-13** [`8bf145d119`](https://github.com/sgl-project/sglang/commit/8bf145d119) [#43735](https://github.com/sgl-project/sglang/pull/43735) — [DCP] Decode context parallelism for DSA (GLM-5.2 / GLM-5.3) with MTP (#43735)
- **2026-10-13** [`e9400c5a8f`](https://github.com/sgl-project/sglang/commit/e9400c5a8f) [#43985](https://github.com/sgl-project/sglang/pull/43985) — [AMD][DI][CI] kimik26 2p1d-ep16: capture CUDA graph on decode (eager decode is slow) (#43985)
- **2026-10-13** [`96f519e4fa`](https://github.com/sgl-project/sglang/commit/96f519e4fa) [#43977](https://github.com/sgl-project/sglang/pull/43977) — [AMD][DI][CI] glm52 2p1d-ep16: capture CUDA graph on decode (eager decode is too slow) (#43977)
- **2026-10-13** [`aa15b06abe`](https://github.com/sgl-project/sglang/commit/aa15b06abe) [#43928](https://github.com/sgl-project/sglang/pull/43928) — [AMD][CI] Run test_tracing.py in the extra tier, matching CUDA (#43928)
- **2026-10-13** [`e0c957e222`](https://github.com/sgl-project/sglang/commit/e0c957e222) [#41769](https://github.com/sgl-project/sglang/pull/41769) — [HiCache][PD] Allow DSA index-K elision under HiCache and disaggregation (#41769)
- **2026-10-13** [`50a144057c`](https://github.com/sgl-project/sglang/commit/50a144057c) [#37358](https://github.com/sgl-project/sglang/pull/37358) — [AMD][PD] enable mori transfer for PD decode DCP (#37358)
- **2026-10-13** [`603a05e6c0`](https://github.com/sgl-project/sglang/commit/603a05e6c0) [#43328](https://github.com/sgl-project/sglang/pull/43328) — [ROCm][Spec] Route NGRAM tree reconstruction to the JIT kernel on HIP (#43328)
- **2026-10-13** [`fc404bbbb3`](https://github.com/sgl-project/sglang/commit/fc404bbbb3) [#43944](https://github.com/sgl-project/sglang/pull/43944) — [AMD][DI][CI] dsv4pro-fp8 2p1d-ep16-mtp: raise prefill mem fraction for MORI EP v2 memory (#43944)
- **2026-10-13** [`a69e893b1a`](https://github.com/sgl-project/sglang/commit/a69e893b1a) [#42911](https://github.com/sgl-project/sglang/pull/42911) — [AMD] Fuse prefill index-Q RoPE fake-quant and fp4 quantize kernels in DSV4.1 (#42911)
- **2026-10-13** [`42e43cf33f`](https://github.com/sgl-project/sglang/commit/42e43cf33f) [#43793](https://github.com/sgl-project/sglang/pull/43793) — [AMD] Fix Flux2 kv-gather abort on non-contiguous K/V (#43793)
- **2026-10-13** [`43356304b4`](https://github.com/sgl-project/sglang/commit/43356304b4) [#43968](https://github.com/sgl-project/sglang/pull/43968) — [AMD][Kimi-K3] Use public FlyDSL APIs in KDA decode kernels (#43968)
- **2026-10-13** [`cda267ab0f`](https://github.com/sgl-project/sglang/commit/cda267ab0f) [#43350](https://github.com/sgl-project/sglang/pull/43350) — [diffusion] fix: keep MiniMax-H3 VAE fused norms off ROCm (#43350)
- **2026-10-13** [`c2dfd5d3d6`](https://github.com/sgl-project/sglang/commit/c2dfd5d3d6) [#43962](https://github.com/sgl-project/sglang/pull/43962) — [AMD] Update v4 amd cookbook 1012 (#43962)
- **2026-10-13** [`23150f7ae0`](https://github.com/sgl-project/sglang/commit/23150f7ae0) [#43921](https://github.com/sgl-project/sglang/pull/43921) — [DSv4.1] Reduce sparse-prefill workspace padding (#43921)
- **2026-10-12** [`7224fce1b5`](https://github.com/sgl-project/sglang/commit/7224fce1b5) [#41980](https://github.com/sgl-project/sglang/pull/41980) — [AMD] Recalibrate test_quark_mxfp4 GSM8K thresholds to observed MI355X noise (#41980)
- **2026-10-12** [`6781da8e5b`](https://github.com/sgl-project/sglang/commit/6781da8e5b) [#43834](https://github.com/sgl-project/sglang/pull/43834) — [AMD] [Docker] Update MoRI to v1.2.4 (#43834)
- **2026-10-12** [`64cffed139`](https://github.com/sgl-project/sglang/commit/64cffed139) [#43836](https://github.com/sgl-project/sglang/pull/43836) — [AMD] Fix test_compact_attention_hip.py CI (#43836)
- **2026-10-12** [`d6853f5066`](https://github.com/sgl-project/sglang/commit/d6853f5066) [#43803](https://github.com/sgl-project/sglang/pull/43803) — [AMD] Add flydsl mxfp8 dense gemm kernel for dpsk v4.1 prefill (#43803)
- **2026-10-12** [`6c2a682b59`](https://github.com/sgl-project/sglang/commit/6c2a682b59) [#41793](https://github.com/sgl-project/sglang/pull/41793) — [AMD] Keep the FP4 varctx schedule test off AITER's 2048-row compile (#41793)
- **2026-10-12** [`6966c5d027`](https://github.com/sgl-project/sglang/commit/6966c5d027) [#42553](https://github.com/sgl-project/sglang/pull/42553) — [ROCm] Eliminate HiCache migration stalls and use exact-size host allocations (#42553)
- **2026-10-12** [`0d0be8fc98`](https://github.com/sgl-project/sglang/commit/0d0be8fc98) [#40666](https://github.com/sgl-project/sglang/pull/40666) — [AMD][MORI] Add MORI EP V2 support (#40666)
- **2026-10-12** [`37d2e5c34f`](https://github.com/sgl-project/sglang/commit/37d2e5c34f) [#43077](https://github.com/sgl-project/sglang/pull/43077) — [AMD][V4.1][*/N] Fix DP attention + TP MoE decode NaN and support bounded replay (#43077)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#37451](https://github.com/sgl-project/sglang/issues/37451) | [Failure Tracker] PR Test (AMD) | ci-failure-tracker | 2026-10-19 |
| [#42752](https://github.com/sgl-project/sglang/issues/42752) | [CI] Flaky tests and CI infrastructure failures seen while babysitting | — | 2026-10-19 |
| [#44635](https://github.com/sgl-project/sglang/issues/44635) | [RFC] Context-parallel support for the unified L3 key scheme | — | 2026-10-19 |
| [#45189](https://github.com/sgl-project/sglang/issues/45189) | [RFC]: Programmable KV Cache: Composable Policies for Agentic Serving | — | 2026-10-19 |
| [#27194](https://github.com/sgl-project/sglang/issues/27194) | moe_kernels.py, stage-2 reduce path: small SGLANG_MORI_NUM_MAX_DISPATC | inactive | 2026-10-19 |
| [#44206](https://github.com/sgl-project/sglang/issues/44206) | [Tracking][Mori] PRs for Community Review | — | 2026-10-19 |
| [#45162](https://github.com/sgl-project/sglang/issues/45162) | [Bug] PP + EAGLE/MTP: --speculative-use-block-verification / --specula | — | 2026-10-19 |
| [#43885](https://github.com/sgl-project/sglang/issues/43885) | [Roadmap] Pipeline Parallelism Roadmap (2026 Q4) | high priority | 2026-10-19 |
| [#45128](https://github.com/sgl-project/sglang/issues/45128) | [RFC] linker: Prefetch SSD-resident KV while the request is queued | — | 2026-10-19 |
| [#43098](https://github.com/sgl-project/sglang/issues/43098) | Agentic Cache Scheduling System Roadmap (Q4) | — | 2026-10-19 |
| [#43526](https://github.com/sgl-project/sglang/issues/43526) | [AMD][Bug] Accuracy issue with gfx942 block-FP8 linear AITER CK blocks | — | 2026-10-19 |
| [#44721](https://github.com/sgl-project/sglang/issues/44721) | [RFC] scheduler: Overlap prefill scheduling and KV loading with model  | — | 2026-10-19 |
| [#39963](https://github.com/sgl-project/sglang/issues/39963) | [RFC] Asymmetric P/D deployment for DeepSeek-V4.1 Flash | — | 2026-10-19 |
| [#45030](https://github.com/sgl-project/sglang/issues/45030) | [Feature]  Streamed restore: chunked materialization for oversized sto | — | 2026-10-18 |
| [#45014](https://github.com/sgl-project/sglang/issues/45014) | [Bug] Unauthenticated Mooncake STAGING_RSP chunk index causes Prefill  | — | 2026-10-18 |
| [#44931](https://github.com/sgl-project/sglang/issues/44931) | [Bug] gpt-oss on /v1/chat/completions drops replayed reasoning: the te | — | 2026-10-18 |
| [#44897](https://github.com/sgl-project/sglang/issues/44897) | [Bug] [AMD] --ep-dispatch-algorithm fake routes with the real correcti | — | 2026-10-17 |
| [#40877](https://github.com/sgl-project/sglang/issues/40877) | [SM120] Field report: DeepSeek-V4.1-Flash in production on 8x RTX PRO  | — | 2026-10-17 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-10-17 |
| [#44872](https://github.com/sgl-project/sglang/issues/44872) | [Feature] Support pending external linker lookup at native prefill adm | — | 2026-10-17 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 132 |
| Multimodal | 75 |
| KV Cache / Memory | 48 |
| Prefill / Decode Disaggregation | 43 |
| MoE / Expert Parallel | 30 |
| Tensor / Data Parallel | 28 |
| Scheduler / Batching | 28 |
| Docs / Examples | 22 |
| Other | 19 |
| Quantization | 17 |
| CI / Build | 16 |
| ROCm / AMD | 16 |
| Models | 11 |
| Triton / Kernels | 10 |
| Serving / API | 10 |
| Speculative Decoding | 8 |
| LoRA | 2 |
| Structured Output | 1 |

## Attention / FlashInfer  (132 commits)

- **2026-10-19** [`7c4cc5a51c`](https://github.com/sgl-project/sglang/commit/7c4cc5a51c) [#41229](https://github.com/sgl-project/sglang/pull/41229)
  [Perf] [AMD] attention: Spread uneven Triton decode batches across XCDs (#41229)
  _Files: `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/kernels/ops/attention/metadata.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `test/registered/attention/test_triton_attention_kernels.py`_
- **2026-10-19** [`8111841103`](https://github.com/sgl-project/sglang/commit/8111841103) [#43733](https://github.com/sgl-project/sglang/pull/43733)
  [Perf] deepseek-v4.1: Replay the breakable prefill CUDA graph at any context length (#43733)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py` _+7 more__
- **2026-10-19** [`af9bb2a32d`](https://github.com/sgl-project/sglang/commit/af9bb2a32d) [#45111](https://github.com/sgl-project/sglang/pull/45111)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches with twelve open InferenceX PRs (#45111)
  _Files: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx` _+2 more__
- **2026-10-19** [`97857f9f96`](https://github.com/sgl-project/sglang/commit/97857f9f96) [#44307](https://github.com/sgl-project/sglang/pull/44307)
  [Doc] cookbook: GB300 full-set accuracy and tool follow-up output for Ling-3.1-flash (#44307)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.1-flash.mdx`, `docs/src/snippets/configs/inclusionAI/ling-3.1-flash-benchmarks.jsx`, `docs/src/snippets/configs/inclusionAI/ling-3.1-flash.jsx`_
- **2026-10-19** [`dc81f17b90`](https://github.com/sgl-project/sglang/commit/dc81f17b90) [#44225](https://github.com/sgl-project/sglang/pull/44225)
  [Fix] [XPU] gemma3: Enable bidirectional image attention (#44225)
  _Files: `python/sglang/srt/layers/attention/xpu_backend.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/gemma3_mm.py`, `test/registered/xpu/test_xpu_gemma3_bidirectional_attn.py`_
- **2026-10-19** [`a3330237db`](https://github.com/sgl-project/sglang/commit/a3330237db) [#45059](https://github.com/sgl-project/sglang/pull/45059)
  [Perf] deepseek-v4.1: Run decoder replay tail layers from CUDA graphs on eager prefill steps (#45059)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/model_executor/runner/row_bucket_graph_runner.py`, `python/sglang/srt/models/deepseek_v4.py` _+2 more__
- **2026-10-19** [`834bfe4ef0`](https://github.com/sgl-project/sglang/commit/834bfe4ef0) [#44580](https://github.com/sgl-project/sglang/pull/44580)
  [Fix] attention: Opt FlashMLA scheduler into dynamic shared memory (#44580)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/flashmla_sched_meta.cuh`, `test/registered/kernels/ops/attention/test_flashmla_sched_meta.py`_
- **2026-10-19** [`8d3eee46a7`](https://github.com/sgl-project/sglang/commit/8d3eee46a7) [#44927](https://github.com/sgl-project/sglang/pull/44927)
  [Perf] [AMD] deepseek-v4: Skip top-k refinement for proven positive-zero ties (#44927)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `test/registered/kernels/ops/attention/test_topk_v2.py`_
- **2026-10-19** [`7b1710324c`](https://github.com/sgl-project/sglang/commit/7b1710324c) [#45039](https://github.com/sgl-project/sglang/pull/45039)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches for Qwen3.8-Flash-Next H200 (v0.5.22, TP2 points) (#45039)
  _Files: `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`_
- **2026-10-19** [`377cd867fd`](https://github.com/sgl-project/sglang/commit/377cd867fd) [#43775](https://github.com/sgl-project/sglang/pull/43775)
  [Perf] dsa: Route the k-pool indexer top-k through the top-k v2 kernel (#43775)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dsv4/__init__.py`, `python/sglang/kernels/ops/attention/dsv4/topk.py` _+8 more__
- **2026-10-19** [`df078cc729`](https://github.com/sgl-project/sglang/commit/df078cc729) [#45048](https://github.com/sgl-project/sglang/pull/45048)
  [Fix] DSv4.1: Support CUDA image requests with encoder bounded replay and CI Test (#45048)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/e2e/models/test_deepseek_v41_flash_gb300_encoder_bcg.py`, `test/registered/unit/model_executor/test_encoder_swa_replay.py`_
- **2026-10-19** [`10ec53ac2f`](https://github.com/sgl-project/sglang/commit/10ec53ac2f) [#43390](https://github.com/sgl-project/sglang/pull/43390)
  [Perf] [NVIDIA] fp8_fa_sm120: Use the block-scaled MMA encoding (#43390)
  _Files: `python/sglang/kernels/ops/attention/fp8_fa_sm120/kernel.py`, `python/sglang/kernels/ops/attention/fp8_fa_sm120/plan.py`, `python/sglang/multimodal_gen/test/unit/test_fp8_fa_sm120_attn.py`_
- **2026-10-18** [`4ec19ca27f`](https://github.com/sgl-project/sglang/commit/4ec19ca27f) [#40917](https://github.com/sgl-project/sglang/pull/40917)
  [Refactor] memory-pool: Build KV host pools from buffer info (#40917)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/mem_cache/device_pool_info.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` _+31 more__
- **2026-10-18** [`e9b22a0818`](https://github.com/sgl-project/sglang/commit/e9b22a0818) [#44601](https://github.com/sgl-project/sglang/pull/44601)
  [Perf] [AMD] monokernels: Let a plugin skip per-step attention metadata (#44601)
  _Files: `docker/rocm.Dockerfile`, `python/pyproject_other.toml`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/monokernels/runtime.py` _+2 more__
- **2026-10-18** [`57db5089c2`](https://github.com/sgl-project/sglang/commit/57db5089c2) [#44973](https://github.com/sgl-project/sglang/pull/44973)
  [Perf] attention: Capture translated FA4 verify metadata for DSPARK (#44973)
  _Files: `python/sglang/kernels/ops/attention/metadata.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+4 more__
- **2026-10-18** [`2a83471676`](https://github.com/sgl-project/sglang/commit/2a83471676) [#44971](https://github.com/sgl-project/sglang/pull/44971)
  [Perf] mamba: Fuse strided state updates and replay index translation (#44971)
  _Files: `python/sglang/kernels/ops/mamba/mamba_state_scatter_triton.py`, `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `test/registered/kernels/ops/attention/test_inkling_checkpoint_indices.py`, `test/registered/unit/layers/test_mamba_state_scatter_triton.py`_
- **2026-10-18** [`a5b21145e1`](https://github.com/sgl-project/sglang/commit/a5b21145e1) [#44969](https://github.com/sgl-project/sglang/pull/44969)
  [Refactor] attention: Separate decode metadata from pool ownership (#44969)
  _Files: `python/sglang/kernels/ops/attention/metadata.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/xpu_backend.py`, `test/registered/attention/test_normal_decode_set_metadata.py` _+1 more__
- **2026-10-18** [`3edb156dec`](https://github.com/sgl-project/sglang/commit/3edb156dec) [#43326](https://github.com/sgl-project/sglang/pull/43326)
  [Feat] unified-memory: Fuse drafts with sliding-window and recurrent-state layers (#43326)
  _Files: `python/sglang/kernels/ops/attention/extend_attention.py`, `python/sglang/kernels/ops/speculative/__init__.py`, `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py` _+46 more__
- **2026-10-18** [`1d17066bad`](https://github.com/sgl-project/sglang/commit/1d17066bad) [#43171](https://github.com/sgl-project/sglang/pull/43171)
  [Perf] gdn: Select FlashInfer prefill for page-major pools (#43171)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `test/registered/unit/layers/attention/test_gdn_prefill_backend_policy.py`, `test/registered/unit/server_args/test_page_major_backend_allowlist.py`_
- **2026-10-18** [`8dee3f6bdb`](https://github.com/sgl-project/sglang/commit/8dee3f6bdb) [#44892](https://github.com/sgl-project/sglang/pull/44892)
  [Fix] [H200] ci: Split GLM-5.3-Flash serving recipes into separate tests (#44892)
  _Files: `python/sglang/test/glm53_flash_common.py`, `test/registered/e2e/models/test_glm53_flash_h200.py`, `test/registered/e2e/models/test_glm53_flash_h200_high_throughput.py`, `test/registered/e2e/models/test_glm53_flash_h200_low_latency.py`_
- **2026-10-18** [`3a6e1fcf77`](https://github.com/sgl-project/sglang/commit/3a6e1fcf77) [#44963](https://github.com/sgl-project/sglang/pull/44963)
  [Perf] DSv4.1: Bound encoder BCG metadata memory (#44963)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-10-18** [`a11fa06be7`](https://github.com/sgl-project/sglang/commit/a11fa06be7) [#41907](https://github.com/sgl-project/sglang/pull/41907)
  [Fix] hicache: Key MLA Mamba state per TP rank in the file backend (#41907)
  _Files: `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/storage/file/lru_file_evictor.py`, `test/registered/unit/mem_cache/test_hicache_file_lru_unit.py`_
- **2026-10-18** [`ffc4573c98`](https://github.com/sgl-project/sglang/commit/ffc4573c98) [#43816](https://github.com/sgl-project/sglang/pull/43816)
  [Fix] hicache: Key MLA Mamba state per TP rank in the SeaweedFS backend (#43816)
  _Files: `python/sglang/srt/mem_cache/storage/seaweedfs/seaweedfs_store.py`, `test/registered/unit/mem_cache/test_hicache_seaweedfs_storage.py`_
- **2026-10-18** [`e6c2cd47a9`](https://github.com/sgl-project/sglang/commit/e6c2cd47a9) [#43333](https://github.com/sgl-project/sglang/pull/43333)
  [Fix] hicache: Keep unified memory off the direct page_first_direct copies (#43333)
  _Files: `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/mem_cache/pool_host/mha.py`, `python/sglang/srt/mem_cache/pool_host/mla.py`, `test/registered/kernels/ops/kvcache/test_hicache_strided_device_rows.py` _+2 more__
- **2026-10-18** [`00f6cdcd1b`](https://github.com/sgl-project/sglang/commit/00f6cdcd1b) [#44089](https://github.com/sgl-project/sglang/pull/44089)
  [Fix] [AMD] kda: Reject match_cutedsl_decode on ROCm and skip its parity tests (#44089)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `test/registered/attention/test_kda_kernels.py`_
- **2026-10-18** [`3626978a13`](https://github.com/sgl-project/sglang/commit/3626978a13) [#43991](https://github.com/sgl-project/sglang/pull/43991)
  [Fix] [AMD] kda: Match the fused verify Q/K norm to its reference kernel (#43991)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_kda_conv_recurrent_verify.py`_
- **2026-10-18** [`d20d010574`](https://github.com/sgl-project/sglang/commit/d20d010574) [#44948](https://github.com/sgl-project/sglang/pull/44948)
  [Fix] deepseek-v4.1: Exchange late-layer DP row counts before the forward (#44948)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/model_executor/forward_batch_info.py` _+3 more__
- **2026-10-18** [`6fe630ae14`](https://github.com/sgl-project/sglang/commit/6fe630ae14) [#44946](https://github.com/sgl-project/sglang/pull/44946)
  [CI] deepseek-v4: Set the KV pool in the BCG replay contract test (#44946)
  _Files: `test/registered/attention/unittests/dsv4/test_deepseek_v4.py`_
- **2026-10-18** [`ff73d63121`](https://github.com/sgl-project/sglang/commit/ff73d63121) [#44930](https://github.com/sgl-project/sglang/pull/44930)
  [Perf] deepseek-v4.1: Run encoder SWA bounded replay in the breakable prefill graph (#44930)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` _+7 more__
- **2026-10-18** [`a0b77db84d`](https://github.com/sgl-project/sglang/commit/a0b77db84d) [#44119](https://github.com/sgl-project/sglang/pull/44119)
  [Perf] DFLASH: build the draft num_token_non_padded scalar with torch.full (#44119)
  _Files: `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-10-18** [`531b426281`](https://github.com/sgl-project/sglang/commit/531b426281) [#39475](https://github.com/sgl-project/sglang/pull/39475)
  [Feat] diffusion/model: support Cosmos Dreams and Cosmos Multiview (#39475) (#39475)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `docs/src/snippets/diffusion/model-catalog.jsx`, `python/sglang/multimodal_gen/configs/models/dits/cosmos3_sim_auto.py`, `python/sglang/multimodal_gen/configs/models/dits/cosmos_dreams.py` _+55 more__
- **2026-10-18** [`3b0a154e60`](https://github.com/sgl-project/sglang/commit/3b0a154e60) [#44937](https://github.com/sgl-project/sglang/pull/44937)
  [Doc] cookbook: Add DeepSeek V4.1 Flash 1017 variant (#44937)
  _Files: `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-10-18** [`d748bede96`](https://github.com/sgl-project/sglang/commit/d748bede96) [#34385](https://github.com/sgl-project/sglang/pull/34385)
  [Feat] diffusion: selectable sequence-parallel strategies for LingBot causal attention (#34385)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/lingbot_world.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/lingbot_world/lingbot_world_causal_denoising.py`_
- **2026-10-17** [`b234b5c32e`](https://github.com/sgl-project/sglang/commit/b234b5c32e) [#42288](https://github.com/sgl-project/sglang/pull/42288)
  [Refactor] TCPCG: Consolidate attention eager regions and isolate Inkling policy (4/9) (#42288)
  _Files: `python/sglang/srt/layers/attention/graph_utils.py`, `python/sglang/srt/layers/attention/hpc_ops_backend.py`, `python/sglang/srt/layers/radix_attention.py`, `python/sglang/srt/layers/radix_linear_attention.py` _+18 more__
- **2026-10-17** [`e4512a5a17`](https://github.com/sgl-project/sglang/commit/e4512a5a17) [#44920](https://github.com/sgl-project/sglang/pull/44920)
  [Perf] DSv4.1: Reduce BCG metadata memory (#44920)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`_
- **2026-10-17** [`563cd60345`](https://github.com/sgl-project/sglang/commit/563cd60345) [#44934](https://github.com/sgl-project/sglang/pull/44934)
  [Fix] [AMD] deepseek-v4.1: Reject attention DP with encoder SWA bounded replay on ROCm (#44934)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `test/registered/unit/model_executor/test_encoder_swa_replay.py`_
- **2026-10-17** [`05ce0e980f`](https://github.com/sgl-project/sglang/commit/05ce0e980f) [#42901](https://github.com/sgl-project/sglang/pull/42901)
  [Perf] deepseek-v4.1: Skip wasted layer 20 work on earlier prompt tokens under decoder bounded replay (#42901)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-17** [`3b34d9f8b6`](https://github.com/sgl-project/sglang/commit/3b34d9f8b6) [#44114](https://github.com/sgl-project/sglang/pull/44114)
  [Perf] [NVIDIA] qsa: Keep sparse decode scratch in FP8 for FP8 KV pools (#44114)
  _Files: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `test/registered/kernels/ops/attention/qsa/test_qsa.py`, `test/registered/kernels/ops/attention/qsa/test_qsa_fused_kv_prepare.py`, `test/registered/kernels/ops/attention/qsa/test_qsa_strided_zero_fill.py`_
- **2026-10-17** [`d4191a4624`](https://github.com/sgl-project/sglang/commit/d4191a4624) [#44493](https://github.com/sgl-project/sglang/pull/44493)
  [Fix] diffusion: stabilize FLUX.3 serving and reuse static conditioning (#44493)
  _Files: `docs/cookbook/diffusion/FLUX/FLUX.3.mdx`, `docs/src/snippets/configs/black-forest-labs/flux3.jsx`, `python/sglang/multimodal_gen/configs/pipeline_configs/flux3_image.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py` _+7 more__
- **2026-10-17** [`5fcb07da34`](https://github.com/sgl-project/sglang/commit/5fcb07da34) [#43817](https://github.com/sgl-project/sglang/pull/43817)
  [Fix] hicache: Key MLA Mamba state per TP rank in the HF3FS backend (#43817)
  _Files: `python/sglang/srt/mem_cache/storage/hf3fs/storage_hf3fs.py`, `test/registered/hicache/test_hicache_storage_3fs_backend.py`_
- **2026-10-17** [`465ddf9758`](https://github.com/sgl-project/sglang/commit/465ddf9758) [#43823](https://github.com/sgl-project/sglang/pull/43823)
  [Feat] diffusion/VSA-H3: support sm80 (A100) with a raw-pointer Triton load path (#43823)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/vsa_h3_kernels.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`, `python/sglang/multimodal_gen/test/unit/test_vsa_h3_attention.py`_
- **2026-10-17** [`a126e8d640`](https://github.com/sgl-project/sglang/commit/a126e8d640) [#44838](https://github.com/sgl-project/sglang/pull/44838)
  [Perf] deepseek_v4: fold the MegaAttention query layout into wq_b for block-FP8-as-MXFP8 checkpoints (#44838)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-17** [`a2953d7b7f`](https://github.com/sgl-project/sglang/commit/a2953d7b7f) [#44850](https://github.com/sgl-project/sglang/pull/44850)
  [Fix] deepseek-v4.1: Serve prompt-logprob requests under decoder SWA bounded replay (#44850)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `python/sglang/kernels/ops/attention/dsv4_attn_metadata_kernels.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/fields/exec_.py` _+8 more__
- **2026-10-17** [`ef26f6ad49`](https://github.com/sgl-project/sglang/commit/ef26f6ad49) [#44857](https://github.com/sgl-project/sglang/pull/44857)
  [Fix] deepseek-v4.1: Keep the cached KV of folded encoder replay rows (#44857)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/model_executor/encoder_swa_replay.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/model_executor/test_encoder_swa_replay.py`_
- **2026-10-17** [`bce7b27aa6`](https://github.com/sgl-project/sglang/commit/bce7b27aa6) [#44842](https://github.com/sgl-project/sglang/pull/44842)
  [Perf] deepseek_v4: run FlashInfer autotune for block-FP8 models served as MXFP8 (#44842)
  _Files: `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`_
- **2026-10-17** [`2d8a05e719`](https://github.com/sgl-project/sglang/commit/2d8a05e719) [#44602](https://github.com/sgl-project/sglang/pull/44602)
  [Test] attention: Fix replicated attention test missing full_attention_interval (#44602)
  _Files: `test/registered/unit/layers/test_replicated_attention_parallel_groups.py`_
- **2026-10-17** [`29a7e19de1`](https://github.com/sgl-project/sglang/commit/29a7e19de1) [#41745](https://github.com/sgl-project/sglang/pull/41745)
  [Refactor] nvfp4_online: Use explicit FlashInfer 4over6 config (#41745)
  _Files: `python/sglang/srt/layers/quantization/nvfp4_online.py`, `python/sglang/srt/model_loader/loader.py`_
- **2026-10-17** [`3603824541`](https://github.com/sgl-project/sglang/commit/3603824541) [#44403](https://github.com/sgl-project/sglang/pull/44403)
  [Perf] DSv4.1: Enable decoder bounded replay by default (#44403)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`, `python/sglang/kernels/jit/csrc/deepseek_v4/candidate_block_table.cuh`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` _+10 more__
- **2026-10-17** [`2d3dd3168d`](https://github.com/sgl-project/sglang/commit/2d3dd3168d) [#40131](https://github.com/sgl-project/sglang/pull/40131)
  [Fix] [NPU] attention: Use FIA TND for MLA prefix attention and add Gemma norm fallback (#40131)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/layernorm.py`, `test/registered/unit/npu/attention/test_npu_ascend_backend.py`_
- **2026-10-16** [`36cf028346`](https://github.com/sgl-project/sglang/commit/36cf028346) [#44592](https://github.com/sgl-project/sglang/pull/44592)
  [Perf] unified-memory: Prewarm the compaction move at startup and copy whole page envelopes by page id (#44592)
  _Files: `python/sglang/kernels/ops/kvcache/copy_pages.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py` _+11 more__
- **2026-10-16** [`aaf5f397a5`](https://github.com/sgl-project/sglang/commit/aaf5f397a5) [#43813](https://github.com/sgl-project/sglang/pull/43813)
  [Feat] dsv4.1: Support encoder SWA bounded replay with CUDA DP attention (#43813)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/model_executor/encoder_swa_replay.py` _+1 more__
- **2026-10-16** [`8e3f11b219`](https://github.com/sgl-project/sglang/commit/8e3f11b219) [#44783](https://github.com/sgl-project/sglang/pull/44783)
  [Perf] DSv4.1: Skip discarded KV rows during window commit (#44783)
  _Files: `python/sglang/kernels/ops/attention/dsv4/request_window_copy.py`, `python/sglang/srt/mem_cache/dsv41_request_window.py`, `test/registered/kernels/ops/attention/test_dsv41_request_window_copy.py`_
- **2026-10-16** [`2948662026`](https://github.com/sgl-project/sglang/commit/2948662026) [#44622](https://github.com/sgl-project/sglang/pull/44622)
  [Perf] dp-attention: Exchange the scheduler's MLP sync rows with gather + broadcast on gloo (#44622)
  _Files: `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `test/registered/unit/managers/scheduler_components/test_dp_attn.py`_
- **2026-10-16** [`21791e7023`](https://github.com/sgl-project/sglang/commit/21791e7023) [#44696](https://github.com/sgl-project/sglang/pull/44696)
  [CI] [NVIDIA] DSv4.1-Flash: Split GB300 accuracy test into one file per config (#44696)
  _Files: `python/sglang/test/dsv41_flash_common.py`, `test/registered/e2e/models/test_deepseek_v41_flash_gb300_bounded_replay_bcg.py`, `test/registered/e2e/models/test_deepseek_v41_flash_gb300_dp4ep4.py`, `test/registered/e2e/models/test_deepseek_v41_flash_gb300_tp4ep4.py` _+1 more__
- **2026-10-16** [`7c99ace127`](https://github.com/sgl-project/sglang/commit/7c99ace127) [#42565](https://github.com/sgl-project/sglang/pull/42565)
  [Fix] dsa: Fix ragged seed indices before MTP draft decode (#42565)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/attention/index_topk_share.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsa_attention.py` _+2 more__
- **2026-10-16** [`5e240a200d`](https://github.com/sgl-project/sglang/commit/5e240a200d) [#44712](https://github.com/sgl-project/sglang/pull/44712)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches for Qwen3.5 and DeepSeek-V4.1-Flash GB300 (#44712)
  _Files: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx` _+2 more__
- **2026-10-16** [`2adc76ad61`](https://github.com/sgl-project/sglang/commit/2adc76ad61) [#41903](https://github.com/sgl-project/sglang/pull/41903)
  [Perf] [AMD] dsv4: reuse the q_lora fp8 quant for the C4 indexer wq_b (4/8) (#41903)
  _Files: `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-16** [`8d229d96e0`](https://github.com/sgl-project/sglang/commit/8d229d96e0) [#42930](https://github.com/sgl-project/sglang/pull/42930)
  [Fix] unified-memory: enabling trtllm_mha with decode graphs and speculative decoding (#42930)
  _Files: `python/sglang/kernels/ops/kvcache/zero_pages.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py` _+7 more__
- **2026-10-16** [`6efc96abf9`](https://github.com/sgl-project/sglang/commit/6efc96abf9) [#44006](https://github.com/sgl-project/sglang/pull/44006)
  [Perf] [AMD] dsv4: FP4 indexer on aiter's row-group kernel for decode and target-verify (5/8) (#44006)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/fp4_indexer_rope_hip.cuh`, `python/sglang/kernels/ops/attention/dsv4/candidate_blocks_hip.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_hip.py`, `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_rope_hip.py` _+9 more__
- **2026-10-16** [`ab5858ac8a`](https://github.com/sgl-project/sglang/commit/ab5858ac8a) [#44016](https://github.com/sgl-project/sglang/pull/44016)
  [Perf] [AMD] dsv4: fp8 unified_kv decode/verify on FlyDSL v4 nm decode with a latency-model split plan (1/8) (#44016)
  _Files: `.pre-commit-config.yaml`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dsv4/flydsl_v4nm/__init__.py`, `python/sglang/kernels/ops/attention/dsv4/flydsl_v4nm/kernels/__init__.py` _+11 more__
- **2026-10-16** [`fad7d95a7f`](https://github.com/sgl-project/sglang/commit/fad7d95a7f) [#44673](https://github.com/sgl-project/sglang/pull/44673)
  [Fix] deepseek-v4.1: Keep the DSpark draft SWA out of the radix tree (#44673)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_attn_metadata.py`, `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` _+7 more__
- **2026-10-16** [`44be30d216`](https://github.com/sgl-project/sglang/commit/44be30d216) [#44591](https://github.com/sgl-project/sglang/pull/44591)
  [Chore] deps: Bump FlashInfer to 0.7.2 (#44591)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`_
- **2026-10-16** [`83940471b4`](https://github.com/sgl-project/sglang/commit/83940471b4) [#44387](https://github.com/sgl-project/sglang/pull/44387)
  [Fix] [NVIDIA] allreduce-fusion: Decline MNNVL fusion across NVLink cliques (#44387)
  _Files: `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `test/registered/unit/layers/test_flashinfer_comm_fusion.py`_
- **2026-10-16** [`06934575b9`](https://github.com/sgl-project/sglang/commit/06934575b9) [#44131](https://github.com/sgl-project/sglang/pull/44131)
  [Fix] DSv4.1: Fix BCG image handling and add multimodal bounded replay coverage (#44131)
  _Files: `python/pyproject.toml`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/e2e/models/test_deepseek_v41_flash_gb300.py` _+2 more__
- **2026-10-16** [`2a08e261ec`](https://github.com/sgl-project/sglang/commit/2a08e261ec) [#41993](https://github.com/sgl-project/sglang/pull/41993)
  [Feat] MiniCPM-V-4.7: add model support (#41993)
  _Files: `python/sglang/srt/arg_groups/model_overrides/minicpmv.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/minicpmv4_6.py` _+14 more__
- **2026-10-16** [`fd4b75c696`](https://github.com/sgl-project/sglang/commit/fd4b75c696) [#44654](https://github.com/sgl-project/sglang/pull/44654)
  [Doc] cookbook: Add SemiAnalysis AgentX launches to Muse Spark Open, refresh DeepSeek-V4.1-Flash (#44654)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+3 more__
- **2026-10-16** [`4e85e8ed37`](https://github.com/sgl-project/sglang/commit/4e85e8ed37) [#44430](https://github.com/sgl-project/sglang/pull/44430)
  [Fix] imports: Bind FlashInfer lazily at four import sites so the server starts without it (#44430)
  _Files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/speculative/dflash_utils.py` _+1 more__
- **2026-10-15** [`91f6ef2322`](https://github.com/sgl-project/sglang/commit/91f6ef2322) [#44555](https://github.com/sgl-project/sglang/pull/44555)
  [DSv4.1] Fuse request-window KV copies (#44555)
  _Files: `python/sglang/kernels/ops/attention/dsv4/request_window_copy.py`, `python/sglang/srt/mem_cache/dsv41_request_window.py`, `test/registered/kernels/ops/attention/test_dsv41_request_window_copy.py`_
- **2026-10-15** [`bc76a6b819`](https://github.com/sgl-project/sglang/commit/bc76a6b819) [#44557](https://github.com/sgl-project/sglang/pull/44557)
  [DSv4] Sparse prefill: build compressed lengths without a host sync (#44557)
  _Files: `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`_
- **2026-10-15** [`5ef8319f16`](https://github.com/sgl-project/sglang/commit/5ef8319f16) [#27702](https://github.com/sgl-project/sglang/pull/27702)
  [Perf] [AMD] attention: Enable diffusion BF16 attention and MXFP4 compilation (#27702)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/mxfp4.py`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`, `python/sglang/multimodal_gen/test/unit/test_transformer_quant.py`_
- **2026-10-15** [`09b7383624`](https://github.com/sgl-project/sglang/commit/09b7383624) [#44418](https://github.com/sgl-project/sglang/pull/44418)
  [diffusion] model: support FLUX.3 image (#44418)
  _Files: `docs/cookbook/diffusion/FLUX/FLUX.3.mdx`, `docs/cookbook/diffusion/intro.mdx`, `docs/docs.json`, `docs/docs/sglang-diffusion/cache_dit.mdx` _+70 more__
- **2026-10-15** [`c5bf3aafbc`](https://github.com/sgl-project/sglang/commit/c5bf3aafbc) [#37625](https://github.com/sgl-project/sglang/pull/37625)
  Fix overflow in legacy and v1 DSA top-k selectors (#37625)
  _Files: `python/sglang/kernels/aot/csrc/elementwise/deepseek_v4_topk.cu`, `python/sglang/kernels/aot/csrc/elementwise/topk.cu`, `python/sglang/kernels/aot/include/sgl_kernel/dsa/legacy_radix_topk.cuh`, `python/sglang/kernels/aot/tests/test_topk.py` _+4 more__
- **2026-10-15** [`abf92826ee`](https://github.com/sgl-project/sglang/commit/abf92826ee) [#44432](https://github.com/sgl-project/sglang/pull/44432)
  [NPU] [DOC] update NPU best practices and model deployment docs to CANN 9.1.0 (#44432)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/deepseek_v4_flash.mdx`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/glm_5_1.mdx` _+25 more__
- **2026-10-15** [`e1f9fce7b3`](https://github.com/sgl-project/sglang/commit/e1f9fce7b3) [#43605](https://github.com/sgl-project/sglang/pull/43605)
  [Refactor] layer-boundary: Bind residual completion to producer updates (#43605)
  _Files: `python/sglang/srt/layers/layer_boundary/boundary.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py`, `python/sglang/srt/layers/layer_boundary/exit.py` _+23 more__
- **2026-10-15** [`93dbe88183`](https://github.com/sgl-project/sglang/commit/93dbe88183) [#43106](https://github.com/sgl-project/sglang/pull/43106)
  Fuse MiMo verification RoPE and KV cache writes (#43106)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/pos_enc.cuh`, `python/sglang/kernels/ops/attention/rope.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` _+3 more__
- **2026-10-15** [`86f4ede4fb`](https://github.com/sgl-project/sglang/commit/86f4ede4fb) [#37941](https://github.com/sgl-project/sglang/pull/37941)
  [Fix] dsa: Make the fused top-k exact on an overflowing threshold bin (#37941)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `test/registered/kernels/ops/attention/test_topk_v2.py`_
- **2026-10-15** [`9ea5472833`](https://github.com/sgl-project/sglang/commit/9ea5472833) [#39727](https://github.com/sgl-project/sglang/pull/39727)
  [HiCache] Add the page_unified host KV layout and the unified L3 key (#39727)
  _Files: `python/sglang/srt/mem_cache/hicache_key_scheme.py`, `python/sglang/srt/mem_cache/pool_host/mha.py`, `python/sglang/srt/mem_cache/pool_host/mla.py`, `python/sglang/srt/mem_cache/pool_host/page_unified.py` _+1 more__
- **2026-10-15** [`33618d4f00`](https://github.com/sgl-project/sglang/commit/33618d4f00) [#43927](https://github.com/sgl-project/sglang/pull/43927)
  [Feat] runtime: Include FlashInfer’s default tactic in startup tuning. (#43927)
  _Files: `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`, `test/registered/unit/model_executor/runner/test_flashinfer_autotune_sync.py`_
- **2026-10-15** [`a12814c158`](https://github.com/sgl-project/sglang/commit/a12814c158) [#43643](https://github.com/sgl-project/sglang/pull/43643)
  [Perf] [AMD] dsa: Enable the gfx950 fused DSA indexer for block-FP8 wq_b/wk (#43643)
  _Files: `python/sglang/kernels/ops/attention/dsa/hip_gfx950/fused_decode.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-10-15** [`9fa9308e95`](https://github.com/sgl-project/sglang/commit/9fa9308e95) [#44357](https://github.com/sgl-project/sglang/pull/44357)
  [Doc] cookbook: Add Step 5 Preview cookbook (#44357)
  _Files: `docs/cookbook/autoregressive/StepFun/Step-3.7-Flash.mdx`, `docs/cookbook/autoregressive/StepFun/Step-5-Preview.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+1 more__
- **2026-10-15** [`9d68ecce2e`](https://github.com/sgl-project/sglang/commit/9d68ecce2e) [#44051](https://github.com/sgl-project/sglang/pull/44051)
  [DeepSeek-V4.1] DeepSelect cluster top-k for long rows and bf16 index logits (#44051)
  _Files: `python/sglang/kernels/jit/csrc/deep_select/vendor/cuda_kernels/common_parts.cuh`, `python/sglang/kernels/jit/csrc/deep_select/vendor/cuda_kernels/v3_cluster/topk_select.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/block_amax.cuh`, `python/sglang/kernels/jit/csrc/occupancy/cluster_probe.cuh` _+12 more__
- **2026-10-15** [`c5c4bbbd25`](https://github.com/sgl-project/sglang/commit/c5c4bbbd25) [#43642](https://github.com/sgl-project/sglang/pull/43642)
  [Perf] [AMD] dsa: Run DSA prefill under breakable CUDA graphs on HIP (#43642)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/dsa_prefill_cuda_graph.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+1 more__
- **2026-10-15** [`64a0a08f0a`](https://github.com/sgl-project/sglang/commit/64a0a08f0a) [#44326](https://github.com/sgl-project/sglang/pull/44326)
  [DSv4.1] Support TRT-LLM decoder bounded replay with BCG (#44326)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/attention/deepseek_v4_trtllm_backend.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+7 more__
- **2026-10-15** [`c891c5c7ca`](https://github.com/sgl-project/sglang/commit/c891c5c7ca) [#43166](https://github.com/sgl-project/sglang/pull/43166)
  [DSv4.1] Fold encoder-SWA replay into the extend forward (#43166)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/encoder_swa_replay.py` _+2 more__
- **2026-10-14** [`ed40c7fc66`](https://github.com/sgl-project/sglang/commit/ed40c7fc66) [#44301](https://github.com/sgl-project/sglang/pull/44301)
  [Doc] cookbook: add Ling-3.1-flash (#44301)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash-VL.mdx`, `docs/cookbook/autoregressive/InclusionAI/Ling-3.1-flash.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-10-14** [`204644c2dc`](https://github.com/sgl-project/sglang/commit/204644c2dc) [#44243](https://github.com/sgl-project/sglang/pull/44243)
  [Fix] sglang-processor: Follow Python's OpenAI layer through #43027, #37577, #43006, #43026, #43005 (#44243)
  _Files: `experimental/sgl-router/tests/fixtures/deepseek/v4.json`, `experimental/sgl-router/tests/fixtures/deepseek/v41.json`, `experimental/sgl-router/tests/scripts/generate_deepseek_parity.py`, `rust/sglang-processor/src/openai/chat.rs` _+11 more__
- **2026-10-14** [`bab9c81fea`](https://github.com/sgl-project/sglang/commit/bab9c81fea) [#35757](https://github.com/sgl-project/sglang/pull/35757)
  fix: FA4 paged-KV zero-size page-table registers on SM90 (#35757)
  _Files: `python/sglang/kernels/ops/attention/flash_attn/cute/paged_kv.py`_
- **2026-10-14** [`c82e8bd5fe`](https://github.com/sgl-project/sglang/commit/c82e8bd5fe) [#44210](https://github.com/sgl-project/sglang/pull/44210)
  [Fix] DeepSeek-V4.1: Align paged indexer score rows for DeepSelect decode (#44210)
  _Files: `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/full_topk.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/scoring.py`, `test/registered/kernels/ops/attention/test_fp4_indexer.py`_
- **2026-10-14** [`df1a089cd3`](https://github.com/sgl-project/sglang/commit/df1a089cd3) [#43054](https://github.com/sgl-project/sglang/pull/43054)
  [Spec] Fix DFLASH verify mask policy for wrapped attention backends (#43054)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/speculative/dflash_utils.py`_
- **2026-10-14** [`817781b828`](https://github.com/sgl-project/sglang/commit/817781b828) [#43689](https://github.com/sgl-project/sglang/pull/43689)
  [Feat] sgl-router: Render Qwen3.8 (Max, 27B, Flash-Next) through sglang-processor (#43689)
  _Files: `.agents/skills/processor-model-parity/SKILL.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/tokenizer/chat_formatter.rs`, `experimental/sgl-router/src/tokenizer/mod.rs` _+24 more__
- **2026-10-14** [`72730d6360`](https://github.com/sgl-project/sglang/commit/72730d6360) [#44228](https://github.com/sgl-project/sglang/pull/44228)
  [Doc] cookbook: Mirror SA cluster NCCL_CUMEM_ENABLE in AgentX launches, fix GPU counts (#44228)
  _Files: `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+2 more__
- **2026-10-14** [`68c18a5701`](https://github.com/sgl-project/sglang/commit/68c18a5701) [#44216](https://github.com/sgl-project/sglang/pull/44216)
  Revert "[XPU] Support Gemma-3 bidirectional image attention in XPUAttentionBackend" (#44216)
  _Files: `python/sglang/srt/layers/attention/xpu_backend.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/gemma3_mm.py`, `test/registered/xpu/test_xpu_gemma3_bidirectional_attn.py`_
- **2026-10-14** [`b87d62e581`](https://github.com/sgl-project/sglang/commit/b87d62e581) [#39805](https://github.com/sgl-project/sglang/pull/39805)
  [XPU] Support Gemma-3 bidirectional image attention in XPUAttentionBackend (#39805)
  _Files: `python/sglang/srt/layers/attention/xpu_backend.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/gemma3_mm.py`, `test/registered/xpu/test_xpu_gemma3_bidirectional_attn.py`_
- **2026-10-14** [`4560da58ee`](https://github.com/sgl-project/sglang/commit/4560da58ee) [#43625](https://github.com/sgl-project/sglang/pull/43625)
  [sgl-router] Render GLM-5.3 and GLM-5.3-Flash through sglang-processor (#43625)
  _Files: `.agents/skills/processor-model-parity/SKILL.md`, `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/README.md` _+25 more__
- **2026-10-14** [`d5f80aa3c3`](https://github.com/sgl-project/sglang/commit/d5f80aa3c3) [#41561](https://github.com/sgl-project/sglang/pull/41561)
  [Test] dsv4: Fix Hopper indexer replay test after DeepSelect decode (#41561) (#44193)
  _Files: `test/registered/kernels/ops/attention/test_fp4_indexer.py`_
- **2026-10-14** [`30bdd09aed`](https://github.com/sgl-project/sglang/commit/30bdd09aed) [#33739](https://github.com/sgl-project/sglang/pull/33739)
  DSPARK enable for XPU (#33739)
  _Files: `docs/docs/hardware-platforms/xpu.mdx`, `python/sglang/kernels/ops/attention/dsv4_attn_metadata_kernels.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/attention/xpu_backend.py` _+11 more__
- **2026-10-14** [`721953c6f6`](https://github.com/sgl-project/sglang/commit/721953c6f6) [#44065](https://github.com/sgl-project/sglang/pull/44065)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main (GLM-5.2 NVFP4 B300 agg TP4, Dynamo frontend counts) (#44065)
  _Files: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx` _+1 more__
- **2026-10-14** [`2428d0f531`](https://github.com/sgl-project/sglang/commit/2428d0f531) [#42122](https://github.com/sgl-project/sglang/pull/42122)
  [XPU] Use the shared fused decode-metadata kernel in the intel_xpu ba… (#42122)
  _Files: `python/sglang/srt/layers/attention/xpu_backend.py`, `test/registered/attention/test_normal_decode_set_metadata.py`_
- **2026-10-14** [`b50fdeb0ef`](https://github.com/sgl-project/sglang/commit/b50fdeb0ef) [#41561](https://github.com/sgl-project/sglang/pull/41561)
  [DeepSeek V4.1] Use DeepSelect for Hopper full top-k decode. (#41561)
  _Files: `python/sglang/srt/layers/attention/dsv4/v41_indexer/full_topk.py`, `test/registered/kernels/ops/attention/test_deep_select.py`, `test/registered/unit/layers/test_dsv4_nonpaged_indexer.py`_
- **2026-10-14** [`87beb3a052`](https://github.com/sgl-project/sglang/commit/87beb3a052) [#43468](https://github.com/sgl-project/sglang/pull/43468)
  [CPU] Temporarily disable subblock sparse attention test on Xeon CI (#43468)
  _Files: `test/registered/cpu/test_subblock_sparse_attention.py`_
- **2026-10-14** [`7f0434e4af`](https://github.com/sgl-project/sglang/commit/7f0434e4af) [#44098](https://github.com/sgl-project/sglang/pull/44098)
  [GLM-5.3-Flash] Drop the NextN layer from the KDA state pool (#44098)
  _Files: `python/sglang/srt/configs/glm5_next.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`_
- **2026-10-13** [`b3991b53da`](https://github.com/sgl-project/sglang/commit/b3991b53da) [#32947](https://github.com/sgl-project/sglang/pull/32947)
  GLM5.2 DSA Indexer Fallback (#32947)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/kernels/ops/attention/test_dsa_indexer.py`_
- **2026-10-13** [`5917604a95`](https://github.com/sgl-project/sglang/commit/5917604a95) [#43812](https://github.com/sgl-project/sglang/pull/43812)
  [DSV4.1] Support decoder SWA bounded replay with CUDA DP attention (#43812)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/models/deepseek_common/decoder_swa_bounded_replay.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-13** [`2341e647d3`](https://github.com/sgl-project/sglang/commit/2341e647d3) [#43736](https://github.com/sgl-project/sglang/pull/43736)
  [DeepSeek-V4.1] Run decoder SWA bounded replay inside the breakable prefill CUDA graph (#43736)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-13** [`8bf145d119`](https://github.com/sgl-project/sglang/commit/8bf145d119) [#43735](https://github.com/sgl-project/sglang/pull/43735)
  [DCP] Decode context parallelism for DSA (GLM-5.2 / GLM-5.3) with MTP (#43735)
  _Files: `docs/docs/advanced_features/dcp.mdx`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/kernels/ops/attention/dsa/transform_index.py` _+22 more__
- **2026-10-13** [`4c5ed0597e`](https://github.com/sgl-project/sglang/commit/4c5ed0597e) [#39769](https://github.com/sgl-project/sglang/pull/39769)
  Skip fully-masked KV tiles in sliding-window extend attention (#39769)
  _Files: `python/sglang/kernels/ops/attention/extend_attention.py`, `test/registered/attention/unittests/swa/test_triton.py`_
- **2026-10-13** [`5100f8d11d`](https://github.com/sgl-project/sglang/commit/5100f8d11d) [#41790](https://github.com/sgl-project/sglang/pull/41790)
  [DSA] Q8KV8 FP8 Sparse Prefill on GLM-5.3-Flash with BF16 KV Cache (#41790)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/docs/advanced_features/attention_backend.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx` _+6 more__
- **2026-10-13** [`4e0fa52530`](https://github.com/sgl-project/sglang/commit/4e0fa52530) [#43570](https://github.com/sgl-project/sglang/pull/43570)
  [Perf] Compact GDN causal-conv grids for skewed prefill batches (#43570)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba2_metadata.py`, `test/registered/attention/test_gdn_prefill_layout.py`, `test/registered/unit/layers/attention/test_gdn_prefill_backend_policy.py` _+1 more__
- **2026-10-13** [`195cb7afb4`](https://github.com/sgl-project/sglang/commit/195cb7afb4) [#43975](https://github.com/sgl-project/sglang/pull/43975)
  [CI] Use sgl-eval for GLM-5.3-Flash GSM8K tests (#43975)
  _Files: `python/sglang/test/kits/eval_accuracy_kit.py`, `test/registered/e2e/models/test_glm53_flash_b200.py`, `test/registered/e2e/models/test_glm53_flash_h200.py`_
- **2026-10-13** [`dbad07a06f`](https://github.com/sgl-project/sglang/commit/dbad07a06f) [#43983](https://github.com/sgl-project/sglang/pull/43983)
  [Docs] Cookbook: refresh SemiAnalysis AgentX launches (DeepSeek-V4.1 GB200/GB300, GLM-5.2 FP8 B300) (#43983)
  _Files: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx` _+1 more__
- **2026-10-13** [`46b7357779`](https://github.com/sgl-project/sglang/commit/46b7357779) [#43667](https://github.com/sgl-project/sglang/pull/43667)
  [Diffusion] Speed up LTX-2 guidance and video output (#43667)
  _Files: `python/sglang/kernels/kda_kernels/csrc/diffusion/residual_gate_add.cuh`, `python/sglang/kernels/kda_kernels/residual_gate_add_jit.py`, `python/sglang/multimodal_gen/configs/sample/ltx_2.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py` _+8 more__
- **2026-10-13** [`a69e893b1a`](https://github.com/sgl-project/sglang/commit/a69e893b1a) [#42911](https://github.com/sgl-project/sglang/pull/42911)
  [AMD] Fuse prefill index-Q RoPE fake-quant and fp4 quantize kernels in DSV4.1 (#42911)
  _Files: `python/sglang/kernels/ops/attention/dsv4/fp4_indexer_hip.py`, `python/sglang/srt/layers/attention/dsv4/low_ratio_backend_hip.py`, `test/registered/kernels/ops/attention/test_fp4_indexer_hip.py`_
- **2026-10-13** [`42e43cf33f`](https://github.com/sgl-project/sglang/commit/42e43cf33f) [#43793](https://github.com/sgl-project/sglang/pull/43793)
  [AMD] Fix Flux2 kv-gather abort on non-contiguous K/V (#43793)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/group_coordinator.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/test/unit/test_sp_kv_gather_contiguous.py`_
- **2026-10-13** [`43356304b4`](https://github.com/sgl-project/sglang/commit/43356304b4) [#43968](https://github.com/sgl-project/sglang/pull/43968)
  [AMD][Kimi-K3] Use public FlyDSL APIs in KDA decode kernels (#43968)
  _Files: `python/sglang/kernels/ops/attention/kda_flydsl/kernels/kimi_k3_kda_decode.py`, `python/sglang/kernels/ops/attention/kda_flydsl/kernels/kimi_k3_kda_decode_fb.py`_
- **2026-10-13** [`cda267ab0f`](https://github.com/sgl-project/sglang/commit/cda267ab0f) [#43350](https://github.com/sgl-project/sglang/pull/43350)
  [diffusion] fix: keep MiniMax-H3 VAE fused norms off ROCm (#43350)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/attention.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/vae_vit.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_vae_parallel_modes.py`_
- **2026-10-13** [`23150f7ae0`](https://github.com/sgl-project/sglang/commit/23150f7ae0) [#43921](https://github.com/sgl-project/sglang/pull/43921)
  [DSv4.1] Reduce sparse-prefill workspace padding (#43921)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `test/manual/test_dsv41_ragged_prefill.py` _+1 more__
- **2026-10-13** [`59445b3da1`](https://github.com/sgl-project/sglang/commit/59445b3da1) [#43935](https://github.com/sgl-project/sglang/pull/43935)
  [DSV4][CP] Write low-ratio page indices when CP prefill runs paged attention (#43935)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-10-12** [`93809202a3`](https://github.com/sgl-project/sglang/commit/93809202a3) [#43918](https://github.com/sgl-project/sglang/pull/43918)
  [Kernel] Expose bundled FlashMLA MegaAttention kernels and APIs (#43918)
  _Files: `python/sglang/kernels/aot/benchmark/bench_flashmla_mega.py`, `python/sglang/kernels/aot/cmake/flashmla.cmake`, `python/sglang/kernels/aot/csrc/flashmla_mega_extension.cc`, `python/sglang/kernels/aot/python/sgl_kernel/flash_mla_mega.py` _+1 more__
- **2026-10-12** [`64cffed139`](https://github.com/sgl-project/sglang/commit/64cffed139) [#43836](https://github.com/sgl-project/sglang/pull/43836)
  [AMD] Fix test_compact_attention_hip.py CI (#43836)
  _Files: `python/sglang/kernels/ops/attention/dsv4/compact_attention_hip.py`_
- **2026-10-12** [`6c2a682b59`](https://github.com/sgl-project/sglang/commit/6c2a682b59) [#41793](https://github.com/sgl-project/sglang/pull/41793)
  [AMD] Keep the FP4 varctx schedule test off AITER's 2048-row compile (#41793)
  _Files: `test/registered/kernels/ops/attention/test_fp4_indexer_hip.py`_
- **2026-10-12** [`0efbb3d2b9`](https://github.com/sgl-project/sglang/commit/0efbb3d2b9) [#43791](https://github.com/sgl-project/sglang/pull/43791)
  [DFlash] Decide the Domino candidate pool in one place and apply simulated acceptance inside the accept (#43791)
  _Files: `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/domino_utils.py`, `python/sglang/srt/speculative/spec_utils.py` _+2 more__
- **2026-10-12** [`d88d5c325a`](https://github.com/sgl-project/sglang/commit/d88d5c325a) [#37525](https://github.com/sgl-project/sglang/pull/37525)
  Prebuild fixup_zero_kv JIT module at TRTLLM-MLA backend init (#37525)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-10-12** [`23a1f53fc3`](https://github.com/sgl-project/sglang/commit/23a1f53fc3) [#43463](https://github.com/sgl-project/sglang/pull/43463)
  [QSA] Bound the decode indexer's work by the context length (#43463)
  _Files: `python/sglang/srt/layers/attention/qsa/fused_kv.py`, `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` _+2 more__
- **2026-10-12** [`f006fb49ec`](https://github.com/sgl-project/sglang/commit/f006fb49ec) [#43308](https://github.com/sgl-project/sglang/pull/43308)
  [NPU] Stabilize HiCache and registered CI tests (#43308)
  _Files: `scripts/ci/npu/npu_ci_install_dependency.sh`, `test/manual/ascend/test_npu_piecewise_graph_prefill.py`, `test/registered/npu/basic_function/HiCache/test_npu_hicache_mla.py`, `test/registered/npu/basic_function/dp_attn/test_npu_dp_attention.py` _+4 more__
- **2026-10-12** [`b0c84d4518`](https://github.com/sgl-project/sglang/commit/b0c84d4518) [#43799](https://github.com/sgl-project/sglang/pull/43799)
  [Docs] Cookbook: refresh SemiAnalysis AgentX launches (GLM-5.2 B300, DeepSeek-V4.1 GB300) (#43799)
  _Files: `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+2 more__
- **2026-10-12** [`450837e770`](https://github.com/sgl-project/sglang/commit/450837e770) [#43802](https://github.com/sgl-project/sglang/pull/43802)
  [Docs] Update GLM-5.3-Flash playground: B300 default, CP8, EP and PD (#43802)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-10-12** [`54409c2fa0`](https://github.com/sgl-project/sglang/commit/54409c2fa0) [#38603](https://github.com/sgl-project/sglang/pull/38603)
  [BCG][DSV4-Flash][CP] Support DeepSeek V4 prefill with interleave CP and breakable CUDA graphs (#38603)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/cp/bcg.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/unit/layers/cp/test_dsv4_prefill_cp_bcg.py`_
- **2026-10-12** [`8d491fbc3e`](https://github.com/sgl-project/sglang/commit/8d491fbc3e) [#34355](https://github.com/sgl-project/sglang/pull/34355)
  [XPU] Support decode context parallelism (DCP) on Intel XPU (#34355)
  _Files: `docs/docs/advanced_features/dcp.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/hardware-platforms/xpu.mdx`, `python/sglang/srt/arg_groups/attention_hook.py` _+9 more__
- **2026-10-12** [`b6ba148384`](https://github.com/sgl-project/sglang/commit/b6ba148384) [#43711](https://github.com/sgl-project/sglang/pull/43711)
  Capture KV host transfer buffers (#43711)
  _Files: `python/sglang/srt/mem_cache/pool_host/mha.py`, `python/sglang/srt/mem_cache/pool_host/mla.py`, `test/registered/unit/mem_cache/pool_host/test_kvcacheio_asymmetric.py`, `test/registered/unit/mem_cache/test_asymmetric_mha_pool_host_unit.py` _+6 more__
- **2026-10-12** [`da4bf1ef8e`](https://github.com/sgl-project/sglang/commit/da4bf1ef8e) [#43238](https://github.com/sgl-project/sglang/pull/43238)
  [Perf] Route BF16 mixed-batch decode tails through decode attention (#43238)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-10-12** [`130e11d50e`](https://github.com/sgl-project/sglang/commit/130e11d50e) [#43494](https://github.com/sgl-project/sglang/pull/43494)
  [Deps] Bump FlashInfer to 0.7.1 (#43494)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`, `python/pyproject.toml`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/README.md` _+2 more__
- **2026-10-12** [`bf703013f2`](https://github.com/sgl-project/sglang/commit/bf703013f2) [#43762](https://github.com/sgl-project/sglang/pull/43762)
  [Test] Re-anchor the VLM flashinfer throughput floor (#43762)
  _Files: `test/registered/basic_perf/test_vlm_serving_flashinfer.py`_

## Multimodal  (75 commits)

- **2026-10-19** [`e45cbce599`](https://github.com/sgl-project/sglang/commit/e45cbce599) [#45118](https://github.com/sgl-project/sglang/pull/45118)
  [Fix] diffusion: Prevent int32 overflow in Qwen-Image-2.1-Turbo VAE RMSNorm (#45118)
  _Files: `python/sglang/kernels/ops/diffusion/norm/channel_rmsnorm_preserve_reduction.py`_
- **2026-10-19** [`04c8c9703f`](https://github.com/sgl-project/sglang/commit/04c8c9703f) [#43883](https://github.com/sgl-project/sglang/pull/43883)
  [Fix] docker: Install numactl in runtime images - needed for SGLANG_NUMA_BIND_V2 (#43883)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`_
- **2026-10-19** [`f726461287`](https://github.com/sgl-project/sglang/commit/f726461287) [#36632](https://github.com/sgl-project/sglang/pull/36632)
  [Feat] [CPU] model: Support LTX and MOVA models on CPU (#36632)
  _Files: `python/sglang/multimodal_gen/runtime/models/vocoder/ltx_2_vocoder.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/mova.py`, `python/sglang/multimodal_gen/runtime/platforms/cpu.py` _+4 more__
- **2026-10-19** [`2b75048e2a`](https://github.com/sgl-project/sglang/commit/2b75048e2a) [#44996](https://github.com/sgl-project/sglang/pull/44996)
  [CI] diffusion: tighten H100 baselines and enable B200 performance checks (#44996)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/b200.json`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/server/testcase_configs.py`_
- **2026-10-19** [`58ad0748a6`](https://github.com/sgl-project/sglang/commit/58ad0748a6) [#44770](https://github.com/sgl-project/sglang/pull/44770)
  [Fix] diffusion: Unmerge LoRA layers the next adapter does not cover (#44770)
  _Files: `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py`, `python/sglang/multimodal_gen/test/unit/test_lora_pipeline.py`_
- **2026-10-19** [`617c8b67b1`](https://github.com/sgl-project/sglang/commit/617c8b67b1) [#44306](https://github.com/sgl-project/sglang/pull/44306)
  [Fix] Z-Image: Synchronize device after warmup request (#44306)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`_
- **2026-10-19** [`642f43ce59`](https://github.com/sgl-project/sglang/commit/642f43ce59) [#44090](https://github.com/sgl-project/sglang/pull/44090)
  [Fix] diffusion: size the in-context slot from both input grids for wan-animate-2(#44090)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/wan_animate_2_block.py`, `python/sglang/multimodal_gen/test/unit/test_wan_animate_2_config.py`, `python/sglang/multimodal_gen/test/unit/test_wan_animate_2_parallelism.py`_
- **2026-10-19** [`cff88d6eac`](https://github.com/sgl-project/sglang/commit/cff88d6eac) [#44204](https://github.com/sgl-project/sglang/pull/44204)
  [Fix] diffusion: Invalidate merged LoRA cache after adapter rewrites (#44204)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/lora/lora_merge_cache.py`, `test/registered/unit/multimodal_gen/test_lora_merge_cache_key.py`_
- **2026-10-19** [`329072d99a`](https://github.com/sgl-project/sglang/commit/329072d99a) [#44690](https://github.com/sgl-project/sglang/pull/44690)
  [Refactor] kernels/diffusion/tests: Prune dead code and fix tests that never ran (#44690)
- **2026-10-18** [`da414adda7`](https://github.com/sgl-project/sglang/commit/da414adda7) [#45038](https://github.com/sgl-project/sglang/pull/45038)
  [Fix] engram: Clamp multimodal pad ids in host-built history rows (#45038)
  _Files: `python/sglang/srt/layers/engram.py`, `python/sglang/srt/model_executor/encoder_swa_replay.py`, `python/sglang/srt/model_executor/model_runner_components/ngram_embedding_manager.py`, `test/registered/unit/layers/test_engram_history.py`_
- **2026-10-18** [`1fd46ddd56`](https://github.com/sgl-project/sglang/commit/1fd46ddd56) [#44180](https://github.com/sgl-project/sglang/pull/44180)
  [Perf] diffusion: fused indexed modulation for FP32 AdaLN tables (#44180)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/modulate/indexed_modulation_triton.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` _+1 more__
- **2026-10-18** [`de61ab53d4`](https://github.com/sgl-project/sglang/commit/de61ab53d4) [#44606](https://github.com/sgl-project/sglang/pull/44606)
  [Perf] diffusion: Defer full GC collections while importing the runtime (#44606)
  _Files: `python/sglang/multimodal_gen/registry.py`, `python/sglang/multimodal_gen/runtime/managers/worker_bootstrap.py`, `python/sglang/multimodal_gen/runtime/utils/process.py`, `python/sglang/multimodal_gen/test/unit/test_process.py`_
- **2026-10-18** [`f96a7326e6`](https://github.com/sgl-project/sglang/commit/f96a7326e6) [#43952](https://github.com/sgl-project/sglang/pull/43952)
  [Fix] [AMD] diffusion: Prevent ComponentResidencyError after compile warmup (#43952)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_compile_offload_keeps_explicit_layerwise.py`, `python/sglang/multimodal_gen/test/unit/test_offload_during_compile.py`_
- **2026-10-18** [`140c57d5bf`](https://github.com/sgl-project/sglang/commit/140c57d5bf) [#44478](https://github.com/sgl-project/sglang/pull/44478)
  [Perf] diffusion: classify residual_gate_add operands once per call (#44478)
  _Files: `python/sglang/kernels/kda_kernels/residual_gate_add_jit.py`, `test/registered/kernels/ops/diffusion/test_modulate.py`_
- **2026-10-18** [`3acfa2efcc`](https://github.com/sgl-project/sglang/commit/3acfa2efcc) [#42833](https://github.com/sgl-project/sglang/pull/42833)
  [Feat] runtime: Support tokenized multimodal generation (#42833)
  _Files: `proto/sglang/runtime/v1/sglang.proto`, `rust/sglang-api-types/src/generated/sglang.runtime.v1.rs`, `rust/sglang-grpc/src/utils/request_utils.rs`_
- **2026-10-18** [`8d02b69c11`](https://github.com/sgl-project/sglang/commit/8d02b69c11) [#44471](https://github.com/sgl-project/sglang/pull/44471)
  [Perf] diffusion: Replay Triton launches without the runner's per-launch hook metadata (#44471)
  _Files: `python/sglang/kernels/ops/diffusion/common/fast_launch.py`, `test/registered/kernels/ops/diffusion/test_fast_launch.py`_
- **2026-10-18** [`949e1a2080`](https://github.com/sgl-project/sglang/commit/949e1a2080) [#44643](https://github.com/sgl-project/sglang/pull/44643)
  [Perf] diffusion: Cache the fused linear-GELU verdict per linear (#44643)
  _Files: `python/sglang/kernels/ops/diffusion/sites/fused_linear_gelu_site.py`, `test/registered/kernels/ops/diffusion/test_sites.py`_
- **2026-10-17** [`4eb606b2ae`](https://github.com/sgl-project/sglang/commit/4eb606b2ae) [#44634](https://github.com/sgl-project/sglang/pull/44634)
  [Feat] diffusion: support opt-in pi0.5 completion-boundary action batching (#44634)
  _Files: `examples/usage/pi05_segmented_actions/README.md`, `examples/usage/pi05_segmented_actions/compare.py`, `examples/usage/pi05_segmented_actions/segmented.json`, `python/sglang/multimodal_gen/configs/pipeline_configs/pi05.py` _+9 more__
- **2026-10-17** [`9771e5a4f0`](https://github.com/sgl-project/sglang/commit/9771e5a4f0) [#44662](https://github.com/sgl-project/sglang/pull/44662)
  [Feat] diffusion: Per-task prompt enhancer config and the FLUX.3 Klein upsampler protocol (#44662)
  _Files: `docs/cookbook/diffusion/FLUX/FLUX.3.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/prompt_enhancement.py`, `python/sglang/multimodal_gen/test/unit/test_prompt_enhancement.py`_
- **2026-10-17** [`e01dfd3cbc`](https://github.com/sgl-project/sglang/commit/e01dfd3cbc) [#44845](https://github.com/sgl-project/sglang/pull/44845)
  [Refactor] multimodal: Replace padding strategies with helpers (#44845)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/models/bailing_mm.py`, `python/sglang/srt/models/bailing_mm_v3.py`, `python/sglang/srt/models/cohere2_vision.py` _+56 more__
- **2026-10-17** [`80f40522cd`](https://github.com/sgl-project/sglang/commit/80f40522cd) [#44376](https://github.com/sgl-project/sglang/pull/44376)
  [UX] diffusion: log LoRA merge decisions only on first evaluation (#44376)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py`, `python/sglang/multimodal_gen/test/unit/test_lora_auto_merge_rounding.py`_
- **2026-10-17** [`56a20d7e34`](https://github.com/sgl-project/sglang/commit/56a20d7e34) [#44644](https://github.com/sgl-project/sglang/pull/44644)
  [Perf] kernels: Enter a JIT kernel's device guard only when the device differs (#44644)
  _Files: `python/sglang/kernels/jit/utils/__init__.py`, `python/sglang/kernels/jit/utils/common.py`, `python/sglang/kernels/ops/diffusion/rope/qknorm_complex_rope_jit.py`, `test/registered/profiling/test_diffusion_stage_profiler_sync.py` _+1 more__
- **2026-10-17** [`86cc2e02ec`](https://github.com/sgl-project/sglang/commit/86cc2e02ec) [#44720](https://github.com/sgl-project/sglang/pull/44720)
  [Fix] gateway: Drop unused npyz dev-dependency to unbreak builds after zip yank (#44720)
  _Files: `.github/workflows/pr-test-rust.yml`, `.gitignore`, `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/scripts/generate_vision_golden.py`_
- **2026-10-17** [`5cbe2371a5`](https://github.com/sgl-project/sglang/commit/5cbe2371a5) [#44764](https://github.com/sgl-project/sglang/pull/44764)
  [Feat] rust-server: Report Python's launch-time /server_info fields from the Rust frontend (#44764)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/internal_state.py`, `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/rust_server/server.py` _+8 more__
- **2026-10-16** [`a038a0dca0`](https://github.com/sgl-project/sglang/commit/a038a0dca0) [#44751](https://github.com/sgl-project/sglang/pull/44751)
  [Fix] dsv41: Preserve tool-result image order and current-turn thinking (#44751)
  _Files: `python/sglang/srt/entrypoints/openai/encoding_dsv41.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-10-16** [`536cdb4b04`](https://github.com/sgl-project/sglang/commit/536cdb4b04) [#44621](https://github.com/sgl-project/sglang/pull/44621)
  [Feat] [AMD] docker: Install the sgl-amd-mono monokernel plugin in the ROCm image (#44621)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-16** [`92580581da`](https://github.com/sgl-project/sglang/commit/92580581da) [#44650](https://github.com/sgl-project/sglang/pull/44650)
  [Doc] [NPU] docs: Freeze qwen3-235b-a22b recommended image to a fixed version (#44650)
  _Files: `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/qwen3_235b_a22b.mdx`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/qwen3_235b_a22b.mdx`, `docs/docs/hardware-platforms/ascend-npus/optimization/parameter_tuning.mdx`_
- **2026-10-16** [`e1d20574da`](https://github.com/sgl-project/sglang/commit/e1d20574da) [#44664](https://github.com/sgl-project/sglang/pull/44664)
  [Chore] docker: Add muse spark CUDA image and DeepGEMM patches (1/5) (#44664)
  _Files: `docker/muse_spark/apply_deep_gemm_patches.sh`, `docker/muse_spark/deep_gemm.patch`, `docker/muse_spark/muse-spark.Dockerfile`_
- **2026-10-16** [`6d70787398`](https://github.com/sgl-project/sglang/commit/6d70787398) [#44275](https://github.com/sgl-project/sglang/pull/44275)
  [Fix] diffusion: Align Qwen-Image 2.1 resolution and handle RGBA JPEG output (#44275)
  _Files: `python/sglang/multimodal_gen/configs/sample/qwenimage21.py`, `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/test/unit/test_output_saving.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py`_
- **2026-10-16** [`e5274752a8`](https://github.com/sgl-project/sglang/commit/e5274752a8) [#44646](https://github.com/sgl-project/sglang/pull/44646)
  [Doc] diffusion: align PR title conventions (#44646)
  _Files: `docs/docs/developer_guide/contribution_guide.mdx`, `docs/docs/sglang-diffusion/contributing.mdx`_
- **2026-10-16** [`3420baea8c`](https://github.com/sgl-project/sglang/commit/3420baea8c) [#44508](https://github.com/sgl-project/sglang/pull/44508)
  [diffusion] CI: batch performance failure-policy runner scenarios (#44508)
  _Files: `python/sglang/multimodal_gen/test/unit/test_performance_failure_policy.py`_
- **2026-10-16** [`6231a617d3`](https://github.com/sgl-project/sglang/commit/6231a617d3) [#44595](https://github.com/sgl-project/sglang/pull/44595)
  [Test] diffusion: Load NVFP4 block scales through the weight loader in tests (#44595)
  _Files: `test/registered/kernels/ops/diffusion/test_nvfp4_scaled_mm.py`_
- **2026-10-16** [`75e25a21bd`](https://github.com/sgl-project/sglang/commit/75e25a21bd) [#44100](https://github.com/sgl-project/sglang/pull/44100)
  [Fix] [XPU] nightly: Fix rerank, zimage, flux2 and EAGLE parity (#44100)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines/xpu_b60.json`, `test/registered/spec/eagle/test_spec_eagle_parity.py`, `test/registered/xpu/conftest.py`, `test/registered/xpu/test_xpu_flux2_dev.py` _+1 more__
- **2026-10-16** [`75e77fca25`](https://github.com/sgl-project/sglang/commit/75e77fca25) [#43768](https://github.com/sgl-project/sglang/pull/43768)
  [Fix] wan: fix opt-in Wan2.2 progressive mode and one-step transitions (#43768)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/progressive_resolution/denoising.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/progressive_resolution/wan.py`, `python/sglang/multimodal_gen/test/unit/progressive_resolution/test_progressive.py`_
- **2026-10-16** [`1e33d2c4bd`](https://github.com/sgl-project/sglang/commit/1e33d2c4bd) [#39989](https://github.com/sgl-project/sglang/pull/39989)
  [Perf] [XPU] usp: Enable packed Ulysses QKV all-to-all (#39989)
  _Files: `python/sglang/kernels/ops/diffusion/layout/ulysses_qkv_triton.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_dit_contract.py`, `python/sglang/multimodal_gen/test/unit/test_usp_packed_qkv_a2a.py`_
- **2026-10-15** [`02a43eeef6`](https://github.com/sgl-project/sglang/commit/02a43eeef6) [#44315](https://github.com/sgl-project/sglang/pull/44315)
  [Feat] rust-server: Attach configured metadata headers to a healthy /health_generate (#44315)
  _Files: `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/rust_server/server.py`, `rust/sglang-server/src/api_server/http/native_api.rs`, `rust/sglang-server/src/message/config.rs` _+1 more__
- **2026-10-15** [`5b12ec163c`](https://github.com/sgl-project/sglang/commit/5b12ec163c) [#44515](https://github.com/sgl-project/sglang/pull/44515)
  [Doc] cookbook: Expand the FLUX.3 Image Klein model description (#44515)
  _Files: `docs/cookbook/diffusion/FLUX/FLUX.3.mdx`, `docs/docs.json`_
- **2026-10-15** [`28b98e5d13`](https://github.com/sgl-project/sglang/commit/28b98e5d13) [#44512](https://github.com/sgl-project/sglang/pull/44512)
  [Doc] cookbook: Add the FLUX.3 prompt upsampler section (#44512)
  _Files: `docs/cookbook/diffusion/FLUX/FLUX.3.mdx`_
- **2026-10-15** [`23c2a026db`](https://github.com/sgl-project/sglang/commit/23c2a026db) [#44325](https://github.com/sgl-project/sglang/pull/44325)
  [diffusion] model: support MOSS-Image (#44325)
  _Files: `docs/cookbook/diffusion/OpenMOSS/MOSS-Image.mdx`, `docs/cookbook/diffusion/intro.mdx`, `docs/docs.json`, `docs/src/snippets/configs/OpenMOSS/moss-image.jsx` _+23 more__
- **2026-10-15** [`f2b73d4f9b`](https://github.com/sgl-project/sglang/commit/f2b73d4f9b) [#44377](https://github.com/sgl-project/sglang/pull/44377)
  [diffusion] doc: document reference resizing, LoRA auto mode and image profiling (#44377)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/profiling.mdx`_
- **2026-10-15** [`a50c17e979`](https://github.com/sgl-project/sglang/commit/a50c17e979) [#38650](https://github.com/sgl-project/sglang/pull/38650)
  [diffusion] perf: fuse the Wan VAE conv bias epilogue and tile the RMSNorm+SiLU kernel (#38650)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/modulate/conv_bias_epilogue_triton.py`, `python/sglang/kernels/ops/diffusion/norm/wan_rmsnorm_silu_triton.py` _+7 more__
- **2026-10-15** [`676c038aa5`](https://github.com/sgl-project/sglang/commit/676c038aa5) [#40657](https://github.com/sgl-project/sglang/pull/40657)
  [diffusion] fix: fix the load duration missing from subclassed server tests (#40657)
  _Files: `python/sglang/multimodal_gen/test/server/test_server_common.py`, `python/sglang/multimodal_gen/test/unit/test_performance_failure_policy.py`, `test/registered/amd/test_zimage_turbo.py`, `test/registered/xpu/test_xpu_flux2_dev.py` _+1 more__
- **2026-10-15** [`93842f52fe`](https://github.com/sgl-project/sglang/commit/93842f52fe) [#35435](https://github.com/sgl-project/sglang/pull/35435)
  [CPU]: Add group-aware CPU SHM collective kernels (#35435)
  _Files: `python/sglang/kernels/aot/csrc/cpu/interface.cpp`, `python/sglang/kernels/aot/csrc/cpu/shm.cpp`, `python/sglang/kernels/aot/csrc/cpu/shm.h`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp` _+4 more__
- **2026-10-15** [`4dc9b5c68c`](https://github.com/sgl-project/sglang/commit/4dc9b5c68c) [#44311](https://github.com/sgl-project/sglang/pull/44311)
  [Test] [AMD] diffusion: Expect CUDA-only fast paths to be off on ROCm in kernel tests (#44311)
  _Files: `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`, `test/registered/kernels/ops/diffusion/test_modulate.py`_
- **2026-10-15** [`c92108bb93`](https://github.com/sgl-project/sglang/commit/c92108bb93) [#44058](https://github.com/sgl-project/sglang/pull/44058)
  [diffusion] comfyui: grouped SGLDOptions, native model loader and model-aware preflight (#44058)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/README.md`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/__init__.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/preflight.py` _+14 more__
- **2026-10-15** [`0cf683ea8d`](https://github.com/sgl-project/sglang/commit/0cf683ea8d) [#44088](https://github.com/sgl-project/sglang/pull/44088)
  [diffusion] comfyui: return several server-mode images as one IMAGE batch (#44088)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/README.md`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/nodes.py`_
- **2026-10-15** [`8333ccfccb`](https://github.com/sgl-project/sglang/commit/8333ccfccb) [#43770](https://github.com/sgl-project/sglang/pull/43770)
  [Fix] [AMD] diffusion: Compare ReduceOp by identity so the compiled TP all-reduce stays one graph (#43770)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/group_coordinator.py`_
- **2026-10-14** [`1737251730`](https://github.com/sgl-project/sglang/commit/1737251730) [#44096](https://github.com/sgl-project/sglang/pull/44096)
  [Test] [AMD] diffusion: Run the IPC all-to-all transport tests only on CUDA (#44096)
  _Files: `python/sglang/multimodal_gen/test/unit/test_ipc_a2a_lifecycle.py`_
- **2026-10-14** [`5e90312eb1`](https://github.com/sgl-project/sglang/commit/5e90312eb1) [#41340](https://github.com/sgl-project/sglang/pull/41340)
  [diffusion] perf: support bit-exact norm/bias fusions and channels_last decode for Qwen-Image 2.1(#41340)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/bias_residual_add.cuh`, `python/sglang/kernels/jit/csrc/diffusion/channel_rmsnorm_finish_silu.cuh`, `python/sglang/kernels/jit/csrc/diffusion/channel_rmsnorm_silu_nhwc.cuh`, `python/sglang/kernels/ops/diffusion/README.md` _+13 more__
- **2026-10-14** [`3b72b70ef4`](https://github.com/sgl-project/sglang/commit/3b72b70ef4) [#44235](https://github.com/sgl-project/sglang/pull/44235)
  [CI] vlm: Pin baidu/Unlimited-OCR revision in test_unlimited_ocr_server (#44235)
  _Files: `test/registered/vlm/test_unlimited_ocr_server.py`_
- **2026-10-14** [`6daae9c98e`](https://github.com/sgl-project/sglang/commit/6daae9c98e) [#44023](https://github.com/sgl-project/sglang/pull/44023)
  [Perf] Bind scheduler CPUs to the GPU's NUMA node when memory policy is not permitted (#44023)
  _Files: `docs/docs/references/environment_variables.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/srt/utils/numa_utils.py` _+1 more__
- **2026-10-14** [`6f646563a2`](https://github.com/sgl-project/sglang/commit/6f646563a2) [#40660](https://github.com/sgl-project/sglang/pull/40660)
  [AMD] diffusion: expect the residual-gate fast path to be off on ROCm in test_modulate (#40660)
  _Files: `test/registered/kernels/ops/diffusion/test_modulate.py`_
- **2026-10-14** [`2c1e85964e`](https://github.com/sgl-project/sglang/commit/2c1e85964e) [#43704](https://github.com/sgl-project/sglang/pull/43704)
  [diffusion] cache-dit: respect CFG parallel for dual-transformer models (#43704)
  _Files: `python/sglang/multimodal_gen/runtime/cache/cache_dit_integration.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_cache_dit_integration.py`_
- **2026-10-14** [`16176278d0`](https://github.com/sgl-project/sglang/commit/16176278d0) [#43859](https://github.com/sgl-project/sglang/pull/43859)
  [diffusion] perf: replay small Triton wrappers' launches per operand signature (#43859)
  _Files: `python/sglang/kernels/kda_kernels/layernorm_modulate_triton.py`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/activation/silu_mul_bitexact.py`, `python/sglang/kernels/ops/diffusion/common/__init__.py` _+6 more__
- **2026-10-14** [`53fe21cdfd`](https://github.com/sgl-project/sglang/commit/53fe21cdfd) [#44069](https://github.com/sgl-project/sglang/pull/44069)
  [diffusion] perf: replace padded rows without a host sync for Z-Image (#44069)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/zimage.py`, `python/sglang/multimodal_gen/test/unit/test_zimage_padding_no_sync.py`_
- **2026-10-14** [`5efb7384c1`](https://github.com/sgl-project/sglang/commit/5efb7384c1) [#43493](https://github.com/sgl-project/sglang/pull/43493)
  [diffusion] comfyui: consolidate 6 unrelated plugin fixes (#43493)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/server_api.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/qwen_image.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/nodes.py` _+5 more__
- **2026-10-14** [`ac187c0cd5`](https://github.com/sgl-project/sglang/commit/ac187c0cd5) [#43014](https://github.com/sgl-project/sglang/pull/43014)
  [diffusion] Bound frame_interpolation_exp to RIFE's supported range (#43014)
  _Files: `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/runtime/postprocess/rife_interpolator.py`, `python/sglang/multimodal_gen/test/unit/realtime/test_output_materialization.py`, `python/sglang/multimodal_gen/test/unit/test_multiple_task_types.py`_
- **2026-10-13** [`2ebdf9360b`](https://github.com/sgl-project/sglang/commit/2ebdf9360b) [#44143](https://github.com/sgl-project/sglang/pull/44143)
  [Fix] Work around a CPython fork deadlock in the CPU preprocess pool (#44143)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`_
- **2026-10-13** [`baa632b049`](https://github.com/sgl-project/sglang/commit/baa632b049) [#39730](https://github.com/sgl-project/sglang/pull/39730)
  [Score] Send stacked GPU embedding overrides through a CUDA IPC pool (#39730)
  _Files: `python/sglang/srt/entrypoints/engine_score_mixin.py`, `python/sglang/srt/managers/embed_types.py`, `python/sglang/srt/managers/positional_embeds_transport.py`, `python/sglang/srt/managers/schedule_batch.py` _+7 more__
- **2026-10-13** [`7f9f742535`](https://github.com/sgl-project/sglang/commit/7f9f742535) [#43925](https://github.com/sgl-project/sglang/pull/43925)
  [Rust] Refuse an unsupported multimodal model before the Rust listener binds (#43925)
  _Files: `python/sglang/srt/rust_server/server.py`, `test/registered/unit/multimodal/rust/shared/test_rust_server_extension.py`_
- **2026-10-13** [`5727f08932`](https://github.com/sgl-project/sglang/commit/5727f08932) [#35839](https://github.com/sgl-project/sglang/pull/35839)
  [diffusion] feat: add configurable reference image resizing for MiniMax H3 Ref2VA (#35839)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx`, `python/sglang/multimodal_gen/configs/sample/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/constants.py` _+5 more__
- **2026-10-13** [`85254b5a8f`](https://github.com/sgl-project/sglang/commit/85254b5a8f) [#43581](https://github.com/sgl-project/sglang/pull/43581)
  [diffusion] comfyui: run Qwen-Image 2.1 in SGLD integrated mode (#43581)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/README.md`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/qwen_image21.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/nodes.py` _+8 more__
- **2026-10-13** [`991a29d0ad`](https://github.com/sgl-project/sglang/commit/991a29d0ad) [#42127](https://github.com/sgl-project/sglang/pull/42127)
  fix(multimodal): convert grayscale tensors to RGB in PIL backend (#42127)
  _Files: `python/sglang/srt/utils/hf_transformers_patches.py`, `test/registered/unit/utils/test_hf_transformers.py`_
- **2026-10-13** [`4b5b727145`](https://github.com/sgl-project/sglang/commit/4b5b727145) [#42933](https://github.com/sgl-project/sglang/pull/42933)
  Fix EVS for NemotronH_Omni_Reasoning_V3 (#42933)
  _Files: `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/multimodal/evs/evs_module.py`, `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `test/registered/unit/models/test_nano_nemotron_vl.py` _+2 more__
- **2026-10-13** [`ea13359da9`](https://github.com/sgl-project/sglang/commit/ea13359da9) [#42770](https://github.com/sgl-project/sglang/pull/42770)
  [diffusion] perf: implement paint_use_remesh (decimate to 40k faces before UV unwrap) for Hunyuan3D (#42770)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan3d.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/hunyuan3d/paint.py`, `python/sglang/multimodal_gen/runtime/utils/mesh3d_utils.py`, `python/sglang/multimodal_gen/test/unit/test_hunyuan3d_native_texture_models.py`_
- **2026-10-13** [`feba04fa49`](https://github.com/sgl-project/sglang/commit/feba04fa49) [#43028](https://github.com/sgl-project/sglang/pull/43028)
  [diffusion] fix: avoid redundant LoRA scaling while preserving exact numerics (#43028)
  _Files: `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/test/unit/test_lora_dynamic_delta_in_gemm.py`, `python/sglang/multimodal_gen/test/unit/test_lora_inference_mode.py`_
- **2026-10-13** [`b4822bae03`](https://github.com/sgl-project/sglang/commit/b4822bae03) [#43504](https://github.com/sgl-project/sglang/pull/43504)
  [diffusion] comfyui: run MiniMax H3, FastH3 and VDN in SGLD integrated mode (#43504)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/minimax_h3.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/nodes.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/comfyui_step.py` _+3 more__
- **2026-10-12** [`1a553927b0`](https://github.com/sgl-project/sglang/commit/1a553927b0) [#37426](https://github.com/sgl-project/sglang/pull/37426)
  [CI][Diffusion] Add caching for npu GT images in CI (#37426)
  _Files: `.github/workflows/pr-test-npu.yml`, `scripts/ci/utils/diffusion/prefetch_consistency_gt.py`_
- **2026-10-12** [`279f1fad90`](https://github.com/sgl-project/sglang/commit/279f1fad90) [#43756](https://github.com/sgl-project/sglang/pull/43756)
  [diffusion] chore: bind worker CPUs to the GPU's NUMA node when memory policy is not permitted (#43756)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/test/unit/test_gpu_worker_cpu_threads.py`, `python/sglang/srt/utils/numa_utils.py`, `test/registered/utils/test_numa_utils.py`_
- **2026-10-12** [`d1357bf87b`](https://github.com/sgl-project/sglang/commit/d1357bf87b) [#43210](https://github.com/sgl-project/sglang/pull/43210)
  [NPU] Diffusion CI fixes (#43210)
  _Files: `.github/workflows/_npu-analyze-failure.yml`, `.github/workflows/pr-test-npu.yml`, `proto/sglang/api/v1/generate.proto`, `python/sglang/api/v1/api_types.py` _+11 more__
- **2026-10-12** [`208df292e5`](https://github.com/sgl-project/sglang/commit/208df292e5) [#41940](https://github.com/sgl-project/sglang/pull/41940)
  [diffusion][xpu] FLUX.2: enable the bit-exact Triton SwiGLU on XPU (#41940)
  _Files: `python/sglang/kernels/ops/diffusion/activation/silu_mul_bitexact.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py`_
- **2026-10-12** [`6ac8602e8d`](https://github.com/sgl-project/sglang/commit/6ac8602e8d) [#43747](https://github.com/sgl-project/sglang/pull/43747)
  [CI] Fix TestQwenImageModulationCache after Qwen-Image modulation sharding (#43747)
  _Files: `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-10-12** [`d0a098b2e0`](https://github.com/sgl-project/sglang/commit/d0a098b2e0) [#43684](https://github.com/sgl-project/sglang/pull/43684)
  [diffusion] perf: split and batch LTX-2.3 one-stage guidance passes under CFG parallel (#43684)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/encode_while_decoding.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/joy_echo/setup.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/decoding_av.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py` _+2 more__
- **2026-10-12** [`a954b395e6`](https://github.com/sgl-project/sglang/commit/a954b395e6) [#43683](https://github.com/sgl-project/sglang/pull/43683)
  [diffusion] perf: layerwise offload for the LTX-2.5 Gemma-4 text encoder (#43683)
  _Files: `docs/cookbook/diffusion/LTX/LTX2.5.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/models/encoders/gemma_4_unified.py`, `python/sglang/multimodal_gen/test/unit/test_gemma4_unified_layerwise_offload.py`_
- **2026-10-12** [`a67228aa43`](https://github.com/sgl-project/sglang/commit/a67228aa43) [#43691](https://github.com/sgl-project/sglang/pull/43691)
  [diffusion] fix: shard Qwen-Image adaLN modulation and text FFN under TP (#43691)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image.mdx`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image_joint_qkv.py`_

## KV Cache / Memory  (48 commits)

- **2026-10-19** [`c04f9a61f0`](https://github.com/sgl-project/sglang/commit/c04f9a61f0) [#44286](https://github.com/sgl-project/sglang/pull/44286)
  [Fix] diffusion: Fix VMoBA chunk selection bugs (#44286)
  _Files: `python/sglang/multimodal_gen/csrc/attn/vmoba_attn/tests/test_vmoba_selection.py`, `python/sglang/multimodal_gen/csrc/attn/vmoba_attn/tests/test_vmoba_selection_gpu.py`, `python/sglang/multimodal_gen/csrc/attn/vmoba_attn/vmoba/vmoba.py`_
- **2026-10-19** [`96ba108072`](https://github.com/sgl-project/sglang/commit/96ba108072) [#44564](https://github.com/sgl-project/sglang/pull/44564)
  [Fix] dsa-eagle-topk: Copy token keys and scales when relocating index cache (#44564)
  _Files: `python/sglang/srt/mem_cache/index_key_cache.py`, `test/registered/kernels/ops/kvcache/test_dsa_index_cache_move.py`, `test/registered/unit/mem_cache/test_index_key_cache_move.py`_
- **2026-10-19** [`59fec011dd`](https://github.com/sgl-project/sglang/commit/59fec011dd) [#45051](https://github.com/sgl-project/sglang/pull/45051)
  [Fix] deepseek-v4.1: Reject encoder replay on a chunk too small for a hit or on other models (#45051)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `test/registered/unit/managers/test_prefill_adder.py`, `test/registered/unit/model_executor/test_encoder_swa_replay.py`_
- **2026-10-18** [`6708426728`](https://github.com/sgl-project/sglang/commit/6708426728) [#45043](https://github.com/sgl-project/sglang/pull/45043)
  [Fix] spec: Remove `--speculative-skip-dp-mlp-sync` (#45043)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/spec.py` _+5 more__
- **2026-10-18** [`1461152cb0`](https://github.com/sgl-project/sglang/commit/1461152cb0) [#45040](https://github.com/sgl-project/sglang/pull/45040)
  [Fix] deepseek-v4.1: Leave room for encoder replay rows when sizing a prefill chunk (#45040)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/model_executor/encoder_swa_replay.py`, `test/registered/unit/managers/test_prefill_adder.py`_
- **2026-10-18** [`bb1d4cddd9`](https://github.com/sgl-project/sglang/commit/bb1d4cddd9) [#44968](https://github.com/sgl-project/sglang/pull/44968)
  [Refactor] hicache: Route Mamba host transfers from pool info (#44968)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `test/registered/kernels/ops/mamba/test_mtp_hicache.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`, `test/registered/unit/mem_cache/test_unified_hicache_regressions.py`_
- **2026-10-18** [`d4e3c163c9`](https://github.com/sgl-project/sglang/commit/d4e3c163c9) [#45004](https://github.com/sgl-project/sglang/pull/45004)
  [CI] radix-cache: Register the Inkling cache linker KL test to extra-b (#45004)
  _Files: `test/registered/radix_cache/unified_radix_tree/linker/test_unified_cache_linker_kl_inkling.py`_
- **2026-10-18** [`2e9b2cacda`](https://github.com/sgl-project/sglang/commit/2e9b2cacda) [#44972](https://github.com/sgl-project/sglang/pull/44972)
  [Perf] speculative: Fuse draft write-window gathering and KV translation (#44972)
  _Files: `python/sglang/kernels/ops/speculative/__init__.py`, `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/srt/mem_cache/kv_index_translator.py`, `python/sglang/srt/mem_cache/kv_loc_plan.py` _+4 more__
- **2026-10-18** [`d318a546da`](https://github.com/sgl-project/sglang/commit/d318a546da) [#44970](https://github.com/sgl-project/sglang/pull/44970)
  [Perf] unified-memory: Reduce allocation and SWA retirement overhead (#44970)
  _Files: `python/sglang/kernels/ops/memory/virtual_slot.py`, `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py`, `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py`, `test/registered/kernels/ops/memory/test_virtual_slot_binding.py` _+3 more__
- **2026-10-18** [`19cb24f1e1`](https://github.com/sgl-project/sglang/commit/19cb24f1e1) [#43325](https://github.com/sgl-project/sglang/pull/43325)
  [Feat] unified-memory: Support asymmetric KV rows (#43325)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/layout/fused_draft.py`, `python/sglang/srt/mem_cache/unified_memory_pool.py` _+3 more__
- **2026-10-18** [`ba50ea3d77`](https://github.com/sgl-project/sglang/commit/ba50ea3d77) [#43170](https://github.com/sgl-project/sglang/pull/43170)
  [Perf] unified-memory: Free SWA segments without a host sync (#43170)
  _Files: `python/sglang/srt/mem_cache/allocator/swa.py`, `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py`, `test/registered/unit/mem_cache/test_unified_free_no_host_sync.py`, `test/registered/unit/mem_cache/test_unified_radix_allocation_eviction.py` _+1 more__
- **2026-10-18** [`47eeddcd18`](https://github.com/sgl-project/sglang/commit/47eeddcd18) [#43168](https://github.com/sgl-project/sglang/pull/43168)
  [Fix] swa: Retain a whole window behind insertion pages (#43168)
  _Files: `python/sglang/srt/mem_cache/common.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-10-18** [`f8e32706fc`](https://github.com/sgl-project/sglang/commit/f8e32706fc) [#44938](https://github.com/sgl-project/sglang/pull/44938)
  [CI] radix-cache: Re-enable Inkling unified cache linker KL test (#44938)
  _Files: `test/registered/radix_cache/unified_radix_tree/linker/test_unified_cache_linker_kl_inkling.py`_
- **2026-10-18** [`3b932cde26`](https://github.com/sgl-project/sglang/commit/3b932cde26) [#43043](https://github.com/sgl-project/sglang/pull/43043)
  [Fix] VLM: harden Kimi image cache identity across preprocessing and radix hashing (#43043)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/cpp_utils/hash_binding.cpp`, `python/sglang/srt/mem_cache/cpp_utils/native_hash.py` _+17 more__
- **2026-10-18** [`ba3fc9441d`](https://github.com/sgl-project/sglang/commit/ba3fc9441d) [#43559](https://github.com/sgl-project/sglang/pull/43559)
  [Fix] mamba: Release consumed lazy Mamba prefix locks before donation retry (#43559)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/mamba.py`, `test/registered/radix_cache/test_mamba_cache_kl.py`, `test/registered/unit/mem_cache/test_mamba_donated_alloc_ratio.py`_
- **2026-10-17** [`86e67f7d93`](https://github.com/sgl-project/sglang/commit/86e67f7d93) [#43387](https://github.com/sgl-project/sglang/pull/43387)
  [Fix] unified_cache: Prevent misaligned Mamba checkpoints after speculative truncation (#43387)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/radix_cache/test_mamba_cache_kl.py`, `test/registered/unit/managers/test_batch_result_processor_spec_grammar.py`_
- **2026-10-17** [`025655068c`](https://github.com/sgl-project/sglang/commit/025655068c) [#44097](https://github.com/sgl-project/sglang/pull/44097)
  [Fix] unified-memory: Avoid gather scratch during Mamba and Conv compaction (#44097)
  _Files: `python/sglang/srt/mem_cache/unified_memory_pool.py`, `test/registered/unit/mem_cache/test_unified_conv_compaction.py`, `test/registered/unit/mem_cache/test_unified_mamba_compaction.py`, `test/registered/unit/mem_cache/test_unified_mamba_views.py`_
- **2026-10-17** [`ee30dc4d40`](https://github.com/sgl-project/sglang/commit/ee30dc4d40) [#39294](https://github.com/sgl-project/sglang/pull/39294)
  [Fix] unified-memory: Bound joint reclaim and preserve cached prefixes (#39294)
  _Files: `python/sglang/srt/mem_cache/allocation.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` _+6 more__
- **2026-10-17** [`ae28306a74`](https://github.com/sgl-project/sglang/commit/ae28306a74) [#44220](https://github.com/sgl-project/sglang/pull/44220)
  [Fix] cuda_graph: Wait for in-flight layer-wise cache loads before prefill graph replay (#44220)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/l2_transfer.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_hybrid_bitexact.py` _+1 more__
- **2026-10-17** [`f75232cb42`](https://github.com/sgl-project/sglang/commit/f75232cb42) [#44800](https://github.com/sgl-project/sglang/pull/44800)
  [Fix] hicache: Order write-back host copies after the forward that produced the KV (#44800)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+7 more__
- **2026-10-17** [`6a39ddf1f2`](https://github.com/sgl-project/sglang/commit/6a39ddf1f2) [#44843](https://github.com/sgl-project/sglang/pull/44843)
  [Fix] unified_cache: Resize test allocator before allocating backed pages (#44843)
  _Files: `test/registered/unit/mem_cache/test_unified_post_capture_sizing.py`_
- **2026-10-16** [`f39c2693aa`](https://github.com/sgl-project/sglang/commit/f39c2693aa) [#44773](https://github.com/sgl-project/sglang/pull/44773)
  [CI] rust-server: Raise the ChunkEvent frame-size cap to 152 bytes (#44773)
  _Files: `rust/sglang-server/src/message/response.rs`_
- **2026-10-16** [`a18a908066`](https://github.com/sgl-project/sglang/commit/a18a908066) [#44777](https://github.com/sgl-project/sglang/pull/44777)
  [Test] mem_cache: Free SWA peers below the eviction floor in the SWA repair test (#44777)
  _Files: `test/registered/unit/mem_cache/test_rust_tree_core_integration.py`_
- **2026-10-16** [`80c54e6ac5`](https://github.com/sgl-project/sglang/commit/80c54e6ac5) [#42716](https://github.com/sgl-project/sglang/pull/42716)
  [Fix] [AMD] hicache: Serve encoder-replay prefix hits with a paged DSpark draft SWA (#42716)
  _Files: `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa.py` _+2 more__
- **2026-10-16** [`453b251dbd`](https://github.com/sgl-project/sglang/commit/453b251dbd) [#44614](https://github.com/sgl-project/sglang/pull/44614)
  [Fix] hicache: Bound the storage prefetch timeout from the first blocked admission poll (#44614)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/unified_cache/storage_attachment.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+6 more__
- **2026-10-16** [`f05da43d44`](https://github.com/sgl-project/sglang/commit/f05da43d44) [#30929](https://github.com/sgl-project/sglang/pull/30929)
  [Feat] [AMD] disagg: Support DSV4 decode radix cache on ROCm unified KV (bf16/fp8, DSpark) (#30929)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `test/registered/unit/mem_cache/test_decode_radix_cache_validation.py`_
- **2026-10-16** [`a448fdf316`](https://github.com/sgl-project/sglang/commit/a448fdf316) [#44267](https://github.com/sgl-project/sglang/pull/44267)
  [Perf] [AMD] qwen3: Fuse QK-norm + RoPE + KV cache write for dense Qwen3 decode (#44267)
  _Files: `python/sglang/srt/models/qwen3.py`, `test/registered/amd/test_qwen3_aiter_fused_qk_norm_rope.py`_
- **2026-10-15** [`173e0f2e9b`](https://github.com/sgl-project/sglang/commit/173e0f2e9b) [#44173](https://github.com/sgl-project/sglang/pull/44173)
  [Feat] hicache: Add opt-in tail-only SWA backups in buffer mode (#44173)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `test/registered/unit/mem_cache/test_buffer_mode_sidecar.py` _+2 more__
- **2026-10-15** [`2f5407da28`](https://github.com/sgl-project/sglang/commit/2f5407da28) [#44266](https://github.com/sgl-project/sglang/pull/44266)
  [Fix] [AMD] qwen3: Fix KV cache write in the fused QK-norm + mRoPE decode path (#44266)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/models/qwen3.py`, `test/registered/amd/test_qwen3_aiter_fused_qk_norm_rope.py`_
- **2026-10-15** [`d59c3448b0`](https://github.com/sgl-project/sglang/commit/d59c3448b0) [#43604](https://github.com/sgl-project/sglang/pull/43604)
  [Fix] kimi-k3: Preserve pipeline graph bank inputs and bound chunk profiling (#43604)
  _Files: `python/sglang/srt/managers/scheduler_components/dynamic_chunk_sizer.py`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/managers/scheduler_components/test_dynamic_chunk_sizer.py`, `test/registered/unit/models/test_kimi_k3_pipeline_layers.py`_
- **2026-10-15** [`3b5ae4ea86`](https://github.com/sgl-project/sglang/commit/3b5ae4ea86) [#44351](https://github.com/sgl-project/sglang/pull/44351)
  [Fix] scheduler: Drop finished requests from the running batch before every admission (#44351)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_chunked_req_gate.py`, `test/registered/unit/managers/test_scheduler_hicache_events.py`, `test/registered/unit/managers/test_scheduler_running_batch_finished.py`_
- **2026-10-15** [`3c28614f12`](https://github.com/sgl-project/sglang/commit/3c28614f12) [#43108](https://github.com/sgl-project/sglang/pull/43108)
  [Fix] hicache: Defer query beliefs until the rank-synchronized hit drain (#43108)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_buffer_mode_sidecar.py`, `test/registered/unit/mem_cache/test_storage_prefetch_lifecycle.py`_
- **2026-10-14** [`e7d6a88bfc`](https://github.com/sgl-project/sglang/commit/e7d6a88bfc) [#43932](https://github.com/sgl-project/sglang/pull/43932)
  [HiCache] Buffer-only L3 for an auxiliary SWA window; load back only missing window rows (#43932)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/hicache_storage.py` _+18 more__
- **2026-10-14** [`c964d9ba20`](https://github.com/sgl-project/sglang/commit/c964d9ba20) [#42818](https://github.com/sgl-project/sglang/pull/42818)
  [Feat] sgl-router: Separate LoRA block IDs from prompt lookup keys (#42818)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/README.md`, `experimental/sgl-router/sgl-kv-indexer/Cargo.toml`, `experimental/sgl-router/sgl-kv-indexer/README.md` _+37 more__
- **2026-10-14** [`4f5fcbfef5`](https://github.com/sgl-project/sglang/commit/4f5fcbfef5) [#41147](https://github.com/sgl-project/sglang/pull/41147)
  [JIT] Clean up kernel headers: move runtime helpers, add once.h (#41147)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/topk_bf16_small.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh` _+16 more__
- **2026-10-13** [`01f3ed18a5`](https://github.com/sgl-project/sglang/commit/01f3ed18a5) [#43919](https://github.com/sgl-project/sglang/pull/43919)
  [unified memory pool] Prefer SWA reclaim quotas with a HiCache storage backend or on PD decode (#43919)
  _Files: `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py`, `test/registered/unit/mem_cache/test_multi_ended_allocator.py`_
- **2026-10-13** [`7e3da1b784`](https://github.com/sgl-project/sglang/commit/7e3da1b784) [#43870](https://github.com/sgl-project/sglang/pull/43870)
  [HiCache] Extract the buffer-mode prefetch and load-back lifecycle into pipeline operations (#43870)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/unified_cache/components/base.py`, `python/sglang/srt/mem_cache/unified_cache/components/full.py` _+2 more__
- **2026-10-13** [`a8381d73be`](https://github.com/sgl-project/sglang/commit/a8381d73be) [#43868](https://github.com/sgl-project/sglang/pull/43868)
  [HiCache] Block-group pool hits, caller-owned load destinations, allocation-target FULL eviction (#43868)
  _Files: `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py` _+2 more__
- **2026-10-13** [`6ade23696d`](https://github.com/sgl-project/sglang/commit/6ade23696d) [#43920](https://github.com/sgl-project/sglang/pull/43920)
  [Core] Keep request priority within the signed 64-bit range in radix caches (#43920)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py` _+2 more__
- **2026-10-13** [`c0584cf9af`](https://github.com/sgl-project/sglang/commit/c0584cf9af) [#41951](https://github.com/sgl-project/sglang/pull/41951)
  [perf] [multi-lora] remove empty CTAs from fused LoRA expand and add split-K to shrink (#41951)
  _Files: `benchmark/kernels/lora_csgmv/bench_csgmv_split_k.py`, `benchmark/kernels/lora_csgmv/tune_lora_csgmv.py`, `python/sglang/kernels/ops/lora/dense/chunked_sgmv_expand.py`, `python/sglang/kernels/ops/lora/dense/chunked_sgmv_shrink.py` _+3 more__
- **2026-10-13** [`45418d7dc6`](https://github.com/sgl-project/sglang/commit/45418d7dc6) [#42077](https://github.com/sgl-project/sglang/pull/42077)
  [HiCache] Avoid full-store scans for uncached file prefix lookups (#42077)
  _Files: `python/sglang/srt/mem_cache/hicache_storage.py`, `test/registered/unit/mem_cache/test_hicache_file_lru_unit.py`_
- **2026-10-12** [`6966c5d027`](https://github.com/sgl-project/sglang/commit/6966c5d027) [#42553](https://github.com/sgl-project/sglang/pull/42553)
  [ROCm] Eliminate HiCache migration stalls and use exact-size host allocations (#42553)
  _Files: `benchmark/hicache/bench_host_memory_migration.py`, `python/sglang/srt/mem_cache/pool_host/common.py`, `test/registered/unit/mem_cache/test_hicache_host_register.py`_
- **2026-10-12** [`a70a83bcd2`](https://github.com/sgl-project/sglang/commit/a70a83bcd2) [#43594](https://github.com/sgl-project/sglang/pull/43594)
  Keep NIXL Mamba checkpoint keys separate by TP rank (#43594)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/hicache_nixl.py`, `test/registered/unit/mem_cache/test_hicache_nixl_storage.py`_
- **2026-10-12** [`5ca0695aa6`](https://github.com/sgl-project/sglang/commit/5ca0695aa6) [#40223](https://github.com/sgl-project/sglang/pull/40223)
  [HiCache] Preserve all MTP KV and recurrent state (#40223)
  _Files: `python/sglang/srt/configs/inkling.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/mem_cache/base_swa_memory_pool.py`, `python/sglang/srt/mem_cache/cache_init_params.py` _+12 more__
- **2026-10-12** [`f5f5003323`](https://github.com/sgl-project/sglang/commit/f5f5003323) [#36345](https://github.com/sgl-project/sglang/pull/36345)
  [HiCache] Support Mamba in buffer-only host memory mode (#36345)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/storage_prefetch.py`, `python/sglang/srt/mem_cache/unified_cache/components/base.py` _+7 more__
- **2026-10-12** [`20c49f12c9`](https://github.com/sgl-project/sglang/commit/20c49f12c9) [#40925](https://github.com/sgl-project/sglang/pull/40925)
  Support kv cache sharding for DSA indexer (#40925)
  _Files: `python/sglang/srt/mem_cache/page_interleave_pool.py`, `test/registered/unit/mem_cache/test_page_interleave_shard.py`_
- **2026-10-12** [`77a15cf4e2`](https://github.com/sgl-project/sglang/commit/77a15cf4e2) [#43722](https://github.com/sgl-project/sglang/pull/43722)
  [MemCache] Add shared component size and path APIs to the tree core interface (#43722)
  _Files: `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/components/base.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py` _+6 more__
- **2026-10-12** [`e4cfc0c42a`](https://github.com/sgl-project/sglang/commit/e4cfc0c42a) [#43721](https://github.com/sgl-project/sglang/pull/43721)
  [MemCache] Split the SWA mapping move out of locked-full recovery as `RecoverEvictedSWA` (#43721)
  _Files: `python/sglang/srt/mem_cache/unified_cache/cache_action.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa.py`, `test/registered/unit/mem_cache/test_swa_locked_full_recover_unified.py`_

## Prefill / Decode Disaggregation  (43 commits)

- **2026-10-19** [`33dd8f6a2e`](https://github.com/sgl-project/sglang/commit/33dd8f6a2e) [#34535](https://github.com/sgl-project/sglang/pull/34535)
  [Fix] hybrid-SSM: DP attention failures at low concurrency (#34535)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` _+12 more__
- **2026-10-19** [`82c9a8b037`](https://github.com/sgl-project/sglang/commit/82c9a8b037) [#45075](https://github.com/sgl-project/sglang/pull/45075)
  [Perf] deepseek-v4.1: Default PD to MegaAttention, with the KV layout in the PD handshake (#45075)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py` _+5 more__
- **2026-10-19** [`69076b9f9e`](https://github.com/sgl-project/sglang/commit/69076b9f9e) [#41675](https://github.com/sgl-project/sglang/pull/41675)
  [CI] [NPU] tests: Reduce HiCache sizes and enable expandable pinned memory in focused tests (#41675)
  _Files: `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py`, `test/registered/npu/accuracy/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms_aime26.py`, `test/registered/npu/basic_function/HiCache/test_npu_hicache_mha.py`, `test/registered/npu/basic_function/HiCache/test_npu_hicache_mla.py` _+5 more__
- **2026-10-18** [`fe89a7c890`](https://github.com/sgl-project/sglang/commit/fe89a7c890) [#45037](https://github.com/sgl-project/sglang/pull/45037)
  [Fix] deepseek-v4.1: Start the PD decode draft SWA window at the prefill draft valid-from (#45037)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_attn_metadata.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+9 more__
- **2026-10-18** [`5a930cfd88`](https://github.com/sgl-project/sglang/commit/5a930cfd88) [#43871](https://github.com/sgl-project/sglang/pull/43871)
  [Fix] glm4v: Clamp request video budgets to the deployment limit (#43871)
  _Files: `docs/docs/supported-models/multimodal_language_models.mdx`, `python/sglang/srt/disaggregation/encoder/preprocessor.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/multimodal/processors/glm4v.py` _+1 more__
- **2026-10-18** [`6c3db0f520`](https://github.com/sgl-project/sglang/commit/6c3db0f520) [#44740](https://github.com/sgl-project/sglang/pull/44740)
  [Perf] NIXL: prepared dlists for hybrid-model state transfer (#44740)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-10-18** [`889658a5be`](https://github.com/sgl-project/sglang/commit/889658a5be) [#43760](https://github.com/sgl-project/sglang/pull/43760)
  [Fix] disaggregation: Reuse startup decode graphs across PD role switches (#43760)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `test/registered/unit/disaggregation/test_pd_role_switch.py`_
- **2026-10-18** [`d33dd0566a`](https://github.com/sgl-project/sglang/commit/d33dd0566a) [#44666](https://github.com/sgl-project/sglang/pull/44666)
  [Feat] srt: Add muse spark runtime, multimodal support and tests (3/5) (#44666)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/rerun-test.yml`, `docker/muse_spark/muse-spark.Dockerfile`, `docs/docs/advanced_features/server_arguments.mdx` _+78 more__
- **2026-10-18** [`f1cf2e1005`](https://github.com/sgl-project/sglang/commit/f1cf2e1005) [#44412](https://github.com/sgl-project/sglang/pull/44412)
  [Fix] [AMD] mori: Look up elided DSA state entries by the paired dst index (#44412)
  _Files: `python/sglang/srt/disaggregation/mori/conn.py`, `test/registered/amd/disaggregation/test_mori_backend_basic.py`_
- **2026-10-18** [`396e97e5dd`](https://github.com/sgl-project/sglang/commit/396e97e5dd) [#44409](https://github.com/sgl-project/sglang/pull/44409)
  [CI] [AMD] ci/slurm: Add a Mooncake KV-transfer test to the MI355X disaggregation nightly (#44409)
  _Files: `scripts/ci/slurm/launch_mi355x.sh`, `scripts/ci/slurm/nightly-configs.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/dsv4flash/1k1k/1p1d-mooncake.yaml`_
- **2026-10-18** [`8a4239fbdc`](https://github.com/sgl-project/sglang/commit/8a4239fbdc) [#44404](https://github.com/sgl-project/sglang/pull/44404)
  [Fix] [AMD] mooncake: Bump Mooncake to v0.3.14-rc1 for cross-node KV transfer (#44404)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-18** [`df966f2345`](https://github.com/sgl-project/sglang/commit/df966f2345) [#44952](https://github.com/sgl-project/sglang/pull/44952)
  [Feat] deepseek-v4.1: Run encoder SWA bounded replay on PD prefill workers (#44952)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/mem_cache/base_swa_memory_pool.py` _+5 more__
- **2026-10-17** [`05c1539098`](https://github.com/sgl-project/sglang/commit/05c1539098) [#41343](https://github.com/sgl-project/sglang/pull/41343)
  [Feat] unified_cache: Support hybrid SWA + Mamba models in the Mooncake direct linker (#41343)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `python/sglang/srt/mem_cache/unified_cache/components/mamba.py` _+8 more__
- **2026-10-17** [`23f8e6f7ec`](https://github.com/sgl-project/sglang/commit/23f8e6f7ec) [#43732](https://github.com/sgl-project/sglang/pull/43732)
  [Fix] diffusion: keep ZMQ ingress sockets on their configured port (#43732)
  _Files: `python/sglang/multimodal_gen/runtime/disaggregation/orchestrator.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/runtime/utils/common.py`, `python/sglang/multimodal_gen/test/unit/test_zmq_bind_port.py`_
- **2026-10-16** [`989ccf4863`](https://github.com/sgl-project/sglang/commit/989ccf4863) [#44605](https://github.com/sgl-project/sglang/pull/44605)
  [Feat] disaggregation: Let a KV transfer backend skip the checksum for an incomparable peer (#44605)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_kv_checksum.py`_
- **2026-10-16** [`3a5d46e946`](https://github.com/sgl-project/sglang/commit/3a5d46e946) [#38955](https://github.com/sgl-project/sglang/pull/38955)
  [Perf] pd: Stage decode-side KV preallocation lengths through pinned memory (#38955)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/allocator/swa.py`, `test/registered/unit/disaggregation/test_decode_prealloc_no_host_sync.py`_
- **2026-10-16** [`f9df33494a`](https://github.com/sgl-project/sglang/commit/f9df33494a) [#44386](https://github.com/sgl-project/sglang/pull/44386)
  [Fix] scheduler: Keep PD decode non-idle while deferred KV releases are held (#44386)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-10-16** [`bda6ef7e01`](https://github.com/sgl-project/sglang/commit/bda6ef7e01) [#44568](https://github.com/sgl-project/sglang/pull/44568)
  [Perf] [NVIDIA] scheduler: Pageable host staging and inline hidden-state/DSpark readback under Confidential Computing (#44568)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/utils/common.py`, `test/registered/unit/disaggregation/test_prefill_result_polling.py`, `test/registered/unit/managers/test_async_d2h_copy_worker.py`_
- **2026-10-16** [`ed8c3139f1`](https://github.com/sgl-project/sglang/commit/ed8c3139f1) [#41303](https://github.com/sgl-project/sglang/pull/41303)
  [Fix] deepseek-v4.1: Keep the full SWA window for short bounded-replay extends (#41303)
  _Files: `python/sglang/kernels/ops/attention/dsv4_attn_metadata_kernels.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` _+10 more__
- **2026-10-16** [`d14fa5db9b`](https://github.com/sgl-project/sglang/commit/d14fa5db9b) [#44598](https://github.com/sgl-project/sglang/pull/44598)
  [Perf] pd: Copy prebuilt decode batch inputs to the GPU without host syncs (#44598)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/speculative/eagle_disaggregation.py`, `python/sglang/srt/utils/common.py`_
- **2026-10-15** [`aa5c7e887c`](https://github.com/sgl-project/sglang/commit/aa5c7e887c) [#41006](https://github.com/sgl-project/sglang/pull/41006)
  [Feat] docker: Add AWS EFA image variants built on published images (#41006)
  _Files: `.github/workflows/release-docker-efa.yml`, `docker/efa.Dockerfile`, `docs/docs/advanced_features/pd_disaggregation.mdx`, `docs/docs/get-started/install.mdx` _+2 more__
- **2026-10-15** [`87211088c9`](https://github.com/sgl-project/sglang/commit/87211088c9) [#36810](https://github.com/sgl-project/sglang/pull/36810)
  perf: fix overlap scheduling for NVIDIA Confidential Computing(CC) on Blackwell (#36810)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/async_d2h_copy_worker.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/utils.py` _+4 more__
- **2026-10-15** [`2528cd2b91`](https://github.com/sgl-project/sglang/commit/2528cd2b91) [#44140](https://github.com/sgl-project/sglang/pull/44140)
  [PD] Send DSA indexer state only past decode_prefix_len (#44140)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/mem_cache/common.py`_
- **2026-10-14** [`2a9f6a25a7`](https://github.com/sgl-project/sglang/commit/2a9f6a25a7) [#44113](https://github.com/sgl-project/sglang/pull/44113)
  [Core] Add subclass hooks for the generation request class and optimistic prefill eligibility (#44113)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/session/session_controller.py` _+2 more__
- **2026-10-14** [`5f2861bf59`](https://github.com/sgl-project/sglang/commit/5f2861bf59) [#44112](https://github.com/sgl-project/sglang/pull/44112)
  [Perf] session: Cache multimodal prompt token counts across turns (#44112)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py` _+6 more__
- **2026-10-14** [`d3dc14eb38`](https://github.com/sgl-project/sglang/commit/d3dc14eb38) [#40857](https://github.com/sgl-project/sglang/pull/40857)
  [mem_cache][PD] Fix decode radix cache ownership and allow EAGLE/EAGLE3 with decode radix cache (#40857)
  _Files: `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+2 more__
- **2026-10-14** [`010776e94f`](https://github.com/sgl-project/sglang/commit/010776e94f) [#42817](https://github.com/sgl-project/sglang/pull/42817)
  [KV events] Publish opaque LoRA block IDs and adapter names (#42817)
  _Files: `python/sglang/srt/disaggregation/kv_events.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+14 more__
- **2026-10-14** [`0d130f1915`](https://github.com/sgl-project/sglang/commit/0d130f1915) [#39724](https://github.com/sgl-project/sglang/pull/39724)
  [Qwen3.8 CP 4/4] Prefill context parallel E2E support of Qwen3.8 (#39724)
  _Files: `python/sglang/srt/arg_groups/cp_tp_group_sharing_hook.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py` _+12 more__
- **2026-10-14** [`7ca4cbfcef`](https://github.com/sgl-project/sglang/commit/7ca4cbfcef) [#44002](https://github.com/sgl-project/sglang/pull/44002)
  [Disagg] Return prompt routed experts from the PD prefill server (#44002)
  _Files: `python/sglang/srt/disaggregation/prefill.py`_
- **2026-10-13** [`18210ed849`](https://github.com/sgl-project/sglang/commit/18210ed849) [#37771](https://github.com/sgl-project/sglang/pull/37771)
  [HiSparse] Add speculative decoding support with multi-step KV cache swapping (#37771)
  _Files: `python/sglang/srt/arg_groups/hisparse_hook.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+27 more__
- **2026-10-13** [`149ef7d1b7`](https://github.com/sgl-project/sglang/commit/149ef7d1b7) [#43924](https://github.com/sgl-project/sglang/pull/43924)
  [Rust] Let an embedding package wrap the frontend HTTP app (#43924)
  _Files: `rust/sglang-server/src/api_server/disaggregation/bootstrap.rs`, `rust/sglang-server/src/api_server/http/app.rs`, `rust/sglang-server/src/lib.rs`, `rust/sglang-server/src/utils/runtime.rs`_
- **2026-10-13** [`e0c957e222`](https://github.com/sgl-project/sglang/commit/e0c957e222) [#41769](https://github.com/sgl-project/sglang/pull/41769)
  [HiCache][PD] Allow DSA index-K elision under HiCache and disaggregation (#41769)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `python/sglang/srt/disaggregation/utils.py` _+3 more__
- **2026-10-13** [`35a014c7e8`](https://github.com/sgl-project/sglang/commit/35a014c7e8) [#43723](https://github.com/sgl-project/sglang/pull/43723)
  [PD][NIXL] Fix staging buffer startup by accepting slot_layer_ids (#43723)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-10-13** [`50a144057c`](https://github.com/sgl-project/sglang/commit/50a144057c) [#37358](https://github.com/sgl-project/sglang/pull/37358)
  [AMD][PD] enable mori transfer for PD decode DCP (#37358)
  _Files: `.github/workflows/pr-test-amd-mori.yml`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/mori/conn.py`, `test/registered/amd/disaggregation/test_mori_backend_basic.py` _+1 more__
- **2026-10-13** [`3eebf987ed`](https://github.com/sgl-project/sglang/commit/3eebf987ed) [#40909](https://github.com/sgl-project/sglang/pull/40909)
  [PD] Support heterogeneous TP for hybrid SWA KV transfer (#40909)
  _Files: `docs/docs/advanced_features/pd_disaggregation.mdx`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+5 more__
- **2026-10-13** [`43e4e84731`](https://github.com/sgl-project/sglang/commit/43e4e84731) [#43936](https://github.com/sgl-project/sglang/pull/43936)
  [PD] Recompute retracted DeepSeek-V4 requests on prefill instead of crashing decode (#43936)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `test/registered/disaggregation/test_disaggregation_dsv4.py` _+2 more__
- **2026-10-13** [`e775fa7253`](https://github.com/sgl-project/sglang/commit/e775fa7253) [#43021](https://github.com/sgl-project/sglang/pull/43021)
  [Build][CI] Drop Python 3.10: require Python 3.11+ and run CUDA CI on Python 3.12 (#43021)
  _Files: `.github/actions/download-rust-ext/action.yml`, `.github/workflows/_pr-test-rust-ext-build.yml`, `.github/workflows/_pr-test-simulator-cpu.yml`, `.github/workflows/_pr-test-stage-cpu.yml` _+35 more__
- **2026-10-12** [`f92199b569`](https://github.com/sgl-project/sglang/commit/f92199b569) [#40896](https://github.com/sgl-project/sglang/pull/40896)
  [Unified Cache] Abort requests whose external linker load fails instead of crashing the scheduler (#40896)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py` _+15 more__
- **2026-10-12** [`7953751bfa`](https://github.com/sgl-project/sglang/commit/7953751bfa) [#41783](https://github.com/sgl-project/sglang/pull/41783)
  [PD][Spec] Give a PD decode's first EAGLE draft step a proposal distribution (#41783)
  _Files: `python/sglang/srt/speculative/eagle_disaggregation.py`, `test/registered/unit/speculative/test_pd_eagle_draft_proposal.py`_
- **2026-10-12** [`62ff466ac0`](https://github.com/sgl-project/sglang/commit/62ff466ac0) [#40323](https://github.com/sgl-project/sglang/pull/40323)
  [DSV4.1][PD][1/N] Support prefill node use cp parallel strategy (#40323)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` _+5 more__
- **2026-10-12** [`4195980f5a`](https://github.com/sgl-project/sglang/commit/4195980f5a) [#43719](https://github.com/sgl-project/sglang/pull/43719)
  [PD] Poison the deferred abort ack when a Mooncake send fails (#43719)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `test/registered/unit/disaggregation/test_deferred_decode_kv_release.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py` _+1 more__
- **2026-10-12** [`9e0b001db4`](https://github.com/sgl-project/sglang/commit/9e0b001db4) [#43769](https://github.com/sgl-project/sglang/pull/43769)
  [CI] Skip eval retries in the PD transfer-failure test (#43769)
  _Files: `test/registered/disaggregation/test_disaggregation_basic.py`_
- **2026-10-12** [`a1001bcf3a`](https://github.com/sgl-project/sglang/commit/a1001bcf3a) [#43757](https://github.com/sgl-project/sglang/pull/43757)
  [PD] Retract transferred decode requests on a retract pause (#43757)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_flush_cache_after_retract.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_

## MoE / Expert Parallel  (30 commits)

- **2026-10-19** [`8e7601ae4a`](https://github.com/sgl-project/sglang/commit/8e7601ae4a) [#42557](https://github.com/sgl-project/sglang/pull/42557)
  [Feat] paged-experts: Serve MoE models whose weights do not fit VRAM (#42557)
  _Files: `docs/docs.json`, `docs/docs/advanced_features/paged_experts.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/kernels/jit/csrc/moe/paged_experts.cuh` _+19 more__
- **2026-10-19** [`ed0b8f433f`](https://github.com/sgl-project/sglang/commit/ed0b8f433f) [#43837](https://github.com/sgl-project/sglang/pull/43837)
  [Fix] [NPU] kimi-k3: skip fused gmm1 for situ activation in Ascend runner (#43837)
  _Files: `python/sglang/kernels/ops/attention/mla_output_gate.py`, `python/sglang/srt/layers/moe/moe_runner/ascend.py`_
- **2026-10-19** [`7c9a78efbe`](https://github.com/sgl-project/sglang/commit/7c9a78efbe) [#44518](https://github.com/sgl-project/sglang/pull/44518)
  [Feat] nemotron: Port Nemotron 3.5 Super serving changes (#44518)
  _Files: `python/sglang/kernels/jit/csrc/gemm/hopper_bf16_gemv.cuh`, `python/sglang/kernels/jit/csrc/gemm/sm120_fp8_gemv.cuh`, `python/sglang/kernels/jit/csrc/gemm/sm120_nvfp4_moe_mtp_mma.cuh`, `python/sglang/kernels/jit/csrc/gemm/sm120_nvfp4_weight_transpose.cuh` _+19 more__
- **2026-10-19** [`266550048a`](https://github.com/sgl-project/sglang/commit/266550048a) [#44715](https://github.com/sgl-project/sglang/pull/44715)
  [Fix] bailing: MoE gate dtype follows config.router_dtype (#44715)
  _Files: `python/sglang/srt/models/bailing_moe_v3.py`_
- **2026-10-17** [`7a8804edb5`](https://github.com/sgl-project/sglang/commit/7a8804edb5) [#40516](https://github.com/sgl-project/sglang/pull/40516)
  [Fix] [NPU] qwen: Fix shared-expert routing with Ascend FuseEP (#40516)
  _Files: `python/sglang/srt/models/qwen2_moe.py`_
- **2026-10-17** [`14c4dda24e`](https://github.com/sgl-project/sglang/commit/14c4dda24e) [#44837](https://github.com/sgl-project/sglang/pull/44837)
  [Perf] deepseek_v4: fuse block-FP8 shared experts into MegaMoE for any 32-aligned block size (#44837)
  _Files: `python/sglang/srt/layers/moe/mega_moe.py`_
- **2026-10-17** [`9259553f09`](https://github.com/sgl-project/sglang/commit/9259553f09) [#44847](https://github.com/sgl-project/sglang/pull/44847)
  [Fix] megamoe: Support EPLB rebalance on SM100 (#44847)
  _Files: `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`_
- **2026-10-17** [`ff979e0816`](https://github.com/sgl-project/sglang/commit/ff979e0816) [#44816](https://github.com/sgl-project/sglang/pull/44816)
  [Fix] megamoe: Respect request-pool limits in decode validation (#44816)
  _Files: `python/sglang/srt/arg_groups/mega_moe_hook.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-10-16** [`456231e251`](https://github.com/sgl-project/sglang/commit/456231e251) [#44665](https://github.com/sgl-project/sglang/pull/44665)
  [Feat] kernels: Add muse spark operators and collective GEMM (2/5) (#44665)
  _Files: `python/sglang/kernels/README.md`, `python/sglang/kernels/aot/csrc/cpu/extend.cpp`, `python/sglang/kernels/fused_op.py`, `python/sglang/kernels/jit/csrc/distributed/custom_all_reduce.cuh` _+40 more__
- **2026-10-16** [`4afae5568b`](https://github.com/sgl-project/sglang/commit/4afae5568b) [#44657](https://github.com/sgl-project/sglang/pull/44657)
  [Perf] [AMD] dsv4: Add a separate MegaMoE decode instance (#44657)
  _Files: `python/sglang/srt/arg_groups/mega_moe_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe_flydsl.py`, `test/registered/unit/layers/moe/test_mega_moe_decode_capacity.py`_
- **2026-10-16** [`9fde8bcc46`](https://github.com/sgl-project/sglang/commit/9fde8bcc46) [#44004](https://github.com/sgl-project/sglang/pull/44004)
  [Perf] [AMD] moe: small-batch sort with histogram + bitonic sort for 32 < P <= 256 (3/8) (#44004)
  _Files: `python/sglang/kernels/ops/moe/moe_sorting_small.py`, `test/registered/amd/test_moe_sorting_small.py`_
- **2026-10-16** [`7098ec387c`](https://github.com/sgl-project/sglang/commit/7098ec387c) [#44036](https://github.com/sgl-project/sglang/pull/44036)
  [Feat] FlashInfer: Add NVFP4 W4A16 and SiTU support to MegaMoE (#44036)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/moe_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/environ.py` _+11 more__
- **2026-10-16** [`a93f16f0cf`](https://github.com/sgl-project/sglang/commit/a93f16f0cf) [#43922](https://github.com/sgl-project/sglang/pull/43922)
  [Perf] deepseek-v4.1: Integrate FlashMLA MegaAttention with NVFP4 KV (#43922)
  _Files: `python/pyproject.toml`, `python/sglang/kernels/ops/attention/deepseek_v4_rope.py`, `python/sglang/kernels/ops/moe/dsv4.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` _+8 more__
- **2026-10-15** [`4e0609ea27`](https://github.com/sgl-project/sglang/commit/4e0609ea27) [#40498](https://github.com/sgl-project/sglang/pull/40498)
  [Fix] moe: Preserve negative routing sentinel in EP mapping (#40498)
  _Files: `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/moe/token_dispatcher/standard.py`, `test/registered/unit/layers/moe/test_standard_dispatcher.py`_
- **2026-10-15** [`6fe5596ebb`](https://github.com/sgl-project/sglang/commit/6fe5596ebb) [#43685](https://github.com/sgl-project/sglang/pull/43685)
  Support EPLB for Nemotron-H (#43685)
  _Files: `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_mtp.py` _+3 more__
- **2026-10-15** [`f7ad4345b8`](https://github.com/sgl-project/sglang/commit/f7ad4345b8) [#43607](https://github.com/sgl-project/sglang/pull/43607)
  [Refactor] deepseek-v4: Use explicit stage boundaries and row transport (#43607)
  _Files: `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py`, `python/sglang/srt/layers/layer_boundary/factories.py` _+29 more__
- **2026-10-15** [`d4daf52369`](https://github.com/sgl-project/sglang/commit/d4daf52369) [#44347](https://github.com/sgl-project/sglang/pull/44347)
  [Fix] dsv41: Bound MoE routing to live SWA graph-tail rows (#44347)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-10-14** [`87ed1b9526`](https://github.com/sgl-project/sglang/commit/87ed1b9526) [#33728](https://github.com/sgl-project/sglang/pull/33728)
  [4/N] elastic-ep: Scale at DP-attention replica granularity (#33728)
  _Files: `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/elastic_ep/elastic_ep.py`, `python/sglang/srt/elastic_ep/topology.py`, `python/sglang/srt/layers/dcp/comm.py` _+14 more__
- **2026-10-14** [`c54ba66cd4`](https://github.com/sgl-project/sglang/commit/c54ba66cd4) [#43639](https://github.com/sgl-project/sglang/pull/43639)
  [Perf] Enable native MXFP4 routing and CuTeDSL fusion for MiMo (#43639)
  _Files: `python/sglang/kernels/ops/moe/smallm_router_gfx950/__init__.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/flashinfer_mnnvl_cutedsl.py` _+4 more__
- **2026-10-14** [`13a6dee99b`](https://github.com/sgl-project/sglang/commit/13a6dee99b) [#42837](https://github.com/sgl-project/sglang/pull/42837)
  [Fix] moe_sum_reduce: gate the bf16 vectorized path on hidden % 16 (#42837)
  _Files: `python/sglang/kernels/aot/csrc/moe/moe_sum_reduce.cu`_
- **2026-10-13** [`74e0a47863`](https://github.com/sgl-project/sglang/commit/74e0a47863) [#40022](https://github.com/sgl-project/sglang/pull/40022)
  Fix/compressed tensors nvfp4 hopper (#40022)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/README.md`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a16_nvfp4.py` _+4 more__
- **2026-10-13** [`01f6840693`](https://github.com/sgl-project/sglang/commit/01f6840693) [#43789](https://github.com/sgl-project/sglang/pull/43789)
  [FlashInfer] Add startup autotuning for MegaMoE (#43789)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/flashinfer_megamoe.py`, `python/sglang/srt/layers/moe/flashinfer_megamoe_autotune.py` _+5 more__
- **2026-10-13** [`27be99ae73`](https://github.com/sgl-project/sglang/commit/27be99ae73) [#40772](https://github.com/sgl-project/sglang/pull/40772)
  [NVIDIA][MegaMoE] Fix the default spec decoding moe backend when the target model uses flashinfer megamoe (#40772)
  _Files: `python/sglang/srt/arg_groups/fields/spec.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/moe/utils.py`, `test/registered/unit/test_model_overrides.py` _+1 more__
- **2026-10-13** [`40f5d9411f`](https://github.com/sgl-project/sglang/commit/40f5d9411f) [#43939](https://github.com/sgl-project/sglang/pull/43939)
  Reuse Hugging Face LFM2-MoE configuration (#43939)
  _Files: `python/sglang/srt/configs/lfm2_moe.py`_
- **2026-10-13** [`03416e8c0f`](https://github.com/sgl-project/sglang/commit/03416e8c0f) [#43563](https://github.com/sgl-project/sglang/pull/43563)
  [Fix] Account for captured inputs in DeepGEMM masked workspace budget (#43563)
  _Files: `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`, `test/registered/kernels/ops/moe/test_minimax_quant_scatter.py`_
- **2026-10-12** [`06887827c7`](https://github.com/sgl-project/sglang/commit/06887827c7) [#43784](https://github.com/sgl-project/sglang/pull/43784)
  [CI] Move tests that do not need GB300 off the per-PR GB300 suite (#43784)
  _Files: `test/registered/e2e/models/test_deepseek_v41_flash_gb300.py`, `test/registered/e2e/models_large/test_deepseek_v3_cutedsl_4gpu.py`, `test/registered/ep/test_flashinfer_a2a.py`, `test/registered/kernels/ops/attention/test_flash_attention_4_sm103.py` _+2 more__
- **2026-10-12** [`166b4ae7fc`](https://github.com/sgl-project/sglang/commit/166b4ae7fc) [#43688](https://github.com/sgl-project/sglang/pull/43688)
  [Fix] Adapt to transformers 5.18 / 5.19 changes (#43688)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `python/sglang/multimodal_gen/runtime/models/encoders/hunyuan3d.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/configs/granitemoehybrid.py` _+5 more__
- **2026-10-12** [`0d0be8fc98`](https://github.com/sgl-project/sglang/commit/0d0be8fc98) [#40666](https://github.com/sgl-project/sglang/pull/40666)
  [AMD][MORI] Add MORI EP V2 support (#40666)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/moe_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/eplb/expert_distribution.py` _+13 more__
- **2026-10-12** [`37d2e5c34f`](https://github.com/sgl-project/sglang/commit/37d2e5c34f) [#43077](https://github.com/sgl-project/sglang/pull/43077)
  [AMD][V4.1][*/N] Fix DP attention + TP MoE decode NaN and support bounded replay (#43077)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+3 more__
- **2026-10-12** [`0c52cb1519`](https://github.com/sgl-project/sglang/commit/0c52cb1519) [#42212](https://github.com/sgl-project/sglang/pull/42212)
  [MoE] Skip block-padding rows in the TMA down activation and quant (#42212)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/activation.cuh`, `python/sglang/kernels/jit/csrc/gemm/per_token_group_quant.cuh`, `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/kernels/ops/quantization/per_token_group_quant.py` _+4 more__

## Tensor / Data Parallel  (28 commits)

- **2026-10-19** [`f86a04a331`](https://github.com/sgl-project/sglang/commit/f86a04a331) [#44402](https://github.com/sgl-project/sglang/pull/44402)
  [Feat] sgl-router: Add --decode-dispatch-limit to pick decode DP ranks near KV arrival (#44402)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/REFERENCE.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs` _+8 more__
- **2026-10-19** [`06342acad2`](https://github.com/sgl-project/sglang/commit/06342acad2) [#45062](https://github.com/sgl-project/sglang/pull/45062)
  [Perf] deepseek-v4.1: Stage late-layer DP row counts through pinned memory (#45062)
  _Files: `python/sglang/srt/models/deepseek_common/decoder_swa_bounded_replay.py`_
- **2026-10-18** [`3671503e44`](https://github.com/sgl-project/sglang/commit/3671503e44) [#43967](https://github.com/sgl-project/sglang/pull/43967)
  [Feat] bench: report goodput and SLO attainment in bench_serving (#43967)
  _Files: `docs/docs/developer_guide/bench_serving.mdx`, `python/sglang/benchmark/goodput.py`, `python/sglang/benchmark/serving.py`, `test/registered/unit/bench/test_bench_serving_goodput.py`_
- **2026-10-18** [`14ad64c411`](https://github.com/sgl-project/sglang/commit/14ad64c411) [#44158](https://github.com/sgl-project/sglang/pull/44158)
  [Perf] custom_op: call register_custom_op ops directly in plain eager execution (#44158)
  _Files: `python/sglang/srt/utils/custom_op.py`, `test/registered/cuda_graph/breakable/test_deepseek_dual_stream_outputs.py`, `test/registered/unit/utils/test_custom_op_eager_direct.py`_
- **2026-10-18** [`f53bd436c1`](https://github.com/sgl-project/sglang/commit/f53bd436c1) [#44642](https://github.com/sgl-project/sglang/pull/44642)
  [Perf] distributed: cache the eager launch of custom all-reduce v2 per size (#44642)
  _Files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `test/registered/kernels/ops/communication/test_custom_all_reduce.py`_
- **2026-10-17** [`01dc08e23f`](https://github.com/sgl-project/sglang/commit/01dc08e23f) [#42787](https://github.com/sgl-project/sglang/pull/42787)
  [Refactor] dsv41: Shard Engram tables on hash-column boundaries (#42787)
  _Files: `python/sglang/srt/layers/engram.py`, `test/registered/unit/models/test_deepseek_v4_amd_tp4.py`_
- **2026-10-17** [`4fc86f73c2`](https://github.com/sgl-project/sglang/commit/4fc86f73c2) [#44597](https://github.com/sgl-project/sglang/pull/44597)
  [CI] glm5.2: Keep EOS in HiSparse needle test output (#44597)
  _Files: `test/registered/e2e/models/test_dsa_glm52_hisparse.py`_
- **2026-10-16** [`d5d87899f9`](https://github.com/sgl-project/sglang/commit/d5d87899f9) [#43832](https://github.com/sgl-project/sglang/pull/43832)
  [Fix] DSA: skip-topk pipeline handoff for owed outputs (#43832)
  _Files: `python/sglang/srt/models/deepseek_v2.py`, `test/registered/unit/models/test_deepseek_pp_mtp_embedding.py`_
- **2026-10-16** [`07950be745`](https://github.com/sgl-project/sglang/commit/07950be745) [#42811](https://github.com/sgl-project/sglang/pull/42811)
  [Perf] [NVIDIA] custom-all-reduce: Add 2shot_push all-reduce and retune SM100 TP4/TP8 (#42811)
  _Files: `python/sglang/kernels/jit/csrc/distributed/custom_all_reduce.cuh`, `python/sglang/srt/distributed/device_communicators/configs/custom_all_reduce_v2.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `test/registered/kernels/ops/communication/test_custom_all_reduce.py`_
- **2026-10-16** [`63a9b7a713`](https://github.com/sgl-project/sglang/commit/63a9b7a713) [#44583](https://github.com/sgl-project/sglang/pull/44583)
  [Feat] http_server: Make the multi-worker ASGI app path configurable (#44583)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/environ.py`_
- **2026-10-16** [`26a2f18c02`](https://github.com/sgl-project/sglang/commit/26a2f18c02) [#44532](https://github.com/sgl-project/sglang/pull/44532)
  [Feat] sglang-server: serve /v1/loads from the Rust frontend (#44532)
  _Files: `python/sglang/srt/rust_server/config.py`, `rust/Cargo.lock`, `rust/sglang-server/Cargo.toml`, `rust/sglang-server/src/api_server/http.rs` _+6 more__
- **2026-10-16** [`a2981ab8ea`](https://github.com/sgl-project/sglang/commit/a2981ab8ea) [#42674](https://github.com/sgl-project/sglang/pull/42674)
  [Feat] sgl-router: Serve native gRPC ChatComplete (#42674)
  _Files: `.github/workflows/pr-test-sgl-router.yml`, `docker/sgl-router.Dockerfile`, `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml` _+23 more__
- **2026-10-16** [`2957ff3165`](https://github.com/sgl-project/sglang/commit/2957ff3165) [#42637](https://github.com/sgl-project/sglang/pull/42637)
  [Fix] sglang-server: Keep the matched stop token in output_ids (#42637)
  _Files: `rust/sglang-server/src/api_server/core/frame.rs`, `rust/sglang-server/src/api_server/grpc/service.rs`, `rust/sglang-server/src/api_server/http/openai/chat.rs`, `rust/sglang-server/src/message/response.rs` _+1 more__
- **2026-10-15** [`ec7ab9d0c2`](https://github.com/sgl-project/sglang/commit/ec7ab9d0c2) [#44353](https://github.com/sgl-project/sglang/pull/44353)
  [Feat] [AMD] monokernels: one runtime switch for vendor monokernel plugins (#44353)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/pyproject_other.toml`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/pipeline.py` _+9 more__
- **2026-10-15** [`a57707377f`](https://github.com/sgl-project/sglang/commit/a57707377f) [#44072](https://github.com/sgl-project/sglang/pull/44072)
  [Fix] sgl-router: Send disagg_prefill_dp_rank to decode under --dp-aware (#44072)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/server/routes/chat/forward.rs`, `experimental/sgl-router/tests/proxy/dp_rank_routing.rs`_
- **2026-10-15** [`3a835cf417`](https://github.com/sgl-project/sglang/commit/3a835cf417) [#43606](https://github.com/sgl-project/sglang/pull/43606)
  [Refactor] inkling: Use short-convolution stage boundaries (#43606)
  _Files: `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py`, `python/sglang/srt/layers/layer_boundary/exit.py` _+21 more__
- **2026-10-15** [`fa66e7d816`](https://github.com/sgl-project/sglang/commit/fa66e7d816) [#29753](https://github.com/sgl-project/sglang/pull/29753)
  [NPU] [Bugfix] Fix rope sin cos pre-calculation for Qwen3.5 during Pipeline Parallelism (#29753)
  _Files: `python/sglang/srt/models/interns2_mobius.py`, `python/sglang/srt/models/qwen3_5.py`, `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`_
- **2026-10-15** [`08f15e76bb`](https://github.com/sgl-project/sglang/commit/08f15e76bb) [#43511](https://github.com/sgl-project/sglang/pull/43511)
  [Feat] sgl-router: Add --dp-rank-policy round_robin for --dp-aware (#43511)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs` _+27 more__
- **2026-10-14** [`9732188a58`](https://github.com/sgl-project/sglang/commit/9732188a58) [#43926](https://github.com/sgl-project/sglang/pull/43926)
  [Rust] Serve /weights_checker from the Rust frontend (#43926)
  _Files: `rust/Cargo.lock`, `rust/sglang-server/Cargo.toml`, `rust/sglang-server/src/api_server/core/handle.rs`, `rust/sglang-server/src/api_server/http/info.rs` _+1 more__
- **2026-10-14** [`12dc623102`](https://github.com/sgl-project/sglang/commit/12dc623102) [#43451](https://github.com/sgl-project/sglang/pull/43451)
  [Chore] rust: Remove the sglang-renderer crate (#43451)
  _Files: `.agents/skills/processor-model-parity/SKILL.md`, `.github/CODEOWNERS`, `.github/labeler.yml`, `.github/workflows/_pr-test-check-changes.yml` _+50 more__
- **2026-10-14** [`e00754bab1`](https://github.com/sgl-project/sglang/commit/e00754bab1) [#44144](https://github.com/sgl-project/sglang/pull/44144)
  [DSV4.1] Derive the late-layer DP geometry from the captured shape under the breakable prefill graph (#44144)
  _Files: `python/sglang/srt/models/deepseek_common/decoder_swa_bounded_replay.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-14** [`ff8d964cf5`](https://github.com/sgl-project/sglang/commit/ff8d964cf5) [#44192](https://github.com/sgl-project/sglang/pull/44192)
  [CI] glm5.2: Temporarily disable PD HiSparse+MTP B300 test (#44192)
  _Files: `test/registered/e2e/models/test_dsa_glm52_hisparse.py`_
- **2026-10-13** [`684fea8af3`](https://github.com/sgl-project/sglang/commit/684fea8af3) [#43993](https://github.com/sgl-project/sglang/pull/43993)
  [DSV4.1] Skip Mega mHC fusion on 0-row (DP-idle) batches (#43993)
  _Files: `python/sglang/srt/models/deepseek_v4_mhc.py`_
- **2026-10-13** [`ce5352a814`](https://github.com/sgl-project/sglang/commit/ce5352a814) [#43923](https://github.com/sgl-project/sglang/pull/43923)
  [Rust] Serve any `model` name on the OpenAI chat and completions routes (#43923)
  _Files: `rust/sglang-server/src/api_server/http/openai.rs`, `rust/sglang-server/src/api_server/http/openai/chat.rs`, `rust/sglang-server/src/api_server/http/openai/completions.rs`, `rust/sglang-server/src/api_server/http/openai/test_utils.rs`_
- **2026-10-13** [`96f519e4fa`](https://github.com/sgl-project/sglang/commit/96f519e4fa) [#43977](https://github.com/sgl-project/sglang/pull/43977)
  [AMD][DI][CI] glm52 2p1d-ep16: capture CUDA graph on decode (eager decode is too slow) (#43977)
  _Files: `scripts/ci/slurm/recipes/mi355x-fp4/glm52/1k1k/2p1d-ep16-mtp.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/glm52/1k1k/2p1d-ep16.yaml`_
- **2026-10-13** [`d8f8522348`](https://github.com/sgl-project/sglang/commit/d8f8522348) [#43483](https://github.com/sgl-project/sglang/pull/43483)
  [router] power_of_two: in-flight request load for --dp-aware decode (#43483)
  _Files: `sgl-model-gateway/src/policies/power_of_two.rs`_
- **2026-10-13** [`17c3b259f5`](https://github.com/sgl-project/sglang/commit/17c3b259f5) [#42027](https://github.com/sgl-project/sglang/pull/42027)
  [router] Fix power_of_two with --dp-aware (#42027)
  _Files: `sgl-model-gateway/src/config/validation.rs`, `sgl-model-gateway/src/core/worker_manager.rs`, `sgl-model-gateway/src/policies/power_of_two.rs`, `sgl-model-gateway/src/routers/http/pd_router.rs`_
- **2026-10-13** [`75a0d91c1f`](https://github.com/sgl-project/sglang/commit/75a0d91c1f) [#43796](https://github.com/sgl-project/sglang/pull/43796)
  [Fix] Preserve HTTP errors for non-streaming /v1/messages (#43796)
  _Files: `python/sglang/srt/entrypoints/anthropic/serving.py`, `test/registered/unit/entrypoints/anthropic/test_serving.py`_

## Scheduler / Batching  (28 commits)

- **2026-10-19** [`a7fd2e1158`](https://github.com/sgl-project/sglang/commit/a7fd2e1158) [#45050](https://github.com/sgl-project/sglang/pull/45050)
  [Feat] dsv4.1: Return prompt logprobs under encoder SWA bounded replay (#45050)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/encoder_swa_replay.py` _+1 more__
- **2026-10-19** [`fea48754de`](https://github.com/sgl-project/sglang/commit/fea48754de) [#42118](https://github.com/sgl-project/sglang/pull/42118)
  [Feat] rust/grpc: Add ListModels, Detokenize, and Abort to api.v1 (#42118)
  _Files: `proto/sglang/api/v1/generate.proto`, `proto/sglang/api/v1/sampling.proto`, `proto/sglang/api/v1/service.proto`, `python/sglang/api/v1/api_types.py` _+42 more__
- **2026-10-19** [`3c560089e1`](https://github.com/sgl-project/sglang/commit/3c560089e1) [#45047](https://github.com/sgl-project/sglang/pull/45047)
  [Refactor] scheduler: Bill encoder replay rows in `_update_prefill_budget` (#45047)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/model_executor/encoder_swa_replay.py`, `test/registered/unit/dllm/test_gemma4_uniform_lifecycle.py`_
- **2026-10-19** [`1637a4e305`](https://github.com/sgl-project/sglang/commit/1637a4e305) [#45042](https://github.com/sgl-project/sglang/pull/45042)
  [Fix] scheduler: Clear stale `encoder_swa_reset` in `convert_decode_to_extend` (#45042)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_schedule_batch_convert_decode_to_extend.py`_
- **2026-10-18** [`3f13f5d966`](https://github.com/sgl-project/sglang/commit/3f13f5d966) [#45041](https://github.com/sgl-project/sglang/pull/45041)
  [Fix] scheduler: Drop prefill embedding overrides in `prepare_for_decode` (#45041)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-10-17** [`0d13efb2b8`](https://github.com/sgl-project/sglang/commit/0d13efb2b8) [#44767](https://github.com/sgl-project/sglang/pull/44767)
  [Feat] rust-server: Serve /v1/tokenize and /v1/detokenize from the Rust frontend (#44767)
  _Files: `python/sglang/srt/rust_server/config.py`, `rust/sglang-server/src/api_server/core/handle.rs`, `rust/sglang-server/src/api_server/http/openai.rs`, `rust/sglang-server/src/api_server/http/openai/chat.rs` _+14 more__
- **2026-10-17** [`b62a48ee15`](https://github.com/sgl-project/sglang/commit/b62a48ee15) [#44766](https://github.com/sgl-project/sglang/pull/44766)
  [Feat] sglang-server: Serve /flush_cache from the Rust frontend (#44766)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/flush_wrapper.py`, `rust/sglang-server/src/api_server/core/handle.rs`, `rust/sglang-server/src/api_server/http/info.rs` _+2 more__
- **2026-10-16** [`d8dd49d21d`](https://github.com/sgl-project/sglang/commit/d8dd49d21d) [#44785](https://github.com/sgl-project/sglang/pull/44785)
  [Fix] srt: Apply --gc-threshold in every server process and freeze every tokenizer worker (#44785)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py` _+4 more__
- **2026-10-16** [`a46fe83c70`](https://github.com/sgl-project/sglang/commit/a46fe83c70) [#44679](https://github.com/sgl-project/sglang/pull/44679)
  [CI] tests: Fork the gloo exchange test's ranks from a preloaded forkserver (#44679)
  _Files: `test/registered/unit/managers/scheduler_components/test_dp_attn.py`_
- **2026-10-16** [`f110b2f801`](https://github.com/sgl-project/sglang/commit/f110b2f801) [#44531](https://github.com/sgl-project/sglang/pull/44531)
  [Feat] rust-server: Report cached_tokens and reasoning_tokens in meta_info (#44531)
  _Files: `proto/sglang/api/v1/generate.proto`, `python/sglang/api/v1/api_types.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `python/sglang/srt/rust_server/server.py` _+10 more__
- **2026-10-16** [`d393298736`](https://github.com/sgl-project/sglang/commit/d393298736) [#44537](https://github.com/sgl-project/sglang/pull/44537)
  [Fix] tokenizer_manager: re-report only emitted customized_info keys on cumulative streams (#44537)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
- **2026-10-15** [`0b1a73599a`](https://github.com/sgl-project/sglang/commit/0b1a73599a) [#44312](https://github.com/sgl-project/sglang/pull/44312)
  [Feat] rust-server: Apply the x-override-* request headers (#44312)
  _Files: `proto/sglang/api/v1/generate.proto`, `python/sglang/api/v1/api_types.py`, `python/sglang/srt/rust_server/config.py`, `rust/sglang-api-types/src/generated/sglang.api.v1.rs` _+13 more__
- **2026-10-15** [`c5a5bf0d0b`](https://github.com/sgl-project/sglang/commit/c5a5bf0d0b) [#44453](https://github.com/sgl-project/sglang/pull/44453)
  [Fix] pp: Order output send/recv by rank parity to fix cross-node hang (#44453)
  _Files: `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/registered/unit/managers/test_pp_output_exchange_order.py`_
- **2026-10-15** [`a776851c97`](https://github.com/sgl-project/sglang/commit/a776851c97) [#44420](https://github.com/sgl-project/sglang/pull/44420)
  [Refactor] scheduler: Check the prefill budget at the admission loop head; drop a redundant PD gate (#44420)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_held_row_admission.py`_
- **2026-10-15** [`f9bdb74a5a`](https://github.com/sgl-project/sglang/commit/f9bdb74a5a) [#44401](https://github.com/sgl-project/sglang/pull/44401)
  [Fix] scheduler: Count a request's held req_to_token row once at admission (#44401)
  _Files: `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_held_row_admission.py`_
- **2026-10-15** [`a6a8c56015`](https://github.com/sgl-project/sglang/commit/a6a8c56015) [#33715](https://github.com/sgl-project/sglang/pull/33715)
  [Fix] detokenizer router: Route by rid without tokenizer worker ipcs and broadcast logging config (#33715)
  _Files: `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `test/registered/unit/managers/test_multi_tokenizer_mixin.py`_
- **2026-10-15** [`0536cec73d`](https://github.com/sgl-project/sglang/commit/0536cec73d) [#43323](https://github.com/sgl-project/sglang/pull/43323)
  [Feat] metrics: Expose multi-detokenizer router CPU usage (#43323)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `test/registered/unit/managers/test_multi_tokenizer_mixin.py`_
- **2026-10-14** [`0f36c8015c`](https://github.com/sgl-project/sglang/commit/0f36c8015c) [#31892](https://github.com/sgl-project/sglang/pull/31892)
  [Bug] Fix multi-tokenizer BatchEmbeddingOutput repack dropping fields (#31892)
  _Files: `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `test/registered/unit/managers/test_multi_tokenizer_mixin.py`_
- **2026-10-14** [`aa8793f33b`](https://github.com/sgl-project/sglang/commit/aa8793f33b) [#43942](https://github.com/sgl-project/sglang/pull/43942)
  [Rust] Serve scheduler metrics on the Rust frontend's /metrics (#43942)
  _Files: `python/sglang/srt/rust_server/config.py`, `rust/sglang-server/src/api_server/http.rs`, `rust/sglang-server/src/api_server/http/app.rs`, `rust/sglang-server/src/api_server/http/metrics.rs` _+8 more__
- **2026-10-14** [`97d3150a6a`](https://github.com/sgl-project/sglang/commit/97d3150a6a) [#43520](https://github.com/sgl-project/sglang/pull/43520)
  [Perf] Cache msgspec struct fields in the batch splitter (#43520)
  _Files: `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `test/registered/unit/managers/test_multi_tokenizer_mixin.py`_
- **2026-10-14** [`4273814771`](https://github.com/sgl-project/sglang/commit/4273814771) [#44288](https://github.com/sgl-project/sglang/pull/44288)
  [Perf] detokenizer: Group return IPC sends by tokenizer worker (#44288)
  _Files: `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `test/registered/unit/managers/test_multi_tokenizer_mixin.py`_
- **2026-10-13** [`a832609b92`](https://github.com/sgl-project/sglang/commit/a832609b92) [#42890](https://github.com/sgl-project/sglang/pull/42890)
  [Feature] Return output top logprobs as flat base64 arrays on request (#42890)
  _Files: `docs/docs/basic_usage/openai_api_completions.mdx`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/managers/io_struct.py` _+7 more__
- **2026-10-13** [`5bcaf0f8ed`](https://github.com/sgl-project/sglang/commit/5bcaf0f8ed) [#43772](https://github.com/sgl-project/sglang/pull/43772)
  [Core] Add request-level customized_info keys and mark Full prefill capture batches (#43772)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/model_executor/forward_batch_info.py` _+5 more__
- **2026-10-13** [`ff3f8c348c`](https://github.com/sgl-project/sglang/commit/ff3f8c348c) [#43946](https://github.com/sgl-project/sglang/pull/43946)
  [Observability] Report per-request storage prefetch and staging waits in meta_info (#43946)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/observability/req_time_stats.py`, `test/registered/unit/observability/test_req_time_stats.py`_
- **2026-10-12** [`b60444c621`](https://github.com/sgl-project/sglang/commit/b60444c621) [#43854](https://github.com/sgl-project/sglang/pull/43854)
  Fix autograd retention in CUDA graph capture tail hooks (#43854)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-10-12** [`28621739fc`](https://github.com/sgl-project/sglang/commit/28621739fc) [#41911](https://github.com/sgl-project/sglang/pull/41911)
  [Fix] Make tokenizer request-state initialization atomic (#41911)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
- **2026-10-12** [`2240049194`](https://github.com/sgl-project/sglang/commit/2240049194) [#43758](https://github.com/sgl-project/sglang/pull/43758)
  [RL] Return a failed weight update when the cache flush is refused (#43758)
  _Files: `python/sglang/srt/managers/scheduler_components/weight_updater.py`_
- **2026-10-12** [`a297cd3da1`](https://github.com/sgl-project/sglang/commit/a297cd3da1) [#41872](https://github.com/sgl-project/sglang/pull/41872)
  [Fix] scheduler: stop latching batch_is_full when nothing can run (#41872)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_batch_is_full_latch.py`_

## Docs / Examples  (22 commits)

- **2026-10-19** [`7f96dc6874`](https://github.com/sgl-project/sglang/commit/7f96dc6874) [#43345](https://github.com/sgl-project/sglang/pull/43345)
  [Perf] [XPU] server_args: Enable fused QK-norm + RoPE by default (#43345)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/platform_hook.py` _+1 more__
- **2026-10-19** [`0dc6de2e74`](https://github.com/sgl-project/sglang/commit/0dc6de2e74) [#44587](https://github.com/sgl-project/sglang/pull/44587)
  [Doc] nemotron-3.5-super: update H200 and Spark wizard recipes (#44587)
  _Files: `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx`_
- **2026-10-18** [`80914b7c9b`](https://github.com/sgl-project/sglang/commit/80914b7c9b) [#44950](https://github.com/sgl-project/sglang/pull/44950)
  [Refactor] sgl-router: Rename --max-in-flight to --max-inflight-requests (#44950)
  _Files: `experimental/sgl-router/ARCHITECTURE.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs` _+1 more__
- **2026-10-18** [`62d4261cf4`](https://github.com/sgl-project/sglang/commit/62d4261cf4) [#43592](https://github.com/sgl-project/sglang/pull/43592)
  [Doc] sgl-router: Rewrite README and add architecture guide (#43592)
  _Files: `experimental/sgl-router/ARCHITECTURE.md`, `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/REFERENCE.md` _+3 more__
- **2026-10-18** [`a8b939da43`](https://github.com/sgl-project/sglang/commit/a8b939da43) [#44947](https://github.com/sgl-project/sglang/pull/44947)
  Revert "[Doc] cookbook: Add Muse Spark Open SWA ratio calculator" (#44947)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`, `docs/scripts/tests/muse-spark-swa-ratio.test.mjs`, `docs/src/snippets/_muse_spark_swa_ratio.jsx`, `docs/src/snippets/_muse_spark_swa_ratio_calculator.jsx`_
- **2026-10-18** [`df24bca4ba`](https://github.com/sgl-project/sglang/commit/df24bca4ba) [#44693](https://github.com/sgl-project/sglang/pull/44693)
  [Doc] popular-models: Replace Kimi-K3 with Muse Spark Open (#44693)
  _Files: `docs/src/snippets/configs/popular-models.jsx`_
- **2026-10-17** [`3fc08b939a`](https://github.com/sgl-project/sglang/commit/3fc08b939a) [#44849](https://github.com/sgl-project/sglang/pull/44849)
  [Feat] server-args: Add --enable-hicache alias for --enable-hierarchical-cache (#44849)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/utils/server_args_config_parser.py`_
- **2026-10-17** [`9590dc80cc`](https://github.com/sgl-project/sglang/commit/9590dc80cc) [#44790](https://github.com/sgl-project/sglang/pull/44790)
  [Doc] hicache: Explain HiCache host pool sizing with a storage backend (#44790)
  _Files: `docs/docs/advanced_features/hicache_best_practices.mdx`_
- **2026-10-16** [`2c2986be2b`](https://github.com/sgl-project/sglang/commit/2c2986be2b) [#44694](https://github.com/sgl-project/sglang/pull/44694)
  docs: add Beam 1.0 deployment cookbook (#44694)
  _Files: `docs/cards/logos/reflection.png`, `docs/cookbook/autoregressive/Reflection/Beam-1_0.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-10-16** [`9baace8456`](https://github.com/sgl-project/sglang/commit/9baace8456) [#44310](https://github.com/sgl-project/sglang/pull/44310)
  [Doc] cookbook: refresh MiniCPM-V 4.7 DSPARK benchmarks at the final model PR head (#44310)
  _Files: `docs/cookbook/autoregressive/OpenBMB/MiniCPM-V-4_7.mdx`, `docs/src/snippets/configs/openbmb/minicpm-v-4.7-benchmarks.jsx`_
- **2026-10-16** [`9d394dfbd7`](https://github.com/sgl-project/sglang/commit/9d394dfbd7) [#44695](https://github.com/sgl-project/sglang/pull/44695)
  [Doc] [NPU] docs: refresh associated dependency  versions in npu docs (#44695)
  _Files: `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`_
- **2026-10-16** [`dfc89580f1`](https://github.com/sgl-project/sglang/commit/dfc89580f1) [#44687](https://github.com/sgl-project/sglang/pull/44687)
  [Doc] cookbook: Add Muse Spark Open SWA ratio calculator (#44687)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`, `docs/scripts/tests/muse-spark-swa-ratio.test.mjs`, `docs/src/snippets/_muse_spark_swa_ratio.jsx`, `docs/src/snippets/_muse_spark_swa_ratio_calculator.jsx`_
- **2026-10-16** [`c15edf314d`](https://github.com/sgl-project/sglang/commit/c15edf314d) [#44616](https://github.com/sgl-project/sglang/pull/44616)
  [Doc] blogs: Sync LMSYS SGLang blog cards (#44616)
  _Files: `docs/index.mdx`_
- **2026-10-15** [`a8aaf95b58`](https://github.com/sgl-project/sglang/commit/a8aaf95b58) [#44527](https://github.com/sgl-project/sglang/pull/44527)
  [Cookbook] Add cookbook for muse spark open (#44527)
  _Files: `docs/cookbook/autoregressive/Meta/MuseGlimmer.mdx`, `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+3 more__
- **2026-10-15** [`05cbe241be`](https://github.com/sgl-project/sglang/commit/05cbe241be) [#44510](https://github.com/sgl-project/sglang/pull/44510)
  [Doc] cookbook: Add Nemotron 3.5 Super VL (#44510)
  _Files: `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`, `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Super.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-10-15** [`8f853b0041`](https://github.com/sgl-project/sglang/commit/8f853b0041) [#42766](https://github.com/sgl-project/sglang/pull/42766)
  [Doc] cookbook: Add Jais 3 deployment recipes (#42766)
  _Files: `docs/cookbook/autoregressive/IFM/Jais-3.mdx`, `docs/docs.json`, `docs/src/snippets/configs/IFM/jais-3-benchmarks.jsx`, `docs/src/snippets/configs/IFM/jais-3.jsx`_
- **2026-10-14** [`3a9cae27ed`](https://github.com/sgl-project/sglang/commit/3a9cae27ed) [#44177](https://github.com/sgl-project/sglang/pull/44177)
  [Doc] [NPU] docs: Update NPU CANN version to 9.1.0 (#44177)
  _Files: `docs/docs/hardware-platforms/ascend-npus/evaluation/accuracy_evaluation.mdx`, `docs/docs/hardware-platforms/ascend-npus/evaluation/performance_testing.mdx`, `docs/docs/hardware-platforms/ascend-npus/faq.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx` _+4 more__
- **2026-10-13** [`5eda6b7e67`](https://github.com/sgl-project/sglang/commit/5eda6b7e67) [#43829](https://github.com/sgl-project/sglang/pull/43829)
  docs: add MiniCPM-V 4.7 cookbook (#43829)
  _Files: `docs/cookbook/autoregressive/OpenBMB/MiniCPM-V-4_7.mdx`, `docs/cookbook/autoregressive/OpenBMB/MiniCPM5-2B.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-10-13** [`29974d543e`](https://github.com/sgl-project/sglang/commit/29974d543e) [#44052](https://github.com/sgl-project/sglang/pull/44052)
  [NPU] [DOC] update kimi k3 cookbook and supported features on NPU (#44052)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-10-12** [`180933518e`](https://github.com/sgl-project/sglang/commit/180933518e) [#42316](https://github.com/sgl-project/sglang/pull/42316)
  [sgl-router] Serve the Anthropic Messages API on /v1/messages (#42316)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/lib.rs`, `experimental/sgl-router/src/protocol/anthropic/mod.rs`, `experimental/sgl-router/src/protocol/anthropic/request.rs` _+10 more__
- **2026-10-12** [`62c853b654`](https://github.com/sgl-project/sglang/commit/62c853b654) [#43787](https://github.com/sgl-project/sglang/pull/43787)
  docs: clarify prefill CP terminology and simplify wording (#43787)
  _Files: `docs/docs/advanced_features/prefill_cp.mdx`_
- **2026-10-12** [`f9bd83e7a9`](https://github.com/sgl-project/sglang/commit/f9bd83e7a9) [#43462](https://github.com/sgl-project/sglang/pull/43462)
  docs: sync LMSYS SGLang blog cards (#43462)
  _Files: `docs/index.mdx`_

## Other  (19 commits)

- **2026-10-19** [`62cee1b15c`](https://github.com/sgl-project/sglang/commit/62cee1b15c) [#45100](https://github.com/sgl-project/sglang/pull/45100)
  [Fix] sgl-router: Keep the kv-indexer connection through bursts of cancelled prefix queries (#45100)
  _Files: `experimental/sgl-router/sgl-kv-indexer/src/client.rs`, `experimental/sgl-router/sgl-kv-indexer/src/service.rs`_
- **2026-10-19** [`0025f93944`](https://github.com/sgl-project/sglang/commit/0025f93944) [#45120](https://github.com/sgl-project/sglang/pull/45120)
  [Fix] sgl-router: Refuse prefill workers that cannot compute before bootstrap under --decode-dispatch-limit (#45120)
  _Files: `experimental/sgl-router/REFERENCE.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/workers/introspect.rs`, `experimental/sgl-router/src/workers/manager.rs`_
- **2026-10-18** [`fe1851c3c2`](https://github.com/sgl-project/sglang/commit/fe1851c3c2) [#44305](https://github.com/sgl-project/sglang/pull/44305)
  [Fix] sgl-router: Receive kv-indexer-bridge event batches outside tokio's coop budget (#44305)
  _Files: `experimental/sgl-router/sgl-kv-indexer/src/bridge.rs`_
- **2026-10-18** [`520df8a491`](https://github.com/sgl-project/sglang/commit/520df8a491) [#39264](https://github.com/sgl-project/sglang/pull/39264)
  [Perf] weight-sync: Allocate packed receive buffers from metadata (#39264)
  _Files: `python/sglang/srt/model_executor/model_runner_components/weight_updater.py`, `python/sglang/srt/weight_sync/tensor_bucket.py`, `test/registered/rl/test_tensor_bucket.py`_
- **2026-10-16** [`d230f2c35b`](https://github.com/sgl-project/sglang/commit/d230f2c35b) [#44775](https://github.com/sgl-project/sglang/pull/44775)
  [Feat] profiler: Add the forward pass id to detailed step span labels (#44775)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/utils/profile_utils.py`, `test/registered/unit/managers/test_detailed_annotations.py`_
- **2026-10-16** [`71b60fa46c`](https://github.com/sgl-project/sglang/commit/71b60fa46c) [#44787](https://github.com/sgl-project/sglang/pull/44787)
  [Fix] engram: Avoid blocking history copies during PD admission (#44787)
  _Files: `python/sglang/srt/model_executor/model_runner_components/ngram_embedding_manager.py`_
- **2026-10-16** [`553068af25`](https://github.com/sgl-project/sglang/commit/553068af25) [#44533](https://github.com/sgl-project/sglang/pull/44533)
  [Fix] rust-server: Honour cache_salt and require_reasoning on /generate (#44533)
  _Files: `proto/sglang/api/v1/generate.proto`, `python/sglang/api/v1/api_types.py`, `rust/sglang-api-types/src/generated/sglang.api.v1.rs`, `rust/sglang-api-types/src/generated/sglang.api.v1.serde.rs` _+3 more__
- **2026-10-16** [`e3961eb6fa`](https://github.com/sgl-project/sglang/commit/e3961eb6fa) [#44440](https://github.com/sgl-project/sglang/pull/44440)
  [Fix] utils: Allowlist torch.bcomplex32 in SafeUnpickler (#44440)
  _Files: `python/sglang/srt/utils/common.py`, `test/registered/unit/utils/test_safe_unpickler.py`_
- **2026-10-15** [`c7fb57d990`](https://github.com/sgl-project/sglang/commit/c7fb57d990) [#44509](https://github.com/sgl-project/sglang/pull/44509)
  [Fix] sgl-router: Bump rustls to 0.23.46 for RUSTSEC-2026-0346..0349 (#44509)
  _Files: `experimental/sgl-router/Cargo.lock`_
- **2026-10-15** [`c4870d98cf`](https://github.com/sgl-project/sglang/commit/c4870d98cf) [#44093](https://github.com/sgl-project/sglang/pull/44093)
  [Fix] glm5_next: Correct num_experts_per_tok default to 8 (#44093)
  _Files: `python/sglang/srt/configs/glm5_next.py`_
- **2026-10-14** [`209f8220d6`](https://github.com/sgl-project/sglang/commit/209f8220d6) [#44207](https://github.com/sgl-project/sglang/pull/44207)
  [Fix] sglang-server: Honour extra_key on the Rust frontend's /generate (#44207)
  _Files: `proto/sglang/api/v1/generate.proto`, `python/sglang/api/v1/api_types.py`, `rust/sglang-api-types/src/generated/sglang.api.v1.rs`, `rust/sglang-api-types/src/generated/sglang.api.v1.serde.rs` _+3 more__
- **2026-10-14** [`7b53a13401`](https://github.com/sgl-project/sglang/commit/7b53a13401) [#44256](https://github.com/sgl-project/sglang/pull/44256)
  [Fix] glm5.2: Align PD HiSparse prefill KV layout (#44256)
  _Files: `test/registered/e2e/models/test_dsa_glm52_hisparse.py`_
- **2026-10-14** [`58f2c923ed`](https://github.com/sgl-project/sglang/commit/58f2c923ed) [#44218](https://github.com/sgl-project/sglang/pull/44218)
  [Feat] sgl-router: skip engines at an admission cap in power-of-two; forward x-sglext headers (#44218)
  _Files: `experimental/sgl-router/src/policies_reorg/admission.rs`, `experimental/sgl-router/src/policies_reorg/cache_aware.rs`, `experimental/sgl-router/src/policies_reorg/power_of_two.rs`, `experimental/sgl-router/src/policies_reorg/session_aware.rs` _+5 more__
- **2026-10-14** [`4f751da975`](https://github.com/sgl-project/sglang/commit/4f751da975) [#44040](https://github.com/sgl-project/sglang/pull/44040)
  [Agents] Add a rule to prefer sgl-eval for accuracy evals (#44040)
  _Files: `.agents/skills/generate-profile/SKILL.md`, `.agents/skills/write-sglang-test/SKILL.md`, `.claude/rules/prefer-sgl-eval.md`, `python/sglang/test/few_shot_gsm8k.py`_
- **2026-10-14** [`44b44774c3`](https://github.com/sgl-project/sglang/commit/44b44774c3) [#43067](https://github.com/sgl-project/sglang/pull/43067)
  [Bugfix] Keep rope_theta when --json-model-override-args overrides rope_scaling (#43067)
  _Files: `python/sglang/srt/utils/hf_transformers/config.py`, `test/registered/unit/utils/test_hf_transformers_loading.py`_
- **2026-10-12** [`296774da37`](https://github.com/sgl-project/sglang/commit/296774da37) [#43104](https://github.com/sgl-project/sglang/pull/43104)
  [Tokenizer] Require fastokens>=0.3.2 and include it in the all extra (#43104)
  _Files: `python/pyproject.toml`_
- **2026-10-12** [`cd8ed1bb55`](https://github.com/sgl-project/sglang/commit/cd8ed1bb55) [#43398](https://github.com/sgl-project/sglang/pull/43398)
  [Bugfix] Preserve available host memory for integrated MUSA devices (#43398)
  _Files: `python/sglang/srt/utils/common.py`, `test/registered/unit/platforms/test_platform_interface.py`_
- **2026-10-12** [`95ce9caaf2`](https://github.com/sgl-project/sglang/commit/95ce9caaf2) [#43724](https://github.com/sgl-project/sglang/pull/43724)
  [Rust] Lock hyper 1.12.0 and want 0.3.2 in the rust workspace (#43724)
  _Files: `rust/Cargo.lock`_
- **2026-10-12** [`3c74f68a9c`](https://github.com/sgl-project/sglang/commit/3c74f68a9c) [#43702](https://github.com/sgl-project/sglang/pull/43702)
  [Fix] Initialize BF16 GEMM dispatch in the one-batch benchmark (#43702)
  _Files: `python/sglang/benchmark/one_batch.py`_

## Quantization  (17 commits)

- **2026-10-19** [`806e7423af`](https://github.com/sgl-project/sglang/commit/806e7423af) [#44618](https://github.com/sgl-project/sglang/pull/44618)
  [Perf] deepseek_v4: size the masked silu-mul-quant grid to the GPU, not the padded capacity (#44618)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `test/registered/kernels/ops/quantization/test_per_token_group_quant.py`_
- **2026-10-19** [`417606527d`](https://github.com/sgl-project/sglang/commit/417606527d) [#44500](https://github.com/sgl-project/sglang/pull/44500)
  [Fix] nvfp4: Own streamed tensors while waiting for paired weights (#44500)
  _Files: `python/sglang/srt/layers/quantization/nvfp4_online.py`, `python/sglang/srt/model_loader/weight_utils.py`, `test/registered/unit/layers/quantization/test_nvfp4_online_weight_loader.py`_
- **2026-10-18** [`e17fed6ea7`](https://github.com/sgl-project/sglang/commit/e17fed6ea7) [#44196](https://github.com/sgl-project/sglang/pull/44196)
  [Perf] diffusion: fused gate/up + SwiGLU MLP on comfy_kitchen INT8 for Qwen-Image 2.1 (#44196)
  _Files: `python/sglang/multimodal_gen/runtime/layers/quantization/convrot_int8_comfy_kitchen.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image21.py`, `python/sglang/multimodal_gen/test/unit/test_convrot_int8_backends.py`_
- **2026-10-18** [`680a2ff27e`](https://github.com/sgl-project/sglang/commit/680a2ff27e) [#44761](https://github.com/sgl-project/sglang/pull/44761)
  [Perf] [NVIDIA] diffusion/FLUX.3: Run dynamic LoRA through PrimsTS GEMMs (#44761)
  _Files: `python/sglang/kernels/ops/diffusion/gemm/flux3_fp8_prims_ts.py`, `python/sglang/kernels/ops/diffusion/gemm/flux3_nvfp4_prims_ts.py`, `python/sglang/kernels/ops/diffusion/gemm/flux3_prims_ts_config.py`, `python/sglang/multimodal_gen/runtime/layers/flux3_fused_ops.py` _+6 more__
- **2026-10-17** [`b15a78a881`](https://github.com/sgl-project/sglang/commit/b15a78a881) [#40171](https://github.com/sgl-project/sglang/pull/40171)
  [Fix] diffusion/lora: revalidate FLUX.2 FP8/NVFP4 fast paths after LoRA attach (#40171)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py`_
- **2026-10-16** [`baf451fcd6`](https://github.com/sgl-project/sglang/commit/baf451fcd6) [#44008](https://github.com/sgl-project/sglang/pull/44008)
  [Perf] [AMD] dsv4: carry aiter DSv4 GEMM tuned rows and mHC tile_m=16 until aiter ships them (7/8) (#44008)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/a8w8_blockscale_bpreshuffle_tuned_gemm.csv`, `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=2048-K=7168.json`, `python/sglang/srt/models/deepseek_common/amd/aiter_intree_configs/triton/gfx950/gemm_a8w8_blockscale_preshuffled/GEMM-A8W8_BLOCKSCALE_PRESHUFFLED-N=7168-K=2048.json` _+4 more__
- **2026-10-16** [`42eb556e66`](https://github.com/sgl-project/sglang/commit/42eb556e66) [#44007](https://github.com/sgl-project/sglang/pull/44007)
  [Perf] [AMD] dsv4: optional e8m0 mxscale GEMM for dense 128x128 fp8 linears (6/8) (#44007)
  _Files: `python/sglang/kernels/ops/layernorm/rmsnorm_fp8_e8m0.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` _+3 more__
- **2026-10-16** [`f0ff18353d`](https://github.com/sgl-project/sglang/commit/f0ff18353d) [#44003](https://github.com/sgl-project/sglang/pull/44003)
  [Perf] [AMD] dsv4: fp8 verify writes the SWA ring in the fused norm/rope kernel (2/8) (#44003)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-16** [`5117bfbaeb`](https://github.com/sgl-project/sglang/commit/5117bfbaeb) [#44213](https://github.com/sgl-project/sglang/pull/44213)
  [Fix] compressed-tensors: Serve NVFP4 W4A4 linears via FP4 Marlin when --fp4-gemm-backend marlin is set on SM100 (#44213)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `test/registered/unit/layers/quantization/test_compressed_tensors_fp4_schemes.py`_
- **2026-10-15** [`2092160d42`](https://github.com/sgl-project/sglang/commit/2092160d42) [#41988](https://github.com/sgl-project/sglang/pull/41988)
  [AMD][Diffusion] Route unquantized linears through aiter tgemm on gfx1250 (#41988)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/linear.py`_
- **2026-10-14** [`536d065370`](https://github.com/sgl-project/sglang/commit/536d065370) [#44022](https://github.com/sgl-project/sglang/pull/44022)
  [CP] Automatically enable BCG for supported prefill CP configurations (#44022)
  _Files: `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/arg_groups/resolution_hooks.py`, `python/sglang/srt/layers/cp/base.py` _+3 more__
- **2026-10-13** [`e9400c5a8f`](https://github.com/sgl-project/sglang/commit/e9400c5a8f) [#43985](https://github.com/sgl-project/sglang/pull/43985)
  [AMD][DI][CI] kimik26 2p1d-ep16: capture CUDA graph on decode (eager decode is slow) (#43985)
  _Files: `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/2p1d-ep16-mtp-mxfp4.yaml`, `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/2p1d-ep16-mxfp4.yaml`_
- **2026-10-13** [`8e37c6cf37`](https://github.com/sgl-project/sglang/commit/8e37c6cf37) [#44055](https://github.com/sgl-project/sglang/pull/44055)
  [CI] Run test_pi05_modelopt_fp8_cuda in the kernel-unit lane (#44055)
  _Files: `test/registered/kernels/ops/gemm/test_pi05_modelopt_fp8_cuda.py`_
- **2026-10-13** [`fc404bbbb3`](https://github.com/sgl-project/sglang/commit/fc404bbbb3) [#43944](https://github.com/sgl-project/sglang/pull/43944)
  [AMD][DI][CI] dsv4pro-fp8 2p1d-ep16-mtp: raise prefill mem fraction for MORI EP v2 memory (#43944)
  _Files: `scripts/ci/slurm/recipes/mi355x-fp8/dsv4pro/1k1k/2p1d-ep16-mtp.yaml`_
- **2026-10-12** [`7224fce1b5`](https://github.com/sgl-project/sglang/commit/7224fce1b5) [#41980](https://github.com/sgl-project/sglang/pull/41980)
  [AMD] Recalibrate test_quark_mxfp4 GSM8K thresholds to observed MI355X noise (#41980)
  _Files: `test/registered/e2e/quantization/test_quark_mxfp4.py`_
- **2026-10-12** [`d6853f5066`](https://github.com/sgl-project/sglang/commit/d6853f5066) [#43803](https://github.com/sgl-project/sglang/pull/43803)
  [AMD] Add flydsl mxfp8 dense gemm kernel for dpsk v4.1 prefill (#43803)
  _Files: `python/sglang/kernels/ops/quantization/mxfp8_aiter_gfx95.py`, `python/sglang/kernels/ops/quantization/mxfp8_amd_gfx95.py`, `python/sglang/kernels/ops/quantization/mxfp8_flydsl_gfx95.py`, `python/sglang/srt/environ.py` _+1 more__
- **2026-10-12** [`d434ea444d`](https://github.com/sgl-project/sglang/commit/d434ea444d) [#42159](https://github.com/sgl-project/sglang/pull/42159)
  [DSV4.1] Reduce eager Engram extend preparation (#42159)
  _Files: `python/sglang/kernels/ops/embeddings/engram_hash.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/engram.py`, `test/manual/quantization/test_engram_extend_hash.py`_

## CI / Build  (16 commits)

- **2026-10-19** [`8c4680cb65`](https://github.com/sgl-project/sglang/commit/8c4680cb65) [#45153](https://github.com/sgl-project/sglang/pull/45153)
  [CI] npu: Move llada2-mini FDFO test to full test (#45153)
  _Files: `test/registered/npu/basic_function/dllm/test_npu_llada2_mini_fdfo.py`_
- **2026-10-19** [`b6d3b7e163`](https://github.com/sgl-project/sglang/commit/b6d3b7e163) [#45013](https://github.com/sgl-project/sglang/pull/45013)
  [CI] [Intel] xpu: Disable L0 copy offload to fix first-H2D-copy hang (#45013)
  _Files: `scripts/ci/xpu/xpu_ci_start_container.sh`_
- **2026-10-19** [`f02458fff1`](https://github.com/sgl-project/sglang/commit/f02458fff1) [#40066](https://github.com/sgl-project/sglang/pull/40066)
  [Fix] [CPU] memory: Honor cgroup memory.max when sizing CPU memory (#40066)
  _Files: `.github/workflows/pr-test-xeon.yml`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/utils/common.py`_
- **2026-10-19** [`299da60131`](https://github.com/sgl-project/sglang/commit/299da60131) [#45053](https://github.com/sgl-project/sglang/pull/45053)
  [CI] test-utils: Abort the test run when its server dies inside a `CustomTestCase` method (#45053)
  _Files: `python/sglang/test/test_utils.py`_
- **2026-10-17** [`eb5739b30e`](https://github.com/sgl-project/sglang/commit/eb5739b30e) [#44881](https://github.com/sgl-project/sglang/pull/44881)
  [CI] pr-test-npu: Temporarily disable recommend-tests-from-coverage job (#44881)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-10-16** [`a31a8c2bbd`](https://github.com/sgl-project/sglang/commit/a31a8c2bbd) [#44729](https://github.com/sgl-project/sglang/pull/44729)
  [CI] tests: Let test_hicache_storage size its host cache to the runner (#44729)
  _Files: `test/registered/hicache/test_hicache_storage.py`_
- **2026-10-16** [`81c9d804b0`](https://github.com/sgl-project/sglang/commit/81c9d804b0) [#44708](https://github.com/sgl-project/sglang/pull/44708)
  [CI] pr-check-comment: Comment on PRs when lint or title check fails (#44708)
  _Files: `.github/scripts/pr-check-comment.cjs`, `.github/workflows/pr-check-comment.yml`_
- **2026-10-16** [`06b81b120e`](https://github.com/sgl-project/sglang/commit/06b81b120e) [#44706](https://github.com/sgl-project/sglang/pull/44706)
  [CI] deepgemm: Increase B200 release test timeout to 180 minutes (#44706)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-10-16** [`5dd37af412`](https://github.com/sgl-project/sglang/commit/5dd37af412) [#44647](https://github.com/sgl-project/sglang/pull/44647)
  [Doc] [XPU] Cookbook: Update the XPU Docker version to 0.5.22 (#44647)
  _Files: `docs/docs/hardware-platforms/xpu.mdx`_
- **2026-10-15** [`877be2974a`](https://github.com/sgl-project/sglang/commit/877be2974a) [#44410](https://github.com/sgl-project/sglang/pull/44410)
  [CI] pr-test: Let stage wait jobs reach their max-wait budget (#44410)
  _Files: `.agents/skills/ci-workflow-guide/SKILL.md`, `.github/actions/wait-for-jobs/action.yml`, `.github/workflows/pr-test.yml`_
- **2026-10-15** [`01ac2cf36d`](https://github.com/sgl-project/sglang/commit/01ac2cf36d) [#44108](https://github.com/sgl-project/sglang/pull/44108)
  [CI] [XPU] nightly: Split Intel Main and Wheel workflows (#44108)
  _Files: `.github/workflows/nightly-test-intel-wheel.yml`, `.github/workflows/nightly-test-intel.yml`, `.github/workflows/release-branch-cut.yml`, `.github/workflows/xpu-ci-job-monitor.yml`_
- **2026-10-15** [`e573d91275`](https://github.com/sgl-project/sglang/commit/e573d91275) [#44380](https://github.com/sgl-project/sglang/pull/44380)
  [CI] tests: Fix stale fakes in the CP strategy and request-class override unit tests (#44380)
  _Files: `test/registered/cp/test_cp_strategy_unit.py`, `test/registered/unit/managers/test_request_class_override_points.py`_
- **2026-10-14** [`b67785153a`](https://github.com/sgl-project/sglang/commit/b67785153a) [#44303](https://github.com/sgl-project/sglang/pull/44303)
  [Fix] glm5.2: Align HiSparse warmup backends and move test to nightly (#44303)
  _Files: `test/registered/e2e/models/test_dsa_glm52_hisparse.py`_
- **2026-10-14** [`491d4ef178`](https://github.com/sgl-project/sglang/commit/491d4ef178) [#41005](https://github.com/sgl-project/sglang/pull/41005)
  [MLU][CI] Bootstrap MLU runner workflows (#41005)
  _Files: `.github/workflows/mlu-ci-reliability-report.yml`, `.github/workflows/nightly-test-mlu.yml`, `.github/workflows/pr-states.yml`, `.github/workflows/pr-test-mlu.yml` _+3 more__
- **2026-10-12** [`8afe107c24`](https://github.com/sgl-project/sglang/commit/8afe107c24) [#42003](https://github.com/sgl-project/sglang/pull/42003)
  [XPU] Upgrade XPU backend to PyTorch 2.14 (#42003)
  _Files: `docker/xpu.Dockerfile`, `docs/docs/hardware-platforms/xpu.mdx`, `python/pyproject_xpu.toml`_
- **2026-10-12** [`8ce76b88df`](https://github.com/sgl-project/sglang/commit/8ce76b88df) [#42048](https://github.com/sgl-project/sglang/pull/42048)
  [XPU CI] Optimize PR CI per-file timeouts and fail hanging tests fast (#42048)
  _Files: `.github/workflows/pr-test-xpu.yml`, `python/sglang/test/ci/ci_utils.py`, `test/run_suite.py`_

## ROCm / AMD  (16 commits)

- **2026-10-19** [`a90e9c5dd8`](https://github.com/sgl-project/sglang/commit/a90e9c5dd8) [#44443](https://github.com/sgl-project/sglang/pull/44443)
  [Fix] [AMD] mhc: Bound the Triton fused post+pre buffer cache (#44443)
  _Files: `python/sglang/srt/models/deepseek_common/amd/deepseek_v4_fused_mhc.py`, `test/registered/unit/models/test_deepseek_v4_amd_fused_mhc.py`_
- **2026-10-19** [`5d9c956f8e`](https://github.com/sgl-project/sglang/commit/5d9c956f8e) [#45070](https://github.com/sgl-project/sglang/pull/45070)
  [Doc] [AMD] dsv4: Update amd cookbook 1016 (#45070)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-10-19** [`3d588779e1`](https://github.com/sgl-project/sglang/commit/3d588779e1) [#40674](https://github.com/sgl-project/sglang/pull/40674)
  [CI] [AMD] test: Run UMBP HiCache E2E through standalone DRAM server (#40674)
  _Files: `test/registered/hicache/test_hicache_storage_umbp_backend.py`_
- **2026-10-18** [`e5dc10e73b`](https://github.com/sgl-project/sglang/commit/e5dc10e73b) [#44903](https://github.com/sgl-project/sglang/pull/44903)
  [Doc] [AMD] dsv41: Update amd cookbook 1016 (#44903)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-10-16** [`ed2ebad342`](https://github.com/sgl-project/sglang/commit/ed2ebad342) [#44454](https://github.com/sgl-project/sglang/pull/44454)
  [Doc] [AMD] cookbook: Refresh DeepSeek V4 AgentX PD recipe optimizations (#44454)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-10-16** [`9246acd462`](https://github.com/sgl-project/sglang/commit/9246acd462) [#44620](https://github.com/sgl-project/sglang/pull/44620)
  [CI] [AMD] aiter: pin aiter commit to 2bb549 for rocm10.1 gfx1250 (#44620)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-15** [`4cca7fcd3e`](https://github.com/sgl-project/sglang/commit/4cca7fcd3e) [#44590](https://github.com/sgl-project/sglang/pull/44590)
  chore: bump sgl-kernel version to 0.4.10 (#44590)
  _Files: `python/sglang/kernels/aot/pyproject.toml`, `python/sglang/kernels/aot/pyproject_cpu.toml`, `python/sglang/kernels/aot/pyproject_musa.toml`, `python/sglang/kernels/aot/pyproject_rocm.toml` _+1 more__
- **2026-10-15** [`bba535ebb4`](https://github.com/sgl-project/sglang/commit/bba535ebb4) [#44534](https://github.com/sgl-project/sglang/pull/44534)
  [Fix] [AMD] docker: Repair the AITER build step after the 2bb549102 pin bump (#44534)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-15** [`e87e32b311`](https://github.com/sgl-project/sglang/commit/e87e32b311) [#42699](https://github.com/sgl-project/sglang/pull/42699)
  [Feat] [AMD] docker: Release ROCm 10.1 for gfx1250 in parallel with ROCm 10.0 (#42699)
  _Files: `.github/workflows/release-docker-amd-rocm10.yml`, `docker/rocm.Dockerfile`, `python/pyproject_other.toml`_
- **2026-10-15** [`71a17dbc24`](https://github.com/sgl-project/sglang/commit/71a17dbc24) [#42148](https://github.com/sgl-project/sglang/pull/42148)
  [AMD][CI] setup: Skip redundant pip-cache chown walk and MORI rebuild (#42148)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-10-15** [`28703575f9`](https://github.com/sgl-project/sglang/commit/28703575f9) [#44379](https://github.com/sgl-project/sglang/pull/44379)
  [AMD] Update ROCm AITER pin to 2bb549102 (#44379)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-15** [`4851d182a1`](https://github.com/sgl-project/sglang/commit/4851d182a1) [#44368](https://github.com/sgl-project/sglang/pull/44368)
  [Doc][AMD] Update v41 amd cookbook 1015 (#44368)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-10-14** [`e29eee18df`](https://github.com/sgl-project/sglang/commit/e29eee18df) [#43945](https://github.com/sgl-project/sglang/pull/43945)
  [AMD][DI][CI] nightly mi355x disagg: stage packed logs under RUNNER_TEMP, not /tmp (#43945)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-10-13** [`aa15b06abe`](https://github.com/sgl-project/sglang/commit/aa15b06abe) [#43928](https://github.com/sgl-project/sglang/pull/43928)
  [AMD][CI] Run test_tracing.py in the extra tier, matching CUDA (#43928)
  _Files: `test/registered/observability/test_tracing.py`_
- **2026-10-13** [`c2dfd5d3d6`](https://github.com/sgl-project/sglang/commit/c2dfd5d3d6) [#43962](https://github.com/sgl-project/sglang/pull/43962)
  [AMD] Update v4 amd cookbook 1012 (#43962)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-10-12** [`6781da8e5b`](https://github.com/sgl-project/sglang/commit/6781da8e5b) [#43834](https://github.com/sgl-project/sglang/pull/43834)
  [AMD] [Docker] Update MoRI to v1.2.4 (#43834)
  _Files: `docker/rocm.Dockerfile`_

## Models  (11 commits)

- **2026-10-19** [`9a93a17c08`](https://github.com/sgl-project/sglang/commit/9a93a17c08) [#44624](https://github.com/sgl-project/sglang/pull/44624)
  [Feat] [CPU] model: Support Muse models on CPU (#44624)
  _Files: `python/sglang/srt/configs/muse_glimmer.py`, `python/sglang/srt/configs/update_config.py`, `python/sglang/srt/models/muse_glimmer.py`_
- **2026-10-17** [`4cbea9d3c7`](https://github.com/sgl-project/sglang/commit/4cbea9d3c7) [#44848](https://github.com/sgl-project/sglang/pull/44848)
  [Doc] cookbook: Allow PD with DSpark for DeepSeek-V4.1 (#44848)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-10-16** [`56a3c4fa16`](https://github.com/sgl-project/sglang/commit/56a3c4fa16) [#44707](https://github.com/sgl-project/sglang/pull/44707)
  [Doc] cookbook: Add RTX Spark Qwen3.6 NVFP4 recipe (#44707)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`_
- **2026-10-14** [`53a24c448e`](https://github.com/sgl-project/sglang/commit/53a24c448e) [#43608](https://github.com/sgl-project/sglang/pull/43608)
  [Feat] sgl-router: Render Kimi-K3 through sglang-processor (#43608)
  _Files: `.agents/skills/processor-model-parity/SKILL.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/tokenizer/chat_formatter.rs`, `experimental/sgl-router/src/tokenizer/kimi.rs` _+35 more__
- **2026-10-13** [`4d5692b6cd`](https://github.com/sgl-project/sglang/commit/4d5692b6cd) [#43006](https://github.com/sgl-project/sglang/pull/43006)
  fix(openai): honor tool_choice=none in DeepSeek encoders (#43006)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-10-13** [`7bd41aec12`](https://github.com/sgl-project/sglang/commit/7bd41aec12) [#43973](https://github.com/sgl-project/sglang/pull/43973)
  [CI] Remove Mistral Small 4 e2e test (#43973)
  _Files: `test/registered/e2e/models/test_ministral4_models.py`_
- **2026-10-13** [`07566cbf0d`](https://github.com/sgl-project/sglang/commit/07566cbf0d) [#43948](https://github.com/sgl-project/sglang/pull/43948)
  [DSv4.1] Temporarily disable B300 PD/CP accuracy test (#43948)
  _Files: `test/registered/e2e/models/test_deepseek_v41_pd_cp_dspark.py`_
- **2026-10-13** [`107cff72d3`](https://github.com/sgl-project/sglang/commit/107cff72d3) [#43833](https://github.com/sgl-project/sglang/pull/43833)
  [DeepSeek-V4.1] mHC: drop seam_open, narrow precomputed stats in take_rows (#43833)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_mhc.py`_
- **2026-10-12** [`6a7abcfc9b`](https://github.com/sgl-project/sglang/commit/6a7abcfc9b) [#43734](https://github.com/sgl-project/sglang/pull/43734)
  [DeepSeek-V4.1] Admit the NIXL transfer backend for DSpark PD (#43734)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`_
- **2026-10-12** [`c6e822c29b`](https://github.com/sgl-project/sglang/commit/c6e822c29b) [#43309](https://github.com/sgl-project/sglang/pull/43309)
  [Fix] Adapt NPU Qwen-VL processor patch to transformers 5.19 resize() signature change (#43309)
  _Files: `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`_
- **2026-10-12** [`1a7af3290d`](https://github.com/sgl-project/sglang/commit/1a7af3290d) [#43446](https://github.com/sgl-project/sglang/pull/43446)
  Fix Mistral-native format detection when the Hub is unreachable (#43446)
  _Files: `python/sglang/srt/arg_groups/model_path_hook.py`_

## Triton / Kernels  (10 commits)

- **2026-10-19** [`a5117beb11`](https://github.com/sgl-project/sglang/commit/a5117beb11) [#44906](https://github.com/sgl-project/sglang/pull/44906)
  [Perf] mhc: Parallelize small-batch post across hidden tiles (#44906)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`_
- **2026-10-18** [`0f4aedfecc`](https://github.com/sgl-project/sglang/commit/0f4aedfecc) [#45035](https://github.com/sgl-project/sglang/pull/45035)
  [Perf] deepseek-v4.1: Default decoder SWA bounded replay on for both PD roles on CUDA (#45035)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`_
- **2026-10-18** [`01f3cba70e`](https://github.com/sgl-project/sglang/commit/01f3cba70e) [#40941](https://github.com/sgl-project/sglang/pull/40941)
  [Fix] dLLM: Size decode graphs to the default max running requests (#40941)
  _Files: `python/sglang/srt/model_executor/runner/base_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `test/registered/unit/model_executor/model_runner_components/test_cuda_graph_setup.py`_
- **2026-10-17** [`400c1dfe6e`](https://github.com/sgl-project/sglang/commit/400c1dfe6e) [#44251](https://github.com/sgl-project/sglang/pull/44251)
  [Perf] distributed: skip the DLPack re-wrap of custom all-reduce results (#44251)
  _Files: `python/sglang/kernels/ops/communication/all_reduce.py`_
- **2026-10-17** [`9c7b338a19`](https://github.com/sgl-project/sglang/commit/9c7b338a19) [#44645](https://github.com/sgl-project/sglang/pull/44645)
  [CI] jit-kernel: Honor continue_on_error on scheduled runs (#44645)
  _Files: `.github/workflows/pr-test-jit-kernel.yml`, `.github/workflows/pr-test.yml`_
- **2026-10-16** [`51faf52305`](https://github.com/sgl-project/sglang/commit/51faf52305) [#44630](https://github.com/sgl-project/sglang/pull/44630)
  [Fix] monokernels: Honor resolved CUDA graph configuration (#44630)
  _Files: `python/sglang/srt/monokernels/guards.py`, `python/sglang/srt/monokernels/runtime.py`_
- **2026-10-14** [`c053fc71d3`](https://github.com/sgl-project/sglang/commit/c053fc71d3) [#44165](https://github.com/sgl-project/sglang/pull/44165)
  [CI] pr-title: Validate pull request title format (#44165)
  _Files: `.agents/skills/cookbook-add-model/SKILL.md`, `.github/pull_request_template.md`, `.github/scripts/pr-title.test.cjs`, `.github/workflows/bot-cherry-pick.yml` _+6 more__
- **2026-10-13** [`08550acc28`](https://github.com/sgl-project/sglang/commit/08550acc28) [#44137](https://github.com/sgl-project/sglang/pull/44137)
  Mark FP32 redux asm volatile (#44137)
  _Files: `python/sglang/kernels/jit/include/sgl_kernel/warp.cuh`_
- **2026-10-13** [`7ff3a11284`](https://github.com/sgl-project/sglang/commit/7ff3a11284) [#43236](https://github.com/sgl-project/sglang/pull/43236)
  [Perf] Enable fast-math for JIT activations on Blackwell (#43236)
  _Files: `python/sglang/kernels/jit/utils/arch.py`_
- **2026-10-12** [`a0e6effe50`](https://github.com/sgl-project/sglang/commit/a0e6effe50) [#43764](https://github.com/sgl-project/sglang/pull/43764)
  [Fix] Link cuda_ipc JIT against CUDA driver stubs dir (#43764)
  _Files: `python/sglang/kernels/ops/communication/all_reduce.py`_

## Serving / API  (10 commits)

- **2026-10-18** [`a3abea3560`](https://github.com/sgl-project/sglang/commit/a3abea3560) [#44075](https://github.com/sgl-project/sglang/pull/44075)
  [Fix] sgl-router: Resend on a closed pooled connection; add --disable-circuit-breaker (#44075)
  _Files: `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/README.md`, `experimental/sgl-router/REFERENCE.md`, `experimental/sgl-router/src/config/cli.rs` _+13 more__
- **2026-10-18** [`1ff2c1d71e`](https://github.com/sgl-project/sglang/commit/1ff2c1d71e) [#44951](https://github.com/sgl-project/sglang/pull/44951)
  [Fix] sgl-router: Fill the media fields when converting TextGenerate to Generate (#44951)
  _Files: `experimental/sgl-router/src/proxy/grpc.rs`_
- **2026-10-16** [`3d61bdd2c9`](https://github.com/sgl-project/sglang/commit/3d61bdd2c9) [#42681](https://github.com/sgl-project/sglang/pull/42681)
  [Feat] sgl-router: Serve the remaining native gRPC inference RPCs (#42681)
  _Files: `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/proxy/grpc.rs`, `experimental/sgl-router/src/proxy/sse.rs` _+6 more__
- **2026-10-13** [`5569b14d26`](https://github.com/sgl-project/sglang/commit/5569b14d26) [#34511](https://github.com/sgl-project/sglang/pull/34511)
  fix(benchmark): request token IDs when counting OpenAI prompts (#34511)
  _Files: `python/sglang/benchmark/datasets/openai_dataset.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`_
- **2026-10-13** [`79af3df346`](https://github.com/sgl-project/sglang/commit/79af3df346) [#42673](https://github.com/sgl-project/sglang/pull/42673)
  [gRPC] Move runtime.v1 bindings to tonic 0.14, report OpenAI status codes, return text on request (#42673)
  _Files: `proto/sglang/runtime/v1/sglang.proto`, `python/sglang/srt/entrypoints/grpc_bridge.py`, `rust/sglang-api-types/src/generated/sglang.runtime.v1.rs`, `rust/sglang-grpc/src/bridge.rs` _+2 more__
- **2026-10-13** [`e98c6d7b25`](https://github.com/sgl-project/sglang/commit/e98c6d7b25) [#43950](https://github.com/sgl-project/sglang/pull/43950)
  Rainj me/rust bench (#43950)
  _Files: `python/sglang/benchmark/rust_client.py`, `python/sglang/benchmark/serving.py`, `rust/Cargo.lock`, `rust/Cargo.toml` _+10 more__
- **2026-10-13** [`11cd2701a8`](https://github.com/sgl-project/sglang/commit/11cd2701a8) [#43005](https://github.com/sgl-project/sglang/pull/43005)
  fix(openai): preserve zero cached tokens when cache reporting is enabled (#43005)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/usage_processor.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`, `test/registered/unit/entrypoints/openai/test_usage_processor.py`_
- **2026-10-13** [`3f1e185f6e`](https://github.com/sgl-project/sglang/commit/3f1e185f6e) [#43026](https://github.com/sgl-project/sglang/pull/43026)
  fix(openai): keep chat stream created timestamp stable (#43026)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-10-13** [`27b68303d0`](https://github.com/sgl-project/sglang/commit/27b68303d0) [#43027](https://github.com/sgl-project/sglang/pull/43027)
  fix(openai): omit absent tool_calls from chat responses (#43027)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `test/registered/unit/entrypoints/openai/test_protocol.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-10-13** [`6a89181614`](https://github.com/sgl-project/sglang/commit/6a89181614) [#39771](https://github.com/sgl-project/sglang/pull/39771)
  tokenizer perf optimization (#39771)
  _Files: `python/sglang/srt/entrypoints/openai/serving_base.py`, `test/registered/unit/entrypoints/openai/test_serving_decisions.py`_

## Speculative Decoding  (8 commits)

- **2026-10-16** [`bdc4ec15ce`](https://github.com/sgl-project/sglang/commit/bdc4ec15ce) [#44405](https://github.com/sgl-project/sglang/pull/44405)
  [Perf] [AMD] dspark: No per-step host sync in decode (1/4) (#44405)
  _Files: `python/sglang/kernels/ops/speculative/dspark/simulated_bonus.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py` _+2 more__
- **2026-10-15** [`1d809bbbbd`](https://github.com/sgl-project/sglang/commit/1d809bbbbd) [#43502](https://github.com/sgl-project/sglang/pull/43502)
  [Fix] DSv4.1: Size the encoder-replay SWA pool by the DSpark draft's stages, and keep more prefix tails (#43502)
  _Files: `python/sglang/srt/arg_groups/fields/schedule.py`, `python/sglang/srt/model_executor/model_runner_components/spec_aux_hidden_state.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py` _+1 more__
- **2026-10-14** [`d2a436446c`](https://github.com/sgl-project/sglang/commit/d2a436446c) [#44252](https://github.com/sgl-project/sglang/pull/44252)
  [Feat] sgl-router: Fix cache-aware routing for MTP/EAGLE on hybrid (Mamba/KDA) models (#44252)
  _Files: `experimental/sgl-router/src/state/kv_events/discovery.rs`, `experimental/sgl-router/src/workers/introspect.rs`_
- **2026-10-14** [`05bb5afb62`](https://github.com/sgl-project/sglang/commit/05bb5afb62) [#43849](https://github.com/sgl-project/sglang/pull/43849)
  [NPU][Bugfix] use CANN libdevice for DSpark Markov sampling (#43849)
  _Files: `python/sglang/kernels/ops/speculative/dspark/markov_sample.py`_
- **2026-10-14** [`7e226b1b71`](https://github.com/sgl-project/sglang/commit/7e226b1b71) [#43640](https://github.com/sgl-project/sglang/pull/43640)
  [AMD] Use the preallocated EAGLE topk=1 draft chain on HIP (#43640)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-10-13** [`7dc2930585`](https://github.com/sgl-project/sglang/commit/7dc2930585) [#37577](https://github.com/sgl-project/sglang/pull/37577)
  [Feature] Add Aaronson-Gumbel text watermarking (#37577)
  _Files: `docs/docs.json`, `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/advanced_features/text_watermarking.mdx`, `examples/watermark/README.md` _+42 more__
- **2026-10-13** [`603a05e6c0`](https://github.com/sgl-project/sglang/commit/603a05e6c0) [#43328](https://github.com/sgl-project/sglang/pull/43328)
  [ROCm][Spec] Route NGRAM tree reconstruction to the JIT kernel on HIP (#43328)
  _Files: `python/sglang/srt/speculative/ngram_worker.py`, `test/registered/kernels/ops/speculative/test_ngram_utils.py`, `test/registered/spec/test_spec_ngram_extra.py`_
- **2026-10-12** [`392039d752`](https://github.com/sgl-project/sglang/commit/392039d752) [#43790](https://github.com/sgl-project/sglang/pull/43790)
  [DSpark] Share draft params, logits dtype, confidence and the accept tail between graph and eager (#43790)
  _Files: `python/sglang/srt/models/deepseek_v4_dspark.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py` _+7 more__

## LoRA  (2 commits)

- **2026-10-17** [`33b5d26fa6`](https://github.com/sgl-project/sglang/commit/33b5d26fa6) [#44771](https://github.com/sgl-project/sglang/pull/44771)
  [CI] lora: Use the canonical Llama model ID in eviction tests (#44771)
  _Files: `test/registered/lora/test_lora_eviction.py`_
- **2026-10-13** [`2a8e9db3b0`](https://github.com/sgl-project/sglang/commit/2a8e9db3b0) [#39798](https://github.com/sgl-project/sglang/pull/39798)
  [lora] Support LoRA for the NemotronH_Nano_VL_V2 model family (#39798)
  _Files: `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/lora/lora_manager.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/models/mllama4.py` _+6 more__

## Structured Output  (1 commits)

- **2026-10-18** [`80fef63786`](https://github.com/sgl-project/sglang/commit/80fef63786) [#44716](https://github.com/sgl-project/sglang/pull/44716)
  [Fix] Inkling: frame constrained output in native message tokens (#44716)
  _Files: `python/sglang/srt/constrained/base_grammar_backend.py`, `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/constrained/reasoner_grammar_backend.py`, `python/sglang/srt/constrained/xgrammar_backend.py` _+4 more__

---
_Generated 2026-10-19 15:31 UTC_