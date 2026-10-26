# vllm-project/vllm — Weekly Change Report
**Period:** 2026-10-19 → 2026-10-26  |  **Total commits:** 523

## ✨ New Features This Week

- **2026-10-26** [#63036](https://github.com/vllm-project/vllm/pull/63036) — [docs] correct NIXL hybrid SSM heterogeneous TP support (#63036)
- **2026-10-26** [#58768](https://github.com/vllm-project/vllm/pull/58768) — [docker] add vllm-openai-efa target (#58768)
- **2026-10-26** [#63658](https://github.com/vllm-project/vllm/pull/63658) — [XPU][CI] Enable test_fusion_rmsnorm_quant on XPU (#63658)
- **2026-10-26** [#61094](https://github.com/vllm-project/vllm/pull/61094) — [Frontend] Add --reasoning-effort-map to rewrite request reasoning efforts (#61094)
- **2026-10-26** [#61879](https://github.com/vllm-project/vllm/pull/61879) — [Model] Add Muse Spark Open support (#61879)
- **2026-10-25** [#63616](https://github.com/vllm-project/vllm/pull/63616) — [Benchmark] Add steady-state PP support to bench forward (#63616)
- **2026-10-25** [#63613](https://github.com/vllm-project/vllm/pull/63613) — [Benchmark] Add PCP support to vllm bench forward (#63613)
- **2026-10-25** [#63088](https://github.com/vllm-project/vllm/pull/63088) — [Fast Start] Add daemon-to-daemon warmup cache seeding for Preload (#63088)
- **2026-10-25** [#60149](https://github.com/vllm-project/vllm/pull/60149) — [Model] Add Dory support (#60149)
- **2026-10-24** [#58466](https://github.com/vllm-project/vllm/pull/58466) — [Sampling] Add adaptive verification support to batch-sharded sampling (#58466)
- _…and 76 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-26** [`d0d681e40d`](https://github.com/vllm-project/vllm/commit/d0d681e40d) [#63669](https://github.com/vllm-project/vllm/pull/63669) — [ROCm][Perf] Make MXFP4 the default indexer K cache dtype for DeepSeek-V4 (#63669)
- **2026-10-26** [`c3941c032d`](https://github.com/vllm-project/vllm/commit/c3941c032d) [#63099](https://github.com/vllm-project/vllm/pull/63099) — [Bugfix][ROCm] Match the DeepSeek-V4.1 FP8 config in the shared-expert FSE compatibility check (#63099)
- **2026-10-26** [`9bea474d65`](https://github.com/vllm-project/vllm/commit/9bea474d65) [#59478](https://github.com/vllm-project/vllm/pull/59478) — [ROCm][Perf] Use AITER FlyDSL INT4 QuickReduce when INT4 QuickReduce is selected (#59478)
- **2026-10-26** [`ae3bc684e0`](https://github.com/vllm-project/vllm/commit/ae3bc684e0) [#63665](https://github.com/vllm-project/vllm/pull/63665) — [Doc][ROCm] Update DeepSeek-V4.1-Flash MI355X AgentX scheduling profiles (#63665)
- **2026-10-26** [`2f34dce583`](https://github.com/vllm-project/vllm/commit/2f34dce583) [#63657](https://github.com/vllm-project/vllm/pull/63657) — [Doc][ROCm] Update Kimi-K3 MI355X AgentX scheduling cells (#63657)
- **2026-10-26** [`00b6c4c565`](https://github.com/vllm-project/vllm/commit/00b6c4c565) [#59774](https://github.com/vllm-project/vllm/pull/59774) — [ROCm] Octave KV (`ROCM_OCTAVE`): native 3-bit KV cache backend for AMD GPUs (#59774)
- **2026-10-26** [`0f6b261910`](https://github.com/vllm-project/vllm/commit/0f6b261910) [#61879](https://github.com/vllm-project/vllm/pull/61879) — [Model] Add Muse Spark Open support (#61879)
- **2026-10-25** [`2c880f1e68`](https://github.com/vllm-project/vllm/commit/2c880f1e68) [#59223](https://github.com/vllm-project/vllm/pull/59223) — [Bugfix] Preserve FP8 indexer WK pairs across load_weights calls (#59223)
- **2026-10-25** [`f8c12c212a`](https://github.com/vllm-project/vllm/commit/f8c12c212a) [#63609](https://github.com/vllm-project/vllm/pull/63609) — [CI] Disable jobs with unpinned runtime installs (#63609)
- **2026-10-25** [`9d48c8ab95`](https://github.com/vllm-project/vllm/commit/9d48c8ab95) [#63608](https://github.com/vllm-project/vllm/pull/63608) — [CI] Disable jobs with unlocked transitive dependencies (#63608)
- **2026-10-25** [`a55937f255`](https://github.com/vllm-project/vllm/commit/a55937f255) [#60084](https://github.com/vllm-project/vllm/pull/60084) — [ROCm][Perf] Restore 32-bit buffer addressing for TRITON_ATTN KV cache views (#60084)
- **2026-10-25** [`444d69110e`](https://github.com/vllm-project/vllm/commit/444d69110e) [#63520](https://github.com/vllm-project/vllm/pull/63520) — [Doc][ROCm] Align Kimi-K3 MI355X AgentX recipe with InferenceX #4393 (#63520)
- **2026-10-24** [`56e4e42868`](https://github.com/vllm-project/vllm/commit/56e4e42868) [#62102](https://github.com/vllm-project/vllm/pull/62102) — [GLM 5.3 Perf] Skip scale calculation for `concat_and_cache_mla`, 1.2% ~ 3.0% E2E TPOT improvement (#62102)
- **2026-10-24** [`7822663cb4`](https://github.com/vllm-project/vllm/commit/7822663cb4) [#62713](https://github.com/vllm-project/vllm/pull/62713) — [DeepSeek][ROCm] V4.1-Flash: enable --monokernel on MI325X (#62713)
- **2026-10-24** [`c0ba7e01ff`](https://github.com/vllm-project/vllm/commit/c0ba7e01ff) [#60413](https://github.com/vllm-project/vllm/pull/60413) — [Perf][ROCm][Kernel] Add W4A8 int8-dot MXFP4 GEMV for RDNA3/RDNA3.5 d… (#60413)
- **2026-10-24** [`39504080e5`](https://github.com/vllm-project/vllm/commit/39504080e5) [#61628](https://github.com/vllm-project/vllm/pull/61628) — [ROCm][MLA][DCP] Drop VLLM_ROCM_AITER_MLA_DCP_VERIFY (#61628)
- **2026-10-24** [`cba669d45d`](https://github.com/vllm-project/vllm/commit/cba669d45d) [#57909](https://github.com/vllm-project/vllm/pull/57909) — [ROCm][PERF] Enable MiniMax-M3 Indexer CP (#57909)
- **2026-10-24** [`139feb4534`](https://github.com/vllm-project/vllm/commit/139feb4534) [#61482](https://github.com/vllm-project/vllm/pull/61482) — [ROCm][Perf][DSv4] Standalone mono decode layer for DeepSeek-V4-Pro on MI355X (#61482)
- **2026-10-24** [`2aa7269a83`](https://github.com/vllm-project/vllm/commit/2aa7269a83) [#62473](https://github.com/vllm-project/vllm/pull/62473) — [Bugfix][ROCm][MoRIIO] Release every prefill rank a READ holds (#62473)
- **2026-10-24** [`7a64fb8fc9`](https://github.com/vllm-project/vllm/commit/7a64fb8fc9) [#63452](https://github.com/vllm-project/vllm/pull/63452) — [CI] Fix the Domyn Edge (ROCm) and Qwen2 embed HF references (#63452)
- **2026-10-24** [`a5b71c1eb3`](https://github.com/vllm-project/vllm/commit/a5b71c1eb3) [#62835](https://github.com/vllm-project/vllm/pull/62835) — [Security] Refresh vulnerable runtime and test dependencies (#62835)
- **2026-10-24** [`debcf22843`](https://github.com/vllm-project/vllm/commit/debcf22843) [#59100](https://github.com/vllm-project/vllm/pull/59100) — [CI][ROCm] Export kernel source maps for CI selection (#59100)
- **2026-10-23** [`2c58be22b6`](https://github.com/vllm-project/vllm/commit/2c58be22b6) [#63131](https://github.com/vllm-project/vllm/pull/63131) — [Bugfix][ROCm][Kimi-K3] Validate gfx942's int4 expert requant as int4 (#63131)
- **2026-10-23** [`96bbaa300f`](https://github.com/vllm-project/vllm/commit/96bbaa300f) [#60644](https://github.com/vllm-project/vllm/pull/60644) — [ROCm][RDNA][Perf] W4A16: packed fp16 prefill dequant and tiles for gfx1151 (#60644)
- **2026-10-23** [`c7476c7a6f`](https://github.com/vllm-project/vllm/commit/c7476c7a6f) [#62384](https://github.com/vllm-project/vllm/pull/62384) — [Feature][PCP] Support decoder-side SWA bounded replay with APC for DeepSeek-V4.1-Flash (#62384)
- **2026-10-23** [`1a1540480d`](https://github.com/vllm-project/vllm/commit/1a1540480d) [#63400](https://github.com/vllm-project/vllm/pull/63400) — [Refactor] Remove dead code models (#63400)
- **2026-10-23** [`29cf023770`](https://github.com/vllm-project/vllm/commit/29cf023770) [#61649](https://github.com/vllm-project/vllm/pull/61649) — [Refactor] [AMD] flydsl: Move UltraQuant/TurboQuant decode to public APIs (#61649)
- **2026-10-23** [`18df4cd9a9`](https://github.com/vllm-project/vllm/commit/18df4cd9a9) [#63268](https://github.com/vllm-project/vllm/pull/63268) — [ROCm][Bugfix] Fix Triton paged decode leaving output heads unwritten on gfx942 (#63268)
- **2026-10-23** [`be03d19750`](https://github.com/vllm-project/vllm/commit/be03d19750) [#62907](https://github.com/vllm-project/vllm/pull/62907) — [CI][ROCm][MoE] Add MXFP4 SWIGLUOAI_UNINTERLEAVE/SITU test coverage on MI355 (#62907)
- **2026-10-23** [`bc3afc4096`](https://github.com/vllm-project/vllm/commit/bc3afc4096) [#63242](https://github.com/vllm-project/vllm/pull/63242) — [CI][ROCm] Fail the AITER nightly overlay on wheels ci_base cannot load (#63242)
- **2026-10-23** [`f869d64788`](https://github.com/vllm-project/vllm/commit/f869d64788) [#63283](https://github.com/vllm-project/vllm/pull/63283) — [CI][ROCm] Run the online FP8 MoE batch-invariance test on ROCm (#63283)
- **2026-10-23** [`b1c66e5545`](https://github.com/vllm-project/vllm/commit/b1c66e5545) [#62757](https://github.com/vllm-project/vllm/pull/62757) — [ROCm][Model] Muse Spark: share one RoPE cache sized by max_model_len (#62757)
- **2026-10-23** [`224b2f54f1`](https://github.com/vllm-project/vllm/commit/224b2f54f1) [#62934](https://github.com/vllm-project/vllm/pull/62934) — [ROCm][CI] Move NFS-affected MI300 test groups to MI355 (#62934)
- **2026-10-23** [`74ba6384c2`](https://github.com/vllm-project/vllm/commit/74ba6384c2) [#63344](https://github.com/vllm-project/vllm/pull/63344) — [Doc][ROCm] Document DeepSeek-V4.1-Flash MI355X AgentX TP2 profiles (#63344)
- **2026-10-23** [`c0a41721c7`](https://github.com/vllm-project/vllm/commit/c0a41721c7) [#63269](https://github.com/vllm-project/vllm/pull/63269) — [CI][ROCm] Raise the MI355 MiniMax M3 MonoKernel timeout to 45 minutes (#63269)
- **2026-10-23** [`be08fa5355`](https://github.com/vllm-project/vllm/commit/be08fa5355) [#62827](https://github.com/vllm-project/vllm/pull/62827) — [ROCm] Bump UCX to v1.23.0-rc1 so NIXL uses rocm_ipc (#62827)
- **2026-10-23** [`098eb89ea4`](https://github.com/vllm-project/vllm/commit/098eb89ea4) [#63031](https://github.com/vllm-project/vllm/pull/63031) — [ROCm][Kimi-K3] Support MoRIIO consumers with specialized decode (#63031)
- **2026-10-23** [`dc05b14556`](https://github.com/vllm-project/vllm/commit/dc05b14556) [#58743](https://github.com/vllm-project/vllm/pull/58743) — [ROCm][Kimi-K3] Support BF16 KDA recurrent state (#58743)
- **2026-10-23** [`da180efbcd`](https://github.com/vllm-project/vllm/commit/da180efbcd) [#63257](https://github.com/vllm-project/vllm/pull/63257) — [ROCm][Recipe] MiniMax-M3.1-Flash: MI355X PD, DBO / SP prefill, Quark MXFP4, mono decode (#63257)
- **2026-10-23** [`3dbf2b6c0c`](https://github.com/vllm-project/vllm/commit/3dbf2b6c0c) [#62756](https://github.com/vllm-project/vllm/pull/62756) — [Bugfix][ROCm] Muse Spark: apply output multiplier and softcap in compute_logits_local (#62756)
- **2026-10-23** [`2d40c0609f`](https://github.com/vllm-project/vllm/commit/2d40c0609f) [#61855](https://github.com/vllm-project/vllm/pull/61855) — [ROCm][Perf] Triton port of the fused GDN MTP decode kernel (#61855)
- **2026-10-23** [`022b43c66f`](https://github.com/vllm-project/vllm/commit/022b43c66f) [#60834](https://github.com/vllm-project/vllm/pull/60834) — [ROCm][Perf] Apply opt-in paged MXFP4 sparse indexer dense path for DeepSeek-V4 (#60834)
- **2026-10-23** [`f120f1dbf2`](https://github.com/vllm-project/vllm/commit/f120f1dbf2) [#63082](https://github.com/vllm-project/vllm/pull/63082) — [Bugfix][ROCm][MiniMax-M3] Reject IndexCache overrides that miss text_config (#63082)
- **2026-10-22** [`cc1a6d3135`](https://github.com/vllm-project/vllm/commit/cc1a6d3135) [#63105](https://github.com/vllm-project/vllm/pull/63105) — [ROCm][Build] Reland #62475: paged attention kernel split with `--offload-compress` => x4-x7 wheel build speedup on ROCm (#63105)
- **2026-10-22** [`6d1909a1f2`](https://github.com/vllm-project/vllm/commit/6d1909a1f2) [#63007](https://github.com/vllm-project/vllm/pull/63007) — [Bugfix][ROCm][DSv4.1] Gather Engram hashes across DP replicas in the AMD model (#63007)
- **2026-10-22** [`f01a76f950`](https://github.com/vllm-project/vllm/commit/f01a76f950) [#63009](https://github.com/vllm-project/vllm/pull/63009) — [ROCm][DSv4.1] Allocate offloaded Engram tables at their exact size (#63009)
- **2026-10-22** [`1d3e4006c4`](https://github.com/vllm-project/vllm/commit/1d3e4006c4) [#62099](https://github.com/vllm-project/vllm/pull/62099) — [ROCm][CI] Fix int8 GEMM kernel selection logic for ROCm platform (#62099)
- **2026-10-22** [`90aa823cba`](https://github.com/vllm-project/vllm/commit/90aa823cba) [#63127](https://github.com/vllm-project/vllm/pull/63127) — [ROCm][CI] Download quick-reduce e2e model when cached snapshot has no weights (#63127)
- **2026-10-22** [`168a86ab8f`](https://github.com/vllm-project/vllm/commit/168a86ab8f) [#60238](https://github.com/vllm-project/vllm/pull/60238) — [Multimodal] Skip encoder towers on later PP stages under V2 (#60238)
- **2026-10-22** [`fa72b61b55`](https://github.com/vllm-project/vllm/commit/fa72b61b55) [#62868](https://github.com/vllm-project/vllm/pull/62868) — [Security] Refresh Python and runtime CA certificates (#62868)
- **2026-10-22** [`6ab6bff1b6`](https://github.com/vllm-project/vllm/commit/6ab6bff1b6) [#62622](https://github.com/vllm-project/vllm/pull/62622) — [Model][ROCm] Add Muse Spark Open support on ROCm (#62622)
- **2026-10-22** [`f46ea25e58`](https://github.com/vllm-project/vllm/commit/f46ea25e58) [#58660](https://github.com/vllm-project/vllm/pull/58660) — [Perf][Frontend] Share orjson responses across render and pooling (#58660)
- **2026-10-22** [`aa31fa038f`](https://github.com/vllm-project/vllm/commit/aa31fa038f) [#61862](https://github.com/vllm-project/vllm/pull/61862) — [CI] Move V1 Attention, core kernels and quantization AMD mirrors from fixed to automatic shards (#61862)
- **2026-10-22** [`05406ba470`](https://github.com/vllm-project/vllm/commit/05406ba470) [#62994](https://github.com/vllm-project/vllm/pull/62994) — [ROCm][Perf][MiniMax-M3] MonoKernel: serve EAGLE3 verify steps (#62994)
- **2026-10-22** [`9d61ade7f6`](https://github.com/vllm-project/vllm/commit/9d61ade7f6) [#62475](https://github.com/vllm-project/vllm/pull/62475) — [ROCm] Revert "[ROCm][Build] Compile paged attention kernels in parallel (7.6x faster attention build) (#62475)" (#62983)
- **2026-10-22** [`a4aa37d1a0`](https://github.com/vllm-project/vllm/commit/a4aa37d1a0) [#57481](https://github.com/vllm-project/vllm/pull/57481) — [ROCm] Capture CUDA graphs with expandable segments off for AITER all-reduce (#57481)
- **2026-10-22** [`a6020fc669`](https://github.com/vllm-project/vllm/commit/a6020fc669) [#62977](https://github.com/vllm-project/vllm/pull/62977) — [ROCm] Add _maybe_pad_weight guard-condition and RL-reload stability tests (#62977)
- **2026-10-21** [`833349105b`](https://github.com/vllm-project/vllm/commit/833349105b) [#58509](https://github.com/vllm-project/vllm/pull/58509) — [ROCm][Perf] HY4 preview perf boost (#58509)
- **2026-10-21** [`c84edac4cb`](https://github.com/vllm-project/vllm/commit/c84edac4cb) [#62893](https://github.com/vllm-project/vllm/pull/62893) — [ROCm][CI] Enable batch invariance for eagle3 scheduling accuracy (#62893)
- **2026-10-21** [`f143f65d7c`](https://github.com/vllm-project/vllm/commit/f143f65d7c) [#62882](https://github.com/vllm-project/vllm/pull/62882) — [CI][ROCm] Set the FP8 MLA prefill scale cache in the test double (#62882)
- **2026-10-21** [`db3b0f0fae`](https://github.com/vllm-project/vllm/commit/db3b0f0fae) [#60808](https://github.com/vllm-project/vllm/pull/60808) — [Bugfix][KV Connector][ROCm] MoRIIO READ: await every read before the forward (#60808)
- **2026-10-21** [`d7ada3aace`](https://github.com/vllm-project/vllm/commit/d7ada3aace) [#62869](https://github.com/vllm-project/vllm/pull/62869) — [CI][ROCm] Give the M3 embed-sharing fixture a kernel_config (#62869)
- **2026-10-21** [`e9cc6244a0`](https://github.com/vllm-project/vllm/commit/e9cc6244a0) [#62721](https://github.com/vllm-project/vllm/pull/62721) — [Rust Frontend] Refresh rust/AGENTS.md with ownership and design conventions (#62721)
- **2026-10-21** [`64c5f14f6a`](https://github.com/vllm-project/vllm/commit/64c5f14f6a) [#59266](https://github.com/vllm-project/vllm/pull/59266) — [ROCm][DI][CI] Enable WideEP EP16/DP16 tests  (#59266)
- **2026-10-21** [`153b76b304`](https://github.com/vllm-project/vllm/commit/153b76b304) [#57832](https://github.com/vllm-project/vllm/pull/57832) — [ROCm][Model][MiniMax-M3] Context-parallel sparse lightning indexer (Triton, opt-in) (#57832)
- **2026-10-21** [`385d1dab3b`](https://github.com/vllm-project/vllm/commit/385d1dab3b) [#62712](https://github.com/vllm-project/vllm/pull/62712) — [ROCm][Perf][MiniMax-M3] MonoKernel decode for M3 MXFP4 on MI355X (#62712)
- **2026-10-21** [`fc377f7771`](https://github.com/vllm-project/vllm/commit/fc377f7771) [#62405](https://github.com/vllm-project/vllm/pull/62405) — [Quantization] Use replace_parameter for params re-created in process_weights_after_loading (#62405)
- **2026-10-21** [`a9bf45ed8a`](https://github.com/vllm-project/vllm/commit/a9bf45ed8a) [#60683](https://github.com/vllm-project/vllm/pull/60683) — [ROCm][Perf][Kimi-K3] Specialized decode for Kimi-K3 on MI355X (#60683)
- **2026-10-21** [`e8ae84bf7e`](https://github.com/vllm-project/vllm/commit/e8ae84bf7e) [#62475](https://github.com/vllm-project/vllm/pull/62475) — [ROCm][Build] Compile paged attention kernels in parallel (7.6x faster attention build) (#62475)
- **2026-10-21** [`aca582857b`](https://github.com/vllm-project/vllm/commit/aca582857b) [#62646](https://github.com/vllm-project/vllm/pull/62646) — [CI][ROCm] Mirror the Distributed Preload group on MI355 (#62646)
- **2026-10-21** [`27aadb3096`](https://github.com/vllm-project/vllm/commit/27aadb3096) [#62403](https://github.com/vllm-project/vllm/pull/62403) — [ROCm][Bugfix] Fix wrong output of the QK-norm + RoPE + KV-cache fusion on ROCM_ATTN (#62403)
- **2026-10-21** [`e632d66433`](https://github.com/vllm-project/vllm/commit/e632d66433) [#61058](https://github.com/vllm-project/vllm/pull/61058) — [CI] Fix Buildkite path filters that point at moved or deleted files (#61058)
- **2026-10-21** [`532a7d19d2`](https://github.com/vllm-project/vllm/commit/532a7d19d2) [#55901](https://github.com/vllm-project/vllm/pull/55901) — [MyPy] Fix mypy errors in KV connector tests (kv-B) (#55901)
- **2026-10-20** [`b1ab16c548`](https://github.com/vllm-project/vllm/commit/b1ab16c548) [#62486](https://github.com/vllm-project/vllm/pull/62486) — [ROCm] Bump AITER to v1.26.0 (#62486)
- **2026-10-20** [`3a1bd8347a`](https://github.com/vllm-project/vllm/commit/3a1bd8347a) [#55542](https://github.com/vllm-project/vllm/pull/55542) — [MyPy] Fix mypy errors in easy tests/v1/kv_connector files (kv-A) (#55542)
- **2026-10-20** [`0f30006267`](https://github.com/vllm-project/vllm/commit/0f30006267) [#62735](https://github.com/vllm-project/vllm/pull/62735) — [ROCm][CI][Bug] Remove padding from AITER output for quantization/tes… (#62735)
- **2026-10-20** [`9da5f2d310`](https://github.com/vllm-project/vllm/commit/9da5f2d310) [#60250](https://github.com/vllm-project/vllm/pull/60250) — [ROCm] Enable the rms_norm_gated custom op by default (Qwen3.8-27B) (#60250)
- **2026-10-20** [`09fd027217`](https://github.com/vllm-project/vllm/commit/09fd027217) [#59634](https://github.com/vllm-project/vllm/pull/59634) — [ROCm][Perf][Kimi-K3] Fuse the GLA gate GEMM and the MLA FP8 prefill q/k/v prep (#59634)
- **2026-10-20** [`005cef040a`](https://github.com/vllm-project/vllm/commit/005cef040a) [#62731](https://github.com/vllm-project/vllm/pull/62731) — [CI][ROCm] Remove MI300 Model Runner V2 steps (#62731)
- **2026-10-20** [`6e780d14cd`](https://github.com/vllm-project/vllm/commit/6e780d14cd) [#62032](https://github.com/vllm-project/vllm/pull/62032) — [CI][ROCm] Use AITER prebuilt fp8 MoE modules when inter dim is 256 aligned (#62032)
- **2026-10-20** [`82b7dad5e3`](https://github.com/vllm-project/vllm/commit/82b7dad5e3) [#61790](https://github.com/vllm-project/vllm/pull/61790) — [Test][UMBP][2/10] Add shared connector contract coverage (#61790)
- **2026-10-20** [`4a30738d21`](https://github.com/vllm-project/vllm/commit/4a30738d21) [#41197](https://github.com/vllm-project/vllm/pull/41197) — [ROCm][benchmark][perf] fix moe tuning script for RDNA (#41197)
- **2026-10-20** [`11a8d571d2`](https://github.com/vllm-project/vllm/commit/11a8d571d2) [#62680](https://github.com/vllm-project/vllm/pull/62680) — [CI][AMD] Deselect distributed tests in the MI300 Model Executor step (#62680)
- **2026-10-20** [`a6c898e2a9`](https://github.com/vllm-project/vllm/commit/a6c898e2a9) [#62686](https://github.com/vllm-project/vllm/pull/62686) — [CI][AMD] Shard the MI300 V1 Spec Decode step (#62686)
- **2026-10-20** [`e2d2680417`](https://github.com/vllm-project/vllm/commit/e2d2680417) [#62039](https://github.com/vllm-project/vllm/pull/62039) — [CI] Shard E2E Scheduling, Benchmarks CLI and six AMD mirrors automatically (#62039)
- **2026-10-20** [`87fa712793`](https://github.com/vllm-project/vllm/commit/87fa712793) [#62562](https://github.com/vllm-project/vllm/pull/62562) — [CI] Shard (H200 MIG 35GB / MI355 DPX) Multimodal Models (Standard) 4 automatically (#62562)
- **2026-10-20** [`f85e39ea01`](https://github.com/vllm-project/vllm/commit/f85e39ea01) [#57916](https://github.com/vllm-project/vllm/pull/57916) — [ROCm][Quantization][MOE] Enable fused shared experts for MXFP8 checkpoints (#57916)
- **2026-10-20** [`428cd0cb4a`](https://github.com/vllm-project/vllm/commit/428cd0cb4a) [#62421](https://github.com/vllm-project/vllm/pull/62421) — [ROCm][Model] DeepSeek-V4.1 VL: stream language-model weights on ROCm (#62421)
- **2026-10-20** [`9499c949be`](https://github.com/vllm-project/vllm/commit/9499c949be) [#52670](https://github.com/vllm-project/vllm/pull/52670) — [Quantizaiton][Feature] Pluggable KV Cache Data Types (#52670)
- **2026-10-20** [`1a74cc7bb2`](https://github.com/vllm-project/vllm/commit/1a74cc7bb2) [#60731](https://github.com/vllm-project/vllm/pull/60731) — [ROCm][Perf][DSv4.1] Mono decode on MI300X and MI325X (gfx942) (#60731)
- **2026-10-19** [`53172fa72e`](https://github.com/vllm-project/vllm/commit/53172fa72e) [#61983](https://github.com/vllm-project/vllm/pull/61983) — [CI] Bump Transformers version to 5.20.0 (#61983)
- **2026-10-19** [`8c60cf07b3`](https://github.com/vllm-project/vllm/commit/8c60cf07b3) [#62567](https://github.com/vllm-project/vllm/pull/62567) — [CI] Keep the AMD mirrors of the nightly-only 4xL4 steps on PRs (#62567)
- **2026-10-19** [`b439421f11`](https://github.com/vllm-project/vllm/commit/b439421f11) [#62520](https://github.com/vllm-project/vllm/pull/62520) — [CI][ROCm] Raise data_parallel_offline.py --timeout in AMD Torchrun + Examples (#62520)
- **2026-10-19** [`c8fbb79406`](https://github.com/vllm-project/vllm/commit/c8fbb79406) [#60886](https://github.com/vllm-project/vllm/pull/60886) — [ROCm][MoE] Add AITER MXFP4 W4A16/W4A4 modular-kernel test coverage (#60886)
- **2026-10-19** [`5caabdbb65`](https://github.com/vllm-project/vllm/commit/5caabdbb65) [#62390](https://github.com/vllm-project/vllm/pull/62390) — [Frontend] Consolidate startup utils. (#62390)
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

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#63640](https://github.com/vllm-project/vllm/issues/63640) | [RFC]: vLLM Attention Backend Test Suites | rocm, RFC | 2026-10-26 |
| [#63759](https://github.com/vllm-project/vllm/issues/63759) | [Bug]: Qwen3.5: int32 token-offset overflows in three Triton kernels g | — | 2026-10-26 |
| [#63757](https://github.com/vllm-project/vllm/issues/63757) | [RFC]: Context-length-bounded FULL decode CUDA graphs in Model Runner  | rocm, quantization | 2026-10-26 |
| [#63732](https://github.com/vllm-project/vllm/issues/63732) | [Bug]: Gemma 4 + online --quantization fp8: image requests crash since | quantization | 2026-10-26 |
| [#52911](https://github.com/vllm-project/vllm/issues/52911) | [RFC]: DeepSeek-V4 Performance Optimization on ROCm (Phase Two) | rocm, RFC, deepseek, DSv4 | 2026-10-26 |
| [#57725](https://github.com/vllm-project/vllm/issues/57725) | [Bug]: a malformed structured-output specification returns HTTP 500 wi | bug, structured-output | 2026-10-26 |
| [#63712](https://github.com/vllm-project/vllm/issues/63712) | [ROCm][MI350P] Muse Spark MonoKernel decode assumes 256 co-resident CT | rocm | 2026-10-26 |
| [#63602](https://github.com/vllm-project/vllm/issues/63602) | [Bug]: P2P KV offload tier does not fail fast on peer faults | — | 2026-10-26 |
| [#62697](https://github.com/vllm-project/vllm/issues/62697) | [Bug][ROCm] `ROCM_ATTN` returns wrong attention (and can fault the GPU | rocm | 2026-10-26 |
| [#59457](https://github.com/vllm-project/vllm/issues/59457) | [Bug]: [gpt-oss-20b-bf16] W4A8 quantized model produces garbled output | bug, cpu, gpt-oss, quantization | 2026-10-26 |
| [#62851](https://github.com/vllm-project/vllm/issues/62851) | [Bug]: Qwen3.6 GDN greedy DFlash2 divergence from batch-dependent nume | quantization | 2026-10-26 |
| [#42082](https://github.com/vllm-project/vllm/issues/42082) | [RFC]: Standardize KV-cache Layouts | RFC | 2026-10-26 |
| [#61787](https://github.com/vllm-project/vllm/issues/61787) | [RFC]: Layerwise KV Pooling and P/D Disaggregation for High-Hit-Rate A | kv-connector, pooling | 2026-10-26 |
| [#63455](https://github.com/vllm-project/vllm/issues/63455) | [Bug]: [ROCm] AutoAWQ checkpoints never use the RDNA W4A16 kernel; AWQ | rocm, quantization | 2026-10-26 |
| [#51521](https://github.com/vllm-project/vllm/issues/51521) | DeepSeek-V4 (deepseek_v4): fused topk_softplus_sqrt router rejects non | — | 2026-10-26 |
| [#63666](https://github.com/vllm-project/vllm/issues/63666) | [RFC]: Tiered MoE Expert Offload with Lookahead Expert Scheduling (LES | intel-gpu, quantization | 2026-10-26 |
| [#61024](https://github.com/vllm-project/vllm/issues/61024) | [Roadmap] vLLM Roadmap Q4 2026 | rocm, quantization, kimi, k3 | 2026-10-26 |
| [#63267](https://github.com/vllm-project/vllm/issues/63267) | [Bug]: CUDA builds without FA extensions (Jetson Thor sm_110) cannot s | — | 2026-10-26 |
| [#63646](https://github.com/vllm-project/vllm/issues/63646) | [Bug]: Encountered an inference error when performing a single LLM API | bug, qwen | 2026-10-26 |
| [#48480](https://github.com/vllm-project/vllm/issues/48480) | [RFC]: Make Triton kernel unit tests hardware-agnostic and cover untes | stale | 2026-10-26 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 106 |
| Attention | 47 |
| MoE / Expert Parallel | 45 |
| Multimodal | 42 |
| Other | 41 |
| Serving / API | 39 |
| Disaggregation / PD | 29 |
| KV Cache / Offload | 27 |
| CI / Build | 25 |
| Models | 24 |
| Scheduler / Engine | 21 |
| LoRA | 18 |
| Speculative Decoding | 16 |
| Docs | 15 |
| Quantization | 14 |
| Perf / Benchmark | 9 |
| Compilation / CUDA Graph | 5 |

## ROCm / AMD  (106 commits)

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
- **2026-10-25** [`2c880f1e68`](https://github.com/vllm-project/vllm/commit/2c880f1e68) [#59223](https://github.com/vllm-project/vllm/pull/59223)
  [Bugfix] Preserve FP8 indexer WK pairs across load_weights calls (#59223)
  _Files: `.buildkite/test_areas/model_executor.yaml`, `tests/model_executor/model_loader/test_deepseek_v32_weight_loading.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/models/deepseek_v32/amd/model.py` _+3 more__
- **2026-10-25** [`f8c12c212a`](https://github.com/vllm-project/vllm/commit/f8c12c212a) [#63609](https://github.com/vllm-project/vllm/pull/63609)
  [CI] Disable jobs with unpinned runtime installs (#63609)
  _Files: `.buildkite/hardware_tests/ascend_npu.yaml`, `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/intel_jobs/misc_intel.yaml`, `.buildkite/intel_jobs/model_executor_intel.yaml` _+12 more__
- **2026-10-25** [`9d48c8ab95`](https://github.com/vllm-project/vllm/commit/9d48c8ab95) [#63608](https://github.com/vllm-project/vllm/pull/63608)
  [CI] Disable jobs with unlocked transitive dependencies (#63608)
  _Files: `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/lm_eval.yaml` _+3 more__
- **2026-10-25** [`a55937f255`](https://github.com/vllm-project/vllm/commit/a55937f255) [#60084](https://github.com/vllm-project/vllm/pull/60084)
  [ROCm][Perf] Restore 32-bit buffer addressing for TRITON_ATTN KV cache views (#60084)
  _Files: `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/backends/utils.py`_
- **2026-10-25** [`444d69110e`](https://github.com/vllm-project/vllm/commit/444d69110e) [#63520](https://github.com/vllm-project/vllm/pull/63520)
  [Doc][ROCm] Align Kimi-K3 MI355X AgentX recipe with InferenceX #4393 (#63520)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-24** [`56e4e42868`](https://github.com/vllm-project/vllm/commit/56e4e42868) [#62102](https://github.com/vllm-project/vllm/pull/62102)
  [GLM 5.3 Perf] Skip scale calculation for `concat_and_cache_mla`, 1.2% ~ 3.0% E2E TPOT improvement (#62102)
  _Files: `csrc/cache_kernels.cu`, `csrc/ops.h`, `csrc/torch_bindings.cpp`, `tests/kernels/test_fused_deepseek_v32_norm_rope.py` _+9 more__
- **2026-10-24** [`7822663cb4`](https://github.com/vllm-project/vllm/commit/7822663cb4) [#62713](https://github.com/vllm-project/vllm/pull/62713)
  [DeepSeek][ROCm] V4.1-Flash: enable --monokernel on MI325X (#62713)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-10-24** [`c0ba7e01ff`](https://github.com/vllm-project/vllm/commit/c0ba7e01ff) [#60413](https://github.com/vllm-project/vllm/pull/60413)
  [Perf][ROCm][Kernel] Add W4A8 int8-dot MXFP4 GEMV for RDNA3/RDNA3.5 d… (#60413)
  _Files: `CMakeLists.txt`, `csrc/rocm/mxfp4_w4a8_gemv_rdna3.cu`, `csrc/rocm/ops.h`, `csrc/rocm/torch_bindings.cpp` _+11 more__
- **2026-10-24** [`39504080e5`](https://github.com/vllm-project/vllm/commit/39504080e5) [#61628](https://github.com/vllm-project/vllm/pull/61628)
  [ROCm][MLA][DCP] Drop VLLM_ROCM_AITER_MLA_DCP_VERIFY (#61628)
  _Files: `tests/v1/attention/test_rocm_aiter_mla_dcp_cprr.py`, `tests/v1/attention/test_rocm_aiter_mla_dcp_cprr_numerics.py`, `vllm/envs.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-10-24** [`cba669d45d`](https://github.com/vllm-project/vllm/commit/cba669d45d) [#57909](https://github.com/vllm-project/vllm/pull/57909)
  [ROCm][PERF] Enable MiniMax-M3 Indexer CP (#57909)
  _Files: `tests/kernels/attention/test_indexer_msa.py`, `tests/kernels/attention/test_minimax_m3.py`, `tests/kernels/attention/test_minimax_m3_indexer_cp.py`, `vllm/config/attention.py` _+6 more__
- **2026-10-24** [`139feb4534`](https://github.com/vllm-project/vllm/commit/139feb4534) [#61482](https://github.com/vllm-project/vllm/pull/61482)
  [ROCm][Perf][DSv4] Standalone mono decode layer for DeepSeek-V4-Pro on MI355X (#61482)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_dsv4_mono_decode.py`, `tests/models/test_dsv4_mono_layers.py`, `tests/models/test_dsv4_mono_numerics.py` _+29 more__
- **2026-10-24** [`2aa7269a83`](https://github.com/vllm-project/vllm/commit/2aa7269a83) [#62473](https://github.com/vllm-project/vllm/pull/62473)
  [Bugfix][ROCm][MoRIIO] Release every prefill rank a READ holds (#62473)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `tests/v1/kv_connector/moriio_integration/test_write_dummy_e2e_rocm.py`, `tests/v1/kv_connector/unit/test_moriio_hetero_tp_write.py` _+5 more__
- **2026-10-24** [`7a64fb8fc9`](https://github.com/vllm-project/vllm/commit/7a64fb8fc9) [#63452](https://github.com/vllm-project/vllm/pull/63452)
  [CI] Fix the Domyn Edge (ROCm) and Qwen2 embed HF references (#63452)
  _Files: `tests/models/language/generation/test_common.py`, `tests/models/language/pooling/test_embedding.py`_
- **2026-10-24** [`a5b71c1eb3`](https://github.com/vllm-project/vllm/commit/a5b71c1eb3) [#62835](https://github.com/vllm-project/vllm/pull/62835)
  [Security] Refresh vulnerable runtime and test dependencies (#62835)
  _Files: `requirements/common.txt`, `requirements/kv_connectors.txt`, `requirements/kv_connectors_cu12.txt`, `requirements/test/cpu.txt` _+8 more__
- **2026-10-24** [`debcf22843`](https://github.com/vllm-project/vllm/commit/debcf22843) [#59100](https://github.com/vllm-project/vllm/pull/59100)
  [CI][ROCm] Export kernel source maps for CI selection (#59100)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/test_areas/docker.yaml`, `.buildkite/test_areas/misc.yaml`, `CMakeLists.txt` _+9 more__
- **2026-10-23** [`2c58be22b6`](https://github.com/vllm-project/vllm/commit/2c58be22b6) [#63131](https://github.com/vllm-project/vllm/pull/63131)
  [Bugfix][ROCm][Kimi-K3] Validate gfx942's int4 expert requant as int4 (#63131)
  _Files: `tests/kernels/moe/test_rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-10-23** [`96bbaa300f`](https://github.com/vllm-project/vllm/commit/96bbaa300f) [#60644](https://github.com/vllm-project/vllm/pull/60644)
  [ROCm][RDNA][Perf] W4A16: packed fp16 prefill dequant and tiles for gfx1151 (#60644)
  _Files: `benchmarks/kernels/benchmark_rdna_hybrid_w4a16_gemm.py`, `tests/kernels/quantization/test_rdna_hybrid_w4a16.py`, `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`_
- **2026-10-23** [`c7476c7a6f`](https://github.com/vllm-project/vllm/commit/c7476c7a6f) [#62384](https://github.com/vllm-project/vllm/pull/62384)
  [Feature][PCP] Support decoder-side SWA bounded replay with APC for DeepSeek-V4.1-Flash (#62384)
  _Files: `tests/models/test_deepseek_v41_amd_replay_forward.py`, `tests/models/test_deepseek_v41_pcp.py`, `tests/models/test_deepseek_v41_replay_batch.py`, `tests/v1/worker/test_gpu_pcp_manager.py` _+8 more__
- **2026-10-23** [`1a1540480d`](https://github.com/vllm-project/vllm/commit/1a1540480d) [#63400](https://github.com/vllm-project/vllm/pull/63400)
  [Refactor] Remove dead code models (#63400)
  _Files: `vllm/model_executor/models/llava_onevision.py`, `vllm/model_executor/models/phi4mm_utils.py`, `vllm/model_executor/models/radio.py`, `vllm/models/deepseek_v4/cpu/cpu_sparse.py` _+5 more__
- **2026-10-23** [`29cf023770`](https://github.com/vllm-project/vllm/commit/29cf023770) [#61649](https://github.com/vllm-project/vllm/pull/61649)
  [Refactor] [AMD] flydsl: Move UltraQuant/TurboQuant decode to public APIs (#61649)
  _Files: `tests/kernels/turboquant/test_flydsl_turboquant_decode.py`, `vllm/v1/attention/backends/turboquant_attn.py`, `vllm/v1/attention/ops/flydsl_kernels/buffer_utils.py`, `vllm/v1/attention/ops/flydsl_kernels/mma_utils.py` _+5 more__
- **2026-10-23** [`18df4cd9a9`](https://github.com/vllm-project/vllm/commit/18df4cd9a9) [#63268](https://github.com/vllm-project/vllm/pull/63268)
  [ROCm][Bugfix] Fix Triton paged decode leaving output heads unwritten on gfx942 (#63268)
  _Files: `tests/kernels/attention/test_prefix_prefill.py`, `vllm/v1/attention/ops/chunked_prefill_paged_decode.py`_
- **2026-10-23** [`be03d19750`](https://github.com/vllm-project/vllm/commit/be03d19750) [#62907](https://github.com/vllm-project/vllm/pull/62907)
  [CI][ROCm][MoE] Add MXFP4 SWIGLUOAI_UNINTERLEAVE/SITU test coverage on MI355 (#62907)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/test_modular_kernel_combinations.py`, `tests/kernels/utils.py`_
- **2026-10-23** [`bc3afc4096`](https://github.com/vllm-project/vllm/commit/bc3afc4096) [#63242](https://github.com/vllm-project/vllm/pull/63242)
  [CI][ROCm] Fail the AITER nightly overlay on wheels ci_base cannot load (#63242)
  _Files: `.buildkite/scripts/rocm/aiter-nightly-overlay.sh`_
- **2026-10-23** [`f869d64788`](https://github.com/vllm-project/vllm/commit/f869d64788) [#63283](https://github.com/vllm-project/vllm/pull/63283)
  [CI][ROCm] Run the online FP8 MoE batch-invariance test on ROCm (#63283)
  _Files: `tests/v1/determinism/test_batch_invariance.py`_
- **2026-10-23** [`b1c66e5545`](https://github.com/vllm-project/vllm/commit/b1c66e5545) [#62757](https://github.com/vllm-project/vllm/pull/62757)
  [ROCm][Model] Muse Spark: share one RoPE cache sized by max_model_len (#62757)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_muse_spark_rocm_shared_rope.py`, `vllm/models/muse_spark/amd/model.py`_
- **2026-10-23** [`224b2f54f1`](https://github.com/vllm-project/vllm/commit/224b2f54f1) [#62934](https://github.com/vllm-project/vllm/pull/62934)
  [ROCm][CI] Move NFS-affected MI300 test groups to MI355 (#62934)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/spec_decode.yaml`_
- **2026-10-23** [`74ba6384c2`](https://github.com/vllm-project/vllm/commit/74ba6384c2) [#63344](https://github.com/vllm-project/vllm/pull/63344)
  [Doc][ROCm] Document DeepSeek-V4.1-Flash MI355X AgentX TP2 profiles (#63344)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-10-23** [`c0a41721c7`](https://github.com/vllm-project/vllm/commit/c0a41721c7) [#63269](https://github.com/vllm-project/vllm/pull/63269)
  [CI][ROCm] Raise the MI355 MiniMax M3 MonoKernel timeout to 45 minutes (#63269)
  _Files: `.buildkite/test_areas/models_basic.yaml`_
- **2026-10-23** [`be08fa5355`](https://github.com/vllm-project/vllm/commit/be08fa5355) [#62827](https://github.com/vllm-project/vllm/pull/62827)
  [ROCm] Bump UCX to v1.23.0-rc1 so NIXL uses rocm_ipc (#62827)
  _Files: `docker/Dockerfile.rocm`, `docker/Dockerfile.rocm_72`_
- **2026-10-23** [`098eb89ea4`](https://github.com/vllm-project/vllm/commit/098eb89ea4) [#63031](https://github.com/vllm-project/vllm/pull/63031)
  [ROCm][Kimi-K3] Support MoRIIO consumers with specialized decode (#63031)
  _Files: `docs/features/moriio_connector_usage.md`, `tests/models/kimi_k3/amd_specialized_decode/test_runtime.py`, `vllm/models/kimi_k3/amd/specialized_decode/README.md`, `vllm/models/kimi_k3/amd/specialized_decode/runtime/__init__.py`_
- **2026-10-23** [`dc05b14556`](https://github.com/vllm-project/vllm/commit/dc05b14556) [#58743](https://github.com/vllm-project/vllm/pull/58743)
  [ROCm][Kimi-K3] Support BF16 KDA recurrent state (#58743)
  _Files: `csrc/kimi_k3/fused_kda_chunk_kernel_rocm.cu`, `tests/models/kimi_k3/test_amd_kda_chunk.py`, `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/kda.py` _+4 more__
- **2026-10-23** [`da180efbcd`](https://github.com/vllm-project/vllm/commit/da180efbcd) [#63257](https://github.com/vllm-project/vllm/pull/63257)
  [ROCm][Recipe] MiniMax-M3.1-Flash: MI355X PD, DBO / SP prefill, Quark MXFP4, mono decode (#63257)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-10-23** [`3dbf2b6c0c`](https://github.com/vllm-project/vllm/commit/3dbf2b6c0c) [#62756](https://github.com/vllm-project/vllm/pull/62756)
  [Bugfix][ROCm] Muse Spark: apply output multiplier and softcap in compute_logits_local (#62756)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_muse_spark_logits_local.py`, `vllm/models/muse_spark/amd/model.py`_
- **2026-10-23** [`2d40c0609f`](https://github.com/vllm-project/vllm/commit/2d40c0609f) [#61855](https://github.com/vllm-project/vllm/pull/61855)
  [ROCm][Perf] Triton port of the fused GDN MTP decode kernel (#61855)
  _Files: `tests/kernels/fla/test_fused_gdn_post_conv.py`, `tests/kernels/mamba/test_gdn_fused_mtp.py`, `tests/model_executor/test_qwen_triton_warmup.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py` _+2 more__
- **2026-10-23** [`022b43c66f`](https://github.com/vllm-project/vllm/commit/022b43c66f) [#60834](https://github.com/vllm-project/vllm/pull/60834)
  [ROCm][Perf] Apply opt-in paged MXFP4 sparse indexer dense path for DeepSeek-V4 (#60834)
  _Files: `tests/kernels/attention/test_rocm_dsv4_mxfp4_indexer.py`, `vllm/model_executor/warmup/jit_warmup_triton_helper.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py` _+6 more__
- **2026-10-23** [`f120f1dbf2`](https://github.com/vllm-project/vllm/commit/f120f1dbf2) [#63082](https://github.com/vllm-project/vllm/pull/63082)
  [Bugfix][ROCm][MiniMax-M3] Reject IndexCache overrides that miss text_config (#63082)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `tests/models/minimax_m3/test_index_cache_overrides.py`, `vllm/model_executor/models/config.py` _+1 more__
- **2026-10-22** [`cc1a6d3135`](https://github.com/vllm-project/vllm/commit/cc1a6d3135) [#63105](https://github.com/vllm-project/vllm/pull/63105)
  [ROCm][Build] Reland #62475: paged attention kernel split with `--offload-compress` => x4-x7 wheel build speedup on ROCm (#63105)
  _Files: `CMakeLists.txt`, `csrc/rocm/attention_dispatch.cu`, `csrc/rocm/attention_kernels.cuh`, `csrc/rocm/attention_paged_attn_h128_bf16_auto.cu` _+12 more__
- **2026-10-22** [`6d1909a1f2`](https://github.com/vllm-project/vllm/commit/6d1909a1f2) [#63007](https://github.com/vllm-project/vllm/pull/63007)
  [Bugfix][ROCm][DSv4.1] Gather Engram hashes across DP replicas in the AMD model (#63007)
  _Files: `tests/distributed/test_engram_dp_shard.py`, `vllm/models/deepseek_v41/amd/model.py`_
- **2026-10-22** [`f01a76f950`](https://github.com/vllm-project/vllm/commit/f01a76f950) [#63009](https://github.com/vllm-project/vllm/pull/63009)
  [ROCm][DSv4.1] Allocate offloaded Engram tables at their exact size (#63009)
  _Files: `tests/kernels/test_engram.py`, `vllm/config/engram.py`, `vllm/models/deepseek_v41/common/engram.py`_
- **2026-10-22** [`1d3e4006c4`](https://github.com/vllm-project/vllm/commit/1d3e4006c4) [#62099](https://github.com/vllm-project/vllm/pull/62099)
  [ROCm][CI] Fix int8 GEMM kernel selection logic for ROCm platform (#62099)
  _Files: `tests/kernels/quantization/test_scaled_mm_kernel_selection.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/ScaledMMLinearKernel.py`, `vllm/model_executor/kernels/linear/scaled_mm/aiter.py` _+2 more__
- **2026-10-22** [`90aa823cba`](https://github.com/vllm-project/vllm/commit/90aa823cba) [#63127](https://github.com/vllm-project/vllm/pull/63127)
  [ROCm][CI] Download quick-reduce e2e model when cached snapshot has no weights (#63127)
  _Files: `tests/distributed/test_rocm_quick_reduce.py`_
- **2026-10-22** [`168a86ab8f`](https://github.com/vllm-project/vllm/commit/168a86ab8f) [#60238](https://github.com/vllm-project/vllm/pull/60238)
  [Multimodal] Skip encoder towers on later PP stages under V2 (#60238)
  _Files: `tests/models/transformers/test_backend.py`, `vllm/model_executor/models/interfaces.py`, `vllm/models/qwen4_exp/amd/model.py`, `vllm/models/qwen4_exp/nvidia/model.py`_
- **2026-10-22** [`fa72b61b55`](https://github.com/vllm-project/vllm/commit/fa72b61b55) [#62868](https://github.com/vllm-project/vllm/pull/62868)
  [Security] Refresh Python and runtime CA certificates (#62868)
  _Files: `docker/Dockerfile`, `docs/contributing/dockerfile/dockerfile.md`, `pyproject.toml`, `requirements/common.txt` _+6 more__
- **2026-10-22** [`6ab6bff1b6`](https://github.com/vllm-project/vllm/commit/6ab6bff1b6) [#62622](https://github.com/vllm-project/vllm/pull/62622)
  [Model][ROCm] Add Muse Spark Open support on ROCm (#62622)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/models_basic.yaml` _+87 more__
- **2026-10-22** [`f46ea25e58`](https://github.com/vllm-project/vllm/commit/f46ea25e58) [#58660](https://github.com/vllm-project/vllm/pull/58660)
  [Perf][Frontend] Share orjson responses across render and pooling (#58660)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt` _+12 more__
- **2026-10-22** [`aa31fa038f`](https://github.com/vllm-project/vllm/commit/aa31fa038f) [#61862](https://github.com/vllm-project/vllm/pull/61862)
  [CI] Move V1 Attention, core kernels and quantization AMD mirrors from fixed to automatic shards (#61862)
  _Files: `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/quantization.yaml`_
- **2026-10-22** [`05406ba470`](https://github.com/vllm-project/vllm/commit/05406ba470) [#62994](https://github.com/vllm-project/vllm/pull/62994)
  [ROCm][Perf][MiniMax-M3] MonoKernel: serve EAGLE3 verify steps (#62994)
  _Files: `tests/models/minimax_m3/amd_specialized_decode/test_model.py`, `tests/models/minimax_m3/amd_specialized_decode/test_runtime.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/sparse_attn.py` _+3 more__
- **2026-10-22** [`9d61ade7f6`](https://github.com/vllm-project/vllm/commit/9d61ade7f6) [#62475](https://github.com/vllm-project/vllm/pull/62475)
  [ROCm] Revert "[ROCm][Build] Compile paged attention kernels in parallel (7.6x faster attention build) (#62475)" (#62983)
  _Files: `CMakeLists.txt`, `csrc/rocm/attention.cu`, `csrc/rocm/attention_dispatch.cu`, `csrc/rocm/attention_paged_attn_h128_bf16_auto.cu` _+12 more__
- **2026-10-22** [`a4aa37d1a0`](https://github.com/vllm-project/vllm/commit/a4aa37d1a0) [#57481](https://github.com/vllm-project/vllm/pull/57481)
  [ROCm] Capture CUDA graphs with expandable segments off for AITER all-reduce (#57481)
  _Files: `tests/device_allocator/test_alloc_conf.py`, `tests/distributed/test_rocm_aiter_custom_ar.py`, `vllm/device_allocator/alloc_conf.py`, `vllm/distributed/device_communicators/aiter_custom_all_reduce.py` _+1 more__
- **2026-10-22** [`a6020fc669`](https://github.com/vllm-project/vllm/commit/a6020fc669) [#62977](https://github.com/vllm-project/vllm/pull/62977)
  [ROCm] Add _maybe_pad_weight guard-condition and RL-reload stability tests (#62977)
  _Files: `tests/rocm/test_moe_padding.py`_
- **2026-10-21** [`833349105b`](https://github.com/vllm-project/vllm/commit/833349105b) [#58509](https://github.com/vllm-project/vllm/pull/58509)
  [ROCm][Perf] HY4 preview perf boost (#58509)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `benchmarks/kernels/benchmark_hy_v4_ihc.py`, `tests/kernels/test_minimax_m3_amd_ops.py`, `tests/models/hy_v4/test_triton_ihc.py` _+6 more__
- **2026-10-21** [`c84edac4cb`](https://github.com/vllm-project/vllm/commit/c84edac4cb) [#62893](https://github.com/vllm-project/vllm/pull/62893)
  [ROCm][CI] Enable batch invariance for eagle3 scheduling accuracy (#62893)
  _Files: `tests/v1/e2e/general/test_async_scheduling_accuracy.py`_
- **2026-10-21** [`f143f65d7c`](https://github.com/vllm-project/vllm/commit/f143f65d7c) [#62882](https://github.com/vllm-project/vllm/pull/62882)
  [CI][ROCm] Set the FP8 MLA prefill scale cache in the test double (#62882)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_fp8_prefill.py`_
- **2026-10-21** [`db3b0f0fae`](https://github.com/vllm-project/vllm/commit/db3b0f0fae) [#60808](https://github.com/vllm-project/vllm/pull/60808)
  [Bugfix][KV Connector][ROCm] MoRIIO READ: await every read before the forward (#60808)
  _Files: `tests/v1/kv_connector/unit/test_moriio_tp_ack.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`_
- **2026-10-21** [`d7ada3aace`](https://github.com/vllm-project/vllm/commit/d7ada3aace) [#62869](https://github.com/vllm-project/vllm/pull/62869)
  [CI][ROCm] Give the M3 embed-sharing fixture a kernel_config (#62869)
  _Files: `tests/v1/worker/test_spec_decode_embed_sharing_pp.py`_
- **2026-10-21** [`e9cc6244a0`](https://github.com/vllm-project/vllm/commit/e9cc6244a0) [#62721](https://github.com/vllm-project/vllm/pull/62721)
  [Rust Frontend] Refresh rust/AGENTS.md with ownership and design conventions (#62721)
  _Files: `AGENTS.md`, `rust/AGENTS.md`_
- **2026-10-21** [`64c5f14f6a`](https://github.com/vllm-project/vllm/commit/64c5f14f6a) [#59266](https://github.com/vllm-project/vllm/pull/59266)
  [ROCm][DI][CI] Enable WideEP EP16/DP16 tests  (#59266)
  _Files: `.buildkite/amd-disagg/cluster.sh`, `.buildkite/amd-disagg/models.yaml`, `.buildkite/amd-disagg/pipeline-disagg.yaml`, `.buildkite/amd-disagg/run-slurm-disagg-test.sh` _+3 more__
- **2026-10-21** [`153b76b304`](https://github.com/vllm-project/vllm/commit/153b76b304) [#57832](https://github.com/vllm-project/vllm/pull/57832)
  [ROCm][Model][MiniMax-M3] Context-parallel sparse lightning indexer (Triton, opt-in) (#57832)
  _Files: `.buildkite/test-amd.yaml`, `tests/distributed/test_minimax_m3_indexer_cp_tp.py`, `tests/kernels/attention/test_minimax_m3_indexer_cp.py`, `vllm/config/attention.py` _+4 more__
- **2026-10-21** [`385d1dab3b`](https://github.com/vllm-project/vllm/commit/385d1dab3b) [#62712](https://github.com/vllm-project/vllm/pull/62712)
  [ROCm][Perf][MiniMax-M3] MonoKernel decode for M3 MXFP4 on MI355X (#62712)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `tests/models/minimax_m3/amd_specialized_decode/_xcd_stress.py`, `tests/models/minimax_m3/amd_specialized_decode/test_model.py` _+22 more__
- **2026-10-21** [`fc377f7771`](https://github.com/vllm-project/vllm/commit/fc377f7771) [#62405](https://github.com/vllm-project/vllm/pull/62405)
  [Quantization] Use replace_parameter for params re-created in process_weights_after_loading (#62405)
  _Files: `tests/quantization/test_keep_param_objects.py`, `tests/quantization/test_modelopt.py`, `vllm/model_executor/kernels/linear/mixed_precision/cpu.py`, `vllm/model_executor/kernels/linear/mixed_precision/exllama.py` _+36 more__
- **2026-10-21** [`a9bf45ed8a`](https://github.com/vllm-project/vllm/commit/a9bf45ed8a) [#60683](https://github.com/vllm-project/vllm/pull/60683)
  [ROCm][Perf][Kimi-K3] Specialized decode for Kimi-K3 on MI355X (#60683)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/kimi_k3/amd_specialized_decode/__init__.py`, `tests/models/kimi_k3/amd_specialized_decode/test_engine_fault.py`, `tests/models/kimi_k3/amd_specialized_decode/test_numerics.py` _+30 more__
- **2026-10-21** [`e8ae84bf7e`](https://github.com/vllm-project/vllm/commit/e8ae84bf7e) [#62475](https://github.com/vllm-project/vllm/pull/62475)
  [ROCm][Build] Compile paged attention kernels in parallel (7.6x faster attention build) (#62475)
  _Files: `CMakeLists.txt`, `csrc/rocm/attention_dispatch.cu`, `csrc/rocm/attention_kernels.cuh`, `csrc/rocm/attention_paged_attn_h128_bf16_auto.cu` _+12 more__
- **2026-10-21** [`aca582857b`](https://github.com/vllm-project/vllm/commit/aca582857b) [#62646](https://github.com/vllm-project/vllm/pull/62646)
  [CI][ROCm] Mirror the Distributed Preload group on MI355 (#62646)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`_
- **2026-10-21** [`27aadb3096`](https://github.com/vllm-project/vllm/commit/27aadb3096) [#62403](https://github.com/vllm-project/vllm/pull/62403)
  [ROCm][Bugfix] Fix wrong output of the QK-norm + RoPE + KV-cache fusion on ROCM_ATTN (#62403)
  _Files: `tests/compile/passes/test_rocm_aiter_qk_norm_rope_kvcache_fusion.py`, `tests/compile/passes/test_rope_kvcache_fusion.py`, `vllm/compilation/passes/fusion/qk_norm_rope_kvcache_fusion.py`, `vllm/v1/attention/backends/rocm_attn.py`_
- **2026-10-21** [`e632d66433`](https://github.com/vllm-project/vllm/commit/e632d66433) [#61058](https://github.com/vllm-project/vllm/pull/61058)
  [CI] Fix Buildkite path filters that point at moved or deleted files (#61058)
  _Files: `.buildkite/ci_config_rocm.yaml`, `.buildkite/hardware_tests/ascend_npu.yaml`, `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/misc_intel.yaml` _+10 more__
- **2026-10-20** [`b1ab16c548`](https://github.com/vllm-project/vllm/commit/b1ab16c548) [#62486](https://github.com/vllm-project/vllm/pull/62486)
  [ROCm] Bump AITER to v1.26.0 (#62486)
  _Files: `docker/Dockerfile.rocm_72_base`, `docker/Dockerfile.rocm_base`, `tests/kernels/moe/test_rocm_aiter_moe.py`_
- **2026-10-20** [`0f30006267`](https://github.com/vllm-project/vllm/commit/0f30006267) [#62735](https://github.com/vllm-project/vllm/pull/62735)
  [ROCm][CI][Bug] Remove padding from AITER output for quantization/tes… (#62735)
  _Files: `tests/quantization/test_online_shared_expert_fusion.py`_
- **2026-10-20** [`9da5f2d310`](https://github.com/vllm-project/vllm/commit/9da5f2d310) [#60250](https://github.com/vllm-project/vllm/pull/60250)
  [ROCm] Enable the rms_norm_gated custom op by default (Qwen3.8-27B) (#60250)
  _Files: `tests/compile/passes/test_fusion.py`, `vllm/compilation/passes/fusion/matcher_utils.py`, `vllm/model_executor/layers/layernorm.py`, `vllm/platforms/rocm.py`_
- **2026-10-20** [`09fd027217`](https://github.com/vllm-project/vllm/commit/09fd027217) [#59634](https://github.com/vllm-project/vllm/pull/59634)
  [ROCm][Perf][Kimi-K3] Fuse the GLA gate GEMM and the MLA FP8 prefill q/k/v prep (#59634)
  _Files: `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/mla.py`, `vllm/models/kimi_k3/amd/mtp.py` _+1 more__
- **2026-10-20** [`005cef040a`](https://github.com/vllm-project/vllm/commit/005cef040a) [#62731](https://github.com/vllm-project/vllm/pull/62731)
  [CI][ROCm] Remove MI300 Model Runner V2 steps (#62731)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-10-20** [`6e780d14cd`](https://github.com/vllm-project/vllm/commit/6e780d14cd) [#62032](https://github.com/vllm-project/vllm/pull/62032)
  [CI][ROCm] Use AITER prebuilt fp8 MoE modules when inter dim is 256 aligned (#62032)
  _Files: `tests/kernels/moe/modular_kernel_tools/common.py`_
- **2026-10-20** [`82b7dad5e3`](https://github.com/vllm-project/vllm/commit/82b7dad5e3) [#61790](https://github.com/vllm-project/vllm/pull/61790)
  [Test][UMBP][2/10] Add shared connector contract coverage (#61790)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `tests/v1/kv_connector/umbp_test_utils.py`, `tests/v1/kv_connector/unit/test_umbp_core.py` _+4 more__
- **2026-10-20** [`4a30738d21`](https://github.com/vllm-project/vllm/commit/4a30738d21) [#41197](https://github.com/vllm-project/vllm/pull/41197)
  [ROCm][benchmark][perf] fix moe tuning script for RDNA (#41197)
  _Files: `benchmarks/kernels/benchmark_moe.py`_
- **2026-10-20** [`11a8d571d2`](https://github.com/vllm-project/vllm/commit/11a8d571d2) [#62680](https://github.com/vllm-project/vllm/pull/62680)
  [CI][AMD] Deselect distributed tests in the MI300 Model Executor step (#62680)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-10-20** [`a6c898e2a9`](https://github.com/vllm-project/vllm/commit/a6c898e2a9) [#62686](https://github.com/vllm-project/vllm/pull/62686)
  [CI][AMD] Shard the MI300 V1 Spec Decode step (#62686)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-10-20** [`e2d2680417`](https://github.com/vllm-project/vllm/commit/e2d2680417) [#62039](https://github.com/vllm-project/vllm/pull/62039)
  [CI] Shard E2E Scheduling, Benchmarks CLI and six AMD mirrors automatically (#62039)
  _Files: `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/lm_eval.yaml` _+1 more__
- **2026-10-20** [`87fa712793`](https://github.com/vllm-project/vllm/commit/87fa712793) [#62562](https://github.com/vllm-project/vllm/pull/62562)
  [CI] Shard (H200 MIG 35GB / MI355 DPX) Multimodal Models (Standard) 4 automatically (#62562)
  _Files: `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-10-20** [`f85e39ea01`](https://github.com/vllm-project/vllm/commit/f85e39ea01) [#57916](https://github.com/vllm-project/vllm/pull/57916)
  [ROCm][Quantization][MOE] Enable fused shared experts for MXFP8 checkpoints (#57916)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `vllm/model_executor/layers/quantization/utils/config_utils.py`_
- **2026-10-20** [`428cd0cb4a`](https://github.com/vllm-project/vllm/commit/428cd0cb4a) [#62421](https://github.com/vllm-project/vllm/pull/62421)
  [ROCm][Model] DeepSeek-V4.1 VL: stream language-model weights on ROCm (#62421)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_deepseek_v4_vl_stream_weights.py`, `vllm/models/deepseek_v41/amd/vl_model.py`_
- **2026-10-20** [`9499c949be`](https://github.com/vllm-project/vllm/commit/9499c949be) [#52670](https://github.com/vllm-project/vllm/pull/52670)
  [Quantizaiton][Feature] Pluggable KV Cache Data Types (#52670)
  _Files: `benchmarks/kernels/cpu/benchmark_cpu_attn.py`, `tests/config/test_kv_cache_dtype.py`, `tests/utils_/test_torch_utils.py`, `tests/v1/attention/test_attention_backends.py` _+46 more__
- **2026-10-20** [`1a74cc7bb2`](https://github.com/vllm-project/vllm/commit/1a74cc7bb2) [#60731](https://github.com/vllm-project/vllm/pull/60731)
  [ROCm][Perf][DSv4.1] Mono decode on MI300X and MI325X (gfx942) (#60731)
  _Files: `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/models_basic.yaml`, `tests/kernels/models/__init__.py`, `tests/kernels/models/amd/__init__.py` _+41 more__
- **2026-10-19** [`53172fa72e`](https://github.com/vllm-project/vllm/commit/53172fa72e) [#61983](https://github.com/vllm-project/vllm/pull/61983)
  [CI] Bump Transformers version to 5.20.0 (#61983)
  _Files: `.agents/skills/transformers-upgrade/SKILL.md`, `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in` _+9 more__
- **2026-10-19** [`8c60cf07b3`](https://github.com/vllm-project/vllm/commit/8c60cf07b3) [#62567](https://github.com/vllm-project/vllm/pull/62567)
  [CI] Keep the AMD mirrors of the nightly-only 4xL4 steps on PRs (#62567)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/distributed.yaml`_
- **2026-10-19** [`b439421f11`](https://github.com/vllm-project/vllm/commit/b439421f11) [#62520](https://github.com/vllm-project/vllm/pull/62520)
  [CI][ROCm] Raise data_parallel_offline.py --timeout in AMD Torchrun + Examples (#62520)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`_
- **2026-10-19** [`c8fbb79406`](https://github.com/vllm-project/vllm/commit/c8fbb79406) [#60886](https://github.com/vllm-project/vllm/pull/60886)
  [ROCm][MoE] Add AITER MXFP4 W4A16/W4A4 modular-kernel test coverage (#60886)
  _Files: `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/modular_kernel_tools/mk_objects.py`, `tests/kernels/moe/test_modular_kernel_combinations.py`, `tests/kernels/moe/test_rocm_aiter_moe.py` _+1 more__
- **2026-10-19** [`5caabdbb65`](https://github.com/vllm-project/vllm/commit/5caabdbb65) [#62390](https://github.com/vllm-project/vllm/pull/62390)
  [Frontend] Consolidate startup utils. (#62390)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `docs/mkdocs/gen_files/generate_argparse.py`, `rust/src/cmd/src/cli/unsupported.rs` _+34 more__
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

## Attention  (47 commits)

- **2026-10-26** [`6674eedd28`](https://github.com/vllm-project/vllm/commit/6674eedd28) [#63530](https://github.com/vllm-project/vllm/pull/63530)
  [XPU] Fix MLA cache op arguments (#63530)
  _Files: `vllm/_custom_ops.py`_
- **2026-10-26** [`bbf3d92190`](https://github.com/vllm-project/vllm/commit/bbf3d92190) [#63560](https://github.com/vllm-project/vllm/pull/63560)
  [Recipe] DeepSeek-V4.1-Flash: AgentX lanes as tuned presets (#63560)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`, `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`, `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-25** [`fa2881ed19`](https://github.com/vllm-project/vllm/commit/fa2881ed19) [#63177](https://github.com/vllm-project/vllm/pull/63177)
  [CI][Benchmarks] Fix attention smoke test backend names and failure exit status (#63177)
  _Files: `.buildkite/test_areas/benchmarks.yaml`, `benchmarks/attention_benchmarks/benchmark.py`, `docs/benchmarking/cli.md`_
- **2026-10-25** [`94a29d316e`](https://github.com/vllm-project/vllm/commit/94a29d316e) [#63088](https://github.com/vllm-project/vllm/pull/63088)
  [Fast Start] Add daemon-to-daemon warmup cache seeding for Preload (#63088)
  _Files: `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `tests/model_executor/test_flashinfer_autotune_warmup.py`, `vllm/entrypoints/cli/preload.py` _+6 more__
- **2026-10-24** [`e7473bf686`](https://github.com/vllm-project/vllm/commit/e7473bf686) [#63466](https://github.com/vllm-project/vllm/pull/63466)
  [Kernel] Bump up FlashInfer to 0.7.2.post1 (#63466)
  _Files: `requirements/cuda.txt`_
- **2026-10-24** [`5f63ea461c`](https://github.com/vllm-project/vllm/commit/5f63ea461c) [#63001](https://github.com/vllm-project/vllm/pull/63001)
  [Bugfix][Quantization][Spec Decode] Load ModelOpt mixed-precision DFlash and DSpark drafts (#63001)
  _Files: `.buildkite/test_areas/quantization.yaml`, `docs/features/quantization/modelopt.md`, `tests/config/test_model_arch_config.py`, `tests/quantization/test_modelopt.py` _+5 more__
- **2026-10-24** [`c50aca1441`](https://github.com/vllm-project/vllm/commit/c50aca1441) [#63428](https://github.com/vllm-project/vllm/pull/63428)
  [Doc][Recipe] MiniMax-M3.1-Flash: DEP2 + DEP4 PD on GB200/GB300, 7-token FLASHINFER_TS DSpark on NVIDIA (#63428)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-10-23** [`f3871c3cbf`](https://github.com/vllm-project/vllm/commit/f3871c3cbf) [#63339](https://github.com/vllm-project/vllm/pull/63339)
  [Bugfix][CPU] Match GPU conv-state layout in GDN spec decode (#63339)
  _Files: `tests/kernels/mamba/cpu/test_cpu_gdn_ops.py`, `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py`_
- **2026-10-23** [`eff8a56896`](https://github.com/vllm-project/vllm/commit/eff8a56896) [#63244](https://github.com/vllm-project/vllm/pull/63244)
  [Doc][Recipe] MiniMax-M3.1-Flash: add Hopper FP8 variant, Docker-only install (#63244)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-10-23** [`d05b1c8305`](https://github.com/vllm-project/vllm/commit/d05b1c8305) [#63236](https://github.com/vllm-project/vllm/pull/63236)
  [Doc][Recipe] Add MiniMax-M3.1-Flash recipe (#63236)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.1-Flash.yaml`_
- **2026-10-23** [`0bfeb8d0e3`](https://github.com/vllm-project/vllm/commit/0bfeb8d0e3) [#54163](https://github.com/vllm-project/vllm/pull/54163)
  [Bugfix][Spec Decode] DFlash/DSpark no longer drop the last prefix-cache block (mamba align context recompute) (#54163)
  _Files: `tests/test_config.py`, `tests/v1/core/test_scheduler.py`, `vllm/config/speculative.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-22** [`856b98415b`](https://github.com/vllm-project/vllm/commit/856b98415b) [#62784](https://github.com/vllm-project/vllm/pull/62784)
  [Spec Decode][MRV2] Skip drafting in steps where no request can use the drafts (#62784)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/worker/test_gpu_dp_utils.py`, `tests/v1/worker/test_gpu_ubatch_slicing.py`, `vllm/v1/core/sched/output.py` _+5 more__
- **2026-10-22** [`2a038794e0`](https://github.com/vllm-project/vllm/commit/2a038794e0) [#58304](https://github.com/vllm-project/vllm/pull/58304)
  [Bugfix][Attention] Fix FA4 FP8 descale strides for singleton KV heads (#58304)
  _Files: `tests/kernels/attention/test_flash_attn_interface.py`, `vllm/vllm_flash_attn/flash_attn_interface.py`_
- **2026-10-22** [`4a40c61130`](https://github.com/vllm-project/vllm/commit/4a40c61130) [#63147](https://github.com/vllm-project/vllm/pull/63147)
  [Bugfix] Add SM100 support for Step-5-Preview (#63147)
  _Files: `vllm/models/step5/nvidia/model.py`, `vllm/models/step5/nvidia/sparse_attention.py`_
- **2026-10-22** [`71e9320633`](https://github.com/vllm-project/vllm/commit/71e9320633) [#60532](https://github.com/vllm-project/vllm/pull/60532)
  [Attention] Decode FlashInfer spec queries with fa2 on pre-SM90 GPUs (#60532)
  _Files: `tests/v1/attention/test_attention_backends.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-10-22** [`0ad6ec839e`](https://github.com/vllm-project/vllm/commit/0ad6ec839e) [#60405](https://github.com/vllm-project/vllm/pull/60405)
  [CPU][GDN] Route FP16 attention through Triton/FLA (#60405)
  _Files: `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py`_
- **2026-10-22** [`f9b0a11fe2`](https://github.com/vllm-project/vllm/commit/f9b0a11fe2) [#62665](https://github.com/vllm-project/vllm/pull/62665)
  [Bugfix][CPU] Reject unsupported --kv-cache-dtype at CPU attention backend selection (#62665)
  _Files: `tests/kernels/attention/test_cpu_attn.py`, `vllm/platforms/cpu.py`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-10-22** [`b3b0bc3059`](https://github.com/vllm-project/vllm/commit/b3b0bc3059) [#56937](https://github.com/vllm-project/vllm/pull/56937)
  [Refactor][Multimodal] Refactor and unify mm prefix range computation (#56937)
  _Files: `vllm/v1/attention/backends/utils.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/model_states/default.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-10-22** [`b579949edf`](https://github.com/vllm-project/vllm/commit/b579949edf) [#61615](https://github.com/vllm-project/vllm/pull/61615)
  [Perf] Enable small-head FlashMLA sparse prefill for DS V4.1 on SM90 (#61615)
  _Files: `cmake/external_projects/flashmla.cmake`, `vllm/models/deepseek_v41/nvidia/flashmla.py`_
- **2026-10-22** [`4643f41853`](https://github.com/vllm-project/vllm/commit/4643f41853) [#62971](https://github.com/vllm-project/vllm/pull/62971)
  [Doc] DeepSeek-V4.1-Flash: fix TP4 c32 max-num-seqs in the B200 AgentX guide (#62971)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-10-21** [`aa4ec2093f`](https://github.com/vllm-project/vllm/commit/aa4ec2093f) [#62954](https://github.com/vllm-project/vllm/pull/62954)
  [Doc] DeepSeek-V4.1-Flash: document B200 AgentX router and drop removed c64 points (#62954)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-10-21** [`b6078025b4`](https://github.com/vllm-project/vllm/commit/b6078025b4) [#61489](https://github.com/vllm-project/vllm/pull/61489)
  [Docs] Point users at --disable-flashinfer-autotune (#61489)
  _Files: `benchmarks/replayssm/e2e_decode_speedup.py`, `docs/design/optimization_levels.md`, `recipes/models/MiniMaxAI/MiniMax-M3.yaml`, `recipes/models/deepseek-ai/DeepSeek-V3.2.yaml` _+20 more__
- **2026-10-21** [`35d01660ff`](https://github.com/vllm-project/vllm/commit/35d01660ff) [#62244](https://github.com/vllm-project/vllm/pull/62244)
  [XPU] Enable spec-decode adaptive verification without a confidence head (#62244)
  _Files: `tests/v1/spec_decode/test_acceptance_estimator.py`, `vllm/v1/attention/backends/flash_attn.py`_
- **2026-10-21** [`885592732a`](https://github.com/vllm-project/vllm/commit/885592732a) [#62831](https://github.com/vllm-project/vllm/pull/62831)
  [CI] Assert CPU scheduler metadata is present in group-head test (#62831)
  _Files: `tests/v1/attention/test_group_head_counts.py`_
- **2026-10-21** [`8e2beaa3bf`](https://github.com/vllm-project/vllm/commit/8e2beaa3bf) [#62798](https://github.com/vllm-project/vllm/pull/62798)
  [Doc] Kimi-K3: DCP selector and TOKENSPEED_MLA draft backend on GB200/GB300 (#62798)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-21** [`900828023a`](https://github.com/vllm-project/vllm/commit/900828023a) [#59082](https://github.com/vllm-project/vllm/pull/59082)
  [CPU] Improve long-context MTP attention scheduling on AMX (#59082)
  _Files: `benchmarks/kernels/cpu/benchmark_cpu_attn.py`, `csrc/cpu/cpu_attn_impl.hpp`, `tests/kernels/attention/test_cpu_attn.py`, `tests/v1/attention/test_group_head_counts.py`_
- **2026-10-21** [`d6d5412ca5`](https://github.com/vllm-project/vllm/commit/d6d5412ca5) [#62014](https://github.com/vllm-project/vllm/pull/62014)
  [XPU][Attention] Route multimodal prefix masks through the Triton/FlashAttention composite (#62014)
  _Files: `vllm/model_executor/models/config.py`, `vllm/platforms/xpu.py`, `vllm/v1/attention/backends/flash_attn.py`, `vllm/v1/attention/backends/triton_flash_attn.py`_
- **2026-10-20** [`9d4192aaa1`](https://github.com/vllm-project/vllm/commit/9d4192aaa1) [#59611](https://github.com/vllm-project/vllm/pull/59611)
  [Bugfix][DeepSeek V4] Load redundant EPLB expert slots (#59611)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-EPLB-TEP4.yaml`, `tests/evals/gsm8k/configs/models-spec-decode.txt`, `tests/evals/gsm8k/eplb_checks.py` _+3 more__
- **2026-10-20** [`c6936455a9`](https://github.com/vllm-project/vllm/commit/c6936455a9) [#61186](https://github.com/vllm-project/vllm/pull/61186)
  [CI] Add Nightly to optional Buildkite step labels (#61186)
  _Files: `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/disaggregated.yaml` _+14 more__
- **2026-10-20** [`6083fdeaa2`](https://github.com/vllm-project/vllm/commit/6083fdeaa2) [#62541](https://github.com/vllm-project/vllm/pull/62541)
  [Doc] Document the DeepSeek-V4.1-Flash B200 AgentX profile in the guide and command builder (#62541)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-10-20** [`7b569ec895`](https://github.com/vllm-project/vllm/commit/7b569ec895) [#62029](https://github.com/vllm-project/vllm/pull/62029)
  [Attention] Use trtllm-gen for the FlashInfer DCP prefill context pass (#62029)
  _Files: `tests/kernels/attention/test_flashinfer_trtllm_attention.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-10-20** [`39568e2ec7`](https://github.com/vllm-project/vllm/commit/39568e2ec7) [#62670](https://github.com/vllm-project/vllm/pull/62670)
  [Doc] Document DeepSeek-V4.1-Flash B300 aggregate AgentX config (#62670)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-10-20** [`bc01c06922`](https://github.com/vllm-project/vllm/commit/bc01c06922) [#61601](https://github.com/vllm-project/vllm/pull/61601)
  [Perf][Qwen4Exp] Internal prefill checkpoints for the PLE short conv (#61601)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/kernels/mamba/test_checkpoint_exporter.py`, `tests/models/qwen4_exp/test_ple.py`, `vllm/model_executor/layers/mamba/abstract.py` _+4 more__
- **2026-10-20** [`143ee3b4c9`](https://github.com/vllm-project/vllm/commit/143ee3b4c9) [#62593](https://github.com/vllm-project/vllm/pull/62593)
  [Misc] Fix pre-commit failure on main from conflicts between pluggable KV cache and Step5 (#62593)
  _Files: `vllm/models/step5/nvidia/sparse_attention.py`_
- **2026-10-20** [`e10ecb6bd6`](https://github.com/vllm-project/vllm/commit/e10ecb6bd6) [#60373](https://github.com/vllm-project/vllm/pull/60373)
  [Bugfix][DCP] Support strided LSE in direct A2A reduction (#60373)
  _Files: `.buildkite/test_areas/distributed.yaml`, `csrc/attention/dcp_utils/dcp_direct_a2a_lse_reduce.cu`, `tests/distributed/test_dcp_direct_a2a_lse_reduce.py`, `tools/pre_commit/test_tethering_allowlist.txt`_
- **2026-10-20** [`2296c12e47`](https://github.com/vllm-project/vllm/commit/2296c12e47) [#62561](https://github.com/vllm-project/vllm/pull/62561)
  [Doc] Document DeepSeek-V4.1-Flash B300 Dynamo disaggregated profile (#62561)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
- **2026-10-20** [`45ce4050bc`](https://github.com/vllm-project/vllm/commit/45ce4050bc) [#58471](https://github.com/vllm-project/vllm/pull/58471)
  [Bugfix][KV Connector][NIXL] Shard a GQA draft's KV by head under an MLA target (#58471)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `tests/v1/kv_connector/unit/test_tp_mapping.py` _+3 more__
- **2026-10-20** [`59a51259c5`](https://github.com/vllm-project/vllm/commit/59a51259c5) [#58984](https://github.com/vllm-project/vllm/pull/58984)
  [Perf][Spec Decode] Avoid target request padding in DP drafter (#58984)
  _Files: `vllm/v1/worker/gpu/dp_utils.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`, `vllm/v1/worker/gpu/spec_decode/target_dependent_ar/speculator.py`_
- **2026-10-19** [`3ff10ddeb0`](https://github.com/vllm-project/vllm/commit/3ff10ddeb0) [#62534](https://github.com/vllm-project/vllm/pull/62534)
  [Doc] Document DeepSeek-V4.1-Flash Dynamo sidecar serving / 记录 DeepSeek-V4.1-Flash Dynamo sidecar 部署 (#62534)
  _Files: `recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`_
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

## MoE / Expert Parallel  (45 commits)

- **2026-10-26** [`2f1cb151fd`](https://github.com/vllm-project/vllm/commit/2f1cb151fd) [#59931](https://github.com/vllm-project/vllm/pull/59931)
  [Bugfix] Preserve fp16 in legacy fused MoE LoRA (#59931)
  _Files: `tests/lora/test_fused_moe_lora_kernel.py`, `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`_
- **2026-10-26** [`fcb787055e`](https://github.com/vllm-project/vllm/commit/fcb787055e) [#61875](https://github.com/vllm-project/vllm/pull/61875)
  [Perf][DeepSeek V4] Declare MXFP8 MoE activations and run them as block FP8 on Hopper (#61875)
  _Files: `tests/quantization/test_fp8.py`, `tests/quantization/test_humming_mxfp4_block_fp8.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/models/deepseek_v4/quant_config.py` _+1 more__
- **2026-10-26** [`5a224c1ef3`](https://github.com/vllm-project/vllm/commit/5a224c1ef3) [#63506](https://github.com/vllm-project/vllm/pull/63506)
  [Fast Start] Key the weight cache on MoE and linear kernel backends (#63506)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py`, `vllm/model_executor/model_loader/weight_cache/protocol.py`_
- **2026-10-25** [`2c19f6793e`](https://github.com/vllm-project/vllm/commit/2c19f6793e) [#63372](https://github.com/vllm-project/vllm/pull/63372)
  [Bugfix][MRV2] Keep routed-expert rows of every DBO microbatch (#63372)
  _Files: `tests/v1/worker/test_gpu_ubatch_slicing.py`, `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`, `vllm/v1/worker/gpu/ubatch_utils.py`_
- **2026-10-25** [`8e11a8a49e`](https://github.com/vllm-project/vllm/commit/8e11a8a49e) [#63496](https://github.com/vllm-project/vllm/pull/63496)
  [LoRA] Reject incompatible MegaMoE backends during config validation (#63496)
  _Files: `vllm/config/lora.py`, `vllm/config/vllm.py`, `vllm/models/step5/nvidia/model.py`_
- **2026-10-24** [`7dc44a0016`](https://github.com/vllm-project/vllm/commit/7dc44a0016) [#63319](https://github.com/vllm-project/vllm/pull/63319)
  [Bugfix][LoRA][MoE] Process reloaded weights of LoRA-wrapped MoE layers (#63319)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`_
- **2026-10-23** [`e4db46c79b`](https://github.com/vllm-project/vllm/commit/e4db46c79b) [#59717](https://github.com/vllm-project/vllm/pull/59717)
  [Bugfix][MoE] Remap invalid topk_ids in moe_permute without expert_map (#59717)
  _Files: `csrc/moe/moe_permute_unpermute_op.cu`, `csrc/moe/permute_unpermute_kernels/moe_permute_unpermute_kernel.cu`, `tests/kernels/moe/test_cutlass_moe.py`, `tests/kernels/moe/test_moe_permute_unpermute.py` _+2 more__
- **2026-10-23** [`109669cfb3`](https://github.com/vllm-project/vllm/commit/109669cfb3) [#63118](https://github.com/vllm-project/vllm/pull/63118)
  [Bugfix][Kernel] Fix cooperative_topk illegal memory access on NaN scores (#63118)
  _Files: `csrc/persistent_topk.cuh`, `csrc/sampled_topk.cuh`, `csrc/topk_histogram_4096.cuh`, `tests/kernels/test_top_k_per_row.py`_
- **2026-10-23** [`404c2b510e`](https://github.com/vllm-project/vllm/commit/404c2b510e) [#62171](https://github.com/vllm-project/vllm/pull/62171)
  [Perf][Kernel] Size cooperative_topk's single pass by row length, not stride (#62171)
  _Files: `csrc/cooperative_topk.cuh`, `tests/kernels/test_top_k_per_row.py`_
- **2026-10-23** [`97b6a67d94`](https://github.com/vllm-project/vllm/commit/97b6a67d94) [#62751](https://github.com/vllm-project/vllm/pull/62751)
  [Quantization] Honor MoE activation override for Humming MXFP4 (#62751)
  _Files: `tests/evals/gpt_oss/configs/gpt-oss-20b-humming-mxfp4-mxfp8.yaml`, `tests/evals/gpt_oss/configs/models-b200.txt`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-10-23** [`f4edf9f0f0`](https://github.com/vllm-project/vllm/commit/f4edf9f0f0) [#62419](https://github.com/vllm-project/vllm/pull/62419)
  [XPU] Enable kernel/sampler unit tests on Intel XPU (#62419)
  _Files: `tests/kernels/attention/test_pack_unpack_triton.py`, `tests/kernels/core/test_fused_embed_norm.py`, `tests/kernels/core/test_fused_q_kv_rmsnorm.py`, `tests/kernels/core/test_minimax_reduce_rms.py` _+23 more__
- **2026-10-23** [`6d30b7abd7`](https://github.com/vllm-project/vllm/commit/6d30b7abd7) [#57092](https://github.com/vllm-project/vllm/pull/57092)
  [Bugfix] Make online FP8 MoE experts batch-invariant under VLLM_BATCH_INVARIANT (#57092)
  _Files: `tests/kernels/moe/test_batched_moe.py`, `tests/kernels/moe/test_modular_kernel_combinations.py`, `tests/v1/determinism/test_batch_invariance.py`, `vllm/model_executor/layers/fused_moe/experts/fused_batched_moe.py` _+3 more__
- **2026-10-23** [`284c0317c4`](https://github.com/vllm-project/vllm/commit/284c0317c4) [#62016](https://github.com/vllm-project/vllm/pull/62016)
  [CPU] Add GELU-tanh MoE, FP8 checkpoint support and Gemma-4 INT8 TP=4 padding (#62016)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `cmake/cpu_extension.cmake`, `csrc/cpu/fp8_quant.cpp`, `csrc/cpu/sgl-kernels/common.h` _+17 more__
- **2026-10-22** [`899a1689e2`](https://github.com/vllm-project/vllm/commit/899a1689e2) [#62938](https://github.com/vllm-project/vllm/pull/62938)
  [Model] Add Recursive Flint (#62938)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `docker/Dockerfile`, `docker/versions.json`, `docs/models/supported_models.md` _+27 more__
- **2026-10-22** [`b6031d71be`](https://github.com/vllm-project/vllm/commit/b6031d71be) [#63125](https://github.com/vllm-project/vllm/pull/63125)
  [Quantization][Quark] Support MXFP8 (W8A8) routed experts (#63125)
  _Files: `tests/quantization/test_quark.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py`_
- **2026-10-22** [`b689feb9f2`](https://github.com/vllm-project/vllm/commit/b689feb9f2) [#62526](https://github.com/vllm-project/vllm/pull/62526)
  [Benchmark] benchmark_moe: read Gemma 4's MoE shape from its text config (#62526)
  _Files: `benchmarks/kernels/benchmark_moe.py`_
- **2026-10-22** [`58c903ac94`](https://github.com/vllm-project/vllm/commit/58c903ac94) [#61655](https://github.com/vllm-project/vllm/pull/61655)
  [Refactor] Migrate FlashInfer NVLink one-sided to MoEEpCommunication (#61655)
  _Files: `tests/distributed/test_mnnvl_alltoall.py`, `tests/kernels/moe/test_moe_layer.py`, `tests/quantization/test_online.py`, `vllm/distributed/device_communicators/all2all.py` _+5 more__
- **2026-10-22** [`3b364baef5`](https://github.com/vllm-project/vllm/commit/3b364baef5) [#62054](https://github.com/vllm-project/vllm/pull/62054)
  [MoE] Use the sorted fused-MoE path for host-resident expert weights (#62054)
  _Files: `tests/kernels/moe/test_moe.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`_
- **2026-10-22** [`12c01a22eb`](https://github.com/vllm-project/vllm/commit/12c01a22eb) [#62624](https://github.com/vllm-project/vllm/pull/62624)
  [MoE] Revert platform hook for routed-expert capture rows (#62624) (#63013)
  _Files: `docs/design/plugin_system.md`, `tests/model_executor/test_routed_experts_capture.py`, `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`, `vllm/platforms/interface.py`_
- **2026-10-22** [`9c66703eef`](https://github.com/vllm-project/vllm/commit/9c66703eef) [#62980](https://github.com/vllm-project/vllm/pull/62980)
  [Bugfix] Support online quantization of Kimi K3 NVIDIA projections (#62980)
  _Files: `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-10-22** [`15a78aa88e`](https://github.com/vllm-project/vllm/commit/15a78aa88e) [#61749](https://github.com/vllm-project/vllm/pull/61749)
  [Bugfix][MoE] Require exact strides for moe_forward custom ops (#61749)
  _Files: `tests/quantization/test_trtllm_nvfp4_hidden_dim_padding.py`, `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`_
- **2026-10-22** [`6968d83131`](https://github.com/vllm-project/vllm/commit/6968d83131) [#62874](https://github.com/vllm-project/vllm/pull/62874)
  [Rust Frontend] Pass attributed deltas and the tokenizer to tool parsers (#62874)
  _Files: `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/default/unified.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs` _+43 more__
- **2026-10-22** [`7bac28707d`](https://github.com/vllm-project/vllm/commit/7bac28707d) [#61284](https://github.com/vllm-project/vllm/pull/61284)
  [Bugfix][LoRA] Disable shared-expert aux stream with fully-sharded LoRA (#61284)
  _Files: `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`_
- **2026-10-22** [`e4e6bcaae6`](https://github.com/vllm-project/vllm/commit/e4e6bcaae6) [#62366](https://github.com/vllm-project/vllm/pull/62366)
  [Model][Perf] Fuse Beam's TP all-reduce with its sandwich norms and MoE finalize (#62366)
  _Files: `CMakeLists.txt`, `csrc/beam/allreduce_norm.cu`, `csrc/mnnvl_lamport.cuh`, `csrc/ops.h` _+7 more__
- **2026-10-21** [`d0787e4839`](https://github.com/vllm-project/vllm/commit/d0787e4839) [#61868](https://github.com/vllm-project/vllm/pull/61868)
  [Perf][DSv4.1] DeepSeek-V4.1-Flash specialized decode on GB300 (#61868)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/deepseek_v41/__init__.py`, `tests/models/deepseek_v41/nvidia/__init__.py`, `tests/models/deepseek_v41/nvidia/specialized_decode/__init__.py` _+38 more__
- **2026-10-21** [`0d34366b14`](https://github.com/vllm-project/vllm/commit/0d34366b14) [#62101](https://github.com/vllm-project/vllm/pull/62101)
  [Perf][Model] Cohere2MoE: attention/MoE dual stream, single TP all-reduce per layer, fused add + RMSNorm (#62101)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_cohere2_moe_parallel_block.py`, `vllm/envs.py`, `vllm/model_executor/models/cohere2_moe.py`_
- **2026-10-21** [`b0e1f8052a`](https://github.com/vllm-project/vllm/commit/b0e1f8052a) [#52780](https://github.com/vllm-project/vllm/pull/52780)
  [Bugfix][MoE] Support simulated routing in monolithic MoE backends (#52780)
  _Files: `tests/kernels/moe/test_routed_experts_capture_monolithic.py`, `tests/kernels/moe/test_routing_simulator.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_mxint4_moe.py` _+6 more__
- **2026-10-21** [`dc61c6d027`](https://github.com/vllm-project/vllm/commit/dc61c6d027) [#62573](https://github.com/vllm-project/vllm/pull/62573)
  [EPD] Support metadata-only audio-in-video requests (#62573)
  _Files: `docs/features/disagg_encoder.md`, `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/models/multimodal/processing/test_audio_in_video.py`, `tests/models/multimodal/processing/test_qwen2_5_omni_embed.py` _+11 more__
- **2026-10-21** [`2a1a3c56c9`](https://github.com/vllm-project/vllm/commit/2a1a3c56c9) [#62624](https://github.com/vllm-project/vllm/pull/62624)
  [Feature][MoE] Add platform hook for routed-expert capture rows (#62624)
  _Files: `docs/design/plugin_system.md`, `tests/model_executor/test_routed_experts_capture.py`, `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`, `vllm/platforms/interface.py`_
- **2026-10-20** [`612e928016`](https://github.com/vllm-project/vllm/commit/612e928016) [#59645](https://github.com/vllm-project/vllm/pull/59645)
  [Bugfix] Make cooperative TopK exact on candidate overflow (#59645)
  _Files: `csrc/cooperative_topk.cu`, `csrc/cooperative_topk.cuh`, `csrc/cooperative_topk_overflow.cuh`, `csrc/topk_histogram_4096.cuh` _+2 more__
- **2026-10-20** [`c0fe6c4999`](https://github.com/vllm-project/vllm/commit/c0fe6c4999) [#62681](https://github.com/vllm-project/vllm/pull/62681)
  [Model] Support updated Ling FP8 quantization exclusions and MLA gates (#62681)
  _Files: `vllm/model_executor/models/bailing_moe_v3.py`_
- **2026-10-20** [`cc8a41f328`](https://github.com/vllm-project/vllm/commit/cc8a41f328) [#55485](https://github.com/vllm-project/vllm/pull/55485)
  [MyPy][4/N] Fix mypy errors in medium-hard tests/ dirs (#55485)
  _Files: `tests/entrypoints/pooling/scoring/test_io_processor_unit.py`, `tests/entrypoints/speech_to_text/correctness/test_transcription_api_correctness.py`, `tests/entrypoints/speech_to_text/realtime/test_realtime_validation.py`, `tests/entrypoints/speech_to_text/test_speech_to_text_cancellation.py` _+92 more__
- **2026-10-20** [`b9c8bd5140`](https://github.com/vllm-project/vllm/commit/b9c8bd5140) [#61999](https://github.com/vllm-project/vllm/pull/61999)
  [CI] Shard MTEB, DFlash Nightly, MoE Refactor DP and Entrypoints LLM automatically (#61999)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/models_language.yaml`, `.buildkite/test_areas/spec_decode.yaml`_
- **2026-10-20** [`b44446c180`](https://github.com/vllm-project/vllm/commit/b44446c180) [#62326](https://github.com/vllm-project/vllm/pull/62326)
  [Quantization] replace_parameter keeps the parameter object by default (#62326)
  _Files: `tests/model_executor/test_utils.py`, `tests/quantization/test_keep_param_objects.py`, `vllm/model_executor/kernels/linear/mixed_precision/MPLinearKernel.py`, `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py` _+13 more__
- **2026-10-19** [`b7701fc3e4`](https://github.com/vllm-project/vllm/commit/b7701fc3e4) [#57001](https://github.com/vllm-project/vllm/pull/57001)
  [Bugfix][Test] Synchronise ranks before the profiled call in profile_… (#57001)
  _Files: `tests/kernels/moe/modular_kernel_tools/profile_modular_kernel.py`_
- **2026-10-19** [`fdb953365c`](https://github.com/vllm-project/vllm/commit/fdb953365c) [#62090](https://github.com/vllm-project/vllm/pull/62090)
  [CI][Unit Test] Patch MoE layer unit tests for Blackwell and Rubin (#62090)
  _Files: `tests/kernels/moe/test_moe_layer.py`_
- **2026-10-19** [`3c9beb82d1`](https://github.com/vllm-project/vllm/commit/3c9beb82d1) [#59737](https://github.com/vllm-project/vllm/pull/59737)
  [Perf] Enable PDL for fused MoE top-k gating (#59737)
  _Files: `csrc/moe/topk_softmax_kernels.cu`_
- **2026-10-19** [`bde4d00113`](https://github.com/vllm-project/vllm/commit/bde4d00113) [#62467](https://github.com/vllm-project/vllm/pull/62467)
  [Bugfix][Kernel] persistent_topk: don't select float4 tail lanes past the row length (#62467)
  _Files: `csrc/persistent_topk.cuh`, `tests/kernels/test_top_k_per_row.py`_
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

## Multimodal  (42 commits)

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
- **2026-10-24** [`e9acf48614`](https://github.com/vllm-project/vllm/commit/e9acf48614) [#63017](https://github.com/vllm-project/vllm/pull/63017)
  [Platform] Use pluggable layer for ViT mrope preparation (#63017)
  _Files: `tests/plugins/vllm_add_dummy_platform/vllm_add_dummy_platform/dummy_custom_ops.py`, `tests/plugins_tests/test_platform_plugins.py`, `vllm/model_executor/layers/rotary_embedding/mrope_vit_setup.py`, `vllm/models/minimax_m3/common/vision_tower.py`_
- **2026-10-24** [`49d634bd6a`](https://github.com/vllm-project/vllm/commit/49d634bd6a) [#62850](https://github.com/vllm-project/vllm/pull/62850)
  [Perf][Multimodal] Make encoder cache free linear in items per request (#62850)
  _Files: `tests/v1/core/test_encoder_cache_manager.py`, `vllm/v1/core/encoder_cache_manager.py`_
- **2026-10-24** [`4920df120d`](https://github.com/vllm-project/vllm/commit/4920df120d) [#60687](https://github.com/vllm-project/vllm/pull/60687)
  [Bugfix][Model] Fix Gemma4 encoder CG with `max_soft_tokens` set (#60687)
  _Files: `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-10-23** [`6fd0e701fd`](https://github.com/vllm-project/vllm/commit/6fd0e701fd) [#63413](https://github.com/vllm-project/vllm/pull/63413)
  [CI] Remove redundant Ubuntu 24.04 release variant (#63413)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/publish-release-images.sh`, `docs/getting_started/installation/gpu.cuda.inc.md`_
- **2026-10-23** [`aaa67b754e`](https://github.com/vllm-project/vllm/commit/aaa67b754e) [#59854](https://github.com/vllm-project/vllm/pull/59854)
  [Rust Frontend] Refactor rust frontend for latest `llm-multimodal` v1.14 crate (#59854)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/multimodal/audio.rs` _+11 more__
- **2026-10-23** [`8fae0ff58b`](https://github.com/vllm-project/vllm/commit/8fae0ff58b) [#62181](https://github.com/vllm-project/vllm/pull/62181)
  [Frontend] Accept images on /v1/systemone for multimodal next-token models (#62181)
  _Files: `docs/models/structured_decisions_models.md`, `tests/entrypoints/generate/structured_decisions/test_strategies.py`, `vllm/entrypoints/openai/decisions/strategies.py`_
- **2026-10-23** [`23f546eee0`](https://github.com/vllm-project/vllm/commit/23f546eee0) [#63120](https://github.com/vllm-project/vllm/pull/63120)
  [Bugfix] Fix DeepSeek-VL2 cache identity across cropping modes (#63120)
  _Files: `tests/models/multimodal/generation/test_deepseek_vl2.py`, `tests/models/multimodal/processing/test_deepseek_vl2.py`, `tests/models/multimodal/processing/test_h2ovl.py`, `tests/models/multimodal/processing/test_unlimited_ocr.py` _+3 more__
- **2026-10-23** [`32551991b9`](https://github.com/vllm-project/vllm/commit/32551991b9) [#63145](https://github.com/vllm-project/vllm/pull/63145)
  [MM][Mistral] Use real-valued RoPE in the compiled Pixtral ViT (#63145)
  _Files: `tests/models/multimodal/generation/test_pixtral.py`, `vllm/model_executor/models/pixtral.py`_
- **2026-10-23** [`9c8ad93f68`](https://github.com/vllm-project/vllm/commit/9c8ad93f68) [#62880](https://github.com/vllm-project/vllm/pull/62880)
  [Bugfix] Don't enable MM embedding inputs on KV consumers in language-model-only mode (#62880)
  _Files: `tests/config/test_multimodal_config.py`, `vllm/config/multimodal.py`, `vllm/config/vllm.py`_
- **2026-10-23** [`18343393b4`](https://github.com/vllm-project/vllm/commit/18343393b4) [#63095](https://github.com/vllm-project/vllm/pull/63095)
  [model] Support MiniCPM-OCR 1.0 (#63095)
  _Files: `tests/models/multimodal/processing/test_minicpm_ocr.py`, `tests/models/registry.py`, `vllm/model_executor/models/minicpm_ocr.py`, `vllm/model_executor/models/registry.py` _+1 more__
- **2026-10-22** [`c0c02786a3`](https://github.com/vllm-project/vllm/commit/c0c02786a3) [#63192](https://github.com/vllm-project/vllm/pull/63192)
  [Bugfix][Model] Build the skipped DeepSeek-VL2 vision tower without meta .item() (#63192)
  _Files: `vllm/model_executor/models/deepseek_vl2.py`_
- **2026-10-22** [`fdc5fde9d7`](https://github.com/vllm-project/vllm/commit/fdc5fde9d7) [#60643](https://github.com/vllm-project/vllm/pull/60643)
  [Perf][Gemma4][Multimodal] Fuse Gemma4Unified 2D posemb and batch image/video embedder (#60643)
  _Files: `tests/models/multimodal/processing/test_gemma4_unified.py`, `vllm/model_executor/models/gemma4_unified.py`_
- **2026-10-22** [`f42421354d`](https://github.com/vllm-project/vllm/commit/f42421354d) [#62957](https://github.com/vllm-project/vllm/pull/62957)
  [Model] Add Alpamayo 2 Super (reasoning model) (#62957)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_alpamayo2_super.py`, `tests/models/registry.py`, `vllm/config/model.py` _+8 more__
- **2026-10-22** [`ded32c3ba7`](https://github.com/vllm-project/vllm/commit/ded32c3ba7) [#61946](https://github.com/vllm-project/vllm/pull/61946)
  [Bugfix][Model] Fix maximum image token profiling for Unlimited-OCR (#61946)
  _Files: `tests/models/multimodal/processing/test_unlimited_ocr.py`, `vllm/model_executor/models/unlimited_ocr.py`_
- **2026-10-22** [`8121025f71`](https://github.com/vllm-project/vllm/commit/8121025f71) [#54642](https://github.com/vllm-project/vllm/pull/54642)
  [Bugfix] Include multimodal limits in the model compile-cache hash (#54642)
  _Files: `vllm/config/model.py`_
- **2026-10-22** [`0f09c4b7ca`](https://github.com/vllm-project/vllm/commit/0f09c4b7ca) [#62906](https://github.com/vllm-project/vllm/pull/62906)
  [Bugfix] Apply default multimodal LoRA per batch conversation (#62906)
  _Files: `tests/entrypoints/multimodal/openai/chat_completion/test_default_mm_loras.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py`_
- **2026-10-22** [`49dbf7c44f`](https://github.com/vllm-project/vllm/commit/49dbf7c44f) [#62704](https://github.com/vllm-project/vllm/pull/62704)
  [Bugfix][Multimodal] Return 400 for structurally-corrupted PNG images (#62704)
  _Files: `tests/multimodal/media/test_image.py`, `vllm/multimodal/media/image.py`_
- **2026-10-22** [`268e54951c`](https://github.com/vllm-project/vllm/commit/268e54951c) [#61196](https://github.com/vllm-project/vllm/pull/61196)
  [Bugfix][Model] Fix Gemma 4 image/audio placeholder strings (#61196)
  _Files: `tests/models/multimodal/processing/test_gemma4.py`, `vllm/model_executor/models/diffusion_gemma.py`, `vllm/model_executor/models/gemma4_mm.py`_
- **2026-10-22** [`0dd9da117d`](https://github.com/vllm-project/vllm/commit/0dd9da117d) [#61090](https://github.com/vllm-project/vllm/pull/61090)
  Fix torchcodec lazy-import startup crash when native lib raises OSError (#61090)
  _Files: `vllm/multimodal/media/audio.py`_
- **2026-10-21** [`90c4a1a73e`](https://github.com/vllm-project/vllm/commit/90c4a1a73e) [#62767](https://github.com/vllm-project/vllm/pull/62767)
  [Bugfix] Preserve image normalization constants during dummy loading (#62767)
  _Files: `tests/model_executor/layers/test_mm_input_norm.py`, `vllm/model_executor/layers/fusion/mm_input_norm.py`_
- **2026-10-21** [`4a3ee9a0f6`](https://github.com/vllm-project/vllm/commit/4a3ee9a0f6) [#57393](https://github.com/vllm-project/vllm/pull/57393)
  [Bugfix][Model] Enable ModelOpt support for Cosmos3-Edge (#57393)
  _Files: `tests/models/multimodal/test_mapping.py`, `vllm/model_executor/models/cosmos3_edge.py`_
- **2026-10-21** [`65a886c69f`](https://github.com/vllm-project/vllm/commit/65a886c69f) [#62859](https://github.com/vllm-project/vllm/pull/62859)
  [Bugfix][Pooling] Reject multimodal inputs in chunked embeddings (#62859)
  _Files: `tests/entrypoints/pooling/embed/test_io_processor.py`, `vllm/config/pooler.py`, `vllm/entrypoints/pooling/embed/io_processor.py`_
- **2026-10-21** [`8a21d0a328`](https://github.com/vllm-project/vllm/commit/8a21d0a328) [#62416](https://github.com/vllm-project/vllm/pull/62416)
  [Rust Frontend] Support `--tokenizer`, `--tokenizer-revision`, and `--hf-config-path` (#62416)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/model.rs` _+9 more__
- **2026-10-21** [`70806b6318`](https://github.com/vllm-project/vllm/commit/70806b6318) [#62164](https://github.com/vllm-project/vllm/pull/62164)
  [Bugfix] Fix multimodal sender-cache invalidation race with queued renders (#62164)
  _Files: `tests/multimodal/test_cache.py`, `vllm/renderers/base.py`, `vllm/v1/engine/async_llm.py`_
- **2026-10-21** [`81c2bd702e`](https://github.com/vllm-project/vllm/commit/81c2bd702e) [#57101](https://github.com/vllm-project/vllm/pull/57101)
  [Perf] Optimize Molmo2 pooling preparation (#57101)
  _Files: `tests/models/multimodal/processing/test_molmo2.py`, `vllm/model_executor/models/molmo2.py`_
- **2026-10-20** [`7e3d559565`](https://github.com/vllm-project/vllm/commit/7e3d559565) [#62437](https://github.com/vllm-project/vllm/pull/62437)
  [Frontend] DiffusionGemma joint reads on /v1/systemone and /v1/decisions, images on /v1/systemone (#62437)
  _Files: `docs/models/structured_decisions_models.md`, `examples/features/structured_diffusion/README.md`, `examples/features/structured_diffusion/structured_server.py`, `tests/entrypoints/generate/structured_decisions/test_joint_e2e.py` _+9 more__
- **2026-10-20** [`0ca531ba64`](https://github.com/vllm-project/vllm/commit/0ca531ba64) [#61838](https://github.com/vllm-project/vllm/pull/61838)
  [Perf][Model] Support torch.compile for the PaddleOCR-VL vision encoder (#61838)
  _Files: `tests/compile/fullgraph/test_multimodal_compile.py`, `vllm/model_executor/models/paddleocr_vl.py`_
- **2026-10-20** [`b272cff368`](https://github.com/vllm-project/vllm/commit/b272cff368) [#62714](https://github.com/vllm-project/vllm/pull/62714)
  [Bugfix] Read ColPali hidden size from vlm_config (#62714)
  _Files: `vllm/model_executor/models/colpali.py`_
- **2026-10-20** [`5285b9b864`](https://github.com/vllm-project/vllm/commit/5285b9b864) [#62648](https://github.com/vllm-project/vllm/pull/62648)
  [Bugfix][Model] Build Pixtral vision position ids on device (#62648)
  _Files: `vllm/model_executor/models/pixtral.py`_
- **2026-10-20** [`e7e8deb86c`](https://github.com/vllm-project/vllm/commit/e7e8deb86c) [#62469](https://github.com/vllm-project/vllm/pull/62469)
  [Perf][Multimodal] Keep audio encoder padding masks broadcastable (#62469)
  _Files: `vllm/model_executor/models/audioflamingo3.py`, `vllm/model_executor/models/qwen2_audio.py`_
- **2026-10-20** [`f8e1e87129`](https://github.com/vllm-project/vllm/commit/f8e1e87129) [#62620](https://github.com/vllm-project/vllm/pull/62620)
  [CI][Bugfix] Skip the SmolVLM HF comparison on Transformers 5.20 (#62620)
  _Files: `tests/models/registry.py`_
- **2026-10-20** [`083d61622b`](https://github.com/vllm-project/vllm/commit/083d61622b) [#62575](https://github.com/vllm-project/vllm/pull/62575)
  [CI/Build] Drop CUDA 12.9 from the release pipeline (#62575)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/docker-build-metadata-args.sh`, `.buildkite/scripts/publish-release-images.sh`_
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

## Other  (41 commits)

- **2026-10-26** [`51d43b3683`](https://github.com/vllm-project/vllm/commit/51d43b3683) [#61792](https://github.com/vllm-project/vllm/pull/61792)
  [Test][UMBP][4/10] Cover async lookup, hybrid cache, events, and metrics (#61792)
  _Files: `tests/v1/kv_connector/unit/test_umbp_async_lookup.py`, `tests/v1/kv_connector/unit/test_umbp_core.py`, `tests/v1/kv_connector/unit/test_umbp_events.py`, `tests/v1/kv_connector/unit/test_umbp_hybrid.py`_
- **2026-10-26** [`2a2717d9b8`](https://github.com/vllm-project/vllm/commit/2a2717d9b8) [#63531](https://github.com/vllm-project/vllm/pull/63531)
  [XPU] Fix Kimi-Linear model dispatch (#63531)
  _Files: `tests/models/test_registry.py`, `vllm/models/kimi_k3/__init__.py`_
- **2026-10-26** [`7128f568ac`](https://github.com/vllm-project/vllm/commit/7128f568ac) [#58243](https://github.com/vllm-project/vllm/pull/58243)
  [Bugfix][MRV2] Reserve encoder graph memory without decoder graphs (#58243)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2_cudagraph_profiling.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-10-25** [`636da2476d`](https://github.com/vllm-project/vllm/commit/636da2476d) [#60513](https://github.com/vllm-project/vllm/pull/60513)
  [Bugfix][Spec Decode] Keep speculator limits in sync after auto-fit (#60513)
  _Files: `tests/v1/worker/test_gpu_target_dependent_ar_speculator.py`, `vllm/v1/worker/gpu/spec_decode/speculator.py`_
- **2026-10-25** [`66bf931544`](https://github.com/vllm-project/vllm/commit/66bf931544) [#63476](https://github.com/vllm-project/vllm/pull/63476)
  [Bugfix][MRV2] Report the first failed DBO microbatch (#63476)
  _Files: `tests/v1/worker/test_gpu_ubatch_slicing.py`, `vllm/v1/worker/gpu/ubatch_utils.py`_
- **2026-10-24** [`7050ef881f`](https://github.com/vllm-project/vllm/commit/7050ef881f) [#58466](https://github.com/vllm-project/vllm/pull/58466)
  [Sampling] Add adaptive verification support to batch-sharded sampling (#58466)
  _Files: `tests/v1/sample/test_dry.py`, `tests/v1/worker/test_gpu_batch_shard.py`, `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/config/vllm.py` _+4 more__
- **2026-10-23** [`d561af5dfc`](https://github.com/vllm-project/vllm/commit/d561af5dfc) [#62841](https://github.com/vllm-project/vllm/pull/62841)
  [Bugfix][Mamba] Avoid re-marking committed prompt-tail boundaries as cached this step (#62841)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-10-23** [`44302539f8`](https://github.com/vllm-project/vllm/commit/44302539f8) [#55743](https://github.com/vllm-project/vllm/pull/55743)
  [Bugfix][Tool Parser] Preserve large integer tool arguments (#55743)
  _Files: `tests/tool_parsers/test_k2_horizon_tool_parser.py`, `tests/tool_parsers/test_utils.py`, `vllm/tool_parsers/utils.py`_
- **2026-10-23** [`34b2954482`](https://github.com/vllm-project/vllm/commit/34b2954482) [#63315](https://github.com/vllm-project/vllm/pull/63315)
  [Rust Frontend] Validate, deduplicate and cap bad words like Python (#63315)
  _Files: `rust/src/text/src/lower.rs`, `rust/src/text/src/lower/token_ids.rs`_
- **2026-10-23** [`faccd2f9dd`](https://github.com/vllm-project/vllm/commit/faccd2f9dd) [#63062](https://github.com/vllm-project/vllm/pull/63062)
  [Rust Frontend] End prefilled Kimi K3 reasoning at the response opener like Python (#63062)
  _Files: `rust/src/chat/tests/grammar_replay/Kimi-K3.json`, `rust/src/chat/tests/grammar_replay/Kimi-K3.txt`, `rust/src/parser/src/unified/kimi_k3.rs`, `rust/src/parser/src/unified/kimi_k3/grammar.rs`_
- **2026-10-23** [`58cf73223e`](https://github.com/vllm-project/vllm/commit/58cf73223e) [#63112](https://github.com/vllm-project/vllm/pull/63112)
  [Bugfix][Pooling] Validate late-interaction mode and use count in the Python API (#63112)
  _Files: `tests/test_pooling_params.py`, `vllm/pooling_params.py`_
- **2026-10-23** [`0510bd6679`](https://github.com/vllm-project/vllm/commit/0510bd6679) [#62867](https://github.com/vllm-project/vllm/pull/62867)
  [Bugfix][CPU] Fix DP NUMA affinity regression (#62867)
  _Files: `tests/utils_/test_cpu_resource_utils.py`, `vllm/platforms/cpu.py`, `vllm/utils/cpu_resource_utils.py`, `vllm/utils/ompmultiprocessing.py` _+1 more__
- **2026-10-23** [`19c0e170d2`](https://github.com/vllm-project/vllm/commit/19c0e170d2) [#63146](https://github.com/vllm-project/vllm/pull/63146)
  [Test][Pooling] Cover explicit right truncation for the JinaVL score token (#63146)
  _Files: `tests/entrypoints/pooling/scoring/test_io_processor_unit.py`_
- **2026-10-23** [`5db4dfa2d9`](https://github.com/vllm-project/vllm/commit/5db4dfa2d9) [#63228](https://github.com/vllm-project/vllm/pull/63228)
  [Docs] Fix griffe missing-type warnings in XPress kernels (#63228)
  _Files: `vllm/v1/worker/gpu/spec_decode/xpress/kernels.py`_
- **2026-10-22** [`52f44839f2`](https://github.com/vllm-project/vllm/commit/52f44839f2) [#60028](https://github.com/vllm-project/vllm/pull/60028)
  [Startup][UX] Start multiproc workers concurrently when using spawn (#60028)
  _Files: `tests/v1/executor/test_multiproc_executor.py`, `vllm/v1/executor/multiproc_executor.py`_
- **2026-10-22** [`1cc332ee80`](https://github.com/vllm-project/vllm/commit/1cc332ee80) [#62738](https://github.com/vllm-project/vllm/pull/62738)
  [Frontend] Use VLLMValidationError for client input errors in renderers base (#62738)
  _Files: `tests/renderers/test_completions.py`, `tests/renderers/test_process_multi_modal_uuids.py`, `vllm/renderers/base.py`_
- **2026-10-22** [`e6e4163424`](https://github.com/vllm-project/vllm/commit/e6e4163424) [#62888](https://github.com/vllm-project/vllm/pull/62888)
  [CPU] Warm up MRV2 Triton kernels at startup (#62888)
  _Files: `vllm/v1/worker/cpu/shm.py`, `vllm/v1/worker/cpu_worker.py`, `vllm/v1/worker/gpu/sample/penalties.py`, `vllm/v1/worker/gpu/structured_outputs.py`_
- **2026-10-22** [`87b804f09d`](https://github.com/vllm-project/vllm/commit/87b804f09d) [#62892](https://github.com/vllm-project/vllm/pull/62892)
  [Rust Frontend] Match reasoning delimiters by token identity (#62892)
  _Files: `rust/src/chat/src/parser/reasoning/tests.rs`, `rust/src/chat/tests/chat.rs`, `rust/src/parser/src/reasoning/delimited.rs`, `rust/src/parser/src/reasoning/minimax_m3.rs` _+7 more__
- **2026-10-22** [`47e2b610be`](https://github.com/vllm-project/vllm/commit/47e2b610be) [#62911](https://github.com/vllm-project/vllm/pull/62911)
  [Bugfix][Core] Validate prompt token ids when skip_tokenizer_init is set (#62911)
  _Files: `tests/entrypoints/llm/test_prompt_validation.py`, `vllm/renderers/base.py`_
- **2026-10-22** [`5957bbf125`](https://github.com/vllm-project/vllm/commit/5957bbf125) [#63051](https://github.com/vllm-project/vllm/pull/63051)
  [Bugfix][Pooling] Bound late chunk sizes in the Python API (#63051)
  _Files: `tests/entrypoints/pooling/token_embed/test_offline.py`, `tests/test_pooling_params.py`, `vllm/pooling_params.py`_
- **2026-10-22** [`cd914c98e4`](https://github.com/vllm-project/vllm/commit/cd914c98e4) [#62701](https://github.com/vllm-project/vllm/pull/62701)
  [Core][Sleep Mode] Use torch.accelerator in CuMemAllocator free/sleep (#62701)
  _Files: `tests/basic_correctness/memory/cumem/test_cumem.py`, `vllm/device_allocator/cumem.py`_
- **2026-10-21** [`2916b4b4a6`](https://github.com/vllm-project/vllm/commit/2916b4b4a6) [#62822](https://github.com/vllm-project/vllm/pull/62822)
  [Rust Frontend] Carry return_token_ids through render like Python (#62822)
  _Files: `rust/src/server/src/routes/render.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-10-21** [`e0ca7d9cc1`](https://github.com/vllm-project/vllm/commit/e0ca7d9cc1) [#62824](https://github.com/vllm-project/vllm/pull/62824)
  [Rust Frontend] Report prompts over max_model_len like Python (#62824)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/server/src/error.rs`, `rust/src/text/src/error.rs`, `rust/src/text/src/lower.rs`_
- **2026-10-21** [`4f6a4e2b9d`](https://github.com/vllm-project/vllm/commit/4f6a4e2b9d) [#57862](https://github.com/vllm-project/vllm/pull/57862)
  [XPU][UT] Deflake GPT2 score tests with reruns (#57862)
  _Files: `tests/models/language/generation/test_common.py`_
- **2026-10-21** [`1f5514ec46`](https://github.com/vllm-project/vllm/commit/1f5514ec46) [#62374](https://github.com/vllm-project/vllm/pull/62374)
  [Bugfix][Rust Frontend] Fix HTTP 500 on long conversations: fuel-limit only request templates (#62374)
  _Files: `rust/src/chat/src/renderer/hf/error.rs`, `rust/src/chat/src/renderer/hf/mod.rs`, `rust/src/chat/src/renderer/hf/template.rs`, `tests/test_envs.py` _+1 more__
- **2026-10-21** [`b3047819e0`](https://github.com/vllm-project/vllm/commit/b3047819e0) [#62742](https://github.com/vllm-project/vllm/pull/62742)
  [Docs] Add @TheEpicDolphin as codeowner for spec decode (#62742)
  _Files: `.github/CODEOWNERS`_
- **2026-10-20** [`1e330b1019`](https://github.com/vllm-project/vllm/commit/1e330b1019) [#62142](https://github.com/vllm-project/vllm/pull/62142)
  [MyPy][5/N] Fix mypy errors in hard tests/ dirs and enforce follow-imports=silent (#62142)
- **2026-10-20** [`f1dbfef799`](https://github.com/vllm-project/vllm/commit/f1dbfef799) [#62521](https://github.com/vllm-project/vllm/pull/62521)
  [Core] Don't apply spec decode async scheduling fallbacks with MRV2 (#62521)
  _Files: `vllm/config/vllm.py`_
- **2026-10-20** [`92e379001c`](https://github.com/vllm-project/vllm/commit/92e379001c) [#62644](https://github.com/vllm-project/vllm/pull/62644)
  [Rust Frontend] Cap request token histogram buckets at max_model_len (#62644)
  _Files: `rust/src/llm/src/lib.rs`, `rust/src/llm/src/request_metrics.rs`, `rust/src/metrics/src/request.rs`_
- **2026-10-20** [`fbc3555287`](https://github.com/vllm-project/vllm/commit/fbc3555287) [#62432](https://github.com/vllm-project/vllm/pull/62432)
  [Rust Frontend] Return 501 instead of 404 for Python-only routes (#62432)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/server/src/config.rs` _+2 more__
- **2026-10-20** [`3593d8e5ba`](https://github.com/vllm-project/vllm/commit/3593d8e5ba) [#62429](https://github.com/vllm-project/vllm/pull/62429)
  [Rust Frontend] Emit transfer params at the top level of render output (#62429)
  _Files: `rust/src/server/src/routes/render.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-10-20** [`97a82d3c92`](https://github.com/vllm-project/vllm/commit/97a82d3c92) [#62642](https://github.com/vllm-project/vllm/pull/62642)
  [Rust Frontend] Truncate prompts against max_model_len like Python (#62642)
  _Files: `rust/src/server/src/error.rs`, `rust/src/text/src/error.rs`, `rust/src/text/src/lib.rs`, `rust/src/text/src/truncation.rs`_
- **2026-10-20** [`52712d4259`](https://github.com/vllm-project/vllm/commit/52712d4259) [#62427](https://github.com/vllm-project/vllm/pull/62427)
  [Rust Frontend] Validate cache_salt like Python (#62427)
  _Files: `rust/src/text/src/error.rs`, `rust/src/text/src/request.rs`_
- **2026-10-20** [`1466f372a3`](https://github.com/vllm-project/vllm/commit/1466f372a3) [#62426](https://github.com/vllm-project/vllm/pull/62426)
  [Rust Frontend] Inherit presence and frequency penalties from generation_config (#62426)
  _Files: `rust/src/text/src/backend/hf/config.rs`, `rust/src/text/src/backend/hf/mod.rs`, `rust/src/text/src/backend/mod.rs`, `rust/src/text/src/lower.rs`_
- **2026-10-20** [`50e2296c23`](https://github.com/vllm-project/vllm/commit/50e2296c23) [#62425](https://github.com/vllm-project/vllm/pull/62425)
  [Rust Frontend] Clamp logit_bias to [-100, 100] (#62425)
  _Files: `rust/src/text/src/lower.rs`_
- **2026-10-20** [`3897f95cf1`](https://github.com/vllm-project/vllm/commit/3897f95cf1) [#62610](https://github.com/vllm-project/vllm/pull/62610)
  [Docs] Use probabilistic DSpark sampling in Kimi-K3 GB300 recipes / [Docs] Kimi-K3 GB300 配方使用概率式 DSpark 采样 (#62610)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-20** [`df3bd094ae`](https://github.com/vllm-project/vllm/commit/df3bd094ae) [#62578](https://github.com/vllm-project/vllm/pull/62578)
  [Bugfix][NIXL] Use XPU-compatible block size in sleep test (#62578)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`_
- **2026-10-19** [`e1f3141647`](https://github.com/vllm-project/vllm/commit/e1f3141647) [#60767](https://github.com/vllm-project/vllm/pull/60767)
  [Bugfix][V1] Null sliding-window block-table entries below the window (#60767)
  _Files: `tests/v1/worker/test_gpu_block_table.py`, `vllm/v1/kv_cache_interface.py`, `vllm/v1/worker/gpu/block_table.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-10-19** [`3b05805d47`](https://github.com/vllm-project/vllm/commit/3b05805d47) [#62508](https://github.com/vllm-project/vllm/pull/62508)
  [Misc] Fix failing weight cache RoPE test on main (#62508)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`_
- **2026-10-19** [`aa3564ceef`](https://github.com/vllm-project/vllm/commit/aa3564ceef) [#62461](https://github.com/vllm-project/vllm/pull/62461)
  [Bugfix][Test] Stop requesting capfd in the subprocess weight cache test (#62461)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`_
- **2026-10-19** [`52e88e25ec`](https://github.com/vllm-project/vllm/commit/52e88e25ec) [#62228](https://github.com/vllm-project/vllm/pull/62228)
  [Core] Remove the obsolete VLLM_USE_RAY_V2_EXECUTOR_BACKEND env var (#62228)
  _Files: `vllm/envs.py`_

## Serving / API  (39 commits)

- **2026-10-26** [`059e2de6d8`](https://github.com/vllm-project/vllm/commit/059e2de6d8) [#62450](https://github.com/vllm-project/vllm/pull/62450)
  [Bugfix][Frontend] Preserve DP rank in Responses requests (#62450)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/serving.py`_
- **2026-10-24** [`f959137753`](https://github.com/vllm-project/vllm/commit/f959137753) [#63345](https://github.com/vllm-project/vllm/pull/63345)
  [Bugfix][Frontend] Apply batch tool_choice rules to streamed tool calls (#63345)
  _Files: `tests/entrypoints/openai/chat_completion/test_stream_processor.py`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/entrypoints/openai/chat_completion/message_assembly.py` _+3 more__
- **2026-10-23** [`e2b6723123`](https://github.com/vllm-project/vllm/commit/e2b6723123) [#40186](https://github.com/vllm-project/vllm/pull/40186)
  [entrypoints/openai] add kv params to streaming api response (#40186)
  _Files: `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/completion/protocol.py`, `vllm/entrypoints/openai/completion/serving.py`_
- **2026-10-23** [`ccd4e4030f`](https://github.com/vllm-project/vllm/commit/ccd4e4030f) [#63318](https://github.com/vllm-project/vllm/pull/63318)
  [Rust Frontend] Support --return-tokens-as-token-ids (#63318)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/server/src/config.rs` _+5 more__
- **2026-10-23** [`1b99dc5e8f`](https://github.com/vllm-project/vllm/commit/1b99dc5e8f) [#63314](https://github.com/vllm-project/vllm/pull/63314)
  [Rust Frontend] Render empty tool call arguments as an empty object like Python (#63314)
  _Files: `rust/src/server/src/routes/openai/chat_completions/convert.rs`_
- **2026-10-23** [`574084bfe0`](https://github.com/vllm-project/vllm/commit/574084bfe0) [#63061](https://github.com/vllm-project/vllm/pull/63061)
  [Rust Frontend] Serialize unset chat response fields as null like Python (#63061)
  _Files: `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/openai/chat_completions/types.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-10-23** [`654bd123b3`](https://github.com/vllm-project/vllm/commit/654bd123b3) [#63060](https://github.com/vllm-project/vllm/pull/63060)
  [Rust Frontend] Reject an empty chat tools array like Python (#63060)
  _Files: `rust/src/server/src/routes/openai/chat_completions/validate.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-10-23** [`e879223b5d`](https://github.com/vllm-project/vllm/commit/e879223b5d) [#63148](https://github.com/vllm-project/vllm/pull/63148)
  [Frontend] Share non-streaming chat message assembly with batch derender (#63148)
  _Files: `tests/entrypoints/openai/chat_completion/test_message_assembly.py`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/entrypoints/openai/chat_completion/message_assembly.py` _+3 more__
- **2026-10-23** [`258f42076d`](https://github.com/vllm-project/vllm/commit/258f42076d) [#62583](https://github.com/vllm-project/vllm/pull/62583)
  [Fast Start] Fix weight cache daemon GPU memory and warm-cache warmup hang (#62583)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/entrypoints/cli/preload.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`_
- **2026-10-23** [`751ac8d643`](https://github.com/vllm-project/vllm/commit/751ac8d643) [#47112](https://github.com/vllm-project/vllm/pull/47112)
  [Frontend] Enforce max_tool_calls for Responses built-in tools (#47112)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/serving.py`_
- **2026-10-22** [`f0abb2f828`](https://github.com/vllm-project/vllm/commit/f0abb2f828) [#62294](https://github.com/vllm-project/vllm/pull/62294)
  [Bugfix][Anthropic] Map vLLM error types to Anthropic error.type vocabulary (#62294)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/anthropic/test_error_type_mapping.py`, `vllm/entrypoints/anthropic/api_router.py`, `vllm/entrypoints/anthropic/protocol.py` _+1 more__
- **2026-10-22** [`47c091b100`](https://github.com/vllm-project/vllm/commit/47c091b100) [#62856](https://github.com/vllm-project/vllm/pull/62856)
  [Bugfix][Frontend] Accept and echo prompt-cache and safety_identifier fields in the Responses API (#62856)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/protocol.py`_
- **2026-10-22** [`2de0531d81`](https://github.com/vllm-project/vllm/commit/2de0531d81) [#62507](https://github.com/vllm-project/vllm/pull/62507)
  [Bugfix][Frontend][Kimi K3] Fix Kimi K3 XTML marker leakage in responses API (#62507)
  _Files: `tests/entrypoints/openai/responses/test_sampling_params.py`, `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `tests/tool_use/test_kimi_k3_tool_parser.py`, `vllm/entrypoints/openai/responses/protocol.py`_
- **2026-10-22** [`60a7d568f4`](https://github.com/vllm-project/vllm/commit/60a7d568f4) [#62765](https://github.com/vllm-project/vllm/pull/62765)
  [Feature] [Frontend] [Reasoning] Support Prompt Embeds inputs for reasoning traces (#62765)
  _Files: `docs/features/prompt_embeds.md`, `tests/entrypoints/openai/chat_completion/test_chat_completion_with_prompt_embeds.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/renderers/chat_utils/test_prompt_embeds.py` _+5 more__
- **2026-10-22** [`26cc019013`](https://github.com/vllm-project/vllm/commit/26cc019013) [#62163](https://github.com/vllm-project/vllm/pull/62163)
  [Bugfix][Frontend] Keep completion derender stream logprob offsets aligned with tokens (#62163)
  _Files: `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`, `vllm/renderers/online_derenderer.py`_
- **2026-10-22** [`7d5335936c`](https://github.com/vllm-project/vllm/commit/7d5335936c) [#62928](https://github.com/vllm-project/vllm/pull/62928)
  [Bugfix][Frontend] Normalize beam search scores by generated length (#62928)
  _Files: `tests/samplers/test_beam_search_online.py`, `vllm/entrypoints/generate/beam_search/offline.py`, `vllm/entrypoints/generate/beam_search/online.py`, `vllm/entrypoints/generate/beam_search/utils.py` _+1 more__
- **2026-10-22** [`5fa7b7b01b`](https://github.com/vllm-project/vllm/commit/5fa7b7b01b) [#62783](https://github.com/vllm-project/vllm/pull/62783)
  [Bugfix][Pooling] Keep the JinaVL score token when truncating score prompts (#62783)
  _Files: `tests/entrypoints/pooling/scoring/test_io_processor_unit.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`, `vllm/entrypoints/pooling/utils.py`_
- **2026-10-22** [`8420dd20fb`](https://github.com/vllm-project/vllm/commit/8420dd20fb) [#62719](https://github.com/vllm-project/vllm/pull/62719)
  [Bugfix][Frontend] Cut stop strings and stop tokens on derender (#62719)
  _Files: `docs/serving/online_serving/derenderer.md`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/derender/test_derender_parity.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py` _+2 more__
- **2026-10-22** [`df6603f058`](https://github.com/vllm-project/vllm/commit/df6603f058) [#62786](https://github.com/vllm-project/vllm/pull/62786)
  [Bugfix][Frontend] Render GPT-OSS chats with Harmony in /tokenize (#62786)
  _Files: `tests/entrypoints/scale_out/render/test_render.py`, `vllm/entrypoints/serve/tokenize/protocol.py`, `vllm/entrypoints/serve/tokenize/serving.py`_
- **2026-10-22** [`79d5c93796`](https://github.com/vllm-project/vllm/commit/79d5c93796) [#61772](https://github.com/vllm-project/vllm/pull/61772)
  [Feature][Pooling] Serve late chunking through /v1/embeddings (#61772)
  _Files: `docs/models/pooling_models/README.md`, `docs/models/pooling_models/token_embed.md`, `examples/pooling/token_embed/late_chunking_offline.py`, `examples/pooling/token_embed/late_chunking_retrieval_online.py` _+16 more__
- **2026-10-22** [`d9fcde70ff`](https://github.com/vllm-project/vllm/commit/d9fcde70ff) [#61984](https://github.com/vllm-project/vllm/pull/61984)
  [Bugfix] Resolve disabled thinking effort in Anthropic render (#61984)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/scale_out/render/test_render.py`, `vllm/entrypoints/anthropic/serving.py`, `vllm/entrypoints/common/cli_args.py` _+3 more__
- **2026-10-22** [`ae43d045c4`](https://github.com/vllm-project/vllm/commit/ae43d045c4) [#55809](https://github.com/vllm-project/vllm/pull/55809)
  [Bench] Save server queue time and TTFT in detailed results (#55809)
  _Files: `docs/benchmarking/cli.md`, `rust/src/bench/src/backends/mod.rs`, `rust/src/bench/src/backends/openai_chat.rs`, `rust/src/bench/src/backends/openai_completions.rs` _+4 more__
- **2026-10-22** [`5af272e53d`](https://github.com/vllm-project/vllm/commit/5af272e53d) [#61871](https://github.com/vllm-project/vllm/pull/61871)
  [Bugfix][Pooling] Fix HTTP 500 from max_tokens_per_doc when the query… (#61871)
  _Files: `vllm/entrypoints/pooling/scoring/io_processor.py`_
- **2026-10-21** [`18e8791134`](https://github.com/vllm-project/vllm/commit/18e8791134) [#62823](https://github.com/vllm-project/vllm/pull/62823)
  [Rust Frontend] Apply response_format over structured_outputs like Python (#62823)
  _Files: `rust/src/server/src/routes/openai/utils/structured_outputs.rs`_
- **2026-10-21** [`5ea2c7ff1e`](https://github.com/vllm-project/vllm/commit/5ea2c7ff1e) [#62706](https://github.com/vllm-project/vllm/pull/62706)
  [Frontend] Share ChatStreamProcessor between chat streaming and derender (#62706)
  _Files: `tests/entrypoints/openai/chat_completion/test_stream_processor.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/chat_completion/stream_processor.py` _+1 more__
- **2026-10-20** [`4964e44825`](https://github.com/vllm-project/vllm/commit/4964e44825) [#62663](https://github.com/vllm-project/vllm/pull/62663)
  [Rust Frontend] Report error type and code like Python (#62663)
  _Files: `rust/src/server/src/error.rs`, `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/openai/utils/types.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-10-20** [`3eb3145bd0`](https://github.com/vllm-project/vllm/commit/3eb3145bd0) [#62662](https://github.com/vllm-project/vllm/pull/62662)
  [Rust Frontend] Accept null for nullable request booleans (#62662)
  _Files: `rust/src/server/src/grpc/convert.rs`, `rust/src/server/src/routes/inference/generate/convert.rs`, `rust/src/server/src/routes/inference/generate/types.rs`, `rust/src/server/src/routes/openai/chat_completions/types.rs` _+5 more__
- **2026-10-20** [`68098c7c4f`](https://github.com/vllm-project/vllm/commit/68098c7c4f) [#62643](https://github.com/vllm-project/vllm/pull/62643)
  [Rust Frontend] Accept empty stream_options without streaming (#62643)
  _Files: `rust/src/server/src/routes/inference/generate/validate.rs`, `rust/src/server/src/routes/openai/chat_completions/types.rs`, `rust/src/server/src/routes/openai/chat_completions/validate.rs`, `rust/src/server/src/routes/openai/completions/validate.rs` _+1 more__
- **2026-10-20** [`03dd81a584`](https://github.com/vllm-project/vllm/commit/03dd81a584) [#62428](https://github.com/vllm-project/vllm/pull/62428)
  [Rust Frontend] Accept top_logprobs=0 without logprobs (#62428)
  _Files: `rust/src/server/src/routes/openai/chat_completions/types.rs`, `rust/src/server/src/routes/openai/chat_completions/validate.rs`_
- **2026-10-20** [`255e3a310c`](https://github.com/vllm-project/vllm/commit/255e3a310c) [#62434](https://github.com/vllm-project/vllm/pull/62434)
  [Rust Frontend] Reject silently dropped request fields on chat, completions, and generate (#62434)
  _Files: `rust/src/server/src/routes/inference/generate/convert.rs`, `rust/src/server/src/routes/inference/generate/types.rs`, `rust/src/server/src/routes/inference/generate/validate.rs`, `rust/src/server/src/routes/openai/chat_completions/types.rs` _+5 more__
- **2026-10-20** [`5528685552`](https://github.com/vllm-project/vllm/commit/5528685552) [#62431](https://github.com/vllm-project/vllm/pull/62431)
  [Rust Frontend] Make unhandled `vllm serve` frontend flags explicit (#62431)
  _Files: `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`_
- **2026-10-20** [`d3c9c73307`](https://github.com/vllm-project/vllm/commit/d3c9c73307) [#62449](https://github.com/vllm-project/vllm/pull/62449)
  [Bugfix][Frontend] Return prompt token IDs from derender when requested (#62449)
  _Files: `docs/serving/online_serving/derenderer.md`, `tests/entrypoints/scale_out/derender/test_derender.py`, `tests/entrypoints/scale_out/render/test_render.py`, `vllm/entrypoints/scale_out/derender/serving.py` _+2 more__
- **2026-10-20** [`8dfbeeeac9`](https://github.com/vllm-project/vllm/commit/8dfbeeeac9) [#52505](https://github.com/vllm-project/vllm/pull/52505)
  [Frontend] Write run-batch responses incrementally instead of at the end (#52505)
  _Files: `examples/features/openai_batch/README.md`, `tests/entrypoints/launchers/test_run_batch.py`, `vllm/entrypoints/launchers/run_batch.py`_
- **2026-10-20** [`473cc8ec72`](https://github.com/vllm-project/vllm/commit/473cc8ec72) [#59489](https://github.com/vllm-project/vllm/pull/59489)
  [Rust][Benchmark] Add openai-responses backend to vllm-bench (#59489)
  _Files: `rust/src/bench/README.md`, `rust/src/bench/src/backends/mod.rs`, `rust/src/bench/src/backends/openai_responses.rs`, `rust/src/bench/src/cli.rs`_
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

## Disaggregation / PD  (29 commits)

- **2026-10-26** [`beeed65c10`](https://github.com/vllm-project/vllm/commit/beeed65c10) [#62242](https://github.com/vllm-project/vllm/pull/62242)
  [Bugfix][KV Connector] Report every transfer group as loaded in DecodeBenchConnector (#62242)
  _Files: `tests/v1/core/test_prefix_replay.py`, `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`_
- **2026-10-26** [`330c5bffee`](https://github.com/vllm-project/vllm/commit/330c5bffee) [#63224](https://github.com/vllm-project/vllm/pull/63224)
  [Bugfix][KV Events] Prevent replay truncation when the send queue fills (#63224)
  _Files: `tests/distributed/test_events.py`, `vllm/config/kv_events.py`, `vllm/distributed/kv_events.py`_
- **2026-10-25** [`c9dbc92630`](https://github.com/vllm-project/vllm/commit/c9dbc92630) [#63460](https://github.com/vllm-project/vllm/pull/63460)
  [Refactor][RL] Share NCCL trainer rendezvous initialization (#63460)
  _Files: `tests/distributed/test_weight_transfer.py`, `vllm/distributed/weight_transfer/nccl_common.py`, `vllm/distributed/weight_transfer/nccl_engine.py`, `vllm/distributed/weight_transfer/sparse_nccl_engine.py`_
- **2026-10-25** [`57ab2f35ac`](https://github.com/vllm-project/vllm/commit/57ab2f35ac) [#63457](https://github.com/vllm-project/vllm/pull/63457)
  [Hardware] Use accelerator APIs in weight transfer (#63457)
  _Files: `vllm/distributed/weight_transfer/ipc_engine.py`, `vllm/distributed/weight_transfer/nccl_engine.py`, `vllm/distributed/weight_transfer/packed_tensor.py`, `vllm/distributed/weight_transfer/sharded_rdt_engine.py` _+2 more__
- **2026-10-24** [`c0f9fff649`](https://github.com/vllm-project/vllm/commit/c0f9fff649) [#61791](https://github.com/vllm-project/vllm/pull/61791)
  [UMBP][3/10] Add shared lookup, transfer, hybrid, and observability (#61791)
  _Files: `tests/v1/kv_connector/umbp_test_utils.py`, `tests/v1/kv_connector/unit/test_umbp_core.py`, `vllm/distributed/kv_transfer/kv_connector/v1/umbp/__init__.py`, `vllm/distributed/kv_transfer/kv_connector/v1/umbp/connector.py` _+5 more__
- **2026-10-23** [`933f7962ae`](https://github.com/vllm-project/vllm/commit/933f7962ae) [#63317](https://github.com/vllm-project/vllm/pull/63317)
  [Rust Frontend] Export Mooncake connector transfer metrics like Python (#63317)
  _Files: `rust/src/engine-core-client/src/metrics.rs`, `rust/src/engine-core-client/src/protocol/stats.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py` _+1 more__
- **2026-10-23** [`83c078d955`](https://github.com/vllm-project/vllm/commit/83c078d955) [#63165](https://github.com/vllm-project/vllm/pull/63165)
  [Bugfix] shm_broadcast: poll the notify socket from busy readers (#63165)
  _Files: `tests/distributed/test_shm_broadcast.py`, `vllm/distributed/device_communicators/shm_broadcast.py`_
- **2026-10-23** [`5c3d7ac9b6`](https://github.com/vllm-project/vllm/commit/5c3d7ac9b6) [#63016](https://github.com/vllm-project/vllm/pull/63016)
  [BugFix] Forward the configured cpu distributed timeout to `cpu_all_reduce_`  (#63016)
  _Files: `tests/distributed/test_cpu_all_reduce.py`, `tests/v1/engine/test_engine_core.py`, `vllm/config/parallel.py`, `vllm/distributed/parallel_state.py` _+3 more__
- **2026-10-23** [`544f182d9f`](https://github.com/vllm-project/vllm/commit/544f182d9f) [#63222](https://github.com/vllm-project/vllm/pull/63222)
  [Doc] Kimi-K3: document the GB300 disaggregated specialized-decode points in the guide and command builder (#63222)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-22** [`01ab87600e`](https://github.com/vllm-project/vllm/commit/01ab87600e) [#56939](https://github.com/vllm-project/vllm/pull/56939)
  [KV Connector][Mooncake] Expose transfer stats via Prometheus (#56939)
  _Files: `docs/features/mooncake_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_stats.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/stats.py`_
- **2026-10-22** [`e7bb7e2f20`](https://github.com/vllm-project/vllm/commit/e7bb7e2f20) [#56430](https://github.com/vllm-project/vllm/pull/56430)
  [bug-fix] Fix KV block leak with fault tolerance enabled in P/D disaggregation (#56430)
  _Files: `.buildkite/test_areas/fault_tolerance.yaml`, `tests/v1/executor/test_executor.py`, `tests/v1/fault_tolerance/test_engine_core_sentinel.py`, `tests/v1/kv_connector/unit/test_output_aggregator.py` _+6 more__
- **2026-10-22** [`c723f6d3ee`](https://github.com/vllm-project/vllm/commit/c723f6d3ee) [#62555](https://github.com/vllm-project/vllm/pull/62555)
  [Bugfix][RL] Fix cross-stream reuse of packed NCCL receive buffers (#62555)
  _Files: `tests/distributed/test_packed_tensor.py`, `vllm/distributed/weight_transfer/packed_tensor.py`_
- **2026-10-22** [`667859505b`](https://github.com/vllm-project/vllm/commit/667859505b) [#60298](https://github.com/vllm-project/vllm/pull/60298)
  [CI][Test][1/N] Enable unit tests to run on Rubin (#60298)
  _Files: `tests/compile/passes/test_fusion_attn.py`, `tests/distributed/test_custom_all_gather_reduce_scatter.py`, `tests/distributed/test_custom_all_reduce.py`, `tests/kernels/test_fused_deepseek_v32_norm_rope.py` _+2 more__
- **2026-10-22** [`30aded62d4`](https://github.com/vllm-project/vllm/commit/30aded62d4) [#52921](https://github.com/vllm-project/vllm/pull/52921)
  [Bugfix] Align CPU offload pool size across PP/spec-decode workers (#52921)
  _Files: `tests/config/test_config_utils.py`, `tests/v1/kv_connector/unit/test_simple_cpu_offload_connector.py`, `tests/v1/simple_kv_offload/test_scheduler.py`, `tests/v1/simple_kv_offload/test_worker.py` _+8 more__
- **2026-10-21** [`1c87991978`](https://github.com/vllm-project/vllm/commit/1c87991978) [#55700](https://github.com/vllm-project/vllm/pull/55700)
  [Feat][Frontend] Add Watchdog for Engine and Worker Monitoring (#55700)
  _Files: `tests/config/test_watchdog_config.py`, `tests/utils_/test_watch_dog.py`, `tests/v1/engine/test_engine_core_shutdown_signal.py`, `tests/v1/engine/test_startup_watch_processes.py` _+9 more__
- **2026-10-21** [`532a7d19d2`](https://github.com/vllm-project/vllm/commit/532a7d19d2) [#55901](https://github.com/vllm-project/vllm/pull/55901)
  [MyPy] Fix mypy errors in KV connector tests (kv-B) (#55901)
  _Files: `tests/v1/kv_connector/extract_hidden_states_integration/test_extraction.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker_metadata.py` _+8 more__
- **2026-10-20** [`3a1bd8347a`](https://github.com/vllm-project/vllm/commit/3a1bd8347a) [#55542](https://github.com/vllm-project/vllm/pull/55542)
  [MyPy] Fix mypy errors in easy tests/v1/kv_connector files (kv-A) (#55542)
  _Files: `tests/v1/kv_connector/nixl_integration/test_spec_decode_acceptance.py`, `tests/v1/kv_connector/unit/test_cache_pollution_prevention.py`, `tests/v1/kv_connector/unit/test_error_propagation.py`, `tests/v1/kv_connector/unit/test_flexkv_connector.py` _+13 more__
- **2026-10-20** [`af31693312`](https://github.com/vllm-project/vllm/commit/af31693312) [#59898](https://github.com/vllm-project/vllm/pull/59898)
  [Distributed] Include NCCL's last error in pynccl error messages (#59898)
  _Files: `tests/distributed/test_pynccl.py`, `vllm/distributed/device_communicators/pynccl_wrapper.py`_
- **2026-10-20** [`8122776fba`](https://github.com/vllm-project/vllm/commit/8122776fba) [#58154](https://github.com/vllm-project/vllm/pull/58154)
  [Bugfix][Distributed] Preserve symmetric collective outputs (#58154)
  _Files: `tests/distributed/test_nccl_symm_mem.py`, `vllm/distributed/device_communicators/cuda_communicator.py`_
- **2026-10-20** [`165152f668`](https://github.com/vllm-project/vllm/commit/165152f668) [#62710](https://github.com/vllm-project/vllm/pull/62710)
  [Doc] Fix Kimi-K3 GB300 disaggregated selector and guide gaps (#62710)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-20** [`fce64bc5c2`](https://github.com/vllm-project/vllm/commit/fce64bc5c2) [#35911](https://github.com/vllm-project/vllm/pull/35911)
  [RL] Send NCCL weight metadata once and reuse it (#35911)
  _Files: `docs/training/weight_transfer/nccl.md`, `tests/distributed/test_weight_transfer.py`, `vllm/distributed/weight_transfer/nccl_engine.py`_
- **2026-10-20** [`34ac4f96a3`](https://github.com/vllm-project/vllm/commit/34ac4f96a3) [#62282](https://github.com/vllm-project/vllm/pull/62282)
  [Bugfix][KV Connector][Mooncake] Wait for all peers before completing failed receives to avoid potential KV block write-after-free (#62282)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-10-20** [`5c399f2700`](https://github.com/vllm-project/vllm/commit/5c399f2700) [#62563](https://github.com/vllm-project/vllm/pull/62563)
  [Doc] Add Kimi-K3 GB300 Dynamo disaggregated profile to the recipe selector (#62563)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-20** [`75eb034ce6`](https://github.com/vllm-project/vllm/commit/75eb034ce6) [#62579](https://github.com/vllm-project/vllm/pull/62579)
  [CI] Keep a per-PR 2-GPU core of the NIXL PD accuracy sweeps (#62579)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_core_test.sh`_
- **2026-10-20** [`17dd7d8fdd`](https://github.com/vllm-project/vllm/commit/17dd7d8fdd) [#62489](https://github.com/vllm-project/vllm/pull/62489)
  [Bugfix][AuxOutput] Send routed-experts block hashes only for computed or scheduled blocks (#62489)
  _Files: `tests/distributed/aux_output_connector/test_store.py`, `tests/v1/core/test_scheduler.py`, `vllm/distributed/aux_output_connector/connector.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-19** [`0b7ae8f532`](https://github.com/vllm-project/vllm/commit/0b7ae8f532) [#62564](https://github.com/vllm-project/vllm/pull/62564)
  [CI] Run the heaviest 4xL4 steps nightly only (#62564)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/distributed.yaml`_
- **2026-10-19** [`b188771f98`](https://github.com/vllm-project/vllm/commit/b188771f98) [#62528](https://github.com/vllm-project/vllm/pull/62528)
  [Doc] Document Kimi-K3 GB300 disaggregated AgentX profile (#62528)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-19** [`afe2183f2b`](https://github.com/vllm-project/vllm/commit/afe2183f2b) [#59635](https://github.com/vllm-project/vllm/pull/59635)
  [KV Connector] Support sleep mode with the NIXL pull connector (#59635)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/engine/test_engine_core.py`, `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/test_accuracy.py` _+10 more__
- **2026-10-19** [`b29be52357`](https://github.com/vllm-project/vllm/commit/b29be52357) [#62392](https://github.com/vllm-project/vllm/pull/62392)
  [Perf][AuxOutput] Do not rescan referenced keys in the routed-experts store (#62392)
  _Files: `tests/distributed/aux_output_connector/test_store.py`, `vllm/distributed/aux_output_connector/store.py`_

## KV Cache / Offload  (27 commits)

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
- **2026-10-25** [`1757f6720c`](https://github.com/vllm-project/vllm/commit/1757f6720c) [#61390](https://github.com/vllm-project/vllm/pull/61390)
  [Bugfix][KV Offload] Treat an already-published fs block as stored (#61390)
  _Files: `csrc/fs_io.cpp`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `vllm/v1/kv_offload/tiering/fs/io.py`_
- **2026-10-25** [`6f51433838`](https://github.com/vllm-project/vllm/commit/6f51433838) [#63010](https://github.com/vllm-project/vllm/pull/63010)
  [Bugfix][KV Offload] Reset the store cursor when a request restarts from token 0 (#63010)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-25** [`503e4e16ad`](https://github.com/vllm-project/vllm/commit/503e4e16ad) [#63126](https://github.com/vllm-project/vllm/pull/63126)
  [Bugfix][KV Offload] Catch async lookup iterator errors (#63126)
  _Files: `tests/v1/kv_offload/tiering/test_async_lookup.py`, `vllm/v1/kv_offload/tiering/async_lookup.py`_
- **2026-10-25** [`4a81a50976`](https://github.com/vllm-project/vllm/commit/4a81a50976) [#55576](https://github.com/vllm-project/vllm/pull/55576)
  [Bugfix][KV Offload] Enable NIXL telemetry for the OBJ tier (#55576)
  _Files: `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/tiering/obj/manager.py`_
- **2026-10-25** [`2b1f75c80f`](https://github.com/vllm-project/vllm/commit/2b1f75c80f) [#61780](https://github.com/vllm-project/vllm/pull/61780)
  [Bugfix][KV Offload] Treat failed secondary-tier stores as back-pressure (#61780)
  _Files: `tests/v1/kv_offload/tiering/test_backpressure.py`, `vllm/v1/kv_offload/tiering/backpressure.py`, `vllm/v1/kv_offload/tiering/manager.py`_
- **2026-10-25** [`921ed7fa11`](https://github.com/vllm-project/vllm/commit/921ed7fa11) [#60810](https://github.com/vllm-project/vllm/pull/60810)
  [Bugfix][KV Offload] Reset a resumed streaming session's block table in OffloadingConnector and SimpleCPUOffloadConnector (#60810)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/utils.py` _+2 more__
- **2026-10-25** [`65bc698356`](https://github.com/vllm-project/vllm/commit/65bc698356) [#63266](https://github.com/vllm-project/vllm/pull/63266)
  [Bugfix][KV Offload] Reject misaligned chunked-local CPU suffix hits (#63266)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/simple_kv_offload/test_integration.py`, `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-10-24** [`ae06591864`](https://github.com/vllm-project/vllm/commit/ae06591864) [#63045](https://github.com/vllm-project/vllm/pull/63045)
  [Kimi K3] KDA RecoverSSM: CuTe verify and commit kernels, records outside the KV cache (#63045)
  _Files: `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `tests/models/kimi_k3/test_recoverssm_kernels.py`, `vllm/config/vllm.py` _+11 more__
- **2026-10-23** [`aea0513a32`](https://github.com/vllm-project/vllm/commit/aea0513a32) [#62591](https://github.com/vllm-project/vllm/pull/62591)
  [Bugfix][AuxOutput] Retain routed experts while a KV cache tier holds their blocks (#62591)
  _Files: `tests/distributed/aux_output_connector/test_store.py`, `tests/v1/core/test_scheduler.py`, `vllm/config/aux_output.py`, `vllm/distributed/aux_output_connector/connector.py` _+4 more__
- **2026-10-23** [`c3117c7441`](https://github.com/vllm-project/vllm/commit/c3117c7441) [#59405](https://github.com/vllm-project/vllm/pull/59405)
  [CPU][Bugfix] Skip KV cache memory reservation for pooling models (#59405)
  _Files: `vllm/v1/worker/cpu_worker.py`_
- **2026-10-22** [`c722f3a536`](https://github.com/vllm-project/vllm/commit/c722f3a536) [#61822](https://github.com/vllm-project/vllm/pull/61822)
  [Docs][KV Offload] Document canonical_layout in the KV offloading usage guide (#61822)
  _Files: `docs/features/kv_offloading_usage.md`_
- **2026-10-21** [`550c1cbb8b`](https://github.com/vllm-project/vllm/commit/550c1cbb8b) [#59703](https://github.com/vllm-project/vllm/pull/59703)
  [KV Offload] Preserve group classification on placeholder events (#59703)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-21** [`6af9fc27fc`](https://github.com/vllm-project/vllm/commit/6af9fc27fc) [#59855](https://github.com/vllm-project/vllm/pull/59855)
  [Bugfix][KV Offload] Capture event metadata for pending promotions (#59855)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py` _+3 more__
- **2026-10-21** [`979be69b2c`](https://github.com/vllm-project/vllm/commit/979be69b2c) [#61758](https://github.com/vllm-project/vllm/pull/61758)
  [Bugfix] Include KV cache quantization settings in IPC weight cache key (#61758)
  _Files: `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py` _+1 more__
- **2026-10-21** [`c2861f7f12`](https://github.com/vllm-project/vllm/commit/c2861f7f12) [#62373](https://github.com/vllm-project/vllm/pull/62373)
  [CI][KV Offload] Signal async lookup results once they can be drained (#62373)
  _Files: `tests/v1/kv_offload/tiering/test_async_lookup.py`_
- **2026-10-19** [`4bd75e952a`](https://github.com/vllm-project/vllm/commit/4bd75e952a) [#60374](https://github.com/vllm-project/vllm/pull/60374)
  [Bugfix][KV Offload][P2P] Report NIXL submission failures and escalate persistent faults to session teardown (#60374)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_data_transport.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/data/base.py` _+4 more__

## CI / Build  (25 commits)

- **2026-10-26** [`cd9aa5b5ee`](https://github.com/vllm-project/vllm/commit/cd9aa5b5ee) [#63601](https://github.com/vllm-project/vllm/pull/63601)
  [Bugfix][Platform] Keep PIN_MEMORY eager; avoid resolving platform during import vllm (#63601)
  _Files: `.buildkite/test_areas/plugins.yaml`, `tests/test_force_first_config.py`, `vllm/env_override.py`, `vllm/envs.py` _+4 more__
- **2026-10-25** [`a7407ab445`](https://github.com/vllm-project/vllm/commit/a7407ab445) [#63616](https://github.com/vllm-project/vllm/pull/63616)
  [Benchmark] Add steady-state PP support to bench forward (#63616)
  _Files: `.buildkite/test_areas/distributed.yaml`, `docs/benchmarking/cli.md`, `docs/cli/README.md`, `tests/benchmarks/test_forward_cli.py` _+2 more__
- **2026-10-25** [`d4d647b2b5`](https://github.com/vllm-project/vllm/commit/d4d647b2b5) [#63253](https://github.com/vllm-project/vllm/pull/63253)
  [Kernel] Update DeepGEMM commit (#63253)
  _Files: `cmake/external_projects/deepgemm.cmake`_
- **2026-10-25** [`71a8275604`](https://github.com/vllm-project/vllm/commit/71a8275604) [#63259](https://github.com/vllm-project/vllm/pull/63259)
  [CI] Trigger recipe previews and the recipes.vllm.ai sync on push (#63259)
  _Files: `.github/workflows/recipes-preview.yml`_
- **2026-10-24** [`be2de71198`](https://github.com/vllm-project/vllm/commit/be2de71198) [#63462](https://github.com/vllm-project/vllm/pull/63462)
  [CI][Bench] Keep captured request headers case-insensitive in Responses test (#63462)
  _Files: `tests/benchmarks/test_responses_request_func.py`_
- **2026-10-24** [`717cf84342`](https://github.com/vllm-project/vllm/commit/717cf84342) [#63248](https://github.com/vllm-project/vllm/pull/63248)
  [CI] Label recipe PRs and link their recipes.vllm.ai preview (#63248)
  _Files: `.github/mergify.yml`, `recipes/README.md`_
- **2026-10-24** [`1bd56eaef3`](https://github.com/vllm-project/vllm/commit/1bd56eaef3) [#63449](https://github.com/vllm-project/vllm/pull/63449)
  [CI][Kimi-K3] Expect no trailing-block drop in DSpark resend tests (#63449)
  _Files: `tests/models/kimi_k3/test_prefix_cache.py`_
- **2026-10-23** [`7105440c40`](https://github.com/vllm-project/vllm/commit/7105440c40) [#63394](https://github.com/vllm-project/vllm/pull/63394)
  [Doc] MiniMax-M3: use the autotune flag the pinned GB200 nightly accepts, fix golden-AL links (#63394)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`_
- **2026-10-23** [`7651825993`](https://github.com/vllm-project/vllm/commit/7651825993) [#62540](https://github.com/vllm-project/vllm/pull/62540)
  [CI] Automatically label Reflection Beam model changes (#62540)
  _Files: `.github/mergify.yml`, `.github/workflows/issue_autolabel.yml`_
- **2026-10-23** [`5c465dda9d`](https://github.com/vllm-project/vllm/commit/5c465dda9d) [#63313](https://github.com/vllm-project/vllm/pull/63313)
  [Rust Frontend] Report every invalid logit_bias key like Python (#63313)
  _Files: `.buildkite/test_areas/rust_frontend.yaml`, `rust/src/server/src/utils.rs`_
- **2026-10-23** [`e0e5e6ee0a`](https://github.com/vllm-project/vllm/commit/e0e5e6ee0a) [#63299](https://github.com/vllm-project/vllm/pull/63299)
  [Bugfix][CPU][CI] Accept assigned nodes in the no-Triton worker test (#63299)
  _Files: `tests/v1/worker/test_gpu_worker.py`_
- **2026-10-23** [`14b4576e70`](https://github.com/vllm-project/vllm/commit/14b4576e70) [#63191](https://github.com/vllm-project/vllm/pull/63191)
  [Security][CI/Build] Bump uv to 0.13.4 in CI scripts for eMudhra CA distrust (#63191)
  _Files: `.buildkite/scripts/run-rust-frontend-cargo-ci.sh`, `.buildkite/scripts/upload-release-wheels-pypi.sh`_
- **2026-10-23** [`e38af8bdc9`](https://github.com/vllm-project/vllm/commit/e38af8bdc9) [#63201](https://github.com/vllm-project/vllm/pull/63201)
  [CI][Test] Compare bf16 token embeddings by cosine similarity (#63201)
  _Files: `tests/entrypoints/pooling/token_embed/test_online.py`_
- **2026-10-23** [`d5d8ccaae6`](https://github.com/vllm-project/vllm/commit/d5d8ccaae6) [#63084](https://github.com/vllm-project/vllm/pull/63084)
  [XPU] temporarily ignore test_cumem.py::test_basic_cumem (#63084)
  _Files: `.buildkite/intel_jobs/basic_correctness_intel.yaml`_
- **2026-10-23** [`432b1003f8`](https://github.com/vllm-project/vllm/commit/432b1003f8) [#62576](https://github.com/vllm-project/vllm/pull/62576)
  [Bugfix] Defer MRV2 Triton validation to worker startup (#62576)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/test_config.py`, `tests/v1/worker/test_gpu_worker.py`, `vllm/config/vllm.py` _+1 more__
- **2026-10-22** [`6ee316eaea`](https://github.com/vllm-project/vllm/commit/6ee316eaea) [#63080](https://github.com/vllm-project/vllm/pull/63080)
  upgrade tpu-inference to v0.32.0 and torch to 2.14.0 (#63080)
  _Files: `requirements/build/tpu.txt`, `requirements/tpu.txt`_
- **2026-10-22** [`c1249873af`](https://github.com/vllm-project/vllm/commit/c1249873af) [#63067](https://github.com/vllm-project/vllm/pull/63067)
  [CI] Expect 400 from /v1/embeddings for bge-m3 token_embed (#63067)
  _Files: `tests/models/language/pooling/test_bge_m3.py`_
- **2026-10-21** [`0746329d2a`](https://github.com/vllm-project/vllm/commit/0746329d2a) [#62989](https://github.com/vllm-project/vllm/pull/62989)
  [CI] Auto-apply the hisparse label (#62989)
  _Files: `.github/mergify.yml`_
- **2026-10-21** [`a0a645abda`](https://github.com/vllm-project/vllm/commit/a0a645abda) [#62879](https://github.com/vllm-project/vllm/pull/62879)
  [CI][KV Connector] Start NIXL accuracy decoders after prefillers on shared GPUs (#62879)
  _Files: `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`_
- **2026-10-21** [`f4c07f326c`](https://github.com/vllm-project/vllm/commit/f4c07f326c) [#62829](https://github.com/vllm-project/vllm/pull/62829)
  [XPU][CI] Skip test_bench_forward on XPU (#62829)
  _Files: `tests/benchmarks/test_forward_cli.py`_
- **2026-10-21** [`c835207fcc`](https://github.com/vllm-project/vllm/commit/c835207fcc) [#62616](https://github.com/vllm-project/vllm/pull/62616)
  [XPU][CI] Add kaldi-native-fbank to XPU test requirements (#62616)
  _Files: `requirements/test/xpu.in`, `requirements/test/xpu.txt`_
- **2026-10-20** [`88262cf7d1`](https://github.com/vllm-project/vllm/commit/88262cf7d1) [#61415](https://github.com/vllm-project/vllm/pull/61415)
  [CI] Release the previous checkpoint's page cache between LM Eval models (#61415)
  _Files: `.buildkite/lm-eval-harness/test_lm_eval_correctness.py`, `vllm/model_executor/model_loader/weight_utils.py`_
- **2026-10-20** [`e1faffbaa5`](https://github.com/vllm-project/vllm/commit/e1faffbaa5) [#62422](https://github.com/vllm-project/vllm/pull/62422)
  [CI][XPU] Ignore test_weight_cache.py in Intel CI (#62422)
  _Files: `.buildkite/intel_jobs/model_executor_intel.yaml`_
- **2026-10-19** [`04631c4915`](https://github.com/vllm-project/vllm/commit/04631c4915) [#62547](https://github.com/vllm-project/vllm/pull/62547)
  [Security][CI/Build] Add pre-commit check for hardcoded trust_remote_code=True (#62547)
  _Files: `.buildkite/test_areas/misc.yaml`, `.pre-commit-config.yaml`, `tests/tools/test_check_trust_remote_code.py`, `tools/pre_commit/check_trust_remote_code.py`_
- **2026-10-19** [`b9df8980fb`](https://github.com/vllm-project/vllm/commit/b9df8980fb) [#61442](https://github.com/vllm-project/vllm/pull/61442)
  [CI][Tests] Add SM107a to DeepEP build (#61442)
  _Files: `docker/Dockerfile`_

## Models  (24 commits)

- **2026-10-26** [`41d9d1e14d`](https://github.com/vllm-project/vllm/commit/41d9d1e14d) [#61094](https://github.com/vllm-project/vllm/pull/61094)
  [Frontend] Add --reasoning-effort-map to rewrite request reasoning efforts (#61094)
  _Files: `docs/features/reasoning_outputs.md`, `tests/entrypoints/common/test_cli_args.py`, `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py` _+15 more__
- **2026-10-25** [`0765565f10`](https://github.com/vllm-project/vllm/commit/0765565f10) [#63495](https://github.com/vllm-project/vllm/pull/63495)
  [Pooling] Reduce Clef metadata overhead (#63495)
  _Files: `vllm/model_executor/models/clef_joint_schema.py`_
- **2026-10-25** [`75fc05a53a`](https://github.com/vllm-project/vllm/commit/75fc05a53a) [#60149](https://github.com/vllm-project/vllm/pull/60149)
  [Model] Add Dory support (#60149)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/models/test_dory.py` _+6 more__
- **2026-10-25** [`24324ef0f6`](https://github.com/vllm-project/vllm/commit/24324ef0f6) [#63537](https://github.com/vllm-project/vllm/pull/63537)
  [CI] Fix the Qwen2 embed memory leak and HfRunner no-cache logprobs (#63537)
  _Files: `tests/conftest.py`, `tests/models/language/pooling/test_embedding.py`_
- **2026-10-25** [`b70de52965`](https://github.com/vllm-project/vllm/commit/b70de52965) [#63538](https://github.com/vllm-project/vllm/pull/63538)
  [Bugfix][Model] Borrow Gemma4 _get_max_soft_tokens in EmbeddingGemma2 and DiffusionGemma (#63538)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`, `vllm/model_executor/models/embedding_gemma2.py`_
- **2026-10-23** [`a0544b13f2`](https://github.com/vllm-project/vllm/commit/a0544b13f2) [#63178](https://github.com/vllm-project/vllm/pull/63178)
  [Docs][Mistral] Note that required and named tool choice may not produce a call (#63178)
  _Files: `docs/features/tool_calling.md`_
- **2026-10-23** [`08aa305fb5`](https://github.com/vllm-project/vllm/commit/08aa305fb5) [#62544](https://github.com/vllm-project/vllm/pull/62544)
  [Model] Add Domyn Edge support (#62544)
  _Files: `docs/models/supported_models.md`, `tests/models/language/generation/test_common.py`, `tests/models/registry.py`, `vllm/model_executor/models/domyn_edge.py` _+1 more__
- **2026-10-23** [`afd07e4ddb`](https://github.com/vllm-project/vllm/commit/afd07e4ddb) [#63059](https://github.com/vllm-project/vllm/pull/63059)
  [Rust Frontend] Accept Gemma 4 tool calls without the call prefix like Python (#63059)
  _Files: `rust/src/parser/src/unified/gemma4.rs`_
- **2026-10-23** [`9bd5c2a058`](https://github.com/vllm-project/vllm/commit/9bd5c2a058) [#60613](https://github.com/vllm-project/vllm/pull/60613)
  [Bugfix][DSv4.1] Seed the -1 sentinel in the prefill sparse index workspace (#60613)
  _Files: `vllm/models/deepseek_v41/common/ops/cache_utils.py`_
- **2026-10-22** [`38955340b7`](https://github.com/vllm-project/vllm/commit/38955340b7) [#62843](https://github.com/vllm-project/vllm/pull/62843)
  [Perf][GLM-5.3] Enable GLM low-latency BF16 GEMM on SM107 (#62843)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm.py`_
- **2026-10-22** [`f235b89bdf`](https://github.com/vllm-project/vllm/commit/f235b89bdf) [#62194](https://github.com/vllm-project/vllm/pull/62194)
  [Model] NemotronHMTP: share the target's embedding and LM head (#62194)
  _Files: `tests/v1/worker/test_spec_decode_embed_sharing_pp.py`, `vllm/model_executor/models/nemotron_h_mtp.py`, `vllm/v1/spec_decode/llm_base_proposer.py`_
- **2026-10-22** [`390836a393`](https://github.com/vllm-project/vllm/commit/390836a393) [#63050](https://github.com/vllm-project/vllm/pull/63050)
  [Bugfix][Model] Load Granite Speech checkpoints saved by Transformers v5 (#63050)
  _Files: `vllm/model_executor/models/granite_speech.py`_
- **2026-10-22** [`ab9e54847e`](https://github.com/vllm-project/vllm/commit/ab9e54847e) [#62875](https://github.com/vllm-project/vllm/pull/62875)
  [Rust Frontend] Match DeepSeek DSML markers by token identity (#62875)
  _Files: `rust/src/parser/benches/deepseek_v32.rs`, `rust/src/parser/benches/utils/mod.rs`, `rust/src/parser/src/tool/deepseek_dsml/deepseek_v32.rs`, `rust/src/parser/src/tool/deepseek_dsml/deepseek_v4.rs` _+6 more__
- **2026-10-21** [`fc9b7e6546`](https://github.com/vllm-project/vllm/commit/fc9b7e6546) [#62638](https://github.com/vllm-project/vllm/pull/62638)
  [XPU][Test] Relax streaming/non-streaming equality in mistral tool_choice=none test (#62638)
  _Files: `.buildkite/intel_jobs/entrypoints_intel.yaml`, `tests/tool_use/mistral/test_mistral_tool_calls.py`_
- **2026-10-21** [`817fa3518c`](https://github.com/vllm-project/vllm/commit/817fa3518c) [#60082](https://github.com/vllm-project/vllm/pull/60082)
  [Frontend] Add derender output mode to generate (#60082)
  _Files: `docs/serving/online_serving/derenderer.md`, `docs/serving/online_serving/token_in_token_out.md`, `pyproject.toml`, `tests/entrypoints/cohere/test_api_router.py` _+12 more__
- **2026-10-21** [`85752a43c3`](https://github.com/vllm-project/vllm/commit/85752a43c3) [#62652](https://github.com/vllm-project/vllm/pull/62652)
  [Bugfix][Model] Preserve target-token scoring rows during DeepSeek-V4.1 replay (#62652)
  _Files: `tests/models/test_deepseek_v41_replay_batch.py`, `vllm/models/deepseek_v41/nvidia/model_state.py`_
- **2026-10-20** [`0d00d8b9cf`](https://github.com/vllm-project/vllm/commit/0d00d8b9cf) [#62627](https://github.com/vllm-project/vllm/pull/62627)
  [CI][Bugfix] ColPali miss hidden_size (#62627)
  _Files: `vllm/model_executor/models/colpali.py`_
- **2026-10-19** [`5fd62688ff`](https://github.com/vllm-project/vllm/commit/5fd62688ff) [#61254](https://github.com/vllm-project/vllm/pull/61254)
  [Docs] Add Gemma-2, Granite SWA, Qwen3-0.6B to batch invariance validated models (#61254)
  _Files: `docs/features/batch_invariance.md`_
- **2026-10-19** [`a9104fd3db`](https://github.com/vllm-project/vllm/commit/a9104fd3db) [#62250](https://github.com/vllm-project/vllm/pull/62250)
  [Pooling] Improve SPLADE throughput 3.6% to 7.8%  (#62250)
  _Files: `vllm/model_executor/models/bert.py`_
- **2026-10-19** [`e347836d68`](https://github.com/vllm-project/vllm/commit/e347836d68) [#60362](https://github.com/vllm-project/vllm/pull/60362)
  [Bugfix][Tool Parser] Parse multi-line JSON arguments in the DeepSeek V3 and V3.1 parsers (#60362)
  _Files: `tests/tool_parsers/test_deepseekv31_tool_parser.py`, `tests/tool_parsers/test_deepseekv3_tool_parser.py`, `vllm/tool_parsers/deepseekv31_tool_parser.py`, `vllm/tool_parsers/deepseekv3_tool_parser.py`_
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

## Scheduler / Engine  (21 commits)

- **2026-10-26** [`2383ff0014`](https://github.com/vllm-project/vllm/commit/2383ff0014) [#62734](https://github.com/vllm-project/vllm/pull/62734)
  [Fast Start] Detect weight cache daemon exit in zero-copy engines (#62734)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py`_
- **2026-10-26** [`ee65d02902`](https://github.com/vllm-project/vllm/commit/ee65d02902) [#62456](https://github.com/vllm-project/vllm/pull/62456)
  [Rust Frontend] Select one structured outputs backend for every route (#62456)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/structural_tag.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+11 more__
- **2026-10-25** [`ceb01b6ddf`](https://github.com/vllm-project/vllm/commit/ceb01b6ddf) [#61976](https://github.com/vllm-project/vllm/pull/61976)
  [Bugfix][Core] Keep scheduling running requests after a priority self-preemption (#61976)
  _Files: `vllm/v1/core/sched/scheduler.py`_
- **2026-10-24** [`dd5e754494`](https://github.com/vllm-project/vllm/commit/dd5e754494) [#51974](https://github.com/vllm-project/vllm/pull/51974)
  [Profiling] Add support for profile_prefix payload in HTTP /start_profile endpoint (#51974)
  _Files: `docs/contributing/profiling.md`, `docs/serving/offline_inference.md`, `docs/serving/online_serving/README.md`, `tests/entrypoints/serve/test_profile_api_router.py` _+13 more__
- **2026-10-23** [`d143a9de39`](https://github.com/vllm-project/vllm/commit/d143a9de39) [#63260](https://github.com/vllm-project/vllm/pull/63260)
  [Core] Let VLLM_WORKER_SHUTDOWN_TIMEOUT_SECONDS set the EngineCore cleanup grace after an immediate abort (#63260)
  _Files: `tests/v1/engine/test_startup_watch_processes.py`, `vllm/v1/engine/utils.py`_
- **2026-10-23** [`a50259bb32`](https://github.com/vllm-project/vllm/commit/a50259bb32) [#63371](https://github.com/vllm-project/vllm/pull/63371)
  [vLLM IR] Deprecate ir_op_priority ahead of vLLM IR removal (#63371)
  _Files: `docs/design/vllm_ir.md`, `tests/engine/test_arg_utils.py`, `vllm/config/kernel.py`, `vllm/engine/arg_utils.py`_
- **2026-10-23** [`4bceda5dbf`](https://github.com/vllm-project/vllm/commit/4bceda5dbf) [#62683](https://github.com/vllm-project/vllm/pull/62683)
  [XPU][CI] Run prefix-caching tests for GDN, Mamba and pooling models on XPU (#62683)
  _Files: `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/models_language_intel.yaml`_
- **2026-10-22** [`d0eb5d2f21`](https://github.com/vllm-project/vllm/commit/d0eb5d2f21) [#63138](https://github.com/vllm-project/vllm/pull/63138)
  [Frontend] Expose --sleep-mode-backend on the CLI (#63138)
  _Files: `docs/features/sleep_mode.md`, `tests/engine/test_arg_utils.py`, `vllm/engine/arg_utils.py`_
- **2026-10-22** [`13058ef4d1`](https://github.com/vllm-project/vllm/commit/13058ef4d1) [#62872](https://github.com/vllm-project/vllm/pull/62872)
  [Core][Rust Frontend] Report structured-output compile failures as validation errors (#62872)
  _Files: `rust/src/engine-core-client/src/protocol/output.rs`, `rust/src/server/src/error.rs`, `rust/src/server/src/grpc/convert.rs`, `rust/src/server/src/routes/inference/generate.rs` _+6 more__
- **2026-10-22** [`ddc3f417d4`](https://github.com/vllm-project/vllm/commit/ddc3f417d4) [#62834](https://github.com/vllm-project/vllm/pull/62834)
  [Bugfix][EPD] Check encoder readiness for prefix replay (#62834)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-21** [`40210d8317`](https://github.com/vllm-project/vllm/commit/40210d8317) [#62884](https://github.com/vllm-project/vllm/pull/62884)
  [Bugfix][Core] Release libgomp workers before forking engine processes (#62884)
  _Files: `tests/utils_/test_system_utils.py`, `vllm/utils/system_utils.py`_
- **2026-10-21** [`c1210ccbe5`](https://github.com/vllm-project/vllm/commit/c1210ccbe5) [#62826](https://github.com/vllm-project/vllm/pull/62826)
  [Rust Frontend] Support --custom-histogram-buckets (#62826)
  _Files: `rust/Cargo.lock`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs` _+8 more__
- **2026-10-21** [`bc4794ef9a`](https://github.com/vllm-project/vllm/commit/bc4794ef9a) [#62825](https://github.com/vllm-project/vllm/pull/62825)
  [Rust Frontend] Support VLLM_LOG_STATS_INTERVAL and VLLM_DISABLE_REQUEST_ID_RANDOMIZATION (#62825)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/llm/src/lib.rs`, `rust/src/llm/src/log_stats.rs` _+3 more__
- **2026-10-21** [`6ae1051bd9`](https://github.com/vllm-project/vllm/commit/6ae1051bd9) [#62741](https://github.com/vllm-project/vllm/pull/62741)
  [Rust Frontend] Support --exclude-tools-when-tool-choice-none (#62741)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/harmony/mod.rs`, `rust/src/chat/src/output/structured.rs` _+14 more__
- **2026-10-20** [`88077b746c`](https://github.com/vllm-project/vllm/commit/88077b746c) [#49625](https://github.com/vllm-project/vllm/pull/49625)
  [Bugfix] Reject mixed structured output backends during validation (#49625)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/engine/test_output_processor.py`, `tests/v1/structured_output/test_validation.py`, `vllm/outputs.py` _+2 more__
- **2026-10-20** [`654f78177a`](https://github.com/vllm-project/vllm/commit/654f78177a) [#62661](https://github.com/vllm-project/vllm/pull/62661)
  [Rust Frontend] Cap structured-output JSON nesting at 64 levels (#62661)
  _Files: `rust/src/engine-core-client/src/protocol/structured_outputs.rs`, `rust/src/engine-core-client/src/protocol/structured_outputs/nesting.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs`_
- **2026-10-20** [`29a26e5b0e`](https://github.com/vllm-project/vllm/commit/29a26e5b0e) [#62673](https://github.com/vllm-project/vllm/pull/62673)
  [Rust Frontend] Support --trust-request-chat-template (#62673)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/chat/src/error.rs`, `rust/src/chat/src/renderer/hf/mod.rs` _+10 more__
- **2026-10-20** [`f0c50148a2`](https://github.com/vllm-project/vllm/commit/f0c50148a2) [#55226](https://github.com/vllm-project/vllm/pull/55226)
  [Bugfix][Pooling] Ignore token stream intervals for pooling (#55226)
  _Files: `vllm/v1/engine/output_processor.py`_
- **2026-10-20** [`b8e9001bf9`](https://github.com/vllm-project/vllm/commit/b8e9001bf9) [#61949](https://github.com/vllm-project/vllm/pull/61949)
  [Rust][Frontend] Return routed experts from the generate route (#61949)
  _Files: `rust/src/engine-core-client/src/protocol/output.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py`, `rust/src/llm/src/error.rs` _+10 more__
- **2026-10-19** [`d5b36699b2`](https://github.com/vllm-project/vllm/commit/d5b36699b2) [#51488](https://github.com/vllm-project/vllm/pull/51488)
  [Core] Reject new requests while generation is paused (#51488)
  _Files: `docs/training/async_rl.md`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/stream.rs`, `rust/src/engine-core-client/src/protocol/output.rs` _+30 more__
- **2026-10-19** [`43caf5b352`](https://github.com/vllm-project/vllm/commit/43caf5b352) [#59030](https://github.com/vllm-project/vllm/pull/59030)
  [Bugfix][Core] Requeue encoder-stalled waiting requests (#59030)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_

## LoRA  (18 commits)

- **2026-10-26** [`f1ac0cf20d`](https://github.com/vllm-project/vllm/commit/f1ac0cf20d) [#63694](https://github.com/vllm-project/vllm/pull/63694)
  [XPU][UT] Allow HF reference models to load LoRA adapters by adding PEFT to XPU test dependencies (#63694)
  _Files: `requirements/test/xpu.in`, `requirements/test/xpu.txt`, `tests/models/language/generation/test_hybrid.py`_
- **2026-10-26** [`93dc587bd9`](https://github.com/vllm-project/vllm/commit/93dc587bd9) [#59989](https://github.com/vllm-project/vllm/pull/59989)
  [Bugfix] Fix Qwen3-VL reranker crash on missing tie_word_embeddings in text config (#59989)
  _Files: `vllm/model_executor/models/adapters.py`_
- **2026-10-23** [`b2e178eaa9`](https://github.com/vllm-project/vllm/commit/b2e178eaa9) [#63190](https://github.com/vllm-project/vllm/pull/63190)
  [Bugfix] Skip prompt_embeds passthrough items in set_active_mm_loras (#63190)
  _Files: `tests/v1/worker/test_mm_lora.py`, `vllm/v1/worker/gpu/mm/lora.py`_
- **2026-10-23** [`c569393ed2`](https://github.com/vllm-project/vllm/commit/c569393ed2) [#63320](https://github.com/vllm-project/vllm/pull/63320)
  [CI][Rust Frontend] Run more Python server tests against the Rust frontend (#63320)
  _Files: `.buildkite/test_areas/rust_frontend.yaml`, `tests/entrypoints/openai/chat_completion/test_chat_echo.py`, `tests/entrypoints/openai/chat_completion/test_completion_with_function_calling.py`, `tests/entrypoints/openai/completion/test_completion.py` _+5 more__
- **2026-10-23** [`7b1d07440d`](https://github.com/vllm-project/vllm/commit/7b1d07440d) [#63295](https://github.com/vllm-project/vllm/pull/63295)
  [Bugfix][Rust Frontend] LoraRequest: drop tensorizer_config_dict to match the Python wire layout (#63295)
  _Files: `rust/src/engine-core-client/src/protocol/lora.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py`, `rust/src/llm/tests/generate.rs` _+1 more__
- **2026-10-23** [`4a5ee8fc77`](https://github.com/vllm-project/vllm/commit/4a5ee8fc77) [#63316](https://github.com/vllm-project/vllm/pull/63316)
  [Rust Frontend] Keep load_inplace off cached LoRA requests like Python (#63316)
  _Files: `rust/src/server/src/grpc/control.rs`, `rust/src/server/src/lora.rs`, `rust/src/server/src/routes/openai/models.rs`, `rust/src/server/src/routes/tests.rs` _+1 more__
- **2026-10-22** [`ef5bcaa387`](https://github.com/vllm-project/vllm/commit/ef5bcaa387) [#41482](https://github.com/vllm-project/vllm/pull/41482)
  [bug] Fix lora reloading from disk every step when using AsyncLLM (#41482)
  _Files: `vllm/entrypoints/openai/models/serving.py`_
- **2026-10-22** [`7e005d0f9c`](https://github.com/vllm-project/vllm/commit/7e005d0f9c) [#61279](https://github.com/vllm-project/vllm/pull/61279)
  [Model][LoRA] Enable LoRA support for BERT cross-encoders (#61279)
  _Files: `docs/models/pooling_models/scoring.md`, `vllm/model_executor/models/bert.py`_
- **2026-10-22** [`a11f0cabef`](https://github.com/vllm-project/vllm/commit/a11f0cabef) [#48421](https://github.com/vllm-project/vllm/pull/48421)
  [Bugfix][LoRA] Skip no-LoRA tokens (index -1) in CPU torch bgmv ops (#48421)
  _Files: `tests/lora/test_punica_ops.py`, `vllm/lora/ops/torch_ops/lora_ops.py`_
- **2026-10-22** [`3e58641d1f`](https://github.com/vllm-project/vllm/commit/3e58641d1f) [#60306](https://github.com/vllm-project/vllm/pull/60306)
  [Bugfix][Core] Count unscheduled running requests toward max_loras (#60306)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-10-21** [`96e59c60e0`](https://github.com/vllm-project/vllm/commit/96e59c60e0) [#62883](https://github.com/vllm-project/vllm/pull/62883)
  [CI] Run the remaining 4xL4 steps nightly only (#62883)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/expert_parallelism.yaml`, `.buildkite/test_areas/lora.yaml`, `.buildkite/test_areas/models_distributed.yaml` _+1 more__
- **2026-10-21** [`e8e43c6a09`](https://github.com/vllm-project/vllm/commit/e8e43c6a09) [#61391](https://github.com/vllm-project/vllm/pull/61391)
  [LoRA] Support BERT token classification heads (#61391)
  _Files: `docs/features/lora.md`, `docs/models/pooling_models/token_classify.md`, `vllm/lora/layers/__init__.py`, `vllm/lora/layers/classifier.py` _+5 more__
- **2026-10-21** [`e2d3340087`](https://github.com/vllm-project/vllm/commit/e2d3340087) [#62498](https://github.com/vllm-project/vllm/pull/62498)
  [LoRA][Step5] Support LoRA for Step5 (#62498)
  _Files: `docs/models/supported_models.md`, `vllm/lora/layers/__init__.py`, `vllm/lora/layers/custom_layer.py`, `vllm/lora/utils.py` _+2 more__
- **2026-10-21** [`0495a3de32`](https://github.com/vllm-project/vllm/commit/0495a3de32) [#62679](https://github.com/vllm-project/vllm/pull/62679)
  [XPU][CI] Skip test_deep_sleep_lora_tp2 on non-CUDA platforms (#62679)
  _Files: `tests/basic_correctness/memory/sleep_mode/test_sleep_mode.py`_
- **2026-10-20** [`8407bc0bb6`](https://github.com/vllm-project/vllm/commit/8407bc0bb6) [#62672](https://github.com/vllm-project/vllm/pull/62672)
  [CI][LoRA] Release punica test GPU memory before later engine tests (#62672)
  _Files: `tests/lora/test_punica_ops.py`_
- **2026-10-20** [`86129933fb`](https://github.com/vllm-project/vllm/commit/86129933fb) [#62358](https://github.com/vllm-project/vllm/pull/62358)
  [Bugfix][LoRA] Restore LoRA state on wake-up from level-2 sleep (#62358)
  _Files: `tests/basic_correctness/memory/sleep_mode/test_sleep_mode.py`, `vllm/v1/worker/lora_model_runner_mixin.py`_
- **2026-10-19** [`37891a98ea`](https://github.com/vllm-project/vllm/commit/37891a98ea) [#61884](https://github.com/vllm-project/vllm/pull/61884)
  [Bugfix] Reject LoRA at config time for models without SupportsLoRA (#61884)
  _Files: `tests/test_config.py`, `vllm/config/lora.py`, `vllm/config/model.py`, `vllm/model_executor/models/mamba2.py` _+2 more__
- **2026-10-19** [`83db1ab496`](https://github.com/vllm-project/vllm/commit/83db1ab496) [#61618](https://github.com/vllm-project/vllm/pull/61618)
  [Bugfix][LoRA] Keep failed activations retryable (#61618)
  _Files: `vllm/lora/model_manager.py`_

## Speculative Decoding  (16 commits)

- **2026-10-26** [`85e199e60c`](https://github.com/vllm-project/vllm/commit/85e199e60c) [#62091](https://github.com/vllm-project/vllm/pull/62091)
  [Perf][DSv4.1] Read GPU Engram tables from peers' HBM instead of DP collectives (#62091)
  _Files: `tests/distributed/test_engram_dp_shard.py`, `tests/kernels/test_engram.py`, `vllm/distributed/parallel_state.py`, `vllm/models/deepseek_v41/common/engram.py` _+1 more__
- **2026-10-26** [`39e6a1aafc`](https://github.com/vllm-project/vllm/commit/39e6a1aafc) [#63622](https://github.com/vllm-project/vllm/pull/63622)
  [Benchmark] Include speculative drafting in bench forward (#63622)
  _Files: `.agents/skills/model-microbenchmark/SKILL.md`, `docs/cli/README.md`, `tests/benchmarks/test_forward_cli.py`, `vllm/benchmarks/forward/batch.py` _+5 more__
- **2026-10-26** [`290582fbc5`](https://github.com/vllm-project/vllm/commit/290582fbc5) [#63068](https://github.com/vllm-project/vllm/pull/63068)
  [Bugfix][Multimodal] Respect meta initialization for Engram offload (#63068)
  _Files: `tests/kernels/test_engram.py`, `vllm/models/deepseek_v41/common/engram.py`_
- **2026-10-25** [`fc0cfcdc05`](https://github.com/vllm-project/vllm/commit/fc0cfcdc05) [#61019](https://github.com/vllm-project/vllm/pull/61019)
  [Bugfix][KV Connector] Serve and store OffloadingConnector partial tails with EAGLE/MTP groups (#61019)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-10-23** [`58301f6cb9`](https://github.com/vllm-project/vllm/commit/58301f6cb9) [#63186](https://github.com/vllm-project/vllm/pull/63186)
  [Bugfix][LoRA] Don't reject LoRA for speculative decoding drafters (#63186)
  _Files: `tests/test_config.py`, `vllm/config/lora.py`_
- **2026-10-23** [`37cf712552`](https://github.com/vllm-project/vllm/commit/37cf712552) [#63251](https://github.com/vllm-project/vllm/pull/63251)
  [Spec Decode] Keep drafters within their rotary cache on the V2 model runner (#63251)
  _Files: `docs/features/speculative_decoding/README.md`, `tests/config/test_speculative_draft_limits_max_model_len.py`, `tests/config/test_speculative_draft_max_position_embeddings.py`, `tests/test_config.py` _+2 more__
- **2026-10-22** [`ce9467b757`](https://github.com/vllm-project/vllm/commit/ce9467b757) [#54448](https://github.com/vllm-project/vllm/pull/54448)
  [Core] Add XPress speculative decoding method (#54448)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `tests/models/registry.py`, `tests/v1/e2e/spec_decode/acceptance_rates/xpress/__init__.py`, `tests/v1/e2e/spec_decode/acceptance_rates/xpress/test_xpress.py` _+10 more__
- **2026-10-22** [`124501da07`](https://github.com/vllm-project/vllm/commit/124501da07) [#62692](https://github.com/vllm-project/vllm/pull/62692)
  [Bugfix] Load Engram tables on CPU in the InstantTensor loader (#62692)
  _Files: `tests/model_executor/model_loader/instanttensor_loader/test_weight_utils.py`, `vllm/model_executor/model_loader/default_loader.py`, `vllm/model_executor/model_loader/weight_utils.py`_
- **2026-10-21** [`52a65d7b19`](https://github.com/vllm-project/vllm/commit/52a65d7b19) [#61651](https://github.com/vllm-project/vllm/pull/61651)
  [Model] Add Nemotron Parse 3.5 serving and MTP support (#61651)
  _Files: `docs/models/supported_models.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_nemotron_parse.py`, `tests/models/multimodal/generation/test_nemotron_parse_35.py` _+9 more__
- **2026-10-20** [`4e304b4d1e`](https://github.com/vllm-project/vllm/commit/4e304b4d1e) [#62084](https://github.com/vllm-project/vllm/pull/62084)
  [CI] Move Multimodal Processor, KV Connectors, LoRA, Spec Decode Draft and three more steps from fixed to automatic shards (#62084)
  _Files: `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/lora.yaml`, `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/models_language.yaml` _+2 more__
- **2026-10-20** [`19997aac51`](https://github.com/vllm-project/vllm/commit/19997aac51) [#60823](https://github.com/vllm-project/vllm/pull/60823)
  [Chore] Port more vendored configs and processors to upstream Transformers (#60823)
  _Files: `tests/config/base_model_arch_groundtruth.json`, `tests/models/registry.py`, `tests/transformers_utils/test_muse_glimmer_config.py`, `vllm/config/model.py` _+32 more__
- **2026-10-19** [`8a1c02efca`](https://github.com/vllm-project/vllm/commit/8a1c02efca) [#62208](https://github.com/vllm-project/vllm/pull/62208)
  [Bugfix][DeepSeek V4.1] Inject Engram at pipeline stage entry (#62208)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_deepseek_v41_pipeline.py`, `vllm/models/deepseek_v41/nvidia/model.py`_
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

## Docs  (15 commits)

- **2026-10-26** [`74340c7300`](https://github.com/vllm-project/vllm/commit/74340c7300) [#63036](https://github.com/vllm-project/vllm/pull/63036)
  [docs] correct NIXL hybrid SSM heterogeneous TP support (#63036)
  _Files: `docs/features/nixl_connector_compatibility.md`_
- **2026-10-26** [`256d8b40d0`](https://github.com/vllm-project/vllm/commit/256d8b40d0) [#62885](https://github.com/vllm-project/vllm/pull/62885)
  [Doc] Kolibri 1 reasoning and tool-call parsing via HF response template (#62885)
  _Files: `docs/features/reasoning_outputs.md`, `docs/features/tool_calling.md`_
- **2026-10-25** [`b3466364b6`](https://github.com/vllm-project/vllm/commit/b3466364b6) [#63451](https://github.com/vllm-project/vllm/pull/63451)
  [Bugfix] Release cached cuBLAS workspaces after daemon warmup (#63451)
  _Files: `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`_
- **2026-10-25** [`2f1041e8dd`](https://github.com/vllm-project/vllm/commit/2f1041e8dd) [#63552](https://github.com/vllm-project/vllm/pull/63552)
  [Doc] Kimi-K3: InferenceX AgentX lanes as tuned presets; DCP only in presets (#63552)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-25** [`e4a5b55373`](https://github.com/vllm-project/vllm/commit/e4a5b55373) [#63534](https://github.com/vllm-project/vllm/pull/63534)
  [Doc] MiniMax-M3: InferenceX AgentX lanes as tuned presets (#63534)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`_
- **2026-10-24** [`4e59165715`](https://github.com/vllm-project/vllm/commit/4e59165715) [#63423](https://github.com/vllm-project/vllm/pull/63423)
  [Deprecation] Deprecate LM Format Enforcer structured outputs backend (#63423)
  _Files: `docs/features/structured_outputs.md`, `vllm/config/structured_outputs.py`_
- **2026-10-23** [`89faadf7a6`](https://github.com/vllm-project/vllm/commit/89faadf7a6) [#63370](https://github.com/vllm-project/vllm/pull/63370)
  [MRV2] Remove stale experimental README (#63370)
  _Files: `vllm/v1/worker/gpu/README.md`_
- **2026-10-21** [`9db0da83f5`](https://github.com/vllm-project/vllm/commit/9db0da83f5) [#62601](https://github.com/vllm-project/vllm/pull/62601)
  [Doc] Raise the bar for agent-written tests (#62601)
  _Files: `.agents/skills/pr-checklist/SKILL.md`, `AGENTS.md`, `tests/AGENTS.md`_
- **2026-10-21** [`e410466a2a`](https://github.com/vllm-project/vllm/commit/e410466a2a) [#62599](https://github.com/vllm-project/vllm/pull/62599)
  [Doc] Require docs for user-visible changes (#62599)
  _Files: `.agents/skills/pr-checklist/SKILL.md`, `AGENTS.md`, `docs/contributing/README.md`_
- **2026-10-20** [`56e67b46a3`](https://github.com/vllm-project/vllm/commit/56e67b46a3) [#62761](https://github.com/vllm-project/vllm/pull/62761)
  [Doc] Sync Kimi-K3 GB200 AgentX profiles with InferenceX #4322 (#62761)
  _Files: `recipes/models/moonshotai/Kimi-K3.yaml`_
- **2026-10-20** [`70a609ac40`](https://github.com/vllm-project/vllm/commit/70a609ac40) [#62543](https://github.com/vllm-project/vllm/pull/62543)
  [Doc] Document MiniMax-M3 GB200 Dynamo AgentX profile (#62543)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`_
- **2026-10-20** [`76c9e23ce7`](https://github.com/vllm-project/vllm/commit/76c9e23ce7) [#62709](https://github.com/vllm-project/vllm/pull/62709)
  [Docs] Use release tags for documentation source links (#62709)
  _Files: `docs/mkdocs/hooks/url_schemes.py`_
- **2026-10-19** [`5f446bfb84`](https://github.com/vllm-project/vllm/commit/5f446bfb84) [#58219](https://github.com/vllm-project/vllm/pull/58219)
  docs: explain parser boundary tokens in custom grammars (#58219)
  _Files: `docs/features/structured_outputs.md`, `docs/features/tool_calling.md`_
- **2026-10-19** [`2aa5080fa0`](https://github.com/vllm-project/vllm/commit/2aa5080fa0) [#60994](https://github.com/vllm-project/vllm/pull/60994)
  [Bugfix][Weight Cache] Include RoPE parameters in IPC cache key (#60994)
  _Files: `docs/features/preload.md`, `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py` _+1 more__
- **2026-10-19** [`3497d72a72`](https://github.com/vllm-project/vllm/commit/3497d72a72) [#62207](https://github.com/vllm-project/vllm/pull/62207)
  [Frontend] Add Muse Spark Open reasoning and tool parsers (#62207)
  _Files: `docs/features/tool_calling.md`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/unified.rs`, `rust/src/parser/src/unified/mod.rs` _+10 more__

## Quantization  (14 commits)

- **2026-10-26** [`d26d5db01f`](https://github.com/vllm-project/vllm/commit/d26d5db01f) [#63658](https://github.com/vllm-project/vllm/pull/63658)
  [XPU][CI] Enable test_fusion_rmsnorm_quant on XPU (#63658)
  _Files: `tests/compile/passes/test_fusion.py`_
- **2026-10-23** [`1815ffd948`](https://github.com/vllm-project/vllm/commit/1815ffd948) [#63407](https://github.com/vllm-project/vllm/pull/63407)
  [Doc] MiniMax-M3: update the B300 NVFP4 InferenceX AgentX profile (#63407)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`_
- **2026-10-23** [`c7c11188a0`](https://github.com/vllm-project/vllm/commit/c7c11188a0) [#63395](https://github.com/vllm-project/vllm/pull/63395)
  [Doc] MiniMax-M3: document the B300 NVFP4 InferenceX AgentX aggregated profile (#63395)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`_
- **2026-10-23** [`8b21328cb8`](https://github.com/vllm-project/vllm/commit/8b21328cb8) [#63391](https://github.com/vllm-project/vllm/pull/63391)
  [Doc] MiniMax-M3: document the H200 MXFP8 InferenceX AgentX aggregated profile (#63391)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`_
- **2026-10-23** [`ecd1e12553`](https://github.com/vllm-project/vllm/commit/ecd1e12553) [#63163](https://github.com/vllm-project/vllm/pull/63163)
  [Recipe] MiniMax-M3: add B200 NVFP4 AgentX aggregated profile (#63163)
  _Files: `recipes/models/MiniMaxAI/MiniMax-M3.yaml`_
- **2026-10-23** [`1839702eec`](https://github.com/vllm-project/vllm/commit/1839702eec) [#63281](https://github.com/vllm-project/vllm/pull/63281)
  [XPU][UT] Use W8A8 FP8 linear kernel instead of W8A16 on XPU in modernbert_fp8 unit test (#63281)
  _Files: `tests/models/language/pooling_mteb_test/test_modernbert_fp8.py`_
- **2026-10-22** [`b4411f58a9`](https://github.com/vllm-project/vllm/commit/b4411f58a9) [#62816](https://github.com/vllm-project/vllm/pull/62816)
  [Quantization] Bump humming-kernels to 0.1.18 and remove DeviceInfo workaround (#62816)
  _Files: `requirements/cuda.txt`, `vllm/utils/humming.py`_
- **2026-10-22** [`2f8e0de8f6`](https://github.com/vllm-project/vllm/commit/2f8e0de8f6) [#62451](https://github.com/vllm-project/vllm/pull/62451)
  [Doc][Recipe] Use renamed Mamba prefix flag in Nemotron-3.5-Super-VL FP8 (#62451)
  _Files: `recipes/models/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4.yaml`_
- **2026-10-22** [`876d5da831`](https://github.com/vllm-project/vllm/commit/876d5da831) [#61786](https://github.com/vllm-project/vllm/pull/61786)
  [Bugfix][EPLB] Move 1-byte expert tensors as uint8 views (#61786)
  _Files: `tests/distributed/test_eplb_execute.py`, `vllm/model_executor/models/interfaces.py`_
- **2026-10-21** [`9353ea5fda`](https://github.com/vllm-project/vllm/commit/9353ea5fda) [#61354](https://github.com/vllm-project/vllm/pull/61354)
  [Bugfix][XPU] Fix INC ARK weight loading for small TP shards (#61354)
  _Files: `vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_linear.py`_
- **2026-10-20** [`79218659a6`](https://github.com/vllm-project/vllm/commit/79218659a6) [#58184](https://github.com/vllm-project/vllm/pull/58184)
  [Bugfix][Model] MiMo-V2: skip fused fp8 qkv_proj tensors for layers the model does not have (#58184)
  _Files: `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`_
- **2026-10-20** [`3b51898280`](https://github.com/vllm-project/vllm/commit/3b51898280) [#59053](https://github.com/vllm-project/vllm/pull/59053)
  [Feature][Quantization] Gather MiMo fused-QKV FP8 rows exactly by default (#59053)
  _Files: `tests/models/quantization/test_mimo_v2_qkv_shard.py`, `vllm/model_executor/models/mimo_v2.py`_
- **2026-10-19** [`bbf59fbad4`](https://github.com/vllm-project/vllm/commit/bbf59fbad4) [#55537](https://github.com/vllm-project/vllm/pull/55537)
  [Kernel] Reject unsupported layouts in CUTLASS 3.x scaled_mm (#55537)
  _Files: `.buildkite/test_areas/kernels.yaml`, `csrc/quantization/w8a8/cutlass/scaled_mm_entry.cu`, `tests/kernels/quantization/test_cutlass_scaled_mm.py`_
- **2026-10-19** [`42472f9903`](https://github.com/vllm-project/vllm/commit/42472f9903) [#61965](https://github.com/vllm-project/vllm/pull/61965)
  [CPU][Bugfix] Flatten >2-D activations in the AMX int8 W8A8 linear path (#61965)
  _Files: `tests/kernels/quantization/test_scaled_mm_kernel_selection.py`, `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`_

## Perf / Benchmark  (9 commits)

- **2026-10-25** [`237d2ffd08`](https://github.com/vllm-project/vllm/commit/237d2ffd08) [#63613](https://github.com/vllm-project/vllm/pull/63613)
  [Benchmark] Add PCP support to vllm bench forward (#63613)
  _Files: `docs/cli/README.md`, `tests/benchmarks/test_forward_cli.py`, `vllm/benchmarks/forward/capture.py`, `vllm/benchmarks/forward/routing.py`_
- **2026-10-25** [`fc2b6ab45e`](https://github.com/vllm-project/vllm/commit/fc2b6ab45e) [#62698](https://github.com/vllm-project/vllm/pull/62698)
  [Perf][MRV2] Parallelize staged writes across 1024-element chunks (#62698)
  _Files: `tests/v1/worker/test_gpu_block_table.py`, `vllm/v1/worker/gpu/buffer_utils.py`_
- **2026-10-23** [`4c12fce79d`](https://github.com/vllm-project/vllm/commit/4c12fce79d) [#62654](https://github.com/vllm-project/vllm/pull/62654)
  [Perf] Watermarking: skip greedy-fallback argmax when no request is greedy (#62654)
  _Files: `tests/watermarking/test_watermarking.py`, `vllm/v1/watermarking/gpu_sampler.py`_
- **2026-10-22** [`271941177d`](https://github.com/vllm-project/vllm/commit/271941177d) [#62940](https://github.com/vllm-project/vllm/pull/62940)
  [Perf] Bypass DispatchPooler grouping for homogeneous tasks (#62940)
  _Files: `tests/model_executor/layers/test_pooler_methods.py`, `vllm/model_executor/layers/pooler/special.py`_
- **2026-10-22** [`3e44c0db26`](https://github.com/vllm-project/vllm/commit/3e44c0db26) [#60774](https://github.com/vllm-project/vllm/pull/60774)
  [Bugfix][Benchmark] Support boolean sweep plot filters (#60774)
  _Files: `tests/benchmarks/test_plot_filters.py`, `vllm/benchmarks/sweep/plot.py`_
- **2026-10-21** [`57d9bf768e`](https://github.com/vllm-project/vllm/commit/57d9bf768e) [#62745](https://github.com/vllm-project/vllm/pull/62745)
  [Perf][Kernel] mHC TileLang: skip Sinkhorn on non-finite padding rows; single-pass fused post+pre for <=4 tokens (#62745)
  _Files: `tests/kernels/mhc/test_mhc_jit_warmup.py`, `vllm/model_executor/kernels/mhc/tilelang_kernels.py`_
- **2026-10-21** [`fc84883989`](https://github.com/vllm-project/vllm/commit/fc84883989) [#60284](https://github.com/vllm-project/vllm/pull/60284)
  [Misc] Say when to use the IMA, microbenchmark, and Triton skills (#60284)
  _Files: `.agents/skills/debug-ima/SKILL.md`, `.agents/skills/kernel-microbenchmark/SKILL.md`, `.agents/skills/triton-kernel-writing/SKILL.md`_
- **2026-10-20** [`e4a676cdc2`](https://github.com/vllm-project/vllm/commit/e4a676cdc2) [#61497](https://github.com/vllm-project/vllm/pull/61497)
  [Perf][Mamba] Reduce host overhead in the Mamba2 Triton SSD prefill path (#61497)
  _Files: `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/model_executor/layers/mamba/ops/ssd_bmm.py`, `vllm/model_executor/layers/mamba/ops/ssd_chunk_scan.py`, `vllm/model_executor/layers/mamba/ops/ssd_chunk_state.py` _+4 more__
- **2026-10-19** [`dcf8158cdc`](https://github.com/vllm-project/vllm/commit/dcf8158cdc) [#62341](https://github.com/vllm-project/vllm/pull/62341)
  [Bugfix][Benchmark] Don't count content-free chunks as streamed outputs in chat (#62341)
  _Files: `benchmarks/backend_request_func.py`, `tests/benchmarks/test_endpoint_request_func_timing.py`, `vllm/benchmarks/lib/endpoint_request_func.py`_

## Compilation / CUDA Graph  (5 commits)

- **2026-10-23** [`fbe133ff30`](https://github.com/vllm-project/vllm/commit/fbe133ff30) [#61509](https://github.com/vllm-project/vllm/pull/61509)
  [Bugfix][MRV2] Don't count adaptive verification profiling cache as CUDA graph memory (#61509)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-10-21** [`0eea5aca84`](https://github.com/vllm-project/vllm/commit/0eea5aca84) [#59941](https://github.com/vllm-project/vllm/pull/59941)
  [Bugfix] Resolve eager_break_during_capture at call time, not import time (#59941)
  _Files: `tests/v1/cudagraph/test_breakable_cudagraph.py`, `vllm/compilation/breakable_cudagraph.py`_
- **2026-10-21** [`d29702fd75`](https://github.com/vllm-project/vllm/commit/d29702fd75) [#60318](https://github.com/vllm-project/vllm/pull/60318)
  [Bugfix] Don't Eliminate Clones for graph I/O Aliases (#60318)
  _Files: `tests/compile/fullgraph/test_clone_elimination.py`, `tests/compile/passes/ir/test_clone_cleanup.py`, `vllm/compilation/passes/ir/clone_elimination.py`_
- **2026-10-19** [`a3cee21d0b`](https://github.com/vllm-project/vllm/commit/a3cee21d0b) [#61465](https://github.com/vllm-project/vllm/pull/61465)
  [Bugfix] Require cudnn-frontend >=1.31.0: cuDNN could replay an unloaded kernel from a CUDA graph (#61465)
  _Files: `requirements/cuda.txt`_
- **2026-10-19** [`3788269c98`](https://github.com/vllm-project/vllm/commit/3788269c98) [#62375](https://github.com/vllm-project/vllm/pull/62375)
  [Benchmark][XPU] Support XPU in forward bench graph capture/profiling (#62375)
  _Files: `vllm/benchmarks/forward/capture.py`, `vllm/benchmarks/forward/profile.py`, `vllm/profiler/wrapper.py`_

---
_Generated 2026-10-26 15:15 UTC_