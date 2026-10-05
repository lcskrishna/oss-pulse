# sgl-project/sglang — Weekly Change Report
**Period:** 2026-09-28 → 2026-10-05  |  **Total commits:** 430

## ✨ New Features This Week

- **2026-10-05** [#41832](https://github.com/sgl-project/sglang/pull/41832) — [diffusion] feat: recycle warmup-only entries of conditioning-cache at the first served store (#41832)
- **2026-10-05** [#37549](https://github.com/sgl-project/sglang/pull/37549) — [diffusion] feat: support --async-output-save to overlap output saving with the next request (#37549)
- **2026-10-05** [#35857](https://github.com/sgl-project/sglang/pull/35857) — [diffusion] feat: add community LoRA recipes and Kohya mapping (#35857)
- **2026-10-05** [#42429](https://github.com/sgl-project/sglang/pull/42429) — [sgl-router] Add reorg bucket config with per-group admission (#42429)
- **2026-10-05** [#37261](https://github.com/sgl-project/sglang/pull/37261) — [Feature] DeepEP v2: expanded (do_expand=True) prefill dispatch (#37261)
- **2026-10-04** [#36780](https://github.com/sgl-project/sglang/pull/36780) — [Apple Silicon] Add an Apple Silicon (MPS) platform to the standard Torch model runner (#36780)
- **2026-10-04** [#42171](https://github.com/sgl-project/sglang/pull/42171) — [diffusion] feat: enable cuda graphs for observation encoding and denoising steps for action models (#42171)
- **2026-10-04** [#42174](https://github.com/sgl-project/sglang/pull/42174) — [diffusion] feat: load ComfyUI/ai-toolkit fused `gate_up` LoRAs and diffusers metadata alpha for qwen-image-2.1 (#42174)
- **2026-10-04** [#41797](https://github.com/sgl-project/sglang/pull/41797) — [diffusion] feat: let requests choose the video libx264 preset (#41797)
- **2026-10-04** [#40190](https://github.com/sgl-project/sglang/pull/40190) — [XPU] Enable fused QK-norm + RoPE for Qwen3-MoE (#40190)
- _…and 63 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-05** [`b3f967e809`](https://github.com/sgl-project/sglang/commit/b3f967e809) [#41282](https://github.com/sgl-project/sglang/pull/41282) — Revert "Revert "[AMD][ROCm] Keep cos_sin_cache fp32 on HIP for fused QSA indexer kernel (#41282)"" (#42558)
- **2026-10-05** [`c41b2d26e5`](https://github.com/sgl-project/sglang/commit/c41b2d26e5) [#28650](https://github.com/sgl-project/sglang/pull/28650) — [diffusion][ROCm][Perf]: Set gfx942 AITER FMHA rounding mode to rtz instead of rtna (#28650)
- **2026-10-05** [`456d533e61`](https://github.com/sgl-project/sglang/commit/456d533e61) [#41282](https://github.com/sgl-project/sglang/pull/41282) — Revert "[AMD][ROCm] Keep cos_sin_cache fp32 on HIP for fused QSA indexer kernel (#41282)" (#42541)
- **2026-10-04** [`b792228b35`](https://github.com/sgl-project/sglang/commit/b792228b35) [#39931](https://github.com/sgl-project/sglang/pull/39931) — [ROCm] topk v2: split one long row across blocks, the CDNA cluster-path equivalent (#39931)
- **2026-10-04** [`aa0ce20201`](https://github.com/sgl-project/sglang/commit/aa0ce20201) [#41725](https://github.com/sgl-project/sglang/pull/41725) — [ROCm] GLM-5.2 decode path: decode-shaped MoE/MLA tiles, split speculative softmax, and bf16 GEMM routing (#41725)
- **2026-10-04** [`7a719e9a65`](https://github.com/sgl-project/sglang/commit/7a719e9a65) [#42494](https://github.com/sgl-project/sglang/pull/42494) — [AMD] Fix RoPE cache dtype and diffusion CI failures (#42494)
- **2026-10-04** [`0343bc1483`](https://github.com/sgl-project/sglang/commit/0343bc1483) [#42512](https://github.com/sgl-project/sglang/pull/42512) — [AMD][Docs] fix mori io and umbp playground (#42512)
- **2026-10-04** [`ab9d8f029c`](https://github.com/sgl-project/sglang/commit/ab9d8f029c) [#41405](https://github.com/sgl-project/sglang/pull/41405) — [AMD][DI][CI] mi355x spur: skip RDMA ports that are not PORT_ACTIVE; dump driver log on failure (#41405)
- **2026-10-04** [`bc5a055dd7`](https://github.com/sgl-project/sglang/commit/bc5a055dd7) [#42391](https://github.com/sgl-project/sglang/pull/42391) — [diffusion] move kernel validation into launchers and simplify dispatch (#42391)
- **2026-10-04** [`29bcb74a89`](https://github.com/sgl-project/sglang/commit/29bcb74a89) [#42461](https://github.com/sgl-project/sglang/pull/42461) — [AMD][CI] Fix ROCm kernel wheel sources: drop eagle_utils, add DSV4 kernels (#42461)
- **2026-10-04** [`6cc661f223`](https://github.com/sgl-project/sglang/commit/6cc661f223) [#34438](https://github.com/sgl-project/sglang/pull/34438) — [AMD][DCP 2/N] Enable aiter asm ps for kimi k3 prefill (#34438)
- **2026-10-04** [`4611ea365e`](https://github.com/sgl-project/sglang/commit/4611ea365e) [#38480](https://github.com/sgl-project/sglang/pull/38480) — [HiCache]: Fix host lock ownership across radix splits (#38480)
- **2026-10-04** [`ff219e159e`](https://github.com/sgl-project/sglang/commit/ff219e159e) [#35357](https://github.com/sgl-project/sglang/pull/35357) — [AMD] MiniMax-M3: fuse sparse QK norm, RoPE and cache writes with AITER (#35357)
- **2026-10-04** [`f2385314b2`](https://github.com/sgl-project/sglang/commit/f2385314b2) [#41476](https://github.com/sgl-project/sglang/pull/41476) — [AMD] Add DeepSeek-V4.1-Flash MI35x nightly accuracy test (#41476)
- **2026-10-04** [`663984b5a1`](https://github.com/sgl-project/sglang/commit/663984b5a1) [#41931](https://github.com/sgl-project/sglang/pull/41931) — [AMD] Keep aiter's tuned GEMM for the DeepSeek-V4 compressors (#41931)
- **2026-10-04** [`71dc292b97`](https://github.com/sgl-project/sglang/commit/71dc292b97) [#41707](https://github.com/sgl-project/sglang/pull/41707) — [AMD] Use AITER ASM prefill for MiniMax-M3 HD128 attention (#41707)
- **2026-10-03** [`10edb05e72`](https://github.com/sgl-project/sglang/commit/10edb05e72) [#42348](https://github.com/sgl-project/sglang/pull/42348) — [Refactor] Let the remaining placement consumers read the parallel context (#42348)
- **2026-10-03** [`061e712bab`](https://github.com/sgl-project/sglang/commit/061e712bab) [#42427](https://github.com/sgl-project/sglang/pull/42427) — chore: bump sgl-kernel version to 0.4.9 (#42427)
- **2026-10-03** [`e83c95b650`](https://github.com/sgl-project/sglang/commit/e83c95b650) [#39950](https://github.com/sgl-project/sglang/pull/39950) — [AMD] Fix AITER weight slicing for CP decode TP (#39950)
- **2026-10-03** [`f327f92424`](https://github.com/sgl-project/sglang/commit/f327f92424) [#34200](https://github.com/sgl-project/sglang/pull/34200) — [AMD] Port CP V2 to the DeepSeek-V4 HIP backend (#34200)
- **2026-10-03** [`7be5e3473c`](https://github.com/sgl-project/sglang/commit/7be5e3473c) [#42312](https://github.com/sgl-project/sglang/pull/42312) — [Refactor] Drop the reduction-skip mechanisms stage boundaries no longer use (#42312)
- **2026-10-03** [`8293f9af54`](https://github.com/sgl-project/sglang/commit/8293f9af54) [#37077](https://github.com/sgl-project/sglang/pull/37077) — [PD] Centralize drain-aware abort acknowledgements (#37077)
- **2026-10-03** [`af1bef3eaf`](https://github.com/sgl-project/sglang/commit/af1bef3eaf) [#41870](https://github.com/sgl-project/sglang/pull/41870) — [AMD] GLM-5.3-Flash: fuse shared expert and KDA projections on Quark MXFP4 (#41870)
- **2026-10-02** [`cbe070b6bf`](https://github.com/sgl-project/sglang/commit/cbe070b6bf) [#42278](https://github.com/sgl-project/sglang/pull/42278) — [Docs][AMD] Update GLM-5.2 MI355X daily image to 20260930 (#42278)
- **2026-10-02** [`b69a5f296a`](https://github.com/sgl-project/sglang/commit/b69a5f296a) [#41488](https://github.com/sgl-project/sglang/pull/41488) — [AMD] Add opt-in MiniMax-M3 TP4 indexer context partitioning (#41488)
- **2026-10-02** [`f6fcda8827`](https://github.com/sgl-project/sglang/commit/f6fcda8827) [#41282](https://github.com/sgl-project/sglang/pull/41282) — [AMD][ROCm] Keep cos_sin_cache fp32 on HIP for fused QSA indexer kernel (#41282)
- **2026-10-02** [`a74f259f38`](https://github.com/sgl-project/sglang/commit/a74f259f38) [#42055](https://github.com/sgl-project/sglang/pull/42055) — [AMD][V4.1][*/N] Fuse MXFP8 activation quant into producer kernels on gfx950 (#42055)
- **2026-10-02** [`2cd92d10b9`](https://github.com/sgl-project/sglang/commit/2cd92d10b9) [#42219](https://github.com/sgl-project/sglang/pull/42219) — [AMD] Skip the AITER #6042/#5967 patches on gfx1250 (#42219)
- **2026-10-02** [`e020b389b6`](https://github.com/sgl-project/sglang/commit/e020b389b6) [#41973](https://github.com/sgl-project/sglang/pull/41973) — [AMD][CI] Partition stage-b-test-1-gpu-small-amd-mi35x to stop the 30-min timeout (#41973)
- **2026-10-02** [`544e46c080`](https://github.com/sgl-project/sglang/commit/544e46c080) [#41979](https://github.com/sgl-project/sglang/pull/41979) — [AMD][CI] Fix VLM MMMU nightly max_tokens for CoT prompt (#41979)
- **2026-10-02** [`d61a9c28ba`](https://github.com/sgl-project/sglang/commit/d61a9c28ba) [#42013](https://github.com/sgl-project/sglang/pull/42013) — chore: bump docs install version to 0.5.21 (#42013)
- **2026-10-02** [`58f0d250ec`](https://github.com/sgl-project/sglang/commit/58f0d250ec) [#41533](https://github.com/sgl-project/sglang/pull/41533) — [ROCm] Use the fused MLA absorb + RoPE + KV-write kernel for decode-sized forward modes only (#41533)
- **2026-10-02** [`29f6d408c0`](https://github.com/sgl-project/sglang/commit/29f6d408c0) [#42011](https://github.com/sgl-project/sglang/pull/42011) — [AMD][V4.1][*/N] Fix shared-expert fusion accuracy and speed up MoE routing on ROCm (#42011)
- **2026-10-02** [`2a3655fea1`](https://github.com/sgl-project/sglang/commit/2a3655fea1) [#40331](https://github.com/sgl-project/sglang/pull/40331) — [unified-memory] Name the fused KV translate for what it computes (7/7) (#40331)
- **2026-10-02** [`9855e9c6f8`](https://github.com/sgl-project/sglang/commit/9855e9c6f8) [#40329](https://github.com/sgl-project/sglang/pull/40329) — [unified-memory] Remove the kernel-page multiplier plumbing (5/7) (#40329)
- **2026-10-02** [`4c4e352a4b`](https://github.com/sgl-project/sglang/commit/4c4e352a4b) [#40328](https://github.com/sgl-project/sglang/pull/40328) — [unified-memory] Mark the write loc physical and check it at every write door (4/7) (#40328)
- **2026-10-01** [`f17f7705a5`](https://github.com/sgl-project/sglang/commit/f17f7705a5) [#39273](https://github.com/sgl-project/sglang/pull/39273) — [AMD] [GLM-5.3-Flash] Enable FP8 and MXFP4 serving on gfx950 (#39273)
- **2026-10-01** [`d669efba84`](https://github.com/sgl-project/sglang/commit/d669efba84) [#41981](https://github.com/sgl-project/sglang/pull/41981) — [AMD][V4.1][*/N] Greedy dspark draft/accept under SGLANG_SIMULATE_ACC_LEN (#41981)
- **2026-10-01** [`3c4e218779`](https://github.com/sgl-project/sglang/commit/3c4e218779) [#42017](https://github.com/sgl-project/sglang/pull/42017) — [AMD][V4.1][*/N] OPUS sparse prefill on gfx950 through layout conversion (#42017)
- **2026-10-01** [`f45c004e18`](https://github.com/sgl-project/sglang/commit/f45c004e18) [#42014](https://github.com/sgl-project/sglang/pull/42014) — [AMD][V4.1][*/N] Build DSpark draft metadata inside the CUDA graph on ROCm (#42014)
- **2026-10-01** [`73ba6513f4`](https://github.com/sgl-project/sglang/commit/73ba6513f4) [#41970](https://github.com/sgl-project/sglang/pull/41970) — [AMD][V4.1][*/N] Switch the fp8 dense GEMMs on gfx950 to aiter's MXFP8 GEMM (#41970)
- **2026-10-01** [`0224fcbd1c`](https://github.com/sgl-project/sglang/commit/0224fcbd1c) [#41947](https://github.com/sgl-project/sglang/pull/41947) — [AMD][V4.1][*/N] Route low-ratio indexer and candidate-block top-k through top-k v2 (#41947)
- **2026-10-01** [`5fab1f0f51`](https://github.com/sgl-project/sglang/commit/5fab1f0f51) [#42018](https://github.com/sgl-project/sglang/pull/42018) — [Fix] Let the aiter DCP ASM decode test run without aiter (#42018)
- **2026-10-01** [`69240ba7d6`](https://github.com/sgl-project/sglang/commit/69240ba7d6) [#41971](https://github.com/sgl-project/sglang/pull/41971) — [AMD][V4.1][*/N] Pick the gfx950 wo_a batched gemm tile by row count (#41971)
- **2026-10-01** [`ffb134188b`](https://github.com/sgl-project/sglang/commit/ffb134188b) [#42023](https://github.com/sgl-project/sglang/pull/42023) — [AMD] Update aiter version for v41 (#42023)
- **2026-10-01** [`9c3262d855`](https://github.com/sgl-project/sglang/commit/9c3262d855) [#39166](https://github.com/sgl-project/sglang/pull/39166) — [AMD][DSV4] feat: enable PD-disagg with fp8 unified_kv on gfx950 (#39166)
- **2026-10-01** [`99c9d65b32`](https://github.com/sgl-project/sglang/commit/99c9d65b32) [#40750](https://github.com/sgl-project/sglang/pull/40750) — [AMD] AITER MLA DCP decode ASM path (opt-in) (#40750)
- **2026-10-01** [`f02828ea39`](https://github.com/sgl-project/sglang/commit/f02828ea39) [#40471](https://github.com/sgl-project/sglang/pull/40471) — fix(dsv4): ship the fp8 unified_kv rope pool through the direct external linker (#40471)
- **2026-10-01** [`0148d9a2fd`](https://github.com/sgl-project/sglang/commit/0148d9a2fd) [#41497](https://github.com/sgl-project/sglang/pull/41497) — [AMD] Fix MiniMax-M3 EAGLE3 verification on ROCm (#41497)
- **2026-10-01** [`6af651ea0c`](https://github.com/sgl-project/sglang/commit/6af651ea0c) [#40811](https://github.com/sgl-project/sglang/pull/40811) — [AMD][Quark] Serve the Kimi-K3 MXFP4 checkpoint on ROCm (#40811)
- **2026-09-30** [`986cb8268b`](https://github.com/sgl-project/sglang/commit/986cb8268b) [#41817](https://github.com/sgl-project/sglang/pull/41817) — [Refactor] Enter draft TP scopes by attention ownership and drop ModelRunner.tp_group (#41817)
- **2026-09-30** [`ecc0f0dec2`](https://github.com/sgl-project/sglang/commit/ecc0f0dec2) [#41808](https://github.com/sgl-project/sglang/pull/41808) — [Fix] Pass the draft's attention ownership to DFLASH's eager LiLiCorr scope (#41808)
- **2026-09-30** [`547286bb5a`](https://github.com/sgl-project/sglang/commit/547286bb5a) [#39012](https://github.com/sgl-project/sglang/pull/39012) — [Deps] Bump transformers to 5.17.0 (#39012)
- **2026-09-30** [`3a398442bf`](https://github.com/sgl-project/sglang/commit/3a398442bf) [#41308](https://github.com/sgl-project/sglang/pull/41308) — dsv4.1-amd: serve DeepSeek-V4.1 on gfx950 (#41308)
- **2026-09-30** [`47dcde70f4`](https://github.com/sgl-project/sglang/commit/47dcde70f4) [#41849](https://github.com/sgl-project/sglang/pull/41849) — [Docs] Add MI355X FP8 agentic recipe to the Qwen3.5 cookbook (#41849)
- **2026-09-30** [`e9b0d0c0a3`](https://github.com/sgl-project/sglang/commit/e9b0d0c0a3) [#40911](https://github.com/sgl-project/sglang/pull/40911) — [AMD] Gate flashinfer and TRT-LLM DSA paths on CUDA (#40911)
- **2026-09-30** [`d7cce54885`](https://github.com/sgl-project/sglang/commit/d7cce54885) [#41513](https://github.com/sgl-project/sglang/pull/41513) — [AMD] Resolve QSA packed-varlen decode to aiter on HIP (#41513)
- **2026-09-30** [`b87a241a6f`](https://github.com/sgl-project/sglang/commit/b87a241a6f) [#36901](https://github.com/sgl-project/sglang/pull/36901) — [AMD] Add Qwen3.8-Flash-Next-FP8 nightly validation (#36901)
- **2026-09-30** [`682f4ef32f`](https://github.com/sgl-project/sglang/commit/682f4ef32f) [#41687](https://github.com/sgl-project/sglang/pull/41687) — [ROCm] Select DSA indexer top-k wave size by arch (wave32 on gfx1250) (#41687)
- **2026-09-30** [`3b537e96e2`](https://github.com/sgl-project/sglang/commit/3b537e96e2) [#41135](https://github.com/sgl-project/sglang/pull/41135) — [AMD][DI][CI] Leave the GLM-5.2 MTP decode room to load its Triton kernels (#41135)
- **2026-09-30** [`25de118ae3`](https://github.com/sgl-project/sglang/commit/25de118ae3) [#41238](https://github.com/sgl-project/sglang/pull/41238) — [AMD][DI][CI] Give the dsv4pro-fp4 MTP decode more memory headroom (#41238)
- **2026-09-30** [`4207f1ae23`](https://github.com/sgl-project/sglang/commit/4207f1ae23) [#41099](https://github.com/sgl-project/sglang/pull/41099) — [AMD][DI][CI] Record the commit the MI355X nightly tested (#41099)
- **2026-09-30** [`f85ca901e2`](https://github.com/sgl-project/sglang/commit/f85ca901e2) [#41025](https://github.com/sgl-project/sglang/pull/41025) — [AMD][DI][CI] Fix four failures in the MI355X disaggregation nightly (#41025)
- **2026-09-30** [`964fd6af92`](https://github.com/sgl-project/sglang/commit/964fd6af92) [#38583](https://github.com/sgl-project/sglang/pull/38583) — [ROCm] GLM-5.2: gfx950 four-kernel fused DSA indexer decode path (#38583)
- **2026-09-30** [`cae69be584`](https://github.com/sgl-project/sglang/commit/cae69be584) [#41784](https://github.com/sgl-project/sglang/pull/41784) — chore: bump sgl-kernel version to 0.4.8 (#41784)
- **2026-09-29** [`4885b563c3`](https://github.com/sgl-project/sglang/commit/4885b563c3) [#41681](https://github.com/sgl-project/sglang/pull/41681) — [Test] Demote PD test RDMA openability check to a warning (#41681)
- **2026-09-29** [`875dd41e6f`](https://github.com/sgl-project/sglang/commit/875dd41e6f) [#28734](https://github.com/sgl-project/sglang/pull/28734) — [AMD] Fix Load and Inference of MLA models with Quark PTPC FP8 attention on ROCm (#28734)
- **2026-09-29** [`fa090f7755`](https://github.com/sgl-project/sglang/commit/fa090f7755) [#41444](https://github.com/sgl-project/sglang/pull/41444) — [MUSA] Fix fused MoE GEMV registration and torchada pin (#41444)
- **2026-09-29** [`5828cd4927`](https://github.com/sgl-project/sglang/commit/5828cd4927) [#41602](https://github.com/sgl-project/sglang/pull/41602) — [AMD] Add GLM-5.3 MI30x and MI35x nightly accuracy tests (#41602)
- **2026-09-29** [`c9cb32e310`](https://github.com/sgl-project/sglang/commit/c9cb32e310) [#40546](https://github.com/sgl-project/sglang/pull/40546) — [AMD] fix kda decode flydsl import (#40546)
- **2026-09-29** [`05817a40c9`](https://github.com/sgl-project/sglang/commit/05817a40c9) [#41464](https://github.com/sgl-project/sglang/pull/41464) — [AMD] Fix GLM-5.3 quark MoE MI35x test runner config (#41464)
- **2026-09-29** [`acffb0d20d`](https://github.com/sgl-project/sglang/commit/acffb0d20d) [#41551](https://github.com/sgl-project/sglang/pull/41551) — [Refactor] Select reduction fusion at the consumer (#41551)
- **2026-09-29** [`d9074f7943`](https://github.com/sgl-project/sglang/commit/d9074f7943) [#41600](https://github.com/sgl-project/sglang/pull/41600) — [Test] Fail fast when PD test RDMA devices are not openable by ibverbs (#41600)
- **2026-09-29** [`7889fbab9a`](https://github.com/sgl-project/sglang/commit/7889fbab9a) [#32196](https://github.com/sgl-project/sglang/pull/32196) — [PD] Keep EAGLE DP graph and token metadata consistent (#32196)
- **2026-09-28** [`9654e5c4bc`](https://github.com/sgl-project/sglang/commit/9654e5c4bc) [#41021](https://github.com/sgl-project/sglang/pull/41021) — dsv4.1-amd: fused mHC boundary and all-reduce + mHC post kernels (#41021)
- **2026-09-28** [`096b066fb4`](https://github.com/sgl-project/sglang/commit/096b066fb4) [#41020](https://github.com/sgl-project/sglang/pull/41020) — dsv4.1-amd: gfx950 sparse decode attention and sorted top-k (#41020)
- **2026-09-28** [`26d7539799`](https://github.com/sgl-project/sglang/commit/26d7539799) [#41597](https://github.com/sgl-project/sglang/pull/41597) — [Docs][AMD] Update GLM-5.2 MI355X daily image (#41597)
- **2026-09-28** [`fa443412c5`](https://github.com/sgl-project/sglang/commit/fa443412c5) [#41161](https://github.com/sgl-project/sglang/pull/41161) — [AMD] [GLM5] Fuse shared expert into AITER MoE on gfx950 (#41161)
- **2026-09-28** [`85be04978d`](https://github.com/sgl-project/sglang/commit/85be04978d) [#40943](https://github.com/sgl-project/sglang/pull/40943) — [AMD][DSV4] moe: enable shared-expert fusion on the grouped-topk path (megamoe) (#40943)
- **2026-09-28** [`34f090053e`](https://github.com/sgl-project/sglang/commit/34f090053e) [#41387](https://github.com/sgl-project/sglang/pull/41387) — [AMD] [Docker] Remove unused LLVM 18 setup from ROCm TileLang build (#41387)
- **2026-09-28** [`25de80780a`](https://github.com/sgl-project/sglang/commit/25de80780a) [#36903](https://github.com/sgl-project/sglang/pull/36903) — [AMD] Add GLM-5.3-Flash MI35x nightly test (#36903)
- **2026-09-28** [`3d2827236d`](https://github.com/sgl-project/sglang/commit/3d2827236d) [#41137](https://github.com/sgl-project/sglang/pull/41137) — [AMD] Register Triton data movement tests in PR CI (#41137)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-10-05 |
| [#42473](https://github.com/sgl-project/sglang/issues/42473) | Development Roadmap (2026 Q4) | — | 2026-10-05 |
| [#41939](https://github.com/sgl-project/sglang/issues/41939) | [Bug] GLM-5.3-Flash NVFP4 at TP4 loops in reasoning with no final answ | — | 2026-10-05 |
| [#39991](https://github.com/sgl-project/sglang/issues/39991) | [RFC] Align KV cache events with vLLM's schema so shared consumers hav | — | 2026-10-05 |
| [#42508](https://github.com/sgl-project/sglang/issues/42508) | [Bug] Scheduler aborts with `double free or corruption` inside the idl | — | 2026-10-05 |
| [#42564](https://github.com/sgl-project/sglang/issues/42564) | [Bug][ROCm] FLUX.2-dev fails on gfx1151: NVIDIA PTX inline assembly in | — | 2026-10-05 |
| [#42560](https://github.com/sgl-project/sglang/issues/42560) | [Bug] Deprecated --dp-size N --enable-dp-attention resolves to dp_size | — | 2026-10-05 |
| [#16565](https://github.com/sgl-project/sglang/issues/16565) | [Roadmap][Feature] Support Moore Threads (MUSA) GPU | mthreads | 2026-10-05 |
| [#42361](https://github.com/sgl-project/sglang/issues/42361) | [Bug] DeepSeek V4 Pro loading on Lustre takes 95 minutes despite prefe | — | 2026-10-04 |
| [#42459](https://github.com/sgl-project/sglang/issues/42459) | [Feature] Upgrade Nsight Compute bundled by the CUDA devel base image | — | 2026-10-04 |
| [#37451](https://github.com/sgl-project/sglang/issues/37451) | [Failure Tracker] PR Test (AMD) | ci-failure-tracker | 2026-10-04 |
| [#39684](https://github.com/sgl-project/sglang/issues/39684) | [Bug] sgl-deep-gemm 0.2.0: SM90 weight-scale transform returns a non-o | — | 2026-10-04 |
| [#42369](https://github.com/sgl-project/sglang/issues/42369) | [Bug][KV Cache] nvfp4 KV silently reuses the checkpoint's fp8-calibrat | — | 2026-10-03 |
| [#36796](https://github.com/sgl-project/sglang/issues/36796) | [Performance] Qwen4Exp decode on DGX Spark (SM121): QSA/PLE/GDN kernel | — | 2026-10-03 |
| [#42367](https://github.com/sgl-project/sglang/issues/42367) | [Bug] SM120: DeepSeek-V4.1-Flash decode CUDA graph capture fails with  | — | 2026-10-03 |
| [#42176](https://github.com/sgl-project/sglang/issues/42176) | [Feature] Integrate Cake kernels via FlashInfer: model-by-model tracke | — | 2026-10-03 |
| [#39499](https://github.com/sgl-project/sglang/issues/39499) | [Roadmap] SGLang dLLM Serving | — | 2026-10-02 |
| [#42260](https://github.com/sgl-project/sglang/issues/42260) | [Bug] Anthropic streaming drops a tool call's closing "}" when whitesp | — | 2026-10-02 |
| [#35376](https://github.com/sgl-project/sglang/issues/35376) | [RFC] Orchestrator-facing Elastic EP lifecycle contract | — | 2026-10-02 |
| [#42146](https://github.com/sgl-project/sglang/issues/42146) | [Bug] DeepSeek-V4 on SM120: the default SGLANG_FP8_PAGED_MQA_LOGITS_TO | — | 2026-10-02 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 94 |
| MoE / Expert Parallel | 58 |
| Multimodal | 50 |
| Prefill / Decode Disaggregation | 44 |
| KV Cache / Memory | 33 |
| Other | 29 |
| ROCm / AMD | 16 |
| Tensor / Data Parallel | 15 |
| CI / Build | 15 |
| Docs / Examples | 14 |
| Quantization | 14 |
| Models | 11 |
| Speculative Decoding | 10 |
| Triton / Kernels | 9 |
| Scheduler / Batching | 9 |
| LoRA | 5 |
| Serving / API | 4 |

## Attention / FlashInfer  (94 commits)

- **2026-10-05** [`26a1377c50`](https://github.com/sgl-project/sglang/commit/26a1377c50) [#42057](https://github.com/sgl-project/sglang/pull/42057)
  [Spec] LiLiCorr: named head MLPs and quantized head linears (#42057)
  _Files: `python/sglang/srt/models/dflash.py`, `python/sglang/srt/models/lilicorr.py`, `python/sglang/srt/speculative/lilicorr_utils.py`_
- **2026-10-05** [`284cda01fb`](https://github.com/sgl-project/sglang/commit/284cda01fb) [#41906](https://github.com/sgl-project/sglang/pull/41906)
  [diffusion] optimization: fuse the video VAE decoder's RMSNorm and QK RoPE for MiniMax-H3 (#41906)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/h3_vae_fused_norm.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/attention.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/vae_vit.py` _+3 more__
- **2026-10-05** [`55dcf3254f`](https://github.com/sgl-project/sglang/commit/55dcf3254f) [#41656](https://github.com/sgl-project/sglang/pull/41656)
  Fix XQA draft extend with FP8 KV cache in trtllm_mha (#41656)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `test/registered/attention/test_trtllm_mha_graph_metadata.py`_
- **2026-10-05** [`abd6c374c7`](https://github.com/sgl-project/sglang/commit/abd6c374c7) [#42101](https://github.com/sgl-project/sglang/pull/42101)
  [Perf] Optimize MiMo local audio attention on Hopper (#42101)
  _Files: `python/sglang/kernels/ops/attention/mimo_local_attention.py`, `python/sglang/srt/models/mimo_audio.py`_
- **2026-10-05** [`9f7d38ffd3`](https://github.com/sgl-project/sglang/commit/9f7d38ffd3) [#33855](https://github.com/sgl-project/sglang/pull/33855)
  [diffusion] attention: Allow disabling sequence masking in SP (#33855)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`_
- **2026-10-05** [`c41b2d26e5`](https://github.com/sgl-project/sglang/commit/c41b2d26e5) [#28650](https://github.com/sgl-project/sglang/pull/28650)
  [diffusion][ROCm][Perf]: Set gfx942 AITER FMHA rounding mode to rtz instead of rtna (#28650)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py`_
- **2026-10-05** [`cafb37a10d`](https://github.com/sgl-project/sglang/commit/cafb37a10d) [#40785](https://github.com/sgl-project/sglang/pull/40785)
  [JIT] Fuse FP8 KV-cache quantization into the prefix-valid commit kernel (#40785)
  _Files: `python/sglang/kernels/ops/kvcache/cache_move.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/test/kernels/prefix_valid.py` _+2 more__
- **2026-10-05** [`520d6d0229`](https://github.com/sgl-project/sglang/commit/520d6d0229) [#41659](https://github.com/sgl-project/sglang/pull/41659)
  [DSv4.1] Prefill indexer: raw selection, row-pair schedule ids, no host syncs (#41659)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/__init__.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/dense_blocks.py`, `python/sglang/srt/layers/attention/dsv4/v41_indexer/full_topk.py` _+10 more__
- **2026-10-05** [`f385390be5`](https://github.com/sgl-project/sglang/commit/f385390be5) [#42506](https://github.com/sgl-project/sglang/pull/42506)
  [Refactor] Simplify GDN, vision RoPE and MLA kernel dispatch (#42506)
  _Files: `python/sglang/kernels/ops/attention/set_mla_kv_concat_q.py`, `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/kernels/ops/attention/vision_rope.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py` _+2 more__
- **2026-10-05** [`f70e8c68fc`](https://github.com/sgl-project/sglang/commit/f70e8c68fc) [#42273](https://github.com/sgl-project/sglang/pull/42273)
  [Dsv4.1] Bounded replay with sparse mla path (#42273)
  _Files: `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `test/registered/kernels/ops/attention/test_flashmla_sched_meta.py` _+1 more__
- **2026-10-04** [`b792228b35`](https://github.com/sgl-project/sglang/commit/b792228b35) [#39931](https://github.com/sgl-project/sglang/pull/39931)
  [ROCm] topk v2: split one long row across blocks, the CDNA cluster-path equivalent (#39931)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `test/registered/kernels/ops/attention/test_topk_v2.py`_
- **2026-10-04** [`f5ccc4d7d9`](https://github.com/sgl-project/sglang/commit/f5ccc4d7d9) [#42486](https://github.com/sgl-project/sglang/pull/42486)
  [Kernel] Use explicit reciprocal scaling for recurrent Q/K normalization (#42486)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `test/registered/attention/test_kda_kernels.py`_
- **2026-10-04** [`1d02a36bb7`](https://github.com/sgl-project/sglang/commit/1d02a36bb7) [#38229](https://github.com/sgl-project/sglang/pull/38229)
  fix(inkling): translate unified-memory checkpoint destinations to physical slots (#38229)
  _Files: `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `python/sglang/srt/models/inkling_common/attn.py`, `python/sglang/srt/models/inkling_common/kernels/comm.py`, `python/sglang/srt/models/inkling_common/sconv.py` _+4 more__
- **2026-10-04** [`7eb628612c`](https://github.com/sgl-project/sglang/commit/7eb628612c) [#42460](https://github.com/sgl-project/sglang/pull/42460)
  [Fix] Publish the parallel config the CLIP attention test reads (#42460)
  _Files: `python/sglang/multimodal_gen/test/unit/test_srt_clip_reuse.py`_
- **2026-10-04** [`6cc661f223`](https://github.com/sgl-project/sglang/commit/6cc661f223) [#34438](https://github.com/sgl-project/sglang/pull/34438)
  [AMD][DCP 2/N] Enable aiter asm ps for kimi k3 prefill (#34438)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-10-04** [`0e6d7eba5f`](https://github.com/sgl-project/sglang/commit/0e6d7eba5f) [#42331](https://github.com/sgl-project/sglang/pull/42331)
  [Fix] Count attention-DP ranks in one-batch bench running cap (#42331)
  _Files: `python/sglang/benchmark/one_batch_server.py`_
- **2026-10-04** [`fccc61c1c5`](https://github.com/sgl-project/sglang/commit/fccc61c1c5) [#42038](https://github.com/sgl-project/sglang/pull/42038)
  [CP] Support DP x TP x CP for attention with interleave CP strategy (#42038)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.1.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` _+9 more__
- **2026-10-04** [`f2385314b2`](https://github.com/sgl-project/sglang/commit/f2385314b2) [#41476](https://github.com/sgl-project/sglang/pull/41476)
  [AMD] Add DeepSeek-V4.1-Flash MI35x nightly accuracy test (#41476)
  _Files: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_deepseek_v41_flash_eval_mi35x.py`, `test/run_suite.py`_
- **2026-10-04** [`663984b5a1`](https://github.com/sgl-project/sglang/commit/663984b5a1) [#41931](https://github.com/sgl-project/sglang/pull/41931)
  [AMD] Keep aiter's tuned GEMM for the DeepSeek-V4 compressors (#41931)
  _Files: `python/sglang/srt/layers/attention/dsv4/compressor.py`_
- **2026-10-04** [`71dc292b97`](https://github.com/sgl-project/sglang/commit/71dc292b97) [#41707](https://github.com/sgl-project/sglang/pull/41707)
  [AMD] Use AITER ASM prefill for MiniMax-M3 HD128 attention (#41707)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/amd/test_minimax_hd128_asm_prefill.py`_
- **2026-10-03** [`5916999afb`](https://github.com/sgl-project/sglang/commit/5916999afb) [#41660](https://github.com/sgl-project/sglang/pull/41660)
  [DSv4.1] Fused c1/c2 compress for eager extend, faster c2 decode (#41660)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c2.cuh`, `python/sglang/kernels/jit/csrc/distributed/nvlink_comm.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/math.cuh`, `python/sglang/kernels/ops/attention/dsv4/low_ratio_compress.py` _+3 more__
- **2026-10-03** [`d75d5b33f7`](https://github.com/sgl-project/sglang/commit/d75d5b33f7) [#41658](https://github.com/sgl-project/sglang/pull/41658)
  [DSv4.1] Faster fp4 index-K gather and combine_topk_swa_indices (#41658)
  _Files: `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`, `python/sglang/kernels/ops/attention/dsv4/sparse_prefill_kernels.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` _+1 more__
- **2026-10-03** [`379ec90fb2`](https://github.com/sgl-project/sglang/commit/379ec90fb2) [#41657](https://github.com/sgl-project/sglang/pull/41657)
  [DSv4.1] Fold q_rope_store into fused_q_norm_rope (#41657)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/kernels/ops/attention/dsv4/elementwise.py`, `python/sglang/kernels/ops/attention/dsv4/q_rope_store.py`, `python/sglang/srt/models/deepseek_v4.py` _+1 more__
- **2026-10-03** [`1093c501df`](https://github.com/sgl-project/sglang/commit/1093c501df) [#41985](https://github.com/sgl-project/sglang/pull/41985)
  [diffusion] optimization: route subBlock sparse attention in head chunks (#41985)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse_attn.py`, `python/sglang/multimodal_gen/test/unit/test_subblock_sparse_attention.py`_
- **2026-10-03** [`af1bef3eaf`](https://github.com/sgl-project/sglang/commit/af1bef3eaf) [#41870](https://github.com/sgl-project/sglang/pull/41870)
  [AMD] GLM-5.3-Flash: fuse shared expert and KDA projections on Quark MXFP4 (#41870)
  _Files: `python/sglang/srt/layers/quantization/base_config.py`, `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/glm5_next.py`, `test/registered/unit/models/test_glm5_next_bfg_fusion.py` _+1 more__
- **2026-10-03** [`8ff02f5820`](https://github.com/sgl-project/sglang/commit/8ff02f5820) [#41729](https://github.com/sgl-project/sglang/pull/41729)
  [QSA] Enable breakable prefill CUDA graphs for text-only Qwen3.8 Flash-Next (capture-safe metadata, MTP side-channel padding) (#41729)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/qsa/metadata.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py` _+11 more__
- **2026-10-03** [`65f759144d`](https://github.com/sgl-project/sglang/commit/65f759144d) [#42166](https://github.com/sgl-project/sglang/pull/42166)
  [HiCache] Let the MiniMax-M3 K-only host pool join a host pool group (#42166)
  _Files: `python/sglang/srt/mem_cache/pool_host/mha.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py`_
- **2026-10-02** [`3bde8eb2d8`](https://github.com/sgl-project/sglang/commit/3bde8eb2d8) [#42036](https://github.com/sgl-project/sglang/pull/42036)
  [CP 1/5] Remove the CP adapter and separate interleave transport from boundary reduction (#42036)
  _Files: `python/sglang/srt/layers/cp/interleave.py`, `python/sglang/srt/layers/layer_boundary/adapters/context_parallel.py`, `python/sglang/srt/layers/layer_boundary/ops.py`, `python/sglang/srt/layers/layer_boundary/prepare.py` _+2 more__
- **2026-10-02** [`b69a5f296a`](https://github.com/sgl-project/sglang/commit/b69a5f296a) [#41488](https://github.com/sgl-project/sglang/pull/41488)
  [AMD] Add opt-in MiniMax-M3 TP4 indexer context partitioning (#41488)
  _Files: `python/sglang/kernels/ops/attention/minimax_sparse/decode/indexer_cp.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/indexer_cp.py` _+3 more__
- **2026-10-02** [`e8fab85a02`](https://github.com/sgl-project/sglang/commit/e8fab85a02) [#42251](https://github.com/sgl-project/sglang/pull/42251)
  [KDA] Add an opt-in decode-parity mode to the Triton multi-token recurrence (#42251)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `test/registered/attention/test_kda_kernels.py`_
- **2026-10-02** [`0098b9d29d`](https://github.com/sgl-project/sglang/commit/0098b9d29d) [#42002](https://github.com/sgl-project/sglang/pull/42002)
  [Spec] Fix Qwen3.5 text model EAGLE3/DFLASH aux-layer capture (#42002)
  _Files: `python/sglang/srt/models/qwen3_5_text.py`_
- **2026-10-02** [`89f21671bb`](https://github.com/sgl-project/sglang/commit/89f21671bb) [#39893](https://github.com/sgl-project/sglang/pull/39893)
  fix: preserve QSA indexer state through HiCache (#39893)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/pool_host/qsa.py`, `python/sglang/srt/mem_cache/qsa_kv_pool.py`, `test/registered/kernels/ops/attention/qsa/test_qsa_hicache.py` _+1 more__
- **2026-10-02** [`0f71ec8656`](https://github.com/sgl-project/sglang/commit/0f71ec8656) [#41542](https://github.com/sgl-project/sglang/pull/41542)
  [diffusion] UX: deduplicate SM120 FP8 fallback warnings across layers (#41542)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/fp8_fa_sm120_attn.py`_
- **2026-10-02** [`41bd213c5f`](https://github.com/sgl-project/sglang/commit/41bd213c5f) [#42211](https://github.com/sgl-project/sglang/pull/42211)
  [Test] Add get_swa_key_page_size to the Q8KV8 sparse-prefill fake KV pool (#42211)
  _Files: `test/registered/kernels/ops/attention/test_q8kv8_sparse_prefill_backend.py`_
- **2026-10-02** [`bf8adf9602`](https://github.com/sgl-project/sglang/commit/bf8adf9602) [#41965](https://github.com/sgl-project/sglang/pull/41965)
  [diffusion] fix: fix int32 offset overflow in SubBlock router kernels (#41965)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/kernels.py`, `python/sglang/multimodal_gen/test/unit/test_subblock_sparse_attention.py`_
- **2026-10-02** [`ef867fa40d`](https://github.com/sgl-project/sglang/commit/ef867fa40d) [#42128](https://github.com/sgl-project/sglang/pull/42128)
  [Fix][DSV4.1] SWA page size with bounded replay (#42128)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `test/registered/unit/mem_cache/test_dsv4_compressed_pools.py`_
- **2026-10-02** [`58f0d250ec`](https://github.com/sgl-project/sglang/commit/58f0d250ec) [#41533](https://github.com/sgl-project/sglang/pull/41533)
  [ROCm] Use the fused MLA absorb + RoPE + KV-write kernel for decode-sized forward modes only (#41533)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`_
- **2026-10-02** [`67eab57057`](https://github.com/sgl-project/sglang/commit/67eab57057) [#41175](https://github.com/sgl-project/sglang/pull/41175)
  [qwen 3.8 next] Fuse NEXTN verify and draft graph input preparation (#41175)
  _Files: `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/kernels/ops/speculative/eagle.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `python/sglang/srt/managers/utils.py` _+10 more__
- **2026-10-02** [`2a3655fea1`](https://github.com/sgl-project/sglang/commit/2a3655fea1) [#40331](https://github.com/sgl-project/sglang/pull/40331)
  [unified-memory] Name the fused KV translate for what it computes (7/7) (#40331)
  _Files: `python/sglang/kernels/ops/kvcache/kv_indices.py`, `python/sglang/kernels/ops/memory/__init__.py`, `python/sglang/kernels/ops/memory/virtual_slot.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py` _+24 more__
- **2026-10-02** [`9855e9c6f8`](https://github.com/sgl-project/sglang/commit/9855e9c6f8) [#40329](https://github.com/sgl-project/sglang/pull/40329)
  [unified-memory] Remove the kernel-page multiplier plumbing (5/7) (#40329)
  _Files: `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/kernels/ops/kvcache/kv_read_table.py`, `python/sglang/kernels/ops/memory/virtual_slot.py`, `python/sglang/srt/layers/attention/aiter_backend.py` _+13 more__
- **2026-10-02** [`cdadb1c79a`](https://github.com/sgl-project/sglang/commit/cdadb1c79a) [#38592](https://github.com/sgl-project/sglang/pull/38592)
  [unified-memory] Token-major dense views for the unified memory pool (3/7) (#38592)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/managers/cache_controller.py` _+32 more__
- **2026-10-02** [`5df52e6382`](https://github.com/sgl-project/sglang/commit/5df52e6382) [#40327](https://github.com/sgl-project/sglang/pull/40327)
  [unified-memory] Build paged KV views through one helper (2/7) (#40327)
  _Files: `python/sglang/srt/layers/attention/cutedsl_mla_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py` _+9 more__
- **2026-10-02** [`d3dbb71e5a`](https://github.com/sgl-project/sglang/commit/d3dbb71e5a) [#40326](https://github.com/sgl-project/sglang/pull/40326)
  [unified-memory] Derive KV row addresses from strides, not shapes (1/7) (#40326)
  _Files: `python/sglang/kernels/jit/csrc/attention/fused_fp8_qkv_kv_cache.cuh`, `python/sglang/kernels/jit/csrc/inkling/inkling_attn_prologue_fused.cuh`, `python/sglang/kernels/jit/csrc/kv_canary/canary_common.cuh`, `python/sglang/kernels/jit/csrc/kv_canary/canary_verify.cuh` _+17 more__
- **2026-10-01** [`f17f7705a5`](https://github.com/sgl-project/sglang/commit/f17f7705a5) [#39273](https://github.com/sgl-project/sglang/pull/39273)
  [AMD] [GLM-5.3-Flash] Enable FP8 and MXFP4 serving on gfx950 (#39273)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `python/sglang/kernels/jit/csrc/dsa/kpool_topk_transform.cuh` _+30 more__
- **2026-10-01** [`52d5faed5b`](https://github.com/sgl-project/sglang/commit/52d5faed5b) [#38187](https://github.com/sgl-project/sglang/pull/38187)
  [Bugfix] Llama4 local attention: read page ids from the graph tables in CUDA-graph capture/replay (page_size > 1) (#38187)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/local_attention.py`, `python/sglang/srt/layers/attention/xpu_backend.py`, `test/registered/unit/layers/attention/test_local_attention.py`_
- **2026-10-01** [`f03a183719`](https://github.com/sgl-project/sglang/commit/f03a183719) [#36406](https://github.com/sgl-project/sglang/pull/36406)
  Fix Kimi-K3 MLA output gate dispatch on non-CUDA devices (#36406)
  _Files: `python/sglang/kernels/ops/attention/mla_output_gate.py`, `test/registered/unit/models/test_kimi_k3_mla_output_gate.py`_
- **2026-10-01** [`3c4e218779`](https://github.com/sgl-project/sglang/commit/3c4e218779) [#42017](https://github.com/sgl-project/sglang/pull/42017)
  [AMD][V4.1][*/N] OPUS sparse prefill on gfx950 through layout conversion (#42017)
  _Files: `python/sglang/kernels/ops/attention/dsv4/opus_sparse_prefill_hip.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `test/registered/attention/unittests/dsv4/test_dsv41_opus_sparse_prefill_hip.py`_
- **2026-10-01** [`f45c004e18`](https://github.com/sgl-project/sglang/commit/f45c004e18) [#42014](https://github.com/sgl-project/sglang/pull/42014)
  [AMD][V4.1][*/N] Build DSpark draft metadata inside the CUDA graph on ROCm (#42014)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-10-01** [`0224fcbd1c`](https://github.com/sgl-project/sglang/commit/0224fcbd1c) [#41947](https://github.com/sgl-project/sglang/pull/41947)
  [AMD][V4.1][*/N] Route low-ratio indexer and candidate-block top-k through top-k v2 (#41947)
  _Files: `python/sglang/kernels/ops/attention/dsv4/candidate_blocks_hip.py`, `python/sglang/srt/layers/attention/dsv4/low_ratio_backend_hip.py`_
- **2026-10-01** [`5fab1f0f51`](https://github.com/sgl-project/sglang/commit/5fab1f0f51) [#42018](https://github.com/sgl-project/sglang/pull/42018)
  [Fix] Let the aiter DCP ASM decode test run without aiter (#42018)
  _Files: `test/registered/attention/test_aiter_gluon_h12_fp8.py`_
- **2026-10-01** [`266d9d1fa7`](https://github.com/sgl-project/sglang/commit/266d9d1fa7) [#39721](https://github.com/sgl-project/sglang/pull/39721)
  [Qwen3.8 CP 1/4] Context parallelism for QSA attention and the sparse indexer (#39721)
  _Files: `python/sglang/srt/layers/attention/qsa/metadata.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `test/registered/unit/cp/test_qsa_cp_unit.py`_
- **2026-10-01** [`b51d4a04f0`](https://github.com/sgl-project/sglang/commit/b51d4a04f0) [#41736](https://github.com/sgl-project/sglang/pull/41736)
  [DFlash] Keep grouped-conv taps inside each request's block so NaN/Inf cannot leak across requests (#41736)
  _Files: `python/sglang/srt/models/dflash.py`_
- **2026-10-01** [`42f2e4fcb7`](https://github.com/sgl-project/sglang/commit/42f2e4fcb7) [#41987](https://github.com/sgl-project/sglang/pull/41987)
  [DSA] Stop forcing the per-step CPU seq_lens sync for the k-pool indexer (#41987)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer_kpool.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/unit/layers/test_kpool_stream_scheduling.py`_
- **2026-10-01** [`3ed6367d3f`](https://github.com/sgl-project/sglang/commit/3ed6367d3f) [#41337](https://github.com/sgl-project/sglang/pull/41337)
  [DSV4/DSA] Name the FlashMLA KV format and drop the V4.1 support probe (#41337)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/environ.py` _+2 more__
- **2026-10-01** [`99c9d65b32`](https://github.com/sgl-project/sglang/commit/99c9d65b32) [#40750](https://github.com/sgl-project/sglang/pull/40750)
  [AMD] AITER MLA DCP decode ASM path (opt-in) (#40750)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/attention/test_aiter_gluon_h12_fp8.py`_
- **2026-10-01** [`5733bcaad3`](https://github.com/sgl-project/sglang/commit/5733bcaad3) [#40913](https://github.com/sgl-project/sglang/pull/40913)
  Declare HiCache host pools for DSA indexer (#40913)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/host_pool_config.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/pool_host/dsa.py` _+7 more__
- **2026-10-01** [`40e1bb0f36`](https://github.com/sgl-project/sglang/commit/40e1bb0f36) [#41986](https://github.com/sgl-project/sglang/pull/41986)
  [Docs] Add NVIDIA NVFP4 checkpoint to GLM-5.3-Flash cookbook (#41986)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-10-01** [`99c59a2ea6`](https://github.com/sgl-project/sglang/commit/99c59a2ea6) [#41837](https://github.com/sgl-project/sglang/pull/41837)
  Drop the GLM-5.3-Flash breakable prefill chunk-size pin (#41837)
  _Files: `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/arg_groups/resolution_hooks.py`, `test/registered/unit/server_args/test_resolution_hook_registry.py`_
- **2026-10-01** [`0148d9a2fd`](https://github.com/sgl-project/sglang/commit/0148d9a2fd) [#41497](https://github.com/sgl-project/sglang/pull/41497)
  [AMD] Fix MiniMax-M3 EAGLE3 verification on ROCm (#41497)
  _Files: `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `test/registered/amd/test_minimax_rocm_verify.py`_
- **2026-09-30** [`a9c97c9f69`](https://github.com/sgl-project/sglang/commit/a9c97c9f69) [#41818](https://github.com/sgl-project/sglang/pull/41818)
  [Feature] Add --attn-dp-size and deprecate --enable-dp-attention (#41818)
- **2026-09-30** [`201c4b9b2a`](https://github.com/sgl-project/sglang/commit/201c4b9b2a) [#34201](https://github.com/sgl-project/sglang/pull/34201)
  [RL, Spec] Introduce top-p mask capture for spec and add DFlash/DSpark impl (#34201)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_accept.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py` _+12 more__
- **2026-09-30** [`986cb8268b`](https://github.com/sgl-project/sglang/commit/986cb8268b) [#41817](https://github.com/sgl-project/sglang/pull/41817)
  [Refactor] Enter draft TP scopes by attention ownership and drop ModelRunner.tp_group (#41817)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py`, `python/sglang/srt/hardware_backend/xpu/graph_runner/xpu_full_graph_backend.py`, `python/sglang/srt/managers/tp_worker.py` _+25 more__
- **2026-09-30** [`499e86db98`](https://github.com/sgl-project/sglang/commit/499e86db98) [#41813](https://github.com/sgl-project/sglang/pull/41813)
  [Refactor] Keep only the TP and PP groups on the model runner (#41813)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/hpc_ops_backend.py` _+29 more__
- **2026-09-30** [`ecc0f0dec2`](https://github.com/sgl-project/sglang/commit/ecc0f0dec2) [#41808](https://github.com/sgl-project/sglang/pull/41808)
  [Fix] Pass the draft's attention ownership to DFLASH's eager LiLiCorr scope (#41808)
  _Files: `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-09-30** [`4407a21f3c`](https://github.com/sgl-project/sglang/commit/4407a21f3c) [#40001](https://github.com/sgl-project/sglang/pull/40001)
  [Spec][PP] Fix hybrid recurrent-state commit and micro-batch pairing under PP x speculative decoding (#40001)
  _Files: `python/sglang/kernels/ops/attention/fla/gdn_replayssm_spec_fold.py`, `python/sglang/kernels/ops/attention/fla/kda_replayssm_spec_decode.py`, `python/sglang/kernels/ops/mamba/mamba_state_scatter_triton.py`, `python/sglang/srt/arg_groups/attention_hook.py` _+14 more__
- **2026-09-30** [`547286bb5a`](https://github.com/sgl-project/sglang/commit/547286bb5a) [#39012](https://github.com/sgl-project/sglang/pull/39012)
  [Deps] Bump transformers to 5.17.0 (#39012)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `docker/rocm.Dockerfile`, `python/pyproject.toml`, `python/pyproject_cpu.toml` _+17 more__
- **2026-09-30** [`eae808903f`](https://github.com/sgl-project/sglang/commit/eae808903f) [#40709](https://github.com/sgl-project/sglang/pull/40709)
  [Deps] Bump FlashInfer to 0.7.0.post1 (#40709)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`, `python/pyproject.toml`, `python/sglang/kernels/ops/attention/flash_attn/cute/pyproject.toml` _+8 more__
- **2026-09-30** [`4dfc0ac131`](https://github.com/sgl-project/sglang/commit/4dfc0ac131) [#37984](https://github.com/sgl-project/sglang/pull/37984)
  [BugFix] Pass token-major Q/K tensors from Gemma-3 to RadixAttention (#37984)
  _Files: `python/sglang/srt/models/gemma3_causal.py`_
- **2026-09-30** [`57c81258d4`](https://github.com/sgl-project/sglang/commit/57c81258d4) [#41445](https://github.com/sgl-project/sglang/pull/41445)
  [KDA] Enable the ptx_kda prefill backend on SM100 (B200 / GB200) (#41445)
  _Files: `python/sglang/kernels/jit/csrc/attention/kda_prefill.cu`, `python/sglang/kernels/ops/attention/linear/kda_ptx_prefill/__init__.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_ptx.py` _+2 more__
- **2026-09-30** [`c0296186b7`](https://github.com/sgl-project/sglang/commit/c0296186b7) [#41572](https://github.com/sgl-project/sglang/pull/41572)
  [KDA] Fix ptx_kda prefill NaN without a gate lower bound and workspace growth (#41572)
  _Files: `python/sglang/kernels/jit/csrc/attention/kda_prefill.cu`, `python/sglang/srt/layers/attention/linear/kernels/kda_ptx.py`, `test/registered/kernels/ops/attention/test_kda_prefill.py`, `test/registered/unit/layers/attention/linear/kernels/test_kda_ptx.py`_
- **2026-09-30** [`8055ccd2cd`](https://github.com/sgl-project/sglang/commit/8055ccd2cd) [#40227](https://github.com/sgl-project/sglang/pull/40227)
  [Linear Attention] Expose GDN/KDA prefill hooks and auxiliary cache accounting (#40227)
  _Files: `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` _+2 more__
- **2026-09-30** [`e9b0d0c0a3`](https://github.com/sgl-project/sglang/commit/e9b0d0c0a3) [#40911](https://github.com/sgl-project/sglang/pull/40911)
  [AMD] Gate flashinfer and TRT-LLM DSA paths on CUDA (#40911)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`_
- **2026-09-30** [`d7cce54885`](https://github.com/sgl-project/sglang/commit/d7cce54885) [#41513](https://github.com/sgl-project/sglang/pull/41513)
  [AMD] Resolve QSA packed-varlen decode to aiter on HIP (#41513)
  _Files: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `test/registered/kernels/ops/attention/qsa/test_qsa_rocm.py`_
- **2026-09-30** [`b87a241a6f`](https://github.com/sgl-project/sglang/commit/b87a241a6f) [#36901](https://github.com/sgl-project/sglang/pull/36901)
  [AMD] Add Qwen3.8-Flash-Next-FP8 nightly validation (#36901)
  _Files: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/test_qwen38_flash_next_fp8_eval.py`_
- **2026-09-30** [`88f95f4b87`](https://github.com/sgl-project/sglang/commit/88f95f4b87) [#40972](https://github.com/sgl-project/sglang/pull/40972)
  [qwen next] Fuse QSA KV preparation and sparse block expansion (#40972)
  _Files: `python/sglang/srt/layers/attention/qsa/fused_kv.py`, `python/sglang/srt/layers/attention/qsa/metadata.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py` _+2 more__
- **2026-09-30** [`b660100c00`](https://github.com/sgl-project/sglang/commit/b660100c00) [#41173](https://github.com/sgl-project/sglang/pull/41173)
  [qwen 3.8 next] Fuse QSA graph replay metadata across draft steps (#41173)
  _Files: `python/sglang/srt/layers/attention/qsa/graph_metadata.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `test/registered/kernels/ops/attention/qsa/test_qsa.py`_
- **2026-09-30** [`964fd6af92`](https://github.com/sgl-project/sglang/commit/964fd6af92) [#38583](https://github.com/sgl-project/sglang/pull/38583)
  [ROCm] GLM-5.2: gfx950 four-kernel fused DSA indexer decode path (#38583)
  _Files: `python/sglang/kernels/jit/csrc/dsa_gfx950/dual_gemv_bf16.cuh`, `python/sglang/kernels/jit/csrc/dsa_gfx950/paged_mqa_logits.cuh`, `python/sglang/kernels/jit/csrc/dsa_gfx950/qk_rope_hadamard_quant.cuh`, `python/sglang/kernels/jit/csrc/dsa_gfx950/topk_transform.cuh` _+10 more__
- **2026-09-30** [`113e6a1496`](https://github.com/sgl-project/sglang/commit/113e6a1496) [#41778](https://github.com/sgl-project/sglang/pull/41778)
  [Refactor] Simplify layer boundary internals (#41778)
  _Files: `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/layer_boundary/adapters/attention.py`, `python/sglang/srt/layers/layer_boundary/adapters/context_parallel.py`, `python/sglang/srt/layers/layer_boundary/boundary.py` _+8 more__
- **2026-09-30** [`57d4adeb83`](https://github.com/sgl-project/sglang/commit/57d4adeb83) [#41336](https://github.com/sgl-project/sglang/pull/41336)
  [Kernel] Expose FlashMLA kv_format in sgl-kernel sparse decode (#41336)
  _Files: `python/sglang/kernels/aot/cmake/flashmla.cmake`, `python/sglang/kernels/aot/csrc/flashmla_extension.cc`, `python/sglang/kernels/aot/python/sgl_kernel/flash_mla.py`, `python/sglang/kernels/aot/tests/test_flashmla.py`_
- **2026-09-29** [`37a47737c8`](https://github.com/sgl-project/sglang/commit/37a47737c8) [#41486](https://github.com/sgl-project/sglang/pull/41486)
  [Perf] Tune SM90 GDN recurrent verify launch for small batches (#41486)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py`, `test/registered/kernels/ops/attention/test_fused_verify_triton_gdn.py`_
- **2026-09-29** [`84523d6785`](https://github.com/sgl-project/sglang/commit/84523d6785) [#40159](https://github.com/sgl-project/sglang/pull/40159)
  [Spec] Reuse K3 auxiliary outputs across decode CUDA graph sizes (#40159)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/aux_hidden_states.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/model_runner.py` _+8 more__
- **2026-09-29** [`875dd41e6f`](https://github.com/sgl-project/sglang/commit/875dd41e6f) [#28734](https://github.com/sgl-project/sglang/pull/28734)
  [AMD] Fix Load and Inference of MLA models with Quark PTPC FP8 attention on ROCm (#28734)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`, `test/registered/unit/layers/quantization/test_quark_w8a8_fp8_ptpc.py`_
- **2026-09-29** [`c9cb32e310`](https://github.com/sgl-project/sglang/commit/c9cb32e310) [#40546](https://github.com/sgl-project/sglang/pull/40546)
  [AMD] fix kda decode flydsl import (#40546)
  _Files: `python/sglang/kernels/ops/attention/kda_flydsl/kernels/kimi_k3_kda_decode.py`, `python/sglang/kernels/ops/attention/kda_flydsl/kernels/kimi_k3_kda_decode_fb.py`, `test/registered/kernels/ops/attention/kda_flydsl/test_kimi_k3_kda_decode.py`_
- **2026-09-29** [`c7be3e935b`](https://github.com/sgl-project/sglang/commit/c7be3e935b) [#34528](https://github.com/sgl-project/sglang/pull/34528)
  [SM120] Add optional FlashInfer PCIe-IPC all-reduce for switch-free hosts (#34528)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/distributed/device_communicators/pcie_ipc_ar.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py` _+2 more__
- **2026-09-29** [`49d26ff0c2`](https://github.com/sgl-project/sglang/commit/49d26ff0c2) [#41066](https://github.com/sgl-project/sglang/pull/41066)
  [diffusion] model: support flux 3 action robot policies (#41066)
  _Files: `docs/cookbook/vla/FLUX/FLUX-3-Action.mdx`, `docs/cookbook/vla/intro.mdx`, `docs/docs.json`, `docs/src/snippets/diffusion/model-catalog.jsx` _+21 more__
- **2026-09-29** [`79cafec013`](https://github.com/sgl-project/sglang/commit/79cafec013) [#41590](https://github.com/sgl-project/sglang/pull/41590)
  [Model] Add IQuest Q1 support and MTP draft (#41590)
  _Files: `docs/cookbook/autoregressive/IQuestLab/IQuest-Q1.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json`, `docs/src/snippets/configs/IQuestLab/iquest-q1.jsx` _+29 more__
- **2026-09-28** [`096b066fb4`](https://github.com/sgl-project/sglang/commit/096b066fb4) [#41020](https://github.com/sgl-project/sglang/pull/41020)
  dsv4.1-amd: gfx950 sparse decode attention and sorted top-k (#41020)
  _Files: `python/sglang/kernels/aot/benchmark/bench_dsv4_topk_transform.py`, `python/sglang/kernels/aot/csrc/common_extension_rocm.cc`, `python/sglang/kernels/aot/csrc/elementwise/deepseek_v4_topk.cu`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h` _+13 more__
- **2026-09-28** [`8151378c1a`](https://github.com/sgl-project/sglang/commit/8151378c1a) [#41364](https://github.com/sgl-project/sglang/pull/41364)
  [DeepSelect] Add page-table transform to top-k and tighten the layout contract (#41364)
  _Files: `python/sglang/kernels/jit/csrc/deep_select/README.md`, `python/sglang/kernels/jit/csrc/deep_select/entry.cuh`, `python/sglang/kernels/jit/csrc/deep_select/vendor/.clang-format`, `python/sglang/kernels/jit/csrc/deep_select/vendor/3rdparty/kerutils/README.md` _+23 more__
- **2026-09-28** [`da3eb6db32`](https://github.com/sgl-project/sglang/commit/da3eb6db32) [#41144](https://github.com/sgl-project/sglang/pull/41144)
  [Unified Memory] Fix Inkling conv-checkpoint track ids written to virtual slot numbers (#41144)
  _Files: `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_hybrid_bitexact.py`_
- **2026-09-28** [`bddeb61d94`](https://github.com/sgl-project/sglang/commit/bddeb61d94) [#38133](https://github.com/sgl-project/sglang/pull/38133)
  [Unified Memory] fix: preserve FP8 dtype in unified MHA pool (#38133)
  _Files: `python/sglang/srt/mem_cache/unified_memory_pool.py`, `test/registered/unit/mem_cache/test_unified_mha_views.py`_
- **2026-09-28** [`6582425854`](https://github.com/sgl-project/sglang/commit/6582425854) [#41165](https://github.com/sgl-project/sglang/pull/41165)
  Let predicate-registered linear-attention models carry the mamba radix-cache leaves (#41165)
  _Files: `python/sglang/srt/arg_groups/mamba_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/linear_attn_model_registry.py` _+2 more__
- **2026-09-28** [`f4de6abee6`](https://github.com/sgl-project/sglang/commit/f4de6abee6) [#39060](https://github.com/sgl-project/sglang/pull/39060)
  feat(npu): Support returning indexer top-k results (#39060)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`, `python/sglang/srt/state_capturer/indexer_topk.py`, `python/sglang/test/ascend/test_ascend_utils.py` _+3 more__
- **2026-09-28** [`25de80780a`](https://github.com/sgl-project/sglang/commit/25de80780a) [#36903](https://github.com/sgl-project/sglang/pull/36903)
  [AMD] Add GLM-5.3-Flash MI35x nightly test (#36903)
  _Files: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_glm53_flash_eval_mi35x.py`, `test/run_suite.py`_
- **2026-09-28** [`3d2827236d`](https://github.com/sgl-project/sglang/commit/3d2827236d) [#41137](https://github.com/sgl-project/sglang/pull/41137)
  [AMD] Register Triton data movement tests in PR CI (#41137)
  _Files: `test/registered/attention/test_gdn_fused_split_head_ratios.py`, `test/registered/kernels/ops/embeddings/test_vocab_parallel_embedding.py`_

## MoE / Expert Parallel  (58 commits)

- **2026-10-05** [`438d9d2074`](https://github.com/sgl-project/sglang/commit/438d9d2074) [#37261](https://github.com/sgl-project/sglang/pull/37261)
  [Feature] DeepEP v2: expanded (do_expand=True) prefill dispatch (#37261)
  _Files: `docs/src/snippets/configs/Qwen/qwen3.8.jsx`, `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`, `python/sglang/srt/arg_groups/moe_hook.py` _+13 more__
- **2026-10-04** [`1f299e9f2f`](https://github.com/sgl-project/sglang/commit/1f299e9f2f) [#42481](https://github.com/sgl-project/sglang/pull/42481)
  [Refactor] Build layer stacks in order with append_stages (#42481)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/hyperconnection.py` _+92 more__
- **2026-10-04** [`5c8fb9e938`](https://github.com/sgl-project/sglang/commit/5c8fb9e938) [#42479](https://github.com/sgl-project/sglang/pull/42479)
  [Fix] Offer the fused MoE finalize all-reduce only to a block that owes the sum (#42479)
  _Files: `python/sglang/srt/models/deepseek_v2.py`, `test/registered/unit/layer_boundary/test_stage_producers_leave_sums.py`_
- **2026-10-04** [`f07c1a398e`](https://github.com/sgl-project/sglang/commit/f07c1a398e) [#42478](https://github.com/sgl-project/sglang/pull/42478)
  [Refactor] Build the Qwen4 experimental decoders from stage boundaries (#42478)
  _Files: `python/sglang/srt/arg_groups/boundary_reduction.py`, `python/sglang/srt/layers/layer_boundary/__init__.py`, `python/sglang/srt/layers/layer_boundary/residual/gated.py`, `python/sglang/srt/models/qwen3_5.py` _+6 more__
- **2026-10-04** [`aa0ce20201`](https://github.com/sgl-project/sglang/commit/aa0ce20201) [#41725](https://github.com/sgl-project/sglang/pull/41725)
  [ROCm] GLM-5.2 decode path: decode-shaped MoE/MLA tiles, split speculative softmax, and bf16 GEMM routing (#41725)
  _Files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/kernels/ops/sampling/__init__.py`, `python/sglang/kernels/ops/sampling/temperature_softmax.py`, `python/sglang/srt/layers/moe/topk.py` _+9 more__
- **2026-10-04** [`0bdd0cc8dc`](https://github.com/sgl-project/sglang/commit/0bdd0cc8dc) [#38641](https://github.com/sgl-project/sglang/pull/38641)
  [Deps] Upgrade the CUDA PyTorch stack to 2.14 (#38641)
  _Files: `.github/workflows/_pr-test-rust-ext-build.yml`, `.github/workflows/release-pypi-nightly.yml`, `.github/workflows/release-pypi-pr.yml`, `.github/workflows/release-pypi.yml` _+28 more__
- **2026-10-04** [`9631f6f2d0`](https://github.com/sgl-project/sglang/commit/9631f6f2d0) [#40190](https://github.com/sgl-project/sglang/pull/40190)
  [XPU] Enable fused QK-norm + RoPE for Qwen3-MoE (#40190)
  _Files: `python/sglang/srt/models/qwen3_moe.py`, `test/registered/xpu/test_fused_inplace_qknorm_rope_xpu.py`_
- **2026-10-04** [`55c5415c17`](https://github.com/sgl-project/sglang/commit/55c5415c17) [#42041](https://github.com/sgl-project/sglang/pull/42041)
  [CP] Support scattered interleave CP inputs with expert parallelism (#42041)
  _Files: `python/sglang/srt/layers/cp/base.py`, `python/sglang/srt/layers/cp/interleave.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/cp/test_dsa_prefill_cp.py`_
- **2026-10-04** [`a3275295c4`](https://github.com/sgl-project/sglang/commit/a3275295c4) [#39818](https://github.com/sgl-project/sglang/pull/39818)
  [MoE] Use FlashInfer A2A for prefill instead of AG+RS (#39818)
  _Files: `python/sglang/srt/arg_groups/moe_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/arg_groups/resolution_hooks.py` _+8 more__
- **2026-10-03** [`749a89abd6`](https://github.com/sgl-project/sglang/commit/749a89abd6) [#42299](https://github.com/sgl-project/sglang/pull/42299)
  [LoRA] Reorganize kernels and add CODEOWNERS (#42299)
  _Files: `.github/CODEOWNERS`, `benchmark/kernels/lora_csgmv/tune_lora_csgmv.py`, `python/sglang/kernels/README.md`, `python/sglang/kernels/jit/csrc/lora/trtllm_lora_temp/kimi_k2_moe_fused_gate.cuh` _+79 more__
- **2026-10-03** [`f327f92424`](https://github.com/sgl-project/sglang/commit/f327f92424) [#34200](https://github.com/sgl-project/sglang/pull/34200)
  [AMD] Port CP V2 to the DeepSeek-V4 HIP backend (#34200)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/dsa/utils.py` _+10 more__
- **2026-10-03** [`7be5e3473c`](https://github.com/sgl-project/sglang/commit/7be5e3473c) [#42312](https://github.com/sgl-project/sglang/pull/42312)
  [Refactor] Drop the reduction-skip mechanisms stage boundaries no longer use (#42312)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/layer_boundary/boundary.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py` _+69 more__
- **2026-10-03** [`6faccf3e84`](https://github.com/sgl-project/sglang/commit/6faccf3e84) [#42309](https://github.com/sgl-project/sglang/pull/42309)
  [Refactor] Build the GLM-4, GLM-Image and Granite MoE hybrid decoders from stage boundaries (#42309)
  _Files: `python/sglang/srt/layers/layer_boundary/boundary.py`, `python/sglang/srt/layers/layer_boundary/factories.py`, `python/sglang/srt/layers/layer_boundary/residual/add_norm.py`, `python/sglang/srt/models/glm4.py` _+4 more__
- **2026-10-03** [`2c739b225b`](https://github.com/sgl-project/sglang/commit/2c739b225b) [#42306](https://github.com/sgl-project/sglang/pull/42306)
  [Fix] Jet-Nemotron build and Granite MoE hybrid final norm (#42306)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/models/granitemoehybrid.py`, `python/sglang/srt/models/jet_nemotron.py`_
- **2026-10-03** [`b7fc516986`](https://github.com/sgl-project/sglang/commit/b7fc516986) [#42305](https://github.com/sgl-project/sglang/pull/42305)
  [Fix] EXAONE MoE under DP attention and DeepEP (#42305)
  _Files: `python/sglang/srt/models/exaone_moe.py`_
- **2026-10-03** [`2fa17a6467`](https://github.com/sgl-project/sglang/commit/2fa17a6467) [#42304](https://github.com/sgl-project/sglang/pull/42304)
  [Refactor] Build the ERNIE 4.5 VL MoE and EXAONE MoE decoders from stage boundaries (#42304)
  _Files: `python/sglang/srt/models/ernie45_moe_vl.py`, `python/sglang/srt/models/exaone_moe.py`_
- **2026-10-03** [`f89ead192f`](https://github.com/sgl-project/sglang/commit/f89ead192f) [#42303](https://github.com/sgl-project/sglang/pull/42303)
  [Fix] EXAONE and ERNIE 4.5 VL MoE architecture, backend and PP issues (#42303)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/model_overrides/__init__.py`, `python/sglang/srt/arg_groups/model_overrides/ernie45_vl.py`, `python/sglang/srt/arg_groups/model_overrides/exaone.py` _+4 more__
- **2026-10-03** [`be20e7453c`](https://github.com/sgl-project/sglang/commit/be20e7453c) [#42302](https://github.com/sgl-project/sglang/pull/42302)
  [Fix] Step-3.5 DeepEP routed scaling and Sarvam shared expert under dense TP1 (#42302)
  _Files: `python/sglang/srt/models/sarvam_moe.py`, `python/sglang/srt/models/step3p5.py`_
- **2026-10-03** [`b157d548bb`](https://github.com/sgl-project/sglang/commit/b157d548bb) [#42301](https://github.com/sgl-project/sglang/pull/42301)
  [Refactor] Let stage boundaries complete every stage-output sum (#42301)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/layer_boundary/adapters/branch.py`, `python/sglang/srt/layers/layer_boundary/exit.py`, `python/sglang/srt/layers/layer_boundary/ops.py` _+59 more__
- **2026-10-03** [`d5a8d76bf5`](https://github.com/sgl-project/sglang/commit/d5a8d76bf5) [#42300](https://github.com/sgl-project/sglang/pull/42300)
  [Refactor] Drop TBO op methods that no strategy ever schedules (#42300)
  _Files: `python/sglang/srt/models/dots3_common/modeling.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/minimax_m2.py` _+1 more__
- **2026-10-03** [`391e665dab`](https://github.com/sgl-project/sglang/commit/391e665dab) [#41251](https://github.com/sgl-project/sglang/pull/41251)
  [Perf] Optimize DeepSeek V4.1 Flash Hopper paths and Blackwell prefill selection (#41251)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/activation.cuh`, `python/sglang/kernels/jit/csrc/gemm/marlin_moe/moe_wna16_marlin.cuh`, `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/kernels/ops/attention/__init__.py` _+27 more__
- **2026-10-02** [`2ec9e3b11d`](https://github.com/sgl-project/sglang/commit/2ec9e3b11d) [#42026](https://github.com/sgl-project/sglang/pull/42026)
  [eplb] Warm default-group NCCL P2P transports before KV-cache sizing (#42026)
  _Files: `python/sglang/srt/distributed/bootstrap.py`_
- **2026-10-02** [`6be84e1b72`](https://github.com/sgl-project/sglang/commit/6be84e1b72) [#42172](https://github.com/sgl-project/sglang/pull/42172)
  [Fix] Select the Marlin MoE runner for MiMo-V2 packed MXFP4 experts on SM90 (#42172)
  _Files: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`_
- **2026-10-02** [`29f6d408c0`](https://github.com/sgl-project/sglang/commit/29f6d408c0) [#42011](https://github.com/sgl-project/sglang/pull/42011)
  [AMD][V4.1][*/N] Fix shared-expert fusion accuracy and speed up MoE routing on ROCm (#42011)
  _Files: `python/sglang/kernels/ops/moe/rocm_router_gate.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/topk.py` _+3 more__
- **2026-10-02** [`4c4e352a4b`](https://github.com/sgl-project/sglang/commit/4c4e352a4b) [#40328](https://github.com/sgl-project/sglang/pull/40328)
  [unified-memory] Mark the write loc physical and check it at every write door (4/7) (#40328)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/cutedsl_mla_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` _+41 more__
- **2026-10-01** [`5423a4d885`](https://github.com/sgl-project/sglang/commit/5423a4d885) [#39388](https://github.com/sgl-project/sglang/pull/39388)
  [MegaMoE] Preserve W13 layout for ModelOpt NVFP4 experts (#39388)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`_
- **2026-10-01** [`80bb3fb651`](https://github.com/sgl-project/sglang/commit/80bb3fb651) [#41668](https://github.com/sgl-project/sglang/pull/41668)
  [Fix] Select the MXFP4 MoE runner for MiMo-V2 packed experts on SM100 (#41668)
  _Files: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-10-01** [`2ab1b537f8`](https://github.com/sgl-project/sglang/commit/2ab1b537f8) [#41966](https://github.com/sgl-project/sglang/pull/41966)
  [diffusion] docs: recommend docker for gpu deployments (#41966)
  _Files: `.agents/skills/cookbook-add-model/templates/diffusion-page.mdx.tmpl`, `docs/cookbook/diffusion/CircleStone/Anima.mdx`, `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `docs/cookbook/diffusion/Ernie-Image/Ernie-Image.mdx` _+14 more__
- **2026-10-01** [`6af651ea0c`](https://github.com/sgl-project/sglang/commit/6af651ea0c) [#40811](https://github.com/sgl-project/sglang/pull/40811)
  [AMD][Quark] Serve the Kimi-K3 MXFP4 checkpoint on ROCm (#40811)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`, `python/sglang/kernels/ops/attention/kda_fused_decode_aiter_hip.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py` _+6 more__
- **2026-09-30** [`e7f6a99313`](https://github.com/sgl-project/sglang/commit/e7f6a99313) [#41816](https://github.com/sgl-project/sglang/pull/41816)
  [Refactor] Add make_pp_layers so models stop handing their PP position down (#41816)
  _Files: `python/sglang/srt/models/apertus.py`, `python/sglang/srt/models/arcee.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_linear.py` _+46 more__
- **2026-09-30** [`c7fa37a5ca`](https://github.com/sgl-project/sglang/commit/c7fa37a5ca) [#41814](https://github.com/sgl-project/sglang/pull/41814)
  [Refactor] Let FusedMoE's weight-loading helpers read the layer's MoE-TP rank (#41814)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`_
- **2026-09-30** [`a09aedf1ca`](https://github.com/sgl-project/sglang/commit/a09aedf1ca) [#41812](https://github.com/sgl-project/sglang/pull/41812)
  [Refactor] Drop model placement attributes and parameters nothing reads (#41812)
  _Files: `python/sglang/srt/models/afmoe.py`, `python/sglang/srt/models/bailing_moe.py`, `python/sglang/srt/models/bailing_moe_linear.py`, `python/sglang/srt/models/bailing_moe_nextn.py` _+52 more__
- **2026-09-30** [`e289989933`](https://github.com/sgl-project/sglang/commit/e289989933) [#41807](https://github.com/sgl-project/sglang/pull/41807)
  [Fix] Shard MoE WNA16 and Quark INT4-FP8 weights by the MoE placement (#41807)
  _Files: `python/sglang/srt/layers/quantization/moe_wna16.py`, `python/sglang/srt/layers/quantization/quark_int4fp8_moe.py`, `test/registered/unit/layers/quantization/test_moe_wna16_ep_shard.py`_
- **2026-09-30** [`3f20738846`](https://github.com/sgl-project/sglang/commit/3f20738846) [#41806](https://github.com/sgl-project/sglang/pull/41806)
  [Fix] State the configured MoE-DP width in the weight-cache fingerprint (#41806)
  _Files: `python/sglang/srt/weight_cache/ipc_loader.py`, `test/registered/model_loading/test_weight_cache_daemon.py`_
- **2026-09-30** [`3a398442bf`](https://github.com/sgl-project/sglang/commit/3a398442bf) [#41308](https://github.com/sgl-project/sglang/pull/41308)
  dsv4.1-amd: serve DeepSeek-V4.1 on gfx950 (#41308)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/docs/references/environment_variables.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`, `python/sglang/kernels/ops/layernorm/mhc_post_split_h.py` _+35 more__
- **2026-09-30** [`9ee065e49a`](https://github.com/sgl-project/sglang/commit/9ee065e49a) [#41754](https://github.com/sgl-project/sglang/pull/41754)
  [Fix] Step-3.5: build the shared expert without TP under all-to-all MoE backends (#41754)
  _Files: `python/sglang/srt/models/step3p5.py`_
- **2026-09-30** [`843f50f5c1`](https://github.com/sgl-project/sglang/commit/843f50f5c1) [#41752](https://github.com/sgl-project/sglang/pull/41752)
  [Fix] Reduce the Sarvam dense MLP through its row-parallel projection (#41752)
  _Files: `python/sglang/srt/models/sarvam_moe.py`_
- **2026-09-30** [`ea855f0daf`](https://github.com/sgl-project/sglang/commit/ea855f0daf) [#41751](https://github.com/sgl-project/sglang/pull/41751)
  [Refactor] Leave decoder stacks through final_norm(skip_empty=True) (#41751)
  _Files: `python/sglang/srt/models/gigachat35.py`, `python/sglang/srt/models/interns2_mobius.py`, `python/sglang/srt/models/laguna.py`, `python/sglang/srt/models/minimax_m2.py` _+9 more__
- **2026-09-30** [`cb3ba2f2b7`](https://github.com/sgl-project/sglang/commit/cb3ba2f2b7) [#39618](https://github.com/sgl-project/sglang/pull/39618)
  [XPU] Add dynamic_expert_bias and track_state support (#39618)
  _Files: `python/sglang/srt/hardware_backend/xpu/kernels/fla/chunk_delta_h.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/xpu/test_kda_track_state_xpu.py`_
- **2026-09-30** [`fc9bdc8a3e`](https://github.com/sgl-project/sglang/commit/fc9bdc8a3e) [#41759](https://github.com/sgl-project/sglang/pull/41759)
  [MoE] Keep the moe_align_block_size pad fill inside sorted_token_ids (#41759)
  _Files: `python/sglang/kernels/aot/benchmark/bench_moe_align_block_size.py`, `python/sglang/kernels/aot/csrc/moe/moe_align_kernel.cu`, `python/sglang/kernels/aot/tests/test_moe_align.py`, `python/sglang/kernels/jit/csrc/moe/moe_align_kernel.cu` _+3 more__
- **2026-09-29** [`3d4953839c`](https://github.com/sgl-project/sglang/commit/3d4953839c) [#40980](https://github.com/sgl-project/sglang/pull/40980)
  [Fix] MoE: require TopK layer_id to ensure routed expert captures (#40980)
  _Files: `benchmark/kernels/fused_moe_triton/benchmark_sglang_fused_moe_triton.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/afmoe.py`, `python/sglang/srt/models/bailing_moe.py` _+19 more__
- **2026-09-29** [`fa090f7755`](https://github.com/sgl-project/sglang/commit/fa090f7755) [#41444](https://github.com/sgl-project/sglang/pull/41444)
  [MUSA] Fix fused MoE GEMV registration and torchada pin (#41444)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject_other.toml`, `python/sglang/kernels/aot/csrc/common_extension_musa.cc`, `python/sglang/kernels/aot/pyproject_musa.toml` _+1 more__
- **2026-09-29** [`0e586fd12d`](https://github.com/sgl-project/sglang/commit/0e586fd12d) [#39313](https://github.com/sgl-project/sglang/pull/39313)
  fuse shared experts with routed experts in MegaMoE's DeepGEMM (#39313)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/kernels/ops/moe/dsv4.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py` _+4 more__
- **2026-09-29** [`05817a40c9`](https://github.com/sgl-project/sglang/commit/05817a40c9) [#41464](https://github.com/sgl-project/sglang/pull/41464)
  [AMD] Fix GLM-5.3 quark MoE MI35x test runner config (#41464)
  _Files: `test/registered/e2e/moe/test_glm53_flash_quark_moe_mi35x.py`_
- **2026-09-29** [`dc1bd46802`](https://github.com/sgl-project/sglang/commit/dc1bd46802) [#40470](https://github.com/sgl-project/sglang/pull/40470)
  [diffusion] feat: support bounded exact conditioning cache across native models (#40470)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/caching-acceleration.mdx`, `docs/docs/sglang-diffusion/performance-optimization.mdx` _+47 more__
- **2026-09-29** [`6dad152490`](https://github.com/sgl-project/sglang/commit/6dad152490) [#41557](https://github.com/sgl-project/sglang/pull/41557)
  [Refactor] Document layer boundary contracts and integration (#41557)
  _Files: `.claude/skills/llm-torch-profiler-analysis/references/fuse-overlap-catalog.md`, `.claude/skills/llm-torch-profiler-analysis/scripts/triage_kernel_helpers.py`, `docs/docs.json`, `docs/docs/advanced_features/prefill_cp.mdx` _+31 more__
- **2026-09-29** [`49e7bd179d`](https://github.com/sgl-project/sglang/commit/49e7bd179d) [#41556](https://github.com/sgl-project/sglang/pull/41556)
  [Refactor] Group layer boundary unit tests (#41556)
  _Files: `test/registered/unit/layer_boundary/test_aux_capture_deferred_allreduce.py`, `test/registered/unit/layer_boundary/test_aux_hidden_states.py`, `test/registered/unit/layer_boundary/test_batch_owned_residual.py`, `test/registered/unit/layer_boundary/test_boundary_edges.py` _+23 more__
- **2026-09-29** [`9b89b96230`](https://github.com/sgl-project/sglang/commit/9b89b96230) [#41553](https://github.com/sgl-project/sglang/pull/41553)
  [Refactor] Migrate specialized decoder and overlap boundaries (#41553)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/layernorm_sp_hook.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py` _+57 more__
- **2026-09-29** [`49b5e76e45`](https://github.com/sgl-project/sglang/commit/49b5e76e45) [#41552](https://github.com/sgl-project/sglang/pull/41552)
  [Refactor] Construct independent decoder stage boundaries (#41552)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/boundary_reduction.py`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/exec_.py` _+75 more__
- **2026-09-29** [`acffb0d20d`](https://github.com/sgl-project/sglang/commit/acffb0d20d) [#41551](https://github.com/sgl-project/sglang/pull/41551)
  [Refactor] Select reduction fusion at the consumer (#41551)
  _Files: `python/sglang/srt/layers/communicator/__init__.py`, `python/sglang/srt/layers/communicator/boundary.py`, `python/sglang/srt/layers/communicator/fusions/cutedsl.py`, `python/sglang/srt/layers/communicator/layer.py` _+40 more__
- **2026-09-29** [`cb1fa3c399`](https://github.com/sgl-project/sglang/commit/cb1fa3c399) [#41550](https://github.com/sgl-project/sglang/pull/41550)
  [Refactor] Capture auxiliary states at residual reads (#41550)
  _Files: `python/sglang/srt/layers/aux_hidden_states.py`, `python/sglang/srt/layers/communicator/boundary.py`, `python/sglang/srt/layers/communicator/fusions/cutedsl.py`, `python/sglang/srt/layers/communicator/layer.py` _+25 more__
- **2026-09-29** [`42f58b4da7`](https://github.com/sgl-project/sglang/commit/42f58b4da7) [#41549](https://github.com/sgl-project/sglang/pull/41549)
  [Refactor] Carry residual state across stage boundaries (#41549)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/communicator/boundary.py`, `python/sglang/srt/layers/communicator/layer.py`, `python/sglang/srt/layers/communicator/ops.py` _+69 more__
- **2026-09-29** [`6f72cc3b64`](https://github.com/sgl-project/sglang/commit/6f72cc3b64) [#41548](https://github.com/sgl-project/sglang/pull/41548)
  [Refactor] Centralize decoder output access (#41548)
  _Files: `python/sglang/srt/layers/communicator/__init__.py`, `python/sglang/srt/layers/communicator/boundary.py`, `python/sglang/srt/layers/communicator/layer.py`, `python/sglang/srt/layers/communicator/ops.py` _+48 more__
- **2026-09-29** [`0a8ca85565`](https://github.com/sgl-project/sglang/commit/0a8ca85565) [#41547](https://github.com/sgl-project/sglang/pull/41547)
  [Refactor] Group communicator fusion and CP adapters (#41547)
  _Files: `python/sglang/srt/arg_groups/model_overrides/deepseek_v2.py`, `python/sglang/srt/layers/communicator/adapters/context_parallel.py`, `python/sglang/srt/layers/communicator/fusions/__init__.py`, `python/sglang/srt/layers/communicator/fusions/cutedsl.py` _+8 more__
- **2026-09-28** [`fa443412c5`](https://github.com/sgl-project/sglang/commit/fa443412c5) [#41161](https://github.com/sgl-project/sglang/pull/41161)
  [AMD] [GLM5] Fuse shared expert into AITER MoE on gfx950 (#41161)
  _Files: `python/sglang/srt/models/glm5_next.py`, `test/registered/kernels/ops/moe/test_glm53_shared_expert_fusion.py`, `test/registered/unit/layers/moe/test_fused_shared_expert_scaling.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`_
- **2026-09-28** [`85be04978d`](https://github.com/sgl-project/sglang/commit/85be04978d) [#40943](https://github.com/sgl-project/sglang/pull/40943)
  [AMD][DSV4] moe: enable shared-expert fusion on the grouped-topk path (megamoe) (#40943)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-09-28** [`6be9c78cf4`](https://github.com/sgl-project/sglang/commit/6be9c78cf4) [#40664](https://github.com/sgl-project/sglang/pull/40664)
  [Intel GPU] Xpu/weekly simple model enablement 2026 09 21 (#40664)
  _Files: `.pre-commit-config.yaml`, `python/sglang/check_env.py`, `python/sglang/multimodal_gen/test/server/consistency_thresholds/intel_xpu_b60.json`, `python/sglang/multimodal_gen/test/server/perf_baselines/xpu_b60.json` _+8 more__
- **2026-09-28** [`cc012abd21`](https://github.com/sgl-project/sglang/commit/cc012abd21) [#41002](https://github.com/sgl-project/sglang/pull/41002)
  [CI] fix CI regression on xeon (#41002)
  _Files: `test/registered/cpu/test_subblock_sparse_attention.py`, `test/registered/moe/test_hash_topk.py`_

## Multimodal  (50 commits)

- **2026-10-05** [`efb62ce269`](https://github.com/sgl-project/sglang/commit/efb62ce269) [#40158](https://github.com/sgl-project/sglang/pull/40158)
  [diffusion] fix: resolve QKV layout inference for MiniMax-H3 checkpoints (#40158)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_comfyui_h3.py`_
- **2026-10-05** [`150f568900`](https://github.com/sgl-project/sglang/commit/150f568900) [#41710](https://github.com/sgl-project/sglang/pull/41710)
  [diffusion] kernels: stop specializing on per-request sequence lengths (#41710)
  _Files: `python/sglang/kernels/kda_kernels/layernorm_modulate_triton.py`, `python/sglang/kernels/ops/diffusion/layout/ulysses_qkv_triton.py`, `python/sglang/kernels/ops/diffusion/layout/wan_causal_cache_triton.py`, `python/sglang/kernels/ops/diffusion/modulate/scale_shift_triton.py` _+2 more__
- **2026-10-05** [`a977e3b9d5`](https://github.com/sgl-project/sglang/commit/a977e3b9d5) [#41721](https://github.com/sgl-project/sglang/pull/41721)
  [diffusion] optimization: stream an oversized DiT in auto mode instead of OOMing (#41721)
  _Files: `python/sglang/multimodal_gen/runtime/loader/utils.py`, `python/sglang/multimodal_gen/runtime/server_args/auto_tune.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`, `python/sglang/multimodal_gen/test/unit/test_weight_utils.py`_
- **2026-10-05** [`ad3e80d4de`](https://github.com/sgl-project/sglang/commit/ad3e80d4de) [#41833](https://github.com/sgl-project/sglang/pull/41833)
  [diffusion] chore: warm the image writer and the HTTP route models at startup (#41833)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/test/unit/test_health_warmup_gate.py` _+1 more__
- **2026-10-05** [`c83c84b422`](https://github.com/sgl-project/sglang/commit/c83c84b422) [#41722](https://github.com/sgl-project/sglang/pull/41722)
  [diffusion] chore: keep the DiT off component offload under explicit multi-GPU fsdp (#41722)
  _Files: `docs/cookbook/diffusion/Wan/Wan2.1.mdx`, `docs/cookbook/diffusion/Wan/Wan2.2.mdx`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-10-05** [`23bf107469`](https://github.com/sgl-project/sglang/commit/23bf107469) [#22441](https://github.com/sgl-project/sglang/pull/22441)
  [diffusion] optimization: cache LTX-2 RoPE coords to avoid per-step recompute (#22441)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_bcg_coords.py`_
- **2026-10-05** [`91f9bf8d17`](https://github.com/sgl-project/sglang/commit/91f9bf8d17) [#22813](https://github.com/sgl-project/sglang/pull/22813)
  [diffusion] fix: fix scheduler host not working when ipv6 in multi modal gen (#22813)
  _Files: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-10-05** [`f20f8e120d`](https://github.com/sgl-project/sglang/commit/f20f8e120d) [#39523](https://github.com/sgl-project/sglang/pull/39523)
  [diffusion] model: restore folded H3 GGUF patch embedding (#39523)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/minimax_h3_qwen3vl.py`, `python/sglang/multimodal_gen/test/unit/test_gguf_diffusion.py`_
- **2026-10-05** [`83a6e1d39b`](https://github.com/sgl-project/sglang/commit/83a6e1d39b) [#42227](https://github.com/sgl-project/sglang/pull/42227)
  [diffusion] docs: keep model compatibility details in cookbook recipes (#42227)
  _Files: `docs/cookbook/diffusion/inclusionAI/Ming-Image.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`_
- **2026-10-05** [`860ebe720e`](https://github.com/sgl-project/sglang/commit/860ebe720e) [#40761](https://github.com/sgl-project/sglang/pull/40761)
  [diffusion] fix: skip warmup preferred preload when it would OOM (#40761)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_residency_strategies.py`, `python/sglang/multimodal_gen/test/unit/test_component_residency.py`_
- **2026-10-05** [`8663e3b670`](https://github.com/sgl-project/sglang/commit/8663e3b670) [#40095](https://github.com/sgl-project/sglang/pull/40095)
  [diffusion] optimization: avoid full-video clone in VAE post-processing for MiniMax-H3 (#40095)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/klvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/processor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/decoding.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_vae_processor.py`_
- **2026-10-05** [`d349e672bc`](https://github.com/sgl-project/sglang/commit/d349e672bc) [#41832](https://github.com/sgl-project/sglang/pull/41832)
  [diffusion] feat: recycle warmup-only entries of conditioning-cache at the first served store (#41832)
  _Files: `python/sglang/multimodal_gen/runtime/cache/conditioning.py`, `python/sglang/multimodal_gen/test/unit/test_conditioning_cache.py`_
- **2026-10-05** [`7352073ec6`](https://github.com/sgl-project/sglang/commit/7352073ec6) [#37549](https://github.com/sgl-project/sglang/pull/37549)
  [diffusion] feat: support --async-output-save to overlap output saving with the next request (#37549)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/performance-optimization.mdx`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py` _+4 more__
- **2026-10-05** [`f048d5aa4b`](https://github.com/sgl-project/sglang/commit/f048d5aa4b) [#35857](https://github.com/sgl-project/sglang/pull/35857)
  [diffusion] feat: add community LoRA recipes and Kohya mapping (#35857)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/format_adapter.py`_
- **2026-10-05** [`0263fdacb2`](https://github.com/sgl-project/sglang/commit/0263fdacb2) [#41641](https://github.com/sgl-project/sglang/pull/41641)
  [diffusion] fix: keep generic warmup valid for step-floored models and stop reporting a failed warmup as warm (#41641)
  _Files: `python/sglang/multimodal_gen/configs/sample/minimax_h3.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/runtime/entrypoints/diffusion_generator.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py` _+5 more__
- **2026-10-05** [`dd2ffdb680`](https://github.com/sgl-project/sglang/commit/dd2ffdb680) [#42226](https://github.com/sgl-project/sglang/pull/42226)
  [diffusion] nightly: keep nightly regression baselines on a comparable methodology (#42226)
  _Files: `python/sglang/multimodal_gen/test/unit/test_diffusion_nightly_comparison.py`, `scripts/ci/utils/diffusion/generate_diffusion_dashboard.py`_
- **2026-10-05** [`f218798006`](https://github.com/sgl-project/sglang/commit/f218798006) [#42505](https://github.com/sgl-project/sglang/pull/42505)
  [diffusion] CI: relax the load latency check and extend the 2-GPU retry deadline (#42505)
  _Files: `.github/workflows/pr-test-multimodal-gen.yml`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/server/test_server_utils.py`, `python/sglang/multimodal_gen/test/server/testcase_configs.py` _+2 more__
- **2026-10-04** [`affa261e3d`](https://github.com/sgl-project/sglang/commit/affa261e3d) [#42171](https://github.com/sgl-project/sglang/pull/42171)
  [diffusion] feat: enable cuda graphs for observation encoding and denoising steps for action models (#42171)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/flux3_action.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux3.py`, `python/sglang/multimodal_gen/runtime/pipelines/flux3_action.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/flux3_action.py` _+2 more__
- **2026-10-04** [`279d3f3888`](https://github.com/sgl-project/sglang/commit/279d3f3888) [#42174](https://github.com/sgl-project/sglang/pull/42174)
  [diffusion] feat: load ComfyUI/ai-toolkit fused `gate_up` LoRAs and diffusers metadata alpha for qwen-image-2.1 (#42174)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/qwen_image21.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/peft_adapter.py`, `python/sglang/multimodal_gen/test/unit/test_lora_peft.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21_cuda.py`_
- **2026-10-04** [`44fac689f5`](https://github.com/sgl-project/sglang/commit/44fac689f5) [#41895](https://github.com/sgl-project/sglang/pull/41895)
  [diffusion] optimization: decode json pixel lists to numpy at the entrypoint (#41895)
  _Files: `docs/cookbook/vla/FLUX/FLUX-3-Action.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/action/protocol.py`, `python/sglang/multimodal_gen/test/unit/test_flux3_action.py`_
- **2026-10-04** [`1e490772e5`](https://github.com/sgl-project/sglang/commit/1e490772e5) [#42471](https://github.com/sgl-project/sglang/pull/42471)
  [diffusion] fix: pin the JoyAI-Echo overlay's source revision (#42471)
  _Files: `python/sglang/multimodal_gen/runtime/utils/model_overlay.py`, `python/sglang/multimodal_gen/test/unit/test_model_overlay.py`_
- **2026-10-04** [`ba68306256`](https://github.com/sgl-project/sglang/commit/ba68306256) [#41797](https://github.com/sgl-project/sglang/pull/41797)
  [diffusion] feat: let requests choose the video libx264 preset (#41797)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `python/sglang/multimodal_gen/apps/webui/minimax_h3.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/runtime/entrypoints/diffusion_generator.py` _+9 more__
- **2026-10-04** [`1315d171a0`](https://github.com/sgl-project/sglang/commit/1315d171a0) [#42329](https://github.com/sgl-project/sglang/pull/42329)
  [Diffusion][CI] Add missing B200 Cirrascale runner E2E baselines (#42329)
  _Files: `python/sglang/multimodal_gen/test/runner/PERFORMANCE.md`, `python/sglang/multimodal_gen/test/server/perf_baselines/b200.json`, `python/sglang/multimodal_gen/test/unit/test_runner_perf_baselines.py`_
- **2026-10-03** [`41c6ffea89`](https://github.com/sgl-project/sglang/commit/41c6ffea89) [#42240](https://github.com/sgl-project/sglang/pull/42240)
  [diffusion] fix: keep residual_gate_add on the JIT CUDA path for cont… (#42240)
  _Files: `python/sglang/kernels/kda_kernels/residual_gate_add_jit.py`_
- **2026-10-03** [`65c7425a56`](https://github.com/sgl-project/sglang/commit/65c7425a56) [#41622](https://github.com/sgl-project/sglang/pull/41622)
  [diffusion] fix: respect explicit residency over pipeline preload hints (#41622)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py`, `python/sglang/multimodal_gen/test/unit/test_component_residency.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py` _+1 more__
- **2026-10-02** [`cbe070b6bf`](https://github.com/sgl-project/sglang/commit/cbe070b6bf) [#42278](https://github.com/sgl-project/sglang/pull/42278)
  [Docs][AMD] Update GLM-5.2 MI355X daily image to 20260930 (#42278)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`_
- **2026-10-02** [`bb9a820f09`](https://github.com/sgl-project/sglang/commit/bb9a820f09) [#41711](https://github.com/sgl-project/sglang/pull/41711)
  [diffusion] chore: make perf dump one writer per replica with no first-request NCCL setup (#41711)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/utils/perf_logger.py`, `python/sglang/multimodal_gen/test/unit/test_perf_dump_write.py`, `python/sglang/multimodal_gen/test/unit/test_performance_metrics.py`_
- **2026-10-02** [`544e46c080`](https://github.com/sgl-project/sglang/commit/544e46c080) [#41979](https://github.com/sgl-project/sglang/pull/41979)
  [AMD][CI] Fix VLM MMMU nightly max_tokens for CoT prompt (#41979)
  _Files: `test/registered/amd/accuracy/mi30x/test_vlms_mmmu_eval_amd.py`_
- **2026-10-02** [`e7d9c0299b`](https://github.com/sgl-project/sglang/commit/e7d9c0299b) [#42201](https://github.com/sgl-project/sglang/pull/42201)
  [Docs] Keep the last CUDA 12 image tag fixed during install version bumps (#42201)
  _Files: `docs/docs/get-started/install.mdx`, `scripts/release/README.md`, `scripts/release/bump_docs_install_version.py`_
- **2026-10-02** [`b906cd3f45`](https://github.com/sgl-project/sglang/commit/b906cd3f45) [#41967](https://github.com/sgl-project/sglang/pull/41967)
  doc: refresh README (#41967)
  _Files: `README.md`, `docs/docs/sglang-diffusion/index.mdx`, `docs/docs/sglang-diffusion/installation.mdx`_
- **2026-10-01** [`7be0e85658`](https://github.com/sgl-project/sglang/commit/7be0e85658) [#41500](https://github.com/sgl-project/sglang/pull/41500)
  [CI][NPU][Diffusion] Bump ascend consistency GT to the CANN 9.1.0 baseline (#41500)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `docker/npu.Dockerfile`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-10-01** [`77b64e353f`](https://github.com/sgl-project/sglang/commit/77b64e353f) [#41459](https://github.com/sgl-project/sglang/pull/41459)
  [KDA+Kimi K3] Speed up LTX-2.3 QK norm and split RoPE on H200 (#41459)
  _Files: `python/sglang/kernels/kda_kernels/csrc/diffusion/ltx2_qknorm_split_rope_sm90.cuh`, `python/sglang/kernels/kda_kernels/ltx2_qknorm_split_rope_jit.py`, `test/registered/kernels/ops/diffusion/test_rope_ltx2.py`_
- **2026-10-01** [`baae0195d9`](https://github.com/sgl-project/sglang/commit/baae0195d9) [#41936](https://github.com/sgl-project/sglang/pull/41936)
  [ci] fix renderer image publish (#41936)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/release-docker-renderer.yml`, `docker/renderer.Dockerfile`_
- **2026-09-30** [`488869c2d0`](https://github.com/sgl-project/sglang/commit/488869c2d0) [#41667](https://github.com/sgl-project/sglang/pull/41667)
  [Fix] Keep MiMo-V2 processor available without TorchCodec (#41667)
  _Files: `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`_
- **2026-09-30** [`bd66ce343e`](https://github.com/sgl-project/sglang/commit/bd66ce343e) [#41689](https://github.com/sgl-project/sglang/pull/41689)
  [diffusion] nightly: measure every framework with one client end-to-end methodology (#41689)
  _Files: `python/sglang/multimodal_gen/test/unit/test_diffusion_nightly_comparison.py`, `scripts/ci/utils/diffusion/comparison_configs.json`, `scripts/ci/utils/diffusion/generate_diffusion_dashboard.py`, `scripts/ci/utils/diffusion/run_comparison.py`_
- **2026-09-30** [`45c8ddddd3`](https://github.com/sgl-project/sglang/commit/45c8ddddd3) [#41825](https://github.com/sgl-project/sglang/pull/41825)
  [diffusion] feat: check the final MP4 in-process instead of spawning ffprobe (#41825)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_output_validation.py`_
- **2026-09-30** [`0931a72eb2`](https://github.com/sgl-project/sglang/commit/0931a72eb2) [#34365](https://github.com/sgl-project/sglang/pull/34365)
  [diffusion] feat: support MiniMax H3 RL  (#34365)
  _Files: `python/sglang/multimodal_gen/configs/sample/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/denoise_loop.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/minimax_h3_rollout.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`_
- **2026-09-30** [`be66c1b460`](https://github.com/sgl-project/sglang/commit/be66c1b460) [#41824](https://github.com/sgl-project/sglang/pull/41824)
  [NPU][CI] Fix stale multimodal-gen job name in fast-fail health check (#41824)
  _Files: `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`_
- **2026-09-30** [`e5cec303ae`](https://github.com/sgl-project/sglang/commit/e5cec303ae) [#41777](https://github.com/sgl-project/sglang/pull/41777)
  [Fix] Restore deferred layer dumps and pin SentencePiece for InternVL (#41777)
  _Files: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml` _+3 more__
- **2026-09-29** [`bf80732b92`](https://github.com/sgl-project/sglang/commit/bf80732b92) [#41703](https://github.com/sgl-project/sglang/pull/41703)
  Fix pip install: exclude multimodal_gen/.claude symlink from package data (#41703)
  _Files: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml` _+1 more__
- **2026-09-29** [`98fce73d5b`](https://github.com/sgl-project/sglang/commit/98fce73d5b) [#41650](https://github.com/sgl-project/sglang/pull/41650)
  [XPU] publish nightly docker image with sgl-kernel-xpu built from main (#41650)
  _Files: `.github/workflows/release-docker-intel-xpu-nightly.yml`, `docker/xpu.Dockerfile`_
- **2026-09-29** [`e49d7fb170`](https://github.com/sgl-project/sglang/commit/e49d7fb170) [#41608](https://github.com/sgl-project/sglang/pull/41608)
  Remove GLM-4.1V-9B-Thinking from encoder DP MMMU test (#41608)
  _Files: `test/registered/vlm/test_encoder_dp.py`_
- **2026-09-28** [`26d7539799`](https://github.com/sgl-project/sglang/commit/26d7539799) [#41597](https://github.com/sgl-project/sglang/pull/41597)
  [Docs][AMD] Update GLM-5.2 MI355X daily image (#41597)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`_
- **2026-09-28** [`b07cb9e9e7`](https://github.com/sgl-project/sglang/commit/b07cb9e9e7) [#40987](https://github.com/sgl-project/sglang/pull/40987)
  [NVIDIA] Update deepgemm, deep-ep, sgl-kernel in CUDA 13.4 image, use cuda base image (#40987)
  _Files: `docker/Dockerfile.cu134`_
- **2026-09-28** [`2e7e0802f4`](https://github.com/sgl-project/sglang/commit/2e7e0802f4) [#41339](https://github.com/sgl-project/sglang/pull/41339)
  [diffusion] Qwen-Image 2.1: fuse Q/K RMSNorm + RoPE + KV packing into one CUDA kernel and project Q/K/V with one packed GEMM (#41339)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_complex_rope.cuh`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/qknorm_complex_rope_jit.py` _+5 more__
- **2026-09-28** [`090439bf8f`](https://github.com/sgl-project/sglang/commit/090439bf8f) [#41540](https://github.com/sgl-project/sglang/pull/41540)
  [diffusion] docs: consolidate Qwen-Image 2.1 guidance in its cookbook (#41540)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-2.1.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `python/sglang/multimodal_gen/README.md`_
- **2026-09-28** [`6caf0ff4ae`](https://github.com/sgl-project/sglang/commit/6caf0ff4ae) [#39539](https://github.com/sgl-project/sglang/pull/39539)
  perf(multimodal): offload CPU feature hashing with bounded admission (#39539)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/hash_executor.py`, `test/registered/unit/managers/test_mm_hashes.py`_
- **2026-09-28** [`c02eaadeb2`](https://github.com/sgl-project/sglang/commit/c02eaadeb2) [#40439](https://github.com/sgl-project/sglang/pull/40439)
  [diffusion] optimization: populate cpu weight stores before host registration to speedup layerwise-offload initialization (#40439)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-09-28** [`6c4f36e47a`](https://github.com/sgl-project/sglang/commit/6c4f36e47a) [#39679](https://github.com/sgl-project/sglang/pull/39679)
  Rust server unify datapath for mm and generate requests (#39679)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/rust_server/multimodal.py`, `python/sglang/srt/rust_server/server.py`, `python/sglang/test/server_fixtures/rust_mm_transport_fixture.py` _+49 more__
- **2026-09-28** [`8b2ca8ecc2`](https://github.com/sgl-project/sglang/commit/8b2ca8ecc2) [#38762](https://github.com/sgl-project/sglang/pull/38762)
  [diffusion] feat: support multiple task types for pipelines (#38762)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py` _+21 more__

## Prefill / Decode Disaggregation  (44 commits)

- **2026-10-05** [`734cf3cf3b`](https://github.com/sgl-project/sglang/commit/734cf3cf3b) [#41691](https://github.com/sgl-project/sglang/pull/41691)
  [PD] Reload NIXL peer metadata after the peer is invalidated (#41691)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-10-04** [`148da8e77d`](https://github.com/sgl-project/sglang/commit/148da8e77d) [#42051](https://github.com/sgl-project/sglang/pull/42051)
  [PD] Validate decode state layout once at registration (#42051)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`, `test/registered/unit/disaggregation/test_prefill_complete_integration.py`_
- **2026-10-04** [`bc5a055dd7`](https://github.com/sgl-project/sglang/commit/bc5a055dd7) [#42391](https://github.com/sgl-project/sglang/pull/42391)
  [diffusion] move kernel validation into launchers and simplify dispatch (#42391)
  _Files: `.github/workflows/pr-test-amd.yml`, `python/sglang/kernels/jit/csrc/diffusion/gelu_tanh_cat.cuh`, `python/sglang/kernels/jit/csrc/diffusion/helios_qk_rope.cuh`, `python/sglang/kernels/jit/csrc/diffusion/interleaved_rope_fp64.cuh` _+70 more__
- **2026-10-04** [`937c0a6cfe`](https://github.com/sgl-project/sglang/commit/937c0a6cfe) [#39479](https://github.com/sgl-project/sglang/pull/39479)
  Fix unified HiCache physical transfers (#39479)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/managers/cache_controller.py` _+37 more__
- **2026-10-04** [`f24db66729`](https://github.com/sgl-project/sglang/commit/f24db66729) [#41786](https://github.com/sgl-project/sglang/pull/41786)
  [PD] Publish prefill DP rank whenever forced lookup is enabled (#41786)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `test/registered/unit/disaggregation/test_register_to_bootstrap.py`_
- **2026-10-04** [`169e6223ef`](https://github.com/sgl-project/sglang/commit/169e6223ef) [#42454](https://github.com/sgl-project/sglang/pull/42454)
  [PD] Drop the removed MooncakeKVSender args from test_prefill_complete_integration (#42454)
  _Files: `test/registered/unit/disaggregation/test_prefill_complete_integration.py`_
- **2026-10-03** [`10edb05e72`](https://github.com/sgl-project/sglang/commit/10edb05e72) [#42348](https://github.com/sgl-project/sglang/pull/42348)
  [Refactor] Let the remaining placement consumers read the parallel context (#42348)
  _Files: `docs/docs/advanced_features/dp_dpa_smg_guide.mdx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/fields/parallel.py`, `python/sglang/srt/arg_groups/model_override_base.py` _+69 more__
- **2026-10-03** [`df53c978f1`](https://github.com/sgl-project/sglang/commit/df53c978f1) [#42354](https://github.com/sgl-project/sglang/pull/42354)
  [mem_cache] Run mamba models on `UnifiedRadixCache` when the radix cache is disabled (#42354)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/auxiliary_state.py`, `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/managers/schedule_policy.py` _+9 more__
- **2026-10-03** [`8bf780dda5`](https://github.com/sgl-project/sglang/commit/8bf780dda5) [#41128](https://github.com/sgl-project/sglang/pull/41128)
  feat(metrics): expose deferred decode KV release metrics (#41128)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/observability/metrics_collector.py`, `test/registered/unit/disaggregation/test_deferred_decode_kv_release.py` _+2 more__
- **2026-10-03** [`aaf7ebe077`](https://github.com/sgl-project/sglang/commit/aaf7ebe077) [#42274](https://github.com/sgl-project/sglang/pull/42274)
  Advertise the KV-event replay endpoint in /server_info (#42274)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/observability.py`, `python/sglang/srt/runtime_context.py`, `test/registered/unit/disaggregation/test_kv_events.py`_
- **2026-10-03** [`6acf2f4736`](https://github.com/sgl-project/sglang/commit/6acf2f4736) [#42035](https://github.com/sgl-project/sglang/pull/42035)
  [PD] Keep ingesting requests while a prefill forward result is pending (#42035)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+7 more__
- **2026-10-03** [`5b5d721239`](https://github.com/sgl-project/sglang/commit/5b5d721239) [#40703](https://github.com/sgl-project/sglang/pull/40703)
  [PD] Add opt-in prefill-complete decode KV allocation (#40703)
  _Files: `docs/docs/advanced_features/pd_disaggregation.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/disagg.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py` _+15 more__
- **2026-10-03** [`8293f9af54`](https://github.com/sgl-project/sglang/commit/8293f9af54) [#37077](https://github.com/sgl-project/sglang/pull/37077)
  [PD] Centralize drain-aware abort acknowledgements (#37077)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py` _+7 more__
- **2026-10-02** [`8a328e867b`](https://github.com/sgl-project/sglang/commit/8a328e867b) [#42202](https://github.com/sgl-project/sglang/pull/42202)
  [mem_cache] Rename the tree's request-level `insert_req` to `checkpoint` (#42202)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/allocation.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` _+27 more__
- **2026-10-02** [`7dd93b01a5`](https://github.com/sgl-project/sglang/commit/7dd93b01a5) [#42113](https://github.com/sgl-project/sglang/pull/42113)
  [PD] Make the prebuilt last-token H2D copy non-blocking under overlap (#42113)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`_
- **2026-10-02** [`07e1a4f082`](https://github.com/sgl-project/sglang/commit/07e1a4f082) [#42194](https://github.com/sgl-project/sglang/pull/42194)
  [mem_cache] Skip the release-time insert on optimistic prefill requeue; make `refresh_fill_ids` public (#42194)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/req.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py` _+8 more__
- **2026-10-02** [`1db33bc367`](https://github.com/sgl-project/sglang/commit/1db33bc367) [#42005](https://github.com/sgl-project/sglang/pull/42005)
  [PD][NIXL] Fix prepared dlists for KV entries of different lengths (DeepSeek-V4) (#42005)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_dsv4_kv_slots.py`_
- **2026-10-02** [`50be533d09`](https://github.com/sgl-project/sglang/commit/50be533d09) [#41520](https://github.com/sgl-project/sglang/pull/41520)
  [mem_cache] Rename `cache_unfinished_req` to `checkpoint_req` and count cache hits only when a request finishes (#41520)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py` _+45 more__
- **2026-10-02** [`df530479c6`](https://github.com/sgl-project/sglang/commit/df530479c6) [#40330](https://github.com/sgl-project/sglang/pull/40330)
  [unified-memory] Stride the KV translate kernel and route every translate through it (6/7) (#40330)
  _Files: `python/sglang/kernels/ops/memory/virtual_slot.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py`, `python/sglang/srt/mem_cache/allocator/unified_mamba.py` _+7 more__
- **2026-10-01** [`a0fcebb3bb`](https://github.com/sgl-project/sglang/commit/a0fcebb3bb) [#37827](https://github.com/sgl-project/sglang/pull/37827)
  NIXL: Use stride desc API (#37827)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-10-01** [`1bbce57d9e`](https://github.com/sgl-project/sglang/commit/1bbce57d9e) [#41528](https://github.com/sgl-project/sglang/pull/41528)
  [NPU] [Diffusion] Fix NPU multimodal-gen CI (#41528)
  _Files: `python/sglang/multimodal_gen/runtime/disaggregation/scheduler_mixin.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/text_encoding.py`, `python/sglang/multimodal_gen/test/server/ascend/perf_baselines_npu.json`, `python/sglang/multimodal_gen/test/test_utils.py` _+1 more__
- **2026-10-01** [`1a0250c5b6`](https://github.com/sgl-project/sglang/commit/1a0250c5b6) [#41607](https://github.com/sgl-project/sglang/pull/41607)
  [Disagg] Validate state strides before Mooncake transfers (#41607)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-10-01** [`9c3262d855`](https://github.com/sgl-project/sglang/commit/9c3262d855) [#39166](https://github.com/sgl-project/sglang/pull/39166)
  [AMD][DSV4] feat: enable PD-disagg with fp8 unified_kv on gfx950 (#39166)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `test/manual/dsv4/test_dsv4_pd_disagg_fp8_nixl.py` _+4 more__
- **2026-10-01** [`947fee9384`](https://github.com/sgl-project/sglang/commit/947fee9384) [#41924](https://github.com/sgl-project/sglang/pull/41924)
  [PD] Fix block scale registration for mixed full/SWA KV dtypes (#41924)
  _Files: `python/sglang/srt/disaggregation/utils.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-10-01** [`b62b21e7f4`](https://github.com/sgl-project/sglang/commit/b62b21e7f4) [#41393](https://github.com/sgl-project/sglang/pull/41393)
  [HiCache][PD] fix: keep decode load-back polling out of rank-local collectives (#41393)
  _Files: `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-09-30** [`b0cc246ff8`](https://github.com/sgl-project/sglang/commit/b0cc246ff8) [#41811](https://github.com/sgl-project/sglang/pull/41811)
  [Refactor] Drop placement values nothing reads (#41811)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/flashmla_backend.py` _+17 more__
- **2026-09-30** [`aec4b799e6`](https://github.com/sgl-project/sglang/commit/aec4b799e6) [#41451](https://github.com/sgl-project/sglang/pull/41451)
  [PD][Mamba] fix: free the COW mamba slot of decode requests dropped before preallocation (#41451)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-09-30** [`28c5e7f5cb`](https://github.com/sgl-project/sglang/commit/28c5e7f5cb) [#41380](https://github.com/sgl-project/sglang/pull/41380)
  [Fix] Stop PD-decode queue_time from counting decode time before a retraction (#41380)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_priority_scheduling_disaggregation.py`_
- **2026-09-30** [`964c45cf31`](https://github.com/sgl-project/sglang/commit/964c45cf31) [#41717](https://github.com/sgl-project/sglang/pull/41717)
  [NPU] [DOC]: add Kimi-K3 NPU PD disaggregation recipes (#41717)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-09-30** [`51cae5f303`](https://github.com/sgl-project/sglang/commit/51cae5f303) [#41450](https://github.com/sgl-project/sglang/pull/41450)
  [HiCache][PD] fix: clamp the decode restore to the prefix promised to prefill (#41450)
  _Files: `python/sglang/srt/disaggregation/decode_hicache_mixin.py`_
- **2026-09-30** [`ec0006673a`](https://github.com/sgl-project/sglang/commit/ec0006673a) [#37787](https://github.com/sgl-project/sglang/pull/37787)
  [NPU] Add decode context parallel support for dsa models (#37787)
  _Files: `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/disaggregation/prefill.py` _+17 more__
- **2026-09-30** [`8c75ad9e62`](https://github.com/sgl-project/sglang/commit/8c75ad9e62) [#41678](https://github.com/sgl-project/sglang/pull/41678)
  chore: bump mooncake version to 0.3.13.post1 (#41678)
  _Files: `docker/Dockerfile`, `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-09-30** [`f85ca901e2`](https://github.com/sgl-project/sglang/commit/f85ca901e2) [#41025](https://github.com/sgl-project/sglang/pull/41025)
  [AMD][DI][CI] Fix four failures in the MI355X disaggregation nightly (#41025)
  _Files: `scripts/ci/slurm/launch_mi355x.sh`, `scripts/ci/slurm/recipes/mi355x-fp8/dsv4pro/1k1k/2p1d-ep16.yaml`, `scripts/ci/slurm/recipes/mi355x-fp8/kimik26/1k1k/1p1d-mtp.yaml`_
- **2026-09-30** [`eb9c9ee99d`](https://github.com/sgl-project/sglang/commit/eb9c9ee99d) [#39614](https://github.com/sgl-project/sglang/pull/39614)
  [Qwen4-Exp] Optional fp8 (e4m3) storage for the compressed QSA indexer cache (#39614)
  _Files: `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/ops/attention/qsa_indexer.py`, `python/sglang/srt/arg_groups/fields/model.py`, `python/sglang/srt/arg_groups/model_overrides/qwen4_exp.py` _+9 more__
- **2026-09-29** [`4885b563c3`](https://github.com/sgl-project/sglang/commit/4885b563c3) [#41681](https://github.com/sgl-project/sglang/pull/41681)
  [Test] Demote PD test RDMA openability check to a warning (#41681)
  _Files: `python/sglang/test/server_fixtures/disaggregation_fixture.py`_
- **2026-09-29** [`77a81996ce`](https://github.com/sgl-project/sglang/commit/77a81996ce) [#39711](https://github.com/sgl-project/sglang/pull/39711)
  [PD] Preserve bootstrap metadata in native Messages requests (#39711)
  _Files: `python/sglang/srt/entrypoints/anthropic/protocol.py`, `python/sglang/srt/entrypoints/anthropic/serving.py`, `test/registered/unit/entrypoints/anthropic/test_serving.py`_
- **2026-09-29** [`5781206833`](https://github.com/sgl-project/sglang/commit/5781206833) [#41618](https://github.com/sgl-project/sglang/pull/41618)
  [PD] Give FakeKVReceiver ensure_abort_notified (#41618)
  _Files: `python/sglang/srt/disaggregation/fake/conn.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-09-29** [`d9074f7943`](https://github.com/sgl-project/sglang/commit/d9074f7943) [#41600](https://github.com/sgl-project/sglang/pull/41600)
  [Test] Fail fast when PD test RDMA devices are not openable by ibverbs (#41600)
  _Files: `python/sglang/test/server_fixtures/disaggregation_fixture.py`_
- **2026-09-29** [`77091cea68`](https://github.com/sgl-project/sglang/commit/77091cea68) [#39627](https://github.com/sgl-project/sglang/pull/39627)
  [Radix Cache] Sync Rust TreeCore and make it the default (#39627)
  _Files: `docs/docs/advanced_features/radix_eviction_policy.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/components/__init__.py` _+38 more__
- **2026-09-29** [`7889fbab9a`](https://github.com/sgl-project/sglang/commit/7889fbab9a) [#32196](https://github.com/sgl-project/sglang/pull/32196)
  [PD] Keep EAGLE DP graph and token metadata consistent (#32196)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/managers/schedule_batch.py` _+17 more__
- **2026-09-28** [`6fa3fe69e2`](https://github.com/sgl-project/sglang/commit/6fa3fe69e2) [#41235](https://github.com/sgl-project/sglang/pull/41235)
  [PD] Keep the sampling mask of a replayed rebootstrap token (#41235)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-09-28** [`2a1c477648`](https://github.com/sgl-project/sglang/commit/2a1c477648) [#41404](https://github.com/sgl-project/sglang/pull/41404)
  [PD] Defer decode KV release on every transfer failure, not only decode-initiated aborts (#41404)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_deferred_decode_kv_release.py` _+1 more__
- **2026-09-28** [`e75e3b8a98`](https://github.com/sgl-project/sglang/commit/e75e3b8a98) [#30899](https://github.com/sgl-project/sglang/pull/30899)
  [Bugfix] fix(hicache): wait for decode offload before retraction (#30899)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_
- **2026-09-28** [`55cc90b533`](https://github.com/sgl-project/sglang/commit/55cc90b533) [#41378](https://github.com/sgl-project/sglang/pull/41378)
  [CI] Real-model Kimi-Linear PD parity at page, DCP virtual-page, chunk and cached-prefix boundaries (#41378)
  _Files: `python/sglang/test/kits/pd_parity_kit.py`, `test/registered/disaggregation/test_disaggregation_kimi_linear.py`_

## KV Cache / Memory  (33 commits)

- **2026-10-05** [`503b898540`](https://github.com/sgl-project/sglang/commit/503b898540) [#42539](https://github.com/sgl-project/sglang/pull/42539)
  [Session] Count streaming session KV by owner in pool accounting (#42539)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/managers/scheduler_components/pool_stats_observer.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` _+7 more__
- **2026-10-04** [`bab04cd791`](https://github.com/sgl-project/sglang/commit/bab04cd791) [#42072](https://github.com/sgl-project/sglang/pull/42072)
  fix(unified-memory): propagate unified-memory lazy checkpoint policy and handle unallocated session slots (#42072)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/unified_memory_pool.py`, `python/sglang/srt/session/streaming_session.py`, `python/sglang/test/unified_allocator_fixtures.py` _+1 more__
- **2026-10-04** [`137c084000`](https://github.com/sgl-project/sglang/commit/137c084000) [#41453](https://github.com/sgl-project/sglang/pull/41453)
  [HiCache] refactor: retire in-flight storage prefetches through one helper (#41453)
  _Files: `python/sglang/srt/mem_cache/unified_cache/storage_attachment.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-10-04** [`6cec8f98ce`](https://github.com/sgl-project/sglang/commit/6cec8f98ce) [#39982](https://github.com/sgl-project/sglang/pull/39982)
  [Bugfix] Fix unified-memory compaction gates and pending page reuse (#39982)
  _Files: `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py`, `python/sglang/test/unified_allocator_fixtures.py`, `test/registered/unit/mem_cache/test_unified_dynamic_gate_capacity.py`, `test/registered/unit/mem_cache/test_unified_float_move_gate.py` _+2 more__
- **2026-10-04** [`048b2a07f3`](https://github.com/sgl-project/sglang/commit/048b2a07f3) [#42330](https://github.com/sgl-project/sglang/pull/42330)
  [Session] Release aborted streaming turns through the normal release path (#42330)
  _Files: `python/sglang/srt/session/streaming_session.py`, `test/registered/unit/mem_cache/test_streaming_session_unit.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-10-04** [`4611ea365e`](https://github.com/sgl-project/sglang/commit/4611ea365e) [#38480](https://github.com/sgl-project/sglang/pull/38480)
  [HiCache]: Fix host lock ownership across radix splits (#38480)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/README.md`, `python/sglang/srt/mem_cache/unified_cache/components/base.py`, `python/sglang/srt/mem_cache/unified_cache/components/full.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa.py` _+16 more__
- **2026-10-04** [`5606fb8592`](https://github.com/sgl-project/sglang/commit/5606fb8592) [#39862](https://github.com/sgl-project/sglang/pull/39862)
  [Fix] HiCache: carry registered Mamba slot side states (Qwen4-Exp PLE) through the host tier (#39862)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/pool_host/mamba.py`, `test/registered/unit/mem_cache/test_hicache_mamba_slot_side_states.py`_
- **2026-10-03** [`4ab720e655`](https://github.com/sgl-project/sglang/commit/4ab720e655) [#42420](https://github.com/sgl-project/sglang/pull/42420)
  [HiCache] Fix cgroup page-cache accounting and the sizing fallback when cgroup discovery fails (#42420)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/hicache_auto_size.py`, `python/sglang/srt/mem_cache/host_memory.py`, `python/sglang/srt/mem_cache/pool_host/base.py` _+1 more__
- **2026-10-03** [`07064fd4a4`](https://github.com/sgl-project/sglang/commit/07064fd4a4) [#42276](https://github.com/sgl-project/sglang/pull/42276)
  [sgl-router] Credit routed prompts before their KV events arrive (#42276)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs` _+13 more__
- **2026-10-03** [`3e9a120add`](https://github.com/sgl-project/sglang/commit/3e9a120add) [#42425](https://github.com/sgl-project/sglang/pull/42425)
  [Fix] Make Hf3fsMockClient reads and writes thread-safe with pread/pwrite (#42425)
  _Files: `python/sglang/srt/mem_cache/storage/hf3fs/hf3fs_client.py`_
- **2026-10-03** [`b016ca406f`](https://github.com/sgl-project/sglang/commit/b016ca406f) [#41961](https://github.com/sgl-project/sglang/pull/41961)
  Support post-capture KV sizing for the unified hybrid-SWA pool (#41961)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py`, `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py` _+5 more__
- **2026-10-03** [`2bae12b9b3`](https://github.com/sgl-project/sglang/commit/2bae12b9b3) [#42264](https://github.com/sgl-project/sglang/pull/42264)
  [HiCache] Fix write-back SWA insert backups tripping the write-through pending-ack assert (#42264)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `rust/sglang-radix-tree/src/tests/unified_tree_core.rs`, `rust/sglang-radix-tree/src/unified_tree_core.rs`, `test/registered/unit/mem_cache/test_rust_tree_core_integration.py` _+1 more__
- **2026-10-03** [`122b59152c`](https://github.com/sgl-project/sglang/commit/122b59152c) [#42362](https://github.com/sgl-project/sglang/pull/42362)
  [mem_cache] Replace `is_chunk_cache` / `is_tree_cache` with `supports_prefix_sharing` (#42362)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_allocator.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+16 more__
- **2026-10-03** [`00bcc25f6c`](https://github.com/sgl-project/sglang/commit/00bcc25f6c) [#42215](https://github.com/sgl-project/sglang/pull/42215)
  [HiCache] Fix DeepSeek-V4 storage backend crash from missing storage_format_tag (#42215)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `test/registered/unit/mem_cache/test_hicache_storage_format_tag.py`_
- **2026-10-03** [`a8b54f138e`](https://github.com/sgl-project/sglang/commit/a8b54f138e) [#42295](https://github.com/sgl-project/sglang/pull/42295)
  [Session] Run streaming sessions only on `UnifiedRadixCache`; reject unverified tree caches (#42295)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/registry.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+5 more__
- **2026-10-02** [`fa7784d140`](https://github.com/sgl-project/sglang/commit/fa7784d140) [#42252](https://github.com/sgl-project/sglang/pull/42252)
  [unified-memory] Copy page envelopes in place during compaction (#42252)
  _Files: `python/sglang/kernels/ops/kvcache/copy_pages.py`, `python/sglang/srt/mem_cache/unified_memory_pool.py`_
- **2026-10-02** [`a64725d407`](https://github.com/sgl-project/sglang/commit/a64725d407) [#42120](https://github.com/sgl-project/sglang/pull/42120)
  [HiCache] Fall back to host memory when no cgroup fs is mounted (#42120)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/host_memory.py`, `test/registered/unit/mem_cache/test_host_memory.py`_
- **2026-10-02** [`1330e437e1`](https://github.com/sgl-project/sglang/commit/1330e437e1) [#42147](https://github.com/sgl-project/sglang/pull/42147)
  [sgl-router] Add native /generate endpoint (#42147)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/policies/selection.rs`, `experimental/sgl-router/src/proxy/sse.rs`, `experimental/sgl-router/src/server/app.rs` _+17 more__
- **2026-10-02** [`895525f062`](https://github.com/sgl-project/sglang/commit/895525f062) [#36266](https://github.com/sgl-project/sglang/pull/36266)
  [Mamba] Warm cache COW kernel before serving (#36266)
  _Files: `python/sglang/srt/mem_cache/mamba_slot_fused.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/layers/mamba/test_mamba_slot_fused.py`_
- **2026-10-01** [`bf2d686a82`](https://github.com/sgl-project/sglang/commit/bf2d686a82) [#39130](https://github.com/sgl-project/sglang/pull/39130)
  Add triton autotune on the Mamba2 SSD kernels (#39130)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/kernels/ops/mamba/triton_ops/autotune.py`, `python/sglang/kernels/ops/mamba/triton_ops/ssd_bmm.py`, `python/sglang/kernels/ops/mamba/triton_ops/ssd_chunk_scan.py` _+2 more__
- **2026-10-01** [`41cbe65de0`](https://github.com/sgl-project/sglang/commit/41cbe65de0) [#41613](https://github.com/sgl-project/sglang/pull/41613)
  [sgl-router] Enforce compatible PD version groups (#41613)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/benches/policy_select.rs`, `experimental/sgl-router/src/buckets_reorg.rs`, `experimental/sgl-router/src/config/cli.rs` _+58 more__
- **2026-10-01** [`11500701f1`](https://github.com/sgl-project/sglang/commit/11500701f1) [#41163](https://github.com/sgl-project/sglang/pull/41163)
  [DSV4] Reserve the FULL logical page in the c4 indexer pool like its KV pool (#41163)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_memory_pool.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `test/registered/unit/mem_cache/test_dsv4_compressed_pools.py`_
- **2026-10-01** [`f02828ea39`](https://github.com/sgl-project/sglang/commit/f02828ea39) [#40471](https://github.com/sgl-project/sglang/pull/40471)
  fix(dsv4): ship the fp8 unified_kv rope pool through the direct external linker (#40471)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `test/registered/unit/mem_cache/test_linker_pool_assembler.py`_
- **2026-10-01** [`bb62f125aa`](https://github.com/sgl-project/sglang/commit/bb62f125aa) [#41346](https://github.com/sgl-project/sglang/pull/41346)
  [HiSparse] fix: return HiSparse slots on PD decode waiting abort and DeepSeek V4 free (#41346)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/allocator/hisparse.py`, `test/registered/unit/mem_cache/test_hisparse_allocator.py`_
- **2026-10-01** [`c9d6c966d0`](https://github.com/sgl-project/sglang/commit/c9d6c966d0) [#41347](https://github.com/sgl-project/sglang/pull/41347)
  [HiSparse] fix: reject speculative decoding and mixed chunk at startup (#41347)
  _Files: `python/sglang/srt/arg_groups/hisparse_hook.py`_
- **2026-09-30** [`517cfa218c`](https://github.com/sgl-project/sglang/commit/517cfa218c) [#41952](https://github.com/sgl-project/sglang/pull/41952)
  [Test] Prune redundant scheduler unit tests (#41952)
  _Files: `test/registered/unit/layers/test_dsv4_nonpaged_indexer.py`, `test/registered/unit/managers/test_detokenizer_stop_trim.py`, `test/registered/unit/managers/test_scheduler_decision_batch_params.py`, `test/registered/unit/managers/test_scheduler_flush_cache.py` _+2 more__
- **2026-09-30** [`e27b6e0971`](https://github.com/sgl-project/sglang/commit/e27b6e0971) [#41805](https://github.com/sgl-project/sglang/pull/41805)
  [Fix] Read TensorCast's WORLD placement under its current names (#41805)
  _Files: `python/sglang/srt/mem_cache/storage/tensorcast_store/host_allocator.py`, `python/sglang/srt/mem_cache/storage/tensorcast_store/test_tensorcast_host_allocator.py`, `python/sglang/srt/mem_cache/storage/tensorcast_store/test_tensorcast_store.py`, `test/registered/unit/test_runtime_context.py`_
- **2026-09-30** [`9f9f9e702a`](https://github.com/sgl-project/sglang/commit/9f9f9e702a) [#41758](https://github.com/sgl-project/sglang/pull/41758)
  [HiCache] Attribute buffer-mode storage hits against the joint device match (#41758)
  _Files: `python/sglang/srt/mem_cache/buffer_mode/pipeline.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_storage_prefetch_lifecycle.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-30** [`21ed9fbf44`](https://github.com/sgl-project/sglang/commit/21ed9fbf44) [#41726](https://github.com/sgl-project/sglang/pull/41726)
  [Rust] Extract shared runtime.v1 protobuf bindings (#41726)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.pre-commit-config.yaml`, `docker/Dockerfile`, `docker/Dockerfile.cu134` _+15 more__
- **2026-09-29** [`f0e4001930`](https://github.com/sgl-project/sglang/commit/f0e4001930) [#40979](https://github.com/sgl-project/sglang/pull/40979)
  [Fix] Allocate SWA KV pools inside the memory-saver region (#40979)
  _Files: `python/sglang/srt/mem_cache/index_key_cache.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/mem_cache/swa_memory_pool.py`_
- **2026-09-29** [`2ff52e3ceb`](https://github.com/sgl-project/sglang/commit/2ff52e3ceb) [#33804](https://github.com/sgl-project/sglang/pull/33804)
  [Intel][XPU]Enable chunked prefill scnearios for XPU with UT (#33804)
  _Files: `python/sglang/test/chunked_prefill_test_utils.py`, `python/sglang/test/scripted_runtime/http_server.py`, `python/sglang/test/scripted_runtime_chunked_helpers.py`, `test/manual/chunked_prefill/test_scripted_abort.py` _+6 more__
- **2026-09-29** [`6e1df69623`](https://github.com/sgl-project/sglang/commit/6e1df69623) [#41527](https://github.com/sgl-project/sglang/pull/41527)
  [npu]support NPU 910C L2 memcache offload (#41527)
  _Files: `python/sglang/srt/mem_cache/pool_host/npu_memfabric.py`_
- **2026-09-28** [`89e1316eae`](https://github.com/sgl-project/sglang/commit/89e1316eae) [#41469](https://github.com/sgl-project/sglang/pull/41469)
  [mem cache] refactor: remove the index-K continuous getters orphaned by the CP v1 removal (#41469)
  _Files: `python/sglang/srt/mem_cache/index_key_cache.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/mem_cache/swa_memory_pool.py`_

## Other  (29 commits)

- **2026-10-05** [`ab4f8a44f4`](https://github.com/sgl-project/sglang/commit/ab4f8a44f4) [#42572](https://github.com/sgl-project/sglang/pull/42572)
  [sgl-router] Point the design doc at the shared engine ranking (#42572)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`_
- **2026-10-04** [`d475b5a25c`](https://github.com/sgl-project/sglang/commit/d475b5a25c) [#38828](https://github.com/sgl-project/sglang/pull/38828)
  [weight_cache] Coordinate daemon readiness across ranks (#38828)
  _Files: `python/sglang/srt/weight_cache/daemon.py`_
- **2026-10-02** [`d954c88a4f`](https://github.com/sgl-project/sglang/commit/d954c88a4f) [#42179](https://github.com/sgl-project/sglang/pull/42179)
  [Fix] Update stale source-patch match in dumper comparator e2e test (#42179)
  _Files: `test/registered/debug_utils/test_engine_dumper_comparator_e2e.py`_
- **2026-10-01** [`dcf4e18283`](https://github.com/sgl-project/sglang/commit/dcf4e18283) [#40648](https://github.com/sgl-project/sglang/pull/40648)
  fix(nccl): disable graph buffer registration for pausable graph pools (#40648)
  _Files: `python/sglang/srt/arg_groups/parallel_hook.py`_
- **2026-10-01** [`315080a0de`](https://github.com/sgl-project/sglang/commit/315080a0de) [#41610](https://github.com/sgl-project/sglang/pull/41610)
  [sgl-router] Exclude portless prefills and retry bootstrap discovery (#41610)
  _Files: `experimental/sgl-router/src/health/circuit_breaker.rs`, `experimental/sgl-router/src/policies/registry.rs`, `experimental/sgl-router/src/server/routes/health.rs`, `experimental/sgl-router/src/workers/manager.rs` _+5 more__
- **2026-10-01** [`c78fa09290`](https://github.com/sgl-project/sglang/commit/c78fa09290) [#42010](https://github.com/sgl-project/sglang/pull/42010)
  [Router] Drop the snapshot client's redirect-following fallback (#42010)
  _Files: `experimental/sgl-router/src/state/kv_events/index.rs`_
- **2026-10-01** [`dc7defd294`](https://github.com/sgl-project/sglang/commit/dc7defd294) [#38991](https://github.com/sgl-project/sglang/pull/38991)
  [Kimi-K3][DCP][DSpark] fix eager mode nonetype crash due to no extend_prefix_lens (#38991)
  _Files: `python/sglang/srt/model_executor/runner/eager_runner.py`_
- **2026-10-01** [`86807b87dd`](https://github.com/sgl-project/sglang/commit/86807b87dd) [#41915](https://github.com/sgl-project/sglang/pull/41915)
  [XPU] Fix test_qsa_indexer_xpu after defer_expansion change (#41915)
  _Files: `test/registered/xpu/test_qsa_indexer_xpu.py`_
- **2026-10-01** [`3b6d37a56e`](https://github.com/sgl-project/sglang/commit/3b6d37a56e) [#40699](https://github.com/sgl-project/sglang/pull/40699)
  [Router] Gate readiness on peer bootstrap, and make it observable (13/13) (#40699)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/main.rs`, `experimental/sgl-router/src/server/app_context.rs` _+5 more__
- **2026-10-01** [`a702970ecb`](https://github.com/sgl-project/sglang/commit/a702970ecb) [#41886](https://github.com/sgl-project/sglang/pull/41886)
  [Perf] Use FA4 by default for MiMo on SM100 (#41886)
  _Files: `python/sglang/srt/arg_groups/model_overrides/mimo_v2.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-09-30** [`4b3f63ec70`](https://github.com/sgl-project/sglang/commit/4b3f63ec70) [#40697](https://github.com/sgl-project/sglang/pull/40697)
  [Router] Prove a bootstrapped replica answers like the one it copied (11/13) (#40697)
  _Files: `experimental/sgl-router/tests/component/policies/kv_events_peer_bootstrap.rs`, `experimental/sgl-router/tests/component/policies/mod.rs`_
- **2026-09-30** [`4c930125c7`](https://github.com/sgl-project/sglang/commit/4c930125c7) [#40696](https://github.com/sgl-project/sglang/pull/40696)
  [Router] Ask the fleet when a graft's splice goes unwitnessed (10/13) (#40696)
  _Files: `experimental/sgl-router/src/state/kv_events/index.rs`, `experimental/sgl-router/src/state/kv_events/index/fallback.rs`, `experimental/sgl-router/src/state/kv_events/index/graft.rs`, `experimental/sgl-router/src/state/kv_events/index/probe.rs` _+1 more__
- **2026-09-30** [`53225fadf4`](https://github.com/sgl-project/sglang/commit/53225fadf4) [#41838](https://github.com/sgl-project/sglang/pull/41838)
  [Fix] Stop the namespace census at the leaf a read names (#41838)
  _Files: `test/registered/unit/test_server_args_namespaces.py`_
- **2026-09-30** [`f8500474c9`](https://github.com/sgl-project/sglang/commit/f8500474c9) [#40695](https://github.com/sgl-project/sglang/pull/40695)
  [Router] Share one fleet-wide fetch across a discovery burst (9/13) (#40695)
  _Files: `experimental/sgl-router/src/state/kv_events/bootstrap/vet.rs`, `experimental/sgl-router/src/state/kv_events/index.rs`, `experimental/sgl-router/src/state/kv_events/index/coordinator.rs`, `experimental/sgl-router/src/state/kv_events/index/fallback.rs` _+3 more__
- **2026-09-30** [`4d4d3f2e5c`](https://github.com/sgl-project/sglang/commit/4d4d3f2e5c) [#40694](https://github.com/sgl-project/sglang/pull/40694)
  [Router] Sweep the fleet for a peer snapshot and hand it to the pump (8/13) (#40694)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/main.rs` _+8 more__
- **2026-09-30** [`7fb85a9d88`](https://github.com/sgl-project/sglang/commit/7fb85a9d88) [#41314](https://github.com/sgl-project/sglang/pull/41314)
  [MLX] Fix startup after logical token capacity change (#41314)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `test/registered/unit/hardware_backend/mlx/test_mlx_runner_pool_contract.py`_
- **2026-09-30** [`01b5f572b7`](https://github.com/sgl-project/sglang/commit/01b5f572b7) [#41750](https://github.com/sgl-project/sglang/pull/41750)
  [Refactor] Rename layer boundary protocols, contracts and helpers (#41750)
- **2026-09-29** [`8d2d874758`](https://github.com/sgl-project/sglang/commit/8d2d874758) [#41749](https://github.com/sgl-project/sglang/pull/41749)
  [Fix] Release consumed residual contributions (#41749)
  _Files: `python/sglang/srt/layers/layer_boundary/residual/stream.py`, `test/registered/unit/layer_boundary/test_residual_stream.py`_
- **2026-09-29** [`9a16e47437`](https://github.com/sgl-project/sglang/commit/9a16e47437) [#41728](https://github.com/sgl-project/sglang/pull/41728)
  chore: grant jain-ria CI permissions (#41728)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-09-29** [`4a4e1ce014`](https://github.com/sgl-project/sglang/commit/4a4e1ce014) [#40693](https://github.com/sgl-project/sglang/pull/40693)
  [Router] Hold a booting rank's batches and graft a snapshot on the pump (7/13) (#40693)
  _Files: `experimental/sgl-router/src/state/kv_events/bootstrap.rs`, `experimental/sgl-router/src/state/kv_events/bootstrap/tracker.rs`, `experimental/sgl-router/src/state/kv_events/index.rs`, `experimental/sgl-router/src/state/kv_events/index/fallback.rs` _+5 more__
- **2026-09-29** [`8d1643b21e`](https://github.com/sgl-project/sglang/commit/8d1643b21e) [#40692](https://github.com/sgl-project/sglang/pull/40692)
  [Router] Vet a peer's snapshot before it may touch the tree (6/13) (#40692)
  _Files: `experimental/sgl-router/src/state/kv_events/bootstrap.rs`, `experimental/sgl-router/src/state/kv_events/bootstrap/vet.rs`, `experimental/sgl-router/src/state/kv_events/mod.rs`, `experimental/sgl-router/src/state/kv_events/tree.rs` _+1 more__
- **2026-09-29** [`8b3a4cad8b`](https://github.com/sgl-project/sglang/commit/8b3a4cad8b) [#40691](https://github.com/sgl-project/sglang/pull/40691)
  [Router] Track a booting rank's bootstrap and fetch a peer's snapshot (5/13) (#40691)
  _Files: `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/src/state/kv_events/bootstrap.rs`, `experimental/sgl-router/src/state/kv_events/bootstrap/fetch.rs`, `experimental/sgl-router/src/state/kv_events/bootstrap/peers.rs` _+2 more__
- **2026-09-29** [`f731e82f09`](https://github.com/sgl-project/sglang/commit/f731e82f09) [#41065](https://github.com/sgl-project/sglang/pull/41065)
  Fix MUSA detection under torch.compile fullgraph (#41065)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-09-29** [`34a1234d21`](https://github.com/sgl-project/sglang/commit/34a1234d21) [#40515](https://github.com/sgl-project/sglang/pull/40515)
  chore: expose agent skills via `.agents` directories (#40515)
- **2026-09-29** [`de9f850b36`](https://github.com/sgl-project/sglang/commit/de9f850b36) [#41555](https://github.com/sgl-project/sglang/pull/41555)
  [Refactor] Rename the module to layer_boundary (#41555)
- **2026-09-29** [`701213c867`](https://github.com/sgl-project/sglang/commit/701213c867) [#41554](https://github.com/sgl-project/sglang/pull/41554)
  [Refactor] Retire the layer facade and simplify boundary internals (#41554)
- **2026-09-28** [`f124c5ceec`](https://github.com/sgl-project/sglang/commit/f124c5ceec) [#41588](https://github.com/sgl-project/sglang/pull/41588)
  [Model Loader] Stop checkpoint prefetch after iterator completion (#41588)
  _Files: `python/sglang/srt/model_loader/weight_utils.py`_
- **2026-09-28** [`2f88c65289`](https://github.com/sgl-project/sglang/commit/2f88c65289) [#40688](https://github.com/sgl-project/sglang/pull/40688)
  [Router] Serve the cache-aware tree at /internal/kv_snapshot (2/13) (#40688)
  _Files: `experimental/sgl-router/Cargo.lock`, `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/src/main.rs`, `experimental/sgl-router/src/server/app.rs` _+8 more__
- **2026-09-28** [`df378bca42`](https://github.com/sgl-project/sglang/commit/df378bca42) [#40687](https://github.com/sgl-project/sglang/pull/40687)
  [Router] Give the cache-aware tree a snapshot surface (1/13) (#40687)
  _Files: `experimental/sgl-router/src/state/kv_events/tree.rs`, `experimental/sgl-router/src/state/kv_events/tree/snapshot.rs`_

## ROCm / AMD  (16 commits)

- **2026-10-05** [`b3f967e809`](https://github.com/sgl-project/sglang/commit/b3f967e809) [#41282](https://github.com/sgl-project/sglang/pull/41282)
  Revert "Revert "[AMD][ROCm] Keep cos_sin_cache fp32 on HIP for fused QSA indexer kernel (#41282)"" (#42558)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/layers/rotary_embedding/mrope.py`_
- **2026-10-05** [`456d533e61`](https://github.com/sgl-project/sglang/commit/456d533e61) [#41282](https://github.com/sgl-project/sglang/pull/41282)
  Revert "[AMD][ROCm] Keep cos_sin_cache fp32 on HIP for fused QSA indexer kernel (#41282)" (#42541)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/layers/rotary_embedding/mrope.py`_
- **2026-10-04** [`0343bc1483`](https://github.com/sgl-project/sglang/commit/0343bc1483) [#42512](https://github.com/sgl-project/sglang/pull/42512)
  [AMD][Docs] fix mori io and umbp playground (#42512)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-10-04** [`ab9d8f029c`](https://github.com/sgl-project/sglang/commit/ab9d8f029c) [#41405](https://github.com/sgl-project/sglang/pull/41405)
  [AMD][DI][CI] mi355x spur: skip RDMA ports that are not PORT_ACTIVE; dump driver log on failure (#41405)
  _Files: `scripts/ci/slurm/launch_mi355x.sh`_
- **2026-10-04** [`ff219e159e`](https://github.com/sgl-project/sglang/commit/ff219e159e) [#35357](https://github.com/sgl-project/sglang/pull/35357)
  [AMD] MiniMax-M3: fuse sparse QK norm, RoPE and cache writes with AITER (#35357)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/minimax_m3.py`_
- **2026-10-03** [`061e712bab`](https://github.com/sgl-project/sglang/commit/061e712bab) [#42427](https://github.com/sgl-project/sglang/pull/42427)
  chore: bump sgl-kernel version to 0.4.9 (#42427)
  _Files: `python/sglang/kernels/aot/pyproject.toml`, `python/sglang/kernels/aot/pyproject_cpu.toml`, `python/sglang/kernels/aot/pyproject_musa.toml`, `python/sglang/kernels/aot/pyproject_rocm.toml` _+1 more__
- **2026-10-02** [`f6fcda8827`](https://github.com/sgl-project/sglang/commit/f6fcda8827) [#41282](https://github.com/sgl-project/sglang/pull/41282)
  [AMD][ROCm] Keep cos_sin_cache fp32 on HIP for fused QSA indexer kernel (#41282)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/layers/rotary_embedding/mrope.py`_
- **2026-10-02** [`2cd92d10b9`](https://github.com/sgl-project/sglang/commit/2cd92d10b9) [#42219](https://github.com/sgl-project/sglang/pull/42219)
  [AMD] Skip the AITER #6042/#5967 patches on gfx1250 (#42219)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-02** [`d61a9c28ba`](https://github.com/sgl-project/sglang/commit/d61a9c28ba) [#42013](https://github.com/sgl-project/sglang/pull/42013)
  chore: bump docs install version to 0.5.21 (#42013)
  _Files: `docs/docs/get-started/install.mdx`, `docs/docs/hardware-platforms/amd_gpu.mdx`_
- **2026-10-01** [`ffb134188b`](https://github.com/sgl-project/sglang/commit/ffb134188b) [#42023](https://github.com/sgl-project/sglang/pull/42023)
  [AMD] Update aiter version for v41 (#42023)
  _Files: `docker/rocm.Dockerfile`_
- **2026-09-30** [`682f4ef32f`](https://github.com/sgl-project/sglang/commit/682f4ef32f) [#41687](https://github.com/sgl-project/sglang/pull/41687)
  [ROCm] Select DSA indexer top-k wave size by arch (wave32 on gfx1250) (#41687)
  _Files: `python/sglang/kernels/aot/include/hip/dsa_topk_coop.cuh`_
- **2026-09-30** [`4207f1ae23`](https://github.com/sgl-project/sglang/commit/4207f1ae23) [#41099](https://github.com/sgl-project/sglang/pull/41099)
  [AMD][DI][CI] Record the commit the MI355X nightly tested (#41099)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-09-30** [`cae69be584`](https://github.com/sgl-project/sglang/commit/cae69be584) [#41784](https://github.com/sgl-project/sglang/pull/41784)
  chore: bump sgl-kernel version to 0.4.8 (#41784)
  _Files: `python/sglang/kernels/aot/pyproject.toml`, `python/sglang/kernels/aot/pyproject_cpu.toml`, `python/sglang/kernels/aot/pyproject_musa.toml`, `python/sglang/kernels/aot/pyproject_rocm.toml` _+1 more__
- **2026-09-29** [`5828cd4927`](https://github.com/sgl-project/sglang/commit/5828cd4927) [#41602](https://github.com/sgl-project/sglang/pull/41602)
  [AMD] Add GLM-5.3 MI30x and MI35x nightly accuracy tests (#41602)
  _Files: `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi30x/test_glm53_eval_mi30x.py`, `test/registered/amd/accuracy/mi35x/test_glm53_eval_mi35x.py`, `test/run_suite.py`_
- **2026-09-28** [`9654e5c4bc`](https://github.com/sgl-project/sglang/commit/9654e5c4bc) [#41021](https://github.com/sgl-project/sglang/pull/41021)
  dsv4.1-amd: fused mHC boundary and all-reduce + mHC post kernels (#41021)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mhc_boundary_gfx95.cuh`, `python/sglang/kernels/jit/csrc/distributed/all_reduce_mhc_hip.cuh`, `python/sglang/kernels/ops/communication/all_reduce_mhc_hip.py`, `python/sglang/kernels/ops/layernorm/mhc.py` _+3 more__
- **2026-09-28** [`34f090053e`](https://github.com/sgl-project/sglang/commit/34f090053e) [#41387](https://github.com/sgl-project/sglang/pull/41387)
  [AMD] [Docker] Remove unused LLVM 18 setup from ROCm TileLang build (#41387)
  _Files: `docker/rocm.Dockerfile`_

## Tensor / Data Parallel  (15 commits)

- **2026-10-05** [`08fa37e48d`](https://github.com/sgl-project/sglang/commit/08fa37e48d) [#42429](https://github.com/sgl-project/sglang/pull/42429)
  [sgl-router] Add reorg bucket config with per-group admission (#42429)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/buckets_reorg.rs`, `experimental/sgl-router/src/config/cli.rs` _+36 more__
- **2026-10-05** [`a96b146491`](https://github.com/sgl-project/sglang/commit/a96b146491) [#42428](https://github.com/sgl-project/sglang/pull/42428)
  [sgl-router] Move pressure and prefix signals out of legacy policies (#42428)
  _Files: `experimental/sgl-router/src/main.rs`, `experimental/sgl-router/src/policies/admission.rs`, `experimental/sgl-router/src/policies/cache_aware.rs`, `experimental/sgl-router/src/policies/decode.rs` _+19 more__
- **2026-10-03** [`71b04e02cf`](https://github.com/sgl-project/sglang/commit/71b04e02cf) [#42311](https://github.com/sgl-project/sglang/pull/42311)
  [Refactor] Build the ZAYA1, IQuest-Q1 and Gemma 4 decoders from stage boundaries (#42311)
  _Files: `python/sglang/srt/layers/layer_boundary/factories.py`, `python/sglang/srt/layers/layer_boundary/residual/add_norm.py`, `python/sglang/srt/layers/layer_boundary/residual/batch.py`, `python/sglang/srt/layers/layer_boundary/stage.py` _+6 more__
- **2026-10-02** [`19794f5743`](https://github.com/sgl-project/sglang/commit/19794f5743) [#42258](https://github.com/sgl-project/sglang/pull/42258)
  [sgl-router] Add SGLang's /v1/classify (#42258)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/server/app.rs`, `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/src/server/routes/chat/preparation.rs` _+4 more__
- **2026-10-02** [`ebf161cea4`](https://github.com/sgl-project/sglang/commit/ebf161cea4) [#42205](https://github.com/sgl-project/sglang/pull/42205)
  [sgl-router] Add SGLang's /v1/rerank (#42205)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/server/app.rs`, `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/src/server/routes/chat/preparation.rs` _+5 more__
- **2026-10-01** [`d7565215ec`](https://github.com/sgl-project/sglang/commit/d7565215ec) [#41974](https://github.com/sgl-project/sglang/pull/41974)
  [sgl-router] Route to a specific DP rank inside multi-rank workers (--dp-aware) (#41974)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs` _+36 more__
- **2026-10-01** [`3f4bfda13c`](https://github.com/sgl-project/sglang/commit/3f4bfda13c) [#31801](https://github.com/sgl-project/sglang/pull/31801)
  [Bugfix] Fix DeepSeek V4 Pro TP24 vocabulary-padding failure on Hopper (#31801)
  _Files: `python/sglang/srt/layers/vocab_parallel_embedding.py`, `test/registered/unit/dllm/test_gemma4_cuda_graph.py`_
- **2026-10-01** [`fb92ba1127`](https://github.com/sgl-project/sglang/commit/fb92ba1127) [#41964](https://github.com/sgl-project/sglang/pull/41964)
  [Rust] Wire the gRPC server into the frontend lifecycle (#41964)
  _Files: `python/sglang/srt/arg_groups/serving_hook.py`, `python/sglang/srt/rust_server/config.py`, `rust/Cargo.lock`, `rust/sglang-server/Cargo.toml` _+8 more__
- **2026-09-30** [`8e4bcc5ca9`](https://github.com/sgl-project/sglang/commit/8e4bcc5ca9) [#41896](https://github.com/sgl-project/sglang/pull/41896)
  [rust-renderer] `sglang-processor` lib (#41896)
  _Files: `.github/CODEOWNERS`, `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/release-docker-renderer.yml`, `docker/renderer.Dockerfile` _+29 more__
- **2026-09-30** [`4f3ee94d25`](https://github.com/sgl-project/sglang/commit/4f3ee94d25) [#41810](https://github.com/sgl-project/sglang/pull/41810)
  [Fix] Make the Solar model constructible and runnable (#41810)
  _Files: `python/sglang/srt/models/solar.py`, `test/registered/unit/models/test_solar_pipeline_split.py`_
- **2026-09-30** [`3b537e96e2`](https://github.com/sgl-project/sglang/commit/3b537e96e2) [#41135](https://github.com/sgl-project/sglang/pull/41135)
  [AMD][DI][CI] Leave the GLM-5.2 MTP decode room to load its Triton kernels (#41135)
  _Files: `scripts/ci/slurm/recipes/mi355x-fp4/glm52/1k1k/1p1d-mtp.yaml`_
- **2026-09-30** [`25de118ae3`](https://github.com/sgl-project/sglang/commit/25de118ae3) [#41238](https://github.com/sgl-project/sglang/pull/41238)
  [AMD][DI][CI] Give the dsv4pro-fp4 MTP decode more memory headroom (#41238)
  _Files: `scripts/ci/slurm/recipes/mi355x-fp4/dsv4pro/1k1k/1p1d-mtp.yaml`_
- **2026-09-29** [`ced5e9fe49`](https://github.com/sgl-project/sglang/commit/ced5e9fe49) [#35330](https://github.com/sgl-project/sglang/pull/35330)
  [Kimi] Enable GB300 TP4 and GB200/GB300 TP16 SP collectives (#35330)
  _Files: `python/sglang/kernels/ops/communication/configs/sp_collective/world=16,H=7168,device_name=NVIDIA_GB200.json`, `python/sglang/kernels/ops/communication/configs/sp_collective/world=16,H=7168,device_name=NVIDIA_GB300.json`, `python/sglang/kernels/ops/communication/sp_collective.py`, `python/sglang/srt/distributed/parallel_state.py` _+4 more__
- **2026-09-29** [`7bcfcf5aa0`](https://github.com/sgl-project/sglang/commit/7bcfcf5aa0) [#40690](https://github.com/sgl-project/sglang/pull/40690)
  [Router] Watch EndpointSlices for sibling router replicas (4/13) (#40690)
  _Files: `experimental/sgl-router/src/discovery/k8s.rs`, `experimental/sgl-router/src/discovery/k8s/peers.rs`, `experimental/sgl-router/src/main.rs`_
- **2026-09-28** [`6624999385`](https://github.com/sgl-project/sglang/commit/6624999385) [#40446](https://github.com/sgl-project/sglang/pull/40446)
  [Fix][NPU] fix dp-attn hang when pin_mem is True on NPU (#40446)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py`, `python/sglang/srt/platforms/npu.py`, `test/registered/unit/platforms/test_platform_interface.py`_

## CI / Build  (15 commits)

- **2026-10-05** [`1818db4e54`](https://github.com/sgl-project/sglang/commit/1818db4e54) [#42543](https://github.com/sgl-project/sglang/pull/42543)
  [CI] Drop the echoed command from /rerun-test result replies (#42543)
  _Files: `.agents/skills/ci-workflow-guide/SKILL.md`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-10-05** [`b1bbd74f28`](https://github.com/sgl-project/sglang/commit/b1bbd74f28) [#41634](https://github.com/sgl-project/sglang/pull/41634)
  [XPU][CI] Disable test_xpu_graph until tc_piecewise is removed (#41634) (#42524)
  _Files: `test/registered/xpu/test_xpu_graph.py`_
- **2026-10-04** [`fea3c088a1`](https://github.com/sgl-project/sglang/commit/fea3c088a1) [#42463](https://github.com/sgl-project/sglang/pull/42463)
  [CI] Temporarily disable GB300 (#42463)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/release-whl-deepgemm.yml`, `.github/workflows/rerun-test.yml` _+1 more__
- **2026-10-04** [`35f3c96ff4`](https://github.com/sgl-project/sglang/commit/35f3c96ff4) [#42487](https://github.com/sgl-project/sglang/pull/42487)
  [CI] Fix bootstrap sender registration test on main (#42487)
- **2026-10-03** [`0072e2cc08`](https://github.com/sgl-project/sglang/commit/0072e2cc08) [#42214](https://github.com/sgl-project/sglang/pull/42214)
  [Fix] Validate per-layer rope_parameters on transformers 5.17 (Laguna-S/XS-2.1 nightly) (#42214)
  _Files: `python/sglang/srt/utils/hf_transformers_patches.py`_
- **2026-10-01** [`d010e50ad6`](https://github.com/sgl-project/sglang/commit/d010e50ad6) [#39788](https://github.com/sgl-project/sglang/pull/39788)
  [PPU][1/N] CI: Add backend registration and runner preflight (#39788)
  _Files: `.github/workflows/pr-test-ppu.yml`, `python/sglang/test/ci/ci_register.py`, `scripts/ci/ppu/check_ppu_environment.py`, `scripts/ci/utils/ci_coverage_report.py` _+3 more__
- **2026-10-01** [`36330b8c08`](https://github.com/sgl-project/sglang/commit/36330b8c08) [#40698](https://github.com/sgl-project/sglang/pull/40698)
  [Router] k8s e2e for cache-aware peer bootstrap (12/13) (#40698)
  _Files: `experimental/sgl-router/tests/e2e/k8s_integration/Dockerfile.fake_kv_worker`, `experimental/sgl-router/tests/e2e/k8s_integration/conftest.py`, `experimental/sgl-router/tests/e2e/k8s_integration/fake_kv_worker.py`, `experimental/sgl-router/tests/e2e/k8s_integration/manifests/kv-bootstrap.yaml` _+2 more__
- **2026-10-01** [`b37e6f79fc`](https://github.com/sgl-project/sglang/commit/b37e6f79fc) [#41935](https://github.com/sgl-project/sglang/pull/41935)
  [ci] grant ci permissions to sagearc (#41935)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-09-30** [`9b7464c8dd`](https://github.com/sgl-project/sglang/commit/9b7464c8dd) [#41856](https://github.com/sgl-project/sglang/pull/41856)
  ci: temporarily disable A5 (950) nightly job during power maintenance (#41856)
  _Files: `.github/workflows/nightly-test-npu.yml`_
- **2026-09-30** [`24ee67d2fa`](https://github.com/sgl-project/sglang/commit/24ee67d2fa) [#41787](https://github.com/sgl-project/sglang/pull/41787)
  Readme refresh (#41787)
  _Files: `README.md`, `docs/docs.json`, `docs/docs/basic_usage/aws_sagemaker.mdx`, `docs/docs/developer_guide/development_guide_using_docker.mdx` _+4 more__
- **2026-09-30** [`8854857a99`](https://github.com/sgl-project/sglang/commit/8854857a99) [#41800](https://github.com/sgl-project/sglang/pull/41800)
  [CI] Bound maintenance API requests to 30 seconds (#41800)
  _Files: `.github/actions/check-maintenance/action.yml`_
- **2026-09-30** [`7b30ff26ee`](https://github.com/sgl-project/sglang/commit/7b30ff26ee) [#41625](https://github.com/sgl-project/sglang/pull/41625)
  [CI] Evaluate the maintenance gate with github-script instead of jq (#41625)
  _Files: `.github/actions/check-maintenance/action.yml`_
- **2026-09-29** [`ba3e04c063`](https://github.com/sgl-project/sglang/commit/ba3e04c063) [#41775](https://github.com/sgl-project/sglang/pull/41775)
  [CI] Grant CI permissions to four contributors (#41775)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-09-29** [`affc602f51`](https://github.com/sgl-project/sglang/commit/affc602f51) [#41720](https://github.com/sgl-project/sglang/pull/41720)
  [CI] Extend DeepGEMM GB300 validation timeout to three hours (#41720)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-09-28** [`0823651b0b`](https://github.com/sgl-project/sglang/commit/0823651b0b) [#41075](https://github.com/sgl-project/sglang/pull/41075)
  [XPU] Disable test_ngram_corpus on XPU and detect XPU tests dynamically in CI filter (#41075)
  _Files: `.github/workflows/pr-test-xpu.yml`, `scripts/ci/xpu/detect_xpu_test_changes.py`_

## Docs / Examples  (14 commits)

- **2026-10-05** [`70f0b7351e`](https://github.com/sgl-project/sglang/commit/70f0b7351e) [#42545](https://github.com/sgl-project/sglang/pull/42545)
  [sgl-router] Improved policy balanced mode (#42545)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/buckets_reorg.rs`, `experimental/sgl-router/src/config/cli.rs` _+10 more__
- **2026-10-04** [`8afef58af4`](https://github.com/sgl-project/sglang/commit/8afef58af4) [#41296](https://github.com/sgl-project/sglang/pull/41296)
  docs: sync LMSYS SGLang blog cards (#41296)
  _Files: `docs/index.mdx`_
- **2026-10-03** [`fd5e68f99e`](https://github.com/sgl-project/sglang/commit/fd5e68f99e) [#42275](https://github.com/sgl-project/sglang/pull/42275)
  [sgl-router] Repair KV-event sequence gaps from the engine's replay socket (#42275)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/src/server/routes/metrics.rs`, `experimental/sgl-router/src/state/kv_events/discovery.rs` _+7 more__
- **2026-10-02** [`8c9030ce3f`](https://github.com/sgl-project/sglang/commit/8c9030ce3f) [#41990](https://github.com/sgl-project/sglang/pull/41990)
  [sgl-router] Unify reorg session and cache affinity modes (#41990)
  _Files: `experimental/sgl-router/POLICY_DESIGN.md`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs` _+7 more__
- **2026-10-02** [`8acd36b56b`](https://github.com/sgl-project/sglang/commit/8acd36b56b) [#42109](https://github.com/sgl-project/sglang/pull/42109)
  [Docs] GLM-5.2 GB300 NVFP4: add env vars from InferenceX AgentX recipe (#42109)
  _Files: `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-10-01** [`a21dcbd320`](https://github.com/sgl-project/sglang/commit/a21dcbd320) [#41996](https://github.com/sgl-project/sglang/pull/41996)
  [sgl-router] Support engines started with --api-key (--worker-api-key) (#41996)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/main.rs` _+3 more__
- **2026-10-01** [`a71c7d19e7`](https://github.com/sgl-project/sglang/commit/a71c7d19e7) [#42049](https://github.com/sgl-project/sglang/pull/42049)
  [Router] Document peer bootstrap: flags, RBAC, downward API, probe implications (#42049)
  _Files: `experimental/sgl-router/README.md`_
- **2026-10-01** [`3b2ad1c6ae`](https://github.com/sgl-project/sglang/commit/3b2ad1c6ae) [#41612](https://github.com/sgl-project/sglang/pull/41612)
  [sgl-router] Fail fast and cancel decode when prefill fails (#41612)
  _Files: `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/src/proxy/mod.rs`, `experimental/sgl-router/src/proxy/sse.rs`, `experimental/sgl-router/src/server/error.rs` _+8 more__
- **2026-10-01** [`46637965ab`](https://github.com/sgl-project/sglang/commit/46637965ab) [#41611](https://github.com/sgl-project/sglang/pull/41611)
  [sgl-router] Allow load-only routing without a tokenizer (#41611)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/buckets_reorg.rs`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs` _+29 more__
- **2026-10-01** [`047be72a8c`](https://github.com/sgl-project/sglang/commit/047be72a8c) [#41999](https://github.com/sgl-project/sglang/pull/41999)
  [Router] Harden peer-bootstrap edges: refuse redirects and metric docs (#41999)
  _Files: `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/src/server/routes/cache.rs`, `experimental/sgl-router/src/state/kv_events/bootstrap/peers.rs`, `experimental/sgl-router/src/state/kv_events/index.rs` _+1 more__
- **2026-09-30** [`d26ec4690d`](https://github.com/sgl-project/sglang/commit/d26ec4690d) [#41851](https://github.com/sgl-project/sglang/pull/41851)
  docs: remove unreliable DeepWiki badge (#41851)
  _Files: `README.md`_
- **2026-09-29** [`f884231f5a`](https://github.com/sgl-project/sglang/commit/f884231f5a) [#41746](https://github.com/sgl-project/sglang/pull/41746)
  [Docs] Add IQuestLab card logo to cookbook landing page (#41746)
  _Files: `docs/cards/logos/iquestlab.png`, `docs/cookbook/autoregressive/intro.mdx`_
- **2026-09-29** [`b95329a74d`](https://github.com/sgl-project/sglang/commit/b95329a74d) [#41118](https://github.com/sgl-project/sglang/pull/41118)
  [Docs] Add GigaChat 3.5 and GigaChat 3.5 Reasoning cookbook pages (#41118)
  _Files: `docs/cards/logos/gigachat.png`, `docs/cookbook/autoregressive/GigaChat/GigaChat3.5-Reasoning.mdx`, `docs/cookbook/autoregressive/GigaChat/GigaChat3.5.mdx`, `docs/cookbook/autoregressive/intro.mdx` _+5 more__
- **2026-09-28** [`6aacca2d91`](https://github.com/sgl-project/sglang/commit/6aacca2d91) [#40689](https://github.com/sgl-project/sglang/pull/40689)
  [Router] Name a replica's siblings with --kv-peer-selector (3/13) (#40689)
  _Files: `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs` _+6 more__

## Quantization  (14 commits)

- **2026-10-04** [`7a719e9a65`](https://github.com/sgl-project/sglang/commit/7a719e9a65) [#42494](https://github.com/sgl-project/sglang/pull/42494)
  [AMD] Fix RoPE cache dtype and diffusion CI failures (#42494)
  _Files: `.github/workflows/pr-test-amd.yml`, `python/sglang/kernels/aot/csrc/elementwise/pos_enc.cu`, `python/sglang/multimodal_gen/runtime/layers/quantization/__init__.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py` _+3 more__
- **2026-10-04** [`fbce0d9478`](https://github.com/sgl-project/sglang/commit/fbce0d9478) [#42121](https://github.com/sgl-project/sglang/pull/42121)
  [diffusion] fix: load serialized h3 INT8 in ComfyUI integrated mode (#42121)
  _Files: `python/sglang/multimodal_gen/runtime/loader/comfyui_checkpoints/spec.py`, `python/sglang/multimodal_gen/test/unit/test_comfyui_h3.py`_
- **2026-10-04** [`295a53c90e`](https://github.com/sgl-project/sglang/commit/295a53c90e) [#41671](https://github.com/sgl-project/sglang/pull/41671)
  [diffusion] optimization: fuse Flux3 rowwise FP8 quantization with triton (#41671)
  _Files: `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/quantization/fp8_rowwise_triton.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux3.py`, `test/registered/kernels/benchmark/diffusion/bench_fp8_rowwise.py` _+1 more__
- **2026-10-03** [`e83c95b650`](https://github.com/sgl-project/sglang/commit/e83c95b650) [#39950](https://github.com/sgl-project/sglang/pull/39950)
  [AMD] Fix AITER weight slicing for CP decode TP (#39950)
  _Files: `python/sglang/srt/layers/cp/cp_decode_attn_tp.py`, `test/registered/kernels/ops/quantization/test_fp8_utils_aiter.py`_
- **2026-10-03** [`254aa41f78`](https://github.com/sgl-project/sglang/commit/254aa41f78) [#42203](https://github.com/sgl-project/sglang/pull/42203)
  [Fix] Guard DeepSeek NVFP4 shared-expert fusion for LoRA and FP4 backends (#42203)
  _Files: `python/sglang/srt/layers/quantization/fp4_utils.py`, `python/sglang/srt/models/deepseek_v2.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4.py`_
- **2026-10-03** [`ce617d410b`](https://github.com/sgl-project/sglang/commit/ce617d410b) [#42255](https://github.com/sgl-project/sglang/pull/42255)
  [diffusion] fix: fix native FP8 format handling for FLUX 3 row-wise linears (#42255)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/flux3.py`, `python/sglang/multimodal_gen/test/unit/test_flux3_action.py`, `python/sglang/multimodal_gen/test/unit/test_modelopt_fp8_layerwise_offload_load.py`, `python/sglang/multimodal_gen/test/unit/test_transformer_quant.py`_
- **2026-10-02** [`a74f259f38`](https://github.com/sgl-project/sglang/commit/a74f259f38) [#42055](https://github.com/sgl-project/sglang/pull/42055)
  [AMD][V4.1][*/N] Fuse MXFP8 activation quant into producer kernels on gfx950 (#42055)
  _Files: `python/sglang/kernels/ops/activation/silu_and_mul_clamp_hip.py`, `python/sglang/kernels/ops/gemm/gfx95_batched_gemm_bf16_fp8_grid.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_common/amd/deepseek_v2_hip_act.py` _+5 more__
- **2026-10-02** [`e667ab10d5`](https://github.com/sgl-project/sglang/commit/e667ab10d5) [#38040](https://github.com/sgl-project/sglang/pull/38040)
  [diffusion] quantization: ConvRot INT8 online W8A8 for DiTs (sgl-kernel + `convrot_int8_customkernel`) (#38040)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/environment_variables.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/kernels/jit/csrc/gemm/convrot_int8/convrot_int8_entry.cuh` _+30 more__
- **2026-10-02** [`e020b389b6`](https://github.com/sgl-project/sglang/commit/e020b389b6) [#41973](https://github.com/sgl-project/sglang/pull/41973)
  [AMD][CI] Partition stage-b-test-1-gpu-small-amd-mi35x to stop the 30-min timeout (#41973)
  _Files: `.github/workflows/pr-test-amd.yml`, `test/registered/e2e/quantization/test_quark_mxfp4.py`_
- **2026-10-01** [`73ba6513f4`](https://github.com/sgl-project/sglang/commit/73ba6513f4) [#41970](https://github.com/sgl-project/sglang/pull/41970)
  [AMD][V4.1][*/N] Switch the fp8 dense GEMMs on gfx950 to aiter's MXFP8 GEMM (#41970)
  _Files: `python/sglang/kernels/ops/quantization/mxfp8_aiter_gfx95.py`, `python/sglang/kernels/ops/speculative/dspark/dspark_draft_model.py`, `python/sglang/srt/layers/quantization/fp8_hip.py`, `python/sglang/srt/layers/quantization/fp8_utils.py` _+3 more__
- **2026-10-01** [`69240ba7d6`](https://github.com/sgl-project/sglang/commit/69240ba7d6) [#41971](https://github.com/sgl-project/sglang/pull/41971)
  [AMD][V4.1][*/N] Pick the gfx950 wo_a batched gemm tile by row count (#41971)
  _Files: `python/sglang/kernels/ops/gemm/gfx95_batched_gemm_bf16_fp8_grid.py`, `test/registered/kernels/ops/quantization/test_fp8_grid_producers_gfx95.py`_
- **2026-09-30** [`036a3b3e14`](https://github.com/sgl-project/sglang/commit/036a3b3e14) [#41799](https://github.com/sgl-project/sglang/pull/41799)
  [Test] Lower the SM120 NVFP4 KV GSM8K threshold to 0.60 (#41799)
  _Files: `test/registered/e2e/quantization/test_llama8b_nvfp4_kv_cache_sm120.py`_
- **2026-09-30** [`47dcde70f4`](https://github.com/sgl-project/sglang/commit/47dcde70f4) [#41849](https://github.com/sgl-project/sglang/pull/41849)
  [Docs] Add MI355X FP8 agentic recipe to the Qwen3.5 cookbook (#41849)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-09-29** [`9ae43b0eee`](https://github.com/sgl-project/sglang/commit/9ae43b0eee) [#40828](https://github.com/sgl-project/sglang/pull/40828)
  [XPU] Support compressed-tensors W4A16 by reusing the torch int4pack path (#40828)
  _Files: `python/sglang/srt/hardware_backend/xpu/quantization/compressed_tensors_wna16_kernels.py`, `python/sglang/srt/hardware_backend/xpu/quantization/int4pack_utils.py`, `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py` _+2 more__

## Models  (11 commits)

- **2026-10-04** [`a99567ab74`](https://github.com/sgl-project/sglang/commit/a99567ab74) [#42480](https://github.com/sgl-project/sglang/pull/42480)
  [Fix] GigaChat 3.5: build the stage boundaries once (#42480)
  _Files: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/gigachat35.py`, `test/registered/unit/layer_boundary/test_stage_boundaries_built_once.py`_
- **2026-10-04** [`92d60351e2`](https://github.com/sgl-project/sglang/commit/92d60351e2) [#42477](https://github.com/sgl-project/sglang/pull/42477)
  [Refactor] Build the Hunyuan V4 decoder from stage boundaries (#42477)
  _Files: `python/sglang/srt/layers/layer_boundary/__init__.py`, `python/sglang/srt/layers/layer_boundary/residual/ihc.py`, `python/sglang/srt/models/hunyuan_v4.py`, `python/sglang/srt/models/hunyuan_v4_nextn.py` _+1 more__
- **2026-10-04** [`caf96324fc`](https://github.com/sgl-project/sglang/commit/caf96324fc) [#36780](https://github.com/sgl-project/sglang/pull/36780)
  [Apple Silicon] Add an Apple Silicon (MPS) platform to the standard Torch model runner (#36780)
  _Files: `.github/workflows/pr-test-mlx.yml`, `python/sglang/_platform_stubs.py`, `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/hardware_backend/mps/__init__.py` _+16 more__
- **2026-10-03** [`f85c2c4923`](https://github.com/sgl-project/sglang/commit/f85c2c4923) [#42310](https://github.com/sgl-project/sglang/pull/42310)
  [Fix] GigaChat 3.5: apply the sandwich norms to the complete sums (#42310)
  _Files: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/gigachat35.py`_
- **2026-10-01** [`3031091c36`](https://github.com/sgl-project/sglang/commit/3031091c36) [#40269](https://github.com/sgl-project/sglang/pull/40269)
  [Kimi-K3] Guard optimized paths by platform (#40269)
  _Files: `python/sglang/srt/layers/attn_residual.py`, `python/sglang/srt/models/kimi_k3.py`_
- **2026-09-30** [`00659ac099`](https://github.com/sgl-project/sglang/commit/00659ac099) [#41815](https://github.com/sgl-project/sglang/pull/41815)
  [Refactor] Stop passing models' layers the placement they already read (#41815)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_dspark.py`, `python/sglang/srt/models/glm5_next.py`, `python/sglang/srt/models/grok.py` _+2 more__
- **2026-09-30** [`d41904f05e`](https://github.com/sgl-project/sglang/commit/d41904f05e) [#41779](https://github.com/sgl-project/sglang/pull/41779)
  [Refactor] Build seven more decoders from stage boundaries (#41779)
  _Files: `python/sglang/srt/layers/layer_boundary/boundary.py`, `python/sglang/srt/layers/layer_boundary/construction.py`, `python/sglang/srt/layers/layer_boundary/contracts.py`, `python/sglang/srt/layers/layer_boundary/exit.py` _+8 more__
- **2026-09-30** [`faa5064f6e`](https://github.com/sgl-project/sglang/commit/faa5064f6e) [#41753](https://github.com/sgl-project/sglang/pull/41753)
  [Refactor] Send producer-written residual streams through to_pp (#41753)
  _Files: `docs/docs/developer_guide/layer_boundary.mdx`, `python/sglang/srt/layers/layer_boundary/residual/batch.py`, `python/sglang/srt/models/glm5_next.py`_
- **2026-09-29** [`bd78095030`](https://github.com/sgl-project/sglang/commit/bd78095030) [#41059](https://github.com/sgl-project/sglang/pull/41059)
  [Fix] Add name mapping in load_weights of nvidia/LocateAnything-3B (#41059)
  _Files: `python/sglang/srt/models/locate_anything.py`, `test/registered/unit/models/test_locate_anything.py`_
- **2026-09-28** [`47ad1928a2`](https://github.com/sgl-project/sglang/commit/47ad1928a2) [#41226](https://github.com/sgl-project/sglang/pull/41226)
  [sgl-router] Scope input_ids forwarding by renderer: all text chats for DeepSeek-V4 (#41226)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/server/metrics.rs`, `experimental/sgl-router/src/server/routes/chat/preparation.rs`, `experimental/sgl-router/src/tokenizer/chat_formatter.rs` _+6 more__
- **2026-09-28** [`546bfa7221`](https://github.com/sgl-project/sglang/commit/546bfa7221) [#41164](https://github.com/sgl-project/sglang/pull/41164)
  [Kimi-K3] Merge fused_qkvg_proj into the loader-seeded packed_modules_mapping (#41164)
  _Files: `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/models/test_kimi_k3_packed_modules_mapping.py`_

## Speculative Decoding  (10 commits)

- **2026-10-04** [`29bcb74a89`](https://github.com/sgl-project/sglang/commit/29bcb74a89) [#42461](https://github.com/sgl-project/sglang/pull/42461)
  [AMD][CI] Fix ROCm kernel wheel sources: drop eagle_utils, add DSV4 kernels (#42461)
  _Files: `3rdparty/amd/wheel/sgl-kernel/CMakeLists_rocm.txt`, `3rdparty/amd/wheel/sgl-kernel/rocm_hipify.py`_
- **2026-10-03** [`b2aa993cb8`](https://github.com/sgl-project/sglang/commit/b2aa993cb8) [#42347](https://github.com/sgl-project/sglang/pull/42347)
  [Fix] Skip a draft's decode recapture when it owns no decode graph (#42347)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `test/registered/unit/model_executor/test_draft_graph_recapture.py`_
- **2026-10-03** [`1a18de4b29`](https://github.com/sgl-project/sglang/commit/1a18de4b29) [#42346](https://github.com/sgl-project/sglang/pull/42346)
  [Fix] Load a draft's tensor weight update from its deployment TP rank (#42346)
  _Files: `python/sglang/srt/model_executor/model_runner_components/weight_updater.py`, `test/registered/unit/model_executor/test_weight_update_tensor_rank.py`_
- **2026-10-03** [`e4554fd5e5`](https://github.com/sgl-project/sglang/commit/e4554fd5e5) [#42308](https://github.com/sgl-project/sglang/pull/42308)
  [Refactor] Build the Llama and Nemotron-NAS decoders from stage boundaries (#42308)
  _Files: `python/sglang/srt/layers/layer_boundary/prepare.py`, `python/sglang/srt/models/llama.py`, `python/sglang/srt/models/llama_eagle.py`, `python/sglang/srt/models/llama_eagle3.py` _+5 more__
- **2026-10-03** [`740a4d5955`](https://github.com/sgl-project/sglang/commit/740a4d5955) [#42307](https://github.com/sgl-project/sglang/pull/42307)
  [Refactor] Build the Qwen2 decoders from stage boundaries (#42307)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/layer_boundary/residual/access.py`, `python/sglang/srt/layers/layer_boundary/residual/batch.py`, `python/sglang/srt/layers/layernorm.py` _+8 more__
- **2026-10-01** [`d669efba84`](https://github.com/sgl-project/sglang/commit/d669efba84) [#41981](https://github.com/sgl-project/sglang/pull/41981)
  [AMD][V4.1][*/N] Greedy dspark draft/accept under SGLANG_SIMULATE_ACC_LEN (#41981)
  _Files: `python/sglang/kernels/ops/speculative/dspark/simulated_bonus.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py` _+1 more__
- **2026-09-30** [`f050ab194a`](https://github.com/sgl-project/sglang/commit/f050ab194a) [#41154](https://github.com/sgl-project/sglang/pull/41154)
  fix(spec): enable Qwen3.5 EAGLE3 capture and streaming overlap (#41154)
  _Files: `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_utils/buffers.py`, `python/sglang/srt/models/qwen3_5.py` _+2 more__
- **2026-09-29** [`d3f8a8f4f5`](https://github.com/sgl-project/sglang/commit/d3f8a8f4f5) [#41623](https://github.com/sgl-project/sglang/pull/41623)
  [Spec/Prefill Coordination] Dspark support (#41623)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/speculative/dspark_components/dspark_draft.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`, `test/registered/spec/dspark/test_dspark_dp_spec_prefill_coordination.py` _+2 more__
- **2026-09-28** [`f209e67767`](https://github.com/sgl-project/sglang/commit/f209e67767) [#39643](https://github.com/sgl-project/sglang/pull/39643)
  [Spec] Model-agnostic last-stage draft embedding under pipeline parallelism (#39643)
  _Files: `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/frozen_kv_mtp_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` _+4 more__
- **2026-09-28** [`7ee7bef79d`](https://github.com/sgl-project/sglang/commit/7ee7bef79d) [#39354](https://github.com/sgl-project/sglang/pull/39354)
  docs: add prefill context parallelism guide and design draft (#39354)
  _Files: `docs/docs.json`, `docs/docs/advanced_features/overview.mdx`, `docs/docs/advanced_features/prefill_cp.mdx`_

## Triton / Kernels  (9 commits)

- **2026-10-04** [`c12bc635ca`](https://github.com/sgl-project/sglang/commit/c12bc635ca) [#42233](https://github.com/sgl-project/sglang/pull/42233)
  [CI] Install only userspace libgdrapi for GDRCopy (#42233)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-10-03** [`4301be7bdb`](https://github.com/sgl-project/sglang/commit/4301be7bdb) [#42405](https://github.com/sgl-project/sglang/pull/42405)
  Pick the default nccl_port below the kernel ephemeral range (#42405)
  _Files: `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/network.py`_
- **2026-10-03** [`3122b9c995`](https://github.com/sgl-project/sglang/commit/3122b9c995) [#42366](https://github.com/sgl-project/sglang/pull/42366)
  Update AOT kernels for Torch 2.14 (#42366)
  _Files: `python/sglang/kernels/aot/CMakeLists.txt`, `python/sglang/kernels/aot/Dockerfile`, `python/sglang/kernels/aot/README.md`, `python/sglang/kernels/aot/pyproject.toml`_
- **2026-10-03** [`3dc7f4b816`](https://github.com/sgl-project/sglang/commit/3dc7f4b816) [#40543](https://github.com/sgl-project/sglang/pull/40543)
  fix(cuda-graph): remove unnecessary CP batch alignment (#40543)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-10-02** [`354ed2a7b6`](https://github.com/sgl-project/sglang/commit/354ed2a7b6) [#42125](https://github.com/sgl-project/sglang/pull/42125)
  Size the VMM graph-input exchange by the widest input across ranks (#42125)
  _Files: `python/sglang/srt/utils/cuda_vmm_utils.py`, `test/registered/unit/test_cuda_vmm_utils.py`_
- **2026-10-02** [`1a2eb6c426`](https://github.com/sgl-project/sglang/commit/1a2eb6c426) [#42004](https://github.com/sgl-project/sglang/pull/42004)
  [Kernel] Use Cake softmax for qualified SM103 sampling workloads (#42004)
  _Files: `python/sglang/kernels/cake_kernels/README.md`, `python/sglang/kernels/cake_kernels/__init__.py`, `python/sglang/kernels/cake_kernels/sampling.py`, `python/sglang/kernels/ops/sampling/__init__.py` _+1 more__
- **2026-09-28** [`0318a8d0af`](https://github.com/sgl-project/sglang/commit/0318a8d0af) [#41545](https://github.com/sgl-project/sglang/pull/41545)
  [Doc] Add kernel benchmark rule on L2 cache reuse (#41545)
  _Files: `.claude/rules/kernel-benchmark.md`, `.claude/skills/add-jit-kernel/SKILL.md`, `.claude/skills/add-sgl-kernel/SKILL.md`_
- **2026-09-28** [`e8eeff2956`](https://github.com/sgl-project/sglang/commit/e8eeff2956) [#41220](https://github.com/sgl-project/sglang/pull/41220)
  [XPU] Bump sglang-kernel-xpu wheel to v0.3.0 (#41220)
  _Files: `python/pyproject_xpu.toml`_
- **2026-09-28** [`6cbdfec453`](https://github.com/sgl-project/sglang/commit/6cbdfec453) [#40814](https://github.com/sgl-project/sglang/pull/40814)
  [Fix][NPU] Fix performance degradation caused by serial execution of two-stage ACL op calls on graph (#40814)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py`_

## Scheduler / Batching  (9 commits)

- **2026-10-03** [`482b062d28`](https://github.com/sgl-project/sglang/commit/482b062d28) [#42183](https://github.com/sgl-project/sglang/pull/42183)
  [Feature] serve pplx-decider decision checkpoints on /v1/systemone (#42183)
  _Files: `docs/cards/logos/perplexity.png`, `docs/cookbook/autoregressive/Perplexity/pplx-decider-v1-27b.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+10 more__
- **2026-10-02** [`4a4dad1cf1`](https://github.com/sgl-project/sglang/commit/4a4dad1cf1) [#42025](https://github.com/sgl-project/sglang/pull/42025)
  [Metrics] Label scheduler stage wall time by sampled forward overlap (#42025)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/observability/metrics_collector.py`, `python/sglang/srt/observability/scheduler_stage_metrics.py` _+5 more__
- **2026-09-30** [`63321e3693`](https://github.com/sgl-project/sglang/commit/63321e3693) [#41950](https://github.com/sgl-project/sglang/pull/41950)
  [Scheduler] Move internal-state readback and updates into a collaborator (#41950)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/internal_state.py`, `test/registered/unit/managers/test_exportable_env_vars.py`, `test/registered/unit/managers/test_scheduler_internal_state_world_size.py` _+1 more__
- **2026-09-30** [`a659e6461f`](https://github.com/sgl-project/sglang/commit/a659e6461f) [#41809](https://github.com/sgl-project/sglang/pull/41809)
  [Fix] Size the prefill delayer's gather buffer to its TP group (#41809)
  _Files: `python/sglang/srt/managers/prefill_delayer.py`, `test/registered/unit/managers/test_prefill_delayer_gather.py`_
- **2026-09-29** [`46beacf13d`](https://github.com/sgl-project/sglang/commit/46beacf13d) [#41709](https://github.com/sgl-project/sglang/pull/41709)
  [grpc rust] Define semantic frontend contract (#41709)
  _Files: `rust/sglang-server/src/api_server.rs`, `rust/sglang-server/src/api_server/app.rs`, `rust/sglang-server/src/api_server/common.rs`, `rust/sglang-server/src/api_server/frame.rs` _+16 more__
- **2026-09-29** [`3c4653b6a3`](https://github.com/sgl-project/sglang/commit/3c4653b6a3) [#39706](https://github.com/sgl-project/sglang/pull/39706)
  [Metrics] Fix PD latency histogram accounting (#39706)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/observability/metrics_collector.py`, `test/registered/unit/observability/test_ray_wrappers.py`_
- **2026-09-29** [`51ace48387`](https://github.com/sgl-project/sglang/commit/51ace48387) [#40275](https://github.com/sgl-project/sglang/pull/40275)
  [Metrics] Add request-level TPOT histogram (sglang:request_time_per_output_token_seconds) (#40275)
  _Files: `docs/docs/references/production_metrics.mdx`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/observability/metrics_collector.py`, `python/sglang/srt/observability/req_time_stats.py` _+4 more__
- **2026-09-29** [`8f2a9638f7`](https://github.com/sgl-project/sglang/commit/8f2a9638f7) [#38600](https://github.com/sgl-project/sglang/pull/38600)
  [metrics] Fix non-streaming TTFT by flushing the first output through detokenization (#38600)
  _Files: `docs/docs/references/production_metrics.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
- **2026-09-29** [`069523f999`](https://github.com/sgl-project/sglang/commit/069523f999) [#39385](https://github.com/sgl-project/sglang/pull/39385)
  [Rust] Extract a transport-neutral frontend core (#39385)
  _Files: `rust/sglang-server/src/api_server.rs`, `rust/sglang-server/src/api_server/app.rs`, `rust/sglang-server/src/api_server/common.rs`, `rust/sglang-server/src/api_server/guard.rs` _+17 more__

## LoRA  (5 commits)

- **2026-10-02** [`edee4308bc`](https://github.com/sgl-project/sglang/commit/edee4308bc) [#42191](https://github.com/sgl-project/sglang/pull/42191)
  [sgl-router] Add OpenAI /v1/embeddings (#42191)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/server/app.rs`, `experimental/sgl-router/src/server/routes/chat.rs`, `experimental/sgl-router/src/server/routes/chat/forward.rs` _+8 more__
- **2026-10-01** [`3fb721917d`](https://github.com/sgl-project/sglang/commit/3fb721917d) [#41322](https://github.com/sgl-project/sglang/pull/41322)
  [Fix] Require admin auth for /load_lora_adapter_from_tensors and /set_trace_level (#41322)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `test/registered/unit/entrypoints/test_http_server_auth_levels.py`_
- **2026-10-01** [`b4df214948`](https://github.com/sgl-project/sglang/commit/b4df214948) [#31808](https://github.com/sgl-project/sglang/pull/31808)
  Fix LoRA usage-counter accounting across request lifecycle paths (#31808)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
- **2026-10-01** [`ebccddce19`](https://github.com/sgl-project/sglang/commit/ebccddce19) [#41766](https://github.com/sgl-project/sglang/pull/41766)
  [Rust] Implement the Rust gRPC adapter for native generation (#41766)
  _Files: `rust/Cargo.lock`, `rust/sglang-server/Cargo.toml`, `rust/sglang-server/src/api_server/frame.rs`, `rust/sglang-server/src/frontend/contract.rs` _+8 more__
- **2026-09-29** [`c5a38d3998`](https://github.com/sgl-project/sglang/commit/c5a38d3998) [#41268](https://github.com/sgl-project/sglang/pull/41268)
  [sgl-router] Add --tokenizer-backend fast and --tokenizer-l1-cache-mb (#41268)
  _Files: `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs` _+27 more__

## Serving / API  (4 commits)

- **2026-10-01** [`ebdeba2fee`](https://github.com/sgl-project/sglang/commit/ebdeba2fee) [#41789](https://github.com/sgl-project/sglang/pull/41789)
  [Fix] Emit Responses reasoning content-part events (#41789)
  _Files: `python/sglang/srt/entrypoints/openai/serving_responses.py`, `test/registered/unit/entrypoints/openai/test_serving_responses_stream.py`_
- **2026-09-30** [`826f15bf9c`](https://github.com/sgl-project/sglang/commit/826f15bf9c) [#40077](https://github.com/sgl-project/sglang/pull/40077)
  [Fix] Preserve inline instructions for Responses and Kimi K3 Messages (#40077)
  _Files: `python/sglang/srt/entrypoints/anthropic/serving.py`, `python/sglang/srt/entrypoints/openai/chat_encoding.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py` _+3 more__
- **2026-09-29** [`211b1d9784`](https://github.com/sgl-project/sglang/commit/211b1d9784) [#41756](https://github.com/sgl-project/sglang/pull/41756)
  [Refactor] Share PD routing fields across request models (#41756)
  _Files: `python/sglang/srt/entrypoints/anthropic/protocol.py`, `python/sglang/srt/entrypoints/anthropic/serving.py`, `python/sglang/srt/entrypoints/openai/protocol.py`_
- **2026-09-28** [`6405cf2881`](https://github.com/sgl-project/sglang/commit/6405cf2881) [#41517](https://github.com/sgl-project/sglang/pull/41517)
  Fix chat template cache key order (#41517)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`_

---
_Generated 2026-10-05 17:06 UTC_