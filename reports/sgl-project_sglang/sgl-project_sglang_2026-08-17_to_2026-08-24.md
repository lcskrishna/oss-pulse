# sgl-project/sglang — Weekly Change Report
**Period:** 2026-08-17 → 2026-08-24  |  **Total commits:** 417

## ✨ New Features This Week

- **2026-08-24** [#36070](https://github.com/sgl-project/sglang/pull/36070) — [diffusion] feat: support loading pruned minimax h3 components natively (#36070)
- **2026-08-24** [#36052](https://github.com/sgl-project/sglang/pull/36052) — [diffusion] feat: support loading self-describing quanto int8 encoders (#36052)
- **2026-08-24** [#36084](https://github.com/sgl-project/sglang/pull/36084) — [diffusion] feat: add per-component quantization overrides (#36084)
- **2026-08-24** [#35072](https://github.com/sgl-project/sglang/pull/35072) — [Intel XPU] support prefill only models for xpu (#35072)
- **2026-08-24** [#36062](https://github.com/sgl-project/sglang/pull/36062) — [diffusion] feat: cache LoRA-merged weights in files the page cache can hold (#36062)
- **2026-08-24** [#32597](https://github.com/sgl-project/sglang/pull/32597) — Support streaming session on NPU (#32597)
- **2026-08-24** [#36086](https://github.com/sgl-project/sglang/pull/36086) — [diffusion] feat: add plain component weight overrides (#36086)
- **2026-08-24** [#36037](https://github.com/sgl-project/sglang/pull/36037) — [diffusion] feat: support loading mixed w4a8 text encoders (#36037)
- **2026-08-24** [#33323](https://github.com/sgl-project/sglang/pull/33323) — [Intel XPU] Add xpu pass for biased_topk and hash_topk (#33323)
- **2026-08-24** [#33840](https://github.com/sgl-project/sglang/pull/33840) — [XPU] Support softmax_lse in sgl_kernel::fwd API (#33840)
- _…and 105 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-24** [`7de80e566c`](https://github.com/sgl-project/sglang/commit/7de80e566c) [#35686](https://github.com/sgl-project/sglang/pull/35686) — [AMD][CI] Name the ROCm Image That Actually Ran in AMD Job Names (#35686)
- **2026-08-24** [`7bbd0ddeb5`](https://github.com/sgl-project/sglang/commit/7bbd0ddeb5) [#36124](https://github.com/sgl-project/sglang/pull/36124) — [AMD] Quark shared-experts gate: recognise a trailing MTP layer (#36124)
- **2026-08-24** [`666b08b4a5`](https://github.com/sgl-project/sglang/commit/666b08b4a5) [#34461](https://github.com/sgl-project/sglang/pull/34461) — [ROCm] Extend the gfx950 extend-attention tile to head_dim <= 128: -43% kernel, -14% TTFT, bit-identical (#34461)
- **2026-08-24** [`97b176e64c`](https://github.com/sgl-project/sglang/commit/97b176e64c) [#32597](https://github.com/sgl-project/sglang/pull/32597) — Support streaming session on NPU (#32597)
- **2026-08-24** [`20064623ab`](https://github.com/sgl-project/sglang/commit/20064623ab) [#35383](https://github.com/sgl-project/sglang/pull/35383) — [AMD][CI] Add the Qwen3.8 MXFP4 MI35x nightly (#35383)
- **2026-08-23** [`95f5ecd3d2`](https://github.com/sgl-project/sglang/commit/95f5ecd3d2) [#35854](https://github.com/sgl-project/sglang/pull/35854) — [AMD] Update amd deepseek v4 cookbook 0822 (#35854)
- **2026-08-23** [`362c2ee849`](https://github.com/sgl-project/sglang/commit/362c2ee849) [#35908](https://github.com/sgl-project/sglang/pull/35908) — config: borrowed-record reads follow the config bags (#35908)
- **2026-08-23** [`155aa26c19`](https://github.com/sgl-project/sglang/commit/155aa26c19) [#36004](https://github.com/sgl-project/sglang/pull/36004) — [AMD][DSV4] perf: use full 1024-thread block for indexer top-k on ROCm (#36004)
- **2026-08-23** [`edd675cecf`](https://github.com/sgl-project/sglang/commit/edd675cecf) [#34490](https://github.com/sgl-project/sglang/pull/34490) — [AMD] Add Radix-4 MoE top-k router kernel for Kimi-K3 routing (#34490)
- **2026-08-22** [`eec794bce0`](https://github.com/sgl-project/sglang/commit/eec794bce0) [#30105](https://github.com/sgl-project/sglang/pull/30105) — [AMD][Spec] Fix aiter GQA packing + split-KV routing in NEXTN spec attention (verify & draft_extend) (#30105)
- **2026-08-22** [`d315eb7250`](https://github.com/sgl-project/sglang/commit/d315eb7250) [#32577](https://github.com/sgl-project/sglang/pull/32577) — [AMD] DeepSeek-V4: add aiter fused mHC post+pre with cross-layer boundary dispatch (#32577)
- **2026-08-22** [`ac179eec11`](https://github.com/sgl-project/sglang/commit/ac179eec11) [#35890](https://github.com/sgl-project/sglang/pull/35890) — fix(disagg): PD transfer-failure injection was silently inert (#35890)
- **2026-08-22** [`0db2bdfec5`](https://github.com/sgl-project/sglang/commit/0db2bdfec5) [#35769](https://github.com/sgl-project/sglang/pull/35769) — Fix buffer-mode HiCache load-back ownership races; add optional prefetch anchor lock (#35769)
- **2026-08-21** [`4d42deff0a`](https://github.com/sgl-project/sglang/commit/4d42deff0a) [#35911](https://github.com/sgl-project/sglang/pull/35911) — chore: bump docs install version to 0.5.18 (#35911)
- **2026-08-21** [`4c98759c73`](https://github.com/sgl-project/sglang/commit/4c98759c73) [#34536](https://github.com/sgl-project/sglang/pull/34536) — [AMD] fix(rocm): support flydsl 0.3.0 in the FlyDSL fused norm kernel (#34536)
- **2026-08-21** [`6a12583679`](https://github.com/sgl-project/sglang/commit/6a12583679) [#35810](https://github.com/sgl-project/sglang/pull/35810) — [AMD] Update ROCm AITER pin to c16d44b (#35810)
- **2026-08-21** [`44c90c6282`](https://github.com/sgl-project/sglang/commit/44c90c6282) [#34973](https://github.com/sgl-project/sglang/pull/34973) — [AMD] DSv4: fuse the qk-norm-rope pair on the MTP target-verify path (#34973)
- **2026-08-21** [`a688682f4b`](https://github.com/sgl-project/sglang/commit/a688682f4b) [#35764](https://github.com/sgl-project/sglang/pull/35764) — [AMD][CI] Fix ROCm 7.0's dead apt index fail the MORI dependency install (#35764)
- **2026-08-21** [`f64080fbaf`](https://github.com/sgl-project/sglang/commit/f64080fbaf) [#34483](https://github.com/sgl-project/sglang/pull/34483) — [AMD] CI: cut two setup cycles from the AMD multimodal-gen lanes (#34483)
- **2026-08-21** [`78c964d9d7`](https://github.com/sgl-project/sglang/commit/78c964d9d7) [#35654](https://github.com/sgl-project/sglang/pull/35654) — [AMD] Retry transient network failures in ROCm Dockerfile curl fetches (#35654)
- **2026-08-21** [`34180a0d35`](https://github.com/sgl-project/sglang/commit/34180a0d35) [#35499](https://github.com/sgl-project/sglang/pull/35499) — [AMD] Improve K3 dspark draft attn kernel perf (#35499)
- **2026-08-21** [`bda9952377`](https://github.com/sgl-project/sglang/commit/bda9952377) [#33166](https://github.com/sgl-project/sglang/pull/33166) — [AMD] DeepSeek-V4 MI355X: eliminate bpreshuffle fp8-scale copies at producer sites (MoE down, MLA o_proj bmm) (#33166)
- **2026-08-21** [`978244d671`](https://github.com/sgl-project/sglang/commit/978244d671) [#27770](https://github.com/sgl-project/sglang/pull/27770) — [P/D disagg] Decode-side radix cache for SWA hybrid models (unified radix tree) (#27770)
- **2026-08-20** [`5a7b26c636`](https://github.com/sgl-project/sglang/commit/5a7b26c636) [#32832](https://github.com/sgl-project/sglang/pull/32832) — [AMD] [sgl-kernel] Bypass caches for peer traffic in ROCm custom all-reduce (#32832)
- **2026-08-20** [`0149f56e84`](https://github.com/sgl-project/sglang/commit/0149f56e84) [#35750](https://github.com/sgl-project/sglang/pull/35750) — [CI] Gate `/rerun-test` on commenter trust and remove `/rerun-stage` (#35750)
- **2026-08-20** [`06ad7b2b0d`](https://github.com/sgl-project/sglang/commit/06ad7b2b0d) [#35603](https://github.com/sgl-project/sglang/pull/35603) — [AMD][CI] Run Both ROCm 7.2.4 and ROCm 7.2.0 Images on Nightly Test AMD (#35603)
- **2026-08-20** [`f386e2a471`](https://github.com/sgl-project/sglang/commit/f386e2a471) [#35602](https://github.com/sgl-project/sglang/pull/35602) — [AMD][CI] Default the ROCm 7.2 PR gate to ROCm 7.2.4 Image (#35602)
- **2026-08-20** [`50dae2d99d`](https://github.com/sgl-project/sglang/commit/50dae2d99d) [#32340](https://github.com/sgl-project/sglang/pull/32340) — Amd/dsv4 shared experts fusion top6 (#32340)
- **2026-08-20** [`02b93e7e01`](https://github.com/sgl-project/sglang/commit/02b93e7e01) [#32570](https://github.com/sgl-project/sglang/pull/32570) — [AMD] Add GLM-5.2 MI35x nightly accuracy and perf benchmark (#32570)
- **2026-08-20** [`09b7af1371`](https://github.com/sgl-project/sglang/commit/09b7af1371) [#34813](https://github.com/sgl-project/sglang/pull/34813) — [CI] Surface AMD ROCm 7.2 state in the PR CI-states block (#34813)
- **2026-08-20** [`dc175b3ad2`](https://github.com/sgl-project/sglang/commit/dc175b3ad2) [#34452](https://github.com/sgl-project/sglang/pull/34452) — [CI][AMD] Run the profiling suite without CUDA graphs on ROCm (#34452)
- **2026-08-20** [`c7478228dd`](https://github.com/sgl-project/sglang/commit/c7478228dd) [#30984](https://github.com/sgl-project/sglang/pull/30984) — [AMD] [Docker] Upgrade Python 3.12 + torch 2.11 + triton 3.7 in ROCm 7.2.4 (#30984)
- **2026-08-20** [`e805a8f98e`](https://github.com/sgl-project/sglang/commit/e805a8f98e) [#34481](https://github.com/sgl-project/sglang/pull/34481) — [AMD] Keep the PTX-inline-asm diffusion norm fusions off on ROCm (fix FLUX warmup crash) (#34481)
- **2026-08-19** [`574274660f`](https://github.com/sgl-project/sglang/commit/574274660f) [#35445](https://github.com/sgl-project/sglang/pull/35445) — [AMD] cookbook: serve Qwen3.5 MXFP4 on MI355X with an fp8_e4m3 KV cache (#35445)
- **2026-08-19** [`f446e853e7`](https://github.com/sgl-project/sglang/commit/f446e853e7) [#33313](https://github.com/sgl-project/sglang/pull/33313) — [AMD] DeepSeek-V4: route decode wo_a bf16 batched matmul to aiter batched_gemm_bf16 (#33313)
- **2026-08-19** [`ce1830c59b`](https://github.com/sgl-project/sglang/commit/ce1830c59b) [#33165](https://github.com/sgl-project/sglang/pull/33165) — [AMD] DeepSeek-V4 MI355X: eliminate bpreshuffle fp8-scale relayout copy in dense w8a8 linear (#33165)
- **2026-08-19** [`ebec85f606`](https://github.com/sgl-project/sglang/commit/ebec85f606) [#35467](https://github.com/sgl-project/sglang/pull/35467) — [AMD][DI][CI] Run MI355X disagg nightly at 7AM UTC (#35467)
- **2026-08-19** [`f4158719d1`](https://github.com/sgl-project/sglang/commit/f4158719d1) [#34485](https://github.com/sgl-project/sglang/pull/34485) — [AMD] Let the diffusion AITer backend take grouped-query K/V (fix Cosmos3-Nano startup) (#34485)
- **2026-08-18** [`f7101b0ae6`](https://github.com/sgl-project/sglang/commit/f7101b0ae6) [#32099](https://github.com/sgl-project/sglang/pull/32099) — [AMD] MiniMax-M3 : Fuse QKV+index proj for block-fp8 (#32099)
- **2026-08-18** [`24d625698d`](https://github.com/sgl-project/sglang/commit/24d625698d) [#31370](https://github.com/sgl-project/sglang/pull/31370) — [AMD] feat(moe): fold padded-topk_ids fill into fused shared-experts append+remap (#31370)
- **2026-08-18** [`a779a2a2a5`](https://github.com/sgl-project/sglang/commit/a779a2a2a5) [#35196](https://github.com/sgl-project/sglang/pull/35196) — [Chore] Move version tag helper to release scripts (#35196)
- **2026-08-18** [`27596abdc0`](https://github.com/sgl-project/sglang/commit/27596abdc0) [#35263](https://github.com/sgl-project/sglang/pull/35263) — [AMD] Update amd k3 cookbook for PR#34580 (#35263)
- **2026-08-18** [`ea27e3ddab`](https://github.com/sgl-project/sglang/commit/ea27e3ddab) [#35200](https://github.com/sgl-project/sglang/pull/35200) — [AMD] Fix Quark Shared Experts Fusion Gate after load-time-override Removal (#35200)
- **2026-08-18** [`9401db3f29`](https://github.com/sgl-project/sglang/commit/9401db3f29) [#35195](https://github.com/sgl-project/sglang/pull/35195) — [AMD] Scope the EAGLE greedy-verify TP broadcast to ROCm only (#35195)
- **2026-08-18** [`8ea5229d42`](https://github.com/sgl-project/sglang/commit/8ea5229d42) [#34985](https://github.com/sgl-project/sglang/pull/34985) — [AMD] Add the Kimi-K3 MI35x perf benchmarks in nightly (#34985)
- **2026-08-18** [`d01812d89e`](https://github.com/sgl-project/sglang/commit/d01812d89e) [#34580](https://github.com/sgl-project/sglang/pull/34580) — [AMD] Optimize KIMI-K3 with Triton MLA decode kernel by tuning the stage-1 geometry for gfx950 (#34580)
- **2026-08-17** [`bc312d185d`](https://github.com/sgl-project/sglang/commit/bc312d185d) [#34926](https://github.com/sgl-project/sglang/pull/34926) — Clean deprecated DeepSeek V4 Environs (#34926)
- **2026-08-17** [`816ea65058`](https://github.com/sgl-project/sglang/commit/816ea65058) [#32568](https://github.com/sgl-project/sglang/pull/32568) — [AMD] Add Kimi-K3 8-GPU MI35x nightly accuracy CI (#32568)
- **2026-08-17** [`c82e928fe5`](https://github.com/sgl-project/sglang/commit/c82e928fe5) [#35111](https://github.com/sgl-project/sglang/pull/35111) — [AMD] diffusion: normalize ModelOpt-FP8 weights to e4m3fnuz on gfx942 (#35111)
- **2026-08-17** [`056808723e`](https://github.com/sgl-project/sglang/commit/056808723e) [#35128](https://github.com/sgl-project/sglang/pull/35128) — [AMD] Guard ROCm 7.0 build from using hipMemcpyBatchAsync (#35128)
- **2026-08-17** [`92bce3d7bb`](https://github.com/sgl-project/sglang/commit/92bce3d7bb) [#30519](https://github.com/sgl-project/sglang/pull/30519) — [AMD] [GLM5] fp8 MLA absorbed bmm for GLM-5.2 on gfx950 (#30519)
- **2026-08-17** [`b83d507cd7`](https://github.com/sgl-project/sglang/commit/b83d507cd7) [#33676](https://github.com/sgl-project/sglang/pull/33676) — [NPU] Support DeepSeek-V4 DSpark and refactor DSV4 cache management (#33676)
- **2026-08-17** [`0099107e8b`](https://github.com/sgl-project/sglang/commit/0099107e8b) [#35105](https://github.com/sgl-project/sglang/pull/35105) — Revert "[AMD] [GLM5] Fuse shared-expert append into aiter grouped-topk (skip per-layer append kernel)" (#35105)
- **2026-08-17** [`eb61cb2823`](https://github.com/sgl-project/sglang/commit/eb61cb2823) [#33480](https://github.com/sgl-project/sglang/pull/33480) — [AMD] Support prefill context parallel two batch overlap for DeepSeek V4 (#33480)
- **2026-08-17** [`8e0499bd50`](https://github.com/sgl-project/sglang/commit/8e0499bd50) [#31323](https://github.com/sgl-project/sglang/pull/31323) — [AMD] [GLM5] Fuse shared-expert append into aiter grouped-topk (skip per-layer append kernel) (#31323)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-08-24 |
| [#33522](https://github.com/sgl-project/sglang/issues/33522) | [Roadmap]Fast Engine Recovery: Weight Cache Daemon | — | 2026-08-24 |
| [#32903](https://github.com/sgl-project/sglang/issues/32903) | [RFC] KVCR as a HiCacheStorage backend for peer-to-peer KV reuse | hicache | 2026-08-24 |
| [#36140](https://github.com/sgl-project/sglang/issues/36140) | [Bug] DFLASH speculative decoding is not supported under PD disaggrega | — | 2026-08-24 |
| [#34340](https://github.com/sgl-project/sglang/issues/34340) | [Bug] Two SM10x-gated cluster/tcgen05 kernels fail on B300 (sm_103): c | — | 2026-08-24 |
| [#33783](https://github.com/sgl-project/sglang/issues/33783) | [Bug] pause_generation(mode="retract") does not fully release RadixCac | — | 2026-08-24 |
| [#30760](https://github.com/sgl-project/sglang/issues/30760) | [Bug] HiCache prefetch all_reduce deadlock with TP=4, no PP — mismatch | — | 2026-08-24 |
| [#36033](https://github.com/sgl-project/sglang/issues/36033) | [PD] Inconsistent prefill→decode failure notification across transfer  | — | 2026-08-23 |
| [#36071](https://github.com/sgl-project/sglang/issues/36071) | [Bug][AMD] DSA dense/k-only decode graph produces all-NaN logits with  | — | 2026-08-23 |
| [#32321](https://github.com/sgl-project/sglang/issues/32321) | [RFC] Replace the MLX runner-stub split with one Torch-owned SRT path  | — | 2026-08-23 |
| [#35860](https://github.com/sgl-project/sglang/issues/35860) | [Playground] Verified cell: Qwen3.8-27B / dgx-spark / nvfp4 / DFLASH2  | — | 2026-08-22 |
| [#35912](https://github.com/sgl-project/sglang/issues/35912) | [Bug] `uv pip install sglang` with uv < 0.12 silently installs 0.5.9 ( | — | 2026-08-21 |
| [#35783](https://github.com/sgl-project/sglang/issues/35783) | [MoonEP] Kimi-K3 production integration roadmap | — | 2026-08-21 |
| [#26890](https://github.com/sgl-project/sglang/issues/26890) | [AITER-Upgrade] AITER Scout Status | — | 2026-08-21 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-08-21 |
| [#32968](https://github.com/sgl-project/sglang/issues/32968) | [Bug][kimi-k3] Long-context [PAD] (id 163839) storms + DSPARK inf/nan  | kimi | 2026-08-21 |
| [#35826](https://github.com/sgl-project/sglang/issues/35826) | [Bug] Grammar token sync initializes a singleton NCCL group under DP a | — | 2026-08-21 |
| [#35789](https://github.com/sgl-project/sglang/issues/35789) | RFC: Re-layer Draft SWA into Committed Sidecar KV and Verify Scratch | — | 2026-08-21 |
| [#35241](https://github.com/sgl-project/sglang/issues/35241) | [Bug] PrefillDelayer can enter a persistent mixed-state feedback loop  | — | 2026-08-21 |
| [#35785](https://github.com/sgl-project/sglang/issues/35785) | Triton version mismatch | — | 2026-08-21 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Multimodal | 96 |
| Attention / FlashInfer | 64 |
| Quantization | 44 |
| Prefill / Decode Disaggregation | 44 |
| MoE / Expert Parallel | 34 |
| KV Cache / Memory | 28 |
| ROCm / AMD | 18 |
| Other | 17 |
| Tensor / Data Parallel | 16 |
| Scheduler / Batching | 11 |
| Triton / Kernels | 8 |
| Models | 8 |
| Docs / Examples | 7 |
| Serving / API | 7 |
| Speculative Decoding | 6 |
| CI / Build | 5 |
| Structured Output | 4 |

## Multimodal  (96 commits)

- **2026-08-24** [`51b27f747a`](https://github.com/sgl-project/sglang/commit/51b27f747a) [#36070](https://github.com/sgl-project/sglang/pull/36070)
  [diffusion] feat: support loading pruned minimax h3 components natively (#36070)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/models/dits/base.py` _+4 more__
- **2026-08-24** [`7de80e566c`](https://github.com/sgl-project/sglang/commit/7de80e566c) [#35686](https://github.com/sgl-project/sglang/pull/35686)
  [AMD][CI] Name the ROCm Image That Actually Ran in AMD Job Names (#35686)
  _Files: `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd-extra.yml` _+5 more__
- **2026-08-24** [`c8e1ddc707`](https://github.com/sgl-project/sglang/commit/c8e1ddc707) [#36062](https://github.com/sgl-project/sglang/pull/36062)
  [diffusion] feat: cache LoRA-merged weights in files the page cache can hold (#36062)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/lora_merge_cache.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py` _+2 more__
- **2026-08-24** [`9866fe910b`](https://github.com/sgl-project/sglang/commit/9866fe910b) [#36024](https://github.com/sgl-project/sglang/pull/36024)
  [diffusion] Speed up LingBot high-quality VAE decode (#36024)
  _Files: `docs/cookbook/diffusion/LingBot-World/LingBot-World-2.0.mdx`, `docs/cookbook/diffusion/LingBot-World/LingBot-World.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/lingbot_world.py` _+6 more__
- **2026-08-24** [`cc74aba330`](https://github.com/sgl-project/sglang/commit/cc74aba330) [#36019](https://github.com/sgl-project/sglang/pull/36019)
  [diffusion] Honor XDG cache for model overlays (#36019)
  _Files: `python/sglang/multimodal_gen/runtime/utils/model_overlay.py`, `python/sglang/multimodal_gen/test/unit/test_model_overlay.py`_
- **2026-08-24** [`6d40b8aebf`](https://github.com/sgl-project/sglang/commit/6d40b8aebf) [#36009](https://github.com/sgl-project/sglang/pull/36009)
  [diffusion] Fix Hunyuan QKV pack indexing at production video shapes (#36009)
  _Files: `python/sglang/kernels/ops/diffusion/rope/hunyuan_qkv_pack_triton.py`, `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-08-24** [`b43931e878`](https://github.com/sgl-project/sglang/commit/b43931e878) [#36016](https://github.com/sgl-project/sglang/pull/36016)
  [diffusion] Refresh quality and BCG benchmark skills (#36016)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md` _+4 more__
- **2026-08-24** [`344613c159`](https://github.com/sgl-project/sglang/commit/344613c159) [#36012](https://github.com/sgl-project/sglang/pull/36012)
  [diffusion] Default Hunyuan VAE to tiled decode (#36012)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan.py`, `python/sglang/multimodal_gen/test/unit/test_hunyuan_config.py`_
- **2026-08-24** [`8dcfb3b5e7`](https://github.com/sgl-project/sglang/commit/8dcfb3b5e7) [#35995](https://github.com/sgl-project/sglang/pull/35995)
  [diffusion] Fuse LongCat-Image QKNorm and interleaved RoPE (#35995)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_rope.cuh`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/rope/qknorm_rope_jit.py`, `python/sglang/multimodal_gen/runtime/models/dits/longcat_image.py` _+3 more__
- **2026-08-24** [`09592f5889`](https://github.com/sgl-project/sglang/commit/09592f5889) [#35993](https://github.com/sgl-project/sglang/pull/35993)
  [diffusion] Keep LongLive2 components resident on large GPUs (#35993)
  _Files: `docs/cookbook/diffusion/LongLive/LongLive-2.0.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/longlive2.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-08-24** [`5ce700aee8`](https://github.com/sgl-project/sglang/commit/5ce700aee8) [#36082](https://github.com/sgl-project/sglang/pull/36082)
  [diffusion] feat: infer LoRA alpha from safetensors metadata (#36082)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/lora/peft_adapter.py`, `python/sglang/multimodal_gen/test/unit/test_lora_peft.py`_
- **2026-08-24** [`f294d51a71`](https://github.com/sgl-project/sglang/commit/f294d51a71) [#35832](https://github.com/sgl-project/sglang/pull/35832)
  [diffusion] fix: fix a refit key error on mapped weights, and stop claiming strides the reload discards (#35832)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-08-24** [`6ca872a11f`](https://github.com/sgl-project/sglang/commit/6ca872a11f) [#36057](https://github.com/sgl-project/sglang/pull/36057)
  [diffusion] chore: fetch metadata beside nested lora weights (#36057)
  _Files: `python/sglang/multimodal_gen/runtime/utils/hf_diffusers_utils.py`, `python/sglang/multimodal_gen/test/unit/test_lora_pipeline.py`_
- **2026-08-24** [`1a368eca1c`](https://github.com/sgl-project/sglang/commit/1a368eca1c) [#36027](https://github.com/sgl-project/sglang/pull/36027)
  [diffusion] optimization: reuse minimax h3 prompt refinement across outputs (#36027)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_denoise_loop.py`_
- **2026-08-24** [`f6fff25756`](https://github.com/sgl-project/sglang/commit/f6fff25756) [#36085](https://github.com/sgl-project/sglang/pull/36085)
  [diffusion] feat: support vae weight-file overrides (#36085)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`, `python/sglang/multimodal_gen/test/unit/test_vae_loader.py`_
- **2026-08-24** [`fee00a41db`](https://github.com/sgl-project/sglang/commit/fee00a41db) [#36078](https://github.com/sgl-project/sglang/pull/36078)
  [diffusion] feat: add composable component weight path cli (#36078)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-08-24** [`e129fe21e5`](https://github.com/sgl-project/sglang/commit/e129fe21e5) [#35981](https://github.com/sgl-project/sglang/pull/35981)
  [diffusion] Flatten Wan VAE RMSNorm row addressing (#35981)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/norm/wan_rmsnorm_silu_triton.py`, `test/registered/kernels/benchmark/diffusion/bench_wan_rmsnorm_silu.py`, `test/registered/kernels/ops/diffusion/test_norm.py`_
- **2026-08-24** [`b2eb0fa51e`](https://github.com/sgl-project/sglang/commit/b2eb0fa51e) [#36000](https://github.com/sgl-project/sglang/pull/36000)
  [diffusion] Keep Cosmos3 Nano resident on high-memory GPUs (#36000)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-08-24** [`f4448e677f`](https://github.com/sgl-project/sglang/commit/f4448e677f) [#35961](https://github.com/sgl-project/sglang/pull/35961)
  [diffusion] Reuse SANA fast paths in SANA-Video BCG (#35961)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/multimodal_gen/runtime/models/dits/sana.py`, `python/sglang/multimodal_gen/runtime/models/dits/sana_video.py` _+1 more__
- **2026-08-23** [`d1af3c8923`](https://github.com/sgl-project/sglang/commit/d1af3c8923) [#36067](https://github.com/sgl-project/sglang/pull/36067)
  [diffusion] feat: support loading native diffusers miniMax h3 components (#36067)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_dit_contract.py`_
- **2026-08-23** [`de6a1dbd7a`](https://github.com/sgl-project/sglang/commit/de6a1dbd7a) [#36080](https://github.com/sgl-project/sglang/pull/36080)
  [diffusion] feat: support hybrid conditioning for minimax h3 (#36080)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/canvas.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/packed_sequence.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/request_validation.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/resolved_plan.py` _+6 more__
- **2026-08-23** [`939c00a7e3`](https://github.com/sgl-project/sglang/commit/939c00a7e3) [#36076](https://github.com/sgl-project/sglang/pull/36076)
  [diffusion] feat: support compact qwen3-vl conditioning for minimax h3 (#36076)
  _Files: `python/sglang/multimodal_gen/configs/models/encoders/minimax_h3_qwen3vl.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/models/encoders/base.py`, `python/sglang/multimodal_gen/runtime/models/encoders/minimax_h3_qwen3vl.py` _+2 more__
- **2026-08-23** [`886e37a649`](https://github.com/sgl-project/sglang/commit/886e37a649) [#36051](https://github.com/sgl-project/sglang/pull/36051)
  [diffusion] CI: guard the anonymous-host budget alongside peak VRAM (#36051)
  _Files: `python/sglang/multimodal_gen/runtime/loader/weight_utils.py`, `python/sglang/multimodal_gen/runtime/utils/perf_logger.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/5090.json`, `python/sglang/multimodal_gen/test/server/test_server_common.py` _+2 more__
- **2026-08-23** [`e3a008a9db`](https://github.com/sgl-project/sglang/commit/e3a008a9db) [#36034](https://github.com/sgl-project/sglang/pull/36034)
  [diffusion] UX: clean up startup and offload logs (#36034)
  _Files: `python/sglang/multimodal_gen/registry.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/base_device_communicator.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/cpu_communicator.py`, `python/sglang/multimodal_gen/runtime/distributed/group_coordinator.py` _+6 more__
- **2026-08-23** [`340391a297`](https://github.com/sgl-project/sglang/commit/340391a297) [#35910](https://github.com/sgl-project/sglang/pull/35910)
  config: publish before the launcher reads effective configuration (#35910)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/runtime_context.py`, `test/registered/unit/multimodal/test_gpu_feature_transport.py` _+4 more__
- **2026-08-23** [`bd3cc97e7e`](https://github.com/sgl-project/sglang/commit/bd3cc97e7e) [#36032](https://github.com/sgl-project/sglang/pull/36032)
  [diffusion] CI: let the 5090 consumer case runs two warm requests on the full recipe (#36032)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/5090.json`, `python/sglang/multimodal_gen/test/server/test_server_common.py`, `python/sglang/multimodal_gen/test/server/testcase_configs.py`_
- **2026-08-23** [`97ae27893a`](https://github.com/sgl-project/sglang/commit/97ae27893a) [#35734](https://github.com/sgl-project/sglang/pull/35734)
  [diffusion] feat: release a layerwise component's non-layer weights between uses (#35734)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_residency_strategies.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-08-23** [`bbbcbf9418`](https://github.com/sgl-project/sglang/commit/bbbcbf9418) [#35997](https://github.com/sgl-project/sglang/pull/35997)
  [diffusion] fix: stabilize ltx-2.3 two-stage cold requests (#35997)
  _Files: `python/sglang/multimodal_gen/runtime/warmup_request_builder.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/unit/test_cfg_parallel_warmup.py`_
- **2026-08-23** [`59cdc9de7d`](https://github.com/sgl-project/sglang/commit/59cdc9de7d) [#35986](https://github.com/sgl-project/sglang/pull/35986)
  [diffusion] chore: re-home decode-dtype vae weights to a file-backed store (#35986)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/test/unit/test_vae_decoder_store.py`_
- **2026-08-23** [`7f30d66045`](https://github.com/sgl-project/sglang/commit/7f30d66045) [#35305](https://github.com/sgl-project/sglang/pull/35305)
  [Kimi-K3] Fix "wrong grids" crash in DP-sharded vision preprocessing (#35305)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/multimodal_gen/test/unit/test_cpp_extension_loader.py`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/models/test_kimi_k3_vision.py`_
- **2026-08-22** [`7d22b7a875`](https://github.com/sgl-project/sglang/commit/7d22b7a875) [#35816](https://github.com/sgl-project/sglang/pull/35816)
  [diffusion] docs: add tuning guide for h3 on consumer-level gpu (#35816)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/scripts/check_cookbook_configs.mjs`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx`_
- **2026-08-22** [`0b064e3739`](https://github.com/sgl-project/sglang/commit/0b064e3739) [#35352](https://github.com/sgl-project/sglang/pull/35352)
  [diffusion] comfyui: add a minimax-h3 node and a generic extra-fields passthrough (#35352)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/SKILL.md`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/README.md`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/server_api.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/nodes.py` _+1 more__
- **2026-08-22** [`46cb12ab45`](https://github.com/sgl-project/sglang/commit/46cb12ab45) [#35989](https://github.com/sgl-project/sglang/pull/35989)
  [diffusion] fix: fix hunyuan3d stale extension lock hangs (#35989)
  _Files: `python/pyproject.toml`, `python/sglang/kernels/ops/diffusion/ext/loader.py`, `python/sglang/multimodal_gen/test/unit/test_cpp_extension_loader.py`_
- **2026-08-22** [`db570fe619`](https://github.com/sgl-project/sglang/commit/db570fe619) [#35812](https://github.com/sgl-project/sglang/pull/35812)
  [diffusion] chore: let the auto policy select h3's dit for layerwise offload (#35812)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/server_args/auto_tune.py`_
- **2026-08-22** [`61981e1fcd`](https://github.com/sgl-project/sglang/commit/61981e1fcd) [#35967](https://github.com/sgl-project/sglang/pull/35967)
  [diffusion] optimization: keep vae decoder weights in their decode dtype from load (#35967)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/test/unit/test_vae_loader_decode_dtype.py`_
- **2026-08-22** [`a8c16b2e55`](https://github.com/sgl-project/sglang/commit/a8c16b2e55) [#35946](https://github.com/sgl-project/sglang/pull/35946)
  [diffusion] feature: use the directory for the vae mapping gate (#35946)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/test/unit/test_vae_loader.py`_
- **2026-08-22** [`382343f860`](https://github.com/sgl-project/sglang/commit/382343f860) [#35882](https://github.com/sgl-project/sglang/pull/35882)
  [diffusion] optimization: transfer mapped layers through a courier thread (#35882)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/host_memory_budget.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py` _+4 more__
- **2026-08-22** [`90354326c7`](https://github.com/sgl-project/sglang/commit/90354326c7) [#35463](https://github.com/sgl-project/sglang/pull/35463)
  [VLM] Split Pixtral multi-image features before the CUDA IPC wrap (#35463)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/pixtral.py`, `test/registered/unit/multimodal/test_pixtral_processor.py`_
- **2026-08-22** [`96bfd2476c`](https://github.com/sgl-project/sglang/commit/96bfd2476c) [#35729](https://github.com/sgl-project/sglang/pull/35729)
  [diffusion] Enable SANA-Video breakable CUDA graphs (#35729)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-performance/SKILL.md`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/model_padders/sana_video.py` _+3 more__
- **2026-08-22** [`83e9ece672`](https://github.com/sgl-project/sglang/commit/83e9ece672) [#35695](https://github.com/sgl-project/sglang/pull/35695)
  [diffusion] Fuse SANA-Video interleaved RoPE (#35695)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/jit/csrc/diffusion/interleaved_rope_fp64.cuh`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py` _+5 more__
- **2026-08-22** [`5290327025`](https://github.com/sgl-project/sglang/commit/5290327025) [#35939](https://github.com/sgl-project/sglang/pull/35939)
  [diffusion] feat: resolve hub component subfolders (#35939)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/pipelines_core/composed_pipeline_base.py`, `python/sglang/multimodal_gen/test/unit/test_hf_diffusers_utils.py`_
- **2026-08-22** [`0be2a209ac`](https://github.com/sgl-project/sglang/commit/0be2a209ac) [#35867](https://github.com/sgl-project/sglang/pull/35867)
  [diffusion] refactor: hand out pinned host memory per layer (#35867)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-08-22** [`22dafbcbd9`](https://github.com/sgl-project/sglang/commit/22dafbcbd9) [#35862](https://github.com/sgl-project/sglang/pull/35862)
  [diffusion] feat: keep a cpu-started vae weights on the checkpoint mapping (#35862)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/runtime/loader/utils.py`, `python/sglang/multimodal_gen/test/unit/test_vae_loader.py`_
- **2026-08-21** [`932f632158`](https://github.com/sgl-project/sglang/commit/932f632158) [#35745](https://github.com/sgl-project/sglang/pull/35745)
  [diffusion] fix: do not warn that the recommended short edge is unverified (#35745)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/request_validation.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_short_edge.py`_
- **2026-08-21** [`5a46d657b7`](https://github.com/sgl-project/sglang/commit/5a46d657b7) [#35774](https://github.com/sgl-project/sglang/pull/35774)
  [diffusion] refactor: resolve lora weight sources deterministically (#35774)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/utils/hf_diffusers_utils.py`, `python/sglang/multimodal_gen/runtime/weights/__init__.py`, `python/sglang/multimodal_gen/runtime/weights/source.py` _+2 more__
- **2026-08-21** [`5206f11543`](https://github.com/sgl-project/sglang/commit/5206f11543) [#35813](https://github.com/sgl-project/sglang/pull/35813)
  [diffusion] fix: stop the mapped-weight store from holding the parameter itself (#35813)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-08-21** [`a5c52a9358`](https://github.com/sgl-project/sglang/commit/a5c52a9358) [#35724](https://github.com/sgl-project/sglang/pull/35724)
  [diffusion] Enable LongCat breakable CUDA graphs (#35724)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-performance/SKILL.md`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/model_padders/longcat_image.py` _+3 more__
- **2026-08-21** [`4c98759c73`](https://github.com/sgl-project/sglang/commit/4c98759c73) [#34536](https://github.com/sgl-project/sglang/pull/34536)
  [AMD] fix(rocm): support flydsl 0.3.0 in the FlyDSL fused norm kernel (#34536)
  _Files: `python/sglang/kernels/ops/diffusion/norm/fused_residual_norm_flydsl.py`_
- **2026-08-21** [`f64080fbaf`](https://github.com/sgl-project/sglang/commit/f64080fbaf) [#34483](https://github.com/sgl-project/sglang/pull/34483)
  [AMD] CI: cut two setup cycles from the AMD multimodal-gen lanes (#34483)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `scripts/ci/utils/ci_coverage_report.py`_
- **2026-08-21** [`6127d1daee`](https://github.com/sgl-project/sglang/commit/6127d1daee) [#35701](https://github.com/sgl-project/sglang/pull/35701)
  [diffusion] feat: allow offloaded weights stay on the checkpoint mapping (#35701)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/runtime/loader/utils.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/host_memory_budget.py` _+5 more__
- **2026-08-21** [`7e80e889a2`](https://github.com/sgl-project/sglang/commit/7e80e889a2) [#35698](https://github.com/sgl-project/sglang/pull/35698)
  [diffusion] Fuse LTX-2.5 decoder 3D RoPE (#35698)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/jit/csrc/diffusion/ltx25_decoder_rope.cuh`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py` _+5 more__
- **2026-08-21** [`5bb981dce1`](https://github.com/sgl-project/sglang/commit/5bb981dce1) [#35707](https://github.com/sgl-project/sglang/pull/35707)
  [diffusion] chore: read the cgroup this process is actually in (#35707)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/host_memory_budget.py`, `python/sglang/multimodal_gen/test/unit/test_host_memory_budget.py`_
- **2026-08-20** [`ba8e601358`](https://github.com/sgl-project/sglang/commit/ba8e601358) [#35761](https://github.com/sgl-project/sglang/pull/35761)
  [docs] fix note formatting in sglang-d documentation (#35761)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `docs/docs/sglang-diffusion/deployment_cookbook.mdx`_
- **2026-08-20** [`0f744b6848`](https://github.com/sgl-project/sglang/commit/0f744b6848) [#29656](https://github.com/sgl-project/sglang/pull/29656)
  feat: make mm_inputs msgpack-native (#29656)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/models/nano_nemotron_vl.py`, `python/sglang/srt/multimodal/evs/evs_module.py` _+5 more__
- **2026-08-20** [`23cb04093c`](https://github.com/sgl-project/sglang/commit/23cb04093c) [#35700](https://github.com/sgl-project/sglang/pull/35700)
  fix(multimodal): keep LLaVA image fetch off the CPU-preprocess timeout budget (flaky test_mixed_batch) (#35700)
  _Files: `python/sglang/srt/multimodal/processors/llava.py`_
- **2026-08-20** [`81df6f2c57`](https://github.com/sgl-project/sglang/commit/81df6f2c57) [#35610](https://github.com/sgl-project/sglang/pull/35610)
  [MUSA] Harden CI dependencies and diffusion warmup (#35610)
  _Files: `.github/workflows/nightly-test-musa.yml`, `.github/workflows/pr-test-musa.yml`, `python/sglang/multimodal_gen/test/server/musa/testcase_configs_musa.py`, `scripts/ci/musa/musa_install_dependency.sh` _+2 more__
- **2026-08-20** [`be373395b4`](https://github.com/sgl-project/sglang/commit/be373395b4) [#35713](https://github.com/sgl-project/sglang/pull/35713)
  [diffusion] feat: support out-of-tree models and pipelines (#35713)
  _Files: `docs/docs/sglang-diffusion/environment_variables.mdx`, `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/registry.py` _+4 more__
- **2026-08-20** [`7f8f030000`](https://github.com/sgl-project/sglang/commit/7f8f030000) [#35688](https://github.com/sgl-project/sglang/pull/35688)
  [diffusion] feat: let every layerwise component be configurable (#35688)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-08-20** [`04444ee352`](https://github.com/sgl-project/sglang/commit/04444ee352) [#35679](https://github.com/sgl-project/sglang/pull/35679)
  [diffusion] Refresh eager optimization skills and benchmark safeguards (#35679)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md` _+3 more__
- **2026-08-20** [`97efc0507c`](https://github.com/sgl-project/sglang/commit/97efc0507c) [#35641](https://github.com/sgl-project/sglang/pull/35641)
  [diffusion] feat: plan pinned host memory against the cgroup cap not the machine (#35641)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/host_memory_budget.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_host_memory_budget.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-08-20** [`cf3813f4ce`](https://github.com/sgl-project/sglang/commit/cf3813f4ce) [#35668](https://github.com/sgl-project/sglang/pull/35668)
  [diffusion] feat: add weight source reader (#35668)
  _Files: `python/sglang/multimodal_gen/runtime/loader/weight_readers/__init__.py`, `python/sglang/multimodal_gen/runtime/loader/weight_readers/base.py`, `python/sglang/multimodal_gen/runtime/loader/weight_readers/runai_streamer.py`, `python/sglang/multimodal_gen/runtime/loader/weight_readers/safetensors_mmap.py` _+2 more__
- **2026-08-20** [`17313cf4b2`](https://github.com/sgl-project/sglang/commit/17313cf4b2) [#35511](https://github.com/sgl-project/sglang/pull/35511)
  [diffusion] CI: add minimax-h3 ref2va audio consistency coverage and guard peak vram (#35511)
  _Files: `.github/workflows/pr-test-multimodal-gen.yml`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/composed_pipeline_base.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/reference_encoding.py` _+20 more__
- **2026-08-20** [`f1b9a1f42a`](https://github.com/sgl-project/sglang/commit/f1b9a1f42a) [#35664](https://github.com/sgl-project/sglang/pull/35664)
  [diffusion] feat: support unverified short edge instead of rejecting it for minimax-h3 (#35664)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/constants.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/request_validation.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/resolved_plan.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_short_edge.py`_
- **2026-08-20** [`06ad7b2b0d`](https://github.com/sgl-project/sglang/commit/06ad7b2b0d) [#35603](https://github.com/sgl-project/sglang/pull/35603)
  [AMD][CI] Run Both ROCm 7.2.4 and ROCm 7.2.0 Images on Nightly Test AMD (#35603)
  _Files: `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/bot-bump-sglang-version.yml`, `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/release-branch-cut.yml`_
- **2026-08-20** [`f386e2a471`](https://github.com/sgl-project/sglang/commit/f386e2a471) [#35602](https://github.com/sgl-project/sglang/pull/35602)
  [AMD][CI] Default the ROCm 7.2 PR gate to ROCm 7.2.4 Image (#35602)
  _Files: `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/pr-test-amd-extra.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/release-branch-cut.yml`_
- **2026-08-20** [`b8996a5ab2`](https://github.com/sgl-project/sglang/commit/b8996a5ab2) [#35626](https://github.com/sgl-project/sglang/pull/35626)
  [diffusion] fix: keep large vocab tables in host memory under layerwise offload (#35626)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen3vl.py`, `python/sglang/multimodal_gen/runtime/models/encoders/t5.py`, `python/sglang/multimodal_gen/test/unit/test_host_resident_vocab_table.py`_
- **2026-08-20** [`7ba3430365`](https://github.com/sgl-project/sglang/commit/7ba3430365) [#33730](https://github.com/sgl-project/sglang/pull/33730)
  Fix Grok-2 nightly: derive image-understanding capability from is_multimodal (#33730)
  _Files: `python/sglang/srt/configs/model_config.py`_
- **2026-08-20** [`f744607567`](https://github.com/sgl-project/sglang/commit/f744607567) [#35618](https://github.com/sgl-project/sglang/pull/35618)
  [diffusion] UX: report where a component's weights are (#35618)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/utils.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_component_residency_report.py`_
- **2026-08-20** [`db2eb47500`](https://github.com/sgl-project/sglang/commit/db2eb47500) [#35612](https://github.com/sgl-project/sglang/pull/35612)
  [diffusion] fix: keep cosmos3 T=1 fusion on blackwell only (#35612)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`_
- **2026-08-20** [`a3e4592f89`](https://github.com/sgl-project/sglang/commit/a3e4592f89) [#35615](https://github.com/sgl-project/sglang/pull/35615)
  [diffusion] CI: use canonical residency selector in nightly (#35615)
  _Files: `scripts/ci/utils/diffusion/comparison_configs.json`_
- **2026-08-20** [`3b22f4f000`](https://github.com/sgl-project/sglang/commit/3b22f4f000) [#35614](https://github.com/sgl-project/sglang/pull/35614)
  [diffusion] UX: reduce per-request log noise (#35614)
  _Files: `python/sglang/multimodal_gen/runtime/models/adapter/ltx_2_duration_head.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/longcat_image.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/duration.py`_
- **2026-08-20** [`f65961844a`](https://github.com/sgl-project/sglang/commit/f65961844a) [#35587](https://github.com/sgl-project/sglang/pull/35587)
  docker: fix CUDA-13 build — rename NCCL_VERSION ARG to avoid base image ENV collision (#35587)
  _Files: `docker/Dockerfile`_
- **2026-08-20** [`1f87d8f512`](https://github.com/sgl-project/sglang/commit/1f87d8f512) [#35538](https://github.com/sgl-project/sglang/pull/35538)
  [diffusion] fix: stop reserving nccl device buffers for single-rank groups (#35538)
  _Files: `python/sglang/multimodal_gen/runtime/cache/cache_dit_integration.py`, `python/sglang/multimodal_gen/runtime/distributed/group_coordinator.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_groups.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py` _+1 more__
- **2026-08-20** [`e805a8f98e`](https://github.com/sgl-project/sglang/commit/e805a8f98e) [#34481](https://github.com/sgl-project/sglang/pull/34481)
  [AMD] Keep the PTX-inline-asm diffusion norm fusions off on ROCm (fix FLUX warmup crash) (#34481)
  _Files: `python/sglang/kernels/ops/diffusion/norm/layernorm_modulate_triton.py`, `python/sglang/kernels/ops/diffusion/norm/rmsnorm_scale_shift_bitexact.py`, `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-08-19** [`defb2a3100`](https://github.com/sgl-project/sglang/commit/defb2a3100) [#33606](https://github.com/sgl-project/sglang/pull/33606)
  feat(openai): Accept the input_audio content part in chat completions (#33606)
  _Files: `docs/cookbook/autoregressive/Google/Gemma4.mdx`, `docs/cookbook/autoregressive/ThinkingMachines/Inkling-Small.mdx`, `docs/cookbook/autoregressive/ThinkingMachines/Inkling.mdx`, `python/sglang/srt/entrypoints/openai/protocol.py` _+2 more__
- **2026-08-19** [`29f5d1c7c3`](https://github.com/sgl-project/sglang/commit/29f5d1c7c3) [#35509](https://github.com/sgl-project/sglang/pull/35509)
  [diffusion] fix: fix multi-group layerwise offload startup memory (#35509)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-08-19** [`c57ada81e1`](https://github.com/sgl-project/sglang/commit/c57ada81e1) [#34612](https://github.com/sgl-project/sglang/pull/34612)
  [Diffusion]  Use current_platform instead of hardcoded "cuda" in cosmos3 guardrails  (#34612)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3_guardrails.py`_
- **2026-08-19** [`3e5ce26c2d`](https://github.com/sgl-project/sglang/commit/3e5ce26c2d) [#32611](https://github.com/sgl-project/sglang/pull/32611)
  fix: fix transcription & audio-understanding for ASR/audio/speech models (#32611)
  _Files: `python/sglang/srt/entrypoints/openai/transcription_adapters/__init__.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/glmasr.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/granite_speech.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/qwen2_audio.py` _+6 more__
- **2026-08-19** [`9113fc6d93`](https://github.com/sgl-project/sglang/commit/9113fc6d93) [#35436](https://github.com/sgl-project/sglang/pull/35436)
  [docs] Add a fused-kernels page for SGLang Diffusion (#35436)
  _Files: `docs/docs.json`, `docs/docs/sglang-diffusion/fused_kernels.mdx`, `docs/docs/sglang-diffusion/performance-optimization.mdx`_
- **2026-08-19** [`4cef72faee`](https://github.com/sgl-project/sglang/commit/4cef72faee) [#35006](https://github.com/sgl-project/sglang/pull/35006)
  [diffusion] refactor: reuse srt qwen vision and text modules (#35006)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/minimax_h3_qwen3vl.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen2_5vl.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen2_5vl_vision.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen3.py` _+22 more__
- **2026-08-19** [`77fc5c128e`](https://github.com/sgl-project/sglang/commit/77fc5c128e) [#35318](https://github.com/sgl-project/sglang/pull/35318)
  [perf] overlap page preprocessing, pack the vit, enable prefill CUDA graph for paddle-ocr (#35318)
  _Files: `docs/cookbook/autoregressive/Baidu/PaddleOCR-VL.mdx`, `docs/cookbook/autoregressive/Baidu/Unlimited-OCR.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+9 more__
- **2026-08-18** [`3f26febaff`](https://github.com/sgl-project/sglang/commit/3f26febaff) [#34713](https://github.com/sgl-project/sglang/pull/34713)
  [diffusion] fix: decouple encoder parallelism from the dit parallel layout (#34713)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/encoder_parallel.mdx`, `python/sglang/multimodal_gen/configs/models/encoders/base.py` _+9 more__
- **2026-08-18** [`c60952d933`](https://github.com/sgl-project/sglang/commit/c60952d933) [#35238](https://github.com/sgl-project/sglang/pull/35238)
  Exclude multimodal-gen NPU jobs from fast-fail cascade (#35238)
  _Files: `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/pr-test-npu.yml`_
- **2026-08-18** [`94eef833fe`](https://github.com/sgl-project/sglang/commit/94eef833fe) [#34197](https://github.com/sgl-project/sglang/pull/34197)
  [diffusion] rl: support cosmos3 (#34197)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`, `python/sglang/multimodal_gen/runtime/post_training/rollout_scheduler.py`, `python/sglang/multimodal_gen/runtime/post_training/weights_updater.py`, `python/sglang/multimodal_gen/test/unit/test_cosmos3_rollout.py`_
- **2026-08-18** [`ae6945e112`](https://github.com/sgl-project/sglang/commit/ae6945e112) [#35114](https://github.com/sgl-project/sglang/pull/35114)
  [kernels] Reorganize ops/diffusion by operator domain behind a lazy facade (#35114)
- **2026-08-18** [`70ee6b1714`](https://github.com/sgl-project/sglang/commit/70ee6b1714) [#35125](https://github.com/sgl-project/sglang/pull/35125)
  [Rust Server] Add e2e latency metadata and fix Sarashina import (#35125)
  _Files: `python/sglang/srt/models/sarashina2_vision.py`, `rust/sglang-server/src/api_server/native_api.rs`_
- **2026-08-18** [`667389c50f`](https://github.com/sgl-project/sglang/commit/667389c50f) [#35107](https://github.com/sgl-project/sglang/pull/35107)
  [diffusion] chore: filter transformer safetensors by index.json to drop duplicate shard variants (#35107)
  _Files: `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`_
- **2026-08-18** [`772018fe36`](https://github.com/sgl-project/sglang/commit/772018fe36) [#34933](https://github.com/sgl-project/sglang/pull/34933)
  [diffusion] Per-section LoRA adapters on fused linear layers (#34933)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/runtime/pipelines/cosmos3_pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora_pipeline.py`, `python/sglang/multimodal_gen/runtime/post_training/weights_updater.py` _+1 more__
- **2026-08-18** [`61600c9f39`](https://github.com/sgl-project/sglang/commit/61600c9f39) [#31453](https://github.com/sgl-project/sglang/pull/31453)
  [Diffusion][Refactor] Refactor and extract complex RoPE implementation to layers/rotary_embedding for MOVA DiT (#31453)
  _Files: `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/__init__.py`, `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/utils.py`, `python/sglang/multimodal_gen/runtime/models/dits/mova_video_dit.py`_
- **2026-08-17** [`2b278b4ac4`](https://github.com/sgl-project/sglang/commit/2b278b4ac4) [#35022](https://github.com/sgl-project/sglang/pull/35022)
  config: retire the multi-engine accommodation in the runtime context (#35022)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/runtime_context.py` _+4 more__
- **2026-08-17** [`d97b796c16`](https://github.com/sgl-project/sglang/commit/d97b796c16) [#35004](https://github.com/sgl-project/sglang/pull/35004)
  [diffusion] chore: reuse SRT CLIP encoder blocks (#35004)
  _Files: `python/sglang/multimodal_gen/configs/models/encoders/base.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/models/encoders/base.py` _+17 more__
- **2026-08-17** [`e9ad8102a2`](https://github.com/sgl-project/sglang/commit/e9ad8102a2) [#34992](https://github.com/sgl-project/sglang/pull/34992)
  [diffusion] chore: reuse SRT SigLIP in Pi0.5 (#34992)
  _Files: `docs/cookbook/vla/OpenPI/Pi0.5.mdx`, `python/sglang/multimodal_gen/runtime/models/vlas/pi05_core.py`, `python/sglang/multimodal_gen/runtime/models/vlas/pi05_policy.py`, `python/sglang/multimodal_gen/test/unit/test_pi05_runtime_helpers.py` _+1 more__
- **2026-08-17** [`f33b83b4cc`](https://github.com/sgl-project/sglang/commit/f33b83b4cc) [#34940](https://github.com/sgl-project/sglang/pull/34940)
  [diffusion] fix: fix h3 swap peft SwiGLU lora_B halves when loading FFN Lora (#34940)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/lora_pipeline.py`_
- **2026-08-17** [`744740dbea`](https://github.com/sgl-project/sglang/commit/744740dbea) [#31751](https://github.com/sgl-project/sglang/pull/31751)
  [XPU] upgrade sglang xpu backend to PyTorch 2.13 (#31751)
  _Files: `docker/xpu.Dockerfile`, `docs/docs/hardware-platforms/xpu.mdx`, `docs/docs/sglang-diffusion/installation.mdx`, `python/pyproject_xpu.toml` _+1 more__
- **2026-08-17** [`eafbe2cb6f`](https://github.com/sgl-project/sglang/commit/eafbe2cb6f) [#34818](https://github.com/sgl-project/sglang/pull/34818)
  [CI] Install sgl-eval in xeon (CPU) Docker image (#34818)
  _Files: `docker/xeon.Dockerfile`_
- **2026-08-17** [`0aa09ab40d`](https://github.com/sgl-project/sglang/commit/0aa09ab40d) [#34930](https://github.com/sgl-project/sglang/pull/34930)
  [diffusion] Reuse bit-exact modulation fast path for LTX-2.3 (#34930)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `test/registered/kernels/ops/diffusion/test_ltx2_rms_norm_modulate.py`_

## Attention / FlashInfer  (64 commits)

- **2026-08-24** [`5c4622341f`](https://github.com/sgl-project/sglang/commit/5c4622341f) [#35775](https://github.com/sgl-project/sglang/pull/35775)
  [GDN] remove XPU path of causal_conv1d_fn and causal_conv1d_update (#35775)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`_
- **2026-08-24** [`2070927e00`](https://github.com/sgl-project/sglang/commit/2070927e00) [#34462](https://github.com/sgl-project/sglang/pull/34462)
  [Triton] Bound the sliding-window extend-attention KV loop: -86.6% on SWA layers, -9.4% prefill GPU, bit-identical (#34462)
  _Files: `python/sglang/kernels/ops/attention/extend_attention.py`_
- **2026-08-24** [`666b08b4a5`](https://github.com/sgl-project/sglang/commit/666b08b4a5) [#34461](https://github.com/sgl-project/sglang/pull/34461)
  [ROCm] Extend the gfx950 extend-attention tile to head_dim <= 128: -43% kernel, -14% TTFT, bit-identical (#34461)
  _Files: `python/sglang/kernels/ops/attention/extend_attention.py`, `test/registered/attention/test_triton_attention_kernels.py`_
- **2026-08-24** [`c439e77872`](https://github.com/sgl-project/sglang/commit/c439e77872) [#34715](https://github.com/sgl-project/sglang/pull/34715)
  [bugfix] [NPU] fix transpose batch matmul K*B exceed 65536. (#34715)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/models/kimi_k3.py`, `python/sglang/srt/server_args.py`_
- **2026-08-24** [`852b04b358`](https://github.com/sgl-project/sglang/commit/852b04b358) [#36149](https://github.com/sgl-project/sglang/pull/36149)
  fix(xpu): read enable_deterministic_inference from the config bag (#36149)
  _Files: `python/sglang/srt/layers/attention/xpu_backend.py`_
- **2026-08-24** [`3e30649064`](https://github.com/sgl-project/sglang/commit/3e30649064) [#35454](https://github.com/sgl-project/sglang/pull/35454)
  [Fix] Harden FlashAttention CUDA graph metadata bounds (#35454)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/unit/layers/attention/test_flashattention_graph_metadata.py`_
- **2026-08-24** [`5b5b29d4e2`](https://github.com/sgl-project/sglang/commit/5b5b29d4e2) [#33354](https://github.com/sgl-project/sglang/pull/33354)
  [XPU] Use a fused GDN kernel from sgl-kernel for Qwen3.5 (#33354)
  _Files: `python/sglang/srt/hardware_backend/xpu/attention/__init__.py`, `python/sglang/srt/hardware_backend/xpu/attention/xpu_gdn_backend.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py` _+5 more__
- **2026-08-24** [`4c02584773`](https://github.com/sgl-project/sglang/commit/4c02584773) [#29143](https://github.com/sgl-project/sglang/pull/29143)
  Add intel_xpu to DETERMINISTIC_ATTENTION_BACKEND_CHOICES (#29143)
  _Files: `python/sglang/srt/layers/attention/xpu_backend.py`, `python/sglang/srt/server_args.py`, `test/registered/attention/test_deterministic.py`_
- **2026-08-24** [`447048dba2`](https://github.com/sgl-project/sglang/commit/447048dba2) [#36008](https://github.com/sgl-project/sglang/pull/36008)
  [diffusion] Reject unsafe quality=high BCG replay (#36008)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_bcg_padding.py`_
- **2026-08-23** [`44db041700`](https://github.com/sgl-project/sglang/commit/44db041700) [#35405](https://github.com/sgl-project/sglang/pull/35405)
  [NVIDIA] Fix SM107 MXFP8 activation prep (#35405)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `test/registered/unit/layers/quantization/test_fp8_utils_mxfp4.py`, `test/registered/unit/layers/quantization/test_mxfp4_flashinfer_activation_prep.py`_
- **2026-08-22** [`eec794bce0`](https://github.com/sgl-project/sglang/commit/eec794bce0) [#30105](https://github.com/sgl-project/sglang/pull/30105)
  [AMD][Spec] Fix aiter GQA packing + split-KV routing in NEXTN spec attention (verify & draft_extend) (#30105)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `test/manual/test_aiter_unified_draft_extend_env.py`_
- **2026-08-22** [`b98d472158`](https://github.com/sgl-project/sglang/commit/b98d472158) [#34855](https://github.com/sgl-project/sglang/pull/34855)
  [NPU] [Diffusion] Fix critical Ascend NPU Diffusion regression/bugs & restore 2-NPU CI testcase (#34855)
  _Files: `.github/workflows/diffusion-ci-gt-gen-npu.yml`, `.github/workflows/pr-test-npu.yml`, `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml` _+16 more__
- **2026-08-22** [`6fd0384d42`](https://github.com/sgl-project/sglang/commit/6fd0384d42) [#35932](https://github.com/sgl-project/sglang/pull/35932)
  Make draft attention backends extensible (#35932)
  _Files: `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/draft_worker_common.py`_
- **2026-08-22** [`af39ad9349`](https://github.com/sgl-project/sglang/commit/af39ad9349) [#33829](https://github.com/sgl-project/sglang/pull/33829)
  [Model] Complete dots.note.omni support with native encoders, video preprocessing, and MTP decoding (#33829)
  _Files: `docs/cookbook/autoregressive/RedNote/Dots3-Note.mdx`, `docs/src/snippets/configs/rednote/dots3-note.jsx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/__init__.py` _+51 more__
- **2026-08-21** [`7fd5454335`](https://github.com/sgl-project/sglang/commit/7fd5454335) [#35175](https://github.com/sgl-project/sglang/pull/35175)
  [DSA] Route the ragged prefill top-k to the v2 kernel (#35175)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/kernels/ops/attention/dsv4/topk.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer_metadata.py` _+3 more__
- **2026-08-21** [`7d893255c3`](https://github.com/sgl-project/sglang/commit/7d893255c3) [#34337](https://github.com/sgl-project/sglang/pull/34337)
  [Spec][LoRA] Support multi-adapter LoRA with EAGLE/NEXTN/DFLASH/DSPARK speculative decoding (#34337)
  _Files: `python/sglang/srt/lora/backend/base_backend.py`, `python/sglang/srt/lora/backend/chunked_backend.py`, `python/sglang/srt/lora/backend/triton_backend.py`, `python/sglang/srt/lora/layers.py` _+19 more__
- **2026-08-21** [`05c584c44f`](https://github.com/sgl-project/sglang/commit/05c584c44f) [#35861](https://github.com/sgl-project/sglang/pull/35861)
  docs: add DSPARK speculative decoding option to Ling-3.0-flash cookbook (#35861)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash.mdx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash-benchmarks.jsx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash.jsx`_
- **2026-08-21** [`0447ade326`](https://github.com/sgl-project/sglang/commit/0447ade326) [#35796](https://github.com/sgl-project/sglang/pull/35796)
  [diffusion] fix: fall back to a component's default attention backend (#35796)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py` _+17 more__
- **2026-08-21** [`39d4d65a51`](https://github.com/sgl-project/sglang/commit/39d4d65a51) [#35728](https://github.com/sgl-project/sglang/pull/35728)
  [diffusion] Accelerate SANA-Video linear attention in quality=high (#35728)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/sites/sana_video_linear_attention_site.py` _+5 more__
- **2026-08-21** [`3efa057449`](https://github.com/sgl-project/sglang/commit/3efa057449) [#35786](https://github.com/sgl-project/sglang/pull/35786)
  [docs] Retune the Qwen3.8-27B RTX 5090 DFLASH2 cells against 1cf2b8c (#35786)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b.jsx`_
- **2026-08-21** [`34180a0d35`](https://github.com/sgl-project/sglang/commit/34180a0d35) [#35499](https://github.com/sgl-project/sglang/pull/35499)
  [AMD] Improve K3 dspark draft attn kernel perf (#35499)
  _Files: `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/triton_backend.py`_
- **2026-08-20** [`14795dcb1a`](https://github.com/sgl-project/sglang/commit/14795dcb1a) [#35767](https://github.com/sgl-project/sglang/pull/35767)
  [docs] Point the Qwen3.8-27B DFLASH2 note back at the rolling dev image tag (#35767)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`_
- **2026-08-20** [`67f6ad61d9`](https://github.com/sgl-project/sglang/commit/67f6ad61d9) [#35197](https://github.com/sgl-project/sglang/pull/35197)
  fix(kernel) Fix Helion small-token prefill bug (#35197)
  _Files: `python/sglang/kernels/ops/attention/helion/kda_decode.py`, `python/sglang/kernels/ops/attention/helion/kda_prefill.py`, `test/registered/kernels/ops/attention/test_kda_helion.py`_
- **2026-08-20** [`1a138e13b9`](https://github.com/sgl-project/sglang/commit/1a138e13b9) [#35753](https://github.com/sgl-project/sglang/pull/35753)
  [docs] Tell Qwen3.8-27B DFLASH2 users to build from main (#35753)
  _Files: `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/scripts/check_cookbook_configs.mjs` _+2 more__
- **2026-08-20** [`d9f6861359`](https://github.com/sgl-project/sglang/commit/d9f6861359) [#35663](https://github.com/sgl-project/sglang/pull/35663)
  [docs] Add DFlash2 speculative cells to the Qwen3.8-27B cookbook (#35663)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b.jsx`_
- **2026-08-20** [`eac91ac362`](https://github.com/sgl-project/sglang/commit/eac91ac362) [#35412](https://github.com/sgl-project/sglang/pull/35412)
  [Fix] Land the decode mamba checkpoint depth on the tree page under DCP (#35412)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/speculative/dflash_worker_v2.py` _+5 more__
- **2026-08-20** [`ba97cc6397`](https://github.com/sgl-project/sglang/commit/ba97cc6397) [#35689](https://github.com/sgl-project/sglang/pull/35689)
  Skip empty linear-attention state buffers in PD transfer (#35689)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/mem_cache/test_mamba_state_transfer_buffers.py`_
- **2026-08-20** [`b03ac355e7`](https://github.com/sgl-project/sglang/commit/b03ac355e7) [#34936](https://github.com/sgl-project/sglang/pull/34936)
  [NPU] [FIX] Fix non-contiguous parameter issue in FIA operator (#34936)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-08-20** [`c98f1ccedb`](https://github.com/sgl-project/sglang/commit/c98f1ccedb) [#34935](https://github.com/sgl-project/sglang/pull/34935)
  [NPU]Ensure tensors allocated by empty_like are contiguous (#34935)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-08-20** [`a4ffb996db`](https://github.com/sgl-project/sglang/commit/a4ffb996db) [#35632](https://github.com/sgl-project/sglang/pull/35632)
  [Fix] Keep deterministic GDN prefill on Triton (#35632)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `test/registered/unit/layers/attention/test_gdn_prefill_backend_policy.py`_
- **2026-08-20** [`ae23423b46`](https://github.com/sgl-project/sglang/commit/ae23423b46) [#34888](https://github.com/sgl-project/sglang/pull/34888)
  Split TRTLLM MHA decode batches by KV sequence length (#34888)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `test/registered/attention/unittests/dense/test_trtllm_mha.py`_
- **2026-08-20** [`9db4ba8da1`](https://github.com/sgl-project/sglang/commit/9db4ba8da1) [#32327](https://github.com/sgl-project/sglang/pull/32327)
  [DeepSeek-V4] Add Q8KV8 sparse MLA prefill runtime backend (#32327)
  _Files: `python/sglang/kernels/ops/attention/dsv4/dequant_k_cache.py`, `python/sglang/kernels/ops/attention/sparse_mla_q8kv8_prefill_sm90.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py` _+3 more__
- **2026-08-20** [`1cf2b8c54d`](https://github.com/sgl-project/sglang/commit/1cf2b8c54d) [#35496](https://github.com/sgl-project/sglang/pull/35496)
  [Spec] Support quantized target lm_head in the DFlash2 selector (#35496)
  _Files: `python/sglang/srt/models/dflash.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `test/registered/unit/spec/test_dflash_logits.py`_
- **2026-08-19** [`a6bc0532c9`](https://github.com/sgl-project/sglang/commit/a6bc0532c9) [#34561](https://github.com/sgl-project/sglang/pull/34561)
  [Fix] Fix Nemotron-H Mamba illegal memory access under DP attention with CUDA graph (#34561)
  _Files: `python/sglang/srt/models/nemotron_h.py`, `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`_
- **2026-08-19** [`746418a1ec`](https://github.com/sgl-project/sglang/commit/746418a1ec) [#35041](https://github.com/sgl-project/sglang/pull/35041)
  [DSA] Trim top-k v2 output modes and tighten its PDL waits (#35041)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/kernels/ops/attention/dsv4/topk.py`, `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py` _+1 more__
- **2026-08-19** [`1c82955861`](https://github.com/sgl-project/sglang/commit/1c82955861) [#35540](https://github.com/sgl-project/sglang/pull/35540)
  [HiCache] Split the host-memory budget across co-located ranks (#35540)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/pool_host/base.py`, `python/sglang/srt/mem_cache/pool_host/mamba.py`, `python/sglang/srt/mem_cache/pool_host/mha.py` _+2 more__
- **2026-08-19** [`f22442d3a4`](https://github.com/sgl-project/sglang/commit/f22442d3a4) [#35502](https://github.com/sgl-project/sglang/pull/35502)
  Add three new test cases (#35502)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w4a8_16p_gpqa.py`, `test/registered/npu/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_1p1d_16p_in8k_out1k_50ms.py` _+2 more__
- **2026-08-19** [`f4158719d1`](https://github.com/sgl-project/sglang/commit/f4158719d1) [#34485](https://github.com/sgl-project/sglang/pull/34485)
  [AMD] Let the diffusion AITer backend take grouped-query K/V (fix Cosmos3-Nano startup) (#34485)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py`, `python/sglang/multimodal_gen/test/unit/test_aiter_attention_impl.py`_
- **2026-08-19** [`c0c87e0547`](https://github.com/sgl-project/sglang/commit/c0c87e0547) [#35336](https://github.com/sgl-project/sglang/pull/35336)
  VLM: feed the packed qkv projection output to vision backends uncopied (#35336)
  _Files: `python/sglang/srt/layers/attention/vision.py`, `test/registered/unit/layers/attention/test_vision_strided_qkv.py`_
- **2026-08-19** [`593b1a9b8a`](https://github.com/sgl-project/sglang/commit/593b1a9b8a) [#33880](https://github.com/sgl-project/sglang/pull/33880)
  [diffusion] optimization: reduce minimax h3 mps memory pressure (#33880)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py`, `python/sglang/multimodal_gen/runtime/layers/linear.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py` _+22 more__
- **2026-08-19** [`ee1f2e8dfd`](https://github.com/sgl-project/sglang/commit/ee1f2e8dfd) [#34680](https://github.com/sgl-project/sglang/pull/34680)
  [diffusion][Minimax H3]support subblock sparse attention on SM90 (#34680)
  _Files: `python/sglang/kernels/ops/attention/flash_attn/cute/block_sparse_utils.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/README.md`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/__init__.py` _+5 more__
- **2026-08-19** [`eb085524c8`](https://github.com/sgl-project/sglang/commit/eb085524c8) [#34993](https://github.com/sgl-project/sglang/pull/34993)
  [diffusion] fix: make MiniMax-H3 AdaLN cache rebuild transactional (#34993)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_adaln_cache.py`_
- **2026-08-19** [`58c5bee3ac`](https://github.com/sgl-project/sglang/commit/58c5bee3ac) [#12961](https://github.com/sgl-project/sglang/pull/12961)
  Fix DP attention on CPU (#12961)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/model_executor/forward_batch_info.py` _+2 more__
- **2026-08-19** [`5d12280ae7`](https://github.com/sgl-project/sglang/commit/5d12280ae7) [#23112](https://github.com/sgl-project/sglang/pull/23112)
  Add fmha_v2 attention backend for SM90/120 (#23112)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/server_args.py`_
- **2026-08-19** [`e73201e462`](https://github.com/sgl-project/sglang/commit/e73201e462) [#35339](https://github.com/sgl-project/sglang/pull/35339)
  [diffusion] feat: support cache-dit, cfg gating, attention backend override as per-request param (#35339)
  _Files: `docs/docs/sglang-diffusion/attention_backends.mdx`, `docs/docs/sglang-diffusion/cache_dit.mdx`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-performance/SKILL.md`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py` _+13 more__
- **2026-08-19** [`64e404263e`](https://github.com/sgl-project/sglang/commit/64e404263e) [#34862](https://github.com/sgl-project/sglang/pull/34862)
  [Doc] Fix TP and attention-TP group layout in initialize_model_parallel docstring (#34862)
  _Files: `python/sglang/srt/distributed/parallel_state.py`_
- **2026-08-19** [`c14312a664`](https://github.com/sgl-project/sglang/commit/c14312a664) [#35371](https://github.com/sgl-project/sglang/pull/35371)
  [Spec] DFlash2: local convolution + candidate selector (#35371)
  _Files: `python/sglang/kernels/ops/speculative/dflash.py`, `python/sglang/srt/model_executor/model_runner_components/spec_aux_hidden_state.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/srt/speculative/dflash_utils.py` _+3 more__
- **2026-08-18** [`87a09494fa`](https://github.com/sgl-project/sglang/commit/87a09494fa) [#35382](https://github.com/sgl-project/sglang/pull/35382)
  [Refactor] Share the page-aligned decode alloc lens between EAGLE and DFLASH (#35382)
  _Files: `python/sglang/srt/mem_cache/allocation_sizing.py`, `python/sglang/srt/speculative/dflash_info_v2.py`, `python/sglang/srt/speculative/eagle_utils.py`_
- **2026-08-18** [`79dfef390b`](https://github.com/sgl-project/sglang/commit/79dfef390b) [#35265](https://github.com/sgl-project/sglang/pull/35265)
  [Spec] Page-align the DFLASH decode KV reservation (#35265)
  _Files: `python/sglang/srt/speculative/dflash_info_v2.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py` _+1 more__
- **2026-08-18** [`955704544c`](https://github.com/sgl-project/sglang/commit/955704544c) [#33431](https://github.com/sgl-project/sglang/pull/33431)
  [Fix] Skip padded state slots in the chunked GDN kernel (#33431)
  _Files: `test/registered/attention/test_chunk_gated_delta_rule.py`_
- **2026-08-18** [`63d783bbe0`](https://github.com/sgl-project/sglang/commit/63d783bbe0) [#34581](https://github.com/sgl-project/sglang/pull/34581)
  [diffusion] optimization: INT8 Linear + pluggable DiT attention backends for MiniMax-H3 on consumer-level GPUs (#34581)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `docs/docs/sglang-diffusion/environment_variables.mdx`, `docs/docs/sglang-diffusion/quantization.mdx` _+6 more__
- **2026-08-18** [`7605529bdf`](https://github.com/sgl-project/sglang/commit/7605529bdf) [#35162](https://github.com/sgl-project/sglang/pull/35162)
  Add deepseek_v4_flash_w8a8_8p_in32k_out1k_50ms (#35162)
  _Files: `test/registered/npu/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in32k_out1k_50ms.py`_
- **2026-08-18** [`0111b29031`](https://github.com/sgl-project/sglang/commit/0111b29031) [#34890](https://github.com/sgl-project/sglang/pull/34890)
  [Perf] Hoist DSv4 draft-extend SWA write locs; unify SWA graph buffer naming (#34890)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/xpu_backend.py`_
- **2026-08-18** [`d01812d89e`](https://github.com/sgl-project/sglang/commit/d01812d89e) [#34580](https://github.com/sgl-project/sglang/pull/34580)
  [AMD] Optimize KIMI-K3 with Triton MLA decode kernel by tuning the stage-1 geometry for gfx950 (#34580)
  _Files: `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/srt/environ.py`, `test/registered/unit/layers/attention/test_mla_decode_forced_splits.py`, `test/registered/unit/layers/attention/test_mla_decode_geometry.py`_
- **2026-08-18** [`f44a130c5e`](https://github.com/sgl-project/sglang/commit/f44a130c5e) [#35084](https://github.com/sgl-project/sglang/pull/35084)
  [DCP] Drop the prefill index-selection syncs by taking each rank's rows by stride (#35084)
  _Files: `python/sglang/srt/layers/dcp/layout.py`, `python/sglang/srt/layers/dcp/planner.py`, `python/sglang/srt/model_executor/forward_batch_deepseek_mha_mixin.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py` _+1 more__
- **2026-08-18** [`d6c837489a`](https://github.com/sgl-project/sglang/commit/d6c837489a) [#30144](https://github.com/sgl-project/sglang/pull/30144)
  [XPU] Enable fused GDN QKV split Triton kernel on XPU (#30144)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`_
- **2026-08-17** [`92bce3d7bb`](https://github.com/sgl-project/sglang/commit/92bce3d7bb) [#30519](https://github.com/sgl-project/sglang/pull/30519)
  [AMD] [GLM5] fp8 MLA absorbed bmm for GLM-5.2 on gfx950 (#30519)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`_
- **2026-08-17** [`4cad864361`](https://github.com/sgl-project/sglang/commit/4cad864361) [#35042](https://github.com/sgl-project/sglang/pull/35042)
  Fix sconv track refresh on graph capture (#35042)
  _Files: `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`_
- **2026-08-17** [`5769b6d637`](https://github.com/sgl-project/sglang/commit/5769b6d637) [#35031](https://github.com/sgl-project/sglang/pull/35031)
  [JIT Kernel] Migrate causal_conv1d_fwd and causal_conv1d_update from AOT to JIT (#35031)
  _Files: `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/tests/test_causal_conv1d.py`, `python/sglang/kernels/jit/csrc/mamba/causal_conv1d.cuh`, `python/sglang/kernels/ops/mamba/__init__.py` _+4 more__
- **2026-08-17** [`721e359ca7`](https://github.com/sgl-project/sglang/commit/721e359ca7) [#34921](https://github.com/sgl-project/sglang/pull/34921)
  Suppress expected FlashInfer TRT-LLM workspace warnings (#34921)
  _Files: `python/sglang/srt/layers/flashinfer_comm_fusion.py`, `test/registered/unit/layers/test_flashinfer_comm_fusion.py`_
- **2026-08-17** [`eb61cb2823`](https://github.com/sgl-project/sglang/commit/eb61cb2823) [#33480](https://github.com/sgl-project/sglang/pull/33480)
  [AMD] Support prefill context parallel two batch overlap for DeepSeek V4 (#33480)
  _Files: `python/sglang/srt/batch_overlap/operations_strategy.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/parallel_state.py` _+6 more__
- **2026-08-17** [`f3225bceb3`](https://github.com/sgl-project/sglang/commit/f3225bceb3) [#34277](https://github.com/sgl-project/sglang/pull/34277)
  [DSV4] Emit TMA-aligned UE8M0 scales for FP8 einsum (#34277)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/fp8_wo_a_group_major_quant.cuh`, `python/sglang/kernels/ops/attention/dsv4/fp8_wo_a.py`, `test/registered/kernels/ops/attention/test_fp8_wo_a.py`_
- **2026-08-17** [`0fb040cbeb`](https://github.com/sgl-project/sglang/commit/0fb040cbeb) [#34889](https://github.com/sgl-project/sglang/pull/34889)
  [DCP]Localize HiCache DCP indices once per transfer, not per layer (#34889)
  _Files: `python/sglang/srt/mem_cache/pool_host/base.py`, `python/sglang/srt/mem_cache/pool_host/mla.py`, `test/registered/unit/mem_cache/test_hicache_dcp_host_pool.py`_
- **2026-08-17** [`0e178c3d22`](https://github.com/sgl-project/sglang/commit/0e178c3d22) [#34988](https://github.com/sgl-project/sglang/pull/34988)
  [diffusion] chore: reuse srt siglip vision model (#34988)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/runtime/models/encoders/gemma_3.py`, `python/sglang/multimodal_gen/test/single_test_file/component_accuracy/engine.py`, `python/sglang/multimodal_gen/test/unit/test_component_accuracy_parallel_runtime.py` _+5 more__

## Quantization  (44 commits)

- **2026-08-24** [`adc09a1f63`](https://github.com/sgl-project/sglang/commit/adc09a1f63) [#36052](https://github.com/sgl-project/sglang/pull/36052)
  [diffusion] feat: support loading self-describing quanto int8 encoders (#36052)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/base_config.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/quanto_int8_config.py` _+9 more__
- **2026-08-24** [`5081ad5d4e`](https://github.com/sgl-project/sglang/commit/5081ad5d4e) [#36084](https://github.com/sgl-project/sglang/pull/36084)
  [diffusion] feat: add per-component quantization overrides (#36084)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/image_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py` _+6 more__
- **2026-08-24** [`7bbd0ddeb5`](https://github.com/sgl-project/sglang/commit/7bbd0ddeb5) [#36124](https://github.com/sgl-project/sglang/pull/36124)
  [AMD] Quark shared-experts gate: recognise a trailing MTP layer (#36124)
  _Files: `python/sglang/srt/layers/quantization/quark/quark.py`_
- **2026-08-24** [`3fe18f13cd`](https://github.com/sgl-project/sglang/commit/3fe18f13cd) [#36086](https://github.com/sgl-project/sglang/pull/36086)
  [diffusion] feat: add plain component weight overrides (#36086)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/adapter_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/diffusion_decoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/sound_tokenizer_loader.py` _+3 more__
- **2026-08-24** [`8df3b9eff9`](https://github.com/sgl-project/sglang/commit/8df3b9eff9) [#36037](https://github.com/sgl-project/sglang/pull/36037)
  [diffusion] feat: support loading mixed w4a8 text encoders (#36037)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/base_config.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/kitchen_w4a8_config.py` _+5 more__
- **2026-08-24** [`f98b60de80`](https://github.com/sgl-project/sglang/commit/f98b60de80) [#33057](https://github.com/sgl-project/sglang/pull/33057)
  fix(xpu): enable compressed-tensors FP8 W8A8 on XPU (RedHatAI FP8-dynamic models) (#33057)
  _Files: `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` _+2 more__
- **2026-08-24** [`7a7b655ddf`](https://github.com/sgl-project/sglang/commit/7a7b655ddf) [#35180](https://github.com/sgl-project/sglang/pull/35180)
  [quantization] share bounded post-load device staging (#35180)
  _Files: `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/model_loader/post_load.py`, `test/registered/unit/test_quantization_post_load.py`_
- **2026-08-24** [`230c052ebc`](https://github.com/sgl-project/sglang/commit/230c052ebc) [#36068](https://github.com/sgl-project/sglang/pull/36068)
  [diffusion] chore: reuse srt AutoRound for quantized DiTs (#36068)
  _Files: `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/__init__.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/auto_round.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/base_config.py` _+4 more__
- **2026-08-24** [`fbdec2855a`](https://github.com/sgl-project/sglang/commit/fbdec2855a) [#30236](https://github.com/sgl-project/sglang/pull/30236)
  [XPU] Support INT4 dense linear (AWQ/GPTQ) for XPU (#30236)
  _Files: `python/sglang/srt/hardware_backend/xpu/quantization/__init__.py`, `python/sglang/srt/hardware_backend/xpu/quantization/awq_kernels.py`, `python/sglang/srt/hardware_backend/xpu/quantization/gptq_kernels.py`, `python/sglang/srt/hardware_backend/xpu/quantization/int4pack_utils.py` _+10 more__
- **2026-08-24** [`2d84de5e69`](https://github.com/sgl-project/sglang/commit/2d84de5e69) [#36036](https://github.com/sgl-project/sglang/pull/36036)
  [diffusion] feat: support loading serialized comfy w4a8 checkpoints (#36036)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/kitchen_w4a8_config.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/kitchen_w4a8.py` _+4 more__
- **2026-08-24** [`1c1c9d9b4e`](https://github.com/sgl-project/sglang/commit/1c1c9d9b4e) [#36063](https://github.com/sgl-project/sglang/pull/36063)
  [diffusion] refactor: reuse srt quantization contracts and mxfp8 kernels (#36063)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/__init__.py` _+12 more__
- **2026-08-24** [`20064623ab`](https://github.com/sgl-project/sglang/commit/20064623ab) [#35383](https://github.com/sgl-project/sglang/pull/35383)
  [AMD][CI] Add the Qwen3.8 MXFP4 MI35x nightly (#35383)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `scripts/ci/amd/check_hf_cache_space.sh`, `test/registered/amd/accuracy/mi35x/test_qwen38_mxfp4_eval_mi35x.py`, `test/run_suite.py`_
- **2026-08-23** [`dd15fb57b5`](https://github.com/sgl-project/sglang/commit/dd15fb57b5) [#36060](https://github.com/sgl-project/sglang/pull/36060)
  [diffusion] feat: automatically infer comfy fp8 activation scaling (#36060)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/comfy_fp8.py`, `python/sglang/multimodal_gen/runtime/utils/quantization_utils.py` _+1 more__
- **2026-08-23** [`70319a0881`](https://github.com/sgl-project/sglang/commit/70319a0881) [#36023](https://github.com/sgl-project/sglang/pull/36023)
  [diffusion] feat: support loading serialized comfy convrot int8 native encoders (#36023)
  _Files: `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/comfy_fp8.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/base_config.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/kitchen_int8_config.py` _+7 more__
- **2026-08-23** [`a36c0746b9`](https://github.com/sgl-project/sglang/commit/a36c0746b9) [#35994](https://github.com/sgl-project/sglang/pull/35994)
  [diffusion] feat: support serialized comfy convrot int8 dits (#35994)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/comfy_fp8.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/base_config.py` _+7 more__
- **2026-08-22** [`453b98c490`](https://github.com/sgl-project/sglang/commit/453b98c490) [#35979](https://github.com/sgl-project/sglang/pull/35979)
  [diffusion] feat: support single-file component weight overrides (#35979)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/image_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py` _+9 more__
- **2026-08-22** [`489e605b35`](https://github.com/sgl-project/sglang/commit/489e605b35) [#35962](https://github.com/sgl-project/sglang/pull/35962)
  [diffusion] feat: admit compatible quantized native encoders (#35962)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/models/encoders/base.py` _+4 more__
- **2026-08-22** [`b391ef171f`](https://github.com/sgl-project/sglang/commit/b391ef171f) [#35945](https://github.com/sgl-project/sglang/pull/35945)
  [diffusion] feat: load serialized bnb4 components with transformers (#35945)
  _Files: `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/test/unit/test_image_encoder_loader.py` _+1 more__
- **2026-08-22** [`b26695a26e`](https://github.com/sgl-project/sglang/commit/b26695a26e) [#35873](https://github.com/sgl-project/sglang/pull/35873)
  [diffusion] feat: reject unsupported quantized component checkpoints (#35873)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs/docs/sglang-diffusion/index.mdx`, `docs/docs/sglang-diffusion/quantization.mdx` _+8 more__
- **2026-08-21** [`5ecd6d794d`](https://github.com/sgl-project/sglang/commit/5ecd6d794d) [#35740](https://github.com/sgl-project/sglang/pull/35740)
  [diffusion] fix: fix quantized qkv scales and missing-param policy for minimax-h3 (#35740)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_qkv_scale_reorder.py`_
- **2026-08-20** [`308bc1228b`](https://github.com/sgl-project/sglang/commit/308bc1228b) [#34829](https://github.com/sgl-project/sglang/pull/34829)
  📝 [NPU] Clean up quantization comments (#34829)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`, `python/sglang/srt/layers/quantization/modelslim/schemes/modelslim_mxfp4_w4a8.py`_
- **2026-08-20** [`82c6fc2db9`](https://github.com/sgl-project/sglang/commit/82c6fc2db9) [#35418](https://github.com/sgl-project/sglang/pull/35418)
  [diffusion] quant: support pruned safetensors checkpoints for minimax-h3 (#35418)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/comfy_fp8.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py` _+5 more__
- **2026-08-20** [`710267dc4c`](https://github.com/sgl-project/sglang/commit/710267dc4c) [#35455](https://github.com/sgl-project/sglang/pull/35455)
  [Quant] Load compressed-tensors kv_cache_scheme scales (#35455)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `test/registered/unit/layers/quantization/test_compressed_tensors_kv_cache.py`_
- **2026-08-20** [`21c88f8625`](https://github.com/sgl-project/sglang/commit/21c88f8625) [#35370](https://github.com/sgl-project/sglang/pull/35370)
  [diffusion] quant: support gguf (#35370)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs/docs/sglang-diffusion/quantization.mdx` _+19 more__
- **2026-08-20** [`02b93e7e01`](https://github.com/sgl-project/sglang/commit/02b93e7e01) [#32570](https://github.com/sgl-project/sglang/pull/32570)
  [AMD] Add GLM-5.2 MI35x nightly accuracy and perf benchmark (#32570)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `test/registered/amd/accuracy/mi35x/test_glm52_fp8_eval_mi35x.py`, `test/registered/amd/perf/mi35x/test_glm52_fp8_perf_mi35x.py`, `test/run_suite.py`_
- **2026-08-20** [`ab203663c4`](https://github.com/sgl-project/sglang/commit/ab203663c4) [#35182](https://github.com/sgl-project/sglang/pull/35182)
  [diffusion] fix: reject unsupported modelopt checkpoint algorithms (#35182)
  _Files: `python/sglang/multimodal_gen/runtime/utils/quantization_utils.py`, `python/sglang/multimodal_gen/test/unit/test_transformer_quant.py`, `python/sglang/srt/layers/modelopt_utils.py`, `python/sglang/srt/layers/quantization/base_config.py` _+1 more__
- **2026-08-19** [`5375babbac`](https://github.com/sgl-project/sglang/commit/5375babbac) [#35228](https://github.com/sgl-project/sglang/pull/35228)
  [Quant] Load compressed-tensors quantized lm_head instead of value-casting it (#35228)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `test/registered/unit/layers/quantization/test_compressed_tensors_lm_head.py`_
- **2026-08-19** [`b1707996e8`](https://github.com/sgl-project/sglang/commit/b1707996e8) [#32440](https://github.com/sgl-project/sglang/pull/32440)
  fix(gemma4): quantize MTP bridge projections (#32440)
  _Files: `python/sglang/srt/models/gemma4_mtp.py`_
- **2026-08-19** [`03cf2de2e3`](https://github.com/sgl-project/sglang/commit/03cf2de2e3) [#35545](https://github.com/sgl-project/sglang/pull/35545)
  [Qwen3.5][MTP] Preserve online NVFP4 draft quantization for mixed checkpoints (#35545)
  _Files: `python/sglang/srt/configs/model_config.py`_
- **2026-08-19** [`157d8ad27a`](https://github.com/sgl-project/sglang/commit/157d8ad27a) [#34908](https://github.com/sgl-project/sglang/pull/34908)
  Support Intern-S2-Mobius FP8 (#34908)
  _Files: `docs/cookbook/autoregressive/InternLM/Intern-S2-Mobius.mdx`, `docs/src/snippets/configs/internlm/intern-s2-mobius.jsx`, `python/sglang/srt/models/interns2_mobius.py`_
- **2026-08-19** [`e3445ed2bd`](https://github.com/sgl-project/sglang/commit/e3445ed2bd) [#35184](https://github.com/sgl-project/sglang/pull/35184)
  [diffusion] fix: route quantized vae component repos safely (#35184)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/test/unit/test_vae_loader.py`_
- **2026-08-19** [`ce1830c59b`](https://github.com/sgl-project/sglang/commit/ce1830c59b) [#33165](https://github.com/sgl-project/sglang/pull/33165)
  [AMD] DeepSeek-V4 MI355X: eliminate bpreshuffle fp8-scale relayout copy in dense w8a8 linear (#33165)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/registered/unit/layers/test_fp8_bpreshuffle_dense_linear_mi35x.py`, `test/registered/unit/layers/test_fp8_bpreshuffle_scale.py`_
- **2026-08-19** [`73e5fa4724`](https://github.com/sgl-project/sglang/commit/73e5fa4724) [#35183](https://github.com/sgl-project/sglang/pull/35183)
  [diffusion] refactor: gate native encoder quantized checkpoints (#35183)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/image_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/models/encoders/base.py` _+3 more__
- **2026-08-19** [`a5c96362b6`](https://github.com/sgl-project/sglang/commit/a5c96362b6) [#35174](https://github.com/sgl-project/sglang/pull/35174)
  [diffusion] chore: reuse shared checkpoint quant metadata resolver (#35174)
  _Files: `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`, `python/sglang/multimodal_gen/runtime/utils/quantization_utils.py`, `python/sglang/multimodal_gen/test/unit/test_transformer_quant.py`_
- **2026-08-19** [`baa2251847`](https://github.com/sgl-project/sglang/commit/baa2251847) [#35353](https://github.com/sgl-project/sglang/pull/35353)
  [diffusion] chore: make --vae-tiling honest, fix the decode oom advice, gate nvfp4 on blackwell (#35353)
  _Files: `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/decoding.py`, `python/sglang/multimodal_gen/test/unit/test_ideogram4.py` _+2 more__
- **2026-08-19** [`ef490853bb`](https://github.com/sgl-project/sglang/commit/ef490853bb) [#35172](https://github.com/sgl-project/sglang/pull/35172)
  quant: extract shared checkpoint quant metadata resolver (#35172)
  _Files: `python/sglang/srt/model_loader/checkpoint_quantization.py`, `python/sglang/srt/model_loader/weight_utils.py`, `test/registered/unit/model_loader/test_modelopt_loader.py`, `test/registered/unit/test_checkpoint_quantization.py`_
- **2026-08-18** [`f7101b0ae6`](https://github.com/sgl-project/sglang/commit/f7101b0ae6) [#32099](https://github.com/sgl-project/sglang/pull/32099)
  [AMD] MiniMax-M3 : Fuse QKV+index proj for block-fp8 (#32099)
  _Files: `python/sglang/srt/models/minimax_m3.py`_
- **2026-08-18** [`880ab72f34`](https://github.com/sgl-project/sglang/commit/880ab72f34) [#34327](https://github.com/sgl-project/sglang/pull/34327)
  test: extend NVFP4 Marlin tests to SM120 (#34327)
  _Files: `test/registered/kernels/ops/quantization/test_gptq_marlin.py`, `test/registered/kernels/ops/quantization/test_nvfp4_marlin.py`_
- **2026-08-18** [`ea27e3ddab`](https://github.com/sgl-project/sglang/commit/ea27e3ddab) [#35200](https://github.com/sgl-project/sglang/pull/35200)
  [AMD] Fix Quark Shared Experts Fusion Gate after load-time-override Removal (#35200)
  _Files: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/deepseek_common/utils.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/deepseek_v4.py` _+2 more__
- **2026-08-18** [`d55f1c28e2`](https://github.com/sgl-project/sglang/commit/d55f1c28e2) [#34986](https://github.com/sgl-project/sglang/pull/34986)
  [diffusion] feat: load quantized H3 text encoder checkpoints (#34986)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py` _+6 more__
- **2026-08-18** [`91144797c5`](https://github.com/sgl-project/sglang/commit/91144797c5) [#35194](https://github.com/sgl-project/sglang/pull/35194)
  Update Qwen3.5 H200 FP8 for AgentX HiCache MTP (#35194)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`_
- **2026-08-17** [`861eca8e25`](https://github.com/sgl-project/sglang/commit/861eca8e25) [#35168](https://github.com/sgl-project/sglang/pull/35168)
  docs: add NVFP4 quantization option to Kimi-K3 deploy panel (#35168)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-08-17** [`c82e928fe5`](https://github.com/sgl-project/sglang/commit/c82e928fe5) [#35111](https://github.com/sgl-project/sglang/pull/35111)
  [AMD] diffusion: normalize ModelOpt-FP8 weights to e4m3fnuz on gfx942 (#35111)
  _Files: `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`_
- **2026-08-17** [`92b1d382c7`](https://github.com/sgl-project/sglang/commit/92b1d382c7) [#35020](https://github.com/sgl-project/sglang/pull/35020)
  [Fix] Correct dense FP8 Marlin bias ordering (#35020)
  _Files: `python/sglang/srt/layers/quantization/marlin_utils_fp8.py`, `test/registered/unit/layers/quantization/test_marlin_utils_fp8.py`_

## Prefill / Decode Disaggregation  (44 commits)

- **2026-08-24** [`a90d770c40`](https://github.com/sgl-project/sglang/commit/a90d770c40) [#33684](https://github.com/sgl-project/sglang/pull/33684)
  [Weight Cache] Support static DP/EP layouts (#33684)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/moe/token_dispatcher/mooncake.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/weight_cache/daemon.py` _+5 more__
- **2026-08-23** [`362c2ee849`](https://github.com/sgl-project/sglang/commit/362c2ee849) [#35908](https://github.com/sgl-project/sglang/pull/35908)
  config: borrowed-record reads follow the config bags (#35908)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` _+61 more__
- **2026-08-23** [`64aa859da2`](https://github.com/sgl-project/sglang/commit/64aa859da2) [#35907](https://github.com/sgl-project/sglang/pull/35907)
  config: constructing a config no longer resolves it (#35907)
  _Files: `examples/runtime/engine/save_remote_state.py`, `examples/runtime/engine/save_sharded_state.py`, `examples/runtime/token_in_token_out/token_in_token_out_vlm_engine.py`, `python/sglang/benchmark/endpoint.py` _+30 more__
- **2026-08-23** [`4bc79a1b49`](https://github.com/sgl-project/sglang/commit/4bc79a1b49) [#35906](https://github.com/sgl-project/sglang/pull/35906)
  config: project the config bags from the resolution result (#35906)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py` _+40 more__
- **2026-08-23** [`0e22777572`](https://github.com/sgl-project/sglang/commit/0e22777572) [#35905](https://github.com/sgl-project/sglang/pull/35905)
  config: record resolution writes in a declaration stash (#35905)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/kimi_k3_hook.py`, `python/sglang/srt/arg_groups/mega_moe_hook.py` _+8 more__
- **2026-08-23** [`6218d6ce3f`](https://github.com/sgl-project/sglang/commit/6218d6ce3f) [#35904](https://github.com/sgl-project/sglang/pull/35904)
  config: a defensive publish must not re-project over a live process (#35904)
  _Files: `python/sglang/srt/disaggregation/encoder/http_server.py`, `python/sglang/srt/disaggregation/encoder/server.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+6 more__
- **2026-08-23** [`8270ac4621`](https://github.com/sgl-project/sglang/commit/8270ac4621) [#36030](https://github.com/sgl-project/sglang/pull/36030)
  refactor(disagg): move _is_watermark_ready into StagingManagerMixin (#36030)
  _Files: `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-08-23** [`849ce71976`](https://github.com/sgl-project/sglang/commit/849ce71976) [#36031](https://github.com/sgl-project/sglang/pull/36031)
  refactor(disagg): dedupe mooncake failure_exception into a mixin (#36031)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`_
- **2026-08-23** [`bd72190728`](https://github.com/sgl-project/sglang/commit/bd72190728) [#36006](https://github.com/sgl-project/sglang/pull/36006)
  refactor(disagg): register SGLANG_ENCODER_MM_LOAD_WORKERS in Envs (#36006)
  _Files: `python/sglang/srt/disaggregation/encoder/preprocessor.py`, `python/sglang/srt/environ.py`_
- **2026-08-22** [`cce0a1244b`](https://github.com/sgl-project/sglang/commit/cce0a1244b) [#35980](https://github.com/sgl-project/sglang/pull/35980)
  refactor(disagg): hoist staging helper imports out of the bootstrap loops (#35980)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-08-22** [`3c69a4c744`](https://github.com/sgl-project/sglang/commit/3c69a4c744) [#35974](https://github.com/sgl-project/sglang/pull/35974)
  fix(test): unbreak test_kv_transfer_replica_metric after #35950 (#35974)
  _Files: `test/registered/unit/disaggregation/test_kv_transfer_replica_metric.py`_
- **2026-08-22** [`5c03069d4b`](https://github.com/sgl-project/sglang/commit/5c03069d4b) [#35950](https://github.com/sgl-project/sglang/pull/35950)
  refactor(disagg): drop dead placeholder overrides in Common KV sender/receiver (#35950)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`_
- **2026-08-22** [`15a4398320`](https://github.com/sgl-project/sglang/commit/15a4398320) [#35948](https://github.com/sgl-project/sglang/pull/35948)
  refactor(disagg): hoist duplicated _handle_staging_req into a mixin (#35948)
  _Files: `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-08-22** [`ac179eec11`](https://github.com/sgl-project/sglang/commit/ac179eec11) [#35890](https://github.com/sgl-project/sglang/pull/35890)
  fix(disagg): PD transfer-failure injection was silently inert (#35890)
  _Files: `python/sglang/srt/disaggregation/utils.py`, `test/registered/amd/disaggregation/test_disaggregation_basic.py`, `test/registered/disaggregation/test_disaggregation_basic.py`, `test/registered/disaggregation/test_disaggregation_nixl.py`_
- **2026-08-22** [`fbafd1b123`](https://github.com/sgl-project/sglang/commit/fbafd1b123) [#35747](https://github.com/sgl-project/sglang/pull/35747)
  Add sampling observer auxiliary output hooks (#35747)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py` _+13 more__
- **2026-08-21** [`7d7ab4b5c6`](https://github.com/sgl-project/sglang/commit/7d7ab4b5c6) [#35239](https://github.com/sgl-project/sglang/pull/35239)
  Rainj me/rust server refactor2 (#35239)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/_pr-test-stage-cpu.yml`, `.github/workflows/lint.yml`, `python/sglang/srt/environ.py` _+57 more__
- **2026-08-21** [`729a050ea3`](https://github.com/sgl-project/sglang/commit/729a050ea3) [#35886](https://github.com/sgl-project/sglang/pull/35886)
  refactor(disagg): extract _all_reduce_polls helper (#35886)
  _Files: `python/sglang/srt/disaggregation/utils.py`_
- **2026-08-21** [`a41da991c8`](https://github.com/sgl-project/sglang/commit/a41da991c8) [#35847](https://github.com/sgl-project/sglang/pull/35847)
  refactor(disagg): collapse duplicated branches in get_kv_class (#35847)
  _Files: `python/sglang/srt/disaggregation/utils.py`_
- **2026-08-21** [`4f343abc13`](https://github.com/sgl-project/sglang/commit/4f343abc13) [#35838](https://github.com/sgl-project/sglang/pull/35838)
  refactor(disagg): remove unreferenced dead code (#35838)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/staging_buffer.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`_
- **2026-08-21** [`dad6fd0f04`](https://github.com/sgl-project/sglang/commit/dad6fd0f04) [#35844](https://github.com/sgl-project/sglang/pull/35844)
  refactor(disagg): remove dead get_embedding_port (#35844)
  _Files: `python/sglang/srt/disaggregation/encoder/server.py`_
- **2026-08-21** [`e7a37c8550`](https://github.com/sgl-project/sglang/commit/e7a37c8550) [#35843](https://github.com/sgl-project/sglang/pull/35843)
  refactor(disagg): remove dead build_and_send_encode_request (#35843)
  _Files: `python/sglang/srt/disaggregation/encoder/receiver.py`_
- **2026-08-21** [`0db2c53dec`](https://github.com/sgl-project/sglang/commit/0db2c53dec) [#35748](https://github.com/sgl-project/sglang/pull/35748)
  Fix overlap prebuilt row reuse race (#35748)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/overlap_utils.py`, `test/registered/unit/managers/test_priority_scheduling_disaggregation.py`_
- **2026-08-21** [`8a123cbd0e`](https://github.com/sgl-project/sglang/commit/8a123cbd0e) [#30398](https://github.com/sgl-project/sglang/pull/30398)
  [Refactor] New EPD (#30398)
  _Files: `.github/CODEOWNERS`, `python/sglang/launch_server.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/disaggregation/encoder/__init__.py` _+21 more__
- **2026-08-21** [`73a2c117c6`](https://github.com/sgl-project/sglang/commit/73a2c117c6) [#35718](https://github.com/sgl-project/sglang/pull/35718)
  Support mxfp8 KV cache in PD transfer (#35718)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` _+4 more__
- **2026-08-21** [`978244d671`](https://github.com/sgl-project/sglang/commit/978244d671) [#27770](https://github.com/sgl-project/sglang/pull/27770)
  [P/D disagg] Decode-side radix cache for SWA hybrid models (unified radix tree) (#27770)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `scripts/ci/amd/amd_ci_install_dependency.sh` _+6 more__
- **2026-08-20** [`628674a5c7`](https://github.com/sgl-project/sglang/commit/628674a5c7) [#35649](https://github.com/sgl-project/sglang/pull/35649)
  Remove unused MOONCAKE_COMPILE_ARG argument from Dockerfile (#35649)
  _Files: `docker/Dockerfile`_
- **2026-08-20** [`32d98aad13`](https://github.com/sgl-project/sglang/commit/32d98aad13) [#35543](https://github.com/sgl-project/sglang/pull/35543)
  [HiCache] Allow a retraction host pool smaller than the device pool (#35543)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+3 more__
- **2026-08-19** [`ed12d6827d`](https://github.com/sgl-project/sglang/commit/ed12d6827d) [#35409](https://github.com/sgl-project/sglang/pull/35409)
  fix(disagg): allow fake transfer with decode DCP (#35409)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-08-19** [`6f69f927da`](https://github.com/sgl-project/sglang/commit/6f69f927da) [#35017](https://github.com/sgl-project/sglang/pull/35017)
  [Scheduler] Add configurable decode interval after prefill (#35017)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/managers/test_scheduler_chunked_req_gate.py`, `test/registered/unit/managers/test_scheduler_prefill_decode_interval.py` _+1 more__
- **2026-08-19** [`adca19c497`](https://github.com/sgl-project/sglang/commit/adca19c497) [#35360](https://github.com/sgl-project/sglang/pull/35360)
  [PD] Deferred decode-side KV release for the NIXL backend (#35360)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py` _+1 more__
- **2026-08-19** [`aa215e5523`](https://github.com/sgl-project/sglang/commit/aa215e5523) [#35071](https://github.com/sgl-project/sglang/pull/35071)
  [PD] Overlap prefill DP-rank bootstrap queries (#35071)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-08-19** [`ccbe380028`](https://github.com/sgl-project/sglang/commit/ccbe380028) [#35407](https://github.com/sgl-project/sglang/pull/35407)
  [CI] Trim the base-c 4-gpu-h100 stage from 5 shards to 4 (#35407)
  _Files: `python/sglang/test/kits/pd_parity_kit.py`, `test/registered/disaggregation/test_disaggregation_kimi_linear.py`, `test/registered/disaggregation/test_disaggregation_unified_memory.py`, `test/registered/ep/test_deepep_small.py` _+8 more__
- **2026-08-18** [`7ebaa98f81`](https://github.com/sgl-project/sglang/commit/7ebaa98f81) [#35396](https://github.com/sgl-project/sglang/pull/35396)
  [Fix] Assert the page-aligned SWA evict floor on both PD decode prealloc paths (#35396)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/mem_cache/test_hisparse_allocator.py`_
- **2026-08-18** [`aa82229173`](https://github.com/sgl-project/sglang/commit/aa82229173) [#35286](https://github.com/sgl-project/sglang/pull/35286)
  [Fix] Assert the page-aligned SWA evict floor at PD decode prealloc (#35286)
  _Files: `python/sglang/srt/disaggregation/decode.py`_
- **2026-08-18** [`97dedd1ce9`](https://github.com/sgl-project/sglang/commit/97dedd1ce9) [#35049](https://github.com/sgl-project/sglang/pull/35049)
  [PD] Deferred decode-side KV release for aborts mid-transfer (#35049)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/environ.py` _+4 more__
- **2026-08-18** [`53621818e4`](https://github.com/sgl-project/sglang/commit/53621818e4) [#35224](https://github.com/sgl-project/sglang/pull/35224)
  [Docs] Enable PD disaggregation for DSV4 low-latency recipes (#35224)
  _Files: `.github/workflows/lint.yml`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/scripts/check_cookbook_configs.mjs`, `docs/src/snippets/_playground.jsx` _+1 more__
- **2026-08-17** [`cba3c5d5ac`](https://github.com/sgl-project/sglang/commit/cba3c5d5ac) [#35026](https://github.com/sgl-project/sglang/pull/35026)
  config: the per-instance families read the bags (#35026)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/constrained/base_grammar_backend.py`, `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py` _+41 more__
- **2026-08-17** [`a97bc8db32`](https://github.com/sgl-project/sglang/commit/a97bc8db32) [#35025](https://github.com/sgl-project/sglang/pull/35025)
  config: the DP/EP topology reads come from the parallel bag (#35025)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/layers/dp_attention.py` _+29 more__
- **2026-08-17** [`d2bc697396`](https://github.com/sgl-project/sglang/commit/d2bc697396) [#35024](https://github.com/sgl-project/sglang/pull/35024)
  spec: size the speculative buffers from the bags, not the startup record (#35024)
  _Files: `python/sglang/srt/debug_utils/pr_fix_toggle.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/layers/attention/dsa/utils.py` _+24 more__
- **2026-08-17** [`3d7ec00179`](https://github.com/sgl-project/sglang/commit/3d7ec00179) [#35023](https://github.com/sgl-project/sglang/pull/35023)
  config: publish before a process reads configuration (#35023)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/detokenizer_manager.py` _+5 more__
- **2026-08-17** [`2e7c85da68`](https://github.com/sgl-project/sglang/commit/2e7c85da68) [#34801](https://github.com/sgl-project/sglang/pull/34801)
  [PD] Preserve decode KV across retraction in HiCache (#34801)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/common.py` _+11 more__
- **2026-08-17** [`af743371cc`](https://github.com/sgl-project/sglang/commit/af743371cc) [#35060](https://github.com/sgl-project/sglang/pull/35060)
  Clean up environ.py: remove dead env vars, unify deprecation handling, move examples to a unit test (#35060)
  _Files: `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/minimax_m2_5.mdx`, `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/disaggregation/common/staging_buffer.py` _+8 more__
- **2026-08-17** [`7c423cfd41`](https://github.com/sgl-project/sglang/commit/7c423cfd41) [#35070](https://github.com/sgl-project/sglang/pull/35070)
  [PD] Avoid unused PREBUILT prompt tensor transfer (#35070)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-08-17** [`b83d507cd7`](https://github.com/sgl-project/sglang/commit/b83d507cd7) [#33676](https://github.com/sgl-project/sglang/pull/33676)
  [NPU] Support DeepSeek-V4 DSpark and refactor DSV4 cache management (#33676)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/disaggregation/decode.py` _+33 more__

## MoE / Expert Parallel  (34 commits)

- **2026-08-24** [`77940dec80`](https://github.com/sgl-project/sglang/commit/77940dec80) [#34915](https://github.com/sgl-project/sglang/pull/34915)
  [MoE] Gather the cutlass MoE activation and its scales in one launch (#34915)
  _Files: `python/sglang/kernels/ops/moe/__init__.py`, `python/sglang/kernels/ops/moe/shuffle_rows_with_scales.py`, `python/sglang/srt/layers/moe/cutlass_moe.py`, `test/registered/kernels/benchmark/moe/bench_shuffle_rows_with_scales.py` _+1 more__
- **2026-08-24** [`b498efce52`](https://github.com/sgl-project/sglang/commit/b498efce52) [#36053](https://github.com/sgl-project/sglang/pull/36053)
  chore: move cuda_vmm_utils.py under srt/utils/ (#36053)
  _Files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `python/sglang/srt/layers/moe/dwdp/layout.py`, `python/sglang/srt/layers/moe/dwdp/page_pool.py` _+8 more__
- **2026-08-24** [`56834422a1`](https://github.com/sgl-project/sglang/commit/56834422a1) [#33323](https://github.com/sgl-project/sglang/pull/33323)
  [Intel XPU] Add xpu pass for biased_topk and hash_topk (#33323)
  _Files: `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/xpu/test_topk.py`_
- **2026-08-23** [`edd675cecf`](https://github.com/sgl-project/sglang/commit/edd675cecf) [#34490](https://github.com/sgl-project/sglang/pull/34490)
  [AMD] Add Radix-4 MoE top-k router kernel for Kimi-K3 routing (#34490)
  _Files: `python/sglang/kernels/jit/csrc/moe/route_radix4_hip.cuh`, `python/sglang/kernels/ops/moe/moe_route_radix4.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/topk.py` _+1 more__
- **2026-08-22** [`3b5909de0e`](https://github.com/sgl-project/sglang/commit/3b5909de0e) [#35918](https://github.com/sgl-project/sglang/pull/35918)
  [DeepSeek V4] Add W4A4 MegaMoE server flag (#35918)
  _Files: `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/scripts/check_cookbook_configs.mjs`, `docs/src/snippets/_playground.jsx` _+11 more__
- **2026-08-21** [`60ff1e33a5`](https://github.com/sgl-project/sglang/commit/60ff1e33a5) [#35919](https://github.com/sgl-project/sglang/pull/35919)
  [DeepSeek V4] Default FP4 checkpoints to FlashInfer MXFP4 MoE (#35919)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/server_args.py`, `test/registered/models_e2e/test_deepseek_v4_flash_fp4_b200.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-08-21** [`834400705f`](https://github.com/sgl-project/sglang/commit/834400705f) [#34938](https://github.com/sgl-project/sglang/pull/34938)
  perf: overlap Qwen shared expert with DeepEP routed experts (#34938)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/qwen2_moe.py`_
- **2026-08-21** [`70983bd7db`](https://github.com/sgl-project/sglang/commit/70983bd7db) [#35794](https://github.com/sgl-project/sglang/pull/35794)
  Add SGLang Granite SWA support via existing Granite models (#35794)
  _Files: `docs/docs/supported-models/generative_models.mdx`, `python/sglang/srt/configs/granitemoehybrid.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/granite.py` _+2 more__
- **2026-08-21** [`8658d00764`](https://github.com/sgl-project/sglang/commit/8658d00764) [#35868](https://github.com/sgl-project/sglang/pull/35868)
  [diffusion] feat: support loading peft lora (#35868)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/pipelines/cosmos3_pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines/ernie_image.py` _+23 more__
- **2026-08-21** [`bda9952377`](https://github.com/sgl-project/sglang/commit/bda9952377) [#33166](https://github.com/sgl-project/sglang/pull/33166)
  [AMD] DeepSeek-V4 MI355X: eliminate bpreshuffle fp8-scale copies at producer sites (MoE down, MLA o_proj bmm) (#33166)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`, `python/sglang/srt/models/deepseek_v2.py`, `test/registered/unit/layers/test_fp8_bpreshuffle_producer_mi35x.py` _+1 more__
- **2026-08-21** [`e0cf75d9bd`](https://github.com/sgl-project/sglang/commit/e0cf75d9bd) [#34247](https://github.com/sgl-project/sglang/pull/34247)
  [doc] standardize diffusion cookbook model pages (#34247)
  _Files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/diffusion-authoring.md`, `.claude/skills/cookbook-add-model/templates/diffusion-config.jsx.tmpl`, `.claude/skills/cookbook-add-model/templates/diffusion-page.mdx.tmpl` _+28 more__
- **2026-08-20** [`ad367d72b0`](https://github.com/sgl-project/sglang/commit/ad367d72b0) [#35554](https://github.com/sgl-project/sglang/pull/35554)
  [Kimi K3] Select FlashInfer MXFP4 for SM107 auto MoE (#35554)
  _Files: `python/sglang/srt/arg_groups/overrides.py`_
- **2026-08-20** [`50dae2d99d`](https://github.com/sgl-project/sglang/commit/50dae2d99d) [#32340](https://github.com/sgl-project/sglang/pull/32340)
  Amd/dsv4 shared experts fusion top6 (#32340)
  _Files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/kernels/ops/moe/moe_fused_gate.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/kernels/ops/moe/test_moe_fused_gate.py` _+2 more__
- **2026-08-20** [`b6dcd393d6`](https://github.com/sgl-project/sglang/commit/b6dcd393d6) [#35593](https://github.com/sgl-project/sglang/pull/35593)
  [Fix] Support 128-aligned hidden sizes in the W4AFP8 DeepEP low-latency requant kernel (#35593)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `test/registered/kernels/ops/moe/test_fp8_per_token_to_per_tensor_quant.py`_
- **2026-08-20** [`a5a9d66baf`](https://github.com/sgl-project/sglang/commit/a5a9d66baf) [#34546](https://github.com/sgl-project/sglang/pull/34546)
  [XPU] Fix/kimi linear xpu (#34546)
  _Files: `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/kimi_linear.py`_
- **2026-08-20** [`d216737e47`](https://github.com/sgl-project/sglang/commit/d216737e47) [#35372](https://github.com/sgl-project/sglang/pull/35372)
  [Kernel] Support wider rows in mega_moe_pre_dispatch (#35372)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`_
- **2026-08-19** [`1270204d2c`](https://github.com/sgl-project/sglang/commit/1270204d2c) [#35568](https://github.com/sgl-project/sglang/pull/35568)
  Revert "[Feature] Add DeepEPv2 (ElasticBuffer) MoE A2A backend" (#35568)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` _+14 more__
- **2026-08-19** [`4f8ecf6ae9`](https://github.com/sgl-project/sglang/commit/4f8ecf6ae9) [#29525](https://github.com/sgl-project/sglang/pull/29525)
  [Feature] Add DeepEPv2 (ElasticBuffer) MoE A2A backend (#29525)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` _+14 more__
- **2026-08-19** [`5f12839591`](https://github.com/sgl-project/sglang/commit/5f12839591) [#35077](https://github.com/sgl-project/sglang/pull/35077)
  [Fix] Support Kimi-K3 ModelOpt mixed NVFP4/FP8 checkpoint (#35077)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4_moe_scales.py` _+2 more__
- **2026-08-19** [`1ef7882a5b`](https://github.com/sgl-project/sglang/commit/1ef7882a5b) [#35294](https://github.com/sgl-project/sglang/pull/35294)
  [NIXL] Query EP top-k index dtype (#35294)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/nixl.py`_
- **2026-08-19** [`8a1e6e4e46`](https://github.com/sgl-project/sglang/commit/8a1e6e4e46) [#34859](https://github.com/sgl-project/sglang/pull/34859)
  Qwen3.8-27B Model Support (#34859)
  _Files: `python/sglang/kernels/jit/csrc/gemm/fp8_blockwise/fp8_blockwise_scaled_mm_sm120.cuh`, `python/sglang/kernels/jit/csrc/gemm/hopper_bf16_gemv.cuh`, `python/sglang/kernels/jit/csrc/gemm/sm120_fp8_gemv.cuh`, `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py` _+14 more__
- **2026-08-18** [`cfc6dfb364`](https://github.com/sgl-project/sglang/commit/cfc6dfb364) [#34923](https://github.com/sgl-project/sglang/pull/34923)
  Apply latest DeepEP branch (#34923)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `scripts/ci/cuda/ci_install_dependency.sh` _+1 more__
- **2026-08-18** [`7b5410c999`](https://github.com/sgl-project/sglang/commit/7b5410c999) [#35362](https://github.com/sgl-project/sglang/pull/35362)
  Laguna: config-driven MoE router scoring (#35362)
  _Files: `python/sglang/srt/configs/laguna.py`, `python/sglang/srt/models/laguna.py`_
- **2026-08-18** [`9485c083bb`](https://github.com/sgl-project/sglang/commit/9485c083bb) [#30319](https://github.com/sgl-project/sglang/pull/30319)
  [NPU] Add mxfp4-w4a4 MOE Quantization Support for NPU (#30319)
  _Files: `docs/docs/advanced_features/quantization.mdx`, `docs/docs/hardware-platforms/ascend-npus/optimization/quantization.mdx`, `python/sglang/srt/hardware_backend/npu/moe/quant.py`, `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py` _+3 more__
- **2026-08-18** [`24d625698d`](https://github.com/sgl-project/sglang/commit/24d625698d) [#31370](https://github.com/sgl-project/sglang/pull/31370)
  [AMD] feat(moe): fold padded-topk_ids fill into fused shared-experts append+remap (#31370)
  _Files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/moe/test_fused_append_remap_per_rank_shared_slots.py`_
- **2026-08-18** [`7f51e6bba0`](https://github.com/sgl-project/sglang/commit/7f51e6bba0) [#35119](https://github.com/sgl-project/sglang/pull/35119)
  [CPU] Explicitly import sgl_kernel in CPU kernel tests (#35119)
  _Files: `test/registered/cpu/test_activation.py`, `test/registered/cpu/test_bmm.py`, `test/registered/cpu/test_comm.py`, `test/registered/cpu/test_decode.py` _+12 more__
- **2026-08-17** [`bc312d185d`](https://github.com/sgl-project/sglang/commit/bc312d185d) [#34926](https://github.com/sgl-project/sglang/pull/34926)
  Clean deprecated DeepSeek V4 Environs (#34926)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` _+24 more__
- **2026-08-17** [`198a7b2fc9`](https://github.com/sgl-project/sglang/commit/198a7b2fc9) [#35062](https://github.com/sgl-project/sglang/pull/35062)
  [Misc] Clean up python/sglang package structure (#35062)
  _Files: `python/sglang/README.md`, `python/sglang/__init__.py`, `python/sglang/_platform_stubs.py`, `python/sglang/_triton_stub.py` _+50 more__
- **2026-08-17** [`82995a001b`](https://github.com/sgl-project/sglang/commit/82995a001b) [#35044](https://github.com/sgl-project/sglang/pull/35044)
  Stabilize GB300 nightly tests (#35044)
  _Files: `python/sglang/test/gb300_utils.py`, `test/registered/attention/test_glm4_moe_lite_deterministic.py`, `test/registered/gb300/test_deepseek_v4_pro_fp4.py`, `test/registered/gb300/test_deepseek_v4_pro_fp4_balanced.py` _+9 more__
- **2026-08-17** [`f7a404e9c3`](https://github.com/sgl-project/sglang/commit/f7a404e9c3) [#31575](https://github.com/sgl-project/sglang/pull/31575)
  Fix rope config compatibility and VL/transformers-fallback weight loading (#31575)
  _Files: `python/sglang/srt/managers/mm_schedule.py`, `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/models/olmo2.py`, `python/sglang/srt/models/qwen.py` _+3 more__
- **2026-08-17** [`0099107e8b`](https://github.com/sgl-project/sglang/commit/0099107e8b) [#35105](https://github.com/sgl-project/sglang/pull/35105)
  Revert "[AMD] [GLM5] Fuse shared-expert append into aiter grouped-topk (skip per-layer append kernel)" (#35105)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-08-17** [`b6d7602914`](https://github.com/sgl-project/sglang/commit/b6d7602914) [#22498](https://github.com/sgl-project/sglang/pull/22498)
  [CPU] Add support for Gemma4 on Xeon (#22498)
  _Files: `python/sglang/kernels/aot/csrc/cpu/aarch64/moe.cpp`, `python/sglang/kernels/aot/csrc/cpu/activation.cpp`, `python/sglang/kernels/aot/csrc/cpu/extend.cpp`, `python/sglang/kernels/aot/csrc/cpu/gemm.h` _+23 more__
- **2026-08-17** [`3adc70bb5e`](https://github.com/sgl-project/sglang/commit/3adc70bb5e) [#34795](https://github.com/sgl-project/sglang/pull/34795)
  [MoE] Add H20 fp8_w8a8 tuned configs for Qwen3.8 (triton 3.7.1) + fix Qwen3_5MoeForCausalLM tuning (#34795)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=512,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`_
- **2026-08-17** [`8e0499bd50`](https://github.com/sgl-project/sglang/commit/8e0499bd50) [#31323](https://github.com/sgl-project/sglang/pull/31323)
  [AMD] [GLM5] Fuse shared-expert append into aiter grouped-topk (skip per-layer append kernel) (#31323)
  _Files: `python/sglang/srt/layers/moe/topk.py`_

## KV Cache / Memory  (28 commits)

- **2026-08-22** [`c35683fda0`](https://github.com/sgl-project/sglang/commit/c35683fda0) [#35933](https://github.com/sgl-project/sglang/pull/35933)
  [HiCache] Clamp tombstoned SWA locs in UnifiedSWAKVPool translation (#35933)
  _Files: `python/sglang/srt/mem_cache/unified_memory_pool.py`_
- **2026-08-22** [`0db2bdfec5`](https://github.com/sgl-project/sglang/commit/0db2bdfec5) [#35769](https://github.com/sgl-project/sglang/pull/35769)
  Fix buffer-mode HiCache load-back ownership races; add optional prefetch anchor lock (#35769)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-08-22** [`5662c03363`](https://github.com/sgl-project/sglang/commit/5662c03363) [#35888](https://github.com/sgl-project/sglang/pull/35888)
  Support CPU offload for mxfp8 KV cache (#35888)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/swa_memory_pool.py`, `test/registered/unit/mem_cache/test_swa_cpu_copy_filter.py`_
- **2026-08-22** [`d90318b3e2`](https://github.com/sgl-project/sglang/commit/d90318b3e2) [#32984](https://github.com/sgl-project/sglang/pull/32984)
  [MLX] Upgrade to Torch 2.13/MLX 0.32+ and redesign the Torch-MLX tensor bridge (#32984)
  _Files: `docs/docs/hardware-platforms/apple_metal.mdx`, `docs/docs/references/environment_variables.mdx`, `docs/docs/sglang-diffusion/environment_variables.mdx`, `docs/docs/sglang-diffusion/fused_kernels.mdx` _+32 more__
- **2026-08-21** [`0bdd28d487`](https://github.com/sgl-project/sglang/commit/0bdd28d487) [#35643](https://github.com/sgl-project/sglang/pull/35643)
  [mem_cache] docs: add a layer map and placement rules (#35643)
  _Files: `python/sglang/srt/mem_cache/README.md`_
- **2026-08-21** [`a7ec6b97f7`](https://github.com/sgl-project/sglang/commit/a7ec6b97f7) [#25122](https://github.com/sgl-project/sglang/pull/25122)
  Restructure mem_cache auto-labels by layer (#25122)
  _Files: `.github/labeler.yml`_
- **2026-08-21** [`896acc8860`](https://github.com/sgl-project/sglang/commit/896acc8860) [#35773](https://github.com/sgl-project/sglang/pull/35773)
  [Fix] Clear full-to-SWA mapping with `index_fill_` to avoid a blocking H2D copy (#35773)
  _Files: `python/sglang/srt/mem_cache/allocator/swa.py`, `python/sglang/srt/mem_cache/multi_ended_allocator.py`, `python/sglang/srt/mem_cache/swa_radix_cache.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py` _+2 more__
- **2026-08-21** [`8ff9c2b227`](https://github.com/sgl-project/sglang/commit/8ff9c2b227) [#35306](https://github.com/sgl-project/sglang/pull/35306)
  [mem_cache][9/N] refactor: move DSAIndexerPoolHost to pool_host.dsa (#35306)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/pool_host/dsa.py`, `test/registered/unit/mem_cache/test_dsa_pool_host_unit.py` _+1 more__
- **2026-08-21** [`44806dc507`](https://github.com/sgl-project/sglang/commit/44806dc507) [#35081](https://github.com/sgl-project/sglang/pull/35081)
  Using unified radix tree by default for all case (#35081)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/registry.py`, `python/sglang/srt/mem_cache/unified_cache/components/README.md` _+6 more__
- **2026-08-20** [`2ef0fe4669`](https://github.com/sgl-project/sglang/commit/2ef0fe4669) [#34406](https://github.com/sgl-project/sglang/pull/34406)
  TP/PP Consensus checker (#34406)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+2 more__
- **2026-08-20** [`238ba40c27`](https://github.com/sgl-project/sglang/commit/238ba40c27) [#35337](https://github.com/sgl-project/sglang/pull/35337)
  [XPU][CI] key persistent JIT kernel cache by image content ID (#35337)
  _Files: `.github/workflows/pr-test-xpu.yml`, `python/sglang/srt/hardware_backend/xpu/kernels/fla/chunk_delta_h.py`, `scripts/ci/xpu/xpu_ci_start_container.sh`_
- **2026-08-19** [`01814e110d`](https://github.com/sgl-project/sglang/commit/01814e110d) [#35574](https://github.com/sgl-project/sglang/pull/35574)
  [HiCache] Simple style change for buffer mode (#35574)
  _Files: `python/sglang/srt/mem_cache/registry.py`_
- **2026-08-19** [`41c018a9ec`](https://github.com/sgl-project/sglang/commit/41c018a9ec) [#35269](https://github.com/sgl-project/sglang/pull/35269)
  [UnifiedTree] feat: support runtime attach/detach (#35269)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/unified_cache/storage_attachment.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py` _+3 more__
- **2026-08-19** [`574274660f`](https://github.com/sgl-project/sglang/commit/574274660f) [#35445](https://github.com/sgl-project/sglang/pull/35445)
  [AMD] cookbook: serve Qwen3.5 MXFP4 on MI355X with an fp8_e4m3 KV cache (#35445)
  _Files: `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-08-19** [`0e4a09480c`](https://github.com/sgl-project/sglang/commit/0e4a09480c) [#35221](https://github.com/sgl-project/sglang/pull/35221)
  [HiCache] Support DCP with DSpark (#35221)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`_
- **2026-08-19** [`e614121866`](https://github.com/sgl-project/sglang/commit/e614121866) [#35424](https://github.com/sgl-project/sglang/pull/35424)
  [Fix] Scale the req_to_token row headroom by attn_dcp_size (#35424)
  _Files: `python/sglang/srt/mem_cache/allocation_sizing.py`_
- **2026-08-19** [`a72d8d29d3`](https://github.com/sgl-project/sglang/commit/a72d8d29d3) [#35446](https://github.com/sgl-project/sglang/pull/35446)
  Fix HiCache PP sync test fixture (#35446)
  _Files: `test/registered/unit/mem_cache/test_hiradix_pp_sync_drain.py`_
- **2026-08-19** [`3b065a56b0`](https://github.com/sgl-project/sglang/commit/3b065a56b0) [#33473](https://github.com/sgl-project/sglang/pull/33473)
  [HiCache] Batch PP write and load completion sync (#33473)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_hiradix_pp_sync_drain.py`_
- **2026-08-19** [`977412ae61`](https://github.com/sgl-project/sglang/commit/977412ae61) [#34798](https://github.com/sgl-project/sglang/pull/34798)
  [HiCache] Buffer-only mode for HiCache host memory layer (#34798)
  _Files: `benchmark/hicache/bench_buffer_mode.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/buffer_mode/__init__.py` _+15 more__
- **2026-08-18** [`37c09ff3d8`](https://github.com/sgl-project/sglang/commit/37c09ff3d8) [#35375](https://github.com/sgl-project/sglang/pull/35375)
  [Memory] Borrow CUDA graph pool storage for EAGLE sampling (#35375)
  _Files: `python/sglang/srt/compilation/cuda_piecewise_backend.py`, `python/sglang/srt/cuda_vmm_utils.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/kv_vmm_backing.py` _+7 more__
- **2026-08-18** [`8bb106cee9`](https://github.com/sgl-project/sglang/commit/8bb106cee9) [#35130](https://github.com/sgl-project/sglang/pull/35130)
  Fix NIXL cleaner grouping for hybrid cache keys (#35130)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/nixl_cleaner.py`, `test/registered/unit/mem_cache/test_hicache_nixl_cleaner.py`_
- **2026-08-18** [`480033def0`](https://github.com/sgl-project/sglang/commit/480033def0) [#35164](https://github.com/sgl-project/sglang/pull/35164)
  Refactor kv cache event mixin into a recorder (#35164)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/events.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/mamba_radix_cache.py` _+8 more__
- **2026-08-18** [`0077f84d37`](https://github.com/sgl-project/sglang/commit/0077f84d37) [#31180](https://github.com/sgl-project/sglang/pull/31180)
  [mem_cache][8/N] refactor: move MambaPoolHost to pool_host.mamba (#31180)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/pool_host/mamba.py`, `test/registered/kernels/ops/mamba/test_transfer_mamba.py` _+2 more__
- **2026-08-18** [`d528192bf9`](https://github.com/sgl-project/sglang/commit/d528192bf9) [#35161](https://github.com/sgl-project/sglang/pull/35161)
  Skip inkling sheared bias under batch invariance (#35161)
  _Files: `python/sglang/srt/models/inkling_common/attn.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_hybrid_bitexact.py`_
- **2026-08-17** [`6e8a4abb57`](https://github.com/sgl-project/sglang/commit/6e8a4abb57) [#35143](https://github.com/sgl-project/sglang/pull/35143)
  Add bit-exact class for MTP (#35143)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_hybrid_bitexact.py`_
- **2026-08-17** [`056808723e`](https://github.com/sgl-project/sglang/commit/056808723e) [#35128](https://github.com/sgl-project/sglang/pull/35128)
  [AMD] Guard ROCm 7.0 build from using hipMemcpyBatchAsync (#35128)
  _Files: `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`_
- **2026-08-17** [`8cc112d486`](https://github.com/sgl-project/sglang/commit/8cc112d486) [#30531](https://github.com/sgl-project/sglang/pull/30531)
  [DSA] Skip indexer KV cache for skip-topk layers (#30531)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/mem_cache/dsa_cache_layer_split.py`, `python/sglang/srt/mem_cache/index_key_cache.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` _+6 more__
- **2026-08-17** [`43226af812`](https://github.com/sgl-project/sglang/commit/43226af812) [#34519](https://github.com/sgl-project/sglang/pull/34519)
  fix(hicache): limit load-back pending to write-back (#34519)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_

## ROCm / AMD  (18 commits)

- **2026-08-24** [`97b176e64c`](https://github.com/sgl-project/sglang/commit/97b176e64c) [#32597](https://github.com/sgl-project/sglang/pull/32597)
  Support streaming session on NPU (#32597)
  _Files: `python/sglang/srt/session/streaming_session.py`, `test/registered/unit/spec/test_decode_bookkeeping_ownership.py`_
- **2026-08-23** [`95f5ecd3d2`](https://github.com/sgl-project/sglang/commit/95f5ecd3d2) [#35854](https://github.com/sgl-project/sglang/pull/35854)
  [AMD] Update amd deepseek v4 cookbook 0822 (#35854)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-08-23** [`155aa26c19`](https://github.com/sgl-project/sglang/commit/155aa26c19) [#36004](https://github.com/sgl-project/sglang/pull/36004)
  [AMD][DSV4] perf: use full 1024-thread block for indexer top-k on ROCm (#36004)
  _Files: `python/sglang/kernels/aot/csrc/elementwise/deepseek_v4_topk.cu`, `python/sglang/kernels/aot/tests/test_topk.py`_
- **2026-08-22** [`d315eb7250`](https://github.com/sgl-project/sglang/commit/d315eb7250) [#32577](https://github.com/sgl-project/sglang/pull/32577)
  [AMD] DeepSeek-V4: add aiter fused mHC post+pre with cross-layer boundary dispatch (#32577)
  _Files: `python/sglang/srt/models/deepseek_common/amd/deepseek_v4_fused_mhc.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/models/test_deepseek_v4_amd_fused_mhc.py`, `test/registered/unit/models/test_deepseek_v4_fused_mhc_policy.py`_
- **2026-08-21** [`4d42deff0a`](https://github.com/sgl-project/sglang/commit/4d42deff0a) [#35911](https://github.com/sgl-project/sglang/pull/35911)
  chore: bump docs install version to 0.5.18 (#35911)
  _Files: `docs/docs/get-started/install.mdx`, `docs/docs/hardware-platforms/amd_gpu.mdx`_
- **2026-08-21** [`6a12583679`](https://github.com/sgl-project/sglang/commit/6a12583679) [#35810](https://github.com/sgl-project/sglang/pull/35810)
  [AMD] Update ROCm AITER pin to c16d44b (#35810)
  _Files: `docker/rocm.Dockerfile`_
- **2026-08-21** [`a688682f4b`](https://github.com/sgl-project/sglang/commit/a688682f4b) [#35764](https://github.com/sgl-project/sglang/pull/35764)
  [AMD][CI] Fix ROCm 7.0's dead apt index fail the MORI dependency install (#35764)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`, `test/registered/unit/tools/test_amd_ci_install_dependency.py`_
- **2026-08-21** [`78c964d9d7`](https://github.com/sgl-project/sglang/commit/78c964d9d7) [#35654](https://github.com/sgl-project/sglang/pull/35654)
  [AMD] Retry transient network failures in ROCm Dockerfile curl fetches (#35654)
  _Files: `docker/rocm.Dockerfile`_
- **2026-08-20** [`5a7b26c636`](https://github.com/sgl-project/sglang/commit/5a7b26c636) [#32832](https://github.com/sgl-project/sglang/pull/32832)
  [AMD] [sgl-kernel] Bypass caches for peer traffic in ROCm custom all-reduce (#32832)
  _Files: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce.cuh`, `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`_
- **2026-08-20** [`0149f56e84`](https://github.com/sgl-project/sglang/commit/0149f56e84) [#35750](https://github.com/sgl-project/sglang/pull/35750)
  [CI] Gate `/rerun-test` on commenter trust and remove `/rerun-stage` (#35750)
  _Files: `.claude/skills/ci-workflow-guide/SKILL.md`, `.github/CI_PERMISSIONS.json`, `.github/FOLDER_README.md`, `.github/update_ci_permission.py` _+8 more__
- **2026-08-20** [`09b7af1371`](https://github.com/sgl-project/sglang/commit/09b7af1371) [#34813](https://github.com/sgl-project/sglang/pull/34813)
  [CI] Surface AMD ROCm 7.2 state in the PR CI-states block (#34813)
  _Files: `.github/workflows/pr-states.yml`_
- **2026-08-20** [`dc175b3ad2`](https://github.com/sgl-project/sglang/commit/dc175b3ad2) [#34452](https://github.com/sgl-project/sglang/pull/34452)
  [CI][AMD] Run the profiling suite without CUDA graphs on ROCm (#34452)
  _Files: `test/registered/profiling/test_start_profile.py`_
- **2026-08-20** [`c7478228dd`](https://github.com/sgl-project/sglang/commit/c7478228dd) [#30984](https://github.com/sgl-project/sglang/pull/30984)
  [AMD] [Docker] Upgrade Python 3.12 + torch 2.11 + triton 3.7 in ROCm 7.2.4 (#30984)
  _Files: `.github/workflows/pr-test-amd-extra.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/release-docker-amd-rocm720-nightly.yml`, `.github/workflows/release-docker-amd.yml` _+5 more__
- **2026-08-19** [`f446e853e7`](https://github.com/sgl-project/sglang/commit/f446e853e7) [#33313](https://github.com/sgl-project/sglang/pull/33313)
  [AMD] DeepSeek-V4: route decode wo_a bf16 batched matmul to aiter batched_gemm_bf16 (#33313)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/models/test_deepseek_v4_amd_wo_a_bf16.py`_
- **2026-08-19** [`ebec85f606`](https://github.com/sgl-project/sglang/commit/ebec85f606) [#35467](https://github.com/sgl-project/sglang/pull/35467)
  [AMD][DI][CI] Run MI355X disagg nightly at 7AM UTC (#35467)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-08-18** [`27596abdc0`](https://github.com/sgl-project/sglang/commit/27596abdc0) [#35263](https://github.com/sgl-project/sglang/pull/35263)
  [AMD] Update amd k3 cookbook for PR#34580 (#35263)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-08-18** [`8ea5229d42`](https://github.com/sgl-project/sglang/commit/8ea5229d42) [#34985](https://github.com/sgl-project/sglang/pull/34985)
  [AMD] Add the Kimi-K3 MI35x perf benchmarks in nightly (#34985)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `test/registered/amd/perf/mi35x/test_kimi_k3_perf_mi35x.py`_
- **2026-08-17** [`816ea65058`](https://github.com/sgl-project/sglang/commit/816ea65058) [#32568](https://github.com/sgl-project/sglang/pull/32568)
  [AMD] Add Kimi-K3 8-GPU MI35x nightly accuracy CI (#32568)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `test/registered/amd/accuracy/mi35x/test_kimi_k3_eval_mi35x.py`, `test/run_suite.py`_

## Other  (17 commits)

- **2026-08-24** [`317da0964e`](https://github.com/sgl-project/sglang/commit/317da0964e) [#35072](https://github.com/sgl-project/sglang/pull/35072)
  [Intel XPU] support prefill only models for xpu (#35072)
  _Files: `test/registered/xpu/test_xpu_classification.py`, `test/registered/xpu/test_xpu_embedding.py`, `test/registered/xpu/test_xpu_rerank.py`, `test/registered/xpu/test_xpu_reward.py`_
- **2026-08-24** [`f464e77d17`](https://github.com/sgl-project/sglang/commit/f464e77d17) [#36150](https://github.com/sgl-project/sglang/pull/36150)
  fix(mini-lb): forward the flush_cache timeout param to workers (#36150)
  _Files: `sgl-model-gateway/bindings/python/src/sglang_router/mini_lb.py`_
- **2026-08-24** [`514b997e6c`](https://github.com/sgl-project/sglang/commit/514b997e6c) [#35227](https://github.com/sgl-project/sglang/pull/35227)
  Register CPU CI for 17 e2e tests and partition xeon base-c suite (#35227)
- **2026-08-23** [`8014d9d062`](https://github.com/sgl-project/sglang/commit/8014d9d062) [#35988](https://github.com/sgl-project/sglang/pull/35988)
  [npu] Kill evalscope session by process group and fix report score parsing (#35988)
  _Files: `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`_
- **2026-08-23** [`a43592dce5`](https://github.com/sgl-project/sglang/commit/a43592dce5) [#35909](https://github.com/sgl-project/sglang/pull/35909)
  config: pin two orderings resolution relies on (#35909)
  _Files: `test/registered/unit/server_args/test_model_config_reads_resolved_input.py`, `test/registered/unit/test_chain_read_ratchet.py`, `test/registered/unit/test_supplied_instance_exposure_ratchet.py`_
- **2026-08-22** [`cb10ca16dd`](https://github.com/sgl-project/sglang/commit/cb10ca16dd) [#33279](https://github.com/sgl-project/sglang/pull/33279)
  [FEAT] Weight Daemon abstraction (#33279)
  _Files: `python/sglang/srt/weight_cache/daemon.py`, `python/sglang/srt/weight_cache/ipc_loader.py`, `python/sglang/srt/weight_cache/transport.py`, `test/registered/unit/model_loader/test_weight_cache_protocol.py`_
- **2026-08-20** [`94907f05c4`](https://github.com/sgl-project/sglang/commit/94907f05c4) [#35600](https://github.com/sgl-project/sglang/pull/35600)
  Add CI permissions for four contributors (#35600)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-08-20** [`9b249a25a1`](https://github.com/sgl-project/sglang/commit/9b249a25a1) [#35293](https://github.com/sgl-project/sglang/pull/35293)
  test: switch the Inkling-Small NVFP4 deterministic suite to DSPARK (#35293)
  _Files: `test/registered/models_e2e/test_inkling_small_nvfp4.py`_
- **2026-08-20** [`0bda0b168a`](https://github.com/sgl-project/sglang/commit/0bda0b168a) [#35361](https://github.com/sgl-project/sglang/pull/35361)
  [Fix]: exclude SM120 from attn-res TMA dispatch (#35361)
  _Files: `python/sglang/srt/layers/attn_residual.py`, `test/registered/unit/layers/test_attn_residual.py`_
- **2026-08-20** [`58e327480a`](https://github.com/sgl-project/sglang/commit/58e327480a) [#34802](https://github.com/sgl-project/sglang/pull/34802)
  update codeowner (#34802)
  _Files: `.github/CODEOWNERS`_
- **2026-08-20** [`a49560ce50`](https://github.com/sgl-project/sglang/commit/a49560ce50) [#35597](https://github.com/sgl-project/sglang/pull/35597)
  [misc] Add a comment style rule to .claude/rules (#35597)
  _Files: `.claude/rules/comment-style.md`, `python/sglang/srt/model_loader/ci_weight_validation.py`_
- **2026-08-20** [`f736895ce9`](https://github.com/sgl-project/sglang/commit/f736895ce9) [#35575](https://github.com/sgl-project/sglang/pull/35575)
  Make PR babysitter launcher fork-safe (#35575)
  _Files: `scripts/playground/launch_pr_babysitters.sh`_
- **2026-08-20** [`1df78c2cf1`](https://github.com/sgl-project/sglang/commit/1df78c2cf1) [#30874](https://github.com/sgl-project/sglang/pull/30874)
  chore: bump tilelang to 0.1.12 (#30874)
  _Files: `python/pyproject.toml`_
- **2026-08-19** [`082aac8fce`](https://github.com/sgl-project/sglang/commit/082aac8fce) [#31378](https://github.com/sgl-project/sglang/pull/31378)
  [Bugfix] Fix min-new-token EOS handling (#31378)
  _Files: `python/sglang/srt/sampling/penaltylib/min_new_tokens.py`, `test/registered/unit/sampling/test_penaltylib.py`_
- **2026-08-19** [`c863760ae1`](https://github.com/sgl-project/sglang/commit/c863760ae1) [#35298](https://github.com/sgl-project/sglang/pull/35298)
  [Fix] DCP: advertise the logical KV-event block size (#35298)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-08-18** [`5b60b7c651`](https://github.com/sgl-project/sglang/commit/5b60b7c651) [#35214](https://github.com/sgl-project/sglang/pull/35214)
  [DSV4] Turn on mhc post pre fusion by default (#35214)
  _Files: `python/sglang/srt/environ.py`_
- **2026-08-17** [`4b06f917ca`](https://github.com/sgl-project/sglang/commit/4b06f917ca) [#35094](https://github.com/sgl-project/sglang/pull/35094)
  Upd: code owners (#35094)
  _Files: `.github/CODEOWNERS`_

## Tensor / Data Parallel  (16 commits)

- **2026-08-24** [`1daa94a069`](https://github.com/sgl-project/sglang/commit/1daa94a069) [#32856](https://github.com/sgl-project/sglang/pull/32856)
  [CPU] Fix NUMA/core binding for DP ranks (#32856)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/utils/numa_utils.py`, `test/registered/cpu/test_binding.py`_
- **2026-08-24** [`167c339c8e`](https://github.com/sgl-project/sglang/commit/167c339c8e) [#35669](https://github.com/sgl-project/sglang/pull/35669)
  [CPU] Add check for fused_input_proj in TP=4 (#35669)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-08-22** [`3e096629cf`](https://github.com/sgl-project/sglang/commit/3e096629cf) [#35607](https://github.com/sgl-project/sglang/pull/35607)
  [CI] Re-enable B300 jobs (#35607)
  _Files: `.github/workflows/pr-test.yml`, `test/registered/models_e2e/test_dsa_glm52_pd_mtp_cp_layersplit.py`, `test/registered/models_e2e/test_kimi_k3_b300.py`_
- **2026-08-21** [`44c90c6282`](https://github.com/sgl-project/sglang/commit/44c90c6282) [#34973](https://github.com/sgl-project/sglang/pull/34973)
  [AMD] DSv4: fuse the qk-norm-rope pair on the MTP target-verify path (#34973)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-08-19** [`38b74d294b`](https://github.com/sgl-project/sglang/commit/38b74d294b) [#35283](https://github.com/sgl-project/sglang/pull/35283)
  Add docs for TP LMHead optimizaiton (#35283)
  _Files: `docs/docs/advanced_features/dp_dpa_smg_guide.mdx`_
- **2026-08-19** [`23f2320c95`](https://github.com/sgl-project/sglang/commit/23f2320c95) [#35458](https://github.com/sgl-project/sglang/pull/35458)
  [Docs] PaddleOCR-VL: update which stage of the pipeline this serves and show real output (#35458)
  _Files: `docs/cookbook/autoregressive/Baidu/PaddleOCR-VL.mdx`_
- **2026-08-18** [`7dcaf11987`](https://github.com/sgl-project/sglang/commit/7dcaf11987) [#35061](https://github.com/sgl-project/sglang/pull/35061)
  [Fix] Select custom all-reduce v2 by topology capability (#35061)
  _Files: `python/sglang/srt/distributed/device_communicators/configs/custom_all_reduce_v2.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py` _+4 more__
- **2026-08-18** [`499e90a125`](https://github.com/sgl-project/sglang/commit/499e90a125) [#33685](https://github.com/sgl-project/sglang/pull/33685)
  [NPU CI] Reorganize test output/log directory structure with workflow context (#33685)
- **2026-08-18** [`a779a2a2a5`](https://github.com/sgl-project/sglang/commit/a779a2a2a5) [#35196](https://github.com/sgl-project/sglang/pull/35196)
  [Chore] Move version tag helper to release scripts (#35196)
  _Files: `.github/workflows/release-docker-amd-nightly.yml`, `.github/workflows/release-docker-amd-rocm720-nightly.yml`, `.github/workflows/release-docker-amd-rocm7_15-nightly.yml`, `.github/workflows/release-pypi-nightly.yml` _+11 more__
- **2026-08-18** [`fcdaaf8a5d`](https://github.com/sgl-project/sglang/commit/fcdaaf8a5d) [#32313](https://github.com/sgl-project/sglang/pull/32313)
  [Feature] Optimize TP LMHead with All-to-All (#32313)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/logits_processor.py` _+3 more__
- **2026-08-18** [`c2c1c4d3eb`](https://github.com/sgl-project/sglang/commit/c2c1c4d3eb) [#35220](https://github.com/sgl-project/sglang/pull/35220)
  [CI] Move DSA PD+MTP+CP Layersplit test to basic B300 test suite (#35220)
  _Files: `test/registered/models_e2e/test_dsa_glm52_pd_mtp_cp_layersplit.py`_
- **2026-08-17** [`c70c7d72a8`](https://github.com/sgl-project/sglang/commit/c70c7d72a8) [#35027](https://github.com/sgl-project/sglang/pull/35027)
  config: the readback and the resolving view say what they are (#35027)
  _Files: `experimental/sgl-router/src/workers/introspect.rs`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/grpc_bridge.py`, `python/sglang/srt/entrypoints/http_server.py` _+8 more__
- **2026-08-17** [`770e7b47a2`](https://github.com/sgl-project/sglang/commit/770e7b47a2) [#34478](https://github.com/sgl-project/sglang/pull/34478)
  [Spec] Support output logprobs with DSpark (#34478)
- **2026-08-17** [`0d8c850a35`](https://github.com/sgl-project/sglang/commit/0d8c850a35) [#35110](https://github.com/sgl-project/sglang/pull/35110)
  [Fix] Read the DSA prefill CP flag from the parallel config bag in bootstrap (#35110)
  _Files: `python/sglang/srt/distributed/bootstrap.py`_
- **2026-08-17** [`9be3044b9c`](https://github.com/sgl-project/sglang/commit/9be3044b9c) [#34999](https://github.com/sgl-project/sglang/pull/34999)
  [Engine] Freeze GC after server warmup (#34999)
  _Files: `python/sglang/srt/entrypoints/http_server.py`_
- **2026-08-17** [`0e500feae6`](https://github.com/sgl-project/sglang/commit/0e500feae6) [#34856](https://github.com/sgl-project/sglang/pull/34856)
  fix tpot by adjusting the sliding max-prefill-size window size (#34856)
  _Files: `test/registered/npu/performance/minimax_m2_5/test_npu_minimax_m2_5_w8a8_4p_in64k_out1k_prefix90_50ms.py`, `test/registered/npu/performance/qwen3-8b/test_npu_qwen3_8b_w8a8_1p_in3k5_out1k5_50ms.py`, `test/registered/npu/performance/qwen3_235b_a22b/test_npu_qwen3_235b_w8a8_8p_in3k5_out1k5_50ms.py`, `test/registered/npu/performance/qwen3_30b_a3b/test_npu_qwen3_30b_w8a8_1p_in3k5_out1k5_50ms.py` _+3 more__

## Scheduler / Batching  (11 commits)

- **2026-08-24** [`fb6e3872e1`](https://github.com/sgl-project/sglang/commit/fb6e3872e1) [#36005](https://github.com/sgl-project/sglang/pull/36005)
  [Mamba] fix mamba index h unexpected assertion for dcp (#36005)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-08-20** [`f825d72936`](https://github.com/sgl-project/sglang/commit/f825d72936) [#35205](https://github.com/sgl-project/sglang/pull/35205)
  [Sampling] Restore finite top-k requirement for sampling masks (#35205)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/sampling/test_sampling_mask.py`_
- **2026-08-20** [`779e593bd1`](https://github.com/sgl-project/sglang/commit/779e593bd1) [#26510](https://github.com/sgl-project/sglang/pull/26510)
  Fix _GenerationStreamAccumulator logprob_end off-by-one under retract (#26510)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `test/registered/scheduler/test_retract_decode_logprob.py`, `test/registered/unit/managers/test_output_streamer_logprobs.py`_
- **2026-08-20** [`5a100d9086`](https://github.com/sgl-project/sglang/commit/5a100d9086) [#35622](https://github.com/sgl-project/sglang/pull/35622)
  [misc] Trim restating comments and docstrings in srt/managers (#35622)
  _Files: `.claude/rules/comment-style.md`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/managers/tokenizer_manager_score_mixin.py`_
- **2026-08-18** [`526af15845`](https://github.com/sgl-project/sglang/commit/526af15845) [#35248](https://github.com/sgl-project/sglang/pull/35248)
  [Metrics] Discount queued prefill load by recent cache hits when waiting-queue matching is off (#35248)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/load_inquirer.py` _+3 more__
- **2026-08-18** [`83d7d45330`](https://github.com/sgl-project/sglang/commit/83d7d45330) [#34627](https://github.com/sgl-project/sglang/pull/34627)
  fix: preserve output logprobs without input logprobs (#34627)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_flat_raw_top_logprobs.py`_
- **2026-08-18** [`0065fbfae1`](https://github.com/sgl-project/sglang/commit/0065fbfae1) [#35191](https://github.com/sgl-project/sglang/pull/35191)
  [Scheduler] Cap prefill-delayer queue target by admission capacity (#35191)
  _Files: `python/sglang/srt/managers/prefill_delayer.py`, `python/sglang/srt/server_args.py`, `test/registered/scheduler/test_prefill_delayer.py`_
- **2026-08-18** [`fc0b95e7ba`](https://github.com/sgl-project/sglang/commit/fc0b95e7ba) [#24911](https://github.com/sgl-project/sglang/pull/24911)
  Profiling Enhancements [2/3]: detailed execution step annotations (#24911)
  _Files: `docs/docs/developer_guide/benchmark_and_profiling.mdx`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler_components/profiler_manager.py`, `python/sglang/srt/model_executor/step_span_utils.py` _+2 more__
- **2026-08-17** [`b3c8f0d923`](https://github.com/sgl-project/sglang/commit/b3c8f0d923) [#35028](https://github.com/sgl-project/sglang/pull/35028)
  config: one control-plane log for the process (#35028)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/runtime_context.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py` _+4 more__
- **2026-08-17** [`b42abbb1ba`](https://github.com/sgl-project/sglang/commit/b42abbb1ba) [#34316](https://github.com/sgl-project/sglang/pull/34316)
  [metrics] Fix prefill FLOPs estimate to count prefix and per-request causal pairs (#34316)
  _Files: `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`_
- **2026-08-17** [`12a455a910`](https://github.com/sgl-project/sglang/commit/12a455a910) [#34997](https://github.com/sgl-project/sglang/pull/34997)
  Fix world-size-one aliasing in MLP batch sync (#34997)
  _Files: `python/sglang/srt/managers/scheduler_components/dp_attn.py`_

## Triton / Kernels  (8 commits)

- **2026-08-24** [`acba8921bf`](https://github.com/sgl-project/sglang/commit/acba8921bf) [#33840](https://github.com/sgl-project/sglang/pull/33840)
  [XPU] Support softmax_lse in sgl_kernel::fwd API (#33840)
  _Files: `python/sglang/srt/hardware_backend/xpu/graph_runner/xpu_graph_runner.py`_
- **2026-08-24** [`fd73d4b019`](https://github.com/sgl-project/sglang/commit/fd73d4b019) [#35506](https://github.com/sgl-project/sglang/pull/35506)
  [CPU] Add graph register for fused_sigmoid_mul_cpu, fused_qk_gemma_rmsnorm (#35506)
  _Files: `python/sglang/kernels/aot/csrc/cpu/activation.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/models/qwen3_5.py` _+1 more__
- **2026-08-21** [`590b11a5ef`](https://github.com/sgl-project/sglang/commit/590b11a5ef) [#35711](https://github.com/sgl-project/sglang/pull/35711)
  [Runtime] Don't override CUDA_MODULE_LOADING (#35711)
  _Files: `python/sglang/srt/entrypoints/engine.py`_
- **2026-08-21** [`f3fe81583e`](https://github.com/sgl-project/sglang/commit/f3fe81583e) [#35726](https://github.com/sgl-project/sglang/pull/35726)
  add py env activate in xpu kernel release workflow (#35726)
  _Files: `.github/workflows/release-whl-kernel-xpu.yml`_
- **2026-08-20** [`92eeed41d7`](https://github.com/sgl-project/sglang/commit/92eeed41d7) [#35756](https://github.com/sgl-project/sglang/pull/35756)
  [Docker] Defer CUDA 13 NCCL override until after dependency resolution (#35756)
  _Files: `docker/Dockerfile`_
- **2026-08-20** [`9234e40aed`](https://github.com/sgl-project/sglang/commit/9234e40aed) [#35571](https://github.com/sgl-project/sglang/pull/35571)
  [sampling] Fix int32 offset overflow in top-k renorm Triton kernels (#35571)
  _Files: `python/sglang/kernels/ops/sampling/renorm_triton.py`_
- **2026-08-18** [`5eb117f6ca`](https://github.com/sgl-project/sglang/commit/5eb117f6ca) [#35050](https://github.com/sgl-project/sglang/pull/35050)
  [XPU] Fix decode graph runner is_current_stream_capturing on non-CUDA devices (#35050)
  _Files: `docker/xpu.Dockerfile`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`_
- **2026-08-18** [`0ea262e6e5`](https://github.com/sgl-project/sglang/commit/0ea262e6e5) [#33679](https://github.com/sgl-project/sglang/pull/33679)
  [XPU] xpu kernel release workflow (#33679)
  _Files: `.github/workflows/release-whl-kernel-xpu.yml`, `scripts/update_kernel_whl_index.py`_

## Models  (8 commits)

- **2026-08-24** [`0c1e9bda57`](https://github.com/sgl-project/sglang/commit/0c1e9bda57) [#35915](https://github.com/sgl-project/sglang/pull/35915)
  [OpenAI] Drop empty assistant turns for mistral_common tokenizers (#35915)
  _Files: `python/sglang/srt/utils/hf_transformers/mistral_utils.py`, `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`_
- **2026-08-22** [`4cb5aebfe0`](https://github.com/sgl-project/sglang/commit/4cb5aebfe0) [#35825](https://github.com/sgl-project/sglang/pull/35825)
  [docs] Re-measure the Qwen3.8-27B RTX 5090, RTX PRO 6000 and DGX Spark grids on 1cf2b8c (#35825)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b.jsx`_
- **2026-08-22** [`0ee3749e07`](https://github.com/sgl-project/sglang/commit/0ee3749e07) [#35921](https://github.com/sgl-project/sglang/pull/35921)
  [Fix] Read the granite sinks dtype from the exec bag, not the legacy global shim (#35921)
  _Files: `python/sglang/srt/models/granite.py`_
- **2026-08-21** [`fe8f9d7457`](https://github.com/sgl-project/sglang/commit/fe8f9d7457) [#35920](https://github.com/sgl-project/sglang/pull/35920)
  [Docs] Add --prerelease=allow to cookbook uv install commands (#35920)
  _Files: `.claude/skills/cookbook-add-model/templates/page.mdx.tmpl`, `docs/cookbook/autoregressive/Baidu/PaddleOCR-VL.mdx`, `docs/cookbook/autoregressive/Baidu/Unlimited-OCR.mdx`, `docs/cookbook/autoregressive/DeepReinforce/Ornith-1.0.mdx` _+24 more__
- **2026-08-20** [`d287880a7a`](https://github.com/sgl-project/sglang/commit/d287880a7a) [#35450](https://github.com/sgl-project/sglang/pull/35450)
  Update deepep for SBO feature (#35450)
  _Files: `python/pyproject.toml`, `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`_
- **2026-08-19** [`1beb805356`](https://github.com/sgl-project/sglang/commit/1beb805356) [#34953](https://github.com/sgl-project/sglang/pull/34953)
  [Perf] Restore the 16-token router GEMM threshold on SM10X (#34953)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-08-17** [`b956e916ae`](https://github.com/sgl-project/sglang/commit/b956e916ae) [#35121](https://github.com/sgl-project/sglang/pull/35121)
  docs(cookbook): add Qwen3.8-27B DGX Spark configs (#35121)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b.jsx`_
- **2026-08-17** [`e03c53fc13`](https://github.com/sgl-project/sglang/commit/e03c53fc13) [#35065](https://github.com/sgl-project/sglang/pull/35065)
  docs(cookbook): Qwen3.8-27B deployment grid rework (#35065)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b-benchmarks.jsx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b.jsx`_

## Docs / Examples  (7 commits)

- **2026-08-24** [`11b1b4c374`](https://github.com/sgl-project/sglang/commit/11b1b4c374) [#36123](https://github.com/sgl-project/sglang/pull/36123)
  [NPU] [DOC] Polish English wording in NPU docs (#36123)
  _Files: `docs/docs/developer_guide/msprobe_debugging_guide.mdx`, `docs/docs/hardware-platforms/ascend-npus/development/support_new_models.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/environment_variables.mdx`_
- **2026-08-23** [`9b1b06b8e6`](https://github.com/sgl-project/sglang/commit/9b1b06b8e6) [#35508](https://github.com/sgl-project/sglang/pull/35508)
  [NPU] [DOC] Add Ascend NPU (A3) recipe to the Kimi-K3 cookbook (#35508)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/_kimi_k3_mamba_ratio_calculator.jsx`, `docs/src/snippets/_playground.jsx` _+1 more__
- **2026-08-23** [`c9f6b9ba25`](https://github.com/sgl-project/sglang/commit/c9f6b9ba25) [#35836](https://github.com/sgl-project/sglang/pull/35836)
  [NPU] [DOC] Refresh supported features and models on Ascend NPU (#35836)
  _Files: `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_models.mdx`_
- **2026-08-21** [`2440820528`](https://github.com/sgl-project/sglang/commit/2440820528) [#35210](https://github.com/sgl-project/sglang/pull/35210)
  docs: add website link to README header (#35210)
  _Files: `README.md`_
- **2026-08-20** [`ba433bb462`](https://github.com/sgl-project/sglang/commit/ba433bb462) [#35419](https://github.com/sgl-project/sglang/pull/35419)
  [Docs] Update contribution guide (#35419)
  _Files: `docs/docs/developer_guide/contribution_guide.mdx`, `docs/docs/developer_guide/evaluating_new_models.mdx`_
- **2026-08-18** [`9ffc2856fb`](https://github.com/sgl-project/sglang/commit/9ffc2856fb) [#35218](https://github.com/sgl-project/sglang/pull/35218)
  docs: sync LMSYS SGLang blog cards (#35218)
  _Files: `docs/index.mdx`_
- **2026-08-17** [`f019f0b064`](https://github.com/sgl-project/sglang/commit/f019f0b064) [#35068](https://github.com/sgl-project/sglang/pull/35068)
  [Docs] Feature MiniMax-H3 in the popular-models banner (#35068)
  _Files: `docs/src/snippets/configs/popular-models.jsx`_

## Serving / API  (7 commits)

- **2026-08-21** [`c3735625de`](https://github.com/sgl-project/sglang/commit/c3735625de) [#35778](https://github.com/sgl-project/sglang/pull/35778)
  fix(grpc): derive choice count before normalization (#35778)
  _Files: `python/sglang/srt/entrypoints/grpc_bridge.py`, `test/registered/unit/entrypoints/test_grpc_bridge.py`_
- **2026-08-21** [`61c2da42bb`](https://github.com/sgl-project/sglang/commit/61c2da42bb) [#35480](https://github.com/sgl-project/sglang/pull/35480)
  [Fix] Pass Anthropic thinking history as reasoning_content for custom chat encoders (#35480)
  _Files: `python/sglang/srt/entrypoints/anthropic/serving.py`, `python/sglang/srt/entrypoints/openai/chat_encoding.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/anthropic/test_serving.py` _+1 more__
- **2026-08-20** [`a4ef828207`](https://github.com/sgl-project/sglang/commit/a4ef828207) [#35323](https://github.com/sgl-project/sglang/pull/35323)
  fix(openai): avoid duplicate routed expert in response when `return_meta_info = True` (#35323)
  _Files: `docs/docs/basic_usage/openai_api_completions.mdx`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-08-20** [`61fa64ae7e`](https://github.com/sgl-project/sglang/commit/61fa64ae7e) [#35714](https://github.com/sgl-project/sglang/pull/35714)
  feat(grpc): expose KV event discovery metadata (#35714)
  _Files: `python/sglang/srt/entrypoints/grpc_bridge.py`_
- **2026-08-20** [`360d10d6bc`](https://github.com/sgl-project/sglang/commit/360d10d6bc) [#33370](https://github.com/sgl-project/sglang/pull/33370)
  [Feature] Add process-local in-memory KV indexer and Router integration (#33370)
  _Files: `.github/workflows/pr-test-sgl-router.yml`, `.pre-commit-config.yaml`, `docker/sgl-router.Dockerfile`, `experimental/sgl-router/Cargo.toml` _+38 more__
- **2026-08-19** [`88f6074392`](https://github.com/sgl-project/sglang/commit/88f6074392) [#33518](https://github.com/sgl-project/sglang/pull/33518)
  feat(api): add sglext_spec (#33518)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_completions.py`, `python/sglang/srt/entrypoints/openai/utils.py` _+2 more__
- **2026-08-18** [`e6df23f3c2`](https://github.com/sgl-project/sglang/commit/e6df23f3c2) [#35225](https://github.com/sgl-project/sglang/pull/35225)
  refactor: rename chat response token IDs (#35225)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/sampling/test_sampling_mask.py`, `test/registered/unit/entrypoints/openai/test_protocol.py` _+1 more__

## Speculative Decoding  (6 commits)

- **2026-08-20** [`99c12218c3`](https://github.com/sgl-project/sglang/commit/99c12218c3) [#35397](https://github.com/sgl-project/sglang/pull/35397)
  Support custom draft worker classes in DSpark (#35397)
  _Files: `python/sglang/srt/speculative/draft_worker_common.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-08-18** [`9401db3f29`](https://github.com/sgl-project/sglang/commit/9401db3f29) [#35195](https://github.com/sgl-project/sglang/pull/35195)
  [AMD] Scope the EAGLE greedy-verify TP broadcast to ROCm only (#35195)
  _Files: `python/sglang/srt/speculative/eagle_utils.py`_
- **2026-08-17** [`c0b6474b43`](https://github.com/sgl-project/sglang/commit/c0b6474b43) [#35207](https://github.com/sgl-project/sglang/pull/35207)
  [Spec] Reduce host-side overhead in ngram draft prep (#35207)
  _Files: `python/sglang/srt/speculative/ngram_worker.py`_
- **2026-08-17** [`032fe9c891`](https://github.com/sgl-project/sglang/commit/032fe9c891) [#35198](https://github.com/sgl-project/sglang/pull/35198)
  [Spec] Relay ngram accept tokens through the FutureMap (#35198)
  _Files: `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/ngram_info.py`, `python/sglang/srt/speculative/ngram_worker.py`_
- **2026-08-17** [`711bdacb82`](https://github.com/sgl-project/sglang/commit/711bdacb82) [#35059](https://github.com/sgl-project/sglang/pull/35059)
  [Spec] Resolve shared-read ends from the backend declaration alone (#35059)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/speculative/ngram_worker.py` _+3 more__
- **2026-08-17** [`07a28ec5cf`](https://github.com/sgl-project/sglang/commit/07a28ec5cf) [#35064](https://github.com/sgl-project/sglang/pull/35064)
  docs: fix Qwen3.8-27B mamba ratio calculator for speculative decoding (#35064)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/_qwen38_mamba_ratio_calculator.jsx`_

## CI / Build  (5 commits)

- **2026-08-24** [`e28b9cf7b0`](https://github.com/sgl-project/sglang/commit/e28b9cf7b0) [#36092](https://github.com/sgl-project/sglang/pull/36092)
  Npu single node test timeout config (#36092)
  _Files: `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml`, `.github/workflows/pr-test-npu.yml`_
- **2026-08-24** [`ec334b17e2`](https://github.com/sgl-project/sglang/commit/ec334b17e2) [#36146](https://github.com/sgl-project/sglang/pull/36146)
  xeon ci fail fast strategy change (#36146)
  _Files: `.github/workflows/pr-test-xeon.yml`_
- **2026-08-21** [`aa3f766799`](https://github.com/sgl-project/sglang/commit/aa3f766799) [#35627](https://github.com/sgl-project/sglang/pull/35627)
  [CI] Temporarily disable B300 jobs (#35627)
  _Files: `.github/workflows/pr-test.yml`_
- **2026-08-18** [`3a8f522f65`](https://github.com/sgl-project/sglang/commit/3a8f522f65) [#30612](https://github.com/sgl-project/sglang/pull/30612)
  install sglang in virtual env instead of system path (#30612)
  _Files: `docker/Dockerfile`_
- **2026-08-18** [`b814a7e812`](https://github.com/sgl-project/sglang/commit/b814a7e812) [#35392](https://github.com/sgl-project/sglang/pull/35392)
  [CI] Skip fast-fail for scheduled stages (#35392)
  _Files: `.github/workflows/_pr-test-stage.yml`_

## Structured Output  (4 commits)

- **2026-08-23** [`27aa48bca1`](https://github.com/sgl-project/sglang/commit/27aa48bca1) [#34237](https://github.com/sgl-project/sglang/pull/34237)
  [Fix] lfm2 detector: recover tool calls dropped by common model-outpu… (#34237)
  _Files: `python/sglang/srt/function_call/lfm2_detector.py`, `python/sglang/srt/function_call/pythonic_detector.py`, `test/registered/unit/function_call/test_function_call_parser.py`_
- **2026-08-19** [`c7e2c08d14`](https://github.com/sgl-project/sglang/commit/c7e2c08d14) [#34679](https://github.com/sgl-project/sglang/pull/34679)
  fix(constrained): reject NUL bytes in grammar specs to stop an xgrammar segfault (#34679)
  _Files: `python/sglang/srt/constrained/base_grammar_backend.py`, `test/registered/unit/constrained/test_base_grammar_backend.py`_
- **2026-08-19** [`3391ab3712`](https://github.com/sgl-project/sglang/commit/3391ab3712) [#35215](https://github.com/sgl-project/sglang/pull/35215)
  [Constrained] Support MistralCommon tokenizers in the XGrammar backend (#35215)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/utils/hf_transformers/mistral_utils.py`, `test/registered/unit/constrained/test_mistral_common_xgrammar.py`_
- **2026-08-18** [`307a90f6d3`](https://github.com/sgl-project/sglang/commit/307a90f6d3) [#34881](https://github.com/sgl-project/sglang/pull/34881)
  Stop losing Kimi-K3 tool calls to reasoning, constraint conflicts, and truncation (#34881)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py`, `python/sglang/srt/function_call/kimik3_detector.py` _+5 more__

---
_Generated 2026-08-24 08:57 UTC_