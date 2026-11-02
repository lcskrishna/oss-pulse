# sgl-project/sglang — Weekly Change Report
**Period:** 2026-10-26 → 2026-11-02  |  **Total commits:** 631

## ✨ New Features This Week

- **2026-11-02** [#42968](https://github.com/sgl-project/sglang/pull/42968) — [Perf] DeepSeek-V4.1: Support indexer TP shard (#42968)
- **2026-11-02** [#47306](https://github.com/sgl-project/sglang/pull/47306) — [Perf] allreduce: enable FlashInfer AllReduce Fusion auto-enable for Kimi-K3 (#47306)
- **2026-11-02** [#47902](https://github.com/sgl-project/sglang/pull/47902) — [Test] [NPU] DeepSeek_v4_pro: Add 16p mix in128k out1k performance and gpqa testcase, DeepSeek_v4_flash:Enable  GPQA case in 950 and add 1p1d gpqa testcase in A3 (#47902)
- **2026-11-02** [#44967](https://github.com/sgl-project/sglang/pull/44967) — [Test] [NPU] kimi_k3: add 128k prefill/decode perf acceptance cases on 4-node mix (#44967)
- **2026-11-02** [#37976](https://github.com/sgl-project/sglang/pull/37976) — [Feat] trace: propagate per-request context to mooncake store RPC for end-to-end request tracing (#37976)
- **2026-11-02** [#47574](https://github.com/sgl-project/sglang/pull/47574) — [Feat] [NPU] eplb: Enable dynamic expert load balancing on Ascend (#47574)
- **2026-11-02** [#30980](https://github.com/sgl-project/sglang/pull/30980) — [Feat] [XPU] graph: Add full prefill graph (#30980)
- **2026-11-02** [#47367](https://github.com/sgl-project/sglang/pull/47367) — [Feat] [NPU] attention: support mixed-chunk on the ascend attention backend (#47367)
- **2026-11-02** [#46580](https://github.com/sgl-project/sglang/pull/46580) — [Feat] diffusion/model: add the BRIA Fibo 2.0 transformer and text conditioning (#46580)
- **2026-11-02** [#42654](https://github.com/sgl-project/sglang/pull/42654) — [Perf] moe: Enable deferred finalize for NVFP4 on the routed TRT-LLM runner (#42654)
- _…and 125 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-11-02** [`16dd97df61`](https://github.com/sgl-project/sglang/commit/16dd97df61) [#46325](https://github.com/sgl-project/sglang/pull/46325) — [Perf] [AMD] deterministic: Use a fixed-order two-stage all-reduce for large inputs (#46325)
- **2026-11-02** [`a133231d31`](https://github.com/sgl-project/sglang/commit/a133231d31) [#47782](https://github.com/sgl-project/sglang/pull/47782) — [Refactor] kernels: Centralize GPU architecture queries in sglang.kernels.arch (#47782)
- **2026-11-02** [`3e88483288`](https://github.com/sgl-project/sglang/commit/3e88483288) [#47844](https://github.com/sgl-project/sglang/pull/47844) — [Doc] [AMD] cookbook: Verify MiniMax-M3.1-Flash High-Throughput on MI355X (#47844)
- **2026-11-02** [`7cad887d53`](https://github.com/sgl-project/sglang/commit/7cad887d53) [#42654](https://github.com/sgl-project/sglang/pull/42654) — [Perf] moe: Enable deferred finalize for NVFP4 on the routed TRT-LLM runner (#42654)
- **2026-11-02** [`f6127bf96e`](https://github.com/sgl-project/sglang/commit/f6127bf96e) [#41639](https://github.com/sgl-project/sglang/pull/41639) — [Feat] [AMD] moe: Add native GLM MXFP4 Triton Gluon backend (#41639)
- **2026-11-02** [`ae66493995`](https://github.com/sgl-project/sglang/commit/ae66493995) [#47030](https://github.com/sgl-project/sglang/pull/47030) — [Fix] [AMD] aiter: Use the layer's KV scales in the legacy target-verify attention (#47030)
- **2026-11-02** [`46e95bb9f9`](https://github.com/sgl-project/sglang/commit/46e95bb9f9) [#47042](https://github.com/sgl-project/sglang/pull/47042) — [Perf] [AMD] aiter: Bucket decode paged-attention partitions by sequence length (#47042)
- **2026-11-02** [`e0c7992d0d`](https://github.com/sgl-project/sglang/commit/e0c7992d0d) [#45332](https://github.com/sgl-project/sglang/pull/45332) — [Fix] [AMD] quark: Load MXFP4 MoE checkpoints on gfx95 and gfx1250 without SGLANG_USE_AITER (#45332)
- **2026-11-01** [`c3654cd93b`](https://github.com/sgl-project/sglang/commit/c3654cd93b) [#46883](https://github.com/sgl-project/sglang/pull/46883) — [Chore] [AMD] docker: Build uTLX into the gfx950 rocm10 images (#46883)
- **2026-11-01** [`e37c1fb020`](https://github.com/sgl-project/sglang/commit/e37c1fb020) [#46691](https://github.com/sgl-project/sglang/pull/46691) — [Feat] [AMD] minimax: gfx950 MoE, router GEMV, block-fp8 GEMM and fp8 producer kernels (#46691)
- **2026-11-01** [`fdf2266c88`](https://github.com/sgl-project/sglang/commit/fdf2266c88) [#46692](https://github.com/sgl-project/sglang/pull/46692) — [Feat] [AMD] distributed: JIT quick all-reduce for TP4 on gfx950 (#46692)
- **2026-11-01** [`03f9054378`](https://github.com/sgl-project/sglang/commit/03f9054378) [#46690](https://github.com/sgl-project/sglang/pull/46690) — [Feat] [AMD] minimax: gfx950 sparse attention, NVFP4 KV and DSpark verify kernels (#46690)
- **2026-11-01** [`b50d439494`](https://github.com/sgl-project/sglang/commit/b50d439494) [#47180](https://github.com/sgl-project/sglang/pull/47180) — [Perf] [AMD] dsa: Replicate the DCP query projection on the owned route (#47180)
- **2026-11-01** [`e232ebf6b0`](https://github.com/sgl-project/sglang/commit/e232ebf6b0) [#47236](https://github.com/sgl-project/sglang/pull/47236) — [Perf] [AMD] moe/topk: Use the Triton softmax top-k router for Qwen3-Next (hidden 2048) (#47236)
- **2026-11-01** [`5831112d03`](https://github.com/sgl-project/sglang/commit/5831112d03) [#46685](https://github.com/sgl-project/sglang/pull/46685) — [CI] [AMD] monokernels: Bump the sgl-amd-mono pin daily (#46685)
- **2026-11-01** [`b146a8576d`](https://github.com/sgl-project/sglang/commit/b146a8576d) [#40708](https://github.com/sgl-project/sglang/pull/40708) — [Perf] [AMD] qwen3.5: Route 512-expert softmax MoE routing through aiter topk_gating (#40708)
- **2026-10-31** [`01fde5cb62`](https://github.com/sgl-project/sglang/commit/01fde5cb62) [#47150](https://github.com/sgl-project/sglang/pull/47150) — [CI] [AMD] pr-test: Run the MI35x 1-GPU stage as one job; move two e2e tests to nightly (#47150)
- **2026-10-31** [`0f92ddaefb`](https://github.com/sgl-project/sglang/commit/0f92ddaefb) [#47568](https://github.com/sgl-project/sglang/pull/47568) — [Perf] [ROCM] diffusion: Encode the MP4 while the VAE decodes on ROCm too (#47568)
- **2026-10-31** [`7585ccc2c0`](https://github.com/sgl-project/sglang/commit/7585ccc2c0) [#47569](https://github.com/sgl-project/sglang/pull/47569) — [Perf] [ROCM] diffusion: Bit-exact fast QK RMSNorm and fused RoPE for MiniMax-H3 (#47569)
- **2026-10-31** [`e93f817325`](https://github.com/sgl-project/sglang/commit/e93f817325) [#47567](https://github.com/sgl-project/sglang/pull/47567) — [Perf] [ROCM] diffusion: Pipeline MiniMax-H3's Ulysses exchange over head groups on RCCL (#47567)
- **2026-10-31** [`6e011a7097`](https://github.com/sgl-project/sglang/commit/6e011a7097) [#47570](https://github.com/sgl-project/sglang/pull/47570) — [Perf] [ROCM] diffusion: Skip dead math-SDPA work in the MiniMax-H3 VAE decoder on gfx950 (#47570)
- **2026-10-31** [`ef4f3f1151`](https://github.com/sgl-project/sglang/commit/ef4f3f1151) [#37367](https://github.com/sgl-project/sglang/pull/37367) — [Perf] [AMD] moe: Resolve MoRI dispatch from the AITER activation contract (#37367)
- **2026-10-31** [`2e80af2857`](https://github.com/sgl-project/sglang/commit/2e80af2857) [#47615](https://github.com/sgl-project/sglang/pull/47615) — [Doc] [AMD] cookbook: Add GLM-5.2 MI355X AgentX recipe (#47615)
- **2026-10-31** [`2f6e7f3475`](https://github.com/sgl-project/sglang/commit/2f6e7f3475) [#44718](https://github.com/sgl-project/sglang/pull/44718) — [Feat] [AMD] mamba: Store hicache checkpoints without a GPU slot (#44718)
- **2026-10-31** [`fb33962605`](https://github.com/sgl-project/sglang/commit/fb33962605) [#47408](https://github.com/sgl-project/sglang/pull/47408) — [Fix] [AMD] quark: Fix the EP>1 crash in the Quark MXFP4 W4A16 MoE path and restrict it to gfx1151 (#47408)
- **2026-10-31** [`1f152be6c5`](https://github.com/sgl-project/sglang/commit/1f152be6c5) [#47520](https://github.com/sgl-project/sglang/pull/47520) — [Doc] [AMD] cookbook: Add Qwen3.8-Flash-Next MI355X AgentX recipe (#47520)
- **2026-10-30** [`a076243cea`](https://github.com/sgl-project/sglang/commit/a076243cea) [#43898](https://github.com/sgl-project/sglang/pull/43898) — [Refactor] scheduler: Remove PD multiplexing (#43898)
- **2026-10-30** [`5628058714`](https://github.com/sgl-project/sglang/commit/5628058714) [#47331](https://github.com/sgl-project/sglang/pull/47331) — [Doc] [AMD] cookbook: Add DCP4 to the GLM-5.2 MI355X MXFP4 high-throughput recipe (#47331)
- **2026-10-30** [`c575b8f36d`](https://github.com/sgl-project/sglang/commit/c575b8f36d) [#47483](https://github.com/sgl-project/sglang/pull/47483) — [Chore] [AMD] mono-kernel: Bump sgl-amd-mono for Qwen3.8-Flash-Next (#47483)
- **2026-10-30** [`02cd9ff0a2`](https://github.com/sgl-project/sglang/commit/02cd9ff0a2) [#47395](https://github.com/sgl-project/sglang/pull/47395) — [Fix] [AMD] scripts: Run and correctly test Dockerfile-only PRs (CI filter + AITER rebuild) (#47395)
- **2026-10-30** [`464187fa95`](https://github.com/sgl-project/sglang/commit/464187fa95) [#47422](https://github.com/sgl-project/sglang/pull/47422) — [Doc] [AMD] cookbook: Update muse-spark recipe 1030 (#47422)
- **2026-10-30** [`a63ea5442b`](https://github.com/sgl-project/sglang/commit/a63ea5442b) [#47419](https://github.com/sgl-project/sglang/pull/47419) — [Chore] release: Bump docs install version to 0.5.23 (#47419)
- **2026-10-30** [`93f4f1a87d`](https://github.com/sgl-project/sglang/commit/93f4f1a87d) [#47152](https://github.com/sgl-project/sglang/pull/47152) — [CI] [AMD] pr-test: Move the Kimi-K2.5 MXFP4 BCG test to nightly (#47152)
- **2026-10-30** [`fcecdad5db`](https://github.com/sgl-project/sglang/commit/fcecdad5db) [#41880](https://github.com/sgl-project/sglang/pull/41880) — [Perf] [AMD] Qwen3.8: AITER FlyDSL hc_mix for Qwen3.8 hyper-connections on gfx950 (#41880)
- **2026-10-30** [`2b11736be1`](https://github.com/sgl-project/sglang/commit/2b11736be1) [#46677](https://github.com/sgl-project/sglang/pull/46677) — [Perf] [AMD] dsv4.1: Wire up 32x32-block fp8 wo_a GEMM (#46677)
- **2026-10-30** [`5035bc97fb`](https://github.com/sgl-project/sglang/commit/5035bc97fb) [#44302](https://github.com/sgl-project/sglang/pull/44302) — [Perf] [AMD] Qwen3.8: Enable fused GDN packing for ratio-3 heads (#44302)
- **2026-10-30** [`0fd1e3a799`](https://github.com/sgl-project/sglang/commit/0fd1e3a799) [#43788](https://github.com/sgl-project/sglang/pull/43788) — [Fix] [AMD] deterministic: Bypass AITER GEMM and MoE in deterministic mode on gfx950 (#43788)
- **2026-10-30** [`96c296b3e8`](https://github.com/sgl-project/sglang/commit/96c296b3e8) [#47054](https://github.com/sgl-project/sglang/pull/47054) — [Test] [AMD] fp8-grid: Compare the GEMM to aiter within one bf16 rounding, not bitwise (#47054)
- **2026-10-30** [`16a3bf3d9d`](https://github.com/sgl-project/sglang/commit/16a3bf3d9d) [#46800](https://github.com/sgl-project/sglang/pull/46800) — [Fix] [AMD] quark: Keep MXFP8 shared experts out of the MXFP4 fused slot on dense-first models (#46800)
- **2026-10-30** [`85af8131e1`](https://github.com/sgl-project/sglang/commit/85af8131e1) [#46833](https://github.com/sgl-project/sglang/pull/46833) — [Fix] [AMD] aiter: Use the layer's softmax scale in MHA prefill and decode (#46833)
- **2026-10-30** [`196ee6b611`](https://github.com/sgl-project/sglang/commit/196ee6b611) [#45486](https://github.com/sgl-project/sglang/pull/45486) — [Fix] [AMD] MoE: Preserve CT FP8 Triton layout and reduction dimensions (#45486)
- **2026-10-30** [`975232c64d`](https://github.com/sgl-project/sglang/commit/975232c64d) [#47394](https://github.com/sgl-project/sglang/pull/47394) — [Doc] [AMD] cookbook: Update Muse Spark Open MI355X AgentX recipe to the 1027 image (#47394)
- **2026-10-30** [`cb4c641b3a`](https://github.com/sgl-project/sglang/commit/cb4c641b3a) [#47362](https://github.com/sgl-project/sglang/pull/47362) — [CI] [AMD] aiter: Update ROCm AITER pin to 26f4f1fb2 (gfx1250 only) (#47362)
- **2026-10-30** [`3b6c28b0b9`](https://github.com/sgl-project/sglang/commit/3b6c28b0b9) [#47118](https://github.com/sgl-project/sglang/pull/47118) — [CI] [AMD] diffusion/ming: Skip the CUDA-only fused RMSNorm test on ROCm (#47118)
- **2026-10-30** [`0b05d49d1f`](https://github.com/sgl-project/sglang/commit/0b05d49d1f) [#47062](https://github.com/sgl-project/sglang/pull/47062) — [Perf] [AMD] attention: Use the AITER FAv3 varlen kernel on gfx942 as well (#47062)
- **2026-10-29** [`f3f23d128c`](https://github.com/sgl-project/sglang/commit/f3f23d128c) [#43895](https://github.com/sgl-project/sglang/pull/43895) — [Refactor] scheduler: Write every request KV length through ReqKvInfo methods (#43895)
- **2026-10-29** [`2c6b95e035`](https://github.com/sgl-project/sglang/commit/2c6b95e035) [#41389](https://github.com/sgl-project/sglang/pull/41389) — [Feat] [AMD] Quark: Run Quark MXFP4 MoE as W4A16 via triton_kernels on RDNA (gfx1151) (#41389)
- **2026-10-29** [`b142fcde83`](https://github.com/sgl-project/sglang/commit/b142fcde83) [#46868](https://github.com/sgl-project/sglang/pull/46868) — [Feat] minimax-m3.1: Support DSpark on Hopper (#46868)
- **2026-10-29** [`686cf98470`](https://github.com/sgl-project/sglang/commit/686cf98470) [#47244](https://github.com/sgl-project/sglang/pull/47244) — [CI] [AMD] workflows: Run scheduled Extra tests, stop skipping nightly tests, merge MI35x 1-GPU jobs- #47238 (#47244)
- **2026-10-29** [`de6c211a49`](https://github.com/sgl-project/sglang/commit/de6c211a49) [#45802](https://github.com/sgl-project/sglang/pull/45802) — [Fix] [AMD] quark: Skip no-copy loads after MXFP4 quantization (#45802)
- **2026-10-29** [`970cbb5fa6`](https://github.com/sgl-project/sglang/commit/970cbb5fa6) [#47162](https://github.com/sgl-project/sglang/pull/47162) — [CI] [AMD] ci: Spread out tests and prefer today's images (#47162)
- **2026-10-29** [`7df65d970d`](https://github.com/sgl-project/sglang/commit/7df65d970d) [#46722](https://github.com/sgl-project/sglang/pull/46722) — [Perf] [AMD] diffusion: Optimize the Wan VAE decode for gfx1250 (#46722)
- **2026-10-29** [`58214f648c`](https://github.com/sgl-project/sglang/commit/58214f648c) [#35151](https://github.com/sgl-project/sglang/pull/35151) — [Feat] [AMD] diffusion: Add quantized attention backends for GFX942/GFX950 (#35151)
- **2026-10-29** [`bd1eb0bb89`](https://github.com/sgl-project/sglang/commit/bd1eb0bb89) [#44465](https://github.com/sgl-project/sglang/pull/44465) — [Perf] [AMD] dsv41: Drop the per-step whole-vocab gather of draft logits via sharded accept (#44465)
- **2026-10-29** [`9df3d27eed`](https://github.com/sgl-project/sglang/commit/9df3d27eed) [#46723](https://github.com/sgl-project/sglang/pull/46723) — [Perf] [AMD] diffusion: Replace the gfx1250 bf16 scale-shift torch fallback with a bit-exact Triton kernel (#46723)
- **2026-10-29** [`2a6c204570`](https://github.com/sgl-project/sglang/commit/2a6c204570) [#47194](https://github.com/sgl-project/sglang/pull/47194) — [CI] [AMD] miles: drop the ROCm 7.2.4 MI35X nightly image build (#47194)
- **2026-10-29** [`00394f9f35`](https://github.com/sgl-project/sglang/commit/00394f9f35) [#44456](https://github.com/sgl-project/sglang/pull/44456) — [Perf] [AMD] mla: Use aiter bf16 batched GEMM for the absorb BMMs on gfx1250 decode (#44456)
- **2026-10-29** [`639dfd0677`](https://github.com/sgl-project/sglang/commit/639dfd0677) [#44455](https://github.com/sgl-project/sglang/pull/44455) — [Perf] [AMD] lm_head: Use aiter tgemm for the bf16 lm_head on gfx1250 (#44455)
- **2026-10-29** [`60d56ea943`](https://github.com/sgl-project/sglang/commit/60d56ea943) [#21194](https://github.com/sgl-project/sglang/pull/21194) — [Fix] [AMD] deepseek-v2/v3: Fix PPMissingLayer AttributeError in aiter_gfx95 code path (#21194)
- **2026-10-29** [`1776e2dcf8`](https://github.com/sgl-project/sglang/commit/1776e2dcf8) [#47163](https://github.com/sgl-project/sglang/pull/47163) — [Fix] [AMD] docker: Remove implicit INT8 QuickReduce default as it causes accuracy issues in 800k+ long context evals (#47163)
- **2026-10-29** [`2d44b55010`](https://github.com/sgl-project/sglang/commit/2d44b55010) [#46625](https://github.com/sgl-project/sglang/pull/46625) — [Fix] kernel-plugins: Serve the MSA plugin behind --enable-nvidia-megakernel (#46625)
- **2026-10-29** [`a99f105294`](https://github.com/sgl-project/sglang/commit/a99f105294) [#46969](https://github.com/sgl-project/sglang/pull/46969) — [CI] permissions: Grant CI access to AMD Hyperloom and paged-experts contributors (#46969)
- **2026-10-29** [`fc778ea2af`](https://github.com/sgl-project/sglang/commit/fc778ea2af) [#46832](https://github.com/sgl-project/sglang/pull/46832) — [Perf] [AMD] qwen3: Use the fused QK-norm + RoPE + KV write in decode with an fp8 KV cache (#46832)
- **2026-10-29** [`100f4d7536`](https://github.com/sgl-project/sglang/commit/100f4d7536) [#46731](https://github.com/sgl-project/sglang/pull/46731) — [Perf] [AMD] moe: Add tuned Triton fused MoE config for gemma-4-26B-A4B on MI355X (#46731)
- **2026-10-29** [`f854e3df13`](https://github.com/sgl-project/sglang/commit/f854e3df13) [#46825](https://github.com/sgl-project/sglang/pull/46825) — [Doc] [AMD] cookbook: Add GLM-5.3 MI355X AgentX recipe (#46825)
- **2026-10-29** [`9497e57c77`](https://github.com/sgl-project/sglang/commit/9497e57c77) [#47151](https://github.com/sgl-project/sglang/pull/47151) — [CI] [AMD] pr-test: Run stage-c-test-large-8-gpu-amd as one job (#47151)
- **2026-10-28** [`c10e0e1773`](https://github.com/sgl-project/sglang/commit/c10e0e1773) [#34031](https://github.com/sgl-project/sglang/pull/34031) — [Refactor] spec: Make ForwardBatch the single channel for the ragged-verify layout (#34031)
- **2026-10-28** [`0faacc3809`](https://github.com/sgl-project/sglang/commit/0faacc3809) [#47122](https://github.com/sgl-project/sglang/pull/47122) — [CI] slash-command: Require explicit hardware for Extra CI (#47122)
- **2026-10-28** [`f1a36c4789`](https://github.com/sgl-project/sglang/commit/f1a36c4789) [#47006](https://github.com/sgl-project/sglang/pull/47006) — [Doc] [AMD] dsv4: Update amd cookbook 1028 (#47006)
- **2026-10-28** [`5ac32ada54`](https://github.com/sgl-project/sglang/commit/5ac32ada54) [#46889](https://github.com/sgl-project/sglang/pull/46889) — [Test] [AMD] diffusion: Compute the VAE blend test's fp16 reference in fp32 on ROCm (#46889)
- **2026-10-28** [`286e018594`](https://github.com/sgl-project/sglang/commit/286e018594) [#46703](https://github.com/sgl-project/sglang/pull/46703) — [CI] [AMD] install: Cache the AOT kernel wheel and stop wiping venv bytecode (#46703)
- **2026-10-28** [`240862923e`](https://github.com/sgl-project/sglang/commit/240862923e) [#46986](https://github.com/sgl-project/sglang/pull/46986) — [Refactor] mem-cache: Bind fused drafts to routed KV views (#46986)
- **2026-10-28** [`f80cb3a2fd`](https://github.com/sgl-project/sglang/commit/f80cb3a2fd) [#46984](https://github.com/sgl-project/sglang/pull/46984) — [Refactor] mem-cache: Replace unified pool variants with a routed cache (#46984)
- **2026-10-28** [`14fea75124`](https://github.com/sgl-project/sglang/commit/14fea75124) [#46983](https://github.com/sgl-project/sglang/pull/46983) — [Fix] [AMD] attention: Avoid fused writes to translated window storage (#46983)
- **2026-10-28** [`306a699a60`](https://github.com/sgl-project/sglang/commit/306a699a60) [#46980](https://github.com/sgl-project/sglang/pull/46980) — [Refactor] mem-cache: Centralize recurrent state ownership and access (#46980)
- **2026-10-28** [`3b597cb76d`](https://github.com/sgl-project/sglang/commit/3b597cb76d) [#46979](https://github.com/sgl-project/sglang/pull/46979) — [Refactor] mem-cache: Route layer access through KV subpool views (#46979)
- **2026-10-28** [`cf3d21b0c9`](https://github.com/sgl-project/sglang/commit/cf3d21b0c9) [#46978](https://github.com/sgl-project/sglang/pull/46978) — [Refactor] mem-cache: Describe KV address translation with ID spaces (#46978)
- **2026-10-28** [`86f72e5b5c`](https://github.com/sgl-project/sglang/commit/86f72e5b5c) [#46861](https://github.com/sgl-project/sglang/pull/46861) — [Fix] [AMD] memory_pool: Keep K and V in separate allocations on ROCm (#46861)
- **2026-10-28** [`edd270fd69`](https://github.com/sgl-project/sglang/commit/edd270fd69) [#44322](https://github.com/sgl-project/sglang/pull/44322) — [Feat] [AMD] dsa: Enable DCP on the triton sparse-MLA backend (#44322)
- **2026-10-28** [`b85d6a8893`](https://github.com/sgl-project/sglang/commit/b85d6a8893) [#42457](https://github.com/sgl-project/sglang/pull/42457) — [Feat] [AMD] mori: Allow MoRI for DeepSeek-V4.1 DSpark PD (#42457)
- **2026-10-28** [`aa8e0a9b6a`](https://github.com/sgl-project/sglang/commit/aa8e0a9b6a) [#41696](https://github.com/sgl-project/sglang/pull/41696) — [Fix] [AMD] dsa: Limit AITER decode metadata to the active batch (#41696)
- **2026-10-28** [`1e7e19285d`](https://github.com/sgl-project/sglang/commit/1e7e19285d) [#44045](https://github.com/sgl-project/sglang/pull/44045) — [Perf] [AMD] batch-invariant: Tune the bf16 matmul for gfx950 (#44045)
- **2026-10-28** [`ef6678fae5`](https://github.com/sgl-project/sglang/commit/ef6678fae5) [#46966](https://github.com/sgl-project/sglang/pull/46966) — [Doc] [AMD] deepseek-v4: Update MI355X C1 mono-kernel recipe (#46966)
- **2026-10-28** [`5858ea88d3`](https://github.com/sgl-project/sglang/commit/5858ea88d3) [#46951](https://github.com/sgl-project/sglang/pull/46951) — [Chore] [AMD] mono-kernel: Bump sgl-amd-mono for MoRI PD decode (#46951)
- **2026-10-28** [`41eaeb0445`](https://github.com/sgl-project/sglang/commit/41eaeb0445) [#33916](https://github.com/sgl-project/sglang/pull/33916) — [Perf] [AMD] kimi-k3: Remove per-layer copies from the aiter MoE path (#33916)
- **2026-10-28** [`45252c64ca`](https://github.com/sgl-project/sglang/commit/45252c64ca) [#46757](https://github.com/sgl-project/sglang/pull/46757) — [Doc] [AMD] cookbook: Add the Qwen3.5 MI355X FP8 agentic recipe covering the GPU-resident and HiCache bands (#46757)
- **2026-10-28** [`5cb41c2416`](https://github.com/sgl-project/sglang/commit/5cb41c2416) [#46902](https://github.com/sgl-project/sglang/pull/46902) — [Chore] [AMD] mono-kernel: Update sgl-amd-mono version (#46902)
- **2026-10-28** [`291f38c390`](https://github.com/sgl-project/sglang/commit/291f38c390) [#44292](https://github.com/sgl-project/sglang/pull/44292) — [Feat] [AMD] torch-profiler: Enable torch.profiler GPU tracing on torch 2.12 / ROCm 10.1 (#44292)
- **2026-10-28** [`20b439ca77`](https://github.com/sgl-project/sglang/commit/20b439ca77) [#46750](https://github.com/sgl-project/sglang/pull/46750) — [CI] [AMD] miles-nightly: Split the 8-GPU suite into two jobs (#46750)
- **2026-10-27** [`2c83dc6656`](https://github.com/sgl-project/sglang/commit/2c83dc6656) [#45555](https://github.com/sgl-project/sglang/pull/45555) — [Perf] [AMD] vattn-asm: Split small-batch MTP verify attention over all CUs on gfx950 (#45555)
- **2026-10-27** [`90a7339419`](https://github.com/sgl-project/sglang/commit/90a7339419) [#46893](https://github.com/sgl-project/sglang/pull/46893) — [Feat] dsv41: Choose where Engram tables live with `--engram-config` (#46893)
- **2026-10-27** [`f9f2665b6e`](https://github.com/sgl-project/sglang/commit/f9f2665b6e) [#44797](https://github.com/sgl-project/sglang/pull/44797) — [Fix] [AMD] moe/topk: Preserve fp32 bias across aiter routing paths (#44797)
- **2026-10-27** [`3145c7ae66`](https://github.com/sgl-project/sglang/commit/3145c7ae66) [#43839](https://github.com/sgl-project/sglang/pull/43839) — [Perf] [AMD] qwen3_5: Quantize the BF16 GDN projections to MXFP4 online (#43839)
- **2026-10-27** [`5044779f0f`](https://github.com/sgl-project/sglang/commit/5044779f0f) [#46036](https://github.com/sgl-project/sglang/pull/46036) — [Feat] [AMD] mono-kernels: Register specs by model type (#46036)
- **2026-10-27** [`cb55d77d37`](https://github.com/sgl-project/sglang/commit/cb55d77d37) [#46774](https://github.com/sgl-project/sglang/pull/46774) — [CI] [AMD] deps: Install openai 2.8.0 in AMD CI for the Responses API (#46774)
- **2026-10-27** [`ec54c220f8`](https://github.com/sgl-project/sglang/commit/ec54c220f8) [#46686](https://github.com/sgl-project/sglang/pull/46686) — [CI] [AMD] diffusion: Skip the CUDA-only Nomas fused-kernel and FlexAttention unit tests on ROCm (#46686)
- **2026-10-27** [`7fe5b127e4`](https://github.com/sgl-project/sglang/commit/7fe5b127e4) [#45678](https://github.com/sgl-project/sglang/pull/45678) — [Fix] disaggregation: Avoid extra GPU contexts with PD (#45678)
- **2026-10-27** [`7e5cd57028`](https://github.com/sgl-project/sglang/commit/7e5cd57028) [#45735](https://github.com/sgl-project/sglang/pull/45735) — [CI] slash-command: Drive opt-in CI tiers from a registry (#45735)
- **2026-10-27** [`f9257d6c7c`](https://github.com/sgl-project/sglang/commit/f9257d6c7c) [#45576](https://github.com/sgl-project/sglang/pull/45576) — [Perf] [AMD] rccl: upgrade rccl to 2.32.3 for rocm10.1 (#45576)
- **2026-10-27** [`a6f5bd397b`](https://github.com/sgl-project/sglang/commit/a6f5bd397b) [#43815](https://github.com/sgl-project/sglang/pull/43815) — [Perf] [AMD] fp8: Use the AITER CK blockscale GEMM by default on gfx942 (#43815)
- **2026-10-27** [`618136d4d3`](https://github.com/sgl-project/sglang/commit/618136d4d3) [#46785](https://github.com/sgl-project/sglang/pull/46785) — [CI] [AMD] docker: Build MORI into the ROCm 10.1 gfx1250 image and fix its CI setup (#46785)
- **2026-10-27** [`61a676125a`](https://github.com/sgl-project/sglang/commit/61a676125a) [#45877](https://github.com/sgl-project/sglang/pull/45877) — [CI] [AMD] test: Skip Mistral-7B and Mixtral-8x7B FP8 in nightly GSM8K eval (#45877)
- **2026-10-27** [`cf04168be1`](https://github.com/sgl-project/sglang/commit/cf04168be1) [#46366](https://github.com/sgl-project/sglang/pull/46366) — [Perf] [AMD] diffusion: Route large BF16 linears to the FlyDSL a16w16 GEMM on gfx1250 (#46366)
- **2026-10-27** [`2b36c718cb`](https://github.com/sgl-project/sglang/commit/2b36c718cb) [#46528](https://github.com/sgl-project/sglang/pull/46528) — [Fix] [AMD] aiter: Fix garbage output with an fp8 KV cache and calibrated KV scales (#46528)
- **2026-10-27** [`db90f584d2`](https://github.com/sgl-project/sglang/commit/db90f584d2) [#45739](https://github.com/sgl-project/sglang/pull/45739) — [Perf] [AMD] Qwen3-Next: fused QK Gemma RMSNorm + partial RoPE on gfx950 (#45739)
- **2026-10-27** [`d69e810f71`](https://github.com/sgl-project/sglang/commit/d69e810f71) [#46708](https://github.com/sgl-project/sglang/pull/46708) — [CI] models: Move less-used model tests to extra and nightly suites (#46708)
- **2026-10-26** [`eb8c2a40ef`](https://github.com/sgl-project/sglang/commit/eb8c2a40ef) [#46340](https://github.com/sgl-project/sglang/pull/46340) — [Fix] [AMD] MiniMax-M3: default SGLANG_MINIMAX_M3_INDEX_TOPK_FREQ to 1 (#46340)
- **2026-10-26** [`01759f0a68`](https://github.com/sgl-project/sglang/commit/01759f0a68) [#39622](https://github.com/sgl-project/sglang/pull/39622) — [Perf] [AMD] dsv4: fp8 target lm_head GEMM for DSPARK verify logits (#39622)
- **2026-10-26** [`7ec4c0d790`](https://github.com/sgl-project/sglang/commit/7ec4c0d790) [#46449](https://github.com/sgl-project/sglang/pull/46449) — [CI] [AMD] diffusion: Skip the CUDA-only gpu-idle and Z-Image RoPE cache unit tests on ROCm (#46449)
- **2026-10-26** [`11550a5845`](https://github.com/sgl-project/sglang/commit/11550a5845) [#46396](https://github.com/sgl-project/sglang/pull/46396) — [CI] [AMD] diffusion: Skip the Wan CuTe DSL q/k norm RoPE imports on ROCm (#46396)
- **2026-10-26** [`ef11eb3b76`](https://github.com/sgl-project/sglang/commit/ef11eb3b76) [#33250](https://github.com/sgl-project/sglang/pull/33250) — [Fix] deepseek-v4: Fix DeepSeek-V4 non-EP TBO for attention TP > 1 (#33250)
- **2026-10-26** [`d19f19d68c`](https://github.com/sgl-project/sglang/commit/d19f19d68c) [#46453](https://github.com/sgl-project/sglang/pull/46453) — [CI] [AMD] pr-test: list tags with ls-remote, 8 small shards (#46453)
- **2026-10-26** [`d96c386335`](https://github.com/sgl-project/sglang/commit/d96c386335) [#45531](https://github.com/sgl-project/sglang/pull/45531) — [Fix] [AMD] attention: Pass the layer softcap to aiter unified-attention decode (#45531)
- **2026-10-26** [`6a28c96a49`](https://github.com/sgl-project/sglang/commit/6a28c96a49) [#45713](https://github.com/sgl-project/sglang/pull/45713) — [Perf] [AMD] kda: Use a HIP fused decode kernel by default for KDA (Kimi-K3) on gfx950 (#45713)
- **2026-10-26** [`c8398cb3a3`](https://github.com/sgl-project/sglang/commit/c8398cb3a3) [#45710](https://github.com/sgl-project/sglang/pull/45710) — [Perf] [AMD] kda: Use a HIP chunked-prefill kernel for KDA on gfx950 (#45710)
- **2026-10-26** [`0cd2a63b36`](https://github.com/sgl-project/sglang/commit/0cd2a63b36) [#41899](https://github.com/sgl-project/sglang/pull/41899) — [Perf] [AMD] quark/Qwen3.8: Quantize the BF16 shared expert of Quark MXFP4 checkpoints to MXFP4 while loading for shared-expert fusion (#41899)
- **2026-10-26** [`5b0be031e7`](https://github.com/sgl-project/sglang/commit/5b0be031e7) [#46236](https://github.com/sgl-project/sglang/pull/46236) — [Fix] [AMD] dsv4.1: Fix the V4.1 k-norm-rope store build on ROCm 10 (#46236)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#45189](https://github.com/sgl-project/sglang/issues/45189) | [RFC] Session-Aware KV Cache Orchestration for SGLang Router and HiCac | — | 2026-11-02 |
| [#44304](https://github.com/sgl-project/sglang/issues/44304) | [ROCm][AMD] Qwen3.8-Flash-Next gfx950 / MI355X Performance Optimizatio | — | 2026-11-02 |
| [#42752](https://github.com/sgl-project/sglang/issues/42752) | [CI] Flaky tests and CI infrastructure failures seen while babysitting | — | 2026-11-02 |
| [#47932](https://github.com/sgl-project/sglang/issues/47932) | [Bug] expert_distribution_recorder records all-zero counts under `flas | — | 2026-11-02 |
| [#47896](https://github.com/sgl-project/sglang/issues/47896) | [Bug] Qwen3.5 GatedDeltaNet: finalize_fused_in_proj builds the fused i | — | 2026-11-02 |
| [#47830](https://github.com/sgl-project/sglang/issues/47830) | [Bug] Hybrid Mamba model + EAGLE: KV-cache sizing error says to raise  | — | 2026-11-02 |
| [#46487](https://github.com/sgl-project/sglang/issues/46487) | [RoadMap] [NPU] NPU Backend Refactor Roadmap | npu, roadmap | 2026-11-02 |
| [#46520](https://github.com/sgl-project/sglang/issues/46520) | [RFC] [XPU] paged-experts: Intel XPU support with Lookahead Expert Sch | — | 2026-11-02 |
| [#47801](https://github.com/sgl-project/sglang/issues/47801) | [Bug] [AMD] diffusion: Qwen-Image 2.1 VAE decode is not deterministic  | — | 2026-11-01 |
| [#47797](https://github.com/sgl-project/sglang/issues/47797) | [RFC] Define per-request speculative decoding opt-out execution semant | — | 2026-11-01 |
| [#32321](https://github.com/sgl-project/sglang/issues/32321) | [RFC] Apple Silicon serving redesign: Torch-owned SRT path with an exp | apple-silicon | 2026-11-01 |
| [#47481](https://github.com/sgl-project/sglang/issues/47481) | [Performance] Reproducible cache hit-rate dip during L2/L3 capacity pr | — | 2026-11-01 |
| [#37372](https://github.com/sgl-project/sglang/issues/37372) | [Feature] [RFC] [HiCache] Out-of-process HiCache data plane with devic | — | 2026-11-01 |
| [#39499](https://github.com/sgl-project/sglang/issues/39499) | [Roadmap] SGLang dLLM Serving | — | 2026-11-01 |
| [#43098](https://github.com/sgl-project/sglang/issues/43098) | Agentic Cache Scheduling System Roadmap (Q4) | — | 2026-11-01 |
| [#47444](https://github.com/sgl-project/sglang/issues/47444) | [Bug] NemotronHConfig rejects transformers 5 layer types `linear_atten | — | 2026-10-31 |
| [#47508](https://github.com/sgl-project/sglang/issues/47508) | [Bug][ROCm] Kimi-K3 fused KDA input-projection buffers are replaced on | — | 2026-10-31 |
| [#47624](https://github.com/sgl-project/sglang/issues/47624) | [RFC] NPU RL Test Consolidation: File Ownership, Coverage Docstrings,  | — | 2026-10-31 |
| [#32774](https://github.com/sgl-project/sglang/issues/32774) | [Roadmap] Integrate NCCL 2.30 Features into SGLang | — | 2026-10-31 |
| [#47562](https://github.com/sgl-project/sglang/issues/47562) | [AITER-Upgrade] PR readiness gfx1250 (MI45x) | — | 2026-10-31 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 151 |
| Multimodal | 103 |
| Prefill / Decode Disaggregation | 72 |
| MoE / Expert Parallel | 66 |
| KV Cache / Memory | 37 |
| ROCm / AMD | 31 |
| Tensor / Data Parallel | 28 |
| Scheduler / Batching | 26 |
| Triton / Kernels | 25 |
| CI / Build | 19 |
| Other | 19 |
| Quantization | 16 |
| Speculative Decoding | 12 |
| Models | 8 |
| Docs / Examples | 7 |
| Serving / API | 5 |
| LoRA | 3 |
| Structured Output | 3 |

## Attention / FlashInfer  (151 commits)

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
- **2026-11-01** [`03f9054378`](https://github.com/sgl-project/sglang/commit/03f9054378) [#46690](https://github.com/sgl-project/sglang/pull/46690)
  [Feat] [AMD] minimax: gfx950 sparse attention, NVFP4 KV and DSpark verify kernels (#46690)
  _Files: `python/sglang/kernels/jit/csrc/kvcacheio/page_row.cuh`, `python/sglang/kernels/ops/attention/minimax_m3_qk_norm_rope.py`, `python/sglang/kernels/ops/attention/minimax_sparse/common/nvfp4.py`, `python/sglang/kernels/ops/attention/minimax_sparse/common/nvfp4_gfx950.py` _+21 more__
- **2026-11-01** [`cdc2f7d1b2`](https://github.com/sgl-project/sglang/commit/cdc2f7d1b2) [#47789](https://github.com/sgl-project/sglang/pull/47789)
  [CI] nightly: Disable the MiniMax-M3.1-Flash H200 test while it times out (#47789)
  _Files: `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py`_
- **2026-11-01** [`b50d439494`](https://github.com/sgl-project/sglang/commit/b50d439494) [#47180](https://github.com/sgl-project/sglang/pull/47180)
  [Perf] [AMD] dsa: Replicate the DCP query projection on the owned route (#47180)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`, `python/sglang/srt/models/deepseek_v2.py` _+1 more__
- **2026-11-01** [`f171859219`](https://github.com/sgl-project/sglang/commit/f171859219) [#47684](https://github.com/sgl-project/sglang/pull/47684)
  [Perf] attention: Round the DeepSeek-V4.1 dense indexer logits tiles to whole SM waves (#47684)
  _Files: `python/sglang/kernels/ops/attention/dsv4/index_logits.py`_
- **2026-11-01** [`1ad0149814`](https://github.com/sgl-project/sglang/commit/1ad0149814) [#47686](https://github.com/sgl-project/sglang/pull/47686)
  [Perf] diffusion: Nomas camera attention reads each frame's value directly when camera_chunk_size is 1 (#47686)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/nomas.py`, `python/sglang/multimodal_gen/test/unit/test_nomas.py`_
- **2026-11-01** [`928e285bc1`](https://github.com/sgl-project/sglang/commit/928e285bc1) [#38943](https://github.com/sgl-project/sglang/pull/38943)
  [Feat] dcp: Support breakable prefill CUDA graphs under decode context parallelism (#38943)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `test/registered/unit/model_executor/test_prefill_cuda_graph_dcp.py`_
- **2026-11-01** [`4f45b15e74`](https://github.com/sgl-project/sglang/commit/4f45b15e74) [#47121](https://github.com/sgl-project/sglang/pull/47121)
  [Perf] diffusion: Wan-Animate-2 1.7x faster denoising via exact FA3 in-context attention, opt-in FP8 reference K/V (#47121)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/models/dits/wan_animate_2.py`, `python/sglang/multimodal_gen/runtime/models/dits/wan_animate_2_block.py`, `python/sglang/multimodal_gen/runtime/models/dits/wan_animate_2_clip_conditioning.py` _+1 more__
- **2026-11-01** [`d8c28b1231`](https://github.com/sgl-project/sglang/commit/d8c28b1231) [#47705](https://github.com/sgl-project/sglang/pull/47705)
  [Refactor] memory-pool: Rename index key format to layout (#47705)
  _Files: `python/sglang/srt/mem_cache/device_pool_info.py`, `python/sglang/srt/mem_cache/hybrid_cache/host_pool_config.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+4 more__
- **2026-11-01** [`ee83f5a2e4`](https://github.com/sgl-project/sglang/commit/ee83f5a2e4) [#40916](https://github.com/sgl-project/sglang/pull/40916)
  [Refactor] memory-pool: Build QSA indexer host pools from buffer info (#40916)
  _Files: `python/sglang/srt/mem_cache/device_pool_info.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/pool_host/qsa.py`, `python/sglang/srt/mem_cache/qsa_kv_pool.py` _+1 more__
- **2026-11-01** [`8d12b65e54`](https://github.com/sgl-project/sglang/commit/8d12b65e54) [#47029](https://github.com/sgl-project/sglang/pull/47029)
  [Fix] attention: Compute extend attention KV offsets in int64 (#47029)
  _Files: `python/sglang/kernels/ops/attention/extend_attention.py`, `test/registered/attention/test_triton_attention_kernels.py`_
- **2026-11-01** [`5032f9881b`](https://github.com/sgl-project/sglang/commit/5032f9881b) [#47566](https://github.com/sgl-project/sglang/pull/47566)
  [Perf] diffusion/minimax-h3: Skip attention for the packing's alignment rows in the Ulysses pipeline (#47566)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_dit_contract.py`_
- **2026-11-01** [`592754fc5e`](https://github.com/sgl-project/sglang/commit/592754fc5e) [#47699](https://github.com/sgl-project/sglang/pull/47699)
  [Doc] cookbook: Add MiniMax-M3.1-Flash GB300 PD AgentX points (#47699)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`_
- **2026-11-01** [`8817f63c2c`](https://github.com/sgl-project/sglang/commit/8817f63c2c) [#47586](https://github.com/sgl-project/sglang/pull/47586)
  [Perf] diffusion: keep GQA and MOSS-Image attention on cuDNN SDPA on Blackwell (#47586)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py`, `python/sglang/multimodal_gen/runtime/models/dits/moss_image.py`, `python/sglang/multimodal_gen/test/unit/test_dynamic_cudnn_sdpa_routing.py`_
- **2026-10-31** [`60b183d5c3`](https://github.com/sgl-project/sglang/commit/60b183d5c3) [#47532](https://github.com/sgl-project/sglang/pull/47532)
  [Feat] rust-server: Reach every attention-DP rank with aborts and publish the listener map (#47532)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/request_receiver.py`, `python/sglang/srt/rust_server/server.py`, `rust/sglang-server/src/api_server/grpc/info.rs` _+9 more__
- **2026-10-31** [`9780c52155`](https://github.com/sgl-project/sglang/commit/9780c52155) [#46936](https://github.com/sgl-project/sglang/pull/46936)
  [Feat] hicache: Store MXFP8 KV pages in L3 as payload + scales objects (#46936)
  _Files: `python/sglang/srt/mem_cache/pool_host/mha_mxfp8.py`, `test/registered/unit/mem_cache/test_mxfp8_mha_pool_host_unit.py`_
- **2026-10-31** [`dff2c4e102`](https://github.com/sgl-project/sglang/commit/dff2c4e102) [#45020](https://github.com/sgl-project/sglang/pull/45020)
  [Refactor] memory-pool: Build unified page-envelope host pools from buffer info (#45020)
  _Files: `python/sglang/srt/mem_cache/device_pool_info.py`, `python/sglang/srt/mem_cache/kv/layout/mha.py`, `python/sglang/srt/mem_cache/pool_host/unified.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`_
- **2026-10-31** [`8368f86fd7`](https://github.com/sgl-project/sglang/commit/8368f86fd7) [#46908](https://github.com/sgl-project/sglang/pull/46908)
  [Perf] [NVIDIA] qwen3: Reuse fused QK-norm/RoPE kernel for decode (#46908)
  _Files: `python/sglang/kernels/ops/attention/table_qk_norm_rope.py`, `python/sglang/srt/models/qwen3.py`, `test/registered/kernels/ops/attention/test_table_qk_norm_rope.py`, `test/registered/unit/models/test_qwen3_qk_norm_rope.py`_
- **2026-10-31** [`b44b02e510`](https://github.com/sgl-project/sglang/commit/b44b02e510) [#45019](https://github.com/sgl-project/sglang/pull/45019)
  [Refactor] memory-pool: Build DSA indexer host pools from buffer info (#45019)
  _Files: `python/sglang/srt/mem_cache/device_pool_info.py`, `python/sglang/srt/mem_cache/hybrid_cache/host_pool_config.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/kv/layout/mha.py` _+13 more__
- **2026-10-31** [`504f9cf720`](https://github.com/sgl-project/sglang/commit/504f9cf720) [#47301](https://github.com/sgl-project/sglang/pull/47301)
  [Fix] diffusion: select Blackwell subtile attention by execution mode and quality (#47301)
  _Files: `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py`, `python/sglang/multimodal_gen/runtime/managers/forward_context.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py` _+6 more__
- **2026-10-31** [`e93f817325`](https://github.com/sgl-project/sglang/commit/e93f817325) [#47567](https://github.com/sgl-project/sglang/pull/47567)
  [Perf] [ROCM] diffusion: Pipeline MiniMax-H3's Ulysses exchange over head groups on RCCL (#47567)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/usp.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/single_test_file/test_usp_pipelined_attention_multi_gpu.py`_
- **2026-10-31** [`67bd749ada`](https://github.com/sgl-project/sglang/commit/67bd749ada) [#47565](https://github.com/sgl-project/sglang/pull/47565)
  [Perf] diffusion: Pipeline Ulysses attention over head groups down to three waves (#47565)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/device_communicators/ipc_a2a_multi.py`, `python/sglang/multimodal_gen/test/single_test_file/test_ipc_a2a_multi_gpu.py`_
- **2026-10-31** [`6e011a7097`](https://github.com/sgl-project/sglang/commit/6e011a7097) [#47570](https://github.com/sgl-project/sglang/pull/47570)
  [Perf] [ROCM] diffusion: Skip dead math-SDPA work in the MiniMax-H3 VAE decoder on gfx950 (#47570)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/attention.py`, `test/registered/kernels/ops/diffusion/test_minimax_h3_vae_output.py`_
- **2026-10-31** [`53a8a22fb1`](https://github.com/sgl-project/sglang/commit/53a8a22fb1) [#45293](https://github.com/sgl-project/sglang/pull/45293)
  [CI] [NPU] tests: Add GSM8K PR gate for DSV4-Flash W8A8 8P GPQA (#45293)
  _Files: `test/registered/npu/accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_gpqa.py`_
- **2026-10-31** [`7adb930d63`](https://github.com/sgl-project/sglang/commit/7adb930d63) [#47623](https://github.com/sgl-project/sglang/pull/47623)
  [Doc] cookbook: Update MiniMax-M3.1-Flash AgentX launches (#47623)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`_
- **2026-10-31** [`b20fdd2eb3`](https://github.com/sgl-project/sglang/commit/b20fdd2eb3) [#45876](https://github.com/sgl-project/sglang/pull/45876)
  [Perf] DFLASH: route draft bf16 GEMMs through tuned dispatch on GB300 (#45876)
  _Files: `python/sglang/kernels/ops/gemm/cutedsl_bf16_gemm.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/models/dflash.py`_
- **2026-10-31** [`2ccbdab65f`](https://github.com/sgl-project/sglang/commit/2ccbdab65f) [#47387](https://github.com/sgl-project/sglang/pull/47387)
  [Perf] [NVIDIA] dsv41: Balance the SM90 paged decode indexer's tiles across the GPU so one long context no longer sets the step time (#47387)
  _Files: `python/sglang/kernels/ops/attention/dsv4/fp4_indexer.py`, `python/sglang/srt/environ.py`, `test/registered/kernels/ops/attention/test_fp4_indexer.py`_
- **2026-10-31** [`9d33af853b`](https://github.com/sgl-project/sglang/commit/9d33af853b) [#44442](https://github.com/sgl-project/sglang/pull/44442)
  [Feat] [NPU] GLM-4.1V: Add ModelSlim W8A8S support with multimodal serving optimizations (#44442)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/linear_method_npu.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/layers/quantization/modelslim/schemes/modelslim_w8a8_int8.py` _+1 more__
- **2026-10-31** [`26452a6cfa`](https://github.com/sgl-project/sglang/commit/26452a6cfa) [#47560](https://github.com/sgl-project/sglang/pull/47560)
  [Doc] cookbook: Add Qwen3.8-Flash-Next B300 NVFP4 AgentX recipes (#47560)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next-b300.jsx`_
- **2026-10-31** [`006ad25169`](https://github.com/sgl-project/sglang/commit/006ad25169) [#45174](https://github.com/sgl-project/sglang/pull/45174)
  [Fix] Minimax-M3: Deterministic tie-breaking in the CUDA radix decode top-k (#45174)
  _Files: `python/sglang/kernels/jit/csrc/minimax/minimax_decode_topk.cuh`, `test/registered/kernels/ops/attention/test_minimax_decode_topk.py`_
- **2026-10-31** [`1a50817ed0`](https://github.com/sgl-project/sglang/commit/1a50817ed0) [#47380](https://github.com/sgl-project/sglang/pull/47380)
  [Doc] [NPU] docs: Rename NPU hardware to A2/A3 Series products (#47380)
  _Files: `docs/docs/hardware-platforms/ascend-npus/evaluation/accuracy_evaluation.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/quick_start.mdx`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/best-practices/deepseek_r1.mdx` _+25 more__
- **2026-10-31** [`1f152be6c5`](https://github.com/sgl-project/sglang/commit/1f152be6c5) [#47520](https://github.com/sgl-project/sglang/pull/47520)
  [Doc] [AMD] cookbook: Add Qwen3.8-Flash-Next MI355X AgentX recipe (#47520)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx`_
- **2026-10-31** [`a2cafa5676`](https://github.com/sgl-project/sglang/commit/a2cafa5676) [#38565](https://github.com/sgl-project/sglang/pull/38565)
  [Fix] sampling: deterministic top-p / top-k renorm when tp_size > 1 (TP rank divergence in DFlash/DSpark) (#38565)
  _Files: `python/sglang/kernels/ops/sampling/renorm.py`, `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/layers/sampling_renorm.py`, `python/sglang/srt/speculative/dflash_utils.py` _+5 more__
- **2026-10-30** [`a959f319f4`](https://github.com/sgl-project/sglang/commit/a959f319f4) [#46857](https://github.com/sgl-project/sglang/pull/46857)
  [Perf] GLM-5.3: Restore TP decode fusion and graph sizing with CP prefill (#46857)
  _Files: `python/sglang/srt/layers/cp/cp_decode_attn_tp.py`, `python/sglang/srt/layers/layer_boundary/exit.py`, `python/sglang/srt/layers/layer_boundary/factories.py`, `python/sglang/srt/layers/layer_boundary/fusions/allreduce.py` _+13 more__
- **2026-10-30** [`e4bb0478c5`](https://github.com/sgl-project/sglang/commit/e4bb0478c5) [#47540](https://github.com/sgl-project/sglang/pull/47540)
  [Fix] spec: Seed the DSpark MLA draft weights in the verify-rows test (#47540)
  _Files: `test/registered/unit/spec/test_dflash_mla.py`_
- **2026-10-30** [`783b3905b1`](https://github.com/sgl-project/sglang/commit/783b3905b1) [#42248](https://github.com/sgl-project/sglang/pull/42248)
  [Perf] srt: Native tensor output and prefill scoring optimizations (#42248)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/graph_utils.py` _+17 more__
- **2026-10-30** [`6fb0fd97fd`](https://github.com/sgl-project/sglang/commit/6fb0fd97fd) [#47130](https://github.com/sgl-project/sglang/pull/47130)
  [Fix] bench: Size the one-batch KV-capacity skip by the heaviest attention-DP rank for ragged batches (#47130)
  _Files: `python/sglang/benchmark/one_batch_server.py`, `test/registered/unit/bench/test_one_batch_ragged_capacity.py`_
- **2026-10-30** [`60e84e91cd`](https://github.com/sgl-project/sglang/commit/60e84e91cd) [#46454](https://github.com/sgl-project/sglang/pull/46454)
  [Perf] diffusion: HunyuanImage-3 prefix K/V cache, opt-in FA3 attention and think-prompt support (#46454)
  _Files: `python/sglang/multimodal_gen/configs/sample/hunyuan_image3.py`, `python/sglang/multimodal_gen/runtime/models/dits/hunyuan_image3.py`, `python/sglang/multimodal_gen/runtime/models/dits/hunyuan_image3_utils.py`, `python/sglang/multimodal_gen/runtime/pipelines/hunyuan_image3.py` _+4 more__
- **2026-10-30** [`8ecabd3c1e`](https://github.com/sgl-project/sglang/commit/8ecabd3c1e) [#46720](https://github.com/sgl-project/sglang/pull/46720)
  [Fix] cuda-graph: Keep attention metadata and SP workspaces alive across graph variants of a batch size (#46720)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py` _+11 more__
- **2026-10-30** [`dde1ef21a0`](https://github.com/sgl-project/sglang/commit/dde1ef21a0) [#47319](https://github.com/sgl-project/sglang/pull/47319)
  [Fix] rust-server: Serve /v1/loads from every listener under multi-node DP attention (#47319)
  _Files: `python/sglang/srt/managers/load_snapshot.py`, `python/sglang/srt/rust_server/config.py`, `test/registered/unit/entrypoints/test_rust_server_dp_ports.py`, `test/registered/unit/managers/test_load_snapshot_backends.py`_
- **2026-10-30** [`c575b8f36d`](https://github.com/sgl-project/sglang/commit/c575b8f36d) [#47483](https://github.com/sgl-project/sglang/pull/47483)
  [Chore] [AMD] mono-kernel: Bump sgl-amd-mono for Qwen3.8-Flash-Next (#47483)
  _Files: `python/pyproject_other.toml`_
- **2026-10-30** [`9691e711cd`](https://github.com/sgl-project/sglang/commit/9691e711cd) [#47464](https://github.com/sgl-project/sglang/pull/47464)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main ea8b3439 (#47464)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4_1.jsx` _+3 more__
- **2026-10-30** [`56a8d3a8d7`](https://github.com/sgl-project/sglang/commit/56a8d3a8d7) [#44438](https://github.com/sgl-project/sglang/pull/44438)
  [Fix] deterministic: Validate the per-phase attention backends (#44438)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-10-30** [`72576df88d`](https://github.com/sgl-project/sglang/commit/72576df88d) [#39947](https://github.com/sgl-project/sglang/pull/39947)
  [Feat] [NPU] DSpark: Support dsv4 dspark on ascend 950 (#39947)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_draft_model.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_dsv4_backend.py`, `python/sglang/srt/hardware_backend/npu/utils.py`, `python/sglang/srt/models/deepseek_v4.py` _+3 more__
- **2026-10-30** [`2b11736be1`](https://github.com/sgl-project/sglang/commit/2b11736be1) [#46677](https://github.com/sgl-project/sglang/pull/46677)
  [Perf] [AMD] dsv4.1: Wire up 32x32-block fp8 wo_a GEMM (#46677)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/models/deepseek_common/amd/deepseek_v4_hip.py`, `python/sglang/srt/models/deepseek_common/amd/deepseek_v4_wo_a_fp8.py`, `python/sglang/srt/models/deepseek_v4.py` _+1 more__
- **2026-10-30** [`85af8131e1`](https://github.com/sgl-project/sglang/commit/85af8131e1) [#46833](https://github.com/sgl-project/sglang/pull/46833)
  [Fix] [AMD] aiter: Use the layer's softmax scale in MHA prefill and decode (#46833)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/aiter_utils.py`, `test/registered/attention/test_aiter_fp8_kv_scales_paths.py`_
- **2026-10-30** [`b572b8ea82`](https://github.com/sgl-project/sglang/commit/b572b8ea82) [#45839](https://github.com/sgl-project/sglang/pull/45839)
  [BugFix][HiCache * BCG] bind captured KDA waits to live load events (#45839)
  _Files: `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_backend/breakable_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_backend/utils.py` _+4 more__
- **2026-10-30** [`0b05d49d1f`](https://github.com/sgl-project/sglang/commit/0b05d49d1f) [#47062](https://github.com/sgl-project/sglang/pull/47062)
  [Perf] [AMD] attention: Use the AITER FAv3 varlen kernel on gfx942 as well (#47062)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py`_
- **2026-10-30** [`0d01c3c129`](https://github.com/sgl-project/sglang/commit/0d01c3c129) [#46627](https://github.com/sgl-project/sglang/pull/46627)
  [Test] minimax-m3.1: Add nightly e2e tests on H200 and B300 (#46627)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`, `test/registered/e2e/models_large/test_minimax_m31_flash_gb300.py`, `test/registered/e2e/models_large/test_minimax_m31_flash_h200.py`_
- **2026-10-30** [`6162b07199`](https://github.com/sgl-project/sglang/commit/6162b07199) [#42725](https://github.com/sgl-project/sglang/pull/42725)
  [Fix] [Intel] attention: Allow page_size=1 on the Intel XPU backend (#42725)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/unlimited_ocr.py`, `python/sglang/srt/layers/attention/xpu_backend.py`, `python/sglang/srt/parser/conversation.py` _+4 more__
- **2026-10-30** [`0f3f619850`](https://github.com/sgl-project/sglang/commit/0f3f619850) [#40746](https://github.com/sgl-project/sglang/pull/40746)
  [Fix] [NPU] mtp: fix darft fias-v2 branch when fias v2 on (#40746)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-10-30** [`a48263b2f1`](https://github.com/sgl-project/sglang/commit/a48263b2f1) [#44457](https://github.com/sgl-project/sglang/pull/44457)
  [Perf] attention: Skip the triton MLA K rescale when k_scale is 1.0 (#44457)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`_
- **2026-10-29** [`da4ffac806`](https://github.com/sgl-project/sglang/commit/da4ffac806) [#47328](https://github.com/sgl-project/sglang/pull/47328)
  [Perf] [NVIDIA] deep_select: Add a 3-CTA tier for the paged indexer top-k (#47328)
  _Files: `python/sglang/kernels/jit/csrc/deep_select/entry.cuh`, `python/sglang/kernels/jit/csrc/deep_select/vendor/cuda_kernels/common_parts.cuh`, `python/sglang/kernels/ops/attention/deep_select.py`, `test/registered/kernels/ops/attention/test_deep_select.py`_
- **2026-10-29** [`fbc90a860e`](https://github.com/sgl-project/sglang/commit/fbc90a860e) [#47286](https://github.com/sgl-project/sglang/pull/47286)
  [Fix] attention: Skip the MSA-v1 QMUL4 prefill case when QMUL4 is unavailable (#47286)
  _Files: `test/registered/kernels/ops/attention/test_minimax_m31_page_row_views.py`_
- **2026-10-29** [`d213124956`](https://github.com/sgl-project/sglang/commit/d213124956) [#47303](https://github.com/sgl-project/sglang/pull/47303)
  [Doc] cookbook: Add MiniMax-M3.1-Flash B300 TP2 SPF AgentX points (#47303)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`_
- **2026-10-29** [`b142fcde83`](https://github.com/sgl-project/sglang/commit/b142fcde83) [#46868](https://github.com/sgl-project/sglang/pull/46868)
  [Feat] minimax-m3.1: Support DSpark on Hopper (#46868)
  _Files: `python/sglang/srt/arg_groups/fields/spec.py`, `python/sglang/srt/arg_groups/model_overrides/minimax_m3.py`, `python/sglang/srt/layers/attention/minimax_sparse_backend.py`, `test/registered/amd/test_minimax_rocm_verify.py` _+2 more__
- **2026-10-29** [`d39c8f94f0`](https://github.com/sgl-project/sglang/commit/d39c8f94f0) [#45765](https://github.com/sgl-project/sglang/pull/45765)
  [Feat] glm5: Expose per-layer MLA key buffer and use_fused_topk in binding (#45765)
  _Files: `python/sglang/srt/kernel_plugins/nvidia/binding.py`, `test/registered/unit/kernel_plugins/nvidia/test_megakernel_binding.py`_
- **2026-10-29** [`8b6de6719d`](https://github.com/sgl-project/sglang/commit/8b6de6719d) [#47092](https://github.com/sgl-project/sglang/pull/47092)
  [Fix] diffusion: fix colored seams in single-GPU Qwen-Image-2.1-Turbo VAE tiling (#47092)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/autoencoder_kl_qwenimage21.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21_attention_barrier.py`_
- **2026-10-29** [`e6ca9285e4`](https://github.com/sgl-project/sglang/commit/e6ca9285e4) [#46851](https://github.com/sgl-project/sglang/pull/46851)
  [Fix] dspark/MiniMax-M3.1-Flash: Inject decode-step draft KV under the draft's TP placement (#46851)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`_
- **2026-10-29** [`149dc279d9`](https://github.com/sgl-project/sglang/commit/149dc279d9) [#47061](https://github.com/sgl-project/sglang/pull/47061)
  [Fix] [NPU] kimi-k3: fix npu fused_sigmoid_gating_delta_rule (#47061)
  _Files: `python/sglang/kernels/ops/attention/linear/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_kda_backend.py`_
- **2026-10-29** [`4aad3283bd`](https://github.com/sgl-project/sglang/commit/4aad3283bd) [#46709](https://github.com/sgl-project/sglang/pull/46709)
  [Refactor] diffusion/bcg: Share graph-pool output management (#46709)
  _Files: `docs/docs/advanced_features/breakable_cuda_graph.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3_vdn_attention.py` _+4 more__
- **2026-10-29** [`58214f648c`](https://github.com/sgl-project/sglang/commit/58214f648c) [#35151](https://github.com/sgl-project/sglang/pull/35151)
  [Feat] [AMD] diffusion: Add quantized attention backends for GFX942/GFX950 (#35151)
  _Files: `docs/docs/sglang-diffusion/attention_backends.mdx`, `python/sglang/multimodal_gen/configs/models/adapter/base.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter_quant.py`, `python/sglang/multimodal_gen/runtime/models/dits/base.py` _+5 more__
- **2026-10-29** [`3abe1c8527`](https://github.com/sgl-project/sglang/commit/3abe1c8527) [#46780](https://github.com/sgl-project/sglang/pull/46780)
  [Feat] rust: Parse DeepSeek-V4/V4.1 output with deepseek-recipe (#46780)
  _Files: `.agents/skills/processor-model-parity/SKILL.md`, `.github/workflows/pr-test-rust-workspace.yml`, `python/sglang/srt/function_call/deepseekv4_detector.py`, `python/sglang/srt/parser/deepseek_recipe_output.py` _+31 more__
- **2026-10-29** [`b069d22a9c`](https://github.com/sgl-project/sglang/commit/b069d22a9c) [#47214](https://github.com/sgl-project/sglang/pull/47214)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main 70a76017 (#47214)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+4 more__
- **2026-10-29** [`00394f9f35`](https://github.com/sgl-project/sglang/commit/00394f9f35) [#44456](https://github.com/sgl-project/sglang/pull/44456)
  [Perf] [AMD] mla: Use aiter bf16 batched GEMM for the absorb BMMs on gfx1250 decode (#44456)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`_
- **2026-10-29** [`8787224bd7`](https://github.com/sgl-project/sglang/commit/8787224bd7) [#47168](https://github.com/sgl-project/sglang/pull/47168)
  [Fix] mem_cache: Default hicache_write_back_staging on MLAView (#47168)
  _Files: `python/sglang/srt/mem_cache/kv/layout/mla.py`_
- **2026-10-29** [`c7e09e5f7c`](https://github.com/sgl-project/sglang/commit/c7e09e5f7c) [#45295](https://github.com/sgl-project/sglang/pull/45295)
  [Perf] hybrid-swa: Detect hybrid SWA models from layer_types (#45295)
  _Files: `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/model_hook.py`, `python/sglang/srt/arg_groups/model_override_base.py`, `python/sglang/srt/arg_groups/model_overrides/exaone.py` _+10 more__
- **2026-10-28** [`c10e0e1773`](https://github.com/sgl-project/sglang/commit/c10e0e1773) [#34031](https://github.com/sgl-project/sglang/pull/34031)
  [Refactor] spec: Make ForwardBatch the single channel for the ragged-verify layout (#34031)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_kda_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py` _+27 more__
- **2026-10-28** [`5cc9c933fc`](https://github.com/sgl-project/sglang/commit/5cc9c933fc) [#47071](https://github.com/sgl-project/sglang/pull/47071)
  [Fix] mem_cache: support prefix commits in unified MHA views (#47071)
  _Files: `python/sglang/srt/mem_cache/kv/layout/mha.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/mem_cache/test_prefix_valid_fp8_pool.py`, `test/registered/unit/mem_cache/test_unified_mha_views.py`_
- **2026-10-28** [`d5bc823ad5`](https://github.com/sgl-project/sglang/commit/d5bc823ad5) [#46990](https://github.com/sgl-project/sglang/pull/46990)
  [Refactor] attention: Use typed KV views and shared layer routing (#46990)
- **2026-10-28** [`240862923e`](https://github.com/sgl-project/sglang/commit/240862923e) [#46986](https://github.com/sgl-project/sglang/pull/46986)
  [Refactor] mem-cache: Bind fused drafts to routed KV views (#46986)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` _+37 more__
- **2026-10-28** [`14fea75124`](https://github.com/sgl-project/sglang/commit/14fea75124) [#46983](https://github.com/sgl-project/sglang/pull/46983)
  [Fix] [AMD] attention: Avoid fused writes to translated window storage (#46983)
  _Files: `python/sglang/srt/models/utils.py`, `test/registered/unit/models/test_fused_set_kv_buffer_gate.py`_
- **2026-10-28** [`5433093d83`](https://github.com/sgl-project/sglang/commit/5433093d83) [#46974](https://github.com/sgl-project/sglang/pull/46974)
  [Refactor] mem_cache: Build unified KV pools from layer declarations (#46974)
  _Files: `python/sglang/srt/mem_cache/allocator/unified_mamba.py`, `python/sglang/srt/mem_cache/kv/build.py`, `python/sglang/srt/mem_cache/kv/decl.py`, `python/sglang/srt/mem_cache/kv/plan.py` _+26 more__
- **2026-10-28** [`335682058a`](https://github.com/sgl-project/sglang/commit/335682058a) [#46973](https://github.com/sgl-project/sglang/pull/46973)
  [Refactor] mem_cache: Separate unified KV layout specifications (#46973)
  _Files: `python/sglang/srt/mem_cache/kv/__init__.py`, `python/sglang/srt/mem_cache/kv/layout/__init__.py`, `python/sglang/srt/mem_cache/kv/layout/base.py`, `python/sglang/srt/mem_cache/kv/layout/mha.py` _+24 more__
- **2026-10-28** [`86f72e5b5c`](https://github.com/sgl-project/sglang/commit/86f72e5b5c) [#46861](https://github.com/sgl-project/sglang/pull/46861)
  [Fix] [AMD] memory_pool: Keep K and V in separate allocations on ROCm (#46861)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/mem_cache/test_mha_pool_fused_kv_layout.py`_
- **2026-10-28** [`edd270fd69`](https://github.com/sgl-project/sglang/commit/edd270fd69) [#44322](https://github.com/sgl-project/sglang/pull/44322)
  [Feat] [AMD] dsa: Enable DCP on the triton sparse-MLA backend (#44322)
  _Files: `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/kernels/ops/attention/dsa/triton_sparse_mla.py`, `python/sglang/kernels/ops/attention/dsa/triton_sparse_mla_decode.py`, `python/sglang/kernels/ops/kvcache/mla_buffer.py` _+19 more__
- **2026-10-28** [`f65af1cd83`](https://github.com/sgl-project/sglang/commit/f65af1cd83) [#39728](https://github.com/sgl-project/sglang/pull/39728)
  [Feat] HiCache: Page unified e2e integration (#39728)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/kernels/ops/kvcache/hicache.py`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/memory.py` _+22 more__
- **2026-10-28** [`aa8e0a9b6a`](https://github.com/sgl-project/sglang/commit/aa8e0a9b6a) [#41696](https://github.com/sgl-project/sglang/pull/41696)
  [Fix] [AMD] dsa: Limit AITER decode metadata to the active batch (#41696)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsa_attention.py`_
- **2026-10-28** [`830103398a`](https://github.com/sgl-project/sglang/commit/830103398a) [#47027](https://github.com/sgl-project/sglang/pull/47027)
  [Doc] cookbook: Drop purged SemiAnalysis AgentX runs and refresh to InferenceX main 253c38bf (#47027)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+4 more__
- **2026-10-28** [`c240169265`](https://github.com/sgl-project/sglang/commit/c240169265) [#46994](https://github.com/sgl-project/sglang/pull/46994)
  [Fix] custom-all-reduce: Keep integer all-reduces off the custom all-reduce kernels (#46994)
  _Files: `python/sglang/kernels/ops/communication/all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `python/sglang/srt/layers/dp_attention.py`_
- **2026-10-28** [`990ee89877`](https://github.com/sgl-project/sglang/commit/990ee89877) [#45503](https://github.com/sgl-project/sglang/pull/45503)
  [Fix] distributed: Prevent unavailable PyNccl enablement (#45503)
  _Files: `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/device_communicators/pynccl.py`, `python/sglang/srt/distributed/device_communicators/pynccl_allocator.py`, `python/sglang/srt/distributed/parallel_state.py` _+5 more__
- **2026-10-28** [`61cf95442a`](https://github.com/sgl-project/sglang/commit/61cf95442a) [#46948](https://github.com/sgl-project/sglang/pull/46948)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main 67de4b34 (#46948)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+4 more__
- **2026-10-28** [`ec3365de18`](https://github.com/sgl-project/sglang/commit/ec3365de18) [#46835](https://github.com/sgl-project/sglang/pull/46835)
  [Perf] dsv4: Skip the copy when the page-index table is already aligned (#46835)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`_
- **2026-10-28** [`0b158f75e7`](https://github.com/sgl-project/sglang/commit/0b158f75e7) [#45470](https://github.com/sgl-project/sglang/pull/45470)
  [Fix] attention: Restore block pointers on Triton 3.9 for FLA kernels (#45470)
  _Files: `python/sglang/kernels/ops/attention/fla/fused_norm_gate.py`, `python/sglang/kernels/ops/attention/fla/utils.py`, `python/sglang/kernels/ops/attention/triton_block_ptr_compat.py`_
- **2026-10-28** [`2eab19ab7f`](https://github.com/sgl-project/sglang/commit/2eab19ab7f) [#46777](https://github.com/sgl-project/sglang/pull/46777)
  [Fix] dsv4: Refuse the draft metadata glue when the backend needs host lengths (#46777)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `test/registered/unit/model_executor/runner/test_dsv41_draft_metadata_glue.py`_
- **2026-10-28** [`357c53885f`](https://github.com/sgl-project/sglang/commit/357c53885f) [#46897](https://github.com/sgl-project/sglang/pull/46897)
  [Fix] dsv4: Let the DSpark draft prep run without host lengths on every device (#46897)
  _Files: `python/sglang/kernels/ops/attention/dsv4/attn_metadata_kernels.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/metadata_glue_graph.py` _+3 more__
- **2026-10-28** [`586355a83b`](https://github.com/sgl-project/sglang/commit/586355a83b) [#46695](https://github.com/sgl-project/sglang/pull/46695)
  [Refactor] attention: Route every FlashAttention call through the selected kernel (#46695)
  _Files: `python/sglang/kernels/ops/attention/flash_attention_v4_sm120.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/unit/layers/attention/test_flashattention_kernel_dispatch.py`_
- **2026-10-27** [`2c83dc6656`](https://github.com/sgl-project/sglang/commit/2c83dc6656) [#45555](https://github.com/sgl-project/sglang/pull/45555)
  [Perf] [AMD] vattn-asm: Split small-batch MTP verify attention over all CUs on gfx950 (#45555)
  _Files: `python/sglang/kernels/ops/attention/vattn_asm_gfx950/__init__.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/amd/test_vattn_segplan_mi35x.py`, `test/registered/unit/layers/attention/test_vattn_asm_segment_plan.py`_
- **2026-10-27** [`a0d4034d5b`](https://github.com/sgl-project/sglang/commit/a0d4034d5b) [#46891](https://github.com/sgl-project/sglang/pull/46891)
  [Fix] dsv4: Build the DSpark draft block metadata without host sequence lengths (#46891)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/speculative/ragged_verify.py`, `test/registered/spec/dspark/test_ragged_verify.py`_
- **2026-10-27** [`90a7339419`](https://github.com/sgl-project/sglang/commit/90a7339419) [#46893](https://github.com/sgl-project/sglang/pull/46893)
  [Feat] dsv41: Choose where Engram tables live with `--engram-config` (#46893)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4_1.mdx`, `docs/docs.json`, `docs/docs/advanced_features/engram.mdx`, `docs/docs/advanced_features/server_arguments.mdx` _+8 more__
- **2026-10-27** [`148bea7302`](https://github.com/sgl-project/sglang/commit/148bea7302) [#45753](https://github.com/sgl-project/sglang/pull/45753)
  [Perf] QSA: Remove the D2D copy in prefill generated kv gather (#45753)
  _Files: `python/sglang/srt/layers/attention/qwen_sparse_attn_backend.py`, `test/registered/kernels/ops/attention/qsa/test_qsa.py`_
- **2026-10-27** [`8f1b7691ca`](https://github.com/sgl-project/sglang/commit/8f1b7691ca) [#45266](https://github.com/sgl-project/sglang/pull/45266)
  [Feat] [NVIDIA] megakernels: Qwen3.5 binding and EAGLE entry wiring for NVIDIA megakernel plugins (#45266)
  _Files: `python/sglang/kernels/plugin_kernels/nvidia/spec.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/kernel_plugins/nvidia/binding.py`, `python/sglang/srt/kernel_plugins/nvidia/eagle_binding.py` _+16 more__
- **2026-10-27** [`bda3718df0`](https://github.com/sgl-project/sglang/commit/bda3718df0) [#46719](https://github.com/sgl-project/sglang/pull/46719)
  [Refactor] bcg: Record graph breaks at capture without running them (#46719)
  _Files: `docs/docs/advanced_features/breakable_cuda_graph.mdx`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/runner.py`, `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/zimage.py` _+12 more__
- **2026-10-27** [`b068417bfc`](https://github.com/sgl-project/sglang/commit/b068417bfc) [#44676](https://github.com/sgl-project/sglang/pull/44676)
  [Feat] dflash: Serve SpecForge MLA drafts through the target MLA attention (#44676)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+12 more__
- **2026-10-27** [`ec54c220f8`](https://github.com/sgl-project/sglang/commit/ec54c220f8) [#46686](https://github.com/sgl-project/sglang/pull/46686)
  [CI] [AMD] diffusion: Skip the CUDA-only Nomas fused-kernel and FlexAttention unit tests on ROCm (#46686)
  _Files: `python/sglang/multimodal_gen/test/unit/test_nomas.py`_
- **2026-10-27** [`359bfc1950`](https://github.com/sgl-project/sglang/commit/359bfc1950) [#46807](https://github.com/sgl-project/sglang/pull/46807)
  [Doc] cookbook: Refresh SemiAnalysis AgentX launches with DeepSeek-V4 B200 DSpark6 disagg and Muse Spark GB300 points (#46807)
  _Files: `docs/src/snippets/agentx/MiniMaxAI/minimax-m3.1.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.5.jsx`, `docs/src/snippets/agentx/Qwen/qwen3.8-flash-next.jsx`, `docs/src/snippets/agentx/deepseek-ai/deepseek-v4.jsx` _+4 more__
- **2026-10-27** [`82b90efc84`](https://github.com/sgl-project/sglang/commit/82b90efc84) [#46736](https://github.com/sgl-project/sglang/pull/46736)
  [Doc] [NPU] docs: update npu docs and fix some issues (#46736)
  _Files: `docs/docs/hardware-platforms/ascend-npus/evaluation/accuracy_evaluation.mdx`, `docs/docs/hardware-platforms/ascend-npus/faq.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/quick_start.mdx` _+30 more__
- **2026-10-27** [`3927a73a34`](https://github.com/sgl-project/sglang/commit/3927a73a34) [#44778](https://github.com/sgl-project/sglang/pull/44778)
  [Fix] kda: Use raw beta in prefill CUDA graphs (#44778)
  _Files: `python/sglang/srt/layers/attention/linear/kda_prefill_graph.py`, `test/registered/kernels/ops/attention/test_kda_prefill_graph.py`_
- **2026-10-27** [`8db96fd402`](https://github.com/sgl-project/sglang/commit/8db96fd402) [#46424](https://github.com/sgl-project/sglang/pull/46424)
  [Fix] dsa: Preserve token-first sparse attention outputs (#46424)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`, `test/registered/unit/layers/attention/test_dsa_backend_dp_padding.py`_
- **2026-10-27** [`449617bc94`](https://github.com/sgl-project/sglang/commit/449617bc94) [#46706](https://github.com/sgl-project/sglang/pull/46706)
  [Fix] dsv4: Render null contents, trailing tool-call turns and numeric string efforts with deepseek-recipe (#46706)
  _Files: `python/sglang/srt/entrypoints/openai/serving_deepseek_recipe.py`, `rust/sglang-processor/src/render/models/deepseek_v4.rs`, `rust/sglang-processor/tests/fixtures/parity/deepseek-v4-flash-0731.json`, `rust/sglang-processor/tests/fixtures/parity/deepseek-v4.1-flash.json` _+1 more__
- **2026-10-27** [`f82f8a94b5`](https://github.com/sgl-project/sglang/commit/f82f8a94b5) [#42760](https://github.com/sgl-project/sglang/pull/42760)
  [Fix] model_loader: Avoid unsafe pickle fallback when loading PyTorch checkpoints (#42760)
  _Files: `python/sglang/multimodal_gen/runtime/loader/weight_utils.py`, `python/sglang/multimodal_gen/runtime/postprocess/rife_interpolator.py`, `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/deepseek_ocr.py` _+2 more__
- **2026-10-27** [`1a120754e0`](https://github.com/sgl-project/sglang/commit/1a120754e0) [#32272](https://github.com/sgl-project/sglang/pull/32272)
  [Perf] fmha_v2: use non-interleaved paged KV input for trtllm sm90/120 GQA prefill (#32272)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/attention/test_trtllm_mha_graph_metadata.py`, `test/registered/attention/unittests/dense/test_trtllm_mha.py` _+1 more__
- **2026-10-27** [`2b36c718cb`](https://github.com/sgl-project/sglang/commit/2b36c718cb) [#46528](https://github.com/sgl-project/sglang/pull/46528)
  [Fix] [AMD] aiter: Fix garbage output with an fp8 KV cache and calibrated KV scales (#46528)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/attention/test_aiter_fp8_kv_scales_paths.py`, `test/registered/attention/test_aiter_fp8_q_unified_attention.py`_
- **2026-10-27** [`58eb1740d2`](https://github.com/sgl-project/sglang/commit/58eb1740d2) [#45796](https://github.com/sgl-project/sglang/pull/45796)
  [Fix] dp-attention: Pad extend host lists out of place so pre-planned DSA metadata keeps its rows (#45796)
  _Files: `python/sglang/srt/model_executor/forward_batch_info.py`, `test/registered/unit/model_executor/test_mlp_sync_pad_unpad.py`_
- **2026-10-27** [`c43abd6d9e`](https://github.com/sgl-project/sglang/commit/c43abd6d9e) [#46659](https://github.com/sgl-project/sglang/pull/46659)
  [Refactor] diffusion: Write DiT attention break outputs into caller-allocated buffers (#46659)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/test/unit/test_attention_bcg_outputs.py`_
- **2026-10-27** [`a912002ee2`](https://github.com/sgl-project/sglang/commit/a912002ee2) [#46660](https://github.com/sgl-project/sglang/pull/46660)
  [Refactor] diffusion: Write MiniMax-H3 and Qwen-Image 2.1 break outputs into caller-allocated buffers (#46660)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3_vdn_attention.py`, `python/sglang/multimodal_gen/runtime/models/dits/qwen_image21.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py`_
- **2026-10-26** [`e732f5d41e`](https://github.com/sgl-project/sglang/commit/e732f5d41e) [#43449](https://github.com/sgl-project/sglang/pull/43449)
  [Feat] spec: Capture aux hidden states on the target without a speculative draft (#43449)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/pipeline.py` _+19 more__
- **2026-10-26** [`d41fbdc647`](https://github.com/sgl-project/sglang/commit/d41fbdc647) [#46668](https://github.com/sgl-project/sglang/pull/46668)
  [Doc] sgl-router: Add GLM-5.3-Flash and DeepSeek-V4.1-Flash deployment examples (#46668)
  _Files: `sgl-router/EXAMPLES.md`, `sgl-router/README.md`_
- **2026-10-26** [`642e9c1448`](https://github.com/sgl-project/sglang/commit/642e9c1448) [#45791](https://github.com/sgl-project/sglang/pull/45791)
  [Perf] QSA: Optimize prefill indexer in long cached prefixes (#45791)
  _Files: `python/sglang/srt/layers/attention/qsa/metadata.py`, `python/sglang/srt/layers/attention/qsa/mqa.py`, `python/sglang/srt/layers/attention/qsa/qsa_indexer.py`, `python/sglang/srt/layers/attention/qsa/sparse_attn.py` _+5 more__
- **2026-10-26** [`4fb422b9fe`](https://github.com/sgl-project/sglang/commit/4fb422b9fe) [#45659](https://github.com/sgl-project/sglang/pull/45659)
  [Fix] rust-server: Match Python's chat layer on templates, streaming and lowered-chat errors (#45659)
  _Files: `rust/sglang-processor/src/lib.rs`, `rust/sglang-processor/src/openai/chat.rs`, `rust/sglang-processor/src/openai/completions.rs`, `rust/sglang-processor/src/openai/mod.rs` _+29 more__
- **2026-10-26** [`2c250563ae`](https://github.com/sgl-project/sglang/commit/2c250563ae) [#46535](https://github.com/sgl-project/sglang/pull/46535)
  [Refactor] attention: Write the eager break's LSE into a caller-allocated buffer (#46535)
  _Files: `python/sglang/srt/layers/radix_attention.py`, `test/registered/unit/layers/test_radix_attention.py`_
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

## Multimodal  (103 commits)

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
- **2026-11-01** [`38d9e4a3fe`](https://github.com/sgl-project/sglang/commit/38d9e4a3fe) [#46274](https://github.com/sgl-project/sglang/pull/46274)
  [Fix] diffusion: Keep each request's rollout trajectory and conditioning under dynamic batching (#46274)
  _Files: `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/runtime/post_training/rl_dataclasses.py`, `python/sglang/multimodal_gen/test/unit/test_image_response_bytes.py`, `python/sglang/multimodal_gen/test/unit/test_multi_output_rollout_trajectory.py`_
- **2026-11-01** [`e8bf40b8ee`](https://github.com/sgl-project/sglang/commit/e8bf40b8ee) [#47605](https://github.com/sgl-project/sglang/pull/47605)
  [Feat] diffusion: LRU eviction for LoRA merge cache (#47605)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/lora/lora_merge_cache.py`, `python/sglang/multimodal_gen/test/unit/test_lora_merge_cache.py`_
- **2026-11-01** [`c3654cd93b`](https://github.com/sgl-project/sglang/commit/c3654cd93b) [#46883](https://github.com/sgl-project/sglang/pull/46883)
  [Chore] [AMD] docker: Build uTLX into the gfx950 rocm10 images (#46883)
  _Files: `docker/rocm.Dockerfile`_
- **2026-11-01** [`9431d2caf6`](https://github.com/sgl-project/sglang/commit/9431d2caf6) [#46255](https://github.com/sgl-project/sglang/pull/46255)
  [Fix] diffusion: LoRA alpha reload, auto-mode skip, critic coverage (#46255)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py`, `python/sglang/multimodal_gen/test/unit/test_fused_lora_compose.py`, `python/sglang/multimodal_gen/test/unit/test_lora_pipeline.py`_
- **2026-11-01** [`a52ee805c8`](https://github.com/sgl-project/sglang/commit/a52ee805c8) [#46328](https://github.com/sgl-project/sglang/pull/46328)
  [Perf] diffusion: opt-in Wan UMT5 padding trim (SGLANG_DIFFUSION_WAN_TEXT_PADDING) (#46328)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/test/unit/test_wan_pipeline_config.py`_
- **2026-11-01** [`e298298511`](https://github.com/sgl-project/sglang/commit/e298298511) [#47474](https://github.com/sgl-project/sglang/pull/47474)
  [Fix] diffusion/bcg: Warm up LTX-2 two-stage at the output resolution (#47474)
  _Files: `python/sglang/multimodal_gen/runtime/warmup_request_builder.py`, `python/sglang/multimodal_gen/test/unit/test_cfg_parallel_warmup.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-11-01** [`4ffc9e1b7d`](https://github.com/sgl-project/sglang/commit/4ffc9e1b7d) [#47488](https://github.com/sgl-project/sglang/pull/47488)
  [Fix] diffusion: Fail fast on offline runtime failures (#47488)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/diffusion_generator.py`, `python/sglang/multimodal_gen/runtime/scheduler_client.py`, `python/sglang/multimodal_gen/runtime/utils/device_errors.py`, `python/sglang/multimodal_gen/test/unit/test_cfg_parallel_warmup.py` _+3 more__
- **2026-11-01** [`bebee560cc`](https://github.com/sgl-project/sglang/commit/bebee560cc) [#45065](https://github.com/sgl-project/sglang/pull/45065)
  [Fix] diffusion: Exit the worker after an unrecoverable device error (#45065)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/test/unit/test_unrecoverable_device_error.py`_
- **2026-11-01** [`07efafb546`](https://github.com/sgl-project/sglang/commit/07efafb546) [#44574](https://github.com/sgl-project/sglang/pull/44574)
  [Fix] multimodal: Keep shared-memory feature transport for multi-node pipeline parallelism (#44574)
  _Files: `python/sglang/srt/multimodal/transport/__init__.py`, `test/registered/unit/multimodal/test_tensor_transport_mode.py`_
- **2026-11-01** [`c108a656f1`](https://github.com/sgl-project/sglang/commit/c108a656f1) [#46871](https://github.com/sgl-project/sglang/pull/46871)
  [Fix] diffusion: keep tied vocab tables on device under layerwise offload (#46871)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/test/unit/test_host_resident_vocab_table.py`_
- **2026-11-01** [`e3ec98b15e`](https://github.com/sgl-project/sglang/commit/e3ec98b15e) [#46860](https://github.com/sgl-project/sglang/pull/46860)
  [Refactor] diffusion: normalize diffusers output layout in one place (#46860)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines/diffusers_pipeline.py`, `python/sglang/multimodal_gen/test/unit/test_pipeline_regressions.py`_
- **2026-11-01** [`cda284e47b`](https://github.com/sgl-project/sglang/commit/cda284e47b) [#47691](https://github.com/sgl-project/sglang/pull/47691)
  [Fix] rust-server: Validate gathered listener ranks and address families (#47691)
  _Files: `python/sglang/srt/rust_server/server.py`, `test/registered/unit/multimodal/rust/shared/test_rust_server_extension.py`_
- **2026-10-31** [`bd1f5596f1`](https://github.com/sgl-project/sglang/commit/bd1f5596f1) [#47551](https://github.com/sgl-project/sglang/pull/47551)
  [CI] tests: Rendezvous the tile-sharding gloo test through a file store (#47551)
  _Files: `python/sglang/multimodal_gen/test/unit/test_diffusion_decoder_tile_sharding.py`_
- **2026-10-31** [`25c3fd8308`](https://github.com/sgl-project/sglang/commit/25c3fd8308) [#47583](https://github.com/sgl-project/sglang/pull/47583)
  [Fix] diffusion: MiniMax-H3 warms up at the short edge --warmup-resolutions names (#47583)
  _Files: `python/sglang/multimodal_gen/configs/sample/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_admission.py`_
- **2026-10-31** [`dc79ae47ca`](https://github.com/sgl-project/sglang/commit/dc79ae47ca) [#47582](https://github.com/sgl-project/sglang/pull/47582)
  [Fix] diffusion: LTX-2.5 two-stage defaults to its 1920x1088 canvas (#47582)
  _Files: `python/sglang/multimodal_gen/configs/sample/ltx_2_5.py`, `python/sglang/multimodal_gen/runtime/warmup_request_builder.py`, `python/sglang/multimodal_gen/test/unit/test_cfg_parallel_warmup.py`_
- **2026-10-31** [`0f92ddaefb`](https://github.com/sgl-project/sglang/commit/0f92ddaefb) [#47568](https://github.com/sgl-project/sglang/pull/47568)
  [Perf] [ROCM] diffusion: Encode the MP4 while the VAE decodes on ROCm too (#47568)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/encode_while_decoding.py`, `python/sglang/multimodal_gen/test/unit/test_ltx_vae_on_frames.py`, `python/sglang/multimodal_gen/test/unit/test_wan_streamed_encode.py`_
- **2026-10-31** [`7585ccc2c0`](https://github.com/sgl-project/sglang/commit/7585ccc2c0) [#47569](https://github.com/sgl-project/sglang/pull/47569)
  [Perf] [ROCM] diffusion: Bit-exact fast QK RMSNorm and fused RoPE for MiniMax-H3 (#47569)
  _Files: `python/sglang/kernels/ops/diffusion/README.md`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/norm/aten_head_rmsnorm_triton.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` _+1 more__
- **2026-10-31** [`37fc17b8d6`](https://github.com/sgl-project/sglang/commit/37fc17b8d6) [#47378](https://github.com/sgl-project/sglang/pull/47378)
  [Feat] diffusion/model: Support Pika-Labs/Pika-H3-Flex (MiniMax-H3 + 6-step LoRA) (#47378)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/src/snippets/diffusion/model-catalog.jsx`, `python/sglang/multimodal_gen/configs/pipeline_configs/minimax_h3.py`, `python/sglang/multimodal_gen/configs/sample/minimax_h3.py` _+8 more__
- **2026-10-31** [`5c46d20db9`](https://github.com/sgl-project/sglang/commit/5c46d20db9) [#47571](https://github.com/sgl-project/sglang/pull/47571)
  [Fix] diffusion: Server warmup reaches every data-parallel replica (#47571)
  _Files: `python/sglang/multimodal_gen/runtime/scheduler_client.py`, `python/sglang/multimodal_gen/runtime/server_warmup.py`, `python/sglang/multimodal_gen/test/unit/test_cfg_parallel_warmup.py`, `python/sglang/multimodal_gen/test/unit/test_scheduler_client.py`_
- **2026-10-31** [`03a27e2a17`](https://github.com/sgl-project/sglang/commit/03a27e2a17) [#46028](https://github.com/sgl-project/sglang/pull/46028)
  [Perf] cosmos3: Accelerate conditioning hashing with GPU BLAKE3 (#46028)
  _Files: `.github/actions/wait-for-jobs/action.yml`, `python/sglang/kernels/ops/memory/__init__.py`, `python/sglang/kernels/ops/memory/gpu_tensor_hash_blake3.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py` _+2 more__
- **2026-10-31** [`419d31a7b2`](https://github.com/sgl-project/sglang/commit/419d31a7b2) [#47625](https://github.com/sgl-project/sglang/pull/47625)
  [CI] diffusion: Fix image preprocessing test dependency environment (#47625)
  _Files: `test/registered/unit/multimodal_gen/test_image_preprocessing.py`_
- **2026-10-31** [`a4a6eddd25`](https://github.com/sgl-project/sglang/commit/a4a6eddd25) [#47516](https://github.com/sgl-project/sglang/pull/47516)
  [Fix] diffusion: Nomas KV budget counts freed cached memory, reject SP-indivisible segments up front (#47516)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/nomas/stages.py`, `python/sglang/multimodal_gen/test/unit/test_nomas.py`_
- **2026-10-31** [`028811fc61`](https://github.com/sgl-project/sglang/commit/028811fc61) [#47549](https://github.com/sgl-project/sglang/pull/47549)
  [CI] chore: add CI permissions and diffusion CODEOWNERS for JackZeng0208 (#47549)
  _Files: `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS`_
- **2026-10-31** [`7bc92100ad`](https://github.com/sgl-project/sglang/commit/7bc92100ad) [#47240](https://github.com/sgl-project/sglang/pull/47240)
  [Fix] diffusion: Check cancellation at stage and sampling boundaries (#47240)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `docs/docs/sglang-diffusion/support_new_models.mdx`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/progress_reporter.py` _+21 more__
- **2026-10-31** [`96a76f5d5f`](https://github.com/sgl-project/sglang/commit/96a76f5d5f) [#47465](https://github.com/sgl-project/sglang/pull/47465)
  [Perf] diffusion: Hold a Qwen-Image-2.1 Q/K norm + RoPE row with a half-warp (#47465)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_complex_rope.cuh`, `test/registered/kernels/ops/diffusion/test_complex_rope.py`_
- **2026-10-31** [`ab86251288`](https://github.com/sgl-project/sglang/commit/ab86251288) [#47467](https://github.com/sgl-project/sglang/pull/47467)
  [Perf] diffusion: Replay Qwen-Image-2.1's text-only encoder from CUDA graphs (#47467)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/qwen_image21.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/text_encoding.py`, `python/sglang/multimodal_gen/runtime/utils/common.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py` _+1 more__
- **2026-10-31** [`bf1ece1f7e`](https://github.com/sgl-project/sglang/commit/bf1ece1f7e) [#47556](https://github.com/sgl-project/sglang/pull/47556)
  [Test] rust-server: Drop request-fake members the output streamer no longer reads (#47556)
  _Files: `test/registered/unit/multimodal/rust/shared/test_rust_server_extension.py`_
- **2026-10-30** [`b5a0c9dc18`](https://github.com/sgl-project/sglang/commit/b5a0c9dc18) [#45834](https://github.com/sgl-project/sglang/pull/45834)
  [Fix] diffusion: LoRA merge cache key identity and eviction (#45834)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/lora/lora_merge_cache.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py`, `python/sglang/multimodal_gen/test/unit/test_comfyui_lora_node.py`, `python/sglang/multimodal_gen/test/unit/test_fused_lora_compose.py` _+3 more__
- **2026-10-30** [`e83c9d57bc`](https://github.com/sgl-project/sglang/commit/e83c9d57bc) [#43866](https://github.com/sgl-project/sglang/pull/43866)
  [Fix] multimodal: Return 400 for images Pillow refuses as decompression bombs (#43866)
  _Files: `python/sglang/srt/utils/common.py`, `test/registered/unit/multimodal/test_base_processor_bad_input.py`_
- **2026-10-30** [`93aefdf0c5`](https://github.com/sgl-project/sglang/commit/93aefdf0c5) [#47539](https://github.com/sgl-project/sglang/pull/47539)
  [Doc] cookbook: Use latest image for Muse Spark Open deployment (#47539)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`, `docs/src/snippets/configs/meta-models/muse-spark.jsx`_
- **2026-10-30** [`c096c8fda7`](https://github.com/sgl-project/sglang/commit/c096c8fda7) [#47537](https://github.com/sgl-project/sglang/pull/47537)
  [Fix] rust-server: Give the mixed-logprob frame test's payload flat output ids with row offsets (#47537)
  _Files: `test/registered/unit/multimodal/rust/shared/test_rust_server_extension.py`_
- **2026-10-30** [`734aa5503e`](https://github.com/sgl-project/sglang/commit/734aa5503e) [#47445](https://github.com/sgl-project/sglang/pull/47445)
  [Fix] ipc: Make multimodal payloads, hidden states and weight-update dtypes round-trip under msgpack IPC (#47445)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/embed_types.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/positional_embeds_transport.py` _+6 more__
- **2026-10-30** [`76820e89a9`](https://github.com/sgl-project/sglang/commit/76820e89a9) [#46963](https://github.com/sgl-project/sglang/pull/46963)
  [Feat] rust-server: Report the scheduler's per-request stats in native /generate meta_info (#46963)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/rust_server/server.py`, `python/sglang/srt/speculative/spec_decoding_metrics.py` _+6 more__
- **2026-10-30** [`60a347b6f3`](https://github.com/sgl-project/sglang/commit/60a347b6f3) [#47106](https://github.com/sgl-project/sglang/pull/47106)
  [Perf] rust-server: Flatten egress logprob columns only for rows that carry them (#47106)
  _Files: `python/sglang/srt/rust_server/server.py`, `python/sglang/srt/utils/flatten.py`, `test/registered/unit/multimodal/rust/shared/test_rust_server_extension.py`_
- **2026-10-30** [`60725d0e17`](https://github.com/sgl-project/sglang/commit/60725d0e17) [#46277](https://github.com/sgl-project/sglang/pull/46277)
  [Perf] diffusion: Wan-Animate-2 decode clamp, LTX-2 Bongmath closed form, rollout log-prob/CPU-copy, validators NaN gate, in-place decode normalize (#46277)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/decoding.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/wan_animate_2/denoising.py` _+8 more__
- **2026-10-30** [`dee613b283`](https://github.com/sgl-project/sglang/commit/dee613b283) [#47466](https://github.com/sgl-project/sglang/pull/47466)
  [Perf] diffusion: Skip the cross-request cache for Qwen3-VL vision features (#47466)
  _Files: `python/sglang/multimodal_gen/runtime/models/encoders/qwen3vl.py`_
- **2026-10-30** [`e3e372931a`](https://github.com/sgl-project/sglang/commit/e3e372931a) [#47411](https://github.com/sgl-project/sglang/pull/47411)
  [Feat] diffusion: Native Gemma-4-Unified text encoder for LTX-2.5 (#47411)
  _Files: `python/sglang/multimodal_gen/configs/models/encoders/gemma_4_unified.py`, `python/sglang/multimodal_gen/runtime/models/encoders/gemma_4_unified.py`, `python/sglang/multimodal_gen/test/unit/test_gemma4_unified_layerwise_offload.py`_
- **2026-10-30** [`24268cc92b`](https://github.com/sgl-project/sglang/commit/24268cc92b) [#47270](https://github.com/sgl-project/sglang/pull/47270)
  [Fix] diffusion: recover LTX eager performance without disabling fusion (#47270)
  _Files: `docs/cookbook/diffusion/LTX/LTX2 & LTX2.3.mdx`, `python/sglang/kernels/ops/diffusion/modulate/head_gate_triton.py`, `python/sglang/kernels/ops/diffusion/norm/rmsnorm_scale_shift_bitexact.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py` _+5 more__
- **2026-10-30** [`8776a94f29`](https://github.com/sgl-project/sglang/commit/8776a94f29) [#46907](https://github.com/sgl-project/sglang/pull/46907)
  [Fix] minimax-h3: Swap the fc1 halves of the Acc LoRA in build_minimax_h3_pdd_weights (#46907)
  _Files: `python/sglang/multimodal_gen/test/unit/test_minimax_h3_pdd_offline.py`, `python/sglang/multimodal_gen/tools/build_minimax_h3_pdd_weights.py`_
- **2026-10-30** [`c805455101`](https://github.com/sgl-project/sglang/commit/c805455101) [#44725](https://github.com/sgl-project/sglang/pull/44725)
  [Fix] minimax_h3: Support out-of-tree platforms (#44725)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_denoise_loop.py`_
- **2026-10-30** [`15ef675846`](https://github.com/sgl-project/sglang/commit/15ef675846) [#47415](https://github.com/sgl-project/sglang/pull/47415)
  [Perf] detokenizer: Send each step's output ids as one flat column with row offsets (#47415)
  _Files: `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py` _+11 more__
- **2026-10-30** [`975232c64d`](https://github.com/sgl-project/sglang/commit/975232c64d) [#47394](https://github.com/sgl-project/sglang/pull/47394)
  [Doc] [AMD] cookbook: Update Muse Spark Open MI355X AgentX recipe to the 1027 image (#47394)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`_
- **2026-10-30** [`93a936d007`](https://github.com/sgl-project/sglang/commit/93a936d007) [#46961](https://github.com/sgl-project/sglang/pull/46961)
  [Feat] rust-server: Report cached tokens by cache tier in native /generate meta_info (#46961)
  _Files: `proto/sglang/api/v1/generate.proto`, `python/sglang/api/v1/api_types.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `python/sglang/srt/rust_server/server.py` _+15 more__
- **2026-10-30** [`3b6c28b0b9`](https://github.com/sgl-project/sglang/commit/3b6c28b0b9) [#47118](https://github.com/sgl-project/sglang/pull/47118)
  [CI] [AMD] diffusion/ming: Skip the CUDA-only fused RMSNorm test on ROCm (#47118)
  _Files: `python/sglang/multimodal_gen/test/unit/test_ming_image.py`_
- **2026-10-30** [`b2367b13a2`](https://github.com/sgl-project/sglang/commit/b2367b13a2) [#46601](https://github.com/sgl-project/sglang/pull/46601)
  [Fix] diffusion: LingBot QKV sharing, causal RoPE on no-cache path, uneven split guard (#46601)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/lingbot_world.py`, `python/sglang/multimodal_gen/test/unit/realtime/test_lingbot_causal_denoising.py`_
- **2026-10-29** [`5ed1433376`](https://github.com/sgl-project/sglang/commit/5ed1433376) [#47161](https://github.com/sgl-project/sglang/pull/47161)
  [Perf] rust-server: Pin frontend threads to one shared CPU set, not one core each (#47161)
  _Files: `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/rust_server/server.py`, `rust/Cargo.lock`, `rust/sglang-mm/src/common/par.rs` _+5 more__
- **2026-10-29** [`8773d60f25`](https://github.com/sgl-project/sglang/commit/8773d60f25) [#47108](https://github.com/sgl-project/sglang/pull/47108)
  [Fix] rust-server: Admit a multimodal model's generations only once its MM processor is installed (#47108)
  _Files: `python/sglang/srt/rust_server/server.py`, `rust/sglang-server/src/api_server/grpc/service.rs`, `rust/sglang-server/src/api_server/handlers/control.rs`, `rust/sglang-server/src/api_server/handlers/generate.rs` _+14 more__
- **2026-10-29** [`1ab008f5b0`](https://github.com/sgl-project/sglang/commit/1ab008f5b0) [#47022](https://github.com/sgl-project/sglang/pull/47022)
  [Perf] joy-image: Fuse image MLP GELU on SM120 in high quality (#47022)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/joy_image.py`, `test/registered/kernels/ops/diffusion/test_model_fast_paths.py`_
- **2026-10-29** [`970cbb5fa6`](https://github.com/sgl-project/sglang/commit/970cbb5fa6) [#47162](https://github.com/sgl-project/sglang/pull/47162)
  [CI] [AMD] ci: Spread out tests and prefer today's images (#47162)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm10-mi30x.yml`, `.github/workflows/nightly-test-amd-miles-rocm10.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd.yml` _+4 more__
- **2026-10-29** [`7df65d970d`](https://github.com/sgl-project/sglang/commit/7df65d970d) [#46722](https://github.com/sgl-project/sglang/pull/46722)
  [Perf] [AMD] diffusion: Optimize the Wan VAE decode for gfx1250 (#46722)
  _Files: `python/sglang/multimodal_gen/configs/models/vaes/wanvae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wan_vae_cuda_opt.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py`, `python/sglang/multimodal_gen/runtime/platforms/rocm.py` _+2 more__
- **2026-10-29** [`9e9296fdf3`](https://github.com/sgl-project/sglang/commit/9e9296fdf3) [#47176](https://github.com/sgl-project/sglang/pull/47176)
  [Doc] diffusion: Index HY-Nomas and FastH3 Omni (#47176)
  _Files: `docs/docs/sglang-diffusion/realtime_models.mdx`, `docs/src/snippets/diffusion/model-catalog.jsx`_
- **2026-10-29** [`8b0f2f929f`](https://github.com/sgl-project/sglang/commit/8b0f2f929f) [#47055](https://github.com/sgl-project/sglang/pull/47055)
  [Feat] diffusion/openai: Cancel video jobs on DELETE (#47055)
  _Files: `docs/docs/sglang-diffusion/api/openai_api.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/utils.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/video_api.py` _+14 more__
- **2026-10-29** [`9df3d27eed`](https://github.com/sgl-project/sglang/commit/9df3d27eed) [#46723](https://github.com/sgl-project/sglang/pull/46723)
  [Perf] [AMD] diffusion: Replace the gfx1250 bf16 scale-shift torch fallback with a bit-exact Triton kernel (#46723)
  _Files: `python/sglang/kernels/ops/diffusion/modulate/scale_shift_triton.py`, `test/registered/kernels/ops/diffusion/test_modulate.py`_
- **2026-10-29** [`2a6c204570`](https://github.com/sgl-project/sglang/commit/2a6c204570) [#47194](https://github.com/sgl-project/sglang/pull/47194)
  [CI] [AMD] miles: drop the ROCm 7.2.4 MI35X nightly image build (#47194)
  _Files: `.github/workflows/release-docker-amd-miles-rocm724-nightly.yml`_
- **2026-10-29** [`71fb709387`](https://github.com/sgl-project/sglang/commit/71fb709387) [#45837](https://github.com/sgl-project/sglang/pull/45837)
  [Fix] diffusion: LoRA adapter-state and merge-transition fixes (#45837)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py`, `python/sglang/multimodal_gen/test/unit/test_component_residency.py`, `python/sglang/multimodal_gen/test/unit/test_fused_lora_compose.py`, `python/sglang/multimodal_gen/test/unit/test_lora_pipeline.py` _+1 more__
- **2026-10-29** [`ce80493fe3`](https://github.com/sgl-project/sglang/commit/ce80493fe3) [#45996](https://github.com/sgl-project/sglang/pull/45996)
  [Fix] rust_server: Give each plain-DP replica its own listener port (#45996)
  _Files: `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/rust_server/server.py`, `test/registered/unit/entrypoints/test_rust_server_dp_ports.py`, `test/registered/unit/multimodal/rust/shared/test_rust_server_extension.py` _+1 more__
- **2026-10-29** [`363d957137`](https://github.com/sgl-project/sglang/commit/363d957137) [#46882](https://github.com/sgl-project/sglang/pull/46882)
  [Feat] grpc: Advertise media inputs in GetServerInfo (#46882)
  _Files: `python/sglang/srt/entrypoints/grpc_bridge.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `test/registered/unit/entrypoints/test_grpc_bridge.py`, `test/registered/unit/entrypoints/test_server_info.py`_
- **2026-10-29** [`0fdc4e82ca`](https://github.com/sgl-project/sglang/commit/0fdc4e82ca) [#46949](https://github.com/sgl-project/sglang/pull/46949)
  [Feat] rust-server: Carry customized_info through the native /generate frontend (#46949)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `python/sglang/srt/rust_server/server.py`, `python/sglang/test/rust_customized_info.py`, `rust/sglang-server/src/api_server/core/frame.rs` _+6 more__
- **2026-10-28** [`eead03fefd`](https://github.com/sgl-project/sglang/commit/eead03fefd) [#47109](https://github.com/sgl-project/sglang/pull/47109)
  [Fix] rust-server: Answer media the multimodal processor refuses with a 400 (#47109)
  _Files: `rust/sglang-server/src/api_server/core/error.rs`, `rust/sglang-server/src/api_server/core/prefetch.rs`, `rust/sglang-server/src/api_server/handlers/generate.rs`, `rust/sglang-server/src/api_server/handlers/handle.rs` _+5 more__
- **2026-10-28** [`5ac32ada54`](https://github.com/sgl-project/sglang/commit/5ac32ada54) [#46889](https://github.com/sgl-project/sglang/pull/46889)
  [Test] [AMD] diffusion: Compute the VAE blend test's fp16 reference in fp32 on ROCm (#46889)
  _Files: `python/sglang/multimodal_gen/test/unit/test_vae_tiled_decode_groups.py`_
- **2026-10-28** [`4517a5ff1b`](https://github.com/sgl-project/sglang/commit/4517a5ff1b) [#46286](https://github.com/sgl-project/sglang/pull/46286)
  [Fix] comfyui: Reject conditioning kwargs the SGLD adapters silently drop (#46286)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/qwen_image.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/zimage.py`, `python/sglang/multimodal_gen/test/unit/test_comfyui_adapters.py`_
- **2026-10-28** [`b1c6945659`](https://github.com/sgl-project/sglang/commit/b1c6945659) [#43697](https://github.com/sgl-project/sglang/pull/43697)
  [Feat] comfyui: Add SGLDWorkerStatus diagnostics node (#43697)
  _Files: `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/README.md`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/core/generator.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/executors/base.py`, `python/sglang/multimodal_gen/apps/ComfyUI_SGLDiffusion/nodes.py` _+3 more__
- **2026-10-28** [`9e36e5fc27`](https://github.com/sgl-project/sglang/commit/9e36e5fc27) [#46946](https://github.com/sgl-project/sglang/pull/46946)
  [Feat] rust-server: Let a multimodal processor observe the final result before scheduling (#46946)
  _Files: `rust/sglang-server/src/lib.rs`, `rust/sglang-server/src/multi_modality/worker.rs`, `rust/sglang-server/src/tokenizer_manager/to_scheduler.rs`, `rust/sglang-server/src/tokenizer_manager/to_scheduler_validation.rs` _+1 more__
- **2026-10-28** [`69233a4622`](https://github.com/sgl-project/sglang/commit/69233a4622) [#46181](https://github.com/sgl-project/sglang/pull/46181)
  [Feat] rust-server: Fan control requests out to every DP rank (#46181)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/rust_server/server.py`, `rust/Cargo.lock` _+37 more__
- **2026-10-28** [`e0df901d68`](https://github.com/sgl-project/sglang/commit/e0df901d68) [#46916](https://github.com/sgl-project/sglang/pull/46916)
  [Fix] diffusion/ci: Keep final failure reasons at the end of shard logs (#46916)
  _Files: `python/sglang/multimodal_gen/test/runner/diffusion_suite_runner.py`, `python/sglang/multimodal_gen/test/runner/pytest_runner.py`, `python/sglang/multimodal_gen/test/unit/test_suite_partitioning.py`_
- **2026-10-28** [`8fabf5e65c`](https://github.com/sgl-project/sglang/commit/8fabf5e65c) [#46728](https://github.com/sgl-project/sglang/pull/46728)
  [CI] npu: Remove internal cache-service references from NPU workflows (#46728)
  _Files: `.github/workflows/_npu-pr-test-stage.yml`, `.github/workflows/_npu-single-node-test-stage.yml`, `.github/workflows/diffusion-ci-gt-gen-npu.yml`, `.github/workflows/pr-test-npu.yml`_
- **2026-10-28** [`4b43572e52`](https://github.com/sgl-project/sglang/commit/4b43572e52) [#46705](https://github.com/sgl-project/sglang/pull/46705)
  [Perf] diffusion/ming: Reuse ordered RMSNorm in the DiT (#46705)
  _Files: `python/sglang/kernels/ops/diffusion/norm/rmsnorm_cast_before_weight_bitexact.py`, `python/sglang/multimodal_gen/runtime/models/dits/ming_image.py`, `python/sglang/multimodal_gen/test/unit/test_ming_image.py`, `test/registered/kernels/ops/diffusion/test_norm.py`_
- **2026-10-28** [`5bb7ecc2c2`](https://github.com/sgl-project/sglang/commit/5bb7ecc2c2) [#46664](https://github.com/sgl-project/sglang/pull/46664)
  [Fix] diffusion/moss: Preserve full latents for sequence parallelism (#46664)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/moss_image.py`, `python/sglang/multimodal_gen/test/unit/test_moss_image_parallel.py`_
- **2026-10-28** [`610a74d648`](https://github.com/sgl-project/sglang/commit/610a74d648) [#46641](https://github.com/sgl-project/sglang/pull/46641)
  [Perf] MOSS-Image: Fuse joint-block QKV projections in high quality (#46641)
  _Files: `docs/cookbook/diffusion/OpenMOSS/MOSS-Image.mdx`, `python/sglang/kernels/ops/diffusion/norm/rmsnorm_cast_before_weight_bitexact.py`, `python/sglang/multimodal_gen/runtime/models/dits/moss_image.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/moss_image.py` _+2 more__
- **2026-10-27** [`e0641da8f8`](https://github.com/sgl-project/sglang/commit/e0641da8f8) [#46895](https://github.com/sgl-project/sglang/pull/46895)
  Revert "[Doc] beam: Use lmsysorg/sglang:dev image in the cookbook" (#46895)
  _Files: `docs/cookbook/autoregressive/Reflection/Beam-1_0.mdx`, `docs/src/snippets/configs/reflection/beam-1.0.jsx`_
- **2026-10-27** [`ab5602731f`](https://github.com/sgl-project/sglang/commit/ab5602731f) [#46886](https://github.com/sgl-project/sglang/pull/46886)
  [Doc] beam: Use lmsysorg/sglang:dev image in the cookbook (#46886)
  _Files: `docs/cookbook/autoregressive/Reflection/Beam-1_0.mdx`, `docs/src/snippets/configs/reflection/beam-1.0.jsx`_
- **2026-10-27** [`69767e5aa6`](https://github.com/sgl-project/sglang/commit/69767e5aa6) [#45638](https://github.com/sgl-project/sglang/pull/45638)
  [Fix] diffusion: float32 Plucker rays for bf16 camera poses (#45638)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/lingbot_world.py`, `python/sglang/multimodal_gen/runtime/utils/camera_geometry.py`, `python/sglang/multimodal_gen/test/unit/test_camera_geometry.py`_
- **2026-10-27** [`dc41126cde`](https://github.com/sgl-project/sglang/commit/dc41126cde) [#45833](https://github.com/sgl-project/sglang/pull/45833)
  [Fix] diffusion: LoRA format alpha and rank scaling (#45833)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/lora/format_adapter.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/peft_adapter.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora/pipeline.py`, `python/sglang/multimodal_gen/test/unit/test_fused_lora_compose.py` _+2 more__
- **2026-10-27** [`b48aba306b`](https://github.com/sgl-project/sglang/commit/b48aba306b) [#46629](https://github.com/sgl-project/sglang/pull/46629)
  [Test] rust-server: Drop two unit tests that mirror one-line delegations (#46629)
  _Files: `test/registered/unit/managers/test_scheduler_flush_cache.py`, `test/registered/unit/multimodal/rust/shared/test_rust_server_extension.py`_
- **2026-10-27** [`8a455f1b90`](https://github.com/sgl-project/sglang/commit/8a455f1b90) [#44888](https://github.com/sgl-project/sglang/pull/44888)
  [Fix] diffusion: pipeline and model-helper bug fixes (#44888)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines/diffusers_pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines/ernie_image.py`, `python/sglang/multimodal_gen/runtime/pipelines/hunyuan3d_pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines/hunyuan_image3.py` _+3 more__
- **2026-10-27** [`618136d4d3`](https://github.com/sgl-project/sglang/commit/618136d4d3) [#46785](https://github.com/sgl-project/sglang/pull/46785)
  [CI] [AMD] docker: Build MORI into the ROCm 10.1 gfx1250 image and fix its CI setup (#46785)
  _Files: `.github/workflows/release-docker-amd-rocm10.yml`, `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-10-27** [`cf04168be1`](https://github.com/sgl-project/sglang/commit/cf04168be1) [#46366](https://github.com/sgl-project/sglang/pull/46366)
  [Perf] [AMD] diffusion: Route large BF16 linears to the FlyDSL a16w16 GEMM on gfx1250 (#46366)
  _Files: `python/sglang/multimodal_gen/runtime/layers/linear.py`, `python/sglang/multimodal_gen/test/unit/test_gfx1250_flydsl_linear.py`_
- **2026-10-27** [`e4d4a9a7de`](https://github.com/sgl-project/sglang/commit/e4d4a9a7de) [#46536](https://github.com/sgl-project/sglang/pull/46536)
  [Fix] diffusion: Guard CUDA-only RoPE paths (#46536)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`_
- **2026-10-27** [`6393e66b86`](https://github.com/sgl-project/sglang/commit/6393e66b86) [#43420](https://github.com/sgl-project/sglang/pull/43420)
  [Refactor] multimodal: [MM refactor 1/9] Move multimodal enums to a shared module (#43420)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/multimodal/modality.py`, `python/sglang/srt/utils/common.py`, `test/registered/unit/utils/test_safe_unpickler.py`_
- **2026-10-27** [`3dce594de3`](https://github.com/sgl-project/sglang/commit/3dce594de3) [#46155](https://github.com/sgl-project/sglang/pull/46155)
  [Fix] diffusion/cli: Preserve explicit argv and registered aliases (#46155)
  _Files: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-10-27** [`9694a99d55`](https://github.com/sgl-project/sglang/commit/9694a99d55) [#46252](https://github.com/sgl-project/sglang/pull/46252)
  [Fix] diffusion/realtime: Reserve generation slots after initialization (#46252)
  _Files: `docs/docs/sglang-diffusion/realtime_models.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/realtime_video_api.py`, `python/sglang/multimodal_gen/test/unit/realtime/test_realtime_runtime.py`_
- **2026-10-27** [`6724403444`](https://github.com/sgl-project/sglang/commit/6724403444) [#46638](https://github.com/sgl-project/sglang/pull/46638)
  [Fix] multimodal: Clip pad spans to a truncated prompt (#46638)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `test/registered/unit/managers/test_mm_pad_input_tokens.py`_
- **2026-10-27** [`5884e4fec6`](https://github.com/sgl-project/sglang/commit/5884e4fec6) [#46679](https://github.com/sgl-project/sglang/pull/46679)
  [Fix] diffusion: Resolve cached named weights without the Hub API (#46679)
  _Files: `python/sglang/multimodal_gen/runtime/weights/source.py`_
- **2026-10-26** [`7ec4c0d790`](https://github.com/sgl-project/sglang/commit/7ec4c0d790) [#46449](https://github.com/sgl-project/sglang/pull/46449)
  [CI] [AMD] diffusion: Skip the CUDA-only gpu-idle and Z-Image RoPE cache unit tests on ROCm (#46449)
  _Files: `python/sglang/multimodal_gen/test/unit/test_ci_gpu_idle.py`, `python/sglang/multimodal_gen/test/unit/test_zimage_rope_cache.py`_
- **2026-10-26** [`11550a5845`](https://github.com/sgl-project/sglang/commit/11550a5845) [#46396](https://github.com/sgl-project/sglang/pull/46396)
  [CI] [AMD] diffusion: Skip the Wan CuTe DSL q/k norm RoPE imports on ROCm (#46396)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`_
- **2026-10-26** [`ae579c5e00`](https://github.com/sgl-project/sglang/commit/ae579c5e00) [#44160](https://github.com/sgl-project/sglang/pull/44160)
  [Fix] multimodal: Preserve caller hashes and offsets for precomputed inputs (#44160)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `test/registered/unit/multimodal/test_precomputed_embedding_validation.py`_
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

## Prefill / Decode Disaggregation  (72 commits)

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
- **2026-11-01** [`240f2a0a64`](https://github.com/sgl-project/sglang/commit/240f2a0a64) [#47758](https://github.com/sgl-project/sglang/pull/47758)
  [Fix] disagg: Give the decode queue test scheduler a tree_cache (#47758)
  _Files: `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-11-01** [`1c0dc0293d`](https://github.com/sgl-project/sglang/commit/1c0dc0293d) [#47716](https://github.com/sgl-project/sglang/pull/47716)
  [Fix] scheduler: Decide early result processing before scheduling the next batch (#47716)
  _Files: `.agents/skills/env-var-conventions/SKILL.md`, `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/environ.py` _+9 more__
- **2026-11-01** [`d3bf0b4e52`](https://github.com/sgl-project/sglang/commit/d3bf0b4e52) [#43900](https://github.com/sgl-project/sglang/pull/43900)
  [Refactor] scheduler: Route every step launch through one hook and count in-flight steps (#43900)
  _Files: `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py` _+7 more__
- **2026-11-01** [`cb0a7a953f`](https://github.com/sgl-project/sglang/commit/cb0a7a953f) [#46395](https://github.com/sgl-project/sglang/pull/46395)
  [Feat] disagg: Write PD decode KV to the linker and skip pages the prefill already stored (#46395)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py` _+4 more__
- **2026-11-01** [`c757c4bb7c`](https://github.com/sgl-project/sglang/commit/c757c4bb7c) [#47732](https://github.com/sgl-project/sglang/pull/47732)
  [Fix] kv_events: Offset ipc endpoints per DP rank and finish shutdown when the queue is full (#47732)
  _Files: `python/sglang/srt/disaggregation/kv_events.py`, `test/registered/unit/disaggregation/test_kv_events.py`_
- **2026-11-01** [`4aaa8997af`](https://github.com/sgl-project/sglang/commit/4aaa8997af) [#45981](https://github.com/sgl-project/sglang/pull/45981)
  [CI] lora: Simplify LoRA tests and add a lora rerun group (#45981)
  _Files: `.github/workflows/pr-test-xpu.yml`, `python/sglang/test/kits/bcg_lora_kit.py`, `python/sglang/test/kits/inkling_sink_lora_kit.py`, `python/sglang/test/kits/lora_prefill_graph_kit.py` _+85 more__
- **2026-11-01** [`43881a719e`](https://github.com/sgl-project/sglang/commit/43881a719e) [#47727](https://github.com/sgl-project/sglang/pull/47727)
  [Fix] disaggregation: Call finalize_bootstrap outside the assert statement (#47727)
  _Files: `python/sglang/srt/disaggregation/prefill.py`_
- **2026-11-01** [`76066d6908`](https://github.com/sgl-project/sglang/commit/76066d6908) [#47725](https://github.com/sgl-project/sglang/pull/47725)
  [Fix] disaggregation: Initialize the bootstrap server loop and runner before the server thread starts (#47725)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `test/registered/unit/disaggregation/test_receiver_connection_pool.py`_
- **2026-11-01** [`3edea93cbc`](https://github.com/sgl-project/sglang/commit/3edea93cbc) [#47704](https://github.com/sgl-project/sglang/pull/47704)
  [Fix] disaggregation: Match the whole bootstrap address when evicting a dead prefill's connections (#47704)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-10-31** [`fc32cbff69`](https://github.com/sgl-project/sglang/commit/fc32cbff69) [#46373](https://github.com/sgl-project/sglang/pull/46373)
  [Fix] disaggregation: Send decode transfer destinations to prefill only after the in-flight forward (#46373)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`, `test/registered/unit/disaggregation/test_deferred_decode_kv_release.py` _+4 more__
- **2026-10-31** [`e624174f07`](https://github.com/sgl-project/sglang/commit/e624174f07) [#47652](https://github.com/sgl-project/sglang/pull/47652)
  [Fix] disaggregation: Ignore a late STAGING_REQ for an already-scattered staging chunk (#47652)
  _Files: `python/sglang/srt/disaggregation/common/staging_buffer.py`, `python/sglang/srt/disaggregation/common/staging_handler.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-10-31** [`5eb7018347`](https://github.com/sgl-project/sglang/commit/5eb7018347) [#47638](https://github.com/sgl-project/sglang/pull/47638)
  [Fix] disaggregation: Send aux_item_lens next to aux_ptrs in PD registration (#47638)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_receiver_connection_pool.py`_
- **2026-10-31** [`f78d906f3e`](https://github.com/sgl-project/sglang/commit/f78d906f3e) [#40107](https://github.com/sgl-project/sglang/pull/40107)
  [Fix] disaggregation: Preserve sampler customized_info across PD (#40107)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py` _+20 more__
- **2026-10-31** [`d9692649e6`](https://github.com/sgl-project/sglang/commit/d9692649e6) [#47603](https://github.com/sgl-project/sglang/pull/47603)
  [CI] test: Drop tests that never run in CI (#47603)
  _Files: `scripts/ci/rerun_test_groups.json`, `test/manual/spec/test_spec_standalone_backends.py`, `test/registered/attention/test_triton_sliding_window.py`, `test/registered/disaggregation/test_disaggregation_hisparse.py` _+34 more__
- **2026-10-31** [`b8d86350d2`](https://github.com/sgl-project/sglang/commit/b8d86350d2) [#43899](https://github.com/sgl-project/sglang/pull/43899)
  [Refactor] scheduler: Track running requests in an owner list (#43899)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py` _+12 more__
- **2026-10-31** [`2f6e7f3475`](https://github.com/sgl-project/sglang/commit/2f6e7f3475) [#44718](https://github.com/sgl-project/sglang/pull/44718)
  [Feat] [AMD] mamba: Store hicache checkpoints without a GPU slot (#44718)
  _Files: `python/sglang/kernels/ops/attention/linear/fused_kda_conv_recurrent_verify.py`, `python/sglang/kernels/ops/attention/linear/fused_sigmoid_gating_recurrent.py`, `python/sglang/kernels/ops/attention/linear/kda_replayssm_spec_decode.py`, `python/sglang/srt/disaggregation/decode.py` _+32 more__
- **2026-10-31** [`566dbd2cb3`](https://github.com/sgl-project/sglang/commit/566dbd2cb3) [#46898](https://github.com/sgl-project/sglang/pull/46898)
  [Perf] disaggregation: Stop device admission in a decode transfer pass at the first refusal (#46898)
  _Files: `python/sglang/srt/disaggregation/decode.py`_
- **2026-10-31** [`4df3895bdd`](https://github.com/sgl-project/sglang/commit/4df3895bdd) [#47544](https://github.com/sgl-project/sglang/pull/47544)
  [Refactor] disaggregation: Commit the PD handoff token through the shared per-token commit (#47544)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/scheduler_components/logprob_result_processor.py`, `test/registered/core/test_srt_endpoint.py` _+1 more__
- **2026-10-30** [`3e83f3a71a`](https://github.com/sgl-project/sglang/commit/3e83f3a71a) [#47177](https://github.com/sgl-project/sglang/pull/47177)
  [Perf] pd: Copy the last chunk's state page indices to the host without a scheduler sync (#47177)
  _Files: `python/sglang/srt/disaggregation/prefill.py`_
- **2026-10-30** [`c105a91b43`](https://github.com/sgl-project/sglang/commit/c105a91b43) [#47521](https://github.com/sgl-project/sglang/pull/47521)
  [Fix] scheduler: Abort retracted requests whose KV the recompute cannot rebuild (#47521)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/entrypoints/openai/serving_tokenize.py` _+7 more__
- **2026-10-30** [`a076243cea`](https://github.com/sgl-project/sglang/commit/a076243cea) [#43898](https://github.com/sgl-project/sglang/pull/43898)
  [Refactor] scheduler: Remove PD multiplexing (#43898)
  _Files: `docs/docs/advanced_features/pd_disaggregation.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/advanced_features/speculative_decoding.mdx`, `docs/docs/developer_guide/layer_boundary.mdx` _+96 more__
- **2026-10-30** [`d51a1e5d97`](https://github.com/sgl-project/sglang/commit/d51a1e5d97) [#45328](https://github.com/sgl-project/sglang/pull/45328)
  [Perf] pd: Publish decode KV destinations without host syncs under overlap (#45328)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/utils.py` _+4 more__
- **2026-10-30** [`e7dd1d094d`](https://github.com/sgl-project/sglang/commit/e7dd1d094d) [#47085](https://github.com/sgl-project/sglang/pull/47085)
  [Feat] RL: Report prompt KV weight versions in generation metadata (#47085)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/advanced_features/sglang_for_rl.mdx`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/exec_.py` _+33 more__
- **2026-10-30** [`e3718813ec`](https://github.com/sgl-project/sglang/commit/e3718813ec) [#46485](https://github.com/sgl-project/sglang/pull/46485)
  [Feat] observability: Add scheduler_iterations_total metric (#46485)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py` _+5 more__
- **2026-10-30** [`e337bb10b5`](https://github.com/sgl-project/sglang/commit/e337bb10b5) [#46892](https://github.com/sgl-project/sglang/pull/46892)
  [Feat] docker: Update the EFA images to EFA installer 1.51.0 (#46892)
  _Files: `docker/efa.Dockerfile`, `docs/docs/advanced_features/pd_disaggregation.mdx`_
- **2026-10-30** [`8080507c3e`](https://github.com/sgl-project/sglang/commit/8080507c3e) [#47260](https://github.com/sgl-project/sglang/pull/47260)
  [Perf] detokenizer: Send per-request decode inputs once and keep them in the detokenizer (#47260)
  _Files: `python/sglang/srt/beam_search/output.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/incremental_detokenize.py` _+19 more__
- **2026-10-30** [`03aba9e647`](https://github.com/sgl-project/sglang/commit/03aba9e647) [#47366](https://github.com/sgl-project/sglang/pull/47366)
  [Fix] disaggregation: Keep output ids during a PD rebootstrap instead of popping and replaying the last one (#47366)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+6 more__
- **2026-10-30** [`2830808030`](https://github.com/sgl-project/sglang/commit/2830808030) [#43896](https://github.com/sgl-project/sglang/pull/43896)
  [Refactor] scheduler: Write every request finish state through Req methods (#43896)
  _Files: `python/sglang/srt/beam_search/coordinator.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` _+15 more__
- **2026-10-29** [`f3f23d128c`](https://github.com/sgl-project/sglang/commit/f3f23d128c) [#43895](https://github.com/sgl-project/sglang/pull/43895)
  [Refactor] scheduler: Write every request KV length through ReqKvInfo methods (#43895)
  _Files: `python/sglang/srt/beam_search/fork.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/schedule_batch.py` _+22 more__
- **2026-10-29** [`15bb4a0fc9`](https://github.com/sgl-project/sglang/commit/15bb4a0fc9) [#45434](https://github.com/sgl-project/sglang/pull/45434)
  [Feat] cp: Add KV layout hooks and padded storage accounting (#45434)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/choices.py`, `python/sglang/srt/arg_groups/field_order.py`, `python/sglang/srt/arg_groups/fields/parallel.py` _+28 more__
- **2026-10-29** [`acdad27d74`](https://github.com/sgl-project/sglang/commit/acdad27d74) [#47124](https://github.com/sgl-project/sglang/pull/47124)
  [Feat] disaggregation: Decode host receive on the unified page-envelope host pool (#47124)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/mem_cache/l2_transfer.py`, `python/sglang/srt/mem_cache/pool_host/base.py` _+3 more__
- **2026-10-29** [`2749b946de`](https://github.com/sgl-project/sglang/commit/2749b946de) [#47015](https://github.com/sgl-project/sglang/pull/47015)
  [Perf] pd: Poll finished KV transfers while the prefill loop waits for a forward result (#47015)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py`, `test/registered/unit/disaggregation/test_prefill_result_polling.py`_
- **2026-10-29** [`1f80b2b21d`](https://github.com/sgl-project/sglang/commit/1f80b2b21d) [#47045](https://github.com/sgl-project/sglang/pull/47045)
  [Fix] disaggregation: Agree on each prefill KV transfer's outcome across PP stages (#47045)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/registered/unit/managers/test_pp_prefill_transfer_outcome.py`_
- **2026-10-29** [`03864d7b2f`](https://github.com/sgl-project/sglang/commit/03864d7b2f) [#47063](https://github.com/sgl-project/sglang/pull/47063)
  [Fix] disaggregation: Agree on each decode KV transfer's outcome across PP stages (#47063)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/registered/unit/managers/test_pp_decode_transfer_outcome.py`_
- **2026-10-29** [`b9407b44c7`](https://github.com/sgl-project/sglang/commit/b9407b44c7) [#43299](https://github.com/sgl-project/sglang/pull/43299)
  [Fix] disaggregation: Fix the early-send wait event on non-CUDA devices and in nixl (#43299)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `test/registered/unit/disaggregation/test_dcp_pack.py` _+3 more__
- **2026-10-28** [`e105742296`](https://github.com/sgl-project/sglang/commit/e105742296) [#45580](https://github.com/sgl-project/sglang/pull/45580)
  [Fix] linker: Order loads behind the forward that may still use the pages (#45580)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_direct_linker.py`, `python/sglang/srt/mem_cache/storage/umbp/umbp_direct_linker.py`, `python/sglang/srt/mem_cache/unified_cache/unified_cache_linker.py`, `test/registered/unit/mem_cache/test_umbp_direct_linker_rank_keys.py` _+1 more__
- **2026-10-28** [`9d2dae3907`](https://github.com/sgl-project/sglang/commit/9d2dae3907) [#46789](https://github.com/sgl-project/sglang/pull/46789)
  [Test] KVShard: Extend HiCache E2E with GLM accuracy coverage (#46789)
  _Files: `docs/docs.json`, `docs/docs/advanced_features/kv_cache_sharing.mdx`, `docs/docs/advanced_features/pd_disaggregation.mdx`, `docs/docs/advanced_features/server_arguments.mdx` _+1 more__
- **2026-10-28** [`e028ee40b0`](https://github.com/sgl-project/sglang/commit/e028ee40b0) [#46991](https://github.com/sgl-project/sglang/pull/46991)
  [Refactor] cache: Build prefix-tree components from storage slots (#46991)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/llada_image/conditioning.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/auxiliary_state.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+72 more__
- **2026-10-28** [`146378629d`](https://github.com/sgl-project/sglang/commit/146378629d) [#46989](https://github.com/sgl-project/sglang/pull/46989)
  [Refactor] kv-cache: Share storage interfaces across runtime consumers (#46989)
  _Files: `python/sglang/srt/beam_search/coordinator.py`, `python/sglang/srt/beam_search/fork.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` _+22 more__
- **2026-10-28** [`53592ea5ff`](https://github.com/sgl-project/sglang/commit/53592ea5ff) [#46988](https://github.com/sgl-project/sglang/pull/46988)
  [Refactor] kv-cache: Centralize request rows and allocation lifecycle (#46988)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/schedule_batch.py` _+43 more__
- **2026-10-28** [`eb79ecca11`](https://github.com/sgl-project/sglang/commit/eb79ecca11) [#46985](https://github.com/sgl-project/sglang/pull/46985)
  [Refactor] mem-cache: Track transfer pins at allocator boundaries (#46985)
  _Files: `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py` _+24 more__
- **2026-10-28** [`f80cb3a2fd`](https://github.com/sgl-project/sglang/commit/f80cb3a2fd) [#46984](https://github.com/sgl-project/sglang/pull/46984)
  [Refactor] mem-cache: Replace unified pool variants with a routed cache (#46984)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/layers/attention/aiter_backend.py` _+45 more__
- **2026-10-28** [`298b563596`](https://github.com/sgl-project/sglang/commit/298b563596) [#46982](https://github.com/sgl-project/sglang/pull/46982)
  [Refactor] mem-cache: Build cache transfers from storage plans (#46982)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` _+13 more__
- **2026-10-28** [`3b597cb76d`](https://github.com/sgl-project/sglang/commit/3b597cb76d) [#46979](https://github.com/sgl-project/sglang/pull/46979)
  [Refactor] mem-cache: Route layer access through KV subpool views (#46979)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/aiter_utils.py`, `python/sglang/srt/layers/attention/base_attn_backend.py` _+39 more__
- **2026-10-28** [`cf3d21b0c9`](https://github.com/sgl-project/sglang/commit/cf3d21b0c9) [#46978](https://github.com/sgl-project/sglang/pull/46978)
  [Refactor] mem-cache: Describe KV address translation with ID spaces (#46978)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/disaggregation/checksum.py`, `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/layers/attention/aiter_backend.py` _+34 more__
- **2026-10-28** [`ccc71fa514`](https://github.com/sgl-project/sglang/commit/ccc71fa514) [#46976](https://github.com/sgl-project/sglang/pull/46976)
  [Refactor] mem_cache: Use one allocator for unified KV sub-pools (#46976)
  _Files: `python/sglang/srt/arg_groups/kv_cache_hook.py`, `python/sglang/srt/kv_canary/api.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/allocator/base.py` _+59 more__
- **2026-10-28** [`3355d668ce`](https://github.com/sgl-project/sglang/commit/3355d668ce) [#46975](https://github.com/sgl-project/sglang/pull/46975)
  [Fix] mem_cache: Forward HiCache completion events to recurrent state (#46975)
  _Files: `python/sglang/srt/mem_cache/allocator/unified_hybrid_swa.py`, `test/registered/unit/disaggregation/test_unified_memory_move_gate.py`_
- **2026-10-27** [`b74fd392e1`](https://github.com/sgl-project/sglang/commit/b74fd392e1) [#45474](https://github.com/sgl-project/sglang/pull/45474)
  [Perf] [NVIDIA] speculative: Move the host work between Qwen3.5 MTP decode graphs into the graphs (1/2) (#45474)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/small_field_copy.cuh`, `python/sglang/kernels/ops/attention/fla/chunk.py`, `python/sglang/kernels/ops/attention/fla/chunk_o.py`, `python/sglang/kernels/ops/mamba/gdn_prefill_track.py` _+29 more__
- **2026-10-27** [`4a58dc9838`](https://github.com/sgl-project/sglang/commit/4a58dc9838) [#43450](https://github.com/sgl-project/sglang/pull/43450)
  [Feat] scheduler: Add forward observer and deferred responses for plugins (#43450)
  _Files: `python/sglang/srt/managers/deferred_output.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py` _+9 more__
- **2026-10-27** [`b28f4fc065`](https://github.com/sgl-project/sglang/commit/b28f4fc065) [#46689](https://github.com/sgl-project/sglang/pull/46689)
  [Perf] disaggregation: Restore host-received decode KV without blocking the scheduler (#46689)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/l2_transfer.py` _+3 more__
- **2026-10-27** [`7fe5b127e4`](https://github.com/sgl-project/sglang/commit/7fe5b127e4) [#45678](https://github.com/sgl-project/sglang/pull/45678)
  [Fix] disaggregation: Avoid extra GPU contexts with PD (#45678)
  _Files: `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py`_
- **2026-10-27** [`2a7987f900`](https://github.com/sgl-project/sglang/commit/2a7987f900) [#44081](https://github.com/sgl-project/sglang/pull/44081)
  [Fix] PD: Skip the cached-prefix early send in batches that start a HiCache load-back (#44081)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/disaggregation/test_prefill_result_polling.py`_
- **2026-10-27** [`8136cbce3d`](https://github.com/sgl-project/sglang/commit/8136cbce3d) [#42973](https://github.com/sgl-project/sglang/pull/42973)
  [Feat] KVShard: Integrate GLM DSA/MTP with PD and CPU HiCache (#42973)
  _Files: `docs/docs/advanced_features/pd_disaggregation.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/kv_shard_hook.py`, `python/sglang/srt/disaggregation/common/conn.py` _+24 more__
- **2026-10-27** [`d69e810f71`](https://github.com/sgl-project/sglang/commit/d69e810f71) [#46708](https://github.com/sgl-project/sglang/pull/46708)
  [CI] models: Move less-used model tests to extra and nightly suites (#46708)
  _Files: `.github/actions/check-pr-test-health/action.test.cjs`, `.github/actions/check-pr-test-health/action.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd.yml` _+42 more__
- **2026-10-27** [`def8f93212`](https://github.com/sgl-project/sglang/commit/def8f93212) [#46510](https://github.com/sgl-project/sglang/pull/46510)
  [CI] rerun: Register the Mooncake test group (#46510)
  _Files: `scripts/ci/rerun_test_groups.json`_
- **2026-10-27** [`7f8ad67373`](https://github.com/sgl-project/sglang/commit/7f8ad67373) [#46144](https://github.com/sgl-project/sglang/pull/46144)
  [Fix] diffusion/disagg: Recompute automatic topology per role (#46144)
  _Files: `docs/docs/sglang-diffusion/disaggregation.mdx`, `python/sglang/multimodal_gen/runtime/launch_server.py`, `python/sglang/multimodal_gen/runtime/server_args/disagg.py`, `python/sglang/multimodal_gen/test/unit/test_launch_server_shutdown.py` _+1 more__
- **2026-10-26** [`66f79f1a90`](https://github.com/sgl-project/sglang/commit/66f79f1a90) [#45254](https://github.com/sgl-project/sglang/pull/45254)
  [Feat] kernels: Beam model support (#45254)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `docs/docs/basic_usage/native_api.mdx`, `docs/docs/references/environment_variables.mdx`, `python/sglang/kernels/jit/csrc/distributed/beam_all_reduce.cuh` _+79 more__
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

## MoE / Expert Parallel  (66 commits)

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
- **2026-11-01** [`e37c1fb020`](https://github.com/sgl-project/sglang/commit/e37c1fb020) [#46691](https://github.com/sgl-project/sglang/pull/46691)
  [Feat] [AMD] minimax: gfx950 MoE, router GEMV, block-fp8 GEMM and fp8 producer kernels (#46691)
  _Files: `python/sglang/kernels/jit/utils/hipcc.py`, `python/sglang/kernels/ops/gemm/aiter_asm_blockscale.py`, `python/sglang/kernels/ops/gemm/router_gemv.py`, `python/sglang/kernels/ops/gemm/smallm_fp8_gfx950/__init__.py` _+19 more__
- **2026-11-01** [`e232ebf6b0`](https://github.com/sgl-project/sglang/commit/e232ebf6b0) [#47236](https://github.com/sgl-project/sglang/pull/47236)
  [Perf] [AMD] moe/topk: Use the Triton softmax top-k router for Qwen3-Next (hidden 2048) (#47236)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/amd/test_qwen35_moe_softmax_topk.py`_
- **2026-11-01** [`b146a8576d`](https://github.com/sgl-project/sglang/commit/b146a8576d) [#40708](https://github.com/sgl-project/sglang/pull/40708)
  [Perf] [AMD] qwen3.5: Route 512-expert softmax MoE routing through aiter topk_gating (#40708)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/topk.py`, `test/registered/amd/test_qwen38_moe_softmax_topk_gating.py`_
- **2026-10-31** [`1c1166ad04`](https://github.com/sgl-project/sglang/commit/1c1166ad04) [#46724](https://github.com/sgl-project/sglang/pull/46724)
  [Perf] [NVIDIA] muse-spark-open: Fuse MoE finalize with the 2shot_push all-reduce (#46724)
  _Files: `python/sglang/kernels/ops/communication/muse_spark_moe_finalize_all_reduce.py`, `python/sglang/kernels/ops/communication/muse_spark_moe_finalize_all_reduce_cutedsl.py`, `python/sglang/srt/layers/communication/muse_spark_finalize_workspace.py`_
- **2026-10-31** [`ef4f3f1151`](https://github.com/sgl-project/sglang/commit/ef4f3f1151) [#37367](https://github.com/sgl-project/sglang/pull/37367)
  [Perf] [AMD] moe: Resolve MoRI dispatch from the AITER activation contract (#37367)
  _Files: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/token_dispatcher/base.py`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/layers/quantization/fp8.py` _+2 more__
- **2026-10-31** [`6e4d53fbc4`](https://github.com/sgl-project/sglang/commit/6e4d53fbc4) [#47577](https://github.com/sgl-project/sglang/pull/47577)
  [Fix] megamoe: Allocate the symmetric buffers before KV cache sizing (#47577)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/spec.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/model_executor/model_runner.py` _+1 more__
- **2026-10-31** [`fb33962605`](https://github.com/sgl-project/sglang/commit/fb33962605) [#47408](https://github.com/sgl-project/sglang/pull/47408)
  [Fix] [AMD] quark: Fix the EP>1 crash in the Quark MXFP4 W4A16 MoE path and restrict it to gfx1151 (#47408)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe_w4a16.py`_
- **2026-10-31** [`c7290006d1`](https://github.com/sgl-project/sglang/commit/c7290006d1) [#40890](https://github.com/sgl-project/sglang/pull/40890)
  [Perf] [NPU] mimo: fold attention_value_scale into o_proj weights (#40890)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/mimo_v2.py`_
- **2026-10-30** [`319b98226f`](https://github.com/sgl-project/sglang/commit/319b98226f) [#47070](https://github.com/sgl-project/sglang/pull/47070)
  [Perf] [NVIDIA] moe: Add H20 block-FP8 Triton configs for Qwen3-30B-A3B (#47070)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=128,N=768,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`_
- **2026-10-30** [`51d5502aff`](https://github.com/sgl-project/sglang/commit/51d5502aff) [#44268](https://github.com/sgl-project/sglang/pull/44268)
  [Fix] moe: Fix --enable-fused-moe-sum-all-reduce outside CUDA and with LoRA hooks (#44268)
- **2026-10-30** [`5d4a6f499e`](https://github.com/sgl-project/sglang/commit/5d4a6f499e) [#44750](https://github.com/sgl-project/sglang/pull/44750)
  [Fix] nemotron-h: Allow explicit CuTe DSL W4A16 MoE (#44750)
  _Files: `python/sglang/srt/arg_groups/model_overrides/nemotron_h.py`, `test/registered/unit/test_model_overrides.py`_
- **2026-10-30** [`8fd181eaf4`](https://github.com/sgl-project/sglang/commit/8fd181eaf4) [#46759](https://github.com/sgl-project/sglang/pull/46759)
  [CI] [NPU] nightly: add rerun suites for three 2-NPU cases (#46759)
  _Files: `test/registered/unit/npu/attention/test_npu_ascend_torch_native_backend.py`, `test/registered/unit/npu/attention/test_npu_dcp.py`, `test/registered/unit/npu/graph_runner/test_npu_cudagraph_backend.py`, `test/registered/unit/npu/graph_runner/test_npu_graph_capture.py` _+6 more__
- **2026-10-30** [`0fd1e3a799`](https://github.com/sgl-project/sglang/commit/0fd1e3a799) [#43788](https://github.com/sgl-project/sglang/pull/43788)
  [Fix] [AMD] deterministic: Bypass AITER GEMM and MoE in deterministic mode on gfx950 (#43788)
  _Files: `python/sglang/srt/layers/quantization/unquant.py`, `test/registered/attention/test_deterministic.py`_
- **2026-10-30** [`196ee6b611`](https://github.com/sgl-project/sglang/commit/196ee6b611) [#45486](https://github.com/sgl-project/sglang/pull/45486)
  [Fix] [AMD] MoE: Preserve CT FP8 Triton layout and reduction dimensions (#45486)
  _Files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `test/registered/unit/layers/quantization/test_compressed_tensors_fp8_moe_layout.py`_
- **2026-10-30** [`ca93940742`](https://github.com/sgl-project/sglang/commit/ca93940742) [#46018](https://github.com/sgl-project/sglang/pull/46018)
  [Fix] humming: adapt integration to kernels 0.1.18 (#46018)
  _Files: `python/pyproject.toml`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/humming.py`, `python/sglang/srt/layers/quantization/humming.py` _+8 more__
- **2026-10-30** [`4201b8fa99`](https://github.com/sgl-project/sglang/commit/4201b8fa99) [#47149](https://github.com/sgl-project/sglang/pull/47149)
  [Perf] dsv4: Fix amax8_varlen and mega MoE pre-dispatch grids for 1024-thread SMs (#47149)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/block_amax.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `test/registered/kernels/ops/moe/test_mega_moe_pre_dispatch.py`_
- **2026-10-30** [`80afdc1280`](https://github.com/sgl-project/sglang/commit/80afdc1280) [#46623](https://github.com/sgl-project/sglang/pull/46623)
  [Feat] xpu: Consolidate simple XPU enablements (#46623)
  _Files: `docker/xpu.Dockerfile`, `python/sglang/benchmark/one_batch.py`, `python/sglang/kernels/ops/attention/fla/fused_recurrent.py`, `python/sglang/srt/arg_groups/hisparse_hook.py` _+18 more__
- **2026-10-30** [`730ed066bf`](https://github.com/sgl-project/sglang/commit/730ed066bf) [#46456](https://github.com/sgl-project/sglang/pull/46456)
  [Perf] paged-experts: exact size pinning (#46456)
  _Files: `python/sglang/srt/layers/moe/paged_experts/store.py`, `test/registered/kernels/ops/moe/test_paged_experts_kernels.py`_
- **2026-10-29** [`20036b7add`](https://github.com/sgl-project/sglang/commit/20036b7add) [#47115](https://github.com/sgl-project/sglang/pull/47115)
  [Perf] moe: Fill padded rows of large narrow buffers with a strided grid (#47115)
  _Files: `python/sglang/kernels/ops/moe/fill_padded_rows.py`, `test/registered/moe/test_topk_padded_region.py`_
- **2026-10-29** [`45fbc06e21`](https://github.com/sgl-project/sglang/commit/45fbc06e21) [#47304](https://github.com/sgl-project/sglang/pull/47304)
  [Perf] dsv41: Drop per-layer routing glue under simulated routing with EPLB (#47304)
  _Files: `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/eplb/expert_location_dispatch.py`, `python/sglang/srt/layers/moe/mega_gate.py`, `python/sglang/srt/layers/moe/topk.py`_
- **2026-10-29** [`3a3a8611a4`](https://github.com/sgl-project/sglang/commit/3a3a8611a4) [#46592](https://github.com/sgl-project/sglang/pull/46592)
  [Fix] eplb: Warm default-group P2P transports on multi-node layouts (#46592)
  _Files: `python/sglang/srt/distributed/bootstrap.py`_
- **2026-10-29** [`2c6b95e035`](https://github.com/sgl-project/sglang/commit/2c6b95e035) [#41389](https://github.com/sgl-project/sglang/pull/41389)
  [Feat] [AMD] Quark: Run Quark MXFP4 MoE as W4A16 via triton_kernels on RDNA (gfx1151) (#41389)
  _Files: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`_
- **2026-10-29** [`de6c211a49`](https://github.com/sgl-project/sglang/commit/de6c211a49) [#45802](https://github.com/sgl-project/sglang/pull/45802)
  [Fix] [AMD] quark: Skip no-copy loads after MXFP4 quantization (#45802)
  _Files: `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4_moe.py`, `test/registered/unit/layers/quantization/test_quark_w4a4_mxfp4_moe.py`_
- **2026-10-29** [`ebfbd3ea35`](https://github.com/sgl-project/sglang/commit/ebfbd3ea35) [#45800](https://github.com/sgl-project/sglang/pull/45800)
  [Fix] GLM: Preserve NextN PTPC quantization for excluded experts (#45800)
  _Files: `python/sglang/srt/models/glm4_moe.py`, `test/registered/unit/models/test_glm_nextn_moe_ptpc.py`_
- **2026-10-29** [`019008afe0`](https://github.com/sgl-project/sglang/commit/019008afe0) [#46212](https://github.com/sgl-project/sglang/pull/46212)
  [Feat] [NPU] Quant: support Qwen3.6-35B-A3B-FP8 which is block FP8 MOE. (#46212)
  _Files: `python/sglang/kernels/ops/gemm/__init__.py`, `python/sglang/kernels/ops/gemm/npu_block_fp8.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py` _+7 more__
- **2026-10-29** [`d7522db332`](https://github.com/sgl-project/sglang/commit/d7522db332) [#45946](https://github.com/sgl-project/sglang/pull/45946)
  [Feat] sail: support sail fa3 and flashmla [3/N] (#45946)
  _Files: `.github/workflows/pr-test-ppu.yml`, `python/pyproject_other.toml`, `python/sglang/srt/arg_groups/attention_hook.py`, `python/sglang/srt/arg_groups/model_override_base.py` _+32 more__
- **2026-10-29** [`3256c33825`](https://github.com/sgl-project/sglang/commit/3256c33825) [#35955](https://github.com/sgl-project/sglang/pull/35955)
  [Fix] gptq_marlin: Fix BF16 dtype and TP act-order w2 scales in MoE (#35955)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`, `python/sglang/srt/layers/quantization/gptq/schemes/gptq_cpu.py`, `python/sglang/srt/layers/quantization/gptq/schemes/gptq_moe.py` _+2 more__
- **2026-10-29** [`100f4d7536`](https://github.com/sgl-project/sglang/commit/100f4d7536) [#46731](https://github.com/sgl-project/sglang/pull/46731)
  [Perf] [AMD] moe: Add tuned Triton fused MoE config for gemma-4-26B-A4B on MI355X (#46731)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_8_0/E=128,N=704,device_name=AMD_Instinct_MI355X.json`_
- **2026-10-29** [`f2d3188925`](https://github.com/sgl-project/sglang/commit/f2d3188925) [#46090](https://github.com/sgl-project/sglang/pull/46090)
  [Perf] moe: Fold the routed scaling factor into the mega MoE pre-dispatch (#46090)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/kernels/ops/moe/dsv4.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `test/registered/kernels/ops/moe/test_mega_moe_pre_dispatch.py`_
- **2026-10-28** [`76d5b3ce02`](https://github.com/sgl-project/sglang/commit/76d5b3ce02) [#47148](https://github.com/sgl-project/sglang/pull/47148)
  [Perf] dsv41: Run MegaGate routing in prefill (#47148)
  _Files: `python/sglang/srt/layers/moe/mega_gate.py`, `test/registered/unit/layers/moe/test_mega_moe_deepgemm_api.py`_
- **2026-10-28** [`41eaeb0445`](https://github.com/sgl-project/sglang/commit/41eaeb0445) [#33916](https://github.com/sgl-project/sglang/pull/33916)
  [Perf] [AMD] kimi-k3: Remove per-layer copies from the aiter MoE path (#33916)
  _Files: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/layers/moe/test_aiter_runner.py` _+1 more__
- **2026-10-28** [`faa56e2b5c`](https://github.com/sgl-project/sglang/commit/faa56e2b5c) [#45889](https://github.com/sgl-project/sglang/pull/45889)
  [Fix] moe: Broadcast scalar block scales correctly with swap_ab on Triton 3.9 (#45889)
  _Files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `test/registered/kernels/ops/moe/test_fused_moe_block_fp8_scales.py`_
- **2026-10-28** [`bacf65f8f1`](https://github.com/sgl-project/sglang/commit/bacf65f8f1) [#46282](https://github.com/sgl-project/sglang/pull/46282)
  [Feat] [NPU] moe: Add Ascend Ops backend for MoE prefill and decode (#46282)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/hardware-platforms/ascend-npus/optimization/quantization.mdx`, `python/sglang/multimodal_gen/runtime/models/dits/hunyuan_image3.py`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py` _+27 more__
- **2026-10-28** [`15d39bd840`](https://github.com/sgl-project/sglang/commit/15d39bd840) [#46267](https://github.com/sgl-project/sglang/pull/46267)
  [Fix] MegaMoE: stop double-dividing the DP prefill budget (#46267)
  _Files: `python/sglang/srt/arg_groups/mega_moe_hook.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-10-28** [`bb4bb01381`](https://github.com/sgl-project/sglang/commit/bb4bb01381) [#41289](https://github.com/sgl-project/sglang/pull/41289)
  [Fix] compressed-tensors: Serve split-expert MXFP4 MoE via FP4 Marlin (#41289)
  _Files: `python/sglang/kernels/jit/csrc/gemm/marlin/gptq_marlin.cuh`, `python/sglang/kernels/jit/csrc/gemm/marlin/kernel.h`, `python/sglang/kernels/jit/csrc/gemm/marlin/marlin_template.h`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` _+10 more__
- **2026-10-27** [`f9f2665b6e`](https://github.com/sgl-project/sglang/commit/f9f2665b6e) [#44797](https://github.com/sgl-project/sglang/pull/44797)
  [Fix] [AMD] moe/topk: Preserve fp32 bias across aiter routing paths (#44797)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/kernels/ops/moe/test_moe_route_radix4.py`, `test/registered/unit/layers/moe/test_topk_correction_bias_cache.py`_
- **2026-10-27** [`7e142dd9fd`](https://github.com/sgl-project/sglang/commit/7e142dd9fd) [#46093](https://github.com/sgl-project/sglang/pull/46093)
  [Perf] moe: Always pass the global token count to the Mega MoE tile heuristic (#46093)
  _Files: `python/sglang/srt/layers/moe/mega_moe.py`_
- **2026-10-27** [`baa349af7b`](https://github.com/sgl-project/sglang/commit/baa349af7b) [#46497](https://github.com/sgl-project/sglang/pull/46497)
  [Perf] eplb: Fuse expert-count recording into one kernel on CUDA decode graphs (#46497)
  _Files: `python/sglang/kernels/ops/moe/__init__.py`, `python/sglang/kernels/ops/moe/eplb_map_record.py`, `python/sglang/srt/eplb/eplb_map_record_fused.py`, `python/sglang/srt/eplb/expert_distribution.py` _+4 more__
- **2026-10-27** [`7f07519943`](https://github.com/sgl-project/sglang/commit/7f07519943) [#43271](https://github.com/sgl-project/sglang/pull/43271)
  [Fix] DSA/KDA: Handle MoE padding in hybrid MTP verification (#43271)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer_kpool.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`_
- **2026-10-27** [`010eb729be`](https://github.com/sgl-project/sglang/commit/010eb729be) [#46792](https://github.com/sgl-project/sglang/pull/46792)
  [Refactor] bcg: Delete capture leftovers and rename `capture_stub` to `on_capture` (#46792)
  _Files: `docs/docs/advanced_features/breakable_cuda_graph.mdx`, `python/sglang/multimodal_gen/test/unit/test_attention_bcg_outputs.py`, `python/sglang/multimodal_gen/test/unit/test_qwen_image21.py`, `python/sglang/srt/layers/attention/dsa/kpool_prefill_cuda_graph.py` _+14 more__
- **2026-10-27** [`e80120b4fb`](https://github.com/sgl-project/sglang/commit/e80120b4fb) [#45363](https://github.com/sgl-project/sglang/pull/45363)
  [Fix] eplb: Load all local replicas of each expert (#45363)
  _Files: `python/sglang/srt/eplb/expert_location.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/moe_wna16.py`, `test/registered/unit/eplb/test_expert_location_weight_loading.py`_
- **2026-10-27** [`a4a19332ab`](https://github.com/sgl-project/sglang/commit/a4a19332ab) [#46567](https://github.com/sgl-project/sglang/pull/46567)
  [Perf] paged-experts: fewer host syncs in host-planned steps (#46567)
  _Files: `python/sglang/srt/layers/moe/paged_experts/executor.py`, `python/sglang/srt/layers/moe/paged_experts/residency.py`, `python/sglang/srt/layers/moe/paged_experts/runners.py`, `test/registered/unit/layers/moe/paged_experts/test_paged_experts.py`_
- **2026-10-27** [`c45ebb507d`](https://github.com/sgl-project/sglang/commit/c45ebb507d) [#46600](https://github.com/sgl-project/sglang/pull/46600)
  [Fix] diffusion: HunyuanImage-3 MoE shared MLP and timestep schedule on CUDA (#46600)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/hunyuan_image3.py`, `python/sglang/multimodal_gen/runtime/pipelines/hunyuan_image3.py`, `python/sglang/multimodal_gen/test/unit/test_hunyuan_image3_tp_broadcast.py`_
- **2026-10-27** [`41fb719cf2`](https://github.com/sgl-project/sglang/commit/41fb719cf2) [#45624](https://github.com/sgl-project/sglang/pull/45624)
  [Feat] model: Add Flint (RecursiveSI/flint) support (#45624)
  _Files: `python/sglang/srt/arg_groups/model_overrides/__init__.py`, `python/sglang/srt/arg_groups/model_overrides/flint.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/flint.py` _+8 more__
- **2026-10-27** [`8063296528`](https://github.com/sgl-project/sglang/commit/8063296528) [#46457](https://github.com/sgl-project/sglang/pull/46457)
  [Perf] paged-experts: fuse slot lookup into decide (#46457)
  _Files: `python/sglang/kernels/jit/csrc/moe/paged_experts.cuh`, `python/sglang/kernels/ops/moe/paged_experts.py`, `python/sglang/srt/layers/moe/paged_experts/executor.py`, `test/registered/kernels/ops/moe/test_paged_experts_kernels.py`_
- **2026-10-27** [`a09c1a096c`](https://github.com/sgl-project/sglang/commit/a09c1a096c) [#46309](https://github.com/sgl-project/sglang/pull/46309)
  [Perf] deepep_v2: Reduce masked GEMM buffer memory during CUDA Graph capture (#46309)
  _Files: `python/sglang/kernels/ops/moe/ep_moe_kernels.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep_v2.py`, `test/registered/unit/layers/moe/test_deepep_v2_buffer_lifecycle.py`_
- **2026-10-27** [`8353f86f0b`](https://github.com/sgl-project/sglang/commit/8353f86f0b) [#33743](https://github.com/sgl-project/sglang/pull/33743)
  [Fix] moe: Fix flashinfer TRT-LLM BF16 expert weight reload on refit (#33743)
  _Files: `docs/docs/advanced_features/sglang_for_rl.mdx`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/model_executor/model_runner_components/weight_updater.py`, `test/registered/unit/layers/quantization/test_flashinfer_trtllm_bf16_moe_reload.py`_
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

## KV Cache / Memory  (37 commits)

- **2026-11-02** [`3d33971dea`](https://github.com/sgl-project/sglang/commit/3d33971dea) [#46606](https://github.com/sgl-project/sglang/pull/46606)
  [Fix] cache: Roll back host slots when allocation raises (#46606)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/pool_host/group.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py`_
- **2026-11-01** [`0f93be7b65`](https://github.com/sgl-project/sglang/commit/0f93be7b65) [#40914](https://github.com/sgl-project/sglang/pull/40914)
  [Refactor] memory-pool: Build draft sidecar host pools from buffer info (#40914)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/host_pool_config.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `test/registered/kernels/ops/kvcache/test_hicache.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`_
- **2026-11-01** [`2d8462fef2`](https://github.com/sgl-project/sglang/commit/2d8462fef2) [#47670](https://github.com/sgl-project/sglang/pull/47670)
  [Fix] mem_cache: Keep K/V in separate allocations under torch.compile (#47670)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-11-01** [`cb7eaa2ea0`](https://github.com/sgl-project/sglang/commit/cb7eaa2ea0) [#39880](https://github.com/sgl-project/sglang/pull/39880)
  [Feat] hicache: Add the fast_file local storage backend (#39880)
  _Files: `benchmark/hicache/bench_buffer_mode.py`, `docs/docs/advanced_features/hicache_best_practices.mdx`, `docs/docs/advanced_features/hicache_design.mdx`, `docs/docs/advanced_features/hicache_storage_runtime_attach_detach.mdx` _+11 more__
- **2026-10-31** [`181380682b`](https://github.com/sgl-project/sglang/commit/181380682b) [#47557](https://github.com/sgl-project/sglang/pull/47557)
  [Fix] hicache: Withhold only protected bytes from page-cache credit (#47557)
  _Files: `python/sglang/srt/mem_cache/host_memory.py`, `test/registered/unit/mem_cache/test_host_memory.py`_
- **2026-10-31** [`a65c9c5969`](https://github.com/sgl-project/sglang/commit/a65c9c5969) [#46827](https://github.com/sgl-project/sglang/pull/46827)
  [Feat] unified-memory: Evict Full and SWA KV from one shared LRU order (joint_lru) (#46827)
  _Files: `docs/docs/advanced_features/radix_eviction_policy.mdx`, `python/sglang/srt/arg_groups/choices.py`, `python/sglang/srt/arg_groups/fields/memory.py`, `python/sglang/srt/managers/schedule_policy.py` _+10 more__
- **2026-10-31** [`2410a09c6e`](https://github.com/sgl-project/sglang/commit/2410a09c6e) [#44990](https://github.com/sgl-project/sglang/pull/44990)
  [Refactor] memory-pool: Describe DeepSeek V4 device pools with buffer info (#44990)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_memory_pool.py`, `python/sglang/srt/mem_cache/deepseek_v4_buffer_info.py`, `python/sglang/srt/mem_cache/deepseek_v4_compress_state.py`, `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py` _+9 more__
- **2026-10-31** [`9767ce3a5a`](https://github.com/sgl-project/sglang/commit/9767ce3a5a) [#47550](https://github.com/sgl-project/sglang/pull/47550)
  [Perf] model_executor: Write small forward metadata with fill kernels behind SGLANG_ENABLE_MLP_SYNC_METADATA_FILL (#47550)
  _Files: `python/sglang/kernels/ops/memory/small_copy.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/l2_transfer.py`, `python/sglang/srt/model_executor/forward_batch_info.py`_
- **2026-10-31** [`fb9846d3e2`](https://github.com/sgl-project/sglang/commit/fb9846d3e2) [#47630](https://github.com/sgl-project/sglang/pull/47630)
  [Fix] hicache: Set host_only_checkpoint in the sidecar restore test (#47630)
  _Files: `test/registered/unit/mem_cache/test_hicache_sidecar_restore.py`_
- **2026-10-31** [`1f834c1964`](https://github.com/sgl-project/sglang/commit/1f834c1964) [#43110](https://github.com/sgl-project/sglang/pull/43110)
  [Fix] hicache: Resolve derived sidecars over every source transfer (#43110)
  _Files: `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/pool_host/group.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+2 more__
- **2026-10-31** [`573649879b`](https://github.com/sgl-project/sglang/commit/573649879b) [#47542](https://github.com/sgl-project/sglang/pull/47542)
  [Perf] unified-memory: Bind the SWA tail's new pages without a host sync in alloc_extend_swa_tail (#47542)
  _Files: `python/sglang/srt/mem_cache/kv/alloc/chain.py`_
- **2026-10-31** [`9dbc462c65`](https://github.com/sgl-project/sglang/commit/9dbc462c65) [#47543](https://github.com/sgl-project/sglang/pull/47543)
  [Fix] hicache: mlock pinned host buffers so page aging never scans them (#47543)
  _Files: `python/sglang/srt/mem_cache/pool_host/common.py`_
- **2026-10-30** [`9f445266c2`](https://github.com/sgl-project/sglang/commit/9f445266c2) [#46884](https://github.com/sgl-project/sglang/pull/46884)
  [Perf] hicache: Publish prefill read-done when offload copies are fenced on the forward stream (#46884)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner_utils/shared_read_event.py`, `test/registered/unit/mem_cache/test_hicache_write_back_ordering.py` _+1 more__
- **2026-10-30** [`a8559ca775`](https://github.com/sgl-project/sglang/commit/a8559ca775) [#47424](https://github.com/sgl-project/sglang/pull/47424)
  [Test] managers: Give the chunked-abort test scheduler an output_streamer (#47424)
  _Files: `test/registered/unit/managers/test_scheduler_chunked_abort_race.py`_
- **2026-10-30** [`f96a6e42f6`](https://github.com/sgl-project/sglang/commit/f96a6e42f6) [#47381](https://github.com/sgl-project/sglang/pull/47381)
  [Fix] scheduler: Retire the beam group of an aborted chunked leader (#47381)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_chunked_abort_race.py`_
- **2026-10-29** [`974831643f`](https://github.com/sgl-project/sglang/commit/974831643f) [#46184](https://github.com/sgl-project/sglang/pull/46184)
  [Perf] mamba: write the deduplicated conv verify window as one tile (#46184)
  _Files: `python/sglang/kernels/ops/mamba/causal_conv1d_triton.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/layers/mamba/test_causal_conv1d.py`_
- **2026-10-29** [`05c59bb323`](https://github.com/sgl-project/sglang/commit/05c59bb323) [#47127](https://github.com/sgl-project/sglang/pull/47127)
  [Fix] mem_cache: Build an empty KVLayerRouter from empty layer maps (#47127)
  _Files: `python/sglang/srt/mem_cache/kv/router.py`, `test/registered/unit/mem_cache/test_kv_layer_router_parts.py`_
- **2026-10-29** [`46caa54562`](https://github.com/sgl-project/sglang/commit/46caa54562) [#47197](https://github.com/sgl-project/sglang/pull/47197)
  [Fix] hicache: Isolate NIXL storage tests from background eviction (#47197)
  _Files: `test/registered/unit/mem_cache/test_hicache_nixl_storage.py`_
- **2026-10-29** [`a99f105294`](https://github.com/sgl-project/sglang/commit/a99f105294) [#46969](https://github.com/sgl-project/sglang/pull/46969)
  [CI] permissions: Grant CI access to AMD Hyperloom and paged-experts contributors (#46969)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-10-29** [`fc778ea2af`](https://github.com/sgl-project/sglang/commit/fc778ea2af) [#46832](https://github.com/sgl-project/sglang/pull/46832)
  [Perf] [AMD] qwen3: Use the fused QK-norm + RoPE + KV write in decode with an fp8 KV cache (#46832)
  _Files: `python/sglang/srt/models/qwen3.py`, `test/registered/amd/test_qwen3_aiter_fused_qk_norm_rope.py`_
- **2026-10-28** [`6b697b9aad`](https://github.com/sgl-project/sglang/commit/6b697b9aad) [#46743](https://github.com/sgl-project/sglang/pull/46743)
  [Perf] LoRA: bound csgmv CUDA-graph segment grids by token count (#46743)
  _Files: `python/sglang/kernels/ops/lora/dense/chunked_embedding_lora_a.py`, `python/sglang/kernels/ops/lora/dense/chunked_sgmv_expand.py`, `python/sglang/kernels/ops/lora/dense/chunked_sgmv_shrink.py`, `python/sglang/srt/lora/backend/chunked_backend.py` _+2 more__
- **2026-10-28** [`ff96d43008`](https://github.com/sgl-project/sglang/commit/ff96d43008) [#47078](https://github.com/sgl-project/sglang/pull/47078)
  [Fix] ci: Repair main after the #39728/#46990 merge race and RUSTSEC-2026-0414 (#47078)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `rust/Cargo.lock`, `sgl-router/Cargo.lock`, `test/registered/unit/mem_cache/test_hicache_dcp_host_pool.py`_
- **2026-10-28** [`1721c099f9`](https://github.com/sgl-project/sglang/commit/1721c099f9) [#46981](https://github.com/sgl-project/sglang/pull/46981)
  [Fix] hicache: Build hybrid recurrent host pools consistently (#46981)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `test/registered/unit/mem_cache/test_hybrid_pool_assembler.py`_
- **2026-10-28** [`5f6075fa2f`](https://github.com/sgl-project/sglang/commit/5f6075fa2f) [#46977](https://github.com/sgl-project/sglang/pull/46977)
  [Refactor] mem_cache: Centralize unified KV capacity pricing and admission (#46977)
  _Files: `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/unified_sub_pool.py`, `python/sglang/srt/mem_cache/kv/alloc/chain.py` _+15 more__
- **2026-10-28** [`8044ed4e28`](https://github.com/sgl-project/sglang/commit/8044ed4e28) [#46972](https://github.com/sgl-project/sglang/pull/46972)
  [Fix] mem_cache: Reject unsupported int8 checkpoints with unified memory (#46972)
  _Files: `python/sglang/srt/arg_groups/mamba_hook.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-10-28** [`77936f7b25`](https://github.com/sgl-project/sglang/commit/77936f7b25) [#46971](https://github.com/sgl-project/sglang/pull/46971)
  [Fix] mem_cache: Preserve convolution slice axis in unified hybrid pools (#46971)
  _Files: `python/sglang/srt/mem_cache/unified_memory_pool.py`, `test/registered/unit/mem_cache/test_unified_layout_golden.py`, `test/registered/unit/mem_cache/unified_layout_golden.json`_
- **2026-10-28** [`ddf24c4d17`](https://github.com/sgl-project/sglang/commit/ddf24c4d17) [#46970](https://github.com/sgl-project/sglang/pull/46970)
  [Test] mem_cache: Add unified KV layout and allocator regression coverage (#46970)
  _Files: `python/sglang/test/unified_allocator_fixtures.py`, `python/sglang/test/unified_allocator_trace.py`, `test/manual/mem_cache/gen_unified_layout_golden.py`, `test/manual/mem_cache/unified_trace_compare.py` _+12 more__
- **2026-10-28** [`f59cc7e45f`](https://github.com/sgl-project/sglang/commit/f59cc7e45f) [#46805](https://github.com/sgl-project/sglang/pull/46805)
  [Perf] [NPU] dsv4: drop host-syncing ops from the decode scheduler chain (aclnnNonzeroV2 + D2H) (#46805)
  _Files: `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_allocator.py`, `python/sglang/srt/hardware_backend/npu/dsv4/dsv4_common_hooks.py`, `python/sglang/srt/mem_cache/allocation.py`_
- **2026-10-28** [`a95864d6e3`](https://github.com/sgl-project/sglang/commit/a95864d6e3) [#46440](https://github.com/sgl-project/sglang/pull/46440)
  [Chore] codeowners: Add paged experts maintainers (#46440)
  _Files: `.github/CODEOWNERS`_
- **2026-10-27** [`e7c55f6959`](https://github.com/sgl-project/sglang/commit/e7c55f6959) [#46700](https://github.com/sgl-project/sglang/pull/46700)
  [Fix] mem_cache: Clamp SWA tombstone recovery to the request's protected prefix (#46700)
  _Files: `python/sglang/srt/mem_cache/unified_cache/components/swa.py`_
- **2026-10-27** [`b7ac4c0e72`](https://github.com/sgl-project/sglang/commit/b7ac4c0e72) [#46674](https://github.com/sgl-project/sglang/pull/46674)
  [Perf] radix-tree: Keep the GIL for tree-core flag, size and digest reads unless the core is busy (#46674)
  _Files: `rust/sglang-radix-tree/src/python_bindings.rs`_
- **2026-10-27** [`f9d132b322`](https://github.com/sgl-project/sglang/commit/f9d132b322) [#31286](https://github.com/sgl-project/sglang/pull/31286)
  [Refactor] HiCache: Remove unused field `CacheInitParams::cache_ttl_second` (#31286)
  _Files: `python/sglang/srt/mem_cache/cache_init_params.py`_
- **2026-10-27** [`75468e4b4f`](https://github.com/sgl-project/sglang/commit/75468e4b4f) [#43978](https://github.com/sgl-project/sglang/pull/43978)
  [Perf] hicache: Parallel THP-backed host pool allocation (opt-in) (#43978)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/storage/mmap/mmap_allocator.py`, `test/registered/unit/mem_cache/test_mmap_allocator.py`_
- **2026-10-26** [`1596e88eda`](https://github.com/sgl-project/sglang/commit/1596e88eda) [#45673](https://github.com/sgl-project/sglang/pull/45673)
  [Fix] hicache: Skip empty auxiliary transfers (#45673)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `test/registered/unit/mem_cache/test_hicache_staged_write_back_dispatch.py`_
- **2026-10-26** [`095750baf9`](https://github.com/sgl-project/sglang/commit/095750baf9) [#46227](https://github.com/sgl-project/sglang/pull/46227)
  [Perf] diffusion: Walk several row chunks per warp in the CuTe-DSL norm kernels (#46227)
  _Files: `python/sglang/kernels/ops/diffusion/norm/cutedsl_common/norm_fusion.py`, `python/sglang/kernels/ops/diffusion/norm/cutedsl_common/reduce.py`, `python/sglang/kernels/ops/diffusion/norm/scale_residual_norm_cutedsl.py`, `test/registered/kernels/ops/diffusion/test_norm.py`_
- **2026-10-26** [`9f594d586b`](https://github.com/sgl-project/sglang/commit/9f594d586b) [#46501](https://github.com/sgl-project/sglang/pull/46501)
  [Fix] hicache: Delegate on_host_pools_registered in the failure injector (#46501)
  _Files: `python/sglang/srt/mem_cache/hicache_storage.py`_
- **2026-10-26** [`fd5c52588f`](https://github.com/sgl-project/sglang/commit/fd5c52588f) [#43539](https://github.com/sgl-project/sglang/pull/43539)
  [Test] HiCache: Inject random delays and failures for testing (#43539)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/storage/backend_factory.py` _+1 more__

## ROCm / AMD  (31 commits)

- **2026-11-02** [`16dd97df61`](https://github.com/sgl-project/sglang/commit/16dd97df61) [#46325](https://github.com/sgl-project/sglang/pull/46325)
  [Perf] [AMD] deterministic: Use a fixed-order two-stage all-reduce for large inputs (#46325)
  _Files: `python/sglang/kernels/aot/csrc/allreduce/custom_all_reduce_hip.cuh`, `python/sglang/kernels/aot/csrc/allreduce/deterministic_all_reduce.hip`, `test/registered/kernels/ops/communication/test_amd_deterministic_allreduce_fixed_order.py`_
- **2026-11-01** [`5831112d03`](https://github.com/sgl-project/sglang/commit/5831112d03) [#46685](https://github.com/sgl-project/sglang/pull/46685)
  [CI] [AMD] monokernels: Bump the sgl-amd-mono pin daily (#46685)
  _Files: `.github/scripts/pr-title.test.cjs`, `.github/workflows/bot-bump-sgl-amd-mono-version.yml`, `scripts/release/README.md`, `scripts/release/bump_sgl_amd_mono_version.py` _+1 more__
- **2026-10-31** [`2e80af2857`](https://github.com/sgl-project/sglang/commit/2e80af2857) [#47615](https://github.com/sgl-project/sglang/pull/47615)
  [Doc] [AMD] cookbook: Add GLM-5.2 MI355X AgentX recipe (#47615)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`_
- **2026-10-30** [`02cd9ff0a2`](https://github.com/sgl-project/sglang/commit/02cd9ff0a2) [#47395](https://github.com/sgl-project/sglang/pull/47395)
  [Fix] [AMD] scripts: Run and correctly test Dockerfile-only PRs (CI filter + AITER rebuild) (#47395)
  _Files: `.github/workflows/pr-test-amd.yml`, `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-10-30** [`464187fa95`](https://github.com/sgl-project/sglang/commit/464187fa95) [#47422](https://github.com/sgl-project/sglang/pull/47422)
  [Doc] [AMD] cookbook: Update muse-spark recipe 1030 (#47422)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`_
- **2026-10-30** [`a63ea5442b`](https://github.com/sgl-project/sglang/commit/a63ea5442b) [#47419](https://github.com/sgl-project/sglang/pull/47419)
  [Chore] release: Bump docs install version to 0.5.23 (#47419)
  _Files: `docs/docs/get-started/install.mdx`, `docs/docs/hardware-platforms/amd_gpu.mdx`_
- **2026-10-30** [`fcecdad5db`](https://github.com/sgl-project/sglang/commit/fcecdad5db) [#41880](https://github.com/sgl-project/sglang/pull/41880)
  [Perf] [AMD] Qwen3.8: AITER FlyDSL hc_mix for Qwen3.8 hyper-connections on gfx950 (#41880)
  _Files: `python/sglang/srt/layers/hc_mix_flydsl.py`, `python/sglang/srt/layers/hyperconnection.py`, `test/registered/kernels/ops/gemm/test_hc_mix_flydsl.py`_
- **2026-10-30** [`5035bc97fb`](https://github.com/sgl-project/sglang/commit/5035bc97fb) [#44302](https://github.com/sgl-project/sglang/pull/44302)
  [Perf] [AMD] Qwen3.8: Enable fused GDN packing for ratio-3 heads (#44302)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-10-30** [`cb4c641b3a`](https://github.com/sgl-project/sglang/commit/cb4c641b3a) [#47362](https://github.com/sgl-project/sglang/pull/47362)
  [CI] [AMD] aiter: Update ROCm AITER pin to 26f4f1fb2 (gfx1250 only) (#47362)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-29** [`686cf98470`](https://github.com/sgl-project/sglang/commit/686cf98470) [#47244](https://github.com/sgl-project/sglang/pull/47244)
  [CI] [AMD] workflows: Run scheduled Extra tests, stop skipping nightly tests, merge MI35x 1-GPU jobs- #47238 (#47244)
  _Files: `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd.yml`_
- **2026-10-29** [`639dfd0677`](https://github.com/sgl-project/sglang/commit/639dfd0677) [#44455](https://github.com/sgl-project/sglang/pull/44455)
  [Perf] [AMD] lm_head: Use aiter tgemm for the bf16 lm_head on gfx1250 (#44455)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `test/registered/unit/layers/test_logits_processor_aiter_lm_head.py`_
- **2026-10-29** [`60d56ea943`](https://github.com/sgl-project/sglang/commit/60d56ea943) [#21194](https://github.com/sgl-project/sglang/pull/21194)
  [Fix] [AMD] deepseek-v2/v3: Fix PPMissingLayer AttributeError in aiter_gfx95 code path (#21194)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-10-29** [`f854e3df13`](https://github.com/sgl-project/sglang/commit/f854e3df13) [#46825](https://github.com/sgl-project/sglang/pull/46825)
  [Doc] [AMD] cookbook: Add GLM-5.3 MI355X AgentX recipe (#46825)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.3.mdx`_
- **2026-10-29** [`9497e57c77`](https://github.com/sgl-project/sglang/commit/9497e57c77) [#47151](https://github.com/sgl-project/sglang/pull/47151)
  [CI] [AMD] pr-test: Run stage-c-test-large-8-gpu-amd as one job (#47151)
  _Files: `.github/workflows/pr-test-amd.yml`_
- **2026-10-28** [`0faacc3809`](https://github.com/sgl-project/sglang/commit/0faacc3809) [#47122](https://github.com/sgl-project/sglang/pull/47122)
  [CI] slash-command: Require explicit hardware for Extra CI (#47122)
  _Files: `.agents/skills/babysit-pr-to-pass-ci/SKILL.md`, `.agents/skills/ci-workflow-guide/SKILL.md`, `.github/FOLDER_README.md`, `.github/workflows/pr-gate.yml` _+11 more__
- **2026-10-28** [`f1a36c4789`](https://github.com/sgl-project/sglang/commit/f1a36c4789) [#47006](https://github.com/sgl-project/sglang/pull/47006)
  [Doc] [AMD] dsv4: Update amd cookbook 1028 (#47006)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-10-28** [`286e018594`](https://github.com/sgl-project/sglang/commit/286e018594) [#46703](https://github.com/sgl-project/sglang/pull/46703)
  [CI] [AMD] install: Cache the AOT kernel wheel and stop wiping venv bytecode (#46703)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-10-28** [`306a699a60`](https://github.com/sgl-project/sglang/commit/306a699a60) [#46980](https://github.com/sgl-project/sglang/pull/46980)
  [Refactor] mem-cache: Centralize recurrent state ownership and access (#46980)
- **2026-10-28** [`b85d6a8893`](https://github.com/sgl-project/sglang/commit/b85d6a8893) [#42457](https://github.com/sgl-project/sglang/pull/42457)
  [Feat] [AMD] mori: Allow MoRI for DeepSeek-V4.1 DSpark PD (#42457)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`_
- **2026-10-28** [`ef6678fae5`](https://github.com/sgl-project/sglang/commit/ef6678fae5) [#46966](https://github.com/sgl-project/sglang/pull/46966)
  [Doc] [AMD] deepseek-v4: Update MI355X C1 mono-kernel recipe (#46966)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`_
- **2026-10-28** [`5858ea88d3`](https://github.com/sgl-project/sglang/commit/5858ea88d3) [#46951](https://github.com/sgl-project/sglang/pull/46951)
  [Chore] [AMD] mono-kernel: Bump sgl-amd-mono for MoRI PD decode (#46951)
  _Files: `python/pyproject_other.toml`_
- **2026-10-28** [`5cb41c2416`](https://github.com/sgl-project/sglang/commit/5cb41c2416) [#46902](https://github.com/sgl-project/sglang/pull/46902)
  [Chore] [AMD] mono-kernel: Update sgl-amd-mono version (#46902)
  _Files: `python/pyproject_other.toml`_
- **2026-10-28** [`291f38c390`](https://github.com/sgl-project/sglang/commit/291f38c390) [#44292](https://github.com/sgl-project/sglang/pull/44292)
  [Feat] [AMD] torch-profiler: Enable torch.profiler GPU tracing on torch 2.12 / ROCm 10.1 (#44292)
  _Files: `python/sglang/__init__.py`, `python/sglang/srt/debug_utils/rocprofiler_register.py`, `python/sglang/srt/environ.py`_
- **2026-10-28** [`20b439ca77`](https://github.com/sgl-project/sglang/commit/20b439ca77) [#46750](https://github.com/sgl-project/sglang/pull/46750)
  [CI] [AMD] miles-nightly: Split the 8-GPU suite into two jobs (#46750)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm10-mi30x.yml`, `.github/workflows/nightly-test-amd-miles-rocm10.yml`_
- **2026-10-27** [`5044779f0f`](https://github.com/sgl-project/sglang/commit/5044779f0f) [#46036](https://github.com/sgl-project/sglang/pull/46036)
  [Feat] [AMD] mono-kernels: Register specs by model type (#46036)
  _Files: `python/sglang/kernels/plugin_kernels/amd/spec.py`, `python/sglang/srt/kernel_plugins/amd/binding.py`_
- **2026-10-27** [`cb55d77d37`](https://github.com/sgl-project/sglang/commit/cb55d77d37) [#46774](https://github.com/sgl-project/sglang/pull/46774)
  [CI] [AMD] deps: Install openai 2.8.0 in AMD CI for the Responses API (#46774)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-10-27** [`7e5cd57028`](https://github.com/sgl-project/sglang/commit/7e5cd57028) [#45735](https://github.com/sgl-project/sglang/pull/45735)
  [CI] slash-command: Drive opt-in CI tiers from a registry (#45735)
  _Files: `.agents/skills/ci-workflow-guide/SKILL.md`, `.github/FOLDER_README.md`, `.github/workflows/pr-gate.yml`, `.github/workflows/pr-test-amd-extra.yml` _+7 more__
- **2026-10-27** [`f9257d6c7c`](https://github.com/sgl-project/sglang/commit/f9257d6c7c) [#45576](https://github.com/sgl-project/sglang/pull/45576)
  [Perf] [AMD] rccl: upgrade rccl to 2.32.3 for rocm10.1 (#45576)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-27** [`db90f584d2`](https://github.com/sgl-project/sglang/commit/db90f584d2) [#45739](https://github.com/sgl-project/sglang/pull/45739)
  [Perf] [AMD] Qwen3-Next: fused QK Gemma RMSNorm + partial RoPE on gfx950 (#45739)
  _Files: `python/sglang/srt/models/qwen3_next.py`_
- **2026-10-26** [`eb8c2a40ef`](https://github.com/sgl-project/sglang/commit/eb8c2a40ef) [#46340](https://github.com/sgl-project/sglang/pull/46340)
  [Fix] [AMD] MiniMax-M3: default SGLANG_MINIMAX_M3_INDEX_TOPK_FREQ to 1 (#46340)
  _Files: `python/sglang/srt/environ.py`_
- **2026-10-26** [`d19f19d68c`](https://github.com/sgl-project/sglang/commit/d19f19d68c) [#46453](https://github.com/sgl-project/sglang/pull/46453)
  [CI] [AMD] pr-test: list tags with ls-remote, 8 small shards (#46453)
  _Files: `.github/workflows/pr-test-amd.yml`, `scripts/ci/amd/amd_ci_start_container.sh`, `scripts/ci/amd/amd_ci_start_container_disagg.sh`, `scripts/release/get_version_tag.py`_

## Tensor / Data Parallel  (28 commits)

- **2026-11-02** [`8c0544b9bf`](https://github.com/sgl-project/sglang/commit/8c0544b9bf) [#46166](https://github.com/sgl-project/sglang/pull/46166)
  [Perf] http: Serialize /v1/embeddings responses with model_json_response (#46166)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `test/registered/unit/entrypoints/test_embedding_responses.py`_
- **2026-11-02** [`96f5a5d78a`](https://github.com/sgl-project/sglang/commit/96f5a5d78a) [#47837](https://github.com/sgl-project/sglang/pull/47837)
  [Test] linear: Expect replicated rows to skip TP symmetric memory (#47837)
  _Files: `python/sglang/srt/hardware_backend/xpu/graph_runner/xpu_graph_runner.py`, `test/registered/unit/layers/test_linear_parallel_groups.py`_
- **2026-11-02** [`009b167f10`](https://github.com/sgl-project/sglang/commit/009b167f10) [#47744](https://github.com/sgl-project/sglang/pull/47744)
  [Fix] linear: Keep replicated outputs out of TP symmetric memory (#47744)
  _Files: `python/sglang/srt/layers/linear.py`, `test/registered/unit/layers/test_kimi_mlp_parallel_groups.py`_
- **2026-11-01** [`fdf2266c88`](https://github.com/sgl-project/sglang/commit/fdf2266c88) [#46692](https://github.com/sgl-project/sglang/pull/46692)
  [Feat] [AMD] distributed: JIT quick all-reduce for TP4 on gfx950 (#46692)
  _Files: `python/sglang/kernels/jit/csrc/distributed/quick_all_reduce/quick_all_reduce.cuh`, `python/sglang/kernels/jit/csrc/distributed/quick_all_reduce/quick_all_reduce.h`, `python/sglang/kernels/jit/csrc/distributed/quick_all_reduce/quick_all_reduce_base.h`, `python/sglang/kernels/jit/csrc/distributed/quick_all_reduce_hip.cuh` _+3 more__
- **2026-11-01** [`b80178734d`](https://github.com/sgl-project/sglang/commit/b80178734d) [#47723](https://github.com/sgl-project/sglang/pull/47723)
  [Doc] skills: Update the CI skills for the tier layout and current pipeline (#47723)
  _Files: `.agents/skills/ci-test-audit/SKILL.md`, `.agents/skills/ci-test-audit/action-items.md`, `.agents/skills/ci-workflow-guide/SKILL.md`, `.agents/skills/rerun-test/SKILL.md` _+2 more__
- **2026-10-30** [`98979301a1`](https://github.com/sgl-project/sglang/commit/98979301a1) [#45683](https://github.com/sgl-project/sglang/pull/45683)
  [Feat] muse-spark: Infer hardware launch defaults and simplify cookbook recipes (#45683)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`, `docs/src/snippets/configs/meta-models/muse-spark.jsx`, `python/sglang/srt/arg_groups/fields/parallel.py`, `python/sglang/srt/arg_groups/muse_spark_hook.py` _+2 more__
- **2026-10-30** [`a3517976f8`](https://github.com/sgl-project/sglang/commit/a3517976f8) [#47160](https://github.com/sgl-project/sglang/pull/47160)
  [Fix] rust-server: Let an HTTP layer start a native /generate request's timing (#47160)
  _Files: `rust/sglang-server/src/api_server/http/native_api.rs`, `rust/sglang-server/src/lib.rs`_
- **2026-10-30** [`039f1f786d`](https://github.com/sgl-project/sglang/commit/039f1f786d) [#47112](https://github.com/sgl-project/sglang/pull/47112)
  [Feat] rust-server: Give the native /generate hook the request, its headers and its outcome (#47112)
  _Files: `rust/sglang-server/src/api_server/http/generate_hook.rs`, `rust/sglang-server/src/api_server/http/native_api.rs`, `rust/sglang-server/src/api_server/http/openai/lowered.rs`, `rust/sglang-server/src/lib.rs`_
- **2026-10-29** [`d89a1b1ae3`](https://github.com/sgl-project/sglang/commit/d89a1b1ae3) [#47335](https://github.com/sgl-project/sglang/pull/47335)
  [Test] managers: Check output_ids in the router grouping test (#47335)
  _Files: `test/registered/unit/managers/test_multi_tokenizer_mixin.py`_
- **2026-10-29** [`46008a7afc`](https://github.com/sgl-project/sglang/commit/46008a7afc) [#47169](https://github.com/sgl-project/sglang/pull/47169)
  [Feat] rust-server: Report the model's launch-time fields in /model_info (#47169)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/rust_server/config.py`, `python/sglang/srt/utils/common.py`, `rust/sglang-server/src/api_server/grpc/info.rs` _+7 more__
- **2026-10-29** [`8705d359b9`](https://github.com/sgl-project/sglang/commit/8705d359b9) [#46968](https://github.com/sgl-project/sglang/pull/46968)
  [Feat] rust-server: Serve /start_profile and /stop_profile (#46968)
  _Files: `rust/sglang-server/src/api_server/handlers.rs`, `rust/sglang-server/src/api_server/handlers/control.rs`, `rust/sglang-server/src/api_server/http/info.rs`, `rust/sglang-server/src/message/io_struct.rs` _+3 more__
- **2026-10-29** [`2d44b55010`](https://github.com/sgl-project/sglang/commit/2d44b55010) [#46625](https://github.com/sgl-project/sglang/pull/46625)
  [Fix] kernel-plugins: Serve the MSA plugin behind --enable-nvidia-megakernel (#46625)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/argparse_actions.py`, `python/sglang/srt/arg_groups/fields/exec_.py`, `python/sglang/srt/arg_groups/pipeline.py` _+8 more__
- **2026-10-28** [`f5c23b4769`](https://github.com/sgl-project/sglang/commit/f5c23b4769) [#47114](https://github.com/sgl-project/sglang/pull/47114)
  [Fix] rust_server: Record startup-time metrics in Rust mode (#47114)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `test/registered/unit/entrypoints/test_rust_server_dp_ports.py`_
- **2026-10-28** [`54d2f65540`](https://github.com/sgl-project/sglang/commit/54d2f65540) [#47033](https://github.com/sgl-project/sglang/pull/47033)
  [Perf] dsv41: Read Engram rows in place by default for GPU tables over NVLink (#47033)
  _Files: `docs/docs/advanced_features/engram.mdx`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `python/sglang/srt/layers/engram.py`_
- **2026-10-28** [`5d8e90a0f9`](https://github.com/sgl-project/sglang/commit/5d8e90a0f9) [#47016](https://github.com/sgl-project/sglang/pull/47016)
  [Fix] rust-server: Read skip_special_tokens on the OpenAI routes and pin per-request detokenization (#47016)
  _Files: `rust/sglang-server/src/api_server/http/openai/chat.rs`, `rust/sglang-server/src/api_server/http/openai/completions.rs`, `rust/sglang-server/src/tokenizer_manager/detokenizer.rs`, `rust/sglang-server/testdata/special_token_tokenizer.json`_
- **2026-10-28** [`db0dfc7228`](https://github.com/sgl-project/sglang/commit/db0dfc7228) [#46925](https://github.com/sgl-project/sglang/pull/46925)
  [Perf] dsv41: Reorder the Engram all-to-all output with a Triton kernel (#46925)
  _Files: `docs/docs/advanced_features/engram.mdx`, `python/sglang/kernels/ops/embeddings/__init__.py`, `python/sglang/kernels/ops/embeddings/engram_gather.py`, `python/sglang/srt/layers/engram.py`_
- **2026-10-28** [`08b9ec6c1d`](https://github.com/sgl-project/sglang/commit/08b9ec6c1d) [#46197](https://github.com/sgl-project/sglang/pull/46197)
  [Perf] [NVIDIA] custom-all-reduce: Enable 2shot_push in SM107 TP4/TP8/TP16 heuristic (#46197)
  _Files: `python/sglang/srt/distributed/device_communicators/configs/custom_all_reduce_v2.py`, `test/registered/kernels/ops/communication/test_custom_all_reduce.py`_
- **2026-10-28** [`e35b5bc429`](https://github.com/sgl-project/sglang/commit/e35b5bc429) [#46917](https://github.com/sgl-project/sglang/pull/46917)
  [Perf] dsv41: Pick the Engram DP lookup collective automatically (#46917)
  _Files: `docs/docs/advanced_features/engram.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/arg_groups/engram_config.py` _+2 more__
- **2026-10-28** [`b7209cf534`](https://github.com/sgl-project/sglang/commit/b7209cf534) [#46635](https://github.com/sgl-project/sglang/pull/46635)
  [Feat] rust_server: Run --sidecar once per node (#46635)
  _Files: `python/sglang/srt/arg_groups/fields/serving.py`, `python/sglang/srt/arg_groups/serving_hook.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py` _+2 more__
- **2026-10-27** [`655059819c`](https://github.com/sgl-project/sglang/commit/655059819c) [#46896](https://github.com/sgl-project/sglang/pull/46896)
  [Fix] dsv41: Use `--attn-dp-size` in the Engram docs and restore env overrides on exceptions (#46896)
  _Files: `docs/docs/advanced_features/engram.mdx`, `python/sglang/srt/environ.py`_
- **2026-10-27** [`6be218a0f2`](https://github.com/sgl-project/sglang/commit/6be218a0f2) [#46879](https://github.com/sgl-project/sglang/pull/46879)
  [Fix] rust-server: Report the launched --tokenizer-path from the info endpoints (#46879)
  _Files: `python/sglang/srt/rust_server/config.py`, `rust/sglang-server/src/api_server/core/handle.rs`, `rust/sglang-server/src/api_server/http/info.rs`, `rust/sglang-server/src/message/config.rs` _+1 more__
- **2026-10-27** [`de26bb16a9`](https://github.com/sgl-project/sglang/commit/de26bb16a9) [#46853](https://github.com/sgl-project/sglang/pull/46853)
  [Fix] custom-all-reduce: Remove multi-node VMM allocator gate (#46853)
  _Files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `test/registered/unit/distributed/test_custom_all_reduce_v2_capability.py`_
- **2026-10-26** [`d4939cc267`](https://github.com/sgl-project/sglang/commit/d4939cc267) [#46553](https://github.com/sgl-project/sglang/pull/46553)
  [Refactor] bcg: Write the debug-mode forward's output buffer inside its eager break (#46553)
  _Files: `python/sglang/srt/model_executor/runner_backend/breakable_cuda_graph_backend.py`_
- **2026-10-26** [`5aeb6dfdb6`](https://github.com/sgl-project/sglang/commit/5aeb6dfdb6) [#46551](https://github.com/sgl-project/sglang/pull/46551)
  [Refactor] nemotron_h: Read the prefill shared expert's output from the caller's holder (#46551)
  _Files: `python/sglang/srt/models/nemotron_h.py`_
- **2026-10-26** [`5e420a1258`](https://github.com/sgl-project/sglang/commit/5e420a1258) [#46543](https://github.com/sgl-project/sglang/pull/46543)
  [Refactor] qwen4: Write QSA top-k and PLE batch breaks into caller-held outputs (#46543)
  _Files: `python/sglang/srt/models/qwen4_exp.py`, `test/registered/cuda_graph/breakable/test_breakable_cuda_graph.py`, `test/registered/unit/cp/test_qsa_cp_unit.py`, `test/registered/unit/model_executor/test_prefill_cuda_graph_runner_helpers.py`_
- **2026-10-26** [`52a6f7049f`](https://github.com/sgl-project/sglang/commit/52a6f7049f) [#46530](https://github.com/sgl-project/sglang/pull/46530)
  [Refactor] dsv41: Write engram hash ids and embeddings into caller-allocated prefill graph outputs (#46530)
  _Files: `python/sglang/srt/layers/engram.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-26** [`3b058f28c2`](https://github.com/sgl-project/sglang/commit/3b058f28c2) [#45950](https://github.com/sgl-project/sglang/pull/45950)
  [Refactor] [NPU] communicator: remove redundant npu communicator (#45950)
  _Files: `python/sglang/srt/distributed/device_communicators/npu_communicator.py`, `python/sglang/srt/distributed/parallel_state.py`, `test/registered/unit/distributed/test_parallel_state.py`_
- **2026-10-26** [`fef058a403`](https://github.com/sgl-project/sglang/commit/fef058a403) [#39774](https://github.com/sgl-project/sglang/pull/39774)
  [Test] [NPU] return-output-ids: Add e2e test for --return-output-ids parameter (#39774)
  _Files: `test/registered/npu/basic_function/api_related/test_npu_return_output_ids.py`_

## Scheduler / Batching  (26 commits)

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
- **2026-10-31** [`571ddad70f`](https://github.com/sgl-project/sglang/commit/571ddad70f) [#47159](https://github.com/sgl-project/sglang/pull/47159)
  [Feat] observability: Report a TTFT phase breakdown in response meta_info (#47159)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/observability/req_time_stats.py`_
- **2026-10-31** [`005b8e033f`](https://github.com/sgl-project/sglang/commit/005b8e033f) [#47546](https://github.com/sgl-project/sglang/pull/47546)
  [Fix] tokenizer_manager: Do not dispatch a request whose abort was already sent (#47546)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_request_class_override_points.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
- **2026-10-31** [`ba78bce729`](https://github.com/sgl-project/sglang/commit/ba78bce729) [#47321](https://github.com/sgl-project/sglang/pull/47321)
  [Fix] rust-server: End an /abort_request-ed request on the scheduler's abort finish reason, as Python does (#47321)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/rust_server/server.py` _+26 more__
- **2026-10-31** [`e9c18259c7`](https://github.com/sgl-project/sglang/commit/e9c18259c7) [#47545](https://github.com/sgl-project/sglang/pull/47545)
  [Fix] request_logger: Redact client watermark keys in request logs when watermarking is off (#47545)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/observability/request_metrics_exporter.py`, `python/sglang/srt/sampling/watermarking/README.md`, `python/sglang/srt/utils/request_logger.py` _+3 more__
- **2026-10-30** [`7146002be8`](https://github.com/sgl-project/sglang/commit/7146002be8) [#43897](https://github.com/sgl-project/sglang/pull/43897)
  [Refactor] scheduler: Finish queue-popped aborts in place (#43897)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_timeouts.py`_
- **2026-10-30** [`dfade835a6`](https://github.com/sgl-project/sglang/commit/dfade835a6) [#47113](https://github.com/sgl-project/sglang/pull/47113)
  [Fix] rust-server: Fix the metrics flush race and the default-priority label (#47113)
  _Files: `rust/sglang-server/src/api_server/core/metrics.rs`, `rust/sglang-server/src/api_server/handlers/generate.rs`, `rust/sglang-server/src/api_server/handlers/handle.rs`, `rust/sglang-server/src/multi_modality/worker.rs` _+3 more__
- **2026-10-30** [`75a5da7fb9`](https://github.com/sgl-project/sglang/commit/75a5da7fb9) [#47087](https://github.com/sgl-project/sglang/pull/47087)
  [Feat] RL: Hash raw received weights by name in check_weights (#47087)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler_components/weight_updater.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/utils/weight_checker.py` _+4 more__
- **2026-10-30** [`2271894884`](https://github.com/sgl-project/sglang/commit/2271894884) [#45496](https://github.com/sgl-project/sglang/pull/45496)
  [Fix] data_parallel_controller: Fix active ranks update and simplify round-robin dispatch (#45496)
  _Files: `python/sglang/srt/managers/data_parallel_controller.py`, `test/registered/unit/managers/test_data_parallel_controller.py`_
- **2026-10-29** [`add6f6d093`](https://github.com/sgl-project/sglang/commit/add6f6d093) [#47338](https://github.com/sgl-project/sglang/pull/47338)
  [Refactor] detokenizer: Move the incremental decode state and step into incremental_detokenize.py (#47338)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/incremental_detokenize.py` _+1 more__
- **2026-10-29** [`f5f79c5c18`](https://github.com/sgl-project/sglang/commit/f5f79c5c18) [#47178](https://github.com/sgl-project/sglang/pull/47178)
  [Perf] scheduler: Send the per-request output stats only when they may have changed (#47178)
  _Files: `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/schedule_batch.py` _+10 more__
- **2026-10-29** [`f18d5e6c19`](https://github.com/sgl-project/sglang/commit/f18d5e6c19) [#47107](https://github.com/sgl-project/sglang/pull/47107)
  [Refactor] tokenizer_manager: Move the crash-dump writer into a utils module (#47107)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/utils/crash_dump.py`, `test/registered/unit/utils/test_crash_dump.py`_
- **2026-10-29** [`1b16e2aa6a`](https://github.com/sgl-project/sglang/commit/1b16e2aa6a) [#47072](https://github.com/sgl-project/sglang/pull/47072)
  [Feat] scheduler: Add typed per-token and per-request customized_info values (#47072)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/model_executor/model_runner.py`, `test/registered/unit/managers/test_batch_result_processor_hidden_states.py` _+1 more__
- **2026-10-29** [`68e57f4005`](https://github.com/sgl-project/sglang/commit/68e57f4005) [#47116](https://github.com/sgl-project/sglang/pull/47116)
  [Fix] usage: Clamp reasoning tokens after stop truncation (#47116)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `test/registered/unit/managers/test_output_streamer_logprobs.py`_
- **2026-10-29** [`16a4337813`](https://github.com/sgl-project/sglang/commit/16a4337813) [#46027](https://github.com/sgl-project/sglang/pull/46027)
  [Fix] pp: Post the first rank's output recv after its own forward (#46027)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `test/registered/unit/managers/test_pp_output_exchange_order.py`_
- **2026-10-29** [`4c14e67c5f`](https://github.com/sgl-project/sglang/commit/4c14e67c5f) [#47166](https://github.com/sgl-project/sglang/pull/47166)
  [Perf] observability: Send scheduler timing to the tokenizer as typed reports (#47166)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+7 more__
- **2026-10-28** [`c6c7533957`](https://github.com/sgl-project/sglang/commit/c6c7533957) [#46159](https://github.com/sgl-project/sglang/pull/46159)
  [Perf] batch-invariant: Fused residual add + RMSNorm kernel (#46159)
  _Files: `python/sglang/srt/batch_invariant_ops/__init__.py`, `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/layers/layernorm.py`, `test/registered/unit/batch_invariant_ops/test_fused_add_rms_norm_batch_invariant.py`_
- **2026-10-28** [`1e7e19285d`](https://github.com/sgl-project/sglang/commit/1e7e19285d) [#44045](https://github.com/sgl-project/sglang/pull/44045)
  [Perf] [AMD] batch-invariant: Tune the bf16 matmul for gfx950 (#44045)
  _Files: `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `test/registered/unit/batch_invariant_ops/test_matmul_persistent_configs.py`_
- **2026-10-28** [`54be2010d3`](https://github.com/sgl-project/sglang/commit/54be2010d3) [#46812](https://github.com/sgl-project/sglang/pull/46812)
  [Perf] scheduler: Refresh PD prefill bootstrap-queue prefixes in the waiting-prefix LRU pass (#46812)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_held_row_admission.py`_
- **2026-10-28** [`6a473b2ac7`](https://github.com/sgl-project/sglang/commit/6a473b2ac7) [#46513](https://github.com/sgl-project/sglang/pull/46513)
  [Fix] rust-server: End a native /generate stream on a scheduler abort frame, as Python does (#46513)
  _Files: `rust/sglang-server/src/api_server/core/error.rs`, `rust/sglang-server/src/api_server/core/handle.rs`, `rust/sglang-server/src/api_server/grpc/native_api.rs`, `rust/sglang-server/src/api_server/http/native_api.rs` _+1 more__
- **2026-10-27** [`40ba5020db`](https://github.com/sgl-project/sglang/commit/40ba5020db) [#45445](https://github.com/sgl-project/sglang/pull/45445)
  [Fix] http_server: Make SageMaker /ping reflect server readiness (#45445)
  _Files: `docs/docs/basic_usage/aws_sagemaker.mdx`, `docs/docs/basic_usage/native_api.mdx`, `examples/checkpoint_engine/update.py`, `python/sglang/srt/checkpoint_engine/update.py` _+4 more__
- **2026-10-26** [`911693e3f8`](https://github.com/sgl-project/sglang/commit/911693e3f8) [#45449](https://github.com/sgl-project/sglang/pull/45449)
  [Feat] rust-server: Render, tokenize and serve chat through sglang-processor (#45449)
  _Files: `python/sglang/srt/rust_server/config.py`, `rust/Cargo.lock`, `rust/sglang-processor/src/lib.rs`, `rust/sglang-processor/src/openai/chat.rs` _+40 more__
- **2026-10-26** [`3a62cdfb3d`](https://github.com/sgl-project/sglang/commit/3a62cdfb3d) [#45923](https://github.com/sgl-project/sglang/pull/45923)
  [Fix] scheduler: Make a Req's "__req__" self-reference weak (#45923)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_req_custom_params_ref.py`_

## Triton / Kernels  (25 commits)

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
- **2026-11-01** [`6dda2f02f7`](https://github.com/sgl-project/sglang/commit/6dda2f02f7) [#47736](https://github.com/sgl-project/sglang/pull/47736)
  [Fix] tests: Initialize DCP replay backend capability (#47736)
  _Files: `test/registered/unit/model_executor/test_prefill_cuda_graph_dcp.py`_
- **2026-11-01** [`fa5580f6d0`](https://github.com/sgl-project/sglang/commit/fa5580f6d0) [#47619](https://github.com/sgl-project/sglang/pull/47619)
  [CI] ci: Re-tier CUDA tests across base, extra, nightly, and weekly by importance (#47619)
- **2026-10-31** [`3908210311`](https://github.com/sgl-project/sglang/commit/3908210311) [#47452](https://github.com/sgl-project/sglang/pull/47452)
  [Perf] kimi-k3: Allow residual bank shards with NCCL (#47452)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/layer_boundary/residual/attn_bank.py`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/layer_boundary/test_attn_bank_residual_ops.py` _+1 more__
- **2026-10-31** [`c0f710f7dc`](https://github.com/sgl-project/sglang/commit/c0f710f7dc) [#44168](https://github.com/sgl-project/sglang/pull/44168)
  [Perf] [NVIDIA] sampling: Enable Cake softmax on SM100 (#44168)
  _Files: `python/sglang/kernels/cake_kernels/README.md`, `python/sglang/kernels/cake_kernels/sampling.py`, `python/sglang/kernels/ops/sampling/__init__.py`, `test/registered/kernels/ops/sampling/test_temperature_softmax.py` _+1 more__
- **2026-10-31** [`07a85353d6`](https://github.com/sgl-project/sglang/commit/07a85353d6) [#47646](https://github.com/sgl-project/sglang/pull/47646)
  [Fix] kernels/jit: Correct the PDLTriggerSecondary comment on what griddepcontrol.wait covers (#47646)
  _Files: `python/sglang/kernels/jit/include/sgl_kernel/utils.cuh`_
- **2026-10-30** [`be556ff0e9`](https://github.com/sgl-project/sglang/commit/be556ff0e9) [#47295](https://github.com/sgl-project/sglang/pull/47295)
  [Perf] cuda-graph: Upload each deduplicated executable on a private stream before its first launch (#47295)
  _Files: `python/sglang/srt/model_executor/runner_backend/cuda_graph_dedup_mixin.py`, `test/registered/unit/model_executor/runner_backend/test_cuda_graph_dedup.py`_
- **2026-10-30** [`47783adde0`](https://github.com/sgl-project/sglang/commit/47783adde0) [#46721](https://github.com/sgl-project/sglang/pull/46721)
  [Test] cuda-graph: Add a standalone CUDA-graph lifetime validation tool and its skill (#46721)
  _Files: `.agents/skills/sglang-multi-graph-check/SKILL.md`, `.agents/skills/sglang-multi-graph-check/references/cli.md`, `python/sglang/test/cuda_graph_lifetime/__init__.py`, `python/sglang/test/cuda_graph_lifetime/__main__.py` _+6 more__
- **2026-10-29** [`0580e941ef`](https://github.com/sgl-project/sglang/commit/0580e941ef) [#47034](https://github.com/sgl-project/sglang/pull/47034)
  [Feat] [MUSA] breakable: Support portable capture status (#47034)
  _Files: `python/sglang/srt/model_executor/runner_backend_utils/breakable_cuda_graph/breakable_cuda_graph.py`, `test/registered/unit/model_executor/runner/test_breakable_capture_status.py`_
- **2026-10-29** [`f664962783`](https://github.com/sgl-project/sglang/commit/f664962783) [#47217](https://github.com/sgl-project/sglang/pull/47217)
  [Fix] [NPU] docker: Bump SGLANG_KERNEL_NPU_TAG to 2026.9.0.post12 (#47217)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `docker/npu.Dockerfile`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-10-29** [`f3bc7a1c1b`](https://github.com/sgl-project/sglang/commit/f3bc7a1c1b) [#46737](https://github.com/sgl-project/sglang/pull/46737)
  [Fix] cuda_graph: Release base storage held by empty break inputs (#46737)
  _Files: `python/sglang/srt/model_executor/runner_backend_utils/breakable_cuda_graph/breakable_cuda_graph.py`, `test/registered/cuda_graph/breakable/test_empty_view_capture.py`_
- **2026-10-28** [`8d11638cd5`](https://github.com/sgl-project/sglang/commit/8d11638cd5) [#47145](https://github.com/sgl-project/sglang/pull/47145)
  [Fix] docker: update NVIDIA megakernel pin to tested commit (#47145)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cu134`_
- **2026-10-28** [`1825a09dbb`](https://github.com/sgl-project/sglang/commit/1825a09dbb) [#46955](https://github.com/sgl-project/sglang/pull/46955)
  [Perf] dsv41: Use the Engram all-to-all lookup for decode and CUDA graphs (#46955)
  _Files: `docs/docs/advanced_features/engram.mdx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/layers/engram.py`_
- **2026-10-28** [`e1b6d7581e`](https://github.com/sgl-project/sglang/commit/e1b6d7581e) [#47105](https://github.com/sgl-project/sglang/pull/47105)
  [Feat] [NVIDIA] runtime: Add a master switch for megakernel runtime optimizations (#47105)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `test/registered/unit/test_environ.py`_
- **2026-10-27** [`37e9bdb7a7`](https://github.com/sgl-project/sglang/commit/37e9bdb7a7) [#46863](https://github.com/sgl-project/sglang/pull/46863)
  [Feat] jit: Split a header-only module's kernel instantiations across parallel translation units (#46863)
  _Files: `python/sglang/kernels/jit/utils/compile/loader.py`, `python/sglang/kernels/jit/utils/compile/spec.py`, `test/registered/unit/kernels/test_jit_cache.py`_
- **2026-10-27** [`922e595a94`](https://github.com/sgl-project/sglang/commit/922e595a94) [#45858](https://github.com/sgl-project/sglang/pull/45858)
  [Chore] [NVIDIA] docker: Update to torch 2.15rc1 in CUDA 13.4 container (#45858)
  _Files: `docker/Dockerfile.cu134`_
- **2026-10-27** [`cc96d552c3`](https://github.com/sgl-project/sglang/commit/cc96d552c3) [#43989](https://github.com/sgl-project/sglang/pull/43989)
  [Feat] [Intel] docker/xpu: Upgrade oneAPI to 2026.1.3 and sglang-kernel-xpu to 0.5.0 (#43989)
  _Files: `docker/xpu.Dockerfile`, `python/pyproject_xpu.toml`_
- **2026-10-27** [`5025cbf7d4`](https://github.com/sgl-project/sglang/commit/5025cbf7d4) [#46658](https://github.com/sgl-project/sglang/pull/46658)
  [Fix] elementwise: Avoid data-dependent token-count guards in sigmoid-mul launchers (#46658)
  _Files: `python/sglang/kernels/ops/elementwise/elementwise.py`_
- **2026-10-27** [`ee5443f530`](https://github.com/sgl-project/sglang/commit/ee5443f530) [#43720](https://github.com/sgl-project/sglang/pull/43720)
  [Perf] async-probe: Fuse asynchronous NaN validation into one kernel (#43720)
  _Files: `python/sglang/srt/utils/async_probe.py`_
- **2026-10-26** [`e1c4b273af`](https://github.com/sgl-project/sglang/commit/e1c4b273af) [#46546](https://github.com/sgl-project/sglang/pull/46546)
  [Doc] cookbook: MiniMax-M3.1 GB200 recipes and B200 Low-Latency (MonoKernel) (#46546)
  _Files: `docs/cookbook/autoregressive/MiniMax/MiniMax-M3.1.mdx`, `docs/src/snippets/configs/MiniMaxAI/minimax-m3.1.jsx`_

## CI / Build  (19 commits)

- **2026-11-02** [`c04bae2b3f`](https://github.com/sgl-project/sglang/commit/c04bae2b3f) [#44967](https://github.com/sgl-project/sglang/pull/44967)
  [Test] [NPU] kimi_k3: add 128k prefill/decode perf acceptance cases on 4-node mix (#44967)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/gen_dataset_fixed_len.py`, `python/sglang/test/ascend/e2e/run_aisbench.sh`, `python/sglang/test/ascend/e2e/test_npu_performance_utils.py` _+2 more__
- **2026-11-02** [`af5731cca6`](https://github.com/sgl-project/sglang/commit/af5731cca6) [#47823](https://github.com/sgl-project/sglang/pull/47823)
  [CI] [NPU] workflow: Gate pr-test-npu-finish on pr-gate and drop nightly PR trigger (#47823)
  _Files: `.github/workflows/nightly-test-npu.yml`, `.github/workflows/pr-test-npu.yml`_
- **2026-11-02** [`e1e0f4ab8c`](https://github.com/sgl-project/sglang/commit/e1e0f4ab8c) [#47611](https://github.com/sgl-project/sglang/pull/47611)
  [Test] [Ascend] npu: Add GLM-5.2 2P2D gpqa cases and unify evalscope retry loop (#47611)
  _Files: `.github/workflows/nightly-test-npu.yml`, `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_dcp_gpqa.py`, `test/registered/npu/accuracy/glm5_2/test_npu_glm_5_2_w8a8_2p2d_32p_pcp_gpqa.py`_
- **2026-11-01** [`4eba700ea4`](https://github.com/sgl-project/sglang/commit/4eba700ea4) [#47563](https://github.com/sgl-project/sglang/pull/47563)
  [CI] health: Retry transient GitHub API failures (#47563)
  _Files: `.github/actions/check-pr-test-health/action.yml`_
- **2026-10-31** [`fbf9ba4b93`](https://github.com/sgl-project/sglang/commit/fbf9ba4b93) [#47592](https://github.com/sgl-project/sglang/pull/47592)
  [CI] ci: Preload `sglang.test.test_utils` in CPU fork workers (#47592)
  _Files: `.github/workflows/_pr-test-stage-cpu.yml`, `python/sglang/test/ci/ci_utils.py`, `python/sglang/test/ci/fork_test_worker.py`, `test/run_suite.py`_
- **2026-10-31** [`98a7f7e175`](https://github.com/sgl-project/sglang/commit/98a7f7e175) [#47522](https://github.com/sgl-project/sglang/pull/47522)
  [CI] codespell: Ignore miniTE blog name (#47522)
  _Files: `.codespellrc`_
- **2026-10-30** [`17e94c4677`](https://github.com/sgl-project/sglang/commit/17e94c4677) [#46394](https://github.com/sgl-project/sglang/pull/46394)
  [CI] [Intel] ci/xpu: Rename rolling Docker tag and add release-cut results CSV (#46394)
  _Files: `.github/workflows/nightly-test-intel-wheel.yml`, `.github/workflows/nightly-test-intel.yml`, `.github/workflows/release-docker-intel-xpu-nightly.yml`_
- **2026-10-30** [`3588dcf050`](https://github.com/sgl-project/sglang/commit/3588dcf050) [#47365](https://github.com/sgl-project/sglang/pull/47365)
  [CI] [NPU] coverage: Refresh the coverage baseline every 2 days and raise the publish gate to 40% (#47365)
  _Files: `.github/workflows/coverage-collection-npu.yml`, `.github/workflows/pr-test-npu.yml`_
- **2026-10-30** [`52604e1d46`](https://github.com/sgl-project/sglang/commit/52604e1d46) [#47208](https://github.com/sgl-project/sglang/pull/47208)
  [CI] [PPU] slash-command: Register PPU with shared opt-in CI tiers (#47208)
  _Files: `.agents/skills/ci-workflow-guide/SKILL.md`, `.github/FOLDER_README.md`, `.github/workflows/pr-test-ppu.yml`, `docs/docs/developer_guide/contribution_guide.mdx` _+1 more__
- **2026-10-29** [`5007cbd6a5`](https://github.com/sgl-project/sglang/commit/5007cbd6a5) [#47246](https://github.com/sgl-project/sglang/pull/47246)
  [CI] slash-command: Write the /run-cpu-ci result back to its reply comment (#47246)
  _Files: `.agents/skills/ci-workflow-guide/SKILL.md`, `.github/workflows/run-cpu-ci.yml`, `docs/docs/developer_guide/contribution_guide.mdx`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-10-29** [`4a4e887bab`](https://github.com/sgl-project/sglang/commit/4a4e887bab) [#47134](https://github.com/sgl-project/sglang/pull/47134)
  [CI] chore: add CI permissions for chenxb002 (#47134)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-10-29** [`32a1c720e1`](https://github.com/sgl-project/sglang/commit/32a1c720e1) [#47133](https://github.com/sgl-project/sglang/pull/47133)
  [CI] chore: add CI permissions for Vinsmoke86 (#47133)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-10-28** [`de9f481316`](https://github.com/sgl-project/sglang/commit/de9f481316) [#46993](https://github.com/sgl-project/sglang/pull/46993)
  [CI] [NPU] pr-test-npu: Auto-publish coverage baseline with an NPU coverage gate (#46993)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-10-28** [`a1966e1b5d`](https://github.com/sgl-project/sglang/commit/a1966e1b5d) [#45385](https://github.com/sgl-project/sglang/pull/45385)
  [CI] [MLU] slash-command: Register MLU with shared opt-in CI tiers (#45385)
  _Files: `.agents/skills/ci-workflow-guide/SKILL.md`, `.github/FOLDER_README.md`, `.github/workflows/pr-test-mlu.yml`, `docs/docs/developer_guide/contribution_guide.mdx` _+2 more__
- **2026-10-27** [`635430d073`](https://github.com/sgl-project/sglang/commit/635430d073) [#46844](https://github.com/sgl-project/sglang/pull/46844)
  [CI] [NPU] precise-test: skip suites that register no PR test (#46844)
  _Files: `scripts/ci/npu/precise-test/bucket_recommended_tests.py`_
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

## Other  (19 commits)

- **2026-11-02** [`3f0051eec7`](https://github.com/sgl-project/sglang/commit/3f0051eec7) [#47858](https://github.com/sgl-project/sglang/pull/47858)
  [Fix] graph: Restore XPU logger and Inkling backend mock dtype (#47858)
- **2026-11-02** [`26fde018e5`](https://github.com/sgl-project/sglang/commit/26fde018e5) [#47875](https://github.com/sgl-project/sglang/pull/47875)
  [Chore] owner: update (#47875)
  _Files: `.github/CODEOWNERS`_
- **2026-11-02** [`ea2fda7fd2`](https://github.com/sgl-project/sglang/commit/ea2fda7fd2) [#44494](https://github.com/sgl-project/sglang/pull/44494)
  [Fix] metrics: Handle CPU monitor clock resets after restore (#44494)
  _Files: `python/sglang/srt/observability/cpu_monitor.py`, `test/registered/unit/observability/test_cpu_monitor.py`_
- **2026-11-01** [`1457851e7e`](https://github.com/sgl-project/sglang/commit/1457851e7e) [#47196](https://github.com/sgl-project/sglang/pull/47196)
  [Feat] model: support Unlimited-OCR v2 (#47196)
- **2026-10-31** [`800de62d7c`](https://github.com/sgl-project/sglang/commit/800de62d7c) [#47337](https://github.com/sgl-project/sglang/pull/47337)
  [Fix] model_loader: Neutral UE8M0 block scales for dummy weights (#47337)
  _Files: `python/sglang/srt/model_loader/weight_utils.py`, `test/registered/unit/model_loader/test_weight_utils.py`_
- **2026-10-31** [`d2cf2371b0`](https://github.com/sgl-project/sglang/commit/d2cf2371b0) [#45302](https://github.com/sgl-project/sglang/pull/45302)
  [Fix] [NPU] DSA: Correct DSA Models Sparse offload index-cache budgeting (#45302)
  _Files: `python/sglang/srt/hardware_backend/npu/sparsity_driven_kv_offload/config.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/npu/test_sparsity_driven_kv_offload_config.py`_
- **2026-10-30** [`6441f6ba8d`](https://github.com/sgl-project/sglang/commit/6441f6ba8d) [#47353](https://github.com/sgl-project/sglang/pull/47353)
  [Feat] fpm: Retain captured intervals and support multiple FpmTiming listeners (#47353)
  _Files: `python/sglang/srt/observability/forward_pass_metrics.py`, `test/registered/unit/observability/test_forward_pass_metrics.py`_
- **2026-10-30** [`f3c9f0a5ab`](https://github.com/sgl-project/sglang/commit/f3c9f0a5ab) [#47084](https://github.com/sgl-project/sglang/pull/47084)
  [Fix] environ: Register the batch-invariant matmul fallback flag in Envs (#47084)
  _Files: `python/sglang/srt/environ.py`_
- **2026-10-30** [`9f0beaa43b`](https://github.com/sgl-project/sglang/commit/9f0beaa43b) [#47216](https://github.com/sgl-project/sglang/pull/47216)
  [Fix] [NPU] dspark: Avoid double-counting verify KV lengths in graph replay (#47216)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`_
- **2026-10-30** [`f00cd37b46`](https://github.com/sgl-project/sglang/commit/f00cd37b46) [#47300](https://github.com/sgl-project/sglang/pull/47300)
  [Fix] TensorMatcher: keep symbol device/dtype options; use kDLGPU aliases (#47300)
- **2026-10-28** [`88fea372d4`](https://github.com/sgl-project/sglang/commit/88fea372d4) [#47146](https://github.com/sgl-project/sglang/pull/47146)
  [Fix] dsv4: Capture the replay tail thread-locally while serving (#47146)
  _Files: `python/sglang/srt/model_executor/runner/row_bucket_graph_runner.py`_
- **2026-10-28** [`59af99a873`](https://github.com/sgl-project/sglang/commit/59af99a873) [#47008](https://github.com/sgl-project/sglang/pull/47008)
  [Perf] sglang-api-types: Decode flat id lists directly instead of buffering them as Values (#47008)
  _Files: `rust/sglang-api-codegen/src/emit.rs`, `rust/sglang-api-types/src/generated/sglang.api.v1.serde.rs`, `rust/sglang-api-types/tests/json_contract.rs`_
- **2026-10-28** [`ca8184e13a`](https://github.com/sgl-project/sglang/commit/ca8184e13a) [#46987](https://github.com/sgl-project/sglang/pull/46987)
  [Refactor] kv-cache: Separate byte storage from allocation identities (#46987)
- **2026-10-28** [`3854993c88`](https://github.com/sgl-project/sglang/commit/3854993c88) [#46821](https://github.com/sgl-project/sglang/pull/46821)
  [Test] HiCache: Don't require a storage hit in the random-failure test (#46821)
  _Files: `test/registered/hicache/test_hicache_storage_file_backend.py`_
- **2026-10-27** [`4549937519`](https://github.com/sgl-project/sglang/commit/4549937519) [#44487](https://github.com/sgl-project/sglang/pull/44487)
  [Fix] nemotron: Preserve nested Puzzle configs (#44487)
  _Files: `python/sglang/srt/configs/nano_nemotron_vl.py`, `test/registered/unit/configs/test_nano_nemotron_vl_config.py`_
- **2026-10-27** [`302d5e7b8c`](https://github.com/sgl-project/sglang/commit/302d5e7b8c) [#45516](https://github.com/sgl-project/sglang/pull/45516)
  [Fix] [CPU] memory: budget overestimation caused by filtering empty NUMA nodes (#45516)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-10-26** [`5a1f174700`](https://github.com/sgl-project/sglang/commit/5a1f174700) [#46640](https://github.com/sgl-project/sglang/pull/46640)
  [Fix] utils: Fix CPU engine detection under torch.compile fullgraph (#46640)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-10-26** [`c23f1ccce1`](https://github.com/sgl-project/sglang/commit/c23f1ccce1) [#46570](https://github.com/sgl-project/sglang/pull/46570)
  [Test] hicache: Accept session_ids in the L3 object-layout test's put stubs (#46570)
  _Files: `test/registered/hicache/test_hicache_l3_object_layout.py`_
- **2026-10-26** [`3ab4b62b0c`](https://github.com/sgl-project/sglang/commit/3ab4b62b0c) [#39772](https://github.com/sgl-project/sglang/pull/39772)
  [Test] [NPU] return-input-ids: Add e2e test for --return-input-ids parameter (#39772)
  _Files: `test/registered/npu/basic_function/api_related/test_npu_return_input_ids.py`_

## Quantization  (16 commits)

- **2026-11-02** [`fbb847bed6`](https://github.com/sgl-project/sglang/commit/fbb847bed6) [#47503](https://github.com/sgl-project/sglang/pull/47503)
  [Perf] rmsnorm: One SM100-tuned JIT template for plain, fused residual-add and fp8 per-tensor quant (#47503)
  _Files: `python/sglang/kernels/jit/csrc/elementwise/fused_add_rmsnorm.cuh`, `python/sglang/kernels/jit/csrc/elementwise/rmsnorm.cuh`, `python/sglang/kernels/jit/csrc/elementwise/rmsnorm_hf.cuh`, `python/sglang/kernels/ops/layernorm/__init__.py` _+10 more__
- **2026-11-02** [`33c8d723a1`](https://github.com/sgl-project/sglang/commit/33c8d723a1) [#43194](https://github.com/sgl-project/sglang/pull/43194)
  [Fix] diffusion: fix cosmos3 Bugs (#43194)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos_dreams.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos_dreams_transfer.py` _+9 more__
- **2026-10-31** [`01fde5cb62`](https://github.com/sgl-project/sglang/commit/01fde5cb62) [#47150](https://github.com/sgl-project/sglang/pull/47150)
  [CI] [AMD] pr-test: Run the MI35x 1-GPU stage as one job; move two e2e tests to nightly (#47150)
  _Files: `test/registered/e2e/quantization/test_quark_mxfp4.py`_
- **2026-10-30** [`5628058714`](https://github.com/sgl-project/sglang/commit/5628058714) [#47331](https://github.com/sgl-project/sglang/pull/47331)
  [Doc] [AMD] cookbook: Add DCP4 to the GLM-5.2 MI355X MXFP4 high-throughput recipe (#47331)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-10-30** [`93f4f1a87d`](https://github.com/sgl-project/sglang/commit/93f4f1a87d) [#47152](https://github.com/sgl-project/sglang/pull/47152)
  [CI] [AMD] pr-test: Move the Kimi-K2.5 MXFP4 BCG test to nightly (#47152)
  _Files: `test/registered/amd/test_kimi_k25_mxfp4_bcg_mi35x.py`_
- **2026-10-30** [`96c296b3e8`](https://github.com/sgl-project/sglang/commit/96c296b3e8) [#47054](https://github.com/sgl-project/sglang/pull/47054)
  [Test] [AMD] fp8-grid: Compare the GEMM to aiter within one bf16 rounding, not bitwise (#47054)
  _Files: `test/registered/kernels/ops/quantization/test_fp8_grid_producers_gfx95.py`_
- **2026-10-30** [`16a3bf3d9d`](https://github.com/sgl-project/sglang/commit/16a3bf3d9d) [#46800](https://github.com/sgl-project/sglang/pull/46800)
  [Fix] [AMD] quark: Keep MXFP8 shared experts out of the MXFP4 fused slot on dense-first models (#46800)
  _Files: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/minimax_m3.py`, `python/sglang/srt/models/minimax_m3_vl.py`, `test/registered/unit/layers/quantization/test_quark_config.py` _+1 more__
- **2026-10-29** [`302b78ccf0`](https://github.com/sgl-project/sglang/commit/302b78ccf0) [#46024](https://github.com/sgl-project/sglang/pull/46024)
  [Perf] mhc: Split hc_combine_norm_mxfp8 rows by batch size and zero padding scales in the kernel (#46024)
  _Files: `python/sglang/kernels/ops/layernorm/hc_combine_norm.py`, `test/registered/kernels/ops/layernorm/test_mxfp8_epilogue.py`_
- **2026-10-29** [`1776e2dcf8`](https://github.com/sgl-project/sglang/commit/1776e2dcf8) [#47163](https://github.com/sgl-project/sglang/pull/47163)
  [Fix] [AMD] docker: Remove implicit INT8 QuickReduce default as it causes accuracy issues in 800k+ long context evals (#47163)
  _Files: `docker/rocm.Dockerfile`_
- **2026-10-29** [`b960aa903a`](https://github.com/sgl-project/sglang/commit/b960aa903a) [#46770](https://github.com/sgl-project/sglang/pull/46770)
  [Fix] sgl-kernel: bump sgl-attn to pick up FP8 two-level accumulation (#46770)
  _Files: `python/sglang/kernels/aot/CMakeLists.txt`_
- **2026-10-28** [`45252c64ca`](https://github.com/sgl-project/sglang/commit/45252c64ca) [#46757](https://github.com/sgl-project/sglang/pull/46757)
  [Doc] [AMD] cookbook: Add the Qwen3.5 MI355X FP8 agentic recipe covering the GPU-resident and HiCache bands (#46757)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`_
- **2026-10-27** [`3145c7ae66`](https://github.com/sgl-project/sglang/commit/3145c7ae66) [#43839](https://github.com/sgl-project/sglang/pull/43839)
  [Perf] [AMD] qwen3_5: Quantize the BF16 GDN projections to MXFP4 online (#43839)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py`, `python/sglang/srt/models/qwen3_5.py` _+1 more__
- **2026-10-27** [`a6f5bd397b`](https://github.com/sgl-project/sglang/commit/a6f5bd397b) [#43815](https://github.com/sgl-project/sglang/pull/43815)
  [Perf] [AMD] fp8: Use the AITER CK blockscale GEMM by default on gfx942 (#43815)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`_
- **2026-10-27** [`61a676125a`](https://github.com/sgl-project/sglang/commit/61a676125a) [#45877](https://github.com/sgl-project/sglang/pull/45877)
  [CI] [AMD] test: Skip Mistral-7B and Mixtral-8x7B FP8 in nightly GSM8K eval (#45877)
  _Files: `test/registered/amd/accuracy/mi30x/test_gsm8k_eval_amd.py`_
- **2026-10-26** [`01759f0a68`](https://github.com/sgl-project/sglang/commit/01759f0a68) [#39622](https://github.com/sgl-project/sglang/pull/39622)
  [Perf] [AMD] dsv4: fp8 target lm_head GEMM for DSPARK verify logits (#39622)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/dspark.py`_
- **2026-10-26** [`589d196bc3`](https://github.com/sgl-project/sglang/commit/589d196bc3) [#40435](https://github.com/sgl-project/sglang/pull/40435)
  [Fix] [NPU] requantization: gate arch35 block-FP8 -> MXFP8 requantization (#40435)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/quantization/w8a8_mxfp8.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`_

## Speculative Decoding  (12 commits)

- **2026-11-02** [`aa3e34aaeb`](https://github.com/sgl-project/sglang/commit/aa3e34aaeb) [#45406](https://github.com/sgl-project/sglang/pull/45406)
  [Feat] [NVIDIA] megakernels: Expose hybrid runtime and DSpark verification views (#45406)
  _Files: `python/sglang/kernels/plugin_kernels/nvidia/spec.py`, `python/sglang/srt/kernel_plugins/nvidia/binding.py`, `python/sglang/srt/model_executor/runner/base_runner.py`, `test/registered/unit/kernel_plugins/nvidia/test_eagle_binding.py` _+2 more__
- **2026-11-02** [`f96d5b1ca8`](https://github.com/sgl-project/sglang/commit/f96d5b1ca8) [#47173](https://github.com/sgl-project/sglang/pull/47173)
  [Refactor] [NPU] graph: Remove the NPU graph runner (#47173)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/multi_layer_eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py` _+16 more__
- **2026-10-30** [`a8d944f5e4`](https://github.com/sgl-project/sglang/commit/a8d944f5e4) [#47333](https://github.com/sgl-project/sglang/pull/47333)
  [Fix] Spec: Fall back to eager when the ragged-verify tier exceeds the captured grid (#47333)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_planner.py`, `test/registered/spec/dspark/test_dspark_scheduler.py`_
- **2026-10-30** [`9cf2bc8925`](https://github.com/sgl-project/sglang/commit/9cf2bc8925) [#47086](https://github.com/sgl-project/sglang/pull/47086)
  [Feat] kv-canary: Pass through canary info when the KV-canary is enabled (#47086)
  _Files: `python/sglang/kernels/jit/csrc/kv_canary/canary_info.cuh`, `python/sglang/kernels/jit/csrc/kv_canary/consts.cuh`, `python/sglang/kernels/ops/kv_canary/__init__.py`, `python/sglang/kernels/ops/kv_canary/canary_info.py` _+34 more__
- **2026-10-30** [`585bfe32a7`](https://github.com/sgl-project/sglang/commit/585bfe32a7) [#46278](https://github.com/sgl-project/sglang/pull/46278)
  [Feat] [NPU] dspark: Integrate native sampling and verification kernels (#46278)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_draft_model.py`, `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py`, `python/sglang/kernels/ops/speculative/dspark/markov_sample.py`, `test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py`_
- **2026-10-29** [`d71bf63fb5`](https://github.com/sgl-project/sglang/commit/d71bf63fb5) [#44200](https://github.com/sgl-project/sglang/pull/44200)
  [Feat] watermark: Add DSPARK speculative decoding support (#44200)
  _Files: `docs/docs/advanced_features/text_watermarking.mdx`, `python/sglang/srt/arg_groups/validation_hook.py`, `python/sglang/srt/sampling/watermarking/README.md`, `python/sglang/srt/sampling/watermarking/core.py` _+3 more__
- **2026-10-29** [`dfdee259c5`](https://github.com/sgl-project/sglang/commit/dfdee259c5) [#47249](https://github.com/sgl-project/sglang/pull/47249)
  [Refactor] scheduler: Drop the dead Req.decoded_text and BatchTokenIDOutput.decoded_texts (#47249)
  _Files: `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/schedule_batch.py` _+6 more__
- **2026-10-29** [`5696215168`](https://github.com/sgl-project/sglang/commit/5696215168) [#34038](https://github.com/sgl-project/sglang/pull/34038)
  [Refactor] Spec: Resolve the ragged-verify graph tier at a single point (#34038)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/speculative/dspark_components/dspark_planner.py`_
- **2026-10-29** [`bd1eb0bb89`](https://github.com/sgl-project/sglang/commit/bd1eb0bb89) [#44465](https://github.com/sgl-project/sglang/pull/44465)
  [Perf] [AMD] dsv41: Drop the per-step whole-vocab gather of draft logits via sharded accept (#44465)
  _Files: `python/sglang/kernels/ops/speculative/dspark/markov_sample.py`, `python/sglang/kernels/ops/speculative/dspark/sharded_accept_hip.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4_dspark.py` _+7 more__
- **2026-10-29** [`3a01d4cc8c`](https://github.com/sgl-project/sglang/commit/3a01d4cc8c) [#46840](https://github.com/sgl-project/sglang/pull/46840)
  [Fix] dspark: Keep the real verify accept cost under simulated acceptance (#46840)
  _Files: `python/sglang/kernels/ops/speculative/dspark/simulated_bonus.py`, `python/sglang/kernels/ops/speculative/dspark/static_accept_tail.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py` _+3 more__
- **2026-10-28** [`73fbf5ccd3`](https://github.com/sgl-project/sglang/commit/73fbf5ccd3) [#46639](https://github.com/sgl-project/sglang/pull/46639)
  [Perf] speculative: Rotate multi-layer EAGLE prefill input_ids 4096 ids per trip, not 8 (#46639)
  _Files: `python/sglang/kernels/ops/speculative/multi_layer_eagle.py`, `test/registered/kernels/ops/speculative/test_boundary_kv_fix_kernels.py`_
- **2026-10-27** [`24d55621a3`](https://github.com/sgl-project/sglang/commit/24d55621a3) [#46404](https://github.com/sgl-project/sglang/pull/46404)
  [Fix] dspark: Draw the simulated-acceptance bonus at the simulated row (#46404)
  _Files: `python/sglang/kernels/ops/speculative/dspark/static_accept_tail.py`, `python/sglang/srt/speculative/dspark_components/dspark_sampling_accept_graph.py`, `python/sglang/srt/speculative/dspark_components/dspark_verify.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py` _+2 more__

## Models  (8 commits)

- **2026-11-01** [`1367b51139`](https://github.com/sgl-project/sglang/commit/1367b51139) [#47601](https://github.com/sgl-project/sglang/pull/47601)
  [Test] model_loader: Cover unindexed Mistral shard filtering (#47601)
  _Files: `test/registered/unit/model_loader/test_weight_utils.py`_
- **2026-10-30** [`2b354b0006`](https://github.com/sgl-project/sglang/commit/2b354b0006) [#47056](https://github.com/sgl-project/sglang/pull/47056)
  [CI] [Intel] xpu-eval: Add sgl-eval to XPU test deps and move all GSM8K tests to it (#47056)
  _Files: `.github/workflows/nightly-test-intel-wheel.yml`, `.github/workflows/nightly-test-intel.yml`, `python/pyproject_xpu.toml`, `python/sglang/test/xpu/simple_eval_gsm8k_xpu_mixin.py` _+7 more__
- **2026-10-30** [`f362716a21`](https://github.com/sgl-project/sglang/commit/f362716a21) [#46676](https://github.com/sgl-project/sglang/pull/46676)
  [Fix] dsv4: Keep a coordinated verify rank out of the decoder-tail idle replay (#46676)
  _Files: `python/sglang/srt/models/deepseek_v4_replay_tail.py`_
- **2026-10-29** [`390acf84e3`](https://github.com/sgl-project/sglang/commit/390acf84e3) [#47212](https://github.com/sgl-project/sglang/pull/47212)
  [Doc] cookbook: Add a new cookbook page (WIP) (#47212)
  _Files: `docs/cookbook/autoregressive/Mistral/Mistral-Large-4.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json`, `docs/src/snippets/_playground.jsx` _+2 more__
- **2026-10-29** [`d1512ad9e9`](https://github.com/sgl-project/sglang/commit/d1512ad9e9) [#47230](https://github.com/sgl-project/sglang/pull/47230)
  [CI] [NPU] coverage: Automated OBS baseline upload and retry-safe attempt merging (#47230)
  _Files: `.github/workflows/pr-test-npu.yml`, `test/registered/npu/accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py`, `test/registered/npu/rl/indexer_replay/test_npu_return_indexer_topk_deepseek_v4.py`, `test/registered/npu/rl/indexer_replay/test_npu_return_indexer_topk_glm52.py`_
- **2026-10-27** [`d3a157a2f2`](https://github.com/sgl-project/sglang/commit/d3a157a2f2) [#46620](https://github.com/sgl-project/sglang/pull/46620)
  [Fix] startup: remove TorchScript deprecations at their sources (#46620)
  _Files: `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml`, `python/pyproject_other.toml` _+4 more__
- **2026-10-27** [`dea05ca16e`](https://github.com/sgl-project/sglang/commit/dea05ca16e) [#46718](https://github.com/sgl-project/sglang/pull/46718)
  [Refactor] dsv4: Set the tail source KV layer id in a capture stub (#46718)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-10-27** [`20ff40cb84`](https://github.com/sgl-project/sglang/commit/20ff40cb84) [#41275](https://github.com/sgl-project/sglang/pull/41275)
  [Fix] deepseek-v4.1: Match KV capacity to physical layouts (#41275)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_

## Docs / Examples  (7 commits)

- **2026-11-02** [`2c362af4cc`](https://github.com/sgl-project/sglang/commit/2c362af4cc) [#47429](https://github.com/sgl-project/sglang/pull/47429)
  [Doc] [NPU] docs: clarify installation and quickstart docs for Ascend NPUs (#47429)
  _Files: `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/quick_start.mdx`_
- **2026-10-31** [`a810654563`](https://github.com/sgl-project/sglang/commit/a810654563) [#44825](https://github.com/sgl-project/sglang/pull/44825)
  [Doc] blogs: Sync LMSYS SGLang blog cards (#44825)
  _Files: `docs/index.mdx`_
- **2026-10-30** [`05fb1c98ad`](https://github.com/sgl-project/sglang/commit/05fb1c98ad) [#45360](https://github.com/sgl-project/sglang/pull/45360)
  [Doc] cookbook: add Muse Spark unified memory control (#45360)
  _Files: `docs/cookbook/autoregressive/Meta/MuseSparkOpen.mdx`, `docs/src/snippets/configs/meta-models/muse-spark.jsx`_
- **2026-10-29** [`733ca06615`](https://github.com/sgl-project/sglang/commit/733ca06615) [#47041](https://github.com/sgl-project/sglang/pull/47041)
  [Doc] docs: Fix documentation normative issues (#47041)
  _Files: `docs/docs/hardware-platforms/ascend-npus/getting-started/installation.mdx`, `docs/docs/hardware-platforms/ascend-npus/getting-started/quick_start.mdx`_
- **2026-10-27** [`33e8e0fabd`](https://github.com/sgl-project/sglang/commit/33e8e0fabd) [#46859](https://github.com/sgl-project/sglang/pull/46859)
  [Doc] cookbook: Add LFM3 cookbook (#46859)
  _Files: `docs/cookbook/autoregressive/LiquidAI/LFM2.5.mdx`, `docs/cookbook/autoregressive/LiquidAI/LFM3.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-10-26** [`d1bbcbdc0d`](https://github.com/sgl-project/sglang/commit/d1bbcbdc0d) [#45642](https://github.com/sgl-project/sglang/pull/45642)
  [Doc] [NPU] cookbook: add A3 deployment scenarios to GLM-5.2 (#45642)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-10-26** [`eabb11a4c1`](https://github.com/sgl-project/sglang/commit/eabb11a4c1) [#46505](https://github.com/sgl-project/sglang/pull/46505)
  [Feat] sgl-router: Confirmed-first pending prefixes for cold prompts, with a follower cap (#46505)
  _Files: `sgl-router/REFERENCE.md`, `sgl-router/monitoring/README.md`, `sgl-router/src/config/cli.rs`, `sgl-router/src/config/types.rs` _+8 more__

## Serving / API  (5 commits)

- **2026-11-02** [`b45a36531c`](https://github.com/sgl-project/sglang/commit/b45a36531c) [#45972](https://github.com/sgl-project/sglang/pull/45972)
  [Fix] kimi_k3: Use uuid tool_call_id instead of history-count id (#45972)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-10-31** [`140bb6dc8d`](https://github.com/sgl-project/sglang/commit/140bb6dc8d) [#47662](https://github.com/sgl-project/sglang/pull/47662)
  [Fix] reasoning: Reject reasoning_effort outside the enum for M3 (#47662)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-10-30** [`5008726431`](https://github.com/sgl-project/sglang/commit/5008726431) [#46937](https://github.com/sgl-project/sglang/pull/46937)
  [Fix] anthropic: Preserve cache_salt for Messages requests (#46937)
  _Files: `python/sglang/srt/entrypoints/anthropic/protocol.py`, `python/sglang/srt/entrypoints/anthropic/serving.py`, `test/registered/unit/entrypoints/anthropic/test_serving.py`_
- **2026-10-29** [`6c61cecca7`](https://github.com/sgl-project/sglang/commit/6c61cecca7) [#47158](https://github.com/sgl-project/sglang/pull/47158)
  [Refactor] engine: Make the follower-rank SIGTERM handler an overridable classmethod (#47158)
  _Files: `python/sglang/srt/entrypoints/engine.py`_
- **2026-10-26** [`2b84393124`](https://github.com/sgl-project/sglang/commit/2b84393124) [#46432](https://github.com/sgl-project/sglang/pull/46432)
  [Chore] sgl-router: use `api.v1` typed generate response (#46432)
  _Files: `rust/sglang-processor/README.md`, `rust/sglang-processor/src/openai/chat.rs`, `rust/sglang-processor/src/openai/completions.rs`, `rust/sglang-processor/src/openai/mod.rs` _+3 more__

## LoRA  (3 commits)

- **2026-11-02** [`1ced9a9eb0`](https://github.com/sgl-project/sglang/commit/1ced9a9eb0) [#46251](https://github.com/sgl-project/sglang/pull/46251)
  [Perf] sgl-router: Encode tiktoken models with fastokens under --tokenizer-backend fast (#46251)
  _Files: `sgl-router/REFERENCE.md`, `sgl-router/src/tokenizer/adapter.rs`, `sgl-router/src/tokenizer/mod.rs`, `sgl-router/src/tokenizer/stats.rs` _+7 more__
- **2026-10-29** [`259f0131c9`](https://github.com/sgl-project/sglang/commit/259f0131c9) [#46500](https://github.com/sgl-project/sglang/pull/46500)
  [Feat] LoRA: revamp LoRADrainer for better performance (#46500)
  _Files: `docs/docs/advanced_features/lora.mdx`, `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/fields/lora.py`, `python/sglang/srt/lora/lora_drainer.py` _+3 more__
- **2026-10-29** [`901ec9fbf6`](https://github.com/sgl-project/sglang/commit/901ec9fbf6) [#45951](https://github.com/sgl-project/sglang/pull/45951)
  [Perf] LoRA: improve throughput and GPU memory usage for multi-LoRA serving under PP (#45951)
  _Files: `docs/docs/advanced_features/lora.mdx`, `python/sglang/srt/arg_groups/fields/lora.py`, `python/sglang/srt/lora/lora_manager.py`, `python/sglang/srt/lora/mem_pool.py` _+6 more__

## Structured Output  (3 commits)

- **2026-10-27** [`9d45fdda46`](https://github.com/sgl-project/sglang/commit/9d45fdda46) [#44124](https://github.com/sgl-project/sglang/pull/44124)
  [Fix] qwen3_coder: Preserve structured values in qwen3_coder mixed unions (#44124)
  _Files: `python/sglang/srt/function_call/qwen3_coder_detector.py`, `test/registered/unit/function_call/test_function_call_parser.py`_
- **2026-10-26** [`5ef99013ac`](https://github.com/sgl-project/sglang/commit/5ef99013ac) [#46049](https://github.com/sgl-project/sglang/pull/46049)
  [Fix] grammar: Give grammar accept failures an error status (#46049)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`_
- **2026-10-26** [`fa622d311d`](https://github.com/sgl-project/sglang/commit/fa622d311d) [#36074](https://github.com/sgl-project/sglang/pull/36074)
  [Feat] [NPU] llguidance: add bitmask path for Ascend (#36074)
  _Files: `python/sglang/srt/constrained/llguidance_backend.py`, `test/manual/ascend/test_llguidance_npu_mask.py`_

---
_Generated 2026-11-02 18:12 UTC_