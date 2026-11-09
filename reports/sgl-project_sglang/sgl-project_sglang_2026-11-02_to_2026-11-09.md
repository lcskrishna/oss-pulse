# sgl-project/sglang — Weekly Change Report
**Period:** 2026-11-02 → 2026-11-09  |  **Total commits:** 602

## ✨ New Features This Week

- **2026-11-09** [#49020](https://github.com/sgl-project/sglang/pull/49020) — [CI] diffusion: Add H100 computable runner baselines for loading and E2E (#49020)
- **2026-11-09** [#49318](https://github.com/sgl-project/sglang/pull/49318) — [Test] npu/glm5.3: Add 2P2D 32P PD-separation perf case (#49318)
- **2026-11-09** [#48786](https://github.com/sgl-project/sglang/pull/48786) — [Feat] HiCache: add tma copy kernel for unified layout (#48786)
- **2026-11-09** [#48014](https://github.com/sgl-project/sglang/pull/48014) — [Feat] attention: Serve several window sub-pools per runner in the Triton backend (#48014)
- **2026-11-09** [#48011](https://github.com/sgl-project/sglang/pull/48011) — [Refactor] mem_cache: Add a layout planner and request demand for the unified chain (#48011)
- **2026-11-09** [#45727](https://github.com/sgl-project/sglang/pull/45727) — [Feat] hisparse: Support shared KV sources in HiSparse MLA swap kernels (#45727)
- **2026-11-09** [#27267](https://github.com/sgl-project/sglang/pull/27267) — [Feat] mem_cache: Add hugepage preflight and allocation modes for host pools (#27267)
- **2026-11-09** [#48662](https://github.com/sgl-project/sglang/pull/48662) — [Feat] cli: Export Cookbook commands as per-checkpoint JSON files (#48662)
- **2026-11-09** [#48364](https://github.com/sgl-project/sglang/pull/48364) — [Feat] [CPU] model: Support Intern-S2-Mobius models on CPU (#48364)
- **2026-11-09** [#48583](https://github.com/sgl-project/sglang/pull/48583) — [Feat] [Intel] xpu_kernel: update sglang-kernel-xpu to 0.6.0 (#48583)
- _…and 125 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-11-09** [`388d03b775`](https://github.com/sgl-project/sglang/commit/388d03b775) [#48014](https://github.com/sgl-project/sglang/pull/48014) — [Feat] attention: Serve several window sub-pools per runner in the Triton backend (#48014)
- **2026-11-09** [`c89cedec26`](https://github.com/sgl-project/sglang/commit/c89cedec26) [#48013](https://github.com/sgl-project/sglang/pull/48013) — [Refactor] mem_cache: Give each window sub-pool its own host pool, PD entry and metrics (#48013)
- **2026-11-09** [`f01950a82a`](https://github.com/sgl-project/sglang/commit/f01950a82a) [#49053](https://github.com/sgl-project/sglang/pull/49053) — [CI] [AMD] spur: Schedule stage-b-test-1-gpu-small-amd-mi35x on the Spur runners (#49053)
- **2026-11-09** [`c81230bffe`](https://github.com/sgl-project/sglang/commit/c81230bffe) [#46517](https://github.com/sgl-project/sglang/pull/46517) — [Fix] srt: Promptly abort running requests on client disconnect (#46517) (#46586)
- **2026-11-09** [`6ec5451954`](https://github.com/sgl-project/sglang/commit/6ec5451954) [#48405](https://github.com/sgl-project/sglang/pull/48405) — [Perf] [AMD] kvcache: Fuse fp8 quantization into the vectorized_5d KV-cache write (#48405)
- **2026-11-09** [`d18e36cb82`](https://github.com/sgl-project/sglang/commit/d18e36cb82) [#47899](https://github.com/sgl-project/sglang/pull/47899) — [Fix] qwen3.5: Keep CPU-offloaded GDN input projections separate (#47899)
- **2026-11-09** [`fd978b6cec`](https://github.com/sgl-project/sglang/commit/fd978b6cec) [#49003](https://github.com/sgl-project/sglang/pull/49003) — [Feat] [AMD] custom-all-reduce: Run carv2 across gfx1250 UALink nodes (#49003)
- **2026-11-09** [`af72557571`](https://github.com/sgl-project/sglang/commit/af72557571) [#48536](https://github.com/sgl-project/sglang/pull/48536) — [Perf] [AMD] quantization: Fuse SiLU-and-mul with the dynamic per-tensor fp8 quant of dense MLPs on gfx95 (#48536)
- **2026-11-09** [`4634c2495c`](https://github.com/sgl-project/sglang/commit/4634c2495c) [#48406](https://github.com/sgl-project/sglang/pull/48406) — [Perf] [AMD] qwen3: Let the fused QK-norm + RoPE + KV write serve the vectorized_5d layout (#48406)
- **2026-11-08** [`3e38c5b77a`](https://github.com/sgl-project/sglang/commit/3e38c5b77a) [#46694](https://github.com/sgl-project/sglang/pull/46694) — [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache (#46694)
- **2026-11-08** [`917c27f1a4`](https://github.com/sgl-project/sglang/commit/917c27f1a4) [#46693](https://github.com/sgl-project/sglang/pull/46693) — [Feat] [AMD] minimax: Support MiniMax-M3.1-Flash on MI350X / MI355X (gfx950) (#46693)
- **2026-11-08** [`33db33f2e3`](https://github.com/sgl-project/sglang/commit/33db33f2e3) [#47908](https://github.com/sgl-project/sglang/pull/47908) — [Fix] [AMD] quark: Match aiter's column-major scale layout in the MXFP4 quant fake (#47908)
- **2026-11-08** [`db680c5b80`](https://github.com/sgl-project/sglang/commit/db680c5b80) [#48043](https://github.com/sgl-project/sglang/pull/48043) — [Perf] [AMD] qwen3: Fuse the 1x128 FP8 input quant into RMSNorm and SiLU-and-mul for block-FP8 linears on gfx950 (#48043)
- **2026-11-08** [`1668d4b993`](https://github.com/sgl-project/sglang/commit/1668d4b993) [#48434](https://github.com/sgl-project/sglang/pull/48434) — [Fix] [AMD] aiter: Quantize q with its own scale in the fp8 prefills over a gathered cache (#48434)
- **2026-11-07** [`9d547e19ff`](https://github.com/sgl-project/sglang/commit/9d547e19ff) [#47862](https://github.com/sgl-project/sglang/pull/47862) — [Feat] [AMD] aiter: One folder of in-tree aiter tuned rows for every model (#47862)
- **2026-11-07** [`ba48fc1a9e`](https://github.com/sgl-project/sglang/commit/ba48fc1a9e) [#49001](https://github.com/sgl-project/sglang/pull/49001) — [Feat] [AMD] custom-all-reduce: Run carv2 on MI450 with FABRIC handles and a gfx1250 table (#49001)
- **2026-11-07** [`391f4e6f17`](https://github.com/sgl-project/sglang/commit/391f4e6f17) [#49087](https://github.com/sgl-project/sglang/pull/49087) — [Doc] [AMD] cookbook: Update Muse Spark Open MI355X AgentX recipe to the 1106 image (#49087)
- **2026-11-07** [`bf1aa1ab4d`](https://github.com/sgl-project/sglang/commit/bf1aa1ab4d) [#48438](https://github.com/sgl-project/sglang/pull/48438) — [Test] [AMD] aiter: Run the HD128 ASM prefill test on gfx950 with a routed pool (#48438)
- **2026-11-07** [`754185aab5`](https://github.com/sgl-project/sglang/commit/754185aab5) [#48830](https://github.com/sgl-project/sglang/pull/48830) — [CI] [AMD] spur: Run 1-, 2- and 4-GPU suites on part of a node (#48830)
- **2026-11-07** [`3048de1871`](https://github.com/sgl-project/sglang/commit/3048de1871) [#48044](https://github.com/sgl-project/sglang/pull/48044) — [Perf] [AMD] qwen3-next: Fuse the full-attention Q/K GemmaRMSNorm and partial RoPE into one Triton kernel on gfx950 (#48044)
- **2026-11-07** [`6220d68645`](https://github.com/sgl-project/sglang/commit/6220d68645) [#48966](https://github.com/sgl-project/sglang/pull/48966) — [CI] [AMD] hc_mix: Skip the FlyDSL hc_mix dispatch tests when AITER lacks the kernel (#48966)
- **2026-11-07** [`24aa7d00b6`](https://github.com/sgl-project/sglang/commit/24aa7d00b6) [#48978](https://github.com/sgl-project/sglang/pull/48978) — [CI] [AMD] jit: Use the platform full warp mask in the DSA indexer RoPE helpers (#48978)
- **2026-11-07** [`9a57115efc`](https://github.com/sgl-project/sglang/commit/9a57115efc) [#49022](https://github.com/sgl-project/sglang/pull/49022) — [Doc] [AMD] cookbook: Match the Kimi-K3.1-Pro MI35x single-node cells to the current recipe (#49022)
- **2026-11-07** [`a240184279`](https://github.com/sgl-project/sglang/commit/a240184279) [#48479](https://github.com/sgl-project/sglang/pull/48479) — [CI] [AMD] nightly: Add Kimi-K3.1-Pro nightly test (#48479)
- **2026-11-07** [`92b1d7be5f`](https://github.com/sgl-project/sglang/commit/92b1d7be5f) [#47695](https://github.com/sgl-project/sglang/pull/47695) — [Feat] [AMD] quark: Quark int4 W4A16 on ROCm, and gfx1151 kernels for Strix Halo decode and prefill (#47695)
- **2026-11-06** [`e45e1d0c56`](https://github.com/sgl-project/sglang/commit/e45e1d0c56) [#47964](https://github.com/sgl-project/sglang/pull/47964) — [Feat] [AMD] custom-all-reduce: Run the JIT custom all-reduce v2 on ROCm (#47964)
- **2026-11-06** [`bda1cf5295`](https://github.com/sgl-project/sglang/commit/bda1cf5295) [#48699](https://github.com/sgl-project/sglang/pull/48699) — [CI] [AMD] disaggregation: Send aux data over TCP in the PP disaggregation test (#48699)
- **2026-11-06** [`80eedfaf2f`](https://github.com/sgl-project/sglang/commit/80eedfaf2f) [#48829](https://github.com/sgl-project/sglang/pull/48829) — [Chore] deps: Drop flash-attn-4 from default dependencies (#48829)
- **2026-11-06** [`c117e31f9f`](https://github.com/sgl-project/sglang/commit/c117e31f9f) [#46662](https://github.com/sgl-project/sglang/pull/46662) — [Doc] [AMD] GLM-5.3: Enable MTP on MI355X and add the agentic recipe with the AMD monokernel (#46662)
- **2026-11-06** [`c843608d39`](https://github.com/sgl-project/sglang/commit/c843608d39) [#48726](https://github.com/sgl-project/sglang/pull/48726) — [CI] [AMD] miles: Skip MI30x FP8 and DeepSeek-V4 tests that cannot run on gfx942 (#48726)
- **2026-11-06** [`c9431eda6f`](https://github.com/sgl-project/sglang/commit/c9431eda6f) [#48692](https://github.com/sgl-project/sglang/pull/48692) — [CI] [AMD] spur: Take HF_TOKEN from the runner environment (#48692)
- **2026-11-06** [`858073e4f6`](https://github.com/sgl-project/sglang/commit/858073e4f6) [#48722](https://github.com/sgl-project/sglang/pull/48722) — [CI] [AMD] nightly-disagg: Install the checkout's runtime deps over the image (#48722)
- **2026-11-05** [`ad11717f3b`](https://github.com/sgl-project/sglang/commit/ad11717f3b) [#48737](https://github.com/sgl-project/sglang/pull/48737) — [Chore] ci: Cut deprecation warnings and TBO debug logs from CI output (#48737)
- **2026-11-05** [`3fa242f27c`](https://github.com/sgl-project/sglang/commit/3fa242f27c) [#44538](https://github.com/sgl-project/sglang/pull/44538) — [CI] [AMD] spur: Run AMD CI suites on MI35x nodes scheduled through Spur (#44538)
- **2026-11-05** [`89b2641381`](https://github.com/sgl-project/sglang/commit/89b2641381) [#46928](https://github.com/sgl-project/sglang/pull/46928) — [Fix] [AMD] aiter: Fix garbage decode output with unified attention at page size 1 under CUDA graph (#46928)
- **2026-11-05** [`732d34b93c`](https://github.com/sgl-project/sglang/commit/732d34b93c) [#48573](https://github.com/sgl-project/sglang/pull/48573) — [Chore] [AMD] aiter: promote gfx1250 pin to 07ff5f318 (#48573)
- **2026-11-05** [`fc7cd5978b`](https://github.com/sgl-project/sglang/commit/fc7cd5978b) [#47940](https://github.com/sgl-project/sglang/pull/47940) — [Chore] [AMD] rccl: pin rccl to d2e0de35 (#47940)
- **2026-11-05** [`729d11854b`](https://github.com/sgl-project/sglang/commit/729d11854b) [#44435](https://github.com/sgl-project/sglang/pull/44435) — [Feat] [NPU] scheduler: align cross-request ViT batching with CUDA and fix NPU graph buffer ownership (#44435)
- **2026-11-05** [`82554dd0e9`](https://github.com/sgl-project/sglang/commit/82554dd0e9) [#45202](https://github.com/sgl-project/sglang/pull/45202) — [Perf] [AMD] Kimi-K3: prepare the attention interface for mono fusion (#45202)
- **2026-11-05** [`3ead93f76d`](https://github.com/sgl-project/sglang/commit/3ead93f76d) [#45601](https://github.com/sgl-project/sglang/pull/45601) — [Perf] [AMD] deterministic: Allow AITER prefill attention on gfx950 (#45601)
- **2026-11-05** [`0fd3515d5f`](https://github.com/sgl-project/sglang/commit/0fd3515d5f) [#48485](https://github.com/sgl-project/sglang/pull/48485) — [Fix] [AMD] mooncake: Bump Mooncake to pick up the HIP IPC sub-allocation fix (#48485)
- **2026-11-05** [`7fb6ff4736`](https://github.com/sgl-project/sglang/commit/7fb6ff4736) [#48535](https://github.com/sgl-project/sglang/pull/48535) — [CI] lint: Import ForwardMode from its defining module in the KV translate test (#48535)
- **2026-11-05** [`2cedfafd30`](https://github.com/sgl-project/sglang/commit/2cedfafd30) [#44459](https://github.com/sgl-project/sglang/pull/44459) — [Perf] [AMD] mla: Fuse RoPE, concat and KV-cache write for MLA decode on gfx1250 (#44459)
- **2026-11-05** [`45886872fd`](https://github.com/sgl-project/sglang/commit/45886872fd) [#48134](https://github.com/sgl-project/sglang/pull/48134) — [CI] [AMD] ci: Follow #47619 on AMD and fix two never-run registrations (#48134)
- **2026-11-05** [`bf40ca98f4`](https://github.com/sgl-project/sglang/commit/bf40ca98f4) [#42198](https://github.com/sgl-project/sglang/pull/42198) — [Perf] [AMD] custom-all-reduce: Select the fused AR+RMSNorm 1-stage kernel by token count and read volume (#42198)
- **2026-11-05** [`a9d3bb7ddd`](https://github.com/sgl-project/sglang/commit/a9d3bb7ddd) [#47632](https://github.com/sgl-project/sglang/pull/47632) — [Perf] [AMD] attention: Forward decode graph variants through wrapper backends (#47632)
- **2026-11-05** [`03d7a10dbc`](https://github.com/sgl-project/sglang/commit/03d7a10dbc) [#34212](https://github.com/sgl-project/sglang/pull/34212) — [Fix] [AMD] DSP: skip unused QuickAllReduce allocation for DCP groups (#34212)
- **2026-11-04** [`c67efab427`](https://github.com/sgl-project/sglang/commit/c67efab427) [#48432](https://github.com/sgl-project/sglang/pull/48432) — [Doc] [AMD] cookbook: Qwen3.8-Flash-Next MI355X, add the HiCache commands for concurrency 24-80 (#48432)
- **2026-11-04** [`61a3c7f2a4`](https://github.com/sgl-project/sglang/commit/61a3c7f2a4) [#48415](https://github.com/sgl-project/sglang/pull/48415) — [Feat] model: Add basic Kimi-K3.1 support (NV, AMD) (#48415)
- **2026-11-04** [`387843d321`](https://github.com/sgl-project/sglang/commit/387843d321) [#48429](https://github.com/sgl-project/sglang/pull/48429) — [Doc] cookbook: Run the Kimi-K3.1-Pro MI35x PD Docker commands on the host network with RDMA (#48429)
- **2026-11-04** [`8884b4b421`](https://github.com/sgl-project/sglang/commit/8884b4b421) [#48413](https://github.com/sgl-project/sglang/pull/48413) — [Doc] cookbook: Add Kimi-K3.1-Pro deployment recipes (#48413)
- **2026-11-04** [`82602c0987`](https://github.com/sgl-project/sglang/commit/82602c0987) [#44503](https://github.com/sgl-project/sglang/pull/44503) — [Refactor] sparse-mla: Expose arithmetic and DSA metadata hooks (#44503)
- **2026-11-04** [`27aedf7f93`](https://github.com/sgl-project/sglang/commit/27aedf7f93) [#47822](https://github.com/sgl-project/sglang/pull/47822) — [Perf] [AMD] aiter: Skip q.contiguous() in unified extend when the per-token layout is dense (#47822)
- **2026-11-04** [`045e0e2e2d`](https://github.com/sgl-project/sglang/commit/045e0e2e2d) [#48323](https://github.com/sgl-project/sglang/pull/48323) — [CI] [AMD] miles: Skip MI30x tests whose kernels exceed gfx942 LDS (#48323)
- **2026-11-04** [`50ae3312c2`](https://github.com/sgl-project/sglang/commit/50ae3312c2) [#48067](https://github.com/sgl-project/sglang/pull/48067) — [CI] [AMD] miles: Pass CI and the SGLang source path to nightly suites (#48067)
- **2026-11-04** [`f0eff990d6`](https://github.com/sgl-project/sglang/commit/f0eff990d6) [#48265](https://github.com/sgl-project/sglang/pull/48265) — [CI] [AMD] miles: Split the MI30x 4-GPU nightly into two jobs (#48265)
- **2026-11-03** [`76b4c91360`](https://github.com/sgl-project/sglang/commit/76b4c91360) [#48229](https://github.com/sgl-project/sglang/pull/48229) — [Perf] dsv4: Expand the low-ratio indexer page table in one Triton kernel (#48229)
- **2026-11-03** [`f7cdb8fa3f`](https://github.com/sgl-project/sglang/commit/f7cdb8fa3f) [#48131](https://github.com/sgl-project/sglang/pull/48131) — [CI] [AMD] nightly-disagg: Keep all MI355X CI settings in the repo and clean up after failed jobs (#48131)
- **2026-11-03** [`f433af22fc`](https://github.com/sgl-project/sglang/commit/f433af22fc) [#47283](https://github.com/sgl-project/sglang/pull/47283) — [Fix] [AMD] deepseek-v4: Respect AITER selection for Q-LoRA quantization (#47283)
- **2026-11-03** [`c97fe3559f`](https://github.com/sgl-project/sglang/commit/c97fe3559f) [#47064](https://github.com/sgl-project/sglang/pull/47064) — [Perf] [AMD] kda: Narrow the Kimi-K3 TP8 KDA recurrent tile for small batches on gfx950 (#47064)
- **2026-11-03** [`8d4e1ce4c7`](https://github.com/sgl-project/sglang/commit/8d4e1ce4c7) [#47969](https://github.com/sgl-project/sglang/pull/47969) — [CI] [AMD] pr-test: Run the MI35x 1-GPU stage after MI300 stage-b; move test_flydsl_v4nm_decode to nightly (#47969)
- **2026-11-03** [`a470d74cdb`](https://github.com/sgl-project/sglang/commit/a470d74cdb) [#46327](https://github.com/sgl-project/sglang/pull/46327) — [Perf] [AMD] unquant: Pad gfx115x linear and lm_head weight rows to avoid cache aliasing (#46327)
- **2026-11-03** [`f77064f635`](https://github.com/sgl-project/sglang/commit/f77064f635) [#47971](https://github.com/sgl-project/sglang/pull/47971) — [CI] [AMD] diffusion/minimax-h3: Skip the group-attend contract test on ROCm (#47971)
- **2026-11-03** [`11d687870f`](https://github.com/sgl-project/sglang/commit/11d687870f) [#46947](https://github.com/sgl-project/sglang/pull/46947) — [CI] [AMD] diffusion/flux3: Make exact-quality VAE convolutions deterministic on ROCm (#46947)
- **2026-11-03** [`cbfc0932e3`](https://github.com/sgl-project/sglang/commit/cbfc0932e3) [#44489](https://github.com/sgl-project/sglang/pull/44489) — [Perf] [AMD] deterministic: Allow AITER decode attention on gfx950 (#44489)
- **2026-11-03** [`a7d535454b`](https://github.com/sgl-project/sglang/commit/a7d535454b) [#48032](https://github.com/sgl-project/sglang/pull/48032) — [CI] [AMD] nightly-disagg: Run MI355X disagg nightly at 04:00 UTC (12:00 UTC+8) (#48032)
- **2026-11-03** [`797af7170f`](https://github.com/sgl-project/sglang/commit/797af7170f) [#43904](https://github.com/sgl-project/sglang/pull/43904) — [Refactor] scheduler: Check request ownership once at step launch (#43904)
- **2026-11-02** [`bde43d6c13`](https://github.com/sgl-project/sglang/commit/bde43d6c13) [#47504](https://github.com/sgl-project/sglang/pull/47504) — [CI] [AMD] mi355x: Clean up interrupted nightly jobs and reduce runner disk usage (#47504)
- **2026-11-02** [`33a1ba4a8a`](https://github.com/sgl-project/sglang/commit/33a1ba4a8a) [#44197](https://github.com/sgl-project/sglang/pull/44197) — [Fix] [AMD] mamba: Import the causal conv1d kernels for Mamba2 layers on ROCm (#44197)
- **2026-11-02** [`20f5f68729`](https://github.com/sgl-project/sglang/commit/20f5f68729) [#45443](https://github.com/sgl-project/sglang/pull/45443) — [Fix] [AMD] imports: Skip import-time device probes when no GPU is visible (#45443)
- **2026-11-02** [`251eb36da0`](https://github.com/sgl-project/sglang/commit/251eb36da0) [#47951](https://github.com/sgl-project/sglang/pull/47951) — [Doc] [AMD] cookbook: Qwen3.8-Flash-Next MI355X, add the monokernel command for concurrency 1-8 (#47951)
- **2026-11-02** [`16dd97df61`](https://github.com/sgl-project/sglang/commit/16dd97df61) [#46325](https://github.com/sgl-project/sglang/pull/46325) — [Perf] [AMD] deterministic: Use a fixed-order two-stage all-reduce for large inputs (#46325)
- **2026-11-02** [`a133231d31`](https://github.com/sgl-project/sglang/commit/a133231d31) [#47782](https://github.com/sgl-project/sglang/pull/47782) — [Refactor] kernels: Centralize GPU architecture queries in sglang.kernels.arch (#47782)
- **2026-11-02** [`3e88483288`](https://github.com/sgl-project/sglang/commit/3e88483288) [#47844](https://github.com/sgl-project/sglang/pull/47844) — [Doc] [AMD] cookbook: Verify MiniMax-M3.1-Flash High-Throughput on MI355X (#47844)
- **2026-11-02** [`7cad887d53`](https://github.com/sgl-project/sglang/commit/7cad887d53) [#42654](https://github.com/sgl-project/sglang/pull/42654) — [Perf] moe: Enable deferred finalize for NVFP4 on the routed TRT-LLM runner (#42654)
- **2026-11-02** [`f6127bf96e`](https://github.com/sgl-project/sglang/commit/f6127bf96e) [#41639](https://github.com/sgl-project/sglang/pull/41639) — [Feat] [AMD] moe: Add native GLM MXFP4 Triton Gluon backend (#41639)
- **2026-11-02** [`ae66493995`](https://github.com/sgl-project/sglang/commit/ae66493995) [#47030](https://github.com/sgl-project/sglang/pull/47030) — [Fix] [AMD] aiter: Use the layer's KV scales in the legacy target-verify attention (#47030)
- **2026-11-02** [`46e95bb9f9`](https://github.com/sgl-project/sglang/commit/46e95bb9f9) [#47042](https://github.com/sgl-project/sglang/pull/47042) — [Perf] [AMD] aiter: Bucket decode paged-attention partitions by sequence length (#47042)
- **2026-11-02** [`e0c7992d0d`](https://github.com/sgl-project/sglang/commit/e0c7992d0d) [#45332](https://github.com/sgl-project/sglang/pull/45332) — [Fix] [AMD] quark: Load MXFP4 MoE checkpoints on gfx95 and gfx1250 without SGLANG_USE_AITER (#45332)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#42752](https://github.com/sgl-project/sglang/issues/42752) | [CI] Flaky tests and CI infrastructure failures seen while babysitting | — | 2026-11-09 |
| [#49327](https://github.com/sgl-project/sglang/issues/49327) | [ROCm][AMD] DeepSeek-V4.1-Flash gfx950 / MI355X Performance Optimizati | — | 2026-11-09 |
| [#49336](https://github.com/sgl-project/sglang/issues/49336) | [Perf] SM90 decode regression v0.5.22 → v0.5.23: +33~45% per-step at c | — | 2026-11-09 |
| [#49324](https://github.com/sgl-project/sglang/issues/49324) | [ROCm][AMD] Qwen3.8-27B gfx950 / MI355X Performance Optimization (SGLa | — | 2026-11-09 |
| [#43699](https://github.com/sgl-project/sglang/issues/43699) | [Roadmap] Prefill-Decode Disaggregation Roadmap (2026 Q4) | PD Disaggregation | 2026-11-09 |
| [#49291](https://github.com/sgl-project/sglang/issues/49291) | [Bug] [NPU] DeepEP on Ascend A2 aborts mid decode-graph capture with a | — | 2026-11-09 |
| [#49209](https://github.com/sgl-project/sglang/issues/49209) | [Bug] sm_120 (RTX 50-series consumer Blackwell) cannot run any model o | — | 2026-11-09 |
| [#49274](https://github.com/sgl-project/sglang/issues/49274) | Silent deterministic output corruption: first token id 0 ("!") then [P | — | 2026-11-09 |
| [#48967](https://github.com/sgl-project/sglang/issues/48967) | [Bug] [AMD] decode attention: MLA-shaped Triton decode returns NaN / w | — | 2026-11-09 |
| [#48968](https://github.com/sgl-project/sglang/issues/48968) | [Bug] [AMD] --enable-deterministic-inference fails at startup on RDNA: | — | 2026-11-09 |
| [#49257](https://github.com/sgl-project/sglang/issues/49257) | [Feature][RFC] STANDALONE PD: homogeneous TP=2 handoff and rank-consis | — | 2026-11-09 |
| [#47562](https://github.com/sgl-project/sglang/issues/47562) | [AITER-Upgrade] PR readiness gfx1250 (MI45x) | — | 2026-11-09 |
| [#39499](https://github.com/sgl-project/sglang/issues/39499) | [Roadmap] SGLang dLLM Serving | — | 2026-11-09 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-11-09 |
| [#49250](https://github.com/sgl-project/sglang/issues/49250) | [Bug] ignore_eos requests finish early when their grammar terminates | — | 2026-11-09 |
| [#49230](https://github.com/sgl-project/sglang/issues/49230) | [Bug] Quark utility import writes optional AITER cache before quantiza | — | 2026-11-09 |
| [#43098](https://github.com/sgl-project/sglang/issues/43098) | Agentic Cache Scheduling System Roadmap (Q4) | — | 2026-11-09 |
| [#49198](https://github.com/sgl-project/sglang/issues/49198) | [Bug] Mixtral, Llama 4 and FP8 Qwen3-MoE: a router stored in FP8 is lo | — | 2026-11-08 |
| [#43313](https://github.com/sgl-project/sglang/issues/43313) | SGLang-Diffusion Roadmap (2026 Q4) | diffusion, roadmap | 2026-11-08 |
| [#32321](https://github.com/sgl-project/sglang/issues/32321) | [RFC] Apple Silicon serving redesign: Torch-owned SRT path with an exp | apple-silicon | 2026-11-07 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 150 |
| Prefill / Decode Disaggregation | 76 |
| MoE / Expert Parallel | 67 |
| Multimodal | 61 |
| KV Cache / Memory | 33 |
| Triton / Kernels | 27 |
| Other | 27 |
| Scheduler / Batching | 27 |
| Tensor / Data Parallel | 27 |
| Quantization | 26 |
| CI / Build | 20 |
| ROCm / AMD | 20 |
| Docs / Examples | 12 |
| Speculative Decoding | 11 |
| Models | 7 |
| Serving / API | 4 |
| Structured Output | 4 |
| LoRA | 3 |

## Attention / FlashInfer  (150 commits)

- **2026-11-09** [`704681229f`](https://github.com/sgl-project/sglang/commit/704681229f) [#47627](https://github.com/sgl-project/sglang/pull/47627)
  [Perf] [NVIDIA] dspark: Stage DSv4.1 long-context target verify metadata beside the draft (#47627)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/graph_variants.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `test/registered/unit/model_executor/runner/test_early_verify_metadata.py`_
- **2026-11-09** [`5325cfabd7`](https://github.com/sgl-project/sglang/commit/5325cfabd7) [#45727](https://github.com/sgl-project/sglang/pull/45727)
  [Feat] hisparse: Support shared KV sources in HiSparse MLA swap kernels (#45727)
  _Files: `python/sglang/kernels/jit/csrc/kvcacheio/hisparse.cuh`, `python/sglang/kernels/jit/csrc/kvcacheio/hisparse_spec.cuh`, `python/sglang/kernels/ops/kvcache/hisparse.py`, `test/registered/kernels/ops/kvcache/test_hisparse.py` _+1 more__
- **2026-11-09** [`2f42565fd2`](https://github.com/sgl-project/sglang/commit/2f42565fd2) [#49260](https://github.com/sgl-project/sglang/pull/49260)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main 0d7f94e7 (#49260)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx` _+4 more__
- **2026-11-09** [`48da6bd190`](https://github.com/sgl-project/sglang/commit/48da6bd190) [#27267](https://github.com/sgl-project/sglang/pull/27267)
  [Feat] mem_cache: Add hugepage preflight and allocation modes for host pools (#27267)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/hicache_auto_size.py`, `python/sglang/srt/mem_cache/host_memory.py` _+24 more__
- **2026-11-09** [`397254e902`](https://github.com/sgl-project/sglang/commit/397254e902) [#46577](https://github.com/sgl-project/sglang/pull/46577)
  [Fix] inkling: Skip KV stores for CUDA-graph padding tokens in the fused attn prologue (#46577)
  _Files: `python/sglang/kernels/jit/csrc/inkling/inkling_attn_prologue_fused.cuh`, `test/registered/kernels/ops/attention/test_inkling_attn_prologue_extend_pad.py`_
- **2026-11-09** [`4b2137e5dc`](https://github.com/sgl-project/sglang/commit/4b2137e5dc) [#46663](https://github.com/sgl-project/sglang/pull/46663)
  [Fix] gemma4: Fix Bolt E4B and Gemma4 prefill CUDA graphs (#46663)
  _Files: `python/sglang/srt/layers/radix_attention.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py` _+1 more__
- **2026-11-09** [`a1ae632658`](https://github.com/sgl-project/sglang/commit/a1ae632658) [#47493](https://github.com/sgl-project/sglang/pull/47493)
  [Fix] dp-attention: Trim MLP-sync pad rows from extend outputs before the draft extend (#47493)
  _Files: `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/model_executor/test_mlp_sync_pad_unpad.py`_
- **2026-11-09** [`6ec5451954`](https://github.com/sgl-project/sglang/commit/6ec5451954) [#48405](https://github.com/sgl-project/sglang/pull/48405)
  [Perf] [AMD] kvcache: Fuse fp8 quantization into the vectorized_5d KV-cache write (#48405)
  _Files: `python/sglang/kernels/ops/kvcache/shuffle_5d_cache.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/attention/test_aiter_fp8_kv_scales_paths.py` _+1 more__
- **2026-11-09** [`4fc912142f`](https://github.com/sgl-project/sglang/commit/4fc912142f) [#47658](https://github.com/sgl-project/sglang/pull/47658)
  [Perf] SM120: honour SGLANG_OPT_DEEPGEMM_HC_PRENORM for the DeepSeek-V4.1 compensated mhc projection (#47658)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_mhc.py`, `test/registered/kernels/ops/layernorm/test_mhc_bf16x3_sm120.py`, `test/registered/unit/models/test_deepseek_v4_platform_dispatch.py`_
- **2026-11-09** [`5e6995dd09`](https://github.com/sgl-project/sglang/commit/5e6995dd09) [#49182](https://github.com/sgl-project/sglang/pull/49182)
  [Fix] [NVIDIA] dsv4: Restore SM120/SM121 to the DeepGEMM indexer gates (#49182)
  _Files: `python/sglang/srt/layers/attention/dsv4/v41_indexer/__init__.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/full_topk.py`, `test/registered/unit/layers/test_dsv41_indexer_arch_gates.py`_
- **2026-11-09** [`c394281b4f`](https://github.com/sgl-project/sglang/commit/c394281b4f) [#48662](https://github.com/sgl-project/sglang/pull/48662)
  [Feat] cli: Export Cookbook commands as per-checkpoint JSON files (#48662)
  _Files: `.github/workflows/lint.yml`, `.pre-commit-config.yaml`, `docs/scripts/export_commands.mjs`, `docs/scripts/tests/cookbook-commands-snapshot.test.mjs` _+7 more__
- **2026-11-09** [`3e8d7c9e09`](https://github.com/sgl-project/sglang/commit/3e8d7c9e09) [#46214](https://github.com/sgl-project/sglang/pull/46214)
  [Fix] flashinfer: Apply the sliding window in ragged prefill for hybrid-SWA models (#46214)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`, `test/registered/kernels/ops/attention/test_flashinfer_window_verify.py`, `test/registered/unit/layers/attention/test_fused_draft_window_metadata.py`_
- **2026-11-09** [`e5d78e65a9`](https://github.com/sgl-project/sglang/commit/e5d78e65a9) [#49247](https://github.com/sgl-project/sglang/pull/49247)
  [Fix] [NVIDIA] dsv4: Import get_eager_max_batch_size from dp_attention in the mega backend (#49247)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_mega_backend.py`_
- **2026-11-09** [`5d78af0ca0`](https://github.com/sgl-project/sglang/commit/5d78af0ca0) [#31447](https://github.com/sgl-project/sglang/pull/31447)
  [Fix] Confidential-Computing: enable Flashinfer all-reduce fusion (#31447)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `test/registered/unit/layers/test_flashinfer_comm_fusion.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-11-09** [`480dcf4ec8`](https://github.com/sgl-project/sglang/commit/480dcf4ec8) [#46062](https://github.com/sgl-project/sglang/pull/46062)
  [Perf] [NVIDIA] deepseek-v4.1: Keep one zeroed MegaAttention packed-query buffer instead of zeroing it per layer (#46062)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_mega_backend.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/kernels/ops/attention/dsv4/test_mega_attention.py`_
- **2026-11-09** [`76dafba55a`](https://github.com/sgl-project/sglang/commit/76dafba55a) [#48879](https://github.com/sgl-project/sglang/pull/48879)
  [Doc] cookbook: Fix Qwen3.8-Flash-Next thinking-mode description (#48879)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`_
- **2026-11-09** [`e4bf2a2084`](https://github.com/sgl-project/sglang/commit/e4bf2a2084) [#46003](https://github.com/sgl-project/sglang/pull/46003)
  [Perf] dsv-v4.1: Score only candidate positions in indexer consumers (#46003)
  _Files: `python/sglang/kernels/ops/attention/dsv4/candidate_blocks.py`, `python/sglang/kernels/ops/attention/dsv4/candidate_scores.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/dense_blocks.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/scoring.py` _+1 more__
- **2026-11-09** [`656ac7b1d4`](https://github.com/sgl-project/sglang/commit/656ac7b1d4) [#47406](https://github.com/sgl-project/sglang/pull/47406)
  [Fix] deepseek-v4.1: Fix bounded replay with CP and DSpark (#47406)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`, `python/sglang/srt/models/deepseek_v4.py` _+2 more__
- **2026-11-09** [`0749a0cc72`](https://github.com/sgl-project/sglang/commit/0749a0cc72) [#48585](https://github.com/sgl-project/sglang/pull/48585)
  [Perf] gdn: reduce MIS output and QK preparation overhead (#48585)
  _Files: `python/sglang/kernels/ops/attention/fla/chunk.py`, `python/sglang/kernels/ops/attention/fla/chunk_o.py`, `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py` _+4 more__
- **2026-11-09** [`4668f37139`](https://github.com/sgl-project/sglang/commit/4668f37139) [#49088](https://github.com/sgl-project/sglang/pull/49088)
  [Perf] [NVIDIA] minimax-sparse: Run the decode indexer CP on Hopper at TP8 with attention DP2 (#49088)
  _Files: `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `test/registered/unit/layers/attention/test_minimax_indexer_cp_gate.py`_
- **2026-11-09** [`a1cb9e4d4e`](https://github.com/sgl-project/sglang/commit/a1cb9e4d4e) [#48211](https://github.com/sgl-project/sglang/pull/48211)
  [Fix] openai: do not render a null tool-level defer_loading (#48211)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `rust/sglang-processor/src/render/models/kimi_k3.rs`, `rust/sglang-processor/src/render/models/qwen38.rs`, `rust/sglang-processor/src/render/template.rs` _+6 more__
- **2026-11-08** [`033c03a9cd`](https://github.com/sgl-project/sglang/commit/033c03a9cd) [#49105](https://github.com/sgl-project/sglang/pull/49105)
  [Feat] kimi-k3.1: HiCache with DFLASH under decode context parallelism (#49105)
  _Files: `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `test/registered/unit/mem_cache/test_hicache_dcp_host_pool.py` _+1 more__
- **2026-11-08** [`5c10928f08`](https://github.com/sgl-project/sglang/commit/5c10928f08) [#46483](https://github.com/sgl-project/sglang/pull/46483)
  [Perf] [NPU] attention: Avoid CPU sequence length synchronization for Kimi K3 (#46483)
  _Files: `docs/docs/hardware-platforms/ascend-npus/reference/environment_variables.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py` _+10 more__
- **2026-11-08** [`d55caa2675`](https://github.com/sgl-project/sglang/commit/d55caa2675) [#49106](https://github.com/sgl-project/sglang/pull/49106)
  [Feat] kimi-k3.1: trtllm DSA backend under decode context parallelism (#49106)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`_
- **2026-11-08** [`3e38c5b77a`](https://github.com/sgl-project/sglang/commit/3e38c5b77a) [#46694](https://github.com/sgl-project/sglang/pull/46694)
  [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache (#46694)
  _Files: `python/sglang/kernels/ops/attention/minimax_sparse/decode/verify_topk_gfx950.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py` _+6 more__
- **2026-11-08** [`d1d317c64d`](https://github.com/sgl-project/sglang/commit/d1d317c64d) [#49019](https://github.com/sgl-project/sglang/pull/49019)
  [Refactor] scheduler: Commit a step's result only on the rows of requests still in the batch (#49019)
  _Files: `python/sglang/srt/beam_search/coordinator.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py` _+9 more__
- **2026-11-08** [`78a9fa1bba`](https://github.com/sgl-project/sglang/commit/78a9fa1bba) [#43703](https://github.com/sgl-project/sglang/pull/43703)
  Revert "[Perf] [NVIDIA] unquant: Autotune low-M BF16 GEMMs via FlashInfer mm_bf16 (#43703)" (#49118)
  _Files: `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`, `python/sglang/srt/models/qwen4_exp.py` _+1 more__
- **2026-11-08** [`3bcde0c80e`](https://github.com/sgl-project/sglang/commit/3bcde0c80e) [#47696](https://github.com/sgl-project/sglang/pull/47696)
  [Perf] diffusion: Run a single packed FA3 sequence through the batch kernel (#47696)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`, `python/sglang/multimodal_gen/test/unit/test_cuda_attention_backend.py`_
- **2026-11-08** [`cbbc6b67f4`](https://github.com/sgl-project/sglang/commit/cbbc6b67f4) [#45891](https://github.com/sgl-project/sglang/pull/45891)
  [Perf] dsa: Run the packed prefill top-k on CUDA (#45891)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer_metadata.py`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/kernels/benchmark/attention/bench_topk.py` _+3 more__
- **2026-11-08** [`94dc5bbf77`](https://github.com/sgl-project/sglang/commit/94dc5bbf77) [#45807](https://github.com/sgl-project/sglang/pull/45807)
  [Perf] [NVIDIA] deepseek-v4.1: Fuse BF16 prefill indexer score epilogue (#45807)
  _Files: `python/sglang/kernels/ops/attention/dsv4/index_score_reduce.py`, `python/sglang/srt/layers/attention/dsv4/dsv41_sparse.py`, `test/registered/kernels/ops/attention/dsv4/test_index_score_reduce.py`_
- **2026-11-08** [`1668d4b993`](https://github.com/sgl-project/sglang/commit/1668d4b993) [#48434](https://github.com/sgl-project/sglang/pull/48434)
  [Fix] [AMD] aiter: Quantize q with its own scale in the fp8 prefills over a gathered cache (#48434)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/aiter_utils.py`, `test/registered/attention/test_aiter_fp8_kv_scales_paths.py`_
- **2026-11-08** [`5713917c55`](https://github.com/sgl-project/sglang/commit/5713917c55) [#48895](https://github.com/sgl-project/sglang/pull/48895)
  [Perf] [NVIDIA] dsa/dcp: Fused DCP8 indexer top-k for decode (#48895)
  _Files: `python/sglang/kernels/jit/csrc/dsa/dcp_fused_topk.cuh`, `python/sglang/kernels/ops/attention/dsa/dcp_fused_topk.py`, `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py`, `python/sglang/srt/environ.py` _+4 more__
- **2026-11-08** [`e30f50724d`](https://github.com/sgl-project/sglang/commit/e30f50724d) [#46929](https://github.com/sgl-project/sglang/pull/46929)
  [Fix] mnnvl: Match FlashInfer's arch-specific CuTe DSL AR profiles (#46929)
  _Files: `python/sglang/srt/layers/flashinfer_mnnvl_cutedsl.py`, `test/registered/unit/layer_boundary/test_cutedsl_ar_fusion.py`_
- **2026-11-07** [`644dd3ac4a`](https://github.com/sgl-project/sglang/commit/644dd3ac4a) [#47893](https://github.com/sgl-project/sglang/pull/47893)
  [Perf] [NVIDIA] glm5_next: Run the fused KDA decode kernel at 8 and 16 heads per rank (#47893)
  _Files: `python/sglang/kernels/jit/csrc/attention/kda_fused_decode.cuh`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/kernels/ops/attention/kda_fused_decode.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py` _+5 more__
- **2026-11-07** [`3048de1871`](https://github.com/sgl-project/sglang/commit/3048de1871) [#48044](https://github.com/sgl-project/sglang/pull/48044)
  [Perf] [AMD] qwen3-next: Fuse the full-attention Q/K GemmaRMSNorm and partial RoPE into one Triton kernel on gfx950 (#48044)
  _Files: `python/sglang/kernels/ops/attention/qk_gemma_norm_rope.py`, `python/sglang/srt/models/qwen3_next.py`, `test/registered/kernels/ops/attention/test_qwen3_next_fused_qk_prologue.py`_
- **2026-11-07** [`caf15159bc`](https://github.com/sgl-project/sglang/commit/caf15159bc) [#38749](https://github.com/sgl-project/sglang/pull/38749)
  [Feat] kernels: Add out-of-tree dispatch for gated RMSNorm (#38749)
  _Files: `python/sglang/kernels/ops/attention/fla/layernorm_gated.py`, `test/registered/attention/test_gdn_prefill_layout.py`, `test/registered/unit/layers/attention/linear/kernels/test_fla_layernorm_gated.py`_
- **2026-11-07** [`6fa3582d36`](https://github.com/sgl-project/sglang/commit/6fa3582d36) [#45497](https://github.com/sgl-project/sglang/pull/45497)
  [Perf] attention: avoid concatenating MLA queries for zigzag CP (#45497)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/cp/zigzag.py`, `test/registered/cp/test_cp_strategy_unit.py`_
- **2026-11-07** [`19cee50c29`](https://github.com/sgl-project/sglang/commit/19cee50c29) [#43703](https://github.com/sgl-project/sglang/pull/43703)
  [Perf] [NVIDIA] unquant: Autotune low-M BF16 GEMMs via FlashInfer mm_bf16 (#43703)
  _Files: `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`, `python/sglang/srt/models/qwen4_exp.py` _+1 more__
- **2026-11-07** [`99833a441e`](https://github.com/sgl-project/sglang/commit/99833a441e) [#48492](https://github.com/sgl-project/sglang/pull/48492)
  [Fix] rust-server: Let DP rank 0's drain wait for every attention-DP listener (#48492)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/rust_server/server.py` _+9 more__
- **2026-11-07** [`00c3b143c0`](https://github.com/sgl-project/sglang/commit/00c3b143c0) [#48740](https://github.com/sgl-project/sglang/pull/48740)
  [Perf] kimi-k3.1: Faster DCP decode reduce (push-combine, V pre-projection, direct exchange) (#48740)
  _Files: `python/sglang/kernels/jit/csrc/dsa/dcp_push_combine.cuh`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/kernels/ops/attention/dcp_push_combine.py` _+9 more__
- **2026-11-07** [`709b8b3c79`](https://github.com/sgl-project/sglang/commit/709b8b3c79) [#48739](https://github.com/sgl-project/sglang/pull/48739)
  [Feat] kimi-k3.1: DSPARK and DFLASH under decode context parallelism (#48739)
  _Files: `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py` _+5 more__
- **2026-11-07** [`a2ad90bd3b`](https://github.com/sgl-project/sglang/commit/a2ad90bd3b) [#48832](https://github.com/sgl-project/sglang/pull/48832)
  [Perf] dsv4: Run compact target verify's ratio 1 and 2 compressors through the fused kernels (#48832)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-11-07** [`21d05ca0c4`](https://github.com/sgl-project/sglang/commit/21d05ca0c4) [#48993](https://github.com/sgl-project/sglang/pull/48993)
  [Refactor] attention: Let the DSV4 backend count the query rows of its prefill shared-read snapshot (#48993)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/hybrid_attn_backend.py`, `python/sglang/srt/model_executor/runner/eager_runner.py` _+5 more__
- **2026-11-07** [`c840718849`](https://github.com/sgl-project/sglang/commit/c840718849) [#48980](https://github.com/sgl-project/sglang/pull/48980)
  [Fix] deepseek-v4.1: Run attention on the real rows of an MLP-sync-padded extend (#48980)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/graph_utils.py`, `python/sglang/srt/layers/radix_attention.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` _+2 more__
- **2026-11-07** [`4bef574039`](https://github.com/sgl-project/sglang/commit/4bef574039) [#48712](https://github.com/sgl-project/sglang/pull/48712)
  [Feat] cuda-graph: Kimi-K3.1 breakable prefill graphs with PP x prefill CP (#48712)
  _Files: `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/cp/bcg/__init__.py`, `python/sglang/srt/layers/cp/bcg/bcg.py` _+6 more__
- **2026-11-07** [`92b1d7be5f`](https://github.com/sgl-project/sglang/commit/92b1d7be5f) [#47695](https://github.com/sgl-project/sglang/pull/47695)
  [Feat] [AMD] quark: Quark int4 W4A16 on ROCm, and gfx1151 kernels for Strix Halo decode and prefill (#47695)
  _Files: `python/sglang/kernels/ops/attention/fla/chunk_fwd.py`, `python/sglang/kernels/ops/attention/fla/chunk_o.py`, `python/sglang/kernels/ops/attention/fla/wy_fast.py`, `python/sglang/kernels/ops/attention/verify_attention_gfx1151.py` _+16 more__
- **2026-11-06** [`6e2f5edf99`](https://github.com/sgl-project/sglang/commit/6e2f5edf99) [#48831](https://github.com/sgl-project/sglang/pull/48831)
  [Perf] dspark: Prepare the DSpark draft attention metadata through the glue graph under every verify mode (#48831)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`_
- **2026-11-06** [`085b0f879d`](https://github.com/sgl-project/sglang/commit/085b0f879d) [#48733](https://github.com/sgl-project/sglang/pull/48733)
  [Perf] [NVIDIA] dsv41: Index-Q RoPE + fp4 pack runs one thread per fp4 block for prefill-sized calls (#48733)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/fp4_indexer_rope.cuh`, `test/registered/kernels/ops/attention/test_fp4_indexer.py`_
- **2026-11-06** [`62384de1ae`](https://github.com/sgl-project/sglang/commit/62384de1ae) [#44399](https://github.com/sgl-project/sglang/pull/44399)
  [Feat] gemma4: per-layer attention backend (#44399)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/hardware_backend/sail/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/minicpm/backend.py` _+8 more__
- **2026-11-06** [`2fd45ed82f`](https://github.com/sgl-project/sglang/commit/2fd45ed82f) [#46597](https://github.com/sgl-project/sglang/pull/46597)
  [Perf] [NVIDIA] minimax-sparse: Run the decode indexer CP on Hopper at TP4 and TP8 (#46597)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py`, `test/registered/kernels/ops/attention/test_minimax_indexer_cp.py`, `test/registered/unit/layers/attention/test_minimax_indexer_cp_gate.py`_
- **2026-11-06** [`d6eb6aa7fe`](https://github.com/sgl-project/sglang/commit/d6eb6aa7fe) [#48857](https://github.com/sgl-project/sglang/pull/48857)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main ce35bc93 (#48857)
  _Files: `docs/src/snippets/_agentx.jsx`, `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx` _+5 more__
- **2026-11-06** [`188cf7da66`](https://github.com/sgl-project/sglang/commit/188cf7da66) [#48721](https://github.com/sgl-project/sglang/pull/48721)
  [Feat] kimi-k3.1: DSA decode context parallelism runtime (#48721)
  _Files: `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py`, `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py`, `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py`, `python/sglang/srt/layers/attention/dsa/dsa_dcp_sharded.py` _+19 more__
- **2026-11-06** [`afe21bcddb`](https://github.com/sgl-project/sglang/commit/afe21bcddb) [#48853](https://github.com/sgl-project/sglang/pull/48853)
  [Chore] flash-attn: Remove the kernels-hub FA3 loader and the kernels dependency (#48853)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`, `docs/docs/references/environment_variables.mdx`, `python/pyproject.toml` _+3 more__
- **2026-11-06** [`80eedfaf2f`](https://github.com/sgl-project/sglang/commit/80eedfaf2f) [#48829](https://github.com/sgl-project/sglang/pull/48829)
  [Chore] deps: Drop flash-attn-4 from default dependencies (#48829)
  _Files: `python/pyproject.toml`, `python/sglang/kernels/ops/attention/flash_attention_v4.py`, `python/sglang/kernels/ops/attention/flash_attention_v4_sm120.py`, `python/sglang/multimodal_gen/runtime/models/dits/cosmos3_simulation/multiview_attention.py` _+5 more__
- **2026-11-06** [`ed61eca15f`](https://github.com/sgl-project/sglang/commit/ed61eca15f) [#48547](https://github.com/sgl-project/sglang/pull/48547)
  [Feat] model: Support ERNIE 5.5 Flash (#48547)
- **2026-11-06** [`bf69aaabaf`](https://github.com/sgl-project/sglang/commit/bf69aaabaf) [#44437](https://github.com/sgl-project/sglang/pull/44437)
  [Fix] mem_cache: Move FP4 MLA block scales with their KV in `move_kv_cache` (#44437)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/mem_cache/test_quantized_kv_pool.py`_
- **2026-11-06** [`abfa0b0850`](https://github.com/sgl-project/sglang/commit/abfa0b0850) [#48525](https://github.com/sgl-project/sglang/pull/48525)
  [Chore] flashmla: bump sgl-flash-mla to 1.0.2 (#48525)
  _Files: `python/pyproject.toml`_
- **2026-11-06** [`4964ced9b1`](https://github.com/sgl-project/sglang/commit/4964ced9b1) [#48789](https://github.com/sgl-project/sglang/pull/48789)
  [Chore] sgl-kernel: Remove the vendored FlashMLA build and wrappers (#48789)
  _Files: `python/sglang/kernels/aot/CMakeLists.txt`, `python/sglang/kernels/aot/benchmark/bench_flashmla_mega.py`, `python/sglang/kernels/aot/cmake/flashmla.cmake`, `python/sglang/kernels/aot/csrc/flashmla_extension.cc` _+7 more__
- **2026-11-06** [`b3f5a7ecbd`](https://github.com/sgl-project/sglang/commit/b3f5a7ecbd) [#33226](https://github.com/sgl-project/sglang/pull/33226)
  [Feat] cp: Support FlashInfer prefill context parallelism (#33226)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/cp/base.py`, `python/sglang/srt/layers/cp/zigzag.py`, `test/registered/cp/test_cp_strategy_unit.py` _+1 more__
- **2026-11-06** [`41e1d97098`](https://github.com/sgl-project/sglang/commit/41e1d97098) [#48756](https://github.com/sgl-project/sglang/pull/48756)
  [CI] spec: Shrink the radix workload in the EAGLE retract stress tests (#48756)
  _Files: `python/sglang/test/kits/radix_cache_server_kit.py`, `python/sglang/test/kits/spec_server_kits.py`, `test/registered/spec/dflash/test_dflash.py`, `test/registered/spec/eagle/test_spec_eagle_stress.py`_
- **2026-11-05** [`ad11717f3b`](https://github.com/sgl-project/sglang/commit/ad11717f3b) [#48737](https://github.com/sgl-project/sglang/pull/48737)
  [Chore] ci: Cut deprecation warnings and TBO debug logs from CI output (#48737)
  _Files: `python/sglang/kernels/ops/attention/cutedsl_gdn.py`, `python/sglang/srt/model_loader/ci_weight_validation.py`, `python/sglang/srt/utils/common.py`, `python/sglang/test/test_utils.py` _+6 more__
- **2026-11-05** [`32b7b66572`](https://github.com/sgl-project/sglang/commit/32b7b66572) [#42718](https://github.com/sgl-project/sglang/pull/42718)
  [Fix] dsv41: Run DSpark compact verify by mapping packed verify tokens to their requests (#42718)
  _Files: `python/sglang/kernels/ops/embeddings/engram_hash.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/dsv41_sparse.py`, `python/sglang/srt/layers/engram.py` _+3 more__
- **2026-11-05** [`a99c1a851e`](https://github.com/sgl-project/sglang/commit/a99c1a851e) [#48622](https://github.com/sgl-project/sglang/pull/48622)
  [Perf] deepseek_v4: call the current DeepGEMM paged MQA API for DSv4.1 decode (#48622)
  _Files: `python/sglang/kernels/ops/attention/dsv4/index_logits.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/metadata.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/full_topk.py` _+3 more__
- **2026-11-05** [`06c60f412a`](https://github.com/sgl-project/sglang/commit/06c60f412a) [#40421](https://github.com/sgl-project/sglang/pull/40421)
  [Perf] [NVIDIA] deepseek-v4.1: Reuse dequantized compressed KV in PD CP prefill (7/N) (#40421)
  _Files: `python/sglang/kernels/ops/attention/dsv4/dequant_k_cache.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `test/registered/kernels/ops/attention/test_dsv41_shared_prefill_kv.py` _+1 more__
- **2026-11-05** [`89b2641381`](https://github.com/sgl-project/sglang/commit/89b2641381) [#46928](https://github.com/sgl-project/sglang/pull/46928)
  [Fix] [AMD] aiter: Fix garbage decode output with unified attention at page size 1 under CUDA graph (#46928)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/attention/test_aiter_unified_attention_page_size_1.py`_
- **2026-11-05** [`1305b1830a`](https://github.com/sgl-project/sglang/commit/1305b1830a) [#48634](https://github.com/sgl-project/sglang/pull/48634)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main 2ad2c9f9 (#48634)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx` _+4 more__
- **2026-11-05** [`c07ec416da`](https://github.com/sgl-project/sglang/commit/c07ec416da) [#47785](https://github.com/sgl-project/sglang/pull/47785)
  [Perf] [NVIDIA] qwen3: Fuse prefill QK norm and RoPE with contiguous Q (#47785)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`, `python/sglang/kernels/jit/csrc/attention/qk_norm_rope.cuh`, `python/sglang/kernels/jit/csrc/elementwise/qknorm.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/impl/norm.cuh` _+6 more__
- **2026-11-05** [`77b6e593e4`](https://github.com/sgl-project/sglang/commit/77b6e593e4) [#47187](https://github.com/sgl-project/sglang/pull/47187)
  [Doc] minimax-m3: Route GB300 decode to trtllm_mha in the cookbook recipe (prefill stays fa4) (#47187)
  _Files: `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`_
- **2026-11-05** [`e32f88502e`](https://github.com/sgl-project/sglang/commit/e32f88502e) [#47678](https://github.com/sgl-project/sglang/pull/47678)
  [Perf] [NVIDIA] dflash: Fill decode-prep length buffers in bulk (#47678)
  _Files: `python/sglang/srt/speculative/dflash_info_v2.py`_
- **2026-11-05** [`f911eef945`](https://github.com/sgl-project/sglang/commit/f911eef945) [#47866](https://github.com/sgl-project/sglang/pull/47866)
  [Fix] KDA: Compile the CuTe DSL decode kernel for the caller's dt_bias dtype (#47866)
  _Files: `python/sglang/kernels/ops/attention/cutedsl_kda.py`, `test/registered/kernels/ops/attention/test_cutedsl_kda.py`_
- **2026-11-05** [`b09bda75c8`](https://github.com/sgl-project/sglang/commit/b09bda75c8) [#47683](https://github.com/sgl-project/sglang/pull/47683)
  [Perf] [NVIDIA] gemm: Tiny GEMM as SIMT + mma.sync templates with batch-size dispatch (#47683)
  _Files: `python/sglang/kernels/jit/csrc/gemm/small_gemm_bf16.cuh`, `python/sglang/kernels/jit/csrc/gemm/tiny_gemm.cuh`, `python/sglang/kernels/jit/csrc/gemm/tiny_gemm/common.cuh`, `python/sglang/kernels/jit/csrc/gemm/tiny_gemm/mma.cuh` _+14 more__
- **2026-11-05** [`815ea8ac18`](https://github.com/sgl-project/sglang/commit/815ea8ac18) [#48499](https://github.com/sgl-project/sglang/pull/48499)
  [Test] [NPU] deepseek_v4_flash: Update 128K AisBench performance test and AisBench (#48499)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/run_aisbench.sh`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_1p1d_16p_in128k_out1k_prefix90_20ms.py`_
- **2026-11-05** [`f3532057e1`](https://github.com/sgl-project/sglang/commit/f3532057e1) [#48588](https://github.com/sgl-project/sglang/pull/48588)
  [Feat] dsa: Exact multicast top-k merge for DCP decode (#48588)
  _Files: `python/sglang/kernels/jit/csrc/dsa/dcp_topk_merge.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/distributed/ptx.cuh`, `python/sglang/kernels/ops/attention/dsa/dcp_topk_merge.py`, `python/sglang/srt/layers/attention/dsa/dsa_dcp_sharded.py` _+1 more__
- **2026-11-05** [`5ec32cef30`](https://github.com/sgl-project/sglang/commit/5ec32cef30) [#47815](https://github.com/sgl-project/sglang/pull/47815)
  [Perf] attention: Use live KV lengths for SM12x FA4 graph replay (#47815)
  _Files: `python/sglang/kernels/ops/attention/fa4_sm120/runtime.py`, `test/registered/kernels/ops/attention/test_flash_attention_4_sm120.py`_
- **2026-11-05** [`b2833196d8`](https://github.com/sgl-project/sglang/commit/b2833196d8) [#48501](https://github.com/sgl-project/sglang/pull/48501)
  [Feat] dsa: Kernel prerequisites for a DCP-sharded indexer (#48501)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/flashmla_sched_meta.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/csrc/dsa/fused_store_index_cache.cuh`, `python/sglang/kernels/ops/attention/dsv4/flashmla_sched_meta.py` _+5 more__
- **2026-11-05** [`c1240a9fa3`](https://github.com/sgl-project/sglang/commit/c1240a9fa3) [#45550](https://github.com/sgl-project/sglang/pull/45550)
  [Fix] [NPU] diffusion: :bug: Auto-select FA for MXFP8 attention (#45550)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/test/unit/test_mxfp8_attention_selection.py`_
- **2026-11-05** [`82554dd0e9`](https://github.com/sgl-project/sglang/commit/82554dd0e9) [#45202](https://github.com/sgl-project/sglang/pull/45202)
  [Perf] [AMD] Kimi-K3: prepare the attention interface for mono fusion (#45202)
  _Files: `python/pyproject_other.toml`, `python/sglang/srt/models/kimi_k3.py`_
- **2026-11-05** [`e3b64bf2a1`](https://github.com/sgl-project/sglang/commit/e3b64bf2a1) [#48546](https://github.com/sgl-project/sglang/pull/48546)
  [Doc] cookbook: Add ERNIE-5.5-Flash deployment recipes (#48546)
  _Files: `docs/cards/logos/ernie.svg`, `docs/cookbook/autoregressive/Baidu/ERNIE-5.5-Flash.mdx`, `docs/cookbook/autoregressive/Baidu/Ernie4.5-VL.mdx`, `docs/cookbook/autoregressive/Baidu/Ernie4.5.mdx` _+7 more__
- **2026-11-05** [`3ead93f76d`](https://github.com/sgl-project/sglang/commit/3ead93f76d) [#45601](https://github.com/sgl-project/sglang/pull/45601)
  [Perf] [AMD] deterministic: Allow AITER prefill attention on gfx950 (#45601)
  _Files: `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/managers/schedule_policy.py` _+1 more__
- **2026-11-05** [`ea2a456627`](https://github.com/sgl-project/sglang/commit/ea2a456627) [#30719](https://github.com/sgl-project/sglang/pull/30719)
  [Perf] [Intel] diffusion: Adding AMX optimizations on CPU platform (#30719)
  _Files: `python/sglang/kernels/aot/csrc/cpu/flash_attn.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/multimodal_gen/configs/models/adapter/base.py`, `python/sglang/multimodal_gen/configs/models/encoders/base.py` _+21 more__
- **2026-11-05** [`3e9ce43944`](https://github.com/sgl-project/sglang/commit/3e9ce43944) [#37597](https://github.com/sgl-project/sglang/pull/37597)
  [Feat] [CPU] glm_ocr: Add model support (#37597)
  _Files: `python/sglang/kernels/aot/csrc/cpu/conv3d.cpp`, `python/sglang/kernels/aot/csrc/cpu/norm.cpp`, `python/sglang/srt/configs/update_config.py`, `python/sglang/srt/layers/attention/vision_utils.py` _+3 more__
- **2026-11-05** [`7fb6ff4736`](https://github.com/sgl-project/sglang/commit/7fb6ff4736) [#48535](https://github.com/sgl-project/sglang/pull/48535)
  [CI] lint: Import ForwardMode from its defining module in the KV translate test (#48535)
  _Files: `test/registered/unit/layers/attention/test_kv_translate_ownership.py`_
- **2026-11-05** [`af633e1759`](https://github.com/sgl-project/sglang/commit/af633e1759) [#40832](https://github.com/sgl-project/sglang/pull/40832)
  [Test] [CPU] UT: Fix the mapping between the TP and the given NUMA nodes. (#40832)
  _Files: `python/sglang/test/test_utils.py`, `test/registered/cpu/quant/test_autoround.py`, `test/registered/cpu/test_binding.py`, `test/registered/cpu/test_cpu_graph.py` _+2 more__
- **2026-11-05** [`2cedfafd30`](https://github.com/sgl-project/sglang/commit/2cedfafd30) [#44459](https://github.com/sgl-project/sglang/pull/44459)
  [Perf] [AMD] mla: Fuse RoPE, concat and KV-cache write for MLA decode on gfx1250 (#44459)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`, `test/registered/unit/models/test_rocm_hisparse_fused_kv.py`, `test/registered/unit/models/test_rocm_mla_absorb_fusion_gate.py`_
- **2026-11-05** [`aaca6d0791`](https://github.com/sgl-project/sglang/commit/aaca6d0791) [#47960](https://github.com/sgl-project/sglang/pull/47960)
  [Perf] [NVIDIA] dsv4/topk_v2: Exactness modes (fast / exact / deterministic) and an exact cluster path (#47960)
  _Files: `python/sglang/kernels/jit/__main__.py`, `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/kernels/ops/attention/dsv4/topk.py` _+2 more__
- **2026-11-05** [`bf20186739`](https://github.com/sgl-project/sglang/commit/bf20186739) [#44394](https://github.com/sgl-project/sglang/pull/44394)
  [Feat] [CPU] cpu-graph: Add prefill torch compile graph and dynamic graph support (#44394)
  _Files: `docs/docs/hardware-platforms/cpu_server.mdx`, `python/sglang/kernels/aot/csrc/cpu/extend.cpp`, `python/sglang/kernels/aot/csrc/cpu/mamba/fla.cpp`, `python/sglang/kernels/aot/csrc/cpu/rope.cpp` _+15 more__
- **2026-11-05** [`6eefba25a0`](https://github.com/sgl-project/sglang/commit/6eefba25a0) [#46922](https://github.com/sgl-project/sglang/pull/46922)
  [Test] cpu: Re-enable the subblock sparse attention test (#46922)
  _Files: `test/registered/cpu/test_subblock_sparse_attention.py`_
- **2026-11-05** [`69fda8040c`](https://github.com/sgl-project/sglang/commit/69fda8040c) [#48467](https://github.com/sgl-project/sglang/pull/48467)
  [Fix] [NVIDIA] deepseek-v4: Pass a caller-owned multi-CTA counter buffer to the trtllm sparse MLA kernel (#48467)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_trtllm_backend.py`, `test/manual/kernels/attention/test_dsv4_trtllm_prefill.py`, `test/registered/attention/unittests/dsv4/test_deepseek_v4.py`_
- **2026-11-05** [`a9d3bb7ddd`](https://github.com/sgl-project/sglang/commit/a9d3bb7ddd) [#47632](https://github.com/sgl-project/sglang/pull/47632)
  [Perf] [AMD] attention: Forward decode graph variants through wrapper backends (#47632)
  _Files: `python/sglang/srt/layers/attention/hybrid_attn_backend.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/tbo_backend.py`, `test/registered/attention/test_aiter_decode_partition_buckets.py` _+1 more__
- **2026-11-05** [`5481134403`](https://github.com/sgl-project/sglang/commit/5481134403) [#41294](https://github.com/sgl-project/sglang/pull/41294)
  [Perf] [NVIDIA] dsv41: Use the fused low-ratio compressor on Hopper (#41294)
  _Files: `python/sglang/srt/layers/attention/dsv4/dsv41_sparse.py`, `test/registered/attention/unittests/dsv4/test_dsv41_fused_compress.py`, `test/registered/kernels/ops/attention/dsv4/test_c2_prefill_ring.py`_
- **2026-11-05** [`1d062d2476`](https://github.com/sgl-project/sglang/commit/1d062d2476) [#48424](https://github.com/sgl-project/sglang/pull/48424)
  [Perf] deepseek_v4: bump sgl-deep-gemm to 0.2.6, FlashInfer-layout scales from DeepGEMM producers, current MQA logits API (#48424)
  _Files: `docker/Dockerfile.cu134`, `python/pyproject.toml`, `python/sglang/kernels/ops/attention/dsv4/index_logits.py`, `python/sglang/srt/layers/quantization/fp8.py` _+4 more__
- **2026-11-05** [`7be9900fb0`](https://github.com/sgl-project/sglang/commit/7be9900fb0) [#47201](https://github.com/sgl-project/sglang/pull/47201)
  [Perf] [NVIDIA] speculative-decoding: Bind generic provider strategies (#47201)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/kernels/plugin_kernels/nvidia/spec.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/kernel_plugins/nvidia/binding.py` _+15 more__
- **2026-11-04** [`c67efab427`](https://github.com/sgl-project/sglang/commit/c67efab427) [#48432](https://github.com/sgl-project/sglang/pull/48432)
  [Doc] [AMD] cookbook: Qwen3.8-Flash-Next MI355X, add the HiCache commands for concurrency 24-80 (#48432)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`_
- **2026-11-04** [`440ae6d070`](https://github.com/sgl-project/sglang/commit/440ae6d070) [#48003](https://github.com/sgl-project/sglang/pull/48003)
  [Refactor] hicache: Move shared host backing and build unified host pools from layout views (#48003)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/kv/__init__.py`, `python/sglang/srt/mem_cache/kv/layout/base.py`, `python/sglang/srt/mem_cache/kv/layout/mha.py` _+8 more__
- **2026-11-04** [`249c09bae5`](https://github.com/sgl-project/sglang/commit/249c09bae5) [#48001](https://github.com/sgl-project/sglang/pull/48001)
  [Fix] spec: Write routed DFLASH and DSPARK context KV into the draft's own rows (#48001)
  _Files: `python/sglang/srt/mem_cache/kv/router.py`, `python/sglang/srt/models/dspark.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/dspark_components/dspark_kv_inject.py` _+3 more__
- **2026-11-04** [`fd19cfb660`](https://github.com/sgl-project/sglang/commit/fd19cfb660) [#48327](https://github.com/sgl-project/sglang/pull/48327)
  [Refactor] scheduler: Release in-step finishes through the request retirer (#48327)
  _Files: `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/scheduler_components/request_retirer.py` _+9 more__
- **2026-11-04** [`e0274b7beb`](https://github.com/sgl-project/sglang/commit/e0274b7beb) [#48392](https://github.com/sgl-project/sglang/pull/48392)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main 57116fff (#48392)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx` _+3 more__
- **2026-11-04** [`82602c0987`](https://github.com/sgl-project/sglang/commit/82602c0987) [#44503](https://github.com/sgl-project/sglang/pull/44503)
  [Refactor] sparse-mla: Expose arithmetic and DSA metadata hooks (#44503)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/model_executor/runner/metadata_glue_graph.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` _+7 more__
- **2026-11-04** [`27aedf7f93`](https://github.com/sgl-project/sglang/commit/27aedf7f93) [#47822](https://github.com/sgl-project/sglang/pull/47822)
  [Perf] [AMD] aiter: Skip q.contiguous() in unified extend when the per-token layout is dense (#47822)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-11-04** [`5e883e409c`](https://github.com/sgl-project/sglang/commit/5e883e409c) [#38440](https://github.com/sgl-project/sglang/pull/38440)
  [Feat] [NPU] DSpark: DeepSeek-V4 support DSpark compact mode (#38440)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_schedule.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_common_hooks.py`, `python/sglang/srt/models/deepseek_v4.py` _+3 more__
- **2026-11-04** [`643909b5a8`](https://github.com/sgl-project/sglang/commit/643909b5a8) [#47924](https://github.com/sgl-project/sglang/pull/47924)
  [Fix] [NPU] attention: Pack valid MLA prefix tokens for mixed batches (#47924)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/mla_cache.py`, `test/registered/unit/npu/attention/test_npu_ascend_backend.py`, `test/registered/unit/npu/attention/test_npu_mla_prefix_cache.py`_
- **2026-11-04** [`b27a5e80a0`](https://github.com/sgl-project/sglang/commit/b27a5e80a0) [#48298](https://github.com/sgl-project/sglang/pull/48298)
  [Fix] spec: Draw `SGLANG_SIMULATE_ACC_LEN` once per step from the server seed (#48298)
  _Files: `python/sglang/kernels/ops/speculative/dspark/simulated_bonus.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py` _+8 more__
- **2026-11-04** [`f03ef01670`](https://github.com/sgl-project/sglang/commit/f03ef01670) [#48160](https://github.com/sgl-project/sglang/pull/48160)
  [Test] [NPU] deepseek_v4: Replace 8K perf case with 128K 1P1D case and add L2 host hit-rate checks (#48160)
  _Files: `.github/workflows/nightly-test-npu.yml`, `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_0731_w8a8_1p1d_16p_gpqa.py`, `test/registered/npu/accuracy/deepseek_v4_pro/test_npu_deepseek_v4_pro_0813_w4a8_1p1d_32p_gpqa.py`, `test/registered/npu/performance/deepseek_v4_flash/expert-layout-ais-replicas16.json` _+2 more__
- **2026-11-04** [`548cbede66`](https://github.com/sgl-project/sglang/commit/548cbede66) [#47944](https://github.com/sgl-project/sglang/pull/47944)
  [Fix] attention: Migrate FLA Triton kernels off tl.make_block_ptr (#47944)
  _Files: `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/chunk_fwd.py`, `python/sglang/kernels/ops/attention/fla/chunk_intra.py`, `python/sglang/kernels/ops/attention/fla/chunk_intra_token_parallel.py` _+12 more__
- **2026-11-04** [`0f3c2c52ba`](https://github.com/sgl-project/sglang/commit/0f3c2c52ba) [#47526](https://github.com/sgl-project/sglang/pull/47526)
  [Perf] Kimi-K3: Enable the fused KDA decode at 6 and 3 heads per rank (#47526)
  _Files: `python/sglang/kernels/ops/attention/kda_fused_decode.py`, `python/sglang/srt/models/kimi_k3.py`_
- **2026-11-04** [`f4b1dc820d`](https://github.com/sgl-project/sglang/commit/f4b1dc820d) [#48246](https://github.com/sgl-project/sglang/pull/48246)
  [Perf] deep_select: use the 3-CTA tier for non-paged bf16 top-512 too (#48246)
  _Files: `python/sglang/kernels/ops/attention/deep_select.py`, `test/registered/kernels/ops/attention/test_deep_select.py`_
- **2026-11-04** [`4699fd4497`](https://github.com/sgl-project/sglang/commit/4699fd4497) [#48266](https://github.com/sgl-project/sglang/pull/48266)
  [Chore] [NVIDIA] deep_select: List SM107 as supported (#48266)
  _Files: `python/sglang/kernels/jit/csrc/deep_select/README.md`, `python/sglang/kernels/jit/csrc/deep_select/entry.cuh`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/deep_select.py` _+2 more__
- **2026-11-04** [`cb7d232f6e`](https://github.com/sgl-project/sglang/commit/cb7d232f6e) [#48243](https://github.com/sgl-project/sglang/pull/48243)
  [Perf] dsv4: dequantize several KV tokens per program in the V4.1 paged dequant (#48243)
  _Files: `python/sglang/kernels/ops/attention/dsv4/dequant_k_cache.py`_
- **2026-11-03** [`76b4c91360`](https://github.com/sgl-project/sglang/commit/76b4c91360) [#48229](https://github.com/sgl-project/sglang/pull/48229)
  [Perf] dsv4: Expand the low-ratio indexer page table in one Triton kernel (#48229)
  _Files: `python/sglang/srt/layers/attention/dsv4/metadata.py`, `test/registered/kernels/ops/attention/dsv4/test_dsv41_decode_glue_hip.py`, `test/registered/kernels/ops/attention/test_fp4_indexer.py`_
- **2026-11-03** [`71ef675ff5`](https://github.com/sgl-project/sglang/commit/71ef675ff5) [#41916](https://github.com/sgl-project/sglang/pull/41916)
  [Fix] sampling: Make top-k/top-p filtering consistent across sampling paths (#41916)
  _Files: `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/eagle_utils.py` _+3 more__
- **2026-11-03** [`4387a94cf2`](https://github.com/sgl-project/sglang/commit/4387a94cf2) [#47119](https://github.com/sgl-project/sglang/pull/47119)
  [Feat] sgl-router: Render MiniMax-M3 and M3.1 through sglang-processor (#47119)
  _Files: `rust/sglang-processor/README.md`, `rust/sglang-processor/src/py.rs`, `rust/sglang-processor/src/render/content_format.rs`, `rust/sglang-processor/src/render/loader.rs` _+53 more__
- **2026-11-03** [`99fd01047d`](https://github.com/sgl-project/sglang/commit/99fd01047d) [#46921](https://github.com/sgl-project/sglang/pull/46921)
  [Feat] [NPU] attention: Support modelslim MLA FP8 KVCache (#46921)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/mla_cache.py`, `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py` _+22 more__
- **2026-11-03** [`c97fe3559f`](https://github.com/sgl-project/sglang/commit/c97fe3559f) [#47064](https://github.com/sgl-project/sglang/pull/47064)
  [Perf] [AMD] kda: Narrow the Kimi-K3 TP8 KDA recurrent tile for small batches on gfx950 (#47064)
  _Files: `python/sglang/kernels/ops/attention/linear/fused_sigmoid_gating_recurrent.py`, `test/registered/kernels/ops/attention/test_kda_recurrent_launch_gfx950.py`_
- **2026-11-03** [`aecfbce3fd`](https://github.com/sgl-project/sglang/commit/aecfbce3fd) [#45248](https://github.com/sgl-project/sglang/pull/45248)
  [Refactor] kda: Import recurrent_kda from the canonical flashinfer namespace (#45248)
  _Files: `benchmark/bench_linear_attention/bench_kda_flashinfer_mtp.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashinfer.py`_
- **2026-11-03** [`8d4e1ce4c7`](https://github.com/sgl-project/sglang/commit/8d4e1ce4c7) [#47969](https://github.com/sgl-project/sglang/pull/47969)
  [CI] [AMD] pr-test: Run the MI35x 1-GPU stage after MI300 stage-b; move test_flydsl_v4nm_decode to nightly (#47969)
  _Files: `.github/workflows/pr-test-amd.yml`, `test/registered/kernels/ops/attention/dsv4/test_flydsl_v4nm_decode.py`_
- **2026-11-03** [`80121f264f`](https://github.com/sgl-project/sglang/commit/80121f264f) [#47993](https://github.com/sgl-project/sglang/pull/47993)
  [Perf] [NVIDIA] qwen3: Reuse the table QK-norm/RoPE kernel for MRoPE decode (#47993)
  _Files: `python/sglang/kernels/ops/attention/table_qk_norm_rope.py`, `python/sglang/srt/models/qwen3.py`, `test/registered/kernels/ops/attention/test_table_qk_norm_rope.py`, `test/registered/unit/models/test_qwen3_qk_norm_rope.py`_
- **2026-11-03** [`cbfc0932e3`](https://github.com/sgl-project/sglang/commit/cbfc0932e3) [#44489](https://github.com/sgl-project/sglang/pull/44489)
  [Perf] [AMD] deterministic: Allow AITER decode attention on gfx950 (#44489)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-11-03** [`c68083d53c`](https://github.com/sgl-project/sglang/commit/c68083d53c) [#48070](https://github.com/sgl-project/sglang/pull/48070)
  [Doc] cookbook: Add MiniMax-M3.1-Flash GB300 MonoKernel and DEP16 AgentX points (#48070)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`_
- **2026-11-03** [`cd41d53d69`](https://github.com/sgl-project/sglang/commit/cd41d53d69) [#47929](https://github.com/sgl-project/sglang/pull/47929)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main c5e8b9b3 and revert #47560 (#47929)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`, `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next-b300.jsx` _+5 more__
- **2026-11-03** [`18b714464f`](https://github.com/sgl-project/sglang/commit/18b714464f) [#48051](https://github.com/sgl-project/sglang/pull/48051)
  [Doc] qwen: Use TRT-LLM MHA for the B300 Qwen3-VL-4B recipe (#48051)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3-VL.mdx`, `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`, `docs/src/snippets/autoregressive/qwen3-vl-deployment.jsx`_
- **2026-11-03** [`f6db18e8c2`](https://github.com/sgl-project/sglang/commit/f6db18e8c2) [#47261](https://github.com/sgl-project/sglang/pull/47261)
  [Fix] attention: Keep fused RoPE KV writes off DCP layouts (#47261)
  _Files: `python/sglang/srt/models/utils.py`, `test/registered/unit/models/test_fused_set_kv_buffer_gate.py`_
- **2026-11-02** [`33a1ba4a8a`](https://github.com/sgl-project/sglang/commit/33a1ba4a8a) [#44197](https://github.com/sgl-project/sglang/pull/44197)
  [Fix] [AMD] mamba: Import the causal conv1d kernels for Mamba2 layers on ROCm (#44197)
  _Files: `python/sglang/srt/layers/attention/mamba/mamba.py`_
- **2026-11-02** [`20f5f68729`](https://github.com/sgl-project/sglang/commit/20f5f68729) [#45443](https://github.com/sgl-project/sglang/pull/45443)
  [Fix] [AMD] imports: Skip import-time device probes when no GPU is visible (#45443)
  _Files: `python/sglang/kernels/ops/attention/rocm_mla_decode_rope.py`, `python/sglang/srt/utils/common.py`, `test/registered/unit/utils/test_common.py`_
- **2026-11-02** [`251eb36da0`](https://github.com/sgl-project/sglang/commit/251eb36da0) [#47951](https://github.com/sgl-project/sglang/pull/47951)
  [Doc] [AMD] cookbook: Qwen3.8-Flash-Next MI355X, add the monokernel command for concurrency 1-8 (#47951)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`_
- **2026-11-02** [`e33cd0c3a1`](https://github.com/sgl-project/sglang/commit/e33cd0c3a1) [#42968](https://github.com/sgl-project/sglang/pull/42968)
  [Perf] DeepSeek-V4.1: Support indexer TP shard (#42968)
  _Files: `python/sglang/kernels/ops/attention/dsv4/index_logits.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/__init__.py` _+7 more__
- **2026-11-02** [`ad6ca42dea`](https://github.com/sgl-project/sglang/commit/ad6ca42dea) [#46082](https://github.com/sgl-project/sglang/pull/46082)
  [Perf] trtllm_mha: Split full-attention decode KV across CTAs at large batch (opt-in) (#46082)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `test/registered/unit/layers/attention/test_trtllm_mha_paged_kv.py`_
- **2026-11-02** [`755783ebe1`](https://github.com/sgl-project/sglang/commit/755783ebe1) [#47306](https://github.com/sgl-project/sglang/pull/47306)
  [Perf] allreduce: enable FlashInfer AllReduce Fusion auto-enable for Kimi-K3 (#47306)
  _Files: `python/sglang/srt/arg_groups/overrides.py`_
- **2026-11-02** [`58592ce679`](https://github.com/sgl-project/sglang/commit/58592ce679) [#47902](https://github.com/sgl-project/sglang/pull/47902)
  [Test] [NPU] DeepSeek_v4_pro: Add 16p mix in128k out1k performance and gpqa testcase, DeepSeek_v4_flash:Enable  GPQA case in 950 and add 1p1d gpqa testcase in A3 (#47902)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_0731_w8a8_1p1d_16p_gpqa.py`, `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_fp8_4p_gpqa_a5.py` _+2 more__
- **2026-11-02** [`a4e51e2873`](https://github.com/sgl-project/sglang/commit/a4e51e2873) [#47714](https://github.com/sgl-project/sglang/pull/47714)
  [Refactor] memory-pool: Build QSA indexer host pools as hybrid sidecars (#47714)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/host_pool_config.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/kernels/ops/attention/qsa/test_qsa_hicache.py` _+2 more__
- **2026-11-02** [`c0c7af402b`](https://github.com/sgl-project/sglang/commit/c0c7af402b) [#47860](https://github.com/sgl-project/sglang/pull/47860)
  [Fix] spec: Give the mocked draft decode backend a cache_loc_dtype in the inkling test (#47860)
  _Files: `test/registered/kernels/ops/attention/test_inkling_checkpoint_indices.py`_
- **2026-11-02** [`cc69762cb7`](https://github.com/sgl-project/sglang/commit/cc69762cb7) [#46816](https://github.com/sgl-project/sglang/pull/46816)
  [Fix] [Intel] gemma4: Bidirectional image attention on the intel_xpu backend (#46816)
  _Files: `docs/cookbook/autoregressive/Google/Gemma4.mdx`, `python/sglang/srt/layers/attention/xpu_backend.py`, `python/sglang/srt/models/gemma4_diffusion.py`, `python/sglang/srt/models/gemma4_mm.py` _+2 more__
- **2026-11-02** [`23c6442cde`](https://github.com/sgl-project/sglang/commit/23c6442cde) [#46478](https://github.com/sgl-project/sglang/pull/46478)
  [Fix] attention: Use ModelRunner query width for DSpark FlashAttention drafts (#46478)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/unit/layers/attention/test_flashattention_graph_metadata.py`_
- **2026-11-02** [`39a5d5b135`](https://github.com/sgl-project/sglang/commit/39a5d5b135) [#30980](https://github.com/sgl-project/sglang/pull/30980)
  [Feat] [XPU] graph: Add full prefill graph (#30980)
  _Files: `docs/docs/hardware-platforms/xpu.mdx`, `python/sglang/srt/arg_groups/platform_hook.py`, `python/sglang/srt/hardware_backend/xpu/graph_runner/xpu_full_graph_backend.py`, `python/sglang/srt/hardware_backend/xpu/graph_runner/xpu_graph_runner.py` _+5 more__
- **2026-11-02** [`9dfa1374e2`](https://github.com/sgl-project/sglang/commit/9dfa1374e2) [#47367](https://github.com/sgl-project/sglang/pull/47367)
  [Feat] [NPU] attention: support mixed-chunk on the ascend attention backend (#47367)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py`_
- **2026-11-02** [`3e88483288`](https://github.com/sgl-project/sglang/commit/3e88483288) [#47844](https://github.com/sgl-project/sglang/pull/47844)
  [Doc] [AMD] cookbook: Verify MiniMax-M3.1-Flash High-Throughput on MI355X (#47844)
  _Files: `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`_
- **2026-11-02** [`b47e58e429`](https://github.com/sgl-project/sglang/commit/b47e58e429) [#47599](https://github.com/sgl-project/sglang/pull/47599)
  [Fix] rust-server: Give each attention-DP listener its own frontend cores (#47599)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/rust_server/server.py`, `test/registered/unit/entrypoints/test_rust_server_dp_ports.py` _+2 more__
- **2026-11-02** [`8fd34681ca`](https://github.com/sgl-project/sglang/commit/8fd34681ca) [#47234](https://github.com/sgl-project/sglang/pull/47234)
  [Feat] attention: Add OOT linear-attention backend registration (#47234)
  _Files: `docs/docs/hardware-platforms/plugin.mdx`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py` _+1 more__
- **2026-11-02** [`2dc5bdd18b`](https://github.com/sgl-project/sglang/commit/2dc5bdd18b) [#47743](https://github.com/sgl-project/sglang/pull/47743)
  [Perf] mla: Use masked K concatenation for padded head counts (#47743)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `test/registered/kernels/ops/attention/test_concat_mla.py`_
- **2026-11-02** [`7605a94d8b`](https://github.com/sgl-project/sglang/commit/7605a94d8b) [#36059](https://github.com/sgl-project/sglang/pull/36059)
  [Perf] dsv4: Add native H16 CuTe sparse prefill backend (#36059)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/advanced_features/server_arguments_undocumented.txt`, `python/sglang/kernels/ops/attention/__init__.py` _+11 more__
- **2026-11-02** [`ae66493995`](https://github.com/sgl-project/sglang/commit/ae66493995) [#47030](https://github.com/sgl-project/sglang/pull/47030)
  [Fix] [AMD] aiter: Use the layer's KV scales in the legacy target-verify attention (#47030)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/attention/test_aiter_fp8_kv_scales_paths.py`_
- **2026-11-02** [`46e95bb9f9`](https://github.com/sgl-project/sglang/commit/46e95bb9f9) [#47042](https://github.com/sgl-project/sglang/pull/47042)
  [Perf] [AMD] aiter: Bucket decode paged-attention partitions by sequence length (#47042)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/base_attn_backend.py` _+5 more__
- **2026-11-02** [`4ae54e9458`](https://github.com/sgl-project/sglang/commit/4ae54e9458) [#47651](https://github.com/sgl-project/sglang/pull/47651)
  [Perf] kda: Batch strided FlashInfer prefill input copies (#47651)
  _Files: `python/sglang/kernels/ops/attention/kda_input_pack.py`, `python/sglang/srt/layers/attention/linear/kda_flashinfer_prefill_graph.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_flashinfer_prefill.py`, `test/registered/kernels/ops/attention/test_kda_input_pack.py`_
- **2026-11-02** [`a7c9c3cad0`](https://github.com/sgl-project/sglang/commit/a7c9c3cad0) [#47675](https://github.com/sgl-project/sglang/pull/47675)
  [Refactor] memory-pool: Build MiniMax K-only index host pools from buffer info (#47675)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/pool_host/mha.py` _+5 more__
- **2026-11-02** [`74ef460d02`](https://github.com/sgl-project/sglang/commit/74ef460d02) [#46738](https://github.com/sgl-project/sglang/pull/46738)
  [Perf] kda: Write convolution output directly into contiguous QKV planes (#46738)
  _Files: `python/sglang/kernels/ops/mamba/causal_conv1d_triton.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kda_prefill_graph.py`, `test/registered/kernels/ops/mamba/test_causal_conv1d_split_output.py` _+1 more__
- **2026-11-02** [`a8e1539ea6`](https://github.com/sgl-project/sglang/commit/a8e1539ea6) [#47512](https://github.com/sgl-project/sglang/pull/47512)
  [Perf] sampling: JIT softmax and argmax for the sampler and speculative verify (#47512)
  _Files: `python/sglang/kernels/jit/csrc/sampling/argmax.cuh`, `python/sglang/kernels/jit/csrc/sampling/softmax.cuh`, `python/sglang/kernels/ops/sampling/__init__.py`, `python/sglang/kernels/ops/sampling/argmax_jit.py` _+18 more__
- **2026-11-02** [`297d2a14ea`](https://github.com/sgl-project/sglang/commit/297d2a14ea) [#47023](https://github.com/sgl-project/sglang/pull/47023)
  [Test] [NPU] deepseek_v4_flash: Switch FP8 4P GPQA test from EAGLE to DSPARK and add acceptance-rate test (#47023)
  _Files: `python/sglang/test/ascend/e2e/run_npu_testcase.sh`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_fp8_4p_gpqa_a5.py`_
- **2026-11-02** [`2b38f4a6ed`](https://github.com/sgl-project/sglang/commit/2b38f4a6ed) [#47791](https://github.com/sgl-project/sglang/pull/47791)
  [Doc] cookbook: Sync MiniMax-M3.1-Flash GB300 AgentX points (#47791)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`_
- **2026-11-02** [`9fcb7a7b98`](https://github.com/sgl-project/sglang/commit/9fcb7a7b98) [#47373](https://github.com/sgl-project/sglang/pull/47373)
  [Perf] [NPU] attention: Support mlaprolog for kimik3 (#47373)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`_
- **2026-11-02** [`a8c69d0f20`](https://github.com/sgl-project/sglang/commit/a8c69d0f20) [#46225](https://github.com/sgl-project/sglang/pull/46225)
  [Fix] attention: Zero padded KDA/GDN recurrent outputs (#46225)
  _Files: `python/sglang/kernels/ops/attention/linear/fused_sigmoid_gating_recurrent.py`, `test/registered/kernels/ops/attention/test_kda_replayssm_ring_ragged.py`_
- **2026-11-02** [`3a345c0743`](https://github.com/sgl-project/sglang/commit/3a345c0743) [#47804](https://github.com/sgl-project/sglang/pull/47804)
  [Refactor] environ: Rename the SGLANG_Q35MF_* runtime switches to SGLANG_OPT_* names (#47804)
  _Files: `python/sglang/kernels/ops/memory/small_field_copy.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/managers/scheduler_components/shm_tag_exchange.py` _+11 more__

## Prefill / Decode Disaggregation  (76 commits)

- **2026-11-09** [`ab84df61dd`](https://github.com/sgl-project/sglang/commit/ab84df61dd) [#46168](https://github.com/sgl-project/sglang/pull/46168)
  [Perf] mooncake: Cut the host time of direct linker layer-wise loads (#46168)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `test/registered/unit/mem_cache/test_linker_pool_assembler.py`, `test/registered/unit/mem_cache/test_mooncake_direct_linker_load.py` _+2 more__
- **2026-11-09** [`388d03b775`](https://github.com/sgl-project/sglang/commit/388d03b775) [#48014](https://github.com/sgl-project/sglang/pull/48014)
  [Feat] attention: Serve several window sub-pools per runner in the Triton backend (#48014)
  _Files: `python/sglang/srt/dllm/attention.py`, `python/sglang/srt/hardware_backend/musa/attention/flashattention_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/attention/aiter_backend.py` _+62 more__
- **2026-11-09** [`c89cedec26`](https://github.com/sgl-project/sglang/commit/c89cedec26) [#48013](https://github.com/sgl-project/sglang/pull/48013)
  [Refactor] mem_cache: Give each window sub-pool its own host pool, PD entry and metrics (#48013)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/checksum.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py` _+66 more__
- **2026-11-09** [`72edb269c2`](https://github.com/sgl-project/sglang/commit/72edb269c2) [#48009](https://github.com/sgl-project/sglang/pull/48009)
  [Refactor] disaggregation: Track unified PD transfers per row and reuse their pages only once quiescent (#48009)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/decode.py` _+44 more__
- **2026-11-09** [`c81230bffe`](https://github.com/sgl-project/sglang/commit/c81230bffe) [#46517](https://github.com/sgl-project/sglang/pull/46517)
  [Fix] srt: Promptly abort running requests on client disconnect (#46517) (#46586)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/test/few_shot_gsm8k.py`, `test/registered/amd/disaggregation/test_disaggregation_pp.py` _+1 more__
- **2026-11-09** [`fb359066c2`](https://github.com/sgl-project/sglang/commit/fb359066c2) [#49218](https://github.com/sgl-project/sglang/pull/49218)
  [Fix] disaggregation: Unregister a failed staging room before releasing its KV (#49218)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_deferred_decode_kv_release.py`_
- **2026-11-09** [`fa57fe84a3`](https://github.com/sgl-project/sglang/commit/fa57fe84a3) [#48936](https://github.com/sgl-project/sglang/pull/48936)
  [CI] ep: Log Mooncake EP JIT events in test_mooncake_ep_small (#48936)
  _Files: `test/registered/ep/test_mooncake_ep_small.py`_
- **2026-11-09** [`7f1d05758d`](https://github.com/sgl-project/sglang/commit/7f1d05758d) [#46552](https://github.com/sgl-project/sglang/pull/46552)
  [Perf] VLM: reuse precomputed combined_hash in MultiModalStaticCache.get (#46552)
  _Files: `python/sglang/srt/disaggregation/encoder/server.py`, `python/sglang/srt/managers/mm_schedule.py`, `python/sglang/srt/mem_cache/multimodal_cache.py`, `test/registered/chunked_prefill/test_mm_chunked_embedding_unit.py` _+1 more__
- **2026-11-09** [`6044714393`](https://github.com/sgl-project/sglang/commit/6044714393) [#45106](https://github.com/sgl-project/sglang/pull/45106)
  [Perf] mooncake: Group and parallelize direct linker layer-wise loads (#45106)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `test/registered/unit/mem_cache/test_mooncake_direct_linker_load.py`_
- **2026-11-09** [`75d7c3ba83`](https://github.com/sgl-project/sglang/commit/75d7c3ba83) [#48882](https://github.com/sgl-project/sglang/pull/48882)
  [Fix] [NPU] dsa: Allow DSA DCP with PD disaggregation (#48882)
  _Files: `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py`, `test/registered/unit/test_dsa_dcp_backend_defaults.py`_
- **2026-11-08** [`842b473831`](https://github.com/sgl-project/sglang/commit/842b473831) [#49156](https://github.com/sgl-project/sglang/pull/49156)
  [Fix] disagg: Fail startup when Mooncake rejects KV buffer registration (#49156)
  _Files: `python/sglang/srt/distributed/device_communicators/mooncake_transfer_engine.py`, `test/registered/unit/disaggregation/test_encode_server.py`_
- **2026-11-08** [`a7d9f81ee2`](https://github.com/sgl-project/sglang/commit/a7d9f81ee2) [#49153](https://github.com/sgl-project/sglang/pull/49153)
  [Test] scheduler: Record embedding sends and check at idle that every taken request sent its final output (#49153)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/exit_ledger.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py` _+3 more__
- **2026-11-08** [`620413be1a`](https://github.com/sgl-project/sglang/commit/620413be1a) [#49151](https://github.com/sgl-project/sglang/pull/49151)
  [Fix] scheduler: Finish rejected requests and offloaded releases through the request retirer (#49151)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` _+17 more__
- **2026-11-08** [`94d1e0230c`](https://github.com/sgl-project/sglang/commit/94d1e0230c) [#48741](https://github.com/sgl-project/sglang/pull/48741)
  [Feat] kimi-k3.1: PD disaggregation under decode context parallelism (#48741)
  _Files: `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py`, `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py` _+16 more__
- **2026-11-08** [`c24285bde9`](https://github.com/sgl-project/sglang/commit/c24285bde9) [#48008](https://github.com/sgl-project/sglang/pull/48008)
  [Refactor] mem_cache: Gate unified page reuse and moves on one per-band page ledger (#48008)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/environ.py` _+85 more__
- **2026-11-08** [`dadff253c0`](https://github.com/sgl-project/sglang/commit/dadff253c0) [#48006](https://github.com/sgl-project/sglang/pull/48006)
  [Refactor] mem_cache: Name each unified window sub-pool by its own window length (#48006)
  _Files: `python/sglang/srt/disaggregation/checksum.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/disaggregation/prefill.py` _+44 more__
- **2026-11-08** [`de3636131d`](https://github.com/sgl-project/sglang/commit/de3636131d) [#48852](https://github.com/sgl-project/sglang/pull/48852)
  [Perf] mem_cache: Defer reuse of freed unified pages instead of waiting on every free (#48852)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `python/sglang/srt/managers/scheduler.py` _+20 more__
- **2026-11-08** [`b070051032`](https://github.com/sgl-project/sglang/commit/b070051032) [#49144](https://github.com/sgl-project/sglang/pull/49144)
  [Refactor] scheduler: Move the pause state into PauseState (#49144)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py` _+18 more__
- **2026-11-08** [`d9fbbb67f1`](https://github.com/sgl-project/sglang/commit/d9fbbb67f1) [#49018](https://github.com/sgl-project/sglang/pull/49018)
  [Test] scheduler: Check that a request exits and sends its final output at most once (#49018)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/exit_ledger.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py` _+16 more__
- **2026-11-07** [`7975093bd1`](https://github.com/sgl-project/sglang/commit/7975093bd1) [#49016](https://github.com/sgl-project/sglang/pull/49016)
  [Test] unit: Pin the Python frontend in tests of Python-frontend-only behaviour (#49016)
  _Files: `test/registered/unit/disaggregation/test_pd_role_switch.py`, `test/registered/unit/multimodal/test_gpu_feature_transport.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-11-07** [`043cfc4d3a`](https://github.com/sgl-project/sglang/commit/043cfc4d3a) [#48375](https://github.com/sgl-project/sglang/pull/48375)
  [Feat] PD: Publish spec_kv_layout so DSpark/DFlash prefill and decode must match (#48375)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/utils.py`, `rust/sglang-server/src/api_server/disaggregation/bootstrap.rs`, `test/registered/unit/disaggregation/test_pd_spec_kv_layout.py` _+1 more__
- **2026-11-07** [`a1a0e19f0f`](https://github.com/sgl-project/sglang/commit/a1a0e19f0f) [#48818](https://github.com/sgl-project/sglang/pull/48818)
  [Feat] rust-server: Let an embedding package register scheduler state fields for /server_info (#48818)
  _Files: `rust/sglang-server/src/api_server/core/fanout.rs`, `rust/sglang-server/src/api_server/disaggregation/bootstrap.rs`, `rust/sglang-server/src/api_server/handlers/handle.rs`, `rust/sglang-server/src/api_server/handlers/info.rs` _+5 more__
- **2026-11-07** [`cd81454957`](https://github.com/sgl-project/sglang/commit/cd81454957) [#48753](https://github.com/sgl-project/sglang/pull/48753)
  [Feat] rust-server: Refuse more ignored settings, add a launch-time GenerateValidator, and catalogue the Python frontend's config reads (#48753)
  _Files: `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/rust_server/parity.py`, `rust/sglang-server/src/api_server/core.rs`, `rust/sglang-server/src/api_server/core/validator.rs` _+23 more__
- **2026-11-07** [`3572b9c318`](https://github.com/sgl-project/sglang/commit/3572b9c318) [#48992](https://github.com/sgl-project/sglang/pull/48992)
  [Fix] scheduler: Honor pause_generation under PP and release aborted PD rooms and rejected sessions (#48992)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py` _+7 more__
- **2026-11-07** [`b165323cb6`](https://github.com/sgl-project/sglang/commit/b165323cb6) [#48877](https://github.com/sgl-project/sglang/pull/48877)
  [Feat] kimi-k3.1: HiCache under decode context parallelism (#48877)
  _Files: `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py` _+5 more__
- **2026-11-07** [`baef1bbb2c`](https://github.com/sgl-project/sglang/commit/baef1bbb2c) [#48997](https://github.com/sgl-project/sglang/pull/48997)
  [Feat] scheduler: Run the state checks in the PD and PP loops and after a flush (#48997)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py` _+12 more__
- **2026-11-07** [`79a3b21956`](https://github.com/sgl-project/sglang/commit/79a3b21956) [#48710](https://github.com/sgl-project/sglang/pull/48710)
  [Feat] kimi-k3.1: MegaMoE, breakable prefill graphs and DFlash under prefill CP (#48710)
  _Files: `python/sglang/srt/arg_groups/cp_tp_group_sharing_hook.py`, `python/sglang/srt/arg_groups/mega_moe_hook.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/layers/attention/dsa/dsa_prefill_cuda_graph.py` _+4 more__
- **2026-11-07** [`0b2a6bdf33`](https://github.com/sgl-project/sglang/commit/0b2a6bdf33) [#48983](https://github.com/sgl-project/sglang/pull/48983)
  [Chore] ci: Remove the runtime Docker image release workflow (#48983)
  _Files: `.github/workflows/_docker-build-and-publish.yml`, `.github/workflows/release-docker-cu134-nightly.yml`, `.github/workflows/release-docker-dev.yml`, `.github/workflows/release-docker-efa.yml` _+7 more__
- **2026-11-06** [`5be59a4c73`](https://github.com/sgl-project/sglang/commit/5be59a4c73) [#48451](https://github.com/sgl-project/sglang/pull/48451)
  [Perf] pd: Poll the prefill result wait per attention-DP shard and pump HiCache storage events in it (#48451)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/disaggregation/test_prefill_result_polling.py` _+1 more__
- **2026-11-06** [`adeec96c4c`](https://github.com/sgl-project/sglang/commit/adeec96c4c) [#48496](https://github.com/sgl-project/sglang/pull/48496)
  [Perf] mem_cache: Order recycled unified-page writers after the forward instead of the current stream (#48496)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/kv/alloc/band.py` _+4 more__
- **2026-11-06** [`5ff6b5a5cf`](https://github.com/sgl-project/sglang/commit/5ff6b5a5cf) [#48458](https://github.com/sgl-project/sglang/pull/48458)
  [Fix] disaggregation: Keep non-final KV sends inside the protected prefix (#48458)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `test/registered/unit/disaggregation/test_dcp_pack.py`, `test/registered/unit/disaggregation/test_prefill_send_protection.py`, `test/registered/unit/mem_cache/test_minimax_m31_cache_transfer.py`_
- **2026-11-06** [`bda1cf5295`](https://github.com/sgl-project/sglang/commit/bda1cf5295) [#48699](https://github.com/sgl-project/sglang/pull/48699)
  [CI] [AMD] disaggregation: Send aux data over TCP in the PP disaggregation test (#48699)
  _Files: `test/registered/amd/disaggregation/test_disaggregation_pp.py`_
- **2026-11-06** [`4be69b9f47`](https://github.com/sgl-project/sglang/commit/4be69b9f47) [#48757](https://github.com/sgl-project/sglang/pull/48757)
  [Fix] scheduler: Abort beam groups on a retract pause and close three request-drop gaps (#48757)
  _Files: `python/sglang/srt/disaggregation/role_switch.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+7 more__
- **2026-11-06** [`8b4a67714c`](https://github.com/sgl-project/sglang/commit/8b4a67714c) [#48447](https://github.com/sgl-project/sglang/pull/48447)
  [Fix] dp-attention: Carry a rank's ShutdownReq to its DP peers through the MLP-sync gather (#48447)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/rust_server/shutdown.py` _+3 more__
- **2026-11-06** [`771f70732d`](https://github.com/sgl-project/sglang/commit/771f70732d) [#45772](https://github.com/sgl-project/sglang/pull/45772)
  [Fix] encoder: allocate embedding cache resources only on rank 0 (#45772)
  _Files: `python/sglang/srt/disaggregation/encoder/server.py`, `python/sglang/srt/mem_cache/embedding_cache_controller.py`, `test/registered/unit/disaggregation/test_embedding_cache_tp_coordination.py`, `test/registered/unit/disaggregation/test_encoder_global_cache_rank0.py` _+1 more__
- **2026-11-06** [`44da79bf1e`](https://github.com/sgl-project/sglang/commit/44da79bf1e) [#48827](https://github.com/sgl-project/sglang/pull/48827)
  [Refactor] utils: Keep sglang.srt and sglang.kernels off sglang.utils (#48827)
  _Files: `.pre-commit-config.yaml`, `python/sglang/__init__.py`, `python/sglang/_lazy_import.py`, `python/sglang/kernels/aot/benchmark/bench_activation.py` _+68 more__
- **2026-11-06** [`db2952a4f5`](https://github.com/sgl-project/sglang/commit/db2952a4f5) [#48231](https://github.com/sgl-project/sglang/pull/48231)
  [Fix] disaggregation: Reject a decode peer whose KV page stride differs at Mooncake registration (#48231)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-11-06** [`6b3d6ce21d`](https://github.com/sgl-project/sglang/commit/6b3d6ce21d) [#45600](https://github.com/sgl-project/sglang/pull/45600)
  [Feat] linker: Add prefetch mode for the Mooncake external linker (#45600)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/managers/scheduler.py` _+15 more__
- **2026-11-05** [`3f1fcf9a35`](https://github.com/sgl-project/sglang/commit/3f1fcf9a35) [#48037](https://github.com/sgl-project/sglang/pull/48037)
  [Perf] disaggregation: Cache host-staged decode admission accounting across a transfer pass (#48037)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/utils.py`, `test/registered/unit/disaggregation/test_unified_memory_move_gate.py`_
- **2026-11-05** [`9b6c796151`](https://github.com/sgl-project/sglang/commit/9b6c796151) [#48452](https://github.com/sgl-project/sglang/pull/48452)
  [Fix] disaggregation: Publish a yielded optimistic prefill's KV under a write-through cache (#48452)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `test/registered/disaggregation/test_disaggregation_optimistic_prefill.py`_
- **2026-11-05** [`8898429e9b`](https://github.com/sgl-project/sglang/commit/8898429e9b) [#48491](https://github.com/sgl-project/sglang/pull/48491)
  [Refactor] scheduler: Release every PD disaggregation exit through RequestRetirer (#48491)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/scheduler.py` _+29 more__
- **2026-11-05** [`c03b6b3df5`](https://github.com/sgl-project/sglang/commit/c03b6b3df5) [#47200](https://github.com/sgl-project/sglang/pull/47200)
  [Perf] [NVIDIA] speculative-decoding: Add generic CUDA runtime fast paths (#47200)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/trtllm_mha_graph_metadata.py`, `python/sglang/kernels/ops/speculative/eagle.py` _+67 more__
- **2026-11-05** [`9a3ed54639`](https://github.com/sgl-project/sglang/commit/9a3ed54639) [#48637](https://github.com/sgl-project/sglang/pull/48637)
  Revert "[Feat] docker: Install AWS EFA in the main image; drop the EFA image variant" (#48637)
  _Files: `.github/workflows/release-docker-efa.yml`, `docker/Dockerfile`, `docker/efa.Dockerfile`, `docker/install_efa.sh` _+2 more__
- **2026-11-05** [`f64efd63fd`](https://github.com/sgl-project/sglang/commit/f64efd63fd) [#48325](https://github.com/sgl-project/sglang/pull/48325)
  [Feat] docker: Install AWS EFA in the main image; drop the EFA image variant (#48325)
  _Files: `.github/workflows/release-docker-efa.yml`, `docker/Dockerfile`, `docker/efa.Dockerfile`, `docker/install_efa.sh` _+2 more__
- **2026-11-05** [`0fd3515d5f`](https://github.com/sgl-project/sglang/commit/0fd3515d5f) [#48485](https://github.com/sgl-project/sglang/pull/48485)
  [Fix] [AMD] mooncake: Bump Mooncake to pick up the HIP IPC sub-allocation fix (#48485)
  _Files: `docker/rocm.Dockerfile`_
- **2026-11-05** [`5ebb02d9ee`](https://github.com/sgl-project/sglang/commit/5ebb02d9ee) [#48339](https://github.com/sgl-project/sglang/pull/48339)
  [CI] [NPU] nightly-4-npu-a3: Rebalance partitions, bound retries, retire GLM-5.2 16p accuracy (#48339)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/npu_eval_accuracy_kit.py`, `test/registered/npu/basic_function/dp_attn/test_npu_dp_attention.py`, `test/registered/npu/basic_function/parallel_strategy/data_parallelism/test_npu_load_balance_method_pd_disaggregation.py`_
- **2026-11-04** [`18a879f847`](https://github.com/sgl-project/sglang/commit/18a879f847) [#48004](https://github.com/sgl-project/sglang/pull/48004)
  [Refactor] mem_cache: Own state and fixed payloads in the KV storage plan and size from them (#48004)
  _Files: `python/sglang/kernels/ops/attention/linear/fused_recurrent_linear_replayssm.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` _+92 more__
- **2026-11-04** [`61a3c7f2a4`](https://github.com/sgl-project/sglang/commit/61a3c7f2a4) [#48415](https://github.com/sgl-project/sglang/pull/48415)
  [Feat] model: Add basic Kimi-K3.1 support (NV, AMD) (#48415)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/ops/attention/dsa/triton_sparse_mla.py`, `python/sglang/kernels/ops/attention/dsa/triton_sparse_mla_decode.py`, `python/sglang/kernels/ops/attention/dsv4/topk.py` _+33 more__
- **2026-11-04** [`7828f56701`](https://github.com/sgl-project/sglang/commit/7828f56701) [#47120](https://github.com/sgl-project/sglang/pull/47120)
  [Fix] multimodal: Preserve strong identities across VLM caches (#47120)
  _Files: `docs/docs/advanced_features/vlm_query.mdx`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` _+54 more__
- **2026-11-04** [`4dc6070f58`](https://github.com/sgl-project/sglang/commit/4dc6070f58) [#41504](https://github.com/sgl-project/sglang/pull/41504)
  [Chore] [NPU] common: Update references from A5 to arch35 or Ascend 950 across multiple modules (#41504)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/ascend_fa.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/environ.py` _+19 more__
- **2026-11-04** [`426281d1bc`](https://github.com/sgl-project/sglang/commit/426281d1bc) [#48283](https://github.com/sgl-project/sglang/pull/48283)
  [Refactor] scheduler: Retire every queued abort through one RequestRetirer entry (#48283)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/request_retirer.py` _+9 more__
- **2026-11-04** [`4c7c775cf4`](https://github.com/sgl-project/sglang/commit/4c7c775cf4) [#48292](https://github.com/sgl-project/sglang/pull/48292)
  [Fix] disaggregation: Reject the KV checksum with DeepSeek-V4 and on a HiSparse decode (#48292)
  _Files: `python/sglang/srt/arg_groups/hisparse_hook.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`_
- **2026-11-04** [`b9f5d7000c`](https://github.com/sgl-project/sglang/commit/b9f5d7000c) [#47255](https://github.com/sgl-project/sglang/pull/47255)
  [Fix] disaggregation: Bind NIXL transfer workers to the rank's device (#47255)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-11-04** [`d091f25872`](https://github.com/sgl-project/sglang/commit/d091f25872) [#43911](https://github.com/sgl-project/sglang/pull/43911)
  [Fix] hisparse: Release HiSparse rows on the KV checksum mismatch and chunked abort exits (#43911)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/disaggregation/test_kv_checksum.py`, `test/registered/unit/managers/test_scheduler_chunked_abort_race.py`_
- **2026-11-03** [`a4bef204c5`](https://github.com/sgl-project/sglang/commit/a4bef204c5) [#43910](https://github.com/sgl-project/sglang/pull/43910)
  [Refactor] scheduler: Hold the waiting queue and the chunked slot in request lists (#43910)
  _Files: `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py` _+41 more__
- **2026-11-03** [`f7cdb8fa3f`](https://github.com/sgl-project/sglang/commit/f7cdb8fa3f) [#48131](https://github.com/sgl-project/sglang/pull/48131)
  [CI] [AMD] nightly-disagg: Keep all MI355X CI settings in the repo and clean up after failed jobs (#48131)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`, `scripts/ci/slurm/generate_matrix.py`, `scripts/ci/slurm/launch_mi355x.sh`, `scripts/ci/slurm/nightly-configs.yaml` _+37 more__
- **2026-11-03** [`57bfde9f2c`](https://github.com/sgl-project/sglang/commit/57bfde9f2c) [#48192](https://github.com/sgl-project/sglang/pull/48192)
  [Chore] mooncake: bump mooncake version to 0.3.14 (#48192)
  _Files: `docker/Dockerfile`, `scripts/ci/cuda/ci_install_dependency.sh`, `test/registered/ep/test_mooncake_ep_small.py`_
- **2026-11-03** [`b6a59c4938`](https://github.com/sgl-project/sglang/commit/b6a59c4938) [#47928](https://github.com/sgl-project/sglang/pull/47928)
  [Refactor] memory-pool: Assemble HiCache host pools from buffer info (#47928)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/mem_cache/hybrid_cache/host_pool_config.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py` _+8 more__
- **2026-11-03** [`fbe54087d6`](https://github.com/sgl-project/sglang/commit/fbe54087d6) [#48121](https://github.com/sgl-project/sglang/pull/48121)
  [Test] mooncake: bind metadata server to loopback in tests (#48121)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/README.md`, `python/sglang/test/mooncake_utils.py`, `test/registered/hicache/test_hicache_storage_mooncake_backend.py`, `test/registered/hicache/test_pp_with_hicache.py`_
- **2026-11-03** [`94aaad8e65`](https://github.com/sgl-project/sglang/commit/94aaad8e65) [#43908](https://github.com/sgl-project/sglang/pull/43908)
  [Refactor] scheduler: Hold wrapped requests in request lists and abort through each list (#43908)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/hisparse_coordinator.py` _+28 more__
- **2026-11-03** [`ed8d232c1a`](https://github.com/sgl-project/sglang/commit/ed8d232c1a) [#43907](https://github.com/sgl-project/sglang/pull/43907)
  [Refactor] scheduler: Share one interface across request lists and abort through each list (#43907)
  _Files: `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/encoder/receiver.py`, `python/sglang/srt/disaggregation/prefill.py` _+41 more__
- **2026-11-03** [`c8704818d4`](https://github.com/sgl-project/sglang/commit/c8704818d4) [#47992](https://github.com/sgl-project/sglang/pull/47992)
  [CI] lint: Reject importing a name through a module that only re-imports it (#47992)
  _Files: `.pre-commit-config.yaml`, `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/sampler.py` _+7 more__
- **2026-11-03** [`dbeecc932d`](https://github.com/sgl-project/sglang/commit/dbeecc932d) [#43906](https://github.com/sgl-project/sglang/pull/43906)
  [Fix] scheduler: Tell a step's middle chunk from the batch's chunked request, not a per-request counter (#43906)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+14 more__
- **2026-11-03** [`b8100b74bf`](https://github.com/sgl-project/sglang/commit/b8100b74bf) [#40825](https://github.com/sgl-project/sglang/pull/40825)
  [Feat] [NPU] kimi-k3: Support DCP with shared compact communication (#40825)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py`, `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py` _+9 more__
- **2026-11-03** [`ba1ed00dfe`](https://github.com/sgl-project/sglang/commit/ba1ed00dfe) [#43905](https://github.com/sgl-project/sglang/pull/43905)
  [Fix] scheduler: Abort held decode requests, and read live requests from the lists (#43905)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/internal_state.py`, `test/registered/unit/managers/test_deferred_output.py` _+3 more__
- **2026-11-03** [`797af7170f`](https://github.com/sgl-project/sglang/commit/797af7170f) [#43904](https://github.com/sgl-project/sglang/pull/43904)
  [Refactor] scheduler: Check request ownership once at step launch (#43904)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/managers/scheduler_components/running_reqs.py` _+10 more__
- **2026-11-02** [`3674c7173f`](https://github.com/sgl-project/sglang/commit/3674c7173f) [#43903](https://github.com/sgl-project/sglang/pull/43903)
  [Refactor] scheduler: Hold a launched prefill in one list until its next holder takes it (#43903)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py` _+14 more__
- **2026-11-02** [`b55350bb93`](https://github.com/sgl-project/sglang/commit/b55350bb93) [#46654](https://github.com/sgl-project/sglang/pull/46654)
  [Fix] scheduler: Skip --prefill-decode-interval when nothing is decoding (#46654)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/schedule.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_prefill_decode_interval.py`_
- **2026-11-02** [`427d8dec90`](https://github.com/sgl-project/sglang/commit/427d8dec90) [#37976](https://github.com/sgl-project/sglang/pull/37976)
  [Feat] trace: propagate per-request context to mooncake store RPC for end-to-end request tracing (#37976)
  _Files: `python/sglang/srt/arg_groups/fields/observability.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py` _+5 more__
- **2026-11-02** [`1599b166ac`](https://github.com/sgl-project/sglang/commit/1599b166ac) [#45377](https://github.com/sgl-project/sglang/pull/45377)
  [CI] [Intel] disaggregation: Run XPU P/D nightly on Mooncake and NIXL (#45377)
  _Files: `.github/workflows/pr-test-xpu.yml`, `docker/xpu.Dockerfile`, `docs/docs/advanced_features/pd_disaggregation.mdx`, `docs/docs/hardware-platforms/xpu.mdx` _+5 more__
- **2026-11-02** [`960e30769e`](https://github.com/sgl-project/sglang/commit/960e30769e) [#43901](https://github.com/sgl-project/sglang/pull/43901)
  [Refactor] scheduler: List every request holder and check no request is in two (#43901)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/deferred_responses.py` _+8 more__
- **2026-11-02** [`768e56202b`](https://github.com/sgl-project/sglang/commit/768e56202b) [#43902](https://github.com/sgl-project/sglang/pull/43902)
  [Refactor] scheduler: Move deferred responses into an object and rename the PD prefill inflight queue to the transfer queue (#43902)
  _Files: `python/sglang/srt/disaggregation/fake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/role_switch.py`, `python/sglang/srt/disaggregation/utils.py` _+26 more__
- **2026-11-02** [`96b5d058b3`](https://github.com/sgl-project/sglang/commit/96b5d058b3) [#47680](https://github.com/sgl-project/sglang/pull/47680)
  [Fix] mem_cache: Skip Mamba checkpoint donation when slots are exhausted (#47680)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/mamba.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`, `test/registered/unit/mem_cache/test_mamba_donated_alloc_ratio.py`_
- **2026-11-02** [`d644cfbe35`](https://github.com/sgl-project/sglang/commit/d644cfbe35) [#47735](https://github.com/sgl-project/sglang/pull/47735)
  [Refactor] vlm/unlimited-ocr: Reduce scheduler coupling (#47735)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py` _+24 more__
- **2026-11-02** [`48db87c29c`](https://github.com/sgl-project/sglang/commit/48db87c29c) [#47825](https://github.com/sgl-project/sglang/pull/47825)
  [CI] disaggregation: Fail a PD test launch fast when an H20 runner is short of GPUs (#47825)
  _Files: `python/sglang/test/test_utils.py`_
- **2026-11-02** [`dfbbfc3116`](https://github.com/sgl-project/sglang/commit/dfbbfc3116) [#47737](https://github.com/sgl-project/sglang/pull/47737)
  [Fix] disaggregation: Use the shared ZMQ context for staging prefetch sockets (#47737)
  _Files: `python/sglang/srt/disaggregation/common/staging_handler.py`_

## MoE / Expert Parallel  (67 commits)

- **2026-11-09** [`c69fb82a56`](https://github.com/sgl-project/sglang/commit/c69fb82a56) [#48871](https://github.com/sgl-project/sglang/pull/48871)
  [Fix] modelopt_fp4: Skip swizzled NVFP4 MoE blockscales on Marlin paths (#48871)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`_
- **2026-11-09** [`ff762d62f8`](https://github.com/sgl-project/sglang/commit/ff762d62f8) [#48942](https://github.com/sgl-project/sglang/pull/48942)
  [Refactor] jit: Unify FP32 activation functions in sgl_kernel/activation.cuh (#48942)
  _Files: `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-jit-kernel/performance-cuda.md`, `python/sglang/kernels/jit/csrc/attention/kda_fused_decode.cuh`, `python/sglang/kernels/jit/csrc/attention/kda_packed_decode.cuh` _+33 more__
- **2026-11-09** [`2ad35d4535`](https://github.com/sgl-project/sglang/commit/2ad35d4535) [#48165](https://github.com/sgl-project/sglang/pull/48165)
  [Perf] quantization: Speed up Hopper group32 FP8 quantization with FP32 scales (#48165)
  _Files: `python/sglang/kernels/jit/csrc/gemm/per_token_group_quant.cuh`, `python/sglang/kernels/jit/csrc/gemm/per_token_group_quant_8bit_v2.cuh`, `python/sglang/kernels/jit/csrc/moe/route_quant_fused.cuh`, `python/sglang/kernels/ops/quantization/fp8_kernel.py` _+8 more__
- **2026-11-09** [`e24833d3e8`](https://github.com/sgl-project/sglang/commit/e24833d3e8) [#49171](https://github.com/sgl-project/sglang/pull/49171)
  [Fix] rope/env: Remove the leftover Dual Chunk Attention RoPE, make env alias warnings visible, restore the DGX Spark b12x env (#49171)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`, `python/sglang/kernels/aot/tests/test_fused_qk_norm_rope.py`, `python/sglang/srt/configs/model_config.py` _+13 more__
- **2026-11-09** [`e6a1ab527e`](https://github.com/sgl-project/sglang/commit/e6a1ab527e) [#47956](https://github.com/sgl-project/sglang/pull/47956)
  [Feat] xpu: Consolidate simple XPU enablements (#47956)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.mdx`, `docs/src/snippets/autoregressive/qwen3-deployment.jsx`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/hardware_backend/xpu/attention/xpu_gdn_backend.py` _+13 more__
- **2026-11-08** [`3825fcd397`](https://github.com/sgl-project/sglang/commit/3825fcd397) [#43739](https://github.com/sgl-project/sglang/pull/43739)
  [Feat] [Ascend] quantization: :sparkles: Support online W4A8 MoE (#43739)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/quant.py`, `python/sglang/srt/hardware_backend/npu/quantization/fp4_moe_methods.py`, `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`, `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py` _+13 more__
- **2026-11-08** [`51d8d1dbbc`](https://github.com/sgl-project/sglang/commit/51d8d1dbbc) [#49091](https://github.com/sgl-project/sglang/pull/49091)
  [Perf] [NVIDIA] moe: Generalize the MXFP4 decode MoE kernel to covered shapes and DeepSeek-V4 (#49091)
  _Files: `python/sglang/kernels/jit/csrc/moe/mxfp4_decode/moe_mxfp4.cuh`, `python/sglang/kernels/ops/moe/k31_decode_moe.py`, `python/sglang/kernels/ops/moe/mxfp4_decode_moe.py`, `python/sglang/srt/environ.py` _+7 more__
- **2026-11-08** [`b6e1401f2f`](https://github.com/sgl-project/sglang/commit/b6e1401f2f) [#48642](https://github.com/sgl-project/sglang/pull/48642)
  [Feat] paged-experts: keep experts on disk so later starts skip loading them (#48642)
  _Files: `docs/docs/advanced_features/paged_experts.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/exec_.py` _+10 more__
- **2026-11-08** [`917c27f1a4`](https://github.com/sgl-project/sglang/commit/917c27f1a4) [#46693](https://github.com/sgl-project/sglang/pull/46693)
  [Feat] [AMD] minimax: Support MiniMax-M3.1-Flash on MI350X / MI355X (gfx950) (#46693)
  _Files: `python/sglang/kernels/jit/utils/hipcc.py`, `python/sglang/kernels/ops/gemm/aiter_asm_blockscale.py`, `python/sglang/kernels/ops/gemm/router_gemv.py`, `python/sglang/kernels/ops/gemm/smallm_fp8_gfx950/__init__.py` _+52 more__
- **2026-11-08** [`2d94e564f4`](https://github.com/sgl-project/sglang/commit/2d94e564f4) [#49096](https://github.com/sgl-project/sglang/pull/49096)
  [Fix] megamoe: Accept FlashInfer 0.7.3 knob cache and enum config fields in startup autotune (#49096)
  _Files: `python/sglang/srt/layers/moe/flashinfer_megamoe_autotune.py`, `test/registered/unit/layers/moe/test_flashinfer_megamoe.py`_
- **2026-11-08** [`c24fa91506`](https://github.com/sgl-project/sglang/commit/c24fa91506) [#48952](https://github.com/sgl-project/sglang/pull/48952)
  [CI] ep: Port the FlashInfer dispatcher test to flashinfer.moe_ep and run it in CI (#48952)
  _Files: `test/manual/ep/test_flashinfer_dispatcher.py`, `test/registered/ep/test_flashinfer_dispatcher.py`_
- **2026-11-07** [`8920463c90`](https://github.com/sgl-project/sglang/commit/8920463c90) [#47247](https://github.com/sgl-project/sglang/pull/47247)
  [Perf] deepseek-v4.1: Use reduce-scatter for CP MoE output (#47247)
  _Files: `python/sglang/srt/models/deepseek_common/moe_transport.py`_
- **2026-11-07** [`5bc1dbe7b1`](https://github.com/sgl-project/sglang/commit/5bc1dbe7b1) [#48946](https://github.com/sgl-project/sglang/pull/48946)
  [Refactor] moe: Remove the bailing_moe_topk and JIT moe_topk_sigmoid routers (#48946)
  _Files: `python/sglang/kernels/jit/csrc/moe/bailing_moe_topk.cuh`, `python/sglang/kernels/jit/csrc/moe/moe_topk_sigmoid.cuh`, `python/sglang/kernels/ops/moe/__init__.py`, `python/sglang/kernels/ops/moe/bailing_moe_topk.py` _+6 more__
- **2026-11-07** [`773fac6d3c`](https://github.com/sgl-project/sglang/commit/773fac6d3c) [#48638](https://github.com/sgl-project/sglang/pull/48638)
  [Perf] [NVIDIA] moe: Add an opt-in persistent MXFP4 decode MoE kernel for Kimi-K3.1 (#48638)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mhc_post_combine_norm_decode.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/wo_a_fused.cuh`, `python/sglang/kernels/jit/csrc/gemm/tiny_gemm/mma.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/attn_res/fused_tma.cuh` _+17 more__
- **2026-11-07** [`d0c2bd97ae`](https://github.com/sgl-project/sglang/commit/d0c2bd97ae) [#48404](https://github.com/sgl-project/sglang/pull/48404)
  [Fix] eplb: reject incompatible recorder modes (#48404)
  _Files: `python/sglang/srt/arg_groups/parallel_hook.py`, `test/registered/npu/basic_function/parallel_strategy/expert_parallelism/test_npu_expert_distribution_recorder_mode.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-11-07** [`780baaaf61`](https://github.com/sgl-project/sglang/commit/780baaaf61) [#49017](https://github.com/sgl-project/sglang/pull/49017)
  [Fix] moe: Match the Triton renormalize sum order in the warp MoE router (#49017)
  _Files: `python/sglang/kernels/jit/csrc/moe/route_warp.cuh`_
- **2026-11-07** [`b8529362f5`](https://github.com/sgl-project/sglang/commit/b8529362f5) [#48470](https://github.com/sgl-project/sglang/pull/48470)
  [Perf] diffusion: Tune LingBot MoE TMA for B300 SXM6 AC (#48470)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=128,N=768,device_name=NVIDIA_B300_SXM6_AC.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=128,N=768,device_name=NVIDIA_B300_SXM6_AC_down.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `test/registered/kernels/ops/moe/test_moe_tma_down_padding_rows.py`_
- **2026-11-07** [`a40b25a2a4`](https://github.com/sgl-project/sglang/commit/a40b25a2a4) [#48584](https://github.com/sgl-project/sglang/pull/48584)
  [Perf] kimi-k3.1: TP-shard the decode MoE front and latent-up tail (#48584)
  _Files: `python/sglang/kernels/jit/csrc/kimi_k3/comm/gemm_ag.cuh`, `python/sglang/kernels/jit/csrc/kimi_k3/comm/moe_front_ag.cuh`, `python/sglang/kernels/ops/communication/__init__.py`, `python/sglang/kernels/ops/communication/gemm_ag.py` _+6 more__
- **2026-11-07** [`b548ead20f`](https://github.com/sgl-project/sglang/commit/b548ead20f) [#48711](https://github.com/sgl-project/sglang/pull/48711)
  [Perf] kimi-k3.1: Fuse MegaMoE padding masks, DSA indexer Q prep and CP row copies (#48711)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dsa/head_gate.py`, `python/sglang/kernels/ops/memory/__init__.py` _+8 more__
- **2026-11-07** [`b82e93fc06`](https://github.com/sgl-project/sglang/commit/b82e93fc06) [#48990](https://github.com/sgl-project/sglang/pull/48990)
  [CI] ci: Remove 13 nightly CUDA tests (#48990)
  _Files: `scripts/ci/rerun_test_groups.json`, `test/registered/attention/test_glm4_moe_lite_deterministic.py`, `test/registered/basic_perf/test_torch_compile_throughput.py`, `test/registered/e2e/models/test_deepseek_v4_flash_fp4_b200_tbo.py` _+10 more__
- **2026-11-06** [`dc4b17b108`](https://github.com/sgl-project/sglang/commit/dc4b17b108) [#48468](https://github.com/sgl-project/sglang/pull/48468)
  [Chore] [NVIDIA] deps: Bump FlashInfer to 0.7.3 and migrate the NVLink one-sided all-to-all to flashinfer.moe_ep (#48468)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`, `python/pyproject.toml`, `python/sglang/kernels/jit/csrc/minimax/nvfp4_store_kv_index.cuh` _+9 more__
- **2026-11-06** [`66daed55d3`](https://github.com/sgl-project/sglang/commit/66daed55d3) [#48784](https://github.com/sgl-project/sglang/pull/48784)
  [Perf] eplb: Vectorize the static per-rank dispatch map (#48784)
  _Files: `python/sglang/srt/eplb/expert_location.py`_
- **2026-11-06** [`0fc97bc07c`](https://github.com/sgl-project/sglang/commit/0fc97bc07c) [#48586](https://github.com/sgl-project/sglang/pull/48586)
  [Perf] kimi-k3: Fuse the decode MoE routing for 1-256 rows into one kernel (#48586)
  _Files: `python/sglang/kernels/jit/csrc/moe/kimi_k3_fused_routing.cuh`, `python/sglang/kernels/ops/moe/kimi_k3_fused_routing.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/moe/route_quant_handoff.py` _+4 more__
- **2026-11-06** [`600dd9e57a`](https://github.com/sgl-project/sglang/commit/600dd9e57a) [#41635](https://github.com/sgl-project/sglang/pull/41635)
  [Feat] gemma4: Add out-of-tree MoE expert executor selection (#41635)
  _Files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/expert_executor.py`, `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/platforms/interface.py` _+1 more__
- **2026-11-06** [`c7959958df`](https://github.com/sgl-project/sglang/commit/c7959958df) [#48174](https://github.com/sgl-project/sglang/pull/48174)
  [Perf] [NVIDIA] moe: Re-land the JIT moe_finalize_fuse_shared with the shared row read after the PDL wait (#48174)
  _Files: `python/sglang/kernels/jit/csrc/moe/moe_finalize_fuse_shared.cu`, `python/sglang/kernels/jit/csrc/moe/moe_finalize_fuse_shared.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/math.cuh`, `python/sglang/kernels/ops/moe/moe_finalize_fuse_shared.py` _+2 more__
- **2026-11-06** [`1442917b4a`](https://github.com/sgl-project/sglang/commit/1442917b4a) [#46053](https://github.com/sgl-project/sglang/pull/46053)
  [Fix] function_call: Normalize GLM non-streaming tool names (#46053)
  _Files: `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `test/registered/unit/function_call/test_function_call_parser.py`, `test/registered/unit/function_call/test_glm47_schema_types.py`_
- **2026-11-06** [`76c36dc7ed`](https://github.com/sgl-project/sglang/commit/76c36dc7ed) [#47354](https://github.com/sgl-project/sglang/pull/47354)
  [Perf] [NVIDIA] glm5: Route small-M BF16 GEMMs to FlashInfer warp split-K with PDL on SM107 (#47354)
  _Files: `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe.py`_
- **2026-11-06** [`2878e71fd7`](https://github.com/sgl-project/sglang/commit/2878e71fd7) [#48723](https://github.com/sgl-project/sglang/pull/48723)
  [Perf] mega_moe: reserve 18 SMs for MegaMoE in sm107 decode and target-verify (#48723)
  _Files: `python/sglang/srt/layers/moe/mega_moe.py`, `test/registered/unit/layers/moe/test_mega_moe_deepgemm_api.py`_
- **2026-11-06** [`5481ac5523`](https://github.com/sgl-project/sglang/commit/5481ac5523) [#48751](https://github.com/sgl-project/sglang/pull/48751)
  [Fix] eplb: Keep draft forwards out of the target expert window (#48751)
  _Files: `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/model_executor/model_runner.py`, `test/registered/unit/eplb/test_expert_distribution_disabled_pass.py`_
- **2026-11-06** [`1ecf89bf9d`](https://github.com/sgl-project/sglang/commit/1ecf89bf9d) [#48264](https://github.com/sgl-project/sglang/pull/48264)
  [Feat] beam: support LoRA for BF16 and FP8 (#48264)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/lora/lora.py`, `python/sglang/srt/lora/mem_pool.py`, `python/sglang/srt/lora/utils.py` _+6 more__
- **2026-11-05** [`50322ac7ba`](https://github.com/sgl-project/sglang/commit/50322ac7ba) [#48617](https://github.com/sgl-project/sglang/pull/48617)
  [CI] runners: Move base-b H100 tests to 1-gpu-small, extra-a, or nightly (#48617)
  _Files: `test/registered/attention/test_deterministic.py`, `test/registered/attention/test_gemma4_unified_swa_virtual_ids.py`, `test/registered/attention/test_unified_memory_deterministic.py`, `test/registered/core/test_srt_engine.py` _+45 more__
- **2026-11-05** [`cf6133a16c`](https://github.com/sgl-project/sglang/commit/cf6133a16c) [#46890](https://github.com/sgl-project/sglang/pull/46890)
  [Feat] dsa: Extend interleave-CP breakable prefill graphs to GlmMoeDs… (#46890)
  _Files: `python/sglang/kernels/ops/attention/dsa/cp_split.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/dsa_prefill_cuda_graph.py`, `python/sglang/srt/layers/attention/dsa_backend.py` _+2 more__
- **2026-11-05** [`47b4fe572b`](https://github.com/sgl-project/sglang/commit/47b4fe572b) [#48082](https://github.com/sgl-project/sglang/pull/48082)
  [Perf] paged-experts: load experts without a staging copy (#48082)
  _Files: `docs/docs/advanced_features/paged_experts.mdx`, `python/sglang/srt/layers/moe/paged_experts/formats.py`, `python/sglang/srt/layers/moe/paged_experts/method.py`, `python/sglang/srt/layers/moe/paged_experts/store.py` _+2 more__
- **2026-11-05** [`d1e2fab36d`](https://github.com/sgl-project/sglang/commit/d1e2fab36d) [#48166](https://github.com/sgl-project/sglang/pull/48166)
  [Perf] [NVIDIA] moe: Add L4 Triton fused MoE configs for Qwen3-30B-A3B (#48166)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=128,N=192,device_name=NVIDIA_L4.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=128,N=384,device_name=NVIDIA_L4,dtype=fp8_w8a8,block_shape=[128, 128].json`_
- **2026-11-05** [`45886872fd`](https://github.com/sgl-project/sglang/commit/45886872fd) [#48134](https://github.com/sgl-project/sglang/pull/48134)
  [CI] [AMD] ci: Follow #47619 on AMD and fix two never-run registrations (#48134)
  _Files: `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd-extra.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/attention/test_torch_native_attention_backend.py` _+36 more__
- **2026-11-05** [`242d15673e`](https://github.com/sgl-project/sglang/commit/242d15673e) [#39793](https://github.com/sgl-project/sglang/pull/39793)
  [Feat] xing4_0: Add model support (#39793)
  _Files: `docs/docs/advanced_features/tool_parser.mdx`, `docs/docs/supported-models/generative_models.mdx`, `python/sglang/kernels/ops/layernorm/mhc.py`, `python/sglang/srt/arg_groups/model_hook.py` _+15 more__
- **2026-11-05** [`f85fef81a8`](https://github.com/sgl-project/sglang/commit/f85fef81a8) [#44491](https://github.com/sgl-project/sglang/pull/44491)
  [Perf] qwen3: Fuse SiLU*mul with the NVFP4 quantization of down_proj in Qwen2MLP (#44491)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/qwen2.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3.py` _+3 more__
- **2026-11-04** [`de522adc0d`](https://github.com/sgl-project/sglang/commit/de522adc0d) [#47643](https://github.com/sgl-project/sglang/pull/47643)
  [Perf] [NVIDIA] mega_moe: Count EPLB load in-kernel (#47643)
  _Files: `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `test/registered/unit/eplb/test_megamoe_prefill_recorder.py`, `test/registered/unit/layers/moe/test_mega_moe_deepgemm_api.py`_
- **2026-11-04** [`58484246d2`](https://github.com/sgl-project/sglang/commit/58484246d2) [#45828](https://github.com/sgl-project/sglang/pull/45828)
  [Perf] fp8: Hopper small-M GEMV, fused KDA output quant, CUDA grouped top-k, partial-block tails (#45828)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/kernels/jit/csrc/gemm/hopper_bf16_tiny_gemv.cuh`, `python/sglang/kernels/jit/csrc/gemm/hopper_fp8_block_gemv.cuh`, `python/sglang/kernels/jit/csrc/gemm/router_gate_matvec.cuh` _+25 more__
- **2026-11-04** [`c16144293a`](https://github.com/sgl-project/sglang/commit/c16144293a) [#48223](https://github.com/sgl-project/sglang/pull/48223)
  [Fix] test: Import sgl_kernel in the Arm64 MoE test (#48223)
  _Files: `test/registered/cpu/arm64/test_moe.py`_
- **2026-11-04** [`e2ad447d00`](https://github.com/sgl-project/sglang/commit/e2ad447d00) [#47853](https://github.com/sgl-project/sglang/pull/47853)
  [Feat] halops: Add HALOps as an opt-in MXFP8 GEMM backend for Blackwell and support mxfp8 megamoe (#47853)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`, `docs/docs/advanced_features/quantization.mdx`, `docs/docs/advanced_features/server_arguments.mdx` _+10 more__
- **2026-11-04** [`ac93f6ca0e`](https://github.com/sgl-project/sglang/commit/ac93f6ca0e) [#48109](https://github.com/sgl-project/sglang/pull/48109)
  [Fix] moe: Match padded-row indices to token-count dtype (#48109)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/moe/test_topk_padded_region.py`_
- **2026-11-04** [`d973326298`](https://github.com/sgl-project/sglang/commit/d973326298) [#47821](https://github.com/sgl-project/sglang/pull/47821)
  [Fix] [NPU] MOE: Skip MoE padded-row kernel launches for empty tensors in case of crashing on NPU (#47821)
  _Files: `python/sglang/kernels/ops/moe/fill_padded_rows.py`_
- **2026-11-03** [`3384ec8890`](https://github.com/sgl-project/sglang/commit/3384ec8890) [#48245](https://github.com/sgl-project/sglang/pull/48245)
  [Perf] dsv4: four chunks per thread in mega MoE pre-dispatch for prefill-sized batches (#48245)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`_
- **2026-11-03** [`7b88f09239`](https://github.com/sgl-project/sglang/commit/7b88f09239) [#48099](https://github.com/sgl-project/sglang/pull/48099)
  [Perf] [NVIDIA] moe: Release localized Mega MoE originals so KV capacity matches non-localized (#48099)
  _Files: `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-11-03** [`1ef3335da1`](https://github.com/sgl-project/sglang/commit/1ef3335da1) [#48041](https://github.com/sgl-project/sglang/pull/48041)
  [Fix] moe: Skip hash layers before topk_config in prefill routing paths (#48041)
  _Files: `python/sglang/srt/models/deepseek_v2.py`, `test/registered/unit/models/test_native_moe_routing_policy.py`_
- **2026-11-03** [`4494d68237`](https://github.com/sgl-project/sglang/commit/4494d68237) [#47641](https://github.com/sgl-project/sglang/pull/47641)
  [Perf] [NVIDIA] moe: One-warp-per-token CUDA MoE router for sigmoid, sqrtsoftplus and softmax routing (#47641)
  _Files: `python/sglang/kernels/jit/csrc/lora/trtllm_lora_temp/kimi_k2_moe_fused_gate.cuh`, `python/sglang/kernels/jit/csrc/lora/trtllm_lora_temp/topk_softmax_pack.cuh`, `python/sglang/kernels/jit/csrc/moe/moe_topk_softmax.cuh`, `python/sglang/kernels/jit/csrc/moe/route_warp.cuh` _+19 more__
- **2026-11-03** [`4709a3a24e`](https://github.com/sgl-project/sglang/commit/4709a3a24e) [#47976](https://github.com/sgl-project/sglang/pull/47976)
  [Perf] [NVIDIA] moe: Localize DeepGEMM Mega MoE weights across locality domains (#47976)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/eplb/expert_location_updater.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `test/manual/test_expert_location_updater.py`_
- **2026-11-03** [`af98fcd545`](https://github.com/sgl-project/sglang/commit/af98fcd545) [#47653](https://github.com/sgl-project/sglang/pull/47653)
  Revert "[Perf] kimi-k3: Seed a validated FlashInfer prefill MoE tactic (#47653)" (#48055)
  _Files: `python/sglang/srt/layers/moe/configs/kimi_k3_sm103_fi072_prefill.json`, `python/sglang/srt/layers/moe/flashinfer_kimi_k3_tactics.py`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`, `test/registered/unit/layers/moe/test_kimi_k3_prefill_tactics.py` _+1 more__
- **2026-11-03** [`62f9f3f785`](https://github.com/sgl-project/sglang/commit/62f9f3f785) [#44148](https://github.com/sgl-project/sglang/pull/44148)
  [Feat] moe: Allow SiTU on the CuTe DSL NVFP4 MoE (Kimi-K3 W4A16) (#44148)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/unit/layers/quantization/test_nvfp4_cutedsl_w4a16_situ_moe.py`_
- **2026-11-03** [`8a0edcf799`](https://github.com/sgl-project/sglang/commit/8a0edcf799) [#47476](https://github.com/sgl-project/sglang/pull/47476)
  [Feat] paged-experts: size the resident experts automatically (#47476)
  _Files: `docs/docs/advanced_features/paged_experts.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/layers/moe/paged_experts/method.py` _+6 more__
- **2026-11-03** [`e7a6c35f38`](https://github.com/sgl-project/sglang/commit/e7a6c35f38) [#47784](https://github.com/sgl-project/sglang/pull/47784)
  [Fix] moe: Revert the JIT rewrite of `moe_finalize_fuse_shared` (#47784) (#47994)
  _Files: `python/sglang/kernels/jit/csrc/moe/moe_finalize_fuse_shared.cu`, `python/sglang/kernels/jit/csrc/moe/moe_finalize_fuse_shared.cuh`, `python/sglang/kernels/ops/moe/moe_finalize_fuse_shared.py`, `test/registered/kernels/benchmark/moe/bench_moe_finalize_fuse_shared.py` _+1 more__
- **2026-11-02** [`c927e7c394`](https://github.com/sgl-project/sglang/commit/c927e7c394) [#47989](https://github.com/sgl-project/sglang/pull/47989)
  [CI] test: Relax bs=1 perf limits for CI hosts with slower CPUs (#47989)
  _Files: `test/registered/dllm/test_dllm_batching_fdfo.py`, `test/registered/moe/test_torch_compile_moe.py`_
- **2026-11-02** [`582168dd7c`](https://github.com/sgl-project/sglang/commit/582168dd7c) [#47687](https://github.com/sgl-project/sglang/pull/47687)
  [CI] moe: Give the NVFP4 non-gated Marlin MoE test bf16-sized headroom (#47687)
  _Files: `test/registered/kernels/ops/moe/test_moe_wna16_marlin.py`_
- **2026-11-02** [`c35f89fc9a`](https://github.com/sgl-project/sglang/commit/c35f89fc9a) [#38719](https://github.com/sgl-project/sglang/pull/38719)
  [Fix] moe: Preserve FP32 router precision across model gates (#38719)
  _Files: `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/ernie4.py`, `python/sglang/srt/models/kimi_linear.py` _+1 more__
- **2026-11-02** [`a133231d31`](https://github.com/sgl-project/sglang/commit/a133231d31) [#47782](https://github.com/sgl-project/sglang/pull/47782)
  [Refactor] kernels: Centralize GPU architecture queries in sglang.kernels.arch (#47782)
  _Files: `python/sglang/kernels/README.md`, `python/sglang/kernels/arch/__init__.py`, `python/sglang/kernels/arch/_cuda.py`, `python/sglang/kernels/arch/_hip.py` _+92 more__
- **2026-11-02** [`d74749b0b6`](https://github.com/sgl-project/sglang/commit/d74749b0b6) [#47574](https://github.com/sgl-project/sglang/pull/47574)
  [Feat] [NPU] eplb: Enable dynamic expert load balancing on Ascend (#47574)
  _Files: `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/eplb/expert_location_updater.py`, `python/sglang/srt/hardware_backend/npu/eplb.py`_
- **2026-11-02** [`806d8634a3`](https://github.com/sgl-project/sglang/commit/806d8634a3) [#44974](https://github.com/sgl-project/sglang/pull/44974)
  [Fix] moe: Avoid stale prefix reads in ep_scatter (#44974)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `test/registered/kernels/ops/moe/test_ep_scatter.py`_
- **2026-11-02** [`7cad887d53`](https://github.com/sgl-project/sglang/commit/7cad887d53) [#42654](https://github.com/sgl-project/sglang/pull/42654)
  [Perf] moe: Enable deferred finalize for NVFP4 on the routed TRT-LLM runner (#42654)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/models/deepseek_v2.py`, `test/registered/unit/models/test_deepseek_v4_amd_tp4.py`_
- **2026-11-02** [`f6127bf96e`](https://github.com/sgl-project/sglang/commit/f6127bf96e) [#41639](https://github.com/sgl-project/sglang/pull/41639)
  [Feat] [AMD] moe: Add native GLM MXFP4 Triton Gluon backend (#41639)
  _Files: `python/sglang/kernels/ops/moe/gluon_moe_gfx950/__init__.py`, `python/sglang/kernels/ops/moe/gluon_moe_gfx950/fused_moe_tp4_m128_4192.py`, `python/sglang/kernels/ops/moe/gluon_moe_gfx950/fused_moe_tp4_m16769_32768_shared.py`, `python/sglang/kernels/ops/moe/gluon_moe_gfx950/fused_moe_tp4_m1_16.py` _+22 more__
- **2026-11-02** [`e0c7992d0d`](https://github.com/sgl-project/sglang/commit/e0c7992d0d) [#45332](https://github.com/sgl-project/sglang/pull/45332)
  [Fix] [AMD] quark: Load MXFP4 MoE checkpoints on gfx95 and gfx1250 without SGLANG_USE_AITER (#45332)
  _Files: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/unit/layers/quantization/test_quark_config.py`_
- **2026-11-02** [`8319febb08`](https://github.com/sgl-project/sglang/commit/8319febb08) [#47653](https://github.com/sgl-project/sglang/pull/47653)
  [Perf] kimi-k3: Seed a validated FlashInfer prefill MoE tactic (#47653)
  _Files: `python/sglang/srt/layers/moe/configs/kimi_k3_sm103_fi072_prefill.json`, `python/sglang/srt/layers/moe/flashinfer_kimi_k3_tactics.py`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`, `test/registered/unit/layers/moe/test_kimi_k3_prefill_tactics.py` _+1 more__
- **2026-11-02** [`cec4554871`](https://github.com/sgl-project/sglang/commit/cec4554871) [#47742](https://github.com/sgl-project/sglang/pull/47742)
  [Fix] kimi-k3: Honor initial expert placement in fused routing (#47742)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/kernels/ops/moe/test_moe_front.py`, `test/registered/unit/layers/moe/test_topk_routing_inputs.py` _+1 more__
- **2026-11-02** [`572d3dc3f1`](https://github.com/sgl-project/sglang/commit/572d3dc3f1) [#47211](https://github.com/sgl-project/sglang/pull/47211)
  [Refactor] [NPU] quant: Refactor shared quantization utilities and DSpark weight mapping (#47211)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/block_fp8_moe.py`, `python/sglang/srt/hardware_backend/npu/quantization/dtype_utils.py`, `python/sglang/srt/hardware_backend/npu/quantization/fp4_moe_methods.py`, `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py` _+10 more__
- **2026-11-02** [`ca819c11cd`](https://github.com/sgl-project/sglang/commit/ca819c11cd) [#47784](https://github.com/sgl-project/sglang/pull/47784)
  [Perf] [NVIDIA] moe: Rewrite moe_finalize_fuse_shared as a JIT kernel with all top-k gathers in flight (#47784)
  _Files: `python/sglang/kernels/jit/csrc/moe/moe_finalize_fuse_shared.cu`, `python/sglang/kernels/jit/csrc/moe/moe_finalize_fuse_shared.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/math.cuh`, `python/sglang/kernels/ops/moe/moe_finalize_fuse_shared.py` _+2 more__
- **2026-11-02** [`22e6ff7aca`](https://github.com/sgl-project/sglang/commit/22e6ff7aca) [#45089](https://github.com/sgl-project/sglang/pull/45089)
  [Perf] [NVIDIA] fused_moe: Add H20 configs for GLM-5.3-Flash TP8/TP4 (#45089)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=288,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=288,N=512,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=289,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=289,N=512,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`_
- **2026-11-02** [`61d2005421`](https://github.com/sgl-project/sglang/commit/61d2005421) [#45200](https://github.com/sgl-project/sglang/pull/45200)
  [Fix] humming: Free replaced MoE weights after each sublayer transform (#45200)
  _Files: `python/sglang/srt/layers/quantization/humming.py`, `python/sglang/srt/layers/quantization/humming_utils.py`, `test/registered/unit/layers/quantization/test_humming_moe_release_replaced.py`_

## Multimodal  (61 commits)

- **2026-11-09** [`4373137b6f`](https://github.com/sgl-project/sglang/commit/4373137b6f) [#49020](https://github.com/sgl-project/sglang/pull/49020)
  [CI] diffusion: Add H100 computable runner baselines for loading and E2E (#49020)
  _Files: `python/sglang/multimodal_gen/test/runner/PERFORMANCE.md`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/server/testcase_configs.py`, `python/sglang/multimodal_gen/test/unit/test_runner_perf_baselines.py`_
- **2026-11-09** [`50dcb7fcc1`](https://github.com/sgl-project/sglang/commit/50dcb7fcc1) [#46050](https://github.com/sgl-project/sglang/pull/46050)
  [Doc] diffusion: Fix documented snippets that cannot load a model (#46050)
  _Files: `docs/cookbook/diffusion/LongLive/LongLive-2.0.mdx`, `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/.claude/CLAUDE.md`_
- **2026-11-09** [`78dd7d444f`](https://github.com/sgl-project/sglang/commit/78dd7d444f) [#49237](https://github.com/sgl-project/sglang/pull/49237)
  [Fix] CI: Avoid coverage fail-fast cycles on diffusion reruns (#49237)
  _Files: `.github/actions/check-pr-test-health/action.yml`_
- **2026-11-09** [`0958198e6a`](https://github.com/sgl-project/sglang/commit/0958198e6a) [#45203](https://github.com/sgl-project/sglang/pull/45203)
  [Fix] multimodal: Compact CPU tensor views before inline transport (#45203)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `test/registered/unit/multimodal/test_mm_inline_storage.py`_
- **2026-11-09** [`64c8f51a4a`](https://github.com/sgl-project/sglang/commit/64c8f51a4a) [#48790](https://github.com/sgl-project/sglang/pull/48790)
  [Fix] [Intel] ci/xeon: Build image from the checked-out revision (#48790)
  _Files: `.github/workflows/pr-test-xeon.yml`, `docker/xeon.Dockerfile`_
- **2026-11-09** [`bfe8e9743b`](https://github.com/sgl-project/sglang/commit/bfe8e9743b) [#49163](https://github.com/sgl-project/sglang/pull/49163)
  [Doc] skills: Add a code-cleanup skill cataloging refactor and cleanup patterns (#49163)
  _Files: `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/code-cleanup/SKILL.md`, `.agents/skills/code-cleanup/patterns.md`, `.agents/skills/env-var-conventions/SKILL.md` _+2 more__
- **2026-11-09** [`6bee4db4af`](https://github.com/sgl-project/sglang/commit/6bee4db4af) [#48281](https://github.com/sgl-project/sglang/pull/48281)
  [Perf] diffusion/helios: Keep timestep conditioning compact (#48281)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/helios.py`_
- **2026-11-09** [`c9bf5c37dd`](https://github.com/sgl-project/sglang/commit/c9bf5c37dd) [#48383](https://github.com/sgl-project/sglang/pull/48383)
  [Perf] diffusion: reuse bit-exact RoPE in HiDream-O1-Image (#48383)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/multimodal_gen/runtime/models/dits/hidream_o1_image.py`, `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-11-08** [`e7909aabf2`](https://github.com/sgl-project/sglang/commit/e7909aabf2) [#49149](https://github.com/sgl-project/sglang/pull/49149)
  [CI] diffusion: Run diffusion lanes through a shared stage and runner configs (#49149)
  _Files: `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/write-sglang-test/SKILL.md`, `.github/workflows/_diffusion-pr-test-stage.yml`, `.github/workflows/_pr-test-check-changes.yml` _+11 more__
- **2026-11-08** [`4003bf1077`](https://github.com/sgl-project/sglang/commit/4003bf1077) [#48800](https://github.com/sgl-project/sglang/pull/48800)
  [Feat] request_logger: Summarize media inputs per modality in request logs (#48800)
  _Files: `python/sglang/srt/observability/request_logger.py`, `rust/sglang-server/src/api_server/core/request_log.rs`, `rust/sglang-server/src/api_server/core/request_log/tests.rs`, `rust/sglang-server/testdata/request_log.json` _+2 more__
- **2026-11-08** [`b966c2798e`](https://github.com/sgl-project/sglang/commit/b966c2798e) [#44955](https://github.com/sgl-project/sglang/pull/44955)
  [Feat] diffusion: Support multiple dynamic LoRA adapters (#44955)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/README.md`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/base.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/nodes.py`, `python/sglang/multimodal_gen/runtime/layers/lora/linear.py` _+4 more__
- **2026-11-08** [`e5739babc1`](https://github.com/sgl-project/sglang/commit/e5739babc1) [#49154](https://github.com/sgl-project/sglang/pull/49154)
  [CI] xeon: Prune dangling docker images and check free disk before the build (#49154)
  _Files: `.github/workflows/pr-test-xeon.yml`_
- **2026-11-08** [`46e296e628`](https://github.com/sgl-project/sglang/commit/46e296e628) [#48688](https://github.com/sgl-project/sglang/pull/48688)
  [Perf] longcat-image: Reuse timestep conditioning for serial CFG (#48688)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/longcat_image.py`, `test/registered/kernels/ops/diffusion/test_longcat_modulation_cache.py`_
- **2026-11-08** [`ef394d57e4`](https://github.com/sgl-project/sglang/commit/ef394d57e4) [#47090](https://github.com/sgl-project/sglang/pull/47090)
  [Perf] qwen-image21: Pack BF16 gate/up projections on SM120 (#47090)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image21.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py`, `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-11-08** [`b3aec080c2`](https://github.com/sgl-project/sglang/commit/b3aec080c2) [#46430](https://github.com/sgl-project/sglang/pull/46430)
  [Fix] diffusion/flux3: Make TP and SP ranks agree on sequential CFG (#46430)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/flux3_image.py`, `python/sglang/multimodal_gen/test/unit/test_flux3_image_stages.py`_
- **2026-11-08** [`b7ccc7e2f9`](https://github.com/sgl-project/sglang/commit/b7ccc7e2f9) [#48122](https://github.com/sgl-project/sglang/pull/48122)
  [Perf] diffusion: Cache MiniMax-H3 reference and keyframe rows per image (#48122)
  _Files: `python/sglang/multimodal_gen/runtime/cache/conditioning.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/keyframe_encoding.py`, `python/sglang/multimodal_gen/test/unit/test_conditioning_cache.py`_
- **2026-11-08** [`19f55e6f2e`](https://github.com/sgl-project/sglang/commit/19f55e6f2e) [#48218](https://github.com/sgl-project/sglang/pull/48218)
  [Perf] diffusion: Enable image-prefix sequence parallelism for ERNIE-Image (#48218)
  _Files: `docs/cookbook/diffusion/Ernie-Image/Ernie-Image.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/ernie_image.py`, `python/sglang/multimodal_gen/runtime/models/dits/ernie_image.py`, `python/sglang/multimodal_gen/test/unit/test_ernie_image_parallel.py` _+1 more__
- **2026-11-08** [`0f3b2b0259`](https://github.com/sgl-project/sglang/commit/0f3b2b0259) [#48442](https://github.com/sgl-project/sglang/pull/48442)
  [Perf] diffusion: Accelerate exact SANA-Video RoPE on SM103 (#48442)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/interleaved_rope_fp64.cuh`, `test/registered/kernels/ops/diffusion/test_interleaved_rope_fp64.py`_
- **2026-11-08** [`4c2670f0cc`](https://github.com/sgl-project/sglang/commit/4c2670f0cc) [#48394](https://github.com/sgl-project/sglang/pull/48394)
  [Perf] diffusion: Fuse Anima gated residuals during BCG capture (#48394)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/multimodal_gen/runtime/models/dits/anima.py`, `python/sglang/multimodal_gen/test/unit/test_anima_cuda.py`_
- **2026-11-07** [`9e10f79ac7`](https://github.com/sgl-project/sglang/commit/9e10f79ac7) [#49023](https://github.com/sgl-project/sglang/pull/49023)
  [Feat] rust-server: Log requests as JSON lines and to log directories, and log OpenAI requests as received (#49023)
  _Files: `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/rust_server/server.py`, `rust/sglang-server/src/api_server/core.rs` _+13 more__
- **2026-11-07** [`391f4e6f17`](https://github.com/sgl-project/sglang/commit/391f4e6f17) [#49087](https://github.com/sgl-project/sglang/pull/49087)
  [Doc] [AMD] cookbook: Update Muse Spark Open MI355X AgentX recipe to the 1106 image (#49087)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`_
- **2026-11-07** [`c3c292b65a`](https://github.com/sgl-project/sglang/commit/c3c292b65a) [#49006](https://github.com/sgl-project/sglang/pull/49006)
  [Feat] rust-server: Pass the image item detail hint to multimodal processors (#49006)
  _Files: `rust/sglang-server/src/api_server/core/request_log.rs`, `rust/sglang-server/src/api_server/core/request_log/tests.rs`, `rust/sglang-server/src/message/multimodal.rs`, `rust/sglang-server/src/message/wire.rs` _+1 more__
- **2026-11-07** [`ba5906471c`](https://github.com/sgl-project/sglang/commit/ba5906471c) [#43886](https://github.com/sgl-project/sglang/pull/43886)
  [Fix] VLM: Preserve empty media in parallel sampling (#43886)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/multimodal/mm_utils.py`, `test/registered/unit/managers/test_io_struct.py`_
- **2026-11-07** [`88d8ef144f`](https://github.com/sgl-project/sglang/commit/88d8ef144f) [#48903](https://github.com/sgl-project/sglang/pull/48903)
  [Test] kandinsky6-sr: Check spatial-shard decode exactly in fp32 and with a calibrated bf16 outlier budget (#48903)
  _Files: `python/sglang/multimodal_gen/test/unit/test_kandinsky6_sr_decode_parallel.py`_
- **2026-11-07** [`06a7c9a397`](https://github.com/sgl-project/sglang/commit/06a7c9a397) [#48515](https://github.com/sgl-project/sglang/pull/48515)
  [Fix] rust-server: Freeze the scheduler's garbage collector after the startup warmup (#48515)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/rust_server/config.py`, `rust/sglang-server/src/api_server/handlers/control.rs`, `rust/sglang-server/src/api_server/http/app.rs` _+10 more__
- **2026-11-07** [`18256b2b19`](https://github.com/sgl-project/sglang/commit/18256b2b19) [#48512](https://github.com/sgl-project/sglang/pull/48512)
  [Feat] rust-server: Refuse ignored flags, enforce API keys, exit on a failed warmup, declare the SSE charset (#48512)
  _Files: `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/arg_groups/resolution_hooks.py`, `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/entrypoints/http_server.py` _+27 more__
- **2026-11-07** [`278fd8382f`](https://github.com/sgl-project/sglang/commit/278fd8382f) [#48457](https://github.com/sgl-project/sglang/pull/48457)
  [Feat] rust-server: Write --crash-dump-folder dumps from the Rust frontend (#48457)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/observability/request_dump.py` _+23 more__
- **2026-11-07** [`bdbc93c2dc`](https://github.com/sgl-project/sglang/commit/bdbc93c2dc) [#48455](https://github.com/sgl-project/sglang/pull/48455)
  [Feat] rust-server: Log requests like the Python server (#48455)
  _Files: `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/rust_server/server.py`, `rust/sglang-server/src/api_server/core.rs` _+28 more__
- **2026-11-07** [`2099ebfd12`](https://github.com/sgl-project/sglang/commit/2099ebfd12) [#49032](https://github.com/sgl-project/sglang/pull/49032)
  [Fix] scheduler: Relay multimodal requests to later PP stages without raw features (#49032)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/registered/unit/managers/test_mm_shm_error_consensus.py`_
- **2026-11-07** [`bfab0abd4a`](https://github.com/sgl-project/sglang/commit/bfab0abd4a) [#48801](https://github.com/sgl-project/sglang/pull/48801)
  [Feat] sgl-router: Log per-request image, video and audio counts in the access log (#48801)
  _Files: `sgl-router/src/server/app.rs`, `sgl-router/src/server/grpc.rs`, `sgl-router/src/server/metrics.rs`, `sgl-router/src/server/routes/chat/forward.rs` _+1 more__
- **2026-11-06** [`91d8dd4ab1`](https://github.com/sgl-project/sglang/commit/91d8dd4ab1) [#46291](https://github.com/sgl-project/sglang/pull/46291)
  [Feat] rust-server: multimodal (image) preprocessing through sglang-processor (#46291)
  _Files: `.agents/skills/processor-mm-parity/SKILL.md`, `.agents/skills/processor-model-parity/SKILL.md`, `.claude/rules/modify-component-must-read.md`, `.gitignore` _+41 more__
- **2026-11-06** [`c6ea17c837`](https://github.com/sgl-project/sglang/commit/c6ea17c837) [#48752](https://github.com/sgl-project/sglang/pull/48752)
  [Fix] rust-server: Publish 127.0.0.1 for an IPv6 loopback SGLANG_HOST_IP on an IPv4 wildcard bind (#48752)
  _Files: `python/sglang/srt/rust_server/server.py`, `test/registered/unit/multimodal/rust/shared/test_rust_server_extension.py`_
- **2026-11-06** [`0e8fca50fe`](https://github.com/sgl-project/sglang/commit/0e8fca50fe) [#48619](https://github.com/sgl-project/sglang/pull/48619)
  [CI] test: Give TestLlavaServer's llava preprocessing more time (#48619)
  _Files: `python/sglang/test/vlm_utils.py`, `test/registered/vlm/test_vision_openai_server_a.py`_
- **2026-11-06** [`944549cb53`](https://github.com/sgl-project/sglang/commit/944549cb53) [#48366](https://github.com/sgl-project/sglang/pull/48366)
  [Refactor] kernels/diffusion/tests: Prune new dead code and make silently skipped tests run (#48366)
- **2026-11-06** [`3173a999fe`](https://github.com/sgl-project/sglang/commit/3173a999fe) [#47724](https://github.com/sgl-project/sglang/pull/47724)
  [Perf] diffusion: qknorm_complex_rope keeps two Q/K rows in flight per half-warp (#47724)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_complex_rope.cuh`_
- **2026-11-06** [`76c3cef33f`](https://github.com/sgl-project/sglang/commit/76c3cef33f) [#48755](https://github.com/sgl-project/sglang/pull/48755)
  [Chore] utils: Guard `srt.utils` imports and remove dead code (#48755)
  _Files: `.pre-commit-config.yaml`, `python/sglang/srt/managers/embed_types.py`, `python/sglang/srt/utils/common.py`, `python/sglang/srt/utils/cuda_ipc_transport_utils.py` _+12 more__
- **2026-11-06** [`858073e4f6`](https://github.com/sgl-project/sglang/commit/858073e4f6) [#48722](https://github.com/sgl-project/sglang/pull/48722)
  [CI] [AMD] nightly-disagg: Install the checkout's runtime deps over the image (#48722)
  _Files: `scripts/ci/slurm/launch_mi355x.sh`_
- **2026-11-05** [`d5a1b615a5`](https://github.com/sgl-project/sglang/commit/d5a1b615a5) [#48604](https://github.com/sgl-project/sglang/pull/48604)
  [CI] [NPU] npu: Switch precision test selection to lb-actions/precision-test (#48604)
  _Files: `.github/workflows/pr-test-npu.yml`, `scripts/ci/npu/precise-test/bucket_recommended_tests.py`, `scripts/ci/npu/precise-test/list_multimodal_tests.py`, `scripts/ci/npu/precise-test/test_selector.py`_
- **2026-11-05** [`92a6910ef2`](https://github.com/sgl-project/sglang/commit/92a6910ef2) [#47907](https://github.com/sgl-project/sglang/pull/47907)
  [Perf] diffusion: Avoid upscaling native H3 references by default (#47907)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx`, `python/sglang/multimodal_gen/configs/sample/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/constants.py` _+4 more__
- **2026-11-05** [`293bfdbead`](https://github.com/sgl-project/sglang/commit/293bfdbead) [#47442](https://github.com/sgl-project/sglang/pull/47442)
  [Fix] diffusion: Build the Cosmos 3 RoPE table on GPU so CPU offload gives the same output (#47442)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/test/unit/test_cosmos3.py`_
- **2026-11-05** [`169c88be12`](https://github.com/sgl-project/sglang/commit/169c88be12) [#45717](https://github.com/sgl-project/sglang/pull/45717)
  [Feat] [Intel] CPU-core-binding: Support Compute Building Block for next Gen Xeon (#45717)
  _Files: `docs/docs/hardware-platforms/cpu_server.mdx`, `python/sglang/multimodal_gen/runtime/managers/cpu_worker.py`, `python/sglang/srt/utils/common.py`, `python/sglang/srt/utils/numa_utils.py` _+1 more__
- **2026-11-05** [`e9564cb360`](https://github.com/sgl-project/sglang/commit/e9564cb360) [#48075](https://github.com/sgl-project/sglang/pull/48075)
  [Perf] Hunyuan3D: Reduce redundant QEM quadric accumulation (#48075)
  _Files: `python/sglang/multimodal_gen/runtime/utils/mesh3d_utils.py`, `python/sglang/multimodal_gen/test/unit/test_hunyuan3d_native_texture_models.py`_
- **2026-11-05** [`348e87e90a`](https://github.com/sgl-project/sglang/commit/348e87e90a) [#48256](https://github.com/sgl-project/sglang/pull/48256)
  [CI] diffusion: Add the B200 baseline override for b200-cirrascale2 (#48256)
  _Files: `python/sglang/multimodal_gen/test/runner/PERFORMANCE.md`, `python/sglang/multimodal_gen/test/server/perf_baselines/b200.json`, `python/sglang/multimodal_gen/test/unit/test_runner_perf_baselines.py`_
- **2026-11-04** [`7c8ada7ec6`](https://github.com/sgl-project/sglang/commit/7c8ada7ec6) [#47235](https://github.com/sgl-project/sglang/pull/47235)
  [Fix] multimodal: Share typed identities for Kimi prepared inputs (#47235)
  _Files: `python/sglang/srt/multimodal/processors/kimi_common.py`, `test/registered/unit/models/test_kimi_k25.py`, `test/registered/unit/multimodal/test_kimi_image_identity.py`_
- **2026-11-04** [`a73010b648`](https://github.com/sgl-project/sglang/commit/a73010b648) [#48176](https://github.com/sgl-project/sglang/pull/48176)
  [CI] rerun-test: Retry diffusion reruns like the multimodal-gen CI (#48176)
  _Files: `.github/workflows/rerun-test.yml`_
- **2026-11-04** [`a29ed2745c`](https://github.com/sgl-project/sglang/commit/a29ed2745c) [#46443](https://github.com/sgl-project/sglang/pull/46443)
  [Fix] diffusion: Fix rollout conditioning and scalar weight checksums (#46443)
  _Files: `python/sglang/multimodal_gen/runtime/post_training/tensor_update_checker.py`, `python/sglang/multimodal_gen/test/unit/test_multi_output_rollout_trajectory.py`, `python/sglang/multimodal_gen/test/unit/test_weight_utils.py`_
- **2026-11-03** [`cbb7ec4120`](https://github.com/sgl-project/sglang/commit/cbb7ec4120) [#47186](https://github.com/sgl-project/sglang/pull/47186)
  [Fix] diffusion: Preserve FP32 product rounding in Anima RoPE (#47186)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/rope/rope_rotate_half_fp32.py`_
- **2026-11-03** [`5845c0da6c`](https://github.com/sgl-project/sglang/commit/5845c0da6c) [#47962](https://github.com/sgl-project/sglang/pull/47962)
  [CI] diffusion: Refresh the LTX-2 two-stage runtime VRAM baseline for the cached prompt K/V (#47962)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`_
- **2026-11-03** [`f77064f635`](https://github.com/sgl-project/sglang/commit/f77064f635) [#47971](https://github.com/sgl-project/sglang/pull/47971)
  [CI] [AMD] diffusion/minimax-h3: Skip the group-attend contract test on ROCm (#47971)
  _Files: `python/sglang/multimodal_gen/test/unit/test_minimax_h3_dit_contract.py`_
- **2026-11-03** [`63c6de2eda`](https://github.com/sgl-project/sglang/commit/63c6de2eda) [#47587](https://github.com/sgl-project/sglang/pull/47587)
  [Doc] diffusion: Set measured cookbook defaults for MiniMax-H3, FastH3 Omni, MOSS-Image and Qwen-Image-2.1 (#47587)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx`, `docs/src/snippets/configs/OpenMOSS/moss-image.jsx` _+1 more__
- **2026-11-03** [`11d687870f`](https://github.com/sgl-project/sglang/commit/11d687870f) [#46947](https://github.com/sgl-project/sglang/pull/46947)
  [CI] [AMD] diffusion/flux3: Make exact-quality VAE convolutions deterministic on ROCm (#46947)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/flux3_image.py`, `python/sglang/multimodal_gen/test/unit/test_flux3_image_stages.py`_
- **2026-11-03** [`825f8f6b89`](https://github.com/sgl-project/sglang/commit/825f8f6b89) [#47292](https://github.com/sgl-project/sglang/pull/47292)
  [Perf] diffusion: Fuse SANA-Video depthwise convolution and GLU on SM120 (#47292)
  _Files: `python/sglang/kernels/kda_kernels/sana_depthwise_glu_triton.py`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/multimodal_gen/runtime/models/dits/sana_video.py` _+1 more__
- **2026-11-03** [`7f878d7c8c`](https://github.com/sgl-project/sglang/commit/7f878d7c8c) [#46580](https://github.com/sgl-project/sglang/pull/46580)
  Revert "[Feat] diffusion/model: add the BRIA Fibo 2.0 transformer and text conditioning (#46580)" (#48054)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/bria_fibo2.py`, `python/sglang/multimodal_gen/configs/models/encoders/bria_fibo2.py`, `python/sglang/multimodal_gen/runtime/models/dits/bria_fibo2.py`, `python/sglang/multimodal_gen/test/unit/test_bria_fibo2.py` _+2 more__
- **2026-11-02** [`114675a0d1`](https://github.com/sgl-project/sglang/commit/114675a0d1) [#47852](https://github.com/sgl-project/sglang/pull/47852)
  [Perf] diffusion: Fuse MiniMax-H3 encoder SiLU and padding (#47852)
  _Files: `python/sglang/kernels/kda_kernels/silu_temporal_pad.py`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/conv.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/norm.py` _+2 more__
- **2026-11-02** [`d2d3632ae0`](https://github.com/sgl-project/sglang/commit/d2d3632ae0) [#46905](https://github.com/sgl-project/sglang/pull/46905)
  [Perf] Hunyuan3D: Speed up shape export with GPU-side grid generation (#46905)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/hunyuan3d_vae.py`, `test/registered/unit/multimodal_gen/test_hunyuan3d_gpu_grid.py`_
- **2026-11-02** [`669292bacc`](https://github.com/sgl-project/sglang/commit/669292bacc) [#47835](https://github.com/sgl-project/sglang/pull/47835)
  [Test] diffusion: align warmup and LoRA fixtures with runtime contracts (#47835)
  _Files: `python/sglang/multimodal_gen/test/unit/test_cfg_parallel_warmup.py`, `python/sglang/multimodal_gen/test/unit/test_fused_lora_compose.py`_
- **2026-11-02** [`180e7a154a`](https://github.com/sgl-project/sglang/commit/180e7a154a) [#46580](https://github.com/sgl-project/sglang/pull/46580)
  [Feat] diffusion/model: add the BRIA Fibo 2.0 transformer and text conditioning (#46580)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/bria_fibo2.py`, `python/sglang/multimodal_gen/configs/models/encoders/bria_fibo2.py`, `python/sglang/multimodal_gen/runtime/models/dits/bria_fibo2.py`, `python/sglang/multimodal_gen/test/unit/test_bria_fibo2.py` _+2 more__
- **2026-11-02** [`6aca419807`](https://github.com/sgl-project/sglang/commit/6aca419807) [#39682](https://github.com/sgl-project/sglang/pull/39682)
  [Feat] diffusion/model: support HiDream-O1-Image (#39682)
  _Files: `docs/cookbook/diffusion/HiDream/HiDream-O1-Image.mdx`, `docs/docs.json`, `docs/src/snippets/configs/HiDream/hidream-o1-image.jsx`, `docs/src/snippets/diffusion/model-catalog.jsx` _+10 more__
- **2026-11-02** [`22e7897f95`](https://github.com/sgl-project/sglang/commit/22e7897f95) [#43865](https://github.com/sgl-project/sglang/pull/43865)
  [Fix] tokenizer_manager: Prevent scheduler crash and has_audio_understanding misreport for audio-declaring models without an audio tower (#43865)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/configs/test_model_config.py`, `test/registered/unit/managers/test_tokenizer_manager_audio_rejection.py`_
- **2026-11-02** [`a58735064e`](https://github.com/sgl-project/sglang/commit/a58735064e) [#41768](https://github.com/sgl-project/sglang/pull/41768)
  [Fix] multimodal: Keep every image, video and audio of a request when n > 1 (#41768)
  _Files: `python/sglang/srt/managers/io_struct.py`, `test/registered/unit/managers/test_io_struct.py`_
- **2026-11-02** [`0c29b0b9f9`](https://github.com/sgl-project/sglang/commit/0c29b0b9f9) [#46956](https://github.com/sgl-project/sglang/pull/46956)
  [Perf] Hunyuan3D: Skip redundant OBJ exports when generating GLB (#46956)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/hunyuan3d/paint.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/hunyuan3d/shape.py`_

## KV Cache / Memory  (33 commits)

- **2026-11-09** [`dfaca5681d`](https://github.com/sgl-project/sglang/commit/dfaca5681d) [#46934](https://github.com/sgl-project/sglang/pull/46934)
  [Fix] hicache: Restore sub-window SWA L3 hits under a mid-tree anchor (#46934)
  _Files: `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa.py`, `python/sglang/srt/mem_cache/unified_cache/storage_attachment.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+4 more__
- **2026-11-09** [`60d8d1f8e4`](https://github.com/sgl-project/sglang/commit/60d8d1f8e4) [#48786](https://github.com/sgl-project/sglang/pull/48786)
  [Feat] HiCache: add tma copy kernel for unified layout (#48786)
  _Files: `python/sglang/kernels/jit/csrc/kvcacheio/hicache_tma.cuh`, `python/sglang/kernels/ops/kvcache/hicache.py`, `test/registered/kernels/ops/kvcache/test_hicache_page_unified_tma.py`_
- **2026-11-09** [`2cbb66f563`](https://github.com/sgl-project/sglang/commit/2cbb66f563) [#48012](https://github.com/sgl-project/sglang/pull/48012)
  [Refactor] mem_cache: Plan, admit and reclaim unified memory through one layout search (#48012)
- **2026-11-09** [`6ea644d6ce`](https://github.com/sgl-project/sglang/commit/6ea644d6ce) [#48011](https://github.com/sgl-project/sglang/pull/48011)
  [Refactor] mem_cache: Add a layout planner and request demand for the unified chain (#48011)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` _+10 more__
- **2026-11-09** [`7455745a5a`](https://github.com/sgl-project/sglang/commit/7455745a5a) [#48010](https://github.com/sgl-project/sglang/pull/48010)
  [Refactor] mem_cache: Give unified request rows one lifecycle state and one reset (#48010)
  _Files: `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/mem_cache/kv/requests.py`, `python/sglang/srt/mem_cache/kv/storage.py`, `python/sglang/srt/mem_cache/static_kv_storage.py` _+5 more__
- **2026-11-09** [`ae58fe775d`](https://github.com/sgl-project/sglang/commit/ae58fe775d) [#46610](https://github.com/sgl-project/sglang/pull/46610)
  [Feat] [Intel] mem_cache: Enable the HiCache Mamba host pool on XPU (#46610)
  _Files: `python/sglang/srt/mem_cache/pool_host/_kvcacheio.py`, `python/sglang/srt/mem_cache/pool_host/mamba.py`, `test/registered/unit/mem_cache/test_hicache_kvcacheio_gate.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py` _+1 more__
- **2026-11-09** [`88deca9f5f`](https://github.com/sgl-project/sglang/commit/88deca9f5f) [#49207](https://github.com/sgl-project/sglang/pull/49207)
  [Fix] session: Defer a session close while an unfinished turn still reads its media (#49207)
  _Files: `python/sglang/srt/session/session_controller.py`, `test/registered/unit/mem_cache/test_session_token_share_unit.py`_
- **2026-11-09** [`eb6cbd046d`](https://github.com/sgl-project/sglang/commit/eb6cbd046d) [#49204](https://github.com/sgl-project/sglang/pull/49204)
  [Refactor] session: Remove the replace session parameter and the turn tree it pruned (#49204)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/session/session_controller.py`, `python/sglang/srt/session/streaming_session.py`, `python/sglang/test/kits/streaming_session_kit.py` _+2 more__
- **2026-11-08** [`fcb3274646`](https://github.com/sgl-project/sglang/commit/fcb3274646) [#48007](https://github.com/sgl-project/sglang/pull/48007)
  [Refactor] mem_cache: Address prefix-tree window slots, cursors and evictions by sub-pool name (#48007)
- **2026-11-08** [`c2a2958900`](https://github.com/sgl-project/sglang/commit/c2a2958900) [#46425](https://github.com/sgl-project/sglang/pull/46425)
  [Refactor] diffusion: Move the Nomas segment KV cache under layers/kvcache (#46425)
  _Files: `python/sglang/multimodal_gen/runtime/layers/kvcache/nomas_segment_cache.py`, `python/sglang/multimodal_gen/runtime/models/dits/nomas.py`, `python/sglang/multimodal_gen/runtime/models/vaes/nomas.py`, `python/sglang/multimodal_gen/test/unit/test_nomas.py` _+1 more__
- **2026-11-07** [`1c8740ecfc`](https://github.com/sgl-project/sglang/commit/1c8740ecfc) [#49034](https://github.com/sgl-project/sglang/pull/49034)
  [Fix] hicache: Return int page slots from `_storage_page_index` without DCP (#49034)
  _Files: `python/sglang/srt/mem_cache/pool_host/base.py`, `test/registered/unit/mem_cache/test_hicache_dcp_host_pool.py`_
- **2026-11-07** [`bcd5ec1195`](https://github.com/sgl-project/sglang/commit/bcd5ec1195) [#48988](https://github.com/sgl-project/sglang/pull/48988)
  [Fix] radix-cache: Use Rust TreeCore with PyTorch 2.15 in the cu134 image instead of slow python backend (#48988)
  _Files: `docker/Dockerfile.cu134`, `python/sglang/srt/rust_extensions/torch_build.py`, `test/registered/rust/test_rust_extension.py`, `test/registered/unit/mem_cache/test_tree_core_registry.py`_
- **2026-11-07** [`784cffe3d9`](https://github.com/sgl-project/sglang/commit/784cffe3d9) [#47984](https://github.com/sgl-project/sglang/pull/47984)
  [Fix] mem_cache: Chunk MambaPool temporal state copy to avoid OOM spike (#47984)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/mem_cache/test_mamba_unittest.py`_
- **2026-11-07** [`0ced08c3db`](https://github.com/sgl-project/sglang/commit/0ced08c3db) [#47129](https://github.com/sgl-project/sglang/pull/47129)
  [Perf] [NVIDIA] muse-spark: Bound B200 projection dispatch and allocator compilation (#47129)
  _Files: `python/sglang/kernels/ops/communication/muse_spark_all_gather.py`, `python/sglang/kernels/ops/memory/allocator.py`, `python/sglang/kernels/ops/memory/common.py`, `python/sglang/srt/mem_cache/allocation.py` _+7 more__
- **2026-11-07** [`b3a3360bc0`](https://github.com/sgl-project/sglang/commit/b3a3360bc0) [#45886](https://github.com/sgl-project/sglang/pull/45886)
  [Fix] InstantTensor: return load-time GPU memory to the KV cache (#45886)
  _Files: `python/sglang/srt/model_loader/weight_utils.py`, `test/registered/unit/model_loader/test_instanttensor_loader.py`_
- **2026-11-07** [`d873c0a235`](https://github.com/sgl-project/sglang/commit/d873c0a235) [#48507](https://github.com/sgl-project/sglang/pull/48507)
  [Fix] multimodal: Cap receive-time CUDA VMM feature copies per GPU and stage the rest in pinned host memory (#48507)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/host_memory.py`, `python/sglang/srt/multimodal/transport/cuda_vmm.py`, `python/sglang/srt/multimodal/transport/receive_budget.py` _+2 more__
- **2026-11-06** [`c2580a7e1e`](https://github.com/sgl-project/sglang/commit/c2580a7e1e) [#46200](https://github.com/sgl-project/sglang/pull/46200)
  [Fix] swa: Start the SWA KV pool at its first layer under pipeline parallelism (#46200)
  _Files: `python/sglang/srt/mem_cache/swa_memory_pool.py`, `test/registered/unit/mem_cache/test_swa_pool_v_head_dim.py`_
- **2026-11-06** [`a46f54b539`](https://github.com/sgl-project/sglang/commit/a46f54b539) [#47968](https://github.com/sgl-project/sglang/pull/47968)
  [Refactor] multimodal: Share the CUDA VMM chunk copy and let the transport pick its pool class (#47968)
  _Files: `python/sglang/srt/multimodal/transport/cuda_vmm.py`_
- **2026-11-06** [`c52ac8a142`](https://github.com/sgl-project/sglang/commit/c52ac8a142) [#48522](https://github.com/sgl-project/sglang/pull/48522)
  [Fix] hicache: Stop L3 prefetch at the match key limit (#48522)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/common.py`, `test/registered/unit/mem_cache/test_storage_prefetch_span.py`_
- **2026-11-06** [`0bdbad964e`](https://github.com/sgl-project/sglang/commit/0bdbad964e) [#48828](https://github.com/sgl-project/sglang/pull/48828)
  [Refactor] radix-cache: Keep only the read pool names in the Rust `PoolName` (#48828)
  _Files: `rust/sglang-radix-tree/src/python_bindings.rs`, `rust/sglang-radix-tree/src/unified_tree_core.rs`_
- **2026-11-06** [`d5935a8677`](https://github.com/sgl-project/sglang/commit/d5935a8677) [#46175](https://github.com/sgl-project/sglang/pull/46175)
  [CI] rust: Publish sglang-api-types on crates.io (#46175)
  _Files: `.github/workflows/pr-test-rust-workspace.yml`, `.github/workflows/pr-test-sgl-router.yml`, `.github/workflows/release-crate-api-types.yml`, `docker/Dockerfile` _+34 more__
- **2026-11-06** [`7a82e415fd`](https://github.com/sgl-project/sglang/commit/7a82e415fd) [#48450](https://github.com/sgl-project/sglang/pull/48450)
  [Fix] mem_cache: Order lazy unified-pool page reuse after the latest forward (#48450)
  _Files: `python/sglang/srt/mem_cache/kv/alloc/band.py`_
- **2026-11-05** [`a08a6158e0`](https://github.com/sgl-project/sglang/commit/a08a6158e0) [#48734](https://github.com/sgl-project/sglang/pull/48734)
  [Fix] spec: Make per-step draft `out_cache_loc` contiguous for KV writes (#48734)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/speculative/eagle_utils.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/unit/mem_cache/test_physical_write_loc.py`_
- **2026-11-05** [`21683c2fcc`](https://github.com/sgl-project/sglang/commit/21683c2fcc) [#48606](https://github.com/sgl-project/sglang/pull/48606)
  [Refactor] scheduler: Release retracted, paused and chunked-aborted requests through RequestRetirer (#48606)
  _Files: `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py` _+7 more__
- **2026-11-05** [`e838360ffd`](https://github.com/sgl-project/sglang/commit/e838360ffd) [#48421](https://github.com/sgl-project/sglang/pull/48421)
  [Fix] HiCache: Reject partial L3 prefetch allocation for hybrid models (#48421)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/unified_radix_cache/test_unified_radix_cache_storage.py`_
- **2026-11-05** [`95560684da`](https://github.com/sgl-project/sglang/commit/95560684da) [#48443](https://github.com/sgl-project/sglang/pull/48443)
  [CI] test: Give test_vision_chunked_prefill's llava preprocessing more time (#48443)
  _Files: `test/registered/vlm/test_vision_chunked_prefill.py`_
- **2026-11-05** [`93e6b42d8a`](https://github.com/sgl-project/sglang/commit/93e6b42d8a) [#48571](https://github.com/sgl-project/sglang/pull/48571)
  [Fix] mamba: Make the lazy full-pool KL test hold across GPUs (#48571)
  _Files: `test/registered/radix_cache/test_mamba_cache_kl.py`_
- **2026-11-05** [`729d11854b`](https://github.com/sgl-project/sglang/commit/729d11854b) [#44435](https://github.com/sgl-project/sglang/pull/44435)
  [Feat] [NPU] scheduler: align cross-request ViT batching with CUDA and fix NPU graph buffer ownership (#44435)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`, `python/sglang/srt/managers/mm_schedule.py`, `test/registered/chunked_prefill/test_mm_chunked_embedding_unit.py`, `test/registered/npu/vlm_models/test_npu_vit_batching.py` _+1 more__
- **2026-11-05** [`02db1235ac`](https://github.com/sgl-project/sglang/commit/02db1235ac) [#48328](https://github.com/sgl-project/sglang/pull/48328)
  [Fix] mamba: Give a lazy boundary snapshot its own slot instead of overwriting the keep slot (#48328)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/mem_cache/allocation.py` _+9 more__
- **2026-11-04** [`f09b88ee96`](https://github.com/sgl-project/sglang/commit/f09b88ee96) [#48005](https://github.com/sgl-project/sglang/pull/48005)
  [Refactor] mem_cache: Plan draft KV bands by retention lifetime (#48005)
- **2026-11-03** [`d2a536fc53`](https://github.com/sgl-project/sglang/commit/d2a536fc53) [#46930](https://github.com/sgl-project/sglang/pull/46930)
  [Perf] hicache: Wait once per write_back eviction walk, not once per victim (#46930)
  _Files: `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/components/full.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py` _+14 more__
- **2026-11-03** [`1ea5f8c6f7`](https://github.com/sgl-project/sglang/commit/1ea5f8c6f7) [#48125](https://github.com/sgl-project/sglang/pull/48125)
  [Feat] unified_cache: Support MiniMax-M3.1 in the direct external linker (#48125)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `test/registered/unit/mem_cache/test_linker_pool_assembler.py`_
- **2026-11-02** [`3d33971dea`](https://github.com/sgl-project/sglang/commit/3d33971dea) [#46606](https://github.com/sgl-project/sglang/pull/46606)
  [Fix] cache: Roll back host slots when allocation raises (#46606)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/pool_host/group.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py`_

## Triton / Kernels  (27 commits)

- **2026-11-09** [`e60f7e909b`](https://github.com/sgl-project/sglang/commit/e60f7e909b) [#43675](https://github.com/sgl-project/sglang/pull/43675)
  [Fix] Kimi-K3: Fix derived weight buffers across CUDA graph reloads (#43675)
  _Files: `python/sglang/srt/layers/attn_residual.py`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/models/test_kimi_k3_bfa_overlap.py`_
- **2026-11-09** [`e8017bc63b`](https://github.com/sgl-project/sglang/commit/e8017bc63b) [#48364](https://github.com/sgl-project/sglang/pull/48364)
  [Feat] [CPU] model: Support Intern-S2-Mobius models on CPU (#48364)
  _Files: `python/sglang/kernels/aot/csrc/cpu/topk.cpp`, `python/sglang/srt/arg_groups/model_overrides/interns2_mobius.py`, `test/registered/cpu/test_topk.py`_
- **2026-11-09** [`d910efa03a`](https://github.com/sgl-project/sglang/commit/d910efa03a) [#48583](https://github.com/sgl-project/sglang/pull/48583)
  [Feat] [Intel] xpu_kernel: update sglang-kernel-xpu to 0.6.0 (#48583)
  _Files: `python/pyproject_xpu.toml`_
- **2026-11-09** [`05a0d7f192`](https://github.com/sgl-project/sglang/commit/05a0d7f192) [#49160](https://github.com/sgl-project/sglang/pull/49160)
  [Test] gemma4: Stop the AR fusion test from deadlocking on a tolerance miss (#49160)
  _Files: `test/registered/kernels/ops/communication/test_gemma4_ar_fusion.py`_
- **2026-11-07** [`ab7ee0aad3`](https://github.com/sgl-project/sglang/commit/ab7ee0aad3) [#49037](https://github.com/sgl-project/sglang/pull/49037)
  [Test] [NVIDIA] megakernel: Stub the DCP push-combine warmup hook in the runtime test (#49037)
  _Files: `test/registered/unit/kernel_plugins/nvidia/test_megakernel_runtime.py`_
- **2026-11-07** [`bb874848bb`](https://github.com/sgl-project/sglang/commit/bb874848bb) [#48689](https://github.com/sgl-project/sglang/pull/48689)
  [Feat] qwen4-exp: accept HMM devices for the file-backed PLE table (#48689)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/models/qwen4_exp_ple_table.py` _+2 more__
- **2026-11-07** [`81c9980416`](https://github.com/sgl-project/sglang/commit/81c9980416) [#47930](https://github.com/sgl-project/sglang/pull/47930)
  [Feat] [NVIDIA] megakernel: Support prefill and extend steps (#47930)
  _Files: `python/sglang/kernels/plugin_kernels/nvidia/spec.py`, `python/sglang/srt/kernel_plugins/nvidia/binding.py`, `test/registered/unit/kernel_plugins/nvidia/test_megakernel_runtime.py`_
- **2026-11-06** [`39619b87fc`](https://github.com/sgl-project/sglang/commit/39619b87fc) [#47749](https://github.com/sgl-project/sglang/pull/47749)
  [CI] [Intel] ci/xpu: Move remaining XPU CI installs to uv and set SGLANG_IS_IN_CI (#47749)
  _Files: `.github/workflows/nightly-test-intel-wheel.yml`, `.github/workflows/nightly-test-intel.yml`, `.github/workflows/pr-test-xpu.yml`, `.github/workflows/release-whl-kernel-xpu.yml` _+1 more__
- **2026-11-06** [`10be18dcfc`](https://github.com/sgl-project/sglang/commit/10be18dcfc) [#48761](https://github.com/sgl-project/sglang/pull/48761)
  [Perf] mhc: halve the DeepGEMM prenorm slices when the grid overflows one wave (#48761)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`_
- **2026-11-06** [`f9436ef644`](https://github.com/sgl-project/sglang/commit/f9436ef644) [#40139](https://github.com/sgl-project/sglang/pull/40139)
  [Fix] [Intel] cpu-kernel: Fix rope for VLA model (#40139)
  _Files: `python/sglang/kernels/aot/csrc/cpu/rope.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/kernels/aot/csrc/cpu/vec.h`, `python/sglang/srt/layers/rotary_embedding/utils.py` _+1 more__
- **2026-11-06** [`1b5e355a91`](https://github.com/sgl-project/sglang/commit/1b5e355a91) [#48401](https://github.com/sgl-project/sglang/pull/48401)
  [Test] [Intel] jit: Stub tvm_ffi paths in test_jit_cache when tvm_ffi is absent (#48401)
  _Files: `test/registered/unit/kernels/test_jit_cache.py`_
- **2026-11-06** [`e867a9b0b4`](https://github.com/sgl-project/sglang/commit/e867a9b0b4) [#48732](https://github.com/sgl-project/sglang/pull/48732)
  [Fix] gemm: Keep Kimi-K3's tiny GEMM shapes on SIMT at every batch size (#48732)
  _Files: `python/sglang/kernels/ops/gemm/tiny_gemm.py`_
- **2026-11-06** [`b48a3bb4db`](https://github.com/sgl-project/sglang/commit/b48a3bb4db) [#48719](https://github.com/sgl-project/sglang/pull/48719)
  [Fix] docker: update NVIDIA megakernel pin for Qwen3.5 follow-up kernels (#48719)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`_
- **2026-11-05** [`dc65932d2b`](https://github.com/sgl-project/sglang/commit/dc65932d2b) [#48284](https://github.com/sgl-project/sglang/pull/48284)
  [Fix] model_loader: Use the local CUDA device in the fastsafetensors loader (#48284)
  _Files: `python/sglang/srt/model_loader/weight_utils.py`, `test/registered/unit/model_loader/test_prefetch_checkpoints.py`_
- **2026-11-05** [`fe6a8a32fd`](https://github.com/sgl-project/sglang/commit/fe6a8a32fd) [#41108](https://github.com/sgl-project/sglang/pull/41108)
  [Perf] mimo-v2: Optimize router GEMM with the HPC-Ops bf16xfp32 kernel (#41108)
  _Files: `python/sglang/srt/models/mimo_v2.py`, `test/registered/kernels/benchmark/gemm/bench_bf16xfp32_router_gemm.py`, `test/registered/kernels/ops/gemm/test_linear_bf16_fp32_hpc.py`, `test/registered/unit/models/test_mimo_v2_router_hpc_gemm.py`_
- **2026-11-05** [`2270cbc17e`](https://github.com/sgl-project/sglang/commit/2270cbc17e) [#47898](https://github.com/sgl-project/sglang/pull/47898)
  [Perf] [NVIDIA] fused-a-gemm: Relax the CuTe DSL kernel's K alignment from 1024 to 256 (#47898)
  _Files: `python/sglang/kernels/ops/gemm/cutedsl_dsv3_fused_a_gemm.py`, `python/sglang/kernels/ops/gemm/fused_a_gemm.py`, `test/registered/kernels/ops/gemm/test_cutedsl_dsv3_fused_a_gemm.py`, `test/registered/kernels/ops/gemm/test_fused_a_gemm.py`_
- **2026-11-05** [`1eca810385`](https://github.com/sgl-project/sglang/commit/1eca810385) [#48380](https://github.com/sgl-project/sglang/pull/48380)
  [Doc] agent-skills: Add JIT kernel performance guide and document more header-library helpers (#48380)
  _Files: `.agents/skills/add-jit-kernel/SKILL.md`, `.agents/skills/add-jit-kernel/performance-cuda.md`_
- **2026-11-04** [`0170a4e849`](https://github.com/sgl-project/sglang/commit/0170a4e849) [#48352](https://github.com/sgl-project/sglang/pull/48352)
  [Chore] [NPU] deps: Bump kernel and hybrid memory packages (#48352)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `docker/npu.Dockerfile`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-11-04** [`637cc7d195`](https://github.com/sgl-project/sglang/commit/637cc7d195) [#46519](https://github.com/sgl-project/sglang/pull/46519)
  [Chore] [XPU] deps: Pin sglang-kernel-xpu by version using uv (#46519)
  _Files: `.github/workflows/pr-test-xpu.yml`, `docker/xpu.Dockerfile`, `docs/docs/hardware-platforms/xpu.mdx`, `python/pyproject_xpu.toml`_
- **2026-11-04** [`b92cfcb4c6`](https://github.com/sgl-project/sglang/commit/b92cfcb4c6) [#48282](https://github.com/sgl-project/sglang/pull/48282)
  [Fix] test: Import sgl_kernel in the Xeon thread-binding test (#48282)
  _Files: `test/registered/cpu/test_binding.py`_
- **2026-11-04** [`f3ef1a32fd`](https://github.com/sgl-project/sglang/commit/f3ef1a32fd) [#48278](https://github.com/sgl-project/sglang/pull/48278)
  [Test] dspark: Register the simulated-bonus test for CUDA CI (#48278)
  _Files: `test/registered/spec/dspark/test_dspark_simulated_bonus.py`_
- **2026-11-02** [`e152f531d9`](https://github.com/sgl-project/sglang/commit/e152f531d9) [#47949](https://github.com/sgl-project/sglang/pull/47949)
  [Perf] [NVIDIA] dsv41: Split small-batch decode mHC post-combine-norm rows over a CTA cluster (#47949)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mhc_post_combine_norm_decode.cuh`, `python/sglang/kernels/ops/layernorm/mhc_post_combine_norm_decode.py`, `test/registered/kernels/ops/layernorm/test_mhc_post_combine_norm_decode.py`_
- **2026-11-02** [`d0d50da899`](https://github.com/sgl-project/sglang/commit/d0d50da899) [#47915](https://github.com/sgl-project/sglang/pull/47915)
  [Fix] kernels: Port rmsnorm and softmax bench off the removed get_jit_cuda_arch (#47915)
  _Files: `python/sglang/kernels/ops/layernorm/norm.py`, `test/registered/kernels/benchmark/sampling/bench_softmax.py`_
- **2026-11-02** [`b0debe0a7a`](https://github.com/sgl-project/sglang/commit/b0debe0a7a) [#46088](https://github.com/sgl-project/sglang/pull/46088)
  [Perf] dsv41: Fuse decode mHC post, combine and RMSNorm into one kernel (#46088)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mhc_post_combine_norm_decode.cuh`, `python/sglang/kernels/ops/layernorm/__init__.py`, `python/sglang/kernels/ops/layernorm/mhc_post_combine_norm_decode.py`, `python/sglang/srt/models/deepseek_v4_boundary.py` _+2 more__
- **2026-11-02** [`46db5f7dcc`](https://github.com/sgl-project/sglang/commit/46db5f7dcc) [#47712](https://github.com/sgl-project/sglang/pull/47712)
  [Fix] [NVIDIA] fused-a-gemm: Check the selected backend's K alignment before taking the fused path (#47712)
  _Files: `python/sglang/kernels/ops/gemm/fused_a_gemm.py`, `python/sglang/srt/models/deepseek_v2.py`, `test/registered/kernels/ops/gemm/test_fused_a_gemm.py`_
- **2026-11-02** [`8088adb4d3`](https://github.com/sgl-project/sglang/commit/8088adb4d3) [#47066](https://github.com/sgl-project/sglang/pull/47066)
  [Fix] kernels: Hash tensors over 8 GiB in gpu_tensor_hash (#47066)
  _Files: `python/sglang/kernels/ops/memory/gpu_tensor_hash.py`, `test/registered/kernels/ops/memory/test_gpu_tensor_hash.py`_
- **2026-11-02** [`a2029238de`](https://github.com/sgl-project/sglang/commit/a2029238de) [#47229](https://github.com/sgl-project/sglang/pull/47229)
  [Fix] kernels: Support OOT fused ops under torch.compile (#47229)
  _Files: `python/sglang/kernels/README.md`, `python/sglang/kernels/fused_op.py`, `test/registered/unit/kernels/test_fused_op_dispatch.py`_

## Other  (27 commits)

- **2026-11-09** [`7b917c0eca`](https://github.com/sgl-project/sglang/commit/7b917c0eca) [#48812](https://github.com/sgl-project/sglang/pull/48812)
  [Fix] weight_checker: Compare weights on the live weight's device (#48812)
  _Files: `python/sglang/srt/model_executor/weight_checker_comparator.py`, `test/registered/unit/model_executor/test_weight_checker.py`_
- **2026-11-09** [`b9d993716e`](https://github.com/sgl-project/sglang/commit/b9d993716e) [#48545](https://github.com/sgl-project/sglang/pull/48545)
  [Fix] [CPU] cpu-graph: Preserve return_logprob and request metadata in dynamic prefill (#48545)
  _Files: `python/sglang/srt/model_executor/cpu_graph_runner.py`, `test/registered/cpu/test_cpu_graph.py`_
- **2026-11-09** [`65abad034b`](https://github.com/sgl-project/sglang/commit/65abad034b) [#49159](https://github.com/sgl-project/sglang/pull/49159)
  [Test] kv_canary: Compare median decode time in the self-bench speed test (#49159)
  _Files: `test/registered/kv_canary/test_self_e2e_bench_speed.py`_
- **2026-11-08** [`5a57473907`](https://github.com/sgl-project/sglang/commit/5a57473907) [#49028](https://github.com/sgl-project/sglang/pull/49028)
  [Test] kv_canary: Ignore EOS in the PD fixture for the SWA model (#49028)
  _Files: `python/sglang/test/kv_canary/pd_fixture.py`_
- **2026-11-07** [`0a8ad45c12`](https://github.com/sgl-project/sglang/commit/0a8ad45c12) [#49092](https://github.com/sgl-project/sglang/pull/49092)
  [Fix] kv-canary: Pass token-oracle request ids into the warmup dummy forward (#49092)
  _Files: `python/sglang/srt/model_executor/runner/base_runner.py`_
- **2026-11-07** [`c6042b570e`](https://github.com/sgl-project/sglang/commit/c6042b570e) [#48797](https://github.com/sgl-project/sglang/pull/48797)
  [Test] server-info: Pin the Python frontend in two /server_info unit tests (#48797)
  _Files: `test/registered/unit/entrypoints/test_server_info.py`_
- **2026-11-07** [`a6ae2a54e5`](https://github.com/sgl-project/sglang/commit/a6ae2a54e5) [#48453](https://github.com/sgl-project/sglang/pull/48453)
  [Test] load-snapshot: Pin the Python server mode in TestZmqReaderOwner (#48453)
  _Files: `test/registered/unit/managers/test_load_snapshot_backends.py`_
- **2026-11-06** [`0afb736d0a`](https://github.com/sgl-project/sglang/commit/0afb736d0a) [#48668](https://github.com/sgl-project/sglang/pull/48668)
  [Fix] sgl-router: Keep a worker's cached chain visible when another worker holds its prefix (#48668)
  _Files: `sgl-router/src/policies/scoring/prefix_cache.rs`, `sgl-router/src/state/kv_events/tree.rs`_
- **2026-11-06** [`27bc1a0615`](https://github.com/sgl-project/sglang/commit/27bc1a0615) [#48399](https://github.com/sgl-project/sglang/pull/48399)
  [Refactor] env: Dispatch on the GPU architecture instead of env vars that restate it (#48399)
- **2026-11-06** [`c06e39c6ca`](https://github.com/sgl-project/sglang/commit/c06e39c6ca) [#48714](https://github.com/sgl-project/sglang/pull/48714)
  [Feat] kimi-k3.1: Opt-in trtllm DSA backend (#48714)
  _Files: `python/sglang/srt/arg_groups/overrides.py`_
- **2026-11-06** [`d93a778ff8`](https://github.com/sgl-project/sglang/commit/d93a778ff8) [#47458](https://github.com/sgl-project/sglang/pull/47458)
  [Fix] nemotron: Accept transformers 5 layer types in NemotronHConfig (#47458)
  _Files: `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/configs/nemotron_h.py`, `test/registered/unit/configs/test_nano_nemotron_vl_config.py`_
- **2026-11-06** [`14e395aa5e`](https://github.com/sgl-project/sglang/commit/14e395aa5e) [#48290](https://github.com/sgl-project/sglang/pull/48290)
  [Test] [NPU] kimi_k3: run the decode perf case via the aisbench prefix mode (#48290)
  _Files: `test/registered/npu/performance/kimi_k3/test_npu_kimi_k3_w4a8_32p_mix_in128k_out1k_decode_prefix.py`_
- **2026-11-06** [`6b13469f91`](https://github.com/sgl-project/sglang/commit/6b13469f91) [#48781](https://github.com/sgl-project/sglang/pull/48781)
  [Refactor] utils: Split `common.py` into topic modules and owner packages (#48781)
- **2026-11-06** [`9285994acc`](https://github.com/sgl-project/sglang/commit/9285994acc) [#41204](https://github.com/sgl-project/sglang/pull/41204)
  [Fix] processor: Restore BOS/EOS flags for processor-owned tokenizers (#41204)
  _Files: `python/sglang/srt/hf_transformers/processor.py`, `test/registered/unit/utils/test_hf_transformers.py`_
- **2026-11-06** [`93cfea6b12`](https://github.com/sgl-project/sglang/commit/93cfea6b12) [#48758](https://github.com/sgl-project/sglang/pull/48758)
  [Refactor] utils: Move domain-dependent modules out of `srt.utils` (#48758)
- **2026-11-05** [`542a7325f0`](https://github.com/sgl-project/sglang/commit/542a7325f0) [#48708](https://github.com/sgl-project/sglang/pull/48708)
  [Chore] CODEOWNERS: Update code owners (#48708)
  _Files: `.github/CODEOWNERS`_
- **2026-11-04** [`a7cbb54c3b`](https://github.com/sgl-project/sglang/commit/a7cbb54c3b) [#48301](https://github.com/sgl-project/sglang/pull/48301)
  [Test] kv_canary: Drop min_p from the canary-info e2e sampling params (#48301)
  _Files: `python/sglang/test/kv_canary/canary_info_utils.py`_
- **2026-11-04** [`1666971264`](https://github.com/sgl-project/sglang/commit/1666971264) [#48002](https://github.com/sgl-project/sglang/pull/48002)
  [Fix] server_args: Refuse a sharded-padded CP KV layout with unified memory (#48002)
  _Files: `python/sglang/srt/arg_groups/parallel_hook.py`, `test/registered/unit/server_args/test_server_args.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-11-04** [`744af7ce72`](https://github.com/sgl-project/sglang/commit/744af7ce72) [#47553](https://github.com/sgl-project/sglang/pull/47553)
  [Perf] R3: Skip routed-expert capture on ranks that send no rows (2/3) (#47553)
  _Files: `python/sglang/srt/state_capturer/base.py`, `python/sglang/srt/state_capturer/routed_experts.py`, `test/registered/unit/state_capturer/test_routed_experts_scattered_a2a.py`_
- **2026-11-03** [`751fa99d7e`](https://github.com/sgl-project/sglang/commit/751fa99d7e) [#48087](https://github.com/sgl-project/sglang/pull/48087)
  [Perf] imports: Keep the detokenizer off TokenizerManager and the tokenizer off schedule_batch (#48087)
- **2026-11-03** [`57abc8a831`](https://github.com/sgl-project/sglang/commit/57abc8a831) [#48092](https://github.com/sgl-project/sglang/pull/48092)
  [Fix] test: Import ResolvedView from model_override_base in test_model_overrides (#48092)
  _Files: `test/registered/unit/test_model_overrides.py`_
- **2026-11-03** [`5bffd74274`](https://github.com/sgl-project/sglang/commit/5bffd74274) [#47990](https://github.com/sgl-project/sglang/pull/47990)
  [Refactor] imports: Import names from where they are defined; remove re-export shims (#47990)
- **2026-11-03** [`1c13f952f8`](https://github.com/sgl-project/sglang/commit/1c13f952f8) [#47954](https://github.com/sgl-project/sglang/pull/47954)
  [Refactor] rust-server: Make the advertised listener host an overridable classmethod (#47954)
  _Files: `python/sglang/srt/rust_server/server.py`_
- **2026-11-03** [`d1dd0b7a62`](https://github.com/sgl-project/sglang/commit/d1dd0b7a62) [#44398](https://github.com/sgl-project/sglang/pull/44398)
  [Test] [NPU] kimi_k3: enable L2 host HiCache for 32p gpqa accuracy test with host hit-rate bench (#44398)
  _Files: `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/accuracy/kimi_k3/test_npu_kimi_k3_w4a8_32p_gpqa.py`_
- **2026-11-02** [`3f0051eec7`](https://github.com/sgl-project/sglang/commit/3f0051eec7) [#47858](https://github.com/sgl-project/sglang/pull/47858)
  [Fix] graph: Restore XPU logger and Inkling backend mock dtype (#47858)
- **2026-11-02** [`26fde018e5`](https://github.com/sgl-project/sglang/commit/26fde018e5) [#47875](https://github.com/sgl-project/sglang/pull/47875)
  [Chore] owner: update (#47875)
  _Files: `.github/CODEOWNERS`_
- **2026-11-02** [`ea2fda7fd2`](https://github.com/sgl-project/sglang/commit/ea2fda7fd2) [#44494](https://github.com/sgl-project/sglang/pull/44494)
  [Fix] metrics: Handle CPU monitor clock resets after restore (#44494)
  _Files: `python/sglang/srt/observability/cpu_monitor.py`, `test/registered/unit/observability/test_cpu_monitor.py`_

## Scheduler / Batching  (27 commits)

- **2026-11-09** [`fd978b6cec`](https://github.com/sgl-project/sglang/commit/fd978b6cec) [#49003](https://github.com/sgl-project/sglang/pull/49003)
  [Feat] [AMD] custom-all-reduce: Run carv2 across gfx1250 UALink nodes (#49003)
  _Files: `python/sglang/srt/distributed/device_communicators/configs/custom_all_reduce_v2.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `python/sglang/srt/distributed/device_communicators/gfx1250_fabric.py` _+5 more__
- **2026-11-09** [`bd5774079a`](https://github.com/sgl-project/sglang/commit/bd5774079a) [#44477](https://github.com/sgl-project/sglang/pull/44477)
  [Fix] metrics: Handle process CPU clock resets after restore (#44477)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/observability/scheduler_stage_metrics.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`, `test/registered/unit/observability/test_scheduler_stage_metrics.py`_
- **2026-11-09** [`80cc4ed64b`](https://github.com/sgl-project/sglang/commit/80cc4ed64b) [#48207](https://github.com/sgl-project/sglang/pull/48207)
  [Fix] routed-experts: reset routed_experts_start_len when a request is rejected at intake (#48207)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/rl/test_return_routed_experts.py`, `test/registered/unit/managers/test_req_finish_state.py`_
- **2026-11-07** [`e93aacbd06`](https://github.com/sgl-project/sglang/commit/e93aacbd06) [#48518](https://github.com/sgl-project/sglang/pull/48518)
  [Fix] server-args: Redact the access keys from /server_info, logs, launch_command and crash dumps (#48518)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/server_utils.py`, `python/sglang/srt/managers/scheduler_components/internal_state.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+7 more__
- **2026-11-07** [`59daec8136`](https://github.com/sgl-project/sglang/commit/59daec8136) [#48666](https://github.com/sgl-project/sglang/pull/48666)
  [Fix] tbo: Capture routed experts at each child's parent rows (#48666)
  _Files: `python/sglang/srt/batch_overlap/operations.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/forward_context.py`, `python/sglang/srt/models/deepseek_v4.py` _+2 more__
- **2026-11-07** [`d333aded47`](https://github.com/sgl-project/sglang/commit/d333aded47) [#48449](https://github.com/sgl-project/sglang/pull/48449)
  [Refactor] scheduler: Run a prefill batch's KV calls from one overridable _flush_prefill (#48449)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/unit/managers/test_batch_result_processor_flush_prefill.py`_
- **2026-11-07** [`c7d154f910`](https://github.com/sgl-project/sglang/commit/c7d154f910) [#48446](https://github.com/sgl-project/sglang/pull/48446)
  [Fix] io_struct: Give each request its own sampling_params dict during normalization (#48446)
  _Files: `python/sglang/srt/managers/io_struct.py`, `test/registered/unit/managers/test_io_struct.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
- **2026-11-07** [`44ba21d564`](https://github.com/sgl-project/sglang/commit/44ba21d564) [#48513](https://github.com/sgl-project/sglang/pull/48513)
  [Feat] rust-server: Export extension metric families and hand media admission timing to the MM processor (#48513)
  _Files: `rust/sglang-server/src/api_server/core.rs`, `rust/sglang-server/src/api_server/core/metrics.rs`, `rust/sglang-server/src/api_server/core/prefetch.rs`, `rust/sglang-server/src/lib.rs` _+5 more__
- **2026-11-06** [`0fde642ff6`](https://github.com/sgl-project/sglang/commit/0fde642ff6) [#48762](https://github.com/sgl-project/sglang/pull/48762)
  [Refactor] scheduler: Run every state check through SchedulerInvariantChecker.run (#48762)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py` _+5 more__
- **2026-11-06** [`db5cd6bad6`](https://github.com/sgl-project/sglang/commit/db5cd6bad6) [#48508](https://github.com/sgl-project/sglang/pull/48508)
  [Perf] tokenizer_manager: Keep the crash-dump request history pickled so the cyclic GC never scans it (#48508)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/observability/test_crash_dump.py`_
- **2026-11-06** [`91fd6756e7`](https://github.com/sgl-project/sglang/commit/91fd6756e7) [#48654](https://github.com/sgl-project/sglang/pull/48654)
  [Fix] scheduler: Match arrival prefixes on every PP stage (#48654)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_pp_arrival_match_parity.py`_
- **2026-11-06** [`59ac9016b0`](https://github.com/sgl-project/sglang/commit/59ac9016b0) [#48061](https://github.com/sgl-project/sglang/pull/48061)
  [Fix] batch-invariant: restore the dispatcher state when a scope exits (#48061)
  _Files: `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `test/registered/unit/batch_invariant_ops/test_batch_invariant_context.py`_
- **2026-11-06** [`2e8dcb13f9`](https://github.com/sgl-project/sglang/commit/2e8dcb13f9) [#48433](https://github.com/sgl-project/sglang/pull/48433)
  [Feat] weight_update: Let platforms serve weight transports through /plugin_weight_update (#48433)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/weight_updater.py` _+4 more__
- **2026-11-06** [`5d60f369b4`](https://github.com/sgl-project/sglang/commit/5d60f369b4) [#48809](https://github.com/sgl-project/sglang/pull/48809)
  [Fix] overlap: Skip deferred-relay flush when future_map is None (#48809)
  _Files: `python/sglang/srt/managers/overlap_utils.py`_
- **2026-11-06** [`5f9e506eb7`](https://github.com/sgl-project/sglang/commit/5f9e506eb7) [#47963](https://github.com/sgl-project/sglang/pull/47963)
  [Fix] rust-server: Park the idle scheduler on its request ring only with --sleep-on-idle (#47963)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/idle_sleeper.py`, `python/sglang/srt/rust_server/server.py`, `test/registered/unit/managers/test_rust_server_idle_sleep.py`_
- **2026-11-05** [`1942c5f095`](https://github.com/sgl-project/sglang/commit/1942c5f095) [#47099](https://github.com/sgl-project/sglang/pull/47099)
  [Feat] platforms: Let platforms default unset profile request fields (#47099)
  _Files: `python/sglang/srt/managers/tokenizer_control_mixin.py`, `python/sglang/srt/platforms/interface.py`, `test/registered/unit/managers/test_tokenizer_control_mixin.py`_
- **2026-11-04** [`2e0edb6d49`](https://github.com/sgl-project/sglang/commit/2e0edb6d49) [#48028](https://github.com/sgl-project/sglang/pull/48028)
  [Fix] batch-invariant: restore torch.bmm when set_batch_invariant_mode exits (#48028)
  _Files: `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`_
- **2026-11-04** [`91747384e5`](https://github.com/sgl-project/sglang/commit/91747384e5) [#47552](https://github.com/sgl-project/sglang/pull/47552)
  [Perf] R3: Keep the routed-expert host cache only on the output rank (1/3) (#47552)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/state_capturer/base.py` _+3 more__
- **2026-11-03** [`4e5057aef9`](https://github.com/sgl-project/sglang/commit/4e5057aef9) [#48119](https://github.com/sgl-project/sglang/pull/48119)
  [Refactor] tokenizer: Fold `TokenizerWorker` into `TokenizerManager` (#48119)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/io_struct.py` _+6 more__
- **2026-11-03** [`36273b916d`](https://github.com/sgl-project/sglang/commit/36273b916d) [#47955](https://github.com/sgl-project/sglang/pull/47955)
  [Perf] srt: Record per request whether an extend row completes its prompt (#47955)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/batch_overlap/test_tbo_filter_batch_marker.py`, `test/registered/unit/managers/test_schedule_batch_out_of_place.py`_
- **2026-11-03** [`12e741c21f`](https://github.com/sgl-project/sglang/commit/12e741c21f) [#43909](https://github.com/sgl-project/sglang/pull/43909)
  [Fix] scheduler: Record weight version events on every request list (#43909)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/load_inquirer.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `test/registered/unit/managers/test_deferred_output.py` _+5 more__
- **2026-11-03** [`602d045671`](https://github.com/sgl-project/sglang/commit/602d045671) [#45785](https://github.com/sgl-project/sglang/pull/45785)
  [Fix] scheduler: Publish KV metrics when idle (#45785)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`, `test/registered/unit/observability/test_stat_loggers_di.py`_
- **2026-11-02** [`efdcb420c7`](https://github.com/sgl-project/sglang/commit/efdcb420c7) [#47731](https://github.com/sgl-project/sglang/pull/47731)
  [Perf] imports: Keep light modules off HF patches, model configs, and the scheduler (#47731)
- **2026-11-02** [`d9521615b7`](https://github.com/sgl-project/sglang/commit/d9521615b7) [#47614](https://github.com/sgl-project/sglang/pull/47614)
  [Fix] PP: record received proxy tensors on the forward stream (#47614)
  _Files: `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/registered/unit/managers/test_disagg_idle_step_counters.py`_
- **2026-11-02** [`d82e124a9e`](https://github.com/sgl-project/sglang/commit/d82e124a9e) [#41771](https://github.com/sgl-project/sglang/pull/41771)
  [Fix] dp-controller: Keep one input_embeds request from killing a DP server under total_tokens (#41771)
  _Files: `python/sglang/srt/managers/data_parallel_controller.py`, `test/registered/unit/managers/test_data_parallel_controller.py`_
- **2026-11-02** [`0abac089e5`](https://github.com/sgl-project/sglang/commit/0abac089e5) [#47829](https://github.com/sgl-project/sglang/pull/47829)
  [Fix] test: Stub _confidence_budget_prepare in the scheduler running-reqs test (#47829)
  _Files: `test/registered/unit/managers/test_scheduler_running_reqs.py`_
- **2026-11-02** [`acd6f55704`](https://github.com/sgl-project/sglang/commit/acd6f55704) [#46334](https://github.com/sgl-project/sglang/pull/46334)
  [Fix] scheduler: Publish KV events while the engine is paused (#46334)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_

## Tensor / Data Parallel  (27 commits)

- **2026-11-07** [`ba48fc1a9e`](https://github.com/sgl-project/sglang/commit/ba48fc1a9e) [#49001](https://github.com/sgl-project/sglang/pull/49001)
  [Feat] [AMD] custom-all-reduce: Run carv2 on MI450 with FABRIC handles and a gfx1250 table (#49001)
  _Files: `python/sglang/kernels/jit/csrc/distributed/custom_all_reduce.cuh`, `python/sglang/srt/distributed/device_communicators/configs/custom_all_reduce_v2.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/environ.py` _+1 more__
- **2026-11-07** [`4b4dc7b01b`](https://github.com/sgl-project/sglang/commit/4b4dc7b01b) [#49030](https://github.com/sgl-project/sglang/pull/49030)
  [Feat] rust-server: Report cached prompt tokens under --enable-cache-report on the OpenAI routes (#49030)
  _Files: `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/rust_server/config.py`, `rust/sglang-server/src/api_server/http/openai/chat.rs`, `rust/sglang-server/src/api_server/http/openai/completions.rs` _+5 more__
- **2026-11-07** [`ab01cf2446`](https://github.com/sgl-project/sglang/commit/ab01cf2446) [#47538](https://github.com/sgl-project/sglang/pull/47538)
  [Feat] http_server: Dispatch SageMaker /invocations to completions and embeddings by request body (#47538)
  _Files: `docs/docs/basic_usage/aws_sagemaker.mdx`, `python/sglang/srt/entrypoints/http_server.py`, `test/registered/unit/entrypoints/test_sagemaker_invocations.py`_
- **2026-11-07** [`985837b6ff`](https://github.com/sgl-project/sglang/commit/985837b6ff) [#48815](https://github.com/sgl-project/sglang/pull/48815)
  [Fix] rust-server: Keep the DP control fan-out off an inherited HTTP proxy (#48815)
  _Files: `rust/sglang-server/src/api_server/core/peer.rs`, `rust/sglang-server/src/api_server/core/request_log.rs`, `rust/sglang-server/src/api_server/handlers/control.rs`, `rust/sglang-server/src/api_server/handlers/generate.rs` _+11 more__
- **2026-11-07** [`a8c169ce72`](https://github.com/sgl-project/sglang/commit/a8c169ce72) [#48798](https://github.com/sgl-project/sglang/pull/48798)
  [Feat] rust-server: Let the launching process list the ports its node's Rust listeners bind (#48798)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/rust_server/server.py`, `test/registered/unit/entrypoints/test_rust_server_dp_ports.py`_
- **2026-11-07** [`9877a3076f`](https://github.com/sgl-project/sglang/commit/9877a3076f) [#48572](https://github.com/sgl-project/sglang/pull/48572)
  [Feat] rust-server: Report the serving DP rank in /generate meta_info (#48572)
  _Files: `proto/sglang/api/v1/generate.proto`, `python/sglang/api/v1/api_types.py`, `rust/sglang-api-types/src/generated/sglang.api.v1.rs`, `rust/sglang-api-types/src/generated/sglang.api.v1.serde.rs` _+9 more__
- **2026-11-07** [`3f2d0fac80`](https://github.com/sgl-project/sglang/commit/3f2d0fac80) [#48523](https://github.com/sgl-project/sglang/pull/48523)
  [Feat] rust-server: Decompress x-body-compressed request bodies (#48523)
  _Files: `python/sglang/srt/rust_server/config.py`, `rust/Cargo.lock`, `rust/sglang-server/Cargo.toml`, `rust/sglang-server/src/api_server/http.rs` _+6 more__
- **2026-11-07** [`286cb448b1`](https://github.com/sgl-project/sglang/commit/286cb448b1) [#48511](https://github.com/sgl-project/sglang/pull/48511)
  [Test] rust-server: Cover the embedded Rust frontend in a two-node TP engine (#48511)
  _Files: `test/registered/core/test_rust_server_multi_node.py`_
- **2026-11-07** [`6d2e648803`](https://github.com/sgl-project/sglang/commit/6d2e648803) [#48709](https://github.com/sgl-project/sglang/pull/48709)
  [Feat] kimi-k3.1: Prefill context parallelism (CP-TP group sharing) (#48709)
  _Files: `python/sglang/srt/arg_groups/cp_tp_group_sharing_hook.py`, `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py`, `python/sglang/srt/configs/kimi_linear.py`, `python/sglang/srt/layers/layer_boundary/construction.py` _+8 more__
- **2026-11-06** [`e45e1d0c56`](https://github.com/sgl-project/sglang/commit/e45e1d0c56) [#47964](https://github.com/sgl-project/sglang/pull/47964)
  [Feat] [AMD] custom-all-reduce: Run the JIT custom all-reduce v2 on ROCm (#47964)
  _Files: `python/sglang/kernels/jit/csrc/distributed/custom_all_reduce.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/distributed/ptx.cuh`, `python/sglang/srt/distributed/device_communicators/configs/custom_all_reduce_v2.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py` _+3 more__
- **2026-11-06** [`5eb49ec4d2`](https://github.com/sgl-project/sglang/commit/5eb49ec4d2) [#37354](https://github.com/sgl-project/sglang/pull/37354)
  [Feat] [Apple] mlx: Add an architecture-independent ATen-to-MLX lowering layer (#37354)
  _Files: `python/sglang/srt/hardware_backend/mlx/fx_lowering.py`, `test/registered/mlx/test_fx_lowering.py`, `test/registered/mlx/test_fx_lowering_schema_parity.py`, `test/registered/mlx/test_fx_lowering_sdpa.py`_
- **2026-11-06** [`1050729dc1`](https://github.com/sgl-project/sglang/commit/1050729dc1) [#48554](https://github.com/sgl-project/sglang/pull/48554)
  [Fix] [NVIDIA] custom-allreduce: Scope a zero NVLink fabric cluster UUID to its own node (#48554)
  _Files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `test/registered/unit/distributed/test_custom_all_reduce_v2_capability.py`_
- **2026-11-06** [`98d7f49e84`](https://github.com/sgl-project/sglang/commit/98d7f49e84) [#48487](https://github.com/sgl-project/sglang/pull/48487)
  [Fix] sampler: skip the token-id all-reduce when the TP sync group has one rank (#48487)
  _Files: `python/sglang/srt/layers/sampler.py`, `test/registered/unit/layers/test_sampler_token_id_sync.py`_
- **2026-11-06** [`3c0e6e9f58`](https://github.com/sgl-project/sglang/commit/3c0e6e9f58) [#48713](https://github.com/sgl-project/sglang/pull/48713)
  [Feat] kimi-k3.1: Let shared-expert TP span interleave prefill CP (#48713)
  _Files: `python/sglang/srt/arg_groups/fields/parallel.py`, `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/distributed/parallel_state.py`, `test/registered/unit/distributed/test_parallel_state.py`_
- **2026-11-06** [`c117e31f9f`](https://github.com/sgl-project/sglang/commit/c117e31f9f) [#46662](https://github.com/sgl-project/sglang/pull/46662)
  [Doc] [AMD] GLM-5.3: Enable MTP on MI355X and add the agentic recipe with the AMD monokernel (#46662)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`_
- **2026-11-06** [`6d4684f7dd`](https://github.com/sgl-project/sglang/commit/6d4684f7dd) [#45149](https://github.com/sgl-project/sglang/pull/45149)
  [Feat] [MLU] platform: Add initial support for Cambricon MLUs (#45149)
  _Files: `docs/docs.json`, `docs/docs/hardware-platforms/cambricon_mlu.mdx`, `python/pyproject_other.toml`, `python/sglang/kernels/fused_op.py` _+18 more__
- **2026-11-06** [`3de594d86f`](https://github.com/sgl-project/sglang/commit/3de594d86f) [#45945](https://github.com/sgl-project/sglang/pull/45945)
  [Feat] comm: Gated background transfers (#45945)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/distributed/device_communicators/gated_transfer.py`, `python/sglang/srt/environ.py`, `test/registered/unit/distributed/test_gated_transfer.py`_
- **2026-11-05** [`5629a8f60d`](https://github.com/sgl-project/sglang/commit/5629a8f60d) [#48277](https://github.com/sgl-project/sglang/pull/48277)
  [Doc] cookbook: Add TPU v7 to Muse Spark Open (#48277)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`, `docs/src/snippets/configs/meta-models/muse-spark.jsx`_
- **2026-11-05** [`493c857736`](https://github.com/sgl-project/sglang/commit/493c857736) [#45883](https://github.com/sgl-project/sglang/pull/45883)
  [Feat] rust/grpc: Honor --grpc-response-timeout-secs in the Rust server (#45883)
  _Files: `python/sglang/srt/rust_server/config.py`, `rust/sglang-server/src/api_server/grpc/service.rs`, `rust/sglang-server/src/message/config.rs`, `test/registered/unit/entrypoints/test_rust_server_dp_ports.py`_
- **2026-11-05** [`8d7be3acff`](https://github.com/sgl-project/sglang/commit/8d7be3acff) [#46637](https://github.com/sgl-project/sglang/pull/46637)
  [Feat] rust/grpc: Report the node's Rust listeners in api.v1 discovery (#46637)
  _Files: `proto/sglang/api/v1/service.proto`, `python/sglang/api/v1/api_types.py`, `python/sglang/srt/rust_server/config.py`, `rust/sglang-api-types/src/generated/sglang.api.v1.rs` _+5 more__
- **2026-11-05** [`bf40ca98f4`](https://github.com/sgl-project/sglang/commit/bf40ca98f4) [#42198](https://github.com/sgl-project/sglang/pull/42198)
  [Perf] [AMD] custom-all-reduce: Select the fused AR+RMSNorm 1-stage kernel by token count and read volume (#42198)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `test/registered/ops/test_aiter_allreduce_fusion_amd.py`_
- **2026-11-05** [`03d7a10dbc`](https://github.com/sgl-project/sglang/commit/03d7a10dbc) [#34212](https://github.com/sgl-project/sglang/pull/34212)
  [Fix] [AMD] DSP: skip unused QuickAllReduce allocation for DCP groups (#34212)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `test/registered/unit/distributed/test_parallel_state.py`_
- **2026-11-04** [`8884b4b421`](https://github.com/sgl-project/sglang/commit/8884b4b421) [#48413](https://github.com/sgl-project/sglang/pull/48413)
  [Doc] cookbook: Add Kimi-K3.1-Pro deployment recipes (#48413)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.1-Pro.mdx`, `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+8 more__
- **2026-11-02** [`9eec211b9a`](https://github.com/sgl-project/sglang/commit/9eec211b9a) [#47894](https://github.com/sgl-project/sglang/pull/47894)
  [Chore] [NVIDIA] deps: Bump sgl-deep-gemm to 0.2.5.post3 (#47894)
  _Files: `docker/Dockerfile.cu134`, `python/pyproject.toml`, `test/registered/e2e/cp/test_cp_decode_attn_tp_server.py`_
- **2026-11-02** [`8c0544b9bf`](https://github.com/sgl-project/sglang/commit/8c0544b9bf) [#46166](https://github.com/sgl-project/sglang/pull/46166)
  [Perf] http: Serialize /v1/embeddings responses with model_json_response (#46166)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `test/registered/unit/entrypoints/test_embedding_responses.py`_
- **2026-11-02** [`96f5a5d78a`](https://github.com/sgl-project/sglang/commit/96f5a5d78a) [#47837](https://github.com/sgl-project/sglang/pull/47837)
  [Test] linear: Expect replicated rows to skip TP symmetric memory (#47837)
  _Files: `python/sglang/srt/hardware_backend/xpu/graph_runner/xpu_graph_runner.py`, `test/registered/unit/layers/test_linear_parallel_groups.py`_
- **2026-11-02** [`009b167f10`](https://github.com/sgl-project/sglang/commit/009b167f10) [#47744](https://github.com/sgl-project/sglang/pull/47744)
  [Fix] linear: Keep replicated outputs out of TP symmetric memory (#47744)
  _Files: `python/sglang/srt/layers/linear.py`, `test/registered/unit/layers/test_kimi_mlp_parallel_groups.py`_

## Quantization  (26 commits)

- **2026-11-09** [`a4b8801197`](https://github.com/sgl-project/sglang/commit/a4b8801197) [#48656](https://github.com/sgl-project/sglang/pull/48656)
  [Fix] comfyui: Load FastH3, H3 FP8, Qwen-Image 2.1 Turbo and community INT8 single files (#48656)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image21.py`, `python/sglang/multimodal_gen/runtime/loader/comfyui_checkpoints/minimax_h3.py` _+9 more__
- **2026-11-09** [`af72557571`](https://github.com/sgl-project/sglang/commit/af72557571) [#48536](https://github.com/sgl-project/sglang/pull/48536)
  [Perf] [AMD] quantization: Fuse SiLU-and-mul with the dynamic per-tensor fp8 quant of dense MLPs on gfx95 (#48536)
  _Files: `python/sglang/kernels/ops/quantization/aiter_fp8_quant_triton.py`, `python/sglang/srt/layers/quantization/fp8_activation.py`, `test/registered/kernels/ops/quantization/test_aiter_fp8_quant_triton.py`, `test/registered/unit/layers/quantization/test_dense_silu_fp8_per_tensor_gfx95.py`_
- **2026-11-08** [`a6989e70cb`](https://github.com/sgl-project/sglang/commit/a6989e70cb) [#44813](https://github.com/sgl-project/sglang/pull/44813)
  [Fix] deepseek_v4: route unquantized BF16/F16/F32 checkpoints off the MXFP4 expert path (#44813)
  _Files: `python/sglang/srt/configs/deepseek_v4.py`, `test/registered/unit/configs/test_deepseek_v4_fp4_detect.py`_
- **2026-11-08** [`33db33f2e3`](https://github.com/sgl-project/sglang/commit/33db33f2e3) [#47908](https://github.com/sgl-project/sglang/pull/47908)
  [Fix] [AMD] quark: Match aiter's column-major scale layout in the MXFP4 quant fake (#47908)
  _Files: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `test/registered/unit/layers/quantization/test_quark_mxfp4_asm.py`_
- **2026-11-08** [`db680c5b80`](https://github.com/sgl-project/sglang/commit/db680c5b80) [#48043](https://github.com/sgl-project/sglang/pull/48043)
  [Perf] [AMD] qwen3: Fuse the 1x128 FP8 input quant into RMSNorm and SiLU-and-mul for block-FP8 linears on gfx950 (#48043)
  _Files: `python/sglang/kernels/ops/gemm/smallm_fp8_blockscale_gfx950/__init__.py`, `python/sglang/kernels/ops/quantization/silu_mul_fp8_group_quant.py`, `python/sglang/srt/layers/layer_boundary/prepare.py`, `python/sglang/srt/layers/layer_boundary/stage.py` _+4 more__
- **2026-11-07** [`9d547e19ff`](https://github.com/sgl-project/sglang/commit/9d547e19ff) [#47862](https://github.com/sgl-project/sglang/pull/47862)
  [Feat] [AMD] aiter: One folder of in-tree aiter tuned rows for every model (#47862)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_common/amd/aiter_intree_tune.py`, `python/sglang/srt/utils/aiter_tuned_configs/a8w8_blockscale_bpreshuffle/deepseek_v4.csv` _+2 more__
- **2026-11-07** [`c8e7e14a12`](https://github.com/sgl-project/sglang/commit/c8e7e14a12) [#48128](https://github.com/sgl-project/sglang/pull/48128)
  [Fix] quantization: Load Muse-Glimmer-NVFP4's MXFP8 lm_head, and run its MXFP8 dense layers as block-FP8 off Blackwell (#48128)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/unit/layers/quantization/test_fp8_lm_head_mxfp8.py`, `test/registered/unit/model_loader/test_modelopt_loader.py`_
- **2026-11-07** [`a20aba1937`](https://github.com/sgl-project/sglang/commit/a20aba1937) [#48563](https://github.com/sgl-project/sglang/pull/48563)
  [Perf] [NVIDIA] gemma4: fuse the TP all-reduce with the layer epilogue and FP8 quant on NVLink multicast (#48563)
  _Files: `python/sglang/kernels/jit/csrc/gemma4/comm/ar_fusion.cuh`, `python/sglang/kernels/ops/communication/gemma4_ar_fusion.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/communication/gemma4_ar_fusion.py` _+4 more__
- **2026-11-07** [`e25fae7cf2`](https://github.com/sgl-project/sglang/commit/e25fae7cf2) [#44486](https://github.com/sgl-project/sglang/pull/44486)
  [Perf] quantization: Add the bias in the cuBLASLt epilogue for per-tensor FP8 linears (#44486)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/registered/unit/layers/quantization/test_fp8_utils.py`_
- **2026-11-07** [`ad951803d6`](https://github.com/sgl-project/sglang/commit/ad951803d6) [#48531](https://github.com/sgl-project/sglang/pull/48531)
  [Perf] [NVIDIA] fp8: Let the Hopper block GEMV take K=6144 for MiniMax M3.1 (#48531)
  _Files: `python/sglang/kernels/ops/gemm/hopper_fp8_block_gemv.py`_
- **2026-11-06** [`c034570cb3`](https://github.com/sgl-project/sglang/commit/c034570cb3) [#48971](https://github.com/sgl-project/sglang/pull/48971)
  [Perf] dsv4: route wo_b and Engram KV MXFP8 GEMMs to cuDNN on CC 10.7 above 8K rows (#48971)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-11-06** [`bfb1a1a0ab`](https://github.com/sgl-project/sglang/commit/bfb1a1a0ab) [#48941](https://github.com/sgl-project/sglang/pull/48941)
  [Perf] layernorm: rmsnorm_mxfp8 on 2 warps for 1280-wide rows; hc_combine_norm loads its weight before the reduction (#48941)
  _Files: `python/sglang/kernels/ops/layernorm/hc_combine_norm.py`, `python/sglang/kernels/ops/layernorm/rmsnorm_mxfp8.py`, `test/registered/kernels/ops/layernorm/test_mxfp8_epilogue.py`_
- **2026-11-06** [`0faab86f78`](https://github.com/sgl-project/sglang/commit/0faab86f78) [#47892](https://github.com/sgl-project/sglang/pull/47892)
  [Fix] quantization: Store --quantization-param-path KV scales the way checkpoint KV scales are stored (#47892)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py`, `test/registered/unit/model_executor/model_runner_components/test_load_kv_cache_scales.py`_
- **2026-11-06** [`732cd768c6`](https://github.com/sgl-project/sglang/commit/732cd768c6) [#41301](https://github.com/sgl-project/sglang/pull/41301)
  [Perf] [NVIDIA] quantization: Add tuned W8A8 block-FP8 GEMM configs for H20 (#41301)
  _Files: `python/sglang/kernels/ops/gemm/configs/N=1280,K=5120,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[32, 32].json`, `python/sglang/kernels/ops/gemm/configs/N=1536,K=5120,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[32, 32].json`, `python/sglang/kernels/ops/gemm/configs/N=1792,K=5120,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[32, 32].json`, `python/sglang/kernels/ops/gemm/configs/N=25600,K=6144,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[32, 32].json` _+7 more__
- **2026-11-06** [`c843608d39`](https://github.com/sgl-project/sglang/commit/c843608d39) [#48726](https://github.com/sgl-project/sglang/pull/48726)
  [CI] [AMD] miles: Skip MI30x FP8 and DeepSeek-V4 tests that cannot run on gfx942 (#48726)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm10-mi30x.yml`_
- **2026-11-06** [`8328c96da9`](https://github.com/sgl-project/sglang/commit/8328c96da9) [#41532](https://github.com/sgl-project/sglang/pull/41532)
  [Feat] [XPU] quant: Add MXFP8 W8A8 compressed-tensors (#41532)
  _Files: `python/sglang/srt/arg_groups/choices.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py` _+9 more__
- **2026-11-05** [`ada4523056`](https://github.com/sgl-project/sglang/commit/ada4523056) [#46964](https://github.com/sgl-project/sglang/pull/46964)
  [Feat] diffusion: Support Hy-Nomas INT8 DiT and FP8 VAE checkpoints (#46964)
  _Files: `docs/cookbook/diffusion/HY-Nomas/HY-Nomas.mdx`, `python/sglang/multimodal_gen/configs/models/dits/nomas.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/base_config.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/quanto_int8_config.py` _+10 more__
- **2026-11-05** [`ab1464c8d3`](https://github.com/sgl-project/sglang/commit/ab1464c8d3) [#38900](https://github.com/sgl-project/sglang/pull/38900)
  [Fix] qwen4: Release loader parameter snapshot before quantization post-processing (#38900)
  _Files: `python/sglang/srt/models/qwen4_exp.py`_
- **2026-11-05** [`6d89ae0d3c`](https://github.com/sgl-project/sglang/commit/6d89ae0d3c) [#35792](https://github.com/sgl-project/sglang/pull/35792)
  [Fix] compressed-tensors: Honor .linear-wrapped ignore entries on fused shards (#35792)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/utils.py`, `test/registered/unit/layers/quantization/test_compressed_tensors_mixed_precision.py`_
- **2026-11-04** [`547e713fb2`](https://github.com/sgl-project/sglang/commit/547e713fb2) [#43786](https://github.com/sgl-project/sglang/pull/43786)
  [Perf] DeepSeek-V4: Fuse inverse RoPE into wo_a FP8 quantization (#43786)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/fp8_wo_a_group_major_quant.cuh`, `python/sglang/kernels/ops/quantization/fp8_group_major_quant_ue8m0.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4.py` _+2 more__
- **2026-11-04** [`3f5b1bec8e`](https://github.com/sgl-project/sglang/commit/3f5b1bec8e) [#47935](https://github.com/sgl-project/sglang/pull/47935)
  [Perf] dsv41: Keep MXFP4 Engram tables packed and decode E2M1 in the gather (#47935)
  _Files: `python/sglang/kernels/ops/embeddings/engram_gather.py`, `python/sglang/srt/layers/engram.py`, `python/sglang/srt/layers/engram_staging.py`, `test/registered/kernels/ops/embeddings/test_engram_gather.py`_
- **2026-11-03** [`f433af22fc`](https://github.com/sgl-project/sglang/commit/f433af22fc) [#47283](https://github.com/sgl-project/sglang/pull/47283)
  [Fix] [AMD] deepseek-v4: Respect AITER selection for Q-LoRA quantization (#47283)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `test/registered/amd/test_dsv4_fused_quant_dispatch.py`_
- **2026-11-03** [`a470d74cdb`](https://github.com/sgl-project/sglang/commit/a470d74cdb) [#46327](https://github.com/sgl-project/sglang/pull/46327)
  [Perf] [AMD] unquant: Pad gfx115x linear and lm_head weight rows to avoid cache aliasing (#46327)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/utils/common.py` _+1 more__
- **2026-11-03** [`2c89ac7cda`](https://github.com/sgl-project/sglang/commit/2c89ac7cda) [#47957](https://github.com/sgl-project/sglang/pull/47957)
  [CI] quant: Lower the Mixtral AWQ MMLU threshold to 0.62 to clear its run-to-run spread (#47957)
  _Files: `test/registered/e2e/quantization/test_awq.py`_
- **2026-11-02** [`fbb847bed6`](https://github.com/sgl-project/sglang/commit/fbb847bed6) [#47503](https://github.com/sgl-project/sglang/pull/47503)
  [Perf] rmsnorm: One SM100-tuned JIT template for plain, fused residual-add and fp8 per-tensor quant (#47503)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/fused_add_rmsnorm.cuh`, `python/sglang/kernels/jit/csrc/elementwise/rmsnorm.cuh`, `python/sglang/kernels/jit/csrc/elementwise/rmsnorm_hf.cuh`, `python/sglang/kernels/ops/layernorm/__init__.py` _+10 more__
- **2026-11-02** [`33c8d723a1`](https://github.com/sgl-project/sglang/commit/33c8d723a1) [#43194](https://github.com/sgl-project/sglang/pull/43194)
  [Fix] diffusion: fix cosmos3 Bugs (#43194)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos_dreams.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos_dreams_transfer.py` _+9 more__

## CI / Build  (20 commits)

- **2026-11-09** [`6a79760533`](https://github.com/sgl-project/sglang/commit/6a79760533) [#49227](https://github.com/sgl-project/sglang/pull/49227)
  [CI] [CPU] cpu-graph: Import STATE_PART from decl instead of router (#49227)
  _Files: `test/registered/cpu/test_cpu_graph.py`_
- **2026-11-09** [`5c5fe25edf`](https://github.com/sgl-project/sglang/commit/5c5fe25edf) [#49318](https://github.com/sgl-project/sglang/pull/49318)
  [Test] npu/glm5.3: Add 2P2D 32P PD-separation perf case (#49318)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/k8s_multi_pd_separation.yaml.jinja2`, `python/sglang/test/ascend/e2e/k8s_multi_pd_separation_green.yaml.jinja2`, `python/sglang/test/ascend/e2e/run_aisbench.sh` _+2 more__
- **2026-11-09** [`e569a3777c`](https://github.com/sgl-project/sglang/commit/e569a3777c) [#49220](https://github.com/sgl-project/sglang/pull/49220)
  [CI] NPU: Bump lb-actions/precision-test to v1.0.9 (#49220)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-11-08** [`8485207289`](https://github.com/sgl-project/sglang/commit/8485207289) [#49201](https://github.com/sgl-project/sglang/pull/49201)
  [Fix] ci: Update the rerun-test reply status when a run is rerun (#49201)
  _Files: `scripts/ci/utils/update_rerun_test_status.py`_
- **2026-11-08** [`cbe0fed913`](https://github.com/sgl-project/sglang/commit/cbe0fed913) [#49128](https://github.com/sgl-project/sglang/pull/49128)
  [Fix] test: Keep a passed precision baseline row pointing at its own tensors (#49128)
  _Files: `python/sglang/test/precision_baseline_store.py`, `test/registered/debug_utils/test_nightly_precision_regression.py`_
- **2026-11-07** [`32d07d269e`](https://github.com/sgl-project/sglang/commit/32d07d269e) [#47828](https://github.com/sgl-project/sglang/pull/47828)
  [Fix] simulator: Lazily import optional AIConfigurator dependency (#47828)
  _Files: `.github/workflows/_pr-test-simulator-cpu.yml`, `tools/sglang-simulator/src/sglang_simulator/simulation/manager/config.py`, `tools/sglang-simulator/src/sglang_simulator/simulation/utils.py`, `tools/sglang-simulator/src/sglang_simulator/time_predictor/__init__.py` _+2 more__
- **2026-11-07** [`512d24195c`](https://github.com/sgl-project/sglang/commit/512d24195c) [#48995](https://github.com/sgl-project/sglang/pull/48995)
  [CI] labeler: Label Reflection Beam PRs and issues (#48995)
  _Files: `.github/labeler.yml`, `.github/workflows/labeler.yml`_
- **2026-11-07** [`5e1774d137`](https://github.com/sgl-project/sglang/commit/5e1774d137) [#48999](https://github.com/sgl-project/sglang/pull/48999)
  [Chore] docker: Remove muse_spark folder (#48999)
  _Files: `docker/muse_spark/apply_deep_gemm_patches.sh`, `docker/muse_spark/deep_gemm.patch`, `docker/muse_spark/muse-spark.Dockerfile`_
- **2026-11-06** [`f4ee6771be`](https://github.com/sgl-project/sglang/commit/f4ee6771be) [#48448](https://github.com/sgl-project/sglang/pull/48448)
  [CI] server_args: Isolate two tests from process state and host hardware (#48448)
  _Files: `test/registered/unit/server_args/test_server_args.py`_
- **2026-11-06** [`51d118a722`](https://github.com/sgl-project/sglang/commit/51d118a722) [#48816](https://github.com/sgl-project/sglang/pull/48816)
  [CI] sgl-router: Stop label events from cancelling and restarting the router tiers (#48816)
  _Files: `.github/workflows/pr-test-rust-exts.yml`, `.github/workflows/pr-test-rust-workspace.yml`, `.github/workflows/pr-test-sgl-router.yml`_
- **2026-11-06** [`08b5a40c51`](https://github.com/sgl-project/sglang/commit/08b5a40c51) [#48799](https://github.com/sgl-project/sglang/pull/48799)
  [CI] [NPU] coverage: publish baseline to OBS only and fail loud on missing data (#48799)
  _Files: `.github/workflows/coverage-collection-npu.yml`, `.github/workflows/pr-test-npu.yml`_
- **2026-11-05** [`622e77207c`](https://github.com/sgl-project/sglang/commit/622e77207c) [#48738](https://github.com/sgl-project/sglang/pull/48738)
  [CI] rerun-test: Tag each test command with its registered CI stage (#48738)
  _Files: `scripts/ci/utils/slash_command_handler.py`_
- **2026-11-05** [`6b0bbd63d3`](https://github.com/sgl-project/sglang/commit/6b0bbd63d3) [#48614](https://github.com/sgl-project/sglang/pull/48614)
  [CI] chore: add CI permissions for QiuMike (weight_cache codeowner) (#48614)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-11-05** [`b147f4aa10`](https://github.com/sgl-project/sglang/commit/b147f4aa10) [#44253](https://github.com/sgl-project/sglang/pull/44253)
  [Feat] simulator: migrate the estimator SDK to AISimulate (#44253)
  _Files: `.github/workflows/_pr-test-simulator-cpu.yml`, `docs/docs/advanced_features/sglang_simulator.mdx`, `tools/sglang-simulator/README.md`, `tools/sglang-simulator/examples/README.md` _+11 more__
- **2026-11-05** [`29e9bbfa85`](https://github.com/sgl-project/sglang/commit/29e9bbfa85) [#48053](https://github.com/sgl-project/sglang/pull/48053)
  [CI] runners: Move H100 tests with no H100-specific dependency to 1-gpu-small (#48053)
- **2026-11-05** [`afea203bd1`](https://github.com/sgl-project/sglang/commit/afea203bd1) [#48104](https://github.com/sgl-project/sglang/pull/48104)
  [Doc] [XPU] Cookbook: Update the XPU Docker version to 0.5.23 (#48104)
  _Files: `docs/docs/hardware-platforms/xpu.mdx`_
- **2026-11-04** [`2120cf1190`](https://github.com/sgl-project/sglang/commit/2120cf1190) [#48279](https://github.com/sgl-project/sglang/pull/48279)
  [Chore] [NVIDIA] docker: Move cu134 container to torch 2.15 official release (#48279)
  _Files: `docker/Dockerfile.cu134`_
- **2026-11-02** [`c04bae2b3f`](https://github.com/sgl-project/sglang/commit/c04bae2b3f) [#44967](https://github.com/sgl-project/sglang/pull/44967)
  [Test] [NPU] kimi_k3: add 128k prefill/decode perf acceptance cases on 4-node mix (#44967)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/gen_dataset_fixed_len.py`, `python/sglang/test/ascend/e2e/run_aisbench.sh`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py` _+2 more__
- **2026-11-02** [`af5731cca6`](https://github.com/sgl-project/sglang/commit/af5731cca6) [#47823](https://github.com/sgl-project/sglang/pull/47823)
  [CI] [NPU] workflow: Gate pr-test-npu-finish on pr-gate and drop nightly PR trigger (#47823)
  _Files: `.github/workflows/nightly-test-npu.yml`, `.github/workflows/pr-test-npu.yml`_
- **2026-11-02** [`e1e0f4ab8c`](https://github.com/sgl-project/sglang/commit/e1e0f4ab8c) [#47611](https://github.com/sgl-project/sglang/pull/47611)
  [Test] [Ascend] npu: Add GLM-5.2 2P2D gpqa cases and unify evalscope retry loop (#47611)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py`_

## ROCm / AMD  (20 commits)

- **2026-11-09** [`f01950a82a`](https://github.com/sgl-project/sglang/commit/f01950a82a) [#49053](https://github.com/sgl-project/sglang/pull/49053)
  [CI] [AMD] spur: Schedule stage-b-test-1-gpu-small-amd-mi35x on the Spur runners (#49053)
  _Files: `.github/workflows/test-amd-mi35x-spur.yml`_
- **2026-11-09** [`d18e36cb82`](https://github.com/sgl-project/sglang/commit/d18e36cb82) [#47899](https://github.com/sgl-project/sglang/pull/47899)
  [Fix] qwen3.5: Keep CPU-offloaded GDN input projections separate (#47899)
  _Files: `python/sglang/srt/models/qwen3_5.py`, `test/registered/amd/test_qwen35_gdn_packed_in_proj.py`, `test/registered/model_loading/test_cpu_offloader.py`_
- **2026-11-09** [`4634c2495c`](https://github.com/sgl-project/sglang/commit/4634c2495c) [#48406](https://github.com/sgl-project/sglang/pull/48406)
  [Perf] [AMD] qwen3: Let the fused QK-norm + RoPE + KV write serve the vectorized_5d layout (#48406)
  _Files: `python/sglang/srt/models/qwen3.py`, `test/registered/amd/test_qwen3_aiter_fused_qk_norm_rope.py`_
- **2026-11-07** [`bf1aa1ab4d`](https://github.com/sgl-project/sglang/commit/bf1aa1ab4d) [#48438](https://github.com/sgl-project/sglang/pull/48438)
  [Test] [AMD] aiter: Run the HD128 ASM prefill test on gfx950 with a routed pool (#48438)
  _Files: `test/registered/amd/test_minimax_hd128_asm_prefill.py`_
- **2026-11-07** [`754185aab5`](https://github.com/sgl-project/sglang/commit/754185aab5) [#48830](https://github.com/sgl-project/sglang/pull/48830)
  [CI] [AMD] spur: Run 1-, 2- and 4-GPU suites on part of a node (#48830)
  _Files: `.github/workflows/test-amd-mi35x-spur.yml`, `scripts/ci/amd/amd_ci_exec.sh`, `scripts/ci/amd/amd_ci_install_dependency.sh`, `scripts/ci/amd/amd_ci_start_container.sh` _+3 more__
- **2026-11-07** [`6220d68645`](https://github.com/sgl-project/sglang/commit/6220d68645) [#48966](https://github.com/sgl-project/sglang/pull/48966)
  [CI] [AMD] hc_mix: Skip the FlyDSL hc_mix dispatch tests when AITER lacks the kernel (#48966)
  _Files: `test/registered/kernels/ops/gemm/test_hc_mix_flydsl.py`_
- **2026-11-07** [`24aa7d00b6`](https://github.com/sgl-project/sglang/commit/24aa7d00b6) [#48978](https://github.com/sgl-project/sglang/pull/48978)
  [CI] [AMD] jit: Use the platform full warp mask in the DSA indexer RoPE helpers (#48978)
  _Files: `python/sglang/kernels/jit/include/sgl_kernel/dsa/indexer_rope.cuh`_
- **2026-11-07** [`9a57115efc`](https://github.com/sgl-project/sglang/commit/9a57115efc) [#49022](https://github.com/sgl-project/sglang/pull/49022)
  [Doc] [AMD] cookbook: Match the Kimi-K3.1-Pro MI35x single-node cells to the current recipe (#49022)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.1-Pro.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.1-pro.jsx`_
- **2026-11-07** [`a240184279`](https://github.com/sgl-project/sglang/commit/a240184279) [#48479](https://github.com/sgl-project/sglang/pull/48479)
  [CI] [AMD] nightly: Add Kimi-K3.1-Pro nightly test (#48479)
  _Files: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_kimi_k31_pro_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_kimi_k31_pro_perf_mi35x.py`, `test/registered/amd/perf/mi35x/test_kimi_k3_perf_mi35x.py` _+1 more__
- **2026-11-06** [`c9431eda6f`](https://github.com/sgl-project/sglang/commit/c9431eda6f) [#48692](https://github.com/sgl-project/sglang/pull/48692)
  [CI] [AMD] spur: Take HF_TOKEN from the runner environment (#48692)
  _Files: `.github/workflows/test-amd-mi35x-spur.yml`, `scripts/ci/slurm/launch_amd_ci_mi35x.sh`_
- **2026-11-05** [`3fa242f27c`](https://github.com/sgl-project/sglang/commit/3fa242f27c) [#44538](https://github.com/sgl-project/sglang/pull/44538)
  [CI] [AMD] spur: Run AMD CI suites on MI35x nodes scheduled through Spur (#44538)
  _Files: `.github/workflows/test-amd-mi35x-spur.yml`, `scripts/ci/amd/amd_ci_exec.sh`, `scripts/ci/amd/amd_ci_install_dependency.sh`, `scripts/ci/amd/amd_ci_start_container.sh` _+3 more__
- **2026-11-05** [`732d34b93c`](https://github.com/sgl-project/sglang/commit/732d34b93c) [#48573](https://github.com/sgl-project/sglang/pull/48573)
  [Chore] [AMD] aiter: promote gfx1250 pin to 07ff5f318 (#48573)
  _Files: `docker/rocm.Dockerfile`_
- **2026-11-05** [`fc7cd5978b`](https://github.com/sgl-project/sglang/commit/fc7cd5978b) [#47940](https://github.com/sgl-project/sglang/pull/47940)
  [Chore] [AMD] rccl: pin rccl to d2e0de35 (#47940)
  _Files: `docker/rocm.Dockerfile`_
- **2026-11-04** [`387843d321`](https://github.com/sgl-project/sglang/commit/387843d321) [#48429](https://github.com/sgl-project/sglang/pull/48429)
  [Doc] cookbook: Run the Kimi-K3.1-Pro MI35x PD Docker commands on the host network with RDMA (#48429)
  _Files: `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/configs/moonshotai/kimi-k3.1-pro.jsx`_
- **2026-11-04** [`045e0e2e2d`](https://github.com/sgl-project/sglang/commit/045e0e2e2d) [#48323](https://github.com/sgl-project/sglang/pull/48323)
  [CI] [AMD] miles: Skip MI30x tests whose kernels exceed gfx942 LDS (#48323)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm10-mi30x.yml`_
- **2026-11-04** [`50ae3312c2`](https://github.com/sgl-project/sglang/commit/50ae3312c2) [#48067](https://github.com/sgl-project/sglang/pull/48067)
  [CI] [AMD] miles: Pass CI and the SGLang source path to nightly suites (#48067)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm10-mi30x.yml`, `.github/workflows/nightly-test-amd-miles-rocm10.yml`_
- **2026-11-04** [`f0eff990d6`](https://github.com/sgl-project/sglang/commit/f0eff990d6) [#48265](https://github.com/sgl-project/sglang/pull/48265)
  [CI] [AMD] miles: Split the MI30x 4-GPU nightly into two jobs (#48265)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm10-mi30x.yml`_
- **2026-11-03** [`a7d535454b`](https://github.com/sgl-project/sglang/commit/a7d535454b) [#48032](https://github.com/sgl-project/sglang/pull/48032)
  [CI] [AMD] nightly-disagg: Run MI355X disagg nightly at 04:00 UTC (12:00 UTC+8) (#48032)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-11-02** [`bde43d6c13`](https://github.com/sgl-project/sglang/commit/bde43d6c13) [#47504](https://github.com/sgl-project/sglang/pull/47504)
  [CI] [AMD] mi355x: Clean up interrupted nightly jobs and reduce runner disk usage (#47504)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`, `scripts/ci/slurm/launch_mi355x.sh`, `scripts/ci/slurm/runner_disk_preflight.py`, `scripts/ci/slurm/test_runner_disk_preflight.py`_
- **2026-11-02** [`16dd97df61`](https://github.com/sgl-project/sglang/commit/16dd97df61) [#46325](https://github.com/sgl-project/sglang/pull/46325)
  [Perf] [AMD] deterministic: Use a fixed-order two-stage all-reduce for large inputs (#46325)
  _Files: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/allreduce/deterministic_all_reduce.hip`, `test/registered/kernels/ops/communication/test_amd_deterministic_allreduce_fixed_order.py`_

## Docs / Examples  (12 commits)

- **2026-11-09** [`5a2645deba`](https://github.com/sgl-project/sglang/commit/5a2645deba) [#49239](https://github.com/sgl-project/sglang/pull/49239)
  [Doc] cookbook: Sort company groups in the sidebar alphabetically (#49239)
  _Files: `.pre-commit-config.yaml`, `docs/docs.json`, `scripts/lint/sort_cookbook_sidebar.py`_
- **2026-11-07** [`b750923a2a`](https://github.com/sgl-project/sglang/commit/b750923a2a) [#48896](https://github.com/sgl-project/sglang/pull/48896)
  [Doc] blogs: Sync LMSYS SGLang blog cards (#48896)
  _Files: `docs/index.mdx`_
- **2026-11-05** [`9ad74f81c2`](https://github.com/sgl-project/sglang/commit/9ad74f81c2) [#48551](https://github.com/sgl-project/sglang/pull/48551)
  [Doc] cookbook: Mirror InferenceX #4811 Kimi-K3.1-Pro GB300 AgentX launches (#48551)
  _Files: `docs/src/snippets/agentx/moonshotai/kimi-k3.1-pro.jsx`_
- **2026-11-05** [`cd83599c6a`](https://github.com/sgl-project/sglang/commit/cd83599c6a) [#48391](https://github.com/sgl-project/sglang/pull/48391)
  [Test] cli: Add cookbook command snapshot and serve direct-launch tests (#48391)
  _Files: `docs/scripts/tests/cookbook-commands-snapshot.test.mjs`, `docs/scripts/tests/cookbook-commands.snapshot.json`, `test/registered/unit/cli/test_serve_backends.py`_
- **2026-11-04** [`b702f0d80e`](https://github.com/sgl-project/sglang/commit/b702f0d80e) [#48435](https://github.com/sgl-project/sglang/pull/48435)
  [Doc] kimi-k3.1: Point the cookbook install branch at kimi-k3.1-day-0 (#48435)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.1-Pro.mdx`_
- **2026-11-04** [`c07df5a055`](https://github.com/sgl-project/sglang/commit/c07df5a055) [#47861](https://github.com/sgl-project/sglang/pull/47861)
  [Doc] cookbook: add Unlimited-OCR-2 NVIDIA platform recipes (#47861)
  _Files: `docs/cookbook/autoregressive/Baidu/Unlimited-OCR-2.mdx`, `docs/src/snippets/configs/baidu/unlimited-ocr-2.jsx`_
- **2026-11-04** [`854bf5a55d`](https://github.com/sgl-project/sglang/commit/854bf5a55d) [#48417](https://github.com/sgl-project/sglang/pull/48417)
  [Doc] popular-models: Feature Kimi-K3.1-Pro first (#48417)
  _Files: `docs/src/snippets/configs/popular-models.jsx`_
- **2026-11-04** [`77c3bcbe2c`](https://github.com/sgl-project/sglang/commit/77c3bcbe2c) [#44506](https://github.com/sgl-project/sglang/pull/44506)
  [Fix] [NPU] glm-ocr: Fix M-RoPE section for GLM-OCR on Ascend and add A3 validation (#44506)
  _Files: `docs/docs/hardware-platforms/ascend-npus/reference/support_models.mdx`, `python/sglang/srt/layers/rotary_embedding/mrope.py`, `test/registered/rotary/test_mrope_axis_map.py`, `test/registered/rotary/test_mrope_npu.py`_
- **2026-11-03** [`40a64e1b5b`](https://github.com/sgl-project/sglang/commit/40a64e1b5b) [#47053](https://github.com/sgl-project/sglang/pull/47053)
  [Doc] kimi-k3: Convert the cookbook page's pipe tables to JSX tables (#47053)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`_
- **2026-11-03** [`133f712a49`](https://github.com/sgl-project/sglang/commit/133f712a49) [#47900](https://github.com/sgl-project/sglang/pull/47900)
  [Doc] cookbook: Align navigation groups with model publishers (#47900)
  _Files: `docs/docs.json`_
- **2026-11-03** [`6c9f5e6d49`](https://github.com/sgl-project/sglang/commit/6c9f5e6d49) [#47997](https://github.com/sgl-project/sglang/pull/47997)
  [Doc] blogs: Sync LMSYS SGLang blog cards (#47997)
  _Files: `docs/index.mdx`_
- **2026-11-02** [`2c362af4cc`](https://github.com/sgl-project/sglang/commit/2c362af4cc) [#47429](https://github.com/sgl-project/sglang/pull/47429)
  [Doc] [NPU] docs: clarify installation and quickstart docs for Ascend NPUs (#47429)
  _Files: `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/quick_start.mdx`_

## Speculative Decoding  (11 commits)

- **2026-11-09** [`86ed6d9c63`](https://github.com/sgl-project/sglang/commit/86ed6d9c63) [#47581](https://github.com/sgl-project/sglang/pull/47581)
  [Perf] [NPU] dspark: Integrate argmax and verify scheduler kernels (#47581)
  _Files: `python/sglang/kernels/ops/sampling/__init__.py`, `python/sglang/kernels/ops/speculative/dspark/dspark_schedule.py`, `test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py`_
- **2026-11-08** [`940fe60b8c`](https://github.com/sgl-project/sglang/commit/940fe60b8c) [#49097](https://github.com/sgl-project/sglang/pull/49097)
  [Test] kv-canary: Serve the EAGLE canary fixture in bf16 to avoid an fp16 overflow (#49097)
  _Files: `python/sglang/test/kv_canary/mode_config.py`_
- **2026-11-07** [`a418db307b`](https://github.com/sgl-project/sglang/commit/a418db307b) [#48833](https://github.com/sgl-project/sglang/pull/48833)
  [Perf] dspark: Build the compact verify window and stage its padded layout in one launch each (#48833)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py`, `python/sglang/kernels/ops/speculative/ragged_verify_kernels.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/speculative/ragged_verify.py` _+2 more__
- **2026-11-05** [`95f1d51213`](https://github.com/sgl-project/sglang/commit/95f1d51213) [#47728](https://github.com/sgl-project/sglang/pull/47728)
  [Fix] dspark: Stage each request's own SWA ring slot at batch size 1 (#47728)
  _Files: `python/sglang/kernels/ops/speculative/dspark/stage_commit.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py`, `test/registered/unit/spec/test_dspark_deferred_commit.py`_
- **2026-11-05** [`8df0cd51e1`](https://github.com/sgl-project/sglang/commit/8df0cd51e1) [#47676](https://github.com/sgl-project/sglang/pull/47676)
  [Perf] [NVIDIA] dsv4: Route padded decode replays through the metadata glue graph (#47676)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/metadata_glue_graph.py`, `test/registered/unit/model_executor/runner/test_decode_cuda_graph_runner.py`, `test/registered/unit/model_executor/runner/test_dsv41_draft_metadata_glue.py` _+1 more__
- **2026-11-04** [`435418253e`](https://github.com/sgl-project/sglang/commit/435418253e) [#47494](https://github.com/sgl-project/sglang/pull/47494)
  [Perf] dspark: Refresh Mamba tracking once per verification step (#47494)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-11-04** [`1097b72f68`](https://github.com/sgl-project/sglang/commit/1097b72f68) [#48111](https://github.com/sgl-project/sglang/pull/48111)
  [Perf] spec: Default `SGLANG_SPEC_TP_SYNC` to `init` (#48111)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/speculative/spec_tp_sync.py`_
- **2026-11-04** [`612cf5c165`](https://github.com/sgl-project/sglang/commit/612cf5c165) [#48244](https://github.com/sgl-project/sglang/pull/48244)
  [Fix] dspark: Expand [N, H] staged embeds in the DeepSeek-V4 DSpark draft forward (#48244)
  _Files: `python/sglang/srt/models/deepseek_v4_dspark.py`_
- **2026-11-04** [`dff6a0c3ac`](https://github.com/sgl-project/sglang/commit/dff6a0c3ac) [#39799](https://github.com/sgl-project/sglang/pull/39799)
  [Fix] mem-cache: Budget the non-DSA EAGLE draft KV pool at its DCP-widened size (#39799)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-11-02** [`aa3e34aaeb`](https://github.com/sgl-project/sglang/commit/aa3e34aaeb) [#45406](https://github.com/sgl-project/sglang/pull/45406)
  [Feat] [NVIDIA] megakernels: Expose hybrid runtime and DSpark verification views (#45406)
  _Files: `python/sglang/kernels/plugin_kernels/nvidia/spec.py`, `python/sglang/srt/kernel_plugins/nvidia/binding.py`, `python/sglang/srt/model_executor/runner/base_runner.py`, `test/registered/unit/kernel_plugins/nvidia/test_eagle_binding.py` _+2 more__
- **2026-11-02** [`f96d5b1ca8`](https://github.com/sgl-project/sglang/commit/f96d5b1ca8) [#47173](https://github.com/sgl-project/sglang/pull/47173)
  [Refactor] [NPU] graph: Remove the NPU graph runner (#47173)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/multi_layer_eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py` _+16 more__

## Models  (7 commits)

- **2026-11-08** [`c2a3982406`](https://github.com/sgl-project/sglang/commit/c2a3982406) [#48370](https://github.com/sgl-project/sglang/pull/48370)
  [Perf] gemma3: Fuse q_norm and k_norm into gemma_rmsnorm for rank above 2 (#48370)
  _Files: `python/sglang/srt/layers/layernorm.py`, `test/registered/layers/test_layernorm_fusion.py`_
- **2026-11-07** [`6d1ce5b894`](https://github.com/sgl-project/sglang/commit/6d1ce5b894) [#49093](https://github.com/sgl-project/sglang/pull/49093)
  [Fix] ernie55: Import layer helpers from their current modules (#49093)
  _Files: `python/sglang/srt/models/ernie55.py`, `python/sglang/srt/models/ernie55_dspark.py`, `python/sglang/srt/models/ernie55_nextn.py`_
- **2026-11-07** [`6de2991cec`](https://github.com/sgl-project/sglang/commit/6de2991cec) [#45534](https://github.com/sgl-project/sglang/pull/45534)
  [Fix] [NVIDIA] DeepSeek-v4.1: scatter the replay tail before the prefill CP gather with DSpark (#45534)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/models/test_deepseek_v4_cp_tail_scatter.py`_
- **2026-11-06** [`6e5d432db2`](https://github.com/sgl-project/sglang/commit/6e5d432db2) [#45798](https://github.com/sgl-project/sglang/pull/45798)
  [Fix] llava: Load LLaVA-1.5 CLIP tower (#45798)
  _Files: `python/sglang/srt/models/clip.py`, `python/sglang/srt/models/llava.py`, `test/registered/unit/models/test_clip.py`_
- **2026-11-05** [`2d5a2f51ab`](https://github.com/sgl-project/sglang/commit/2d5a2f51ab) [#48640](https://github.com/sgl-project/sglang/pull/48640)
  [Test] [NPU] qwen3.6-27b: fail fast on collapsed spec acceptance (#48640)
  _Files: `test/registered/npu/accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in3k5_out1k5_50ms_gpqa.py`_
- **2026-11-04** [`c6f1eef4c9`](https://github.com/sgl-project/sglang/commit/c6f1eef4c9) [#45885](https://github.com/sgl-project/sglang/pull/45885)
  [Feat] nemotron3-embed: Support Nemotron-3-Embed embedding models (#45885)
  _Files: `docs/docs/supported-models/embedding_models.mdx`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/model_overrides/__init__.py`, `python/sglang/srt/arg_groups/model_overrides/nemotron3_embedding.py` _+7 more__
- **2026-11-03** [`4387846672`](https://github.com/sgl-project/sglang/commit/4387846672) [#47810](https://github.com/sgl-project/sglang/pull/47810)
  [Feat] deepseek-recipe: Expose convert and encode_conversation on DeepSeekRecipe (#47810)
  _Files: `python/sglang/srt/parser/deepseek_recipe_renderer.py`, `test/registered/unit/parser/test_deepseek_recipe_renderer.py`_

## Serving / API  (4 commits)

- **2026-11-07** [`fee391881a`](https://github.com/sgl-project/sglang/commit/fee391881a) [#48393](https://github.com/sgl-project/sglang/pull/48393)
  [Fix] kimi-k3: Cap cached_tokens at prompt_tokens in the Rust processor (#48393)
  _Files: `rust/sglang-processor/src/openai/chat.rs`_
- **2026-11-05** [`dac9614d5e`](https://github.com/sgl-project/sglang/commit/dac9614d5e) [#48481](https://github.com/sgl-project/sglang/pull/48481)
  [Fix] kimi-k3: Validate message-level tools and let a forced call override JSON response_format (#48481)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-11-03** [`96301ec478`](https://github.com/sgl-project/sglang/commit/96301ec478) [#45129](https://github.com/sgl-project/sglang/pull/45129)
  [Fix] Anthropic: accept thinking.display="updates" (#45129)
  _Files: `python/sglang/srt/entrypoints/anthropic/protocol.py`, `python/sglang/srt/entrypoints/anthropic/serving.py`, `test/registered/unit/entrypoints/anthropic/test_serving.py`_
- **2026-11-02** [`b45a36531c`](https://github.com/sgl-project/sglang/commit/b45a36531c) [#45972](https://github.com/sgl-project/sglang/pull/45972)
  [Fix] kimi_k3: Use uuid tool_call_id instead of history-count id (#45972)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_

## Structured Output  (4 commits)

- **2026-11-05** [`ebeed89372`](https://github.com/sgl-project/sglang/commit/ebeed89372) [#48480](https://github.com/sgl-project/sglang/pull/48480)
  [Fix] kimi-k3: Make tool_choice required and none grammars end the turn (#48480)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/function_call/kimik3_detector.py`, `python/sglang/srt/function_call/kimik3_structural_tag.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py` _+1 more__
- **2026-11-04** [`a16830deb5`](https://github.com/sgl-project/sglang/commit/a16830deb5) [#48357](https://github.com/sgl-project/sglang/pull/48357)
  [Fix] kimi-k3: Resolve strict tool $refs into the root parameters schema (#48357)
  _Files: `python/sglang/srt/function_call/kimik3_structural_tag.py`, `test/registered/unit/function_call/test_kimik3_structural_tag.py`_
- **2026-11-04** [`851642ade7`](https://github.com/sgl-project/sglang/commit/851642ade7) [#48343](https://github.com/sgl-project/sglang/pull/48343)
  [Fix] openai: Tool schema ids, explicit include_usage=false, and Kimi-K3 prompt fidelity (#48343)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/utils.py`, `python/sglang/srt/function_call/utils.py` _+1 more__
- **2026-11-03** [`035670b685`](https://github.com/sgl-project/sglang/commit/035670b685) [#45466](https://github.com/sgl-project/sglang/pull/45466)
  [Fix] constrained: Do not cache grammar poll timeouts as invalid grammars (#45466)
  _Files: `python/sglang/srt/constrained/grammar_manager.py`, `test/registered/unit/constrained/test_grammar_manager.py`_

## LoRA  (3 commits)

- **2026-11-06** [`3dc9234891`](https://github.com/sgl-project/sglang/commit/3dc9234891) [#48693](https://github.com/sgl-project/sglang/pull/48693)
  [Fix] hicache: Do not count staged-prefetch deferrals while KV awaits a PD transfer (#48693)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/lora/test_lora_pp.py`, `test/registered/unit/managers/test_prefill_adder.py` _+1 more__
- **2026-11-05** [`9b57d1d93f`](https://github.com/sgl-project/sglang/commit/9b57d1d93f) [#48066](https://github.com/sgl-project/sglang/pull/48066)
  [Feat] sgl-router: Add an opt-in fips feature backed by aws-lc-rs (#48066)
  _Files: `.github/workflows/pr-test-sgl-router.yml`, `docker/sgl-router.Dockerfile`, `sgl-router/Cargo.lock`, `sgl-router/Cargo.toml` _+4 more__
- **2026-11-02** [`1ced9a9eb0`](https://github.com/sgl-project/sglang/commit/1ced9a9eb0) [#46251](https://github.com/sgl-project/sglang/pull/46251)
  [Perf] sgl-router: Encode tiktoken models with fastokens under --tokenizer-backend fast (#46251)
  _Files: `sgl-router/REFERENCE.md`, `sgl-router/src/tokenizer/adapter.rs`, `sgl-router/src/tokenizer/mod.rs`, `sgl-router/src/tokenizer/stats.rs` _+7 more__

---
_Generated 2026-11-09 18:41 UTC_