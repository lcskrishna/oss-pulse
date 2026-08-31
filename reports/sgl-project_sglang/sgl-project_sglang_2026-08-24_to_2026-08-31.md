# sgl-project/sglang — Weekly Change Report
**Period:** 2026-08-24 → 2026-08-31  |  **Total commits:** 453

## ✨ New Features This Week

- **2026-08-31** [#37159](https://github.com/sgl-project/sglang/pull/37159) — [Kernel] Add GB300 Triton MoE configs for GLM-4.5 FP8 (#37159)
- **2026-08-31** [#37214](https://github.com/sgl-project/sglang/pull/37214) — test: re-enable DSV4-Flash W8A8 8p nightly perf cases (#37214)
- **2026-08-31** [#36871](https://github.com/sgl-project/sglang/pull/36871) — [AMD] support gfx1250 on ROCM 10 (#36871)
- **2026-08-31** [#34613](https://github.com/sgl-project/sglang/pull/34613) — feat(unified-memory): read unified pool from attention backends fa3/flashinfer/trtllm_mha/flashmla (#34613)
- **2026-08-31** [#36985](https://github.com/sgl-project/sglang/pull/36985) — test: re-enable FlashInfer per-token NVFP4 coverage (#36985)
- **2026-08-31** [#36248](https://github.com/sgl-project/sglang/pull/36248) — [PP] Support prefill CUDA graph proxy tensors (#36248)
- **2026-08-31** [#37151](https://github.com/sgl-project/sglang/pull/37151) — [Unified Cache Linker][3/N]: Add backend-independent linker core (#37151)
- **2026-08-31** [#36991](https://github.com/sgl-project/sglang/pull/36991) — [diffusion] feat: add exact component precision overrides (#36991)
- **2026-08-31** [#31041](https://github.com/sgl-project/sglang/pull/31041) — [Spec] Add LFM2 and LFM2-MoE DSpark speculative decoding support (#31041)
- **2026-08-31** [#35877](https://github.com/sgl-project/sglang/pull/35877) — [Intel GPU] Add rust support to XPU docker images (#35877)
- _…and 101 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-31** [`0674be736c`](https://github.com/sgl-project/sglang/commit/0674be736c) [#37225](https://github.com/sgl-project/sglang/pull/37225) — [AMD] build gfx1250 release image from main (#37225)
- **2026-08-31** [`3865efc9f7`](https://github.com/sgl-project/sglang/commit/3865efc9f7) [#36871](https://github.com/sgl-project/sglang/pull/36871) — [AMD] support gfx1250 on ROCM 10 (#36871)
- **2026-08-31** [`8bb776dc48`](https://github.com/sgl-project/sglang/commit/8bb776dc48) [#34613](https://github.com/sgl-project/sglang/pull/34613) — feat(unified-memory): read unified pool from attention backends fa3/flashinfer/trtllm_mha/flashmla (#34613)
- **2026-08-31** [`3a6ed55999`](https://github.com/sgl-project/sglang/commit/3a6ed55999) [#37194](https://github.com/sgl-project/sglang/pull/37194) — [Fix] Shut hicache test servers down gracefully before SIGKILL (#37194)
- **2026-08-31** [`5972211977`](https://github.com/sgl-project/sglang/commit/5972211977) [#37132](https://github.com/sgl-project/sglang/pull/37132) — [AMD] Fix the QuickReduce bf16 cast failing to build for CDNA (#37132)
- **2026-08-31** [`7700602278`](https://github.com/sgl-project/sglang/commit/7700602278) [#35281](https://github.com/sgl-project/sglang/pull/35281) — [PD] Align defensive protocol behavior across Mooncake, NIXL, and Mori (#35281)
- **2026-08-30** [`4bb8de34cc`](https://github.com/sgl-project/sglang/commit/4bb8de34cc) [#37108](https://github.com/sgl-project/sglang/pull/37108) — [mem_cache] Share one `ReqKvInfo` between a streaming session slot and its request (#37108)
- **2026-08-30** [`7399c2b558`](https://github.com/sgl-project/sglang/commit/7399c2b558) [#37092](https://github.com/sgl-project/sglang/pull/37092) — [AMD] Update v4 amd cookbook 0830 (#37092)
- **2026-08-30** [`5ec959965b`](https://github.com/sgl-project/sglang/commit/5ec959965b) [#37085](https://github.com/sgl-project/sglang/pull/37085) — [mem_cache] Settle extend `kv_committed_len` inside `alloc_for_extend` (#37085)
- **2026-08-30** [`0438b16154`](https://github.com/sgl-project/sglang/commit/0438b16154) [#37078](https://github.com/sgl-project/sglang/pull/37078) — [mem_cache] Move `kv_committed_len` into `ReqKvInfo` (#37078)
- **2026-08-30** [`78fa921189`](https://github.com/sgl-project/sglang/commit/78fa921189) [#34484](https://github.com/sgl-project/sglang/pull/34484) — [ROCm] Fix QuickReduce fp16 saturation corrupting bf16 all-reduces (106M non-finite -> 0, +0.3%) (#34484)
- **2026-08-30** [`67bd163a48`](https://github.com/sgl-project/sglang/commit/67bd163a48) [#37083](https://github.com/sgl-project/sglang/pull/37083) — [AMD] Cherry-pick dsv4 fp4 kv-cache fix aiter commit (#37083)
- **2026-08-30** [`fbecd75c83`](https://github.com/sgl-project/sglang/commit/fbecd75c83) [#36515](https://github.com/sgl-project/sglang/pull/36515) — [AMD] fix: do not emit a shared-expert marker twice on the per-rank slot path (#36515)
- **2026-08-29** [`24a3a63e6b`](https://github.com/sgl-project/sglang/commit/24a3a63e6b) [#36958](https://github.com/sgl-project/sglang/pull/36958) — [misc] Keep `req.kv` non-optional and key KV ownership on `req_pool_idx` (#36958)
- **2026-08-29** [`7f2ee22b70`](https://github.com/sgl-project/sglang/commit/7f2ee22b70) [#36915](https://github.com/sgl-project/sglang/pull/36915) — [AMD] Fix eager metadata for AITER EAGLE draft extend (#36915)
- **2026-08-29** [`24c9251ac5`](https://github.com/sgl-project/sglang/commit/24c9251ac5) [#36714](https://github.com/sgl-project/sglang/pull/36714) — [AMD][Spec][PD] Enable the PD DSA fused-TopK seed remap on ROCm (#36714)
- **2026-08-29** [`3760296be8`](https://github.com/sgl-project/sglang/commit/3760296be8) [#35762](https://github.com/sgl-project/sglang/pull/35762) — [PD] Pack DCP1→DCP-N PD KV transfers into dest-contiguous RDMA blocks (#35762)
- **2026-08-29** [`89816a21a1`](https://github.com/sgl-project/sglang/commit/89816a21a1) [#36828](https://github.com/sgl-project/sglang/pull/36828) — [AMD] Update v4 amd cookbook 0828 (#36828)
- **2026-08-29** [`36afd70f9c`](https://github.com/sgl-project/sglang/commit/36afd70f9c) [#36852](https://github.com/sgl-project/sglang/pull/36852) — [ROCm][Bugfix] Use token-level KV indices in the aiter ASM context-prefill gather (#36852)
- **2026-08-29** [`4944e50e2c`](https://github.com/sgl-project/sglang/commit/4944e50e2c) [#33576](https://github.com/sgl-project/sglang/pull/33576) — [AMD] Add Work-Centric (Lean) Attention: a persistent-CTA decode kernel for long-context serving (#33576)
- **2026-08-28** [`f65b2b2b15`](https://github.com/sgl-project/sglang/commit/f65b2b2b15) [#36914](https://github.com/sgl-project/sglang/pull/36914) — [Fix] Lazy-import aiter in DSv4 paged_decode to unbreak CPU CI (#36914)
- **2026-08-28** [`2a96ebf648`](https://github.com/sgl-project/sglang/commit/2a96ebf648) [#36094](https://github.com/sgl-project/sglang/pull/36094) — [AMD][DSV4] perf: retune decode split-K heuristic for MI355X (#36094)
- **2026-08-28** [`c7879af887`](https://github.com/sgl-project/sglang/commit/c7879af887) [#36892](https://github.com/sgl-project/sglang/pull/36892) — [AMD] release rocm10 image for gfx1250 from amd_helios (#36892)
- **2026-08-28** [`9579bff860`](https://github.com/sgl-project/sglang/commit/9579bff860) [#36434](https://github.com/sgl-project/sglang/pull/36434) — [AMD] Add ROCm 10 (gfx942 / gfx950) release images (#36434)
- **2026-08-28** [`d3b972cbf0`](https://github.com/sgl-project/sglang/commit/d3b972cbf0) [#36379](https://github.com/sgl-project/sglang/pull/36379) — fix(lora): build the MoE LoRA align JIT kernel on ROCm (#36379)
- **2026-08-28** [`0c7d017dbb`](https://github.com/sgl-project/sglang/commit/0c7d017dbb) [#35341](https://github.com/sgl-project/sglang/pull/35341) — [AMD][Fix] Qwen3.5: make empty-batch guard tuple-aware on fused AR+quant path (#35341)
- **2026-08-28** [`2a7fb511c9`](https://github.com/sgl-project/sglang/commit/2a7fb511c9) [#36308](https://github.com/sgl-project/sglang/pull/36308) — [AMD][CI] Limit HiCache MGSM eval concurrency on ROCm (#36308)
- **2026-08-28** [`acc918b3ec`](https://github.com/sgl-project/sglang/commit/acc918b3ec) [#36758](https://github.com/sgl-project/sglang/pull/36758) — [AMD] Qwen3.5 ASM FMHA chunked-prefill context attention (#36758)
- **2026-08-28** [`9fc60a8afd`](https://github.com/sgl-project/sglang/commit/9fc60a8afd) [#29133](https://github.com/sgl-project/sglang/pull/29133) — [PD] Fix MORI-IO ABORT bootstrap message handling (#29133)
- **2026-08-28** [`baf09f3954`](https://github.com/sgl-project/sglang/commit/baf09f3954) [#36684](https://github.com/sgl-project/sglang/pull/36684) — [AMD] Enable deepseek-v4 topk_transform v2 kernel (#36684)
- **2026-08-28** [`cce0b53466`](https://github.com/sgl-project/sglang/commit/cce0b53466) [#35628](https://github.com/sgl-project/sglang/pull/35628) — [AMD] Increase gfx950 DSA model indexer topk_transform kernel occupancy (#35628)
- **2026-08-28** [`2b209711d8`](https://github.com/sgl-project/sglang/commit/2b209711d8) [#36119](https://github.com/sgl-project/sglang/pull/36119) — [AMD][DSV4] perf: MXFP8 MoRI dispatch to match the w4a8 MoE input format (#36119)
- **2026-08-28** [`aa0a0aa3c3`](https://github.com/sgl-project/sglang/commit/aa0a0aa3c3) [#36130](https://github.com/sgl-project/sglang/pull/36130) — [AMD][DSV4] perf: bound the MoRI receive buffer during decode (#36130)
- **2026-08-28** [`de2fb50120`](https://github.com/sgl-project/sglang/commit/de2fb50120) [#36356](https://github.com/sgl-project/sglang/pull/36356) — [AMD] Enable aiter mla asm path through padding attn heads for Kimi K3 (#36356)
- **2026-08-27** [`7cbe564829`](https://github.com/sgl-project/sglang/commit/7cbe564829) [#36529](https://github.com/sgl-project/sglang/pull/36529) — [Fix][XPU/ROCm/NPU] Defer sgl_kernel.quantization import in expert_pack (#36529)
- **2026-08-27** [`e283c9f8ea`](https://github.com/sgl-project/sglang/commit/e283c9f8ea) [#36736](https://github.com/sgl-project/sglang/pull/36736) — [AMD][CI] Merge the four MI35x DeepSeek-V3.2 nightly jobs into two to save runtime (#36736)
- **2026-08-27** [`8ad76415e2`](https://github.com/sgl-project/sglang/commit/8ad76415e2) [#36160](https://github.com/sgl-project/sglang/pull/36160) — [PD][mori] Align prefill transfer control plane for unified control plane (#36160)
- **2026-08-27** [`2ded8a6aea`](https://github.com/sgl-project/sglang/commit/2ded8a6aea) [#35611](https://github.com/sgl-project/sglang/pull/35611) — [AMD] Enable moe_a2a_backend=mori for DeepSeek-V4 prefill context parallelism (#35611)
- **2026-08-27** [`1a91c232ea`](https://github.com/sgl-project/sglang/commit/1a91c232ea) [#36636](https://github.com/sgl-project/sglang/pull/36636) — [AMD][CI] Add targeted Mori test labels (#36636)
- **2026-08-27** [`c967cd19b5`](https://github.com/sgl-project/sglang/commit/c967cd19b5) [#36330](https://github.com/sgl-project/sglang/pull/36330) — [AMD] Optimize Qwen3.5 MTP unified attention on gfx950 (#36330)
- **2026-08-27** [`0f7b5b8b2a`](https://github.com/sgl-project/sglang/commit/0f7b5b8b2a) [#36608](https://github.com/sgl-project/sglang/pull/36608) — [AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X (#36608)
- **2026-08-27** [`f775db03aa`](https://github.com/sgl-project/sglang/commit/f775db03aa) [#36541](https://github.com/sgl-project/sglang/pull/36541) — [AMD] Fix int32 seqused_k overflow in aiter draft-extend attention (#36541)
- **2026-08-27** [`cbfe54fba8`](https://github.com/sgl-project/sglang/commit/cbfe54fba8) [#34296](https://github.com/sgl-project/sglang/pull/34296) — [AMD] Use fast exponentials in C4 and C128 ROCm kernels (#34296)
- **2026-08-27** [`1c8f2b38cb`](https://github.com/sgl-project/sglang/commit/1c8f2b38cb) [#36396](https://github.com/sgl-project/sglang/pull/36396) — [AMD][CI] Add DeepSeek-V4-Flash FP8 accuracy coverage on MI30x (#36396)
- **2026-08-27** [`4f59a8dcfa`](https://github.com/sgl-project/sglang/commit/4f59a8dcfa) [#36309](https://github.com/sgl-project/sglang/pull/36309) — [AMD][Bugfix] Skip invalid fused MoE reduction for direct top-1 output (#36309)
- **2026-08-27** [`d2b3e9051d`](https://github.com/sgl-project/sglang/commit/d2b3e9051d) [#36307](https://github.com/sgl-project/sglang/pull/36307) — [AMD][CI] Stabilize PyTorch sampling backend test on ROCm (#36307)
- **2026-08-27** [`862f9ed3d8`](https://github.com/sgl-project/sglang/commit/862f9ed3d8) [#36343](https://github.com/sgl-project/sglang/pull/36343) — [AMD] Fall back to CPU tensor for decode retraction on ROCm (#36343)
- **2026-08-27** [`20621aa14b`](https://github.com/sgl-project/sglang/commit/20621aa14b) [#33561](https://github.com/sgl-project/sglang/pull/33561) — [Model] Support Ling-3.0-flash (BailingMoeV3)  (#33561)
- **2026-08-26** [`ec4bdbfa4a`](https://github.com/sgl-project/sglang/commit/ec4bdbfa4a) [#31626](https://github.com/sgl-project/sglang/pull/31626) — [Feature] Beam search support (#31626)
- **2026-08-26** [`5263568bcb`](https://github.com/sgl-project/sglang/commit/5263568bcb) [#36317](https://github.com/sgl-project/sglang/pull/36317) — [HiCache] Keep auxiliary load-back out of Full KV pending ownership (#36317)
- **2026-08-26** [`27c36368b6`](https://github.com/sgl-project/sglang/commit/27c36368b6) [#36275](https://github.com/sgl-project/sglang/pull/36275) — fix(moe): guard FP8 delegate activation params (#36275)
- **2026-08-26** [`5bcc978f2a`](https://github.com/sgl-project/sglang/commit/5bcc978f2a) [#36306](https://github.com/sgl-project/sglang/pull/36306) — [AMD][CI] Pass USE_PDL explicitly in the fused MoE gate (#36306)
- **2026-08-26** [`07a9de25b4`](https://github.com/sgl-project/sglang/commit/07a9de25b4) [#36296](https://github.com/sgl-project/sglang/pull/36296) — [AMD][CI] Fix shared-KV verify tests for multi-head GQA (#36296)
- **2026-08-26** [`586a50cd96`](https://github.com/sgl-project/sglang/commit/586a50cd96) [#36393](https://github.com/sgl-project/sglang/pull/36393) — [AMD][CI] Restore MiniMax-M2.5 4-GPU MI35x nightly job (#36393)
- **2026-08-25** [`f7a56494b1`](https://github.com/sgl-project/sglang/commit/f7a56494b1) [#36381](https://github.com/sgl-project/sglang/pull/36381) — Fix SWA ownership across grouped frees (#36381)
- **2026-08-25** [`6569125e3a`](https://github.com/sgl-project/sglang/commit/6569125e3a) [#36142](https://github.com/sgl-project/sglang/pull/36142) — [AMD][CI] Add MiniMax-M3-MXFP8 MI35x nightly perf benchmark (#36142)
- **2026-08-25** [`7ddf92d5f4`](https://github.com/sgl-project/sglang/commit/7ddf92d5f4) [#36029](https://github.com/sgl-project/sglang/pull/36029) — fix(disagg): refresh stale prefill bootstrap metadata (#36029)
- **2026-08-25** [`96a73c4e15`](https://github.com/sgl-project/sglang/commit/96a73c4e15) [#36290](https://github.com/sgl-project/sglang/pull/36290) — [AMD][CI] Adjust MI300 score API performance thresholds (#36290)
- **2026-08-25** [`6a81038317`](https://github.com/sgl-project/sglang/commit/6a81038317) [#33021](https://github.com/sgl-project/sglang/pull/33021) — [AMD] Drop redundant FP8 bpreshuffle scale transpose via fused AR kernel (#33021)
- **2026-08-25** [`a618d4c064`](https://github.com/sgl-project/sglang/commit/a618d4c064) [#36246](https://github.com/sgl-project/sglang/pull/36246) — [AMD] Add Kimi-K2.7-Code-MXFP4 to cookbook (#36246)
- **2026-08-25** [`3bc1c580c6`](https://github.com/sgl-project/sglang/commit/3bc1c580c6) [#35672](https://github.com/sgl-project/sglang/pull/35672) — [AMD] Enable draft_extend CUDA graph for HIP DSA backend (#35672)
- **2026-08-25** [`2e3934f4cb`](https://github.com/sgl-project/sglang/commit/2e3934f4cb) [#35630](https://github.com/sgl-project/sglang/pull/35630) — [AMD] Enable Mori-EP on kimi-k3 (#35630)
- **2026-08-25** [`d067622820`](https://github.com/sgl-project/sglang/commit/d067622820) [#35340](https://github.com/sgl-project/sglang/pull/35340) — [AMD][bugfix] Add moe_ep_size/moe_tp_size to the allreduce-fusion gate test stub (#35340)
- **2026-08-25** [`2d6c12e2fd`](https://github.com/sgl-project/sglang/commit/2d6c12e2fd) [#32926](https://github.com/sgl-project/sglang/pull/32926) — [AMD] Don't request the unused softmax LSE in the AITER diffusion backend (#32926)
- **2026-08-25** [`13d2ee8180`](https://github.com/sgl-project/sglang/commit/13d2ee8180) [#36139](https://github.com/sgl-project/sglang/pull/36139) — [AMD] Skip shared-KV verify test on ROCm 7.0 CI (#36139)
- **2026-08-25** [`9eee990ce1`](https://github.com/sgl-project/sglang/commit/9eee990ce1) [#36245](https://github.com/sgl-project/sglang/pull/36245) — [AMD] cookbook: add HiCache host-DRAM KV tier for Qwen3.5 MXFP4 on MI355X (#36245)
- **2026-08-24** [`24bce93c93`](https://github.com/sgl-project/sglang/commit/24bce93c93) [#36025](https://github.com/sgl-project/sglang/pull/36025) — [AMD][MORI] Deduplicate CP-replicated state transfers (#36025)
- **2026-08-24** [`0d5b5ae620`](https://github.com/sgl-project/sglang/commit/0d5b5ae620) [#35719](https://github.com/sgl-project/sglang/pull/35719) — [AMD] Fix Qwen3.5 MTP dropping fused shared-expert weights (#35719)
- **2026-08-24** [`0665740953`](https://github.com/sgl-project/sglang/commit/0665740953) [#32039](https://github.com/sgl-project/sglang/pull/32039) — [AMD][Fix] Route MoRI through the Qwen MoE all-to-all path (#32039)
- **2026-08-24** [`d8433868ce`](https://github.com/sgl-project/sglang/commit/d8433868ce) [#36171](https://github.com/sgl-project/sglang/pull/36171) — [AMD][CI] Temporarily bypass local-registry image pulls (#36171)
- **2026-08-24** [`7de80e566c`](https://github.com/sgl-project/sglang/commit/7de80e566c) [#35686](https://github.com/sgl-project/sglang/pull/35686) — [AMD][CI] Name the ROCm Image That Actually Ran in AMD Job Names (#35686)
- **2026-08-24** [`7bbd0ddeb5`](https://github.com/sgl-project/sglang/commit/7bbd0ddeb5) [#36124](https://github.com/sgl-project/sglang/pull/36124) — [AMD] Quark shared-experts gate: recognise a trailing MTP layer (#36124)
- **2026-08-24** [`666b08b4a5`](https://github.com/sgl-project/sglang/commit/666b08b4a5) [#34461](https://github.com/sgl-project/sglang/pull/34461) — [ROCm] Extend the gfx950 extend-attention tile to head_dim <= 128: -43% kernel, -14% TTFT, bit-identical (#34461)
- **2026-08-24** [`97b176e64c`](https://github.com/sgl-project/sglang/commit/97b176e64c) [#32597](https://github.com/sgl-project/sglang/pull/32597) — Support streaming session on NPU (#32597)
- **2026-08-24** [`20064623ab`](https://github.com/sgl-project/sglang/commit/20064623ab) [#35383](https://github.com/sgl-project/sglang/pull/35383) — [AMD][CI] Add the Qwen3.8 MXFP4 MI35x nightly (#35383)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-08-31 |
| [#37216](https://github.com/sgl-project/sglang/issues/37216) | [Bug] remote_instance weight loading fails with --pp-size 2 — Transfer | — | 2026-08-31 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-08-31 |
| [#36140](https://github.com/sgl-project/sglang/issues/36140) | [Bug] DFLASH speculative decoding is not supported under PD disaggrega | — | 2026-08-31 |
| [#33522](https://github.com/sgl-project/sglang/issues/33522) | [Roadmap]Fast Engine Recovery: Weight Cache Daemon | — | 2026-08-31 |
| [#37183](https://github.com/sgl-project/sglang/issues/37183) | AMD MI308X SGLang GLM-5.3-Flash ValueError: The checkpoint you are try | — | 2026-08-31 |
| [#37097](https://github.com/sgl-project/sglang/issues/37097) | [Bug] Pretokenized image requests can crash GLM MRoPE with a stale ret | — | 2026-08-31 |
| [#30760](https://github.com/sgl-project/sglang/issues/30760) | [Bug] HiCache prefetch all_reduce deadlock with TP=4, no PP — mismatch | — | 2026-08-31 |
| [#34510](https://github.com/sgl-project/sglang/issues/34510) | [Tracking] PD disaggregation shared-protocol unification | — | 2026-08-31 |
| [#29738](https://github.com/sgl-project/sglang/issues/29738) | [Bug] NameError: name 'deep_gemm' is not defined in tf32_hc_prenorm_ge | — | 2026-08-30 |
| [#37089](https://github.com/sgl-project/sglang/issues/37089) | [Bug] Qwen3.8-Flash-Next W4A16 on A100 TP4: Marlin MoE invalid thread  | — | 2026-08-30 |
| [#35785](https://github.com/sgl-project/sglang/issues/35785) | Triton version mismatch | — | 2026-08-30 |
| [#36830](https://github.com/sgl-project/sglang/issues/36830) | [Bug] GLM-5.3-Flash cannot use FP8 KV cache: `index_kpool > 1` exclude | — | 2026-08-30 |
| [#36807](https://github.com/sgl-project/sglang/issues/36807) | [Bug] fast_topk_v2 can silently return wrong top-k sets when a radix t | — | 2026-08-29 |
| [#37022](https://github.com/sgl-project/sglang/issues/37022) | [Bug] Prefill transfer failed with exception KVTransferError Decode in | — | 2026-08-29 |
| [#36938](https://github.com/sgl-project/sglang/issues/36938) | [Bug] Prefill input logprobs are served from the wrong request when a  | — | 2026-08-29 |
| [#36889](https://github.com/sgl-project/sglang/issues/36889) | [DFLASH] Mamba state cache silently caps effective concurrency on hybr | — | 2026-08-28 |
| [#36820](https://github.com/sgl-project/sglang/issues/36820) | [Feature] Sparse destination-aware MoE dispatch to skip inactive EP ra | — | 2026-08-28 |
| [#36796](https://github.com/sgl-project/sglang/issues/36796) | [Performance] Qwen4Exp decode on DGX Spark (SM121): QSA/PLE/GDN kernel | — | 2026-08-28 |
| [#36179](https://github.com/sgl-project/sglang/issues/36179) | [Bug] When using hicache to enable L2/L3 storage in DeepSeek V4, token | — | 2026-08-28 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 92 |
| Multimodal | 66 |
| MoE / Expert Parallel | 49 |
| Quantization | 47 |
| Prefill / Decode Disaggregation | 45 |
| KV Cache / Memory | 36 |
| Other | 21 |
| CI / Build | 18 |
| ROCm / AMD | 14 |
| Triton / Kernels | 13 |
| Scheduler / Batching | 13 |
| Models | 10 |
| Docs / Examples | 10 |
| Tensor / Data Parallel | 9 |
| Speculative Decoding | 4 |
| Structured Output | 3 |
| Serving / API | 2 |
| LoRA | 1 |

## Attention / FlashInfer  (92 commits)

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
- **2026-08-30** [`4bea51d885`](https://github.com/sgl-project/sglang/commit/4bea51d885) [#34602](https://github.com/sgl-project/sglang/pull/34602)
  feat(unified-memory): dense KV views for uniform-row MHA/SWA models (#34602)
  _Files: `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/kernels/ops/attention/metadata.py`, `python/sglang/kernels/ops/kvcache/__init__.py`, `python/sglang/kernels/ops/kvcache/cache_move.py` _+26 more__
- **2026-08-30** [`9a03bc2dc3`](https://github.com/sgl-project/sglang/commit/9a03bc2dc3) [#37148](https://github.com/sgl-project/sglang/pull/37148)
  [CI] Fix stale GPU capability test patches (#37148)
  _Files: `test/registered/attention/unittests/dsv4/test_deepseek_v4.py`, `test/registered/quant/test_fp8_utils.py`_
- **2026-08-30** [`fe694986a2`](https://github.com/sgl-project/sglang/commit/fe694986a2) [#37049](https://github.com/sgl-project/sglang/pull/37049)
  [diffusion] chore: make malformed component execution options fail-fast (#37049)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan3d.py` _+13 more__
- **2026-08-30** [`e635577431`](https://github.com/sgl-project/sglang/commit/e635577431) [#34446](https://github.com/sgl-project/sglang/pull/34446)
  [rotary] Fix the fused Qwen3.5 RoPE kernel discarding mrope height and width (#34446)
  _Files: `python/sglang/kernels/ops/attention/fused_qk_rmsnorm_rope_gate.py`, `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/models/qwen3_5.py`, `test/registered/kernels/ops/attention/test_fused_qk_rmsnorm_rope_gate.py` _+1 more__
- **2026-08-30** [`7f540274a7`](https://github.com/sgl-project/sglang/commit/7f540274a7) [#37073](https://github.com/sgl-project/sglang/pull/37073)
  Use Flashinfer 0.6.18 release for CUDA 13.4 package (#37073)
  _Files: `docker/Dockerfile.cu134`_
- **2026-08-30** [`f60bc73c58`](https://github.com/sgl-project/sglang/commit/f60bc73c58) [#33614](https://github.com/sgl-project/sglang/pull/33614)
  [Spec] Fix Dspark and Dflash state divergence across TP rank (#33614)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py` _+4 more__
- **2026-08-29** [`cdbfe90b4a`](https://github.com/sgl-project/sglang/commit/cdbfe90b4a) [#36798](https://github.com/sgl-project/sglang/pull/36798)
  [HiCache] Align chunked CUDA host registrations (#36798)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/pool_host/common.py`, `python/sglang/srt/mem_cache/pool_host/dsa.py` _+4 more__
- **2026-08-29** [`78eef34356`](https://github.com/sgl-project/sglang/commit/78eef34356) [#36170](https://github.com/sgl-project/sglang/pull/36170)
  [NPU] [BugFix] Fix discontinuous input for FIA operator in GLM4.7‑Flash (#36170)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-08-29** [`7f2ee22b70`](https://github.com/sgl-project/sglang/commit/7f2ee22b70) [#36915](https://github.com/sgl-project/sglang/pull/36915)
  [AMD] Fix eager metadata for AITER EAGLE draft extend (#36915)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-08-29** [`ec962fd12d`](https://github.com/sgl-project/sglang/commit/ec962fd12d) [#36963](https://github.com/sgl-project/sglang/pull/36963)
  [Fix] Fall back to the process-group broadcast for DSA topk when PyNCCL is absent (#36963)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-08-29** [`ca8cc101b8`](https://github.com/sgl-project/sglang/commit/ca8cc101b8) [#35021](https://github.com/sgl-project/sglang/pull/35021)
  [NPU] add causal conv1d for ascend kda backend (#35021)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_kda_backend.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-08-29** [`92b0d447b0`](https://github.com/sgl-project/sglang/commit/92b0d447b0) [#35434](https://github.com/sgl-project/sglang/pull/35434)
  [CPU] Fix wrongly causal-masked bidirectional attention (#35434)
  _Files: `python/sglang/kernels/aot/csrc/cpu/extend.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `test/registered/cpu/test_extend.py`_
- **2026-08-29** [`51c18d9aa8`](https://github.com/sgl-project/sglang/commit/51c18d9aa8) [#36476](https://github.com/sgl-project/sglang/pull/36476)
  [NPU] [DOC] update npu best practice (#36476)
  _Files: `docs/docs.json`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/deepseek_r1.mdx`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/deepseek_v3_2.mdx`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/deepseek_v4_flash.mdx` _+14 more__
- **2026-08-29** [`7276a30c45`](https://github.com/sgl-project/sglang/commit/7276a30c45) [#35453](https://github.com/sgl-project/sglang/pull/35453)
  [Fix] Support LSE on the RadixAttention extra-kwargs graph path (#35453)
  _Files: `python/sglang/srt/layers/radix_attention.py`, `test/registered/unit/layers/test_radix_attention.py`_
- **2026-08-29** [`a16872767f`](https://github.com/sgl-project/sglang/commit/a16872767f) [#36929](https://github.com/sgl-project/sglang/pull/36929)
  Update CUDA 13.4 image to flashinfer 0.6.18rc10, cutedsl 4.8. Fix sgl- wheel unpinning (#36929)
  _Files: `docker/Dockerfile.cu134`_
- **2026-08-29** [`36afd70f9c`](https://github.com/sgl-project/sglang/commit/36afd70f9c) [#36852](https://github.com/sgl-project/sglang/pull/36852)
  [ROCm][Bugfix] Use token-level KV indices in the aiter ASM context-prefill gather (#36852)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/attention/test_aiter_asm_prefill_gather.py`_
- **2026-08-29** [`4944e50e2c`](https://github.com/sgl-project/sglang/commit/4944e50e2c) [#33576](https://github.com/sgl-project/sglang/pull/33576)
  [AMD] Add Work-Centric (Lean) Attention: a persistent-CTA decode kernel for long-context serving (#33576)
  _Files: `benchmark/lean_kernel_sweep.py`, `python/sglang/kernels/ops/attention/decode_attention.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/triton_backend.py` _+2 more__
- **2026-08-28** [`db6f0a9d53`](https://github.com/sgl-project/sglang/commit/db6f0a9d53) [#36704](https://github.com/sgl-project/sglang/pull/36704)
  Refactor JIT kernel and expert-pack directory layout (#36704)
  _Files: `docs/docs/developer_guide/development_jit_kernel_guide.mdx`, `examples/runtime/deepseek_v4/benchmark_deepseek_5090.py`, `examples/runtime/kimi_k3/benchmark_kimi_k3_5090.py`, `python/sglang/kernels/jit/csrc/elementwise/add_constant.cuh` _+21 more__
- **2026-08-28** [`96a4dcdde8`](https://github.com/sgl-project/sglang/commit/96a4dcdde8) [#36887](https://github.com/sgl-project/sglang/pull/36887)
  [CI] Slim JIT kernel unit tests (#36887)
  _Files: `.github/workflows/pr-test-jit-kernel.yml`, `python/sglang/test/ci/ci_utils.py`, `python/sglang/test/ci/fork_test_worker.py`, `test/registered/kernels/ops/attention/test_rope.py` _+6 more__
- **2026-08-28** [`f65b2b2b15`](https://github.com/sgl-project/sglang/commit/f65b2b2b15) [#36914](https://github.com/sgl-project/sglang/pull/36914)
  [Fix] Lazy-import aiter in DSv4 paged_decode to unbreak CPU CI (#36914)
  _Files: `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/paged_decode.py`_
- **2026-08-28** [`2a96ebf648`](https://github.com/sgl-project/sglang/commit/2a96ebf648) [#36094](https://github.com/sgl-project/sglang/pull/36094)
  [AMD][DSV4] perf: retune decode split-K heuristic for MI355X (#36094)
  _Files: `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/paged_decode.py`, `test/registered/unit/layers/test_dsv4_kv_splits_heuristic.py`_
- **2026-08-28** [`43c63a22ff`](https://github.com/sgl-project/sglang/commit/43c63a22ff) [#36790](https://github.com/sgl-project/sglang/pull/36790)
  config: the derived parallel widths are computed from the leaves (#36790)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/runtime_context.py`, `test/registered/unit/test_runtime_context.py`_
- **2026-08-28** [`69a49fede8`](https://github.com/sgl-project/sglang/commit/69a49fede8) [#36603](https://github.com/sgl-project/sglang/pull/36603)
  fix(kimi-k3): preserve dense ModelSlim MLA weights (#36603)
  _Files: `python/sglang/srt/layers/quantization/expert_pack.py`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/expert_pack/test_kimi_k3_gguf.py`_
- **2026-08-28** [`acc918b3ec`](https://github.com/sgl-project/sglang/commit/acc918b3ec) [#36758](https://github.com/sgl-project/sglang/pull/36758)
  [AMD] Qwen3.5 ASM FMHA chunked-prefill context attention (#36758)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-08-28** [`baf09f3954`](https://github.com/sgl-project/sglang/commit/baf09f3954) [#36684](https://github.com/sgl-project/sglang/pull/36684)
  [AMD] Enable deepseek-v4 topk_transform v2 kernel (#36684)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/srt/server_args.py`, `test/registered/kernels/ops/attention/test_topk_v2.py`_
- **2026-08-28** [`43b5a57dbb`](https://github.com/sgl-project/sglang/commit/43b5a57dbb) [#36784](https://github.com/sgl-project/sglang/pull/36784)
  [Docs] Feature GLM-5.3-Flash in the popular-models banner (#36784)
  _Files: `docs/cookbook/autoregressive/intro.mdx`, `docs/src/snippets/configs/popular-models.jsx`_
- **2026-08-28** [`de2fb50120`](https://github.com/sgl-project/sglang/commit/de2fb50120) [#36356](https://github.com/sgl-project/sglang/pull/36356)
  [AMD] Enable aiter mla asm path through padding attn heads for Kimi K3 (#36356)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`_
- **2026-08-28** [`22f37d414b`](https://github.com/sgl-project/sglang/commit/22f37d414b) [#36672](https://github.com/sgl-project/sglang/pull/36672)
  [NPU] Chain PR test jobs and disable two DeepSeek-V4-Flash perf tests (#36672)
  _Files: `.github/workflows/pr-test-npu.yml`, `test/registered/npu/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in32k_out1k_50ms.py`, `test/registered/npu/performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in8k_out1k_50ms.py`_
- **2026-08-27** [`6ccfeb59bc`](https://github.com/sgl-project/sglang/commit/6ccfeb59bc) [#36740](https://github.com/sgl-project/sglang/pull/36740)
  cookbook: add a Speculative card to the GLM-5.3-Flash playground (#36740)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-08-27** [`d1f14431fd`](https://github.com/sgl-project/sglang/commit/d1f14431fd) [#36544](https://github.com/sgl-project/sglang/pull/36544)
  GLM-5.3-Flash cookbook: HiCache for LL, fusion-flag drop, EAGLE, default-cell numbers, DCP4 overlay (#36544)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-08-27** [`46a544e0a0`](https://github.com/sgl-project/sglang/commit/46a544e0a0) [#36719](https://github.com/sgl-project/sglang/pull/36719)
  [Docs] GLM-5.3-Flash: point at compute-mamba-ratio for the KDA/KV pool split (#36719)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`_
- **2026-08-27** [`11de5e2281`](https://github.com/sgl-project/sglang/commit/11de5e2281) [#36364](https://github.com/sgl-project/sglang/pull/36364)
  docs(cookbook): add GB10 (DGX Spark) MXFP4 cells for Ling-3.0-flash (#36364)
  _Files: `docs/src/snippets/configs/inclusionAI/ling-3.0-flash-benchmarks.jsx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash.jsx`_
- **2026-08-27** [`1af95ffded`](https://github.com/sgl-project/sglang/commit/1af95ffded) [#36571](https://github.com/sgl-project/sglang/pull/36571)
  [diffusion] Fuse Cosmos3 Nano T2I attention on Hopper (#36571)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/test/unit/test_cosmos3.py`_
- **2026-08-27** [`536f570e66`](https://github.com/sgl-project/sglang/commit/536f570e66) [#36611](https://github.com/sgl-project/sglang/pull/36611)
  docs(cookbook): fix Qwen3.8 Flash Next H200 MTP verify with BF16 SSM state (#36611)
  _Files: `docs/src/snippets/configs/Qwen/qwen3.8-flash-next.jsx`_
- **2026-08-27** [`636a6f7dba`](https://github.com/sgl-project/sglang/commit/636a6f7dba) [#36660](https://github.com/sgl-project/sglang/pull/36660)
  cookbook: fix GLM-5.3-Flash speculative flag, size Hopper memory, record GSM8K (#36660)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-08-27** [`a126a5fa31`](https://github.com/sgl-project/sglang/commit/a126a5fa31) [#36605](https://github.com/sgl-project/sglang/pull/36605)
  [CI] Graceful teardown for the radix_cache server fixtures (#36605)
  _Files: `test/registered/radix_cache/test_radix_attention.py`, `test/registered/radix_cache/test_radix_cache_hit.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_hicache_pp_kl.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_cp.py` _+7 more__
- **2026-08-27** [`c608f9bf75`](https://github.com/sgl-project/sglang/commit/c608f9bf75) [#36639](https://github.com/sgl-project/sglang/pull/36639)
  [CI] Fix Q8KV8 sparse prefill test fixture (#36639)
  _Files: `test/registered/kernels/ops/attention/test_q8kv8_sparse_prefill_backend.py`_
- **2026-08-27** [`b8a6adadfe`](https://github.com/sgl-project/sglang/commit/b8a6adadfe) [#35275](https://github.com/sgl-project/sglang/pull/35275)
  [Bug][Spec] fix startup crash and reduce CUDA graph memory usage for speculative adaptive (#35275)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_utils/__init__.py` _+3 more__
- **2026-08-27** [`c967cd19b5`](https://github.com/sgl-project/sglang/commit/c967cd19b5) [#36330](https://github.com/sgl-project/sglang/pull/36330)
  [AMD] Optimize Qwen3.5 MTP unified attention on gfx950 (#36330)
  _Files: `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/unified_attention_3d_mtp.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/amd/test_unified_attention_3d_mtp.py`_
- **2026-08-27** [`b294bd4bc7`](https://github.com/sgl-project/sglang/commit/b294bd4bc7) [#36413](https://github.com/sgl-project/sglang/pull/36413)
  [CPU][CI]: fix a few issues that cause XEON CI failures (#36413)
  _Files: `.github/workflows/pr-test-xeon.yml`, `test/registered/cpu/test_intel_amx_attention_backend_a.py`, `test/registered/cpu/test_intel_amx_attention_backend_b.py`_
- **2026-08-27** [`0f7b5b8b2a`](https://github.com/sgl-project/sglang/commit/0f7b5b8b2a) [#36608](https://github.com/sgl-project/sglang/pull/36608)
  [AMD] Add GLM-5.3-Flash recipes for MI300X, MI325X, and MI355X (#36608)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-08-27** [`f775db03aa`](https://github.com/sgl-project/sglang/commit/f775db03aa) [#36541](https://github.com/sgl-project/sglang/pull/36541)
  [AMD] Fix int32 seqused_k overflow in aiter draft-extend attention (#36541)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-08-27** [`4d5d506486`](https://github.com/sgl-project/sglang/commit/4d5d506486) [#35947](https://github.com/sgl-project/sglang/pull/35947)
  Publish gated DSV4 DFLASH-family target-prefill read completion (#35947)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+4 more__
- **2026-08-27** [`1c8f2b38cb`](https://github.com/sgl-project/sglang/commit/1c8f2b38cb) [#36396](https://github.com/sgl-project/sglang/pull/36396)
  [AMD][CI] Add DeepSeek-V4-Flash FP8 accuracy coverage on MI30x (#36396)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `test/registered/amd/test_deepseek_v4_flash_fp8_mi30x.py`, `test/run_suite.py`_
- **2026-08-27** [`07570202f0`](https://github.com/sgl-project/sglang/commit/07570202f0) [#35342](https://github.com/sgl-project/sglang/pull/35342)
  [VLM] route every multimodal processor through the worker pool's call site (#35342)
  _Files: `python/sglang/srt/multimodal/processors/clip.py`, `python/sglang/srt/multimodal/processors/cohere2_vision.py`, `python/sglang/srt/multimodal/processors/deepseek_ocr.py`, `python/sglang/srt/multimodal/processors/deepseek_vl_v2.py` _+30 more__
- **2026-08-27** [`9d07b9e227`](https://github.com/sgl-project/sglang/commit/9d07b9e227) [#33871](https://github.com/sgl-project/sglang/pull/33871)
  [Performance] Reduce idle DP work in breakable prefill CUDA graphs (#33871)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/radix_attention.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+3 more__
- **2026-08-27** [`058f99c561`](https://github.com/sgl-project/sglang/commit/058f99c561) [#36430](https://github.com/sgl-project/sglang/pull/36430)
  [CPU] Fix truncated KV prefix in intel_amx spec verify (#36430)
  _Files: `python/sglang/srt/layers/attention/intel_amx_backend.py`_
- **2026-08-26** [`ec4bdbfa4a`](https://github.com/sgl-project/sglang/commit/ec4bdbfa4a) [#31626](https://github.com/sgl-project/sglang/pull/31626)
  [Feature] Beam search support (#31626)
  _Files: `python/sglang/srt/beam_search/__init__.py`, `python/sglang/srt/beam_search/batch_tail.py`, `python/sglang/srt/beam_search/beam_group.py`, `python/sglang/srt/beam_search/coordinator.py` _+35 more__
- **2026-08-26** [`3ce243da3f`](https://github.com/sgl-project/sglang/commit/3ce243da3f) [#36233](https://github.com/sgl-project/sglang/pull/36233)
  [NVIDIA] Add CUDA 13.4 container for initial Rubin support (#36233)
  _Files: `.github/workflows/release-docker-cu134-nightly.yml`, `docker/Dockerfile.cu134`, `python/sglang/kernels/aot/CMakeLists.txt`, `python/sglang/kernels/aot/cmake/flashmla.cmake`_
- **2026-08-26** [`a8d716ce8d`](https://github.com/sgl-project/sglang/commit/a8d716ce8d) [#30859](https://github.com/sgl-project/sglang/pull/30859)
  dsa: widen the fp8 k-cache quant kernel's token_id to int64 (#30859)
  _Files: `python/sglang/kernels/ops/attention/dsa/dequant_k_cache.py`, `python/sglang/kernels/ops/attention/dsa/quant_k_cache.py`, `python/sglang/kernels/ops/attention/dsv4/dequant_k_cache.py`, `python/sglang/kernels/ops/attention/dsv4/quant_k_cache.py`_
- **2026-08-26** [`e27a7fac77`](https://github.com/sgl-project/sglang/commit/e27a7fac77) [#36519](https://github.com/sgl-project/sglang/pull/36519)
  GLM-5.3-Flash cookbook: default Blackwell recipes to FP8 KV + TRT-LLM DSA (#36519)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-08-26** [`f8cc1f9525`](https://github.com/sgl-project/sglang/commit/f8cc1f9525) [#36513](https://github.com/sgl-project/sglang/pull/36513)
  GLM-5.3-Flash cookbook: FP8 KV + TRT-LLM DSA benchmark card (#36513)
  _Files: `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-08-26** [`dfc40e0efe`](https://github.com/sgl-project/sglang/commit/dfc40e0efe) [#36440](https://github.com/sgl-project/sglang/pull/36440)
  Add GLM-5.3-Flash cookbook (#36440)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/docs.json`, `docs/src/snippets/_deployment.jsx` _+2 more__
- **2026-08-26** [`8eaffdf382`](https://github.com/sgl-project/sglang/commit/8eaffdf382) [#36499](https://github.com/sgl-project/sglang/pull/36499)
  docs: point the Qwen3.8-Flash-Next cookbook at model support PR #36497 (#36499)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`_
- **2026-08-26** [`c7b5e76fa9`](https://github.com/sgl-project/sglang/commit/c7b5e76fa9) [#36496](https://github.com/sgl-project/sglang/pull/36496)
  Add Qwen3.8-Flash-Next cookbook (#36496)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+3 more__
- **2026-08-26** [`58ecbba0bd`](https://github.com/sgl-project/sglang/commit/58ecbba0bd) [#35640](https://github.com/sgl-project/sglang/pull/35640)
  [Feature] Coordinate FullCG prefill across DP-attention ranks (#35640)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `python/sglang/srt/model_executor/forward_batch_info.py` _+11 more__
- **2026-08-26** [`a3c4936438`](https://github.com/sgl-project/sglang/commit/a3c4936438) [#35343](https://github.com/sgl-project/sglang/pull/35343)
  Sync FlashInfer autotune tactic choice across TP ranks (#35343)
  _Files: `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`, `test/registered/unit/model_executor/runner/test_flashinfer_autotune_sync.py`_
- **2026-08-26** [`3c9febc68b`](https://github.com/sgl-project/sglang/commit/3c9febc68b) [#36313](https://github.com/sgl-project/sglang/pull/36313)
  [Spec][DSA] Add --speculative-dsa-topk-backend (#36313)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/advanced_features/speculative_decoding.mdx`, `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` _+5 more__
- **2026-08-26** [`04c1036bb3`](https://github.com/sgl-project/sglang/commit/04c1036bb3) [#36003](https://github.com/sgl-project/sglang/pull/36003)
  [Kernel] Skip reserved writes in MLA KV cache (#36003)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/set_mla_kv_buffer.cuh`, `python/sglang/kernels/ops/kvcache/mla_buffer.py`, `python/sglang/kernels/ops/kvcache/set_mla_kv_buffer.py`, `test/registered/kernels/benchmark/kvcache/bench_set_mla_kv_buffer.py` _+2 more__
- **2026-08-26** [`2e4773aadd`](https://github.com/sgl-project/sglang/commit/2e4773aadd) [#35820](https://github.com/sgl-project/sglang/pull/35820)
  Fix NPUMHATokenToKVPool missing k_data_ptrs/v_data_ptrs (#35820)
  _Files: `python/sglang/srt/mem_cache/pool_host/mha.py`_
- **2026-08-26** [`cc3b61873f`](https://github.com/sgl-project/sglang/commit/cc3b61873f) [#35850](https://github.com/sgl-project/sglang/pull/35850)
  [Diffusion][minimax-h3] Restrict MiniMax-H3 SubBlock sparsity to video queries (#35850)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/router.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse_attn.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` _+9 more__
- **2026-08-26** [`303227951a`](https://github.com/sgl-project/sglang/commit/303227951a) [#35795](https://github.com/sgl-project/sglang/pull/35795)
  fix: use a bf16-relative tolerance in the DSA indexer K kernel test (#35795)
  _Files: `test/registered/kernels/ops/attention/test_dsv32_indexer_fusion.py`_
- **2026-08-26** [`07a9de25b4`](https://github.com/sgl-project/sglang/commit/07a9de25b4) [#36296](https://github.com/sgl-project/sglang/pull/36296)
  [AMD][CI] Fix shared-KV verify tests for multi-head GQA (#36296)
  _Files: `test/registered/attention/test_verify_shared_kv.py`_
- **2026-08-25** [`41e7612dee`](https://github.com/sgl-project/sglang/commit/41e7612dee) [#36186](https://github.com/sgl-project/sglang/pull/36186)
  [Model] Support Nemotron 3.5 Lightning speculative decoding (#36186)
  _Files: `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py` _+14 more__
- **2026-08-25** [`e9c9df6a52`](https://github.com/sgl-project/sglang/commit/e9c9df6a52) [#36219](https://github.com/sgl-project/sglang/pull/36219)
  [Performance] Tune FlashInfer EXTEND for DP prefill (#36219)
  _Files: `python/sglang/srt/model_executor/runner/base_runner.py`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py`, `test/registered/unit/model_executor/runner/test_flashinfer_autotune.py`_
- **2026-08-25** [`e2b50930b9`](https://github.com/sgl-project/sglang/commit/e2b50930b9) [#35676](https://github.com/sgl-project/sglang/pull/35676)
  [NPU] DeepSeek-V4 adapt sgl-kernel-npu ops (compressor/sparse-attn/sparse-attn-metadata) (#35676)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_memory_pool.py`, `python/sglang/srt/hardware_backend/npu/extra_ops_loader.py` _+3 more__
- **2026-08-25** [`61b67316d8`](https://github.com/sgl-project/sglang/commit/61b67316d8) [#33569](https://github.com/sgl-project/sglang/pull/33569)
  [NPU] [Diffusion] Support MiniMax H3 on Ascend NPU's (#33569)
  _Files: `docker/npu.Dockerfile`, `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/laser_attn.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py` _+17 more__
- **2026-08-25** [`b7f9fca26e`](https://github.com/sgl-project/sglang/commit/b7f9fca26e) [#36260](https://github.com/sgl-project/sglang/pull/36260)
  [CPU] Raise mem-fraction-static 0.1->0.2 in intel_amx backend a/b (#36260)
  _Files: `test/registered/cpu/test_intel_amx_attention_backend_a.py`, `test/registered/cpu/test_intel_amx_attention_backend_b.py`_
- **2026-08-25** [`2d6c12e2fd`](https://github.com/sgl-project/sglang/commit/2d6c12e2fd) [#32926](https://github.com/sgl-project/sglang/pull/32926)
  [AMD] Don't request the unused softmax LSE in the AITER diffusion backend (#32926)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py`_
- **2026-08-25** [`13d2ee8180`](https://github.com/sgl-project/sglang/commit/13d2ee8180) [#36139](https://github.com/sgl-project/sglang/pull/36139)
  [AMD] Skip shared-KV verify test on ROCm 7.0 CI (#36139)
  _Files: `test/registered/attention/test_verify_shared_kv.py`_
- **2026-08-25** [`998eeda0a5`](https://github.com/sgl-project/sglang/commit/998eeda0a5) [#36242](https://github.com/sgl-project/sglang/pull/36242)
  [CI] Register test_dflash_logits at its real cost (#36242)
  _Files: `test/registered/unit/spec/test_dflash_logits.py`_
- **2026-08-25** [`91e7e84ee5`](https://github.com/sgl-project/sglang/commit/91e7e84ee5) [#35116](https://github.com/sgl-project/sglang/pull/35116)
  [SM120] flash_mla: allocate the page-split buffer outside inference mode (#35116)
  _Files: `python/sglang/kernels/ops/attention/flash_mla_sm120.py`_
- **2026-08-24** [`effe0d14d2`](https://github.com/sgl-project/sglang/commit/effe0d14d2) [#36178](https://github.com/sgl-project/sglang/pull/36178)
  [Fix] Keep the MiniCPM-SALA config reads visible to the resolution ratchets (#36178)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/minicpm/backend.py`, `test/registered/unit/layers/test_minicpm_sparse_metadata.py`_
- **2026-08-24** [`6e2f87d589`](https://github.com/sgl-project/sglang/commit/6e2f87d589) [#36204](https://github.com/sgl-project/sglang/pull/36204)
  docs: mark Ling-3.0-flash DSPARK verified for all four quantizations on H200 (#36204)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash.mdx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash-benchmarks.jsx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash.jsx`_
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

## Multimodal  (66 commits)

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
- **2026-08-30** [`5ab97c4f44`](https://github.com/sgl-project/sglang/commit/5ab97c4f44) [#37090](https://github.com/sgl-project/sglang/pull/37090)
  [Diffusion] Cache Qwen-Image modulation across serial CFG branches (#37090)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/qwen_image.py`, `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-08-30** [`8c28cdd116`](https://github.com/sgl-project/sglang/commit/8c28cdd116) [#37075](https://github.com/sgl-project/sglang/pull/37075)
  [Diffusion][Kernel] Fuse Wan2.2 NVFP4 bias + GELU on Blackwell (#37075)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/bias_gelu.cuh`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/sites/nvfp4_bias_gelu_site.py`, `python/sglang/kernels/ops/elementwise/bias_gelu.py` _+6 more__
- **2026-08-30** [`84e56982b6`](https://github.com/sgl-project/sglang/commit/84e56982b6) [#37142](https://github.com/sgl-project/sglang/pull/37142)
  [Fix] Fix transformer loader fallback test fixture (#37142)
  _Files: `python/sglang/multimodal_gen/test/unit/test_transformer_loader_fallback.py`_
- **2026-08-30** [`e6a6492057`](https://github.com/sgl-project/sglang/commit/e6a6492057) [#37043](https://github.com/sgl-project/sglang/pull/37043)
  [vlm] fix: preserve per-request vit graph metadata for qwen-vl (#37043)
  _Files: `python/sglang/srt/models/qwen2_5_vl.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/vit_cuda_graph_runner.py`, `test/registered/unit/multimodal/test_vit_cuda_graph_metadata_cuda.py` _+1 more__
- **2026-08-30** [`e9a7157615`](https://github.com/sgl-project/sglang/commit/e9a7157615) [#35858](https://github.com/sgl-project/sglang/pull/35858)
  [diffusion] feat: allow cache-dit with dit layerwise offload (#35858)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/cache_dit.mdx`, `docs/docs/sglang-diffusion/caching-acceleration.mdx` _+5 more__
- **2026-08-30** [`a6e4021368`](https://github.com/sgl-project/sglang/commit/a6e4021368) [#36917](https://github.com/sgl-project/sglang/pull/36917)
  [diffusion] chore: reject incompatible transformer fallback (#36917)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/bridge_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/test/unit/test_image_encoder_loader.py` _+2 more__
- **2026-08-29** [`97781eb7f3`](https://github.com/sgl-project/sglang/commit/97781eb7f3) [#36905](https://github.com/sgl-project/sglang/pull/36905)
  [diffusion] fix: honor explicit offload in resident requirements (#36905)
- **2026-08-29** [`b24bd44556`](https://github.com/sgl-project/sglang/commit/b24bd44556) [#36832](https://github.com/sgl-project/sglang/pull/36832)
  [diffusion] feat: avoid direct GPU parameter copies (#36832)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/test/unit/test_fsdp_load.py`_
- **2026-08-29** [`0e1146d04f`](https://github.com/sgl-project/sglang/commit/0e1146d04f) [#34599](https://github.com/sgl-project/sglang/pull/34599)
  [diffusion] optimization: optimize Pi0.5 inference and bounded graph serving (#34599)
  _Files: `docs/cookbook/vla/OpenPI/Pi0.5.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/pi05.py`, `python/sglang/multimodal_gen/runtime/entrypoints/action/protocol.py`, `python/sglang/multimodal_gen/runtime/layers/linear.py` _+9 more__
- **2026-08-29** [`fa474b0441`](https://github.com/sgl-project/sglang/commit/fa474b0441) [#36863](https://github.com/sgl-project/sglang/pull/36863)
  [diffusion] fix: fix image encoder parallel folding proposal (#36863)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/encoder_parallel.mdx`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_encoder_world_folding.py`_
- **2026-08-29** [`f5319af1c9`](https://github.com/sgl-project/sglang/commit/f5319af1c9) [#36931](https://github.com/sgl-project/sglang/pull/36931)
  [diffusion] chore: honor explicit component offload (#36931)
  _Files: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-08-28** [`50bc1a3767`](https://github.com/sgl-project/sglang/commit/50bc1a3767) [#36641](https://github.com/sgl-project/sglang/pull/36641)
  [diffusion] Keep Cosmos3 Nano resident on 96 GB GPUs (#36641)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/multimodal_gen/test/unit/test_cosmos3.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-08-28** [`ca179b761b`](https://github.com/sgl-project/sglang/commit/ca179b761b) [#36912](https://github.com/sgl-project/sglang/pull/36912)
  Use kernel build node for cu134 image (#36912)
  _Files: `.github/workflows/release-docker-cu134-nightly.yml`_
- **2026-08-28** [`c7879af887`](https://github.com/sgl-project/sglang/commit/c7879af887) [#36892](https://github.com/sgl-project/sglang/pull/36892)
  [AMD] release rocm10 image for gfx1250 from amd_helios (#36892)
  _Files: `.github/workflows/release-docker-amd-rocm10.yml`_
- **2026-08-28** [`9579bff860`](https://github.com/sgl-project/sglang/commit/9579bff860) [#36434](https://github.com/sgl-project/sglang/pull/36434)
  [AMD] Add ROCm 10 (gfx942 / gfx950) release images (#36434)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd-extra.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/release-docker-amd-rocm10.yml` _+2 more__
- **2026-08-28** [`803b4fb31c`](https://github.com/sgl-project/sglang/commit/803b4fb31c) [#35613](https://github.com/sgl-project/sglang/pull/35613)
  [diffusion] refactor: scope model-specific API parameters (#35613)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `docs/cookbook/diffusion/LTX/LTX2.5.mdx`, `docs/cookbook/diffusion/LongCat/LongCat-Image.mdx`, `docs/cookbook/diffusion/intro.mdx` _+17 more__
- **2026-08-28** [`eebb99c049`](https://github.com/sgl-project/sglang/commit/eebb99c049) [#36521](https://github.com/sgl-project/sglang/pull/36521)
  [diffusion][kernel] avoid 4D scale-shift autotuning (#36521)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/modulate/scale_shift_triton.py`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md`, `test/registered/kernels/benchmark/diffusion/bench_scale_shift_4d.py` _+1 more__
- **2026-08-28** [`45424d8434`](https://github.com/sgl-project/sglang/commit/45424d8434) [#36504](https://github.com/sgl-project/sglang/pull/36504)
  [diffusion][kernel] support transposed residual-gate add (#36504)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/residual_gate_add.cuh`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/modulate/residual_gate_add_jit.py`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md` _+2 more__
- **2026-08-28** [`7088f21922`](https://github.com/sgl-project/sglang/commit/7088f21922) [#36658](https://github.com/sgl-project/sglang/pull/36658)
  [diffusion] fix: make tail_attn_meta cuda-graph capturable (#36658)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/sp_shard_utils.py`, `python/sglang/multimodal_gen/test/unit/test_sp_shard.py`_
- **2026-08-28** [`ad5a105a4a`](https://github.com/sgl-project/sglang/commit/ad5a105a4a) [#36726](https://github.com/sgl-project/sglang/pull/36726)
  [Diffusion] Fix the five unit tests failing on main (#36726)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/sana_wm_components.py`, `python/sglang/multimodal_gen/runtime/realtime/control_signals.py`, `python/sglang/multimodal_gen/runtime/realtime/states/camera_control.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py` _+3 more__
- **2026-08-28** [`96b31770f9`](https://github.com/sgl-project/sglang/commit/96b31770f9) [#36502](https://github.com/sgl-project/sglang/pull/36502)
  [diffusion] fuse Helios paired transposed RoPE (#36502)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/helios_qk_rope.cuh`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/helios_qk_rope_jit.py` _+4 more__
- **2026-08-27** [`a7e3f590ca`](https://github.com/sgl-project/sglang/commit/a7e3f590ca) [#36577](https://github.com/sgl-project/sglang/pull/36577)
  [Diffusion] Fuse LongCat residual gate updates (#36577)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md`, `python/sglang/multimodal_gen/runtime/models/dits/longcat_image.py`_
- **2026-08-27** [`e061dd1b47`](https://github.com/sgl-project/sglang/commit/e061dd1b47) [#36592](https://github.com/sgl-project/sglang/pull/36592)
  [Diffusion][Kernel] Fuse Wan FFN GELU epilogue (#36592)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-performance/SKILL.md`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`, `python/sglang/multimodal_gen/test/unit/test_wan_gelu_mlp.py`_
- **2026-08-27** [`db4125bb56`](https://github.com/sgl-project/sglang/commit/db4125bb56) [#36553](https://github.com/sgl-project/sglang/pull/36553)
  [diffusion] Accept mesh benchmark artifacts (#36553)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/scripts/bench_diffusion_denoise.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_benchmark_skill.py`_
- **2026-08-27** [`d42fa5e10a`](https://github.com/sgl-project/sglang/commit/d42fa5e10a) [#36485](https://github.com/sgl-project/sglang/pull/36485)
  [diffusion] align video BCG warmup frame count (#36485)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/scripts/bench_diffusion_denoise.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py` _+4 more__
- **2026-08-27** [`c2c3320cf0`](https://github.com/sgl-project/sglang/commit/c2c3320cf0) [#35349](https://github.com/sgl-project/sglang/pull/35349)
  [VLM] feat: size the multimodal preprocessing pool by where preprocessing runs (#35349)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/ernie45_vl.py`, `python/sglang/srt/multimodal/processors/executor.py`, `python/sglang/srt/multimodal/processors/midashenglm.py` _+5 more__
- **2026-08-27** [`72bf8c4d53`](https://github.com/sgl-project/sglang/commit/72bf8c4d53) [#36100](https://github.com/sgl-project/sglang/pull/36100)
  [ci] xpu: trigger pr-test-xpu on multimodal_gen changes (#36100)
  _Files: `.github/workflows/pr-test-xpu.yml`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/xpu_b60.json` _+1 more__
- **2026-08-27** [`02dfd37826`](https://github.com/sgl-project/sglang/commit/02dfd37826) [#36602](https://github.com/sgl-project/sglang/pull/36602)
  [CI] Remove GLM-4.1V-9B-Thinking from nightly VLM MMMU eval (#36602)
  _Files: `test/registered/eval/test_vlms_mmmu_eval.py`_
- **2026-08-26** [`924aeee59c`](https://github.com/sgl-project/sglang/commit/924aeee59c) [#36301](https://github.com/sgl-project/sglang/pull/36301)
  [diffusion] feat: support batching for cosmos3 action generation (#36301)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/action/cosmos3.py`, `python/sglang/multimodal_gen/runtime/entrypoints/action/protocol.py`, `python/sglang/multimodal_gen/runtime/entrypoints/utils.py` _+3 more__
- **2026-08-26** [`702de26310`](https://github.com/sgl-project/sglang/commit/702de26310) [#36463](https://github.com/sgl-project/sglang/pull/36463)
  [diffusion] make benchmark caches seedable and cover missing native families (#36463)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/scripts/bench_diffusion_denoise.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_benchmark_skill.py`_
- **2026-08-26** [`170da72c13`](https://github.com/sgl-project/sglang/commit/170da72c13) [#36322](https://github.com/sgl-project/sglang/pull/36322)
  [diffusion] perf: fuse tanh-GELU into the LongCat-Image DiT FFN up-proj (#36322)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/longcat_image.py`_
- **2026-08-26** [`c3c529c28e`](https://github.com/sgl-project/sglang/commit/c3c529c28e) [#36412](https://github.com/sgl-project/sglang/pull/36412)
  [diffusion] docs: distinguish MiniMax H3 checkpoint variants (#36412)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`_
- **2026-08-26** [`3ce4f957eb`](https://github.com/sgl-project/sglang/commit/3ce4f957eb) [#36398](https://github.com/sgl-project/sglang/pull/36398)
  [diffusion] fix: fix MiniMax-H3 dp_size>1 deadlock and cross-request audio determinism (#36398)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/reference_encoding.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/replica_broadcast.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_media.py`_
- **2026-08-26** [`d7baad0116`](https://github.com/sgl-project/sglang/commit/d7baad0116) [#36375](https://github.com/sgl-project/sglang/pull/36375)
  [diffusion] Keep the Cosmos3 Super DiT resident on high-memory GPUs (#36375)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-performance/SKILL.md`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-08-26** [`fa3ac61661`](https://github.com/sgl-project/sglang/commit/fa3ac61661) [#36327](https://github.com/sgl-project/sglang/pull/36327)
  [Diffusion] Bound reusable Ulysses A2A staging buffers across shapes (#36327)
  _Files: `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/test/unit/test_usp_packed_qkv_a2a.py`_
- **2026-08-26** [`4b2c182d3f`](https://github.com/sgl-project/sglang/commit/4b2c182d3f) [#36249](https://github.com/sgl-project/sglang/pull/36249)
  [diffusion] feat: support out-of-tree torch.compile backends (#36249)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/runtime/platforms/interface.py`, `python/sglang/multimodal_gen/runtime/utils/torch_compile.py`, `python/sglang/multimodal_gen/test/unit/test_regional_torch_compile.py`_
- **2026-08-26** [`223dfce917`](https://github.com/sgl-project/sglang/commit/223dfce917) [#36295](https://github.com/sgl-project/sglang/pull/36295)
  fix: bound CUDA memory for fast image preprocessing (#36295)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `test/registered/unit/multimodal/test_processor_device_selection.py`_
- **2026-08-25** [`c3947eeada`](https://github.com/sgl-project/sglang/commit/c3947eeada) [#36169](https://github.com/sgl-project/sglang/pull/36169)
  [diffusion] docs: desktop-safe 24 GB recipe and the DGX Spark tier (#36169)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-h3.jsx`_
- **2026-08-25** [`8f096b853a`](https://github.com/sgl-project/sglang/commit/8f096b853a) [#33859](https://github.com/sgl-project/sglang/pull/33859)
  [diffusion] fix: crop GLM-Image output to requested size (#33859)
  _Files: `python/sglang/multimodal_gen/configs/sample/glmimage.py`, `python/sglang/multimodal_gen/runtime/entrypoints/diffusion_generator.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/image_api.py`, `python/sglang/multimodal_gen/runtime/pipelines/glm_image.py` _+5 more__
- **2026-08-25** [`284ed9d1d3`](https://github.com/sgl-project/sglang/commit/284ed9d1d3) [#35829](https://github.com/sgl-project/sglang/pull/35829)
  [diffusion] feat: support LongCat-Image-Edit and LongCat-Image-Edit-Turbo (#35829)
  _Files: `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/longcat_image.py`, `python/sglang/multimodal_gen/configs/sample/longcat_image.py`, `python/sglang/multimodal_gen/registry.py` _+8 more__
- **2026-08-25** [`5ffdb02d0c`](https://github.com/sgl-project/sglang/commit/5ffdb02d0c) [#36241](https://github.com/sgl-project/sglang/pull/36241)
  [CI] Cut repeated tokenizer loads, serial subprocesses and a double scan (#36241)
  _Files: `test/registered/bench_fn/test_benchmark_datasets_api.py`, `test/registered/kernels/ops/diffusion/test_import_surface.py`, `test/registered/unit/function_call/test_function_call_parser.py`_
- **2026-08-24** [`b4bd5f91ee`](https://github.com/sgl-project/sglang/commit/b4bd5f91ee) [#36175](https://github.com/sgl-project/sglang/pull/36175)
  [diffusion] Fix test_model_fast_paths import after sana_ln_modulate rename (#36175)
  _Files: `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-08-24** [`d8433868ce`](https://github.com/sgl-project/sglang/commit/d8433868ce) [#36171](https://github.com/sgl-project/sglang/pull/36171)
  [AMD][CI] Temporarily bypass local-registry image pulls (#36171)
  _Files: `scripts/ci/amd/amd_ci_start_container.sh`, `scripts/ci/amd/amd_ci_start_container_disagg.sh`_
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

## MoE / Expert Parallel  (49 commits)

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
- **2026-08-30** [`8a87079dbb`](https://github.com/sgl-project/sglang/commit/8a87079dbb) [#35883](https://github.com/sgl-project/sglang/pull/35883)
  Fix stale GLM MoE routing after runtime weight updates (#35883)
  _Files: `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/utils/weight_checker.py`, `test/registered/rl/test_weight_checker_e2e.py` _+2 more__
- **2026-08-30** [`e51a3ae65e`](https://github.com/sgl-project/sglang/commit/e51a3ae65e) [#37087](https://github.com/sgl-project/sglang/pull/37087)
  [Config] Round 5.2: the per-model declarations get their own modules (#37087)
  _Files: `python/sglang/srt/arg_groups/model_override_base.py`, `python/sglang/srt/arg_groups/model_overrides/__init__.py`, `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py`, `python/sglang/srt/arg_groups/model_overrides/deepseek_v4.py` _+40 more__
- **2026-08-30** [`ed39568e79`](https://github.com/sgl-project/sglang/commit/ed39568e79) [#32665](https://github.com/sgl-project/sglang/pull/32665)
  [MoE] Add extension points for custom runner backends (#32665)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/__init__.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py` _+8 more__
- **2026-08-30** [`fbecd75c83`](https://github.com/sgl-project/sglang/commit/fbecd75c83) [#36515](https://github.com/sgl-project/sglang/pull/36515)
  [AMD] fix: do not emit a shared-expert marker twice on the per-rank slot path (#36515)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-08-29** [`00fbb6e8ac`](https://github.com/sgl-project/sglang/commit/00fbb6e8ac) [#35760](https://github.com/sgl-project/sglang/pull/35760)
  [Perf] Tune the W4AFP8 DeepEP low-latency requant launch geometry (#35760)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`, `python/sglang/srt/layers/quantization/w4afp8.py`, `test/registered/kernels/benchmark/moe/bench_fp8_per_token_to_per_tensor_quant.py` _+2 more__
- **2026-08-29** [`09ecb9aaaa`](https://github.com/sgl-project/sglang/commit/09ecb9aaaa) [#36768](https://github.com/sgl-project/sglang/pull/36768)
  :memo: [NPU] Use vendor-neutral wording in quantization comments (#36768)
  _Files: `python/sglang/multimodal_gen/runtime/layers/quantization/modelslim_mxfp4_scheme.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelslim_mxfp8_scheme.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/mxfp4_npu.py`, `python/sglang/srt/hardware_backend/npu/moe/init_routing.py` _+4 more__
- **2026-08-29** [`1a3e152f03`](https://github.com/sgl-project/sglang/commit/1a3e152f03) [#36973](https://github.com/sgl-project/sglang/pull/36973)
  config: six more runtime readers ask the bags (#36973)
  _Files: `python/sglang/srt/elastic_ep/expert_backup_client.py`, `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/layers/moe/kt_ep_wrapper.py`, `python/sglang/srt/managers/prefill_delayer.py` _+16 more__
- **2026-08-28** [`d12b313b93`](https://github.com/sgl-project/sglang/commit/d12b313b93) [#36921](https://github.com/sgl-project/sglang/pull/36921)
  fix: KT's last MoE layer stops deferring experts again (#36921)
  _Files: `python/sglang/srt/layers/moe/kt_ep_wrapper.py`_
- **2026-08-28** [`4d78d59e51`](https://github.com/sgl-project/sglang/commit/4d78d59e51) [#29718](https://github.com/sgl-project/sglang/pull/29718)
  [MoE] Make simulated expert routing support DP>1, and fuse into one triton kernel (#29718)
  _Files: `python/sglang/srt/layers/moe/__init__.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/moe/utils.py`, `test/manual/layers/moe/test_simulate_balanced_routing.py`_
- **2026-08-28** [`3254f9b47c`](https://github.com/sgl-project/sglang/commit/3254f9b47c) [#36657](https://github.com/sgl-project/sglang/pull/36657)
  [Blackwell] Reserve SMs for DeepGEMM MegaMoE grid barriers (#36657)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/models/kimi_k3.py`_
- **2026-08-28** [`74df026877`](https://github.com/sgl-project/sglang/commit/74df026877) [#35677](https://github.com/sgl-project/sglang/pull/35677)
  fix(cpu): skip GPU JIT MoE top-k on CPU (#35677)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-08-28** [`1e6d041f78`](https://github.com/sgl-project/sglang/commit/1e6d041f78) [#34690](https://github.com/sgl-project/sglang/pull/34690)
  [BugFix][VLM] keep Qwen3-VL MoE inference deepstack order (#34690)
  _Files: `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/models/qwen3_vl_moe.py`, `test/registered/vlm/test_vision_openai_server_a.py`_
- **2026-08-28** [`d3b972cbf0`](https://github.com/sgl-project/sglang/commit/d3b972cbf0) [#36379](https://github.com/sgl-project/sglang/pull/36379)
  fix(lora): build the MoE LoRA align JIT kernel on ROCm (#36379)
  _Files: `python/sglang/kernels/jit/csrc/lora/moe_lora_align_kernel.cu`, `test/registered/kernels/ops/moe/test_moe_lora_align_block_size.py`_
- **2026-08-28** [`0665102ce5`](https://github.com/sgl-project/sglang/commit/0665102ce5) [#36626](https://github.com/sgl-project/sglang/pull/36626)
  [Fix] Resolve tool argument types through top-level anyOf/oneOf/allOf (#36626)
  _Files: `python/sglang/srt/function_call/dots_detector.py`, `python/sglang/srt/function_call/glm47_moe_detector.py`, `python/sglang/srt/function_call/glm4_moe_detector.py`, `python/sglang/srt/function_call/hunyuan_detector.py` _+12 more__
- **2026-08-28** [`2b209711d8`](https://github.com/sgl-project/sglang/commit/2b209711d8) [#36119](https://github.com/sgl-project/sglang/pull/36119)
  [AMD][DSV4] perf: MXFP8 MoRI dispatch to match the w4a8 MoE input format (#36119)
  _Files: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `test/registered/unit/layers/test_moriep_mxfp8_dispatch.py`_
- **2026-08-28** [`aa0a0aa3c3`](https://github.com/sgl-project/sglang/commit/aa0a0aa3c3) [#36130](https://github.com/sgl-project/sglang/pull/36130)
  [AMD][DSV4] perf: bound the MoRI receive buffer during decode (#36130)
  _Files: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/utils/common.py`_
- **2026-08-27** [`76217f6603`](https://github.com/sgl-project/sglang/commit/76217f6603) [#36747](https://github.com/sgl-project/sglang/pull/36747)
  Revert "[NPU] [bugfix] Fix import of ggml_moe_a8_vec and Fix NPU MLA HiCache backup accessing missing data_ptrs" (#36747)
  _Files: `python/sglang/srt/layers/quantization/mxfp4_flashinfer_trtllm_moe.py`, `python/sglang/srt/mem_cache/pool_host/mla.py`_
- **2026-08-27** [`5640e53cab`](https://github.com/sgl-project/sglang/commit/5640e53cab) [#36640](https://github.com/sgl-project/sglang/pull/36640)
  [NPU] [bugfix] Fix import of ggml_moe_a8_vec and Fix NPU MLA HiCache backup accessing missing data_ptrs (#36640)
  _Files: `python/sglang/srt/layers/quantization/mxfp4_flashinfer_trtllm_moe.py`, `python/sglang/srt/mem_cache/pool_host/mla.py`_
- **2026-08-27** [`dc10483592`](https://github.com/sgl-project/sglang/commit/dc10483592) [#35374](https://github.com/sgl-project/sglang/pull/35374)
  [Kernel] Add H200 MoE configs for Qwen3.5 and Qwen3.6 (#35374)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=256,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=256,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128]_down.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=256,N=512,device_name=NVIDIA_H200.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=256,N=512,device_name=NVIDIA_H200_down.json`_
- **2026-08-27** [`024a7a1031`](https://github.com/sgl-project/sglang/commit/024a7a1031) [#36542](https://github.com/sgl-project/sglang/pull/36542)
  [diffusion] Fix native LingBot-Video text encoding (#36542)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/qwen3vl.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/lingbot_video_moe/text_encoding.py`, `python/sglang/multimodal_gen/test/unit/test_lingbot_video_moe.py`, `python/sglang/multimodal_gen/test/unit/test_qwen3vl_vision.py`_
- **2026-08-27** [`ad911a5ec0`](https://github.com/sgl-project/sglang/commit/ad911a5ec0) [#36543](https://github.com/sgl-project/sglang/pull/36543)
  [kernel] Tune LingBot-Video MoE TMA configs for H100 (#36543)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=128,N=768,device_name=NVIDIA_H100_80GB_HBM3.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=128,N=768,device_name=NVIDIA_H100_80GB_HBM3_down.json`, `test/registered/unit/layers/moe/test_fused_moe_triton_config.py`_
- **2026-08-27** [`56fdfc3b26`](https://github.com/sgl-project/sglang/commit/56fdfc3b26) [#34492](https://github.com/sgl-project/sglang/pull/34492)
  XPU: remove SGLANG_USE_SGL_XPU flag (#34492)
  _Files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/fp8.py` _+15 more__
- **2026-08-27** [`2ded8a6aea`](https://github.com/sgl-project/sglang/commit/2ded8a6aea) [#35611](https://github.com/sgl-project/sglang/pull/35611)
  [AMD] Enable moe_a2a_backend=mori for DeepSeek-V4 prefill context parallelism (#35611)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-08-27** [`adcf73d7f7`](https://github.com/sgl-project/sglang/commit/adcf73d7f7) [#36198](https://github.com/sgl-project/sglang/pull/36198)
  [Weight Cache] Enhance test and support EPLB (#36198)
  _Files: `python/sglang/srt/server_args.py`, `python/sglang/srt/weight_cache/daemon.py`, `test/registered/model_loading/test_weight_cache_daemon.py`, `test/registered/unit/model_loader/test_weight_cache_protocol.py` _+1 more__
- **2026-08-27** [`a3ae667d67`](https://github.com/sgl-project/sglang/commit/a3ae667d67) [#35634](https://github.com/sgl-project/sglang/pull/35634)
  [Feature] Add DeepEPv2 (ElasticBuffer) MoE A2A backend  (#35634)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` _+16 more__
- **2026-08-27** [`5adc2880f9`](https://github.com/sgl-project/sglang/commit/5adc2880f9) [#35222](https://github.com/sgl-project/sglang/pull/35222)
  [CPU] Enable ERNIE models on CPU (#35222)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/ernie4.py`_
- **2026-08-27** [`4f59a8dcfa`](https://github.com/sgl-project/sglang/commit/4f59a8dcfa) [#36309](https://github.com/sgl-project/sglang/pull/36309)
  [AMD][Bugfix] Skip invalid fused MoE reduction for direct top-1 output (#36309)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`_
- **2026-08-27** [`15688fea7d`](https://github.com/sgl-project/sglang/commit/15688fea7d) [#36584](https://github.com/sgl-project/sglang/pull/36584)
  Fix BailingMoeV3 reading enable_dp_lm_head off live topology instead of config (#36584)
  _Files: `python/sglang/srt/models/bailing_moe_v3.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`_
- **2026-08-27** [`20621aa14b`](https://github.com/sgl-project/sglang/commit/20621aa14b) [#33561](https://github.com/sgl-project/sglang/pull/33561)
  [Model] Support Ling-3.0-flash (BailingMoeV3)  (#33561)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce.cuh`, `python/sglang/kernels/ops/attention/fla/fused_kda_conv_recurrent_verify.py` _+72 more__
- **2026-08-26** [`2935bb8e79`](https://github.com/sgl-project/sglang/commit/2935bb8e79) [#36456](https://github.com/sgl-project/sglang/pull/36456)
  Fix OOB read in mxfp4 MoE weight scales on Hopper (#36456)
  _Files: `python/sglang/srt/layers/quantization/mxfp4.py`_
- **2026-08-26** [`413df1f8db`](https://github.com/sgl-project/sglang/commit/413df1f8db) [#36255](https://github.com/sgl-project/sglang/pull/36255)
  config: ServerArgs holds the raw input (#36255)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `examples/runtime/engine/save_remote_state.py`, `examples/runtime/engine/save_sharded_state.py`, `examples/runtime/token_in_token_out/token_in_token_out_vlm_engine.py` _+30 more__
- **2026-08-26** [`27c36368b6`](https://github.com/sgl-project/sglang/commit/27c36368b6) [#36275](https://github.com/sgl-project/sglang/pull/36275)
  fix(moe): guard FP8 delegate activation params (#36275)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `test/registered/unit/layers/quantization/test_fp8_moe_runner_ownership.py`_
- **2026-08-26** [`5bcc978f2a`](https://github.com/sgl-project/sglang/commit/5bcc978f2a) [#36306](https://github.com/sgl-project/sglang/pull/36306)
  [AMD][CI] Pass USE_PDL explicitly in the fused MoE gate (#36306)
  _Files: `python/sglang/kernels/ops/elementwise/elementwise.py`_
- **2026-08-26** [`2d8484740d`](https://github.com/sgl-project/sglang/commit/2d8484740d) [#35314](https://github.com/sgl-project/sglang/pull/35314)
  Support deepseek v4 and kimi k3 on ssd (#35314)
  _Files: `examples/runtime/deepseek_v4/benchmark_deepseek_5090.py`, `examples/runtime/kimi_k3/benchmark_kimi_k3_5090.py`, `python/sglang/kernels/jit/csrc/moe/expert_pack_mxfp4.cu`, `python/sglang/kernels/jit/csrc/ngram_corpus/result.h` _+42 more__
- **2026-08-25** [`4b4bf3d2a5`](https://github.com/sgl-project/sglang/commit/4b4bf3d2a5) [#35505](https://github.com/sgl-project/sglang/pull/35505)
  [Deepseek-V4] Enable shared-experts fusion on the flashinfer_mxfp4 (trtllm-gen) MoE path (#35505)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/models/test_deepseek_v4_mxfp4_shared_expert_requant.py`_
- **2026-08-25** [`46d9427b91`](https://github.com/sgl-project/sglang/commit/46d9427b91) [#36097](https://github.com/sgl-project/sglang/pull/36097)
  Fix MXFP8 MoE weight sizing for non-gated models (#36097)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `test/registered/unit/layers/quantization/test_fp8_moe_weight_gating.py`_
- **2026-08-25** [`a1f9508dd4`](https://github.com/sgl-project/sglang/commit/a1f9508dd4) [#35188](https://github.com/sgl-project/sglang/pull/35188)
  [Bugfix] Fix int32 destination offset overflow in CUTLASS MoE pre-reorder (#35188)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`_
- **2026-08-25** [`d067622820`](https://github.com/sgl-project/sglang/commit/d067622820) [#35340](https://github.com/sgl-project/sglang/pull/35340)
  [AMD][bugfix] Add moe_ep_size/moe_tp_size to the allreduce-fusion gate test stub (#35340)
  _Files: `test/registered/ops/test_aiter_allreduce_fusion_amd.py`_
- **2026-08-25** [`bf1e03f712`](https://github.com/sgl-project/sglang/commit/bf1e03f712) [#36237](https://github.com/sgl-project/sglang/pull/36237)
  [MegaMoE] Respect padded MXFP8 scale row strides in pre-dispatch (#36237)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `test/registered/kernels/ops/moe/test_mega_moe_pre_dispatch.py`_
- **2026-08-24** [`0665740953`](https://github.com/sgl-project/sglang/commit/0665740953) [#32039](https://github.com/sgl-project/sglang/pull/32039)
  [AMD][Fix] Route MoRI through the Qwen MoE all-to-all path (#32039)
  _Files: `python/sglang/srt/models/qwen2_moe.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`_
- **2026-08-24** [`21258b7a35`](https://github.com/sgl-project/sglang/commit/21258b7a35) [#31429](https://github.com/sgl-project/sglang/pull/31429)
  feat(humming): FP8 DeepEP dispatch for humming MoE backend (#31429)
  _Files: `python/pyproject.toml`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/humming.py`, `python/sglang/srt/layers/quantization/humming.py` _+2 more__
- **2026-08-24** [`46b92b22e2`](https://github.com/sgl-project/sglang/commit/46b92b22e2) [#35969](https://github.com/sgl-project/sglang/pull/35969)
  [diffusion] Accelerate LingBot Video RMSNorm in quality=high (#35969)
  _Files: `docs/docs/sglang-diffusion/fused_kernels.mdx`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/sites/lingbot_video_rmsnorm_site.py`, `python/sglang/multimodal_gen/runtime/models/dits/lingbot_video_moe.py` _+2 more__
- **2026-08-24** [`77940dec80`](https://github.com/sgl-project/sglang/commit/77940dec80) [#34915](https://github.com/sgl-project/sglang/pull/34915)
  [MoE] Gather the cutlass MoE activation and its scales in one launch (#34915)
  _Files: `python/sglang/kernels/ops/moe/__init__.py`, `python/sglang/kernels/ops/moe/shuffle_rows_with_scales.py`, `python/sglang/srt/layers/moe/cutlass_moe.py`, `test/registered/kernels/benchmark/moe/bench_shuffle_rows_with_scales.py` _+1 more__
- **2026-08-24** [`b498efce52`](https://github.com/sgl-project/sglang/commit/b498efce52) [#36053](https://github.com/sgl-project/sglang/pull/36053)
  chore: move cuda_vmm_utils.py under srt/utils/ (#36053)
  _Files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `python/sglang/srt/layers/moe/dwdp/layout.py`, `python/sglang/srt/layers/moe/dwdp/page_pool.py` _+8 more__
- **2026-08-24** [`56834422a1`](https://github.com/sgl-project/sglang/commit/56834422a1) [#33323](https://github.com/sgl-project/sglang/pull/33323)
  [Intel XPU] Add xpu pass for biased_topk and hash_topk (#33323)
  _Files: `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/xpu/test_topk.py`_

## Quantization  (47 commits)

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
- **2026-08-30** [`aa483ab782`](https://github.com/sgl-project/sglang/commit/aa483ab782) [#37004](https://github.com/sgl-project/sglang/pull/37004)
  [diffusion] feat: support streaming native vae weights directly to gpu (#37004)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/composed_pipeline_base.py` _+5 more__
- **2026-08-30** [`9a489f8d2f`](https://github.com/sgl-project/sglang/commit/9a489f8d2f) [#36979](https://github.com/sgl-project/sglang/pull/36979)
  [Test] Move `gpqa` and `aime25` onto sgl-eval, drop unused eval paths (#36979)
  _Files: `docs/docs/hardware-platforms/ascend-npus/development/contribution_guide.mdx`, `python/sglang/test/gpt_oss_common.py`, `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_aime25.py` _+11 more__
- **2026-08-29** [`a1fe4e30a9`](https://github.com/sgl-project/sglang/commit/a1fe4e30a9) [#37018](https://github.com/sgl-project/sglang/pull/37018)
  [Kernel] Fix SM90 FP8 decode regression with benchmarked M/K/N routing (#37018)
  _Files: `python/sglang/kernels/ops/gemm/__init__.py`_
- **2026-08-29** [`f8f501f2e8`](https://github.com/sgl-project/sglang/commit/f8f501f2e8) [#35739](https://github.com/sgl-project/sglang/pull/35739)
  [diffusion] fix: fix nvfp4 diffusion models on sm_120 (RTX PRO 6000 / RTX 50xx) (#35739)
  _Files: `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py`, `python/sglang/multimodal_gen/test/unit/test_modelopt_fp4_backend.py`_
- **2026-08-29** [`d1ce017665`](https://github.com/sgl-project/sglang/commit/d1ce017665) [#36902](https://github.com/sgl-project/sglang/pull/36902)
  [diffusion] feat: delegate recognized quantized components to transformers (#36902)
  _Files: `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/test/unit/test_image_encoder_loader.py` _+1 more__
- **2026-08-29** [`3c1d77be21`](https://github.com/sgl-project/sglang/commit/3c1d77be21) [#36874](https://github.com/sgl-project/sglang/pull/36874)
  [diffusion] feat: respect component weight overrides for upsamplers (#36874)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/upsampler_loader.py`, `python/sglang/multimodal_gen/test/unit/test_component_quantization_admission.py`_
- **2026-08-29** [`f93b48c627`](https://github.com/sgl-project/sglang/commit/f93b48c627) [#36883](https://github.com/sgl-project/sglang/pull/36883)
  [diffusion] refactor: resolve indexed component weight sets (#36883)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`, `python/sglang/multimodal_gen/runtime/weights/source.py`, `python/sglang/multimodal_gen/test/unit/test_transformer_quant.py` _+1 more__
- **2026-08-29** [`8a4c517a60`](https://github.com/sgl-project/sglang/commit/8a4c517a60) [#36950](https://github.com/sgl-project/sglang/pull/36950)
  [Docs] Restore the AIME25 label so GLM-5.3 FP8 and BF16 scores render again (#36950)
  _Files: `docs/src/snippets/configs/zai-org/glm-5.3.jsx`_
- **2026-08-28** [`e1b3bba3cc`](https://github.com/sgl-project/sglang/commit/e1b3bba3cc) [#34318](https://github.com/sgl-project/sglang/pull/34318)
  [Kernel] Route large SM90 row/column-scaled FP8 GEMMs to Torch (#34318)
  _Files: `python/sglang/kernels/ops/gemm/__init__.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/registered/kernels/ops/layernorm/test_kernels_namespace.py`_
- **2026-08-28** [`0c7d017dbb`](https://github.com/sgl-project/sglang/commit/0c7d017dbb) [#35341](https://github.com/sgl-project/sglang/pull/35341)
  [AMD][Fix] Qwen3.5: make empty-batch guard tuple-aware on fused AR+quant path (#35341)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-08-28** [`cbd0271574`](https://github.com/sgl-project/sglang/commit/cbd0271574) [#34747](https://github.com/sgl-project/sglang/pull/34747)
  [diffusion] model: add cosmos3 transfer capability (#34747)
  _Files: `docker/Dockerfile`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/multimodal_gen/configs/sample/cosmos3.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py` _+9 more__
- **2026-08-27** [`7cbe564829`](https://github.com/sgl-project/sglang/commit/7cbe564829) [#36529](https://github.com/sgl-project/sglang/pull/36529)
  [Fix][XPU/ROCm/NPU] Defer sgl_kernel.quantization import in expert_pack (#36529)
  _Files: `python/sglang/srt/layers/quantization/expert_pack.py`, `python/sglang/test/runners.py`, `test/registered/xpu/test_xpu_classification.py`, `test/registered/xpu/test_xpu_embedding.py` _+2 more__
- **2026-08-26** [`45c85c198b`](https://github.com/sgl-project/sglang/commit/45c85c198b) [#36570](https://github.com/sgl-project/sglang/pull/36570)
  [CI] Lower the AWQ Marlin MMLU threshold to 0.80 (#36570)
  _Files: `test/registered/quant/test_awq.py`_
- **2026-08-26** [`689ade69d1`](https://github.com/sgl-project/sglang/commit/689ade69d1) [#35735](https://github.com/sgl-project/sglang/pull/35735)
  [kernel] Split the custom all-reduce communicator into push/pull planes (#35735)
  _Files: `python/sglang/kernels/jit/csrc/distributed/communicator.cuh`, `python/sglang/kernels/jit/csrc/distributed/custom_all_reduce.cuh`, `python/sglang/kernels/jit/csrc/distributed/registry.cuh`, `python/sglang/kernels/jit/csrc/distributed/tp_qknorm.cuh` _+24 more__
- **2026-08-26** [`054f485d38`](https://github.com/sgl-project/sglang/commit/054f485d38) [#36028](https://github.com/sgl-project/sglang/pull/36028)
  [diffusion] docs: add MiniMax H3 checkpoint format table (#36028)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`_
- **2026-08-25** [`6569125e3a`](https://github.com/sgl-project/sglang/commit/6569125e3a) [#36142](https://github.com/sgl-project/sglang/pull/36142)
  [AMD][CI] Add MiniMax-M3-MXFP8 MI35x nightly perf benchmark (#36142)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `test/registered/amd/perf/mi35x/test_minimax_m3_perf_mi35x.py`_
- **2026-08-25** [`6a81038317`](https://github.com/sgl-project/sglang/commit/6a81038317) [#33021](https://github.com/sgl-project/sglang/pull/33021)
  [AMD] Drop redundant FP8 bpreshuffle scale transpose via fused AR kernel (#33021)
  _Files: `python/sglang/srt/distributed/communication_op.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/layernorm.py`_
- **2026-08-25** [`a618d4c064`](https://github.com/sgl-project/sglang/commit/a618d4c064) [#36246](https://github.com/sgl-project/sglang/pull/36246)
  [AMD] Add Kimi-K2.7-Code-MXFP4 to cookbook (#36246)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K2.7-Code.mdx`, `docs/src/snippets/autoregressive/kimi-k27-code-deployment.jsx`_
- **2026-08-25** [`2e3934f4cb`](https://github.com/sgl-project/sglang/commit/2e3934f4cb) [#35630](https://github.com/sgl-project/sglang/pull/35630)
  [AMD] Enable Mori-EP on kimi-k3 (#35630)
  _Files: `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/models/kimi_k3.py`_
- **2026-08-25** [`191244b3f6`](https://github.com/sgl-project/sglang/commit/191244b3f6) [#36046](https://github.com/sgl-project/sglang/pull/36046)
  [diffusion] feat: support loading Comfy NVFP4-AWQ text encoders (#36046)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/comfy_nvfp4.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py` _+3 more__
- **2026-08-25** [`9eee990ce1`](https://github.com/sgl-project/sglang/commit/9eee990ce1) [#36245](https://github.com/sgl-project/sglang/pull/36245)
  [AMD] cookbook: add HiCache host-DRAM KV tier for Qwen3.5 MXFP4 on MI355X (#36245)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-08-25** [`67853c5804`](https://github.com/sgl-project/sglang/commit/67853c5804) [#36066](https://github.com/sgl-project/sglang/pull/36066)
  [diffusion] feat: dispatch fp8 companions in mixed NVFP4 checkpoints (#36066)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`, `python/sglang/multimodal_gen/runtime/loader/minimax_h3_weights.py` _+1 more__
- **2026-08-25** [`f8f9226cd2`](https://github.com/sgl-project/sglang/commit/f8f9226cd2) [#36035](https://github.com/sgl-project/sglang/pull/36035)
  [diffusion] feat: support component-scoped quantization overrides (#36035)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py` _+4 more__
- **2026-08-25** [`ddea7b9156`](https://github.com/sgl-project/sglang/commit/ddea7b9156) [#36061](https://github.com/sgl-project/sglang/pull/36061)
  [diffusion] feat: support mixed Comfy NVFP4 and INT8 layers (#36061)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`, `python/sglang/multimodal_gen/runtime/loader/minimax_h3_weights.py`, `python/sglang/multimodal_gen/test/unit/test_transformer_quant.py`_
- **2026-08-24** [`30f9ed09d1`](https://github.com/sgl-project/sglang/commit/30f9ed09d1) [#36055](https://github.com/sgl-project/sglang/pull/36055)
  [diffusion] feat: support loading minimax h3 gguf text encoders (#36055)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/base_config.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/gguf.py` _+6 more__
- **2026-08-24** [`9b0007ed19`](https://github.com/sgl-project/sglang/commit/9b0007ed19) [#36044](https://github.com/sgl-project/sglang/pull/36044)
  [diffusion] feat: support loading comfy nvfp4 minimax h3 checkpoints (#36044)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/base_config.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py` _+5 more__
- **2026-08-24** [`76d1401881`](https://github.com/sgl-project/sglang/commit/76d1401881) [#36040](https://github.com/sgl-project/sglang/pull/36040)
  [diffusion] feat: support mixed w4a4 and int8 checkpoints (#36040)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/kitchen_w4a4_config.py`, `python/sglang/multimodal_gen/runtime/utils/quantization_utils.py` _+1 more__
- **2026-08-24** [`9856b58de4`](https://github.com/sgl-project/sglang/commit/9856b58de4) [#36056](https://github.com/sgl-project/sglang/pull/36056)
  [diffusion] feat: support loading serialized fp8 clip image encoders (#36056)
  _Files: `python/sglang/multimodal_gen/configs/models/encoders/base.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/models/encoders/base.py`, `python/sglang/multimodal_gen/runtime/models/encoders/clip.py` _+2 more__
- **2026-08-24** [`bfeae4e79a`](https://github.com/sgl-project/sglang/commit/bfeae4e79a) [#36039](https://github.com/sgl-project/sglang/pull/36039)
  [diffusion] feat: support loading serialized convrot w4a4 checkpoints (#36039)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/configs/kitchen_w4a4_config.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/kitchen_w4a4.py` _+5 more__
- **2026-08-24** [`716a6bf10c`](https://github.com/sgl-project/sglang/commit/716a6bf10c) [#32033](https://github.com/sgl-project/sglang/pull/32033)
  feat(humming): support native W4AFP8 checkpoint schemas (#32033)
  _Files: `python/sglang/srt/layers/quantization/humming.py`, `test/registered/unit/layers/quantization/test_humming_w4afp8_schemas.py`_
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

## Prefill / Decode Disaggregation  (45 commits)

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
- **2026-08-30** [`007ef5e23a`](https://github.com/sgl-project/sglang/commit/007ef5e23a) [#37094](https://github.com/sgl-project/sglang/pull/37094)
  [mem_cache] Move `req_pool_idx` into `ReqKvInfo` (#37094)
  _Files: `python/sglang/srt/beam_search/coordinator.py`, `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py` _+64 more__
- **2026-08-30** [`26c754e06e`](https://github.com/sgl-project/sglang/commit/26c754e06e) [#36983](https://github.com/sgl-project/sglang/pull/36983)
  [vlm] fix: recover multimodal decode and processor failures (#36983)
  _Files: `python/sglang/srt/multimodal/cache/identity.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/llava.py`, `python/sglang/srt/multimodal/processors/moss_vl.py` _+7 more__
- **2026-08-30** [`512df615de`](https://github.com/sgl-project/sglang/commit/512df615de) [#33048](https://github.com/sgl-project/sglang/pull/33048)
  [Bugfix] Hold references to fire-and-forget tasks in disaggregation (#33048)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/encoder/runtime.py`_
- **2026-08-30** [`0438b16154`](https://github.com/sgl-project/sglang/commit/0438b16154) [#37078](https://github.com/sgl-project/sglang/pull/37078)
  [mem_cache] Move `kv_committed_len` into `ReqKvInfo` (#37078)
  _Files: `python/sglang/srt/beam_search/coordinator.py`, `python/sglang/srt/beam_search/fork.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_allocator.py` _+33 more__
- **2026-08-30** [`6be767c2d2`](https://github.com/sgl-project/sglang/commit/6be767c2d2) [#36982](https://github.com/sgl-project/sglang/pull/36982)
  [mem_cache] Move `cache_protected_len` and `swa_evict_floor` into `ReqKvInfo` (#36982)
  _Files: `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py` _+25 more__
- **2026-08-30** [`ca8ff035c3`](https://github.com/sgl-project/sglang/commit/ca8ff035c3) [#37026](https://github.com/sgl-project/sglang/pull/37026)
  fix(hicache): isolate decode offload state per request (#37026)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `test/registered/unit/disaggregation/test_specv2_kvcache_offloading.py`_
- **2026-08-29** [`4d53767b09`](https://github.com/sgl-project/sglang/commit/4d53767b09) [#36975](https://github.com/sgl-project/sglang/pull/36975)
  config: the lazy imports that buy nothing become eager (#36975)
  _Files: `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/dllm_hook.py` _+34 more__
- **2026-08-29** [`f0d621cfa6`](https://github.com/sgl-project/sglang/commit/f0d621cfa6) [#36974](https://github.com/sgl-project/sglang/pull/36974)
  config: the dead record parameters go (#36974)
  _Files: `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/memory_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/parallel_hook.py` _+7 more__
- **2026-08-29** [`b65e677e48`](https://github.com/sgl-project/sglang/commit/b65e677e48) [#36972](https://github.com/sgl-project/sglang/pull/36972)
  config: the resolution callbacks into the record go to zero (#36972)
  _Files: `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/expert_pack_hook.py`, `python/sglang/srt/arg_groups/hicache_hook.py` _+46 more__
- **2026-08-29** [`24a3a63e6b`](https://github.com/sgl-project/sglang/commit/24a3a63e6b) [#36958](https://github.com/sgl-project/sglang/pull/36958)
  [misc] Keep `req.kv` non-optional and key KV ownership on `req_pool_idx` (#36958)
  _Files: `python/sglang/srt/beam_search/fork.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/disaggregation/prefill.py` _+14 more__
- **2026-08-29** [`24c9251ac5`](https://github.com/sgl-project/sglang/commit/24c9251ac5) [#36714](https://github.com/sgl-project/sglang/pull/36714)
  [AMD][Spec][PD] Enable the PD DSA fused-TopK seed remap on ROCm (#36714)
  _Files: `python/sglang/srt/layers/attention/dsa/utils.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-08-29** [`3760296be8`](https://github.com/sgl-project/sglang/commit/3760296be8) [#35762](https://github.com/sgl-project/sglang/pull/35762)
  [PD] Pack DCP1→DCP-N PD KV transfers into dest-contiguous RDMA blocks (#35762)
  _Files: `python/sglang/kernels/ops/kvcache/__init__.py`, `python/sglang/kernels/ops/kvcache/pd_dcp_gather.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/dcp_pack.py` _+6 more__
- **2026-08-29** [`5f216fc33f`](https://github.com/sgl-project/sglang/commit/5f216fc33f) [#35758](https://github.com/sgl-project/sglang/pull/35758)
  qwen 3.8 rebase (#35758)
  _Files: `python/sglang/kernels/jit/csrc/minimax/per_token_quant_ue8m0.cuh`, `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/kernels/ops/communication/mnnvl_cutedsl/__init__.py`, `python/sglang/kernels/ops/communication/mnnvl_cutedsl/config.py` _+93 more__
- **2026-08-28** [`c9bba091f8`](https://github.com/sgl-project/sglang/commit/c9bba091f8) [#36382](https://github.com/sgl-project/sglang/pull/36382)
  [HiCache] Key storage prefetch by the request namespace (#36382)
  _Files: `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` _+2 more__
- **2026-08-28** [`ef20fab38a`](https://github.com/sgl-project/sglang/commit/ef20fab38a) [#36792](https://github.com/sgl-project/sglang/pull/36792)
  config: the forwarding slots go; the dispatcher calls the family directly (#36792)
  _Files: `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/arg_groups/lora_hook.py`, `python/sglang/srt/arg_groups/model_hook.py` _+19 more__
- **2026-08-28** [`c2928e86d7`](https://github.com/sgl-project/sglang/commit/c2928e86d7) [#36789](https://github.com/sgl-project/sglang/pull/36789)
  config: the resolution pipeline moves out of the record (#36789)
  _Files: `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/dllm_hook.py`, `python/sglang/srt/arg_groups/hicache_hook.py` _+26 more__
- **2026-08-28** [`b644771e07`](https://github.com/sgl-project/sglang/commit/b644771e07) [#36862](https://github.com/sgl-project/sglang/pull/36862)
  [Fix] Route the Mooncake MoE A2A backend through Kimi K3's EP-A2A / SP-MoE fast path (#36862)
  _Files: `python/sglang/srt/models/kimi_k3.py`_
- **2026-08-28** [`ecbadf0b4b`](https://github.com/sgl-project/sglang/commit/ecbadf0b4b) [#31320](https://github.com/sgl-project/sglang/pull/31320)
  [NPU] [Diffusion] support distributed inference pipeline for GLM-Image  (#31320)
  _Files: `docs/docs/sglang-diffusion/disaggregation.mdx`, `python/sglang/multimodal_gen/runtime/disaggregation/orchestrator.py`, `python/sglang/multimodal_gen/runtime/disaggregation/request_state.py`, `python/sglang/multimodal_gen/runtime/disaggregation/scheduler_mixin.py` _+10 more__
- **2026-08-28** [`9fc60a8afd`](https://github.com/sgl-project/sglang/commit/9fc60a8afd) [#29133](https://github.com/sgl-project/sglang/pull/29133)
  [PD] Fix MORI-IO ABORT bootstrap message handling (#29133)
  _Files: `python/sglang/srt/disaggregation/mori/conn.py`_
- **2026-08-27** [`6ff2a20ccf`](https://github.com/sgl-project/sglang/commit/6ff2a20ccf) [#36622](https://github.com/sgl-project/sglang/pull/36622)
  config: the record is not an object that gets passed around (#36622)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/elastic_ep/elastic_ep.py`, `python/sglang/srt/entrypoints/http_server.py` _+19 more__
- **2026-08-27** [`fd40a331bf`](https://github.com/sgl-project/sglang/commit/fd40a331bf) [#36621](https://github.com/sgl-project/sglang/pull/36621)
  config: a parallel size has one spelling; a patched scope declares its own (#36621)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/benchmark/one_batch.py`, `python/sglang/compile_deep_gemm.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py` _+58 more__
- **2026-08-27** [`8ad76415e2`](https://github.com/sgl-project/sglang/commit/8ad76415e2) [#36160](https://github.com/sgl-project/sglang/pull/36160)
  [PD][mori] Align prefill transfer control plane for unified control plane (#36160)
  _Files: `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/mori/conn.py`_
- **2026-08-27** [`97ba99067d`](https://github.com/sgl-project/sglang/commit/97ba99067d) [#34608](https://github.com/sgl-project/sglang/pull/34608)
  Publish per-scheduler load on a dedicated socket for load-aware routers (#34608)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/disaggregation/kv_events.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/kv_events_publisher.py` _+6 more__
- **2026-08-27** [`3402265989`](https://github.com/sgl-project/sglang/commit/3402265989) [#36586](https://github.com/sgl-project/sglang/pull/36586)
  [Core] Refactor server argument choices (#36586)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/server_args.py`, `test/manual/test_dsa_alias_cli_registry_env.py`, `test/registered/unit/disaggregation/test_kimi_k3_encoder_mode.py` _+1 more__
- **2026-08-26** [`c8b56b1f44`](https://github.com/sgl-project/sglang/commit/c8b56b1f44) [#36493](https://github.com/sgl-project/sglang/pull/36493)
  chore: bump mooncake version to 0.3.13 (#36493)
  _Files: `docker/Dockerfile`, `scripts/ci/cuda/ci_install_dependency.sh`, `test/registered/disaggregation/test_kimi_linear_pd_dcp4.py`_
- **2026-08-26** [`937af8538b`](https://github.com/sgl-project/sglang/commit/937af8538b) [#36254](https://github.com/sgl-project/sglang/pull/36254)
  config: the runtime readers take the published bags (#36254)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/benchmark/offline_throughput.py`, `python/sglang/benchmark/one_batch.py`, `python/sglang/benchmark/one_batch_server.py` _+63 more__
- **2026-08-26** [`5b7fc61306`](https://github.com/sgl-project/sglang/commit/5b7fc61306) [#36253](https://github.com/sgl-project/sglang/pull/36253)
  config: resolution reads the declarations, not the fields (#36253)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/expert_pack_hook.py`, `python/sglang/srt/arg_groups/hisparse_hook.py`, `python/sglang/srt/arg_groups/kimi_k3_hook.py` _+30 more__
- **2026-08-26** [`ae5feb4b9c`](https://github.com/sgl-project/sglang/commit/ae5feb4b9c) [#36252](https://github.com/sgl-project/sglang/pull/36252)
  config: stop handing the record to code that does not read it (#36252)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/distributed/device_communicators/mooncake_transfer_engine.py`, `python/sglang/srt/elastic_ep/elastic_ep.py`, `python/sglang/srt/entrypoints/http_server.py` _+56 more__
- **2026-08-26** [`d7b144f64e`](https://github.com/sgl-project/sglang/commit/d7b144f64e) [#36251](https://github.com/sgl-project/sglang/pull/36251)
  config: publishing is the process entry's job (#36251)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/disaggregation/encoder/grpc_server.py`, `python/sglang/srt/disaggregation/encoder/runtime.py` _+17 more__
- **2026-08-26** [`2511743bd7`](https://github.com/sgl-project/sglang/commit/2511743bd7) [#33091](https://github.com/sgl-project/sglang/pull/33091)
  [unified-memory] Stop eviction when shared allocation capacity is sufficient (#33091)
  _Files: `benchmark/unified_memory/bench_peer_aware_eviction.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/auxiliary_state.py`, `python/sglang/srt/mem_cache/allocation.py` _+18 more__
- **2026-08-26** [`4ae30dc736`](https://github.com/sgl-project/sglang/commit/4ae30dc736) [#35646](https://github.com/sgl-project/sglang/pull/35646)
  fix: detect cross-node multimodal transport by nnodes (#35646)
  _Files: `python/sglang/srt/disaggregation/encoder/receiver.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/rust_server.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+2 more__
- **2026-08-25** [`edff717ef0`](https://github.com/sgl-project/sglang/commit/edff717ef0) [#36351](https://github.com/sgl-project/sglang/pull/36351)
  fix(disagg): snapshot affected rooms before iterating outside the lock (#36351)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`_
- **2026-08-25** [`7ddf92d5f4`](https://github.com/sgl-project/sglang/commit/7ddf92d5f4) [#36029](https://github.com/sgl-project/sglang/pull/36029)
  fix(disagg): refresh stale prefill bootstrap metadata (#36029)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py` _+2 more__
- **2026-08-25** [`829138a31e`](https://github.com/sgl-project/sglang/commit/829138a31e) [#22607](https://github.com/sgl-project/sglang/pull/22607)
  [HiCache] Fix PP inconsistency with HiCache L3 (#22607) (#27010)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` _+6 more__
- **2026-08-25** [`833be86c15`](https://github.com/sgl-project/sglang/commit/833be86c15) [#36222](https://github.com/sgl-project/sglang/pull/36222)
  [CP V1 Deprecation 1/5] Migrate tests to strategy-based prefill CP (#36222)
  _Files: `test/manual/dsv4/test_b200_flash.py`, `test/manual/dsv4/test_b200_pro.py`, `test/manual/dsv4/test_b300_flash.py`, `test/manual/dsv4/test_b300_pro.py` _+16 more__
- **2026-08-24** [`24bce93c93`](https://github.com/sgl-project/sglang/commit/24bce93c93) [#36025](https://github.com/sgl-project/sglang/pull/36025)
  [AMD][MORI] Deduplicate CP-replicated state transfers (#36025)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-08-24** [`586211bc46`](https://github.com/sgl-project/sglang/commit/586211bc46) [#35840](https://github.com/sgl-project/sglang/pull/35840)
  Add PD test for inkling with mxfp8 KV (#35840)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/disaggregation/test_disaggregation_inkling_mxfp8.py`_
- **2026-08-24** [`3b24d8981b`](https://github.com/sgl-project/sglang/commit/3b24d8981b) [#35926](https://github.com/sgl-project/sglang/pull/35926)
  Report per-token weight-version spans in generation meta info (#35926)
  _Files: `docs/docs/advanced_features/sglang_for_rl.mdx`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_completions.py`, `python/sglang/srt/managers/detokenizer_manager.py` _+16 more__
- **2026-08-24** [`092d85eb87`](https://github.com/sgl-project/sglang/commit/092d85eb87) [#30360](https://github.com/sgl-project/sglang/pull/30360)
  [Feature] Add MiniCPM-SALA support (#30360)
  _Files: `python/sglang/kernels/jit/csrc/minicpm_sala/get_block_table.cuh`, `python/sglang/kernels/jit/minicpm_sala/__init__.py`, `python/sglang/kernels/jit/minicpm_sala/get_block_table.py`, `python/sglang/srt/arg_groups/overrides.py` _+40 more__
- **2026-08-24** [`a90d770c40`](https://github.com/sgl-project/sglang/commit/a90d770c40) [#33684](https://github.com/sgl-project/sglang/pull/33684)
  [Weight Cache] Support static DP/EP layouts (#33684)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/moe/token_dispatcher/mooncake.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/weight_cache/daemon.py` _+5 more__

## KV Cache / Memory  (36 commits)

- **2026-08-31** [`5d92e60783`](https://github.com/sgl-project/sglang/commit/5d92e60783) [#37151](https://github.com/sgl-project/sglang/pull/37151)
  [Unified Cache Linker][3/N]: Add backend-independent linker core (#37151)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_hiradix_pp_sync_drain.py`, `test/registered/unit/mem_cache/test_unified_cache_linker.py`_
- **2026-08-31** [`9a9e167179`](https://github.com/sgl-project/sglang/commit/9a9e167179) [#35588](https://github.com/sgl-project/sglang/pull/35588)
  [Bugfix] Fix full prefill CUDA graph padding and EAGLE capture (#35588)
  _Files: `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/cuda_graph/full_prefill/test_full_cuda_graph_prefill.py` _+3 more__
- **2026-08-31** [`62f86ce470`](https://github.com/sgl-project/sglang/commit/62f86ce470) [#37182](https://github.com/sgl-project/sglang/pull/37182)
  [CI] Fix unreachable FakeReq field initialization (#37182)
  _Files: `test/registered/unit/mem_cache/test_streaming_session_unit.py`_
- **2026-08-30** [`4bb8de34cc`](https://github.com/sgl-project/sglang/commit/4bb8de34cc) [#37108](https://github.com/sgl-project/sglang/pull/37108)
  [mem_cache] Share one `ReqKvInfo` between a streaming session slot and its request (#37108)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/session/streaming_session.py`, `test/registered/unit/mem_cache/test_streaming_session_unit.py`, `test/registered/unit/spec/test_decode_bookkeeping_ownership.py`_
- **2026-08-30** [`6a9366f036`](https://github.com/sgl-project/sglang/commit/6a9366f036) [#37098](https://github.com/sgl-project/sglang/pull/37098)
  [Unified Cache Linker][2/N]: Add device pool assembly for external linkers (#37098)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `test/registered/unit/mem_cache/test_linker_pool_assembler.py`_
- **2026-08-30** [`c9eb475a88`](https://github.com/sgl-project/sglang/commit/c9eb475a88) [#37091](https://github.com/sgl-project/sglang/pull/37091)
  [Unified Cache][1/N]: Support cache contract for external linker (#37091)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/unified_cache/components/__init__.py`, `python/sglang/srt/mem_cache/unified_cache/components/full_component.py` _+5 more__
- **2026-08-30** [`5ec959965b`](https://github.com/sgl-project/sglang/commit/5ec959965b) [#37085](https://github.com/sgl-project/sglang/pull/37085)
  [mem_cache] Settle extend `kv_committed_len` inside `alloc_for_extend` (#37085)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/allocation.py`, `test/registered/unit/spec/test_decode_bookkeeping_ownership.py`_
- **2026-08-29** [`a328c19c81`](https://github.com/sgl-project/sglang/commit/a328c19c81) [#36834](https://github.com/sgl-project/sglang/pull/36834)
  [HiCache] buffer mode: decide staged-fetch fate against the live tree (#36834)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-08-28** [`60f6d77a98`](https://github.com/sgl-project/sglang/commit/60f6d77a98) [#36909](https://github.com/sgl-project/sglang/pull/36909)
  [mem_cache] Carry `swa_evicted_seqlen` into `SWARadixCache.cache_unfinished_req` (#36909)
  _Files: `python/sglang/srt/mem_cache/swa_radix_cache.py`, `test/registered/unit/mem_cache/test_swa_unittest.py`_
- **2026-08-28** [`f611e0c073`](https://github.com/sgl-project/sglang/commit/f611e0c073) [#36738](https://github.com/sgl-project/sglang/pull/36738)
  [HiCache] Fence load-back behind the forward stream (#36738)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/mem_cache/test_hicache_staged_write_back_dispatch.py`_
- **2026-08-28** [`7bc3204117`](https://github.com/sgl-project/sglang/commit/7bc3204117) [#36791](https://github.com/sgl-project/sglang/pull/36791)
  config: three cache and pool readers take the bags (#36791)
  _Files: `python/sglang/srt/mem_cache/registry.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-08-28** [`8e04f66a70`](https://github.com/sgl-project/sglang/commit/8e04f66a70) [#36425](https://github.com/sgl-project/sglang/pull/36425)
  HiCache: avoid unnecessary all-reduce in check_prefetch_progress (#36425)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-08-28** [`23cb11ae01`](https://github.com/sgl-project/sglang/commit/23cb11ae01) [#36583](https://github.com/sgl-project/sglang/pull/36583)
  Fix KV cache pool sized far too small when weight-loading memory is still referenced (#36583)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`_
- **2026-08-28** [`d56706459c`](https://github.com/sgl-project/sglang/commit/d56706459c) [#36759](https://github.com/sgl-project/sglang/pull/36759)
  bugfix for index_fill_ on NPU (#36759)
  _Files: `python/sglang/srt/mem_cache/allocator/swa.py`_
- **2026-08-28** [`3785b2d20f`](https://github.com/sgl-project/sglang/commit/3785b2d20f) [#35931](https://github.com/sgl-project/sglang/pull/35931)
  [HiCache] Reject load-back specs that claim nodes pinned by an in-flight load-back (#35931)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-08-28** [`1061e34785`](https://github.com/sgl-project/sglang/commit/1061e34785) [#36227](https://github.com/sgl-project/sglang/pull/36227)
  [HiCache] Retry L3 storage prefetch after a missed attempt (#36227)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` _+3 more__
- **2026-08-28** [`3f1031d697`](https://github.com/sgl-project/sglang/commit/3f1031d697) [#36386](https://github.com/sgl-project/sglang/pull/36386)
  [HiCache] Heal the storage existence cache on a hybrid prefetch discard (#36386)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-08-28** [`2380121e9b`](https://github.com/sgl-project/sglang/commit/2380121e9b) [#36705](https://github.com/sgl-project/sglang/pull/36705)
  [HiCache] Stop populating host-pool mmaps twice (-13% allocation time) (#36705)
  _Files: `python/sglang/srt/mem_cache/storage/mmap/mmap_allocator.py`, `test/registered/unit/mem_cache/test_mmap_allocator.py`_
- **2026-08-28** [`daf6317196`](https://github.com/sgl-project/sglang/commit/daf6317196) [#36637](https://github.com/sgl-project/sglang/pull/36637)
  [mem_cache] Add `free_full` to release the full side of a tombstoned SWA node (#36637)
  _Files: `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/hisparse.py`, `python/sglang/srt/mem_cache/allocator/swa.py`, `python/sglang/srt/mem_cache/multi_ended_allocator.py` _+8 more__
- **2026-08-27** [`5d52f02f22`](https://github.com/sgl-project/sglang/commit/5d52f02f22) [#36739](https://github.com/sgl-project/sglang/pull/36739)
  [misc] Fold the allocator free-group flag into `free_group` (#36739)
  _Files: `python/sglang/srt/hardware_backend/npu/allocator_npu.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/hisparse.py`, `python/sglang/srt/mem_cache/allocator/paged.py` _+3 more__
- **2026-08-27** [`ff5578eb4e`](https://github.com/sgl-project/sglang/commit/ff5578eb4e) [#36288](https://github.com/sgl-project/sglang/pull/36288)
  [1/N][Mix] Mixed Chunk Prefill Base (#36288)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py` _+3 more__
- **2026-08-27** [`20a491d1d3`](https://github.com/sgl-project/sglang/commit/20a491d1d3) [#36595](https://github.com/sgl-project/sglang/pull/36595)
  [Fix] Re-encode multimodal embeddings after cache mismatch (#36595)
  _Files: `python/sglang/srt/managers/mm_schedule.py`, `test/registered/chunked_prefill/test_mm_chunked_embedding_unit.py`_
- **2026-08-27** [`ea48cb04cc`](https://github.com/sgl-project/sglang/commit/ea48cb04cc) [#35944](https://github.com/sgl-project/sglang/pull/35944)
  Pin scheduler metadata before asynchronous H2D copies (#35944)
  _Files: `python/sglang/srt/mem_cache/allocation.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-08-27** [`a2b589fdf8`](https://github.com/sgl-project/sglang/commit/a2b589fdf8) [#35791](https://github.com/sgl-project/sglang/pull/35791)
  [Radix Cache] Add test-only TreeCore inspector for shared backend tests (#35791)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `test/registered/unit/mem_cache/test_tree_core_registry.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`, `test/registered/unit/mem_cache/unified_tree_core_inspection_interface.py` _+1 more__
- **2026-08-27** [`862f9ed3d8`](https://github.com/sgl-project/sglang/commit/862f9ed3d8) [#36343](https://github.com/sgl-project/sglang/pull/36343)
  [AMD] Fall back to CPU tensor for decode retraction on ROCm (#36343)
  _Files: `python/sglang/srt/mem_cache/kv_cache_builder.py`_
- **2026-08-27** [`8739d56a31`](https://github.com/sgl-project/sglang/commit/8739d56a31) [#35379](https://github.com/sgl-project/sglang/pull/35379)
  [Spec] Generalize hybrid SWA MTP draft pool routing (#35379)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/pool_configurator.py`_
- **2026-08-26** [`06694071c6`](https://github.com/sgl-project/sglang/commit/06694071c6) [#35377](https://github.com/sgl-project/sglang/pull/35377)
  [Spec] Avoid tensor scalar reads in spec decode allocation (#35377)
  _Files: `python/sglang/srt/mem_cache/allocation.py`_
- **2026-08-26** [`5263568bcb`](https://github.com/sgl-project/sglang/commit/5263568bcb) [#36317](https://github.com/sgl-project/sglang/pull/36317)
  [HiCache] Keep auxiliary load-back out of Full KV pending ownership (#36317)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-08-26** [`bede6bc37c`](https://github.com/sgl-project/sglang/commit/bede6bc37c) [#36454](https://github.com/sgl-project/sglang/pull/36454)
  Fix unified HiCache PP test import (#36454)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_hicache_pp_kl.py`_
- **2026-08-26** [`bec6248272`](https://github.com/sgl-project/sglang/commit/bec6248272) [#36281](https://github.com/sgl-project/sglang/pull/36281)
  [Unified Cache]: add glm5.2 per commit ci (#36281)
  _Files: `python/sglang/test/kits/unified_radix_cache_kit.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dsv4.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_glm52.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mamba.py` _+1 more__
- **2026-08-25** [`aa718f7343`](https://github.com/sgl-project/sglang/commit/aa718f7343) [#36232](https://github.com/sgl-project/sglang/pull/36232)
  Refactor HiCache host pool management (#36232)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py` _+12 more__
- **2026-08-25** [`f7a56494b1`](https://github.com/sgl-project/sglang/commit/f7a56494b1) [#36381](https://github.com/sgl-project/sglang/pull/36381)
  Fix SWA ownership across grouped frees (#36381)
  _Files: `python/sglang/srt/mem_cache/allocator/swa.py`, `test/registered/unit/mem_cache/test_swa_unittest.py`_
- **2026-08-25** [`01db8a7829`](https://github.com/sgl-project/sglang/commit/01db8a7829) [#35297](https://github.com/sgl-project/sglang/pull/35297)
  [BugFix][Qwen3.8] Support Qwen3.8-MXFP4 DCP by registing Qwen3_5 text-only archs in mamba radix cache whitelists (#35297)
  _Files: `python/sglang/srt/arg_groups/overrides.py`_
- **2026-08-25** [`0f7ba3d115`](https://github.com/sgl-project/sglang/commit/0f7ba3d115) [#32162](https://github.com/sgl-project/sglang/pull/32162)
  [HiSparse] Support hisparse multi-step swap io kernel (#32162)
  _Files: `python/sglang/kernels/jit/csrc/kvcacheio/hisparse.cuh`, `python/sglang/kernels/jit/csrc/kvcacheio/hisparse_spec.cuh`, `python/sglang/kernels/ops/kvcache/hisparse.py`, `test/registered/jit/benchmark/bench_hisparse_spec.py` _+1 more__
- **2026-08-24** [`54ec2c4699`](https://github.com/sgl-project/sglang/commit/54ec2c4699) [#35957](https://github.com/sgl-project/sglang/pull/35957)
  Fix recurrent state loss on decode retraction (#35957)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+1 more__
- **2026-08-24** [`d251fa2453`](https://github.com/sgl-project/sglang/commit/d251fa2453) [#34066](https://github.com/sgl-project/sglang/pull/34066)
  perf(unified-memory): batch lazy-compaction mapping lookup (#34066)
  _Files: `python/sglang/srt/mem_cache/multi_ended_allocator.py`, `test/registered/unit/mem_cache/test_multi_ended_allocator.py`_

## Other  (21 commits)

- **2026-08-31** [`0da6a66856`](https://github.com/sgl-project/sglang/commit/0da6a66856) [#37035](https://github.com/sgl-project/sglang/pull/37035)
  [MLX] Fix startup crash when reporting preloaded weights (#37035)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_runner_pool_contract.py`_
- **2026-08-30** [`7e751153eb`](https://github.com/sgl-project/sglang/commit/7e751153eb) [#37086](https://github.com/sgl-project/sglang/pull/37086)
  [Config] Round 5.1: the published-side readers ask the bags, and a platform fact gets one address (#37086)
- **2026-08-30** [`5b7c62d5d6`](https://github.com/sgl-project/sglang/commit/5b7c62d5d6) [#37029](https://github.com/sgl-project/sglang/pull/37029)
  fix(frontend): bound stop strings and regex patterns (#37029)
  _Files: `python/sglang/srt/sampling/sampling_params.py`, `test/registered/unit/sampling/test_sampling_params.py`_
- **2026-08-29** [`0a585d5bb1`](https://github.com/sgl-project/sglang/commit/0a585d5bb1) [#34639](https://github.com/sgl-project/sglang/pull/34639)
  [BugFix] Allow model_loader_extra_config with remote_instance + modelexpress backend (#34639)
  _Files: `python/sglang/srt/model_loader/loader.py`, `test/registered/unit/model_loader/test_remote_instance_loader.py`_
- **2026-08-28** [`137fab2f48`](https://github.com/sgl-project/sglang/commit/137fab2f48) [#36794](https://github.com/sgl-project/sglang/pull/36794)
  fix(deps): pin compressed-tensors to 0.18.0 (#36794)
  _Files: `python/pyproject.toml`_
- **2026-08-27** [`ca1d7ed8e6`](https://github.com/sgl-project/sglang/commit/ca1d7ed8e6) [#36620](https://github.com/sgl-project/sglang/pull/36620)
  config: a parallel leaf with no live counterpart is read bare (#36620)
- **2026-08-27** [`bd4bb1781a`](https://github.com/sgl-project/sglang/commit/bd4bb1781a) [#36618](https://github.com/sgl-project/sglang/pull/36618)
  config: resolution declares, and nothing writes a field (#36618)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/srt/arg_groups/overrides.py`, `test/registered/unit/server_args/test_record_holds_the_raw_input.py`, `test/registered/unit/test_chain_read_ratchet.py` _+1 more__
- **2026-08-27** [`b647ae82f5`](https://github.com/sgl-project/sglang/commit/b647ae82f5) [#35727](https://github.com/sgl-project/sglang/pull/35727)
  [NPU][Bugfix] Fix OOB gather in decode KV allocation when free pool is tight (#35727)
  _Files: `python/sglang/srt/hardware_backend/npu/allocator_npu.py`_
- **2026-08-27** [`94183a8d2b`](https://github.com/sgl-project/sglang/commit/94183a8d2b) [#36681](https://github.com/sgl-project/sglang/pull/36681)
  Move server args config parser under utils (#36681)
  _Files: `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/server_args_config_parser.py`, `test/manual/test_config_integration.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-08-27** [`b658d64d5b`](https://github.com/sgl-project/sglang/commit/b658d64d5b) [#36443](https://github.com/sgl-project/sglang/pull/36443)
  [CPU] Fix rotary_embedding_cpu fake for in-place layouts (#36443)
  _Files: `python/sglang/srt/model_executor/cpu_graph_runner.py`_
- **2026-08-27** [`a8b72c4c34`](https://github.com/sgl-project/sglang/commit/a8b72c4c34) [#36360](https://github.com/sgl-project/sglang/pull/36360)
  [Intel XPU] Fix cross-encoder rerank hang on B580 runners (#36360)
  _Files: `test/registered/xpu/test_xpu_rerank.py`_
- **2026-08-26** [`e5a1c5a423`](https://github.com/sgl-project/sglang/commit/e5a1c5a423) [#36573](https://github.com/sgl-project/sglang/pull/36573)
  Fix _is_compiling dynamo tracing: import torch instead of sys.modules lookup (#36573)
  _Files: `python/sglang/srt/runtime_context.py`_
- **2026-08-26** [`e7e7894016`](https://github.com/sgl-project/sglang/commit/e7e7894016) [#36299](https://github.com/sgl-project/sglang/pull/36299)
  [Weight Cache] Make daemon socket/ready paths configurable via env (#36299)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/weight_cache/protocol.py`_
- **2026-08-26** [`8005df61d3`](https://github.com/sgl-project/sglang/commit/8005df61d3) [#36250](https://github.com/sgl-project/sglang/pull/36250)
  config: spell the parallel config tier at the call site (#36250)
- **2026-08-25** [`443527af0c`](https://github.com/sgl-project/sglang/commit/443527af0c) [#36300](https://github.com/sgl-project/sglang/pull/36300)
  config: the model-config cache keys on the path the record carried (#36300)
  _Files: `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_model_config_cache.py`_
- **2026-08-25** [`7769ff8f1e`](https://github.com/sgl-project/sglang/commit/7769ff8f1e) [#36231](https://github.com/sgl-project/sglang/pull/36231)
  [DeepGEMM] Deduplicate JIT precompile across local ranks (#36231)
  _Files: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`_
- **2026-08-25** [`a0f52eca98`](https://github.com/sgl-project/sglang/commit/a0f52eca98) [#33634](https://github.com/sgl-project/sglang/pull/33634)
  [NPU] Add test for --dllm-fdfo (#33634)
  _Files: `test/registered/npu/basic_function/dllm/test_npu_llada2_mini_fdfo.py`_
- **2026-08-24** [`3c481b9421`](https://github.com/sgl-project/sglang/commit/3c481b9421) [#30918](https://github.com/sgl-project/sglang/pull/30918)
  [Benchmark] Add optional steady-state window for serving metrics (#30918)
  _Files: `python/sglang/benchmark/steady_state.py`, `python/sglang/benchmark/steady_state_serving.py`, `test/registered/bench_fn/test_steady_state_benchmark.py`_
- **2026-08-24** [`317da0964e`](https://github.com/sgl-project/sglang/commit/317da0964e) [#35072](https://github.com/sgl-project/sglang/pull/35072)
  [Intel XPU] support prefill only models for xpu (#35072)
  _Files: `test/registered/xpu/test_xpu_classification.py`, `test/registered/xpu/test_xpu_embedding.py`, `test/registered/xpu/test_xpu_rerank.py`, `test/registered/xpu/test_xpu_reward.py`_
- **2026-08-24** [`f464e77d17`](https://github.com/sgl-project/sglang/commit/f464e77d17) [#36150](https://github.com/sgl-project/sglang/pull/36150)
  fix(mini-lb): forward the flush_cache timeout param to workers (#36150)
  _Files: `sgl-model-gateway/bindings/python/src/sglang_router/mini_lb.py`_
- **2026-08-24** [`514b997e6c`](https://github.com/sgl-project/sglang/commit/514b997e6c) [#35227](https://github.com/sgl-project/sglang/pull/35227)
  Register CPU CI for 17 e2e tests and partition xeon base-c suite (#35227)

## CI / Build  (18 commits)

- **2026-08-31** [`5e679b0cad`](https://github.com/sgl-project/sglang/commit/5e679b0cad) [#37203](https://github.com/sgl-project/sglang/pull/37203)
  [CI] Speed up lint: cache pre-commit envs + mint, drop redundant work (#37203)
  _Files: `.github/workflows/lint.yml`_
- **2026-08-31** [`10b67aa7a1`](https://github.com/sgl-project/sglang/commit/10b67aa7a1) [#36814](https://github.com/sgl-project/sglang/pull/36814)
  xpu: move prefill-only model tests to the nightly-xpu-1-gpu grid (#36814)
  _Files: `test/registered/xpu/test_xpu_classification.py`, `test/registered/xpu/test_xpu_embedding.py`, `test/registered/xpu/test_xpu_rerank.py`, `test/registered/xpu/test_xpu_reward.py`_
- **2026-08-30** [`a7ee399904`](https://github.com/sgl-project/sglang/commit/a7ee399904) [#36998](https://github.com/sgl-project/sglang/pull/36998)
  Bump sgl-deep-gemm to v0.1.6 (#36998)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`_
- **2026-08-29** [`46ccd7ce3e`](https://github.com/sgl-project/sglang/commit/46ccd7ce3e) [#35547](https://github.com/sgl-project/sglang/pull/35547)
  Add Laguna-XS-2.1 / S-2.1 NVFP4 nightly gsm8k tests (#35547)
  _Files: `python/sglang/test/accuracy_test_runner.py`, `test/registered/4-gpu-models/test_laguna_nvfp4_nightly.py`_
- **2026-08-29** [`46334460a6`](https://github.com/sgl-project/sglang/commit/46334460a6) [#36981](https://github.com/sgl-project/sglang/pull/36981)
  [CI] Temporarily disable GB300 jobs (#36981)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/release-whl-deepgemm.yml`, `.github/workflows/rerun-test.yml`_
- **2026-08-29** [`4d7d2ebb44`](https://github.com/sgl-project/sglang/commit/4d7d2ebb44) [#36946](https://github.com/sgl-project/sglang/pull/36946)
  [Docker] Install AI Dynamo nightly (#36946)
  _Files: `docker/Dockerfile`_
- **2026-08-28** [`726665e08e`](https://github.com/sgl-project/sglang/commit/726665e08e) [#36673](https://github.com/sgl-project/sglang/pull/36673)
  [CI] Read subprocess stdout on a background thread to avoid EOF deadlock (#36673)
  _Files: `python/sglang/test/ci/ci_utils.py`_
- **2026-08-28** [`ce6e1f46b4`](https://github.com/sgl-project/sglang/commit/ce6e1f46b4) [#36756](https://github.com/sgl-project/sglang/pull/36756)
  Limit concurrent build jobs for cu134 container (#36756)
  _Files: `docker/Dockerfile.cu134`_
- **2026-08-27** [`7324021e6c`](https://github.com/sgl-project/sglang/commit/7324021e6c) [#36609](https://github.com/sgl-project/sglang/pull/36609)
  [CI] Grant no-cooldown for UNIDY2002 (#36609)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-08-26** [`0c84eaba7f`](https://github.com/sgl-project/sglang/commit/0c84eaba7f) [#36445](https://github.com/sgl-project/sglang/pull/36445)
  [CI] Grant no-cooldown and tag permissions to seven contributors (#36445)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-08-26** [`3ec22948c1`](https://github.com/sgl-project/sglang/commit/3ec22948c1) [#34057](https://github.com/sgl-project/sglang/pull/34057)
  [CI] /rerun-failed-ci: rerun cancelled runs and target the newest run per workflow (#34057)
  _Files: `docs/docs/developer_guide/contribution_guide.mdx`, `docs/docs/hardware-platforms/ascend-npus/development/contribution_guide.mdx`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-08-26** [`34de1fb47f`](https://github.com/sgl-project/sglang/commit/34de1fb47f) [#34668](https://github.com/sgl-project/sglang/pull/34668)
  fix(test): stabilize nightly precision regression (#34668)
  _Files: `.github/workflows/rerun-test.yml`, `docs/docs/references/nightly_precision_regression.mdx`, `python/sglang/test/precision_baseline_store.py`, `scripts/ci/utils/slash_command_handler.py` _+2 more__
- **2026-08-25** [`2d88c79b3e`](https://github.com/sgl-project/sglang/commit/2d88c79b3e) [#36284](https://github.com/sgl-project/sglang/pull/36284)
  [CI] Add Kimi-K3 MMMU-Pro accuracy coverage (#36284)
  _Files: `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/run_eval.py`, `scripts/ci/utils/sgl_eval_ref.sh`, `test/registered/models_e2e/test_kimi_k3_b300.py` _+3 more__
- **2026-08-25** [`0c7ff19e3b`](https://github.com/sgl-project/sglang/commit/0c7ff19e3b) [#36257](https://github.com/sgl-project/sglang/pull/36257)
  [NPU] [CI] Split the base-c-test-acc-2-npu-a3 task into two parts running in parallel (#36257)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-08-25** [`68575b23d0`](https://github.com/sgl-project/sglang/commit/68575b23d0) [#36240](https://github.com/sgl-project/sglang/pull/36240)
  [CI] Stop the config ratchets re-parsing the package on every scan (#36240)
  _Files: `test/registered/unit/server_args/test_model_config_reads_resolved_input.py`, `test/registered/unit/server_args/test_resolution_reads_no_bag.py`, `test/registered/unit/test_chain_read_ratchet.py`, `test/registered/unit/test_global_config_read_ratchet.py` _+4 more__
- **2026-08-24** [`1ec20fd25d`](https://github.com/sgl-project/sglang/commit/1ec20fd25d) [#36235](https://github.com/sgl-project/sglang/pull/36235)
  [CI] Stop the resolution ratchets re-parsing the whole package (#36235)
  _Files: `test/registered/unit/server_args/test_resolution_is_reproducible.py`_
- **2026-08-24** [`e28b9cf7b0`](https://github.com/sgl-project/sglang/commit/e28b9cf7b0) [#36092](https://github.com/sgl-project/sglang/pull/36092)
  Npu single node test timeout config (#36092)
  _Files: `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml`, `.github/workflows/pr-test-npu.yml`_
- **2026-08-24** [`ec334b17e2`](https://github.com/sgl-project/sglang/commit/ec334b17e2) [#36146](https://github.com/sgl-project/sglang/pull/36146)
  xeon ci fail fast strategy change (#36146)
  _Files: `.github/workflows/pr-test-xeon.yml`_

## ROCm / AMD  (14 commits)

- **2026-08-31** [`5972211977`](https://github.com/sgl-project/sglang/commit/5972211977) [#37132](https://github.com/sgl-project/sglang/pull/37132)
  [AMD] Fix the QuickReduce bf16 cast failing to build for CDNA (#37132)
  _Files: `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce.cuh`, `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce_base.h`_
- **2026-08-30** [`7399c2b558`](https://github.com/sgl-project/sglang/commit/7399c2b558) [#37092](https://github.com/sgl-project/sglang/pull/37092)
  [AMD] Update v4 amd cookbook 0830 (#37092)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-08-30** [`78fa921189`](https://github.com/sgl-project/sglang/commit/78fa921189) [#34484](https://github.com/sgl-project/sglang/pull/34484)
  [ROCm] Fix QuickReduce fp16 saturation corrupting bf16 all-reduces (106M non-finite -> 0, +0.3%) (#34484)
  _Files: `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce.cuh`, `python/sglang/kernels/aot/csrc/allreduce/quick_all_reduce_base.h`, `test/registered/kernels/test_quick_allreduce_bf16_range.py`_
- **2026-08-30** [`67bd163a48`](https://github.com/sgl-project/sglang/commit/67bd163a48) [#37083](https://github.com/sgl-project/sglang/pull/37083)
  [AMD] Cherry-pick dsv4 fp4 kv-cache fix aiter commit (#37083)
  _Files: `docker/rocm.Dockerfile`_
- **2026-08-29** [`89816a21a1`](https://github.com/sgl-project/sglang/commit/89816a21a1) [#36828](https://github.com/sgl-project/sglang/pull/36828)
  [AMD] Update v4 amd cookbook 0828 (#36828)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-08-28** [`2a7fb511c9`](https://github.com/sgl-project/sglang/commit/2a7fb511c9) [#36308](https://github.com/sgl-project/sglang/pull/36308)
  [AMD][CI] Limit HiCache MGSM eval concurrency on ROCm (#36308)
  _Files: `test/registered/hicache/test_hicache_variants.py`_
- **2026-08-28** [`cce0b53466`](https://github.com/sgl-project/sglang/commit/cce0b53466) [#35628](https://github.com/sgl-project/sglang/pull/35628)
  [AMD] Increase gfx950 DSA model indexer topk_transform kernel occupancy (#35628)
  _Files: `python/sglang/kernels/aot/setup_rocm.py`_
- **2026-08-27** [`e283c9f8ea`](https://github.com/sgl-project/sglang/commit/e283c9f8ea) [#36736](https://github.com/sgl-project/sglang/pull/36736)
  [AMD][CI] Merge the four MI35x DeepSeek-V3.2 nightly jobs into two to save runtime (#36736)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`_
- **2026-08-27** [`1a91c232ea`](https://github.com/sgl-project/sglang/commit/1a91c232ea) [#36636](https://github.com/sgl-project/sglang/pull/36636)
  [AMD][CI] Add targeted Mori test labels (#36636)
  _Files: `.github/workflows/pr-test-amd-mori.yml`_
- **2026-08-27** [`cbfe54fba8`](https://github.com/sgl-project/sglang/commit/cbfe54fba8) [#34296](https://github.com/sgl-project/sglang/pull/34296)
  [AMD] Use fast exponentials in C4 and C128 ROCm kernels (#34296)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c128_v2.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/c4_v2.cuh`_
- **2026-08-27** [`d2b3e9051d`](https://github.com/sgl-project/sglang/commit/d2b3e9051d) [#36307](https://github.com/sgl-project/sglang/pull/36307)
  [AMD][CI] Stabilize PyTorch sampling backend test on ROCm (#36307)
  _Files: `test/registered/sampling/test_pytorch_sampling_backend.py`_
- **2026-08-26** [`586a50cd96`](https://github.com/sgl-project/sglang/commit/586a50cd96) [#36393](https://github.com/sgl-project/sglang/pull/36393)
  [AMD][CI] Restore MiniMax-M2.5 4-GPU MI35x nightly job (#36393)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`_
- **2026-08-25** [`96a73c4e15`](https://github.com/sgl-project/sglang/commit/96a73c4e15) [#36290](https://github.com/sgl-project/sglang/pull/36290)
  [AMD][CI] Adjust MI300 score API performance thresholds (#36290)
  _Files: `test/registered/perf/test_bench_serving_1gpu_part2.py`_
- **2026-08-24** [`97b176e64c`](https://github.com/sgl-project/sglang/commit/97b176e64c) [#32597](https://github.com/sgl-project/sglang/pull/32597)
  Support streaming session on NPU (#32597)
  _Files: `python/sglang/srt/session/streaming_session.py`, `test/registered/unit/spec/test_decode_bookkeeping_ownership.py`_

## Triton / Kernels  (13 commits)

- **2026-08-31** [`b77cac06a9`](https://github.com/sgl-project/sglang/commit/b77cac06a9) [#36248](https://github.com/sgl-project/sglang/pull/36248)
  [PP] Support prefill CUDA graph proxy tensors (#36248)
  _Files: `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/memory_hook.py`, `python/sglang/srt/layers/cp/bcg.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py` _+8 more__
- **2026-08-31** [`afbca97f74`](https://github.com/sgl-project/sglang/commit/afbca97f74) [#36422](https://github.com/sgl-project/sglang/pull/36422)
  add suffix for xpu kernel upload space (#36422)
  _Files: `.github/workflows/release-whl-kernel-xpu.yml`, `scripts/update_kernel_whl_index.py`_
- **2026-08-28** [`ade4f4ba8b`](https://github.com/sgl-project/sglang/commit/ade4f4ba8b) [#36778](https://github.com/sgl-project/sglang/pull/36778)
  fix: report the real backend for non-CUDA CI registrations in /rerun-test (#36778)
  _Files: `scripts/ci/utils/slash_command_handler.py`_
- **2026-08-28** [`fcb4ff1ee3`](https://github.com/sgl-project/sglang/commit/fcb4ff1ee3) [#36433](https://github.com/sgl-project/sglang/pull/36433)
  [NPU] Update sgl-kernel-npu version (#36433)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-08-28** [`6ff2fe6a6a`](https://github.com/sgl-project/sglang/commit/6ff2fe6a6a) [#36775](https://github.com/sgl-project/sglang/pull/36775)
  CI: split JIT kernel unit tests into two partitions (#36775)
  _Files: `.github/workflows/pr-test-jit-kernel.yml`_
- **2026-08-28** [`9cee0a31d1`](https://github.com/sgl-project/sglang/commit/9cee0a31d1) [#35290](https://github.com/sgl-project/sglang/pull/35290)
  [XPU] Lazily import tvm_ffi-dependent all_reduce kernel in minimax_m2 (#35290)
  _Files: `python/sglang/srt/models/minimax_m2.py`_
- **2026-08-28** [`26fd7fdaa2`](https://github.com/sgl-project/sglang/commit/26fd7fdaa2) [#35451](https://github.com/sgl-project/sglang/pull/35451)
  [Feature] Support PP in full prefill CUDA graphs (#35451)
  _Files: `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_utils/buffers.py` _+4 more__
- **2026-08-27** [`0132848349`](https://github.com/sgl-project/sglang/commit/0132848349) [#34842](https://github.com/sgl-project/sglang/pull/34842)
  Revert "[Fix] Disable --enable-symm-mem under CUDA graphs on Kimi hybrid models" (#34842)
  _Files: `python/sglang/srt/arg_groups/kimi_k3_hook.py`, `python/sglang/srt/server_args.py`_
- **2026-08-27** [`7c3b5a6732`](https://github.com/sgl-project/sglang/commit/7c3b5a6732) [#36725](https://github.com/sgl-project/sglang/pull/36725)
  config: every handler declares its cuda-graph decisions (#36725)
  _Files: `python/sglang/srt/hardware_backend/npu/utils.py`, `python/sglang/srt/model_executor/cuda_graph_config.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_resolution_declarations.py` _+1 more__
- **2026-08-26** [`7f27bf4708`](https://github.com/sgl-project/sglang/commit/7f27bf4708) [#36465](https://github.com/sgl-project/sglang/pull/36465)
  [Kernel] Declare the PyTorch ABI dependency in sglang-kernel wheels (#36465)
  _Files: `python/sglang/kernels/aot/pyproject.toml`_
- **2026-08-25** [`1fa32d50e1`](https://github.com/sgl-project/sglang/commit/1fa32d50e1) [#32166](https://github.com/sgl-project/sglang/pull/32166)
  [XPU] Use SYCL kernels for DeepSeek V4 MHC on XPU (#32166)
  _Files: `python/sglang/kernels/ops/layernorm/mhc.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-08-24** [`acba8921bf`](https://github.com/sgl-project/sglang/commit/acba8921bf) [#33840](https://github.com/sgl-project/sglang/pull/33840)
  [XPU] Support softmax_lse in sgl_kernel::fwd API (#33840)
  _Files: `python/sglang/srt/hardware_backend/xpu/graph_runner/xpu_graph_runner.py`_
- **2026-08-24** [`fd73d4b019`](https://github.com/sgl-project/sglang/commit/fd73d4b019) [#35506](https://github.com/sgl-project/sglang/pull/35506)
  [CPU] Add graph register for fused_sigmoid_mul_cpu, fused_qk_gemma_rmsnorm (#35506)
  _Files: `python/sglang/kernels/aot/csrc/cpu/activation.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/models/qwen3_5.py` _+1 more__

## Scheduler / Batching  (13 commits)

- **2026-08-30** [`d249672ad3`](https://github.com/sgl-project/sglang/commit/d249672ad3) [#37070](https://github.com/sgl-project/sglang/pull/37070)
  Scatter mm embeddings with row index_copy_ instead of masked_scatter_ to cut transient GPU memory (#37070)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `test/registered/unit/managers/test_mm_embed_scatter.py`_
- **2026-08-29** [`6afb5e1771`](https://github.com/sgl-project/sglang/commit/6afb5e1771) [#36205](https://github.com/sgl-project/sglang/pull/36205)
  Gate the idle-loop tree-cache sanity check behind a default-off env (#36205)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `test/registered/unit/managers/scheduler_components/test_invariant_checker.py`_
- **2026-08-28** [`70088aa5db`](https://github.com/sgl-project/sglang/commit/70088aa5db) [#36638](https://github.com/sgl-project/sglang/pull/36638)
  Fix KeyError on batch requests whose state is freed before it is read (#36638)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
- **2026-08-28** [`6480cce9bc`](https://github.com/sgl-project/sglang/commit/6480cce9bc) [#36568](https://github.com/sgl-project/sglang/pull/36568)
  perf: skip redundant scheduler metadata gather for DP1 (#36568)
  _Files: `python/sglang/srt/managers/scheduler_components/dp_attn.py`, `test/registered/unit/managers/scheduler_components/test_dp_attn.py`_
- **2026-08-27** [`a0a2295271`](https://github.com/sgl-project/sglang/commit/a0a2295271) [#36676](https://github.com/sgl-project/sglang/pull/36676)
  Refactor server_args constants and layout (#36676)
  _Files: `python/sglang/srt/constants.py`, `python/sglang/srt/managers/scheduler_components/logprob_result_processor.py`, `python/sglang/srt/managers/tokenizer_manager_score_mixin.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-08-27** [`78d36f5f62`](https://github.com/sgl-project/sglang/commit/78d36f5f62) [#36589](https://github.com/sgl-project/sglang/pull/36589)
  fix: kill_process_tree waits for the reap by default (#36589)
  _Files: `python/sglang/lang/backend/runtime_endpoint.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/utils/common.py`_
- **2026-08-24** [`d10a656ad8`](https://github.com/sgl-project/sglang/commit/d10a656ad8) [#36203](https://github.com/sgl-project/sglang/pull/36203)
  Cleanup duplicate mamba backup helper (#36203)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-08-24** [`e586a6f2c5`](https://github.com/sgl-project/sglang/commit/e586a6f2c5) [#35929](https://github.com/sgl-project/sglang/pull/35929)
  Report the whole server's world size in the scheduler's internal state (#35929)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/managers/test_scheduler_internal_state_env_vars.py`, `test/registered/unit/managers/test_scheduler_internal_state_world_size.py`_
- **2026-08-24** [`6dd79576cd`](https://github.com/sgl-project/sglang/commit/6dd79576cd) [#35928](https://github.com/sgl-project/sglang/pull/35928)
  Expose the declared sglang env vars of a scheduler in its internal state (#35928)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_internal_state_env_vars.py`_
- **2026-08-24** [`981dfa2b83`](https://github.com/sgl-project/sglang/commit/981dfa2b83) [#35925](https://github.com/sgl-project/sglang/pull/35925)
  Make the scheduler track the published weight version (#35925)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/weight_updater.py` _+2 more__
- **2026-08-24** [`02a3dca738`](https://github.com/sgl-project/sglang/commit/02a3dca738) [#35924](https://github.com/sgl-project/sglang/pull/35924)
  Extract _make_abort_req from the scheduler's abort paths (#35924)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-08-24** [`a37fdae562`](https://github.com/sgl-project/sglang/commit/a37fdae562) [#35923](https://github.com/sgl-project/sglang/pull/35923)
  Extract collect_inflight_reqs from abort_request for reusing (#35923)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-08-24** [`fb6e3872e1`](https://github.com/sgl-project/sglang/commit/fb6e3872e1) [#36005](https://github.com/sgl-project/sglang/pull/36005)
  [Mamba] fix mamba index h unexpected assertion for dcp (#36005)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_

## Models  (10 commits)

- **2026-08-31** [`63b2adbeac`](https://github.com/sgl-project/sglang/commit/63b2adbeac) [#36459](https://github.com/sgl-project/sglang/pull/36459)
  [NPU] Fix evalscope accuracy parsing and add glm5_1 aime26 request timeout (#36459)
  _Files: `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`, `test/registered/npu/accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py`, `test/registered/npu/accuracy/qwen3_next_80b_a3b_instruct/test_npu_qwen3_next_80b_w8a8_2p_in6k_out1k5_bs16_aime25.py`, `test/registered/npu/performance/kimi_k2_6/test_npu_kimi_k2_6_w4a8_16p_in64k_out1k_100ms.py`_
- **2026-08-31** [`4dc7dc8518`](https://github.com/sgl-project/sglang/commit/4dc7dc8518) [#35244](https://github.com/sgl-project/sglang/pull/35244)
  [Fix] Transformers-fallback (GPT-NeoX) + KV pool config (DeepSeek-VL2) (#35244)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/transformers.py`, `test/registered/unit/configs/test_model_config_shapes.py`, `test/registered/unit/model_loader/test_transformers_fallback.py`_
- **2026-08-29** [`a25df83fe3`](https://github.com/sgl-project/sglang/commit/a25df83fe3) [#36977](https://github.com/sgl-project/sglang/pull/36977)
  [Cookbook] Run accuracy benchmarks through sgl-eval (#36977)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`, `docs/cookbook/autoregressive/MiniMax/MiniMax-M2.7.mdx`, `docs/cookbook/autoregressive/Moonshotai/Kimi-K2.6.mdx`_
- **2026-08-28** [`b7686e17d6`](https://github.com/sgl-project/sglang/commit/b7686e17d6) [#36211](https://github.com/sgl-project/sglang/pull/36211)
  [k3] declare packed_modules_mapping on `KimiK3ForConditionalGeneration` (#36211)
  _Files: `python/sglang/srt/models/kimi_k3.py`_
- **2026-08-28** [`84a6f51bd6`](https://github.com/sgl-project/sglang/commit/84a6f51bd6) [#36547](https://github.com/sgl-project/sglang/pull/36547)
  Fix DeepSeek V4 multistream QKV buffer lifetime (#36547)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-08-26** [`db15976fe9`](https://github.com/sgl-project/sglang/commit/db15976fe9) [#36419](https://github.com/sgl-project/sglang/pull/36419)
  Fix DSV4 DSpark sample-from-anchor initialization (#36419)
  _Files: `python/sglang/srt/models/deepseek_v4_dspark.py`_
- **2026-08-26** [`4382947b58`](https://github.com/sgl-project/sglang/commit/4382947b58) [#36424](https://github.com/sgl-project/sglang/pull/36424)
  Fix DSV4 shared-fusion CPU unit test after the EP guard landed (#36424)
  _Files: `test/registered/unit/models/test_deepseek_v4_shared_expert_fusion.py`_
- **2026-08-25** [`d2d8ecea77`](https://github.com/sgl-project/sglang/commit/d2d8ecea77) [#36180](https://github.com/sgl-project/sglang/pull/36180)
  [npu] Combine NPU test fixes from #35472 and #34516 (#36180)
  _Files: `.github/workflows/pr-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`, `python/sglang/test/ascend/e2e/test_npu_multi_node_utils.py`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py` _+3 more__
- **2026-08-24** [`5030637c65`](https://github.com/sgl-project/sglang/commit/5030637c65) [#36020](https://github.com/sgl-project/sglang/pull/36020)
  [docs] Split the Qwen3.8-27B NVFP4 cells by lm_head precision (#36020)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/_qwen38_mamba_ratio_calculator.jsx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b-benchmarks.jsx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b.jsx`_
- **2026-08-24** [`0c1e9bda57`](https://github.com/sgl-project/sglang/commit/0c1e9bda57) [#35915](https://github.com/sgl-project/sglang/pull/35915)
  [OpenAI] Drop empty assistant turns for mistral_common tokenizers (#35915)
  _Files: `python/sglang/srt/utils/hf_transformers/mistral_utils.py`, `test/registered/unit/tokenizer/test_mistral_empty_assistant.py`_

## Docs / Examples  (10 commits)

- **2026-08-29** [`000c636342`](https://github.com/sgl-project/sglang/commit/000c636342) [#37050](https://github.com/sgl-project/sglang/pull/37050)
  docs: state that HiCache L2 is instance-private and only L3 is shared (#37050)
  _Files: `docs/docs/advanced_features/hicache_best_practices.mdx`, `docs/docs/advanced_features/hicache_design.mdx`_
- **2026-08-28** [`395c2258c3`](https://github.com/sgl-project/sglang/commit/395c2258c3) [#36827](https://github.com/sgl-project/sglang/pull/36827)
  [Docs] Add GLM-5.3 cookbook (#36827)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`, `docs/docs.json`, `docs/src/snippets/configs/zai-org/glm-5.3-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3.jsx`_
- **2026-08-28** [`989e51ba9c`](https://github.com/sgl-project/sglang/commit/989e51ba9c) [#36823](https://github.com/sgl-project/sglang/pull/36823)
  [Docs] Rename Tencent cookbook page titles to "Hy4 preview" / "Hy3 preview" (#36823)
  _Files: `docs/cookbook/autoregressive/Tencent/Hunyuan3-Preview.mdx`, `docs/cookbook/autoregressive/Tencent/Hy4-Preview.mdx`_
- **2026-08-28** [`2960d69622`](https://github.com/sgl-project/sglang/commit/2960d69622) [#36808](https://github.com/sgl-project/sglang/pull/36808)
  [Cookbook] Hy4-Preview follow-ups: runtime-accurate recipes + released-model info (#36808)
  _Files: `docs/cookbook/autoregressive/Tencent/Hy4-Preview.mdx`, `docs/src/snippets/configs/tencent/hy4-preview.jsx`_
- **2026-08-28** [`1948b61ad4`](https://github.com/sgl-project/sglang/commit/1948b61ad4) [#36804](https://github.com/sgl-project/sglang/pull/36804)
  [Cookbook] Add the Hy4-Preview model page (Tencent) (#36804)
  _Files: `docs/cookbook/autoregressive/Tencent/Hy3.mdx`, `docs/cookbook/autoregressive/Tencent/Hy4-Preview.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-08-27** [`e6c1a3cd4c`](https://github.com/sgl-project/sglang/commit/e6c1a3cd4c) [#35416](https://github.com/sgl-project/sglang/pull/35416)
  docs: sync LMSYS SGLang blog cards (#35416)
  _Files: `docs/index.mdx`_
- **2026-08-26** [`abe3aeb142`](https://github.com/sgl-project/sglang/commit/abe3aeb142) [#36325](https://github.com/sgl-project/sglang/pull/36325)
  [NPU] [DOC] Update CANN version in NPU installation docs (#36325)
  _Files: `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`_
- **2026-08-25** [`99c02d71b1`](https://github.com/sgl-project/sglang/commit/99c02d71b1) [#36342](https://github.com/sgl-project/sglang/pull/36342)
  docs(cookbook): use auto parser resolution for Granite 4.2 (#36342)
  _Files: `docs/cookbook/autoregressive/IBM/Granite-4.2.mdx`, `docs/src/snippets/configs/ibm-granite/granite-4.2.jsx`_
- **2026-08-25** [`b760f7fb19`](https://github.com/sgl-project/sglang/commit/b760f7fb19) [#36286](https://github.com/sgl-project/sglang/pull/36286)
  docs(cookbook): add IBM Granite 4.2 cookbook (#36286)
  _Files: `docs/cards/logos/ibm.png`, `docs/cookbook/autoregressive/IBM/Granite-4.2.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-08-24** [`11b1b4c374`](https://github.com/sgl-project/sglang/commit/11b1b4c374) [#36123](https://github.com/sgl-project/sglang/pull/36123)
  [NPU] [DOC] Polish English wording in NPU docs (#36123)
  _Files: `docs/docs/developer_guide/msprobe_debugging_guide.mdx`, `docs/docs/hardware-platforms/ascend-npus/development/support_new_models.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/environment_variables.mdx`_

## Tensor / Data Parallel  (9 commits)

- **2026-08-29** [`3a0f1a1344`](https://github.com/sgl-project/sglang/commit/3a0f1a1344) [#29100](https://github.com/sgl-project/sglang/pull/29100)
  [NPU] fix: reach torch>=2.8 CUDA memory-pool APIs lazily via torch._C (#29100)
  _Files: `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/arg_groups/platform_hook.py`, `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`, `test/registered/unit/distributed/test_pynccl_allocator_import.py`_
- **2026-08-29** [`48b88e1256`](https://github.com/sgl-project/sglang/commit/48b88e1256) [#36896](https://github.com/sgl-project/sglang/pull/36896)
  config: the resolution pipeline's dispatcher leaves the record (#36896)
  _Files: `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/arg_groups/platform_hook.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_model_config_reads_resolved_input.py` _+3 more__
- **2026-08-29** [`3904b309db`](https://github.com/sgl-project/sglang/commit/3904b309db) [#36920](https://github.com/sgl-project/sglang/pull/36920)
  Add configurable HTTP/2 connection window (#36920)
  _Files: `python/sglang/srt/arg_groups/serving_hook.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/entrypoints/test_http2_server_config.py`_
- **2026-08-29** [`505228823f`](https://github.com/sgl-project/sglang/commit/505228823f) [#36940](https://github.com/sgl-project/sglang/pull/36940)
  [NPU] [DOC] udpate supported features on NPU (#36940)
  _Files: `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_models.mdx`_
- **2026-08-26** [`1eb629ab4f`](https://github.com/sgl-project/sglang/commit/1eb629ab4f) [#36397](https://github.com/sgl-project/sglang/pull/36397)
  [NVIDIA] Tune custom all reduce v2 for sm_107 (#36397)
  _Files: `python/sglang/srt/distributed/device_communicators/configs/custom_all_reduce_v2.py`_
- **2026-08-24** [`0d5b5ae620`](https://github.com/sgl-project/sglang/commit/0d5b5ae620) [#35719](https://github.com/sgl-project/sglang/pull/35719)
  [AMD] Fix Qwen3.5 MTP dropping fused shared-expert weights (#35719)
  _Files: `python/sglang/srt/models/qwen3_5_mtp.py`_
- **2026-08-24** [`c56cee0f80`](https://github.com/sgl-project/sglang/commit/c56cee0f80) [#35927](https://github.com/sgl-project/sglang/pull/35927)
  Support gated launch to defer startup memory allocation (#35927)
  _Files: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/gated_launch.py`, `python/sglang/srt/server_args.py`, `test/registered/core/test_gated_launch.py` _+1 more__
- **2026-08-24** [`1daa94a069`](https://github.com/sgl-project/sglang/commit/1daa94a069) [#32856](https://github.com/sgl-project/sglang/pull/32856)
  [CPU] Fix NUMA/core binding for DP ranks (#32856)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/utils/numa_utils.py`, `test/registered/cpu/test_binding.py`_
- **2026-08-24** [`167c339c8e`](https://github.com/sgl-project/sglang/commit/167c339c8e) [#35669](https://github.com/sgl-project/sglang/pull/35669)
  [CPU] Add check for fused_input_proj in TP=4 (#35669)
  _Files: `python/sglang/srt/models/qwen3_5.py`_

## Speculative Decoding  (4 commits)

- **2026-08-31** [`3ed3326631`](https://github.com/sgl-project/sglang/commit/3ed3326631) [#36897](https://github.com/sgl-project/sglang/pull/36897)
  Decouple speculative draft capacity from runtime state (#36897)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/runtime_context.py`, `python/sglang/srt/speculative/spec_info.py`, `python/sglang/srt/speculative/spec_registry.py` _+2 more__
- **2026-08-29** [`0df69849ba`](https://github.com/sgl-project/sglang/commit/0df69849ba) [#36934](https://github.com/sgl-project/sglang/pull/36934)
  [Fix] Drop the duplicated DSpark draft sample_block call (#36934)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_draft_sampler.py`_
- **2026-08-27** [`08315c56df`](https://github.com/sgl-project/sglang/commit/08315c56df) [#34053](https://github.com/sgl-project/sglang/pull/34053)
  [Fix] Account resident weight memory in KV sizing (#34053)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_loader/loader.py` _+5 more__
- **2026-08-25** [`3bc1c580c6`](https://github.com/sgl-project/sglang/commit/3bc1c580c6) [#35672](https://github.com/sgl-project/sglang/pull/35672)
  [AMD] Enable draft_extend CUDA graph for HIP DSA backend (#35672)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`_

## Structured Output  (3 commits)

- **2026-08-26** [`ffc431cd4c`](https://github.com/sgl-project/sglang/commit/ffc431cd4c) [#36464](https://github.com/sgl-project/sglang/pull/36464)
  [CI] Fix stale tool_call_parser key in Spark2.5 detector test (#36464)
  _Files: `test/registered/unit/function_call/test_spark25_detector.py`_
- **2026-08-26** [`7ef49e8f7d`](https://github.com/sgl-project/sglang/commit/7ef49e8f7d) [#36416](https://github.com/sgl-project/sglang/pull/36416)
  Rename Spark3 to Spark2.5 (#36416)
  _Files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/spark2_5.py`, `python/sglang/srt/function_call/function_call_parser.py`, `python/sglang/srt/function_call/spark25_detector.py` _+3 more__
- **2026-08-25** [`0c42a44cd7`](https://github.com/sgl-project/sglang/commit/0c42a44cd7) [#35963](https://github.com/sgl-project/sglang/pull/35963)
  Add Spark3 Model (#35963)
  _Files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/spark3.py`, `python/sglang/srt/function_call/function_call_parser.py`, `python/sglang/srt/function_call/spark3_detector.py` _+3 more__

## Serving / API  (2 commits)

- **2026-08-31** [`6580d5cd9a`](https://github.com/sgl-project/sglang/commit/6580d5cd9a) [#36101](https://github.com/sgl-project/sglang/pull/36101)
  weight cache: key daemon paths by GPU UUID (#36101)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/model_runner_components/load_model_utils.py` _+7 more__
- **2026-08-30** [`032fe91bf1`](https://github.com/sgl-project/sglang/commit/032fe91bf1) [#37054](https://github.com/sgl-project/sglang/pull/37054)
  Handle unlimited tokenizer context lengths (#37054)
  _Files: `python/sglang/srt/entrypoints/openai/serving_tokenize.py`_

## LoRA  (1 commits)

- **2026-08-25** [`f2ef826f0c`](https://github.com/sgl-project/sglang/commit/f2ef826f0c) [#32031](https://github.com/sgl-project/sglang/pull/32031)
  [NPU]Fix run_lora_a_embedding out-of-vocab token produces wrong embedding. (#32031)
  _Files: `python/sglang/srt/lora/backend/ascend_backend.py`_

---
_Generated 2026-08-31 16:05 UTC_