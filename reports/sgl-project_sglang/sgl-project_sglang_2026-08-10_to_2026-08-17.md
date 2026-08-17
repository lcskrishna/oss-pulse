# sgl-project/sglang — Weekly Change Report
**Period:** 2026-08-10 → 2026-08-17  |  **Total commits:** 394

## ✨ New Features This Week

- **2026-08-17** [#33676](https://github.com/sgl-project/sglang/pull/33676) — [NPU] Support DeepSeek-V4 DSpark and refactor DSV4 cache management (#33676)
- **2026-08-17** [#33480](https://github.com/sgl-project/sglang/pull/33480) — [AMD] Support prefill context parallel two batch overlap for DeepSeek V4 (#33480)
- **2026-08-17** [#22498](https://github.com/sgl-project/sglang/pull/22498) — [CPU] Add support for Gemma4 on Xeon (#22498)
- **2026-08-17** [#35068](https://github.com/sgl-project/sglang/pull/35068) — [Docs] Feature MiniMax-H3 in the popular-models banner (#35068)
- **2026-08-16** [#34645](https://github.com/sgl-project/sglang/pull/34645) — [AMD][CI] Add GPT-OSS perf benchmarks to the ROCm 7.2 nightly (#34645)
- **2026-08-16** [#34998](https://github.com/sgl-project/sglang/pull/34998) — Add explicit EPLB balancedness reporting modes (#34998)
- **2026-08-16** [#35000](https://github.com/sgl-project/sglang/pull/35000) — Support unified SWA page mapping in attention metadata (#35000)
- **2026-08-16** [#35002](https://github.com/sgl-project/sglang/pull/35002) — Support model-defined prefill input embedding width (#35002)
- **2026-08-16** [#34696](https://github.com/sgl-project/sglang/pull/34696) — [Spec] Support logprobs with DSpark speculative decoding (#34696)
- **2026-08-16** [#35018](https://github.com/sgl-project/sglang/pull/35018) — Clean up playground scripts and add PR babysitter launcher (#35018)
- _…and 84 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-17** [`b83d507cd7`](https://github.com/sgl-project/sglang/commit/b83d507cd7) [#33676](https://github.com/sgl-project/sglang/pull/33676) — [NPU] Support DeepSeek-V4 DSpark and refactor DSV4 cache management (#33676)
- **2026-08-17** [`0099107e8b`](https://github.com/sgl-project/sglang/commit/0099107e8b) [#35105](https://github.com/sgl-project/sglang/pull/35105) — Revert "[AMD] [GLM5] Fuse shared-expert append into aiter grouped-topk (skip per-layer append kernel)" (#35105)
- **2026-08-17** [`eb61cb2823`](https://github.com/sgl-project/sglang/commit/eb61cb2823) [#33480](https://github.com/sgl-project/sglang/pull/33480) — [AMD] Support prefill context parallel two batch overlap for DeepSeek V4 (#33480)
- **2026-08-17** [`8e0499bd50`](https://github.com/sgl-project/sglang/commit/8e0499bd50) [#31323](https://github.com/sgl-project/sglang/pull/31323) — [AMD] [GLM5] Fuse shared-expert append into aiter grouped-topk (skip per-layer append kernel) (#31323)
- **2026-08-16** [`d91c3682b0`](https://github.com/sgl-project/sglang/commit/d91c3682b0) [#34645](https://github.com/sgl-project/sglang/pull/34645) — [AMD][CI] Add GPT-OSS perf benchmarks to the ROCm 7.2 nightly (#34645)
- **2026-08-16** [`f7cb328eb7`](https://github.com/sgl-project/sglang/commit/f7cb328eb7) [#31324](https://github.com/sgl-project/sglang/pull/31324) — [AMD] [GLM5] Skip DSA decode indexer when kv_len <= index_topk (dense k-only fast path) (#31324)
- **2026-08-16** [`67e12131df`](https://github.com/sgl-project/sglang/commit/67e12131df) [#34994](https://github.com/sgl-project/sglang/pull/34994) — Build Rust extensions on demand in source checkouts (#34994)
- **2026-08-16** [`24ab8f9ed9`](https://github.com/sgl-project/sglang/commit/24ab8f9ed9) [#34474](https://github.com/sgl-project/sglang/pull/34474) — [AMD] Qwen3.5: guard attn layers against empty DP-attention batch (#34474)
- **2026-08-16** [`66de161976`](https://github.com/sgl-project/sglang/commit/66de161976) [#32746](https://github.com/sgl-project/sglang/pull/32746) — [Fix][AMD] MoRI EP: drop record_stream in TBO dispatch/combine (HSA out-of-resources) (#32746)
- **2026-08-16** [`6314e9e4f5`](https://github.com/sgl-project/sglang/commit/6314e9e4f5) [#31794](https://github.com/sgl-project/sglang/pull/31794) — [AMD][Fix] Qwen3.5: guard zero-grid launch in fused_qk_gemma_rmsnorm(_with_gate) (HIP invalid configuration on idle DP rank) (#31794)
- **2026-08-16** [`f68517f644`](https://github.com/sgl-project/sglang/commit/f68517f644) [#30900](https://github.com/sgl-project/sglang/pull/30900) — [AMD][Quantization][Bugfix] Fix bug related to fp8 max on gfx95x for per-token-group quant (ROCm) (#30900)
- **2026-08-16** [`4c0e85524d`](https://github.com/sgl-project/sglang/commit/4c0e85524d) [#30808](https://github.com/sgl-project/sglang/pull/30808) — [AMD] [GLM5] Enable dense-MHA short-context prefill fallback on gfx950 (#30808)
- **2026-08-15** [`d22c4cc177`](https://github.com/sgl-project/sglang/commit/d22c4cc177) [#30024](https://github.com/sgl-project/sglang/pull/30024) — [AMD] perf(sgl-kernel): default block_quota=16 for MLA page_first KV gather… (#30024)
- **2026-08-15** [`4d0c5a89af`](https://github.com/sgl-project/sglang/commit/4d0c5a89af) [#34837](https://github.com/sgl-project/sglang/pull/34837) — [AMD] Add concat_and_cast_mha_k_pad_kernel to support 12-head and enable K3 aiter prefill kernel (#34837)
- **2026-08-15** [`6cbfa791d6`](https://github.com/sgl-project/sglang/commit/6cbfa791d6) [#34517](https://github.com/sgl-project/sglang/pull/34517) — [AMD][Spec] Accelerate Qwen3.5 verification with grouped-head shared KV (#34517)
- **2026-08-15** [`5c9ee86d90`](https://github.com/sgl-project/sglang/commit/5c9ee86d90) [#34913](https://github.com/sgl-project/sglang/pull/34913) — [CI] Move the static ratchets back to CPU unit tests (#34913)
- **2026-08-15** [`7216a44dd8`](https://github.com/sgl-project/sglang/commit/7216a44dd8) [#34238](https://github.com/sgl-project/sglang/pull/34238) — [AMD] Broadcast the EAGLE greedy verify decision across TP ranks on ROCm (#34238)
- **2026-08-15** [`bc7e3ba66c`](https://github.com/sgl-project/sglang/commit/bc7e3ba66c) [#29328](https://github.com/sgl-project/sglang/pull/29328) — [AMD][Quantization] Online MXFP4 quantization 4/N - NVFP4 to MXFP4 Online Requantization on AMD GPUs (#29328)
- **2026-08-15** [`5afdb1caea`](https://github.com/sgl-project/sglang/commit/5afdb1caea) [#34877](https://github.com/sgl-project/sglang/pull/34877) — [AMD CI] follow the miles nightly-prefixed MI350 suite names (#34877)
- **2026-08-15** [`2012b4b196`](https://github.com/sgl-project/sglang/commit/2012b4b196) [#34769](https://github.com/sgl-project/sglang/pull/34769) — [AMD][CI] Fix stage-b: AttributeError on multimodal embedding requests (#34769)
- **2026-08-14** [`5e65dd01a7`](https://github.com/sgl-project/sglang/commit/5e65dd01a7) [#34304](https://github.com/sgl-project/sglang/pull/34304) — Remove the torchao integration (--torchao-config) (#34304)
- **2026-08-14** [`65d62109dd`](https://github.com/sgl-project/sglang/commit/65d62109dd) [#34741](https://github.com/sgl-project/sglang/pull/34741) — [AMD] Fix Triton 3.7 gfx950 extend-attention spills (#34741)
- **2026-08-14** [`ba1d980b35`](https://github.com/sgl-project/sglang/commit/ba1d980b35) [#31856](https://github.com/sgl-project/sglang/pull/31856) — [AMD] Accelerate AITER unified-attention decode with scaled FP8 Q (#31856)
- **2026-08-14** [`240a12b302`](https://github.com/sgl-project/sglang/commit/240a12b302) [#28666](https://github.com/sgl-project/sglang/pull/28666) — [AMD] Fuse shared_expert_gate GEMV into the MoE append kernel (HIP/aiter) (#28666)
- **2026-08-14** [`85cdf1178d`](https://github.com/sgl-project/sglang/commit/85cdf1178d) [#34309](https://github.com/sgl-project/sglang/pull/34309) — [CI] Prune redundant CPU test overhead (#34309)
- **2026-08-14** [`34219ed9a7`](https://github.com/sgl-project/sglang/commit/34219ed9a7) [#34768](https://github.com/sgl-project/sglang/pull/34768) — [AMD] CI: pin antlr4-python3-runtime back after lmms-eval (unblocks ROCm 7.2 stage-b evals) (#34768)
- **2026-08-13** [`abdef3c38e`](https://github.com/sgl-project/sglang/commit/abdef3c38e) [#34770](https://github.com/sgl-project/sglang/pull/34770) — [Qwen] Update Docker image tag for MI300X to v0.5.17-rocm700-mi30x-20… (#34770)
- **2026-08-13** [`9720922671`](https://github.com/sgl-project/sglang/commit/9720922671) [#34761](https://github.com/sgl-project/sglang/pull/34761) — [AMD][CI] Restore gfx942 Grok-1 INT4 and Grok-2 schedules (#34761)
- **2026-08-13** [`29b067245b`](https://github.com/sgl-project/sglang/commit/29b067245b) [#34689](https://github.com/sgl-project/sglang/pull/34689) — [AMD] CI: drop the spaces from SGL_EVAL_SPEC (fixes ROCm 7.2 stage-a sgl-eval install) (#34689)
- **2026-08-13** [`07821e9d56`](https://github.com/sgl-project/sglang/commit/07821e9d56) [#34643](https://github.com/sgl-project/sglang/pull/34643) — [AMD][CI] Stop scheduling Grok-1 and Grok-2 on MI30x (#34643)
- **2026-08-13** [`34206c0017`](https://github.com/sgl-project/sglang/commit/34206c0017) [#34597](https://github.com/sgl-project/sglang/pull/34597) — [AMD] Run V4 MTP target-verify through the decode kernel (#34597)
- **2026-08-13** [`c034120cb8`](https://github.com/sgl-project/sglang/commit/c034120cb8) [#29202](https://github.com/sgl-project/sglang/pull/29202) — [AMD] Enable draft-extend CUDA graph and reduce bubble for MTP (#29202)
- **2026-08-13** [`b7f87a2513`](https://github.com/sgl-project/sglang/commit/b7f87a2513) [#34421](https://github.com/sgl-project/sglang/pull/34421) — [AMD][Perf] Fuse GatedDeltaNet QKVZBA split/reshape/cat into a single Triton kernel for Qwen3.5-architecture MoE on HIP (#34421)
- **2026-08-13** [`50cc1aa241`](https://github.com/sgl-project/sglang/commit/50cc1aa241) [#34477](https://github.com/sgl-project/sglang/pull/34477) — [CI] Route mmlu and GB300 MMMU-Pro evals through sgl-eval (#34477)
- **2026-08-13** [`bbda7f32b1`](https://github.com/sgl-project/sglang/commit/bbda7f32b1) [#34328](https://github.com/sgl-project/sglang/pull/34328) — [AMD][CI] CI: fix AMD 2-GPU multimodal-gen partition-count abort (#34328)
- **2026-08-12** [`9deb6952af`](https://github.com/sgl-project/sglang/commit/9deb6952af) [#34476](https://github.com/sgl-project/sglang/pull/34476) — [AMD][DI][CI] Add GLM-5.2 MXFP4 wide-EP16 2P1D nightly recipes (#34476)
- **2026-08-12** [`b5d1453ed2`](https://github.com/sgl-project/sglang/commit/b5d1453ed2) [#34379](https://github.com/sgl-project/sglang/pull/34379) — [AMD] GLM 5.2 MXFP4 SGLANG COOKBOOK (#34379)
- **2026-08-12** [`00bdafe944`](https://github.com/sgl-project/sglang/commit/00bdafe944) [#34204](https://github.com/sgl-project/sglang/pull/34204) — [AMD][CI] Swap the AMD PR gate to ROCm 7.2 and demote ROCm 7.0 to a daily shadow (#34204)
- **2026-08-12** [`793a11dd27`](https://github.com/sgl-project/sglang/commit/793a11dd27) [#34521](https://github.com/sgl-project/sglang/pull/34521) — [AMD] Publish an undated tag for the miles nightly images (#34521)
- **2026-08-12** [`a2d723820e`](https://github.com/sgl-project/sglang/commit/a2d723820e) [#34401](https://github.com/sgl-project/sglang/pull/34401) — [diffusion] fix: fix model-driven dit layerwise offload auto policy (#34401)
- **2026-08-11** [`6f3fe13a9c`](https://github.com/sgl-project/sglang/commit/6f3fe13a9c) [#34364](https://github.com/sgl-project/sglang/pull/34364) — [AMD] Install AITER's pinned Triton wheel in the ROCm 7.2 image (#34364)
- **2026-08-11** [`e74ea5b1d7`](https://github.com/sgl-project/sglang/commit/e74ea5b1d7) [#31105](https://github.com/sgl-project/sglang/pull/31105) — [ROCm/gfx95] Fix fp8 per-channel attention for Kimi-K2.7-code-mxfp4 o… (#31105)
- **2026-08-11** [`dd20826e0a`](https://github.com/sgl-project/sglang/commit/dd20826e0a) [#34220](https://github.com/sgl-project/sglang/pull/34220) — [AMD] Preserve the AITER expert mask across torch_memory_saver pause/resume (#34220)
- **2026-08-11** [`8d050dd880`](https://github.com/sgl-project/sglang/commit/8d050dd880) [#34324](https://github.com/sgl-project/sglang/pull/34324) — [AMD][CI] Run MI300 8-GPU stage-C shards two at a time (#34324)
- **2026-08-10** [`2c72323d90`](https://github.com/sgl-project/sglang/commit/2c72323d90) [#34203](https://github.com/sgl-project/sglang/pull/34203) — [AMD] Fix AITER custom reduce-scatter CUDA-graph capture crash under torch_memory_saver (#34203)
- **2026-08-10** [`ca0f8a0f4c`](https://github.com/sgl-project/sglang/commit/ca0f8a0f4c) [#33484](https://github.com/sgl-project/sglang/pull/33484) — perf(hisparse): fuse the DSv4 value and scale swap-in copy on ROCm (#33484)
- **2026-08-10** [`1a8e4876b6`](https://github.com/sgl-project/sglang/commit/1a8e4876b6) [#33085](https://github.com/sgl-project/sglang/pull/33085) — perf(hisparse): 128-bit non-temporal swap-in copy on ROCm (#33085)
- **2026-08-10** [`4eaaeda004`](https://github.com/sgl-project/sglang/commit/4eaaeda004) [#34276](https://github.com/sgl-project/sglang/pull/34276) — [CI] Build patched Docker images for both amd64 and arm64 (#34276)
- **2026-08-10** [`0977b22431`](https://github.com/sgl-project/sglang/commit/0977b22431) [#34261](https://github.com/sgl-project/sglang/pull/34261) — [AMD] Restore K3 MLA verify kernel path blocked by can_handle() guard (#34261)
- **2026-08-10** [`f2a4c4c847`](https://github.com/sgl-project/sglang/commit/f2a4c4c847) [#31843](https://github.com/sgl-project/sglang/pull/31843) — [AMD] [CI] Enable 3 nested unit tests needing harness stub fixes (#31843)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#34899](https://github.com/sgl-project/sglang/issues/34899) | [Feature] Bit-exact correctness coverage for Unified Radix Cache | — | 2026-08-17 |
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-08-17 |
| [#35122](https://github.com/sgl-project/sglang/issues/35122) | [Bug] [AMD] SGLANG_DSV4_FP4_DEQUANT=1 is ignored by AITER FP4 MoE on R | — | 2026-08-17 |
| [#35096](https://github.com/sgl-project/sglang/issues/35096) | [Bug] apply_rotary_emb_flat_kernel rotates and overwrites the columns  | — | 2026-08-17 |
| [#35053](https://github.com/sgl-project/sglang/issues/35053) | [Bug][Diffusion] Spectrum CFG parallel skips negative-branch initializ | — | 2026-08-16 |
| [#35047](https://github.com/sgl-project/sglang/issues/35047) | [Bug] Triton device-pointer tables use int64 and overflow on Intel XPU | — | 2026-08-16 |
| [#33978](https://github.com/sgl-project/sglang/issues/33978) | [Bug] | — | 2026-08-16 |
| [#35011](https://github.com/sgl-project/sglang/issues/35011) | [diffusion][Model] Support MAGI-2-preview | — | 2026-08-16 |
| [#35003](https://github.com/sgl-project/sglang/issues/35003) | AMD Development Roadmap (2026 Q3) | amd | 2026-08-16 |
| [#23494](https://github.com/sgl-project/sglang/issues/23494) | AMD Development Roadmap (2026 Q2) | amd | 2026-08-16 |
| [#33861](https://github.com/sgl-project/sglang/issues/33861) | [RFC] PD disaggregation: single protocol layer, per-backend transport | — | 2026-08-15 |
| [#34604](https://github.com/sgl-project/sglang/issues/34604) | [Bug] Kimi-K3 tool call parser fails ~8x/hour in production: TypeError | — | 2026-08-15 |
| [#24488](https://github.com/sgl-project/sglang/issues/24488) | [Help] [Performance] PD disaggregation on H200 shows no throughput gai | — | 2026-08-15 |
| [#23206](https://github.com/sgl-project/sglang/issues/23206) | [RFC] Sglang non-GPU process rust migration | — | 2026-08-14 |
| [#29736](https://github.com/sgl-project/sglang/issues/29736) | [Roadmap][DCP] Decode Context Parallelism & Helix Parallelism (2026 Q3 | — | 2026-08-14 |
| [#34861](https://github.com/sgl-project/sglang/issues/34861) | [Bug] [NPU] Router GEMM output should always be fp32 | npu | 2026-08-14 |
| [#34857](https://github.com/sgl-project/sglang/issues/34857) | [Bug] [ROCm] Router GEMM output should always be fp32, and the expert  | amd, aiter | 2026-08-14 |
| [#34815](https://github.com/sgl-project/sglang/issues/34815) | PP8 disaggregated prefill has a load-independent ~30 s TTFT floor on K | — | 2026-08-14 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-08-14 |
| [#32321](https://github.com/sgl-project/sglang/issues/32321) | [RFC] Replace the MLX runner-stub split with one Torch-owned SRT path  | — | 2026-08-14 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Multimodal | 81 |
| Attention / FlashInfer | 76 |
| MoE / Expert Parallel | 41 |
| KV Cache / Memory | 29 |
| Prefill / Decode Disaggregation | 27 |
| Other | 27 |
| Quantization | 20 |
| Docs / Examples | 18 |
| Models | 13 |
| Triton / Kernels | 13 |
| Tensor / Data Parallel | 10 |
| Speculative Decoding | 9 |
| CI / Build | 9 |
| ROCm / AMD | 8 |
| Scheduler / Batching | 7 |
| Serving / API | 4 |
| Structured Output | 2 |

## Multimodal  (81 commits)

- **2026-08-17** [`eafbe2cb6f`](https://github.com/sgl-project/sglang/commit/eafbe2cb6f) [#34818](https://github.com/sgl-project/sglang/pull/34818)
  [CI] Install sgl-eval in xeon (CPU) Docker image (#34818)
  _Files: `docker/xeon.Dockerfile`_
- **2026-08-17** [`0aa09ab40d`](https://github.com/sgl-project/sglang/commit/0aa09ab40d) [#34930](https://github.com/sgl-project/sglang/pull/34930)
  [diffusion] Reuse bit-exact modulation fast path for LTX-2.3 (#34930)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `test/registered/kernels/ops/diffusion/test_ltx2_rms_norm_modulate.py`_
- **2026-08-16** [`a508d60295`](https://github.com/sgl-project/sglang/commit/a508d60295) [#34245](https://github.com/sgl-project/sglang/pull/34245)
  [BCG][6/N] Allow prefill breakable CUDA graph for the Kimi archs (#34245)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/configs/test_multimodal_piecewise_cuda_graph.py`_
- **2026-08-16** [`c6ebcf39ee`](https://github.com/sgl-project/sglang/commit/c6ebcf39ee) [#34995](https://github.com/sgl-project/sglang/pull/34995)
  [VLM] Avoid synchronizing multimodal placeholder counts (#34995)
  _Files: `python/sglang/srt/managers/mm_schedule.py`, `python/sglang/srt/utils/async_probe.py`, `test/registered/unit/managers/test_mm_embedding_length.py`_
- **2026-08-16** [`67e12131df`](https://github.com/sgl-project/sglang/commit/67e12131df) [#34994](https://github.com/sgl-project/sglang/pull/34994)
  Build Rust extensions on demand in source checkouts (#34994)
  _Files: `.github/actions/download-rust-ext/action.yml`, `.github/workflows/_pr-test-rust-ext-build.yml`, `.gitignore`, `docker/rocm.Dockerfile` _+35 more__
- **2026-08-16** [`d3589a7251`](https://github.com/sgl-project/sglang/commit/d3589a7251) [#35016](https://github.com/sgl-project/sglang/pull/35016)
  [diffusion] CI: tighten NVIDIA perf baselines (#35016)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines/5090.json`, `python/sglang/multimodal_gen/test/server/perf_baselines/h100.json`, `python/sglang/multimodal_gen/test/server/test_server_common.py`_
- **2026-08-16** [`41abbb0d32`](https://github.com/sgl-project/sglang/commit/41abbb0d32) [#34932](https://github.com/sgl-project/sglang/pull/34932)
  [diffusion] Accelerate Cosmos3 T2I QKNorm+RoPE (#34932)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`, `test/registered/kernels/ops/diffusion/test_qknorm_rope.py`_
- **2026-08-16** [`095ec6c997`](https://github.com/sgl-project/sglang/commit/095ec6c997) [#34928](https://github.com/sgl-project/sglang/pull/34928)
  [diffusion][kernel] Accelerate Sana BCG with bit-exact conv post-processing (#34928)
  _Files: `python/sglang/kernels/ops/diffusion/triton/sana_conv_post.py`, `python/sglang/multimodal_gen/runtime/models/dits/sana.py`, `test/registered/kernels/ops/diffusion/test_sana_conv_post.py`_
- **2026-08-16** [`0761d3f3a4`](https://github.com/sgl-project/sglang/commit/0761d3f3a4) [#34931](https://github.com/sgl-project/sglang/pull/34931)
  [diffusion] Accelerate lossless Ideogram norm post-processing (#34931)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/ideogram.py`, `python/sglang/multimodal_gen/test/unit/test_ideogram4.py`_
- **2026-08-16** [`b752f1e533`](https://github.com/sgl-project/sglang/commit/b752f1e533) [#34929](https://github.com/sgl-project/sglang/pull/34929)
  [diffusion] Enable breakable CUDA graphs for LTX-2.3 (#34929)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ltx_2/denoising.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_bcg_padding.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_bcg_coords.py`_
- **2026-08-16** [`a54de989c8`](https://github.com/sgl-project/sglang/commit/a54de989c8) [#34817](https://github.com/sgl-project/sglang/pull/34817)
  [diffusion] chore: speed up minimax-h3 vae decode on 2×h100 (#34817)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `python/sglang/multimodal_gen/test/server/gpu_cases.py` _+2 more__
- **2026-08-16** [`4f9da62547`](https://github.com/sgl-project/sglang/commit/4f9da62547) [#34980](https://github.com/sgl-project/sglang/pull/34980)
  [diffusion] chore: use native hunyuan3d paint and delight models (#34980)
  _Files: `python/sglang/multimodal_gen/configs/models/vaes/stable_diffusion.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan3d.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload_components.py`, `python/sglang/multimodal_gen/runtime/models/dits/hunyuan3d.py` _+7 more__
- **2026-08-16** [`19e3bd6391`](https://github.com/sgl-project/sglang/commit/19e3bd6391) [#34945](https://github.com/sgl-project/sglang/pull/34945)
  [diffusion] chore: use native qwen3-vl vision encoder (#34945)
  _Files: `python/sglang/multimodal_gen/configs/models/encoders/qwen3vl.py`, `python/sglang/multimodal_gen/runtime/models/encoders/minimax_h3_qwen3vl.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen3vl.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen3vl_vision.py` _+1 more__
- **2026-08-16** [`eb6b773149`](https://github.com/sgl-project/sglang/commit/eb6b773149) [#34896](https://github.com/sgl-project/sglang/pull/34896)
  [diffusion] chore: use native qwen2.5-vl generation (#34896)
  _Files: `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs/docs/sglang-diffusion/models_with_ar.mdx`, `python/sglang/multimodal_gen/configs/models/encoders/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/longcat_image.py` _+12 more__
- **2026-08-15** [`4beb157e87`](https://github.com/sgl-project/sglang/commit/4beb157e87) [#34952](https://github.com/sgl-project/sglang/pull/34952)
  [diffusion] doc: define native diffusion model integration contract (#34952)
  _Files: `docs/docs/sglang-diffusion/support_new_models.mdx`_
- **2026-08-15** [`a64791b312`](https://github.com/sgl-project/sglang/commit/a64791b312) [#34811](https://github.com/sgl-project/sglang/pull/34811)
  test: restore GLM-4.1V nightly latency threshold (#34811)
  _Files: `test/registered/eval/test_vlms_mmmu_eval.py`_
- **2026-08-15** [`0c072235f4`](https://github.com/sgl-project/sglang/commit/0c072235f4) [#34825](https://github.com/sgl-project/sglang/pull/34825)
  [diffusion] Bound overlong weight lock filenames (#34825)
  _Files: `python/sglang/multimodal_gen/runtime/loader/weight_utils.py`, `python/sglang/multimodal_gen/test/unit/test_weight_utils.py`_
- **2026-08-15** [`2012b4b196`](https://github.com/sgl-project/sglang/commit/2012b4b196) [#34769](https://github.com/sgl-project/sglang/pull/34769)
  [AMD][CI] Fix stage-b: AttributeError on multimodal embedding requests (#34769)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-08-14** [`9c9a3273be`](https://github.com/sgl-project/sglang/commit/9c9a3273be) [#34826](https://github.com/sgl-project/sglang/pull/34826)
  [diffusion] Fix Helios denoising profiler stepping (#34826)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/helios_denoising.py`, `python/sglang/multimodal_gen/test/unit/test_helios_denoising_profiler.py`_
- **2026-08-14** [`9d2f1584fa`](https://github.com/sgl-project/sglang/commit/9d2f1584fa) [#34848](https://github.com/sgl-project/sglang/pull/34848)
  Fix MiniMax-H3 Cache-DiT BCG warning (#34848)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py`_
- **2026-08-14** [`4d94f1d310`](https://github.com/sgl-project/sglang/commit/4d94f1d310) [#34242](https://github.com/sgl-project/sglang/pull/34242)
  [diffusion] fix: warn when bcg disables cache-dit (#34242)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_bcg_padding.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_admission.py`_
- **2026-08-14** [`a86edcdc0a`](https://github.com/sgl-project/sglang/commit/a86edcdc0a) [#34650](https://github.com/sgl-project/sglang/pull/34650)
  [diffusion] feat: rebuild minimax-h3 adaln outputs on demand (#34650)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py` _+8 more__
- **2026-08-14** [`7c15b9b7d0`](https://github.com/sgl-project/sglang/commit/7c15b9b7d0) [#34121](https://github.com/sgl-project/sglang/pull/34121)
  [diffusion] fix: fix cache-first fast path accepting a metadata-only snapshot (#34121)
  _Files: `python/sglang/multimodal_gen/runtime/utils/hf_diffusers_utils.py`, `python/sglang/multimodal_gen/test/unit/test_hf_diffusers_utils.py`_
- **2026-08-14** [`827552bc1d`](https://github.com/sgl-project/sglang/commit/827552bc1d) [#34496](https://github.com/sgl-project/sglang/pull/34496)
  Fix eager AMX backend probe imports (#34496)
  _Files: `python/sglang/multimodal_gen/runtime/utils/common.py`, `python/sglang/srt/utils/common.py`, `test/registered/kernels/ops/layernorm/test_kernels_namespace.py`_
- **2026-08-13** [`abdef3c38e`](https://github.com/sgl-project/sglang/commit/abdef3c38e) [#34770](https://github.com/sgl-project/sglang/pull/34770)
  [Qwen] Update Docker image tag for MI300X to v0.5.17-rocm700-mi30x-20… (#34770)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8.jsx`_
- **2026-08-13** [`69a31ce342`](https://github.com/sgl-project/sglang/commit/69a31ce342) [#33827](https://github.com/sgl-project/sglang/pull/33827)
  fix: make Cache-DiT actually cache on MiniMax-H3 (#33827)
  _Files: `python/sglang/kernels/ops/diffusion/triton/indexed_modulation.py`, `python/sglang/multimodal_gen/runtime/cache/cache_dit_integration.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/denoising.py` _+1 more__
- **2026-08-13** [`c255fbc4fe`](https://github.com/sgl-project/sglang/commit/c255fbc4fe) [#34748](https://github.com/sgl-project/sglang/pull/34748)
  [Diffusion] Add @triple-mu as a code owner (#34748)
  _Files: `.github/CODEOWNERS`_
- **2026-08-13** [`ea7a6e0e99`](https://github.com/sgl-project/sglang/commit/ea7a6e0e99) [#34575](https://github.com/sgl-project/sglang/pull/34575)
  fix(diffusion): unshard FSDP root group for custom encoder entry points (#34575)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/runtime/models/dits/base.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py` _+3 more__
- **2026-08-13** [`ebca0bbde4`](https://github.com/sgl-project/sglang/commit/ebca0bbde4) [#34620](https://github.com/sgl-project/sglang/pull/34620)
  [Diffusion][ERNIE] Fuse QKNorm with full-width RoPE (#34620)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_rope.cuh`, `python/sglang/kernels/ops/diffusion/qknorm_rope.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/ernie_image.py` _+2 more__
- **2026-08-13** [`82f7afb881`](https://github.com/sgl-project/sglang/commit/82f7afb881) [#34615](https://github.com/sgl-project/sglang/pull/34615)
  [Diffusion] Make auto residency decisions component-scoped (#34615)
  _Files: `python/sglang/multimodal_gen/runtime/server_args/auto_tune.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-08-13** [`74c0322342`](https://github.com/sgl-project/sglang/commit/74c0322342) [#34616](https://github.com/sgl-project/sglang/pull/34616)
  [Diffusion][FLUX.2] Fuse eager AdaLN and packed SwiGLU (#34616)
  _Files: `python/sglang/kernels/ops/diffusion/triton/silu_mul_bitexact.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux_2.py`, `test/registered/kernels/ops/diffusion/test_flux2_eager_fusions.py`_
- **2026-08-13** [`3c1791a7df`](https://github.com/sgl-project/sglang/commit/3c1791a7df) [#34617](https://github.com/sgl-project/sglang/pull/34617)
  [Diffusion][HunyuanVideo] Fuse eager QKV packing and high-quality QKNorm (#34617)
  _Files: `python/sglang/kernels/ops/diffusion/hunyuan_qknorm.py`, `python/sglang/kernels/ops/diffusion/triton/hunyuan_qkv_pack.py`, `python/sglang/multimodal_gen/runtime/models/dits/hunyuanvideo.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py` _+1 more__
- **2026-08-13** [`993e24df75`](https://github.com/sgl-project/sglang/commit/993e24df75) [#34534](https://github.com/sgl-project/sglang/pull/34534)
  [diffusion] Add --dit-layerwise-residency-policy for strided DiT residency (#34534)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload_components.py`, `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_layerwise_offload.py`_
- **2026-08-13** [`b764194e81`](https://github.com/sgl-project/sglang/commit/b764194e81) [#23274](https://github.com/sgl-project/sglang/pull/23274)
  [diffusion] model: support LongCat-Image (#23274)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/longcat_image.py`, `python/sglang/multimodal_gen/configs/models/vaes/longcat_image.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/longcat_image.py`, `python/sglang/multimodal_gen/configs/sample/longcat_image.py` _+6 more__
- **2026-08-13** [`a23670ddbf`](https://github.com/sgl-project/sglang/commit/a23670ddbf) [#34584](https://github.com/sgl-project/sglang/pull/34584)
  [diffusion] Wan2.2-TI2V: fuse per-token adaLN table add into contiguous slices + hoist rope cache (denoise -13.1% H100 / -12.6% H200, bit-exact; eager beats compile) (#34584)
  _Files: `python/sglang/kernels/ops/diffusion/triton/wan_temb_table_slices.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`, `python/sglang/multimodal_gen/test/unit/test_wan_temb_table_slices.py`_
- **2026-08-13** [`969921b32d`](https://github.com/sgl-project/sglang/commit/969921b32d) [#34655](https://github.com/sgl-project/sglang/pull/34655)
  [diffusion] chore: track minimax-h3 in the nightly diffusion benchmark (#34655)
  _Files: `scripts/ci/utils/diffusion/comparison_configs.json`, `scripts/ci/utils/diffusion/run_comparison.py`_
- **2026-08-13** [`e8c7dddfa0`](https://github.com/sgl-project/sglang/commit/e8c7dddfa0) [#34398](https://github.com/sgl-project/sglang/pull/34398)
  [VLM] add content-addressed preprocessing cache infrastructure (#34398)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_control_mixin.py` _+14 more__
- **2026-08-13** [`69bf601e3c`](https://github.com/sgl-project/sglang/commit/69bf601e3c) [#34662](https://github.com/sgl-project/sglang/pull/34662)
  fix: restore VLM nightly regression coverage (#34662)
  _Files: `python/sglang/srt/server_args.py`, `python/sglang/test/test_utils.py`, `test/registered/eval/test_vlms_mmmu_eval.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-08-13** [`a318e16956`](https://github.com/sgl-project/sglang/commit/a318e16956) [#34652](https://github.com/sgl-project/sglang/pull/34652)
  [diffusion] feat: publish an index of nightly comparison runs (#34652)
  _Files: `scripts/ci/utils/diffusion/publish_comparison_results.py`_
- **2026-08-13** [`26579d893e`](https://github.com/sgl-project/sglang/commit/26579d893e) [#34619](https://github.com/sgl-project/sglang/pull/34619)
  [Diffusion][GLM-Image] Retune QK head LayerNorm for SM103 (#34619)
  _Files: `python/sglang/kernels/ops/diffusion/triton/layernorm_modulate.py`_
- **2026-08-13** [`bbda7f32b1`](https://github.com/sgl-project/sglang/commit/bbda7f32b1) [#34328](https://github.com/sgl-project/sglang/pull/34328)
  [AMD][CI] CI: fix AMD 2-GPU multimodal-gen partition-count abort (#34328)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `python/sglang/multimodal_gen/test/partitioning.py`, `python/sglang/multimodal_gen/test/run_suite.py` _+2 more__
- **2026-08-12** [`c05eb856f7`](https://github.com/sgl-project/sglang/commit/c05eb856f7) [#34523](https://github.com/sgl-project/sglang/pull/34523)
  [CI] Fix nightly test failures (#34523)
  _Files: `python/sglang/test/test_utils.py`, `test/manual/8-gpu-models/test_llama4.py`, `test/manual/nightly/test_text_models_gsm8k_eval.py`, `test/manual/nightly/test_text_models_perf.py` _+2 more__
- **2026-08-12** [`ad47dde65c`](https://github.com/sgl-project/sglang/commit/ad47dde65c) [#34275](https://github.com/sgl-project/sglang/pull/34275)
  [diffusion] optimize: fuse cosmos qk norm, rope, and kv packing (#34275)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_rope.cuh`, `python/sglang/kernels/ops/diffusion/qknorm_rope.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py` _+1 more__
- **2026-08-12** [`dc5f6c4883`](https://github.com/sgl-project/sglang/commit/dc5f6c4883) [#34564](https://github.com/sgl-project/sglang/pull/34564)
  [diffusion] optimize: stream and parallelize bit-exact video output saves (#34564)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/video_adapter.py`, `python/sglang/multimodal_gen/test/unit/test_output_saving.py`_
- **2026-08-12** [`9701cc138c`](https://github.com/sgl-project/sglang/commit/9701cc138c) [#34563](https://github.com/sgl-project/sglang/pull/34563)
  [diffusion] optimize: optimize bit-exact h3 reference video ingress (#34563)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/reference_encoding.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/text_encoding.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/minimax_h3/stages/visual_encoding.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_media.py`_
- **2026-08-12** [`b3bffef70a`](https://github.com/sgl-project/sglang/commit/b3bffef70a) [#34512](https://github.com/sgl-project/sglang/pull/34512)
  [diffusion] UX: suppress noisy worker startup warnings (#34512)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/utils/logging_utils.py`, `python/sglang/multimodal_gen/test/unit/test_logging_utils.py`_
- **2026-08-12** [`644d55ebfa`](https://github.com/sgl-project/sglang/commit/644d55ebfa) [#34359](https://github.com/sgl-project/sglang/pull/34359)
  [diffusion] feat: support native and peft minimax h3 loras (#34359)
  _Files: `docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `python/sglang/multimodal_gen/configs/models/dits/minimax_h3.py` _+12 more__
- **2026-08-12** [`1f008dc226`](https://github.com/sgl-project/sglang/commit/1f008dc226) [#34508](https://github.com/sgl-project/sglang/pull/34508)
  [Diffusion][LTX-2] Allocate AdaLN outputs from one contiguous slab (#34508)
  _Files: `python/sglang/kernels/ops/diffusion/triton/ltx2_ada_values.py`, `test/registered/kernels/ops/diffusion/test_ltx2_ada_values.py`_
- **2026-08-12** [`daae3acb36`](https://github.com/sgl-project/sglang/commit/daae3acb36) [#34507](https://github.com/sgl-project/sglang/pull/34507)
  [Diffusion][Z-Image] Tune native QK RMSNorm launch for SM103 (#34507)
  _Files: `python/sglang/kernels/ops/diffusion/triton/zimage_native_norm.py`_
- **2026-08-12** [`84ce7502cf`](https://github.com/sgl-project/sglang/commit/84ce7502cf) [#34505](https://github.com/sgl-project/sglang/pull/34505)
  [Diffusion][MiniMax H3] Extend exact QKNorm+RoPE rounding to SM103 (#34505)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_rope.cuh`_
- **2026-08-12** [`45f7063335`](https://github.com/sgl-project/sglang/commit/45f7063335) [#34503](https://github.com/sgl-project/sglang/pull/34503)
  [Diffusion] Tune QK head LayerNorm for SM103 (#34503)
  _Files: `python/sglang/kernels/ops/diffusion/triton/layernorm_modulate.py`_
- **2026-08-12** [`793a11dd27`](https://github.com/sgl-project/sglang/commit/793a11dd27) [#34521](https://github.com/sgl-project/sglang/pull/34521)
  [AMD] Publish an undated tag for the miles nightly images (#34521)
  _Files: `.github/workflows/release-docker-amd-miles-rocm700-nightly.yml`, `.github/workflows/release-docker-amd-miles-rocm720-nightly.yml`_
- **2026-08-12** [`22e4b3a81f`](https://github.com/sgl-project/sglang/commit/22e4b3a81f) [#34350](https://github.com/sgl-project/sglang/pull/34350)
  [Diffusion] Avoid slow cuBLASLt GELU epilogue on SM120 (#34350)
  _Files: `python/sglang/kernels/ops/diffusion/fused_linear_gelu.py`_
- **2026-08-12** [`a9a355774a`](https://github.com/sgl-project/sglang/commit/a9a355774a) [#34391](https://github.com/sgl-project/sglang/pull/34391)
  [diffusion] feat: support dynamically cpu offload components (#34391)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/lingbot_world.py` _+27 more__
- **2026-08-12** [`2be9773a21`](https://github.com/sgl-project/sglang/commit/2be9773a21) [#34497](https://github.com/sgl-project/sglang/pull/34497)
  [diffusion] doc: update cosmos3 edge and distilled cookbook (#34497)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`_
- **2026-08-12** [`4aff4b1822`](https://github.com/sgl-project/sglang/commit/4aff4b1822) [#34412](https://github.com/sgl-project/sglang/pull/34412)
  [Diffusion] Improve bit-exact fusion fallback diagnostics (#34412)
  _Files: `python/sglang/kernels/ops/diffusion/bitexact_gate.py`, `python/sglang/multimodal_gen/runtime/models/dits/ernie_image.py`, `test/registered/kernels/ops/diffusion/test_bitexact_gate.py`_
- **2026-08-12** [`3f9d184833`](https://github.com/sgl-project/sglang/commit/3f9d184833) [#34349](https://github.com/sgl-project/sglang/pull/34349)
  [Diffusion] Tune QK head LayerNorm for SM120 (#34349)
  _Files: `python/sglang/kernels/ops/diffusion/triton/layernorm_modulate.py`_
- **2026-08-12** [`f7b6800b22`](https://github.com/sgl-project/sglang/commit/f7b6800b22) [#31590](https://github.com/sgl-project/sglang/pull/31590)
  [diffusion] model: support cosmos3 edge and distilled (#31590)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`, `python/sglang/multimodal_gen/configs/sample/cosmos3.py`, `python/sglang/multimodal_gen/registry.py` _+9 more__
- **2026-08-12** [`81c88da1ab`](https://github.com/sgl-project/sglang/commit/81c88da1ab) [#34423](https://github.com/sgl-project/sglang/pull/34423)
  [diffusion] fix: nightly diffusion benchmark passes the retired --warmup flag (#34423)
  _Files: `scripts/ci/utils/diffusion/comparison_configs.json`, `scripts/ci/utils/diffusion/run_comparison.py`_
- **2026-08-12** [`a53d3636ce`](https://github.com/sgl-project/sglang/commit/a53d3636ce) [#32921](https://github.com/sgl-project/sglang/pull/32921)
  [diffusion][model] Add native SANA-Video T2V support (#32921)
  _Files: `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `python/sglang/multimodal_gen/configs/models/dits/__init__.py`, `python/sglang/multimodal_gen/configs/models/dits/sana_video.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/__init__.py` _+10 more__
- **2026-08-12** [`37c631ef23`](https://github.com/sgl-project/sglang/commit/37c631ef23) [#34314](https://github.com/sgl-project/sglang/pull/34314)
  [diffusion] Ideogram-4: fuse Qwen3-style RoPE and SwiGLU silu-mul (denoise -5.1% H100 / -4.7% H200, bit-exact) (#34314)
  _Files: `python/sglang/kernels/ops/diffusion/triton/silu_mul_bitexact.py`, `python/sglang/multimodal_gen/runtime/models/dits/ideogram.py`, `python/sglang/multimodal_gen/test/unit/test_ideogram_rope_swiglu_fusion.py`_
- **2026-08-12** [`b1b8ce715b`](https://github.com/sgl-project/sglang/commit/b1b8ce715b) [#34347](https://github.com/sgl-project/sglang/pull/34347)
  [Diffusion][MiniMax H3] Fix SM120 QKNorm+RoPE rounding (#34347)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/qknorm_rope.cuh`_
- **2026-08-11** [`546965fc72`](https://github.com/sgl-project/sglang/commit/546965fc72) [#34315](https://github.com/sgl-project/sglang/pull/34315)
  [diffusion] LTX-2: mount the bit-exact fused modulate at the 8 bare adaLN sites (ltx23-one-stage denoise -2.8% H100 / -2.6% H200) (#34315)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_modulate_mount.py`_
- **2026-08-11** [`071f0f1e9d`](https://github.com/sgl-project/sglang/commit/071f0f1e9d) [#34306](https://github.com/sgl-project/sglang/pull/34306)
  [diffusion] ERNIE-Image: fuse rotate-half RoPE + GELU-mul and hoist rope cos/sin (denoise -16.2% H100 / -12.7% H200, bit-exact) (#34306)
  _Files: `python/sglang/kernels/ops/activation/activation.py`, `python/sglang/kernels/ops/diffusion/triton/rope_rotate_half_bitexact.py`, `python/sglang/multimodal_gen/runtime/models/dits/ernie_image.py`, `python/sglang/multimodal_gen/test/unit/test_ernie_rope_geglu_fusion.py`_
- **2026-08-11** [`6f3fe13a9c`](https://github.com/sgl-project/sglang/commit/6f3fe13a9c) [#34364](https://github.com/sgl-project/sglang/pull/34364)
  [AMD] Install AITER's pinned Triton wheel in the ROCm 7.2 image (#34364)
  _Files: `docker/rocm.Dockerfile`_
- **2026-08-11** [`13aeb91b6e`](https://github.com/sgl-project/sglang/commit/13aeb91b6e) [#34358](https://github.com/sgl-project/sglang/pull/34358)
  [Fix] Update multimodal CUDA VMM helper import (#34358)
  _Files: `python/sglang/srt/multimodal/transport/memory_pool.py`_
- **2026-08-11** [`aeab1de1de`](https://github.com/sgl-project/sglang/commit/aeab1de1de) [#34256](https://github.com/sgl-project/sglang/pull/34256)
  [diffusion] optimization: support cuda graph for Pi-0.5 prefix encoding (#34256)
  _Files: `docs/cookbook/vla/OpenPI/Pi0.5.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/pi05.py`, `python/sglang/multimodal_gen/runtime/models/vlas/pi05_core.py`, `python/sglang/multimodal_gen/runtime/models/vlas/pi05_policy.py` _+4 more__
- **2026-08-11** [`ba5183fe10`](https://github.com/sgl-project/sglang/commit/ba5183fe10) [#34301](https://github.com/sgl-project/sglang/pull/34301)
  [diffusion] UX: fix CI server warmup progress logging (#34301)
  _Files: `python/sglang/multimodal_gen/runtime/server_warmup.py`, `python/sglang/multimodal_gen/test/unit/test_server_warmup_progress.py`_
- **2026-08-10** [`ec9babe36c`](https://github.com/sgl-project/sglang/commit/ec9babe36c) [#34294](https://github.com/sgl-project/sglang/pull/34294)
  [diffusion] fix: fix h3 rank-local fsdp qkv loading (#34294)
  _Files: `python/sglang/multimodal_gen/runtime/loader/rank_local_checkpoint.py`, `python/sglang/multimodal_gen/runtime/models/dits/minimax_h3.py`, `python/sglang/multimodal_gen/test/unit/test_fsdp_load.py`, `python/sglang/multimodal_gen/test/unit/test_minimax_h3_dit_contract.py`_
- **2026-08-10** [`d07ac32d05`](https://github.com/sgl-project/sglang/commit/d07ac32d05) [#34228](https://github.com/sgl-project/sglang/pull/34228)
  [diffusion] feat: support --served-model-name in sglang serve (#34228)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/api/openai_api.mdx`, `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `python/sglang/multimodal_gen/runtime/entrypoints/action/protocol.py` _+9 more__
- **2026-08-10** [`f5f0c3ee7a`](https://github.com/sgl-project/sglang/commit/f5f0c3ee7a) [#34183](https://github.com/sgl-project/sglang/pull/34183)
  [diffusion] Z-Image single-GPU BCG: fix the replay crash and make output bit-exact vs eager (#34183) (#34210)
  _Files: `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/model_padders/zimage.py`, `python/sglang/multimodal_gen/runtime/breakable_cuda_graph/runner.py`, `python/sglang/multimodal_gen/runtime/models/dits/zimage.py`, `python/sglang/multimodal_gen/test/unit/test_diffusion_bcg_padding.py`_
- **2026-08-10** [`fd3036523a`](https://github.com/sgl-project/sglang/commit/fd3036523a) [#34180](https://github.com/sgl-project/sglang/pull/34180)
  [diffusion] Clean up shared bitexact gates, helpers, and stale naming (#34180)
  _Files: `python/sglang/kernels/jit/csrc/diffusion/norm_scale_shift.cuh`, `python/sglang/kernels/ops/diffusion/__init__.py`, `python/sglang/kernels/ops/diffusion/bitexact_gate.py`, `python/sglang/kernels/ops/diffusion/norm_scale_shift_native.py` _+20 more__
- **2026-08-10** [`3e2a26708b`](https://github.com/sgl-project/sglang/commit/3e2a26708b) [#34248](https://github.com/sgl-project/sglang/pull/34248)
  [diffusion] chore: expose architecture config at the dit runtime boundary (#34248)
  _Files: `python/sglang/multimodal_gen/runtime/cache/spectrum.py`, `python/sglang/multimodal_gen/runtime/cache/teacache.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/base.py` _+19 more__
- **2026-08-10** [`4eaaeda004`](https://github.com/sgl-project/sglang/commit/4eaaeda004) [#34276](https://github.com/sgl-project/sglang/pull/34276)
  [CI] Build patched Docker images for both amd64 and arm64 (#34276)
  _Files: `.github/workflows/patch-docker-dev.yml`_
- **2026-08-10** [`443b62db57`](https://github.com/sgl-project/sglang/commit/443b62db57) [#33949](https://github.com/sgl-project/sglang/pull/33949)
  fix(vlm): stream-order cuda-ipc feature pool lifecycle and streamline multimodal transport module (#33949)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/models/kimi_k25.py`, `python/sglang/srt/models/kimi_k3.py`, `python/sglang/srt/models/qwen3_vl.py` _+14 more__
- **2026-08-10** [`955569a2dc`](https://github.com/sgl-project/sglang/commit/955569a2dc) [#34243](https://github.com/sgl-project/sglang/pull/34243)
  [diffusion] feat: expose cosmos3 policies through the Action API (#34243)
  _Files: `docs/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `python/sglang/multimodal_gen/benchmarks/bench_pi05_openpi.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py` _+17 more__
- **2026-08-10** [`0b6189d0e8`](https://github.com/sgl-project/sglang/commit/0b6189d0e8) [#34253](https://github.com/sgl-project/sglang/pull/34253)
  [CI] Add output_tag input to the Patch Docker Image workflow (#34253)
  _Files: `.github/workflows/patch-docker-dev.yml`_
- **2026-08-10** [`f2a4c4c847`](https://github.com/sgl-project/sglang/commit/f2a4c4c847) [#31843](https://github.com/sgl-project/sglang/pull/31843)
  [AMD] [CI] Enable 3 nested unit tests needing harness stub fixes (#31843)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/unit/progressive_resolution/test_progressive.py`, `python/sglang/multimodal_gen/test/unit/sana_wm/test_streaming_realtime_path.py`, `scripts/ci/utils/ci_coverage_report.py`_
- **2026-08-10** [`169783d42f`](https://github.com/sgl-project/sglang/commit/169783d42f) [#34173](https://github.com/sgl-project/sglang/pull/34173)
  [diffusion] chore: make torch.compile opt-in for speed mode (#34173)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/deployment_cookbook.mdx`, `python/sglang/multimodal_gen/configs/pipeline_configs/model_deployment_config.py`, `python/sglang/multimodal_gen/runtime/server_args/auto_tune.py` _+1 more__
- **2026-08-10** [`441910f926`](https://github.com/sgl-project/sglang/commit/441910f926) [#34172](https://github.com/sgl-project/sglang/pull/34172)
  [diffusion] LTX-2 quality=high fused RMSNorm+modulate + FFN GELU epilogue (H200 ltx23-one-stage denoise 45.85->43.24 s, ~matches torch.compile) (#34172)
  _Files: `python/sglang/kernels/ops/diffusion/ltx2_rmsnorm_modulate.py`, `python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `test/registered/kernels/ops/diffusion/test_ltx2_rms_norm_modulate.py`_
- **2026-08-10** [`56ef810cad`](https://github.com/sgl-project/sglang/commit/56ef810cad) [#34174](https://github.com/sgl-project/sglang/pull/34174)
  [diffusion] BCG: auto-capture the default warmup resolution instead of hard-requiring --warmup-resolutions (H200 SANA denoise 0.73->0.457 s with a single flag) (#34174)
  _Files: `python/sglang/multimodal_gen/runtime/server_args/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_

## Attention / FlashInfer  (76 commits)

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
- **2026-08-16** [`f7cb328eb7`](https://github.com/sgl-project/sglang/commit/f7cb328eb7) [#31324](https://github.com/sgl-project/sglang/pull/31324)
  [AMD] [GLM5] Skip DSA decode indexer when kv_len <= index_topk (dense k-only fast path) (#31324)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/shape_key.py`, `python/sglang/srt/model_executor/runner_utils/capture_mode.py`_
- **2026-08-16** [`5e73c89b34`](https://github.com/sgl-project/sglang/commit/5e73c89b34) [#35058](https://github.com/sgl-project/sglang/pull/35058)
  [Spec] Simplify compute_spec_v2_logprobs signature and skip identity gathers (#35058)
  _Files: `python/sglang/srt/layers/logprob_processor.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`, `python/sglang/srt/speculative/eagle_worker_common.py` _+3 more__
- **2026-08-16** [`4c51248427`](https://github.com/sgl-project/sglang/commit/4c51248427) [#35000](https://github.com/sgl-project/sglang/pull/35000)
  Support unified SWA page mapping in attention metadata (#35000)
  _Files: `python/sglang/kernels/ops/attention/metadata.py`_
- **2026-08-16** [`bae353ba55`](https://github.com/sgl-project/sglang/commit/bae353ba55) [#34982](https://github.com/sgl-project/sglang/pull/34982)
  [misc] Rename shared-read boundary to shared-read ends and fix wrapper delegation (#34982)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/hybrid_attn_backend.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` _+7 more__
- **2026-08-16** [`968b355f12`](https://github.com/sgl-project/sglang/commit/968b355f12) [#34991](https://github.com/sgl-project/sglang/pull/34991)
  vlm: streamline vision sdpa reshapes (#34991)
  _Files: `python/sglang/srt/layers/attention/vision.py`, `test/registered/unit/layers/attention/test_vision_backend_selection.py`_
- **2026-08-16** [`24ab8f9ed9`](https://github.com/sgl-project/sglang/commit/24ab8f9ed9) [#34474](https://github.com/sgl-project/sglang/pull/34474)
  [AMD] Qwen3.5: guard attn layers against empty DP-attention batch (#34474)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-08-16** [`4c0e85524d`](https://github.com/sgl-project/sglang/commit/4c0e85524d) [#30808](https://github.com/sgl-project/sglang/pull/30808)
  [AMD] [GLM5] Enable dense-MHA short-context prefill fallback on gfx950 (#30808)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`_
- **2026-08-16** [`d269a28b47`](https://github.com/sgl-project/sglang/commit/d269a28b47) [#34949](https://github.com/sgl-project/sglang/pull/34949)
  [diffusion] refactor: route minimax h3 vae attention through native backends (#34949)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_audio_vae/audio_vae.py`, `python/sglang/multimodal_gen/runtime/models/vaes/minimax_h3_video_vae/attention.py` _+6 more__
- **2026-08-16** [`d106e8b23a`](https://github.com/sgl-project/sglang/commit/d106e8b23a) [#34951](https://github.com/sgl-project/sglang/pull/34951)
  [diffusion] chore: use native ernie prompt enhancer (#34951)
  _Files: `docs/cookbook/diffusion/Ernie-Image/Ernie-Image.mdx`, `docs/docs/sglang-diffusion/models_with_pe.mdx`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/sdpa.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/pe_loader.py` _+2 more__
- **2026-08-15** [`4a6dc267e1`](https://github.com/sgl-project/sglang/commit/4a6dc267e1) [#34763](https://github.com/sgl-project/sglang/pull/34763)
  [Spec] Support mamba-radix-cache-strategy extra_buffer_lazy with DFLASH (#34763)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/dflash_info.py`, `test/registered/unit/spec/test_dflash_extra_buffer_lazy.py`_
- **2026-08-15** [`d22c4cc177`](https://github.com/sgl-project/sglang/commit/d22c4cc177) [#30024](https://github.com/sgl-project/sglang/pull/30024)
  [AMD] perf(sgl-kernel): default block_quota=16 for MLA page_first KV gather… (#30024)
  _Files: `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/aot/python/sgl_kernel/kvcacheio.py`_
- **2026-08-15** [`0f7aaceda5`](https://github.com/sgl-project/sglang/commit/0f7aaceda5) [#34916](https://github.com/sgl-project/sglang/pull/34916)
  [misc] Rename the WAR read-done fastpath to shared-read-done (#34916)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/model_runner.py` _+12 more__
- **2026-08-15** [`4d0c5a89af`](https://github.com/sgl-project/sglang/commit/4d0c5a89af) [#34837](https://github.com/sgl-project/sglang/pull/34837)
  [AMD] Add concat_and_cast_mha_k_pad_kernel to support 12-head and enable K3 aiter prefill kernel (#34837)
  _Files: `python/sglang/kernels/ops/kvcache/cache_ops.py`_
- **2026-08-15** [`e331baaaa8`](https://github.com/sgl-project/sglang/commit/e331baaaa8) [#34891](https://github.com/sgl-project/sglang/pull/34891)
  [diffusion] chore: scope attention backend fallback (#34891)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`, `python/sglang/multimodal_gen/test/unit/test_attention_backend_selector.py` _+1 more__
- **2026-08-15** [`f2ab6e306b`](https://github.com/sgl-project/sglang/commit/f2ab6e306b)
  config: the alias form of the runner-side instance read
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py` _+14 more__
- **2026-08-15** [`d13d5c03ab`](https://github.com/sgl-project/sglang/commit/d13d5c03ab)
  config: decisions keyed on the attention backend read the configured pair
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/layers/rotary_embedding/mrope.py` _+6 more__
- **2026-08-15** [`97279980cf`](https://github.com/sgl-project/sglang/commit/97279980cf)
  config: the last runner-side instance reads read the bags
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/model_runner.py` _+12 more__
- **2026-08-15** [`ab810e4052`](https://github.com/sgl-project/sglang/commit/ab810e4052)
  config: each runner carries its own linear-attn kernel choice
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py` _+6 more__
- **2026-08-15** [`6cbfa791d6`](https://github.com/sgl-project/sglang/commit/6cbfa791d6) [#34517](https://github.com/sgl-project/sglang/pull/34517)
  [AMD][Spec] Accelerate Qwen3.5 verification with grouped-head shared KV (#34517)
  _Files: `python/sglang/kernels/ops/attention/verify_mla.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `test/registered/attention/test_verify_shared_kv.py`_
- **2026-08-15** [`aeee1562e6`](https://github.com/sgl-project/sglang/commit/aeee1562e6) [#32593](https://github.com/sgl-project/sglang/pull/32593)
  [Kernel] Enable Helion backend for Kimi Delta-Attention (#32593)
  _Files: `benchmark/bench_linear_attention/bench_kda_decode.py`, `benchmark/bench_linear_attention/bench_kda_flashinfer_mtp.py`, `benchmark/bench_linear_attention/bench_kda_prefill_cutedsl.py`, `python/sglang/kernels/ops/attention/helion/__init__.py` _+12 more__
- **2026-08-15** [`a5ba081fbb`](https://github.com/sgl-project/sglang/commit/a5ba081fbb) [#34771](https://github.com/sgl-project/sglang/pull/34771)
  [Spec] Wire DFLASH aux-hidden capture into the Qwen3.5 text-only wrapper (#34771)
  _Files: `python/sglang/srt/models/qwen3_5_text.py`_
- **2026-08-14** [`a9654eacc1`](https://github.com/sgl-project/sglang/commit/a9654eacc1) [#33006](https://github.com/sgl-project/sglang/pull/33006)
  fix(dsa): use FlashInfer fused top-k for packed PAGED rows (#33006)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_topk_backend.py`, `test/registered/kernels/ops/attention/test_dsa_indexer.py`_
- **2026-08-14** [`5f2a6d6422`](https://github.com/sgl-project/sglang/commit/5f2a6d6422) [#34824](https://github.com/sgl-project/sglang/pull/34824)
  [diffusion] Fix symbolic replicated-mode counting under torch.compile (#34824)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/test/unit/test_usp_attention_kv_gather.py`_
- **2026-08-14** [`f2c84de022`](https://github.com/sgl-project/sglang/commit/f2c84de022) [#34816](https://github.com/sgl-project/sglang/pull/34816)
  [Perf] Publish the WAR read-done event at DSPARK verify (#34816)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/speculative/spec_info.py`_
- **2026-08-14** [`65d62109dd`](https://github.com/sgl-project/sglang/commit/65d62109dd) [#34741](https://github.com/sgl-project/sglang/pull/34741)
  [AMD] Fix Triton 3.7 gfx950 extend-attention spills (#34741)
  _Files: `python/sglang/kernels/ops/attention/extend_attention.py`, `test/registered/attention/test_triton_attention_kernels.py`_
- **2026-08-14** [`ba1d980b35`](https://github.com/sgl-project/sglang/commit/ba1d980b35) [#31856](https://github.com/sgl-project/sglang/pull/31856)
  [AMD] Accelerate AITER unified-attention decode with scaled FP8 Q (#31856)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/attention/test_aiter_fp8_q_unified_attention.py`_
- **2026-08-14** [`f2b2b567aa`](https://github.com/sgl-project/sglang/commit/f2b2b567aa) [#25855](https://github.com/sgl-project/sglang/pull/25855)
  perf(jit_kernel/deepseek_v4): optimize paged_mqa_metadata (#25855)
  _Files: `benchmark/kernels/bench_paged_mqa_metadata.py`, `python/sglang/kernels/jit/csrc/deepseek_v4/paged_mqa_metadata.cuh`, `python/sglang/kernels/ops/attention/dsv4/attn.py`, `test/registered/kernels/ops/attention/test_paged_mqa_metadata.py`_
- **2026-08-14** [`704e512836`](https://github.com/sgl-project/sglang/commit/704e512836) [#34592](https://github.com/sgl-project/sglang/pull/34592)
  [GDN] Honor configured linear-attn verify backend in the kernel dispatcher (#34592)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`_
- **2026-08-13** [`54c44fef73`](https://github.com/sgl-project/sglang/commit/54c44fef73) [#33857](https://github.com/sgl-project/sglang/pull/33857)
  [Perf] Skip trivial DSV4 nonpaged indexer logits (#33857)
  _Files: `python/sglang/srt/layers/attention/dsv4/indexer.py`, `test/registered/unit/layers/test_dsv4_nonpaged_indexer.py`_
- **2026-08-13** [`81fe452810`](https://github.com/sgl-project/sglang/commit/81fe452810) [#34651](https://github.com/sgl-project/sglang/pull/34651)
  [DCP] Share one pack kernel between both a2a backends (#34651)
  _Files: `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/srt/layers/dcp/comm.py`, `test/registered/kernels/test_dcp_lse_combine.py`_
- **2026-08-13** [`34206c0017`](https://github.com/sgl-project/sglang/commit/34206c0017) [#34597](https://github.com/sgl-project/sglang/pull/34597)
  [AMD] Run V4 MTP target-verify through the decode kernel (#34597)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-08-13** [`dbebc1deb4`](https://github.com/sgl-project/sglang/commit/dbebc1deb4) [#32755](https://github.com/sgl-project/sglang/pull/32755)
  [Perf] Occupancy tuning for DSA indexer fp8-quant Q kernel (#32755)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/main_norm_rope.cuh`, `test/registered/kernels/ops/attention/test_dsv4_indexer_quant.py`_
- **2026-08-13** [`c034120cb8`](https://github.com/sgl-project/sglang/commit/c034120cb8) [#29202](https://github.com/sgl-project/sglang/pull/29202)
  [AMD] Enable draft-extend CUDA graph and reduce bubble for MTP (#29202)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/managers/scheduler_components/profiler_manager.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-08-13** [`889c2f31aa`](https://github.com/sgl-project/sglang/commit/889c2f31aa) [#32991](https://github.com/sgl-project/sglang/pull/32991)
  feat(attention): add architecture-owned SM12x FA4 kernels (#32991)
  _Files: `python/sglang/kernels/ops/attention/fa4_sm120/__init__.py`, `python/sglang/kernels/ops/attention/fa4_sm120/dispatch.py`, `python/sglang/kernels/ops/attention/fa4_sm120/flash_fwd.py`, `python/sglang/kernels/ops/attention/fa4_sm120/flash_fwd_decode.py` _+12 more__
- **2026-08-13** [`6a5a9eccaa`](https://github.com/sgl-project/sglang/commit/6a5a9eccaa) [#34042](https://github.com/sgl-project/sglang/pull/34042)
  add flashinfer cute-dsl backend for mxfp8 gemm (#34042)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py` _+2 more__
- **2026-08-13** [`aefe2d0207`](https://github.com/sgl-project/sglang/commit/aefe2d0207) [#34642](https://github.com/sgl-project/sglang/pull/34642)
  Revert "[Kimi K3] Fuse MLA gate projection into QKV-A GEMM" (#34642)
  _Files: `python/sglang/kernels/jit/csrc/gemm/dsv3_fused_a_gemm.cuh`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/models/test_kimi_k3_mla_gate_fusion.py`_
- **2026-08-12** [`6c6294b7be`](https://github.com/sgl-project/sglang/commit/6c6294b7be) [#34614](https://github.com/sgl-project/sglang/pull/34614)
  [DCP] Fuse the a2a pack/unpack copies in the MLA LSE reduce (#34614)
  _Files: `python/sglang/kernels/ops/attention/__init__.py`, `python/sglang/kernels/ops/attention/dcp_kernels.py`, `python/sglang/srt/layers/dcp/comm.py`, `test/registered/kernels/test_dcp_lse_combine.py`_
- **2026-08-12** [`4f883636a2`](https://github.com/sgl-project/sglang/commit/4f883636a2) [#27689](https://github.com/sgl-project/sglang/pull/27689)
  [Perf] FlashInfer MLA: remove blocking D2H in spec-decode plan (#27689)
  _Files: `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`_
- **2026-08-12** [`b501311fa1`](https://github.com/sgl-project/sglang/commit/b501311fa1) [#33623](https://github.com/sgl-project/sglang/pull/33623)
  [Kimi K3] Fuse MLA gate projection into QKV-A GEMM (#33623)
  _Files: `python/sglang/kernels/jit/csrc/gemm/dsv3_fused_a_gemm.cuh`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/unit/models/test_kimi_k3_mla_gate_fusion.py`_
- **2026-08-12** [`0dab252ffc`](https://github.com/sgl-project/sglang/commit/0dab252ffc) [#34524](https://github.com/sgl-project/sglang/pull/34524)
  Fix DFlash sliding attention causality defaults (#34524)
  _Files: `python/sglang/srt/configs/muse_glimmer.py`, `python/sglang/srt/models/dflash.py`_
- **2026-08-12** [`cac3269305`](https://github.com/sgl-project/sglang/commit/cac3269305) [#32227](https://github.com/sgl-project/sglang/pull/32227)
  [XPU] Fix NemotronH (hybrid mamba2) launch on --device xpu (#32227)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/server_args.py`_
- **2026-08-12** [`30cb848d4b`](https://github.com/sgl-project/sglang/commit/30cb848d4b) [#34443](https://github.com/sgl-project/sglang/pull/34443)
  [Bugfix][DSA] Fix num_splits "(b+1)" crash on prefill-CP speculative decode (#34443)
  _Files: `python/sglang/srt/layers/attention/dsa/utils.py`_
- **2026-08-11** [`c7c03ec53b`](https://github.com/sgl-project/sglang/commit/c7c03ec53b) [#30700](https://github.com/sgl-project/sglang/pull/30700)
  [NVIDIA] Add flashinfer MNNVL backend for allreduce only (#30700)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/distributed/bootstrap.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/layers/communicator.py` _+3 more__
- **2026-08-11** [`fde9ad2531`](https://github.com/sgl-project/sglang/commit/fde9ad2531) [#34262](https://github.com/sgl-project/sglang/pull/34262)
  [Feature] Add Muse Glimmer model support (#34262)
  _Files: `python/sglang/benchmark/utils.py`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py` _+43 more__
- **2026-08-11** [`2c07ca5e8d`](https://github.com/sgl-project/sglang/commit/2c07ca5e8d) [#33075](https://github.com/sgl-project/sglang/pull/33075)
  [Fix] Allow flashinfer_sparse_mla DSA backend for HiSparse on SM120 FP8 KV (#33075)
  _Files: `docs/docs/advanced_features/hisparse_guide.mdx`, `python/sglang/srt/arg_groups/hisparse_hook.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-08-11** [`c58953d90a`](https://github.com/sgl-project/sglang/commit/c58953d90a) [#32208](https://github.com/sgl-project/sglang/pull/32208)
  O(1) slot allocation in ReqToTokenPool.alloc() (#32208)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`, `test/registered/unit/mem_cache/test_dllm_fdfo_kv_reuse.py`_
- **2026-08-11** [`a3bd7d9401`](https://github.com/sgl-project/sglang/commit/a3bd7d9401) [#34372](https://github.com/sgl-project/sglang/pull/34372)
  Bump CuTeDSL to 4.6.2 (#34372)
  _Files: `python/pyproject.toml`, `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py`, `python/sglang/kernels/ops/attention/flash_attn/cute/pyproject.toml`_
- **2026-08-11** [`e74ea5b1d7`](https://github.com/sgl-project/sglang/commit/e74ea5b1d7) [#31105](https://github.com/sgl-project/sglang/pull/31105)
  [ROCm/gfx95] Fix fp8 per-channel attention for Kimi-K2.7-code-mxfp4 o… (#31105)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha_rocm.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla_rocm.py`, `python/sglang/srt/models/deepseek_common/deepseek_weight_loader.py`, `python/sglang/srt/models/deepseek_common/utils.py` _+3 more__
- **2026-08-11** [`1c06c160f9`](https://github.com/sgl-project/sglang/commit/1c06c160f9) [#34363](https://github.com/sgl-project/sglang/pull/34363)
  [Docs] Add Ling-3.0-flash INT4 and MXFP4 recipes (#34363)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-flash.mdx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash-benchmarks.jsx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-flash.jsx`_
- **2026-08-11** [`9d4be40124`](https://github.com/sgl-project/sglang/commit/9d4be40124) [#33865](https://github.com/sgl-project/sglang/pull/33865)
  Fix DSpark + DeepSeek V4 prefill CP compatibility (#33865)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/model_executor/runner/eager_runner.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_dspark.py` _+1 more__
- **2026-08-11** [`b3c02cbce7`](https://github.com/sgl-project/sglang/commit/b3c02cbce7) [#34338](https://github.com/sgl-project/sglang/pull/34338)
  [perf] Collapse the DP attention scheduler sync to a single D2H copy (#34338)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py`_
- **2026-08-11** [`585c3c6816`](https://github.com/sgl-project/sglang/commit/585c3c6816) [#34336](https://github.com/sgl-project/sglang/pull/34336)
  [Refactor] Split the FlashInfer autotune dummy-run flag from the LM-head policy (#34336)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/model_executor/runner/base_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/flashinfer_autotune.py` _+4 more__
- **2026-08-11** [`704808ed27`](https://github.com/sgl-project/sglang/commit/704808ed27) [#34148](https://github.com/sgl-project/sglang/pull/34148)
  [MiniMax-H3] SubBlock: training-free block-sparse attention for the DiT (#34148)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/README.md`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/__init__.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/kernels.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/subblock_sparse/router.py` _+4 more__
- **2026-08-11** [`d59c1ddf70`](https://github.com/sgl-project/sglang/commit/d59c1ddf70) [#33912](https://github.com/sgl-project/sglang/pull/33912)
  fix(dflash): account for DCP in draft KV pool sizing (#33912)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`, `test/registered/unit/model_executor/test_pool_configurator.py`_
- **2026-08-11** [`0967885121`](https://github.com/sgl-project/sglang/commit/0967885121) [#34240](https://github.com/sgl-project/sglang/pull/34240)
  [DCP] Drop two per-layer launches from the MLA target-verify path (#34240)
  _Files: `python/sglang/srt/layers/attention/cutedsl_mla_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `test/registered/dcp/test_dcp_layout_unit.py` _+1 more__
- **2026-08-11** [`2d5009d130`](https://github.com/sgl-project/sglang/commit/2d5009d130) [#33662](https://github.com/sgl-project/sglang/pull/33662)
  [DSV4] Avoid host syncs in EAGLE prefill (#33662)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/sparse_prefill_utils.py`, `python/sglang/srt/speculative/eagle_utils.py`_
- **2026-08-11** [`7c7326ccb3`](https://github.com/sgl-project/sglang/commit/7c7326ccb3) [#31700](https://github.com/sgl-project/sglang/pull/31700)
  Fix DeepSeek-V4/DeepSeek-V4-Pro DP-attention gather semantics (#31700)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_nextn.py`_
- **2026-08-10** [`8a7c8a72d6`](https://github.com/sgl-project/sglang/commit/8a7c8a72d6) [#33517](https://github.com/sgl-project/sglang/pull/33517)
  Fix NaN logits from deterministic Triton extend on the unified memory pool (#33517)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `test/registered/attention/test_unified_memory_deterministic.py`_
- **2026-08-10** [`b86c90215f`](https://github.com/sgl-project/sglang/commit/b86c90215f) [#34323](https://github.com/sgl-project/sglang/pull/34323)
  [Docs] Muse Glimmer cookbook: drop --speculative-dflash-block-size 5 (#34323)
  _Files: `docs/src/snippets/configs/meta-models/muse-glimmer.jsx`_
- **2026-08-10** [`733c05c887`](https://github.com/sgl-project/sglang/commit/733c05c887) [#31847](https://github.com/sgl-project/sglang/pull/31847)
  [spec decoding] support inkling dspark (#31847)
  _Files: `python/sglang/kernels/ops/mamba/mamba_state_scatter_triton.py`, `python/sglang/kernels/ops/speculative/dspark/fused_kv_write.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/srt/models/dspark.py` _+2 more__
- **2026-08-10** [`7738062294`](https://github.com/sgl-project/sglang/commit/7738062294) [#33974](https://github.com/sgl-project/sglang/pull/33974)
  [unified memory] Support DSPARK speculative decoding + fix two NaN root causes (page hand-out zeroing, CuTe int32 slot-stride wrap) (#33974)
  _Files: `python/sglang/kernels/ops/kimi_k3/kda_decode_mtp.py`, `python/sglang/kernels/ops/kvcache/zero_pages.py`, `python/sglang/kernels/ops/mamba/mamba_state_scatter_triton.py`, `python/sglang/srt/environ.py` _+9 more__
- **2026-08-10** [`0977b22431`](https://github.com/sgl-project/sglang/commit/0977b22431) [#34261](https://github.com/sgl-project/sglang/pull/34261)
  [AMD] Restore K3 MLA verify kernel path blocked by can_handle() guard (#34261)
  _Files: `python/sglang/kernels/ops/attention/verify_mla.py`_
- **2026-08-10** [`b51bf9ec9e`](https://github.com/sgl-project/sglang/commit/b51bf9ec9e) [#34234](https://github.com/sgl-project/sglang/pull/34234)
  [Spec] Budget the DFLASH draft KV pool from its own attention geometry (#34234)
  _Files: `python/sglang/srt/mem_cache/kv_cache_dtype.py`, `python/sglang/srt/model_executor/model_runner_components/spec_aux_hidden_state.py`, `python/sglang/srt/model_executor/pool_configurator.py`, `python/sglang/srt/speculative/dflash_utils.py` _+1 more__
- **2026-08-10** [`06f32bab6b`](https://github.com/sgl-project/sglang/commit/06f32bab6b) [#33661](https://github.com/sgl-project/sglang/pull/33661)
  [BCG][5/N] MLA Fully Support (#33661)
  _Files: `python/sglang/kernels/ops/attention/flash_attn/cute/interface.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+3 more__
- **2026-08-10** [`aea78d1e73`](https://github.com/sgl-project/sglang/commit/aea78d1e73) [#34217](https://github.com/sgl-project/sglang/pull/34217)
  [misc] Pass FP8 scales in FlashInfer SWA prefill, autotune fp8 on SM120, and tighten `is_image_understandable_model` (#34217)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/constrained/xgrammar_backend.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/attention_kv_cache.py` _+8 more__
- **2026-08-10** [`2969ab3d41`](https://github.com/sgl-project/sglang/commit/2969ab3d41) [#34166](https://github.com/sgl-project/sglang/pull/34166)
  [MLX] Window-bounded SWA KV storage and in-graph sampling (#34166)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/constrained/xgrammar_backend.py`, `python/sglang/srt/hardware_backend/mlx/aot.py` _+23 more__
- **2026-08-10** [`accc51c6db`](https://github.com/sgl-project/sglang/commit/accc51c6db) [#34167](https://github.com/sgl-project/sglang/pull/34167)
  [DSA] Fix top-k v2 dropping non-primary ranks' output on CUDA 13.1+ (root cause for #33835) (#34167)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/kernels/jit/csrc/deepseek_v4/topk_v2.cuh`, `python/sglang/kernels/jit/include/sgl_kernel/deepseek_v4/topk_impl.cuh`, `python/sglang/kernels/ops/attention/dsv4/topk.py`_
- **2026-08-10** [`ee3ee8393c`](https://github.com/sgl-project/sglang/commit/ee3ee8393c) [#34161](https://github.com/sgl-project/sglang/pull/34161)
  fix: preserve GQA head mapping in Triton DCP prefill (#34161)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `test/registered/dcp/test_dcp_layout_unit.py`_
- **2026-08-10** [`553dc0f936`](https://github.com/sgl-project/sglang/commit/553dc0f936) [#30050](https://github.com/sgl-project/sglang/pull/30050)
  [MLX] Support gpt-oss: sliding-window attention, attention sinks, sm_scale (#30050)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/hardware_backend/mlx/aot.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/__init__.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/attention_contract.py` _+8 more__

## MoE / Expert Parallel  (41 commits)

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
- **2026-08-16** [`f61f584347`](https://github.com/sgl-project/sglang/commit/f61f584347) [#34998](https://github.com/sgl-project/sglang/pull/34998)
  Add explicit EPLB balancedness reporting modes (#34998)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/argparse_actions.py` _+6 more__
- **2026-08-16** [`6ab4b99bc2`](https://github.com/sgl-project/sglang/commit/6ab4b99bc2) [#34962](https://github.com/sgl-project/sglang/pull/34962)
  [Quantization] Fix GPTQ scheme attachment broken by LinearBase.scheme default (#34962)
  _Files: `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/gptq/gptq.py`, `python/sglang/srt/layers/vocab_parallel_embedding.py` _+1 more__
- **2026-08-16** [`2ee0d38a85`](https://github.com/sgl-project/sglang/commit/2ee0d38a85) [#34663](https://github.com/sgl-project/sglang/pull/34663)
  [diffusion] chore: refresh docs, retire stale knobs, and fix nightly attribution (#34663)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `docs/cookbook/base/benchmarks/diffusion_model_benchmark.mdx`, `docs/cookbook/diffusion/FLUX/FLUX.mdx`, `docs/cookbook/diffusion/LTX/LTX2 & LTX2.3.mdx` _+17 more__
- **2026-08-16** [`56a759cffc`](https://github.com/sgl-project/sglang/commit/56a759cffc) [#34509](https://github.com/sgl-project/sglang/pull/34509)
  [JIT Kernel] Migrate moe_topk_softmax from AOT to JIT (#34509)
  _Files: `python/sglang/kernels/jit/csrc/moe/moe_topk_softmax.cuh`, `python/sglang/kernels/ops/moe/__init__.py`, `python/sglang/kernels/ops/moe/moe_topk_softmax.py`, `test/registered/kernels/benchmark/moe/bench_moe_topk_softmax.py` _+1 more__
- **2026-08-16** [`0da87024d3`](https://github.com/sgl-project/sglang/commit/0da87024d3) [#30318](https://github.com/sgl-project/sglang/pull/30318)
  [NPU] Add mxfp4-w4a8 MOE Quantization Support for NPU (#30318)
  _Files: `docs/docs/advanced_features/quantization.mdx`, `docs/docs/hardware-platforms/ascend-npus/optimization/quantization.mdx`, `python/sglang/srt/hardware_backend/npu/quantization/moe_methods.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py` _+2 more__
- **2026-08-16** [`66de161976`](https://github.com/sgl-project/sglang/commit/66de161976) [#32746](https://github.com/sgl-project/sglang/pull/32746)
  [Fix][AMD] MoRI EP: drop record_stream in TBO dispatch/combine (HSA out-of-resources) (#32746)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`_
- **2026-08-16** [`6314e9e4f5`](https://github.com/sgl-project/sglang/commit/6314e9e4f5) [#31794](https://github.com/sgl-project/sglang/pull/31794)
  [AMD][Fix] Qwen3.5: guard zero-grid launch in fused_qk_gemma_rmsnorm(_with_gate) (HIP invalid configuration on idle DP rank) (#31794)
  _Files: `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/models/qwen2_moe.py` _+1 more__
- **2026-08-15** [`7769f54feb`](https://github.com/sgl-project/sglang/commit/7769f54feb) [#34883](https://github.com/sgl-project/sglang/pull/34883)
  [Kimi-K3] Use explicit SiTU activation for MegaMoE (#34883)
  _Files: `python/pyproject.toml`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/models/kimi_k3.py`, `test/registered/models_e2e/test_kimi_k3_b300.py`_
- **2026-08-15** [`3adbbec2fd`](https://github.com/sgl-project/sglang/commit/3adbbec2fd) [#34789](https://github.com/sgl-project/sglang/pull/34789)
  [MoE] Route every trtllm-gen MoE call site through one PDL guard (#34789)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/layers/quantization/mxfp4_flashinfer_trtllm_moe.py`_
- **2026-08-15** [`bc7e3ba66c`](https://github.com/sgl-project/sglang/commit/bc7e3ba66c) [#29328](https://github.com/sgl-project/sglang/pull/29328)
  [AMD][Quantization] Online MXFP4 quantization 4/N - NVFP4 to MXFP4 Online Requantization on AMD GPUs (#29328)
  _Files: `docs/docs/advanced_features/quantization.mdx`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/base_config.py` _+10 more__
- **2026-08-15** [`6eb941a34c`](https://github.com/sgl-project/sglang/commit/6eb941a34c) [#34844](https://github.com/sgl-project/sglang/pull/34844)
  [Spec] Support MegaMoE for DSpark under dp attention (#34844)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `test/registered/spec/dspark/test_dspark_draft_path_default.py`_
- **2026-08-14** [`03c1d58112`](https://github.com/sgl-project/sglang/commit/03c1d58112) [#34150](https://github.com/sgl-project/sglang/pull/34150)
  perf: add H200 Triton MoE configs for E256 N512 (#34150)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=256,N=512,device_name=NVIDIA_H200.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_7_1/E=256,N=512,device_name=NVIDIA_H200_down.json`_
- **2026-08-14** [`d8399af70c`](https://github.com/sgl-project/sglang/commit/d8399af70c) [#34810](https://github.com/sgl-project/sglang/pull/34810)
  fix(qwen3): support DeepEP-class backends and early EPLB state (#34810)
  _Files: `python/sglang/srt/models/qwen3_moe.py`_
- **2026-08-14** [`b95a746948`](https://github.com/sgl-project/sglang/commit/b95a746948) [#32944](https://github.com/sgl-project/sglang/pull/32944)
  [MoE] Fuse swiglu moe up gemm epilogue (#32944)
  _Files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py` _+2 more__
- **2026-08-14** [`240a12b302`](https://github.com/sgl-project/sglang/commit/240a12b302) [#28666](https://github.com/sgl-project/sglang/pull/28666)
  [AMD] Fuse shared_expert_gate GEMV into the MoE append kernel (HIP/aiter) (#28666)
  _Files: `python/sglang/kernels/ops/moe/fused_moe_triton_kernels.py`, `python/sglang/srt/models/qwen2_moe.py`, `test/registered/amd/accuracy/mi35x/test_qwen35_mxfp4_eval_mi35x.py`, `test/registered/moe/test_fused_append_shared_experts.py`_
- **2026-08-14** [`85cdf1178d`](https://github.com/sgl-project/sglang/commit/85cdf1178d) [#34309](https://github.com/sgl-project/sglang/pull/34309)
  [CI] Prune redundant CPU test overhead (#34309)
  _Files: `.claude/rules/unit-test-admission.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `.github/workflows/lint.yml`, `.pre-commit-config.yaml` _+74 more__
- **2026-08-14** [`9d34c2809f`](https://github.com/sgl-project/sglang/commit/9d34c2809f) [#28354](https://github.com/sgl-project/sglang/pull/28354)
  [FlashInfer v0.6.16] Support FlashInfer CuTe DSL NVFP4 MoE quantization (#28354)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/environ.py` _+10 more__
- **2026-08-13** [`b7f87a2513`](https://github.com/sgl-project/sglang/commit/b7f87a2513) [#34421](https://github.com/sgl-project/sglang/pull/34421)
  [AMD][Perf] Fuse GatedDeltaNet QKVZBA split/reshape/cat into a single Triton kernel for Qwen3.5-architecture MoE on HIP (#34421)
  _Files: `python/sglang/kernels/ops/attention/triton_gdn_fused_proj.py`, `python/sglang/srt/models/qwen3_5.py`_
- **2026-08-13** [`3f6ef01322`](https://github.com/sgl-project/sglang/commit/3f6ef01322) [#31956](https://github.com/sgl-project/sglang/pull/31956)
  Optimize MiniMax-M2.7 on CPU (#31956)
  _Files: `python/sglang/kernels/aot/csrc/cpu/norm.cpp`, `python/sglang/kernels/aot/csrc/cpu/topk.cpp`, `python/sglang/kernels/aot/csrc/cpu/torch_extension_cpu.cpp`, `python/sglang/srt/layers/moe/topk.py` _+4 more__
- **2026-08-13** [`ef7208d41d`](https://github.com/sgl-project/sglang/commit/ef7208d41d) [#33559](https://github.com/sgl-project/sglang/pull/33559)
  [kernel] add triton moe TMA up support (#33559)
  _Files: `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton_sep.py`, `python/sglang/srt/layers/moe/moe_runner/triton.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=512,N=128,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=512,N=128,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128]_down.json` _+1 more__
- **2026-08-13** [`8761b971f1`](https://github.com/sgl-project/sglang/commit/8761b971f1) [#34637](https://github.com/sgl-project/sglang/pull/34637)
  [CI] Fix nightly test failures (#34637)
  _Files: `python/sglang/test/test_utils.py`, `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`_
- **2026-08-13** [`bca8ed4afc`](https://github.com/sgl-project/sglang/commit/bca8ed4afc) [#32941](https://github.com/sgl-project/sglang/pull/32941)
  [minimax m3][npu]Adaptation of Minimax M3(w8a8) for NPU platforms [1/2] (#32941)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `python/sglang/srt/hardware_backend/npu/modules/minimax_m3_processor.py`, `python/sglang/srt/hardware_backend/npu/moe/activation.py` _+14 more__
- **2026-08-12** [`2b4381956f`](https://github.com/sgl-project/sglang/commit/2b4381956f) [#33793](https://github.com/sgl-project/sglang/pull/33793)
  fix(glm5.2): restrict MoE weights to local PP layers (#33793)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-08-12** [`197832bcf5`](https://github.com/sgl-project/sglang/commit/197832bcf5) [#33465](https://github.com/sgl-project/sglang/pull/33465)
  [Kimi-K3][NPU]  Support Kimi-K3 on NPU (#33465)
  _Files: `python/sglang/kernels/ops/elementwise/add3.py`, `python/sglang/kernels/ops/kimi_k3/__init__.py`, `python/sglang/kernels/ops/kimi_k3/mla_output_gate.py`, `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py` _+20 more__
- **2026-08-12** [`00e57d74f0`](https://github.com/sgl-project/sglang/commit/00e57d74f0) [#33997](https://github.com/sgl-project/sglang/pull/33997)
  Bump FlashInfer to 0.6.17 and remove Kimi K3 workarounds (#33997)
  _Files: `docker/Dockerfile`, `docker/kimi_k3/flashinfer-perkz-dcp-0.6.15.txt`, `docker/kimi_k3/kimi_k3_cu12.Dockerfile`, `docker/kimi_k3/kimi_k3_cu13.Dockerfile` _+15 more__
- **2026-08-12** [`2d76d537e5`](https://github.com/sgl-project/sglang/commit/2d76d537e5) [#33945](https://github.com/sgl-project/sglang/pull/33945)
  feat: support deterministic FA4 for GLM-4.7-Flash (#33945)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/overrides.py`, `python/sglang/srt/layers/quantization/unquant.py`, `python/sglang/srt/server_args.py` _+2 more__
- **2026-08-12** [`a2d723820e`](https://github.com/sgl-project/sglang/commit/a2d723820e) [#34401](https://github.com/sgl-project/sglang/pull/34401)
  [diffusion] fix: fix model-driven dit layerwise offload auto policy (#34401)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/lingbot_video_moe.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/lingbot_world.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/model_deployment_config.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/mova.py` _+10 more__
- **2026-08-11** [`d82a1d4802`](https://github.com/sgl-project/sglang/commit/d82a1d4802) [#33905](https://github.com/sgl-project/sglang/pull/33905)
  [XPU] Pad MoE expert weight row stride to avoid L3 aliasing (#33905)
  _Files: `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/unquant.py`, `test/registered/xpu/test_moe_ld_padding.py`_
- **2026-08-11** [`dd8c5849af`](https://github.com/sgl-project/sglang/commit/dd8c5849af) [#34249](https://github.com/sgl-project/sglang/pull/34249)
  [diffusion] refactor: move dit execution capabilities to runtime models (#34249)
  _Files: `python/sglang/multimodal_gen/configs/models/base.py`, `python/sglang/multimodal_gen/configs/models/bridges/mova_dual_tower.py`, `python/sglang/multimodal_gen/configs/models/dits/base.py`, `python/sglang/multimodal_gen/configs/models/dits/cosmos3video.py` _+44 more__
- **2026-08-11** [`a58fa0388e`](https://github.com/sgl-project/sglang/commit/a58fa0388e) [#33669](https://github.com/sgl-project/sglang/pull/33669)
  [Fix] Correct W4AFP8 DeepEP scaling and mode-specific dtypes (#33669)
  _Files: `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/layers/quantization/w4afp8.py` _+2 more__
- **2026-08-11** [`dd20826e0a`](https://github.com/sgl-project/sglang/commit/dd20826e0a) [#34220](https://github.com/sgl-project/sglang/pull/34220)
  [AMD] Preserve the AITER expert mask across torch_memory_saver pause/resume (#34220)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/utils/weight_checker.py`_
- **2026-08-11** [`b498f46271`](https://github.com/sgl-project/sglang/commit/b498f46271) [#34326](https://github.com/sgl-project/sglang/pull/34326)
  [CI] Add MegaMoE runner compatibility alias (#34326)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/server_args.py`_
- **2026-08-11** [`df986c4d5e`](https://github.com/sgl-project/sglang/commit/df986c4d5e) [#34199](https://github.com/sgl-project/sglang/pull/34199)
  Consolidate CUDA VMM allocation helpers (#34199)
  _Files: `python/sglang/srt/cuda_vmm_utils.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `python/sglang/srt/layers/moe/dwdp/layout.py` _+9 more__
- **2026-08-10** [`e226bb711c`](https://github.com/sgl-project/sglang/commit/e226bb711c) [#33962](https://github.com/sgl-project/sglang/pull/33962)
  enable TRT-LLM for MiniMax M3 by preserving SwiGLU params (#33962)
  _Files: `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py` _+4 more__
- **2026-08-10** [`449f0da78f`](https://github.com/sgl-project/sglang/commit/449f0da78f) [#33808](https://github.com/sgl-project/sglang/pull/33808)
  [Intel GPU] DeepSeek V4 15/N: Add silu_and_mul_clamp support to triton fused_moe for XPU (#33808)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`_
- **2026-08-10** [`5d85f25f75`](https://github.com/sgl-project/sglang/commit/5d85f25f75) [#32229](https://github.com/sgl-project/sglang/pull/32229)
  fix(minimax): use routed TRT-LLM for NVFP4 MoE auto on SM100 (#32229)
  _Files: `python/sglang/srt/arg_groups/overrides.py`, `test/registered/unit/test_model_overrides.py`_

## KV Cache / Memory  (29 commits)

- **2026-08-17** [`43226af812`](https://github.com/sgl-project/sglang/commit/43226af812) [#34519](https://github.com/sgl-project/sglang/pull/34519)
  fix(hicache): limit load-back pending to write-back (#34519)
  _Files: `python/sglang/srt/mem_cache/unified_cache/unified_tree_core.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-08-16** [`ace7314173`](https://github.com/sgl-project/sglang/commit/ace7314173) [#35030](https://github.com/sgl-project/sglang/pull/35030)
  Add bit-exact guard for extra_buffer_lazy (#35030)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_hybrid_bitexact.py`_
- **2026-08-16** [`4654b927eb`](https://github.com/sgl-project/sglang/commit/4654b927eb) [#33998](https://github.com/sgl-project/sglang/pull/33998)
  [HiCache] Optimize LogicalHostPool free-list release (#33998)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`, `test/registered/unit/mem_cache/test_mem_pool_host.py`_
- **2026-08-16** [`0f706c33d2`](https://github.com/sgl-project/sglang/commit/0f706c33d2) [#34870](https://github.com/sgl-project/sglang/pull/34870)
  Fix swa eviction frontier for bigram keys (#34870)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-08-15** [`dd458f3212`](https://github.com/sgl-project/sglang/commit/dd458f3212) [#34963](https://github.com/sgl-project/sglang/pull/34963)
  Fix dsv4 kl test timeout (#34963)
  _Files: `.github/workflows/pr-test-extra.yml`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dsv4.py`_
- **2026-08-15** [`fb97be4359`](https://github.com/sgl-project/sglang/commit/fb97be4359) [#33604](https://github.com/sgl-project/sglang/pull/33604)
  Fix Whisper transcription for audio over 30 seconds (#33604)
  _Files: `python/sglang/srt/entrypoints/openai/audio_chunking.py`, `python/sglang/srt/entrypoints/openai/serving_transcription.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/base.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/whisper.py` _+5 more__
- **2026-08-14** [`41cd5a7189`](https://github.com/sgl-project/sglang/commit/41cd5a7189) [#34560](https://github.com/sgl-project/sglang/pull/34560)
  [Fix] Fix Qwen3.5 MTP startup with HiCache (#34560)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `test/registered/hicache/test_qwen35_hicache.py`, `test/registered/unit/configs/test_model_config.py` _+1 more__
- **2026-08-14** [`7562e741e2`](https://github.com/sgl-project/sglang/commit/7562e741e2) [#34729](https://github.com/sgl-project/sglang/pull/34729)
  Retain SWA down to the last state checkpoint (#34729)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py` _+2 more__
- **2026-08-14** [`c20aceeb88`](https://github.com/sgl-project/sglang/commit/c20aceeb88) [#34808](https://github.com/sgl-project/sglang/pull/34808)
  Fix mamba checkpoint depth under dcp (#34808)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/unified_cache/components/mamba_component.py`, `python/sglang/srt/runtime_context.py`, `test/registered/unit/managers/test_mamba_checkpoint_depth.py` _+1 more__
- **2026-08-14** [`1a178f7c7c`](https://github.com/sgl-project/sglang/commit/1a178f7c7c) [#31574](https://github.com/sgl-project/sglang/pull/31574)
  [EPD] Batch embedding cache host-device range copies (#31574)
  _Files: `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/csrc/kvcacheio/transfer.cu`, `python/sglang/kernels/aot/include/sgl_kernel_ops.h`, `python/sglang/kernels/aot/python/sgl_kernel/kvcacheio.py` _+3 more__
- **2026-08-14** [`18107e38d2`](https://github.com/sgl-project/sglang/commit/18107e38d2) [#34823](https://github.com/sgl-project/sglang/pull/34823)
  Skip oow slot freeing under eagle (#34823)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-08-14** [`456c5551cc`](https://github.com/sgl-project/sglang/commit/456c5551cc) [#34728](https://github.com/sgl-project/sglang/pull/34728)
  [XPU][test] Add cache_salt=None to _make_req in test_lmcache_radix_cache.py (#34728)
  _Files: `test/registered/xpu/test_lmcache_radix_cache.py`_
- **2026-08-13** [`903439044a`](https://github.com/sgl-project/sglang/commit/903439044a) [#31479](https://github.com/sgl-project/sglang/pull/31479)
  perf(kv-events): coalesce cache events (#31479)
  _Files: `python/sglang/srt/mem_cache/events.py`, `test/manual/test_kv_events.py`, `test/registered/unit/mem_cache/test_hiradix_cache_unit.py`, `test/registered/unit/mem_cache/test_mamba_unittest.py` _+3 more__
- **2026-08-13** [`8ad04a9bee`](https://github.com/sgl-project/sglang/commit/8ad04a9bee) [#30405](https://github.com/sgl-project/sglang/pull/30405)
  docs(nixl): document OBJ throughput target (#30405)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/README.md`, `python/sglang/srt/mem_cache/storage/nixl/nixl.config.toml.sample`_
- **2026-08-13** [`a34f81251f`](https://github.com/sgl-project/sglang/commit/a34f81251f) [#30762](https://github.com/sgl-project/sglang/pull/30762)
  fix(hicache/umbp): support DeepSeek-V4 hybrid HostPoolGroup (multi-po… (#30762)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/storage/umbp/umbp_store.py`, `test/registered/hicache/test_hicache_storage_umbp_backend.py`, `test/registered/unit/mem_cache/test_hicache_staged_write_back_dispatch.py` _+2 more__
- **2026-08-13** [`5a5c3d309b`](https://github.com/sgl-project/sglang/commit/5a5c3d309b) [#34667](https://github.com/sgl-project/sglang/pull/34667)
  Drop the mmlu case from the unified radix cache kit (#34667)
  _Files: `python/sglang/test/kits/unified_radix_cache_kit.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_hicache_pp_kl.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_cp.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dcp.py` _+2 more__
- **2026-08-13** [`26627e999d`](https://github.com/sgl-project/sglang/commit/26627e999d) [#34644](https://github.com/sgl-project/sglang/pull/34644)
  [Fix] Snapshot `req.prefix_indices` when the prefix cache is disabled (#34644)
  _Files: `python/sglang/srt/mem_cache/swa_radix_cache.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-08-13** [`5efe9b104d`](https://github.com/sgl-project/sglang/commit/5efe9b104d) [#34656](https://github.com/sgl-project/sglang/pull/34656)
  Record both architectures in the bit-exact guard docstrings (#34656)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_hybrid_bitexact.py`_
- **2026-08-12** [`3974b00359`](https://github.com/sgl-project/sglang/commit/3974b00359) [#34607](https://github.com/sgl-project/sglang/pull/34607)
  Add bit-exact unified radix cache KL test for hybrid SWA + mamba (#34607)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_hybrid_bitexact.py`_
- **2026-08-12** [`773faf992d`](https://github.com/sgl-project/sglang/commit/773faf992d) [#34141](https://github.com/sgl-project/sglang/pull/34141)
  Reserve multimodal runtime allocations and keep padded inputs aligned (#34141)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/model_executor/model_runner_components/kv_pool_runtime.py`, `test/registered/vlm/test_vision_openai_server_a.py`_
- **2026-08-12** [`5899674504`](https://github.com/sgl-project/sglang/commit/5899674504) [#34458](https://github.com/sgl-project/sglang/pull/34458)
  [Fix] Make DeepSeek-V4 reasoning and tool-call streaming parsing chunk-invariant (#34458)
  _Files: `python/sglang/srt/function_call/deepseekv32_detector.py`, `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/function_call/test_deepseekv4_detector.py`, `test/registered/unit/parser/test_reasoning_parser.py`_
- **2026-08-12** [`1ce515a53d`](https://github.com/sgl-project/sglang/commit/1ce515a53d) [#34464](https://github.com/sgl-project/sglang/pull/34464)
  Refocus LoRA tests on regression coverage (#34464)
  _Files: `test/registered/kernels/ops/gemm/test_chunked_sgmv_cuda_graph.py`, `test/registered/lora/test_embedding_lora_support.py`, `test/registered/lora/test_lora_eviction_policy.py`, `test/registered/lora/test_lora_openai_compatible.py` _+4 more__
- **2026-08-11** [`8f3d3a31f4`](https://github.com/sgl-project/sglang/commit/8f3d3a31f4) [#29792](https://github.com/sgl-project/sglang/pull/29792)
  [HiCache] Fix Mamba track-boundary bookkeeping under overlap scheduling (#29792)
  _Files: `python/sglang/srt/hardware_backend/mlx/kv_cache/auxiliary_state.py`, `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py` _+3 more__
- **2026-08-11** [`5469faec45`](https://github.com/sgl-project/sglang/commit/5469faec45) [#34329](https://github.com/sgl-project/sglang/pull/34329)
  HiSparse: shared-index (IndexShare) plan-then-IO swap-in prefetch (#34329)
  _Files: `docs/docs/advanced_features/hisparse_guide.mdx`, `python/sglang/kernels/jit/csrc/hisparse.cuh`, `python/sglang/kernels/ops/kvcache/hisparse.py`, `python/sglang/srt/environ.py` _+4 more__
- **2026-08-11** [`a92bbf2f24`](https://github.com/sgl-project/sglang/commit/a92bbf2f24) [#34333](https://github.com/sgl-project/sglang/pull/34333)
  docs: remove DSV4 low-latency chunked prefill size (#34333)
  _Files: `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-08-10** [`77b8315b84`](https://github.com/sgl-project/sglang/commit/77b8315b84) [#34272](https://github.com/sgl-project/sglang/pull/34272)
  [CI] Fix GSM8K floating-point tolerance boundary (#34272)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_nightly.py`_
- **2026-08-10** [`ca0f8a0f4c`](https://github.com/sgl-project/sglang/commit/ca0f8a0f4c) [#33484](https://github.com/sgl-project/sglang/pull/33484)
  perf(hisparse): fuse the DSv4 value and scale swap-in copy on ROCm (#33484)
  _Files: `python/sglang/kernels/jit/csrc/hisparse.cuh`, `test/registered/kernels/ops/kvcache/test_hisparse.py`_
- **2026-08-10** [`1a8e4876b6`](https://github.com/sgl-project/sglang/commit/1a8e4876b6) [#33085](https://github.com/sgl-project/sglang/pull/33085)
  perf(hisparse): 128-bit non-temporal swap-in copy on ROCm (#33085)
  _Files: `python/sglang/kernels/jit/csrc/hisparse.cuh`, `test/registered/kernels/ops/kvcache/test_hisparse.py`_
- **2026-08-10** [`3c533acec6`](https://github.com/sgl-project/sglang/commit/3c533acec6) [#33639](https://github.com/sgl-project/sglang/pull/33639)
  [Hicache][2/2]Support Mamba branching in Unified Radix Cache with HiCache (#33639)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/srt/mem_cache/unified_cache/components/mamba_component.py`, `python/sglang/srt/mem_cache/unified_cache/components/swa_component.py`, `python/sglang/srt/mem_cache/unified_cache/components/tree_component.py` _+3 more__

## Prefill / Decode Disaggregation  (27 commits)

- **2026-08-17** [`7c423cfd41`](https://github.com/sgl-project/sglang/commit/7c423cfd41) [#35070](https://github.com/sgl-project/sglang/pull/35070)
  [PD] Avoid unused PREBUILT prompt tensor transfer (#35070)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-08-17** [`b83d507cd7`](https://github.com/sgl-project/sglang/commit/b83d507cd7) [#33676](https://github.com/sgl-project/sglang/pull/33676)
  [NPU] Support DeepSeek-V4 DSpark and refactor DSV4 cache management (#33676)
  _Files: `python/sglang/kernels/ops/speculative/dspark/dspark_verify_window.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/disaggregation/decode.py` _+33 more__
- **2026-08-16** [`3d3194f6c3`](https://github.com/sgl-project/sglang/commit/3d3194f6c3) [#34404](https://github.com/sgl-project/sglang/pull/34404)
  vlm: cache kimi-k3 per-image processor artifacts (#34404)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/models/kimi_k3.py` _+16 more__
- **2026-08-16** [`8922bb98e2`](https://github.com/sgl-project/sglang/commit/8922bb98e2) [#34793](https://github.com/sgl-project/sglang/pull/34793)
  refactor(hicache): flatten L2 transfer execution (#34793)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py` _+6 more__
- **2026-08-15** [`5c0ace30c0`](https://github.com/sgl-project/sglang/commit/5c0ace30c0) [#34471](https://github.com/sgl-project/sglang/pull/34471)
  [diffusion] model: support ltx-2.5 (#34471)
  _Files: `docs/cookbook/diffusion/LTX/LTX2.5.mdx`, `docs/docs.json`, `docs/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs/src/snippets/diffusion/ltx25-deployment.jsx` _+46 more__
- **2026-08-15** [`35cefd1c51`](https://github.com/sgl-project/sglang/commit/35cefd1c51) [#34892](https://github.com/sgl-project/sglang/pull/34892)
  feat: add safeguards for remote media URLs (#34892)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/inkling.py` _+10 more__
- **2026-08-15** [`d804b6bd98`](https://github.com/sgl-project/sglang/commit/d804b6bd98)
  config: pin the step-12 debt on the supplied-instance surface
  _Files: `test/registered/unit/disaggregation/test_kimi_k3_encoder_mode.py`, `test/registered/unit/test_supplied_instance_exposure_ratchet.py`_
- **2026-08-15** [`1ab713c334`](https://github.com/sgl-project/sglang/commit/1ab713c334)
  config: the post-publish consumers of the supplied-instance surface read the bags
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/lora/lora_manager.py` _+13 more__
- **2026-08-13** [`f3beb2c529`](https://github.com/sgl-project/sglang/commit/f3beb2c529) [#34779](https://github.com/sgl-project/sglang/pull/34779)
  [CI] Disable the prefill CUDA graph on the P worker of test_kimi_linear_pd_dcp4 (#34779)
  _Files: `test/registered/disaggregation/test_kimi_linear_pd_dcp4.py`_
- **2026-08-13** [`8554d9a5bc`](https://github.com/sgl-project/sglang/commit/8554d9a5bc) [#34766](https://github.com/sgl-project/sglang/pull/34766)
  [Fix] Carry the backend on Kimi-K3 deferred preprocessing configs (#34766)
  _Files: `python/sglang/srt/models/kimi_k3.py`, `python/sglang/srt/multimodal/kimi_k3_image_processing.py`, `python/sglang/srt/multimodal/processors/kimi_k3.py`, `test/registered/unit/disaggregation/test_kimi_k3_encoder_mode.py` _+2 more__
- **2026-08-13** [`0772e79ee7`](https://github.com/sgl-project/sglang/commit/0772e79ee7) [#34755](https://github.com/sgl-project/sglang/pull/34755)
  [CI][PD] Pin nccl rendezvous port per side to fix flaky disaggregation tests (#34755)
  _Files: `python/sglang/test/server_fixtures/disaggregation_fixture.py`, `test/registered/disaggregation/test_disaggregation_dsv4.py`_
- **2026-08-13** [`a82f8e1777`](https://github.com/sgl-project/sglang/commit/a82f8e1777) [#34692](https://github.com/sgl-project/sglang/pull/34692)
  [PD] Add the missing Prefill bootstrap timeout for NIXL (#34692)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-08-13** [`ba23846ccf`](https://github.com/sgl-project/sglang/commit/ba23846ccf) [#33895](https://github.com/sgl-project/sglang/pull/33895)
  move the PD bootstrap registry under api_server::disaggregation (#33895)
  _Files: `rust/Cargo.lock`, `rust/sglang-server/Cargo.toml`, `rust/sglang-server/src/api_server.rs`, `rust/sglang-server/src/api_server/disaggregation.rs` _+4 more__
- **2026-08-13** [`50cc1aa241`](https://github.com/sgl-project/sglang/commit/50cc1aa241) [#34477](https://github.com/sgl-project/sglang/pull/34477)
  [CI] Route mmlu and GB300 MMMU-Pro evals through sgl-eval (#34477)
  _Files: `.github/workflows/_pr-test-stage-cpu.yml`, `python/sglang/test/accuracy_test_runner.py`, `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/run_eval.py` _+21 more__
- **2026-08-12** [`385903b0ac`](https://github.com/sgl-project/sglang/commit/385903b0ac) [#30827](https://github.com/sgl-project/sglang/pull/30827)
  feat: add cache salt support to KV cache events (#30827)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/kv_events.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/openai/protocol.py` _+39 more__
- **2026-08-12** [`e6250c7c70`](https://github.com/sgl-project/sglang/commit/e6250c7c70) [#34601](https://github.com/sgl-project/sglang/pull/34601)
  docs: update Qwen3.8 disaggregated serving configs (#34601)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8.jsx`_
- **2026-08-11** [`9c1517df4a`](https://github.com/sgl-project/sglang/commit/9c1517df4a) [#34450](https://github.com/sgl-project/sglang/pull/34450)
  Raise PD zmq per-context socket cap via SGLANG_DISAGGREGATION_ZMQ_MAX_SOCKETS (#34450)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/environ.py`_
- **2026-08-11** [`8267d76c2c`](https://github.com/sgl-project/sglang/commit/8267d76c2c) [#34175](https://github.com/sgl-project/sglang/pull/34175)
  [VLM] replace deprecated image processor use_fast (#34175)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `docs/docs/advanced_features/vlm_query.mdx`, `docs/docs/hardware-platforms/ascend-npus/reference/support_features.mdx`, `docs/docs/sglang-diffusion/models_with_ar.mdx` _+17 more__
- **2026-08-11** [`a50ab9cec7`](https://github.com/sgl-project/sglang/commit/a50ab9cec7) [#34341](https://github.com/sgl-project/sglang/pull/34341)
  [npu] [bugfix] Fix HiCache MHA backup for NPU (#34341)
  _Files: `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/mem_cache/pool_host/mha.py`_
- **2026-08-11** [`667e18d99d`](https://github.com/sgl-project/sglang/commit/667e18d99d) [#33807](https://github.com/sgl-project/sglang/pull/33807)
  [PD] Support pipeline-parallel prefill with Mooncake staging buffer (#33807)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py` _+3 more__
- **2026-08-11** [`418975ba64`](https://github.com/sgl-project/sglang/commit/418975ba64) [#34206](https://github.com/sgl-project/sglang/pull/34206)
  [EPD] feat: pipeline owner-only multimodal preprocessing (#34206)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/models/kimi_k3.py`, `python/sglang/srt/multimodal/encoder_preprocessing.py`, `python/sglang/srt/multimodal/kimi_k3_image_processing.py` _+2 more__
- **2026-08-10** [`ceeaec2078`](https://github.com/sgl-project/sglang/commit/ceeaec2078) [#33362](https://github.com/sgl-project/sglang/pull/33362)
  [PD] Support --enable-unified-memory with PD disaggregation (kimi-linear MLA hybrid-Mamba) (#33362)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py` _+11 more__
- **2026-08-10** [`14ffd447a4`](https://github.com/sgl-project/sglang/commit/14ffd447a4) [#30392](https://github.com/sgl-project/sglang/pull/30392)
  [FEAT] Decouple multimodal global cache from Mooncake (#30392)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/mem_cache/embedding_cache_controller.py`, `python/sglang/srt/mem_cache/embedding_store.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_embedding_store.py` _+2 more__
- **2026-08-10** [`c971d7ac9c`](https://github.com/sgl-project/sglang/commit/c971d7ac9c) [#33910](https://github.com/sgl-project/sglang/pull/33910)
  Refactor staging registration metadata fields (#33910)
  _Files: `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py` _+1 more__
- **2026-08-10** [`a76a167812`](https://github.com/sgl-project/sglang/commit/a76a167812) [#28753](https://github.com/sgl-project/sglang/pull/28753)
  Fix/hisparse host backed max request length (#28753)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/model_executor/model_runner.py`, `test/registered/unit/mem_cache/test_hisparse_max_token_pool_size.py`_
- **2026-08-10** [`5a8e360e70`](https://github.com/sgl-project/sglang/commit/5a8e360e70) [#34191](https://github.com/sgl-project/sglang/pull/34191)
  [PD] Skip speculative verify scratch on prefill servers (saves num_draft_tokens x mamba pool per rank) (#34191)
  _Files: `python/sglang/srt/mem_cache/kv_cache_configurator.py`, `python/sglang/srt/model_executor/model_runner_components/cuda_graph_setup.py`, `python/sglang/srt/model_executor/runner/base_runner.py`_
- **2026-08-10** [`c20e99bd22`](https://github.com/sgl-project/sglang/commit/c20e99bd22) [#34163](https://github.com/sgl-project/sglang/pull/34163)
  fix(vlm): preserve Kimi-K3 GPU JPEG accuracy (#34163)
  _Files: `docker/kimi_k3/kimi_k3_cu12.Dockerfile`, `docker/kimi_k3/kimi_k3_cu13.Dockerfile`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/multimodal/processors/kimi_k3.py` _+4 more__

## Other  (27 commits)

- **2026-08-17** [`4b06f917ca`](https://github.com/sgl-project/sglang/commit/4b06f917ca) [#35094](https://github.com/sgl-project/sglang/pull/35094)
  Upd: code owners (#35094)
  _Files: `.github/CODEOWNERS`_
- **2026-08-16** [`b7eccd642f`](https://github.com/sgl-project/sglang/commit/b7eccd642f) [#34996](https://github.com/sgl-project/sglang/pull/34996)
  Increase post-capture decode memory reserve (#34996)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-08-15** [`cef8a32b9d`](https://github.com/sgl-project/sglang/commit/cef8a32b9d) [#34866](https://github.com/sgl-project/sglang/pull/34866)
  update codeowner (#34866)
  _Files: `.github/CODEOWNERS`_
- **2026-08-15** [`e161bd1265`](https://github.com/sgl-project/sglang/commit/e161bd1265) [#34937](https://github.com/sgl-project/sglang/pull/34937)
  Fix Python packaging shadowing in DeepEP wheel builds (#34937)
  _Files: `scripts/build_sgl_deepep.sh`_
- **2026-08-15** [`c87a2ced12`](https://github.com/sgl-project/sglang/commit/c87a2ced12) [#34094](https://github.com/sgl-project/sglang/pull/34094)
  test(step-12): state the bag contract as what resolution produced, and the skill rule that goes with it
  _Files: `.claude/skills/sglang-runtime-context/SKILL.md`, `test/registered/unit/test_runtime_context_config_bags.py`_
- **2026-08-15** [`61908870f6`](https://github.com/sgl-project/sglang/commit/61908870f6) [#27313](https://github.com/sgl-project/sglang/pull/27313)
  config: spell out the one dynamic config read the census could not see
  _Files: `python/sglang/srt/layers/cp/base.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_resolution_is_reproducible.py`, `test/registered/unit/test_global_config_read_ratchet.py`_
- **2026-08-15** [`2a89c6823a`](https://github.com/sgl-project/sglang/commit/2a89c6823a) [#34880](https://github.com/sgl-project/sglang/pull/34880)
  fix: honor explicit model loader classes (#34880)
  _Files: `python/sglang/srt/model_loader/loader.py`_
- **2026-08-14** [`17efe37428`](https://github.com/sgl-project/sglang/commit/17efe37428) [#34875](https://github.com/sgl-project/sglang/pull/34875)
  Remove 11 dead CODEOWNERS rules (#34875)
  _Files: `.github/CODEOWNERS`_
- **2026-08-14** [`d7207be156`](https://github.com/sgl-project/sglang/commit/d7207be156) [#34869](https://github.com/sgl-project/sglang/pull/34869)
  Fix startup weight load after TorchAO removal (#34869)
  _Files: `python/sglang/srt/model_executor/model_runner_components/startup_weight_load.py`, `test/registered/unit/model_executor/model_runner_components/test_startup_weight_load.py`_
- **2026-08-14** [`1af761a09a`](https://github.com/sgl-project/sglang/commit/1af761a09a) [#34019](https://github.com/sgl-project/sglang/pull/34019)
  [SM12x] Default the fused MHC post+pre path on (#34019)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-08-13** [`8bbca87780`](https://github.com/sgl-project/sglang/commit/8bbca87780) [#34730](https://github.com/sgl-project/sglang/pull/34730)
  [Core] Organize environment variable registry (#34730)
  _Files: `python/sglang/srt/environ.py`_
- **2026-08-13** [`ebc144ce3f`](https://github.com/sgl-project/sglang/commit/ebc144ce3f) [#34653](https://github.com/sgl-project/sglang/pull/34653)
  Enable unified cache out-of-window slot freeing by default (#34653)
  _Files: `python/sglang/srt/environ.py`_
- **2026-08-13** [`1286a50bb9`](https://github.com/sgl-project/sglang/commit/1286a50bb9) [#34671](https://github.com/sgl-project/sglang/pull/34671)
  Add New Intel members into CI permission list (#34671)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-08-13** [`cfdfd31826`](https://github.com/sgl-project/sglang/commit/cfdfd31826) [#34649](https://github.com/sgl-project/sglang/pull/34649)
  Add thanhhao98 to CI_PERMISSIONS.json (#34649)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-08-12** [`126010c373`](https://github.com/sgl-project/sglang/commit/126010c373) [#34610](https://github.com/sgl-project/sglang/pull/34610)
  [misc] update CI_PERMISSIONS.json (#34610)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-08-12** [`a2e88279c2`](https://github.com/sgl-project/sglang/commit/a2e88279c2) [#34335](https://github.com/sgl-project/sglang/pull/34335)
  metrics: don't clock-rebase unset time sentinels in ReqTimeStats deserialization (#34335)
  _Files: `python/sglang/srt/observability/req_time_stats.py`, `test/registered/unit/observability/test_req_time_stats.py`_
- **2026-08-12** [`687967c70d`](https://github.com/sgl-project/sglang/commit/687967c70d) [#34500](https://github.com/sgl-project/sglang/pull/34500)
  Fix tokenizer warning filtering for processors (#34500)
  _Files: `python/sglang/srt/utils/hf_transformers/processor.py`, `python/sglang/srt/utils/hf_transformers/tokenizer.py`_
- **2026-08-11** [`983dfd6a9a`](https://github.com/sgl-project/sglang/commit/983dfd6a9a) [#34472](https://github.com/sgl-project/sglang/pull/34472)
  [Misc] Sanitize the structure of environ.py (#34472)
  _Files: `python/sglang/srt/environ.py`_
- **2026-08-11** [`9ced8d0981`](https://github.com/sgl-project/sglang/commit/9ced8d0981) [#32370](https://github.com/sgl-project/sglang/pull/32370)
  Optimize FP32 LM head for bf16/fp16 (#32370)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `test/registered/rl/test_fp32_lm_head.py`_
- **2026-08-11** [`93c1bff1d4`](https://github.com/sgl-project/sglang/commit/93c1bff1d4) [#34440](https://github.com/sgl-project/sglang/pull/34440)
  Fix default dtype restoration after model loader errors (#34440)
  _Files: `python/sglang/srt/model_loader/utils.py`_
- **2026-08-11** [`f9153df62e`](https://github.com/sgl-project/sglang/commit/f9153df62e) [#34356](https://github.com/sgl-project/sglang/pull/34356)
  Add bit-exact hicache logprob-consistency test (#34356)
  _Files: `test/registered/models_e2e/test_inkling_small_nvfp4.py`_
- **2026-08-11** [`b20c375c10`](https://github.com/sgl-project/sglang/commit/b20c375c10) [#34405](https://github.com/sgl-project/sglang/pull/34405)
  Fix flaky decode cache-hit check in Inkling test (#34405)
  _Files: `python/sglang/test/kl_test_utils.py`, `test/registered/models_e2e/test_inkling_small_nvfp4.py`_
- **2026-08-11** [`5af5183351`](https://github.com/sgl-project/sglang/commit/5af5183351) [#34300](https://github.com/sgl-project/sglang/pull/34300)
  test: isolate metal profiler tests from ambient SGLANG_USE_MLX (#34300)
  _Files: `test/registered/unit/hardware_backend/mlx/test_metal_profiler.py`_
- **2026-08-11** [`03c942dfab`](https://github.com/sgl-project/sglang/commit/03c942dfab) [#33086](https://github.com/sgl-project/sglang/pull/33086)
  [Fix] Make wait_port_available actually wait timeout_s seconds (#33086)
  _Files: `python/sglang/srt/utils/network.py`_
- **2026-08-10** [`56e8bb49b8`](https://github.com/sgl-project/sglang/commit/56e8bb49b8) [#34322](https://github.com/sgl-project/sglang/pull/34322)
  fix(ci): constrain NeMo Skills evaluator dependencies (#34322)
  _Files: `python/sglang/test/accuracy_test_runner.py`_
- **2026-08-10** [`c30872fa00`](https://github.com/sgl-project/sglang/commit/c30872fa00) [#34325](https://github.com/sgl-project/sglang/pull/34325)
  [Fix] Read trace level via `get_global_trace_level()` in `trace_async` (#34325)
  _Files: `python/sglang/srt/observability/trace_async.py`_
- **2026-08-10** [`a2161ce682`](https://github.com/sgl-project/sglang/commit/a2161ce682) [#33146](https://github.com/sgl-project/sglang/pull/33146)
  Support thinking budget for Inkling (#33146)
  _Files: `python/sglang/srt/sampling/custom_logit_processor.py`, `test/registered/unit/sampling/test_custom_logit_processor.py`_

## Quantization  (20 commits)

- **2026-08-17** [`92b1d382c7`](https://github.com/sgl-project/sglang/commit/92b1d382c7) [#35020](https://github.com/sgl-project/sglang/pull/35020)
  [Fix] Correct dense FP8 Marlin bias ordering (#35020)
  _Files: `python/sglang/srt/layers/quantization/marlin_utils_fp8.py`, `test/registered/unit/layers/quantization/test_marlin_utils_fp8.py`_
- **2026-08-16** [`e9fe58139f`](https://github.com/sgl-project/sglang/commit/e9fe58139f) [#34736](https://github.com/sgl-project/sglang/pull/34736)
  [diffusion] refactor: unify component residency controls (#34736)
  _Files: `docs/cookbook/diffusion/Krea/Krea-2.mdx`, `docs/cookbook/diffusion/README.mdx`, `docs/docs/sglang-diffusion/api/cli.mdx`, `docs/docs/sglang-diffusion/deployment_cookbook.mdx` _+66 more__
- **2026-08-16** [`f68517f644`](https://github.com/sgl-project/sglang/commit/f68517f644) [#30900](https://github.com/sgl-project/sglang/pull/30900)
  [AMD][Quantization][Bugfix] Fix bug related to fp8 max on gfx95x for per-token-group quant (ROCm) (#30900)
  _Files: `python/sglang/kernels/ops/quantization/fp8_kernel.py`, `test/registered/unit/layers/quantization/test_fp8_kernel_hip_max.py`_
- **2026-08-14** [`a1844709f1`](https://github.com/sgl-project/sglang/commit/a1844709f1) [#34882](https://github.com/sgl-project/sglang/pull/34882)
  [CI] Trim Qwen3.5 FP8 GB300 performance batches (#34882)
  _Files: `test/registered/gb300/test_qwen35_fp8.py`_
- **2026-08-14** [`22dde1dd5b`](https://github.com/sgl-project/sglang/commit/22dde1dd5b) [#31554](https://github.com/sgl-project/sglang/pull/31554)
  [Docs] Fill GLM-5.2 H200 FP8 speed cells (low-latency, balanced); fix MTP notation (#31554)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2-benchmarks.jsx`_
- **2026-08-14** [`5e65dd01a7`](https://github.com/sgl-project/sglang/commit/5e65dd01a7) [#34304](https://github.com/sgl-project/sglang/pull/34304)
  Remove the torchao integration (--torchao-config) (#34304)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `docker/rocm.Dockerfile`, `docker/xpu.Dockerfile`, `docs/docs/advanced_features/quantization.mdx` _+19 more__
- **2026-08-14** [`2622e013eb`](https://github.com/sgl-project/sglang/commit/2622e013eb) [#34774](https://github.com/sgl-project/sglang/pull/34774)
  [Fix] has_hf_quant_config crashes on local dirs without the config (#34774)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-08-14** [`e1c4db9621`](https://github.com/sgl-project/sglang/commit/e1c4db9621) [#34331](https://github.com/sgl-project/sglang/pull/34331)
  [quantization] Add tuned Triton tile configs for channelwise FP8 GEMM… (#34331)
  _Files: `python/sglang/kernels/ops/quantization/configs/N=24576,K=4096,device_name=NVIDIA_L40S,dtype=fp8_w8a8_channelwise.json`, `python/sglang/kernels/ops/quantization/configs/N=4096,K=12288,device_name=NVIDIA_L40S,dtype=fp8_w8a8_channelwise.json`, `python/sglang/kernels/ops/quantization/configs/N=4096,K=4096,device_name=NVIDIA_L40S,dtype=fp8_w8a8_channelwise.json`, `python/sglang/kernels/ops/quantization/configs/N=6144,K=4096,device_name=NVIDIA_L40S,dtype=fp8_w8a8_channelwise.json` _+3 more__
- **2026-08-13** [`9720922671`](https://github.com/sgl-project/sglang/commit/9720922671) [#34761](https://github.com/sgl-project/sglang/pull/34761)
  [AMD][CI] Restore gfx942 Grok-1 INT4 and Grok-2 schedules (#34761)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`_
- **2026-08-13** [`fad376d3ee`](https://github.com/sgl-project/sglang/commit/fad376d3ee) [#29593](https://github.com/sgl-project/sglang/pull/29593)
  [CPU][QUANT] add amx cpu support for auto-round (#29593)
  _Files: `docs/docs/advanced_features/quantization.mdx`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/amx_utils.py`, `python/sglang/srt/layers/quantization/__init__.py` _+2 more__
- **2026-08-12** [`9deb6952af`](https://github.com/sgl-project/sglang/commit/9deb6952af) [#34476](https://github.com/sgl-project/sglang/pull/34476)
  [AMD][DI][CI] Add GLM-5.2 MXFP4 wide-EP16 2P1D nightly recipes (#34476)
  _Files: `scripts/ci/slurm/nightly-configs.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/glm52/1k1k/2p1d-ep16-mtp.yaml`, `scripts/ci/slurm/recipes/mi355x-fp4/glm52/1k1k/2p1d-ep16.yaml`_
- **2026-08-12** [`b5d1453ed2`](https://github.com/sgl-project/sglang/commit/b5d1453ed2) [#34379](https://github.com/sgl-project/sglang/pull/34379)
  [AMD] GLM 5.2 MXFP4 SGLANG COOKBOOK (#34379)
  _Files: `docs/cookbook/autoregressive/GLM/GLM-5.2.mdx`, `docs/src/snippets/configs/zai-org/glm-5.2.jsx`_
- **2026-08-12** [`4827061247`](https://github.com/sgl-project/sglang/commit/4827061247) [#34506](https://github.com/sgl-project/sglang/pull/34506)
  [Diffusion] Make weight-only FP8 dequant cache torch.compile-safe (#34506)
  _Files: `python/sglang/multimodal_gen/runtime/layers/quantization/weight_only_fp8.py`, `python/sglang/multimodal_gen/test/unit/test_weight_only_fp8_dequant_cache.py`_
- **2026-08-11** [`d5d41d07ed`](https://github.com/sgl-project/sglang/commit/d5d41d07ed) [#34395](https://github.com/sgl-project/sglang/pull/34395)
  [Docs] Add Ling-3.0-tiny INT4 recipes (#34395)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-tiny.mdx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-tiny-benchmarks.jsx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-tiny.jsx`_
- **2026-08-11** [`2d193077f7`](https://github.com/sgl-project/sglang/commit/2d193077f7) [#34257](https://github.com/sgl-project/sglang/pull/34257)
  [JIT Kernel] Migrate per-token FP8 quantization from AOT to JIT (#34257)
  _Files: `python/sglang/kernels/aot/benchmark/bench_per_token_quant_fp8.py`, `python/sglang/kernels/aot/csrc/common_extension.cc`, `python/sglang/kernels/aot/tests/test_per_token_quant_fp8.py`, `python/sglang/kernels/jit/csrc/gemm/per_token_quant_fp8.cuh` _+5 more__
- **2026-08-11** [`ba3dc16401`](https://github.com/sgl-project/sglang/commit/ba3dc16401) [#34305](https://github.com/sgl-project/sglang/pull/34305)
  [diffusion] weight-only FP8: dequantize linear weights once at first use (Ideogram-4 denoise -18.8% H200 / -7.8% H100, bit-exact) (#34305)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/weight_only_fp8.py`, `python/sglang/multimodal_gen/test/unit/test_weight_only_fp8_dequant_cache.py`_
- **2026-08-11** [`afa2d5570b`](https://github.com/sgl-project/sglang/commit/afa2d5570b) [#34136](https://github.com/sgl-project/sglang/pull/34136)
  [Diffusion] Add online FP8 support for Krea-2 (#34136)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/krea2.py`, `python/sglang/multimodal_gen/test/unit/test_krea2_fp8.py`_
- **2026-08-10** [`0661eb1c50`](https://github.com/sgl-project/sglang/commit/0661eb1c50) [#34252](https://github.com/sgl-project/sglang/pull/34252)
  plugins: don't directly set quant class (#34252)
  _Files: `python/sglang/srt/model_loader/weight_utils.py`_
- **2026-08-10** [`8ba9385097`](https://github.com/sgl-project/sglang/commit/8ba9385097) [#34064](https://github.com/sgl-project/sglang/pull/34064)
  [diffusion] chore: optimize model weight loading (#34064)
  _Files: `docs/docs/sglang-diffusion/api/cli.mdx`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`, `python/sglang/multimodal_gen/runtime/loader/weight_load_plan.py` _+4 more__
- **2026-08-10** [`d6a066131c`](https://github.com/sgl-project/sglang/commit/d6a066131c) [#34222](https://github.com/sgl-project/sglang/pull/34222)
  [Feature] Support NVFP4 token embedding in ModelOpt mixed-precision checkpoints (#34222)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/quant/test_nvfp4_embedding.py`_

## Docs / Examples  (18 commits)

- **2026-08-17** [`f019f0b064`](https://github.com/sgl-project/sglang/commit/f019f0b064) [#35068](https://github.com/sgl-project/sglang/pull/35068)
  [Docs] Feature MiniMax-H3 in the popular-models banner (#35068)
  _Files: `docs/src/snippets/configs/popular-models.jsx`_
- **2026-08-14** [`8b4faa3336`](https://github.com/sgl-project/sglang/commit/8b4faa3336) [#34886](https://github.com/sgl-project/sglang/pull/34886)
  [Docs] Update Kimi-K3 installation options (#34886)
  _Files: `docs/cookbook/autoregressive/Moonshotai/Kimi-K3.mdx`_
- **2026-08-14** [`bfb224ff01`](https://github.com/sgl-project/sglang/commit/bfb224ff01) [#32414](https://github.com/sgl-project/sglang/pull/32414)
  Add Reasoning-Aware Compression (RAC) pruning recipe for reasoning models (#32414)
  _Files: `docs/docs.json`, `docs/docs/advanced_features/reasoning_aware_compression.mdx`, `examples/usage/reasoning_aware_compression/README.md`, `examples/usage/reasoning_aware_compression/rac_collect_traces.py` _+2 more__
- **2026-08-14** [`b676793e5e`](https://github.com/sgl-project/sglang/commit/b676793e5e) [#32982](https://github.com/sgl-project/sglang/pull/32982)
  docs: sync LMSYS SGLang blog cards (#32982)
  _Files: `docs/index.mdx`_
- **2026-08-14** [`46d84f4b48`](https://github.com/sgl-project/sglang/commit/46d84f4b48) [#34753](https://github.com/sgl-project/sglang/pull/34753)
  feat(cli): add extensible serve backend plugins (#34753)
  _Files: `docs/docs.json`, `docs/docs/developer_guide/overview.mdx`, `docs/docs/developer_guide/serve_backend_plugins.mdx`, `python/sglang/cli/serve.py` _+3 more__
- **2026-08-14** [`6ad3f2d8fd`](https://github.com/sgl-project/sglang/commit/6ad3f2d8fd) [#34797](https://github.com/sgl-project/sglang/pull/34797)
  docs: link dots3.note checkpoints, add H100 cells (#34797)
  _Files: `docs/cookbook/autoregressive/RedNote/Dots3-Note.mdx`, `docs/src/snippets/_deployment.jsx`, `docs/src/snippets/_playground.jsx`, `docs/src/snippets/configs/rednote/dots3-note.jsx`_
- **2026-08-13** [`652a2709d1`](https://github.com/sgl-project/sglang/commit/652a2709d1) [#34654](https://github.com/sgl-project/sglang/pull/34654)
  [Docs] Add decode context parallelism to advanced features (#34654)
  _Files: `docs/docs.json`, `docs/docs/advanced_features/dcp.mdx`, `docs/docs/advanced_features/overview.mdx`, `docs/docs/advanced_features/server_arguments.mdx`_
- **2026-08-13** [`c1142677a8`](https://github.com/sgl-project/sglang/commit/c1142677a8) [#34658](https://github.com/sgl-project/sglang/pull/34658)
  [do not merge] add new cookbooks (#34658)
  _Files: `docs/cookbook/autoregressive/RedNote/Dots3-Note.mdx`, `docs/docs.json`, `docs/src/snippets/configs/rednote/dots3-note.jsx`_
- **2026-08-13** [`40eaf34428`](https://github.com/sgl-project/sglang/commit/40eaf34428) [#30394](https://github.com/sgl-project/sglang/pull/30394)
  fix: make automatic NUMA binding configurable (#30394)
  _Files: `docs/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/utils/numa_utils.py`, `test/registered/utils/test_numa_utils.py`_
- **2026-08-12** [`198b7e9240`](https://github.com/sgl-project/sglang/commit/198b7e9240) [#34626](https://github.com/sgl-project/sglang/pull/34626)
  [Docs] Use Meta's canonical Muse Glimmer GGUF filename (#34626)
  _Files: `docs/src/snippets/configs/meta-models/muse-glimmer.jsx`_
- **2026-08-12** [`f28bc5a6de`](https://github.com/sgl-project/sglang/commit/f28bc5a6de) [#34573](https://github.com/sgl-project/sglang/pull/34573)
  docs(cookbook): add BF16 recipes to Nemotron 3.5 Lightning (#34573)
  _Files: `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning.jsx`_
- **2026-08-11** [`59450c4f18`](https://github.com/sgl-project/sglang/commit/59450c4f18) [#34444](https://github.com/sgl-project/sglang/pull/34444)
  docs(cookbook): Kimi-K3 — drop --enable-symm-mem from the GB cells (#34444)
  _Files: `docs/src/snippets/configs/moonshotai/kimi-k3.jsx`_
- **2026-08-11** [`f148eb6e6e`](https://github.com/sgl-project/sglang/commit/f148eb6e6e) [#30223](https://github.com/sgl-project/sglang/pull/30223)
  Add Hunyuan3 On Ascend Doc (#30223)
  _Files: `docs/docs.json`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/hy3.mdx`_
- **2026-08-11** [`3add7e19ff`](https://github.com/sgl-project/sglang/commit/3add7e19ff) [#33481](https://github.com/sgl-project/sglang/pull/33481)
  Add NVIDIA Nemotron 3.5 Lightning cookbook (#33481)
  _Files: `docs/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json`, `docs/src/snippets/configs/nvidia/nemotron-3.5-lightning-benchmarks.jsx` _+1 more__
- **2026-08-10** [`e54c153ba6`](https://github.com/sgl-project/sglang/commit/e54c153ba6) [#33820](https://github.com/sgl-project/sglang/pull/33820)
  Add Intern-S2-Mobius cookbook (#33820)
  _Files: `docs/cookbook/autoregressive/InternLM/Intern-S2-Mobius.mdx`, `docs/cookbook/autoregressive/InternLM/Intern-S2-Preview.mdx`, `docs/cookbook/autoregressive/intro.mdx`, `docs/docs.json` _+2 more__
- **2026-08-10** [`77c90e7e54`](https://github.com/sgl-project/sglang/commit/77c90e7e54) [#34283](https://github.com/sgl-project/sglang/pull/34283)
  Cookbook: add Ling-3.0-tiny (#34283)
  _Files: `docs/cookbook/autoregressive/InclusionAI/Ling-3.0-tiny.mdx`, `docs/docs.json`, `docs/src/snippets/configs/inclusionAI/ling-3.0-tiny-benchmarks.jsx`, `docs/src/snippets/configs/inclusionAI/ling-3.0-tiny.jsx`_
- **2026-08-10** [`d95e824a49`](https://github.com/sgl-project/sglang/commit/d95e824a49) [#34281](https://github.com/sgl-project/sglang/pull/34281)
  Muse Glimmer Cookbook: install from the PR branch (#34281)
  _Files: `docs/cookbook/autoregressive/Meta/MuseGlimmer.mdx`_
- **2026-08-10** [`d96b1533ea`](https://github.com/sgl-project/sglang/commit/d96b1533ea) [#34278](https://github.com/sgl-project/sglang/pull/34278)
  Muse Glimmer Cookbook: install from the PR branch (#34278)
  _Files: `docs/cookbook/autoregressive/Meta/MuseGlimmer.mdx`_

## Models  (13 commits)

- **2026-08-17** [`e03c53fc13`](https://github.com/sgl-project/sglang/commit/e03c53fc13) [#35065](https://github.com/sgl-project/sglang/pull/35065)
  docs(cookbook): Qwen3.8-27B deployment grid rework (#35065)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b-benchmarks.jsx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b.jsx`_
- **2026-08-16** [`0e231d365a`](https://github.com/sgl-project/sglang/commit/0e231d365a) [#35018](https://github.com/sgl-project/sglang/pull/35018)
  Clean up playground scripts and add PR babysitter launcher (#35018)
  _Files: `scripts/playground/export_deepseek_nextn.py`, `scripts/playground/launch_pr_babysitters.sh`, `scripts/sort_testcases_alphabetically.py`_
- **2026-08-14** [`70e291b70f`](https://github.com/sgl-project/sglang/commit/70e291b70f) [#34863](https://github.com/sgl-project/sglang/pull/34863)
  [Docs] Add GB300 cells and benchmarks for Qwen3.8-27B (#34863)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b-benchmarks.jsx`, `docs/src/snippets/configs/Qwen/qwen3.8-27b.jsx`_
- **2026-08-14** [`29c6be15a4`](https://github.com/sgl-project/sglang/commit/29c6be15a4) [#34860](https://github.com/sgl-project/sglang/pull/34860)
  [Docs] Add Qwen3.8-27B cookbook page (#34860)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/cookbook/autoregressive/Qwen/Qwen3.8.mdx`, `docs/docs.json`, `docs/src/snippets/_qwen38_mamba_ratio_calculator.jsx` _+2 more__
- **2026-08-14** [`c939307e8a`](https://github.com/sgl-project/sglang/commit/c939307e8a) [#34542](https://github.com/sgl-project/sglang/pull/34542)
  [MiniMax-M3] Overlap shared and routed experts (#34542)
  _Files: `python/sglang/srt/models/minimax_m3.py`_
- **2026-08-14** [`fe0c18effd`](https://github.com/sgl-project/sglang/commit/fe0c18effd) [#34836](https://github.com/sgl-project/sglang/pull/34836)
  [NPU] [DOC] Add Qwen3.8-Max deployment tutorial on Ascend NPUs (#34836)
  _Files: `docs/docs.json`, `docs/docs/hardware-platforms/ascend-npus/model-deployment/tutorials/qwen3_8_max.mdx`_
- **2026-08-14** [`463981922c`](https://github.com/sgl-project/sglang/commit/463981922c) [#34809](https://github.com/sgl-project/sglang/pull/34809)
  [Cookbook] Add DeepSeek-V4-Pro-0813 (Pro Official) serving recipes (#34809)
  _Files: `docs/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4-benchmarks.jsx`, `docs/src/snippets/configs/deepseek-ai/deepseek-v4.jsx`_
- **2026-08-14** [`0a6bbbe128`](https://github.com/sgl-project/sglang/commit/0a6bbbe128) [#34788](https://github.com/sgl-project/sglang/pull/34788)
  [Fix] Restore layer-level DSV4 RoPE policy (#34788)
  _Files: `python/sglang/srt/models/deepseek_v4.py`, `test/registered/unit/models/test_deepseek_v4_rope_policy.py`_
- **2026-08-12** [`d21eefc94f`](https://github.com/sgl-project/sglang/commit/d21eefc94f) [#34590](https://github.com/sgl-project/sglang/pull/34590)
  [Docs] Rename Qwen3.8-Max-DSpark to Qwen3.8-2.4T-A95B-DSpark (#34590)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8.mdx`, `docs/src/snippets/configs/Qwen/qwen3.8.jsx`_
- **2026-08-12** [`8e7c07fae7`](https://github.com/sgl-project/sglang/commit/8e7c07fae7) [#34587](https://github.com/sgl-project/sglang/pull/34587)
  [Docs] Add Qwen3.8 cookbook (#34587)
  _Files: `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `docs/cookbook/autoregressive/Qwen/Qwen3.6.mdx`, `docs/cookbook/autoregressive/Qwen/Qwen3.8.mdx` _+5 more__
- **2026-08-11** [`a0a76e4485`](https://github.com/sgl-project/sglang/commit/a0a76e4485) [#29070](https://github.com/sgl-project/sglang/pull/29070)
  [DSV4] perf: Enable alt stream during BCG prefill (#29070)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-08-10** [`8c5d5f75bf`](https://github.com/sgl-project/sglang/commit/8c5d5f75bf) [#33312](https://github.com/sgl-project/sglang/pull/33312)
  Fix DSV4 DSpark shared expert loading (#33312)
  _Files: `python/sglang/srt/models/deepseek_v4_dspark.py`, `test/registered/unit/model_loader/test_runai_model_streamer_loader.py`, `test/registered/unit/models/test_deepseek_v4_shared_expert_fusion.py`_
- **2026-08-10** [`a6c34df044`](https://github.com/sgl-project/sglang/commit/a6c34df044) [#34271](https://github.com/sgl-project/sglang/pull/34271)
  Muse Glimmer Cookbook (#34271)
  _Files: `docs/cards/logos/meta.png`, `docs/cookbook/autoregressive/Meta/Llama3.1.mdx`, `docs/cookbook/autoregressive/Meta/Llama3.3-70B.mdx`, `docs/cookbook/autoregressive/Meta/Llama4.mdx` _+7 more__

## Triton / Kernels  (13 commits)

- **2026-08-16** [`e49557b8da`](https://github.com/sgl-project/sglang/commit/e49557b8da) [#35002](https://github.com/sgl-project/sglang/pull/35002)
  Support model-defined prefill input embedding width (#35002)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`_
- **2026-08-14** [`b784726863`](https://github.com/sgl-project/sglang/commit/b784726863) [#34274](https://github.com/sgl-project/sglang/pull/34274)
  [kernel] Content-addressed JIT build cache, generated from our own ninja (#34274)
  _Files: `python/sglang/kernels/jit/utils/compile.py`, `python/sglang/kernels/jit/utils/compile/__init__.py`, `python/sglang/kernels/jit/utils/compile/cache.py`, `python/sglang/kernels/jit/utils/compile/cpp_args.py` _+8 more__
- **2026-08-13** [`96db53ec70`](https://github.com/sgl-project/sglang/commit/96db53ec70) [#34746](https://github.com/sgl-project/sglang/pull/34746)
  [CI] Fix test_resolution_is_reproducible after cuda_ipc became opt-in (#34746)
  _Files: `test/registered/unit/server_args/test_resolution_is_reproducible.py`_
- **2026-08-13** [`035c622a14`](https://github.com/sgl-project/sglang/commit/035c622a14) [#34538](https://github.com/sgl-project/sglang/pull/34538)
  Reenable breakable CUDA graph for NemotronH (#34538)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/server_args.py`, `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`_
- **2026-08-12** [`273d978bed`](https://github.com/sgl-project/sglang/commit/273d978bed) [#34635](https://github.com/sgl-project/sglang/pull/34635)
  [CI] Use default installer for B300 tests (#34635)
  _Files: `scripts/ci/cuda/ci_install_kimi_k3.sh`, `scripts/ci/runner_configs.yml`_
- **2026-08-12** [`8549cce11b`](https://github.com/sgl-project/sglang/commit/8549cce11b) [#32467](https://github.com/sgl-project/sglang/pull/32467)
  [BugFix] Fix race in c128 prefill plan kernel on ragged extend (#32467)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c_plan.cuh`_
- **2026-08-11** [`7fb6e61b95`](https://github.com/sgl-project/sglang/commit/7fb6e61b95) [#34431](https://github.com/sgl-project/sglang/pull/34431)
  Fix CUDA 13.0 VMM handle type compatibility (#34431)
  _Files: `python/sglang/srt/cuda_vmm_utils.py`, `test/registered/unit/test_cuda_vmm_utils.py`_
- **2026-08-10** [`c80a38edcd`](https://github.com/sgl-project/sglang/commit/c80a38edcd) [#34321](https://github.com/sgl-project/sglang/pull/34321)
  [Fix] Pin `cuda-tile` to 1.6.0rc5 to unblock Python 3.10 x86_64 installs (#34321)
  _Files: `python/pyproject.toml`_
- **2026-08-10** [`166c6f7181`](https://github.com/sgl-project/sglang/commit/166c6f7181) [#32907](https://github.com/sgl-project/sglang/pull/32907)
  [Kernel] cutedsl_bf16_gemm: trailing cluster barrier for 2-CTA TGV kernel exit (#32907) (#32954)
  _Files: `python/sglang/kernels/ops/gemm/cutedsl_bf16_gemm.py`_
- **2026-08-10** [`01a2ef95b8`](https://github.com/sgl-project/sglang/commit/01a2ef95b8) [#34254](https://github.com/sgl-project/sglang/pull/34254)
  [NPU] Modified kernel tag version to 8.10 (#34254)
  _Files: `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-08-10** [`3bb72bc72a`](https://github.com/sgl-project/sglang/commit/3bb72bc72a) [#34231](https://github.com/sgl-project/sglang/pull/34231)
  [CI] Keep the torch compilation cache instead of wiping it on install (#34231)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-08-10** [`7331287c1c`](https://github.com/sgl-project/sglang/commit/7331287c1c) [#26671](https://github.com/sgl-project/sglang/pull/26671)
  [JIT Kernel][DSv4] Optimize epilogue of c128 (#26671)
  _Files: `python/sglang/kernels/jit/csrc/deepseek_v4/c128_v2.cuh`_
- **2026-08-10** [`25b7015064`](https://github.com/sgl-project/sglang/commit/25b7015064) [#34184](https://github.com/sgl-project/sglang/pull/34184)
  Fix stale track rows corrupting conv checkpoints under the prefill graph (#34184)
  _Files: `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `test/registered/models_e2e/test_inkling_small_nvfp4.py`_

## Tensor / Data Parallel  (10 commits)

- **2026-08-17** [`0d8c850a35`](https://github.com/sgl-project/sglang/commit/0d8c850a35) [#35110](https://github.com/sgl-project/sglang/pull/35110)
  [Fix] Read the DSA prefill CP flag from the parallel config bag in bootstrap (#35110)
  _Files: `python/sglang/srt/distributed/bootstrap.py`_
- **2026-08-17** [`9be3044b9c`](https://github.com/sgl-project/sglang/commit/9be3044b9c) [#34999](https://github.com/sgl-project/sglang/pull/34999)
  [Engine] Freeze GC after server warmup (#34999)
  _Files: `python/sglang/srt/entrypoints/http_server.py`_
- **2026-08-17** [`0e500feae6`](https://github.com/sgl-project/sglang/commit/0e500feae6) [#34856](https://github.com/sgl-project/sglang/pull/34856)
  fix tpot by adjusting the sliding max-prefill-size window size (#34856)
  _Files: `test/registered/npu/performance/minimax_m2_5/test_npu_minimax_m2_5_w8a8_4p_in64k_out1k_prefix90_50ms.py`, `test/registered/npu/performance/qwen3-8b/test_npu_qwen3_8b_w8a8_1p_in3k5_out1k5_50ms.py`, `test/registered/npu/performance/qwen3_235b_a22b/test_npu_qwen3_235b_w8a8_8p_in3k5_out1k5_50ms.py`, `test/registered/npu/performance/qwen3_30b_a3b/test_npu_qwen3_30b_w8a8_1p_in3k5_out1k5_50ms.py` _+3 more__
- **2026-08-15** [`e5b3a48751`](https://github.com/sgl-project/sglang/commit/e5b3a48751) [#34796](https://github.com/sgl-project/sglang/pull/34796)
  Add --http2-max-concurrent-streams server arg (#34796)
  _Files: `docs/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/server_args.py`, `test/registered/openai_server/basic/test_http2_server.py` _+1 more__
- **2026-08-14** [`90b3db6dd8`](https://github.com/sgl-project/sglang/commit/90b3db6dd8) [#34319](https://github.com/sgl-project/sglang/pull/34319)
  [Fix: RL] Snapshot async state-capture outputs before overlap (#34319)
  _Files: `python/sglang/srt/state_capturer/base.py`_
- **2026-08-12** [`93e9db5eb8`](https://github.com/sgl-project/sglang/commit/93e9db5eb8) [#34447](https://github.com/sgl-project/sglang/pull/34447)
  [Fix][Qwen]: fused shared-expert detection PP-safe protection (#34447)
  _Files: `python/sglang/srt/models/qwen3_5.py`, `test/registered/unit/models/test_qwen3_5_pipeline_parallel.py`_
- **2026-08-11** [`857910bd35`](https://github.com/sgl-project/sglang/commit/857910bd35) [#34357](https://github.com/sgl-project/sglang/pull/34357)
  docs(semianalysis): Update Qwen3.5 B200 NVFP4 MTP config (#34357)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-08-10** [`2c72323d90`](https://github.com/sgl-project/sglang/commit/2c72323d90) [#34203](https://github.com/sgl-project/sglang/pull/34203)
  [AMD] Fix AITER custom reduce-scatter CUDA-graph capture crash under torch_memory_saver (#34203)
  _Files: `python/sglang/srt/distributed/parallel_state.py`_
- **2026-08-10** [`955aab8db1`](https://github.com/sgl-project/sglang/commit/955aab8db1) [#34213](https://github.com/sgl-project/sglang/pull/34213)
  [DCP] Reuse partial output in natural-log LSE merge (#34213)
  _Files: `python/sglang/srt/layers/dcp/comm.py`_
- **2026-08-10** [`68b961e9fb`](https://github.com/sgl-project/sglang/commit/68b961e9fb) [#33630](https://github.com/sgl-project/sglang/pull/33630)
  Add kda replayssm tests (#33630)
  _Files: `test/registered/kernels/test_kda_mtp_cutedsl_replayssm_ring.py`, `test/registered/kernels/test_kda_replayssm_fold.py`, `test/registered/kernels/test_kda_replayssm_fold_batched.py`, `test/registered/kernels/test_kda_replayssm_ring_fused.py` _+1 more__

## Speculative Decoding  (9 commits)

- **2026-08-17** [`711bdacb82`](https://github.com/sgl-project/sglang/commit/711bdacb82) [#35059](https://github.com/sgl-project/sglang/pull/35059)
  [Spec] Resolve shared-read ends from the backend declaration alone (#35059)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/speculative/ngram_worker.py` _+3 more__
- **2026-08-17** [`07a28ec5cf`](https://github.com/sgl-project/sglang/commit/07a28ec5cf) [#35064](https://github.com/sgl-project/sglang/pull/35064)
  docs: fix Qwen3.8-27B mamba ratio calculator for speculative decoding (#35064)
  _Files: `docs/cookbook/autoregressive/Qwen/Qwen3.8-27B.mdx`, `docs/src/snippets/_qwen38_mamba_ratio_calculator.jsx`_
- **2026-08-16** [`77cadf6b98`](https://github.com/sgl-project/sglang/commit/77cadf6b98) [#35057](https://github.com/sgl-project/sglang/pull/35057)
  [Spec] Point multi-layer eagle's last shared-read runner at the draft runner (#35057)
  _Files: `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-08-16** [`5534380d46`](https://github.com/sgl-project/sglang/commit/5534380d46) [#34696](https://github.com/sgl-project/sglang/pull/34696)
  [Spec] Support logprobs with DSpark speculative decoding (#34696)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/dspark_components/dspark_worker_v2.py`, `test/registered/core/test_basic_sanity_dspark.py`_
- **2026-08-15** [`7216a44dd8`](https://github.com/sgl-project/sglang/commit/7216a44dd8) [#34238](https://github.com/sgl-project/sglang/pull/34238)
  [AMD] Broadcast the EAGLE greedy verify decision across TP ranks on ROCm (#34238)
  _Files: `python/sglang/srt/speculative/eagle_utils.py`_
- **2026-08-14** [`c4271c3fe1`](https://github.com/sgl-project/sglang/commit/c4271c3fe1) [#34759](https://github.com/sgl-project/sglang/pull/34759)
  [DSpark] Fix EP1 decode performance regression (#34759)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_draft.py`_
- **2026-08-13** [`151a314829`](https://github.com/sgl-project/sglang/commit/151a314829) [#34782](https://github.com/sgl-project/sglang/pull/34782)
  [Fix] Make the DSpark draft num_token_non_padded host-to-device copy non-blocking (#34782)
  _Files: `python/sglang/srt/speculative/dspark_components/dspark_draft.py`_
- **2026-08-12** [`9d2d737ebf`](https://github.com/sgl-project/sglang/commit/9d2d737ebf) [#34520](https://github.com/sgl-project/sglang/pull/34520)
  [Benchmark] Remove 22 unmaintained benchmarks (#34520)
  _Files: `benchmark/bench_in_batch_prefix/bench_in_batch_prefix.py`, `benchmark/benchmark_batch/benchmark_batch.py`, `benchmark/benchmark_batch/benchmark_tokenizer.py`, `benchmark/benchmark_vllm_060/README.md` _+77 more__
- **2026-08-10** [`430f38ea25`](https://github.com/sgl-project/sglang/commit/430f38ea25) [#34250](https://github.com/sgl-project/sglang/pull/34250)
  Update dspark draft path in Inkling small cookbook (#34250)
  _Files: `docs/cookbook/autoregressive/ThinkingMachines/Inkling-Small.mdx`, `docs/src/snippets/configs/thinkingmachines/inkling-small.jsx`_

## CI / Build  (9 commits)

- **2026-08-15** [`3802a725ac`](https://github.com/sgl-project/sglang/commit/3802a725ac) [#34961](https://github.com/sgl-project/sglang/pull/34961)
  [CI] Pin the allowed_media_domains supplied-instance reads in the step-12 ratchet (#34961)
  _Files: `test/registered/unit/test_supplied_instance_exposure_ratchet.py`_
- **2026-08-15** [`8d44091326`](https://github.com/sgl-project/sglang/commit/8d44091326) [#34914](https://github.com/sgl-project/sglang/pull/34914)
  Update sgl-deep-ep release workflow for DeepEP v2 (#34914)
  _Files: `.github/workflows/release-whl-deepep.yml`, `docker/sgl-deep-ep.Dockerfile`_
- **2026-08-15** [`e99ecb6eee`](https://github.com/sgl-project/sglang/commit/e99ecb6eee) [#34864](https://github.com/sgl-project/sglang/pull/34864)
  [CI] Path-gate Rust workspace tests in lint (#34864)
  _Files: `.github/workflows/lint.yml`_
- **2026-08-13** [`9c0d4cba3f`](https://github.com/sgl-project/sglang/commit/9c0d4cba3f) [#34669](https://github.com/sgl-project/sglang/pull/34669)
  [CI] Split Kimi K2.5 performance batches by config (#34669)
  _Files: `test/registered/gb300/test_kimi_k25_nvfp4.py`_
- **2026-08-13** [`d44c836cfd`](https://github.com/sgl-project/sglang/commit/d44c836cfd) [#34567](https://github.com/sgl-project/sglang/pull/34567)
  [XPU][CI] disable SYCL_CACHE_PERSISTENT to fix topk segfault (#34567)
  _Files: `scripts/ci/xpu/xpu_ci_start_container.sh`_
- **2026-08-12** [`256981ce16`](https://github.com/sgl-project/sglang/commit/256981ce16) [#34195](https://github.com/sgl-project/sglang/pull/34195)
  [CI] Align rerun-test environment with the test stages (#34195)
  _Files: `.github/workflows/rerun-test.yml`_
- **2026-08-11** [`396722e490`](https://github.com/sgl-project/sglang/commit/396722e490) [#34377](https://github.com/sgl-project/sglang/pull/34377)
  [NPU] Disable failed test cases (#34377)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-08-11** [`d8a61c26a6`](https://github.com/sgl-project/sglang/commit/d8a61c26a6) [#34380](https://github.com/sgl-project/sglang/pull/34380)
  [CI] Add a scheduled workflow to close stale PRs (#34380)
  _Files: `.github/workflows/close-stale-prs.yml`_
- **2026-08-10** [`410088c91e`](https://github.com/sgl-project/sglang/commit/410088c91e) [#34103](https://github.com/sgl-project/sglang/pull/34103)
  [NPU] Increase the retry count to 3 for the GSM8K. (#34103)
  _Files: `.github/workflows/_npu-single-node-test-stage.yml`, `python/sglang/test/ascend/e2e/test_npu_accuracy_utils.py`_

## ROCm / AMD  (8 commits)

- **2026-08-16** [`d91c3682b0`](https://github.com/sgl-project/sglang/commit/d91c3682b0) [#34645](https://github.com/sgl-project/sglang/pull/34645)
  [AMD][CI] Add GPT-OSS perf benchmarks to the ROCm 7.2 nightly (#34645)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `python/sglang/test/nightly_bench_utils.py`, `test/registered/amd/perf/mi30x/test_gpt_oss_perf_amd.py`, `test/registered/amd/perf/mi35x/test_gpt_oss_perf_mi35x.py`_
- **2026-08-15** [`5c9ee86d90`](https://github.com/sgl-project/sglang/commit/5c9ee86d90) [#34913](https://github.com/sgl-project/sglang/pull/34913)
  [CI] Move the static ratchets back to CPU unit tests (#34913)
  _Files: `.claude/rules/unit-test-admission.md`, `.claude/skills/sglang-runtime-context/SKILL.md`, `.pre-commit-config.yaml`, `python/sglang/srt/server_args.py` _+10 more__
- **2026-08-15** [`5afdb1caea`](https://github.com/sgl-project/sglang/commit/5afdb1caea) [#34877](https://github.com/sgl-project/sglang/pull/34877)
  [AMD CI] follow the miles nightly-prefixed MI350 suite names (#34877)
  _Files: `.github/workflows/nightly-test-amd-miles-rocm720.yml`_
- **2026-08-14** [`34219ed9a7`](https://github.com/sgl-project/sglang/commit/34219ed9a7) [#34768](https://github.com/sgl-project/sglang/pull/34768)
  [AMD] CI: pin antlr4-python3-runtime back after lmms-eval (unblocks ROCm 7.2 stage-b evals) (#34768)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-08-13** [`29b067245b`](https://github.com/sgl-project/sglang/commit/29b067245b) [#34689](https://github.com/sgl-project/sglang/pull/34689)
  [AMD] CI: drop the spaces from SGL_EVAL_SPEC (fixes ROCm 7.2 stage-a sgl-eval install) (#34689)
  _Files: `scripts/ci/utils/sgl_eval_ref.sh`_
- **2026-08-13** [`07821e9d56`](https://github.com/sgl-project/sglang/commit/07821e9d56) [#34643](https://github.com/sgl-project/sglang/pull/34643)
  [AMD][CI] Stop scheduling Grok-1 and Grok-2 on MI30x (#34643)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`_
- **2026-08-12** [`00bdafe944`](https://github.com/sgl-project/sglang/commit/00bdafe944) [#34204](https://github.com/sgl-project/sglang/pull/34204)
  [AMD][CI] Swap the AMD PR gate to ROCm 7.2 and demote ROCm 7.0 to a daily shadow (#34204)
  _Files: `.github/workflows/amd-aiter-scout.yml`, `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/bot-bump-sglang-version.yml`, `.github/workflows/nightly-test-amd.yml` _+8 more__
- **2026-08-11** [`8d050dd880`](https://github.com/sgl-project/sglang/commit/8d050dd880) [#34324](https://github.com/sgl-project/sglang/pull/34324)
  [AMD][CI] Run MI300 8-GPU stage-C shards two at a time (#34324)
  _Files: `.github/workflows/pr-test-amd.yml`_

## Scheduler / Batching  (7 commits)

- **2026-08-17** [`12a455a910`](https://github.com/sgl-project/sglang/commit/12a455a910) [#34997](https://github.com/sgl-project/sglang/pull/34997)
  Fix world-size-one aliasing in MLP batch sync (#34997)
  _Files: `python/sglang/srt/managers/scheduler_components/dp_attn.py`_
- **2026-08-15** [`8720a72814`](https://github.com/sgl-project/sglang/commit/8720a72814) [#34284](https://github.com/sgl-project/sglang/pull/34284)
  fix(scheduler): track max prefill batch size over recent real admissions (#34284)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/prefill_delayer.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/npu/performance/kimi_k2_6/test_npu_kimi_k2_6_w4a8_8p_in3k5_out1k5_20ms.py` _+3 more__
- **2026-08-14** [`be804c1b83`](https://github.com/sgl-project/sglang/commit/be804c1b83) [#33593](https://github.com/sgl-project/sglang/pull/33593)
  [RL] Expose top-p-only sampling masks (#33593)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/sampling/test_sampling_mask.py` _+2 more__
- **2026-08-13** [`6b94d39f13`](https://github.com/sgl-project/sglang/commit/6b94d39f13) [#32017](https://github.com/sgl-project/sglang/pull/32017)
  [Model Loading] Overlap checkpoint staging with CUDA graph capture during startup (#32017)
  _Files: `python/sglang/benchmark/one_batch.py`, `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `python/sglang/srt/managers/scheduler.py` _+12 more__
- **2026-08-13** [`eea2e5d6e5`](https://github.com/sgl-project/sglang/commit/eea2e5d6e5) [#32637](https://github.com/sgl-project/sglang/pull/32637)
  Optimize delayed sample and mrope position computation (#32637)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py`, `python/sglang/srt/model_executor/forward_batch_info.py`_
- **2026-08-11** [`aadb9720fe`](https://github.com/sgl-project/sglang/commit/aadb9720fe) [#33940](https://github.com/sgl-project/sglang/pull/33940)
  fix: route scheduler aborts to multi-tokenizer workers (#33940)
  _Files: `python/sglang/srt/managers/scheduler_components/output_sender.py`, `test/registered/unit/managers/scheduler_components/test_output_sender.py`_
- **2026-08-10** [`fb3d1419fd`](https://github.com/sgl-project/sglang/commit/fb3d1419fd) [#30023](https://github.com/sgl-project/sglang/pull/30023)
  [tracing] sglang tracing v2: support exporting tracing data asynchronously (#30023)
  _Files: `docs/docs/references/environment_variables.mdx`, `docs/docs/references/production_request_trace.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py` _+4 more__

## Serving / API  (4 commits)

- **2026-08-16** [`32e6fb4fdc`](https://github.com/sgl-project/sglang/commit/32e6fb4fdc) [#35001](https://github.com/sgl-project/sglang/pull/35001)
  [Frontend] Apply request header overrides to chat completions (#35001)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`_
- **2026-08-16** [`6bb73082c8`](https://github.com/sgl-project/sglang/commit/6bb73082c8) [#35015](https://github.com/sgl-project/sglang/pull/35015)
  Add skill for babysitting PR CI (#35015)
  _Files: `.claude/skills/babysit-pr-to-pass-ci/SKILL.md`, `.claude/skills/babysit-pr-to-pass-ci/agents/openai.yaml`_
- **2026-08-14** [`6f005e4da1`](https://github.com/sgl-project/sglang/commit/6f005e4da1) [#34777](https://github.com/sgl-project/sglang/pull/34777)
  [Fix] Require JSON booleans for response_format json_schema.strict (#34777)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `test/registered/unit/entrypoints/openai/test_protocol.py`_
- **2026-08-13** [`fd1e04d952`](https://github.com/sgl-project/sglang/commit/fd1e04d952) [#33894](https://github.com/sgl-project/sglang/pull/33894)
  refactor error responses into shared utils::response helpers (#33894)
  _Files: `rust/sglang-server/src/api_server/frame.rs`, `rust/sglang-server/src/api_server/native_api.rs`, `rust/sglang-server/src/api_server/openai.rs`, `rust/sglang-server/src/api_server/openai/chat.rs` _+6 more__

## Structured Output  (2 commits)

- **2026-08-14** [`3f64f14360`](https://github.com/sgl-project/sglang/commit/3f64f14360) [#34778](https://github.com/sgl-project/sglang/pull/34778)
  [Fix] Work around xgrammar 0.2.1 negative integer minimum in Kimi-K3 structural tags (#34778)
  _Files: `python/sglang/srt/function_call/kimik3_structural_tag.py`, `test/registered/unit/function_call/test_kimik3_structural_tag.py`_
- **2026-08-14** [`42e8718d3d`](https://github.com/sgl-project/sglang/commit/42e8718d3d) [#34781](https://github.com/sgl-project/sglang/pull/34781)
  fix(muse-glimmer): parse required/named tool calls natively (#34781)
  _Files: `python/sglang/srt/function_call/muse_glimmer_detector.py`_

---
_Generated 2026-08-17 08:53 UTC_