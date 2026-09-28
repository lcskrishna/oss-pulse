# vllm-project/vllm — Weekly Change Report
**Period:** 2026-09-21 → 2026-09-28  |  **Total commits:** 409

## ✨ New Features This Week

- **2026-09-28** [#57766](https://github.com/vllm-project/vllm/pull/57766) — [LoRA] Support variable num_labels for sequence classification (#57766)
- **2026-09-28** [#54956](https://github.com/vllm-project/vllm/pull/54956) — [ROCm][Perf] Kimi-K3 Enable sharded latent MoE up-projection under EP (#54956)
- **2026-09-28** [#58693](https://github.com/vllm-project/vllm/pull/58693) — [CPU] Add video inferencing via torchcodec on s390x (#58693)
- **2026-09-28** [#54628](https://github.com/vllm-project/vllm/pull/54628) — [Benchmark] Add Responses API backend to vllm bench serve (#54628)
- **2026-09-28** [#58673](https://github.com/vllm-project/vllm/pull/58673) — [Minimax-M3] Add Encoder CUDA graph support (#58673)
- **2026-09-28** [#58884](https://github.com/vllm-project/vllm/pull/58884) — [Model] Enable LoRA support for RobertaForSequenceClassification (#58884)
- **2026-09-28** [#58515](https://github.com/vllm-project/vllm/pull/58515) — [CPU] Build CPU wheels on Ubuntu 22.04 with AMX-FP8 support (#58515)
- **2026-09-27** [#58552](https://github.com/vllm-project/vllm/pull/58552) — [Fast Start] Add `/health` endpoint for the weight cache daemon (#58552)
- **2026-09-27** [#57407](https://github.com/vllm-project/vllm/pull/57407) — [ROCm][Perf] Enable layer-aware CSA2 multi-stream overlap for DeepSeek-V4.1-Flash (#57407)
- **2026-09-27** [#49300](https://github.com/vllm-project/vllm/pull/49300) — [mooncake] support CUSTOM_MEM_POOL in vllm (#49300)
- _…and 55 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-28** [`b0d2b854f6`](https://github.com/vllm-project/vllm/commit/b0d2b854f6) [#59056](https://github.com/vllm-project/vllm/pull/59056) — [ROCm]Keep LMCache OpenTelemetry on the image's 1.40 stack (#59056)
- **2026-09-28** [`6b24bd8e75`](https://github.com/vllm-project/vllm/commit/6b24bd8e75) [#58208](https://github.com/vllm-project/vllm/pull/58208) — [ROCm][Perf] Replace torch.topk in DSA candidate block selection (#58208)
- **2026-09-28** [`a7ff44355c`](https://github.com/vllm-project/vllm/commit/a7ff44355c) [#54956](https://github.com/vllm-project/vllm/pull/54956) — [ROCm][Perf] Kimi-K3 Enable sharded latent MoE up-projection under EP (#54956)
- **2026-09-28** [`7ba3df63cb`](https://github.com/vllm-project/vllm/commit/7ba3df63cb) [#58983](https://github.com/vllm-project/vllm/pull/58983) — [ROCm][Refactor] Move DeepSeek-V4/V4.1 multi-stream overlap gate to ROCm platform (#58983)
- **2026-09-28** [`20b52e9f5b`](https://github.com/vllm-project/vllm/commit/20b52e9f5b) [#58114](https://github.com/vllm-project/vllm/pull/58114) — [Perf][Qwen3.8] Reduce PLE metadata construction overhead (#58114)
- **2026-09-28** [`f6877f563c`](https://github.com/vllm-project/vllm/commit/f6877f563c) [#57568](https://github.com/vllm-project/vllm/pull/57568) — [Bugfix][Spec Decode] Implement get_top_tokens() on the ROCm DeepSeek V4 MTP drafter (#57568)
- **2026-09-28** [`252279314b`](https://github.com/vllm-project/vllm/commit/252279314b) [#58652](https://github.com/vllm-project/vllm/pull/58652) — Revert "[CI] Shard (H200 MIG 35GB / MI355 DPX) Entrypoints Integration (Pooling) into named jobs (#58652)" (#59011)
- **2026-09-28** [`66d2d4b2e7`](https://github.com/vllm-project/vllm/commit/66d2d4b2e7) [#58451](https://github.com/vllm-project/vllm/pull/58451) — [CI] Split Dynamic Shapes out of (H200 MIG 35GB) PyTorch Compilation + (MI300) mirror (#58451)
- **2026-09-28** [`413ae4b167`](https://github.com/vllm-project/vllm/commit/413ae4b167) [#58652](https://github.com/vllm-project/vllm/pull/58652) — [CI] Shard (H200 MIG 35GB / MI355 DPX) Entrypoints Integration (Pooling) into named jobs (#58652)
- **2026-09-28** [`4694145045`](https://github.com/vllm-project/vllm/commit/4694145045) [#58646](https://github.com/vllm-project/vllm/pull/58646) — [Skills] Update kernel-microbenchmark to include ROCm (#58646)
- **2026-09-28** [`55de40a2fc`](https://github.com/vllm-project/vllm/commit/55de40a2fc) [#58673](https://github.com/vllm-project/vllm/pull/58673) — [Minimax-M3] Add Encoder CUDA graph support (#58673)
- **2026-09-28** [`77fbd9e225`](https://github.com/vllm-project/vllm/commit/77fbd9e225) [#58945](https://github.com/vllm-project/vllm/pull/58945) — [Test][ROCm] Stabilize the mixed OLMoE LoRA test (#58945)
- **2026-09-28** [`31afa4f1bb`](https://github.com/vllm-project/vllm/commit/31afa4f1bb) [#58867](https://github.com/vllm-project/vllm/pull/58867) — [ROCm] Bump AITER to v0.1.23 (#58867)
- **2026-09-27** [`73859fec58`](https://github.com/vllm-project/vllm/commit/73859fec58) [#55128](https://github.com/vllm-project/vllm/pull/55128) — [Frontend] Switch Python Harmony dependency to oss-harmony (#55128)
- **2026-09-27** [`187c81b32d`](https://github.com/vllm-project/vllm/commit/187c81b32d) [#58923](https://github.com/vllm-project/vllm/pull/58923) — [ROCm][Bugfix] Fall back to default GEMM for CPU tensors on ROCm builds (#58923)
- **2026-09-27** [`44af287ebe`](https://github.com/vllm-project/vllm/commit/44af287ebe) [#57407](https://github.com/vllm-project/vllm/pull/57407) — [ROCm][Perf] Enable layer-aware CSA2 multi-stream overlap for DeepSeek-V4.1-Flash (#57407)
- **2026-09-27** [`3137ff0773`](https://github.com/vllm-project/vllm/commit/3137ff0773) [#58201](https://github.com/vllm-project/vllm/pull/58201) — [ROCm][Kimi-K3] Make VLLM_ROCM_USE_AITER_MOE_SITUV2 select a4w4/a8w4/a16w4 (#58201)
- **2026-09-26** [`a4eb3f25d6`](https://github.com/vllm-project/vllm/commit/a4eb3f25d6) [#57263](https://github.com/vllm-project/vllm/pull/57263) — [Spec Decode] Enable Gemma4 DSpark adaptive verification with FlashInfer (#57263)
- **2026-09-26** [`5840d95284`](https://github.com/vllm-project/vllm/commit/5840d95284) [#57071](https://github.com/vllm-project/vllm/pull/57071) — [Bugfix][ROCm] AMD-Quark mixed-precision DeepSeek-V4.1 support (#57071)
- **2026-09-26** [`da1aaec31f`](https://github.com/vllm-project/vllm/commit/da1aaec31f) [#57054](https://github.com/vllm-project/vllm/pull/57054) — [CI] Split (H200 MIG/MI300) Basic Correctness into named jobs (#57054)
- **2026-09-25** [`e440b75bb6`](https://github.com/vllm-project/vllm/commit/e440b75bb6) [#50605](https://github.com/vllm-project/vllm/pull/50605) — [ROCm] Bump torch 2.13, triton 3.8, torchaudio, torchvision (#50605)
- **2026-09-25** [`31cc226401`](https://github.com/vllm-project/vllm/commit/31cc226401) [#58717](https://github.com/vllm-project/vllm/pull/58717) — [ROCm][CI] Run the MLA attention+quant fusion test on ROCm (#58717)
- **2026-09-25** [`22bbe3f102`](https://github.com/vllm-project/vllm/commit/22bbe3f102) [#57599](https://github.com/vllm-project/vllm/pull/57599) — [ROCm][CI] Expand single-GPU coverage on MI355 DPX (#57599)
- **2026-09-25** [`e3dd5b5a75`](https://github.com/vllm-project/vllm/commit/e3dd5b5a75) [#58740](https://github.com/vllm-project/vllm/pull/58740) — [ROCm][CI] Test AMD DeepSeek V4 MoE routing against a PyTorch reference (#58740)
- **2026-09-25** [`1b922ffcbe`](https://github.com/vllm-project/vllm/commit/1b922ffcbe) [#58748](https://github.com/vllm-project/vllm/pull/58748) — [ROCm][CI] Add quantized MoE serving test for gfx950 (#58748)
- **2026-09-25** [`b21757555a`](https://github.com/vllm-project/vllm/commit/b21757555a) [#58724](https://github.com/vllm-project/vllm/pull/58724) — [ROCm][CI] Cover the AITER MQA logits dispatch on gfx950 (#58724)
- **2026-09-25** [`1417022c3d`](https://github.com/vllm-project/vllm/commit/1417022c3d) [#58045](https://github.com/vllm-project/vllm/pull/58045) — [ROCm][Kimi-K3] Optimize low-concurrency speculative KDA (#58045)
- **2026-09-25** [`2617fe9383`](https://github.com/vllm-project/vllm/commit/2617fe9383) [#58454](https://github.com/vllm-project/vllm/pull/58454) — [Bugfix][GLM-5.3-Flash] kpool corruption with speculative decoding (#58454)
- **2026-09-25** [`25b0add7b8`](https://github.com/vllm-project/vllm/commit/25b0add7b8) [#58698](https://github.com/vllm-project/vllm/pull/58698) — [ROCm][CI] Pass weight_shape in MXFP8 block32 linear tests (#58698)
- **2026-09-25** [`35f92d2abc`](https://github.com/vllm-project/vllm/commit/35f92d2abc) [#58659](https://github.com/vllm-project/vllm/pull/58659) — [ROCm] Credit ROCm/aiter for the block32 GEMM's packed kernel and in-launch split-K (#58659)
- **2026-09-25** [`267eee54bf`](https://github.com/vllm-project/vllm/commit/267eee54bf) [#57497](https://github.com/vllm-project/vllm/pull/57497) — [Qwen4Exp][ROCm] PLE n-gram table CPU offload (#57497)
- **2026-09-25** [`fa94450b74`](https://github.com/vllm-project/vllm/commit/fa94450b74) [#58607](https://github.com/vllm-project/vllm/pull/58607) — [CI][ROCm] Prevent Model Executor apt stalls (#58607)
- **2026-09-25** [`4013f3ad6c`](https://github.com/vllm-project/vllm/commit/4013f3ad6c) [#58244](https://github.com/vllm-project/vllm/pull/58244) — [ROCm] Fix CI runtime and tests for MI355 DPX (#58244)
- **2026-09-25** [`8b365ff949`](https://github.com/vllm-project/vllm/commit/8b365ff949) [#57744](https://github.com/vllm-project/vllm/pull/57744) — [ROCm][Build] Filter crate tags from vLLM version detection (#57744)
- **2026-09-25** [`4d79d5c638`](https://github.com/vllm-project/vllm/commit/4d79d5c638) [#58566](https://github.com/vllm-project/vllm/pull/58566) — [ROCm] Cut 69 wasted contiguous copies per decode step from the skinny GEMM path (#58566)
- **2026-09-25** [`f55419c43c`](https://github.com/vllm-project/vllm/commit/f55419c43c) [#54223](https://github.com/vllm-project/vllm/pull/54223) — [Bugfix][Quantization] Fix MXFP8 startup crash on layers below mm_mxfp8 shape limits (#54223)
- **2026-09-25** [`3059155b47`](https://github.com/vllm-project/vllm/commit/3059155b47) [#58510](https://github.com/vllm-project/vllm/pull/58510) — [ROCm][Perf] MXFP8 GEMM on native 32x32 block scales for gfx950 (#58510)
- **2026-09-25** [`65c5e24689`](https://github.com/vllm-project/vllm/commit/65c5e24689) [#58393](https://github.com/vllm-project/vllm/pull/58393) — [ROCm][CI][AITER Coverage] Harden MoE sorting-backend/dispatch env-var test matrix (#58393)
- **2026-09-24** [`9ac3b7c69f`](https://github.com/vllm-project/vllm/commit/9ac3b7c69f) [#58558](https://github.com/vllm-project/vllm/pull/58558) — [ROCm][CI] Mirror the DSv4-Flash disaggregated DP EP group on MI355 (#58558)
- **2026-09-24** [`e33de821c0`](https://github.com/vllm-project/vllm/commit/e33de821c0) [#58535](https://github.com/vllm-project/vllm/pull/58535) — [ROCm][CI] skip the ROCm MRV1 default where MRV1 cannot serve the config (#58535)
- **2026-09-24** [`92e9c6bf13`](https://github.com/vllm-project/vllm/commit/92e9c6bf13) [#51681](https://github.com/vllm-project/vllm/pull/51681) — [ROCm] Fix misrouting race-condition in multi-decode P/D disagg with mori-io (#51681)
- **2026-09-24** [`58aa2f1ef1`](https://github.com/vllm-project/vllm/commit/58aa2f1ef1) [#58572](https://github.com/vllm-project/vllm/pull/58572) — [Refactor] Move auxiliary files out of the repository root (#58572)
- **2026-09-24** [`3c42385d7d`](https://github.com/vllm-project/vllm/commit/3c42385d7d) [#58446](https://github.com/vllm-project/vllm/pull/58446) — [Refactor] Remove dead or duplicate tests (#58446)
- **2026-09-24** [`721d0e5c11`](https://github.com/vllm-project/vllm/commit/721d0e5c11) [#58456](https://github.com/vllm-project/vllm/pull/58456) — [ROCm][DSv4.1][Perf] Emit MXFP8 from the sparse decode reduce and run wo_a as a grouped FP8 GEMM (#58456)
- **2026-09-24** [`c3f5270270`](https://github.com/vllm-project/vllm/commit/c3f5270270) [#58432](https://github.com/vllm-project/vllm/pull/58432) — [ROCm][CI] Add the MI355 TurboQuant t3nc mirror (#58432)
- **2026-09-24** [`153f2ba1b9`](https://github.com/vllm-project/vllm/commit/153f2ba1b9) [#58474](https://github.com/vllm-project/vllm/pull/58474) — [Compile][CI] Honor Triton cache overrides and add AMD timeout headroom (#58474)
- **2026-09-24** [`4fb767ff0a`](https://github.com/vllm-project/vllm/commit/4fb767ff0a) [#53175](https://github.com/vllm-project/vllm/pull/53175) — [Kernel] Resubmit PR 48666 - Gemma4 FP8 KV FA4 head dim 512 backend selection (#53175)
- **2026-09-24** [`e78e367c6e`](https://github.com/vllm-project/vllm/commit/e78e367c6e) [#54988](https://github.com/vllm-project/vllm/pull/54988) — [ROCm] Give turboquant boundary layers a layout-compatible backend (#54988)
- **2026-09-24** [`e6dc16cebd`](https://github.com/vllm-project/vllm/commit/e6dc16cebd) [#57075](https://github.com/vllm-project/vllm/pull/57075) — [PCP] Support prefill context parallelism with data parallelism (#57075)
- **2026-09-24** [`e9f167129c`](https://github.com/vllm-project/vllm/commit/e9f167129c) [#58369](https://github.com/vllm-project/vllm/pull/58369) — [CI][ROCM] Add the Fusion E2E TP2 Quick group on MI355, and the AITER MLA fix it needs (#58369)
- **2026-09-23** [`21ee743f47`](https://github.com/vllm-project/vllm/commit/21ee743f47) [#58465](https://github.com/vllm-project/vllm/pull/58465) — [CI][Bugfix] Limit MRV2 sampler JIT warmup registration to ROCm (#58465)
- **2026-09-23** [`5fcc6e7c73`](https://github.com/vllm-project/vllm/commit/5fcc6e7c73) [#58419](https://github.com/vllm-project/vllm/pull/58419) — [ROCm][Bugfix] Fix TileLang mHC fused RMSNorm on 64-wide wavefronts (#58419)
- **2026-09-23** [`8b660ce96b`](https://github.com/vllm-project/vllm/commit/8b660ce96b) [#58093](https://github.com/vllm-project/vllm/pull/58093) — [ROCm][Test] Cover MoRI graph replay and output lifetime (#58093)
- **2026-09-23** [`b5ea0c7107`](https://github.com/vllm-project/vllm/commit/b5ea0c7107) [#57923](https://github.com/vllm-project/vllm/pull/57923) — [Bugfix][ROCm] Fix startup OOM in AITER MLA FP8 prefill workspace sizing (#57923)
- **2026-09-23** [`c4cfd7007b`](https://github.com/vllm-project/vllm/commit/c4cfd7007b) [#58012](https://github.com/vllm-project/vllm/pull/58012) — [CI][ROCm] Add an MI355 Kimi-K3 unit test group (#58012)
- **2026-09-23** [`8033bd08c1`](https://github.com/vllm-project/vllm/commit/8033bd08c1) [#58095](https://github.com/vllm-project/vllm/pull/58095) — [ROCm][CI] Validate Mooncake and NIXL prefill/decode accuracy (#58095)
- **2026-09-23** [`b715699df4`](https://github.com/vllm-project/vllm/commit/b715699df4) [#50212](https://github.com/vllm-project/vllm/pull/50212) — [ROCm][Perf] Extend QK-norm/RoPE/KV-cache fusion to MRoPE (#50212)
- **2026-09-23** [`a22c637ed9`](https://github.com/vllm-project/vllm/commit/a22c637ed9) [#58091](https://github.com/vllm-project/vllm/pull/58091) — [ROCm][Test] Check GDN prefill numerics and output ownership (#58091)
- **2026-09-23** [`36bc694889`](https://github.com/vllm-project/vllm/commit/36bc694889) [#58271](https://github.com/vllm-project/vllm/pull/58271) — [ROCm][CI] Include Python tooling in ROCm CI artifacts (#58271)
- **2026-09-23** [`56b3acb55b`](https://github.com/vllm-project/vllm/commit/56b3acb55b) [#58089](https://github.com/vllm-project/vllm/pull/58089) — [ROCm][Bugfix] Keep zero MiniMax MXFP8 activation blocks finite (#58089)
- **2026-09-23** [`1904ed9402`](https://github.com/vllm-project/vllm/commit/1904ed9402) [#58225](https://github.com/vllm-project/vllm/pull/58225) — [Perf][ROCm][Attention] Narrow the Triton prefill-attention KV tile on RDNA3/RDNA4 (#58225)
- **2026-09-23** [`96e203b08e`](https://github.com/vllm-project/vllm/commit/96e203b08e) [#58092](https://github.com/vllm-project/vllm/pull/58092) — [ROCm][Bugfix] Register MRV2 sampler JIT warmups (#58092)
- **2026-09-23** [`26879f3260`](https://github.com/vllm-project/vllm/commit/26879f3260) [#58099](https://github.com/vllm-project/vllm/pull/58099) — [ROCm][Compile] Fuse AITER static FP8 attention output (#58099)
- **2026-09-23** [`153242a314`](https://github.com/vllm-project/vllm/commit/153242a314) [#58281](https://github.com/vllm-project/vllm/pull/58281) — [ROCm][CI] Add MI355 dense NVFP4 and MoRI kernel mirrors (#58281)
- **2026-09-23** [`a9f07d0bc5`](https://github.com/vllm-project/vllm/commit/a9f07d0bc5) [#58282](https://github.com/vllm-project/vllm/pull/58282) — [ROCm][CI] Mirror the three TurboQuant evaluation groups on MI355 (#58282)
- **2026-09-23** [`eb2e91d3ba`](https://github.com/vllm-project/vllm/commit/eb2e91d3ba) [#53283](https://github.com/vllm-project/vllm/pull/53283) — [ROCm][Perf] Use wvSplitK for single-output GEMMs (#53283)
- **2026-09-23** [`88aa0d287d`](https://github.com/vllm-project/vllm/commit/88aa0d287d) [#52988](https://github.com/vllm-project/vllm/pull/52988) — [Spec decode] Support variable-length decode for Kimi-K3 adaptive ver (#52988)
- **2026-09-23** [`e581e14002`](https://github.com/vllm-project/vllm/commit/e581e14002) [#50922](https://github.com/vllm-project/vllm/pull/50922) — [ROCm][CI] Stage G gating (#50922)
- **2026-09-23** [`0eb42dbbfc`](https://github.com/vllm-project/vllm/commit/0eb42dbbfc) [#58098](https://github.com/vllm-project/vllm/pull/58098) — [ROCm][Compile] Support BF16 AsyncTP fusion (#58098)
- **2026-09-23** [`f9dce295c9`](https://github.com/vllm-project/vllm/commit/f9dce295c9) [#57451](https://github.com/vllm-project/vllm/pull/57451) — [ROCm][DSv4][Perf] Fuse the inverse RoPE into the sparse decode reduce (#57451)
- **2026-09-22** [`d110c2f19c`](https://github.com/vllm-project/vllm/commit/d110c2f19c) [#52052](https://github.com/vllm-project/vllm/pull/52052) — [ROCm] Use silu_and_mul_with_clamp's torch._C op (#52052)
- **2026-09-22** [`1c0eee919d`](https://github.com/vllm-project/vllm/commit/1c0eee919d) [#51915](https://github.com/vllm-project/vllm/pull/51915) — [ROCm][Model][Bugfix] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness (#51915)
- **2026-09-22** [`9646f53064`](https://github.com/vllm-project/vllm/commit/9646f53064) [#58153](https://github.com/vllm-project/vllm/pull/58153) — [Bugfix][ROCm] Use the platform FP8 range in the concat MLA q test (#58153)
- **2026-09-22** [`111d7d7be2`](https://github.com/vllm-project/vllm/commit/111d7d7be2) [#58006](https://github.com/vllm-project/vllm/pull/58006) — [ROCm][Build][The Rock] Bump Triton version to 3.8.x tip-of-tree with source build in The Rock image (#58006)
- **2026-09-22** [`fae5cbfc8b`](https://github.com/vllm-project/vllm/commit/fae5cbfc8b) [#58002](https://github.com/vllm-project/vllm/pull/58002) — [Refactor] Remove dead code multiple places (#58002)
- **2026-09-22** [`d1f63f2af9`](https://github.com/vllm-project/vllm/commit/d1f63f2af9) [#58030](https://github.com/vllm-project/vllm/pull/58030) — [ROCm][CI] Add GELU activation for AiterExperts in the modular-kernel coverage (#58030)
- **2026-09-22** [`ca831d1c55`](https://github.com/vllm-project/vllm/commit/ca831d1c55) [#57435](https://github.com/vllm-project/vllm/pull/57435) — [ROCm][DSv4.1][Perf] Fuse the inverse RoPE into the sparse decode reduce (#57435)
- **2026-09-22** [`72675c4706`](https://github.com/vllm-project/vllm/commit/72675c4706) [#58136](https://github.com/vllm-project/vllm/pull/58136) — [Bugfix][ROCm] Dispatch the QuantFP8 CUDA fallback on the class (#58136)
- **2026-09-22** [`68363d64ec`](https://github.com/vllm-project/vllm/commit/68363d64ec) [#47842](https://github.com/vllm-project/vllm/pull/47842) — [ROCm][Perf] Avoid extra reshape kernel in Qwen GDN output norm (#47842)
- **2026-09-22** [`42a85a4976`](https://github.com/vllm-project/vllm/commit/42a85a4976) [#57919](https://github.com/vllm-project/vllm/pull/57919) — [ROCm][Bugfix] Explicitly reject FSE=1 with DPA+ETP deployment for DeepSeek-V4 (#57919)
- **2026-09-21** [`382970ee6c`](https://github.com/vllm-project/vllm/commit/382970ee6c) [#50592](https://github.com/vllm-project/vllm/pull/50592) — [Kimi-K3][AMD] Return KDA and MLA projection outputs directly (#50592)
- **2026-09-21** [`12972ae40b`](https://github.com/vllm-project/vllm/commit/12972ae40b) [#57866](https://github.com/vllm-project/vllm/pull/57866) — [Bugfix][ROCm] Reject unsupported EP for monolithic AITER MXFP4 MoE (#57866)
- **2026-09-21** [`17322375a2`](https://github.com/vllm-project/vllm/commit/17322375a2) [#54185](https://github.com/vllm-project/vllm/pull/54185) — [ROCm][Perf] Route the fused shared-expert gate GEMM through the platform dispatcher (#54185)
- **2026-09-21** [`4f14516790`](https://github.com/vllm-project/vllm/commit/4f14516790) [#57931](https://github.com/vllm-project/vllm/pull/57931) — [ROCm][CI] Use ROCm backend for DeepSeek V4.1 ViT test (#57931)
- **2026-09-21** [`874a6b5a06`](https://github.com/vllm-project/vllm/commit/874a6b5a06) [#55001](https://github.com/vllm-project/vllm/pull/55001) — [ROCm] Refactor tuned gemms (#55001)
- **2026-09-21** [`6b858751f6`](https://github.com/vllm-project/vllm/commit/6b858751f6) [#57958](https://github.com/vllm-project/vllm/pull/57958) — [docs] Fix legacy hf CLI references (vllm) (#57958)
- **2026-09-21** [`e34685dfc0`](https://github.com/vllm-project/vllm/commit/e34685dfc0) [#52362](https://github.com/vllm-project/vllm/pull/52362) — [ROCm][DSv4] Enable DSpark adaptive verification (#52362)
- **2026-09-21** [`7488b5780f`](https://github.com/vllm-project/vllm/commit/7488b5780f) [#57869](https://github.com/vllm-project/vllm/pull/57869) — [ROCm][Tests] Reduce host memory when downcasting FP32 HF references (#57869)
- **2026-09-21** [`82daf9f575`](https://github.com/vllm-project/vllm/commit/82daf9f575) [#57876](https://github.com/vllm-project/vllm/pull/57876) — [CI][ROCm] Add ten AMD parity groups (#57876)
- **2026-09-21** [`04c1f4a407`](https://github.com/vllm-project/vllm/commit/04c1f4a407) [#57906](https://github.com/vllm-project/vllm/pull/57906) — [Bugfix][ROCm][DSv4.1] Disable SWA bounded replay on ROCm (#57906)
- **2026-09-21** [`0aee727ff6`](https://github.com/vllm-project/vllm/commit/0aee727ff6) [#57903](https://github.com/vllm-project/vllm/pull/57903) — [CI][ROCm] Increase timeout for MI300 Distributed DP Extended (#57903)
- **2026-09-21** [`8902dbb177`](https://github.com/vllm-project/vllm/commit/8902dbb177) [#57877](https://github.com/vllm-project/vllm/pull/57877) — [CI][ROCm] Mirror remaining portable suites without duplicate coverage (#57877)
- **2026-09-21** [`b8cf275382`](https://github.com/vllm-project/vllm/commit/b8cf275382) [#54535](https://github.com/vllm-project/vllm/pull/54535) — [AMD][Minimax-M3][perf] Enable packed LBHNC AITER QK-norm fusion for MiniMax-M3 on ROCm (#54535)
- **2026-09-21** [`f05b88751e`](https://github.com/vllm-project/vllm/commit/f05b88751e) [#57870](https://github.com/vllm-project/vllm/pull/57870) — [CI][ROCm] Make Python-only installation failures blocking (#57870)
- **2026-09-21** [`0ff0477ff9`](https://github.com/vllm-project/vllm/commit/0ff0477ff9) [#57526](https://github.com/vllm-project/vllm/pull/57526) — [Perf][ROCm] Add a ROCm path for Hy4 and compile the backbone (#57526)
- **2026-09-21** [`76ee20c1ec`](https://github.com/vllm-project/vllm/commit/76ee20c1ec) [#57864](https://github.com/vllm-project/vllm/pull/57864) — [ROCm][Tests] Avoid pooling cleanup waits against live shared engines (#57864)
- **2026-09-21** [`6dfd87f596`](https://github.com/vllm-project/vllm/commit/6dfd87f596) [#57491](https://github.com/vllm-project/vllm/pull/57491) — [ROCm][DSv4.1] Keep the Engram tables in host memory on ROCm (#57491)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#59064](https://github.com/vllm-project/vllm/issues/59064) | [Bug]: Kimi-K3 MXFP4: flashinfer_trtllm selects unsupported BF16/SiTU  | bug, quantization, kimi, k3 | 2026-09-28 |
| [#59062](https://github.com/vllm-project/vllm/issues/59062) | [RFC]: Online quantization from arbitrary precision | rocm, RFC, quantization | 2026-09-28 |
| [#58931](https://github.com/vllm-project/vllm/issues/58931) | [Bug]: MooncakeStoreConnector crashes EngineCore when a request is pre | bug | 2026-09-28 |
| [#58751](https://github.com/vllm-project/vllm/issues/58751) | [RFC]: Universal Triton kernel autotuning at warmup | RFC | 2026-09-28 |
| [#59057](https://github.com/vllm-project/vllm/issues/59057) | [Bug]: vllm/vllm-openai:v0.30.0-cu129 crashes on import: operator torc | bug | 2026-09-28 |
| [#53912](https://github.com/vllm-project/vllm/issues/53912) | [Bug]: prefix caching + MTP still corrupts output on hybrid Mamba/GDN  | kv-cache-manager | 2026-09-28 |
| [#59045](https://github.com/vllm-project/vllm/issues/59045) | [Bug][ROCm] v0.30.0: DeepSeek-V4.1-Flash cannot boot on gfx942 — Engra | bug, rocm, deepseek, DSv4.1 | 2026-09-28 |
| [#59038](https://github.com/vllm-project/vllm/issues/59038) | [RFC]: DeepSeek-V4.1-Flash performance on MI325X (gfx942) | rocm, deepseek, DSv4.1 | 2026-09-28 |
| [#59022](https://github.com/vllm-project/vllm/issues/59022) | [ROCm][Perf] Fold Q fp8 quantization into QkNormRopeKvCacheFusionPass  | rocm, quantization | 2026-09-28 |
| [#58804](https://github.com/vllm-project/vllm/issues/58804) | [Performance][Bug]: Tiered Offloading | bug | 2026-09-28 |
| [#49106](https://github.com/vllm-project/vllm/issues/49106) | [Bug]: False positive warning "Unexpected gate/up projection names" fo | bug | 2026-09-28 |
| [#58729](https://github.com/vllm-project/vllm/issues/58729) | [Bug]: GLM MXFP4 returns 0 GSM8K on GB200 (DEP8+EP8, vLLM 0.30.0) | bug, glm | 2026-09-28 |
| [#59018](https://github.com/vllm-project/vllm/issues/59018) | [RFC]: Meta-device operator capture: see which operators a model runs  | rocm, intel-gpu, quantization, kimi, k3 | 2026-09-28 |
| [#59027](https://github.com/vllm-project/vllm/issues/59027) | [Bug][ROCm] v0.30.0: GLM-5.3-Flash cannot boot on gfx942 — ROCMAiterML | bug, rocm, glm | 2026-09-28 |
| [#58841](https://github.com/vllm-project/vllm/issues/58841) | [Tracking] Gemma4 AITER QK-norm+RoPE+KVCache fusion + RoPE IR-op migra | rocm | 2026-09-28 |
| [#57149](https://github.com/vllm-project/vllm/issues/57149) | [ROCm][AMD] Qwen3.8-2.4T-A95B gfx950 / MI355X Performance Optimization | performance, rocm, quantization | 2026-09-28 |
| [#57103](https://github.com/vllm-project/vllm/issues/57103) | [RFC]: Programmable KV Cache: Composable Policies for Agentic Serving | RFC, kimi | 2026-09-28 |
| [#59009](https://github.com/vllm-project/vllm/issues/59009) | [Bug]: Rust frontend chat-template rendering fails with 500 "unknown f | tool-calling, rust | 2026-09-28 |
| [#58270](https://github.com/vllm-project/vllm/issues/58270) | [Installation]:  v0.30.0 CPU wheels now require manylinux_2_39 (glibc  | installation | 2026-09-28 |
| [#57895](https://github.com/vllm-project/vllm/issues/57895) | [RFC]: Stable runtime tensor lifecycle for sleep and live weight reloa | RFC, quantization, kimi | 2026-09-28 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 97 |
| Other | 47 |
| Attention | 42 |
| Multimodal | 37 |
| MoE / Expert Parallel | 28 |
| Serving / API | 24 |
| Models | 22 |
| CI / Build | 22 |
| Scheduler / Engine | 20 |
| Quantization | 18 |
| Speculative Decoding | 15 |
| Disaggregation / PD | 13 |
| KV Cache / Offload | 8 |
| LoRA | 6 |
| Perf / Benchmark | 4 |
| Compilation / CUDA Graph | 4 |
| Docs | 2 |

## ROCm / AMD  (97 commits)

- **2026-09-28** [`b0d2b854f6`](https://github.com/vllm-project/vllm/commit/b0d2b854f6) [#59056](https://github.com/vllm-project/vllm/pull/59056)
  [ROCm]Keep LMCache OpenTelemetry on the image's 1.40 stack (#59056)
  _Files: `docker/Dockerfile.rock`, `docker/Dockerfile.rocm`_
- **2026-09-28** [`6b24bd8e75`](https://github.com/vllm-project/vllm/commit/6b24bd8e75) [#58208](https://github.com/vllm-project/vllm/pull/58208)
  [ROCm][Perf] Replace torch.topk in DSA candidate block selection (#58208)
  _Files: `vllm/model_executor/kernels/attention/dsa/candidate_blocks.py`_
- **2026-09-28** [`a7ff44355c`](https://github.com/vllm-project/vllm/commit/a7ff44355c) [#54956](https://github.com/vllm-project/vllm/pull/54956)
  [ROCm][Perf] Kimi-K3 Enable sharded latent MoE up-projection under EP (#54956)
  _Files: `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`_
- **2026-09-28** [`7ba3df63cb`](https://github.com/vllm-project/vllm/commit/7ba3df63cb) [#58983](https://github.com/vllm-project/vllm/pull/58983)
  [ROCm][Refactor] Move DeepSeek-V4/V4.1 multi-stream overlap gate to ROCm platform (#58983)
  _Files: `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/platforms/interface.py`, `vllm/platforms/rocm.py`_
- **2026-09-28** [`20b52e9f5b`](https://github.com/vllm-project/vllm/commit/20b52e9f5b) [#58114](https://github.com/vllm-project/vllm/pull/58114)
  [Perf][Qwen3.8] Reduce PLE metadata construction overhead (#58114)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/amd/ple_layer.py`, `vllm/models/qwen4_exp/nvidia/ple_layer.py`, `vllm/v1/attention/backends/mamba_attn.py` _+1 more__
- **2026-09-28** [`f6877f563c`](https://github.com/vllm-project/vllm/commit/f6877f563c) [#57568](https://github.com/vllm-project/vllm/pull/57568)
  [Bugfix][Spec Decode] Implement get_top_tokens() on the ROCm DeepSeek V4 MTP drafter (#57568)
  _Files: `tests/v1/spec_decode/test_dsv4_mtp_local_argmax.py`, `vllm/models/deepseek_v4/amd/mtp.py`_
- **2026-09-28** [`252279314b`](https://github.com/vllm-project/vllm/commit/252279314b) [#58652](https://github.com/vllm-project/vllm/pull/58652)
  Revert "[CI] Shard (H200 MIG 35GB / MI355 DPX) Entrypoints Integration (Pooling) into named jobs (#58652)" (#59011)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `tests/entrypoints/pooling/scoring/bi_encoder/__init__.py`, `tests/entrypoints/pooling/scoring/cross_encoder/__init__.py`, `tests/entrypoints/pooling/scoring/late_interaction/__init__.py` _+18 more__
- **2026-09-28** [`66d2d4b2e7`](https://github.com/vllm-project/vllm/commit/66d2d4b2e7) [#58451](https://github.com/vllm-project/vllm/pull/58451)
  [CI] Split Dynamic Shapes out of (H200 MIG 35GB) PyTorch Compilation + (MI300) mirror (#58451)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/pytorch.yaml`, `tests/compile/dynamic_shapes/__init__.py`, `tests/compile/dynamic_shapes/test_dynamic_shapes_compilation.py`_
- **2026-09-28** [`413ae4b167`](https://github.com/vllm-project/vllm/commit/413ae4b167) [#58652](https://github.com/vllm-project/vllm/pull/58652)
  [CI] Shard (H200 MIG 35GB / MI355 DPX) Entrypoints Integration (Pooling) into named jobs (#58652)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `tests/entrypoints/pooling/basic/test_factories.py`, `tests/entrypoints/pooling/basic/test_io_processor.py`, `tests/entrypoints/pooling/basic/test_utils.py` _+18 more__
- **2026-09-28** [`4694145045`](https://github.com/vllm-project/vllm/commit/4694145045) [#58646](https://github.com/vllm-project/vllm/pull/58646)
  [Skills] Update kernel-microbenchmark to include ROCm (#58646)
  _Files: `.agents/skills/kernel-microbenchmark/SKILL.md`, `.agents/skills/kernel-microbenchmark/benchmarks/graph_replay_benchmark.py`_
- **2026-09-28** [`55de40a2fc`](https://github.com/vllm-project/vllm/commit/55de40a2fc) [#58673](https://github.com/vllm-project/vllm/pull/58673)
  [Minimax-M3] Add Encoder CUDA graph support (#58673)
  _Files: `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/common/encoder_cudagraph.py`, `vllm/models/minimax_m3/common/vision_tower.py` _+1 more__
- **2026-09-28** [`77fbd9e225`](https://github.com/vllm-project/vllm/commit/77fbd9e225) [#58945](https://github.com/vllm-project/vllm/pull/58945)
  [Test][ROCm] Stabilize the mixed OLMoE LoRA test (#58945)
  _Files: `tests/lora/test_olmoe_tp.py`_
- **2026-09-28** [`31afa4f1bb`](https://github.com/vllm-project/vllm/commit/31afa4f1bb) [#58867](https://github.com/vllm-project/vllm/pull/58867)
  [ROCm] Bump AITER to v0.1.23 (#58867)
  _Files: `docker/Dockerfile.rock_base`, `docker/Dockerfile.rocm_base`, `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a16_moe.py`_
- **2026-09-27** [`73859fec58`](https://github.com/vllm-project/vllm/commit/73859fec58) [#55128](https://github.com/vllm-project/vllm/pull/55128)
  [Frontend] Switch Python Harmony dependency to oss-harmony (#55128)
  _Files: `.buildkite/intel_jobs/lm_eval_intel.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `docker/Dockerfile` _+13 more__
- **2026-09-27** [`187c81b32d`](https://github.com/vllm-project/vllm/commit/187c81b32d) [#58923](https://github.com/vllm-project/vllm/pull/58923)
  [ROCm][Bugfix] Fall back to default GEMM for CPU tensors on ROCm builds (#58923)
  _Files: `vllm/model_executor/layers/utils.py`_
- **2026-09-27** [`44af287ebe`](https://github.com/vllm-project/vllm/commit/44af287ebe) [#57407](https://github.com/vllm-project/vllm/pull/57407)
  [ROCm][Perf] Enable layer-aware CSA2 multi-stream overlap for DeepSeek-V4.1-Flash (#57407)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/utils/multi_stream_utils.py`_
- **2026-09-27** [`3137ff0773`](https://github.com/vllm-project/vllm/commit/3137ff0773) [#58201](https://github.com/vllm-project/vllm/pull/58201)
  [ROCm][Kimi-K3] Make VLLM_ROCM_USE_AITER_MOE_SITUV2 select a4w4/a8w4/a16w4 (#58201)
  _Files: `tests/kernels/moe/test_rocm_aiter_moe.py`, `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py` _+1 more__
- **2026-09-26** [`a4eb3f25d6`](https://github.com/vllm-project/vllm/commit/a4eb3f25d6) [#57263](https://github.com/vllm-project/vllm/pull/57263)
  [Spec Decode] Enable Gemma4 DSpark adaptive verification with FlashInfer (#57263)
  _Files: `docs/design/cuda_graphs.md`, `tests/distributed/test_dcp_direct_a2a_lse_reduce.py`, `tests/models/language/generation/test_gemma.py`, `tests/test_config.py` _+20 more__
- **2026-09-26** [`5840d95284`](https://github.com/vllm-project/vllm/commit/5840d95284) [#57071](https://github.com/vllm-project/vllm/pull/57071)
  [Bugfix][ROCm] AMD-Quark mixed-precision DeepSeek-V4.1 support (#57071)
  _Files: `tests/quantization/test_fp8.py`, `tests/quantization/test_quark.py`, `vllm/model_executor/layers/quantization/quark/quark.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py` _+7 more__
- **2026-09-26** [`da1aaec31f`](https://github.com/vllm-project/vllm/commit/da1aaec31f) [#57054](https://github.com/vllm-project/vllm/pull/57054)
  [CI] Split (H200 MIG/MI300) Basic Correctness into named jobs (#57054)
  _Files: `.buildkite/intel_jobs/basic_correctness_intel.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/distributed.yaml` _+14 more__
- **2026-09-25** [`e440b75bb6`](https://github.com/vllm-project/vllm/commit/e440b75bb6) [#50605](https://github.com/vllm-project/vllm/pull/50605)
  [ROCm] Bump torch 2.13, triton 3.8, torchaudio, torchvision (#50605)
  _Files: `cmake/external_projects/triton_kernels.cmake`, `docker/Dockerfile.rocm`, `docker/Dockerfile.rocm_base`, `vllm/model_executor/kernels/linear/mxfp8/rocm_native.py` _+1 more__
- **2026-09-25** [`31cc226401`](https://github.com/vllm-project/vllm/commit/31cc226401) [#58717](https://github.com/vllm-project/vllm/pull/58717)
  [ROCm][CI] Run the MLA attention+quant fusion test on ROCm (#58717)
  _Files: `tests/compile/passes/test_mla_attn_quant_fusion.py`_
- **2026-09-25** [`22bbe3f102`](https://github.com/vllm-project/vllm/commit/22bbe3f102) [#57599](https://github.com/vllm-project/vllm/pull/57599)
  [ROCm][CI] Expand single-GPU coverage on MI355 DPX (#57599)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/compile.yaml` _+21 more__
- **2026-09-25** [`e3dd5b5a75`](https://github.com/vllm-project/vllm/commit/e3dd5b5a75) [#58740](https://github.com/vllm-project/vllm/pull/58740)
  [ROCm][CI] Test AMD DeepSeek V4 MoE routing against a PyTorch reference (#58740)
  _Files: `tests/models/test_deepseek_v4_vl_rocm.py`_
- **2026-09-25** [`1b922ffcbe`](https://github.com/vllm-project/vllm/commit/1b922ffcbe) [#58748](https://github.com/vllm-project/vllm/pull/58748)
  [ROCm][CI] Add quantized MoE serving test for gfx950 (#58748)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/quantization.yaml`, `tests/quantization/test_rocm_moe.py`_
- **2026-09-25** [`b21757555a`](https://github.com/vllm-project/vllm/commit/b21757555a) [#58724](https://github.com/vllm-project/vllm/pull/58724)
  [ROCm][CI] Cover the AITER MQA logits dispatch on gfx950 (#58724)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`_
- **2026-09-25** [`1417022c3d`](https://github.com/vllm-project/vllm/commit/1417022c3d) [#58045](https://github.com/vllm-project/vllm/pull/58045)
  [ROCm][Kimi-K3] Optimize low-concurrency speculative KDA (#58045)
  _Files: `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/__init__.py` _+2 more__
- **2026-09-25** [`2617fe9383`](https://github.com/vllm-project/vllm/commit/2617fe9383) [#58454](https://github.com/vllm-project/vllm/pull/58454)
  [Bugfix][GLM-5.3-Flash] kpool corruption with speculative decoding (#58454)
  _Files: `tests/kernels/test_kpool_decode_update_batched.py`, `tests/v1/attention/test_kpool_tail_slot_mapping.py`, `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/common/attention.py` _+1 more__
- **2026-09-25** [`25b0add7b8`](https://github.com/vllm-project/vllm/commit/25b0add7b8) [#58698](https://github.com/vllm-project/vllm/pull/58698)
  [ROCm][CI] Pass weight_shape in MXFP8 block32 linear tests (#58698)
  _Files: `tests/kernels/quantization/test_rocm_mxfp8_linear.py`_
- **2026-09-25** [`35f92d2abc`](https://github.com/vllm-project/vllm/commit/35f92d2abc) [#58659](https://github.com/vllm-project/vllm/pull/58659)
  [ROCm] Credit ROCm/aiter for the block32 GEMM's packed kernel and in-launch split-K (#58659)
  _Files: `vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py`_
- **2026-09-25** [`267eee54bf`](https://github.com/vllm-project/vllm/commit/267eee54bf) [#57497](https://github.com/vllm-project/vllm/pull/57497)
  [Qwen4Exp][ROCm] PLE n-gram table CPU offload (#57497)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/qwen4_exp/test_ple.py`, `tests/test_config.py`, `vllm/config/engram.py` _+3 more__
- **2026-09-25** [`fa94450b74`](https://github.com/vllm-project/vllm/commit/fa94450b74) [#58607](https://github.com/vllm-project/vllm/pull/58607)
  [CI][ROCm] Prevent Model Executor apt stalls (#58607)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/model_executor.yaml`, `docker/Dockerfile.rock`, `docker/Dockerfile.rocm` _+1 more__
- **2026-09-25** [`4013f3ad6c`](https://github.com/vllm-project/vllm/commit/4013f3ad6c) [#58244](https://github.com/vllm-project/vllm/pull/58244)
  [ROCm] Fix CI runtime and tests for MI355 DPX (#58244)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `tests/basic_correctness/test_mem.py`, `tests/conftest.py`, `tests/evals/gsm8k/configs/models-gfx950-small.txt` _+8 more__
- **2026-09-25** [`8b365ff949`](https://github.com/vllm-project/vllm/commit/8b365ff949) [#57744](https://github.com/vllm-project/vllm/pull/57744)
  [ROCm][Build] Filter crate tags from vLLM version detection (#57744)
  _Files: `docker/Dockerfile.rock`, `docker/Dockerfile.rocm`, `docker/Dockerfile.rocm_gfx1250`_
- **2026-09-25** [`4d79d5c638`](https://github.com/vllm-project/vllm/commit/4d79d5c638) [#58566](https://github.com/vllm-project/vllm/pull/58566)
  [ROCm] Cut 69 wasted contiguous copies per decode step from the skinny GEMM path (#58566)
  _Files: `vllm/model_executor/layers/utils.py`_
- **2026-09-25** [`f55419c43c`](https://github.com/vllm-project/vllm/commit/f55419c43c) [#54223](https://github.com/vllm-project/vllm/pull/54223)
  [Bugfix][Quantization] Fix MXFP8 startup crash on layers below mm_mxfp8 shape limits (#54223)
  _Files: `tests/kernels/core/test_fused_q_kv_rmsnorm.py`, `tests/kernels/quantization/test_flashinfer_mxfp8_trtllm.py`, `tests/kernels/quantization/test_marlin_tile_padding.py`, `tests/kernels/quantization/test_mxfp8_kernel_selection.py` _+12 more__
- **2026-09-25** [`3059155b47`](https://github.com/vllm-project/vllm/commit/3059155b47) [#58510](https://github.com/vllm-project/vllm/pull/58510)
  [ROCm][Perf] MXFP8 GEMM on native 32x32 block scales for gfx950 (#58510)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/kernels/quantization/test_rocm_mxfp8_linear.py`, `vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py`, `vllm/model_executor/kernels/linear/mxfp8/rocm_native.py` _+1 more__
- **2026-09-25** [`65c5e24689`](https://github.com/vllm-project/vllm/commit/65c5e24689) [#58393](https://github.com/vllm-project/vllm/pull/58393)
  [ROCm][CI][AITER Coverage] Harden MoE sorting-backend/dispatch env-var test matrix (#58393)
  _Files: `tests/kernels/moe/test_modular_kernel_combinations.py`, `tests/kernels/moe/test_rocm_aiter_moe.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/layers/fused_moe/fused_flydsl_moe.py`_
- **2026-09-24** [`9ac3b7c69f`](https://github.com/vllm-project/vllm/commit/9ac3b7c69f) [#58558](https://github.com/vllm-project/vllm/pull/58558)
  [ROCm][CI] Mirror the DSv4-Flash disaggregated DP EP group on MI355 (#58558)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+1 more__
- **2026-09-24** [`e33de821c0`](https://github.com/vllm-project/vllm/commit/e33de821c0) [#58535](https://github.com/vllm-project/vllm/pull/58535)
  [ROCm][CI] skip the ROCm MRV1 default where MRV1 cannot serve the config (#58535)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-DSpark-FP8-TP4-ROCm.yaml`, `tests/evals/gsm8k/configs/models-spec-decode-rocm.txt`, `tests/test_config.py` _+1 more__
- **2026-09-24** [`92e9c6bf13`](https://github.com/vllm-project/vllm/commit/92e9c6bf13) [#51681](https://github.com/vllm-project/vllm/pull/51681)
  [ROCm] Fix misrouting race-condition in multi-decode P/D disagg with mori-io (#51681)
  _Files: `tests/v1/kv_connector/unit/test_moriio_kv_layout.py`, `tests/v1/kv_connector/unit/test_moriio_write_done_routing.py`, `tests/v1/kv_connector/unit/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py` _+2 more__
- **2026-09-24** [`58aa2f1ef1`](https://github.com/vllm-project/vllm/commit/58aa2f1ef1) [#58572](https://github.com/vllm-project/vllm/pull/58572)
  [Refactor] Move auxiliary files out of the repository root (#58572)
  _Files: `.buildkite/ci_config_rocm.yaml`, `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/scripts/hardware_ci/run-gh200-test.sh`, `.buildkite/test-amd.yaml` _+31 more__
- **2026-09-24** [`3c42385d7d`](https://github.com/vllm-project/vllm/commit/3c42385d7d) [#58446](https://github.com/vllm-project/vllm/pull/58446)
  [Refactor] Remove dead or duplicate tests (#58446)
  _Files: `tests/entrypoints/pooling/scoring/test_bi_encoder_online.py`, `tests/entrypoints/pooling/scoring/test_cross_encoder_online.py`, `tests/kernels/attention/test_attention_selector.py`, `tests/kernels/attention/test_rocm_attention_selector.py` _+7 more__
- **2026-09-24** [`721d0e5c11`](https://github.com/vllm-project/vllm/commit/721d0e5c11) [#58456](https://github.com/vllm-project/vllm/pull/58456)
  [ROCm][DSv4.1][Perf] Emit MXFP8 from the sparse decode reduce and run wo_a as a grouped FP8 GEMM (#58456)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-09-24** [`c3f5270270`](https://github.com/vllm-project/vllm/commit/c3f5270270) [#58432](https://github.com/vllm-project/vllm/pull/58432)
  [ROCm][CI] Add the MI355 TurboQuant t3nc mirror (#58432)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/Qwen3-4B-TQ-t3nc-ROCm.yaml`, `tests/evals/gsm8k/configs/models-turboquant-t3nc-rocm.txt`_
- **2026-09-24** [`153f2ba1b9`](https://github.com/vllm-project/vllm/commit/153f2ba1b9) [#58474](https://github.com/vllm-project/vllm/pull/58474)
  [Compile][CI] Honor Triton cache overrides and add AMD timeout headroom (#58474)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/model_executor.yaml`, `docs/design/torch_compile.md`, `vllm/compilation/compiler_interface.py`_
- **2026-09-24** [`4fb767ff0a`](https://github.com/vllm-project/vllm/commit/4fb767ff0a) [#53175](https://github.com/vllm-project/vllm/pull/53175)
  [Kernel] Resubmit PR 48666 - Gemma4 FP8 KV FA4 head dim 512 backend selection (#53175)
  _Files: `tests/kernels/attention/test_attention_selector.py`, `tests/v1/attention/test_backend_per_kind.py`, `vllm/model_executor/layers/attention/attention.py`, `vllm/model_executor/models/config.py` _+43 more__
- **2026-09-24** [`e78e367c6e`](https://github.com/vllm-project/vllm/commit/e78e367c6e) [#54988](https://github.com/vllm-project/vllm/pull/54988)
  [ROCm] Give turboquant boundary layers a layout-compatible backend (#54988)
  _Files: `tests/v1/attention/test_rocm_attention_backends_selection.py`, `vllm/platforms/rocm.py`, `vllm/v1/attention/selector.py`_
- **2026-09-24** [`e6dc16cebd`](https://github.com/vllm-project/vllm/commit/e6dc16cebd) [#57075](https://github.com/vllm-project/vllm/pull/57075)
  [PCP] Support prefill context parallelism with data parallelism (#57075)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/test_pcp_dp.py`, `tests/v1/worker/test_gpu_autoregressive_speculator.py`, `tests/v1/worker/test_gpu_pcp_manager.py` _+11 more__
- **2026-09-24** [`e9f167129c`](https://github.com/vllm-project/vllm/commit/e9f167129c) [#58369](https://github.com/vllm-project/vllm/pull/58369)
  [CI][ROCM] Add the Fusion E2E TP2 Quick group on MI355, and the AITER MLA fix it needs (#58369)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/compile.yaml`, `tests/compile/fusions_e2e/models.py`, `tests/compile/fusions_e2e/test_tp2_ar_rms.py` _+3 more__
- **2026-09-23** [`21ee743f47`](https://github.com/vllm-project/vllm/commit/21ee743f47) [#58465](https://github.com/vllm-project/vllm/pull/58465)
  [CI][Bugfix] Limit MRV2 sampler JIT warmup registration to ROCm (#58465)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-09-23** [`5fcc6e7c73`](https://github.com/vllm-project/vllm/commit/5fcc6e7c73) [#58419](https://github.com/vllm-project/vllm/pull/58419)
  [ROCm][Bugfix] Fix TileLang mHC fused RMSNorm on 64-wide wavefronts (#58419)
  _Files: `vllm/model_executor/kernels/mhc/tilelang_kernels.py`_
- **2026-09-23** [`8b660ce96b`](https://github.com/vllm-project/vllm/commit/8b660ce96b) [#58093](https://github.com/vllm-project/vllm/pull/58093)
  [ROCm][Test] Cover MoRI graph replay and output lifetime (#58093)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/fault_tolerance.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/moe/test_moe_layer.py`_
- **2026-09-23** [`b5ea0c7107`](https://github.com/vllm-project/vllm/commit/b5ea0c7107) [#57923](https://github.com/vllm-project/vllm/pull/57923)
  [Bugfix][ROCm] Fix startup OOM in AITER MLA FP8 prefill workspace sizing (#57923)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-09-23** [`c4cfd7007b`](https://github.com/vllm-project/vllm/commit/c4cfd7007b) [#58012](https://github.com/vllm-project/vllm/pull/58012)
  [CI][ROCm] Add an MI355 Kimi-K3 unit test group (#58012)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `tests/models/kimi_k3/test_attn_res.py`, `vllm/platforms/rocm.py`_
- **2026-09-23** [`8033bd08c1`](https://github.com/vllm-project/vllm/commit/8033bd08c1) [#58095](https://github.com/vllm-project/vllm/pull/58095)
  [ROCm][CI] Validate Mooncake and NIXL prefill/decode accuracy (#58095)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/disaggregated_mooncake.yaml`, `tests/v1/kv_connector/mooncake_integration/test_accuracy_rocm.py` _+3 more__
- **2026-09-23** [`b715699df4`](https://github.com/vllm-project/vllm/commit/b715699df4) [#50212](https://github.com/vllm-project/vllm/pull/50212)
  [ROCm][Perf] Extend QK-norm/RoPE/KV-cache fusion to MRoPE (#50212)
  _Files: `tests/compile/fusions_e2e/common.py`, `tests/compile/fusions_e2e/conftest.py`, `tests/compile/passes/test_rocm_aiter_qk_norm_rope_kvcache_fusion.py`, `vllm/_aiter_ops.py` _+7 more__
- **2026-09-23** [`a22c637ed9`](https://github.com/vllm-project/vllm/commit/a22c637ed9) [#58091](https://github.com/vllm-project/vllm/pull/58091)
  [ROCm][Test] Check GDN prefill numerics and output ownership (#58091)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/mamba/test_gdn_rocm_layout_dispatch.py`_
- **2026-09-23** [`36bc694889`](https://github.com/vllm-project/vllm/commit/36bc694889) [#58271](https://github.com/vllm-project/vllm/pull/58271)
  [ROCm][CI] Include Python tooling in ROCm CI artifacts (#58271)
  _Files: `docker/Dockerfile.rocm`_
- **2026-09-23** [`56b3acb55b`](https://github.com/vllm-project/vllm/commit/56b3acb55b) [#58089](https://github.com/vllm-project/vllm/pull/58089)
  [ROCm][Bugfix] Keep zero MiniMax MXFP8 activation blocks finite (#58089)
  _Files: `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`_
- **2026-09-23** [`1904ed9402`](https://github.com/vllm-project/vllm/commit/1904ed9402) [#58225](https://github.com/vllm-project/vllm/pull/58225)
  [Perf][ROCm][Attention] Narrow the Triton prefill-attention KV tile on RDNA3/RDNA4 (#58225)
  _Files: `tests/kernels/attention/test_triton_prefill_attention.py`, `vllm/v1/attention/ops/triton_prefill_attention.py`_
- **2026-09-23** [`96e203b08e`](https://github.com/vllm-project/vllm/commit/96e203b08e) [#58092](https://github.com/vllm-project/vllm/pull/58092)
  [ROCm][Bugfix] Register MRV2 sampler JIT warmups (#58092)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/jit_monitor.yaml`, `tests/jit_monitor/test_no_runtime_jit_rocm.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-09-23** [`26879f3260`](https://github.com/vllm-project/vllm/commit/26879f3260) [#58099](https://github.com/vllm-project/vllm/pull/58099)
  [ROCm][Compile] Fuse AITER static FP8 attention output (#58099)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/compile.yaml`, `tests/compile/correctness_e2e/test_attn_quant.py`, `tests/compile/passes/test_fusion_attn.py` _+1 more__
- **2026-09-23** [`153242a314`](https://github.com/vllm-project/vllm/commit/153242a314) [#58281](https://github.com/vllm-project/vllm/pull/58281)
  [ROCm][CI] Add MI355 dense NVFP4 and MoRI kernel mirrors (#58281)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/moe/test_mori_moe.py`, `tests/kernels/quantization/test_nvfp4_emulation.py`_
- **2026-09-23** [`a9f07d0bc5`](https://github.com/vllm-project/vllm/commit/a9f07d0bc5) [#58282](https://github.com/vllm-project/vllm/pull/58282)
  [ROCm][CI] Mirror the three TurboQuant evaluation groups on MI355 (#58282)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/Qwen3-4B-TQ-k3v4nc-ROCm.yaml`, `tests/evals/gsm8k/configs/Qwen3-4B-TQ-k8v4-ROCm.yaml` _+4 more__
- **2026-09-23** [`eb2e91d3ba`](https://github.com/vllm-project/vllm/commit/eb2e91d3ba) [#53283](https://github.com/vllm-project/vllm/pull/53283)
  [ROCm][Perf] Use wvSplitK for single-output GEMMs (#53283)
  _Files: `tests/model_executor/layers/test_rocm_unquantized_gemm.py`, `vllm/model_executor/layers/utils.py`_
- **2026-09-23** [`88aa0d287d`](https://github.com/vllm-project/vllm/commit/88aa0d287d) [#52988](https://github.com/vllm-project/vllm/pull/52988)
  [Spec decode] Support variable-length decode for Kimi-K3 adaptive ver (#52988)
  _Files: `tests/v1/attention/test_flashinfer_mla_dcp.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `tests/v1/worker/test_mamba_hybrid_model_state.py` _+9 more__
- **2026-09-23** [`e581e14002`](https://github.com/vllm-project/vllm/commit/e581e14002) [#50922](https://github.com/vllm-project/vllm/pull/50922)
  [ROCm][CI] Stage G gating (#50922)
  _Files: `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/e2e_integration.yaml` _+3 more__
- **2026-09-23** [`0eb42dbbfc`](https://github.com/vllm-project/vllm/commit/0eb42dbbfc) [#58098](https://github.com/vllm-project/vllm/pull/58098)
  [ROCm][Compile] Support BF16 AsyncTP fusion (#58098)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/compile.yaml`, `tests/compile/correctness_e2e/test_async_tp.py`, `tests/compile/fusions_e2e/test_tp2_rocm_async_tp.py` _+5 more__
- **2026-09-23** [`f9dce295c9`](https://github.com/vllm-project/vllm/commit/f9dce295c9) [#57451](https://github.com/vllm-project/vllm/pull/57451)
  [ROCm][DSv4][Perf] Fuse the inverse RoPE into the sparse decode reduce (#57451)
  _Files: `vllm/models/deepseek_v4/amd/rocm.py`_
- **2026-09-22** [`d110c2f19c`](https://github.com/vllm-project/vllm/commit/d110c2f19c) [#52052](https://github.com/vllm-project/vllm/pull/52052)
  [ROCm] Use silu_and_mul_with_clamp's torch._C op (#52052)
  _Files: `tests/kernels/core/test_activation.py`, `vllm/model_executor/layers/activation.py`_
- **2026-09-22** [`1c0eee919d`](https://github.com/vllm-project/vllm/commit/1c0eee919d) [#51915](https://github.com/vllm-project/vllm/pull/51915)
  [ROCm][Model][Bugfix] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness (#51915)
  _Files: `tests/kernels/test_fused_deepseek_v32_norm_rope.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/models/deepseek_v2.py` _+4 more__
- **2026-09-22** [`9646f53064`](https://github.com/vllm-project/vllm/commit/9646f53064) [#58153](https://github.com/vllm-project/vllm/pull/58153)
  [Bugfix][ROCm] Use the platform FP8 range in the concat MLA q test (#58153)
  _Files: `tests/kernels/test_concat_mla_q.py`_
- **2026-09-22** [`111d7d7be2`](https://github.com/vllm-project/vllm/commit/111d7d7be2) [#58006](https://github.com/vllm-project/vllm/pull/58006)
  [ROCm][Build][The Rock] Bump Triton version to 3.8.x tip-of-tree with source build in The Rock image (#58006)
  _Files: `docker/Dockerfile.rock_base`_
- **2026-09-22** [`fae5cbfc8b`](https://github.com/vllm-project/vllm/commit/fae5cbfc8b) [#58002](https://github.com/vllm-project/vllm/pull/58002)
  [Refactor] Remove dead code multiple places (#58002)
  _Files: `vllm/entrypoints/generate/base/protocol.py`, `vllm/logits_process.py`, `vllm/model_executor/layers/fused_moe/utils.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py` _+8 more__
- **2026-09-22** [`d1f63f2af9`](https://github.com/vllm-project/vllm/commit/d1f63f2af9) [#58030](https://github.com/vllm-project/vllm/pull/58030)
  [ROCm][CI] Add GELU activation for AiterExperts in the modular-kernel coverage (#58030)
  _Files: `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/test_modular_kernel_combinations.py`_
- **2026-09-22** [`ca831d1c55`](https://github.com/vllm-project/vllm/commit/ca831d1c55) [#57435](https://github.com/vllm-project/vllm/pull/57435)
  [ROCm][DSv4.1][Perf] Fuse the inverse RoPE into the sparse decode reduce (#57435)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/models/deepseek_v41/amd/rocm.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-09-22** [`72675c4706`](https://github.com/vllm-project/vllm/commit/72675c4706) [#58136](https://github.com/vllm-project/vllm/pull/58136)
  [Bugfix][ROCm] Dispatch the QuantFP8 CUDA fallback on the class (#58136)
  _Files: `vllm/model_executor/layers/quantization/input_quant_fp8.py`_
- **2026-09-22** [`68363d64ec`](https://github.com/vllm-project/vllm/commit/68363d64ec) [#47842](https://github.com/vllm-project/vllm/pull/47842)
  [ROCm][Perf] Avoid extra reshape kernel in Qwen GDN output norm (#47842)
  _Files: `tests/compile/passes/test_fusion.py`, `tests/kernels/mamba/test_gdn_output_projection.py`, `tests/kernels/test_fla_layernorm_guard.py`, `vllm/compilation/passes/fusion/rocm_aiter_fusion.py` _+2 more__
- **2026-09-22** [`42a85a4976`](https://github.com/vllm-project/vllm/commit/42a85a4976) [#57919](https://github.com/vllm-project/vllm/pull/57919)
  [ROCm][Bugfix] Explicitly reject FSE=1 with DPA+ETP deployment for DeepSeek-V4 (#57919)
  _Files: `tests/models/test_deepseek_v4_vl_rocm.py`, `vllm/models/deepseek_v4/amd/model.py`_
- **2026-09-21** [`382970ee6c`](https://github.com/vllm-project/vllm/commit/382970ee6c) [#50592](https://github.com/vllm-project/vllm/pull/50592)
  [Kimi-K3][AMD] Return KDA and MLA projection outputs directly (#50592)
  _Files: `tests/models/kimi_k3/test_amd_kda_direct_return.py`, `tests/models/kimi_k3/test_amd_mla_direct_return.py`, `tests/models/kimi_k3/test_nvidia_kda_direct_return.py`, `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` _+3 more__
- **2026-09-21** [`12972ae40b`](https://github.com/vllm-project/vllm/commit/12972ae40b) [#57866](https://github.com/vllm-project/vllm/pull/57866)
  [Bugfix][ROCm] Reject unsupported EP for monolithic AITER MXFP4 MoE (#57866)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a8_moe.py`_
- **2026-09-21** [`17322375a2`](https://github.com/vllm-project/vllm/commit/17322375a2) [#54185](https://github.com/vllm-project/vllm/pull/54185)
  [ROCm][Perf] Route the fused shared-expert gate GEMM through the platform dispatcher (#54185)
  _Files: `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`_
- **2026-09-21** [`4f14516790`](https://github.com/vllm-project/vllm/commit/4f14516790) [#57931](https://github.com/vllm-project/vllm/pull/57931)
  [ROCm][CI] Use ROCm backend for DeepSeek V4.1 ViT test (#57931)
  _Files: `tests/models/multimodal/generation/test_vit_cudagraph.py`_
- **2026-09-21** [`874a6b5a06`](https://github.com/vllm-project/vllm/commit/874a6b5a06) [#55001](https://github.com/vllm-project/vllm/pull/55001)
  [ROCm] Refactor tuned gemms (#55001)
  _Files: `tests/kernels/quantization/test_rocm_mxfp4.py`, `vllm/_aiter_ops.py`_
- **2026-09-21** [`6b858751f6`](https://github.com/vllm-project/vllm/commit/6b858751f6) [#57958](https://github.com/vllm-project/vllm/pull/57958)
  [docs] Fix legacy hf CLI references (vllm) (#57958)
  _Files: `docker/Dockerfile.rock`, `docker/Dockerfile.rocm`, `docker/Dockerfile.rocm_gfx1250`, `docs/getting_started/installation/gpu.rocm.inc.md` _+2 more__
- **2026-09-21** [`e34685dfc0`](https://github.com/vllm-project/vllm/commit/e34685dfc0) [#52362](https://github.com/vllm-project/vllm/pull/52362)
  [ROCm][DSv4] Enable DSpark adaptive verification (#52362)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `tests/models/test_deepseek_v4_dspark_rocm.py`, `tests/v1/attention/test_deepseek_v4_rocm_adaptive.py`, `vllm/models/deepseek_v4/amd/dspark.py` _+2 more__
- **2026-09-21** [`7488b5780f`](https://github.com/vllm-project/vllm/commit/7488b5780f) [#57869](https://github.com/vllm-project/vllm/pull/57869)
  [ROCm][Tests] Reduce host memory when downcasting FP32 HF references (#57869)
  _Files: `tests/conftest.py`_
- **2026-09-21** [`82daf9f575`](https://github.com/vllm-project/vllm/commit/82daf9f575) [#57876](https://github.com/vllm-project/vllm/pull/57876)
  [CI][ROCm] Add ten AMD parity groups (#57876)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/disaggregated_ec.yaml`, `.buildkite/test_areas/disaggregated_mooncake.yaml` _+12 more__
- **2026-09-21** [`04c1f4a407`](https://github.com/vllm-project/vllm/commit/04c1f4a407) [#57906](https://github.com/vllm-project/vllm/pull/57906)
  [Bugfix][ROCm][DSv4.1] Disable SWA bounded replay on ROCm (#57906)
  _Files: `vllm/models/deepseek_v41/attention.py`_
- **2026-09-21** [`0aee727ff6`](https://github.com/vllm-project/vllm/commit/0aee727ff6) [#57903](https://github.com/vllm-project/vllm/pull/57903)
  [CI][ROCm] Increase timeout for MI300 Distributed DP Extended (#57903)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-21** [`8902dbb177`](https://github.com/vllm-project/vllm/commit/8902dbb177) [#57877](https://github.com/vllm-project/vllm/pull/57877)
  [CI][ROCm] Mirror remaining portable suites without duplicate coverage (#57877)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/models_basic.yaml` _+7 more__
- **2026-09-21** [`b8cf275382`](https://github.com/vllm-project/vllm/commit/b8cf275382) [#54535](https://github.com/vllm-project/vllm/pull/54535)
  [AMD][Minimax-M3][perf] Enable packed LBHNC AITER QK-norm fusion for MiniMax-M3 on ROCm (#54535)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/_aiter_ops.py`, `vllm/models/minimax_m3/amd/model.py`_
- **2026-09-21** [`f05b88751e`](https://github.com/vllm-project/vllm/commit/f05b88751e) [#57870](https://github.com/vllm-project/vllm/pull/57870)
  [CI][ROCm] Make Python-only installation failures blocking (#57870)
  _Files: `.buildkite/test_areas/misc.yaml`_
- **2026-09-21** [`0ff0477ff9`](https://github.com/vllm-project/vllm/commit/0ff0477ff9) [#57526](https://github.com/vllm-project/vllm/pull/57526)
  [Perf][ROCm] Add a ROCm path for Hy4 and compile the backbone (#57526)
  _Files: `tests/models/test_hyv4_rocm.py`, `vllm/models/hy_v4/__init__.py`, `vllm/models/hy_v4/amd/__init__.py`, `vllm/models/hy_v4/amd/model.py`_
- **2026-09-21** [`76ee20c1ec`](https://github.com/vllm-project/vllm/commit/76ee20c1ec) [#57864](https://github.com/vllm-project/vllm/pull/57864)
  [ROCm][Tests] Avoid pooling cleanup waits against live shared engines (#57864)
  _Files: `tests/models/language/pooling/conftest.py`, `tests/models/language/pooling_mteb_test/conftest.py`, `tests/models/multimodal/pooling/conftest.py`_
- **2026-09-21** [`6dfd87f596`](https://github.com/vllm-project/vllm/commit/6dfd87f596) [#57491](https://github.com/vllm-project/vllm/pull/57491)
  [ROCm][DSv4.1] Keep the Engram tables in host memory on ROCm (#57491)
  _Files: `tests/kernels/test_engram.py`, `tests/test_config.py`, `vllm/config/engram.py`, `vllm/config/vllm.py` _+1 more__

## Other  (47 commits)

- **2026-09-28** [`d7f5722d7b`](https://github.com/vllm-project/vllm/commit/d7f5722d7b) [#58747](https://github.com/vllm-project/vllm/pull/58747)
  [Bugfix][Logging] Preserve application log record factories (#58747)
  _Files: `tests/test_logger.py`, `vllm/logger.py`_
- **2026-09-27** [`fba47397f3`](https://github.com/vllm-project/vllm/commit/fba47397f3) [#43931](https://github.com/vllm-project/vllm/pull/43931)
  [Bugfix] V1: clear stale allowed_token_ids mask in InputBatch.condense (#43931)
  _Files: `tests/v1/worker/test_gpu_input_batch.py`, `vllm/v1/worker/gpu_input_batch.py`_
- **2026-09-25** [`9bf44c4013`](https://github.com/vllm-project/vllm/commit/9bf44c4013) [#58372](https://github.com/vllm-project/vllm/pull/58372)
  [Bugfix][Reasoning] Count Kimi K3 reasoning tokens (#58372)
  _Files: `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py`_
- **2026-09-25** [`974cb65155`](https://github.com/vllm-project/vllm/commit/974cb65155) [#48419](https://github.com/vllm-project/vllm/pull/48419)
  [Bugfix] V1: fix allowed_token_ids_mask aliasing in InputBatch.swap_states (#48419)
  _Files: `tests/v1/worker/test_gpu_input_batch.py`, `vllm/v1/worker/gpu_input_batch.py`_
- **2026-09-25** [`614b55f0b6`](https://github.com/vllm-project/vllm/commit/614b55f0b6) [#58205](https://github.com/vllm-project/vllm/pull/58205)
  [AuxOutput] Only require Model Runner V2 on GPU platform (#58205)
  _Files: `vllm/config/vllm.py`_
- **2026-09-25** [`a44d7b5151`](https://github.com/vllm-project/vllm/commit/a44d7b5151) [#57957](https://github.com/vllm-project/vllm/pull/57957)
  [Core][Logging] Fix JSON logging process decoration (#57957)
  _Files: `examples/features/logging_configuration.md`, `tests/test_logger.py`, `vllm/logger.py`, `vllm/logging_utils/formatter.py` _+2 more__
- **2026-09-25** [`234df712ed`](https://github.com/vllm-project/vllm/commit/234df712ed) [#58610](https://github.com/vllm-project/vllm/pull/58610)
  [MRV2] Minor model_runner.py code cleanup (#58610)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-09-25** [`afea5c20c7`](https://github.com/vllm-project/vllm/commit/afea5c20c7) [#58687](https://github.com/vllm-project/vllm/pull/58687)
  [Docs] Add return annotation to `fused_mm_input_norm_triton` (#58687)
  _Files: `vllm/model_executor/layers/fusion/mm_input_norm.py`_
- **2026-09-25** [`3a58aeb1a1`](https://github.com/vllm-project/vllm/commit/3a58aeb1a1) [#58336](https://github.com/vllm-project/vllm/pull/58336)
  [Bugfix] Stop leaking the internal field name in the max_tokens validation error (#58336)
  _Files: `vllm/renderers/params.py`_
- **2026-09-25** [`1f0bc49ee6`](https://github.com/vllm-project/vllm/commit/1f0bc49ee6) [#58321](https://github.com/vllm-project/vllm/pull/58321)
  [Structured Outputs] Parse Lark grammars natively in the xgrammar backend (#58321)
  _Files: `tests/entrypoints/llm/test_struct_output_generate.py`, `tests/v1/structured_output/test_backend_xgrammar_lark.py`, `vllm/sampling_params.py`, `vllm/v1/structured_output/backend_xgrammar.py` _+1 more__
- **2026-09-25** [`44257c2e35`](https://github.com/vllm-project/vllm/commit/44257c2e35) [#43048](https://github.com/vllm-project/vllm/pull/43048)
  [Feature] Triton kernel dispatcher (#43048)
  _Files: `tests/kernels/mamba/cpu/test_cpu_gdn_ops.py`, `tests/model_executor/test_triton_dispatcher.py`, `vllm/platforms/cpu.py`, `vllm/platforms/interface.py` _+4 more__
- **2026-09-25** [`32fc82343f`](https://github.com/vllm-project/vllm/commit/32fc82343f) [#56020](https://github.com/vllm-project/vllm/pull/56020)
  [Bugfix][LogitsProcessor] Validate ':' separator in custom logits processor FQCN (#56020)
  _Files: `tests/v1/logits_processors/test_loader.py`, `vllm/v1/sample/logits_processor/__init__.py`_
- **2026-09-25** [`7dbd0a8d22`](https://github.com/vllm-project/vllm/commit/7dbd0a8d22) [#58434](https://github.com/vllm-project/vllm/pull/58434)
  [Bugfix][MRV2] Treat padded prompt tails as spec-decode rows for hybrid models (#58434)
  _Files: `tests/v1/worker/test_mamba_hybrid_model_state.py`, `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`_
- **2026-09-25** [`a811738a60`](https://github.com/vllm-project/vllm/commit/a811738a60) [#57743](https://github.com/vllm-project/vllm/pull/57743)
  [Bugfix] Accept EOS after grammar finish in outlines backend; reject json_object at validation (#57743)
  _Files: `vllm/v1/structured_output/backend_outlines.py`_
- **2026-09-25** [`7833ff25dd`](https://github.com/vllm-project/vllm/commit/7833ff25dd) [#57988](https://github.com/vllm-project/vllm/pull/57988)
  Release prompt_embeds tensor when its InputBatch slot is freed (#57988)
  _Files: `tests/v1/worker/test_gpu_input_batch.py`, `vllm/v1/worker/gpu_input_batch.py`_
- **2026-09-24** [`e773247f8a`](https://github.com/vllm-project/vllm/commit/e773247f8a) [#58370](https://github.com/vllm-project/vllm/pull/58370)
  [Fast Start] Wait for weight cache daemon readiness (#58370)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py`_
- **2026-09-24** [`e30559b58f`](https://github.com/vllm-project/vllm/commit/e30559b58f) [#58590](https://github.com/vllm-project/vllm/pull/58590)
  [Core] Skip JIT monitor when JIT warmup is disabled (#58590)
  _Files: `tests/v1/worker/test_gpu_worker.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-09-24** [`074d57fce1`](https://github.com/vllm-project/vllm/commit/074d57fce1) [#58593](https://github.com/vllm-project/vllm/pull/58593)
  [Bugfix] Keep JIT warmup under enforce-eager when fault tolerance is on (#58593)
  _Files: `tests/compile/test_config.py`, `vllm/config/vllm.py`_
- **2026-09-24** [`d881812500`](https://github.com/vllm-project/vllm/commit/d881812500) [#58550](https://github.com/vllm-project/vllm/pull/58550)
  [Chore] Use Transformers v5 names and drop redundant processor `use_fast` (#58550)
- **2026-09-24** [`cccf7e1376`](https://github.com/vllm-project/vllm/commit/cccf7e1376) [#58541](https://github.com/vllm-project/vllm/pull/58541)
  Remove `.gemini/` and `CLAUDE.md` (#58541)
  _Files: `.gemini/config.yaml`, `CLAUDE.md`_
- **2026-09-24** [`14f98cbe5d`](https://github.com/vllm-project/vllm/commit/14f98cbe5d) [#54514](https://github.com/vllm-project/vllm/pull/54514)
  [Bugfix][XPU] store the pointer raw bit pattern instead of its numeric value (#54514)
  _Files: `vllm/v1/worker/gpu/model_states/prompt_embeds.py`_
- **2026-09-24** [`23110a0c9e`](https://github.com/vllm-project/vllm/commit/23110a0c9e) [#58275](https://github.com/vllm-project/vllm/pull/58275)
  [Bugfix] Capture prefill kernels for mixed FULL graphs (#58275)
  _Files: `tests/compile/fullgraph/test_full_cudagraph.py`, `tests/v1/cudagraph/test_cudagraph_manager.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/cudagraph_utils.py`_
- **2026-09-24** [`a5603f21ae`](https://github.com/vllm-project/vllm/commit/a5603f21ae) [#58330](https://github.com/vllm-project/vllm/pull/58330)
  [Rust Frontend] Recognize new frontend-owned serve args as unsupported or no-op (#58330)
  _Files: `rust/src/cmd/src/cli/unsupported.rs`_
- **2026-09-24** [`bcdacfc1ff`](https://github.com/vllm-project/vllm/commit/bcdacfc1ff) [#55612](https://github.com/vllm-project/vllm/pull/55612)
  [Test][Determinism] Cover chunked prefill in the batch-invariance suite (#55612)
  _Files: `tests/v1/determinism/test_batch_invariance.py`_
- **2026-09-23** [`310f15d354`](https://github.com/vllm-project/vllm/commit/310f15d354) [#58462](https://github.com/vllm-project/vllm/pull/58462)
  [Bugfix][MRV2] Align dummy idx_mapping dtype to avoid runtime jit (#58462)
  _Files: `vllm/v1/worker/gpu/input_batch.py`_
- **2026-09-23** [`97b1b12117`](https://github.com/vllm-project/vllm/commit/97b1b12117) [#55936](https://github.com/vllm-project/vllm/pull/55936)
  [Docs] Fix docstring typos (output_dytpe, kwrags, Abbrivations) (#55936)
  _Files: `vllm/transformers_utils/processors/ovis.py`, `vllm/transformers_utils/processors/ovis2_5.py`, `vllm/v1/core/kv_cache_manager.py`_
- **2026-09-23** [`73c59d365b`](https://github.com/vllm-project/vllm/commit/73c59d365b) [#55721](https://github.com/vllm-project/vllm/pull/55721)
  [XPU] Wire up SYCL apply_rotary_emb kernel in ApplyRotaryEmb (#55721)
  _Files: `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/_xpu_ops.py`, `vllm/model_executor/layers/rotary_embedding/common.py`_
- **2026-09-23** [`94f4170df3`](https://github.com/vllm-project/vllm/commit/94f4170df3) [#55891](https://github.com/vllm-project/vllm/pull/55891)
  [Bugfix] Set worker runtime threads before profiling and compilation (#55891)
  _Files: `tests/v1/worker/test_gpu_worker.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-09-23** [`826e300cde`](https://github.com/vllm-project/vllm/commit/826e300cde) [#58212](https://github.com/vllm-project/vllm/pull/58212)
  [Bugfix] Skip VllmConfig re-validation for with_hf_config submodel views (#58212)
  _Files: `tests/test_config.py`, `vllm/config/model.py`, `vllm/config/vllm.py`_
- **2026-09-22** [`5c3b61e9c4`](https://github.com/vllm-project/vllm/commit/5c3b61e9c4) [#58197](https://github.com/vllm-project/vllm/pull/58197)
  [Core] Disable JIT warmup in eager mode (#58197)
  _Files: `vllm/config/vllm.py`_
- **2026-09-22** [`01e15bc94c`](https://github.com/vllm-project/vllm/commit/01e15bc94c) [#58189](https://github.com/vllm-project/vllm/pull/58189)
  [Bugfix] Backport Inductor custom-op pattern matching fix (#58189)
  _Files: `tests/compile/test_config.py`, `vllm/env_override.py`_
- **2026-09-22** [`71a2392845`](https://github.com/vllm-project/vllm/commit/71a2392845) [#58149](https://github.com/vllm-project/vllm/pull/58149)
  [Bugfix][V1] Read ModelState max_model_len from model config (#58149)
  _Files: `tests/v1/worker/test_mamba_hybrid_model_state.py`, `vllm/v1/worker/gpu/model_states/interface.py`_
- **2026-09-22** [`415e11c6f1`](https://github.com/vllm-project/vllm/commit/415e11c6f1) [#55146](https://github.com/vllm-project/vllm/pull/55146)
  [Bugfix][V1] Honor enable_jit_warmup for V2 kernel warmup (#55146)
  _Files: `vllm/v1/worker/gpu_worker.py`_
- **2026-09-22** [`bc162b3f92`](https://github.com/vllm-project/vllm/commit/bc162b3f92) [#57834](https://github.com/vllm-project/vllm/pull/57834)
  [MRV2] Release weight offloader on shutdown (#57834)
  _Files: `vllm/model_executor/offloader/base.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-09-22** [`f944491db9`](https://github.com/vllm-project/vllm/commit/f944491db9) [#58179](https://github.com/vllm-project/vllm/pull/58179)
  [Bugfix] batch_invariant: keep non-AllReduce collectives enabled on NCCL >= 2.31 (#58179)
  _Files: `vllm/model_executor/determinism/batch_invariant.py`_
- **2026-09-22** [`c024cfdb02`](https://github.com/vllm-project/vllm/commit/c024cfdb02) [#57386](https://github.com/vllm-project/vllm/pull/57386)
  [Fast Start] Support data parallelism in the weight cache daemon  (#57386)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/model_executor/model_loader/weight_cache/daemon.py`, `vllm/model_executor/model_loader/weight_cache/ipc_loader.py`, `vllm/model_executor/model_loader/weight_cache/protocol.py`_
- **2026-09-22** [`c42f5285ec`](https://github.com/vllm-project/vllm/commit/c42f5285ec) [#58073](https://github.com/vllm-project/vllm/pull/58073)
  [Bugfix] prioritize architecture capability before DeepGEMM availability check (#58073)
  _Files: `vllm/utils/deep_gemm.py`_
- **2026-09-22** [`feb87b1934`](https://github.com/vllm-project/vllm/commit/feb87b1934) [#58150](https://github.com/vllm-project/vllm/pull/58150)
  [Bugfix] Narrow AuxOutput KV restrictions to known PD connectors (#58150)
  _Files: `tests/config/test_aux_output_config.py`, `vllm/config/vllm.py`_
- **2026-09-22** [`5c121e962a`](https://github.com/vllm-project/vllm/commit/5c121e962a) [#58166](https://github.com/vllm-project/vllm/pull/58166)
  [SpecDecode] Restore residual-logits comments in _resample_kernel (#58166)
  _Files: `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-09-22** [`1ea7c63f4a`](https://github.com/vllm-project/vllm/commit/1ea7c63f4a) [#56250](https://github.com/vllm-project/vllm/pull/56250)
  [Bugfix][Structured Output] Disallow MRV1 + PP>1 + async sched + structured output (#56250)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-09-22** [`e548298f81`](https://github.com/vllm-project/vllm/commit/e548298f81) [#47450](https://github.com/vllm-project/vllm/pull/47450)
  [Bugfix][Structured Outputs] Reject empty `structural_tag` at request validation (#47450)
  _Files: `tests/v1/structured_output/test_validation.py`, `vllm/sampling_params.py`_
- **2026-09-22** [`9815732c16`](https://github.com/vllm-project/vllm/commit/9815732c16) [#55931](https://github.com/vllm-project/vllm/pull/55931)
  [BugFix][Core] Make the structured-output grammar poll non-blocking (#55931)
  _Files: `tests/v1/structured_output/test_request.py`, `vllm/v1/structured_output/request.py`_
- **2026-09-21** [`7d06dd1ffa`](https://github.com/vllm-project/vllm/commit/7d06dd1ffa) [#57737](https://github.com/vllm-project/vllm/pull/57737)
  [Pooling] MRV2 pooling shutdown model ref (#57737)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-09-21** [`15859bb3a1`](https://github.com/vllm-project/vllm/commit/15859bb3a1) [#57545](https://github.com/vllm-project/vllm/pull/57545)
  [Test] Organize structured output utility tests (#57545)
  _Files: `tests/v1/structured_output/test_utils.py`_
- **2026-09-21** [`3c84ad13ed`](https://github.com/vllm-project/vllm/commit/3c84ad13ed) [#48416](https://github.com/vllm-project/vllm/pull/48416)
  [Bugfix] Fix xgrammar feature gate bypass when JSON Schema type is a list (#48416)
  _Files: `tests/v1/structured_output/test_utils.py`, `tests/v1/structured_output/test_validation.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-09-21** [`8ec00ec2bc`](https://github.com/vllm-project/vllm/commit/8ec00ec2bc) [#57868](https://github.com/vllm-project/vllm/pull/57868)
  [Tests] Release HF embedding weights after prompt extraction (#57868)
  _Files: `tests/models/language/generation/test_common.py`_
- **2026-09-21** [`3df4ae153e`](https://github.com/vllm-project/vllm/commit/3df4ae153e) [#57783](https://github.com/vllm-project/vllm/pull/57783)
  [Core][KDA] Generalize Mamba prefill checkpoint builder and exporter (#57783)
  _Files: `tests/models/kimi_k3/test_kda.py`, `vllm/model_executor/layers/mamba/checkpoint.py`, `vllm/model_executor/layers/mamba/kda_checkpoint.py`, `vllm/models/kimi_k3/nvidia/kda.py` _+1 more__

## Attention  (42 commits)

- **2026-09-28** [`94d1462924`](https://github.com/vllm-project/vllm/commit/94d1462924) [#58814](https://github.com/vllm-project/vllm/pull/58814)
  [Bugfix][Kimi-K3] Refresh DSpark context KV cache pointers after the KV cache is re-bound (#58814)
  _Files: `vllm/models/kimi_k3/nvidia/dspark_mla.py`_
- **2026-09-28** [`522101f6ed`](https://github.com/vllm-project/vllm/commit/522101f6ed) [#56711](https://github.com/vllm-project/vllm/pull/56711)
  [Multimodal] Avoid extra d2d for encoder cudagraph with fused input norm (#56711)
  _Files: `vllm/model_executor/layers/fusion/mm_input_norm.py`, `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/v1/attention/ops/vit_attn_wrappers.py`_
- **2026-09-28** [`004e37ece2`](https://github.com/vllm-project/vllm/commit/004e37ece2) [#58557](https://github.com/vllm-project/vllm/pull/58557)
  [Misc] Name each backend and its kernel block sizes in block-size errors (#58557)
  _Files: `tests/v1/worker/test_attn_utils.py`, `tests/v1/worker/test_gpu_model_runner.py`, `vllm/v1/attention/backend.py`, `vllm/v1/worker/utils.py`_
- **2026-09-28** [`dd3bc9c72f`](https://github.com/vllm-project/vllm/commit/dd3bc9c72f) [#58762](https://github.com/vllm-project/vllm/pull/58762)
  [Perf][MRV2] Reuse Mamba/GDN metadata across KV cache groups (#58762)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`, `tests/v1/attention/test_gdn_metadata_builder.py`, `tests/v1/worker/test_gpu_autoregressive_speculator.py`, `vllm/v1/attention/backends/gdn_attn.py` _+1 more__
- **2026-09-27** [`0376f81530`](https://github.com/vllm-project/vllm/commit/0376f81530) [#57214](https://github.com/vllm-project/vllm/pull/57214)
  [Perf][Pooling] Avoid blocking seq_lens GPU-to-CPU copy for pooling in FlashInfer metadata builder (#57214)
  _Files: `tests/v1/attention/test_attention_backends.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-09-27** [`c8d7a7dd13`](https://github.com/vllm-project/vllm/commit/c8d7a7dd13) [#58684](https://github.com/vllm-project/vllm/pull/58684)
  [Perf][Attention] Remove D2H sync from FlashInfer SM90 sparse MLA plan under async scheduling (#58684)
  _Files: `tests/v1/attention/test_flashinfer_mla_sparse_sm90.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse_sm90.py`_
- **2026-09-27** [`24c9772d19`](https://github.com/vllm-project/vllm/commit/24c9772d19) [#54967](https://github.com/vllm-project/vllm/pull/54967)
  [Attention][CPU] Use zentorch SDPA for CPU MLA prefill (#54967)
  _Files: `tests/v1/attention/test_cpu_mla_backend.py`, `tests/v1/attention/test_mla_prefill_selector.py`, `vllm/v1/attention/backends/mla/prefill/registry.py`, `vllm/v1/attention/backends/mla/prefill/selector.py` _+1 more__
- **2026-09-27** [`a9eafde59c`](https://github.com/vllm-project/vllm/commit/a9eafde59c) [#58634](https://github.com/vllm-project/vllm/pull/58634)
  [Perf][DSv4.1] Fuse small-batch WO-A with inverse RoPE and MXFP8 quant on SM100/SM103 (#58634)
  _Files: `tests/kernels/test_fused_inv_rope_fp8_quant.py`, `vllm/models/deepseek_v41/attention.py`, `vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v41/nvidia/flashmla.py` _+2 more__
- **2026-09-27** [`7a877ae34d`](https://github.com/vllm-project/vllm/commit/7a877ae34d) [#57105](https://github.com/vllm-project/vllm/pull/57105)
  [Qwen3.8-Flash-Next] Avoid memory fragmentation in QSA indexer logits workspace (#57105)
  _Files: `vllm/models/qwen4_exp/nvidia/ops/qsa_indexer.py`_
- **2026-09-26** [`4be061c5af`](https://github.com/vllm-project/vllm/commit/4be061c5af) [#58846](https://github.com/vllm-project/vllm/pull/58846)
  [Kernel] Bump FlashKDA to keep the recurrent state in fp32 (#58846)
  _Files: `cmake/external_projects/flashkda.cmake`_
- **2026-09-26** [`927c87b347`](https://github.com/vllm-project/vllm/commit/927c87b347) [#56723](https://github.com/vllm-project/vllm/pull/56723)
  [PCP][DCP] Support DCP target model with non-DCP Dspark (#56723)
  _Files: `tests/v1/attention/test_attention_backends.py`, `tests/v1/attention/test_group_head_counts.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_prefix_caching.py` _+28 more__
- **2026-09-26** [`ddd6fbca14`](https://github.com/vllm-project/vllm/commit/ddd6fbca14) [#58316](https://github.com/vllm-project/vllm/pull/58316)
  [Bugfix][Frontend][Rust Frontend] Update DeepSeek V4.1 Flash reasoning effort mappings (#58316)
  _Files: `rust/src/chat/src/renderer/deepseek.rs`, `rust/src/chat/src/renderer/deepseek_v41/fixtures/test_output_1.txt`, `rust/src/chat/src/renderer/deepseek_v41/fixtures/test_output_2.txt`, `rust/src/chat/src/renderer/deepseek_v41/fixtures/test_output_developer_tools.txt` _+5 more__
- **2026-09-25** [`c88f4824ff`](https://github.com/vllm-project/vllm/commit/c88f4824ff) [#58450](https://github.com/vllm-project/vllm/pull/58450)
  [GLM5.3 Perf] Optimize glm 5.3 metadata op, 1.6~4.8x kernel level performance improvement (#58450)
  _Files: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/model_executor/layers/attention/sparse_mla_attention.py`, `vllm/v1/attention/backends/mla/flashattn_mla_sparse.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse.py`_
- **2026-09-25** [`2edbb32e58`](https://github.com/vllm-project/vllm/commit/2edbb32e58) [#58704](https://github.com/vllm-project/vllm/pull/58704)
  [Bugfix][GLM-5.3-Flash] SM90 sparse MLA: index_kpool mismatch leads to corruption via unread query token (#58704)
  _Files: `tests/v1/attention/test_flashinfer_mla_sparse_sm90.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse_sm90.py`_
- **2026-09-25** [`73a78e6f1f`](https://github.com/vllm-project/vllm/commit/73a78e6f1f) [#57934](https://github.com/vllm-project/vllm/pull/57934)
  [SpecDecode] Add LiLiCorr drafter (#57934)
  _Files: `docs/features/speculative_decoding/README.md`, `docs/features/speculative_decoding/lilicorr.md`, `tests/models/registry.py`, `tests/test_config.py` _+17 more__
- **2026-09-25** [`5ff3bbfb08`](https://github.com/vllm-project/vllm/commit/5ff3bbfb08) [#58621](https://github.com/vllm-project/vllm/pull/58621)
  [Perf][DSv4] Fuse inverse RoPE + FP8 quant into FlashInfer sparse MLA (#58621)
  _Files: `tests/kernels/attention/test_flashmla_sparse.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` _+1 more__
- **2026-09-25** [`29468dde8b`](https://github.com/vllm-project/vllm/commit/29468dde8b) [#55528](https://github.com/vllm-project/vllm/pull/55528)
  [Bugfix][KV Cache][MLA] Align packed block strides for V3.2 sparse MLA (#55528)
  _Files: `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_sparse_mla_kv_cache_layout.py`, `tests/v1/core/test_contiguous_kv_packing.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+2 more__
- **2026-09-25** [`155b988373`](https://github.com/vllm-project/vllm/commit/155b988373) [#58496](https://github.com/vllm-project/vllm/pull/58496)
  [CI] Run DFlash2 NVFP4 acceptance test on B200; skip it on H200 35GB MIG (#58496)
  _Files: `.buildkite/test_areas/spec_decode.yaml`_
- **2026-09-25** [`34ee85d5ca`](https://github.com/vllm-project/vllm/commit/34ee85d5ca) [#49371](https://github.com/vllm-project/vllm/pull/49371)
  [Perf] Batch Mamba2 prefill SSM state saves, removing GPU<->CPU syncs (#49371)
  _Files: `tests/v1/attention/test_mamba_update_block_table.py`, `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/v1/attention/backends/mamba2_attn.py`, `vllm/v1/attention/backends/mamba_attn.py`_
- **2026-09-25** [`39724758e7`](https://github.com/vllm-project/vllm/commit/39724758e7) [#55270](https://github.com/vllm-project/vllm/pull/55270)
  [Bugfix] GLM-5.3-Flash: launch the kpool paged MQA logits in the varlen mode its schedule was built with (#55270)
  _Files: `vllm/models/glm5next/nvidia/sparse_indexer.py`_
- **2026-09-24** [`04730e8270`](https://github.com/vllm-project/vllm/commit/04730e8270) [#57632](https://github.com/vllm-project/vllm/pull/57632)
  [DFlash] Capture the context K/V precompute in the draft CUDA graph (#57632)
  _Files: `vllm/v1/worker/gpu/spec_decode/dflash/cudagraph.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`_
- **2026-09-24** [`26f49e336a`](https://github.com/vllm-project/vllm/commit/26f49e336a) [#57918](https://github.com/vllm-project/vllm/pull/57918)
  [Perf][Attention] Bound FlashInfer prefill dequantization scratch (#57918)
  _Files: `tests/v1/attention/test_trtllm_attention_integration.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-09-24** [`5963795ec7`](https://github.com/vllm-project/vllm/commit/5963795ec7) [#54508](https://github.com/vllm-project/vllm/pull/54508)
  [Attention][CPU] Run Zen CPU encoder attention on zentorch SDPA (#54508)
  _Files: `setup.py`, `tests/kernels/attention/test_cpu_attn.py`, `vllm/v1/attention/backends/cpu_attn.py`, `vllm/v1/attention/backends/zentorch_sdpa.py` _+1 more__
- **2026-09-24** [`67ddac3ea8`](https://github.com/vllm-project/vllm/commit/67ddac3ea8) [#53300](https://github.com/vllm-project/vllm/pull/53300)
  [CPU][GDN] Support NIXL DS convolution-state layout (#53300)
  _Files: `tests/kernels/mamba/cpu/test_cpu_gdn_ops.py`, `tests/platforms/test_cpu.py`, `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py`, `vllm/platforms/cpu.py`_
- **2026-09-24** [`9ef37771be`](https://github.com/vllm-project/vllm/commit/9ef37771be) [#58215](https://github.com/vllm-project/vllm/pull/58215)
  [Bugfix][DSA] Bound DeepSelect sentinel columns in the sparse top-k remap (#58215)
  _Files: `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`_
- **2026-09-23** [`e26547adfb`](https://github.com/vllm-project/vllm/commit/e26547adfb) [#49845](https://github.com/vllm-project/vllm/pull/49845)
  [Bugfix] Pick a KV block size supported by every attention backend (#49845)
  _Files: `tests/v1/worker/test_gpu_model_runner.py`, `vllm/platforms/cpu.py`, `vllm/platforms/interface.py`_
- **2026-09-23** [`88afb9dcac`](https://github.com/vllm-project/vllm/commit/88afb9dcac) [#56252](https://github.com/vllm-project/vllm/pull/56252)
  [CPU] Adds support for fp32 attention sinks (#56252)
  _Files: `csrc/cpu/cpu_attn.cpp`, `csrc/cpu/cpu_attn_impl.hpp`, `tests/kernels/attention/test_cpu_attn.py`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-09-23** [`c843f0cab7`](https://github.com/vllm-project/vllm/commit/c843f0cab7) [#55277](https://github.com/vllm-project/vllm/pull/55277)
  [Bugfix][SM120][MLA] Support NoPE sparse MLA (GLM-5.3-Flash) on the FlashInfer SM120 backend (#55277)
  _Files: `csrc/libtorch_stable/cache_kernels.cu`, `tests/kernels/attention/test_cache.py`_
- **2026-09-23** [`afec265bca`](https://github.com/vllm-project/vllm/commit/afec265bca) [#57980](https://github.com/vllm-project/vllm/pull/57980)
  [MRV2] Miscellaneous code cleanup (#57980)
  _Files: `tests/v1/spec_decode/test_eagle_draft_attn_metadata.py`, `tests/v1/worker/test_gpu_input_batch_v2.py`, `tests/v1/worker/test_gpu_pcp_manager.py`, `tests/v1/worker/test_gpu_ubatch_slicing.py` _+20 more__
- **2026-09-23** [`6632ed559e`](https://github.com/vllm-project/vllm/commit/6632ed559e) [#58169](https://github.com/vllm-project/vllm/pull/58169)
  [Perf][Attention] Avoid CPU-GPU sync in DCP sequence lengths (#58169)
  _Files: `vllm/v1/attention/backends/utils.py`_
- **2026-09-23** [`973a3be780`](https://github.com/vllm-project/vllm/commit/973a3be780) [#57732](https://github.com/vllm-project/vllm/pull/57732)
  [Refactor][Quantization] Make FP8 and MLA weight transforms reusable pure functions (#57732)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/modelopt.py` _+2 more__
- **2026-09-22** [`066ee91197`](https://github.com/vllm-project/vllm/commit/066ee91197) [#56579](https://github.com/vllm-project/vllm/pull/56579)
  [Bugfix][Attention] Avoid NaN in the Triton softcap for large attention logits (#56579)
  _Files: `tests/kernels/attention/test_triton_unified_attention.py`, `vllm/v1/attention/ops/triton_attention_helpers.py`_
- **2026-09-22** [`c9b34fdb2d`](https://github.com/vllm-project/vllm/commit/c9b34fdb2d) [#58061](https://github.com/vllm-project/vllm/pull/58061)
  [Bugfix][GLM-5.3-Flash] Run the dense MLP layers on the sequence-parallel shard (#58061)
  _Files: `tests/models/glm5next/test_sequence_parallel.py`, `vllm/models/glm5next/common/model.py`_
- **2026-09-22** [`91d7324cb1`](https://github.com/vllm-project/vllm/commit/91d7324cb1) [#55385](https://github.com/vllm-project/vllm/pull/55385)
  [perf] wire FA and FlashMLA for sm90 GLM5Next NoPE SparseMLA (#55385)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`, `tests/v1/attention/test_flashmla_nope_sm90_backend_selection.py`, `vllm/v1/attention/backends/mla/flashattn_mla_sparse.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-09-22** [`f92b78f6ef`](https://github.com/vllm-project/vllm/commit/f92b78f6ef) [#57428](https://github.com/vllm-project/vllm/pull/57428)
  [Kernel][DSV4.1] Fuse MXFP8 wo_b GEMM with sequence-parallel reduce-scatter (#57428)
  _Files: `.buildkite/test_areas/distributed.yaml`, `benchmarks/kernels/benchmark_gemm_rs_ar.py`, `benchmarks/kernels/benchmark_kimi_k3_gemm_rs_ar.py`, `tests/kernels/test_gemm_rs_ar.py` _+14 more__
- **2026-09-22** [`0961bbae28`](https://github.com/vllm-project/vllm/commit/0961bbae28) [#58065](https://github.com/vllm-project/vllm/pull/58065)
  [Spec Decode] Enable async scheduling for DFlash (#58065)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-09-22** [`c4d424c2e2`](https://github.com/vllm-project/vllm/commit/c4d424c2e2) [#56448](https://github.com/vllm-project/vllm/pull/56448)
  [Bugfix][Spec Decode] Cap DFlash/DSpark profiling query batch (#56448)
  _Files: `tests/v1/spec_decode/test_dflash_profile.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/spec_decode/speculator.py`_
- **2026-09-22** [`79468c20ef`](https://github.com/vllm-project/vllm/commit/79468c20ef) [#51565](https://github.com/vllm-project/vllm/pull/51565)
  [Bugfix][GDN] Fix stateless first-chunk classification (#51565)
  _Files: `tests/v1/attention/test_gdn_metadata_builder.py`, `vllm/v1/attention/backends/gdn_attn.py`_
- **2026-09-22** [`a369a7becc`](https://github.com/vllm-project/vllm/commit/a369a7becc) [#57458](https://github.com/vllm-project/vllm/pull/57458)
  [Perf][Attention] Reduce GLM sparse MLA preparation overhead (#57458)
  _Files: `tests/kernels/attention/test_flashinfer_mla_decode.py`, `tests/kernels/test_concat_mla_q.py`, `tests/v1/attention/test_indexer_dcp_localize.py`, `tests/v1/attention/test_sparse_mla_backends.py` _+3 more__
- **2026-09-21** [`8c0825090d`](https://github.com/vllm-project/vllm/commit/8c0825090d) [#57389](https://github.com/vllm-project/vllm/pull/57389)
  [Bugfix][NIXL] Fix DCP pulls across MLA cache regions (#57389)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py`_
- **2026-09-21** [`97dc6b19d2`](https://github.com/vllm-project/vllm/commit/97dc6b19d2) [#57885](https://github.com/vllm-project/vllm/pull/57885)
  [Perf][Attention] Avoid redundant sparse attention metadata operations (#57885)
  _Files: `vllm/v1/attention/backends/mla/indexer.py`, `vllm/v1/attention/backends/mla/sparse_swa.py`_
- **2026-09-21** [`86ce4d10e2`](https://github.com/vllm-project/vllm/commit/86ce4d10e2) [#57811](https://github.com/vllm-project/vllm/pull/57811)
  [BUGFIX][HY4]  Record indexer completion event for full CUDA graph capture (#57811)
  _Files: `vllm/models/hy_v4/nvidia/attention.py`_

## Multimodal  (37 commits)

- **2026-09-28** [`cd63bf9996`](https://github.com/vllm-project/vllm/commit/cd63bf9996) [#57461](https://github.com/vllm-project/vllm/pull/57461)
  [Bugfix] Use the correct repository revision for secondary artifact loaders (#57461)
  _Files: `vllm/model_executor/models/funaudiochat.py`, `vllm/renderers/hf.py`_
- **2026-09-28** [`ccfd1cea75`](https://github.com/vllm-project/vllm/commit/ccfd1cea75) [#58796](https://github.com/vllm-project/vllm/pull/58796)
  [CPU] Include vLLM Recipes tooling in release image to deploy models using vLLM Recipes (#58796)
  _Files: `docker/Dockerfile.cpu`, `docs/getting_started/installation/cpu.x86.inc.md`, `docs/models/hardware_supported_models/cpu.md`, `tools/recipes/README.md`_
- **2026-09-28** [`fd2f3fcfa5`](https://github.com/vllm-project/vllm/commit/fd2f3fcfa5) [#58693](https://github.com/vllm-project/vllm/pull/58693)
  [CPU] Add video inferencing via torchcodec on s390x (#58693)
  _Files: `docker/Dockerfile.s390x`, `docs/getting_started/installation/cpu.s390x.inc.md`, `requirements/cpu.txt`_
- **2026-09-28** [`0da126676e`](https://github.com/vllm-project/vllm/commit/0da126676e) [#58900](https://github.com/vllm-project/vllm/pull/58900)
  [Bugfix] Fix the two multimodal root tests that fail on main (OpenPangu-VL embed merge, MiMo sink test fixture) (#58900)
  _Files: `tests/models/multimodal/test_mimo_v2_omni.py`, `vllm/model_executor/models/openpangu_vl.py`_
- **2026-09-26** [`7d8c5fe9a9`](https://github.com/vllm-project/vllm/commit/7d8c5fe9a9) [#58499](https://github.com/vllm-project/vllm/pull/58499)
  [Bugfix][DSV4.1] Avoid host sync in ViT CUDA graph replay metadata (#58499)
  _Files: `vllm/models/deepseek_v4/common/vision.py`, `vllm/models/deepseek_v41/common/vl_cudagraph.py`_
- **2026-09-26** [`31f2e70cd3`](https://github.com/vllm-project/vllm/commit/31f2e70cd3) [#58830](https://github.com/vllm-project/vllm/pull/58830)
  [Security] Gate per-request multimodal processor kwargs (#58830)
  _Files: `docs/usage/security.md`, `rust/src/cmd/src/cli/unsupported.rs`, `tests/engine/test_arg_utils.py`, `tests/entrypoints/multimodal/openai/chat_completion/test_audio_in_video.py` _+13 more__
- **2026-09-25** [`b6761e8ded`](https://github.com/vllm-project/vllm/commit/b6761e8ded) [#57241](https://github.com/vllm-project/vllm/pull/57241)
  [Bugfix] Default missing detail for Responses API input images (#57241)
  _Files: `tests/tool_use/test_responses_request_validations.py`, `vllm/entrypoints/openai/responses/protocol.py`_
- **2026-09-25** [`8a269919f4`](https://github.com/vllm-project/vllm/commit/8a269919f4) [#56798](https://github.com/vllm-project/vllm/pull/56798)
  [MM] Add Triton kernel for mm_input_normal. (#56798)
  _Files: `docs/design/mm_processing.md`, `tests/model_executor/layers/test_mm_input_norm.py`, `tests/models/multimodal/processing/test_qwen2_vl.py`, `tests/models/test_vision.py` _+5 more__
- **2026-09-25** [`16070ed7e9`](https://github.com/vllm-project/vllm/commit/16070ed7e9) [#58526](https://github.com/vllm-project/vllm/pull/58526)
  [Minimax-M3][Perf] Use triton_mrope for vision tower + int64 offset fix for triton_mrope (#58526)
  _Files: `tests/kernels/core/test_mrope.py`, `vllm/model_executor/layers/rotary_embedding/mrope.py`, `vllm/model_executor/layers/rotary_embedding/mrope_vit_setup.py`, `vllm/models/minimax_m3/common/vision_tower.py`_
- **2026-09-25** [`ade1056ee5`](https://github.com/vllm-project/vllm/commit/ade1056ee5) [#58527](https://github.com/vllm-project/vllm/pull/58527)
  [Kimi-K3][Perf] Dispatch GEMM for vision patch embedder (#58527)
  _Files: `tests/model_executor/layers/test_conv.py`, `vllm/model_executor/models/kimi_k25_vit.py`_
- **2026-09-24** [`f6aa2919bc`](https://github.com/vllm-project/vllm/commit/f6aa2919bc) [#58288](https://github.com/vllm-project/vllm/pull/58288)
  [Bugfix][Core] Keep every multimodal feature in the partial-block KV event (#58288)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_primitives.py`, `vllm/v1/core/block_pool.py`_
- **2026-09-24** [`bd4cb3fe4e`](https://github.com/vllm-project/vllm/commit/bd4cb3fe4e) [#52623](https://github.com/vllm-project/vllm/pull/52623)
  [BUGFIX] fix ovis2_5 multimodal tokens (#52623)
  _Files: `vllm/model_executor/models/ovis2_5.py`, `vllm/transformers_utils/processors/ovis2_5.py`_
- **2026-09-24** [`5b3f280a6d`](https://github.com/vllm-project/vllm/commit/5b3f280a6d) [#48760](https://github.com/vllm-project/vllm/pull/48760)
  [Bugfix] Count unsplit Idefics3 image patches (#48760)
  _Files: `tests/models/multimodal/processing/test_smolvlm.py`, `vllm/model_executor/models/idefics3.py`_
- **2026-09-24** [`d636456b1f`](https://github.com/vllm-project/vllm/commit/d636456b1f) [#58545](https://github.com/vllm-project/vllm/pull/58545)
  [Frontend] Remove the slow tokenizer mode (#58545)
  _Files: `benchmarks/backend_request_func.py`, `examples/generate/multimodal/vision_language_multi_image_offline.py`, `rust/src/bench/src/cli.rs`, `tests/renderers/test_token_offsets.py` _+8 more__
- **2026-09-24** [`344fcc252a`](https://github.com/vllm-project/vllm/commit/344fcc252a) [#56092](https://github.com/vllm-project/vllm/pull/56092)
  [Bugfix] Resolve the Hub revision once per repo (#56092)
  _Files: `tests/test_config.py`, `tests/transformers_utils/test_config.py`, `vllm/config/model.py`, `vllm/model_executor/model_loader/runai_streamer_loader.py` _+1 more__
- **2026-09-24** [`484c211fe8`](https://github.com/vllm-project/vllm/commit/484c211fe8) [#57347](https://github.com/vllm-project/vllm/pull/57347)
  [Bugfix][Pooling] Fix JinaVL label configuration and restore multimodal tests (#57347)
  _Files: `tests/models/multimodal/pooling/test_jinavl_reranker.py`, `vllm/model_executor/models/config.py`_
- **2026-09-24** [`f5a78f2ad7`](https://github.com/vllm-project/vllm/commit/f5a78f2ad7) [#58460](https://github.com/vllm-project/vllm/pull/58460)
  [Multimodal] Reuse the supplied tokenizer in the MiniMax-M3 VL processor (#58460)
  _Files: `vllm/transformers_utils/processors/minimax_m3.py`_
- **2026-09-24** [`e430f7421f`](https://github.com/vllm-project/vllm/commit/e430f7421f) [#58378](https://github.com/vllm-project/vllm/pull/58378)
  [Bugfix][Rust Frontend] Prevent MM timing from enabling debug tracing (#58378)
  _Files: `rust/src/chat/Cargo.toml`, `rust/src/chat/src/multimodal/timing.rs`, `rust/src/tracing/src/timing.rs`_
- **2026-09-24** [`00b7847c80`](https://github.com/vllm-project/vllm/commit/00b7847c80) [#58512](https://github.com/vllm-project/vllm/pull/58512)
  [Perf] Use Conv3dLayer for MiniMax M3 patch embedding (#58512)
  _Files: `tests/model_executor/layers/test_conv.py`, `vllm/models/minimax_m3/common/vision_tower.py`_
- **2026-09-24** [`cf78797cb7`](https://github.com/vllm-project/vllm/commit/cf78797cb7) [#57634](https://github.com/vllm-project/vllm/pull/57634)
  [Rust Frontend] Pass vision preprocessing context for Nemotron-H (#57634)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/multimodal.rs` _+4 more__
- **2026-09-24** [`a1b6763df6`](https://github.com/vllm-project/vllm/commit/a1b6763df6) [#58311](https://github.com/vllm-project/vllm/pull/58311)
  [Rust Frontend] Accept custom chat roles for HF templates (#58311)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/renderer/deepseek.rs`, `rust/src/chat/src/renderer/deepseek_v32/encoding.rs` _+10 more__
- **2026-09-22** [`ecdd11d0e0`](https://github.com/vllm-project/vllm/commit/ecdd11d0e0) [#58204](https://github.com/vllm-project/vllm/pull/58204)
  [CI] Build the torch-nightly image on Ubuntu 24.04 (#58204)
  _Files: `.buildkite/image_build/image_build_torch_nightly.sh`_
- **2026-09-22** [`81d7293c21`](https://github.com/vllm-project/vllm/commit/81d7293c21) [#58109](https://github.com/vllm-project/vllm/pull/58109)
  [Rust Frontend] Construct model-owned vision processors through specs (#58109)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/multimodal/image.rs` _+1 more__
- **2026-09-22** [`64a48b19b4`](https://github.com/vllm-project/vllm/commit/64a48b19b4) [#58097](https://github.com/vllm-project/vllm/pull/58097)
  [CI] Emit a kernel symbol map from the csrc build (opt-in, for test selection) (#58097)
  _Files: `.buildkite/image_build/image_build.sh`, `docker/Dockerfile`, `docs/assets/contributing/dockerfile-stages-dependency.png`, `tools/ci/kernel_symbol_map.py`_
- **2026-09-22** [`a6c47fbbf4`](https://github.com/vllm-project/vllm/commit/a6c47fbbf4) [#58084](https://github.com/vllm-project/vllm/pull/58084)
  [Rust Frontend] Separate multimodal instrumentation from request timing (#58084)
  _Files: `rust/src/bench/src/mm_processor.rs`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/multimodal/audio.rs` _+5 more__
- **2026-09-22** [`a33b3bac5d`](https://github.com/vllm-project/vllm/commit/a33b3bac5d) [#47736](https://github.com/vllm-project/vllm/pull/47736)
  [Bugfix][Qwen2.5-VL] Honor video fps for temporal M-RoPE (#47736)
  _Files: `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_common.py`, `tests/models/multimodal/generation/test_qwen2_5_vl.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py` _+3 more__
- **2026-09-22** [`f84325c48c`](https://github.com/vllm-project/vllm/commit/f84325c48c) [#51922](https://github.com/vllm-project/vllm/pull/51922)
  [Frontend][Rust] Add mm-processor benchmark for Rust frontend (#51922)
  _Files: `rust/Cargo.lock`, `rust/src/bench/AGENTS.md`, `rust/src/bench/Cargo.toml`, `rust/src/bench/README.md` _+10 more__
- **2026-09-21** [`8644d2af2f`](https://github.com/vllm-project/vllm/commit/8644d2af2f) [#57871](https://github.com/vllm-project/vllm/pull/57871)
  [CI][Build] Harden triton-cpu sleef submodule fetch in CPU image build (#57871)
  _Files: `docker/Dockerfile.cpu`_
- **2026-09-21** [`9fe1cbd463`](https://github.com/vllm-project/vllm/commit/9fe1cbd463) [#55608](https://github.com/vllm-project/vllm/pull/55608)
  [Docker] Use zstd for CI images and offer a Docker Hub variant (#55608)
  _Files: `.buildkite/image_build/image_build.sh`, `.buildkite/image_build/zstd.hcl`, `.buildkite/scripts/publish-release-images.sh`, `.buildkite/scripts/publish-zstd-image.sh`_
- **2026-09-21** [`7853700d4c`](https://github.com/vllm-project/vllm/commit/7853700d4c) [#57967](https://github.com/vllm-project/vllm/pull/57967)
  [MM] Move get_dummy_processor_inputs into MM processor (#57967)
  _Files: `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_tensor_schema.py`, `tests/renderers/test_warmup.py`, `vllm/model_executor/models/hyperclovax_vision_v2.py` _+6 more__
- **2026-09-21** [`4e61ad8ee1`](https://github.com/vllm-project/vllm/commit/4e61ad8ee1) [#55767](https://github.com/vllm-project/vllm/pull/55767)
  [Bugfix] unskip InternViT test for transformers v5 compatibility (#55767)
  _Files: `tests/models/multimodal/pooling/test_intern_vit.py`_
- **2026-09-21** [`c8824a1e42`](https://github.com/vllm-project/vllm/commit/c8824a1e42) [#57913](https://github.com/vllm-project/vllm/pull/57913)
  [MM] Move `supports_multimodal_inputs` and cache out of registry (#57913)
  _Files: `tests/config/test_multimodal_config.py`, `tests/entrypoints/generate/generative_scoring/test_generative_scoring.py`, `tests/entrypoints/openai/chat_completion/test_chat_error.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py` _+32 more__
- **2026-09-21** [`606d124b37`](https://github.com/vllm-project/vllm/commit/606d124b37) [#57234](https://github.com/vllm-project/vllm/pull/57234)
  [Bugfix][Multimodal] Tolerate malformed EXIF in Molmo 2 image preprocessing (#57234)
  _Files: `vllm/model_executor/models/molmo2.py`_
- **2026-09-21** [`7268f6e38e`](https://github.com/vllm-project/vllm/commit/7268f6e38e) [#57833](https://github.com/vllm-project/vllm/pull/57833)
  [Security] Prefer fresh multimodal payloads over a stale receiver cache (#57833)
  _Files: `tests/multimodal/test_cache.py`, `vllm/multimodal/cache.py`_
- **2026-09-21** [`9598487bc1`](https://github.com/vllm-project/vllm/commit/9598487bc1) [#53758](https://github.com/vllm-project/vllm/pull/53758)
  [Bugfix][Model] Mistral3: align placeholder grid with public processor (#53758)
  _Files: `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/mistral3.py`_
- **2026-09-21** [`59f1527280`](https://github.com/vllm-project/vllm/commit/59f1527280) [#57769](https://github.com/vllm-project/vllm/pull/57769)
  [Bugfix] Fix Whisper engine crash on audio clips longer than 30s (#57769)
  _Files: `tests/models/multimodal/processing/test_whisper.py`, `vllm/model_executor/models/whisper.py`_
- **2026-09-21** [`ff0c885494`](https://github.com/vllm-project/vllm/commit/ff0c885494) [#57589](https://github.com/vllm-project/vllm/pull/57589)
  [Bugfix] DiffusionGemma: fix multimodal support (#57589)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_

## MoE / Expert Parallel  (28 commits)

- **2026-09-27** [`231fdb83cc`](https://github.com/vllm-project/vllm/commit/231fdb83cc) [#58880](https://github.com/vllm-project/vllm/pull/58880)
  [Perf][MoE] Use fused MiniMax2 routing with non-unit routed scaling (#58880)
  _Files: `tests/kernels/moe/test_flashinfer.py`, `tests/kernels/moe/test_routing.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/router/cpu_router.py` _+4 more__
- **2026-09-26** [`77871126f9`](https://github.com/vllm-project/vllm/commit/77871126f9) [#58586](https://github.com/vllm-project/vllm/pull/58586)
  [Kernel][DSV4.1] Fuse MoE finalize into the TP all-reduce + mHC boundary (#58586)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/all_reduce_mhc.cu`, `tests/distributed/test_custom_all_reduce.py`, `vllm/models/deepseek_v41/nvidia/model.py` _+4 more__
- **2026-09-26** [`3576691c42`](https://github.com/vllm-project/vllm/commit/3576691c42) [#58594](https://github.com/vllm-project/vllm/pull/58594)
  [GLM5.3 Bug] Fix sparse indexer attn topk backend selection (#58594)
  _Files: `vllm/models/deepseek_v32/attention.py`_
- **2026-09-26** [`5113cf9d16`](https://github.com/vllm-project/vllm/commit/5113cf9d16) [#58046](https://github.com/vllm-project/vllm/pull/58046)
  [Mypy] Fix mypy typing for Qwen and Qianfan models (#58046)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/qianfan_ocr.py`, `vllm/model_executor/models/qwen2.py` _+19 more__
- **2026-09-26** [`ad6817b68d`](https://github.com/vllm-project/vllm/commit/ad6817b68d) [#58720](https://github.com/vllm-project/vllm/pull/58720)
  [Perf][MoE] Index expert mapping lookups in RoutedExperts.load_weights (#58720)
  _Files: `tests/kernels/moe/test_moe_weight_loading_padded.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-09-26** [`bf93e1f92c`](https://github.com/vllm-project/vllm/commit/bf93e1f92c) [#58803](https://github.com/vllm-project/vllm/pull/58803)
  [Refactor] Remove dead tests utils (#58803)
  _Files: `tests/conftest.py`, `tests/entrypoints/serve/dev/rlhf/conftest.py`, `tests/kernels/attention/test_attention.py`, `tests/kernels/mamba/test_causal_conv1d.py` _+12 more__
- **2026-09-25** [`378504a544`](https://github.com/vllm-project/vllm/commit/378504a544) [#58635](https://github.com/vllm-project/vllm/pull/58635)
  [MoE] Defer the TRTLLM-Gen top-k finalize on the modular path (#58635)
  _Files: `tests/kernels/moe/test_flashinfer.py`, `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/kernels/moe/test_trtllm_nvfp4_moe.py`, `tests/kernels/moe/utils.py` _+22 more__
- **2026-09-25** [`3652f35e7c`](https://github.com/vllm-project/vllm/commit/3652f35e7c) [#57954](https://github.com/vllm-project/vllm/pull/57954)
  [Bugfix][Quantization] Refresh online NVFP4 scales before reload post-processing (#57954)
  _Files: `tests/kernels/moe/test_trtllm_nvfp4_moe.py`, `tests/quantization/test_online.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`, `vllm/model_executor/layers/quantization/online/nvfp4.py`_
- **2026-09-24** [`90a9515006`](https://github.com/vllm-project/vllm/commit/90a9515006) [#53585](https://github.com/vllm-project/vllm/pull/53585)
  [Cleanup] Remove online quantization support in `fp8.py` in favor of online shorthands (#53585)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`, `docs/features/quantization/llm_compressor/fp8.md`, `tests/compile/passes/test_mla_attn_quant_fusion.py` _+11 more__
- **2026-09-24** [`cd06e81c41`](https://github.com/vllm-project/vllm/commit/cd06e81c41) [#58427](https://github.com/vllm-project/vllm/pull/58427)
  [Bugfix][Quantization] Add Humming to the W4A8 (INT4xFP8) MoE oracle (#58427)
  _Files: `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/w4a8.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py` _+1 more__
- **2026-09-24** [`09fe178dba`](https://github.com/vllm-project/vllm/commit/09fe178dba) [#56956](https://github.com/vllm-project/vllm/pull/56956)
  Revert "[DSpark] Support pipeline-parallel targets in aggregated serving (#56956)" (#58484)
  _Files: `tests/kernels/moe/test_topk_softplus_sqrt.py`, `tests/v1/spec_decode/test_dflash_prepare_inputs.py`, `tests/v1/worker/test_pp_utils.py`, `vllm/model_executor/layers/fused_moe/router/dsv4_topk.py` _+7 more__
- **2026-09-24** [`44bf011f44`](https://github.com/vllm-project/vllm/commit/44bf011f44) [#58069](https://github.com/vllm-project/vllm/pull/58069)
  [Dependency] Upgrade FlashInfer version to 0.7.0 (#58069)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `requirements/cuda.txt`, `requirements/rubin-prerelease.txt` _+11 more__
- **2026-09-24** [`8b06a343ec`](https://github.com/vllm-project/vllm/commit/8b06a343ec) [#56168](https://github.com/vllm-project/vllm/pull/56168)
  [Bugfix][CPU][MoE] Fix out-of-bounds write and segfault when router weights are fp32 (#56168)
  _Files: `tests/model_executor/test_cpu_unquantized_gemm_dispatch.py`, `vllm/model_executor/layers/utils.py`_
- **2026-09-23** [`9ed81581a8`](https://github.com/vllm-project/vllm/commit/9ed81581a8) [#58051](https://github.com/vllm-project/vllm/pull/58051)
  [Perf][MoE] Skip top-k slots routed to non-local experts in TritonExp… (#58051)
  _Files: `tests/kernels/moe/test_block_fp8.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`_
- **2026-09-23** [`157bcb7c48`](https://github.com/vllm-project/vllm/commit/157bcb7c48) [#56956](https://github.com/vllm-project/vllm/pull/56956)
  [DSpark] Support pipeline-parallel targets in aggregated serving (#56956)
  _Files: `tests/kernels/moe/test_topk_softplus_sqrt.py`, `tests/v1/spec_decode/test_dflash_prepare_inputs.py`, `tests/v1/worker/test_pp_utils.py`, `vllm/model_executor/layers/fused_moe/router/dsv4_topk.py` _+7 more__
- **2026-09-23** [`e34489a543`](https://github.com/vllm-project/vllm/commit/e34489a543) [#56013](https://github.com/vllm-project/vllm/pull/56013)
  [XPU] upgrade to PyTorch 2.14 (#56013)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `docker/Dockerfile.xpu`, `docs/getting_started/installation/gpu.xpu.inc.md`, `requirements/test/xpu.txt` _+2 more__
- **2026-09-23** [`9127170b88`](https://github.com/vllm-project/vllm/commit/9127170b88) [#57176](https://github.com/vllm-project/vllm/pull/57176)
  [Quantization] Select per-token NVFP4 MoE backends explicitly (#57176)
  _Files: `tests/quantization/test_online.py`, `vllm/model_executor/layers/fused_moe/all2all_utils.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py` _+2 more__
- **2026-09-23** [`de6674b002`](https://github.com/vllm-project/vllm/commit/de6674b002) [#58234](https://github.com/vllm-project/vllm/pull/58234)
  [MoE] Use GateLinear for all MoE models (#58234)
  _Files: `vllm/model_executor/layers/fused_moe/router/gate_linear.py`, `vllm/model_executor/models/AXK1.py`, `vllm/model_executor/models/afmoe.py`, `vllm/model_executor/models/bailing_moe.py` _+30 more__
- **2026-09-23** [`8d16ca6cc2`](https://github.com/vllm-project/vllm/commit/8d16ca6cc2) [#58107](https://github.com/vllm-project/vllm/pull/58107)
  [CI][Bugfix] Update IPC test caller for #57312's _apply_entries signature (#58107)
  _Files: `tests/kernels/moe/test_flashinfer.py`_
- **2026-09-23** [`3ee2906f47`](https://github.com/vllm-project/vllm/commit/3ee2906f47) [#57887](https://github.com/vllm-project/vllm/pull/57887)
  [EPD] Support metadata-only audio inputs (#57887)
  _Files: `docs/features/disagg_encoder.md`, `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/model_executor/test_qwen3_omni.py`, `tests/models/multimodal/processing/test_common.py` _+10 more__
- **2026-09-22** [`e4340e41c9`](https://github.com/vllm-project/vllm/commit/e4340e41c9) [#55881](https://github.com/vllm-project/vllm/pull/55881)
  [Feat][XPU] VLLM_BATCH_INVARIANT support for Dense/MoE models (#55881)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `.buildkite/scripts/hardware_ci/run-xpu-batch-invariance.sh`, `tests/v1/determinism/test_xpu_batch_invariant_ut.py`, `vllm/distributed/device_communicators/xpu_communicator.py` _+6 more__
- **2026-09-22** [`c723a831a8`](https://github.com/vllm-project/vllm/commit/c723a831a8) [#57312](https://github.com/vllm-project/vllm/pull/57312)
  [Fast Start] Cache the MTP draft model in a separate daemon group (#57312)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `tests/model_executor/test_qwen3_omni.py`, `tests/v1/spec_decode/test_draft_attention_backend_override.py`, `tests/v1/spec_decode/test_draft_moe_backend_override.py` _+12 more__
- **2026-09-22** [`1fee69838e`](https://github.com/vllm-project/vllm/commit/1fee69838e) [#49685](https://github.com/vllm-project/vllm/pull/49685)
  [XPU] Fix Nemotron FP8 LM-eval config: drop CUDA-only moe_backend and wire to new Buildkite job (#49685)
  _Files: `.buildkite/intel_jobs/lm_eval_intel.yaml`, `.buildkite/lm-eval-harness/configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8-xpu.yaml`, `.buildkite/lm-eval-harness/configs/models-large-xpu-fp8.txt`_
- **2026-09-21** [`8bf051cd51`](https://github.com/vllm-project/vllm/commit/8bf051cd51) [#57984](https://github.com/vllm-project/vllm/pull/57984)
  [Bugfix][Kernel] Skip the fused silu-mul block-quant fast path when a swiglu clamp is set (#57984)
  _Files: `tests/kernels/moe/test_block_fp8.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`_
- **2026-09-21** [`9179bcd416`](https://github.com/vllm-project/vllm/commit/9179bcd416) [#57867](https://github.com/vllm-project/vllm/pull/57867)
  [Bugfix][MoE] Reject hash routing for unsupported monolithic backends (#57867)
  _Files: `tests/kernels/moe/conftest.py`, `tests/kernels/moe/test_topk_softplus_sqrt.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/layer.py` _+1 more__
- **2026-09-21** [`0b7f11a1ee`](https://github.com/vllm-project/vllm/commit/0b7f11a1ee) [#45635](https://github.com/vllm-project/vllm/pull/45635)
  [AuxOutput] Add block-keyed storage for routed-expert outputs (#45635)
  _Files: `tests/config/test_aux_output_config.py`, `tests/distributed/aux_output_connector/test_store.py`, `tests/entrypoints/openai/test_return_routed_experts.py`, `tests/entrypoints/scale_out/token_in_token_out/test_return_routed_experts.py` _+28 more__
- **2026-09-21** [`6654bcbfca`](https://github.com/vllm-project/vllm/commit/6654bcbfca) [#57277](https://github.com/vllm-project/vllm/pull/57277)
  [MRV2][XPU] use xpu sample kernel in mrv2 sampler (#57277)
  _Files: `vllm/v1/sample/ops/topk_topp_sampler.py`, `vllm/v1/watermarking/gpu_sampler.py`, `vllm/v1/worker/gpu/sample/sampler.py`_
- **2026-09-21** [`a15dbbd63d`](https://github.com/vllm-project/vllm/commit/a15dbbd63d) [#57855](https://github.com/vllm-project/vllm/pull/57855)
  [XPU][CI] fallback to 7-args of moe_align_block_size (#57855)
  _Files: `vllm/_custom_ops.py`_

## Serving / API  (24 commits)

- **2026-09-28** [`6f65fde419`](https://github.com/vllm-project/vllm/commit/6f65fde419) [#58958](https://github.com/vllm-project/vllm/pull/58958)
  [Bugfix][Frontend] Apply Harmony adjust_request in batched chat completions (#58958)
  _Files: `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py`, `vllm/renderers/online_renderer.py`_
- **2026-09-28** [`027b6f3a22`](https://github.com/vllm-project/vllm/commit/027b6f3a22) [#58939](https://github.com/vllm-project/vllm/pull/58939)
  [Bugfix][Frontend] Use a fresh parser per choice in non-streaming chat completions (#58939)
  _Files: `vllm/entrypoints/openai/chat_completion/serving.py`_
- **2026-09-28** [`4d07e90653`](https://github.com/vllm-project/vllm/commit/4d07e90653) [#58929](https://github.com/vllm-project/vllm/pull/58929)
  [Bugfix][Frontend] Sample batched chat completions from the adjusted requests (#58929)
  _Files: `vllm/entrypoints/openai/chat_completion/batch_serving.py`_
- **2026-09-28** [`3184226984`](https://github.com/vllm-project/vllm/commit/3184226984) [#58927](https://github.com/vllm-project/vllm/pull/58927)
  [Bugfix][Frontend] Count Responses reasoning tokens per tool round (#58927)
  _Files: `tests/entrypoints/openai/responses/test_parsable_context_unit.py`, `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/serving.py`_
- **2026-09-27** [`e7900156e1`](https://github.com/vllm-project/vllm/commit/e7900156e1) [#58552](https://github.com/vllm-project/vllm/pull/58552)
  [Fast Start] Add `/health` endpoint for the weight cache daemon (#58552)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `vllm/entrypoints/cli/preload.py`_
- **2026-09-26** [`379e9a1ea8`](https://github.com/vllm-project/vllm/commit/379e9a1ea8) [#58832](https://github.com/vllm-project/vllm/pull/58832)
  [Security] Harden message sanitization (#58832)
  _Files: `tests/entrypoints/serve/exception_handling/test_error_sanitization.py`, `vllm/entrypoints/serve/exception_handling/utils.py`_
- **2026-09-26** [`dfab504333`](https://github.com/vllm-project/vllm/commit/dfab504333) [#58754](https://github.com/vllm-project/vllm/pull/58754)
  [Bugfix][Frontend] Detect Anthropic inline-system merge against the resolved chat template (#58754)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/openai/chat_completion/test_chat_error.py`, `tests/entrypoints/openai/completion/test_completion_error.py`, `tests/entrypoints/scale_out/render/test_render.py` _+2 more__
- **2026-09-26** [`d64f277c54`](https://github.com/vllm-project/vllm/commit/d64f277c54) [#58786](https://github.com/vllm-project/vllm/pull/58786)
  [Bugfix] Fix Anthropic Thinking Disabled with P/D (#58786)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/protocol.py`_
- **2026-09-25** [`8b47e8b22c`](https://github.com/vllm-project/vllm/commit/8b47e8b22c) [#56067](https://github.com/vllm-project/vllm/pull/56067)
  [Perf][Frontend] Defer reasoning usage recounts for non-continuous chat streams (#56067)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/entrypoints/openai/chat_completion/serving.py`_
- **2026-09-25** [`de2d478d9a`](https://github.com/vllm-project/vllm/commit/de2d478d9a) [#58788](https://github.com/vllm-project/vllm/pull/58788)
  [Bugfix][Frontend] Document 404 response for `/generative_scoring` (#58788)
  _Files: `vllm/entrypoints/generate/generative_scoring/api_router.py`_
- **2026-09-25** [`7871963fcc`](https://github.com/vllm-project/vllm/commit/7871963fcc) [#58551](https://github.com/vllm-project/vllm/pull/58551)
  [Bugfix][Frontend] Respect max_output_tokens in the Harmony tool-call loop (#58551)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/serving.py`_
- **2026-09-25** [`f339e0e757`](https://github.com/vllm-project/vllm/commit/f339e0e757) [#58583](https://github.com/vllm-project/vllm/pull/58583)
  [Bugfix][Frontend] Keep logprobs of parser-suppressed streaming chunks (#58583)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/entrypoints/openai/chat_completion/serving.py`_
- **2026-09-25** [`bb35e2587b`](https://github.com/vllm-project/vllm/commit/bb35e2587b) [#57666](https://github.com/vllm-project/vllm/pull/57666)
  [Pooling] Preserve reranker tokenization with document limits (#57666)
  _Files: `tests/entrypoints/pooling/scoring/test_io_processor_unit.py`, `tests/entrypoints/pooling/scoring/test_utils.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`, `vllm/entrypoints/pooling/scoring/utils.py`_
- **2026-09-25** [`50f78084da`](https://github.com/vllm-project/vllm/commit/50f78084da) [#57729](https://github.com/vllm-project/vllm/pull/57729)
  [Bugfix] Fix generative scoring body cancellation (#57729)
  _Files: `vllm/entrypoints/generate/generative_scoring/api_router.py`_
- **2026-09-25** [`24928a4d62`](https://github.com/vllm-project/vllm/commit/24928a4d62) [#56680](https://github.com/vllm-project/vllm/pull/56680)
  [UX][Frontend] Introduce `vllm preload` cli for fast restart (#56680)
  _Files: `docs/cli/README.md`, `docs/features/preload.md`, `docs/mkdocs/gen_files/generate_argparse.py`, `tests/model_executor/model_loader/test_weight_cache.py` _+4 more__
- **2026-09-25** [`5a2ed2e7ee`](https://github.com/vllm-project/vllm/commit/5a2ed2e7ee) [#58613](https://github.com/vllm-project/vllm/pull/58613)
  [Frontend] Handle Disable Thinking in /v1/messages (#58613)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/anthropic/test_protocol_exports.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/anthropic/serving.py` _+2 more__
- **2026-09-25** [`34e104f6fe`](https://github.com/vllm-project/vllm/commit/34e104f6fe) [#55102](https://github.com/vllm-project/vllm/pull/55102)
  [gRPC] Fix ping tolerance so long non-streaming RPCs are not dropped (#55102)
  _Files: `vllm/entrypoints/launchers/grpc_server.py`_
- **2026-09-24** [`a7d203efe5`](https://github.com/vllm-project/vllm/commit/a7d203efe5) [#50769](https://github.com/vllm-project/vllm/pull/50769)
  fix(config): apply presence_penalty/frequency_penalty from override-generation-config (#50769)
  _Files: `tests/config/test_config_generation.py`, `tests/entrypoints/openai/test_penalty_default_resolution.py`, `vllm/config/model.py`, `vllm/entrypoints/openai/chat_completion/protocol.py` _+1 more__
- **2026-09-24** [`e028554a1f`](https://github.com/vllm-project/vllm/commit/e028554a1f) [#58306](https://github.com/vllm-project/vllm/pull/58306)
  [Rust Frontend] Support `--sse-keep-alive-interval` (#58306)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/server/src/config.rs`, `rust/src/server/src/routes/inference/generate.rs` _+3 more__
- **2026-09-24** [`7f1a5398e9`](https://github.com/vllm-project/vllm/commit/7f1a5398e9) [#58488](https://github.com/vllm-project/vllm/pull/58488)
  Fix full logprobs in token-in/token-out responses (#58488)
  _Files: `tests/entrypoints/scale_out/token_in_token_out/test_tokens_logprobs.py`, `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-09-23** [`b33c8a657d`](https://github.com/vllm-project/vllm/commit/b33c8a657d) [#46303](https://github.com/vllm-project/vllm/pull/46303)
  [Bugfix][Frontend] Keep length finish_reason for max_tokens-truncated streaming tool calls (#46303)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/entrypoints/openai/chat_completion/serving.py`_
- **2026-09-21** [`21aa17c128`](https://github.com/vllm-project/vllm/commit/21aa17c128) [#57948](https://github.com/vllm-project/vllm/pull/57948)
  [Bugfix][Frontend] Accept diarized transcription responses in run-batch (#57948)
  _Files: `vllm/entrypoints/launchers/run_batch.py`_
- **2026-09-21** [`887cf91e30`](https://github.com/vllm-project/vllm/commit/887cf91e30) [#57498](https://github.com/vllm-project/vllm/pull/57498)
  [Pooling] Fix normalization of chunked long-text embeddings (#57498)
  _Files: `vllm/entrypoints/pooling/embed/io_processor.py`_
- **2026-09-21** [`8b98b7d0b4`](https://github.com/vllm-project/vllm/commit/8b98b7d0b4) [#57922](https://github.com/vllm-project/vllm/pull/57922)
  [Frontend] Add streaming parity tests and docs for derender (#57922)
  _Files: `docs/serving/online_serving/derenderer.md`, `tests/entrypoints/scale_out/derender/test_derender_parity.py`, `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `tests/entrypoints/scale_out/derender/utils.py` _+1 more__

## Models  (22 commits)

- **2026-09-28** [`8cc9aa5ad3`](https://github.com/vllm-project/vllm/commit/8cc9aa5ad3) [#54213](https://github.com/vllm-project/vllm/pull/54213)
  [Bugfix][Model] Gemma4: register aliased embedding scalars as buffers (#54213)
  _Files: `vllm/model_executor/models/gemma4.py`_
- **2026-09-28** [`d6cce94fd4`](https://github.com/vllm-project/vllm/commit/d6cce94fd4) [#58957](https://github.com/vllm-project/vllm/pull/58957)
  [Perf][Qwen4Exp] Fuse HC down projection and SiLU on NVIDIA (#58957)
  _Files: `tests/models/qwen4_exp/test_hc_ops.py`, `vllm/models/qwen4_exp/nvidia/hyperconnection.py`, `vllm/models/qwen4_exp/nvidia/model.py`, `vllm/models/qwen4_exp/nvidia/ops/cute_dsl/__init__.py` _+3 more__
- **2026-09-28** [`1668e5976d`](https://github.com/vllm-project/vllm/commit/1668e5976d) [#58964](https://github.com/vllm-project/vllm/pull/58964)
  [CPU] Use accelerator memory API in DiffusionGemma (#58964)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-09-28** [`b9e2903b89`](https://github.com/vllm-project/vllm/commit/b9e2903b89) [#58239](https://github.com/vllm-project/vllm/pull/58239)
  [Mypy] Fix mypy typing for Ultravox and Unlimited-OCR models (#58239)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/model_loader/reload/torchao_decorator.py`, `vllm/model_executor/models/phi4mm.py`, `vllm/model_executor/models/ultravox.py` _+2 more__
- **2026-09-28** [`39d49539de`](https://github.com/vllm-project/vllm/commit/39d49539de) [#58651](https://github.com/vllm-project/vllm/pull/58651)
  [KimiViT][Perf] Fuse per-layer QK RoPE into one in-place kernel (#58651)
  _Files: `tests/kernels/core/test_apply_rotary_emb.py`, `vllm/model_executor/layers/rotary_embedding/packed_qk_rope.py`, `vllm/model_executor/models/kimi_k25_vit.py`_
- **2026-09-27** [`2b9b55c7f1`](https://github.com/vllm-project/vllm/commit/2b9b55c7f1) [#56086](https://github.com/vllm-project/vllm/pull/56086)
  [Bugfix] Support repsonse_format + tool_choice=auto (#56086)
  _Files: `tests/parser/test_abstract_parser.py`, `tests/parser/test_harmony.py`, `vllm/parser/abstract_parser.py`, `vllm/parser/cohere_command.py` _+2 more__
- **2026-09-27** [`924707f1bf`](https://github.com/vllm-project/vllm/commit/924707f1bf) [#57237](https://github.com/vllm-project/vllm/pull/57237)
  [CI] Split (H200 MIG 35GB) Spec Decode Speculators + MTP into 4 named jobs (#57237)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `tests/v1/e2e/spec_decode/mtp/_correctness.py`, `tests/v1/e2e/spec_decode/mtp/deepseek/__init__.py`, `tests/v1/e2e/spec_decode/mtp/deepseek/test_mtp.py` _+8 more__
- **2026-09-25** [`b040321b33`](https://github.com/vllm-project/vllm/commit/b040321b33) [#52580](https://github.com/vllm-project/vllm/pull/52580)
  fix: perf: use startswith(x, i) instead of string slicing to avoid O(N^2) (#52580)
  _Files: `vllm/parser/gemma4.py`_
- **2026-09-25** [`6ec2f84e1a`](https://github.com/vllm-project/vllm/commit/6ec2f84e1a) [#57664](https://github.com/vllm-project/vllm/pull/57664)
  [Pooling] Preserve BERT-family heads for raw logits (#57664)
  _Files: `vllm/model_executor/models/bert.py`, `vllm/model_executor/models/modernbert.py`_
- **2026-09-25** [`353e491efd`](https://github.com/vllm-project/vllm/commit/353e491efd) [#58226](https://github.com/vllm-project/vllm/pull/58226)
  [Perf] DiffusionGemma: one-pass sampler statistics kernel (#58226)
  _Files: `tests/v1/sample/test_diffusion_gemma_reads.py`, `tests/v1/sample/test_diffusion_sampler_stats.py`, `vllm/model_executor/models/diffusion_gemma.py`, `vllm/model_executor/models/diffusion_gemma_sampler.py`_
- **2026-09-25** [`064bc747ab`](https://github.com/vllm-project/vllm/commit/064bc747ab) [#58626](https://github.com/vllm-project/vllm/pull/58626)
  [Bugfix][Frontend] Count reasoning tokens for Harmony, DeepSeek-V3 and Step3 parsers (#58626)
  _Files: `tests/parser/test_harmony.py`, `tests/reasoning/test_deepseekv3_reasoning_parser.py`, `tests/reasoning/test_step3_reasoning_parser.py`, `vllm/parser/harmony.py` _+2 more__
- **2026-09-24** [`ab3de6edf2`](https://github.com/vllm-project/vllm/commit/ab3de6edf2) [#58216](https://github.com/vllm-project/vllm/pull/58216)
  [Perf] DiffusionGemma: constrained reads over the request's logprob_token_ids (#58216)
  _Files: `examples/features/structured_diffusion/README.md`, `examples/features/structured_diffusion/structured_server.py`, `tests/test_sampling_params.py`, `tests/v1/sample/test_diffusion_gemma_reads.py` _+2 more__
- **2026-09-24** [`8b84e15066`](https://github.com/vllm-project/vllm/commit/8b84e15066) [#54461](https://github.com/vllm-project/vllm/pull/54461)
  [transformer] RMSNorm matching for alternative rsqrt (#54461)
  _Files: `tests/models/transformers/fusers/test_rms_norm.py`, `vllm/model_executor/models/transformers/fusers/rms_norm.py`_
- **2026-09-24** [`cfd5c20286`](https://github.com/vllm-project/vllm/commit/cfd5c20286) [#58117](https://github.com/vllm-project/vllm/pull/58117)
  [XPU][UT] Align HF and vLLM inputs for Qwen2 embedding test by preventing Sentence Transformers from applying chat template (#58117)
  _Files: `requirements/test/xpu.in`, `requirements/test/xpu.txt`_
- **2026-09-24** [`1291bdb85e`](https://github.com/vllm-project/vllm/commit/1291bdb85e) [#58086](https://github.com/vllm-project/vllm/pull/58086)
  [EPD][Model Loader] Skip language-model checkpoint shards for `--mm-encoder-only` (#58086)
  _Files: `tests/model_executor/model_loader/test_mm_encoder_only_weight_filter.py`, `tests/model_executor/model_loader/test_registry.py`, `vllm/model_executor/model_loader/default_loader.py`, `vllm/model_executor/model_loader/weight_utils.py` _+1 more__
- **2026-09-23** [`f9ad9dd6b4`](https://github.com/vllm-project/vllm/commit/f9ad9dd6b4) [#46466](https://github.com/vllm-project/vllm/pull/46466)
  Doc: add DiffusionGemma to supported models (#46466)
  _Files: `docs/models/supported_models.md`_
- **2026-09-23** [`d95a896ea6`](https://github.com/vllm-project/vllm/commit/d95a896ea6) [#44229](https://github.com/vllm-project/vllm/pull/44229)
  [Feature][Frontend] Add DeepSeek-V4 FIM completion rendering (#44229)
  _Files: `tests/entrypoints/openai/completion/test_completion_error.py`, `vllm/entrypoints/openai/completion/serving.py`, `vllm/renderers/base.py`, `vllm/renderers/deepseek_v4.py` _+1 more__
- **2026-09-22** [`276db94fb2`](https://github.com/vllm-project/vllm/commit/276db94fb2) [#55442](https://github.com/vllm-project/vllm/pull/55442)
  [Bugfix][Model][Spec Decode] Defer disposable GLM MTP head (#55442)
  _Files: `tests/v1/spec_decode/test_mtp.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/models/glm5next/common/mtp.py`_
- **2026-09-22** [`496c6472cb`](https://github.com/vllm-project/vllm/commit/496c6472cb) [#57340](https://github.com/vllm-project/vllm/pull/57340)
  [Rust Frontend] Build full-output grammars from initialized reasoning parsers (#57340)
  _Files: `rust/src/parser/src/output_grammar.rs`, `rust/src/parser/src/reasoning/deepseek_r1.rs`, `rust/src/parser/src/reasoning/deepseek_v3.rs`, `rust/src/parser/src/reasoning/delimited.rs` _+8 more__
- **2026-09-22** [`ff3c9cba3f`](https://github.com/vllm-project/vllm/commit/ff3c9cba3f) [#57933](https://github.com/vllm-project/vllm/pull/57933)
  [Rust Frontend] Add MiMo V2.5 parser support (#57933)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/default/structural_tag.rs`, `rust/src/chat/src/parser/reasoning/mod.rs`, `rust/src/chat/src/parser/tool/mod.rs` _+9 more__
- **2026-09-22** [`78d7836525`](https://github.com/vllm-project/vllm/commit/78d7836525) [#57965](https://github.com/vllm-project/vllm/pull/57965)
  [CI] Split (H200) LM Eval Large Models into per-model jobs (#57965)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/models-h200-deepseek-r1-dp.txt`, `tests/evals/gsm8k/configs/models-h200-deepseek-r1-tp.txt`, `tests/evals/gsm8k/configs/models-h200-deepseek-v32-dp.txt` _+3 more__
- **2026-09-21** [`9b49f92344`](https://github.com/vllm-project/vllm/commit/9b49f92344) [#57603](https://github.com/vllm-project/vllm/pull/57603)
  [Perf][DSV4.1] Overlap mHC coefficients for small TP batches (#57603)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/model_executor/kernels/mhc/tilelang_kernels.py`, `vllm/model_executor/kernels/mhc/warmup.py`, `vllm/models/deepseek_v41/nvidia/model.py` _+2 more__

## CI / Build  (22 commits)

- **2026-09-28** [`2407f405b5`](https://github.com/vllm-project/vllm/commit/2407f405b5) [#58055](https://github.com/vllm-project/vllm/pull/58055)
  [CI] Allowlist-shrink batch 1: wire 17 root-level tests + drop 5 stale watermarking entries into misc.yaml (#58055)
  _Files: `.buildkite/test_areas/misc.yaml`, `docker/Dockerfile.cpu`, `tests/test_request_input_bounds.py`, `tests/test_triton_utils.py` _+4 more__
- **2026-09-26** [`2f41e00235`](https://github.com/vllm-project/vllm/commit/2f41e00235) [#58609](https://github.com/vllm-project/vllm/pull/58609)
  [CI] Split (B200) Miscellaneous Kernels into mHC, FLA Ops and Misc named jobs (#58609)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/fla/__init__.py`, `tests/kernels/fla/test_fla_layernorm_guard.py`, `tests/kernels/fla/test_fused_gdn_post_conv.py` _+7 more__
- **2026-09-26** [`3b4566c5cf`](https://github.com/vllm-project/vllm/commit/3b4566c5cf) [#58764](https://github.com/vllm-project/vllm/pull/58764)
  [CI] Only isolate the registry tests that need a fresh process (#58764)
  _Files: `tests/models/test_registry.py`_
- **2026-09-25** [`e55d076f89`](https://github.com/vllm-project/vllm/commit/e55d076f89) [#57982](https://github.com/vllm-project/vllm/pull/57982)
  [Bugfix] Don't drop the rest of the allocator config when toggling expandable segments (#57982)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/device_allocator/test_alloc_conf.py`, `vllm/device_allocator/alloc_conf.py`, `vllm/device_allocator/cumem.py`_
- **2026-09-25** [`4ccfe12398`](https://github.com/vllm-project/vllm/commit/4ccfe12398) [#56809](https://github.com/vllm-project/vllm/pull/56809)
  [watermarking] golden tests for backwards compatibility (#56809)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/watermarking/__init__.py`, `tests/watermarking/generate_goldens.py`, `tests/watermarking/golden_candidates.py` _+3 more__
- **2026-09-25** [`2d7dd0e5c1`](https://github.com/vllm-project/vllm/commit/2d7dd0e5c1) [#58701](https://github.com/vllm-project/vllm/pull/58701)
  [Bugfix][CI] Report subprocess test skips as skips, not passes (#58701)
  _Files: `tests/utils.py`, `tests/utils_/test_spawn_decorator.py`_
- **2026-09-25** [`2bc902eb0f`](https://github.com/vllm-project/vllm/commit/2bc902eb0f) [#57735](https://github.com/vllm-project/vllm/pull/57735)
  [CI] [MRV2] Restore MRV2 pp dp coverage (#57735)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/expert_parallelism.yaml`, `.buildkite/test_areas/rust_frontend.yaml`_
- **2026-09-25** [`fa6c407d15`](https://github.com/vllm-project/vllm/commit/fa6c407d15) [#58645](https://github.com/vllm-project/vllm/pull/58645)
  [CI] Shard (H100) Helion Kernels five ways (#58645)
  _Files: `.buildkite/test_areas/kernels.yaml`_
- **2026-09-24** [`f5b40fcdfe`](https://github.com/vllm-project/vllm/commit/f5b40fcdfe) [#58628](https://github.com/vllm-project/vllm/pull/58628)
  [CI] Report to CRCR after all jobs finish, gated on the build's long pole (#58628)
  _Files: `.buildkite/scripts/crcr-report.sh`, `.buildkite/test_areas/crcr_report.yaml`_
- **2026-09-24** [`7edb27f68e`](https://github.com/vllm-project/vllm/commit/7edb27f68e) [#58283](https://github.com/vllm-project/vllm/pull/58283)
  [XPU][CI] enable prompt embeds tests on XPU (#58283)
  _Files: `tests/v1/worker/test_prompt_embeds_state.py`_
- **2026-09-24** [`b44895cf93`](https://github.com/vllm-project/vllm/commit/b44895cf93) [#58140](https://github.com/vllm-project/vllm/pull/58140)
  [CPU] Use pre-built triton (#58140)
  _Files: `docker/Dockerfile.cpu`, `requirements/cpu.txt`, `vllm/platforms/cpu.py`_
- **2026-09-24** [`7ef0d69ea0`](https://github.com/vllm-project/vllm/commit/7ef0d69ea0) [#58455](https://github.com/vllm-project/vllm/pull/58455)
  [5/12][ci-selector][CI] Skip the Proton GPU test when another CUPTI tool is injected (#58455)
  _Files: `tests/v1/worker/test_gpu_profiler.py`_
- **2026-09-23** [`89d9fd83e2`](https://github.com/vllm-project/vllm/commit/89d9fd83e2) [#58452](https://github.com/vllm-project/vllm/pull/58452)
  [CI] Disable JIT warmup by default in VllmRunner (#58452)
  _Files: `tests/conftest.py`_
- **2026-09-23** [`34b069080d`](https://github.com/vllm-project/vllm/commit/34b069080d) [#58351](https://github.com/vllm-project/vllm/pull/58351)
  [CI] Select one GPU for the H200 initialized snapshot E2E step (#58351)
  _Files: `.buildkite/test_areas/entrypoints.yaml`_
- **2026-09-23** [`e975732152`](https://github.com/vllm-project/vllm/commit/e975732152) [#58237](https://github.com/vllm-project/vllm/pull/58237)
  [XPU][CI] Deselect tests/v1/spec_decode/test_mtp.py::test_glm_mtp_defers_lm_head (#58237)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-09-23** [`355d789f0d`](https://github.com/vllm-project/vllm/commit/355d789f0d) [#58173](https://github.com/vllm-project/vllm/pull/58173)
  [Compilation] Fix QuTLASS compilation with PyTorch 2.13 (#58173)
  _Files: `cmake/external_projects/qutlass.cmake`_
- **2026-09-22** [`d90f0eade5`](https://github.com/vllm-project/vllm/commit/d90f0eade5) [#57945](https://github.com/vllm-project/vllm/pull/57945)
  [Build] Fix CUDA 12 KV connector dependency selection (#57945)
  _Files: `.buildkite/scripts/install-kv-connectors.sh`, `docker/Dockerfile`, `requirements/kv_connectors_cu12.txt`_
- **2026-09-22** [`362a64b21d`](https://github.com/vllm-project/vllm/commit/362a64b21d) [#58050](https://github.com/vllm-project/vllm/pull/58050)
  [XPU][CI]Remove model_runner_v2 test from Intel GPU CI (#58050)
  _Files: `.buildkite/intel_jobs/model_runner_v2_intel.yaml`_
- **2026-09-22** [`f07e227ee9`](https://github.com/vllm-project/vllm/commit/f07e227ee9) [#57606](https://github.com/vllm-project/vllm/pull/57606)
  [Docker] Expose bundled vllm-rs on PATH (#57606)
  _Files: `docker/Dockerfile`_
- **2026-09-22** [`e9f169d16b`](https://github.com/vllm-project/vllm/commit/e9f169d16b) [#54867](https://github.com/vllm-project/vllm/pull/54867)
  [CI] Add pre-commit check that new tests are tethered to Buildkite jobs (#54867)
  _Files: `.buildkite/test_areas/misc.yaml`, `.pre-commit-config.yaml`, `docker/Dockerfile.cpu`, `tests/tools/test_check_test_tethering.py` _+4 more__
- **2026-09-21** [`db7f1f6714`](https://github.com/vllm-project/vllm/commit/db7f1f6714) [#57889](https://github.com/vllm-project/vllm/pull/57889)
  [CI][XPU] Deselect Ray UT in XPU V1 test Job (#57889)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`_
- **2026-09-21** [`eb87980585`](https://github.com/vllm-project/vllm/commit/eb87980585) [#57554](https://github.com/vllm-project/vllm/pull/57554)
  [Build] Fix DeepGEMM CUDA 12.9 release builds (#57554)
  _Files: `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_

## Scheduler / Engine  (20 commits)

- **2026-09-28** [`b721a4c709`](https://github.com/vllm-project/vllm/commit/b721a4c709) [#54335](https://github.com/vllm-project/vllm/pull/54335)
  [Feature] Add fixed-token prefill scoring (#54335)
  _Files: `docs/training/prompt_token_id_logprobs.md`, `rust/Cargo.lock`, `rust/src/engine-core-client/src/protocol/output.rs`, `rust/src/engine-core-client/src/protocol/sampling.rs` _+32 more__
- **2026-09-28** [`53d2e16a97`](https://github.com/vllm-project/vllm/commit/53d2e16a97) [#58490](https://github.com/vllm-project/vllm/pull/58490)
  [Bugfix][EPD] Skip sampling for encoder-only async steps (#58490)
  _Files: `tests/v1/engine/test_engine_core.py`, `tests/v1/kv_connector/unit/test_handshake_pp_aggregation.py`, `vllm/v1/engine/core.py`_
- **2026-09-26** [`fdcce47e9b`](https://github.com/vllm-project/vllm/commit/fdcce47e9b) [#58792](https://github.com/vllm-project/vllm/pull/58792)
  [Bugfix][Frontend] Fix Inkling tool name leaking into content after reasoning (#58792)
  _Files: `tests/parser/engine/test_inkling.py`, `vllm/parser/inkling.py`_
- **2026-09-25** [`b05f7d5fbc`](https://github.com/vllm-project/vllm/commit/b05f7d5fbc) [#55145](https://github.com/vllm-project/vllm/pull/55145)
  [PP][XPU]Add the flag to control microbatch feature on MRV2+PP (#55145)
  _Files: `vllm/envs.py`, `vllm/v1/core/sched/async_scheduler.py`, `vllm/v1/worker/gpu/pp_utils.py`_
- **2026-09-25** [`055f150df5`](https://github.com/vllm-project/vllm/commit/055f150df5) [#58574](https://github.com/vllm-project/vllm/pull/58574)
  [Perf][Rust Frontend] Make histogram observations lock-free (#58574)
  _Files: `rust/Cargo.lock`, `rust/clippy.toml`, `rust/src/metrics/Cargo.toml`, `rust/src/metrics/src/api_server.rs` _+4 more__
- **2026-09-24** [`bbd7c24d6e`](https://github.com/vllm-project/vllm/commit/bbd7c24d6e) [#57728](https://github.com/vllm-project/vllm/pull/57728)
  [MRV2] Validate MRV2 entrypoint logits processors (#57728)
  _Files: `vllm/v1/engine/input_processor.py`, `vllm/v1/worker/gpu/sample/logits_processor/loader.py`_
- **2026-09-24** [`c0c35ddd8e`](https://github.com/vllm-project/vllm/commit/c0c35ddd8e) [#58342](https://github.com/vllm-project/vllm/pull/58342)
  [Bugfix][CI] Fix the flaky sharded-sampling tests, and the engine teardown need (#58342)
  _Files: `tests/v1/e2e/general/test_sharded_sampling.py`, `tests/v1/e2e/spec_decode/test_sharded_sampling.py`, `vllm/v1/engine/core_client.py`_
- **2026-09-24** [`bbc4ddeca9`](https://github.com/vllm-project/vllm/commit/bbc4ddeca9) [#57696](https://github.com/vllm-project/vllm/pull/57696)
  [Bugfix][V1] Reject encoder-cache hits with mismatched embedding counts (#57696)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/test_encoder_cache_manager.py`, `tests/v1/core/test_scheduler.py`, `vllm/v1/core/encoder_cache_manager.py` _+1 more__
- **2026-09-24** [`28282ffe34`](https://github.com/vllm-project/vllm/commit/28282ffe34) [#58163](https://github.com/vllm-project/vllm/pull/58163)
  [Feature][Frontend] Request JSON body debug logging on `--enable-log-requests` flag (#58163)
  _Files: `vllm/entrypoints/serve/engine/serving.py`, `vllm/entrypoints/serve/utils/request_logger.py`_
- **2026-09-24** [`6697a7dd30`](https://github.com/vllm-project/vllm/commit/6697a7dd30) [#58459](https://github.com/vllm-project/vllm/pull/58459)
  [Scheduler] Tune --long-prefill-token-threshold adaptiveness (#58459)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `vllm/config/scheduler.py`, `vllm/engine/arg_utils.py` _+1 more__
- **2026-09-23** [`0f2a15c927`](https://github.com/vllm-project/vllm/commit/0f2a15c927) [#58272](https://github.com/vllm-project/vllm/pull/58272)
  [Tests] Select V2 for diffusion scheduler unit tests (#58272)
  _Files: `tests/v1/core/test_scheduler.py`_
- **2026-09-22** [`1b3b88ec2b`](https://github.com/vllm-project/vllm/commit/1b3b88ec2b) [#57250](https://github.com/vllm-project/vllm/pull/57250)
  [Core] structured generation mode for DiffusionGemma model (Jev-like) (#57250)
  _Files: `examples/features/structured_diffusion/README.md`, `examples/features/structured_diffusion/structured_server.py`, `tests/config/test_model_arch_config.py`, `tests/test_sampling_params.py` _+12 more__
- **2026-09-22** [`6dc34b6334`](https://github.com/vllm-project/vllm/commit/6dc34b6334) [#56547](https://github.com/vllm-project/vllm/pull/56547)
  [CPU] Add device-memory-utilization CLI alias (#56547)
  _Files: `tests/engine/test_arg_utils.py`, `vllm/config/cache.py`, `vllm/engine/arg_utils.py`_
- **2026-09-22** [`5abf85d27a`](https://github.com/vllm-project/vllm/commit/5abf85d27a) [#57006](https://github.com/vllm-project/vllm/pull/57006)
  [Bugfix][Frontend] Validate mixed prompt embedding mask lengths (#57006)
  _Files: `tests/test_request_input_bounds.py`, `vllm/v1/engine/input_processor.py`_
- **2026-09-22** [`4800024b98`](https://github.com/vllm-project/vllm/commit/4800024b98) [#57731](https://github.com/vllm-project/vllm/pull/57731)
  [Security] Reject min_tokens that exceeds the filled max_tokens default (#57731)
  _Files: `tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py`, `tests/test_request_input_bounds.py`, `vllm/v1/engine/input_processor.py`_
- **2026-09-22** [`639461eda4`](https://github.com/vllm-project/vllm/commit/639461eda4) [#57891](https://github.com/vllm-project/vllm/pull/57891)
  [RL][Sleep] Retain frozen weights across level-2 sleep (#57891)
  _Files: `docs/features/sleep_mode.md`, `tests/v1/worker/test_sleep_mode_backend.py`, `vllm/config/model.py`, `vllm/engine/arg_utils.py` _+1 more__
- **2026-09-22** [`c64b15cde5`](https://github.com/vllm-project/vllm/commit/c64b15cde5) [#57951](https://github.com/vllm-project/vllm/pull/57951)
  [Scheduler] Soften Long Prefill Tokens Threshhold (#57951)
  _Files: `tests/v1/core/test_deferred_block_free.py`, `tests/v1/core/test_scheduler.py`, `tests/v1/e2e/general/test_pooling_chunked_prefill.py`, `vllm/config/scheduler.py` _+1 more__
- **2026-09-21** [`dc479a2d83`](https://github.com/vllm-project/vllm/commit/dc479a2d83) [#53743](https://github.com/vllm-project/vllm/pull/53743)
  [Bugfix] Fix external LB DP rank handling when replicas share nodes (#53743)
  _Files: `docs/serving/data_parallel_deployment.md`, `tests/test_config.py`, `tests/v1/engine/test_engine_args.py`, `vllm/config/parallel.py` _+1 more__
- **2026-09-21** [`3918f3c5a3`](https://github.com/vllm-project/vllm/commit/3918f3c5a3) [#57460](https://github.com/vllm-project/vllm/pull/57460)
  [Profiler] Unify platform-aware torch profiling (#57460)
  _Files: `docs/contributing/profiling.md`, `tests/v1/engine/test_async_llm.py`, `tests/v1/worker/test_gpu_profiler.py`, `vllm/config/profiler.py` _+5 more__
- **2026-09-21** [`1185254851`](https://github.com/vllm-project/vllm/commit/1185254851) [#54581](https://github.com/vllm-project/vllm/pull/54581)
  [Bugfix][KV Connector] Propagate cache reset failure during sleep (#54581)
  _Files: `vllm/v1/engine/core.py`_

## Quantization  (18 commits)

- **2026-09-28** [`5eaa50f151`](https://github.com/vllm-project/vllm/commit/5eaa50f151) [#58515](https://github.com/vllm-project/vllm/pull/58515)
  [CPU] Build CPU wheels on Ubuntu 22.04 with AMX-FP8 support (#58515)
  _Files: `docker/Dockerfile.cpu`_
- **2026-09-25** [`38cc054fc2`](https://github.com/vllm-project/vllm/commit/38cc054fc2) [#58194](https://github.com/vllm-project/vllm/pull/58194)
  [Perf][Kernel] Vectorized flat abs-max for dynamic per-tensor FP8 quantization (#58194)
  _Files: `csrc/libtorch_stable/quantization/w8a8/fp8/common.cu`, `tests/kernels/quantization/test_fp8_quant.py`_
- **2026-09-25** [`f550ad8bf7`](https://github.com/vllm-project/vllm/commit/f550ad8bf7) [#55330](https://github.com/vllm-project/vllm/pull/55330)
  [Kernel][Perf] Register-resident path for per-token-group 8-bit quant (#55330)
  _Files: `benchmarks/kernels/benchmark_per_token_group_quant.py`, `csrc/libtorch_stable/quantization/w8a8/fp8/per_token_group_quant.cu`, `tests/kernels/quantization/test_per_token_group_quant.py`_
- **2026-09-25** [`609731e8f5`](https://github.com/vllm-project/vllm/commit/609731e8f5) [#57679](https://github.com/vllm-project/vllm/pull/57679)
  [Perf][DSv4.1] Restore the fused query RMSNorm + MXFP8 quantization path (#57679)
  _Files: `vllm/models/deepseek_v41/common/ops/query_quant.py`_
- **2026-09-24** [`7a9406690e`](https://github.com/vllm-project/vllm/commit/7a9406690e) [#58472](https://github.com/vllm-project/vllm/pull/58472)
  [KV Connector] Fix DecodeBench fp8 fill values and add a startup fill mode (#58472)
  _Files: `docs/serving/expert_parallel_deployment.md`, `tests/v1/kv_connector/unit/test_decode_bench_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`_
- **2026-09-24** [`4f72bd0152`](https://github.com/vllm-project/vllm/commit/4f72bd0152) [#58444](https://github.com/vllm-project/vllm/pull/58444)
  [Bugfix][Quantization] Give LM heads standard linear metadata (#58444)
  _Files: `tests/quantization/test_lm_head.py`, `tests/quantization/test_modelopt.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa4.py` _+4 more__
- **2026-09-24** [`0908116dd9`](https://github.com/vllm-project/vllm/commit/0908116dd9) [#48521](https://github.com/vllm-project/vllm/pull/48521)
  [Bugfix] Pass quant_config to DiffusionGemma's ParallelLMHead (#48521)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-09-24** [`dcfc17e0b1`](https://github.com/vllm-project/vllm/commit/dcfc17e0b1) [#51600](https://github.com/vllm-project/vllm/pull/51600)
  [XPU] enable XPU GRAPH by default (#51600)
  _Files: `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`, `tests/quantization/test_auto_round.py` _+3 more__
- **2026-09-24** [`f34a0e0797`](https://github.com/vllm-project/vllm/commit/f34a0e0797) [#58133](https://github.com/vllm-project/vllm/pull/58133)
  [CPU] Gate the AVX10.2 paths on compiler support (#58133)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/sgl-kernels/common.h`, `csrc/cpu/sgl-kernels/gemm_fp8_w8a8.cpp`_
- **2026-09-24** [`e0f03eb4f4`](https://github.com/vllm-project/vllm/commit/e0f03eb4f4) [#58469](https://github.com/vllm-project/vllm/pull/58469)
  [CI] Share BF16 baselines across quantization comparison tests (#58469)
  _Files: `tests/models/quantization/conftest.py`, `tests/models/quantization/test_fp8_per_channel.py`, `tests/models/quantization/test_mxfp8.py`_
- **2026-09-23** [`0549e8d0ab`](https://github.com/vllm-project/vllm/commit/0549e8d0ab) [#51800](https://github.com/vllm-project/vllm/pull/51800)
  [Quark] Remove quark-specific silent online quantization (#51800)
  _Files: `tests/quantization/test_quark.py`, `vllm/model_executor/layers/quantization/quark/quark.py`, `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`_
- **2026-09-23** [`f69cc7c178`](https://github.com/vllm-project/vllm/commit/f69cc7c178) [#58054](https://github.com/vllm-project/vllm/pull/58054)
  [Quantization][Bugfix] Bump humming-kernels to 0.1.16 (#58054)
  _Files: `requirements/cuda.txt`, `tests/evals/gsm8k/configs/humming/Qwen3-0.6B-MXFP8-humming.yaml`, `tests/evals/gsm8k/configs/humming/Qwen3-30B-A3B-FP8-block-humming.yaml`_
- **2026-09-23** [`9f07d023d0`](https://github.com/vllm-project/vllm/commit/9f07d023d0) [#46528](https://github.com/vllm-project/vllm/pull/46528)
  [Quantization] Enable humming wNaM asymmetric quant (zero_point) with compressed-tensors (#46528)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/humming/Qwen3-4B-mixed-quant-RTN-humming.yaml`, `tests/evals/gsm8k/configs/humming/Qwen3-4B-mixed-quant-RTN-no-w4a4-humming.yaml`, `tests/evals/gsm8k/configs/humming/config-a100-act-int8-shard-0.txt` _+8 more__
- **2026-09-23** [`955bd6abef`](https://github.com/vllm-project/vllm/commit/955bd6abef) [#58252](https://github.com/vllm-project/vllm/pull/58252)
  [CI][Bugfix] Extend groupwise rms_norm scale tolerance to CUDA (#58252)
  _Files: `tests/kernels/core/test_fused_quant_layernorm.py`_
- **2026-09-22** [`25965ee583`](https://github.com/vllm-project/vllm/commit/25965ee583) [#58001](https://github.com/vllm-project/vllm/pull/58001)
  [Kernel] Remove AllSpark INT8 W8A16 GEMM backend (#58001)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_marlin.py`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/quantization/gptq_allspark/allspark_qgemm_w8a16.cu` _+9 more__
- **2026-09-22** [`74370a0e30`](https://github.com/vllm-project/vllm/commit/74370a0e30) [#43462](https://github.com/vllm-project/vllm/pull/43462)
  [Bugfix] hadacore_transform: respect inplace parameter to fix garbage outputs with QuIP transforms (#43462)
  _Files: `csrc/libtorch_stable/quantization/hadamard/hadacore/hadamard_transform_cuda.cu`, `vllm/model_executor/layers/quantization/compressed_tensors/transform/module.py`_
- **2026-09-22** [`2af05512cf`](https://github.com/vllm-project/vllm/commit/2af05512cf) [#50814](https://github.com/vllm-project/vllm/pull/50814)
  [Kernel] Add opt-in load-time MXFP4 dequantization (#50814)
  _Files: `tests/kernels/quantization/test_mxfp4_kernel_selection.py`, `vllm/envs.py`, `vllm/model_executor/kernels/linear/mxfp4/emulation.py`_
- **2026-09-21** [`13058faa49`](https://github.com/vllm-project/vllm/commit/13058faa49) [#51360](https://github.com/vllm-project/vllm/pull/51360)
  [Frontend] Add reusable TP1 initialized-engine snapshots (#51360)
  _Files: `.buildkite/scripts/initialized-snapshot-e2e.sh`, `.buildkite/test_areas/entrypoints.yaml`, `docker/Dockerfile`, `docs/features/initialized_snapshots.md` _+12 more__

## Speculative Decoding  (15 commits)

- **2026-09-26** [`4bb804cc5b`](https://github.com/vllm-project/vllm/commit/4bb804cc5b) [#58678](https://github.com/vllm-project/vllm/pull/58678)
  [Perf][DSv4.1] Shard the Engram wkv projection across TP ranks (#58678)
  _Files: `tests/kernels/test_engram.py`, `vllm/models/deepseek_v41/common/engram.py`_
- **2026-09-26** [`8a2364605c`](https://github.com/vllm-project/vllm/commit/8a2364605c) [#58779](https://github.com/vllm-project/vllm/pull/58779)
  [Core] Bound draft-token RPC waits by the execute-model timeout (#58779)
  _Files: `tests/v1/executor/test_multiproc_executor.py`, `vllm/v1/executor/multiproc_executor.py`_
- **2026-09-25** [`6936e77ba4`](https://github.com/vllm-project/vllm/commit/6936e77ba4) [#56926](https://github.com/vllm-project/vllm/pull/56926)
  [Perf][Engram] Serialize offloaded lookups and pack host tables into huge pages (#56926)
  _Files: `tests/kernels/test_engram.py`, `tests/model_executor/test_weight_utils.py`, `vllm/config/engram.py`, `vllm/model_executor/model_loader/weight_utils.py` _+2 more__
- **2026-09-25** [`48d8880d09`](https://github.com/vllm-project/vllm/commit/48d8880d09) [#58489](https://github.com/vllm-project/vllm/pull/58489)
  [Bugfix][Qwen4Exp] Keep pinned PLE prefetch ids out of the CUDA graph pool (#58489)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/nvidia/ngram_embedding.py`_
- **2026-09-24** [`d5051abaf1`](https://github.com/vllm-project/vllm/commit/d5051abaf1) [#58368](https://github.com/vllm-project/vllm/pull/58368)
  [Bugfix][Mamba] Restore prompt-tail prefix-cache hits with MTP (#58368)
  _Files: `tests/v1/core/prefix_cache/test_mamba_eagle_resume_checkpoint.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-09-24** [`36f94d5fe8`](https://github.com/vllm-project/vllm/commit/36f94d5fe8) [#58612](https://github.com/vllm-project/vllm/pull/58612)
  [Bugfix][Outlines] Fix EOS termination and unconstrained masks after rejected drafts (#58612)
  _Files: `tests/v1/structured_output/test_structured_output_manager.py`, `vllm/v1/structured_output/__init__.py`, `vllm/v1/structured_output/backend_outlines.py`_
- **2026-09-24** [`ee2f3cdf12`](https://github.com/vllm-project/vllm/commit/ee2f3cdf12) [#54631](https://github.com/vllm-project/vllm/pull/54631)
  [Bugfix][Spec Decode] Separate DSpark width from MTP stage validation (#54631)
  _Files: `tests/config/test_speculative_draft_hf_overrides.py`, `vllm/config/speculative.py`_
- **2026-09-22** [`d421a2e8fc`](https://github.com/vllm-project/vllm/commit/d421a2e8fc) [#57396](https://github.com/vllm-project/vllm/pull/57396)
  [Perf] Remove CPU-GPU sync in heterogeneous vocabulary speculative decoding (#57396)
  _Files: `tests/v1/spec_decode/test_vocab_mapping.py`, `vllm/v1/spec_decode/vocab_mapping.py`_
- **2026-09-22** [`4edb55169f`](https://github.com/vllm-project/vllm/commit/4edb55169f) [#58193](https://github.com/vllm-project/vllm/pull/58193)
  [CI] Shard (H200 MIG 18GB) Spec Decode Draft Model across whole-directory replicas (#58193)
  _Files: `.buildkite/test_areas/spec_decode.yaml`_
- **2026-09-22** [`a6131b0e65`](https://github.com/vllm-project/vllm/commit/a6131b0e65) [#57914](https://github.com/vllm-project/vllm/pull/57914)
  [Bugfix][Engram] Fall back when /dev/shm is absent before sharing tables (#57914)
  _Files: `vllm/models/deepseek_v41/nvidia/engram.py`_
- **2026-09-21** [`54020c3c3e`](https://github.com/vllm-project/vllm/commit/54020c3c3e) [#57937](https://github.com/vllm-project/vllm/pull/57937)
  [Engram] Drop redundant VLLM_PLE_CPU_OFFLOAD env var (#57937)
  _Files: `tests/test_config.py`, `vllm/config/engram.py`, `vllm/envs.py`_
- **2026-09-21** [`fba33e39cb`](https://github.com/vllm-project/vllm/commit/fba33e39cb) [#57910](https://github.com/vllm-project/vllm/pull/57910)
  [Docs] Add an Engram feature page explaining Engram usage in vLLM (#57910)
  _Files: `docs/features/engram.md`_
- **2026-09-21** [`76ffb0d374`](https://github.com/vllm-project/vllm/commit/76ffb0d374) [#57651](https://github.com/vllm-project/vllm/pull/57651)
  [Model][Engram] Share host tables across co-located DP replicas by default (#57651)
  _Files: `tests/distributed/test_engram_dp_shard.py`, `tests/engine/test_arg_utils.py`, `tests/test_config.py`, `vllm/config/engram.py` _+3 more__
- **2026-09-21** [`9a70c233cd`](https://github.com/vllm-project/vllm/commit/9a70c233cd) [#57643](https://github.com/vllm-project/vllm/pull/57643)
  [Perf][DSV4.1] Fuse TP all-reduce with mHC input preparation (#57643)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/all_reduce_mhc.cu`, `tests/distributed/test_custom_all_reduce.py`, `tests/distributed/test_engram_dp_shard.py` _+5 more__
- **2026-09-21** [`d2983f2f16`](https://github.com/vllm-project/vllm/commit/d2983f2f16) [#56734](https://github.com/vllm-project/vllm/pull/56734)
  [Bugfix][Spec Decode] Stop dummy draft decode steps from writing KV through stale block-table rows (#56734)
  _Files: `tests/v1/worker/test_gpu_block_table.py`, `vllm/v1/worker/gpu/block_table.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`, `vllm/v1/worker/gpu/spec_decode/multi_module_mtp/speculator.py` _+1 more__

## Disaggregation / PD  (13 commits)

- **2026-09-27** [`386ac2573e`](https://github.com/vllm-project/vllm/commit/386ac2573e) [#58919](https://github.com/vllm-project/vllm/pull/58919)
  [Bugfix][KV Connector] Retry Mooncake bootstrap registration on timeout (reopens #55763) (#58919)
  _Files: `docs/features/mooncake_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_utils.py` _+1 more__
- **2026-09-27** [`fff03267da`](https://github.com/vllm-project/vllm/commit/fff03267da) [#50047](https://github.com/vllm-project/vllm/pull/50047)
  [Bugfix][NIXL] Release a dead peer's NIXL state without waiting for TTL (#50047)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+1 more__
- **2026-09-27** [`eb0f2ca37f`](https://github.com/vllm-project/vllm/commit/eb0f2ca37f) [#49300](https://github.com/vllm-project/vllm/pull/49300)
  [mooncake] support CUSTOM_MEM_POOL in vllm (#49300)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/base.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py` _+3 more__
- **2026-09-26** [`2bb7605ae1`](https://github.com/vllm-project/vllm/commit/2bb7605ae1) [#58473](https://github.com/vllm-project/vllm/pull/58473)
  [Elastic EP] Fix EPLB load statistics during scaling (#58473)
  _Files: `vllm/distributed/elastic_ep/elastic_execute.py`, `vllm/distributed/eplb/eplb_state.py`_
- **2026-09-26** [`b6d2b4fc25`](https://github.com/vllm-project/vllm/commit/b6d2b4fc25) [#51520](https://github.com/vllm-project/vllm/pull/51520)
  [RL] Add sharding-aware NCCL M2N weight transfer (#51520)
  _Files: `.buildkite/test_areas/distributed.yaml`, `docs/training/weight_transfer/README.md`, `docs/training/weight_transfer/m2n.md`, `examples/rl/rlhf_m2n.py` _+9 more__
- **2026-09-25** [`c89b5b4176`](https://github.com/vllm-project/vllm/commit/c89b5b4176) [#58292](https://github.com/vllm-project/vllm/pull/58292)
  [Bugfix][KV Connector] Reap expired NIXL leases behind a heartbeated head (#58292)
  _Files: `tests/v1/kv_connector/unit/test_nixl_heartbeat.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-09-25** [`45d56c0baf`](https://github.com/vllm-project/vllm/commit/45d56c0baf) [#57205](https://github.com/vllm-project/vllm/pull/57205)
  [Core] Model console logging as CLI configuration (#57205)
  _Files: `examples/features/logging_configuration.md`, `tests/conftest.py`, `tests/entrypoints/launchers/test_cli_args.py`, `tests/test_logger.py` _+32 more__
- **2026-09-25** [`442bd00d9f`](https://github.com/vllm-project/vllm/commit/442bd00d9f) [#55072](https://github.com/vllm-project/vllm/pull/55072)
  [Perf][Distributed] Add low-SM multimem reduce-scatter for SM100/SM103 (#55072)
  _Files: `benchmarks/kernels/benchmark_multimem_reduce_scatter.py`, `csrc/custom_all_gather_reduce_scatter.cuh`, `csrc/custom_all_reduce.cuh`, `csrc/libtorch_stable/custom_all_gather_reduce_scatter.cu` _+6 more__
- **2026-09-24** [`6a86bf626e`](https://github.com/vllm-project/vllm/commit/6a86bf626e) [#52245](https://github.com/vllm-project/vllm/pull/52245)
  [PD][PushConnector] Record last activity of remotes on the D side (#52245)
  _Files: `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/push_worker.py`_
- **2026-09-23** [`c4f6ce4874`](https://github.com/vllm-project/vllm/commit/c4f6ce4874) [#58188](https://github.com/vllm-project/vllm/pull/58188)
  [Bugfix][NIXL] Restore successful push completion reporting (#58188)
  _Files: `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/push_worker.py`_
- **2026-09-23** [`9488318c6a`](https://github.com/vllm-project/vllm/commit/9488318c6a) [#57174](https://github.com/vllm-project/vllm/pull/57174)
  [Mooncake] Address review nits from #56855 (#57174)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector_hma.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py` _+1 more__
- **2026-09-21** [`986e217158`](https://github.com/vllm-project/vllm/commit/986e217158) [#53423](https://github.com/vllm-project/vllm/pull/53423)
  [Feature] Add first-class KV hints request envelope for programmatic KV management (#53423)
  _Files: `rust/proto/inference.proto`, `rust/src/chat/src/lib.rs`, `rust/src/engine-core-client/src/protocol/kv_hints.rs`, `rust/src/engine-core-client/src/protocol/mod.rs` _+26 more__
- **2026-09-21** [`7ddd461a28`](https://github.com/vllm-project/vllm/commit/7ddd461a28) [#57742](https://github.com/vllm-project/vllm/pull/57742)
  [Docs] Add ECMooncakeConnector usage example for EPD (#57742)
  _Files: `docs/features/disagg_encoder.md`_

## KV Cache / Offload  (8 commits)

- **2026-09-28** [`a2be4d3cc7`](https://github.com/vllm-project/vllm/commit/a2be4d3cc7) [#58961](https://github.com/vllm-project/vllm/pull/58961)
  [Bugfix][Qwen4Exp] Release the profiling KV cache held by QSA key views (#58961)
  _Files: `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/models/qwen4_exp/common/qsa_cache.py`_
- **2026-09-27** [`cd1daf58a9`](https://github.com/vllm-project/vllm/commit/cd1daf58a9) [#57251](https://github.com/vllm-project/vllm/pull/57251)
  [Metrics][KV Offload] Add Prometheus metrics for SimpleCPUOffloadConnector (#57251)
  _Files: `docs/mkdocs/gen_files/generate_metrics.py`, `docs/usage/metrics.md`, `tests/v1/kv_connector/unit/test_simple_cpu_offload_metrics.py`, `vllm/distributed/kv_transfer/kv_connector/v1/simple_cpu_offload_connector.py` _+2 more__
- **2026-09-25** [`6491f481a7`](https://github.com/vllm-project/vllm/commit/6491f481a7) [#58430](https://github.com/vllm-project/vllm/pull/58430)
  [Bugfix] Stop allocator fragmentation from shrinking the KV cache during memory profiling (#58430)
  _Files: `tests/v1/worker/test_gpu_worker.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-09-24** [`e6c07ea576`](https://github.com/vllm-project/vllm/commit/e6c07ea576) [#51694](https://github.com/vllm-project/vllm/pull/51694)
  [Bugfix][KV Cache] Fix incremental multimodal block hashing (#51694)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-09-24** [`70fc359d25`](https://github.com/vllm-project/vllm/commit/70fc359d25) [#57453](https://github.com/vllm-project/vllm/pull/57453)
  [Bugfix][KV Offload] Retain offload event metadata through batch translation (#57453)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py`_
- **2026-09-23** [`c961121519`](https://github.com/vllm-project/vllm/commit/c961121519) [#58287](https://github.com/vllm-project/vllm/pull/58287)
  [Bugfix] Disable prefix caching for encoder-only before model config hooks (#58287)
  _Files: `vllm/config/vllm.py`_
- **2026-09-22** [`4ec0b95c44`](https://github.com/vllm-project/vllm/commit/4ec0b95c44) [#57113](https://github.com/vllm-project/vllm/pull/57113)
  [CI] Split LM Eval TurboQuant KV Cache into per-config jobs (#57113)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/models-turboquant-k3v4nc.txt`, `tests/evals/gsm8k/configs/models-turboquant-k8v4.txt`, `tests/evals/gsm8k/configs/models-turboquant-t3nc.txt` _+2 more__
- **2026-09-22** [`0bce411a07`](https://github.com/vllm-project/vllm/commit/0bce411a07) [#55390](https://github.com/vllm-project/vllm/pull/55390)
  [Bugfix] Annotate MTP draft KV cache groups positionally on the hybrid grouping path (#55390)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_

## LoRA  (6 commits)

- **2026-09-28** [`953f90d25f`](https://github.com/vllm-project/vllm/commit/953f90d25f) [#57766](https://github.com/vllm-project/vllm/pull/57766)
  [LoRA] Support variable num_labels for sequence classification (#57766)
  _Files: `docs/features/lora.md`, `tests/lora/test_sequence_classification.py`, `vllm/config/lora.py`, `vllm/engine/arg_utils.py` _+4 more__
- **2026-09-28** [`4a190dc518`](https://github.com/vllm-project/vllm/commit/4a190dc518) [#58884](https://github.com/vllm-project/vllm/pull/58884)
  [Model] Enable LoRA support for RobertaForSequenceClassification (#58884)
  _Files: `docs/models/pooling_models/scoring.md`, `vllm/model_executor/models/roberta.py`_
- **2026-09-25** [`83db8c8390`](https://github.com/vllm-project/vllm/commit/83db8c8390) [#55957](https://github.com/vllm-project/vllm/pull/55957)
  [Feature][Frontend] Add granite_thinking_parser reasoning parser for Granite 4.2 (#55957)
  _Files: `docs/features/reasoning_outputs.md`, `tests/parser/engine/replay_harness.py`, `tests/parser/engine/test_replay.py`, `tests/parser/engine/trace_builder.py` _+5 more__
- **2026-09-25** [`b3a87b2d04`](https://github.com/vllm-project/vllm/commit/b3a87b2d04) [#57775](https://github.com/vllm-project/vllm/pull/57775)
  [Bugfix][KVConnector] Finalize saves on steps without a forward (#57775)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_connector/unit/test_kv_connector_lifecycle.py`, `tests/v1/kv_connector/unit/test_lmcache_connector.py`, `tests/v1/worker/test_gpu_kv_connector.py` _+7 more__
- **2026-09-23** [`15ed1262e7`](https://github.com/vllm-project/vllm/commit/15ed1262e7) [#49648](https://github.com/vllm-project/vllm/pull/49648)
  [Bugfix][Tool Parser] Migrate Granite to the streaming Parser Engine (#49648)
  _Files: `tests/parser/engine/test_delegating_replay.py`, `tests/parser/engine/test_granite.py`, `tests/parser/engine/test_replay.py`, `tests/parser/engine/trace_builder.py` _+10 more__
- **2026-09-22** [`d50723df04`](https://github.com/vllm-project/vllm/commit/d50723df04) [#55269](https://github.com/vllm-project/vllm/pull/55269)
  [Rust Frontend] Introduce parser-owned output grammar interfaces (#55269)
  _Files: `rust/Cargo.lock`, `rust/src/chat/src/error.rs`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/default/mod.rs` _+30 more__

## Perf / Benchmark  (4 commits)

- **2026-09-28** [`af7f9488c2`](https://github.com/vllm-project/vllm/commit/af7f9488c2) [#54628](https://github.com/vllm-project/vllm/pull/54628)
  [Benchmark] Add Responses API backend to vllm bench serve (#54628)
  _Files: `docs/benchmarking/cli.md`, `tests/benchmarks/test_responses_request_func.py`, `vllm/benchmarks/datasets/datasets.py`, `vllm/benchmarks/lib/endpoint_request_func.py` _+1 more__
- **2026-09-25** [`f83ea61cfe`](https://github.com/vllm-project/vllm/commit/f83ea61cfe) [#58112](https://github.com/vllm-project/vllm/pull/58112)
  [Benchmark] Record model_id in bench latency/throughput --output-json (#58112)
  _Files: `vllm/benchmarks/latency.py`, `vllm/benchmarks/throughput.py`_
- **2026-09-24** [`71891bdb94`](https://github.com/vllm-project/vllm/commit/71891bdb94) [#58582](https://github.com/vllm-project/vllm/pull/58582)
  [Perf] Parallelize registered CUDA Triton kernel warmup at startup (#58582)
  _Files: `tests/model_executor/test_jit_warmup_triton_launcher.py`, `vllm/envs.py`, `vllm/model_executor/warmup/jit_warmup_triton_helper.py`_
- **2026-09-24** [`5747d4500a`](https://github.com/vllm-project/vllm/commit/5747d4500a) [#57528](https://github.com/vllm-project/vllm/pull/57528)
  [Perf][Frontend] Offload streaming derender detokenization (#57528)
  _Files: `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/renderers/online_derenderer.py`_

## Compilation / CUDA Graph  (4 commits)

- **2026-09-26** [`0239bd2549`](https://github.com/vllm-project/vllm/commit/0239bd2549) [#58810](https://github.com/vllm-project/vllm/pull/58810)
  [CI] Stabilize batch submission in full CUDA graph tests (#58810)
  _Files: `tests/compile/fullgraph/test_full_cudagraph.py`_
- **2026-09-26** [`79ac28c5bd`](https://github.com/vllm-project/vllm/commit/79ac28c5bd) [#58749](https://github.com/vllm-project/vllm/pull/58749)
  [CI] Reduce CUDA graph mode test overhead (#58749)
  _Files: `tests/v1/cudagraph/test_cudagraph_mode.py`_
- **2026-09-23** [`711fc55c10`](https://github.com/vllm-project/vllm/commit/711fc55c10) [#57586](https://github.com/vllm-project/vllm/pull/57586)
  [Perf] Use breakable CUDA graphs (no torch.compile) by default under VLLM_BATCH_INVARIANT so the tuned matmul configs see the runtime M (#57586)
  _Files: `docs/features/batch_invariance.md`, `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-09-21** [`67513c8b67`](https://github.com/vllm-project/vllm/commit/67513c8b67) [#57874](https://github.com/vllm-project/vllm/pull/57874)
  [Bugfix][DSV4.1] Restrict mHC overlap to full CUDA graphs (#57874)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/models/deepseek_v41/nvidia/model.py`, `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`, `vllm/models/deepseek_v41/nvidia/ops/mhc.py`_

## Docs  (2 commits)

- **2026-09-27** [`0c87a197b8`](https://github.com/vllm-project/vllm/commit/0c87a197b8) [#56377](https://github.com/vllm-project/vllm/pull/56377)
  [Bugfix] Disable sequence parallelism / async TP under batch invariance and add a TP regression test (#56377)
  _Files: `docs/features/batch_invariance.md`, `vllm/config/vllm.py`_
- **2026-09-21** [`3e67044972`](https://github.com/vllm-project/vllm/commit/3e67044972) [#57314](https://github.com/vllm-project/vllm/pull/57314)
  [Doc] Refresh Kthena integration guide (#57314)
  _Files: `docs/deployment/integrations/kthena.md`_

---
_Generated 2026-09-28 16:46 UTC_