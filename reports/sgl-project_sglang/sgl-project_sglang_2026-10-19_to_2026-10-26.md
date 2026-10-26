# sgl-project/sglang — Weekly Change Report
**Period:** 2026-10-19 → 2026-10-26  |  **Total commits:** 630

## ✨ New Features This Week

- **2026-10-26** [#45925](https://github.com/sgl-project/sglang/pull/45925) — [Feat] minimax: Support MiniMax-M3.1-Flash (#45925)
- **2026-10-26** [#43341](https://github.com/sgl-project/sglang/pull/43341) — [Feat] [CPU] Grok-model: enable grok-2 model on xeon cpu (#43341)
- **2026-10-26** [#40467](https://github.com/sgl-project/sglang/pull/40467) — [Feat] hicache: Expose the Mooncake L3 object-key layout for external KV routers (#40467)
- **2026-10-26** [#45642](https://github.com/sgl-project/sglang/pull/45642) — [Doc] [NPU] cookbook: add A3 deployment scenarios to GLM-5.2 (#45642)
- **2026-10-26** [#46533](https://github.com/sgl-project/sglang/pull/46533) — [CI] deepep: Add release workflow for sgl-deep-ep-v25 (DeepEP 2.5) (#46533)
- **2026-10-26** [#36074](https://github.com/sgl-project/sglang/pull/36074) — [Feat] [NPU] llguidance: add bitmask path for Ascend (#36074)
- **2026-10-26** [#39774](https://github.com/sgl-project/sglang/pull/39774) — [Test] [NPU] return-output-ids: Add e2e test for --return-output-ids parameter (#39774)
- **2026-10-26** [#39772](https://github.com/sgl-project/sglang/pull/39772) — [Test] [NPU] return-input-ids: Add e2e test for --return-input-ids parameter (#39772)
- **2026-10-26** [#46506](https://github.com/sgl-project/sglang/pull/46506) — [Doc] cookbook: Add MiniMax-M3.1-Flash AgentX launches and refresh with nine InferenceX PRs (#46506)
- **2026-10-26** [#44611](https://github.com/sgl-project/sglang/pull/44611) — [Feat] mem_cache: tag Mooncake offloads with the writing session (#44611)
- _…and 113 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-26** [`ef11eb3b76`](https://github.com/sgl-project/sglang/commit/ef11eb3b76) [#33250](https://github.com/sgl-project/sglang/pull/33250) — [Fix] deepseek-v4: Fix DeepSeek-V4 non-EP TBO for attention TP > 1 (#33250)
- **2026-10-26** [`d19f19d68c`](https://github.com/sgl-project/sglang/commit/d19f19d68c) [#46453](https://github.com/sgl-project/sglang/pull/46453) — [CI] [AMD] pr-test: list tags with ls-remote, 8 small shards (#46453)
- **2026-10-26** [`d96c386335`](https://github.com/sgl-project/sglang/commit/d96c386335) [#45531](https://github.com/sgl-project/sglang/pull/45531) — [Fix] [AMD] attention: Pass the layer softcap to aiter unified-attention decode (#45531)
- **2026-10-26** [`6a28c96a49`](https://github.com/sgl-project/sglang/commit/6a28c96a49) [#45713](https://github.com/sgl-project/sglang/pull/45713) — [Perf] [AMD] kda: Use a HIP fused decode kernel by default for KDA (Kimi-K3) on gfx950 (#45713)
- **2026-10-26** [`c8398cb3a3`](https://github.com/sgl-project/sglang/commit/c8398cb3a3) [#45710](https://github.com/sgl-project/sglang/pull/45710) — [Perf] [AMD] kda: Use a HIP chunked-prefill kernel for KDA on gfx950 (#45710)
- **2026-10-26** [`0cd2a63b36`](https://github.com/sgl-project/sglang/commit/0cd2a63b36) [#41899](https://github.com/sgl-project/sglang/pull/41899) — [Perf] [AMD] quark/Qwen3.8: Quantize the BF16 shared expert of Quark MXFP4 checkpoints to MXFP4 while loading for shared-expert fusion (#41899)
- **2026-10-26** [`5b0be031e7`](https://github.com/sgl-project/sglang/commit/5b0be031e7) [#46236](https://github.com/sgl-project/sglang/pull/46236) — [Fix] [AMD] dsv4.1: Fix the V4.1 k-norm-rope store build on ROCm 10 (#46236)
- **2026-10-25** [`8252e3af63`](https://github.com/sgl-project/sglang/commit/8252e3af63) [#41701](https://github.com/sgl-project/sglang/pull/41701) — [Fix] [AMD] mamba: Keep a chunked prefill cut on the mamba chunk grid so DCP can donate checkpoints (#41701)
- **2026-10-25** [`b48809dfc2`](https://github.com/sgl-project/sglang/commit/b48809dfc2) [#46085](https://github.com/sgl-project/sglang/pull/46085) — [CI] [AMD] pr-test: Move large-model and perf tests from AMD PR CI to nightly (#46085)
- **2026-10-25** [`5d11819f3a`](https://github.com/sgl-project/sglang/commit/5d11819f3a) [#39729](https://github.com/sgl-project/sglang/pull/39729) — [Fix] disaggregation: Clean-up and optimize the KV checksum implementation (#39729)
- **2026-10-24** [`6563312956`](https://github.com/sgl-project/sglang/commit/6563312956) [#34543](https://github.com/sgl-project/sglang/pull/34543) — [Fix] [AMD] custom-allreduce: Stop registering oversized inputs in the deterministic all-reduce (#34543)
- **2026-10-24** [`b86d294a98`](https://github.com/sgl-project/sglang/commit/b86d294a98) [#45389](https://github.com/sgl-project/sglang/pull/45389) — [Refactor] kernels: Add the plugin kernel backend and split plugin contracts from their srt integration (#45389)
- **2026-10-24** [`efc9849520`](https://github.com/sgl-project/sglang/commit/efc9849520) [#45758](https://github.com/sgl-project/sglang/pull/45758) — [Perf] [AMD] GPT-OSS: Pick the gfx1250 W4A8 MoE backend, in-kernel GEMM 1 gather (#45758)
- **2026-10-24** [`85f5f7fd73`](https://github.com/sgl-project/sglang/commit/85f5f7fd73) [#46084](https://github.com/sgl-project/sglang/pull/46084) — [CI] [AMD] pr-test: Move tests in CUDA's extra tier to the AMD extra workflow (#46084)
- **2026-10-24** [`7671d16ce8`](https://github.com/sgl-project/sglang/commit/7671d16ce8) [#46161](https://github.com/sgl-project/sglang/pull/46161) — [Fix] [AMD] rotary: Pass a query-dtype cos_sin_cache to the HIP fallback (#46161)
- **2026-10-24** [`55f23a8b59`](https://github.com/sgl-project/sglang/commit/55f23a8b59) [#46151](https://github.com/sgl-project/sglang/pull/46151) — [Fix] [AMD] dsv4.1: Fix decode graph capture with quantized low-ratio activations (#46151)
- **2026-10-24** [`de7055f596`](https://github.com/sgl-project/sglang/commit/de7055f596) [#41140](https://github.com/sgl-project/sglang/pull/41140) — [Refactor] pd: Consolidate sender and receiver implementations (#41140)
- **2026-10-24** [`88ac7c02a6`](https://github.com/sgl-project/sglang/commit/88ac7c02a6) [#45838](https://github.com/sgl-project/sglang/pull/45838) — [Fix] [AMD] diffusion: Fix the first-step denoise regression from compiling ENABLE_CK=0 BF16 attention (#45838)
- **2026-10-23** [`194abb8e54`](https://github.com/sgl-project/sglang/commit/194abb8e54) [#45983](https://github.com/sgl-project/sglang/pull/45983) — [CI] [AMD] diffusion: Drain the Cosmos Dreams decode stream after freeing its outputs (#45983)
- **2026-10-23** [`ac3db731b3`](https://github.com/sgl-project/sglang/commit/ac3db731b3) [#45917](https://github.com/sgl-project/sglang/pull/45917) — [Fix] moe: Preserve CUTLASS routing metadata and execution budgets (#45917)
- **2026-10-23** [`0931dfedc9`](https://github.com/sgl-project/sglang/commit/0931dfedc9) [#39083](https://github.com/sgl-project/sglang/pull/39083) — [Fix] [AMD] dsa: Fix AITER prefill with an FP8 KV cache (#39083)
- **2026-10-23** [`1340044e97`](https://github.com/sgl-project/sglang/commit/1340044e97) [#45915](https://github.com/sgl-project/sglang/pull/45915) — [Fix] deepseek-v4: Preserve decoder-tail token-count ownership (#45915)
- **2026-10-23** [`9d7ad308bd`](https://github.com/sgl-project/sglang/commit/9d7ad308bd) [#40776](https://github.com/sgl-project/sglang/pull/40776) — [Fix] [AMD] Quark: fix Quark block-FP8 loading in DeepSeek loader (#40776)
- **2026-10-23** [`baf80c61b7`](https://github.com/sgl-project/sglang/commit/baf80c61b7) [#45897](https://github.com/sgl-project/sglang/pull/45897) — [Feat] platforms: Let out-of-tree platforms bind group devices and custom ops (#45897)
- **2026-10-23** [`f967418a35`](https://github.com/sgl-project/sglang/commit/f967418a35) [#46032](https://github.com/sgl-project/sglang/pull/46032) — [Doc] cookbook: Qwen3.5 MI355X FP8 agentic adds scheduler/tokenizer tuning from the InferenceX recipe (#46032)
- **2026-10-23** [`69f830756e`](https://github.com/sgl-project/sglang/commit/69f830756e) [#46017](https://github.com/sgl-project/sglang/pull/46017) — [Doc] cookbook: Qwen3.5 MI355X FP8 agentic uses HiCache write_through on the v0.5.22 image (#46017)
- **2026-10-23** [`bb72b47daf`](https://github.com/sgl-project/sglang/commit/bb72b47daf) [#45728](https://github.com/sgl-project/sglang/pull/45728) — [Test] [AMD] deepseek-v4.1: Give the encoder-replay test's request window a zero_row (#45728)
- **2026-10-23** [`7d1a16d3eb`](https://github.com/sgl-project/sglang/commit/7d1a16d3eb) [#45861](https://github.com/sgl-project/sglang/pull/45861) — [CI] [AMD] diffusion: Skip the LTX-2.5 diffusion decoder case on the 2-GPU lane (#45861)
- **2026-10-23** [`6e667c4310`](https://github.com/sgl-project/sglang/commit/6e667c4310) [#45973](https://github.com/sgl-project/sglang/pull/45973) — [Fix] disaggregation: Poison the deferred abort ack when a NIXL or Mori write fails (#45973)
- **2026-10-23** [`6c844eb12e`](https://github.com/sgl-project/sglang/commit/6c844eb12e) [#45941](https://github.com/sgl-project/sglang/pull/45941) — [Perf] dsv4: Replay the V4.1 prefill graph past 16K contexts on SM90 (#45941)
- **2026-10-23** [`7baacd1d1b`](https://github.com/sgl-project/sglang/commit/7baacd1d1b) [#45882](https://github.com/sgl-project/sglang/pull/45882) — [CI] [AMD] docker: Add a build-only dispatch option to the ROCm nightly image workflows (#45882)
- **2026-10-23** [`e83f585ae6`](https://github.com/sgl-project/sglang/commit/e83f585ae6) [#45893](https://github.com/sgl-project/sglang/pull/45893) — [Perf] dsv41: Serve token-interleaved V4.1 KV caches with sgl-flash-mla (#45893)
- **2026-10-23** [`5daa1352ba`](https://github.com/sgl-project/sglang/commit/5daa1352ba) [#42567](https://github.com/sgl-project/sglang/pull/42567) — [CI] tests: Retire test/srt and reject legacy test paths (#42567)
- **2026-10-23** [`a95ae5f1c5`](https://github.com/sgl-project/sglang/commit/a95ae5f1c5) [#45848](https://github.com/sgl-project/sglang/pull/45848) — [CI] [AMD] docker: Start the ROCm 10 nightly at 10:00 UTC and ROCm 7.2 at 11:00 UTC (#45848)
- **2026-10-23** [`9c7dd3c45f`](https://github.com/sgl-project/sglang/commit/9c7dd3c45f) [#45909](https://github.com/sgl-project/sglang/pull/45909) — [Perf] dsv4: Dequantize each shared sparse-prefill KV source once per forward (#45909)
- **2026-10-22** [`035ed73b9d`](https://github.com/sgl-project/sglang/commit/035ed73b9d) [#45676](https://github.com/sgl-project/sglang/pull/45676) — [Fix] [AMD] kernels: Import the HIP launch helpers from jit.utils.hipcc in smallm_fp8_blockscale_gfx950 (#45676)
- **2026-10-22** [`0d6b283d7e`](https://github.com/sgl-project/sglang/commit/0d6b283d7e) [#45783](https://github.com/sgl-project/sglang/pull/45783) — [Refactor] dsv4: Keep only the two-level V4.1 indexer in the prefill graph (#45783)
- **2026-10-22** [`c80285ca9a`](https://github.com/sgl-project/sglang/commit/c80285ca9a) [#43809](https://github.com/sgl-project/sglang/pull/43809) — [Fix] [AMD] deterministic: Refuse RCCL all-reduce in deterministic mode above TP2 (#43809)
- **2026-10-22** [`0a87f163dc`](https://github.com/sgl-project/sglang/commit/0a87f163dc) [#45507](https://github.com/sgl-project/sglang/pull/45507) — [Test] [AMD] deepseek-v4.1: Fix the HIP breakable-graph unit tests for the default prefill context limit and the DSpark draft ring (#45507)
- **2026-10-22** [`1c967f5043`](https://github.com/sgl-project/sglang/commit/1c967f5043) [#34241](https://github.com/sgl-project/sglang/pull/34241) — [Fix] [AMD] test: Recalibrate MiniMax-M2.7 GSM8K threshold 0.93->0.91 for MI300 runners (#34241)
- **2026-10-22** [`b5137693a5`](https://github.com/sgl-project/sglang/commit/b5137693a5) [#45304](https://github.com/sgl-project/sglang/pull/45304) — [Fix] [AMD] diffusion: Enable `--quantization fp8` on gfx1250 (torch.compile lowering + per-channel weight scales) (#45304)
- **2026-10-22** [`f91b81b82a`](https://github.com/sgl-project/sglang/commit/f91b81b82a) [#45689](https://github.com/sgl-project/sglang/pull/45689) — [Doc] [AMD] cookbook: Add Muse Spark Open MI355X AgentX recipe (#45689)
- **2026-10-22** [`17babd67b4`](https://github.com/sgl-project/sglang/commit/17babd67b4) [#45699](https://github.com/sgl-project/sglang/pull/45699) — [Fix] dsv4: Never read attention metadata for idle SWA stores (#45699)
- **2026-10-22** [`9ee9858805`](https://github.com/sgl-project/sglang/commit/9ee9858805) [#45693](https://github.com/sgl-project/sglang/pull/45693) — [Doc] [AMD] dsv41: Update amd cookbook 1021 (#45693)
- **2026-10-22** [`5fff58a169`](https://github.com/sgl-project/sglang/commit/5fff58a169) [#45469](https://github.com/sgl-project/sglang/pull/45469) — [CI] [AMD] miles: Fix the ROCm 10 nightly suites that never finish (#45469)
- **2026-10-21** [`991b846227`](https://github.com/sgl-project/sglang/commit/991b846227) [#42803](https://github.com/sgl-project/sglang/pull/42803) — [Perf] speculative: Parallelize EAGLE spec-decode KV index building over token blocks (flashinfer draft decode; verify/draft-extend for flashinfer, flashinfer_mla, aiter) (#42803)
- **2026-10-21** [`51baa1f6e9`](https://github.com/sgl-project/sglang/commit/51baa1f6e9) [#45408](https://github.com/sgl-project/sglang/pull/45408) — [Test] [AMD] debug-utils: Opt TestCrashDump into expect_server_exit (#45408)
- **2026-10-21** [`f7d4f06242`](https://github.com/sgl-project/sglang/commit/f7d4f06242) [#45579](https://github.com/sgl-project/sglang/pull/45579) — [Perf] dsv4: Compute request-window history rows once per batch (#45579)
- **2026-10-21** [`7e0e259435`](https://github.com/sgl-project/sglang/commit/7e0e259435) [#45519](https://github.com/sgl-project/sglang/pull/45519) — [CI] [AMD] disaggregation: Register Mooncake KV buffers without HIP dmabuf (#45519)
- **2026-10-21** [`6e98c84c60`](https://github.com/sgl-project/sglang/commit/6e98c84c60) [#39598](https://github.com/sgl-project/sglang/pull/39598) — [Perf] [AMD] quark: Add opt-in AITER ASM FP4 GEMM for Quark dense linear (#39598)
- **2026-10-21** [`4b1a44bc77`](https://github.com/sgl-project/sglang/commit/4b1a44bc77) [#45409](https://github.com/sgl-project/sglang/pull/45409) — [Test] [AMD] diffusion: Avoid Python 3.11-only enterContext in test_usp_ring_replicated (#45409)
- **2026-10-21** [`131c42ba33`](https://github.com/sgl-project/sglang/commit/131c42ba33) [#45498](https://github.com/sgl-project/sglang/pull/45498) — [Perf] [AMD] aiter: Update ROCm AITER pin to 285579b62 (gfx942/gfx950 only) (#45498)
- **2026-10-21** [`1278087336`](https://github.com/sgl-project/sglang/commit/1278087336) [#45546](https://github.com/sgl-project/sglang/pull/45546) — [Fix] [AMD] mono-kernel: Update sgl-amd-mono version (#45546)
- **2026-10-21** [`132836b369`](https://github.com/sgl-project/sglang/commit/132836b369) [#45329](https://github.com/sgl-project/sglang/pull/45329) — [Fix] [AMD] docker: Build Triton from source for ROCm 10.1 gfx1250 (#45329)
- **2026-10-21** [`bd5a445bf7`](https://github.com/sgl-project/sglang/commit/bd5a445bf7) [#45480](https://github.com/sgl-project/sglang/pull/45480) — [Fix] [AMD] dsv41: Set moe act to fp8 by default (#45480)
- **2026-10-21** [`956b9a24ee`](https://github.com/sgl-project/sglang/commit/956b9a24ee) [#42229](https://github.com/sgl-project/sglang/pull/42229) — [Perf] [AMD] qwen3.5: Fuse activation quant into small-M FP8 block-scale GEMM on gfx950 (#42229)
- **2026-10-21** [`4b5c9c4b5e`](https://github.com/sgl-project/sglang/commit/4b5c9c4b5e) [#45099](https://github.com/sgl-project/sglang/pull/45099) — [Perf] [AMD] attention: Restore the gfx950 extend tile for head_dim <= 128 (#45099)
- **2026-10-21** [`f1ba723c64`](https://github.com/sgl-project/sglang/commit/f1ba723c64) [#45476](https://github.com/sgl-project/sglang/pull/45476) — [Test] [AMD] moe: Expect gfx1250 W4A8 layers to build with expert parallelism (#45476)
- **2026-10-20** [`9686edcf80`](https://github.com/sgl-project/sglang/commit/9686edcf80) [#45124](https://github.com/sgl-project/sglang/pull/45124) — [Perf] [AMD] dsv41: faster mHC boundary Triton tile for 96+ rows, bitwise unchanged (#45124)
- **2026-10-20** [`299a75ac5d`](https://github.com/sgl-project/sglang/commit/299a75ac5d) [#44994](https://github.com/sgl-project/sglang/pull/44994) — [Refactor] moe: Derive routing inputs from the layer and active forward (#44994)
- **2026-10-20** [`533020b500`](https://github.com/sgl-project/sglang/commit/533020b500) [#45123](https://github.com/sgl-project/sglang/pull/45123) — [Perf] [AMD] dsv41: run gfx950 MXFP8 dense GEMMs on aiter's preshuffled FlyDSL kernel (#45123)
- **2026-10-20** [`4f8f06faf3`](https://github.com/sgl-project/sglang/commit/4f8f06faf3) [#44993](https://github.com/sgl-project/sglang/pull/44993) — [Refactor] moe: Derive layer contracts from the selected quant method (#44993)
- **2026-10-20** [`d5e83ea4f6`](https://github.com/sgl-project/sglang/commit/d5e83ea4f6) [#45098](https://github.com/sgl-project/sglang/pull/45098) — [Perf] [AMD] deterministic: Faster extend attention launch on gfx950 (#45098)
- **2026-10-20** [`29274b41c6`](https://github.com/sgl-project/sglang/commit/29274b41c6) [#44198](https://github.com/sgl-project/sglang/pull/44198) — [Fix] [AMD] activation: Run ReLU2 natively on ROCm (#44198)
- **2026-10-20** [`82ac83a8d0`](https://github.com/sgl-project/sglang/commit/82ac83a8d0) [#45339](https://github.com/sgl-project/sglang/pull/45339) — [Perf] [AMD] dsv41: Skip unneeded layer 20 computation under decoder-bounded-replay (#45339)
- **2026-10-20** [`f82465718b`](https://github.com/sgl-project/sglang/commit/f82465718b) [#44596](https://github.com/sgl-project/sglang/pull/44596) — [Test] [AMD] diffusion: Skip MOSS-Image mismatched-operand test on ROCm (#44596)
- **2026-10-20** [`89860fbd2e`](https://github.com/sgl-project/sglang/commit/89860fbd2e) [#45365](https://github.com/sgl-project/sglang/pull/45365) — [Fix] [AMD] gpt-oss: support EP for gfx1250 W4A8 MXFP4 MoE (#45365)
- **2026-10-20** [`7591118794`](https://github.com/sgl-project/sglang/commit/7591118794) [#45217](https://github.com/sgl-project/sglang/pull/45217) — [Fix] [AMD] grok: accept allow_patterns_overrides in presharded _prepare_weights patch (#45217)
- **2026-10-20** [`407bfc94f9`](https://github.com/sgl-project/sglang/commit/407bfc94f9) [#44599](https://github.com/sgl-project/sglang/pull/44599) — [Test] [AMD] diffusion: Make multimodal_gen unit tests ROCm-aware (#44599)
- **2026-10-20** [`36978d6c4d`](https://github.com/sgl-project/sglang/commit/36978d6c4d) [#44421](https://github.com/sgl-project/sglang/pull/44421) — [Test] [AMD] diffusion: Skip the Kandinsky6 FA dispatch test on ROCm (#44421)
- **2026-10-20** [`50fa3727eb`](https://github.com/sgl-project/sglang/commit/50fa3727eb) [#45297](https://github.com/sgl-project/sglang/pull/45297) — [Doc] [AMD] cookbook: Fix DeepSeek-V4 PD image and c1 capacity (#45297)
- **2026-10-20** [`472f0d540b`](https://github.com/sgl-project/sglang/commit/472f0d540b) [#45301](https://github.com/sgl-project/sglang/pull/45301) — [Fix] deepseek-v4.1: Keep the padded query buffer inside decoder tail graphs (#45301)
- **2026-10-20** [`1140a8dfd9`](https://github.com/sgl-project/sglang/commit/1140a8dfd9) [#43335](https://github.com/sgl-project/sglang/pull/43335) — [Fix] [AMD] aiter: Fix garbage decode output for non-sliding-window models on the vectorized_5d KV layout (#43335)
- **2026-10-19** [`6b90e5716d`](https://github.com/sgl-project/sglang/commit/6b90e5716d) [#44913](https://github.com/sgl-project/sglang/pull/44913) — [Refactor] moe: Scope shared-expert configuration to each model (#44913)
- **2026-10-19** [`964ab2b280`](https://github.com/sgl-project/sglang/commit/964ab2b280) [#44912](https://github.com/sgl-project/sglang/pull/44912) — [Refactor] moe: Split the two meanings of num_fused_shared_experts (#44912)
- **2026-10-19** [`3a059de94c`](https://github.com/sgl-project/sglang/commit/3a059de94c) [#44901](https://github.com/sgl-project/sglang/pull/44901) — [Fix] moe: Count routed_scaling_factor once when top-k folds it (#44901)
- **2026-10-19** [`49766a74f9`](https://github.com/sgl-project/sglang/commit/49766a74f9) [#43438](https://github.com/sgl-project/sglang/pull/43438) — [Fix] attn_residual: int64 program ids in the score/combine kernels (int32 overflow at 37,451 tokens) (#43438)
- **2026-10-19** [`7656ea0e74`](https://github.com/sgl-project/sglang/commit/7656ea0e74) [#44393](https://github.com/sgl-project/sglang/pull/44393) — [CI] python: Move the remaining CUDA build paths off Python 3.10 (#44393)
- **2026-10-19** [`80b86dbecb`](https://github.com/sgl-project/sglang/commit/80b86dbecb) [#44672](https://github.com/sgl-project/sglang/pull/44672) — [Fix] [AMD] diffusion: Accept residual and skip_bias in the ROCm Conv3d-to-Conv2d VAE patch (#44672)
- **2026-10-19** [`5ed306bd69`](https://github.com/sgl-project/sglang/commit/5ed306bd69) [#44671](https://github.com/sgl-project/sglang/pull/44671) — [Fix] [AMD] diffusion: Keep gfx1250 FlyDSL BF16 attention out of torch.compile (#44671)
- **2026-10-19** [`7c4cc5a51c`](https://github.com/sgl-project/sglang/commit/7c4cc5a51c) [#41229](https://github.com/sgl-project/sglang/pull/41229) — [Perf] [AMD] attention: Spread uneven Triton decode batches across XCDs (#41229)
- **2026-10-19** [`a90e9c5dd8`](https://github.com/sgl-project/sglang/commit/a90e9c5dd8) [#44443](https://github.com/sgl-project/sglang/pull/44443) — [Fix] [AMD] mhc: Bound the Triton fused post+pre buffer cache (#44443)
- **2026-10-19** [`8111841103`](https://github.com/sgl-project/sglang/commit/8111841103) [#43733](https://github.com/sgl-project/sglang/pull/43733) — [Perf] deepseek-v4.1: Replay the breakable prefill CUDA graph at any context length (#43733)
- **2026-10-19** [`5d9c956f8e`](https://github.com/sgl-project/sglang/commit/5d9c956f8e) [#45070](https://github.com/sgl-project/sglang/pull/45070) — [Doc] [AMD] dsv4: Update amd cookbook 1016 (#45070)
- **2026-10-19** [`3d588779e1`](https://github.com/sgl-project/sglang/commit/3d588779e1) [#40674](https://github.com/sgl-project/sglang/pull/40674) — [CI] [AMD] test: Run UMBP HiCache E2E through standalone DRAM server (#40674)
- **2026-10-19** [`8d3eee46a7`](https://github.com/sgl-project/sglang/commit/8d3eee46a7) [#44927](https://github.com/sgl-project/sglang/pull/44927) — [Perf] [AMD] deepseek-v4: Skip top-k refinement for proven positive-zero ties (#44927)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#46588](https://github.com/sgl-project/sglang/issues/46588) | [Roadmap] TDX/CC Prefill–Decode Disaggregation | — | 2026-10-26 |
| [#41648](https://github.com/sgl-project/sglang/issues/41648) | [Feature] Attention–FFN disaggregation with pipelining and CUDA Graph  | — | 2026-10-26 |
| [#46520](https://github.com/sgl-project/sglang/issues/46520) | [RFC] [XPU] paged-experts: Intel XPU support with Lookahead Expert Sch | — | 2026-10-26 |
| [#46446](https://github.com/sgl-project/sglang/issues/46446) | [Bug] Qwen3.5-9B deterministic greedy output differs with mixed-chunk  | — | 2026-10-26 |
| [#46418](https://github.com/sgl-project/sglang/issues/46418) | [Bug] JIT link fails with the pip CUDA toolkit: -L$CUDA_HOME/lib64 -lc | — | 2026-10-26 |
| [#43412](https://github.com/sgl-project/sglang/issues/43412) | Speculative decoding crashes server on first non-greedy request: flash | — | 2026-10-26 |
| [#46455](https://github.com/sgl-project/sglang/issues/46455) | [PD] Per-backend transport interface | — | 2026-10-25 |
| [#46462](https://github.com/sgl-project/sglang/issues/46462) | AMD Development Roadmap (2026 Q4) | — | 2026-10-25 |
| [#33522](https://github.com/sgl-project/sglang/issues/33522) | [Roadmap]Fast Engine Recovery: Weight Cache Daemon | — | 2026-10-25 |
| [#42473](https://github.com/sgl-project/sglang/issues/42473) | Development Roadmap (2026 Q4) | — | 2026-10-25 |
| [#39499](https://github.com/sgl-project/sglang/issues/39499) | [Roadmap] SGLang dLLM Serving | — | 2026-10-25 |
| [#45367](https://github.com/sgl-project/sglang/issues/45367) | [Bug] Kimi-K3 DCP a2a produces garbled decode output on 2-node GB300;  | — | 2026-10-25 |
| [#45847](https://github.com/sgl-project/sglang/issues/45847) | [Failure Tracker] PR Test (AMD) | ci-failure-tracker | 2026-10-25 |
| [#45373](https://github.com/sgl-project/sglang/issues/45373) | [Tracking] GLM-5.3-Flash performance optimization on Hopper (SM90) | — | 2026-10-25 |
| [#38515](https://github.com/sgl-project/sglang/issues/38515) | sgl_kernel AOT: rmsnorm NoKernelImage on sm_75 while silu_and_mul / ge | — | 2026-10-25 |
| [#42508](https://github.com/sgl-project/sglang/issues/42508) | [Bug] Scheduler aborts with `double free or corruption` inside the idl | — | 2026-10-24 |
| [#30599](https://github.com/sgl-project/sglang/issues/30599) | [Feature][AMD] Officially support consumer Radeon RDNA3/RDNA4 (gfx1100 | amd | 2026-10-24 |
| [#46314](https://github.com/sgl-project/sglang/issues/46314) | [Bug] diffusion quantization layer: 11 correctness bugs (ModelSlim MXF | — | 2026-10-24 |
| [#46312](https://github.com/sgl-project/sglang/issues/46312) | [Bug] DeepSeek AWQ checkpoints fail to load on CUDA: ModuleNotFoundErr | — | 2026-10-24 |
| [#46310](https://github.com/sgl-project/sglang/issues/46310) | [Performance] DeepSeek-V4.1-Flash-1017 on 8x H20-3e: SGLang vs DeepInf | — | 2026-10-24 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 135 |
| Multimodal | 123 |
| MoE / Expert Parallel | 64 |
| Prefill / Decode Disaggregation | 52 |
| KV Cache / Memory | 43 |
| Quantization | 31 |
| Other | 30 |
| CI / Build | 27 |
| Triton / Kernels | 20 |
| Tensor / Data Parallel | 19 |
| ROCm / AMD | 18 |
| Scheduler / Batching | 15 |
| Speculative Decoding | 14 |
| Docs / Examples | 10 |
| Models | 10 |
| LoRA | 9 |
| Structured Output | 5 |
| Serving / API | 5 |

## Attention / FlashInfer  (135 commits)

- **2026-10-26** [`9841183827`](https://github.com/sgl-project/sglang/commit/9841183827) [#46308](https://github.com/sgl-project/sglang/pull/46308)
  [Perf] diffusion: Hide the pipelined Ulysses own-row copies behind the exchange (#46308)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a_multi.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`, `python/sglang/multimodal_gen/test/single_test_file/test_usp_pipelined_attention_multi_gpu.py`_
- **2026-10-26** [`d96c386335`](https://github.com/sgl-project/sglang/commit/d96c386335) [#45531](https://github.com/sgl-project/sglang/pull/45531)
  [Fix] [AMD] attention: Pass the layer softcap to aiter unified-attention decode (#45531)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/attention/test_aiter_fp8_q_unified_attention.py`_
- **2026-10-26** [`6a28c96a49`](https://github.com/sgl-project/sglang/commit/6a28c96a49) [#45713](https://github.com/sgl-project/sglang/pull/45713)
  [Perf] [AMD] kda: Use a HIP fused decode kernel by default for KDA (Kimi-K3) on gfx950 (#45713)
  _Files: `python/sglang/kernels/kda_kernels/README.md`, `python/sglang/kernels/kda_kernels/csrc/attention/kda_decode_gfx950.cu`, `python/sglang/kernels/kda_kernels/kda_decode_gfx950.py`, `python/sglang/kernels/ops/attention/__init__.py` _+4 more__
- **2026-10-26** [`c8398cb3a3`](https://github.com/sgl-project/sglang/commit/c8398cb3a3) [#45710](https://github.com/sgl-project/sglang/pull/45710)
  [Perf] [AMD] kda: Use a HIP chunked-prefill kernel for KDA on gfx950 (#45710)
  _Files: `python/sglang/kernels/kda_kernels/README.md`, `python/sglang/kernels/kda_kernels/csrc/attention/kda_prefill_gfx950.cu`, `python/sglang/kernels/kda_kernels/kda_prefill_gfx950.py`, `python/sglang/kernels/ops/attention/__init__.py` _+3 more__
- **2026-10-26** [`d42e1ee7e1`](https://github.com/sgl-project/sglang/commit/d42e1ee7e1) [#46547](https://github.com/sgl-project/sglang/pull/46547)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches with MiniMax-M3.1-Flash B200 / GB200 HiCache points (#46547)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+4 more__
- **2026-10-26** [`655c2cdd64`](https://github.com/sgl-project/sglang/commit/655c2cdd64) [#46263](https://github.com/sgl-project/sglang/pull/46263)
  [Perf] [NVIDIA] deepseek-v4.1: Default aggregated servers to MegaAttention only when each rank holds 64 query heads (#46263)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/fields/exec_.py`_
- **2026-10-26** [`3d2a781b3e`](https://github.com/sgl-project/sglang/commit/3d2a781b3e) [#46516](https://github.com/sgl-project/sglang/pull/46516)
  [Refactor] dsv4: Write the replay tail's outputs into caller-held prefill graph bridges (#46516)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/models/deepseek_v4_replay_tail.py`, `test/registered/unit/model_executor/test_num_token_non_padded_localization.py`_
- **2026-10-26** [`a0618d5e65`](https://github.com/sgl-project/sglang/commit/a0618d5e65) [#46468](https://github.com/sgl-project/sglang/pull/46468)
  [Perf] [NVIDIA] kimi-k3: Route draft/dense bf16 GEMMs to TGV and narrow the MLA output gate vector (#46468)
  _Files: `python/sglang/kernels/jit/csrc/kimi_k3/mla_output_gate.cuh`, `python/sglang/kernels/ops/gemm/cutedsl_bf16_gemm.py`_
- **2026-10-26** [`e8019014b0`](https://github.com/sgl-project/sglang/commit/e8019014b0) [#46399](https://github.com/sgl-project/sglang/pull/46399)
  [Refactor] dsv41: Write the candidate table into caller-held prefill graph buffers (#46399)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/sparse_table.py`, `python/sglang/srt/model_executor/runner_backend_utils/breakable_cuda_graph/breakable_cuda_graph.py`_
- **2026-10-26** [`3f29ad1145`](https://github.com/sgl-project/sglang/commit/3f29ad1145) [#46506](https://github.com/sgl-project/sglang/pull/46506)
  [Doc] cookbook: Add MiniMax-M3.1-Flash AgentX launches and refresh with nine InferenceX PRs (#46506)
  _Files: `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx` _+6 more__
- **2026-10-26** [`132b0f0ae7`](https://github.com/sgl-project/sglang/commit/132b0f0ae7) [#46417](https://github.com/sgl-project/sglang/pull/46417)
  [Fix] [Intel] dp-attention: Skip the CustomAllReduceV2 import on XPU (#46417)
  _Files: `python/sglang/srt/layers/dp_attention.py`_
- **2026-10-26** [`65f19fce48`](https://github.com/sgl-project/sglang/commit/65f19fce48) [#45794](https://github.com/sgl-project/sglang/pull/45794)
  [Perf] [NVIDIA] deepseek-v4.1: Align BF16 prefill indexer score width (#45794)
  _Files: `python/sglang/srt/layers/attention/dsv4/v41_indexer/scoring.py`_
- **2026-10-26** [`cf66f7ed73`](https://github.com/sgl-project/sglang/commit/cf66f7ed73) [#46247](https://github.com/sgl-project/sglang/pull/46247)
  [Perf] diffusion: Write Wan's normed q/k straight into the Ulysses exchange (#46247)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/rmsnorm_interleaved_rope_cutedsl.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a_multi.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py` _+6 more__
- **2026-10-26** [`5b0be031e7`](https://github.com/sgl-project/sglang/commit/5b0be031e7) [#46236](https://github.com/sgl-project/sglang/pull/46236)
  [Fix] [AMD] dsv4.1: Fix the V4.1 k-norm-rope store build on ROCm 10 (#46236)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh`, `test/registered/kernels/ops/attention/dsv4/test_v41_kv_store.py`_
- **2026-10-26** [`d6ccb495da`](https://github.com/sgl-project/sglang/commit/d6ccb495da) [#45949](https://github.com/sgl-project/sglang/pull/45949)
  [Perf] [NPU] AscendAttnBackend: D2H-free block-table gather for mirrorless DSA graph replay (#45949)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py` _+1 more__
- **2026-10-25** [`640e11ebc0`](https://github.com/sgl-project/sglang/commit/640e11ebc0) [#46465](https://github.com/sgl-project/sglang/pull/46465)
  [Perf] [NVIDIA] kda: Narrower V tiles for the KDA spec-verify recurrence on SM107 (#46465)
  _Files: `python/sglang/kernels/ops/attention/linear/fused_sigmoid_gating_recurrent.py`_
- **2026-10-25** [`f264183bfe`](https://github.com/sgl-project/sglang/commit/f264183bfe) [#46359](https://github.com/sgl-project/sglang/pull/46359)
  [Feat] dcp: Replicate a block-FP8 q_b_proj under --dcp-replicate-q-proj (#46359)
  _Files: `docs/docs/advanced_features/dcp.mdx`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_v2.py`_
- **2026-10-25** [`1406ffda09`](https://github.com/sgl-project/sglang/commit/1406ffda09) [#46243](https://github.com/sgl-project/sglang/pull/46243)
  [Feat] rust: Render DeepSeek-V4/V4.1 prompts with deepseek-recipe in sglang-processor and sgl-router (#46243)
  _Files: `.agents/skills/processor-model-parity/SKILL.md`, `rust/Cargo.lock`, `rust/sglang-processor/Cargo.toml`, `rust/sglang-processor/README.md` _+30 more__
- **2026-10-25** [`4991bd33ae`](https://github.com/sgl-project/sglang/commit/4991bd33ae) [#46141](https://github.com/sgl-project/sglang/pull/46141)
  [Feat] attention: Add the MSA-v1 sparse backend and NVFP4 KV pool (#46141)
  _Files: `python/sglang/kernels/jit/csrc/minimax/fused_gemma_qknorm_rope.cuh`, `python/sglang/kernels/ops/attention/minimax_qknorm_rope.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/graph_utils.py` _+13 more__
- **2026-10-25** [`174bd2976d`](https://github.com/sgl-project/sglang/commit/174bd2976d) [#46139](https://github.com/sgl-project/sglang/pull/46139)
  [Feat] msa: Add MSA-v1 decode and NVFP4 KV cache kernels (#46139)
  _Files: `python/sglang/kernels/jit/csrc/kvcacheio/page_row.cuh`, `python/sglang/kernels/jit/csrc/minimax/msa_v1/attn/dequant.cuh`, `python/sglang/kernels/jit/csrc/minimax/nvfp4_store_kv_index.cuh`, `python/sglang/kernels/ops/attention/__init__.py` _+6 more__
- **2026-10-25** [`9b230c1dae`](https://github.com/sgl-project/sglang/commit/9b230c1dae) [#46138](https://github.com/sgl-project/sglang/pull/46138)
  [Fix] dp-attention: Align prefill graph buckets and decode padding across DP ranks (#46138)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py` _+1 more__
- **2026-10-25** [`dba22e9b68`](https://github.com/sgl-project/sglang/commit/dba22e9b68) [#45752](https://github.com/sgl-project/sglang/pull/45752)
  [Perf] QSA: Optimize the prefill indexer gather (#45752)
  _Files: `python/sglang/srt/layers/attention/qsa/kernel.py`, `python/sglang/srt/layers/attention/qsa/metadata.py`, `test/registered/kernels/ops/attention/qsa/test_qsa.py`_
- **2026-10-25** [`5971f47bc8`](https://github.com/sgl-project/sglang/commit/5971f47bc8) [#46179](https://github.com/sgl-project/sglang/pull/46179)
  [Perf] dsa: Overlap CP KV gather with indexer computation (#46179)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_kpool.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/cp/bcg/interleave_bcg.py` _+2 more__
- **2026-10-25** [`38ff13ea79`](https://github.com/sgl-project/sglang/commit/38ff13ea79) [#46330](https://github.com/sgl-project/sglang/pull/46330)
  [Feat] spec: Support CUDA attention DP for DFlash and DFlash2 (#46330)
  _Files: `docs/docs/advanced_features/speculative_decoding.mdx`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/speculative/dflash_dp.py` _+4 more__
- **2026-10-25** [`6623ea445a`](https://github.com/sgl-project/sglang/commit/6623ea445a) [#46290](https://github.com/sgl-project/sglang/pull/46290)
  [Refactor] spec: Resolve draft parallel placement from model declarations (#46290)
  _Files: `python/sglang/srt/configs/draft_parallel.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/mem_cache/draft_kv_budget.py` _+25 more__
- **2026-10-25** [`db7b66c1b6`](https://github.com/sgl-project/sglang/commit/db7b66c1b6) [#46135](https://github.com/sgl-project/sglang/pull/46135)
  [Perf] minimax-sparse: Speed up MiniMax-M3 sparse attention on Hopper (#46135)
  _Files: `python/sglang/kernels/jit/csrc/minimax/fused_store_kv_index.cuh`, `python/sglang/kernels/ops/attention/minimax_sparse/common/tile_ptr.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/kernels/ops/attention/minimax_sparse/decode/topk_sparse.py` _+4 more__
- **2026-10-25** [`50d767a447`](https://github.com/sgl-project/sglang/commit/50d767a447) [#45110](https://github.com/sgl-project/sglang/pull/45110)
  [Fix] kimi-k3: Avoid vision attention child-name collisions (#45110)
  _Files: `python/sglang/srt/models/kimi_k3_vl.py`, `test/registered/unit/models/test_kimi_k3_vision.py`_
- **2026-10-24** [`13b7ef75c5`](https://github.com/sgl-project/sglang/commit/13b7ef75c5) [#46145](https://github.com/sgl-project/sglang/pull/46145)
  [Perf] diffusion: Keep same-device copies out of the pipelined Ulysses exchange (#46145)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/layout/head_group_copy_triton.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a_multi.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/attention_backend.py` _+5 more__
- **2026-10-24** [`052feb72a8`](https://github.com/sgl-project/sglang/commit/052feb72a8) [#42929](https://github.com/sgl-project/sglang/pull/42929)
  [Perf] dsv4: Vectorize paged KV cache dequantization (#42929)
  _Files: `python/sglang/kernels/ops/attention/dsv4/dequant_k_cache.py`, `test/registered/kernels/ops/attention/test_dsv4_dequant_k_cache.py`_
- **2026-10-24** [`b86d294a98`](https://github.com/sgl-project/sglang/commit/b86d294a98) [#45389](https://github.com/sgl-project/sglang/pull/45389)
  [Refactor] kernels: Add the plugin kernel backend and split plugin contracts from their srt integration (#45389)
  _Files: `.agents/skills/kernel-organization/SKILL.md`, `docker/Dockerfile`, `docker/Dockerfile.cu134`, `docker/rocm.Dockerfile` _+41 more__
- **2026-10-24** [`19212d19b5`](https://github.com/sgl-project/sglang/commit/19212d19b5) [#46045](https://github.com/sgl-project/sglang/pull/46045)
  [Perf] diffusion: Keep shared denoising paths off the host and add host-sync test guards (#46045)
  _Files: `docs/docs/sglang-diffusion/contributing.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py` _+8 more__
- **2026-10-24** [`0b73cc01c0`](https://github.com/sgl-project/sglang/commit/0b73cc01c0) [#46146](https://github.com/sgl-project/sglang/pull/46146)
  [Perf] diffusion: Prefer FA4 over cuDNN SDPA for long self-attention on B300 (#46146)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py`, `python/sglang/multimodal_gen/test/unit/test_dynamic_cudnn_sdpa_selection.py`_
- **2026-10-24** [`f7af00d691`](https://github.com/sgl-project/sglang/commit/f7af00d691) [#46149](https://github.com/sgl-project/sglang/pull/46149)
  [Perf] diffusion: Speed up Wan's spatial-parallel VAE decode (#46149)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wan_vae_cuda_opt.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py`, `python/sglang/multimodal_gen/test/unit/test_vae_loader.py` _+2 more__
- **2026-10-24** [`7d996300b9`](https://github.com/sgl-project/sglang/commit/7d996300b9) [#46230](https://github.com/sgl-project/sglang/pull/46230)
  [Perf] dsv41: Use the fused ratio-2 compressor in the prefill graph (#46230)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-10-24** [`54df642fe6`](https://github.com/sgl-project/sglang/commit/54df642fe6) [#46229](https://github.com/sgl-project/sglang/pull/46229)
  [Perf] dsv41: Translate SWA locations once per prefill graph step (#46229)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/models/deepseek_v4_replay_tail.py`, `test/registered/attention/unittests/dsv4/test_deepseek_v4.py`, `test/registered/unit/layers/test_dsv41_late_layer_tail_readers.py`_
- **2026-10-24** [`564aec61c8`](https://github.com/sgl-project/sglang/commit/564aec61c8) [#46231](https://github.com/sgl-project/sglang/pull/46231)
  [Perf] dsv41: Feed wo_b the fused MXFP8 attention output in the prefill graph (#46231)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_mhc.py`_
- **2026-10-24** [`55f23a8b59`](https://github.com/sgl-project/sglang/commit/55f23a8b59) [#46151](https://github.com/sgl-project/sglang/pull/46151)
  [Fix] [AMD] dsv4.1: Fix decode graph capture with quantized low-ratio activations (#46151)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `test/registered/unit/layers/test_dsv41_late_layer_tail_readers.py`_
- **2026-10-24** [`42ac81c655`](https://github.com/sgl-project/sglang/commit/42ac81c655) [#46107](https://github.com/sgl-project/sglang/pull/46107)
  [Perf] diffusion: Route dense attention with a sub-tile side to FA4 on Blackwell (#46107)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py`, `python/sglang/multimodal_gen/test/unit/test_dynamic_cudnn_sdpa_routing.py`_
- **2026-10-24** [`88ac7c02a6`](https://github.com/sgl-project/sglang/commit/88ac7c02a6) [#45838](https://github.com/sgl-project/sglang/pull/45838)
  [Fix] [AMD] diffusion: Fix the first-step denoise regression from compiling ENABLE_CK=0 BF16 attention (#45838)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py`, `python/sglang/multimodal_gen/test/unit/test_aiter_attention_impl.py`_
- **2026-10-24** [`327c906764`](https://github.com/sgl-project/sglang/commit/327c906764) [#41944](https://github.com/sgl-project/sglang/pull/41944)
  [Perf] [XPU] diffusion: Avoid QKV copies in flash attention (#41944)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/xpu_backend.py`, `test/registered/kernels/ops/diffusion/test_flux2_xpu_norm_fusions.py`_
- **2026-10-24** [`2e6d87e2ca`](https://github.com/sgl-project/sglang/commit/2e6d87e2ca) [#46102](https://github.com/sgl-project/sglang/pull/46102)
  [Perf] diffusion: Serve FA4 head sizes on Blackwell instead of falling back to sm80 SDPA (#46102)
  _Files: `python/sglang/multimodal_gen/runtime/platforms/cuda.py`, `python/sglang/multimodal_gen/test/unit/test_cuda_attention_backend.py`_
- **2026-10-23** [`0931dfedc9`](https://github.com/sgl-project/sglang/commit/0931dfedc9) [#39083](https://github.com/sgl-project/sglang/pull/39083)
  [Fix] [AMD] dsa: Fix AITER prefill with an FP8 KV cache (#39083)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsa_attention.py`_
- **2026-10-23** [`0e34962884`](https://github.com/sgl-project/sglang/commit/0e34962884) [#45966](https://github.com/sgl-project/sglang/pull/45966)
  [Perf] diffusion: Cut LTX-2 denoising-step host overhead (#45966)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_bcg_coords.py` _+1 more__
- **2026-10-23** [`9b46f27090`](https://github.com/sgl-project/sglang/commit/9b46f27090) [#45732](https://github.com/sgl-project/sglang/pull/45732)
  [Fix] [NPU] tests: Restore evalscope GSM8K baseline via NPUGSM8KMixin backend (#45732)
  _Files: `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`, `python/sglang/test/ascend/npu_eval_accuracy_kit.py`, `test/registered/npu/basic_function/dp_attn/test_npu_dp_attention.py`, `test/registered/npu/basic_function/runtime_opts/test_npu_mla_fia_hicache_bf16.py`_
- **2026-10-23** [`02d2445138`](https://github.com/sgl-project/sglang/commit/02d2445138) [#46005](https://github.com/sgl-project/sglang/pull/46005)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches with seven open InferenceX PRs (#46005)
  _Files: `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+4 more__
- **2026-10-23** [`6d6c9cd4ae`](https://github.com/sgl-project/sglang/commit/6d6c9cd4ae) [#44139](https://github.com/sgl-project/sglang/pull/44139)
  [Fix] offloader: Preserve cached weights during CPU offload (#44139)
  _Files: `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/radix_linear_attention.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/utils/offloader.py` _+2 more__
- **2026-10-23** [`6c844eb12e`](https://github.com/sgl-project/sglang/commit/6c844eb12e) [#45941](https://github.com/sgl-project/sglang/pull/45941)
  [Perf] dsv4: Replay the V4.1 prefill graph past 16K contexts on SM90 (#45941)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `test/registered/attention/unittests/dsv4/test_deepseek_v4.py`, `test/registered/unit/layers/test_dsv41_late_layer_tail_readers.py`_
- **2026-10-23** [`904691e0b5`](https://github.com/sgl-project/sglang/commit/904691e0b5) [#45478](https://github.com/sgl-project/sglang/pull/45478)
  [Feat] [CPU] model: Support Cosmos3 series models on CPU (#45478)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/video_sparse_attn.py`_
- **2026-10-23** [`e83f585ae6`](https://github.com/sgl-project/sglang/commit/e83f585ae6) [#45893](https://github.com/sgl-project/sglang/pull/45893)
  [Perf] dsv41: Serve token-interleaved V4.1 KV caches with sgl-flash-mla (#45893)
  _Files: `python/pyproject.toml`, `python/sglang/kernels/jit/csrc/deepseek_v4/c1.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/c2.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/flashmla_sched_meta.cuh` _+32 more__
- **2026-10-23** [`698651acd0`](https://github.com/sgl-project/sglang/commit/698651acd0) [#45700](https://github.com/sgl-project/sglang/pull/45700)
  [Feat] HiCache: Support fused DFLASH KV in unified hybrid SWA pools (#45700)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/kv_cache_dtype.py` _+3 more__
- **2026-10-23** [`a4838160b3`](https://github.com/sgl-project/sglang/commit/a4838160b3) [#45934](https://github.com/sgl-project/sglang/pull/45934)
  [Perf] dsv4: Write V4.1 K rows with one warp per token in the fused k-norm-rope store (#45934)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh`, `test/registered/kernels/ops/attention/dsv4/test_v41_kv_store.py`_
- **2026-10-23** [`c4fa35b829`](https://github.com/sgl-project/sglang/commit/c4fa35b829) [#45938](https://github.com/sgl-project/sglang/pull/45938)
  [Perf] dsv4: Map V4.1 prefill index selections to pool slots in one kernel (#45938)
  _Files: `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/scoring.py`_
- **2026-10-23** [`5daa1352ba`](https://github.com/sgl-project/sglang/commit/5daa1352ba) [#42567](https://github.com/sgl-project/sglang/pull/42567)
  [CI] tests: Retire test/srt and reject legacy test paths (#42567)
  _Files: `.pre-commit-config.yaml`, `test/README.md`, `test/registered/attention/test_aiter_cross_layer_kv_guard.py`, `test/registered/attention/test_aiter_swa_kv_pool_resolver.py` _+1 more__
- **2026-10-23** [`26396bf566`](https://github.com/sgl-project/sglang/commit/26396bf566) [#45407](https://github.com/sgl-project/sglang/pull/45407)
  [Fix] [NVIDIA] deepseek-v4.1: Fix the breakable prefill CUDA graph in the late-layer tail on SM90 (#45407)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/layers/test_dsv41_late_layer_tail_readers.py`_
- **2026-10-23** [`97b79f0796`](https://github.com/sgl-project/sglang/commit/97b79f0796) [#45881](https://github.com/sgl-project/sglang/pull/45881)
  [Fix] prefill-graph: Keep every DP rank eager when the replay tail captures behind rank barriers (#45881)
  _Files: `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/models/deepseek_v4_replay_tail.py`, `python/sglang/srt/runtime_context.py`_
- **2026-10-23** [`9c7dd3c45f`](https://github.com/sgl-project/sglang/commit/9c7dd3c45f) [#45909](https://github.com/sgl-project/sglang/pull/45909)
  [Perf] dsv4: Dequantize each shared sparse-prefill KV source once per forward (#45909)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `test/manual/test_dsv41_ragged_prefill.py` _+3 more__
- **2026-10-22** [`9c0f6d6a61`](https://github.com/sgl-project/sglang/commit/9c0f6d6a61) [#45901](https://github.com/sgl-project/sglang/pull/45901)
  [Perf] dsv4: Write the MegaAttention output straight into the prefill graph buffer (#45901)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-22** [`840a6313c9`](https://github.com/sgl-project/sglang/commit/840a6313c9) [#45880](https://github.com/sgl-project/sglang/pull/45880)
  [Perf] dsv4: Score the V4.1 index logits in bf16 on SM100 (#45880)
  _Files: `python/sglang/kernels/ops/attention/dsv4/index_logits.py`, `python/sglang/srt/environ.py`, `test/registered/kernels/ops/attention/test_dense_prefill_indexer.py`, `test/registered/kernels/ops/attention/test_dsv41_prefill_sparse_indexer.py`_
- **2026-10-22** [`154e29c1ec`](https://github.com/sgl-project/sglang/commit/154e29c1ec) [#43792](https://github.com/sgl-project/sglang/pull/43792)
  [Perf] CP: QSA Context Parallel Optimization (#43792)
  _Files: `python/sglang/srt/layers/attention/qsa/metadata.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/layers/attention/qsa/sparse_attn.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` _+2 more__
- **2026-10-22** [`0d6b283d7e`](https://github.com/sgl-project/sglang/commit/0d6b283d7e) [#45783](https://github.com/sgl-project/sglang/pull/45783)
  [Refactor] dsv4: Keep only the two-level V4.1 indexer in the prefill graph (#45783)
  _Files: `python/sglang/kernels/ops/attention/dsv4/topk.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py` _+5 more__
- **2026-10-22** [`c80285ca9a`](https://github.com/sgl-project/sglang/commit/c80285ca9a) [#43809](https://github.com/sgl-project/sglang/pull/43809)
  [Fix] [AMD] deterministic: Refuse RCCL all-reduce in deterministic mode above TP2 (#43809)
  _Files: `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-10-22** [`cc811ff0c3`](https://github.com/sgl-project/sglang/commit/cc811ff0c3) [#44280](https://github.com/sgl-project/sglang/pull/44280)
  [Feat] KVShard: Add attention and indexer support for page-sharded DSA caches (#44280)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_metadata.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/mem_cache/page_interleave_pool.py` _+2 more__
- **2026-10-22** [`a9902f47e3`](https://github.com/sgl-project/sglang/commit/a9902f47e3) [#41564](https://github.com/sgl-project/sglang/pull/41564)
  [Fix] [NPU] qwen: adapt pcp-v2 (#41564)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `test/manual/ascend/test_npu_prefill_cp_backend.py`_
- **2026-10-22** [`0a87f163dc`](https://github.com/sgl-project/sglang/commit/0a87f163dc) [#45507](https://github.com/sgl-project/sglang/pull/45507)
  [Test] [AMD] deepseek-v4.1: Fix the HIP breakable-graph unit tests for the default prefill context limit and the DSpark draft ring (#45507)
  _Files: `test/registered/amd/test_dsv4_hip_bcg_metadata.py`, `test/registered/attention/unittests/dsv4/test_dsv41_bcg_hip.py`_
- **2026-10-22** [`779adb4b82`](https://github.com/sgl-project/sglang/commit/779adb4b82) [#45565](https://github.com/sgl-project/sglang/pull/45565)
  [Perf] cuda-graph: Raise MLA prefill capture default to chunked size capped at 8192 (#45565)
  _Files: `python/sglang/srt/arg_groups/memory_hook.py`_
- **2026-10-22** [`82f7249ce6`](https://github.com/sgl-project/sglang/commit/82f7249ce6) [#45741](https://github.com/sgl-project/sglang/pull/45741)
  [Perf] dsv4: Gather V4.1 index-K slots once per prefill graph replay (#45741)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/types.py`_
- **2026-10-22** [`a56024c267`](https://github.com/sgl-project/sglang/commit/a56024c267) [#45651](https://github.com/sgl-project/sglang/pull/45651)
  [CI] flash-mla: Add the sgl-flash-mla release workflow (#45651)
  _Files: `.github/workflows/release-whl-flashmla.yml`, `docker/sgl-flash-mla.Dockerfile`, `scripts/build_sgl_flash_mla.sh`, `scripts/rename_sgl_flash_mla_whl.sh` _+1 more__
- **2026-10-22** [`12370da115`](https://github.com/sgl-project/sglang/commit/12370da115) [#45749](https://github.com/sgl-project/sglang/pull/45749)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches with five open InferenceX PRs (#45749)
  _Files: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx` _+3 more__
- **2026-10-22** [`d9ce511646`](https://github.com/sgl-project/sglang/commit/d9ce511646) [#45530](https://github.com/sgl-project/sglang/pull/45530)
  [Feat] diffusion: support FastH3 Omni (Ref2VA 8-step PDD) (#45530)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/configs/sample/minimax_h3.py`, `python/sglang/multimodal_gen/registry.py` _+10 more__
- **2026-10-22** [`17babd67b4`](https://github.com/sgl-project/sglang/commit/17babd67b4) [#45699](https://github.com/sgl-project/sglang/pull/45699)
  [Fix] dsv4: Never read attention metadata for idle SWA stores (#45699)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-10-22** [`b057d5b3f1`](https://github.com/sgl-project/sglang/commit/b057d5b3f1) [#42976](https://github.com/sgl-project/sglang/pull/42976)
  [Fix] [NPU] mla-pool: DCP allocator page and index-K bound, short-pool warning (#42976)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/mem_cache/allocation.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` _+3 more__
- **2026-10-22** [`3d508d614f`](https://github.com/sgl-project/sglang/commit/3d508d614f) [#45294](https://github.com/sgl-project/sglang/pull/45294)
  [CI] [NVIDIA] gb300: Run DSV4.1-Flash tests on 2 GPUs with engram host tables (#45294)
  _Files: `.github/workflows/pr-test.yml`, `python/sglang/test/dsv41_flash_common.py`, `scripts/ci/runner_configs.yml`, `test/registered/e2e/models/test_deepseek_v41_flash_gb300_dp2ep2.py` _+4 more__
- **2026-10-22** [`59149553b9`](https://github.com/sgl-project/sglang/commit/59149553b9) [#45684](https://github.com/sgl-project/sglang/pull/45684)
  [Refactor] attention: centralize linear and draft TP group selection (#45684)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/model_runner_components/spec_aux_hidden_state.py`, `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/runtime_context.py` _+4 more__
- **2026-10-21** [`da7b97a737`](https://github.com/sgl-project/sglang/commit/da7b97a737) [#45582](https://github.com/sgl-project/sglang/pull/45582)
  [Perf] dsv4: Publish prefill read-done under the request window and on V4.1 (#45582)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `test/registered/attention/unittests/dsv4/test_deepseek_v4.py`_
- **2026-10-21** [`f4035cab0b`](https://github.com/sgl-project/sglang/commit/f4035cab0b) [#43182](https://github.com/sgl-project/sglang/pull/43182)
  [Feat] cp: Enable GLM-5.3 Flash interleave BCG with batched prefill and DFlash2 (#43182)
  _Files: `python/sglang/kernels/ops/attention/dsa/cp_split.py`, `python/sglang/srt/arg_groups/cp_tp_group_sharing_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py` _+14 more__
- **2026-10-21** [`991b846227`](https://github.com/sgl-project/sglang/commit/991b846227) [#42803](https://github.com/sgl-project/sglang/pull/42803)
  [Perf] speculative: Parallelize EAGLE spec-decode KV index building over token blocks (flashinfer draft decode; verify/draft-extend for flashinfer, flashinfer_mla, aiter) (#42803)
  _Files: `python/sglang/kernels/ops/attention/kv_indices.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/mem_cache/kv_index_translator.py` _+4 more__
- **2026-10-21** [`99cf403c9e`](https://github.com/sgl-project/sglang/commit/99cf403c9e) [#45586](https://github.com/sgl-project/sglang/pull/45586)
  [Fix] dsv4: Write idle SWA stores to an idle request-window layout (#45586)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/mem_cache/dsv41_request_window.py`_
- **2026-10-21** [`29e78045fb`](https://github.com/sgl-project/sglang/commit/29e78045fb) [#40424](https://github.com/sgl-project/sglang/pull/40424)
  [Fix] dsv4: Skip DP-attention pad rows in the engram hasher and low-ratio sources (#40424)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/engram.py`_
- **2026-10-21** [`f7d4f06242`](https://github.com/sgl-project/sglang/commit/f7d4f06242) [#45579](https://github.com/sgl-project/sglang/pull/45579)
  [Perf] dsv4: Compute request-window history rows once per batch (#45579)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/mem_cache/dsv41_request_window.py`, `test/registered/kernels/ops/attention/test_q8kv8_sparse_prefill_backend.py` _+3 more__
- **2026-10-21** [`bc412213c1`](https://github.com/sgl-project/sglang/commit/bc412213c1) [#45577](https://github.com/sgl-project/sglang/pull/45577)
  [Perf] dsv4: Gather V4.1 index-K slots once per forward and cache the prefill index plan (#45577)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/__init__.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/dense_blocks.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/full_topk.py` _+3 more__
- **2026-10-21** [`97945831f9`](https://github.com/sgl-project/sglang/commit/97945831f9) [#45573](https://github.com/sgl-project/sglang/pull/45573)
  [Perf] dsv4: Restore sparse prefill for request-window rows (#45573)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-10-21** [`f06d1bb1f4`](https://github.com/sgl-project/sglang/commit/f06d1bb1f4) [#45473](https://github.com/sgl-project/sglang/pull/45473)
  [Perf] cuda-graph: Capture FlashInfer KDA prefill  (#45473)
  _Files: `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kda_flashinfer_prefill_graph.py`, `python/sglang/srt/layers/attention/linear/kda_prefill_graph.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashinfer_prefill.py` _+1 more__
- **2026-10-21** [`7163e97462`](https://github.com/sgl-project/sglang/commit/7163e97462) [#45597](https://github.com/sgl-project/sglang/pull/45597)
  [Doc] [NPU] GLM: Add Ascend cookbook deployment recipes (#45597)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/glm_5_3_flash.mdx` _+3 more__
- **2026-10-21** [`6efdd33d07`](https://github.com/sgl-project/sglang/commit/6efdd33d07) [#45504](https://github.com/sgl-project/sglang/pull/45504)
  [Refactor] spec: Move platform dispatch and Triton kernels into `kernels/ops` (#45504)
  _Files: `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/table_qk_norm_rope.py`, `python/sglang/kernels/ops/sampling/renorm.py`, `python/sglang/kernels/ops/speculative/__init__.py` _+22 more__
- **2026-10-21** [`f7b8c6fe40`](https://github.com/sgl-project/sglang/commit/f7b8c6fe40) [#45349](https://github.com/sgl-project/sglang/pull/45349)
  [Fix] glm-5.2: Record side-stream work right before its join to keep CUDA-graph replay on one stream (#45349)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`_
- **2026-10-21** [`4449d7ecb0`](https://github.com/sgl-project/sglang/commit/4449d7ecb0) [#43372](https://github.com/sgl-project/sglang/pull/43372)
  [Doc] [NPU] GLM: Add GLM-5.3 and GLM-5.3-Flash deployment tutorials (#43372)
  _Files: `docs/docs.json`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/glm_5_3.mdx`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/glm_5_3_flash.mdx`_
- **2026-10-21** [`1689cb2d52`](https://github.com/sgl-project/sglang/commit/1689cb2d52) [#45513](https://github.com/sgl-project/sglang/pull/45513)
  [Doc] cookbook: Add GLM-5.3 AgentX section and refresh with eight open InferenceX PRs (#45513)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+4 more__
- **2026-10-21** [`4b5c9c4b5e`](https://github.com/sgl-project/sglang/commit/4b5c9c4b5e) [#45099](https://github.com/sgl-project/sglang/pull/45099)
  [Perf] [AMD] attention: Restore the gfx950 extend tile for head_dim <= 128 (#45099)
  _Files: `python/sglang/kernels/ops/attention/extend_attention.py`_
- **2026-10-21** [`eb91a41f38`](https://github.com/sgl-project/sglang/commit/eb91a41f38) [#44977](https://github.com/sgl-project/sglang/pull/44977)
  [Feat] unified_cache: Support FULL + MAMBA MLA models (Kimi-K3) in the direct external linker (#44977)
  _Files: `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py` _+3 more__
- **2026-10-21** [`c0d18c0254`](https://github.com/sgl-project/sglang/commit/c0d18c0254) [#40399](https://github.com/sgl-project/sglang/pull/40399)
  [Fix] [NPU] dspark: Fix attn_tp > 1 draft wo_b all_reduce group (#40399)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-10-21** [`c1c287a429`](https://github.com/sgl-project/sglang/commit/c1c287a429) [#45326](https://github.com/sgl-project/sglang/pull/45326)
  [Doc] cookbook: add TPU7x recipe for GLM-5.3-Flash (#45326)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-10-20** [`bf145750a6`](https://github.com/sgl-project/sglang/commit/bf145750a6) [#37958](https://github.com/sgl-project/sglang/pull/37958)
  [Perf] prefill-cuda-graph: Make prefill shared-read completion explicit and default-on (#37958)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dots_hybrid_backend.py` _+11 more__
- **2026-10-20** [`d5e83ea4f6`](https://github.com/sgl-project/sglang/commit/d5e83ea4f6) [#45098](https://github.com/sgl-project/sglang/pull/45098)
  [Perf] [AMD] deterministic: Faster extend attention launch on gfx950 (#45098)
  _Files: `python/sglang/kernels/ops/attention/extend_attention.py`, `test/registered/attention/test_triton_attention_kernels.py`_
- **2026-10-20** [`82ac83a8d0`](https://github.com/sgl-project/sglang/commit/82ac83a8d0) [#45339](https://github.com/sgl-project/sglang/pull/45339)
  [Perf] [AMD] dsv41: Skip unneeded layer 20 computation under decoder-bounded-replay (#45339)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_platform_stage.py`_
- **2026-10-20** [`7656071309`](https://github.com/sgl-project/sglang/commit/7656071309) [#43826](https://github.com/sgl-project/sglang/pull/43826)
  [Feat] platform: Add initial T-HEAD SAIL platform support [2/N] (#43826)
  _Files: `.github/workflows/pr-test-ppu.yml`, `docs/docs.json`, `docs/docs/hardware-platforms/sail.mdx`, `python/pyproject_other.toml` _+29 more__
- **2026-10-20** [`e262b44eef`](https://github.com/sgl-project/sglang/commit/e262b44eef) [#43063](https://github.com/sgl-project/sglang/pull/43063)
  [CI] [NPU] tests: Replace DeepSeek-V2-Lite-W8A8 cases with Moonlight (#43063)
  _Files: `test/registered/npu/basic_function/HiCache/test_npu_hicache_mla.py`, `test/registered/npu/basic_function/dp_attn/test_npu_dp_attention.py`, `test/registered/npu/basic_function/runtime_opts/test_npu_mla_fia_hicache_bf16.py`, `test/registered/npu/basic_function/runtime_opts/test_npu_mla_fia_w8a8int8.py` _+1 more__
- **2026-10-20** [`10d5293546`](https://github.com/sgl-project/sglang/commit/10d5293546) [#43469](https://github.com/sgl-project/sglang/pull/43469)
  [Perf] [NPU] glm5.2: Support dynamic INT8 MLAProlog for attention (#43469)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `test/registered/unit/attention/test_npu_mlaprolog.py`_
- **2026-10-20** [`aa91108f64`](https://github.com/sgl-project/sglang/commit/aa91108f64) [#40165](https://github.com/sgl-project/sglang/pull/40165)
  [Fix] [NPU] glm5.2: support pcp v2 with interleave & zigzag (#40165)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/attention/dsa/dsa_npu_indexer.py`, `python/sglang/srt/models/deepseek_v2.py`_
- **2026-10-20** [`ee2f95a522`](https://github.com/sgl-project/sglang/commit/ee2f95a522) [#41642](https://github.com/sgl-project/sglang/pull/41642)
  [Fix] [NPU] glm5.2-mtp: L2 cache adaptation (#41642)
  _Files: `python/sglang/srt/mem_cache/pool_host/mla.py`_
- **2026-10-20** [`07eb671b6a`](https://github.com/sgl-project/sglang/commit/07eb671b6a) [#38461](https://github.com/sgl-project/sglang/pull/38461)
  [Perf] [NPU] attn: add not needs_cpu_seq_lens for dsa modules (#38461)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`, `test/manual/ascend/llm_models/test_npu_glm_5_1_w4a8_draft_prefetch.py`_
- **2026-10-20** [`ca473ef3e4`](https://github.com/sgl-project/sglang/commit/ca473ef3e4) [#45154](https://github.com/sgl-project/sglang/pull/45154)
  [Feat] glm-5.3: Render GLM-5.3 and GLM-5.3-Flash chat prompts with a Python chat template (#45154)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/parser/glm53_chat_template.py`, `python/sglang/srt/parser/python_chat_template.py`, `python/sglang/srt/parser/template_detection.py` _+4 more__
- **2026-10-20** [`306ccf6f57`](https://github.com/sgl-project/sglang/commit/306ccf6f57) [#40762](https://github.com/sgl-project/sglang/pull/40762)
  [Perf] spec: Let the FlashAttention backend capture the draft-extend CUDA graph (#40762)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-10-20** [`0788f1fdd0`](https://github.com/sgl-project/sglang/commit/0788f1fdd0) [#45277](https://github.com/sgl-project/sglang/pull/45277)
  [Refactor] kernels: Register agent-generated kernels under their KDA / Cake backend (#45277)
  _Files: `python/sglang/kernels/README.md`, `python/sglang/kernels/fused_op.py`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/diffusion/__init__.py` _+3 more__
- **2026-10-20** [`9e23107772`](https://github.com/sgl-project/sglang/commit/9e23107772) [#45311](https://github.com/sgl-project/sglang/pull/45311)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches with five open InferenceX PRs (#45311)
  _Files: `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx` _+2 more__
- **2026-10-20** [`472f0d540b`](https://github.com/sgl-project/sglang/commit/472f0d540b) [#45301](https://github.com/sgl-project/sglang/pull/45301)
  [Fix] deepseek-v4.1: Keep the padded query buffer inside decoder tail graphs (#45301)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-20** [`476fe86a12`](https://github.com/sgl-project/sglang/commit/476fe86a12) [#45251](https://github.com/sgl-project/sglang/pull/45251)
  [Perf] deepseek-v4.1: Score a request's verify rows as one request in the full-scan indexer (#45251)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/full_topk.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/scoring.py` _+2 more__
- **2026-10-20** [`35c873cff4`](https://github.com/sgl-project/sglang/commit/35c873cff4) [#45319](https://github.com/sgl-project/sglang/pull/45319)
  [Fix] observability: Log scheduler stats once per attention CP group (#45319)
  _Files: `python/sglang/srt/observability/metrics_collector.py`_
- **2026-10-20** [`602c92ccd8`](https://github.com/sgl-project/sglang/commit/602c92ccd8) [#44632](https://github.com/sgl-project/sglang/pull/44632)
  [Perf] DeepSeek-V4.1: Raise the SM100 swap-AB decode cap to 40 rows (#44632)
  _Files: `python/sglang/kernels/ops/attention/dsv4/decode_attention_sm100.py`, `test/registered/kernels/ops/attention/dsv4/test_swapab_attention.py`_
- **2026-10-20** [`d1c3346f74`](https://github.com/sgl-project/sglang/commit/d1c3346f74) [#45033](https://github.com/sgl-project/sglang/pull/45033)
  [Fix] [Intel] spec: Fix XPU nightly dflash stop_regex and DSpark capture check (#45033)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py`, `test/registered/e2e/xpu/test_dspark_intel_xpu.py`, `test/registered/unit/managers/test_stop_str_speculative.py`_
- **2026-10-20** [`72d886efb8`](https://github.com/sgl-project/sglang/commit/72d886efb8) [#43838](https://github.com/sgl-project/sglang/pull/43838)
  [Perf] DeepSeek-V4.1: Run the small-batch decode fusions at TP2 (#43838)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/wo_a_fused.cuh`, `python/sglang/kernels/ops/attention/dsv4/decode_attention_sm100.py`, `python/sglang/kernels/ops/attention/dsv4/decode_attention_sm100_gluon.py`, `python/sglang/kernels/ops/attention/dsv4/wo_a.py` _+5 more__
- **2026-10-20** [`5b683d6b72`](https://github.com/sgl-project/sglang/commit/5b683d6b72) [#45218](https://github.com/sgl-project/sglang/pull/45218)
  [Fix] test: Add logical_forward_mode to the KDA prefill-graph stand-in batch (#45218)
  _Files: `test/registered/kernels/ops/attention/test_kda_prefill_graph.py`_
- **2026-10-20** [`e3205080ce`](https://github.com/sgl-project/sglang/commit/e3205080ce) [#42087](https://github.com/sgl-project/sglang/pull/42087)
  [Fix] qwen3.8: Fix batch-invariant kernels for Qwen3.8 Flash-Next (#42087)
  _Files: `python/sglang/kernels/ops/elementwise/elementwise.py`, `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/layers/attention/qsa/kernel.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py` _+3 more__
- **2026-10-20** [`1140a8dfd9`](https://github.com/sgl-project/sglang/commit/1140a8dfd9) [#43335](https://github.com/sgl-project/sglang/pull/43335)
  [Fix] [AMD] aiter: Fix garbage decode output for non-sliding-window models on the vectorized_5d KV layout (#43335)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/amd/test_aiter_vectorized_5d_decode.py`_
- **2026-10-20** [`8683f8ad4a`](https://github.com/sgl-project/sglang/commit/8683f8ad4a) [#32503](https://github.com/sgl-project/sglang/pull/32503)
  [Feat] [Intel] hicache: Enable L1<->L2 support on XPU (#32503)
  _Files: `python/sglang/srt/mem_cache/l2_transfer.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/pool_host/_kvcacheio.py`, `python/sglang/srt/mem_cache/pool_host/common.py` _+13 more__
- **2026-10-20** [`5e630fa571`](https://github.com/sgl-project/sglang/commit/5e630fa571) [#45275](https://github.com/sgl-project/sglang/pull/45275)
  [Perf] deepseek-v4.1: Drop host syncs from encoder-replay folding and tail metadata (#45275)
  _Files: `python/sglang/kernels/ops/attention/dsv4/attn_metadata_kernels.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/model_executor/encoder_swa_replay.py`, `test/registered/unit/model_executor/test_encoder_swa_replay.py`_
- **2026-10-20** [`1897575ce1`](https://github.com/sgl-project/sglang/commit/1897575ce1) [#44514](https://github.com/sgl-project/sglang/pull/44514)
  [Fix] runtime: Version FlashInfer caches for default-tactic tuning. (#44514)
  _Files: `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`_
- **2026-10-19** [`28448a86d4`](https://github.com/sgl-project/sglang/commit/28448a86d4) [#45245](https://github.com/sgl-project/sglang/pull/45245)
  [Doc] cookbook: Default Qwen3.8-Flash-Next datacenter recipes to FP8 KV cache and QSA indexer (#45245)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-flash-next.jsx`_
- **2026-10-19** [`05d7f7a166`](https://github.com/sgl-project/sglang/commit/05d7f7a166) [#33007](https://github.com/sgl-project/sglang/pull/33007)
  [Fix] attention: Honor selected FlashAttention implementation (#33007)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`_
- **2026-10-19** [`49766a74f9`](https://github.com/sgl-project/sglang/commit/49766a74f9) [#43438](https://github.com/sgl-project/sglang/pull/43438)
  [Fix] attn_residual: int64 program ids in the score/combine kernels (int32 overflow at 37,451 tokens) (#43438)
  _Files: `python/sglang/kernels/ops/attention/attn_res_hip.py`, `python/sglang/srt/layers/attn_residual.py`, `test/registered/kernels/ops/attention/test_attn_res_mix_large_tokens.py`_
- **2026-10-19** [`7656ea0e74`](https://github.com/sgl-project/sglang/commit/7656ea0e74) [#44393](https://github.com/sgl-project/sglang/pull/44393)
  [CI] python: Move the remaining CUDA build paths off Python 3.10 (#44393)
  _Files: `.github/workflows/_pr-test-sgl-kernel-build.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/bot-bump-docs-version.yml`, `.github/workflows/bot-bump-flashinfer-version.yml` _+31 more__
- **2026-10-19** [`aaa9388c91`](https://github.com/sgl-project/sglang/commit/aaa9388c91) [#45018](https://github.com/sgl-project/sglang/pull/45018)
  [Fix] kda: Keep FlashInfer prefill off its grouped kernel's bf16/flat-dt_bias contract (#45018)
  _Files: `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashinfer_prefill.py`, `test/registered/unit/layers/attention/linear/kernels/test_kda_flashinfer_prefill.py`_
- **2026-10-19** [`f1a2ee763d`](https://github.com/sgl-project/sglang/commit/f1a2ee763d) [#45107](https://github.com/sgl-project/sglang/pull/45107)
  [Perf] deepseek-v4.1: Run decoder replay tail graphs in prefill-graph steps and under DP attention (#45107)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/model_executor/runner/row_bucket_graph_runner.py`, `python/sglang/srt/models/deepseek_v4.py` _+1 more__
- **2026-10-19** [`5ed306bd69`](https://github.com/sgl-project/sglang/commit/5ed306bd69) [#44671](https://github.com/sgl-project/sglang/pull/44671)
  [Fix] [AMD] diffusion: Keep gfx1250 FlyDSL BF16 attention out of torch.compile (#44671)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py`, `python/sglang/multimodal_gen/runtime/platforms/aiter.py`, `python/sglang/multimodal_gen/test/unit/test_aiter_attention_impl.py`_
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

## Multimodal  (123 commits)

- **2026-10-26** [`fe4ccb37e4`](https://github.com/sgl-project/sglang/commit/fe4ccb37e4) [#46060](https://github.com/sgl-project/sglang/pull/46060)
  [Fix] diffusion/api: Publish image inputs atomically (#46060)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/utils.py`, `python/sglang/multimodal_gen/runtime/utils/image_io.py`, `python/sglang/multimodal_gen/test/unit/test_openai_security.py`_
- **2026-10-26** [`ce77d5e93d`](https://github.com/sgl-project/sglang/commit/ce77d5e93d) [#46057](https://github.com/sgl-project/sglang/pull/46057)
  [Fix] diffusion/server: Clean up rejected and cancelled video requests (#46057)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/test/unit/test_prompt_enhancement.py`, `python/sglang/multimodal_gen/test/unit/test_video_job_lifecycle.py`_
- **2026-10-26** [`042dc54cbf`](https://github.com/sgl-project/sglang/commit/042dc54cbf) [#46249](https://github.com/sgl-project/sglang/pull/46249)
  [Fix] diffusion: Route realtime cleanup to the session owner (#46249)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/control_requests.py`, `python/sglang/multimodal_gen/runtime/scheduler_client.py`, `python/sglang/multimodal_gen/test/unit/test_dp_routing.py`, `python/sglang/multimodal_gen/test/unit/test_scheduler_client.py`_
- **2026-10-26** [`bd03d33f6b`](https://github.com/sgl-project/sglang/commit/bd03d33f6b) [#46254](https://github.com/sgl-project/sglang/pull/46254)
  [Test] diffusion: Make restoration tests independent of execution order (#46254)
  _Files: `python/sglang/multimodal_gen/test/unit/test_plain_state_dict_loaders.py`, `python/sglang/multimodal_gen/test/unit/test_text_encoder_loader.py`_
- **2026-10-26** [`af21e2b989`](https://github.com/sgl-project/sglang/commit/af21e2b989) [#46393](https://github.com/sgl-project/sglang/pull/46393)
  [Fix] [Intel] diffusion/wan: Guard the CuTe DSL q/k norm RoPE imports on XPU (#46393)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`_
- **2026-10-26** [`c4e335f84e`](https://github.com/sgl-project/sglang/commit/c4e335f84e) [#46174](https://github.com/sgl-project/sglang/pull/46174)
  [Perf] diffusion: Build spatial-parallel causal conv inputs in one pass (#46174)
  _Files: `python/sglang/multimodal_gen/runtime/layers/parallel_conv.py`, `python/sglang/multimodal_gen/test/unit/test_vae_spatial_parallel_decode.py`_
- **2026-10-26** [`d72664d903`](https://github.com/sgl-project/sglang/commit/d72664d903) [#46240](https://github.com/sgl-project/sglang/pull/46240)
  [Perf] diffusion: Blend VAE tile seams in one pass (#46240)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/common.py`, `python/sglang/multimodal_gen/test/unit/test_vae_tiled_decode_groups.py`_
- **2026-10-26** [`60d941293e`](https://github.com/sgl-project/sglang/commit/60d941293e) [#46493](https://github.com/sgl-project/sglang/pull/46493)
  [Perf] diffusion/worker: Move cyclic GC out of request execution (#46493)
  _Files: `docs/docs/sglang-diffusion/performance-optimization.mdx`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/request_gc.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py` _+4 more__
- **2026-10-26** [`bc809a3622`](https://github.com/sgl-project/sglang/commit/bc809a3622) [#45919](https://github.com/sgl-project/sglang/pull/45919)
  [Feat] diffusion/openai: Report per-step progress for async video jobs (#45919)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_progress.py` _+11 more__
- **2026-10-25** [`c05fb1bd04`](https://github.com/sgl-project/sglang/commit/c05fb1bd04) [#46154](https://github.com/sgl-project/sglang/pull/46154)
  [Fix] diffusion/serving: Reclaim abandoned shared-memory replies (#46154)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/ipc_array.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/runtime/scheduler_client.py` _+2 more__
- **2026-10-25** [`97220dd674`](https://github.com/sgl-project/sglang/commit/97220dd674) [#46173](https://github.com/sgl-project/sglang/pull/46173)
  [Perf] diffusion: Run Cosmos3's multi-GPU VAE decode on the lossless fast path (#46173)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`, `python/sglang/multimodal_gen/test/unit/test_cosmos3.py`, `python/sglang/multimodal_gen/test/unit/test_vae_loader.py`_
- **2026-10-25** [`bea6a21c36`](https://github.com/sgl-project/sglang/commit/bea6a21c36) [#46124](https://github.com/sgl-project/sglang/pull/46124)
  [Feat] diffusion/model: support Hy-Nomas (#46124)
  _Files: `docs/cookbook/diffusion/HY-Nomas/HY-Nomas.mdx`, `docs/docs.json`, `docs/src/snippets/configs/HY-Nomas/hy-nomas.jsx`, `python/sglang/multimodal_gen/configs/models/dits/nomas.py` _+23 more__
- **2026-10-25** [`933853a3f2`](https://github.com/sgl-project/sglang/commit/933853a3f2) [#45733](https://github.com/sgl-project/sglang/pull/45733)
  [Perf] diffusion/preprocess: generalize exact GPU input processing optimization across pipelines (#45733)
  _Files: `docs/docs/sglang-diffusion/performance-optimization.mdx`, `python/sglang/kernels/ops/mm/process/lanczos.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/flux.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image.py` _+8 more__
- **2026-10-25** [`a887ac8fc6`](https://github.com/sgl-project/sglang/commit/a887ac8fc6) [#46111](https://github.com/sgl-project/sglang/pull/46111)
  [Perf] diffusion: Vectorize the LTX-2 Q/K RMSNorm + split-RoPE kernel (#46111)
  _Files: `python/sglang/kernels/kda_kernels/csrc/diffusion/ltx2_qknorm_split_rope.cuh`, `test/registered/kernels/ops/diffusion/test_rope_ltx2.py`_
- **2026-10-25** [`90396623bd`](https://github.com/sgl-project/sglang/commit/90396623bd) [#44020](https://github.com/sgl-project/sglang/pull/44020)
  [Fix] chat-template: Pass return_dict=False to apply_chat_template(tokenize=True) for transformers 5 (#44020)
  _Files: `python/sglang/benchmark/datasets/speed_bench.py`, `python/sglang/srt/entrypoints/ollama/serving.py`, `python/sglang/srt/entrypoints/openai/chat_encoding.py`, `python/sglang/srt/multimodal/processors/voxtral.py` _+1 more__
- **2026-10-25** [`17204f3482`](https://github.com/sgl-project/sglang/commit/17204f3482) [#46044](https://github.com/sgl-project/sglang/pull/46044)
  [Fix] diffusion/zimage: Stop serving a previous request's RoPE tables (#46044)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/zimage.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/test_server_common.py`, `python/sglang/multimodal_gen/test/server/testcase_configs.py` _+3 more__
- **2026-10-25** [`8ef5dec95f`](https://github.com/sgl-project/sglang/commit/8ef5dec95f) [#46047](https://github.com/sgl-project/sglang/pull/46047)
  [Perf] diffusion: Remove per-step host syncs and uploads in video models (#46047)
  _Files: `python/sglang/multimodal_gen/runtime/models/bridges/mova_dual_tower.py`, `python/sglang/multimodal_gen/runtime/models/dits/causal_wanvideo.py`, `python/sglang/multimodal_gen/runtime/models/dits/cosmos3_sim_auto.py`, `python/sglang/multimodal_gen/runtime/models/dits/cosmos_dreams.py` _+27 more__
- **2026-10-25** [`9c0fa18106`](https://github.com/sgl-project/sglang/commit/9c0fa18106) [#46156](https://github.com/sgl-project/sglang/pull/46156)
  [Fix] diffusion/openai: Bound job lists and complete cursor pagination (#46156)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/mesh_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/stores.py` _+2 more__
- **2026-10-25** [`7ba699b3c8`](https://github.com/sgl-project/sglang/commit/7ba699b3c8) [#46264](https://github.com/sgl-project/sglang/pull/46264)
  [Refactor] diffusion: Share segmented row-parallel weight loading (#46264)
  _Files: `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/runtime/layers/linear.py`, `python/sglang/multimodal_gen/runtime/loader/rank_local_checkpoint.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux.py` _+6 more__
- **2026-10-24** [`773cb938fe`](https://github.com/sgl-project/sglang/commit/773cb938fe) [#46294](https://github.com/sgl-project/sglang/pull/46294)
  [Fix] diffusion: Complete Blackwell routing test fixture (#46294)
  _Files: `python/sglang/multimodal_gen/test/unit/test_dynamic_cudnn_sdpa_routing.py`_
- **2026-10-24** [`059ba6b666`](https://github.com/sgl-project/sglang/commit/059ba6b666) [#46136](https://github.com/sgl-project/sglang/pull/46136)
  [Chore] docker: Select released wheels and the torch index in the cu134 image (#46136)
  _Files: `docker/Dockerfile.cu134`_
- **2026-10-24** [`625399c7d2`](https://github.com/sgl-project/sglang/commit/625399c7d2) [#46250](https://github.com/sgl-project/sglang/pull/46250)
  [Fix] diffusion/realtime: Keep frame payloads contiguous (#46250)
  _Files: `docs/cookbook/diffusion/SANA-WM/SANA-WM.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/generate_session.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/realtime_video_api.py`, `python/sglang/multimodal_gen/test/unit/realtime/test_realtime_runtime.py`_
- **2026-10-24** [`93d70b3802`](https://github.com/sgl-project/sglang/commit/93d70b3802) [#46171](https://github.com/sgl-project/sglang/pull/46171)
  [Perf] diffusion: Gather spatial-parallel decode heights on the host (#46171)
  _Files: `python/sglang/multimodal_gen/runtime/layers/parallel_conv.py`, `python/sglang/multimodal_gen/test/unit/test_ltx_vae_parallel_decode.py`, `python/sglang/multimodal_gen/test/unit/test_vae_spatial_parallel_decode.py`_
- **2026-10-24** [`6df9015b4f`](https://github.com/sgl-project/sglang/commit/6df9015b4f) [#46228](https://github.com/sgl-project/sglang/pull/46228)
  [Perf] diffusion: Fuse Wan's q/k RMSNorm with its interleaved RoPE (#46228)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/rmsnorm_interleaved_rope_cutedsl.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`, `test/registered/kernels/ops/diffusion/test_rmsnorm_interleaved_rope.py`_
- **2026-10-24** [`8bf88667fd`](https://github.com/sgl-project/sglang/commit/8bf88667fd) [#46221](https://github.com/sgl-project/sglang/pull/46221)
  [Perf] diffusion: Stop the idle loop from starving async-save replies (#46221)
  _Files: `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/test/unit/test_async_output_save.py`_
- **2026-10-24** [`a9b23e98c7`](https://github.com/sgl-project/sglang/commit/a9b23e98c7) [#46253](https://github.com/sgl-project/sglang/pull/46253)
  [Fix] diffusion/loader: Honor custom weight-loader overrides (#46253)
  _Files: `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/test/unit/test_fsdp_load.py`_
- **2026-10-24** [`638374c389`](https://github.com/sgl-project/sglang/commit/638374c389) [#46157](https://github.com/sgl-project/sglang/pull/46157)
  [Fix] diffusion/scheduler: Isolate invalid IPC requests (#46157)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/test/unit/test_scheduler_client.py`_
- **2026-10-24** [`5ac018b251`](https://github.com/sgl-project/sglang/commit/5ac018b251) [#46172](https://github.com/sgl-project/sglang/pull/46172)
  [Perf] diffusion: Encode Cosmos3 video while it decodes (#46172)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/unit/test_cosmos3.py`_
- **2026-10-24** [`af7d941fc3`](https://github.com/sgl-project/sglang/commit/af7d941fc3) [#46239](https://github.com/sgl-project/sglang/pull/46239)
  [Perf] diffusion: Validate breakable CUDA graphs for LTX-2.5 two-stage serving (#46239)
  _Files: `docs/cookbook/diffusion/LTX/LTX2.5.mdx`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-10-24** [`31b352b8ea`](https://github.com/sgl-project/sglang/commit/31b352b8ea) [#46235](https://github.com/sgl-project/sglang/pull/46235)
  [Fix] diffusion: Preserve metrics collectives after output save errors (#46235)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/test/unit/test_perf_dump_write.py`, `test/registered/e2e/diffusion/test_async_video_serving.py`_
- **2026-10-24** [`d30134818c`](https://github.com/sgl-project/sglang/commit/d30134818c) [#46237](https://github.com/sgl-project/sglang/pull/46237)
  [Perf] diffusion: Split LTX tiled VAE decode across the decode-parallel ranks (#46237)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/ltx_2_vae.py`, `python/sglang/multimodal_gen/test/unit/test_ltx_vae_parallel_decode.py`, `python/sglang/multimodal_gen/test/unit/test_vae_spatial_parallel_decode.py`_
- **2026-10-24** [`1d0f90bf2b`](https://github.com/sgl-project/sglang/commit/1d0f90bf2b) [#46241](https://github.com/sgl-project/sglang/pull/46241)
  [Perf] diffusion/loader: Avoid temporary GPU tensors when loading encoders (#46241)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/test/unit/test_text_encoder_loader.py`_
- **2026-10-24** [`0498ab7b6e`](https://github.com/sgl-project/sglang/commit/0498ab7b6e) [#45179](https://github.com/sgl-project/sglang/pull/45179)
  [Perf] diffusion/minimax-h3: Batch the video VAE decoder tiles and fuse the output chain (#45179)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/jit/csrc/diffusion/minimax_h3_vae_output.cuh`, `python/sglang/kernels/ops/diffusion/README.md` _+20 more__
- **2026-10-24** [`31fdc0f0cf`](https://github.com/sgl-project/sglang/commit/31fdc0f0cf) [#46147](https://github.com/sgl-project/sglang/pull/46147)
  [Perf] diffusion: Tile the 3D scale-shift Triton kernel by rows (#46147)
  _Files: `python/sglang/kernels/ops/diffusion/modulate/scale_shift_triton.py`, `test/registered/kernels/ops/diffusion/test_modulate.py`_
- **2026-10-24** [`6f0ac70cf1`](https://github.com/sgl-project/sglang/commit/6f0ac70cf1) [#46162](https://github.com/sgl-project/sglang/pull/46162)
  [Fix] diffusion/api: Do not publish failed generation outputs (#46162)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/utils.py`, `python/sglang/multimodal_gen/test/unit/test_image_response_bytes.py`, `python/sglang/multimodal_gen/test/unit/test_openai_utils.py` _+1 more__
- **2026-10-24** [`a1d4f386dd`](https://github.com/sgl-project/sglang/commit/a1d4f386dd) [#46142](https://github.com/sgl-project/sglang/pull/46142)
  [Fix] diffusion/server: Clean up workers on startup failure (#46142)
  _Files: `python/sglang/multimodal_gen/runtime/launch_server.py`, `python/sglang/multimodal_gen/test/unit/test_launch_server_shutdown.py`, `python/sglang/multimodal_gen/test/unit/test_load_inclusive_e2e.py`_
- **2026-10-24** [`4b4ae831bb`](https://github.com/sgl-project/sglang/commit/4b4ae831bb) [#46206](https://github.com/sgl-project/sglang/pull/46206)
  [Feat] rust-server: Let a multimodal processor check and fetch media during admission (#46206)
  _Files: `rust/sglang-server/src/api_server/core/handle.rs`, `rust/sglang-server/src/api_server/core/prefetch.rs`, `rust/sglang-server/src/lib.rs`, `rust/sglang-server/src/multi_modality/payload.rs` _+2 more__
- **2026-10-24** [`f09cec65e9`](https://github.com/sgl-project/sglang/commit/f09cec65e9) [#46068](https://github.com/sgl-project/sglang/pull/46068)
  [Fix] diffusion/storage: Join uploads before request cleanup (#46068)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/storage.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py` _+1 more__
- **2026-10-24** [`f4ecaae888`](https://github.com/sgl-project/sglang/commit/f4ecaae888) [#46081](https://github.com/sgl-project/sglang/pull/46081)
  [Fix] diffusion/mesh: Guard asynchronous job publication and defaults (#46081)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/mesh_api.py`, `python/sglang/multimodal_gen/test/unit/test_openai_security.py`_
- **2026-10-24** [`cdab6c1bcc`](https://github.com/sgl-project/sglang/commit/cdab6c1bcc) [#46095](https://github.com/sgl-project/sglang/pull/46095)
  [Fix] diffusion/loader: Preserve checkpoints on read failures (#46095)
  _Files: `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `python/sglang/multimodal_gen/runtime/loader/rank_local_checkpoint.py`, `python/sglang/multimodal_gen/runtime/loader/weight_utils.py`, `python/sglang/multimodal_gen/test/unit/test_weight_utils.py`_
- **2026-10-24** [`f2c634961b`](https://github.com/sgl-project/sglang/commit/f2c634961b) [#46105](https://github.com/sgl-project/sglang/pull/46105)
  [Perf] diffusion: Project LTX-2 prompt K/V once per denoising loop (#46105)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_bcg_coords.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_prompt_kv_cache.py`_
- **2026-10-24** [`7cefa60765`](https://github.com/sgl-project/sglang/commit/7cefa60765) [#46007](https://github.com/sgl-project/sglang/pull/46007)
  [Perf] diffusion: Wait on the socket when the scheduler is idle (#46007)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py` _+1 more__
- **2026-10-24** [`25ba24e9a7`](https://github.com/sgl-project/sglang/commit/25ba24e9a7) [#46109](https://github.com/sgl-project/sglang/pull/46109)
  [Perf] diffusion: Build one LTX-2.3 AdaLN row per sample when every token shares the sigma (#46109)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_ltx23_per_sample_adaln.py`_
- **2026-10-24** [`5bef70c0a2`](https://github.com/sgl-project/sglang/commit/5bef70c0a2) [#41943](https://github.com/sgl-project/sglang/pull/41943)
  [Perf] flux2: Build the single-block output projection without a cat (#41943)
  _Files: `python/sglang/kernels/ops/diffusion/activation/silu_mul_bitexact.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py`, `test/registered/kernels/ops/diffusion/test_flux2_xpu_norm_fusions.py`_
- **2026-10-24** [`1d4dcc81cc`](https://github.com/sgl-project/sglang/commit/1d4dcc81cc) [#46043](https://github.com/sgl-project/sglang/pull/46043)
  [Perf] diffusion/registry: Reduce model discovery work at startup (#46043)
  _Files: `python/sglang/multimodal_gen/runtime/models/registry.py`, `python/sglang/multimodal_gen/test/unit/test_registry.py`_
- **2026-10-24** [`47c0791ad1`](https://github.com/sgl-project/sglang/commit/47c0791ad1) [#46099](https://github.com/sgl-project/sglang/pull/46099)
  [Perf] diffusion: Write uncompressed PNG responses without Pillow's row filters (#46099)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/test/unit/test_image_response_bytes.py`, `python/sglang/multimodal_gen/test/unit/test_output_saving.py`_
- **2026-10-24** [`bbc77e7db4`](https://github.com/sgl-project/sglang/commit/bbc77e7db4) [#46110](https://github.com/sgl-project/sglang/pull/46110)
  [Perf] diffusion: Cut LTX-2.3 per-block elementwise work (contiguous AdaLN values, gate-folded masks, vectorized head gate) (#46110)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/modulate/head_gate_triton.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_ada_values_layout.py` _+1 more__
- **2026-10-24** [`4e2d5b17ad`](https://github.com/sgl-project/sglang/commit/4e2d5b17ad) [#45978](https://github.com/sgl-project/sglang/pull/45978)
  [Perf] diffusion: Keep every component resident in auto mode when memory allows (#45978)
  _Files: `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py`, `python/sglang/multimodal_gen/runtime/loader/utils.py`, `python/sglang/multimodal_gen/runtime/server_args/auto_tune.py` _+6 more__
- **2026-10-24** [`be8600d02d`](https://github.com/sgl-project/sglang/commit/be8600d02d) [#45993](https://github.com/sgl-project/sglang/pull/45993)
  [Fix] diffusion: Step MOVA latents outside the serial-CFG branch (#45993)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/mova.py`, `python/sglang/multimodal_gen/test/unit/test_mova_denoising_loop.py`_
- **2026-10-24** [`a08bb0ec9e`](https://github.com/sgl-project/sglang/commit/a08bb0ec9e) [#46108](https://github.com/sgl-project/sglang/pull/46108)
  [Perf] diffusion: Run LTX-2 stage 2 on a premerged resident DiT (#46108)
  _Files: `docs/cookbook/diffusion/LTX/LTX2 & LTX2.3.mdx`, `python/sglang/multimodal_gen/runtime/pipelines/ltx_2_pipeline.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_premerged_stage2.py` _+1 more__
- **2026-10-24** [`e66c9e981d`](https://github.com/sgl-project/sglang/commit/e66c9e981d) [#45977](https://github.com/sgl-project/sglang/pull/45977)
  [Perf] diffusion: Turn on breakable CUDA graphs by default for LTX-2/LTX-2.3 two-stage serving (#45977)
  _Files: `docs/cookbook/diffusion/LTX/LTX2 & LTX2.3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/ltx_2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/model_deployment_config.py` _+8 more__
- **2026-10-24** [`386fa9ecfd`](https://github.com/sgl-project/sglang/commit/386fa9ecfd) [#46106](https://github.com/sgl-project/sglang/pull/46106)
  [Perf] diffusion: Drop LTX-2's all-valid prompt mask under lossless quality (#46106)
  _Files: `python/sglang/multimodal_gen/runtime/models/adapter/ltx_2_connector.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/text_connector.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_prompt_mask_registers.py`_
- **2026-10-24** [`5b8955e70f`](https://github.com/sgl-project/sglang/commit/5b8955e70f) [#45965](https://github.com/sgl-project/sglang/pull/45965)
  [Perf] diffusion: Shard LTX-2 stage 2 over the CFG ranks as Ulysses (#45965)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/group_coordinator.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/executors/parallel_executor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/base.py` _+2 more__
- **2026-10-24** [`738e4535ea`](https://github.com/sgl-project/sglang/commit/738e4535ea) [#46101](https://github.com/sgl-project/sglang/pull/46101)
  [Perf] diffusion/qwen-image-2.1: Keep an image prefix's K/V in the packed buffer across steps (#46101)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/qwen_image21.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21_cuda.py`_
- **2026-10-24** [`3712b5944d`](https://github.com/sgl-project/sglang/commit/3712b5944d) [#46148](https://github.com/sgl-project/sglang/pull/46148)
  [Perf] diffusion: Patchify Wan latents straight into tokens (#46148)
  _Files: `python/sglang/multimodal_gen/runtime/layers/visual_embedding.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`, `python/sglang/multimodal_gen/test/unit/test_patch_embed_tokens.py`_
- **2026-10-24** [`2d5ad3243f`](https://github.com/sgl-project/sglang/commit/2d5ad3243f) [#46169](https://github.com/sgl-project/sglang/pull/46169)
  [Fix] diffusion/http: Allow bounded graceful shutdown (#46169)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/launch_server.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_launch_server_shutdown.py` _+1 more__
- **2026-10-23** [`4542fc8f59`](https://github.com/sgl-project/sglang/commit/4542fc8f59) [#45656](https://github.com/sgl-project/sglang/pull/45656)
  [Fix] mistral3: Subclass LlavaForConditionalGeneration instead of wrapping it (#45656)
  _Files: `python/sglang/srt/models/llava.py`, `python/sglang/srt/models/mistral.py`, `test/registered/unit/models/test_mistral3_vision_feature.py`_
- **2026-10-23** [`194abb8e54`](https://github.com/sgl-project/sglang/commit/194abb8e54) [#45983](https://github.com/sgl-project/sglang/pull/45983)
  [CI] [AMD] diffusion: Drain the Cosmos Dreams decode stream after freeing its outputs (#45983)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3_simulation/dreams.py`_
- **2026-10-23** [`1d605b7ece`](https://github.com/sgl-project/sglang/commit/1d605b7ece) [#45461](https://github.com/sgl-project/sglang/pull/45461)
  [CI] vlm: Harden fixture cleanup after setup and shutdown failures (#45461)
  _Files: `test/registered/vlm/test_vlm_input_format.py`_
- **2026-10-23** [`74c08f3dc5`](https://github.com/sgl-project/sglang/commit/74c08f3dc5) [#45914](https://github.com/sgl-project/sglang/pull/45914)
  [Feat] rust-server: Let a multimodal processor finalize item layout after caller hashes (#45914)
  _Files: `rust/sglang-server/src/multi_modality/worker.rs`_
- **2026-10-23** [`efd2ce8a9d`](https://github.com/sgl-project/sglang/commit/efd2ce8a9d) [#43673](https://github.com/sgl-project/sglang/pull/43673)
  [Feat] comfyui: video-to-video input and prompt enhancement for server-mode nodes (#43673)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/README.md`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/server_api.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/nodes.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/test/test_h3_request.py` _+3 more__
- **2026-10-23** [`02b983603d`](https://github.com/sgl-project/sglang/commit/02b983603d) [#45943](https://github.com/sgl-project/sglang/pull/45943)
  [Fix] diffusion: Keep dynamic LoRA deltas on fused linear-GELU sites (#45943)
  _Files: `python/sglang/kernels/ops/diffusion/sites/fused_linear_gelu_site.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/server/test_server_common.py` _+2 more__
- **2026-10-23** [`82ff16dad0`](https://github.com/sgl-project/sglang/commit/82ff16dad0) [#45979](https://github.com/sgl-project/sglang/pull/45979)
  [Perf] diffusion: Skip the residency calibration probe in auto mode until a planner consumes it (#45979)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/server_args/auto_tune.py`, `python/sglang/multimodal_gen/test/unit/test_auto_residency.py`_
- **2026-10-23** [`3e5f5505ed`](https://github.com/sgl-project/sglang/commit/3e5f5505ed) [#45987](https://github.com/sgl-project/sglang/pull/45987)
  [Perf] diffusion: Serve image responses from in-memory encoded bytes (#45987)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `docs/docs/sglang-diffusion/performance-optimization.mdx`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py` _+10 more__
- **2026-10-23** [`2fbd094a8c`](https://github.com/sgl-project/sglang/commit/2fbd094a8c) [#45995](https://github.com/sgl-project/sglang/pull/45995)
  [Fix] diffusion: Offset LTX-2.3 BCG video RoPE by the SP shard start (#45995)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_bcg_coords.py`_
- **2026-10-23** [`4b1941e889`](https://github.com/sgl-project/sglang/commit/4b1941e889) [#46040](https://github.com/sgl-project/sglang/pull/46040)
  [CI] diffusion: Run the FLUX.2 XPU norm-fusion test on the XPU suite only (#46040)
  _Files: `test/registered/kernels/ops/diffusion/test_flux2_xpu_norm_fusions.py`_
- **2026-10-23** [`535aeae2a7`](https://github.com/sgl-project/sglang/commit/535aeae2a7) [#46014](https://github.com/sgl-project/sglang/pull/46014)
  [CI] [NPU] precise-test: run only the recommended multimodal_gen cases (#46014)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-10-23** [`494eeecb6c`](https://github.com/sgl-project/sglang/commit/494eeecb6c) [#45944](https://github.com/sgl-project/sglang/pull/45944)
  [Fix] diffusion: Keep the linear-GELU verdict cache out of torch.compile traces (#45944)
  _Files: `python/sglang/kernels/ops/diffusion/sites/fused_linear_gelu_site.py`, `test/registered/kernels/ops/diffusion/test_sites.py`_
- **2026-10-23** [`f9129915a3`](https://github.com/sgl-project/sglang/commit/f9129915a3) [#45994](https://github.com/sgl-project/sglang/pull/45994)
  [Fix] diffusion: Give every SP rank the same Wan TI2V timestep (#45994)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/wan_ti2v.py`, `python/sglang/multimodal_gen/test/unit/test_wan_ti2v_helpers.py`_
- **2026-10-23** [`7d1a16d3eb`](https://github.com/sgl-project/sglang/commit/7d1a16d3eb) [#45861](https://github.com/sgl-project/sglang/pull/45861)
  [CI] [AMD] diffusion: Skip the LTX-2.5 diffusion decoder case on the 2-GPU lane (#45861)
  _Files: `.github/workflows/pr-test-amd.yml`_
- **2026-10-23** [`2b8e4cde95`](https://github.com/sgl-project/sglang/commit/2b8e4cde95) [#40092](https://github.com/sgl-project/sglang/pull/40092)
  [Doc] [CPU] Cookbook: Update to the cookbook for models supported by Intel Xeon CPUs (#40092)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-OCR.mdx`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-R1.mdx`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_1.mdx` _+39 more__
- **2026-10-23** [`4b273537de`](https://github.com/sgl-project/sglang/commit/4b273537de) [#44887](https://github.com/sgl-project/sglang/pull/44887)
  [Fix] diffusion: runtime utils bug fixes (#44887)
  _Files: `python/sglang/multimodal_gen/runtime/utils/common.py`, `python/sglang/multimodal_gen/runtime/utils/hf_diffusers_utils.py`, `python/sglang/multimodal_gen/runtime/utils/image_io.py`, `python/sglang/multimodal_gen/runtime/utils/logging_utils.py` _+12 more__
- **2026-10-23** [`472208fec0`](https://github.com/sgl-project/sglang/commit/472208fec0) [#45955](https://github.com/sgl-project/sglang/pull/45955)
  [CI] [NPU] precise-test: recommend multimodal_gen cases at test-case granularity (#45955)
  _Files: `.github/workflows/pr-test-npu.yml`, `scripts/ci/npu/precise-test/bucket_recommended_tests.py`, `scripts/ci/npu/precise-test/test_selector.py`_
- **2026-10-23** [`6f466f655a`](https://github.com/sgl-project/sglang/commit/6f466f655a) [#41942](https://github.com/sgl-project/sglang/pull/41942)
  [Perf] [XPU] diffusion/flux2: Fuse bit-exact LayerNorm and gated residual norm (#41942)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/layernorm_modulate_xpu_triton.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py`, `python/sglang/srt/environ.py` _+1 more__
- **2026-10-23** [`8708d2ee99`](https://github.com/sgl-project/sglang/commit/8708d2ee99) [#45942](https://github.com/sgl-project/sglang/pull/45942)
  [Fix] diffusion/ltx: Keep tiled VAE decode off the sharded convs under parallel decode (#45942)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/runtime/models/vaes/ltx_2_vae.py`, `python/sglang/multimodal_gen/test/unit/test_ltx_vae_parallel_decode.py`_
- **2026-10-23** [`4f47c48b33`](https://github.com/sgl-project/sglang/commit/4f47c48b33) [#45948](https://github.com/sgl-project/sglang/pull/45948)
  [Fix] diffusion: Keep the N-rank IPC all-to-all's flags and staging out of expandable segments (#45948)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a_multi.py`, `python/sglang/multimodal_gen/test/single_test_file/test_ipc_a2a_multi_gpu.py`, `python/sglang/multimodal_gen/test/unit/test_ipc_a2a_lifecycle.py`_
- **2026-10-23** [`1cd0ebb3d3`](https://github.com/sgl-project/sglang/commit/1cd0ebb3d3) [#45967](https://github.com/sgl-project/sglang/pull/45967)
  [Perf] diffusion: Remove per-step and per-request host syncs in Cosmos3 and Qwen-Image-2.1 (#45967)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/qwen_image21.py`, `python/sglang/multimodal_gen/test/unit/test_cosmos3_rollout.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py`_
- **2026-10-23** [`4da6f585f3`](https://github.com/sgl-project/sglang/commit/4da6f585f3) [#43585](https://github.com/sgl-project/sglang/pull/43585)
  [Fix] diffusion: OpenAI API hardening (#43585)
  _Files: `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/utils.py`, `python/sglang/multimodal_gen/runtime/postprocess/bounded_cache.py` _+5 more__
- **2026-10-23** [`6dd0dfabf0`](https://github.com/sgl-project/sglang/commit/6dd0dfabf0) [#45854](https://github.com/sgl-project/sglang/pull/45854)
  [CI] [Intel] docker/xpu: Tag nightly images with main-whl and main-main kernel variant (#45854)
  _Files: `.github/workflows/release-docker-intel-xpu-nightly.yml`_
- **2026-10-23** [`76c382e80f`](https://github.com/sgl-project/sglang/commit/76c382e80f) [#41401](https://github.com/sgl-project/sglang/pull/41401)
  [Perf] [XPU] diffusion: Use the AOT SYCL fused residual-norm-scale-shift kernel (#41401)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/scale_residual_norm_scale_shift_sycl.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`_
- **2026-10-23** [`7c680a0d45`](https://github.com/sgl-project/sglang/commit/7c680a0d45) [#45398](https://github.com/sgl-project/sglang/pull/45398)
  [Perf] diffusion/cosmos3: optimize v2v preprocess performance (#45398)
  _Files: `python/sglang/kernels/ops/mm/__init__.py`, `python/sglang/kernels/ops/mm/process/__init__.py`, `python/sglang/kernels/ops/mm/process/lanczos.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py` _+3 more__
- **2026-10-23** [`7baacd1d1b`](https://github.com/sgl-project/sglang/commit/7baacd1d1b) [#45882](https://github.com/sgl-project/sglang/pull/45882)
  [CI] [AMD] docker: Add a build-only dispatch option to the ROCm nightly image workflows (#45882)
  _Files: `.github/workflows/release-docker-amd-gfx1151-nightly.yml`, `.github/workflows/release-docker-amd-rocm10.yml`, `.github/workflows/release-docker-amd-rocm720-nightly.yml`_
- **2026-10-23** [`f4a2df3dac`](https://github.com/sgl-project/sglang/commit/f4a2df3dac) [#45831](https://github.com/sgl-project/sglang/pull/45831)
  [CI] diffusion: Calibrate single-GPU shard scheduling from CI (#45831)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`_
- **2026-10-23** [`fa628c5359`](https://github.com/sgl-project/sglang/commit/fa628c5359) [#43536](https://github.com/sgl-project/sglang/pull/43536)
  [Fix] comfyui: Fix GGUF detection, import guard and VRAM accounting in SGLDiffusion plugin (#43536)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/__init__.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/minimax_h3.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/nodes.py` _+6 more__
- **2026-10-23** [`ae4258715c`](https://github.com/sgl-project/sglang/commit/ae4258715c) [#45904](https://github.com/sgl-project/sglang/pull/45904)
  [Perf] dsv4: Keep V4.1 image rows inside the Engram gate kernel (#45904)
  _Files: `python/sglang/kernels/ops/embeddings/engram_gate.py`, `python/sglang/srt/layers/engram.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/models/test_deepseek_v41_bcg_multimodal.py`_
- **2026-10-22** [`e5db41b329`](https://github.com/sgl-project/sglang/commit/e5db41b329) [#44581](https://github.com/sgl-project/sglang/pull/44581)
  [Fix] nemotron_vl: Pad visual spans using processor offsets (#44581)
  _Files: `python/sglang/srt/models/nano_nemotron_vl.py`, `test/registered/unit/models/test_nano_nemotron_vl.py`, `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`_
- **2026-10-22** [`afd0d7b47b`](https://github.com/sgl-project/sglang/commit/afd0d7b47b) [#44260](https://github.com/sgl-project/sglang/pull/44260)
  [Fix] diffusion/flux: use true_cfg_scale as the FLUX CFG weight (#44260)
  _Files: `docs/cookbook/diffusion/FLUX/FLUX.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/flux.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/test/unit/test_flux_true_cfg_scale.py`_
- **2026-10-22** [`0f7d3a0451`](https://github.com/sgl-project/sglang/commit/0f7d3a0451) [#45761](https://github.com/sgl-project/sglang/pull/45761)
  [CI] diffusion: target thirty-minute CI shards (#45761)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `scripts/ci/utils/diffusion/compute_diffusion_partitions.py`, `scripts/ci/utils/diffusion/test_compute_diffusion_partitions.py`_
- **2026-10-22** [`d0a7565436`](https://github.com/sgl-project/sglang/commit/d0a7565436) [#45778](https://github.com/sgl-project/sglang/pull/45778)
  [Fix] diffusion: Drop stale mismatch_msg from FLUX 3 video VAE gate call (#45778)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/flux3_video_vae.py`_
- **2026-10-22** [`3f6c313389`](https://github.com/sgl-project/sglang/commit/3f6c313389) [#45775](https://github.com/sgl-project/sglang/pull/45775)
  [Fix] diffusion: Restore the kernel registry import after #41894 (#45775)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/flux3_video_qknorm_rope_triton.py`_
- **2026-10-22** [`5c2cb60790`](https://github.com/sgl-project/sglang/commit/5c2cb60790) [#45725](https://github.com/sgl-project/sglang/pull/45725)
  [Fix] [Intel] diffusion: Restore copy offload for FLUX.2-dev nightly (#45725)
  _Files: `test/registered/xpu/test_xpu_flux2_dev.py`_
- **2026-10-22** [`24e45961c6`](https://github.com/sgl-project/sglang/commit/24e45961c6) [#41894](https://github.com/sgl-project/sglang/pull/41894)
  [Perf] diffusion: fuse QKV norm + RoPE, cached RoPE tables for FLUX 3 video VAE (#41894)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/flux3_video_qknorm_rope_triton.py`, `python/sglang/multimodal_gen/runtime/models/vaes/flux3_video_vae.py` _+1 more__
- **2026-10-22** [`c64886f9e3`](https://github.com/sgl-project/sglang/commit/c64886f9e3) [#32860](https://github.com/sgl-project/sglang/pull/32860)
  [Perf] diffusion: fuse Wan VAE DupUp3D shortcut add (#32860)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py`, `python/sglang/multimodal_gen/test/unit/test_wan_vae_dupup.py`_
- **2026-10-22** [`f727076ed0`](https://github.com/sgl-project/sglang/commit/f727076ed0) [#44085](https://github.com/sgl-project/sglang/pull/44085)
  [Feat] diffusion: support wan-animate-2 distilled model (#44085)
  _Files: `docs/cookbook/diffusion/Wan/Wan-Animate-2.mdx`, `docs/scripts/tests/wan-animate-2-config.test.mjs`, `docs/src/snippets/configs/Wan/wan-animate-2.jsx`, `docs/src/snippets/diffusion/model-catalog.jsx` _+14 more__
- **2026-10-22** [`33a0734ca1`](https://github.com/sgl-project/sglang/commit/33a0734ca1) [#45553](https://github.com/sgl-project/sglang/pull/45553)
  [CI] [NPU] precise-test: collect multimodal_gen coverage per test case (#45553)
  _Files: `.github/workflows/coverage-collection-npu.yml`, `.github/workflows/pr-test-npu.yml`, `python/sglang/multimodal_gen/test/server/ascend/test_glm_image_distributed.py`, `scripts/ci/npu/precise-test/list_multimodal_tests.py` _+1 more__
- **2026-10-22** [`ce66b3ab59`](https://github.com/sgl-project/sglang/commit/ce66b3ab59) [#45413](https://github.com/sgl-project/sglang/pull/45413)
  [Feat] systemone: serve Kev pointer head decision models (#45413)
  _Files: `docs/cookbook/autoregressive/Kev/kev.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json`, `docs/docs/supported-models/decision_models.mdx` _+16 more__
- **2026-10-22** [`45de4adde9`](https://github.com/sgl-project/sglang/commit/45de4adde9) [#44841](https://github.com/sgl-project/sglang/pull/44841)
  [Feat] diffusion: Add worker-side ComfyUI compatibility patches (#44841)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/options.py`, `python/sglang/multimodal_gen/apps/comfyui_worker_patches/__init__.py`, `python/sglang/multimodal_gen/apps/comfyui_worker_patches/h3.py` _+1 more__
- **2026-10-22** [`780a5b1acc`](https://github.com/sgl-project/sglang/commit/780a5b1acc) [#45705](https://github.com/sgl-project/sglang/pull/45705)
  [Doc] diffusion: document prompt enhancer tasks and link Cosmos recipes (#45705)
  _Files: `docs/docs/sglang-diffusion/models_with_pe.mdx`, `docs/src/snippets/diffusion/model-catalog.jsx`_
- **2026-10-22** [`b453996b7d`](https://github.com/sgl-project/sglang/commit/b453996b7d) [#45267](https://github.com/sgl-project/sglang/pull/45267)
  [Doc] diffusion/minimax-h3: Refresh VDN-H3 B200 benchmarks, fix 8-step bench presets and popular-models snippet (#45267)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/.agents/skills/sglang-diffusion-benchmark-profile/scripts/bench_diffusion_denoise.py`_
- **2026-10-21** [`4b1a44bc77`](https://github.com/sgl-project/sglang/commit/4b1a44bc77) [#45409](https://github.com/sgl-project/sglang/pull/45409)
  [Test] [AMD] diffusion: Avoid Python 3.11-only enterContext in test_usp_ring_replicated (#45409)
  _Files: `python/sglang/multimodal_gen/test/unit/test_usp_ring_replicated.py`_
- **2026-10-21** [`cdbd478422`](https://github.com/sgl-project/sglang/commit/cdbd478422) [#40120](https://github.com/sgl-project/sglang/pull/40120)
  [Doc] [NPU] cookbook: add tested A2 deployment and A3 reference for MiniMax-M2.5 (#40120)
  _Files: `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.5.mdx`, `docs/scripts/tests/diffusion-builders.test.mjs`, `docs/scripts/tests/minimax-m25-deployment.test.mjs`, `docs/src/snippets/autoregressive/minimax-m25-deployment.jsx`_
- **2026-10-21** [`62b4127668`](https://github.com/sgl-project/sglang/commit/62b4127668) [#43698](https://github.com/sgl-project/sglang/pull/43698)
  [Feat] comfyui: Apply ControlNet residuals in Flux integrated mode (#43698)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/README.md`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/adapter.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/base.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/flux.py` _+7 more__
- **2026-10-21** [`21f775cd97`](https://github.com/sgl-project/sglang/commit/21f775cd97) [#45431](https://github.com/sgl-project/sglang/pull/45431)
  [Feat] rust-server: Let the launcher set the default max_new_tokens for /generate (#45431)
  _Files: `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/rust_server/server.py`, `rust/sglang-server/src/api_server/http/native_api.rs`, `rust/sglang-server/src/message/config.rs` _+3 more__
- **2026-10-21** [`dbe0a9a7c9`](https://github.com/sgl-project/sglang/commit/dbe0a9a7c9) [#44184](https://github.com/sgl-project/sglang/pull/44184)
  [Fix] nemotron_vl: Preserve tokenized prompts during media expansion (#44184)
  _Files: `python/sglang/srt/multimodal/processors/nano_nemotron_vl.py`, `test/registered/unit/multimodal/test_nano_nemotron_vl_processor.py`_
- **2026-10-21** [`6cac4dc3fe`](https://github.com/sgl-project/sglang/commit/6cac4dc3fe) [#44603](https://github.com/sgl-project/sglang/pull/44603)
  [Refactor] diffusion: Rollout controller as a scheduler-step plugin instead of mixins (#44603)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/models/schedulers/scheduling_flow_match_euler_discrete.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/schedule_batch.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py` _+10 more__
- **2026-10-21** [`6bd1c76735`](https://github.com/sgl-project/sglang/commit/6bd1c76735) [#45432](https://github.com/sgl-project/sglang/pull/45432)
  [Fix] rust-server: Drop the fixed 64-item multimodal cap in favor of --limit-mm-data-per-request (#45432)
  _Files: `python/sglang/srt/rust_server/config.py`, `rust/sglang-mm/README.md`, `rust/sglang-mm/src/driver.rs`, `rust/sglang-server/src/api_server/core/handle.rs` _+3 more__
- **2026-10-20** [`7b1d5cd02d`](https://github.com/sgl-project/sglang/commit/7b1d5cd02d) [#43666](https://github.com/sgl-project/sglang/pull/43666)
  [Doc] agent-skills: Fix stale paths and deleted guard tests in skills and rules (#43666)
  _Files: `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/clean-startup-log/references/noise-sources.md`, `.agents/skills/cookbook-review-pr/SKILL.md`, `.agents/skills/llm-torch-profiler-analysis/references/source-map.md` _+4 more__
- **2026-10-20** [`d69966f9c0`](https://github.com/sgl-project/sglang/commit/d69966f9c0) [#45253](https://github.com/sgl-project/sglang/pull/45253)
  [Chore] docker: Add Beam CUDA image (1/8) (#45253)
  _Files: `docker/beam/beam.Dockerfile`_
- **2026-10-20** [`f82465718b`](https://github.com/sgl-project/sglang/commit/f82465718b) [#44596](https://github.com/sgl-project/sglang/pull/44596)
  [Test] [AMD] diffusion: Skip MOSS-Image mismatched-operand test on ROCm (#44596)
  _Files: `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-10-20** [`36978d6c4d`](https://github.com/sgl-project/sglang/commit/36978d6c4d) [#44421](https://github.com/sgl-project/sglang/pull/44421)
  [Test] [AMD] diffusion: Skip the Kandinsky6 FA dispatch test on ROCm (#44421)
  _Files: `python/sglang/multimodal_gen/test/unit/test_kandinsky6_bf16_dtype.py`_
- **2026-10-20** [`50fa3727eb`](https://github.com/sgl-project/sglang/commit/50fa3727eb) [#45297](https://github.com/sgl-project/sglang/pull/45297)
  [Doc] [AMD] cookbook: Fix DeepSeek-V4 PD image and c1 capacity (#45297)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-10-20** [`71ee2dc950`](https://github.com/sgl-project/sglang/commit/71ee2dc950) [#40899](https://github.com/sgl-project/sglang/pull/40899)
  [Fix] inkling: Return 400 instead of 500 for unfetchable/undecodable multimodal input (#40899)
  _Files: `python/sglang/srt/multimodal/inkling/feature_extraction.py`, `python/sglang/srt/multimodal/inkling/image_processing.py`, `python/sglang/srt/multimodal/inkling/image_processing_rust.py`, `python/sglang/srt/multimodal/processors/inkling.py` _+1 more__
- **2026-10-19** [`81ac15391c`](https://github.com/sgl-project/sglang/commit/81ac15391c) [#44663](https://github.com/sgl-project/sglang/pull/44663)
  [Fix] metrics: record HTTP request metrics in tokenizer workers (#44663)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/observability/http_request_metrics.py`, `python/sglang/srt/utils/common.py` _+1 more__
- **2026-10-19** [`80b86dbecb`](https://github.com/sgl-project/sglang/commit/80b86dbecb) [#44672](https://github.com/sgl-project/sglang/pull/44672)
  [Fix] [AMD] diffusion: Accept residual and skip_bias in the ROCm Conv3d-to-Conv2d VAE patch (#44672)
  _Files: `python/sglang/multimodal_gen/runtime/platforms/rocm.py`, `python/sglang/multimodal_gen/test/unit/test_rocm_conv3d_patch.py`_
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

## MoE / Expert Parallel  (64 commits)

- **2026-10-26** [`316ff4dce2`](https://github.com/sgl-project/sglang/commit/316ff4dce2) [#45143](https://github.com/sgl-project/sglang/pull/45143)
  [Perf] function_call: stop rescanning unclosed GLM tool calls per chunk (#45143)
  _Files: `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `test/registered/unit/function_call/test_function_call_parser.py`_
- **2026-10-26** [`ef11eb3b76`](https://github.com/sgl-project/sglang/commit/ef11eb3b76) [#33250](https://github.com/sgl-project/sglang/pull/33250)
  [Fix] deepseek-v4: Fix DeepSeek-V4 non-EP TBO for attention TP > 1 (#33250)
  _Files: `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_common/moe_transport.py`, `python/sglang/srt/models/deepseek_v2.py` _+10 more__
- **2026-10-26** [`144bcdfe34`](https://github.com/sgl-project/sglang/commit/144bcdfe34) [#43341](https://github.com/sgl-project/sglang/pull/43341)
  [Feat] [CPU] Grok-model: enable grok-2 model on xeon cpu (#43341)
  _Files: `python/sglang/kernels/aot/csrc/cpu/norm.cpp`, `python/sglang/kernels/aot/csrc/cpu/topk.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` _+4 more__
- **2026-10-26** [`0cd2a63b36`](https://github.com/sgl-project/sglang/commit/0cd2a63b36) [#41899](https://github.com/sgl-project/sglang/pull/41899)
  [Perf] [AMD] quark/Qwen3.8: Quantize the BF16 shared expert of Quark MXFP4 checkpoints to MXFP4 while loading for shared-expert fusion (#41899)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` _+5 more__
- **2026-10-26** [`66cac6b79c`](https://github.com/sgl-project/sglang/commit/66cac6b79c) [#40519](https://github.com/sgl-project/sglang/pull/40519)
  [Perf] [NPU] deepep: enable MXFP8 low-latency dispatch for Fp8MoEMethod FP4 experts (#40519)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/fp4_moe_methods.py`, `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py`, `python/sglang/srt/layers/quantization/fp8.py`_
- **2026-10-25** [`1b112fd62a`](https://github.com/sgl-project/sglang/commit/1b112fd62a) [#46464](https://github.com/sgl-project/sglang/pull/46464)
  [Perf] [NVIDIA] kimi-k3: FP32 warp split-K GEMM for the MoE front projection on SM107 (#46464)
  _Files: `python/sglang/kernels/ops/gemm/cutedsl_bf16_gemm.py`, `python/sglang/kernels/ops/gemm/dense_bf16_gemm_warp_splitk.py`, `test/registered/kernels/ops/gemm/test_cutedsl_bf16_gemm.py`_
- **2026-10-25** [`2d3de82633`](https://github.com/sgl-project/sglang/commit/2d3de82633) [#45787](https://github.com/sgl-project/sglang/pull/45787)
  [Feat] paged-experts: AWQ, compressed-tensors, MXFP4, NVFP4, W8A8 and block-INT8 experts (#45787)
  _Files: `docs/docs/advanced_features/paged_experts.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/kernels/jit/csrc/moe/paged_experts.cuh`, `python/sglang/kernels/ops/moe/paged_experts.py` _+8 more__
- **2026-10-25** [`a99c7d050f`](https://github.com/sgl-project/sglang/commit/a99c7d050f) [#46140](https://github.com/sgl-project/sglang/pull/46140)
  [Feat] quantization: Add the MiniMax-M3.1 NVFP4 MoE method (#46140)
  _Files: `python/sglang/srt/arg_groups/mega_moe_hook.py`, `python/sglang/srt/arg_groups/moe_hook.py`, `python/sglang/srt/configs/minimax_vl.py`, `python/sglang/srt/configs/model_config.py` _+11 more__
- **2026-10-25** [`ad950cdcd9`](https://github.com/sgl-project/sglang/commit/ad950cdcd9) [#46365](https://github.com/sgl-project/sglang/pull/46365)
  [Fix] deepseek-v4: Complete the MoE output locally when the transport declares no sum group (#46365)
  _Files: `python/sglang/srt/models/deepseek_v4_boundary.py`, `test/registered/unit/models/test_deepseek_v4_boundary.py`_
- **2026-10-25** [`d558ac2f3e`](https://github.com/sgl-project/sglang/commit/d558ac2f3e) [#46137](https://github.com/sgl-project/sglang/pull/46137)
  [Feat] layer-boundary: Fuse TP all-reduce, residual add and RMSNorm on the push plane (#46137)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/kernels/jit/csrc/distributed/all_reduce_fusion.cuh`, `python/sglang/kernels/ops/communication/all_reduce_fusion.py`, `python/sglang/srt/layers/layer_boundary/fusions/custom_all_reduce_fusion.py` _+10 more__
- **2026-10-24** [`bf1a252953`](https://github.com/sgl-project/sglang/commit/bf1a252953) [#46134](https://github.com/sgl-project/sglang/pull/46134)
  [Perf] moe: Run the Marlin GPT-OSS SwiGLU through the fused Triton kernel (#46134)
  _Files: `python/sglang/kernels/ops/activation/minimax_m3_swiglu.py`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py`, `test/registered/kernels/ops/activation/test_activation.py`, `test/registered/kernels/ops/moe/test_marlin_moe.py`_
- **2026-10-24** [`efc9849520`](https://github.com/sgl-project/sglang/commit/efc9849520) [#45758](https://github.com/sgl-project/sglang/pull/45758)
  [Perf] [AMD] GPT-OSS: Pick the gfx1250 W4A8 MoE backend, in-kernel GEMM 1 gather (#45758)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/fused_moe_triton/aiter_mxfp4_w4a8_moe.py`_
- **2026-10-24** [`85f5f7fd73`](https://github.com/sgl-project/sglang/commit/85f5f7fd73) [#46084](https://github.com/sgl-project/sglang/pull/46084)
  [CI] [AMD] pr-test: Move tests in CUDA's extra tier to the AMD extra workflow (#46084)
  _Files: `.github/workflows/pr-test-amd-extra.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/attention/test_torch_native_attention_backend.py`, `test/registered/attention/test_triton_sliding_window.py` _+23 more__
- **2026-10-24** [`3b95120f00`](https://github.com/sgl-project/sglang/commit/3b95120f00) [#46242](https://github.com/sgl-project/sglang/pull/46242)
  [Fix] dsv41: Revert MegaGate routing in prefill (#46242)
  _Files: `python/sglang/srt/layers/moe/mega_gate.py`, `test/registered/unit/layers/moe/test_mega_moe_deepgemm_api.py`_
- **2026-10-24** [`3c6a6c8068`](https://github.com/sgl-project/sglang/commit/3c6a6c8068) [#46232](https://github.com/sgl-project/sglang/pull/46232)
  [Perf] dsv41: Run MegaGate routing in prefill (#46232)
  _Files: `python/sglang/srt/layers/moe/mega_gate.py`, `test/registered/unit/layers/moe/test_mega_moe_deepgemm_api.py`_
- **2026-10-24** [`79701a2549`](https://github.com/sgl-project/sglang/commit/79701a2549) [#46180](https://github.com/sgl-project/sglang/pull/46180)
  [Perf] dsv41: Read Engram rows from peer device shards (#46180)
  _Files: `python/sglang/kernels/ops/embeddings/__init__.py`, `python/sglang/kernels/ops/embeddings/engram_gather.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/engram.py` _+3 more__
- **2026-10-24** [`ee2dd727a3`](https://github.com/sgl-project/sglang/commit/ee2dd727a3) [#46163](https://github.com/sgl-project/sglang/pull/46163)
  [Perf] dsv41: Let Mega-mHC write the MegaMoE input under MegaGate (#46163)
  _Files: `python/sglang/kernels/ops/layernorm/mhc_mega.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4_boundary.py`, `python/sglang/srt/models/deepseek_v4_mhc.py`_
- **2026-10-23** [`5f7542d762`](https://github.com/sgl-project/sglang/commit/5f7542d762) [#46071](https://github.com/sgl-project/sglang/pull/46071)
  [Perf] dsv41: Build the MegaGate row masks once per forward (#46071)
  _Files: `python/sglang/srt/layers/moe/mega_gate.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_dspark.py`_
- **2026-10-23** [`d0022e1df3`](https://github.com/sgl-project/sglang/commit/d0022e1df3) [#45681](https://github.com/sgl-project/sglang/pull/45681)
  [Fix] lora: Preserve MoE projection identity and routing lifetimes (#45681)
  _Files: `python/sglang/kernels/jit/csrc/lora/trtllm_lora_temp/moe_lora_merged_align_kernel.cu`, `python/sglang/kernels/ops/lora/common/routing.py`, `python/sglang/kernels/ops/lora/moe/trtllm_lora_temp/moe_lora_merged_align.py`, `python/sglang/kernels/ops/lora/moe/trtllm_lora_temp/virtual_experts.py` _+14 more__
- **2026-10-23** [`ac3db731b3`](https://github.com/sgl-project/sglang/commit/ac3db731b3) [#45917](https://github.com/sgl-project/sglang/pull/45917)
  [Fix] moe: Preserve CUTLASS routing metadata and execution budgets (#45917)
  _Files: `python/sglang/kernels/jit/csrc/moe/cutlass_prepare_moe_input.cuh`, `python/sglang/kernels/jit/csrc/moe/shuffle_weighted_sum.cuh`, `python/sglang/kernels/ops/moe/__init__.py`, `python/sglang/kernels/ops/moe/cutlass_prepare_moe_input.py` _+28 more__
- **2026-10-23** [`8b9b992e41`](https://github.com/sgl-project/sglang/commit/8b9b992e41) [#45462](https://github.com/sgl-project/sglang/pull/45462)
  [Perf] moe: Preserve Marlin workspace and route-count budgets (#45462)
  _Files: `python/sglang/kernels/jit/csrc/gemm/marlin_moe/kernel.h`, `python/sglang/kernels/jit/csrc/gemm/marlin_moe/marlin_template.h`, `python/sglang/kernels/jit/csrc/gemm/marlin_moe/moe_wna16_marlin.cuh`, `python/sglang/kernels/jit/csrc/moe/align_single_token.cuh` _+15 more__
- **2026-10-23** [`e6451c1a95`](https://github.com/sgl-project/sglang/commit/e6451c1a95) [#45916](https://github.com/sgl-project/sglang/pull/45916)
  [Fix] gguf: Preserve MoE routing, weighting and allocation budgets (#45916)
  _Files: `python/setup.py`, `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/csrc/common_extension_musa.cc`, `python/sglang/kernels/aot/csrc/moe/gguf_moe_weights.cuh` _+32 more__
- **2026-10-23** [`1340044e97`](https://github.com/sgl-project/sglang/commit/1340044e97) [#45915](https://github.com/sgl-project/sglang/pull/45915)
  [Fix] deepseek-v4: Preserve decoder-tail token-count ownership (#45915)
  _Files: `python/sglang/srt/model_executor/runner/row_bucket_graph_runner.py`, `python/sglang/srt/models/deepseek_v4_replay_tail.py`, `test/registered/e2e/model_executor/test_decoder_tail_moe_bound.py`, `test/registered/kernels/ops/diffusion/test_flux2_xpu_norm_fusions.py` _+1 more__
- **2026-10-23** [`c7994e7076`](https://github.com/sgl-project/sglang/commit/c7994e7076) [#45969](https://github.com/sgl-project/sglang/pull/45969)
  [Fix] dsv41: Keep MegaGate out of prefill graphs by gating on the forward mode (#45969)
  _Files: `python/sglang/srt/layers/moe/mega_gate.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `test/registered/unit/layers/moe/test_mega_moe_deepgemm_api.py`_
- **2026-10-23** [`5bdbec0d48`](https://github.com/sgl-project/sglang/commit/5bdbec0d48) [#45933](https://github.com/sgl-project/sglang/pull/45933)
  [Perf] dsv41: Drop the MegaGate padded-row copy on sgl-deep-gemm 0.2.3.post2 (#45933)
  _Files: `docker/Dockerfile.cu134`, `python/pyproject.toml`, `python/sglang/kernels/ops/moe/mega_gate.py`, `test/registered/unit/layers/moe/test_mega_moe_deepgemm_api.py`_
- **2026-10-23** [`f2873f1613`](https://github.com/sgl-project/sglang/commit/f2873f1613) [#44554](https://github.com/sgl-project/sglang/pull/44554)
  [Perf] [NVIDIA] muse-spark-open: Fuse pre-expert RMSNorm with static-scale NVFP4 quantization (#44554)
  _Files: `python/sglang/kernels/jit/csrc/muse_spark/norm_fp4_quant.cuh`, `python/sglang/kernels/ops/layernorm/muse_spark_rmsnorm_nvfp4_quant.py`, `python/sglang/srt/layers/muse_spark/muse_spark_fp4_moe.py`_
- **2026-10-23** [`e5dc0c363a`](https://github.com/sgl-project/sglang/commit/e5dc0c363a) [#43262](https://github.com/sgl-project/sglang/pull/43262)
  [Perf] dsv41: Integrate DeepGEMM MegaGate routing (#43262)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/kernels/ops/moe/__init__.py`, `python/sglang/kernels/ops/moe/dsv4.py`, `python/sglang/kernels/ops/moe/mega_gate.py` _+8 more__
- **2026-10-23** [`c82f7141ad`](https://github.com/sgl-project/sglang/commit/c82f7141ad) [#45450](https://github.com/sgl-project/sglang/pull/45450)
  [Perf] [NVIDIA] dspark: Move the host work between DSv4.1 decode graphs into the graphs for the megakernel path (#45450)
  _Files: `python/sglang/kernels/ops/embeddings/engram_hash.py`, `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/kernels/ops/speculative/dspark/blockwise_rejection.py`, `python/sglang/kernels/ops/speculative/dspark/simulated_bonus.py` _+41 more__
- **2026-10-22** [`13999673ef`](https://github.com/sgl-project/sglang/commit/13999673ef) [#45892](https://github.com/sgl-project/sglang/pull/45892)
  [Feat] lora: Add plan-driven dense and MoE LoRA engines (#45892)
- **2026-10-22** [`635836129b`](https://github.com/sgl-project/sglang/commit/635836129b) [#45637](https://github.com/sgl-project/sglang/pull/45637)
  [Perf] [KDA] muse_spark: use BLOCK_M 240 for BF16 MegaMoE prefill shards (#45637)
  _Files: `python/sglang/srt/layers/muse_spark/muse_spark_megamoe.py`_
- **2026-10-22** [`91fc46a017`](https://github.com/sgl-project/sglang/commit/91fc46a017) [#45456](https://github.com/sgl-project/sglang/pull/45456)
  [Fix] [NVIDIA] docker: Disable torch 2.15 nccl2 in CUDA 13.4 container to fix EPLB rebalance crash (#45456)
  _Files: `docker/Dockerfile.cu134`_
- **2026-10-22** [`e43f6128a0`](https://github.com/sgl-project/sglang/commit/e43f6128a0) [#45422](https://github.com/sgl-project/sglang/pull/45422)
  [Fix] [KDA] cookbook: add MoE runner backend to Muse Spark BF16 recipes (#45422)
  _Files: `docs/src/snippets/configs/meta-models/muse-spark.jsx`_
- **2026-10-22** [`f4ccfd4183`](https://github.com/sgl-project/sglang/commit/f4ccfd4183) [#45591](https://github.com/sgl-project/sglang/pull/45591)
  [Perf] moe: Add H200 block-FP8 Triton configurations (#45591)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=72,N=2048,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=72,N=2048,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128]_down.json`_
- **2026-10-22** [`9301ca37a0`](https://github.com/sgl-project/sglang/commit/9301ca37a0) [#45386](https://github.com/sgl-project/sglang/pull/45386)
  [Fix] modelopt: Correct NVFP4 TRT-LLM clamps for untied gate/up scales (#45386)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4_moe_scales.py`_
- **2026-10-21** [`aa5880e2b8`](https://github.com/sgl-project/sglang/commit/aa5880e2b8) [#45662](https://github.com/sgl-project/sglang/pull/45662)
  [Fix] bailing: Renormalize top-k routing weights by default for Ling-2.5/2.6 (#45662)
  _Files: `python/sglang/srt/models/bailing_moe_linear.py`_
- **2026-10-21** [`f3f0f7b68c`](https://github.com/sgl-project/sglang/commit/f3f0f7b68c) [#45581](https://github.com/sgl-project/sglang/pull/45581)
  [Perf] dsv4: Let the decoder tail leave the prefill graph under DP attention with MegaMoE (#45581)
  _Files: `python/sglang/srt/models/deepseek_v4_replay_tail.py`_
- **2026-10-21** [`620718c8ea`](https://github.com/sgl-project/sglang/commit/620718c8ea) [#45575](https://github.com/sgl-project/sglang/pull/45575)
  [Fix] moe: Keep the DeepSeek V4.1 vision router off the packed-ids path under routing simulation (#45575)
  _Files: `python/sglang/srt/multimodal/dsv41/vl_routing.py`_
- **2026-10-21** [`ed268dd320`](https://github.com/sgl-project/sglang/commit/ed268dd320) [#45628](https://github.com/sgl-project/sglang/pull/45628)
  [Fix] moe: Apply SGLANG_SIMULATE_* routing on DeepSeek-V4.1 vision-biased gates (#45628)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/multimodal/dsv41/vl_routing.py`_
- **2026-10-21** [`5bf10d4c79`](https://github.com/sgl-project/sglang/commit/5bf10d4c79) [#45082](https://github.com/sgl-project/sglang/pull/45082)
  [Fix] nemotron: Correct weight-export failures and GEMV dispatch (#45082)
  _Files: `python/sglang/kernels/jit/csrc/gemm/sm120_nvfp4_moe_mtp_mma.cuh`, `python/sglang/kernels/ops/gemm/__init__.py`, `python/sglang/kernels/ops/gemm/hopper_bf16_gemv.py`, `python/sglang/kernels/ops/gemm/sm120_fp8_gemv.py` _+12 more__
- **2026-10-21** [`bd5a445bf7`](https://github.com/sgl-project/sglang/commit/bd5a445bf7) [#45480](https://github.com/sgl-project/sglang/pull/45480)
  [Fix] [AMD] dsv41: Set moe act to fp8 by default (#45480)
  _Files: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-21** [`f1ba723c64`](https://github.com/sgl-project/sglang/commit/f1ba723c64) [#45476](https://github.com/sgl-project/sglang/pull/45476)
  [Test] [AMD] moe: Expect gfx1250 W4A8 layers to build with expert parallelism (#45476)
  _Files: `test/registered/unit/layers/moe/test_standard_dispatcher.py`_
- **2026-10-20** [`5b1dbc2c80`](https://github.com/sgl-project/sglang/commit/5b1dbc2c80) [#45289](https://github.com/sgl-project/sglang/pull/45289)
  [Fix] [NVIDIA] modelopt-nvfp4: Keep MoE global scales in gate/up order (#45289)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4_moe_scales.py`_
- **2026-10-20** [`027208ae02`](https://github.com/sgl-project/sglang/commit/027208ae02) [#44896](https://github.com/sgl-project/sglang/pull/44896)
  [Doc] layer-boundary/moe: Correct guides and comments that drifted from the code (#44896)
  _Files: `docs/docs/advanced_features/expert_parallelism.mdx`, `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/layer_boundary/residual/add_norm.py`, `python/sglang/srt/layers/moe/utils.py`_
- **2026-10-20** [`299a75ac5d`](https://github.com/sgl-project/sglang/commit/299a75ac5d) [#44994](https://github.com/sgl-project/sglang/pull/44994)
  [Refactor] moe: Derive routing inputs from the layer and active forward (#44994)
  _Files: `.github/workflows/_pr-test-simulator-gpu.yml`, `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/csrc/quantization/gguf/moe.cuh`, `python/sglang/kernels/aot/csrc/quantization/gguf/moe_vec.cuh` _+79 more__
- **2026-10-20** [`4f8f06faf3`](https://github.com/sgl-project/sglang/commit/4f8f06faf3) [#44993](https://github.com/sgl-project/sglang/pull/44993)
  [Refactor] moe: Derive layer contracts from the selected quant method (#44993)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/hunyuan_image3.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` _+91 more__
- **2026-10-20** [`e2e1a97fc3`](https://github.com/sgl-project/sglang/commit/e2e1a97fc3) [#44480](https://github.com/sgl-project/sglang/pull/44480)
  [Fix] moe: Map expert ids for layers whose runner needs local ids under EP (#44480)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/standard.py`, `test/registered/unit/layers/moe/test_standard_dispatcher_runner_backend.py`, `test/registered/unit/lora/test_mem_pool_ep_unit.py`_
- **2026-10-20** [`1dd0f361b8`](https://github.com/sgl-project/sglang/commit/1dd0f361b8) [#45448](https://github.com/sgl-project/sglang/pull/45448)
  [Fix] moe: Run the shared-slot routing test without a published server config (#45448)
  _Files: `test/registered/moe/test_shared_expert_routing_extra.py`_
- **2026-10-20** [`89860fbd2e`](https://github.com/sgl-project/sglang/commit/89860fbd2e) [#45365](https://github.com/sgl-project/sglang/pull/45365)
  [Fix] [AMD] gpt-oss: support EP for gfx1250 W4A8 MXFP4 MoE (#45365)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/aiter_mxfp4_w4a8_moe.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a8_mxfp4_moe.py`_
- **2026-10-20** [`800e60e345`](https://github.com/sgl-project/sglang/commit/800e60e345) [#45376](https://github.com/sgl-project/sglang/pull/45376)
  [Fix] moe: Publish a server config in the CUTLASS runner dispatch-format and placement tests (#45376)
  _Files: `test/registered/unit/layers/moe/test_flashinfer_dispatcher.py`, `test/registered/unit/layers/moe/test_moe_runner_config_placement.py`_
- **2026-10-20** [`9db58ab547`](https://github.com/sgl-project/sglang/commit/9db58ab547) [#39580](https://github.com/sgl-project/sglang/pull/39580)
  [Fix] eplb: Fix Qwen3 MoE output corruption after EPLB rebalance (#39580)
  _Files: `python/sglang/srt/models/qwen3_moe.py`_
- **2026-10-20** [`f8fd41c36e`](https://github.com/sgl-project/sglang/commit/f8fd41c36e) [#43363](https://github.com/sgl-project/sglang/pull/43363)
  [Perf] moe: Extend FlashInfer CUTLASS MoE autotune coverage to prefill chunks (#43363)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutlass.py`, `test/registered/unit/layers/moe/test_flashinfer_cutlass_swiglu_params.py`, `test/registered/unit/layers/moe/test_moe_runner_config_placement.py`, `test/registered/unit/layers/quantization/test_mxfp4_sm120_cutlass.py` _+1 more__
- **2026-10-20** [`fdd89d182a`](https://github.com/sgl-project/sglang/commit/fdd89d182a) [#45350](https://github.com/sgl-project/sglang/pull/45350)
  [Fix] moe: add uses_expert_location to MegaMoE test fixtures (#45350)
  _Files: `test/registered/unit/layers/moe/test_mega_moe_decode_capacity.py`, `test/registered/unit/layers/moe/test_mega_moe_deepgemm_api.py`_
- **2026-10-20** [`78185f4b3f`](https://github.com/sgl-project/sglang/commit/78185f4b3f) [#44858](https://github.com/sgl-project/sglang/pull/44858)
  [Fix] [NVIDIA] modelopt-nvfp4: Read w13 global scales in the TRT-LLM [up, gate] order (#44858)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4_moe_scales.py`_
- **2026-10-20** [`c7687a0e7c`](https://github.com/sgl-project/sglang/commit/c7687a0e7c) [#45299](https://github.com/sgl-project/sglang/pull/45299)
  [Fix] deepseek-v4: Keep the draft MoE out of the target's expert placement (#45299)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/mega_moe_flydsl.py`, `python/sglang/srt/layers/quantization/moe_wna16.py` _+2 more__
- **2026-10-20** [`67d9ee156c`](https://github.com/sgl-project/sglang/commit/67d9ee156c) [#43556](https://github.com/sgl-project/sglang/pull/43556)
  [Fix] [SM120] quantization: Requantize block-FP8 MoE weights to UE8M0 for DeepGEMM (#43556)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/model_loader/utils.py`, `test/registered/unit/layers/quantization/test_deepgemm_ue8m0_requant.py`_
- **2026-10-19** [`6b90e5716d`](https://github.com/sgl-project/sglang/commit/6b90e5716d) [#44913](https://github.com/sgl-project/sglang/pull/44913)
  [Refactor] moe: Scope shared-expert configuration to each model (#44913)
  _Files: `.agents/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/arg_groups/fields/model.py`, `python/sglang/srt/configs/shared_experts.py`, `python/sglang/srt/layers/moe/hash_topk.py` _+58 more__
- **2026-10-19** [`964ab2b280`](https://github.com/sgl-project/sglang/commit/964ab2b280) [#44912](https://github.com/sgl-project/sglang/pull/44912)
  [Refactor] moe: Split the two meanings of num_fused_shared_experts (#44912)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/topk.py`, `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/moe/utils.py` _+11 more__
- **2026-10-19** [`48ea486928`](https://github.com/sgl-project/sglang/commit/48ea486928) [#44904](https://github.com/sgl-project/sglang/pull/44904)
  [Fix] moe: Renormalize per-rank shared-slot routing over routed experts only (#44904)
  _Files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/kernels/ops/moe/moe_fused_gate.py`, `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/topk.py` _+7 more__
- **2026-10-19** [`3a059de94c`](https://github.com/sgl-project/sglang/commit/3a059de94c) [#44901](https://github.com/sgl-project/sglang/pull/44901)
  [Fix] moe: Count routed_scaling_factor once when top-k folds it (#44901)
  _Files: `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/mega_moe_flydsl.py`, `python/sglang/srt/layers/moe/topk.py` _+15 more__
- **2026-10-19** [`5385866108`](https://github.com/sgl-project/sglang/commit/5385866108) [#44138](https://github.com/sgl-project/sglang/pull/44138)
  [Fix] moe: gated NVFP4 MoE intermediate alignment for FlashInfer TRTLLM (#44138)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/unit/layers/quantization/test_nvfp4_moe_backends.py`_
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

## Prefill / Decode Disaggregation  (52 commits)

- **2026-10-26** [`d3e84c32e5`](https://github.com/sgl-project/sglang/commit/d3e84c32e5) [#46193](https://github.com/sgl-project/sglang/pull/46193)
  [Fix] diffusion/disaggregation: Preserve GLM pixels for the head (#46193)
  _Files: `python/sglang/multimodal_gen/test/unit/test_image_response_bytes.py`_
- **2026-10-26** [`c25c24d783`](https://github.com/sgl-project/sglang/commit/c25c24d783) [#46561](https://github.com/sgl-project/sglang/pull/46561)
  [CI] [NPU] registry: Downsize nightly test registrations to the cards each test actually uses (#46561)
  _Files: `test/registered/npu/basic_function/parallel_strategy/data_parallelism/test_npu_load_balance_method_pd_disaggregation.py`, `test/registered/npu/basic_function/pd_disaggregation/test_npu_pd_disaggregation.py`, `test/registered/npu/performance/qwen3_6_27b/test_npu_qwen3_6_27b_2p_in64k_out1k_prefix90_50ms.py`, `test/registered/npu/performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in64k_out1k_50ms.py`_
- **2026-10-26** [`a9bf8c76a0`](https://github.com/sgl-project/sglang/commit/a9bf8c76a0) [#45925](https://github.com/sgl-project/sglang/pull/45925)
  [Feat] minimax: Support MiniMax-M3.1-Flash (#45925)
  _Files: `docker/Dockerfile.cu134`, `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py`, `python/sglang/kernels/ops/speculative/dspark/fused_kv_write.py`, `python/sglang/srt/arg_groups/fields/spec.py` _+59 more__
- **2026-10-26** [`64fc5f0bdb`](https://github.com/sgl-project/sglang/commit/64fc5f0bdb) [#40467](https://github.com/sgl-project/sglang/pull/40467)
  [Feat] hicache: Expose the Mooncake L3 object-key layout for external KV routers (#40467)
  _Files: `docs/docs/advanced_features/hicache_design.mdx`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/data_parallel_controller.py` _+11 more__
- **2026-10-26** [`d7f832d30a`](https://github.com/sgl-project/sglang/commit/d7f832d30a) [#46220](https://github.com/sgl-project/sglang/pull/46220)
  [Perf] pd: Apply the prefill WAR barrier after the previous result is processed (#46220)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `test/registered/unit/disaggregation/test_prefill_result_polling.py`, `test/registered/unit/managers/test_disagg_idle_step_counters.py`_
- **2026-10-26** [`5987ec82ed`](https://github.com/sgl-project/sglang/commit/5987ec82ed) [#44611](https://github.com/sgl-project/sglang/pull/44611)
  [Feat] mem_cache: tag Mooncake offloads with the writing session (#44611)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `python/sglang/srt/mem_cache/storage/umbp/umbp_direct_linker.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py` _+3 more__
- **2026-10-25** [`ee98bb09b0`](https://github.com/sgl-project/sglang/commit/ee98bb09b0) [#46423](https://github.com/sgl-project/sglang/pull/46423)
  [Feat] disaggregation: Verify the KV checksum under a decode-side radix cache (#46423)
  _Files: `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/disaggregation/checksum.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` _+3 more__
- **2026-10-25** [`3dfb166322`](https://github.com/sgl-project/sglang/commit/3dfb166322) [#46388](https://github.com/sgl-project/sglang/pull/46388)
  [Refactor] linker: Use dedicated configuration throughout linker setup (#46388)
  _Files: `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx` _+15 more__
- **2026-10-25** [`5d11819f3a`](https://github.com/sgl-project/sglang/commit/5d11819f3a) [#39729](https://github.com/sgl-project/sglang/pull/39729)
  [Fix] disaggregation: Clean-up and optimize the KV checksum implementation (#39729)
  _Files: `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+11 more__
- **2026-10-25** [`a996b5f224`](https://github.com/sgl-project/sglang/commit/a996b5f224) [#46120](https://github.com/sgl-project/sglang/pull/46120)
  [Fix] diffusion/disaggregation: Isolate malformed request and result messages (#46120)
  _Files: `docs/docs/sglang-diffusion/disaggregation.mdx`, `python/sglang/multimodal_gen/runtime/disaggregation/orchestrator.py`, `python/sglang/multimodal_gen/runtime/disaggregation/scheduler_mixin.py`, `python/sglang/multimodal_gen/test/unit/test_disagg_orchestration.py`_
- **2026-10-25** [`f82af9ca17`](https://github.com/sgl-project/sglang/commit/f82af9ca17) [#40595](https://github.com/sgl-project/sglang/pull/40595)
  [Feat] unified-cache: Support out-of-tree external linkers (#40595)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/advanced_features/server_arguments_undocumented.txt`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/memory.py` _+9 more__
- **2026-10-25** [`0ff67ee72a`](https://github.com/sgl-project/sglang/commit/0ff67ee72a) [#45076](https://github.com/sgl-project/sglang/pull/45076)
  [Fix] hicache: Count the EAGLE bigram boundary token in PD decode restores (#45076)
  _Files: `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `test/registered/unit/disaggregation/test_decode_hicache_tree_core.py`, `test/registered/unit/mem_cache/unified_radix_cache/test_unified_radix_cache_storage.py`_
- **2026-10-25** [`0f41fffec8`](https://github.com/sgl-project/sglang/commit/0f41fffec8) [#46025](https://github.com/sgl-project/sglang/pull/46025)
  [Fix] diffusion: Fail closed after local worker loss or multi-rank OOM (#46025)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/disaggregation/orchestrator.py`, `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/launch_server.py` _+9 more__
- **2026-10-25** [`c5e734e437`](https://github.com/sgl-project/sglang/commit/c5e734e437) [#46205](https://github.com/sgl-project/sglang/pull/46205)
  [Feat] rust-server: Report weight versions and media token counts in generate meta_info (#46205)
  _Files: `proto/sglang/api/v1/generate.proto`, `python/sglang/api/v1/api_types.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+37 more__
- **2026-10-24** [`f0f6fd4e9d`](https://github.com/sgl-project/sglang/commit/f0f6fd4e9d) [#46104](https://github.com/sgl-project/sglang/pull/46104)
  [Fix] diffusion/disaggregation: Keep decoded images in tensor transport (#46104)
  _Files: `python/sglang/multimodal_gen/runtime/disaggregation/scheduler_mixin.py`, `python/sglang/multimodal_gen/test/unit/test_image_response_bytes.py`_
- **2026-10-24** [`1335d372f0`](https://github.com/sgl-project/sglang/commit/1335d372f0) [#45970](https://github.com/sgl-project/sglang/pull/45970)
  [Feat] metrics: Export prealloc_{full,swa}_token_usage for decode requests with a pending KV transfer (#45970)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/managers/scheduler_components/pool_stats_observer.py`, `python/sglang/srt/observability/metrics_collector.py` _+3 more__
- **2026-10-24** [`a99eaf9a76`](https://github.com/sgl-project/sglang/commit/a99eaf9a76) [#46127](https://github.com/sgl-project/sglang/pull/46127)
  [Fix] scheduler: Keep long prefill steps in the busy counter and exclude engine pauses (#46127)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/disaggregation/test_prefill_result_polling.py`, `test/registered/unit/managers/test_disagg_idle_step_counters.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_
- **2026-10-24** [`de7055f596`](https://github.com/sgl-project/sglang/commit/de7055f596) [#41140](https://github.com/sgl-project/sglang/pull/41140)
  [Refactor] pd: Consolidate sender and receiver implementations (#41140)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+11 more__
- **2026-10-23** [`0d592c475b`](https://github.com/sgl-project/sglang/commit/0d592c475b) [#46066](https://github.com/sgl-project/sglang/pull/46066)
  [Fix] rust-server: Keep a transfer backend's own bootstrap port on prefill (#46066)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/managers/disagg_service.py`, `test/registered/unit/entrypoints/test_rust_server_dp_ports.py`_
- **2026-10-23** [`ea226cf782`](https://github.com/sgl-project/sglang/commit/ea226cf782) [#43774](https://github.com/sgl-project/sglang/pull/43774)
  [Feat] glm5.3flash: Support padded CP BCG and prefix replay with PD/DFlash2 (#43774)
  _Files: `python/sglang/srt/arg_groups/cp_tp_group_sharing_hook.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/attention/graph_utils.py` _+13 more__
- **2026-10-23** [`1e894eb92d`](https://github.com/sgl-project/sglang/commit/1e894eb92d) [#46126](https://github.com/sgl-project/sglang/pull/46126)
  [CI] disaggregation: Run the SWA decode radix cache test on Mooncake (#46126)
  _Files: `test/registered/disaggregation/test_disaggregation_decode_radix_cache_swa.py`_
- **2026-10-23** [`16aa816060`](https://github.com/sgl-project/sglang/commit/16aa816060) [#45922](https://github.com/sgl-project/sglang/pull/45922)
  [Fix] disaggregation: Restart a lost prefill's heartbeat miss count (#45922)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-10-23** [`5a86d6ee17`](https://github.com/sgl-project/sglang/commit/5a86d6ee17) [#45899](https://github.com/sgl-project/sglang/pull/45899)
  [Fix] rust-server: Deliver scheduler-side aborts to Rust frontend clients (#45899)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/rust_server/server.py`, `test/registered/unit/dllm/test_gemma4_uniform_lifecycle.py`, `test/registered/unit/managers/test_multimodal_abort_cleanup.py` _+6 more__
- **2026-10-23** [`c677171c1d`](https://github.com/sgl-project/sglang/commit/c677171c1d) [#41187](https://github.com/sgl-project/sglang/pull/41187)
  [Feat] hicache: Support MLA DCP with HiCache L3(file/mooncake) (#41187)
  _Files: `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py` _+10 more__
- **2026-10-23** [`77bc8cab18`](https://github.com/sgl-project/sglang/commit/77bc8cab18) [#43548](https://github.com/sgl-project/sglang/pull/43548)
  [Fix] hicache/pd: Promise prefill only the L3 span the decode prefetch takes (#43548)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `test/registered/unit/mem_cache/unified_radix_cache/test_unified_radix_cache_storage.py`_
- **2026-10-23** [`6e667c4310`](https://github.com/sgl-project/sglang/commit/6e667c4310) [#45973](https://github.com/sgl-project/sglang/pull/45973)
  [Fix] disaggregation: Poison the deferred abort ack when a NIXL or Mori write fails (#45973)
  _Files: `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_mori_deferred_kv_release.py`, `test/registered/unit/disaggregation/test_nixl_deferred_kv_release.py`_
- **2026-10-23** [`363e6c6b4d`](https://github.com/sgl-project/sglang/commit/363e6c6b4d) [#45309](https://github.com/sgl-project/sglang/pull/45309)
  [Feat] diffusion/disaggregation: split FLUX.3 prompt and image encoders (#45309)
  _Files: `docs/cookbook/diffusion/FLUX/FLUX.3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/disaggregation.mdx`, `python/sglang/multimodal_gen/runtime/disaggregation/orchestrator.py` _+17 more__
- **2026-10-22** [`81841d6bdc`](https://github.com/sgl-project/sglang/commit/81841d6bdc) [#40565](https://github.com/sgl-project/sglang/pull/40565)
  [Fix] hicache: Fail fast on a null pointer from the Mooncake host allocator (#40565)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `test/registered/unit/mem_cache/test_mooncake_host_allocator.py`_
- **2026-10-22** [`8a6770d566`](https://github.com/sgl-project/sglang/commit/8a6770d566) [#45722](https://github.com/sgl-project/sglang/pull/45722)
  [Fix] NIXL: Preserve explicit UCX network device selection (#45722)
  _Files: `docs/docs/advanced_features/pd_disaggregation.mdx`, `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-10-22** [`f68e82e7bc`](https://github.com/sgl-project/sglang/commit/f68e82e7bc) [#41376](https://github.com/sgl-project/sglang/pull/41376)
  [Fix] epd: Accept tokens-in requests on scheduler-side transfer backends (#41376)
  _Files: `python/sglang/srt/disaggregation/encoder/receiver.py`, `test/registered/unit/disaggregation/test_encode_receiver.py`_
- **2026-10-22** [`9569a36561`](https://github.com/sgl-project/sglang/commit/9569a36561) [#44001](https://github.com/sgl-project/sglang/pull/44001)
  [Feat] scheduler: Gate --prefill-decode-interval on running batch size (#44001)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/advanced_features/server_arguments_undocumented.txt`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/schedule.py` _+5 more__
- **2026-10-22** [`a6a6beffac`](https://github.com/sgl-project/sglang/commit/a6a6beffac) [#45641](https://github.com/sgl-project/sglang/pull/45641)
  [Refactor] disaggregation: Share the flag all-reduce and host-destination predicate in the decode transfer queue (#45641)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/utils.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`, `test/registered/unit/disaggregation/test_deferred_decode_kv_release.py`_
- **2026-10-22** [`6929afb528`](https://github.com/sgl-project/sglang/commit/6929afb528) [#45108](https://github.com/sgl-project/sglang/pull/45108)
  [Fix] hisparse: Keep PD destination host pages until the decode KV release (#45108)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_deferred_decode_kv_release.py`_
- **2026-10-22** [`8dc7f98005`](https://github.com/sgl-project/sglang/commit/8dc7f98005) [#45492](https://github.com/sgl-project/sglang/pull/45492)
  [Perf] pd: Send prefill KV chunks without a host sync on the scheduler thread (#45492)
  _Files: `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `test/registered/unit/disaggregation/test_mooncake_transfer_batching.py`_
- **2026-10-22** [`3468a65b51`](https://github.com/sgl-project/sglang/commit/3468a65b51) [#45578](https://github.com/sgl-project/sglang/pull/45578)
  [CI] labeler: Add a mooncake PR label (#45578)
  _Files: `.github/labeler.yml`_
- **2026-10-21** [`2c7a9e3b50`](https://github.com/sgl-project/sglang/commit/2c7a9e3b50) [#45559](https://github.com/sgl-project/sglang/pull/45559)
  [Fix] radix-cache: Order linker offloads behind the forward that writes the pages (#45559)
  _Files: `python/sglang/srt/mem_cache/registry.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/storage/umbp/umbp_direct_linker.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py` _+3 more__
- **2026-10-21** [`7e0e259435`](https://github.com/sgl-project/sglang/commit/7e0e259435) [#45519](https://github.com/sgl-project/sglang/pull/45519)
  [CI] [AMD] disaggregation: Register Mooncake KV buffers without HIP dmabuf (#45519)
  _Files: `.github/workflows/pr-test-amd.yml`_
- **2026-10-21** [`b57b5e2286`](https://github.com/sgl-project/sglang/commit/b57b5e2286) [#45453](https://github.com/sgl-project/sglang/pull/45453)
  [Fix] disaggregation: Synchronize deferred decode KV release across TP ranks (#45453)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`, `test/registered/unit/disaggregation/test_deferred_decode_kv_release.py`_
- **2026-10-21** [`af49ada16d`](https://github.com/sgl-project/sglang/commit/af49ada16d) [#44215](https://github.com/sgl-project/sglang/pull/44215)
  [Fix] pd: Allow runtime role switching with DP and DP attention (#44215)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/role_switch.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_control_mixin.py` _+1 more__
- **2026-10-21** [`8e3e2980db`](https://github.com/sgl-project/sglang/commit/8e3e2980db) [#40861](https://github.com/sgl-project/sglang/pull/40861)
  [Feat] [Intel] disaggregation: Support XPU for staging-buffer KV transfer (#40861)
  _Files: `docs/docs/advanced_features/pd_disaggregation.mdx`, `docs/docs/hardware-platforms/xpu.mdx`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/dcp_pack.py` _+9 more__
- **2026-10-21** [`2e7c9d851c`](https://github.com/sgl-project/sglang/commit/2e7c9d851c) [#43482](https://github.com/sgl-project/sglang/pull/43482)
  [Feat] NIXL: Support per-GPU UCX device selection (#43482)
  _Files: `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `python/sglang/test/server_fixtures/disaggregation_fixture.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-10-21** [`be65391abd`](https://github.com/sgl-project/sglang/commit/be65391abd) [#45338](https://github.com/sgl-project/sglang/pull/45338)
  [Feat] mooncake: Enable the failed-session probe by default with backoff and idle pruning (#45338)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/environ.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py` _+2 more__
- **2026-10-21** [`fb6e6a09ce`](https://github.com/sgl-project/sglang/commit/fb6e6a09ce) [#43814](https://github.com/sgl-project/sglang/pull/43814)
  [Fix] [NPU] disaggregation: Fix host-pool backup for decode retraction (#43814)
  _Files: `python/sglang/srt/hardware_backend/npu/utils.py`, `python/sglang/srt/mem_cache/pool_host/mha.py`, `test/registered/npu/basic_function/pd_disaggregation/test_npu_pd_decode_retraction_backup.py`_
- **2026-10-21** [`1c2f42470c`](https://github.com/sgl-project/sglang/commit/1c2f42470c) [#45440](https://github.com/sgl-project/sglang/pull/45440)
  [Fix] disaggregation: Keep a requeued optimistic prefill request's multimodal inputs (#45440)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `test/registered/unit/disaggregation/test_prefill_complete_integration.py`_
- **2026-10-21** [`93088901fb`](https://github.com/sgl-project/sglang/commit/93088901fb) [#44803](https://github.com/sgl-project/sglang/pull/44803)
  [Chore] attention: Remove the tokenspeed_mla backend and dependency (#44803)
  _Files: `.agents/skills/sglang-runtime-context/SKILL.md`, `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/docs/advanced_features/attention_backend.mdx`, `docs/src/snippets/autoregressive/kimi-k25-deployment.jsx` _+36 more__
- **2026-10-20** [`eb4b167d27`](https://github.com/sgl-project/sglang/commit/eb4b167d27) [#38473](https://github.com/sgl-project/sglang/pull/38473)
  [Feat] KVShard: PD transfer and e2e test (#38473)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `test/registered/e2e/disaggregation/test_disaggregation_kv_cache_sharding.py` _+3 more__
- **2026-10-20** [`1ec902e00f`](https://github.com/sgl-project/sglang/commit/1ec902e00f) [#44623](https://github.com/sgl-project/sglang/pull/44623)
  [Fix] cache: Support DeepSeek-V4.1 external linker pools (#44623)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py` _+4 more__
- **2026-10-20** [`3eb4bd598f`](https://github.com/sgl-project/sglang/commit/3eb4bd598f) [#43344](https://github.com/sgl-project/sglang/pull/43344)
  [Perf] hicache: Unify PP prefetch hit queries and buffer allocation (#43344)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `test/registered/unit/mem_cache/test_pp_prefetch_ticket.py`_
- **2026-10-19** [`0ce41c5a06`](https://github.com/sgl-project/sglang/commit/0ce41c5a06) [#42702](https://github.com/sgl-project/sglang/pull/42702)
  [Fix] PD: retraction restores racing the in-flight decode forward (#42702)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`, `test/registered/unit/mem_cache/test_decode_retraction_backup.py`_
- **2026-10-19** [`33dd8f6a2e`](https://github.com/sgl-project/sglang/commit/33dd8f6a2e) [#34535](https://github.com/sgl-project/sglang/pull/34535)
  [Fix] hybrid-SSM: DP attention failures at low concurrency (#34535)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` _+12 more__
- **2026-10-19** [`82c9a8b037`](https://github.com/sgl-project/sglang/commit/82c9a8b037) [#45075](https://github.com/sgl-project/sglang/pull/45075)
  [Perf] deepseek-v4.1: Default PD to MegaAttention, with the KV layout in the PD handshake (#45075)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py` _+5 more__
- **2026-10-19** [`69076b9f9e`](https://github.com/sgl-project/sglang/commit/69076b9f9e) [#41675](https://github.com/sgl-project/sglang/pull/41675)
  [CI] [NPU] tests: Reduce HiCache sizes and enable expandable pinned memory in focused tests (#41675)
  _Files: `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py`, `test/registered/npu/accuracy/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms_aime26.py`, `test/registered/npu/basic_function/HiCache/test_npu_hicache_mha.py`, `test/registered/npu/basic_function/HiCache/test_npu_hicache_mla.py` _+5 more__

## KV Cache / Memory  (43 commits)

- **2026-10-26** [`095750baf9`](https://github.com/sgl-project/sglang/commit/095750baf9) [#46227](https://github.com/sgl-project/sglang/pull/46227)
  [Perf] diffusion: Walk several row chunks per warp in the CuTe-DSL norm kernels (#46227)
  _Files: `python/sglang/kernels/ops/diffusion/norm/cutedsl_common/norm_fusion.py`, `python/sglang/kernels/ops/diffusion/norm/cutedsl_common/reduce.py`, `python/sglang/kernels/ops/diffusion/norm/scale_residual_norm_cutedsl.py`, `test/registered/kernels/ops/diffusion/test_norm.py`_
- **2026-10-26** [`9f594d586b`](https://github.com/sgl-project/sglang/commit/9f594d586b) [#46501](https://github.com/sgl-project/sglang/pull/46501)
  [Fix] hicache: Delegate on_host_pools_registered in the failure injector (#46501)
  _Files: `python/sglang/srt/mem_cache/hicache_storage.py`_
- **2026-10-26** [`fd5c52588f`](https://github.com/sgl-project/sglang/commit/fd5c52588f) [#43539](https://github.com/sgl-project/sglang/pull/43539)
  [Test] HiCache: Inject random delays and failures for testing (#43539)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/storage/backend_factory.py` _+1 more__
- **2026-10-25** [`8252e3af63`](https://github.com/sgl-project/sglang/commit/8252e3af63) [#41701](https://github.com/sgl-project/sglang/pull/41701)
  [Fix] [AMD] mamba: Keep a chunked prefill cut on the mamba chunk grid so DCP can donate checkpoints (#41701)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_mamba_checkpoint_depth.py`_
- **2026-10-25** [`94d2b61e38`](https://github.com/sgl-project/sglang/commit/94d2b61e38) [#46442](https://github.com/sgl-project/sglang/pull/46442)
  [Fix] unified-memory: Name the draft KV dtype flag in the fused-region mismatch error (#46442)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`_
- **2026-10-25** [`26a1e5110d`](https://github.com/sgl-project/sglang/commit/26a1e5110d) [#43727](https://github.com/sgl-project/sglang/pull/43727)
  [Feat] hicache: Export host Mamba pool occupancy next to host KV (#43727)
  _Files: `docs/docs/advanced_features/hicache_best_practices.mdx`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/mem_cache/pool_host/mamba.py`, `python/sglang/srt/observability/metrics_collector.py` _+2 more__
- **2026-10-25** [`c00e7e12b6`](https://github.com/sgl-project/sglang/commit/c00e7e12b6) [#45104](https://github.com/sgl-project/sglang/pull/45104)
  [Fix] hisparse: Copy DeepSeek-V4 eager backups token by token (#45104)
  _Files: `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `test/registered/unit/managers/test_hisparse_unit.py`_
- **2026-10-24** [`3ea7e210d2`](https://github.com/sgl-project/sglang/commit/3ea7e210d2) [#44029](https://github.com/sgl-project/sglang/pull/44029)
  [Perf] KVShard: 0SM KV Cache Allgather for KV Cache Sharding (#44029)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/distributed/device_communicators/pynccl.py`, `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py` _+6 more__
- **2026-10-23** [`005333d029`](https://github.com/sgl-project/sglang/commit/005333d029) [#45444](https://github.com/sgl-project/sglang/pull/45444)
  [Refactor] radix-tree: Make each cache action a typed CacheAction implementation (#45444)
  _Files: `rust/sglang-radix-tree/src/cache_action.rs`, `rust/sglang-radix-tree/src/components/full.rs`, `rust/sglang-radix-tree/src/components/mamba.rs`, `rust/sglang-radix-tree/src/components/mod.rs` _+12 more__
- **2026-10-23** [`79ab8f6d7c`](https://github.com/sgl-project/sglang/commit/79ab8f6d7c) [#40929](https://github.com/sgl-project/sglang/pull/40929)
  [Feat] KVShard: Support kv cache sharding for MTP (#40929)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/page_interleave.py`, `python/sglang/srt/mem_cache/page_interleave_pool.py`, `test/registered/unit/managers/test_prefill_adder.py` _+2 more__
- **2026-10-23** [`94e4611eac`](https://github.com/sgl-project/sglang/commit/94e4611eac) [#45714](https://github.com/sgl-project/sglang/pull/45714)
  [Refactor] unified-cache: Factor match validators and match completion into helpers (#45714)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/unified_radix_cache/test_unified_radix_cache_core.py`_
- **2026-10-22** [`3b0003dac1`](https://github.com/sgl-project/sglang/commit/3b0003dac1) [#42701](https://github.com/sgl-project/sglang/pull/42701)
  [Fix] HiCache: stale host KV from write-through copies racing the in-flight forward (#42701)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_hicache_staged_write_back_dispatch.py`_
- **2026-10-22** [`bf0e193bfd`](https://github.com/sgl-project/sglang/commit/bf0e193bfd) [#45702](https://github.com/sgl-project/sglang/pull/45702)
  [Refactor] radix-tree: Move insert overlap handling into a resumable OVERLAP phase (#45702)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/README.md`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`_
- **2026-10-22** [`aae2145eb2`](https://github.com/sgl-project/sglang/commit/aae2145eb2) [#45703](https://github.com/sgl-project/sglang/pull/45703)
  [Feat] radix-tree: Report the last visited node and a shorter FULL device match in match results (#45703)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `rust/sglang-radix-tree/src/python_bindings.rs` _+3 more__
- **2026-10-22** [`357323e912`](https://github.com/sgl-project/sglang/commit/357323e912) [#45701](https://github.com/sgl-project/sglang/pull/45701)
  [Refactor] hicache: Route buffer-mode backup admission keys and FULL transfers through pipeline hooks (#45701)
  _Files: `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`_
- **2026-10-22** [`4f96807ea8`](https://github.com/sgl-project/sglang/commit/4f96807ea8) [#45334](https://github.com/sgl-project/sglang/pull/45334)
  [CI] radix-cache: Build unified radix cache test states through production paths (#45334)
  _Files: `python/sglang/test/kits/unified_radix_cache/config.py`, `python/sglang/test/kits/unified_radix_cache/core.py`, `python/sglang/test/kits/unified_radix_cache/fixtures.py`, `python/sglang/test/kits/unified_radix_cache/insert_walk.py` _+11 more__
- **2026-10-22** [`8cd3c494a3`](https://github.com/sgl-project/sglang/commit/8cd3c494a3) [#45538](https://github.com/sgl-project/sglang/pull/45538)
  [Fix] mem_cache: Skip linker L3 lookup on PD decode (#45538)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_cache_linker.py`_
- **2026-10-22** [`dcf05724f7`](https://github.com/sgl-project/sglang/commit/dcf05724f7) [#37620](https://github.com/sgl-project/sglang/pull/37620)
  [Perf] diffusion: accumulate chunked LoRA merges with addmm (#37620)
  _Files: `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/test/unit/manual/bench_lora_merge_addmm.py`, `python/sglang/multimodal_gen/test/unit/test_lora_inference_mode.py`_
- **2026-10-22** [`9d5386fd13`](https://github.com/sgl-project/sglang/commit/9d5386fd13) [#45726](https://github.com/sgl-project/sglang/pull/45726)
  [Perf] dsv41: Fuse request-window layout construction (#45726)
  _Files: `python/sglang/kernels/ops/kvcache/__init__.py`, `python/sglang/kernels/ops/kvcache/dsv41_window_layout.py`, `python/sglang/srt/mem_cache/dsv41_request_window.py`_
- **2026-10-21** [`4b9936b5e3`](https://github.com/sgl-project/sglang/commit/4b9936b5e3) [#43448](https://github.com/sgl-project/sglang/pull/43448)
  [Fix] deepseek_v4: Fix mHC prewarm when chunked prefill is disabled (#43448)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`_
- **2026-10-21** [`740d5f9f9e`](https://github.com/sgl-project/sglang/commit/740d5f9f9e) [#45472](https://github.com/sgl-project/sglang/pull/45472)
  [Perf] scheduler: Plan hybrid Mamba extend batches without host-device syncs (#45472)
  _Files: `python/sglang/srt/hardware_backend/mlx/kv_cache/auxiliary_state.py`, `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `python/sglang/srt/managers/mm_schedule.py`, `python/sglang/srt/managers/mm_utils.py` _+10 more__
- **2026-10-21** [`5e79333c95`](https://github.com/sgl-project/sglang/commit/5e79333c95) [#45439](https://github.com/sgl-project/sglang/pull/45439)
  [Refactor] radix-tree: Reuse the insert walk, component hooks and bindings for custom tree cores (#45439)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/c128_sidecar_component.py`, `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/components/base.py`, `python/sglang/srt/mem_cache/unified_cache/components/full.py` _+27 more__
- **2026-10-21** [`da7e3f1c12`](https://github.com/sgl-project/sglang/commit/da7e3f1c12) [#44929](https://github.com/sgl-project/sglang/pull/44929)
  [Fix] cache: Accept packed draft layer mappings in the UMBP linker (#44929)
  _Files: `python/sglang/srt/mem_cache/storage/umbp/umbp_direct_linker.py`, `test/registered/unit/mem_cache/test_umbp_direct_linker_rank_keys.py`_
- **2026-10-21** [`32c26788f3`](https://github.com/sgl-project/sglang/commit/32c26788f3) [#45435](https://github.com/sgl-project/sglang/pull/45435)
  [Fix] mamba: Keep prefill rows' checkpoint tracking through mixed chunked prefill (#45435)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/managers/test_mix_with_running_mamba_track.py`, `test/registered/unit/managers/test_schedule_batch_out_of_place.py`_
- **2026-10-20** [`cc7ae372ac`](https://github.com/sgl-project/sglang/commit/cc7ae372ac) [#45242](https://github.com/sgl-project/sglang/pull/45242)
  [Refactor] radix-cache: Route pending-backup split bookkeeping through one component action (#45242)
  _Files: `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/cache_action.py`, `python/sglang/srt/mem_cache/unified_cache/components/full.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa.py` _+12 more__
- **2026-10-20** [`0b536ca112`](https://github.com/sgl-project/sglang/commit/0b536ca112) [#45238](https://github.com/sgl-project/sglang/pull/45238)
  [Fix] radix-cache: Separate logical and reclaimable value lengths in tree components (#45238)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/base.py`, `python/sglang/srt/mem_cache/unified_cache/components/full.py`, `python/sglang/srt/mem_cache/unified_cache/components/mamba.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa.py` _+12 more__
- **2026-10-20** [`bab4a808d8`](https://github.com/sgl-project/sglang/commit/bab4a808d8) [#45222](https://github.com/sgl-project/sglang/pull/45222)
  [Perf] unified-memory: Allocate free pages from each sub-pool's own end first (#45222)
  _Files: `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py`, `test/registered/unit/mem_cache/test_unified_hicache_transfer_lifecycle.py`_
- **2026-10-20** [`0d7638b035`](https://github.com/sgl-project/sglang/commit/0d7638b035) [#45158](https://github.com/sgl-project/sglang/pull/45158)
  [Fix] scheduler: Exclude accepted storage-tier hits from the waiting prefill load (#45158)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/load_inquirer.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+2 more__
- **2026-10-20** [`dc62c3effd`](https://github.com/sgl-project/sglang/commit/dc62c3effd) [#45241](https://github.com/sgl-project/sglang/pull/45241)
  [Feat] radix-tree: Report each path node's child count in collect_path_info (#45241)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py`, `rust/sglang-radix-tree/src/python_bindings.rs`, `rust/sglang-radix-tree/src/tests/unified_tree_core.rs` _+2 more__
- **2026-10-20** [`cfec1b91bb`](https://github.com/sgl-project/sglang/commit/cfec1b91bb) [#45356](https://github.com/sgl-project/sglang/pull/45356)
  [Fix] muse_spark: support unified KV memory with TRT-LLM (#45356)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/rerun-test.yml`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/models/muse_spark.py` _+1 more__
- **2026-10-20** [`3bf4cbc6cf`](https://github.com/sgl-project/sglang/commit/3bf4cbc6cf) [#44436](https://github.com/sgl-project/sglang/pull/44436)
  [Perf] [NPU] mem_cache: Increase GLM-5.2-W4A8C8 KV cache capacity with compact DSA indexer allocation (#44436)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/mem_cache/test_kv_cache_configurator_npu_indexer.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-10-20** [`15e8e687db`](https://github.com/sgl-project/sglang/commit/15e8e687db) [#45090](https://github.com/sgl-project/sglang/pull/45090)
  [Chore] environ: Remove retired unified radix tree environment variable (#45090)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx`, `docs/src/snippets/agentx/zai-org/glm-5.2.jsx`, `python/sglang/srt/environ.py`_
- **2026-10-20** [`4a651146de`](https://github.com/sgl-project/sglang/commit/4a651146de) [#44030](https://github.com/sgl-project/sglang/pull/44030)
  [Feat] hicache: Notify storage backends when the initial host-pool registration burst completes (#44030)
  _Files: `docs/docs/advanced_features/hicache_design.mdx`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py` _+3 more__
- **2026-10-20** [`ce329c85fa`](https://github.com/sgl-project/sglang/commit/ce329c85fa) [#45276](https://github.com/sgl-project/sglang/pull/45276)
  [Perf] deepseek-v4.1: Skip the request-window history check when invariant checks are off (#45276)
  _Files: `python/sglang/srt/mem_cache/dsv41_request_window.py`_
- **2026-10-20** [`ebc71e650e`](https://github.com/sgl-project/sglang/commit/ebc71e650e) [#40535](https://github.com/sgl-project/sglang/pull/40535)
  [Perf] [NPU] mem_cache: Add optional ScatterPa KV cache writes (#40535)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `test/registered/unit/npu/test_npu_scatter_pa_kv_cache.py`_
- **2026-10-20** [`ab580b2e06`](https://github.com/sgl-project/sglang/commit/ab580b2e06) [#45236](https://github.com/sgl-project/sglang/pull/45236)
  [CI] radix-cache: Split unified radix cache unit tests into topic files and a shared kit (#45236)
  _Files: `python/sglang/test/kits/unified_radix_cache/__init__.py`, `python/sglang/test/kits/unified_radix_cache/config.py`, `python/sglang/test/kits/unified_radix_cache/core.py`, `python/sglang/test/kits/unified_radix_cache/fixtures.py` _+28 more__
- **2026-10-19** [`1238edd954`](https://github.com/sgl-project/sglang/commit/1238edd954) [#45247](https://github.com/sgl-project/sglang/pull/45247)
  [Perf] deepseek-v4.1: Reset request-window tags without a host sync (#45247)
  _Files: `python/sglang/srt/mem_cache/dsv41_request_window.py`_
- **2026-10-19** [`80ea5ee638`](https://github.com/sgl-project/sglang/commit/80ea5ee638) [#39592](https://github.com/sgl-project/sglang/pull/39592)
  [Fix] dLLM: Preserve prompt tails and literal mask tokens across prefix reuse (#39592)
  _Files: `python/sglang/srt/dllm/algorithm/base.py`, `python/sglang/srt/dllm/algorithm/joint_threshold.py`, `python/sglang/srt/dllm/algorithm/joint_threshold_indel.py`, `python/sglang/srt/dllm/algorithm/low_confidence.py` _+6 more__
- **2026-10-19** [`b20cb3665d`](https://github.com/sgl-project/sglang/commit/b20cb3665d) [#45232](https://github.com/sgl-project/sglang/pull/45232)
  [CI] radix-cache: Drop redundant unified radix cache unit tests (#45232)
  _Files: `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-10-19** [`8b1d1e0d74`](https://github.com/sgl-project/sglang/commit/8b1d1e0d74) [#45223](https://github.com/sgl-project/sglang/pull/45223)
  [Perf] deepseek-v4.1: Check request-window SWA history without per-layer host syncs (#45223)
  _Files: `python/sglang/srt/mem_cache/dsv41_request_window.py`_
- **2026-10-19** [`c04f9a61f0`](https://github.com/sgl-project/sglang/commit/c04f9a61f0) [#44286](https://github.com/sgl-project/sglang/pull/44286)
  [Fix] diffusion: Fix VMoBA chunk selection bugs (#44286)
  _Files: `python/sglang/multimodal_gen/csrc/attn/vmoba_attn/tests/test_vmoba_selection.py`, `python/sglang/multimodal_gen/csrc/attn/vmoba_attn/tests/test_vmoba_selection_gpu.py`, `python/sglang/multimodal_gen/csrc/attn/vmoba_attn/vmoba/vmoba.py`_
- **2026-10-19** [`96ba108072`](https://github.com/sgl-project/sglang/commit/96ba108072) [#44564](https://github.com/sgl-project/sglang/pull/44564)
  [Fix] dsa-eagle-topk: Copy token keys and scales when relocating index cache (#44564)
  _Files: `python/sglang/srt/mem_cache/index_key_cache.py`, `test/registered/kernels/ops/kvcache/test_dsa_index_cache_move.py`, `test/registered/unit/mem_cache/test_index_key_cache_move.py`_
- **2026-10-19** [`59fec011dd`](https://github.com/sgl-project/sglang/commit/59fec011dd) [#45051](https://github.com/sgl-project/sglang/pull/45051)
  [Fix] deepseek-v4.1: Reject encoder replay on a chunk too small for a hit or on other models (#45051)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `test/registered/unit/managers/test_prefill_adder.py`, `test/registered/unit/model_executor/test_encoder_swa_replay.py`_

## Quantization  (31 commits)

- **2026-10-26** [`589d196bc3`](https://github.com/sgl-project/sglang/commit/589d196bc3) [#40435](https://github.com/sgl-project/sglang/pull/40435)
  [Fix] [NPU] requantization: gate arch35 block-FP8 -> MXFP8 requantization (#40435)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/quantization/w8a8_mxfp8.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-10-25** [`b48809dfc2`](https://github.com/sgl-project/sglang/commit/b48809dfc2) [#46085](https://github.com/sgl-project/sglang/pull/46085)
  [CI] [AMD] pr-test: Move large-model and perf tests from AMD PR CI to nightly (#46085)
  _Files: `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/amd/perf/mi35x/test_qwen35_fp8_ar_fusion_mi35x.py`, `test/registered/amd/test_deepseek_v32_basic.py` _+6 more__
- **2026-10-24** [`c9f40557e6`](https://github.com/sgl-project/sglang/commit/c9f40557e6) [#46046](https://github.com/sgl-project/sglang/pull/46046)
  [Perf] diffusion: Remove per-step host syncs and uploads in image models (#46046)
  _Files: `python/sglang/multimodal_gen/configs/models/vaes/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/glm_image.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/krea2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image.py` _+24 more__
- **2026-10-23** [`197be2203a`](https://github.com/sgl-project/sglang/commit/197be2203a) [#46170](https://github.com/sgl-project/sglang/pull/46170)
  [Doc] quantization: Link W4A16 design from environment reference (#46170)
  _Files: `docs/docs/references/environment_variables.mdx`_
- **2026-10-23** [`9d7ad308bd`](https://github.com/sgl-project/sglang/commit/9d7ad308bd) [#40776](https://github.com/sgl-project/sglang/pull/40776)
  [Fix] [AMD] Quark: fix Quark block-FP8 loading in DeepSeek loader (#40776)
  _Files: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `test/registered/unit/models/test_deepseek_quark_block_fp8_loading.py`_
- **2026-10-23** [`f967418a35`](https://github.com/sgl-project/sglang/commit/f967418a35) [#46032](https://github.com/sgl-project/sglang/pull/46032)
  [Doc] cookbook: Qwen3.5 MI355X FP8 agentic adds scheduler/tokenizer tuning from the InferenceX recipe (#46032)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-10-23** [`69f830756e`](https://github.com/sgl-project/sglang/commit/69f830756e) [#46017](https://github.com/sgl-project/sglang/pull/46017)
  [Doc] cookbook: Qwen3.5 MI355X FP8 agentic uses HiCache write_through on the v0.5.22 image (#46017)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-10-23** [`0e338777b0`](https://github.com/sgl-project/sglang/commit/0e338777b0) [#45980](https://github.com/sgl-project/sglang/pull/45980)
  [Perf] dsv4: Let the fused MXFP8 producers run inside the breakable prefill graph (#45980)
  _Files: `python/sglang/srt/models/deepseek_v4_mhc.py`_
- **2026-10-22** [`bb9e9d5632`](https://github.com/sgl-project/sglang/commit/bb9e9d5632) [#45219](https://github.com/sgl-project/sglang/pull/45219)
  [Perf] mlp: Fuse dense SwiGLU with block-FP8 quantization on decode (#45219)
  _Files: `python/sglang/kernels/jit/csrc/gemm/per_token_group_quant.cuh`, `python/sglang/kernels/ops/quantization/per_token_group_quant.py`, `python/sglang/srt/layers/quantization/fp8_activation.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` _+7 more__
- **2026-10-22** [`035ed73b9d`](https://github.com/sgl-project/sglang/commit/035ed73b9d) [#45676](https://github.com/sgl-project/sglang/pull/45676)
  [Fix] [AMD] kernels: Import the HIP launch helpers from jit.utils.hipcc in smallm_fp8_blockscale_gfx950 (#45676)
  _Files: `python/sglang/kernels/ops/gemm/smallm_fp8_blockscale_gfx950/__init__.py`_
- **2026-10-22** [`f9b7225f2e`](https://github.com/sgl-project/sglang/commit/f9b7225f2e) [#45903](https://github.com/sgl-project/sglang/pull/45903)
  [Perf] dsv4: Use the fused MXFP8 producers in eager prefill (#45903)
  _Files: `python/sglang/srt/models/deepseek_v4_mhc.py`_
- **2026-10-22** [`698fa949ec`](https://github.com/sgl-project/sglang/commit/698fa949ec) [#42758](https://github.com/sgl-project/sglang/pull/42758)
  [Perf] diffusion: fuse FLUX3 SwiGLU with rowwise FP8 quantization (#42758)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/quantization/swiglu_fp8_rowwise_triton.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux3.py` _+3 more__
- **2026-10-22** [`b5137693a5`](https://github.com/sgl-project/sglang/commit/b5137693a5) [#45304](https://github.com/sgl-project/sglang/pull/45304)
  [Fix] [AMD] diffusion: Enable `--quantization fp8` on gfx1250 (torch.compile lowering + per-channel weight scales) (#45304)
  _Files: `python/sglang/kernels/ops/gemm/fp8_gfx1250.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/fp8.py`, `python/sglang/srt/environ.py`, `test/registered/amd/test_fp8_gemm_gfx1250.py`_
- **2026-10-22** [`3472e16f96`](https://github.com/sgl-project/sglang/commit/3472e16f96) [#45706](https://github.com/sgl-project/sglang/pull/45706)
  [Refactor] diffusion: remove the deprecated kitchen_int8 alias (#45706)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/comfyui.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/__init__.py` _+7 more__
- **2026-10-22** [`1962cbeebe`](https://github.com/sgl-project/sglang/commit/1962cbeebe) [#44179](https://github.com/sgl-project/sglang/pull/44179)
  [Perf] diffusion: convrot_int8 comfy_kitchen issues one GEMM per layer by default (#44179)
  _Files: `docs/docs/sglang-diffusion/environment_variables.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/convrot_int8_comfy_kitchen.py`_
- **2026-10-22** [`aa10927271`](https://github.com/sgl-project/sglang/commit/aa10927271) [#45632](https://github.com/sgl-project/sglang/pull/45632)
  [Perf] dsv41: Mega-mHC and the wo_a einsum write MXFP8 for wqkv_a and wo_b (#45632)
  _Files: `python/sglang/kernels/ops/layernorm/mhc_mega.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` _+5 more__
- **2026-10-21** [`ed89693c4a`](https://github.com/sgl-project/sglang/commit/ed89693c4a) [#45633](https://github.com/sgl-project/sglang/pull/45633)
  [Perf] dsv41: Fuse the q_norm MXFP8 quantize for wq_b at every row count (#45633)
  _Files: `python/sglang/kernels/ops/layernorm/rmsnorm_mxfp8.py`, `python/sglang/kernels/ops/quantization/mxfp8_epilogue.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-21** [`f5eca05b05`](https://github.com/sgl-project/sglang/commit/f5eca05b05) [#45585](https://github.com/sgl-project/sglang/pull/45585)
  [Fix] [SM100] quantization: Honor `deep_gemm` for 32x32 block-FP8 linears (#45585)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/registered/unit/layers/deep_gemm_wrapper/test_warmup_memory.py`_
- **2026-10-21** [`028de2c5d4`](https://github.com/sgl-project/sglang/commit/028de2c5d4) [#45630](https://github.com/sgl-project/sglang/pull/45630)
  [Perf] dsv41: Use tuned MXFP8 tactics at decode sizes (#45630)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/layers/quantization/test_fp8_blockwise_linear_backends.py`_
- **2026-10-21** [`6e98c84c60`](https://github.com/sgl-project/sglang/commit/6e98c84c60) [#39598](https://github.com/sgl-project/sglang/pull/39598)
  [Perf] [AMD] quark: Add opt-in AITER ASM FP4 GEMM for Quark dense linear (#39598)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py`_
- **2026-10-21** [`7a632cf998`](https://github.com/sgl-project/sglang/commit/7a632cf998) [#42689](https://github.com/sgl-project/sglang/pull/42689)
  [Fix] quantization: Preserve BF16 NaNs in per-token FP8 quantization (#42689)
  _Files: `python/sglang/kernels/jit/csrc/gemm/per_token_group_quant.cuh`, `test/registered/kernels/ops/quantization/test_per_token_group_quant.py`_
- **2026-10-21** [`fee32a5c1f`](https://github.com/sgl-project/sglang/commit/fee32a5c1f) [#44865](https://github.com/sgl-project/sglang/pull/44865)
  [Feat] ComfyUI: Add online INT8 quantization for BF16 Qwen-Image-2.1 single files (#44865)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/README.md`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/preflight.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/options.py`, `python/sglang/multimodal_gen/runtime/loader/comfyui_checkpoints/spec.py` _+3 more__
- **2026-10-21** [`844d2b5dec`](https://github.com/sgl-project/sglang/commit/844d2b5dec) [#32745](https://github.com/sgl-project/sglang/pull/32745)
  [Fix] [NPU] qwen3.5: Fix dense serving on Ascend 950 (#32745)
  _Files: `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/layers/quantization/modelslim/schemes/modelslim_mxfp8.py` _+5 more__
- **2026-10-21** [`956b9a24ee`](https://github.com/sgl-project/sglang/commit/956b9a24ee) [#42229](https://github.com/sgl-project/sglang/pull/42229)
  [Perf] [AMD] qwen3.5: Fuse activation quant into small-M FP8 block-scale GEMM on gfx950 (#42229)
  _Files: `python/sglang/kernels/ops/gemm/smallm_fp8_blockscale_gfx950/__init__.py`, `python/sglang/kernels/ops/gemm/smallm_fp8_blockscale_gfx950/smallm_fp8_blockscale_gemm.hip`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/registered/amd/test_smallm_fp8_blockscale_gfx950.py`_
- **2026-10-20** [`533020b500`](https://github.com/sgl-project/sglang/commit/533020b500) [#45123](https://github.com/sgl-project/sglang/pull/45123)
  [Perf] [AMD] dsv41: run gfx950 MXFP8 dense GEMMs on aiter's preshuffled FlyDSL kernel (#45123)
  _Files: `python/sglang/kernels/ops/gemm/mxfp8_aiter_gfx95.py`, `python/sglang/kernels/ops/speculative/dspark/dspark_draft_model.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/fp8_hip.py` _+1 more__
- **2026-10-20** [`eae134d61f`](https://github.com/sgl-project/sglang/commit/eae134d61f) [#45368](https://github.com/sgl-project/sglang/pull/45368)
  [Test] kernels: Import silu_and_mul_contig_post_quant from its new home (#45368)
  _Files: `test/registered/kernels/ops/quantization/test_per_token_group_quant.py`_
- **2026-10-20** [`407bfc94f9`](https://github.com/sgl-project/sglang/commit/407bfc94f9) [#44599](https://github.com/sgl-project/sglang/pull/44599)
  [Test] [AMD] diffusion: Make multimodal_gen unit tests ROCm-aware (#44599)
  _Files: `python/sglang/multimodal_gen/test/unit/test_flux3_image_dit_quant.py`, `python/sglang/multimodal_gen/test/unit/test_flux3_prims_ts_config.py`, `python/sglang/multimodal_gen/test/unit/test_kandinsky6_layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_moss_image_parallel.py` _+3 more__
- **2026-10-20** [`fdd53418a0`](https://github.com/sgl-project/sglang/commit/fdd53418a0) [#45308](https://github.com/sgl-project/sglang/pull/45308)
  [CI] [NVIDIA] gb300: Drop Kimi-K2.5 and Qwen3.5 nightly tests (#45308)
  _Files: `test/registered/gb300/test_kimi_k25_nvfp4_dp.py`, `test/registered/gb300/test_kimi_k25_nvfp4_tp.py`, `test/registered/gb300/test_qwen35_fp8_dp.py`, `test/registered/gb300/test_qwen35_fp8_tp.py`_
- **2026-10-20** [`3c07ff2654`](https://github.com/sgl-project/sglang/commit/3c07ff2654) [#40052](https://github.com/sgl-project/sglang/pull/40052)
  [Perf] [XPU] fp8: Optimize FP8 scale layouts (#40052)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/registered/e2e/xpu/test_xpu_fp8_linear.py`_
- **2026-10-19** [`806e7423af`](https://github.com/sgl-project/sglang/commit/806e7423af) [#44618](https://github.com/sgl-project/sglang/pull/44618)
  [Perf] deepseek_v4: size the masked silu-mul-quant grid to the GPU, not the padded capacity (#44618)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/silu_and_mul_masked_post_quant.cuh`, `test/registered/kernels/ops/quantization/test_per_token_group_quant.py`_
- **2026-10-19** [`417606527d`](https://github.com/sgl-project/sglang/commit/417606527d) [#44500](https://github.com/sgl-project/sglang/pull/44500)
  [Fix] nvfp4: Own streamed tensors while waiting for paired weights (#44500)
  _Files: `python/sglang/srt/layers/quantization/nvfp4_online.py`, `python/sglang/srt/model_loader/weight_utils.py`, `test/registered/unit/layers/quantization/test_nvfp4_online_weight_loader.py`_

## Other  (30 commits)

- **2026-10-26** [`c23f1ccce1`](https://github.com/sgl-project/sglang/commit/c23f1ccce1) [#46570](https://github.com/sgl-project/sglang/pull/46570)
  [Test] hicache: Accept session_ids in the L3 object-layout test's put stubs (#46570)
  _Files: `test/registered/hicache/test_hicache_l3_object_layout.py`_
- **2026-10-26** [`3ab4b62b0c`](https://github.com/sgl-project/sglang/commit/3ab4b62b0c) [#39772](https://github.com/sgl-project/sglang/pull/39772)
  [Test] [NPU] return-input-ids: Add e2e test for --return-input-ids parameter (#39772)
  _Files: `test/registered/npu/basic_function/api_related/test_npu_return_input_ids.py`_
- **2026-10-25** [`39b54ae0ee`](https://github.com/sgl-project/sglang/commit/39b54ae0ee) [#46463](https://github.com/sgl-project/sglang/pull/46463)
  [Fix] [NVIDIA] dist: Detect MNNVL fabric devices by NVML fabric state, not only by GB200/GB300 name (#46463)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-10-25** [`5066fbbfec`](https://github.com/sgl-project/sglang/commit/5066fbbfec) [#46260](https://github.com/sgl-project/sglang/pull/46260)
  [Fix] sgl-router: Bump tokio for RUSTSEC-2026-0386 (#46260)
  _Files: `sgl-router/Cargo.lock`_
- **2026-10-23** [`30dc2f9430`](https://github.com/sgl-project/sglang/commit/30dc2f9430) [#45982](https://github.com/sgl-project/sglang/pull/45982)
  [Feat] benchmark: Add --input-len-list to bench_one_batch_server for per-request input lengths (#45982)
  _Files: `python/sglang/benchmark/one_batch_server.py`_
- **2026-10-23** [`86933b1f33`](https://github.com/sgl-project/sglang/commit/86933b1f33) [#45857](https://github.com/sgl-project/sglang/pull/45857)
  [Fix] deps: Pin python-dateutil<3 to keep botocore resolvable (#45857)
  _Files: `python/pyproject.toml`_
- **2026-10-23** [`3f36fc0833`](https://github.com/sgl-project/sglang/commit/3f36fc0833) [#41213](https://github.com/sgl-project/sglang/pull/41213)
  [Fix] [XPU] runtime: Fix XPU rotary embeddings and tokenizer padding (#41213)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/utils/patch_tokenizer.py`, `test/registered/unit/utils/test_patch_tokenizer.py`_
- **2026-10-23** [`92e57d5de7`](https://github.com/sgl-project/sglang/commit/92e57d5de7) [#44692](https://github.com/sgl-project/sglang/pull/44692)
  [Perf] request_logger: skip per-token watermark redaction walk (#44692)
  _Files: `python/sglang/srt/sampling/watermarking/core.py`, `python/sglang/srt/utils/request_logger.py`, `test/registered/unit/utils/test_request_logger_redaction.py`_
- **2026-10-22** [`77f90ade97`](https://github.com/sgl-project/sglang/commit/77f90ade97) [#45918](https://github.com/sgl-project/sglang/pull/45918)
  [Fix] weight_checker: Make the checksum device-agnostic (#45918)
  _Files: `python/sglang/srt/utils/weight_checker.py`, `test/registered/unit/utils/test_weight_checker_cpu.py`_
- **2026-10-22** [`786cdfc040`](https://github.com/sgl-project/sglang/commit/786cdfc040) [#43216](https://github.com/sgl-project/sglang/pull/43216)
  [Fix] nccl: Disable graph buffer registration whenever a captured graph can hold a collective (#43216)
  _Files: `python/sglang/srt/arg_groups/parallel_hook.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-10-22** [`d67d1ae02c`](https://github.com/sgl-project/sglang/commit/d67d1ae02c) [#45855](https://github.com/sgl-project/sglang/pull/45855)
  [Fix] logits: Preserve lm_head precision with shared buffers (#45855)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `test/registered/rl/test_fp32_lm_head.py`_
- **2026-10-22** [`80263b5580`](https://github.com/sgl-project/sglang/commit/80263b5580) [#45696](https://github.com/sgl-project/sglang/pull/45696)
  [Fix] sgl-router: Do not abort forwarded requests on reqwest's default 30 s TCP_USER_TIMEOUT (#45696)
  _Files: `sgl-router/src/proxy/mod.rs`, `sgl-router/tests/proxy/timeout.rs`_
- **2026-10-22** [`4049941a82`](https://github.com/sgl-project/sglang/commit/4049941a82) [#39609](https://github.com/sgl-project/sglang/pull/39609)
  [Fix] [NPU] scope: fix dtype error in sampling backend ascend (#39609)
  _Files: `python/sglang/srt/layers/sampler.py`_
- **2026-10-22** [`eacd0a07d7`](https://github.com/sgl-project/sglang/commit/eacd0a07d7) [#40900](https://github.com/sgl-project/sglang/pull/40900)
  [Feat] bench: support --tokenize-prompt for generated-shared-prefix (#40900)
  _Files: `python/sglang/benchmark/datasets/common.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `python/sglang/benchmark/serving.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`_
- **2026-10-21** [`3438ed660d`](https://github.com/sgl-project/sglang/commit/3438ed660d) [#45672](https://github.com/sgl-project/sglang/pull/45672)
  [Test] cpu: prune mirror and tautology cases from the per-commit CPU suite (#45672)
- **2026-10-21** [`ed1f56fead`](https://github.com/sgl-project/sglang/commit/ed1f56fead) [#45419](https://github.com/sgl-project/sglang/pull/45419)
  [Fix] [Apple] mlx: Give the stub model a shared-expert layout (#45419)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_runner_pool_contract.py`_
- **2026-10-21** [`68623cae92`](https://github.com/sgl-project/sglang/commit/68623cae92) [#45670](https://github.com/sgl-project/sglang/pull/45670)
  [Fix] test: Gather Mamba track indices from `track_position` in the mixed-batch track test (#45670)
  _Files: `test/registered/unit/managers/test_mix_with_running_mamba_track.py`_
- **2026-10-21** [`a2e4ffbcea`](https://github.com/sgl-project/sglang/commit/a2e4ffbcea) [#43941](https://github.com/sgl-project/sglang/pull/43941)
  [Fix] parser: Accept whole-number floats for integer tool arguments (#43941)
  _Files: `python/sglang/srt/parser/chat_parsing/response_parser.py`, `test/registered/unit/parser/test_chat_parsing.py`_
- **2026-10-21** [`dd9ea06c00`](https://github.com/sgl-project/sglang/commit/dd9ea06c00) [#45606](https://github.com/sgl-project/sglang/pull/45606)
  [Fix] rust: Format health probe handle setup (#45606)
  _Files: `rust/sglang-server/src/api_server/core/handle.rs`_
- **2026-10-21** [`43a3f956cb`](https://github.com/sgl-project/sglang/commit/43a3f956cb) [#45502](https://github.com/sgl-project/sglang/pull/45502)
  [Fix] sgl-router: Wait for the detached PD prefill in routing tests (#45502)
  _Files: `sgl-router/tests/proxy/bucket_routing.rs`, `sgl-router/tests/proxy/chat_routing/reorg.rs`_
- **2026-10-21** [`8bd6aa9a6c`](https://github.com/sgl-project/sglang/commit/8bd6aa9a6c) [#40478](https://github.com/sgl-project/sglang/pull/40478)
  [Feat] parser: Enrich chat_parsing streaming events (#40478)
  _Files: `python/sglang/srt/parser/chat_parsing/content_parsers.py`, `python/sglang/srt/parser/chat_parsing/response_parser.py`, `test/registered/unit/parser/test_chat_parsing.py`_
- **2026-10-21** [`cd61db49c7`](https://github.com/sgl-project/sglang/commit/cd61db49c7) [#45526](https://github.com/sgl-project/sglang/pull/45526)
  [Fix] sgl-router: Bump rustls-webpki and webpki-roots for emSign advisories (#45526)
  _Files: `sgl-router/Cargo.lock`, `sgl-router/deny.toml`_
- **2026-10-21** [`aba892fbdf`](https://github.com/sgl-project/sglang/commit/aba892fbdf) [#45414](https://github.com/sgl-project/sglang/pull/45414)
  [Refactor] sgl-router: Move experimental/sgl-router to top-level sgl-router (#45414)
- **2026-10-20** [`f1eec1232d`](https://github.com/sgl-project/sglang/commit/f1eec1232d) [#44991](https://github.com/sgl-project/sglang/pull/44991)
  [Fix] config: Preserve ServerArgs positional constructor slots (#44991)
  _Files: `python/sglang/srt/arg_groups/field_order.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-10-20** [`f0b6590722`](https://github.com/sgl-project/sglang/commit/f0b6590722) [#45433](https://github.com/sgl-project/sglang/pull/45433)
  [Fix] DSpark: Disable simulated acceptance shortcuts by default (#45433)
  _Files: `python/sglang/srt/environ.py`_
- **2026-10-20** [`df13d5dce3`](https://github.com/sgl-project/sglang/commit/df13d5dce3) [#45103](https://github.com/sgl-project/sglang/pull/45103)
  [Feat] sgl-router: Route prefill buckets by uncached tokens (#45103)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/policies/buckets.rs`, `experimental/sgl-router/src/policies/cache_aware.rs` _+4 more__
- **2026-10-20** [`c53b98d1fe`](https://github.com/sgl-project/sglang/commit/c53b98d1fe) [#45172](https://github.com/sgl-project/sglang/pull/45172)
  [Fix] test-utils: Allow expected server exits in canary tests (#45172)
  _Files: `python/sglang/test/test_utils.py`, `test/registered/kv_canary/test_self_e2e_perturb_raise.py`_
- **2026-10-19** [`4ef9765e76`](https://github.com/sgl-project/sglang/commit/4ef9765e76) [#45102](https://github.com/sgl-project/sglang/pull/45102)
  [Feat] sgl-router: Add --pd-stream-after-prefill (#45102)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/server/routes/chat/forward.rs`_
- **2026-10-19** [`62cee1b15c`](https://github.com/sgl-project/sglang/commit/62cee1b15c) [#45100](https://github.com/sgl-project/sglang/pull/45100)
  [Fix] sgl-router: Keep the kv-indexer connection through bursts of cancelled prefix queries (#45100)
  _Files: `experimental/sgl-router/sgl-kv-indexer/src/client.rs`, `experimental/sgl-router/sgl-kv-indexer/src/service.rs`_
- **2026-10-19** [`0025f93944`](https://github.com/sgl-project/sglang/commit/0025f93944) [#45120](https://github.com/sgl-project/sglang/pull/45120)
  [Fix] sgl-router: Refuse prefill workers that cannot compute before bootstrap under --decode-dispatch-limit (#45120)
  _Files: `experimental/sgl-router/REFERENCE.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/workers/introspect.rs`, `experimental/sgl-router/src/workers/manager.rs`_

## CI / Build  (27 commits)

- **2026-10-26** [`9f6678aa3d`](https://github.com/sgl-project/sglang/commit/9f6678aa3d) [#45830](https://github.com/sgl-project/sglang/pull/45830)
  [Fix] ci: Add executable entry point to Muse Spark router test (#45830)
- **2026-10-26** [`fb40bdcff3`](https://github.com/sgl-project/sglang/commit/fb40bdcff3) [#46481](https://github.com/sgl-project/sglang/pull/46481)
  [Chore] ci: Update test est_time values (#46481)
- **2026-10-26** [`ccfb2b3207`](https://github.com/sgl-project/sglang/commit/ccfb2b3207) [#46558](https://github.com/sgl-project/sglang/pull/46558)
  [CI] [NPU] workflow: Fix indentation of branches filter in pr-test-npu.yml (#46558)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-10-26** [`f3a86ef2bc`](https://github.com/sgl-project/sglang/commit/f3a86ef2bc) [#46533](https://github.com/sgl-project/sglang/pull/46533)
  [CI] deepep: Add release workflow for sgl-deep-ep-v25 (DeepEP 2.5) (#46533)
  _Files: `.github/workflows/release-whl-deepep-v25.yml`, `docker/sgl-deep-ep-v25.Dockerfile`, `scripts/build_sgl_deepep_v25.sh`, `scripts/update_deepep_whl_index.py`_
- **2026-10-23** [`2a46e32fbc`](https://github.com/sgl-project/sglang/commit/2a46e32fbc) [#46055](https://github.com/sgl-project/sglang/pull/46055)
  [CI] [NPU] precise-test: skip recommend-tests-from-coverage when no NPU paths changed (#46055)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-10-23** [`0347b2bb4e`](https://github.com/sgl-project/sglang/commit/0347b2bb4e) [#46042](https://github.com/sgl-project/sglang/pull/46042)
  [CI] [NPU] precise-test: gate precision on PR judgeability, not bucket count (#46042)
  _Files: `.github/workflows/pr-test-npu.yml`, `scripts/ci/npu/precise-test/bucket_recommended_tests.py`_
- **2026-10-23** [`2be6577ba9`](https://github.com/sgl-project/sglang/commit/2be6577ba9) [#45991](https://github.com/sgl-project/sglang/pull/45991)
  [Doc] beam: Offer Python and Docker commands in the cookbook (#45991)
  _Files: `docs/cookbook/autoregressive/Reflection/Beam-1_0.mdx`, `docs/src/snippets/configs/reflection/beam-1.0.jsx`_
- **2026-10-23** [`79eb10e182`](https://github.com/sgl-project/sglang/commit/79eb10e182) [#45920](https://github.com/sgl-project/sglang/pull/45920)
  [CI] [NVIDIA] gb300: Restore the aarch64 rust-ext cache on ARM runners (#45920)
  _Files: `.github/actions/download-rust-ext/action.yml`_
- **2026-10-23** [`ce2261863f`](https://github.com/sgl-project/sglang/commit/ce2261863f) [#45571](https://github.com/sgl-project/sglang/pull/45571)
  [CI] [NPU] precise-test: add empty-recommendation skip-all rule, slim baseline artifacts, and move setup-covstub off the NPU pool (#45571)
  _Files: `.github/workflows/coverage-collection-npu.yml`, `.github/workflows/pr-test-npu.yml`, `scripts/ci/npu/precise-test/bucket_recommended_tests.py`, `scripts/ci/npu/precise-test/coveragerc` _+1 more__
- **2026-10-22** [`8d47d515e4`](https://github.com/sgl-project/sglang/commit/8d47d515e4) [#45910](https://github.com/sgl-project/sglang/pull/45910)
  [CI] deepgemm: Remove obsolete ref_mhc preflight check (#45910)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-10-22** [`a904e4d31a`](https://github.com/sgl-project/sglang/commit/a904e4d31a) [#45873](https://github.com/sgl-project/sglang/pull/45873)
  [Fix] ci: Reduce runner utilization scan overhead and bound API retries (#45873)
  _Files: `.github/workflows/runner-utilization.yml`, `scripts/ci/utils/runner_utilization_report.py`, `scripts/ci/utils/test_runner_utilization_report.py`_
- **2026-10-22** [`8d8916815b`](https://github.com/sgl-project/sglang/commit/8d8916815b) [#45843](https://github.com/sgl-project/sglang/pull/45843)
  [Fix] ci: Add pytest entry point for Muse Spark router tests (#45843)
- **2026-10-22** [`9ec74a53cc`](https://github.com/sgl-project/sglang/commit/9ec74a53cc) [#45521](https://github.com/sgl-project/sglang/pull/45521)
  [Fix] [NVIDIA] docker: Build sgl-deep-gemm 0.2.3 for cu134 to match the sglang pin (#45521)
  _Files: `.pre-commit-config.yaml`, `docker/Dockerfile.cu134`, `scripts/lint/check_dockerfile_wheel_pins.py`_
- **2026-10-21** [`7554be5a69`](https://github.com/sgl-project/sglang/commit/7554be5a69) [#45564](https://github.com/sgl-project/sglang/pull/45564)
  [CI] codeowners: Add owners for the top-level sgl-router (#45564)
  _Files: `.github/CODEOWNERS`_
- **2026-10-21** [`c3b2b55bbb`](https://github.com/sgl-project/sglang/commit/c3b2b55bbb) [#45374](https://github.com/sgl-project/sglang/pull/45374)
  [CI] [NPU] precise-test: add recommendation summary & run artifacts, fix NPU-only coverage view, and quiet benign teardown noise (#45374)
  _Files: `.github/workflows/pr-test-npu.yml`, `scripts/ci/npu/precise-test/bucket_recommended_tests.py`, `scripts/ci/npu/precise-test/precise_test_coverage_plugin.py`, `scripts/ci/npu/precise-test/run_tests_with_coverage.sh`_
- **2026-10-21** [`574f9cdb2e`](https://github.com/sgl-project/sglang/commit/574f9cdb2e) [#45501](https://github.com/sgl-project/sglang/pull/45501)
  [CI] slash-command: Add /run-cpu-ci to run only the CPU unit suite (#45501)
  _Files: `.agents/skills/ci-workflow-guide/SKILL.md`, `.github/FOLDER_README.md`, `.github/workflows/_pr-test-stage-cpu.yml`, `.github/workflows/run-cpu-ci.yml` _+3 more__
- **2026-10-20** [`b008ec3de6`](https://github.com/sgl-project/sglang/commit/b008ec3de6) [#45454](https://github.com/sgl-project/sglang/pull/45454)
  [CI] muse_spark: Move unified memory test to B300 (#45454)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/rerun-test.yml`, `test/registered/e2e/models/test_muse_spark_unified_memory.py`_
- **2026-10-20** [`583cfc4d55`](https://github.com/sgl-project/sglang/commit/583cfc4d55) [#45428](https://github.com/sgl-project/sglang/pull/45428)
  [CI] muse_spark: Use complete local checkpoints in model tests (#45428)
  _Files: `python/sglang/test/muse_spark_utils.py`, `test/registered/e2e/models/test_muse_spark_12_b300_pd.py`, `test/registered/e2e/models/test_muse_spark_unified_memory.py`_
- **2026-10-20** [`952c63b1bb`](https://github.com/sgl-project/sglang/commit/952c63b1bb) [#45383](https://github.com/sgl-project/sglang/pull/45383)
  [CI] sgl-router: Gate on live run-ci label so /tag-and-rerun-ci can start the tiers (#45383)
  _Files: `.github/workflows/pr-test-sgl-router.yml`_
- **2026-10-20** [`06314dc2e8`](https://github.com/sgl-project/sglang/commit/06314dc2e8) [#45281](https://github.com/sgl-project/sglang/pull/45281)
  [CI] [Intel] tests: Remove CPU monitor and crash-dump tests from Xeon CI (#45281)
  _Files: `test/registered/debug_utils/test_crash_dump.py`, `test/registered/unit/observability/test_cpu_monitor.py`_
- **2026-10-20** [`553836c164`](https://github.com/sgl-project/sglang/commit/553836c164) [#44299](https://github.com/sgl-project/sglang/pull/44299)
  [Feat] simulator: Add baseline collection and ML latency predictor training tools (#44299)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/_pr-test-simulator-cpu.yml`, `.github/workflows/_pr-test-simulator-gpu.yml`, `.github/workflows/pr-test-extra.yml` _+16 more__
- **2026-10-19** [`642a671c30`](https://github.com/sgl-project/sglang/commit/642a671c30) [#44975](https://github.com/sgl-project/sglang/pull/44975)
  [CI] tests: Re-enable muse spark B300 PD coverage (#44975)
  _Files: `test/registered/e2e/models/test_muse_spark_12_b300_pd.py`_
- **2026-10-19** [`716c9151f2`](https://github.com/sgl-project/sglang/commit/716c9151f2) [#44019](https://github.com/sgl-project/sglang/pull/44019)
  [CI] [NPU] npu-coverage: run only coverage-recommended tests on PRs (precise test selection) (#44019)
  _Files: `.github/workflows/_npu-analyze-failure.yml`, `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/coverage-collection-npu.yml` _+8 more__
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

## Triton / Kernels  (20 commits)

- **2026-10-26** [`e1c4b273af`](https://github.com/sgl-project/sglang/commit/e1c4b273af) [#46546](https://github.com/sgl-project/sglang/pull/46546)
  [Doc] cookbook: MiniMax-M3.1 GB200 recipes and B200 Low-Latency (MonoKernel) (#46546)
  _Files: `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`_
- **2026-10-24** [`49a2fbf817`](https://github.com/sgl-project/sglang/commit/49a2fbf817) [#46030](https://github.com/sgl-project/sglang/pull/46030)
  [Fix] docker: Pin sgl-nvidia-mega to 3333e4c so the megakernel starts on main (#46030)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`_
- **2026-10-24** [`79e5c4bb9b`](https://github.com/sgl-project/sglang/commit/79e5c4bb9b) [#46176](https://github.com/sgl-project/sglang/pull/46176)
  [Perf] dsv41: Trim per-step DSpark decode overhead (#46176)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`, `python/sglang/srt/layers/aux_hidden_states.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_dspark.py` _+3 more__
- **2026-10-23** [`f05ad5ec01`](https://github.com/sgl-project/sglang/commit/f05ad5ec01) [#46167](https://github.com/sgl-project/sglang/pull/46167)
  [Perf] logits: Cast bf16 logits into the fp32 buffer with a Triton kernel (#46167)
  _Files: `python/sglang/kernels/ops/activation/__init__.py`, `python/sglang/kernels/ops/activation/softcap.py`, `python/sglang/srt/layers/logits_processor.py`_
- **2026-10-23** [`2da6c0c237`](https://github.com/sgl-project/sglang/commit/2da6c0c237) [#45940](https://github.com/sgl-project/sglang/pull/45940)
  [Perf] dsv4: Combine the final mHC streams from bf16 without an fp32 copy (#45940)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-22** [`5849ff5337`](https://github.com/sgl-project/sglang/commit/5849ff5337) [#45911](https://github.com/sgl-project/sglang/pull/45911)
  [Fix] [NVIDIA] jit: Build sm_100f on CC 10.7 until the bundled CUTLASS supports SM107 (#45911)
  _Files: `python/sglang/kernels/jit/utils/arch.py`_
- **2026-10-22** [`ba83415eea`](https://github.com/sgl-project/sglang/commit/ba83415eea) [#45879](https://github.com/sgl-project/sglang/pull/45879)
  [Perf] engram: Read host-table rows in address order on GPUs without host page tables (#45879)
  _Files: `python/sglang/kernels/ops/embeddings/engram_gather.py`, `python/sglang/srt/layers/engram.py`_
- **2026-10-22** [`913e91ed51`](https://github.com/sgl-project/sglang/commit/913e91ed51) [#45845](https://github.com/sgl-project/sglang/pull/45845)
  [Fix] CI: add missing entry point to Muse Spark router test (#45845)
  _Files: `test/registered/kernels/ops/gemm/test_muse_spark_router_gemv_cutedsl.py`_
- **2026-10-22** [`851419717a`](https://github.com/sgl-project/sglang/commit/851419717a) [#45508](https://github.com/sgl-project/sglang/pull/45508)
  [Perf] [KDA] muse_spark: Run the one-token router GEMV on CuTe DSL (#45508)
  _Files: `python/sglang/kernels/ops/gemm/__init__.py`, `python/sglang/kernels/ops/gemm/muse_spark_router_gemv_cutedsl.py`, `python/sglang/srt/models/muse_spark.py`, `test/registered/kernels/ops/gemm/test_muse_spark_router_gemv_cutedsl.py` _+1 more__
- **2026-10-22** [`178febef5d`](https://github.com/sgl-project/sglang/commit/178febef5d) [#45214](https://github.com/sgl-project/sglang/pull/45214)
  [Perf] qknorm: run head_dim-128 rows two per warp with 16B lanes, bit-identical (#45214)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/qknorm.cuh`, `python/sglang/kernels/ops/layernorm/norm.py`, `test/registered/kernels/ops/layernorm/test_qknorm.py`_
- **2026-10-22** [`569dda1e61`](https://github.com/sgl-project/sglang/commit/569dda1e61) [#45288](https://github.com/sgl-project/sglang/pull/45288)
  [CI] [NPU] npu: Update SGLang kernel tag to 2026.9.0.post10 (#45288)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `docker/npu.Dockerfile`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-10-21** [`7e5d3780ef`](https://github.com/sgl-project/sglang/commit/7e5d3780ef) [#45593](https://github.com/sgl-project/sglang/pull/45593)
  [Fix] [NPU] tests: Run the HiCache Mamba case with bfloat16 SSM kernels (#45593)
  _Files: `test/registered/npu/basic_function/HiCache/test_npu_hicache_mamba.py`_
- **2026-10-21** [`a175e39b84`](https://github.com/sgl-project/sglang/commit/a175e39b84) [#45557](https://github.com/sgl-project/sglang/pull/45557)
  [CI] cuda: Rebuild workspace crates when the shared Cargo target dir came from another rust/ tree (#45557)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-10-21** [`a361f0c410`](https://github.com/sgl-project/sglang/commit/a361f0c410) [#44886](https://github.com/sgl-project/sglang/pull/44886)
  [Fix] kda: Align graph tracking branch dtype with the recurrent state pool (#44886)
  _Files: `python/sglang/kernels/ops/mamba/kda_prefill_track.py`_
- **2026-10-20** [`b326e8349d`](https://github.com/sgl-project/sglang/commit/b326e8349d) [#45213](https://github.com/sgl-project/sglang/pull/45213)
  [Perf] mamba: Copy tracked decode states at HBM bandwidth in one persistent launch (#45213)
  _Files: `python/sglang/kernels/ops/mamba/mamba_state_scatter_triton.py`, `test/registered/unit/layers/test_mamba_track_states_triton.py`_
- **2026-10-20** [`2229345dff`](https://github.com/sgl-project/sglang/commit/2229345dff) [#45359](https://github.com/sgl-project/sglang/pull/45359)
  [Doc] kda_kernels: Point the SM121 QSA kernel provenance at its SGLang PR (#45359)
  _Files: `python/sglang/kernels/kda_kernels/README.md`, `python/sglang/kernels/kda_kernels/qwen38_qsa_sm121/README.md`, `python/sglang/kernels/kda_kernels/qwen38_qsa_sm121/__init__.py`, `python/sglang/kernels/kda_kernels/qwen38_qsa_sm121/kernel.py`_
- **2026-10-20** [`1739d962a4`](https://github.com/sgl-project/sglang/commit/1739d962a4) [#44367](https://github.com/sgl-project/sglang/pull/44367)
  [Refactor] [Apple] MLX: Use Native Extension Builder for Metal Kernels (#44367)
  _Files: `python/pyproject_other.toml`, `python/sglang/kernels/aot/csrc/metal/README.md`, `python/sglang/kernels/aot/csrc/metal/rope_pool_fused.cpp`, `python/sglang/kernels/aot/python/sgl_kernel/metal.py` _+1 more__
- **2026-10-20** [`ec1fdc22a9`](https://github.com/sgl-project/sglang/commit/ec1fdc22a9) [#45252](https://github.com/sgl-project/sglang/pull/45252)
  [Fix] [NVIDIA] docker: Fix CUDA 13.4 container by updating torch nightly (#45252)
  _Files: `docker/Dockerfile.cu134`_
- **2026-10-20** [`693d333306`](https://github.com/sgl-project/sglang/commit/693d333306) [#45112](https://github.com/sgl-project/sglang/pull/45112)
  [Refactor] kernels: Regroup operators by computation and dissolve ops/muse_spark (#45112)
- **2026-10-19** [`a5117beb11`](https://github.com/sgl-project/sglang/commit/a5117beb11) [#44906](https://github.com/sgl-project/sglang/pull/44906)
  [Perf] mhc: Parallelize small-batch post across hidden tiles (#44906)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`_

## Tensor / Data Parallel  (19 commits)

- **2026-10-26** [`52a6f7049f`](https://github.com/sgl-project/sglang/commit/52a6f7049f) [#46530](https://github.com/sgl-project/sglang/pull/46530)
  [Refactor] dsv41: Write engram hash ids and embeddings into caller-allocated prefill graph outputs (#46530)
  _Files: `python/sglang/srt/layers/engram.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-26** [`3b058f28c2`](https://github.com/sgl-project/sglang/commit/3b058f28c2) [#45950](https://github.com/sgl-project/sglang/pull/45950)
  [Refactor] [NPU] communicator: remove redundant npu communicator (#45950)
  _Files: `python/sglang/srt/distributed/device_communicators/npu_communicator.py`, `python/sglang/srt/distributed/parallel_state.py`, `test/registered/unit/distributed/test_parallel_state.py`_
- **2026-10-26** [`fef058a403`](https://github.com/sgl-project/sglang/commit/fef058a403) [#39774](https://github.com/sgl-project/sglang/pull/39774)
  [Test] [NPU] return-output-ids: Add e2e test for --return-output-ids parameter (#39774)
  _Files: `test/registered/npu/basic_function/api_related/test_npu_return_output_ids.py`_
- **2026-10-25** [`ca4bedfffa`](https://github.com/sgl-project/sglang/commit/ca4bedfffa) [#46031](https://github.com/sgl-project/sglang/pull/46031)
  [Chore] processor: use typed api output (#46031)
  _Files: `rust/Cargo.lock`, `rust/sglang-processor/Cargo.toml`, `rust/sglang-processor/README.md`, `rust/sglang-processor/src/openai/chat.rs` _+6 more__
- **2026-10-24** [`6563312956`](https://github.com/sgl-project/sglang/commit/6563312956) [#34543](https://github.com/sgl-project/sglang/pull/34543)
  [Fix] [AMD] custom-allreduce: Stop registering oversized inputs in the deterministic all-reduce (#34543)
  _Files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `test/registered/kernels/ops/communication/test_amd_deterministic_custom_allreduce.py`_
- **2026-10-23** [`855c092deb`](https://github.com/sgl-project/sglang/commit/855c092deb) [#45335](https://github.com/sgl-project/sglang/pull/45335)
  [Fix] inkling: Keep BF16 LM-head operands with FP32 output (#45335)
  _Files: `python/sglang/srt/configs/inkling.py`, `python/sglang/srt/layers/logits_processor.py`, `test/registered/kernels/ops/sampling/test_lm_head_output_dtype.py`, `test/registered/unit/configs/test_inkling_config.py`_
- **2026-10-23** [`15dc838f9b`](https://github.com/sgl-project/sglang/commit/15dc838f9b) [#45760](https://github.com/sgl-project/sglang/pull/45760)
  [Fix] http_server: Apply SGLANG_TIMEOUT_KEEP_ALIVE to Granian HTTP/1.1 connections (#45760)
  _Files: `python/sglang/srt/entrypoints/http_server.py`_
- **2026-10-23** [`baf80c61b7`](https://github.com/sgl-project/sglang/commit/baf80c61b7) [#45897](https://github.com/sgl-project/sglang/pull/45897)
  [Feat] platforms: Let out-of-tree platforms bind group devices and custom ops (#45897)
  _Files: `docs/docs/hardware-platforms/plugin.mdx`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/platforms/cuda.py`, `python/sglang/srt/platforms/interface.py` _+5 more__
- **2026-10-23** [`eb8ef80842`](https://github.com/sgl-project/sglang/commit/eb8ef80842) [#45888](https://github.com/sgl-project/sglang/pull/45888)
  [Feat] rust-server: Serve /abort_request from the Rust frontend (#45888)
  _Files: `rust/sglang-server/src/api_server/http/info.rs`_
- **2026-10-22** [`8d7df07a56`](https://github.com/sgl-project/sglang/commit/8d7df07a56) [#44726](https://github.com/sgl-project/sglang/pull/44726)
  [Feat] rust-server: Add HiCache storage management endpoints (#44726)
  _Files: `proto/sglang/api/v1/hicache.proto`, `proto/sglang/api/v1/service.proto`, `python/sglang/api/v1/api_types.py`, `python/sglang/srt/rust_server/config.py` _+17 more__
- **2026-10-22** [`5f62e23d30`](https://github.com/sgl-project/sglang/commit/5f62e23d30) [#45629](https://github.com/sgl-project/sglang/pull/45629)
  [Doc] cookbook: Add Muse Spark Open GB300 Dynamo + SGLang deployments measured with AA AgentPerf (#45629)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`_
- **2026-10-21** [`7e5256d1ba`](https://github.com/sgl-project/sglang/commit/7e5256d1ba) [#45482](https://github.com/sgl-project/sglang/pull/45482)
  [Feat] srt: Balance uvicorn tokenizer workers with per-worker SO_REUSEPORT listeners (#45482)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/pyproject.toml`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/serving.py` _+5 more__
- **2026-10-21** [`2815eed49c`](https://github.com/sgl-project/sglang/commit/2815eed49c) [#43039](https://github.com/sgl-project/sglang/pull/43039)
  [Fix] [NPU] pre_warm_nccl: init npu backend before the parallel runtime touches a device (#43039)
  _Files: `python/sglang/srt/distributed/bootstrap.py`_
- **2026-10-20** [`af856717c2`](https://github.com/sgl-project/sglang/commit/af856717c2) [#45212](https://github.com/sgl-project/sglang/pull/45212)
  [Fix] mamba: Skip zero-width conv pools in the MTP verify scatter (#45212)
  _Files: `python/sglang/kernels/ops/mamba/mamba_state_scatter_triton.py`, `test/registered/unit/layers/test_mamba_state_scatter_triton.py`_
- **2026-10-19** [`9a949403f1`](https://github.com/sgl-project/sglang/commit/9a949403f1) [#45246](https://github.com/sgl-project/sglang/pull/45246)
  [Doc] tpu: Introduce SGLang-TorchTPU in README and TPU guide (#45246)
  _Files: `README.md`, `docs/docs/hardware-platforms/tpu.mdx`_
- **2026-10-19** [`9ab74b8517`](https://github.com/sgl-project/sglang/commit/9ab74b8517) [#44150](https://github.com/sgl-project/sglang/pull/44150)
  [Fix] Qwen3.8next: Stop retaining per-size PLE outputs in breakable prefill CUDA graphs (#44150)
  _Files: `python/sglang/srt/models/qwen4_exp.py`_
- **2026-10-19** [`678913a0f0`](https://github.com/sgl-project/sglang/commit/678913a0f0) [#44689](https://github.com/sgl-project/sglang/pull/44689)
  [Feat] sgl-model-gateway: Add --decode-dispatch-limit to pick PD decode workers near KV arrival (#44689)
  _Files: `docs/docs/advanced_features/sgl_model_gateway.mdx`, `sgl-model-gateway/README.md`, `sgl-model-gateway/bindings/python/src/lib.rs`, `sgl-model-gateway/bindings/python/src/sglang_router/router.py` _+10 more__
- **2026-10-19** [`f86a04a331`](https://github.com/sgl-project/sglang/commit/f86a04a331) [#44402](https://github.com/sgl-project/sglang/pull/44402)
  [Feat] sgl-router: Add --decode-dispatch-limit to pick decode DP ranks near KV arrival (#44402)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/REFERENCE.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs` _+8 more__
- **2026-10-19** [`06342acad2`](https://github.com/sgl-project/sglang/commit/06342acad2) [#45062](https://github.com/sgl-project/sglang/pull/45062)
  [Perf] deepseek-v4.1: Stage late-layer DP row counts through pinned memory (#45062)
  _Files: `python/sglang/srt/models/deepseek_common/decoder_swa_bounded_replay.py`_

## ROCm / AMD  (18 commits)

- **2026-10-26** [`d19f19d68c`](https://github.com/sgl-project/sglang/commit/d19f19d68c) [#46453](https://github.com/sgl-project/sglang/pull/46453)
  [CI] [AMD] pr-test: list tags with ls-remote, 8 small shards (#46453)
  _Files: `.github/workflows/pr-test-amd.yml`, `scripts/ci/amd/amd_ci_start_container.sh`, `scripts/ci/amd/amd_ci_start_container_disagg.sh`, `scripts/release/get_version_tag.py`_
- **2026-10-24** [`7671d16ce8`](https://github.com/sgl-project/sglang/commit/7671d16ce8) [#46161](https://github.com/sgl-project/sglang/pull/46161)
  [Fix] [AMD] rotary: Pass a query-dtype cos_sin_cache to the HIP fallback (#46161)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`, `test/registered/unit/layers/test_rope_hip_fallback_cache_dtype.py`_
- **2026-10-23** [`bb72b47daf`](https://github.com/sgl-project/sglang/commit/bb72b47daf) [#45728](https://github.com/sgl-project/sglang/pull/45728)
  [Test] [AMD] deepseek-v4.1: Give the encoder-replay test's request window a zero_row (#45728)
  _Files: `test/registered/amd/test_dsv4_hip_bcg_metadata.py`_
- **2026-10-23** [`a95ae5f1c5`](https://github.com/sgl-project/sglang/commit/a95ae5f1c5) [#45848](https://github.com/sgl-project/sglang/pull/45848)
  [CI] [AMD] docker: Start the ROCm 10 nightly at 10:00 UTC and ROCm 7.2 at 11:00 UTC (#45848)
  _Files: `.github/workflows/release-docker-amd-rocm10.yml`, `.github/workflows/release-docker-amd-rocm720-nightly.yml`_
- **2026-10-22** [`1c967f5043`](https://github.com/sgl-project/sglang/commit/1c967f5043) [#34241](https://github.com/sgl-project/sglang/pull/34241)
  [Fix] [AMD] test: Recalibrate MiniMax-M2.7 GSM8K threshold 0.93->0.91 for MI300 runners (#34241)
  _Files: `test/registered/amd/accuracy/mi30x/test_minimax_m27_eval_amd.py`_
- **2026-10-22** [`f91b81b82a`](https://github.com/sgl-project/sglang/commit/f91b81b82a) [#45689](https://github.com/sgl-project/sglang/pull/45689)
  [Doc] [AMD] cookbook: Add Muse Spark Open MI355X AgentX recipe (#45689)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`_
- **2026-10-22** [`9ee9858805`](https://github.com/sgl-project/sglang/commit/9ee9858805) [#45693](https://github.com/sgl-project/sglang/pull/45693)
  [Doc] [AMD] dsv41: Update amd cookbook 1021 (#45693)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-10-22** [`5fff58a169`](https://github.com/sgl-project/sglang/commit/5fff58a169) [#45469](https://github.com/sgl-project/sglang/pull/45469)
  [CI] [AMD] miles: Fix the ROCm 10 nightly suites that never finish (#45469)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm10-mi30x.yml`, `.github/workflows/nightly-test-amd-miles-rocm10.yml`_
- **2026-10-21** [`51baa1f6e9`](https://github.com/sgl-project/sglang/commit/51baa1f6e9) [#45408](https://github.com/sgl-project/sglang/pull/45408)
  [Test] [AMD] debug-utils: Opt TestCrashDump into expect_server_exit (#45408)
  _Files: `test/registered/debug_utils/test_crash_dump.py`_
- **2026-10-21** [`131c42ba33`](https://github.com/sgl-project/sglang/commit/131c42ba33) [#45498](https://github.com/sgl-project/sglang/pull/45498)
  [Perf] [AMD] aiter: Update ROCm AITER pin to 285579b62 (gfx942/gfx950 only) (#45498)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-21** [`1278087336`](https://github.com/sgl-project/sglang/commit/1278087336) [#45546](https://github.com/sgl-project/sglang/pull/45546)
  [Fix] [AMD] mono-kernel: Update sgl-amd-mono version (#45546)
  _Files: `python/pyproject_other.toml`_
- **2026-10-21** [`132836b369`](https://github.com/sgl-project/sglang/commit/132836b369) [#45329](https://github.com/sgl-project/sglang/pull/45329)
  [Fix] [AMD] docker: Build Triton from source for ROCm 10.1 gfx1250 (#45329)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-20** [`9686edcf80`](https://github.com/sgl-project/sglang/commit/9686edcf80) [#45124](https://github.com/sgl-project/sglang/pull/45124)
  [Perf] [AMD] dsv41: faster mHC boundary Triton tile for 96+ rows, bitwise unchanged (#45124)
  _Files: `python/sglang/kernels/ops/layernorm/mhc_boundary_hip.py`, `python/sglang/srt/environ.py`_
- **2026-10-20** [`29274b41c6`](https://github.com/sgl-project/sglang/commit/29274b41c6) [#44198](https://github.com/sgl-project/sglang/pull/44198)
  [Fix] [AMD] activation: Run ReLU2 natively on ROCm (#44198)
  _Files: `python/sglang/srt/layers/activation.py`_
- **2026-10-20** [`7591118794`](https://github.com/sgl-project/sglang/commit/7591118794) [#45217](https://github.com/sgl-project/sglang/pull/45217)
  [Fix] [AMD] grok: accept allow_patterns_overrides in presharded _prepare_weights patch (#45217)
  _Files: `python/sglang/srt/models/grok.py`_
- **2026-10-19** [`a90e9c5dd8`](https://github.com/sgl-project/sglang/commit/a90e9c5dd8) [#44443](https://github.com/sgl-project/sglang/pull/44443)
  [Fix] [AMD] mhc: Bound the Triton fused post+pre buffer cache (#44443)
  _Files: `python/sglang/srt/models/deepseek_common/amd/deepseek_v4_fused_mhc.py`, `test/registered/unit/models/test_deepseek_v4_amd_fused_mhc.py`_
- **2026-10-19** [`5d9c956f8e`](https://github.com/sgl-project/sglang/commit/5d9c956f8e) [#45070](https://github.com/sgl-project/sglang/pull/45070)
  [Doc] [AMD] dsv4: Update amd cookbook 1016 (#45070)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-10-19** [`3d588779e1`](https://github.com/sgl-project/sglang/commit/3d588779e1) [#40674](https://github.com/sgl-project/sglang/pull/40674)
  [CI] [AMD] test: Run UMBP HiCache E2E through standalone DRAM server (#40674)
  _Files: `test/registered/hicache/test_hicache_storage_umbp_backend.py`_

## Scheduler / Batching  (15 commits)

- **2026-10-24** [`fab0e896ab`](https://github.com/sgl-project/sglang/commit/fab0e896ab) [#46074](https://github.com/sgl-project/sglang/pull/46074)
  [Fix] rust-server: Start a transfer backend's own KV bootstrap server on prefill (#46074)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/disagg_service.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/entrypoints/test_rust_server_dp_ports.py`_
- **2026-10-23** [`b588aa39e9`](https://github.com/sgl-project/sglang/commit/b588aa39e9) [#45921](https://github.com/sgl-project/sglang/pull/45921)
  [Perf] dsv4: Optionally stage V4.1 engram rows from the shared host table on the scheduler (#45921)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/engram.py`, `python/sglang/srt/layers/engram_staging.py`, `python/sglang/srt/managers/schedule_batch.py` _+4 more__
- **2026-10-22** [`67bbfcee3c`](https://github.com/sgl-project/sglang/commit/67bbfcee3c) [#45170](https://github.com/sgl-project/sglang/pull/45170)
  [Perf] [NPU] scheduler: Remove blocking seq_lens D2H from graph replay (#45170)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`_
- **2026-10-21** [`42db2db4a8`](https://github.com/sgl-project/sglang/commit/42db2db4a8) [#45460](https://github.com/sgl-project/sglang/pull/45460)
  [Fix] rust-server: Check only a client-sent max_new_tokens against the context window (#45460)
  _Files: `rust/sglang-server/src/api_server/grpc/service.rs`, `rust/sglang-server/src/api_server/http/native_api.rs`, `rust/sglang-server/src/message/request.rs`, `rust/sglang-server/src/message/wire.rs` _+2 more__
- **2026-10-21** [`a3d00eff58`](https://github.com/sgl-project/sglang/commit/a3d00eff58) [#45487](https://github.com/sgl-project/sglang/pull/45487)
  [Perf] srt: Record on the host whether an extend batch completes a prompt (#45487)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/batch_overlap/test_tbo_filter_batch_marker.py`, `test/registered/unit/layers/test_mamba_prefill_track_metadata.py` _+1 more__
- **2026-10-21** [`ca72dad953`](https://github.com/sgl-project/sglang/commit/ca72dad953) [#45475](https://github.com/sgl-project/sglang/pull/45475)
  [Fix] rust-server: Answer health probes a busy scheduler skipped on the response ring (#45475)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/rust_server/server.py`, `rust/sglang-server/src/api_server/core/handle.rs`, `rust/sglang-server/src/lib.rs` _+4 more__
- **2026-10-21** [`2c9d919071`](https://github.com/sgl-project/sglang/commit/2c9d919071) [#45437](https://github.com/sgl-project/sglang/pull/45437)
  [Fix] srt: Pin the source address of TCP ZMQ connects for the peer allowlist (#45437)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/load_snapshot.py`, `python/sglang/srt/utils/network.py`, `test/registered/unit/utils/test_network.py`_
- **2026-10-20** [`468e26f253`](https://github.com/sgl-project/sglang/commit/468e26f253) [#45280](https://github.com/sgl-project/sglang/pull/45280)
  [Perf] detokenizer: Add SGLANG_BATCH_TOKENIZER_OUTPUTS to opt out of grouped return sends (#45280)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `test/registered/unit/managers/test_multi_tokenizer_mixin.py`_
- **2026-10-20** [`194876bea0`](https://github.com/sgl-project/sglang/commit/194876bea0) [#45250](https://github.com/sgl-project/sglang/pull/45250)
  [Fix] srt: Admit only allowlisted peers on TCP-bound ZMQ IPC sockets (#45250)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/load_snapshot.py`, `python/sglang/srt/ray/data_parallel_controller.py` _+1 more__
- **2026-10-20** [`a70b1b73d3`](https://github.com/sgl-project/sglang/commit/a70b1b73d3) [#38211](https://github.com/sgl-project/sglang/pull/38211)
  [Fix] tracing: Fix OTel tracing context lost in multi-tokenizer router processes (#38211)
  _Files: `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/observability/trace.py`, `test/registered/observability/test_tracing.py`, `test/registered/unit/observability/test_trace.py`_
- **2026-10-19** [`ab258b6453`](https://github.com/sgl-project/sglang/commit/ab258b6453) [#44681](https://github.com/sgl-project/sglang/pull/44681)
  [Fix] symm-mem: Name the window registration in the scheduler watchdog dump (#44681)
  _Files: `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `test/registered/unit/distributed/test_symm_mem_registration_watchdog.py`_
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

## Speculative Decoding  (14 commits)

- **2026-10-25** [`8db75fc6d0`](https://github.com/sgl-project/sglang/commit/8db75fc6d0) [#46441](https://github.com/sgl-project/sglang/pull/46441)
  [Fix] mlx: Accept draft_parallel_layout in the stub's alloc_memory_pool (#46441)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`_
- **2026-10-24** [`a7183a8246`](https://github.com/sgl-project/sglang/commit/a7183a8246) [#45145](https://github.com/sgl-project/sglang/pull/45145)
  [Feat] spec: Let out-of-tree platforms provide EAGLE draft graph runners (#45145)
  _Files: `docs/docs/hardware-platforms/plugin.mdx`, `python/sglang/srt/platforms/interface.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/unit/spec/test_oot_eagle_hooks.py`_
- **2026-10-24** [`af3f9e4c8f`](https://github.com/sgl-project/sglang/commit/af3f9e4c8f) [#45144](https://github.com/sgl-project/sglang/pull/45144)
  [Feat] spec: Let out-of-tree platforms provide their own speculative worker (#45144)
  _Files: `docs/docs/hardware-platforms/plugin.mdx`, `python/sglang/kernels/ops/speculative/spec_tree.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/platforms/interface.py` _+3 more__
- **2026-10-24** [`5994c5597d`](https://github.com/sgl-project/sglang/commit/5994c5597d) [#41169](https://github.com/sgl-project/sglang/pull/41169)
  [Perf] spec-decoding: fuse simulated speculative acceptance tensor preparation (#41169)
  _Files: `python/sglang/kernels/ops/speculative/__init__.py`, `python/sglang/kernels/ops/speculative/simulated_accept.py`, `python/sglang/srt/speculative/spec_utils.py`_
- **2026-10-23** [`49933325cc`](https://github.com/sgl-project/sglang/commit/49933325cc) [#45964](https://github.com/sgl-project/sglang/pull/45964)
  [Perf] dspark: Combine the draft's mHC streams from bf16 without an fp32 copy (#45964)
  _Files: `python/sglang/srt/models/deepseek_v4_dspark.py`_
- **2026-10-22** [`c394a90c2b`](https://github.com/sgl-project/sglang/commit/c394a90c2b) [#45771](https://github.com/sgl-project/sglang/pull/45771)
  [Perf] gemma4: Capture single-step frozen-KV drafts (#45771)
  _Files: `python/sglang/srt/speculative/frozen_kv_mtp_worker_v2.py`_
- **2026-10-22** [`25ad569ff9`](https://github.com/sgl-project/sglang/commit/25ad569ff9) [#33395](https://github.com/sgl-project/sglang/pull/33395)
  [Feat] speculative: Seed rejection-sampling draft proposals for deterministic inference (#33395)
  _Files: `benchmark/kernels/sampling/bench_deterministic_fast_sample.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_utils.py` _+10 more__
- **2026-10-22** [`d61f618276`](https://github.com/sgl-project/sglang/commit/d61f618276) [#45682](https://github.com/sgl-project/sglang/pull/45682)
  [Perf] spec: Let DSPARK prefill publish read-done by placing its draft KV inject before the target forward (#45682)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_kv_inject.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`, `python/sglang/srt/speculative/spec_info.py`, `test/registered/unit/model_executor/runner/test_prefill_shared_read_done.py`_
- **2026-10-21** [`8acfabbd67`](https://github.com/sgl-project/sglang/commit/8acfabbd67) [#38711](https://github.com/sgl-project/sglang/pull/38711)
  [Fix] observability: Correct speculative FPM timing and decode lengths (#38711)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py` _+8 more__
- **2026-10-21** [`573b5716f5`](https://github.com/sgl-project/sglang/commit/573b5716f5) [#45491](https://github.com/sgl-project/sglang/pull/45491)
  [Fix] spec: Take post-verify KV move targets from the verify window (#45491)
  _Files: `python/sglang/srt/speculative/spec_utils.py`, `test/registered/unit/spec/test_move_accept_tokens_targets.py`_
- **2026-10-20** [`7d9bc10493`](https://github.com/sgl-project/sglang/commit/7d9bc10493) [#45421](https://github.com/sgl-project/sglang/pull/45421)
  [Perf] [NVIDIA] DSpark: Enable the simulated-acceptance fast paths on CUDA (#45421)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_verify.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-10-20** [`c2e5742464`](https://github.com/sgl-project/sglang/commit/c2e5742464) [#45260](https://github.com/sgl-project/sglang/pull/45260)
  [Perf] deepseek-v4: DSpark draft stages take the TF32 mHC statistics path from 32 rows on SM100 (#45260)
  _Files: `python/sglang/srt/models/deepseek_v4_dspark.py`, `python/sglang/srt/models/deepseek_v4_mhc.py`_
- **2026-10-19** [`fdc2dd0d05`](https://github.com/sgl-project/sglang/commit/fdc2dd0d05) [#45234](https://github.com/sgl-project/sglang/pull/45234)
  [Perf] dspark: Make the prefill SWA valid-from update sync-free (#45234)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-10-19** [`722669e606`](https://github.com/sgl-project/sglang/commit/722669e606) [#44945](https://github.com/sgl-project/sglang/pull/44945)
  [Feat] [NVIDIA] megakernels: Add --enable-nvidia-megakernel and a layer for NVIDIA megakernel plugins (#44945)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/exec_.py` _+14 more__

## Docs / Examples  (10 commits)

- **2026-10-26** [`d1bbcbdc0d`](https://github.com/sgl-project/sglang/commit/d1bbcbdc0d) [#45642](https://github.com/sgl-project/sglang/pull/45642)
  [Doc] [NPU] cookbook: add A3 deployment scenarios to GLM-5.2 (#45642)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-10-26** [`eabb11a4c1`](https://github.com/sgl-project/sglang/commit/eabb11a4c1) [#46505](https://github.com/sgl-project/sglang/pull/46505)
  [Feat] sgl-router: Confirmed-first pending prefixes for cold prompts, with a follower cap (#46505)
  _Files: `sgl-router/REFERENCE.md`, `sgl-router/monitoring/README.md`, `sgl-router/src/config/cli.rs`, `sgl-router/src/config/types.rs` _+8 more__
- **2026-10-24** [`406786fd91`](https://github.com/sgl-project/sglang/commit/406786fd91) [#46207](https://github.com/sgl-project/sglang/pull/46207)
  [Fix] request_logger: Skip watermark redaction when watermarking is disabled (#46207)
  _Files: `python/sglang/srt/sampling/watermarking/README.md`, `python/sglang/srt/utils/request_logger.py`_
- **2026-10-23** [`f36ee5de93`](https://github.com/sgl-project/sglang/commit/f36ee5de93) [#45924](https://github.com/sgl-project/sglang/pull/45924)
  [Doc] Cookbook: add MiniMax-M3.1 (#45924)
  _Files: `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-10-22** [`0ec3fee429`](https://github.com/sgl-project/sglang/commit/0ec3fee429) [#45429](https://github.com/sgl-project/sglang/pull/45429)
  [Perf] [KDA] cookbook: enable custom all-reduce for GB300 BF16 Muse Spark (#45429)
  _Files: `docs/src/snippets/configs/meta-models/muse-spark.jsx`_
- **2026-10-21** [`75878f27c8`](https://github.com/sgl-project/sglang/commit/75878f27c8) [#45625](https://github.com/sgl-project/sglang/pull/45625)
  [Doc] cookbook: Add Recursive Flint cookbook (#45625)
  _Files: `docs/cards/logos/recursive.png`, `docs/cookbook/autoregressive/Recursive/Flint.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+1 more__
- **2026-10-20** [`c1e43b95f4`](https://github.com/sgl-project/sglang/commit/c1e43b95f4) [#45455](https://github.com/sgl-project/sglang/pull/45455)
  [Doc] cookbook: Add DeepReinforce Ornith-1.5 (#45455)
  _Files: `docs/cookbook/autoregressive/DeepReinforce/Ornith-1.0.mdx`, `docs/cookbook/autoregressive/DeepReinforce/Ornith-1.5.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-10-20** [`4a0c6f2fe0`](https://github.com/sgl-project/sglang/commit/4a0c6f2fe0) [#45271](https://github.com/sgl-project/sglang/pull/45271)
  docs: promote SGLang Summit 2026 in README (#45271)
  _Files: `README.md`_
- **2026-10-19** [`7f96dc6874`](https://github.com/sgl-project/sglang/commit/7f96dc6874) [#43345](https://github.com/sgl-project/sglang/pull/43345)
  [Perf] [XPU] server_args: Enable fused QK-norm + RoPE by default (#43345)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/platform_hook.py` _+1 more__
- **2026-10-19** [`0dc6de2e74`](https://github.com/sgl-project/sglang/commit/0dc6de2e74) [#44587](https://github.com/sgl-project/sglang/pull/44587)
  [Doc] nemotron-3.5-super: update H200 and Spark wizard recipes (#44587)
  _Files: `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl-benchmarks.jsx`, `docs/src/snippets/configs/nvidia/nemotron-3.5-super-vl.jsx`_

## Models  (10 commits)

- **2026-10-22** [`818d7932d7`](https://github.com/sgl-project/sglang/commit/818d7932d7) [#45900](https://github.com/sgl-project/sglang/pull/45900)
  [Perf] dsv4: Drop local references that keep residual-stream tensors alive through the prefill step (#45900)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-22** [`96f013b452`](https://github.com/sgl-project/sglang/commit/96f013b452) [#45495](https://github.com/sgl-project/sglang/pull/45495)
  [Doc] Cookbook: update GB300 DSV4.1 disagg AgentX launches from InferenceX #4303 (#45495)
  _Files: `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-10-22** [`f1e26dc658`](https://github.com/sgl-project/sglang/commit/f1e26dc658) [#45631](https://github.com/sgl-project/sglang/pull/45631)
  [Perf] logits: Write lm_head logits straight into the fp32 logits buffer (#45631)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/models/muse_spark.py`, `test/registered/rl/test_fp32_lm_head.py`_
- **2026-10-21** [`e109bc1832`](https://github.com/sgl-project/sglang/commit/e109bc1832) [#45602](https://github.com/sgl-project/sglang/pull/45602)
  [Doc] [NPU] deepseek-v4: Add A3/950 single-node cookbook recipes (#45602)
  _Files: `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-10-21** [`fda84f80b7`](https://github.com/sgl-project/sglang/commit/fda84f80b7) [#45574](https://github.com/sgl-project/sglang/pull/45574)
  [Doc] [NPU] docs: reference released Qwen3.8-Max W4A8 checkpoint in tutorial (#45574)
  _Files: `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/qwen3_8_max.mdx`_
- **2026-10-21** [`43728298fe`](https://github.com/sgl-project/sglang/commit/43728298fe) [#40889](https://github.com/sgl-project/sglang/pull/40889)
  [Fix] [NPU] qwen3_6: Set accuracy cases to greedy decoding and tune retries (#40889)
  _Files: `test/registered/npu/accuracy/kimi_k3/test_npu_kimi_k3_w4a8_32p_gpqa.py`, `test/registered/npu/accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_1p_gpqa.py`, `test/registered/npu/accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in3k5_out1k5_50ms_gpqa.py`, `test/registered/npu/accuracy/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_aime26.py` _+1 more__
- **2026-10-21** [`9c10e0dd61`](https://github.com/sgl-project/sglang/commit/9c10e0dd61) [#38678](https://github.com/sgl-project/sglang/pull/38678)
  [Doc] [NPU] cookbook: add NPU (A3 series) deployment scenarios for Qwen3.6 (#38678)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/src/snippets/autoregressive/qwen36-deployment.jsx`_
- **2026-10-20** [`afe3e1df31`](https://github.com/sgl-project/sglang/commit/afe3e1df31) [#45427](https://github.com/sgl-project/sglang/pull/45427)
  [Fix] DSpark: Restore weight-loading CPU tests (#45427)
  _Files: `test/registered/unit/model_loader/test_runai_model_streamer_loader.py`, `test/registered/unit/models/test_deepseek_v4_shared_expert_fusion.py`_
- **2026-10-20** [`43a896933e`](https://github.com/sgl-project/sglang/commit/43a896933e) [#41630](https://github.com/sgl-project/sglang/pull/41630)
  [Fix] deepseek-v4: Refresh attn_sink after loading weights (#41630)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-19** [`9a93a17c08`](https://github.com/sgl-project/sglang/commit/9a93a17c08) [#44624](https://github.com/sgl-project/sglang/pull/44624)
  [Feat] [CPU] model: Support Muse models on CPU (#44624)
  _Files: `python/sglang/srt/configs/muse_glimmer.py`, `python/sglang/srt/configs/update_config.py`, `python/sglang/srt/models/muse_glimmer.py`_

## LoRA  (9 commits)

- **2026-10-24** [`17d92ea671`](https://github.com/sgl-project/sglang/commit/17d92ea671) [#46219](https://github.com/sgl-project/sglang/pull/46219)
  [Feat] openai: Parse DeepSeek text for the native endpoints through deepseek-recipe (#46219)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/chat_encoding_adapters.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_deepseek_recipe.py` _+7 more__
- **2026-10-24** [`a77998e157`](https://github.com/sgl-project/sglang/commit/a77998e157) [#45907](https://github.com/sgl-project/sglang/pull/45907)
  [Feat] openai: parse DeepSeek output through deepseek-recipe (#45907)
  _Files: `python/sglang/srt/entrypoints/openai/chat_encoding.py`, `python/sglang/srt/entrypoints/openai/chat_encoding_adapters.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_deepseek_recipe.py` _+7 more__
- **2026-10-24** [`e22a530859`](https://github.com/sgl-project/sglang/commit/e22a530859) [#45315](https://github.com/sgl-project/sglang/pull/45315)
  [Feat] openai: Render DeepSeek-V4/V4.1 chat prompts with deepseek-recipe (#45315)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` _+21 more__
- **2026-10-23** [`6a319e7b34`](https://github.com/sgl-project/sglang/commit/6a319e7b34) [#44685](https://github.com/sgl-project/sglang/pull/44685)
  [Fix] muse: Support Responses namespace tools and defer_loading (#44685)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/responses_adapters.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py` _+2 more__
- **2026-10-23** [`27ac614f05`](https://github.com/sgl-project/sglang/commit/27ac614f05) [#40479](https://github.com/sgl-project/sglang/pull/40479)
  [Feat] parser: Add checkpoint-driven response-template adapters (#40479)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py`, `python/sglang/srt/function_call/function_call_parser.py` _+16 more__
- **2026-10-23** [`8b9f72417f`](https://github.com/sgl-project/sglang/commit/8b9f72417f) [#45340](https://github.com/sgl-project/sglang/pull/45340)
  [Feat] Inkling: render and parse chat via tml-renderers (#45340)
  _Files: `python/pyproject.toml`, `python/sglang/srt/entrypoints/openai/chat_encoding.py`, `python/sglang/srt/entrypoints/openai/chat_encoding_adapters.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py` _+12 more__
- **2026-10-20** [`16eb87c06f`](https://github.com/sgl-project/sglang/commit/16eb87c06f) [#44450](https://github.com/sgl-project/sglang/pull/44450)
  [Fix] openai: distinguish s3 served-model-name from LoRA adapter syntax (#44450)
  _Files: `python/sglang/srt/entrypoints/openai/serving_base.py`, `test/registered/lora/test_lora_openai_api.py`_
- **2026-10-20** [`4b83f215f4`](https://github.com/sgl-project/sglang/commit/4b83f215f4) [#45300](https://github.com/sgl-project/sglang/pull/45300)
  [Feat] entrypoints: add a chat encoding adapter registry (#45300)
  _Files: `python/sglang/srt/entrypoints/openai/chat_encoding_adapters.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_inkling.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py` _+1 more__
- **2026-10-20** [`55b2aef7ad`](https://github.com/sgl-project/sglang/commit/55b2aef7ad) [#40908](https://github.com/sgl-project/sglang/pull/40908)
  [Fix] [NPU] LoRA: Update for follow-up with changes in sgl-kernel-npu (#40908)
  _Files: `python/sglang/srt/lora/backend/ascend_backend.py`_

## Structured Output  (5 commits)

- **2026-10-26** [`5ef99013ac`](https://github.com/sgl-project/sglang/commit/5ef99013ac) [#46049](https://github.com/sgl-project/sglang/pull/46049)
  [Fix] grammar: Give grammar accept failures an error status (#46049)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`_
- **2026-10-26** [`fa622d311d`](https://github.com/sgl-project/sglang/commit/fa622d311d) [#36074](https://github.com/sgl-project/sglang/pull/36074)
  [Feat] [NPU] llguidance: add bitmask path for Ascend (#36074)
  _Files: `python/sglang/srt/constrained/llguidance_backend.py`, `test/manual/ascend/test_llguidance_npu_mask.py`_
- **2026-10-24** [`d0f517168d`](https://github.com/sgl-project/sglang/commit/d0f517168d) [#46133](https://github.com/sgl-project/sglang/pull/46133)
  [Fix] minimax-m3: Type nested tool-call arguments and count self-opened reasoning (#46133)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/usage_processor.py` _+15 more__
- **2026-10-20** [`2c00b5d129`](https://github.com/sgl-project/sglang/commit/2c00b5d129) [#43981](https://github.com/sgl-project/sglang/pull/43981)
  [Test] constrained: Cover JSON whitespace limits (#43981)
  _Files: `test/registered/npu/basic_function/runtime_opts/test_npu_constrained_json_whitespace.py`_
- **2026-10-20** [`79ed13fc2c`](https://github.com/sgl-project/sglang/commit/79ed13fc2c) [#41233](https://github.com/sgl-project/sglang/pull/41233)
  [Fix] glm47: Disable tool grammar for `tool_choice="none"` (#41233)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_

## Serving / API  (5 commits)

- **2026-10-26** [`2b84393124`](https://github.com/sgl-project/sglang/commit/2b84393124) [#46432](https://github.com/sgl-project/sglang/pull/46432)
  [Chore] sgl-router: use `api.v1` typed generate response (#46432)
  _Files: `rust/sglang-processor/README.md`, `rust/sglang-processor/src/openai/chat.rs`, `rust/sglang-processor/src/openai/completions.rs`, `rust/sglang-processor/src/openai/mod.rs` _+3 more__
- **2026-10-24** [`fe1bd10837`](https://github.com/sgl-project/sglang/commit/fe1bd10837)
  [Perf] glm-5.3: Encode GLM-5.3 Python chat template prompts segment by segment
  _Files: `python/sglang/srt/entrypoints/openai/parallel_prompt_encode.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/parser/glm53_chat_template.py`, `python/sglang/srt/parser/python_chat_template.py` _+3 more__
- **2026-10-24** [`463af5ac80`](https://github.com/sgl-project/sglang/commit/463af5ac80) [#46078](https://github.com/sgl-project/sglang/pull/46078)
  [Fix] bench: Add missing HiCache RPCs to gRPC mock (#46078)
  _Files: `rust/sglang-bench/tests/grpc.rs`_
- **2026-10-23** [`611a703061`](https://github.com/sgl-project/sglang/commit/611a703061) [#45164](https://github.com/sgl-project/sglang/pull/45164)
  [Chore] api: add fields to generate request (#45164)
  _Files: `proto/sglang/api/v1/generate.proto`, `python/sglang/api/v1/api_types.py`, `rust/sglang-api-types/src/generated/sglang.api.v1.rs`, `rust/sglang-api-types/src/generated/sglang.api.v1.serde.rs` _+8 more__
- **2026-10-21** [`8599b7251f`](https://github.com/sgl-project/sglang/commit/8599b7251f) [#45291](https://github.com/sgl-project/sglang/pull/45291)
  [Chore] deps: Bump the OpenAI SDK to 2.8.0 for Responses shell tools (2/8) (#45291)
  _Files: `python/pyproject.toml`_

---
_Generated 2026-10-26 15:10 UTC_