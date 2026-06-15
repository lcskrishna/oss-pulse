# sgl-project/sglang — Weekly Change Report
**Period:** 2026-06-08 → 2026-06-15  |  **Total commits:** 373

## ✨ New Features This Week

- **2026-06-15** [#28223](https://github.com/sgl-project/sglang/pull/28223) — [NPU] Add MiMo-V2-Flash manual testcases (#28223)
- **2026-06-15** [#28207](https://github.com/sgl-project/sglang/pull/28207) — docs(minimax-m3): refresh B200 benchmarks (tp8, piecewise) + add GPQA (#28207)
- **2026-06-15** [#28205](https://github.com/sgl-project/sglang/pull/28205) — [diffusion] feat: persist torch.compile inductor/triton cache across restarts (#28205)
- **2026-06-15** [#27122](https://github.com/sgl-project/sglang/pull/27122) — feat: report multimodal (image/audio/video) token counts in usage.prompt_tokens_details (#27122)
- **2026-06-14** [#28206](https://github.com/sgl-project/sglang/pull/28206) — ci(docker): support layered overlay images in release-docker-dev (#28206)
- **2026-06-14** [#28193](https://github.com/sgl-project/sglang/pull/28193) — [diffusion] feat: use regional torch.compile (compile_repeated_blocks) for DiT of diffusers backend (#28193)
- **2026-06-14** [#28184](https://github.com/sgl-project/sglang/pull/28184) — [diffusion] feat: add --warmup-mode enum server arg (#28184)
- **2026-06-14** [#28071](https://github.com/sgl-project/sglang/pull/28071) — [diffusion] feat: enable spatial-shard vae decode across GPUs (#28071)
- **2026-06-14** [#27469](https://github.com/sgl-project/sglang/pull/27469) — dflash add sliding window attention draft layer support (#27469)
- **2026-06-14** [#28165](https://github.com/sgl-project/sglang/pull/28165) — Unify NVTX annotation helpers and split the enable gate per subsystem (#28165)
- _…and 94 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-06-15** [`c4ec39a785`](https://github.com/sgl-project/sglang/commit/c4ec39a785) [#28265](https://github.com/sgl-project/sglang/pull/28265) — [AMD] refactor sparse MLA decode kernel for Deepseek V4 triton backend (#28265)
- **2026-06-15** [`da12f36629`](https://github.com/sgl-project/sglang/commit/da12f36629) [#28275](https://github.com/sgl-project/sglang/pull/28275) — [AMD] Refactor unified_kv attention metadata to data class and fuse c4/128 out_loc (#28275)
- **2026-06-15** [`9864059e2b`](https://github.com/sgl-project/sglang/commit/9864059e2b) [#28249](https://github.com/sgl-project/sglang/pull/28249) — [AMD] Update AITER commit (#28249)
- **2026-06-15** [`19c78552dc`](https://github.com/sgl-project/sglang/commit/19c78552dc) [#28263](https://github.com/sgl-project/sglang/pull/28263) — [AMD] Restrict CI image fallback to versioned tags (#28263)
- **2026-06-15** [`63df86f5e7`](https://github.com/sgl-project/sglang/commit/63df86f5e7) [#22985](https://github.com/sgl-project/sglang/pull/22985) — [AMD] Skip eplb bookkeeping and topk remap when EPLB is not in use on mori-ep / HIP (#22985) (#28188)
- **2026-06-15** [`c127ba6483`](https://github.com/sgl-project/sglang/commit/c127ba6483) [#28214](https://github.com/sgl-project/sglang/pull/28214) — [AMD] ci: fix scheduled AMD runs startup failure when calling extra-a suite (#28214)
- **2026-06-14** [`f18d38d040`](https://github.com/sgl-project/sglang/commit/f18d38d040) [#28213](https://github.com/sgl-project/sglang/pull/28213) — Revert "[AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs" (#28213)
- **2026-06-13** [`3f4a338212`](https://github.com/sgl-project/sglang/commit/3f4a338212) [#18182](https://github.com/sgl-project/sglang/pull/18182) — [AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs (#18182)
- **2026-06-13** [`10d3337048`](https://github.com/sgl-project/sglang/commit/10d3337048) [#27935](https://github.com/sgl-project/sglang/pull/27935) — [AMD] Support unified_kv_triton for disaggregation (#27935)
- **2026-06-13** [`bde6bccf39`](https://github.com/sgl-project/sglang/commit/bde6bccf39) [#28129](https://github.com/sgl-project/sglang/pull/28129) — [Spec] Remove deprecated EAGLE v1 DRAFT_EXTEND forward mode (#28129)
- **2026-06-13** [`60d4bd4c70`](https://github.com/sgl-project/sglang/commit/60d4bd4c70) [#27855](https://github.com/sgl-project/sglang/pull/27855) — [AMD] fix moriep quant kernel not implemented issue (#27855)
- **2026-06-13** [`eb9483b5c2`](https://github.com/sgl-project/sglang/commit/eb9483b5c2) [#26288](https://github.com/sgl-project/sglang/pull/26288) — [PD][AMD]: incremental KV transfer with decode radix cache (#26288)
- **2026-06-13** [`bcd45d3ac7`](https://github.com/sgl-project/sglang/commit/bcd45d3ac7) [#28112](https://github.com/sgl-project/sglang/pull/28112) — [AMD][DFlash] Add DFlash test to AMD CI (#28112)
- **2026-06-13** [`053e153183`](https://github.com/sgl-project/sglang/commit/053e153183) [#27817](https://github.com/sgl-project/sglang/pull/27817) — [AMD] ci: register 8 attention-backend unit tests to run on AMD CI (#27817)
- **2026-06-13** [`f288283c07`](https://github.com/sgl-project/sglang/commit/f288283c07) [#27057](https://github.com/sgl-project/sglang/pull/27057) — [AMD] move shared expert check function to quark (#27057)
- **2026-06-12** [`fda7955890`](https://github.com/sgl-project/sglang/commit/fda7955890) [#27854](https://github.com/sgl-project/sglang/pull/27854) — [AMD][DFlash] Enable Fused KV Materialization (#27854)
- **2026-06-12** [`87554c7855`](https://github.com/sgl-project/sglang/commit/87554c7855) [#28093](https://github.com/sgl-project/sglang/pull/28093) — [Spec] Move draft-extend prep to `EagleDraftWorkerBase`; unify `prepare_for_*` names (#28093)
- **2026-06-12** [`54989b1fd0`](https://github.com/sgl-project/sglang/commit/54989b1fd0) [#27822](https://github.com/sgl-project/sglang/pull/27822) — [AMD] ci: add label-gated extra-a tier (kv_canary + mock_model unit tests) (#27822)
- **2026-06-12** [`65d76bd3f6`](https://github.com/sgl-project/sglang/commit/65d76bd3f6) [#28075](https://github.com/sgl-project/sglang/pull/28075) — [AMD] Fix CI base-a `fwd_occupancy`: disable `SGLANG_SANITIZE_NAN_LOGITS` in AMD CI (#28075)
- **2026-06-12** [`371b96e210`](https://github.com/sgl-project/sglang/commit/371b96e210) [#27972](https://github.com/sgl-project/sglang/pull/27972) — [AMD] Fix DeepSeek-V4-Flash-FP8 on MI300 (#27972)
- **2026-06-12** [`1cd5cb1220`](https://github.com/sgl-project/sglang/commit/1cd5cb1220) [#27149](https://github.com/sgl-project/sglang/pull/27149) — [AMD] [CI] Add dsv4 accuracy PR gate to pr-test-amd-rocm720 (#27149)
- **2026-06-12** [`36d61613a1`](https://github.com/sgl-project/sglang/commit/36d61613a1) [#27978](https://github.com/sgl-project/sglang/pull/27978) — [AMD] Cache unified_kv swa_loc once per step instead of per layer (#27978)
- **2026-06-12** [`cce35ee2e5`](https://github.com/sgl-project/sglang/commit/cce35ee2e5) [#27994](https://github.com/sgl-project/sglang/pull/27994) — Remove outdated patch (#27994)
- **2026-06-12** [`ddbe5ff2f1`](https://github.com/sgl-project/sglang/commit/ddbe5ff2f1) [#27999](https://github.com/sgl-project/sglang/pull/27999) — [AMD] Pin maturin<1.14 to fix ROCm image build failure (#27999)
- **2026-06-12** [`3ffe72517f`](https://github.com/sgl-project/sglang/commit/3ffe72517f) [#27977](https://github.com/sgl-project/sglang/pull/27977) — [Spec] Remove the dead spec V1 scheduler paths (#27977)
- **2026-06-11** [`c0480a88be`](https://github.com/sgl-project/sglang/commit/c0480a88be) [#27964](https://github.com/sgl-project/sglang/pull/27964) — [Spec] Retire Spec V1 (#27964)
- **2026-06-11** [`949326d922`](https://github.com/sgl-project/sglang/commit/949326d922) [#27967](https://github.com/sgl-project/sglang/pull/27967) — Add SGLANG_ENABLE_WAR_BARRIER to force-enable the overlap scheduler WAR barrier on non-CUDA (e.g. AMD) (#27967)
- **2026-06-11** [`acdb39edd2`](https://github.com/sgl-project/sglang/commit/acdb39edd2) [#27959](https://github.com/sgl-project/sglang/pull/27959) — [Spec] Remove the DFLASH V1 worker path (#27959)
- **2026-06-11** [`6e885c844f`](https://github.com/sgl-project/sglang/commit/6e885c844f) [#27919](https://github.com/sgl-project/sglang/pull/27919) — Revert "[AMD] Fix DeepSeek V4 Pro c128 state tensor dtype mismatch error and c4_sparse_raw_indices attribute error in cuda graph phase" (#27919)
- **2026-06-11** [`12d3f02be8`](https://github.com/sgl-project/sglang/commit/12d3f02be8) [#27850](https://github.com/sgl-project/sglang/pull/27850) — [AMD] Fix DSA device-to-host direct test on rocm720 (page_size%16 assert) (#27850)
- **2026-06-11** [`22c7285a26`](https://github.com/sgl-project/sglang/commit/22c7285a26) [#27630](https://github.com/sgl-project/sglang/pull/27630) — [AMD] Fuse sigmoid + mul attention output gate into single Triton kernel (#27630)
- **2026-06-11** [`f4b3b99413`](https://github.com/sgl-project/sglang/commit/f4b3b99413) [#27583](https://github.com/sgl-project/sglang/pull/27583) — [AMD] Enable fused GDN QKV split Triton kernel on HIP (#27583)
- **2026-06-11** [`b8376aebd0`](https://github.com/sgl-project/sglang/commit/b8376aebd0) [#27858](https://github.com/sgl-project/sglang/pull/27858) — [AMD] Fix the dsv4 performance of MoE issue. (#27858)
- **2026-06-11** [`f4f30d7d23`](https://github.com/sgl-project/sglang/commit/f4f30d7d23) [#27840](https://github.com/sgl-project/sglang/pull/27840) — [Fix] Use int64 seq_lens across all CUDA graph runners and backends (#27840)
- **2026-06-11** [`588d1f7bc9`](https://github.com/sgl-project/sglang/commit/588d1f7bc9) [#23000](https://github.com/sgl-project/sglang/pull/23000) — [Feature] Spec V2 DFlash Support (#23000)
- **2026-06-11** [`99ab90c5b7`](https://github.com/sgl-project/sglang/commit/99ab90c5b7) [#27811](https://github.com/sgl-project/sglang/pull/27811) — [AMD] Restore AMD piecewise CUDA graph support dropped by #23906 (#27811)
- **2026-06-10** [`0da18f8d91`](https://github.com/sgl-project/sglang/commit/0da18f8d91) [#27656](https://github.com/sgl-project/sglang/pull/27656) — [AMD][Perf] Fuse QK RMSNorm + gate extraction Triton kernel for Qwen3.5 on HIP (#27656)
- **2026-06-10** [`0ae27405d0`](https://github.com/sgl-project/sglang/commit/0ae27405d0) [#22985](https://github.com/sgl-project/sglang/pull/22985) — [AMD] Support eplb for moriep (#22985)
- **2026-06-10** [`6a16f29af6`](https://github.com/sgl-project/sglang/commit/6a16f29af6) [#25939](https://github.com/sgl-project/sglang/pull/25939) — [AMD] ci: register 8 framework / unit tests to run on AMD CI (#25939)
- **2026-06-10** [`502bc89e1b`](https://github.com/sgl-project/sglang/commit/502bc89e1b) [#27529](https://github.com/sgl-project/sglang/pull/27529) — [AMD] Fix DeepSeek V4 Pro c128 state tensor dtype mismatch error and c4_sparse_raw_indices attribute error in cuda graph phase (#27529)
- **2026-06-10** [`4faaa9ba92`](https://github.com/sgl-project/sglang/commit/4faaa9ba92) [#27803](https://github.com/sgl-project/sglang/pull/27803) — [CI] Fix stale ngram bookkeeping owner sites (#27803)
- **2026-06-10** [`b0d888a195`](https://github.com/sgl-project/sglang/commit/b0d888a195) [#27795](https://github.com/sgl-project/sglang/pull/27795) — [CI] Remove AMD DSv4 Docker publish job (#27795)
- **2026-06-10** [`f2bcdb0508`](https://github.com/sgl-project/sglang/commit/f2bcdb0508) [#27380](https://github.com/sgl-project/sglang/pull/27380) — [AMD] Add unified kv attention support in dpsk-v4 (#27380)
- **2026-06-10** [`95d8a75bc9`](https://github.com/sgl-project/sglang/commit/95d8a75bc9) [#27695](https://github.com/sgl-project/sglang/pull/27695) — Bundle set_kv_buffer write targets into KVWriteLoc (loc + swa_loc) (#27695)
- **2026-06-10** [`758fd4bb9a`](https://github.com/sgl-project/sglang/commit/758fd4bb9a) [#27617](https://github.com/sgl-project/sglang/pull/27617) — [SWA] Cache full→SWA out_cache_loc per forward across attention backends (#27617)
- **2026-06-10** [`4704b10d0d`](https://github.com/sgl-project/sglang/commit/4704b10d0d) [#27669](https://github.com/sgl-project/sglang/pull/27669) — [AMD] Update MoRI to v1.2.0 (#27669)
- **2026-06-10** [`f42a093261`](https://github.com/sgl-project/sglang/commit/f42a093261) [#27722](https://github.com/sgl-project/sglang/pull/27722) — [AMD] Migrate 2-GPU kernel allreduce tests into the registered system (#27722)
- **2026-06-10** [`f332e52611`](https://github.com/sgl-project/sglang/commit/f332e52611) [#27710](https://github.com/sgl-project/sglang/pull/27710) — Add UT guarding per-request bookkeeping clock ownership (#27710)
- **2026-06-09** [`9ab7a64ee1`](https://github.com/sgl-project/sglang/commit/9ab7a64ee1) [#27660](https://github.com/sgl-project/sglang/pull/27660) — [AMD] Update amd qwen3.5 cookbook (#27660)
- **2026-06-09** [`2fef951fe8`](https://github.com/sgl-project/sglang/commit/2fef951fe8) [#23927](https://github.com/sgl-project/sglang/pull/23927) — [AMD] Replace fp8 mla with fp8 mha kernel for diffusion model aiter backend (#23927)
- **2026-06-09** [`5babb902a9`](https://github.com/sgl-project/sglang/commit/5babb902a9) [#27581](https://github.com/sgl-project/sglang/pull/27581) — [AMD] fix: handle per-frame 4D shift in native scale-shift kernel (#27581)
- **2026-06-09** [`17d8c5801d`](https://github.com/sgl-project/sglang/commit/17d8c5801d) [#27505](https://github.com/sgl-project/sglang/pull/27505) — [AMD] Fix test_deepseek_r1_mxfp4_8gpu.py : disable async-assert probes on AMD CI (#27505)
- **2026-06-09** [`a32aeb688a`](https://github.com/sgl-project/sglang/commit/a32aeb688a) [#27580](https://github.com/sgl-project/sglang/pull/27580) — [AMD] Fix AttributeError in GeneratedSharedPrefixDataset.from_args for in-process callers (#27580)
- **2026-06-08** [`ea1d190ed0`](https://github.com/sgl-project/sglang/commit/ea1d190ed0) [#27289](https://github.com/sgl-project/sglang/pull/27289) — [ROCm] dsv4: remove the redundant fp8 scale transpose-copy on decode (#27289)
- **2026-06-08** [`3607cbd65a`](https://github.com/sgl-project/sglang/commit/3607cbd65a) [#27555](https://github.com/sgl-project/sglang/pull/27555) — [AMD] update ROCm AITER commit (#27555)
- **2026-06-08** [`61e4132bc2`](https://github.com/sgl-project/sglang/commit/61e4132bc2) [#27537](https://github.com/sgl-project/sglang/pull/27537) — [MUSA] bump torchada version to 0.1.59 and workaround PCG limitation. (#27537)
- **2026-06-08** [`a26587dd4e`](https://github.com/sgl-project/sglang/commit/a26587dd4e) [#22786](https://github.com/sgl-project/sglang/pull/22786) — [AMD][diffusion] Add FlyDSL fused normalization kernels for ROCm diffusion models optimization (#22786)
- **2026-06-08** [`8ff0c9fef9`](https://github.com/sgl-project/sglang/commit/8ff0c9fef9) [#27534](https://github.com/sgl-project/sglang/pull/27534) — [PD] Downgrade propagated rank failure logs from error to debug (#27534)
- **2026-06-08** [`df6b9c2d9d`](https://github.com/sgl-project/sglang/commit/df6b9c2d9d) [#27538](https://github.com/sgl-project/sglang/pull/27538) — [AMD] ci: reinstall MoRI if Different from Dockerfile-pinned commit during install_dependency (#27538)
- **2026-06-08** [`18d728967a`](https://github.com/sgl-project/sglang/commit/18d728967a) [#26922](https://github.com/sgl-project/sglang/pull/26922) — [PD][MoRI] Drive KV transfers with a sharded synchronous worker pool (#26922)
- **2026-06-08** [`1aa5040c74`](https://github.com/sgl-project/sglang/commit/1aa5040c74) [#27530](https://github.com/sgl-project/sglang/pull/27530) — Update code owners (AMD) (#27530)
- **2026-06-08** [`1c73ff8ad3`](https://github.com/sgl-project/sglang/commit/1c73ff8ad3) [#27063](https://github.com/sgl-project/sglang/pull/27063) — [AMD] Optimize gpt-oss-120B performance (#27063)
- **2026-06-08** [`303757ccd8`](https://github.com/sgl-project/sglang/commit/303757ccd8) [#27485](https://github.com/sgl-project/sglang/pull/27485) — [Attn] Fix aiter MLA verify `kv_indices` under-alloc + shared `assert_buffer_fits` guard (#27485)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17050](https://github.com/sgl-project/sglang/issues/17050) | [Tracking] CI Test Failures and Fixes | — | 2026-06-15 |
| [#27937](https://github.com/sgl-project/sglang/issues/27937) | [Failure Tracker] PR Test (AMD) | — | 2026-06-15 |
| [#25887](https://github.com/sgl-project/sglang/issues/25887) | [Bug] CP+PP Occur RuntimeError: The size of tensor a (4) must match th | — | 2026-06-15 |
| [#28300](https://github.com/sgl-project/sglang/issues/28300) | Performance regression on 8x B300 Llama-4-Scout after PR #27091 (AIPer | — | 2026-06-15 |
| [#28298](https://github.com/sgl-project/sglang/issues/28298) | gRPC mode: --enable-metrics error message cites wrong servicer version | — | 2026-06-15 |
| [#26324](https://github.com/sgl-project/sglang/issues/26324) | [Bug] flashinfer_trtllm MoE runner corrupts MiniMax-M2.7-NVFP4 output  | — | 2026-06-15 |
| [#27574](https://github.com/sgl-project/sglang/issues/27574) | [Agentic Inference] Programmatic KV Cache for Agentic Workloads | high priority | 2026-06-15 |
| [#28272](https://github.com/sgl-project/sglang/issues/28272) | [Bug][NPU] Qwen3.6-35B-A3B crash with prefix cache | — | 2026-06-15 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-06-15 |
| [#26890](https://github.com/sgl-project/sglang/issues/26890) | [AITER-Upgrade] AITER Scout Status | — | 2026-06-15 |
| [#28011](https://github.com/sgl-project/sglang/issues/28011) | [Bug] Intermittent NCCL hang during Spec V2 verify with DSA backend +  | speculative-decoding | 2026-06-15 |
| [#27521](https://github.com/sgl-project/sglang/issues/27521) | [AMD] PR CI new test cases to cover | amd | 2026-06-13 |
| [#28152](https://github.com/sgl-project/sglang/issues/28152) | [Bug] After enabling MTP on the NPU platform, the startup is abnormal, | — | 2026-06-13 |
| [#28141](https://github.com/sgl-project/sglang/issues/28141) | [Bug] DeepSeek-V4-Flash on ROCm MI350X fails during weight loading: `M | — | 2026-06-13 |
| [#20372](https://github.com/sgl-project/sglang/issues/20372) | [Feature] Introduce hardware plugin system | — | 2026-06-12 |
| [#28019](https://github.com/sgl-project/sglang/issues/28019) | [Bug] Gemma-4-26B-A4B FP8 Dynamic fused-MoE exceeds SM121 shared memor | — | 2026-06-12 |
| [#28018](https://github.com/sgl-project/sglang/issues/28018) | [Bug] Gemma-4-31B QAT W4A16 CT fails gptq_marlin_repack on SM121 | — | 2026-06-12 |
| [#28020](https://github.com/sgl-project/sglang/issues/28020) | [Feature] Support Mistral-native checkpoints via --config-format mistr | — | 2026-06-12 |
| [#27418](https://github.com/sgl-project/sglang/issues/27418) | [Mamba] Clean up _handle_mamba_radix_cache and rename mamba_scheduler_ | — | 2026-06-12 |
| [#26702](https://github.com/sgl-project/sglang/issues/26702) | [RFC] TensorCast KV backend integration | — | 2026-06-12 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 78 |
| Multimodal | 40 |
| KV Cache / Memory | 32 |
| Prefill / Decode Disaggregation | 29 |
| Docs / Examples | 26 |
| MoE / Expert Parallel | 26 |
| Speculative Decoding | 23 |
| Other | 22 |
| Tensor / Data Parallel | 15 |
| Triton / Kernels | 14 |
| ROCm / AMD | 14 |
| CI / Build | 14 |
| Models | 12 |
| Quantization | 12 |
| Scheduler / Batching | 10 |
| Structured Output | 3 |
| LoRA | 2 |
| Serving / API | 1 |

## Attention / FlashInfer  (78 commits)

- **2026-06-15** [`20f4272109`](https://github.com/sgl-project/sglang/commit/20f4272109) [#28073](https://github.com/sgl-project/sglang/pull/28073)
  fix: Fix DSR1 perf regression due to unnecessarily falling back to triton gemm (#28073)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/model_loader/utils.py`, `test/registered/unit/layers/quantization/test_flashinfer_trtllm_fp8_fallback.py`_
- **2026-06-15** [`09e9c4fde3`](https://github.com/sgl-project/sglang/commit/09e9c4fde3) [#28118](https://github.com/sgl-project/sglang/pull/28118)
  【bugfix】The NPU's forward_dsa_prepare_npu also needs special handling for is_nextn (#28118)
  _Files: `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`_
- **2026-06-15** [`3df6e2f968`](https://github.com/sgl-project/sglang/commit/3df6e2f968) [#28223](https://github.com/sgl-project/sglang/pull/28223)
  [NPU] Add MiMo-V2-Flash manual testcases (#28223)
  _Files: `python/sglang/test/ascend/test_ascend_utils.py`, `test/manual/ascend/llm_models/test_npu_mimo_v2_flash.py`_
- **2026-06-15** [`c4ec39a785`](https://github.com/sgl-project/sglang/commit/c4ec39a785) [#28265](https://github.com/sgl-project/sglang/pull/28265)
  [AMD] refactor sparse MLA decode kernel for Deepseek V4 triton backend (#28265)
  _Files: `python/sglang/srt/layers/attention/nsa/triton_decode/triton_mla_kernels_decode_common.py`, `python/sglang/srt/layers/attention/nsa/triton_decode/triton_mla_kernels_decode_dsv4.py`, `python/sglang/srt/layers/attention/nsa/triton_decode/triton_mla_kernels_decode_fused.py`, `python/sglang/srt/layers/attention/nsa/triton_decode/triton_mla_kernels_decode_optimized.py` _+1 more__
- **2026-06-15** [`da12f36629`](https://github.com/sgl-project/sglang/commit/da12f36629) [#28275](https://github.com/sgl-project/sglang/pull/28275)
  [AMD] Refactor unified_kv attention metadata to data class and fuse c4/128 out_loc (#28275)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`, `python/sglang/srt/layers/attention/dsv4/unified_kv_kernels/env_gate.py`_
- **2026-06-15** [`1a66059c4e`](https://github.com/sgl-project/sglang/commit/1a66059c4e) [#28192](https://github.com/sgl-project/sglang/pull/28192)
  [Spec] Restore index_share_for_mtp_iteration in EAGLE V2 draft worker (#28192)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/standalone_worker_v2.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_draft_runner.py`_
- **2026-06-14** [`8c5320b37e`](https://github.com/sgl-project/sglang/commit/8c5320b37e) [#27469](https://github.com/sgl-project/sglang/pull/27469)
  dflash add sliding window attention draft layer support (#27469)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/srt/speculative/dflash_utils.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_target_verify_runner.py` _+2 more__
- **2026-06-14** [`37ed10bd24`](https://github.com/sgl-project/sglang/commit/37ed10bd24) [#28169](https://github.com/sgl-project/sglang/pull/28169)
  [diffusion] UX: reduce attention backend log noise (#28169)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/selector.py`, `python/sglang/multimodal_gen/runtime/platforms/cuda.py`_
- **2026-06-14** [`1747b88c5e`](https://github.com/sgl-project/sglang/commit/1747b88c5e) [#28110](https://github.com/sgl-project/sglang/pull/28110)
  [LoRA] Support DSA indexer LoRA targets for GLM-5.1 / DeepSeek-V3.2-family models (#28110)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/lora/lora_manager.py`, `python/sglang/srt/lora/utils.py`, `python/sglang/srt/utils/common.py`_
- **2026-06-13** [`27ba13358e`](https://github.com/sgl-project/sglang/commit/27ba13358e) [#28133](https://github.com/sgl-project/sglang/pull/28133)
  [Spec] Clear dead DRAFT_EXTEND objects left after EAGLE v1 removal (#28133)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_backend_mtp_precompute.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/observability/req_time_stats.py`, `python/sglang/srt/speculative/frozen_kv_mtp_info.py` _+1 more__
- **2026-06-13** [`bde6bccf39`](https://github.com/sgl-project/sglang/commit/bde6bccf39) [#28129](https://github.com/sgl-project/sglang/pull/28129)
  [Spec] Remove deprecated EAGLE v1 DRAFT_EXTEND forward mode (#28129)
  _Files: `python/sglang/srt/hardware_backend/musa/attention/flashattention_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`, `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py` _+52 more__
- **2026-06-13** [`f7041c9dee`](https://github.com/sgl-project/sglang/commit/f7041c9dee) [#27739](https://github.com/sgl-project/sglang/pull/27739)
  step3.5 flash revise for graph mode and use triton activation (#27739)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`, `python/sglang/srt/layers/quantization/unquant.py`_
- **2026-06-13** [`bcd45d3ac7`](https://github.com/sgl-project/sglang/commit/bcd45d3ac7) [#28112](https://github.com/sgl-project/sglang/pull/28112)
  [AMD][DFlash] Add DFlash test to AMD CI (#28112)
  _Files: `test/registered/spec/dflash/test_dflash.py`_
- **2026-06-13** [`053e153183`](https://github.com/sgl-project/sglang/commit/053e153183) [#27817](https://github.com/sgl-project/sglang/pull/27817)
  [AMD] ci: register 8 attention-backend unit tests to run on AMD CI (#27817)
  _Files: `test/registered/attention/unittests/dense/test_torch_native.py`, `test/registered/attention/unittests/dense/test_triton.py`, `test/registered/attention/unittests/gdn/test_torch_native.py`, `test/registered/attention/unittests/gdn/test_triton.py` _+4 more__
- **2026-06-13** [`a0c6e0b3a4`](https://github.com/sgl-project/sglang/commit/a0c6e0b3a4) [#28116](https://github.com/sgl-project/sglang/pull/28116)
  chore: bump tokenspeed_mla 0.1.1 -> 0.1.6 (#28116)
  _Files: `python/pyproject.toml`_
- **2026-06-13** [`1a19f66acb`](https://github.com/sgl-project/sglang/commit/1a19f66acb) [#28102](https://github.com/sgl-project/sglang/pull/28102)
  Fix DP attention + EP mode of Nemotron (#28102)
  _Files: `python/sglang/srt/models/nemotron_h.py`, `python/sglang/srt/models/nemotron_h_utils.py`_
- **2026-06-13** [`6c3e429ba1`](https://github.com/sgl-project/sglang/commit/6c3e429ba1) [#28107](https://github.com/sgl-project/sglang/pull/28107)
  [Tiny] Cuda Graph Refactor Code Style Follow up (#28107)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/kv_canary/api.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/cuda_graph_config.py` _+17 more__
- **2026-06-12** [`fda7955890`](https://github.com/sgl-project/sglang/commit/fda7955890) [#27854](https://github.com/sgl-project/sglang/pull/27854)
  [AMD][DFlash] Enable Fused KV Materialization (#27854)
  _Files: `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-06-12** [`3a1417a0c1`](https://github.com/sgl-project/sglang/commit/3a1417a0c1) [#28081](https://github.com/sgl-project/sglang/pull/28081)
  [refactor] Fold FrozenKVMTPCudaGraphRunner onto the shared DecodeCudaGraphRunner base (#28081)
  _Files: `python/sglang/srt/speculative/frozen_kv_mtp_cuda_graph_runner.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_draft_runner.py`_
- **2026-06-12** [`87554c7855`](https://github.com/sgl-project/sglang/commit/87554c7855) [#28093](https://github.com/sgl-project/sglang/pull/28093)
  [Spec] Move draft-extend prep to `EagleDraftWorkerBase`; unify `prepare_for_*` names (#28093)
  _Files: `python/sglang/srt/kv_canary/plan_input.py`, `python/sglang/srt/speculative/base_spec_worker.py`, `python/sglang/srt/speculative/dflash_info.py`, `python/sglang/srt/speculative/dflash_worker_v2.py` _+8 more__
- **2026-06-12** [`6e0fa5afe1`](https://github.com/sgl-project/sglang/commit/6e0fa5afe1) [#24955](https://github.com/sgl-project/sglang/pull/24955)
  Support Nemotron DP attention and MTP (#24955)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/hybrid_attn_backend.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py` _+9 more__
- **2026-06-12** [`bb33594c1a`](https://github.com/sgl-project/sglang/commit/bb33594c1a) [#27737](https://github.com/sgl-project/sglang/pull/27737)
  flashinfer swa kv pool fix (dflash gemma 4) (#27737)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/test/kits/attention_unittest/attention_methods/gdn_attention.py`, `test/registered/unit/spec/test_resolve_swa_kv_pool.py`_
- **2026-06-12** [`75998d0421`](https://github.com/sgl-project/sglang/commit/75998d0421) [#23862](https://github.com/sgl-project/sglang/pull/23862)
  Fix --mem-fraction-static not accounting for EAGLE draft model KV cache       (#23862)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tp_worker.py` _+18 more__
- **2026-06-12** [`f308abc052`](https://github.com/sgl-project/sglang/commit/f308abc052) [#28016](https://github.com/sgl-project/sglang/pull/28016)
  Revise the mimo-v2-flash best practice (#28016)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`_
- **2026-06-12** [`371b96e210`](https://github.com/sgl-project/sglang/commit/371b96e210) [#27972](https://github.com/sgl-project/sglang/pull/27972)
  [AMD] Fix DeepSeek-V4-Flash-FP8 on MI300 (#27972)
  _Files: `python/sglang/srt/layers/attention/dsv4/unified_kv_kernels/paged_prefill.py`, `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-06-12** [`1cd5cb1220`](https://github.com/sgl-project/sglang/commit/1cd5cb1220) [#27149](https://github.com/sgl-project/sglang/pull/27149)
  [AMD] [CI] Add dsv4 accuracy PR gate to pr-test-amd-rocm720 (#27149)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `test/registered/amd/test_deepseek_v4_flash_fp4.py`, `test/registered/amd/test_deepseek_v4_flash_fp8.py`, `test/registered/amd/test_deepseek_v4_pro_fp4.py` _+1 more__
- **2026-06-12** [`36d61613a1`](https://github.com/sgl-project/sglang/commit/36d61613a1) [#27978](https://github.com/sgl-project/sglang/pull/27978)
  [AMD] Cache unified_kv swa_loc once per step instead of per layer (#27978)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-06-12** [`8038806557`](https://github.com/sgl-project/sglang/commit/8038806557) [#27826](https://github.com/sgl-project/sglang/pull/27826)
  [diffusion] optimize: optimize flux1 tensor parallel sharding (#27826)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux.py`, `python/sglang/multimodal_gen/runtime/utils/model_overlay.py`, `python/sglang/multimodal_gen/test/test_utils.py` _+1 more__
- **2026-06-12** [`3a3a759464`](https://github.com/sgl-project/sglang/commit/3a3a759464) [#26147](https://github.com/sgl-project/sglang/pull/26147)
  [NPU] Add Gemma4 Sliding Window Attention support on Ascend backend (#26147)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_torch_native_backend.py`, `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py` _+10 more__
- **2026-06-12** [`3ffe72517f`](https://github.com/sgl-project/sglang/commit/3ffe72517f) [#27977](https://github.com/sgl-project/sglang/pull/27977)
  [Spec] Remove the dead spec V1 scheduler paths (#27977)
  _Files: `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/layers/utils/logprob.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/schedule_batch.py` _+11 more__
- **2026-06-12** [`2e74ff192c`](https://github.com/sgl-project/sglang/commit/2e74ff192c) [#27973](https://github.com/sgl-project/sglang/pull/27973)
  [DSV4] Use int64 for compressor out_loc tensors (#27973)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`, `python/sglang/srt/layers/attention/dsv4/metadata_kernel.py`, `test/registered/jit/deepseek_v4/test_fp4_indexer.py`_
- **2026-06-11** [`c0480a88be`](https://github.com/sgl-project/sglang/commit/c0480a88be) [#27964](https://github.com/sgl-project/sglang/pull/27964)
  [Spec] Retire Spec V1 (#27964)
  _Files: `.claude/skills/env-var-conventions/SKILL.md`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx` _+42 more__
- **2026-06-11** [`cd075d1f64`](https://github.com/sgl-project/sglang/commit/cd075d1f64) [#27307](https://github.com/sgl-project/sglang/pull/27307)
  [RL] convert DeepSeek V4 APE layout through weight loader (#27307)
  _Files: `python/sglang/srt/layers/attention/dsv4/compressor.py`_
- **2026-06-11** [`fee717f303`](https://github.com/sgl-project/sglang/commit/fee717f303) [#27950](https://github.com/sgl-project/sglang/pull/27950)
  [Spec] Fold the DFLASH worker base into DFlashWorkerV2 on BaseSpecWorker (#27950)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/dflash_worker.py`, `python/sglang/srt/speculative/dflash_worker_v2.py`_
- **2026-06-11** [`acdb39edd2`](https://github.com/sgl-project/sglang/commit/acdb39edd2) [#27959](https://github.com/sgl-project/sglang/pull/27959)
  [Spec] Remove the DFLASH V1 worker path (#27959)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/speculative/dflash_info.py`, `python/sglang/srt/speculative/dflash_worker.py`, `python/sglang/srt/speculative/dflash_worker_v2.py` _+2 more__
- **2026-06-11** [`6e885c844f`](https://github.com/sgl-project/sglang/commit/6e885c844f) [#27919](https://github.com/sgl-project/sglang/pull/27919)
  Revert "[AMD] Fix DeepSeek V4 Pro c128 state tensor dtype mismatch error and c4_sparse_raw_indices attribute error in cuda graph phase" (#27919)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/c128_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4_v2.cuh`, `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`_
- **2026-06-11** [`1a6b5561db`](https://github.com/sgl-project/sglang/commit/1a6b5561db) [#26203](https://github.com/sgl-project/sglang/pull/26203)
  Fix MLA scaling when YARN scaling is disabled (#26203)
  _Files: `python/sglang/srt/configs/model_config.py`, `test/registered/unit/configs/test_model_config_scaling.py`_
- **2026-06-11** [`d571e076fa`](https://github.com/sgl-project/sglang/commit/d571e076fa) [#27429](https://github.com/sgl-project/sglang/pull/27429)
  [codex] Centralize more inline Triton kernels (#27429)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba_state_scatter_triton.py`, `python/sglang/srt/layers/attention/triton_ops/kv_indices.py`, `python/sglang/srt/layers/attention/triton_ops/pad.py` _+4 more__
- **2026-06-11** [`22c7285a26`](https://github.com/sgl-project/sglang/commit/22c7285a26) [#27630](https://github.com/sgl-project/sglang/pull/27630)
  [AMD] Fuse sigmoid + mul attention output gate into single Triton kernel (#27630)
  _Files: `python/sglang/jit_kernel/tests/test_sigmoid_gate_mul.py`, `python/sglang/jit_kernel/triton/sigmoid_gate_mul.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`_
- **2026-06-11** [`f4b3b99413`](https://github.com/sgl-project/sglang/commit/f4b3b99413) [#27583](https://github.com/sgl-project/sglang/pull/27583)
  [AMD] Enable fused GDN QKV split Triton kernel on HIP (#27583)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`_
- **2026-06-11** [`9425ba2478`](https://github.com/sgl-project/sglang/commit/9425ba2478) [#27856](https://github.com/sgl-project/sglang/pull/27856)
  Remove extra_pytest_path from pr-test.yml (#27856)
  _Files: `.github/workflows/pr-test.yml`, `test/registered/jit/test_flash_attention_4.py`_
- **2026-06-11** [`f4f30d7d23`](https://github.com/sgl-project/sglang/commit/f4f30d7d23) [#27840](https://github.com/sgl-project/sglang/pull/27840)
  [Fix] Use int64 seq_lens across all CUDA graph runners and backends (#27840)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py` _+8 more__
- **2026-06-11** [`588d1f7bc9`](https://github.com/sgl-project/sglang/commit/588d1f7bc9) [#23000](https://github.com/sgl-project/sglang/pull/23000)
  [Feature] Spec V2 DFlash Support (#23000)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py` _+17 more__
- **2026-06-11** [`475e9d25bf`](https://github.com/sgl-project/sglang/commit/475e9d25bf) [#27808](https://github.com/sgl-project/sglang/pull/27808)
  bugfix for npu mtp graph runner (#27808)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/multi_layer_eagle_draft_extend_npu_graph_runner.py` _+4 more__
- **2026-06-10** [`8c6bbe0658`](https://github.com/sgl-project/sglang/commit/8c6bbe0658) [#27510](https://github.com/sgl-project/sglang/pull/27510)
  [deepseek] Enable DP attention + TBO + shared experts fusion (#27510)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/server_args.py`, `test/registered/ep/test_tbo_shared_experts_fusion.py`_
- **2026-06-10** [`502bc89e1b`](https://github.com/sgl-project/sglang/commit/502bc89e1b) [#27529](https://github.com/sgl-project/sglang/pull/27529)
  [AMD] Fix DeepSeek V4 Pro c128 state tensor dtype mismatch error and c4_sparse_raw_indices attribute error in cuda graph phase (#27529)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/c128_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4_v2.cuh`, `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/layers/attention/dsv4/compressor.py`_
- **2026-06-10** [`53ed34cb88`](https://github.com/sgl-project/sglang/commit/53ed34cb88) [#27668](https://github.com/sgl-project/sglang/pull/27668)
  Fix MiMo-V2.5-Pro DP-attention dp size in cookbook deployment snippet (#27668)
  _Files: `docs_new/src/snippets/autoregressive/mimo-v25-deployment.jsx`_
- **2026-06-10** [`518e35fae7`](https://github.com/sgl-project/sglang/commit/518e35fae7) [#27488](https://github.com/sgl-project/sglang/pull/27488)
  [KDA] Add CuteDSL Prefill Kernel on SM100 (#27488)
  _Files: `benchmark/bench_linear_attention/bench_kda_prefill_cutedsl.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_blackwell/__init__.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_blackwell/kernel_h.py` _+5 more__
- **2026-06-10** [`111009ea54`](https://github.com/sgl-project/sglang/commit/111009ea54) [#17260](https://github.com/sgl-project/sglang/pull/17260)
  [Feature] [Ngram spec] Support ngram spec v2 (#17260)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py` _+9 more__
- **2026-06-10** [`f2bcdb0508`](https://github.com/sgl-project/sglang/commit/f2bcdb0508) [#27380](https://github.com/sgl-project/sglang/pull/27380)
  [AMD] Add unified kv attention support in dpsk-v4 (#27380)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/jit_kernel/dsv4/compress.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py` _+12 more__
- **2026-06-10** [`95d8a75bc9`](https://github.com/sgl-project/sglang/commit/95d8a75bc9) [#27695](https://github.com/sgl-project/sglang/pull/27695)
  Bundle set_kv_buffer write targets into KVWriteLoc (loc + swa_loc) (#27695)
  _Files: `python/sglang/srt/hardware_backend/musa/attention/flashattention_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`, `python/sglang/srt/layers/attention/aiter_backend.py` _+11 more__
- **2026-06-10** [`758fd4bb9a`](https://github.com/sgl-project/sglang/commit/758fd4bb9a) [#27617](https://github.com/sgl-project/sglang/pull/27617)
  [SWA] Cache full→SWA out_cache_loc per forward across attention backends (#27617)
  _Files: `python/sglang/srt/hardware_backend/musa/attention/flashattention_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py` _+10 more__
- **2026-06-10** [`08ceb96ea5`](https://github.com/sgl-project/sglang/commit/08ceb96ea5) [#27065](https://github.com/sgl-project/sglang/pull/27065)
  [diffusion] fix: remove boolean arithmetic guard to fix compiling (#27065)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`_
- **2026-06-10** [`d21c31f681`](https://github.com/sgl-project/sglang/commit/d21c31f681) [#25883](https://github.com/sgl-project/sglang/pull/25883)
  fix: forward update_mamba_state_after_mtp_verify in HybridAttnBackend (#25883)
  _Files: `python/sglang/srt/layers/attention/hybrid_attn_backend.py`_
- **2026-06-09** [`bc82086ef8`](https://github.com/sgl-project/sglang/commit/bc82086ef8) [#27453](https://github.com/sgl-project/sglang/pull/27453)
  Remove FlashInfer GB transport workaround (#27453)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py`_
- **2026-06-09** [`4455abd164`](https://github.com/sgl-project/sglang/commit/4455abd164) [#27468](https://github.com/sgl-project/sglang/pull/27468)
  dflash piecewise cuda graphs support (#27468)
  _Files: `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`, `test/registered/piecewise_cuda_graph/test_pcg_with_speculative_decoding_dflash.py`_
- **2026-06-09** [`decb88e0e3`](https://github.com/sgl-project/sglang/commit/decb88e0e3) [#27607](https://github.com/sgl-project/sglang/pull/27607)
  Support spec v2 for Frozen-KV MTP; remove v1 worker (#27607)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/frozen_kv_mtp_cuda_graph_runner.py`, `python/sglang/srt/speculative/frozen_kv_mtp_info.py` _+9 more__
- **2026-06-09** [`2fef951fe8`](https://github.com/sgl-project/sglang/commit/2fef951fe8) [#23927](https://github.com/sgl-project/sglang/pull/23927)
  [AMD] Replace fp8 mla with fp8 mha kernel for diffusion model aiter backend (#23927)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/aiter.py`_
- **2026-06-09** [`8ae328e5f0`](https://github.com/sgl-project/sglang/commit/8ae328e5f0) [#27647](https://github.com/sgl-project/sglang/pull/27647)
  [sgl] Fix kimi-k2.5 EAGLE3 MLA draft embeds for batched MM prefill (#27647)
  _Files: `python/sglang/srt/models/kimi_k25_eagle3.py`_
- **2026-06-09** [`1368717248`](https://github.com/sgl-project/sglang/commit/1368717248) [#27506](https://github.com/sgl-project/sglang/pull/27506)
  Add more testing for chunked prefill (#27506)
  _Files: `python/sglang/test/chunked_prefill_test_utils.py`, `python/sglang/test/scripted_runtime/context/api.py`, `python/sglang/test/scripted_runtime/context/http_post.py`, `python/sglang/test/scripted_runtime/context/lifecycle.py` _+38 more__
- **2026-06-09** [`cd6efcb947`](https://github.com/sgl-project/sglang/commit/cd6efcb947) [#27202](https://github.com/sgl-project/sglang/pull/27202)
  [NPU][Bugfix] fix MTP accuracy regression on Qwen3 hybrid models (#27202)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-06-09** [`db143e5212`](https://github.com/sgl-project/sglang/commit/db143e5212) [#26460](https://github.com/sgl-project/sglang/pull/26460)
  [Intel GPU][Encoder] Add xpu_attn backend for encoder vision attention (#26460)
  _Files: `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/server_args.py`, `test/registered/xpu/test_encoder_attention_backend.py`_
- **2026-06-09** [`ea66b2cca7`](https://github.com/sgl-project/sglang/commit/ea66b2cca7) [#24390](https://github.com/sgl-project/sglang/pull/24390)
  [XPU] Enable NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 on Intel XPU backend (#24390)
  _Files: `.gitignore`, `python/sglang/srt/layers/attention/mamba/mamba.py`, `python/sglang/srt/layers/quantization/unquant.py`_
- **2026-06-09** [`009a0ceefa`](https://github.com/sgl-project/sglang/commit/009a0ceefa) [#27526](https://github.com/sgl-project/sglang/pull/27526)
  [XPU CI] Re-enable stage B with docker-pull flow and split tests (#27526)
  _Files: `.github/workflows/pr-test-xpu.yml`, `test/registered/attention/test_chunk_gated_delta_rule.py`, `test/registered/xpu/test_deepseek_ocr.py`, `test/registered/xpu/test_deepseek_ocr_triton.py` _+3 more__
- **2026-06-09** [`6abef38627`](https://github.com/sgl-project/sglang/commit/6abef38627) [#21197](https://github.com/sgl-project/sglang/pull/21197)
  [NPU]adaptation to support deterministic inference (#21197)
  _Files: `python/sglang/srt/batch_invariant_ops/batch_invariant_ops.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/batch_invariant_ops/npu_batch_invariant_ops.py`, `python/sglang/srt/layers/sampler.py` _+2 more__
- **2026-06-09** [`a09e85d677`](https://github.com/sgl-project/sglang/commit/a09e85d677) [#25077](https://github.com/sgl-project/sglang/pull/25077)
  Fix(spec): Fix the crash issue in the FA3 backend when running with top-k > 1 and page_size > 1 (#25077)
  _Files: `test/manual/attention/test_flashattn_backend.py`_
- **2026-06-08** [`28c1a3cb45`](https://github.com/sgl-project/sglang/commit/28c1a3cb45) [#25464](https://github.com/sgl-project/sglang/pull/25464)
  [Spec] Deprecate Spec V1 (#25464)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/debug_utils/pr_fix_toggle.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py` _+17 more__
- **2026-06-08** [`ea1d190ed0`](https://github.com/sgl-project/sglang/commit/ea1d190ed0) [#27289](https://github.com/sgl-project/sglang/pull/27289)
  [ROCm] dsv4: remove the redundant fp8 scale transpose-copy on decode (#27289)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py` _+3 more__
- **2026-06-08** [`fca4ef9d69`](https://github.com/sgl-project/sglang/commit/fca4ef9d69) [#27491](https://github.com/sgl-project/sglang/pull/27491)
  Fix SWA pool resolution for EAGLE draft workers (#27491)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dense_attention.py`, `test/registered/unit/spec/test_resolve_swa_kv_pool.py`_
- **2026-06-08** [`bcb5645629`](https://github.com/sgl-project/sglang/commit/bcb5645629) [#27495](https://github.com/sgl-project/sglang/pull/27495)
  Fix TRTLLM target verify query metadata (#27495)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-06-08** [`b047bb3e92`](https://github.com/sgl-project/sglang/commit/b047bb3e92) [#27387](https://github.com/sgl-project/sglang/pull/27387)
  build(sgl-kernel): support configurable mirrors for restricted networks (#27387)
  _Files: `sgl-kernel/CMakeLists.txt`, `sgl-kernel/Dockerfile`, `sgl-kernel/Makefile`, `sgl-kernel/build.sh` _+1 more__
- **2026-06-08** [`57ea09badb`](https://github.com/sgl-project/sglang/commit/57ea09badb) [#27545](https://github.com/sgl-project/sglang/pull/27545)
  Fix NaN in triton EAGLE spec-v2 draft-extend CUDA graph at topk>1 (wrong qo_indptr stride) (#27545)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`_
- **2026-06-08** [`0d0254c9de`](https://github.com/sgl-project/sglang/commit/0d0254c9de) [#20260](https://github.com/sgl-project/sglang/pull/20260)
  Fix port overflow in DP attention path when base port is near 65535 (#20260)
  _Files: `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/network.py`_
- **2026-06-08** [`3d2165a286`](https://github.com/sgl-project/sglang/commit/3d2165a286) [#27361](https://github.com/sgl-project/sglang/pull/27361)
  Fix dual-chunk sparse fallback index overflow (#27361)
  _Files: `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dual_chunk_attention.py`, `test/registered/attention/unittests/KNOWN_FAILURES.md`, `test/registered/attention/unittests/dual_chunk/README.md` _+1 more__
- **2026-06-08** [`bf7fb6b925`](https://github.com/sgl-project/sglang/commit/bf7fb6b925) [#27477](https://github.com/sgl-project/sglang/pull/27477)
  fix dflash rope config parsing for updated transformers (#27477)
  _Files: `python/sglang/srt/models/dflash.py`_
- **2026-06-08** [`1c73ff8ad3`](https://github.com/sgl-project/sglang/commit/1c73ff8ad3) [#27063](https://github.com/sgl-project/sglang/pull/27063)
  [AMD] Optimize gpt-oss-120B performance (#27063)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/aiter_utils.py`, `python/sglang/srt/layers/attention/utils.py` _+7 more__
- **2026-06-08** [`303757ccd8`](https://github.com/sgl-project/sglang/commit/303757ccd8) [#27485](https://github.com/sgl-project/sglang/pull/27485)
  [Attn] Fix aiter MLA verify `kv_indices` under-alloc + shared `assert_buffer_fits` guard (#27485)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py` _+1 more__
- **2026-06-08** [`f68c79675f`](https://github.com/sgl-project/sglang/commit/f68c79675f) [#27463](https://github.com/sgl-project/sglang/pull/27463)
  Support `topk > 1` tree drafting for mamba/hybrid-linear models on spec v2 (#27463)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/attention/linear/lightning_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` _+4 more__

## Multimodal  (40 commits)

- **2026-06-15** [`818808d152`](https://github.com/sgl-project/sglang/commit/818808d152) [#28204](https://github.com/sgl-project/sglang/pull/28204)
  [diffusion] optimize: optimize causal conv3d vae padding (#28204)
  _Files: `python/sglang/jit_kernel/diffusion/triton/causal_conv3d_pad.py`, `python/sglang/multimodal_gen/runtime/layers/parallel_conv.py`, `python/sglang/multimodal_gen/runtime/models/vaes/autoencoder_kl_qwenimage.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py`_
- **2026-06-15** [`2a33724c9b`](https://github.com/sgl-project/sglang/commit/2a33724c9b) [#28056](https://github.com/sgl-project/sglang/pull/28056)
  [perf] Reuse a pooled HTTP session for multimodal URL downloads (#28056)
  _Files: `python/sglang/srt/multimodal/processors/mimo_audio.py`, `python/sglang/srt/utils/common.py`_
- **2026-06-15** [`19c78552dc`](https://github.com/sgl-project/sglang/commit/19c78552dc) [#28263](https://github.com/sgl-project/sglang/pull/28263)
  [AMD] Restrict CI image fallback to versioned tags (#28263)
  _Files: `scripts/ci/amd/amd_ci_start_container.sh`, `scripts/ci/amd/amd_ci_start_container_disagg.sh`_
- **2026-06-15** [`578e936d8d`](https://github.com/sgl-project/sglang/commit/578e936d8d) [#28205](https://github.com/sgl-project/sglang/pull/28205)
  [diffusion] feat: persist torch.compile inductor/triton cache across restarts (#28205)
  _Files: `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`_
- **2026-06-15** [`07b9108348`](https://github.com/sgl-project/sglang/commit/07b9108348) [#28166](https://github.com/sgl-project/sglang/pull/28166)
  [Diffusion] FLUX: fuse FeedForward GELU into up-proj GEMM (cublasLt epilogue) (#28166)
  _Files: `python/sglang/multimodal_gen/runtime/layers/fused_linear_act/__init__.py`, `python/sglang/multimodal_gen/runtime/layers/fused_linear_act/gelu.py`, `python/sglang/multimodal_gen/runtime/models/dits/flux.py`_
- **2026-06-14** [`000fc975c7`](https://github.com/sgl-project/sglang/commit/000fc975c7) [#28206](https://github.com/sgl-project/sglang/pull/28206)
  ci(docker): support layered overlay images in release-docker-dev (#28206)
  _Files: `.github/workflows/release-docker-dev.yml`_
- **2026-06-14** [`3cb29f6747`](https://github.com/sgl-project/sglang/commit/3cb29f6747) [#28193](https://github.com/sgl-project/sglang/pull/28193)
  [diffusion] feat: use regional torch.compile (compile_repeated_blocks) for DiT of diffusers backend (#28193)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines/diffusers_pipeline.py`_
- **2026-06-14** [`ec36dde580`](https://github.com/sgl-project/sglang/commit/ec36dde580) [#28184](https://github.com/sgl-project/sglang/pull/28184)
  [diffusion] feat: add --warmup-mode enum server arg (#28184)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/cli/serve.py`, `python/sglang/multimodal_gen/runtime/server_args.py`, `python/sglang/multimodal_gen/runtime/server_warmup.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-06-14** [`582bd23f71`](https://github.com/sgl-project/sglang/commit/582bd23f71) [#28071](https://github.com/sgl-project/sglang/pull/28071)
  [diffusion] feat: enable spatial-shard vae decode across GPUs (#28071)
  _Files: `python/sglang/multimodal_gen/configs/models/vaes/base.py`, `python/sglang/multimodal_gen/configs/models/vaes/hunyuan3d.py`, `python/sglang/multimodal_gen/configs/models/vaes/hunyuanvae.py`, `python/sglang/multimodal_gen/configs/models/vaes/ltx_audio.py` _+21 more__
- **2026-06-14** [`5331de0f8c`](https://github.com/sgl-project/sglang/commit/5331de0f8c) [#28177](https://github.com/sgl-project/sglang/pull/28177)
  [diffusion] chore: resolve model_index.json Hub-first with local-cache fallback (#28177)
  _Files: `python/sglang/multimodal_gen/runtime/utils/hf_diffusers_utils.py`_
- **2026-06-14** [`1456eb612d`](https://github.com/sgl-project/sglang/commit/1456eb612d) [#28123](https://github.com/sgl-project/sglang/pull/28123)
  [diffusion] CI: tighten perf baselines (#28123)
  _Files: `python/sglang/multimodal_gen/test/server/perf_baselines.json`_
- **2026-06-14** [`31ac743484`](https://github.com/sgl-project/sglang/commit/31ac743484) [#28127](https://github.com/sgl-project/sglang/pull/28127)
  [diffusion] chore: improve server warmup coverage (#28127)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/diffusion_generator.py`, `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/utils.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py` _+7 more__
- **2026-06-13** [`cb4933b22e`](https://github.com/sgl-project/sglang/commit/cb4933b22e) [#27875](https://github.com/sgl-project/sglang/pull/27875)
  [diffusion] optimize: enable vae parallel decode with cfg-parallel (#27875)
  _Files: `python/sglang/multimodal_gen/runtime/distributed/__init__.py`, `python/sglang/multimodal_gen/runtime/distributed/parallel_state.py`, `python/sglang/multimodal_gen/runtime/models/vaes/parallel/wan_dist_utils.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py` _+3 more__
- **2026-06-13** [`8becb37519`](https://github.com/sgl-project/sglang/commit/8becb37519) [#28119](https://github.com/sgl-project/sglang/pull/28119)
  [diffusion] warmup: improve diffusion server warmup (#28119)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/schedule_batch.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/base.py` _+11 more__
- **2026-06-13** [`5f315c74da`](https://github.com/sgl-project/sglang/commit/5f315c74da) [#28108](https://github.com/sgl-project/sglang/pull/28108)
  [CI] Enforce modern `stage=`/`runner_config=` form for dispatchable test suites (#28108)
  _Files: `.pre-commit-config.yaml`, `scripts/ci/check_registered_tests.py`, `test/registered/tokenizer/test_multi_detokenizer.py`, `test/registered/unit/spec/test_eagle_worker_v2_topk1_fastpath.py` _+1 more__
- **2026-06-12** [`ca17bd8347`](https://github.com/sgl-project/sglang/commit/ca17bd8347) [#26082](https://github.com/sgl-project/sglang/pull/26082)
  perf: eliminate CUDA syncs in VLM embed path (#26082)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `test/registered/vlm/test_vision_openai_server_a.py`_
- **2026-06-12** [`ddbe5ff2f1`](https://github.com/sgl-project/sglang/commit/ddbe5ff2f1) [#27999](https://github.com/sgl-project/sglang/pull/27999)
  [AMD] Pin maturin<1.14 to fix ROCm image build failure (#27999)
  _Files: `docker/rocm.Dockerfile`_
- **2026-06-11** [`ec0eb6cce8`](https://github.com/sgl-project/sglang/commit/ec0eb6cce8) [#26278](https://github.com/sgl-project/sglang/pull/26278)
  Support MiMo v2 ASR (#26278)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/__init__.py`, `python/sglang/srt/entrypoints/openai/transcription_adapters/mimo_v2_asr.py`, `python/sglang/srt/models/mimo_audio.py` _+5 more__
- **2026-06-11** [`24c5d76f74`](https://github.com/sgl-project/sglang/commit/24c5d76f74) [#27846](https://github.com/sgl-project/sglang/pull/27846)
  fix: per-sequence last-token embedding in EAGLE3/MTP draft for batched multimodal spec decoding (#27846)
  _Files: `python/sglang/srt/models/llama_eagle3.py`, `python/sglang/srt/models/qwen3_5_mtp.py`_
- **2026-06-11** [`7f57b344c9`](https://github.com/sgl-project/sglang/commit/7f57b344c9) [#27736](https://github.com/sgl-project/sglang/pull/27736)
  [diffusion] feat: progressive resolution growing for Ideogram 4 via GPU DCT upsampling with up to 1.56× speedup (#27736)
  _Files: `docs_new/docs/sglang-diffusion/progressive_resolution.mdx`, `python/sglang/multimodal_gen/runtime/pipelines/ideogram.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/progressive_resolution/denoising.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/progressive_resolution/flux.py` _+3 more__
- **2026-06-11** [`d9110d971e`](https://github.com/sgl-project/sglang/commit/d9110d971e) [#27876](https://github.com/sgl-project/sglang/pull/27876)
  [diffusion] fix: fix wan ti2v sp timestep padding (#27876)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/wan_ti2v.py`, `python/sglang/multimodal_gen/test/unit/test_wan_ti2v_helpers.py`_
- **2026-06-11** [`9e9fde1478`](https://github.com/sgl-project/sglang/commit/9e9fde1478) [#27892](https://github.com/sgl-project/sglang/pull/27892)
  [diffusion] Revert "Mistral3 add tensor parallel support for diffusion text encoder " (#27892)
  _Files: `python/sglang/multimodal_gen/configs/models/encoders/flux_2.py`, `python/sglang/multimodal_gen/configs/models/encoders/mistral3.py`, `python/sglang/multimodal_gen/runtime/layers/custom_op.py`, `python/sglang/multimodal_gen/runtime/models/encoders/mistral_3.py` _+1 more__
- **2026-06-10** [`1cf8efdd08`](https://github.com/sgl-project/sglang/commit/1cf8efdd08) [#27824](https://github.com/sgl-project/sglang/pull/27824)
  docs: Diffusion Gemma cookbook (#27824)
  _Files: `docs_new/cookbook/autoregressive/Google/DiffusionGemma.mdx`, `docs_new/docs.json`, `docs_new/docs/supported-models/diffusion_language_models.mdx`_
- **2026-06-10** [`56f06278c6`](https://github.com/sgl-project/sglang/commit/56f06278c6) [#27698](https://github.com/sgl-project/sglang/pull/27698)
  [diffusion] refactor: refactor realtime control state and adapters (#27698)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/adapters/lingbot_world_realtime_adapter.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/adapters/sana_wm_realtime_adapter.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/generate_session.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/realtime_adapter.py` _+22 more__
- **2026-06-10** [`5809bbe35d`](https://github.com/sgl-project/sglang/commit/5809bbe35d) [#25950](https://github.com/sgl-project/sglang/pull/25950)
  Mistral3 add tensor parallel support for diffusion text encoder  (#25950)
  _Files: `python/sglang/multimodal_gen/configs/models/encoders/flux_2.py`, `python/sglang/multimodal_gen/configs/models/encoders/mistral3.py`, `python/sglang/multimodal_gen/runtime/layers/custom_op.py`, `python/sglang/multimodal_gen/runtime/models/encoders/mistral_3.py`_
- **2026-06-10** [`af55025644`](https://github.com/sgl-project/sglang/commit/af55025644) [#27697](https://github.com/sgl-project/sglang/pull/27697)
  [diffusion] refactor: refactor realtime and model-specific stage modules (#27697)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines/hunyuan3d_pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines/lingbot_world_causal_dmd_pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines/ltx_2_pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines/sana_wm_realtime_pipeline.py` _+22 more__
- **2026-06-09** [`98fe7e326e`](https://github.com/sgl-project/sglang/commit/98fe7e326e) [#26320](https://github.com/sgl-project/sglang/pull/26320)
  fix(gemma4): register image/video/audio token_regex for HF-expanded prompts  (#26320)
  _Files: `python/sglang/srt/multimodal/processors/gemma4.py`_
- **2026-06-09** [`5babb902a9`](https://github.com/sgl-project/sglang/commit/5babb902a9) [#27581](https://github.com/sgl-project/sglang/pull/27581)
  [AMD] fix: handle per-frame 4D shift in native scale-shift kernel (#27581)
  _Files: `python/sglang/jit_kernel/diffusion/triton/scale_shift.py`_
- **2026-06-09** [`aa18a68ac5`](https://github.com/sgl-project/sglang/commit/aa18a68ac5) [#27431](https://github.com/sgl-project/sglang/pull/27431)
  [diffusion] Run LTX-2 VAE decode in channels_last_3d (faster decode, lower peak memory) (#27431)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/runtime/models/vaes/ltx_2_vae.py`, `python/sglang/multimodal_gen/test/unit/test_ltx2_vae_channels_last.py`, `python/sglang/multimodal_gen/test/unit/test_vae_loader.py`_
- **2026-06-09** [`fdcd28a08d`](https://github.com/sgl-project/sglang/commit/fdcd28a08d) [#27283](https://github.com/sgl-project/sglang/pull/27283)
  [NPU] Enable consistency checking for diffusion tests (#27283)
  _Files: `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/utils.py`, `python/sglang/multimodal_gen/test/server/ascend/testcase_configs_npu.py`, `python/sglang/multimodal_gen/test/test_utils.py`_
- **2026-06-09** [`5c0b2859e8`](https://github.com/sgl-project/sglang/commit/5c0b2859e8) [#22817](https://github.com/sgl-project/sglang/pull/22817)
  [diffusion] rl: extract post-training weight apis into mixins and add tensor update/checker paths (#22817)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/post_training/io_struct.py`, `python/sglang/multimodal_gen/runtime/entrypoints/post_training/weights_api.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py` _+4 more__
- **2026-06-09** [`f6d53d6d16`](https://github.com/sgl-project/sglang/commit/f6d53d6d16) [#27626](https://github.com/sgl-project/sglang/pull/27626)
  docs: update SANA-WM cookbook serve examples (#27626)
  _Files: `docs_new/cookbook/diffusion/SANA-WM/SANA-WM.mdx`_
- **2026-06-09** [`bdf47315ce`](https://github.com/sgl-project/sglang/commit/bdf47315ce) [#27198](https://github.com/sgl-project/sglang/pull/27198)
  docs: add cookbook for SANA-WM (#27198)
  _Files: `docs_new/cards/logos/sana.png`, `docs_new/cookbook/diffusion/SANA-WM/SANA-WM.mdx`, `docs_new/cookbook/diffusion/intro.mdx`, `docs_new/docs.json`_
- **2026-06-09** [`71e8258783`](https://github.com/sgl-project/sglang/commit/71e8258783) [#26635](https://github.com/sgl-project/sglang/pull/26635)
  Improve registration in cpu_graph_runner (#26635)
  _Files: `python/sglang/multimodal_gen/runtime/managers/cpu_worker.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-06-08** [`b0cd533a96`](https://github.com/sgl-project/sglang/commit/b0cd533a96) [#27524](https://github.com/sgl-project/sglang/pull/27524)
  [diffusion] feat: progressive resolution growing for image and video models (#27524)
  _Files: `docs_new/docs/sglang-diffusion/progressive_resolution.mdx`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/runtime/pipelines/flux.py`, `python/sglang/multimodal_gen/runtime/pipelines/flux_2.py` _+19 more__
- **2026-06-08** [`a26587dd4e`](https://github.com/sgl-project/sglang/commit/a26587dd4e) [#22786](https://github.com/sgl-project/sglang/pull/22786)
  [AMD][diffusion] Add FlyDSL fused normalization kernels for ROCm diffusion models optimization (#22786)
  _Files: `python/sglang/jit_kernel/diffusion/flydsl/fused_residual_norm.py`, `python/sglang/jit_kernel/tests/diffusion/test_flydsl_fused_norm.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`_
- **2026-06-08** [`6c2770149b`](https://github.com/sgl-project/sglang/commit/6c2770149b) [#27432](https://github.com/sgl-project/sglang/pull/27432)
  [diffusion] Fix native text-encoder loading for T5/UMT5 encoder-decoder models (#27432)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/test/unit/test_text_encoder_loader.py`_
- **2026-06-08** [`acf65c1c68`](https://github.com/sgl-project/sglang/commit/acf65c1c68) [#27282](https://github.com/sgl-project/sglang/pull/27282)
  [XPU CI] Pull prebuilt nightly image instead of building per-stage (#27282)
  _Files: `.github/workflows/pr-test-xpu.yml`, `scripts/ci/xpu/xpu_ci_start_container.sh`_
- **2026-06-08** [`12d47fa78b`](https://github.com/sgl-project/sglang/commit/12d47fa78b) [#27299](https://github.com/sgl-project/sglang/pull/27299)
  ci(xpu): push latest tag and use 7-char SHA in nightly image tags (#27299)
  _Files: `.github/workflows/release-docker-intel-xpu-nightly.yml`_
- **2026-06-08** [`70db73afce`](https://github.com/sgl-project/sglang/commit/70db73afce) [#27512](https://github.com/sgl-project/sglang/pull/27512)
  [Spec] Clamp multimodal pad sentinels in spec-v2 draft prefill embedding (#27512)
  _Files: `python/sglang/srt/models/mimo_v2_nextn.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_

## KV Cache / Memory  (32 commits)

- **2026-06-15** [`e985422b2b`](https://github.com/sgl-project/sglang/commit/e985422b2b) [#27863](https://github.com/sgl-project/sglang/pull/27863)
  [Fix][MTP][MM] Fix EAGLE v2 chunked-prefill next-token chain crash on multimodal models due to placeholder tokens (#27863)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-06-14** [`f293ddf3ce`](https://github.com/sgl-project/sglang/commit/f293ddf3ce) [#27965](https://github.com/sgl-project/sglang/pull/27965)
  [perf] reduce overhead of fill_ids list reconstruction and decref (#27965)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/mamba_radix_cache.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/radix_cache_cpp.py` _+4 more__
- **2026-06-14** [`5fb4e2d02e`](https://github.com/sgl-project/sglang/commit/5fb4e2d02e) [#27931](https://github.com/sgl-project/sglang/pull/27931)
  [UnifiedTree] Use Qwen3-32B in unified radix pp kl tests and set KL threshold to 0.005 (#27931)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_hicache_pp_kl.py`_
- **2026-06-13** [`568aa5fcdb`](https://github.com/sgl-project/sglang/commit/568aa5fcdb) [#27953](https://github.com/sgl-project/sglang/pull/27953)
  Fix missing draft KV pool transfers in HybridCacheController (#27953)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`_
- **2026-06-13** [`8ce05e8a20`](https://github.com/sgl-project/sglang/commit/8ce05e8a20) [#27444](https://github.com/sgl-project/sglang/pull/27444)
  [UnifiedTree]: Pin host buffers across async H→D in UnifiedRadixCache.load_back (#27444)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/mamba_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-06-13** [`d8f8e89ffb`](https://github.com/sgl-project/sglang/commit/d8f8e89ffb) [#27913](https://github.com/sgl-project/sglang/pull/27913)
  [Test] Add unit tests for srt/mem_cache/utils.py (#27913)
  _Files: `test/registered/unit/mem_cache/test_mem_cache_utils.py`_
- **2026-06-13** [`e02f7ca482`](https://github.com/sgl-project/sglang/commit/e02f7ca482) [#28076](https://github.com/sgl-project/sglang/pull/28076)
  [perf] remove several h2d sync (#28076)
  _Files: `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/sampling/sampling_batch_info.py`_
- **2026-06-12** [`54989b1fd0`](https://github.com/sgl-project/sglang/commit/54989b1fd0) [#27822](https://github.com/sgl-project/sglang/pull/27822)
  [AMD] ci: add label-gated extra-a tier (kv_canary + mock_model unit tests) (#27822)
  _Files: `.github/workflows/pr-test-amd-extra.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/kv_canary/test_self_unit_buffer_alloc.py` _+21 more__
- **2026-06-12** [`627ed3476b`](https://github.com/sgl-project/sglang/commit/627ed3476b) [#28013](https://github.com/sgl-project/sglang/pull/28013)
  Fix invalid KVFP4QuantizeUtil references (#28013)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `test/manual/quant/test_kvfp4_quant_dequant.py`_
- **2026-06-12** [`fcae6767d5`](https://github.com/sgl-project/sglang/commit/fcae6767d5) [#27672](https://github.com/sgl-project/sglang/pull/27672)
  Add bucketed multi-dir layout for NIXL file storage (#27672)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/README.md`, `python/sglang/srt/mem_cache/storage/nixl/hicache_nixl.py`, `python/sglang/srt/mem_cache/storage/nixl/nixl_routing.py`, `python/sglang/srt/mem_cache/storage/nixl/nixl_utils.py` _+1 more__
- **2026-06-12** [`60e4f14953`](https://github.com/sgl-project/sglang/commit/60e4f14953) [#27752](https://github.com/sgl-project/sglang/pull/27752)
  [NPU][Bugfix] Fix accuracy issue in no-graph with MTP (#27752)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`, `python/sglang/srt/mem_cache/allocator/swa.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-06-12** [`3c1f9eafa5`](https://github.com/sgl-project/sglang/commit/3c1f9eafa5) [#27402](https://github.com/sgl-project/sglang/pull/27402)
  [sgl] proactively release out-of-window SWA slots after chunked prefill (#27402)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py` _+3 more__
- **2026-06-11** [`12d3f02be8`](https://github.com/sgl-project/sglang/commit/12d3f02be8) [#27850](https://github.com/sgl-project/sglang/pull/27850)
  [AMD] Fix DSA device-to-host direct test on rocm720 (page_size%16 assert) (#27850)
  _Files: `test/registered/unit/mem_cache/test_dsa_pool_host_unit.py`_
- **2026-06-11** [`66076f2409`](https://github.com/sgl-project/sglang/commit/66076f2409) [#26678](https://github.com/sgl-project/sglang/pull/26678)
  [mem_cache][3/N] refactor: move HiSparse allocators to allocator/hisparse.py (#26678)
  _Files: `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/allocator/hisparse.py`, `python/sglang/srt/mem_cache/chunk_cache.py` _+3 more__
- **2026-06-11** [`54cba63b6c`](https://github.com/sgl-project/sglang/commit/54cba63b6c) [#27779](https://github.com/sgl-project/sglang/pull/27779)
  Fix paged SWA free mapping cleanup (#27779)
  _Files: `python/sglang/srt/mem_cache/allocator/swa.py`, `test/registered/unit/mem_cache/test_swa_unittest.py`_
- **2026-06-11** [`5e0271536a`](https://github.com/sgl-project/sglang/commit/5e0271536a) [#27759](https://github.com/sgl-project/sglang/pull/27759)
  [UnifiedTree]: HybridModel launches HiCache via UnifiedTree by default. (#27759)
  _Files: `python/sglang/srt/mem_cache/registry.py`, `test/registered/unit/mem_cache/test_registry.py`_
- **2026-06-11** [`b4bed8c398`](https://github.com/sgl-project/sglang/commit/b4bed8c398) [#27709](https://github.com/sgl-project/sglang/pull/27709)
  [diffusion] fix: cast to float32 (from float64) in triton kernel to unblock torch.compile (#27709)
  _Files: `python/sglang/jit_kernel/diffusion/triton/sana_wm_gdn_chunkwise.py`_
- **2026-06-11** [`db061e97c0`](https://github.com/sgl-project/sglang/commit/db061e97c0) [#27108](https://github.com/sgl-project/sglang/pull/27108)
  [Unified] Fix UnifiedRadixCache write_backup issue  in write-back mode(#27108)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-06-11** [`740305e1d9`](https://github.com/sgl-project/sglang/commit/740305e1d9) [#26670](https://github.com/sgl-project/sglang/pull/26670)
  [HiCache] Add opt-in LRU eviction to file storage backend (CP-aware) (#26670)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/storage/file/__init__.py`, `python/sglang/srt/mem_cache/storage/file/lru_file_evictor.py` _+1 more__
- **2026-06-10** [`5fefe91289`](https://github.com/sgl-project/sglang/commit/5fefe91289) [#27799](https://github.com/sgl-project/sglang/pull/27799)
  [Spec] `NGRAMWorker` on `BaseSpecWorker`; algo-owned verify-tree shape params (#27799)
  _Files: `python/sglang/srt/mem_cache/common.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/ngram_info.py`, `python/sglang/srt/speculative/ngram_worker.py` _+2 more__
- **2026-06-10** [`d1895cb60d`](https://github.com/sgl-project/sglang/commit/d1895cb60d) [#27764](https://github.com/sgl-project/sglang/pull/27764)
  [Spec] Extract move_accept_tokens_to_target_kvcache into spec_utils (#27764)
  _Files: `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/spec_utils.py`_
- **2026-06-10** [`f101b287ef`](https://github.com/sgl-project/sglang/commit/f101b287ef) [#27655](https://github.com/sgl-project/sglang/pull/27655)
  [Unified Tree]fix compatibility with eagle key and l3 hicache (#27655)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dsv4.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-06-10** [`854d232a40`](https://github.com/sgl-project/sglang/commit/854d232a40) [#27688](https://github.com/sgl-project/sglang/pull/27688)
  Fix flaky hicache l3 mmlu nightly test (#27688)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_nightly.py`_
- **2026-06-09** [`42322947aa`](https://github.com/sgl-project/sglang/commit/42322947aa) [#27645](https://github.com/sgl-project/sglang/pull/27645)
  [BUG FIX]Fix DSA CPU offload mamba indices signature (#27645)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `test/registered/unit/mem_cache/test_dsa_pool_host_unit.py`_
- **2026-06-09** [`991689fd0d`](https://github.com/sgl-project/sglang/commit/991689fd0d) [#27550](https://github.com/sgl-project/sglang/pull/27550)
  fix(hiradix): wait for extra pool IO (#27550)
  _Files: `python/sglang/srt/mem_cache/hiradix_cache.py`_
- **2026-06-08** [`32bedbf88e`](https://github.com/sgl-project/sglang/commit/32bedbf88e) [#27531](https://github.com/sgl-project/sglang/pull/27531)
  [diffusion] model: support SANA-WM with streaming support (#27531)
  _Files: `python/sglang/jit_kernel/diffusion/triton/sana_wm_gdn.py`, `python/sglang/jit_kernel/diffusion/triton/sana_wm_gdn_chunkwise.py`, `python/sglang/multimodal_gen/apps/realtime_webui/app.js`, `python/sglang/multimodal_gen/apps/realtime_webui/index.html` _+54 more__
- **2026-06-08** [`62c505a196`](https://github.com/sgl-project/sglang/commit/62c505a196) [#27293](https://github.com/sgl-project/sglang/pull/27293)
  [HiCache][Dsv4] Don't cache C128 State pool in L3 (#27293)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`_
- **2026-06-08** [`1ff7c627cd`](https://github.com/sgl-project/sglang/commit/1ff7c627cd) [#27554](https://github.com/sgl-project/sglang/pull/27554)
  [UnifiedTree]: Support hicache metrics (#27554)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-06-08** [`d03182cd2d`](https://github.com/sgl-project/sglang/commit/d03182cd2d) [#27489](https://github.com/sgl-project/sglang/pull/27489)
  Fix TP deadlock in unified radix cache writing_check / loading_check (#27489)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-06-08** [`71a0b10462`](https://github.com/sgl-project/sglang/commit/71a0b10462) [#26938](https://github.com/sgl-project/sglang/pull/26938)
  Fix the _chunked_req_scheduled_last_iter flag with a content-based stash gate (#26938)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_chunked_req_gate.py`_
- **2026-06-08** [`3197808283`](https://github.com/sgl-project/sglang/commit/3197808283) [#26547](https://github.com/sgl-project/sglang/pull/26547)
  Avoid calling filter_batch with chunked_req_to_exclude being things unrelated to chunked reqs (#26547)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-06-08** [`6365d6faee`](https://github.com/sgl-project/sglang/commit/6365d6faee) [#27486](https://github.com/sgl-project/sglang/pull/27486)
  [spec] Misc defensive guards for EAGLE draft KV indexing (#27486)
  _Files: `python/sglang/jit_kernel/csrc/elementwise/kvcache.cuh`, `python/sglang/jit_kernel/kvcache.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker.py` _+2 more__

## Prefill / Decode Disaggregation  (29 commits)

- **2026-06-15** [`8bdb007e58`](https://github.com/sgl-project/sglang/commit/8bdb007e58) [#28277](https://github.com/sgl-project/sglang/pull/28277)
  [NPU] Docs op performance optimize (#28277)
  _Files: `docs_new/docs/advanced_features/pd_disaggregation.mdx`, `docs_new/docs/basic_usage/send_request.mdx`, `docs_new/docs/developer_guide/msprobe_debugging_guide.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_operator_performance_optimizing.mdx`_
- **2026-06-15** [`eb349efb14`](https://github.com/sgl-project/sglang/commit/eb349efb14) [#28031](https://github.com/sgl-project/sglang/pull/28031)
  [EPD][BugFix] Fix encode_with_global_cache_mooncake (#28031)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`_
- **2026-06-15** [`bf38a0b03d`](https://github.com/sgl-project/sglang/commit/bf38a0b03d) [#25736](https://github.com/sgl-project/sglang/pull/25736)
  Fix disaggregated decode load token accounting (#25736)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/scheduler_components/load_inquirer.py`_
- **2026-06-15** [`37505eca27`](https://github.com/sgl-project/sglang/commit/37505eca27) [#27122](https://github.com/sgl-project/sglang/pull/27122)
  feat: report multimodal (image/audio/video) token counts in usage.prompt_tokens_details (#27122)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py` _+7 more__
- **2026-06-14** [`bb48405c31`](https://github.com/sgl-project/sglang/commit/bb48405c31) [#28165](https://github.com/sgl-project/sglang/pull/28165)
  Unify NVTX annotation helpers and split the enable gate per subsystem (#28165)
  _Files: `python/sglang/srt/batch_overlap/operations.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py` _+5 more__
- **2026-06-14** [`50993554d8`](https://github.com/sgl-project/sglang/commit/50993554d8) [#28143](https://github.com/sgl-project/sglang/pull/28143)
  fix(health): make health-check rid unique across tokenizer workers (#28143)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/entrypoints/http_server.py`_
- **2026-06-14** [`a3fd5c24be`](https://github.com/sgl-project/sglang/commit/a3fd5c24be) [#27901](https://github.com/sgl-project/sglang/pull/27901)
  feat: add NVTX markers for the scheduler main loop (#27901)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py` _+2 more__
- **2026-06-13** [`10d3337048`](https://github.com/sgl-project/sglang/commit/10d3337048) [#27935](https://github.com/sgl-project/sglang/pull/27935)
  [AMD] Support unified_kv_triton for disaggregation (#27935)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py` _+5 more__
- **2026-06-13** [`806365e778`](https://github.com/sgl-project/sglang/commit/806365e778) [#27378](https://github.com/sgl-project/sglang/pull/27378)
  feat: Support HiCache for MiMo-V2 models (1/N) (#27378)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py` _+7 more__
- **2026-06-13** [`eb9483b5c2`](https://github.com/sgl-project/sglang/commit/eb9483b5c2) [#26288](https://github.com/sgl-project/sglang/pull/26288)
  [PD][AMD]: incremental KV transfer with decode radix cache (#26288)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-06-13** [`a14d1a5656`](https://github.com/sgl-project/sglang/commit/a14d1a5656) [#28098](https://github.com/sgl-project/sglang/pull/28098)
  Add DeepSeek V4 MTP acceptance length checks (#28098)
  _Files: `test/registered/cp/test_deepseek_v4_flash_fp4_b200_cp.py`, `test/registered/disaggregation/test_disaggregation_dsv4.py`, `test/registered/models_e2e/test_deepseek_v4_flash_fp4_b200.py`, `test/registered/models_e2e/test_deepseek_v4_flash_fp4_h200.py` _+2 more__
- **2026-06-12** [`1e71c1a859`](https://github.com/sgl-project/sglang/commit/1e71c1a859) [#28039](https://github.com/sgl-project/sglang/pull/28039)
  fix(pd): disable overlap for spec+grammar in disagg decode loop (#28039)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `test/registered/disaggregation/test_disaggregation_basic.py`_
- **2026-06-12** [`18989f3d48`](https://github.com/sgl-project/sglang/commit/18989f3d48) [#28022](https://github.com/sgl-project/sglang/pull/28022)
  [PD] Fix resource leak on prealloc/transfer abort and idle check (#28022)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/disaggregation/test_decode_queue_cleanup.py`_
- **2026-06-12** [`694cea8656`](https://github.com/sgl-project/sglang/commit/694cea8656) [#25994](https://github.com/sgl-project/sglang/pull/25994)
  Add EPD disaggregated encode tracing (#25994)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/observability/req_time_stats.py`_
- **2026-06-12** [`0a1fb0da86`](https://github.com/sgl-project/sglang/commit/0a1fb0da86) [#25954](https://github.com/sgl-project/sglang/pull/25954)
  add LRU eviction for mooncacke embedding cache (#25954)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/embedding_cache_controller.py`, `test/registered/unit/mem_cache/test_embedding_cache_controller.py`_
- **2026-06-11** [`10219bd9d6`](https://github.com/sgl-project/sglang/commit/10219bd9d6) [#27885](https://github.com/sgl-project/sglang/pull/27885)
  [PD] Fix negative prefill kv_transfer_alloc_ms under optimistic prefill (#27885)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/observability/req_time_stats.py`_
- **2026-06-11** [`6a012fbb2d`](https://github.com/sgl-project/sglang/commit/6a012fbb2d) [#27796](https://github.com/sgl-project/sglang/pull/27796)
  [PD] Fix ZMQ stale socket reconnection in PD disaggregation (#27796)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`_
- **2026-06-11** [`be45745f38`](https://github.com/sgl-project/sglang/commit/be45745f38) [#27039](https://github.com/sgl-project/sglang/pull/27039)
  [EPD] fix: zmq PUSH socket reconnect-aware connection management with tcp keepalive (#27039)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/encode_server.py`_
- **2026-06-11** [`9788c8e867`](https://github.com/sgl-project/sglang/commit/9788c8e867) [#27696](https://github.com/sgl-project/sglang/pull/27696)
  [RL] Handle Mooncake buffers across memory release (#27696)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py` _+1 more__
- **2026-06-10** [`6a16f29af6`](https://github.com/sgl-project/sglang/commit/6a16f29af6) [#25939](https://github.com/sgl-project/sglang/pull/25939)
  [AMD] ci: register 8 framework / unit tests to run on AMD CI (#25939)
  _Files: `test/registered/disaggregation/test_specv2_kvcache_offloading.py`, `test/registered/models/test_transformers_backend_eval.py`, `test/registered/unit/constrained/test_e2e_constrained_reasoning.py`, `test/registered/unit/managers/test_priority_scheduling_disaggregation.py` _+4 more__
- **2026-06-10** [`e76e4959b5`](https://github.com/sgl-project/sglang/commit/e76e4959b5) [#26908](https://github.com/sgl-project/sglang/pull/26908)
  [CI][PD] Add unit tests for nixl backend (#26908)
  _Files: `test/registered/unit/disaggregation/test_nixl_backend_basic.py`_
- **2026-06-10** [`e8a437ef26`](https://github.com/sgl-project/sglang/commit/e8a437ef26) [#27767](https://github.com/sgl-project/sglang/pull/27767)
  [diffusion] doc: update docs architecture (#27767)
  _Files: `docs_new/custom.css`, `docs_new/docs.json`, `docs_new/docs/sglang-diffusion/api/cli.mdx`, `docs_new/docs/sglang-diffusion/attention_backends.mdx` _+14 more__
- **2026-06-10** [`77c4d53f19`](https://github.com/sgl-project/sglang/commit/77c4d53f19) [#27608](https://github.com/sgl-project/sglang/pull/27608)
  [PD] Fix prefill bootstrap registration failure with --host 0.0.0.0 (#27608)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `test/registered/unit/disaggregation/test_register_to_bootstrap.py`_
- **2026-06-09** [`ab70153b62`](https://github.com/sgl-project/sglang/commit/ab70153b62) [#27415](https://github.com/sgl-project/sglang/pull/27415)
  [XPU][NIXL] Use uint64 for XPU address arithmetic in prep handle builders (#27415)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-06-08** [`6394a8b381`](https://github.com/sgl-project/sglang/commit/6394a8b381) [#27542](https://github.com/sgl-project/sglang/pull/27542)
  [EPD] Dynamic encoder registration cleanup (#27542)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`_
- **2026-06-08** [`8ff0c9fef9`](https://github.com/sgl-project/sglang/commit/8ff0c9fef9) [#27534](https://github.com/sgl-project/sglang/pull/27534)
  [PD] Downgrade propagated rank failure logs from error to debug (#27534)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py` _+2 more__
- **2026-06-08** [`13dda3b8de`](https://github.com/sgl-project/sglang/commit/13dda3b8de) [#22253](https://github.com/sgl-project/sglang/pull/22253)
  [EPD] Support dynamic encoder register (#22253)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/io_struct.py` _+2 more__
- **2026-06-08** [`18d728967a`](https://github.com/sgl-project/sglang/commit/18d728967a) [#26922](https://github.com/sgl-project/sglang/pull/26922)
  [PD][MoRI] Drive KV transfers with a sharded synchronous worker pool (#26922)
  _Files: `docker/rocm.Dockerfile`, `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/environ.py`, `test/registered/amd/disaggregation/test_mori_transfer_engine_e2e.py`_
- **2026-06-08** [`259a2da3e0`](https://github.com/sgl-project/sglang/commit/259a2da3e0) [#26637](https://github.com/sgl-project/sglang/pull/26637)
  Refactor Req.fill_ids into full_untruncated_fill_ids + fill_len with equivalence (#26637)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/prefill.py` _+25 more__

## Docs / Examples  (26 commits)

- **2026-06-15** [`81166f382d`](https://github.com/sgl-project/sglang/commit/81166f382d) [#28283](https://github.com/sgl-project/sglang/pull/28283)
  Fix inaccuracies and add NPU constraints in ascend_npu_profiling.mdx. (#28283)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_profiling.mdx`_
- **2026-06-15** [`f8d1d397b6`](https://github.com/sgl-project/sglang/commit/f8d1d397b6) [#28279](https://github.com/sgl-project/sglang/pull/28279)
  [NPU] fix ascend_docs (#28279)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_faq.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_operator_development.mdx`_
- **2026-06-15** [`f768344b1a`](https://github.com/sgl-project/sglang/commit/f768344b1a) [#28295](https://github.com/sgl-project/sglang/pull/28295)
  [DOCS][NPU]Supplementary Notes (#28295)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`_
- **2026-06-15** [`7bd1a9d163`](https://github.com/sgl-project/sglang/commit/7bd1a9d163) [#28284](https://github.com/sgl-project/sglang/pull/28284)
  Update documentation for Ascend NPU Guide (#28284)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_optimization.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_performance_testing.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quick_start.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-06-15** [`edd5eff519`](https://github.com/sgl-project/sglang/commit/edd5eff519) [#28296](https://github.com/sgl-project/sglang/pull/28296)
  [NPU] [DOC] fix issues in ascend_npu_support_new_models (#28296)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_new_models.mdx`_
- **2026-06-14** [`93b402580c`](https://github.com/sgl-project/sglang/commit/93b402580c) [#28160](https://github.com/sgl-project/sglang/pull/28160)
  feat: add decode clear steps env var (#28160)
  _Files: `docs_new/docs/hardware-platforms/apple_metal.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/mlx/model_runner.py`_
- **2026-06-13** [`47fabb52ed`](https://github.com/sgl-project/sglang/commit/47fabb52ed) [#28150](https://github.com/sgl-project/sglang/pull/28150)
  docs(minimax-m3): add high-concurrency throughput tip for H200 bf16 (#28150)
  _Files: `docs_new/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`_
- **2026-06-13** [`d988d5d681`](https://github.com/sgl-project/sglang/commit/d988d5d681) [#28128](https://github.com/sgl-project/sglang/pull/28128)
  feat(cookbook): generic config-declared `flagSelects` playground axis (#28128)
  _Files: `.claude/skills/cookbook-add-model/references/engine-axis.md`, `.claude/skills/cookbook-migrate-model/SKILL.md`, `.claude/skills/cookbook-migrate-model/references/dimension-mapping.md`, `docs_new/src/snippets/_playground.jsx`_
- **2026-06-13** [`45f8d48994`](https://github.com/sgl-project/sglang/commit/45f8d48994) [#28078](https://github.com/sgl-project/sglang/pull/28078)
  docs: add llm-d page under Advanced Features (#28078)
  _Files: `docs_new/docs.json`, `docs_new/docs/advanced_features/llm-d.mdx`_
- **2026-06-13** [`c26669e37b`](https://github.com/sgl-project/sglang/commit/c26669e37b) [#28083](https://github.com/sgl-project/sglang/pull/28083)
  [NPU] [DOC] Update server arguments to NPU support features page (#28083)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-06-12** [`95867f0932`](https://github.com/sgl-project/sglang/commit/95867f0932) [#28087](https://github.com/sgl-project/sglang/pull/28087)
  [Doc] Fix some inconsistencies in the Nemotron Cookbook (#28087)
  _Files: `docs_new/cookbook/autoregressive/NVIDIA/Nemotron3-Ultra.mdx`, `docs_new/src/snippets/autoregressive/nemotron3-ultra-deployment.jsx`_
- **2026-06-12** [`fa4273d2db`](https://github.com/sgl-project/sglang/commit/fa4273d2db) [#28064](https://github.com/sgl-project/sglang/pull/28064)
  [Docs] Add Kimi K2.7 Code cookbook (#28064)
  _Files: `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K2.6.mdx`, `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K2.7-Code.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/cookbook/intro copy.mdx` _+2 more__
- **2026-06-12** [`9f6b2339f9`](https://github.com/sgl-project/sglang/commit/9f6b2339f9) [#28062](https://github.com/sgl-project/sglang/pull/28062)
  docs(minimax-m3): warm-steady-state benchmark numbers (#28062)
  _Files: `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx`_
- **2026-06-12** [`50815d54a7`](https://github.com/sgl-project/sglang/commit/50815d54a7) [#28061](https://github.com/sgl-project/sglang/pull/28061)
  docs (#28061)
- **2026-06-12** [`dba617f2ec`](https://github.com/sgl-project/sglang/commit/dba617f2ec) [#28060](https://github.com/sgl-project/sglang/pull/28060)
  doc: update docs for new model (#28060)
  _Files: `docs_new/cookbook/autoregressive/MiniMax/MiniMax-M2.7.mdx`, `docs_new/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json` _+2 more__
- **2026-06-12** [`83c0007f8d`](https://github.com/sgl-project/sglang/commit/83c0007f8d) [#27866](https://github.com/sgl-project/sglang/pull/27866)
  examples: add Chain-of-Verification (CoVe) hallucination reduction demo (#27866)
  _Files: `examples/runtime/README.md`, `examples/runtime/chain_of_verification.py`_
- **2026-06-12** [`66ab5c9c7a`](https://github.com/sgl-project/sglang/commit/66ab5c9c7a) [#27997](https://github.com/sgl-project/sglang/pull/27997)
  fix(gateway): make sgl-model-gateway a cargo workspace so maturin 1.14 accepts the parent README (#27997)
  _Files: `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/bindings/python/Cargo.toml`, `sgl-model-gateway/bindings/python/src/lib.rs`_
- **2026-06-12** [`40894be3c3`](https://github.com/sgl-project/sglang/commit/40894be3c3) [#27409](https://github.com/sgl-project/sglang/pull/27409)
  add lfm2.5 to new cookbook. (#27409)
  _Files: `docs_new/cards/logos/liquidai.png`, `docs_new/cookbook/autoregressive/LiquidAI/LFM2.5.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json` _+2 more__
- **2026-06-11** [`0bac184425`](https://github.com/sgl-project/sglang/commit/0bac184425) [#24465](https://github.com/sgl-project/sglang/pull/24465)
  [NVIDIA] Update Minimax-M2.5,M2.7 docs with flags for performance  (#24465)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `docs_new/src/snippets/autoregressive/minimax-m25-deployment.jsx`, `docs_new/src/snippets/autoregressive/minimax-m27-deployment.jsx`_
- **2026-06-11** [`ce0ff154a5`](https://github.com/sgl-project/sglang/commit/ce0ff154a5) [#27665](https://github.com/sgl-project/sglang/pull/27665)
  add mimo best practice (#27665)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`_
- **2026-06-11** [`fc1fee528c`](https://github.com/sgl-project/sglang/commit/fc1fee528c) [#27677](https://github.com/sgl-project/sglang/pull/27677)
  [NPU] [DOC] replace <code> with backticks and remove obsolete params (#27677)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-06-10** [`73d0989d9b`](https://github.com/sgl-project/sglang/commit/73d0989d9b) [#27827](https://github.com/sgl-project/sglang/pull/27827)
  docs: make playground issue template model field a free-form input (#27827)
  _Files: `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-review-pr/SKILL.md`, `.github/ISSUE_TEMPLATE/3-playground-verified-cell.yml`_
- **2026-06-10** [`276c98c6cf`](https://github.com/sgl-project/sglang/commit/276c98c6cf) [#27714](https://github.com/sgl-project/sglang/pull/27714)
  [Docs] Add Kimi-K2.6 NVFP4 and update Kimi-K2.5 cookbook guidance (#27714)
  _Files: `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K2.5.mdx`, `docs_new/cookbook/autoregressive/Moonshotai/Kimi-K2.6.mdx`, `docs_new/src/snippets/autoregressive/kimi-k25-deployment.jsx`, `docs_new/src/snippets/autoregressive/kimi-k26-deployment.jsx`_
- **2026-06-10** [`91ff7baa28`](https://github.com/sgl-project/sglang/commit/91ff7baa28) [#27708](https://github.com/sgl-project/sglang/pull/27708)
  [Docs] Add GLM-5.1 NVFP4 to cookbook (#27708)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.1.mdx`, `docs_new/src/snippets/autoregressive/glm-51-deployment.jsx`_
- **2026-06-09** [`badab6b136`](https://github.com/sgl-project/sglang/commit/badab6b136) [#27591](https://github.com/sgl-project/sglang/pull/27591)
  [router] Add request/TTFT/worker metrics + Grafana dashboard to experimental sgl-router (#27591)
  _Files: `experimental/sgl-router/monitoring/README.md`, `experimental/sgl-router/monitoring/grafana-dashboard.json`, `experimental/sgl-router/src/health/circuit_breaker.rs`, `experimental/sgl-router/src/proxy/mod.rs` _+6 more__
- **2026-06-08** [`801fe5e0f2`](https://github.com/sgl-project/sglang/commit/801fe5e0f2) [#27517](https://github.com/sgl-project/sglang/pull/27517)
  docs: sync LMSYS SGLang blog cards (#27517)
  _Files: `docs_new/index.mdx`_

## MoE / Expert Parallel  (26 commits)

- **2026-06-15** [`63df86f5e7`](https://github.com/sgl-project/sglang/commit/63df86f5e7) [#22985](https://github.com/sgl-project/sglang/pull/22985)
  [AMD] Skip eplb bookkeeping and topk remap when EPLB is not in use on mori-ep / HIP (#22985) (#28188)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`, `python/sglang/srt/layers/moe/topk.py`_
- **2026-06-15** [`441b75ee69`](https://github.com/sgl-project/sglang/commit/441b75ee69) [#27588](https://github.com/sgl-project/sglang/pull/27588)
  [quantization] NVFP4 MoE: split fused w13 gate/up global scales (#27588)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `test/registered/unit/layers/quantization/test_modelopt_nvfp4_moe_scales.py`_
- **2026-06-14** [`f18d38d040`](https://github.com/sgl-project/sglang/commit/f18d38d040) [#28213](https://github.com/sgl-project/sglang/pull/28213)
  Revert "[AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs" (#28213)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/dequantization.py` _+11 more__
- **2026-06-14** [`f79a6b5c33`](https://github.com/sgl-project/sglang/commit/f79a6b5c33) [#28149](https://github.com/sgl-project/sglang/pull/28149)
  Support GLM-4.7 function calling via structural tags (#28149)
  _Files: `python/sglang/srt/function_call/glm47_moe_detector.py`, `test/registered/unit/function_call/test_function_call_parser.py`_
- **2026-06-14** [`171037c3e7`](https://github.com/sgl-project/sglang/commit/171037c3e7) [#27869](https://github.com/sgl-project/sglang/pull/27869)
  Fix Qwen3.5 deterministic batch-invariant logprobs (#27869)
  _Files: `python/sglang/srt/layers/attention/fla/layernorm_gated.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/fused_moe.py`, `test/registered/attention/test_qwen35_deterministic.py`_
- **2026-06-14** [`91c63aeb4d`](https://github.com/sgl-project/sglang/commit/91c63aeb4d) [#28041](https://github.com/sgl-project/sglang/pull/28041)
  Fix stale CUDA graph benchmark and docs refs (#28041)
  _Files: `benchmark/kernels/fused_moe_triton/benchmark_torch_compile_fused_moe.py`, `docs_new/docs/advanced_features/breakable_cuda_graph.mdx`, `docs_new/docs/advanced_features/piecewise_cuda_graph.mdx`, `python/sglang/srt/model_executor/runner_backend_utils/breakable_cuda_graph/__init__.py`_
- **2026-06-13** [`3f4a338212`](https://github.com/sgl-project/sglang/commit/3f4a338212) [#18182](https://github.com/sgl-project/sglang/pull/18182)
  [AMD][Quantization] Online MXFP4 quantization 2/N - FP8 to MXFP4 requantization on AMD GPUs (#18182)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/linear.py`, `python/sglang/srt/layers/quantization/dequantization.py` _+11 more__
- **2026-06-13** [`0e592395c7`](https://github.com/sgl-project/sglang/commit/0e592395c7) [#26188](https://github.com/sgl-project/sglang/pull/26188)
  [Apple Silicon] [MLX] Fuse SwiGLU activation into gate gather_qmv for SwitchGLU MoE blocks (#26188)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `python/sglang/srt/hardware_backend/mlx/moe/__init__.py`, `python/sglang/srt/hardware_backend/mlx/moe/fused_swiglu.py` _+2 more__
- **2026-06-13** [`aea0e30853`](https://github.com/sgl-project/sglang/commit/aea0e30853) [#26924](https://github.com/sgl-project/sglang/pull/26924)
  [4/N] Qwen3.5Opt: Overlap mamba verify update with draft extend (#26924)
  _Files: `benchmark/kernels/bench_fused_gate_sigmoid_mul_add.py`, `benchmark/kernels/bench_fused_sigmoid_mul.py`, `python/sglang/srt/layers/elementwise.py`, `python/sglang/srt/models/qwen2_moe.py` _+3 more__
- **2026-06-13** [`60d4bd4c70`](https://github.com/sgl-project/sglang/commit/60d4bd4c70) [#27855](https://github.com/sgl-project/sglang/pull/27855)
  [AMD] fix moriep quant kernel not implemented issue (#27855)
  _Files: `python/sglang/srt/layers/moe/moe_runner/aiter.py`_
- **2026-06-13** [`f288283c07`](https://github.com/sgl-project/sglang/commit/f288283c07) [#27057](https://github.com/sgl-project/sglang/pull/27057)
  [AMD] move shared expert check function to quark (#27057)
  _Files: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_5.py`_
- **2026-06-13** [`d1a39b0c74`](https://github.com/sgl-project/sglang/commit/d1a39b0c74) [#27720](https://github.com/sgl-project/sglang/pull/27720)
  [DeepSeek V3] Defer moe finalize and fused it with main stream add (#27720)
  _Files: `python/sglang/jit_kernel/csrc/moe/moe_finalize_fuse_shared.cu`, `python/sglang/jit_kernel/csrc/moe/tvm_ffi_utils.h`, `python/sglang/jit_kernel/moe_finalize_fuse_shared.py`, `python/sglang/srt/environ.py` _+3 more__
- **2026-06-13** [`82eedd5bd0`](https://github.com/sgl-project/sglang/commit/82eedd5bd0) [#27107](https://github.com/sgl-project/sglang/pull/27107)
  [DeepEP] Enable fabric handles automatically when supported (#27107)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`_
- **2026-06-12** [`f23f48df98`](https://github.com/sgl-project/sglang/commit/f23f48df98) [#27945](https://github.com/sgl-project/sglang/pull/27945)
  fix(moe): make FlashInfer A2A robust to collapsed global_num_tokens (moe_dense_tp_size NaN) (#27945)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`_
- **2026-06-11** [`06e0df5899`](https://github.com/sgl-project/sglang/commit/06e0df5899) [#26204](https://github.com/sgl-project/sglang/pull/26204)
  Optimize Qwen3 Next FP8 MoE on H200 (#26204)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=513,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=513,N=512,device_name=NVIDIA_H200,dtype=fp8_w8a8,block_shape=[128, 128]_down.json`, `python/sglang/srt/models/qwen2_moe.py`, `python/sglang/srt/models/qwen3_next.py` _+1 more__
- **2026-06-11** [`6ac9f66596`](https://github.com/sgl-project/sglang/commit/6ac9f66596) [#27841](https://github.com/sgl-project/sglang/pull/27841)
  Remove MoE prefill CUDA graph disable guard (#27841)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-11** [`b8376aebd0`](https://github.com/sgl-project/sglang/commit/b8376aebd0) [#27858](https://github.com/sgl-project/sglang/pull/27858)
  [AMD] Fix the dsv4 performance of MoE issue. (#27858)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`_
- **2026-06-10** [`0ae27405d0`](https://github.com/sgl-project/sglang/commit/0ae27405d0) [#22985](https://github.com/sgl-project/sglang/pull/22985)
  [AMD] Support eplb for moriep (#22985)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/eplb/expert_location_dispatch.py`, `python/sglang/srt/eplb/expert_location_updater.py` _+5 more__
- **2026-06-10** [`01f10acd06`](https://github.com/sgl-project/sglang/commit/01f10acd06) [#26083](https://github.com/sgl-project/sglang/pull/26083)
  Implement online nvfp4 quantization (#26083)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/configs/model_config.py` _+8 more__
- **2026-06-10** [`7e3e616159`](https://github.com/sgl-project/sglang/commit/7e3e616159) [#25007](https://github.com/sgl-project/sglang/pull/25007)
  Add Arm64 INT8 MoE test coverage (#25007)
  _Files: `.github/workflows/pr-test-arm64.yml`, `test/registered/cpu/arm64/test_moe.py`, `test/registered/cpu/test_activation.py`, `test/registered/cpu/test_decode.py` _+8 more__
- **2026-06-10** [`6565b7c464`](https://github.com/sgl-project/sglang/commit/6565b7c464) [#27726](https://github.com/sgl-project/sglang/pull/27726)
  [Docs] Update MegaMoE handling and rerun benchmarks (#27726)
  _Files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/references/engine-axis.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl` _+4 more__
- **2026-06-10** [`2947781ce6`](https://github.com/sgl-project/sglang/commit/2947781ce6) [#25455](https://github.com/sgl-project/sglang/pull/25455)
  [NPU] MiMo-V2-Flash Adaptation (#25455)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/multi_layer_eagle_draft_extend_npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`, `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py` _+5 more__
- **2026-06-09** [`c6be251c5b`](https://github.com/sgl-project/sglang/commit/c6be251c5b) [#26717](https://github.com/sgl-project/sglang/pull/26717)
  [NPU] RL update_weights_from_disk/ tensor /distributed (#26717)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`_
- **2026-06-09** [`a287ab83c0`](https://github.com/sgl-project/sglang/commit/a287ab83c0) [#26791](https://github.com/sgl-project/sglang/pull/26791)
  Fix Gemma4 NVFP4 MoE default attention backend (#26791)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-08** [`ca66e6fb5e`](https://github.com/sgl-project/sglang/commit/ca66e6fb5e) [#25195](https://github.com/sgl-project/sglang/pull/25195)
  [BCG] Support breakable CUDA graph for DeepSeek V4 DP attention (#25195)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/mega_moe_pre_dispatch.cuh`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py` _+9 more__
- **2026-06-08** [`1f5dc2cdca`](https://github.com/sgl-project/sglang/commit/1f5dc2cdca) [#26786](https://github.com/sgl-project/sglang/pull/26786)
  [GPTQ] Refactor CPU quantization schemes (#26786)
  _Files: `python/sglang/srt/hardware_backend/cpu/quantization/awq_kernels.py`, `python/sglang/srt/hardware_backend/cpu/quantization/gptq_kernels.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/auto_round.py` _+9 more__

## Speculative Decoding  (23 commits)

- **2026-06-15** [`ce9fad7196`](https://github.com/sgl-project/sglang/commit/ce9fad7196) [#28043](https://github.com/sgl-project/sglang/pull/28043)
  [Bugfix][DeepSeek-V4] Fix Spec V2 Draft Input ID Dtype for DP Collectives (#28043)
  _Files: `python/sglang/srt/speculative/base_spec_worker.py`_
- **2026-06-15** [`0417951a86`](https://github.com/sgl-project/sglang/commit/0417951a86) [#27882](https://github.com/sgl-project/sglang/pull/27882)
  [Bug Fix] Validate tokenizer-dependent features with skip_tokenizer_init (#27882)
  _Files: `python/sglang/srt/sampling/sampling_params.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/managers/test_stop_str_speculative.py`, `test/registered/unit/sampling/test_sampling_params.py`_
- **2026-06-13** [`32ef040618`](https://github.com/sgl-project/sglang/commit/32ef040618) [#28117](https://github.com/sgl-project/sglang/pull/28117)
  [Spec] Move eagle verify `prepare_for_verify`/`sample` to `eagle_utils` free helpers (#28117)
  _Files: `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_utils.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` _+3 more__
- **2026-06-13** [`e9c3b262e4`](https://github.com/sgl-project/sglang/commit/e9c3b262e4) [#28026](https://github.com/sgl-project/sglang/pull/28026)
  [Bugfix][Spec] Fix multi-layer EAGLE DRAFT_EXTEND_V2 attn-TP logprob metadata capture (#28026)
  _Files: `python/sglang/srt/speculative/multi_layer_eagle_draft_extend_cuda_graph_runner.py`_
- **2026-06-13** [`5633ca8599`](https://github.com/sgl-project/sglang/commit/5633ca8599) [#28105](https://github.com/sgl-project/sglang/pull/28105)
  [Spec] Move `prepare_for_draft` to `EagleDraftWorkerBase` (#28105)
  _Files: `python/sglang/srt/speculative/base_spec_worker.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-06-12** [`d601edab73`](https://github.com/sgl-project/sglang/commit/d601edab73) [#28096](https://github.com/sgl-project/sglang/pull/28096)
  [Spec] Fix EagleDraftWorker draft-extend attn backend assignment (#28096)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`, `test/registered/unit/spec/test_eagle_worker_v2_topk1_fastpath.py`_
- **2026-06-12** [`caf59759ea`](https://github.com/sgl-project/sglang/commit/caf59759ea) [#28032](https://github.com/sgl-project/sglang/pull/28032)
  [Spec] Centralize dummy verify-input capture; add `carries_draft_hidden_states` (#28032)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/spec_info.py`_
- **2026-06-12** [`a52ccd2179`](https://github.com/sgl-project/sglang/commit/a52ccd2179) [#24860](https://github.com/sgl-project/sglang/pull/24860)
  [Spec] Install `EagleDraftExtendInput` as the V2 draft-extend `spec_info` (#24860)
  _Files: `python/sglang/srt/kv_canary/plan_input.py`, `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` _+1 more__
- **2026-06-12** [`e1164a6dfc`](https://github.com/sgl-project/sglang/commit/e1164a6dfc) [#27761](https://github.com/sgl-project/sglang/pull/27761)
  [Spec] Remove dead `prepare_for_verify` / `prepare_extend_after_decode` + extend-decode kernel (#27761)
  _Files: `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/spec_utils.py`, `python/sglang/srt/speculative/triton_ops/cache_locs.py`_
- **2026-06-12** [`7074704c0c`](https://github.com/sgl-project/sglang/commit/7074704c0c) [#27966](https://github.com/sgl-project/sglang/pull/27966)
  [Spec] Dedup post-verify mamba state commit into shared spec_utils helpers (#27966)
  _Files: `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/ngram_worker.py`, `python/sglang/srt/speculative/spec_utils.py`_
- **2026-06-11** [`d71e9bede6`](https://github.com/sgl-project/sglang/commit/d71e9bede6) [#26351](https://github.com/sgl-project/sglang/pull/26351)
  [bugfix] commit Mamba states after NGRAM target verify (#26351)
  _Files: `python/sglang/srt/speculative/ngram_worker.py`_
- **2026-06-11** [`df5055e00f`](https://github.com/sgl-project/sglang/commit/df5055e00f) [#27952](https://github.com/sgl-project/sglang/pull/27952)
  Bump spec logprob match delta for the bf16 eagle fixture (#27952)
  _Files: `python/sglang/test/kits/spec_server_kits.py`_
- **2026-06-11** [`880e6f66fc`](https://github.com/sgl-project/sglang/commit/880e6f66fc) [#27857](https://github.com/sgl-project/sglang/pull/27857)
  [BCG] Share output buffers across capture sizes + typed ShapeKey (#27857)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_cudagraph_backend.py`, `python/sglang/srt/model_executor/runner/__init__.py`, `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py` _+8 more__
- **2026-06-11** [`493bb6ae0d`](https://github.com/sgl-project/sglang/commit/493bb6ae0d) [#27883](https://github.com/sgl-project/sglang/pull/27883)
  Fix fp16 NaN flake in spec CI: bf16 eagle fixture; sanitize NaN logits in sampler (#27883)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/utils/async_probe.py` _+1 more__
- **2026-06-10** [`16124fc9b2`](https://github.com/sgl-project/sglang/commit/16124fc9b2) [#27836](https://github.com/sgl-project/sglang/pull/27836)
  [Metrics] Fix `fwd_occupancy` reading NaN on every decode log line; probe-free `base-a` (#27836)
  _Files: `.github/workflows/_pr-test-stage.yml`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `test/registered/core/test_basic_sanity.py`, `test/registered/core/test_basic_sanity_eagle3.py`_
- **2026-06-10** [`3600a9ac5f`](https://github.com/sgl-project/sglang/commit/3600a9ac5f) [#27493](https://github.com/sgl-project/sglang/pull/27493)
  [SPEC] feat: init adaptive spec params from config (#27493)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/adaptive_spec_params.py`, `test/registered/spec/eagle/test_adaptive_speculative.py` _+2 more__
- **2026-06-09** [`53a4b51f8c`](https://github.com/sgl-project/sglang/commit/53a4b51f8c) [#26049](https://github.com/sgl-project/sglang/pull/26049)
  Fix GLM NextN draft value head dim (#26049)
  _Files: `python/sglang/srt/configs/model_config.py`_
- **2026-06-09** [`2218622f50`](https://github.com/sgl-project/sglang/commit/2218622f50) [#25980](https://github.com/sgl-project/sglang/pull/25980)
  Fix spec v2 stop output boundary (#25980)
  _Files: `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_stop_str_speculative.py`, `test/registered/unit/managers/test_trim_matched_stop.py`_
- **2026-06-09** [`d145a6127a`](https://github.com/sgl-project/sglang/commit/d145a6127a) [#23802](https://github.com/sgl-project/sglang/pull/23802)
  fix: stop-string check misses early matches during speculative decoding (#23802)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_stop_str_speculative.py`_
- **2026-06-09** [`9a3e845fc1`](https://github.com/sgl-project/sglang/commit/9a3e845fc1) [#27615](https://github.com/sgl-project/sglang/pull/27615)
  [Spec] Add nvtx to spec regions (#27615)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/frozen_kv_mtp_worker.py`, `python/sglang/srt/speculative/spec_utils.py`_
- **2026-06-08** [`3fe6bc390b`](https://github.com/sgl-project/sglang/commit/3fe6bc390b) [#27599](https://github.com/sgl-project/sglang/pull/27599)
  [Spec] Naming cleanup: contiguous draft-loc kernel + `accepted`->`accept` (#27599)
  _Files: `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/spec_utils.py`, `python/sglang/srt/speculative/triton_ops/cache_locs.py` _+2 more__
- **2026-06-08** [`c95179bc85`](https://github.com/sgl-project/sglang/commit/c95179bc85) [#27233](https://github.com/sgl-project/sglang/pull/27233)
  [Spec] Fuse small kenrels under `gather_spec_extras`  (#27233)
  _Files: `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/speculative/triton_ops/gather_spec_extras.py`, `test/registered/kernels/test_gather_spec_extras.py`_
- **2026-06-08** [`b5c64b94d5`](https://github.com/sgl-project/sglang/commit/b5c64b94d5) [#27552](https://github.com/sgl-project/sglang/pull/27552)
  [Spec] Rename token resolver to `_resolve_spec_v2_tokens`; remove dead V1 helpers (#27552)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/scheduler_components/weight_updater.py`, `python/sglang/srt/speculative/eagle_utils.py`, `python/sglang/srt/speculative/spec_utils.py` _+2 more__

## Other  (22 commits)

- **2026-06-15** [`bf186cf8fc`](https://github.com/sgl-project/sglang/commit/bf186cf8fc) [#27802](https://github.com/sgl-project/sglang/pull/27802)
  bugfix revise interface get cpu copy for npu mem pool to align with gpu (#27802)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-06-15** [`a88ba6cc0b`](https://github.com/sgl-project/sglang/commit/a88ba6cc0b) [#28228](https://github.com/sgl-project/sglang/pull/28228)
  [Fix] Reduce power of two to constant time (#28228)
  _Files: `experimental/sgl-router/src/policies/power_of_two.rs`, `experimental/sgl-router/tests/component/policies/power_of_two.rs`_
- **2026-06-15** [`c0dfe4c8ec`](https://github.com/sgl-project/sglang/commit/c0dfe4c8ec) [#27980](https://github.com/sgl-project/sglang/pull/27980)
  [router] Reconcile workers that registered without resolving model_ids (#27980)
  _Files: `experimental/sgl-router/src/discovery/k8s.rs`, `experimental/sgl-router/src/workers/manager.rs`, `experimental/sgl-router/tests/component/workers/manager.rs`_
- **2026-06-14** [`54acffc864`](https://github.com/sgl-project/sglang/commit/54acffc864) [#27102](https://github.com/sgl-project/sglang/pull/27102)
  Eval accuracy gpqa aime25 mixins (#27102)
  _Files: `python/sglang/test/kits/eval_accuracy_kit.py`, `test/registered/unit/test_eval_accuracy_kit_sgl_eval.py`_
- **2026-06-14** [`b250bea994`](https://github.com/sgl-project/sglang/commit/b250bea994) [#28153](https://github.com/sgl-project/sglang/pull/28153)
  fix(sampling): reject non-finite temperature in SamplingParams.verify (#28153)
  _Files: `python/sglang/srt/sampling/sampling_params.py`, `test/registered/unit/sampling/test_sampling_params.py`_
- **2026-06-13** [`1800d7caa6`](https://github.com/sgl-project/sglang/commit/1800d7caa6) [#27724](https://github.com/sgl-project/sglang/pull/27724)
  Bump ray minimum version to 2.55.1 (#27724)
  _Files: `python/pyproject.toml`_
- **2026-06-13** [`b001d3e815`](https://github.com/sgl-project/sglang/commit/b001d3e815) [#28120](https://github.com/sgl-project/sglang/pull/28120)
  Add prajjwal1 to CI_PERMISSIONS.json (#28120)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-06-13** [`ade30fd494`](https://github.com/sgl-project/sglang/commit/ade30fd494) [#28094](https://github.com/sgl-project/sglang/pull/28094)
  fix(server): serialize nested dict config values as JSON (#28094)
  _Files: `python/sglang/srt/server_args_config_parser.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-06-12** [`9d37e710b7`](https://github.com/sgl-project/sglang/commit/9d37e710b7) [#27662](https://github.com/sgl-project/sglang/pull/27662)
  [Bench] Add consistent p90/p95/p99 percentiles for all latency metrics (#27662)
  _Files: `python/sglang/bench_serving.py`_
- **2026-06-12** [`3be5a7ec89`](https://github.com/sgl-project/sglang/commit/3be5a7ec89) [#27399](https://github.com/sgl-project/sglang/pull/27399)
  Respect explicit --max-running-requests instead of clamping to heuristic (#27399)
  _Files: `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`_
- **2026-06-12** [`533b59d00c`](https://github.com/sgl-project/sglang/commit/533b59d00c) [#28066](https://github.com/sgl-project/sglang/pull/28066)
  Add @alexnails as codeowner for srt/platforms (#28066)
  _Files: `.github/CODEOWNERS`_
- **2026-06-12** [`97a0031799`](https://github.com/sgl-project/sglang/commit/97a0031799) [#27984](https://github.com/sgl-project/sglang/pull/27984)
  [lint] Enable Ruff UP037 to drop redundant quoted annotations (#27984)
- **2026-06-11** [`d26b90cf70`](https://github.com/sgl-project/sglang/commit/d26b90cf70) [#27957](https://github.com/sgl-project/sglang/pull/27957)
  Add weireweire to CI permissions (#27957)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-06-11** [`8077fb1df7`](https://github.com/sgl-project/sglang/commit/8077fb1df7) [#27922](https://github.com/sgl-project/sglang/pull/27922)
  fix(deepgemm): align PP-parallel warmup bs to CP padding (#27922)
  _Files: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`_
- **2026-06-11** [`dc1e46ec8f`](https://github.com/sgl-project/sglang/commit/dc1e46ec8f) [#27646](https://github.com/sgl-project/sglang/pull/27646)
  [Intel GPU]Add sycl mrope pass for xpu device (#27646)
  _Files: `python/sglang/srt/layers/rotary_embedding/mrope.py`_
- **2026-06-11** [`5f913c1135`](https://github.com/sgl-project/sglang/commit/5f913c1135) [#27190](https://github.com/sgl-project/sglang/pull/27190)
  [Fix] Emulate PDEATHSIG on macOS to prevent orphaned worker processes (#27190)
  _Files: `python/sglang/srt/hardware_backend/mlx/parent_watchdog.py`, `python/sglang/srt/utils/common.py`_
- **2026-06-10** [`0c7faf01fb`](https://github.com/sgl-project/sglang/commit/0c7faf01fb) [#27742](https://github.com/sgl-project/sglang/pull/27742)
  test(sgl-router): cover sticky scale-up no-redistribution e2e (#27742)
  _Files: `experimental/sgl-router/tests/proxy/sticky_routing.rs`_
- **2026-06-09** [`eb8dceda44`](https://github.com/sgl-project/sglang/commit/eb8dceda44) [#27671](https://github.com/sgl-project/sglang/pull/27671)
  Defer DeepGEMM PDL setup to worker init (#27671)
  _Files: `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`_
- **2026-06-09** [`609f5f549c`](https://github.com/sgl-project/sglang/commit/609f5f549c) [#27502](https://github.com/sgl-project/sglang/pull/27502)
  Add mixed-prefix gsm8k eval and its CPU unit test (#27502)
  _Files: `python/sglang/test/run_eval.py`, `python/sglang/test/simple_eval_gsm8k.py`, `python/sglang/test/simple_eval_mixed_prefix_gsm8k.py`, `test/registered/unit/bench/test_mixed_prefix_gsm8k.py`_
- **2026-06-09** [`317fc6a9dd`](https://github.com/sgl-project/sglang/commit/317fc6a9dd) [#27235](https://github.com/sgl-project/sglang/pull/27235)
  refactor: replace oversized 1.3MB tiny_tokenizer.json fixture with a genuinely tiny byte-level BPE fixture (#27235)
  _Files: `experimental/sgl-router/src/tokenizer/mod.rs`, `experimental/sgl-router/tests/fixtures/tiny_tokenizer.json`_
- **2026-06-08** [`f5fdf9c5d8`](https://github.com/sgl-project/sglang/commit/f5fdf9c5d8) [#26874](https://github.com/sgl-project/sglang/pull/26874)
  Speed up dump comparator percentile computation using numpy (#26874)
  _Files: `python/sglang/srt/debug_utils/comparator/tensor_comparator/comparator.py`, `test/registered/debug_utils/comparator/tensor_comparator/test_comparator.py`_
- **2026-06-08** [`6bc3953b48`](https://github.com/sgl-project/sglang/commit/6bc3953b48) [#27394](https://github.com/sgl-project/sglang/pull/27394)
  feat(agentic router): add sticky-session routing policy (#27394)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/policies/active_load.rs` _+22 more__

## Tensor / Data Parallel  (15 commits)

- **2026-06-15** [`33f99831f8`](https://github.com/sgl-project/sglang/commit/33f99831f8) [#28207](https://github.com/sgl-project/sglang/pull/28207)
  docs(minimax-m3): refresh B200 benchmarks (tp8, piecewise) + add GPQA (#28207)
  _Files: `docs_new/cookbook/autoregressive/MiniMax/MiniMax-M3.mdx`, `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3-benchmarks.jsx`, `docs_new/src/snippets/configs/MiniMaxAI/minimax-m3.jsx`_
- **2026-06-15** [`69b02ea68a`](https://github.com/sgl-project/sglang/commit/69b02ea68a) [#24548](https://github.com/sgl-project/sglang/pull/24548)
  [Distributed] Guard torch symm mem all-reduce sizes (#24548)
  _Files: `python/sglang/srt/distributed/device_communicators/torch_symm_mem.py`, `python/sglang/srt/distributed/parallel_state.py`_
- **2026-06-14** [`d72314808f`](https://github.com/sgl-project/sglang/commit/d72314808f) [#26706](https://github.com/sgl-project/sglang/pull/26706)
  [JIT Kernel] Multi-GPU test/bench framework for custom all-reduce + TP QKNorm (#26706)
  _Files: `python/sglang/jit_kernel/benchmark/marker.py`, `python/sglang/jit_kernel/benchmark/utils.py`, `python/sglang/jit_kernel/mp.py`, `python/sglang/jit_kernel/tests/utils.py` _+4 more__
- **2026-06-12** [`85712fa5b0`](https://github.com/sgl-project/sglang/commit/85712fa5b0) [#25881](https://github.com/sgl-project/sglang/pull/25881)
  Fix Responses API request handling (#25881)
  _Files: `python/sglang/srt/entrypoints/harmony_utils.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_responses.py` _+7 more__
- **2026-06-12** [`b3270264e4`](https://github.com/sgl-project/sglang/commit/b3270264e4) [#25876](https://github.com/sgl-project/sglang/pull/25876)
  Fix Anthropic Messages API compatibility (#25876)
  _Files: `python/sglang/srt/entrypoints/anthropic/protocol.py`, `python/sglang/srt/entrypoints/anthropic/serving.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py` _+1 more__
- **2026-06-12** [`f5c9f88ee2`](https://github.com/sgl-project/sglang/commit/f5c9f88ee2) [#23969](https://github.com/sgl-project/sglang/pull/23969)
  [plugin][distributed] use active platform's backend in `get_default_distributed_backend` (#23969)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/platforms/__init__.py`, `python/sglang/srt/platforms/device_mixin.py`, `test/registered/unit/distributed/test_get_default_distributed_backend.py`_
- **2026-06-10** [`255843d454`](https://github.com/sgl-project/sglang/commit/255843d454) [#26347](https://github.com/sgl-project/sglang/pull/26347)
  Support for Zyphra zaya1 model (#26347)
  _Files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/zaya.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/zaya.py` _+5 more__
- **2026-06-10** [`047e5df3b1`](https://github.com/sgl-project/sglang/commit/047e5df3b1) [#27758](https://github.com/sgl-project/sglang/pull/27758)
  Revert "Share BCG output buffers across capture sizes" (#27758)
  _Files: `python/sglang/srt/model_executor/breakable_cuda_graph_runner.py`_
- **2026-06-10** [`165331a200`](https://github.com/sgl-project/sglang/commit/165331a200) [#27659](https://github.com/sgl-project/sglang/pull/27659)
  Share BCG output buffers across capture sizes (#27659)
  _Files: `python/sglang/srt/model_executor/breakable_cuda_graph_runner.py`_
- **2026-06-09** [`ca716f4734`](https://github.com/sgl-project/sglang/commit/ca716f4734) [#27721](https://github.com/sgl-project/sglang/pull/27721)
  Add TP server GPU process regression test (#27721)
  _Files: `test/registered/core/test_no_extra_forked_cuda_context.py`_
- **2026-06-09** [`a32aeb688a`](https://github.com/sgl-project/sglang/commit/a32aeb688a) [#27580](https://github.com/sgl-project/sglang/pull/27580)
  [AMD] Fix AttributeError in GeneratedSharedPrefixDataset.from_args for in-process callers (#27580)
  _Files: `python/sglang/benchmark/datasets/generated_shared_prefix.py`_
- **2026-06-09** [`c2eae96c56`](https://github.com/sgl-project/sglang/commit/c2eae96c56) [#22734](https://github.com/sgl-project/sglang/pull/22734)
  MSCCL++ Integration (#22734)
  _Files: `benchmark/kernels/all_reduce/README.md`, `benchmark/kernels/all_reduce/benchmark_mscclpp.py`, `docker/Dockerfile`, `python/sglang/bench_one_batch.py` _+13 more__
- **2026-06-09** [`95090b837e`](https://github.com/sgl-project/sglang/commit/95090b837e) [#27612](https://github.com/sgl-project/sglang/pull/27612)
  [router] Add /flush_cache endpoint to experimental sgl-router (#27612)
  _Files: `experimental/sgl-router/src/server/app.rs`, `experimental/sgl-router/src/server/routes/cache.rs`, `experimental/sgl-router/src/server/routes/mod.rs`, `experimental/sgl-router/src/workers/registry.rs`_
- **2026-06-08** [`61e4132bc2`](https://github.com/sgl-project/sglang/commit/61e4132bc2) [#27537](https://github.com/sgl-project/sglang/pull/27537)
  [MUSA] bump torchada version to 0.1.59 and workaround PCG limitation. (#27537)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject_other.toml`, `sgl-kernel/pyproject_musa.toml`_
- **2026-06-08** [`995e649190`](https://github.com/sgl-project/sglang/commit/995e649190) [#26850](https://github.com/sgl-project/sglang/pull/26850)
  Add parallel-rank dump filenames and pipeline-global layer remapping to dumper (#26850)
  _Files: `python/sglang/srt/debug_utils/dumper.py`, `test/registered/debug_utils/test_dumper.py`_

## Triton / Kernels  (14 commits)

- **2026-06-15** [`d5899b95c4`](https://github.com/sgl-project/sglang/commit/d5899b95c4) [#27868](https://github.com/sgl-project/sglang/pull/27868)
  fix(qwen3.5): keep CUDA dual-stream overlap (regressed by #25885) (#27868)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-06-15** [`3b419f66da`](https://github.com/sgl-project/sglang/commit/3b419f66da) [#28273](https://github.com/sgl-project/sglang/pull/28273)
  [JIT] Track angle-bracket includes in source hash (#28273)
  _Files: `python/sglang/jit_kernel/utils.py`_
- **2026-06-15** [`1180b70440`](https://github.com/sgl-project/sglang/commit/1180b70440) [#27624](https://github.com/sgl-project/sglang/pull/27624)
  triton-ascend update (#27624)
  _Files: `docker/npu.Dockerfile`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-06-14** [`cc72e2bd8c`](https://github.com/sgl-project/sglang/commit/cc72e2bd8c) [#27773](https://github.com/sgl-project/sglang/pull/27773)
  [Docs] Fix outdated benchmark marker API in add-jit-kernel skill (#27773)
  _Files: `.claude/skills/add-jit-kernel/SKILL.md`_
- **2026-06-11** [`f8b0a120b8`](https://github.com/sgl-project/sglang/commit/f8b0a120b8) [#27747](https://github.com/sgl-project/sglang/pull/27747)
  fix: DSV4 BCG compress-prefill plan OOB on underfilled (tiny) prefill replay (#27747)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`_
- **2026-06-10** [`b40f365732`](https://github.com/sgl-project/sglang/commit/b40f365732) [#27781](https://github.com/sgl-project/sglang/pull/27781)
  [CI] Move misplaced mhc kernel test into test/registered/kernels (#27781)
  _Files: `test/registered/kernels/test_mhc_kernels.py`_
- **2026-06-10** [`70c71ba183`](https://github.com/sgl-project/sglang/commit/70c71ba183) [#27774](https://github.com/sgl-project/sglang/pull/27774)
  [NPU] Fix dead patch_model monkey-patch breaking NPU torch.compile capture (#27774)
  _Files: `python/sglang/srt/model_executor/runner/decode_cuda_graph_runner.py`_
- **2026-06-10** [`2495c02c2c`](https://github.com/sgl-project/sglang/commit/2495c02c2c) [#23906](https://github.com/sgl-project/sglang/pull/23906)
  [Refactor] Cuda Graph Runner/Backend Refactor (#23906)
- **2026-06-09** [`fde4004429`](https://github.com/sgl-project/sglang/commit/fde4004429) [#24401](https://github.com/sgl-project/sglang/pull/24401)
  [Fix] Reset positions tensor in CUDA graph runner when batch size differs from captured size (#24401)
  _Files: `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`_
- **2026-06-09** [`186f1e300a`](https://github.com/sgl-project/sglang/commit/186f1e300a) [#27644](https://github.com/sgl-project/sglang/pull/27644)
  [CI] Move JIT kernel tests + benchmarks to test/registered/jit; add in-package guard (#27644)
- **2026-06-09** [`d981b7b9c4`](https://github.com/sgl-project/sglang/commit/d981b7b9c4) [#27549](https://github.com/sgl-project/sglang/pull/27549)
  [Fix] Avoid applying cuda graph input-buffer registry on non-cuda devices (#27549)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-06-09** [`cae022aa88`](https://github.com/sgl-project/sglang/commit/cae022aa88) [#27605](https://github.com/sgl-project/sglang/pull/27605)
  [JIT] Reuse JIT kernel build cache across CI runs (#27605)
  _Files: `python/sglang/jit_kernel/utils.py`_
- **2026-06-09** [`15c801f726`](https://github.com/sgl-project/sglang/commit/15c801f726) [#22516](https://github.com/sgl-project/sglang/pull/22516)
  fix(server): clamp piecewise_cuda_graph_max_tokens to context_length (#22516)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-08** [`12de907bc2`](https://github.com/sgl-project/sglang/commit/12de907bc2) [#27242](https://github.com/sgl-project/sglang/pull/27242)
  [MUSA][23/N] CI: Fix torchada preflight lock cleanup and add LLM server smoke test (#27242)
  _Files: `.github/workflows/nightly-test-musa.yml`, `.github/workflows/pr-test-musa.yml`, `.github/workflows/release-whl-kernel.yml`, `python/sglang/test/ci/ci_register.py` _+3 more__

## ROCm / AMD  (14 commits)

- **2026-06-15** [`9864059e2b`](https://github.com/sgl-project/sglang/commit/9864059e2b) [#28249](https://github.com/sgl-project/sglang/pull/28249)
  [AMD] Update AITER commit (#28249)
  _Files: `docker/rocm.Dockerfile`_
- **2026-06-15** [`c127ba6483`](https://github.com/sgl-project/sglang/commit/c127ba6483) [#28214](https://github.com/sgl-project/sglang/pull/28214)
  [AMD] ci: fix scheduled AMD runs startup failure when calling extra-a suite (#28214)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`_
- **2026-06-12** [`65d76bd3f6`](https://github.com/sgl-project/sglang/commit/65d76bd3f6) [#28075](https://github.com/sgl-project/sglang/pull/28075)
  [AMD] Fix CI base-a `fwd_occupancy`: disable `SGLANG_SANITIZE_NAN_LOGITS` in AMD CI (#28075)
  _Files: `scripts/ci/amd/amd_ci_exec.sh`, `test/registered/core/test_basic_sanity.py`_
- **2026-06-12** [`cce35ee2e5`](https://github.com/sgl-project/sglang/commit/cce35ee2e5) [#27994](https://github.com/sgl-project/sglang/pull/27994)
  Remove outdated patch (#27994)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-06-11** [`99ab90c5b7`](https://github.com/sgl-project/sglang/commit/99ab90c5b7) [#27811](https://github.com/sgl-project/sglang/pull/27811)
  [AMD] Restore AMD piecewise CUDA graph support dropped by #23906 (#27811)
  _Files: `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/runner/prefill_cuda_graph_runner.py`, `python/sglang/srt/model_executor/runner_backend/tc_piecewise_cuda_graph_backend.py`, `python/sglang/srt/model_executor/runner_backend_utils/tc_piecewise_cuda_graph/context_manager.py`_
- **2026-06-10** [`0da18f8d91`](https://github.com/sgl-project/sglang/commit/0da18f8d91) [#27656](https://github.com/sgl-project/sglang/pull/27656)
  [AMD][Perf] Fuse QK RMSNorm + gate extraction Triton kernel for Qwen3.5 on HIP (#27656)
  _Files: `python/sglang/jit_kernel/tests/test_fused_qk_gemma_rmsnorm_gate.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/utils.py`_
- **2026-06-10** [`4faaa9ba92`](https://github.com/sgl-project/sglang/commit/4faaa9ba92) [#27803](https://github.com/sgl-project/sglang/pull/27803)
  [CI] Fix stale ngram bookkeeping owner sites (#27803)
  _Files: `test/registered/unit/spec/test_decode_bookkeeping_ownership.py`_
- **2026-06-10** [`b0d888a195`](https://github.com/sgl-project/sglang/commit/b0d888a195) [#27795](https://github.com/sgl-project/sglang/pull/27795)
  [CI] Remove AMD DSv4 Docker publish job (#27795)
  _Files: `.github/workflows/release-docker-amd-rocm720-nightly.yml`_
- **2026-06-10** [`4704b10d0d`](https://github.com/sgl-project/sglang/commit/4704b10d0d) [#27669](https://github.com/sgl-project/sglang/pull/27669)
  [AMD] Update MoRI to v1.2.0 (#27669)
  _Files: `docker/rocm.Dockerfile`_
- **2026-06-10** [`f332e52611`](https://github.com/sgl-project/sglang/commit/f332e52611) [#27710](https://github.com/sgl-project/sglang/pull/27710)
  Add UT guarding per-request bookkeeping clock ownership (#27710)
  _Files: `test/registered/unit/spec/test_decode_bookkeeping_ownership.py`_
- **2026-06-09** [`9ab7a64ee1`](https://github.com/sgl-project/sglang/commit/9ab7a64ee1) [#27660](https://github.com/sgl-project/sglang/pull/27660)
  [AMD] Update amd qwen3.5 cookbook (#27660)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs_new/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-06-08** [`3607cbd65a`](https://github.com/sgl-project/sglang/commit/3607cbd65a) [#27555](https://github.com/sgl-project/sglang/pull/27555)
  [AMD] update ROCm AITER commit (#27555)
  _Files: `docker/rocm.Dockerfile`_
- **2026-06-08** [`df6b9c2d9d`](https://github.com/sgl-project/sglang/commit/df6b9c2d9d) [#27538](https://github.com/sgl-project/sglang/pull/27538)
  [AMD] ci: reinstall MoRI if Different from Dockerfile-pinned commit during install_dependency (#27538)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-06-08** [`1aa5040c74`](https://github.com/sgl-project/sglang/commit/1aa5040c74) [#27530](https://github.com/sgl-project/sglang/pull/27530)
  Update code owners (AMD) (#27530)
  _Files: `.github/CODEOWNERS`_

## CI / Build  (14 commits)

- **2026-06-14** [`5da3b37a9d`](https://github.com/sgl-project/sglang/commit/5da3b37a9d) [#26902](https://github.com/sgl-project/sglang/pull/26902)
  [CI] add Precision Regression Test on Nightly Run CI (#26902)
  _Files: `.github/workflows/nightly-test-nvidia.yml`, `docs_new/docs.json`, `docs_new/docs/references/nightly_precision_regression.mdx`, `python/sglang/test/precision_baseline_store.py` _+4 more__
- **2026-06-12** [`fd977adbd6`](https://github.com/sgl-project/sglang/commit/fd977adbd6) [#27785](https://github.com/sgl-project/sglang/pull/27785)
  Fix PR-close cancellation skipping workflows beyond the first 30 (#27785)
  _Files: `.github/workflows/cancel-pr-workflow-on-merge.yml`, `.github/workflows/cancel-pr-workflows-on-close.yml`_
- **2026-06-12** [`fe887e6935`](https://github.com/sgl-project/sglang/commit/fe887e6935) [#27861](https://github.com/sgl-project/sglang/pull/27861)
  test(xpu): add multi-feature and embedding stage-b tests (#27861)
  _Files: `.github/workflows/pr-test-xpu.yml`, `test/registered/xpu/test_xpu_embedding.py`, `test/registered/xpu/test_xpu_serving_features.py`_
- **2026-06-11** [`493f828bfa`](https://github.com/sgl-project/sglang/commit/493f828bfa) [#27075](https://github.com/sgl-project/sglang/pull/27075)
  Add DeepGEMM prerelease wheel tests (#27075)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-06-11** [`7e245afefe`](https://github.com/sgl-project/sglang/commit/7e245afefe) [#27909](https://github.com/sgl-project/sglang/pull/27909)
  [CI] Fix registered sigmoid gate mul test location (#27909)
  _Files: `test/registered/jit/test_sigmoid_gate_mul.py`_
- **2026-06-11** [`2a51479a91`](https://github.com/sgl-project/sglang/commit/2a51479a91) [#27860](https://github.com/sgl-project/sglang/pull/27860)
  ci(xpu): pull intel/sglang-dev:latest and clean workspace properly (#27860)
  _Files: `.github/workflows/pr-test-xpu.yml`, `scripts/ci/xpu/xpu_ci_start_container.sh`_
- **2026-06-11** [`57907cff97`](https://github.com/sgl-project/sglang/commit/57907cff97) [#27157](https://github.com/sgl-project/sglang/pull/27157)
  docker(xeon): support running container as non-root user (#27157)
  _Files: `docker/xeon.Dockerfile`_
- **2026-06-11** [`e113d884d0`](https://github.com/sgl-project/sglang/commit/e113d884d0) [#27703](https://github.com/sgl-project/sglang/pull/27703)
  ci(xpu): checkout deadicated dir for night build (#27703)
  _Files: `.github/workflows/release-docker-intel-xpu-nightly.yml`_
- **2026-06-10** [`125ef88892`](https://github.com/sgl-project/sglang/commit/125ef88892) [#27838](https://github.com/sgl-project/sglang/pull/27838)
  Disable async assert in Nemotron nightly tests (#27838)
  _Files: `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`, `test/registered/8-gpu-models/test_nvidia_nemotron_3_super_nightly.py`_
- **2026-06-10** [`1a5775a9df`](https://github.com/sgl-project/sglang/commit/1a5775a9df) [#27766](https://github.com/sgl-project/sglang/pull/27766)
  [Docs] Remove the legacy release-docs.yml deploy workflow (#27766)
  _Files: `.github/workflows/release-docs.yml`_
- **2026-06-10** [`6110ed671f`](https://github.com/sgl-project/sglang/commit/6110ed671f) [#27648](https://github.com/sgl-project/sglang/pull/27648)
  ci(xpu): clean build artifacts in cleanup (#27648)
  _Files: `.github/workflows/pr-test-xpu.yml`, `scripts/ci/xpu/xpu_ci_start_container.sh`_
- **2026-06-10** [`bcd9c5a903`](https://github.com/sgl-project/sglang/commit/bcd9c5a903) [#27133](https://github.com/sgl-project/sglang/pull/27133)
  update pytorch-xpu to 2.12 (#27133)
  _Files: `docker/xpu.Dockerfile`, `docs_new/docs/hardware-platforms/xpu.mdx`, `python/pyproject_xpu.toml`_
- **2026-06-09** [`f6e6394d86`](https://github.com/sgl-project/sglang/commit/f6e6394d86) [#27627](https://github.com/sgl-project/sglang/pull/27627)
  ci: run pr-test-extra on release branch cuts (not just base suites) (#27627)
  _Files: `.github/workflows/pr-test.yml`_
- **2026-06-09** [`9c53031d2b`](https://github.com/sgl-project/sglang/commit/9c53031d2b) [#27621](https://github.com/sgl-project/sglang/pull/27621)
  ci: partition the H200 nightly 'Run test' step across the matrix (#27621)
  _Files: `.github/workflows/nightly-test-nvidia.yml`_

## Models  (12 commits)

- **2026-06-13** [`29128f31fd`](https://github.com/sgl-project/sglang/commit/29128f31fd) [#27663](https://github.com/sgl-project/sglang/pull/27663)
  [NPU] Best Practice Docs Splitting (#27663)
  _Files: `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_r1.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/deepseek_v3_2.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/best_practice/glm5_1.mdx` _+10 more__
- **2026-06-13** [`29ac249be1`](https://github.com/sgl-project/sglang/commit/29ac249be1) [#27845](https://github.com/sgl-project/sglang/pull/27845)
  docs: add cookbook-migrate-model skill from the Qwen3.5 pilot (#27845)
  _Files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/references/engine-axis.md`, `.claude/skills/cookbook-add-model/references/mintlify-authoring.md` _+5 more__
- **2026-06-12** [`cb9140ee61`](https://github.com/sgl-project/sglang/commit/cb9140ee61) [#27941](https://github.com/sgl-project/sglang/pull/27941)
  Enable PDL for GPT-OSS tinygemm router (#27941)
  _Files: `python/sglang/srt/models/gpt_oss.py`_
- **2026-06-11** [`1ac75c3463`](https://github.com/sgl-project/sglang/commit/1ac75c3463) [#27955](https://github.com/sgl-project/sglang/pull/27955)
  [CI] Fix GB300 TestDummyWithSBO crash: disable NaN assert and coredump for dummy weights (#27955)
  _Files: `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`_
- **2026-06-11** [`43835b5ba5`](https://github.com/sgl-project/sglang/commit/43835b5ba5) [#27842](https://github.com/sgl-project/sglang/pull/27842)
  docs: cookbook benchmark accuracy labels come from the model config (no engine default) (#27842)
  _Files: `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/templates/config.jsx.tmpl`, `.claude/skills/cookbook-review-pr/SKILL.md`, `docs_new/src/snippets/_deployment.jsx` _+1 more__
- **2026-06-10** [`bdf3ef6421`](https://github.com/sgl-project/sglang/commit/bdf3ef6421) [#27839](https://github.com/sgl-project/sglang/pull/27839)
  [CI] Fix registered QK Gemma RMSNorm test location (#27839)
  _Files: `test/registered/jit/test_fused_qk_gemma_rmsnorm_gate.py`_
- **2026-06-10** [`3c1b0fb226`](https://github.com/sgl-project/sglang/commit/3c1b0fb226) [#27312](https://github.com/sgl-project/sglang/pull/27312)
  [1/n] [CP] Simplify prefill context parallel server args (#27312)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/arg_groups/deepseek_v4_hook.py`, `python/sglang/srt/server_args.py`, `test/manual/test_dsa_alias_cli_registry_env.py` _+1 more__
- **2026-06-10** [`99258b2f1e`](https://github.com/sgl-project/sglang/commit/99258b2f1e) [#27830](https://github.com/sgl-project/sglang/pull/27830)
  [Docs] Restore right-hand ToC on the DeepSeek-V4 cookbook page (#27830)
  _Files: `.claude/skills/cookbook-add-model/references/mintlify-authoring.md`, `.claude/skills/cookbook-add-model/templates/page.mdx.tmpl`, `.claude/skills/cookbook-review-pr/SKILL.md`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`_
- **2026-06-10** [`f3ecc3688f`](https://github.com/sgl-project/sglang/commit/f3ecc3688f) [#25794](https://github.com/sgl-project/sglang/pull/25794)
  Fix Gemma3 ModelOpt kv-scale loading (#25794)
  _Files: `python/sglang/srt/models/gemma3_causal.py`_
- **2026-06-09** [`0f8673851c`](https://github.com/sgl-project/sglang/commit/0f8673851c) [#27342](https://github.com/sgl-project/sglang/pull/27342)
  test: fix gemma GSM8K thresholds in nightly text eval (#27342)
  _Files: `test/registered/eval/test_text_models_gsm8k_eval.py`_
- **2026-06-08** [`d1777d1f6d`](https://github.com/sgl-project/sglang/commit/d1777d1f6d) [#26885](https://github.com/sgl-project/sglang/pull/26885)
  Cookbook renovation (#26885)
  _Files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/references/engine-axis.md`, `.claude/skills/cookbook-add-model/references/mintlify-authoring.md` _+12 more__
- **2026-06-08** [`2d1856bf45`](https://github.com/sgl-project/sglang/commit/2d1856bf45) [#10950](https://github.com/sgl-project/sglang/pull/10950)
  Support encoder_decoder on cpu_graph_runner (#10950)
  _Files: `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/models/mllama.py`_

## Quantization  (12 commits)

- **2026-06-13** [`eb18416f9f`](https://github.com/sgl-project/sglang/commit/eb18416f9f) [#27449](https://github.com/sgl-project/sglang/pull/27449)
  [jit-kernel] Support per token group quant 8bit v2 jit kernel (#27449)
  _Files: `python/sglang/jit_kernel/csrc/gemm/per_token_group_quant_8bit_v2.cuh`, `python/sglang/jit_kernel/per_token_group_quant_8bit_v2.py`, `python/sglang/srt/layers/quantization/fp8_kernel.py`, `test/registered/jit/benchmark/bench_per_token_group_quant_8bit_v2.py` _+1 more__
- **2026-06-12** [`c80d8fe78a`](https://github.com/sgl-project/sglang/commit/c80d8fe78a) [#27896](https://github.com/sgl-project/sglang/pull/27896)
  [Perf] Skip per-call mat_a/scales_a padding in cutlass FP8 blockwise GEMM (#27896)
  _Files: `python/sglang/srt/layers/quantization/fp8_kernel.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `test/registered/quant/test_fp8_blockwise_row_padding.py`_
- **2026-06-12** [`8bfcc0c39c`](https://github.com/sgl-project/sglang/commit/8bfcc0c39c) [#27956](https://github.com/sgl-project/sglang/pull/27956)
  Use the correct wrapper for `fp4_quantize` (#27956)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-06-11** [`b2728bda9d`](https://github.com/sgl-project/sglang/commit/b2728bda9d) [#27590](https://github.com/sgl-project/sglang/pull/27590)
  [diffusion] feat: use fused w8a8 kernel for Ideogram4 weight-only linear as an opt-in (#27590)
  _Files: `docs_new/docs/sglang-diffusion/environment_variables.mdx`, `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/weight_only_fp8.py`, `python/sglang/multimodal_gen/runtime/models/encoders/qwen3vl.py` _+1 more__
- **2026-06-11** [`66989a7642`](https://github.com/sgl-project/sglang/commit/66989a7642) [#27782](https://github.com/sgl-project/sglang/pull/27782)
  Fix gpt-oss-20b with mxfp4 support for Xeon (#27782)
  _Files: `python/sglang/srt/layers/quantization/__init__.py`_
- **2026-06-10** [`f42a093261`](https://github.com/sgl-project/sglang/commit/f42a093261) [#27722](https://github.com/sgl-project/sglang/pull/27722)
  [AMD] Migrate 2-GPU kernel allreduce tests into the registered system (#27722)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/jit/test_activation.py`, `test/registered/jit/test_amd_deterministic_custom_allreduce.py` _+3 more__
- **2026-06-09** [`17d8c5801d`](https://github.com/sgl-project/sglang/commit/17d8c5801d) [#27505](https://github.com/sgl-project/sglang/pull/27505)
  [AMD] Fix test_deepseek_r1_mxfp4_8gpu.py : disable async-assert probes on AMD CI (#27505)
  _Files: `scripts/ci/amd/amd_ci_exec.sh`_
- **2026-06-09** [`d7c8b9ab9f`](https://github.com/sgl-project/sglang/commit/d7c8b9ab9f) [#27533](https://github.com/sgl-project/sglang/pull/27533)
  [Intel GPU] Enable fused_experts in fp8.py for quantized models on XPU (#27533)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`_
- **2026-06-08** [`dc24a26821`](https://github.com/sgl-project/sglang/commit/dc24a26821) [#27528](https://github.com/sgl-project/sglang/pull/27528)
  Fix GPT-OSS MXFP4 hidden size reshape on SM10X (#27528)
  _Files: `python/sglang/srt/models/gpt_oss.py`_
- **2026-06-08** [`593eb2e0fa`](https://github.com/sgl-project/sglang/commit/593eb2e0fa) [#27577](https://github.com/sgl-project/sglang/pull/27577)
  [NPU] Fix CI (#27577)
  _Files: `test/registered/ascend/basic_function/quant/test_npu_w4a4_quantization.py`_
- **2026-06-08** [`40030d8af8`](https://github.com/sgl-project/sglang/commit/40030d8af8) [#24689](https://github.com/sgl-project/sglang/pull/24689)
  [NPU] Add GitHub test summary and deduplicate test code. Part 2 (#24689)
  _Files: `.github/CODEOWNERS`, `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/test_ascend_utils.py`, `python/sglang/test/ascend/test_mmlu.py` _+8 more__
- **2026-06-08** [`5bf7dd8e4a`](https://github.com/sgl-project/sglang/commit/5bf7dd8e4a) [#27496](https://github.com/sgl-project/sglang/pull/27496)
  Update SGLang diffusion skills (#27496)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-ako4all-kernel/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-ako4all-kernel/references/ako-loop.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-ako4all-kernel/scripts/ensure_ako4all_clean.sh` _+6 more__

## Scheduler / Batching  (10 commits)

- **2026-06-14** [`8c334e2224`](https://github.com/sgl-project/sglang/commit/8c334e2224) [#26971](https://github.com/sgl-project/sglang/pull/26971)
  fix(io_struct): index extra_key per sub-request in batched GenerateReqInput (#26971)
  _Files: `python/sglang/srt/managers/io_struct.py`, `test/registered/unit/managers/test_io_struct.py`_
- **2026-06-14** [`b796338271`](https://github.com/sgl-project/sglang/commit/b796338271) [#25975](https://github.com/sgl-project/sglang/pull/25975)
  Fix prefill delayer wait histograms always observing 0 (#25975)
  _Files: `python/sglang/srt/managers/prefill_delayer.py`, `test/registered/scheduler/test_prefill_delayer.py`_
- **2026-06-13** [`f4029d0fc0`](https://github.com/sgl-project/sglang/commit/f4029d0fc0) [#26009](https://github.com/sgl-project/sglang/pull/26009)
  [HiCache] fix: clear storage reset state (#26009)
  _Files: `python/sglang/srt/managers/cache_controller.py`_
- **2026-06-13** [`335a9c7837`](https://github.com/sgl-project/sglang/commit/335a9c7837) [#28088](https://github.com/sgl-project/sglang/pull/28088)
  fix(frontend): return HTTP 400 for out-of-vocabulary token_ids_logprob (#28088)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/openai_server/validation/test_request_length_validation.py`_
- **2026-06-11** [`949326d922`](https://github.com/sgl-project/sglang/commit/949326d922) [#27967](https://github.com/sgl-project/sglang/pull/27967)
  Add SGLANG_ENABLE_WAR_BARRIER to force-enable the overlap scheduler WAR barrier on non-CUDA (e.g. AMD) (#27967)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-06-09** [`7f730edfdc`](https://github.com/sgl-project/sglang/commit/7f730edfdc) [#22367](https://github.com/sgl-project/sglang/pull/22367)
  fix: correct off-by-one in vocab boundary check for token validation (#22367)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/unit/managers/test_vocab_boundary_finish.py`_
- **2026-06-08** [`eb646c7b78`](https://github.com/sgl-project/sglang/commit/eb646c7b78) [#27363](https://github.com/sgl-project/sglang/pull/27363)
  [srt] Add sglang:weight_load_duration_seconds gauge with source label (#27363)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/weight_updater.py`, `python/sglang/srt/observability/metrics_collector.py`_
- **2026-06-08** [`f746e4a608`](https://github.com/sgl-project/sglang/commit/f746e4a608) [#26999](https://github.com/sgl-project/sglang/pull/26999)
  Fix fill_len asymmetric assignment statement in ignore-eos branch (#26999)
  _Files: `python/sglang/srt/managers/schedule_policy.py`_
- **2026-06-08** [`9034c2f9ae`](https://github.com/sgl-project/sglang/commit/9034c2f9ae) [#26659](https://github.com/sgl-project/sglang/pull/26659)
  Fix Req fill_len (fill_ids) having dual semantics by restricting to truncated/committed semantics (#26659)
  _Files: `python/sglang/srt/dllm/mixin/req.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-06-08** [`4201de11de`](https://github.com/sgl-project/sglang/commit/4201de11de) [#26548](https://github.com/sgl-project/sglang/pull/26548)
  Extract release_req and retract_all as module-level free functions (#26548)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_

## Structured Output  (3 commits)

- **2026-06-14** [`f2d7d67603`](https://github.com/sgl-project/sglang/commit/f2d7d67603) [#26983](https://github.com/sgl-project/sglang/pull/26983)
  numa: bind within allowed CPUs when affinity is already constrained (#26983)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/utils/numa_utils.py`, `test/registered/utils/test_numa_utils.py`_
- **2026-06-13** [`8a9f2aa116`](https://github.com/sgl-project/sglang/commit/8a9f2aa116) [#23653](https://github.com/sgl-project/sglang/pull/23653)
  fix: prevent stale bitmask leakage in LLGuidance grammar backend (#23653)
  _Files: `python/sglang/srt/constrained/llguidance_backend.py`_
- **2026-06-09** [`365b7dab9a`](https://github.com/sgl-project/sglang/commit/365b7dab9a) [#27017](https://github.com/sgl-project/sglang/pull/27017)
  fix(schema): update tokens_after_end (#27017)
  _Files: `python/sglang/srt/constrained/reasoner_grammar_backend.py`_

## LoRA  (2 commits)

- **2026-06-10** [`21647f1f5d`](https://github.com/sgl-project/sglang/commit/21647f1f5d) [#27386](https://github.com/sgl-project/sglang/pull/27386)
  [router] Apply chat template before cache-aware hashing (fix overlap=0 on chat traffic) (#27386)
  _Files: `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/src/policies/cache_aware_zmq.rs`, `experimental/sgl-router/src/tokenizer/adapter.rs`, `experimental/sgl-router/src/tokenizer/chat_template.rs` _+5 more__
- **2026-06-09** [`dff695c76b`](https://github.com/sgl-project/sglang/commit/dff695c76b) [#27597](https://github.com/sgl-project/sglang/pull/27597)
  [lora] Exclude finished requests from running_loras (#27597)
  _Files: `python/sglang/srt/managers/scheduler.py`_

## Serving / API  (1 commits)

- **2026-06-12** [`b0b8436f1c`](https://github.com/sgl-project/sglang/commit/b0b8436f1c) [#28095](https://github.com/sgl-project/sglang/pull/28095)
  [Fix] Unquote ResponseTool annotation breaking lint on all PRs (#28095)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`_

---
_Generated 2026-06-15 14:33 UTC_