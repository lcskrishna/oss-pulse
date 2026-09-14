# sgl-project/sglang — Weekly Change Report
**Period:** 2026-09-07 → 2026-09-14  |  **Total commits:** 379

## ✨ New Features This Week

- **2026-09-14** [#38833](https://github.com/sgl-project/sglang/pull/38833) — [NPU][CI] Add CANN 9.1.0 and Ascend a5 nightly suites (#38833)
- **2026-09-14** [#39406](https://github.com/sgl-project/sglang/pull/39406) — [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260913, enable TOPK_V2 (#39406)
- **2026-09-14** [#37413](https://github.com/sgl-project/sglang/pull/37413) — [AMD][DSV4] feat: enable fp8 two-pool unified_kv on gfx950 (#37413)
- **2026-09-14** [#37425](https://github.com/sgl-project/sglang/pull/37425) — HiCache: Add @rank_consensus to various functions (#37425)
- **2026-09-14** [#37382](https://github.com/sgl-project/sglang/pull/37382) — [NPU] Support DSV4 host memory cache management (#37382)
- **2026-09-14** [#39337](https://github.com/sgl-project/sglang/pull/39337) — chore: add hzh0425 and xiezhq-hermann as Rust tree and HiSparse code owners (#39337)
- **2026-09-14** [#37418](https://github.com/sgl-project/sglang/pull/37418) — [unified-memory] Enable prefill cuda-graph capture (#37418)
- **2026-09-14** [#36472](https://github.com/sgl-project/sglang/pull/36472) — [feat] Add base NpuSRTPlatform implementation (#36472)
- **2026-09-13** [#36141](https://github.com/sgl-project/sglang/pull/36141) — [PD] Add /v1/responses support to the HTTP PD router (#36141)
- **2026-09-13** [#39122](https://github.com/sgl-project/sglang/pull/39122) — [PD][OpenAI] Gate /v1/responses persistence behind --enable-response-store, default off (#39122)
- _…and 88 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-14** [`242d8a70c0`](https://github.com/sgl-project/sglang/commit/242d8a70c0) [#39406](https://github.com/sgl-project/sglang/pull/39406) — [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260913, enable TOPK_V2 (#39406)
- **2026-09-14** [`5aa9b8fb3e`](https://github.com/sgl-project/sglang/commit/5aa9b8fb3e) [#37413](https://github.com/sgl-project/sglang/pull/37413) — [AMD][DSV4] feat: enable fp8 two-pool unified_kv on gfx950 (#37413)
- **2026-09-14** [`95140a7b0c`](https://github.com/sgl-project/sglang/commit/95140a7b0c) [#39396](https://github.com/sgl-project/sglang/pull/39396) — [docs] DeepSeek-V4: MI355X PD disaggregation recipes for all three strategies (#39396)
- **2026-09-14** [`5200508b0f`](https://github.com/sgl-project/sglang/commit/5200508b0f) [#32888](https://github.com/sgl-project/sglang/pull/32888) — [AMD][gfx95] Fill the chunked-prefill compute budget exactly (#32888)
- **2026-09-14** [`3eeb7d37f9`](https://github.com/sgl-project/sglang/commit/3eeb7d37f9) [#39172](https://github.com/sgl-project/sglang/pull/39172) — [AMD] gfx950 assembly attention: length-aware split-KV for dynamic workload (#39172)
- **2026-09-14** [`ce66ba2844`](https://github.com/sgl-project/sglang/commit/ce66ba2844) [#39360](https://github.com/sgl-project/sglang/pull/39360) — [AMD] Fix AITER FP8-Q unified-attention Test (#39360)
- **2026-09-14** [`edf9584be9`](https://github.com/sgl-project/sglang/commit/edf9584be9) [#39356](https://github.com/sgl-project/sglang/pull/39356) — [AMD][CI] Disable Wave attention test file on ROCm 10 (#39356)
- **2026-09-14** [`2f5cc8e33e`](https://github.com/sgl-project/sglang/commit/2f5cc8e33e) [#39358](https://github.com/sgl-project/sglang/pull/39358) — [AMD] Align Qwen3.5 MI355X cookbook with AttnFP8-V2 and HiCache direct / page_first_direct (#39358)
- **2026-09-13** [`4358a1617c`](https://github.com/sgl-project/sglang/commit/4358a1617c) [#39324](https://github.com/sgl-project/sglang/pull/39324) — chore: bump sgl-kernel version to 0.4.7 (#39324)
- **2026-09-13** [`d6fabb74b4`](https://github.com/sgl-project/sglang/commit/d6fabb74b4) [#37564](https://github.com/sgl-project/sglang/pull/37564) — [AMD][Fix] Fix aiter bpreshuffle GEMM for output sizes it cannot dispatch for qwen3.5 mxfp-attn-fp8-v2 TP4 (#37564)
- **2026-09-13** [`7763f666f3`](https://github.com/sgl-project/sglang/commit/7763f666f3) [#39245](https://github.com/sgl-project/sglang/pull/39245) — Fix DeepGEMM release MegaMoE validation without RDMA (#39245)
- **2026-09-13** [`ec5fba5777`](https://github.com/sgl-project/sglang/commit/ec5fba5777) [#39252](https://github.com/sgl-project/sglang/pull/39252) — [AMD] Add dspark config and agentic workload section for deepseek-v4 model (#39252)
- **2026-09-12** [`6657f7d844`](https://github.com/sgl-project/sglang/commit/6657f7d844) [#38328](https://github.com/sgl-project/sglang/pull/38328) — [MoE][ROCm] Admit the unified Triton router on ROCm, including single-group routing (#38328)
- **2026-09-12** [`288627e400`](https://github.com/sgl-project/sglang/commit/288627e400) [#39230](https://github.com/sgl-project/sglang/pull/39230) — [AMD] Document GLM-5.2 MXFP4 recipe update on MI355X (#39230)
- **2026-09-12** [`21289cfd50`](https://github.com/sgl-project/sglang/commit/21289cfd50) [#39116](https://github.com/sgl-project/sglang/pull/39116) — [AMD] Fix Dspark accept length and reduce host bubble on DSV4 (#39116)
- **2026-09-12** [`fd32226706`](https://github.com/sgl-project/sglang/commit/fd32226706) [#38908](https://github.com/sgl-project/sglang/pull/38908) — Fix gpt-oss RunAI streamer weight ownership (#38908)
- **2026-09-12** [`7bc4eb3740`](https://github.com/sgl-project/sglang/commit/7bc4eb3740) [#39104](https://github.com/sgl-project/sglang/pull/39104) — [AMD] Update MI355X MXFP4 HiCache defaults and quick-reduce quantization for Qwen3.5 cookbook (#39104)
- **2026-09-12** [`7c195b9151`](https://github.com/sgl-project/sglang/commit/7c195b9151) [#37254](https://github.com/sgl-project/sglang/pull/37254) — [AMD] Fix Quark load of MiniMax-M3 MXFP4 index_qkv_proj (#37254)
- **2026-09-12** [`55e5e21c88`](https://github.com/sgl-project/sglang/commit/55e5e21c88) [#36651](https://github.com/sgl-project/sglang/pull/36651) — [Qwen3.8-Next] Add PD state transfer for Flash Next (#36651)
- **2026-09-12** [`0d1bea77da`](https://github.com/sgl-project/sglang/commit/0d1bea77da) [#38758](https://github.com/sgl-project/sglang/pull/38758) — [AMD] Allow aiter attention backend for Gemma-4 (#38758)
- **2026-09-12** [`e1d364dd1f`](https://github.com/sgl-project/sglang/commit/e1d364dd1f) [#38757](https://github.com/sgl-project/sglang/pull/38757) — [AMD] aiter: route head_dim>256 prefill through Triton unified_attention (#38757)
- **2026-09-11** [`5f3606c7b2`](https://github.com/sgl-project/sglang/commit/5f3606c7b2) [#39029](https://github.com/sgl-project/sglang/pull/39029) — [Cookbook][AMD] Kimi-K3 MI350X/MI355X: pin a ROCm image with the DSPARK graph-capture fix, add measured cell numbers (#39029)
- **2026-09-11** [`6671cfc775`](https://github.com/sgl-project/sglang/commit/6671cfc775) [#34330](https://github.com/sgl-project/sglang/pull/34330) — [AMD] Fix weight checking for AITER-shuffled block FP8 weights (#34330)
- **2026-09-11** [`a338a9a01c`](https://github.com/sgl-project/sglang/commit/a338a9a01c) [#38585](https://github.com/sgl-project/sglang/pull/38585) — [AMD][CI] Skip failing Wave test and relax multi-LoRA output check (#38585)
- **2026-09-11** [`d7c284b894`](https://github.com/sgl-project/sglang/commit/d7c284b894) [#39106](https://github.com/sgl-project/sglang/pull/39106) — [AMD] Use the triton DSA backend for GLM-5.2 MXFP4 on MI355X (#39106)
- **2026-09-11** [`833bce9df5`](https://github.com/sgl-project/sglang/commit/833bce9df5) [#34432](https://github.com/sgl-project/sglang/pull/34432) — [AMD][DCP 1/N] add dcp support for aiter backend (#34432)
- **2026-09-11** [`ddf02a4f58`](https://github.com/sgl-project/sglang/commit/ddf02a4f58) [#38756](https://github.com/sgl-project/sglang/pull/38756) — [AMD] aiter: resolve SWA KV pool for draft workers + guard paged decode (#38756)
- **2026-09-11** [`2a46cf2ca0`](https://github.com/sgl-project/sglang/commit/2a46cf2ca0) [#36612](https://github.com/sgl-project/sglang/pull/36612) — [PD] Share the prefill->decode failure notification across backends (#36612)
- **2026-09-11** [`822e73ccdd`](https://github.com/sgl-project/sglang/commit/822e73ccdd) [#38269](https://github.com/sgl-project/sglang/pull/38269) — [Unified Cache][AMD] Support DeepSeek-V4 unified KV in direct external linkers (#38269)
- **2026-09-11** [`f618022b73`](https://github.com/sgl-project/sglang/commit/f618022b73) [#39044](https://github.com/sgl-project/sglang/pull/39044) — [AMD][CI] Temporarily pause MI355X disaggregated nightly (#39044)
- **2026-09-11** [`69aa46b2fa`](https://github.com/sgl-project/sglang/commit/69aa46b2fa) [#39036](https://github.com/sgl-project/sglang/pull/39036) — [ROCm] Raise HiCache JIT block quota for mapped-host throughput (#39036)
- **2026-09-11** [`76ef679cb1`](https://github.com/sgl-project/sglang/commit/76ef679cb1) [#38755](https://github.com/sgl-project/sglang/pull/38755) — [AMD] aiter: fail loudly on cross-layer KV sharing in target_verify (#38755)
- **2026-09-11** [`2465ee3948`](https://github.com/sgl-project/sglang/commit/2465ee3948) [#38446](https://github.com/sgl-project/sglang/pull/38446) — [AMD] Fix DeepSeek block-FP8 loading on gfx94x (#38446)
- **2026-09-11** [`b9899b04c1`](https://github.com/sgl-project/sglang/commit/b9899b04c1) [#33939](https://github.com/sgl-project/sglang/pull/33939) — [AMD] Add gfx1151 (Strix Halo / Ryzen AI MAX+) Docker image (#33939)
- **2026-09-11** [`b3dc0388ed`](https://github.com/sgl-project/sglang/commit/b3dc0388ed) [#38791](https://github.com/sgl-project/sglang/pull/38791) — test(lora): enable ROCm logprob accuracy coverage (#38791)
- **2026-09-11** [`7e3ae15f73`](https://github.com/sgl-project/sglang/commit/7e3ae15f73) [#38754](https://github.com/sgl-project/sglang/pull/38754) — [AMD] aiter: honor per-layer softmax scale (#38754)
- **2026-09-11** [`41da06adca`](https://github.com/sgl-project/sglang/commit/41da06adca) [#38954](https://github.com/sgl-project/sglang/pull/38954) — [Refactor] Generalize DeepSeek V4 compressed pool management (#38954)
- **2026-09-11** [`d006f40e24`](https://github.com/sgl-project/sglang/commit/d006f40e24) [#38767](https://github.com/sgl-project/sglang/pull/38767) — [AMD][CI] Retire the ROCm 7.0 kernel wheel (#38767)
- **2026-09-10** [`dc5f59c3a2`](https://github.com/sgl-project/sglang/commit/dc5f59c3a2) [#38947](https://github.com/sgl-project/sglang/pull/38947) — [Refactor] Clarify DeepSeek V4 metadata names for V4.1 (#38947)
- **2026-09-10** [`06dfe05d65`](https://github.com/sgl-project/sglang/commit/06dfe05d65) [#38801](https://github.com/sgl-project/sglang/pull/38801) — [Deps] Raise smg-grpc-servicer floor to >=0.9.0 to unbreak SMG E2E CI (#38801)
- **2026-09-10** [`a26273d668`](https://github.com/sgl-project/sglang/commit/a26273d668) [#38748](https://github.com/sgl-project/sglang/pull/38748) — [AMD] Quantize the bf16 MTP draft experts online to MXFP4 for Qwen3.5 (#38748)
- **2026-09-10** [`12771786f2`](https://github.com/sgl-project/sglang/commit/12771786f2) [#38575](https://github.com/sgl-project/sglang/pull/38575) — [AMD] Restore AITER verify runtime sizing reverted by #34647 (#38575)
- **2026-09-10** [`8a6ab89bf0`](https://github.com/sgl-project/sglang/commit/8a6ab89bf0) [#30575](https://github.com/sgl-project/sglang/pull/30575) — [AMD] Enable Fast Triton Sparse MLA backend (#30575)
- **2026-09-10** [`6b2e13bcb0`](https://github.com/sgl-project/sglang/commit/6b2e13bcb0) [#38686](https://github.com/sgl-project/sglang/pull/38686) — [AMD] Fix the diffusion perf fixture lookup  (#38686)
- **2026-09-10** [`bd922bc39b`](https://github.com/sgl-project/sglang/commit/bd922bc39b) [#38672](https://github.com/sgl-project/sglang/pull/38672) — [AMD][CI] Fix UMBP test buffer after MoRI upgrade (#38672)
- **2026-09-10** [`13fb796c81`](https://github.com/sgl-project/sglang/commit/13fb796c81) [#38694](https://github.com/sgl-project/sglang/pull/38694) — [AMD][CI] Drop the dead miles ROCm 7.0 nightly image build (#38694)
- **2026-09-10** [`026e61bd94`](https://github.com/sgl-project/sglang/commit/026e61bd94) [#38581](https://github.com/sgl-project/sglang/pull/38581) — [AMD] Restore AMD CI registrations dropped by #37436 (#38581)
- **2026-09-10** [`f3152439d0`](https://github.com/sgl-project/sglang/commit/f3152439d0) [#38763](https://github.com/sgl-project/sglang/pull/38763) — [AMD][CI] Publish ROCm 10 release images and kernel wheel (#38763)
- **2026-09-10** [`c415f977b8`](https://github.com/sgl-project/sglang/commit/c415f977b8) [#38677](https://github.com/sgl-project/sglang/pull/38677) — [AMD] Update v4 args for agentic workload (#38677)
- **2026-09-10** [`106cc561f9`](https://github.com/sgl-project/sglang/commit/106cc561f9) [#37495](https://github.com/sgl-project/sglang/pull/37495) — [AMD] ci: move the miles nightlies from rocm700 to rocm10 (#37495)
- **2026-09-10** [`ce555ed82a`](https://github.com/sgl-project/sglang/commit/ce555ed82a) [#38699](https://github.com/sgl-project/sglang/pull/38699) — [diffusion] refactor: refactor utility ownership and document helper placement (#38699)
- **2026-09-10** [`92d831d3d7`](https://github.com/sgl-project/sglang/commit/92d831d3d7) [#37659](https://github.com/sgl-project/sglang/pull/37659) — [AMD] Parallelize aiter spec-decode KV index building over token blocks (#37659)
- **2026-09-09** [`708f51e44b`](https://github.com/sgl-project/sglang/commit/708f51e44b) [#38659](https://github.com/sgl-project/sglang/pull/38659) — [AMD][CI] Make ROCm 10 the Default for AMD PR and Nightly Tests (#38659)
- **2026-09-09** [`5998e9321c`](https://github.com/sgl-project/sglang/commit/5998e9321c) [#38329](https://github.com/sgl-project/sglang/pull/38329) — [AMD][Fix] Fix regression in jit build error with FLUX.2-dev on gfx1250 (#38329)
- **2026-09-09** [`eb42598bdd`](https://github.com/sgl-project/sglang/commit/eb42598bdd) [#38571](https://github.com/sgl-project/sglang/pull/38571) — [AMD][DSV4] Skip the paged SWA page return under the per-request ring (#38571)
- **2026-09-09** [`8ab9982851`](https://github.com/sgl-project/sglang/commit/8ab9982851) [#38174](https://github.com/sgl-project/sglang/pull/38174) — [NPU]support mf device urma and host rdma trans type (#38174)
- **2026-09-08** [`e634ba78a4`](https://github.com/sgl-project/sglang/commit/e634ba78a4) [#37465](https://github.com/sgl-project/sglang/pull/37465) — [AMD] gfx950 assembly attention for EAGLE verify, draft extend and decode  (#37465)
- **2026-09-08** [`141febf329`](https://github.com/sgl-project/sglang/commit/141febf329) [#37140](https://github.com/sgl-project/sglang/pull/37140) — [AMD] fix: use the hardware fp8 e4m3 convert on gfx950 (#37140)
- **2026-09-08** [`7edcdd5ae6`](https://github.com/sgl-project/sglang/commit/7edcdd5ae6) [#38467](https://github.com/sgl-project/sglang/pull/38467) — [AMD] Skip AITER FP8 ASM prefill when GQA is unsupported (#38467)
- **2026-09-08** [`4c3d47f1df`](https://github.com/sgl-project/sglang/commit/4c3d47f1df) [#38456](https://github.com/sgl-project/sglang/pull/38456) — [AMD] Copy MoE weight views before H2D in slow-loading nightlies (#38456)
- **2026-09-08** [`80e9a4ec74`](https://github.com/sgl-project/sglang/commit/80e9a4ec74) [#38411](https://github.com/sgl-project/sglang/pull/38411) — [AMD] [Docker] Update MoRI to v1.2.3 (#38411)
- **2026-09-08** [`5aa913e156`](https://github.com/sgl-project/sglang/commit/5aa913e156) [#37133](https://github.com/sgl-project/sglang/pull/37133) — [AMD][GLM-5.2] Keep GlmMoeDsa MoE e_score_correction_bias in fp32 (#37133)
- **2026-09-07** [`85d39401c8`](https://github.com/sgl-project/sglang/commit/85d39401c8) [#38293](https://github.com/sgl-project/sglang/pull/38293) — [CP V1 Deprecation 3.5/5]  Deprecate HIP/NPU/MUSA prefill CP and remove legacy implementation (#38293)
- **2026-09-07** [`5a5d8e47c5`](https://github.com/sgl-project/sglang/commit/5a5d8e47c5) [#38288](https://github.com/sgl-project/sglang/pull/38288) — [AMD][CI] Remove obsolete split-dim check from Kimi-K3 prefill test (#38288)
- **2026-09-07** [`e9e9e37ddc`](https://github.com/sgl-project/sglang/commit/e9e9e37ddc) [#32759](https://github.com/sgl-project/sglang/pull/32759) — [AMD] Restore SWA reprefill-tail on UnifiedRadixCache when HiCache is off (#32759)
- **2026-09-07** [`570087ceda`](https://github.com/sgl-project/sglang/commit/570087ceda) [#38192](https://github.com/sgl-project/sglang/pull/38192) — [AMD][DSV4] Reland unified-KV pool sizing and SWA ring accounting, fully gated (#38192)
- **2026-09-07** [`6287ebf43a`](https://github.com/sgl-project/sglang/commit/6287ebf43a) [#38318](https://github.com/sgl-project/sglang/pull/38318) — [AMD] Fix EAGLE crash when no kv_index_translator is bound on the DSA fp8 read door (#38318)
- **2026-09-07** [`a8edafff7c`](https://github.com/sgl-project/sglang/commit/a8edafff7c) [#38227](https://github.com/sgl-project/sglang/pull/38227) — [AMD][gfx95] DSV4 wo_b (dp-attention): route to tuned bpreshuffle GEMM instead of triton (#38227)
- **2026-09-07** [`644841c50c`](https://github.com/sgl-project/sglang/commit/644841c50c) [#37691](https://github.com/sgl-project/sglang/pull/37691) — [AMD] Support aiter fa mha chunked kv for Kimi-K3 (#37691)
- **2026-09-07** [`b99175dc7d`](https://github.com/sgl-project/sglang/commit/b99175dc7d) [#38049](https://github.com/sgl-project/sglang/pull/38049) — [Config] Round 6.4: the runtime reads the bags, not the record (#38049)
- **2026-09-07** [`df2f34cca1`](https://github.com/sgl-project/sglang/commit/df2f34cca1) [#38259](https://github.com/sgl-project/sglang/pull/38259) — Drop stale test_mla_gluon_h12_fp8.py broken by aiter gluon rewrite (#38259)
- **2026-09-07** [`503511c963`](https://github.com/sgl-project/sglang/commit/503511c963) [#38256](https://github.com/sgl-project/sglang/pull/38256) — [AMD] Cherry-pick aiter commit for dsv4 a8w8 bpreshuffle gemm config (#38256)
- **2026-09-07** [`1d5d85260c`](https://github.com/sgl-project/sglang/commit/1d5d85260c) [#37601](https://github.com/sgl-project/sglang/pull/37601) — [AMD] support qlen>1 for aiter gluon path for Kimi K3 (#37601)
- **2026-09-07** [`b9b39f222d`](https://github.com/sgl-project/sglang/commit/b9b39f222d) [#37784](https://github.com/sgl-project/sglang/pull/37784) — [AMD] Update ROCm AITER pin to 4ad9983 (#37784)
- **2026-09-07** [`15aa2fb843`](https://github.com/sgl-project/sglang/commit/15aa2fb843) [#37124](https://github.com/sgl-project/sglang/pull/37124) — [ROCm] Take the fused DSA metadata kernels and drop redundant work from the absorb path (#37124)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-09-14 |
| [#26751](https://github.com/sgl-project/sglang/issues/26751) | [Bug] Gemma-4 mm: single non-RGB image crashes vision tower and kills  | — | 2026-09-14 |
| [#37559](https://github.com/sgl-project/sglang/issues/37559) | [Bug] CUDA_ERROR_ILLEGAL_ADDRESS in MXFP8FP4/W4A8 MegaMoE path on B300 | — | 2026-09-14 |
| [#34861](https://github.com/sgl-project/sglang/issues/34861) | [Bug] [NPU] Router GEMM output should always be fp32 | npu | 2026-09-14 |
| [#39367](https://github.com/sgl-project/sglang/issues/39367) | [CI][PD] test_decode_hicache_file_backend_l3_reuses_decode_output_afte | — | 2026-09-14 |
| [#37633](https://github.com/sgl-project/sglang/issues/37633) | [Bug] CUDA illegal memory access in QSA extend forward at 8 concurrent | — | 2026-09-14 |
| [#39302](https://github.com/sgl-project/sglang/issues/39302) | [Bug] GLM-5.x NoPE MLA (qk_rope_head_dim=0) cannot run on SM120: every | — | 2026-09-14 |
| [#37451](https://github.com/sgl-project/sglang/issues/37451) | [Failure Tracker] PR Test (AMD) | ci-failure-tracker | 2026-09-13 |
| [#39311](https://github.com/sgl-project/sglang/issues/39311) | [Bug] DeepSeek-V4 checkpoint with fp8 routed experts scores 10pp lower | — | 2026-09-13 |
| [#6357](https://github.com/sgl-project/sglang/issues/6357) | [Bug] The Prometheus metric `avg_request_queue_latency` is not being c | good first issue | 2026-09-13 |
| [#39279](https://github.com/sgl-project/sglang/issues/39279) | [Feature] Interleaved Prefill Pipeline Parallelism for DeepSeek-V4.1:  | — | 2026-09-13 |
| [#39277](https://github.com/sgl-project/sglang/issues/39277) | [Bug] b12x-vision dev-v4f-2dgx regresses DSV4 history argument encodin | — | 2026-09-13 |
| [#35826](https://github.com/sgl-project/sglang/issues/35826) | [Bug] Grammar token sync initializes a singleton NCCL group under DP a | — | 2026-09-13 |
| [#39173](https://github.com/sgl-project/sglang/issues/39173) | [Bug] DeepSeek-V4.1-Flash + Engram: profiled SPS table (compact ragged | — | 2026-09-13 |
| [#38980](https://github.com/sgl-project/sglang/issues/38980) | [Bug] sgl_kernel flash_attn: is_fa3_supported() accepts sm_89 but no s | — | 2026-09-12 |
| [#38902](https://github.com/sgl-project/sglang/issues/38902) | [Feature] Store DeepSeek-V4.1 C1/C2 Main KV in packed FP4 on Hopper | — | 2026-09-12 |
| [#34815](https://github.com/sgl-project/sglang/issues/34815) | PP8 disaggregated prefill has a load-independent ~30 s TTFT floor on K | — | 2026-09-12 |
| [#37813](https://github.com/sgl-project/sglang/issues/37813) | [Tracking] GLM-5.3-Flash on SM120: required fixes, carry status and re | — | 2026-09-11 |
| [#30599](https://github.com/sgl-project/sglang/issues/30599) | [Feature][AMD] Officially support consumer Radeon RDNA3/RDNA4 (gfx1100 | amd | 2026-09-11 |
| [#35241](https://github.com/sgl-project/sglang/issues/35241) | [Bug] Generation health checks can perturb DP user routing state and c | — | 2026-09-11 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 91 |
| Multimodal | 50 |
| KV Cache / Memory | 37 |
| Prefill / Decode Disaggregation | 35 |
| Other | 30 |
| MoE / Expert Parallel | 30 |
| CI / Build | 18 |
| Quantization | 16 |
| Triton / Kernels | 15 |
| Tensor / Data Parallel | 13 |
| Models | 12 |
| ROCm / AMD | 9 |
| Scheduler / Batching | 6 |
| LoRA | 5 |
| Docs / Examples | 4 |
| Serving / API | 3 |
| Speculative Decoding | 3 |
| Structured Output | 2 |

## Attention / FlashInfer  (91 commits)

- **2026-09-14** [`7465e42b7a`](https://github.com/sgl-project/sglang/commit/7465e42b7a) [#38833](https://github.com/sgl-project/sglang/pull/38833)
  [NPU][CI] Add CANN 9.1.0 and Ascend a5 nightly suites (#38833)
  _Files: `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_fp8_4p_gpqa_a5.py` _+4 more__
- **2026-09-14** [`433c999dd0`](https://github.com/sgl-project/sglang/commit/433c999dd0) [#39403](https://github.com/sgl-project/sglang/pull/39403)
  [NPU][CI] Fix sglang.test.ascend import failure in multi-node e2e pods (#39403)
  _Files: `python/sglang/test/ascend/e2e/run_npu_testcase.sh`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py`, `test/registered/npu/basic_function/dp_attn/test_npu_dp_attention.py`_
- **2026-09-14** [`87db743021`](https://github.com/sgl-project/sglang/commit/87db743021) [#39353](https://github.com/sgl-project/sglang/pull/39353)
  [NPU] Fix device mismatch in SWA mask for DSpark verify graph capture (#39353)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-09-14** [`66c7bc838e`](https://github.com/sgl-project/sglang/commit/66c7bc838e) [#39405](https://github.com/sgl-project/sglang/pull/39405)
  [misc] Revert #38346, #33426, #39061 and #39219 (#39405)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_kda_conv_recurrent_verify.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py` _+5 more__
- **2026-09-14** [`5aa9b8fb3e`](https://github.com/sgl-project/sglang/commit/5aa9b8fb3e) [#37413](https://github.com/sgl-project/sglang/pull/37413)
  [AMD][DSV4] feat: enable fp8 two-pool unified_kv on gfx950 (#37413)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/kernels/ops/attention/dsv4/compress.py`, `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/env_gate.py`, `python/sglang/kernels/ops/attention/dsv4/unified_kv_kernels/layout.py` _+17 more__
- **2026-09-14** [`3eeb7d37f9`](https://github.com/sgl-project/sglang/commit/3eeb7d37f9) [#39172](https://github.com/sgl-project/sglang/pull/39172)
  [AMD] gfx950 assembly attention: length-aware split-KV for dynamic workload (#39172)
  _Files: `python/sglang/kernels/ops/attention/unified_attention_3d_mtp.py`, `python/sglang/kernels/ops/attention/vattn_asm_gfx950/__init__.py`, `python/sglang/kernels/ops/attention/vattn_asm_gfx950/vattn3_core.s`, `python/sglang/kernels/ops/attention/vattn_asm_gfx950/vred.s` _+2 more__
- **2026-09-14** [`ce66ba2844`](https://github.com/sgl-project/sglang/commit/ce66ba2844) [#39360](https://github.com/sgl-project/sglang/pull/39360)
  [AMD] Fix AITER FP8-Q unified-attention Test (#39360)
  _Files: `test/registered/attention/test_aiter_fp8_q_unified_attention.py`_
- **2026-09-14** [`edf9584be9`](https://github.com/sgl-project/sglang/commit/edf9584be9) [#39356](https://github.com/sgl-project/sglang/pull/39356)
  [AMD][CI] Disable Wave attention test file on ROCm 10 (#39356)
  _Files: `test/registered/attention/test_wave_attention_kernels.py`_
- **2026-09-14** [`2fd835b9c1`](https://github.com/sgl-project/sglang/commit/2fd835b9c1) [#39219](https://github.com/sgl-project/sglang/pull/39219)
  [Fix] Don't write conv state from the fused KDA verify kernel (#39219)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_kda_conv_recurrent_verify.py`, `test/registered/kernels/test_fused_kda_conv_recurrent_verify.py`_
- **2026-09-14** [`60f6f03409`](https://github.com/sgl-project/sglang/commit/60f6f03409) [#39061](https://github.com/sgl-project/sglang/pull/39061)
  Fix MUSA detection in compiled prefill path (#39061)
  _Files: `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/utils/common.py`, `test/registered/cp/test_cp_strategy_unit.py`, `test/registered/unit/utils/test_common.py`_
- **2026-09-14** [`f2111715cd`](https://github.com/sgl-project/sglang/commit/f2111715cd) [#33426](https://github.com/sgl-project/sglang/pull/33426)
  [fa] Make the FlashAttention backend extensible by subclasses (#33426)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/attention/unittests/dense/test_fa4.py`_
- **2026-09-14** [`5a132c061b`](https://github.com/sgl-project/sglang/commit/5a132c061b) [#39232](https://github.com/sgl-project/sglang/pull/39232)
  [Perf] trtllm_mla: reuse the fused fp8 KV/Q prepare on target verify (#39232)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-09-14** [`6410800af9`](https://github.com/sgl-project/sglang/commit/6410800af9) [#37418](https://github.com/sgl-project/sglang/pull/37418)
  [unified-memory] Enable prefill cuda-graph capture (#37418)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/e2e/models/test_inkling_unified.py`, `test/registered/unit/layers/attention/test_flashattention_graph_metadata.py` _+1 more__
- **2026-09-13** [`5ebb16005d`](https://github.com/sgl-project/sglang/commit/5ebb16005d) [#39171](https://github.com/sgl-project/sglang/pull/39171)
  [DeepSeek-V4.1] Bump FlashMLA to the fork's rebase head (v4.1 kernels) (#39171)
  _Files: `python/sglang/kernels/aot/cmake/flashmla.cmake`, `python/sglang/kernels/aot/csrc/flashmla_extension.cc`, `python/sglang/test/kits/basic_decode_correctness_kit.py`_
- **2026-09-13** [`f9fca05803`](https://github.com/sgl-project/sglang/commit/f9fca05803) [#39291](https://github.com/sgl-project/sglang/pull/39291)
  [diffusion] fix: make the sp sequence gather pass contiguous shards (#39291)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/test/unit/test_sp_gather_sharded_sequence_contiguous.py`_
- **2026-09-13** [`3e035a3513`](https://github.com/sgl-project/sglang/commit/3e035a3513) [#38584](https://github.com/sgl-project/sglang/pull/38584)
  [Diffusion] Optimize Qwen-Image-Edit attention on Hopper (#38584)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qwen_qkv_epilogue.cuh`, `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/rope/qwen_qkv_epilogue_jit.py` _+5 more__
- **2026-09-12** [`a66451c058`](https://github.com/sgl-project/sglang/commit/a66451c058) [#38845](https://github.com/sgl-project/sglang/pull/38845)
  [GLM-5.3 Flash] Restore and enable KPool metadata fusion (#38845)
  _Files: `python/sglang/kernels/ops/attention/dsa_kpool_metadata/__init__.py`, `python/sglang/kernels/ops/attention/dsa_kpool_metadata/decode.py`, `python/sglang/kernels/ops/attention/dsa_kpool_metadata/draft_extend.py`, `python/sglang/kernels/ops/attention/dsa_kpool_metadata/scan.py` _+8 more__
- **2026-09-12** [`21289cfd50`](https://github.com/sgl-project/sglang/commit/21289cfd50) [#39116](https://github.com/sgl-project/sglang/pull/39116)
  [AMD] Fix Dspark accept length and reduce host bubble on DSV4 (#39116)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `test/registered/amd/test_deepseek_v4_pro_fp4_dspark.py`_
- **2026-09-12** [`b5a2aebc7e`](https://github.com/sgl-project/sglang/commit/b5a2aebc7e) [#39213](https://github.com/sgl-project/sglang/pull/39213)
  [Docs] GLM-5.3-Flash cookbook: fixed MTP 5/1/6, EP1 + flashinfer_trtllm on Blackwell (#39213)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash-benchmarks.jsx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`_
- **2026-09-12** [`7b89b95168`](https://github.com/sgl-project/sglang/commit/7b89b95168) [#38689](https://github.com/sgl-project/sglang/pull/38689)
  [diffusion] feat: pick the attention backend by measuring it (#38689)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/autotune.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py` _+2 more__
- **2026-09-12** [`6dc7b3421b`](https://github.com/sgl-project/sglang/commit/6dc7b3421b) [#34556](https://github.com/sgl-project/sglang/pull/34556)
  Inference Support Mamba 2 and 1 (#34556)
  _Files: `docs/docs/supported-models/generative_models.mdx`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/hybrid_arch.py`, `python/sglang/srt/configs/mamba.py` _+12 more__
- **2026-09-12** [`6953dae005`](https://github.com/sgl-project/sglang/commit/6953dae005) [#38960](https://github.com/sgl-project/sglang/pull/38960)
  [Qwen 3.8 Next] Remove unused tokenwise QSA implementation and tests (#38960)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh`, `python/sglang/srt/arg_groups/model_overrides/qwen4_exp.py`, `python/sglang/srt/layers/attention/qsa/__init__.py`, `python/sglang/srt/layers/attention/qsa/config.py` _+8 more__
- **2026-09-12** [`1cdc5bca5e`](https://github.com/sgl-project/sglang/commit/1cdc5bca5e) [#38346](https://github.com/sgl-project/sglang/pull/38346)
  fix(qsa): clamp the compress gather to the rows this forward has (#38346)
  _Files: `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`_
- **2026-09-12** [`ff1ce11348`](https://github.com/sgl-project/sglang/commit/ff1ce11348) [#37903](https://github.com/sgl-project/sglang/pull/37903)
  [diffusion] model: support VDN-H3 with a hybrid_window_attn_h3 backend (#37903)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `docs/docs/sglang-diffusion/quantization.mdx` _+41 more__
- **2026-09-12** [`e91c948057`](https://github.com/sgl-project/sglang/commit/e91c948057) [#37069](https://github.com/sgl-project/sglang/pull/37069)
  feat: support TP>1 Domino rollout for DFlash V2 (#37069)
  _Files: `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/domino_utils.py`, `test/registered/e2e/speculative/test_dflash_domino.py`, `test/registered/unit/spec/test_dflash_domino.py`_
- **2026-09-12** [`0d1bea77da`](https://github.com/sgl-project/sglang/commit/0d1bea77da) [#38758](https://github.com/sgl-project/sglang/pull/38758)
  [AMD] Allow aiter attention backend for Gemma-4 (#38758)
  _Files: `docs/docs/advanced_features/attention_backend.mdx`, `python/sglang/srt/arg_groups/model_hook.py`_
- **2026-09-12** [`e1d364dd1f`](https://github.com/sgl-project/sglang/commit/e1d364dd1f) [#38757](https://github.com/sgl-project/sglang/pull/38757)
  [AMD] aiter: route head_dim>256 prefill through Triton unified_attention (#38757)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-09-12** [`b805cc5014`](https://github.com/sgl-project/sglang/commit/b805cc5014) [#37818](https://github.com/sgl-project/sglang/pull/37818)
  [Bugfix] Track DFlash Mamba state at checkpoint boundaries (#37818)
  _Files: `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-09-11** [`f963d7a27c`](https://github.com/sgl-project/sglang/commit/f963d7a27c) [#38851](https://github.com/sgl-project/sglang/pull/38851)
  fix(qsa): make the paged sparse-decode gather memory-safe (zero-fill scratch, int64 offsets, dequant FP8 on gather) (#38851)
  _Files: `python/sglang/srt/layers/attention/qsa/sparse_attn.py`, `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `test/registered/kernel/qsa/test_qsa_strided_zero_fill.py`_
- **2026-09-11** [`a338a9a01c`](https://github.com/sgl-project/sglang/commit/a338a9a01c) [#38585](https://github.com/sgl-project/sglang/pull/38585)
  [AMD][CI] Skip failing Wave test and relax multi-LoRA output check (#38585)
  _Files: `python/sglang/test/lora_utils.py`, `test/registered/attention/test_wave_attention_kernels.py`_
- **2026-09-11** [`833bce9df5`](https://github.com/sgl-project/sglang/commit/833bce9df5) [#34432](https://github.com/sgl-project/sglang/pull/34432)
  [AMD][DCP 1/N] add dcp support for aiter backend (#34432)
  _Files: `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/aiter_mla_gluon.py`, `python/sglang/srt/layers/attention/triton_backend.py` _+5 more__
- **2026-09-11** [`ddf02a4f58`](https://github.com/sgl-project/sglang/commit/ddf02a4f58) [#38756](https://github.com/sgl-project/sglang/pull/38756)
  [AMD] aiter: resolve SWA KV pool for draft workers + guard paged decode (#38756)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/srt/test_aiter_swa_kv_pool_resolver.py`_
- **2026-09-11** [`335f6aab27`](https://github.com/sgl-project/sglang/commit/335f6aab27) [#33672](https://github.com/sgl-project/sglang/pull/33672)
  [DSV4] Support raw-index output in TopK v2 (#33672)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/ops/attention/dsv4/topk.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `test/registered/kernels/ops/attention/test_topk_v2.py` _+1 more__
- **2026-09-11** [`165d8dd177`](https://github.com/sgl-project/sglang/commit/165d8dd177) [#38827](https://github.com/sgl-project/sglang/pull/38827)
  [NPU][Hicache] Add Ascend Memcache Hicache L3 storage backend (#38827)
  _Files: `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/arg_groups/hicache_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/cache_controller.py` _+7 more__
- **2026-09-11** [`747734dce4`](https://github.com/sgl-project/sglang/commit/747734dce4) [#38807](https://github.com/sgl-project/sglang/pull/38807)
  [NPU]glm5.2 fp8 memory opt (#38807)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`_
- **2026-09-11** [`ad5af539cd`](https://github.com/sgl-project/sglang/commit/ad5af539cd) [#39013](https://github.com/sgl-project/sglang/pull/39013)
  [CI] Trim DSV4 trtllm B200 tests (#39013)
  _Files: `test/registered/attention/unittests/dsv4/test_deepseek_v4.py`, `test/registered/e2e/dsv4/test_dsv4_fp8_trtllm_backend.py`, `test/registered/e2e/models/test_deepseek_v4_flash_fp4_b200_trtllm.py`_
- **2026-09-11** [`17fa5ad327`](https://github.com/sgl-project/sglang/commit/17fa5ad327) [#38993](https://github.com/sgl-project/sglang/pull/38993)
  [Refactor] Generalize attention graph variants in the decode runner (#38993)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/graph_variants.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/shape_key.py` _+6 more__
- **2026-09-11** [`76ef679cb1`](https://github.com/sgl-project/sglang/commit/76ef679cb1) [#38755](https://github.com/sgl-project/sglang/pull/38755)
  [AMD] aiter: fail loudly on cross-layer KV sharing in target_verify (#38755)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/srt/test_aiter_cross_layer_kv_guard.py`_
- **2026-09-11** [`6182d45524`](https://github.com/sgl-project/sglang/commit/6182d45524) [#39019](https://github.com/sgl-project/sglang/pull/39019)
  [Test] Fix Q8KV8 sparse-prefill pool fixture after page-size rename (#39019)
  _Files: `test/registered/kernels/ops/attention/test_q8kv8_sparse_prefill_backend.py`_
- **2026-09-11** [`0fadad8933`](https://github.com/sgl-project/sglang/commit/0fadad8933) [#32798](https://github.com/sgl-project/sglang/pull/32798)
  DFLASH support added for XPU (#32798)
  _Files: `python/sglang/srt/arg_groups/choices.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/attention/xpu_backend.py`, `python/sglang/srt/speculative/dflash_utils.py` _+3 more__
- **2026-09-11** [`7e3ae15f73`](https://github.com/sgl-project/sglang/commit/7e3ae15f73) [#38754](https://github.com/sgl-project/sglang/pull/38754)
  [AMD] aiter: honor per-layer softmax scale (#38754)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-09-11** [`3716e496ea`](https://github.com/sgl-project/sglang/commit/3716e496ea) [#30548](https://github.com/sgl-project/sglang/pull/30548)
  Speculative Decoding support for intel_xpu attention backend on XPU target (#30548)
  _Files: `python/sglang/srt/layers/attention/xpu_backend.py`, `python/sglang/srt/speculative/draft_utils.py`, `test/registered/e2e/xpu/test_spec_eagle_intel_xpu.py`, `test/registered/unit/layers/attention/test_encoder_decoder_varlen_gather.py` _+1 more__
- **2026-09-11** [`41da06adca`](https://github.com/sgl-project/sglang/commit/41da06adca) [#38954](https://github.com/sgl-project/sglang/pull/38954)
  [Refactor] Generalize DeepSeek V4 compressed pool management (#38954)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_memory_pool.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py` _+4 more__
- **2026-09-10** [`d076eec427`](https://github.com/sgl-project/sglang/commit/d076eec427) [#36655](https://github.com/sgl-project/sglang/pull/36655)
  [SM120] Use exact query-head widths for DeepSeek-V4 sparse MLA decode (#36655)
  _Files: `python/sglang/kernels/ops/attention/flash_mla_sm120.py`, `python/sglang/srt/models/deepseek_v4.py`, `test/registered/kernels/ops/attention/test_flash_mla_backends.py`_
- **2026-09-10** [`bb15be6d79`](https://github.com/sgl-project/sglang/commit/bb15be6d79) [#38169](https://github.com/sgl-project/sglang/pull/38169)
  [Spec] Stage Inkling MTP draft metadata before verify (#38169)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/linear/inkling_sconv_backend.py`, `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py` _+1 more__
- **2026-09-10** [`55b45cb45a`](https://github.com/sgl-project/sglang/commit/55b45cb45a) [#38855](https://github.com/sgl-project/sglang/pull/38855)
  fix(qsa): dequantize FP8 cached prefixes in the sparse prefill kernels (#38855)
  _Files: `python/sglang/srt/layers/attention/qsa/sparse_attn.py`, `test/registered/kernel/qsa/test_qsa.py`_
- **2026-09-10** [`209654c420`](https://github.com/sgl-project/sglang/commit/209654c420) [#38826](https://github.com/sgl-project/sglang/pull/38826)
  [NPU][Hicache] Optimize HiCache L2 IO with Memfabric acc_offload (#38826)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `python/sglang/srt/hardware_backend/npu/utils.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/pool_host/mha.py` _+2 more__
- **2026-09-10** [`12771786f2`](https://github.com/sgl-project/sglang/commit/12771786f2) [#38575](https://github.com/sgl-project/sglang/pull/38575)
  [AMD] Restore AITER verify runtime sizing reverted by #34647 (#38575)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-09-10** [`c9c26d56b2`](https://github.com/sgl-project/sglang/commit/c9c26d56b2) [#38784](https://github.com/sgl-project/sglang/pull/38784)
  [diffusion] docs: sync snapshot and minimax-h3 subblock features (#38784)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/README.md`_
- **2026-09-10** [`8a6ab89bf0`](https://github.com/sgl-project/sglang/commit/8a6ab89bf0) [#30575](https://github.com/sgl-project/sglang/pull/30575)
  [AMD] Enable Fast Triton Sparse MLA backend (#30575)
  _Files: `python/sglang/kernels/ops/attention/dsa/triton_sparse_mla.py`, `python/sglang/kernels/ops/attention/dsa/triton_sparse_mla_decode.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/hisparse_hook.py` _+5 more__
- **2026-09-10** [`9a2f17f41d`](https://github.com/sgl-project/sglang/commit/9a2f17f41d) [#38527](https://github.com/sgl-project/sglang/pull/38527)
  Add INT4 and FP4 lanes to the Ling-3.0-flash-VL cookbook (#38527)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash-VL.mdx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash-vl-benchmarks.jsx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash-vl.jsx`_
- **2026-09-10** [`6b2e13bcb0`](https://github.com/sgl-project/sglang/commit/6b2e13bcb0) [#38686](https://github.com/sgl-project/sglang/pull/38686)
  [AMD] Fix the diffusion perf fixture lookup  (#38686)
  _Files: `test/registered/amd/conftest.py`, `test/registered/amd/test_wan22_fp8_mla.py`, `test/registered/amd/test_zimage_turbo.py`_
- **2026-09-10** [`69777c4d36`](https://github.com/sgl-project/sglang/commit/69777c4d36) [#38802](https://github.com/sgl-project/sglang/pull/38802)
  Add DeepSeek-V4.1 Flash cookbook (#38802)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-09-10** [`03e4c06589`](https://github.com/sgl-project/sglang/commit/03e4c06589) [#33922](https://github.com/sgl-project/sglang/pull/33922)
  Fix Qwen3.5 GDN multi-item scoring (#33922)
  _Files: `python/sglang/kernels/ops/attention/fla/chunk.py`, `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/srt/hardware_backend/xpu/kernels/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` _+9 more__
- **2026-09-10** [`3ff226ba8f`](https://github.com/sgl-project/sglang/commit/3ff226ba8f) [#38250](https://github.com/sgl-project/sglang/pull/38250)
  [NPU]Support GLM5.2 and FP8 DSA&Indexer kvcache for 950 (#38250)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` _+6 more__
- **2026-09-10** [`92d831d3d7`](https://github.com/sgl-project/sglang/commit/92d831d3d7) [#37659](https://github.com/sgl-project/sglang/pull/37659)
  [AMD] Parallelize aiter spec-decode KV index building over token blocks (#37659)
  _Files: `python/sglang/kernels/ops/attention/utils.py`, `python/sglang/kernels/ops/kvcache/kv_indices.py`, `python/sglang/kernels/ops/speculative/cache_locs.py`, `python/sglang/srt/layers/attention/aiter_backend.py` _+1 more__
- **2026-09-10** [`880d6fa64d`](https://github.com/sgl-project/sglang/commit/880d6fa64d) [#30805](https://github.com/sgl-project/sglang/pull/30805)
  [DSv4] Integrate TRT-LLM DSv4 Attention for SM100/103 (#30805)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` _+9 more__
- **2026-09-10** [`0084030179`](https://github.com/sgl-project/sglang/commit/0084030179) [#38522](https://github.com/sgl-project/sglang/pull/38522)
  Add Opt-In for GLM-5.3 Flash breakable prefill CUDA graphs (#38522)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx`, `docs/src/snippets/configs/zai-org/glm-5.3-flash.jsx`, `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/pipeline.py` _+5 more__
- **2026-09-09** [`a84ffd1326`](https://github.com/sgl-project/sglang/commit/a84ffd1326) [#36899](https://github.com/sgl-project/sglang/pull/36899)
  feat: add optimized Domino rollout to DFlash V2 (#36899)
  _Files: `python/sglang/srt/arg_groups/fields/spec.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/srt/speculative/dflash_worker_v2.py` _+4 more__
- **2026-09-09** [`96d91ef926`](https://github.com/sgl-project/sglang/commit/96d91ef926) [#38621](https://github.com/sgl-project/sglang/pull/38621)
  [Model] Support GLM-5.3 Flash NVFP4 loading (#38621)
  _Files: `python/sglang/srt/models/glm5_next.py`, `test/registered/unit/models/test_glm5_next_modelopt.py`_
- **2026-09-09** [`8733da8cf4`](https://github.com/sgl-project/sglang/commit/8733da8cf4) [#34430](https://github.com/sgl-project/sglang/pull/34430)
  [rust-server] Use node-local HTTP ports for DP attention (#34430)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/rust_server/server.py`, `test/registered/unit/entrypoints/test_rust_server_dp_ports.py`_
- **2026-09-09** [`ffe98a4279`](https://github.com/sgl-project/sglang/commit/ffe98a4279) [#37982](https://github.com/sgl-project/sglang/pull/37982)
  [Diffusion][MiniMax-H3] Add SM90 Sage compute for SubBlock sparse attention (#37982)
  _Files: `python/sglang/kernels/ops/attention/subblock_sage_fp8_sm90.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/README.md`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/__init__.py` _+6 more__
- **2026-09-09** [`1ad3eb09a9`](https://github.com/sgl-project/sglang/commit/1ad3eb09a9) [#38590](https://github.com/sgl-project/sglang/pull/38590)
  [Attention] Size FlashInfer MLA indptr buffers to the padded max batch (#38590)
  _Files: `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`_
- **2026-09-09** [`13469c16d3`](https://github.com/sgl-project/sglang/commit/13469c16d3) [#34820](https://github.com/sgl-project/sglang/pull/34820)
  Store mamba prefix-cache checkpoints at the configured SSM state dtype (#34820)
  _Files: `python/sglang/kernels/ops/attention/fla/chunk_delta_h.py`, `python/sglang/kernels/ops/attention/fla/kda.py`, `python/sglang/kernels/ops/attention/helion/kda_prefill.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` _+13 more__
- **2026-09-09** [`da821aad11`](https://github.com/sgl-project/sglang/commit/da821aad11) [#33366](https://github.com/sgl-project/sglang/pull/33366)
  [XPU][Diffusion] Enable MiniMax H3 on XPU platforms (#33366)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/xpu_backend.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/keyframe_encoding.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`_
- **2026-09-09** [`295132c4a5`](https://github.com/sgl-project/sglang/commit/295132c4a5) [#33089](https://github.com/sgl-project/sglang/pull/33089)
  [NPU] Add sparsity-driven KV offload for DeepSeek DSA on Ascend (#33089)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `python/sglang/srt/hardware_backend/npu/sparsity_driven_kv_offload/attention.py` _+5 more__
- **2026-09-08** [`a25bbca8ed`](https://github.com/sgl-project/sglang/commit/a25bbca8ed) [#36527](https://github.com/sgl-project/sglang/pull/36527)
  MiniMax-M3: share the sparse index top-k across layers and reuse the decode top-k buffer (#36527)
  _Files: `python/sglang/kernels/ops/attention/minimax_sparse/decode/flash_with_topk_idx.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `python/sglang/srt/layers/attention/minimax_sparse_ops/minimax_sparse.py`_
- **2026-09-08** [`ed183d45ac`](https://github.com/sgl-project/sglang/commit/ed183d45ac) [#36229](https://github.com/sgl-project/sglang/pull/36229)
  [CP V1 Deprecation 4/5] Canonicalize prefill CP API names (#36229)
  _Files: `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dsa/cp_split.py`, `python/sglang/kernels/ops/attention/dsv4/metadata_kernel.py`, `python/sglang/kernels/ops/layernorm/mhc.py` _+29 more__
- **2026-09-08** [`afe90a8bc9`](https://github.com/sgl-project/sglang/commit/afe90a8bc9) [#38539](https://github.com/sgl-project/sglang/pull/38539)
  Point Ling-3.0-flash-VL cookbook install section at the model image (#38539)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash-VL.mdx`_
- **2026-09-08** [`8a0863c728`](https://github.com/sgl-project/sglang/commit/8a0863c728) [#36800](https://github.com/sgl-project/sglang/pull/36800)
  [HiCache] Add MLA host-dedup primitives (#36800)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/mla_host_dedup.py`, `python/sglang/srt/mem_cache/pool_host/dsa.py`, `python/sglang/srt/mem_cache/pool_host/mla.py` _+1 more__
- **2026-09-08** [`482e9f257b`](https://github.com/sgl-project/sglang/commit/482e9f257b) [#38434](https://github.com/sgl-project/sglang/pull/38434)
  Add Ling-3.0-flash-VL cookbook (#38434)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash-VL.mdx`, `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash.mdx`, `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-tiny.mdx`, `docs/cookbook/autoregressive/intro.mdx` _+4 more__
- **2026-09-08** [`2d339ddef1`](https://github.com/sgl-project/sglang/commit/2d339ddef1) [#38422](https://github.com/sgl-project/sglang/pull/38422)
  [NPU] Phase A calibration: full GSM8K eval for dp_attention mixed-chunk (#38422)
  _Files: `.github/workflows/_npu-pr-test-stage.yml`, `test/registered/npu/basic_function/dp_attn/test_npu_dp_attention.py`_
- **2026-09-08** [`e634ba78a4`](https://github.com/sgl-project/sglang/commit/e634ba78a4) [#37465](https://github.com/sgl-project/sglang/pull/37465)
  [AMD] gfx950 assembly attention for EAGLE verify, draft extend and decode  (#37465)
  _Files: `.codespellrc`, `python/sglang/kernels/ops/attention/unified_attention_3d_mtp.py`, `python/sglang/kernels/ops/attention/vattn_asm_gfx950/__init__.py`, `python/sglang/kernels/ops/attention/vattn_asm_gfx950/vattn3_core.s` _+2 more__
- **2026-09-08** [`141febf329`](https://github.com/sgl-project/sglang/commit/141febf329) [#37140](https://github.com/sgl-project/sglang/pull/37140)
  [AMD] fix: use the hardware fp8 e4m3 convert on gfx950 (#37140)
  _Files: `python/sglang/kernels/aot/csrc/elementwise/dsv4_norm_rope.cu`, `python/sglang/kernels/jit/csrc/deepseek_v4/fp8_cvt.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/fp8_utils.cuh`, `python/sglang/kernels/ops/attention/dsv4/fp8_cvt.py` _+2 more__
- **2026-09-08** [`7edcdd5ae6`](https://github.com/sgl-project/sglang/commit/7edcdd5ae6) [#38467](https://github.com/sgl-project/sglang/pull/38467)
  [AMD] Skip AITER FP8 ASM prefill when GQA is unsupported (#38467)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/unit/layers/attention/test_aiter_fp8_asm_gqa.py`_
- **2026-09-08** [`5ae4ccb0fd`](https://github.com/sgl-project/sglang/commit/5ae4ccb0fd) [#38399](https://github.com/sgl-project/sglang/pull/38399)
  [Bench] Amortize the GDN ReplaySSM decode latency over the flush cycle (#38399)
  _Files: `benchmark/kernels/attention/bench_gdn_replayssm_decode.py`_
- **2026-09-08** [`cf35384fe4`](https://github.com/sgl-project/sglang/commit/cf35384fe4) [#35866](https://github.com/sgl-project/sglang/pull/35866)
  [Intel GPU] Add MLA support to Intel XPU Attention backend for Prefill (#35866)
  _Files: `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/attention/xpu_backend.py`, `test/registered/xpu/test_intel_xpu_backend.py`_
- **2026-09-08** [`8656901504`](https://github.com/sgl-project/sglang/commit/8656901504) [#37093](https://github.com/sgl-project/sglang/pull/37093)
  [Fix][DSA] Bound prefill Triton specializations for page-table stride (#37093)
  _Files: `python/sglang/kernels/ops/attention/dsa/transform_index.py`, `test/registered/kernels/ops/attention/test_dsa_transform_index.py`_
- **2026-09-07** [`f4b75b5c36`](https://github.com/sgl-project/sglang/commit/f4b75b5c36) [#37995](https://github.com/sgl-project/sglang/pull/37995)
  docs(cookbook): Qwen3.8-Flash-Next NVFP4 recipes for DGX Spark (1x, 2x) and RTX PRO 6000 (#37995)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-flash-next-benchmarks.jsx`, `docs/src/snippets/configs/Qwen/qwen3.8-flash-next.jsx`_
- **2026-09-07** [`5a5d8e47c5`](https://github.com/sgl-project/sglang/commit/5a5d8e47c5) [#38288](https://github.com/sgl-project/sglang/pull/38288)
  [AMD][CI] Remove obsolete split-dim check from Kimi-K3 prefill test (#38288)
  _Files: `test/registered/unit/layers/attention/test_triton_mla_prefill_gfx950.py`_
- **2026-09-07** [`6287ebf43a`](https://github.com/sgl-project/sglang/commit/6287ebf43a) [#38318](https://github.com/sgl-project/sglang/pull/38318)
  [AMD] Fix EAGLE crash when no kv_index_translator is bound on the DSA fp8 read door (#38318)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`_
- **2026-09-07** [`a711785475`](https://github.com/sgl-project/sglang/commit/a711785475) [#38124](https://github.com/sgl-project/sglang/pull/38124)
  [Kernel] Drop the vendored dense BF16 GEMM port in favor of FlashInfer 0.6.18 (#38124)
  _Files: `python/sglang/kernels/ops/gemm/flashinfer_pr4266_dense_bf16_gemm_sm100_direct.py`, `python/sglang/kernels/ops/gemm/flashinfer_pr4266_dense_bf16_gemm_sm100_splitk.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/environ.py` _+3 more__
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

## Multimodal  (50 commits)

- **2026-09-14** [`39e147443b`](https://github.com/sgl-project/sglang/commit/39e147443b) [#39145](https://github.com/sgl-project/sglang/pull/39145)
  [Session] Fix image append positions and parent metadata (#39145)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/sessions/test_session_control.py`_
- **2026-09-14** [`42b5af8c62`](https://github.com/sgl-project/sglang/commit/42b5af8c62) [#39244](https://github.com/sgl-project/sglang/pull/39244)
  [diffusion] docs: refresh the VDN-H3 on b200 numbers in cookbook (#39244)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `python/sglang/multimodal_gen/runtime/utils/model_overlay.py`_
- **2026-09-14** [`3480112a9c`](https://github.com/sgl-project/sglang/commit/3480112a9c) [#39303](https://github.com/sgl-project/sglang/pull/39303)
  [diffusion] fix: serve requests that turn cfg off on a cfg-parallel server (#39303)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/input_validation.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/runtime/utils/logging_utils.py`, `python/sglang/multimodal_gen/test/unit/test_cfg_parallel_warmup.py` _+1 more__
- **2026-09-13** [`9ffe548738`](https://github.com/sgl-project/sglang/commit/9ffe548738) [#39292](https://github.com/sgl-project/sglang/pull/39292)
  [diffusion] fix: don't route an unreadable checkpoint into the native fallback (#39292)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/test/unit/test_transformer_loader_fallback.py`_
- **2026-09-13** [`d2f054d916`](https://github.com/sgl-project/sglang/commit/d2f054d916) [#39255](https://github.com/sgl-project/sglang/pull/39255)
  [diffusion] CI: make diffusion GT generation usable without the publish token, and cover the 5090 lane (#39255)
  _Files: `.github/workflows/diffusion-ci-gt-gen.yml`_
- **2026-09-13** [`492f346d88`](https://github.com/sgl-project/sglang/commit/492f346d88) [#38657](https://github.com/sgl-project/sglang/pull/38657)
  [diffusion] CI: set an explicit x264 preset for video output (#38657)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/test/test_utils.py`, `python/sglang/multimodal_gen/test/unit/test_video_encode_preset.py`_
- **2026-09-13** [`23bc4c6ed9`](https://github.com/sgl-project/sglang/commit/23bc4c6ed9) [#38549](https://github.com/sgl-project/sglang/pull/38549)
  [Diffusion] Return Qwen-Image-Layered outputs and preserve CFG2 rounding (#38549)
  _Files: `docs/cookbook/diffusion/Qwen-Image/Qwen-Image-Edit.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image.py`, `python/sglang/multimodal_gen/configs/sample/qwenimage.py`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py` _+6 more__
- **2026-09-12** [`dc3171c322`](https://github.com/sgl-project/sglang/commit/dc3171c322) [#39097](https://github.com/sgl-project/sglang/pull/39097)
  [diffusion] CI: remove mova ulysses two-gpu CI case (#39097)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/single_test_file/component_accuracy/config.py`_
- **2026-09-12** [`bf3305b65e`](https://github.com/sgl-project/sglang/commit/bf3305b65e) [#39022](https://github.com/sgl-project/sglang/pull/39022)
  [diffusion] feat: read mapped layers directly when the host cannot cache them (#39022)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/host_memory_budget.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_host_memory_budget.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-09-11** [`5f3606c7b2`](https://github.com/sgl-project/sglang/commit/5f3606c7b2) [#39029](https://github.com/sgl-project/sglang/pull/39029)
  [Cookbook][AMD] Kimi-K3 MI350X/MI355X: pin a ROCm image with the DSPARK graph-capture fix, add measured cell numbers (#39029)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3-benchmarks.jsx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-09-11** [`d6b5dca90c`](https://github.com/sgl-project/sglang/commit/d6b5dca90c) [#38529](https://github.com/sgl-project/sglang/pull/38529)
  [Diffusion] Optimize SANA-WM convolution post-processing and streaming GDN (#38529)
  _Files: `python/sglang/kernels/ops/diffusion/activation/sana_conv_post_triton.py`, `python/sglang/multimodal_gen/runtime/models/dits/sana_wm_components.py`, `test/registered/kernel/diffusion/test_sana_wm_conv_post.py`, `test/registered/kernel/diffusion/test_sana_wm_reverse_scan.py`_
- **2026-09-11** [`e016de462c`](https://github.com/sgl-project/sglang/commit/e016de462c) [#38782](https://github.com/sgl-project/sglang/pull/38782)
  [diffusion] CI: expose nightly server telemetry coverage (#38782)
  _Files: `docs/docs/sglang-diffusion/ci_perf.mdx`, `python/sglang/multimodal_gen/test/unit/test_diffusion_nightly_comparison.py`, `scripts/ci/utils/diffusion/generate_diffusion_dashboard.py`_
- **2026-09-11** [`7f09fbcd25`](https://github.com/sgl-project/sglang/commit/7f09fbcd25) [#38533](https://github.com/sgl-project/sglang/pull/38533)
  [Diffusion] Preserve BF16 rounding in Hopper LTX QKNorm and RoPE fusion (#38533)
  _Files: `python/sglang/kernels/kda_kernels/csrc/diffusion/ltx2_qknorm_split_rope.cuh`, `python/sglang/kernels/kda_kernels/ltx2_qknorm_split_rope_jit.py`_
- **2026-09-11** [`dd67a42634`](https://github.com/sgl-project/sglang/commit/dd67a42634) [#38783](https://github.com/sgl-project/sglang/pull/38783)
  [diffusion] UX: quiet request-path cache diagnostics (#38783)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_residency_strategies.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3_adaln_cache.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/helios_denoising.py`_
- **2026-09-11** [`ab9750fb35`](https://github.com/sgl-project/sglang/commit/ab9750fb35) [#39021](https://github.com/sgl-project/sglang/pull/39021)
  [diffusion] optimization: pin layerwise host stores in place at their exact size (#39021)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-09-11** [`358c163250`](https://github.com/sgl-project/sglang/commit/358c163250) [#39034](https://github.com/sgl-project/sglang/pull/39034)
  [diffusion] fix: recover ipc jit initialization after interrupted builds (#39034)
  _Files: `python/sglang/kernels/jit/csrc/distributed/ipc_a2a.cuh`, `python/sglang/kernels/ops/communication/ipc_a2a.py`, `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a.py`, `test/registered/e2e/diffusion/test_ipc_a2a_jit_recovery.py`_
- **2026-09-11** [`b9899b04c1`](https://github.com/sgl-project/sglang/commit/b9899b04c1) [#33939](https://github.com/sgl-project/sglang/pull/33939)
  [AMD] Add gfx1151 (Strix Halo / Ryzen AI MAX+) Docker image (#33939)
  _Files: `.github/workflows/release-docker-amd-gfx1151-nightly.yml`, `docker/patches/sgl-kernel-gfx1151.sh`, `docker/rocm-gfx1151.Dockerfile`_
- **2026-09-11** [`d0035da34e`](https://github.com/sgl-project/sglang/commit/d0035da34e) [#33555](https://github.com/sgl-project/sglang/pull/33555)
  [Diffusion][Refactor] Refactor and unify RoPE execution for DiT models using RotaryEmbedding based on CustomOp (#33555)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/base.py`, `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/utils.py` _+9 more__
- **2026-09-11** [`00143e9c23`](https://github.com/sgl-project/sglang/commit/00143e9c23) [#38958](https://github.com/sgl-project/sglang/pull/38958)
  Fix dataclasses.asdict on the msgspec ServerArgs (#38958)
  _Files: `benchmark/simulator/bench_runner.py`, `examples/runtime/engine/offline_batch_inference.py`, `examples/runtime/engine/offline_batch_inference_async.py`, `examples/runtime/engine/offline_batch_inference_vlm.py`_
- **2026-09-10** [`fae8cd84cb`](https://github.com/sgl-project/sglang/commit/fae8cd84cb) [#35599](https://github.com/sgl-project/sglang/pull/35599)
  Support NemotronH_Omni_Reasoning_V3 in SGLang (#35599)
  _Files: `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py` _+16 more__
- **2026-09-10** [`b23db06769`](https://github.com/sgl-project/sglang/commit/b23db06769) [#38824](https://github.com/sgl-project/sglang/pull/38824)
  pyproject(xpu): drop human-eval git dep to unblock image build (#38824)
  _Files: `python/pyproject_xpu.toml`_
- **2026-09-10** [`13fb796c81`](https://github.com/sgl-project/sglang/commit/13fb796c81) [#38694](https://github.com/sgl-project/sglang/pull/38694)
  [AMD][CI] Drop the dead miles ROCm 7.0 nightly image build (#38694)
- **2026-09-10** [`f3152439d0`](https://github.com/sgl-project/sglang/commit/f3152439d0) [#38763](https://github.com/sgl-project/sglang/pull/38763)
  [AMD][CI] Publish ROCm 10 release images and kernel wheel (#38763)
  _Files: `.github/workflows/release-docker-amd.yml`, `.github/workflows/release-whl-kernel.yml`, `3rdparty/amd/wheel/sgl-kernel/build_rocm.sh`, `3rdparty/amd/wheel/sgl-kernel/rename_wheels_rocm.sh`_
- **2026-09-10** [`6f481ad0e3`](https://github.com/sgl-project/sglang/commit/6f481ad0e3) [#38735](https://github.com/sgl-project/sglang/pull/38735)
  [router] Raise chat body cap to 32 MB for multimodal payloads (#38735)
  _Files: `experimental/sgl-router/src/server/routes/chat.rs`_
- **2026-09-10** [`01ad27ecd9`](https://github.com/sgl-project/sglang/commit/01ad27ecd9) [#34767](https://github.com/sgl-project/sglang/pull/34767)
  [CPU] Fix native KV hash compilation in Xeon image (#34767)
  _Files: `docker/xeon.Dockerfile`_
- **2026-09-10** [`7f0285093e`](https://github.com/sgl-project/sglang/commit/7f0285093e) [#38656](https://github.com/sgl-project/sglang/pull/38656)
  [diffusion] feat: spill large tensors over shared memory like numpy arrays (#38656)
  _Files: `python/sglang/multimodal_gen/runtime/ipc_array.py`, `python/sglang/multimodal_gen/test/unit/test_ipc_array.py`_
- **2026-09-09** [`0027af2eac`](https://github.com/sgl-project/sglang/commit/0027af2eac) [#34722](https://github.com/sgl-project/sglang/pull/34722)
  [diffusion] [NPU] Optimize LTX-2/2.3 inference performance for NPU (#34722)
  _Files: `python/sglang/kernels/ops/diffusion/modulate/ltx2_ada_values_triton.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py`, `python/sglang/multimodal_gen/runtime/platforms/interface.py` _+1 more__
- **2026-09-09** [`a27be5ff62`](https://github.com/sgl-project/sglang/commit/a27be5ff62) [#38591](https://github.com/sgl-project/sglang/pull/38591)
  [Diffusion] Enable lossless BCG for FLUX.1-dev (#38591)
  _Files: `docs/cookbook/diffusion/FLUX/FLUX.mdx`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_bcg_padding.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-09-09** [`5998e9321c`](https://github.com/sgl-project/sglang/commit/5998e9321c) [#38329](https://github.com/sgl-project/sglang/pull/38329)
  [AMD][Fix] Fix regression in jit build error with FLUX.2-dev on gfx1250 (#38329)
  _Files: `python/sglang/kernels/ops/diffusion/norm/flux2_gated_resnorm_jit.py`_
- **2026-09-09** [`00a9028e87`](https://github.com/sgl-project/sglang/commit/00a9028e87) [#38535](https://github.com/sgl-project/sglang/pull/38535)
  [diffusion] feat: add explicit snapshot-offload component residency (#38535)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`, `python/sglang/multimodal_gen/runtime/loader/utils.py` _+16 more__
- **2026-09-09** [`0ee8e41a4e`](https://github.com/sgl-project/sglang/commit/0ee8e41a4e) [#38629](https://github.com/sgl-project/sglang/pull/38629)
  [diffusion] CI: don't fail the nightly when a perf dump is unreadable (#38629)
  _Files: `scripts/ci/utils/diffusion/run_comparison.py`_
- **2026-09-09** [`03d06a764e`](https://github.com/sgl-project/sglang/commit/03d06a764e) [#38534](https://github.com/sgl-project/sglang/pull/38534)
  [Docs] Add measured JoyEcho H200 residency and BCG recipe (#38534)
  _Files: `docs/cookbook/diffusion/JoyEcho/JoyEcho.mdx`_
- **2026-09-09** [`2952c8d5ea`](https://github.com/sgl-project/sglang/commit/2952c8d5ea) [#38530](https://github.com/sgl-project/sglang/pull/38530)
  [Diffusion] Fuse LongCat Image normalization and modulation (#38530)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/longcat_image.py`, `test/registered/kernel/diffusion/test_longcat_image_norm_modulate.py`_
- **2026-09-09** [`db1de6ff4c`](https://github.com/sgl-project/sglang/commit/db1de6ff4c) [#38182](https://github.com/sgl-project/sglang/pull/38182)
  [Diffusion] Keep the Wan VAE decoder channels_last and add a Triton NHWC nearest upsample (#38182)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/layout/nearest_upsample_nhwc_triton.py`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/existing-fast-paths.md` _+4 more__
- **2026-09-09** [`a67a31aa81`](https://github.com/sgl-project/sglang/commit/a67a31aa81) [#35492](https://github.com/sgl-project/sglang/pull/35492)
  [CPU] Support Qwen3.8 text+video: adding torchcodec, ffmpeg and removing pin_memory (#35492)
  _Files: `docker/xeon.Dockerfile`, `python/pyproject_cpu.toml`, `python/sglang/srt/multimodal/processors/qwen_vl.py`, `python/sglang/srt/utils/video_decoder.py`_
- **2026-09-08** [`15ff470472`](https://github.com/sgl-project/sglang/commit/15ff470472) [#38496](https://github.com/sgl-project/sglang/pull/38496)
  [diffusion] chore: key the VAE decode-dtype store by module layout (#38496)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/test/unit/test_vae_decoder_store.py`_
- **2026-09-08** [`554f817948`](https://github.com/sgl-project/sglang/commit/554f817948) [#38396](https://github.com/sgl-project/sglang/pull/38396)
  [Diffusion] Optimize LTX-2 QKNorm and split RoPE on Hopper (#38396)
  _Files: `python/sglang/kernels/kda_kernels/ltx2_qknorm_split_rope_jit.py`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/sites/ltx2_qknorm_split_rope_site.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py` _+3 more__
- **2026-09-08** [`88a9bfd1ff`](https://github.com/sgl-project/sglang/commit/88a9bfd1ff) [#38457](https://github.com/sgl-project/sglang/pull/38457)
  [diffusion] CI: add per-case timing tolerance for host-I/O-bound perf guards (#38457)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines/5090.json`, `python/sglang/multimodal_gen/test/server/test_server_common.py`, `python/sglang/multimodal_gen/test/server/test_server_utils.py`, `python/sglang/multimodal_gen/test/server/testcase_configs.py` _+1 more__
- **2026-09-08** [`775f17b07c`](https://github.com/sgl-project/sglang/commit/775f17b07c) [#38441](https://github.com/sgl-project/sglang/pull/38441)
  [diffusion] optimization: stream mapped weights on a shared host/device pool (#38441)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/runtime/loader/host_spill.py` _+15 more__
- **2026-09-08** [`b83a59835d`](https://github.com/sgl-project/sglang/commit/b83a59835d) [#38095](https://github.com/sgl-project/sglang/pull/38095)
  sglang-server remove opaque type (#38095)
  _Files: `rust/sglang-server/src/api_server/prefetch.rs`, `rust/sglang-server/src/message.rs`, `rust/sglang-server/src/message/multimodal.rs`, `rust/sglang-server/src/message/request.rs` _+3 more__
- **2026-09-08** [`2bf04f3a67`](https://github.com/sgl-project/sglang/commit/2bf04f3a67) [#35147](https://github.com/sgl-project/sglang/pull/35147)
  [Diffusion][CPU] Enable MiniMax-H3 on Xeon CPU (#35147)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/group_coordinator.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`_
- **2026-09-08** [`fba967ed9c`](https://github.com/sgl-project/sglang/commit/fba967ed9c) [#36026](https://github.com/sgl-project/sglang/pull/36026)
  [diffusion] Support diffusion decoder parallel tiling for LTX-2.5 (#36026)
  _Files: `docs/cookbook/diffusion/LTX/LTX2.5.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py`, `python/sglang/multimodal_gen/runtime/models/decoders/ltx_2_5_diffusion_decoder.py` _+6 more__
- **2026-09-08** [`c72cae201e`](https://github.com/sgl-project/sglang/commit/c72cae201e) [#37758](https://github.com/sgl-project/sglang/pull/37758)
  [NPU] Fix ViT graph key layout handling (#37758)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/vit_npu_graph_runner.py`, `python/sglang/srt/models/qwen3_vl.py`, `test/registered/unit/multimodal/test_vit_npu_graph_runner.py`_
- **2026-09-07** [`f3ccd1c0e4`](https://github.com/sgl-project/sglang/commit/f3ccd1c0e4) [#38335](https://github.com/sgl-project/sglang/pull/38335)
  [diffusion] CI: baseline the e2e of ten unguarded perf cases (#38335)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines/b200.json`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`_
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

## KV Cache / Memory  (37 commits)

- **2026-09-14** [`f81fbc749a`](https://github.com/sgl-project/sglang/commit/f81fbc749a) [#38941](https://github.com/sgl-project/sglang/pull/38941)
  [Fix] Merge adjacent KV-row frees so a mid-page split under DCP cannot double-free (#38941)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/common.py`, `test/registered/unit/mem_cache/test_free_kv_row_coalesce.py`_
- **2026-09-14** [`5200508b0f`](https://github.com/sgl-project/sglang/commit/5200508b0f) [#32888](https://github.com/sgl-project/sglang/pull/32888)
  [AMD][gfx95] Fill the chunked-prefill compute budget exactly (#32888)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_policy.py`_
- **2026-09-14** [`0d95a9c1ff`](https://github.com/sgl-project/sglang/commit/0d95a9c1ff) [#38925](https://github.com/sgl-project/sglang/pull/38925)
  [HiCache] Keep the file backend temp file name within NAME_MAX (#38925)
  _Files: `python/sglang/srt/mem_cache/hicache_storage.py`_
- **2026-09-13** [`ff228d11fe`](https://github.com/sgl-project/sglang/commit/ff228d11fe) [#38483](https://github.com/sgl-project/sglang/pull/38483)
  [HiCache] Release buffer prefetch anchor locks during storage cleanup (#38483)
  _Files: `python/sglang/srt/mem_cache/unified_cache/storage_attachment.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-13** [`7f1f8c706a`](https://github.com/sgl-project/sglang/commit/7f1f8c706a) [#35644](https://github.com/sgl-project/sglang/pull/35644)
  [mem_cache][10/N] refactor: drop the redundant _component suffix in unified_cache/components (#35644)
  _Files: `python/sglang/srt/hardware_backend/mlx/kv_cache/auxiliary_state.py`, `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/unified_cache/components/README.md`, `python/sglang/srt/mem_cache/unified_cache/components/__init__.py` _+14 more__
- **2026-09-13** [`7078e5ffbc`](https://github.com/sgl-project/sglang/commit/7078e5ffbc) [#38486](https://github.com/sgl-project/sglang/pull/38486)
  [HiCache] Publish a host store event for storage-prefetch refills (#38486)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `rust/sglang-radix-tree/src/tests/unified_tree_core.rs`, `rust/sglang-radix-tree/src/unified_tree_core.rs`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-13** [`a7cf4a6fbc`](https://github.com/sgl-project/sglang/commit/a7cf4a6fbc) [#37914](https://github.com/sgl-project/sglang/pull/37914)
  [Unified Cache][7/N]  Support MTP, EAGLE, and DSpark draft KV caches in the external linker (#37914)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/speculative/base_spec_worker.py`, `test/registered/unit/mem_cache/test_linker_pool_assembler.py`_
- **2026-09-13** [`34b2904741`](https://github.com/sgl-project/sglang/commit/34b2904741) [#39038](https://github.com/sgl-project/sglang/pull/39038)
  [Session] Work with PD and Fix empty continuations (#39038)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/session/session_controller.py`, `test/registered/unit/mem_cache/test_session_token_share_unit.py`_
- **2026-09-13** [`24b6c1c7f5`](https://github.com/sgl-project/sglang/commit/24b6c1c7f5) [#39120](https://github.com/sgl-project/sglang/pull/39120)
  Fix multimodal embedding cache retaining full batches through views (#39120)
  _Files: `python/sglang/srt/mem_cache/multimodal_cache.py`, `test/registered/chunked_prefill/test_mm_chunked_embedding_unit.py`_
- **2026-09-12** [`bd45cd50ca`](https://github.com/sgl-project/sglang/commit/bd45cd50ca) [#37584](https://github.com/sgl-project/sglang/pull/37584)
  [Unified Tree] Port SWA Branching-Point Caching to the Rust TreeCore (#37584)
  _Files: `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py` _+11 more__
- **2026-09-12** [`b9cb96496d`](https://github.com/sgl-project/sglang/commit/b9cb96496d) [#38482](https://github.com/sgl-project/sglang/pull/38482)
  [Unified Tree] Preserve aux LRU recency when splitting nodes (#38482)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `rust/sglang-radix-tree/src/components/swa.rs`, `rust/sglang-radix-tree/src/tests/unified_tree_core.rs` _+3 more__
- **2026-09-12** [`0a57403468`](https://github.com/sgl-project/sglang/commit/0a57403468) [#36411](https://github.com/sgl-project/sglang/pull/36411)
  [Perf] Optimize Qwen3-VL unique-image serving on H100 (#36411)
  _Files: `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/arg_groups/fields/mm.py`, `python/sglang/srt/arg_groups/fields/schedule.py`, `python/sglang/srt/arg_groups/memory_hook.py` _+26 more__
- **2026-09-11** [`4309c7ce19`](https://github.com/sgl-project/sglang/commit/4309c7ce19) [#39101](https://github.com/sgl-project/sglang/pull/39101)
  Fix stale DSV4 indexer metadata names in the TopK v2 dispatch test (#39101)
  _Files: `test/registered/unit/layers/test_dsv4_nonpaged_indexer.py`_
- **2026-09-11** [`822e73ccdd`](https://github.com/sgl-project/sglang/commit/822e73ccdd) [#38269](https://github.com/sgl-project/sglang/pull/38269)
  [Unified Cache][AMD] Support DeepSeek-V4 unified KV in direct external linkers (#38269)
  _Files: `python/sglang/srt/mem_cache/allocator/swa.py`, `python/sglang/srt/mem_cache/hybrid_cache/linker_pool_assembler.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py` _+3 more__
- **2026-09-11** [`69aa46b2fa`](https://github.com/sgl-project/sglang/commit/69aa46b2fa) [#39036](https://github.com/sgl-project/sglang/pull/39036)
  [ROCm] Raise HiCache JIT block quota for mapped-host throughput (#39036)
  _Files: `python/sglang/kernels/ops/kvcache/hicache.py`_
- **2026-09-11** [`a713349faf`](https://github.com/sgl-project/sglang/commit/a713349faf) [#38835](https://github.com/sgl-project/sglang/pull/38835)
  [HiCache] fix: preserve SWA host lock boundaries across splits (#38835)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py`_
- **2026-09-11** [`40a84d6dfc`](https://github.com/sgl-project/sglang/commit/40a84d6dfc) [#38356](https://github.com/sgl-project/sglang/pull/38356)
  [kv-shard 1/4] Logical-page placement with UnifiedRadixCache (#38356)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/allocation.py`, `python/sglang/srt/mem_cache/allocator/page_interleave.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py` _+7 more__
- **2026-09-10** [`19b83b4b9d`](https://github.com/sgl-project/sglang/commit/19b83b4b9d) [#38349](https://github.com/sgl-project/sglang/pull/38349)
  [Radix Cache] Fix PureSWA tail release without insertion (#38349)
  _Files: `python/sglang/srt/mem_cache/pure_swa_radix_cache.py`, `test/registered/unit/mem_cache/test_pure_swa_radix_cache.py`_
- **2026-09-10** [`cc7e43ad22`](https://github.com/sgl-project/sglang/commit/cc7e43ad22) [#38481](https://github.com/sgl-project/sglang/pull/38481)
  [HiCache] Account for newly pinned ancestors in load-back quota (#38481)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-09-10** [`908226fea2`](https://github.com/sgl-project/sglang/commit/908226fea2) [#37306](https://github.com/sgl-project/sglang/pull/37306)
  [Rust TreeCore] Support external cache linker (#37306)
  _Files: `python/sglang/srt/mem_cache/rust_tree_core/adapter.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core_interface.py` _+14 more__
- **2026-09-10** [`bd922bc39b`](https://github.com/sgl-project/sglang/commit/bd922bc39b) [#38672](https://github.com/sgl-project/sglang/pull/38672)
  [AMD][CI] Fix UMBP test buffer after MoRI upgrade (#38672)
  _Files: `test/registered/unit/mem_cache/test_umbp_store.py`_
- **2026-09-10** [`058cca0192`](https://github.com/sgl-project/sglang/commit/058cca0192) [#38350](https://github.com/sgl-project/sglang/pull/38350)
  [HiCache] Fix side pools to use resolved host allocator (#38350)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`_
- **2026-09-10** [`fd596a474c`](https://github.com/sgl-project/sglang/commit/fd596a474c) [#35051](https://github.com/sgl-project/sglang/pull/35051)
  [XPU][Fix] Pack device-pointer tables as uint64 to avoid 64-bit address overflow (#35051)
  _Files: `python/sglang/kernels/ops/mamba/mamba_state_scatter_triton.py`, `python/sglang/kernels/ops/memory/ptr_table.py`, `python/sglang/srt/mem_cache/mamba_slot_fused.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+7 more__
- **2026-09-09** [`bede776c2a`](https://github.com/sgl-project/sglang/commit/bede776c2a) [#36713](https://github.com/sgl-project/sglang/pull/36713)
  fix(unified-memory): evict Full KV for Mamba byte shortfalls (#36713)
  _Files: `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py`, `python/sglang/srt/mem_cache/allocator/unified_mamba.py`, `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py` _+4 more__
- **2026-09-09** [`78da625190`](https://github.com/sgl-project/sglang/commit/78da625190) [#38462](https://github.com/sgl-project/sglang/pull/38462)
  [mem_cache] skip duplicates host evict via environ (#38462)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`_
- **2026-09-09** [`eb42598bdd`](https://github.com/sgl-project/sglang/commit/eb42598bdd) [#38571](https://github.com/sgl-project/sglang/pull/38571)
  [AMD][DSV4] Skip the paged SWA page return under the per-request ring (#38571)
  _Files: `python/sglang/srt/mem_cache/allocator/swa.py`, `test/registered/unit/mem_cache/test_swa_ring_page_return.py`_
- **2026-09-09** [`7a464a7014`](https://github.com/sgl-project/sglang/commit/7a464a7014) [#37303](https://github.com/sgl-project/sglang/pull/37303)
  [Rust TreeCore] Harden runtime and CI parity (#37303)
  _Files: `.github/actions/download-rust-ext/action.yml`, `.github/workflows/_pr-test-rust-ext-build.yml`, `.github/workflows/seed-rust-ext-cache.yml`, `python/sglang/srt/rust_extensions/loader.py` _+18 more__
- **2026-09-08** [`ccfa120dae`](https://github.com/sgl-project/sglang/commit/ccfa120dae) [#38417](https://github.com/sgl-project/sglang/pull/38417)
  Fix DSA compression tail capacity for PD decode request slots (#38417)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`_
- **2026-09-08** [`da1c017ae8`](https://github.com/sgl-project/sglang/commit/da1c017ae8) [#38418](https://github.com/sgl-project/sglang/pull/38418)
  [CI] test: initialize disable_radix_cache in scheduler stub (#38418)
  _Files: `test/registered/unit/multimodal/test_gpu_feature_transport.py`_
- **2026-09-08** [`61d501427d`](https://github.com/sgl-project/sglang/commit/61d501427d) [#38313](https://github.com/sgl-project/sglang/pull/38313)
  fix: make dfs weight ordering iterative (#38313)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`_
- **2026-09-08** [`28ebede865`](https://github.com/sgl-project/sglang/commit/28ebede865) [#38159](https://github.com/sgl-project/sglang/pull/38159)
  [mem_cache] Free hybrid SWA pages by one representative per page on `page_size > 1` (#38159)
  _Files: `python/sglang/srt/mem_cache/allocator/hisparse.py`, `python/sglang/srt/mem_cache/allocator/paged.py`, `python/sglang/srt/mem_cache/allocator/swa.py`, `python/sglang/srt/mem_cache/allocator/token.py` _+8 more__
- **2026-09-08** [`e31e5319a0`](https://github.com/sgl-project/sglang/commit/e31e5319a0) [#37562](https://github.com/sgl-project/sglang/pull/37562)
  HiCache: Reduce the number of `all_reduce` in `check_hicache_events` for PP (#37562)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_hiradix_pp_sync_drain.py`_
- **2026-09-08** [`792543f98c`](https://github.com/sgl-project/sglang/commit/792543f98c) [#37143](https://github.com/sgl-project/sglang/pull/37143)
  [Scheduler] Make request-timeout aborts rank-consistent to fix TP collective hangs (#37143)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/request_receiver.py`, `test/registered/unit/managers/test_mm_shm_error_consensus.py`, `test/registered/unit/managers/test_pp_cp_rank_offsets.py` _+3 more__
- **2026-09-07** [`e9e9e37ddc`](https://github.com/sgl-project/sglang/commit/e9e9e37ddc) [#32759](https://github.com/sgl-project/sglang/pull/32759)
  [AMD] Restore SWA reprefill-tail on UnifiedRadixCache when HiCache is off (#32759)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-09-07** [`c5367fa964`](https://github.com/sgl-project/sglang/commit/c5367fa964) [#38315](https://github.com/sgl-project/sglang/pull/38315)
  [CI] Fix stale ServerArgs fake in chunked-SGMV LoRA test (#38315)
  _Files: `test/registered/kernels/ops/gemm/test_chunked_sgmv_cuda_graph.py`_
- **2026-09-07** [`6e312af8c2`](https://github.com/sgl-project/sglang/commit/6e312af8c2) [#38204](https://github.com/sgl-project/sglang/pull/38204)
  fix: collect prefix hash values iteratively (#38204)
  _Files: `python/sglang/srt/mem_cache/mamba_radix_cache.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`_
- **2026-09-07** [`f25848913d`](https://github.com/sgl-project/sglang/commit/f25848913d) [#38138](https://github.com/sgl-project/sglang/pull/38138)
  fix: preserve SWA host lock on node split (#38138)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py`_

## Prefill / Decode Disaggregation  (35 commits)

- **2026-09-14** [`95140a7b0c`](https://github.com/sgl-project/sglang/commit/95140a7b0c) [#39396](https://github.com/sgl-project/sglang/pull/39396)
  [docs] DeepSeek-V4: MI355X PD disaggregation recipes for all three strategies (#39396)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-14** [`4c71d14fba`](https://github.com/sgl-project/sglang/commit/4c71d14fba) [#39162](https://github.com/sgl-project/sglang/pull/39162)
  [HiCache][LoRA] Simplify decode offload hash inputs (#39162)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `test/registered/unit/disaggregation/test_specv2_kvcache_offloading.py`_
- **2026-09-14** [`bf9773e1da`](https://github.com/sgl-project/sglang/commit/bf9773e1da) [#37425](https://github.com/sgl-project/sglang/pull/37425)
  HiCache: Add @rank_consensus to various functions (#37425)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `python/sglang/test/server_fixtures/default_fixture.py`, `python/sglang/test/test_utils.py`, `test/registered/hicache/test_hicache_spec_file_storage.py` _+20 more__
- **2026-09-14** [`ca8ecc6a6f`](https://github.com/sgl-project/sglang/commit/ca8ecc6a6f) [#37382](https://github.com/sgl-project/sglang/pull/37382)
  [NPU] Support DSV4 host memory cache management (#37382)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/c128_sidecar_component.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_allocator.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_memory_pool.py`, `python/sglang/srt/managers/schedule_batch.py` _+8 more__
- **2026-09-14** [`2ec4bbcbd4`](https://github.com/sgl-project/sglang/commit/2ec4bbcbd4) [#37506](https://github.com/sgl-project/sglang/pull/37506)
  [unified-memory] PD disaggregation for every unified pool shape (#37506)
  _Files: `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py` _+14 more__
- **2026-09-13** [`6220f45d8e`](https://github.com/sgl-project/sglang/commit/6220f45d8e) [#36141](https://github.com/sgl-project/sglang/pull/36141)
  [PD] Add /v1/responses support to the HTTP PD router (#36141)
  _Files: `docs/docs/advanced_features/pd_disaggregation.mdx`, `sgl-model-gateway/src/routers/http/pd_router.rs`, `sgl-model-gateway/tests/routing/pd_routing_test.rs`_
- **2026-09-13** [`14a131ad5b`](https://github.com/sgl-project/sglang/commit/14a131ad5b) [#39122](https://github.com/sgl-project/sglang/pull/39122)
  [PD][OpenAI] Gate /v1/responses persistence behind --enable-response-store, default off (#39122)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/serving.py`, `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/arg_groups/resolution_hooks.py` _+4 more__
- **2026-09-13** [`fa663e7297`](https://github.com/sgl-project/sglang/commit/fa663e7297) [#39202](https://github.com/sgl-project/sglang/pull/39202)
  config: delete the redundant full stamp in initialize_model_parallel (#39202)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/srt/disaggregation/encoder/server.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/dp_attention.py` _+5 more__
- **2026-09-12** [`0b415fa573`](https://github.com/sgl-project/sglang/commit/0b415fa573) [#38577](https://github.com/sgl-project/sglang/pull/38577)
  [HiCache][LoRA] Isolate storage pages by extra key (#38577)
  _Files: `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/events.py` _+17 more__
- **2026-09-12** [`55e5e21c88`](https://github.com/sgl-project/sglang/commit/55e5e21c88) [#36651](https://github.com/sgl-project/sglang/pull/36651)
  [Qwen3.8-Next] Add PD state transfer for Flash Next (#36651)
  _Files: `python/sglang/srt/arg_groups/model_overrides/qwen4_exp.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+14 more__
- **2026-09-12** [`a984c78330`](https://github.com/sgl-project/sglang/commit/a984c78330) [#37565](https://github.com/sgl-project/sglang/pull/37565)
  [NPU] Support DFlash speculative decoding for MiMo-V2.5-Pro (mxfp4) (#37565)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py` _+11 more__
- **2026-09-12** [`a207786205`](https://github.com/sgl-project/sglang/commit/a207786205) [#37709](https://github.com/sgl-project/sglang/pull/37709)
  [PD] Transfer the DCP-replicated DSPARK draft KV in DCP1->DCP-N relayouts (#37709)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/dcp_pack.py`, `python/sglang/srt/disaggregation/common/utils.py` _+7 more__
- **2026-09-11** [`2c10f87991`](https://github.com/sgl-project/sglang/commit/2c10f87991) [#39100](https://github.com/sgl-project/sglang/pull/39100)
  [PD] Read nixl TransferInfo.is_dummy as a field in unit tests (#39100)
  _Files: `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-09-11** [`2a46cf2ca0`](https://github.com/sgl-project/sglang/commit/2a46cf2ca0) [#36612](https://github.com/sgl-project/sglang/pull/36612)
  [PD] Share the prefill->decode failure notification across backends (#36612)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py` _+2 more__
- **2026-09-11** [`f618022b73`](https://github.com/sgl-project/sglang/commit/f618022b73) [#39044](https://github.com/sgl-project/sglang/pull/39044)
  [AMD][CI] Temporarily pause MI355X disaggregated nightly (#39044)
  _Files: `.github/workflows/nightly-amd-mi355x-disagg.yml`_
- **2026-09-11** [`2018c64e22`](https://github.com/sgl-project/sglang/commit/2018c64e22) [#34977](https://github.com/sgl-project/sglang/pull/34977)
  [PD] Add is_dummy truth-table wire tests for mooncake and nixl (#34977)
  _Files: `test/registered/unit/disaggregation/test_disaggregation_wire.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-09-10** [`dc5f59c3a2`](https://github.com/sgl-project/sglang/commit/dc5f59c3a2) [#38947](https://github.com/sgl-project/sglang/pull/38947)
  [Refactor] Clarify DeepSeek V4 metadata names for V4.1 (#38947)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+12 more__
- **2026-09-10** [`fd7743e0e1`](https://github.com/sgl-project/sglang/commit/fd7743e0e1) [#36631](https://github.com/sgl-project/sglang/pull/36631)
  [Sampling] Support sampling masks with overlap scheduling (#36631)
  _Files: `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/pipeline.py`, `python/sglang/srt/arg_groups/validation_hook.py` _+20 more__
- **2026-09-10** [`f1a512c51c`](https://github.com/sgl-project/sglang/commit/f1a512c51c) [#38753](https://github.com/sgl-project/sglang/pull/38753)
  [Config] msgspec.Struct for the config tier (#38753)
  _Files: `python/sglang/benchmark/endpoint.py`, `python/sglang/lang/backend/runtime_endpoint.py`, `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/fields/__init__.py` _+40 more__
- **2026-09-10** [`ce555ed82a`](https://github.com/sgl-project/sglang/commit/ce555ed82a) [#38699](https://github.com/sgl-project/sglang/pull/38699)
  [diffusion] refactor: refactor utility ownership and document helper placement (#38699)
  _Files: `docs/cookbook/diffusion/SANA-WM/SANA-WM.mdx`, `docs/docs/sglang-diffusion/contributing.mdx`, `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/configs/models/vaes/base.py` _+92 more__
- **2026-09-09** [`beaf3d9252`](https://github.com/sgl-project/sglang/commit/beaf3d9252) [#36848](https://github.com/sgl-project/sglang/pull/36848)
  [HiCache] Replace skip_lock_node_ids with a segment lock protocol (#36848)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py` _+37 more__
- **2026-09-09** [`8ab9982851`](https://github.com/sgl-project/sglang/commit/8ab9982851) [#38174](https://github.com/sgl-project/sglang/pull/38174)
  [NPU]support mf device urma and host rdma trans type (#38174)
  _Files: `python/sglang/srt/disaggregation/ascend/transfer_engine.py`_
- **2026-09-08** [`559c7fa75b`](https://github.com/sgl-project/sglang/commit/559c7fa75b) [#38572](https://github.com/sgl-project/sglang/pull/38572)
  Revert "PD disaggregation, isolated transfer, prefill OOM fixed." (#38572)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-09-08** [`52fecfdf09`](https://github.com/sgl-project/sglang/commit/52fecfdf09) [#37500](https://github.com/sgl-project/sglang/pull/37500)
  support qwen 3.8 flash next (#37500)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/kernels/jit/csrc/attention/qsa_indexer.cuh`, `python/sglang/kernels/jit/csrc/elementwise/fast_topk.cuh`, `python/sglang/kernels/jit/csrc/elementwise/grouped_gemma_rmsnorm.cuh` _+87 more__
- **2026-09-08** [`a6b542813f`](https://github.com/sgl-project/sglang/commit/a6b542813f) [#32758](https://github.com/sgl-project/sglang/pull/32758)
  fix(glm-5.2-nvfp4): bound Mooncake synchronous transfer batches (#32758)
  _Files: `docs/docs/advanced_features/pd_disaggregation.mdx`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/environ.py`, `test/registered/unit/disaggregation/test_mooncake_transfer_batching.py` _+2 more__
- **2026-09-08** [`4df5df911b`](https://github.com/sgl-project/sglang/commit/4df5df911b) [#32911](https://github.com/sgl-project/sglang/pull/32911)
  [Scheduler] Add HRRN schedule policy to significantly reduce TTFT (#32911)
  _Files: `python/sglang/srt/arg_groups/fields/schedule.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py` _+4 more__
- **2026-09-08** [`f8f03910f2`](https://github.com/sgl-project/sglang/commit/f8f03910f2) [#32207](https://github.com/sgl-project/sglang/pull/32207)
  【NPU】Support EAGLE when PP enabled in prefill nodes (#32207)
  _Files: `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/prefill.py` _+8 more__
- **2026-09-08** [`5aab054ec8`](https://github.com/sgl-project/sglang/commit/5aab054ec8) [#36234](https://github.com/sgl-project/sglang/pull/36234)
  [rust-server] fix p/d bootstrap across dp listeners (#36234)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/rust_server/server.py` _+1 more__
- **2026-09-08** [`92371e9887`](https://github.com/sgl-project/sglang/commit/92371e9887) [#38094](https://github.com/sgl-project/sglang/pull/38094)
  PD disaggregation, isolated transfer, prefill OOM fixed. (#38094)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-09-08** [`b23d835048`](https://github.com/sgl-project/sglang/commit/b23d835048) [#38389](https://github.com/sgl-project/sglang/pull/38389)
  [Scheduler] Unify per-iteration request intake into ingest_requests() (#38389)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py` _+8 more__
- **2026-09-07** [`85d39401c8`](https://github.com/sgl-project/sglang/commit/85d39401c8) [#38293](https://github.com/sgl-project/sglang/pull/38293)
  [CP V1 Deprecation 3.5/5]  Deprecate HIP/NPU/MUSA prefill CP and remove legacy implementation (#38293)
  _Files: `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/cuda_graph_hook.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/field_order.py` _+43 more__
- **2026-09-07** [`570087ceda`](https://github.com/sgl-project/sglang/commit/570087ceda) [#38192](https://github.com/sgl-project/sglang/pull/38192)
  [AMD][DSV4] Reland unified-KV pool sizing and SWA ring accounting, fully gated (#38192)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/kernels/ops/attention/dsv4/attn.py`, `python/sglang/kernels/ops/attention/dsv4/compress.py`, `python/sglang/srt/disaggregation/decode.py` _+16 more__
- **2026-09-07** [`62a4a6ea0e`](https://github.com/sgl-project/sglang/commit/62a4a6ea0e) [#37373](https://github.com/sgl-project/sglang/pull/37373)
  [NPU] Add NPU arch35 support and enhance DSV4 processing in DeepSeek-V4 (#37373)
  _Files: `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/disaggregation/ascend/transfer_engine.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/environ.py` _+21 more__
- **2026-09-07** [`df623d3cbd`](https://github.com/sgl-project/sglang/commit/df623d3cbd) [#38195](https://github.com/sgl-project/sglang/pull/38195)
  fix: keep queued Mooncake linker loads after abort (#38195)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`_
- **2026-09-07** [`b99175dc7d`](https://github.com/sgl-project/sglang/commit/b99175dc7d) [#38049](https://github.com/sgl-project/sglang/pull/38049)
  [Config] Round 6.4: the runtime reads the bags, not the record (#38049)
  _Files: `python/sglang/srt/constrained/grammar_manager.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/encoder/grpc_server.py`, `python/sglang/srt/disaggregation/encoder/http_server.py` _+81 more__

## Other  (30 commits)

- **2026-09-14** [`7b4972a9cb`](https://github.com/sgl-project/sglang/commit/7b4972a9cb) [#39337](https://github.com/sgl-project/sglang/pull/39337)
  chore: add hzh0425 and xiezhq-hermann as Rust tree and HiSparse code owners (#39337)
  _Files: `.github/CODEOWNERS`_
- **2026-09-13** [`ddc1df1203`](https://github.com/sgl-project/sglang/commit/ddc1df1203) [#39259](https://github.com/sgl-project/sglang/pull/39259)
  fix(router): simplify bucket context limit check (#39259)
  _Files: `experimental/sgl-router/src/policies/buckets.rs`_
- **2026-09-13** [`14b647cf27`](https://github.com/sgl-project/sglang/commit/14b647cf27) [#38682](https://github.com/sgl-project/sglang/pull/38682)
  chore: add HiSparse coordinator and allocator code owners (#38682)
  _Files: `.github/CODEOWNERS`_
- **2026-09-13** [`7e3d18bbcc`](https://github.com/sgl-project/sglang/commit/7e3d18bbcc) [#39182](https://github.com/sgl-project/sglang/pull/39182)
  Add a provider hook for prefill-buffer ceilings (#39182)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/arg_groups/prefill_buffer_ceiling.py`, `python/sglang/srt/runtime_context.py`, `test/registered/unit/test_runtime_context.py`_
- **2026-09-13** [`18cc55dc0b`](https://github.com/sgl-project/sglang/commit/18cc55dc0b) [#39178](https://github.com/sgl-project/sglang/pull/39178)
  Expose a capacity check for graph-pool borrows (#39178)
  _Files: `python/sglang/srt/model_executor/runner_utils/pool.py`, `test/registered/unit/model_executor/runner_utils/test_graph_pool_borrow.py`_
- **2026-09-12** [`7ae4af8187`](https://github.com/sgl-project/sglang/commit/7ae4af8187) [#39177](https://github.com/sgl-project/sglang/pull/39177)
  Scope graph-pool borrowing to the runtime and reduce fragmentation (#39177)
  _Files: `python/sglang/srt/model_executor/runner_utils/pool.py`, `python/sglang/srt/runtime_context.py`, `test/registered/unit/model_executor/runner_utils/test_graph_pool_borrow.py`_
- **2026-09-12** [`25a5641cf2`](https://github.com/sgl-project/sglang/commit/25a5641cf2) [#39144](https://github.com/sgl-project/sglang/pull/39144)
  [Session + MM] Fix text positions in session continuations (#39144)
  _Files: `python/sglang/srt/model_executor/forward_batch_info.py`_
- **2026-09-12** [`c389dd0863`](https://github.com/sgl-project/sglang/commit/c389dd0863) [#38988](https://github.com/sgl-project/sglang/pull/38988)
  Fix RunAI object-storage checkpoint index filtering (#38988)
  _Files: `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/model_loader/weight_utils.py`, `test/registered/unit/model_loader/test_runai_model_streamer_loader.py`, `test/registered/unit/model_loader/test_weight_utils.py`_
- **2026-09-11** [`7d9c57da6e`](https://github.com/sgl-project/sglang/commit/7d9c57da6e) [#39035](https://github.com/sgl-project/sglang/pull/39035)
  [Session] Fix session idle timeout after rejected requests (#39035)
  _Files: `python/sglang/srt/session/session_controller.py`_
- **2026-09-11** [`593c7a900d`](https://github.com/sgl-project/sglang/commit/593c7a900d) [#38693](https://github.com/sgl-project/sglang/pull/38693)
  Add granite_thinking_parser reasoning parser for Granite 4.2 (#38693)
  _Files: `python/sglang/srt/parser/reasoning_parser.py`, `python/sglang/srt/parser/template_detection.py`, `test/registered/unit/parser/test_reasoning_parser.py`, `test/registered/unit/parser/test_template_manager.py`_
- **2026-09-11** [`e8a36d339c`](https://github.com/sgl-project/sglang/commit/e8a36d339c) [#38297](https://github.com/sgl-project/sglang/pull/38297)
  Auto-detect GLM-5.3 chat templates as glm45/glm47 parsers (#38297)
  _Files: `python/sglang/srt/parser/template_detection.py`, `test/registered/unit/parser/test_template_manager.py`_
- **2026-09-11** [`8e7deb329e`](https://github.com/sgl-project/sglang/commit/8e7deb329e) [#38814](https://github.com/sgl-project/sglang/pull/38814)
  [Router] Preserve global cache affinity with bucket routing (#38814)
  _Files: `experimental/sgl-router/src/policies/buckets.rs`, `experimental/sgl-router/src/policies/cache_aware.rs`, `experimental/sgl-router/src/policies/mod.rs`, `experimental/sgl-router/tests/component/policies/bucket_domains.rs` _+1 more__
- **2026-09-11** [`2adb2e8485`](https://github.com/sgl-project/sglang/commit/2adb2e8485) [#32093](https://github.com/sgl-project/sglang/pull/32093)
  [XPU] Adapt device agnostic API usage (#32093)
  _Files: `python/sglang/srt/debug_utils/dumper.py`, `test/manual/layers/test_fused_gate_sigmoid_mul_add.py`, `test/manual/layers/test_fused_sigmoid_mul.py`, `test/registered/debug_utils/test_dumper.py`_
- **2026-09-11** [`9df72e8f5a`](https://github.com/sgl-project/sglang/commit/9df72e8f5a) [#38730](https://github.com/sgl-project/sglang/pull/38730)
  Fix custom logit processor params when num_tokens_in_batch is used (#38730)
  _Files: `python/sglang/srt/layers/sampler.py`, `test/registered/unit/sampling/test_custom_logit_processor.py`_
- **2026-09-10** [`fa6e657b93`](https://github.com/sgl-project/sglang/commit/fa6e657b93) [#38834](https://github.com/sgl-project/sglang/pull/38834)
  [misc] Update CI permission (#38834)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-09-10** [`55b4f4f195`](https://github.com/sgl-project/sglang/commit/55b4f4f195) [#38336](https://github.com/sgl-project/sglang/pull/38336)
  [Test] Add offline Transformers loader compatibility checks (#38336)
  _Files: `test/registered/unit/utils/test_hf_transformers_loading.py`_
- **2026-09-10** [`6ab6df54b9`](https://github.com/sgl-project/sglang/commit/6ab6df54b9) [#36098](https://github.com/sgl-project/sglang/pull/36098)
  Add missing test dependencies to pyproject.toml variants (#36098)
  _Files: `python/pyproject_xpu.toml`_
- **2026-09-10** [`2f7393f0d2`](https://github.com/sgl-project/sglang/commit/2f7393f0d2) [#38732](https://github.com/sgl-project/sglang/pull/38732)
  [Simulator] Give the OFFLINE/BLOCKING comparison tolerances real headroom (#38732)
  _Files: `tools/sglang-simulator/test/test_simulation_offline_blocking.py`_
- **2026-09-09** [`76eea36e38`](https://github.com/sgl-project/sglang/commit/76eea36e38) [#38588](https://github.com/sgl-project/sglang/pull/38588)
  Cast fp32 routing weights to bf16 in the Kimi-K3 fused finalize (#38588)
  _Files: `python/sglang/srt/layers/k3_ar_fusion.py`_
- **2026-09-08** [`db272201a2`](https://github.com/sgl-project/sglang/commit/db272201a2) [#38375](https://github.com/sgl-project/sglang/pull/38375)
  [Config] Retire get_global_server_args, and clear the deprecated flags that have a replacement (#38375)
- **2026-09-08** [`325ab245a1`](https://github.com/sgl-project/sglang/commit/325ab245a1) [#37767](https://github.com/sgl-project/sglang/pull/37767)
  [DCP] Allow fi_a2a on single-node systems Blackwell without MNNVL fabric ( ex B200 B300) (#37767)
  _Files: `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py`, `python/sglang/srt/layers/dcp/comm.py`_
- **2026-09-08** [`73c4cdb795`](https://github.com/sgl-project/sglang/commit/73c4cdb795) [#38394](https://github.com/sgl-project/sglang/pull/38394)
  update codeowners (#38394)
  _Files: `.github/CODEOWNERS`_
- **2026-09-08** [`7d2d6624b1`](https://github.com/sgl-project/sglang/commit/7d2d6624b1) [#38125](https://github.com/sgl-project/sglang/pull/38125)
  [NPU] Enable L1 prefix cache for Kimi-K3 W4A8 accuracy test (gpqa) (#38125)
  _Files: `test/registered/npu/accuracy/kimi_k3/test_npu_kimi_k3_w4a8_32p_gpqa.py`_
- **2026-09-07** [`bf68369a18`](https://github.com/sgl-project/sglang/commit/bf68369a18) [#31415](https://github.com/sgl-project/sglang/pull/31415)
  [ray] Support Ray metric backend for engine metrics (#31415)
  _Files: `python/sglang/srt/observability/metrics_collector.py`, `python/sglang/srt/observability/ray_wrappers.py`, `python/sglang/srt/ray/engine.py`, `test/registered/unit/observability/test_ray_wrappers.py`_
- **2026-09-07** [`b5c9b68f03`](https://github.com/sgl-project/sglang/commit/b5c9b68f03) [#37743](https://github.com/sgl-project/sglang/pull/37743)
  [Kimi-K3] Recover the reply when the model skips the think channel (#37743)
  _Files: `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/parser/test_kimik3_reasoning_parser.py`_
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

## MoE / Expert Parallel  (30 commits)

- **2026-09-13** [`cebca698e2`](https://github.com/sgl-project/sglang/commit/cebca698e2) [#39126](https://github.com/sgl-project/sglang/pull/39126)
  [Qwen3.8] Enable NVIDIA NVFP4 on DGX Spark with file-backed PLE and PDL router fix (#39126)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/references/environment_variables.mdx`, `python/sglang/kernels/jit/csrc/moe/route_radix.cuh`, `python/sglang/kernels/ops/moe/moe_fused_gate.py` _+17 more__
- **2026-09-13** [`6d6d42d1c0`](https://github.com/sgl-project/sglang/commit/6d6d42d1c0) [#39136](https://github.com/sgl-project/sglang/pull/39136)
  [Fix] Preserve GLM tool argument types across JSON Schema unions (#39136)
  _Files: `python/sglang/srt/function_call/glm47_moe_detector.py`, `test/registered/unit/function_call/test_glm47_schema_types.py`_
- **2026-09-13** [`7763f666f3`](https://github.com/sgl-project/sglang/commit/7763f666f3) [#39245](https://github.com/sgl-project/sglang/pull/39245)
  Fix DeepGEMM release MegaMoE validation without RDMA (#39245)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-09-12** [`6657f7d844`](https://github.com/sgl-project/sglang/commit/6657f7d844) [#38328](https://github.com/sgl-project/sglang/pull/38328)
  [MoE][ROCm] Admit the unified Triton router on ROCm, including single-group routing (#38328)
  _Files: `python/sglang/kernels/ops/moe/moe_fused_gate.py`, `python/sglang/srt/layers/attention/wave_ops/decode_attention.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/kernel/moe/test_jit_grouped_topk.py`_
- **2026-09-12** [`ae1acf822d`](https://github.com/sgl-project/sglang/commit/ae1acf822d) [#37679](https://github.com/sgl-project/sglang/pull/37679)
  [GraniteMoE] Load split per-expert quantized MoE weights (#37679)
  _Files: `python/sglang/srt/models/granitemoe.py`, `test/registered/unit/models/test_granitemoe_split_expert_loading.py`_
- **2026-09-11** [`ec30f19e4a`](https://github.com/sgl-project/sglang/commit/ec30f19e4a) [#38578](https://github.com/sgl-project/sglang/pull/38578)
  [LoRA] Support MoE in full and breakable prefill CUDA graphs (#38578)
  _Files: `python/sglang/srt/lora/backend/base_backend.py`, `python/sglang/srt/lora/backend/chunked_backend.py`, `python/sglang/srt/lora/backend/triton_backend.py`, `python/sglang/srt/lora/layers.py` _+5 more__
- **2026-09-10** [`92dffebe16`](https://github.com/sgl-project/sglang/commit/92dffebe16) [#38775](https://github.com/sgl-project/sglang/pull/38775)
  [NPU] Set DEEPEP_HYBRID_DEPLOYMENT for new DeepEP tests; switch glm5_2 to w8a8; tune nightly timeouts (#38775)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_16p_gpqa.py`, `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py` _+3 more__
- **2026-09-10** [`dc2157dcd6`](https://github.com/sgl-project/sglang/commit/dc2157dcd6) [#38830](https://github.com/sgl-project/sglang/pull/38830)
  [JIT] Port the expert-pack MXFP4 kernels to load_jit and fix their launch limits (#38830)
  _Files: `python/sglang/kernels/jit/csrc/moe/expert_pack_mxfp4.cu`, `python/sglang/kernels/jit/csrc/moe/expert_pack_mxfp4.cuh`, `python/sglang/kernels/ops/moe/expert_pack_mxfp4.py`_
- **2026-09-10** [`1b77f498a0`](https://github.com/sgl-project/sglang/commit/1b77f498a0) [#31470](https://github.com/sgl-project/sglang/pull/31470)
  [NVIDIA] Support flashinfer Mega Moe (#31470)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/references/environment_variables.mdx`, `python/pyproject.toml`, `python/sglang/srt/arg_groups/choices.py` _+27 more__
- **2026-09-10** [`c0b790cf7f`](https://github.com/sgl-project/sglang/commit/c0b790cf7f) [#32114](https://github.com/sgl-project/sglang/pull/32114)
  Delete cutlass_mla, non-Marlin GPTQ, AWQ AOT kernel, and Dual Chunk Flash Attention (#32114)
  _Files: `.github/labeler.yml`, `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`, `docs/docs/advanced_features/attention_backend.mdx`, `docs/docs/advanced_features/quantization.mdx` _+67 more__
- **2026-09-10** [`7152c14384`](https://github.com/sgl-project/sglang/commit/7152c14384) [#34459](https://github.com/sgl-project/sglang/pull/34459)
  Fix DeepSeek-V4 routing: sqrtsoftplus underflow and unfloored renorm (#34459)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/hash_topk.cuh`, `python/sglang/kernels/jit/csrc/moe/moe_fused_gate.cuh`, `python/sglang/kernels/ops/moe/moe_fused_gate.py`, `python/sglang/srt/layers/moe/hash_topk.py`_
- **2026-09-09** [`7b791c9534`](https://github.com/sgl-project/sglang/commit/7b791c9534) [#37933](https://github.com/sgl-project/sglang/pull/37933)
  [Bugfix] Keep a shared MAX_LEN prefill CUDA graph bucket when the graph captures a DP gather (MegaMoE sparse-DP hang) (#37933)
  _Files: `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/runtime_context.py` _+1 more__
- **2026-09-09** [`2b1c4e4c85`](https://github.com/sgl-project/sglang/commit/2b1c4e4c85) [#38667](https://github.com/sgl-project/sglang/pull/38667)
  [NPU] Set DEEPEP_HYBRID_DEPLOYMENT=1 for collocated DeepEP test cases (#38667)
  _Files: `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_gpqa.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w4a8_16p_gpqa.py`, `test/registered/npu/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py`, `test/registered/npu/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_480b.py` _+10 more__
- **2026-09-09** [`72d5c5bb73`](https://github.com/sgl-project/sglang/commit/72d5c5bb73) [#38612](https://github.com/sgl-project/sglang/pull/38612)
  [Kimi-K3] Accept fp32 routing weights in the fused MoE finalize (#38612)
  _Files: `python/sglang/kernels/jit/csrc/kimi_k3/comm/ar_fusion.cuh`, `python/sglang/kernels/jit/csrc/moe/moe_finalize_fuse_shared.cu`, `python/sglang/kernels/jit/include/sgl_kernel/math.cuh`, `python/sglang/kernels/ops/kimi_k3/all_reduce.py` _+3 more__
- **2026-09-09** [`daf66f6670`](https://github.com/sgl-project/sglang/commit/daf66f6670) [#36606](https://github.com/sgl-project/sglang/pull/36606)
  [Diffusion][SenseNova] support SenseNova-U1.5-8B-MoT  (#36606)
  _Files: `docs/cookbook/diffusion/SenseNova/SenseNova-U1.5-8B-MoT.mdx`, `docs/cookbook/diffusion/intro.mdx`, `docs/docs.json`, `docs/src/snippets/diffusion/model-catalog.jsx` _+32 more__
- **2026-09-08** [`30e7a3072d`](https://github.com/sgl-project/sglang/commit/30e7a3072d) [#33631](https://github.com/sgl-project/sglang/pull/33631)
  Keep fp32 routing weights in the fp8 block-scale and bf16 trtllm MoE (#33631)
  _Files: `python/sglang/kernels/ops/moe/__init__.py`, `python/sglang/kernels/ops/moe/pack_topk_ids.py`, `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py` _+1 more__
- **2026-09-08** [`4c3d47f1df`](https://github.com/sgl-project/sglang/commit/4c3d47f1df) [#38456](https://github.com/sgl-project/sglang/pull/38456)
  [AMD] Copy MoE weight views before H2D in slow-loading nightlies (#38456)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`_
- **2026-09-08** [`91a45ea37e`](https://github.com/sgl-project/sglang/commit/91a45ea37e) [#30345](https://github.com/sgl-project/sglang/pull/30345)
  [Intel][XPU][LoRA] Enable LoRA on Intel XPU (#30345)
  _Files: `.github/workflows/pr-test-xpu.yml`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/layers/rotary_embedding/mrope.py` _+15 more__
- **2026-09-08** [`5aa913e156`](https://github.com/sgl-project/sglang/commit/5aa913e156) [#37133](https://github.com/sgl-project/sglang/pull/37133)
  [AMD][GLM-5.2] Keep GlmMoeDsa MoE e_score_correction_bias in fp32 (#37133)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/deepseek_v2.py`, `test/registered/unit/models/test_glmmoedsa_correction_bias_fp32.py`_
- **2026-09-08** [`f4bbf12423`](https://github.com/sgl-project/sglang/commit/f4bbf12423) [#38374](https://github.com/sgl-project/sglang/pull/38374)
  docs(cookbook): Qwen3.5 FP8 on B200/B300 — trtllm-gen MoE + symm mem (#38374)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-09-08** [`4dcecc7891`](https://github.com/sgl-project/sglang/commit/4dcecc7891) [#38381](https://github.com/sgl-project/sglang/pull/38381)
  Revert "[kernel] add fused silu mul quant fp8" (#38381)
  _Files: `python/sglang/kernels/aot/benchmark/bench_silu_quant_fp8.py`, `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `test/registered/kernels/ops/quantization/test_fused_silu_mul_quant_fp8.py`_
- **2026-09-07** [`dcebe8c473`](https://github.com/sgl-project/sglang/commit/dcebe8c473) [#38116](https://github.com/sgl-project/sglang/pull/38116)
  [Kernel] Add fused MoE Triton configs for Qwen3.8-Flash-Next FP8 on NVIDIA H200 NVL (TP2+EP2) (#38116)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=256,N=640,device_name=NVIDIA_H200_NVL,dtype=fp8_w8a8,block_shape=[128, 128].json`_
- **2026-09-07** [`c99d906eff`](https://github.com/sgl-project/sglang/commit/c99d906eff) [#33591](https://github.com/sgl-project/sglang/pull/33591)
  Drop the routing bias casts in flashinfer trtllm MoE (#33591)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`_
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

## CI / Build  (18 commits)

- **2026-09-13** [`a8b5616303`](https://github.com/sgl-project/sglang/commit/a8b5616303) [#39241](https://github.com/sgl-project/sglang/pull/39241)
  Fix DeepGEMM release dependencies and bound GPU validation (#39241)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-09-12** [`56a4f47ca6`](https://github.com/sgl-project/sglang/commit/56a4f47ca6) [#39195](https://github.com/sgl-project/sglang/pull/39195)
  [CI] Fix base-a wait for skipped CPU matrix (#39195)
  _Files: `.github/actions/wait-for-jobs/action.yml`_
- **2026-09-12** [`3bb2a5231a`](https://github.com/sgl-project/sglang/commit/3bb2a5231a) [#39194](https://github.com/sgl-project/sglang/pull/39194)
  [CI] Extend DeepGEMM SM90 test timeout to four hours (#39194)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-09-12** [`9c365e97b1`](https://github.com/sgl-project/sglang/commit/9c365e97b1) [#39163](https://github.com/sgl-project/sglang/pull/39163)
  [CI] Fix DeepGEMM sanitizer setup and Blackwell test timeouts (#39163)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-09-12** [`29cc9d2dc9`](https://github.com/sgl-project/sglang/commit/29cc9d2dc9) [#39152](https://github.com/sgl-project/sglang/pull/39152)
  [CI] Install elfutils headers for DeepGEMM wheel builds (#39152)
  _Files: `docker/sgl-deep-gemm.Dockerfile`_
- **2026-09-11** [`a4ff5634b8`](https://github.com/sgl-project/sglang/commit/a4ff5634b8) [#39077](https://github.com/sgl-project/sglang/pull/39077)
  [CI] Add CI permissions for PP contributor stepinto (#39077)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-09-11** [`0bae67648a`](https://github.com/sgl-project/sglang/commit/0bae67648a) [#38968](https://github.com/sgl-project/sglang/pull/38968)
  [NPU] Change npu.Dockerfile working directory to /sgl-workspace (#38968)
  _Files: `docker/npu.Dockerfile`_
- **2026-09-11** [`67d3a2ea57`](https://github.com/sgl-project/sglang/commit/67d3a2ea57) [#32382](https://github.com/sgl-project/sglang/pull/32382)
  [XPU] Make checkpoint_engine worker device-agnostic (#32382)
  _Files: `.github/workflows/pr-test-xpu.yml`, `docs/docs/advanced_features/checkpoint_engine.mdx`, `python/pyproject_xpu.toml`, `python/sglang/srt/checkpoint_engine/checkpoint_engine_worker.py` _+1 more__
- **2026-09-10** [`8022505705`](https://github.com/sgl-project/sglang/commit/8022505705) [#38842](https://github.com/sgl-project/sglang/pull/38842)
  Revert "[CI] Temporarily disable GB300 tests" (#38842)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/release-whl-deepgemm.yml`_
- **2026-09-10** [`a1ec35a330`](https://github.com/sgl-project/sglang/commit/a1ec35a330) [#38796](https://github.com/sgl-project/sglang/pull/38796)
  docker(xpu): install libssl-dev so JIT hicache_hash_cpp builds (#38796)
  _Files: `.github/workflows/pr-test-xpu.yml`, `docker/xpu.Dockerfile`_
- **2026-09-10** [`9a1b1d2d5e`](https://github.com/sgl-project/sglang/commit/9a1b1d2d5e) [#38665](https://github.com/sgl-project/sglang/pull/38665)
  docker(xpu): drop redundant setvars.sh from torch_memory_saver RUN (#38665)
  _Files: `docker/xpu.Dockerfile`_
- **2026-09-10** [`3700c4ee26`](https://github.com/sgl-project/sglang/commit/3700c4ee26) [#38770](https://github.com/sgl-project/sglang/pull/38770)
  [CI] Temporarily disable GB300 tests (#38770)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/release-whl-deepgemm.yml`_
- **2026-09-10** [`a7e00b7576`](https://github.com/sgl-project/sglang/commit/a7e00b7576) [#38736](https://github.com/sgl-project/sglang/pull/38736)
  [CI] Answer unrecognized slash commands instead of skipping silently (#38736)
  _Files: `.github/workflows/slash-command-handler.yml`, `docs/docs/developer_guide/contribution_guide.mdx`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-09-09** [`2948a62a6f`](https://github.com/sgl-project/sglang/commit/2948a62a6f) [#38734](https://github.com/sgl-project/sglang/pull/38734)
  [CI] Add /run-full-ci and /run-extra-ci slash commands (#38734)
  _Files: `.claude/skills/ci-workflow-guide/SKILL.md`, `.github/FOLDER_README.md`, `.github/workflows/slash-command-handler.yml`, `docs/docs/developer_guide/contribution_guide.mdx` _+1 more__
- **2026-09-09** [`07c7b2674d`](https://github.com/sgl-project/sglang/commit/07c7b2674d) [#38014](https://github.com/sgl-project/sglang/pull/38014)
  ci(xpu): merge stage-a+b into one job and trim main_package scope (#38014)
  _Files: `.github/workflows/pr-test-xpu.yml`, `.github/workflows/xpu-ci-job-monitor.yml`_
- **2026-09-09** [`32d7d943d1`](https://github.com/sgl-project/sglang/commit/32d7d943d1) [#38638](https://github.com/sgl-project/sglang/pull/38638)
  use private --shm-size instead of --ipc=host to stop /dev/shm leak (#38638)
  _Files: `.github/workflows/pr-test-xeon.yml`_
- **2026-09-08** [`b8a81f055d`](https://github.com/sgl-project/sglang/commit/b8a81f055d) [#38380](https://github.com/sgl-project/sglang/pull/38380)
  [CI] Replace the Lark `queue-digest` card with a daily `queue-timeline` chart (#38380)
  _Files: `.github/workflows/ci-lark-notify.yml`, `.github/workflows/runner-utilization.yml`, `scripts/ci/utils/runner_utilization_report.py`, `scripts/ci_monitor/README.md` _+1 more__
- **2026-09-07** [`62bca081a3`](https://github.com/sgl-project/sglang/commit/62bca081a3) [#38342](https://github.com/sgl-project/sglang/pull/38342)
  [CI] Fix request receiver EP scale joiner test patch (#38342)
  _Files: `test/registered/unit/managers/test_pp_cp_rank_offsets.py`_

## Quantization  (16 commits)

- **2026-09-14** [`242d8a70c0`](https://github.com/sgl-project/sglang/commit/242d8a70c0) [#39406](https://github.com/sgl-project/sglang/pull/39406)
  [AMD] GLM-5.2 MI355X MXFP4: bump image to 20260913, enable TOPK_V2 (#39406)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-09-14** [`a4781c9fe5`](https://github.com/sgl-project/sglang/commit/a4781c9fe5) [#37384](https://github.com/sgl-project/sglang/pull/37384)
  [NPU] Fix error due to missing parameter quant_linear passing (#37384)
  _Files: `python/sglang/srt/layers/quantization/modelslim/modelslim.py`_
- **2026-09-14** [`2f5cc8e33e`](https://github.com/sgl-project/sglang/commit/2f5cc8e33e) [#39358](https://github.com/sgl-project/sglang/pull/39358)
  [AMD] Align Qwen3.5 MI355X cookbook with AttnFP8-V2 and HiCache direct / page_first_direct (#39358)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-09-13** [`d6fabb74b4`](https://github.com/sgl-project/sglang/commit/d6fabb74b4) [#37564](https://github.com/sgl-project/sglang/pull/37564)
  [AMD][Fix] Fix aiter bpreshuffle GEMM for output sizes it cannot dispatch for qwen3.5 mxfp-attn-fp8-v2 TP4 (#37564)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w8a8_fp8.py`_
- **2026-09-12** [`288627e400`](https://github.com/sgl-project/sglang/commit/288627e400) [#39230](https://github.com/sgl-project/sglang/pull/39230)
  [AMD] Document GLM-5.2 MXFP4 recipe update on MI355X (#39230)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-09-12** [`7bc4eb3740`](https://github.com/sgl-project/sglang/commit/7bc4eb3740) [#39104](https://github.com/sgl-project/sglang/pull/39104)
  [AMD] Update MI355X MXFP4 HiCache defaults and quick-reduce quantization for Qwen3.5 cookbook (#39104)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-09-12** [`7c195b9151`](https://github.com/sgl-project/sglang/commit/7c195b9151) [#37254](https://github.com/sgl-project/sglang/pull/37254)
  [AMD] Fix Quark load of MiniMax-M3 MXFP4 index_qkv_proj (#37254)
  _Files: `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`, `test/registered/unit/layers/quantization/test_quark_utils.py`_
- **2026-09-12** [`dbd4302bbb`](https://github.com/sgl-project/sglang/commit/dbd4302bbb) [#39141](https://github.com/sgl-project/sglang/pull/39141)
  Keep NVFP4 blockscale swizzle padding on the input device (#39141)
  _Files: `python/sglang/srt/layers/quantization/utils.py`_
- **2026-09-11** [`6671cfc775`](https://github.com/sgl-project/sglang/commit/6671cfc775) [#34330](https://github.com/sgl-project/sglang/pull/34330)
  [AMD] Fix weight checking for AITER-shuffled block FP8 weights (#34330)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/utils/weight_checker.py`, `python/sglang/srt/utils/weight_checker_comparator.py` _+2 more__
- **2026-09-11** [`d7c284b894`](https://github.com/sgl-project/sglang/commit/d7c284b894) [#39106](https://github.com/sgl-project/sglang/pull/39106)
  [AMD] Use the triton DSA backend for GLM-5.2 MXFP4 on MI355X (#39106)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-09-11** [`2465ee3948`](https://github.com/sgl-project/sglang/commit/2465ee3948) [#38446](https://github.com/sgl-project/sglang/pull/38446)
  [AMD] Fix DeepSeek block-FP8 loading on gfx94x (#38446)
  _Files: `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`_
- **2026-09-10** [`a26273d668`](https://github.com/sgl-project/sglang/commit/a26273d668) [#38748](https://github.com/sgl-project/sglang/pull/38748)
  [AMD] Quantize the bf16 MTP draft experts online to MXFP4 for Qwen3.5 (#38748)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_loader/weight_utils.py`_
- **2026-09-10** [`613002281e`](https://github.com/sgl-project/sglang/commit/613002281e) [#38881](https://github.com/sgl-project/sglang/pull/38881)
  [CI] Drop the GPTQ dynamic-config test for the deleted non-Marlin kernel (#38881)
  _Files: `test/registered/quant/test_gptqmodel_dynamic.py`_
- **2026-09-09** [`a8e45f16cc`](https://github.com/sgl-project/sglang/commit/a8e45f16cc) [#38506](https://github.com/sgl-project/sglang/pull/38506)
  [diffusion] feat: support mixed INT8 embeddings and Comfy NVFP4 encoders for minimax-h3 (#38506)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/runtime/layers/quantization/comfy_int8.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/comfy_nvfp4.py` _+5 more__
- **2026-09-09** [`65400bb420`](https://github.com/sgl-project/sglang/commit/65400bb420) [#38455](https://github.com/sgl-project/sglang/pull/38455)
  [diffusion] model: support MiniMax-H3 singularity hybrid checkpoints (#38455)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/apps/webui/minimax_h3.py`, `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py` _+8 more__
- **2026-09-07** [`20ca564bf7`](https://github.com/sgl-project/sglang/commit/20ca564bf7) [#33624](https://github.com/sgl-project/sglang/pull/33624)
  Add zianglih as online NVFP4 and DSA Top-K code owner (#33624)
  _Files: `.github/CODEOWNERS`, `python/sglang/srt/layers/quantization/nvfp4_online.py`_

## Triton / Kernels  (15 commits)

- **2026-09-14** [`2123aca87e`](https://github.com/sgl-project/sglang/commit/2123aca87e) [#38409](https://github.com/sgl-project/sglang/pull/38409)
  [Fix] Wait for PDL before reading DeepSeek V4 K cache locations (#38409)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh`_
- **2026-09-14** [`96a95171c7`](https://github.com/sgl-project/sglang/commit/96a95171c7) [#39346](https://github.com/sgl-project/sglang/pull/39346)
  chore: bump sglang-kernel version to 0.4.7 (#39346)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`_
- **2026-09-12** [`2784a86062`](https://github.com/sgl-project/sglang/commit/2784a86062) [#39176](https://github.com/sgl-project/sglang/pull/39176)
  Reuse live CUDA graph executables during dedup registration (#39176)
  _Files: `python/sglang/srt/model_executor/runner_backend/cuda_graph_dedup_mixin.py`, `test/registered/kernel/cuda_graph/test_cuda_graph_dedup.py`_
- **2026-09-11** [`94ce940ff8`](https://github.com/sgl-project/sglang/commit/94ce940ff8) [#38992](https://github.com/sgl-project/sglang/pull/38992)
  [Bug] Include DSA variant in exact-bucket graph admission (#38992)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`_
- **2026-09-11** [`480b14edad`](https://github.com/sgl-project/sglang/commit/480b14edad) [#37394](https://github.com/sgl-project/sglang/pull/37394)
  [xpu] install xpu-kernel by released wheel (#37394)
  _Files: `python/pyproject_xpu.toml`_
- **2026-09-10** [`52c191da52`](https://github.com/sgl-project/sglang/commit/52c191da52) [#38404](https://github.com/sgl-project/sglang/pull/38404)
  [Deps] Retire the CUDA 12 lane (#38404)
  _Files: `.github/workflows/_docker-build-and-publish.yml`, `.github/workflows/patch-docker-dev.yml`, `.github/workflows/release-docker-dev.yml`, `.github/workflows/release-docker-runtime.yml` _+34 more__
- **2026-09-09** [`2092f6df05`](https://github.com/sgl-project/sglang/commit/2092f6df05) [#38688](https://github.com/sgl-project/sglang/pull/38688)
  [CI] Install helion 1.4.0 for the KDA Helion kernel tests (#38688)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-09-09** [`354ee46c26`](https://github.com/sgl-project/sglang/commit/354ee46c26) [#38722](https://github.com/sgl-project/sglang/pull/38722)
  Keep VMM capability votes on CPU (#38722)
  _Files: `python/sglang/srt/utils/cuda_vmm_utils.py`_
- **2026-09-09** [`dba34cc964`](https://github.com/sgl-project/sglang/commit/dba34cc964) [#38437](https://github.com/sgl-project/sglang/pull/38437)
  [NPU] Bump memfabric and sgl-kernel-npu versions in docs and pyproject_npu.toml (#38437)
  _Files: `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `python/pyproject_npu.toml`_
- **2026-09-09** [`d10ebdd0cb`](https://github.com/sgl-project/sglang/commit/d10ebdd0cb) [#38617](https://github.com/sgl-project/sglang/pull/38617)
  docker(xpu): unblock nightly build (setvars.sh + sgl-kernel rename) (#38617)
  _Files: `docker/xpu.Dockerfile`, `python/pyproject_xpu.toml`_
- **2026-09-09** [`35df2fecde`](https://github.com/sgl-project/sglang/commit/35df2fecde) [#38564](https://github.com/sgl-project/sglang/pull/38564)
  [Fix] Stamp sequence-parallel state on dummy forward batches (#38564)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `test/registered/unit/model_executor/test_prefill_cuda_graph_runner.py`_
- **2026-09-08** [`5177a3ec08`](https://github.com/sgl-project/sglang/commit/5177a3ec08) [#36557](https://github.com/sgl-project/sglang/pull/36557)
  MiniMax-M3: Triton split-K router GEMV with in-kernel fixup (#36557)
  _Files: `python/sglang/kernels/ops/gemm/router_gemv.py`, `python/sglang/srt/models/minimax_m3.py`_
- **2026-09-07** [`7d37b86ff2`](https://github.com/sgl-project/sglang/commit/7d37b86ff2) [#37886](https://github.com/sgl-project/sglang/pull/37886)
  Remove obsolete CUDA graph buffer population methods (#37886)
  _Files: `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_utils/buffers.py` _+1 more__
- **2026-09-07** [`39a80354aa`](https://github.com/sgl-project/sglang/commit/39a80354aa) [#36709](https://github.com/sgl-project/sglang/pull/36709)
  [MUSA] Add installation guide and Dockerfile (#36709)
  _Files: `docker/musa.Dockerfile`, `docs/docs/hardware-platforms/mthreads_gpu.mdx`, `docs/docs/hardware-platforms/overview.mdx`, `docs/index.mdx` _+2 more__
- **2026-09-07** [`707da81e84`](https://github.com/sgl-project/sglang/commit/707da81e84) [#35604](https://github.com/sgl-project/sglang/pull/35604)
  [CPU] Add native CPU kernel for MurmurHash32 (#35604)
  _Files: `python/sglang/kernels/aot/csrc/cpu/sampling.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/kernels/ops/sampling/murmur_hash.py`, `test/registered/cpu/test_sampling.py`_

## Tensor / Data Parallel  (13 commits)

- **2026-09-14** [`6388b6cfb1`](https://github.com/sgl-project/sglang/commit/6388b6cfb1) [#36472](https://github.com/sgl-project/sglang/pull/36472)
  [feat] Add base NpuSRTPlatform implementation (#36472)
  _Files: `python/sglang/srt/platforms/__init__.py`, `python/sglang/srt/platforms/npu.py`, `test/registered/unit/platforms/test_platform_interface.py`_
- **2026-09-13** [`fa260f26da`](https://github.com/sgl-project/sglang/commit/fa260f26da) [#39137](https://github.com/sgl-project/sglang/pull/39137)
  config: delete dead ensure_model_parallel_initialized (#39137)
  _Files: `python/sglang/srt/distributed/parallel_state.py`_
- **2026-09-13** [`6804eeaabe`](https://github.com/sgl-project/sglang/commit/6804eeaabe) [#39134](https://github.com/sgl-project/sglang/pull/39134)
  config: an out-of-tree replacement point for every resolution-pipeline step (#39134)
  _Files: `python/sglang/srt/arg_groups/memory_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/parallel_hook.py`, `python/sglang/srt/arg_groups/pipeline.py` _+4 more__
- **2026-09-12** [`6ba96d329f`](https://github.com/sgl-project/sglang/commit/6ba96d329f) [#39165](https://github.com/sgl-project/sglang/pull/39165)
  [DCP] Resolve --dcp-comm-backend to fi_a2a/a2a by default for every model (#39165)
  _Files: `docs/docs/advanced_features/dcp.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/parallel.py`, `python/sglang/srt/arg_groups/model_overrides/kimi_k3.py` _+6 more__
- **2026-09-11** [`45715e7f20`](https://github.com/sgl-project/sglang/commit/45715e7f20) [#38936](https://github.com/sgl-project/sglang/pull/38936)
  [Fix] Disable NCCL graph buffer registration for the TP LM-head all-to-all (pure-DP decode hang under request bursts) (#38936)
  _Files: `python/sglang/srt/arg_groups/parallel_hook.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-09-11** [`d006f40e24`](https://github.com/sgl-project/sglang/commit/d006f40e24) [#38767](https://github.com/sgl-project/sglang/pull/38767)
  [AMD][CI] Retire the ROCm 7.0 kernel wheel (#38767)
  _Files: `.github/workflows/release-whl-kernel.yml`, `3rdparty/amd/wheel/README.md`, `3rdparty/amd/wheel/sgl-kernel/build_rocm.sh`, `3rdparty/amd/wheel/sglang/pyproject.toml`_
- **2026-09-10** [`a63efd9056`](https://github.com/sgl-project/sglang/commit/a63efd9056) [#38558](https://github.com/sgl-project/sglang/pull/38558)
  [Spec] Support large MTP batches in short-convolution metadata (#38558)
  _Files: `python/sglang/srt/models/inkling_common/kernels/sconv.py`, `test/registered/kernels/ops/mamba/test_sconv_extend_metadata.py`_
- **2026-09-10** [`06dfe05d65`](https://github.com/sgl-project/sglang/commit/06dfe05d65) [#38801](https://github.com/sgl-project/sglang/pull/38801)
  [Deps] Raise smg-grpc-servicer floor to >=0.9.0 to unbreak SMG E2E CI (#38801)
  _Files: `.github/workflows/pr-test-rust.yml`, `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject.toml`, `python/pyproject_cpu.toml` _+3 more__
- **2026-09-09** [`51c8581a26`](https://github.com/sgl-project/sglang/commit/51c8581a26) [#37994](https://github.com/sgl-project/sglang/pull/37994)
  [Rust] Gate health on startup warmup completion (#37994)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/rust_server/config.py`, `rust/sglang-server/src/api_server/app.rs`, `rust/sglang-server/src/api_server/native_api.rs` _+2 more__
- **2026-09-09** [`95a88bfd69`](https://github.com/sgl-project/sglang/commit/95a88bfd69) [#38725](https://github.com/sgl-project/sglang/pull/38725)
  Relax GSM8K thresholds for the GLM-5.2 DSA-MTP variants (#38725)
  _Files: `python/sglang/test/server_fixtures/dsa_mtp_fixture.py`, `test/registered/e2e/models/test_dsa_glm52_nvfp4_dp_mtp.py`, `test/registered/e2e/models/test_dsa_glm52_nvfp4_tp_mtp.py`_
- **2026-09-07** [`755f97c622`](https://github.com/sgl-project/sglang/commit/755f97c622) [#38314](https://github.com/sgl-project/sglang/pull/38314)
  [CI] Fix the DSpark dp-tier unit test fixture after #34919 (#38314)
  _Files: `test/registered/spec/dspark/test_dspark_dp_tier.py`_
- **2026-09-07** [`98f69ccbf3`](https://github.com/sgl-project/sglang/commit/98f69ccbf3) [#38048](https://github.com/sgl-project/sglang/pull/38048)
  [Config] Round 6.3: the record remembers how it was asked for, and is sealed while resolution runs (#38048)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/grpc_bridge.py`, `python/sglang/srt/entrypoints/http_server.py` _+2 more__
- **2026-09-07** [`1c992bbd94`](https://github.com/sgl-project/sglang/commit/1c992bbd94) [#37179](https://github.com/sgl-project/sglang/pull/37179)
  [CPU] Fix shm allreduce collision and sglang-router import (#37179)
  _Files: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/utils/__init__.py`, `python/sglang/srt/utils/numa_utils.py`_

## Models  (12 commits)

- **2026-09-14** [`d5f1c593c1`](https://github.com/sgl-project/sglang/commit/d5f1c593c1) [#39047](https://github.com/sgl-project/sglang/pull/39047)
  [NPU] Remove temperature/top_p from Qwen3.5-397B-A17B perf test (#39047)
  _Files: `test/registered/npu/performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py`_
- **2026-09-11** [`df6424967a`](https://github.com/sgl-project/sglang/commit/df6424967a) [#38611](https://github.com/sgl-project/sglang/pull/38611)
  [docs] Add the NVIDIA NVFP4 export to the Qwen3.8-27B cookbook (#38611)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/_qwen38_mamba_ratio_calculator.jsx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b.jsx`_
- **2026-09-11** [`690428b470`](https://github.com/sgl-project/sglang/commit/690428b470) [#36278](https://github.com/sgl-project/sglang/pull/36278)
  [XPU] Add xpu forward in Gemma3RMSNorm & Add test and benchmark for Gemma3RMSNorm (#36278)
  _Files: `python/sglang/srt/layers/layernorm.py`, `test/manual/layers/test_layernorm.py`_
- **2026-09-10** [`4b7331fb77`](https://github.com/sgl-project/sglang/commit/4b7331fb77) [#38861](https://github.com/sgl-project/sglang/pull/38861)
  Make the remaining DeepSeek-V4.1 NVIDIA cells start (#38861)
  _Files: `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-09-10** [`a37ded1693`](https://github.com/sgl-project/sglang/commit/a37ded1693) [#38844](https://github.com/sgl-project/sglang/pull/38844)
  [Cookbook] DeepSeek-V4.1: add the HiCache L2 knob to the Playground (#38844)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-09-10** [`5caafd2118`](https://github.com/sgl-project/sglang/commit/5caafd2118) [#38839](https://github.com/sgl-project/sglang/pull/38839)
  Fix the DeepSeek-V4.1 reasoning example and mark the B300 cells verified (#38839)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4_1.jsx`_
- **2026-09-09** [`e54ff1efb9`](https://github.com/sgl-project/sglang/commit/e54ff1efb9) [#36230](https://github.com/sgl-project/sglang/pull/36230)
  [CP V1 Deprecation 5/5] Update prefill CP documentation (#36230)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.1.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx` _+3 more__
- **2026-09-08** [`5097f9ac95`](https://github.com/sgl-project/sglang/commit/5097f9ac95) [#37325](https://github.com/sgl-project/sglang/pull/37325)
  Disable Hopper GLM shared-expert fusion for modelopt_fp4 Marlin (#37325)
  _Files: `python/sglang/srt/models/deepseek_v2.py`, `test/registered/unit/models/test_shared_experts_fusion_gates.py`_
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

## ROCm / AMD  (9 commits)

- **2026-09-13** [`4358a1617c`](https://github.com/sgl-project/sglang/commit/4358a1617c) [#39324](https://github.com/sgl-project/sglang/pull/39324)
  chore: bump sgl-kernel version to 0.4.7 (#39324)
  _Files: `python/sglang/kernels/aot/pyproject.toml`, `python/sglang/kernels/aot/pyproject_cpu.toml`, `python/sglang/kernels/aot/pyproject_musa.toml`, `python/sglang/kernels/aot/pyproject_rocm.toml` _+1 more__
- **2026-09-13** [`ec5fba5777`](https://github.com/sgl-project/sglang/commit/ec5fba5777) [#39252](https://github.com/sgl-project/sglang/pull/39252)
  [AMD] Add dspark config and agentic workload section for deepseek-v4 model (#39252)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-12** [`fd32226706`](https://github.com/sgl-project/sglang/commit/fd32226706) [#38908](https://github.com/sgl-project/sglang/pull/38908)
  Fix gpt-oss RunAI streamer weight ownership (#38908)
  _Files: `python/sglang/srt/models/gpt_oss.py`, `test/registered/unit/models/test_gpt_oss_runai_ownership.py`_
- **2026-09-10** [`c415f977b8`](https://github.com/sgl-project/sglang/commit/c415f977b8) [#38677](https://github.com/sgl-project/sglang/pull/38677)
  [AMD] Update v4 args for agentic workload (#38677)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-09-10** [`106cc561f9`](https://github.com/sgl-project/sglang/commit/106cc561f9) [#37495](https://github.com/sgl-project/sglang/pull/37495)
  [AMD] ci: move the miles nightlies from rocm700 to rocm10 (#37495)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm10.yml`, `.github/workflows/release-docker-amd-miles-rocm10-nightly.yml`_
- **2026-09-09** [`708f51e44b`](https://github.com/sgl-project/sglang/commit/708f51e44b) [#38659](https://github.com/sgl-project/sglang/pull/38659)
  [AMD][CI] Make ROCm 10 the Default for AMD PR and Nightly Tests (#38659)
  _Files: `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/bot-bump-sglang-version.yml`, `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/pr-states.yml` _+4 more__
- **2026-09-08** [`80e9a4ec74`](https://github.com/sgl-project/sglang/commit/80e9a4ec74) [#38411](https://github.com/sgl-project/sglang/pull/38411)
  [AMD] [Docker] Update MoRI to v1.2.3 (#38411)
  _Files: `docker/rocm.Dockerfile`_
- **2026-09-07** [`503511c963`](https://github.com/sgl-project/sglang/commit/503511c963) [#38256](https://github.com/sgl-project/sglang/pull/38256)
  [AMD] Cherry-pick aiter commit for dsv4 a8w8 bpreshuffle gemm config (#38256)
  _Files: `docker/rocm.Dockerfile`_
- **2026-09-07** [`b9b39f222d`](https://github.com/sgl-project/sglang/commit/b9b39f222d) [#37784](https://github.com/sgl-project/sglang/pull/37784)
  [AMD] Update ROCm AITER pin to 4ad9983 (#37784)
  _Files: `docker/rocm.Dockerfile`_

## Scheduler / Batching  (6 commits)

- **2026-09-13** [`206034e520`](https://github.com/sgl-project/sglang/commit/206034e520) [#39180](https://github.com/sgl-project/sglang/pull/39180)
  Keep graph-pool borrows on their allocation stream (#39180)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/runner_utils/pool.py`, `test/registered/unit/model_executor/model_runner_components/test_startup_weight_load.py`, `test/registered/unit/model_executor/runner_utils/test_graph_pool_borrow.py`_
- **2026-09-10** [`203d7e812c`](https://github.com/sgl-project/sglang/commit/203d7e812c) [#38596](https://github.com/sgl-project/sglang/pull/38596)
  Fix KV-canary workspace accounting after graph capture (#38596)
  _Files: `python/sglang/kernels/ops/kv_canary/verify.py`, `python/sglang/kernels/ops/kv_canary/write.py`, `python/sglang/srt/kv_canary/capacities.py`, `python/sglang/srt/kv_canary/expected_inputs.py` _+8 more__
- **2026-09-10** [`42bbaac259`](https://github.com/sgl-project/sglang/commit/42bbaac259) [#38566](https://github.com/sgl-project/sglang/pull/38566)
  [metrics] Report logical prefill token counts (#38566)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `test/registered/unit/managers/test_prefill_adder.py`_
- **2026-09-10** [`334e94d8ac`](https://github.com/sgl-project/sglang/commit/334e94d8ac) [#38249](https://github.com/sgl-project/sglang/pull/38249)
  [NPU] fix pp 2 hang on npu (#38249)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`_
- **2026-09-08** [`beecfda314`](https://github.com/sgl-project/sglang/commit/beecfda314) [#37789](https://github.com/sgl-project/sglang/pull/37789)
  [observability] Fix missing e2e/decode/inference latency span attributes (#37789)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/observability/req_time_stats.py`, `test/registered/unit/observability/test_req_time_stats.py`_
- **2026-09-07** [`a88e852fab`](https://github.com/sgl-project/sglang/commit/a88e852fab) [#38279](https://github.com/sgl-project/sglang/pull/38279)
  [Sampling] Allow sampling-mask replay with DisallowedTokensLogitsProcessor (#38279)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/sampling/custom_logit_processor.py`, `test/registered/sampling/test_sampling_mask.py`, `test/registered/unit/managers/test_sampling_mask_validation.py`_

## LoRA  (5 commits)

- **2026-09-12** [`925e684a88`](https://github.com/sgl-project/sglang/commit/925e684a88) [#38690](https://github.com/sgl-project/sglang/pull/38690)
  [Feat][Responses API] Support custom tools, encrypted reasoning replay, developer tier and model validation (#38690)
  _Files: `python/sglang/srt/entrypoints/harmony_utils.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/responses_adapters.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py` _+4 more__
- **2026-09-11** [`b3dc0388ed`](https://github.com/sgl-project/sglang/commit/b3dc0388ed) [#38791](https://github.com/sgl-project/sglang/pull/38791)
  test(lora): enable ROCm logprob accuracy coverage (#38791)
  _Files: `test/registered/lora/test_lora_gpt_oss_20b_logprob_diff.py`, `test/registered/lora/test_lora_qwen3_8b_logprob_diff.py`_
- **2026-09-10** [`53dc77ff4e`](https://github.com/sgl-project/sglang/commit/53dc77ff4e) [#38752](https://github.com/sgl-project/sglang/pull/38752)
  [Config] One writer for the declaration stash; no exception to the write seal (#38752)
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/arg_groups/lora_hook.py`, `python/sglang/srt/arg_groups/overrides.py` _+15 more__
- **2026-09-08** [`2358916d5a`](https://github.com/sgl-project/sglang/commit/2358916d5a) [#29935](https://github.com/sgl-project/sglang/pull/29935)
  [Feature][Intel XPU] Add memory saver support for Intel XPU via upstream torch_memory_saver (#29935)
  _Files: `docker/xpu.Dockerfile`, `docs/docs/hardware-platforms/xpu.mdx`, `python/sglang/srt/utils/torch_memory_saver_adapter.py`, `test/registered/xpu/test_xpu_memory_saver.py`_
- **2026-09-07** [`ed82def55f`](https://github.com/sgl-project/sglang/commit/ed82def55f) [#38047](https://github.com/sgl-project/sglang/pull/38047)
  [Config] Round 6.2: the field declarations move to their namespaces, and the record is assembled from them (#38047)
  _Files: `python/sglang/srt/arg_groups/arg_utils.py`, `python/sglang/srt/arg_groups/choices.py`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/__init__.py` _+14 more__

## Docs / Examples  (4 commits)

- **2026-09-14** [`f539c1fc65`](https://github.com/sgl-project/sglang/commit/f539c1fc65) [#38737](https://github.com/sgl-project/sglang/pull/38737)
  [sgl-router] Stream outcome observability for 2xx SSE streams (#38737)
  _Files: `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/src/proxy/mod.rs`, `experimental/sgl-router/src/proxy/sse.rs`, `experimental/sgl-router/src/server/metrics.rs` _+2 more__
- **2026-09-12** [`0d08668821`](https://github.com/sgl-project/sglang/commit/0d08668821) [#39190](https://github.com/sgl-project/sglang/pull/39190)
  [Cookbook] Kimi-K3: keep DCP under HiCache L1+L2 with DSPARK (#39190)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`, `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-09-10** [`887c401e15`](https://github.com/sgl-project/sglang/commit/887c401e15) [#36773](https://github.com/sgl-project/sglang/pull/36773)
  docs: sync LMSYS SGLang blog cards (#36773)
  _Files: `docs/index.mdx`_
- **2026-09-07** [`e4008de757`](https://github.com/sgl-project/sglang/commit/e4008de757) [#38295](https://github.com/sgl-project/sglang/pull/38295)
  Add MiniCPM5-2B cookbook (#38295)
  _Files: `docs/cookbook/autoregressive/OpenBMB/MiniCPM-V-4_6.mdx`, `docs/cookbook/autoregressive/OpenBMB/MiniCPM5-2B.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__

## Serving / API  (3 commits)

- **2026-09-12** [`981b947568`](https://github.com/sgl-project/sglang/commit/981b947568) [#39105](https://github.com/sgl-project/sglang/pull/39105)
  [Fix] Seed raw tokenizer_path for smg-grpc-servicer in gRPC mode (#39105)
  _Files: `.github/workflows/pr-test-rust.yml`, `python/sglang/launch_server.py`, `sgl-model-gateway/e2e_test/embeddings/test_correctness.py`_
- **2026-09-11** [`f69d6fc28a`](https://github.com/sgl-project/sglang/commit/f69d6fc28a) [#35503](https://github.com/sgl-project/sglang/pull/35503)
  [OpenAI] Propagate PD routing metadata through /v1/responses (#35503)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py`, `test/registered/unit/entrypoints/openai/test_responses_protocol.py`, `test/registered/unit/entrypoints/openai/test_serving_responses.py`_
- **2026-09-11** [`ad7f57c9ea`](https://github.com/sgl-project/sglang/commit/ad7f57c9ea) [#35486](https://github.com/sgl-project/sglang/pull/35486)
  [Responses] Fix empty-prompt routing for token-first chat encoders (kimi_k3, inkling) (#35486)
  _Files: `python/sglang/srt/entrypoints/openai/chat_encoding.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py`, `test/registered/unit/entrypoints/openai/test_serving_responses.py`_

## Speculative Decoding  (3 commits)

- **2026-09-09** [`6c1d0b1b29`](https://github.com/sgl-project/sglang/commit/6c1d0b1b29) [#38041](https://github.com/sgl-project/sglang/pull/38041)
  Revert "[Spec] Publish the final multi-layer EAGLE shared-read event" (#38041)
  _Files: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`, `test/registered/unit/spec/test_multi_layer_eagle_shared_read_event.py`_
- **2026-09-08** [`dfd9b5c2a4`](https://github.com/sgl-project/sglang/commit/dfd9b5c2a4) [#32495](https://github.com/sgl-project/sglang/pull/32495)
  [NPU] Enable non-greedy MTP sampling (#32495)
  _Files: `docs/docs/hardware-platforms/ascend-npus/optimization/parameter_tuning.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `python/sglang/srt/speculative/eagle_utils.py`_
- **2026-09-07** [`8392c36bce`](https://github.com/sgl-project/sglang/commit/8392c36bce) [#37165](https://github.com/sgl-project/sglang/pull/37165)
  [Bugfix][Mamba] Clear deferred init metadata before speculative decode (#37165)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_schedule_batch_prepare_for_decode.py`_

## Structured Output  (2 commits)

- **2026-09-13** [`d24eacaecd`](https://github.com/sgl-project/sglang/commit/d24eacaecd) [#37015](https://github.com/sgl-project/sglang/pull/37015)
  [Test] Add unit test for muse_glimmer_format (#37015)
  _Files: `test/registered/unit/function_call/test_muse_glimmer_format.py`_
- **2026-09-10** [`026e61bd94`](https://github.com/sgl-project/sglang/commit/026e61bd94) [#38581](https://github.com/sgl-project/sglang/pull/38581)
  [AMD] Restore AMD CI registrations dropped by #37436 (#38581)
  _Files: `test/registered/debug_utils/test_tensor_dump_forward_hook.py`, `test/registered/observability/test_tracing.py`, `test/registered/openai_server/function_call/test_anthropic_tool_use.py`, `test/registered/openai_server/function_call/test_openai_function_calling.py` _+1 more__

---
_Generated 2026-09-14 15:00 UTC_